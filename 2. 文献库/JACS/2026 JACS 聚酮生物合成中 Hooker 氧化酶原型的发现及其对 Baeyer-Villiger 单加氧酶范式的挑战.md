![9f84751f-d08f-4df3-a2fd-34282e87aba9.png](http://synbiopath.online/9f84751f-d08f-4df3-a2fd-34282e87aba9.png)

---

## 一：基本信息
**文章题目**：A Hooker Oxygenase Archetype in Polyketide Biosynthesis Challenging the Baeyer–Villiger Monooxygenase Paradigm
**文章 DOI 号**：10.1021/jacs.5c21759
**期刊名称**：Journal of the American Chemical Society (JACS)
**通讯作者**：Robin Teufel
**通讯作者工作单位**：巴塞尔大学药物科学系，药物生物学 (Pharmaceutical Biology, Department of Pharmaceutical Sciences, University of Basel, Switzerland)

---

## 二：核心速览

### 研究背景
放线菌产生的芳香聚酮类化合物是一类结构复杂且具有重要药用价值的天然产物。其生物合成过程涉及聚酮链的组装、环化、芳构化以及随后的酶促修饰。其中，黄素蛋白单加氧酶 (FPMOs) 在骨架重排和氧化修饰中起着关键作用。Rishirilide A 是一种具有独特桥环结构的聚酮化合物，其生物合成中的关键步骤是由 FPMO RslO9 催化的氧化重排。此前，该酶被普遍认为是一种 Baeyer-Villiger 单加氧酶 (BVMO)，通过内酯化和随后的醛醇缩合形成桥环骨架。
![image.png](http://synbiopath.online/20260127180608952.png)

### 本文突破点
本研究通过深入的机理研究、结构生物学解析和底物谱拓展，推翻了 RslO9 作为 BVMO 的传统认知。研究发现，RslO9 催化的反应并非 Baeyer-Villiger 氧化，而是一种类似于经典的 Hooker 氧化的新型酶促反应机制。该机制涉及底物的羟基化，随后发生二苯乙醇酸重排 (benzilic acid rearrangement) 导致的烷基迁移。

### 核心科学发现
1.  **立体化学修正**：确证了 Rishirilide B 的绝对构型为 2S,3S,4S，这与之前提出的 BVMO 机制所要求的立体化学不符。
2.  **新反应机制**：发现 RslO9 能催化非天然底物 Lapachol 生成 Hooker 中间体，证实了其催化烷基迁移的能力。
3.  **结构基础**：解析了 RslO9 的晶体结构，揭示了其活性位点特征，并排除了典型 BVMO 催化所需的关键残基。
4.  **机理推广**：提出类似的烷基迁移机制可能也适用于其他非典型 BVMO（如 MtmOIV），为理解这类酶的催化功能提供了新范式。

---

## 三：研究思路

**步骤 1：立体化学再评估**
首先对 Rishirilide B 的立体化学进行重新确证。通过分离纯化天然产物，利用 NOESY-NMR 和 IR/VCD 光谱分析，确认其构型为 2S,3S,4S。这一结果与 BVMO 机制预测的产物构型（需为 2S,3R,4S 才能进行后续反应）相矛盾，从而引发了对原有机制的质疑。

**步骤 2：酶结构解析与分子对接**
解析 RslO9 的晶体结构（包括无配体和底物浸泡状态），并进行分子对接和分子动力学模拟。结构分析显示 RslO9 缺乏典型 BVMO 所需的用于稳定 Criegee 中间体的精氨酸或用于去质子化的催化碱。对接结果表明底物结合位置更有利于 C4 位的羟基化而非 C4a 位的亲核进攻。

**步骤 3：底物谱拓展与中间体捕获**
测试了一系列萘醌和蒽醌类底物类似物。发现 RslO9 能高效转化 Lapachol (8) 生成 Hooker 中间体 (16)。通过 18O 同位素标记实验和邻苯二胺 (OPD) 捕获实验，证实了反应涉及单加氧酶活性和随后的二苯乙醇酸重排（涉及水的参与），而非 BVMO 机制。

**步骤 4：机理重构**
基于上述发现，提出了 RslO9 催化天然底物 5 的新机理：首先在 C4 位发生亲电羟基化（形成偕二醇或环氧化物），随后发生烷基迁移（二苯乙醇酸重排类反应），最终形成内酯环。

**步骤 5：关键残基验证**
通过定点突变（如 H251N/A）考察活性位点残基的作用，发现 H251 并非绝对必需的催化残基，但在低 pH 下可能辅助质子转移或稳定中间体。

---

## 四：研究方法

*   **光谱学分析**: NOESY-NMR, IR, VCD (振动圆二色谱) 用于立体化学鉴定。
*   **结构生物学**: X 射线晶体学 (数据收集于 Diamond Light Source 和 Swiss Light Source)，结构解析与精修。
*   **计算化学**: 分子对接 (Smina), 分子动力学 (OpenMM), 量子化学计算 (Gaussian 16)。
*   **生化实验**: 蛋白表达纯化, 热稳定性分析 (nanoDSF), 酶活测定 (LC-MS), 同位素标记 ($^{18}O_2$, $H_2^{18}O$), 中间体化学捕获。

---

## 五：实验设计及结果分析

### 研究部分一：Rishirilide B 立体化学的再确证
#### 实验目的与设计逻辑
为了验证 RslO9 是否通过 BVMO 机制催化反应，首先需要明确产物 Rishirilide B (2) 的绝对构型。因为根据之前的假设，BVMO 氧化后形成的七元内酯环需要特定的立体构型才能发生后续的 Aldol 缩合形成桥环。作者从发酵液中分离了化合物 2，并利用 NOESY-NMR 确定相对构型，利用 VCD 光谱确定绝对构型。

#### 实验结果与深度解析
NOESY 谱图显示 C4-异戊基与 A 环 C2-质子之间存在相关信号，证实了 C2-甲基与 C4-异戊基处于反式关系 (Trans)。VCD 光谱的实验数据与计算模拟数据（基于 2S,3S,4S 构型）高度吻合，从而确证了 Rishirilide B 的构型为 **2S,3S,4S**。这一结果至关重要，因为如果是 BVMO 机制，中间体需要形成 2S,3R,4S 构型才能在空间上允许后续的碳负离子进攻侧链形成桥环。现有的 2S,3S,4S 构型在立体空间上阻碍了这种 Aldol 缩合（Figure S1B）。因此，这一发现直接挑战了原有的生物合成假设，提示 RslO9 必然采用了不同的催化策略。

> "The proposed RslO9-catalyzed aldol condensation step... is sterically hindered by the seven-membered lactone ring... Therefore, the stereochemical configuration of the rishirilides was first revisited."

### 研究部分二：RslO9 的晶体结构与活性位点分析
#### 实验目的与设计逻辑
为了探究 RslO9 的真实催化机制，作者解析了其晶体结构。由于全长蛋白难以结晶，使用了切除 N 端柔性区域的截短体 RslO9PAP 进行结晶，并成功解析了无配体和底物 5 浸泡后的结构。

#### 实验结果与深度解析
RslO9 呈现典型的 A 类 FPMO 折叠结构，包含 FAD 结合域、底物结合域和硫氧还蛋白样结构域。底物 5 的对接模型显示，其 C4 位距离 FAD 的 C4a 位点约 5.0 Å，且取向适合氧原子转移 (Figure 2B)。与典型的 BVMO 不同，RslO9 的活性位点缺乏用于稳定 Criegee 中间体的保守精氨酸残基，也缺乏用于活化过氧黄素的催化碱。此外，底物 5 的 C4a 位点是 β-酮-烯醇结构的一部分，电子云密度较高，不利于亲核性的过氧黄素阴离子进攻（这是 BVMO 的典型机制）。相反，这种富电子结构更适合亲电性的过氧黄素 (FlC4aOOH) 进行羟基化或环氧化。这些结构特征强烈暗示 RslO9 并非 BVMO，而更可能是一个羟化酶或环氧化酶。

> "Overall, these stereochemical, structural, and biochemical considerations support an initial hydroxylation rather than a lactone-forming Baeyer–Villiger oxidation."

### 研究部分三：非天然底物 Lapachol 的转化与 Hooker 中间体的发现
#### 实验目的与设计逻辑
为了寻找机理证据，作者测试了 RslO9 对一系列底物类似物的催化活性。其中，Lapachol (8) 是一种含异戊烯基侧链的萘醌，结构上与天然底物 5 相似。

#### 实验结果与深度解析
RslO9 能高效转化 Lapachol (8) 生成单一产物 16。通过详细的 NMR 和 MS 解析，产物 16 被鉴定为 **Hooker 中间体**。Hooker 氧化是一个经典的化学反应，涉及萘醌侧链的氧化断裂和烷基迁移。产物 16 的形成意味着反应过程中发生了 **二苯乙醇酸重排 (benzilic acid rearrangement)** 导致的烷基迁移，而不是 BVMO 类型的插入氧化。为了进一步证实这一点，作者在反应体系中加入邻苯二胺 (OPD)，成功捕获了开环的二酮中间体 18（以吩嗪衍生物 19 的形式检测到）。这直接证明了反应经过了氧化开环步骤。同位素标记实验显示，产物 16 中的一个氧原子来自 $^{18}O_2$，证实了单加氧酶活性；而在 $H_2^{18}O$ 中反应未见标记，但在 OPD 捕获实验中，中间体 19 保留了来自 $O_2$ 的标记，这与 Hooker 氧化机制（羟基化/环氧化 -> 水合/重排）完全一致。

> "To our surprise, 16 was identified as the characteristic 'Hooker intermediate'... Importantly, the formation of intermediate 18 thus underscores that the RslO9 reaction does not involve Baeyer–Villiger oxidation."

### 研究部分四：RslO9 催化天然底物的“类 Hooker”机理推导
#### 实验目的与设计逻辑
基于 Lapachol 的反应结果，作者重新推导了 RslO9 催化天然底物 5 生成中间体 6 的机理。

#### 实验结果与深度解析
提出的新机理 (Figure 4A, Figure 5) 包括：(1) 亲电性的 FlC4aOOH 进攻底物 5 的 C4 位（富电子的烯醇双键），形成环氧化物或偕二醇中间体；(2) 随后发生类似于二苯乙醇酸重排的烷基迁移，侧链从 C4a 迁移到 C4；(3) 环氧化物开环形成 β-内酯；(4) β-内酯开环并重排形成最终的 γ-内酯产物 6。这一机理不仅解释了产物 6 的形成，而且完美契合了 Rishirilide B (2) 的 2S,3S,4S 立体化学构型。此外，该机理也解释了为何 RslO9 需要底物具有特定的电子特性（β-酮-烯醇结构）才能进行反应。

> "For native substrate 5, a similar alkyl migration is proposed, fully consistent with the stereochemistry of the rishirilides—an enzyme functionality that overturns the previously proposed BVMO chemistry."

---

## 六：总体结论

本研究通过对 RslO9 酶的深入剖析，彻底修正了 Rishirilide 生物合成中的关键氧化重排步骤。RslO9 并非此前认为的 Baeyer-Villiger 单加氧酶，而是一种催化“类 Hooker 氧化”反应的酶，通过亲电羟基化/环氧化引发烷基迁移（二苯乙醇酸重排），从而构建复杂的桥环骨架。这一发现不仅揭示了自然界中一种罕见的酶促反应类型，也为理解其他非典型 BVMO（如 MtmOIV）的催化机制提供了新的视角和理论框架。

---

## 七：论文评价

### 优点与创新
1.  **范式转移**：挑战并推翻了长期以来关于 RslO9 及相关酶类（Group A FPMOs）作为 BVMO 的定论，提出了全新的烷基迁移机制。
2.  **证据链完整**：从产物立体化学的修正，到酶晶体结构的解析，再到非天然底物的机理探针实验（Hooker 中间体的捕获），逻辑严密，证据确凿。
3.  **化学与生物学的结合**：巧妙利用经典的有机化学反应（Hooker 氧化）来解释复杂的酶促反应机理，体现了对酶学机制的深刻理解。

### 未来研究方向
1.  **其他同源酶的重评估**：基于本研究，需要重新审视其他被归类为“非典型 BVMO”的酶（如 MtmOIV, PxaB），验证它们是否也采用类似的烷基迁移机制。
2.  **酶工程改造**：利用 RslO9 的新机理，通过定向进化或理性设计，开发能够催化特定烷基迁移或骨架重排的生物催化剂，用于复杂天然产物的合成。

---

## 八：关键问题及回答

#### 问题一：为什么 RslO9 被称为“Hooker Oxygenase Archetype”？
**回答：** Hooker 氧化是一个经典的有机化学反应，描述了萘醌类化合物在氧化条件下发生侧链降解和烷基迁移的过程。本研究发现 RslO9 催化非天然底物 Lapachol 时，生成了 Hooker 氧化的特征性中间体（Hooker intermediate），且其催化天然底物的机制也涉及类似的氧化引发的烷基迁移（二苯乙醇酸重排）。因此，RslO9 代表了自然界中执行这种复杂化学转化的一类新型酶的原型。

#### 问题二：本研究如何排除了 Baeyer-Villiger 氧化机制？
**回答：** 主要基于三点证据：(1) **立体化学冲突**：BVMO 机制预测的产物构型与实验确证的 Rishirilide B 构型 (2S,3S,4S) 不符，后者在空间上无法通过 BVMO 路径生成。(2) **结构特征**：RslO9 的活性位点缺乏稳定 BVMO 关键中间体（Criegee 中间体）所需的残基，且底物的结合模式更利于亲电进攻而非亲核进攻。(3) **中间体捕获**：在 Lapachol 的转化中，捕获到了开环的二酮中间体（通过 OPD 衍生化），这直接证明了反应涉及二苯乙醇酸重排类型的烷基迁移，而非 BVMO 的酯插入机制。