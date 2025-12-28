# 1. 安装 Zotero
    
1. 打开官网：[https://www.zotero.org/](https://www.zotero.org/)，注册账号（后面会用），点击“**Download**”。
![image.png](http://synbiopath.online/20251227185107882.png)

2. 下载 **Zotero 7 for Windows** 版本，同时选择“**Install Chrome Connector**”，在浏览器中安装插件。
![image.png](http://synbiopath.online/20251227185153096.png)

插件的作用是直接从网页中抓取文献元数据（包括 PDF 文件）并存入数据库，是目前 Zotero 中最好用的功能。

3. 点击下载好的安装包，按照默认设置安装即可。

4. 安装完成后，启动软件

5. 点击菜单栏中的“**编辑**”-->“**设置**”。
![image.png](http://synbiopath.online/20251228104909481.png)

选择“**常规**”-->“**文件重命名**”中的“**自定义文件格式**”。
![image.png](http://synbiopath.online/20251228105023917.png)

在弹出的窗口中输入下列内容，作用是对后续保存下来的PDF文件进行重命名，格式为“**年份-期刊-文献标题**”，例如“2020-Chemcal Science-The sporothriolides. A new biosynthetic family of fungal secondary metabolites”
```
{{year suffix="-"}}{{publicationTitle suffix="-"}}{{title truncate="200"}}
```


---

# 2. 云同步
为了防止文献数据丢失，或者是在多个设备中无缝切换，我们选择将 Zotero 中的文献保存在云端。由于 Zotero 官方存储较贵，因此我们使用坚果云的 WebDev 来进行文献的上传与下载。
>坚果云免费版：每个月有 1G 的上传流量，3G 的下载流量，足够所有人使用了。

1. 打开坚果云官网：https://www.jianguoyun.com/，注册账号。

2. 点击右上角的用户名，选择“**账户信息**”
![image.png](http://synbiopath.online/20251228110758769.png)

3. 在界面中，我们会看到流量重置的时间，以及当月所使用的上传和下载流量。我们点击“**安全选项**”进行下一步操作。
![image.png](http://synbiopath.online/20251228111000752.png)

4. 点击界面中的“**添加应用**”，输入用户名，此处输入“**Zotero**”，点击“**生成密码**”。
![image.png](http://synbiopath.online/20251228111140421.png)
牢记生成的密码等信息，接下来会用到。

5. 返回 Zotero，点击菜单栏中的“**编辑**”-->“**设置**”-->“**同步**”。填入最开始时注册的 Zotero 账号和密码，点击“**启用同步**”
![image.png](http://synbiopath.online/20251228111648667.png)

6. 在下方的“**文件同步**”区域中，我们选择“**WebDAV**”，并第四步中生成的“**网址**”、“**用户名**”和“**密码**”。
![image.png](http://synbiopath.online/20251228111917330.png)
![image.png](http://synbiopath.online/20251228112332824.png)

7. 填写完成后，点击“**验证服务器**”，弹出“文件同步设定成功”后，证明设置完成，此外，我们选择“**在需要时**”下载文件。
![image.png](http://synbiopath.online/20251228112503723.png)

---

# 3. 插件安装

在插件商店中，下载下面所有的插件：[https://zotero-chinese.com/plugins/](https://zotero-chinese.com/plugins/)

## 1. Jasminum（茉莉花）

**用途**：下载中文文献

**安装**：

1. 在插件商店中搜索“**Jasminum**”，选择"**Gitee下载**" 
![image.png](http://synbiopath.online/20251228113322338.png)


2. 在 Zotero 中，点击菜单栏中的“**工具**”-->“**插件**”。在弹出的窗口中，点击右上角的“**齿轮**”，选择“**Install Plaugin form a file**”，找到自己刚刚下载的 xpi 格式的插件，即可安装成功。
![image.png](http://synbiopath.online/20251228113512116.png)
![image.png](http://synbiopath.online/20251228113657258.png)

## 2. Green Frog（绿青蛙）

**用途**：显示期刊的 JCR 分区，中科院分区，影响因子等信息

**安装**：
1. 按照 Jasminum 插件的安装方式，在插件商店中搜索、下载并安装好插件。

2. 点击菜单栏中的“**编辑**”-->“**设置**”-->“**绿青蛙**”。点击此处的“目前还没有 EasyScholar 密钥，点击注册申请密钥”。
![image.png](http://synbiopath.online/20251228114814200.png)

3. 在弹出的网站中，注册账号，并点击“**我的信息**”
![image.png](http://synbiopath.online/20251228115141621.png)

4. 随后点击左侧的“**开放接口**”，复制“**密钥**”，粘贴至 Zotero 中即可。
![image.png](http://synbiopath.online/20251228115729619.png)
![image.png](http://synbiopath.online/20251228115921747.png)


## 3. DOI Manager

**用途**：用于获取与验证 DOI 号

**安装**：按照 Jasminum 插件的安装方式，在插件商店中搜索、下载并安装好插件即可。


## 4. SCI-PDF

**用途**：用于获取与验证 DOI 号

**安装**：按照 Jasminum 插件的安装方式，在插件商店中搜索、下载并安装好插件即可。

## 5. Ethereal Style

**用途**：用于对Zotero的阅读界面进行美化

**安装**：
1. 按照 Jasminum 插件的安装方式，在插件商店中搜索、下载并安装好插件。

2. 在 Zotero 的导航栏中，点击鼠标右键，选择“年”；“出版物”；“JCR 分区”；“中科院升级版”；“影响因子”；“#标签”；“阅读时间”；
![image.png](http://synbiopath.online/20251228123948439.png)

![image.png](http://synbiopath.online/20251228122642048.png)

3. 调整后，界面如图所示，各种信息一目了然。
![image.png](http://synbiopath.online/20251228123800537.png)

---

# 4. 文献管理技巧

## 1. 文献分区

按照我的习惯，我一般会把文献分为以下 
![image.png](http://synbiopath.online/20251228124904571.png)

