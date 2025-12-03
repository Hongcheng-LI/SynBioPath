
**PyMOL-开源版安装及使用教程**

\1. **PyMOL简介**

PyMOL 适用于创作高品质的小分子或是生物大分子的三维结构图像。在所有正式发表的科学文献中的蛋白质结构图像中，有四分之一是使用 PyMOL 来制作的。

PyMOL 是一个开源项目，目前有企业版、政府和学术版、教学版，还有开源版。除了开源版和教学版外，其他都是需要付费购买的。目前从网络上下载的 edu 版的 PyMOL 有很多功能限制，对于要发表文章需要图片渲染等高级功能的用户来说极为不便。本文就介绍在 Win 10 系统中安装 PyMOL 开源版本的教程。

\2. **安装教程**

2.1 **安装 python**

1. 打开 python 官网，下载 python windows installer 64 bit 安装包，本教程中安装的 python 版本是 3.11.9。

<https://www.python.org/downloads/release/python-3119/>

2. 点击安装包，勾选**Add python.exe to PATH**，并选择合适的安装地址。本教程的安装位置为 **F:\Software\Address\python**。

![...](..\..\..\0.%20软件教程\分子对接\PyMOL%20使用教程\images\PyMOL-开源版安装及使用教程.001.png)

注意：安装路径中不要出现中文和空格，安装时候要勾选 pip。

3. 安装完成后，按**Win+R**，输入cmd进入命令行窗口，在命令行中输入**python -V**，若输出版本号，则证明安装成功。

![...](..\..\..\0.%20软件教程\分子对接\PyMOL%20使用教程\images\PyMOL-开源版安装及使用教程.002.png)

2.2 **安装 PMW**

按**Win+R**，输入**cmd**进入命令行窗口，在命令行中输入下列命令

```Markdown
#使用 pip 安装 pmw
python -m pip install pmw```
![...](..\..\..\0.%20软件教程\分子对接\PyMOL%20使用教程\images\PyMOL-开源版安装及使用教程.003.png)

出现 Successfully installed 则代表安装成功。

2.3 **安装 PyMOL**

1. 打开下列网站，找到与自己 python 版本对应的 PyMOL 安装包，此处下载的是

<https://github.com/cgohlke/pymol-open-source-wheels/releases>

pymol-3.0.0-cp311-cp311-win\_amd64.whl

pymol\_launcher-3.0-cp311-cp311-win\_amd64.whl

```cp311 指 python 版本是 3.11 版本，amd64 是指 64 位系统```

2. 打开下列网站，找到与自己 python 版本对应的 numpy 安装包，此处下载的是

<https://github.com/cgohlke/numpy-mkl-wheels/releases>

` `mkl\_fft-1.3.8-cp311-cp311-win\_amd64.whl

3. 将下载好的 3 个文件放在一个英文路径下的文件夹中，本次安装放在 F 盘中，路径为：F:

4. 在命令行中输入以下代码，进入 python 的安装目录

```Markdown
#由C盘进入F盘
F:

#进入python所在的文件夹
cd F:\Software\Address\python```

5. 输入以下三行命令，安装 PyMOL

```Markdown
python -m pip install F:/mkl\_fft-1.3.8-cp311-cp311-win\_amd64.whl
python -m pip install F:/pymol-3.0.0-cp311-cp311-win\_amd64.whl
python -m pip install F:/pymol\_launcher-3.0-cp311-cp311-win\_amd64.whl```


```<p>注意：</p><p>代码中的 **F:** 是**三个安装文件存放的路径**（在这里，我建议你就放在磁盘根目录下）</p><p>如果你将文件放在了 **D 盘根目录**下，那么你就只需要把代码中的 **F: 换为 D:** 即可</p><p>一定要记住 **PyMOL** 文件要和 **python 版本相匹配**，要不然无法安装。</p>```

出现 successfully installed 字样说明安装成功。

![...](..\..\..\0.%20软件教程\分子对接\PyMOL%20使用教程\images\PyMOL-开源版安装及使用教程.004.png)

6. 安装完成后，进入 python 安装目录，即可看到 PyMOL.exe 安装文件，鼠标右键发送到桌面快捷方式，选择管理员身份运行，即可打开软件。

\3. **入门教程**

3.1 **软件界面介绍**

![...](..\..\..\0.%20软件教程\分子对接\PyMOL%20使用教程\images\PyMOL-开源版安装及使用教程.005.png)

3.2 **查看和修改工作路径**

3.2.1 **查看工作路径**

点击**菜单窗口**中的 **File** -> **Working Directory** -> **File Browser**，即可查看当前的工作目录。

![...](..\..\..\0.%20软件教程\分子对接\PyMOL%20使用教程\images\PyMOL-开源版安装及使用教程.006.png)

3.2.2 **修改工作路径**

点击**菜单窗口**中的 **File** -> **Working Directory** -> **Change**，即可选择指定的文件目录为工作目录。

![...](..\..\..\0.%20软件教程\分子对接\PyMOL%20使用教程\images\PyMOL-开源版安装及使用教程.007.png)

3.2.3 **建议**

- 不同项目设置不同的工作目录
- 设置一个默认工作目录
- 不要把工作目录设置在软件安装目录
- 双击 PDB 文件打开 PyMOL，会自动切换工作目录到该 PDB 文件所在目录。
- 从软件安装处打开 PyMOL，则工作目录为软件安装目录。

3.3 **下载蛋白文件**

3.3.1 **从 PDB 数据库下载**

1. 点击链接，进入 PDB 官网：<https://www.rcsb.org/>

2. 在搜索框中输入需要蛋白的简称或类型，比如输入“Tryptophan-5-halogenase”，在搜索出的结果中选择“8F0X”，点击进入，即可选择下载不同格式的文件。

![...](..\..\..\0.%20软件教程\分子对接\PyMOL%20使用教程\images\PyMOL-开源版安装及使用教程.008.png)

3.3.2 **命令行下载**

1. 在命令行输入窗口输入以下命令，即可下载相应的蛋白结构文件至**当前工作目录**，并打开该 PDB 文件。

```Markdown
#下载编号为“8F0X”的蛋白结构文件
fetch 8F0X```

3.4 **加载 PDB 文件**

3.4.1 **软件打开**

1. 点击**菜单窗口**中的 **File** -> **Open**，即可打开已下载好的 PDB 文件。

![...](..\..\..\0.%20软件教程\分子对接\PyMOL%20使用教程\images\PyMOL-开源版安装及使用教程.009.png)

3.4.2 **文件目录打开**

1. 找到下载好的 PDB 蛋白结构文件，双击即可打开。

3.4.3 **命令行打开**

1. 在命令行输入窗口输入以下命令，即可下载相应的蛋白结构文件至**当前工作目录**，并打开该 PDB 文件。

```Markdown
#下载编号为“8F0X”的蛋白结构文件
fetch 8F0X```

3.5 **蛋白的平移、放大、旋转**

3.5.1 **平移**

1. 按住鼠标中键不放，然后上下左右移动，蛋白会随着鼠标而移动

3.5.2 **旋转**

1. 按住鼠标左键不放，然后上下左右移动鼠标，蛋白会进行旋转

3.5.3 **缩放**

1. 按住鼠标右键不放，然后上下移动，蛋白会进行缩放

3.5.4 **切割**

1. 滚动鼠标中键， 建议将蛋白渲染成 surface 模式，然后滚动鼠标中键

3.5.5 **问题解决**

1. 当软件不能正常使用上述操作，可以点击
- **File** -> **Reinitialize** -> **Original Settings**，推荐该操作
- **File** -> **Reinitialize** -> **Everything**，注意，该操作会删除当前所有的 Object。

3.6 **蛋白展现形式**

3.6.1 **PyMOL 中蛋白的展现形式**

1. PyMOL 可以以不同的形式来可视化同一个蛋白，具体如下图。

![...](..\..\..\0.%20软件教程\分子对接\PyMOL%20使用教程\images\PyMOL-开源版安装及使用教程.010.png)

- **mesh**：网状
- **ribbon**：丝带
- **line**：线状
- **sticks**：棒（棍）状，一般在看分子间相互作用时常用
- **surface**：表面结构，一般在看蛋白表面的口袋时常用
- **dots**：点（原子）
- **spheres**：球状
- **cartoon**：大部分蛋白展示二级结构用

3.6.2 **展现蛋白的操作区域**

1. 在 2.3 对象列表窗口中，我们可以看到现在有 2 个 object 名字
- 一个是 all，all 不是真实的 object，它代表了所有的 object。
- 一个是 8F0X，8F0X 就是我们刚刚载入的蛋白。

2. 每个 object 都有对应的 A S H L C 操作，如下图所示

![...](..\..\..\0.%20软件教程\分子对接\PyMOL%20使用教程\images\PyMOL-开源版安装及使用教程.011.png)

3.6.3 **对蛋白进行 Action 操作**

**A：**Action，主要包含了对 object 的常用操作的集合，如 复制、删除 object，对 object 加氢，展示 Object 等。

1. **A -> Zoom：**将蛋白结构放大之后，点击该按钮，就可以直接缩放成刚打开时的大小。
2. **A -> Orient：**改变蛋白结构的方向之后，点击该按钮，就可以恢复到刚打开时的状态。
3. **A -> Center**：移动蛋白结构的位置之后，点击该按钮，就可以将蛋白重新移动到最中心的位置。
4. **A -> Origin**：将选定的对象移动到坐标原点（0,0,0）。
5. **A -> Drag matrix**：通过拖动鼠标来旋转、平移和缩放分子结构。
6. **A -> Reset matrix**：将所有旋转、平移和缩放操作恢复到初始状态。
7. **A -> Drag coordinates**： 通过拖动鼠标来移动分子结构。当释放鼠标按钮时，移动将被固定。
8. **A -> Clean**：清除当前的视图，移除所有临时的标记、箭头、测量等。
9. **A -> Preset**：
- **A -> Preset -> simple**：显示蛋白质的简化形式，通常只显示主链的轮廓。
- **A -> Preset -> simple（no solvent）**：显示蛋白质的简化形式，不包括溶剂分子。
- **A -> Preset -> ball and stick**：显示蛋白质的球棍模型，其中原子用球表示，化学键用棍表示。
- **A -> Preset -> b-factor putty**：根据B因子（温度因子）数值显示蛋白质的柔性。B因子越高，表示原子在晶体结构中的位置越不确定，模型将显示为更柔软。
- **A -> Preset -> technical**：显示技术性细节，包括所有原子和键，以及可能的辅助信息，如氢键。
- **A -> Preset -> ligands**：显示蛋白的配体
- **A -> Preset -> ligand sites**：显示配体结合位点，有多种视图选项：
- **A -> Preset -> ligand sites -> cartoon**：以卡通形式显示配体结合位点，突出显示小分子和蛋白质之间的氢键。
- **A -> Preset -> ligand sites -> solid surface**：以实心表面形式显示配体结合位点。
- **A -> Preset -> ligand sites -> solid（better）**：以更精细的实心表面形式显示配体结合位点。
- **A -> Preset -> ligand sites -> transparent surface**：以透明表面形式显示配体结合位点。
- **A -> Preset -> ligand sites -> transparent（better）**：以更精细的透明表面形式显示配体结合位点。
- **A -> Preset -> ligand sites -> dots surface**：以点状表面形式显示配体结合位点。
- **A -> Preset -> ligand sites -> mesh surface**：以网格表面形式显示配体结合位点。
- **A -> Preset -> pretty**：显示蛋白质的美观视图，通常包括主链和侧链的卡通表示。
- **A -> Preset -> pretty（with solvent）**：显示蛋白质的美观视图，包括溶剂分子。
- **A -> Preset -> publication**：显示高质量出版标准的视图，通常用于准备发表的图像。
- **A -> Preset -> publication（with solvent）**：显示高质量出版标准的视图，包括溶剂分子。
10. **A -> Find**：找极性作用力
- **A -> Find -> polar contacts**：
- **A -> Find -> polar contacts -> within selection**：在所选区域内寻找极性作用力
- **A -> Find -> polar contacts -> involving side chain**：寻找包含侧链在内的极性作用力
- **A -> Find -> polar contacts -> involving solvent**：寻找包含溶剂在内的极性作用力
- **A -> Find -> polar contacts -> excluding solvent**：寻找除溶剂之外其余区域的极性作用力
- **A -> Find -> polar contacts -> excluding main chain**：寻找除主链之外其余区域的极性作用力
- **A -> Find -> polar contacts -> excluding intra-main chain**：寻找除主内链之外其余区域的极性作用力
- **A -> Find -> polar contacts -> just intra-side chain**：仅在侧内链区域内寻找极性作用力
- **A -> Find -> polar contacts -> just intra-mian chain**：仅在主内链区域内寻找极性作用力
- **A -> Find -> any contacts**：
- **A -> Find -> any contacts -> between chains within 3.0A**：找出距离在 3.0 A 之内的两条链之间的作用力
- **A -> Find -> any contacts -> between chains within 3.5A**：找出距离在 3.5 A 之内的两条链之间的作用力
- **A -> Find -> any contacts -> between chains within 4.0A**：找出距离在 4.0 A 之内的两条链之间的作用力
- **A -> Find -> halogen-bond interactions**：
- **A -> Find -> halogen-bond interactions -> halogen-bond**：搜索并高亮显示所有的卤素键相互作用。这包括卤素原子与氢原子或其他电负性原子之间的相互作用。
- **A -> Find -> salt-bridge interactions**：
- **A -> Find -> salt-bridge interactions -> salt-bridge**：搜索并高亮显示所有的盐桥相互作用。这有助于识别和分析蛋白质中的电荷互补区域。
- **A -> Find -> pi interactions**：
- **A -> Find -> pi interactions -> all**：搜索并高亮显示所有类型的π相互作用，包括π-π和π-阳离子相互作用。
- **A -> Find -> pi interactions -> pi-pi**：用于识别和显示π-π相互作用，即两个芳香环之间的相互作用。
- **A -> Find -> pi interactions -> pi-cation**：用于识别和显示π-阳离子相互作用，其中阳离子（如质子或金属离子）与芳香环的π电子系统相互作用。
11. **A -> Align**：
- **A -> Align -> to molecule（\*/CA）**：用于将当前选择的分子或分子的一部分对齐到另一个指定的分子。 \*/CA 表示对齐时主要考虑主链的α-碳原子。
- **A -> Align -> to selection（\*/CA）**：
- **A -> Align -> to selection（\*/CA）-> sele**：允许指定一个选择（selection），即分子的特定部分，然后对齐到这个选择。
- **A -> Align -> enable to this（\*/CA）**：用于启用对齐到当前选择的分子或分子的一部分。这通常在多步骤对齐过程中使用，其中第一步是选择一个参考点。
- **A -> Align -> all to this（\*/CA）**：用于将所有分子对齐到当前选择的分子或分子的一部分。这在比较多个相似结构时非常有用。
- **A -> Align -> states（\*/CA）**：用于对齐分子的不同状态。在分子动力学模拟中，分子可能会经历多个构象状态，这个命令可以帮助对齐这些状态以进行比较。
- **A -> Align -> states**：与 states（\*/CA） 类似，但不特别强调使用α-碳原子进行对齐。
- **A -> Align -> matrix from**：用于从当前对齐状态生成一个变换矩阵。这个矩阵可以用于其他对齐操作或保存以供将来使用。
- **A -> Align -> matrix to**：用于应用一个已保存的变换矩阵到当前选择的分子或分子的一部分。这允许你重用之前保存的对齐参数。
- **A -> Align -> matrix reset**：将所有旋转、平移和缩放操作恢复到初始状态。
12. **A -> Generate**：
- **A -> Generate -> selection**：
- **A -> Generate -> selection -> all**：生成包含所有原子的选择。
- **A -> Generate -> selection -> polymer**：生成包含聚合物（如蛋白质、核酸等）的选择。
- **A -> Generate -> selection -> organic**：生成包含有机分子的选择。
- **A -> Generate -> selection -> solvent**：生成包含溶剂分子的选择。
- **A -> Generate -> selection -> polar hydrogens**：生成包含极性氢原子的选择。
- **A -> Generate -> selection -> non-polar hydrogens**：生成包含非极性氢原子的选择。
- **A -> Generate -> selection -> donors**：生成包含氢键供体的选择。
- **A -> Generate -> selection -> acceptors**：生成包含氢键受体的选择。
- **A -> Generate -> selection -> surface atoms**：生成包含分子表面原子的选择。
- **A -> Generate -> selection -> C-alphas**：生成包含α-碳原子的选择，这在蛋白质结构分析中非常有用。
- **A -> Generate -> symetry mates**：
- **A -> Generate -> symetry mates -> within 4A**：生成在指定距离（4 埃）内的对称结构。
- **A -> Generate -> symetry mates -> within 5A**：生成在指定距离（5 埃）内的对称结构。
- **A -> Generate -> symetry mates -> within 6A**：生成在指定距离（6 埃）内的对称结构。
- **A -> Generate -> symetry mates -> within 8A**：生成在指定距离（8 埃）内的对称结构。
- **A -> Generate -> symetry mates -> within 12A**：生成在指定距离（12 埃）内的对称结构。
- **A -> Generate -> symetry mates -> within 20A**：生成在指定距离（20 埃）内的对称结构。
- **A -> Generate -> symetry mates -> within 50A**：生成在指定距离（50 埃）内的对称结构。
- **A -> Generate -> symetry mates -> within 100A**：生成在指定距离（100 埃）内的对称结构。
- **A -> Generate -> symetry mates -> within 250A**：生成在指定距离（250 埃）内的对称结构。
- **A -> Generate -> symetry mates -> within 1000A**：生成在指定距离（1000 埃）内的对称结构。
- **A -> Generate -> vacuum electrostatics**：
- **A -> Generate -> vacuum electrostatics -> protein contact potential**：显示蛋白的静电势图
13. **A -> Assign sec, struc.**：用于分配或修改分子对象的二级结构（如螺旋、片层等）和三级结构信息。这对于分析蛋白质结构和理解其功能非常重要。
14. **A -> Rename object**：用于重命名当前选择的对象。在处理多个分子或分子片段时，重命名可以帮助更好地组织和识别不同的对象。
15. **A -> Copy to object**：
- **A -> Copy to object -> new**：会创建一个名为 "new" 的新对象副本。你可以在创建副本后对其进行进一步的修改或分析，而不会影响原始对象。
- **A -> Group -> new**：会创建一个新的组，并将当前选择的对象添加到该组中。分组可以帮助你组织复杂的分子模型，特别是当模型包含多个分子或分子片段时。
- **A -> Group -> ungroup**：用于取消对象的分组。如果你之前将对象分组，但后来需要对单个对象进行操作，可以使用这个命令将对象从组中移除。
16. **A -> Delete object**：删除项目，该操作属于红色警告操作，是不可逆的操作。删除项目后，无法通过 Ctrl-Z 进行撤销。
17. **A -> Hydrogens**：在 line 和 stick 模式下面可以看到 H 原子，cartoon 模式下面看不到氢原子 因此在 line 或者 stick 模式下，执行下述操作。
- **A -> Hydrogens -> add**：增加所有氢原子
- **A -> Hydrogens -> add polar**：增加极性氢原子。
- **A -> Hydrogens -> remove**：删除所有氢原子
- **A -> Hydrogens -> remove non polar**：删除所有非极性氢原子。
18. **A -> Remove Waters**：删除水分子，该操作属于红色警告操作，是不可逆的操作。删除水分子后，无法通过 Ctrl-Z 进行撤销。
19. **A -> State**：
- **A -> State -> freeze**：冻结当前选择对象的所有状态，使其在动画或多状态对象中保持当前状态。
- **A -> State -> all states**：显示对象的所有可能状态。
- **A -> State -> thaw**：解冻对象，使其可以在动画或多状态对象中变化。
- **A -> State -> split**：将当前选择的对象分割成多个独立的对象，每个对象对应一个状态。
20. **A -> Masking**：
- **A -> Masking -> mask**：隐藏当前选择的对象或分子部分。
- **A -> Masking -> unmask**：显示之前被隐藏的对象或分子部分。
21. **A -> Sequence**：
- **A -> Sequence -> include**：在序列显示中包含当前选择的残基。
- **A -> Sequence -> exclude**：在序列显示中排除当前选择的残基。
- **A -> Sequence -> default**：恢复序列显示的默认设置。
22. **A -> Movement**：
- **A -> Movement -> protect**：保护当前选择的对象，防止在动画或多状态对象中变化。
- **A -> Movement -> deprotect**：解除保护，允许当前选择的对象在动画或多状态对象中变化。
23. **A -> Compute**：
- **A -> Compute -> atom count**：计算当前选择的原子数。
- **A -> Compute -> charge**：计算当前选择的电荷。
- **A -> Compute -> surface area**：计算当前选择的表面区域。
- **A -> Compute -> molecular weight**：计算当前选择的分子量。

3.6.4 **对蛋白进行 Show 操作**

**S：**Show， 将 object 渲染成 cartoon 、line、stick，sphere，surface，mesh，dots，ribbon 等模式

1. **S -> as**：
- **S -> as -> Wire**：将对象渲染成线框模式，显示原子之间的连接线，但不显示原子本身。
- **S -> as -> Lines**：将对象渲染成线模式，只显示原子之间的连接线，不显示原子。
- **S -> as -> Nonbonded**：显示非键相互作用，如氢键、π-π堆积等，通常用于突出显示分子间的非共价相互作用。
- **S -> as -> Licorice**： 将对象渲染成棒状模式，显示原子为棒状，化学键为棍状。
- **S -> as -> Sticks**：将对象渲染成棍状模式，显示原子为球体，化学键为棍状。
- **S -> as -> nb\_spheres**：显示非键相互作用的球体，通常用于突出显示分子间的非共价相互作用。
- **S -> as -> Ribbon**：将对象渲染成带状模式，通常用于展示蛋白质的二级结构，如α-螺旋和β-折叠。
- **S -> as -> Cartoon**：将对象渲染成卡通模式，显示蛋白质的二级结构为卡通带，提供更直观的结构信息。
- **S -> as -> Label**：在对象上添加标签，如原子编号、残基名称等，有助于识别特定的原子或残基。
- **S -> as -> Cell**：将对象渲染成单元格模式，显示分子的晶体学单元格。
- **S -> as -> Dots**：将对象渲染成点模式，只显示原子位置，不显示化学键。
- **S -> as -> Spheres**：将对象渲染成球体模式，显示原子为球体，提供原子的三维空间分布。
- **S -> as -> Mesh**：将对象渲染成网格模式，显示原子的表面网格，通常用于展示分子表面。
- **S -> as -> Surface**：将对象渲染成表面模式，显示原子的三维表面，提供更直观的分子表面信息。
- **S -> as -> Flag ignore**：
- **S -> as -> Flag ignore -> clear**：清除对象的忽略标志，使其在渲染和选择操作中可见。
2. **S -> Wire**：将选定对象渲染成线框模式，显示原子之间的连接线，但不显示原子本身。
3. **S -> Lines**：将选定对象渲染成线模式，只显示原子之间的连接线，不显示原子。
4. **S -> Nonbonded**：显示选定对象的非键相互作用，如氢键、π-π堆积等。
5. **S -> Licorice**：将选定对象渲染成棒状模式，显示原子为棒状，化学键为棍状。
6. **S -> Sticks**：将选定对象渲染成棍状模式，显示原子为球体，化学键为棍状。
7. **S -> nb\_spheres**：显示选定对象的非键相互作用的球体。
8. **S -> Ribbon**：将选定对象渲染成带状模式，通常用于展示蛋白质的二级结构。
9. **S -> Cartoon**：将选定对象渲染成卡通模式，显示蛋白质的二级结构为卡通带。
10. **S -> Label**：在选定对象上添加标签，如原子编号、残基名称等。
11. **S -> Cell**：将选定对象渲染成单元格模式，显示分子的晶体学单元格。
12. **S -> Dots**：将选定对象渲染成点模式，只显示原子位置，不显示化学键。
13. **S -> Spheres**：将选定对象渲染成球体模式，显示原子为球体。
14. **S -> Mesh**：将选定对象渲染成网格模式，显示原子的表面网格。
15. **S -> Surface**：将选定对象渲染成表面模式，显示原子的三维表面。
16. **S -> Flag ignore**：
- **S -> Flag ignore -> clear**：清除选定对象的忽略标志，使其在渲染和选择操作中可见。
17. **S -> Organic**：
- **S -> Organic -> lines**：将有机分子渲染成线模式。
- **S -> Organic -> sticks**： 将有机分子渲染成棍状模式。
- **S -> Organic -> spheres**：将有机分子渲染成球体模式。
18. **S -> Main Chain：**
- **S -> Main Chain -> lines：**将主链渲染成线模式。
- **S -> Main Chain -> sticks：**将主链渲染成棍状模式。
- **S -> Main Chain -> spheres：**将主链渲染成球体模式。
19. **S -> Side Chain**：
- **S -> Side Chain -> lines：**将侧链渲染成线模式。
- **S -> Side Chain -> sticks：**将侧链渲染成棍状模式。
- **S -> Side Chain -> spheres：**将侧链渲染成球体模式。
20. **S -> Disulfides**：
- **S -> Disulfides -> lines：**将二硫键渲染成线模式。
- **S -> Disulfides -> sticks：**将二硫键渲染成棍状模式。
- **S -> Disulfides -> spheres：**将二硫键渲染成球体模式。
21. **S -> Valence**：显示原子的价电子，有助于理解原子的成键情况。


```<p>**注意：Show 有两类操作方式**</p><p>1. **先点击 S -> as -> cartoon，再点击 S -> as -> stick：**</p><p>- **可以看到 as 模式是把原有的渲染模式抹除后再重新渲染，经过上述操作后仅仅显示 stick 形式。**</p><p>2. **先点击 S -> as -> cartoon，再点击 S -> stick：**</p><p>- **可以看到 该操作是保留原有的渲染模式，再添加新的渲染模式，经过上述操作后同时显示cartoon 和 stick 形式。**</p>```
![...](..\..\..\0.%20软件教程\分子对接\PyMOL%20使用教程\images\PyMOL-开源版安装及使用教程.012.png)

3.6.5 **对蛋白进行 Hide 操作**

**H：**Hide，根据 object 的状态或者描述进行相应的掩藏

1. **H -> everything**：隐藏所有对象。
2. **H -> Wire**：隐藏对象的线框表示。
3. **H -> Lines**：隐藏对象的线条表示。
4. **H -> Nonbonded**：隐藏非键相互作用。
5. **H -> Licorice**：隐藏对象的棒状表示。
6. **H -> Sticks**：隐藏对象的棍状表示。
7. **H -> nb\_spheres**：隐藏非键相互作用的球体表示。
8. **H -> Ribbon**：隐藏对象的带状表示，通常用于蛋白质的二级结构。
9. **H -> Cartoon**：隐藏对象的卡通表示，通常用于蛋白质的二级结构。
10. **H -> Label**： 隐藏标签，如原子编号、残基名称等。
11. **H -> Cell**：隐藏晶体学单元格。
12. **H -> Dots**：隐藏点表示。
13. **H -> Spheres**：隐藏球体表示。
14. **H -> Mesh**：隐藏网格表示。
15. **H -> Surface**：隐藏表面表示。
16. **H -> Flag ignore**：
- **H -> Flag ignore -> clear**：清除隐藏被标记为忽略的对象。
17. **H -> Main Chain：隐藏主链。**
18. **H -> Side Chain**：隐藏侧链。
19. **H -> waters**：隐藏水分子。
20. **H -> Hydrogens**：
- **H -> Hydrogens -> all**：隐藏所有氢原子。
- **H -> Hydrogens -> nonpolar**：隐藏非极性氢原子。
21. **H -> unselected**：隐藏未选择的部分。
22. **H -> valence**：隐藏价电子。

3.6.6 **对蛋白进行 Lable 操作**

**L：**Lable，显示 object 中残基，原子等名称或者属性

1. **L -> Clear**：删除选定对象上所有的标签。
2. **L -> Residues**：在 α 碳原子上标记其残基名字和编号。这是最常用的标签方式，有助于识别蛋白质或核酸中的残基。
3. **L -> Residues（one letter）**：使用单字母代码在α碳原子上标记残基名称。
4. **L -> Chains**：标记链的标识符。
5. **L -> Segments**：标记片段的标识符。
6. **L -> Atom name**：显示对象上所有原子的名称。
7. **L -> Element symbol**：显示对象上所有原子的元素名字
8. **L -> Residue name**：在所有原子上标记残基名称。这在需要详细显示每个原子所属残基时使用，但不常用，因为它会使视图变得混乱。
9. **L -> One letter code**：使用单字母代码标记残基。
10. **L -> Residue identifier**：标记残基的标识符。
11. **L -> Chain identifier**：标记链的标识符。
12. **L -> Segment identifier**：标记片段的标识符。
13. **L -> B-factor**：标记原子的B因子，这有助于识别结构的灵活性。
14. **L -> Occupany**：标记原子的占据率，这有助于识别结构的确定性。
15. **L -> Vdw radius**：查看原子的范德华半径，这有助于理解分子的三维空间分布。
16. **L -> Other properties**：
- **L -> Other properties -> formal charge**：标记原子的形式电荷。
- **L -> Other properties -> partial charge（0.00）**：标记原子的部分电荷，保留两位小数。
- **L -> Other properties -> partial charge（0.0000）**：标记原子的部分电荷，保留四位小数。
- **L -> Other properties -> elec. radius**：标记原子的电子半径。
- **L -> Other properties -> text type**：设置文本类型。
- **L -> Other properties -> numeric type**：设置数字类型。
- **L -> Other properties -> sterochemistry**：标记立体化学信息。
17. **L -> Atom identifiers**：
- **L -> Atom identifiers -> rank**：标记原子的排名。
- **L -> Atom identifiers -> ID**：标记原子的ID。
- **L -> Atom identifiers -> index**：标记原子的索引。

3.6.7 **对蛋白进行 Color 操作**

**C：**Color，对 Object 进行着色

1. **C -> By element**：按照原子类型进行着色
2. **C -> By chain**：
- **C -> By chain -> By chain（elem C）**：根据链，并且结合元素类型为每个链上色。
- **C -> By chain -> By chain（\*/CA）**：根据链，并且结合主链α-碳原子为每个链上色。
- **C -> By chain -> By chain**：简单地根据每个链为分子结构上色。
- **C -> By chain -> chainbows**：为每个链分配彩虹色，产生多彩的效果。
- **C -> By chain -> By segi（elem C）**：根据链段（segment），并且结合元素类型为每个链段上色。
- **C -> By chain -> By segi**：根据链段为每个链段上色。
3. **C -> By ss**：根据二级结构（secondary structure）为分子结构上色，如α-螺旋、β-折叠等。
4. **C -> By rep**：
- **C -> By rep -> lines**：根据线条（line）表示方式上色。
- **C -> By rep -> sticks**：根据棍状（stick）表示方式上色。
- **C -> By rep -> ribbon**：根据带状（ribbon）表示方式上色，通常用于显示蛋白质的二级结构。
- **C -> By rep -> cartoon**：根据卡通（cartoon）表示方式上色，通常用于显示蛋白质的二级结构和三级结构。
- **C -> By rep -> labels**：根据标签的表示方式设置颜色。
- **C -> By rep -> dots**：根据点的表示方式设置颜色。
- **C -> By rep -> spheres**： 根据球体的表示方式设置颜色。
- **C -> By rep -> mesh**：根据网格的表示方式设置颜色。
- **C -> By rep -> surface**：根据表面的表示方式设置颜色。
5. **C -> Spectrum**：
- **C -> Spectrum -> rainbow（elem C）**：根据元素类型设置颜色渐变（彩虹色）。
- **C -> Spectrum -> rainbow（\*/CA）**：根据 α 碳原子设置颜色渐变（彩虹色）。
- **C -> Spectrum -> rainbow**：根据选定对象设置颜色渐变（彩虹色）。
- **C -> Spectrum -> b-factors**：根据B因子设置颜色渐变。
- **C -> Spectrum -> b-factors（\*/CA）**：根据α碳原子的B因子设置颜色渐变。
- **C -> Spectrum -> area（molecular）**：根据分子表面面积设置颜色渐变。
- **C -> Spectrum -> area（solvent）**：根据溶剂可接触表面面积设置颜色渐变。
6. **C -> Auto**：
- **C -> Auto -> elem C**：根据元素类型自动设置颜色。
- **C -> Auto -> all**：自动设置所有对象的颜色。
- **C -> Auto -> by obj（elem C）**：根据对象和元素类型自动设置颜色。
- **C -> Auto -> by obj**：根据对象自动设置颜色。
7. **C -> Reds**：将选定对象的颜色设置为红色。
8. **C -> Greens**：将选定对象的颜色设置为绿色。
9. **C -> Blues**：将选定对象的颜色设置为蓝色。
10. **C -> Yellows**：将选定对象的颜色设置为黄色。
11. **C -> Magentas**：将选定对象的颜色设置为洋红色。
12. **C -> Cyans**：将选定对象的颜色设置为青色。
13. **C -> Oranges**：将选定对象的颜色设置为橙色。
14. **C -> Tints**：为选定对象添加淡色调。
15. **C -> Grays**：将选定对象的颜色设置为灰色。

3.7 **查看该结构的序列**

1. 点击右下角的 S（sequence），即可显示蛋白的序列信息。再点击一次 S，即可隐藏序列信息。

![...](..\..\..\0.%20软件教程\分子对接\PyMOL%20使用教程\images\PyMOL-开源版安装及使用教程.007.png)

2. 点击**菜单窗口**中的**Display** -> **Sequence**，即可显示当前结构的序列。

![...](..\..\..\0.%20软件教程\分子对接\PyMOL%20使用教程\images\PyMOL-开源版安装及使用教程.013.png)

3. 点击**菜单窗口**中的**Display** -> **Sequence mode**，即可选择当前结构序列的显示模式。

![...](..\..\..\0.%20软件教程\分子对接\PyMOL%20使用教程\images\PyMOL-开源版安装及使用教程.006.png)

3.8 **选择蛋白的特定残基**

3.9 **设置背景颜色**

1. 背景颜色默认是黑色的，发表文章的时候背景颜色通常设置为白色。

2. 点击**菜单窗口**中的**Display** -> **background** -> **white**，即可将背景颜色改为白色。

![...](..\..\..\0.%20软件教程\分子对接\PyMOL%20使用教程\images\PyMOL-开源版安装及使用教程.013.png)

3.10 **制作 b-factor value 图**

1. 点击**对象列表窗口**中的**A** -> **preset** -> **b-factor putty**，即可生成 b-factor value 图。

![...](..\..\..\0.%20软件教程\分子对接\PyMOL%20使用教程\images\PyMOL-开源版安装及使用教程.001.png)

![...](..\..\..\0.%20软件教程\分子对接\PyMOL%20使用教程\images\PyMOL-开源版安装及使用教程.001.png)

3.11 **给蛋白关键残基添加 Lable**

1. 以蛋白 8F0X 为例，标记其三个残基：LEU131，SER159，GLN203

2. 载入 8F0X 蛋白

3. 在 8F0X object 上点击 **S** -> **as cartoon**

![...](..\..\..\0.%20软件教程\分子对接\PyMOL%20使用教程\images\PyMOL-开源版安装及使用教程.001.png)

4. 点击右下角的 **S** 开关按钮，选择 LEU131，SER159，GLN203 三个残基，得到 sele 临时object

![...](..\..\..\0.%20软件教程\分子对接\PyMOL%20使用教程\images\PyMOL-开源版安装及使用教程.001.png)

5. 在 sele object 上点击 **S** -> **stick**，**H** -> **main chain**

![...](..\..\..\0.%20软件教程\分子对接\PyMOL%20使用教程\images\PyMOL-开源版安装及使用教程.001.png)

![...](..\..\..\0.%20软件教程\分子对接\PyMOL%20使用教程\images\PyMOL-开源版安装及使用教程.001.png)

6. 在 sele object 上点击 **L** -> **residue**

![...](..\..\..\0.%20软件教程\分子对接\PyMOL%20使用教程\images\PyMOL-开源版安装及使用教程.001.png)

7. 点击 **Mouse Mode** 切换为 **editing** 模式

![...](..\..\..\0.%20软件教程\分子对接\PyMOL%20使用教程\images\PyMOL-开源版安装及使用教程.001.png)

8. 在 sele object 上点击 **C** -> **red**-> **warmpink，**将标记残基的颜色改为酒红色

![...](..\..\..\0.%20软件教程\分子对接\PyMOL%20使用教程\images\PyMOL-开源版安装及使用教程.001.png)

9. 按住 ctrl 键不放，然后将鼠标移动到残基标签上方，并按下鼠标左键不放，然后移动鼠标，就可以调整标签的位置。

![...](..\..\..\0.%20软件教程\分子对接\PyMOL%20使用教程\images\PyMOL-开源版安装及使用教程.001.png)

10. 调整结束后，点击**Mouse Mode** 切换为 **view** 模式。

![...](..\..\..\0.%20软件教程\分子对接\PyMOL%20使用教程\images\PyMOL-开源版安装及使用教程.001.png)

11. 点击**菜单窗口**中的**Display** -> **background** -> **white**，将背景颜色改为白色。

![...](..\..\..\0.%20软件教程\分子对接\PyMOL%20使用教程\images\PyMOL-开源版安装及使用教程.013.png)

3.12 **调整配体的位置**

3.13 **调整修改二面角**

3.14 **测量两个原子之间的距离**

以蛋白 8F0X 为例，测量 Gly107 和 Lys96 两个残基中 N 原子的距离

1. 点击菜单栏中的 **Wizard** -> **Measurement**，打开 Measurement 面板，位于 object list 面板下方。

![...](..\..\..\0.%20软件教程\分子对接\PyMOL%20使用教程\images\PyMOL-开源版安装及使用教程.009.png)

2. 鼠标点击 Gly107 侧链上的 O 原子 和 Lys96 侧链上面的 N 原子，即可显示两个原子之间的距离；

![...](..\..\..\0.%20软件教程\分子对接\PyMOL%20使用教程\images\PyMOL-开源版安装及使用教程.014.png)

3. 如要测定其他 2 个原子的距离，鼠标继续点击选择 2 个原子就可以了。

4. 测定完成后，点击 **Measurement** 面板中的 **done** 就可以了。

![...](..\..\..\0.%20软件教程\分子对接\PyMOL%20使用教程\images\PyMOL-开源版安装及使用教程.006.png)

5. 默认测定的距离是保留 1 位小数，如果想要显示 2 位小数，可点击菜单栏中的 **Setting** -> **Edit All**

![...](..\..\..\0.%20软件教程\分子对接\PyMOL%20使用教程\images\PyMOL-开源版安装及使用教程.013.png)

然后搜索 **label\_digits**，找到该索引，并把后面的数值设置为 **2** 就可以了。如图所示。

![...](..\..\..\0.%20软件教程\分子对接\PyMOL%20使用教程\images\PyMOL-开源版安装及使用教程.013.png)

3.15 **突变氨基酸残基**

\4. **基础教程**

4.1 **将结果保存为图片**

```Markdown
#渲染图片
ray

#在工作目录保存一张名为 aaaa 的 png 图片，像素为 5000 x 5000 px，分辨率为1200 dpi。
png aaaa.png, 5000, 5000, dpi=1200```

\5. **进阶教程**

一、PDB 文件下载

二、PyMOL 常用操作

三、实用的 PyMOL 命令行

set cartoon\_loop\_radius, 0.4

set ray\_trace\_mode, 1

set ray\_shadows, 0

set specular, 0

space cmyk

set ray\_trace\_color, [0,0,0]


