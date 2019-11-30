## 实验室设备情况说明

> 用来记录实验室设备的故事

### 门口的工作站

> 该工作站的系统比较老旧，需要重装系统！

1. 重大更新：（2019-11-30）
  
  > 系统环境：`CUDA9.2`、`Anaconda2`、`NVIDIA-Linux-x86_64-390.87`
  
  > 由于跑`tensorflow`的代码，需要`tensorflow 1.11.0`，从而需要`CUDA9.0`。另一方面，又想安装`Anaconda3`（`Anaconda3-2019.07-Linux-x86_64.sh`）。
  
  * 安装`CUDA9.0`后不管用，折腾了半天，因此想卸载`CUDA9.2`。
  
  * `CUDA9.2`卸载之后，又重新安装`NVIDIA`显卡驱动（`NVIDIA-Linux-x86_64-390.87.run`），之后安装`CUDA9.0`，然后就**神奇的可用了**！！！！
  注意，此时没有安装`cudnn`。
  
  > 至此，虽然可用了，但是非常迷惑！！！！
  
  * 然后就想着安装了`cudnn`了事。安装的版本是`libcudnn7_7.0.5.15-1+cuda9.0_amd64`，结果报错：
  
  ```
  Loaded runtime CuDNN library: 7.0.5 but source was compiled with: 7.2.1.
  ```
  
  > 这么看来，`tensorflow`运行的时候去`/usr/local/cuda-9.0`中寻找了`cudnn`，只不过因为版本不对，报了错误。
  因此，猜测肯定在系统中的某个地方有正确的`cudnn`。
  
  * 果然，找到了可疑的地方：`Anaconda2`的`pkgs`中存在`cudnn`。
  
  可能的原因是：运行时调用的`cudnn`是`Anaconda2`中的`cudnn`。 
  
  > reference: [Tensorflow的大坑](https://blog.csdn.net/Tilamy/article/details/88616201)

  * 最终，没有安装`cudnn`，先凑合着用吧，以后会重装系统的。毕竟还有格权限乱用的问题没有解决！！！
  
  
