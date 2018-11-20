### 安装Caffe

* GitHub地址： [https://github.com/BVLC/caffe](https://github.com/BVLC/caffe)
* 官方安装地址： [http://caffe.berkeleyvision.org/installation.html](http://caffe.berkeleyvision.org/installation.html)

下载Caffe:
  ```
  git clone https://github.com/BVLC/caffe.git
  cd caffe
  ```
  
### 注意！！！！

* 注意编译的时候python的版本。一定要在执行之前查看python的版本。毕竟工作站中的Linux系统的Python可能会比较乱，原因大家都懂的。


### Windows 安装

> GitHub地址： [https://github.com/BVLC/caffe/tree/windows](https://github.com/BVLC/caffe/tree/windows)

* 有预编译版本，下载后可直接安装。


### Ubuntu 安装

* GitHub地址： [https://github.com/BVLC/caffe](https://github.com/BVLC/caffe)
* 官方安装地址： [http://caffe.berkeleyvision.org/install_apt.html](http://caffe.berkeleyvision.org/install_apt.html)

官方安装步骤如下：
1. [http://caffe.berkeleyvision.org/install_apt.html](http://caffe.berkeleyvision.org/install_apt.html)
2. [http://caffe.berkeleyvision.org/installation.html#compilation](http://caffe.berkeleyvision.org/installation.html#compilation)

16.04 python3.5 安装步骤如下：
1. 安装依赖
  ```
  sudo apt-get update
  sudo apt-get install -y build-essential cmake git pkg-config
  sudo apt-get install -y libprotobuf-dev libleveldb-dev libsnappy-dev libhdf5-serial-dev protobuf-compiler
  sudo apt-get install -y libatlas-base-dev
  sudo apt-get install -y --no-install-recommends libboost-all-dev
  sudo apt-get install -y libgflags-dev libgoogle-glog-dev liblmdb-dev
  ```

2. 安装OpenCV3
  * 详见[opencv.md](https://github.com/alisure-ml/Installation/blob/master/opencv.md)

3. 修改配置文件
  * 复制配置文件
  ```
  cp Makefile.config.example Makefile.config
  ```
  * 修改配置项
  ```
  # 取消注释
  CPU_ONLY := 1
  OPENCV_VERSION := 3
 
  # 包含和库路径保持同下面一致
  INCLUDE_DIRS := $(PYTHON_INCLUDE) /usr/local/include /usr/include/hdf5/serial
  LIBRARY_DIRS := $(PYTHON_LIB) /usr/local/lib /usr/lib /usr/lib/x86_64-linux-gnu /usr/lib/x86_64-linux-gnu/hdf5/serial /usr/share/OpenCV/3rdparty/lib/
  ```
4. 编译运行
  ```
  make all
  make test
  make runtest
  make pycaffe
  ```
  
5. 配置环境变量
  ```
  vim ~/.bashrc
  ```
  ```
  export PYTHONPATH=/caffe path/python:$PYTHONPATH
  ```

* 遇到的问题

0. 注意权限问题！！！

1. 编译时出现OpenCV3问题（OpenCV已成功安装）
  ```
  cv.imread().... 不存在。。。
  ```
  原因电脑上OpenCV版本有点多（乱），没有设置好OpenCV。
  
  * 解决办法   
  修改这一行，将`/usr/share/OpenCV/3rdparty/lib/`去掉：
  ```
  LIBRARY_DIRS := $(PYTHON_LIB) /usr/local/lib /usr/lib /usr/lib/x86_64-linux-gnu /usr/lib/x86_64-linux-gnu/hdf5/serial
  ```
  然后，解开这一行的注释
  ```
  USE_PKG_CONFIG := 1
  ```
  
  * linux下查看opencv版本
  ```
  pkg-config --modversion opencv
  ```
  

2. make pycaffe
  ```
  /usr/bin/ld: 找不到 -lboost_python3
  ```
  首先去/usr/lib/x86_64-linux-gnu目录下查看是否有python3版本的libboost，
  如果有类似libboost_python35.so但是没有libboost_python3.so则需要手动建立连接。 
  
  * 解决办法
  ```
  sudo ln -s libboost_python-py35.so libboost_python3.so 
  ```
  
  * reference 
    * [python3编译caffe错误:cannot find -lboost_python3](http://blog.csdn.net/songyu0120/article/details/77895373)


3. make: Nothing to be done for `all'

  * 解决办法
  ```
  make clean
  ```

4. 注意编译的时候python的版本。一定要在执行之前查看python的版本。毕竟工作站中的Linux系统的Python可能会比较乱，原因大家都懂的。


5. fatal error: hdf5.h:没有那个文件或目录

  * 解决办法
  ```
  将下句修改：
  INCLUDE_DIRS := $(PYTHON_INCLUDE) /usr/local/include
  为：
  INCLUDE_DIRS := $(PYTHON_INCLUDE) /usr/local/include /usr/include/hdf5/serial
  ```


* reference
  * [深度学习caffe:Ubuntu16.04安装指南(2)](http://www.cnblogs.com/AbcFly/p/6306201.html)

