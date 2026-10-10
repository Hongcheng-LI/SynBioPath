---
type: literature-reading
zotero_key: QG9AQFQQ
doi: "10.1021/acssynbio.5c00109"
paper_type: research
classification_status: pending
reading_status: main-text-and-figures-read
review_status: codex-source-checked
human_full_paper_review: false
source_attachment: GXKM3ZXP
source_sha256: 27e43b2a7792739360340935c011772f87ade4cbaa5639f49bd1c3203870dab2
created: 2026-10-10
---

> 原文来源：[Zotero 条目](zotero://select/library/items/QG9AQFQQ)；[DOI](https://doi.org/10.1021/acssynbio.5c00109)；由当前 Codex 读取原始主文并核对图表，尚未经人工逐项复核。 来源限制：当前 Zotero 条目未提供 Supporting Information；基因构建、引物及 3 L 反应器详细条件等需后续依据 SI 核对。

# 基本信息

- **论文题目**：Metabolic Engineering of Methanotrophic Bacteria for De Novo Production of Taxadiene from Methane
- **作者**：Xinzhe Zhang、Aipeng Li、Xiaohan Huang、Shuqi Guo、Chenyue Zhang、Ramon Gonzalez、Qiang Fei。
- **来源**：*ACS Synthetic Biology*，Research Article；DOI: 10.1021/acssynbio.5c00109；Zotero 记录日期 2025-07-14。当前本地 PDF 的卷期页显示 XXXX/XXX，故不补写未核实的卷页信息。
- **研究主题**：以甲烷为唯一碳源，工程化甲烷氧化菌 *Methylotuvimicrobium buryatense* 5GB1C 生产紫杉醇前体 taxadiene；通过内源启动子挖掘、MEP 通路增强、NADPH 供给和温度两阶段培养提高滴度。
- **原文核验**：本地 Zotero 附件为 13 页研究论文主文，首页包括摘要、Introduction、实验方法与全文结果；题名、DOI 和 SHA-256 与条目一致（27e43b2a7792739360340935c011772f87ade4cbaa5639f49bd1c3203870dab2）。首页的 Supporting Information 图标是出版商网页链接，未改变附件为主文的判断。图 1–7 和表 1 已按原 PDF 截图。
- **研究边界**：taxadiene 是紫杉醇生物合成前体，不是紫杉醇本身。论文的终产物是 taxadiene；没有在甲烷菌中构建后续氧化、酰化、baccatin III 或紫杉醇全合成路线。作者的碳减排结果是基于模型和假设的计算，不等于全生命周期评估。

# 研究背景

Taxadiene 是紫杉醇的萜类骨架前体。以糖为原料的工程菌能够生产 taxadiene，但甲烷作为丰富的一碳原料，能否经甲烷氧化菌转化为高碳数二萜仍有几个实际障碍：甲烷先进入 RuMP 等一碳同化过程，碳需要再进入 MEP 通路形成 IPP/DMAPP；MEP 通路的前体供给、GGPP 链延长与 taxadiene synthase（TXS）环化可能相互制约；多个反应还消耗还原力，造成细胞生长与萜类合成之间的资源竞争。

作者选择 *M. buryatense* 5GB1C，先验证甲烷到 taxadiene 的转化，再建立可用于筛选萜类通量的报告体系，挖掘菌株自身启动子，逐步调整 MEP 通路和辅因子供给，最后以温度调节将高密度生长阶段与 taxadiene 积累阶段分开。图 1 是碳流和工程策略示意图，不能理解为本文已测定每个胞内代谢物的实际流量。


![Figure 1 原文第 2 页](https://synbiopath.online/QG9AQFQQ-Figure-1-p2-1-4e124293ed02918c.png)

*Figure 1：Figure 1. Schematic metabolic engineering for taxadiene biosynthesis from methane. Abbreviations: H6P, hex-3-ulose 6-phosphate; G6P, glucose-
6-phosphate; GAP, glyceraldehde-3-phosphate; Ru5P, ribulose-5-phosphate; 6PGL, 6-phospho-D-glucono-1,5-lactone; DXP, 1-deoxy-D-xylulose 5-
phosphate; DMAPP, dimethylallyl diphosphate; IPP, isopentenyl diphosphate; GPP, geranyl diphosphate; FPP, farnesyl diphosphate; GGPP,
geranylgeranyl diphosphate; RuMP cycle, ribulose monophosphate cycle; PPP pathway, pentose phosphate pathway; MEP pathway,
methylerythritol phosphate pathway.（原文 PDF 截图）。*


*图 1：甲烷到 taxadiene 的候选代谢路线及本文使用的启动子、通路和还原力工程策略。*

# 研究思路

研究分为四步。第一，用 TXS 和 *M. buryatense* 自身的 ispA 比较底盘对萜类骨架的合成能力，以 GC–MS 确认产物。第二，从转录组中筛选高表达基因的上游启动子，在 GFP 和 α-farnesene synthase（AFS）报告系统中比较启动子强度，再将强启动子用于 TXS。第三，以 α-farnesene 为便于筛选的通量指示产物，比较 MEP 通路各基因过表达效果；将有利的 dxs1、dxs2、ispA 和异源 idi 引入 taxadiene 工程株。第四，测试 PPP 的 zwf1、zwf2、gnd 对 NADPH/NADP⁺ 和萜类产物的影响，并以 zwf1、温度切换和 3 L 生物反应器检验终产物改善。

α-farnesene 路径与 taxadiene 共享多处前体供给，但其合成酶和产物不同，因此它适用于单因素筛选，不等于 taxadiene 的定量替代。作者随后在 taxadiene 菌株中逐步确认关键工程步骤，这一设计提高了筛选效率，也要求最终结果回到目标产物实测，而不能仅凭报告产物或转录水平判断目标通量。

# 研究方法

1. **宿主与培养**：使用 *M. buryatense* 5GB1C；摇瓶培养在 250 mL serum vial 中加入 50 mL nitrate mineral salts（NMS）培养基，30°C、200 rpm，并加入 5 mL n-dodecane。以甲烷替换气相至终浓度 20%（v/v），每日更新气相；常规培养约 120 h。初步放大使用 500 mL spinner bottle，加入 300 mL 培养基、30 mL n-dodecane，以甲烷/空气 1:4 混合气、300 mL/min 通气和 400 rpm 搅拌。
2. **启动子筛选与菌株构建**：依据转录组表达水平和 Softberry 启动子预测挑选候选内源启动子，用 GFP 荧光和 AFS 产物进行验证；再将选出的启动子、MEP/PPP 通路基因和 TXS 构建到质粒或染色体中。基因组编辑采用无标记整合方法，并对阳性克隆进行 PCR 和测序验证。所有菌株、引物、质粒及启动子序列在作者的 SI 中列出，但当前 Zotero 附件没有该补充 PDF。
3. **代谢物与辅因子测量**：使用 n-dodecane 富集疏水产物，GC–MS 分析 taxadiene 和 α-farnesene；测量细胞生长、甲烷消耗、CO₂ 释放及 NADPH/NADP⁺。分子对接用于比较 GDH1/GDH2 与 G6P 的模型结合，不是实测酶动力学或结合常数。
4. **统计方法**：作者报告所有实验均进行三次重复，结果以 mean ± SD 表示，并采用双尾 t 检验，显著性阈值为 *P*<0.05。此为论文的总体统计说明；具体图表的独立培养批次对应关系仍应以原始数据/补充材料为准。
5. **3 L 培养**：作者采用温度两阶段策略，先以 30°C 促进细胞生长，约 48 h 进入对数生长期后段再降至 22°C 以促进 taxadiene 积累。图 7 报告了滴度、干细胞重、OD₆₀₀ 和温度变化；详细气体传质与补料条件需结合缺失的 SI 核查。

# 实验设计及结果分析

**1. 先确认底盘能以甲烷形成 taxadiene。** 工程株 TD00 表达 TXS 与异源 TcGGPPS，TD01 表达 TXS；120 h 培养后两者均检出 taxadiene。异源 TcGGPPS 没有明显提高滴度，作者据此提出该宿主已有的 ispA 可能能提供 GGPP，或瓶颈在其他步骤。TD01 初始产量较低，约 0.53 mg/L。作者用 AFS 构建 α-farnesene 株 FA00，作为共享前体途径的筛选工具；GC–MS 保留时间和质谱用于支持目标产物身份。这里的“首次甲烷到 taxadiene”是作者对研究新颖性的表述，独立范围检索未在本文内展示。


![Figure 2 原文第 5 页](https://synbiopath.online/QG9AQFQQ-Figure-2-p5-1-d3501dae5b555716.png)

*Figure 2：Figure 2. Verification of the ability of M. buryatense 5GB1C to synthesize terpenes. (A) The metabolic pathways for synthesizing sesquiterpenes (α-
farnesene) and diterpenes (taxadiene) in M. buryatense 5GB1C. (B) Schematic diagram of the construction of engineered strain TD00, TD01, and
FA00. (C) Chromatograms of fermentation products of M. buryatense 5GB1C, FA00, TD01. (D) The production of taxadiene in TD00 and TD01
and α-farnesene in FA00. (E-F) The mass spectra correspond to peaks I and II in (C).（原文 PDF 截图）。*


*图 2：甲烷氧化菌合成 taxadiene/α-farnesene 的路线、代表菌株、GC–MS 色谱及质谱证据。*

表 1 列出本文使用的菌株，包括启动子报告株、通路筛选株、多个 FA/TD 工程株及来源对照。表格的作用是将菌株编号对应到基因构建，后续比较应按具体编号和图注读取；相似前缀不代表菌株背景完全相同。由于构建细节和序列位于未附的 SI，笔记只记录主文明确报告的关键基因组合，不从表中压缩的基因型推测额外编辑。


![Table 1 原文第 3 页](https://synbiopath.online/QG9AQFQQ-Table-1-p3-1-824fbcacad89e105.png)

*Table 1：Table 1. Strains Used in This Study（原文 PDF 截图）。*


*表 1：研究中使用的 M. buryatense 5GB1C 工程株及对照株。*

**2. 内源强启动子提高 TXS 表达和 taxadiene 产量。** 作者由转录组筛选高表达基因的启动子，并以 GFP 及 AFS 产物交叉比较启动子强度。PpmoC 与 P16200 表现较强；将它们用于 TXS 表达后，TD02、TD03 的 taxadiene 分别达到约 2.50 和 2.58 mg/L。GFP 与 AFS 的结果趋势相似，支持这些序列能在该宿主中驱动表达。P16200 所在基因的功能并未因此被证明参与 taxadiene 生物合成；其作为启动子元件的用途与原生基因功能需要区分。主文图 3A 的转录组热图标注四次独立实验，文章方法亦报告总体三重复。


![Figure 3 原文第 6 页](https://synbiopath.online/QG9AQFQQ-Figure-3-p6-1-f4337ddc2da0e6cc.png)

*Figure 3：Figure 3. Mining and characterization of endogenous promoters in M. buryatense 5GB1C. (A) Heatmaps showing gene expression levels (FPKM >
5,000) from four independent experiments. (B) Validation of promoter strength using green fluorescence protein (GFP) and terpene synthase
(AFS). (C) Construction strategy of engineered strain PG01-PG06. (D) Fluorescence intensity per unit of bacteria counts over 120 h. (E)
Construction strategy of engineered strain PA01-PA06. (F) Variation in terpene titers resulting from regulation of terpene synthase by different
promoters. (G) Construction strategy of engineered strain TD02-TD03. (H) Taxadiene titer is produced by the strongest promoter driving the
expression of TXS gene.（原文 PDF 截图）。*


*图 3：内源启动子挖掘、GFP/AFS 验证，以及启动子调节 TXS 的结果。*

**3. 增强 MEP 通路前体并补足 IDI。** 作者用 AFS 对九个候选基因进行单因素筛选，dxs1、dxs2 和 ispA 对萜类生成的提升较明显；其他若干 dxr、ispD/E/F/G/H 过表达效果较弱。随后在 taxadiene 株中整合 dxs1、dxs2、ispA，滴度从 TD03 的 2.58 mg/L 提高到 TD04 的 5.06 mg/L。主文指出 5GB1C 缺乏内源 idi，故分别补入大肠杆菌 I 型 EcIDI 和枯草芽孢杆菌 II 型 BsIDI；二者均促进 taxadiene，BsIDI 的 TD06 达 9.69 mg/L。作者讨论两类 IDI 的催化机制差异可能解释其效果，但本文未给出纯化酶动力学或细胞内 IPP/DMAPP 定量来验证该机制。


![Figure 4 原文第 7 页](https://synbiopath.online/QG9AQFQQ-Figure-4-p7-1-62e0caf6338a7caa.png)

*Figure 4：Figure 4. Enhancement of MEP pathway flux for taxadiene biosynthesis in M. buryatense 5GB1C. (A) The carbon flow of MEP pathway in M.
buryatense 5GB1C. The endogenous genes of M. buryatense 5GB1C are shown in green, the gene from E. coli or B. subtilis is shown in purple, and
the gene from Taxus brevifolia is shown in blue. (B) Construction strategy of engineered strain FA01-FA09. (C) Differences in terpene titers caused
by overexpression of individual genes in MEP pathway. (D) Construction strategy of engineered strain TD03-TD06. (E) Taxadiene titer after the
overexpression of key genes in the MEP pathway.（原文 PDF 截图）。*


*图 4：MEP 通路结构、单基因筛选及 dxs1/dxs2/ispA/idi 工程对 taxadiene 的影响。*

**4. NADPH 补给是该阶段的重要限制因素。** MEP 通路的 DXR 直接使用 NADPH，IspG/IspH 还通过 ferredoxin 依赖步骤消耗还原力。作者比较 PPP 相关 zwf1、zwf2、gnd 后发现，过表达 zwf1 最能提高萜类产量并恢复 NADPH/NADP⁺比例；zwf2 作用较弱。AlphaFold2 结构模型与 G6P 对接中，GDH1-G6P 计算结合能为 −5.58 kcal/mol，GDH2-G6P 为 −4.64 kcal/mol；作者提出 GDH1 的 H215 可与底物形成氢键，或解释其表现差异。对接结果是结构假说，不是实验测得亲和力，也没有通过 H215 定点突变建立因果关系。


![Figure 5 原文第 8 页](https://synbiopath.online/QG9AQFQQ-Figure-5-p8-1-6b524cd1de8ae7b3.png)

*Figure 5：Figure 5. Influences of reducing power enhancement on terpene biosynthesis in M. buryatense 5GB1C. (A) Pentose phosphate pathway for
producing NADPH in M. buryatense 5GB1C. 6PG, 6-Phospho-D-gluconate. (B) Construction strategy of engineered strain FA10-FA12. (C)
Influence of overexpressing zwf1, zwf2, and gnd on terpene production capacity. (D) Impact of overexpressing zwf1, zwf2, and gnd on the cofactor
proportion in terpene synthesis strain. (E) Binding energy of GDH1-G6P and GDH2-G6P complex. (F) Docking result between two kinds of
GDH (light gray) and G6P (cyan). And the NADP+ is shown in green. Å is the unit of distance.（原文 PDF 截图）。*


*图 5：PPP 还原力工程、zwf1/zwf2/gnd 产物比较及 GDH1/GDH2–G6P 结构对接模型。*

**5. zwf1 组合改善滴度、还原状态和生长表型。** 在 TD06 基础上染色体过表达 zwf1 得到 TD07，NADPH/NADP⁺ 比值提高约 2.1 倍，taxadiene 达 22.97 mg/L，较 TD06 高约 1.4 倍。TD06 有生长延迟，TD07 生长接近野生型。两者甲烷消耗率和 CO₂ 释放率相近，作者据此认为生长恢复主要来自还原力补充，而非甲烷摄取增强；这是由多项表型支持的解释，但不能等同于已完成全碳流解析。该结果还说明 PPP 与 MEP 共用 G6P 时，瓶颈未必简单等于碳源不足。


![Figure 6 原文第 9 页](https://synbiopath.online/QG9AQFQQ-Figure-6-p9-1-c7f98d093c79f605.png)

*Figure 6：Figure 6. Improvement of taxadiene biosynthesis with replenishment of reducing power in M. buryatense 5GB1C. (A) Construction strategy of
engineered strain TD07. (B) The influence of overexpressing zwf1 on the ratio of cofactors in the taxadiene synthesis strain. (C) The impact of
overexpressing zwf1 on the production of taxadiene. (D) The growth status of strains TD06, TD07, and wild type M. buryatense 5GB1C. (E) The
consumption of methane in serum vials per 24 h. (F) The emission of CO2 in serum vials per 24 h.（原文 PDF 截图）。*


*图 6：TD07 构建、NADPH/NADP⁺、taxadiene、细胞生长、甲烷消耗和 CO₂ 释放比较。*

**6. 温度两阶段培养提高滴度和体积生产率。** 在 18–30°C 梯度中，22°C 有利于 TD07 的 taxadiene 积累，但更低温度会明显抑制生长。作者因而先在 30°C 生长约 48 h，再降至 22°C 促进产物合成。该策略在 spinner bottle 验证后用于 3 L 生物反应器，终点 taxadiene 为 104.88 mg/L，第二阶段报告的最高体积生产率为 26.22 mg/L·d。作者提出温度切换同时利用甲烷菌的生长温度偏好和 TXS 的温度稳定性；主文展示的模型/培养结果支持该工艺选择，但没有比较多个罐次和长期连续培养稳定性。


![Figure 7 原文第 10 页](https://synbiopath.online/QG9AQFQQ-Figure-7-p10-1-a2fd8c3fcc7cde37.png)

*Figure 7：Figure 7. Taxadiene production by a final engineered strain of M.
buryatense 5GB1C using methane with controlling culture temper-
atures. (A) Effects of culture temperatures on taxadiene biosynthesis
and cell growth. (B) Taxadiene production under a two-stage
cultivation in 3-L bioreactors. (C) Carbon reduction evaluation of
methane bioconversion to 1 kg taxadiene and combustion or
emission.（原文 PDF 截图）。*


*图 7：3 L 反应器温度两阶段培养及 taxadiene 产量、细胞生长和作者计算的碳减排估算。*

**7. “负碳足迹”是条件化模型结果。** 图 7C 将每千克 taxadiene 的碳吸收量与甲烷燃烧/排放情境比较。方法按生物量与 taxadiene 的碳含量、甲烷全球变暖潜势（GWP100）等计算，文章报告潜在抵消超过 1,900 kg CO₂-eq/kg taxadiene。该模型说明甲烷被转入生物质和产物时可能减少排放，但不涵盖完整的甲烷供给、泄漏率、搅拌/冷却、分离纯化、原料预处理及设备能耗等生命周期边界，不能直接写成已实测的工艺碳足迹或净负排放。



**8. 报告系统与目标产物的证据关系**

作者先以 GFP 测转录驱动强度，再以 AFS 产物检验启动子在萜类合成环境中的表现，最后将启动子用于 TXS 并实测 taxadiene。这个三级验证比只按 FPKM 排名更接近工程目标，但 GFP、AFS 和 TXS 仍处于不同蛋白/产物背景，因此它们的表达效应不能完全互换。PpmoC 和 P16200 均能提高 taxadiene，文章选择 P16200 进入后续工程；其原生基因功能并未被作为通路因果节点验证，且启动子强度高不意味着在每个培养阶段都最适合。若后续复用，应在同一整合位点、相同拷贝数和相同菌株背景下测 TXS 蛋白/活性与目标滴度，避免把位置效应或拷贝数效应误当成启动子本身的差异。

**9. 甲烷菌的碳源利用和产物积累存在阶段性权衡**

碳同化、细胞增殖和萜类积累并非同一目标。作者观察到 taxadiene 在培养后段积累，并在细胞进入晚期生长阶段后采用降温策略；这类似将生物量生成与产物合成部分解耦。TD06 生长受阻而 TD07 恢复，且两者甲烷消耗相似，为还原力供给影响中心代谢提供了证据。两阶段 3 L 培养中，第二阶段细胞量仍增加并持续产物形成，故“生长阶段/生产阶段”是操作上的温度切换，不代表完全无生长的静置生产。若评估放大，除滴度外还应报告甲烷单耗、碳收率、尾气组分、干重和分离收率；作者关于碳转化效率提高的论述可由这些数据进一步量化。

**10. 结构和碳减排解释均需限定范围**

GDH1 H215 与 G6P 的预测氢键以及较低的对接能量，为 zwf1/zwf2 表型差异提供了可检验假说；但模型采用预测结构与计算对接，尚未由纯化 GDH1/GDH2 比较 kcat、Km，或通过 H215/V213 互换突变验证。类似地，图 7 的碳减排示意基于甲烷潜在排放替代和碳进入生物量/产物的假设，文章未展示完整生命周期清单。较稳妥的表述是“模型提示以甲烷生产 taxadiene 可能产生碳减排收益”，而不是“该工艺已证明净负碳”。

# 总体结论

作者在甲烷氧化菌 *M. buryatense* 5GB1C 中建立了从甲烷到 taxadiene 的路线，并通过内源启动子、MEP 通路基因、异源 IDI、NADPH 供给和两阶段温度培养，逐步提高产物滴度。摇瓶工程株 TD07 达 22.97 mg/L；3 L 反应器两阶段培养达到 104.88 mg/L，最高体积生产率报告为 26.22 mg/L·d。研究证明甲烷能够作为碳源进入 taxadiene 生产，为紫杉醇前体制造提供了一个甲烷利用概念平台；但还未解决 taxadiene 后续转化为紫杉醇的多步酶促路线，也未完成完整生命周期碳核算。

# 论文评价

- **主要贡献**：研究把甲烷氧化菌、萜类通路工程和发酵温度控制结合起来，不停留在启动子或单个基因层面；从色谱/质谱验证到 3 L 反应器放大，形成了较完整的“产物发现—瓶颈优化—工艺验证”链条。
- **可迁移策略**：P16200/PpmoC 等内源启动子扩充了 5GB1C 的调控元件；以 α-farnesene 作共享通路筛选工具，再回到 taxadiene 目标株验证；通过 zwf1 改善 NADPH 后同时恢复生长和提高产物，展示了碳流与还原力要联合考量。
- **证据边界**：Taxadiene 的 GC–MS 证据、三重复均值±SD及双尾 t 检验使产量结论较清楚。GDH1/GDH2 的结合能与氢键解释仅属计算支持；碳减排是用简化边界估算，非全生命周期分析；作者所称“最高”也限定在其检索比较范围。
- **工程限制**：培养体系使用 20% 甲烷气相和有机覆盖相；放大时需要控制气体组成、传质、温度、甲烷泄漏和安全运行。本文未提供独立反应器批次间变异或长期连续发酵稳定性，也没有把 taxadiene 进一步转成 T5OH、T10OH、baccatin III 或 paclitaxel。
- **总体判断**：这是一项甲烷底物利用和 taxadiene 前体生产研究，不是紫杉醇成品生物制造。其关键工程结果可为天然产物细胞工厂提供参考，但滴度、生产率、碳效率和产品下游完整性应分别评价。

# 关键问题及回答

1. **论文生产的是紫杉醇吗？**  
   不是。终产物是 taxadiene，即紫杉醇生物合成的二萜骨架前体；论文未构建后续氧化、酰化、baccatin III 或侧链组装。
2. **滴度如何逐步提高？**  
   以强启动子表达 TXS 得到约 2.58 mg/L；增强 dxs1/dxs2/ispA 并补入 BsIDI 后达 9.69 mg/L；zwf1 工程使摇瓶滴度达 22.97 mg/L；最后 30°C 生长、22°C 生产的两阶段培养在 3 L 反应器达到 104.88 mg/L。
3. **为什么选择 zwf1 而不是 zwf2？**  
   过表达 zwf1 可提高 NADPH/NADP⁺ 并提高萜类产量，而 zwf2 表现较弱。对接模型提出 GDH1 对 G6P 的结合更有利，但这不是经过酶动力学或残基突变验证的机制。
4. **甲烷转化效率是否更高于糖发酵？**  
   本文结果不能直接得出此结论。它证明甲烷可作 taxadiene 碳源并报告了较高滴度，但与糖路线的完整碳收率、能耗、分离成本及生命周期排放没有同边界比较。
5. **超过 1,900 kg CO₂-eq/kg taxadiene 是否代表负排放？**  
   这是作者按甲烷全球变暖潜势及产品/生物量碳含量作出的模型估算。若未计甲烷泄漏、供气、搅拌冷却、纯化和设备等排放，不能等同完整工艺的实测净碳足迹。
6. **最值得后续验证的环节是什么？**  
   应在独立 3 L 批次中复现滴度和 26.22 mg/L·d 生产率，测定甲烷碳进入生物量与 taxadiene 的真实摩尔收率，并量化尾气甲烷、CO₂、氧利用和分离损失；随后将 taxadiene 的下游氧化/酰化模块接入并确认具体产物，才能判断甲烷底物路线对紫杉醇制造的整体贡献。

> 分类状态：待全部文献笔记完成后统一分类归档。
