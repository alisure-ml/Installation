
## Ubuntu循环登录问题
> 以前的循环登录问题都是实验室另一位大神解决，这次他去陪女朋友了，所以只好自己试着解决了。

1. 进入文本模式，登录
  ```
  CTRL + ALT + F1
  ```

2. 卸载之前的驱动
  ```
  sudo apt-get remove nvidia-*
  sudo apt-get autoremove
  ```
  
3. 从`.run`文件卸载驱动
  ```
  sudo nvidia-uninstall
  ```
  
4. 此时，重启可正常登录（界面刷新会变慢）
  ```
  sudo reboot
  ```

5. 重新安装驱动
  ```
  CTRL + ALT + F1
  sudo service lightdm stop
  sudo chmod +x NVIDIA-Linux-x86_64-xxx.xx.run -no-x-check -no-nouveau-check -no-opengl-files
  ```

6. 启动`lightdm`
  ```
  sudo service lightdm restart
  ```
  

### Problem

* `Building kernel modules`出错
  安装驱动过程中出现下列错误：
  ```
  ERROR: An error occurred while performing the step: "Building kernel modules". See /var/log/nvidia-installer.log for details.
  ```
  可能的原因：驱动版本和系统内核版本不匹配。   
  解决办法：下载最新版本的驱动（或者下载补丁）

* 驱动的版本  
  下载驱动时可能找不到版本，比如我的是`GeForce GTX TITAN X`/`Ubuntu 16.04`，直接查找找不到对应的驱动。
  我就随便多选了几个，发现有一个支持该GPU，然后就下载使用了。
  

### Reference
* [Ubuntu 16.04 用户登录界面死循环问题的解决](http://blog.csdn.net/ssmixi/article/details/73483795)
* [Ubuntu系统安装CUDA或NVIDIA驱动后出现循环登录问题的Solution (附：building kernel modules error)](http://blog.csdn.net/xl928471061/article/details/78130165)
* [安装Nvidia显卡驱动和CUDA](http://blog.csdn.net/bluewhalerobot/article/details/73658267)
