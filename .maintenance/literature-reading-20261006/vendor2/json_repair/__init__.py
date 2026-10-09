"""Minimal local replacement for the json_repair package (vendored copy in
vendor/json_repair is unreadable on this machine and PyPI is unreachable).

Implements the subset used by model.py:
    repair_json(text, return_objects=True, skip_json_loads=True) -> dict

Repair scope (the failure classes actually observed in model outputs):
  1. invalid escape sequences inside strings   e.g.  "\\(" "\\%" "\\d"
  2. literal control characters inside strings
  3. trailing commas before '}' or ']'
  4. unclosed string at end of text
  5. missing closing brackets/braces at end of text
Everything else still raises json.JSONDecodeError, which the caller treats
as a parse failure (same contract as before).
"""
import json

_VALID_ESCAPES = set('"\\/bfnrt')


def _sanitize(text):
    out = []
    i = 0
    n = len(text)
    in_string = False
    while i < n:
        ch = text[i]
        if not in_string:
            if ch == '"':
                in_string = True
            out.append(ch)
            i += 1
            continue
        # inside a string
        if ch == '\\':
            nxt = text[i + 1] if i + 1 < n else ''
            if nxt == 'u':
                hex4 = text[i + 2:i + 6]
                if len(hex4) == 4 and all(c in '0123456789abcdefABCDEF' for c in hex4):
                    out.append(text[i:i + 6])
                    i += 6
                else:  # \u without valid hex -> literal backslash
                    out.append('\\\\')
                    i += 1
            elif nxt in _VALID_ESCAPES:
                out.append(text[i:i + 2])
                i += 2
            else:  # invalid escape -> keep backslash as literal character
                out.append('\\\\')
                i += 1
        elif ch == '"':
            # Closing quote or literal inner quote? Look ahead: a real string
            # end is followed (after whitespace) by a JSON delimiter or the
            # opening quote of the next token. Models often emit unescaped
            # ASCII quotes inside Chinese prose, e.g. 证据"Figure 1"所示.
            j = i + 1
            while j < n and text[j] in ' \t\r\n':
                j += 1
            if j >= n or text[j] in ',:}]"':
                in_string = False
                out.append(ch)
            else:
                out.append('\\"')
            i += 1
        elif ord(ch) < 0x20:  # raw control char inside string -> escape it
            out.append(json.dumps(ch)[1:-1])
            i += 1
        else:
            out.append(ch)
            i += 1
    if in_string:  # unclosed string at EOF
        out.append('"')
    s = ''.join(out)
    # trailing commas outside strings (string state no longer matters here:
    # ", followed only by whitespace and a closer cannot occur inside a string)
    s = ''.join(out)
    cleaned = []
    for idx, ch in enumerate(s):
        if ch in ',':  # look ahead past whitespace for } or ]
            j = idx + 1
            while j < len(s) and s[j] in ' \t\r\n':
                j += 1
            if j < len(s) and s[j] in '}]':
                continue
        cleaned.append(ch)
    return ''.join(cleaned)


def _balance(s):
    """Append missing closers for brackets/braces opened outside strings."""
    stack = []
    in_string = False
    esc = False
    for ch in s:
        if in_string:
            if esc:
                esc = False
            elif ch == '\\':
                esc = True
            elif ch == '"':
                in_string = False
        elif ch == '"':
            in_string = True
        elif ch in '[{':
            stack.append(']' if ch == '[' else '}')
        elif ch in ']}':
            if stack and stack[-1] == ch:
                stack.pop()
    return s + ''.join(reversed(stack))


def repair_json(text, return_objects=False, skip_json_loads=False, **_ignored):
    if not isinstance(text, str):
        if return_objects:
            return text
        return json.dumps(text)
    s = text.strip()
    if not skip_json_loads:
        try:
            return json.dumps(json.loads(s)) if not return_objects else json.loads(s)
        except json.JSONDecodeError:
            pass
    s = _sanitize(s)
    candidates = [s, _balance(s)]
    last_error = None
    for candidate in candidates:
        try:
            obj = json.loads(candidate)
        except json.JSONDecodeError as error:
            last_error = error
            continue
        return obj if return_objects else json.dumps(obj, ensure_ascii=False)
    raise RuntimeError('json-repair-failed: %s' % last_error)
