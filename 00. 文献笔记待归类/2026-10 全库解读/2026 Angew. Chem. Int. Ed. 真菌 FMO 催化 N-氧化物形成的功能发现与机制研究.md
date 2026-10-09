---
type: literature-reading
zotero_key: 52KLS4JN
doi: "10.1002/anie.9391687"
paper_type: research
classification_status: pending
reading_status: main-text-and-figures-read
review_status: model-source-crosschecked
human_full_paper_review: false
source_attachment: KBMPX297
source_sha256: f2c9263811f238be8ade347342b5d75384020f9d701a2c7d65e20654f15716ef
created: 2026-10-07
---

> 原文来源：[Zotero 条目](zotero://select/library/items/52KLS4JN)；[DOI](https://doi.org/10.1002/anie.9391687)；主文与图表已按来源进行模型交叉核对，尚未经人工逐项复核。 来源限制：Supporting Information 全文未提供,所有以 Figure S* 引用的子图(SI 图 S1A/B、S2A/B、S4–S39、S6A–C 时程、S7–S16 NMR、S17–S18 同位素与动力学、S19–S20 系统发育、S21–S32 新化合物 NMR、S33–S39 结构与突变补充等)只能依据正文叙述引用,无法核对原始谱图细节；ΔpldC 突变体的 LC-HRMS 图(C 部分,4 张化合物 1–4 谱图)以及 Figure 2C 各 [M+H]+ 峰标注(化合物 1: 350.1942 / 368.1943,化合物 2: 336.2051,化合物 3: 352.1998,化合物 4: 368.1936)只能援引正文 [M+H]+ 数值,无法独立确认峰位图；Figure 4H 柱状图仅以 'Data are presented as mean ± SD from three independent replicates' 给出,各柱精确数值未在正文列出；AlphaFold3 + 分子对接得到的 PldC-FAD-2/3 复合物模型属于计算预测,缺乏高分辨率含配体晶体结构直接验证；PldC 自身晶体结构(PDB: 26WF,3.5 Å)中 FAD 与底物无可解释电子密度,故活性位点残基编号定位主要依赖 CtdE(PDB: 7KPT)同源建模与对接。

# 一、基本信息

**文章题目**：Discovery and Characterization of Conserved N-Oxide-Forming Function of FAD-Dependent Monooxygenases for Fungal Prenylated Indole Alkaloid Biosynthesis(真菌异戊烯基吲哚生物碱生物合成中 FAD 依赖单加氧酶保守 N-氧化物形成功能的发现与表征)

**文章 DOI 号**：10.1002/anie.9391687

**期刊名称**：Angewandte Chemie International Edition

**通讯作者及工作单位**：

- **Wei Zhang (张卫)**：中国科学院海洋研究所 实验海洋生物学实验室 / 海洋生物多样性与生物资源可持续利用山东省重点实验室 (Laboratory of Experimental Marine Biology, Shandong Province Key Laboratory of Marine Biodiversity and Bio-resource Sustainable Utilization, Institute of Oceanology, Chinese Academy of Sciences, Qingdao, China)

**其他主要合作单位**：山东大学微生物技术国家重点实验室;中国科学院大学;厦门大学药学院福建省创新药物靶点研究重点实验室;青岛海洋科学与技术中心海洋生物学与生物技术实验室。

---

# 二、研究背景

N-氧化物 (R<sub>3</sub>N<sup>+</sup>–O<sup>−</sup>) 是天然产物中广泛存在的药效团兼结构单元,极性共价 N─O 键赋予其增强水溶性、改善膜通透性、调控受体结合等多重生物功能,在植物源 N-络合物中常作为"前体毒素"抵御食草动物,在微生物中参与生态位竞争。然而,N-氧化物生物合成及其酶学机制研究长期滞后,目前在哺乳动物、植物和细菌中仅明确了三类酶:植物 GAME33/34 等非血红素双铁酶、细菌 AurF/CmlI 双铁氧化酶、CYP71/CYP80 等细胞色素 P450,以及 FMO(Class A 黄素依赖单加氧酶,以哺乳动物 FMO3、细菌 Tmm 和植物 SNO 为代表)。Class A FMO 共有的 Rossmann-like ββα 折叠 (CATH 3.50.50.60) 与 D-氨基酸氧化酶折叠 (CATH 3.30.9.10) 是其结构基础。


![Figure 1 原文第 2 页](https://synbiopath.online/52KLS4JN-Figure-1-p2-1-c3616f5f1392f3d0.png)

*Figure 1：(A) 含有 N-杂环氧化的药物分子;(B) 具有 N─O 配位键的代表性真菌异戊烯基吲哚生物碱 (PIAs)。（原文 PDF 截图）。*


真菌异戊烯基吲哚生物碱 (prenylated indole alkaloids, PIAs) 是最大天然产物家族之一,其中部分化合物(如 VM55596、(–)-mangrovamide B、sclerotiamide G)含有 N─O 配位键,但负责该化学转化的酶与机制长期未被阐明。作者从深海来源 *Pallidocercospora* sp. ADS-F95 中分离得到六种 penicimutamides,发现 penicimutamide C N-oxide (1) 同时具有 N─O 配位键和 3-羟基吲哚烯胺 (3-hydroxyindolenine) 基团,但缺少 bicyclo[2.2.2]diazaoctane (BCDO) 骨架,为研究 PIA 中 N-氧化物生物合成与 3-羟基吲哚烯胺基团形成提供了理想分子探针。

---

# 三、研究思路

作者的整体研究路线为:化合物 1 的发现与结构解析 → 通过同源 NRPS 基因 *malG* 探针定位候选生物合成基因簇 (BGC, 命名为 *pld*) → 通过 *ΔpldH* 和 *ΔpldC* 基因敲除验证 BGC 功能并锁定关键 FMO 候选 PldC → 在 *E. coli* 中异源表达并纯化 PldC 蛋白 → 体外酶促反应重构 2→3→4 顺序转化路径并通过 LC-HRMS、NMR、DP4+、电子圆二色谱 (ECD) 鉴定中间体 3 和新化合物 4 → 通过 <sup>18</sup>O<sub>2</sub> / H<sub>2</sub><sup>18</sup>O 同位素示踪和 Michaelis-Menten 动力学分析确立 PldC 的双功能属性 → 在 PldC 同源酶 CtdE (citrinadin 途径) 和 PhqK (paraherquamide 途径) 中检验 N-氧化物形成活性的保守性 → 通过 X 射线晶体学、AlphaFold3 与分子对接构建活性位点模型并用定点突变验证残基功能。

整个研究形成"化合物发现 → BGC 鉴定 → 体外酶学重构 → 同源酶功能比较 → 结构与机制确证"的完整闭环。

---

# 四、研究方法

- **生物信息学与 BGC 挖掘**：以已知 PIA 生物合成 NRPS 基因 *malG* 为探针在 *Pallidocercospora* sp. ADS-F95 基因组中定位候选 BGC *pld*,结合 BLAST 同源比对与系统发育分析(Figure S4,Table S2)确认 FMO 候选 PldC。
- **基因敲除验证**：采用 split-marker 同源重组策略构建 *ΔpldH* 和 *ΔpldC* 框内缺失突变株,通过 HPLC 和 LC-HRMS 比较野生型与突变株代谢谱变化(Figure 2B,C)。
- **异源表达与蛋白纯化**：将密码子优化后的 *pldC* 在 *E. coli* BL21(DE3) 中表达,通过 Ni-NTA 等方法纯化,紫外可见光谱表征 FAD 结合(Figure S5)。
- **体外酶促反应与产物鉴定**：以纯化 PldC 与底物 2、3、9 及 NADPH/FAD 在体外孵育,通过 HPLC(λ = 280 nm)监测反应,LC-HRMS 测定精确质量,1D/2D NMR(结合 DP4+ 概率计算与 ECD)确证化合物 3、4、8、9 结构;时程实验(Figure S6A)用于判别反应顺序。
- **同位素示踪**：以 <sup>18</sup>O<sub>2</sub> 气氛或 H<sub>2</sub><sup>18</sup>O 缓冲液进行 PldC / PhqK 反应,根据产物分子量偏移确定氧来源(Figure S17,S33)。
- **酶动力学**：对 PldC 以底物 2 和 3 进行 Michaelis-Menten 分析,计算 *k*<sub>cat</sub>/*K*<sub>M</sub>(Figure S18,正文报告数值)。
- **化学衍生化验证**：通过本课题组前期开发的温和铟介导 N─O 还原裂解反应验证 N-氧化物结构(Figure S6B,C)。
- **X 射线晶体学与计算结构**：测定 PldC 自身晶体结构(PDB: 26WF,3.5 Å)以及化合物 8 的单晶结构(CCDC 2521192);以 CtdE 结构 (PDB: 7KPT) 为模板,用 AlphaFold3 与分子对接构建 PldC–FAD–2/3 复合物模型,辅以分子动力学(MD)模拟。
- **定点突变与活性比较**：对 PldC 的 G61、T196、M225、M234、N249、I404、V405、D58、R120 以及 CtdE 对应残基构建突变体,通过相对产率比较(Figure 3C,D,4H,Figure S38)评估各残基对 C-氧化与 N-氧化的贡献。

---

# 五、实验设计及结果分析

### (一) Penicimutamide C N-oxide 的发现与生物合成基因簇 (*pld*) 鉴定

### 实验目的与设计逻辑

作者从 *Pallidocercospora* sp. ADS-F95 培养物中分离得到六个 penicimutamides(Figure S1A),其中 1 同时具有 N─O 配位键和 3-羟基吲哚烯胺基团,但缺少 bicyclo[2.2.2]diazaoctane (BCDO) 骨架。这一结构特征为研究 PIA 中 N-氧化物形成与 3-羟基吲哚烯胺基团起源提供了独特切入点。作者利用已知 PIA 途径 NRPS 基因 *malG* 作为探针,在 ADS-F95 基因组中检索同源区域,以定位候选 BGC。

### 实验结果与证据解析


![Figure 2 原文第 3 页](https://synbiopath.online/52KLS4JN-Figure-2-p3-1-ae42eea650126b42.png)

*Figure 2：Penicimutamide 的化学结构、基因簇组成与拟议生物合成途径。(A) pld (Pallidocercospora sp. ADS-F95)、ctd (Penicillium citrinum ATCC 9849) 和 mal (Malbranchea aurantiaca RRC1813) 的 BGC 比较分析;(B) 野生型及 ΔpldH、ΔpldC 敲除株 HPLC 谱图 (λ=280 nm);(C) 正离子 ESI+ 模式 LC-HRMS 谱图;(D) Penicimutamides 的拟议生物合成途径。（原文 PDF 截图）。*


候选 *pld* BGC 包含 NRPS、PT(prenyltransferase)、FMO、SDR 和 NmrA-like 等基因(Figure 2A),与 citrinadin 途径的 *ctd* BGC 和 malbrancheamide 途径的 *mal* BGC 存在明显共线性区域(Figure 2A)。为实验验证 *pld* 参与 1 的生物合成,作者用 split-marker 重组策略框内缺失 NRPS *pldH*,得到 Δ*pldH* 突变株。HPLC(λ = 280 nm)分析显示 1 及其他 penicimutamides 在 Δ*pldH* 中完全消失(Figure 2B),说明 *pld* 簇负责 penicimutamides 的生物合成。同时 Δ*pldC* 突变株中 1 消失,但积累一个主要新产物,经 LC-HRMS 鉴定 [M+H]<sup>+</sup> *obsd.* 336.2051, *calcd.* 336.2070,确认为 penicimutamide E (2)(Figure 2B,C)。该结果直接表明 PldC 是 BCDO 骨架形成后负责吲哚环氧化的候选酶(Figure 2D),但 Δ*pldC* 中未直接观察到 3-羟基吲哚烯胺或 N-氧化物中间体,提示这些步骤快速进行或在 *pldC* 缺失时被绕开。

基于此,作者建立了一个拟议途径:PldH 催化 L-Pro–L-Trp 二肽环化;PldB(PT)催化 DMAPP 引入;CtdE/PhqK 同源的 FMO PldC 负责吲哚 2,3-环氧化;三个 NmrA-like 蛋白 PldJ/PldE/PldK 形成 BCDO 骨架(Figure 2D)。该途径以 2 为中心中间体,与已知 malbrancheamide、citrinadin、paraherquamide 途径共用早期步骤。

---

### (二) PldC 的体外生化表征:双功能 FMO 催化 3-羟基吲哚和 N-氧化物形成

### 实验目的与设计逻辑

Δ*pldC* 表型表明 PldC 在 2 转化为 1 的过程中发挥关键作用,但其分子功能(单一环氧化 vs 顺序氧化)尚不明确。作者在 *E. coli* 中异源表达并纯化 PldC,通过体外酶促反应与时程分析直接验证 PldC 催化活性并解析反应顺序。

### 实验结果与证据解析


![Figure 3 原文第 4 页](https://synbiopath.online/52KLS4JN-Figure-3-p4-1-8bdc404c1473cfe8.png)

*Figure 3：PldC、CtdE 和 PhqK 的比较功能表征。(A) 三酶介导的拟议生物合成途径;(B, D) PldC、CtdE、PhqK 及其突变体以不同底物 (2、3、9) 进行体外反应的 HPLC 分析(280 nm)。（原文 PDF 截图）。*


纯化的 PldC 呈亮黄色,FAD 分析证实其结合 FAD 辅因子(Figure S5)。当底物 2 与 PldC、NADPH、FAD 共同孵育时,HPLC 检测到 P1 和 P2 两个产物(Figure 3B, trace ii)。时程分析(Figure S6A)显示 P1 先积累,随后转化为 P2;将纯化 P1 重新与 PldC 孵育可高效生成 P2(Figure 3B, trace iii),**直接证明 P1 是 P2 形成过程中的 en route 中间体**,从而确立严格的 2→P1→P2 顺序途径。

P1 经 LC-HRMS([M+H]<sup>+</sup> *obsd.* 352.1998, *calcd.* 352.2020,Figure S7,S8)、1D/2D NMR(Figure S9,S10,Table S7)以及 ECD(Figure S11)联合表征被鉴定为 3*S*-羟基吲哚烯胺 penicimutamide D (3);P2 质量较 3 增加 16 Da([M+H]<sup>+</sup> *obsd.* 368.1936, *calcd.* 368.1969,Figure S8),经 NMR(Figure S12–S16,Table S8)确认为含 N13 处 N─O 配位键的新化合物 penicimutamide D N-oxide (4),并经本课题组开发的铟介导 N─O 还原裂解反应(Figure S6B)进一步验证 N-氧化物结构。

作者通过同位素标记实验确定氧来源。在 <sup>18</sup>O<sub>2</sub> 条件下,PldC 催化 2 生成 3 的分子量增加 2 Da,生成 4 时分子量增加 4 Da;而在 H<sub>2</sub><sup>18</sup>O 缓冲液中两个产物均未出现质量位移(Figure S17),**证明两个氧化步骤的氧原子均来源于 O<sub>2</sub>**,符合 FMO 催化特征。重要的是,HPLC 与 LC-HRMS 均未检测到 2 直接 N13-氧化的产物,**表明反应严格遵循 2→3→4 的酶控顺序途径**。

Michaelis-Menten 动力学分析进一步揭示 2 是 PldC 羟基化的优选底物,*k*<sub>cat</sub>/*K*<sub>M</sub> = 1.1 ± 0.2 min<sup>-1</sup> M<sup>-1</sup>,较 3(*k*<sub>cat</sub>/*K*<sub>M</sub> = 2.2 ± 0.6 min<sup>-1</sup> mM<sup>-1</sup>)高约 500 倍(Figure S18);这一显著差异在数值上支持"2 完全消耗后 3 才积累"的时程观察,**直接确立了 PldC 作为双功能酶催化顺序氧化反应**。

---

### (三) 同源 FMO(CtdE 和 PhqK)N-氧化活性的保守性

### 实验目的与设计逻辑

CtdE 已知催化 (+)-precitrinadin A 的吲哚 2,3-环氧化生成 3*S*-螺氧吲哚 citrinadin-5;PhqK 则在 paraherquamide 生物合成中介导两条平行螺环化路径。它们的天然底物分别与 2 仅在 C20-α 侧环 S-甲基取代或吡咯烷/哌啶酸环上存在差异(Figure S2A,S20,S26),但整体骨架同属 MKP 型 PIA。作者据此推测 CtdE 和 PhqK 可能识别 2 / 3,并通过体外反应检验 N-氧化活性是否在该 FMO 家族中保守。

### 实验结果与证据解析



将 CtdE 与 2 共同孵育生成新产物 8([M+H]<sup>+</sup> *obsd.* 352.2033, *calcd.* 352.2020,Figure 3B trace v,Figure S5,S6),其保留时间和 UV 谱图与 3、4 显著不同。1D/2D NMR(Figure S21–S25,Table S9)确证 8 为含 3*S*-螺氧吲哚基团的新化合物 penicimutamide F,**该结构由单晶 X 射线衍射进一步直接确证(CCDC 2521192,Table S3)**,绝对构型被唯一指认为 3*S*。值得注意的是,**CtdE 不能直接将 2 N-氧化,但能将 3 转化为痕量的 N-氧化物 4**(Figure 3B trace vi),表明 CtdE 同样具备 N-氧化潜力,但活性远低于其 C-氧化活性。

PhqK 与 2 孵育得到新产物 9(Figure 3B trace vii),1D/2D NMR(Figure S27–S32,Table S10)与铟介导 N─O 还原(Figure S6C)共同证明其含有 N13 处 N─O 配位键,被命名为 penicimutamide E N-oxide (9);<sup>18</sup>O<sub>2</sub> 标记实验(Figure S33)进一步证实其 N-氧化物氧源自 O<sub>2</sub>,与 FMO 催化特性一致。然而 PhqK 不能以 3 为底物生成任何产物。

以上三组体外实验共同表明,CtdE 和 PhqK 除原有 C-氧化活性外,还具备此前未识别的 N-氧化能力(Figure 3A)。CtdE 通过"先 C-氧化再微弱 N-氧化"运作,PhqK 则绕过 3-羟基吲哚烯胺中间体直接对 2 进行 N13-氧化,呈现出与 PldC 不同的底物谱和反应路径。

---

### (四) 结构生物学解析催化功能分化的分子基础

### 实验目的与设计逻辑

PldC 与 CtdE、PhqK 属于同一 Class A FMO 亚家族却展现出 C-氧化与 N-氧化不同偏好。作者通过晶体学、AlphaFold3 建模、分子对接与定点突变,试图揭示催化功能分化的结构基础。

### 实验结果与证据解析


![Figure 4 原文第 6 页](https://synbiopath.online/52KLS4JN-Figure-4-p6-1-e77ed3388ee52384.png)

*Figure 4：PldC 与 CtdE 功能分化的结构与机制基础。(A) PldC(天蓝色)和 CtdE(鲑红色)中底物 2 的结合构象比较,分别朝向 α-面(橙色)和 β-面(绿色)环氧化;(B) PldC–FAD–2 复合物(FAD 黄色);(C) PldC 与 CtdE 中底物 2(β-面取向)的二维相互作用图;(D) CtdE–FAD–2 活性位点视图;(E, F) PldC 活性位点内底物 2(橙色)与羟基化产物 3(石板蓝)的叠加结合构象;(G) PhqK(水绿色)中底物 2 的结合模式;(H) PldC 及突变体孵育 2 的相对产率分析(三次独立重复 mean ± SD)。（原文 PDF 截图）。*


PldC 自身晶体结构分辨率为 3.5 Å(PDB: 26WF),但 FAD 和底物的电子密度不可解释(Figure S34)。鉴于 PldC 与 CtdE 序列和底物高度相似(序列相似性/一致性 72.4%/47.0% 与 CtdE、63.0%/34.7% 与 PhqK,Figure S19,Table S2),作者以 CtdE 结构(PDB: 7KPT)为模板,使用 AlphaFold3 与分子对接构建 PldC–FAD–2/3 和 CtdE–FAD–2/3 复合物模型(Figure S35)。两蛋白共享典型的 Rossmann-like 三层 ββα 夹心结构域(用于 FAD 结合)以及富含 β 折叠的底物结合结构域,与 Class A FMO 拓扑一致。底物结合空腔富集疏水残基,有利于稳定嵌入吲哚环。

活性位点 5 Å 范围内共鉴定出 17 个残基,其中 10 个保守,7 个分歧(G61、T196、M225、M234、N249、I404、V405 在 PldC;对应 S63、I198、L227、T236、G251、M404、I405 在 CtdE,Figure S35)。其中 T196、M234、N249 推测与底物 2 的吲哚单元相互作用,G61、M225、I404、V405 紧邻 BCDO 环;**这些相互作用将底物 2 的 C2─C3 吲哚环锁定于距 FAD C4α 原子 5.5 Å 处,适合氧化反应进行**。

关键结构差异在于 FAD 相对于底物 2 的空间取向:**PldC 中 FAD 位于底物 2 的 α-面,驱动生成 3*S*-羟基吲哚烯胺**(Figure 4A,B);**而 CtdE 中 FAD 占据 β-面,驱动生成 3*S*-螺氧吲哚**(Figure 4A,C,D,S36)。α/β 面的差异由此决定了 C2–C3 双键环氧化与 N13 氧化的化学路径分支。

3 的 3-OH 是 PldC 与 CtdE 后续 N-氧化的先决条件。建模与 MD 模拟显示,3 相对于 2 在活性位点中向上偏移,可能由 C3-OH 和 C20-酮基分别与 G334 和 P331 形成氢键所致(Figure 4E,F);这一位移使 N13 与 C4a 距离从 7.5 Å 缩短至 6.0 Å,达到适合氧转移的反应距离。作者据此提出 3-OH 介导的构象重排是 N-氧化进行的必要前提。T196、M234 和 N249 通过疏水与偶极-π 相互作用稳定这一生产性结合模式(Figure 4A,F)。

定点突变验证:与底物 2 的吲哚单元相互作用的 T196、M234、N249 的突变几乎不影响 2→3 转化,但显著削弱 3→4 生成(Figure 3C,4H)。其中 PldC<sup>T196I</sup> 完全丧失 3→4 活性,PldC<sup>M234T</sup>、PldC<sup>N249G</sup> 大幅下降;而 BCDO 邻近残基突变(M225L、I404M、V405I)影响有限(Figure 3C)。作者强调,所有突变体仍保留对 2→3 的催化能力,说明它们并非失活死突变,而是特异性地损伤 N-氧化步骤。

最具揭示性的发现是 PldC 第 61 位的甘氨酸。PldC<sup>G61A/S/C</sup> 突变体直接生成 N13-氧化产物 9,而非按 2→3→4 顺序进行(Figure 3D,4H)。分子对接显示这些位点突变的侧链与底物羧基产生立体冲突,迫使底物向下位移并重新定位 N13 至接近 C4a,从而将催化从 C3-氧化重定向为 N-氧化(Figure 4F,S37);相比之下,在该位点引入更大侧链(Thr、Val、Leu、Phe、Tyr)则显著降低酶活性并完全消除 N-氧化(Figure S38A)。PldC<sup>G61S</sup> 仍可生成 8 表明该位点是 PldC 活性的"热点"(Figure 3D)。另一方面,9 与 PldC 孵育可生成 4,而 CtdE 及其突变体均不能转化 9(Figure 3B trace iv,Figure S38B),进一步说明 PldC 在该分支中具有独特活性。

PhqK 则采取完全不同的结合逻辑。对接与 MD 模拟显示,PhqK 中 2 的结合姿态与 paraherquamide L 在 PhqK 晶体结构 (PDB: 6PVI) 中的姿态相似;**与 PldC、CtdE 相比,底物 2 在 PhqK 中采取近似 180° 翻转的结合方向**(Figure 4G)。具体而言,2 的吲哚 NH 与 A325 形成 1.6 Å 氢键以刚性化构象,N13 由 D47(2.4 Å H 键/静电作用)和 C48(3.7 Å 范德华作用)锚定;C48 和 G326 共同塑形催化微环境,使 N13 精确朝向 FAD,**此时 FAD C4a-OOH 与 N13 仅距 6.7 Å**,可直接进行 N-氧化而无需经过 3-OH 中间体。CtdE 对应残基突变分析(Figure S38C,D)显示 I198T、L227M、T236M、G251N、M404I、I405V 仅轻度影响 2→8 转化,CtdE<sup>S63G</sup> 完全丧失 8 的生成但 N-氧化活性反而增强,反向印证第 61/63 位点是 C-氧化 / N-氧化选择性的关键开关。

邻近 FAD 的 D58 与 R120 推测在催化循环中介导质子转移。作者测试了 PldC<sup>R120A</sup>(完全失活)与 PldC<sup>D58A</sup>(仅残留 3 微量生成),且两者均不能将 3 转化为 4(Figure 4H,Figure S38E)。考虑到 R120 与底物距离较远,**作者提出可能由桥连水分子介导质子转移**,而非侧链直接供质子,该假设得到 CtdE–FAD–citrinadin-2 复合物中桥连水分子的结构支持(Figure S39A,B)。

综上,**FMO 活性口袋高度保守,而底物结合取向决定了过氧黄素中间体是进攻吲哚 C2═C3 双键(C─O 成键)还是叔胺氮孤对电子(N─O 成键)**;G61/S63 位点及其同源残基正是这一选择性开关。

---

# 六、总体结论

本文鉴定了首个负责复杂真菌 PIA 中 N-氧化物生物合成的丝状真菌酶家族——以 PldC 为代表,联合 CtdE 和 PhqK 三例功能表征,确立 **Class A FMO 同时承担吲哚 C2–C3 环氧化与叔胺 N-氧化双重氧化反应**,扩展了该家族的催化谱系。三个酶此前被归为立体选择性吲哚单加氧酶,本文证明其 N-氧化活性在该家族分支中具有进化保守性。机制层面,作者提出 C/N 选择性主要由**底物在保守活性口袋内的结合取向**(而非独立催化残基或辅因子构象)决定——PldC 与 CtdE 中 α-面 / β-面取向决定 C-氧化产物,3-OH 介导的构象重排或 180° 翻转(如 PhqK)则将 N13 推向 C4a 实现 N-氧化。PhqK 自身 N-氧化能力的发现也暗示 paraherquamide 类天然产物(VM55596、(–)-mangrovamide B)的生物合成装配中可能存在独立的第三条途径。

**该研究最核心的科学定论为:FMO 单一家族能够驱动 C-氧化与 N-氧化双路径生成结构多样的生物碱代谢物,N-氧化物形成是该 FMO 进化枝在真菌 PIA 生物合成中的保守功能特征**。

---

# 七、论文评价

### 优点与创新

本文最突出的贡献是**首次在真菌 PIA 体系中确立 FMO 介导的 N-氧化物生物合成机制**,突破了此前哺乳动物、细菌、植物三个 N-氧化酶体系的局限,填补了真菌这一最大天然产物家族在该化学领域的空白。作者通过 Δ*pldH*/Δ*pldC* 敲除、异源表达、体外重构、NMR/ECD/单晶 X 射线衍射等多种正交手段,构建了从 BGC 到催化机制较为严密的证据链;三个新化合物(4、8、9)的系统结构表征为本研究奠定了化学基础**,**特别是 8 的单晶结构(CCDC 2521192)为螺氧吲哚绝对构型的指认提供了直接证据。同时,通过对 PldC、CtdE、PhqK 三酶功能保守性与分化的比较分析,提出"底物结合取向决定 C/N 选择性"的统一机制模型,并通过 G61/S63 位点突变实现"开关"式功能切换,**为 FMO 催化设计原则提供了少见的可工程化范例**。

### 未来研究方向

最重要的后续工作是**获得 PldC 含 FAD 与底物的高分辨率共晶体结构**,以直接验证当前基于 AlphaFold3 与分子对接提出的活性位点模型;尤其是 D58/R120 与桥连水的质子转移机制,目前仅有间接突变和同源结构支持。同时,**应将 PldC、CtdE、PhqK 在天然宿主(分别为 *Pallidocercospora* sp. ADS-F95、*Penicillium citrinum*、*Malbranchea aurantiaca*)中进行基因敲除或回补**,以验证体外 N-氧化活性是否在体内也驱动相应 N-氧化物形成,从而将体外充分性提升为天然条件下的必要性证据。

---

# 八、关键问题及回答

**Q1: PldC 晶体结构(PDB: 26WF)中 FAD 与底物缺乏可解释电子密度,本文提出的底物结合取向与质子转移机制究竟由哪些证据直接支持?**

**A**: 本文中**直接实验证据**包括:(1) Δ*pldH* 和 Δ*pldC* 敲除后代谢谱改变(Figure 2B,C);(2) PldC 体外酶促反应 2→3→4 顺序(Figure 3B,Figure S6A);(3) <sup>18</sup>O<sub>2</sub> 同位素证实 O<sub>2</sub> 为氧源(Figure S17,S33);(4) PldC<sup>T196I/M234T/N249G</sup> 突变体特异损伤 3→4 而不影响 2→3(Figure 3C,4H);(5) PldC<sup>G61A/S/C</sup> 直接生成 9(Figure 3D,4H)以及 CtdE<sup>S63G</sup> 增强 N-氧化(Figure S38D)。**然而 α-面 / β-面结合取向、3-OH 引起的构象重排(7.5 Å→6.0 Å)、PhqK 中 180° 翻转、D58/R120 与桥连水的质子供体角色均依赖 AlphaFold3 与分子对接/动力学模拟**(Figure 4,S35,S37,S39),属于**作者据此提出的机制模型而非直接结构确证**。因此在解读这些机制图时,应明确将"敲除 / 突变结果"与"对接构象解释"区分开来。

**Q2: PhqK 直接以底物 2 为底物进行 N13-氧化(Figure 3B trace vii),而 PldC 与 CtdE 均不能越过 3-OH 中间体,这一差异是否意味着 paraherquamide 生物合成中独立存在第三条平行的 N-氧化途径?**

**A**: 体外数据支持 PhqK 采取与 PldC(顺序 2→3→4)和 CtdE(先 C-后弱 N-)完全不同的催化逻辑。**PhqK 与 2 共孵育生成 9、与 3 共孵育不生成产物**(Figure 3B trace vii),且 9 的 N-氧化物氧源自 <sup>18</sup>O<sub>2</sub>(Figure S33),与 FMO 催化特性一致;分子对接显示 2 在 PhqK 中相对 PldC/CtdE 呈约 180° 翻转,N13 由 D47、C48、A325 锚定后直接朝向 FAD C4a-OOH(6.7 Å,Figure 4G)。**作者据此推断 paraherquamide 类天然产物(VM55596、(–)-mangrovamide B)的生物合成中可能存在一条不经 3-OH 中间体的第三条 N-氧化途径**。但必须指出,这一推论**尚未在天然宿主 *Malbranchea aurantiaca* 中通过基因敲除 / 回补实验加以验证**,因而目前主要属于作者基于体外数据的合理推测,不能等同于体内确证。

**Q3: 体外重构的顺序途径 2→3→4 中,为何 PldC 不能将 2 直接 N-氧化生成 9?这一限制在体内是否同样存在?**

**A**: 作者在体外明确报告"direct N13-oxidation of substrate 2 was undetectable via both HPLC and LC-HRMS analyses",且 G61 野生型 PldC 与 2 孵育时只观察到 P1/P2(Figure 3B trace ii)而未见 9;只有引入 G61A/S/C 突变后,空间位阻改变底物取向,9 才作为主要产物出现(Figure 3D,4H,S38A)。**这一证据说明,在 PldC 野生型活性位点中,底物 2 的吲哚 C2═C3 双键相对于 FAD C4a-OOH 的反应取向优于 N13 孤对电子**,因此 C-氧化动力学占绝对优势(Figure S18 给出 *k*<sub>cat</sub>/*K*<sub>M</sub> 500 倍差异);只有在底物被强制重新定向时,N-氧化才能成为主反应。**在体内,作者通过 Δ*pldC* 突变体中 1 消失、2 积累的表型(Figure 2B,C)确认 PldC 是该途径的关键节点,但并未直接比较天然宿主中是否存在 9 或类似 N-氧化物旁路产物**;因此"体内是否完全不存在 2→9 直链"仍属于待验证的推论,而非直接证明。

> 分类状态：待全部文献笔记完成后统一分类归档。
