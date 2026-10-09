---
type: literature-reading
zotero_key: ANV2VH9A
doi: "10.1016/j.ymben.2022.10.007"
paper_type: research
classification_status: pending
reading_status: main-text-and-figures-read
review_status: model-source-crosschecked
human_full_paper_review: false
source_attachment: ZX6747RX
source_sha256: a2c70ff330e570888cf641312bd0967772c511e05f2f468df0e045bdb08e3377
created: 2026-10-07
---

> 原文来源：[Zotero 条目](zotero://select/library/items/ANV2VH9A)；[DOI](https://doi.org/10.1016/j.ymben.2022.10.007)；主文与图表已按来源进行模型交叉核对，尚未经人工逐项复核。 来源限制：未提供 Supporting Information 文件，化合物 1–18 的具体 NMR/HRMS 数据、图 S1–S23、Table S1–S5 等无法核对；Figure 2C 中化合物 1、15 标记为新化合物，但具体结构与波谱归属细节仅在 SI (Tables S3–S4 与 Figs. S3–S19) 中给出，正文未展开；关于 PtaI 的动力学参数 (K_m, k_cat)、底物谱与结构信息原文未提供。

# 一、基本信息

**文章题目**：Microbial production of the plant-derived fungicide physcion（植物源杀菌剂大黄素甲醚的微生物生产）

**文章 DOI 号**：10.1016/j.ymben.2022.10.007

**期刊名称**：Metabolic Engineering

**通讯作者及工作单位**：

- **黄雪年 (Xuenian Huang)**：中国科学院青岛生物能源与过程研究所（Qingdao Institute of Bioenergy and Bioprocess Technology, Chinese Academy of Sciences），同时挂靠山东省合成生物学重点实验室、山东省能源研究所、青岛新能源山东实验室及中国科学院大学
- **吕雪峰 (Xuefeng Lu)**：中国科学院青岛生物能源与过程研究所（Qingdao Institute of Bioenergy and Bioprocess Technology, Chinese Academy of Sciences），同时挂靠山东省合成生物学重点实验室、山东省能源研究所、青岛新能源山东实验室、中国科学院大学及青岛海洋科学与技术国家实验室海洋生物学与生物技术实验室

第一作者齐菲菲 (Feifei Qi) 与张伟 (Wei Zhang) 对本文有同等贡献；其他作者包括薛莹莹 (Yingying Xue)、耿策 (Ce Geng)、靳志刚 (Zhigang Jin, 同时隶属山东大学微生物技术国家重点实验室与山东鲁抗医药股份有限公司)、李吉彬 (Jibin Li, 山东鲁抗医药股份有限公司) 与郭强 (Qiang Guo, 山东鲁抗医药股份有限公司)。

---

# 二、研究背景

大黄素甲醚 (physcion) 又称 parietin (蜈蚣苔素)，是大黄等蓼科 (Polygonaceae) Rheum 属植物的特征性蒽醌类次级代谢产物，因其 C3 位羟基的甲醚化修饰，相较大黄素 (emodin) 及其 C1 位甲醚化产物 questin 表现出更优的抗肿瘤（通过干扰 6-磷酸葡萄糖酸脱氢酶活性或诱导细胞凋亡，Ding et al., 2018; Lin et al., 2015）、抗菌 (Basile et al., 2015) 与抗肥胖 (Lee et al., 2019) 等药理活性 (Xun et al., 2019)。此外，大黄素甲醚在中国已被批准为商品化植物源杀菌剂，用于防治白粉病、霜霉病及灰霉病等 (Ma et al., 2010; Yang et al., 2008)。然而目前大黄素甲醚完全依赖大黄属 (Rheum) 植物的种植、采收与提取，存在产区与气候受限、生长与采收周期长、易受环境影响、关键成分含量低 (0.01%–0.2%) 且组成复杂等问题，导致其加工成本高昂、规模化困难，难以满足持续增长的市场需求 (Cai et al., 2004; Dai et al., 2018; Li et al., 2019)。

植物体内的次级代谢途径通常较为复杂且难以解析，主要原因是其生物合成基因不像微生物那样成簇分布；具体到本课题，大黄素及其衍生物在植物中的生物合成途径至今仍远未清晰，因此难以通过合成生物学策略在微生物中进行完整重构。
![Figure 1 原文第 2 页](https://synbiopath.online/ANV2VH9A-Figure-1-p2-1-2d9893d63ced1dbe.png)

*Figure 1：生产大黄素甲醚的两种替代策略示意图 (Fig. 1. Two alternative strategies for the production of the plant-derived fungicide physcion)（原文 PDF 截图）。*
Fig. 1 概括了大黄素甲醚生产的两种替代途径：Fig. 1A 为传统的大黄种植、采收、提取与结晶路径；Fig. 1B 为本研究提出的丝状真菌 A. terreus 细胞工厂路径——通过过表达转录激活因子 GedR 以激活 geodin BGC 中 gedC (PKS)、gedB (β-内酰胺酶型硫酯酶)、gedI (脱羧酶) 与 gedH (大黄素蒽酮氧化酶) 等基因的表达，并在 Module I 中敲除 gedA 以构建大黄素积累型细胞工厂，在 Module II 中过表达具备 C3 位区域选择性的 3-EOMT 以获得大黄素甲醚生产型细胞工厂。

微生物尤其是丝状真菌的次级代谢生物合成基因簇 (biosynthetic gene clusters, BGCs) 结构紧凑、遗传操作工具成熟，为植物源天然产物的微生物制造提供了可行替代路径 (Meng et al., 2022)。土曲霉 (Aspergillus terreus) 是工业级丝状真菌，已用于洛伐他汀与衣康酸的发酵生产 (Huang et al., 2021)，并且其体内 geodin 生物合成途径中 13 个假定基因的功能已通过生物信息学分析、体内基因敲除、异源重构及体外生化实验被基本完整阐明 (Awakawa et al., 2009; Nielsen et al., 2013; Qi et al., 2021; Schor and Cox, 2018)；其中关键的 C1-O-甲基转移酶 GedA 已由本课题组前期通过体外酶活实验证实即为长期寻找的 1-EOMT，负责将大黄素 C1 位羟基甲醚化为 questin (Xue et al., 2022)；此外 Nielsen 等人的工作亦表明 GedR 是激活 geodin BGC 基因表达的转录激活因子 (Nielsen et al., 2013)。基于此，本研究旨在 A. terreus 中通过过表达 GedR 激活 geodin BGC 以积累大黄素、敲除 gedA 阻断大黄素向 questin 的 C1 位甲基化支路、并通过生物信息学挖掘与体外酶活筛选获得具备 C3 位区域选择性的 3-EOMT，最终构建大黄素甲醚的微生物细胞工厂 (Fig. 1B)。

---

# 三、研究思路

本研究以"激活已知 BGC + 移除分支竞争 + 引入新型甲基化酶"的三步式合成生物学策略为主线 (Fig. 1B)：(1) 以 A. terreus HXN301-ΔpyrG (HXN301 的尿嘧啶营养缺陷型衍生株) 为出发株，通过同源重组将 PgpdAt 强组成型启动子驱动的 gedR 表达盒整合至染色体 *ku80* 位点，构建过表达株 OEgedR，以激活原本沉默的 geodin 途径，并通过代谢物谱变化验证；(2) 在 OEgedR 基础上同源重组敲除 *gedA*，阻断大黄素向 questin 的 C1 甲基化支路，构建大黄素积累型底盘 ΔgedA；(3) 通过基于结构相似性（蒽醌/黄酮/蒽环类）的多策略生物信息学筛选与基于 gedC (PKS) 和 gedA (OMT) 的 cluster blast 比对，从 24 个候选中预筛出 6 个 OMT 进行体外酶活表征，鉴定出对大黄素 C3 位具有完全区域选择性的 PtaI；进一步通过 gedA 位点的同源重组构建双向载体 (bifunctional vector)，将 PgedA-PtaI 表达盒一步整合至 ΔgedA 染色体内，同步实现 gedA 敲除与 3-EOMT 敲入，得到大黄素甲醚生产菌株 PgedA-PtaI（另平行构建 PgedA-MpOMT1A 与 PgedA-KNG44545 作为对照）；(4) 在 LPM 摇瓶与 100 L 两阶段补料分批发酵中评估效价，并通过胞内外分布测定指示下游分离可行性。

---

# 四、研究方法

- **真菌遗传操作**：采用 PEG 介导的原生质体转化 (Zhang et al., 2019)、pyrG 营养缺陷与 pyrithiamine 抗性筛选、同源重组与 Gateway BP Clonase II 构建敲除/敲入载体，并辅以 Phire Plant Direct PCR Kit 进行菌落 PCR 验证，用于 A. terreus 染色体编辑。
- **HPLC 与 LC-HRMS 分析**：使用 ThermoFisher Scientific C18 反相柱 (5 μm, 4.6 mm × 250 mm) 与线性梯度洗脱 (50% ACN 维持 1 min、19 min 内 50%–100% ACN、100% ACN 维持 5 min，0.1% TFA 水溶液为流动相，流速 1 mL/min)；LC-HRMS 在 Agilent 1290 Infinity II 与 6545 LC/Q-TOF 系统上完成，使用 Eclipse Plus C18 RRHD 柱 (2.1 × 50 mm) 与 0.05% 甲酸/乙腈-水梯度体系。
- **化合物分离与结构鉴定**：采用硅胶与 ODS 真空液相色谱、半制备 HPLC，结合 1D/2D NMR (Bruker AVANCE III 600, 600 MHz ¹H/150 MHz ¹³C)、UV (Beckman DU-800)、IR (Nicolet iN10)、ECD (JASCO J-815-150S)、旋光 (JASCO P-1020) 与 LC-HRMS，对 OEgedR 菌株中放大的次级代谢产物进行结构解析。
- **异源蛋白表达与体外酶活测定**：候选 3-EOMT 基因经 E. coli 密码子优化（部分如 PtaI 同时按 A. terreus 密码子偏好优化）后由 BGI Genomics 合成，克隆至 pET28b (Nde I/Xho I 或 Nco I/Hind III 位点)，转化 E. coli BL21(DE3) 经 0.2 mM IPTG、16 °C 诱导 20 h 表达，Ni-NTA 纯化得到 N 端 His6 标签重组蛋白；在 50 mM NaH₂PO₄ (pH 7.4) 反应缓冲液中以 5 μM (OsNOMT 10 μM) 蛋白、100 μM 大黄素、1 mM SAM 于 30 °C 孵育 8 h，以 HPLC 检测产物 physcion 并换算转化率。
- **补料分批发酵**：种子罐 10 L (装液量 6 L 改良种子培养基) 30 °C、150 rpm、1.6 vvm 培养 24 h 后，转入 100 L 主罐 (装液量 60 L 补料分批发酵培养基) 28 °C、120–180 rpm、0.5–1.0 vvm 控制溶氧 >30%，以 2.5 M 柠檬酸与 13 M 氨水控制 pH 6.0；初始糖耗尽后每日补 15 g/L 葡萄糖与 15 g/L 甘油，培养 14 d。
- **生物信息学候选筛选**：基于 antiSMASH/cluster blast 比对 (以 gedC、gedA 为探针) 结合文献调研从植物、链霉菌与真菌 OMT 中预筛 24 个候选 (Table S5，SI 未提供)，最终选定 6 个进行体外表征；其中包括 3 个具多重催化杂泛性的黄酮 7-OMT (SaOMT-2、OsNOMT、MpOMT1A)、1 个四并霉素 3-OMT TcmN 缺失 N 端 148 氨基酸的截短体 TcmN-149C，以及 cluster blast 命中的 6 个 OMT 中的代表性候选 KNG44545 与 PtaI。

---

# 五、实验设计及结果分析

### (一) geodin BGC 激活与 OEgedR 株次级代谢谱重构

#### 实验目的与设计逻辑

土曲霉 HXN301 是一株高产的 statin 生产菌 (Huang et al., 2016)，前期观察显示其体内 geodin 途径几乎沉默，仅可检测到痕量大黄素 (16) 与其 O-甲基化衍生物 questinol (4)，并伴有多种 statin 类产物 (Fig. 2A, trace i)。作者假设：若过表达 geodin BGC 的转录激活因子 GedR，可将乙酰辅酶 A 与丙二酰辅酶 A 的代谢流从 statin 途径分流至 geodin 途径，从而引发新代谢产物的产生。基于此，作者以 HXN301-ΔpyrG 为出发株，构建在 PgpdAt 强组成型启动子控制下于 *ku80* 位点整合额外 *gedR* 拷贝的 OEgedR 株 (Fig. 2B 与 Fig. S1)，并以 PDA 平板颜色与 LPM 摇瓶发酵提取物的 HPLC 谱对比验证 BGC 激活效果。

#### 实验结果与证据解析

在 28 °C、7 d 培养后，OEgedR 平板颜色明显加深 (Fig. S2)，提示有额外色素类次级代谢物产生。HPLC 在 250 nm 检测波长下显示 OEgedR 较 HXN301 出现大量新增色谱峰 (Fig. 2A, trace ii vs. i)，其中 trace i 中红箭头所指的为 statin 类峰，OEgedR 中 statin 峰显著减弱，与作者关于代谢流重分配的假设一致。
![Figure 2 原文第 5 页](https://synbiopath.online/ANV2VH9A-Figure-2-p5-1-2d3780f744222e41.png)

*Figure 2：geodin BGC 激活型 A. terreus 突变株的构建与表征 (Fig. 2. Construction and characterization of a geodin BGC-activated A. terreus mutant)（原文 PDF 截图）。*
Fig. 2A 直接说明 BGC 激活带来的代谢谱重构，Fig. 2B 给出 *ku80* 位点整合及 PgpdAt-*gedR* 表达盒构建示意图。

为解析这些新增化合物的结构，作者采用大规模发酵、硅胶与 ODS 真空液相色谱、半制备 HPLC 分离，结合 NMR 与 LC-HRMS，最终鉴定出 18 个化合物 (Fig. 2C)，包括 5 个二苯甲酮 (1, 2, 6, 10, 17)、7 个二苯醚 (3, 5, 7–9, 12, 13)、4 个蒽醌 (4, 11, 15, 16)、1 个 geodin (14) 与 1 个 geomycin D (18)，其中 1 与 15 为新化合物 (Tables S3–S4 与 Figs. S3–S19，SI 未提供)。该结果**实验直接证明** geodin BGC 已被全面激活，代谢流确实从 statin 转向 geodin 系列次级代谢物。然而 OEgedR 中大黄素 (16) 的量仍很低，作者据此提出"大黄素可被转化为 geodin 下游衍生物"的合理解释，但本文未直接测定中间代谢通量，属于作者推论而非本文给出的直接定量数据。

### (二) gedA 敲除与大黄素积累型底盘 ΔgedA 的构建

#### 实验目的与设计逻辑

OEgedR 中大黄素被持续转化是阻碍其作为大黄素甲醚前体供应底盘的主要原因。基于前期工作确认 GedA 即 1-EOMT (Xue et al., 2022)，作者假设：敲除 *gedA* 可阻断大黄素向 questin 的 C1 甲基化支路，使大黄素得以大量积累。基于此，作者采用同源重组策略将 *gedA* 替换为含 PgedA-Ttef 等元件的敲除盒，得到 ΔgedA 株 (Fig. 3A)，并通过 HPLC、LC-HRMS 验证大黄素积累。

#### 实验结果与证据解析

在 440 nm 检测波长下，ΔgedA 发酵提取物出现显著的橙色大黄素峰，保留时间与标准品 (trace iii) 一致，且 OEgedR 对照未观察到相应峰 (Fig. 3B 与 Fig. S20)。该结果**实验直接证明** *gedA* 缺失导致大黄素积累，与作者假设一致。在 LPM 摇瓶 8 d 培养的时程分析中，ΔgedA 大黄素效价在第 8 天达到 **1.71 g/L** 的峰值 (Fig. 3C)，三个独立生物学重复的误差棒显示重复性较好。
![Figure 3 原文第 6 页](https://synbiopath.online/ANV2VH9A-Figure-3-p6-1-978bbcce19a14d92.png)

*Figure 3：大黄素积累型 A. terreus 细胞工厂的构建与分析 (Fig. 3. Construction and analysis of the emodin-accumulating A. terreus cell factory)（原文 PDF 截图）。*
Fig. 3A 给出 ΔgedA 敲除策略示意图，Fig. 3B–C 共同支撑"ΔgedA 是高效大黄素积累底盘"这一结论。作者进一步将 ΔgedA 与文献报道的工程化酿酒酵母 (528.4 mg/L、5 L 罐 5 d) 及野生 *Aspergillus ochraceus* (干重 0.8%) 比较 (Ping Lu and Cui, 2010; Sun et al., 2019)，认为 ΔgedA 的大黄素生产水平更高。需注意的是，该比较的发酵时间、培养基与反应器规模并不一致，应理解为作者提出的相对优势判断而非严格基准比较。

Fig. 3D 显示 ΔgedA 发酵产物中大黄素胞内分布达 99.71%、胞外仅 0.29%，意味着下游分离可主要通过菌体收集与破壁完成。这一性质对工业生产具有重要工程意义，因为大量胞外分泌往往伴随复杂的发酵液杂质。综上，ΔgedA 是一个兼具高产量与可分离性的大黄素底盘。

### (三) 候选 3-EOMT 的生物信息学筛选与体外功能表征

#### 实验目的与设计逻辑

大黄素 C3 位甲基化在大黄属植物中已有报道，但其催化酶尚不明确。作者以多策略生物信息学方法从公开数据库和文献中筛选可能具有 C3 位选择性的 OMT：

(1) 基于蒽醌、黄酮、蒽环类结构相似性，纳入 3 个具有多重催化杂泛性的黄酮 7-OMT：链霉菌 *Streptomyces avermitilis* 来源 SaOMT-2 (Kim et al., 2006)、水稻 *Oryza sativa* 来源 OsNOMT (Shimizu et al., 2012)、薄荷 *Mentha × piperita* 来源 MpOMT1A (Willits et al., 2004)；

(2) 纳入缺失 N 端 148 氨基酸 (芳香化酶/环化酶结构域) 的四并霉素 3-OMT TcmN 截短体 TcmN-149C (Fu et al., 1996; Ames et al., 2008)；

(3) 以 *gedC* (PKS) 与 *gedA* (OMT) 为探针进行 cluster blast (Medema et al., 2011)，获得 4 个相似 BGC 中的 6 个 OMT，包括 viridicatumtoxin BGC 中的 VrtF、灰黄霉素 BGC 的 GsfB (Chooi et al., 2010)、番茄匍柄霉 *Stemphylium lycopersici* 来源 KNG44545 与 KNG44549 (Li et al., 2017)，以及植物内生真菌拟盘多毛孢 *Pestalotiopsis fici* pestheic acid BGC 中的 PtaI 与 PtaH (Xu et al., 2014)；随后经系统发育树分析锁定最可能的 3-EOMT 候选 KNG44545 与 PtaI。

经过预筛共获 24 个候选 (Table S5，SI 未提供)，最终作者选择其中 6 个进行体外表征。

#### 实验结果与证据解析

作者将 6 个候选 OMT 在 E. coli BL21(DE3) 中表达 (PtaI 同时按 A. terreus 密码子偏好优化)，经 Ni-NTA 纯化后 SDS–PAGE 显示除 KNG44545 因易沉淀导致收率偏低外，其余纯度均 >95% (Fig. S22，SI 未提供)。在 5 μM (OsNOMT 10 μM) 蛋白、100 μM 大黄素、1 mM SAM 的标准反应中于 30 °C 孵育 8 h，HPLC 检测产物 physcion (Fig. 4A)。对照 (trace i) 不含酶，trace viii/ix 分别为大黄素与 physcion 标准品。
![Figure 4 原文第 7 页](https://synbiopath.online/ANV2VH9A-Figure-4-p7-1-def1eb4500a38c2e.png)

*Figure 4：候选 3-EOMT 的体外筛选与功能表征 (Fig. 4. Screening and functional characterization of putative 3-EOMTs)（原文 PDF 截图）。*
Fig. 4A 的 9 条 trace 完整展示了"缺酶对照–6 个候选酶–2 个标准品"的体外反应体系，并通过保留时间一致性与 LC-HRMS 共同支持产物为 physcion；Fig. 4B 量化了 6 个候选的转化率 (三次独立生物学重复)。

结果显示 PtaI 表现出最高的催化效率，达到 **87.3%**，远高于 MpOMT1A (61.4%)、TcmN-149C (34.9%)、SaOMT-2 (32.7%)；KNG44545 与 OsNOMT 转化率较低 (Fig. 4B 柱形上方分别标注 5.7% 与 3.1%)。该结果**实验直接证明** PtaI 是对大黄素最有效的 C3 区域选择性 OMT。Fig. 4B 图注本身将"PtaI 的优势"归因于更高的底物偏好 (substrate preference)，但 K<sub>m</sub>、k<sub>cat</sub>、底物谱等动力学参数未在正文中给出，因此"底物偏好更高"为作者基于转化率的合理推论而非直接酶动力学证据。同时所有 6 个酶在体外均表现为对 C3 位的完全区域选择性，无 C1 位或其他位点的甲基化产物被检测到，这一区域选择性证据具有较强的可重复性。

### (四) 大黄素甲醚生产菌株 PgedA-PtaI 的构建与摇瓶验证

#### 实验目的与设计逻辑

基于 ΔgedA 大黄素积累底盘与 PtaI 的最佳体外活性，作者假设：将 PtaI 在 ΔgedA 株中以 PgedA 启动子驱动并整合至 *gedA* 染色体内，可同步实现 *gedA* 缺失与 3-EOMT 表达，从而构建大黄素甲醚生产菌 PgedA-PtaI。为对比，作者同时构建了 PgedA-MpOMT1A 与 PgedA-KNG44545 株。

#### 实验结果与证据解析

作者采用双向载体 (bifunctional vectors)，在 *gedA* 上游/下游同源臂之间整合 PgedA-PtaI/MpOMT1A/KNG44545 表达盒 (Fig. 5A)。HPLC 在 440 nm 检测下显示 PgedA-PtaI 出现显著的绿色 physcion 峰 (trace v)，保留时间与标准品 (trace vii) 一致；同时仍可检测到少量大黄素 (trace v、Fig. S23)，表明大黄素未被完全转化 (Fig. 5B)。
![Figure 5 原文第 7 页](https://synbiopath.online/ANV2VH9A-Figure-5-p7-1-b603eed8ce354ba8.png)

*Figure 5：大黄素甲醚生产型 A. terreus 细胞工厂的构建与分析 (Fig. 5. Construction and analysis of the physcion-producing A. terreus cell factory)（原文 PDF 截图）。*
Fig. 5A 给出 *gedA* 位点 3-EOMT 敲入策略示意图，Fig. 5B 直观对比了 OEgedR (trace i)、ΔgedA (trace ii)、PgedA-KNG44545 (trace iii)、PgedA-MpOMT1A (trace iv) 与 PgedA-PtaI (trace v)，说明只有 PtaI 的引入带来了显著的 physcion 积累；同时 PgedA-MpOMT1A 中仅检测到痕量 physcion，PgedA-KNG44545 中未检出 physcion，与体外活性差异一致 (Fig. 5B, traces iii–iv)。

摇瓶 8 d 时程分析显示 PgedA-PtaI 的 physcion 效价达 **1.74 g/L**，而大黄素残余为 **0.23 g/L** (Fig. 5C)。大黄素残余提示 PtaI 在体内的活性或表达量可能尚不足以完全消耗大黄素。Fig. 5C 同时显示摇瓶 8 d 时大黄素仍持续被缓慢消耗，提示延长发酵时间或强化 PtaI 表达有望进一步降低残余。Fig. 5D 显示 physcion 在胞内的效价 (1.74 g/L) 远高于胞外 (0.016 g/L)，与 ΔgedA 中大黄素的胞内积累 (99.71%) 趋势一致，再次提示下游分离应以菌体为主要处理对象。

### (五) 100 L 补料分批发酵与工艺验证

#### 实验目的与设计逻辑

为验证 PgedA-PtaI 在工业级规模下的稳健性与产率上限，并展示该细胞工厂的商业化潜力，作者开展了 100 L 规模的两阶段补料分批发酵 (10 L 种子罐 + 100 L 主罐)。

#### 实验结果与证据解析

种子罐 (10 L、6 L 改良种子培养基) 30 °C、150 rpm、1.6 vvm 培养 24 h 后转入 100 L 主罐 (60 L 补料分批发酵培养基)，28 °C、120–180 rpm、0.5–1.0 vvm 控制溶氧 >30%，以 2.5 M 柠檬酸与 13 M 氨水控制 pH 6.0；初始糖耗尽后每日补 15 g/L 葡萄糖与 15 g/L 甘油。**physcion 在第 1 天即可被检出**，与菌体良好生长相伴；最佳颗粒状菌丝形态在第 4 天形成，有利于丝状真菌次级代谢物合成；初始葡萄糖供应在第 6 天耗尽后启动补料。
![Figure 6 原文第 8 页](https://synbiopath.online/ANV2VH9A-Figure-6-p8-1-063e57994b596142.png)

*Figure 6：PgedA-PtaI 菌株在 100 升生物反应器中补料分批发酵的产量曲线 (Fig. 6. Time courses of emodin and physcion production during fed-batch fermentation of the PgedA-PtaI variant in a 100-litre bioreactor)（原文 PDF 截图）。*
Fig. 6 显示，在 14 d 的补料分批发酵中 physcion 效价持续上升，第 14 天达到 **6.3 g/L**，是摇瓶效价的 **3.6 倍**；同时大黄素积累 **1.75 g/L** (Fig. 6)。三个相同重复的误差棒说明结果具有较好的可重复性。

该结果**实验直接证明** PgedA-PtaI 在工业规模上能够实现大黄素甲醚的稳定发酵生产，是本文的核心定量结论之一。需要注意的是，发酵液中除目标产物外仍残留大黄素、statin 与其他未鉴定副产物，作者在讨论部分将其作为后续工艺改进的重要切入点。

---

# 六、总体结论

本研究在土曲霉 HXN301 中通过合成生物学重构策略，首次实现了植物源杀菌剂大黄素甲醚的微生物全发酵生产。作者**将原本沉默的 geodin BGC 通过过表达转录激活因子 GedR 成功激活**，并通过同源重组敲除 *gedA* 构建了大黄素效价达 1.71 g/L 的 ΔgedA 积累型底盘；进一步通过生物信息学挖掘与体外酶活筛选，**鉴定出对大黄素 C3 位具有完全区域选择性、转化率达 87.3% 的 O-甲基转移酶 PtaI**，并将其一步整合至 ΔgedA 染色体内获得大黄素甲醚生产菌 PgedA-PtaI；摇瓶效价达 1.74 g/L，100 L 补料分批发酵效价达 **6.3 g/L**，为迄今报道的大黄素及其衍生物微生物生产最高水平。文中所构建的 ΔgedA 与 PgedA-PtaI 底盘为后续生产大黄酸 (rhein)、芦荟大黄素 (aloe-emodin)、 chrysophanol、糖苷化衍生物 (emodin-8-O-β-D-glucoside、physcion-8-O-β-D-glucopyranoside) 与 hypericin 等系列蒽醌化合物提供了可拓展的工程平台；同时"激活已知 BGC 合成上游前体 + 生物信息学挖掘合成下游终产物"的"化合物导向"而非"全途径重构"的微生物合成思路，为难以完整解析的植物源天然产物制造提供了新范式。**作者最终建立了一套在丝状真菌中以大黄素为节点高效合成大黄素甲醚的细胞工厂，并验证其具备工业级生产可行性**。

---

# 七、论文评价

### 优点与创新

本文最突出的创新在于将"激活已知微生物 BGC 合成上游中间体"与"生物信息学/酶学筛选下游修饰酶"两条互补路线整合在同一株工业丝状真菌中，从而绕开了植物体内大黄素甲醚生物合成途径尚未完整解析、难以异源重构的瓶颈。这种"化合物导向"的微生物合成思路对于以大黄 (Rhubarb) 为代表的多种药用植物成分的微生物制造具有方法学上的借鉴意义。从证据链完整性看，作者在 PtaI 的功能表征中同时提供了体外反应 (Fig. 4)、体内表达 (Fig. 5) 与 100 L 规模发酵 (Fig. 6) 三层正交证据，使"PtaI 足以在体内将大黄素转化为大黄素甲醚"这一核心结论具有较强可信度。

### 未来研究方向

最优先的后续工作是阻断大黄素向 statin 与其他未知副产物的代谢分流。发酵液中 statin 与 1.75 g/L 大黄素的存在表明 acetyl-CoA/malonyl-CoA 供应或 3-EOMT 活性尚未达到最优。建议通过 (1) 引入额外 PtaI 拷贝或更换更高活性的 3-EOMT 以提高大黄素转化率；(2) 敲除 statin 途径关键聚酮合酶 LovB 以增加前体供给并简化下游分离；同时辅以发酵参数的系统优化与产物胞外分泌机制的探索，以进一步推高效价并降低工业成本。

---

# 八、关键问题及回答

**Q1：在 ΔgedA 中观察到大黄素积累，是否充分证明 *gedA* 是 OEgedR 株中大黄素消耗的唯一原因？**

A：尚不充分。敲除 *gedA* 显著提高大黄素效价 (从痕量到 1.71 g/L) **支持** GedA 是 C1 甲基化的关键酶，但该结果未排除 OEgedR 株中可能存在其他低活性酶或非酶途径参与大黄素转化，且无法区分"必要性"与"充分性"。若在 ΔgedA 中进一步回补 *gedA* 并观察到 questin 恢复积累，将构成对必要性更强的因果证据。

**Q2：体外活性最高的 PtaI (87.3%) 为何在体内仅将大黄素部分转化 (0.23 g/L 残余)？**

A：体外与体内活性差异可能源于 (1) PtaI 在 A. terreus 中的表达水平与折叠效率有限；(2) 体内 SAM 浓度、pH、底物可及性等微环境与体外反应缓冲液不同；(3) 大黄素在细胞器或隔室中的区隔分布可能限制酶-底物接触。Fig. 5C 显示摇瓶 8 d 时大黄素仍持续被缓慢消耗，提示延长发酵时间或强化 PtaI 表达有望进一步降低残余。该结论为作者提出的合理推论，需通过蛋白定量、亚细胞定位或增加 PtaI 拷贝数的对照实验加以验证。

**Q3：本研究是否充分证明了 PgedA-PtaI 株中的大黄素甲醚完全来源于 PtaI 催化而非其他宿主酶？**

A：体外反应中 PtaI 对大黄素 C3 位的完全区域选择性 (Fig. 4) 与 ΔgedA/PgedA-KNG44545 体内几乎检测不到 physcion 的事实 (Fig. 5B) 共同支持 PtaI 是 PgedA-PtaI 株中大黄素甲醚形成的关键酶，但严格的"完全来源"证据仍需 PtaI 失活突变对照 (例如在 PgedA-PtaI 基础上再次敲除 PtaI) 来排除 A. terreus 内源酶或非酶甲基化的潜在贡献。

> 分类状态：待全部文献笔记完成后统一分类归档。
