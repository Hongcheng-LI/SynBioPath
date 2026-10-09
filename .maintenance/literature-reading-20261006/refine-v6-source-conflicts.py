from pathlib import Path
d=Path(__file__).parent
p=d/'sources'/'V6BKYU8Q'/'codex-report.md'
s=p.read_text(encoding='utf-8').replace('图标示 19.7%，正文取整。','图标示 19.7%，正文取整。但 Figure 4 将这一重叠组分标为 H11β/H13α，而正文写 H11α/H13α，α/β 存在内部冲突；本文不能自行统一。').replace('作者最初将含氟产物 H1β','Table 2 的 H18Z 写 δ 4.71，而 Table 1 的参考物 20 对应值为 δ 4.70，两表也有小差异。\n\n作者最初将含氟产物 H1β').replace('Scheme 2 将三个主要产物','Scheme 2 顶端写 7-fluoroGGPP (17)，而底物标题、合成定义及其他反应式为 6-fluoroGGPP；底物与环化产物的位置编号不可混同，这处图中文字矛盾保留。\n\nScheme 2 将三个主要产物')
p.write_text(s,encoding='utf-8')
p=d/'prepare-v6-codex.py'
s=p.read_text(encoding='utf-8').replace('[53,44,294,295]','[53,44,294,299]').replace('NOE19.7Figure4rounded20bodyH11alpha/H13alphaoverlapnotindependentexactsignalcontributions','NOE19.7Figure4rounded20body;Figure4H11beta/H13alphavsbodyH11alpha/H13alphaunresolved;overlapnotindependentexactcontributions;Table2H18Z4.71vsTable1reference204.70;Scheme2substratelabel7fluoroGGPP17vsdefined6fluoroGGPPunresolved')
p.write_text(s,encoding='utf-8')
