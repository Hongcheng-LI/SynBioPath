
**AutoDock vina 安装及使用教程**

```本教程参考自下列视频```
**[该类型的内容暂不支持下载]**

\1. **AutoDock vina 简介**

` `AutoDock Vina 是一种用于分子对接的开源软件工具，旨在帮助研究人员预测小分子配体与大分子受体（如蛋白质）之间的结合模式。它是 AutoDock 系列工具的一部分，由 Scripps Research 开发。

AutoDock 和 AutoDock Vina 都是用于分子对接的软件，但它们在性能、易用性和功能方面有一些显著的区别。以下是 AutoDock Vina 相对于 AutoDock 的几个主要优点：

1. **更快的计算速度**

```AutoDock Vina 通常比 AutoDock 更快。这是因为 Vina 采用了更先进的优化算法和多线程处理技术，可以更高效地搜索配体和受体之间的最佳结合方式。在多核处理器上，Vina 可以显著提高计算速度。```
2. **改进的对接精度**

```AutoDock Vina 在对接精度上有所改进。它使用了改进的评分函数，更好地评估和预测配体与受体之间的结合模式。这个改进使得 Vina 在许多情况下能够提供更准确的对接结果。```
3. **更简单的用户界面和配置**

```AutoDock Vina 的配置文件（配置参数）更简洁，更易于设置和使用。例如，Vina 的配置文件不需要用户指定详细的原子类型和参数，简化了使用流程。以下是一个 Vina 的简单配置文件示例：```


```Markdown
receptor = receptor.pdbqt
ligand = ligand.pdbqt
center\_x = 0
center\_y = 0
center\_z = 0
size\_x = 20
size\_y = 20
size\_z = 20```
4. **自动化处理多次对接**

```AutoDock Vina 可以自动执行多次对接计算，并返回多个可能的对接构象（poses）。用户不需要手动设置多个运行参数，简化了对多个构象的分析和选择过程。```
5. **多平台支持**

```AutoDock Vina 支持 Windows、Mac 和 Linux 等多种操作系统，用户可以在不同平台上进行对接计算。而且，它的安装和运行过程相对简单，不需要复杂的依赖库配置。```
6. **更好的多核支持**

```AutoDock Vina 内置了多线程支持，可以充分利用现代处理器的多核优势，从而显著提高计算速度。而 AutoDock 的多线程支持则较为有限。```
7. **社区支持和更新**

```由于 AutoDock Vina 是 AutoDock 的后续版本，并且由同一个开发团队维护，它通常会得到更多的社区支持和更新。用户可以从不断更新的软件版本和更丰富的资源中受益。```
8. **总结**

```<p>AutoDock Vina 在速度、精度、易用性和多平台支持等方面相对于 AutoDock 具有显著的优势。这些改进使得 Vina 在许多分子对接研究中成为更受欢迎的选择。</p><p>然而，需要注意的是，AutoDock Vina 并不适用于所有情况。例如，对于某些特定的对接任务，AutoDock 的结果可能更好。因此，用户应根据具体的研究需求选择适合的软件工具。</p>```

\2. **安装教程**

2.1 **AutoDock vina 1.2.5 安装**

1：进入下列网址，下载最新版本的 AutoDock vina 安装包，当前最新版本为 1.2.5。

<https://github.com/ccsb-scripps/AutoDock-Vina/releases>

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.001.png)

此处需要下载两个安装包，分别是 **vina\_1.2.5\_win.exe** 和 **vina\_split\_1.2.5\_win.exe** 两个安装包。

2：下载完成后，将两个安装包放置在一个文件夹内，本教程放置的文件夹目录为：

F:\Software\Address\AutoDock\_vina

3：按 Win+R，输入 cmd 进入命令行窗口，由于安装包放置在 F 盘，而 cmd 默认的工作目录为 C 盘，因此首先要将工作目录从 C 盘切换为 F 盘。


```Markdown
#将工作目录从 C 盘切换至 F 盘
F:

#进入 AutoDock vina 安装包所在的文件夹
cd F:\Software\Address\AutoDock\_vina

#验证当前版本的 AutoDock vina 是否可用
.\vina\_1.2.5\_win.exe```

若出现如下界面，则证明当前版本的 AutoDock vina 是可用的

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.002.png)

2.2 **MGLTools 1.5.7 安装**

在使用 AutoDock vina 进行分子对接之前，需要通过分子对接图形化软件 MGLTools 软件对目标蛋白和小分子进行相应的处理，因此需要安装该软件。

1. 进入下列网址，下载最新版本的 MGLTools 1.5.7 安装包，当前最新版本为 1.5.7。

<https://ccsb.scripps.edu/mgltools/downloads/>

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.003.png)

2. 双击安装包 **mgltools\_win32\_1.5.7\_Setup.exe**，安装 MGLTools。安装完成后，会在桌面上生成相应的快捷方式。打开后，软件界面如图所示。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.004.png)

2.3 **设置工作目录**

1. 在 F 盘内新建一个文件夹 **Molecular\_docking**，用作分子对接的默认工作目录。

```注意：工作目录文件夹中不要含有空格，否则后期运行会出错。```

2. 将 AutoDock vina 安装目录内的 **vina\_1.2.5\_win.exe** 复制到 **Molecular\_docking** 文件夹中

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.005.png)

3. 将 MGLTools 安装目录中的 **adt.bat** 复制到 **Molecular\_docking** 文件夹中。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.005.png)

4. 打开 AutoDock Tools，点击 **菜单窗口** 中的 **File** -> **Preference** -> **set**，即可弹出设置窗口。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.006.png)

5. 在弹出的窗口中，将 **Molecular\_docking** 文件夹的地址输入到  **Startup Directory**  栏中，并点击 make Default，即可完成修改默认工作目录。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.007.png)

\3. **使用教程**

本教程所用的蛋白和小分子为 **hsg1** 和 **ind**。

3.1 **导入蛋白结构**

1. 下载蛋白和小分子文件

[准备蛋白和小分子结构文件](准备蛋白和小分子结构文件.md)

2. 将需要对接的蛋白和小分子文件的 pdb 文件复制到默认的工作目录中，此处即复制到 **Molecular\_docking** 文件夹中。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.005.png)

3. 导入蛋白结构。点击 **菜单窗口** 中的 **File** -> **read molecular**。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.004.png)

在弹出的窗口中选中 **hsg1.pdb** 文件，并选择打开。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.008.png)

打开后，界面如图所示。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.009.png)

3.2 **对蛋白结构进行预处理**

3.2.1 **除水**

点击 **菜单窗口** 中的 **Edit** -> **delete water**，即可完成除水操作。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.008.png)

3.2.2 **加氢**

点击 **菜单窗口** 中的 **Edit** -> **Hydrogens** -> **add**。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.008.png)

在弹出的窗口中选择 **all Hydrogens**，即可完成加氢操作。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.008.png)

3.2.3 **将蛋白设为受体**

点击**菜单窗口**中的**Grid** -> **Macromolecular** -> **choose**。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.009.png)

在弹出的窗口中选中蛋白结构文件 **hsg1.pdb**，再点击 **select molecular**。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.008.png)

点击 ok，对蛋白进行初始化，即可将蛋白设为受体。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.008.png)

此时，会在默认工作目录中生成一个名为 **hsg1.pdbqt** 的 pdbqt 格式的文件，此时选择保存即可。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.008.png)

4. 在左侧路径中，鼠标右键点击 **hsg1** 文件，点击 **delete**。在当前窗口中删除该文件。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.008.png)

3.3 **导入小分子文件**

1. 点击**菜单窗口**中的**File** -> **read molecular**。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.004.png)

2. 在弹出的窗口中选中 **ind.pdb** 文件，并选择打开。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.008.png)

3. 打开后，界面如图所示。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.008.png)

3.4 **对小分子进行预处理**

3.4.1 **加氢**

1. 点击**菜单窗口**中的**Edit** -> **Hydrogens** -> **add**

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.008.png)

2. 在弹出的窗口中选择 **all Hydrogens**，即可完成加氢操作。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.008.png)

3.4.2 **将小分子设为配体**

1. 点击**菜单窗口**中的**Ligand** -> **Input** -> **choose**。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.009.png)

2. 在弹出的窗口中选中小分子结构文件 **ind.pdb**，再点击 **select molecule for AutoDock4**。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.009.png)

3. 点击 ok，对小分子结构进行初始化，即可将小分子设为配体。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.009.png)

3.4.3 **检测扭转中心及扭转键**

1. 点击**菜单窗口**中的**Ligand** -> **Torsion tree** -> **choose root**。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.006.png)

2. 点击**菜单窗口**中的**Ligand** -> **Torsion tree** -> **choose torsion**。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.009.png)

3. 此时，化合物变成了红绿两种颜色，红色的键代表不可旋转，绿色的键代表可以旋转。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.008.png)

4. 在弹出的窗口中显示，共有 14 根可以旋转的键，随后点击 **done**，即可完成操作。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.009.png)

3.4.4 **导出为 pdbqt 文件**

1. 点击**菜单窗口**中的**Ligand** -> **Output** -> **Save as PDBQT**。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.008.png)

2. 此时，会在默认工作目录中生成一个名为 **ind.pdbqt** 的 pdbqt 格式的文件，此时选择保存即可。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.009.png)

3. 在左侧路径中，鼠标右键点击 **ind** 文件，点击 **delete**。在当前窗口中删除该文件。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.008.png)

3.5 **设置对接参数**

3.5.1 **打开蛋白分子的 pdbqt 文件**

1. 点击**菜单窗口**中的**Grid** -> **Macromolecular** -> **open**。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.009.png)

2. 在弹出的窗口中打开刚刚保存的蛋白 pdbqt文件 **hsg1.pdbqt**。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.006.png)

3. 在弹出的窗口中点击 **yes**。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.009.png)

4. 在弹出的窗口中点击 **确定**。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.009.png)

3.5.2 **打开小分子的 pdbqt 文件**

1. 点击**菜单窗口**中的**Grid** -> **Set Map Types** -> **open Ligand**。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.008.png)

2. 在弹出的窗口中打开刚刚保存的小分子 pdbqt文件 **ind.pdbqt**。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.006.png)

3.5.3 **更改蛋白和小分子的显示形状**

1. 为了更直接的显示蛋白和小分子的结构，将蛋白和小分子分别改为下方两种类型。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.004.png)

3.5.4 **设置对接 box**

1. 点击**菜单窗口**中的**Grid**-> **Grid box**。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.009.png)

2. 此时，在蛋白中出现了一个 40\*40\*40 的立方体盒子。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.009.png)

3. 大家接下来要做的是调整盒子的大小，使其完整包裹住整个蛋白质，如果大家知道该蛋白的活性位点，可以仅包裹活性位点即可。盒子越大，对接速度越慢，盒子越小，对接速度越快。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.010.png)

3.5.5 **显示出小分子**

1. 此时，小分子已经被蛋白包裹住了，需要将小分子给显示出来。

2. 点击**菜单窗口**中的**DejaVu GUI**按钮。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.008.png)

3. 在弹出的窗口中取消勾选 **mouse transforms apply to "root" object only**，或者是点击 **Preference** -> **Transf. Root Only**，二者效果相同。

```![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.011.png)|![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.011.png)``` :- |

4. 选中 **ind** 小分子文件，点击鼠标右键向右移动，即可将小分子拖出。

```![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.011.png)|![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.011.png)``` :- |

5. 将小分子拖拽出来之后，再将**mouse transforms apply to "root" object only**勾选上，然后关闭窗口，即可完成操作。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.008.png)

6. 点击窗口中的 **Close saving current**，即可完成操作

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.004.png)

3.6 **设置 AutoDock vina 参数**

3.6.1 **确认受体与配体是否正确**

1. 点击**菜单窗口**中的**Docking** -> **Output**-> **Vina Config (Config.txt)**。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.010.png)



2. 在弹出的窗口中，首先确认 Receptor 与 Ligand 的名字是否与自己的目标蛋白和小分子名字一致。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.009.png)

3. 若是不一致，可以点击红框中的 **browse** 进行替换为正确的 Receptor 与 Ligand。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.006.png)

3.6.2 **重要参数**

1. **Out** 和 **Out filename** 是对接结束后输出的文件类型和名字。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.009.png)

2. 点击窗口中的 **Show options**，在新显示的参数中有一个 **mode**，代表着对接次数，默认是 9 次，此处将其修改为 10 次。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.006.png)

3. 打开默认的工作目录，发现新生成了一个名为 **config.txt** 的文件。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.005.png)

4. 打开 **config.txt** 文件，可以看到 receptor，ligand，盒子的中心位置，以及放大的倍数等对接的参数。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.012.png)

5. 下图为对接 **对接 box 参数** 与 **config.txt** 中结果的说明比较

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.013.png)

3.7 **进行分子对接**

3.7.1 **运行 AutoDock vina 进行对接**

1. 点击**菜单窗口**中的**Run** -> **Run AutoDock Vina**。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.004.png)

2. 在弹出的窗口中，若 **config filename** 一栏为空白，点击 **Browse**。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.008.png)

3. 在刚弹出的窗口中，选中刚生成的 **config.txt** 文件即可。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.008.png)

4. 更新完 **config.txt** 文件之后，还需要确认 **Vina Program Pathname** 是否正确，若不正确，则需要修正为正确的vina 安装路径，此处修改为 **F:/Software/Address/AutoDock\_vina/vina\_1.2.5\_win.exe**。确认无误后，点击 **Launch**，开始进行对接。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.007.png)

5. 在开始对接之后，会弹出一个窗口，不需要管它，等待它自己消失即可。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.008.png)

3.7.2 **查看对接结果**

1. 对接工作结束后，在命令行窗口中会给出下列结果，表明对接了九次，结果按照结合能（affinity）的绝对值由大到小排列。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.014.png)

2. 此时，在默认工作目录中，新生成了一个 **result.pdbqt** 文件

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.005.png)

3. 点击**菜单窗口**中的**Edit** -> **Delete**-> **Delete All Molecules**，删除显示面板中所有的分子。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.009.png)

4. 接下来通过 AutoDock Tool 查看分子对接结果。点击**菜单窗口**中的**Analyze** -> **Dockings**-> **Open AutoDock vina results**，查看分子对接结果。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.009.png)

5. 在弹出的窗口中，选择 **Single molecule with mutipule conformations**，点击 **ok**。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.015.png)

6. 在弹出的窗口中提示，可以通过使用键盘上的方向键来查看九种不同构象的对接结果。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.004.png)

7. 点击**菜单窗口**中的**Analyze** -> **Macromolecule**-> **Open**

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.009.png)

8. 在弹出的窗口中，选择 **hsg1.pdbqt** 文件，在对接结果中加入蛋白结构，以便更直观的分析对接结果。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.009.png)

9. 为了便于观察，将蛋白结构和小分子分别设置成不同的展示形式。通过点击键盘上的左右方向键，可以查看不同构象的对接结果。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.009.png)

3.7.3 **查看相互作用**

1. 点击**菜单窗口**中的**Analyze** -> **Dockings**-> **Show interactions**，查看相互作用。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.016.png)

2. 此时，会弹出两个新的窗口，一个用于展示结合位点处的相互作用，一个用于展示是否存在氢键。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.008.png)

3. 在 **Binding Site Interaction display options** 中，依次点击 **display pi-pi interactions** 和 **display pi-cation interactions**，结果提示不存在 pi-pi 相互作用，存在 pi-cation 相互作用。当切换不同构象的对接结果时，发现有时候两种相互作用均不存在。结果表明不同构象的对接结果会有不同的作用力。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.004.png)

4. 在 **Show Hydrogen Bonds as Spheres** 窗口中，提示在当前构象下，小分子与 hsg1 蛋白 B 链中 29 位 Asp 氨基酸中的氨基氢存在氢键作用。若没有**Show Hydrogen Bonds as Spheres** 窗口，则证明在该构象下，不存在氢键作用。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.009.png)

\4. **用一条命令行来运行 AutoDock vina**

1. 在使用 AutoDock vina 准备好 config.txt，hsg1.pdbqt，ind.pdbqt 文件后，可以考虑使用命令行来运行 vina 进行分子对接。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.017.png)

2. 在默认工作目录的地址栏中输入 **cmd**，即可弹出命令行窗口。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.018.png)

3. 在命令行窗口中输入下列代码，即可查看该软件对应的各种参数。

```Markdown
#查看 AutoDock vina 的各种参数
vina\_1.2.5\_win```
![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.019.png)

4. 在命令行窗口中输入下列代码，即可运行 AutoDock vina 进行分子对接。

```Markdown
#运行 AutoDock vina 进行分子对接
vina\_1.2.5\_win --config config.txt```

5. 运行结束后，可以发现，跟使用软件运行分子对接的结果一样，也生成了九种不同构象的对接结果。分析方式可以参考使用软件分析的步骤。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.020.png)

\5. **使用 PyMOL 输出蛋白小分子复合物的对接结果**

5.1 **AutoDock vina 将对接结果保存为 pdb 格式**

1. 点击**菜单窗口**中的**Analyze** -> **Dockings**-> **Open AutoDock vina results**，选中刚刚生成的 **result.pdbqt** 文件，查看分子对接结果。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.009.png)

2. 在弹出的窗口中，选择 **Single molecule with mutipule conformations**，点击 **ok**。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.015.png)

3. 在弹出的窗口中提示，可以通过使用键盘上的方向键来查看九种不同构象的对接结果。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.004.png)

4. 在结合能为 -11.479 的对接结果中，点击**菜单窗口**中的**File** -> **Save**-> **Write PDB**，将该构象下的对接结果保存为 PDB 格式文件。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.009.png)

5. 在弹出的窗口中，将文件保存路径改为默认工作路径，即 **F:\Molecular\_docking**，文件名仍为 **result.pdb**。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.008.png)

5.2 **PyMOL 生成蛋白小分子复合物文件**

1. 进入默认的工作路径，双击刚生成的 **result.pdb** 文件，即可用 PyMOL 查看对接结果。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.005.png)

2. 点击**菜单窗口**中的**File** -> **open**。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.021.png)

3. 在弹出的窗口中，选中 **hsg1.pdb** 文件，点击**确认**，即可用 PyMOL 查看蛋白结构。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.022.png)

4. 此时，同时打开了小分子和蛋白结构。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.023.png)

5. 在将文件保存为蛋白小分子复合物之前，需要对蛋白进行去水操作。在对象列表窗口中 **hsg1** 处点击 **A** -> **remove waters**，即可对蛋白质完成去水操作。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.024.png)

6. 点击**菜单窗口**中的**File** -> **Export Molecule**。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.022.png)

7. 在弹出的窗口中，同时选中 **result** 和 **hsg1**，并选择 **one file**，点击 **ok** 即可生成蛋白-小分子复合物文件，将文件命名为 **complex.pdb**，保存至默认工作路径。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.022.png)

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.021.png)

8. 生成蛋白小分子复合物文件之后，在对象列表窗口中 **All** 处点击 **A** -> **delete everything**，即可 删除当前所有的对象文件。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.022.png)

5.3 **PyMOL 对蛋白小分子复合物文件进行处理**

1. 点击**菜单窗口**中的**File** -> **Open**。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.023.png)

2. 在弹出的窗口中，选择刚生成的 **complex.pdb** 文件，并点击**确定**，即可打开蛋白小分子复合物文件。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.021.png)

3. 选中小分子结构，在对象列表窗口中 **sele** 处点击 **H** -> **valence**，即可隐藏小分子中可见的键价（valence）表示。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.025.png)

4. 选中小分子结构，在对象列表窗口中 **sele** 处点击 **H** -> **Hydrogen**-> **all**，即可隐藏小分子中所有的氢原子。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.022.png)

5. 选中小分子结构，在对象列表窗口中 **sele** 处点击 **A** -> **Find** -> **polar contacts** -> **to other atoms in object**，即可显示小分子与蛋白之间的氢键作用。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.021.png)

6. 图中的黄色虚线即为氢键作用

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.026.png)

\6. **AutoDock 与 AutoDock vina 的区别**

```|**AutoDock vina**|**AutoDock**``` :-: | :-: |
|工作路径内的文件|vina.exe|adt.bat; autogrid4; autodock4|
|直到哪一步之前的操作是相同的|grid box|grid box|
|不同的步骤|<p>Docking->output->vina config</p><p>Analyze->dockings->vina results</p>|输出 gpf 文件，设置更多的对接参数与算法|
|参数文件|config.txt|grid.gpf; dock.dpf|
|结果文件格式|result.pdbqt|xx.glg; xx.dlg; complex.pdbqt 以及一堆 map 文件|
|结果文件中的分子|只有小分子，但有多个构象，代表了多次对接|复合物，既有小分子，又有大分子，但是只有一次构象。|
|运算速度|快|慢|

\7. **仔细检查是否生成氢键**

7.1 **打开对接结果**

1. 点击**菜单窗口**中的**Analyze** -> **Dockings**-> **Open AutoDock vina results**，选中刚刚生成的 **result.pdbqt** 文件，查看分子对接结果。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.009.png)

2. 在弹出的窗口中，选择 **Single molecule with mutipule conformations**，点击 **ok**。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.015.png)

3. 在弹出的窗口中提示，可以通过使用键盘上的方向键来查看九种不同构象的对接结果。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.004.png)

7.2 **添加蛋白分子**

1. 点击**菜单窗口**中的**Analyze** -> **Macromolecule**-> **Open**

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.009.png)

2. 在弹出的窗口中，选择 **hsg1.pdbqt** 文件，在对接结果中加入蛋白结构，以便更直观的分析对接结果。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.009.png)

7.3 **查看相互作用**

1. 点击**菜单窗口**中的**Analyze** -> **Dockings**-> **Show interactions**，查看相互作用。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.016.png)

2. 此时，可以看到，在结合能为 -9.877 的对接结果中，仅弹出一个窗口，用于展示结合位点处的相互作用。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.008.png)

3. 此时，取消展示蛋白的各种表现形式，并取消勾选 **display msms** 和 **close contact**。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.016.png)

4. 最后，勾选 **hydrogen bonds**，但是无任何变化，表明该构象下的对接结果中不存在氢键。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.006.png)

5. 当用键盘上的方向键切换不同构象下的对接结果时，发现有的构象会弹出氢键的结果，并在小分子周围出现两个网状球，表明存在氢键作用。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.008.png)

\8. **用 PyMOL 计算配体的 RMSD**

8.1 **前期准备**

8.1.1  **所需要的文件**

- 某一次对接结果中某一构象的 pdb 文件或 pdbqt 文件。
- 这次对接中用到的小分子的 pdb 文件或 pdbqt 文件。

8.1.2 **注意事项**

- 不要直接拿结果文件（也就是包含多个构象的文件 result.pdbqt）拿去计算，需要单独导出某一构象的 pdb 或 pdbqt 文件。

8.1.3 **命令行**

```Markdown
#计算 RMSD 值
align x, y```

8.2 **计算步骤**

8.2.1 **AutoDock vina 打开对接结果**

1. 点击**菜单窗口**中的**Analyze** -> **Dockings**-> **Open AutoDock vina results**，选中刚刚生成的 **result.pdbqt**文件，查看分子对接结果。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.009.png)

2. 在弹出的窗口中，选择 **Single molecule with mutipule conformations**，点击 **ok**。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.015.png)

3. 在弹出的窗口中提示，可以通过使用键盘上的方向键来查看九种不同构象的对接结果。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.004.png)

8.2.2 **导出单一构象的 pdb 或 pdbqt 文件**

1. 在结合能为 -11.479 的对接结果中，点击**菜单窗口**中的**File** -> **Save**-> **Write PDB**，将该构象下的对接结果保存为 PDB 格式文件，文件名为 **1.pdb**。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.009.png)

2. 在结合能为 -11.479 的对接结果中，点击**菜单窗口**中的**File** -> **Save**-> **Write PDBQT**，将该构象下的对接结果保存为 PDBQT 格式文件，文件名为 **11.pdbqt**。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.008.png)

3. 通过摁键盘上的方向键，切换到结合能为 -10.307 的对接结果，点击**菜单窗口**中的**File** -> **Save**-> **Write PDB**，将该构象下的对接结果保存为 PDB 格式文件，文件名为 **2.pdb**。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.009.png)

4. 在结合能为 -10.307 的对接结果中，点击**菜单窗口**中的**File** -> **Save**-> **Write PDBQT**，将该构象下的对接结果保存为 PDBQT 格式文件，文件名为 **22.pdbqt**。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.009.png)

8.2.3 **PyMOL 计算 RMSD 值**

1. 在默认工作路径内，选中刚刚生成的 **1.pdb** 文件，点击红框内的 **PyMOL.exe**，打开 PyMOL 软件。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.017.png)

2. 点击**菜单窗口**中的**File** -> **open**。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.021.png)

3. 在弹出的窗口中，选中剩余的某一构象的 pdb 或 pdbqt 文件（**2.pdb**，**11.pdbqt**，**22.pdbqt**），以及用于对接的小分子的 pdb 文件（**ind.pdb**） 文件，点击**确认**即可。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.027.png)

4. 在 PyMOL 的命令行中输入下列命令，即可算出结合能为 -11.479 构象下的 RMSD 值为 0.191。

```Markdown
#计算 RMSD 值
align ind, 1```
![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.026.png)

5. 在 PyMOL 的命令行中输入下列命令，即可算出结合能为 -11.479 构象下的 RMSD 值为 0.191。说明使用 PDB 文件或 PDBQT 文件计算得到的 RMSD 值相同。

```Markdown
#计算 RMSD 值
align ind, 11```
![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.028.png)

\9. **使用 PyMOL 绘制其他作用力**

9.1 **AutoDock vina 查看相互作用**

9.1.1 **打开对接结果**

1. 接下来通过 AutoDock Tool 查看分子对接结果。点击**菜单窗口**中的**Analyze** -> **Dockings**-> **Open AutoDock vina results**，查看分子对接结果。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.009.png)

2. 在弹出的窗口中，选择 **Single molecule with mutipule conformations**，点击 **ok**。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.015.png)

3. 在弹出的窗口中提示，可以通过使用键盘上的方向键来查看九种不同构象的对接结果。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.004.png)

9.1.2 **添加蛋白分子**

1. 点击**菜单窗口**中的**Analyze** -> **Macromolecule**-> **Open**，

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.009.png)

2. 在弹出的窗口中，选择 **hsg1.pdbqt** 文件，在对接结果中加入蛋白结构，以便更直观的分析对接结果。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.009.png)

3. 为了便于观察，将蛋白结构和小分子分别设置成不同的展示形式。通过点击键盘上的左右方向键，可以查看不同构象的对接结果。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.009.png)

9.1.3 **查看相互作用**

1. 点击**菜单窗口**中的**Analyze** -> **Dockings**-> **Show interactions**，查看相互作用。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.016.png)

2. 此时，会弹出两个新的窗口，一个用于展示结合位点处的相互作用，一个用于展示是否存在氢键。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.008.png)

3. 在 **Binding Site Interaction display options** 中，依次点击 **display pi-pi interactions** 和 **display pi-cation interactions**，结果提示不存在 pi-pi 相互作用，存在 pi-cation 相互作用。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.004.png)

4. 为了进一步观察 pi-cation 相互作用，取消勾选 **display msms** 和 **close contact**。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.009.png)

5. 勾选 **display pi-cation interactions**，可以看到小分子与 8 位的 Arg 存在 pi-cation 相互作用。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.009.png)

6. 为了用 PyMOL 绘制 pi-cation 相互作用图，将该构象下的对接结果保存为 PDB 格式文件。在结合能为 -11.479 的对接结果中，点击**菜单窗口**中的**File** -> **Save**-> **Write PDB**

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.009.png)

7. 在弹出的窗口中，将文件保存路径改为默认工作路径，即 **F:\Molecular\_docking**，文件名仍为 **result.pdb**。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.008.png)

9.1.4 **PyMOL 生成蛋白小分子复合物文件**

1. 进入默认的工作路径，双击刚生成的 **result.pdb** 文件，即可用 PyMOL 查看对接结果。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.005.png)

2. 点击**菜单窗口**中的**File** -> **open**。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.021.png)

3. 在弹出的窗口中，选中 **hsg1.pdb** 文件，点击**确认**，即可用 PyMOL 查看蛋白结构。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.022.png)

4. 此时，同时打开了小分子和蛋白结构。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.023.png)

5. 在将文件保存为蛋白小分子复合物之前，需要对蛋白进行去水操作。在对象列表窗口中 **hsg1** 处点击 **A** -> **remove waters**，即可对蛋白质完成去水操作。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.024.png)

6. 点击**菜单窗口**中的**File** -> **Export Molecule**。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.022.png)

7. 在弹出的窗口中，同时选中 **result** 和 **hsg1**，并选择 **one file**，点击 **ok** 即可生成蛋白-小分子复合物文件，将文件命名为 **complex.pdb**，保存至默认工作路径。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.022.png)

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.021.png)

8. 生成蛋白小分子复合物文件之后，在对象列表窗口中 **All** 处点击 **A** -> **delete everything**，即可 删除当前所有的对象文件。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.022.png)

9.2 **PyMOL 修改作用力的颜色**

1. 点击**菜单窗口**中的**File** -> **Open**。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.023.png)

2. 在弹出的窗口中，选择刚生成的 **complex.pdb** 文件，并点击**确定**，即可打开蛋白小分子复合物文件。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.021.png)

3. 选中小分子结构，在对象列表窗口中 **sele** 处点击 **H** -> **valence**，即可隐藏小分子中可见的键价（valence）表示。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.025.png)

4. 选中小分子结构，在对象列表窗口中 **sele** 处点击 **H** -> **Hydrogen**-> **all**，即可隐藏小分子中所有的氢原子。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.022.png)

5. 选中小分子结构，在对象列表窗口中 **sele** 处点击 **A** -> **Rename selection**，将小分子命名为 ligand。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.026.png)

6. 点击红框处，将选择 **Residue**（残基）改为选择 **chain**（链）。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.023.png)

7. 选中蛋白的两条链，在对象列表窗口中 **sele** 处点击 **A** -> **Rename selection**，将蛋白命名为 protein。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.026.png)

8. 在对象列表窗口中 **ligand** 处点击 **A** -> **Find** -> **polar contacts** -> **to other atoms in object**，即可显示小分子与蛋白之间的氢键作用。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.028.png)

9. 点击红框处，将选择 **chain**（链）改为选择 **Residue**（残基）。并点击下方红框中的 **S**，使其显示氨基酸序列。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.027.png)

10. 图中的黄色虚线即为与其他原子的相互作用。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.023.png)

11. 为了改变红框中作用力的颜色，使其与其他作用力区分开来。首先选中蛋白中与小分子形成该作用力的残基，在对象列表窗口中 **Sele** 处点击 **S** -> **sticks**，即可显示该残基的结构。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.023.png)

12. 为便于区分，在对象列表窗口中 **Sele** 处点击 **C** -> **cyans** -> **cyan**，即可改变该残基的颜色。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.026.png)

13. 在菜单栏中点击 **Wizard** -> **Measurement**。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.023.png)

14. 先后点击红框中的 **1** 和 **2** 处，即可显示两个原子之间的距离为 1.9 埃。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.026.png)

15. 在对象列表窗口中 **measure01** 处点击 **C** -> **greens** -> **green**，即可改变该测量距离的颜色。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.028.png)

16. 此时颜色未发生改变，点击红框中的 **ligand\_polar\_contant** 两下，就会发现该处作用力的颜色已变为绿色，与其他作用力区分开来。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.023.png)

17. 点击红框中的 **done**，即可完成此次修改颜色的操作。

![...](..\..\..\0.%20软件教程\分子对接\AutoDock%20vina%20使用教程\images\AutoDock%20vina%20安装及使用教程.029.png)

