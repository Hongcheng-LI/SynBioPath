
**MestreNova 12.0：核磁谱图处理**

```本教程旨在为大家介绍如何利用 MestreNova 对得到的核磁数据进行处理，为后续的解谱过程和文章发表提供便利。```


```<p>**前期准备**：</p><p>软件：MestreNova 12.0 及以上版本</p><p>数据：全部核磁数据，包括一维（1H，13C）及二维（HSQC，H-H COSY，HMBC，NOESY）。</p><p></p>```



\1. **数据导入**

1：打开 MestreNova 12.0 软件，将测试得到的谱图拖入软件中，从而打开相应的核磁数据。

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.001.png)

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.002.png)

\2. **一维谱图处理**

2.1 **1H NMR** 

2.1.1 **属性调整**

1. 双击鼠标左键或单击鼠标右键，选择属性（Properties），打开属性面板。

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.003.png)

2. General：取消勾选 Title

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.003.png)

3. 调整 Grid
- 取消勾选 Show Horizontal
- 取消勾选 Show Vertical
- 取消勾选 Show Frame

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.004.png)

4. 调整 1D
- Color：选择蓝色（blue）
- Line Width：改为 4

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.003.png)

5. 调整 Scales：
- 字体：Arial；粗细：Bold；字号：12 号
- Horizontal：不做调整
- Vertical：取消勾选

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.003.png)

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.005.png)

6. Peaks
- Label：勾选
- 颜色：red
- 字体：Arial；粗细：Bold；字号：12 号
- Decimals（小数位数）：4
- 其余皆为默认

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.005.png)

7. Integrals
- Label 颜色：red
- 字体：Arial；粗细：Bold；字号：12 号
- Decimals（小数位数）：2
- Curve color：red
- 其余皆为默认

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.005.png)

8. 点击 Ok，即可得到调整好的 1H NMR 谱图。

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.006.png)

2.1.2 **相位调整**

1. 点击工具栏中的 Phase correction，选择 Automatic，即可得到相位校正后的 1H NMR 谱图。

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.007.png)

2.1.3 **基线调整**

1. 点击工具栏中的 Baseline correction，即可得到基线校正后的 1H NMR 谱图。

2.1.4 **定标（校正化学位移）**

1. 点击工具栏中的 reference，选中谱图中的溶剂峰，输入溶剂峰的正确化学位移，即可得到化学位移校正之后的 1H NMR 谱图。

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.007.png)

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.008.png)

2. 如果不确定该样品用什么溶剂溶解，可点击菜单栏中的 View，选择其中的 Table 选项，之后在弹出的窗口中选中 Common 中的 Parameters，点击 OK，在弹出的窗口中即可看到样品所用的溶剂。

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.008.png)

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.008.png)

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.009.png)

3. 如果不确定溶剂峰的具体化学位移，在 reference 界面，选择 Solvents，即可找到相应溶剂的正确化学位移，选中之后，点击 OK，即可得到化学位移校正之后的 1H NMR 谱图。

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.010.png)

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.010.png)

2.1.5 **标峰（标注化学位移）**

1. 点击工具栏中的 Peaks Picking，选择 Peak by Peak，在目标峰的峰尖处点击，即可标注出该峰的化学位移。若出现错误标注，点击工具栏中的 Peaks Picking，选择 delete manually，拖动选中错误标注的目标峰，即可删除错误标注。

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.011.png)

2.1.6 **积分（标注目标峰的峰面积）**

1. 点击工具栏中的 Integration，选择 Manual，选择低场处氢数目可能为 1 峰（5-8 ppm）进行积分，将该峰的峰面积定为 1，之后对其他的峰进行积分时，将会以该峰的峰面积为基准。若出现错误积分，点击工具栏中的 Integration，选择 delete manually，拖动选中错误积分的目标峰，即可删除错误积分。

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.012.png)

2. 此时，1H NMR 已处理完成。

2.2 **13C**

2.2.1 **属性调整**

1. 双击鼠标左键或单击鼠标右键，选择属性（Properties），打开属性面板。

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.003.png)

2. General：取消勾选 Title

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.003.png)

3. 调整 Grid
- 取消勾选 Show Horizontal
- 取消勾选 Show Vertical
- 取消勾选 Show Frame

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.004.png)

4. 调整 1D
- Color：选择蓝色（blue）
- Line Width：改为 4

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.003.png)

5. 调整 Scales：
- 字体：Arial；粗细：Bold；字号：12 号
- Horizontal：不做调整
- Vertical：取消勾选

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.003.png)

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.005.png)

6. Peaks
- Label：勾选
- 颜色：red
- 字体：Arial；粗细：Bold；字号：12 号
- Decimals（小数位数）：4
- 其余皆为默认

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.004.png)

7. 点击 Ok，即可得到调整好的 13C NMR 谱图。

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.013.png)

2.2.2 **相位调整**

1. 13C NMR 谱图中，所有的碳均朝上，一般不需要调整相位。

2.2.3 **基线调整**

1. 点击工具栏中的 Baseline correction，即可得到基线校正后的 13C NMR 谱图。

2.2.4 **定标（校正化学位移）**

1. 点击工具栏中的 reference，选中谱图中的溶剂峰，输入溶剂峰的正确化学位移，即可得到化学位移校正之后的 13C NMR 谱图。

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.008.png)

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.008.png)

2. 如果不确定溶剂峰的具体化学位移，在 reference 界面，选择 Solvents，即可找到相应溶剂的正确化学位移，选中之后，点击 OK，即可得到化学位移校正之后的 13C NMR 谱图。

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.010.png)

2.2.5 **标峰（标注化学位移）**

1. 点击工具栏中的 Peaks Picking，选择 Peak by Peak，在目标峰的峰尖处点击，即可标注出该峰的化学位移。若出现错误标注，点击工具栏中的 Peaks Picking，选择 delete manually，拖动选中错误标注的目标峰，即可删除错误标注。

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.014.png)

2. 此时，13C NMR 已处理完成。

2.3 **DEPTQ**

2.3.1 **属性调整**

1. 双击鼠标左键或单击鼠标右键，选择属性（Properties），打开属性面板。

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.003.png)

2. General：取消勾选 Title

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.003.png)

3. 调整 Grid
- 取消勾选 Show Horizontal
- 取消勾选 Show Vertical
- 取消勾选 Show Frame

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.004.png)

4. 调整 1D
- Color：选择蓝色（blue）
- Line Width：改为 4

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.004.png)

5. 调整 Scales：
- 字体：Arial；粗细：Bold；字号：12 号
- Horizontal：不做调整
- Vertical：取消勾选

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.003.png)

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.005.png)

6. Peaks
- Label：勾选
- 颜色：red
- 字体：Arial；粗细：Bold；字号：12 号
- Decimals（小数位数）：4
- 其余皆为默认

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.004.png)

7. 点击 Ok，即可得到调整好基本参数的 DEPTQ 谱图。

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.008.png)

2.3.2 **相位调整**

1. DEPTQ 谱图中，有以下三个特征
- 溶剂峰朝下
- 亚甲基（CH2）和季碳（C）朝下
- 甲基（CH3）和次甲基（CH）朝上

2. 若选择使用自动调整相位，会使溶剂峰朝上，使我们无法准确的判断出 DEPTQ 谱中碳的类型，因此一般需要手动调整相位。

3. 点击工具栏 Phase correction 中的 Manual correction，会弹出一个窗口。

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.002.png)

4. 在弹出窗口的红色区域，摁住鼠标左键向下滑动，此时溶剂峰会逐渐向下，不断滑动直到溶剂峰完全朝下。

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.002.png)

5. 此时，大部分碳都已经完全朝上或朝下，但仍有部分碳同时存在朝上和朝下的峰，因此需要进一步调整相位。

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.001.png)

6. 摁住鼠标右键，向上或向下持续滑动鼠标，直至所有的目标峰都正确的朝上或朝下，即可得到相位校正后的 DEPTQ 谱图。

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.001.png)

7. 判断依据：

（1）高场区的甲基碳朝上

（2）低场区的季碳朝下

2.3.3 **基线调整**

1. 点击工具栏中的 Baseline Correction，即可得到基线校正后的 DEPTQ 谱图。

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.001.png)

2.3.4 **定标（校正化学位移）**

1. 点击工具栏中的 reference，选中谱图中的溶剂峰，输入溶剂峰的正确化学位移，即可得到化学位移校正之后的 13C NMR 谱图。

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.002.png)

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.001.png)

2. 如果不确定溶剂峰的具体化学位移，在 reference 界面，选择 Solvents，即可找到相应溶剂的正确化学位移，选中之后，点击 OK，即可得到化学位移校正之后的 DEPTQ 谱图。

2.3.5 **标峰（标注化学位移）**

1. 点击工具栏中的 Peaks Picking，选择 Peak by Peak，在目标峰的峰尖处点击，即可标注出该峰的化学位移。若出现错误标注，点击工具栏中的 Peaks Picking，选择 delete manually，拖动选中错误标注的目标峰，即可删除错误标注。

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.001.png)

2. 此时，DEPTQ 已处理完成。

\3. **二维谱图处理**

HSQC、H-H COSY、HMBC 等二维谱图处理过程类似，因此本文以 HMBC 为例讲解二维谱图的处理步骤。

3.1 **导入一维谱图**

1. 有时，二维谱图中缺少一维谱图，因此第一步需要将一维谱图导入。

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.008.png)

2. 点击侧边工具栏中最下方的 Show traces，选择 Show traces，即可在二维谱图中显示一维谱图。

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.008.png)

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.010.png)

3. 显示一维谱图之后，需要重新导入校正之后的一维谱图。点击侧边工具栏中最下方的 Show traces，选择 Setup。在弹出的窗口中选中 Available 1D spectra 中的 1H NMR 谱图，点击 Horizontal traces 中的对号，即可导入校正后的  1H NMR 谱图。

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.008.png)

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.015.png)

4. 同理，在弹出的窗口中选中 Available 1D spectra 中的 13C NMR 谱图，点击 Vertical traces 中的对号，即可导入校正后的  13C NMR 谱图。点击 OK，即可得到导入校正后一维图谱的二维图谱。

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.016.png)

3.2 **属性调整**

1. 双击鼠标左键或单击鼠标右键，选择属性（Properties），打开属性面板。

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.017.png)

2. General：取消勾选 Title

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.017.png)

3. 调整 Grid
- 取消勾选 Show Horizontal
- 取消勾选 Show Vertical
- 取消勾选 Show Frame

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.018.png)

4. 调整 1D
- Color：选择蓝色（blue）
- Line Width：改为 4

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.019.png)

5. 调整 2D
- Palette：选择 Red-Blue Gradient
- Plotting Method：选择 Contour
- Traces：不做调整

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.020.png)

6. 调整 Scales：
- 字体：Arial；粗细：Bold；字号：12 号
- Horizontal：不做调整
- Vertical：不做调整

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.021.png)

7. Peaks
- Label：勾选
- 颜色：blue
- 字体：Arial；粗细：Bold；字号：12 号
- Decimals（小数位数）：2
- 其余皆为默认

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.017.png)

3.3 **定标（校正化学位移）**

1. 点击工具栏中的 reference，选中谱图中的溶剂峰，在弹出的窗口中，分别在 f2 和 f1 处输入溶剂峰的正确化学位移，即可得到化学位移校正之后的 2D NMR 谱图。

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.008.png)

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.008.png)

2. 若谱图中不含有溶剂峰，则选择其他易识别的峰来进行校正化学位移。

3.4 **标峰（标注化学位移）**

1. 点击工具栏中的 Peaks Picking，选择 Peak by Peak，在目标峰的中央点击，即可标注出该峰的化学位移。若出现错误标注，点击工具栏中的 Peaks Picking，选择 delete manually，拖动选中错误标注的目标峰，即可删除错误标注。

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.010.png)

2. 此时，HMBC 谱图已处理完成。

3.5 **特殊情况**

1. 若二维谱出现下图所示情况，所有信号均不是一个规则的圆形。

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.022.png)

2. 点击工具栏中的“Processing”“Processing Template”

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.023.png)

3. 在弹出的窗口中，选择“Phase correction”，并点击“...”

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.024.png)

4. 在弹出的窗口中，将 Method 改为“Automatic”,Initial Phase 改为“Imported”，点击 ok。

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.025.png)

5. 切换到 f1， 选择“Phase correction”，并点击“...”

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.024.png)

6. 在弹出的窗口中，将 Method 改为“Automatic”,Initial Phase 改为“Imported”，点击 ok。

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.026.png)

7. 若下面的 NOESY 谱图出现同样的问题，可采用同样的处理方法。

\4. **NOESY 谱图处理**

4.1 **导入一维谱图**

1. 有时，二维谱图中缺少一维谱图，因此第一步需要将一维谱图导入。

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.008.png)

2. 点击侧边工具栏中最下方的 Show traces，选择 Show traces，即可在二维谱图中显示一维谱图。

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.010.png)

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.008.png)

3. 显示一维谱图之后，需要重新导入校正之后的一维谱图。点击侧边工具栏中最下方的 Show traces，选择 Setup。在弹出的窗口中选中 Available 1D spectra 中的 1H NMR 谱图，点击 Horizontal traces 和 Vertical traces 中的对号，即可导入校正后的  1H NMR 谱图。

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.008.png)

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.001.png)

4.2 **属性调整**

1. 双击鼠标左键或单击鼠标右键，选择属性（Properties），打开属性面板。

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.017.png)

2. General：取消勾选 Title

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.017.png)

3. 调整 Grid
- 取消勾选 Show Horizontal
- 取消勾选 Show Vertical
- 取消勾选 Show Frame

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.018.png)

4. 调整 1D
- Color：选择蓝色（blue）
- Line Width：改为 4

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.019.png)

5. 调整 2D
- Palette：选择 Red-Blue Gradient
- Plotting Method：选择 Contour
- Traces：不做调整

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.020.png)

6. 调整 Scales：
- 字体：Arial；粗细：Bold；字号：12 号
- Horizontal：不做调整
- Vertical：不做调整

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.021.png)

7. Peaks
- Label：勾选
- 颜色：blue
- 字体：Arial；粗细：Bold；字号：12 号
- Decimals（小数位数）：2
- 其余皆为默认

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.017.png)

4.3 **定标（校正化学位移）**

1. 点击工具栏中的 reference，选中谱图中的溶剂峰，在弹出的窗口中，分别在 f2 和 f1 处输入溶剂峰的正确化学位移，即可得到化学位移校正之后的 2D NMR 谱图。

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.027.png)

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.027.png)

2. 若谱图中不含有溶剂峰，则选择其他易识别的峰来进行校正化学位移。

4.4 **相位校正**

1. 点击工具栏中的相位校正，即可自动校正 f1 和 f2 的相位。

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.027.png)

2. 点击工具栏中的“Processing”“Processing Template”

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.028.png)

3. 点击图中 Apodization 右下角的三个小点，勾选正弦平方设为 90 度。

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.028.png)

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.027.png)

4. 点击 f1，同样点击 Apodization 右下角的三个小点，勾选正弦平方设为90度，确保 f1 和 f2 窗函数的高斯、正弦平方、起点的三个数值一致。

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.028.png)

![...](..\..\0.%20软件教程\化学软件（Windows）\images\MestreNova%2012.0：核磁谱图处理.027.png)

5. 这样一张漂亮的 NOESY 谱就做出来了。



