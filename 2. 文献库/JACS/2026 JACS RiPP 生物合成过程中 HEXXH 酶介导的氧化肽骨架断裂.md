![image.png](http://synbiopath.online/20260122165135475.png)

---

## 一：基本信息
**文章题目**：Oxidative Peptide Backbone Cleavage by a HEXXH Enzyme during RiPP Biosynthesis
**文章 DOI 号**：10.1021/jacs.5c19246
**期刊名称**：Journal of the American Chemical Society (JACS)
**通讯作者**：Wilfred A. van der Donk
**通讯作者工作单位**：
1. 伊利诺伊大学厄巴纳-香槟分校化学系 (Department of Chemistry, University of Illinois at Urbana-Champaign, Urbana, Illinois, USA)
2. 霍华德·休斯医学研究所 (Howard Hughes Medical Institute, USA)

---

## 二：核心速览

### 研究背景
核糖体合成和翻译后修饰肽 (RiPPs) 是一类结构多样的天然产物，其生物合成依赖于修饰酶对前体肽的加工。近年来，多核非血红素铁氧化酶 (MNIOs) 等新型酶类的发现极大地扩展了 RiPP 的化学空间。HEXXH 蛋白家族通常被认为是锌依赖性金属蛋白酶，但近期研究发现部分成员实际上是 α-酮戊二酸 (αKG) 依赖的单核非血红素铁酶，催化羟基化反应。

### 本文突破点
本研究首次发现并表征了两个 αKG 依赖性 HEXXH 酶（PflC 和 PosC），它们不仅能对前体肽中的连续谷氨酰胺 (Gln) 残基进行 β-羟基化，还能特异性识别 C 端 ARMD 四肽基序，触发氧化性肽骨架断裂，生成 C 端酰胺化产物。这是一种全新的 RiPP 修饰策略。此外，该基因簇还编码一种独特的 MNIO-硝基还原酶融合蛋白 (PflD)，催化了 RiPP 中首例 Z-脱氢苯丙氨酸的形成。

### 核心发现
1.  **新酶活**：PflC/PosC 兼具 Gln 羟基化和氧化性骨架断裂（酰胺化）双重活性。
2.  **识别机制**：骨架断裂严格依赖于 C 端 ARMD 基序中的 Ala 残基。
3.  **前体肽调控**：PflC 在无前导肽时表现为水解酶（蛋白酶），而在全长前体肽存在时表现为氧化酶，揭示了前导肽对酶催化选择性的变构调控作用。
4.  **新修饰**：PflD 催化了罕见的 Phe 脱氢反应。

---

## 三：研究思路

**步骤 1：生物信息学挖掘与基因簇锁定**
利用序列相似性网络 (SSN) 分析 HEXXH 酶家族，发现了一个包含 MNIO-硝基还原酶融合蛋白的新聚类。通过基因组挖掘，锁定了 *Pseudomonas* 菌株中的 *pfl* 和 *pos* 基因簇，并预测了前体肽序列。

**步骤 2：异源表达与功能初筛**
在大肠杆菌中重构生物合成途径，共表达前体肽与修饰酶。利用高分辨质谱 (HRMS) 检测修饰后的质量变化，初步推断酶的功能（如 PflC 导致的质量减少暗示了骨架断裂）。

**步骤 3：结构确证与化学分析**
通过 LysC 酶解、NMR 波谱解析（TOCSY, NOESY, HSQC）和二级质谱 (MS/MS)，精确确定了 Gln 的 β-羟基化位置、C 端 ARMD 的移除及酰胺化结构，以及 PflD 催化的 Asp 羟基化和 Phe 脱氢结构。

**步骤 4：机理探究与突变验证**
通过定点突变（如 ARMD 基序的丙氨酸扫描）确定骨架断裂的关键位点。利用同位素标记 ($H_2^{18}O$) 和厌氧实验，区分 PflC 的氧化活性与水解活性，并提出基于 α-碳氢原子攫取 (HAT) 的氧化断裂机理。

**步骤 5：结构模拟与分子对接**
利用 AlphaFold 3 预测酶-底物复合物结构，分析活性中心与底物关键残基（如 ARMD 中的 Ala）的空间距离，为机理推导提供结构支持。

---

## 四：研究方法

*   **生物信息学分析**: EFI-EST 构建 SSN，ClusterBlast 进行基因簇比对，AlphaFold 3 进行蛋白结构预测。
*   **生化实验**: 异源表达、蛋白纯化、体外酶活重建。
*   **波谱学分析**: HR-LC-MS, HR-ESI-MS/MS, 1D/2D NMR (1H, 13C, TOCSY, NOESY, HSQC, HMBC)。
*   **化学合成**: 固相肽合成 (SPPS) 制备截短底物。

---

## 五：实验设计及结果分析

### 研究部分一：生物信息学挖掘与基因簇鉴定
#### 实验目的与设计逻辑
为了寻找具有新颖功能的 HEXXH 酶，研究人员利用酶功能倡议酶相似性工具 (EFI-EST) 构建了 αKG 依赖性 HEXXH 型 β-羟基化酶家族的序列相似性网络 (SSN)。通过分析网络聚类，旨在发现与已知酶（如 ChlBH, BpmH）不同的新亚家族，特别是那些与特殊修饰酶（如 MNIO）共编码的基因簇。

#### 实验结果与深度解析
SSN 分析揭示了一个独特的 HEXXH 酶聚类（Figure 1B，紫色圆圈），该聚类中的酶由包含 MNIO-硝基还原酶融合蛋白基因的生物合成基因簇 (BGC) 编码。基于此，研究者选择了 *Pseudomonas fluorescens* CH267 的 *pfl* 基因簇和 *Pseudomonas* sp. Os17 的 *pos* 基因簇作为研究对象（Figure 2A, S7）。基因组挖掘显示，这两个 BGC 编码了前体肽 (PflA/PosA)、乙酰转移酶 (PflB)、HEXXH 蛋白 (PflC/PosC)、MNIO-硝基还原酶融合蛋白 (PflD) 以及转运蛋白。对前体肽序列的多序列比对 (Figure 2B) 发现了一个高度保守的 C 端基序：一段连续的 Gln 残基后紧跟 ARMD 四肽序列。生物信息学预测 PflA 的 N 端可能属于腈水合酶样前导肽 (NHLP) 家族，但缺乏典型的双甘氨酸 (double-Gly) 切割位点，暗示其成熟过程可能涉及非典型的蛋白酶解或修饰机制。这一生物信息学分析为后续发现 PflC/PosC 的特殊骨架断裂活性提供了关键线索。
![image.png](http://synbiopath.online/20260122171745912.png)
![image.png](http://synbiopath.online/20260122171809198.png)


> "A multisequence alignment of PflA with precursor peptides encoded in related BGCs shows a highly conserved C-terminal consecutive Gln motif followed by an ARMD sequence."

### 研究部分二：PflC/PosC 的双重催化活性与产物结构确证
#### 实验目的与设计逻辑
旨在通过湿实验验证 PflC 和 PosC 的功能。将前体肽与酶在大肠杆菌中共表达，利用 HRMS 分析分子量变化。随后，通过 LysC 酶解和 NMR 波谱技术，解析修饰后的化学结构，以解释观察到的异常质量损失。

#### 实验结果与深度解析
质谱分析显示，PflC 使 PflA 质量减少 394 Da，PosC 使 PosA 质量减少 410 Da (Figure 2C)。这种大幅度的质量减少无法仅用羟基化 (+16 Da) 解释。通过纯化 PosC 修饰后的 PosA 酶解片段并进行 NMR 解析 (Figure 3)，研究人员观察到 C 端 ARMD 四肽的信号消失，且末端 Gln 残基的信号特征符合 C 端酰胺化结构。同时，肽段内部的四个 Gln 残基在 NMR 谱图中显示出 β-位次甲基信号 (CH)，证实发生了 β-羟基化。综合 NMR 和 MS/MS 数据 (Figure 3B)，确证了 PosC 催化了两个反应：(1) 四个 Gln 的 β-羟基化；(2) 氧化移除 C 端 ARMD 四肽并生成 C 端酰胺。质量计算完美吻合：4 × (+16) （羟基化）- 490 （ARMD 丢失） + 16 （酰胺化） = -410 Da。这一结果证实了 HEXXH 酶具有前所未有的氧化骨架断裂活性。
![image.png](http://synbiopath.online/20260122171856528.png)


> "Collectively, these data demonstrate that PosC catalyzed β-hydroxylation of four Gln residues and removal of the ARMD motif to generate a terminal amide."

### 研究部分三：PflD 的功能鉴定与新修饰发现
#### 实验目的与设计逻辑
探究基因簇中独特的 MNIO-硝基还原酶融合蛋白 PflD 的功能。通过共表达实验和定点突变（如 MNIO 结构域的 H73A 突变），解析两个结构域各自催化的反应类型。

#### 实验结果与深度解析
共表达结果显示 PflD 导致 PflA 产生 +14 Da 和 -2 Da 两种修饰产物。PflD-H73A 突变体（失活 MNIO）仅产生 -2 Da 产物，表明 -2 Da (脱氢) 由硝基还原酶结构域催化，而 +16 Da (羟基化) 由 MNIO 结构域催化 (Figure S4, S6)。NMR 分析 (Figure 3C) 揭示 -2 Da 修饰对应于 Phe7 转化为 Z-构型的脱氢苯丙氨酸 (Z-dehydro-Phe)，这是首次在 RiPP 中发现此类修饰。+16 Da 修饰则被鉴定为 Asp8 的 β-羟基化。这一发现不仅证实了 PflD 的双功能性，也拓展了 RiPP 的修饰类型。

> "To the best of our knowledge, this study reports the first dehydrophenylalanine formation in RiPPs."

### 研究部分四：骨架断裂的底物识别与催化机理
#### 实验目的与设计逻辑
为了阐明氧化骨架断裂的机理，特别是酶如何识别切割位点，研究人员对 C 端 ARMD 基序进行了丙氨酸扫描和序列重排。结合 AlphaFold 3 结构模拟，推测酶与底物的结合模式和反应机制。

#### 实验结果与深度解析
突变实验表明，ARMD 中的 R, M, D 残基突变不影响骨架断裂，但 A91Q 突变完全阻断了断裂反应，仅保留了羟基化活性 (Figure 4B, C)。这证明 **Ala** 是断裂反应的关键决定簇。AlphaFold 3 模拟的酶-底物复合物结构 (Figure S32, S33) 显示，酶的活性中心铁离子恰好位于 ARMD 基序中 Ala 残基的附近，这为 Ala 特异性氧化提供了结构基础。基于此，作者提出了一个氧化断裂机理：酶活性中心的高价铁-氧物种夺取 Ala91 的 α-氢原子，生成碳自由基，随后经羟基化或电子转移生成亚胺中间体，最终水解导致肽键断裂和 C 端酰胺化。此外，将 ARMD 移位或增加拷贝数的实验 (Figure 4D-F) 表明，该基序具有位置独立性，只要位于前导肽的一定距离之外即可被识别。
![image.png](http://synbiopath.online/20260122171924723.png)


> "To rationalize the site-specific backbone cleavage and amide formation, we propose that Ala91 undergoes α-C−H abstraction by a high-valent iron−oxo species."

### 研究部分五：前导肽对酶活性的变构调控
#### 实验目的与设计逻辑
为了探究前导肽在酶催化中的作用，研究人员合成了缺乏 N 端前导肽的截短 PflA 底物，并在体外与 PflC 反应。通过同位素标记 ($H_2^{18}O$) 和厌氧条件下的反应，区分氧化与水解机制。

#### 实验结果与深度解析
在缺乏前导肽的情况下，PflC 意外地表现出了**水解酶活性**，直接水解切除了 C 端 ARMD，产生羧基末端而非酰胺末端 (Figure 5)。在 $H_2^{18}O$ 中进行的实验证实产物结合了来自水的氧原子，确证了水解机理。而在全长前体肽存在时，PflC 表现为 αKG 依赖的**氧化酶活性**。这一截然不同的结果表明，前导肽与酶的结合诱导了酶构象的改变，这种变构效应可能重新排列了活性中心，使其能够结合氧气并进行氧化反应，从而抑制了默认的水解活性。这揭示了 RiPP 生物合成中一种精妙的调控机制：利用前导肽将一个潜在的蛋白酶“重编程”为氧化酶。
![image.png](http://synbiopath.online/20260122171946571.png)


> "This observation established peptidase activity of PflC in the absence of the N-terminal sequence of PflA... indicating that leader peptide−enzyme interactions modulate the observed reaction selectivity."

---

## 六：总体结论

本研究通过基因组挖掘、生化表征和机理研究，揭示了 bacterial RiPP 生物合成中一种全新的酶学功能：αKG 依赖性 HEXXH 酶 (PflC/PosC) 能够催化位点特异性的氧化肽骨架断裂，生成 C 端酰胺。研究阐明了该反应严格依赖于 C 端 ARMD 基序中的 Ala 残基，并受前导肽的变构调控（决定氧化 vs 水解）。此外，发现的 MNIO-硝基还原酶融合蛋白 (PflD) 催化了 RiPP 中首例 Z-脱氢苯丙氨酸的形成。这些发现极大地扩展了我们对 HEXXH 酶家族功能多样性和 RiPP 修饰化学逻辑的理解。

---

## 七：论文评价

### 优点与创新
1.  **打破传统认知**：首次证明 HEXXH 酶在 RiPP 生物合成中可以作为氧化酶催化骨架断裂，而非传统的蛋白水解，刷新了对该酶家族的认知。
2.  **干湿结合紧密**：利用 SSN 和 AlphaFold 3 等生物信息学工具精准定位目标基因簇并解释底物识别机制，结合扎实的生化实验（NMR, MS, 突变），逻辑严密。
3.  **调控机制新颖**：揭示了前导肽作为“分子开关”调控酶催化类型（水解/氧化）的独特机制，为酶工程改造提供了新思路。

### 未来研究方向
1.  **晶体结构解析**：解析 PflC/PosC 与全长及截短底物的复合物晶体结构，以直观展示前导肽诱导的构象变化细节。
2.  **产物功能探索**：由于该 BGC 广泛存在于假单胞菌中，且产物结构独特，未来应深入探究成熟产物的生物活性及生态学功能。

---

## 八：关键问题及回答

#### 问题一：PflC/PosC 的氧化骨架断裂机理与传统的 α-酰胺化酶 (如 PAM) 有何异同？
**回答：** 两者都涉及底物 α-碳原子的氢原子攫取 (HAT) 和随后的 C-N 键断裂生成 C 端酰胺。不同点在于：(1) **酶学家族**：PAM 是铜依赖性单加氧酶，而 PflC/PosC 是 αKG 依赖性非血红素铁酶；(2) **底物识别**：PAM 通常识别 C 端甘氨酸，而 PflC/PosC 特异性识别内部的丙氨酸 (Ala)；(3) **反应路径**：PAM 通常形成 α-羟基甘氨酸中间体，随后由裂解酶 (PAL) 水解；而 PflC/PosC 可能通过生成亚胺中间体直接水解或氧化断裂，且该过程与上游 Gln 的羟基化紧密偶联。

#### 问题二：AlphaFold 3 的结构模拟如何辅助解释了 ARMD 基序的特异性识别？
**回答：** AlphaFold 3 预测的 PosC-PosA 复合物结构显示，PosA 的 C 端 ARMD 基序深入酶的活性口袋，其中 Ala 残基的 α-碳原子距离活性中心的铁离子非常近，处于理想的氢原子攫取位置。这种空间上的邻近性解释了为什么酶特异性地氧化断裂 Ala 位点。此外，模型还展示了前导肽与酶表面的广泛相互作用，这支持了前导肽对酶构象和活性中心组装起关键稳定作用的假设。