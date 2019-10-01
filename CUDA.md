## 安装CUDA和CUDNN


### 安装NVIDIA驱动

可以参考：[Installation/NVIDIA.md](https://github.com/alisure-ml/Installation/blob/master/NVIDIA.md)


### CUDA

* 下载完CUDA 9.0之后执行如下语句，运行.run文件

```
sudo sh cuda_9.0.176_384.81_linux.run
```

单击回车，一路往下运行，直到提示“是否为NVIDIA安装驱动nvidia-384？”，选择否，因为已经安装好驱动程序了，其他的全都是默认。

不过要记住安装位置，默认是安装在/usr/local/cuda文件夹下。

* 配置环境变量，运行如下命令打开profile文件

```
sudo gedit  /etc/profile
```

打开文件后在文件末尾添加路径，也就是安装目录，命令如下：

```
export PATH=/usr/local/cuda-9.0/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda-9.0/lib64:$LD_LIBRARY_PATH　　
```

保存，然后重启电脑:

```
sudo reboot
```

* 测试安装是否成功

```
cd /usr/local/cuda/samples/1_Utilities/deviceQuery
sudo make
./deviceQuery
```

如果显示关于GPU的信息就是成功了。


### 安装cudnn

1. 下载对应版本的[cudnn](https://developer.nvidia.com/cudnn)  

2. 需要下载两个版本，runtime版和developer版

```
cuDNN Runtime Library for Ubuntu18.04 (Deb)
cuDNN Developer Library for Ubuntu18.04 (Deb)
```

3. 将下载的文件格式改为.tgz，然后解压

4. 一个里版本里面有头文件(在include中)，一个里面有动态连接文件（在lib中）

  * 将`include`中头文件`cudnn.h`拷贝到`/usr/local/cuda/lib64`
  * 将`lib`中的动态连接文件拷贝到`/usr/local/cuda/lib64`

5. 添加环境变量

```
sudo gedit ~/.bashrc
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
```

6. 对拷贝进来的两个动态连接库创建软链接

```
cd /usr/local/cuda/lib64/
sudo ln -s libcudnn.so.7 libcudnn.so
sudo ln -s libcudnn.so.7.x.x libcudnn.so.7
```

参考：[Install_AND_path/install nvidiaDriver_cuda_cudnn.md](https://github.com/waallf/Install_AND_path/blob/master/install%20nvidiaDriver_cuda_cudnn.md)

### Pycharm中找不到cuda

参考：[Install_AND_path/无法找到cuda9.0](https://github.com/waallf/Install_AND_path/blob/master/%E6%97%A0%E6%B3%95%E6%89%BE%E5%88%B0cuda9.0.md)

