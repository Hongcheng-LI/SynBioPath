
**FoldSeek：海量数据背景下的快速蛋白比对神器**

```<p>*🔗 原文链接： [https://mp.weixin.qq.com/s/SerXSg2N...*](https://mp.weixin.qq.com/s/SerXSg2NS3XqnZ3LwFtphQ)*</p><p>原创 生物帮SA 生物帮SA*2024年12月19日 10:01  北京*</p>```

*此文章由“第一届生物分享杯”参赛者投稿。为保证公平暂不公布参赛者信息。* 

随着 Alphafold3 、 Boltz-1 等模型的问世，越来越多的蛋白质结构被预测并公开， 如何从庞大的数据库中高效地找到相关结构 成为了一个挑战。 Foldseek 通过将蛋白质的三级结构转化为结构字母表的序列，用字母表示的 “ 语言 ” 来描述蛋白质的结构信息，从而简化了结构的表示，使得结构比对计算更加高效。 接下来，将为大家介绍 **FoldSeek 的功能类别、在线使用方法以及优势** 。

[🎦 点击观看视频](https://mpvideo.qpic.cn/0b2e5yadiaaahaaorklcejtvb3wdgtxaanaa.f10002.mp4?dis_k=c115e93e2dc9f219cace2db36794f275&dis_t=1758937982&play_scene=10120&auth_info=Z67s58F4RgthqKX7/l5wampLU3U9RFgTJ3UvXDxRE2lBf29tVHcbZANrOD5Of2dQYA==&auth_key=cb5b82f92ecea68eb2c96e57f6efa862&vid=wxv_3773867628800999430&format_id=10002&support_redirect=0&mmversion=false)

**🌟 FoldSeek 的功能类别** 

\1. 未知蛋白的功能推测 

对一个未知蛋白进行序列比对后，未能找到与其相似的蛋白，此时可以尝试通过其 **三维结构找到相似蛋白** 。如前期文章中我们介绍的通过DALI进行三维结构比对【 [如何寻找蛋白的同源蛋白：从一级序列比对到三维结构比对 ](https://mp.weixin.qq.com/s?__biz=MzkyODY1MTk0Ng==&mid=2247484523&idx=1&sn=d278a8de26e6c44d2ffd4128dc758ded&scene=21#wechat_redirect)】。

\2. De novo 设计蛋白的验证 

进行从头（ de novo ）蛋白设计，需要证明设计的蛋白在结构上与数据库中任何已知蛋白都不相似，以此确保设计的创新性。 

\3. 特定功能蛋白的设计验证 

从零开始设计一个具有特定功能的蛋白，可以利用 FoldSeek 确认其结构是否与已知具有该功能的蛋白相似，从而验证设计的合理性。 

**🌟  单个蛋白的比对搜索** 

\1. 导入搜索蛋白： 打开网址 https://search.foldseek.com/search ，左侧工具栏显示 Search 、 Multimer search 和 FoldMason MSA ，分别适用于： 

① Search ：单个蛋白质； 

② Multimer search ：蛋白复合物或多聚体； 

③ FoldMason MSA （ Multiple Sequence Alignment ）：构建基于结构的多序列比对，用于保守区域识别或功能预测。通过三维结构信息来优化多序列比对。

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\FoldSeek：海量数据背景下的快速蛋白比对神器.001.png)

点击 Search 模块，点击 UPLOAD PDB ，选择本地蛋白 PDB 数据文件（也可以点击 LOAD ACCESSION ，输入蛋白的 PDB ID ）。前期文章也已介绍获得结构未解析蛋白的PDB文件的方法【 [如何寻找蛋白的同源蛋白：从一级序列比对到三维结构比对 ](https://mp.weixin.qq.com/s?__biz=MzkyODY1MTk0Ng==&mid=2247484523&idx=1&sn=d278a8de26e6c44d2ffd4128dc758ded&scene=21#wechat_redirect)】。

这里以 8HFE （人源去甲肾上腺素转运蛋白）为例。加载完成后， 8HFE 的文件信息将显示在框内： 



![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\FoldSeek：海量数据背景下的快速蛋白比对神器.002.png)

\2. 选择蛋白搜索数据库： 点击 Databases & search settings 前面的“ + ” ，选择进行搜索的数据库类型。默认勾选所有数据库选项。 

① Mode ：选择 3Di/AA 模式，能极大提高搜索效率。 

② Taxonomic filter ：筛选搜索结果中的特定分类（如物种、属、科），仅保留感兴趣的生物群体。 



![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\FoldSeek：海量数据背景下的快速蛋白比对神器.003.png)

\3. 运行比对程序： 点击“SEARCH”，耗时 1-2 分钟。结果页面如下： 



![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\FoldSeek：海量数据背景下的快速蛋白比对神器.004.png)

\4. 分析比对结果： 分析如下 

**①**  **评价指标：** 

Prob.(  Probability) ： 比对的 匹配概率 ，表示该比对结果是正确的概率。值越接近 1 ，表示比对结果越可靠。 

Seq. Id.(Sequence Identity) ： 比对的 序列相似性 ，表示两个序列在一级结构（氨基酸）上的相似程度。例如 80% 以上表示查询序列与目标序列高度相似。 

E-Value ： 比对结果的 期望值 ，值越小，表示比对结果越显著，可信度越高。 

**②**  **挑选最优比对结果：** 在 AFDB-PROTEOME 数据库中定位最优比对结果： P23975 （ Uniprot ID ），人源钠离子依赖的去甲肾上腺素转运体，匹配概率 1 ，序列相似度 98.2% ， E-value < 0.0001 。 



![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\FoldSeek：海量数据背景下的快速蛋白比对神器.005.png)

**③**  **结果可视化：** 点击上图中 Alignment 下方的“三” ，可以查看具体的比对信息。得到下图： 

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\FoldSeek：海量数据背景下的快速蛋白比对神器.006.png)

鼠标选中未匹配的序列后，右侧结构图中对应序列将被标记为青色。 



![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\FoldSeek：海量数据背景下的快速蛋白比对神器.007.png)

**④**  **保存结果：** 点击结构图下方的 PDB 或者 PNG 按钮，保存为 PDB 数据文件或者图片文件。 

**🌟  复合物或多聚体的比对搜索** 

1.选择模式： 点击 Multimer search ，这里以 8WA2 （莱茵衣藻纤绒毛结构）为例。 



![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\FoldSeek：海量数据背景下的快速蛋白比对神器.008.png)

2.比对： 点击“ + ”，默认勾选 BFMD 和 PDB100 数据库，选择 3Di/AA 搜索模式，点击 SEARCH 运行比对程序。 



![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\FoldSeek：海量数据背景下的快速蛋白比对神器.009.png)

\3. 定位最优比对结果： 选择 PDB100 数据库中的第一条比对结果： Chain pairing 将 Query 的每条链比对到 Target 的相应链，例如 Query 的 A 链对应 Target （ PDB ID ： 8TXB ）的 C 链。 



![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\FoldSeek：海量数据背景下的快速蛋白比对神器.010.png)

4.查询比对信息： 点击第3步图中的 Alignment 下方的“三”，查看具体比对信息。具体如下： 



![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\FoldSeek：海量数据背景下的快速蛋白比对神器.011.png)

5.数据可视化： 在 Chimera 中打开保存的比对结果。



![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\FoldSeek：海量数据背景下的快速蛋白比对神器.012.png)

**🌟 FoldSeek 的性能优势** 

与传统的蛋白质结构比对方法（如 Dali 、 TM-align 和 CE ）相比， Foldseek 大幅提高了计算效率，缩短了计算时间（达到四到五个数量级） 。同时， Foldseek 的比对灵敏度（即准确性）保持不变，分别为 Dali 的 86% 、 TM-align 的 88% 和 CE 的 133% 。 

**🌟  关于生物帮 SA** 

生物帮 SA 由清华大学博士团队创立，致力于打造学术一体化生态圈，全方位助力科研与职业发展： 

**[1] 解决生物问题：** 百余位来自清华、北大、 Stanford University 、 University of Nebraska Lincoln 、 Imperial College London 、复旦、浙大、中科院等国内外顶尖高校的老师、工程师、博后、硕博生加入团队，提供考 / 保研咨询、科研问题解决、文献阅读等生物相关问题解决方案，重点打造论文写作、实验合作等专项服务； 

**[2] 分享科研干货：** 涵盖生物知识、科研作图、经验交流，助力科研之路。 

**[3] 传播实用信息：** 分享就业资讯、试剂仪器信息和培训资源。

**参考资料：** 

[1] Van Kempen M, Kim S S, Tumescheit C, et al. Fast and accurate protein structure search with Foldseek[J]. Nature biotechnology, 2024, 42(2): 243-246.

[2] Baca C F, Majumder P, Hickling J H, et al. The CRISPR-associated adenosine deaminase Cad1 converts ATP to ITP to provide antiviral immunity[J]. Cell, 2024.

[3] Huang J, Tao H, Chen J, et al. Structure-guided discovery of protein and glycan components in native mastigonemes[J]. Cell, 2024, 187(7): 1733-1744. e12.




