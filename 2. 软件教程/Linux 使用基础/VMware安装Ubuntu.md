
**VMware安装Ubuntu**

\1. **准备工作**

- Ubuntu 镜像文件
- VMware 16 软件

\2. **安装步骤**

1. 打开VMware Workstation 16 Pro ，点击创建新的虚拟机。

![...](..\..\0.%20软件教程\Linux%20使用基础\images\VMware安装Ubuntu.001.png)

2. 选择“自定义（高级）”

![...](..\..\0.%20软件教程\Linux%20使用基础\images\VMware安装Ubuntu.001.png)

3. 选择兼容性，（直接默认就行）

![...](..\..\0.%20软件教程\Linux%20使用基础\images\VMware安装Ubuntu.001.png)

4. 选择“安装程序光盘镜像文件”并点击“浏览”选择之前已下好的镜像文件。

![...](..\..\0.%20软件教程\Linux%20使用基础\images\VMware安装Ubuntu.001.png)

5. 填写个人信息，之后进行下一步

![...](..\..\0.%20软件教程\Linux%20使用基础\images\VMware安装Ubuntu.001.png)

6. 选择虚拟机安装的位置，以及虚拟机的名字

![...](..\..\0.%20软件教程\Linux%20使用基础\images\VMware安装Ubuntu.001.png)

7. 设置虚拟机的硬件配置，以本人的笔记本电脑为例，联想拯救者 R7000 系列。只含有一个 CPU R7-4800，即单处理器，8 核心，16 线程。 分配给虚拟机 6 个核心，12 个线程。

![...](..\..\0.%20软件教程\Linux%20使用基础\images\VMware安装Ubuntu.001.png)

8. 设置虚拟机使用的内存大小，本人笔记本电脑共 16G 内存，分配给虚拟机 12G。

![...](..\..\0.%20软件教程\Linux%20使用基础\images\VMware安装Ubuntu.001.png)

9. 此时一直选择推荐的设置即可

![...](..\..\0.%20软件教程\Linux%20使用基础\images\VMware安装Ubuntu.001.png)

![...](..\..\0.%20软件教程\Linux%20使用基础\images\VMware安装Ubuntu.001.png)

![...](..\..\0.%20软件教程\Linux%20使用基础\images\VMware安装Ubuntu.001.png)

10. 选择创建新的虚拟机

![...](..\..\0.%20软件教程\Linux%20使用基础\images\VMware安装Ubuntu.001.png)

11. 根据自己硬盘的剩余容量大小，设置虚拟磁盘的大小，本人剩 F 盘剩余容量有 430 G，因此设置 300G 磁盘大小。并选择将磁盘裂分为多个文件。

![...](..\..\0.%20软件教程\Linux%20使用基础\images\VMware安装Ubuntu.001.png)

12. 默认磁盘文件名称

![...](..\..\0.%20软件教程\Linux%20使用基础\images\VMware安装Ubuntu.001.png)

13. 检查一下自己之前为虚拟机设置的配置，没有问题，点击 Finsh 即可完成。

![...](..\..\0.%20软件教程\Linux%20使用基础\images\VMware安装Ubuntu.001.png)

14. 此时虚拟机安装完成。

15. 打开 VMware，选择开启此虚拟机，静静等待安装即可。

![...](..\..\0.%20软件教程\Linux%20使用基础\images\VMware安装Ubuntu.002.png)

16. VMware 虚拟机与主机之间还不能自由剪切复制文件，共有两种思路来解决这个问题：
- 安装 VMware tools
- 在虚拟机中设置共享文件夹

17. 进入安装好的 Ubuntu 系统，打开终端，安装 VMware tools

```C#
# 安装open-vm-tools
sudo apt-get install open-vm-tools

# 安装open-vm-tools-desktop
sudo apt-get install open-vm-tools-desktop

# 重启系统
sudo reboot```
完成上述操作后，你的虚拟机终端就可以与电脑主机互相复制粘贴，若该方法不可行，可考虑设置共享文件夹。

**Ubuntu复制粘贴快捷键**

复制：Ctrl+Shift+C

粘贴：Ctrl+Shift+V

18. 设置共享文件夹


\3. **参考资料**

[1：2020最新版VMware安装Ubuntu20.04教程(巨细)！](https://zhuanlan.zhihu.com/p/141033713)

[2：VMware 虚拟机安装Linux系统（Ubuntu）](https://zhuanlan.zhihu.com/p/649522975)

[3：VMware安装 Ubuntu 16.04](https://zhuanlan.zhihu.com/p/150263093)

[4：手把手教你在VMware16.0上安装ubuntu20.04（虚拟机安装Ubuntu系统））](https://blog.csdn.net/jiu_liu/article/details/121597146)

[5：VMware虚拟机和主机间复制粘贴共享剪贴板](https://zhuanlan.zhihu.com/p/665154528)

