
**DeepBGC 安装及使用教程**

\1. **DeepBGC 简介**

DeepBGC 使用深度学习来检测细菌和真菌基因组中的 BGC，可以挖掘到 antismash 没有分析出来的 BGC。

\2. **DeepBGC 的安装**

1. 安装 conda

[Ubuntu系统安装 Conda](Ubuntu系统安装 Conda.md)

2. 创建 DeepBGC 环境，并安装所需的依赖

```C#
# 创建 DeepBGC 环境，并安装所需的依赖
conda create -n deepbgc python=3.7 hmmer prodigal```

3. 激活 DeepBGC 环境

```C#
# 激活 DeepBGC 环境
conda activate deepbgc```

4. 安装 DeepBGC，共有两种不同的方法，一种是使用 pip 安装，另一种是使用 conda 安装

```C#
pip 安装 DeepBGC
# 使用 pip 安装 DeepBGC
pip install deepbgc```


```C#
使用 Conda 安装 DeepBGC
# 使用 Conda 安装 DeepBGC
conda install deepbgc```



