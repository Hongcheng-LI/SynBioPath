
**Gaussian 16 安装教程**

\1. **软件简介**

在天然产物研究领域，Gaussian 通常用于计算 ECD，以便确定化合物的绝对构型。

\2. **安装教程**

2.1 **安装 Gaussian 16**

1. 解压压缩包

```C#
#解压 g16 压缩包
tar -xvf g16.tar```

2. 进入 Gaussian 16 所在文件夹

```C#
#进入 Gaussian 16 所在文件夹
cd g16```

3. 建立 scratch 文件夹，用于存放计算的文件

```C#
#建立 scratch 文件夹，用于存放计算的文件
mkdir scratch```

4：编辑类似环境信息

```C#
#编辑类似环境信息
gedit ~/.bashrc```

5：在新弹出的窗口结尾处输入下列<最重要的信息>

```C#
export g16root=/home/lhc/
export GAUSS\_SCRDIR=/home/lhc/g16/scratch
source /home/lhc/g16/bsd/g16.profile```


```注意：路径中的“/home/lhc/”要更换为自己的实际路径```

6. 在 /home/lhc/g16 目录下运行下列命令：

（1）更改文件夹权限

```C#
#更改文件夹权限
chmod 750 -R \* ```

（2）激活环境，不会报错为正确，否则查找原因。

```C#
source ~/.bashrc```

2.2 **安装 GaussView**

1. 解压压缩包

```C#
#解压 GaussView 压缩包
tar -xvf gv.tar```

2. 进入 GaussView 所在文件夹

```C#
#进入 GaussView 所在文件夹
cd gv```

3. 编辑类似环境信息

```C#
#编辑类似环境信息
gedit ~/.bashrc```

4. 在新弹出的窗口结尾处输入下列信息

```C#
export GV\_DIR=/home/lhc/g16/gv/
export LIBPATH=/home/lhc/g16/gv/lib
export LD\_LIBRARY\_PATH=$LD\_LIBRARY\_PATH:/home/lhc/g16/gv/lib
PATH=$PATH:/home/lhc/g16/gv/```


```注意：路径中的“/home/lhc/”要更换为自己的实际路径```

5. 在终端输入 gv，即可出现 GaussView 软件界面

```C#
#打开 GaussView 软件界面
gv```



