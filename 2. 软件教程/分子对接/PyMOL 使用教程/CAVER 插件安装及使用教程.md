
**CAVER 插件安装及使用教程**

\1. **安装教程**

1. 浏览器搜索 PyMOLwiki，搜索 CAVER

![...](..\..\..\0.%20软件教程\分子对接\PyMOL%20使用教程\images\CAVER%20插件安装及使用教程.001.png)

2. 然后先安装 Java，再下载下面的安装包

![...](..\..\..\0.%20软件教程\分子对接\PyMOL%20使用教程\images\CAVER%20插件安装及使用教程.002.png)

3. 进行下载，下载完成之后打开 Pymol

![...](..\..\..\0.%20软件教程\分子对接\PyMOL%20使用教程\images\CAVER%20插件安装及使用教程.003.png)

4. 点击Plugin中的Plugin Manager

![...](..\..\..\0.%20软件教程\分子对接\PyMOL%20使用教程\images\CAVER%20插件安装及使用教程.004.png)

5. 再点击Install New Plugin中的Choose file....，将文件上传之后点击安装即可

\2. **使用教程**

1. 首先在 PyMOL 打开你的蛋白和配体结合的文件

![...](..\..\..\0.%20软件教程\分子对接\PyMOL%20使用教程\images\CAVER%20插件安装及使用教程.005.png)

2. 然后选中配体小分子，打开 caver 插件

![...](..\..\..\0.%20软件教程\分子对接\PyMOL%20使用教程\images\CAVER%20插件安装及使用教程.006.png)

- Output directories：指定输出文件的保存路径（这里是 C:\Software\01-Address\34-python），计算结果会存储到该目录。
- Configuration save/load：用于 “加载（Load settings）” 或 “保存（Save settings）” 软件配置，方便重复使用相同参数。
- Maximum Java heap size (MB)：设置 Java 堆内存大小（此处为 6000MB），内存越大，越能支持复杂分子的计算。
- Minimum probe radius：最小探针半径（0.9），探针用于模拟 “探索” 分子通道的工具，半径影响通道检测的精细度。
- Shell depth：壳层深度（4）；Shell radius：壳层半径（3）；Clustering threshold：聚类阈值（3.5），这些参数共同控制通道分析的算法逻辑（如区域划分、结果聚类）。
- Number of approximating balls：近似球的数量（12），用于算法中对分子结构的简化近似。
- Input model：选中的输入模型为 emodin\_out\_g263\_fad，可通过 “Reload” 重新加载模型。（这里一定要选中你的模型）

3. 然后点击配体，点击 “Convert surroundings to x,y,z coordinates of starting point” 将配体（sele）转换为起始点坐标；也可直接设置 x, y, z 坐标（当前为 x: -5.296, y: -4.736, z: 4.711）。
- Starting point optimization：优化起始点的参数，Maximum distance (Å)（最大距离，3 埃）和 Desired radius (Å)（期望半径，5 埃），用于调整起始点附近的计算范围。
4. 最后点击Compute tunnels，则计算出所有的底物通道
5. 分析的结果文件均保存在工作路径，特别是“**analysis**”文件夹，从中可以获得每个通道最小/最大半径、平均半径、长度、曲率、涉及的残基/原子等信息。

![...](..\..\..\0.%20软件教程\分子对接\PyMOL%20使用教程\images\CAVER%20插件安装及使用教程.007.png)


