![image.png](http://synbiopath.online/20251228174604156.png)


---

## 一：基本信息

**文章题目**：Enzymatic Anti-Baldwin Ring-Closure Cascade for Fused Bicyclic Ether Formation

**文章 DOI 号**：10.1021/jacs.5c17188

**期刊名称**：*Journal of the American Chemical Society* (JACS)

**通讯作者**：Kenji Watanabe；K. N. Houk

**通讯作者工作单位**：
*   Kenji Watanabe: 静冈县立大学药学部 (Department of Pharmaceutical Sciences, University of Shizuoka)
*   K. N. Houk: 加利福尼亚大学洛杉矶分校化学与生物分子工程系 (Department of Chemical and Biomolecular Engineering, University of California, Los Angeles)

---

## 二：核心速览

### 研究背景
稠环聚醚类化合物（如海洋毒素短裸甲藻毒素 Brevetoxins）具有强效生物活性，其复杂的梯状或稠合环系结构一直是合成化学和生物合成领域的研究热点。著名的“Nakanishi 级联假说”提出，这类结构是通过多聚环氧化物中间体经连续的“反 Baldwin 规则”（anti-Baldwin）环氧开环环化形成的。然而，这种稠合醚环骨架形成的具体酶学机制尚未被实验完全证实。

### 前期研究
此前，Tang 和 Houk 课题组曾基于计算研究提出了 aurovertins 中稠合双环醚形成的机制，涉及碱催化的亲核加成。近期在 lasalocid 生物合成中也证实了细菌 Lsd19 酶能催化反 Baldwin 环氧开环。尽管如此，真菌来源的复杂稠合多醚类化合物（如 pyrenulic acids）的酶学形成机制仍未被阐明。
![image.png](http://synbiopath.online/20251228173928966.png)

### 本文突破点
1.  **基因簇鉴定**：首次鉴定了真菌 *Pyrenula* sp. 中负责 pyrenulic acid 生物合成的基因簇（*pya* cluster）。
2.  **新颖酶功能发现**：发现并表征了 $\alpha/\beta$ 水解酶 PyaF，它能催化连续的 **6-endo-tet** 和 **7-endo-tet** 环化反应，构建 6,7-稠合双环醚骨架。
3.  **非典型催化机制**：通过计算模拟和突变实验，揭示 PyaF 采用一种罕见的 **“催化四分体” (catalytic tetrad: Ser170-His169-Asn342-Asp314)** 进行通用碱催化，而非传统的 Ser-His-Asp 三联体。
4.  **区域选择性控制**：阐明了酶如何通过活性位点残基（如 His284）的静电相互作用，强制反应按热力学上非优势的 anti-Baldwin 路径进行。

### 研究难点
*   **遗传操作困难**：地衣共生真菌 *Pyrenula* sp. 难以进行基因敲除等遗传操作，迫使研究团队采用异源表达策略。
*   **缺乏晶体结构**：PyaF 尚无晶体结构，研究团队利用 AI 预测工具 Chai-1 结合分子动力学（MD）模拟构建了高精度的酶-底物模型。
*   **反应路径复杂**：需要区分自发的环化路径与酶促路径，并解释酶如何克服固有能垒实现特定的区域选择性。

---

## 三：研究思路

**步骤 1：目标基因簇的生物信息学挖掘与锁定**

对生产菌 *Pyrenula* sp. 进行全基因组测序，利用 antiSMASH 分析及 RT-PCR 转录分析，锁定与 pyrenulic acid 结构特征（聚酮骨架、氧化修饰）相符的高表达基因簇 *pya*。

**步骤 2：异源表达体系构建与 P450 功能解析**

由于原宿主遗传操作困难，将 *pya* 基因簇导入模式生物构巢曲霉 (*Aspergillus nidulans*) 进行异源表达。通过逐步引入氧化酶基因（*pyaJ*, *pyaG*），利用 NMR 和 MS 鉴定中间体，确立了 P450 酶在环氧化和羟基化修饰中的功能。

**步骤 3：核心环化酶 PyaF 的发现与体外验证**

基于前体转化实验，推测 α/β 水解酶 PyaF 负责关键的成环步骤。在大肠杆菌中表达纯化 PyaF，通过体外酶活实验（*in vitro* assay）直接证实其催化双环氧化物底物生成稠合双环产物的能力。

**步骤 4：基于 AI 建模与 MD 模拟的结构-功能分析**

利用 AI 工具 Chai-1 预测 PyaF 结构，并通过 200 ns 分子动力学模拟优化模型。识别出关键活性位点残基，特别是预测了非典型的催化中心结构。

**步骤 5：定点突变与酶学性质表征**

基于结构模型设计突变体（如 S170A, N342A/H 等），通过动力学参数（$k_{cat}$, $K_m$）测定，验证了“催化四分体”假说及关键残基在酸碱催化中的作用。

**步骤 6：量子化学计算揭示反应机理与选择性**

利用密度泛函理论（DFT）计算反应能垒，对比有无酶存在下的反应路径。结合 MM/GBSA 结合能分析，阐明酶如何通过特定残基（如 His284）稳定过渡态，从而翻转反应的区域选择性，实现 anti-Baldwin 环化。

---

## 四：研究方法

**基因组测序与生物信息学分析**: 全基因组测序，antiSMASH 用于基因簇预测，Chai-1 用于蛋白质三维结构预测。

**异源表达 (Heterologous Expression)**: 使用构巢曲霉 (*Aspergillus nidulans*) 作为宿主表达真菌基因簇。

**波谱学分析**: 1D/2D NMR 和 HR-MS 用于代谢产物结构鉴定。

**体外酶活测定 (In vitro Assay)**: 重组蛋白表达（*E. coli*），底物转化实验及 HPLC 监测。

**定点突变 (Site-directed Mutagenesis)**: 构建突变质粒，分析关键氨基酸功能。

**计算化学**:
*   **分子动力学 (MD)**: AMBER 软件，ff19SB/OPC 力场，模拟酶-底物复合物动态。
*   **量子力学 (QM/DFT)**: Gaussian 16，$\omega$B97X-D 泛函，计算反应路径和过渡态能量。
*   **结合自由能计算**: MM/GBSA 方法分析底物与酶的结合亲和力。

---

## 五：实验设计及结果分析

### 研究部分一：Pyrenulic Acid 生物合成基因簇的鉴定与 P450 功能解析
#### 实验目的与设计
识别负责 pyrenulic acid 合成的基因簇，并解析修饰骨架的前期氧化步骤。

#### 实验结果与分析

**基因簇锁定**：在 *Pyrenula* sp. 基因组中筛选出 13 个候选 PKS 基因簇，RT-PCR 显示 *pks6* 在产物生成条件下高表达（Figure S1）。该基因簇（命名为 *pya*）包含 PKS、还原酶、P450s 和 α/β 水解酶（Table 1）。
![image.png](http://synbiopath.online/20251228174152309.png)

**P450 功能验证**：
![image.png](http://synbiopath.online/20251228174237924.png)

*   在 *A. nidulans* 中表达 PyaJ，饲喂化合物 **2**（epoxidized pyrenulic acid A），生成了新化合物 **3**。NMR 数据（Figure S19-S23）证实 PyaJ 在侧链 C6-C7 双键处引入了环氧基团。
*   在 *A. nidulans* 中共表达 PyaJ 和 PyaG，生成了化合物 **4**。NMR 数据证实 PyaG 在 C22 位引入了羟基（Figure 3, Figure S24-S28）。
*   **结论**：PyaJ 和 PyaG 分别负责环氧化和末端羟基化，为后续环化反应准备了关键的双环氧-羟基前体 **4**。

### 研究部分二：稠合双环醚合酶 PyaF 的发现与活性验证
#### 实验目的与设计
确定负责将双环氧前体 **4** 转化为稠合双环产物 **5** 的酶。

#### 实验结果与分析
*   **体内验证**：在表达 *pyaJ* 和 *pyaG* 的 *A. nidulans* 菌株中引入 *pyaF*，检测到产物 **5**（pyrenulic acid D）的生成（Figure 3vi）。产物结构经 NMR 确证（Figure S17, S18）。
![image.png](http://synbiopath.online/20251228174300914.png)

*   **体外验证**：在大肠杆菌中表达纯化 GST 标签的 PyaF 蛋白（68.0 kDa）。体外酶活实验显示，PyaF 能高效将底物 **4** 转化为产物 **5**（Figure 4a, 4bii），直接证实 PyaF 是负责连续 6-endo/7-endo 环化的环氧水解酶。
![image.png](http://synbiopath.online/20251228174323271.png)

> "In vitro assay of the recombinant PyaF with 4 led to the formation of 5, confirming its activity."

### 研究部分三：PyaF 催化机制与活性位点解析
#### 实验目的与设计
揭示 PyaF 的催化残基及其独特的“催化四分体”机制。

#### 实验结果与分析
**序列比对**：PyaF 与 hydroxynitrile lyases 具有同源性。通常的 Ser-His-Asp 三联体在 PyaF 中对应位置为 Ser170, Asn342, Asp314。Asn342 的出现是非典型的（Figure 4a）。
![image.png](http://synbiopath.online/20251228174352773.png)

**突变分析**：
*   **S170A, D314A**：活性完全丧失（Figure 4biii, iv），证实其核心催化作用。
*   **N342A**：活性保留，但 $k_{cat}/K_m$ 降低约 21%（Figure 4c）。
*   **N342H**：活性增强（$k_{cat}$ 提升 2.2 倍），表明组氨酸在此位置能提供更佳的质子传递效率，但原生的 Asn 也能维持功能。
**催化四分体模型**：MD 模拟（Figure 5a）显示 His169 位于 Ser170 和 Asn342 之间，形成 **Ser170-His169-Asn342-Asp314** 的氢键网络。His169 实际上充当了传统三联体中 His 的角色，辅助 Ser170 夺取底物羟基的质子，启动亲核攻击。
![image.png](http://synbiopath.online/20251228174412129.png)

> "The study revealed the involvement of a catalytic tetrad... In this tetrad, the triad His residue is replaced with an Asn residue and assisted by an additional His residue [His169]."

### 研究部分四：反应区域选择性的计算化学研究
#### 实验目的与设计
解释为何酶促反应能生成热力学上不占优的 anti-Baldwin 产物（6,7-稠环），而非自发反应可能生成的其他产物。

#### 实验结果与分析
**无酶条件计算**：DFT 计算显示，无酶催化时，第二步环氧开环更倾向于 **6-exo-tet** 路径（生成 im5），而非观察到的 **7-endo-tet** 路径（Figure 6）。
![image.png](http://synbiopath.online/20251228174440617.png)

**酶促机制计算**：
![image.png](http://synbiopath.online/20251228174502750.png)

*   **结合能分析**：MM/GBSA 计算（Figure 7）表明，酶与 **6-endo** 过渡态 (tsa) 的结合能显著优于 5-exo，与 **7-endo** 过渡态 (tsc) 的结合能优于 6-exo。
*   **关键残基作用**：能量分解分析显示，残基 **His284** 与 **Tyr255** 在稳定特定过渡态中起关键作用。特别是 His284 通过静电相互作用稳定了 6-endo 路径，并在此后的 7-endo 步骤中可能作为广义酸稳定氧负离子中间体。
*   **His284 突变**：H284A 突变体活性大幅下降（Figure 4bxi），实验结果支持了计算预测。
**结论**：PyaF 通过活性口袋的预组织（preorganization）和特定残基的静电稳定作用，强行扭转了反应路径，使其遵循 anti-Baldwin 规则生成 6,7-稠合环系。

---

## 六：总体结论

本研究完整解析了真菌聚酮化合物 Pyrenulic acid 中复杂的 6,7-稠合双环醚骨架的生物合成机制。核心发现是 $\alpha/\beta$ 水解酶 PyaF 利用一种罕见的 **Ser-His-Asn-Asp 催化四分体** 激活底物，并通过精细的活性位点环境（特别是 His284 和 Tyr255）控制连续的环氧开环反应，实现了在动力学和热力学上均具挑战性的双重 anti-Baldwin 环化。这项工作为理解酶如何控制复杂成环反应的区域选择性提供了深刻的分子机制视角。

---

## 七：论文评价

### 优点与创新
*   **机制新颖性**：首次发现了 $\alpha/\beta$ 水解酶家族中独特的“催化四分体”结构，拓展了对该酶家族催化机制多样性的认知。
*   **方法整合度高**：完美结合了经典的天然产物生物合成方法（基因挖掘、异源表达、同位素标记）与前沿的计算化学手段（AI 结构预测、高精度 QM/MM 计算），为无晶体结构酶的机制研究树立了典范。
*   **解决长期科学问题**：为 Nakanishi 提出的聚醚形成假说提供了确凿的真菌酶学证据，特别是针对稠合环系的形成。

### 未来研究方向
*   **结构生物学验证**：尽管 AI 预测模型与突变数据吻合，但获取 PyaF 的 X 射线晶体结构或冷冻电镜结构仍是最终确证“四分体”构象的必要步骤。
*   **酶工程改造**：基于本研究揭示的 His284 等关键残基对选择性的控制，未来可尝试通过改造 PyaF 来合成具有不同环系大小（如 6,6-或 7,7-稠环）的非天然聚醚衍生物。

---

## 八：关键问题及回答

#### 问题一：为什么 PyaF 被认为使用“催化四分体”而不是传统的“催化三联体”？
**回答：** 传统的 $\alpha/\beta$ 水解酶催化三联体通常由 Ser-His-Asp 组成。在 PyaF 中，序列比对显示传统 His 的位置被 Asn342 占据。计算模拟和突变实验揭示，临近的 His169 插入到了 Ser170 和 Asn342 之间，形成了 Ser170-His169-Asn342-Asp314 的氢键中继网络。His169 实际上承担了接受质子的角色，而 Asn342 辅助定位。这种四残基协同作用的模式与经典三联体显著不同，因此被称为“催化四分体”。

#### 问题二：PyaF 是如何控制“Anti-Baldwin”环化选择性的？
**回答：** 根据 DFT 计算，在没有酶的情况下，第二步环氧开环倾向于遵循 Baldwin 规则进行 6-exo-tet 环化。然而，PyaF 通过活性口袋的构象限制和特定残基的相互作用改变了这一路径。特别是残基 **His284** 和 **Tyr255**，它们作为广义酸稳定了环氧打开后产生的氧负离子。能量分解分析显示，酶与 7-endo-tet 过渡态的结合能显著优于 6-exo-tet 过渡态，从而在动力学上强制反应通过 anti-Baldwin 路径进行，生成 6,7-稠合双环产物。