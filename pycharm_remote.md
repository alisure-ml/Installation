## Pycharm远程

## 服务器端

> 需要有ssh和ssh-server的支持

```
sudo apt install openssh-server
```


## 客户端

1. GitHub上新建项目

> 由于我的项目都同步到github上，所以先从这里开始。


2. PC端下载项目后用pycharm打开

```
git clone https://github.com/ALISURE/pycharm_remote_demo.git
```

或

```
在pycharm中打开
```


3. 配置

* Tools -> Deployment -> Configuration

  1. 输入名称，选择Type：SFTP
  
  2. 配置：Connection 和 Mappings
  

* Project Interpreter

  1. 在Project配置即可：Add Remote -> SSH Credentials

  2. 添加Host、User name、Password、Python interpreter path


* Path mappings

  > 配置路径映射关系即可
  


4. 测试

* 新建 `demo.py`

```
import platform

if __name__ == '__main__':
    print("os.platform={}".format(platform.platform()))
    pass
```

* 运行：输出类似信息即可

```
os.platform=Linux-4.15.0-106-generic-x86_64-with-debian-buster-sid
```




