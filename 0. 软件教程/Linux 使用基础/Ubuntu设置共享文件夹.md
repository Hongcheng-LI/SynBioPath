
**Ubuntu设置共享文件夹**

1. 点击工具栏中的：**VM** -> **setting**

![...](..\..\0.%20软件教程\Linux%20使用基础\images\Ubuntu设置共享文件夹.001.png)

2. 在弹出的窗口中点击 **Options** -> **Shared Folders** 

![...](..\..\0.%20软件教程\Linux%20使用基础\images\Ubuntu设置共享文件夹.002.png)

3. 在弹出的窗口中点击 **Always enabled** -> **Add**，按照弹出的窗口提示一步步操作，直到输入路径和文件夹名字。选中 **F:\Software\data** 路径下的 **LHC\_Ubuntu** 的文件夹后，会自动填充路径和文件夹名字。最后点击 **OK** 即可。
- 前期已经在 **F:\Software\data** 路径下新建了一个名为 **LHC\_Ubuntu** 的文件夹，用作共享文件夹。

![...](..\..\0.%20软件教程\Linux%20使用基础\images\Ubuntu设置共享文件夹.002.png)

4. 进入 Ubuntu 系统，在桌面打开终端，输入以下命令，如果输出先前设置的共享文件夹名字，则代表正确设置。

```C#
vmware-hgfsclient```
![...](..\..\0.%20软件教程\Linux%20使用基础\images\Ubuntu设置共享文件夹.003.png)

5. 点击左上角的 **file**文件夹，选择 **other locations**，点击 **Ubuntu**-> **mnt**，即可进入 **mnt** 目录，看名下是否有 **hgfs** 的文件夹。

![...](..\..\0.%20软件教程\Linux%20使用基础\images\Ubuntu设置共享文件夹.004.png)

![...](..\..\0.%20软件教程\Linux%20使用基础\images\Ubuntu设置共享文件夹.005.png)

![...](..\..\0.%20软件教程\Linux%20使用基础\images\Ubuntu设置共享文件夹.006.png)

6. 如果没有，则在该文件夹中打开终端，输入下列命令创建该文件夹

```C#
# 在 mnt 目录下创建名为 hgfs 的文件夹
sudo mkdir /mnt/hgfs```

7. 进入 **hgfs** 目录下，打开终端，输入下列命令，即可设置完成。

```C#
sudo /usr/bin/vmhgfs-fuse .host:/ /mnt/hgfs -o allow\_other -o uid=1000 -o gid=1000 -o umask=022```

8. 从 Win 系统中将几个文件放置在共享文件夹下，即可看到在 **Ubuntu** 的共享文件夹中出现了该文件。


