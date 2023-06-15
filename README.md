# ctsd

## 描述

### 项目内容

利用[kats](https://github.com/facebookresearch/Kats)进行时序数据预测。kats使用教程可参见本项目[tutorials](https://github.com/PrivateHUTBChen/ctsd/tree/main/tutorials)及[demo_kats](https://github.com/PrivateHUTBChen/ctsd/tree/main/demo_kats)。

### 任务

- 专注于时序数据。
- 专注于算法验证。
- 尽可能多的寻找开源数据源领域在AIOPS类、 CPU、光纤、内存、磁盘、机械制造类（马达、轴承）等，然后用Kats中的方法对数据进行验证，汇报验证结果。

### 待讨论

1. 对于分类问题，在数据不平衡的情况下，用什么标准来验证？
2. 预测问题，观察值和预测值之间的差异。

## 贡献指南

本项目为AIOps团队共用项目，在进行更改之前，请阅读[贡献指南](https://github.com/OpenHUTB/bazaar/blob/master/CONTRIBUTING.md)文档。

## 环境配置

### 包导入

建议使用python==3.8

```
pip install kats
```

### 错误解决

- 出现fbprophet错误，可参照[博客](https://blog.csdn.net/baidu_35108799/article/details/121383359)：


```
conda install -c anaconda ephem
# 安装pystan的版本应为2.19.1.1
pip install pystan
conda install -c conda-forge fbprophet
```

- 代码运行时报以下错误可参考该[issue](https://github.com/facebook/Ax/issues/1126)：


```
requires ax-platform be installed
```

- 出现“packaging.version”错误：


```
# 遇到以下错误：
module 'packaging.version' has no attribute 'LegacyVersion'
# 解决方案：
conda install packaging=21.3
```

- 出现“object.**init**() takes exactly one argument”错误：

```
pip install holidays==0.10.2
```

遇到其他错误可在官方文档的[issues](https://github.com/facebookresearch/Kats/issues)里面搜索。

