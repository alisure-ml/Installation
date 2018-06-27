# PyTorch

## 方法一：pip安装

* Python3.6+pip安装cpu版本

```
pip install http://download.pytorch.org/whl/cpu/torch-0.4.0-cp36-cp36m-win_amd64.whl
```

* Python3.5+pip安装cpu版本

```
pip install http://download.pytorch.org/whl/cpu/torch-0.4.0-cp35-cp35m-win_amd64.whl
```

* Python3.6+pip安装gpu版本

```
# 目前gpu版本支持cuda8.0,cuda9.0和cuda9.1，请选择对应的版本下载安装，不要同时执行下面三个命令！
pip install http://download.pytorch.org/whl/cu80/torch-0.4.0-cp36-cp36m-win_amd64.whl  
pip install http://download.pytorch.org/whl/cu90/torch-0.4.0-cp36-cp36m-win_amd64.whl 
pip install http://download.pytorch.org/whl/cu91/torch-0.4.0-cp36-cp36m-win_amd64.whl 
```

* Python3.5+pip安装gpu版本

```
# 目前gpu版本支持cuda8.0,cuda9.0和cuda9.1，请选择对应的版本下载安装，不要同时执行下面三个命令！
pip install http://download.pytorch.org/whl/cu80/torch-0.4.0-cp35-cp35m-win_amd64.whl
pip install http://download.pytorch.org/whl/cu90/torch-0.4.0-cp35-cp35m-win_amd64.whl
pip install http://download.pytorch.org/whl/cu91/torch-0.4.0-cp35-cp35m-win_amd64.whl
```


## 方法二：Conda安装

* 如果你是Anaconda|Python用户，就不需要区分Python3.5和Python3.6，执行命令:

```
conda install pytorch -c pytorch 
```

就可以完成安装。不过这个默认安装的是cuda8.0的gpu版本,如果你需要安装cuda9.0或cuda1.0的gpu版本，请执行来进行安装：

```
conda install pytorch cuda90 -c pytorch
# 或者
conda install pytorch cuda91 -c pytorch
```


## 测试安装是否成功

```
import torch
print(torch.__version__)
```

如果输出0.4.0，那么恭喜Windows下的PyTorch0.4.0安装成功！


## 最后需要安装 torchvision：

```
pip install torchvision
```
