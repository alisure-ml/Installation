## Shadowsocks的使用


## 目前方案

> 到vultr上开一台服务器，然后下载东西，使用SSH传过来。


* wget

`wget xxx`

* curl

`curl xxx --output xxx`

* axel

```
sudo apt-get install axel
axel xxx
```


## 购买国外服务器

* [https://www.vultr.com/](https://www.vultr.com/), [https://my.vultr.com/](https://my.vultr.com/)

* 注册（562282219@qq.com, a*A）

* 充值

* 选择最便宜的服务器并部署

* 此时，会获得服务器IP、用户名、密码等信息


## 登录服务器

> 使用SSH客户端连接服务器：BvSshClient或Putty


## 配置防火墙

* 安装

```
yum install firewalld
systemctl start firewalld
```

* 启动

```
firewall-cmd --permanent --zone=public --add-port=443/tcp
firewall-cmd --reload
```

上述端口号`443`要和Shadowsocks的`server_port`一样。


## 服务器端安装Shadowsocks

* `pip install shadowsocks`


* 修改`openssl.py`文件：`vim /usr/local/lib/python3.6/site-packages/shadowsocks/crypto/openssl.py`

将所有`EVP_CIPHER_CTX_cleanup`替换成为`EVP_CIPHER_CTX_reset`（有两处）。


* `vim /etc/shadowsocks.json`

```
{
    "server":"0.0.0.0",
    "server_port":443,
    "local_address": "127.0.0.1",
    "local_port":1080,
    "password":"123456",
    "timeout":300,
    "method":"aes-256-cfb",
    "fast_open": false
}
```

* 启动Shadowsocks服务

前台启动：
```
ssserver -c /etc/shadowsocks.json
```

后台启动：
```
nohup ssserver -c /etc/shadowsocks.json &
```


## 客户端配置

* 下载`Shadowsocks`

* 按以下操作设置：

打开->服务器->编辑服务器->设置服务器地址、端口、密码、加密方式、代理端口等（和服务器端的shadowsocks.json设置一样）。

* 设置`系统代理`为`全局代理`。

如果不想用的话，可以设置为`禁用`。


## 浏览器设置

* 下载插件`SwitchyOmega`

* 选择`系统代理`即可，如果不想使用则选择`直接代理`。



## Reference

* [国外服务器如何选择以及搭建ShadowSocks教程](https://segmentfault.com/a/1190000015387870?utm_source=tag-newest)

