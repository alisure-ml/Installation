## 加速训练

> 将数据挂载到内存虚拟硬盘，从而加快训练。


## 步骤

1. 创建目录

```
sudo mkdir /mnt/4T/tmp_train_data
```

2. 挂载

```
sudo mount -t tmpfs -o size=40G tmpfs /mnt/4T/tmp_train_data
```

3. 查看

```
df -h
```


4. 将数据放入使用`/mnt/4T/tmp_train_data`即可


## Reference

1. [Ubuntu内存虚拟硬盘——tmpfs](https://blog.csdn.net/qq_29912325/article/details/108666516)

2. [liunx 内存文件 tmpfs](https://www.cnblogs.com/zhangeamon/p/5457432.html)

3. [Linux mount命令](https://www.runoob.com/linux/linux-comm-mount.html)

4. [deepinsight/insightface](https://github.com/deepinsight/insightface/blob/master/challenges/iccv21-mfr/tutorial_pytorch_cn.md)


