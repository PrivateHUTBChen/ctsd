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

本项目为AIOps团队共用项目，在进行更改之前，请阅读以下内容。

### 本地检查`Pull requests`请求

有人发送`Pull requests`时，可以在 GitHub 上合并之前[测试并验证更改](https://docs.github.com/zh/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/checking-out-pull-requests-locally)。

### 开源项目管理

#### git管理

以下方式可二选其一，也可相辅相成：

- [命令管理](https://blog.csdn.net/weixin_45682261/article/details/124003706)；
- 工具管理：利用可视化工具[TortoiseGit](https://blog.csdn.net/xwnxwn/article/details/108694863)进行项目管理。

#### 代码提交

先进行本地提交（参考可视化工具管理），然后[推送到开源仓库](https://zhuanlan.zhihu.com/p/23457016)。

## 环境配置

### 包导入

创建环境时建议使用的python为3.8。

建议采用anaconda导入kats：

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

