---
type: literature-reading
zotero_key: N5CFQ4FU
doi: "10.3389/fpls.2024.1403060"
paper_type: research
classification_status: pending
reading_status: main-text-and-figures-read
review_status: codex-source-checked
human_full_paper_review: false
source_attachment: 8EVCLUYD
source_sha256: 6fd2d7e3da3e54f5584ed9cbad6eb24d17f066d3b6c70a234dcb97914ea0ef9a
created: 2026-10-08
---

> 原文来源：[Zotero 条目](zotero://select/library/items/N5CFQ4FU)；[DOI](https://doi.org/10.3389/fpls.2024.1403060)；由当前 Codex 读取原始主文并核对图表，尚未经人工逐项复核。 来源限制：All11mainpagesreadandviewedFigure1to5Table1; actualsupplementarytablesunreadSRArawdatabasesnotdownloadedreferencesnotindependentlyread；Allregulationedgespredictionorcoexpression noPARE5RACEcleavagereportergeneticperturbationtaxolquantification nofunctionalenzymeproof；Methodtreatmentreplicate1 tissue6sex3; new2female2male leavesdifferentdataset n3notunified nofullmetadataorbatchmodelverified；Table1miR159bduplicateB/C 15categoryentries14uniquemiRNA namesplusPhas217; Discussion4.3directtargetovergeneralization；49miRNAtargetenzymes18phasiRNAtargetenzymesoverlapunknownnot67unique;160PHASloci not160validatedmatureproducts；48of160Chr10equals30percent;71enzymehomologyespecially_like_notvalidatedfunction；Coordinates109N30Ewith60minuteinvalid retainnotcorrect;141.687512MbregionnotcompactBGCproof；TPTMsRNA notTPMmRNA orpercellcopies activity yield; heatmaptranscriptnotmetaboliteproduction。

# 文献基本信息

**标题：** Regulatory microRNAs and phasiRNAs of paclitaxel biosynthesis in Taxus chinensis。**中文题名：** 中国红豆杉紫杉醇生物合成相关 microRNA 与 phasiRNA 的候选调控网络。

**作者：** Ming-Sheng Sun、Yan Jia、Xin-Yi Chen、Ji-Shi Chen、Ying Guo、Fang-Fang Fu、Liang-Jiao Xue；后两位为通讯作者。单位为南京林业大学相关林木遗传育种与南方现代林业研究平台。**期刊及年份：** Frontiers in Plant Science，2024，15:1403060；2024年5月8日发表。**DOI：** 10.3389/fpls.2024.1403060。**类型：** 原始研究，以转录组、小 RNA 测序和计算预测为主。

**阅读范围：** 已核对主文 PDF 全部11页及 Figure 1–5、Table 1 原图；图片来自本地原始 PDF。补充表、SRA 原始数据和参考文献全文未实际读取，不把其内容标为独立复核。新增数据的作者报告 accession 为 PRJNA1031429；公共数据为 PRJNA730337、PRJNA251671、PRJNA173133，尚未下载核验。自动题名匹配标记原先为 false，但主文第一页标题、作者和 DOI 与记录一致，人工逐字核对后确认主文身份。

**一句话结论：** 论文整合多条件表达数据，提出酶基因—转录因子—miRNA—phasiRNA 的候选网络；它适合作为后续功能验证的线索库，尚未证明具体小 RNA 对目标基因的切割、因果调控或紫杉醇增产。

# 研究背景

紫杉醇的天然供应和细胞培养生产受到原料、生长状态、复杂代谢途径及调控不稳定等限制。通路涉及多种氧化、酰基转移和侧链连接反应，同一家族还存在功能未确定的同源成员。因此，仅凭单个酶的表达量，难以判断整体通量；仅改变一个转录因子，也可能影响生长和其他次生代谢。

已有研究关注 MYB、AP2/ERF、bHLH、WRKY 等转录因子，而 miRNA 和相位性小干扰 RNA，即 phasiRNA，提供转录后调节的另一层候选机制。植物 miRNA 可以通过序列互补介导靶 RNA 降解或影响翻译，但这种一般机制不能自动证明某条预测配对在红豆杉中确实有效。phasiRNA 还可能经由转录因子产生间接作用，使网络层次更加复杂。

本文真正需要回答的是：哪些通路相关基因在不同组织、性别和茉莉酸处理下共同变化，哪些转录因子与其表达相关，哪些小 RNA 在序列上可能靶向这些节点？作者在摘要中使用“调控”和“稳健调节”等措辞，但主文提供的直接证据主要是测序、注释、相关性和靶标预测，需要与经过生化或遗传验证的调控作用区分。

# 研究思路

研究依次建立四个层次。第一，依据参考基因组和同源注释筛选紫杉醇合成相关基因，并比较组织、处理和性别表达。第二，在全基因组转录因子中用 Spearman 相关和 WGCNA 寻找与候选酶基因同变化的节点。第三，根据小 RNA 测序、前体结构及相位特征识别 miRNA、PHAS 候选位点，并预测靶标。第四，将这些关系合并成网络，区分直接靶向酶、通过转录因子以及通过 PHAS—转录因子产生作用的候选路径。

这条路线能够缩小搜索空间，但每次合并都引入假设：同源注释假设功能相关，共表达假设存在共同调控，互补配对假设可发生有效靶向，多层网络又假设各节点在相容的细胞和条件下发挥作用。本文没有完成这些假设的逐层实验确认，所以网络应被读作“可检验关系图”，而不是已建立的机制链。

# 研究方法

新增材料为2021年5月湖北恩施采集的两株雌树、两株雄树幼叶，同时整合42个已发表 RNA-seq 样本和3个公共小 RNA 样本。方法给出的采样坐标为109°52′19″N、30°60′03″E，其纬度和分值写法明显异常；保留原文问题，不据此自行修正具体地点。新采个体数与作者报告性别差异分析重复数并非直接一一对应，完整样本配对关系需要补充元数据核验。

mRNA 测序采用 Illumina NovaSeq 双端测序；Trimmomatic 0.39 清洗，STAR 2.7.9 两轮比对，RSEM 计算 TPM。作者描述对部分重复取平均，并给出组织、处理、性别差异分析的重复数分别为6、1、3。edgeR 筛选阈值为 |logFC|>1、FDR<0.05。正文没有充分交代完整计数矩阵、离散度估计及批次模型；不能根据 TPM 的描述就断言 edgeR 使用了 TPM，也不能认为统计阈值补足了处理组缺少独立重复的问题。

小 RNA 使用 HiSeq2500 单端50 bp 测序，Cutadapt 2.10、Rfam 11.0 和 Bowtie 1.3.0 清洗及去除其他非编码 RNA。ShortStack 根据覆盖和前体信息筛选 miRNA，PatMaN 与 miRBase 22.1 比对已知成熟体，允许至多4个错配；其余候选结合前体和 miRNA* 信息处理。PHASIS 3.3 用于相位性小 RNA 位点识别，phastrigs 推测触发 miRNA。预测鉴定结果不等于每一成熟小 RNA 的加工过程已得到实验确认。

psRNATarget 用于靶标预测，最大 score 为3，GU 配对惩罚0.5、错配惩罚1、HSP 长度19、gap opening 2、gap extension 0.5。该分数是计算筛选尺度，不是作用强度或靶标切割率。小 RNA 丰度单位为 TPTM，即每千万 reads 的转录本数，与 mRNA 的 TPM 不同。

Diamond 以 E-value≤10⁻⁵进行同源及背景注释，iTAK 识别转录因子，clusterProfiler 3.18.1 进行 GO/KEGG 富集，FDR≤0.05。共表达筛选 |Spearman r|≥0.7，WGCNA 合并阈值 height>0.25；Figure 3 中蓝线对应网络权重>0.3，红线对应相关系数绝对值≥0.7。这些线既不能证明启动子结合，也不能确定激活或抑制方向。主文未报告小 RNA 靶标的降解组、5′ RACE、报告基因、遗传干预或紫杉醇定量验证。

# 实验设计及结果分析

### 1. 通路候选基因与表达比较：表达图谱不能直接替代产量

作者获得71个通路相关候选基因，覆盖 GGPPS、TXS、多类羟化酶、酰基转移酶和侧链相关基因。Figure 1 为结合既有研究绘制的途径框架，蓝色表示已鉴定酶、红色表示未知酶；本文没有重新测定图中全部反应。图中 oxetane 形成、C9 氧化等知识来自引用的前人工作，不能归为本文的酶学发现。


![Figure 1 原文第 4 页](https://synbiopath.online/N5CFQ4FU-Figure-1-p4-complete-ce9fc1fffd9d9d76.png)

*Figure 1：原文 Figure 1：完整图表及图注（原文 PDF 截图）。*


作者讨论染色体9上约80.46 Mb和141.69 Mb的区域，并在后一个区域识别额外 T10βOH_like 与 T5αOH_like 同源候选。给定坐标616,470,670–758,158,182 bp，跨度约141.6875 Mb，是很大的区域；位置聚集并不自动证明紧凑、共转录或已功能验证的生物合成基因簇。名称中的 `_like_` 必须保留，不能直接升级为具有对应催化活性的酶。

Figure 2A 显示多种通路基因在球果和根中表达相对较高。这里反映转录状态，本文没有同时测量这些样本的紫杉醇浓度，因此不能推出球果或根必然产量更高。热图使用 log₂(TPM+1)，不同面板的色标和比较目标需要分别理解，颜色深浅不是共同的产量单位。

Figure 2B 整合细胞系茉莉酸处理0、2、4、8、24小时与酒精对照，许多通路基因上调，4小时反应较明显，GGPPS 和 CoA ligase 为作者指出的例外。处理差异分析报告重复数为1，图中星号和 FDR 阈值不能替代独立生物重复，因而不宜把时间曲线视为稳定可重现的定量调控规律。

Figure 2C 中雌雄差异依组织而变：部分后段基因在雌树树皮中较高，球果整体雄性较低，但根中趋势可反转，叶片差异较小；新增恩施幼叶未见显著性别差异。这些结果不支持“雌树在所有组织都更适合紫杉醇生产”的概括，组织、发育阶段、材料来源和条件都可能影响比较。


![Figure 2 原文第 5 页](https://synbiopath.online/N5CFQ4FU-Figure-2-p5-complete-3afa28abdd2534e7.png)

*Figure 2：原文 Figure 2：完整图表及图注（原文 PDF 截图）。*


### 2. 转录因子共表达网络：筛选候选而非证明直接调控

全基因组识别990个转录因子、60个家族，相关候选包括 MYB、AP2/ERF、bHLH、HB、LOB、MADS 和 WRKY。WGCNA 得到29个模块，通路相关基因主要见于 Green-yellow、Lightcyan1 和 Lightcyan。Figure 3A 展示的是模块中相关转录因子数量和组成，不是各家族调控效应的大小。

Figure 3B 的最终网络含10个酶基因和28个转录因子。酶基因为 GGPPS-1、T5αOH_like_4、T13αOH-3、TAT-1、T2αOH-1、T10βOH_like_5、T10βOH_like_8、TBT-2、TBT-4、BAPT-2。箭头表现作者构建的关系，但原始证据仍为共表达。由于筛选使用相关系数绝对值，正负关系可能同时进入网络，不能将全部箭头解释为激活。


![Figure 3 原文第 6 页](https://synbiopath.online/N5CFQ4FU-Figure-3-p6-complete-5be46a9aaf44dc15.png)

*Figure 3：原文 Figure 3：完整图表及图注（原文 PDF 截图）。*


组织和处理变化可能共同驱动多个基因，因而相关关系既可能来自真实调控，也可能来自相同细胞类型、共同上游信号或数据来源差异。本文没有对这些候选进行启动子结合验证，也没有排除所有批次与组织组成因素。候选 TF 可作为后续研究入口，但不是已确认的直接调控元件清单。

### 3. miRNA 与 phasiRNA 图谱：数量、位点和富集的含义

作者报告460个 miRNA、311个家族，其中92个已知家族和219个新家族；92+219对应家族总数311，不是460个成熟 miRNA 被划分为92个已知和219个新成员。长度20–24 nt，以21 nt 为主，第一碱基偏向 U；染色体臂上候选较多，着丝粒附近较少。

另识别160个21-nt phasiRNA 相关候选，48个位于染色体10，比例为30%。正文称超过四分之一，不能把它写成恰好25%。方法识别的是 PHAS 位点，表中使用 Phas 编号；“160 phasiRNAs”的表述不能不加区分地转成160条已验证成熟产物。未检出其他长度候选仅限该数据和分析流程，不能推出中国红豆杉从不产生24-nt phasiRNA。

miRNA 靶标预测涉及49个通路相关基因，phasiRNA 靶标预测涉及18个。两集合是否重叠没有在主文给出完整核查结果，所以不能把49+18=67当作67个不同通路基因，也不能断言71个候选都受小 RNA 控制。280个 miRNA 被预测可触发160个 PHAS 候选，仍未得到触发切割和相位起始实验验证。


![Figure 4 原文第 7 页](https://synbiopath.online/N5CFQ4FU-Figure-4-p7-complete-07aabc5f768a6129.png)

*Figure 4：原文 Figure 4：完整图表及图注（原文 PDF 截图）。*


Figure 4 的 GO/KEGG 富集涉及所有预测靶标及其交集，并非只分析紫杉醇酶基因。ADP binding、铜离子结合、氧化还原、蛋白二硫键还原、激素信号等富集说明靶标注释的统计分布，不证明紫杉醇途径的真实响应机制。富集显著性不是单条调控边的可信概率；图中 GeneRatio、点大小和校正后 P 值也不能替代具体靶标功能验证。

### 4. 多层网络与高丰度候选：保留直接、间接及重复计数

Figure 5 合并60个 miRNA、9个 phasiRNA、14个转录因子和10个酶基因。这个14 TF 的网络不同于 Figure 3 的28 TF 网络，不能混用节点数量。红线和紫线分别代表预测的 miRNA/酶及 phasiRNA/酶关系，灰线还包含 miRNA/TF、phasiRNA/TF 和 TF/酶关系，其中最后一类来自共表达；图形统一不表示证据类型统一。


![Figure 5 原文第 7 页](https://synbiopath.online/N5CFQ4FU-Figure-5-p7-complete-2915e8ac78f6c270.png)

*Figure 5：原文 Figure 5：完整图表及图注（原文 PDF 截图）。*


Table 1 的 A 部分有6个直接靶向酶的 miRNA 候选，并另列 Phas-217。例如 miRN108 与 miRN109 预测靶向 TBT-2，丰度分别1,649,830和667,260 TPTM；miR164a 与 miR164c 预测靶向 T10βOH_like_8；miR482g 预测靶向 T5αOH_like_4；miR7762.1 预测靶向 TAT-1。Phas-217 为275,530 TPTM，其预测酶靶标为 T5αOH_like_4。表中丰度是测序归一化量，不是每细胞拷贝数、作用率或抑制倍数。

B 部分的6个 miRNA 通过候选 TF 联系通路。miR482j 为2,172,780 TPTM，预测靶标是 HB-HD-ZIP 转录因子 gK_016017，表列下游 TBT-4、T5αOH_like_4；这不能简化为 miR482j 已被证明直接切割这两个酶转录本。miR396d 和 miR396b 涉及两个 GRF 候选，miR159b 与 miRN187 涉及 MYB 候选 gK_002135。表中 Note 列给出的是进一步关联的酶基因，不是第一层直接靶标。

C 部分的 miR482c、miR482l 预测经 Phas-227/Phas-297 联系 MADS-MIKC 候选，再联系酶基因；miR159b 另经 Phas-7 联系同一个 MYB 候选。miR482c 丰度3,957,410 TPTM，数值较高不代表它最适合工程干预，更不代表紫杉醇增产倍数。


![Table 1 原文第 8 页](https://synbiopath.online/N5CFQ4FU-Table-1-p8-complete-5f5280071646a46f.png)

*Table 1：原文 Table 1：完整图表及图注（原文 PDF 截图）。*


正文将高丰度候选称为15个 miRNA，并按6个直接、6个经 TF、3个经 PHAS 分类。但 miR159b 同时列于 B 和 C，按表格名称去重得到14个不同 miRNA；15是类别条目数。保留作者报告15的同时注明重复，不能把它悄悄改成15条独立小 RNA。讨论4.3又将若干关键酶称为被15个高丰度 miRNA“直接靶向”，与 Table 1 的多层关系不一致，笔记以明确列出的层次为准。

### 5. 从候选网络到因果机制还缺什么

本研究完成了测序和计算筛选，但没有报告降解组、5′ RACE 或其他目标切割证据，也没有小 RNA 干预后的靶标 RNA、蛋白、酶活和紫杉醇定量。因而“miRNA—PHAS—TF—酶”只能作为待检验机制。若 TF 实际是抑制因子，小 RNA 抑制 TF 可能解除对通路的抑制；若 TF 是激活因子则可能相反，网络本身不能决定最终作用方向。

作者提出 miRNA sponge、ceRNA 或基因编辑等应用方向，属于展望，本文没有实施或证明增产效果。合理的后续验证需要首先核对序列、同源家族及同一组织中的表达共存，再区分直接靶向与间接相关，最后将分子证据与代谢读数对应。这里不补写论文未实施的具体构建参数、剂量、培养条件或产量。

# 总体结论

本文在中国红豆杉中建立了71个通路相关候选基因的表达图谱，并提出990个 TF、460个 miRNA 和160个 PHAS 相关候选参与的调控搜索空间。它将组织和性别差异、茉莉酸响应、共表达与小 RNA 配对信息连接起来，形成最终含60 miRNA、9 phasiRNA、14 TF 和10酶基因的候选网络。

最有价值的结果是可追踪的候选节点和关系层次。最重要的限制是网络没有完成因果验证或产量验证：同源基因未必具有命名所暗示的酶活，小 RNA 预测靶标未必被实际切割，共表达 TF 未必直接结合启动子，多层联系也未必产生同方向的净效应。应将本文归入调控网络发现与功能验证线索，待全库笔记完成后统一分类。

# 论文评价

**优点：** 将转录调控和转录后调控放在同一框架；区分组织、性别和处理条件；原图和 Table 1 提供了可定位的候选关系；报告多个软件版本、筛选阈值和新增数据 accession，便于复核。对于紫杉醇细胞工厂知识库，能补足单一转录因子研究之外的 RNA 调控视角。

**限制：** 多来源数据的样本独立性、批次处理及完整统计设计不够清晰，处理差异分析的重复数尤其有限。缺少靶标切割、结合、遗传干预和代谢物验证，因此“层级调控”“稳健调控”的结论强度高于直接证据。71个同源候选、160个 PHAS 位点及各网络节点数量需要分别理解，不能拼接成已经完整验证的机制图。

**原文内部问题：** Table 1 中 miR159b 重复出现在两类路径，15个高丰度候选不能按15个独立名称统计；讨论将间接关系概括为直接靶向；采样经纬度写法异常。上述问题不会抹去测序资源的价值，但降低了直接将文字结论转为知识库事实或工程靶点的可靠性。

**证据边界：** 本笔记完成主文和图表源核对，不代表原始数据重分析、补充材料验证或独立专家复审。作者在利益冲突声明中报告无商业或财务关系，资助包括2022YFD2200601、32101559及BK20220411；这些是作者报告信息，不是额外独立验证。

# 关键问题及回答

**问题1：这篇论文证明某个 miRNA 能提高紫杉醇产量了吗？**

没有。它报告测序、靶标预测和共表达网络，没有小 RNA 干预与紫杉醇定量的对应实验。正文提出应用方向不能改写为已完成增产。

**问题2：49个 miRNA 靶向通路基因与18个 phasiRNA 靶向基因可以相加吗？**

不能用相加结果表示不同基因数，集合可能重叠。只有逐条核对补充表中的基因 ID 才能计算并集，主文尚不足以完成这一核验。

**问题3：Table 1 的高丰度是否代表调控更强？**

不能。TPTM 是序列 reads 归一化丰度，受文库和加工等因素影响。靶标可及性、实际配对、细胞共定位以及 TF 正负作用均未由丰度值证明。

**问题4：网络箭头能表示直接激活吗？**

不能。部分边为计算配对，部分为表达相关，且相关阈值采用绝对值。是否直接结合、激活或抑制，需要独立实验和带方向的信息。

**问题5：该文与已经解读的 TcWRKY33、TcMYB73 研究如何连接？**

它为潜在上游 RNA 层提供线索，但没有证明这些小 RNA 作用于已验证的具体 TcWRKY33 或 TcMYB73 机制链。若基因名称相似，也需核对精确基因 ID、序列和实验材料后才能建立跨论文连接。

**问题6：最应保留的知识库标签是什么？**

保留紫杉醇、Taxus chinensis、miRNA、PHAS/phasiRNA、共表达、靶标预测以及“功能待验证”的证据描述。目前暂存于待归类目录，完整分类在全库笔记完成后统一进行。

> 分类状态：待全部文献笔记完成后统一分类归档。
