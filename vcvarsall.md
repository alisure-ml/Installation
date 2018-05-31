# vcvarsall

> 在Win10系统中，执行`pyhton setup.py xxx`时报错：`error: Unable to find vcvarsall.bat`

* 环境：Win10 + python3.5

## 解决办法

* 安装VS2017/VS2015：勾选v140工具集


## 在解决过程中可能会出现下列错误

```
fatal error LNK1158: cannot run "rc.exe"
error: command 'C:\\Program Files (x86)\\Microsoft Visual Studio 14.0\\VC\\BIN\\x86_amd64\\link.exe' failed with exit status 1158
```

* 解决办法：在`C:\\Program Files (x86)`下搜索`rc.exe`,将所在目录添加到`PATH`环境变量中即可。
比如我的是：`C:\Program Files (x86)\Windows Kits\10\bin\10.0.17134.0\x86`


## Inference

* [python3.5 安装报错error: Unable to find vcvarsall.bat](https://www.cnblogs.com/bigvase/p/6512476.html)

* [Windows下安装Python扩展模块提示“Unable to find vcvarsall.bat”的问题](https://www.cnblogs.com/yyds/p/7065637.html)

* [How to deal with the pain of “unable to find vcvarsall.bat”](https://blogs.msdn.microsoft.com/pythonengineering/2016/04/11/unable-to-find-vcvarsall-bat)

* [error: command 'C:\\Program Files (x86)\\Microsoft Visual Studio 14.0\\VC\\BIN\\x86_amd64\\link.exe' failed with exit status 1158](https://www.jianshu.com/p/957621736210)
