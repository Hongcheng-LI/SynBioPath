---
type: literature-reading
zotero_key: 7V234D63
doi: "10.1002/biot.201600697"
paper_type: research
classification_status: pending
reading_status: main-text-and-figures-read
review_status: codex-source-checked
human_full_paper_review: false
source_attachment: IGNBLLSK
source_sha256: 9feb44c324dc9e3fd066d75a3ec8be34c9b79a84d6294465e84ec5a415c3c77a
created: 2026-10-10
---

> 原文来源：[Zotero 条目](zotero://select/library/items/7V234D63)；[DOI](https://doi.org/10.1002/biot.201600697)；由当前 Codex 读取原始主文并核对图表，尚未经人工逐项复核。 来源限制：SI Figure 1（A. alternata TPF6 中 MVA 通路转录水平）未提供原始图像，无法核实具体 FPKM 数值与基因 ID；SI Figure 2（pGB92–pGB99 系列启动子报告质粒图谱）未提供，无法核实质粒结构细节；SI Figure 3（T2 纯化 taxadiene 的 1H NMR 谱）未提供，无法核实信号归属；Supplementary Table 1（所用寡核苷酸列表）未提供，无法核实引物序列；正文未报告 GGPPS 蛋白水平、Taxadiene 标准曲线及 GB127 五次重复的具体数值分布。

# 一、基本信息

**文章题目**：Production of taxadiene by engineering of mevalonate pathway in *Escherichia coli* and endophytic fungus *Alternaria alternata* TPF6

**文章 DOI 号**：10.1002/biot.201600697

**期刊名称**：Biotechnology Journal

**通讯作者及工作单位**：

- **刘天罡**：武汉大学药学院，组合生物合成与药物发现教育部重点实验室 (Key Laboratory of Combinatorial Biosynthesis and Drug Discovery, Ministry of Education, and School of Pharmaceutical Sciences, Wuhan University)

---

# 二、研究背景

紫杉醇 (paclitaxel) 是 1971 年自短叶紫杉 (*Taxus brevifolia*) 树皮中分离得到的二萜类化合物，因其显著的抗癌活性长期用于临床。由于价格高昂且供应受限于红豆杉属植物，紫杉醇及其下游紫杉烷的微生物合成成为重要的替代路线。紫杉二烯 (taxadiene) 是该途径中第一个被环化酶 (TS) 催化形成的关键 C20 二萜骨架，由通用 C5 前体异戊烯基焦磷酸 (IPP) 与二甲基烯丙基焦磷酸 (DMAPP) 经牻牛儿基牻牛儿基焦磷酸合酶 (GGPPS) 与紫杉二烯合酶 (TS) 合成。

IPP/DMAPP 在自然界由两条独立的途径产生：依赖丙酮酸/甘油醛-3-磷酸的 2-C-甲基-D-赤藓糖醇-4-磷酸 (MEP) 途径，以及以乙酰辅酶 A 为前体的甲羟戊酸 (MVA) 途径。在大肠杆菌中通过多变量模块策略优化 MEP 途径，紫杉二烯产量可提升约 15,000 倍；随后在含 P450 系统下进一步获得氧化紫杉烷。然而，*E. coli* 中由 CYP725A4 介导的非特异性氧化副产物严重限制下游产量，且紫杉醇合成还需 7 步额外的 P450 氧化，存在严重的底盘局限。

丝状真菌由于生物量大、对 P450 等翻译后修饰酶友好，成为紫杉醇类二萜的理想替代宿主。课题组前期已在 *E. coli* 中通过 MVA 途径成功合成了法尼烯、番茄红素和虾青素，提示将模块化的 MVA 平台向真菌拓展具有可行性。

因此，本研究的核心问题是：**能否在丝状真菌 *Alternaria alternata* TPF6（已知可产紫杉醇的内生真菌）这一新底盘内复建 MVA 紫杉二烯合成途径，并通过理性代谢工程实现稳定的紫杉二烯生产？** 切入点在于搭建 *A. alternata* TPF6 的遗传操作系统（ATMT），评估异源启动子强度，并基于转录组学背景选择需补偿的 MVA 关键节点。

---

# 三、研究思路

作者将紫杉醇生产问题拆解为'前体供给—底盘选择—遗传操作—理性设计'四个层次，按照以下逻辑递进展开：

1. 先在已有 MVA 平台的 *E. coli* 中快速替换法尼烯模块为紫杉二烯模块（TS + GGPPS），验证技术路线的可行性，并比较不同拷贝数质粒的影响；
2. 对目标宿主 *A. alternata* TPF6 开展三样本转录组测序，明确其 MVA 通路中各基因的转录水平；
3. 建立 *A. alternata* TPF6 的根癌农杆菌介导转化 (ATMT) 方法，并以 GFP 报告系统量化 6 个常用真菌异源启动子的相对强度；
4. 依据 MVA 体外重构的最佳酶比例 (AtoB:ERG13:tHMG1:ERG12:ERG8:MVD1:Idi = 1:10:2:5:5:2:5) 和 *A. alternata* 自身 MVA 转录图谱，理性选择并组合表达 tHMG1、Idi 和 TS，构建紫杉二烯生产菌株 GB127；
5. 通过 GC-MS 与标品比对 (m/z 122、tR = 16.6 min) 验证产物，并完成从原核底盘到真核底盘的通路转化。

整体形成'模块借用—宿主适配—理性设计—产物验证'的完整闭环。

---

# 四、研究方法

- **质粒构建**：Gibson 组装、SOE-PCR 连接、'simple cloning' 直接转化方法，用于将 *TS*、*GGPPS*、*Idi*、*tHMG1* 等基因按不同启动子组合装入 pETDuet-1、pCAMBIA1301 等骨架。
- ***E. coli* 紫杉二烯生产**：以 BL21(DE3) 为宿主，LB + IPTG 诱导，摇瓶发酵，正己烷萃取后 GC-MS 检测，DCW 通过 OD600 换算（0.3 g DCW/OD600），并辅以 <sup>1</sup>H NMR 结构确认。
- **转录组测序**：PDB 培养基 3 天培养、3 个生物学重复，Illumina NEBNext Ultra RNA Library 建库，10612 个预测基因用于解析 MVA 通路转录水平。
- **ATMT 遗传操作系统**：以 PDA 斜面培养 28 天的分生孢子为受体，A. *tumefaciens* EHA105 + IM 诱导 6 h，Co-IM 共培养 3 天，潮霉素 B (50 mg/L) 筛选，连续三次继代培养并经 PCR 确证。
- **启动子强度评估**：6 个异源启动子分别驱动 *gfp* 报告基因，荧光显微观察（诱导培养基：alcA 用甘油+苏氨酸，glaA/agdA 用麦芽糖，trpC/gpdA/oliC 用低糖 PDA），并以 *gapdh* 为内参进行 qPCR 量化。
- ***A. alternata* 摇瓶发酵**：500 mL 摇瓶 / 100 mL PGT 培养基 (200 g/L 土豆、12.6 g/L 甘油、1 g/L 葡萄糖、3 g/L 苏氨酸)，28 ℃、250 rpm、14 天，hexane:EtOAc = 4:1 双相萃取，旋蒸后用正己烷复溶进行 GC-MS 检测。
- **GC-MS 检测**：Thermo TRACE GC ULTRA + TSQ QUANTUM XLS，TRACE TR-5MS (30 m × 0.25 mm × 0.25 μm) 色谱柱，升温程序 80 ℃ 1 min – 220 ℃ (10 ℃/min) – 220 ℃ 15 min；进样口 230 ℃，传输线 240 ℃，监测 *m/z* 122 等 taxadiene 特征离子。

---

# 五、实验设计及结果分析

### (一) 紫杉二烯合成途径的整体构架与底盘选择的理论依据

#### 实验目的与设计逻辑

作者在引入具体实验数据前先以路径图统一定义了 IPP/DMAPP 的两条来源途径，并明确指出在 *E. coli* 中沿 MEP 路线提升紫杉二烯虽已实现 15,000 倍放大，但下游 P450 介导的氧化步骤受 CYP725A4 非特异性影响，导致氧化紫杉烷生产受限。该图不仅给出两个途径在 *E. coli* 中并存的化学逻辑，也突出了在真核宿主中再走 MVA 路线的合理性，因为丝状真菌对 P450 等翻译后修饰酶更友好。

#### 实验结果与证据解析


![Figure 1 原文第 21 页](https://synbiopath.online/7V234D63-Figure-1-p21-1-0871c334ebcf09a4.png)

![Figure 1 原文第 22 页](https://synbiopath.online/7V234D63-Figure-1-p22-2-156171a16b1bcf46.png)

*Figure 1：紫杉二烯在 E. coli 与真菌中经 MEP 与 MVA 途径的合成路径示意；标注所有中间代谢物缩写及各步酶（包括 DXS/DXR/IspD–IspH 的 MEP 途径以及 ERG10/ERG13/HMGR/ERG12/ERG8/MVD1/Idi 的 MVA 途径），最终经 GGPPS 与 TS 形成 taxa-4(5),11(12)-diene。（原文 PDF 截图）。*


Figure 1 给出从 G3P/丙酮酸或乙酰辅酶 A 出发，经 MEP 或 MVA 途径汇聚到 IPP/DMAPP，再经 GGPPS 缩合为 GGPP，最终被 TS 环化形成 taxa-4(5),11(12)-diene 的整体化学路径。该图清晰地界定：**MVA 支路** 在酵母和多数真菌中已经天然运行，仅需补足 GGPP→taxadiene 的两步，而 *E. coli* 中天然仅具 MEP 支路，需要导入完整的 MVA 上游模块；这一差异直接决定了后文两条技术分支（一为同源 MEP 旁路扩展为 MVA，另一为在真菌中补足下游 GGPP+TS）。但作者基于课题组既往的 MVA 平台，**直接选择 MVA 路线在两个底盘分别尝试**，是该研究路径选择的关键解释。

### (二) 在 *E. coli* 中通过 MVA 路线生产紫杉二烯并比较拷贝数

#### 实验目的与设计逻辑

为快速获得一个可重复的紫杉二烯生产模块并验证 MVA 路线在 *E. coli* 中的可用性，作者把原 *E. coli* 法尼烯生产平台中的法尼烯合酶基因替换为 *TS* 与 *GGPPS*，并通过比较 TS/GGPPS 在低拷贝 (pSC101 复制子) 与高拷贝 (pBR322 复制子) 背景下的产量差异，探索质粒拷贝数对异源二萜产量的影响。

#### 实验结果与证据解析

Figure 2 与正文方法显示，作者将 *TS* + *GGPPS* 表达盒分别克隆到低拷贝 pXC02 与高拷贝 pFZ131，并分别与 MVA 上游模块质粒 pMH1 (*lacp:AtoB, ERG13, tHMG1*) 与 pFZ81 (*lacp:ERG12, ERG8, MVD1, Idi*) 共转化 BL21(DE3)，获得工程菌株 T2 (含 pXC02) 和 T4 (含 pFZ131)。上方的 Figure 2A 给出三个质粒上各基因盒的排列与所用启动子（*lac* 启动子驱动 MVA 上游，T7 启动子驱动 *TS*+*GGPPS*）；下方 Figure 2B 是摇瓶 8–72 h 的产量时程曲线。


![Figure 2 原文第 23 页](https://synbiopath.online/7V234D63-Figure-2-p23-1-bac2457e108142f8.png)

*Figure 2：E. coli 中紫杉二烯生产：A，比较不同拷贝数质粒（pXC02 vs pFZ131）下 TS 和 GGPPS 表达对紫杉二烯合成的影响；B，T2（pMH1/pFZ81/pXC02）与 T4（pMH1/pFZ81/pFZ131）在 8–72 h 摇瓶发酵过程中紫杉二烯产量（mg/L）的动态比较，显示三个生物学重复的均值±SD。（原文 PDF 截图）。*


数据直接支持以下三条结论：

1. **MVA 路线可在 *E. coli* 中合成紫杉二烯**：T2 最高产量 11.3 ± 0.5 mg/L（13.2 mg/gDCW），T4 最高产量 5.0 ± 0.7 mg/L（5.9 mg/gDCW），两者均通过 GC-MS 与 Phil S. Baran 提供的真品比对确认，T2 产物进一步经 <sup>1</sup>H NMR 鉴定（Supplementary Figure 3，本文未提供图像），证明峰归属的正确性。
2. **低拷贝优于高拷贝**：尽管直觉上提升 TS/GGPPS 拷贝数应提高产量，但实际 T2 的 taxadiene 时程曲线始终高于 T4，至 54 h 即达 11.3 mg/L，并在 64 h 略有回落后保持稳定。作者据此**经验性论证** —— 与此前法尼烯平台的工程经验一致 —— *TS* 与 *GGPPS* 高表达可能造成代谢负担或质粒不稳定性，但原文未在蛋白水平或质粒保持率层面给出进一步解释。
3. **E. coli 平台可作为后续真菌系统的对照基准**：作者明确将 T2 产量与已有文献 (Engels et al., 2008 在酵母中的低产 MVA 路线) 比较，认为 T2 的水平'相对可行'，从而将该平台作为模块化'紫杉二烯模块'向真菌迁移的技术基础。


![Figure 3 原文第 24 页](https://synbiopath.online/7V234D63-Figure-3-p24-1-9c5fc3cafdc93267.png)

*Figure 3：A. alternata TPF6 中异源启动子强度评估：A，6 株转化子（GB92 trpC、GB93 gpdA、GB94 alcA、GB96 oliC、GB98 glaA、GB99 agdA）的 GFP 荧光显微成像，比例尺 10 μm；B，qPCR 测定的 gfp 相对 mRNA 水平（log10 刻度，三个生物学重复的均值±SD），由弱到强排序为 gpdA<oliC<glaA<trpC<agdA<alcA，跨度超过 7,000 倍。（原文 PDF 截图）。*


值得注意的是，该部分并未报告 GGPP 中间体积累、IPP/DMAPP 池或 CYP725A4 等氧化副产物，因此**不能用于评估氧化副产物问题是否同样存在于 MVA 路线**。该局限在讨论部分亦被作者承认。

### (三) *A. alternata* TPF6 中 MVA 通路转录水平的背景刻画

#### 实验目的与设计逻辑

为决定在丝状真菌中应该强化哪些 MVA 节点、保留哪些节点，作者对 *A. alternata* TPF6 进行三样本转录组测序，并将各基因 FPKM 与前期 *in vitro* MVA 体外重构的经验性优化比例 (AtoB:ERG13:tHMG1:ERG12:ERG8:MVD1:Idi = 1:10:2:5:5:2:5) 进行比对。

#### 实验结果与证据解析

转录组结果 (Supplementary Figure 1，本文未提供图像) 显示 *erg10, erg13, erg12, erg8, mvd1, idi* 等 MVA 上游与中游基因在 TPF6 中的转录水平与体外重构的'足以供给 IPP/DMAPP 的水平'相当；而 *hmg1*（HMG-CoA 还原酶，与甾醇反馈抑制相关）的转录水平则明显偏低。这些转录组结果支持 TPF6 中存在 MVA 通路相关基因表达，并提示 *hmg1* 转录水平相对偏低。作者将这一观察与真菌中的甾醇负反馈调控联系起来，但本文没有测定 Hmg1 蛋白/酶活、MVA 中间体或通量，因此不能仅凭转录水平把 Hmg1 定为已验证的唯一限速酶。作者据此把截短 *tHMG1* 与 *Idi*、*TS* 组合过表达作为候选工程策略。Supplementary Figure 1 未提供，正文也没有列出具体 FPKM 数值，故无法独立复核各基因表达量及组间差异。

### (四) 在 *A. alternata* TPF6 中建立 ATMT 遗传操作系统与异源启动子强度评估

#### 实验目的与设计逻辑

丝状真菌的代谢工程长期受限于缺乏可靠的遗传操作工具与系统化的启动子库。作者将 *A. tumefaciens* EHA105 介导的 ATMT 引入 TPF6，并以 GFP 为报告基因量化 6 个常用真菌启动子的相对强度，为后续 MVA 关键酶的精细调控提供依据。

#### 实验结果与证据解析

Table 1 列出 6 株 GFP 报告株 (GB92–GB99)，分别由 *trpC, gpdA, alcA, oliC, glaA, agdA* 启动子驱动。Figure 3A 的 GFP 荧光显微图像显示 *alcA* 启动子（GB94）荧光强度显著高于其余 5 个，且其余菌株间荧光差异在可视化层面并不明显。Figure 3B 的 qPCR 量化则提供更精细的层级：**alcA (3.4 × 10<sup>7</sup>) > agdA > trpC > glaA > oliC > gpdA (4.5 × 10<sup>3</sup>)**；跨度超过 7,000 倍。该结果直接证明：


![Table 1 原文第 20 页](https://synbiopath.online/7V234D63-Table-1-p20-1-c1cf8f2cab55bb59.png)

*Table 1：本研究使用的菌株与质粒一览（含 BL21(DE3) 系列、EHA105、链格孢菌 TPF6 及 GB92–GB127 系列衍生株，以及 pMH1、pFZ81、pFZ131、pXC02、pCAMBIA-1301、pGB86–pGB127 系列质粒）。（原文 PDF 截图）。*


1. *trpC, gpdA, oliC* 为组成型启动子；*alcA* 受葡萄糖抑制、在甘油+苏氨酸下强诱导；*glaA*、*agdA* 在麦芽糖下诱导，这三类调控谱为后续在不同代谢背景下灵活调整酶量提供了可用元件。
2. **alcA 启动子强度远超其他**，作者据此选择 *alcA* 驱动关键的下游酶 *TS*（环化反应直接决定产物形成）。

值得注意的是，原文使用了三种不同条件 (alcA 用甘油+苏氨酸，glaA/agdA 用麦芽糖，其余用低糖 PDA) 来匹配各启动子的'诱导态'进行比较。这意味着 Figure 3B 的柱高并非严格意义下'同一条件下的稳态对比'，而是'各启动子在最适诱导条件下的表达水平'。这是该实验设计中**需要在解读时注意的重要语境**：所报告的跨度大于 7,000 倍反映的是'启动子表达潜力的差异'，而非'在恒定培养条件下 *alcA* 与 *gpdA* 的瞬时强度比'。这并未被作者单独注明，本文在此明确指出。

### (五) 紫杉二烯生产株的逐步构建与 GC-MS 检测

#### 实验目的与设计逻辑

依据上一节的启动子强度排序与 MVA 体外重构比例，作者构建了三个递进工程菌：

- GB123：*alcAp-TS*（仅导入下游紫杉二烯合酶）；
- GB125：*trpCp-Idi* + *alcAp-TS*（补足 IPP/DMAPP 异构酶）；
- GB127：*trpCp-Idi* + *oliCp-tHMG1* + *alcAp-TS*（再过表达解除反馈的 HMG-CoA 还原酶）。

这一组递进构建用于测试在导入 *TS* 的基础上，再加入 *Idi*，以及进一步加入 *tHMG1* 后，是否能使产物达到 GC-MS 检测水平。由于 GB127 与 GB125 的主要构建差异是增加 *tHMG1* 表达盒，结果可支持该组合对可检测产物形成有贡献；但没有直接测定酶活、前体池或通量，也没有对各因子进行完整的单独/组合拆分，因而不能据此唯一定位限速步骤。

#### 实验结果与证据解析

Figure 4A 展示了 T-DNA 构建：pGB123 导入 *alcAp-TS*，pGB125 在此基础上加入 *trpCp-Idi-Aa-niaDt*，pGB127 再加入 *oliCp-tHMG1-Aa-agdAt*（构建详情见 Table 1）。Figure 4B 的 *m/z* 122 提取离子色谱在约 16.6 min 处仅显示 GB127 与 taxadiene 标准品的对应峰，野生型、GB123 和 GB125 在该检测条件下未见相应可检出峰。Figure 4C 中 GB127 与标准品的质谱主要碎片模式相符，支持产物鉴定为 taxadiene。


![Figure 4 原文第 25 页](https://synbiopath.online/7V234D63-Figure-4-p25-1-d1bc23d6a01fb1d3.png)

*Figure 4：紫杉二烯生产相关 T-DNA 载体构建及 GC-MS 检测：A，pGB123/125/127 三种 T-DNA 载体结构（CAMV-HPTII 筛选盒 + alcAp-TS 表达盒，并依次加入 trpCp-Idi-niaDt 与 oliCp-tHMG1-agdAt 元件）；B，野生型 TPF6、GB123、GB125、GB127 及紫杉二烯标品在 16–17.2 min 区间的总离子计数（TIC）色谱图，taxadiene 信号标记于 16.60 min；C，GB127 与标品 taxadiene 的质谱图（m/z 122 等碎片），两者碎片模式一致。（原文 PDF 截图）。*


在本文的检测条件下，野生型、GB123 与 GB125 未检出 taxadiene，而 GB127 在发酵 14 天后达到 61.9 ± 6.3 μg/L；作者报告该结果在五次平行实验中重现。实验直接支持的是 *Idi*、*tHMG1* 与 *TS* 这一组合能够在 TPF6 中形成可检测的 taxadiene。GB125 与 GB127 的差异提示增加 *tHMG1* 表达可能有贡献，但本文没有测定 HMGR 酶活或通路通量，因此“Hmg1 是唯一限速步骤”仍属于机制推断，不能写成已直接证明的结论。

同一研究中，*E. coli* T2 的摇瓶滴度为 11.3 ± 0.5 mg/L，约为 GB127 的 180 倍；该比值仅是不同宿主/构建和培养条件下的描述性对照，不等同于严格的工艺效率比较。作者讨论提出的染色质调控与内源萜类途径竞争 GGPP 是可能解释，本文未通过基因扰动或通量测量验证这些机制。

---

# 六、总体结论

**该研究通过递进策略，在 *E. coli* 与丝状真菌 *A. alternata* TPF6 中分别建立了基于 MVA 途径的紫杉二烯生产系统。** 在 *E. coli* 中，作者将课题组既有的法尼烯模块替换为 *TS* + *GGPPS*，获得 T2 工程菌（11.3 ± 0.5 mg/L taxadiene，13.2 mg/gDCW），验证 MVA 路线在该底盘的可行性。

在丝状真菌中，作者首先通过 ATMT 首次为 *A. alternata* TPF6 建立了稳定的遗传操作系统，并以 GFP 报告与 qPCR 量化证明 *alcA*、*agdA*、*trpC*、*glaA*、*oliC*、*gpdA* 六种异源启动子在 TPF6 中均能工作且相对强度跨度超过 7,000 倍。基于此，结合 *in vitro* MVA 的最佳酶比例 (AtoB:ERG13:tHMG1:ERG12:ERG8:MVD1:Idi = 1:10:2:5:5:2:5)，作者设计 *trpCp-Idi / oliCp-tHMG1 / alcAp-TS* 三段表达盒组合，获得 GB127 工程菌（61.9 ± 6.3 μg/L），作者将其报告为丝状真菌中首次观察到紫杉二烯生物合成；这一文献优先权表述属于作者结论，本笔记未独立系统检索验证。

该项工作的核心学术贡献在于：**(i) 将 MVA 紫杉二烯模块从原核底盘成功迁移到丝状真菌新底盘；(ii) 为后续紫杉醇生物合成中 P450 介导的氧化步骤提供可控的真核表达系统；(iii) 将 ATMT 与六种异源启动子的强度评估打包为一组可复用的 *Alternaria* 遗传操作工具集。**

---

# 七、论文评价

### 优点与创新

本文的核心创新在于**首次将紫杉二烯生产从原核及酵母底盘向丝状真菌 *A. alternata* TPF6 拓展**，并为该底盘配套建立了 ATMT 遗传操作系统与启动子强度档案。作者依据有限的转录组信息与 *in vitro* MVA 优化比例做出理性设计而非穷举筛选，体现出明确的'计算/先验信息辅助工程决策'理念。GB127 5 次独立实验的稳定检测佐证了产物的可重复性，结合 *m/z* 122 提取离子色谱与 taxadiene 真品的保留时间和质谱碎片高度吻合，**关键产物的化学确证较为充分**。

### 未来研究方向

为巩固该平台的下游应用，应优先解答以下问题：**在 *A. alternata* TPF6 中，HMG-CoA 还原酶反馈调控之外是否还存在其他限速步骤？** 建议后续在 GB127 基础上：(i) 进行 *<sup>13</sup>C* 标记葡萄糖或乙酸示踪实验，定量 IPP/DMAPP 池的实际流量；(ii) 通过 RNA-seq 评估 *trpC/oliC/alcA* 启动子在该宿主中的稳态表达水平，并通过调整酶剂量 (tHMG1 拷贝数) 与更换更强启动子验证 HMG1 是否仍为唯一定量瓶颈，从而定量区分是真菌全局调控还是单一酶反馈抑制限制了产量。

---

# 八、关键问题及回答

**Q1：为什么 GB123 与 GB125 未检出 taxadiene，而 GB127 可以检出？**

**A**：原文直接报告，在所用培养与 GC-MS 检测条件下，只有同时表达 *Idi*、*tHMG1* 和 *TS* 的 GB127 出现可鉴定信号（61.9 ± 6.3 μg/L；五次平行实验重现）。这一比较支持该工程组合能使 TPF6 达到可检测产物水平，也提示 *tHMG1* 的加入可能提高前体供给；但未测定 HMGR 活性或代谢通量，也没有完整拆分 *Idi*、*tHMG1*、*TS* 与 GGPP 供给的单因素效应。因此，“Hmg1 是唯一限速步骤”属于作者提出的机制解释，证据强度低于直接证明。

**Q2：Figure 3 中报告的启动子强度'大于 7,000 倍跨度'是否具有直接可比性？**

**A**：Figure 3 的 qPCR 数据（GB93 *gpdA* = 4.5 × 10<sup>3</sup> 至 GB94 *alcA* = 3.4 × 10<sup>7</sup>）确实呈现出 >7,000 倍的 mRNA 水平差异，但**该比较发生在各启动子的最适诱导条件下**（*alcA* 用甘油+苏氨酸、*glaA/agdA* 用麦芽糖，其余用低糖 PDA），属于'启动子最大潜力'的比较，而非'恒定培养条件下的稳态对比'。这一前提并未在正文或图注中明确提示。因此该数据**仅支持'*alcA* 是这几个启动子中最强的可诱导元件'，不应被直接外推到恒定培养下各启动子的同步比较**。这是利用本文信息时需要注意的证据边界。

**Q3：该产量是否足以支撑后续紫杉烷生物合成研究？**

**A**：GB127 的 taxadiene 达到可检测水平且作者报告五次平行实验重现，说明 TPF6 可作为进一步研究的真核底盘原型；这还不能说明产量足以支撑完整紫杉醇途径或放大生产。本文未检测下游氧化紫杉烷，也没有给出放大、分离纯化或经济性数据。同一研究中的 *E. coli* T2 滴度为 11.3 ± 0.5 mg/L，约高 180 倍，但两套宿主与培养条件不同，不能将该算术比值当作严格性能排名。是否由甾醇反馈调控或内源萜类竞争造成低滴度，仍需独立实验验证。

---

> 注：原文未提供 SI Figure 1（TPF6 MVA 通路转录水平）、SI Figure 2（启动子报告质粒图）、SI Figure 3（T2 纯化 taxadiene 的 <sup>1</sup>H NMR 谱）和 Supplementary Table 1（寡核苷酸列表）的原始图像，故相关定量细节及结构鉴定化学位移无法核实；本文对以上图像中可能含的具体数值采用保守处理，仅依据正文定性结论加以引用。

> 分类状态：待全部文献笔记完成后统一分类归档。
