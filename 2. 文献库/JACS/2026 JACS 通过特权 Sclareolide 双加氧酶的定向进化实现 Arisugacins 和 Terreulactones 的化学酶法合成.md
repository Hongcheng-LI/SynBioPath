![image.png](https://synbiopath.online/20260219155332086.png)

---

## 一：基本信息

**文章题目**：Chemoenzymatic Synthesis of Arisugacins and Terreulactones via Directed Evolution of a Privileged Sclareolide Dioxygenase
**文章 DOI 号**：10.1021/jacs.5c22624
**期刊名称**：*Journal of the American Chemical Society* (JACS)
**通讯作者**：李键 (Jian Li)
**通讯作者工作单位**：上海交通大学变革性分子前沿科学中心，化学化工学院，协同生物合成化学国家重点实验室 (Frontiers Science Center for Transformative Molecules, School of Chemistry and Chemical Engineering, State Key Laboratory of Synergistic Chem-Bio Synthesis, Shanghai Jiao Tong University)

---

## 二：核心速览

本研究建立了一个高效的化学酶法合成平台，旨在解决多环萜类化合物位点和化学选择性氧化的合成难题。研究团队以廉价的手性源 Sclareolide（香紫苏内酯）为起始原料，通过对非血红素 Fe(II)/$\alpha$-酮戊二酸依赖型双加氧酶 AndA 进行多轮定向进化，成功获得了 STAC 系列突变体。这些突变体能够对 Sclareolide 的 C1、C3 和 C5 位点进行精准的 C-H 键羟基化，活性相比野生型提高了 82 倍，并实现了克级至十克级的制备。利用该酶法平台，作者开发了简洁的合成路线：通过 C5 羟基化模块实现了 (+)-phorbadione 的形式合成；通过 C1/C3/C5 的正交氧化策略，结合 Suarez 氧化断裂和胺催化的形式 [3 + 3] 环化反应，构建了关键中间体，从而完成了 Arisugacin J、D、M 以及 Terreulactone C、B 的首次全合成。该工作确立了 AndA 作为一种类似于 P450BM3 的“特权”萜类氧化酶的地位，为从简单手性原料合成高度氧化的混源萜类天然产物提供了通用策略。
![image.png](https://synbiopath.online/20260219155426195.png)

---

## 三：研究思路

1.  **问题识别与假设提出**：针对 Labdane/Drimane 家族天然产物中 C1、C3、C5 位点氧化难以通过传统化学方法引入的问题，作者提出利用生物催化剂 AndA 直接氧化 Sclareolide 的设想。基于 AndA 晶体结构的分子对接模拟显示底物 $\alpha$-面朝向金属中心，预示了定向进化的可行性。
2.  **酶的定向进化与库构建**：以 AndA 为模板，通过结构指导的饱和突变（利用 22c-trick 方法），筛选出分别针对 C1、C3、C5 位点具有高选择性和高活性的突变体（STAC 系列）。
3.  **多位点氧化级联的构建**：在 C5-氧化产物的基础上，进一步进化酶突变体以引入 C1 和 C3 位的氧化，构建出高度氧化的多官能团中间体。
4.  **化学合成路线的整合**：
    *   利用 C5-氧化产物，通过简短的化学修饰完成 (+)-phorbadione 的形式合成。
    *   利用 C1/C3/C5-氧化产物，结合 Suarez 氧化断裂开环和优化的 [3 + 3] 环化反应，构建 Arisugacin/Terreulactone 家族的核心骨架。
5.  **发散式全合成**：从公共的高级中间体出发，通过后期修饰（如水合、乙酰化、氧化、脱氢等）完成 5 个天然产物的全合成。

---

## 四：研究方法

*   **生物信息学与结构模拟（干实验）**：基于 AndA 的晶体结构进行**分子对接 (Molecular Docking)**，预测底物结合姿态，指导突变位点（如 Q66, N120, A229 等）的选择。
*   **蛋白质工程（湿实验）**：**定向进化 (Directed Evolution)**，**饱和突变 (Saturation Mutagenesis)**（使用 22c-trick 方法），全细胞转化筛选。
*   **化学合成**：Suarez 氧化断裂（利用 PIDA/I$_2$），Burgess 试剂脱水，Dess-Martin 氧化，Mukaiyama 水合反应，胺催化的形式 [3 + 3] 环化。
*   **结构鉴定**：核磁共振 (NMR)，X-射线单晶衍射 (X-ray Crystallography)。

---

## 五：实验设计及结果分析

### （一）AndA 酶的定向进化与 Sclareolide 的位点选择性氧化
#### 实验目的与设计逻辑
为了在 Sclareolide（化合物 **1**）的惰性碳骨架上引入 C1、C3 和 C5 位的羟基，作者没有选择传统的化学氧化（通常偏向 C2 位），而是选择了酶法策略。基于前期 AndA 晶体结构（PDB 4W6Z）的**分子对接（Molecular Docking）** 分析，作者发现化合物 **1** 的 $\alpha$-面朝向活性中心的 Fe(II) 离子，且其结构与 AndA 的天然底物相似。基于此结构信息，作者推测通过对底物结合口袋附近的残基进行**饱和突变**，可以重新编程酶的区域选择性。

#### 实验结果与深度解析
通过多轮定向进化，作者成功构建了针对不同位点的特异性氧化酶。如 **Figure 2** 所示，进化路线分为三条分支。首先，筛选前期突变体库发现 AndA I69Y N120C 能产生微量 C5$\alpha$ 氧化产物 **14**，而 I69Y Y138H 能氧化 C1$\alpha$。针对 C1 氧化，通过对 Q66、A229 等残基的迭代突变，最终获得了突变体 **STAC1** (AndA Q66P I69Y Y138H A229D)，其将化合物 **1** 转化为 **12** 的转化率高达 81%。针对 C3 氧化，筛选发现双突变体 I69Y N157T 具有独特的 C3 选择性，进一步引入 A229M 突变后获得 **STAC3**，转化率达到 92%（产物 **13**）。针对最具挑战性的 C5 氧化，通过对 Y138、N157、R66、I70 等位点的系统优化，获得了六突变体 **STAC5**，其生成 C5$\alpha$-羟基化产物 **14** 的转化率达到 82%。这些结果表明，通过精细调控活性口袋的极性和空间位阻（如 Q66P 改变骨架刚性，A229 调整空间），可以显著改变酶对刚性萜类骨架的识别模式。
![image.png](https://synbiopath.online/20260219155733551.png)

此外，**Figure 3** 展示了在 C5-羟基化产物 **14** 的基础上进行的第二阶段进化。为了模拟 Arisugacin 家族的氧化模式，需要在 **14** 的基础上引入 C1 和 C3 氧化。作者以 **14** 为底物进行筛选，发现 **STAC5** 的前体突变体具有一定活性，经过进一步对 Q66 和 A229 的饱和突变，获得了 **STAC5C1**（92% 转化率生成 **15**）和 **STAC5C3**（79% 转化率生成 **16**）。这一系列**干湿结合**的实验不仅验证了分子模拟的预测，还提供了一套互补的生物催化剂库，能够以克级规模制备多种氧化态的 Labdane 中间体。
![image.png](https://synbiopath.online/20260219155754937.png)

> "Directed evolution of the nonheme Fe(II)/$\alpha$-ketoglutarate oxygenase AndA furnishes STAC variants with complementary C1$\alpha$/C3$\alpha$/C5$\alpha$ selectivity and up to 82-fold activity improvements."

### （二）(+)-Phorbadione 的化学酶法形式合成
#### 实验目的与设计逻辑
为了验证进化酶在天然产物合成中的实用性，作者首先选择了结构相对简单的 (+)-Phorbadione 作为目标。传统化学合成路线需要从 Sclareolide 出发经过 11 步繁琐的氧化态调整才能得到关键中间体二烯酮醛 **17**。作者旨在利用 **STAC5** 酶一步引入 C5 羟基的能力，大幅缩短这一路线。

#### 实验结果与深度解析
如 **Figure 4** 所示，合成路线从 Sclareolide (**1**) 出发，首先利用 **STAC5** 酶进行 C5$\alpha$-羟基化得到化合物 **14**。随后，利用 Burgess 试剂进行脱水反应构建 $\Delta^{4,5}$ 双键，接着通过 KHMDS/P(OMe)$_3$/O$_2$ 体系引入 $\alpha$-羟基，最后经由 NaIO$_4$ 介导的 C-环氧化断裂（Renata 小组报道的方法），仅需 5 步即可高效得到关键中间体 **17**。相比之下，传统化学法受限于 Sclareolide C5 位的惰性，必须绕道进行多步官能团转化。这一结果直观地展示了生物催化在“氧化态编辑”上的巨大优势，能够直接在非活化碳氢键上引入官能团，从而改写逆合成分析的逻辑。
![image.png](https://synbiopath.online/20260219155823472.png)

> "This route stands in stark contrast to traditional routes to 17 from sclareolide which... require a protracted 11-step sequence to correct the inherent oxidation-state disparity."

### （三）Arisugacins 和 Terreulactones 的发散式全合成
#### 实验目的与设计逻辑
针对结构更为复杂的 Arisugacin 和 Terreulactone 家族，其核心骨架包含 C1, C3, C5 三个氧原子以及独特的五环结构。作者设计了一条高度汇聚的路线：首先利用酶法构建含氧 Labdane 核心，然后通过化学手段构建吡喃酮环。关键挑战在于如何高效构建五环骨架（即 B/C/D 环系统的融合）。作者计划通过 Suarez 氧化断裂打开 B 环，再通过形式上的 [3 + 3] 环化反应构建 D 环。

#### 实验结果与深度解析
合成从化合物 **16**（由 **1** 经两步酶法氧化得到）开始。首先保护 3,5-二醇得到硅缩醛 **19**，随后在 C2 位引入羟基得到 **20**（**Figure 5**）。由于硅缩醛对还原条件不稳定，作者巧妙地采用了 Suarez 氧化断裂（PIDA/I$_2$）策略，成功切断 C-C 键并异构化得到烯醛 **21**。在尝试构建五环骨架的关键 [3 + 3] 环化步骤中，作者遇到了挑战。如 **Figure 5** 表格所示，初始条件（EDDA 催化）产率极低，推测是硅保护基的大位阻阻碍了亚胺的形成。通过移除硅保护基得到 **22**，反应活性显著提高，但 **22** 不稳定。最终，通过使用乙二胺乙酸盐作为催化剂，并在 150 °C 下反应，成功以 42% 的产率获得了关键的五环二醇中间体 **24**。
获得 **24** 后，作者通过一系列后期修饰完成了全合成（**Figure 6**）。利用 Mukaiyama 水合反应在 **24** 的 C9-C11 双键上引入叔羟基，高立体选择性地得到了 **Arisugacin J (3)**，其结构经 **X-ray 单晶衍射**确证。随后，通过对 C3 羟基的乙酰化得到 **Arisugacin D (28)**；通过 Dess-Martin 氧化得到 **Terreulactone C (29)**；进而通过 $\alpha,\beta$-脱氢得到 **Terreulactone B (4)**；或通过 NaBH$_4$ 还原得到 **Arisugacin M (30)**。这一系列转化充分证明了中间体 **24** 的多能性以及化学酶法策略在构建复杂混源萜方面的强大能力。

> "To the best of our knowledge, these sequences constitute the first syntheses of arisugacin J, arisugacin D, arisugacin M, terreulactone C, and terreulactone B."

---

## 六：总体结论

本研究成功开发了一种结合定向进化与化学合成的综合策略，解决了 Sclareolide 骨架上 C1、C3、C5 位点难以选择性氧化的难题。通过对 AndA 酶的改造，获得了 5 种具有不同区域选择性的高效生物催化剂。以此为基础，仅通过 5-11 步反应便完成了 1 种天然产物的形式合成和 5 种复杂天然产物的首次全合成。该工作展示了生物催化在简化逆合成分析、缩短合成路线以及构建复杂氧化态萜类化合物方面的巨大潜力。

---

## 七：论文评价

### 优点与创新
1.  **酶工程与全合成的完美融合**：不仅通过定向进化获得了高性能酶，还将其深度整合到复杂天然产物的全合成路线中，解决了纯化学法难以克服的 C-H 键活化难题。
2.  **克服了底物偏好性**：相比于前期工作需要预先将 Sclareolide 转化为 9,11-脱氢衍生物，本工作直接对廉价、惰性的 Sclareolide 进行改造，避免了繁琐的氧化还原调整步骤（Redox toggle），提高了原子经济性和步骤经济性。
3.  **多位点正交氧化**：实现了在同一骨架上对 C1、C3、C5 三个位点的可编程氧化，为构建多样化的萜类库提供了通用平台。
4.  **关键化学步骤的优化**：在 [3 + 3] 环化反应中，通过“先脱保护后环化”的策略克服了位阻效应，体现了深厚的有机合成功底。

### 未来研究方向
1.  **酶的底物谱拓展**：进一步探索 STAC 系列突变体对其他 Labdane 或 Drimane 型萜类的催化能力。
2.  **工业化应用**：通过高密度发酵和辅因子循环系统的优化，进一步降低酶法步骤的成本，推动其中间体的规模化制备。
3.  **机理研究**：深入研究突变残基（如 A229, Q66）如何具体影响底物在活性口袋中的构象，结合 MD 模拟为未来的理性设计提供理论支撑。

---

## 八：关键问题及回答

**Q1: 为什么作者选择 Sclareolide 直接作为底物，而不是沿用之前的 9,11-dehydrosclareolide？**
**A1:** 虽然 9,11-dehydrosclareolide 更容易发生烯丙位氧化，但使用它需要在合成后期进行烯烃加氢还原，这属于非构建性的“氧化还原调整（Redox toggle）”，增加了步骤但不增加骨架复杂度。直接使用 Sclareolide（化合物 **1**）作为底物，虽然 C-H 键活化难度更大，但可以避免引入额外的氧化还原步骤，使合成路线更加简洁高效，且 Sclareolide 原料更廉价易得。

**Q2: 在 [3 + 3] 环化构建五环骨架时，作者遇到了什么问题？是如何解决的？**
**A2:** 作者最初尝试直接利用硅缩醛保护的烯醛 **21** 进行环化，但产率极低。作者推测是大位阻的二异丙基硅基团阻碍了亚胺中间体的形成和随后的环化。解决方案是先脱除硅保护基得到裸露的二醇烯醛 **22**。虽然 **22** 较不稳定，但在优化的条件（乙二胺乙酸盐催化，150 °C）下，其反应活性更高，最终以 42% 的产率成功获得了关键中间体 **24**，打通了合成路线。