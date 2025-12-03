
**ACWB：自动化计算化学工作流程软件使用教程**

\1. **ACWB 简介**

在天然药物化学研究中，量子化学计算已经普遍用于未知化合物的结构解析和验证，但是由于有一定的门槛，这些技术成为了许多研究者的技术瓶颈。

本软件（Automatic Computation Workflow for Beginners，**ACWB**）用于有机化合物的构象搜索、量化软件输入文件生成（支持高斯 09/16 和 ORCA），计算任务的自动调度，以及数据处理。用于大批量化合物，以及多构象化合物的量化计算，可大大节约人工操作时间，简易的操作方法和规范化的计算参数文件可大幅减少用户工作量和上手门槛。

软件仅需要提供目标化合物的坐标文件（xyz），即可自动完成化合物的构象搜索，并根据用户预先设置的 protocol 文件生成高斯或 ORCA 的输入文件，并可自动根据用户设置顺序调度输入文件，无需用户干预。软件还提供数据处理模块，可自动筛查重复构象、去除含虚频构象及高能量构象，并自动计算能量，收集所需的目标参数，自动进行玻尔兹曼平均，输出为用户可直接操作的文件，包括数据文件、分子坐标文件、以及用于计算 ECD 的构象比例文件等。

\2. **运行环境**

因为基于 Anaconda 环境，原则上该软件可以跨平台运行，但由于调用的 CREST 软件只有 Linux 版本，因此目前主程序只能在 Linux 系统上使用。Conda 环境的基础包即可支持它的运行。量子化学计算的软件如高斯、ORCA 等需要用户提前安装并设置好环境变量。

1. [VMware安装Ubuntu](..\Linux 使用基础\VMware安装Ubuntu.md)
2. [Ubuntu系统安装 Conda](..\生物信息学工具（Linux）\Ubuntu系统安装 Conda.md)
3. [Ubuntu 安装 ORCA](Ubuntu 安装 ORCA.md)
4. [Ubuntu 安装 XTB](Ubuntu 安装 XTB.md)
5. [Ubuntu 安装 Crest](Ubuntu 安装 Crest.md)

```设置好 xTB 的环境变量后，将预编译的 Crest 程序直接复制到 xTB 的 bin 目录下即可。```
6. [Ubuntu 安装 Multiwfn](Ubuntu 安装 Multiwfn.md)
7. [Ubuntu 安装 Gaussian](Ubuntu 安装 Gaussian.md)

\3. **计算流程**

3.1 **生成 3D 结构**

用分子建模软件生成 3D 结构，然后保存成 xyz 文件

```**注意**：Chem3D 不支持直接生成 xyz 文件，可以先生成不含其他任何额外信息的 cc2 文件，再增加一个标题行并改 cc2 后缀为 xyz 文件即可。```

3.2 **构象搜索**

1. 使用 acwb.py 调用 CREST 和 xTB 进行构象搜索和 GFN2-xTB 级别的构象筛选。

2. 对于柔性分子均需要该步骤，即便是部分刚性环结构也不要忽略，以免一些初始结构较差，导致构象不正确。如果计算的化合物或者类似化合物有单晶结构，则从单晶结构出发进行建模。基于半经验方法 GFN2-xTB 的筛选能量窗口默认为 4 kcal/mol。

```<p>**注意**：</p><p>- 文件名和文件路径中不要有空格和中文，否则容易引起错误。</p><p>- 注意分子的净电荷和自旋多重度，如果净电荷不为 0 或者自旋多重度不为 1，需要自行在 protocol 文件中修改。</p><p>- ORCA 约定后缀 inp 和 log；Gaussian 约定后缀 gjf 和 out。</p>```

3.3 **预筛选**

1. acwb.py 根据筛选后的构象集合以及 protocol 文件，对构象集合进行拆分，生成 ORCA（.inp）或Gaussian（.gjf) 输入文件。

2. 对应 prescreen\_orca 中的 protocol 文件，该步骤仅用 r2scan-3c 方法进行结构优化而不进行频率计算，一方面 r2scan-3c 计算速度较快，精度较高，尤其相对于 B3LYP 这样的杂化泛函，在体系较大的时候优势更加明显；另一方面简化频率计算也可以大大降低计算时间。数据处理时可以使用较窄（2-3 kcal/mol）的能量窗口去掉高能量构象，从而大大降低构象数目。相较于使用半经验方法或者力场方法计算的能量来筛选构象，该方法要靠谱得多。如果不放心，可以进一步放大能量窗口。

```<p>**注意**：</p><p>文献中有很多人用力场方法计算的玻尔兹曼比例或能量来进行筛选，能量窗口设置很低，比如 5 kJ/mol，或去掉小于 5% 比例的构象。这种方法极其错误，几乎不可避免的导致漏掉重要构象。对于 MMFF 之类的力场方法，能量窗口要设置到 10 kcal/mol 以上才有可能包含大部分重要构象（仍然不是全部）。GFN2-xTB 筛选的能量窗口可以缩小到 4-6 kcal/mol，r2scan-3c 可以缩小到 2-4 kcal/mol。</p>```

3.4 **结构优化和频率计算**

1. 使用 run\_jobs.py 顺序执行输入文件。计算完毕后，收集 ORCA（.log）或 Gaussian（.out）的输出文件到同一个目录下，使用 data\_prcs.py 进行处理。

2. 使用步骤 3 处理得到 acwb\_cluster.xyz 文件和 opt\_freq 文件夹中 protocol 文件生成进行结构优化和频率计算的输入文件，比较推荐 opt\_freq\_orca 中的基于 r2scan-3c 的方法，对于大的结构速度优势明显。由于建立在较好的几何结构和减少的构象数目基础上，该步骤计算量会大大减少。这一步必不可少，可以得到热力学参数，计算 Gibbs 自由能，并且可以去掉带虚频的结构。

```<p>**注意**：</p><p>- 该步的 population.xlsx 和 Multiwfn.txt 文件是最终用来做玻尔兹曼平均的文件，非常重要。其他生成的文件如 acwb\_cluster.xyz、SI.txt、averaged\_NOE\_intensity.xlsx 也是最终有效的文件。</p><p>- run\_jobs.py 文件使用核数 = 输入文件中定义的并发数 \* 用户输入的并行输入文件数，使用核数不要超过机器物理核数。</p>```

3.5 **性质计算**

1. data\_prcs.py 会生成 acwb\_cluster.xyz、averaged\_NOE\_intensity.xlsx、population.xlsx、multiple.txt、SI.txt、averaged\_coupling\_constant.xlsx 等文件，用于后续处理。

2. 本步骤中得到的 acwb\_cluster.xyz 和具体某种性质如 ECD、碳谱计算的 protocol 生成输入文件，计算的过程中不再需要做结构优化和频率计算，也方便进行方法的尝试。特别是 ECD 计算，只需要尝试 ECD计算的步骤即可，使用本步骤中的 Multiwfn.txt 即可正确地进行玻尔兹曼平均，无需结构优化从而节省大量时间。

```**注意**：STS 方法除外，需要使用特定的结构优化方法，会稍微耗时一些，可以选择 no\_freq 的protocol。计算耦合常数或 NMR 进行玻尔兹曼平均时，使用步骤 3 中的 population.xlsx（将其与输出文件放到同一个文件夹中即可）中的能量进行平均。```

3.6 **后续处理 1**

使用 python acwb.py acwb\_cluster.xyz 即可直接拆分上一步计算的构象集合，根据 protocol 文件生成下一步的输入文件，用于分步计算。

3.7 **后续处理 2**

1. data\_prcs.py 处理输出文件时，使用 population.xlsx，则读取 population.xlsx 中的能量，而不使用输出文件中的能量进行玻尔兹曼平均。

```**注意**：除了 STS 之外，ACWB 不再推荐使用 Gaussian 和 ORCA 的自动分步计算。而是用acwb\_cluster.xyz 进行手动分步计算，用 population.xlsx 传递上一步的能量信息。```

\4. **实际操作**

```本教程以化合物 3-buten-2-ol 为例进行演示，CD 的测试溶剂为氯仿。```
4.1 **化合物 3D 文件生成**

4.1.1 **绘制 3D 结构**

1. 在 Chemdraw 中画好 3-buten-2-ol 的结构

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.001.png)

2. 选择 **view** --> **show ChemBio3D HotLink Window**

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.002.png)

3. 在弹出的 ChemBio3D 窗口中点击 **Launch Chem3D**，即可在 ChemBio3D 中打开。

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.003.png)

4. 下图即为化合物在 ChemBio3D 中的样式，此结构为软件自动生成，不代表正确。若结构中含有桥环结构，可能会存在一些不合理的地方，需要自己去检查纠正。

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.004.png)

4.1.2 **能量优化**

1. 对该结构进行能量优化，一般选择 MMFF94 方法，操作为 **calculation** --> **MMFF94** --> **perform MMFF94 minimization**，在弹出的窗口中，点击 **run** ，软件会自动进行能量优化。

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.004.png)

```<p>**注意：**    </p><p>- 当结构中含有吲哚环时，通过 MMFF94 能量最小化之后，吲哚结构中的五元环的键长和键角会变的与正常情况不一样。</p><p>- 当结构中含有糖时，糖环上的羟基理论上要处于平伏键，通过 MMFF94 能量最小化之后，有可能羟基处于直立键。</p><p>- 因此生成 Chem3D 结构之后，要仔细检查。</p>```

2. 优化结束后，将文件存为 cc2 格式。操作为 **File** --> **save copy as**。

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.005.png)

3. 在弹出的窗口中，文件格式选为：**Cart Coords 2 (\*.cc2)**。由于 cc2 格式的文件包含 connection 中的所有信息，因此 Connection 选择 missing，取消所有框的勾选。

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.006.png)

4.1.3 **cc2 文件转化为 xyz 文件**

用记事本打开 cc2 文件，第一行的 13 是指结构中的原子数，在 13 处输入回车即可保存并关闭文件。

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.007.png)

```<p>**注意：**    </p><p>- cc2 文件跟 xyz 文件的区别就在于 cc2 文件少了一个注释行，我们在 13 后面加上一个回车，文件就由 cc2 格式转变为 xyz 格式了。</p><p>- 将桌面上 3-buten-2-ol.cc2 文件的后缀名改为 3-buten-2-ol.xyz，此时用于计算的 3D 文件已经准备完毕。</p>```

4.2 **准备计算**

1. 将 **acwb\_1.1** 软件包放置在 **/home/lhc/** 目录下。

2. 在 **/home/lhc/** 目录下新建 **compounds** 文件夹，在此处存放化合物的 Chem3D 文件和执行计算工作。

3. 在 **/home/lhc/compounds/** 目录下新建 **01\_3-buten-2-ol** 文件夹，将第一步准备好的 **3-buten-2-ol.xyz** 文件放置在该目录下。

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.008.png)

4. 复制 **acwb\_1.1 软件包**中的 **acwb.py** 文件，将其放到 **/home/lhc/compounds/01\_3-buten-2-ol/** 目录中

5. 复制 **/home/lhc/acwb\_1.1/protocols/prescreen\_orca/** 目录下的的 **prescreen\_Chloroform.protocol** 文件，将其放到 **/home/lhc/compounds/01\_3-buten-2-ol/** 目录中

```<p>**注意：**    </p><p>该目录下共有 3 个文件，分别对应乙腈、氯仿、甲醇</p><p>用什么溶剂测 CD，就选择对应溶剂的文件。3-buten-2-ol 是用氯仿进行测试，因此选择prescreen\_Chloroform.protocol 文件。</p>```


4.3 **构象搜索**

1. 在 /home/lhc/compounds/01\_3-buten-2-ol/ 目录中打开终端，输入下列命令

```C#
#使用 python 运行 acwb.py 计算 3-buten-2-ol.xyz
python acwb.py 3-buten-2-ol.xyz```

2. 输出下列结果，可以看到搜索到了 8 个构象文件。

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.009.png)

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.010.png)

3. 此时在 **/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/** 目录中会生成一个以这个文件名 **3-buten-2-ol** 为命名的一个目录，并且在这个目录里面进行构象搜索。图中框起来的 8 个文件即为生成的构象文件，可以看到命名规则为 c1~c8。

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.011.png)

4.4 **预筛选**

4.4.1  **运行 run\_jobs.py**

1. 在 **/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol** 目录中新建一个名为 **pre\_opt** 的文件夹，将生成的 8 个构象文件移动到 **pre\_opt** 文件夹中。

2. 复制 **/home/lhc/acwb\_1.1/** 目录下的 **run\_jobs.py** 文件，将其粘贴至 **/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/pre\_opt/** 目录中。

3. 在 **/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/pre\_opt/** 目录下打开终端，输入下列命令

```C#
python run\_jobs.py```

4. 此时会提示让你输入想要运用多少个线程，该数值由 CPU 决定。本服务器的 CPU 为 AMD R9 7950X，是 16 核心，32 线程。由于共有 8 个构象文件，因此我们选择分配给该任务 8 个线程。

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.012.png)

```<p>**注意：**    </p><p>- 若分配 8 个线程，但构象文件多于 8 个，此时会首选运行前八个构象文件，若有构象文件分析完之后，会自动递补运行后面的构象文件，不需要手动操作。</p>```

5. 此时，可以看到，在 **/pre\_opt/**目录下生成了以每个构象文件名命名的 8 个文件夹。

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.013.png)

4.4.2 **运行 data\_prcs.py**

1. 这 8 个文件夹中都含有一个 log 文件，这个文件是用于 orca 计算，我们需要将其复制到一个新的目录中，但挨个复制比较麻烦。因此点击图中的搜索按钮，搜索 log，此时会发现，出现了 8 个 log 文件，复制这 8 个 log 文件。

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.013.png)

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.011.png)

2. 在 **/pre\_opt/** 目录下新建一个名为 **logs** 的目录，将 8 个 log 文件粘贴进去。

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.013.png)

3. 复制 **/home/lhc/acwb\_1.1/** 目录下的 **data\_prcs.py** 文件，将其粘贴至 **/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/pre\_opt/logs/** 目录中。

4. 在 **/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/pre\_opt/logs/**目录下打开终端，输入下列命令

```C#
python data\_prcs.py```

5. 若提示下列错误，则代表 python 环境中没有安装 numpy 环境。

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.014.png)

6. 我们在桌面上打开终端，输入下列命令，即可安装 numpy 环境。

```C#
# 安装 numpy
conda install numpy

# 安装 pandas
conda install pandas

# 安装 openpyxl
conda install openpyxl```

7. 在 **/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/pre\_opt/logs/** 目录下打开终端，输入下列命令

```C#
python data\_prcs.py```

会看到提示缺少吉布斯自由能。

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.015.png)

8. 在 **/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/pre\_opt/logs/** 目录下会看到生成了一个 **acwb\_cluster.xyz** 文件，该文件包含了优化后的构象的详细信息。

4.5 **结构优化和频率计算**

4.5.1  **运行 acwb.py**

1. 复制 **/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/pre\_opt/logs/** 目录下的**acwb\_cluster.xyz** 文件，在 **/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/** 目录下新建一个名为 **opt\_freq** 的目录，将刚复制的 **acwb\_cluster.xyz** 文件粘贴进去。

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.016.png)

2. 复制 **/home/lhc/acwb\_1.1/** 目录下的 **acwb.py** 文件，将其粘贴至 **/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/opt\_freq/** 目录中。

3. 复制 **/home/lhc/acwb\_1.1/protocol/opt\_freq\_orca/** 目录下的 **opt\_freq\_chloroform.protocol** 文件，将其粘贴至 **/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/opt\_freq/** 目录中。

```<p>**注意**：    </p><p>- 该目录下共有 3 个文件，分别对应乙腈、氯仿、甲醇</p><p>- 用什么溶剂测 CD，就选择对应溶剂的文件。3-buten-2-ol 是用氯仿进行测试，因此选择opt\_freq\_chloroform.protocol 文件。</p>```
![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.013.png)

4. 在 **/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/opt\_freq/** 目录中，打开终端，输入下列命令

```C#
python acwb.py acwb\_cluster.xyz```
![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.017.png)

5. 会将 **acwb\_cluster.xyz** 文件中的 8 个构象信息拆分成 8 个 inp 格式的文件，每个文件包含一个构象的详细信息。

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.018.png)

4.5.2  **运行 run\_jobs.py**

1. 在 **/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/opt\_freq/** 目录下新建一个名为 **inp** 的目录，将刚生成的 8 个 inp 文件粘贴进去。

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.019.png)

2. 复制 **/home/lhc/acwb\_1.1/**目录下的 **run\_jobs.py** 文件，将其粘贴至 **/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/opt\_freq/inp/** 目录中。

3. 在 **/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/opt\_freq/inp/** 目录下打开终端，输入下列命令

```C#
python run\_jobs.py```

此时仍提示让你输入想要运用多少个线程，我们依旧选择分配给该任务 8 个线程。

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.020.png)

4. 此时，可以看到，在 **/inp/**目录下生成了以每个构象文件名命名的 8 个文件夹。这 8 个文件夹中都含有一个 log 文件，这个文件是用于 orca 计算。

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.018.png)

4.5.3  **运行 data\_prcs.py**

1. 点击图中的搜索按钮，搜索 **log**，此时会发现，出现了 8 个 log 文件，复制这 8 个 log 文件。

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.013.png)

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.011.png)

2. 在 **/inp/**目录下新建一个名为 **logs** 的目录，将 8 个 log 文件粘贴进去。

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.018.png)

3. 复制 **/home/lhc/acwb\_1.1/** 目录下的 **data\_prcs.py**文件，将其粘贴至 **/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/opt\_freq/inp/logs/** 目录中。

4. 在 **/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/opt\_freq/inp/logs/** 目录下打开终端，输入下列命令

```C#
python data\_prcs.py```

5. 在 **/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/opt\_freq/inp/logs/** 目录下会生成多个文件。

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.018.png)

6. 虽然在 **/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/opt\_freq/inp/logs/** 目录下新生成的文件名与在 **/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/pre\_opt/logs/**目录下的文件名相同，但是文件内的内容不一样。

|路径|acwb\_cluster.xyz|population.xlx|
| :-: | :-: | :-: |
|/pre\_opt/logs/|delet G 数值不同|吉布斯自由能为 0|
|/opt\_freq/inp/logs/||计算出了吉布斯自由能|

4.6 **性质计算**

4.6.1 **碳谱计算（ STS 处理）**

4.6.1.1 **运行 acwb.py**

1. 复制**/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/opt\_freq/inp/logs/**目录下的 **acwb\_cluster.xyz** 文件，在 **/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/**目录下新建一个名为 **STS** 的目录，将刚复制的 **acwb\_cluster.xyz** 文件粘贴进去。

2. 复制 **/home/lhc/acwb\_1.1/** 目录下的 **acwb.py** 文件，将其粘贴至 **/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/STS/** 目录中。

3. 复制 **/home/lhc/acwb\_1.1/protocol/STS\_g16/** 目录下的 **STS\_CHCl3.protocol** 文件，将其粘贴至 **/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/STS/** 目录中。

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.018.png)

4. 在**/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/STS/** 目录中，打开终端，输入下列命令

```C#
python acwb.py acwb\_cluster.xyz```
![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.021.png)

5. 会将 acwb\_cluster.xyz 文件中的 8 个构象信息拆分成 8 个 gif 格式的文件，每个文件包含一个构象的详细信息。

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.016.png)

4.6.1.2 **运行 run\_jobs.py**

1. 在 **/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/STS/**目录下新建一个名为 **gifs** 的目录，将刚生成的 8 个 gif 文件粘贴进去。

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.013.png)

2. 复制 **/home/lhc/acwb\_1.1/** 目录下的 **run\_jobs.py** 文件，将其粘贴至 **/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/STS/gifs/** 目录中。

3. 在 /home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/STS/gifs/目录下打开终端，输入下列命令

```C#
python run\_jobs.py```

此时仍提示让你输入想要运用多少个线程，我们依旧选择分配给该任务 8 个线程。

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.022.png)

4. 此时，可以看到，在 **/gifs/**目录下生成了以每个构象文件名命名的 8 个文件夹。这 8 个文件夹中都含有一个 out 文件，这个文件是用于 Gaussian 计算。

4.6.1.3 **运行 data\_prcs.py**

1. 点击图中的搜索按钮，搜索 out，此时会发现，出现了 8 个 out 文件，复制这 8 个 out 文件。

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.013.png)

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.018.png)

2. 在 **/gifs/**目录下新建一个名为 **outs** 的目录，将 8 个 out 文件粘贴进去。

3. 复制**/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/opt\_freq/inp/logs/**目录下的 **population.xlsx** 文件，粘贴至**/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/STS/gifs/outs/** 目录中。

4. 复制 **/home/lhc/acwb\_1.1/** 目录下的 **data\_prcs.py** 文件，将其粘贴至 **/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/STS/gifs/outs/** 目录中。

5. 在 **/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/STS/gifs/outs/** 目录下打开终端，输入下列命令

```C#
python data\_prcs.py```
![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.023.png)

6. 在 **/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/STS/gifs/outs/** 目录下生成一个名为 **Averaged\_C\_shielding.xlsx** 的文件

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.011.png)

4.6.2 **耦合常数计算（j\_coupling）**

4.6.2.1 **运行 acwb.py**

1. 复制**/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/opt\_freq/inp/logs/**目录下的 **acwb\_cluster.xyz** 文件，在 **/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/**目录下新建一个名为 **j\_coupling** 的目录，将刚复制的 **acwb\_cluster.xyz** 文件粘贴进去。

2. 复制 **/home/lhc/acwb\_1.1/** 目录下的 **acwb.py** 文件，将其粘贴至 **/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/j\_coupling/** 目录中。

3. 复制 **/home/lhc/acwb\_1.1/protocol/coupling\_orca/** 目录下的 **coupling\_CHCl3.protocol** 文件，将其粘贴至 **/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/j\_coupling/** 目录中。

4. 在 **/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/j\_coupling/** 目录下打开终端，输入下列命令

```C#
python acwb.py acwb\_cluster.xyz```
![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.024.png)

5. 会将 **acwb\_cluster.xyz** 文件中的 8 个构象信息拆分成 8 个 inp 格式的文件，每个文件包含一个构象的详细信息。

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.013.png)

4.6.2.2 **运行 run\_jobs.py**

1. 在 **/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/j\_coupling/**目录下新建一个名为 **inp** 的目录，将刚生成的 8 个 inp 文件粘贴进去。

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.013.png)

2. 复制 **/home/lhc/acwb\_1.1/** 目录下的 **run\_jobs.py** 文件，将其粘贴至 **/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/j\_coupling/inp/** 目录中。

3. 在 **/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/j\_coupling/inp/**目录下打开终端，输入下列命令

```C#
python run\_jobs.py```

此时仍提示让你输入想要运用多少个线程，我们依旧选择分配给该任务 8 个线程。

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.025.png)

4. 此时，可以看到，在 /inp/目录下生成了以每个构象文件名命名的 8 个文件夹。这 8 个文件夹中都含有一个 inp 文件，这个文件是用于 ORCA 计算。

4.6.2.3 **运行 data\_prcs.py**

1. 点击图中的搜索按钮，搜索 log，此时会发现，出现了 8 个 **log** 文件，复制这 8 个 log 文件。

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.016.png)

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.018.png)

2. 在 **/inp/**目录下新建一个名为 **logs** 的目录，将 8 个 log 文件粘贴进去。

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.013.png)

3. 复制**/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/opt\_freq/inp/logs/**目录下的 **population.xlsx** 文件，粘贴至**/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/STS/inp/logs/** 目录中。

4. 复制 **/home/lhc/acwb\_1.1/** 目录下的 **data\_prcs.py** 文件，将其粘贴至 **/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/STS/inp/logs/** 目录中。

5. 在 **/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/STS/inp/logs/** 目录下打开终端，输入下列命令

```C#
python data\_prcs.py```
![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.026.png)

6. 在 **/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/STS/inp/logs/** 目录下生成一个名为 **averaged\_coupling\_constant.xlsx** 的文件

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.011.png)

7. 在 **averaged\_coupling\_constant.xlsx** 文件中，表格中展示的是通过计算得到的不同氢之间的耦合常数，单位是 Hz。

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.018.png)

4.6.3 **ECD 计算（ECD\_orca）**

4.6.3.1 **运行 acwb.py**

1. 复制**/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/opt\_freq/inp/logs/**目录下的 **acwb\_cluster.xyz** 文件，在 **/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/**目录下新建一个名为 **ECD\_orca** 的目录，将刚复制的 **acwb\_cluster.xyz** 文件粘贴进去。

2. 复制 **/home/lhc/acwb\_1.1/** 目录下的 **acwb.py** 文件，将其粘贴至 **/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/ECD\_orca/** 目录中。

3. 复制 **/home/lhc/acwb\_1.1/protocol/ECD\_orca/** 目录下的 **ECD-b3lyp\_TZV(P)\_acetonitrile.protocol** 文件，将其粘贴至 **/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/ECD\_orca/** 目录中，运行下列命令

```C#
python acwb.py acwb\_cluster.xyz```
![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.024.png)

4. 会将 **acwb\_cluster.xyz** 文件中的 8 个构象信息拆分成 8 个 **inp** 格式的文件，每个文件包含一个构象的详细信息。

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.016.png)

4.6.3.2 **运行 run\_jobs.py**

1. 在 **/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/ECD\_orca/**目录下新建一个名为 **inp** 的目录，将刚生成的 8 个 inp 文件粘贴进去。

2. 复制 **/home/lhc/acwb\_1.1/** 目录下的 **run\_jobs.py** 文件，将其粘贴至 **/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/ECD\_orca/inp/** 目录中。

3. 在 **/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/ECD\_orca/inp/**目录下打开终端，输入下列命令

```C#
python run\_jobs.py```

此时仍提示让你输入想要运用多少个线程，我们依旧选择分配给该任务 8 个线程。

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.027.png)

4. 此时，可以看到，在 **/inp/**目录下生成了以每个构象文件名命名的 8 个文件夹。这 8 个文件夹中都含有一个 inp 文件，这个文件是用于 ORCA 计算。

4.6.3.3 **运行 Mutliwfn**

1. 点击图中的搜索按钮，搜索 **log**，此时会发现，出现了 8 个 log 文件，复制这 8 个 log 文件。

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.011.png)

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.011.png)

2. 在 **/inp/**目录下新建一个名为 **logs** 的目录，将 8 个 log 文件粘贴进去。

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.016.png)

3. 复制**/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/opt\_freq/inp/logs/**目录下的 **multiple.txt** 文件，粘贴至 **Multiwfn** 软件的工作目录中，即 **/home/lhc/Multiwfn\_3.8\_bin\_Linux/**目录中。

4. 打开 **multiple.txt** 文件，我们可以看到文件中列举了 **/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/opt\_freq/inp/logs\** 路径中 8 个 log 文件的位置，但是我们要替换成 **/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/ECD\_orca/inp/logs/** 路径中 8 个 log 文件的位置。

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.011.png)

5. 点击查找和替换，将 **/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/opt\_freq/inp/logs\** 路径全部替换为**/home/lhc/acwb\_1.1/compounds/01\_3-buten-2-ol/3-buten-2-ol/ECD\_orca/inp/logs/** 路径。

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.011.png)

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.028.png)

6. 此时，还需要在路径的两端加上“ ”，完成上述操作后，保存文件退出即可。

![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.018.png)

7. 在 **/home/lhc/Multiwfn\_3.8\_bin\_Linux/**目录中打开终端，输入下列命令 ，即可进行运算

```C#
Multiwfn multiple.txt```
![...](..\..\0.%20软件教程\化学软件（Linux）\images\ACWB：自动化计算化学工作流程软件使用教程.029.png)

8. 绘制 ECD 曲线

```C#
# 绘制 IR/Raman/UV-Vis/ECD/VCD/ROA/NMR spectrum
11

# 绘制 ECD 谱图
4

# 读取速度表象的转子强度，这是绘制ECD光谱所需的关键参数之一。
2

# 调整横坐标的起点、终点和坐标轴标签间隔，使光谱主体特征充满画面
3

# 输入横坐标的起点、终点和坐标轴标签间隔（根据自己的谱图任意调整），目的是使光谱主体特征充满画面
120 300 20

# 把模拟的 ECD 曲线数据导出到当前目录下的 spectrum\_curve.txt 文件中。
# 同时，离散的跃迁数据会导出到 spectrum\_line.txt 文件中。
2

# 绘制当前设置下的光谱图形
0 Plot spectrum

# 保存当前绘制的光谱图形到当前工作目录下。保存格式可以通过  -4  选项设置。
1 Save graphical file of the spectrum in current folder

# 设置保存图形的格式，默认为PNG格式。你可以选择其他支持的格式，如EPS、SVG等。
-4 Set format of saving graphical file, current: png 

# 将光谱的X-Y数据（波长和吸光度）导出为纯文本文件，方便后续在其他软件中进行分析或绘图。
2 Export X-Y data set of lines and curves to plain text file 

# 将跃迁数据（如激发能、振子强度等）导出为纯文本文件。
-2 Export transition data to plain text file 

# 显示当前的跃迁数据，包括激发能、振子强度等信息。
-1 Show transition data```


9. 将 Multiwfn 的 ECD 数据和实测 CD 数据导入到绘图软件中

\5. **参考资料**

[Gaussian的安装方法及运行时的相关问题](http://sobereva.com/439)


