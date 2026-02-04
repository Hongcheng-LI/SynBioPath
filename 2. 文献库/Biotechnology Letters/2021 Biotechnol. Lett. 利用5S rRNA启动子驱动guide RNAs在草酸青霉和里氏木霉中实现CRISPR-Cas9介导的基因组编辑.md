![image.png](https://synbiopath.online/20260204104656804.png)

---

## 一：基本信息
**文章题目**：CRISPR/Cas9-mediated genome editing in *Penicillium oxalicum* and *Trichoderma reesei* using 5S rRNA promoter-driven guide RNAs
**文章 DOI 号**：10.1007/s10529-020-03024-7
**期刊名称**：*Biotechnology Letters*
**通讯作者**：高丽伟 (Liwei Gao)、刘国栋 (Guodong Liu)
**通讯作者工作单位**：山东大学微生物技术国家重点实验室，国家糖工程技术研究中心 (State Key Laboratory of Microbial Technology, National Glycoengineering Research Center, Shandong University)

---

## 二：核心速览
本研究旨在为两种重要的工业产酶真菌——草酸青霉 (*Penicillium oxalicum*) 和里氏木霉 (*Trichoderma reesei*) 构建高效、便捷的CRISPR/Cas9基因组编辑系统。研究者利用RNA聚合酶III型启动子——5S rRNA基因启动子来驱动sgRNA的表达。在*P. oxalicum*中，利用来自黑曲霉 (*Aspergillus niger*) 的异源5S rRNA启动子，成功实现了$\beta$-葡萄糖苷酶基因 (*bgl2*) 的删除，并在转录抑制因子基因 (*creA*) 中实现了无痕的小片段精准替换，编辑效率最高可达80%。而在*T. reesei*中，异源启动子效率较低，作者通过挖掘并使用其内源5S rRNA启动子，成功在全局调控因子 (*lae1*) 基因中引入提前终止密码子，实现了无痕基因编辑，效率为36.67%。该研究证明了5S rRNA启动子在丝状真菌基因编辑中的通用性和高效性，为工业菌株的遗传改造提供了有力工具。

---

## 三：研究思路
**步骤 1：构建适用于*P. oxalicum*的CRISPR/Cas9系统并验证基因删除效率**
首先，构建包含Cas9表达盒和sgRNA表达盒的质粒，其中Cas9由组成型启动子驱动，sgRNA由异源的*A. niger* 5S rRNA启动子驱动。以*bgl2*基因为靶点，分别测试带有筛选标记（*hph*）和无筛选标记的供体DNA对基因删除效率的影响，验证微同源臂（40 bp）介导的同源重组可行性。

**步骤 2：探索无痕基因编辑与精准突变**
进一步利用无筛选标记的供体DNA，尝试在*creA*基因内部进行精准的小片段替换（引入20 bp异源序列）。通过表型筛选（纤维素降解能力）和DNA测序，评估该系统在引入特定突变方面的能力，旨在实现无痕基因编辑。

**步骤 3：在*T. reesei*中优化启动子策略并实现基因编辑**
将上述系统迁移至*T. reesei*，首先测试*A. niger* 5S rRNA启动子的效率。在发现效率低下后，通过生物信息学挖掘*T. reesei*内源的5S rRNA启动子。利用内源启动子驱动sgRNA，以*lae1*基因为靶点，通过引入终止密码子的无痕供体DNA，成功实现基因功能失活，并评估编辑效率。

---

## 四：研究方法
*   **原生质体转化 (Protoplast Transformation)**: 用于将Cas9、sgRNA表达盒及供体DNA共转化进入真菌细胞。
*   **融合PCR (Fusion PCR)**: 用于构建Cas9表达盒及长同源臂供体DNA。
*   **生物信息学分析 (Bioinformatics)**: 利用CHOPCHOP设计sgRNA靶点，利用BLASTn搜索同源5S rRNA基因序列。
*   **表型分析 (Phenotype Analysis)**: 通过在含纤维素平板上的生长圈大小评估纤维素酶分泌能力，或通过产孢情况筛选突变体。
*   **DNA测序 (Sanger Sequencing)**: 用于最终确证基因组编辑的准确性。

---

## 五：实验设计及结果分析

### （一）*P. oxalicum* 中基于异源5S rRNA启动子的基因删除与无痕编辑
#### 实验目的与设计逻辑
在丝状真菌中，sgRNA的高效表达是CRISPR/Cas9系统成功的关键。鉴于5S rRNA启动子在黑曲霉中的成功应用，作者首先尝试将其引入亲缘关系较近的*P. oxalicum*。为了验证该系统的有效性及供体DNA设计对效率的影响，作者选择了$\beta$-葡萄糖苷酶基因*bgl2*作为靶点。设计了两个sgRNA靶向*bgl2*编码区两侧，旨在产生双链断裂（DSB）并介导整个基因的删除。同时，设计了两种供体DNA：一种带有*hph*筛选标记且两侧仅含40 bp微同源臂（图1a），另一种为无标记的500 bp长同源臂融合片段（图1b），以评估不同修复模板对同源重组（HR）效率的影响。

#### 实验结果与深度解析
实验结果显示，*A. niger*的5S rRNA启动子能有效驱动sgRNA在*P. oxalicum*中的表达并引导Cas9切割。如**Fig. 1**所示，利用带有筛选标记且仅含40 bp微同源臂的供体DNA（图1a），*bgl2*的删除效率高达80%（16/20转化子，**Fig. S3**）。这表明在Cas9切割产生的DSB压力下，微同源臂足以介导高效的HR。当使用无标记的长同源臂供体DNA时（图1b），虽然效率下降至30%（6/20），但成功实现了无痕删除。表型分析（**Fig. 1c**）显示，*bgl2*缺失株在纤维素平板上的透明圈明显大于亲本菌株M12，证实了基因功能的丧失及纤维素酶分泌的提升。这一部分不仅验证了异源5S rRNA启动子的活性，还确立了在该菌中利用微同源臂进行基因敲除的可行性。
![image.png](https://synbiopath.online/20260204104728814.png)

> "The above results showed that micro-homology arms on donor DNA are sufficient for homologous recombination in *P. oxalicum* with the aid of CRISPR/Cas9."

### （二）*P. oxalicum* 中 *creA* 基因的精准片段替换
#### 实验目的与设计逻辑
为了进一步展示该系统的精准编辑潜力，作者选择了碳代谢阻遏因子基因*creA*作为靶点。与*bgl2*的全基因删除不同，此次旨在通过单sgRNA切割和无痕供体DNA修复，在*creA*内部精准替换一段序列。设计思路是利用含有500 bp同源臂的供体DNA，将*creA*编码区内一段序列替换为20 bp的异源序列（导致氨基酸序列改变），从而解除CreA的阻遏效应（图2a）。

#### 实验结果与深度解析
通过共转化Cas9-pyrG表达盒、sgRNA及无标记供体DNA，作者随机挑选了20个转化子进行PCR筛选。结果显示（**Fig. S4**），11个转化子（55%）成功引入了异源序列，测序结果（**Fig. 2b**）进一步证实了氨基酸残基129-144被精准替换。表型测试（**Fig. 2c**）表明，突变株在含纤维素平板上的生长和透明圈与亲本相比有显著差异，暗示CreA功能的改变。这一结果证明了该系统不仅能做“减法”（删除），还能做精细的“改法”（原位替换），且效率可观（>50%），为代谢工程改造提供了强力工具。

> "Therefore, the gene editing system from *A. niger* could be used for both gene deletion and small region replacement in *P. oxalicum*."

### （三）*T. reesei* 中内源5S rRNA启动子的挖掘与应用
#### 实验目的与设计逻辑
鉴于*A. niger* 5S rRNA启动子在*P. oxalicum*中的成功，作者尝试将其应用于另一工业真菌*T. reesei*。然而，初步实验显示该异源启动子在*T. reesei*中效率极低。为了解决这一问题，作者转向挖掘*T. reesei*自身的内源启动子。利用近缘物种*Trichoderma virens*的5S rRNA序列作为探针进行BLASTn搜索，锁定了*T. reesei*基因组中的同源序列（图3）。随后，利用该内源启动子构建sgRNA表达盒，靶向全局调控因子*lae1*，旨在引入提前终止密码子使其失活（图4a）。

#### 实验结果与深度解析
序列比对（**Fig. 3**）显示*T. reesei*的5S rRNA基因与*T. virens*具有93%的相似性，但与*A. niger*差异较大，这解释了异源启动子效率低下的原因。利用内源启动子驱动sgRNA targeting *lae1*，通过引入终止密码子的无标记供体DNA进行修复。由于*lae1*缺失会导致产孢减少，作者利用这一表型进行初筛（**Fig. 4c**）。PCR和测序验证（**Fig. 4b**）表明，在30个随机挑选的转化子中，有11个（36.67%）成功实现了精准的碱基突变。相比之下，使用异源*A. niger*启动子的对照组未获得任何正确转化子。这一结果强调了在远缘物种间进行CRISPR系统移植时，启动子种属特异性的重要性，同时也证明了内源5S rRNA启动子是驱动sgRNA表达的优良元件。

> "Genotyping of the transformants showed that an editing efficiency of 36.67% ... was achieved by using the native 5S rRNA promoter."

---

## 六：总体结论
本研究成功在*P. oxalicum*和*T. reesei*中建立了基于5S rRNA启动子驱动sgRNA的CRISPR/Cas9基因编辑系统。在*P. oxalicum*中，异源的*A. niger* 5S rRNA启动子表现出高活性，支持微同源臂介导的高效基因删除（80%）和无痕精准替换（55%）。在*T. reesei*中，内源5S rRNA启动子的应用克服了异源启动子效率低的问题，实现了36.67%的无痕点突变效率。该研究提供了一种不依赖于传统的U6启动子或体外转录的高效、经济的基因编辑策略，对于丝状真菌的代谢工程改造具有重要应用价值。

---

## 七：论文评价
### 优点与创新
1.  **启动子策略的拓展**：验证了5S rRNA启动子（无论是异源还是内源）在丝状真菌CRISPR/Cas9系统中的适用性，为缺乏有效U6启动子信息的物种提供了新的解决方案。
2.  **无痕编辑的实现**：在两个物种中均成功实现了不引入筛选标记的无痕编辑（Markerless editing），这对工业菌株的多次改造和生物安全性至关重要。
3.  **微同源臂的应用**：在*P. oxalicum*中证明了40 bp微同源臂足以支持高效的基因敲除，简化了供体DNA的构建过程（可直接通过引物合成）。

### 未来研究方向
1.  **多基因编辑**：虽然文中提到了潜力，但未在*T. reesei*中实际演示多基因同时编辑，未来可进一步探索。
2.  **效率优化**：在*T. reesei*中的编辑效率（~37%）仍有提升空间，可能需要优化Cas9的表达或核定位信号。
3.  **广泛适用性验证**：该策略是否适用于更多非模式丝状真菌仍需进一步验证。

---

## 八：关键问题及回答

**问题 1：为什么在*T. reesei*中，*A. niger*来源的5S rRNA启动子效率远低于在*P. oxalicum*中的效率？**
**回答**：这主要是由于物种间的亲缘关系差异导致的序列保守性不同。*P. oxalicum*（青霉属）与*A. niger*（曲霉属）同属于散囊菌目（Eurotiales），亲缘关系较近，其5S rRNA基因序列相似度较高（文中提到BLASTn最佳匹配达92%），因此转录机器能较好地识别异源启动子。而*T. reesei*属于肉座菌目（Hypocreales），与*A. niger*进化距离较远，序列差异较大（如图3所示），导致*A. niger*的启动子无法被*T. reesei*的RNA聚合酶III高效识别和转录。

**问题 2：本研究中使用的无痕编辑（Markerless editing）策略有何优势？又是如何筛选突变株的？**
**回答**：无痕编辑的优势在于不在基因组中残留抗性筛选标记，这不仅避免了对后续代谢流的潜在影响，还允许在同一菌株中反复使用有限的筛选标记进行多轮改造。在本研究中，作者采用“共转化”策略进行筛选：将Cas9表达质粒（带有*pyrG*筛选标记）与无标记的sgRNA及供体DNA共转化。由于转化过程中质粒进入细胞的概率相对较低，凡是获得*pyrG*标记（即能在缺尿嘧啶培养基上生长）的转化子，其细胞内通常也摄入了足量的Cas9和sgRNA，从而有较高概率发生基因编辑。随后通过PCR或测序对这些转化子进行基因型验证。

**问题 3：微同源臂（40 bp）在*P. oxalicum*中的成功应用说明了什么？**
**回答**：这说明在Cas9引发的双链断裂（DSB）压力下，细胞内的同源重组（HR）修复机制被强力激活，即使是极短的同源序列（40 bp）也足以作为同源重组的底物引导修复。这意味着在构建供体DNA时，不再需要通过繁琐的融合PCR去拼接长达500-1000 bp的同源臂，仅需在扩增筛选标记的引物5'端添加40 bp同源序列即可，极大地简化了基因敲除载体的构建流程，提高了实验效率。