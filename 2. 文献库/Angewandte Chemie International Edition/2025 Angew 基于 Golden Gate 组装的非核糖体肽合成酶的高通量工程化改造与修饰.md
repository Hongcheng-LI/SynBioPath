![image.png](http://synbiopath.online/20260113110850174.png)

---

# 一：基本信息

**文章题目**：High-Throughput Engineering and Modification of Non-Ribosomal Peptide Synthetases Based on Golden Gate Assembly

**文章 DOI 号**：10.1002/anie.202508967

**期刊名称**：Angewandte Chemie International Edition

**通讯作者**：Helge B. Bode

**通讯作者工作单位**：
马克斯·普朗克陆地微生物研究所（Department of Natural Products in Organismic Interactions, Max Planck Institute for Terrestrial Microbiology）

法兰克福歌德大学（Molecular Biotechnology, Department of Biosciences, Goethe University Frankfurt）

马尔堡菲利普斯大学（Center for Synthetic Microbiology (SYNMIKRO) & Department of Chemistry, Phillips University Marburg）

---

## 二：核心速览

### 研究背景
非核糖体肽通常由非核糖体肽合成酶 (NRPS) 合成，因其结构复杂和多样的生物活性而在临床药物（如抗生素、抗癌药物）开发中具有重要地位。然而，天然产物在应用于临床前往往需要对其选择性、稳定性或生物利用度进行优化。相比于化学合成，利用合成生物学手段在体内对 NRPS 进行理性工程化改造以改变其产物骨架是一种更具可持续性的替代方案。

### 前期研究
过去 30 年来，NRPS 工程化改造经历了从单氨基酸替换、腺苷化 (A) 结构域替换到完整模块交换的发展过程。近期提出的 eXchange Unit (XU) 和 eXchange Unit Condensation (XUC) 概念，以及最新的 eXchange Unit Thiolation (XUT) 概念，分别在 A-C 连接子或 T 结构域内部（XUTIII 和 XUTIV）定义了融合位点，极大地提高了 NRPS 模块组装的通用性。然而，传统的克隆方法（如 Gibson 组装）虽然精确，但缺乏高通量潜力，且片段往往不可复用。

### 本文突破点
本研究建立了一种基于 Golden Gate Assembly (GGA) 的新型克隆方法，并将其与 XUT 概念相结合。通过利用 XUTIV 位点中高度保守的甘氨酸残基设计通用的粘性末端，实现了 scarless（无疤痕）组装。该方法成功构建了包含超过 100 种新型 NRPS 的模块化库，并实现了对 xenoamicin 生物合成基因簇的高通量衍生化修饰。

### 研究难点
NRPS 基因通常巨大（约 3 kb/模块），克隆和异源表达具有挑战性。此外，为了保证 GGA 的顺利进行，必须在不改变氨基酸序列的前提下通过沉默突变去除所有内源性 BsaI 酶切位点，这增加了序列设计的复杂性。同时，确保工程化杂合 NRPS 能够正确折叠并高效生产目标肽也是关键挑战。

---

## 三：研究思路

1.  **GGA 系统设计与序列优化**
   

分析 NRPS T 结构域中的 XUTIV 位点（"FFxxGGxS" 基序），选择其中两个高度保守的甘氨酸作为融合点。针对这些位点设计特异性粘性末端（A/B, A/C, C/B 等），并对所有供体和受体载体进行序列优化，移除内源性 BsaI 位点，构建适用于 GGA 的 Acceptor（含起始和终止模块）和 Donor（含延伸模块）质粒库。

2.  **方法验证与单模块交换**

利用 GGA 方法将单个延伸模块插入受体质粒，通过 HPLC/MS 检测产物，并与传统的 Gibson 组装方法进行对比，验证新方法的可行性和产物的正确性。同时测试随机文库中供体模块的分布情况。

3.  **高通量双模块文库构建与验证**

设计不同的粘性末端组合（A/C 和 C/B），实现连续插入两个延伸模块。构建包含 81 种 NRPS 变体的文库，分析其产物多样性，并开发 qPCR 方法对文库中各供体片段的插入频率进行高通量验证。

4.  **起始模块工程的扩展**

将 GGA 方法扩展至起始模块的替换。设计新的粘性末端（S/A），构建缺失起始模块的受体，并引入不同的起始供体，验证该方法对肽链 N 端修饰（如脂肪酸引入或游离氨基酸）的可行性。

5.  **天然产物衍生化应用**

将该策略应用于天然产物 xenoamicin 的生物合成基因簇 (xabABCD)。针对负责环状结构合成的模块进行替换，构建 36 种工程化 NRPS 变体，分析其对 xenoamicin 衍生物生成的影响。

---

## 四：研究方法

*   **Golden Gate Assembly (GGA)**: 利用 IIS 型限制性内切酶 BsaI 在识别位点外侧切割，产生可设计的 4 个核苷酸粘性末端。通过设计 XUTIV 位点中的通用粘性末端，实现受体载体与供体片段的一锅法组装。
*   **基因克隆与载体构建**: 使用高拷贝质粒 pSEVA681 和低拷贝表达质粒 pACYC 分别构建供体和受体。通过沉默突变去除基因内部的 BsaI 位点以避免干扰。
*   **高效液相色谱-质谱联用 (HPLC/MS)**: 用于工程化菌株发酵产物的定性和定量分析，确认目标肽的生成、分子量及衍生物的存在。
*   **化学合成**: 合成部分关键肽化合物（如 13, 36, 50, 71）作为标准品，通过对比保留时间和 MS 数据确认生物合成产物的结构。
*   **实时荧光定量 PCR (qPCR)**: 开发了一种半自动化方法，用于快速筛选和验证文库质粒中插入的供体模块类型及其位置分布，替代繁琐的全长测序。

---

## 五：实验设计及结果分析

### 研究部分一：NRPS Golden Gate Assembly 的设计与流程建立

#### 实验目的与设计
本部分旨在建立一套基于 GGA 的 NRPS 工程化通用标准。核心在于利用 XUTIV 位点（位于 T 结构域 Loop 1 和 Helix 2 的 N 端，基序为 "FFxxGGxS"）中的两个保守甘氨酸来设计粘性末端，实现无缝组装。
![image.png](http://synbiopath.online/20260113111122017.png)

#### 实验结果与分析
研究者选择了 XUTIV 位点，因为该位点在细菌 T 结构域中最为丰富。利用保守的甘氨酸密码子设计了 16 种 scarless 粘性末端（如 A, B, C 等）。Acceptor 质粒（如 NRPS-A1, NRPS-A2）包含起始模块（来自 XldS，引入 C14 脂肪酸）和终止模块（分别来自 SzeS 和 GxpS），中间插入 BsaI 位点产生 A 和 B 粘性末端。Donor 质粒（如 D1-D6）则包含延伸模块及其两端的 BsaI 位点。

为了验证该设计的可行性，研究者构建了 5 个 NRPS 系统的 GGA 组装版本，并与 Gibson 组装版本进行平行比较。通过在 *E. coli* DH10B::mtaA 中异源表达并进行 HPLC/MS 分析，结果显示两种组装方式得到的产物谱几乎完全一致。
> "After analysis by HPLC/MS, almost identical production profiles were obtained for both approaches, establishing the viability of GGA for NRPS engineering and the creation of libraries."

此外，通过使用等量的供体片段进行随机组装，测序结果显示文库中各变体的分布较为均匀，证明了该方法适用于随机文库的构建。

---

### 研究部分二：延伸模块文库的构建与产物分析

#### 实验目的与设计
本部分旨在评估 GGA 方法在构建 NRPS 延伸模块文库时的效率，以及不同模块组合对产物多样性和产量的影响。

#### 实验结果与分析
首先，研究者使用包含 6 个供体（D1-D6）的文库与受体（NRPS-A1, NRPS-A2）进行组装。结果分析（对应 **Figure 2**）显示，NRPS-A2 系列（含 C/E 域的终止模块）成功产生了预期肽的比例高于 NRPS-A1 系列。例如，NRPS-A2_D6 成功产生了预期的脂肽 **C14-QaL**。然而，部分组合如 NRPS-A2_D4 仅产生了因模块跳跃而产生的截短肽 **C14-qL**。
![image.png](http://synbiopath.online/20260113111247342.png)


为了增加肽链长度和复杂度，研究者设计了新的粘性末端组合（A/C 和 C/B），旨在插入两个延伸模块。通过使用供体 D7-D12 和 D16-D21，构建了 36 个不同的 NRPS 系统（**Figure 3a** 黑色框区域）。HPLC/MS 分析表明，83% 的构建体表现出功能性，其中 61% 生成了预期的全序列肽。然而，某些模块（如 D18，引入酪氨酸；D10，引入缬氨酸）往往导致 NRPS 功能丧失或产生大量截短产物。针对这一情况，研究者引入了新的缬氨酸和酪氨酸模块（D13-D15, D22-D24），最终构建了包含 81 个变体的完整文库。
![image.png](http://synbiopath.online/20260113111318111.png)

**Figure 3a** 的热图展示了 81 个构建体的生产情况，其中深蓝色代表检测到预期产物，浅蓝色代表检测到衍生物（通常为模块跳跃产物），灰色代表无产物。数据表明，通过优化供体模块，显著提高了预期肽的检出率。**Figure 4** 展示了部分成功合成的目标肽（如 13, 17, 36 等）的化学结构，涵盖了不同的氨基酸组合（包括 D-氨基酸和 D-allo-氨基酸）。
![image.png](http://synbiopath.online/20260113111402852.png)


为了验证高通量文库的多样性，研究者采用了 qPCR 方法（**Figure 3b**）对 287 个随机克隆进行了分析。结果显示，除了 D16（14%）和 D15（3.5%）外，大多数供体的分布集中在 8%-9%，表明该 GGA 方法能够生成具有良好多样性的随机文库。
![image.png](http://synbiopath.online/20260113111338855.png)


---

### 研究部分三：起始模块文库的构建

#### 实验目的与设计
本部分旨在扩展 GGA 方法的应用范围，将其应用于 NRPS 起始模块的替换，以实现对产物 N 端的多样化修饰。

#### 实验结果与分析
研究者构建了一个新的受体 NRPS-A3，该受体移除了原有的起始模块，并在起始位点引入了基于起始密码子（ATG）的特异性粘性末端 S ("CATG")。供体质粒则设计为带有 S/A 粘性末端的起始模块。

实验中使用了 4 个起始供体（D25-D28）：D25 为 C14-Q（阳性对照），D26 来自 XabABC（C4-P），D27 来自 AmbS（丝氨酸），D28 来自未表征的 NRPS。HPLC/MS 分析结果（对应 **Figure 5**）显示，NRPS-A3_D25 成功复现了阳性对照产物。而 NRPS-A3_D26 和 NRPS-A3_D27/D28 分别产生了含有 C4 脂肪酰基的肽 **48** 以及不含酰基修饰的肽 **50** 和 **51**。这表明，某些起始模块中的 C Starter 域可能在工程化背景下失活或缺失功能，但 GGA 方法本身能够成功整合不同来源的起始模块并赋予产物不同的 N 端特征。
![image.png](http://synbiopath.online/20260113111427867.png)


> "Both NRPS-A3_D27 and NRPS-A3_D28 produced peptides (50, 51) without any acyl group at the N-terminus, suggesting the Cstarter domain of LC536431 is also non-functional in regards to the incorporation of an acyl moiety."

---

### 研究部分四：Xenoamicin 生物合成基因簇的衍生化改造

#### 实验目的与设计
本部分旨在将 GGA 方法应用于真实且复杂的天然 NRPS 系统——xenoamicin 的生物合成基因簇 *xabABCD*，以验证其在产生新型天然产物衍生物方面的潜力。

#### 实验结果与分析
Xenoamicin 是一种 13 个氨基酸长的脂肽-脱氢肽，具有环状 C 端。研究者选取负责合成环状部分的 XabC 模块作为改造对象。构建受体 NRPS-A4，其中移除了 β-丙氨酸和脯氨酸模块，并加入了 *xabD*（编码天冬氨酸脱羧酶）以保证 β-丙氨酸的供应。
![image.png](http://synbiopath.online/20260113111545426.png)

在第一阶段，研究者通过引入单个供体（D1-D6, D29, D30）替换缺失的模块。HPLC/MS 分析（对应 **Figure 6b**）显示，所有 8 个改造后的 NRPS 均具有功能，成功生成了预期的肽 **55** 至 **65**。由于替换了一个供体，所得脱氢肽的环状结构大小相比天然产物有所减小。


随后，研究者尝试引入两个供体模块（A/C 和 C/B 粘性末端组合），试图恢复或改变原有的氨基酸序列。在构建的 36 个变体中（对应 **Figure 6c**），只有 8 个变体生成了预期的全长肽，16 个变体出现了模块跳跃现象，13 个变体未能产生产物。尽管如此，在总共检测到的 23 种肽中，有 17 种是新型的 xenoamicin 衍生物。例如，化学合成的标准品 **71**（NRPS-A4_D9_D21 的产物）证实了工程化 NRPS 成功产生了含有新氨基酸序列的衍生物。

---

### 研究部分五：总结与展望

#### 实验目的与设计
综合上述实验数据，评估 GGA-XUT 方法的整体性能、优势及其在 NRPS 工程领域的意义。

#### 实验结果与分析
研究结果表明，相较于 Gibson 组装，GGA 方法在构建 NRPS 杂合基因时具有显著的速度和效率优势，特别适合高通量筛选。虽然需要在设计阶段去除内源性 BsaI 位点，但这通过序列优化可以解决。此外，供体模块的可复用性大大降低了工作量。

值得注意的是，该方法目前主要局限于 NRPS，因为 PKS 中的 T 结构域缺乏同样高度保守的 FFxxGGxS 基序。研究中观察到大量的“模块跳跃”现象，这表明模块间的兼容性仍受未知结构域相互作用的影响。未来积累的大数据集有望通过机器学习手段揭示支配模块兼容性的规律。

---

## 六：总体结论

本研究成功建立并验证了一种基于 Golden Gate Assembly 和 XUT 概念的高通量 NRPS 工程化方法。该方法通过利用 XUTIV 位点保守基序设计通用粘性末端，实现了 scarless 的模块化组装。研究者构建了包含 100 余种新型 NRPS 的文库，涵盖了延伸模块、起始模块以及终止模块的替换。通过对 xenoamicin 生物合成基因簇的改造，成功生成了 25 种新型衍生物（其中 17 种为预期结构）。该策略不仅展示了 NRPS 模块组装的高通量潜力，也为快速获取具有生物活性的新型肽类化合物提供了强有力的工具。

---

## 七：论文评价

### 优点与创新
1.  **高通量与标准化**：将 GGA 技术引入 NRPS 工程化，克服了传统 Gibson 组装在通量上的瓶颈，建立了标准化的粘性末端库，极大地提高了构建效率。
2.  **无缝组装**：巧妙利用 XUTIV 位点保守的甘氨酸残基设计粘性末端，实现了基因水平的 scarless 连接，避免了引入可能影响蛋白功能的氨基酸残基。
3.  **系统性强**：研究覆盖了起始、延伸和终止模块的全方位改造，从模型系统到复杂的天然产物系统均有涉及，证明了方法的普适性。
4.  **数据分析创新**：开发了 qPCR 筛选方法用于快速验证文库多样性，为高通量筛选提供了高效的解决方案。

### 未来研究方向
1.  **机制解析与预测**：针对研究中观察到的模块跳跃现象，需要进一步深入解析分子水平的兼容性规则，并结合机器学习建立预测模型，以提高工程化 NRPS 的成功率。
2.  **应用范围拓展**：尝试在聚酮合酶 (PKS) 中寻找类似的保守位点，以扩展 GGA 方法的适用范围。
3.  **挖掘生物活性**：对生成的大量新型肽类化合物进行系统的生物活性筛选，寻找具有药用潜力的先导化合物。

---

## 八：关键问题及回答

#### 问题一：为什么选择 XUTIV 位点而不是 XUTIII 位点进行 GGA 设计？

**回答：** 虽然 XUTIII 和 XUTIV 都位于 T 结构域的保守区域，但 XUTIV 位点对应的基序 "FFxxGGxS" 中包含两个高度保守的甘氨酸。这两个甘氨酸提供了足够多的密码子组合，能够设计出 16 种 scarless 粘性末端。相比之下，XUTIII 位点中的苯丙氨酸虽然保守，但仅由两个密码子编码，可供设计的粘性末端数量有限，限制了组合多样性。此外，此前的研究表明 XUTIV 位点在工程化 NRPS 中表现出优异的整体功能性。

> "Although the high phenylalanines of XUTIII are only encoded by two different codons each, we used both conserved glycines from XUTIV, which is by far the most abundant sequence in all bacterial T domains at this position... They provide enough codons to create 16 scarless overhangs..."

#### 问题二：Golden Gate Assembly 相比于 Gibson Assembly 在 NRPS 工程化中的具体优势是什么？

**回答：** Gibson 组装依赖于片段间特异性的重叠序列，每次构建新质粒往往需要重新设计和合成引物或片段，缺乏通用的接口，难以适应高通量需求。而 GGA 使用 IIS 型限制性内切酶产生预定义的粘性末端，一旦建立了标准化的 Acceptor 和 Donor 库，就可以像搭积木一样通过简单的酶切连接反应快速组装成百上千种不同的组合，供体质粒可重复使用，极大地提高了通量和灵活性。

> "In contrast, a restriction enzyme approach, such as the GGA, obviates the need for such unique overhangs... The flexible application of the GGA-based NRPS engineering comes with greater sustainability in terms of workload and consumables..."

#### 问题三：在研究中，Xenoamicin 衍生化改造的成功率如何？

**回答：** 在对 xenoamicin 生物合成基因簇的改造中，当引入单个模块替换时，所有 8 个构建体均为功能性并产生了预期肽。然而，在尝试引入两个模块以恢复或改变原有长度时，在 36 个变体中，仅 8 个变体生成了预期的肽，16 个出现了模块跳跃，13 个无产物。尽管成功率有所下降，但总体上生成了 23 种可检测的肽，其中 17 种是新型衍生物，证明了该方法对天然产物骨架进行有效修饰的潜力。

> "From the 36 generated xenoamicin synthetase variants, eight showed the production of the expected peptides, while 16 showed skipping of one or both of the newly incorporated modules, respectively, and 13 did not show any production... Of the total 23 peptides produced, 17 represent new derivatives of xenoamicin..."