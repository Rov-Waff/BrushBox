# 盒子 IM 刷屏器

为[盒子 IM](http://www.boxim.online)做的一个刷屏工具，基于 PySide6 构建了 UI

## 安装

在 Release 里下载 whl 包进行安装，PyPI 上没有，因为我把我的 2FA 丢了

## 使用

你可以使用 cli 或者 gui 进行刷屏，对于 cli，使用指令：

```bash
$ python3 -m brushbox [token] [内容] [群id] [次数]
```

对于 GUI，使用该指令打开 GUI

```bash
$ python3 -m brushbox.gui
```

## 获取Token和群ID

进入你的群，按下<kbd>F12</kbd>打开开发者工具，切换到网络面板，进入群，发送一条信息，其中`Accesstoken`这个请求头为Token，请求体中`groupID`为群id

## 开源

使用MIT License进行开源