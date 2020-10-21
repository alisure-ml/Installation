# VNC viewer 远程

## Windows部分

1. 下载 [VNC viewer](https://www.realvnc.com/en/connect/download/viewer/)

2. 安装

3. 配置Linux电脑，并得到其ip地址（参见Linux部分）

4. 在VNC Viewer中输入ip地址进行连接


## Linux部分

1. 在搜索框搜索 `Sharing` 并打开

2. 设置 `Screen Sharing`, 点击左上角`ON`， 点击勾线`Allow connections to control the screen`，并选择 `Require a password`. 关闭后 `Screen Sharing` 显示为 `Active` 状态。

3. 安装 `dconf-editor` 工具，方便配置 `dconf`.

* 打开命令行：`Ctrl + Alt + T`
* 命令行中输入：`sudo apt-get install dconf-editor`
* 输入密码

4. 设置 `remote-access`

* 命令行中输入：`dconf-editor` 打开 `dconf`
* 选择 `org->gnome->desktop->peripherals->remote-access` 中取消 `requre-encryption`

5. 获得ip地址

* 命令行中输入：`ifconfig`

