![image.png](http://synbiopath.online/20251226230206798.png)


## 一：基本信息

**文章题目**：An Aspergillus nidulans Platform for the Complete Cluster Refactoring and Total Biosynthesis of Fungal Natural Products

**文章** **DOI** **号**：10.1021/acssynbio.0c00536

**期刊名称**：ACS Synthetic Biology

**通讯作者**：Clay C. C. Wang; Yi-Ming Chiang

**通讯作者工作单位**：

- **Clay C. C. Wang**: 南加州大学 (University of Southern California)
    
- **Yi-Ming Chiang**: 南加州大学 (University of Southern California)；嘉南药理大学 (Chia Nan University of Pharmacy and Science)
    

## 二：核心速览

### 研究背景

真菌天然产物 (Fungal Natural Products, NPs) 是药物的重要来源，但其在天然宿主中产量低、合成途径复杂，限制了其开发应用。异源表达，即将整个生物合成基因簇 (BGC) 转移到一个易于操作的模式宿主中进行生产，是解决这一瓶颈的有效策略。然而，现有的异源表达系统往往效率不高，难以实现对复杂、多基因 BGC 的完整重建和高产。

本研究的核心科学问题是：**能否开发一个全新的、高效的、标准化的异源表达平台，实现对完整真菌 BGC 的“重构”(refactoring) 和目标产物的“全生物合成”(total biosynthesis)。**

### 前期研究

在此之前，已有多种策略用于在模式真菌（如米曲霉 _Aspergillus oryzae_、构巢曲霉 _Aspergillus nidulans_）中进行异源表达。这些策略通常使用组成型或可诱导的初级代谢启动子（如 _gpdA_, _alcA_）来驱动单个或少数几个基因的表达。然而，当面对一个包含十几个基因的复杂 BGC 时，如何协调所有基因的表达，使其像在天然宿主中一样高效协同工作，一直是一个巨大的挑战。利用天然 BGC 的内源调控元件（如通路特异性转录因子）来驱动整个基因簇的协同表达，被认为是一种更有前途但技术上更难实现的策略。

### 本文突破点
![image.png](http://synbiopath.online/20251226230233315.png)


1. **方法学创新：开发了“afo regulon”平台**：首次提出并成功实践了一种全新的“基因簇重构”策略。该策略巧妙地利用了构巢曲霉 (_A. nidulans_) 内源 asperfuranone 基因簇 (`afo` 簇) 的调控系统。通过将外源 BGC 的所有基因编码区 (CDS) 逐一替换掉 `afo` 簇中对应基因的 CDS，同时保留 `afo` 簇完整的启动子、终止子和调控网络，从而实现对外源基因簇的“即插即用”式高效协同表达。
    
2. **实现了复杂 BGC 的高效重建**：利用该平台，成功地将两个来自不同真菌的、具有重要药用价值的复杂 BGC——citreoviridin BGC (4个基因) 和 pleuromutilin BGC (7个基因)——完整地在 _A. nidulans_ 中进行了重构和全生物合成。
    
3. **实现了高产**：通过该平台表达的 citreoviridin 产量高达 **615.7 mg/L**，pleuromutilin 产量高达 **~150 mg/L**。这些产量不仅远高于之前的报道，甚至达到了具有工业化生产潜力的水平，充分证明了该平台的卓越性能。
    
4. **技术流程的简化与高效**：整个流程基于 Gibson assembly 和体内同源重组，无需传统的限制性内切酶克隆和酵母穿梭载体，大大简化了操作，缩短了实验周期，使得对长达 35 kb 的外源 DNA 进行整合成为可能。
    

### 研究难点

1. **多基因、大片段 DNA 的无缝组装与整合**：要将一个包含 7 个基因、总长度超过 20 kb 的外源 DNA 片段精确地整合到宿主基因组的特定位点，是一项巨大的分子生物学挑战。
    
2. **保证所有基因的协同、高水平表达**：如何确保导入的多个外源基因能够被宿主转录和翻译机器高效识别，并以正确的时序和比例进行表达，是异源表达成功的关键。
    
3. **避免宿主内源代谢的干扰**：_A. nidulans_ 自身会产生多种次级代谢产物，可能会干扰目标产物的检测或与外源途径竞争前体。
    

## 三：研究方法

- **基因簇重构 (Cluster Refactoring)**：这是本文的核心策略。首先，选择 _A. nidulans_ 中一个表达水平极高且调控机制清晰的内源 BGC（`afo` 簇）作为“底盘”或“机箱”。然后，通过同源重组，将目标外源 BGC 的基因编码区 (CDS) 逐一替换掉 `afo` 簇中相应基因的 CDS，但完整保留 `afo` 簇的启动子、终止子和基因间区域。
    
- **体内同源重组 (In vivo Homologous Recombination)**：利用 _A. nidulans_ 自身高效的同源重组能力，将多个线性的、带有重叠末端的大片段 DNA（通过 Gibson assembly 和 PCR 制备）**共转化**到宿主原生质体中。细胞内的重组机制会自动将这些片段与基因组以及彼此进行无缝拼接，从而在目标位点原位组装成一个完整的、重构后的人工基因簇。
    
- **可诱导表达系统**：整个重构后的基因簇的表达，受 `afo` 簇的天然正调控因子 AfoA 的控制。通过将 `afoA` 基因置于一个可诱导的启动子 (_PalcA_) 之下，研究人员可以精确地控制整个外源 BGC 的“开关”。
    
- **Gibson Assembly**：一种高效的体外 DNA 无缝连接技术，用于将多个 PCR 扩增的 DNA 片段（如外源基因 CDS、`afo` 簇的基因间区域）预先组装成更大的 DNA 模块，作为后续体内重组的转化片段。
    
- **代谢物分析 (Metabolite Analysis)**：使用高效液相色谱 (HPLC) 和核磁共振波谱 (¹H NMR) 对工程菌株的发酵产物进行定量和定性分析。
    

## 四：实验设计及结果分析

### 研究部分一：平台设计与原理验证

#### 实验目的与设计

本部分的核心目的是阐述“afo regulon”平台的设计原理，并以一个相对简单的 BGC (citreoviridin) 为例，验证该策略的可行性。
![image.png](http://synbiopath.online/20251226230244041.png)


1. **平台设计**：`afo` 簇在诱导条件下表达量极高（产物 > 900 mg/L），且其调控因子 AfoA 能协同激活簇内所有基因。因此，将外源基因置于 `afo` 簇的调控元件之下，有望实现高产。
    
2. **Citreoviridin BGC 重建**：选择来自 _A. terreus_ 的 citreoviridin BGC（4个基因，`ctvA-D`）作为第一个测试案例。通过 Gibson assembly 和 PCR 制备 3 个大的 DNA 片段 (ctvF1-F3)，这 3 个片段包含了 4 个 `ctv` 基因的 CDS 和 `afo` 簇的基因间区域。
    
3. **转化与验证**：将这 3 个片段共转化到 _A. nidulans_ 宿主中，通过 4 次体内同源重组事件，将 `ctvA-D` 基因替换掉 `afo` 簇中的 4 个基因。
    

#### 实验结果与分析

- **Figure 2** 展示了 `afo` 簇的基因组成和功能，它是整个平台的“引擎”。
    ![image.png](http://synbiopath.online/20251226230253366.png)


- **Figure 3** 描绘了体内多片段同源重组的原理，展示了如何通过 3-5 次 HR 事件，将长达 17-35 kb 的外源 DNA 精确整合。
    ![image.png](http://synbiopath.online/20251226230302171.png)


- **Figure 4** 是 citreoviridin 重建的成功证据。
    
    ![](https://synbiopath.feishu.cn/space/api/box/stream/download/asynccode/?code=NmIzMzEwZGYzOTFlNjE5ZTk5MzNmMTQ1YWRlNDQ3ZTRfUXhENE5hNjVDWDk2TEQzRUxjdGhCeW54VUl6VnlRZVpfVG9rZW46Rkh5WWJaUlRzb3hpV294YkJtTmM4Zm41bndiXzE3NjUxODczMjU6MTc2NTE5MDkyNV9WNA)
    
    - **Figure 4b** 的示意图展示了如何通过 3 个转化片段 (ctvF1-F3) 重构 `ctv` 簇。
        
    - **Figure 4c** 的 HPLC 图谱显示，重构后的菌株 YM192 在诱导后产生了大量的 citreoviridin (**1**)，而对照菌株 YM87 则没有。
        
    - 产量分析显示，10 个随机挑选的转化子均能高产 citreoviridin，最高产量达到 **615.7 mg/L**。
        
- **结论**：这个实验成功地证明了“afo regulon”平台的可行性和高效性。
    

### 研究部分二：完整重建更复杂的 Pleuromutilin 生物合成途径

#### 实验目的与设计

本部分的目的是挑战一个更复杂的系统，即重建包含 7 个基因的 pleuromutilin 生物合成途径，以进一步展示平台的强大功能。

1. **分步重建策略**：由于基因数量多，作者采用两步法：
    
    1. **第一步：合成 Mutilin (2)**。将前 5 个基因 (`pl-ggs`, `cyc`, `p450-1`, `p450-2`, `sdr`) 通过两个转化片段 (pluF1, pluF2) 导入宿主，构建 mutilin 生产菌株 YM283。
        
    2. **第二步：合成 Pleuromutilin (3)**。在 YM283 的基础上，再导入后 2 个基因 (`pl-atf`, `p450-3`)，构建最终的 pleuromutilin 生产菌株 YM343。
        
2. **产物分析**：通过 LC-MS 和 ¹H NMR 对每一步的产物进行鉴定和定量。
    

#### 实验结果与分析

- **Figure 5b** 展示了第一步 mutilin 的合成。通过两个大片段 (pluF1, 9.2 kb; pluF2, 8.2 kb) 的共转化，成功构建了菌株 YM283。**Figure 5d** 的质谱和 **Figure S10** 的 NMR 谱证实，该菌株高效地生产了 mutilin (**2**)。
    

![](https://synbiopath.feishu.cn/space/api/box/stream/download/asynccode/?code=ZDUxMTk2NDgyOGJkYzMyZjA2YWM5OGVlODU4MTlmODRfMEpnU09IV3dDOTZtdFVETjhETkZiRHVmT1hzTzhCdlpfVG9rZW46QXFWYmJuRWt1b081RjF4V3FqVGN3aUJmblhlXzE3NjUxODczMjU6MTc2NTE5MDkyNV9WNA)

- **Figure 5c** 展示了第二步 pleuromutilin 的合成。在 YM283 基础上，通过转化一个 8.9 kb 的片段 (pluF3)，成功导入了最后两个基因，构建了菌株 YM343。
    

![](https://synbiopath.feishu.cn/space/api/box/stream/download/asynccode/?code=NGZkNDNhZGI0N2I1MzVlZTM1NjAzZDU5Nzk5ZjY0NmVfdWFBSHNoWG91dWNDVFJWMXl3T05hTHlXZ0RwaDVZZ2dfVG9rZW46SW0yemJvaU9Xb0VIY0l4MkF6cWNhbEpZbkNjXzE3NjUxODczMjU6MTc2NTE5MDkyNV9WNA)

- **Figure 5d** 的质谱图显示，YM343 成功地将 mutilin (**2**) 转化为了最终产物 pleuromutilin (**3**)。
    
- **Figure 6** 展示了转化片段 pluF3 与宿主基因组存在 4 个同源区域，这给筛选带来了复杂性，但作者通过筛选大量克隆，最终成功获得了正确的重组子。
    

![](https://synbiopath.feishu.cn/space/api/box/stream/download/asynccode/?code=M2RkMjU3ODJlMzhiNzlkODBhZmRiNjllNGU2ODVkOGZfMkxCNEhuN21nZFdFaWFDUk83OE5sNzFGc0FaODA5R2tfVG9rZW46R003UGJIM2tib0x6OW14QUVHTWNtdWpZbm9mXzE3NjUxODczMjU6MTc2NTE5MDkyNV9WNA)

- **产量分析**：最终的 pleuromutilin 产量约为 **150 mg/L**，显著高于之前在米曲霉中报道的产量 (~84 mg/L)，再次证明了该平台的优越性。
    

## 五：总体结论

1. **成功开发了高效异源表达平台**：本研究建立了一个基于 _A. nidulans_ `afo` 调控网络的新型、高效、标准化的异源表达平台。该平台能够通过“基因簇重构”的策略，实现对完整、复杂真菌 BGC 的高效协同表达。
    
2. **实现了高产**：利用该平台，成功地对两种高价值的真菌天然产物 citreoviridin 和 pleuromutilin 进行了全生物合成，产量分别高达 615.7 mg/L 和 150 mg/L，展示了其巨大的工业应用潜力。
    
3. **简化了技术流程**：该平台采用无克隆、基于体内同源重组的策略，大大简化了对大片段 DNA 的操作，为快速、系统地研究真菌沉默 BGCs 提供了强有力的工具。
    
4. **为合成生物学提供了新范式**：本文提出的“利用内源高效调控网络来驱动外源途径”的“重构”思想，为未来设计和构建微生物细胞工厂提供了全新的、极具启发性的设计范式。
    

## 六：论文评价

### 优点与创新

1. **方法学的重大创新**：“afo regulon”平台的设计思想非常巧妙和新颖。它不是简单地用一个通用启动子替换所有基因，而是“劫持”了整个天然的高效表达和调控系统，从而实现了所有基因的“天然协同”高表达，这是其成功的关键。
    
2. **技术上的巨大突破**：在丝状真菌中实现多达 7 个基因、总长超过 20 kb 的外源途径的完整、高产重建，在当时是一项重大的技术成就，极大地推动了真菌合成生物学领域的发展。
    
3. **结果令人印象深刻**：获得的 citreoviridin 和 pleuromutilin 产量非常高，直接展示了该平台的强大性能和实际应用价值，使得研究成果不仅仅停留在概念验证层面。
    
4. **研究的系统性与前瞻性**：论文不仅展示了两个成功的案例，还系统地讨论了该平台的优势、潜在应用（如阐明未知途径）和未来展望，具有很强的前瞻性和指导意义。
    

### 未来研究方向

1. **平台的通用性拓展**：将该平台应用于更多样化、更复杂的真菌 BGCs（如 PKS-NRPS 杂合体、生物碱等），以检验其通用性，并进一步优化以适应不同类型的生物合成途径。
    
2. **开发其他“调控网络”平台**：借鉴 `afo` 平台的成功经验，在 _A. nidulans_ 或其他模式真菌中，寻找并改造其他内源的高效 SM 调控网络（如 `mdp` 或 `apd` 簇），以构建一系列具有不同特性和适用范围的异源表达平台。
    
3. **组合生物合成**：利用该平台灵活、高效的基因组编辑能力，进行组合生物合成研究。例如，将不同来源的修饰酶导入到 pleuromutilin 生产菌株中，以创造出具有新颖结构和活性的“非天然”pleuromutilin 衍生物。
    

## 七：关键问题及回答

### 问题一：本文提出的“基因簇重构”(Cluster Refactoring) 策略，其核心思想是什么？

回答： 其核心思想是**“偷梁换柱”**，即**只替换基因的功能部分（编码区 CDS），而完整保留并利用一个天然高效基因簇的整个调控框架（启动子、终止子、基因间区域和调控因子）**。 具体来说，他们选择了一个在 _A. nidulans_ 中本身就能被诱导高表达的 `afo` 基因簇作为“机箱”。这个机箱自带一套完整的、能够协同工作的“电路系统”（即所有基因的启动子和调控因子 AfoA）。然后，他们将外源的目标基因（如 `ctvA`）的编码区，精确地替换掉 `afo` 簇中某个基因（如 `afoG`）的编码区。这样一来，`ctvA` 基因就被“伪装”成了 `afoG`，置于 `afoG` 原来的启动子之下。当研究人员激活总开关 AfoA 时，宿主的转录机器就会像识别内源 `afo` 基因一样，高效地转录这个被替换进来的外源基因。通过对簇内所有基因进行这样的替换，就实现了对外源 BGC 的整体“劫持”和协同高表达。

### 问题二：作者是如何在没有使用传统克隆载体的情况下，将一个包含 5 个基因、总长近 20 kb 的 pleuromutilin 上游途径导入宿主的？

回答： 作者采用了一种非常高效的、基于**体内同源重组 (in vivo homologous recombination)** 的无克隆策略 (Figure 5b)。

1. **化整为零**：他们没有试图一次性操作一个 20 kb 的巨大 DNA 片段，而是将其拆分为两个更易于操作的大片段：pluF1 (9.2 kb) 和 pluF2 (8.2 kb)。这两个片段是通过体外的 Gibson Assembly 和 PCR 制备的。
    
2. **设计“粘性末端”**：这两个片段被设计成在它们要连接的地方具有一段重叠的同源序列。同时，每个片段的两端也分别带有一段与宿主基因组目标整合位点（`afo` 基因座的上下游）同源的序列。
    
3. **共转化与体内组装**：他们将 pluF1 和 pluF2 这两个线性的 DNA 片段**同时**转化到 _A. nidulans_ 的原生质体中。进入细胞后，宿主自身强大的同源重组修复系统会识别出这些“粘性末端”，并自动地完成三件事：
    
    1. pluF1 的上游端与基因组的上游同源臂重组。
        
    2. pluF2 的下游端与基因组的下游同源臂重组。
        
    3. pluF1 的下游端与 pluF2 的上游端（即它们之间的重叠区）发生重组。 通过这一系列的体内重组事件，两个独立的 DNA 片段被无缝地拼接在一起，并作为一个整体精确地整合到了基因组的预定位置，从而完成了整个复杂途径的导入。
        

### 问题三：这项研究的成功对于未来从真菌中发现和开发新药有何重要意义？

回答： 这项研究的成功具有里程碑式的意义，它为真菌天然产物的发现和开发提供了一个**通用、高效的“加速器”**。

1. **解锁“沉默”的化学宝库**：真菌基因组中 90% 以上的 BGCs 是沉默的，传统方法无法触及。本文的平台提供了一种通用的方法，可以将任何来源的、任何沉默的 BGC“唤醒”，从而系统性地探索这个巨大的未知化学空间，大大增加了发现新颖药物先导化合物的机会。
    
2. **解决“产量瓶颈”**：许多有潜力的天然产物因为在天然宿主中产量过低而无法进行后续的药物开发。本文的平台通过将 BGC 置于一个超强表达系统的控制下，能够将产量提升数倍甚至数十倍（如 pleuromutilin 产量翻倍），直接解决了药物开发的原料供应瓶颈。
    
3. **加速“组合生物合成”**：该平台灵活的基因编辑能力，使得研究人员可以方便地对 BGC 进行“修修改改”，例如敲除某个基因以积累中间体，或引入新的修饰酶来创造“非天然”的衍生物。这极大地加速了药物的结构优化和构效关系研究。 总而言之，该平台将真菌天然产物的研究从一种依赖于菌种筛选和发酵条件优化的、缓慢且充满不确定性的过程，转变为一种可预测、可编程、高效率的工程化过程。