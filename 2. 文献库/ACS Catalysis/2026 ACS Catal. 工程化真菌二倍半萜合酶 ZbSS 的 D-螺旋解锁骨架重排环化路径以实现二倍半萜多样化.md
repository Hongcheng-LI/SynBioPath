![image.png](https://synbiopath.online/20260210223129655.png)


---

# 一：基本信息

**文章题目**：Engineering the D-Helix in Fungal Sesterterpene Synthase ZbSS Unlocks a Skeletal Rearrangement Cyclization Route toward Sesterterpene Diversification
**文章 DOI 号**：10.1021/acscatal.5c07482
**期刊名称**：*ACS Catalysis*
**通讯作者**：刘雪婷 (Xueting Liu)
**通讯作者工作单位**：华东理工大学生物反应器工程国家重点实验室 (State Key Laboratory of Bioreactor Engineering, East China University of Science and Technology)

---

# 二：核心速览

本文聚焦于真菌二倍半萜合酶（Fungal Sesterterpene Synthases, **BF-STPSs**）中鲜为人知的骨架重排机制。研究团队通过生物信息学比对与 AlphaFold2 结构预测，发现 A 型 **BF-STPSs** 活性中心 D-螺旋（D-helix）上的一个关键残基（Phe/Ile）是控制骨架重排的“分子开关”。研究者以天然不发生骨架重排的 **ZbSS** 为模板，通过单点突变（I92F）引入芳香残基，成功解锁了复杂的骨架重排路径，生成了包括五环 *dia*-quiannulatenes 在内的一系列新颖二倍半萜产物。结合 DFT 计算与 MD 模拟，文章揭示了 Phe92 通过阳离子-$\pi$ 相互作用（Cation-$\pi$ interaction）稳定碳正离子中间体，从而改变环化轨迹的分子机制。这项工作为理性设计萜类合酶以扩展萜类化合物的结构多样性提供了精准的策略。

---

# 三：研究思路

1.  **概括核心任务**：通过挖掘决定真菌二倍半萜合酶骨架重排功能的关键结构元件，利用蛋白质工程手段对天然仅产生简单骨架的酶进行重编程，使其获得催化复杂骨架重排的能力，并解析其分子机制。
2.  **序列与结构挖掘**：对比具有重排功能的 **EvQS** 和无重排功能的 **ZbSS**，结合 AlphaFold2 建模，锁定活性中心 D-螺旋上的差异残基（Phe92 vs Ile92）。
3.  **功能验证与产物鉴定**：在酵母底盘中进行定点突变实验。验证 **EvQS** 中 F92 的必要性，并在 **ZbSS** 中引入 I92F 突变，通过 GC-MS 和 NMR/X-ray 鉴定新产生的重排产物。
4.  **机理推导与计算验证**：利用 DFT 计算推导从线性前体到多环重排产物的反应能垒路径；利用 MD 模拟揭示突变残基如何通过改变活性口袋环境（如距离、非共价相互作用）来导向特定的反应流。

---

# 四：研究方法

*   **生物信息学与结构预测**：AlphaFold2 蛋白结构预测、多序列比对（MSA）、功能区域（Plastic regions）分析。
*   **基因工程与发酵**：酿酒酵母（*Saccharomyces cerevisiae*）异源表达系统、定点突变（Site-directed mutagenesis）、大孔树脂吸附提取。
*   **化学分析与结构鉴定**：气相色谱-质谱联用（GC-MS）、高分辨质谱（HR-EI-MS）、核磁共振（NMR）、X-射线单晶衍射（X-ray diffraction）、电子圆二色谱（ECD）计算。
*   **计算化学**：密度泛函理论（DFT）计算反应路径与能垒、分子动力学（MD）模拟、IRC（内禀反应坐标）分析。

---

# 五：实验设计及结果分析

### （一）结构元件挖掘与功能位点锁定
#### 实验目的与设计逻辑
真菌二倍半萜合酶（**BF-STPSs**）分为 A 型和 B 型，其中 B 型通常涉及复杂的骨架重排，而 A 型多形成简单的 5/15 或 5/6 双环骨架（**Scheme 1A**）。然而，少数 A 型酶（如 **EvQS**）也能催化重排反应生成 quiannulatene。作者旨在通过对比这两类酶的结构特征，寻找控制重排的关键位点。逻辑上，如果某些 A 型酶能重排而其他的不能，那么活性中心的差异残基即为关键线索。因此，作者结合已有晶体结构和 AlphaFold2 模型，对活性腔周边的 $\alpha$1-loop、D-helix、G-helix 和 J-helix 进行系统分析。
![image.png](https://synbiopath.online/20260210223210412.png)

#### 实验结果与深度解析
通过对 **Scheme 1B** 的分析，作者指出 **EvQS** 能产生重排产物 quiannulatene，而与其同源性较高（40.4%）的 **ZbSS** 仅产生未重排的 sesterevisene。
![image.png](https://synbiopath.online/20260210223232124.png)

生物信息学分析（**Figure 1A**）显示，B 型酶在 D-helix、$\alpha$1-loop 和 J-helix 区域富含芳香族残基，形成疏水轮廓。在 **Figure 1B** 的结构叠合中，作者发现一个显著差异：在能催化重排的 **EvQS** 中，D-helix 的 92 位是苯丙氨酸（Phe92），而在无重排功能的 **ZbSS** 中，该位置是异亮氨酸（Ile92）。这一位置在 **NfSS** 和 **PbSS** 等酶中也显示出功能相关性。基于此，作者提出假设：D-helix 上的保守芳香残基是引导 A 型 **BF-STPSs** 进行骨架重排的关键“开关”。这为后续将 **ZbSS** 改造为重排型合酶提供了明确的靶点。
![image.png](https://synbiopath.online/20260210223256635.png)

> "We hypothesize that the conserved phenylalanine at position 92... is critical for directing skeletal rearrangements."

### （二）功能重编程与新颖骨架的发现
#### 实验目的与设计逻辑
为了验证 Phe92/Ile92 的功能决定性作用，作者设计了互补的突变实验：一方面破坏 **EvQS** 的 Phe92（突变为 A/V/L/I），观察是否丧失重排能力；另一方面在 **ZbSS** 中引入芳香残基（I92F/Y/W），观察是否能“解锁”重排活性。这是验证“结构-功能”关系最直接的证据，并通过大规模发酵和波谱学手段鉴定新产物结构。

#### 实验结果与深度解析
GC-MS 分析结果（**Figure 2A**）极具说服力。**EvQS** 的 F92A 突变导致活性完全丧失，F92I 突变导致产物量剧减且主要生成非重排副产物，证明 Phe92 对 **EvQS** 的催化至关重要。反之，在 **ZbSS** 中引入 I92F 突变产生了戏剧性的结果：野生型 **ZbSS** 仅产生化合物 **3**（sesterevisene），而 **ZbSS-I92F** 突变体几乎完全由 **3** 转向生成七种新化合物 **4-10**。通过 **Figure 2B** 的结构鉴定，化合物 **4** 和 **5** 被确定为一对 C3 差向异构体，具有罕见的五环 *dia*-quiannulatene 骨架；化合物 **7** 具有 retigeranin 型五环骨架；**8** 和 **9** 为双环化合物。特别是化合物 **4** 的绝对构型通过 X-射线单晶衍射（**Table S15**）得到确证。这一结果表明，仅通过 D-helix 上的单个位点突变，就成功将一个非重排型合酶重编程为能够合成复杂五环重排产物的多能酶，实现了产物多样性的爆发式增长。
![image.png](https://synbiopath.online/20260210223326850.png)

> "The I92F mutation in ZbSS effectively reprogrammed its outcome, unlocking a rearrangement to produce the pentacyclic *dia*-quiannulatenes."

### （三）反应机理推导与 DFT 计算验证
#### 实验目的与设计逻辑
为了解释从线性底物 GFPP 到复杂的 *dia*-quiannulatene 骨架（化合物 **4-6**）的形成过程，特别是 **ZbSS-I92F** 如何通过碳正离子重排实现这一转化，作者构建了详细的环化路径假设，并利用 DFT 计算评估各步反应的能垒，以验证路径的热力学和动力学可行性。

#### 实验结果与深度解析
作者提出了从中间体 **IM7** 出发的几条分支路径（**Figure 3A**）。其中，**Path IV**（**Figure 3C**）被认为是形成 *dia*-quiannulatene 的主要路径。DFT 计算显示，双键 $\Delta^{10,11}$ 的 $\pi$ 电子进攻 C3 碳正离子，将 **IM7a** 转化为五环中间体 **IM8a**，随后经过连续的烷基迁移（C10→C12, C3→C4）形成 **IM10a**，最终经 1,2-氢迁移和去质子化生成化合物 **4**。值得注意的是，**Figure 3B** 展示了另一条路径 Path III，涉及复杂的协同-非同步重排过程。DFT 数据（如活化能仅 2.3 kcal/mol 的氢迁移步骤）支持了 **Figure 3C** 路径的快速进行。不同于之前报道的 quiannulatene（化合物 **1**）的形成机制，*dia*-quiannulatene 的形成涉及 A 环立体化学的差异，这归因于中间体 **IM7** 中 C2 位构型的不同。这些机理推导不仅解释了新骨架的来源，也为后续理解酶如何控制立体选择性奠定了基础。
![image.png](https://synbiopath.online/20260210223347508.png)

> "The low activation barriers associated with both transition states confirm the energetic feasibility of these complex rearrangement processes."

### （四）分子动力学模拟揭示“阳离子-$\pi$”控制机制
#### 实验目的与设计逻辑
虽然突变实验证实了 I92F 的功能，但其微观物理机制尚不清楚。为什么引入苯丙氨酸会引发重排？作者通过 100 ns 的 MD 模拟，对比了 **ZbSS-WT** 和 **ZbSS-I92F** 与底物或中间体复合物的动态行为，重点考察活性腔体积变化、关键原子距离以及残基与中间体的相互作用。

#### 实验结果与深度解析
MD 模拟结果精细地揭示了两种酶变体的不同催化策略。首先，体积分析表明突变体（I92F/Y/W）的活性腔体积显著小于野生型（**Figure 4i-iv** 标注体积数值），这符合大侧链引入造成的空间压缩效应。关键的差异在于对反应流向的控制：在 **ZbSS-WT** 中（**Figure 4i**），Ile92 的主链羰基氧原子与中间体 **IM7** 的 H4 原子保持极近距离（4.6 Å），这暗示 Ile92 可能作为广义碱（General Base）直接夺取 H4 质子，从而终止反应生成非重排产物 **3**。相反，在 **ZbSS-I92F** 中（**Figure 4ii**），由于侧链位阻，主链羰基远离了 H4，阻断了去质子化路径。更为重要的是，Phe92 的芳香侧链与 **IM7** 的 C3 碳正离子形成了稳定的阳离子-$\pi$ 相互作用（Cation-$\pi$ interaction），这种稳定作用延长了中间体的寿命，使得 C3 有机会对 C10/C11 双键发起亲电进攻，从而驱动了后续的骨架重排反应。这一发现（**Figure 4**）完美解释了为何芳香残基是解锁重排路径的必要条件。
![image.png](https://synbiopath.online/20260210223405045.png)

> "Phe92 engages in cation−$\pi$ interactions with carbocation intermediates, thereby directing cyclization fidelity and rearrangement trajectories."

---

# 六：总体结论

本研究以真菌 A 型二倍半萜合酶 **ZbSS** 为模型，首次确定了 D-螺旋上的单一残基（第 92 位）是调控骨架重排的关键开关。通过将该位点的异亮氨酸突变为苯丙氨酸（I92F），成功将原本只催化简单环化的酶重编程为能够合成复杂五环 *dia*-quiannulatene 骨架的重排型合酶。机制研究表明，野生型酶利用主链羰基辅助去质子化终止反应，而工程化酶利用芳香侧链的阳离子-$\pi$ 相互作用稳定碳正离子，从而诱导进一步的骨架重排。

---

# 七：论文评价

### 优点与创新
1.  **理性设计的典范**：不同于传统的随机进化，本研究基于结构比对和 AlphaFold2 预测，精准锁定了 D-helix 上的单个关键残基，实现了酶功能的巨大转变，体现了极高的理性设计水平。
2.  **新颖骨架的发现**：通过酶工程手段获得了一系列自然界中罕见的 *dia*-quiannulatene 类五环二倍半萜，极大地扩展了萜类化合物的化学空间。
3.  **机理阐释深入**：结合 DFT 计算与 MD 模拟，提出了令人信服的“羰基去质子化”与“阳离子-$\pi$ 稳定”两种截然不同的控制机制，深化了对萜类合酶催化可塑性的理解。

### 未来研究方向
1.  **酶晶体结构解析**：尽管 MD 模拟提供了合理解释，但若能获得 ZbSS 及其突变体与底物类似物的共晶结构，将更直观地证实阳离子-$\pi$ 相互作用的存在。
2.  **催化普适性验证**：该 D-helix “开关”策略是否适用于其他类型的真菌或植物萜类合酶，值得进一步探索以建立通用的工程化法则。

---

# 八：关键问题及回答

**Q1: 为什么 Phe92 对于骨架重排是必须的？MD 模拟提供了什么证据？**
**A1:** Phe92 通过其富含 $\pi$ 电子的苯环侧链与反应中间体（特别是 C3 位的碳正离子）形成**阳离子-$\pi$ 相互作用**。在 MD 模拟中（**Figure 4ii**），观察到突变体 I92F 中苯环与碳正离子的距离维持在能形成有效相互作用的范围内。这种相互作用稳定了高能的碳正离子中间体，防止其过早发生去质子化（淬灭），从而允许其进行跨越能垒的后续亲电进攻和骨架重排反应。相比之下，野生型的 Ile92 缺乏这种稳定能力，且其主链羰基倾向于直接夺取质子终止反应。

**Q2: 文章中提到的 *dia*-quiannulatene 与已知的 quiannulatene 有何区别？**
**A2:** 两者均属于五环二倍半萜骨架，主要的区别在于立体化学构型。**Figure 3** 和相关的 DFT 分析指出，*dia*-quiannulatene（如化合物 **4-6**）与 quiannulatene（化合物 **1**）在 A 环的立体构型以及 C2 位构型上存在差异（Diastereomeric difference）。这种差异源于环化过程中中间体 **IM7** 与 **IM7a** 的构象不同，导致后续的环化和重排路径发生了细微但决定性的偏转，最终形成了非对映异构的骨架结构。


---

# 九：近期工作

刘雪婷课题组长期致力于微生物天然药物的发现与创造，利用合成生物学策略合成“非天然”的活性天然产物及其关键酶催化机制研究。课题组采用基因组挖掘策略高效发现新颖抗感染活性天然产物（Angew.  Chem. 2013；Org. Lett. 2013；Org. Lett. 2016；Cell Chem. Biol. 2020；J.  Agric. Food Chem. 2024, 2025；ACS Chem. Biol.  2025等）；并进一步通过计算化学与蛋白质工程的融合创新，激活天然产物关键酶的新颖催化功能，创造了一系列“非天然”的新颖化合物（Nat.  Prod. Rep. 2018；Org. Lett. 2021；JACS Au 2022，ACS Catal. 2023，Angew.  Chem. 2024，ACS Catal. 2025等）。

课题组主页：https://biotech.ecust.edu.cn/2018/0329/c7935a74416/page.htm

[2025 ACS Catal. | G2螺旋功能可塑区揭示真菌双功能萜合酶催化二倍半萜环化的立体构型选择性调控机制](https://mp.weixin.qq.com/s/iV7WdDi4gfGERbW5ZzSdTQ)

[2024 Angew | 分子动力学模拟辅助改造 PfNS 芳香族残基簇以实现真菌二倍半萜合酶的功能转换](https://mp.weixin.qq.com/s/JdW_lOfAsTYU-AxW6kNJLQ)
