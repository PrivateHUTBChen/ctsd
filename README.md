# ctsd

### 描述

#### 项目内容

利用[kats](https://github.com/facebookresearch/Kats)进行时序数据预测。kats使用教程可参见本项目[tutorials](https://github.com/PrivateHUTBChen/ctsd/tree/main/tutorials)及[demo_kats](https://github.com/PrivateHUTBChen/ctsd/tree/main/demo_kats)。

#### 任务

- 专注于时序数据。
- 专注于算法验证。
- 尽可能多的寻找开源数据源领域在AIOPS类、 CPU、光纤、内存、磁盘、机械制造类（马达、轴承）等，然后用Kats中的方法对数据进行验证，汇报验证结果。

#### 待讨论

1. 对于分类问题，在数据不平衡的情况下，用什么标准来验证？
2. 预测问题，观察值和预测值之间的差异。

### 环境配置

建议使用python==3.8

```
pip install kats
```

### 错误解决

出现fbprophet错误，可参照[博客](https://blog.csdn.net/baidu_35108799/article/details/121383359)。

```
conda install -c anaconda ephem
# 安装pystan的版本应为2.19.1.1
pip install pystan
conda install -c conda-forge fbprophet
```

代码运行时报以下错误可参考该[issue](https://github.com/facebook/Ax/issues/1126)：

```
requires ax-platform be installed
```

遇到其他错误可在官方文档的issues里面搜索。
