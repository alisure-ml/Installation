## 国内如何下载huggingface模型、数据集


### huggingface-cli

huggingface-cli是 Hugging Face 官方提供的命令行工具，自带完善的下载功能。

#### 1. 安装依赖
```
pip install -U huggingface_hub
```

#### 2. 设置环境变量
```
Linux
export HF_ENDPOINT=https://hf-mirror.com
```
```
Windows Powershell
$env:HF_ENDPOINT = "https://hf-mirror.com"
```

建议将上面这一行写入 ~/.bashrc。


#### 3.1 下载模型
```
gpt2
huggingface-cli download --resume-download gpt2 --local-dir gpt2
```
```
chatglm-6b
huggingface-cli download --resume-download THUDM/chatglm-6b --local-dir model
```

#### 3.2 下载数据集
```
huggingface-cli download --repo-type dataset --resume-download cifar10 --local-dir cifar10
```

在代码中使用下载的地址即可，例如`/home/abc/.cache/huggingface/datasets/cifar10`

#### Reference

原文链接：https://blog.csdn.net/tangsiqi130/article/details/136815313
