![image.png](http://synbiopath.online/20260116104814822.png)

---

# 一：基本信息

**文章题目**：Evolution-Guided Discovery of Antimycobacterial Triculamin-Like Lasso Peptides

**文章 DOI 号**：10.1002/anie.202425134

**期刊名称**：Angewandte Chemie International Edition

**通讯作者**：Thomas Tørring, Marc G. Chevrette

**通讯作者工作单位**：
*   Thomas Tørring: 奥胡斯大学生物与化学工程系 (Department of Biological & Chemical Engineering, Aarhus University)
*   Marc G. Chevrette: 佛罗里达大学微生物与细胞科学系; 佛罗里达大学遗传学研究所 (Department of Microbiology & Cell Sciences, University of Florida; University of Florida Genetics Institute, University of Florida)

---

## 二：核心速览

### 研究背景
核糖体合成和翻译后修饰肽是一类结构、生物合成方式和生物活性高度多样化的天然产物。套索肽 是 RiPPs 的一个子类，通常具有由前导肽、RiPP 识别元件 (RRE, B1)、肽酶 (B2) 和大环化酶 (C) 组成的典型生物合成基因簇 (BGC)。然而，三苦胺 是一种具有抗分枝杆菌活性的套索肽，其 BGC 极其不典型，缺失了 B1 和 B2 基因，且前体肽 (triA) 缺乏前导序列 而包含 Follower 序列，其生物合成机制尚不明确。

### 前期研究
作者此前曾报道过三苦胺的结构及其不寻常的 BGC 结构。已知三苦胺具有高度的阳离子氨基酸，且其 BGC 中包含一个截短的大环化酶 triC，缺失了其他套索肽大环化酶 N 端约 150-250 个氨基酸的结构域。

### 本文突破点
1.  阐明了三苦胺的生物合成途径，确定了四个必需基因 (*triA*, *triC*, *triD*, *triT*)。
2.  发现 N-乙酰转移酶 triT 能够通过乙酰化修饰三苦胺从而使其失活，揭示了这是一种自抗性 机制。
3.  通过基因组挖掘发现类三苦胺 BGC 广泛分布于多个细菌门类（放线菌门、厚壁菌门、变形菌门），且存在典型和非典型两种截然不同的 BGC 构型。
4.  发现并表征了两种新型类三苦胺套索肽：棕榈胺 和明胶胺，后者具有独特的双大环内酯结构。
5.  提出类三苦胺套索肽是天然产物中趋同进化 的罕见案例，且可能是 RiPPs 中的首例。

### 研究难点
1.  三苦胺 BGC 的非典型性导致其异源表达 初期失败，需要重新解析其基因组成。
2.  需要在基因组尺度上区分典型与非典型 BGC，并确证不同进化来源的酶是否能产生结构相似的产物。
3.  明胶胺的双大环内酯结构较为罕见，其形成机制（特别是 C 端到赖氨酸侧链的成环）需要通过质谱数据进行推断。

---

## 三：研究思路

**步骤 1：目标基因簇的异源表达与必需基因鉴定**
利用 *Streptomyces albus* J1074 作为宿主，克隆 *Streptomyces triculaminicus* 的 BGC。初期克隆 *triACD* 失败后，重新审视基因组背景，引入 *triT* 和 *H* 基因。通过构建一系列基因缺失突变体，逐一验证每个基因在生物合成中的必要性，并利用 LC-MS 检测产物。

**步骤 2：TriT 酶的功能表征与抗性机制验证**
为了探究 *triT* 的功能，对重组 TriT 蛋白进行异源表达与纯化。通过体外酶学反应，将 TriT、乙酰辅酶 A (AcCoA) 与三苦胺 B 共孵育，利用 LC-MS 和生物活性测定验证乙酰化修饰及其对活性的影响，从而确证其抗性机制。

**步骤 3：跨门类的类三苦胺 BGC 生物信息学挖掘与系统发育分析**
基于已知的类三苦胺核心肽序列，在 NCBI 数据库中进行广泛搜索。鉴定典型与非典型 BGC 的分布特征，并重点构建大环化酶 的系统发育树，分析其进化关系，探究是否存在趋同进化。

**步骤 4：典型 BGC 来源产物的异源表达与鉴定（棕榈胺）**
选择包含典型 BGC（具有前导肽和完整修饰酶系）的 *Chitinasicproducens palmae*，尝试异源表达。由于 *E. coli* 表达失败，选用伯克霍尔德氏菌 作为宿主进行异源表达，利用 LC-MS/MS 鉴定产物。

**步骤 5：非典型 BGC 来源产物的分离与结构解析（明胶胺）**
选择 *Brevibacillus gelatini* 进行发酵培养，利用 OSMAC 策略诱导产物合成。通过阳离子交换色谱分离活性组分，利用高分辨质谱和 MS2 碎片离子分析，推断其双大环内酯结构及乙酰化修饰位点。

**步骤 6：验证乙酰化抗性机制的普适性**
使用已纯化的 TriT 酶对新发现的明胶胺进行体外乙酰化实验，检测其活性变化，验证该抗性机制是否适用于类三苦胺肽家族。

---

## 四：研究方法

**异源表达**: 使用 *Streptomyces albus* J1074 和 *Burkholderia* sp. FERM-3421 作为宿主，通过接合转移或电转化将目标 BGC 克隆至表达载体（如 pL99, pHNF008），实现目标化合物的生产。

**液相色谱-质谱联用 (LC-MS/MS)**: 用于发酵产物的定性与定量分析，监测分子量变化（如乙酰化修饰引起的 +42 Da 位移），并通过二级质谱 (MS2) 碎片离子推断氨基酸序列和成环方式。

**基因缺失**: 在异源表达载体上构建单个基因的缺失突变体，通过对比产物合成情况确定基因功能。

**体外酶学实验**: 将重组表达并纯化的 TriT 酶与底物（三苦胺/明胶胺）及 AcCoA 在体外反应体系中共孵育，模拟体内的乙酰化过程。

**生物活性测定**: 采用纸片扩散法或点种法，测定化合物或反应混合物对耻垢分枝杆菌 和 *Mycobacterium phlei* 的抑制活性。

**系统发育分析**: 基于 BLAST 搜索和序列比对，构建大环化酶蛋白序列的系统发育树，分析不同 BGC 类型及来源菌之间的进化关系。

---

## 五：实验设计及结果分析

### 研究部分一：三苦胺生物合成基因簇的解析与异源表达
#### 实验目的与设计
旨在确定 *S. triculaminicus* 中三苦胺生物合成所需的最小基因集，并解析各基因的具体功能。

#### 实验结果与分析
研究者首先尝试在 *S. albus* 中异源表达最初鉴定的 *triACD* 基因簇，但未能检测到三苦胺产物。回顾原始菌株提取物时，发现除了已知的 triculamin A 外，还存在 C 端多一个 Arg 的 triculamin B 以及它们各自的乙酰化形式（质量增加 42 Da）。这提示乙酰化修饰的存在。重新审视 BGC 周围序列后，发现了一个 N-乙酰转移酶基因 *triT* 和一个转录调节基因 *H*。

随后，研究者构建了包含 *triACDHT* 的质粒并转化 *S. albus*，成功检测到了 triculamin B 及其乙酰化形式。为明确各基因作用，构建了系列缺失突变体：
![image.png](http://synbiopath.online/20260116105154388.png)

*   **Figure 1 分析**: Figure 1c 展示了不同基因缺失突变体的 LC-MS 色谱图。
    *   **ΔtriA** 和 **ΔtriC**: 完全未检测到产物，证实前体肽和大环化酶是生物合成所必需的。
    *   **ΔtriT**: 虽然未检测到乙酰化产物，但非乙酰化的 triculamin B 产量显著下降，且产物主要集中在胞内。这表明 *triT* 并非大环化反应所必需，但其缺失导致产物滞留胞内，可能影响转运或稳定性。
    *   **ΔtriD**: 产物产量降低，且检测到的产物几乎完全为乙酰化形式。这提示转运蛋白 *triD* 负责将产物排出胞外；当转运受阻时，产物在胞内积累并被 *triT* 乙酰化。
    *   **ΔH**: 产物产量与对照组相当，表明转录调节基因 *H* 在异源宿主中可能不发挥主要调控作用。

综上所述，*triA*（前体）、*triC*（大环化酶）和 *triT*（乙酰转移酶）是三苦胺在 *S. albus* 中生物合成所必需的，而 *triD* 负责产物外排。值得注意的是，*triT* 的缺失虽然阻碍了乙酰化，但也导致了产量的下降，提示其在生物合成过程中可能具有辅助折叠或调控作用。

> "The chromatograms in Figure 1c demonstrate that triA, triC, and triT were required and sufficient to produce triculamin in S. albus J1074."

### 研究部分二：TriT 酶的功能表征及其作为自抗性机制的验证
#### 实验目的与设计
明确 *triT* 编码的 N-乙酰转移酶的功能，特别是验证其乙酰化修饰是否作为一种自我抗性机制。

#### 实验结果与分析
为了验证 *triT* 的功能，研究者在 *E. coli* 中表达了带有 His 标签的 TriT 蛋白并进行了纯化，产量约为 6 mg/L 发酵液。随后进行了体外酶促反应：

**Figure 2 分析**: Figure 2 展示了体外乙酰化反应的结果。
![image.png](http://synbiopath.online/20260116105226107.png)

*   **Figure 2a**: 反应示意图，TriT 以 AcCoA 为供体，对三苦胺 B 进行乙酰化，可能位点为赖氨酸 (K2, K3, K5)。
*   **Figure 2b & c**: LC-MS 结果显示，三苦胺 B (x) 与 AcCoA (y) 共孵育无变化；但加入 TriT (z) 后，检测到了分子量增加 42 Da 的单乙酰化产物 (4, 5) 以及少量双乙酰化产物 (6)。质谱图显示峰形较宽，提示乙酰化可能发生在多个赖氨酸位点。
*   **Figure 2d**: 生物活性测定结果显示，三苦胺 B (x) 及其与 AcCoA 的混合物 (y) 对耻垢分枝杆菌 和 *M. phlei* 具有明显的抑制活性（出现了抑菌圈）。然而，经 TriT 乙酰化后的反应混合物 (z) 完全失去了抗菌活性。

这一结果直接证实了 TriT 能够利用 AcCoA 对三苦胺进行乙酰化修饰，且该修饰导致抗生素活性丧失。这表明 *triT* 在 BGC 中的主要作用是作为一种自我抗性机制，通过乙酰化来保护宿主菌免受自身产生的抗生素的伤害。

> "The results shown in Figure 2, clearly demonstrate that not only is triculamin B fully acetylated (M+42 Da), but it also loses activity against the Mycobacteria tested."

### 研究部分三：类三苦胺 BGC 的跨门类分布与大环化酶的系统发育分析
#### 实验目的与设计
探究类三苦胺 BGC 在自然界中的分布范围，分析其进化关系，验证其是否为趋同进化的产物。

#### 实验结果与分析
研究者基于三苦胺的核心肽序列在细菌基因组中进行了广泛的挖掘。结果显示，类三苦胺核心肽不仅存在于放线菌门，还存在于变形菌门 和厚壁菌门，这与通常局限于单一门类的套索肽形成鲜明对比。研究者发现了两类 BGC：非典型 BGC（如三苦胺，含 Follower 序列和截短的大环化酶）和典型 BGC（含前导肽、RRE、肽酶和完整大环化酶），且两类 BGC 核心肽序列高度相似。

**Figure 3 分析**: Figure 3 展示了基于大环化酶序列构建的系统发育树。
![image.png](http://synbiopath.online/20260116105306086.png)

*   树中包含三个折叠节点（灰色为天冬酰胺合成酶样蛋白，蓝色为 β-内酰胺合成酶，红色为其他套索肽大环化酶）。
*   **内圈颜色**：深紫色代表典型类三苦胺 BGC，浅紫色代表非典型类三苦胺 BGC。
*   **分支分布**: 非典型 BGC 的大环化酶主要分布在放线菌门，少数在蓝细菌门、变形菌门和浮霉菌门；典型 BGC 的大环化酶则主要分布在变形菌门和芽孢杆菌门。
*   **进化关系**: 系统发育树显示，来自典型和非典型 BGC 的大环化酶虽然都能产生类三苦胺核心肽，但它们在进化上相距甚远。非典型类三苦胺分支与一个包含 *Stlassin*, *Lihuanodin* 等其他套索肽的折叠分支以及 Barrett 等人综述中的东南侧分支似乎源自共同祖先。而典型的类三苦胺分支则与 Barrett 等人综述中的西北侧基底分支互为姐妹群。
*   **序列保守性**: 所有的前体肽核心序列都包含几乎不变的 PGDG 基序（以形成大环内酯的 Asp 为中心）以及大量的带正电荷氨基酸 (K, R, H)。典型分支的前导肽缺乏通常在 -2 位的 Thr，这导致依赖该位点进行预测的 antiSMASH 等软件无法识别这些前导肽。

这种“结构高度相似但酶系进化关系疏远”的现象强烈提示了趋同进化的存在。即不同进化谱系的细菌为了应对类似的生态压力（如抗分枝杆菌竞争），独立进化出了产生结构相似套索肽的能力。

> "The deep branching separating the non-canonical and canonical containing groups suggests independent origins of triculamin-like macrocyclases and convergent or parallel evolution the triculamin-like lasso peptides."

### 研究部分四：典型 BGC 产物棕榈胺 的异源表达与鉴定
#### 实验目的与设计
验证包含典型 BGC 架构的菌株是否确实能产生类三苦胺肽，并解析其结构。

#### 实验结果与分析
研究者选择了 *Chitinasicproducens palmae*（属于伯克霍尔德氏菌科），其 BGC 具有典型的架构：包含大环化酶 (palC)、RRE (palB1)、肽酶 (palB2)、转运蛋白 和带有前导肽的前体。由于 OSMAC 策略未能诱导产物，研究者尝试异源表达。

**Figure 4 分析**: Figure 4 展示了棕榈胺的异源表达过程及结果。
![image.png](http://synbiopath.online/20260116105335785.png)

*   **Figure 4a**: 展示了从 *C. palmae* 克隆 *pal* BGC 并在 *Burkholderia* sp. FERM-3421 中表达的流程。
*   **Figure 4b**: 典型套索肽的生物合成假设示意图，包括前体被 B1、B2、C 蛋白翻译后修饰的过程。
*   **Figure 4c**: LC-MS 色谱图显示，含有 *pal* BGC 的发酵液在特定保留时间出现了一个新峰，其分子量与理论预测的棕榈胺质量一致，而空载体对照组无此峰。
*   **Figure 4d**: 该新峰的 MS2 质谱图显示了套索肽特征性的 b 离子和 y 离子碎片，确认了其与预测的套索肽结构一致。

这一结果成功证明了即便基因架构完全不同（典型 vs 非典型），不同来源的酶系确实能产生高度相似的套索肽。

> "This confirms the successful heterologous expression and demonstrates that distinct biosynthetic machinery found in distantly related bacteria can produce nearly identical lasso peptides."

### 研究部分五：新型双大环内酯套索肽明胶胺 A 的发现
#### 实验目的与设计
从具有典型 BGC 的 *Brevibacillus gelatini* 中分离并鉴定类三苦胺产物，解析其特殊的结构特征。

#### 实验结果与分析
研究者对 *B. gelatini* 进行了发酵，通过阳离子交换色谱分离了活性组分。

**Figure 5 分析**: Figure 5 展示了明胶胺的分离与结构解析。
![image.png](http://synbiopath.online/20260116105413513.png)

*   **Figure 5a**: *B. gelatini* 的 BGC 示意图，除了典型的 *A, B1, B2, D* 基因外，还包含一个 Clostripain 家族肽酶和一个 N-乙酰转移酶。
*   **Figure 5b**: 总结了发酵液中发现的明胶胺变体，包括乙酰化和非乙酰化形式，以及单脱水和双脱水形式。
*   **Figure 5c**: LC-MS 去卷积色谱图显示，主要产物 8 和 9 的分子量分别为 1741 Da 和 1783 Da，相差 42 Da（乙酰化）。与理论预测质量相比，存在 C 末端 Gly 缺失和一个脱水反应的质量差异。
*   **Figure 5d**: MS2 质谱图显示，常规套索肽 C 端尾巴的特征碎片离子完全缺失。取而代之的是出现了双碎片离子，这符合在赖氨酸 (K2 或 K5) 侧链氨基与 C 端之间形成第二个大环内酯的结构特征。此外，还检测到了单乙酰化 (9) 和双乙酰化 (10) 产物。

基于质谱数据和 BGC 中存在的 Clostripain 家族蛋白酶，研究者推测该酶催化了转肽反应，导致 C 末端 Gly 被切除，并与赖氨酸侧链成环，形成了独特的双环套索肽。

> "The mass difference, lacking tail fragments, and the MS2 spectra observed in Figure 5d are consistent with macrolactamization between the C-terminus and a lysine residue located in the normal lasso peptide macrolactam."

### 研究部分六：TriT 酶对明胶胺的乙酰化修饰及抗性机制普适性验证
#### 实验目的与设计
验证 TriT 乙酰转移酶对新发现的明胶胺是否具有同样的修饰活性，并确认该抗性机制的普适性。

#### 实验结果与分析
研究者将纯化的 TriT 酶与明胶胺 A 在体外进行共孵育。

**Figure 6 分析**: Figure 6 展示了明胶胺的体外乙酰化结果。
![image.png](http://synbiopath.online/20260116105445880.png)

*   **Figure 6a**: 明胶胺的单乙酰化和双乙酰化示意图。
*   **Figure 6b**: LC-MS 结果显示，明胶胺 (x) 与 TriT 及 AcCoA 反应后 (z)，主要转化为双乙酰化产物 (10)，且检测到了少量三乙酰化产物 (*)。
*   **Figure 6c**: 生物活性测定显示，明胶胺 (x) 及其与 AcCoA 的混合物 (y) 对分枝杆菌有显著抑制活性。然而，经 TriT 乙酰化后的反应混合物 (z) 活性完全消失。
*   **Figure 6d**: MS2 图谱确认了单乙酰化 (9) 和双乙酰化 (10) 明胶胺的结构。

尽管 TriT 与明胶胺自身 BGC 中的 GelT 序列相似度较低（44.6%），但 TriT 依然能够高效乙酰化明胶胺并使其失活。这证实了乙酰化失活是类三苦胺肽家族中一种普遍且保守的自我抗性机制。

> "Our results in Figure 6c demonstrate that triT acetylated gelatinamin A in two positions which completely abolished the bioactivity of gelatinamin A, further supporting its role as a resistance mechanism."

---

## 六：总体结论

本研究通过异源表达和体外实验，阐明了三苦胺的生物合成途径，确定 *triA*、*triC*、*triD* 和 *triT* 是其生物合成和转运所必需的基因。研究发现 *triT* 编码的 N-乙酰转移酶通过乙酰化修饰使三苦胺失活，作为一种关键的自我抗性机制。基因组挖掘和系统发育分析揭示了类三苦胺 BGC 在放线菌门、变形菌门和厚壁菌门中均有分布，且存在典型和非典型两种截然不同的基因架构。来自不同谱系的大环化酶能够产生高度相似的套索肽，这表明类三苦胺肽可能是 RiPPs 天然产物中趋同进化的首个实例。此外，研究还发现了两种新型类三苦胺肽：棕榈胺 和具有独特双大环内酯结构的明胶胺。这些发现极大地扩展了套索肽的生物合成多样性，为理解非典型 RiPP 途径的进化和功能复杂性提供了新的视角。

> "In this manuscript, we demonstrate that the heterologous expression of the triculamin BGC in S. albus confirms that four genes—triA, triC, triD, and triT—are sufficient and necessary for triculamin biosynthesis and export."

---

## 七：论文评价

### 优点与创新
1.  **首次解析非典型套索肽生物合成机制**：填补了关于缺乏前导肽和 RRE/肽酶的套索肽生物合成机制的知识空白，揭示了 *triA*、*triC* 和 *triT* 的核心作用。
2.  **发现 RiPPs 中的趋同进化案例**：通过宏大的基因组比较和系统发育分析，有力地证明了结构相似的天然产物可以由进化上距离甚远的不同酶系合成，这挑战了人们对 RiPPs 进化保守性的传统认知。
3.  **解析新型 PTM 结构**：发现并确证了明胶胺中由 Clostripain 酶介导的、形成 C 端到赖氨酸侧链第二个大环内酯的独特翻译后修饰，丰富了套索肽的结构多样性。
4.  **阐明普遍的自抗性机制**：通过体外生化实验，确证了乙酰化修饰是类三苦胺肽家族通用的自我抗性策略，理解了微生物如何通过简单修饰保护自身免受抗生素伤害。

### 未来研究方向
1.  **酶学机制深入探究**：进一步阐明非典型大环化酶 TriC 的催化机制，特别是它如何在没有 RRE 辅助的情况下识别和修饰前体肽；解析 Clostripain 酶催化第二个大环内酯形成的具体分子机制。
2.  **生物活性靶点验证**：鉴于近期有研究提示类似三苦胺的肽可能抑制细菌蛋白质合成，需要进一步通过结构生物学（如 X 射线晶体学）方法确证其具体的分子靶点。
3.  **功能与应用拓展**：探索这种双环套索肽是否具有比单环套索肽更优的稳定性或生物活性，评估其作为新型抗生素先导物的潜力。

---

## 八：关键问题及回答

#### 问题一：文中提到的“非典型”和“典型”类三苦胺 BGC 的主要区别是什么？
**回答：**
主要区别在于基因组成和前体肽的结构。
1.  **非典型 BGC (如 tri BGC)**：包含一个截短的大环化酶（缺失 N 端约 150-250 aa），缺失 RRE (B1) 和肽酶 (B2) 基因。其前体肽缺乏前导序列，但包含一个 Follower 序列。代表菌株为 *Streptomyces triculaminicus*。
2.  **典型 BGC (如 pal BGC)**：包含完整的大环化酶、RRE (B1)、肽酶 (B2) 和转运蛋白。其前体肽具有典型的 N 端前导序列。代表菌株为 *Chitinasicproducens palmae* 和 *Brevibacillus gelatini*。尽管基因架构不同，两者产生的核心肽序列高度相似。

#### 问题二：TriT 酶在生物合成中的具体作用是什么？实验证据是什么？
**回答：**
TriT 酶的主要作用是作为自我抗性机制，通过催化三苦胺或明胶胺的乙酰化修饰，使其失去抗菌活性，从而保护宿主菌。
**实验证据**：
1.  **Figure 1c**: 在 *S. albus* 中缺失 *triT* 后，未检测到乙酰化产物，且产物产量下降并滞留在胞内（推测被滞留物乙酰化），暗示 *triT* 的存在影响产物的转运和最终形式。
2.  **Figure 2 & 6**: 体外酶学实验证明，纯化的 TriT 蛋白在 AcCoA 存在下，能将三苦胺 B 和明胶胺 A 转化为单乙酰化或双乙酰化形式（LC-MS 显示质量增加 42 Da 或 84 Da）。
3.  **Figure 2d & 6c**: 生物活性测定显示，经 TriT 乙酰化后的反应混合物对 *Mycobacterium phlei* 和 *M. smegmatis* 完全失去抑制活性。

#### 问题三：作者如何证明类三苦胺套索肽是趋同进化的产物？
**回答：**
作者通过系统发育分析提供了证据。
1.  Figure 3 显示，来自典型 BGC（深紫色内圈）和非典型 BGC（浅紫色内圈）的大环化酶在系统发育树上分别聚集成独立的分支，且这两个分支在进化上距离很远，处于不同的进化位置。
2.  这两类大环化酶各自与已知的其他类型套索肽大环化酶（如 Barrett et al. 描述的分支）亲缘关系更近，而不是彼此之间。
3.  然而，这两类截然不同的大环化酶却能修饰产生几乎相同的核心肽序列（具有保守的 PGDG 基序）。这种“酶系来源不同但产物结构相似”的现象，且这两类 BGC 广泛分布于不同的细菌门类，强烈暗示了它们是独立进化产生的，即趋同进化。

> "The deep branching separating the non-canonical and canonical containing groups suggests independent origins of triculamin-like macrocyclases and convergent or parallel evolution the triculamin-like lasso peptides."