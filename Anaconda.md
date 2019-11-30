# Anaconda


## 清华大学的源

> [pypi 镜像使用帮助](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/)

* 临时使用

```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
```

注意，`simple`不能少, 是`https`而不是`http`。


* 设为默认(推荐使用该方法)

升级`pip`到最新的版本(>=10.0.0)后进行配置：

```
pip install pip -U
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

如果您到`pip`默认源的网络连接较差，临时使用本镜像站来升级`pip`：

```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U
```


## 安装

* 下载：[Anaconda Distribution](https://www.anaconda.com/distribution/)

* 安装:直接按照要求安装即可

```
sh ./Anaconda3-2019.07-Linux-x86_64.sh
```

有可能需要执行下列命令使环境变量有效：

```
source ~/.bashrc
```

* 检查更新

安装完成后，我们还需要对所有工具包进行升级，以避免可能发生的错误。

```
conda upgrade --all
```


## 管理Python包

安装一个 package：

```
conda install package_name
```

这里 package_name 是需要安装包的名称。

你也可以同时安装多个包，比如同时安装numpy 、scipy 和 pandas，则执行如下命令：

```
conda install numpy scipy pandas
```

你也可以指定安装的版本，比如安装 1.1 版本的 numpy ：

```
conda install numpy=1.10
```

移除一个 package：

```
conda remove package_name
```

升级 package 版本：

```
conda update package_name
```

查看所有的 packages：

```
conda list
```

如果你记不清 package 的具体名称，也可以进行模糊查询：

```
conda  search search_term
```


## 管理Python环境

> 新的环境保存在`~/anaconda3/envs`或`~/.conda/envs`中

默认的环境是 root，你也可以创建一个新环境：

```
conda create -n env_name  list of packages
```

其中 -n 代表 name，env_name 是需要创建的环境名称，list of packages 则是列出在新环境中需要安装的工具包。

例如，当我安装了 Python3 版本的 Anaconda 后，默认的 root 环境自然是 Python3，但是我还需要创建一个 Python 2 的环境来运行旧版本的 Python 代码，最好还安装了 pandas 包，于是我们运行以下命令来创建：

```
conda create -n py2 python=2.7 pandas
```

细心的你一定会发现，py2 环境中不仅安装了 pandas，还安装了 numpy 等一系列 packages，这就是使用 conda 的方便之处，它会自动为你安装相应的依赖包，而不需要你一个个手动安装。

进入名为 env_name 的环境：

```
source activate env_name
```

或者
```
conda activate env_name
```

退出当前环境：

```
source deactivate
```

或者
```
conda deactivate
```

另外注意，在 Windows 系统中，使用 activate env_name 和 deactivate 来进入和退出某个环境。

删除名为 env_name 的环境：

```
conda env remove -n env_name
```

显示所有的环境：

```
conda env list
```

当分享代码的时候，同时也需要将运行环境分享给大家，执行如下命令可以将当前环境下的 package 信息存入名为 environment 的 YAML 文件中。

```
conda env export > environment.yaml
```

同样，当执行他人的代码时，也需要配置相应的环境。这时你可以用对方分享的 YAML 文件来创建一摸一样的运行环境。

```
conda env create -f environment.yaml
```


## condarc

配置代理 `～/.condarc`

> [configuration/use-condarc](https://conda.io/projects/conda/en/latest/user-guide/configuration/use-condarc.html)


## 什么是 Anaconda

> Anaconda是专注于数据分析的Python发行版本，包含了conda、Python等190多个科学包及其依赖项。

conda 是开源包（packages）和虚拟环境（environment）的管理系统。

* packages 管理： 可以使用 conda 来安装、更新 、卸载工具包 ，并且它更关注于数据科学相关的工具包。
* 虚拟环境管理： 在conda中可以建立多个虚拟环境，用于隔离不同项目所需的不同版本的工具包，以防止版本上的冲突。


## Anaconda 的优点

> 省时省心、分析利器。

* 省时省心： Anaconda通过管理工具包、开发环境、Python版本，大大简化了你的工作流程。不仅可以方便地安装、更新、卸载工具包，而且安装时能自动安装相应的依赖包，同时还能使用不同的虚拟环境隔离不同要求的项目。
* 分析利器： 适用于企业级大数据分析的Python工具。其包含了720多个数据科学相关的开源包，在数据可视化、机器学习、深度学习等多方面都有涉及。不仅可以做数据分析，甚至可以用在大数据和人工智能领域。


## Reference

* [致Python初学者：Anaconda入门使用指南](http://python.jobbole.com/87522/)
