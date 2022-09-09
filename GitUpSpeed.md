
### Linux

## 1

```
sudo gedit /etc/hosts
```

```
140.82.114.10 codeload.github.com
140.82.114.4 github.com
185.199.109.154 github.githubassets.com
199.232.69.194 github.global.ssl.fastly.net
52.217.18.198 s3.amazonaws.com
```


## 2

```
sudo /etc/init.d/networking restart
```

### Windows


> 现象：`ping github.com`不通


* 在`C:\Windows\System32\drivers\etc\hosts`中加入一下内容

```
140.82.113.4 github.com
185.199.108.153 assets-cdn.github.com
185.199.109.153 assets-cdn.github.com
185.199.110.153 assets-cdn.github.com
185.199.111.153 assets-cdn.github.com
185.199.108.154 github.githubassets.com
185.199.109.154 github.githubassets.com
185.199.110.154 github.githubassets.com
185.199.111.154 github.githubassets.com
199.232.69.194 github.global.ssl.fastly.net
```

* 刷新

```
ipconfig /flushdns      //清除DNS缓存内容

ipconfig /displaydns    //显示DNS缓存内容
```



