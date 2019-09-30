# 安装深度学习环境


## 安装系统

* 制作系统盘

* 安装系统

* 更新软件

启动系统后会自动弹出更新软件，或者到设置中进行更新检查。

* 安装`vim`,`gcc`,`make`,`lightdm`

```
sudo apt install vim
sudo apt install gcc
sudo apt install make
sudo apt install lightdm
```


## 安装Anaconda.md

* 下载、安装Anaconda：请参考[Anaconda.md](https://github.com/alisure-ml/Installation/blob/master/Anaconda.md)

* 创建环境

```
conda -n alisure36tf python=3.6
```


## 安装NVIDIA显卡驱动

* 下载显卡驱动：[Download Drivers](https://www.nvidia.com/Download/index.aspx)

选择匹配的版本即可，例如`NVIDIA-Linux-x86_64-430.50.run`

* 安装显卡驱动：请参考[NVIDIA.md](https://github.com/alisure-ml/Installation/blob/master/NVIDIA.md)



## 安装CUDA

* 下载CUDA

* 安装CUDA，请参考：[CUDA.md](https://github.com/alisure-ml/Installation/blob/master/CUDA.md)


