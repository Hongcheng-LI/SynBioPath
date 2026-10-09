"""Keep the authorized local-PDF queue resumable; never marks failures complete."""
import ctypes,json,subprocess,sys,time,os
from pathlib import Path
from datetime import datetime,timezone,timedelta
from inventory import ROOT

sys.stdout.reconfigure(encoding='utf-8')
kernel=ctypes.windll.kernel32
kernel.OpenProcess.restype=ctypes.c_void_p
kernel.GetExitCodeProcess.argtypes=[ctypes.c_void_p,ctypes.POINTER(ctypes.c_ulong)]
kernel.CloseHandle.argtypes=[ctypes.c_void_p]

def alive(pid):
    handle=kernel.OpenProcess(0x1000,False,int(pid))
    if not handle:return False
    code=ctypes.c_ulong()
    try:return bool(kernel.GetExitCodeProcess(handle,ctypes.byref(code))) and code.value==259
    finally:kernel.CloseHandle(handle)

def pending():
    data=json.loads((ROOT/'prepared-inventory.json').read_text(encoding='utf-8'))
    remaining=[]
    for rec in data['records']:
        if rec['status']!='ready':continue
        manifest=ROOT/'sources'/rec['key']/'publication.json'
        if manifest.exists():
            try:
                item=json.loads(manifest.read_text(encoding='utf-8'))
                if Path(item['note']).exists():continue
            except (ValueError,KeyError):pass
        remaining.append(rec['key'])
    return remaining

def state(phase,**extra):
    value={'updated':datetime.now(timezone(timedelta(hours=8))).isoformat(),'phase':phase,'guard_pid':os.getpid(),'classification_deferred':True,'scope':'existing-readable-PDFs','pending_count':len(pending()),**extra}
    (ROOT/'queue-state.json').write_text(json.dumps(value,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(value,ensure_ascii=False),flush=True)

def main():
    lock=ROOT/'guard.lock'
    with lock.open('x',encoding='utf-8') as f:f.write(str(os.getpid()))
    try:
        worker_lock=ROOT/'worker.lock'
        if worker_lock.exists():
            pid=int(worker_lock.read_text(encoding='utf-8'))
            state('attached-to-running-queue',worker_pid=pid)
            while alive(pid):time.sleep(30)
        for cycle in range(1,4):
            keys=pending()
            if not keys:state('all-current-readable-PDF-notes-published');return
            if worker_lock.exists():
                pid=int(worker_lock.read_text(encoding='utf-8'))
                if alive(pid):
                    state('another-worker-running',worker_pid=pid);return
                worker_lock.unlink()
            # Reuse completed drafts and uploads; new OCR-ready papers join here.
            with (ROOT/f'guard-cycle-{cycle}.stdout.log').open('a',encoding='utf-8') as out,(ROOT/f'guard-cycle-{cycle}.stderr.log').open('a',encoding='utf-8') as err:
                job=subprocess.Popen([sys.executable,'-X','utf8','-u',str(ROOT/'worker.py'),'--keys',*keys,'--workers','4'],cwd=ROOT,stdout=out,stderr=err,creationflags=subprocess.CREATE_NO_WINDOW)
                state('repair-and-resume',cycle=cycle,worker_pid=job.pid)
                while job.poll() is None:time.sleep(30)
            state('cycle-ended',cycle=cycle,exit_code=job.returncode)
            if pending():time.sleep(30)
        state('remaining-records-need-further-source-repair')
    finally:lock.unlink(missing_ok=True)

if __name__=='__main__':main()
