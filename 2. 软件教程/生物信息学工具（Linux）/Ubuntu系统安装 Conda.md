
**Ubuntu系统安装 Conda**

\1. **Conda 简介**

Conda 是一个可以在 Windows、macOS 和 Linux 上运行的开源的软件和环境管理系统。利用 Conda 可以快速安装、运行和更新软件包及其依赖环境。

Conda 分为 anaconda 和 miniconda。anaconda是包含一些常用包的版本，占用内存较大。miniconda 则是精简版，需要啥装啥，所以推荐使用 miniconda。

\2. **miniconda 下载与安装**

1. 从清华镜像源去下载 miniconda 的安装包

```C#
# 从清华镜像源去下载 miniconda 的安装包
wget -c https://mirrors.bfsu.edu.cn/anaconda/miniconda/Miniconda3-latest-Linux-x86\_64.sh```

2. 给刚下载好的安装包可执行权限

```C#
#刚下载好的安装包没有可执行权限，所以需要先给权限
chmod 777 Miniconda3-latest-Linux-x86\_64.sh```

3. 使用 bash 安装 conda

```C#
#使用 bash 安装 conda，以 .sh 结尾的文件，除了 bash  之外还可以使用 ./ 运行
bash Miniconda3-latest-Linux-x86\_64.sh```

4. 输入 **bash** 命令后，此时开始安装 minconda，注意在安装过程中，需要输入两次 **yes**。

![...](..\..\0.%20软件教程\生物信息学工具（Linux）\images\Ubuntu系统安装%20Conda.001.png)

5. miniconda 安装结束后，需要将 conda 路径添加至环境变量中。

```C#
#在终端中输入以下命令，打开对应的配置文件：
vim ~/.bashrc```

6. 此时，会打开一个对应的环境变量配置文件，你会看到一个蓝色的界面，显示文件内容。此时，vim 默认处于“普通模式”，无法直接编辑内容。按  **i**  键进入“插入模式”，这样你就可以开始编辑文件了。

7. 将光标移动到文件的末尾，在文件末尾添加上 miniconda 的路径。Miniconda3 中 bin 文件夹的位置为：**/home/lwl/miniconda3/bin（每个人的文件安装地址不同，请自行查看并修改）**。因此我在环境变量配置文件的末尾加入下列一行内容，即可将 conda 路径添加至环境变量中。

```C#
#在环境变量配置文件的末尾加入下列一行内容，将conda 路径添加至环境变量中。
export PATH=$PATH:/home/lwl/miniconda3/bin```

8. 完成编辑后，按 Esc 键退出“插入模式”，回到“普通模式”。输入以下命令保存文件并退出。

```C#
#强制保存并退出文件
：wq!```

9. 保存并退出后，需要重新加载配置文件，使更改生效。在终端中运行以下命令：

```C#
source ~/.bashrc```

10. 输入下列命令，查看 conda 版本号，显示版本号则证明路径已成功添加至环境变量中

```C#
#输入下列命令，查看 conda 版本号
conda --version```
![...](..\..\0.%20软件教程\生物信息学工具（Linux）\images\Ubuntu系统安装%20Conda.002.png)

\3. **配置镜像**

1. 在使用 conda 安装其他开源软件时，默认去自己的官网搜索软件源。Conda 官网所在的服务器位于国外，而我们使用的服务器位于国内，利用国内的网络去访问国外的网站时会特别慢，所以需要配置镜像，提高软件的下载安装速度。

2. 国内常用的镜像一般是清华的镜像源，输入以下命令，安装各种镜像源。

```C#
#安装各种镜像源
conda config --add channels conda-forge
conda config --add channels defaults
conda config --add channels r
conda config --add channels bioconda
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/bioconda/
conda config --set show\_channel\_urls yes```

3. 查看已经添加的 channels

```C#
# 查看已经添加的 channels
conda config --get channels```


