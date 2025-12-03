
**Ubuntu 安装 antiSMASH 7**

\1. **简介**

细菌和真菌的次级代谢机制使其成为具有潜在药用价值的生物活性化合物的丰富来源，包括抗生物、降胆固醇药物或抗肿瘤药物。部分化合物在微生物体内的生物合成途径已经被鉴定，有意思的是，编码负责产生这种次级代谢产物的基因通常在染色体上成簇存在，因此被称为“生物合成基因簇”。这种遗传结构为通过定位其基因簇直接检测次级代谢物生物合成途径提供了可能性。

近年来，细菌和真菌的测序成本已大大降低，并且许多基因组序列已经公布。基于某类基因簇中特异性基因的隐马尔可夫模型，antiSMASH 能够准确地识别编码所有已知类别的次级代谢产物的基因簇。antiSMASH 不仅可以检测基因簇，还可以提供详细的序列分析，下面介绍 antiSMASH 的安装步骤。

\2. **安装教程**

1. 下载和安装 miniconda

[Ubuntu系统安装 Conda](Ubuntu系统安装 Conda.md)

2. 创建名为 bioinfo 的环境

```C#
# 创建名为 bioinfo 的环境
conda create -y --name bioinfo python=3```


```输入该命令后，如果出现如下错误：```

```<p>Collecting package metadata (current\_repodata. json): failed</p><p>Conda HTTP Error: HTTP 000 CONNECTION FAILED for url<https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/noarch/current\_repodata.json></p><p>Elapsed: An HTTP erroroccurred when trying to retrieve this URL.</p><p>HTTP errors are often intermittent, and a simple retry will get you on your way.</p><p>'<https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/noarch'></p>```

```<p></p><p>说明缺少该 channel，conda 添加该 channel 即可</p>```


```C#
# 使用 conda 添加该 channel 
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/noarch```

3. 激活 bioinfo 环境

```C#
# 激活 bioinfo 环境
source activate bioinfo```

\4. 更新 miniconda

```C#
# 更新 miniconda
conda update conda```


```输入该命令后，如果出现如下错误：```

```<p>PackageNotInstalledError:Package is not installed in prefix.</p><p>prefix:/home/lhc/miniconda3/envs/bioinfo</p><p>package name: conda</p>```

```<p></p><p>这个时候不用慌，把终端关掉重新开启就解决了</p>```

下面进行 antiSMASH 的安装

5. ` `创建 antiSMASH 环境

```C#
# 创建 antiSMASH 环境
conda create -n antiSMASH```

6. 激活 antiSMASH 环境

```C#
# 切换到 antismash 环境中
conda activate antiSMASH```

7. 安装需要的依赖包

```C#
# 然后安装需要的依赖包
conda install -y diamond=0.8.36
conda install -y fasttree=2.1.9
conda install -y glimmerhmm=3.0.4
conda install -y hmmer=2.3.2
conda install -y hmmer=3.1b2
conda install -y meme=4.11.2
conda install -y muscle=3.8.1551
conda install -y blast=2.2.31
conda install -y prodigal=2.6.3
conda install -y java-jdk
conda install -y python
conda install hmmer2
conda install baileyandrew::python
conda install conda-forge::virtualenv
conda install bioconda::blast
conda install diamond=2.0.9```

8. 外部的一些依赖包安装好以后，接下来是下载 antiSMASH

```C#
# 下载 antismash
wget https://dl.secondarymetabolites.org/releases/7.0.0/antismash-7.0.0.tar.gz
tar -zxf antismash-7.0.0.tar.gz
pip install ./antismash-7.0.0```


```在运行“pip install ./antismash-7.0.0”时，如果出现如下报错：```

```pip.\_vendor. urllib3. exceptions. Read Time out Error: HTTPS Connection Pool (host='files. pythonhosted.org', port=443): Read timed out.```

```<p></p><p>大概率是由于网速过慢引起的，重新运行一遍“**pip install ./antismash-7.0.0**“即可</p><p></p><p></p><p>在运行“pip install ./antismash-7.0.0”时，如果出现如下报错：</p>```

```ERROR: Could not build wheels for nes-py, which is required to install pyproject.toml-based projects```

```<p></p><p>执行下面两条命令即可</p><p># 在 anaconda 搜索 moods- python 的安装命令
**conda install -c lalit.shaktawat moods-python**

# 将 python 的版本降为低版本，此处降到 3.9.0
**conda install -y python==3.9.0**</p>```

9. 此处重新运行下方代码，即可安装成功

```C#
 # 安装 antiSMASH
 pip install ./antismash-7.0.0```

此时已完成 antiSMASH 的本地安装。

10. 下载 antiSMASH 所需要的数据库

```C#
# 下载 antiSMASH 所需要的数据库
download-antismash-databases```


```# 若出现如下报错```

```Import Error: "Bio.Alphabet" has been removed from Biopython. In many cases, the alphabet can simply be ignored and removed from scripts. In a few cases, you may need to specify the "molecule\_type" as an annotation on a SeqRecord for your script to work correctly. Please see <https://biopython.org/wiki/Alphabet> for more information."```

```<p></p><p>说明是 Biopython 1.78 版本过高，需要使用较低版本</p><p></p><p># 因此首先卸载当前版本的 Biopython</p><p>pip3 uninstall biopython</p><p># 安装 Biopython 1.77</p><p>**pip3 install biopython==1.77**</p>```

11. 安装完成后，重新下载需要的数据库

```C#
#下载 antiSMASH 数据库
download-antismash-databases```



12. 得到以下的结果则说明数据库下载并且配置成功

```C#
Creating check sum of Pfam-A.hmm
PFAM file present and ok for version 27.0
Downloading PFAM version 31.0
Creating check sum of Pfam-A.hmm.gz
Creating check sum of Pfam-A.hmm.gz
Extraction of Pfam-A.hmm.gz finished successfully.
Resfams database present and checked
Creating check sum of proteins.fasta
Cluster Blast fasta file present and checked
Pre-building all databases...
done.```

13. 验证 antismash 软件是否安装成功

```C#
# 验证 antismash 软件是否安装成功
antismash --check-prereqs```


```<p>当出现以下输出结果则表示 antismash 安装成功！</p><p>All prerequisites satisfied</p>```

14. 查看 antismash 帮助文档：

```C#
# 查看 antismash 帮助文档：
antismash -h```


```<p>**下面对主要参数进行介绍**</p><p>**-h, --help**   帮助文档。
**--help-showall**   在此帮助文本中显示完整的参数。
**-cCPUS, --cpus CPUS**   设置并行使用 cpu 数量（默认是 12 个）。


**基础分析选项**:
**--taxon {bacteria, fungi}**   选择物种类型（分为 bacteria 和 fungi，默认是 bacteria）。


**附加分析选项**:
**--fullhmmer**   进行全基因组的 HMMER 分析，寻找 BGCs 中 domains 出现过于频繁的基因组区域。这样能找到一些 clusterblast 步骤中漏掉的基因簇。
**--cassis**   基于 Motif 的 BGCs 区域预测，仅用于对真菌基因组进行分析。
**--cf-borders-only**   只注释现有基因簇的边界。
**--cf-create-clusters**   发现并寻找新的基因簇。
**--clusterhmmer**   仅对 BGCs 进行 HMMer 分析。
**--smcog-trees**   对 BGCs 进行分析并归类为不同的家族，并使用该家族的基因（最多 100 个）构建系统发育树。
**--tta-thresholdTTA\_THRESHOLD**   用于注释 TTA 密码子的最低 GC 含量（默认值：0.65）
**--cb-general**   将预测的 BGCs 与 antiSMASH 预测的 BGCs 数据库进行比较。
**--cb-subclusters**   将预测的 BGCs 与已知负责合成次级代谢产物前体的亚簇进行比较。
**--cb-knownclusters**   将预测的 BGCs 与 MIBiG 数据库中已鉴定的 BGCs 进行比较。
**--asf**   对活性位点进行预测分析。
**--pfam2go**   利用 Pfam 对 BGCs 中的模块功能进行预测。


**输出参数:**
**--output-dirOUTPUT\_DIR**   输出文件夹。
**--html-titleHTML\_TITLE**   自定义 HTML 输出页面的标题（默认为输入文件名）。  
**--html-descriptionHTML\_DESCRIPTION**   将自定义描述添加到输出结果中。


**基因查找选项（注释 ORF 时忽略）:**
**--genefinding-tool {glimmerhmm, prodigal, prodigal-m, none, error}**   指定用于基因发现的算法：GlimmerHMM，Prodigal，Prodigal Metagenomic /Anonymous 模式或无。如果尝试基因发现，运行“error”选项将引起报错。运行“none”选项将不会运行基因查找（默认值：error）。
**--genefinding-gff3 GFF3\_FILE**   从指定 GFF3 文件中提取特征。</p>```


15. 从 NCBI 数据库中下载 Genbank 文件。

16. 进入 Genbank 文件所在文件夹，以桌面为例

```C#
# 进入 Genbank 文件所在文件夹，以桌面为例。
cd /home/lhc/Desktop```

17. 使用下列命令对基因组进行分析


```C#
#对细菌基因组进行分析
antismash --taxon 'bacteria' --fullhmmer --clusterhmmer --cb-general --cb-knownclusters --cb-subclusters --asf --pfam2go --smcog-trees streptomyces\_coelicolor.gbk

#对真菌基因组进行分析
antismash --taxon 'fungi' --fullhmmer --cassis --clusterhmmer --tigrfam --cc-mibig --cb-general --cb-subclusters --cb-knownclusters --pfam2go --rre --tfbs --asf --genefinding-tool 'glimmerhmm' 1032.fasta```

18. 结果文件保存于 **streptomyces\_coelicolor** 或 **1032** 文件夹中。点击 **index.html** 查看预测结果。

\3. **参考教程**

[1：Bioconda 安装与使用](https://www.jianshu.com/p/a20bb8c0bc5c)

[2：antismash 安装教程](http://blog.sciencenet.cn/blog-3416913-1240614.html)

[3：报错解决办法（一）](https://blog.csdn.net/Hellokitty101/article/details/134357077)

[4：报错解决办法（二）](https://blog.csdn.net/weixin_45552562/article/details/109668589)

[5：报错解决办法（三）](https://blog.csdn.net/qq_47054630/article/details/132100417)

