# opencv

## 方法一
* pip install opencv-python

## 方法二

* 安装OpenCV的依赖包

```
# 编译器
sudo apt-get install build-essential
# 必须安装
sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodedec-dev libavformat-dev libswscale-dev
# 可选安装
sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev
```

* 从源代码构建OpenCV

下载opencv:[https://opencv.org/releases.html](https://opencv.org/releases.html)

解压后运行以下命令:

```
mkdir build
cd build
cmake –D CMAKE_BUILD_TYPE=Release –D CMAKE_INSTALL_PREFIX=/usr/local ..
make
make install
```

* 若在python下运行opencv库，必须安装如下

```
sudo apt-get install python-opencv
```

完成上述流程即安装完成

* 进行测试，检查opencv是否安装成功

到opencv自带的samples文件夹，然后运行一个.py的文件，如果没有提示出错则正确。例如：

```
python kmeans.py
```

则会出现kmeans的分类图形。

