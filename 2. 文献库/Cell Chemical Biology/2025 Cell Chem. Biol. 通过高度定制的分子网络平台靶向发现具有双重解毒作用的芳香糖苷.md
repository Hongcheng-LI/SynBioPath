![image.png](http://synbiopath.online/20260104235303613.png)

---

## 一：基本信息

**文章题目**：Targeted discovery of aromatic glycosides with dual detoxification effects via a highly customized molecular networking platform

**文章 DOI 号**：https://doi.org/10.1016/j.chembiol.2025.12.001

**期刊名称**：Cell Chemical Biology

**通讯作者**：Bin Wei（魏斌）；Hong Wang（王鸿）；Qihao Wu（吴祺豪）

**通讯作者工作单位**：
* 魏斌：浙江工业大学药学院、长三角绿色制药协同创新中心、浙江省绿色低碳高效海洋渔业资源开发重点实验室、滨江人工智能研究院
* 王鸿：浙江工业大学药学院、长三角绿色制药协同创新中心、浙江省绿色低碳高效海洋渔业资源开发重点实验室、滨江人工智能研究院
* 吴祺豪：美国匹兹堡大学药学院

## 二：核心速览
### 研究背景
基于液相色谱-串联质谱 (LC-MS/MS) 的非靶向代谢组学是发现新天然产物的关键技术。分子网络 (Molecular Networking, MN) 通过比较二级质谱 (MS²) 的相似性来可视化结构相关的代谢物簇。然而，当前的分析平台（如 GNPS）主要依赖单一的修正余弦算法进行谱图比较，这可能导致漏掉因谱图差异（如离子强度分布不同）而结构相似的化合物，限制了全面发现隐藏代谢物的能力。

### 前期研究
已知不同 MS² 相似性算法（如熵、峰值百分比、中性丢失等）在某些情况下优于经典的余弦算法。然而，这些算法尚未被系统性地整合到一个平台中，也未在真实的天然产物发现工作流中评估其互补性。同时，实验谱图库的增长相对缓慢，而基于计算的虚拟谱图库可以作为补充，但需解决其引入假阳性注释的问题。

### 本文突破点
本研究开发并发布了 MSanalyst，一个用户友好的计算平台。它首次整合了 46 种不同的 MS² 相似性算法，并构建了包含实验谱图和 46 万余个虚拟谱图的综合谱图库。通过系统性的基准测试，筛选出 29 种能提供互补信息的算法。应用该平台分析 *Kutzneria viridogrisea* DSM 43850 菌株，成功发现了一类全新的细菌源芳香糖苷——kutznaposides A-F，并揭示了其生物合成源于 menaquinone（维生素 K₂）途径的一个未表征的分流途径，该途径充当了宿主清除活性氧 (ROS) 并避免自身毒性的双重解毒策略。

### 研究难点
1.  算法整合与优化：如何将众多算法无缝集成到一个高效、易用的工作流中，并为每种算法确定其在真实数据中的最佳相似性阈值，以平衡真阳性发现率和假阳性率。
2.  虚拟谱图的有效利用与质量控制：如何将大规模虚拟谱图库整合到注释流程中，同时设计有效策略（如基于化学相似性的过滤）来降低其引入假阳性注释的风险。
3.  隐蔽代谢途径的解析：发现的 kutznaposides 其生物合成基因在基因组中分散存在，未形成典型的生物合成基因簇，难以通过传统的基因组挖掘工具（如 antiSMASH）预测，需要结合多组学数据阐明其合成逻辑。
4.  通路功能的机理解释：需要整合蛋白质组学、生物活性实验和生物信息学分析，才能阐明 menaquinone 分流途径被激活的条件及其作为自我解毒策略的生物学意义。

---

## 三：研究思路
本研究遵循“方法学开发 -> 方法学验证 -> 方法学应用与生物学发现”的逻辑主线，具体步骤如下：

**步骤 1：多算法分子网络平台 MSanalyst 的构建与算法评估**
 
**具体思路和逻辑**：为解决单一算法在代谢物注释上的局限性，作者首先构建了一个集成化平台 MSanalyst。该平台整合了来自 matchms 和 SpectralEntropy 的 46 种谱图相似性算法，并利用 CFM-ID 为超过 46 万个天然产物结构生成虚拟 MS² 谱图库，与 GNPS 实验谱图库互补。然后，作者使用一个包含 81 个微生物天然产物真实谱图的数据集以及一个包含超过 300 万个谱图对的大型数据集，系统评估了所有算法在谱图库搜索和构建分子网络两方面的性能，通过计算真阳性率、假阳性率、网络拓扑指标等，筛选出能有效补充经典修正余弦算法的算法组合。

**步骤 2：应用 MSanalyst 全面挖掘目标菌株的代谢组**

**具体思路和逻辑**：为展示 MSanalyst 的实用性，作者选择了一个生物合成基因簇丰富但代谢组未被充分解析的放线菌 *Kutzneria viridogrisea* DSM 43850 作为目标。通过多培养基发酵和 LC-MS/MS 分析获取其代谢谱数据。利用 MSanalyst 中已验证的互补算法组合（修正余弦、熵、峰值百分比）进行谱图库搜索，并结合中性丢失算法进行分子网络聚类，旨在发现可能被单一算法遗漏的特征代谢物。

**步骤 3：目标代谢物的靶向分离、结构解析与生物活性评价**

**具体思路和逻辑**：基于分子网络分析锁定了一个潜在的糖苷类化合物簇。通过大规模发酵和基于质谱引导的分离纯化，获得了六个新化合物 kutznaposides A-F (**1-6**)。运用一维/二维核磁共振 (NMR)、高分辨质谱 (HRMS)、酸水解、化学合成及单晶 X 射线衍射等手段，精确鉴定了它们的平面结构和绝对构型。随后，对化合物及其前体进行了抗菌和抗氧化活性测试，以评估其潜在的生物医学价值。

**步骤 4：kutznaposides 生物合成途径的多组学解析与酶学验证**

**具体思路和逻辑**：kutznaposides C-F 具有独特的萘酚糖苷结构，提示其生物合成可能涉及非经典途径。作者通过基因组生物信息学分析，鉴定了 menaquinone 核心合成途径（*knp* 基因）的同源物。结合蛋白质组学分析，比较了能诱导 kutznaposides 产生的 GSM 培养基和对照 R2A 培养基中蛋白质的表达差异，锁定了可能负责酰胺化 (GAT) 和糖基化 (GT) 修饰的候选酶。最后，通过在大肠杆菌中进行异源表达和体外酶活实验，直接验证了关键糖基转移酶 GT5 和 GT6 的功能。

**步骤 5：阐明 menaquinone 分流途径的生物学功能与调控机制**

**具体思路和逻辑**：为了理解该分流途径的生物学意义，作者进行了自我抑制生长实验，证明了中间体 DHNA 对生产菌自身具有毒性，而下游糖苷化产物毒性降低，提示这是一个解毒过程。进一步对差异表达蛋白质组进行 GO 和 KEGG 富集分析，并结合蛋白质-蛋白质互作网络分析，揭示了在 GSM 条件下，菌体的三羧酸循环、丙酸代谢、NAD⁺合成等与旺盛有氧代谢和 ROS 生成相关的通路被显著激活。由此提出一个完整假设：菌体在氧化压力下激活 menaquinone 途径以合成抗氧化剂 DHNA，但 DHNA 自身具有细胞毒性；为解除此自身毒性，菌体进化出由 GAT 和 GTs 介导的分流途径，将 DHNA 转化为无毒的糖苷化产物 kutznaposides，从而实现“解毒抗氧化剂”的双重防御功能。

---

## 四：研究方法
以列表形式，详细拆解本研究采用的核心技术方法。

**多算法整合的分子网络分析**: 本研究开发了 MSanalyst 平台，其核心是整合了 46 种不同的 MS² 谱图相似性算法（如修正余弦、熵、峰值百分比、中性丢失等），允许用户在谱图库搜索和分子网络构建中自由切换或组合算法，以最大化发现结构相关代谢物的能力。

**基于 CFM-ID 的虚拟 MS² 谱图库构建**: 为了克服实验谱图库有限的瓶颈，作者使用 CFM-ID (Competitive Fragmentation Modeling) 工具，对从 CMNPD、NPAtlas 和 COCONUT 数据库中收集的 467,126 个非冗余天然产物结构进行了理论 MS² 谱图预测，构建了一个大规模的虚拟谱图库，并将其与 GNPS 实验谱图库整合，极大地扩展了可注释的化学空间。

**非靶向代谢组学与特征分子网络**: 对 *K. viridogrisea* 在不同培养基中的提取物进行 LC-HRMS/MS 分析，使用 MZmine 等软件进行峰检测、对齐和去卷积，生成包含 MS¹ 和 MS² 信息的特征列表。将此特征列表导入 MSanalyst 进行基于多算法的分子网络构建和注释，实现从复杂混合物中快速发现和归类代谢物家族。

**多组学整合分析（基因组学、蛋白质组学）**: 对目标菌株进行全基因组测序和注释，利用 antiSMASH 预测生物合成基因簇 (BGC)。通过基于 DIA/DDA 的定量蛋白质组学，比较不同培养条件下全蛋白的表达差异。将代谢组学发现的产物、基因组学预测的基因与蛋白质组学检测到的酶表达量相关联，从而解析隐蔽的、非基因簇编码的生物合成途径。

**酶学功能异源验证**: 将蛋白质组学筛选出的候选糖基转移酶基因 (**GT5**, **GT6**) 克隆至表达载体，在大肠杆菌 BL21(DE3) 中异源表达。以 DHNC 为底物， UDP-葡萄糖或 UDP-鼠李糖为糖基供体，进行全细胞催化反应，并通过 LC-MS/MS 检测糖基化产物 (**4**, **6**) 的生成，从而直接证实候选酶的体内催化功能。

**基于化学相似性的虚拟注释过滤**: 为控制虚拟谱图库带来的假阳性注释风险，作者设计了一种过滤策略：只有当虚拟谱图注释与同一分子网络簇中至少一个实验谱图注释的化学 Dice 相似度 ≥ 0.75（基于 Morgan 指纹计算）时，该虚拟注释才被保留。这有效提高了注释的可靠性。

--

## 五：实验设计及结果分析

### 研究部分一：MSanalyst平台的构建与多算法系统性评估
#### 实验目的与设计
本部分旨在开发一个超越单一算法局限性的分子网络分析平台，并通过严谨的基准测试，评估不同谱图相似性算法在真实代谢组学数据中的性能，筛选出能提供互补信息的优化算法组合。实验设计分为三步：1）构建包含 46 种算法和综合谱图库的 MSanalyst 平台；2）使用一个已知的微生物天然产物谱图数据集 (n=81) 评估各算法在谱图库搜索中的表现，使用约登指数 (Youden‘s Index) 为每个算法确定最佳阈值；3）使用一个更大的谱图对数据集 (n=2，543， 约三百万对) 评估各算法在反映结构相似性方面的广谱性能。
#### 实验结果与分析
作者首先概述了 MSanalyst 的工作流程 (Figure 1)。平台接受原始或预处理的质谱数据，集成了 UmetaFlow 和 matchms 进行数据预处理。其核心在于一个包含 GNPS 实验谱图和 CFM-ID 生成的超过 46 万个虚拟谱图的综合库，以及 46 种可选的相似性算法。在分子网络构建中，支持为库搜索和自聚类步骤选择不同的算法，并可通过“重分析”模块快速优化参数。
![image.png](http://synbiopath.online/20260104235824397.png)

> “MSanalyst incorporates these validated similarity metrics and assembles a comprehensive spectral library that includes both experimental and predicted spectra.”

随后，作者对算法进行了系统性评估 (Figure 2)。使用 81 个微生物天然产物谱图进行库搜索评估时发现，不同算法的最佳阈值差异很大 (Figure 2C)。例如，熵 (entropy) 算法在最佳阈值下获得了最多的真阳性 (TP) 注释 (36个)，而修正余弦 (modified cosine) 为 30 个 (Data S1)。重要的是，有 39 种算法能提供超出修正余弦的额外 TP 注释，证明了算法互补的必要性。通过计算各算法在最佳阈值下的混淆矩阵，发现大多数算法仅在阈值极高时 TP 数才锐减，而假发现率 (FDR) 随阈值提高逐渐降低 (Figures S7, S8)。作者发现，联合使用熵和 ms_for_id 算法，在各自优化阈值下，可以捕获所有单个算法识别出的 TP 注释 (Figure 2D)，这为实际应用提供了高效策略。
![image.png](http://synbiopath.online/20260104235903910.png)

> “Thus, Youden’s Index provides a practical criterion for algorithm-specific threshold optimization, with fine-tuning around these values to balance TP and FP annotations.”

在分子网络构建能力的评估中，作者基于 N20、网络分类准确率 (NACC) 和正确分类簇比率 (RCCC) 三个网络拓扑指标，将算法分为三组 (Figures 2E, 2F)。第 1 组算法生成小而精确的簇；第 2 组（包含修正余弦和峰值百分比）生成的簇更多、更大，且最接近理想的化学 Dice 相似度网络；第 3 组算法则产生包含大量不相关结构的大簇，效率低下。当将分析扩展到包含三百万谱图对的大数据集时，发现许多算法在相当大比例的谱图对比较中得分高于修正余弦，其中峰值百分比 (peak percentage) 算法在 37% 的比较中得分更高 (Figure 2G)。综合分析共筛选出 29 种具有互补价值的算法 (Data S1)。本研究还揭示了一些算法是修正余弦的子集 (如 avg_i， Figure 2H)，而另一些则完全无法反映结构相似性 (如 symmetric_chi_squared， Figure 2I)。

> “Collectively, these analyses help filter several low-accuracy and ineffective algorithms, thereby revealing 29 complementary algorithms—particularly peak percentage and entropy—which serve to enhance the establishment of spectral correlations.”

### 研究部分二：应用MSanalyst发现Kutzneria viridogrisea中的新芳香糖苷
#### 实验目的与设计
本部分旨在展示 MSanalyst 在挖掘复杂微生物代谢组、发现隐藏天然产物方面的实际应用能力。选择生物合成基因簇丰富但代谢物研究较少的 *Kutzneria viridogrisea* DSM 43850 为目标菌株，通过七种不同培养基培养以激活其生物合成潜力。利用 LC-MS/MS 获取代谢组数据后，使用 MSanalyst 中性能互补的算法组合（修正余弦、熵、峰值百分比）进行注释，并利用中性丢失算法进行聚类，以全面探索其代谢组并识别值得深入研究的代谢物家族。
#### 实验结果与分析
经过背景扣除，从 *K. viridogrisea* 的粗提物中鉴定出 214 个分子特征。使用 MSanalyst 分析后，修正余弦、峰值百分比和熵算法共同鉴定出 57 个实验谱图匹配和 1 个虚拟谱图匹配，覆盖了其他算法发现的所有已注释特征 (Figure 3A)。在排除合成药物和常见初级代谢物后，两个植物来源的糖苷注释引起了注意：特征 83 被注释为 rubinaphthin A，特征 33 被注释为 p-coumaryl alcohol 4-O-glucoside (Figure 3B)。关键的是，这两个糖苷使用峰值百分比算法与参考谱图的相似度很高 (>0.7)，但使用修正余弦算法的得分却很低 (<0.1) (Figure S16)。这一发现直接证明了依赖单一余弦算法会漏掉此类化合物，凸显了多算法整合的价值。
![image.png](http://synbiopath.online/20260105000043756.png)

> “These glycosides scored highly with peak percentage (>0.7) but poorly with the modified cosine score (<0.1) against the reference spectrum, underscoring the risk of missing such compounds when relying solely on cosine scoring.”

为了寻找更多类似物，作者将这些注释通过分子网络进行传播。在大多数算法生成的网络中，这两个糖苷特征都是单节点，但修正余弦和中性丢失算法生成的网络将它们与类似物连接了起来 (Figure S17)。修正余弦网络由于允许前体 m/z 偏移匹配，导致可视化结构拥挤 (Figure 3C)。相比之下，基于中性丢失的分子网络 (Figure 3A) 清晰地分离出一个界限明确的糖苷簇，这得益于糖苷类化合物共享一致的中性丢失片段（己糖基：162.0528 Da；脱氧己糖基：146.0579 Da）(Figure 3D)。通过整合培养基元数据，发现这类酚醛糖苷仅在 Gym Streptomyces Medium (GSM) 培养的细菌代谢组中被检测到 (Figure S19)。最终，通过分子网络分析锁定了 7 个潜在的糖苷特征，为后续的靶向分离指明了方向。

### 研究部分三：Kutznaposides的结构解析、生物活性及其生物合成起源推测
#### 实验目的与设计
本部分旨在验证 MSanalyst 预测的糖苷类化合物的结构，评估其生物活性，并初步探究其生物合成起源。首先，在能诱导产物产生的 GSM 培养基中进行大规模发酵，靶向分离目标化合物。综合运用 NMR、HRMS、化学合成、单晶衍射和酸水解等技术，精确解析六个新化合物 **1-6** 的平面结构与绝对构型。随后，对化合物及其生物合成前体进行抗菌和抗氧化活性测试。基于化合物的萘酚结构和已知的 menaquinone 生物合成知识，提出其可能来源于 menaquinone 途径的分支。
#### 实验结果与分析
通过大规模发酵和质谱引导的分离，成功获得了六个新化合物，命名为 kutznaposides A-F (**1-6**) (Figure 4A)。综合 NMR 和 MS 分析确定了它们的平面结构 (Figures 4B, S20-S26)。化合物 **1** 和 **2** 的苷元为取代苯，而 **3、4、5、6** 共享一个三取代萘骨架。对于 **3、4、6** 共有的苷元 1，4-二羟基-2-萘甲酰胺 (DHNC)，作者通过化学合成 (Figure S23) 和培养 **4** 的单晶 (CCDC: 2373550) 获得了直接证据，并通过单晶 X 射线衍射确证了其结构 (Figure 4B)。酸水解和糖衍生化 LC-MS 分析 (Figure 4C) 结合苷元质子偶合常数确定：**1、2、4、5** 含有常见的 α-L-鼠李糖，**3** 含有 β-6-脱氧-D-葡萄糖，**6** 含有 β-D-葡萄糖 (Figure 4D)。
![image.png](http://synbiopath.online/20260105000118511.png)

> “Subsequent hydrolysis assays and the J value of every anomeric proton revealed that kutznaposides A, B, D, and E (1, 2, 4, and 5) contained the common α-L-rhamnose, which is replaced by β-deoxy-D-glucose and β-D-glucose in kutznaposide C (3) and kutznaposide F (6), respectively.”

生物活性测试表明 (Figure 4E)，menaquinone 途径中间体 1，4-二羟基-2-萘甲酸 (DHNA)、其酰胺化产物 DHNC 以及糖苷化产物 **3、4、6** 对多种病原菌（包括耐甲氧西林金黄色葡萄球菌 MRSA）表现出不同程度的抑制活性，最小抑菌浓度 (MIC) 在 8-64 μg/mL 之间。在 ABTS 自由基清除实验中，DHNA、DHNC 和 **4** 表现出与阳性对照维生素 C (8.2 μM) 相当的抗氧化能力，其 IC₅₀ 值分别为 6.5、7.8 和 9.2 μM (Figure 4E， Figure S27)。这些结果表明，从 DHNA 到 DHNC 再到糖苷的修饰过程，改变了化合物的抗菌谱和活性强度，但保留了核心的抗氧化能力。

基于 **3-6** 的萘酚糖苷结构，作者推测其生物合成起源于细菌 menaquinone (维生素 K₂) 途径 (Figure 5E)。该途径从分支酸开始，经过一系列 *men* 基因编码的酶催化生成 DHNA。随后，一个推测的 II 类谷氨酰胺酰胺转移酶 (GAT) 可能负责将 DHNA 的羧基酰胺化为 DHNC。最后，尿苷二磷酸糖基转移酶 (UGT) 或胸苷二磷酸糖基转移酶 (TGT) 催化糖基化反应，生成最终的 kutznaposide 糖苷。
![image.png](http://synbiopath.online/20260105000236140.png)

### 研究部分四：多组学驱动的Kutznaposides生物合成途径解析与关键酶功能验证
#### 实验目的与设计
本部分旨在利用基因组学和定量蛋白质组学技术，在分子水平上验证和细化第三部分提出的生物合成假说，并鉴定负责关键修饰步骤的特定酶。首先，通过生物信息学分析在基因组中定位 menaquinone 核心合成酶的同源物 (*knp* 基因)。然后，对比产生 kutznaposides 的 GSM 培养基和不产生/少产生该化合物的 R2A 培养基的定量蛋白质组数据，筛选差异表达的候选 GAT 和 GT 基因。最后，通过在大肠杆菌中进行异源表达和体外酶活实验，直接验证候选 GT 的功能。
#### 实验结果与分析
基因组注释和 hummsearch 分析证实，菌株 DSM 43850 中存在 menaquinone 途径所有必需酶 (*menB* 至 *menF*, *menH*, *menI*) 的推定同源物，作者将其命名为 *knpB1* 至 *knpF1*, *knpH1*, *knpI1* (Figure 5A， Data S2)。为了寻找负责酰胺化和糖基化的酶，作者以已知的细菌 GAT 和 TGT 序列为参考，在基因组中筛选出 2 个 GAT 候选基因和 16 个 GT 候选基因 (Data S3)。
![image.png](http://synbiopath.online/20260105000211638.png)

定量蛋白质组学分析 (GSM vs. R2A) 的火山图显示了许多差异表达蛋白 (Figure 5A)。其中，一个 GAT (GAT1) 在 GSM 中表达显著上调。在 16 个候选 GT 中，有 9 个的表达量变化倍数 (log₂FC) > 1 (Figure 5B)。其中 5 个 (GTs 1-5) 仅在 GSM 条件下表达，另外 4 个 (GTs 6-9) 在 GSM 中的表达量是 R2A 中的 2 到 6 倍，提示它们可能参与 O-糖基化。

为了验证 GT 的功能，作者将表达量变化显著的 **GTs 1-9** 在大肠杆菌 BL21 中进行异源表达。以 DHNC 为底物， UDP-葡萄糖或 UDP-鼠李糖为供体进行全细胞催化实验。结果表明，表达 **GT5** 和 **GT6** 的细胞能够分别将 DHNC 转化为 kutznaposide D (**4**, α-L-鼠李糖苷) 和 kutznaposide F (**6**, β-D-葡萄糖苷) (Figure 5C)。有趣的是，**GT5** 和 **GT6** 都不能糖基化 DHNA，说明糖基化发生在酰胺化修饰之后。生物信息学分析还发现，这些参与 kutznaposides 生物合成的基因 (*knp*, *GAT*, *GTs*) 在基因组中分散分布，并未形成可由 antiSMASH 预测的典型生物合成基因簇 (Figure 5D, Table S2)。这一发现凸显了 MSanalyst 这类基于代谢组表型的方法在发现“隐蔽”代谢物方面的独特优势。

> “Collectively, proteomic profiling and enzymatic assays support the biosynthetic pathway in which the production of kutznaposides is driven by knp-encoded machinery... followed by tailoring steps catalyzed by GAT and the identified GTs.”

### 研究部分五：Menaquinone分流途径作为自我解毒策略的机制阐释
#### 实验目的与设计
本部分旨在阐明 *K. viridogrisea* 进化出 menaquinone 分流途径的生物学原因及其调控机制。通过自我抑制生长实验，验证 DHNA 及其下游产物对生产菌自身的毒性差异。通过对差异表达蛋白质组进行 GO 和 KEGG 富集分析，以及构建蛋白质-蛋白质互作网络，系统探究在激活该分流途径的 GSM 培养条件下，菌体内部发生的全局性生理变化，特别是与氧化应激和解毒相关的通路，从而构建一个完整的“压力感应-解毒响应”生物学模型。
#### 实验结果与分析
自我抑制生长实验表明 (Figure 6A)，menaquinone 途径的中间体 DHNA 对 *K. viridogrisea* 自身的生长抑制最强，而下游的酰胺化产物 DHNC 和糖苷化产物 **3、4、6** 的抑制活性依次减弱。这直接证明从 DHNA 到 kutznaposide 的两步酶促反应是一个逐步降低自身毒性的“自我解毒”过程，GAT 和 GTs 可被视为自我抗性基因。
![image.png](http://synbiopath.online/20260105000307178.png)

> “As expected, DHNA showed the most potent inhibitory effect against K. viridogrisea, followed by the downstream products DHNC and kutznaposides. These findings suggest that this two-step enzymatic reaction represents a self-detoxification process...”

为了理解该通路在何种条件下被激活，作者对定量蛋白质组数据进行了深入分析。GO 富集分析显示，在 GSM 培养基中，与解毒过程相关的条目被显著富集，如“细胞对异生物刺激的反应”和“异生物代谢过程” (Figure 6B)。KEGG 通路富集分析的前两位是“丙酸代谢”和“丙氨酸、天冬氨酸和谷氨酸代谢” (Figure 6C)。几乎所有参与这些通路的基因都显著上调 (Data S3)。
![image.png](http://synbiopath.online/20260105000324457.png)


通过提取这些关键通路中的蛋白质并构建其互作网络 (Figure 6D)，作者发现 GAT1 与喹啉酸合酶 (EC: 2.5.1.72) 和 L-天冬氨酸氧化酶 (EC: 1.4.3.16) 存在间接关联，这两个酶参与从喹啉酸合成 NAD⁺ 的前两步。它们的上调可能导致活性氧 (ROS) 的积累 (Figure 6E)。此外，在乙醛酸氧化过程中，过氧化氢酶 (EC: 1.11.1.6) 的缺乏和 (S)-2-羟基酸氧化酶 (EC: 1.1.3.15) 的上调也可能导致 ROS 积累。这可能是由于 *K. viridogrisea* 在 GSM 中比在 R2A 中进行了更旺盛的有氧代谢，这一点得到了三羧酸循环中所有酶的表达量均上调的支持 (Figure 6E)，且 GSM 培养的生物量约为 R2A 的两倍 (Figure S31)。
![image.png](http://synbiopath.online/20260105000342940.png)

基于以上数据，作者提出了一个完整的模型 (Figure 6E): *K. viridogrisea* 在 GSM 培养基中经历更强的有氧代谢和氧化压力，导致 ROS 积累。作为响应，菌体上调 menaquinone 途径以合成抗氧化剂 DHNA。然而，DHNA 本身对细胞有毒性。为了解除此自身毒性，菌体同时上调了 GAT1 和特定的 GTs (如 **GT5**, **GT6**)，将有毒的 DHNA 通过酰胺化和糖基化转化为低毒或无毒的 kutznaposide 糖苷。这样，该分流途径实现了双重功能：一方面，通过生成抗氧化剂 DHNA 应对氧化压力；另一方面，通过将 DHNA 解毒为糖苷，避免自我伤害。

> “Therefore, we propose that this bacteria-originated menaquinone shunt pathway employs a series of unconventional biochemical transformations as a dual strategy for surviving in oxidative environments and self-detoxifying the antioxidants they produce.”

---

## 六：总体结论
本研究成功开发并验证了 MSanalyst，一个通过整合多种互补性 MS² 谱图相似性算法来增强非靶向代谢组学分析能力的强大平台。该平台克服了单一算法（如修正余弦）的局限性，能够发现更多隐藏的谱图-结构关联。应用 MSanalyst 对 *Kutzneria viridogrisea* 进行分析，直接导致了一类全新细菌源芳香糖苷——kutznaposides A-F 的发现。通过多组学整合与酶学实验，本研究首次阐明 kutznaposides C-F 来源于一个此前未表征的 menaquinone 分流途径。该途径在宿主面临氧化压力时被激活，通过将 menaquinone 途径的有毒中间体 DHNA 逐步转化为无毒的糖苷，巧妙地实现了清除 ROS 和避免自身毒性的双重解毒目的。这项工作不仅提供了一个高效的代谢组学发现工具，也揭示了一种新颖的微生物自我防御代谢策略。

---

## 七：论文评价
### 优点与创新
1.  **方法学创新性强**：MSanalyst 是首个系统整合并评估多达 46 种 MS² 相似性算法的综合性平台。其“算法互补”理念和基于真实数据的阈值优化策略，为代谢组学数据分析提供了新的范式，显著提升了注释深度和广度。
2.  **研究逻辑完整严密**：工作流从方法开发、基准测试，到实际应用、产物发现、结构解析、途径阐明，直至功能机制阐释，构成了一个从技术到生物学发现的完整闭环，逻辑链条清晰，证据逐层递进。
3.  **多学科技术深度融合**：研究巧妙地融合了计算代谢组学、天然产物化学、合成化学、蛋白质组学、基因组学和酶工程学，是多组学驱动天然产物发现的优秀范例。
4.  **发现具有重要生物学意义**：不仅发现了新结构实体，更重要的是阐明了一个新颖的“自我解毒抗氧化剂”的代谢适应策略，为理解微生物在压力环境下的生存机制提供了新视角。

### 未来研究方向
1.  **算法与平台的持续优化**：文中指出，虚拟谱图与实验谱图间的系统性差异以及缺乏标准化的基准数据集限制了算法的严格评估。未来需要收集更高质量、更全面的标准化谱图数据以进一步提升算法性能。此外，可以探索集成更先进的机器学习模型用于谱图预测和相似性计算。
2.  **生物合成途径的完全解析**：本研究通过蛋白质组学和异源表达验证了糖基转移酶的功能，但负责关键酰胺化步骤的 GAT 酶尚未经实验验证。未来需要通过基因敲除、回补或体外重构实验，确证 GAT1 或 GAT2 的功能。
3.  **自我解毒机制的深入验证**：论文提出的自我保护机制虽然得到多组学数据和表型实验的有力支持，但仍缺乏直接的遗传学证据（如 *gat* 或 *gt* 基因敲除菌株对 DHNA 敏感性的改变）。未来的基因操作实验将能提供更直接的因果性证明。
4.  **拓展MSanalyst的应用范围**：可尝试将该平台应用于更广泛的样本类型（如植物提取物、人体微生物组、环境样本等），以检验其普适性并发现更多新颖代谢物。
5.  **Kutznaposides的潜在应用探索**：鉴于 kutznaposides 展示的抗菌和抗氧化活性，未来可对其构效关系进行深入研究，并评估其在抗感染或作为抗氧化剂方面的应用潜力。

---

## 八：关键问题及回答
#### 问题一：MSanalyst 整合虚拟谱图库带来了更高的注释覆盖率，但如何有效控制由此引入的假阳性注释风险？

**回答：** 作者设计了一个基于化学相似性的过滤策略来解决此问题。在分子网络生成后，只有当虚拟谱图注释与其所在分子簇中至少一个实验谱图注释之间的化学 Dice 相似度 ≥ 0.75（基于 Morgan 指纹计算）时，该虚拟注释才会被保留在网络中用于后续分析。这一策略利用了分子网络本身能将结构相似物聚类在一起的特性，用簇内可靠的实验注释作为“锚点”来校验和过滤不可靠的虚拟注释，从而在利用虚拟库扩大覆盖面的同时，显著降低假阳性率。

> “To mitigate this, in silico annotations are retained only when they meet a chemical dice similarity ≥ 0.75 to co-occurring experimental annotations within the same cluster.”

#### 问题二：为什么本研究发现的 kutznaposides 生物合成途径难以通过传统的基因组挖掘方法（如 antiSMASH）预测？

**回答：** 有两个主要原因。首先，**基因簇的非典型性**：负责 kutznaposides 生物合成的关键基因，包括 menaquinone 核心合成基因 (*knp*)、酰胺转移酶基因 (*gat*) 和糖基转移酶基因 (*gts*)，在 *K. viridogrisea* 基因组中是**分散分布**的，并未紧密连锁形成一个典型的、可用于生物信息学工具识别的生物合成基因簇 (BGC) (Figure 5D, Table S2)。其次，**途径的“拼凑”特性**：该途径利用了细胞初级代谢（menaquinone 合成）的核心酶系，并额外招募了在基因组其他位置、可能具有其他原始功能的修饰酶（GAT, GTs）。这种“招募-重组”形成的代谢通路，超出了当前主要基于基因簇同源性搜索的基因组挖掘工具的预测范围。

> “Moreover, neither GTs nor GTs glycosylated DHNA, indicating that glycosylation likely occurs after amidotransferase-mediated modification... These findings indicate that kutznaposides are not readily identifiable using traditional bottom-up genome mining strategies, underscoring the powerful capability of MSanalyst to target valuable metabolites derived from noncanonical metabolic pathways directly.”

#### 问题三：蛋白质组学分析如何支持“menaquinone 分流途径是应对氧化压力策略”这一假设？

**回答：** 定量蛋白质组学提供了多个层次的证据支持这一假设：
1.  **压力响应通路上调**：GO 富集分析显示，在产生 kutznaposides 的 GSM 条件下，与“异生物代谢过程”和“细胞对异生物刺激的反应”相关的蛋白显著上调 (Figure 6B)，这是经典的解毒和应激反应标志。
2.  **有氧代谢增强**：KEGG 分析显示“丙酸代谢”和“氨基酸代谢”通路富集 (Figure 6C)。更关键的是，三羧酸循环中的所有检测到的酶均显著上调 (Figure 6E)，且菌体生物量翻倍，共同表明 GSM 条件下菌体处于旺盛的有氧代谢状态，这通常伴随 ROS 生成增加。
3.  **ROS 生成相关酶的表达模式**：研究发现喹啉酸合成通路（NAD⁺合成）和乙醛酸代谢通路中的关键氧化酶表达上调，而过氧化氢酶缺失 (Figure 6E)。这种酶谱组合极易导致细胞内 H₂O₂ 等 ROS 的积累，创造了氧化压力环境。
4.  **解毒途径关键酶的诱导表达**：正是在这种氧化压力背景下，负责将有毒抗氧化剂 DHNA 解毒的酶（GAT1, **GT5**, **GT6**）被特异性诱导高表达 (Figure 5A, 5B)。将压力信号（ROS累积）、毒性物质（DHNA）的产生以及解毒酶（GAT, GTs）的激活在蛋白质组水平上关联起来，构成了支持该假设的完整证据链。

---
## 美国匹兹堡大学吴祺豪组硕士招生启事

吴祺豪博⼠ (Qihao Wu, Ph.D.) 现任匹兹堡⼤学药学院药物科学系 (Pharmaceutical Sciences,
University of Pittsburgh) 助理教授 (Assistant Professor)。

课题组目前有2026年秋季硕士名额若干，详情请联系吴博士(qiw153@pitt.edu)或者查看课题组主页https://wulabpitt.com

吴博⼠在浙江⼯业⼤学药学院获博⼠学位，师从王鸿教授，并作为浙江⼯业⼤学-美国罗德岛⼤学-中国科学院上海药物所联合培养博⼠，在上海药物所郭跃伟研究员课题组完成博⼠课题研究。随后在普林斯顿⼤学 (Princeton University)、威斯康星⼤学麦迪逊分校 (University of Wisconsin–Madison) 和耶鲁⼤学 (Yale University) 进⾏博⼠后与副研究员阶段训练，系统开展微⽣物来源⼩分⼦化合物化学⽣物学研究。

吴博⼠长期从事海洋天然产物化学与肠道微⽣物代谢机制研究，围绕“共⽣微⽣物与宿主互作”，聚焦⼩分⼦发现与作⽤机理解析，发展了结合代谢组学、基因组学与化学⽣物学的
活性分⼦挖掘与酶机制解析研究。近五年来，课题组依托多学科交叉融合，围绕共⽣微⽣物与宿主互作的药物发现与开发展开系统研究，并取得⼀系列创新性成果：(1) 以化学⽣态学-代谢组学为导向，从海洋软体动物、珊瑚及海绵中⾼效发现百余个结构新颖、⽣理活性显著的复杂海洋天然产物 (Angew. Chem. Int. Ed. 2020)；(2) 建⽴结合代谢组学、基因组学分析及⽣物活性筛选的技术体系，实现了微⽣物次级代谢产物的⾼效筛选，成功鉴定出多种新⾻架活性天然产物 (J . Am. Chem. Soc. 2023; J . Am. Chem. Soc. 2025a; J . Am. Chem. Soc.2025b; Cell Chem. Biol. 2025)；(3) 开发基于离体培养-⾼通量质谱代谢组学的技术平台，系统解析⼈体肠道共⽣细菌对⼝服 G 蛋⽩偶联受体 (GPCR) 药物的结构修饰，揭⽰了多条新颖的药物代谢通路及其对药物活性的调控作⽤(Nat. C hem. 2025; C ell 2020)。

### 近期研究工作

[2025 Nat. Chem. | 人类肠道菌群代谢影响 GPCR 靶向药的活性](https://mp.weixin.qq.com/s/NtvNO_SquQ_5SELygo1E_Q)

[2025 JACS | 一个嵌合型聚酮类癌症免疫原性化疗先导化合物的发现](https://mp.weixin.qq.com/s/KGBbu6-Af2gBiwDKCIpK1Q)

[2025 JACS | 一种含钴的萜烯-聚酮-非核糖体肽三混源抗冠状病毒天然产物的发现与生物合成研究](https://mp.weixin.qq.com/s/rWn5_MDZsGpQcY6gSnzSbA)