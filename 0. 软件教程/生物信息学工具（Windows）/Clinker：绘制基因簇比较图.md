
**Clinker：绘制基因簇比较图**

\1. **工具简介**

通过对同源基因簇进行比对和分析，可以对这些基因的功能和进化史有进一步的认知。

使用 clinker 可以直接生成同源基因簇比对图，生成的图片可以直接用于文章发表。

[CAGECAT: the online CompArative Gene Cluster Analysis Toolbox](https://cagecat.bioinformatics.nl/)

\2. **前期准备**

```<p>clinker 可识别的文件为 GeneBank 文件（后缀为 .gbk），该类型文件可由以下几种途径获得：</p><p>- 由 antiSMASH、cblaster 等序列搜索分析工具直接生成</p><p>- 由 Snapgene、Geneious 等软件从基因组中提取出来的序列文件</p><p>- 从 NCBI，MiBiG 等网站直接下载。</p>```

2.1 **antiSMASH 直接下载**

1. 将自己测序获得或从 NCBI 等数据库中下载得到的基因组提交到 antiSMASH 中，得到分析结果如下：

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\Clinker：绘制基因簇比较图.001.png)

2. 以“Region 1.1”为例，点击目标基因簇，进入详细界面后，点击“Download region GeneBank file”，即可下载目标基因簇的 GeneBank 文件。

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\Clinker：绘制基因簇比较图.002.png)

2.2 **从 MiBiG 网站下载**

1. 打开网址

[MIBiG：Minimum Information about a Biosynthetic Gene cluster](https://mibig.secondarymetabolites.org/)

2. 点击 search

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\Clinker：绘制基因簇比较图.003.png)

3. 点击“Build a query”，选择“compound name”，输入化合物的名字，点击搜索。例如输入：neosartorin

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\Clinker：绘制基因簇比较图.004.png)

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\Clinker：绘制基因簇比较图.005.png)

4. 点击“Download Cluster GeneBank file”，即可获得该基因簇 GeneBank 格式的文件。

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\Clinker：绘制基因簇比较图.006.png)

\3. **生成基因簇比较图**

1. 打开网址：[CAGECAT: the online CompArative Gene Cluster Analysis Toolbox](https://cagecat.bioinformatics.nl/)，点击 clinker 中的 start 按钮。

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\Clinker：绘制基因簇比较图.007.png)

2. 下面是软件运行界面的功能说明

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\Clinker：绘制基因簇比较图.008.png)

（1）Server status：服务器状态

- Running：3；说明当前正在运行 3 个项目
- Queued：0；说明当前没有正在排队的项目
- Completed：20558；说明当前已完成 20558 个项目

（2）Previous jobs：自己之前已经分析完成的项目，点击对应的 ID 即可查看之前的分析结果

（3）Job description：项目描述

- Job title：给本次的分析项目起一个名称，便于后期快速识别本项目。
- Email address for notification：输入邮箱地址，分析完成后会将结果发送到邮箱内。

（4）Input：输入分析文件

- Genome files：点击该按钮即可上传自己需要分析的文件，文件必需是 GenBank 格式的文件（gbk，gb，genbank，gbf，gbff），最多允许上传的基因簇数量为 50 个，且不可上传全基因组文件。

（5）Alignment：设置比对参数

- Don't align clusters：在输出的结果中，不显示基因簇之间的同源性，仅显示基因簇的组成。请勿勾选。
- Min. alignment sequence identity：0.3；在输出的结果中，只有同源性超过 30% 的基因之间才会显示同源性相关，该数值在输出结果中还可以修改。

（6）Output：设置输出文件

- Delimiter：分界符；在生成基因簇比较图结果时，会使用特定的分界符将结果分开。默认不使用分界符。
- Decimals：小数位数；在输出的结果中，显示的同源性分数的小数位数，默认保留 2 位小数。
- Hide alignment column headers：隐藏基因簇比对图中的柱头，默认不勾选。
- Hide alignment cluster name headers：隐藏基因簇比对图中的基因簇的名字，默认不勾选。

（7）AddiTional oppotions：其他选项

- Maintain order of input files：按照输入文件的顺序输出基因簇比对结果，默认不勾选。

（8）Explanations：解释

- 在 ③~⑦ 相中，不同选项的后面均有一个 "？",点击“？”，即可在此处显示对该选项的解释。

3. 以软件自带的案例文件为例，进行分析

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\Clinker：绘制基因簇比较图.009.png)

4. 得到结果如下

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\Clinker：绘制基因簇比较图.010.png)

5. 点击“Download results”，即可下载本次分析结果。

注意：

- 拖动簇可以重新对图中簇的顺序重新排列
- 将鼠标放在基因簇上，会显示小手的形状。摁住鼠标左键左右拖动，可以移动基因簇的位置
- 单击某一个基因，就可以以该基因为锚点，对其基因簇
- 双击鼠标左键，就可以调整该基因簇的方向
- 点击基因簇的名字和图例就可以对其进行重命名
- 点击图例处的圆圈可以改变基因的颜色
- 鼠标右键单击图例可以隐藏该基因
- 单击图片上的比例尺可以调整基因的长度

6. 调整好图片之后，点击图片中的“Save SVG”

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\Clinker：绘制基因簇比较图.011.png)

7. 将下载好的“SVG 图片”文件复制到 PPT 中，如下图所示

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\Clinker：绘制基因簇比较图.012.png)

8. 鼠标右键点击图片，选择“组合”中的“取消组合”，直到图片中不再有任何组合。

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\Clinker：绘制基因簇比较图.013.png)

9. 经过调整，即可得到自己需要的图片

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\Clinker：绘制基因簇比较图.014.png)

