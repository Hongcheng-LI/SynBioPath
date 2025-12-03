
**NCBI Banklt：在线提交基因序列**


```天然产物生物合成领域的研究人员在发表相关研究论文时，需要将基因簇的信息提交至 NCBI。本文介绍通过 NCBI Banklt 在线提交基因簇信息的详细教程。```

\1. **前期准备**

1. 在开始提交之前，需提前准备好**核酸序列与氨基酸序列的 fasta 文件**。

```<p>基因簇中所有基因的核酸序列或氨基酸序列均存放在同一个 fasta 文件内。</p><p>核酸序列 fasta 文件和氨基酸序列 fasta 文件内相同基因的 Sequence\_ID 要相同 </p>```
![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\NCBI%20Banklt：在线提交基因序列.001.png)

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\NCBI%20Banklt：在线提交基因序列.002.png)

\2. **注册  NCBI 账号并登陆**

1. 进入 NCBI 官网，点击界面右上角的 log in，进入注册及登录界面。

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\NCBI%20Banklt：在线提交基因序列.003.png)

2. 如果之前有 NCBI 账号，则选择 Log in again with XXX，如果没有 NCBI 账号，则点击 More login options，点击下方的 sign up 进行注册。 

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\NCBI%20Banklt：在线提交基因序列.004.png)

3. 注册账号时，推荐选择使用 Microsoft 账号进行注册。

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\NCBI%20Banklt：在线提交基因序列.005.png)

\3. **进入 Banklt 提交界面**

1. 账号注册完成后，点击 NCBI 首页的 submit 选项，进入提交页面。

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\NCBI%20Banklt：在线提交基因序列.006.png)

2. 由于上传的基因序列属于 genomic DNA，因此点击红框中的 submit 进入 Banklt 界面。

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\NCBI%20Banklt：在线提交基因序列.007.png)

3. 在 Banklt 界面中，选择 Start Banklt Submission 开始提交序列，此时 NCBI 会自动分配一个 Submission ID。 

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\NCBI%20Banklt：在线提交基因序列.008.png)

\4. **正式提交**

4.1 **Contact**

1. 在此界面，需要补充个人的详细信息，建议除 Phone 及 Fax 外，其余均认真填写。填写完成后，点击Continue。

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\NCBI%20Banklt：在线提交基因序列.009.png)

4.2 **Reference**

1. 在此界面，需要填写序列作者（Sequence Authors）及参考信息（Reference Information）。
- 序列作者：填写文章的全部作者。
- 发表状态（Publication Status）：选择未发表（Unpublished）、发表（Published）和出版（In-Press）。
- 参考题目（Reference Title）：填写相应文章的题目。
- 参考作者（Reference Authors）：选择 Same As Sequence Authors。

2. 填写完毕后，点击 Continue 进行下一步。

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\NCBI%20Banklt：在线提交基因序列.010.png)

4.3 **Sequencing Technology**

1. 在此界面，需要填写测序技术（Sequencing Technology）及组装软件（Assembly Program）。
- 测序技术：根据实际情况选择相应的测序技术即可，一代测序技术为 Sanger dideoxy sequencing。二代测序技术为 Illumina，三代测序技术为 PacBio 和 Nanopore。
- 组装与否：选择 Assembled sequence。
- 组装软件：若不清楚组装软件及版本，可填写 # 代替。

2. 填写完毕后，点击 Continue 进行下一步。

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\NCBI%20Banklt：在线提交基因序列.011.png)

4.4 **Nucleotide**

1. 在此步骤中，需要设置序列的释放日期（Submission Release Date）、序列类型（Molecule Type）、拓扑结构（Topology）、序列格式（Sequence data format）并上传核酸序列的 fasta 文件。
- 序列释放日期：选择立即释放（Immediately After Processing）或指定特定的释放日期（Release Date）。
- 序列类型：选择 genomic DNA。
- 拓扑结构：选择 Linear。
- 序列格式：Fasta 文件。
- 上传核酸序列：上传之前准备好的核酸序列 fasta 文件。

2. 填写完毕后，点击 Continue 进行下一步。

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\NCBI%20Banklt：在线提交基因序列.001.png)

4.5 **Organsim**

1. 在此步骤中，需要提供基因的组织名称（Organism name）。
- 组织名称：填写基因的物种来源，例如 *Penicillium oxalicium*。

2. 填写完毕后，点击 Continue 进行下一步。

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\NCBI%20Banklt：在线提交基因序列.012.png)

3. 此时，会在界面下方显示 fasta 文件中所有基因的序列 ID（Sequence ID）及物种来源。核对无误后，继续点击 Continue 进行下一步。

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\NCBI%20Banklt：在线提交基因序列.013.png)

4.6 **Set/Batch**

1. 在此步骤中，需要设置所上传基因的类型。此处选择 Batch，即：所上传的基因是可能来自同一生物的多个相关基因。

2. 填写完毕后，点击 Continue 进行下一步。

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\NCBI%20Banklt：在线提交基因序列.014.png)

4.7 **Submission Category**

1. 在此步骤中，需要设置所提交基因的类别，是初次提交（Original）还是来自于第三方机构（Third Party Annotation）。此处选择初次提交。

2. 填写完毕后，点击 Continue 进行下一步。

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\NCBI%20Banklt：在线提交基因序列.015.png)

4.8 **Source Modifiers**

1. 在此步骤中，需要设置基因在来源物种中的位置，包括质粒、线粒体等等。此处可不填写，直接点击 Continue 进入下一步。

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\NCBI%20Banklt：在线提交基因序列.016.png)

4.9 **Feature（重要）**

1. 在此步骤中，需要对提交的核酸序列进行注释。此处选择通过添加氨基酸序列进行注释。

2. 首先选择 Add features by completing input forms，在下方选择 Coding Region (CDS) / Gene / mRNA -- if your sequence encodes a protein, choose this option，接下来选择 providing protein sequence data，最后选择 Add 添加氨基酸序列 fasta 文件。

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\NCBI%20Banklt：在线提交基因序列.017.png)

3. 在新出现的界面中，需要填写序列的相关信息，包括 CDS 所含有的序列部位（Partial）、蛋白名称（Protein Name）、蛋白序列（Protein sequence）、mRNA 信息（mRNA information）。
- 序列部位：同时选中 5' 和 3'。
- 蛋白名称：若上传单个基因，可准确填写，若同时上传多个基因，则可随便填写，后期精准修改。
- 蛋白序列：上传之前准备好的氨基酸序列 fasta 文件。
- mRNA 信息：选中添加 mRNA。

4. 填写完毕后，选择最下方的 Accept。

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\NCBI%20Banklt：在线提交基因序列.018.png)

5. 在新出现的界面中，点击列表中的 edit，对单个基因的名称及产物进行详细注释。

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\NCBI%20Banklt：在线提交基因序列.019.png)

6. 在新出现的界面中，可以看到，序列类型已选中为线性（Strand），序列中包含 5' 和 3'，同时也已添加 mRNA 信息。接下来只需要修改蛋白信息（Protein Information）和基因信息（Gene Information）即可。
- 蛋白名称：该基因簇被命名为 opd BGC，因此核心基因编码的蛋白被注视为 OpdA。
- 蛋白描述：OpdA 的功能被注释为 PKS-NRPS。
- 基因名称：该基因被注释为 *opdA*。
- 基因描述：*opdA* 的功能被注释为 PKS-NRPS。

7. 填写完毕后，点击左下角的 accept 返回上一界面，继续对下一个基因进行注释。所有基因全部注释完毕后，点击 continue 进入最后的环节。

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\NCBI%20Banklt：在线提交基因序列.020.png)

4.10 **Review and Correct**

1. 对填写完成的信息进行检查并修改，确认无误后，点击 Finish submission 完成序列上传工作。

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\NCBI%20Banklt：在线提交基因序列.021.png)

2. 在新的页面中，会看到序列上传成功，并且 GeneBank accession numbers 会在两个工作日内发送到邮箱中。

![...](..\..\0.%20软件教程\生物信息学工具（Windows）\images\NCBI%20Banklt：在线提交基因序列.022.png)

\5. **参考资料**

[如何利用BankIt向NCBI在线提交序列](https://www.biomart.cn/experiment/430/590/597/57949.htm)

