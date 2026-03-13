
# 一：视频教程

[Sequence Similarity Network (SSN) 和进化树 Phylogenetic Tree](https://www.bilibili.com/video/BV1A94y1Y75j/?spm_id_from=333.337.search-card.all.click)

# 二：案例素材

## （一）序列文件

GenBank: UFA62170.1

>UFA62170.1氨基酸序列
>MRETIPIKYIDTIEINKLSIQDLEDLSSCKYKLLSAYLIGKIPANKILDADELEIYHNERTKKILAKAIKARKLVIVLKATRLCNLRCTYCHSWAEGPNQTILFSTLIHIVRQILAIPNVNRFEFVWHGGEVTLLKPAFFKKLIWLQEQFKRPEQYITNTMQSNIVNISDEWLIFIKGIGMNVGISLDGIPAVNDKRRVDFRGRGTSDRIAKGIKKLQKYDILYGALIVVDREVYQTDMREMLDYFILIELNGIEFLNIVPDNRLTAGEDIGNNFISYAEFIKFLSALFVIWIKGYREKIHIAIFEDFISVLENPEKKLSACYWSGNCSQEIITLEPNGDVSPCDKYRGDAGSIYGSLLKTDLAGLLTQSSHNQQAIDEEVAATRKMQHCEWFSICHGGCPHDRVINRRHTKGYNDECCGTGKLLATIKAYLADIR

https://www.ncbi.nlm.nih.gov/protein/UFA62170.1/?report=fasta

## （二）所用工具

EFI-EST：https://efi.igb.illinois.edu/efi-est/



# 三：实操教程

## （一）准备序列数据

首先，我们要明确自己的数据是什么情况：
- **情况 A：只有 1 条蛋白质序列**。那需要用这条序列去数据库里“钓”出它的同源序列，然后再做网络图。
- **情况 B：你已经有了一个包含很多条序列的文件（FASTA格式）**。比如几十上百条序列，你想看看它们之间的聚类关系。可以直接上传到 EFI-EST 网站，进行分析。

如果是情况 A，也有两种处理方法：
- **方法一**：直接在 EFI-EST 网站中选择 **Option A (BLAST)**。把你的那条序列粘贴进去，设置最多提取多少条同源序列（比如默认的1000条或5000条），，在 UniProt 数据库中进行检索，即可获得用于构建序列分子网络所需要的序列数据。
- **方法二**：在 NCBI 中对这条序列进行 Blastp 搜索，下载对应的 Fasta 序列合集，也可获得用于构建序列分子网络所需要的序列数据。

如果单说”全面性”（序列的数量和广度），NCBI 绝对比 UniProt 更全面；但是，如果是为了“做 SSN 分析”，使用 EFI-EST 自带的 UniProt 检索通常是更好、更实用的选择。

### 1. 在 EFI-EST 中获得序列数据

打开下列网址，进入 EFI-EST 网站
https://efi.igb.illinois.edu/efi-est/
![image.png](https://synbiopath.online/20260310215643621.png)

在 Query Sequence 处输入目标序列，在 UniProt BLAST query e-value 处输入默认值 5；Maximum number of sequences retrieved 处输入默认值 1000，序列太多会导致后面 Cytoscape 画图时电脑卡顿，第一次操作建议选择默认值即可。Sequence database 有三种选项，Uniprot，Uniprot90，Uniprot50。

这三个数据库的区别是
- 「Uniprot」通常指**UniProtKB 全库 / UniRef100**，是完整的原始蛋白数据库；
- 「Uniprot90/Uniprot50」官方标准名称为**UniRef90/UniRef50**，是 UniProt 官方基于全库做的**序列相似性去冗余聚类子集**，不是独立的新数据库，所有序列和注释均来源于 UniProtKB。

一开始我们可以先用 **Uniprot** 数据库，如果后面发现序列实在太多，可以选择使用 **UniRef90** 数据库。这相当于 UniProt 帮你做了一个“去重”：把相似度 >90% 的序列合并成一个代表点。这样既保证了物种多样性（全面），又大大减少了数据冗余，画出来的图也更漂亮！
![image.png](https://synbiopath.online/20260311161659896.png)

在最下面输入任务名和邮箱，点击 submit analysis。

此时，会提示任务完成后邮箱中会收到一封邮件。
![image.png](https://synbiopath.online/20260311162812520.png)

等任务完成之后，就可以获得用于构建序列相似性网络的序列数据了。


### 2. 在 NCBI 中获得序列数据

在此处，我们也给出在 NCBI 中通过 Blast 检索获得用于构建序列分子网络所需要的序列数据的过程

首先，对目标序列进行 Blast 分析
![image.png](https://synbiopath.online/20260228223701885.png)

点击图中的 Download，在之前的操作中，直接选择下载 Fasta格式的序列时，上传到 EFI-EST 网站中去，会导致报错，因此我们选择下载 CSV 格式的文件
![image.png](https://synbiopath.online/20260310211227917.png)

打开刚刚下载的 CSV 文件，复制文件中的 Accession Number 号，粘贴到文本文件中。
随后，进入下面的网站，选择 Protein，上传刚刚处理好的  txt 文件，点击 Retrieve，
https://www.ncbi.nlm.nih.gov/sites/batchentrez
![image.png](https://synbiopath.online/20260310212305701.png)

在新的窗口中，点击 Retrieve records for 25 UID(s)，进入新的界面
![image.png](https://synbiopath.online/20260310212250408.png)

在这个界面中，点击 Send to，选择为 File，格式为 fasta，点击 create file，即可获得用于构建序列分子网络所需要的序列数据。
![image.png](https://synbiopath.online/20260310213301498.png)


## （二）使用 EFI-EST 网站生成网络文件（XGMML）

### 1. 对从 EFI-EST 中获得的序列数据进行分析

我们在 EFI-EST 中通过 **Option A (BLAST)** 进行 blast 之后，会收到一封任务完成的邮件，点击邮件中的连接，会可以看到在 Dataset Summary 处列出了这个数据集的各种信息，此时我们点击 SSN Finalization，进行 SSN 网络优化
![image.png](https://synbiopath.online/20260311172543724.png)

点击 Dataset Analysis（数据集分析）标签页，该标签页会生成序列特征的直方图、箱线图，以及 BLAST 全序列两两比对的统计结果，为后续 **SSN Finalization** 环节的参数（比对得分阈值、序列长度过滤）设置提供数据依据。
![image.png](https://synbiopath.online/20260311172902363.png)

在 Sequences as a Function of Full Length Histogram (序列长度分布直方图)中，图中有一个极其突兀且尖锐的紫色高峰，对应的横坐标（长度）大约在 **390 - 410** 个氨基酸左右。而在此之外，几乎没有其他高度的柱子。说明这个蛋白家族在长度上**非常保守**。它大概率是一个单结构域的蛋白质。那些极少数特别短的（比如长度小于300的）可能是测序不完整的“碎片（Fragments）”，特别长的可能是融合蛋白。我们可以在下一步设置长度过滤，把那些碎片剔除掉，保证进入网络图的都是完整的序列。
![image.png](https://synbiopath.online/20260311173630984.png)

Alignment Length vs Alignment Score Box Plot (比对长度与AS得分的箱线图) 是最重要的一张图，可以看到曲线一开始急速上升，然后在横坐标（AS）达到 **25~35** 左右时，曲线突然**变平了（Plateau）**，变成了一条水平的直线，对应的纵坐标（比对长度）正好是大约 350-400。这进一步印证了它是单结构域蛋白。当 AS 得分极低时，BLAST 只能比对上蛋白质的一小段（比如几十个氨基酸）；**当 AS 超过大约 35 之后，BLAST 的比对长度就达到了整个蛋白质的全长（~400 aa）**。说明 **AS 阈值绝对不能低于 35 这个“拐点”！** 如果 AS 选太低，网络图中会出现大量仅靠“局部小片段相似”就连在一起的错误连线。因此，你的 AS 阈值**至少要大于 35**。
![image.png](https://synbiopath.online/20260311174233583.png)

Percent Identity vs Alignment Score Box Plot (序列一致性百分比与AS得分箱线图) 是一条近似直线的上升曲线。EFI 官方强烈建议，初始的 SSN 网络应该选择 **序列一致性（Percent Identity）在 35% 到 40% 左右** 对应的 AS 值。我们在图的纵坐标找到 35%-40%，横向看过去，对应的横坐标 AS 值大约在 **35 到 45** 之间。结合图2和图3，我们可以断定，初始 AS 阈值设置在 **40 左右** 是非常科学的。
![image.png](https://synbiopath.online/20260311174258341.png)

Edge Count vs Alignment Score Plot (连线数量与AS得分图) 这张图是用来评估你的电脑会不会“卡死”的。EFI 提示中写了：16GB 内存的电脑可以轻松打开 200万（2M）条边的网络。我们可以看到这张图是一条逐渐下降的曲线。如果你选 AS = 40，对应的纵坐标（连线数）大约是 **400k（40万条边）**。40 万条边远远低于电脑的极限，所以你可以放心大胆地生成包含所有序列的**全网络图（Full SSN）**，不需要生成压缩版的代表节点网络（Rep Node SSN）。
![image.png](https://synbiopath.online/20260311174528028.png)

Edges as a Function of Alignment Score Histogram (连线数量分布直方图) 这张图中有好几个明显的“山峰”（大约在 AS=37, 62, 110, 245 附近都有峰值）。这说明下载的这批序列**功能多样性非常丰富**，它们内部明显分化出了好几个不同的同源亚家族（Isofunctional clusters）。如果是单一功能的蛋白，图中只会有一个靠右边的大峰。这预示着你最终画出来的 Cytoscape 散点图会非常漂亮，会聚集成好几个明显分开的簇（Clusters）。

随后我们打开 SSN Finalization 界面，我们会看到一个叫 **Alignment Score Threshold（AS）** 的参数，AS 这个参数是用来筛选连线的。**AS = 50 相当于 BLAST 的 E-value 为 10 的负 50 次方**。AS 值越大，要求两条序列越像才能连线，图里的簇（Cluster）就会分得越散。根据 Dataset Analysis 中的建议，我们设置 AS 值为 40。

在 Sequence Length Restrictions (序列长度限制)选项中，基于 Dataset Analysis 中的分析结果，绝大多数序列都在 390-410 之间。因此我们在 Minimum length (最小长度) 处填入**350**，在 Maximum length (最大长度) 处填入：**450**。设置 350-450 可以有效地把那些残缺不全的测序片段（Fragments）过滤掉，让生成的网络图更干净、更准确。

输入任务名之后，点击 Create SSN，此时，服务器会在后台进行计算。

计算完毕后，会收到一封邮件，打开邮件里的链接，打开 Networks Files。
- Full Network（全网络）：每个节点对应**单个蛋白序列**，保留最精细的序列间连接关系，无聚类简化
- Representative Node Networks（代表节点网络）：按序列一致性百分比（% ID）聚类，每个节点代表一组高相似性蛋白，节点 / 边数大幅减少，聚类结构与全网络一致。

![image.png](https://synbiopath.online/20260311184841259.png)

### 2. 对从 NCBI 中获得的数据进行分析

打开下列网址，进入 EFI-EST 网站
https://efi.igb.illinois.edu/efi-est/
![image.png](https://synbiopath.online/20260310215643621.png)

在 Fasta 界面，点击 Choose a file，上传刚刚获得的 fasta文件，提交之后，输入任务名和邮箱，点击 submit analysis。
![image.png](https://synbiopath.online/20260310215712867.png)

此时，服务器会在后台计算所有序列两两之间的相似性。算好后，会给你的邮箱发一封邮件，点击邮件里的链接。

随后，我们就可以按照 「对从 EFI-EST 中获得的序列数据进行分析」中的步骤进行分析处理了。


## （三）使用 Cytoscape 绘制并美化 SSN 图

### 1. 下载并安装软件：

去官网 ([https://cytoscape.org/](https://www.google.com/url?sa=E&q=https%3A%2F%2Fcytoscape.org%2F)) 下载 **Cytoscape** 并安装（它是免费的。如果提示需要安装 Java 运行环境，请按提示安装）。


### 2. 导入文件

打开 Cytoscape，点击左上角的 File -> Import -> Network from File...，- 选中你刚才从 EFI 网站下载的 **.xgmml** 文件并打开。
![image.png](https://synbiopath.online/20260311190230323.png)

当 Cytoscape 处于如下状态时，就代表已经导入完成了
![image.png](https://synbiopath.online/20260311192057610.png)

#### 3. **给网络图“整形”（改变布局）**：

刚导进去的时候，所有的点（序列）可能挤成一团方块，非常难看。
![image.png](https://synbiopath.online/20260313113519363.png)

点击工具栏中的 Layout -> Prefuse Force Directed Layout -> alignment_score，软件会计算一会儿，然后图就会“炸开”，相似的序列会聚集成一簇一簇的（Cluster）。这就有了SSN的雏形了！
![image.png](https://synbiopath.online/20260313113551413.png)


>注意：在构建序列相似性网络 SSN 图谱时，Prefuse Force Directed Layout 是最通用的一种布局方式，适合大多数中小型网络。当超过 1000  条数据时，应选择 Prefuse Force Directed OpenCL Layout，该算法会使用 GPU 加速（OpenCL），处理大规模网络更快。
>
>在应用 Prefuse 力导向布局时，会提供不同的选项应用“边权重（edge weight）”来影响节点的排列。一般默认使用 alignment_score（比对得分）作为权重，该选项非常适合基于同源/相似性构建的网络（如蛋白家族、基因 ortholog 网络）。


#### 4. 统一节点样式

在 Cytoscape 左侧控制面板，点击 **Style**（样式）标签页，确保下方选中的是 **Node**（节点）。
![image.png](https://synbiopath.online/20260313154519868.png)

找到 **Fill Color**（填充色），然后点击 Fill Color 最左侧的默认颜色块，点击 ColarBrowser Diverging -> RGB，输入颜色代码 CADBEF，或输入RGB代码：R 202 G 219 B 239。
![image.png](https://synbiopath.online/20260313163405304.png)


**增加黑色描边**：找到 **Border Paint**（边框颜色），点击左侧默认色块，选**黑色**；找到 **Border Width**（边框宽度），点击左侧默认数字，输入 **5.0**（默认是 0，所以看不见边框）。
![image.png](https://synbiopath.online/20260313162430211.png)

**调整节点大小和形状**：找到左侧控制面板中的 Height 和 Width，把默认值改为 50。然后找到 Shape，把形状改为圆形。
![image.png](https://synbiopath.online/20260313163813149.png)

**调淡连线颜色**：点击下方的 **Edge**（边）标签，找到 Stroke Color (Unselected)，点击 ColarBrowser Diverging -> RGB，输入颜色代码 DDDDDD，或输入RGB代码：R 221 G 221 B 221。把默认颜色改为**浅灰色**，这样连线就不会喧宾夺主。
![image.png](https://synbiopath.online/20260313164005149.png)


#### 5. 清理并定制标签文字（Label） 

**隐藏所有默认标签**：回到 **Node**（节点）样式页面，找到 **Label**，点击映射旁边的 🗑️ 垃圾桶，删掉它。现在整个图变得干干净净，没有任何文字。
![image.png](https://synbiopath.online/20260313164336245.png)

**把标签位置移到下方**：
- 勾选左侧属性列表中的 More Properties 下拉菜单，确保 Label Position（标签位置）被勾选显示出来。
![image.png](https://synbiopath.online/20260313164533827.png)
![image.png](https://synbiopath.online/20260313164623002.png)

- 找到 **Label Position**，点击左侧的默认方块，会弹出一个九宫格位置设置。
![image.png](https://synbiopath.online/20260313164716154.png)

- 把 Node Anchor（节点锚点）选在**中下（South）**，把 Label Anchor（标签锚点）选在**中上（North）**。这就代表文字会挂在节点的正下方。
![image.png](https://synbiopath.online/20260313164906720.png)

**调整字体大小**：找到 **Label Font Size**，把默认值改为 16。勾选左侧属性列表中的 More Properties 下拉菜单，选中 Label Font Face（标签字体）。找到左侧控制面板中的 Label Font Face，选择字体为 **Arial Bold**。
![image.png](https://synbiopath.online/20260313165253438.png)

#### 6. 给特殊节点上色（Bypass 功能）

在图上用鼠标**单独点击选中**你想高亮的那个节点（比如你想作为 pigA1 的那个节点，选中后它会变成黄色提示被选中）。
![image.png](https://synbiopath.online/20260313165708267.png)

回到左侧 Style -> Node 面板，属性栏的第三列有一个空白的小方块，这叫 Bypass 专栏，意思是“只对当前选中的节点强制生效”。

**给节点上色 (Node Fill Color)**：找到 Fill Color，展开它。你可以根据序列的属性（比如物种分布、序列长度、或者是不是你的目标序列）来上色。在 Column 里选择你想映射的属性（比如 Description 或 Length），然后在 Mapping Type 选择 Discrete Mapping（离散映射）或 Continuous Mapping（连续映射），接着挑一个好看的调色板。
![image.png](https://synbiopath.online/20260312110110490.png)

**改变节点形状 (Shape)**：点击 Shape，可以把默认的序列设置成圆形，把你的目标研究序列设置成巨大的星星或三角形，让它醒目，接着挑一个好看的调色板。
![image.png](https://synbiopath.online/20260312111017197.png)

**去掉碍眼的标签 (Label)**：默认可能每个点上都有很长的名字，显得杂乱。在 Style -> Node -> Label 里，把映射清空，点就变干净了。
![image.png](https://synbiopath.online/20260312111056424.png)

#### 5. 导出图片

调整到你满意的样子后，点击 File -> Export -> Network to Image -> PNG，勾选 Hide Labels。
![image.png](https://synbiopath.online/20260312175223881.png)



![image.png](https://synbiopath.online/20260312175132902.png)
