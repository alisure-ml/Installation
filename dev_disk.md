# 磁盘管理


## gparted

> gparted是ubuntu上很好的分区调整工具

* 安装
```
sudo apt-get install gparted
```

* 使用
```
sudo gparted
```


## df

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

## lsblk

可以查看各个硬盘以及相应的分区和挂载情况
```
lsblk
```


