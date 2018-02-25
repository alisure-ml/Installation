
### 环境变量
> 解决环境变量问题

出现下列问题：

* 运行Tensorflow需要在`Pycharm`中设置`LD_LIBRARY_PATH=/usr/local/cuda/lib64`的问题

* `Pycharm`中不能找到caffe包的问题


### 解决方法

1. 打开系统环境变量
```
CTRL + ALT + T
sudo gedit /etc/profile
```

2. 添加环境变量
```
export PATH=/usr/local/cuda-8.0/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda-8.0/lib64:$LD_LIBRARY_PATH

export PYTHONPATH=/you/path/of/caffe/python:$PYTHONPATH
```

3. 生效修改
```
source /etc/profile
```

4. 此时在命令行中已经生效，但是在Pycharm中还未生效
```
重启电脑即可
```


### 环境变量

> 有多种设置环境变量的方式，比如：系统级环境变量，用户级环境变量，终端级环境变量

1. 系统级环境变量：对所有用户生效的永久变量
```
sudo gedit /etc/profile
```

用`export`指令添加环境变量。   

添加完成后新的环境变量不会立即生效，除非你调用source /etc/profile 该文件才会生效。
否则只能在下次重进此用户时才能生效。

```
source /etc/profile
```


2. 用户级环境变量：只对当前的用户永久生效
> 在`.bashrc`和`.bash_profile`中都可以设置此类环境变量。
`.bash_profile`文件只会在用户登录的时候读取一次，而`.bashrc`在每次打开终端进行一次新的会话时都会读取。

```
sudo gedit ~/.bashrc
```

用`export`指令添加环境变量。   

添加完成后新的环境变量不会立即生效，除非你调用source ~/.bash_profile 该文件才会生效。
否则只能在下次重进此用户时才能生效。


3. 终端级环境变量：只对当前shell有效
> 此类环境变量只对当前的shell有效。当退出登录或者关闭终端再重新打开时，这个环境变量就会消失。

直接使用`export`指令添加。



### Reference

* [Linux环境变量及其设置](http://blog.csdn.net/llzk_/article/details/53813266)
