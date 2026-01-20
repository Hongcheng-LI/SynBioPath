![image.png](http://synbiopath.online/20260120114139760.png)


---

## 一：基本信息

**文章题目**：Biosynthesis of the Biphenomycin Family of Potent Antibiotics

**文章** **DOI** **号**：10.1002/anie.202516156

**期刊名称**：Angewandte Chemie International Edition

**通讯作者**：Tobias A. M. Gulder

**通讯作者工作单位**：亥姆霍兹药物研究所（Helmholtz Institute for Pharmaceutical Research Saarland，HIPS）；德累斯顿工业大学（Technical University of Dresden）

## 二：核心速览

### 研究背景

联苯霉素类 (Biphenomycins) 是一类具有大环肽结构的细菌天然产物，其分子特征是含有通过联芳基键 (biaryl linkage) 连接的独特邻位-酪氨酸 (_ortho_-tyrosine, _o_Tyr) 残基。这类化合物对革兰氏阳性菌表现出强效的抗菌活性，且对真核细胞毒性低，具有作为新型抗生素的开发潜力。尽管联苯霉素早在 1967 年即被发现，但其完整的生物合成途径一直未能被阐明，这限制了对其进行生物工程改造和发现新型类似物。
![Uploading file...qg64h]()


### 前期研究

在本项目启动之前，关于联苯霉素的生物合成来源（是核糖体途径还是非核糖体途径）、关键结构单元（如 _o_Tyr 和联芳基键）的形成机制、以及前体肽的成熟过程均是未知的。这为本研究提供了一个从头解析全新生物合成途径的机会。

### 本文突破点

本文的核心突破在于首次完整地阐明了联苯霉素家族的生物合成全过程，并揭示了其中涉及的一系列具有新颖功能的酶。研究证实联苯霉素来源于核糖体合成与翻译后修饰途径 (Ribosomally synthesized and Post-translationally modified Peptide, RiPP)，并详细解析了每一步酶促成熟反应：

1. **发现了具有双重功能的酶 BipEF**：一个多核非血红素铁依赖性氧化酶 (multinuclear nonheme iron-dependent oxidase, MNIO) BipE 与其伴侣蛋白 BipF 形成的复合物，不仅负责催化两个苯丙氨酸残基的选择性邻位羟基化以生成 _o_Tyr，还在特定条件下（缺少 Fe²⁺ 和 DTT）表现出 N-端蛋白酶解活性。
    
2. **解析了关键的 C-C 偶联反应**：证实了由一个 B12-依赖性自由基 SAM (radical SAM, rSAM) 酶 BipD 催化两个 _o_Tyr 残基之间的联芳基 C-C 键形成，从而构建大环结构。
    
3. **阐明了侧链修饰与蛋白酶解过程**：鉴定了一个高区域选择性的精氨酸酶 BipC、多个专一的羟化酶（BipG, BipH）以及一个独特的、无需辅助因子即可同时进行 N-端和 C-端切割的 TldD-样蛋白酶 BipI。
    

### 研究难点

本研究的主要难点在于从头解析一个全新的、包含多个功能未知酶的完整 RiPP 生物合成途径。这包括：1) 在没有遗传学线索的情况下，从头鉴定负责生物合成的基因簇 (_bip_ BGC)；2) 表达并功能性表征多个此前未知的酶，特别是具有新颖双重功能或催化罕见化学反应的酶（如 BipEF, BipI）；3) 在体外重构多步酶促级联反应，以确定正确的反应顺序。

## 三：研究方法

- **基因组挖掘与测序**: 对已知的联苯霉素产生菌 _Streptomyces griseorubiginosus_ No. 43708 进行 PacBIO SMRT 测序，并使用 antiSMASH 等生物信息学工具分析其基因组，以鉴定候选的生物合成基因簇 (_bip_ BGC)。
    
- **异源表达与基因功能确证**: 在大肠杆菌 (_Escherichia coli_) 中对 _bip_ 基因簇中的酶进行单独或组合表达。通过在体外 (in vitro) 将纯化的酶与合成的前体肽底物共孵育，或在体内 (in vivo) 共表达多个酶和前体肽，来验证每个酶的具体生化功能。
    
- **液相色谱-高分辨质谱**: 作为核心分析工具，用于检测和鉴定酶促反应的产物。通过精确的质量数变化（如羟基化+16 Da，脱胍基-42 Da，C-C 偶联-2 Da）和 MS/MS 碎片分析来确定修饰的类型和位点。
    
- **定点诱变**: (虽然文中未详细展开，但作为标准方法，在研究酶催化机制时通常会使用) 用于验证酶活性位点的关键氨基酸残基。
    
- **蛋白表达与纯化**: 利用带有亲和标签（如 His-tag, MBP-tag）的表达系统，在 _E. coli_ 中大量制备生物合成酶，并通过亲和层析进行纯化，用于后续的体外酶学实验。
    

## 四：实验设计及结果分析

### 研究部分一：联苯霉素生物合成基因簇 (_bip_ BGC) 的鉴定

研究的第一步是从已知的产生菌 _S. griseorubiginosus_ 中找到负责联苯霉素合成的基因簇。由于其来源未知（RiPP 或 NRPS），作者首先排除了 NRPS 途径的可能性，然后基于 RiPP 的特征，在其基因组中搜索编码核心肽序列 (Phe-Arg-Phe-Arg-Ser, FRFRS) 的小基因。

- **(图 2)** 通过基因组测序和生物信息学分析，成功在 _S. griseorubiginosus_ 中鉴定出一个候选的 RiPP 基因簇，命名为 _Sg_bip_。该基因簇的核心是一个编码 41 个氨基酸前体肽的基因 _Sg_bipA_，其 C-末端恰好包含 FRFRS 序列。
    

![](https://synbiopath.feishu.cn/space/api/box/stream/download/asynccode/?code=NjdkNThjODI1ZjVjN2VhYjI4MmMzMzU3MWVlOGM5YmRfeGFpVnBqaGE5dVdTRWFHRVk3d1RsRFlIdmQwSzZlZkZfVG9rZW46WmhrOGJtUVV2b2RnSGt4cEp3emNuWHdWblNoXzE3NjUxODg4NzU6MTc2NTE5MjQ3NV9WNA)

- 基因簇还包含一系列编码假定修饰酶的基因，包括 _bipE_ (MNIO), _bipD_ (rSAM), _bipC_ (UPF0489 家族，可能为精氨酸酶), _bipG_ (JmjC 羟化酶), 和 _bipI_ (TldD 蛋白酶) 等，这些酶的功能与合成联苯霉素所需的化学转化（羟化、C-C 偶联、侧链修饰、蛋白酶解）高度吻合。
    
- 为进一步验证该基因簇的功能，作者测序了另一个产生菌 _S. filipinensis_，发现了几乎相同的 _bip_ 基因簇。更重要的是，作者从一个公共菌株库中筛选出一个含有类似基因簇的菌株 _Peribacillus simplex_D_，并实验证明该菌株能够产生联苯霉素 B (**7b**)，从而将 _bip_ 基因簇与联苯霉素的合成直接关联起来。
    

### 研究部分二：BipEF 的双重功能：邻位羟化与 N-端蛋白酶解

联苯霉素的核心结构是 _o_Tyr。前体肽 BipA 中对应位置是苯丙氨酸 (Phe)。因此，必然存在一个或多个羟化酶。BipE 被注释为 MNIO，是该反应的主要候选酶。本部分旨在通过体外酶学实验验证 BipE 及其伴侣蛋白 BipF 的功能。

**(图 3)** 作者在 _E. coli_ 中共表达了 BipE 和 BipF，并证实它们形成异质二聚体复合物 BipEF。

![](https://synbiopath.feishu.cn/space/api/box/stream/download/asynccode/?code=MWEyMDRlY2Y4ZjYxM2NjYTAxYjcyN2NhMDAyM2Q1OTBfWGFwSnUzZ0lJMnVaYmxwMExLWVo5a2dzWjhzNHZTZ0FfVG9rZW46SDU2M2JJRGlQb2lzc1d4UlN4ZmN6VDZUblNjXzE3NjUxODg4NzU6MTc2NTE5MjQ3NV9WNA)

**体外酶活实验揭示了其条件依赖的双重功能**：

- **在 Fe²⁺ 和 DTT 存在下**，BipEF 表现出**二羟化酶活性**。LC-MS 分析显示，前体肽 BipA 的质量数增加了 32 Da，MS/MS 碎片分析确认两个羟基分别加在了两个 Phe 残基上，生成了含有两个 _o_Tyr 的产物。
    
- **在 Fe²⁺ 和 DTT 缺失时**，BipEF 的活性发生戏剧性转变，表现出**N-端蛋白酶解活性**，能够切除前体肽的先导肽 (Leader Peptide, LP) 部分。
    

这一发现极为新颖，首次报道了 MNIO 家族酶具有这种条件依赖的催化功能切换，既是羟化酶又是蛋白酶。

### 研究部分三：侧链修饰酶 BipC 和 BipG 的功能表征

联苯霉素的骨架中含有一个中央的鸟氨酸 (Orn) 或 γ-羟基鸟氨酸残基，而前体肽 BipA 中对应的是精氨酸 (Arg)。因此，需要一个精氨酸酶将 Arg 转化为 Orn，以及一个羟化酶引入 γ-羟基。本部分旨在验证 BipC 和 BipG 的功能。

- **(图 4)** **BipC 是一个高区域选择性的精氨酸酶**。体外实验表明，纯化的 BipC 能够催化前体肽 BipA 脱去胍基，将 Arg 转化为 Orn，导致质量数减少 42.02 Da。值得注意的是，BipA 的核心肽序列是 F-R-F-R-S，含有两个 Arg 残基。MS/MS 碎片分析（对比 y₃ 和 y₄ 离子）精确地证明，BipC **只水解位于两个 Phe 之间的 Arg**，而对 C-末端的 Arg 无活性，表现出极高的区域选择性。
    

![](https://synbiopath.feishu.cn/space/api/box/stream/download/asynccode/?code=ZjZiYWJmNTBkMDg0NDFkYTQ0MWRkMWMzMGVmZmFhZDFfeFNLYklTd1pwN1JoWXcxMWtDNm41aFBLNUI3MVF1Z1BfVG9rZW46TnV2UWJxazJhb2REUUt4SDc0T2NHMlQxblhUXzE3NjUxODg4NzU6MTc2NTE5MjQ3NV9WNA)

- **(图 5)** **BipG 是一个 γ-鸟氨酸羟化酶**。体外实验证实，BipG 能够催化含有 Orn 的前体肽发生羟基化，质量数增加 15.99 Da。该酶的底物是 Orn，而不是 Arg，表明其在生物合成途径中的作用顺序位于 BipC 之后。
    

![](https://synbiopath.feishu.cn/space/api/box/stream/download/asynccode/?code=MzZiMWZjZTAyOGVlMTdhODhmZWFkNjlmYzRiZWRkOTBfTHZjTDVSMEFXbEZ1SEVnNnRWcUlBS0xJZllkeXFVYjlfVG9rZW46WlR6WWJHaXAxb0xqRXh4ZHJCMGNWQWpsblhlXzE3NjUxODg4NzU6MTc2NTE5MjQ3NV9WNA)

### 研究部分四：关键大环化步骤：BipD 催化的联芳基偶联

联苯霉素的大环结构是通过两个 _o_Tyr 残基的 C-C 偶联形成的。BipD 被注释为 B12-依赖性 rSAM 酶，是催化该反应的最可能候选者。由于 rSAM 酶的体外重构复杂，作者设计了在 _E. coli_ 中的体内重构实验来验证其功能。

- **(图 6)** 作者在 _E. coli_ 中共表达了前体肽 BipA 以及催化上游所有修饰的酶（BipEF, BipC）和 BipD。
    

![](https://synbiopath.feishu.cn/space/api/box/stream/download/asynccode/?code=N2QxYWFkNWFkZmMwODQxZmI3NmEwODMxZDE2Njc2NDlfREJWWlRCbnN6Z1JIbzFJUkNPVEN6cjlXMzJydHdLYW1fVG9rZW46QzVib2JiNXJKb0RRTmN4eERGWGNrZXVjbkxjXzE3NjUxODg4NzU6MTc2NTE5MjQ3NV9WNA)

- LC-MS 分析显示，在表达了 BipD 的体系中，检测到了一个质量数相比其线性前体减少了 2 Da 的产物（例如，从 m/z 652.99 变为 652.31）。这一质量变化是 C-C 键形成（脱去两个氢原子）的典型特征，从而提供了直接证据，证实 **BipD 负责催化联芳基键的形成**，完成大环化。
    
- 实验还表明，该反应需要 B12 辅酶和还原系统，符合 rSAM 酶的催化特性。
    

### 研究部分五：BipI 的双向蛋白酶解活性与完整生物合成途径

RiPP 成熟的最后一步通常是蛋白酶解，切除先导肽 (LP) 和（如果存在）尾随肽 (FP)，释放出成熟的核心肽。BipI 被注释为 TldD-样金属蛋白酶。本部分旨在验证 BipI 的功能，并整合所有结果，提出完整的生物合成途径。

**(图 7)** 体外实验表明，BipI 是一个功能强大的蛋白酶。与典型的 TldD 酶不同，**BipI 无需 TldE 伴侣蛋白即可发挥高效活性**。

![](https://synbiopath.feishu.cn/space/api/box/stream/download/asynccode/?code=Yjk2NDg4ZjJmYmNhZjgxOWU4ZWNhZmVjMjMyMjFlMmFfYnBCV2Vnd1dsc0NGbWt6czM1R1R5bnNsY3FUOXcxMFBfVG9rZW46TkJXVmI3WWFsb2RZTmp4WXlrd2N6R1l4bkRkXzE3NjUxODg4NzU6MTc2NTE5MjQ3NV9WNA)

更重要的是，BipI 表现出**双向切割活性**。它不仅能切除 N-端的 LP，还能切除 C-端的 FP。作者通过检测反应产物（释放的 LP、FP、CP-FP 和最终的 CP），证明了 BipI 采用一种“渐进式”或“铅笔刀”模型，先切 N-端，再切 C-端。

**(图 8)** 基于以上所有实验结果，作者提出了联苯霉素家族完整的生物合成途径：

![](https://synbiopath.feishu.cn/space/api/box/stream/download/asynccode/?code=MWVlYjI5MzcyMjQ4ODMwODQxYTNlOTI4ZGRkZWY2NTRfNHVEbk1ncXZlUUY3QUo1ejRMNmhoNFJkdHRiTXhXa0pfVG9rZW46TkptNmJ0d2J6b3BwZjl4U2F4R2NMV0hObnljXzE3NjUxODg4NzU6MTc2NTE5MjQ3NV9WNA)

1. 核糖体合成前体肽 BipA (**8**)。
    
2. BipEF 催化双-邻位羟基化，生成含两个 _o_Tyr 的中间体 (**9**)。
    
3. BipC 区域选择性地将中央的 Arg 水解为 Orn (**10**)。
    
4. BipD 催化联芳基偶联，形成大环 (**11**)。
    
5. BipG 催化 Orn 的 γ-羟基化 (**12**)。
    
6. 在 _S. griseorubiginosus_ 中，BipH 进一步催化 C-末端 _o_Tyr 的 β-羟基化，生成 **13**。
    
7. 最后，蛋白酶 BipI 进行 N-端和 C-端的切割，释放出成熟的联苯霉素 A (**7a**) 或 B (**7b**)，或 C (**7c**)。
    

## 五：总体结论

本研究通过结合基因组挖掘、体内外功能重构和详细的生化分析，首次完整地阐明了强效抗生素联苯霉素家族的核糖体生物合成途径。研究揭示了该途径中每一步翻译后修饰的酶学基础，包括由一个具有新颖双重功能的 MNIO 酶 BipEF 催化的邻位羟基化、由 B12-依赖性 rSAM 酶 BipD 催化的大环化 C-C 偶联、以及由一系列高选择性酶（BipC, BipG, BipH）催化的侧链修饰。特别值得注意的是，研究发现了一个独特的、自给自足的 TldD-样蛋白酶 BipI，它能独立完成前体肽的 N-端和 C-端双向切割。这项工作不仅彻底解决了联苯霉素生物合成这一长期存在的科学问题，还发现了一系列具有新颖催化功能的酶，为生物催化和合成生物学提供了宝贵的工具，并为通过基因组挖掘发现新型联苯霉素类似物和进行生物工程改造以提高产量和活性奠定了坚实的理论基础。

## 六：论文评价

### 优点与创新

1. **研究的完整性与系统性**：该研究从零开始，完整解析了一个复杂的天然产物生物合成途径的每一步，逻辑清晰，证据确凿。这是一个系统生物化学研究的杰出典范。
    
2. **发现多种新颖的酶学功能**：本研究的亮点在于发现了多个具有前所未见功能的酶。特别是 BipEF 的条件依赖性双功能（羟化酶/蛋白酶）和 BipI 的自给自足双向切割功能，极大地丰富了我们对 RiPP 成熟酶催化多样性的认识。
    
3. **严谨的实验设计**：研究综合运用了多种前沿技术。例如，通过在不同物种中验证基因簇功能、体外重构多酶体系、体内重构关键步骤等，构建了坚实的证据链。对 BipC 区域选择性的 MS/MS 解析尤为精妙。
    
4. **潜在的应用价值**：阐明完整的生物合成途径为通过合成生物学方法（如异源表达、启动子替换）提高联苯霉素产量提供了路线图。同时，新发现的酶（如 BipC, BipG, BipI）本身也可能作为生物催化工具，用于其他肽的定点修饰。
    

### 未来研究方向

1. **结构生物学研究**：解析关键酶（特别是 BipEF, BipD, BipI）与其底物复合物的晶体或冷冻电镜结构，将从原子层面揭示其新颖催化机制的分子基础。
    
2. **BipEF 双功能切换的调控机制**：深入研究细胞内氧化还原环境（Fe²⁺/DTT 的生理等效物）如何精确调控 BipEF 在羟化和蛋白酶解功能之间的切换，这可能揭示一种新的酶活性调控模式。
    
3. **生物工程与药物发现**：利用已阐明的生物合成途径，通过组合生物合成或前体导向生物合成等策略，创造新型的联苯霉素衍生物，并筛选其抗菌活性，以期获得性能更优的抗生素候选药物。
    
4. **靶向基因组挖掘**：利用本研究中鉴定的关键酶（如 BipE, BipD）的序列作为探针，在更广泛的微生物基因组数据库中进行靶向挖掘，以发现更多结构多样、功能独特的联苯霉素类天然产物。
    

## 七：关键问题及回答

#### **问题一：研究者是如何确定联苯霉素是 RiPP 而不是 NRPS 来源的？**

**回答：** 研究者通过基因组分析排除了 NRPS 来源，并找到了支持 RiPP 来源的直接证据：

1. **排除 NRPS**：对产生菌的基因组进行分析，虽然发现了一个 NRPS 基因簇，但其结构和预测的底物特异性与合成联苯霉素所需的氨基酸（Phe, Arg, Ser）不符，因此排除了其作为候选途径的可能性。
    
2. **找到 RiPP 证据**：RiPP 的核心特征是存在一个编码前体肽的小基因。研究者以联苯霉素的核心氨基酸序列 (FRFRS) 为线索，在基因组中搜索编码该序列的基因。他们成功找到了一个名为 _bipA_ 的小基因，它编码一个 41 氨基酸的前体肽，其 C-末端正好是 FRFRS 核心肽序列，前面还有一个典型的先导肽序列。这个 _bipA_ 基因位于一个包含多种翻译后修饰酶的基因簇中，这完全符合 RiPP 生物合成基因簇的典型组织结构，从而确立了其 RiPP 来源。
    

#### **问题二：BipEF 的“双重功能”具体指什么？这一发现有何重要性？**

**回答：** BipEF 的“双重功能”指的是它可以在不同反应条件下催化两种完全不同的化学反应：

1. **邻位羟化酶功能**：在有辅因子 Fe²⁺ 和还原剂 DTT 的条件下，BipEF 催化前体肽中的两个苯丙氨酸残基发生邻位羟基化，生成 _ortho_-酪氨酸 (_o_Tyr)。这是其在联苯霉素生物合成中的主要生理功能。
    
2. **蛋白酶功能**：在**缺少** Fe²⁺ 和 DTT 的条件下，BipEF 的催化活性发生改变，转而对前体肽的 N-端进行切割，表现出蛋白酶活性。
    

这一发现的重要性在于：它首次揭示了 MNIO 这一类酶可以具有条件依赖性的催化功能“开关”。这不仅是一个新颖的酶学现象，也提示了细胞可能通过调控局部微环境（如氧化还原状态）来控制酶的功能，为理解酶的催化多样性和调控复杂性提供了新的视角。

#### **问题三：研究如何证明 BipD 催化了联芳基 C-C 键的形成？**

**回答：** 证明 BipD 功能的关键证据来自于**体内重构实验**和**精确的质谱分析** (图 6e)：

1. **实验设计**：由于 rSAM 酶体外反应条件苛刻，研究者选择在 _E. coli_ 中进行体内重构。他们共表达了合成线性、修饰后前体所需的所有组分（前体肽 BipA、羟化酶 BipEF、精氨酸酶 BipC）以及目标酶 BipD。
    
2. **核心检测方法**：联芳基 C-C 键的形成是一个氧化偶联反应，会脱去两个氢原子。因此，反应产物的分子量会比其线性前体精确地减少 2 Da。
    
3. **实验结果**：LC-MS 分析显示，在完整表达了 BipA, BipEF, BipC 和 BipD 的体系中，可以检测到一个新产物，其质谱峰的 m/z 值（例如，[M+3H]³⁺ 离子峰从 652.98 变为 652.31）精确地对应于分子量减少了 2 Da。而在缺少 BipD 的对照组中则没有这个产物。
    

这个 -2 Da 的质量变化是 C-C 键形成的“指纹”信号，为 BipD 催化联芳基偶联反应提供了确凿的证据。