
**AlphaFold3：在线版使用指南 【知乎】**

```🔗 原文链接： [https://zhuanlan.zhihu.com/p/289411...](https://zhuanlan.zhihu.com/p/2894118911)```

** AlphaFold3作为革命性的人工智能模型，不仅可以预测 [蛋白质三维结构 ](https://zhida.zhihu.com/search?content_id=249601543&content_type=Article&match_order=1&q=%E8%9B%8B%E7%99%BD%E8%B4%A8%E4%B8%89%E7%BB%B4%E7%BB%93%E6%9E%84&zhida_source=entity)，还能够预测所有生命分子的结构和相互作用，包括蛋白质、DNA、RNA、配体小分子、离子等生物分子相互作用。今天Kiki学姐将手把手教你如何使用AlphaFold3在线版预测分子结构。

本文分为两个篇章

- 第一章 AlphaFold3分子结构预测使用简介
- 第二章 AlphaFold3分子结构预测实操演示



**第一章 AlphaFold3分子结构预测使用简介**

\1. **使用条件**

**科学上网+Google账号（Kiki学姐小提示：如果您还没有谷歌账号，需要先创建一个哦）**

\2. **访问 AlphaFold Server**

**方法** ：打开谷歌浏览器 → 登陆谷歌账户 → 进入AlphaFold3（网址： [https:// alphafoldserver.com/  ](https://link.zhihu.com/?target=https%3A//alphafoldserver.com/)） → 即可出现下图（图1）

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\AlphaFold3：在线版使用指南%20【知乎】.001.jpeg)

\3. **上传序列数据**

在AlphaFold Server序列输入区：点击“Add entity”（图2） **→** 即出现序列输入框（图3） **→** 根据分子类型选择蛋白质/DNA/RNA/配体/离子（图4） **→** 选择序列出现次数（图4） **→输入序列** （图4）。 **→** 点击“Continue and preview job”进行下一步操作（图5）。

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\AlphaFold3：在线版使用指南%20【知乎】.002.jpeg)

图2 AlphaFold Server序列输入区A

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\AlphaFold3：在线版使用指南%20【知乎】.003.jpeg)

图3 AlphaFold Server序列输入区B

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\AlphaFold3：在线版使用指南%20【知乎】.004.jpeg)

图4 AlphaFold Server序列输入区C

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\AlphaFold3：在线版使用指南%20【知乎】.005.jpeg)

图5 AlphaFold Server序列输入区D

\4. **预测和下载结果** （具体操作流程在下方实操演示中查看）

\5. **结果可视化**

使用PyMOL等分子可视化软件打开下载的.cif文件，以查看和编辑蛋白质的三维结构。（具体操作流程在下方实操演示中查看）



**第二章 AlphaFold3分子结构预测实操演示（以预测Human IL-10结构为例）**

\1. **确定Human IL-10氨基酸结构及序列**

- **确定Human IL-10氨基酸结构**

登陆uniprot（ [https://www. uniprot.org/  ](https://link.zhihu.com/?target=https%3A//www.uniprot.org/)，图6）→ 输入蛋白种属及名称（Human IL-10，图6） → 点击“search” （图6），进入对应网页（图7）→ 仔细核对，选择正确蛋白（图7） → 点击对应“Entry”（P22301），进入详情页（图8） → 在详情页中，点击“Struture” （图8）→ 推测Human IL-10为二聚体（图8） → 本次选择1INR，点击RCSB-PDB（图8），进入对应网页（图9） → 确认1INR晶体结构为二聚体 **（Kiki学姐小提示：做个笔记记录下来，后面会用到哦）**

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\AlphaFold3：在线版使用指南%20【知乎】.006.jpeg)

图6 uniprot首页

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\AlphaFold3：在线版使用指南%20【知乎】.007.jpeg)

图7 uniprot Human IL-10列表页

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\AlphaFold3：在线版使用指南%20【知乎】.008.jpeg)

图8 uniprot Human IL-10详情页A

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\AlphaFold3：在线版使用指南%20【知乎】.009.jpeg)

图9 PDB 1INR详情页

- **确定Human IL-10氨基酸序列：**

点击“Sequence”（图10） → 点击“Copy sequence”（图10），复制Human IL-10氨基酸序列。

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\AlphaFold3：在线版使用指南%20【知乎】.010.jpeg)

图10 uniprot Human IL-10详情页B

\2.  **AlphaFold Server在线预测**

- **登陆AlphaFold Serve并上传序列数据**

登陆AlphaFold3（网址： [https:// alphafoldserver.com/  ](https://link.zhihu.com/?target=https%3A//alphafoldserver.com/)，图11）→ 在序列输入区：“Molecule type”选择protein（图11） → “Copies”选择2（KiKi学姐在上文中提醒过哦，Human IL10为二聚体，所以Copies选择2，图11）→ 输入序列（图11）→ 点击“Continue and preview job”（图11）。

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\AlphaFold3：在线版使用指南%20【知乎】.011.jpeg)

图11 AlphaFold Server序列输入区E

- **预测和下载结果**

修改Job name（Human IL-10，图12） → 点击“Confirm and submit job” （图12）→ 在AlphaFold Server历史记录中找到“Human IL-10”，点击“Human IL-10”（图13），进入网页（图14） → 进行预测结果分析（分析结果如下） → 点击“Download” （图14），下载预测的蛋白质结构文件（图16）。

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\AlphaFold3：在线版使用指南%20【知乎】.012.jpeg)

图12 AlphaFold Server提交

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\AlphaFold3：在线版使用指南%20【知乎】.013.jpeg)

图13 AlphaFold Server历史记录区

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\AlphaFold3：在线版使用指南%20【知乎】.014.jpeg)

图14 AlphaFold Server Human IL-10预测结果详情页

***AlphaFold Server预测结果分析***

- 在图14中，蛋白整体偏深蓝，说明结构整体置信度良好。
- pTM>0.5，说明复合物的整体预测与真实结构相似。
- 0.8>ipTM>0.6：预测结果正确与否不能确定。

- **结果可视化**

打开PyMOL（图15）→打开alphafold下载结果（图16），有.cif和.json格式文件。默认选择“\_model\_0.cif”进行分析→将“fold\_human\_il\_10\_model\_0.cif”文件拖入PyMOL→可看到蛋白质分子结构（图17）

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\AlphaFold3：在线版使用指南%20【知乎】.015.jpeg)

图15 PyMOL

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\AlphaFold3：在线版使用指南%20【知乎】.016.jpeg)

图16 AlphaFold Server Human IL-10预测结果文档

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\AlphaFold3：在线版使用指南%20【知乎】.017.jpeg)

图17 PyMOL Human IL-10预测结果可视化

下期，Kiki学姐将教大家使用AlphaFold3预测分子间相互作用，以及使用Pymol查看分子结构及分子互作，敬请期待吧！

关于本章节内容，大家如果有不清楚的可在下方留言，小编将结合大家需求，更新笔记。

（原创不易，转载或引用时请注明来源）

编辑于 2025-02-21 12:17 ・湖北


