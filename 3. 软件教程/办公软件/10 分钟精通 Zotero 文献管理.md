# 1. 安装 Zotero
    
1. 打开官网：[https://www.zotero.org/](https://www.zotero.org/)，注册账号（后面会用），点击“**Download**”。
![image.png](https://synbiopath.online/20251227185107882.png)

2. 下载 **Zotero 7 for Windows** 版本，同时选择“**Install Chrome Connector**”，在浏览器中安装插件。
![image.png](https://synbiopath.online/20251227185153096.png)

插件的作用是直接从网页中抓取文献元数据（包括 PDF 文件）并存入数据库，是目前 Zotero 中最好用的功能。

3. 点击下载好的安装包，按照默认设置安装即可。

4. 安装完成后，启动软件

5. 点击菜单栏中的“**编辑**”-->“**设置**”。
![image.png](https://synbiopath.online/20251228104909481.png)

选择“**常规**”-->“**文件重命名**”中的“**自定义文件格式**”。
![image.png](https://synbiopath.online/20251228105023917.png)

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
![image.png](https://synbiopath.online/20251228110758769.png)

3. 在界面中，我们会看到流量重置的时间，以及当月所使用的上传和下载流量。我们点击“**安全选项**”进行下一步操作。
![image.png](https://synbiopath.online/20251228111000752.png)

4. 点击界面中的“**添加应用**”，输入用户名，此处输入“**Zotero**”，点击“**生成密码**”。
![image.png](https://synbiopath.online/20251228111140421.png)
牢记生成的密码等信息，接下来会用到。

5. 返回 Zotero，点击菜单栏中的“**编辑**”-->“**设置**”-->“**同步**”。填入最开始时注册的 Zotero 账号和密码，点击“**启用同步**”
![image.png](https://synbiopath.online/20251228111648667.png)

6. 在下方的“**文件同步**”区域中，我们选择“**WebDAV**”，并第四步中生成的“**网址**”、“**用户名**”和“**密码**”。
![image.png](https://synbiopath.online/20251228111917330.png)
![image.png](https://synbiopath.online/20251228112332824.png)

7. 填写完成后，点击“**验证服务器**”，弹出“文件同步设定成功”后，证明设置完成，此外，我们选择“**在需要时**”下载文件。
![image.png](https://synbiopath.online/20251228112503723.png)

---

# 3. 插件安装

在插件商店中，下载下面所有的插件：[https://zotero-chinese.com/plugins/](https://zotero-chinese.com/plugins/)

## 1. Jasminum（茉莉花）

**用途**：下载中文文献

**安装**：

1. 在插件商店中搜索“**Jasminum**”，选择"**Gitee下载**" 
![image.png](https://synbiopath.online/20251228113322338.png)


2. 在 Zotero 中，点击菜单栏中的“**工具**”-->“**插件**”。在弹出的窗口中，点击右上角的“**齿轮**”，选择“**Install Plaugin form a file**”，找到自己刚刚下载的 xpi 格式的插件，即可安装成功。
![image.png](https://synbiopath.online/20251228113512116.png)
![image.png](https://synbiopath.online/20251228113657258.png)

## 2. Green Frog（绿青蛙）

**用途**：显示期刊的 JCR 分区，中科院分区，影响因子等信息

**安装**：
1. 按照 Jasminum 插件的安装方式，在插件商店中搜索、下载并安装好插件。

2. 点击菜单栏中的“**编辑**”-->“**设置**”-->“**绿青蛙**”。点击此处的“目前还没有 EasyScholar 密钥，点击注册申请密钥”。
![image.png](https://synbiopath.online/20251228114814200.png)

3. 在弹出的网站中，注册账号，并点击“**我的信息**”
![image.png](https://synbiopath.online/20251228115141621.png)

4. 随后点击左侧的“**开放接口**”，复制“**密钥**”，粘贴至 Zotero 中即可。
![image.png](https://synbiopath.online/20251228115729619.png)
![image.png](https://synbiopath.online/20251228115921747.png)


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
![image.png](https://synbiopath.online/20251228123948439.png)

![image.png](https://synbiopath.online/20251228122642048.png)

3. 调整后，界面如图所示，各种信息一目了然。
![image.png](https://synbiopath.online/20251228123800537.png)

---

# 4. 文献管理技巧

## 1. 文献分区

按照我的习惯，我一般会把文献分为以下几类
![image.png](https://synbiopath.online/20251228124904571.png)
- **课题相关**：按照化合物的类别或者是基因簇的类别，将课题相关的文献保存到此处。
- **毕业论文**：将知网上的硕博毕业论文保存到此处，按照习惯，再细分为“真菌”；“放线菌”；“植物”；“酶工程“等不同方向
![image.png](https://synbiopath.online/20251228131939800.png)
- **综述**：进一步细分为：“多重耐药菌”；“海洋环境”；“海洋真菌”等
![image.png](https://synbiopath.online/20251228131913220.png)
- **博士文章**：每一篇发表的文章单独建一个分类，用来整理相关文献，参考文献等
- **期刊分类**：按照不同的期刊进行细分，优先将新的文献保存在对应的期刊子分类中。
![image.png](https://synbiopath.online/20251228131852261.png)

- **人名分类**：按照不同的国家进行细分，再按照人名进行进一步的分类。
![image.png](https://synbiopath.online/20251228131826298.png)

## 2. 标签管理

对于看过的文献，一般会对其打上标签：我一般会按照以下几个维度对其进行标签管理，一般标签数量不超过 5 个：
- 期刊名
- 通讯作者
- 菌株来源
- 文献内容（可多个）

例如，对唐奕的一篇JACS进行打标签，标注：“#JACS”“#唐奕”；“#酵母”；“#NRPKS”
![image.png](https://synbiopath.online/20251228132418681.png)

## 3. 文献阅读

好多人推荐在 Zotero 通过插件接入AI功能，但我却更建议在 AI 浏览器中进行文献阅读，目前我推荐的是 夸克浏览器。

1. 进入官网：https://www.quark.cn/，安装夸克浏览器

2. 点击菜单栏中的“**编辑**”-->“**设置**”-->“**通用**”。将PDF打开方式设置为夸克浏览器
![image.png](https://synbiopath.online/20251228133136983.png)

3. 随后，打开一篇文献，就可以看到既可以对文献进行标注，也可以用 AI 对文献进行解读，提问。
![image.png](https://synbiopath.online/20251228133244778.png)

4. 如果有更进一步的需求，可以打开右上角的“千问”图标，在弹出的 AI 侧边栏中对文献进行提问。
![image.png](https://synbiopath.online/20251228133608009.png)

---


