# 一、文献基本信息

**文章题目**：Emerging Technologies Empowering the Biosynthesis of Paclitaxel (赋能紫杉醇生物合成的涌现技术)

**文章 DOI 号**：10.70322/sbe.2026.10006

**期刊名称**：Synthetic Biology and Engineering (Synth. Biol. Eng.)，2026, 4(2), 10006

**通讯作者及工作单位**：

- **Xiaonan Liu**：湖北工业大学 工业发酵协同创新中心、发酵工程教育部重点实验室 (Cooperative Innovation Center of Industrial Fermentation, Hubei University of Technology)
- **Huifeng Jiang**：中国科学院天津工业生物技术研究所，低碳制造工程生物学实验室 (Key Laboratory of Engineering Biology for Low-Carbon Manufacturing, Tianjin Institute of Industrial Biotechnology, CAS)

---

# 二、核心摘要

紫杉醇 (paclitaxel, Taxol) 是源自珍稀红豆杉 (Taxus spp.) 的四环二萜类抗癌药物，其工业生产长期受限于 Taxus 资源稀缺与半合成路线的供给瓶颈。综述聚焦 2024-2026 年间紫杉醇生物合成途径解析与异源合成生物学研究中的系列突破，对约 20 步酶促反应的代谢网络进行系统重构，涉及细胞色素 P450 单加氧酶 (cytochrome P450 monooxygenases, P450)、α-酮戊二酸/Fe(II) 依赖性双加氧酶 (2-oxoglutarate/Fe(II)-dependent dioxygenases, ODD/OGD) 及酰基转移酶 (acyltransferases) 三大酶类。综述讨论了三条 Taxus 基因组 (T. chinensis、T. wallichiana、T. yunnanensis) 与 *Pseudotaxus chienii* 比较基因组分析所揭示的途径起源和 CYP725A 亚家族扩张；mpXsn 多重扰动-单核测序、MALDI 成像质谱 (MALDI-IMS)、TteUPO 来源的氧化酶工具箱 (oxidase toolbox) 及基因 dropout 等新兴技术如何在 Pathway I/II/III 分支与 C4β-C20 环氧、氧杂环丁烷 (oxetane) 形成、C13α-O-乙酰化-脱乙酰化模块等长期空白环节中识别新酶 (FoTO1、T9αOH-750C、T1βOH-184/686、T7AT、T7dA1/T79dA/T13dA1/T13dA2、CoAL(A312G)、T2′OGD、T3′NBT 等)。综述还系统评估了大肠杆菌、酿酒酵母、解脂耶氏酵母、本氏烟草、内生真菌与蓝藻等异源底盘的紫杉醇中间体生产能力、关键 P450 工程 (TS、T5αOH、T10βOH、DBAT) 与体内/体外的催化机制证据，并指出当前核心瓶颈仍为植物源 P450 与酰基转移酶的底物混杂性和催化效率低下。综述主张以多物种酶筛选、机器学习辅助酶工程、烟草原生底盘与微生物-化学协同路线来实现紫杉醇的可持续生产。

---

# 三、内容深度解读

### (一) 紫杉醇生物合成途径的整体架构

#### 1. 途径三阶段划分与近年重构

紫杉醇的生物合成被划分为三个阶段：第一阶段为从香叶基香叶基焦磷酸 (geranylgeranyl pyrophosphate, GGPP) 经紫杉二烯合酶 (taxa-4(5),11(12)-diene synthase, TS) 环化生成 taxa-4(5),11(12)-diene 核心骨架，并经 C5α 羟基化生成 taxadien-5α-ol；第二阶段为从 taxadien-5α-ol 经多步 P450 羟基化、酰基化和氧化生成巴卡丁 III (baccatin III)；第三阶段为苯丙氨酸经氨基变位酶 (phenylalanine aminomutase, PAM) 异构化为 β-phenylalanine，由 β-phenylalanyl-CoA 连接酶 (β-phenylalanine coenzyme A ligase, PCL/CoAL) 活化为 β-phenylalanyl-CoA 后，由 BAPT 在 C13 位与巴卡丁 III 连接，再经 C2′α 羟基化与 N3′ 苯甲酰化最终生成紫杉醇 (PDF 第 3-7 页)。综述强调近两年 (2024-2026) 在 Pathway I 与 Pathway II 分支、C4β-C20 环氧、氧杂环丁烷形成以及 C13α-O-乙酰化-脱乙酰化模块等长期空白环节集中取得突破，使得从 GGPP 到紫杉醇的几乎全部酶促反应都已被鉴定 (Table 1)。

#### 2. 关键酶与近期新发现

如表 1 与正文第 2 节 (PDF 第 7-8 页) 所述，已鉴定的紫杉醇途径酶包括 GGPP 合酶 (GGPPS)、TS、CYP725A 亚家族的多种 P450 (T5αOH、T13αOH、T10βOH、T7βOH、T2αOH、T14βOH、CYP725A4/37/55/T9αOH-1/T9αOH-750C/T1βOH-184/T1βOH-686)、酰基转移酶 (TAT、TBT、DBAT、BAPT、T7AT、TAX19)、去乙酰酶 (T7dA/T7dA1/T79dA/T13dA1/T13dA2)、OGD (TB328/T2′OGD/Tm576/TcOGD1/TcOGD2)、以及与 FoTO1 形成复合物的 T5αOH 和 TS。FoTO1 是 NTF2-like 蛋白，被证实与 T5αOH 形成多酶复合物，能够将上游途径产量提升 10-17 倍，并通过 D68/D149 双催化位点以异构化机制将不稳定的 4(5)-环氧紫杉二烯中间体定向转化为目标 T5α-ol (PDF 第 23-25 页)。这一发现打破了三十余年来以单一 P450 主导的线性途径假设，将紫杉醇生物合成重新定位为代谢网络。

#### 3. Pathway I/II/III 与 oxetane 形成的机制再评估

[图 2：紫杉醇生物合成途径总览] 系统归纳了从 taxadiene 到 baccatin III 再到 paclitaxel 的完整酶-中间体映射。Pathway I 与 Pathway II 均经过 taxusin 与 baccatin VI 两类新近认定为 on-pathway 中间体的紫杉烷，并经 13-hydroxytaxusin-TAX19-T2αOH-TBT-T7βOH-T7AT-TOT-T1βOH 序列形成 baccatin VI；自该节点，Pathway I 经 T7dA1/T9dA/T13dA/T9ox 顺序生成 baccatin III，Pathway II 则由 T9dA-T9ox-T7dA1-T13dA1 顺序完成 (PDF 第 6 页)。在氧杂环丁烷形成方面，作者将三项独立机制并列阐述：Kampranis 团队报告 CYP725A4 (T5αOH) 以两阶段环氧化机制催化形成氧杂环丁烷 (JACS 2023)；Yan 团队报告 TOT1 同时将双键结构转化为三元和四元环，DFT 计算表明氧杂环丁烷在动力学与热力学上均优于环氧化物 (Science 2024)；Zhou/Dai 团队通过对 CYP725A55/TmCYP1 的同位素标记证实氧杂环丁烷可能经直接氧化-酰基重排形成 (Nat Commun 2024)。综述指出，这些独立结果共同提示紫杉醇途径更接近于代谢网络而非线性路径。

### (二) 多组学驱动的演化起源与途径发现

#### 1. 红豆杉属基因组与 CYP725A 亚家族扩张

三套红豆杉参考基因组的发表 (T. wallichiana var. mairei、Himalayan yew、T. yunnanensis) 为途径起源分析提供了基础 (PDF 第 8-9 页)。Xiong 等 (Nature Plants 2021) 在 T. mairei 9 号染色体上定位了 paclitaxel 途径基因簇，并通过共调控网络鉴定到 17 个 CYP725A 基因、3 个转移酶与 10 个转录因子；Cheng 等 (Molecular Plant 2021) 在 T. wallichiana 中解析出 31 个候选 P450 基因并提出串联基因复制 (tandem gene duplication) 为该家族扩张的主要驱动力；Song 等 (Communications Biology 2021) 在 T. yunnanensis 中证实途径基因簇主要位于 12 号染色体并伴随 hydroxylase 家族的显著扩张。综述还讨论了 Shen 团队对 *Pseudotaxus chienii* 的染色体级基因组与 MALDI-IMS 联合分析 (Nat Commun 2025)：该工作通过 9999 个空间分辨数据点揭示了紫杉烷的组织特异性积累，并通过比较基因组指出 TBT/TOT1 步骤的中断可能将代谢流重定向至 taxusin 或类似物，同时在 *Torreya grandis* 中未检出 TS 同源基因，提示该物种不存在功能性的紫杉烷途径。

#### 2. 单细胞与单核转录组分辨的细胞类型特异表达

Yu 等在 *Taxus media* 茎组织中通过 UPLC-MS/MS 定量揭示 paclitaxel 与 10-DAB 主要在韧皮部积累、baccatin III 在髓部积累、3′-N-debenzoyltaxol (DAP) 在皮层与韧皮部积累，而四种代谢物在木质部均最低 (PDF 第 9-10 页)。后续基于质谱成像与单细胞转录组的整合分析 (Plant J 2023) 进一步将 TS、T14βOH、T5αOH 定位至内皮层细胞；T10βOH 与 DBTNBT 定位至木质部薄壁细胞；DBAT 定位至表皮细胞，并预测了 MYB、TEM、RAV、NAC 等细胞类型特异转录因子的靶位点，为植物底盘的亚细胞区隔策略提供了直接的空间表达证据。

#### 3. mpXsn 多重扰动-单核测序

mpXsn (multiplexed perturbation × single nuclei sequencing) 对 136 种处理 (包括激素、病原、途径中间体) 下的红豆杉组织进行单核 RNA 测序，构建了高分辨率基因共表达网络并将已知紫杉醇途径基因划分为早、中、晚三阶段表达模块，从中识别出 8 个新基因，包括 T9αOH-750C、T7AT、T1βOH-184/686、T9dA (DeAc898)、T7dA (DeAc1023) 等 (Nature 2025)。综述将 mpXsn 定位为从相关性转录组数据向因果性、基于网络的途径解析转变的范式工具。

### (三) 异源底盘工程：从原核到光合微生物

#### 1. 大肠杆菌与枯草芽孢杆菌

[图 1：演化与合成生物学总览] 与 [表 2：异源表达系统] 系统归纳了不同底盘的紫杉醇中间体生产能力。在 *E. coli* 中，Ajikumar 等 (Science 2010) 通过多变量模块化代谢工程将途径拆分为上游 IPP 模块 (dxs、idi、ispD、ispF) 与下游 taxadiene 模块 (GGPPS、TS)，并通过 TS 与 T5αOH 共表达将 taxa-4(5),11(12)-diene 产量提升约 15000 倍至 **1 g/L**，将 T5α-ol 提升 2400 倍至 **58 ± 3 mg/L**，首次让原核底盘触及下游 P450 氧化的可行性边界 (PDF 第 10-11 页)。在 *Bacillus subtilis* 168 中，Abdallah 等 (Front Microbiol 2019) 通过过表达 MEP 途径与 IspA/crtE 将 taxa-4(5),11(12)-diene 提升 83 倍至 **17.8 mg/L**，展示了革兰阳性细菌作为前体平台的潜力。然而综述明确指出，原核底盘的限制包括：(1) 缺乏内部膜系统与 P450 N-端疏水区相容；(2) P450 必需的 NADPH 与细胞色素 P450 还原酶 (CPR) 电子传递链效率受限；(3) 缺少真核细胞器区隔，无法实现中间体的时空分布 (PDF 第 11-12 页)。

#### 2. 酿酒酵母与解脂耶氏酵母

在 *S. cerevisiae* 中，综述梳理了从早期 Engels 等 (Metab Eng 2008) 的 UPC2-1/tHMGR/GGPPS/TS 共表达 (8.7 mg/L) 到 Nowrouzi 等 (Microb Cell Fact 2020) 通过 MBP 标签的多拷贝 TS 与 GAL1 启动子在 20 °C 培养下达 **129 mg/L** taxadiene 的系列里程碑 (PDF 第 12 页)。Walls 等 (2021) 在 1 L 生物反应器中获得 taxadiene 71 ± 8 mg/L (95 h)，并报告 T5αOH 主产物 OCT/iso-OCT/T5α-ol 分别达 16 ± 3、44 ± 3 与 42 ± 4 mg/L，T5α-Ac 达 21 ± 0.3 mg/L，但 T5α-ol 转化率始终低于 10%。Nowrouzi 等 (2022) 进一步通过融合蛋白策略与 10 mL resting cell 系统将氧化 taxanes 推至 **361.4 ± 52.4 mg/L**、T5α-ol 至 **38.1 ± 8.4 mg/L** (PDF 第 12-13 页)。Min 等 (2023) 通过计算代谢工程在酵母中将 taxadiene 推至 **215 mg/L**。在 *Y. lipolytica* 中，Xu 等 (2023) 通过 SUMO-TS 融合与 tHMG1/GGS1/TS 过表达在 fed-batch 中获得 **101.4 mg/L** taxadiene。综述指出，2024 年 Yan 团队在酵母中重建 T5α-ol 至 1β-dehydroxybaccatin VI 的高度氧化途径，但 BAPT 在酵母中表达不稳定性成为瓶颈；2025 年 Kampranis 团队通过 Protein-Sol 预测与 MBP-IGGG 融合构建 MBPig3BAPTm 变体，使 BAPTm 转化率提升 27%，并通过 CoAL(A312G)-MBPig3BAPTm-T2′OGD-T3′NBT 整合与补料 baccatin III 与 β-phenylalanine 在酵母中获得 **0.59 ± 0.03 μg/L** 的紫杉醇滴度 (PDF 第 13 页)。

#### 3. 植物底盘：拟南芥与本氏烟草

在 *Arabidopsis thaliana* 中，Besumbes 等 (2004) 通过 CaMV 35S 启动子驱动 TS 表达获得 taxadiene，但出现下胚轴素矮化、叶绿素缺失、生长迟缓与开花延迟等表型，反映出 taxadiene 对植物发育的潜在毒性；改用糖皮质激素诱导型启动子可缓解表型但产量仍较低 (PDF 第 13-14 页)。在 *N. benthamiana* 中，Li 等 (2019) 通过叶绿体区隔 TS/T5αOH/CPR 与 MEP 强化获得 **56.6 ± 3.2 µg/g** 鲜重 taxadiene 与 **1.3 ± 0.5 µg/g** 鲜重 T5α-ol；Fu 等 (2021) 通过叶绿体转运肽融合在 *N. tabacum* cv. Xanthi 中将 taxadiene 推至 **87.8 µg/g** 干重；Zhang 等 (2023) 通过瞬时表达 nsTXS/nsGGPS/HMGR 等 13 个基因整合途径生成 **154.87 ng/g** 鲜重 baccatin III 与 **64.29 ng/g** 鲜重 paclitaxel；Jiang 等 (2024) 通过 TOT/T9αOH-1 与 7 个已知酶共表达获得 **50 ng/g** 干重 baccatin III，并通过亚细胞定位证明 GGPP 在叶绿体中环化为 taxadiene 后转运至胞质，由 ER 锚定的 T2αOH、T5αOH、T7βOH、T9αOH、T13αOH、TOT 与胞质酰基转移酶 TAT/TBT 协同生成 baccatin III (PDF 第 14-15 页)。2025 年 McClune 等 (Nature) 通过 7 新基因 + 9 已知基因 (TS、T5αOH、TAT、T10βOH、DBAT、T13αOH、T2αOH、TBT、TOT) 与 FoTO1 共表达在本氏烟草中获得 **10-30 μg/g 干重** baccatin III，产量与红豆杉针叶天然含量相当 (PDF 第 15 页)。Li 等 (bioRxiv 2026) 通过加入 T13dA1/T79dA/T7dA1 的 C13α-O-乙酰化-脱乙酰化模块重构 18-19 基因途径，结合 T9αH-750C 获得 **23 µg/g 干重** baccatin III (PDF 第 15-16 页)。综述明确指出，TB328 这一 α-KG 依赖性双加氧酶虽在 *E. coli* 与 *S. cerevisiae* 中无法功能性表达，但能在烟草底盘中介导 C4β-C20 环氧化，使 baccatin III 的 de novo 合成首次在该植物中实现, 凸显了植物底盘在膜定位、辅因子与分子伴侣环境方面对植物源 P450/OGD 的独特相容性。

#### 4. 内生真菌与蓝藻

综述对内生真菌的现状评估较为保守：物理/化学诱变与原生质体融合可将一株真菌的紫杉醇滴度从 125.7 μg/L 提升至 **468.62 μg/L**，但仍存在菌株不稳定、滴度低、可放大性差等问题；CRISPR/Cas9 通过同时敲除 squalene synthase 与 cycloartenol synthase 重定向甾醇代谢的策略仍处于早期 (PDF 第 18 页)。综述将内生真菌定位为未来挖掘新酶零件的潜在遗传资源库，而非工业底盘。在 *Synechocystis* sp. PCC 6803 中，Ma 团队通过 MEP 模块与紫杉醇级联合成 DIGT-P560 株，从 CO₂ 直接产出 **17.43 mg/L** 氧化紫杉烷与 **4.32 mg/L** T5α-ol，首次实现光合自养紫杉醇前体生产 (PDF 第 18-19 页)。

### (四) 关键酶的工程化与催化机制

#### 1. TS 的结构-功能与突变体改造

TS 包含 862 个氨基酸残基，N-端约 80 残基为质体定位信号，C-端 S553-V862 为 I 类萜环化酶 (DDXXD、(N,D)DXX(S,T)XXXE motif 与三核 Mg²⁺ 簇负责焦磷酸解离)，N-端 M107-I135 与插入结构域 S349-Q552 为 II 类萜环化酶 (DXDD motif 负责双键/环氧质子化) (PDF 第 19-20 页)。基于 TS 晶体结构 (Koksal et al, Nature 2011) 的定点突变已识别出 Y688、W753、S713、C803 等关键残基：Y688L 偏向生成 taxa-4(20),11(12)-diene，使下游 T5αOH 介导的 T5α-ol 产量提升 2.4 倍；W753H 完全改变产物谱，使其转向 cembrene A；S713T 保留 97.4% 活性。综述指出 TS 在发酵条件下将 **93.2%** GGPP 转化为 taxa-4(5),11(12)-diene、4.7% 为 taxa-4(20),11(12)-diene，但下游只有 < 10% 经 T5αOH 进入目的通路, 这一定量数据为上游产物调控与下游酶瓶颈分析提供了关键基准。

#### 2. T5αOH 的双机制争议与晶体结构解析

综述详细论述了 T5αOH (CYP725A4) 催化机制的两种长期假设 (PDF 第 20-21 页)：Yadav 等提出 ferryl-oxo 在 C3/C13/C20 的竞争性氢抽取导致产物多样性；Edgar 等提出 taxa-4(5),11(12)-diene 先经环氧化为不稳定的 4(5)-epoxide，再经非特异裂解生成 T5α-ol 与 OCT/iso-OCT。Barton 等进一步证实 4(5)-epoxide 在酸性条件下尤其在铁-卟啉存在下发生多种重排，对其中间体身份提出质疑。2024 年 Song 等 (ACS Catal) 通过 X 射线晶体学、MD、QM/MM 与 QM 计算解析了 CYP725A4-taxadiene 复合物结构，证实氧化首先产生两性离子中间体；可分两路经过：经水介导重排生成 T5α-ol，或经氧原子质子化、氢迁移与 C-O 偶联生成 OCT/iso-OCT；taxa-4(20),11(12)-diene 则直接经 C5 羟基化生成 T5α-ol 而无需环氧化物中间体。综述据此将 T5αOH 的机制争议从定性争论推进到基于复合体结构的能量学层面。

#### 3. FoTO1：兼具催化与支架功能

综述整合两项 preprints 阐释 FoTO1 的双功能 (PDF 第 23-24 页)：Bai 等 (bioRxiv 2026) 通过体外重建、定点突变与 QM/MM 证实 FoTO1 是专一的环氧异构酶，D68/D149 二联体通过静电活化驱动环氧开环异构化生成 T5α-ol；Wick 等 (bioRxiv 2026) 进一步发现 FoTO1 通过 C 端延伸模块与 P450 形成蛋白-蛋白相互作用，作为非催化支架组织多酶复合体以提升 pathway 效率，且该支架功能在其他植物二萜途径中具有可推广性。该双重角色将长期被认为仅作为辅因子的 FoTO1 重新定位为兼具催化与支架两类机制的关键节点。

#### 4. T10βOH、DBAT 与 TteUPO 氧化酶工具箱

Zhang 等 (Appl Microbiol Biotechnol 2023) 通过 AlphaFold2 建模 + PROSS 预测 + FoldX 评估识别 T10βOH 三点突变 I75F/L226K/S345V，三点组合使底物转化率提升 **2.8 倍**、异源表达量提升 **9.5 倍** (PDF 第 21-22 页)。DBAT 改造方面，Li 等 (Nat Commun 2017) 通过丙氨酸扫描鉴定 G38R/F301V 双突变使催化效率提升 6 倍，G38R 单点提升 2.15 倍；Lin 等 (Mol Biotechnol 2018) 通过 I43S/D390R 改善催化效率并可利用乙烯乙酸酯作为经济性酰基供体 (PDF 第 22 页)。氧化酶工具箱 (Lai 等, Nat Commun 2025) 在 29 个真菌氧化酶中筛选 TteUPO，构建多突变体文库实现 taxane 在 C4、C6、C10、C11、C12、C13 的位点特异氧化，并在 *E. coli* 中实现氧化 taxane 的 de novo 合成 (PDF 第 22-23 页)。综述将这一策略定位为取代植物源膜结合 P450 的可溶性、细菌表达平台，克服 P450 异源表达与电子传递链组装的长期瓶颈。

### (五) 涌现技术：从数据到机制再到通路

#### 1. MALDI-IMS 空间代谢组

MALDI-IMS (Shen 团队) 在 *Pseudotaxus* 茎、叶、韧皮等冷冻切片上生成至高密空间代谢分布图，识别紫杉烷组织特异积累并指导亚细胞区隔策略与组织特异启动子选择 (PDF 第 24-25 页)。综述指出当前局限包括通量较低、需要专用仪器、绝对定量困难以及同分异构体难以分辨。

#### 2. dropout 实验与最小基因集

Zhang 等 (Mol Plant 2023) 通过在 *N. benthamiana* 中逐基因 dropout 鉴定 baccatin III 与 paclitaxel 合成的最小必需基因集，包括 C4β-C20 epoxidase、T9αOH、T1βOH、PCL 等 (PDF 第 25 页)。该方法将共表达或转录组相关性证据提升为因果性遗传证据。

#### 3. 机器学习与多物种酶筛选

综述将多物种酶筛选与机器学习辅助酶工程定位为未来破解 P450/酰基转移酶混杂性、提升代谢通量的核心方法 (PDF 第 25-26 页)。具体方向包括基于序列-结构-功能的指纹训练上调 Pal-like P450 的区域/化学选择性，以及通过 deep mutational scanning 与分子动力学辅助筛选突变体。

---

# 四、总结与展望

### 4.1 总结

综述将紫杉醇生物合成研究的最新进展概括为以下层面：**第一**，途径层面已从三十年来的线性模型演化为可被 PK 区精确定义的代谢网络，从 GGPP 到紫杉醇的约 20 步酶促反应及其关键分支 (Pathway I/II/III、C4β-C20 环氧、oxetane 形成、C13α-O-乙酰化-脱乙酰化模块) 已基本鉴定；**第二**，机制层面，T5αOH/CYP725A4 的两性离子中间体路径与 FoTO1 兼具环氧异构酶与多酶支架的双重角色，从结构生物学层面重构了上游瓶颈；**第三**，技术层面，mpXsn、MALDI-IMS、dropout 与 TteUPO 工具箱将发现-验证闭环从单基因/纯相关性跃迁至网络级因果解析；**第四**，底盘层面，本氏烟草以 23-30 µg/g 干重 baccatin III 接近天然红豆杉针叶含量，确立其作为完整途径重构的优势底盘，而 *E. coli* 与 *S. cerevisiae* 在 taxadiene 阶段 (1 g/L、215 mg/L、361.4 mg/L 氧化 taxanes) 仍为最高产前体平台，蓝藻首次实现光合自养前体生产。综述的核心学术贡献在于系统整合近两年 (2024-2026) 的多学科证据，提出以多物种酶筛选+机器学习辅助工程+植物底盘+化学-生物协同作为突破当前 P450/酰基转移酶混杂性与代谢通量瓶颈的整体路线图。

### 4.2 展望

作者明确指出的未来方向集中在三点。其一，**底盘-酶协同进化**：现有异源平台的核心约束仍为 P450 与酰基转移酶的底物混杂性、膜定位需求、NADPH 供给以及分子伴侣相容性差异，未来需结合多物种酶筛选 (红豆杉近缘种、*Pseudotaxus chienii*、*Torreya grandis* 等) 与机器学习辅助的 P450 工程，对 CYP725A 家族进行系统性功能多样性挖掘并设计催化选择性可控的突变体。FoTO1 的非催化支架功能在其他植物二萜途径中的可推广性也为开发模块化蛋白支架提供了新思路。其二，**原生与光合底盘的能力拓展**：本氏烟草在膜定位 P450/OGD 上的相容性优势使其成为完整 baccatin III 通路重构的最优底盘，但仍需解决多基因瞬时共表达的稳定转化、农杆菌介导的规模化生产与烟草原生细胞工厂的可放大性问题；*Synechocystis* PCC 6803 通过 CO₂ 直接合成 T5α-ol 的成功开辟了光合自养路线，但目前产量仍处于 mg/L 量级，未来需结合光合电子传递优化与碳通量重定向以提升经济可行性。其三，**化学-生物协同路线**：作者主张利用微生物底盘构建 taxane 多环核心骨架，再由化学方法引入侧链官能团，以互补方式规避下游生物催化的低效率环节、减轻传统全合成的环境压力与能耗。这一前瞻性思路同时需要发展标准化的化学-酶法接口 (例如 β-phenylalanine 类似物的多样性扩展) 与自动化的途径-化学组合设计平台。综合来看，紫杉醇生物合成的研究范式已从传统基因挖掘转向系统性底盘重建，未来突破将取决于多学科 (基因组学、结构生物学、机器学习、合成生物学、有机化学) 的深度耦合。