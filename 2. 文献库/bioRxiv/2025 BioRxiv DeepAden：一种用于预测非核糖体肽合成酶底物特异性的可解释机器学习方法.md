![image.png](http://synbiopath.online/20251230163029326.png)


---

## 一：基本信息

**文章题目**：DeepAden: An explainable machine learning method for predicting the substrate specificity of nonribosomal peptide synthetases

**文章 DOI 号**：10.1101/2025.05.21.655435 (bioRxiv Preprint)

**发布时间**：2025年12月23日 (Posted date)

**通讯作者**：Zhiwei Qin（秦志伟）；Heqian Zhang（张鹤千）

**通讯作者工作单位**：北京师范大学自然科学高等研究院生物科学与技术中心 (Center for Biological Science and Technology, Advanced Institute of Natural Sciences, Beijing Normal University, Zhuhai, China)

---

## 二：核心速览

### 研究背景
非核糖体肽（NRPs）是一类结构多样的微生物次级代谢产物，是临床药物的重要来源。其生物合成由巨型酶复合物——非核糖体肽合成酶（NRPSs）驱动。其中，腺苷化结构域（A-domain）负责特异性识别并激活氨基酸底物，决定了NRPs的核心骨架结构。因此，准确预测A结构域的底物特异性对于基因组挖掘和新型天然产物的发现至关重要。

### 前期研究
传统的预测方法（如NRPSpredictor2, SANDPUMA, PARAS）主要基于Stachelhaus等人定义的“特异性赋予密码”（Specificity-Conferring Codes, SCCs，即10个关键残基）或Rausch等人定义的扩展结合口袋（34个残基）。这些方法通常依赖于多序列比对（MSA）或隐马尔可夫模型（HMM），在处理与参考序列（如GrsA-Phe）同源性较低的序列或非蛋白源性底物时，准确率显著下降。近期虽有基于蛋白质语言模型（如NRPStransformer）的尝试，但在结合口袋的精确界定和非天然底物的泛化能力上仍有不足。

### 本文突破点
![image.png](http://synbiopath.online/20251230163242095.png)

**重新定义结合口袋（27-AA ABP）**：基于晶体结构数据，定义了以配体为中心6 Å范围内的27个氨基酸残基为核心结合口袋（ABP），相比传统的34-AA模型更加紧凑且特征明确。
**两阶段深度学习框架**：
*   **第一阶段（ABP-GAT）**：利用图注意力网络（GAT）结合ESM2蛋白质语言模型，在无结构输入的情况下，从序列直接精确定位结合口袋残基。
*   **第二阶段（对比学习）**：利用对比学习（Contrastive Learning）对齐口袋特征（Protein embedding）和底物化学特征（Molecule embedding），实现“口袋-底物”的匹配预测。
**可解释性与数据增强**：引入SHAP（SHapley Additive exPlanations）分析，揭示了关键功能残基，并基于SHAP值低位点进行数据增强，有效解决了样本不平衡问题。

### 研究难点
*   **同源性低导致的对齐困难**：对于进化距离较远的A结构域，传统MSA难以准确提取活性位点。
*   **样本不平衡**：已知的A结构域-底物对中，非蛋白源性氨基酸的数据极其稀缺。
*   **结构依赖性**：结合口袋的空间特征通常依赖于3D结构，而大规模预测难以获取所有晶体结构或AlphaFold预测结构。

---

## 三：研究思路

**步骤 1：结合口袋的结构重定义与数据集构建**

作者首先分析了10个含配体的A结构域共晶结构，系统比较了6 Å和8 Å截断值下的残基覆盖情况，最终确定了27个残基（27-AA ABP）作为核心结合口袋。同时，构建了包含4,545个A结构域序列的训练数据集。

**步骤 2：基于图神经网络的口袋定位（ABP-GAT模型）**

为了摆脱对MSA的依赖，作者开发了ABP-GAT模型。该模型利用预训练的ESM2提取序列特征，结合ResNet预测的残基接触图构建蛋白质图网络，通过图注意力机制在序列中精确定位上述定义的27个关键残基。

**步骤 3：特征重要性分析与数据增强（SHAP-guided）**

利用随机森林模型和TreeSHAP算法分析27个位点对底物特异性的贡献度。识别出高度保守的结构支撑位点和决定特异性的功能位点。针对非蛋白源性底物数据稀缺的问题，对SHAP贡献度低的位点进行突变（数据增强），扩充训练集。

**步骤 4：基于对比学习的底物预测**

构建双塔模型：一端使用微调的ESM2编码口袋序列（ABP-ESM2），另一端使用MoLFormer编码底物SMILES。通过对比损失函数（Contrastive Loss）拉近匹配的口袋-底物对在向量空间中的距离，推远不匹配对。最后使用核密度估计（KDE）对预测分数进行置信度校准。

**步骤 5：基准测试与应用验证**

在独立测试集上与现有SOTA工具（NRPStransformer, PARAS）进行对比。最后，利用DeepAden对*Streptomyces hygroscopicus* OsiSh-2菌株的基因组进行挖掘，成功关联了两个孤儿基因簇与其对应的代谢产物（nyuzenamides和octaminomycins）。

---

## 四：研究方法

*   **数据集构建**：整合NRPStransformer、PARAS数据集及文献数据，清洗后获得4,545条标记序列和18万+未标记序列。
*   **蛋白质语言模型 (PLM)**：使用 **ESM2-650M** 作为骨干网络，通过LoRA（Low-Rank Adaptation）技术进行微调，生成残基嵌入。
*   **图注意力网络 (GAT)**：用于从接触图（Contact Map）中聚合空间信息，预测口袋残基。
*   **化学语言模型 (CLM)**：使用 **MoLFormer** 编码底物分子的SMILES字符串。
*   **可解释性分析**：使用 **TreeSHAP** 计算特征重要性。
*   **对比学习 (Contrastive Learning)**：采用双向对比损失函数优化口袋和底物的向量表示。
*   **实验验证**：LC-MS/MS非靶向代谢组学分析，结合GNPS分子网络，验证基因簇与产物的对应关系。

---

## 五：实验设计及结果分析

### 研究部分一：结合口袋的重新定义与ABP-GAT模型性能
#### 实验目的与设计
验证27-AA口袋定义的有效性，并评估ABP-GAT模型在不依赖结构输入情况下定位口袋残基的能力。

#### 实验结果与分析
**口袋定义**：通过分析10个共晶结构，发现6 Å范围内的27个残基（27-AA）比8 Å范围的49个残基更能被模型精确恢复（恢复率：0.9980 vs 0.9386）。
**模型性能 (Figure 2)**：
![image.png](http://synbiopath.online/20251230163332441.png)

*   在包含4,545个序列的测试中，ABP-GAT在不同序列一致性区间（0-60% identity）均保持了极高的口袋恢复率。
*   相比基于1amu（GrsA-Phe）的HMM方法，ABP-GAT在**低同源性序列**和**非蛋白源性底物**（Non-proteinogenic substrates）的口袋识别上表现出显著优势。HMM方法在非蛋白源底物上的恢复率大幅下降，而ABP-GAT保持稳定。
>"ABP-GAT maintains high recovery across all identity ranges... whereas the HMM model performed substantially worse for nonproteinogenic substrates."

### 研究部分二：SHAP引导的特征分析与进化洞察
#### 实验目的与设计
利用可解释性AI分析哪些残基决定了底物特异性，并验证其生物学意义。

#### 实验结果与分析
**关键位点识别 (Figure 4)**：SHAP分析突出了8个高贡献位点（如位置20, 24, 27等），这些位点多位于口袋入口的柔性环区或侧链交互区。
![image.png](http://synbiopath.online/20251230163410724.png)

**Ser与Cys的区别 (Figure 5)**：
![image.png](http://synbiopath.online/20251230163441092.png)

*   系统发育树显示识别Ser和Cys的A结构域在序列上分属不同分支。
*   SHAP分析指出**位置20**是区分两者的关键。在Ser结合型中为Pro20（刚性，限制构象），在Cys结合型中为Ala20（柔性，允许重排）。
*   这一发现与晶体结构（PDB 6ea3 vs 7en1）的分析完全一致，证明了模型的生物学可解释性。

### 研究部分三：底物特异性预测性能基准测试
#### 实验目的与设计
对比DeepAden与现有最先进工具（NRPStransformer, PARAS）的预测精度。

#### 实验结果与分析
![image.png](http://synbiopath.online/20251230163508164.png)

*   **总体精度 (Figure 6C)**：在包含201个独立A结构域的基准数据集上，DeepAden的Top-3准确率略优于对比工具（高出2.5-5%）。
*   **低同源性表现 (Figure 6D)**：在与训练集序列一致性较低（<40%）的区间，DeepAden仍保持44.44%的准确率，而NRPStransformer仅为18.18%。PARAS虽然表现不错（50%），但样本量较小。
*   **非蛋白源底物 (Figure 6E)**：这是DeepAden的强项。对于50个非蛋白源性底物样本，DeepAden的Top-1准确率比NRPStransformer高12%，比PARAS高14%。
> "DeepAden demonstrated superior predictive performance, outperforming NRPStransformer by 12% and PARAS by 14% [on non-proteinogenic substrates]."

### 研究部分四：基因组挖掘应用案例（*Streptomyces hygroscopicus*）
#### 实验目的与设计
验证DeepAden在实际基因组挖掘中关联基因簇与代谢产物的能力。

#### 实验结果与分析
**代谢产物鉴定**：通过LC-MS/MS鉴定出两类NRPs：nyuzenamides（双环肽）和octaminomycins（线性肽）。
**基因簇匹配 (Figure 7)**：
![image.png](http://synbiopath.online/20251230163545093.png)

*   **Nyuzenamide BGC**：DeepAden对该基因簇所有A结构域的底物预测与化合物结构的氨基酸序列完全一致。
*   **Octaminomycin BGC**：虽然主要底物预测准确，但对于某些模块（如M23, M24），模型以较低置信度预测了实际存在的替代底物（如Phe替代Tyr，Pip替代Pro），这反映了模型对底物宽泛性（promiscuity）的捕捉能力。

---

## 六：总体结论

DeepAden 是一个具有高度可解释性和鲁棒性的NRPS A结构域底物特异性预测工具。通过结合图注意力网络定位结合口袋和对比学习进行底物匹配，它成功克服了传统方法对序列同源性的依赖。特别是SHAP引导的数据增强策略，显著提升了模型对非蛋白源性底物的预测能力。在实际案例中，DeepAden展示了从基因组到化学结构的精准链接能力，为新型天然产物的发现提供了强有力的工具。

---

## 七：论文评价

### 优点与创新
1.  **方法学创新**：将“口袋定位”与“底物匹配”解耦为两个阶段，利用PLM和GAT在无结构数据的情况下实现了精确的结构特征提取。
2.  **解决痛点**：针对非蛋白源性底物预测难、低同源性序列预测准度差这两个长期存在的痛点，提供了有效的解决方案（数据增强+对比学习）。
3.  **可解释性强**：不仅仅是黑盒预测，通过SHAP值提供了残基水平的功能解释，并得到了晶体学证据的支撑（如Ser/Cys的区别），增强了生物学家的信任度。
4.  **置信度校准**：引入KDE进行概率校准，使得预测分数具有统计学意义，而非单纯的排序。

### 未来研究方向
1.  **多模态融合**：虽然使用了MoLFormer编码底物，未来可引入底物的3D构象信息进行更精细的对接模拟。
2.  **构象动态性**：目前的口袋定义是静态的（27-AA），未来需考虑底物结合过程中的蛋白质构象变化（Induced fit）。
3.  **复杂组装逻辑**：如文中讨论所述，单纯预测A结构域底物不能完全解决非共线性组装（iterative, skipping）的预测问题，需结合C/PCP结构域信息进行全通路预测。

---

## 八：关键问题及回答

#### 问题一：DeepAden 如何在没有蛋白质三维结构输入的情况下，实现精确的结合口袋定位？

**回答：** DeepAden 利用了蛋白质语言模型（ESM2）中蕴含的丰富结构信息。具体而言，ESM2 的注意力图（Attention Map）包含了残基间的接触信息。DeepAden 通过一个 ResNet 模块从 ESM2 的特征中预测残基接触图（Contact Map），构建蛋白质图结构，然后利用图注意力网络（GAT）在这个图上进行节点分类，从而识别出空间上聚集的口袋残基。这使得模型仅凭序列就能“感知”到空间结构。

#### 问题二：为什么 SHAP 引导的数据增强能显著提升模型对非蛋白源性底物的预测性能？

**回答：** 非蛋白源性底物的训练数据非常稀缺，导致模型容易过拟合。传统的随机过采样或随机突变可能会破坏蛋白质的功能结构。SHAP 分析揭示了哪些残基对底物识别至关重要（高SHAP值），哪些是结构支撑或非关键残基（低SHAP值）。作者仅对低SHAP值的位点进行保守突变（使用BLOSUM-62矩阵），这样既增加了样本的多样性，又保留了关键的底物识别特征，生成了符合生物学规律的增强数据，从而提升了模型在稀疏样本上的泛化能力。