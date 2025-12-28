![image.png](http://synbiopath.online/20251228191843056.png)


---

## 一：基本信息

**文章题目**：Concise Biosynthesis of Antifungal Papulacandins（）

**文章 DOI 号**：10.1021/jacs.4c13101

**期刊名称**：*Journal of the American Chemical Society*

**通讯作者**：张转 (Zhuan Zhang)；Gerald F. Bills；安志强 (Zhiqiang An), 

**通讯作者工作单位**：
*   **张转**：中国医学科学院北京协和医学院医药生物技术研究所，微生物药物生物技术国家卫生健康委员会重点实验室 (NHC Key Laboratory of Biotechnology for Microbial Drugs, Institute of Medicinal Biotechnology, Chinese Academy of Medical Sciences & Peking Union Medical College, Beijing, People’s Republic of China)
*  **Gerald F. Bills**：德克萨斯大学休斯顿健康科学中心，布朗基金会分子医学研究所，德克萨斯治疗研究所 (Texas Therapeutics Institute, The Brown Foundation Institute of Molecular Medicine, University of Texas Health Science Center at Houston, Houston, Texas, United States)
*   **安志强**：德克萨斯大学休斯顿健康科学中心，布朗基金会分子医学研究所，德克萨斯治疗研究所 (Texas Therapeutics Institute, The Brown Foundation Institute of Molecular Medicine, University of Texas Health Science Center at Houston, Houston, Texas, United States)

---

## 二：核心速览

### 研究背景
Papulacandins 是一类最早于1976年从真菌 *Papularia sphaerosperma* 中分离出的天然抗真菌剂。其核心药理机制为抑制 $\beta$-(1,3)-D-葡聚糖合成酶 (GS)，破坏真菌细胞壁合成。其中，Papulacandin B 对 GS 的 $\text{IC}_{50}$ 值低至 $0.02\ \mu\text{g/mL}$，效力是抗真菌药物卡泊芬净 (caspofungin) 的 10 倍。结构上，这类化合物包含独特的苯并螺环缩酮 (benzannulated spiroketal) 骨架，该结构单元是其抗真菌活性的关键决定因素。
![image.png](http://synbiopath.online/20251228192035534.png)

### 前期研究
尽管 Papulacandins 具有显著的药用潜力，但其复杂的结构使得化学全合成极具挑战性。目前仅有结构最简单的 Papulacandin D (2) 实现了全合成，需 31 步反应，总产率仅为 9.2%。该类化合物生物合成途径的缺失，限制了对其进行生物工程改造以获取更优类似物的能力。

### 本文突破点
1.  **完整途径解析**：首次完整解析了 Papulacandins 的生物合成基因簇 (*ppc*)，确立了其采用“五组分汇聚式”合成策略。
2.  **关键酶学机制阐明**：
    *   发现并表征了 **PpcD**，一种具有独特区域选择性的芳基 C-糖基转移酶。
    *   揭示了 **PpcE**，一种 Fe(II)/$\alpha$-酮戊二酸依赖性加氧酶，负责催化高难度的氧化螺环化反应，构建苯并螺环核心。
    *   鉴定了一种罕见的融合肉碱酰基转移酶结构域 (cAT) 的 HRPKS (**PpcF**)，能直接将聚酮链酯化到芳基 C-糖苷上。
3.  **异源合成**：在 *Aspergillus nidulans* 和 *E. coli* 中成功重构了关键步骤，并实现了目标产物的酶法合成。

### 研究难点
*   **螺环构建机制**：苯并螺环缩酮结构的酶学形成机制在真菌次级代谢中极为罕见，需区分氧化、脱氢或自由基机制。
*   **多组分装配顺序**：分子涉及芳环、糖基、不同链长的脂肪酸链，确定各组分的精确装配顺序（特别是酰基化与螺环化的先后关系）是逻辑难点。

---

## 三：研究思路

本研究遵循“基因挖掘 $\rightarrow$ 逐步异源表达 $\rightarrow$ 体外酶学表征 $\rightarrow$ 机制解析”的逻辑路径：

**步骤 1：基因簇挖掘与鉴定**

基于 Papulacandin D 的逆合成分析，推测其生物合成涉及 NRPKS（非还原型聚酮合酶）。利用已知的 orsellinic acid 合成酶 ArmB 序列作为探针，在生产菌 *Codinaeella minuta* 基因组中锁定了一个包含 10 个基因的 *ppc* 基因簇 (Figure 2A)。

**步骤 2：芳香前体合成模块的功能验证**

在异源宿主 *Aspergillus nidulans* A1145 中逐步表达 *ppcA-C*。通过代谢产物分析，确定 PpcA (NRPKS) 合成 orsellinic acid，PpcB (脱羧酶) 将其转化为 3,5-dihydroxytoluene，PpcC (P450) 进一步羟基化生成关键前体 3,5-dihydroxybenzyl alcohol (**5**)。

**步骤 3：C-糖基化与螺环化机制解析 (核心突破)**

在大肠杆菌中表达 PpcD 和 PpcE。体外酶活实验证实 PpcD 将 UDP-葡萄糖连接至前体 **5** 形成 C-糖苷 (**6**)；随后 PpcE 在 Fe(II) 和 $\alpha$-酮戊二酸存在下，催化 **6** 发生氧化螺环化生成 deacylated papulacandin D (**7**)。

**步骤 4：酰基化装配逻辑确证**

在 *A. nidulans* 中组合表达 *ppcD/ppcE* 和 *ppcD/ppcF*，发现 PpcF (HRPKS-cAT) 负责 C3-OH 位的长链脂肪酸酰基化。通过底物饲喂实验，确定了必须先进行 PpcE 介导的螺环化，再进行 PpcF 介导的酰基化，从而生成 Papulacandin D (**2**)。

**步骤 5：后修饰与全合成途径补全**

通过体外实验证实 PpcG 为半乳糖基转移酶，将半乳糖连接至 Papulacandin D (**2**)。最后结合 PpcI (P450) 和 PpcH (酰基转移酶) 的功能推导，完成了从 Papulacandin D 到最终产物 L-687,781 (**1**) 的生物合成路径构建。

---

## 四：研究方法

*   **全基因组测序与生物信息学分析**: 对 *Codinaeella minuta* 进行测序，利用 BLAST 和 antiSMASH 进行基因簇挖掘。
*   **异源表达 (Heterologous Expression)**: 使用 *Aspergillus nidulans* A1145 作为真菌宿主，逐步引入 *ppc* 基因簇成员，构建不同组合的突变株。
*   **重组蛋白表达与纯化**: 在 *E. coli* BL21(DE3) 中表达 PpcD, PpcE, PpcG 等蛋白，并进行镍柱亲和纯化。
*   **体外酶活测定 (In vitro Enzymatic Assay)**: 构建含底物、辅因子（如 UDP-Glucose, $\alpha$KG, Fe(II)）的反应体系，通过 HPLC 和 HRMS 检测产物。
*   **波谱学结构鉴定**: 利用 NMR ($^1$H, $^{13}$C, 2D) 和 HRMS 确定分离化合物及酶反应产物的化学结构。
*   **分子模拟与对接**: 使用 AlphaFold2 预测 PpcE 结构，结合 AutoDock 进行底物分子对接，辅助机制推测。

---

## 五：实验设计及结果分析

### 研究部分一：生物合成基因簇的鉴定与早期途径重构
#### 实验目的与设计
确定 Papulacandin 的生物合成基因簇，并验证负责芳香环骨架合成的基因功能。

#### 实验结果与分析
*   **基因簇定位 (Figure 2A)**: 鉴定的 *ppc* 基因簇包含 10 个基因。NCBI 比对显示该簇在多种植物致病真菌中保守 (Figure S2)。
![image.png](http://synbiopath.online/20251228192101075.png)

*   **早期代谢物鉴定 (Figure 2C, Figure S4)**:
![image.png](http://synbiopath.online/20251228192226130.png)
*   表达 *ppcA* 产生 orsellinic acid (**3**)。
*   共表达 *ppcA/B* 产生 3,5-dihydroxytoluene (**4**)。
*   共表达 *ppcA/B/C* 产生 3,5-dihydroxybenzyl alcohol (**5**)。
*   **结论**: 这一系列转化确立了 Papulacandin 的芳香核心来源于 PKS 途径，并经脱羧和氧化修饰。

### 研究部分二：C-糖基化与关键螺环骨架的构建
#### 实验目的与设计
阐明独特的 C-糖苷键及苯并螺环缩酮结构的形成机制。

#### 实验结果与分析
**PpcD 的 C-糖基化活性 (Figure 2D)**:
![image.png](http://synbiopath.online/20251228192312596.png)

*   体外实验显示 PpcD 能催化 **5** 与 UDP-glucose 反应生成化合物 **6**。
*   **动力学参数**: $k_{cat}/K_M$ 值为 $246.7\ \text{mM}^{-1}\text{s}^{-1}$，显示出极高的催化效率。
*   **区域选择性**: NMR 证实糖基化发生在前体 **5** 的 C2 位（两个羟基之间），且为 $\beta$-构型。这与常规酚 C-糖基转移酶（通常作用于邻二酚结构）不同，具有独特的区域特异性。
**PpcE 的螺环化活性 (Figure 2D, 2C)**:
![image.png](http://synbiopath.online/20251228192332113.png)

*   在 *A. nidulans* 中共表达 *ppcD* 和 *ppcE* 产生了化合物 **7** (deacylated papulacandin D)。
*   体外实验证实 PpcE 需要 $\alpha$-酮戊二酸 ($\alpha$KG) 和 Fe(II) 作为辅因子，将化合物 **6** 转化为 **7**。
*   **动力学参数**: $k_{cat}/K_M$ 值为 $29.7\ \text{mM}^{-1}\text{s}^{-1}$。
**机制推测 (Figure 2E)**: 分子对接与定点突变（W242F 失活）表明，PpcE 通过 Fe(IV)-oxo 物种夺取 C1 氢原子启动反应，经自由基或阳离子中间体，由苄位羟基进行分子内亲核进攻闭环。这扩展了 $\alpha$KGD 酶家族的反应类型。
![image.png](http://synbiopath.online/20251228192408038.png)

> "The formation of the challenging tricyclic benzannulated spiroketal core is initiated by the C-glycosylation... followed by spirocyclization catalyzed by a Fe(II)/$\alpha$-ketoglutarate-dependent oxygenase PpcE."

### 研究部分三：酰基化修饰与装配顺序的逻辑
#### 实验目的与设计
解析两条脂肪酸链（C3位和C6'位）的引入机制及次序。

#### 实验结果与分析
  **PpcF 的特殊功能 (Figure 2C, Figure 3)**:
    *   在 *A. nidulans* 中共表达 *ppcD* 和 *ppcF* 产生了化合物 **8**（3-OH 被酰基化，但未螺环化）。
    *   **顺序验证**: 化合物 **8** 无法被 PpcE 转化为 Papulacandin D (**2**)；反之，化合物 **5** 在表达 *ppcD-F* 的菌株中能生成 **2**。这证明生物合成必须遵循 **先螺环化 (PpcE) 后酰基化 (PpcF)** 的顺序。
    *   **酶学特征**: PpcF 是首个被鉴定的直接将聚酮链酯化到芳基 C-糖苷上的 HRPKS-cAT 融合酶。
  **PpcG 的半乳糖基化 (Figure 3B)**:
    *   体外实验显示 PpcG 能利用 UDP-galactose 将 **2** 转化为 **10**，也能将 **8** 转化为 **9**。表明 PpcG 对底物螺环结构不敏感，但在天然路径中应作用于 **2** 之后。

### 研究部分四：终产物 L-687,781 的合成与全途径整合
#### 实验目的与设计
完成从 Papulacandin D (**2**) 到最终复杂产物 **1** 的转化。

#### 实验结果与分析
*   **PpcI 与 PpcH 的协同作用 (Figure 3C)**:
    *   仅在表达完整 *ppcD-I* 基因簇并补加 (2E,4Z)-deca-2,4-dienoic acid 的 *A. nidulans* 中检测到最终产物 **1**。
    *   推测 P450 酶 **PpcI** 负责脂肪酸链 C-8'' 位的羟基化，生成中间体 **12**。
    *   膜蛋白酰基转移酶 **PpcH** 随后将培养基中的特定不饱和脂肪酸连接至半乳糖的 6-OH 位。
    *   **结论**: 成功在异源宿主中重构了 Papulacandin 的全生物合成途径。

---

## 六：总体结论

本研究通过基因组挖掘和系统的生化表征，阐明了抗真菌剂 Papulacandin 的“五组分汇聚式”生物合成途径。核心发现包括：(1) 由 PpcD 和 PpcE 协同完成的 C-糖基化耦合氧化螺环化过程，高效构建了苯并螺环骨架；(2) 由 PpcF (HRPKS-cAT) 执行的独特酰基化机制；(3) 严格的底物传递逻辑（先成环后酰基化）。该研究不仅解决了一个长期存在的生物合成难题，也为该类重要抗真菌药物的生物制造和结构修饰奠定了基础。

---

## 七：论文评价

### 优点与创新
*   **机制创新**: 首次发现 $\alpha$-酮戊二酸依赖性加氧酶 (PpcE) 用于构建苯并螺环缩酮结构，拓展了该酶家族的催化潜能。
*   **策略严谨**: 结合了体内异源表达和体外酶动力学分析，特别是通过中间体饲喂实验严格确证了酶的催化顺序，逻辑严密。
*   **合成生物学价值**: PpcF 作为一个能直接装载聚酮链的融合酶，为聚酮类化合物的生物工程改造提供了新的酶学元件。

### 未来研究方向
*   **酶工程改造**: 针对 PpcE 和 PpcF 进行定向进化，以接纳非天然底物，创造具有新颖骨架或脂肪酸链的衍生物。
*   **产量优化**: 目前异源表达的产量数据未详细讨论，未来需在工业微生物底盘中优化代谢流以提升产量。

---

## 八：关键问题及回答

#### 问题一：PpcE 催化螺环化的具体机制是什么？有何证据支持？
**回答：** PpcE 是一种 Fe(II)/$\alpha$-酮戊二酸依赖性加氧酶。其机制被提议为：Fe(IV)-oxo 物种首先夺取底物 C1 位的氢原子（分子对接显示距离为 3.8 Å），形成底物自由基。随后，通过两种可能的路径（直接自由基偶联或电子转移形成碳正离子后发生亲核进攻），由苯甲醇羟基进攻 C1 位形成 C-O 键，完成螺环化。突变实验证实活性位点的 W242 残基可能作为碱辅助酚羟基质子的移除（W242F 突变导致活性几乎丧失）。

#### 问题二：为什么说 PpcF 是一个“非典型”的酶？
**回答：** 典型的 HRPKS (高度还原型聚酮合酶) 通常需要独立的释放机制或硫酯酶结构域。PpcF 的独特性在于它在其 C 端融合了一个肉碱酰基转移酶样结构域 (carnitine acyl-transferase-like domain, cAT)。这使得 PpcF 不仅能合成聚酮链，还能直接将该链作为酰基供体，转移并酯化到芳基 C-糖苷的特定羟基上。这是首例报道的具有此类功能的聚酮合酶，简化了酰基链的装载过程。