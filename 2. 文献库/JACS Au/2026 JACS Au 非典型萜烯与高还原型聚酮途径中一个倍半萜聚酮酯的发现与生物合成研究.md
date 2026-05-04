![image.png](https://synbiopath.online/20260504161640887.png)

---

# 一：基本信息

**文章题目**：Discovery and Biosynthesis of Sesquiterpene Polyketide Ester from an Atypical Terpene and Highly Reducing Polyketide Pathway（）

**文章 DOI 号**：https://doi.org/10.1021/jacsau.6c00383

**期刊名称**：JACS Au

**通讯作者及工作单位**：
- **邹懿**：西南大学药学院 (College of Pharmaceutical Sciences, Southwest University, Chongqing 400715, P. R. China)

---

# 二：研究背景

真菌来源的杂合倍半萜酯类天然产物因其复杂的化学结构与多样的生物活性而备受关注。根据酯键所连接的基团类型，该类化合物可划分为两个亚类：倍半萜氨基酸酯 (sesquiterpene amino acid ester, sqTAAE) 与倍半萜聚酮酯 (sesquiterpene polyketide ester, sqTPKE)。前者中，倍半萜骨架通过酯键与氨基酸单元相连；后者中，倍半萜骨架则与聚酮链形成酯键。**Figure 1** 系统展示了这两类化合物的代表性结构及其对应的关键合成酶。如 **Figure 1A** 所示，sqTAAE 的典型实例包括 aculeanes（以 norsequiterpene 骨架与 L-脯氨酸酯化）、chlamonitrides（以高度氧化的愈创木烷型倍半萜与非蛋白源异腈异亮氨酸结合）、flavunoidine（四环倍半萜核心与非蛋白源 S,S-二甲基脯氨酸结合）以及 astellolides（6-6 双环 drimane 型倍半萜与对羟基苯甲酸酯化）。这些 sqTAAE 的合成涉及不同类型的萜烯环化酶 (terpene cyclase, TC)（如 class I TC 与 HAD-like TC）与不同单模块非核糖体肽合成酶 (nonribosomal peptide synthetase, NRPS)（携带末端缩合结构域或转移酶结构域）之间的协同装配。相比之下，**Figure 1B** 呈现了目前已鉴定的三类 sqTPKE 家族——melleolides、calidoustenes 和 fumagillins。这些 sqTPKE 所涉及的 TC 类型包括 class I TC、HAD-like TC 以及 UbiA-type TC，分别对应不同的环系结构（如 4-6-5 三环、6-6 双环和 6-4 桥环）。在酰基供体方面，非还原型聚酮合酶 (nonreducing polyketide synthase, nrPKS) 生成的 ACP 结合型苔色酸，或高还原型聚酮合酶 (highly reducing polyketide synthase, hrPKS) 生成的线性多烯聚酮链，可通过顺式硫酯酶 (thioesterase, TE) 结构域、反式转移酶或 α/β 水解酶转移至倍半萜骨架上。

![image.png](https://synbiopath.online/20260504161811284.png)

然而，当前领域内一个重要的科学瓶颈在于：已发现的 sqTPKE 数量远少于 sqTAAE，且其生物合成途径中新颖的 TC 类型、PKS 类型以及两者之间非典型的协同方式仍有待挖掘。**Figure 1C** 以示意图形式提出了本研究的切入点：通过挖掘新型 TC 与 PKS 之间非传统的合作模式，有望发现新的 sqTPKE。作者注意到一类在多个 *Aspergillus* 和 *Penicillium* 物种中保守存在的未表征基因簇，其中来自 *Aspergillus aculeatus* CRI323-04 的 *lpg* 簇（NCBI 编号 PX726970）编码了 11 个基因，包括一个 TC (Lpg1)、一个 hrPKS (Lpg9)、一个丝氨酸水解酶 (serine hydrolase, SH, Lpg8)、两个细胞色素 P450 酶 (CYP450s, Lpg2 和 Lpg4)、一个黄素依赖型胺氧化酶 (flavin-dependent amine oxidase, FAO, Lpg10)、一个焦磷酸硫胺素依赖型脱羧酶 (thiamine pyrophosphate-dependent decarboxylase, TPDC, Lpg7)、一个 CoA 连接酶 (Lpg6)、一个转移酶 (AT, Lpg3) 以及两个调控因子。该基因簇呈现多处区别于已知 sqTPKE 簇的显著特征：Lpg1 属于不含经典 DDxxD 基序的新型 TC 家族，可能使用 K/M 作为催化残基；hrPKS Lpg9 与 SH Lpg8 的共存暗示 ACP 结合型聚酮链通过水解或内酯化释放，但其向萜烯骨架转移的方式尚不明确；此外，FAO Lpg10 与 TPDC Lpg7 的存在提示可能与氨基酸修饰相关。基于上述分析，作者提出该 *lpg* 簇编码了一条非典型的萜烯与高还原型聚酮途径，可能负责新型 sqTPKE 的合成。本文旨在通过异源表达、基因组合重构、同位素饲喂及系统的体外生化表征，完整阐明该途径的催化机制与装配逻辑。

![image.png](https://synbiopath.online/20260504161833168.png)

---

# 三：研究思路

本研究首先通过生物信息学分析锁定 *lpg* 簇中编码非典型 TC 的基因 *lpg1*，利用 *Aspergillus nidulans* 和 *Saccharomyces cerevisiae* 异源表达体系确证其催化法尼基焦磷酸 (farnesyl pyrophosphate, FPP) 环化生成 **ent-β-longipinene (1)** 的功能，并通过 X 射线晶体衍射确定其绝对构型。随后，将候选 CYP450 基因 *lpg2* 与 *lpg4* 分别与 *lpg1* 组合表达，鉴定出 Lpg2 催化化合物 **1** 的 C10 与 C5 双位点羟化生成化合物 **2**。进一步将 *lpg* 簇中除两个调控基因外的其余六个基因 (*lpg3, lpg6, lpg7, lpg8, lpg9, lpg10*) 与 *lpg12* 共同表达，检测到终产物 **3 (aculealdehyde)**，其结构为化合物 **2** 的 C5-羟基与一个独特的 isoheptylic acid (4) 单元形成的酯。通过逐级基因敲除与组合回补实验，明确了 *lpg3, lpg6, lpg7, lpg8, lpg9, lpg10* 对侧链合成与酯化均不可或缺。为解析侧链来源，采用同位素标记的 L-亮氨酸饲喂实验，确证 L-亮氨酸通过脱氨与脱羧途径掺入侧链。在此基础上，通过体外生化反应逐一表征了 Lpg10 (催化 L-亮氨酸氧化脱氨生成 4-methyl-2-oxovaleric acid, **6**)、Lpg7 (催化 **6** 非氧化脱羧生成 isovaleraldehyde, **7**)、Lpg6 (作为 isovaleryl-CoA 合酶催化 **5** 生成 isovaleryl-CoA, **8**) 以及 Lpg9/Lpg8 合作将 **8** 延伸为 **4** 的功能。最后，发现 Lpg6 还具有第二项功能：活化 **4** 生成 isobutyl-CoA (9)，并由 Lpg3 催化 **9** 与 **2** 的酯化反应，完成终产物 **3** 的合成。值得注意的是，异源宿主 *A. nidulans* 自身的内源 CoA 连接酶 XP_050469183.1 亦能部分替代 Lpg6 的第二个功能，协助 **4** 的活化。

---

# 四：研究方法

- **异源表达体系**：以 *Aspergillus nidulans* (AN-WT) 和 *Saccharomyces cerevisiae* (SC 及 RC01 菌株) 为底盘，通过原生质体转化或酵母转化法，构建携带不同基因组合的重组菌株，用于体内功能鉴定与产物谱分析。
- **气相色谱-质谱联用与液相色谱-质谱联用**：采用 GC-MS 检测挥发性倍半萜烃类产物 (化合物 **1**)；采用 LC-MS 及高分辨质谱 (HR-MS) 检测氧化产物与酯化产物，并通过提取离子流图 (EIC) 进行定量比较。
- **核磁共振波谱与 X 射线晶体衍射**：分离纯化化合物 **1**、**2** 和 **3**，通过 1D 和 2D NMR (COSY, NOESY, HSQC, HMBC) 确定平面结构与相对构型；对化合物 **2** 进行单晶 X 射线衍射分析，确定绝对构型。
- **同位素标记饲喂实验**：向重组菌株 *A. nidulans* 中分别饲喂 L-Leu-\(^{13}C_6\)、2-\(^{13}C\)-Leu 和 1,2-\(^{13}C\)-Leu，通过 HR-MS 检测化合物 **3** 的分子量位移，追踪 L-亮氨酸碳原子的掺入模式。
- **体外酶学实验**：将目标基因 (*lpg10, lpg7, lpg6, lpg3*) 分别在大肠杆菌或酵母中异源表达并纯化重组蛋白，在优化缓冲体系中加入底物、辅因子 (ATP, CoA, 2-硝基苯肼等)，通过 LC-MS 或 HR-MS/MS 检测酶促产物。
- **生物信息学与结构建模**：通过序列比对、系统发育分析及同源建模 (基于已知晶体结构)，预测 Lpg1 的三维结构、催化残基及跨膜区。

---

# 五：实验设计及结果分析

### （一）非典型萜烯环化酶 Lpg1 的功能确证与 **ent-β-longipinene** 的生物合成

#### 实验目的与设计逻辑

为揭示 *lpg* 簇中编码的非典型 TC 是否具有催化 FPP 环化生成新颖倍半萜骨架的能力，作者首先对 Lpg1 进行了系统的生物信息学分析，发现其仅与已知的 2Z-humulene 环化酶 EupE 和 humulene 环化酶 AsR6 具有约 42%-49% 的序列一致性，且缺乏经典 TC 的保守 DDxxD 基序，推测其采用 K/M 残基作为催化亲核试剂。此外，Lpg1 的 C 末端含有一段 23 个氨基酸的跨膜序列，提示其为罕见的膜结合型 AsR6-like TC。基于此，作者将 *lpg1* 基因分别引入 *A. nidulans* 和 *S. cerevisiae* 中进行异源表达，以期鉴定其催化产物。

#### 实验结果与机理解析

**Figure 2A** 展示了 *lpg* 基因簇的整体组织与各基因的推定功能。其中 *lpg1* 编码的 TC 被标注为“atypical TC”。**Figure 2B** 呈现了 Lpg1 功能验证的 GC-MS 分析结果。图 2B-i 为阴性对照 *A. nidulans* 空菌株 (AN-WT) 的代谢物谱，未见保留时间约 13.5 分钟的显著峰；图 2B-ii 为表达 *lpg1* 的 AN-*lpg1* 菌株，在该保留时间处出现一个分子量为 204 的新峰，与倍半萜烃类分子量相符。进一步在酵母体系中验证：图 2B-iii 为表达空载体的 *S. cerevisiae* 微粒体组分，无对应产物；图 2B-iv 为表达 *lpg1* 的 S.c-*lpg1* 微粒体组分，同样检测到相同保留时间的产物。**Figure 2C** 展示了化合物 **1** 和 **2** 的化学结构。通过 NMR 分析，确定 **1** 为具有罕见 7-6-4 桥环体系的 **ent-β-longipinene**（绝对构型为 1R, 2S, 7R, 8R）。NOESY 相关信号（CH3-14/H7, H7/CH3-12, CH3-12/H1, H8/CH3-13）确立了相对构型，而化合物 **2** 的单晶 X 射线衍射（CCDC 2518044）及旋光分析共同确认了 **1** 的绝对构型为 **1R, 2S, 7R, 8R**，与植物来源的 (-)-β-longipinene 呈对映关系。**Figure 2D** 提出了 Lpg1 催化 FPP 环化生成 **1** 的推演机理：FPP 首先经 1,10-环化生成 humulene 型阳离子中间体，随后经一系列氢迁移、甲基迁移和再环化，最终形成 7-6-4 三环体系。图中同时标出了 Lpg2 后续催化 C10 和 C5 位羟化的位点（红色波浪线）。**Figure 2E** 为基因组合表达实验的 LC-MS 结果（EIC m/z 219 [M+H-H2O]+，对应于化合物 **2** 的特征离子）。图 2E-i 为 AN-*lpg1* 对照，无 **2** 生成；图 2E-ii 为 AN-*lpg12*（共表达 *lpg1* 和 *lpg2*），检测到 **2**；图 2E-iii 为 AN-*lpg14*（共表达 *lpg1* 和 *lpg4*），无 **2**；图 2E-iv 为 AN-*lpg124*（共表达 *lpg1, lpg2, lpg4*），同样检测到 **2**，表明 Lpg4 对 **1** 和 **2** 均无羟化能力，而 Lpg2 可独立催化 **1** 转化为 **2**。进一步的酵母体系实验（Figure S9）也证实了 Lpg2 的这一功能。**结构解析显示，Lpg2 同时催化了 1 中相距约 5.2 Å 的两个最远端惰性碳原子 C10 和 C5 的羟化反应，并分别生成 10R 与 5S 构型**，展现出与 trichodiene 合酶 Tri4 类似的多步氧化能力。单点突变实验（Figure S8）证实 M254L 和 K258A 突变均使 Lpg1 丧失活性，确证了这两个残基在催化中的关键作用。

![image.png](https://synbiopath.online/20260504161958341.png)

> “These results confirm that Lpg1 is a TC for the synthesis of ent-β-longipinene, a β-longipinene family TC first discovered in nature, it indeed differs from EupE and AsR6 that are responsible for the synthesis of humulene.”

### （二）酯化终产物 aculealdehyde 的发现与侧链来源的示踪验证

#### 实验目的与设计逻辑

在确证 Lpg1 和 Lpg2 可分别生成 **1** 和 **2** 的基础上，作者试图探究 *lpg* 簇中其余基因是否参与进一步的修饰，尤其是形成 sqTPKE 所必需的酯化步骤。由于调控因子 Lpg5 和 Lpg11 可能仅参与转录调控而非直接催化，作者将剩余的六个基因 (*lpg3, lpg6, lpg7, lpg8, lpg9, lpg10*) 与 *lpg12* 共同导入 *A. nidulans* 中，构建 AN-*lpg123678910* 菌株，以期检测到完整的酯化产物。同时，为解析侧链单元的来源（鉴于簇中存在 L-亮氨酸代谢相关的酶），作者设计了同位素标记饲喂实验，以追踪 L-亮氨酸是否掺入终产物。

#### 实验结果与机理解析

**Figure 3A** 展示了基因组合实验的 LC-MS 结果（EIC m/z 331 [M+H-H2O]+，对应于化合物 **3** 的特征离子）。图 3A-i 为 AN-*lpg12* 对照，无 **3** 生成；图 3A-ii 为 AN-*lpg123678910*，检测到显著的新峰，经分离纯化与 NMR 鉴定为化合物 **3**（命名为 aculealdehyde）。**Figure 3B** 展示了化合物 **3** 的化学结构：其核心为 **2** 的 C5-羟基与一个独特的 isoheptylic acid (4) 单元通过酯键连接。图 3B 中同时标示了 L-亮氨酸碳原子在 **4** 中的掺入位置（红色标注）。为确证 L-亮氨酸是 **4** 的前体，作者分别饲喂三种同位素标记的 L-亮氨酸：L-Leu-\(^{13}C_6\) 使 **3** 的分子量增加 5 Da；2-\(^{13}C\)-Leu 和 1,2-\(^{13}C\)-Leu 均使 **3** 的分子量增加 1 Da（图 S20-S22）。**这些数据明确表明 L-亮氨酸的 C2-C6 骨架整体掺入 4 中，同时 C1 位羧基在脱羧过程中丢失**。**Figure 3C** 为侧链中间体喂养实验的 LC-MS 结果（图 3C-i 至 3C-vii）。将化合物 **4** 直接饲喂给 AN-*lpg1236*（不含 *lpg7-10*）可恢复 **3** 的生成（图 3C-vi-vii）；将 isovaleric acid (5) 饲喂给 AN-*lpg123689*（不含 *lpg7, lpg10*）也可恢复 **3** 的生成（图 3C-iv）。此外，将 isovaleraldehyde (7) 饲喂给 AN-*lpg123689* 同样检测到 **3**（图 3C-v）。这些结果共同证明 **5** 和 **4** 是侧链合成的关键中间体，且 **7** 可在体内或缓冲条件下自发氧化为 **5**（图 3D-vi-vii）。

![image.png](https://synbiopath.online/20260504162119936.png)

> “These results confirm that L- Leu is indeed incorporated into the synthesis of 4 via the deamination and 1-C decarboxylation.”

### （三）L-亮氨酸向异戊酸及异庚酸的酶促转化途径

#### 实验目的与设计逻辑

基于同位素示踪和喂养实验的结果，作者推断从 L-亮氨酸生成 isoheptylic acid (4) 的途径可分为两个阶段：第一阶段由 Lpg10 和 Lpg7 催化 L-亮氨酸转化为 isovaleric acid (5)；第二阶段由 Lpg6、Lpg9 和 Lpg8 协作将 **5** 延伸为 **4**。为验证这一假设，作者分别纯化了 Lpg10、Lpg7 和 Lpg6 重组蛋白，并设计体外酶促反应以逐级验证每一步的催化功能。

#### 实验结果与机理解析

**Figure 3D** 展示了 Lpg10 和 Lpg7 的体外生化分析结果。图 3D-i 为底物 L-亮氨酸对照；图 3D-ii 为 Lpg10 与 L-亮氨酸孵育后，检测到 4-methyl-2-oxovaleric acid (6) 的生成（m/z 129 [M-H]-），证实 **Lpg10 作为黄素依赖型胺氧化酶，催化 L-亮氨酸的氧化脱氨生成 6 **。图 3D-iii 为 Lpg7 与 6 孵育，并加入 2-硝基苯肼 (2NP) 捕获羰基产物，检测到 isovaleraldehyde 的 2NP 衍生物 (E/Z-2NP-7，m/z 222 [M+H]+)（图 3D-iv 为底物对照，图 3D-v 为保留时间对比）；图 3D-vi 为不加酶的缓冲液对照，亦能检测到微量的 5 (m/z 101 [M-H]-) 生成；图 3D-vii 为 Lpg7 催化反应后检测到 5的生成。**以上结果共同表明：Lpg7 催化 6 的非氧化脱羧生成 7，而 7 可发生自发的氧化转化生成 **5**。后续实验（图 3C-v）进一步确证 **7** 在体内也可转化为 **5**。

**Figure 3E** 展示了 Lpg6 催化 isovaleryl-CoA (8) 生成的质谱证据。将纯化的 Lpg6 与 CoA、ATP 及底物 **5** 共同孵育，通过 HR-MS/MS 检测到 **8** 的特征性分子离子峰（图 3E-i 为不加酶的对照，图 3E-ii 为加酶反应）。**该结果首次鉴定 Lpg6 为 isovaleryl-CoA 合酶，拓展了真菌 hrPKS 起始单元的来源（不限于经典的乙酰-CoA 或丙酰-CoA）**。在此基础上，作者提出 Lpg9 (hrPKS) 以 **8** 为起始单元，经连续的还原性延伸生成聚酮链，最终由 Lpg8 (丝氨酸水解酶) 介导释放并形成 isoheptylic acid (4)。这一过程与经典的 hrPKS 编程逻辑一致。

### （四）双重功能的 CoA 连接酶 Lpg6 与酯化步骤的完成

#### 实验目的与设计逻辑

在明确了 **4** 的生成途径后，最后一个关键问题在于：**4** 如何与 **2** 的 C5-羟基发生酯化？簇中编码的转移酶 Lpg3 被推定负责该步反应。然而，体外实验显示 Lpg3 无法直接以游离的 **4** 为酰基供体。考虑到 **4** 的结构（一个带支链的七碳羧酸）与常见的 CoA 衍生物类似，作者推测 **4** 需要先被活化为 CoA 酯 (isobutyl-CoA, **9**)，再由 Lpg3 识别并转移至 **2**。令人关注的是，簇中的 CoA 连接酶 Lpg6 已经参与了 **5** 的活化，它是否也能活化 **4**？作者对此进行了验证。

#### 实验结果与机理解析

**Figure 3F** 展示了 Lpg6 催化 **4** 生成 **9** 的分析结果。图 3F-i 为阴性对照（不加酶），无 **9** 生成；图 3F-ii 为 Lpg6 与 **4**、CoA 和 ATP 孵育后，通过 HR-MS/MS 检测到 **9** 的生成。值得注意的是，**图 3F-ii 与图 3E-ii 对比显示，Lpg6 催化 **4** 生成 **9** 的效率低于其催化 **5** 生成 **8** 的效率**，提示 **4** 可能不是 Lpg6 的天然最优底物。尽管如此，**该结果首次鉴定 Lpg6 为同时识别 isovaleric acid 和 isoheptylic acid 的双功能 CoA 连接酶**。**Figure 3G** 展示了 Lpg3 催化的酯化反应。图 3G-i 为 Lpg3 与 **4** 和 **2** 直接孵育，无 **3** 生成；图 3G-ii 为无酶对照；图 3G-iii 为 Lpg6 与 Lpg3 的偶联反应（同时加入 **4**、**2**、CoA、ATP 及两种酶），检测到 **3** 的生成；图 3G-iv 为本研究鉴定的异源宿主内源酶 XP_050469183.1 与 Lpg3 的偶联反应，同样检测到 **3**。此外，作者还验证了 Lpg3 不能以 **8** 为酰基供体生成相应的酯化产物（Figure S13）。**上述结果确证：Lpg3 特异性识别 isobutyl-CoA (9) 作为酰基供体，催化与化合物 **2** 的 C5-羟基发生酯化反应，最终生成 **3**。Lpg6 在其中扮演双重角色：既作为 isovaleryl-CoA 合酶启动 hrPKS 程序，又作为 isoheptylyl-CoA 合酶为酯化步骤提供活化形式的侧链。**

值得注意的是，异源宿主 *A. nidulans* 的内源 CoA 连接酶 XP_050469183.1 与 Lpg6 具有约 44% 的序列一致性，其功能同样被表征为 isoheptylyl-CoA 合酶（图 3F-iii），且在与 Lpg3 偶联时也能生成 **3**（图 3G-iv）。这一发现解释了为何在缺乏 *lpg6* 的菌株中仍能检测到少量 **3**（图 3C-vi-vii）。**本工作揭示的 Lpg6 双重功能与异源宿主内源酶的补偿作用，共同构成了 sqTPKE 侧链活化与酯化的完整分子基础。**

> “Notably, Lpg6 was identified as the isovaleryl-CoA synthase, which not only expands the substrate origin of fungal hrPKSs (not limited to the classical acetyl-CoA or propionyl-CoA), but also provides an alternative biocatalyst for further engineering the diversity of the fungal hrPKS starting units.”

### （五）完整的生物合成模型

**Figure 4** 以总结性示意图的形式，完整呈现了从 L-亮氨酸出发，经 Lpg10、Lpg7、Lpg6、Lpg9、Lpg8 协同作用生成 isoheptylic acid (4)，继而由 Lpg6（或宿主内源酶 XP_050469183.1）活化生成 **9**，并由 Lpg3 催化与 Lpg1/Lpg2 生成的倍半萜核心 **2** 发生酯化，最终得到 aculealdehyde (3) 的全路径。图中以方框突出展示了宿主内源 CoA 连接酶对 **4** 向 **9** 转化的补偿作用。该模型突出了三个核心创新点：(1) Lpg1 作为非典型膜结合 TC 催化生成 **ent-β-longipinene**；(2) Lpg2 实现双位点远端羟化；(3) Lpg6 作为一个单酶同时启动 hrPKS 延伸与终产物酯化两个关键步骤，且 hrPKS 的起始单元为来源于 L-亮氨酸代谢的支链 CoA 酯 (8)，而非经典的小分子酰基 CoA。

---

# 六：总体结论

本研究通过异源表达、基因组合重构、同位素示踪与系统的体外生化表征，从 *Aspergillus aculeatus* 中发现并完整解析了一个新型倍半萜聚酮酯 aculealdehyde (3) 的生物合成途径。**该途径的核心特征包括：一个非典型的膜结合萜烯环化酶 Lpg1 催化 FPP 环化生成具有罕见 7-6-4 桥环结构的 **ent-β-longipinene (1)**；一个多功能细胞色素 P450 酶 Lpg2 在 **1** 的 C10 与 C5 两个最远端惰性碳原子上同时引入羟基，生成 **2**；以及一条由 L-亮氨酸代谢启动的高还原型聚酮途径**。尤为重要的是，**本研究首次鉴定了一个具有双重功能的 CoA 连接酶 Lpg6**，它既能将 isovaleric acid (5) 活化为 isovaleryl-CoA (8) 以启动 hrPKS 的延伸程序，又能将 isoheptylic acid (4) 活化为 isobutyl-CoA (9) 以供给最终的酯化步骤。**转移酶 Lpg3 特异性识别 **9** 而非 **8** 作为酰基供体，催化与 **2** 的 C5-羟基发生酯化**。这一装配逻辑与已知的 sqTPKE 生物合成策略（聚酮链直接以 ACP 结合形式作为酰基供体）存在显著差异。本研究拓展了真菌 hrPKS 起始单元的底物范围，揭示了一种新的 sqTPKE 装配线，并为挖掘更多支链酮酸-CoA 合成酶及新型萜烯-聚酮杂合天然产物提供了理论依据与酶学工具。

---

# 七：论文评价

### 优点与创新

1. **新颖的基因簇与酶学功能**：Lpg1 属于非典型、不含经典 DDxxD 基序的膜结合 TC 家族，其催化生成 **ent-β-longipinene** 的活性为首次报道。Lpg2 的双位点（C10 与 C5）远端羟化能力在倍半萜氧化修饰中较为罕见。
2. **Lpg6 的双重功能揭示**：单酶同时作为 isovaleryl-CoA 合酶与 isoheptylyl-CoA 合酶，该发现拓展了真菌 CoA 连接酶的底物谱，并为 hrPKS 起始单元的非天然拓展提供了新的生物催化元件。
3. **完整的干湿结合研究范式**：从生物信息学预测、异源表达体内功能验证，到体外纯酶反应逐一确证每一步催化反应，逻辑链条完整严密，数据翔实。
4. **对 sqTPKE 装配逻辑的新认知**：区别于已知 sqTPKE 中聚酮链以 ACP 结合形式直接作为酰基供体，本研究中酯化步骤采用“离线”的 CoA 结合型支链酸作为供体，由独立的转移酶 Lpg3 完成，代表了一种新的生物合成策略。

### 未来研究方向

1. **Lpg9 (hrPKS) 的催化编程机制**：目前研究通过体内基因组合与喂养实验间接证明了 Lpg9 与 Lpg8 协作将 isovaleryl-CoA (8) 延伸为 isoheptylic acid (4)，但尚缺乏 Lpg9 的体外重构数据。后续可尝试表达纯化 Lpg9 及其 ACP 结构域，在体外重建完整的聚酮链延伸与释放过程，明确其还原结构域 (DH, ER, KR) 的精确编程规则。
2. **Lpg2 的底物范围与催化机理**：Lpg2 如何在单一活性口袋中实现对两个相距甚远且化学环境不同的惰性碳原子的区域选择性与立体选择性羟化，其晶体结构与分子对接模拟将有助于阐明这一非典型 P450 的催化机制。
3. **酯化步骤的底物宽泛性**：Lpg3 对 isobutyl-CoA (9) 具有严格的选择性，而对 isovaleryl-CoA (8) 无活性。通过结构生物学与定点突变，可探究决定其底物特异性的关键氨基酸残基，并尝试通过蛋白质工程拓展其底物范围，为组合生物合成创造非天然杂合分子。

---

# 八：关键问题及回答

**问题一：Lpg6 在体内同时催化 **5** 和 **4** 的 CoA 活化，但体外数据显示其对 **4** 的催化效率显著低于对 **5** 的催化效率。结合异源宿主中存在内源补偿酶 XP_050469183.1 的现象，如何评价 Lpg6 双重功能在原始宿主 *A. aculeatus* 中的生理意义？**

**解答**：Lpg6 对 **5** 的高效催化是其核心功能，因为 **8** 作为 hrPKS 的起始单元是整个聚酮侧链延伸的“种子”，其生成效率直接决定终产物 **3** 的产量。相比之下，对 **4** 的活化效率较低可能反映了两种进化上的考量：第一，**4** 在细胞内可能通过 Lpg9/Lpg8 的连续作用原位生成并局部富集，其有效浓度远高于体外反应体系中添加的外源底物浓度，因此较低的内在催化常数在体内仍可满足需求；第二，*A. aculeatus* 基因组中可能存在其他内源 CoA 连接酶（类似于 *A. nidulans* 中的 XP_050469183.1）协同完成 **4** 的活化。本研究在异源宿主中观察到的补偿现象提示，原始宿主中很可能也存在类似的“代谢冗余”机制。因此，**Lpg6 的双重功能更应被理解为：在进化过程中，一个原本专一于 **5** 活化的酶偶然获得了对 **4** 的部分活性，而这一副活性在宿主内源辅助酶的存在下被保留并整合进入了完整的合成途径**。这一发现也为合成生物学中“途径酶的非最优化特性可通过宿主代谢网络补偿”提供了例证。

**问题二：Lpg2 能够催化 **1** 上 C10 与 C5 两个位点的羟化反应，且两个产物羟基的构型不同（10R 与 5S）。请结合 P450 单加氧酶的一般催化机制，讨论 Lpg2 实现区域选择性与立体选择性控制的可能性分子基础。**

**解答**：典型的细胞色素 P450 单加氧酶通过一个共同的铁氧活性物种 (Compound I) 催化惰性 C-H 键的氢原子提取与羟基 rebound 反应。一个 P450 酶在一个底物上催化两个不同位点的羟化通常有两种机制：一是顺序催化，即酶先催化一个位点的羟化，产物从活性口袋释放后重新结合，再催化第二个位点的羟化；二是底物在活性口袋中以特定构象结合后，Compound I 依次对两个位点发起攻击。Lpg2 更可能采用后者，理由如下：第一，**1** 具有刚性三环骨架，C10 与 C5 虽相距约 5.2 Å，但若底物结合模式使这两个 C-H 键分别处于 Compound I 的可及范围内，一次结合即可实现两步氧化；第二，**2** 的生成不需要中间产物的分离与再结合，这与 AN-*lpg12* 菌株中只检测到终产物 **2** 而几乎检测不到单羟化中间体的现象一致。关于立体选择性：C10 位生成 R 构型、C5 位生成 S 构型，表明 Lpg2 的活性位点对底物不同区域的 prochiral C-H 键具有精确的空间约束。推测底物 **1** 以特定的取向嵌入活性口袋，使得 C10 上的 pro-R 氢与 C5 上的 pro-S 氢分别指向铁氧物种。后续通过 Lpg2 的晶体结构解析与分子对接模拟，可进一步验证是否存在两个独立的底物结合模式或一个延长的结合通道，从而同时容纳两个反应位点。

**问题三：本研究中 hrPKS Lpg9 使用了非经典的起始单元 isovaleryl-CoA (8)，而非真菌 hrPKS 最常见的乙酰-CoA 或丙酰-CoA。这一发现对理解真菌 hrPKS 的起始单元选择机制以及后续工程化改造有何启示？**

**解答**：传统认知中，真菌 hrPKS 的起始单元通常由酰基转移酶 (AT) 结构域从乙酰-CoA 或丙酰-CoA 中选择性装载到 ACP 上。本研究发现 Lpg9 能够接受 isovaleryl-CoA 作为起始单元，提示其 AT 结构域具有更宽的底物谱。**这一突破拓展了 hrPKS 起始单元的化学空间，意味着通过基因组挖掘或结构域交换，可能获得以更多样化的支链酰基-CoA（如来源于其他支链氨基酸代谢的异丁酰-CoA、2-甲基丁酰-CoA 等）为起始单元的 hrPKS**。对工程化改造的启示有三：第一，可以将 Lpg9 的 AT 结构域与其它 hrPKS 的 AT 结构域进行置换，以改变聚酮产物的起始结构；第二，Lpg6 这类支链酰基-CoA 合成酶可与 hrPKS 共表达，构建“即插即用”的支链起始单元供给模块；第三，结合酮基合成酶 (KS) 结构域对起始单元的空间容忍度分析，可理性设计非天然的“起始单元-延伸单元”组合，创制结构新颖的聚酮天然产物类似物。此外，本研究也为探索其他来源于氨基酸代谢的酰基-CoA 是否可作为真菌 PKS 起始单元提供了重要的方法学参考。