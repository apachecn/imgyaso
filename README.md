# ImgYaso

提供多种图像处理工具，包括自适应二值化，灰度网格仿色，扩散仿色，和颜色缩减。

## 安装

通过pip（推荐）：

```
pip install imgyaso
```

从源码安装：

```
pip install git+https://github.com/apachecn/imgyaso
```

## 使用说明

```
imgyaso [-h] [-v] [-c COLORS] [-m {grid,noise,trunc,quant,thres}]
        [-o OFNAME]
        fname
        
-c COLORS: 颜色数，只对 trunc, quant 模式有效
-m MODE: 模式名称，值为 grid（灰度网格仿色），noise（灰度扩散仿色），
         trunc（灰度截断），quant（颜色缩减），thres（自适应二值化），
         默认为 grid
-o OFNAME: 输出文件名称，默认和输入文件相同
fname: 输入文件名称
```

## 协议

本项目基于 SATA 协议发布。

您有义务为此开源项目点赞，并考虑额外给予作者适当的奖励。

## 赞助我们

![](https://home.apachecn.org/img/about/donate.jpg)

## 另见

+   [ApacheCN 学习资源](https://docs.apachecn.org/)
+   [计算机电子书](http://it-ebooks.flygon.net)
+   [布客新知](http://flygon.net/ixinzhi/)
