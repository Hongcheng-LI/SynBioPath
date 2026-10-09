---
type: literature-reading
zotero_key: GSGUZKME
doi: "10.1016/j.xplc.2023.100630"
paper_type: research
classification_status: pending
reading_status: main-text-and-figures-read
review_status: codex-source-checked
human_full_paper_review: false
source_attachment: 4HVETZVX
source_sha256: b8344d86c08b82abbe8d142c999aef35ee9d63a443fff227ab88d2afbb0db46a
created: 2026-10-09
---

> 原文来源：[Zotero 条目](zotero://select/library/items/GSGUZKME)；[DOI](https://doi.org/10.1016/j.xplc.2023.100630)；由当前 Codex 读取原始主文并核对图表，尚未经人工逐项复核。 来源限制：17mainpagesreadandviewed7complete300dpiFigures SI figures tables1to10actualunread rawMSscRNAmatrixPRJNA909435notdownloaded nohumanreview referencesnotindependentlyread；SpatialMS20umpositive150to1200twobiorepsmasserror10ppmLibraryannotationnotallstandardsstructuresconfirmed3510pixels3506featuresdifferentobjects；DiscussionPM947ResultsFigure974conflict;Fig2selected4taxoidsnotpaclitaxelabsoluteconcentrationtransportnotruledout；8846cellsnotindependentplants35874meanreads2352mediangenesResultsmeanwordconflict36808genes15552cluster-enriched15clusters11Arabidopsismarkersseveralunannotated；Figure3HcaptiontSNEaxisUMAPCellRanger6.1.1vs3.0Monocle3vs2functions mitochondrial5vs20percentdoubletlogicunresolved noanalysisrerun；Leafmesophyllsubclasses16810910379total459CD182pseudotimenotrealageflux;Figure4geneclasscountsResultsconflictsnoenzymeassayforallels；CYP487CYP72574candidatecoexpressionnotreactionidentityFigure5EactualheatmapcaptionKEGGenrichmentconflict；27TF54promotersnetworkpredictednotallvalidatedfiveWRKYonly4IDslistconflict；SixTFEMSAreporterMYB17TSandbHLH46GGPPSrepressWRKY12DBATWRKY31SQEERF13C3HGT2CHSactivateGT2CHSEMSApanelEproteinGSTGT2butarrowbHLH68conflict；GSTpGEXresultsversusHisNimethodproteinidentityconflictEMSA3technicalreporter3biologicalnoTaxusnativeChIPmetabolicinterventionyieldnoKd;deferclassification。

# 文献基本信息

英文标题：Mass spectrometry imaging and single-cell transcriptional profiling reveal the tissue-specific regulation of bioactive ingredient biosynthesis in Taxus leaves。中文题意：质谱成像与单细胞转录组揭示红豆杉叶片活性成分的组织分布及候选调控。研究性论文，Plant Communications，2023，4，100630，DOI：10.1016/j.xplc.2023.100630。正文记录 2023 年 5 月 25 日在线发表，卷期页脚为 9 月 11 日，二者不是同一种日期。Zotero key GSGUZKME；主文附件 4HVETZVX。

作者为 Xiaori Zhan、Tian Qiu、Hongshan Zhang、Kailin Hou、Xueshuang Liang、Cheng Chen、Zhijing Wang、Qicong Wu、Xiaojia Wang、Xiao-lin Li、Mingshuang Wang、Shangguo Feng、Houqing Zeng、Chunna Yu、Huizhong Wang、Chenjia Shen；后两位为通讯作者。主要单位为杭州师范大学，另有中国中医科学院相关单位。作者声明无利益冲突。资助包括国家自然科学基金 32271905、32270382 等。

本次完整读取并查看主文 17 页和 Figure 1–7，图表来自原 PDF。补充图、Supplemental Tables 1–10、原始单细胞矩阵与成像谱图尚未实际读取；所引论文全文未逐篇核实。作者报告参考基因组 BioProject PRJNA730337、scRNA-seq PRJNA909435，相关数据本次未下载或重新分析。当前笔记是 Codex 原文核对产物，未经过人工全文复核，新增笔记统一暂存，分类延后。

# 研究背景

红豆杉叶片是紫杉烷提取的重要原料，但整片叶平均转录或代谢数据会掩盖不同细胞的分工。同一种代谢物可以在某处合成、运输到另一处并积累；“检测到的位置”不能直接等同于“合成发生的位置”。转录组也只反映 RNA 检测，不直接提供酶活、代谢通量或终产物浓度。

作者把 MALDI-2 质谱成像与 scRNA-seq 结合，尝试分别回答成分在哪里积累、有关基因在哪类细胞表达、哪些转录因子可能参与调控。前者提供切片空间信息，后者提高细胞群体分辨率，两者互补。它们并非同一细胞同时测量的配对多组学，因此不能未经空间配准和额外验证就把每个离子图映射到特定单细胞。

背景讨论涉及已报道的 MYB、WRKY、ERF 和 MYC 调控，本文进一步利用细胞表达模式缩小候选范围。其理论价值在于将“有没有这个基因”推进到“哪些细胞检测到它、其候选调控是否与组织位置相容”。所谓主要合成细胞仍需要结构鉴定、酶功能和原位证据支撑，不应仅由成像颜色或单细胞富集断言完整途径已确定。

# 研究思路

首先制备叶切片，获取质谱空间信号并进行分区、PCA 和特征聚类；其次从叶片获得原生质体，构建单细胞转录图谱，利用拟南芥同源 marker 注释部分细胞群；随后将紫杉烷、萜类、甾体、酚酸和黄酮相关候选基因映射到细胞群，并进行叶肉亚群及拟时序分析。

候选调控筛选结合两条线索：转录因子与代谢基因的表达位置相似，以及目标启动子存在匹配的候选顺式元件。表达共现和 motif 都属于预测，不能独立证明直接调控。作者再选取六个 TF–启动子组合，通过 EMSA 和异源双荧光素酶进行局部验证，这才把部分网络连线从预测提升到具有实验支持的候选关系。

笔记将空间积累、RNA 表达、拟时序、体外结合和异源报告分别解释，不把所有网络边视为相同证据等级。尤其需要区分紫杉烷途径本身的已知知识、本文候选基因注释和本文新验证的启动子联系。

# 研究方法

材料为杭州师范大学仓前校区露地生长的五年生 T. mairei，取嫩枝叶片。主文没有充分说明单细胞样本来自多少独立树、是否混样及各生物学重复怎样映射到测序文库，8846 个细胞不能当作 8846 个独立植株重复。质谱成像使用 timsTOF fleX MALDI-2，切片与成像分辨率均为 20 µm，正离子模式、m/z 范围 150–1200。文本提取曾把 µm 读成 mm，本次以原页图像核对单位。

成像使用 SCiLS Lab MVS v2021a Pro、MetaboScape 和 Bruker Library MS Metabase 3.0，分子质量误差阈值 <10 ppm。主文没有给出所有成分逐一与标准品共测、MS/MS 匹配得分或结构鉴定等级，因此成分名称应当保留库注释边界，尤其不能仅凭质量匹配确认立体异构体。Methods 报告成像两个生物学重复，但主要图没有展示每个重复的离散程度或全部不确定性。

单细胞使用 10× Chromium、Illumina NovaSeq 6000，并报告 Cell Ranger v6.1.1 和 v3.0.0、Seurat v2.3.4、DoubletFinder v2.0.2。质控中同时写 mitochondrial reads >5% 和 >20%，且将多种筛选条件统称 doublets，具体逻辑不清楚。拟时序写 Monocle v3.0，同时列出 Monocle 2 的 importCDS 等函数，版本与执行细节仍待代码核查。结果页同时出现 Loupe、Seurat、t-SNE 与 UMAP，不能假定所有投影都来自同一算法。

启动子预测使用 2000 bp 上游区域和 PlantCARE。EMSA 有结合探针、竞争探针及突变竞争探针，Methods 称三个技术重复；双荧光素酶称三个生物学重复，并记录 ANOVA 后 Duncan 比较及 P <0.05。原文未给出全部精确 P 值、置信区间或原始重复值，不能由星号自行还原。蛋白标签、部分图例和面板标签存在冲突，具体见下文。

# 实验设计及结果分析

### 1. 空间质谱揭示积累模式，但成分和合成位置仍需区分


![Figure 1 原文第 3 页](https://synbiopath.online/GSGUZKME-Figure-1-p3-complete-e647e33f470daa5b.png)

*Figure 1：原文 Figure 1：完整图表及图注（原文 PDF 截图）。*



![Figure 2 原文第 4 页](https://synbiopath.online/GSGUZKME-Figure-2-p4-complete-c645f1d263b7faef.png)

*Figure 2：原文 Figure 2：完整图表及图注（原文 PDF 截图）。*


Figure 1 的空间图有 3510 个点，不是 3510 个结构已确认的代谢物。特征聚类六组分别为 974、717、485、411、636、283，总计 3506 个特征；两组数字代表不同对象，不能因为接近就混用。作者把四个 PC 关联到 SM、EP、BS、PM，其中 SM 描述还包含韧皮部与海绵叶肉，说明组织分区不是严格纯单细胞类别。

Figure 2 展示七类各四种库注释成分。quercetin、rutin 等在表皮方向信号较高；所选四种紫杉烷包括 10-deacetyl cephalomannine、10-deacetyl paclitaxel、10-deacetyl baccatin III、baccatin III，作者描述主要位于 SM。这里并非直接展示 paclitaxel 本身，也没有提供 µg/g 或 mg/L 的紫杉醇定量。颜色和比例体现相对离子信号，不能直接作为不同化合物的绝对浓度比较，因为离子化效率和基质效应可能不同。

空间成分与基因表达之间的一致性支持组织分工假设，但代谢物运输、储存和不同空间分辨率仍是替代解释。Discussion 将 PM 特征数写成 947，而 Results 与 Figure 1 为 974，本次并列记录，不自行选择一个正确值。成像能够指导取样和提出定位问题，不能仅由最亮区域认定该区域具有最高净合成通量。

### 2. 单细胞图谱和细胞注释的覆盖边界


![Figure 3 原文第 5 页](https://synbiopath.online/GSGUZKME-Figure-3-p5-complete-0773e0330a84e3f0.png)

*Figure 3：原文 Figure 3：完整图表及图注（原文 PDF 截图）。*


图谱保留 8846 个细胞，平均每细胞 35,874 reads；Figure 3D、摘要和 Discussion 将 2352 标为每细胞基因数中位数，Results 部分却写平均值。本笔记采用图中清楚标示的 median，并保留文字冲突。表达数据覆盖 36,808 个基因，报告 15,552 个 cluster-enriched genes；这些数量并不等于 15,552 个独立功能已验证的 marker。

作者分成 15 群，最大 Cluster 0 为 1180 个细胞，最小 Cluster 14 为 90。11 个来自拟南芥同源比对的 marker 用于识别部分组织：6/7 与叶肉有关，3 与维管束鞘及叶脉有关，8/12 包含气孔复合体和保卫细胞，9 为维管/原形成层，13 为 pavement cells，14 为韧皮部。Cluster 12 同时含多种表皮相关标签，注释不能简单写成十五群分别对应十五种已明确细胞类型。

Discussion 明确有一些大群因缺可靠 marker 尚不能注释。marker 同源性和表达富集是合理起点，但未等同于红豆杉原位定位验证。原生质体解离还可能造成不同细胞回收率和诱导表达的差异，不能将群体大小直接解释为原叶片的精确细胞组成比例。Figure 3H 图注称 t-SNE，面板坐标标 UMAP，这一图文不一致也需保留。

### 3. 紫杉烷候选基因主要在叶肉亚群表达，拟时序不是实测时间


![Figure 4 原文第 7 页](https://synbiopath.online/GSGUZKME-Figure-4-p7-complete-e3787a77d6ab2b45.png)

*Figure 4：原文 Figure 4：完整图表及图注（原文 PDF 截图）。*


Figure 4B/C 显示不少紫杉烷相关候选 RNA 在 6/7 群较丰富，另有 T10OH、TBT、DBBT、DBTNBT 等部分候选在 Cluster 3 有信号。作者以表达细胞覆盖率比较同一酶类别候选：TS ctg6088_gene.1 为 7.85%，T5OH ctg7747_gene.2 为 8.17%，DBTNBT ctg887_gene.16 为 22.48% 等。覆盖率表示检测到表达的细胞比例，不能等同于转录量、酶效率、反应重要性或最终产量。

叶肉再聚类 A/B/C/D 为 168、109、103、79 个细胞，总计 459，其中 C+D 为 182，约占 39.65%。大部分所列通路候选在 C/D 中较高，作者结合拟时序解释为较成熟叶肉。该结果支持一个候选表达状态，但不是实际追踪同一细胞从年轻到成熟，也不证明 C/D 群是唯一合成细胞。分支与先后关系依赖输入、根节点及算法，生物学年龄需要独立验证。

主文 Results 的各类基因数量与 Figure 4A 括号存在多处不一致，例如正文 T5OH 四个，图中标五个，TAT 正文七个，图中标三个；图注又用“each key enzyme”作概括。因此不把图 A 的数字和 Results 列表合并成一个已确认的通路基因总数。途径图及 RNA 注释不是本文逐个重构酶反应的结果，Discussion 提出的提高沉默基因覆盖率可以增产也仍属假设。

### 4. CYP725 和跨途径调控网络是候选筛选资源


![Figure 5 原文第 8 页](https://synbiopath.online/GSGUZKME-Figure-5-p8-complete-8525e2fa7b81411d.png)

*Figure 5：原文 Figure 5：完整图表及图注（原文 PDF 截图）。*



![Figure 6 原文第 10 页](https://synbiopath.online/GSGUZKME-Figure-6-p10-complete-a76cb8038d36f32b.png)

*Figure 6：原文 Figure 6：完整图表及图注（原文 PDF 截图）。*


作者根据参考基因组识别 487 个 CYP 候选，包括 74 个 CYP725。Figure 5 支持部分 CYP725 在 6/7 和 C/D 富集，并展示六个候选的表达。家族归属加上表达位置相似有助于优先筛选，但尚未鉴定这些候选各自催化的底物、产物或反应位点。Figure 5E 实际为表达热图，图注却写 KEGG enrichment，与正文拟时序描述不一致；不能把该面板作为 KEGG 富集结果引用。

Figure 6 的候选 TF 筛选使用 log2(target cluster/other clusters)>0.26、P <0.01，约相当于表达比值 >1.20，属于作者筛选阈值，并非功能效应的普遍标准。列出六 MYB、五 bHLH、四 GT_2、五 ERF、七 WRKY，共 27 个候选。启动子筛选覆盖 24 紫杉烷、6 酚酸、6 黄酮、13 萜类、5 甾体相关候选，共 54 个启动子；并非所有连接都被验证。

共表达和 motif 匹配形成的是预测网络。紫杉烷候选部分写五个 WRKY，却仅列四个 ID，数量仍未解决。多个 TF 可能匹配相同元件，也可能通过其他蛋白间接调控；不能因为网络图有连线，就认为该因子在红豆杉内源染色质上实际占据该启动子。关于甾体与萜类碳流竞争，也未在本篇以同位素或通量实验直接验证。

### 5. 六组 TF–启动子关系的实验支持及标签问题


![Figure 7 原文第 11 页](https://synbiopath.online/GSGUZKME-Figure-7-p11-complete-e67da641c7b916c9.png)

*Figure 7：原文 Figure 7：完整图表及图注（原文 PDF 截图）。*


正文将六组配对写为 MYB17–TS、WRKY12–DBAT、WRKY31–SQE、ERF13–C3H、GT_2–CHS、bHLH46–GGPPS。EMSA 显示蛋白加入后出现较慢迁移带，未标记野生型竞争探针增加时复合物减弱，突变竞争探针不产生相同削弱，支持体外序列选择性结合。20×、200× 属竞争探针比例，不能换算为 Kd，也不是目标启动子全部区域的原位占据证据。

Figure 7H 的异源报告支持 WRKY12、WRKY31、ERF13、GT_2 对所配启动子产生激活，MYB17 和 bHLH46 则产生抑制。不能因为在候选通路中表达就将所有 TF 写成增产激活因子。实验以启动子输出为终点，没有在 Taxus 中操作这些因子后测代谢物，也没有证明六组关系对内源产物积累必要或充分。

原文 Figure 7E 的 CHS 探针面板上方蛋白标为 GST-GT_2，复合物箭头旁却写 bHLH68，与正文 GT_2–CHS 配对冲突；Figure 7F 才是 bHLH46–GGPPS。Figure 7H 的 GT_2–CHS 报告与正文一致。Methods 的 pGEX4-T 与图注 GST 蛋白，和同段 His 标签、Ni 树脂描述也不一致。当前可记录作者声称的 GT_2–CHS 关系及其 reporter 结果，但不能隐去 EMSA 复合物标签未解决的问题。Figure 7I–L 是整合空间示意，不是新增原位杂交或示踪实验。

# 总体结论

研究建立了红豆杉叶片相对空间代谢图与单细胞 RNA 图谱，提出多数紫杉烷相关候选表达在叶肉细胞的特定亚群，酚酸和黄酮相关候选更多位于表皮相关群。它还将共表达与顺式元件用于筛选调控因子，并为六组局部配对提供体外结合和异源启动子报告结果。

最有价值的是发现和排序候选的框架，而非将全部代谢物、酶功能与空间因果关系一次确认。成分库注释、跨物种 marker、拟时序和共表达网络各有边界；EMSA 与 reporter 的局部验证也不能代替红豆杉内源染色质占据、代谢输出和运输证据。本篇没有紫杉醇增产或工业性能比较。

# 论文评价

优点是两种互补组学联合定位问题，并把一部分计算候选推进到实验验证；数据可用于优先关注细胞表达相容的基因和调控关系。Methods 对成像、EMSA 和 reporter 的重复类型作了区分，这对证据解释很重要，不能把技术重复混作生物学重复。

限制包括成像注释等级、单细胞独立植株重复、未注释群体、解离偏倚和拟时序依据；再加上数处图文标签及软件说明冲突，妨碍直接复现。Discussion 写“下调萜类合成基因可以提高紫杉醇”与上文强调 GGPP 前体供给之间需要具体竞争分支背景，不能把这句话直接当作通用工程建议。现有数据也不能区分本地合成与跨组织运输。

对知识库使用，本篇可与 TcWRKY26/33、MYB39 和叶片组织专题建立联系，但不能把不同物种、组织或 promoter 片段的结果拼成一个完全验证的网络。优先保留候选 ID、细胞群、配对证据类型和未解决标签问题，后续才便于筛选真正需要原始数据或实验验证的关系。

# 关键问题及回答

**问题 1：8846 个细胞是否意味着 8846 个独立生物学重复？** 否，它们是捕获细胞数；植株、样本与文库的独立性主文未充分交代，不能将细胞数量代替植株重复。

**问题 2：质谱成像最亮处就是合成位置吗？** 不一定。信号涉及积累、运输和离子化；RNA 空间关联可以加强候选解释，仍不直接测通量或排除运输。

**问题 3：拟时序证明成熟细胞形成时间和紫杉醇产量了吗？** 没有。它对转录状态排序，生物学方向依赖解释与验证；本文没有实际时间追踪或产量测定。

**问题 4：六个 TF 全部促进所配启动子吗？** 否，MYB17–TS 和 bHLH46–GGPPS 在 reporter 中为抑制，另四组为激活。GT_2–CHS 的 EMSA 面板蛋白标签还存在冲突。

**问题 5：CYP725 的共表达足以分配酶反应吗？** 不足，它用于优先选候选，不提供底物、产物和区域选择性的直接测量。

**问题 6：后续最需要核查什么？** 优先核查补充材料、原始矩阵和分析代码，以澄清标签、细胞注释、重复和版本问题；对空间因果与代谢输出另行建立原位及功能证据。当前这些均未完成，不能宣称全网络已验证。

> 分类状态：待全部文献笔记完成后统一分类归档。
