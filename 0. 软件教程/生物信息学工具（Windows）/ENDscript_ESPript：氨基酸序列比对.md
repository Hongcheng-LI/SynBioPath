
**ENDscript\_ESPript：氨基酸序列比对**

\1. **所用工具**

1. CLUSTALW 网站

<https://www.genome.jp/tools-bin/clustalw>

2. ENDscript/ESPript 网站

<https://espript.ibcp.fr/ESPript/cgi-bin/ESPript.cgi>

\2. **使用教程**

1. 进入 CLUSTALW 网站，按 fasta 格式输入所有蛋白的氨基酸序列。

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\ENDscript\_ESPript：氨基酸序列比对.001.png)

参数设置

- Output Format: **CLUSTAL**
- Pairwise Alignment: **FAST/APPROXIMATE**
- Enter your sequence: **Protein**

2. 点击 Execute Multiple Alignment，在新弹出的结果界面中选择 **Clustalw.aln** 下载序列比对文件。

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\ENDscript\_ESPript：氨基酸序列比对.002.png)

3. 进入 ENDscript/ESPript 网站，点击浏览，将刚刚得到的序列比对文件上传至此处。

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\ENDscript\_ESPript：氨基酸序列比对.003.png)

4. 修改参数，将 Number of columns 改为 100，Gap between blocks 改为 3。

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\ENDscript\_ESPript：氨基酸序列比对.004.png)

参数说明：

- Number of columns：每一行显示的氨基酸残基数目，本次设置每一行显示 100 个氨基酸。
- Gap between blocks：段与段之间的距离，基本单位为 1 行。本次设置段与段之间的距离为 3 行。

5. 设置图片格式，选择 PNG image（300 dpi）或 TIF image（300 dpi）格式，得到的结果可直接用于文章发表。

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\ENDscript\_ESPript：氨基酸序列比对.005.png)

6. 参数设置完成后，点击页面最上方的 SUBMIT，几秒后即可在弹出的结果页面下载氨基酸序列比对结果。

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\ENDscript\_ESPript：氨基酸序列比对.006.png)

\3. **参考教程**

[如何做出漂亮的序列比对图——ENDscript/ESPript](https://blog.csdn.net/duwenyi2017/article/details/78822245)

