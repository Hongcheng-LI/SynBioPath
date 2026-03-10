
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

在这个界面中，选中所有的目标序列之后，点击 Send to，选择为 File，格式为 fasta，点击 create file，即可获得目标序列同源蛋白的 fasta 序列。
![image.png](https://synbiopath.online/20260310213301498.png)
