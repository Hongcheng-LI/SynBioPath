在用 Augustus 对测序的基因组数据进行注释之后，随后用 TBtool 软件，根据 gff3 注释文件提取基因组中的全部基因信息。

---

# 1. TBtool 下载及安装
## 1.1 下载地址
- **Microsoft 应用商店**：https://apps.microsoft.com/detail/9nvr9lb426p2?hl=zh-CN&gl=US 
- **GitHub**：https://github.com/CJ-Chen/TBtools-II 

## 1.2 软件使用手册
https://www.yuque.com/cjchen/hirv8i/xq65ml

## 1.3 软件安装
下载完成后，直接双击安装器即可完成。

---

# 2. 提取全部基因信息用于本地 blast
1. 点击菜单栏中的 ==`sequence Toolkit`== > ==GFF3/GTF Manipilate== > ==GXF Sequence Extract==
![image.png](http://synbiopath.online/20251215153425371.png)

2. 按照以下步骤，完成所有操作
	- 1：在此处上传 Augustus 注释生成的 gff3 文件，此处为 ==SQ11-20.gff3==
	- 2：点击 ==Initialize==，对上传的 gff3 文件进行初始化处理
	- 3：Feature Tag 处选择 ==gene== 标签
	- 4：Feature ID 选择 ==ID== 格式
	- 5：在此处上传基因组测序生成的（拼装好的）原始基因组数据，此处为 ==SQ11-20.fasta==
	- 6：Up Stream Bases：选择 ==0==
	- 7：Down Stream Bases：选择 ==0==
	- 8：先在桌面上新建一个txt文件，命名为 ==SQ11-20_gene.txt==，然后在此处输入该文件的地址：==C:\Users\lhc\Desktop\SQ11-20.fasta==
	- 9：点击 ==start==，提示完成后，就会发现桌面上生成了 3 个文件，我们先前建立的 SQ11-20_gene.txt 文档已经含有了根据 gff3 注释信息从基因组文件中提取出来的全部基因序列。
![4adcd861-58f3-44c2-9eb3-27e35bdc1195.png](http://synbiopath.online/4adcd861-58f3-44c2-9eb3-27e35bdc1195.png)

此时，将 ==SQ11-20_gene.txt== 的后缀名 txt 改为 fasta，即可用于本地 blast。


---

# 3. 提取全部基因信息用于基因敲除
1. 点击菜单栏中的 ==`sequence Toolkit`== > ==GFF3/GTF Manipilate== > ==GXF Sequence Extract==
![image.png](http://synbiopath.online/20251215153425371.png)

2. 按照以下步骤，完成所有操作
	- 1：在此处上传 Augustus 注释生成的 gff3 文件，此处为 ==SQ11-20.gff3==
	- 2：点击 ==Initialize==，对上传的 gff3 文件进行初始化处理
	- 3：Feature Tag 处选择 ==gene== 标签
	- 4：Feature ID 选择 ==ID== 格式
	- 5：在此处上传基因组测序生成的（拼装好的）原始基因组数据，此处为 ==SQ11-20.fasta==
	- 6：Up Stream Bases：选择 ==0==
	- 7：Down Stream Bases：选择 ==0==
	- 8：先在桌面上新建一个txt文件，命名为 ==SQ11-20_gene.txt==，然后在此处输入该文件的地址：==C:\Users\lhc\Desktop\SQ11-20.fasta==
	- 9：点击 ==start==，提示完成后，就会发现桌面上生成了 3 个文件，我们先前建立的 SQ11-20_gene.txt 文档已经含有了根据 gff3 注释信息从基因组文件中提取出来的全部基因序列。


此时，将 ==SQ11-20_gene.txt== 的后缀名 txt 改为 fasta，即可用于本地 blast。