
**GNPS分子网络的构建**

GNPS（global natural products social network）**分子网络**是由美国加利福尼亚大学圣迭戈分校的**Pieter C. Dorrestein** 教授课题组开发的一套在天然产物研究当中对想要分析的样品质谱数据快速进行排重，注释，类似物可视化聚类的一个工具。

**一、前期准备 🌱**

**数据采集与格式转换**

- 获取 LC‑MS/MS 原始数据，在这里推荐Thermo的高分辨质谱QE。
- 使用 **Protein Wizard** 的 **MSConvert** 将 .raw 转换为 mzML、mzXML 或 .mgf，我只尝试过前两者，没感觉到区别。软件可以很方便在网上找到，注意数据转换的时候软件上的filters选peak picking，MS-Level输入1-2。其他选项都是默认，我没有动过。

![...](..\..\0.%20软件教程\化学软件（Windows）\images\GNPS分子网络的构建.001.png)


**二、登录 GNPS 上传数据**

访问 GNPS 官网注册/登录账户。https://gnps.ucsd.edu/

上传数据至 MassIVE：这一步我用的是WinSCP，登录的时候主机名是：xxxxxx@massive-ftp.ucsd.edu(xxxxxx是GNPS官网注册的user name)，密码是注册GNPS官网时的密码。

登陆成功之后即可上传数据，如图所示，将转换好的数据文件拖拽到右边即可。

![...](..\..\0.%20软件教程\化学软件（Windows）\images\GNPS分子网络的构建.002.png)

然后进入官网，页面中下部选择creat molecular network

![...](..\..\0.%20软件教程\化学软件（Windows）\images\GNPS分子网络的构建.003.png)

对于单个数据，直接点第一个 select input files (Required)，母离子和子离子容差参数我一般选0.5和0.2，实际可以比这个低，根据你的仪器选择和数据质量而来，并且鼠标移上去后有官方的建议。该界面上方需要你给本次任务起一个title，省略会报错。

![...](..\..\0.%20软件教程\化学软件（Windows）\images\GNPS分子网络的构建.004.png)

在跳出的界面中按顺序，先选中自己的文件，然后添加至右边spectrum files G1，最后结束添加。

![...](..\..\0.%20软件教程\化学软件（Windows）\images\GNPS分子网络的构建.005.png)

结束finish selection提交之后，这个弹出的页面会关闭，然后点submit就好。

![...](..\..\0.%20软件教程\化学软件（Windows）\images\GNPS分子网络的构建.006.png)

这个分析的过程一般需要十几分钟到一个小时。结束之后可以根据页面的提示查看在库中注释到的Hit，可以下载文件到cytoscape可视化，也可与其他工具联用做更多的分析。




