
# 一：视频教程

[Sequence Similarity Network (SSN) 和进化树 Phylogenetic Tree](https://www.bilibili.com/video/BV1A94y1Y75j/?spm_id_from=333.337.search-card.all.click)

# 二：案例素材

## （一）序列文件

GenBank: UFA62170.1

>UFA62170.1氨基酸序列
>MRETIPIKYIDTIEINKLSIQDLEDLSSCKYKLLSAYLIGKIPANKILDADELEIYHNERTKKILAKAIKARKLVIVLKATRLCNLRCTYCHSWAEGPNQTILFSTLIHIVRQILAIPNVNRFEFVWHGGEVTLLKPAFFKKLIWLQEQFKRPEQYITNTMQSNIVNISDEWLIFIKGIGMNVGISLDGIPAVNDKRRVDFRGRGTSDRIAKGIKKLQKYDILYGALIVVDREVYQTDMREMLDYFILIELNGIEFLNIVPDNRLTAGEDIGNNFISYAEFIKFLSALFVIWIKGYREKIHIAIFEDFISVLENPEKKLSACYWSGNCSQEIITLEPNGDVSPCDKYRGDAGSIYGSLLKTDLAGLLTQSSHNQQAIDEEVAATRKMQHCEWFSICHGGCPHDRVINRRHTKGYNDECCGTGKLLATIKAYLADIR

https://www.ncbi.nlm.nih.gov/protein/UFA62170.1/?report=fasta

## （二）所用软件


# 三：实操教程

## （一）准备序列数据

首先，我们要明确自己的数据是什么情况：
- **情况 A：只有 1 条蛋白质序列**。那需要用这条序列去数据库里“钓”出它的同源序列，然后再做网络图。
- **情况 B：你已经有了一个包含很多条序列的文件（FASTA格式）**。比如几十上百条序列，你想看看它们之间的聚类关系。可以直接上传到 EFI-EST 网站，进行分析

如果是情况 A，也有两种处理方法：
- **方法一**：直接在 EFI-EST 网站中选择 **Option A (BLAST)**。把你的那条序列粘贴进去，设置最多提取多少条同源序列（比如默认的1000条或5000条），即可获得用于构建序列分子网络所需要的序列数据。
- **方法二**：在 NCBI 中对这条序列进行 Blastp 搜索，下载对应的 Fasta 序列合集，也可获得用于构建序列分子网络所需要的序列数据。


## （一）Blast 分析

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

在这个界面中，点击 Send to，选择为 File，格式为 fasta，点击 create file，即可获得目标序列同源蛋白的 fasta 序列。
![image.png](https://synbiopath.online/20260310213301498.png)


## （二）EFI-EST 分析

打开下列网址，进入 EFI-EST 网站
https://efi.igb.illinois.edu/efi-est/
![image.png](https://synbiopath.online/20260310215643621.png)

在 Fasta 界面，点击 Choose a file，上传刚刚获得的 fasta文件，提交之后，输入人物名和邮箱，点击 submit analysis。
![image.png](https://synbiopath.online/20260310215712867.png)
