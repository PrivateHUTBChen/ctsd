# ctsd
#### 描述

利用[kats](https://github.com/facebookresearch/Kats)进行时序数据预测。

#### 环境配置

建议使用python==3.8

```
pip install kats
```

##### 错误解决

出现fbprophet错误，可参照[博客](https://blog.csdn.net/baidu_35108799/article/details/121383359)。

```
conda install -c anaconda ephem
# 安装pystan的版本应为2.19.1.1
pip install pystan
conda install -c conda-forge fbprophet
```

遇到其他错误可在官方文档的issues里面搜索。

