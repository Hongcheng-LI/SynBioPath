---
type: literature-reading
zotero_key: AHSIX7A6
doi: "10.1186/s40643-022-00569-5"
paper_type: research
classification_status: pending
reading_status: main-text-and-figures-read
review_status: model-source-crosschecked
human_full_paper_review: false
source_attachment: VGACPTNB
source_sha256: 5000f22b2df44b5e0101e29c376d4e45b6f0a56ca5b26b3164c5bcc0376528e9
created: 2026-10-10
---

> 原文来源：[Zotero 条目](zotero://select/library/items/AHSIX7A6)；[DOI](https://doi.org/10.1186/s40643-022-00569-5)；主文与图表已按来源进行模型交叉核对，尚未经人工逐项复核。 来源限制：Figure 1A 的 GC-MS 谱图未在 SI 中提供原图，仅在正文给出主峰位置，难以截取完整色谱及内标对应峰；坐标按整页保留；Figure 2C 的 SDS-PAGE 原始扫描未单独提供，整图按 PDF 第 5 页下方的实际版式定位；正文提及的补充图表（Figure S1–S7、Table S1–S2）随附于 Additional file 1，PDF 未提供 SI 单独文件，正文未给出可截取的单独图像；Taxadien-5α-ol 与 OCT、iso-OCT 的具体质量收率、误差线数值未在正文文字中报告，本笔记仅复述论文中给出的近似倍数提升；Taxadiene 与各含氧化紫烷在不同时间点（24 h、48 h、72 h）的精确浓度数值未在正文中逐一列出，相关趋势仅能由 Figure 1B 柱高估读；Figure 5 各子图（14 °C/22 °C/28 °C、不同 IPTG、不同培养基、不同甘油浓度）下 taxadien-5α-ol 与 diterpenoid1 的逐柱数值未在正文给出，本笔记仅引用 27 mg/L 总含氧化紫烷与 7.0 mg/L taxadien-5α-ol 这两个汇总数值。

# 一、基本信息

**文章题目**：Construction of an *Escherichia coli* cell factory to synthesize taxadien-5α-ol, the key precursor of anti-cancer drug paclitaxel

**文章 DOI 号**：10.1186/s40643-022-00569-5

**期刊名称**：Bioresources and Bioprocessing

**通讯作者及工作单位**：

- **Hui-Lei Yu (余慧蕾)**：华东理工大学生物工程学院、生物反应器工程国家重点实验室、上海生物制造协同创新中心 (State Key Laboratory of Bioreactor Engineering, Shanghai Collaborative Innovation Centre for Biomanufacturing, College of Biotechnology, East China University of Science and Technology)
- **Jian-He Xu (许建和)**：同上

# 二、研究背景

紫杉醇 (paclitaxel, Taxol™) 是从短叶红豆杉 (*Taxus brevifolia*) 树皮中分离的二萜类生物碱，因对多种实体瘤具有广谱抗癌活性，是临床最重要的化疗药物之一。传统生产方式面临三重瓶颈：从红豆杉树皮直接提取紫杉醇的得率极低，每获得 1 g 紫杉醇至少需要消耗三棵成熟红豆杉；化学全合成路线步骤冗长、收率低；目前工业上以从可再生针叶中提取 baccatin III、10-deacetylbaccatin III 为前体的半合成法为主，但仍受红豆杉生长速度制约。

紫杉醇的生物合成以所有萜类共有的 C<sub>5</sub> 前体异戊烯基焦磷酸 (isopentenyl diphosphate, IPP) 与二甲基烯丙基焦磷酸 (dimethylallyl diphosphate, DMAPP) 为起点，二者经甲羟戊酸 (mevalonate, MVA) 途径或 2-C-甲基-D-赤藓糖醇-4-磷酸 (2-C-methyl-D-erythritol-4-phosphate, MEP) 途径合成；随后由香叶基香叶基焦磷酸合酶 (geranylgeranyl diphosphate synthase, GGPPS) 缩合生成 C<sub>20</sub> 的香叶基香叶基焦磷酸 (geranylgeranyl diphosphate, GGPP)，再由紫杉二烯合酶 (taxadiene synthase, TS) 环化生成 taxa-4(5),11(12)-diene (taxadiene) 及 iso-taxadiene；taxadiene 经紫杉二烯-5α-羟化酶 (taxadiene-5α-hydroxylase, CYP725A4, T5αOH) 介导的首步加氧生成 taxadien-5α-ol，并继续经过至少 17 步酶催化的下游修饰才能得到紫杉醇本身。

由于植物 P450 在原核系统中正确折叠较为困难，E. coli 中含氧化紫杉烷产量一直偏低；Ajikumar 等 (2010) 通过多元模块途径工程在 E. coli MG1655 中获得 1 g/L taxadiene，但引入 T5αOH 与 CPR 后总含氧化紫烷仅 116 mg/L；Biggs 等 (2016a) 通过 N 端改造将这一数值提升至 570 mg/L。*Saccharomyces cerevisiae* 虽具备内膜系统更利于 P450 表达，但紫杉烷总产量 (Zhou 等 2015 报告的 *E. coli–S. cerevisiae* 联合体系 33 mg/L；Walls 等 2021 报告的 1 L 微生物反应器中 98.9 mg/L) 仍不具规模优势。

本研究的切入点是：在 E. coli 中搭建一条以甘油为碳源、自 IPP/DMAPP 起算的紫杉烷合成途径，并通过关键酶筛选、连接肽优化、代谢负担调控、前体供给强化和发酵条件优化，把 *de novo* 合成的 taxadien-5α-ol 推至可在摇瓶水平检测的水平。作者的总体目标是构建一个能够稳定生产紫杉二烯-5α-醇的大肠杆菌细胞工厂，并展示其作为萜类通用平台的潜力。

# 三、研究思路

作者的研究路线围绕"细胞工厂搭建—关键酶筛选—代谢负担削减—前体通路比较—发酵条件优化"五个逻辑阶段展开。

首先，作者在 E. coli BL21(DE3) 中组装三个质粒的初始菌株 TaolE1，使其分别承担上游 MEP 途径前体供给 (p40T7-*dxs*-*idi*)、中游 TS-GGPPS 模块 (pRSFDuet-1-*TbrTS*-GGPPS) 与下游 T5αOH-CPR 融合蛋白模块 (pACYCDuet-1-T5αOH-CPR)，并通过 GC-MS 鉴定产物分布。其次，针对下游模块的限速步骤，作者筛选了三种 TS (TbrTS/TbaTS/TwTS) 与两种细胞色素 P450 还原酶 (CPR/ATR)，同时考察连接肽 (GSG)<sub>n</sub> 对融合蛋白可溶表达与电子传递的影响。第三步，把下游三基因整合到同一 pACYCDuet-1 质粒上形成六个操纵子排列，验证质粒数与基因排列对代谢负担、酶可溶表达与产物得率的影响。第四步，比较 MEP 通路、过表达 MEP 限速酶 (*dxs*、*idi*)、异源 MVA 通路 (来自 *Enterococcus faecalis* 的 *mvaE/mvaS* 与来自酿酒酵母的 *erg12/erg8/erg19/idi*) 以及 MVA 与 MEP 协同供给对产物的影响。最后，对最佳 TaolV1 菌株开展温度、IPTG 浓度、培养基与甘油浓度的单因素优化。

这一路线形成了一个"模块化设计—瓶颈识别—代谢平衡—过程优化"的完整闭环。

# 四、研究方法

- **菌株与质粒构建**：以 *E. coli* BL21(DE3) 为宿主；GGPPS、T5αOH、CPR 来自 *Taxus canadensis*；TS 来源于 *Taxus brevifolia* (TbrTS)、*Taxus baccata* (TbaTS) 与 *Taxus wallichiana* (TwTS)；MVA 通路使用 *Enterococcus faecalis* 的 *mvaE/mvaS* 和酿酒酵母的 *erg12/erg8/erg19/idi*；载体为 pET21a(+)、pRSFDuet-1、pTrcHis2B 和 pACYCDuet-1。所有基因经 *E. coli* 密码子优化并由 GenScript 合成。
- **蛋白工程化改造**：去除 GGPPS 与三个 TS 的 N 端 98 和 60 个氨基酸；T5αOH、CPR、ATR 各自去除 N 端 24 和 74 个跨膜残基；T5αOH 截短 N 端融合牛 17α 羟化酶的 8 残基信号肽 MALLLAVF 并保留 GSTGS 连接肽。
- **小规模发酵与两相培养**：50 mL Terrific Broth (TB) 培养基 (含 12 g/L 蛋白胨、24 g/L 酵母粉、15 g/L 甘油、2.31 g/L KH<sub>2</sub>PO<sub>4</sub>、12.54 g/L K<sub>2</sub>HPO<sub>4</sub>)，添加 10% (v/v) 正十二烷作原位产物萃取；37 ℃、200 r/min 培养至 OD<sub>600</sub> ≈ 0.6 后以 IPTG (0.1 mM) 和 δ-氨基酮戊酸 (δ-ALA, 0.2 mM) 诱导，降温至 22 ℃ (优化后 16 ℃) 培养 48 h。
- **产物检测**：以 GC-MS (Shimadzu QP2010 SE，Rtx-5MS 柱，m/z 50–350 全扫描) 鉴定代谢产物；以正十八烷为内标归一化，taxadiene 用外标法定量，含氧紫烷产物以 taxadiene 标准曲线折算。
- **蛋白可溶表达分析**：SDS-PAGE 比较 TaolED1–6 菌株上清 (S) 与沉淀 (P) 中 TbrTS、T5αOH-CPR 与 GGPPS 的分布。
- **关键筛选对照**：单因素比较 TbrTS/TbaTS/TwTS、CPR vs ATR、(GSG)<sub>n</sub> 连接肽 (n = 1–5) 与原始 GSTGS、不同操纵子排列 (TaolED1–6)、不同前体供给策略 (MEP、MVA、MEP+dxs/idi、MVA+MEP 共表达) 与不同发酵条件 (温度、IPTG、培养基、甘油)。

# 五、实验设计及结果分析

### (一) 初始菌株 TaolE1 的构建与含氧化紫杉烷产物鉴定

#### 实验目的与设计逻辑

为检验"上游 MEP 通路 + 中游 TS + 下游 T5αOH-CPR"的三质粒组合能否 *de novo* 合成含氧化紫杉烷，作者构建了 TaolE1 菌株，并通过两相培养减轻产物反馈抑制，再用 GC-MS 鉴定产物分布与时序。

#### 实验结果与证据解析

如图形摘要所示，整条代谢路线以甘油为碳源，通过 Trc4 质粒承载的异源 MVA 通路 (*mvaS*、*mvaE*、*erg12*、*erg8*、*erg19*、*idi*) 与 AES4 质粒承载的下游紫杉烷模块 (GGPPS–TbrTS–T5αOH–CPR) 共同向细胞供给前体并完成 *de novo* 合成，最终指向 taxadien-5α-ol 这一紫杉醇关键前体。


![Graphical Abstract 原文第 2 页](https://synbiopath.online/AHSIX7A6-Graphical-Abstract-p2-1-ce3f7ed2e3c9a317.png)

*Graphical Abstract：论文图形摘要：以甘油为碳源的大肠杆菌细胞工厂，通过异源 MVA 通路（Trc4 携带 mvaS、mvaE、erg12、erg8、erg19、idi）与紫杉烷下游模块 (AES4 包含 GGPPS–TbrTS–T5αOH–CPR) 合成紫杉醇关键前体 taxadien-5α-ol。（原文 PDF 截图）。*


Figure 1A 的 GC-MS 总离子流图同时显示 Dodecane overlay、TIC 与 m/z 289 选择离子监测 (SIM) 三条曲线，可清晰指认 *taxa*-4(5),11(12)-diene (1)、5(13)-oxa-3(11)-cyclotaxane (*iso-OCT, 2*)、diterpenoid1 (3)、5(12)-oxa-3(11)-cyclotaxane (*OCT, 4*)、taxadien-5α-ol (5) 与两个未知单加氧二萜 (6, 7)。Figure 1B 显示各化合物在 24 h、48 h、72 h 三个时间点的产物浓度。原文明示，48 h 时 TaolE1 总含氧化紫烷滴度为 2.3 mg/L，其中 taxadien-5α-ol 为 0.31 mg/L。


![Figure 1 原文第 4 页](https://synbiopath.online/AHSIX7A6-Figure-1-p4-1-ce656193df07786e.png)

*Figure 1：De novo synthesis of oxygenated taxanes in E. coli cell factories. A GC–MS analysis of the products of TaolE1 strain. Seven compounds are taxa-4(5),11(12)-diene (1), 5(13)-oxa-3(11)-cyclotaxane (iso-OCT, 2), diterpenoid1 (3), 5(12)-oxa-3(11)-cyclotaxane (OCT, 4), taxadiene-5α-ol (5) and other unknown mono-oxygenated diterpenoids (6, 7). B Products concentrations of taxadiene and oxygenated taxanes at 48 h.（原文 PDF 截图）。*


这一结果既证明 E. coli 中确实能同时承担 TS 环化与 P450 介导的首步加氧，又暴露出两点现象：第一，原文明确指出本研究中 taxadien-5α-ol 滴度高于 OCT 与 iso-OCT，与 Sagwan-Barkdoll 与 Anterola (2018) 等既往报道以 OCT/iso-OCT 为主导的结果形成对照，作者将其归因于发酵条件差异 (Edgar 等 2016 报告 taxadien-5α-ol 占 T5αOH 总产物的 0–25%)；第二，原文进一步指出本体系的主要产物是未知化合物 diterpenoid1 (3，可能为 taxadien-5α-ol 的异构体)，这一点与 Walls 等 (2021) 在 *S. cerevisiae* 中的观察一致。此外，TaolE1 菌 OD<sub>600</sub> 仅 16，提示三质粒共存对细胞造成显著代谢负担，这是后续整合该菌株的起点。

补充实验 (SI Figure S1–S2) 比较了 *T. baccata* (TbaTS) 与 *T. wallichiana* (TwTS) 紫杉二烯合酶，以及来自 *Arabidopsis thaliana* 的 ATR 与来自 *Taxus cuspidata* 的 CPR。结果显示 TbrTS 优于 TbaTS、TwTS，Taxus 同源 CPR 也比通用 ATR 更适配 T5αOH，因此后续构建均沿用 TbrTS 与 Taxus CPR。

#### 关于融合蛋白连接肽优化的初步证据

作者以 (GSG)<sub>n</sub> (n = 1–5) 系列柔性连接肽替换原始 GSTGS，发现 (GSG)<sub>n</sub> 能提高 T5αOH-CPR 融合蛋白的可溶表达水平，但含氧化紫烷的比产却反而下降。作者据此推测 CPR 与 P450 不能形成正确构象，影响电子从 CPR 向 P450 的有效传递 (Wang 等 2021)。该结果直接否定了"连接肽越柔越有利于功能酶兼容"的简单假设，提示融合蛋白的设计需要结构层面的精确匹配，为后续表达优化指明了方向。

### (二) 通过质粒整合降低宿主代谢负担以提高产量


![Figure 2 原文第 5 页](https://synbiopath.online/AHSIX7A6-Figure-2-p5-1-7eaf5ab7ceaaf2b9.png)

*Figure 2：Effects of bacterial metabolic burden on the yield of oxygenated taxanes. A Comparison of the OD₆₀₀ values of TaolED1-6 strains at 48 h; B comparison of the specific titers of TaolED1-6 strains; C SDS-PAGE analysis of the protein expression levels of TaolED1-6 strains; D comparison of the product concentrations of TaolED1-6 strains. M: marker; S: supernatant; P: precipitate.（原文 PDF 截图）。*


#### 实验目的与设计逻辑

TaolE1 携带三个相容质粒，生长受限 (OD<sub>600</sub> ≈ 16)，直接限制产物总量。为检验"代谢负担"假设，作者把原 GGPPS-*TbrTS* (在 pRSFDuet-1) 与 T5αOH-CPR (在 pACYCDuet-1) 的下游三基因重新整合到单个 pACYCDuet-1 载体上，构建六个不同操纵子排列的 TaolED1–6 菌株。

#### 实验结果与证据解析

Figure 2A 显示 TaolED1–6 菌株在 48 h 的 OD<sub>600</sub> 均显著高于 TaolE1 (约 25 vs 16)，说明三质粒整合为两质粒后生长压力下降。Figure 2B 比较比产率，可见 TaolED3、TaolED4、TaolED5 三株的含氧化紫烷比产率显著高于 TaolE1 和 TaolED1、TaolED2；其中 TaolED1 和 TaolED6 比产率反而下降。Figure 2C 的 SDS-PAGE 提供了关键证据：T5αOH-CPR (127 kDa) 在六个菌株中可溶表达均极差，作者推断 E. coli 不利于表达如此大分子量的融合蛋白；而 TbrTS 在 TaolED1、TaolED2 与 TaolED6 中可溶表达较弱，在 TaolED3–5 中较强，这与 Figure 2B 中 TaolED3–5 比产率较高一致；GGPPS 在 TaolED5 中可溶表达稍弱，但并不影响最终产物，说明 GGPPS 不是下游模块的限速因素。

综合 Figure 2C 的证据，作者推断 TaolED1–6 之间产物差异的根本原因是 TbrTS 的可溶表达水平差异，进而决定了 taxadiene 的供给能力。Figure 2D 显示最优的 TaolED4 总含氧化紫烷为 12 mg/L，taxadien-5α-ol 为 3.1 mg/L，相较 TaolE1 (2.3 mg/L 与 0.31 mg/L) 分别提升约 5 倍和 10 倍。该结果提示 taxadiene 供给已逐步转化为关键瓶颈。

### (三) 引入 MVA 通路强化萜类前体供给


![Figure 3 原文第 6 页](https://synbiopath.online/AHSIX7A6-Figure-3-p6-1-e306943c67f82022.png)

*Figure 3：Schematic diagram of the biosynthesis of oxygenated taxanes with a heterologous MVA pathway. mvaE: acetoacetyl-CoA thiolase/HMG-CoA reductase gene; mvaS: HMG-CoA synthase gene; erg12: mevalonate kinase; erg8: phosphomevalonate kinase; erg19: mevalonate pyrophosphate decarboxylase; idi: IPP:DMAPP isomerase; GGPPS: geranylgeranyl pyrophosphate synthase; TS: taxadiene synthase; T5αOH-CPR: the fusion protein of taxadiene-5α-hydroxylase and Taxus-derived cytochrome P450 reductase; OCT: 5(12)-oxa-3(11)-cyclotaxane; iso-OCT: 5(13)-oxa-3(11)-cyclotaxane.（原文 PDF 截图）。*


#### 实验目的与设计逻辑

TaolED4 仍残留较多未被转化的 taxadiene (Figure 2D)，提示前体供给与下游加氧之间存在不平衡。作者假设胞内参与非天然萜合成的 IPP/DMAPP 不足，因此引入异源 MVA 通路 (Figure 3) 并与原 MEP 通路、过表达 MEP 限速酶 (dxs、idi) 的策略进行系统比较。

#### 实验结果与证据解析

Figure 3 系统总结了从乙酰辅酶 A 出发的 MVA 途径 (*mvaE*、*mvaS*、*erg12*、*erg8*、*erg19*、*idi*)，并把 GGPP 经 TS 生成 taxadiene、再由 T5αOH-CPR 转化为 taxadien-5α-ol、OCT、iso-OCT 及其他含氧化紫杉烷的完整路径绘制在同一示意图中，为后续比较不同前体供给途径提供参照。

Figure 4A 与 4B 比较了 TaolV1–5 系列菌株 (在 TaolED4 基因骨架上切换前体供给模块)。具体而言，TaolV1 在 TaolED4 基因骨架上以 TrcE (pTrcHis2B-*erg12*-*erg8*-*erg19*-*idi*) 提供 MVA 通路前体，其含氧化紫烷为 14 mg/L、taxadien-5α-ol 为 3.8 mg/L，比 TaolED4 (12 mg/L、3.1 mg/L) 略有提升，提示 MVA 通路能够支撑 taxadiene 的合成。然而，TaolV2 的比产率并未优于 TaolV1，原文推测是 TS 基因在质粒上需要占据更靠前的组装位序所致，说明基因排列同样重要。


![Figure 4 原文第 7 页](https://synbiopath.online/AHSIX7A6-Figure-4-p7-1-f28f406db7751fc5.png)

*Figure 4：Effects of different terpenoid precursor supply pathways on the yield of oxygenated taxanes. A Comparison of the specific titers of TaolV1-5 strains; B comparison of the product concentrations of TaolV1-5 strains with those of TaolE1 and TaolED4.（原文 PDF 截图）。*


Table 1 提供了 TrcE 与 T7E1 两种 MVA 质粒表达强度的定量对比：当 Trc 启动子强度定义为 1、T7 启动子定义为 5、两种质粒拷贝数均为 20 时，TrcE 与 T7E1 的表达强度分别为 20 与 100。然而，TaolV3 (T7E1) 的含氧化紫烷并未优于 TaolV1，原文将其归因于过强的转录加重代谢负担、扰乱前体供给与下游加氧之间的平衡。


![Table 1 原文第 7 页](https://synbiopath.online/AHSIX7A6-Table-1-p7-1-76ae1740e88be2d6.png)

*Table 1：Comparison of the expression strength of the MVA pathway (TrcE 与 T7E1 两种质粒的载体、启动子、复制子、拷贝数与计算得到的表达强度)。（原文 PDF 截图）。*


为进一步验证前体供给是否充分，作者在 T7E1 和 TrcE1 质粒中过表达 MEP 限速酶 *dxs* (TaolV4、TaolV5)。结果显示 TaolV5 产量低于 TaolV4；TaolV4 中残留 taxadiene 约占总 taxadiene 供给的 37%，比 TaolV1 (≈24%) 高约 51%。原文将这一现象解释为 MEP 与 MVA 两条通路均能工作、两条通路协同提供充足前体，但额外质粒与酶的引入打破了代谢平衡，导致下游 T5αOH-CPR 来不及把全部 taxadiene 转化为含氧化紫烷。原文同时指出，MEP 与 MVA 两种通路单独提供的萜类前体水平相近，而 MVA 与 MEP 限速酶 (*dxs*、*idi*) 的协同过表达并未超过单一通路。

综合 Figure 4A、B 与 Table 1 的证据，作者选择 TaolV1 作为后续发酵优化的对象。

### (四) TaolV1 菌株发酵条件优化

#### 实验目的与设计逻辑

在代谢通路与基因骨架已确定的前提下，温度、诱导剂浓度、培养基与碳源浓度是摇瓶水平上影响 P450 表达与代谢平衡的四个最常见变量。作者采用单因素比较法检验它们对总含氧化紫烷与 taxadien-5α-ol 的影响。

#### 实验结果与证据解析

Figure 5A 显示 14 ℃ 与 16 ℃ 下的总含氧化紫烷产量基本持平，但 14 ℃ 时 taxadien-5α-ol 的产量极低，说明低温虽有利于可溶表达但改变了 T5αOH 的产物分布比例。作者据此选择 16 ℃ 为最佳温度。Figure 5B 显示 IPTG 浓度为 0.2 mM 时总含氧化紫烷最高；过低 (0.1 mM) 限制诱导表达，过高 (0.5、1 mM) 则带来细胞毒性。Figure 5C 比较 LB、2YT 与 TB 三种培养基，TB 因营养充足而显著优于其他两者。Figure 5D 显示在 15 g/L 甘油基础上进一步提高甘油浓度 (20、30 g/L) 并未提升含氧化紫烷产量，因此选择 15 g/L 甘油作为最佳碳源。

在上述最优条件下，TaolV1 总含氧化紫烷达 **27 mg/L**、taxadien-5α-ol 达 **7.0 mg/L**，相较 TaolE1 初始菌株 (2.3 mg/L、0.31 mg/L) 分别实现 **约 12 倍与 23 倍提升**，且 taxadien-5α-ol 占总含氧化紫烷约 26% (引自原文 Conclusions)。原文同时指出，经过培养条件优化后残留 taxadiene 几乎消失，提示原有生产区间的瓶颈已由下游 T5αOH-CPR 的表达效率转移至 taxadiene 供给。


![Figure 5 原文第 8 页](https://synbiopath.online/AHSIX7A6-Figure-5-p8-1-6eee49fd61137d0f.png)

*Figure 5：Optimization of the fermentation conditions for TaolV1 strain. A Temperature; B IPTG concentration; C culture medium; D glycerol concentration.（原文 PDF 截图）。*


# 六、总体结论

本研究通过关键酶筛选、质粒整合、代谢负担调控、前体通路比较与发酵条件优化五个层面的协同改进，在 *E. coli* BL21(DE3) 中构建了一条 *de novo* 合成 taxadien-5α-ol 的细胞工厂路径。最终 TaolV1 菌株在 50 mL 摇瓶水平上获得 27 mg/L 总含氧化紫烷和 7.0 mg/L taxadien-5α-ol，分别是初始 TaolE1 菌株的约 12 倍和 23 倍，**taxadien-5α-ol 占总含氧化紫烷的 26%，明显高于 iso-OCT 与 OCT 在本研究体系中的占比，与既往文献中 taxadien-5α-ol 多作为少数产物的现象形成对比**。

论文形成的核心方法是两点：一方面是作者以质粒整合 (三→两质粒) 和启动子强度合理选择 (Trc vs T7) 来控制代谢负担，从而让外源萜类通路能在 E. coli 中长期稳定表达；另一方面是作者系统比较 MEP、MVA、MVA+MEP 与 MVA+dxs/idi 四种前体供给模式，证明在本系统中 MVA 与 MEP 通路对前体供给的贡献无显著差异。

对领域的实质性补充是：作者建立的工程化 MVA 通路与优化后的下游紫杉烷模块不仅服务于紫杉醇前体本身，也被论证可作为生产其他高附加值二萜的通用底盘；同时，本研究把"taxadien-5α-ol 高于 OCT/iso-OCT、diterpenoid1 为体系主要产物"作为可重复的现象加以实证，呼应了 Walls 等 (2021) 在酵母中的观察。

# 七、论文评价

### 优点与创新

第一，本研究最具辨识度的创新是把代谢负担管理作为紫杉烷细胞工厂设计的关键变量。论文通过 TaolED1–6 系列菌株的可溶表征与比产数据，把"质粒数过多导致 TbrTS 可溶表达不足"这一现象清楚地展示出来，是当前紫杉烷异源生产文献中较少系统呈现的环节。

第二，作者在发酵条件层面同样提供了若干正交证据：在 14 ℃ 与 16 ℃ 下观察到含氧化紫烷总量相近而 taxadien-5α-ol 比例变化，说明温度对 T5αOH 产物分布有调控作用；在 IPTG 浓度梯度上得到 0.2 mM 的窄区间最优点，符合"高浓度 IPTG 抑制生长、低浓度限制诱导"的诱导平衡逻辑。

第三，本研究是少数同时报告 taxadien-5α-ol、diterpenoid1 (3，可能为 taxadien-5α-ol 异构体)、OCT 与 iso-OCT 分布并量化 taxadien-5α-ol 在含氧化紫烷中占比 (26%) 的研究，与既往以 OCT/iso-OCT 为主的报道形成互补，且与 Walls 等 (2021) 在酿酒酵母中的观察一致。

### 未来研究方向

优先级最高的补充实验是对 T5αOH-CPR 的精细结构建模与连接肽工程。现有数据表明柔性 (GSG)<sub>n</sub> 可改善可溶表达但显著降低产物，作者推测是构象错位影响了电子传递效率；后续可通过 AlphaFold 多体预测或冷冻电镜结构解析 T5αOH-CPR 融合蛋白构象，并据此设计刚性连接肽或定向融合，以同时提高可溶表达与催化效率。

第二个方向是将 MVA 通路与下游模块整合到 *E. coli* MG1655 或 DH5α 染色体中，减少质粒数量与抗生素需求，从而获得更易于规模放大且遗传稳定的紫杉烷细胞工厂，并便于引入下一步 taxadien-5α-ol 乙酰转移酶 (TAT) 推进紫杉醇的 *de novo* 合成。

# 八、关键问题及回答

**Q1：本研究能否证明 T5αOH 在大肠杆菌中天然主要生成 taxadien-5α-ol，而非 OCT/iso-OCT？**

A：本研究通过 GC-MS 在同一菌株、同一发酵条件下同时定量 taxadien-5α-ol、OCT、iso-OCT 与 diterpenoid1，发现在 TaolE1 与 TaolV1 中 taxadien-5α-ol 始终高于 OCT 与 iso-OCT；然而，原文明示本体系的主要产物为未知化合物 diterpenoid1 (3，可能为 taxadien-5α-ol 的异构体)，这一点与 Walls 等 (2021) 在酿酒酵母中的观察一致，亦与 Edgar 等 (2016) 报告的 taxadien-5α-ol 占 T5αOH 总产物 0–25% 的区间相符。taxadien-5α-ol 滴度高于 OCT/iso-OCT 的现象在多次发酵与发酵条件优化 (温度、IPTG、培养基、甘油) 中稳定复现，符合**与表达系统耦合的工程结论**。作者并未对 T5αOH 的体外酶促反应进行底物特异性测定，**因此 taxadien-5α-ol 不是本研究体系中丰度最高的产物；其高于 OCT/iso-OCT 的现象应被理解为宿主、培养基、提取方法与下游模块协同作用下的综合结果**，而不能据此推论 T5αOH 本身的酶学选择性改变。

**Q2：(GSG)<sub>n</sub> 柔性连接肽提升可溶表达但降低产物得率，这一现象到底说明了什么？**

A：本研究提供的证据是：(GSG)<sub>n</sub> 提高了 T5αOH-CPR 的可溶表达 (SDS-PAGE 中上清带更强)，但 taxadien-5α-ol 与总含氧化紫烷的比产均下降。作者据此提出两种解释：一是活性位点空间取向改变导致电子传递效率下降，二是 T5αOH 与 CPR 形成不利的构象。**该结论仍受到如下限制：缺乏对融合蛋白二级/三级结构的直接观测、缺乏对电子传递速率的定量测量、缺乏对单一连接肽对酶活性 (而非可溶表达) 的独立测试。**因此，"柔性连接肽不利于功能"目前应被理解为一种工程现象学结论，后续需要结构生物学证据 (如 Cryo-EM 或 AlphaFold 多体预测) 才能转化为机制性结论。

**Q3：本研究代谢扰动 (质粒数、启动子强度、前体通路选择) 与产物得率的关系，是否构成一个可外推的设计原则？**

A：现有数据支持三条经验性原则：(i) 三质粒共存会显著抑制 *E. coli* 生长并降低 TbrTS 可溶表达，把下游三基因整合到单质粒可同时提高 OD 与比产；(ii) 对 MVA 通路而言，启动子强度并非越强越好，Trc 与 T7 在本系统中差异不大，过强的转录反而扰乱前体供给与下游加氧的平衡；(iii) 前体通路并非越"全越"提供越多前体，同时过表达 MEP 限速酶 (*dxs*) 与 MVA 通路反而打破平衡。这三条原则**符合本论文的实验观察**，但因变量 (启动子、酶源、碳源等) 仅在紫杉烷本体系中得到验证，**可外推性需要在其他二萜或三萜系统中独立检验**。此外，作者把高 DNA 表达与细胞内代谢扰动之间的因果关系作为解释变量，但缺乏转录组/代谢组层面直接证据，因此结论宜被视为表达优化经验而非通用代谢工程通则。

> 分类状态：待全部文献笔记完成后统一分类归档。
