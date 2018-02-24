
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
  

### Reference
* [Ubuntu 16.04 用户登录界面死循环问题的解决](http://blog.csdn.net/ssmixi/article/details/73483795)
