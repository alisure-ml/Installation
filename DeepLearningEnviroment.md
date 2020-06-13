# 安装深度学习环境



## 安装系统

* 制作系统盘

* 安装系统

* 更新软件

启动系统后会自动弹出更新软件，或者到设置中进行更新检查。

* 更新Source

[apt更改为国内源](https://www.jianshu.com/p/71ddb83adc1e)


* 安装`vim`,`gcc`,`make`,`lightdm`,`git`

```
sudo apt install vim
sudo apt install gcc
sudo apt install make
sudo apt install lightdm
sudo apt install git
```

* 更新`apt`

```
sudo apt-get update
sudo apt-get upgrade
```


## 安装Anaconda.md

* 下载、安装Anaconda：请参考[Anaconda.md](https://github.com/alisure-ml/Installation/blob/master/Anaconda.md)

* 创建环境

```
conda create -n alisure36tf python=3.6
```

* `pypi`镜像：[pypi 镜像使用帮助](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/)

```
pip install pip -U
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```



## 安装NVIDIA显卡驱动

* 下载显卡驱动：[Download Drivers](https://www.nvidia.com/Download/index.aspx)

选择匹配的版本即可，例如`NVIDIA-Linux-x86_64-430.50.run`

* 安装显卡驱动：请参考[NVIDIA.md](https://github.com/alisure-ml/Installation/blob/master/NVIDIA.md)



## 安装CUDA

* 下载CUDA：[cuda-toolkit-archive](https://developer.nvidia.com/cuda-toolkit-archive)

选择版本，例如`cuda_10.0.130_410.48_linux.run`。

* 安装CUDA，请参考：[CUDA.md](https://github.com/alisure-ml/Installation/blob/master/CUDA.md)



## 安装cudnn

* 请参考：[CUDA.md/安装cudnn](https://github.com/alisure-ml/Installation/blob/master/CUDA.md#%E5%AE%89%E8%A3%85cudnn)



## 安装`pycharm`

* 下载最新版：[pycharm](https://www.jetbrains.com/pycharm/download/#section=linux)

* 解压缩到相应的目录

* 添加程序快捷方式：请参考：[desktop_entry.md](https://github.com/alisure-ml/Installation/blob/master/desktop_entry.md)
  
  还需要添加到收藏夹。
  
* 破解

> 将 `0.0.0.0 account.jetbrains.com` 添加到 `/etc/hosts`(`sudo gedit /etc/hosts`) 文件中，然后再搜索密钥。

  1. [学生授权申请方式](https://sales.jetbrains.com/hc/zh-cn/articles/207154369-%E5%AD%A6%E7%94%9F%E6%8E%88%E6%9D%83%E7%94%B3%E8%AF%B7%E6%96%B9%E5%BC%8F)
  2. [lanyus](http://idea.lanyus.com/)
  3. [http://lookdiv.com](http://lookdiv.com) 钥匙：1211268069


## `Tensorflow`环境

* 创建环境

```
conda create -n alisure36tf python=3.6
conda activate alisure36tf

pip install pip -U
pip install tensorflow-gpu
```

* 测试环境

```
import tensorflow as tf 
sess = tf.Session() 
a = tf.constant(1) 
b = tf.constant(2) 
print(sess.run(a+b)) 
```



## `PyTorch`环境

* 创建环境

```
conda create -n alisure36torch python=3.6
conda activate alisure36torch

pip install pip -U
pip install torch torchvision
```

* 测试环境

```
import torch
print(torch.cuda.is_available())
```

## Problem

* [Ubuntu安装软件时Could not get lock /var/lib/dpkg/lock - open (11: Resource temporarily unavailable)的解决方案](https://blog.csdn.net/qq_22999067/article/details/92851100)

