# 磁盘管理


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

```

```

