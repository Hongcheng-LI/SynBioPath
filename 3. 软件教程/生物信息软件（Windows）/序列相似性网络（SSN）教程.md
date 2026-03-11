
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


在 SSN Finalization 界面，我们会看到一个叫 **Alignment Score Threshold（AS）** 的参数，AS 这个参数是用来筛选连线的。**AS = 50 相当于 BLAST 的 E-value 为 10 的负 50 次方**。AS 值越大，要求两条序列越像才能连线，图里的簇（Cluster）就会分得越散。你可以用不同的 AS 值生成好几个网络，到时候看看哪个聚类效果最符合你的研究预期。



### 2. 对从 NCBI 中获得的数据进行分析

打开下列网址，进入 EFI-EST 网站
https://efi.igb.illinois.edu/efi-est/
![image.png](https://synbiopath.online/20260310215643621.png)

在 Fasta 界面，点击 Choose a file，上传刚刚获得的 fasta文件，提交之后，输入任务名和邮箱，点击 submit analysis。
![image.png](https://synbiopath.online/20260310215712867.png)

此时，服务器会在后台计算所有序列两两之间的相似性。算好后，会给你的邮箱发一封邮件，点击邮件里的链接。

在打开的连接中，可以看到在 Dataset Summary 处列出了这个数据集的各种信息，此时我们点击 SSN Finalization，进行 SSN 网络优化
![image.png](https://synbiopath.online/20260311170723752.png)

在 SSN Finalization 界面，我们会看到一个叫 **Alignment Score Threshold（AS）** 的参数，AS 这个参数是用来筛选连线的。**AS = 50 相当于 BLAST 的 E-value 为 10 的负 50 次方**。AS 值越大，要求两条序列越像才能连线，图里的簇（Cluster）就会分得越散。你可以用不同的 AS 值生成好几个网络，到时候看看哪个聚类效果最符合你的研究预期。
![image.png](https://synbiopath.online/20260311171852062.png)

在序列长度过滤（Sequence Length Restriction Options）界面，主要用于根据序列长度筛选 SSN 中的蛋白序列，避免过短 / 过长的异常序列干扰分析，此处我们可以不做设置。

点击 Create SSN，此时，服务器会在后台进行计算。
