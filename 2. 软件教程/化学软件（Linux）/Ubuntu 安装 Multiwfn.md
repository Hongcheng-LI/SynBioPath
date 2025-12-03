
**Ubuntu 安装 Multiwfn**

\1. **Multiwfn 简介**

Multiwfn 是一款功能强大的量子化学波函数分析工具，由卢天博士开发，自 2009 年首次发布以来，已成为波函数分析领域的重要工具。该程序旨在提供一个功能全面、易于使用且完全开源免费的波函数分析平台，帮助量子化学研究者从电子波函数中提取丰富的化学信息。

1.1 **核心功能**

- **波函数分析**：Multiwfn 能够对量子化学计算得到的波函数进行深入分析，揭示体系的电子结构特征，如成键类型和强度、电荷分布、电子离域性等。它支持多种分析方法，包括但不限于 ADCH 原子电荷、拉普拉斯键级、范德华势等。
- **电子激发分析**：Multiwfn 提供了丰富的电子激发分析功能，如轨道成分分析、轨道重叠程度和质心距离的计算等。这些功能有助于研究电子激发过程中的电荷转移和能量转换机制。
- **几何操作与结构处理**：Multiwfn 不仅是一个波函数分析工具，还具备强大的几何操作功能。它可以对分子或晶体结构进行平移、旋转、镜像反转等操作，支持多种文件格式的导入和导出。例如，用户可以轻松地将分子的某个键平行于某个笛卡尔轴，或者将被晶胞截断的分子恢复完整。
- **静电势计算**：Multiwfn 能够高效地计算静电势，其内部代码经过优化后，计算速度大幅提升。

1.2  **应用场景**

- **化学键分析**：通过波函数分析，研究分子中的化学键类型和强度，揭示成键的本质。
- **电子结构研究**：分析电子分布、电荷转移等，帮助理解分子的电子结构特征。
- **分子间相互作用**：研究分子间弱相互作用，如氢键、范德华力等。
- **电子激发特性**：分析电子激发过程中的轨道贡献和电荷转移情况。

1.3  **开发与支持**

- **开发者**：卢天博士。
- **主页**：<http://sobereva.com/multiwfn>
- **交流平台**：拥有中文和英文论坛，方便用户交流和学习。
- **培训与支持**：开发者定期举办培训班，帮助用户快速掌握程序的使用。

1.4 **特点与优势**

- **功能全面**：集成了多种波函数分析方法和几何操作功能。
- **开源免费**：对学术领域用户永久免费，代码开源。
- **易用性高**：提供详细的用户手册和丰富的在线教程。
- **广泛认可**：被全球 90 多个国家的研究者使用，相关文章被广泛引用。

总之，Multiwfn 是一个功能强大且易于使用的波函数分析工具，适用于量子化学研究的多个方面，能够帮助研究者深入理解化学体系的内在特征。

\2. **Multiwfn 安装**

1. 安装 motif 和 libgl1 库

```C#
#安装 motif 库
sudo apt-get install libxm4

#安装 libgl1 库
sudo apt-get install libgl1```

2. 检查 SysV 共享内存段

```C#
# 检查 SysV 共享内存段，输出数值的单位为字节
cat /proc/sys/kernel/shmmax```
若内存过小，比如 32MB，在做一些较耗内存的分析时会崩溃，因此需要增大内存

3. 增大共享内存，打开 **/etc/sysctl.conf** 文件，加入下列内容

```C#
# 增大共享内存为 2GB
kernel.shmmax = 2000000000```

4. 打开官网：<http://sobereva.com/multiwfn/>，下载 Multiwfn 的 Linux 版本，此处为 **Multiwfn\_3.8\_dev\_linux.zip**。

![...](..\..\0.%20软件教程\化学软件（Linux）\images\Ubuntu%20安装%20Multiwfn.001.png)

Linux 系统的 Multiwfn 有两个版本，一个是 Linux 64bit，一个是 Linux 64bit noGUI version。具体区别见参考资料（[Multiwfn在Linux下安装的中文说明](http://sobereva.com/688)），此处安装的版本是 Linux 64bit 版本，即带有 GUI 图形界面的版本。

5. 将下载好的安装包 **Multiwfn\_3.8\_dev\_linux.zip** 放在 **/home/lhc/** 目录下，打开终端，输入下列命令解压文件。

```C#
# 解压文件
unzip Multiwfn\_3.8\_dev\_linux.zip```
解压后的目录是 **/home/lhc/Multiwfn\_3.8\_bin\_Linux**，文件夹中包含各种文件。

6. 配置环境变量

```C#
# 使用 vim 打开 .bashrc 文件
vim ~/.bashrc

# 打开仅阅读模式
O

# 进入编辑模式
i

# 将光标移至最后，输入下列代码
ulimit -s unlimited
export OMP\_STACKSIZE=200M
export Multiwfnpath=/home/lhc/Multiwfn\_3.8\_bin\_Linux
export PATH=$PATH:/home/lhc/Multiwfn\_3.8\_bin\_Linux

# 摁 esc 键退出编辑模式

# 强制保存并退出
:wq!

# 执行以下命令使配置生效
source ~/.bashrc```

7. 增加可执行权限

Multiwfn 的普通版的可执行文件是 Multiwfn 目录下的 Multiwfn。打开 **/home/lhc/Multiwfn\_3.8\_bin\_Linux/** 文件夹中打开终端

```C#
# 增加可执行权限
chmod +x /home/lhc/Multiwfn\_3.8\_bin\_Linux/Multiwfn```

8. 配置settings.ini

进入 **/home/lhc/Multiwfn\_3.8\_bin\_Linux/** 目录下，打开终端

```C#
# 使用 vim 打开 settings.ini 文件
vim settings.ini

# 进入编辑模式
i

# 找到 nthreads，将值改为 CPU 的物理核心数
nthreads = 12

# 找到 formchkpath，改为 Gaussian 目录下 formchk 程序的实际路径
formchkpath = "/home/lhc/g16/formchk"

# 找到 orca\_2mklpath，改为 ORCA 目录下的 orca\_2mkl 可执行文件的路径
orca\_2mklpath = "/home/lhc/ocra\_6\_0\_1\_avx2/orca\_2mkl"

# 找到 gaupath，改为 Gaussian 的可执行文件的路径
gaupath = "/home/lhc/g16/g16"

# 找到 ocrapath，改为 ORCA 的可执行文件的路径
ocrapath = "/home/lhc/ocra\_6\_0\_1\_avx2/orca"

# 摁 esc 键退出编辑模式

# 强制保存并退出
:wq!```


9. 测试

关闭终端，进入 **/home/lhc/Multiwfn\_3.8\_bin\_Linux/** 目录下，打开终端

```C#
# 打开 Multiwfn 软件
Multiwfn

# 载入 Multiwfn 程序包自带的 examples 目录下的 CH3CONH2.fch 文件
examples/CH3CONH2.fch

# 输入数字，回车
9

# 输入数字，回车
8

# 屏幕上马上就会输出拉普拉斯键级```
此时证明软件已安装成功。

\3. **参考资料**

[Multiwfn在Linux下安装的中文说明](http://sobereva.com/688)

