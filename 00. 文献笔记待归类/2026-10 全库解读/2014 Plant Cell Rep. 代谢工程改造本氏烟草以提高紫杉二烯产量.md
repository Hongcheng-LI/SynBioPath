---
type: literature-reading
zotero_key: DIETLRIU
doi: "10.1007/s00299-014-1568-9"
paper_type: research
classification_status: pending
reading_status: main-text-and-figures-read
review_status: codex-source-checked
human_full_paper_review: false
source_attachment: 2IAR3HBN
source_sha256: 1d936974f2096d32c4cc91693c387b1ad65c7e941a78a21f2c43d4cd954a4d4a
created: 2026-10-10
---

> 原文来源：[Zotero 条目](zotero://select/library/items/DIETLRIU)；[DOI](https://doi.org/10.1007/s00299-014-1568-9)；由当前 Codex 读取原始主文并核对图表，尚未经人工逐项复核。 来源限制：Fig. 4 与 Fig. 6 中以小写字母（a、ab、bc、c 或 a、b、c、d）标注差异，但原文未注明所用统计检验方法；不能断言为 Tukey HSD 或 Duncan 多重比较中任一种；本研究未直接测定 PSY / PDS 沉默后 GGPP 池的绝对浓度变化，亦未测定下游类胡萝卜素中间体（八氢番茄红素、ζ-胡萝卜素等）的水平，故'通量重定向'是基于 PSY / PDS 已知生化功能的合理推论，并非代谢组学定量证据；原文中关于 TS 导入造成的'赤霉素缺乏性矮化'解释以推论形式提出（'suggesting that the newly introduced TS gene interferes with the biosynthesis of gibberellins possibly by reducing the pool of available GGPP'），本研究未直接测定赤霉素或叶绿素含量，原文亦未给出补充验证数据（'data not shown'）；Fig. 2 仅做了转化植株中 TS 转录本的存在 / 缺失定性判断，未对不同转化系 TS 表达水平做半定量灰度分析或 qPCR 量化；无内参基因共扩增对照；Fig. 3 紫杉二烯的鉴定仅依靠保留时间（13.09 min）与质谱图谱比对，原文未提供 NMR 或共注标准品的完整结构证实；Fig. 6 中 TRV:GFP 对照本身已大幅压低紫杉二烯产量，原文亦确认'VIGS vector itself significantly reduced the production of taxadiene'，故 PSY 沉默组的'净'提升部分需注意解读；论文正文未提供 Supporting Information 附件，故无 SI 数据；Table 1 之后的延伸表格、原始凝胶图或色谱原始数据均未出现；Fig. 1 右下角 Paclitaxel (Taxol) 完整母核结构仅作为紫杉醇途径的远端目标示意，并非本研究实际产物；Fig. 5 中 PSY/PDS VIGS 构造载体片段长度（PSY 198 bp；PDS 369 bp）在 Table 1 与正文一致，但 Fig. 5c/d 中的相对沉默程度无定量条形图，仅可定性比较；为保留全部图版与图注，截图采用原文整页。

# 一、基本信息

**文章题目**：Metabolic engineering of *Nicotiana benthamiana* for the increased production of taxadiene（代谢工程改造本氏烟草以提高紫杉二烯产量）

**文章 DOI 号**：10.1007/s00299-014-1568-9

**期刊名称**：Plant Cell Reports

**通讯作者及工作单位**：

- **Kwang-Hyun Baek**：韩国岭南大学校生物技术学院（School of Biotechnology, Yeungnam University, Gyeongbuk 712-749, Korea），邮箱 khbaek@ynu.ac.kr。

合作单位：韩国 KRIBB 植物系统工程研究中心（Plant System Engineering Research Center, 125 Gwahangno, Daejeon）；韩国基础科学研究院大邱分院分析研究部（Daegu Center, Korea Basic Science Institute）；韩国中央大学食品营养系（Department of Food and Nutrition, Chung-Ang University）；韩国 Samyang Genexbio 公司。作者团队另特别致谢华盛顿州立大学 Rodney Croteau 博士惠赠 TS 基因（pBluescript SK(−) 模板）。

**收稿日期 / 修订日期 / 接收日期 / 上线日期**：2013-10-08 / 2014-01-08 / 2014-01-09 / 2014-01-25。

**致谢资助**：韩国农村振兴厅下一代生物绿色 21 项目（Next-Generation BioGreen 21 Program, PJ00950603）。

# 二、研究背景

紫杉醇（paclitaxel，商品名 Taxol®）是从太平洋红豆杉（*Taxus brevifolia*）树皮中分离的二萜类天然产物，1971 年由 Wani 等首次报道化学结构，1982 年获 FDA 批准上市。该化合物通过诱导微管蛋白聚合并抑制解聚发挥抗癌活性（Kumar 1981; Parness and Horwitz 1981; Ahn et al. 2010），已用于难治性卵巢癌、转移性乳腺癌、肺癌、艾滋病相关卡波西肉瘤等不同类型癌症，并对部分肾脏衰竭、类风湿性关节炎及再狭窄显示出疗效（Charles et al. 2001; Hata et al. 2004; Francis et al. 1995; Gill et al. 1999; Arsenaulta et al. 1998; Heldman et al. 2001; Woo et al. 1994）。紫杉醇的生物合成主要分为三步：GGPP 前体合成、GGPP 环化为紫杉烷骨架核心（taxadiene）、然后经多步氧化与酰化形成紫杉醇（Fig. 1）。紫杉二烯（taxadiene，taxa-4(5),11(12)-diene）是紫杉醇生物合成中第一个被限定的二萜中间体，从红豆杉树皮中含量极低（Koepp et al. 1995），由紫杉烷二烯合成酶（taxadiene synthase, TS）从共同前体香叶基香叶基焦磷酸（geranylgeranyl diphosphate, GGPP）环化生成（Koepp et al. 1995; Hezari et al. 1995; Wildung & Croteau 1996）。

TS 基因已先后从 *T. brevifolia*、*T. cuspidata* Sieb. Et Zucc. 和 *T. chinensis* 中克隆成功，并在 *Escherichia coli* 中获得功能性表达（Wang et al. 2002）。围绕紫杉醇代谢工程瓶颈即首步紫杉二烯生产，TS 已被导入 *E. coli* 与 *Saccharomyces cerevisiae*（Ajikumar et al. 2010; Boghigian et al. 2012; DeJong et al. 2006; Huang et al. 2001），以及多种植物底盘如拟南芥（Besumbes et al. 2004）、苔藓（Anterola et al. 2009）、番茄（Kovacs et al. 2007）和人参发根（Cha et al. 2012）。红豆杉生长缓慢且树皮紫杉醇含量仅约 0.01%（Vidensek et al. 1990），全合成因复杂性与高成本难以规模化（Danishefsky et al. 1996; Nicolaou et al. 1994; Cragg et al. 1993）；细胞悬浮培养亦存在稳定性差、放大困难等问题（Brunakova et al. 2005; Cusidó et al. 2002; Hara et al. 2008; Srinivasan et al. 1995; Tabata 2006; Exposito et al. 2009; Kajani et al. 2012; Onrubia et al. 2013）。红豆杉毛状根（Kim et al. 2009）与内生真菌（*Taxomyces andreanae*、*Taxodium distichum*、*Corylus* sp.）虽可产生紫杉醇，但产量过低（Li et al. 1996; Stierle et al. 1993）。以 10-deacetylbaccatin III 为前体的半合成方法（Castor & Theodore 1993）已被有限使用。

本氏烟草（*Nicotiana benthamiana*）是茄科中与 *N. tabacum* 亲缘关系较近的快速生长模式植物，具有农杆菌转化与病毒诱导基因沉默（virus-induced gene silencing, VIGS）操作成熟、生物量大等优势，但此前尚无 TS 转基因本氏烟草合成紫杉二烯的报道。本研究将 *T. cuspidata* 来源的 TS 编码区导入本氏烟草，以 CaMV 35S 启动子驱动组成型表达，并通过 GC-MS 确证紫杉二烯的从头合成，进一步评估甲基茉莉酸甲酯（methyl jasmonate, MJ）诱发子和通过沉默 PSY/PDS 阻断类胡萝卜素支路两类产量提升策略。

# 三、研究思路

本研究沿"基因克隆—异源转化—分子鉴定—代谢物确证—纯合筛选—诱发子处理—通量重定向"的逻辑链展开：(1) 构建 CaMV 35S::TS 表达载体（TSS），将 *T. cuspidata* 来源的 TS 编码区亚克隆至 pCAMBIA2300 衍生载体 23001；(2) 通过农杆菌叶盘法转化本氏烟草，经卡那霉素—头孢噻肟筛选获得转化系；(3) 通过 RT-PCR 在转录水平确证 TS 整合，再以 GC-MS 检测 13.09 min 处紫杉二烯特征峰并以质谱比对验证代谢物身份；(4) 通过 qPCR 与卡那霉素平板发芽率筛选 T1 纯合系并量化比较各系产量；(5) 在产量最高的 TSS-8 纯合系上分别施加 100 μM MJ 诱发子（两次叶面喷施）和 TRV 系统介导的 PSY / PDS VIGS 沉默，定量比较两类策略的提升效果；(6) 与苔藓、拟南芥、人参发根、普通番茄、黄色果肉番茄等其他底盘的产量做横向比较并形成方法学归纳。

# 四、研究方法

- **TSS 载体构建**：以 BamH I 和 Kpn I 双酶切将 TS 编码区从 pBluescript SK(−) 亚克隆入 pCAMBIA2300 衍生载体 23001（KRIBB 提供），CaMV 35S 启动子驱动（按 Cha et al. 2012 方法）。冻融法（Holsters et al. 1978; Hood et al. 1993）转化入 KM(S) *Agrobacterium tumefaciens* EHA105，以 TS 特异引物 TS5M/TS3M 做菌落 PCR 验证。
- **农杆菌叶盘法转化**：1 月龄无菌本氏烟草叶切成约 0.5 cm² 小块（去叶脉），MS + 3% 蔗糖 + 0.1 mg/L NAA + 1 mg/L BAP + 0.8% 植物琼脂预培养 24 h。农杆菌在 YEP + 50 mg/L 卡那霉素中过夜培养（28 °C、120 rpm），离心重悬于 10 mM MES + MgCl₂ 至 OD600 = 0.5，加入 100 μM 乙酰丁香酮预诱导 4 h（22 °C），叶块浸入悬浊液 15 min 完成侵染。
- **选择与再生**：侵染后叶块在共培养基（覆盖无菌 Whatman 滤纸）暗培养 3 天（25 °C）；转入再生培养基（含 100 mg/L 头孢噻肟和 50 mg/L 卡那霉素）以 2 周间隔继代；愈伤组织转入生根培养基（1% 蔗糖 + 50 mg/L 卡那霉素 + 0.1 mg/L NAA + 0.8% 植物琼脂）；1 月后移入温室土壤。
- **分子鉴定与纯合筛选**：一站式 RT-PCR（XP Thermal Cycler, BIOER）以 TS5D/TS3D 引物检测转化植株 TS 转录（逆转录 45 °C × 45 min；PCR 35 个循环：94 °C 30 s / 50 °C 40 s / 72 °C 1.5 min；72 °C 终延伸 5 min）；产物以 1.2% 琼脂糖电泳检测。T1 种子在含 50 mg/L 卡那霉素的 MS 上发芽后以 TSqF/TSqR 引物做 qPCR（35 个循环：95 °C 15 s / 52 °C 40 s / 72 °C 40 s；Rotor-Gene 600），筛选纯合系后再以 100% 卡那霉素发芽率二次确认。
- **MJ 处理**：3 周龄 T1 转化植株以 100 μM MJ + 0.05% Tween-80 叶面喷施两次（每株 40 mL），间隔 1 周，第二次喷施后 15 天采收叶片。
- **VIGS**：依据 *N. tabacum* PSY（NCBI 登录号 JX101475）和 PDS（NCBI 登录号 AJ616742）序列，用 PhytoSF/PhytoSR（PSY 含 EcoR I + Xho I 接头）和 PhytoDSF/PhytoDSR（PDS 含 Xba I + BamH I 接头）分别扩增 PSY 198 bp 与 PDS 369 bp 片段，酶切后克隆入 pTRV2；冻融法（Chung et al. 2004; Liu et al. 2002）转化 *A. tumefaciens* GV2260；与 pTRV1 农杆菌按 1:1 混合后注射入 18 天龄四叶期本氏烟草下层叶；以 TRV:GFP 为非靶对照；23 °C，16 h 光 / 8 h 暗培养。
- **半定量 RT-PCR**：取 VIGS 后 4 周叶组织，以 TRI Reagent 抽提总 RNA；以 OptiScript™ One-step RT-PCR Kit 做 RT-PCR；PSY 上游（PsyF1/R1）、下游（PsyF2/R2），PDS 上游（PdsF1/R1）、下游（PdsF2/R2）各 25 个循环（95 °C 30 s / 50 °C 40 s / 72 °C 40 s；72 °C 终延伸 5 min）；1.2% 琼脂糖电泳。
- **紫杉二烯提取与 GC-MS 定量**：0.5 g 冻干叶粉加 5 mL 含 20 μg/mL 十九烷（nonadecane）内标的己烷超声 20 min（40 kHz）；棉塞过滤后残渣再以等体积己烷重复提取 4 次；合并有机相 N₂ 吹干；1 mL 己烷复溶；Agilent 6890N GC + JMS 700 MS（韩国基础科学研究院大邱分院），DB-5 柱（30 m × 0.25 mm × 0.25 μm），10:1 分流进样（进样口 280 °C），程序升温 120 °C 维持 2 min → 以 10 °C/min 升至 250 °C 维持 5 min，氦气载气；以十九烷为内标定量。

Table 1 列出本文所涉及的全部引物（TSClonF/R 用于 TS 编码区克隆，TS5M/3M 用于农杆菌验证，TS5D/3D 用于本氏烟草转化验证，TSqF/R 用于 qPCR 纯合筛选；PhytoSF/R 与 PhytoDSF/R 分别用于 PSY/PDS VIGS 构造；PsyF1/R1、PsyF2/R2、PdsF1/R1、PdsF2/R2 分别用于 PSY/PDS 上下游沉默效率检测），限制性内切酶位点以斜体并加下划线标示。
![Table 1 原文第 4 页](https://synbiopath.online/DIETLRIU-Table-1-p4-1-ef01566c5eeee202.png)

*Table 1：Table 1 Primers for construction of N. benthamiana transformed with the TS gene and for virus-induced gene silencing of the PSY and PDS gene in TS-transformed N. benthamiana（包含 TS、PSY、PDS 三组引物的基因、引物名、序列 5′–3′ 与用途，限制性内切酶位点以斜体加下划线标出）（原文 PDF 截图）。*


# 五、实验设计及结果分析

### (一) TSS 表达载体构建与本氏烟草转化

#### 实验目的与设计逻辑

为实现紫杉二烯在本氏烟草中的异源合成，作者将 *T. cuspidata* 来源 TS 编码区置于 CaMV 35S 启动子下游，构建 pCAMBIA2300 衍生载体 TSS。本氏烟草作为异源宿主的优势为生长迅速、农杆菌转化与 VIGS 操作成熟，但此前尚无 TS 转基因本氏烟草合成紫杉二烯的报道。

#### 实验结果与证据解析

通过双酶切、连接、转化 E. coli DH5α 和冻融法转入 EHA105，最终获得 TSS 重组载体并经农杆菌菌落 PCR 验证成功。
![Figure 1 原文第 3 页](https://synbiopath.online/DIETLRIU-Figure-1-p3-a0eebeabd225406c.png)

*Figure 1：Fig. 1 Taxadiene [Taxa-4(5),11(12)-diene] or carotenoids biosynthesis from the precursor GGPP（原图：上方为 GGPP 经紫杉二烯合成酶 TS 进入 taxadiene [Taxa-4(5), 11(12)-diene] 骨架（四环二萜结构），并以箭头延伸到右下角 Paclitaxel (Taxol) 完整母核结构；下方为 PSY / PDS 进入类胡萝卜素支路）（原文 PDF 截图）。*
 Fig. 1 系统描绘了从共同前体 GGPP 出发的两条代谢分支：上支由 TS 环化为 taxadiene，并经多步氧化酰化延伸至图右下角 Paclitaxel (Taxol) 完整母核结构（含含氧 / 含氮取代基的四环二萜框架）；下支由 PSY（phytoene synthase，催化 GGPP → phytoene 的类胡萝卜素途径第一限速步骤）与 PDS（phytoene desaturase，催化 phytoene → ζ-carotene 的第二步）进入类胡萝卜素途径。该图既是后续 PSY / PDS VIGS 通量重定向实验的设计基础，也是本文核心假设"抑制类胡萝卜素支路可使更多 GGPP 流向紫杉二烯分支"的视觉化呈现。需要明确说明，图右下角的 Paclitaxel (Taxol) 完整结构仅是紫杉醇远端代谢目标的示意，并非本研究的实际产物；本研究最终代谢物为紫杉二烯。

农杆菌叶盘法侵染共得到约 200 个愈伤组织，后续移植得到 110 株独立转化系；经 RT-PCR 整合验证后，最终判定 14 株成功整合 TS 基因（详见下节）。

### (二) 转基因系中 TS 基因整合的分子鉴定

#### 实验目的与设计逻辑

再生得到的 110 株转化系并非全部整合并表达 TS 基因，需要在转录水平确认阳性个体后方可推进到代谢物检测阶段。

#### 实验结果与证据解析


![Figure 2 原文第 6 页](https://synbiopath.online/DIETLRIU-Figure-2-p6-1-95a8c4be8211dda4.png)

*Figure 2：Fig. 2 Selection of N. benthamiana plants expressing the taxadiene synthase (TS) gene. RT-PCR was performed using total RNA. Lane 1: 1 kb + DNA marker, Lanes 2–14: N. benthamiana plants transformed with the TS gene, Lane 15: N. benthamiana plants transformed with the empty 23001 vector and Lane 16: TSS vector plasmid as the positive control（原文 PDF 截图）。*
 Fig. 2 为 1.2% 琼脂糖凝胶电泳图：最左侧 M 标记为 1 kb + DNA marker，编号 1–14 为 *N. benthamiana* 独立转化植株，NC 为转化空载体 23001 的阴性对照，PC 为 TSS 质粒阳性对照；箭头标示 579 bp 处为 TS 扩增产物。该图作为整合验证的定性证据支撑 14 株阳性转化系的判定（原文："the survived 14 transformed plants indicated the successful integration of the TS gene (Fig. 2)"）；但作者未对各泳道条带进行半定量灰度分析，亦未显示内参对照（如看家基因共扩增），因此不同转化系中 TS 表达量是否一致仍为缺口（图-文层面）。

### (三) 紫杉二烯从头合成的 GC-MS 确证

#### 实验目的与设计逻辑

转录水平证实整合只是前提，需要在代谢物水平检验 TS 是否真正催化了 GGPP 到紫杉二烯的环化。

#### 实验结果与证据解析

取 14 株 T0 转化系和野生型本氏烟草叶片的己烷粗提物进行 GC-MS 分析。
![Figure 3 原文第 6 页](https://synbiopath.online/DIETLRIU-Figure-3-p6-1-9572305cea8a11a2.png)

*Figure 3：Fig. 3 Measurement of taxadiene by gas chromatography/mass spectroscopy. a Crude hexane extracts from leaves of non-transformed wild-type N. benthamiana not showing any peak corresponding to taxadiene, b peak at 13.09 min in the gas chromatograph indicating the de novo production of taxadiene in correspondence with taxadiene in the taxadiene synthase transformed N. benthamiana, and c mass spectra profile matched exactly the taxadiene mass spectra profile（原文 PDF 截图）。*
 Fig. 3 包含三个子图：

- (a) 野生型本氏烟草色谱图（横轴 10–15 min），在 11–15 min 区间无对应峰；
- (b) 一株代表性转化系在保留时间 13.09 min 处出现特征峰（图中以 * 标记，与紫杉二烯标准品保留时间一致）；
- (c) 该 13.09 min 峰的质谱图（横轴 m/z 40–360；图面标注的主要碎片离子包括 41、55、79、81、95、107、122、133、161、174、187、215、229、257、272 等），与文献报道的紫杉二烯质谱图谱相匹配。

通过上述三重标准（保留时间一致、目标峰仅出现于转化系、质谱图谱与文献一致），作者在 14 株转化系中鉴定出 7 株（TSS-2、3、5、6、7、8、10）从头合成紫杉二烯，并报告"producing 4–18 µg taxadiene per gram of dried leaves (Fig. 4)"。该证据类型为代谢物直接检测 + 标准品质谱比对，已足以证实 TS 基因在本氏烟草中驱动紫杉二烯合成的充分性；但 GC-MS 鉴定仅依靠保留时间与质谱图谱比对，原文未提供 NMR 或共注标准品的完整结构证实；对已知化合物而言，这一证据水平在植物代谢物组学中已被广泛接受。

### (四) T1 纯合系筛选及紫杉二烯积累量比较

#### 实验目的与设计逻辑

T0 代为杂合转化系，后代分离将使代谢物定量复杂化。挑选 T0 中产量最高的四个系自交，结合 qPCR 与卡那霉素平板筛选 T1 纯合系，可为后续诱发子和 VIGS 实验提供遗传稳定的材料基础。

#### 实验结果与证据解析

对 T0 代中产量最高的四个系（TSS-5、TSS-7、TSS-8、TSS-10）自交，T1 种子在含 50 mg/L 卡那霉素的 MS 上发芽后以 qPCR 扩增 216 bp TS 片段筛选，再以 100% 卡那霉素发芽率二次确认纯合性。
![Figure 4 原文第 7 页](https://synbiopath.online/DIETLRIU-Figure-4-p7-1-58f1aeafb2db2a5e.png)

*Figure 4：Fig. 4 Accumulation of taxadiene in the leaves of the transformed N. benthamiana T0 plants and the homozygous T1 lines. The vertical bars represent mean ± standard deviations (n = 3)（原文 PDF 截图）。*
 Fig. 4 为 T0 代（左半部分）与 T1 纯合系（右半部分）叶中紫杉二烯积累柱状图，纵坐标 Amount of taxadiene (μg/g dw)，数据表示为 mean ± SD (n = 3)，以小写字母（a、ab、b 等）标注差异显著性。

**T0 栏柱状图**（左半部分）从左至右共含 **8 根柱**：野生型 Control + 7 株 GC-MS 阳性系（TSS-2、TSS-3、TSS-5、TSS-6、TSS-7、TSS-8、TSS-10），柱高均落在 4–18 μg/g dw 范围内，与正文"producing 4–18 µg taxadiene per gram of dried leaves"及"seven independent T0 transformed lines, TSS-2, 3, 5, 6, 7, 8, and 10"完全对应；Control 柱显著高于所有转化系柱（标记 a），各转化系柱之间标记为 ab 或 b 等。

**T1 纯合系栏**（右半部分）共含 4 根柱（TSS-5、TSS-7、TSS-8、TSS-10）：TSS-5、TSS-7、TSS-8、TSS-10 的具体产量依次为 **22、13、27 和 11 μg taxadiene/g dw**（原文："the TSS-5, 7, 8, and 10 homogene lines accumulated 22, 13, 27, and 11 μg taxadiene per gram of dried leaves, respectively (Fig. 4)"）；其中 TSS-8 以 27 μg/g dw 居首，成为后续诱发子（MJ）与 VIGS 实验的核心对象。Fig. 4 的 T0 与 T1 数据无图-文不一致。

**统计说明**：原图以小写字母（a、ab、b、bc、c 等）标注差异，但未明示所用统计检验方法；该缺口已在 source_gaps 中明确标注，不作推断。

### (五) 通过 MJ 诱发子处理提高紫杉二烯积累

#### 实验目的与设计逻辑

TS 表达并催化紫杉二烯合成后，下一步利用已知二萜诱发子 MJ 进一步提升产量。MJ 在多个物种中曾显示上调二萜生物合成的功能（Besumbes et al. 2004; Kim et al. 2009），Cha et al. (2012) 在人参发根中报告 50 μM MJ 处理使紫杉二烯提升 1.6 倍。

#### 实验结果与证据解析

以 100 μM MJ + 0.05% Tween-80 对 3 周龄 TSS-8 T1 纯合系叶面喷施两次（间隔 1 周），第二次喷施后 15 天采收。
![Figure 6 原文第 8 页](https://synbiopath.online/DIETLRIU-Figure-6-p8-1-835f8b31ee5d042c.png)

*Figure 6：Fig. 6 Effect of methyl jasmonate (MJ) spray or metabolic pathway shunting by virus-induced gene silencing of the PSY and PDS gene on the accumulation of taxadiene in the leaves of the TS-transformed N. benthamiana TSS-8 line. The vertical bars represent mean ± standard deviations (n = 3)（原文 PDF 截图）。*
 Fig. 6 显示：MJ 处理柱将紫杉二烯从对照 TSS-8 的 25 μg/g dw 提升至 35 μg/g dw，相当于 1.4 倍升高，与对照柱显著不同。该结果支持 MJ 在本氏烟草中作为二萜诱发子的有效性，但效应幅度低于人参发根中报告的 1.6 倍提升。作者推断 MJ 的正向效应主要来源于其诱导二萜合成途径调控因子（包括 TS 自身）表达上调，但该解释尚未由独立的转录组数据直接验证。

### (六) 通过 VIGS 沉默 PSY 和 PDS 实现代谢通量重定向

#### 实验目的与设计逻辑

紫杉二烯与类胡萝卜素共享前体 GGPP。理论上，抑制类胡萝卜素途径可使更多 GGPP 流向紫杉二烯分支。PSY 作为类胡萝卜素途径的"第一限速步骤"（GGPP → phytoene），PDS 作为下游第二步（phytoene → ζ-carotene），二者在 Fig. 1 中明确标出。作者以 PSY / PDS 两个连续步骤同时沉默，比较位点选择效应。

#### 实验结果与证据解析

构建 pTRV2:PSY（198 bp 片段）和 pTRV2:PDS（369 bp 片段）VIGS 载体，冻融法转化 *A. tumefaciens* GV2260；与 pTRV1 农杆菌按 1:1 混合后浸润 TSS-8 植株下层叶；TRV:GFP 为非靶对照。
![Figure 5 原文第 8 页](https://synbiopath.online/DIETLRIU-Figure-5-p8-1-c436090e7c95638d.png)

*Figure 5：Fig. 5 Virus-induced gene silencing of PSY and PDS genes in the TS- transformed N. benthamiana TSS-8 line. a Location of the primers used for the VIGS construct for the PSY gene (198 bp) and detection of silencing of the PSY gene. b Location of the primers used for the VIGS construct for the PDS gene (369 bp) and for detection of silencing of the PDS gene. Semiquantitative RT-PCR confirmed silencing of the c PSY gene and d PDS gene using two primer sets for detection of gene expression from both the upstream and downstream region of the VIGS construct, respectively. e Phenotypes of N. benthamiana TSS-8 line non-silenced or silenced with GFP, PSY, and PDS gene, respectively（原文 PDF 截图）。*
 Fig. 5 包含五个子图：
- (a) PSY 基因 VIGS construct 模式图：标出 VIGS construct 位置（198 bp）、PsyF1/PsyR1（上游）引物与 PsyF2/PsyR2（下游）引物对；
- (b) PDS 基因 VIGS construct 模式图：标出 VIGS construct 位置（369 bp）、PdsF1/PdsR1（上游）与 PdsF2/PdsR2（下游）引物对；
- (c) 半定量 RT-PCR：TRV:GFP vs TRV:PSY 处理样本中 PsyF1/R1 与 PsyF2/R2 两对引物均显示 TRV:PSY 表达显著降低或几乎不可检测；底部 rRNA 内参条带在 TRV:GFP 与 TRV:PSY 两泳道均清晰可见且强度相近；
- (d) 半定量 RT-PCR：TRV:GFP vs TRV:PDS 处理样本中 PdsF1/R1 与 PdsF2/R2 两对引物均显示 TRV:PDS 表达显著降低或几乎不可检测；底部 rRNA 内参条带在 TRV:GFP 与 TRV:PDS 两泳道同样清晰可见且强度相近；
- (e) 植物表型照片（自左向右）：TSS-8（深绿色对照）、TRV:GFP（深绿色对照）、TRV:PSY（黄绿色，PSY 缺失相关色素合成受阻）、TRV:PDS（白化，PDS 缺失相关）；PSY 与 PDS 沉默植株均伴有一定程度的生长减缓。原文描述为"PSY-silenced plants showed a yellowish-green phenotype, whereas PDS-silenced plants showed bleached leaves (Fig. 5e). Both the PSY- and PDS-silenced plants showed reduced growth relative to the wild-type and TSS-8 line (Fig. 5e). MJ-treated plants showed yellowish leaves with reduced growth (Fig. 5e)."

Fig. 6 进一步给出通量重定向后的紫杉二烯积累量（横坐标依次为 TSS-8、MJ、TRV:GFP、TRV:PSY、TRV:PDS，纵坐标 Amount of taxadiene (μg/g dw)，以平均 ± SD (n = 3) 标示，柱顶字母 a、b、c、d、e 标注差异显著性，具体字母对应以原图为准）：
- TSS-8 对照：25 μg/g dw；
- MJ 处理：35 μg/g dw；
- TRV:GFP：显著低于未处理 TSS-8 对照（柱顶标注差异显著性字母，具体对应需以原图为准）；
- TRV:PSY：**48 μg/g dw**，相对 TSS-8 对照升高 93.58%（原文："accumulation of 48 μg taxadiene/g of dried leaves, which was 93.58 % higher than the control TSS-8 line"）；
- TRV:PDS：相对 TSS-8 对照降低 47.59%。

作者据此提出"PSY 是本氏烟草中最适于提高紫杉二烯合成的截流靶点"。同时作者明确承认"the VIGS vector itself significantly reduced the production of taxadiene due to a metabolic effect like interruption in the newly formed taxadiene synthesis pathway or any other unknown reasons"——即 TRV:GFP 对照本身的产量被明显压低，构成本研究的一个关键混杂因素。

**未充分验证的环节**：(1) 本研究使用瞬时 VIGS 而非稳定的 T-DNA 插入或 CRISPR 敲除，无法排除病毒载体本身对植株代谢的副作用；(2) 未直接测定 PSY / PDS 沉默后 GGPP 池的绝对量化变化，故"通量重定向"是基于间接推论而非直接代谢组证据；(3) PDS 沉默降低产量的反直觉现象，作者未提供深入机制解释，仅以"unknown reasons"一笔带过。读者层面可推测 PDS 沉默可能因下游中间体（八氢番茄红素 / ζ-胡萝卜素）累积引起的反馈抑制、毒性反应或对光合作用/生长抑制的次级效应，导致紫杉二烯合成被间接压制。

# 六、总体结论

本研究通过农杆菌介导转化将 *T. cuspidata* 来源的 TS 基因导入本氏烟草，**首次以 GC-MS 在代谢物水平确证了紫杉二烯在本氏烟草中的从头生物合成**。T1 纯合系 TSS-5、TSS-7、TSS-8、TSS-10 各自积累 22、13、27 和 11 μg taxadiene/g dw，其中 TSS-8（27 μg/g dw）为对照基线。后续分别施加 MJ 诱发子和 PSY VIGS 沉默实现 1.4 倍（35 vs 25 μg/g dw）和 1.9 倍（48 vs 25 μg/g dw，即 93.58% 升高）的额外提升；PDS VIGS 沉默反而使产量下降 47.59%。本研究建立了"异源单基因表达 + 诱发子处理 + 代谢通量重定向"的多层产量提升策略，并通过与苔藓（5 μg/g dw）、拟南芥（0.6 μg/g dw）、人参发根（9.6 μg/g dw）、普通番茄（20 μg/g dw）和 TS-transgenic yellow flesh tomato（160 μg/g dw）的横向产量比较，提出**茄科植物（特别是烟草属）是目前异源紫杉二烯生产最有效的底盘之一**，为后续紫杉醇途径完整重构提供了优先候选系统（作者原文："the Solanaceae family is currently the best option for taxadiene metabolic engineering and future paclitaxel production"）。

# 七、论文评价

### 优点

本研究的核心创新在于将紫杉二烯生产从已尝试过的微生物与少数植物宿主扩展到本氏烟草这一未验证的茄科模式植物，**首次在 N. benthamiana 中证实 TS 单基因驱动的紫杉二烯从头合成**。论文在实验闭环上具有较好的合理性：作者通过 RT-PCR 在转录水平证实 TS 整合（Fig. 2），通过 GC-MS 在代谢物水平确证紫杉二烯的产生（Fig. 3），通过 T1 纯合系筛选获得遗传稳定材料（Fig. 4），并以独立的 MJ 处理和 PSY/PDS VIGS 两个分支策略同步验证可调控性（Fig. 5、Fig. 6）。在产量层面，TSS-8 纯合系 27 μg/g dw 高于此前在拟南芥、苔藓、人参发根与普通番茄中报告的水平，但低于 TS-transgenic yellow flesh tomato（160 μg/g dw）；后者的优势常被解释为其 PSY 缺失造成 GGPP 至类胡萝卜素的通量被截断，使更多 GGPP 流向紫杉二烯分支，这恰与本研究中 PSY VIGS 沉默所观察的提升效应在概念上一致，但本研究未对二者之间的产量差异（48 vs 160 μg/g dw）提供机制性解释。对 PDS 沉默降低产量的反直觉现象，作者保持谨慎解读态度（归因于"unknown reasons"），未过度推测，体现良好的证据克制。

### 缺点与缺口

1. **统计检验方法未明示**：Fig. 4 与 Fig. 6 的字母标记差异（a/ab/b/bc/c 或 a/b/c/d/e）所采用的统计检验方法在原文中未明确说明；属 source_gaps，不作推断。
2. **rRNA 内参可见性**：Fig. 5c、d 底部 rRNA 内参条带在 TRV:GFP 与 TRV:PSY（或 TRV:PDS）两泳道均清晰可见且强度相近，可作为上样量对照；但未做灰度归一化定量，仅可定性比较沉默效率。
3. **TS 表达水平未做定量比较**：Fig. 2 仅对转化植株 TS 转录做了存在/缺失的定性判断，未对不同转化系间 TS 表达量做灰度分析或 qPCR 量化。
4. **GGPP 池绝对浓度未测定**：本研究对"通量重定向"效应的解释仅基于 PSY / PDS 已知生化功能的间接推论，未直接测定 PSY / PDS 沉默后 GGPP 的绝对浓度变化，亦未测定类胡萝卜素下游中间体的水平。
5. **赤霉素机制为推论而非直接验证**：原文以推论形式提出（"suggesting that the newly introduced TS gene interferes with the biosynthesis of gibberellins possibly by reducing the pool of available GGPP"），并未直接测定赤霉素含量或叶绿素水平（原文标注 "data not shown"）。
6. **Paclitaxel 结构作为远端目标示意**：Fig. 1 右下角 Paclitaxel (Taxol) 完整母核结构仅作为紫杉醇途径远端目标示意，并非本研究的实际产物。

### 未来研究方向

最值得优先推进的方向是将 TS 基因与下游紫杉烷骨架修饰酶（各类 P450 依赖氧化酶与酰基转移酶）在 *N. benthamiana* 中进行多基因叠加表达，并通过稳定遗传转化逐步逼近完整紫杉醇或紫杉醇前体的异源生产。配套实验应在 PSY 沉默背景下同步测定 GGPP 池的绝对浓度变化（必要时辅以 ¹³C 同位素示踪），以定量验证"通量重定向"的代谢贡献；同时构建稳定的 CRISPR/Cas9 PSY 敲除系以替代瞬时 VIGS，将瞬时性表型效应与稳定的 GGPP 重定向效应分开，避免病毒载体引入的混杂因素。在赤霉素方面，可通过外源赤霉素补给实验检验 GGPP 池对赤霉素合成的限制程度。

# 八、关键问题及回答

**Q1：VIGS 介导的 PSY 沉默显著提高紫杉二烯积累（48 vs 25 μg/g dw），是否可以等同于证明"GGPP 通量重定向"是该效应的直接原因？**

**A**：现有数据可证明"PSY 沉默使紫杉二烯积累增加"这一现象（48 μg/g dw vs 25 μg/g dw；93.58% 升高），但将其完全归因于 GGPP 通量重定向仍缺乏直接代谢证据。作者未在 PSY 沉默植株中直接测定 GGPP 的绝对浓度，也未测定类胡萝卜素下游代谢物的变化，因此"通量重定向"是基于 PSY 已知生化功能的合理推论，而非代谢组定量证据。其次，TRV:GFP 对照中也观察到紫杉二烯产量大幅下降（Fig. 6），说明 VIGS 载体本身对代谢有副作用，PSY 沉默组的净增加是相对于未处理 TSS-8 对照，但 Fig. 6 同时显示 TRV:GFP 大幅压低产量，这一混杂因素在讨论"净"提升幅度时需谨慎区分。建议后续在稳定的 CRISPR PSY 敲除系中重复该实验，并补充 ¹³C 同位素示踪或 GGPP 定量以提供更直接的因果证据。

**Q2：PDS 沉默降低紫杉二烯产量，而 PSY 沉默增加产量，两个结果如何在机制上协调？**

**A**：作者未给出系统性解释，这是本研究最直接的未解之处。可形成数种推测：其一，PSY 直接催化 GGPP → 八氢番茄红素，是类胡萝卜素支路的"第一限速步骤"，阻断后理论上消除对 GGPP 的主要竞争；PDS 位于更下游（八氢番茄红素 → ζ-胡萝卜素），其缺失将导致中间体累积，可能对紫杉二烯合成产生反馈抑制或毒性效应。其二，PDS 沉默引起的严重白化（Fig. 5e）可能改变光保护与氧化还原平衡，带来系统性生理应激，间接压制二萜积累。其三，TRV:PDS 引起的白化可能导致叶片生物量大幅下降，虽指标已换算为 μg/g dw，仍难免引入系统性偏差。建议后续在 PDS 沉默植株中分别监测八氢番茄红素和 ζ-胡萝卜素水平、GGPP 池以及总黄化程度，以进一步定位关键节点。

**Q3：将 TS 基因导入本氏烟草后出现的生长减弱和种子延迟萌发（data not shown），是否提示 GGPP 池被消耗并影响其他必需途径？**

**A**：作者在讨论部分以推论形式提出该解释："suggesting that the newly introduced TS gene interferes with the biosynthesis of gibberellins possibly by reducing the pool of available GGPP."GGPP 不仅是类胡萝卜素和紫杉二烯的前体，也是赤霉素（gibberellins）等必要代谢物的共同前体；CaMV 35S 启动子驱动 TS 组成型过表达，可能将部分 GGPP 转化为紫杉二烯，造成用于赤霉素合成的 GGPP 不足，进而可能造成赤霉素缺乏性矮化。作者援引 Kovacs 等 (2007) 在转基因番茄与 Besumbes 等 (2004) 在转基因拟南芥中观察到的相似现象作为跨物种的间接对应，**但本研究并未直接测定赤霉素或叶绿素含量的具体变化**（"data not shown"，未在本论文中报告独立数据）。因此该解释仍属于合理推论而非常规充分验证；后续可配合外源赤霉素补给实验以验证 GGPP 池对赤霉素合成的限制程度。

> 分类状态：待全部文献笔记完成后统一分类归档。
