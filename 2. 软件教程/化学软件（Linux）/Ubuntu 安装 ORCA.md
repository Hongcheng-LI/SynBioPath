
**Ubuntu 安装 ORCA**

\1. **ORCA 简介**

ORCA 是一款专业的量子化学计算软件，主要用于模拟和研究分子的电子结构和化学性质。它提供了从头计算（Ab Initio）、密度泛函理论（DFT）以及半经验方法等多种计算方法，能够处理从小分子到大分子体系的各种问题。

ORCA 的特点包括：

- **多功能性**：支持多种量子化学方法，包括 HF、DFT、MP2、CI、CCSD 等。
- **易用性**：提供简洁的输入文件格式和丰富的文档支持。
- **高效性**：优化的并行计算能力，适合大规模计算任务。
- **免费使用**：对学术用户免费，但不开源。

\2. **编译环境安装**

2.1 **更新软件包列表** 

打开终端，更新软件包列表，以确保安装的是最新版本的软件

```C#
# 更新软件包列表
sudo apt update```

2.2 **安装编译环境**

```<p>**gcc**：是 GNU 编译器集合，用于编译 C 程序。</p><p>**gfortran**： 是 GNU Fortran 编译器，用于编译 Fortran 程序。</p><p>**g++**：是 C++ 编译器（g++）</p>```


```C#
# 安装 gcc
sudo apt install gcc

# 安装 gfortran
sudo apt install gfortran

# 安装 g++
sudo apt install build-essential g++ cpp```

2.3 **验证编译环境是否安装成功**

```C#
# 验证 gcc 是否安装成功
gcc --version

# 验证 gfortran 是否安装成功
gfortran --version

# 验证 g++ 是否安装成功
g++ --version```

\3. **OpenMPI 下载与安装**

3.1 **下载 OpenMPI 4.1.6**

```C#
# 下载 OpenMPI 4.1.6 源码
wget https://download.open-mpi.org/release/open-mpi/v4.1/openmpi-4.1.6.tar.gz```

3.2 **解压源码包**

```C#
# 解压 OpenMPI-4.1.6 源码包
tar -xzf openmpi-4.1.6.tar.gz

# 进入解压后的源码包
cd openmpi-4.1.6```

3.3 **配置编译选项**

```C#
# 配置编译选项,/home/lhc/请换成自己的地址
./configure --prefix=/home/lhc/openmpi-4.1.6 --disable-builtin-atomics```
默认情况下，ORCA 会安装在根目录下的 /openmpi-4.1.6 目录中，此处安装在/home/lhc/ openmpi-4.1.6 目录中。

3.4 **编译并安装**

```C#
# 编译
make -j $(nproc)

# 安装
sudo make install```

3.5 **配置环境变量**

```C#
# 使用 vim 打开 .bashrc 文件
vim ~/.bashrc

# 打开仅阅读模式
O

# 进入编辑模式
i

# 将光标移至最后，输入下列代码
export PATH=$PATH:/home/lhc/openmpi-4.1.6/bin
export LD\_LIBRARY\_PATH=$LD\_LIBRARY\_PATH:/home/lhc/openmpi-4.1.6/lib

# 摁 esc 键退出编辑模式

# 强制保存并退出
:wq!

# 执行以下命令使配置生效
source ~/.bashrc```

3.6 **验证 OpenMPI-4.1.6 是否安装成功**

Ubuntu 系统中同时安装了多个 MPI 实现（如 MPICH 和 OpenMPI），可能会导致命令冲突，因此需要使用绝对路径来运行 mpiexec 命令

```C#
# 验证 OpenMPI-4.1.6 是否安装成功
/home/lhc/openmpi-4.1.6/bin/mpiexec -V```

\4. **安装 ORCA**

4.1 **安装包下载**

- 访问 ORCA 官方网站，注册一个新用户账号。
- 登录后进入论坛，点击页面上方的 Download 按钮，进入下载页面。
- 选择适合您系统的 Linux 版本的 ORCA 安装包。如果您已经安装了 OpenMPI 4.1.6，则应选择包含 openmpi416 字样的安装包（其他版本同理），例如 orca\_6\_0\_1\_linux\_x86-64\_shared\_openmpi416.run。

4.2 **安装 ORCA**

在终端中进入下载的文件所在的目录，然后执行以下命令以安装 ORCA

```C#
# 给 orca 安装包文件添加可执行权限，从而使其能够被直接运行。
chmod +x orca\_6\_0\_1\_linux\_x86-64\_shared\_openmpi416.run

# 直接运行 orca 安装包
./orca\_6\_0\_1\_linux\_x86-64\_shared\_openmpi416.run```

默认情况下，ORCA 会安装在根目录下的 /orca\_6\_0\_1 目录中，此处安装在/home/lhc/ orca\_6\_0\_1 目录中。

4.3 **配置环境变量**

```C#
# 使用 vim 打开 .bashrc 文件
vim ~/.bashrc

# 打开仅阅读模式
O

# 进入编辑模式
i

# 将光标移至最后，输入下列代码
export PATH=$PATH:/home/lhc/orca\_6\_0\_1
export LD\_LIBRARY\_PATH=$LD\_LIBRARY\_PATH:/home/lhc/orca\_6\_0\_1
alias orca='/home/lhc/orca\_6\_0\_1/orca'
    
# 摁 esc 键退出编辑模式

# 强制保存并退出
:wq!

# 执行以下命令使配置生效
source ~/.bashrc```

4.4 **使用 vim 创建 test.inp 文件**

1. 创建并编辑文件

```C#
# 使用 vim 创建 test.inp 文件
vim test.inp```


```C#
# 在打开的 vim 编辑器中，输入以下内容：
! BLYP D3 def2-TZVP def2/J noautostart miniprint nopop
\* xyz   0   1
C 0.0 0.0 0.0
O 0.0 0.0 1.13
\*```

2. 按下 Esc键，然后输入 :wq 保存并退出。

```C#
# 保存并退出
:wq```

4.5 **验证 ORCA 是否安装成功**

```C#
# 在终端中运行以下命令以测试 ORCA：
orca test.inp > test.out```

检查输出文件 test.out，如果最后有 "ORCA TERMINATED NORMALLY" 这一行，则说明安装成功。

\5. **参考资料**

量子化学程序ORCA的安装方法：<http://sobereva.com/451>

