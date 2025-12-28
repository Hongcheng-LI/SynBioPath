# 1. 安装 Zotero
    
1. 打开官网：[https://www.zotero.org/](https://www.zotero.org/)，注册账号（后面会用），点击“Download”。
![image.png](http://synbiopath.online/20251227185107882.png)

2. 下载 Zotero 7 for Windows 版本，同时选择“Install Chrome Connector”，在浏览器中安装插件。
![image.png](http://synbiopath.online/20251227185153096.png)

插件的作用是直接从网页中抓取文献元数据（包括 PDF 文件）并存入数据库

3. 点击下载好的安装包，按照默认设置安装即可。

4. 安装完成后，启动软件

5. 点击菜单栏中的“编辑”-->“设置”。
![image.png](http://synbiopath.online/20251228104909481.png)

选择“常规”-->“文件重命名”中的“自定义文件格式”。
![image.png](http://synbiopath.online/20251228105023917.png)

在弹出的格式中输入，作用是对后续保存下来的PDF文件进行重命名，格式为“年份-期刊-文献标题”，例如“2020-Chemcal Science-The sporothriolides. A new biosynthetic family of fungal secondary metabolites”
```
{{year suffix="-"}}{{publicationTitle suffix="-"}}{{title truncate="200"}}
```


---

# 2. 云同步
为了防止文献数据丢失，或者是在多个设备中无缝切换，我们选择将 Zotero 中的文献保存在云端。由于 Zotero 官方存储较贵，因此我们使用坚果云的 WebDev 来进行文献的上传与下载。
>坚果云免费版：每个月有 1G 的上传流量，3G 的下载流量，足够所有人使用了。

1. 打开坚果云官网：https://www.jianguoyun.com/，注册账号。

2. 点击右上角的用户名，选择“账户信息”
![image.png](http://synbiopath.online/20251228110758769.png)

3. 在界面中，我们会看到流量重置的时间，以及当月所使用的上传和下载流量。我们点击“安全选项”进行下一步操作。
![image.png](http://synbiopath.online/20251228111000752.png)

4. 点击界面中的“添加应用”，输入用户名，此处输入“Zotero”，点击“生成密码”。
![image.png](http://synbiopath.online/20251228111140421.png)
牢记生成的密码等信息，接下来会用到。

5. 返回 Zotero，点击菜单栏中的“编辑”-->“设置”-->“同步”。填入最开始时注册的 Zotero 账号和密码，点击“启用同步”
![image.png](http://synbiopath.online/20251228111648667.png)
