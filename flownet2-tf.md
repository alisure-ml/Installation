## make的问题

### 1

```
ModuleNotFoundError: No module named 'tensorflow'
```

忘记激活环境了：

```
source activate alisure36
```

### 2

```
error: #error -- unsupported GNU version! gcc versions later than 6 are not supported!
```

gcc版本太高，所以要降级：

```
sudo apt-get install gcc-6
sudo apt-get install g++-6
```

查看安装的gcc：

```
gcc -v
ls /usr/bin/gcc*
```

方法一：更改gcc的优先级：
```
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-6 60 --slave /usr/bin/g++ g++ /usr/bin/g++-6
```

方法二：
```
sudo ln -s /usr/bin/gcc-7 /usr/bin/gcc -f
sudo ln -s /usr/bin/gcc-ar-7 /usr/bin/gcc-ar -f
sudo ln -s /usr/bin/gcc-nm-7 /usr/bin/gcc-nm -f
sudo ln -s /usr/bin/gcc-ranlib-7 /usr/bin/gcc-ranlib -f
````

```
sudo ln -s /usr/bin/gcc-6 /usr/bin/gcc -f
sudo ln -s /usr/bin/gcc-ar-6 /usr/bin/gcc-ar -f
sudo ln -s /usr/bin/gcc-nm-6 /usr/bin/gcc-nm -f
sudo ln -s /usr/bin/gcc-ranlib-6 /usr/bin/gcc-ranlib -f
````

```
sudo ln -s /usr/bin/gcc-5 /usr/bin/gcc -f
sudo ln -s /usr/bin/gcc-ar-5 /usr/bin/gcc-ar -f
sudo ln -s /usr/bin/gcc-nm-5 /usr/bin/gcc-nm -f
sudo ln -s /usr/bin/gcc-ranlib-5 /usr/bin/gcc-ranlib -f
```

参考：[https://blog.csdn.net/qq_28660035/article/details/78703095](https://blog.csdn.net/qq_28660035/article/details/78703095)


### 3

```
/home/ubuntu/miniconda3/envs/alisure36/lib/python3.6/site-packages/tensorflow/include/tensorflow/core/util/cuda_device_functions.h:32:31: fatal error: cuda/include/cuda.h: No such file or directory
 #include "cuda/include/cuda.h"
```

在nvcc中加入下列搜索路径：
```
-I"/usr/local"
```

* 原因分析

当打开`cuda_device_functions.h`会发现：
```
#include <algorithm>
#include <complex>
#include "third_party/eigen3/unsupported/Eigen/CXX11/Tensor"
#include "cuda/include/cuda.h"
#include "tensorflow/core/platform/types.h"
```

所以，是没有把`/usr/local`加入到搜索路径中。


### 4

```
/home/ubuntu/miniconda3/envs/alisure36/lib/python3.6/site-packages/tensorflow/include/absl/strings/string_view.h(501): error: constexpr function return is non-constant
```

在nvcc中加入`-DNDEBUG`即可。

```
 -DNDEBUG
```

解决办法来自：[https://github.com/tensorflow/tensorflow/issues/22766](https://github.com/tensorflow/tensorflow/issues/22766)


### 5

```
/home/ubuntu/miniconda3/envs/alisure36/lib/python3.6/site-packages/tensorflow/include/tensorflow/core/util/cuda_device_functions.h(523): error: calling a constexpr __host__ function("real") from a __device__ function("CudaAtomicAdd") is not allowed. The experimental flag '--expt-relaxed-constexpr' can be used to allow this.
```

按照提示，在nvcc中加入`--expt-relaxed-constexpr`即可。

```
--expt-relaxed-constexpr
```


### 总结

```
GPUCC     = nvcc
CFLAGS    = -std=c++11 -I$(TF_INC) -I"$(CUDA_HOME)/include" -I"/usr/local" -DGOOGLE_CUDA=1 --expt-relaxed-constexpr -DNDEBUG
```

主要是对gcc不熟，对nvcc命令不熟。以后加强在这方面的学习。

