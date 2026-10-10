---
type: literature-reading
zotero_key: 8ZTA7F52
doi: "10.1016/j.apsb.2021.03.029"
paper_type: research
classification_status: pending
reading_status: main-text-and-figures-read
review_status: codex-source-checked
human_full_paper_review: false
source_attachment: 6C6F8K4Y
source_sha256: 234e385d4ffd914a177a1de5b61aa619c030652af21754485f7206bcb7f0655d
created: 2026-10-10
---

> 原文来源：[Zotero 条目](zotero://select/library/items/8ZTA7F52)；[DOI](https://doi.org/10.1016/j.apsb.2021.03.029)；由当前 Codex 读取原始主文并核对图表，尚未经人工逐项复核。 来源限制：PDFtextlayer mapsmu tom visuallyFigure2C/body101.6ugpergDCW Figure3CugmL Figure2BmgpergDCW；MainPDFarticleinpress final11(10)3322-3334fromliveZotero notprintedreadversion；SIabsent NMR spectraassignmentsCoASHwaterfractionC7epimersS1-7 notindependentlyreviewed；Figure3captionandmethod2.5 gmLvsaxisbodymgmL1000xunitconflict；Results3.4refFig5 actualfermentationFigure6 sourceconflict；MseriesmodulesversusRDBATstrains notinterchangeable；AcCoApoolAU/mgperDCW/mgLnotflux andDBATgelgraynotactivity；Eq1conversionis10DABpeakareadisappearance nottargetmolaryieldselectivity massconcentrationrationotmolconversion；R10notmax8hAcCoA highratiooutputgrowthconfounding；AceticacidbothpHandsupply cannotassignindependentcausalcontributions；CoASH20K6combined50fromunavailableSI notformalstatisticalsynergy potassiumphosphatesnotfullyionmatched；ReverseCoASHacetylacceptor notexclusivelywaterhydrolysis proposedbranchesremain；InitialacidpHgroupsdifferentfrommaintainedpHgroups 55htotal24hproduction；3Lreactorinitial1L finalvolumeafterfeedingnotfullyreconstructed；86percent2.59over3not7.5 crudeextract HPLCpuritynotgravimetricpurity；Figure2/3n3biorepsSD Figure1/6n3SDnotallsamereplicatedefinition allP/CI/rawpointsabsent；External10DABnotdenovobaccatin/PTX historicalhighestnotcurrentverifiedrecord industrialcostnotshown。

# 文献基本信息

**题目：** Construction of acetyl-CoA and DBAT hybrid metabolic pathway for acetylation of 10-deacetylbaccatin III to baccatin III。中文解读：乙酰供体、DBAT 逆向反应与 baccatin III 全细胞转化的耦合。

**作者与出处：** Hao Wang、Bo-Yong Zhang、Ting Gong、Tian-Jiao Chen、Jing-Jing Chen、Jin-Ling Yang、Ping Zhu；前两位共同第一作者，Ping Zhu 为通讯作者。主要单位为中国医学科学院、北京协和医学院药物研究所。Zotero 当前记录为 Acta Pharmaceutica Sinica B，2021，11(10)：3322–3334，DOI：10.1016/j.apsb.2021.03.029。本次实际读取的是带 ARTICLE IN PRESS 标识的 13 页 PDF；最终卷期页码来自本地 Zotero 元数据，不把该版本的内部页码当成正式排版页码。下文定位均指 PDF 页码。

**来源与阅读范围：** Zotero key 8ZTA7F52，主附件 6C6F8K4Y。完整阅读正文、方法、讨论及参考文献，并逐页查看全部 13 页，保留 Scheme 1、Table 1、Figure 1–6 共八张完整原图表。现有附件中未取得 SI，因此补充图谱、引物、原始数据和补充发酵曲线不作为已独立核实内容。原始 PDF SHA-256：234e385d4ffd914a177a1de5b61aa619c030652af21754485f7206bcb7f0655d。当前暂存，全部解读完成后再分类。

# 研究背景

10-deacetylbaccatin III（10-DAB）是紫杉醇半合成的原料，DBAT 将其 C10 羟基乙酰化，得到 baccatin III。单独使用酶时需要供应 acetyl-CoA，而采购化学计量的供体不利于规模化。因此，这篇论文将供体生成与乙酰转移整合在 E. coli BL21(DE3) 内，用细胞自身代谢支持一个外加复杂底物的末端转化。

问题有两层：供体是否足够，以及生成的产物是否能在反应液中保留。作者发现随着培养液碱化，已经生成的 baccatin III 会下降，并伴随 10-DAB 回升。因而高供体水平不必然对应最终高产量；正向转化、反向去乙酰化、非酶促不稳定性和细胞生长负担需要同时考察。该研究实际解决的是外加 10-DAB 的生物转化，未重建紫杉烷骨架，也未合成完整 paclitaxel。

# 研究思路

作者先用不同 acetyl-CoA 模块筛选宿主，再引入 Taxus cuspidata 的 dbat，将供体积累能力与实际产物输出连接；随后追踪 pH、底物和产物随时间变化，判断为何反应后期倒退；通过缓冲液、空宿主、工程宿主、纯酶和宿主匀浆比较拆分逆向过程；最后在补料培养中调节乙酸与 pH，检验克级产物积累及分离。

Scheme 1 同时画出糖、乙酸供给 acetyl-CoA 和碱性条件下的反向反应。这不是单纯“增加供体酶即可增产”的故事，而是将反应方向和产物稳定性纳入细胞工厂设计。乙酸兼具前体和酸化作用，两种作用在部分实验中一起改变，因此不能仅凭加乙酸增产就分配各自贡献比例。


![Scheme 1 原文第 3 页](https://synbiopath.online/8ZTA7F52-Scheme-1-complete.png)

*Scheme 1：Scheme1.Forwardexternal10DABacetylationandreverseunderalkalineconditions;notdenovotaxanecore/PTX.（原文 PDF 截图）。*


# 研究方法

**材料与构建。** 主宿主为 E. coli BL21(DE3)，M0 为基础宿主，M1–M12 为供体模块组合；在 M0、M7、M8、M10 中加入 dbat 后，结果中分别称 R0、R7、R8、R10。Table 1 与 Figure 1 提供载体、基因组合和菌株对应关系。M10 的核心为 PDH（aceE、aceF、lpdA）、PANK 与 ACS 变体；ACS 是来源于 Salmonella enterica 的 acetyl-CoA synthetase L641P，文中致谢给出 AAO71645.1。这里是将单个代谢酶用于供体生成，实验宿主仍是 BL21(DE3)，不混淆酶来源与培养菌株。构建方法中使用的菌株编号与结果的 R 系列写法需结合上下文对应，不把所有 M 菌株都当作已经携带 DBAT。


![Table 1 原文第 3 页](https://synbiopath.online/8ZTA7F52-Table-1-complete.png)

*Table 1：Table1.AllM0-M12modulesandplasmids;R0/R7/R8/R10areDBATaddedcounterparts notallMstrainsequivalent.（原文 PDF 截图）。*


**检测与计量。** 供体采用相应分析方法测定；图中既有 A.U. 相对水平，也有 mg/g DCW 或 mg/L，分母不同，不能直接跨图排序。DBAT 用 SDS-PAGE 条带灰度作半定量，不等于活性蛋白量或酶催化速率。底物与产物由 HPLC 定量，产物 LC–MS 与标准品比较，正文报告 [M+H]+ 为 587.3。作者另外报告 NMR 鉴定，但谱图和归属在 SI，未取得附件，不能声称本次已经逐峰复核。

**转化率定义。** 方法公式是反应前后 10-DAB HPLC 峰面积减少量除以初始峰面积。因此下文 98%、97%、78% 均为作者定义的底物消失转化率，不自动等于 baccatin III 的摩尔收率或选择性。乙酰化改变分子质量，所以“产物 g/L ÷ 输入底物 g/L”也不是同一指标。Figure 5 的质谱与结构支持两者区别，完整物料平衡仍需核算残留、异构体及其他产物。

**重复与统计。** Figure 2、3 明确 n=3 生物学重复、均值±SD；Figure 1、6 写 n=3 和 SD，但没有同样明确逐一说明重复性质。Figure 4、5 的所有检测不能统一补写成三次独立生物学重复。文中未为每项比较提供精确 P 值、置信区间或完整原始点，本笔记不自行赋予统计显著性。

# 实验设计及结果分析

### 1. 供体模块筛选：增加通路酶并不总是增加 acetyl-CoA

**观察：** Figure 1 展示十二种组合。增加 PDH 的 M1 供体水平约为 M0 的 1.8 倍；继续提高 PGK/GAPD 后，M2、M3 反而下降。降低相关表达载体拷贝数的 M4 部分改善，组合 PANK 与 ACS 后 M10 最优，正文称约为基础宿主的三倍。进一步增加 PGK/GAPD 的 M9、M11、M12 也不优于对应基础组合。


![Figure 1 原文第 5 页](https://synbiopath.online/8ZTA7F52-Figure-1-complete.png)

*Figure 1：Figure1.ModulesupplyrelativeAcCoApoolAU notmeasuredflux;M10bestnotmonotonicgenecount.（原文 PDF 截图）。*


**解释：** 筛选支持“表达组合和负担需要协调”，不能推论每个供体通路基因都有单调正效应。Figure 1C 的纵轴为 Acetyl-CoA A.U.，只支持该检测框架内相对池水平。作者在行文中使用 productivity 等词，但这些柱形没有直接测定单位时间通量。表达负担、前体重新分配和生理状态改变是合理解释；没有同位素通量或代谢网络数据，就不把三倍池大小写成三倍通量。

### 2. 引入 DBAT：高供体宿主有更高比产物量，同时生长明显受损

**观察：** Figure 2A 中 8 h 的 R0/R7/R8/R10 OD600 分别约为 15.4/7.9/2.4/1.0。R0 在 16 h 达到约 25，而 R8、R10 到 48 h 才约为 11.8、11.1。Figure 2B 的 8 h 供体量分别为 0.9、2.5、2.4、2.3 mg/g DCW，所以 R10 在这一时间点并非最高；它的优势是后续供体维持和产物表现。24 h R10 的 baccatin III 达 101.6 μg/g DCW，这个数不能抄成 101.6 mg/g DCW 或 mg/L。PDF 文本层将 μ 映射为 m，原图与原文视觉核对均为 μg/g DCW；Figure 3C 的供体单位为 μg/mL，Figure 2B 则为 mg/g DCW。


![Figure 2 原文第 7 页](https://synbiopath.online/8ZTA7F52-Figure-2-complete.png)

*Figure 2：Figure2.BiomassAcCoAmgpergDCW baccatinugpergDCW DBATgelgrayAU;R10notmaxAcCoAat8h growthburden n3biorepsSD.（原文 PDF 截图）。*


**解释与限制：** R10 的高比产物量伴随低细胞量，说明不能仅凭单位干重产物判断最终体积滴度或经济性。Figure 2D 的 DBAT 灰度在 18 h 最高，后续仍可见表达，并不证明所有时段具有同一活性。Figure 2 的采样时间、不同面板归一化和 Figure 3 的体积滴度应分别记录。外加底物、不同宿主及产物结构证据支持 DBAT 转化成立，但培养时间与供体浓度之间的共变不足以单独证明供体是所有差异的唯一原因。

### 3. 时间追踪揭示反应倒退：乙酸同时改变前体和 pH

**观察：** Figure 3A 的优化组合在 24 h 达到 1.14 mg/mL，采用 1.5 mg/mL 10-DAB 与初始 OD600 40。另一个时间追踪实验中，产物 18 h 达约 1.3 mg/mL，48 h 降至 0.73 mg/mL；10-DAB 从最低 0.32 mg/mL 回升至 0.91 mg/mL，pH 从约 7.0 升至 8.8。该曲线是产物与底物互逆变化的直接观察，不能只截取早期峰值宣布全程稳定。


![Figure 3 原文第 8 页](https://synbiopath.online/8ZTA7F52-Figure-3-complete.png)

*Figure 3：Figure3.Substrateaxis mgmL caption gmL1000xconflict;aceticacid changesbothsupplyandpH;1.14/1.3/1.57differentendpoints n3biorepsSD.（原文 PDF 截图）。*


**乙酸效果：** 50 mmol/L 乙酸组供体水平更高，环境 pH 约在 5.7–7.8，18 h 产物达 1.54 mg/mL，最高约 1.57 mg/mL，并维持约十小时后仍有下降。乙酸既可能提供 acetyl-CoA 的碳源，又降低 pH，现有组合没有完全正交拆分这两种作用，因此“乙酸提高前体供应并缓解倒退”比“全由供体提升造成”更符合证据。酸、乙酸盐及等 pH 条件的充分匹配对照和完整通量分析尚缺。

**原文单位冲突：** Figure 3A 图注写 1.0、1.5、2.0 g/mL，而坐标轴及结果正文写 mg/mL；方法 2.5 的末句也有 g/mL 写法。两者相差千倍，本笔记按图轴及正文一致的 mg/mL 解释，同时保留冲突说明；不能将错误单位直接变成可执行条件。1.14、1.3 与 1.57 mg/mL 分属优化终点、无乙酸时间峰值和乙酸组峰值，不是同一个时间点的可互换重复结果。

### 4. DBAT 的逆向作用：空宿主、纯酶与匀浆提供不同层次证据

**观察：** Figure 4A 的 pH 6 缓冲液中 baccatin III 在 48 h 较稳定；pH 9 时缓慢减少并产生少量 10-DAB。空宿主 M0 不显著增强该过程，带 DBAT 的 R10 则产生明显逆转，12 h 的 10-DAB 浓度约为 baccatin III 两倍。Figure 4 区分碱性环境本身和工程宿主的附加效应，支持两者均需考虑。


![Figure 4 原文第 9 页](https://synbiopath.online/8ZTA7F52-Figure-4-complete.png)

*Figure 4：Figure4.AllfourconditionspH6/9bufferM0/R10;nonenzymaticandDBATlinkedreversenotallwaterhydrolysis.（原文 PDF 截图）。*


Figure 5A 的纯 DBAT 在碱性条件下也能产生少量 10-DAB；加入 M0 匀浆后更强，4 h 的 10-DAB 超过剩余 baccatin III。该比较支持 DBAT 可参与反向反应，且宿主组分会增强结果。Figure 5C 保留结构示意和原始 MS，而不是用文字替代鉴定图。


![Figure 5 原文第 10 页](https://synbiopath.online/8ZTA7F52-Figure-5-complete.png)

*Figure 5：Figure5.PureDBATplusM0homogenate chromatograms structuresMS reverseacetyltransferorhydrolysis proposedbranches.（原文 PDF 截图）。*


**证据边界：** 正文进一步报告水提组分有效、乙酸乙酯组分无效，水提组分中鉴定到 CoASH；CoASH、钾盐、两者联用使 10-DAB 分别约增加 20、6、50 倍。这些细分结果主要依赖 S5、S6，本次未取得 SI，属于作者报告而非本次看过的原始图。CoASH 可作为乙酰基受体，反向转移生成 acetyl-CoA；“去乙酰化”描述产物变化，不等于已经证明其唯一机理为水解。Figure 5C 同时画出 acetyl-CoA 或 CH3COOH，不能隐去机制分支。

钾盐组使用磷酸盐体系，同时可能改变离子强度、缓冲环境及阴离子；主文不足以排除这些因素，也没有展示全部离子匹配对照。联用 50 倍不是仅凭数值就能定义的统计学协同。C7 差向异构化是作者依据 SI 报告的现象，未读补充谱图不重新确证其结构或定量。

### 5. 补料培养：区分初始酸化、持续 pH 控制和分离回收

**规模与阶段：** 作者使用 3-L 反应器、初始 1-L 工作体积；培养、表达、产物转化分阶段。发酵末端读数为培养总时长 55 h，即生产阶段约 24 h，不将 55 h 当作全部底物转化时间。Figure 6 是完整发酵图，包含 A–G 和 DBAT 凝胶。结果 3.4 若干处误引用 Fig. 5，但实际对应 Figure 6，本笔记按图像内容定位并保留编号问题。


![Figure 6 原文第 11 页](https://synbiopath.online/8ZTA7F52-Figure-6-complete.png)

*Figure 6：Figure6.Allsevenpanelsgel included sourcebodymisrefsFig5;initialvsmaintainedpHdiffer;2/3/4.6gLnot98/97/78percentmolyield;3Lreactorinitial1L.（原文 PDF 截图）。*


**不同实验层次：** 加入 30、50、65 mmol/L 乙酸形成初始 pH 6.0、5.5、5.0 的三组，正文报告末端滴度为 1.2、1.6、0.4 g/L。另一组将 pH 持续保持 6.0、5.8、5.5，正文报告末端分别为 1.5、2.0、1.0 g/L；这组对应初始乙酸 30、35、50 mmol/L。初始 pH 5.5 的 1.6 g/L 不能与维持 pH 5.5 的 1.0 g/L 合并，也不能跨组把乙酸浓度和 pH 单独归因。原图另有冲突：Figure 6D 第三幅凝胶标签写 55 mmol/L，而 6C、6E 及正文写 65 mmol/L；Figure 6F 的 pH 5.5 柱高视觉约 1.2 g/L，正文则写 1.0 g/L。Figure 3A 最优柱高视觉约 1.0 mg/mL，正文报告 1.14 mg/mL。本笔记保留正文数值与图像差异，未取得原始点，不能自行决定哪一项是精确真值。

在持续 pH 5.8 的后续底物比较中，输入 2、3、6 g/L 10-DAB，分别得到 2、3、4.6 g/L baccatin III，作者定义的底物转化率分别为 98%、97%、78%。高底物组体积滴度最高，却有更低底物消失比例，故最佳选择取决于滴度、底物成本、反应时间及回收。不能因前两组产物与底物质量浓度数字相同就宣称定量摩尔收率。

**分离：** 作者从 3 g/L 输入组的发酵液提得 7.5 g 粗提物，柱层析得到 2.59 g baccatin III，HPLC 纯度 >98%。以作者报告的发酵液 HPLC 产物总量 3 g 为分母，2.59/3=86.33%，吻合约 86% 回收率；2.59/7.5=34.53% 只是粗提物中分离目标物的质量比例，不是该回收率。HPLC 峰面积纯度不直接等于称量纯度，补料后最终体积也未据此精确重建，不能用初始 1 L 自动推算所有批次最终产物总质量。

# 总体结论

本研究支持三条结论：PDH/PANK/ACS 的恰当组合能够提高供体池并改善 DBAT 全细胞转化；碱化会促进产物损失，其中 DBAT 与宿主组分参与了逆向过程；将供体补给和环境控制结合，可以在小型补料反应器中积累克每升级 baccatin III，并分离获得克级产物。该证据覆盖细胞筛选、时间曲线、逆向反应对照和产物分离，明显强于只报告某一时间点的色谱峰。

结论范围仍是外加 10-DAB 的乙酰化，不是从糖从头制造 baccatin III 或 paclitaxel。主文不能给出正反向催化的完整动力学、各环境因素的独立贡献，也不足以证明可直接工业应用或经济优势。作者当时“最高滴度”的历史陈述未用当前文献重新比较，不改写为当前纪录。

# 论文评价

**贡献。** 最有价值的是把产物下降解释为需要验证的反应网络问题：既测供体，也观察底物回升，还通过纯酶与空宿主拆分逆向因素。对天然产物生物转化的启示是，末端修饰的净产物量由生成、逆反应、化学稳定性和生长共同决定，供体池并非唯一优化指标。

**限制。** 供体池与通量、生物量归一化与体积产量、底物消失与产物摩尔收率需要严格区分。多个图注明示 SD，但缺少全面的统计检验和原始点；SI 缺失限制 CoASH/钾效应、异构体及 NMR 的独立核验。酶表达强度不能代替酶活。原文单位、图号和菌株命名也有容易传播的错误，须在复用笔记时保留勘误说明。

**后续研究意义。** 若研究目标是解释反应方向，关键应是匹配 pH 与供体/受体条件，分别计量底物、目标产物及异构体，而非只测底物消失；若目标是比较细胞工厂性能，应同时保留体积滴度、干重比产量、净生产速率和回收率。这样的比较需要完整原始数据与 SI，不能凭正文柱形补造数值。作者提出降低诱导成本和染色体整合是未来方向，本研究并未完成这些验证。

**利益与支持。** 作者声明无利益冲突。资助包括国家重点研发计划 2018YFA0901900、2020YFA0908003，重大新药创制 2018ZX09711001-006-001，NSFC 81573325，CAMS 2017-I2M-2-004、2019-I2M-1-005，PUMC 201920100801；这些来自正文致谢，不用于提升科学结论强度。

# 关键问题及回答

**问题 1：是否已经实现紫杉醇从头合成？**

没有。需要外加 10-DAB，得到的是 baccatin III；供体部分由宿主代谢供应。复杂骨架和紫杉醇侧链并未在该工作中从头合成。

**问题 2：为什么增加供体基因不一定有利？**

Figure 1 的不同组合出现下降，Figure 2 显示明显生长负担。数据支持寻找平衡，作者关于代谢重分配的解释尚不能替代通量测定；M10 的优势也不等于每个基因的独立贡献已分离。

**问题 3：97% 转化率与 3 g/L 是否说明 97% 摩尔产物收率？**

不能。97% 根据 10-DAB 峰面积消失计算，3 g/L 是产物质量浓度。目标产物收率需要相应摩尔量和物料平衡，不能把底物消失自动归为目标产品。

**问题 4：乙酸作用是否只在提高 acetyl-CoA？**

不是。它同时改变前体供应和 pH，产物稳定性及 DBAT 逆向作用也受环境影响。当前实验支持耦合效应，未充分分离各项贡献，更未证明乙酸在任何条件下都会增产。

**问题 5：哪些数字容易误用？**

101.6 的单位是 μg/g DCW，Figure 3 图注的 g/mL 与图轴 mg/mL 冲突，Figure 6 的发酵结果在正文被误引为 Figure 5。86% 由 2.59 g 分离产物除以约 3 g 发酵液目标物得到，不能除以 7.5 g 粗提物。主文全部图表已保留，SI 未取得仍标为未独立复核。

> 分类状态：待全部文献笔记完成后统一分类归档。
