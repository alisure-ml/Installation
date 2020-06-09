## 若发生一下错误，需要对gcc降级

```
error: #error -- unsupported GNU version! gcc versions later than 6 are not supported!
```

gcc版本太高，所以要降级：

```
sudo apt-get install gcc-6
sudo apt-get install g++-6
```

查看安装的gcc：

```
gcc -v
ls /usr/bin/gcc*
```

方法一：更改gcc的优先级：
```
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-6 60 --slave /usr/bin/g++ g++ /usr/bin/g++-6
```

方法二：创建软链接：
```
sudo ln -s /usr/bin/gcc-8 /usr/bin/gcc -f
sudo ln -s /usr/bin/gcc-ar-8 /usr/bin/gcc-ar -f
sudo ln -s /usr/bin/gcc-nm-8 /usr/bin/gcc-nm -f
sudo ln -s /usr/bin/gcc-ranlib-8 /usr/bin/gcc-ranlib -f
````

```
sudo ln -s /usr/bin/gcc-7 /usr/bin/gcc -f
sudo ln -s /usr/bin/gcc-ar-7 /usr/bin/gcc-ar -f
sudo ln -s /usr/bin/gcc-nm-7 /usr/bin/gcc-nm -f
sudo ln -s /usr/bin/gcc-ranlib-7 /usr/bin/gcc-ranlib -f
````

```
sudo ln -s /usr/bin/gcc-6 /usr/bin/gcc -f
sudo ln -s /usr/bin/gcc-ar-6 /usr/bin/gcc-ar -f
sudo ln -s /usr/bin/gcc-nm-6 /usr/bin/gcc-nm -f
sudo ln -s /usr/bin/gcc-ranlib-6 /usr/bin/gcc-ranlib -f
````

```
sudo ln -s /usr/bin/gcc-5 /usr/bin/gcc -f
sudo ln -s /usr/bin/gcc-ar-5 /usr/bin/gcc-ar -f
sudo ln -s /usr/bin/gcc-nm-5 /usr/bin/gcc-nm -f
sudo ln -s /usr/bin/gcc-ranlib-5 /usr/bin/gcc-ranlib -f
```

参考：[https://blog.csdn.net/qq_28660035/article/details/78703095](https://blog.csdn.net/qq_28660035/article/details/78703095)
