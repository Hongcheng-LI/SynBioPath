
**BIG-SCAPE：安装及使用教程**

\1. **BIG-SCAPE 介绍**

1.1 **简介**

**BiG-SCAPE**（生物合成基因相似性聚类和勘探引擎）是一个用 Python 编写的软件包，用于构建生物合成基因簇 （BGC） 的序列相似性网络，并通过比较基因簇之间的蛋白质结构域类型、顺序、拷贝数和序列同一性来计算基因簇之间的距离来将它们分组为基因簇家族 （GCF）。

**BiG-SCAPE 2** 工具共有四种工作流程：Cluster、Query、Dereplicate、Benchmark

- bigscape cluster：将生物合成基因簇（BGCs）聚类为基因簇家族（GCFs），功能相当于运行 BiG-SCAPE 1 的 bigscape.py。
- bigscape query：可搜索与用户提供的查询 BGC/.gbk 文件相似的 BGCs。
- bigscape dereplicate：基于蛋白质序列进行冗余分析，去除近乎相同的序列。
- bigscape benchmark：将 BiG-SCAPE 2 Cluster 模式运行结果、BiG-SCAPE 1 运行结果或 BiG-SLICE 运行结果，与用户提供的 BGC <-> GCF 分配集进行比较。

BIG-SCAPE 官网：<https://github.com/medema-group/BiG-SCAPE>

1.2 **Cluster 功能**

1.2.1 **输入**

1.2.1.1 **输入文件选择**

- BiG-SCAPE 2 主要设计用于处理经 antiSMASH 处理的 .gbk 文件，会在 --input-dir 或 --gbk-dir 目录（包括子目录）中查找这些文件。
- **输入文件选择默认规则**：默认情况下，BiG-SCAPE 2 仅识别名称中包含有 cluster（antiSMASH 4）或 region（antiSMASH 5+）字符串的文件，名称中有 final 字符串的文件无法被识别。这些默认设置可通过 --include-gbk 和 --exclude-gbk 参数调整，文件名会与输出和交互式可视化中的 BGC 名称对应。
- **文件名冲突处理**：原则上，若两个不同文件同名，BiG-SCAPE 2 可基于文件内容处理冲突，但强烈建议避免不同文件使用重复名称，因为这可能导致处理和结果解释时混淆，且 Cytoscape 无法处理文件名重复问题，若要导入 BiG-SCAPE 结果，需确保所有文件名称唯一。
- **文件过滤方式**：.gbk 文件还可根据 antiSMASH 类别，利用 --include-class/--category 和 --exclude-class/--category 选项进行过滤；也可根据文本文件中列出的特定 profile hmm 结构域（通常为 PFAM 结构域），通过 --domain-includelist-all/--any 选项进行过滤。

1.2.1.2 **特征解析与输入验证**

- BiG-SCAPE 会解析 .gbk 文件中的 DEFINITION（定义）和 ORGANISM（生物）信息，以便在输出的 .tsv 文件和可视化结果中展示这些内容。其中，ORGANISM 字段还会被用于确定可视化中显示的独特基因组数量。
- 此外，BiG-SCAPE 会解析各种特征，以验证输入文件是否符合 antiSMASH 的正确格式：
- **antiSMASH 4 的 .gbk** **文件**：应包含且仅包含一个 cluster 特征，该特征需带有限定符 product=[class]、note=Cluster number: [number] 以及 contig\_edge=[True/False]。
- **antiSMASH 版本检测**：对于版本 5 及以上的 antiSMASH，由于 .gbk 头文件中包含 COMMENT 字段（示例如下），可实现版本检测：

```Plain Text
COMMENT ##antiSMASH-Data-START##
    Version :: 6.1.1
    ...
##antiSMASH-Data-END##```
- 如果不存在上述 COMMENT 字段，BiG-SCAPE 会将文件解析为 antiSMASH 版本 4。
- **antiSMASH ≥5 的 .gbk** **文件**：应包含且仅包含一个 region 特征，该 region 特征需带有一个或多个 cand\_cluster、protocluster 和 proto\_core 特征。每个这些特征至少应具有如下表格所列的限定符：

```特征（Feature）|region|cand\_cluster|protocluster|proto\_core``` :- | :- | :- | :- |
|限定符（Qualifiers）|region\_number|candidate\_cluster\_number|product|product|
||product|product|protocluster\_number|protocluster\_number|
||candidate\_cluster\_numbers|protoclusters|contig\_edge (bool)||
||contig\_edge (bool)|kind|||
|||contig\_edge|||

1.2.1.3 **使用未经 antiSMASH 处理的 GenBank 文件作为输入文件**

- 原则上，可通过启用 --force-gbk 选项来使用未经 antiSMASH 处理的 .gbk 文件。但 BiG-SCAPE 2 仍要求这些替代的 .gbk 文件包含 CDS 和 Sequence 特征，并且需要调整 --include-gbk 的默认设置，或者在文件名中添加 “region”/“cluster”。
- 若同时提供经 antiSMASH 处理和未经 antiSMASH 处理的 .gbk 文件，并启用 --force-gbk，BiG-SCAPE 会识别每种类型的文件并进行相应解析。
- 实际上，该选项利用了在给定 .gbk 文件中检测不到 antiSMASH 版本，且不存在任何 region 或 cluster 特征的情况，来激活 --force-gbk 解析。同样，上述 antiSMASH 元素的存在会激活 antiSMASH 解析。
- 这意味着，如果提供给 BiG-SCAPE 的是有问题的经 antiSMASH 处理的输出（例如手动修改了 antiSMASH .gbk 文件，使其不再包含所有预期特征），即使启用了 --force-gbk 选项，BiG-SCAPE 仍会对该特定文件报错。
- 需注意，此功能处于测试阶段（beta 状态），尚未经过广泛测试，因此使用时需谨慎，若发现其行为存在问题，请反馈。

1.2.1.4 **处理基因序列相关特征时的一些规则和可配置项**

- **CDS 特征重叠情况**：若两个 CDS（编码序列）特征存在重叠（例如剪接事件），BiG-SCAPE 最多允许重叠部分为最短 CDS 长度的 10%。若检测到重叠部分超过该比例，BiG-SCAPE 会从分析中舍弃较小的那个特征。
- **蛋白质结构域重叠情况**：类似地，若在同一 CDS 内检测到两个蛋白质结构域存在重叠，BiG-SCAPE 最多允许重叠部分为最短结构域长度的 10%，并会保留得分最高的结构域。这些百分比可在 config.yml 文件中进行修改。
- **BGC 长度限制**：生物合成基因簇（BGC）的最小和最大长度也可设定，相关配置在 config.yml 文件的 MIN/MAX\_BGC\_LENGTH 项中。

1.2.1.5 **参考基因簇的使用**

如果需要，BiG-SCAPE 2 可以使用两种参考基因簇类型（经 antiSMASH 处理的）参考：**MIBiG .gbk** 文件和用户定义的**参考 .gbk** 文件。

使用 MIBiG 存储库的方法：要使用 MIBiG 存储库中的文件，请切换 --mibig 选项以确保使用适当的经 antiSMASH 处理的 .gbk 文件。首次执行此操作时，将在 BiG-SCAPE 2 本地目录中下载这些文件（例如 ./bigscape/MIBiG/mibig\_antismash\_4.0.gbk 或 ./microbiome/ens/bigscape/11b/python.11/site-packages/bigscape/MIBiG/mibig\_antismash\_3.1.gbk）。目前仅支持 MIBiG 版本 3.1 和 envs/bigscape/11b 中的这个站点。


自定义 MIBiG .gbk 文件的使用：任何此类自定义 antiSMASH 处理的 MIBiG .gbk 文件集（如文件的子集）也可通过将这些文件放置在 ./bigscape/MIBiG/mibig\_antismash\_[any\_string].gbk 中并使用 --mibig\_version [any\_string] 运行来使用。如果已将 BiG-SCAPE 安装到环境中，此文件夹通常位于 ./microbiome/ens/bigscape/11b/python.11/site-packages/bigscape/...

用户定义参考 .gbk 文件的提供：任何通过 “普通” antiSMASH 运行处理的用户定义参考基因簇 .gbk 文件可通过 -reference\_dir 提供。

旧版本 MIBiG 文件的处理：如果用户想要提供无法从 [dl.secondarymetabolites.org/mibig/repo](https://dl.secondarymetabolites.org/mibig/repo) 获取的（旧版）经 antiSMASH 处理的 MIBiG，并且希望使用内部 antiSMASH 预先处理这些 .gbk 文件，理论上可通过 --mibig\_version 或 --reference\_dir 提供这些 .gbk 文件。

非 antiSMASH 处理的用户定义参考 .gbk 文件的使用：通过切换 --force\_gbk 选项，可以提供非 antiSMASH 处理的用户定义参考 .gbk 文件。尽管如此，BiG-SCAPE 2 仍要求这些 .gbk 文件中存在 cds 和 sequence 特征。

参考 BGC 记录节点的显示：最后，参考 BGC 记录节点在交互式可视化网络中以蓝色边为特征，包含唯一参考 BGC 记录的连通分量以及参考单例，将不会显示在输出交互式可视化或输出 tsv 文件中，也不会保存到数据库中。

1.2.1.6 **使用 Pfam/phmm 数据库进行结构域检测**

- **结构域检测工具与数据库**：BiG-SCAPE 2 使用 phmm（profile hidden Markov model，隐马尔可夫模型）数据库进行结构域检测，借助 HMMER 套件中的 hmmscan 工具来实现。最常用的是 Pfam phmm 数据库，因此 BiG-SCAPE 要求该数据库中的所有 phmm 遵循 Pfam 格式。当前版本的 Pfam 数据库可从指定链接（here）下载。
- **压缩文件处理**：若 .hmm 文件已被压缩，且压缩文件与 Pfam 的 .hmm 文件位于同一文件夹，BiG-SCAPE 会使用这些压缩文件；若不满足该情况，BiG-SCAPE 会运行 hmmpress（这要求用户对指定的 Pfam 文件夹有写入权限）。
- **自定义数据库**：原则上，只要遵循 Pfam 格式，用户可以定义任何给定的 phmm 数据库。
- **注意事项**：BiG-SCAPE 2 目前还不能处理在同一个 SQLite 数据库中存储多个 phmm 数据库的运行情况，因此建议每当用户想要使用不同的 phmm 数据库时，都从一个全新的 SQLite 数据库开始。

1.2.2 **输出文件**

` `**BiG-SCAPE 2** 的输出文件夹结构可分为以下几类：

- **日志文件**：包含 .log 和 .config.log 文件。
- **SQLite 数据库**：以 [parent\_folder\_name].db 命名，存储所有记录数据，可用于后续运行。它还额外存储所有生成的记录对之间的边，以及所有使用过它的运行中的 GCF（基因簇家族）分配。
- **主交互可视化文件**：即 [output\_dir]/index.html 文件，承载完整的交互式可视化。可通过点击 index.html 文件或用任意网页浏览器打开该文件来启动交互式输出。该文件位于输出文件夹的根目录，打开可视化页面时，会要求加载结果数据库文件，此文件也在输出文件夹的根目录，与 index.html 文件位置相同。由于 index.html 文件本身不包含任何运行数据（它从选定的数据库加载数据），所以任何运行的 index.html 文件都可以与任何结果数据库一起使用。
- **其他输出文件**：存储在 output\_files 中，以及每个相关的 /run\_cutoff/ 文件夹中，包括：
- GCF 树的 .newick 文件，以及用于构建这些树的 fasta 比对文件。
- 每个相关 run/cutoff 对应的 .network.tsv 文件，可导入到外部网络可视化软件（如 Cytoscape，见教程）。本质上，该文件包含一个边列表，带有多个节点和边属性，如 BGC 记录名称、记录类型、记录编号、antiSMASH 可比较区域坐标、BiG-SCAPE 距离和距离成分（DSS、Jaccard 和邻接指数）、比对模式、延伸策略等。
- 每个相关 run/cutoff 对应的 .topology.network.tsv 文件（当记录类型不是 region 时），这是一个边列表，其中节点和边是拓扑链接，允许在 Cytoscape 等第三方软件中查看和加载拓扑链接/边。
- 带有 BGC -> GCF 分配的 clustering\_[cutoff].tsv 文件。
- record\_annotations.tsv 文件，包含关于输入中成功处理的每个 BGC 的信息，包括 BGC 记录名称、记录类型、记录编号、antiSMASH 类别和分类、生物、分类学、.gbk 文件中的描述特征等。
- 每个运行对应的 full\_network.tsv 文件，包含应用任何截断之前的“原始”距离（相当于运行 GCF 截断为 1.0 的 BiG-SCAPE 2）。

1.2.3 **交互式可视化输出功能**

用户可通过启动主输出文件 [output\_dir]/index.html 访问交互式界面（UI），启动后需选择一个 SQLite 数据库文件读取。加载数据库后，能在该界面中浏览数据，界面包含以下元素（如图 2 所示）：

![...](..\..\0.%20软件教程\生物信息学工具（Linux）\images\BIG-SCAPE：安装及使用教程.001.png)

1. **主题选择**：有自动（Auto）、浅色（Light）、深色（Dark）三种主题可选。
2. **分类选择**：下拉菜单内容取决于是否使用了分类模式。
3. **数据库选择**。
4. **运行选择**：下拉菜单会显示所有运行过且保存到已加载数据库中的 run\_cutoff（如 run\_1\_cutoff\_0.3, run\_1\_cutoff\_0.5 等）。
5. **概览部分**：位于页面顶部，可通过“Overview”按钮重新定位。
- **运行信息部分**：展示当前所选运行使用的模式和参数。
- **输入数据部分**：包含基因组总数、BGC（生物合成基因簇）总数，以及每个基因组中 BGC 分布和 antiSMASH 类别信息。
- **GCF/基因组概览部分**：提供关于 GCF（基因簇家族）特征的信息，还有一个 GCF/基因组热图，该热图仅根据匹配特征的相似度比较，不使用正式分类法。
6. **网络部分**：可通过页面底部的按钮导航。
- **连通分量（CC）表格**：列出所有 CC 及其对应的家族和记录数量，可利用筛选字段（接受多个描述符）进行过滤，选中后可通过“Download Current Selection”按钮下载。
- **网络视图**：选择特定 CC 后，该 CC 的节点和边会加载显示，也可使用“Visualize All”按钮查看整个数据集的节点和边（但大型数据集这样做计算量可能很大）。
- 在参考模式下，相关节点会用蓝色圈出。
- 在查询模式下，查询节点会用绿色圈出。
- 当记录类型为 Protocluster 或 Protcore 时，拓扑连通分量中的节点会变浅。
- 节点可通过手动点击或利用“高级搜索”功能在已加载网络中搜索/过滤，搜索结果可下载为节点 .tsv 文件和包含所选节点间所有边的边 .tsv 文件。
- **节点与 GCF 详情部分**：
- 节点可通过悬停和点击选中，会显示在该部分。上半部分是 BGC 及其所属家族的直观表示（可展开），下半部分列出所选 BGC 及其所属家族。
- 点击“Node&GCF Detail”中的 GCF 会触发弹出窗口，显示 GCF 树，点击树中节点会显示该节点所有成员的窗口。悬停在 GCF 树的结构域上会显示其在 BGC 中的 accession、名称、得分和在开放阅读框（ORF）内的位置；悬停在每个 ORF 上会显示其在 BGC 中的位置。
- 当记录类型为 Protocluster 或 Protcore 时，会显示完整的 .gbk 文件，不属于相关记录的结构域/ORF 会变浅。

1.3 **Query 功能**

BiG-SCAPE 2 的查询工作流程旨在方便搜索与用户提供的查询 BGC（生物合成基因簇）.gbk 文件相似的 BGC。

在该模式下，用户必须提供查询 BGC .gbk 文件的路径，该文件可位于 /input\_dir 或其他任何位置。所有位于 /input\_dir 中的其余 BGC 都将被 BiG-SCAPE Query 视为参考序列。此外，还可使用 MIBiG 参考序列和其他用户定义的参考序列，使用方式与 BiG-SCAPE Cluster 中相同。

默认情况下，BiG-SCAPE 2 会执行一组“查询与所有（序列）”的比较。或者，使用 --propagate 参数时，在这第一组比较之后，会进行一组迭代的“参考与参考（序列）”比较，这会传播连通分量，直到不再创建新的边。最后，在这两种情况下，都会计算新连接的参考节点之间的任何缺失的边。

其他输入和输出特征与 BiG-SCAPE Cluster 一致。


1.4 **运行参数**

1.4.1 **所有模式通用的命令行参数**

1. -v, --verbose
- 作用：打印分析过程中每个步骤更详细的信息，输出各种日志（包括调试日志信息），并写入日志文件。
- 使用方式：启用该选项可激活详细日志输出。

2. --quiet
- 作用：不向输出端打印任何日志信息，仅将日志写入日志文件。

3. -l, --label
- 作用：为输出结果文件夹名称以及可视化页面中的下拉菜单添加运行标签。
- 默认情况：BiG-SCAPE 运行的名称默认格式为 [label]\_YYYY-MM-DD\_HH-MM-SS。

4. -o, --output-dir
- 作用：指定所有 BiG-SCAPE 结果文件的输出目录。
- 更多细节：可点击“here”链接查看更详细的说明。

5. --log-path
- 默认值：output\_dir/timestamp.log（output\_dir 为指定的输出目录，timestamp 为时间戳）。
- 作用：指定输出日志文件的路径。

1.4.2  **Cluster（聚类）、Query（查询）和 Dereplicate（去重复）模式通用的命令行参数**

\1. -i, --input-dir, --gbk\_dir

- 作用：指定包含供 BiG-SCAPE 使用的 .gbk 文件的输入目录。
- 说明：重复的文件名可以处理，但不推荐。更多细节可点击“here”链接查看。

\2. --config-file-path

- 作用：指定 BiG-SCAPE 的 config.yml 文件路径，该文件存储了一系列高级使用参数的值。
- 默认值：bundled bigscape/config.yml（即 BiG-SCAPE 自带的配置文件）。

\3. -c, --cores

- 默认值：使用所有可用的核心。
- 作用：设置可用的最大核心数。BiG-SCAPE 会尝试对分析中的一些步骤（如结构域预测和距离计算）进行并行化处理。使用此选项可设置脚本可使用的核心数，若未指定，BiG-SCAPE 将使用所有可用核心。

\4. --input-mode

- 选项："recursive"（递归）、"flat"（平面）。
- 默认值：recursive。
- 作用：告知 BiG-SCAPE 在哪里查找输入 .gbk 文件。recursive 表示在输入目录中递归搜索 .gbk 文件；flat 表示仅在输入目录中搜索 .gbk 文件。

\5. --include-gbk

- 默认值：cluster, region。
- 作用：由逗号分隔的字符串列表。只有文件名中包含该列表中字符串的 .gbk 文件才会被用于分析。使用星号（\*）表示接受所有文件（\* 会覆盖 --exclude-gbk）。

\6. --exclude-gbk

- 默认值：final。
- 作用：由逗号分隔的字符串列表。如果文件名中包含该列表中的任何字符串，该文件将不被用于分析。

1.4.3  **Cluster（聚类）和 Query（查询）模式通用的命令行参数**

1. --profiling
- 作用：运行分析器并输出性能分析报告。
- 注意：目前仅在 Linux 系统上可用。
2. -m, --mibig-version
- 作用：指定 MIBiG（Minimum Information about a Biosynthetic Gene cluster）的版本号（从 3.1 及以上版本）。
- 说明：如果不提供该参数，MIBiG 基因簇将不包含在分析中。如果需要，BiG-SCAPE 会将经 antiSMASH 处理的 MIBiG 数据库下载到 ./bigscape/MIBiG/mibig\_antismash\_<version>.gbk。对于高级用户，只要存在预期的文件夹，任何自定义（经 antiSMASH 处理的）MIBiG 集合都可以使用，例如提供 -m mymibig 并配合 ./bigscape/MIBiG/mibig\_antismash\_mymibig.gbk。更多细节可点击“here”链接查看。

3. -r, --reference-dir
- 作用：指定包含用户定义的、非 MIBiG 的、经 antiSMASH 处理的参考基因簇的目录路径。更多细节可点击“here”链接查看。

4. -p, --pfam-path
- 作用：指定 Pfam 数据库 .hmm 文件（如 Pfam-A.hmm）的路径。
- 说明：如果 .hmm 文件已经被压缩，且压缩文件与 Pfam 的 .hmm 文件位于同一文件夹，BiG-SCAPE 会使用这些压缩文件；如果不满足该情况，BiG-SCAPE 会运行 hmmpress（这要求用户对指定的 Pfam 文件夹有写入权限）。

5. --domain-includelist-all-path
- 作用：指定包含 phmm 结构域访问号（通常是 Pfam 访问号，如 PF00501）的 .txt 文件路径。只有包含所有列出的访问号的区域才会被分析。
- 说明：在该文件中，每行包含一个单独的 phmm 结构域访问号（可带有可选注释，用制表符分隔），以 # 开头的行会被忽略，结构域访问号区分大小写，且不能与 --domain-includelist-any-path 同时使用。

6. --domain-includelist-any-path
- 作用：指定包含 phmm 结构域访问号（通常是 Pfam 访问号，如 PF00501）的 .txt 文件路径。只有包含列出的任何一个访问号的 BGC 才会被分析。
- 说明：在该文件中，每行包含一个单独的 phmm 结构域访问号（可带有可选注释，用制表符分隔），以 # 开头的行会被忽略，结构域访问号区分大小写，且不能与 --domain-includelist-all-path 同时使用。

7. --legacy-weights
- 作用：在距离计算中使用 BiG-SCAPE 1 基于类别的权重。
- 说明：如果不选择该选项，距离度量将基于“mix”权重（混合权重）。警告：这些权重仅对“region”记录类型验证过，对于其他记录类型（可通过 --record\_type 选项设置）未验证，更多细节可点击“here”查看。

8. --alignment-mode
- 默认值：global。
- 选项：global、glocal、local、auto。
- 作用：每对基因簇的比对模式。
- global：比较每个 BGC 记录的整个结构域列表。
- glocal：先找到两个记录之间的最长公共子簇（LCS），然后扩展每一侧（见 --extend-strategy）。
- local：通过尝试找到最长的公共结构域内容片段（最长公共子簇，LCS）来计算距离，然后扩展每一侧（见 --extend-strategy）。
- auto：当每对中的至少一个 BGC 有来自 antiSMASH v4+ 的 contig\_edge 注释时，使用 local 模式；否则，对该对使用 global 模式。更多细节可点击“here”查看。

9. --extend-strategy
- 默认值：legacy。
- 选项：legacy、greedy、simple match。
- 作用：扩展 BGC 记录对可比较区域的策略。
- legacy：使用原始 BiG-SCAPE 的扩展策略。
- greedy 和 simple match：是 BiG-SCAPE 2 新引入的。legacy 和 simple match 都会检查 BGC 的结构域架构，greedy 是一种非常简单的方法，以最外侧匹配结构域的坐标作为扩展边界。更多细节可点击“here”查看。

10. --gcf-cutoffs
- 默认值：0.3。
- 作用：生成家族前应用的距离截断值的逗号分隔列表。每次运行可提供一个或多个值。如果提供多个截断值，BiG-SCAPE 将为每个距离截断值生成一个网络。值应在 (0.0, 1.0] 范围内。例如（提供多个截断值）：--gcf-cutoffs 0.1,0.2,0.3,0.5,1.0。更多细节可点击“here”查看。

11. --profile-path
- 默认值：output\_dir/.（输出目录下）。
- 作用：指定输出性能分析文件的路径。

12. -db, --db-path
- 默认值：output\_dir/data\_sqlite.db（输出目录下的 data\_sqlite.db 文件）。
- 作用：指定 SQLite 数据库输出文件的路径。

13. --record-type
- 选项：region、cand\_cluster、protocluster、proto\_core。
- 默认值：region。
- 作用：使用特定类型的 antiSMASH 记录进行比较。对于每个 .gbk 文件，BiG-SCAPE 会尝试提取请求的记录类型，如果不存在，会尝试提取下一个更高级别的记录类型（记录类型的层次结构为：region > cand\_cluster > protocluster > proto\_core）。更多细节可点击“here”查看。

14. --no-db-dump
- 作用：直到运行结束时才将 SQLite 数据库转储到磁盘。这会加快运行速度，但如果运行崩溃，将不会存储任何信息，需要从头重新启动运行。

15. --db-only-output
- 作用：除了存储在 SQLite 数据库中的数据外，不生成任何其他输出。适用于只希望使用存储在 SQLite 数据库中结果的高级用户。

16. --no-trees
- 作用：不生成任何 GCF（基因簇家族）的 Newick 树。适用于不使用输出可视化，只使用输出 .tsv 文件（包括网络文件）和/或 SQLite 数据库中存储结果的用户。

17. --force-gbk
- 适用人群：仅推荐高级用户使用。
- 作用：允许 BiG-SCAPE 使用未经 antiSMASH 处理的 .gbk 文件。如果发现没有 antiSMASH 注释的 .gbk 文件（具体来说，BiG-SCAPE 会检查是否缺少 antiSMASH 版本特征），BiG-SCAPE 仍会读取和解析这些文件，并创建内部 .gbk 记录对象，每个对象都有一个覆盖整个序列长度的 region 特征和一个 product 特征（值为 other）。
- 警告：BiG-SCAPE 仍然需要 CDS 特征和序列特征才能处理非 antiSMASH 的 .gbk 文件。此外，如果 .gbk 文件名也不遵循 antiSMASH 格式，--include-gbk 和 --exclude-gbk 参数可能需要调整。免责声明：此功能仍在开发中，使用需自行承担风险。

1.4.4 **聚类（Cluster）模式特有的参数：**

1. --mix
- 作用：使用“mix”分组计算距离，其中不应用任何分类。这会对所有输入的 BGC（生物合成基因簇）记录进行全对全（all - vs - all）比较。
- 权重分布：该分组使用“mix”权重分布，即 {JC: 0.2, AI: 0.05, DSS: 0.75, Anchor boost: 2.0}。更多细节可点击“here”查看。

2. --classify
- 选项：none、class、category、legacy。
- 默认值：category。
- 作用：定义 BiG-SCAPE 应使用哪种方法将 BGC 记录划分为分析组。
- --classify class 和 --classify category 分别使用 antiSMASH/BGC 类别（如 T2PKS）或分类（如 PKS）对基于类别/分类的组进行分析。
- --classify legacy 基于 BiG-SCAPE v1 预定义的组（PKS1、PKSOther、NRPS、NRPS-PKS-hybrid、RiPP、Saccharide、Terpene、Others），并会自动配合 --legacy-weights 使用。--classify legacy 用于与 antiSMASH 版本 up to 7 生成的输入 .gbk 文件向后兼容。对于更高版本的 antiSMASH，使用时需自行承担风险，因为 BGC 类别可能已改变。所有该旧版模式无法识别的 antiSMASH 类别都会被归到“others”组中。若要自行更新 antiSMASH 类别列表，可查看 config.yml 文件。
- 组合使用：--classify class 和 --classify category 可与 --legacy-weights 结合使用（若输入 .gbk 文件由 antiSMASH 版本 6 或更高版本生成）。对于较旧版本的 antiSMASH，可使用 --classify legacy，或不选择 --legacy-weights（此时将基于通用的“mix”权重进行加权距离计算）。

3. --hybrids-off
- 作用：启用后，将具有混合预测类别/分类的 BGC 记录添加到每个子类中，而不是添加到混合类/网络中（例如，一个 terpene-nrps BGC 会被添加到 terpene 和 nrps 类别/网络中，而不是 terpene.nrps 网络中）。
- 限制：仅在选择了任何 --classify 模式时有效。

4. --exclude-categories
- 作用：指定一个由逗号分隔的 antiSMASH 产物类别列表。具有该列表中至少一个产物类别的 BGC 将被排除在比较之外（例如，NRPS,PKS 会排除所有 NRPS 或 PKS 类的 BGC 记录，甚至像 NRPS-terpene 这样的杂合类也会被排除）。
- 限制：仅适用于由 antiSMASH 版本 6 或更高版本生成的 .gbk 文件。

5. --include-categories
- 作用：指定一个由逗号分隔的 antiSMASH 产物类别列表。只有具有该列表中至少一个产物类别的 BGC 才会被包含在比较中（例如，NRPS 只会包含 NRPS 类的 BGC 记录，包括像 NRPS-PKS 这样的杂合类）。
- 限制：仅适用于由 antiSMASH 版本 6 或更高版本生成的 .gbk 文件。

6. --exclude-classes
- 作用：指定一个由逗号分隔的 antiSMASH 产物类列表。具有该列表中至少一个产物类的 BGC 记录将被排除在比较之外（例如，T1PKS,T2PKS 会排除所有 T1PKS 和 T2PKS 类的 BGC 记录，甚至像 NRPS-T1PKS 这样的杂合类也会被排除）。

7. --include-classes
- 作用：指定一个由逗号分隔的 antiSMASH 产物类列表。只有具有该列表中至少一个产物类的 BGC 才会被包含在比较中（例如，T1PKS 只会包含 T1PKS 类的 BGC 记录，包括像 NRPS-T1PKS 这样的杂合类）。

8. --include-singletons
- 作用：在网络和所有相应的输出中包含单例（singletons，即不与其他 BGC 形成连通分量的单独 BGC）。
- 限制：即使启用该选项，参考单例也不会被包含。

1.4.5 **查询（Query）模式特有的参数**

1. -q, --query-bgc-path
- 作用：指定查询用的 .gbk 文件路径。BiG-SCAPE 会以“一对多（one - vs - all）”的模式，将输入和参考文件夹中的所有 BGC（生物合成基因簇）记录与该查询记录进行比较。

2. -n, --query-record-number
- 作用：查询 BGC 记录编号。用于从查询 BGC 的 .gbk 文件中选择特定的记录，仅在运行 --record-type cand\_cluster、protocluster 或 proto\_core 时相关。
- 警告：如果交错或化学杂合的原始簇/核心被合并（见配置文件），相关编号是合并簇的第一条记录的编号（编号最小的那条）。例如，如果记录 1 和 2 被合并，相关编号为 1。

3. --propagate
- 作用：默认情况下，BiG-SCAPE 只会在查询和参考 BGC 记录之间生成边。使用 --propagate 标志后，BiG-SCAPE 会经过多轮边生成循环，直到没有新的参考 BGC 连接到查询的连通分量。更多细节可点击“here”查看。

4. --classify
- 选项：none、class、category。
- 默认值：none。
- 作用：默认情况下，BiG-SCAPE 会将查询 BGC 记录与所有其他提供的参考 BGC 记录进行比较，无论它们的 antiSMASH 产物类/分类如何。选择 class 或 category 后，会对特定类别的组进行分析，此时只有与查询记录具有相同类/分类的参考 BGC 记录会被比较。可与 --legacy-weights 结合使用（适用于由 antiSMASH 版本 6 或更高版本生成的 .gbk 文件）。对于较旧版本的 antiSMASH，或未选择 --legacy-weights 时，BiG-SCAPE 会使用通用的“mix”权重：{JC: 0.2, AI: 0.05, DSS: 0.75, Anchor boost: 2.0}。

1.4.6 **去重复（Dereplicate）模式特有的参数**

1. --cutoff
- 作用：设置 Sourmash 距离的相似度阈值。
- 说明：只有相似度大于或等于该阈值的序列对才会被考虑用于聚类。

1.4.7 **基准测试（Benchmark）模式特有的参数**

1. --GCF-assignment-file
- 作用：指定 GCF（Gene Cluster Family，基因簇家族）分配文件的路径。
- 说明：BiG-SCAPE 会将运行输出与该文件中的 GCF 分配情况进行比较，用于评估聚类结果的准确性等基准测试相关操作。

2. --BiG-dir
- 作用：指定 BiG-SCAPE（v1/v2 版本）或 BiG-SLICE（v1/v2 版本）输出目录的路径。
- 说明：在基准测试模式下，该目录中的输出结果会被用于相关的比较或分析等操作。

\2. **BIG-SCAPE 安装**

2.1 **前期准备**

- Ubuntu 中 conda 安装：[Ubuntu系统安装 Conda](https://www.yuque.com/dviy1p/zfgvwt/bw82kar2an5gmce0)
- Python 3.11 或更高版本

2.2 **安装包准备**

2.2.1  **git 仓库克隆**

此方法需要要求在 Ubuntu 中安装 git，如果 ubuntu 系统上没安装 git，可以考虑第二种方法。

2.2.2 **官网下载安装包**

1. 进入 BIG-SCAPE 官网：<https://github.com/medema-group/BiG-SCAPE>
2. 点击框中的 code，选择 `Download ZIP`，即可下载软件安装包

![...](..\..\0.%20软件教程\生物信息学工具（Linux）\images\BIG-SCAPE：安装及使用教程.002.png)

3. 将安装包复制到 Ubuntu 系统桌面，并解压安装包，即可完成准备工作

2.3 **正式安装**

1. 进入解压后的安装包，打开终端，输入以下命令

```Markdown
# 使用 conda 包管理器来创建一个新的环境
conda env create -f environment.yml```


```环境是一种隔离的运行空间，可以用来安装特定版本的软件包，而不会影响到系统中其他环境的软件包。这里使用 -f environment.yml 参数，表示根据 environment.yml 文件中的配置来创建环境。environment.yml 文件通常包含了环境中需要安装的软件包的名称、版本等信息，通过这个文件可以确保创建的环境具有正确的依赖关系。```

2. 激活刚才创建的名为 “bigscape” 的环境

```Markdown
# 激活刚才创建的名为 “bigscape” 的环境
 conda activate bigscape```


```激活环境后，后续在这个环境中安装的软件包和执行的操作都将在这个隔离的环境中进行，而不会影响到系统中的其他环境。```

3. 使用 pip 来安装 BiG-SCAPE 2

```Markdown
# 使用 pip 来安装 BiG-SCAPE 2
pip install```


```在前面的步骤中已经创建并激活了环境，现在在这个环境中使用 pip 安装 BiG-SCAPE 2，这样就可以在该环境中使用 BiG-SCAPE 2 了。```

4. 出现下面提示，则证明安装完成

![...](..\..\0.%20软件教程\生物信息学工具（Linux）\images\BIG-SCAPE：安装及使用教程.003.png)

5. 验证 BIG-SCAPE 是否安装成功

```Markdown
# 验证 BIG-SCAPE 是否安装成功
bigscape --help```


```这表示安装完成后，用户可以在任何地方运行 BiG-SCAPE 2。bigscape --help 是一个命令，用于显示 BiG-SCAPE 2 的帮助信息，帮助用户了解如何使用 BiG-SCAPE 2 的各种功能和参数。```
![...](..\..\0.%20软件教程\生物信息学工具（Linux）\images\BIG-SCAPE：安装及使用教程.004.png)

\3.  **BIG-SCAPE 使用**

3.1 **下载 Pfam 文件**

1. 进入 Interfro 官网，下载 Pfam-A.hmm 文件

InterPro：https://www.ebi.ac.uk/interpro/download/Pfam/

![...](..\..\0.%20软件教程\生物信息学工具（Linux）\images\BIG-SCAPE：安装及使用教程.005.png)

2. 解压下载好的 Pfam-A.hmm 压缩包。
3. 将 Pfam-A.hmm 文件置于 /home/lhc/Desktop/BiG-SCAPE-master/big\_scape/hmm/ 路径中。

3.2 **准备参考基因簇文件**

1. 进入 MIBiG 官网，下载 gbk 格式的基因簇文件

https://mibig.secondarymetabolites.org/download

![...](..\..\0.%20软件教程\生物信息学工具（Linux）\images\BIG-SCAPE：安装及使用教程.006.png)

2. 将下载好的 gbk 文件放置在 ./big\_scape/MIBiG/ 文件夹中。

![...](..\..\0.%20软件教程\生物信息学工具（Linux）\images\BIG-SCAPE：安装及使用教程.007.png)

3.3 **准备输入文件**

1. 将 antiSMASH 预测生成的基因簇 .gbk 文件放置在./big\_scape/file\_input/ 文件夹中。

![...](..\..\0.%20软件教程\生物信息学工具（Linux）\images\BIG-SCAPE：安装及使用教程.008.png)


3.4 **运行 Bigscape** 

1. ` `激活 bigscape 环境

```Markdown
# 激活 bigscape 环境
conda activate bigscape```


```每次重新进入 Linux 系统时，输入该命令，即可重新激活 bigscape 环境```

2. 运行 bigscape

```Markdown
# 运行 bigscape 
bigscape cluster --input-dir file\_input/ --output-dir output --reference-dir MIBiG --pfam-path /home/lhc/Desktop/BiG-SCAPE-master/big\_scape/hmm/Pfam-A.hmm --mix --gcf-cutoffs 0.8,1 --record-type protocluster --label protocluster```
- **bigscape cluster**核心指令，指定运行 BiG-SCAPE 的“聚类”模式，用于将输入的生物合成基因簇（BGC）聚类为基因簇家族（GCF）。
- **--input-dir file\_input/**指定输入目录为 file\_input/，该目录需包含经 antiSMASH 处理的 .gbk 文件（如 PKS 或 PKS 杂合基因簇的注释结果），是分析的核心数据来源。
- **--output-dir output**指定输出目录为 output，所有分析结果（如日志、聚类网络文件、可视化数据、SQLite 数据库等）将保存在此目录。
- **--reference-dir MIBiG**指定参考基因簇目录为 MIBiG，该目录通常包含经 antiSMASH 处理的 MIBiG 数据库基因簇（已知的生物合成基因簇），用于与输入的基因簇进行比较分析。
- **--pfam-path /home/.../Pfam-A.hmm**指定 Pfam 数据库文件（Pfam-A.hmm）的绝对路径，BiG-SCAPE 依赖该数据库进行蛋白质结构域的识别和比对，是基因簇相似性计算的关键依据。
- **--mix**启用“混合模式”，对所有输入的 BGC 进行全对全（all-vs-all）比较，不基于 antiSMASH 的类别/分类进行分组过滤，适合分析跨类别的基因簇关系（如 PKS 与其他类型的杂合簇）。
- **--gcf-cutoffs 0.8,1**设置基因簇家族（GCF）的距离截断值为 0.8 和 1.0（范围 (0,1]）。BiG-SCAPE 会为每个截断值生成独立的聚类网络：  
- 截断值越高（如 1.0），允许的基因簇间差异越大，同一 GCF 包含的成员更广泛；  
- 截断值较低（如 0.8），则对相似性要求更严格，GCF 成员更相似。
1. **--record-type protocluster**指定使用 antiSMASH 注释中的 protocluster 层级记录进行分析（而非默认的 region）。protocluster 是更精细的预测基因簇单元，适合关注核心合成基因的场景。
2. **--label protocluster**为此次运行添加标签“protocluster”，便于在输出目录名称和可视化界面中快速识别该次分析（尤其当多次运行时，可通过标签区分参数差异）。

**命令整体作用**

该命令将以 file\_input/ 中的基因簇（如 PKS 及杂合簇）为输入，结合 MIBiG 参考基因簇和指定的 Pfam 数据库，采用旧版权重计算方式，在“混合模式”下对 protocluster 层级的记录进行全对全比较，分别以 0.8 和 1.0 的截断值生成聚类结果，最终输出到 output 目录，并标记为“protocluster”以便区分。

适合用于探索 PKS 相关基因簇的家族关系，尤其是需要兼顾跨类别比较和不同严格度聚类结果的场景。


