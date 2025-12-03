
**Obsidian 使用教程**

\1. **安装步骤**

1. 进入官网，下载 Obsidian 安装包：https://obsidian.md/
2. 如果网络不好，下载一个 Watt Toolkit 工具解决网络问题：https://apps.microsoft.com/detail/9mtcfhs560ng?hl=zh-cn&gl=US
3. Obsidian安装完成后，界面如图所示。

![...](..\..\0.%20软件教程\其他\images\Obsidian%20使用教程.001.png)

由于 Obsidian 没有云同步功能，因此我们选择使用 GitHub 自动同步。

\2. **云同步（GitHub）**

1. 注册 GitHub 账号：https://github.com/

```若存在网络问题，可使用 Watt Toolkit 工具解决网络问题```
2. 注册完成后，创建新的仓库

![...](..\..\0.%20软件教程\其他\images\Obsidian%20使用教程.002.png)

3. 输入仓库的姓名，即可创建仓库

![...](..\..\0.%20软件教程\其他\images\Obsidian%20使用教程.003.png)

4. 此时仓库已经创建完成

![...](..\..\0.%20软件教程\其他\images\Obsidian%20使用教程.004.png)

5. 下载 GitHub 客户端：https://desktop.github.com/download/
6. 使用 GitHub 账号登陆，界面如下

![...](..\..\0.%20软件教程\其他\images\Obsidian%20使用教程.005.png)

7. 将刚刚创建的的 GitHub 仓库克隆至本地

![...](..\..\0.%20软件教程\其他\images\Obsidian%20使用教程.005.png)

![...](..\..\0.%20软件教程\其他\images\Obsidian%20使用教程.005.png)

8. 此时，在目标路径下已出现了克隆好的 GitHub 仓库

![...](..\..\0.%20软件教程\其他\images\Obsidian%20使用教程.006.png)

9. 打开 Obsidian，选择打开本地仓库，打开刚刚克隆下来的 GitHub 仓库

![...](..\..\0.%20软件教程\其他\images\Obsidian%20使用教程.007.png)

![...](..\..\0.%20软件教程\其他\images\Obsidian%20使用教程.008.png)

![...](..\..\0.%20软件教程\其他\images\Obsidian%20使用教程.009.png)

10. 点击创建新文件，新建一个文件，我们会看到在刚刚克隆下来的本地仓库中生成了一个后缀名为“.md”的“通往合成生物学之路”文件，这就是我们刚刚新建的文档，完全存储在本地。

![...](..\..\0.%20软件教程\其他\images\Obsidian%20使用教程.010.png)

![...](..\..\0.%20软件教程\其他\images\Obsidian%20使用教程.010.png)

![...](..\..\0.%20软件教程\其他\images\Obsidian%20使用教程.006.png)

11. 在本地的 SynBioPath 仓库中，还出现了一个 .Obsidian文件夹，里面含有 Obsidian 的配置文件。我们看到里面有一个 workspace.json 文件，这个文件记录了我们在 Obsidian上的每一次操作，如果频繁上传到 GitHub，会造成冲突。

![...](..\..\0.%20软件教程\其他\images\Obsidian%20使用教程.011.png)

12. 我们在在本地的 SynBioPath 仓库中，新建一个名为.gitignore的文件，在里面输入两行命令，设置为在云同步时不上传workspace.json 和 workspace-mobile.json文件，防止造成冲突。

![...](..\..\0.%20软件教程\其他\images\Obsidian%20使用教程.011.png)

```Markdown
.gitignore
.obsidian/workspace.json
.obsidian/workspace-mobile.json```
13. 回到 GitHub 桌面端，选中 5 个文件，添加描述后，点击 commit。再点击 “publish branch”选项，即可同步到 GitHub 云端。此时我们在 GitHub 的网页端中，已经看到了刚刚新建的笔记。这样，我们就把本地的 obsidian笔记库，跟 GitHub 做了一个云同步，并且备份到了 GitHub 中。到这里，我们只能是手动进行云同步，比较麻烦。我们借助 obsidian 的一个插件，可以实现自动云同步。

![...](..\..\0.%20软件教程\其他\images\Obsidian%20使用教程.012.png)

![...](..\..\0.%20软件教程\其他\images\Obsidian%20使用教程.012.png)

![...](..\..\0.%20软件教程\其他\images\Obsidian%20使用教程.013.png)

14. 点击 Obsidian 底部的齿轮，点击第三方插件，并关闭安全模式，点击浏览插件市场。

![...](..\..\0.%20软件教程\其他\images\Obsidian%20使用教程.010.png)

![...](..\..\0.%20软件教程\其他\images\Obsidian%20使用教程.010.png)

![...](..\..\0.%20软件教程\其他\images\Obsidian%20使用教程.010.png)

15. 在插件市场中搜索 git，安装后点击启用。

![...](..\..\0.%20软件教程\其他\images\Obsidian%20使用教程.010.png)

![...](..\..\0.%20软件教程\其他\images\Obsidian%20使用教程.010.png)


