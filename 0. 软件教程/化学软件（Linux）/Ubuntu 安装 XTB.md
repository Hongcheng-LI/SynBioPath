
**Ubuntu 安装 XTB**

\1. **xTB 简介**

xTB（Extended Tight Binding）是一个基于紧束缚方法的量子化学程序，常用于计算分子和材料的电子结构。它以高效性和准确性著称，广泛应用于化学、材料科学和纳米技术等领域。xTB 是 ORCA 的一个扩展模块，也可以作为独立程序使用。

\2. **xTB 安装**

1. 进入 github 网站：<https://github.com/grimme-lab/xtb/releases>，下载合适的版本号

```C#
# 下载 xTB-6.7.1 版本
wget https://github.com/grimme-lab/xtb/releases/download/v6.7.1/xtb-6.7.1-linux-x86\_64.tar.xz```

2. 解压文件

```C#
# 解压文件
tar -xJf xtb-6.7.1-linux.x86\_64.tar.xz```

3. 将解压后的文件夹移动到一个合适的位置，例如 /home/lhc/xTB

4：配置环境变量

```C#
# 使用 vim 打开 .bashrc 文件
vim ~/.bashrc

# 打开仅阅读模式
O

# 进入编辑模式
i

# 将光标移至最后，输入下列代码
export PATH=$PATH:/home/lhc/xTB/xtb-dist/bin
export XTBPATH=/home/lhc/xTB/xtb-dist/share/xtb
export OMP\_NUM\_THREADS=12
export MKL\_NUM\_THREADS=12
export OMP\_STACKSIZE=1000M
ulimit -s unlimited

# 摁 esc 键退出编辑模式

# 强制保存并退出
:wq!

# 执行以下命令使配置生效
source ~/.bashrc```
其中 N 是并行计算时使用的 CPU 核心数，不要超过 CPU 的物理核心数。

5. 验证安装

```C#
# 检查 xTB 是否安装成功
xtb --version```

\3. **参考资料**

[将 Gaussian 与 Grimme 的 xtb 程序联用搜索过渡态、产生 IRC、做振动分析](http://bbs.keinsci.com/thread-10106-1-1.html)

