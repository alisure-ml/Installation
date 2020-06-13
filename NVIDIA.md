# NVIDIA

## 监控

```
watch -n1 -d nvidia-smi
```


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

5. 禁用nouveau驱动（具体见下面的`Problem`，不确定是否是可选）

6. 重新安装驱动
  
  下载驱动：[https://www.nvidia.com/Download/index.aspx](https://www.nvidia.com/Download/index.aspx)

  ```
  CTRL + ALT + F1
  sudo service lightdm stop
  sudo chmod +x NVIDIA-Linux-x86_64-xxx.xx.run
  sudo ./NVIDIA-Linux-x86_64-xxx.xx.run -no-x-check -no-nouveau-check -no-opengl-files
  ```

7. 启动`lightdm`
  ```
  sudo service lightdm restart
  ```

8. 验证是否安装成功
  ```
  nvidia-smi
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
  
* 在解决问题中禁用了nouveau驱动
  1. 用`vim`打开`blacklist.conf`文件
  ```
  sudo vim /etc/modprobe.d/blacklist.conf
  ```
  2. 在文末添加下列内容
  ```
  blacklist nouveau
  options nouveau modeset=0
  ```
  3. 使配置生效
  ```
  sudo update-initramfs -u
  ```
  4. 重启
  ```
  sudo reboot
  ```
  5. 验证是否禁用成功（没有输出即成功）
  ```
  lsmod | grep nouveau
  ```
  
* 系统更新后加载不了桌面

  解决方法见链接：[ubuntu16.04更新系统后桌面出错的解决办法](https://blog.csdn.net/zhangxue2017/article/details/79937114)


### Reference

* [Ubuntu 16.04 用户登录界面死循环问题的解决](http://blog.csdn.net/ssmixi/article/details/73483795)

* [Ubuntu系统安装CUDA或NVIDIA驱动后出现循环登录问题的Solution (附：building kernel modules error)](http://blog.csdn.net/xl928471061/article/details/78130165)

* [安装Nvidia显卡驱动和CUDA](http://blog.csdn.net/bluewhalerobot/article/details/73658267)

* [Ubuntu 16.04安装NVIDIA驱动](http://blog.csdn.net/cosmoshua/article/details/76644029)

