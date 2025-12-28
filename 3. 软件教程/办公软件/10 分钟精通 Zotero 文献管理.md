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
为了在不同的设备上对