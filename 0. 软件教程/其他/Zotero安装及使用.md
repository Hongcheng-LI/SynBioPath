
**Zotero安装及使用**

\1. **安装 Zotero**

- 官网：<https://www.zotero.org/>
- 下载 Zotero 7 版本，同时选择“Install Chrome Connector”，在浏览器中安装插件。

![...](..\..\0.%20软件教程\其他\images\Zotero安装及使用.001.png)

![...](..\..\0.%20软件教程\其他\images\Zotero安装及使用.002.png)

\2. **安装 Zotero 插件**

2.1 **下载插件**

- 插件商店：<https://zotero-chinese.com/plugins/>
- 推荐插件：

Translate for Zotero

Jasminum

Awesome GPT

Ethereal Style

Ethereal Reference

DOI Manager

Actions and Tags for Zotero

Green Frog

下载适配 Zotero 7 的插件

![...](..\..\0.%20软件教程\其他\images\Zotero安装及使用.003.png)

2.2 **安装插件**

1. 点击**工具** ---> **插件**

![...](..\..\0.%20软件教程\其他\images\Zotero安装及使用.004.png)

2. 点击**齿轮**，选择“**Install Plugin from File**”

![...](..\..\0.%20软件教程\其他\images\Zotero安装及使用.005.png)

\3. **将 Deepseek 接入 Zotero**

3.1 **安装 deepseek**

`    `此处为语雀内容卡片，点击链接查看：<https://www.yuque.com/dviy1p/zfgvwt/cmtagtvib7zqsfg6#GIwZp>   

`    `此处为语雀内容卡片，点击链接查看：<https://www.yuque.com/dviy1p/zfgvwt/cmtagtvib7zqsfg6#EmsWz>   

3.2 **设置 Zotero 的 LLM 模型**

1. 点击**编辑** ---> **设置**

![...](..\..\0.%20软件教程\其他\images\Zotero安装及使用.006.png)

2. 在设置窗口中，找到 GPT 插件，然后进行设置

![...](..\..\0.%20软件教程\其他\images\Zotero安装及使用.007.png)

- Base API：http://localhost:11434
- API key：由于是本地部署 Deepseek-R1，因此不需要输入 API 密码，随便输入几个数字就行，例如 1234。
- Model：输入自己安装部署的 deepseek-r1 模型，我安装的是 8B 版本，因此输入deepseek-r1:8b。
- Temperature：0.5~0.7 之间皆可
- 由于 deepseek 不支持文本嵌入模型，因此还需要另找一个供应商提供嵌入模型（也就是插件下面的embedding）。此处选择硅基流动提供的 embedding 模型。

3.3 **获取硅基流动 API**

- 官网：<https://cloud.siliconflow.cn/models>
- 选择：BAAI/bge-m3 模型

1. 点击**嵌入**。

![...](..\..\0.%20软件教程\其他\images\Zotero安装及使用.008.png)

2. 选择 **API 文档**

![...](..\..\0.%20软件教程\其他\images\Zotero安装及使用.009.png)

3. 获取 Full API 链接和 API Key。

![...](..\..\0.%20软件教程\其他\images\Zotero安装及使用.010.png)

Full API：<https://api.siliconflow.cn/v1/embeddings>

4. 点击**新建 API 密钥**，输入 **Zotero**，即可获得 **API 密钥**。

![...](..\..\0.%20软件教程\其他\images\Zotero安装及使用.011.png)

API Key：上图所示

3.5 **设置 Zotero 的 embedding 模型**

![...](..\..\0.%20软件教程\其他\images\Zotero安装及使用.012.png)

- Full API：<https://api.siliconflow.cn/v1/embeddings>
- API Key：参考第三步获得的 API Key
- Model：BAAI/bge-m3

点击 text，如果如下图所示，则证明 Zotero 成功接入 deepseek 

![...](..\..\0.%20软件教程\其他\images\Zotero安装及使用.013.png)

打开文献，点击红色按钮，即可使用了

![...](..\..\0.%20软件教程\其他\images\Zotero安装及使用.014.png)

