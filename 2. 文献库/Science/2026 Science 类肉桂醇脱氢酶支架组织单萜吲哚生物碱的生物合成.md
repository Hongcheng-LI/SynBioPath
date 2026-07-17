# 一、基本信息

**文章题目**：A cinnamyl alcohol dehydrogenase–like scaffold organizes monoterpenoid indole alkaloid biosynthesis

**文章 DOI 号**：10.1126/science.aeb0357

**期刊名称**：Science

**通讯作者及工作单位**：
- **王雅婕**：西湖大学工程学院 (School of Engineering, Westlake University, Hangzhou, China)；西湖大学合成生物学与生物集成工程中心 (Westlake Center of Synthetic Biology and Integrated Bioengineering, Westlake University, Hangzhou, China)
- **曲洋**：新不伦瑞克大学化学系 (Department of Chemistry, University of New Brunswick, Fredericton, NB, Canada)
- **连佳长**：浙江大学生物质化工教育部重点实验室，化学工程与生物工程学院 (Key Laboratory of Biomass Chemical Engineering of Ministry of Education, College of Chemical and Biological Engineering, Zhejiang University, Hangzhou, China)；北京生命科学研究院 (Beijing Life Science Academy, Beijing, China)；浙江省智能生物材料重点实验室 (Zhejiang Key Laboratory of Smart Biomaterials, Zhejiang University, Hangzhou, Zhejiang, China)


# 二、研究背景

单萜吲哚生物碱 (monoterpenoid indole alkaloids, MIAs) 是一类结构多样且具有重要药用价值的天然产物，其家族成员超过 3,000 种，其中包括抗肿瘤药物长春碱 (vinblastine)、抗疟疾药物奎宁以及镇痛药物吗啡喃类生物碱等。长春碱生物合成途径的完全解析历时数十年，涉及约 30 步酶促反应，是植物次生代谢研究领域的标志性成就。该途径的完整阐明使得在酵母等异源宿主中实现长春碱及其前体的从头生物合成成为可能。然而，目前酵母细胞工厂中的 MIA 产量仍处于微克每升水平，距工业化生产所需的克每升阈值相距甚远。这一产量瓶颈的根本原因在于途径的冗长性以及 MIA 生物合成在植物细胞内的复杂区室化分布。

在 MIA 生物合成途径中，strictosidine 是所有 MIAs 的通用前体，于液泡中合成后转运至细胞核。在细胞核内，strictosidine β-葡萄糖苷酶 (strictosidine β-glucosidase, SGD) 切除其葡萄糖基团，生成高度不稳定的中间体 strictosidine aglycone。该中间体随后由一类类肉桂醇脱氢酶 (cinnamyl alcohol dehydrogenase, CAD) 还原酶催化转化为稳定的异构体，从而进入下游多样化途径。在长春碱途径中，该还原步骤由 geissoschizine 合成酶 (geissoschizine synthase, GS) 催化，生成关键分支点中间体 geissoschizine。此前的研究已表明，SGD 定位于细胞核并含有一个 bipartite 核定位信号，而 GS 主要分布于细胞质中，虽然部分也存在于细胞核。双分子荧光互补 (bimolecular fluorescence complementation, BiFC) 实验未能检测到 GS 与 SGD 之间的直接相互作用，这与另一 CAD 家族成员 heteroyohimbine 合成酶 (HYS) 的情况形成鲜明对比——后者能够与 SGD 在细胞核内发生物理互作。这一矛盾暗示着存在一个未知因子，负责介导 GS 与 SGD 之间的空间耦合，并促进 strictosidine aglycone 从 SGD 向 GS 的高效传递。

本研究以这一科学问题为切入点，旨在鉴定该缺失的分子衔接因子，并阐明其对 strictosidine aglycone 加工过程的调控机制。作者提出，这一因子的发现不仅能够填补 MIA 生物合成区室化调控的关键空白，还可能为利用合成生物学实现 MIA 的高效异源生产提供全新的工程策略。


# 三、研究思路

本研究的总体逻辑遵循“基因筛选—功能验证—机制解析—异源应用—演化拓展”的递进式研究范式。作者首先基于前期发现的 CAD 基因簇及其与 MIA 生物合成基因的共表达特征，采用病毒诱导的基因沉默 (virus-induced gene silencing, VIGS) 技术对候选基因进行功能筛选，锁定了 CAD2（即 VinBLAST）作为潜在的 SGD-GS 衔接因子。随后，通过在产 MIA 的酿酒酵母和毕赤酵母菌株中异源表达 VinBLAST，验证其对多种 MIA 终产物（geissoschizine methyl ether, catharanthine, vindoline）产量的促进作用。

在机制层面，作者综合运用 BiFC、酵母双杂交 (yeast two-hybrid, Y2H)、表面等离子体共振 (surface plasmon resonance, SPR) 和 pull-down 等蛋白互作检测技术，系统表征了 VinBLAST 与 SGD、GS 之间的物理相互作用及其亚细胞定位。同时，通过分子动力学 (molecular dynamics, MD) 模拟结合定点突变，分别鉴定 VinBLAST-SGD 和 VinBLAST-GS 的相互作用界面关键残基，进而利用催化失活突变体和界面突变体解析 VinBLAST 各功能维度（支架作用与催化活性）对 MIA 合成的相对贡献。此外，为了探究 VinBLAST 增强 GS 催化效率的结构基础，作者通过 MD 模拟比较了 GS 同源二聚体与 VinBLAST-GS 异源二聚体的底物通道构象及近攻击构象 (near-attack conformation, NAC) 频率，并通过隧道突变加以验证。

最后，作者通过共线性分析和系统发育分析追溯 VinBLAST 在植物界的演化分布，并选取来自 MIA 产生物种和非产生物种的多个同源蛋白，通过体外酶活和酵母发酵实验验证其功能的保守性，从而揭示 CAD 蛋白家族在植物次生代谢中的非经典功能演化路径。


# 四、研究方法

- **病毒诱导的基因沉默 (VIGS)** ：在长春花 (Catharanthus roseus) 叶片中分别沉默 CAD1-CAD5 候选基因，通过 UPLC-MS/MS 检测 MIA 代谢谱变化，以评估各基因对 MIA 生物合成的功能贡献。
- **酵母异源表达系统**：将 VinBLAST 及其突变体整合至产 geissoschizine methyl ether、catharanthine 和 vindoline 的工程化酿酒酵母 (Saccharomyces cerevisiae) 菌株中，通过 24 孔板培养和补料分批发酵评估产量变化。
- **双分子荧光互补 (BiFC)** ：在酿酒酵母和本氏烟草 (Nicotiana benthamiana) 叶片表皮细胞中表达融合 mVenus 片段的 SGD、GS 和 VinBLAST 及其突变体，通过共聚焦显微镜检测黄色荧光信号，以鉴定蛋白-蛋白相互作用及亚细胞定位。
- **酵母双杂交 (Y2H)** ：将 SGD、GS 和 VinBLAST 分别融合至 GAL4 的 DNA 结合结构域和激活结构域，通过营养缺陷型培养基筛选验证相互作用界面。
- **表面等离子体共振 (SPR)** ：将 SGD 固定于传感芯片表面，检测梯度浓度的 GS、VinBLAST 及 VinBLAST-GS 混合物的结合响应，计算解离常数 (K<sub>d</sub>)。
- **pull-down 实验**：使用 His 标签标记的 VinBLAST 及突变体结合镍柱，检测对无标签 GS 的捕获能力，验证异源二聚体形成。
- **分子动力学模拟**：基于 AlphaFold3 预测的 VinBLAST-GS 异源二聚体结构和已有晶体结构 (PDB ID: 8A3N)，采用 GROMACS 软件和 Amber 力场进行超过 1,000 ns 的模拟，分析底物通道构象和 NAC 频率。
- **共线性分析和系统发育分析**：利用 MCScanX、SynMap 和 GFF 工具比较多个植物基因组中 GS-VinBLAST 基因座的保守性；通过最大似然法构建 CAD 蛋白家族的系统发育树。
- **加权基因共表达网络分析 (WGCNA)** ：基于长春花叶片和根组织的转录组数据，以 STR、GS 和 GO 为诱饵基因，筛选共表达基因模块。


# 五、实验设计及结果分析

### (一) VinBLAST 的发现与功能验证

#### 实验目的与设计逻辑

为了寻找介导 SGD 与 GS 相互作用的未知因子，作者首先对长春花中 CAD 基因簇进行了共表达分析。前期的基因组学研究已揭示长春花中存在一个包含 GS、8HGO、ASO 及其同源基因的 MIA 生物合成基因簇。作者推测该基因簇中可能存在尚未表征的组分，能够作为 SGD 与 GS 之间的内源衔接子。为验证这一假设，作者以 STR、GS 和 GO 为诱饵基因进行了 WGCNA，筛选与之高度共表达的候选基因，并通过 VIGS 实验评估这些候选基因对 MIA 代谢谱的影响。

#### 实验结果与机理解析

WGCNA 分析结果显示，两个位于 GS 基因簇中与 GS 紧密相邻的 CAD 家族基因 CAD1 和 CAD2，与 STR、GS 和 GO 表现出强烈的共表达相关性（图 2A）。**值得注意的是，这 3 个诱饵基因均与 VinBLAST 及多个关键 MIA 合成酶（包括 dihydroproecdylocarpine synthase (DPAS)、stemmadenine 形成还原酶 Redox1/2、stemmadenine O-乙酰转移酶 SAT、tabersonine 合成酶 TabS 和 8HGO）存在共表达关系。** 这一结果表明 CAD1 和 CAD2 可能参与 MIA 生物合成的调控。

作者随后通过 VIGS 对 CAD1-CAD5 进行了功能沉默。沉默 CAD3-CAD5 对 MIA 谱无显著影响，但沉默 CAD2 导致了显著的表型变化：**catharanthine 和 vindoline 的含量分别下降 93.5% 和 83.7%** ，而 HYS 来源的 MIAs（amygdaline 和 serpentine）分别上升 6.1 倍和 3.7 倍（图 2B）。这一表型与先前报道的 GS 沉默结果高度一致，表明 CAD2 沉默导致 geissoschizine 代谢流从 GS 分支被重定向至 HYS 分支。qPCR 检测证实 VIGS-CAD2 植物中 CAD2 转录本下降 88.7%，而 CAD1 仅下降 38.5%，GS 转录本略有上升（图 2C）。

在确认 CAD2 的体内功能后，作者将 CAD2 表达盒整合至产 GME、catharanthine 和 vindoline 的酿酒酵母工程菌株中。**结果显示 3 种产物的滴度分别提高 13.7 倍、18.4 倍和 13.1 倍**（图 2D）。类似地，在产 catharanthine 的毕赤酵母菌株 CAN19 中引入 CAD2 使其产量提升 10.2 倍。在补料分批发酵条件下，产 catharanthine 的酿酒酵母菌株 CA02 从甘油和半乳糖等简单碳源中实现了 **164.9 mg L<sup>-1</sup>** 的 catharanthine 产量（图 2E）。基于这些结果，作者将 CAD2 命名为 VinBLAST（Vinca 生物碱生物合成定位与激活支架衔接子）。

### (二) VinBLAST 作为 SGD 与 GS 的物理支架

#### 实验目的与设计逻辑

上述结果表明 VinBLAST 对 MIA 生物合成具有显著的促进效应。为了揭示其作用机制，作者假设 VinBLAST 作为一个非催化性的支架蛋白，物理介导 SGD 与 GS 的相互作用，从而解决 strictosidine aglycone 在细胞核内从 SGD 到 GS 的低效传递问题。为验证这一假设，作者采用 BiFC、Y2H 和 SPR 等多种蛋白互作检测技术，系统鉴定 VinBLAST、SGD 和 GS 三者之间的物理相互作用及亚细胞定位。

#### 实验结果与机理解析

BiFC 实验显示，SGD 在酵母细胞核内存在强烈的自相互作用，与其已知的寡聚结构一致；GS 单独存在时不与 SGD 相互作用，且主要定位于细胞质。单独表达 VinBLAST 时其主要分布于细胞质。**值得关注的是，VinBLAST 与 SGD 在细胞核内相互作用，而与 GS 则在细胞质中相互作用**（图 3A）。当无标签的 VinBLAST 与 GS-SGD BiFC 体系共表达时，作者在细胞核内清楚地观察到了 GS 与 SGD 之间的相互作用信号（图 3B），**这直接证明 VinBLAST 确实是一个此前未被识别的支架蛋白，能够介导 GS 与 SGD 之间的物理连接。**

SPR 实验进一步量化了三者之间的结合亲和力。结果显示 GS 与 SGD 无可检测的结合，而 VinBLAST 与 SGD 之间的解离常数 K<sub>d</sub> 约为 **1.48 μM**，VinBLAST 与 GS 之间的 K<sub>d</sub> 约为 **0.48 μM**。值得注意的是，**VinBLAST 与 GS 的等摩尔混合物与 SGD 之间的结合亲和力进一步增强至 K<sub>d</sub> ≈ 0.57 μM**（图 3C），表明 VinBLAST 和 GS 同时存在时能够协同增强与 SGD 的结合。

为了排除 VinBLAST 自身的 CAD 催化活性对 MIA 产量提升的贡献，作者构建了 NADPH 结合必需的催化活性丧失双突变体 VinBLAST<sup>C51A,H56A</sup> (VinBLAST<sup>CM</sup>)。该突变体在体外无 strictosidine aglycone 还原活性，但其与 SGD 和 GS 的相互作用能力在 BiFC 和 Y2H 中均未发生改变。在酵母中表达 VinBLAST<sup>CM</sup> 仍能获得与野生型 VinBLAST 相当的 GME、catharanthine 和 vindoline 产量（图 2D）。**这些结果确证 VinBLAST 的支架功能与其 CAD 催化活性彼此独立，前者是 MIA 生物合成增强的主因。**

为了定量评估支架功能的贡献，作者进一步鉴定了 VinBLAST 与 SGD 相互作用界面的关键残基。MD 模拟预测 K359 为 VinBLAST 中介导 SGD 结合的关键残基，BiFC、Y2H 和 SPR 实验均证实 VinBLAST<sup>K359G</sup> 突变体与 SGD 的相互作用显著减弱甚至消失，而保留与 GS 的结合能力。在酵母中表达 VinBLAST<sup>K359G</sup> 后，GME、catharanthine 和 vindoline 的产量分别降至野生型水平的 **27.9%** 、**29.8%** 和 **32.8%** （图 2D）。**这一结果明确表明，VinBLAST 介导的 SGD-GS 物理连接是驱动 MIA 高效生物合成的关键因素。**

### (三) VinBLAST 对 GS 催化活性的变构增强

#### 实验目的与设计逻辑

前述结果已明确 VinBLAST 作为物理支架的职能，但作者注意到人工蛋白支架策略仅能将 MIA 产量提升 1.8 至 3.7 倍，远低于 VinBLAST 所达到的 13 至 18 倍增强效果。这一差异暗示 VinBLAST 可能还具有支架功能之外的额外调控机制。作者由此提出假设：VinBLAST 与 GS 形成的异源二聚体可能直接调控 GS 的催化活性。为验证该假设，作者开展了体外酶活测定、MD 模拟和结构突变分析。

#### 实验结果与机理解析

体外酶活测定显示，VinBLAST 能显著增强 GS 的催化速率。**动力学分析表明，VinBLAST 将 GS 的 V<sub>max</sub> 提升了 24.3 倍**，而底物结合亲和力 K<sub>m</sub> 未发生明显变化。这一结果表明 VinBLAST 影响了 GS 活性中心的构象而非底物识别过程。

为进一步阐明结构机制，作者进行了 MD 模拟。鉴于 GS、HYS 及相关 CAD 家族成员均具有保守的 β-折叠稳定的同源二聚体结构，作者推测 VinBLAST 与 GS 可能通过类似的 β-折叠结构基序形成异源二聚体。Native PAGE 实验证实了异源二聚体的存在。MD 模拟首先鉴定了 GS 同源二聚体的关键界面残基 I301，该残基通过酰胺骨架相互作用稳定 β-折叠界面。**将 I301 突变为谷氨酸 (GS<sup>I301E</sup>, GS<sup>IM</sup>) 后，模拟显示 β-折叠间距从约 5 Å 扩大至约 10 Å**，BiFC 证实 GS 自相互作用消失，且体外和体内催化活性完全丧失。这一结果证明了 GS 二聚化对其催化功能的必要性。

随后，作者通过 MD 模拟鉴定了 VinBLAST-GS 异源二聚体界面中介导相互作用的关键残基 M298 和 V299（图 4, A 和 B）。为验证这一位点，作者构建了 VinBLAST<sup>M298E,V299E</sup> (VinBLAST<sup>IM</sup>) 以破坏异源二聚化。BiFC 和 Y2H 均显示 VinBLAST<sup>IM</sup> 与 GS 的相互作用显著减弱，pull-down 实验也证实 VinBLAST<sup>IM</sup> 无法有效保留 GS 于亲和柱上。**在酵母中表达 VinBLAST<sup>IM</sup> 后，GME、catharanthine 和 vindoline 的产量分别降至野生型 VinBLAST 水平的 18.7%** 、**10.5%** 和 **12.8%** （图 2D）。**这些结果共同表明 VinBLAST 与 GS 的异源二聚化不仅是支架功能的结构基础，也是变构增强 GS 催化活性的必要条件。**

### (四) 底物通道重塑与催化效率提升的结构机制

#### 实验目的与设计逻辑

在确证 VinBLAST-GS 异源二聚化增强 GS 催化速率的基础上，作者进一步探究其结构机制。作者推测异源二聚体的形成可能改变了 GS 活性中心的底物进入通道，从而提高底物 4,21-dehydrogeissoschizine 到达催化位点的效率。为验证这一假设，作者比较了 GS 同源二聚体和 VinBLAST-GS 异源二聚体中底物通道的构象差异，并通过隧道突变和 NAC 频率分析加以验证。

#### 实验结果与机理解析

MD 模拟揭示了 VinBLAST-GS 异源二聚体与 GS 同源二聚体在底物通道结构上的显著差异。**在异源二聚体中，来自 VinBLAST 的 H<sup>288</sup>SAPLLMGRK<sup>297</sup> 片段与来自 GS 的 P<sup>290</sup>AAPLIMGKR<sup>299</sup> 片段共同构成了底物通道的壁面**（图 4C），与同源二聚体中仅由两个 GS 单体相应片段形成的通道相比，通道构型发生了明显重塑（图 4A）。NAC 频率分析进一步显示，在 VinBLAST-GS 异源二聚体中，底物处于近攻击构象的频率为 **41.6%** ，而在 GS 同源二聚体的两个活性位点中分别为 **23.0%** 和 **26.5%** （图 S37）。**这一更高的 NAC 频率表明异源二聚体中的底物更易于达到过渡态几何构型，与动力学实验中观察到的速率加速效应相一致。**

为了验证隧道结构对催化性能的直接影响，作者设计了 GS 隧道突变体 GS<sup>P290H,A291S,I295L</sup> (GS<sup>TM</sup>)，使其隧道结构模拟 VinBLAST-GS 异源二聚体的构型。**体外酶活测定显示 GS<sup>TM</sup> 的 V<sub>max</sub> 较野生型 GS 提升了 5.3 倍**（图 4D）。在酵母中表达 GS<sup>TM</sup> 使 MIA 产量提高 2.0 至 2.7 倍，而进一步通过人工蛋白支架将 GS<sup>TM</sup> 与 SGD 连接后，产量提升幅度扩大至 4.9 至 7.5 倍。相反，作者构建了反向隧道突变体 VinBLAST<sup>H288P,S289A,L293I</sup> (VinBLAST<sup>TM</sup>) 使其隧道结构趋近于 GS 样构型，该突变体使异源二聚体的活性降低了 24.9%（图 4D）。**这些结果确证 VinBLAST-GS 异源二聚化通过重塑底物隧道构型来增强 GS 的催化效率。**

### (五) VinBLAST 同源蛋白功能的演化保守性

#### 实验目的与设计逻辑

鉴于 geissoschizine 是自然界中超过 700 种 MIA 的中央前体，作者推测 VinBLAST 的同源蛋白可能在多种 MIA 产生植物中广泛存在并发挥类似功能。为验证该假说，作者开展了跨物种的共线性分析、系统发育分析以及功能互补实验，并进一步将考察范围扩展至非 MIA 产生物种，以探究 CAD 蛋白家族这一非经典功能的演化起源。

#### 实验结果与机理解析

共线性分析显示，在龙胆目 MIA 产生物种中，包括 Rauvolfia tetraphylla（夹竹桃科）、Gelsemium sempervirens（钩吻科）和 Mitragyna speciosa（茜草科），均存在保守的 VinBLAST-GS 基因簇（图 5A）。**令人关注的是，该基因簇同样存在于非 MIA 产生的龙胆目物种如 Calotropis gigantea（夹竹桃科）和 Eustoma grandiflorum（龙胆科），以及唇形目的 Nepeta mussinii 和茄科的 Solanum lycopersicum 中**（图 5A）。该共线性区域甚至可以追溯至约 1.48 亿年前与其他谱系分化的葡萄 (Vitis vinifera) 中，提示这一古老的基因组区域可能是 CAD 还原酶（包括 GS 和 VinBLAST）在多个植物谱系中演化的热点。

系统发育分析将 VinBLAST、GS 及其同源蛋白归入 CAD 进化枝 III（图 5B）。与进化枝 I 中功能明确参与木质素合成的 CAD 不同，进化枝 III 中成员的体内功能此前大多未知。**基于 VinBLAST 与其他 CAD 高达 70% 以上的氨基酸序列一致性，其支架功能很可能在进化枝 III 的其他同源蛋白中同样存在。**

为验证这一预测，作者选取了来自 MIA 产生物种和非产生物种的多个 VinBLAST 同源蛋白进行了体外和体内功能测试。体外实验显示，所有测试的 VinBLAST 同源蛋白均能增强对应 GS 的活性。例如，**来自 Strychnos spinosa（马钱科）的 VinBLAST 将其同源 SspGS 的体外活性提升 13.2 倍**，而长春花 VinBLAST 对 SspGS 的增强效应高达 44.5 倍。更为引人注目的是，来自葡萄和本氏烟草（图 5B）的 VinBLAST 同源蛋白（二者均非 MIA 产生物种）也能分别将长春花 GS 的活性提升 2.7 倍和 1.8 倍（图 5C）。在酿酒酵母中，这些同源蛋白对 GME、catharanthine 和 vindoline 的产量表现出不同程度的促进效应，**最高提升幅度分别达到 19.0 倍、23.9 倍和 24.2 倍**（图 5D）。BiFC 实验进一步证实了本氏烟草 VinBLAST 同源蛋白与长春花 GS 在细胞质中、与 SGD 在细胞核中的互作（图 5E）。**综合上述结果，VinBLAST 的支架功能在植物界具有广泛的保守性，其可能从祖先 CAD 演化而来，在 MIA 生物合成中获得了特化的、不可或缺的支架职能。**


# 六、总体结论

本研究鉴定并表征了一种来源于 CAD 蛋白家族的支架蛋白 VinBLAST，**其作为 MIA 生物合成途径中的非催化性衔接子，通过物理介导 strictosidine β-葡萄糖苷酶 SGD 与 geissoschizine 合成酶 GS 在细胞核内的相互作用，解决了高度不稳定的 strictosidine aglycone 中间体从 SGD 到 GS 的低效传递这一关键生物学问题。** VinBLAST 的作用机制包含两个在功能上协同的维度：一是作为物理支架将 GS 锚定于 SGD 所在的细胞核内；二是通过与 GS 形成异源二聚体，重塑 GS 活性中心的底物通道构型，**将 GS 的催化速率 V<sub>max</sub> 提升 24.3 倍**。两个维度的功能均独立于 VinBLAST 自身微弱的 CAD 催化活性，构成了植物次生代谢中一种非典型酶功能演化的范例。

该发现在合成生物学应用层面具有重要价值：**在工程化酿酒酵母中引入 VinBLAST 使 catharanthine 产量达到 164.9 mg L<sup>-1</sup>，较此前报道提升近 1,000 倍**，为长春碱及其他 geissoschizine 衍生药物的工业化生物制造提供了可行的技术路径。**此外，VinBLAST 同源蛋白在包括葡萄和烟草在内的多种非 MIA 产生植物中广泛存在并保留功能活性**，揭示 CAD 蛋白家族在植物次生代谢中的非经典功能具有深远的演化保守性，也为在非模式植物中挖掘未知代谢调控元件提供了新的视角。


# 七、论文评价

### 优点与创新

该研究在多个层面展现出突出的学术价值与方法论创新。在科学发现层面，作者揭示了一种此前未知的代谢调控范式——来源于经典木质素合成酶的 CAD 蛋白通过“功能切换”成为次生代谢途径中专一性的支架蛋白，这一发现扩展了人们对酶家族功能演化的认知。在机制解析层面，本研究将支架功能进一步拆解为“物理募集”和“变构激活”两个维度，并利用 MD 模拟与定点突变的紧密耦合，**从近攻击构象频率和底物通道构型两个角度揭示了异源二聚化增强催化效率的结构基础**，为理解蛋白-蛋白相互作用对酶动力学调控提供了精细的分子图像。

在技术策略层面，本研究实现了多组学筛选（WGCNA）、计算结构生物学（MD 模拟）、细胞生物学（BiFC 亚细胞定位）和合成生物学（酵母异源重构）的深度融合。尤其是将 VinBLAST 引入酵母细胞工厂时所取得的产量跃升，有力地证明了基础机制研究对合成生物学工程策略的指导价值——**人工蛋白支架策略无法达到 VinBLAST 同等水平的增强效果**，凸显了自然演化出的调控机制在效率上的优势。整体而言，该工作代表了植物天然产物生物合成领域从“途径解析”向“途径调控”研究范式转变的一个典型范例。

### 未来研究方向

本研究为后续探索提出了若干值得深入的问题。首先，VinBLAST 对 SGD 和 GS 相互作用的动态调控机制尚不完全清楚——VinBLAST 是否在特定发育阶段或胁迫条件下被诱导表达，其与 SGD 和 GS 的结合是否受到翻译后修饰或代谢物浓度的调节，这些问题有待进一步探究。其次，本研究的体外实验表明 VinBLAST 同源蛋白在多个非 MIA 产生物种中保留功能，这提示 CAD 蛋白的支架功能可能参与其他尚未被鉴定的次生代谢途径，未来可在更广泛的植物物种中进行代谢组学与蛋白互作组学的联合筛选。此外，VinBLAST 所展示的“催化惰性”支架如何通过共进化获得与 GS 的特异性互作界面，也是一个值得从演化生物学角度深入探究的课题。最后，将 VinBLAST 介导的产量提升策略推广至其他 MIAs 及更广泛的植物天然产物的异源生物合成，具有重要的合成生物学应用前景。


# 八、关键问题及回答

**Q1**：VinBLAST 自身保留的 CAD 催化活性虽然远低于经典的木质素 CAD，但其对 strictosidine aglycone 是否仍具有低水平的还原活性？如果存在这种活性，是否可能对 geissoschizine 的立体化学纯度产生影响？

**A**：作者通过体外酶活实验检测了 VinBLAST 对 strictosidine aglycone 的还原活性，结果显示其在标准反应条件下对该底物无检测到的催化活性（图 S11）。这与 GS 形成鲜明对比——GS 能够特异性将 strictosidine aglycone 还原为 geissoschizine。VinBLAST 对肉桂醛和松柏醛等典型 CAD 底物仍具有还原活性，但其催化效率 (k<sub>cat</sub>/K<sub>m</sub>) 比长春花叶片中负责木质素合成的 clade I CAD 低 144 倍，表明其在植物体内的主要功能已不再是 CAD 催化。更重要的是，催化活性丧失的双突变体 VinBLAST<sup>CM</sup> 在 BiFC 中与 SGD 和 GS 的互作模式完全不变，在酵母中对 MIA 产量的促进效应也与野生型相当（图 2D）。这些证据共同表明 VinBLAST 的 CAD 活性残余在生理条件下可忽略不计，不会干扰 geissoschizine 的立体化学纯度或代谢流分配。

**Q2**：本研究中 VinBLAST 被鉴定为一个“非催化性支架”，但它与经典意义上的代谢物 (metabolon) 中的支架蛋白（如 Boccia 等人 2024 年在 Science 上报道的 GAME15）有何本质区别？

**A**：两者虽然同属植物次生代谢中的支架蛋白，但功能模式和机制细节存在显著差异。GAME15 被报道为甾体生物碱 (steroidal glycoalkaloids) 生物合成中的支架蛋白，其与途径中的多个酶形成稳定的代谢物复合体，可能通过物理临近效应促进底物通道。而 VinBLAST 的独特之处在于其功能是“双重的”：一方面作为物理支架介导 SGD 与 GS 的细胞核内互作，另一方面通过异源二聚化变构重塑 GS 的底物通道结构并显著提升其催化速率 (V<sub>max</sub> 增加 24.3 倍)。这种“变构激活”效应无法仅通过物理临近来解释——人工蛋白支架最多仅能实现 3.7 倍的产量提升，远不及 VinBLAST 的效果。此外，VinBLAST 是从一个具有催化活性的 CAD 酶演化而来，其自身的 CAD 活性已大幅退化（降低 144 倍），而 GAME15 的演化起源则不同。因此，VinBLAST 代表了一种“催化功能退化的同时获得双重调控功能”的非典型酶演化模式，在机制层次上比经典的代谢物支架更为复杂。

**Q3**：VinBLAST 同源蛋白在非 MIA 产生的物种（如葡萄和烟草）中保留了对 GS 的增强活性，这一发现是否暗示葡萄和烟草体内可能存在内源的 strictosidine aglycone 类似物或其他未知底物，使得这些“孤儿”CAD 蛋白在自然条件下具有生理功能？

**A**：这是一个极具洞察力的推论。作者在讨论部分已明确指出，葡萄和烟草虽不以生产 MIAs 而闻名，但它们确实具有完整的莽草酸途径和萜类代谢网络。strictosidine aglycone 的吲哚部分来源于色氨酸，而萜烯部分来源于 secologanin——这两类前体在绝大多数植物中均存在，只是缺乏 strictosidine 合成酶 (STR) 而无法生成 strictosidine。因此，葡萄和烟草中的 VinBLAST 同源蛋白在自然条件下不会遭遇 strictosidine aglycone，其生理底物应另有其物。本研究的意义在于，**这些同源蛋白在体外和酵母中能够识别并结合异源的 CrGS 和 CrSGD，说明它们的支架功能识别界面具有相当的序列保守性和可塑性**。这提示 CAD 进化枝 III 的成员可能具有一种尚未被认识的“通用型”蛋白-蛋白相互作用能力，可能在各自宿主中参与其他依赖于酶复合体组装的代谢途径。未来可通过免疫共沉淀结合质谱的方法，在葡萄或烟草中寻找这些 CAD 同源蛋白的内源互作蛋白，有望揭示新的植物代谢调控网络。