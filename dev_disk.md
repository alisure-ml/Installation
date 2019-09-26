# 磁盘管理


## 挂载磁盘

> 假设设备为`/dev/sdc1`,要挂载的地方为`/home/ubuntu/ALISURE`

1. 查看是否挂载

```
df -h
```

原则上不会显示该磁盘，若出现异常情况，则进行卸载：
```
sudo umount /dev/sdc1 /home/ubuntu/ALISURE
```

2. 查看是否识别磁盘

```
sudo fdisk -l
```

原则上会显示该磁盘。

3. 磁盘格式化（请跳过该步骤，若确实需要格式化磁盘请三思后谨慎操作！！！）

```
sudo mkfs -t ext4 /dev/sdc1
```

4. 挂载磁盘

```
sudo mount /dev/sdc1 /home/ubuntu/ALISURE
```

可以指定磁盘格式： `ext4`,`vfat`（适用于FAT32），如：
```
sudo mount -t ext4 /dev/sdc1 /home/ubuntu/ALISURE
```

5. 配置硬盘在系统启动自动挂载（如果是U盘的话，此步不需要）

```
sudo vim /etc/fstab
```
加入：
```
/dev/sdc1 /home/ubuntu/ALISURE ext4 defaults 0 0
```

6. 挂载后设置权限

> 两种解决方案

1. FAT32不支持POSIX权限系统，可以把FAT32格式的U盘格式化为NTFS、Ext3或Ext4格式

2. 或者是挂载时加上参数`-o umask=000`: 
```
sudo mount -o umask=000 /dev/sdc1 /home/ubuntu/ALISURE
```

7. 挂载后文件名汉字乱码

> 挂载时加上参数`-o iocharset=utf8`
```
sudo mount -o umask=000 -o iocharset=utf8 /dev/sdc1 /home/ubuntu/ALISURE
```

8. 弹出磁盘

> 执行弹出之后，执行`sudo fdisk -l`就识别不了该磁盘了，因为已经弹出来了重新拔出插上才可以。

```
sudo eject /dev/sdc1
```


## 一些命令

### gparted

> gparted是ubuntu上很好的分区调整工具

* 安装
```
sudo apt-get install gparted
```

* 使用
```
sudo gparted
```


### df

* 常用命令, 可以查看各个盘分区使用及挂载情况. 
```
df
```

* 以GB之类显示而非字节
```
df -h
```

* 查看分区的文件系统类型
```
df -T
```

### lsblk

可以查看各个硬盘以及相应的分区和挂载情况
```
lsblk
```

### fdisk
可以查看各个硬盘的分区, 扇区情况等更详尽的信息
```
sudo fdisk -l
```

## Inference

* [Ubuntu--硬盘的挂载与卸载](https://www.cnblogs.com/cappuccinom/p/8971999.html)
* [linux系统挂载U盘，中文文件名乱码解决方案](https://www.cnblogs.com/zhouqinxiong/p/3497293.html)
* [解决U盘挂载到linux上没有写和执行的权限](https://blog.csdn.net/zgy0808/article/details/51082087)
* [Ubuntu命令行弹出光驱的方法](https://www.cnblogs.com/QuLory/archive/2012/10/23/2735489.html)


