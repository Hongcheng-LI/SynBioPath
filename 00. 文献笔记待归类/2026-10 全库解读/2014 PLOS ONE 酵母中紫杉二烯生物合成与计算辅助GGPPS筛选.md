---
type: literature-reading
zotero_key: WAMRE36G
doi: "10.1371/journal.pone.0109348"
paper_type: research
classification_status: pending
reading_status: main-text-and-figures-read
review_status: codex-source-checked
human_full_paper_review: false
source_attachment: 8CIEIEP5
source_sha256: 775aa4161c339f4b93f8abfda75609246181c753a4bc4841e84d7bcce5bee5dd
created: 2026-10-10
---

> 原文来源：[Zotero 条目](zotero://select/library/items/WAMRE36G)；[DOI](https://doi.org/10.1371/journal.pone.0109348)；由当前 Codex 读取原始主文并核对图表，尚未经人工逐项复核。 来源限制：正文未给出 Figure 3 6 个对接面板各行的精确像素坐标；Figure 3 在原文第 4 页占据整页底部跨双栏，仅靠机器定位的窄条形 bbox 不足以覆盖整幅 9.2 Å 标尺与全部子图，本笔记按近似位置给出扩展 bbox 并保留原 caption 坐标，仅作占位；正文 Table 1、Table 2 与 Figure 1、Figure 4、Figure 5、Figure 6 的候选 bbox 明显只截取标题/图注行，本笔记按观察扩展至含完整图/表主体的近似 bbox；未提供 Supporting Information File S1 的图像（Figure S1 1H/13C NMR、Figure S2 GC-MS 鉴定、Figure S3 GGPPS 蛋白与转录水平、Figure S4 溶氧依赖的产量与 OD600、Table S1 引物、Table S2 同源建模模板）；本笔记不引用 SI 中的具体数值，相关结论以正文表述为唯一来源；论文两个生物学重复的代谢组学数据未给出原始峰面积或 p 值，本笔记仅按原文相对趋势描述，不自行估算精确数字；各菌株紫杉二烯滴度以三次独立发酵均值报告，未给出 SD 或统计检验数值，本笔记沿用正文文本，不从柱高外推；Figure 5 与 Figure 6 涉及代谢组学层面，文中多用相对丰度（归一化峰面积比）描述，不代表绝对浓度，本笔记在分析时已明确标注证据等级。

# 一、基本信息

**文章题目**：Biosynthesis of Taxadiene in *Saccharomyces cerevisiae*: Selection of Geranylgeranyl Diphosphate Synthase Directed by a Computer-Aided Docking Strategy（通过计算机辅助对接策略筛选香叶基香叶基焦磷酸合酶以在酿酒酵母中合成紫杉二烯）

**文章 DOI 号**：10.1371/journal.pone.0109348

**期刊名称**：PLOS ONE

**通讯作者及工作单位**：
- **袁颖靳 (Ying-jin Yuan)**：天津大学 系统生物工程教育部重点实验室、化学工程与技术学院 (Key Laboratory of Systems Bioengineering, Ministry of Education & School of Chemical Engineering and Technology, Tianjin University)
- **殷政 (Zheng Yin)**：南开大学 药物化学生物学国家重点实验室、药学院 (State Key Laboratory of Medicinal Chemical Biology & College of Pharmacy, Nankai University)

# 二、研究背景

萜类化合物种类超过 5 万种，紫杉二烯 (taxadiene) 是抗肿瘤药物紫杉醇 (taxol) 合成途径中的关键二萜骨架前体。早期通过 *E. coli* 异源重构甲羟戊酸 (mevalonate, MVA) 途径与紫杉二烯合成酶 (taxadiene synthase, TS)，发酵优化后可达 1020 mg/L 紫杉二烯滴度，但 *E. coli* 缺乏下游 P450 羟基化等修饰酶的适配环境，难以承担后续工业改造。酿酒酵母 (*Saccharomyces cerevisiae*) 内源拥有 MVA 途径、可利用亚细胞器分区并耐受 pH 与渗透压波动，被视为更具工业化潜力的萜类底盘；然而当时酵母紫杉二烯滴度仅约 8.7 mg/L，远不能满足工业化预期。

强化 MVA 途径代谢通量是该领域共识，常用策略包括过表达 *erg20* (FPP 合酶) 与截短 *hmgr* (tHMGR，限速调控元件) 以扩大前体池。但 FPP 至 GGPP (geranylgeranyl diphosphate) 的转化由 GGPPS (geranylgeranyl diphosphate synthase) 完成，不同物种同工酶在口袋大小、FPP 亲和力和复合物稳定性方面差异显著，而相关体外动力学数据稀缺，常规同工酶筛选需要多轮随机尝试。本研究的总体目标是：(1) 通过 BLAST-同源建模-AutoDock 4.2 分子对接评估 6 种 GGPPS 与 FPP 的相互作用，以理性筛选最佳同工酶用于紫杉二烯合成；(2) 通过代谢组学比较两个酵母底盘 W303-1A 与 YSG50 的中央代谢差异，识别更优生产宿主；(3) 整合酶工程与宿主选择思路，建立可推广的萜类细胞工厂设计框架。

# 三、研究思路

作者采取"先通路后酶、先计算后体内、结合代谢组学解释宿主差异"的迭代策略。首先在 W303-1A 中单独表达 *ts*、再叠加 *ggppssc*，确认 FPP 供给不足是首要瓶颈，随后整合 *erg20*、*thmgr* 构建可检测的紫杉二烯合成底盘 SyBE_001110；接下来借助 BLAST 检索 6 种 GGPPS 的同源模板、MOE 建立同源模型、AutoDock 半柔性对接 FPP，按结合能与抑制常数对六酶进行排序，将排名 1、4、6 的 GGPPSbc、GGPPSeh、GGPPSsc 引入体内测试以验证计算预测；同步在 W303-1A 与 YSG50 两个底盘上构建同一套途径，比较"酶 × 宿主"两个维度的紫杉二烯滴度；最后用 GC-TOF/MS 代谢组学比较两底盘的糖酵解、TCA 循环中间体及关联氨基酸相对含量，解释 YSG50 在 MVA 通量分配上的优势，结合溶氧实验支撑"TCA 受抑-乙酰辅酶 A 流向 MVA"的工作模型。

# 四、研究方法

- **载体构建与酵母转化**：OE-PCR (overlap extension PCR) 组装 *tdh3p-ts-pgkt*、*pgkp-ggpps-cyct*、*tdh3p-erg20-cyct*、*tdh3p-thmgr-cyct* 等表达盒，分别克隆到 pRS425（高拷贝 2μ）、pRS305、pRS403、pRS304（整合型）酵母穿梭载体；*ts*、*ggppsbc*、*ggppseh* 经 AuGCT 密码子优化；LiAc/SScarrier DNA/PEG 法转化酵母并在 SD-drop 营养缺陷平板上筛选，PCR 验证转化子。
- **紫杉二烯发酵与提取**：SD 或 YPD 培养基 30°C、200 rpm 摇瓶 60 h；5 L 生物反应器（2 L SD，pH 5.7，1 vvm，350 rpm，66 h）培养 SyBE_001113，加 300 mL 正己烷萃取后硅胶柱纯化；以 NMR (1H、13C) 与 GC-TOF/MS（*m/z* 272、122、107）确证结构。
- **胞内代谢物分析**：液氮淬灭-甲醇/水提取-两阶段衍生化（甲氧肟化 + MSTFA 三甲基硅烷化），琥珀酸-d4 为内标，GC-TOF/MS 扫描 *m/z* 50–800，定量糖酵解、TCA 循环及支链氨基酸中间体。
- **同源建模与分子对接**：BLAST 检索六种 GGPPS 模板（具体模板见 SI Table S2），MOE 的 Protein 模块在 Amber12EHT 力场下构建同源模型；AutoDock 4.2 的 Lamarckian 遗传算法对 FPP 进行全口袋半柔性对接，输出结合自由能与抑制常数。
- **蛋白水平与转录水平检测**：Anti-FLAG (Sigma, 1:10000) 检测带 FLAG 标签的 GGPPS，Anti-α-Tubulin 为内参；TriZol 提取总 RNA，ACTIN 为内参 qPCR 比较 *ggppsbc/ggppseh/ggppssc* 表达。

# 五、实验设计及结果分析

### (一) 在酿酒酵母中搭建最低紫杉二烯合成单元并强化 MVA 通量

#### 实验目的与设计逻辑
作者首先回答"酵母能否从头合成紫杉二烯"这一前置问题，并通过逐步引入 *ts*、GGPPS、*erg20*、*thmgr* 模块，建立最低限度的紫杉二烯合成底盘，为后续同工酶与底盘比较建立统一基线。

#### 实验结果与证据解析
作者在 W303-1A 中首先构建仅含 *ts* 高拷贝表达盒的 SyBE_001188，60 h 摇瓶发酵未检测到紫杉二烯 (Fig. 2)；叠加 *ggppssc* 形成 SyBE_001189 后产物仍未检出 (Fig. 2)。该结果直接证明在内源 MVA 通量极低的条件下，单纯导入外源 TS 和酵母自身 GGPPS 不足以形成足够的 GGPP 前体，单一代谢步骤的引入尚未跨越"前体可获得性"阈值。

随后作者引入 FPP 池强化策略：在 SyBE_001189 基础上整合 *erg20* 过表达盒得到 SyBE_001190，摇瓶发酵得到 **0.22 mg/L** 紫杉二烯 (Fig. 2)。进一步整合截短 *thmgr* (tHMGR) 得到 SyBE_001110，滴度提高至 **1.82 mg/L** (Fig. 2)，即 *erg20 + thmgr* 协同过表达使紫杉二烯滴度较单独 *erg20* 提升约 8 倍。论文未对生长曲线、内源 *erg20* 与 *hmg1/2* 表达水平作系统分析，因此 *erg20 + thmgr* 的协同究竟是源于 FPP 池真实提升、辅因子供给均衡，还是弱化了内源甲羟戊酸途径的反馈抑制，目前仍有歧义。


![Figure 1 原文第 3 页](https://synbiopath.online/WAMRE36G-Figure-1-p3-1-1e7c467052b5f073.png)

*Figure 1：Figure 1. 酿酒酵母中重构的紫杉二烯生物合成途径（The engineered taxadiene biosynthetic pathway in S. cerevisiae）（原文 PDF 截图）。*


![Table 1 原文第 3 页](https://synbiopath.online/WAMRE36G-Table-1-p3-1-bd8c35f673c425be.png)

*Table 1：Table 1. 本研究使用的菌株一览（Strains used in this study）（原文 PDF 截图）。*


![Figure 2 原文第 4 页](https://synbiopath.online/WAMRE36G-Figure-2-p4-1-a9fbd2f950571fc5.png)

*Figure 2：Figure 2. 工程化酿酒酵母 SyBE_001188、SyBE_001189、SyBE_001190、SyBE_001110 的紫杉二烯产量；数据为三次独立发酵均值（原文 PDF 截图）。*


图 1 用节点-箭头图直观展示葡萄糖经 MVA 途径合成紫杉二烯的全流程并标注基因操作位点 (*tHMGR、ERG20、GGPPS、TS*)；图 2 用柱形图给出四菌株 60 h SD 摇瓶滴度的逐步爬升过程 (0 → 0.22 → 1.82 mg/L)。表 1 列出本研究构建的 13 株工程菌基因型 (SyBE_001103/001104/001188–001190/001109–001111/001113–001115)，可作为后续两两比较的索引。**此处实验直接证明：FPP/GGPP 前体供给是限制酵母紫杉二烯合成的首要瓶颈，但即使解决了前体问题，单纯依赖酵母内源 GGPPS 的转化效率仍不能支撑高滴度生产，下一步酶工程改造不可省略。**

### (二) 通过分子对接理性筛选 6 种 GGPPS 同工酶

#### 实验目的与设计逻辑
为解决"在缺乏完整体外动力学数据的前提下选择最佳 GGPPS"的难题，作者将思路从"随机筛选同工酶"转向"先计算后验证"。基本假设：GGPPS 催化口袋大小、关键残基与 FPP 配体的结合自由能差异可以预测催化效率，从而作为同工酶选择的先验排序。

#### 实验结果与证据解析
作者 BLAST 检索六种 GGPPS (Taxus baccata × T. cuspidate, GGPPSbc; Ginkgo biloba, GGPPSgb; Rana catesbeiana, GGPPSrc; Erwinia herbicola, GGPPSeh; Chlamydomonas reinhardtii, GGPPScr; S. cerevisiae, GGPPSsc)，在 MOE 中以 Amber12EHT 力场构建同源模型，并以 AutoDock 4.2 完成对接。图 3A–F 展示 FPP 与六种 GGPPS 的全蛋白对接（左）与口袋近距离图（右），配体均以棒状显示于结合口袋内部。Table 2 给出对接结合自由能与抑制常数：GGPPSbc (-8.09 kcal/mol，K<sub>i</sub> ≈ 1.17 μM，排名 1)、GGPPSgb (-7.17 kcal/mol，5.58 μM，排名 2)、GGPPSrc (-6.20 kcal/mol，28.59 μM，排名 3)、GGPPSeh (-5.88 kcal/mol，48.80 μM，排名 4)、GGPPScr (-5.49 kcal/mol，62.37 μM，排名 5)、GGPPSsc (-4.90 kcal/mol，256.57 μM，排名 6)。作者据此挑选排名 1、4、6 三种进行体内实验以代表"优、中、差"三档预测。

作者进一步分析结合口袋孔径：模拟 FPP 在真空中的长度约 9.2 Å (Fig. 3G)，GGPPSrc (8.2 Å) 与 GGPPSsc (8.6 Å) 孔径过窄可能限制 FPP 进入与 GGPP 排出；而 GGPPSbc (11.4 Å)、GGPPSgb (10.6 Å)、GGPPScr (10.8 Å)、GGPPSeh (9.6 Å) 孔径均大于 FPP。作者据此推断 GGPPSbc 可能在体内具有最佳催化能力。


![Figure 3 原文第 4 页](https://synbiopath.online/WAMRE36G-Figure-3-p4-1-9713815b5b62bb00.png)

*Figure 3：Figure 3. FPP 与六种 GGPPS 的对接结果：(A) GGPPSbc；(B) GGPPSgb；(C) GGPPSrc；(D) GGPPSeh；(E) GGPPScr；(F) GGPPSsc。左侧为整蛋白对接视图，右侧为活性位点放大视图；右侧另含 FPP 在真空中宽度约 9.2 Å 的标尺 (Fig. 3G)（原文 PDF 截图）。*


![Table 2 原文第 5 页](https://synbiopath.online/WAMRE36G-Table-2-p5-1-9e51b9aaed9044ab.png)

*Table 2：Table 2. 酶-底物对接数据（Data of enzyme-substrate docking）（原文 PDF 截图）。*


图 3 的 6 组对接图直观呈现各酶结合口袋的几何特征与关键残基-配体作用位点；表 2 提供对接的定量输出。作者据此完成"计算-排序"环节，验证环节交给下一节。**应区分：对接结合自由能是大规模筛选的代理指标，并未直接证明 K<sub>m</sub>、k<sub>cat</sub> 等真实动力学差异；口袋孔径观察属于几何层面支持，亦非完全体内证据。**

### (三) 不同底盘与不同同工酶组合的体内验证

#### 实验目的与设计逻辑
为了回答"对接排序是否真实反映体内催化效率"以及"底盘遗传背景差异是否放大或稀释该差异"，作者在 W303-1A 与 YSG50 两个酵母底盘同时引入 *erg20 + thmgr* 整合模块与三种 GGPPS 高拷贝模块，构建 6 株工程菌并比较紫杉二烯摇瓶滴度。

#### 实验结果与证据解析
W303-1A 底盘上 (Fig. 4)，以 SyBE_001110 (ggppssc) 为参照 (≈1.82 mg/L)，SyBE_001111 (ggppseh) 提高 1.5 倍 (≈2.7 mg/L)，SyBE_001109 (ggppsbc) 提高 7.2 倍 (≈13 mg/L)，排序与对接排名 1、4、6 完全一致。YSG50 底盘上，三菌株滴度同步抬升，SyBE_001114 (ggppssc)、SyBE_001115 (ggppseh)、SyBE_001113 (ggppsbc) 较对应 W303-1A 版本分别提高 3.7、1.6、4.3 倍；其中 **SyBE_001113 (YSG50, ggppsbc) 在 5 L 生物反应器 66 h 培养后滴度达 72.8 mg/L**，是本研究最佳株 (Fig. 4)。

作者随后以 Anti-FLAG Western blot 与 qPCR 检测三 GGPPS 在工程菌中的表达水平（SI Fig. S3）。结果与滴度排序相反：GGPPSsc 表达水平显著高于 GGPPSeh 与 GGPPSbc，但紫杉二烯仍最低。作者据此推断 GGPPSsc 与下游 TS 的代谢"适配度"不佳，即**该酶的酶活性主要由酶自身结构（口袋几何、底物亲和力）决定，而非由表达量决定**。


![Figure 4 原文第 5 页](https://synbiopath.online/WAMRE36G-Figure-4-p5-1-b47d29e335f7032d.png)

*Figure 4：Figure 4. 工程化酿酒酵母 SyBE_001109、SyBE_001110、SyBE_001111、SyBE_001113、SyBE_001114、SyBE_001115 的紫杉二烯产量；数据为三次独立发酵均值（原文 PDF 截图）。*


图 4 双底盘六菌株对比柱状图直观显示：(1) 对接排序在两个底盘上均成立，提示跨底盘迁移性；(2) YSG50 底盘整体上抬紫杉二烯滴度 1.6–4.3 倍，呈现明显叠加效应。**需注意：体内差异亦受蛋白折叠、辅因子可用性、GGPP 毒性等多因素影响，尚不能被简化为单一酶活性差异。**

### (四) 代谢组学揭示 YSG50 在 MVA 通量分配中的优势

#### 实验目的与设计逻辑
前三节证实了 YSG50 × GGPPSbc 组合的最优性，本节回答"为什么 YSG50 优于 W303-1A"。作者通过 GC-TOF/MS 测定两底盘菌株在指数期与稳定期胞内代谢物相对丰度，聚焦糖酵解到 TCA 循环这一与 MVA 途径竞争乙酰辅酶 A 的关键分支点。

#### 实验结果与证据解析
图 5 在完整的糖酵解-氨基酸-TCA 通路上展示 10 种代谢物的相对含量。结果显示：(1) 糖酵解末端的丙酮酸在两底盘之间无明显差异；(2) 从丙酮酸出发的三个支链氨基酸 (Ser、Phe、Leu) 在 W303-1A 中高于 YSG50，说明 W303-1A 中更多碳从丙酮酸进入氨基酸合成、损失通量；(3) 三种 TCA 循环有机酸（柠檬酸、延胡索酸、琥珀酸）以及由 TCA 中间体衍生的 Thr、Asn 在 W303-1A 中均显著高于 YSG50，指示 YSG50 中 TCA 通量更低。作者据此**推断 YSG50 由于 TCA 循环相对较弱，使更多乙酰辅酶 A 进入 MVA 途径**，从而具备更高的紫杉二烯生产潜力。

第二轮代谢组学（图 6）则比较 YSG50 与三株工程菌 SyBE_001113/114/115 中三种 TCA 中间体的相对丰度。结果显示工程菌中柠檬酸、延胡索酸、琥珀酸的水平较底盘 YSG50 进一步下降，紫杉二烯生产进一步抑制 TCA 循环，使更多碳通量流入 MVA。该结果支持"产物形成负反馈于 TCA 流量"的代谢可塑性。

作者在 SI Fig. S4 中进一步以 SyBE_001115 为对象考察通气量对滴度的影响：总滴度随通气下降而下降，但单位细胞滴度显著上升，与文献报道的限氧抑制 2-酮戊二酸脱氢酶 (2-ketoglutarate dehydrogenase) 从而将丙酮酸导向乙酰辅酶 A 的结论一致。


![Figure 5 原文第 6 页](https://synbiopath.online/WAMRE36G-Figure-5-p6-1-c930db15717fda26.png)

*Figure 5：Figure 5. W303-1A 与 YSG50 底盘菌株糖酵解途径与 TCA 循环中已鉴定代谢物及氨基酸的相对含量；纵轴为归一化峰面积（相对丰度），数值为两次独立生物学重复均值（原文 PDF 截图）。*


![Figure 6 原文第 7 页](https://synbiopath.online/WAMRE36G-Figure-6-p7-1-60dbcf8e348bcb41.png)

*Figure 6：Figure 6. 紫杉二烯生产菌 SyBE_001113、SyBE_001114、SyBE_001115 较 YSG50 底盘 TCA 循环中间体（柠檬酸、琥珀酸、延胡索酸）的相对丰度（原文 PDF 截图）。*


图 5 同时承载通路示意图与多个小型柱状图，每组柱形对应一种代谢物；图 6 用相对丰度柱状图比较 YSG50 与三株工程菌。**值得注意的是：上述比较均为相对丰度（归一化峰面积比），不是绝对浓度；两次生物学重复的统计推断能力有限；同时，氨基酸差异也可能源自两底盘在氮源利用或应激状态上的差异，而非仅由碳通量分配引起——因此对"TCA 通量下降导致 MVA 通量上升"的因果链应当作工作模型而非完全确证。**

# 六、总体结论

本研究通过在 *S. cerevisiae* 中引入紫杉二烯合成模块（*ts*）并过表达 *erg20*、*thmgr*，建立了最低检测滴度的紫杉二烯合成底盘（SyBE_001110，1.82 mg/L）；通过 BLAST-同源建模-AutoDock 对接预测六种 GGPPS 对 FPP 的结合能力，按排名选择 GGPPSbc、GGPPSeh、GGPPSsc 三种同工酶；体内滴度与对接排序高度一致，验证了计算辅助同工酶筛选策略的有效性。作者通过引入 YSG50 底盘并借助 GC-TOF/MS 代谢组学证据，推断 YSG50 由于 TCA 通量较低而将更多乙酰辅酶 A 导向 MVA 通路，最终在 YSG50 × GGPPSbc 组合下获得 72.8 mg/L 紫杉二烯滴度，**较此前报道的酵母内紫杉二烯产量提升约一个数量级**。该工作将计算酶学引入到萜类合成途径优化流程，提供了"理性筛选-体内验证-宿主选择"的合成生物学设计框架。

# 七、论文评价

### 优点与创新
论文最突出的贡献在于将原本依赖随机筛选的"GGPPS 同工酶选择"问题，借助分子对接排序转化为可量化的预测-验证闭环。该策略在两个独立底盘上重复成立，提供了正交证据。作者进一步通过代谢组学从 TCA 循环竞争碳通量角度解释宿主差异，方法学层面具有可推广性。最后，本文建立的 13 株工程菌与 SI 中的引物、模板、Western blot、qPCR 数据为后续同领域工作提供了可直接复用的资源。文中以 NMR + GC-MS 鉴定纯化产物并通过 5 L 生物反应器将滴度验证提高至 72.8 mg/L，也是论文价值链的关键支撑。

### 未来研究方向
建议优先补充：(1) GGPPSbc 的体外酶动力学实验（K<sub>m</sub>、k<sub>cat</sub>），以确认对接排序反映真实催化效率的程度；(2) 在 YSG50 中分别下调 *icd*、*gltA* 或 *sdh* 等 TCA 关键基因、观察紫杉二烯滴度变化，从而将"宿主差异源于 TCA 通量"这一工作模型推进为"限速步骤明确-再通量优化的工程实践"，并对比基因敲除与通气控制两条路线的优劣。

# 八、关键问题及回答

**Q1：分子对接排序是否真实反映体内 GGPPS 催化活性差异？即 GGPPSbc 优于 GGPPSsc，究竟是因为其口袋更适合 FPP，还是因为其在酵母中表达/折叠更稳定或下游 TS 适配性更好？**

**A**：本文直接证据仅限于对接结合自由能与体内紫杉二烯滴度的同向性，属于相关性而非因果。作者通过 Western blot / qPCR 显示 GGPPSsc 表达水平显著高于 GGPPSbc 但紫杉二烯仍较低，提示适配性/催化效率而非表达量为主要决定因素；但该实验并未彻底排除 GGPPSbc 在酵母中折叠稳定性、辅因子可用性或膜定位等优势。建议后续以纯酶体外动力学测定明确 GGPPSbc 的 K<sub>m</sub> / k<sub>cat</sub> 是否显著优于 GGPPSsc，将相关证据升级为因果证据。

**Q2：本研究在 YSG50 × GGPPSbc 中获得 72.8 mg/L 紫杉二烯滴度，将其归因于"TCA 通量更低使 MVA 通量更高"是否充分？**

**A**：作者提供的代谢组学差异（柠檬酸、延胡索酸、琥珀酸在 YSG50 中更低；产物形成后进一步降低）与限氧-单位滴度上升的旁证支持该工作模型；但相对丰度归一化（内标校正）只能揭示相对通量，且两底盘在氮代谢、应激响应上的差异也未被排除。YSG50 与 W303-1A 的遗传背景存在多处差异（如 YSG50 含 *ade3Δ22* 等），不能保证 TCA 差异独立于其他基因型因素。因此该解释目前应作为合理但尚未完全确证的工作模型。

**Q3：本研究"GGPPS 是 MVA 通量限速步骤"这一推断是否得到体内外直接验证？**

**A**：该推断建立在"更换 GGPPS 即改变紫杉二烯滴度 7.2 倍"的观察之上。逻辑上，紫杉二烯滴度变化可能受 GGPP 池、GGPP 稳定性、TS 适配性、辅因子、应激等多因素影响；论文未测定胞内 GGPP 绝对浓度、未做 *ggpps* 敲除验证其在该通路的必要性，因此"GGPPS 是限速步骤"目前是较合理的间接推论而非直接证明。建议后续以 LC-MS/MS 测定 GGPP 池、并以 *bts1* (酵母 GGPPS) 敲除观察 GGPP 与紫杉二烯变化来升级证据等级。

> 分类状态：待全部文献笔记完成后统一分类归档。
