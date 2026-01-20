![image.png](http://synbiopath.online/20260120120008534.png)

该研究报道了真菌界中首个同系萜（Homoterpene）生物合成途径的发现，打破了长期以来认为此类化合物仅存在于植物、昆虫和细菌中的认知。作者通过基因组挖掘、体外酶活重构及系统发育分析，揭示了一种独特的“细菌基因水平转移 + 真菌趋同进化”的生物合成逻辑。

---

## 一：基本信息

**文章题目**：Homoterpene Biosynthesis in Fungi

**文章** **DOI** **号**：10.1002/anie.202517837

**期刊名称**：Angewandte Chemie International Edition

**通讯作者**：Lena Barra

**通讯作者工作单位**：康斯坦茨大学化学系 (Department of Chemistry, University of Konstanz, Germany)

## 二：核心速览

### 研究背景

萜类化合物通常遵循“异戊二烯规则”，由整数个 C₅ 单元构成。同系萜 (Homoterpenes) 是一类在碳骨架上含有额外甲基 (C₁) 的非典型萜类。此前，同系萜的生物合成途径主要在植物（通过 P450 介导的 C₄ 单元氧化移除）和细菌（通过甲基转移酶介导的 C₁ 单元添加）中被阐明。在真菌界，尽管其作为萜类化合物的重要来源，此前从未报道过同系萜的生物合成途径。

### 前期研究

细菌中的同系萜合成通常涉及两个关键酶：一个 S-腺苷甲硫氨酸 (SAM) 依赖的甲基转移酶 (MT) 和一个萜类环化酶 (TC)。例如，在变形菌门 (Pseudomonadota) 中发现了结构复杂的 "Greek philosophers" 同系萜（如 sodorifen），而在放线菌门 (Actinomycetota) 中则发现了简单甲基化的 "humanists" 同系萜（如 kantenol）。
![image.png](http://synbiopath.online/20260120120017985.png)


### 本文突破点

1. **真菌界首例**: 首次在真菌（植物病原真菌 _Neonectria ditissima_）中发现并重构了同系萜生物合成途径。
    
2. **新颖骨架**: 发现了一种具有全新 heptamethylbicyclo[3.3.1]nonane 骨架的 C₁₆ 同系倍半萜，命名为 **aspasiadiene (11)**。
    
3. **独特的进化机制**: 揭示了该途径的嵌合进化起源——关键的甲基转移酶 (NdiMT) 源自细菌的水平基因转移 (HGT)，而萜类环化酶 (NdiTC) 则源自真菌内部的趋同进化。
    

### 研究难点

1. **基因簇的沉默与低表达**: 目标基因簇在异源宿主 _E. coli_ 中的表达效率较低，特别是甲基转移酶 NdiMT，这给产物的制备和结构鉴定带来了挑战。
    
2. **中间体的捕捉与鉴定**: 需要精确捕捉并鉴定不稳定的磷酸酯中间体，以确定酶的催化顺序和底物特异性。
    

## 三：研究方法

- **基因组挖掘 (Genome Mining)**: 基于细菌同系萜合成酶的序列特征，对真菌基因组数据库进行BLAST搜索，筛选潜在的 MT-TC 基因对。
    
- **异源表达与体外酶活重建 (Heterologous Expression & In Vitro Reconstitution)**: 将候选基因在 _E. coli_ BL21 中表达，纯化蛋白后与底物 (FPP, GPP, GGPP) 及辅因子 (SAM) 共孵育，通过 GC-MS 检测产物。
    
- **化学结构解析 (Structural Elucidation)**: 利用制备级酶反应（借用细菌同源酶 PchlMT 替代低活性的 NdiMT）大量制备产物，通过高分辨质谱 (HRESIMS) 和多维核磁共振 (1D/2D NMR) 确定化合物的平面及立体结构。
    
- **系统发育分析 (Phylogenetic Analysis)**: 构建最大似然树，分析真菌 MT 和 TC 与细菌同源蛋白的进化关系，推断基因起源。
    

## 四：实验设计及结果分析

### 研究部分一：真菌同系萜生物合成基因簇的发现

旨在通过生物信息学手段，在真菌基因组中寻找类似于细菌“甲基转移酶 (MT) + 萜类环化酶 (TC)”的基因组合，以挖掘潜在的同系萜生物合成途径。

- **Figure 2a & Table S1**: 研究者在苹果溃疡病病原真菌 _Neonectria ditissima_ 中鉴定到一个推测的基因簇 (_ndi_)。该基因簇包含一个 I 型萜类环化酶 (**NdiTC**) 和一个 I 类甲基转移酶 (**NdiMT**)，并由调节元件 (NdiR1-3) 和转运蛋白 (NdiT) 侧翼包围。
    ![image.png](http://synbiopath.online/20260120120026235.png)


- **序列分析**: NdiTC 与担子菌 _Coprinopsis cinerea_ 的倍半萜合酶 COP4 具有 31% 的氨基酸序列一致性 (aaSI)；而 NdiMT 与参与生物素合成的丙二酰-ACP O-甲基转移酶 BioC 具有 30% aaSI。值得注意的是，NdiMT 与已知的细菌同系萜甲基转移酶（如 _Pseudomonas lini_ 的 PlMTα）序列一致性较低 (最高 42%)，但保留了关键的二磷酸结合基序 (Figure S1)。这表明该基因簇具有合成同系萜的潜力，但其序列特征与已知细菌途径存在差异。
    

### 研究部分二：生物合成途径的体外重构

为了验证 NdiMT 和 NdiTC 的功能，研究者将这两个基因在 _E. coli_ 中进行异源表达，纯化蛋白后进行体外酶活测定。实验设置了不同的底物 (GPP, FPP, GGPP) 和酶组合，利用 GC-MS 分析产物。

**Figure 2b & 2c**:
![image.png](http://synbiopath.online/20260120120031668.png)

- 当 NdiMT 和 NdiTC 与 FPP (C₁₅) 和 SAM 共同孵育时，GC-MS 检测到一个明显的产物峰，其质荷比 (m/z) 为 218 (Figure 2b)。这与 C₁₆ 烃类化合物的分子量一致，表明发生了甲基化和环化。
    
- 单独孵育 NdiMT、FPP 和 SAM 时，检测到一个 m/z 236 的产物 (Figure 2c)，推测为醇类中间体（磷酸基团水解后）。
    
- **对照实验**: NdiTC 单独无法转化 FPP (Figure S5B)；NdiMT 或 NdiTC 均不能转化 GPP 或 GGPP (Figure S2, S6)。
    

**结论**: NdiMT 和 NdiTC 构成了一个功能性的生物合成途径，特异性地利用 FPP 作为底物，通过 SAM 介导的甲基化和随后的环化反应生成同系倍半萜。

### 研究部分三：中间体鉴定与终产物结构解析

确定 NdiMT 催化的中间体结构，并解析最终产物 **11** 的精确化学结构。由于 NdiMT 表达量低，研究者利用细菌来源的同源酶 PchlMT 辅助制备中间体。

**Figure 3a-d (中间体鉴定)**:
![image.png](http://synbiopath.online/20260120120042812.png)


- NdiMT 的产物 (m/z 236) 的 EI 质谱图显示出 m/z 137 的基峰，这与细菌同系萜途径中的 presodorifen alcohol (**8b**) 高度相似。
    
- 研究者克隆并表达了细菌来源的 presodorifen diphosphate 合酶 **PchlMT**。GC-MS 分析显示，PchlMT 的产物与 NdiMT 的产物具有完全一致的保留时间和质谱指纹 (Figure 3a, 3b)。
    
- 进一步地，NdiTC 能够将 PchlMT 生成的中间体转化为与原 NdiMT/NdiTC 反应相同的最终产物 (Figure 3c, 3d)。
    
- **结论**: 确认 NdiMT 的功能是催化 FPP 甲基化生成 **presodorifen diphosphate (8a)**。
    

**Figure 3e & Table S2 (终产物结构)**:
![image.png](http://synbiopath.online/20260120120049454.png)

- 通过 PchlMT 和 NdiTC 的联用，研究者制备了 0.5 mg 的最终产物。
    
- 综合 1D 和 2D NMR 数据（特别是 ¹H-¹H COSY 和 HMBC 相关信号），确定该化合物为一种具有 heptamethylbicyclo[3.3.1]nonane 骨架的新颖同系倍半萜。
    
- 该化合物被命名为 **aspasiadiene (11)**。其结构与细菌产生的 "Greek philosophers" 同系萜（如 sodorifen **7**）在骨架上截然不同，显示了真菌环化酶独特的催化产物特异性。
    

> "Based on these analyses, the structure of the NdiTC product was assigned as aspasiadiene (11), an unprecedented heptamethyl bicyclo[3.3.1]nonane hydrocarbon."

### 研究部分四：进化起源分析

为了探究真菌如何获得这一通常存在于细菌中的代谢途径，研究者对 NdiMT 和 NdiTC 进行了系统发育分析。

**Figure 4**:
![image.png](http://synbiopath.online/20260120120056702.png)


- **NdiMT (Figure 4b)**: 在系统发育树中，真菌来源的 NdiMT 与细菌来源的 SodC 及其同源蛋白（产生 presodorifen diphosphate 的酶）聚类在同一个分支上。这强烈暗示了 **NdiMT 是通过水平基因转移 (HGT) 从细菌（可能是变形菌门）获得**的。
    ![image.png](http://synbiopath.online/20260120120102292.png)


- **NdiTC (Figure 4c)**: 与 MT 不同，NdiTC 并没有与细菌的同系萜环化酶 (如 SodD) 聚类。相反，它与典型的真菌 I 型萜类环化酶（如 aristolochene synthase）聚在一起，且与细菌 SodD 的序列一致性极低 (<16%)。
    
- **结论**: 这表明 NdiTC 并非通过 HGT 获得，而是由真菌祖先的萜类环化酶通过**趋同进化 (convergent evolution)** 获得了代谢 presodorifen diphosphate 的能力。这揭示了一种独特的“细菌招募 + 真菌创新”的进化模式。
    

## 五：总体结论

本研究首次证实了真菌界具备生物合成同系萜（homoterpenes）的能力。以植物病原真菌 _Neonectria ditissima_ 为模型，阐明了由甲基转移酶 NdiMT 和萜类环化酶 NdiTC 组成的生物合成途径。该途径首先将 FPP 转化为细菌型中间体 presodorifen diphosphate，随后通过真菌特有的环化酶将其转化为结构新颖的 C₁₆ 化合物 aspasiadiene (**11**)。进化分析表明，该途径是真菌通过水平转移获取细菌甲基转移酶基因，并将其与自身进化的环化酶功能整合的结果。

## 六：论文评价

### 优点与创新

1. **填补进化空白**: 首次将同系萜的生物合成版图扩展到了真菌界，挑战了该类化合物仅限于植物和细菌的传统观点。
    
2. **进化机制的深刻洞察**: 提出的“HGT + 趋同进化”模型非常引人入胜，解释了真菌如何利用外源基因资源并结合自身代谢背景创造新的化学多样性。
    
3. **严谨的生化确证**: 通过借用细菌同源酶 PchlMT 巧妙解决了真菌酶表达量低的问题，成功实现了中间体和终产物的制备与鉴定，逻辑严密，数据详实。
    

### 未来研究方向

1. **生态功能探索**: _N. ditissima_ 是苹果树溃疡病的病原菌，aspasiadiene (**11**) 是否作为致病因子、种间信号分子或防御化合物参与宿主-病原体相互作用，值得深入研究。
    
2. **催化机理研究**: NdiTC 如何将 presodorifen diphosphate 环化为独特的 bicyclo[3.3.1]nonane 骨架？其环化机制与细菌 SodD 有何不同？这需要进一步的晶体结构和机理研究。
    
3. **广泛性挖掘**: 基于本研究建立的挖掘策略，在其他真菌基因组中寻找类似的 MT-TC 基因对，可能会发现更多结构新颖的同系萜。
    

## 七：关键问题及回答

#### **问题一：真菌同系萜的生物合成策略与植物和细菌有何不同？**

**回答：**

- **植物**: 采用“减法”策略。通常由 P450 酶氧化切除 C₂₀ (GGPP) 或 C₁₅ (FPP) 前体末端的 C₄ 单元，生成 C₁₆ (TMTT) 或 C₁₁ (DMNT) 同系萜 (Figure 1a)。
    
- **细菌**: 采用“加法”策略。利用 SAM 依赖的甲基转移酶在 FPP 或 GPP 上添加 C₁ 单元，随后进行环化 (Figure 1c)。
    
- **真菌 (本研究)**: 采用与细菌类似的“加法”策略，即 SAM 介导的甲基化。但其独特之处在于，真菌通过 HGT 获得了细菌的甲基化能力，却利用自身进化的环化酶产生结构截然不同的骨架。
    

#### **问题二：为什么研究者认为 NdiTC 是趋同进化的产物，而不是通过 HGT 获得的？**

**回答：** 系统发育分析 (Figure 4c) 显示，NdiTC 与细菌的同系萜环化酶 (SodD) 在进化树上距离极远，且序列一致性极低 (<16%)。相反，NdiTC 稳固地聚类在真菌典型的 I 型萜类环化酶分支中（如 aristolochene synthase）。这表明 NdiTC 是从真菌自身的萜类合酶祖先演化而来，独立获得了识别并环化甲基化底物 (presodorifen diphosphate) 的能力，而非直接从细菌水平转移而来。

#### **问题三：本研究中 NdiMT 表达量低的问题是如何解决的？这说明了什么？**

**回答：** NdiMT 在 _E. coli_ 中的可溶性表达产量极低，不足以制备足够的中间体用于结构分析。研究者利用了细菌来源的同源酶 PchlMT（来自 _Pseudomonas chlororaphis_）作为替代。PchlMT 表达效率高，且被证实能产生与 NdiMT 相同的中间体 (presodorifen diphosphate)。这一策略的成功不仅解决了技术难题，也从生化功能的角度有力地佐证了 NdiMT 与细菌 MT 的功能保守性。