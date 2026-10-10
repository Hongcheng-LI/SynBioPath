![image.png](https://synbiopath.online/20261010094620877.png)

# 一、基本信息

**文章题目**：The genetic basis for the production of toxic quinolizidine alkaloids in lupins

**文章 DOI 号**：10.1126/science.aie5520

**期刊名称**：Science

**通讯作者及工作单位**：

- **Fernando Geu-Flores**：哥本哈根大学植物与环境科学系 (Department of Plant and Environmental Sciences, University of Copenhagen)

# 二、研究背景

羽扇豆（Lupinus spp.）是种子蛋白含量极高的豆科作物，但多数栽培材料积累苦味且有毒的喹诺里西啶生物碱 (quinolizidine alkaloids, QAs)，限制了其作为食品和饲料蛋白源的利用。QAs 具有抗胆碱能毒性，传统育种虽已获得低碱“甜”品种，但残留 QA 水平随季节波动，常超过食品安全限量。QA 生物合成以 L-赖氨酸为起点，已知早期酶包括赖氨酸脱羧酶 (LDC)、铜胺氧化酶 (CAO) 和 BAHD 乙酰转移酶 (AT)，晚期酶包括 CYP71D189、SDR1 和 HMT/HLT，但核心喹诺里西啶骨架如何形成、哪些酶参与骨架重排、立体选择性如何建立以及晚期分支如何产生不同 QAs，长期不清楚。这一知识缺口既阻碍低碱品种的精准选育，也限制了对复杂生物碱骨架形成机制的酶学认识。作者因此以窄叶羽扇豆 (narrow-leafed lupin, NLL; *Lupinus angustifolius*) 为对象，试图补全 QA 途径并应用于低碱育种。

# 三、研究思路

作者以 NLL 中已知的 *LDC* 为诱饵，利用多组织转录组进行共表达分析，筛选与 QA 途径共调控且系统发育特异性较高的候选基因，其中包括多个主要乳胶蛋白样蛋白 (major latex protein-like proteins, MLPLs)、细胞色素 P450、还原酶和水解酶。随后在本氏烟草 (*Nicotiana benthamiana*) 中逐步重构途径：先以 LDC、CAO、AT 为起点，加入候选酶，通过 LC-MS、GC-MS 和 NMR 鉴定新中间体；再通过基因 dropout 判断每个候选酶对终产物 (-)-sparteine 的贡献。对关键步骤，作者用大肠杆菌表达纯化 MLPL2 进行体外平衡实验，区分酶催化与自发反应。最后，作者在 NLL 突变体库中分离敲除株验证途径，并利用白羽扇豆 (*L. albus*) 泛基因组和遗传分析鉴定甜基因 *exiguus*，同时构建 *HYD* 敲除低碱 NLL 材料，形成从基因发现、异源重构、体外酶学、化学结构到体内遗传验证的闭环。

# 四、研究方法

- **共表达与候选基因筛选**：基于 NLL 多组织 RNA-seq 的 TPM 数据，以 *LDC* 为诱饵计算 Pearson 相关系数，结合 BLASTX 系统发育特异性筛选候选 QA 基因。
- **本氏烟草瞬时表达与途径重构**：农杆菌介导共表达已知和候选基因，进行逐步延伸、基因 dropout、外源 (-)-sparteine 喂养及突变等位基因功能测试。
- **LC-MS/GC-MS 分析**：提取离子色谱、精确质量、与标准品或植物提取物共洗脱，定量 QAs 和中间体；手性 GC-MS 测定 ammodendrine 和 sparteine 的对映体过量。
- **体外酶学**：大肠杆菌表达纯化 MLPL2，以 Δ<sup>1</sup>-piperideine 或 tetrahydroanabasine 为底物，监测平衡建立，经 NaBH<sub>4</sub> 还原和苯甲酰化后 GC-MS 分析。
- **NMR 与 HRMS 结构鉴定**：纯化 2-hydroxyammodendrine (12) 和 1,2-didehydrolusitanine (13)，通过 1D/2D NMR 和精确质量确定结构。
- **遗传突变体与泛基因组分析**：从 NLL FIND-IT 突变库筛选 KO 株，TaqMan 和 Sanger 验证；在白羽扇豆泛基因组中查找 *MLPL1* 失活突变，并通过 gDNA/cDNA 测序和异源表达验证。
- **表达定位与系统发育**：激光显微切割转录组、DeepLoc/TargetP 预测亚细胞定位，InterPro/Pfam 和最大似然树分析 MLPL 与 IRED 家族。

# 五、实验设计及结果分析

### (一) 共表达筛选锁定 QA 核心途径候选基因

作者首先需要回答“早期乙酰化之后到 (-)-sparteine 之间的未知酶是什么”。Figure 1 以化学逻辑图总结了当时已知和推定的 QA 反应：L-赖氨酸经 LDC、CAO 生成 Δ<sup>1</sup>-piperideine (3)，其二聚化产生 tetrahydroanabasine (4)，再被 AT 乙酰化为 ammodendrine (5)；此后需经过氧化、脱乙酰、重排、加入第三个 piperideine 单元和还原，才能形成 (-)-sparteine (6)。Figure 1B 则展示从 6 到 (+)-lupanine (8)、(+)-13α-hydroxylupanine (9)、(-)-angustifoline (10) 和酯化 QA 的晚期分支。该图本身不是新实验数据，而是全文的路线图和缺口定义。

![image.png](https://synbiopath.online/20261010093934774.png)

为找到缺失酶，作者以 *LDC* 为诱饵进行共表达分析，发现 *AT*、*CAO* 和 *CYP71D189* 位于最紧密共表达转录本中。进一步按系统发育特异性筛选后，获得 31 个候选，包括 3 个 CYP450、3 个还原酶、1 个水解酶、1 个酰基转移酶和 6 个 MLPL。补充表 S1 记录了这些候选。该设计的核心假设是：植物特殊代谢途径基因常共表达，且新途径酶往往比初级代谢同源物具有更低的 BLASTX 相似性。这一策略成功锁定了后续验证的多个关键酶，但共表达本身只提供候选，不能证明功能。

### (二) MLPL2/6 加速二聚化并支持动态动力学拆分

为了检验 MLPL 是否参与早期 QA 途径，作者在本氏烟草中共表达 LDC、CAO、AT，并分别加入 GFP 或 MLPL1–6，检测 ammodendrine (5) 的积累。Figure 2A 显示，只有 MLPL2 和 MLPL6 使 5 的峰面积相对 GFP 对照提高约 3 倍，而 MLPL1、3、4、5 无显著影响。由于 MLPL2 与 MLPL6 蛋白同一性约 93%，提示二者功能冗余。手性 GC-MS 进一步显示，产生的 5 接近对映体纯，约 96% ee，且该 ee 在缺少 MLPL2 或 MLPL6 时并未改变，说明决定立体选择性的不是 MLPL，而更可能是 AT。

![image.png](https://synbiopath.online/20261010094002595.png)

为了直接观察 MLPL 功能，作者纯化 MLPL2，分别以 3 或 4 为起点进行体外时间进程实验。补充图 S7 显示，MLPL2 能从两个方向加速 3 与 4 之间平衡的建立。该结果支持作者提出的模型：MLPL2 并非传统意义上形成新共价键的催化酶，而是加速自发平衡，使 AT 能够对 (+)-4 进行动态动力学拆分，最终高效生成 (+)-5。现有数据直接证明 MLPL2 足以加速平衡，但精确催化机制、活性位点及 MLPL6 的独立贡献仍未完全解析。

### (三) CYP76E36 触发乙酰化喹诺里西啶核心形成

在确定 ammodendrine (5) 之后，作者需要解释喹诺里西啶骨架如何形成。Figure 2B 显示，在 LDC、CAO、MLPL2、AT 基础上加入 CYP76E36 后，底物 5 减少，并出现三个新化合物峰，其中两个在色谱上非常接近。经纯化和 NMR 鉴定，这两个化合物分别为 2-hydroxyammodendrine (12) 和 1,2-didehydrolusitanine (13)。Figure 2C 提出机制：CYP76E36 羟化 5 生成 12，随后 12 自发重排为含喹诺里西啶亚胺核心的乙酰化双环中间体 13。该结果是全文核心突破之一：**喹诺里西啶骨架以乙酰化形式组装，CYP76E36 足以催化关键羟化并触发后续重排**。不过，重排本身是否完全自发、CYP76E36 是否还影响重排速率，现有数据尚不能完全区分。

### (四) 逐步重构至 (-)-sparteine 与基因 dropout

为了补全至 (-)-sparteine (6) 的途径，作者将剩余候选 MLPL、HYD、IRED1 和 IRED2 与前述酶共表达。Figure 3A 给出推定途径，Figure 3C 的 LC-MS 提取离子色谱显示，完整组合可产生 6 以及少量 α-isosparteine (16) 和 β-isosparteine (17)。为判断每个候选酶的必要性，作者进行 dropout 实验，将单个基因替换为 GFP。Figure 3B 显示，缺失 MLPL2、CYP76E36、HYD 或 MLPL1 时，6 降至痕量或检测不到；缺失 MLPL3 或 MLPL4 则显著降低 6；单独缺失 IRED1 或 IRED2 不影响 6，但同时缺失二者则完全不能产生 6，说明二者功能冗余；缺失 MLPL5 无影响。该组数据将异源重构的“充分性”与突变体中的“必要性”联系起来，但冗余基因和未测试组合仍是证据边界。

![image.png](https://synbiopath.online/20261010094053434.png)

Figure 3D–F 进一步分析立体选择性。当加入 IRED3 时，6 相对于 16 和 17 的比例显著提高，纯度从约 86% 提高到约 96%，产量无显著变化；手性 GC-MS 显示 6 的对映体过量从约 60% 提高到约 97%。作者据此提出，IRED3 可能通过 redox-neutral 方式纠正自发产生的错误立体异构体，确保最终产物以 (-)-6 为主。该结果直接证明 IRED3 提高立体选择性，但其精确催化机制仍待结构生物学和定点突变验证。

### (五) 晚期途径重构至 lupanine 及酯化 QAs

在获得 (-)-6 后，作者转向 NLL 中主要积累的晚期 QAs。Figure 4A 显示，在提供外源 (-)-6 的条件下，共表达 CYP71D189 和 SDR1 可产生 (+)-lupanine (8)；进一步加入 CYP71A168 可产生 (+)-13α-hydroxylupanine (9) 和 (-)-angustifoline (10)；加入 HLT1/2 后产生 13α-tigloyloxylupanine (11) 和 13α-benzoyloxylupanine (21)。这些产物的保留时间和质谱与 NLL 叶片提取物中的对应峰一致。Figure 4B 提出机制：CYP71D189 和 SDR1 将 6 氧化为 8；CYP71A168 可能经 lupanin-13-yl radical 中间体 (29) 生成 9 和 10；HLT1/2 催化 9 与 tigloyl-CoA 或 benzoyl-CoA 酯化。该部分证明这些酶对晚期转化具有充分性，但 CYP71A168 的环裂解机制及自由基中间体仍属作者提出的合理模型。

![image.png](https://synbiopath.online/20261010094116928.png)

### (六) 白羽扇豆 *exiguus* 甜基因的鉴定

为了验证途径知识的育种价值，作者挖掘白羽扇豆泛基因组，寻找新发现 QA 基因的失活突变。Figure 5A 显示，甜品种 Neuland 的 *MLPL1* 存在剪接位点突变 G184C，命名为 *MLPL1*<sup>exiguus</sup>；Neutra 和 Gyulatanya 也分别携带移码或剪接突变。cDNA 分析表明，Neuland 产生两种异常转录本。Figure 5B 在 N. benthamiana 中比较 GFP、*MLPL1*<sup>WT</sup> 和 *MLPL1*<sup>exiguus</sup>，发现突变等位基因不能恢复 6 的合成，表型类似 GFP，并伴随 16 比例升高。Figure 5C 显示，Neuland 叶片积累 12、13、23、24 等中间体，与 *MLPL1*<sup>exiguus</sup> 异源表达模拟的化学表型相似。Figure 5D 进一步显示，Neuland 中 8 降低而 18 相对升高，说明 MLPL1 参与第三个 piperideine 单元的立体选择性加入。该部分将遗传定位、cDNA 和异源功能验证结合，**鉴定出 *exiguus* 甜基因是 *MLPL1* 的功能丧失等位基因**，但该突变在天然白羽扇豆途径中的精确生化后果仍需体内酶学补充。

![image.png](https://synbiopath.online/20261010094211022.png)

### (七) NLL *HYD* 敲除低碱材料与其他突变体验证

作者进一步在 NLL 中验证 HYD 的功能。HYD 是去除乙酰基的水解酶。Figure 5E–F 显示，*HYD*<sup>KO</sup> 种子中正常 QAs 几乎全部低于检测限，仅 (+)-9 略高于检测限，同时积累早期中间体和旁路产物，其中以 lusitanine (25) 为主。该结果支持 HYD 在途径中的关键去乙酰化作用，并证明敲除 *HYD* 可产生低碱 NLL 材料。作者还分离了 *CYP76E36*、*MLPL4*、*MLPL1*、*CYP71A168* 和 *IRED3* 等 KO 株，其化学表型与途径模型基本一致。例如 *CYP76E36* KO 积累 ammodendrine (5)，*CYP71A168* KO 积累 lupanine (8)，*IRED3* KO 导致 (+)-6 和 (-)-17 积累。这些遗传数据增强了途径模型的可靠性，但部分冗余基因未能获得双突变，因此某些步骤的必要性仍未完全排除补偿效应。

![image.png](https://synbiopath.online/20261010094221769.png)

### (八) 基因组分布、组织定位与总结模型

Figure 6 是全文总结模型，展示从 L-赖氨酸到 (-)-6、8、9、10、11 和 21 的 15 个酶步骤，其中新鉴定酶用红色标出，新引入原子用蓝色标出，并标明通往 α-pyridone、lupanine-type、martine-type 和 Ormosia 型生物碱的分支。补充图 S33 显示 QA 基因除局部重复外分散于 NLL 基因组，未形成紧密基因簇；补充图 S34 表明早期基因主要在绿色器官表皮表达，晚期基因也延伸到叶肉和维管组织；补充表 S3 和补充图 S35 预测 LDC 位于叶绿体、CAO 和 HLT1/2 位于过氧化物酶体，其余多为胞质。该部分将生化途径置于组织和亚细胞背景中，但亚细胞定位多为计算预测，仍需荧光蛋白融合或单细胞转录组验证。

![image.png](https://synbiopath.online/20261010094241925.png)

# 六、总体结论

本研究在窄叶羽扇豆中建立了一个包含 15 个酶步骤的 QA 生物合成途径，并新鉴定 9 个酶。核心机制包括：MLPL 家族蛋白加速自发化学平衡，CYP76E36 催化 ammodendrine 羟化并触发乙酰化喹诺里西啶骨架形成，HYD 去除隐藏乙酰基，MLPL1 和 IRED3 参与第三个 piperideine 单元的立体选择性组装，CYP71A168 和 HLT1/2 负责晚期氧化、环裂解和酯化。**作者据此提出，QA 途径并非完全由传统“成键酶”逐步催化，而是由加速自发平衡的 MLPL、立体纠错型氧化还原酶和少数关键 P450 共同塑造。** 应用层面，作者鉴定了白羽扇豆 *exiguus* 甜基因 *MLPL1*，并构建了 *HYD* 敲除的低碱 NLL 材料。该工作为羽扇豆及其他含 QA 豆科的精准育种和异源生产 (-)-sparteine 提供了遗传与生化基础。

# 七、论文评价

### 优点与创新

本文最具辨识度的创新是首次补全了羽扇豆 QA 核心途径，并发现 MLPL 蛋白以“加速自发平衡”而非传统催化成键的方式参与复杂生物碱合成。CYP76E36 催化羟化并触发喹诺里西啶骨架重排，是机制上的关键突破；IRED3 提高非对映和对映选择性，揭示了特殊代谢途径中立体纠错的新策略。作者将共表达筛选、异源重构、dropout、体外酶学、NMR 结构鉴定、NLL 突变体和白羽扇豆泛基因组分析结合，形成了较强的正交证据链。此外，*HYD*<sup>KO</sup> 和 *exiguus* 的鉴定直接展示了途径知识在低碱育种中的应用价值。

### 未来研究方向

后续最优先的方向之一是解析 MLPL 加速平衡和 IRED3 立体纠错的精确催化机制，例如通过结构生物学、定点突变和预稳态动力学区分“加速平衡”与“定向催化”。另一个方向是评估 *HYD*<sup>KO</sup> 种子中积累的 lusitanine (25) 等旁路产物的毒性，并开展定量毒理和田间稳定性试验；这将决定该低碱材料能否真正用于食品和饲料。此外，在酵母等底盘中进行 (-)-sparteine 异源生产的产量和可放大性也值得检验。

# 八、关键问题及回答

**Q1：MLPL 是否真正“催化”了 QA 途径中的关键反应，还是仅加速自发平衡？**

**A**：现有证据更支持后者。纯化 MLPL2 在体外能从 3 和 4 两个方向加速平衡建立，但并未改变最终平衡位置；在 N. benthamiana 中，MLPL2/6 使 ammodendrine (5) 增加约 3 倍，而决定 5 对映体纯度的主要是 AT，而非 MLPL。因此，MLPL 的生理角色可能是通过加速亚胺平衡，使下游酶能够进行动态动力学拆分。作者据此提出 MLPL 参与多个步骤，但精确催化机制、活性位点以及各 MLPL 是否具有底物特异性仍缺少直接结构证据。将其简单称为“催化成键酶”并不准确。

**Q2：异源重构和基因 dropout 能否证明某基因在天然途径中必需？**

**A**：不能单独证明。N. benthamiana 共表达多个基因生成产物，通常证明这些基因对该转化具有充分性；dropout 造成产物减少或消失，可支持该基因在重构体系中重要，但仍可能受表达水平、蛋白稳定性和宿主背景影响。本文的强项是进一步在 NLL 中分离了 *CYP76E36*、*MLPL4*、*MLPL1*、*CYP71A168*、*IRED3* 和 *HYD* 等 KO 株，其化学表型与模型一致，从而增强了必要性证据。然而，MLPL2/6、IRED1/2 等存在功能冗余，部分双突变未能获得，因此这些步骤在天然途径中的必要性仍未完全闭环。

**Q3：*HYD*<sup>KO</sup> 低碱羽扇豆是否可以直接视为安全育种材料？**

**A**：尚不能直接下结论。*HYD*<sup>KO</sup> 种子中正常 QAs 大幅降低，仅 (+)-9 略高于检测限，说明低碱目标已初步实现。但该材料同时积累 lusitanine (25) 等早期中间体和旁路产物，其毒性据既有研究可能介于 lupanine 和 13α-hydroxylupanine 之间。作者也指出，需要定量 25 并进行毒理评估，才能与现有甜品种比较安全性。因此，*HYD*<sup>KO</sup> 是有前景的育种起点，但在食品和饲料应用前，必须完成旁路产物定量、毒理和田间稳定性验证；将其与 *iucundus* 等甜等位基因堆叠，可能进一步降低总 QA 和中间体水平。