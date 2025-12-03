
**Ubuntu 安装 Gaussian**

\1. **Gaussian 简介**

Gaussian 是一款广泛使用的量子化学计算软件，用于研究分子的电子结构、化学反应、分子轨道、振动频率等。它在化学、材料科学、药物设计和理论物理等领域有着重要的应用。

\2. **Gaussian 16 安装**

1. 解压文件

```C#
# 解压文件
tar -xvf g16.tar.xz```

2. 将解压后的文件夹 移动到/home/lhc/

3. 进入 /home/lhc/g16 目录中，新建 scratch 文件夹，用于储存 Gaussian 运行过程中产生的临时文件。

```C#
# 新建 scratch文件夹
mkdir scratch```

4. 配置环境变量

```C#
# 使用 vim 打开 .bashrc 文件
vim ~/.bashrc

# 打开仅阅读模式
O

# 进入编辑模式
i

# 将光标移至最后，输入下列代码
export g16root=/home/lhc/
export GAUSS\_SCRDIR=/home/lhc/g16/scratch
source /home/lhc/g16/bsd/g16.profile

# 摁 esc 键退出编辑模式

# 强制保存并退出
:wq!

# 执行以下命令使配置生效
source ~/.bashrc```

5. 设置并行计算的核心数及内存大小

```电脑的内存为 32Gb，CPU 的核心数为 16 核心，因此分配 12 核心，28 GB 内存用于并行计算。```

在 /home/lhc/g16/ 文件夹中打开终端

```C#
# 使用 vim 新建 DefaultRoute 文件
vim Default.Route

# 进入编辑模式
i

# 输入下列内容
-M- 28GB
-P- 12

# 摁 esc 退出编辑界面

# 退出并保存
:wq!```

\3. **GaussView 09 安装**

1. 解压文件

```C#
# 解压文件
tar -xvf gv.tar.xz```

2. 将解压后的文件夹移动到 /home/lhc/g16/

3. 配置环境变量

```C#
# 使用 vim 打开 .bashrc 文件
vim ~/.bashrc

# 打开仅阅读模式
O

# 进入编辑模式
i

# 将光标移至最后，输入下列代码
export GV\_DIR=/home/lhc/g16/gv/
export LIBPATH=/home/lhc/g16/gv/lib
export LD\_LIBRATY\_PATH=$LD\_LIBTATY\_PATH:/home/lhc/g16/gv/lib
PATH=$PATH:/home/lhc/g16/gv/
alias='gv=gview.exe'

# 摁 esc 键退出编辑模式

# 强制保存并退出
:wq!

# 执行以下命令使配置生效
source ~/.bashrc```

4. 验证安装是否成功

```C#
# 输入下列命令
gv```

若能打开 GaussView 06 窗口界面，则证明安装成功

\4. **参考资料**

[Gaussian的安装方法及运行时的相关问题](http://sobereva.com/439)

