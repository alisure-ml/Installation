## Pycharm远程

> 大家可以编辑修改这个文件，提交Pull requests.


## 服务器端

> 需要有ssh和ssh-server的支持

```
sudo apt install openssh-server
```

| 主机 | 域名 | 负责人 |
|---|---|---|
| TitanX + 48core + 256G | titanx.ddns.net | - |
| TitanX + 48core + 256G | action101.ddns.net | - |
| RTX2080Ti + 32core + 128G | faceid.ddns.net | - |
| RTX2080Ti + 32core + 128G | zshot.ddns.net | - |



## 客户端(PyCharm 2017)

1. GitHub上新建项目并在PC端下载项目

> 由于我的项目都同步到github上，所以先从这里开始。不在github上，直接下一步即可。

```
git clone https://github.com/ALISURE/pycharm_remote_demo.git
```

2. 用pycharm打开项目


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

* 上传： 在需要上传的文件上`右键 -> Upload to XXXX` 即可


* 运行：输出类似信息即可

```
os.platform=Linux-4.15.0-106-generic-x86_64-with-debian-buster-sid
```


5. 控制台

> Tools -> Start SSH Session...


