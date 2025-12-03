
**DeepTMHMM：一种高效精准的蛋白质跨膜结构预测工具（网页版使用和本地教程）【YBioinformatics】**

```<p>*🔗 原文链接： [https://mp.weixin.qq.com/s/1jQLnO8E...*](https://mp.weixin.qq.com/s/1jQLnO8EHBFLMdY0bVt8UA)*</p><p>原创 小袁爱打球 YBioinformatics*2025年07月31日 11:58  江苏 标题已修改*</p>```
跨膜蛋白在细胞膜中起着至关重要的作用，涉及物质转运、信号传导和能量转换等多种生命过程。由于其结构复杂且难以通过实验手段解析，跨膜蛋白的结构预测成为结构生物学和生物信息学的重要研究方向。传统的跨膜结构预测方法往往依赖于序列同源性、隐马尔可夫模型（HMM）或机器学习方法，存在预测准确率有限、跨物种泛化能力不足等问题。

为了解决上述挑战，DeepTMHMM 应运而生。DeepTMHMM 是一款基于深度学习蛋白质语言模型的跨膜结构预测工具，能够同时识别 α-螺旋和 β-桶状结构的跨膜蛋白。它采用无需同源序列比对的策略，仅凭蛋白质一级序列即可高效预测蛋白的跨膜拓扑结构，包括信号肽、跨膜区段、胞内与胞外片段的位置等。该方法在多个数据集上均显示出优异的性能，并广泛适用于各类真核和原核生物蛋白的结构注释与功能分析。

本文主要介绍DeepTMHMM的网页版使用方法以及本地安装教程：

（1）登录 DeepTMHMM的官网，网址如下：

**https://services.healthtech.dtu.dk/services/DeepTMHMM-1.0/**

（2）将需要预测的蛋白氨基酸序列输入到文本框中， **需要fasta格式** ，这里以 Bacteriorhodopsin（细菌视紫红质）蛋白为例（pdb id：1C3W），该蛋白是 典型的七跨膜 α-螺旋蛋白，点击Submit按钮进行提交。

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\DeepTMHMM：一种高效精准的蛋白质跨膜结构预测工具（网页版使用和本地教程）【YBioinformatics】.001.png)

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\DeepTMHMM：一种高效精准的蛋白质跨膜结构预测工具（网页版使用和本地教程）【YBioinformatics】.002.png)

（3）预测结果分析

预测结果图由两个部分组成，上图显示的是最可能的拓扑结构（Most Likely Topology），将每个氨基酸根据预测结果归类为位于膜外（Outside）、膜内（Inside）或膜中（Membrane）。可以看到图中有7个红色块，代表预测出了7个的跨膜区段。

下图为后验概率图（Posterior Probabilities），表示每个氨基酸属于三种区域之一的概率分布。图中红色线（Membrane）在跨膜区域段内高度接近1，粉色（Inside）和蓝色（Outside）则在其他区域占主导，表明模型对不同区域的划分具有高度置信度，边界切换清晰。整体预测结果表明，该蛋白的跨膜区段分布稳定、拓扑结构明确，模型输出具有较高的可靠性和生物学意义。

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\DeepTMHMM：一种高效精准的蛋白质跨膜结构预测工具（网页版使用和本地教程）【YBioinformatics】.003.png)

另外结果中还有每个每个跨膜区域的详细氨基酸划分，其中O：Outside表示膜外，I：Inside表示膜内，M：Membrane表示膜中/跨膜区。

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\DeepTMHMM：一种高效精准的蛋白质跨膜结构预测工具（网页版使用和本地教程）【YBioinformatics】.004.png)

（4）本地版本安装和使用：

本地版的使用也非常简单，只需要准备好蛋白的氨基酸序列即可，主要的预测结果文件是 deeptmhmm\_results.md

```Plaintext
pip3 install pybiolib
biolib run DTU/DeepTMHMM --fasta input.fasta```
![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\DeepTMHMM：一种高效精准的蛋白质跨膜结构预测工具（网页版使用和本地教程）【YBioinformatics】.005.png)


在使用安装该软件的过程中遇到任何问题都可以扫描下方二维码联系作者~

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\DeepTMHMM：一种高效精准的蛋白质跨膜结构预测工具（网页版使用和本地教程）【YBioinformatics】.006.jpeg)










