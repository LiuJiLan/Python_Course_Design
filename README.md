# Python_Course_Design
本科阶段Python结课课设,C语言永远的神.

## 有关项目
- 个人不常写纯Python, 应该说Cython写的都比Python多
- 如果项目中与README中有纰漏, 请多多海涵

## 缺点
- 现在管理员和一般用户的区别是靠UI控件的走向来控制的, 之后应该改为每个指令都需要服务器确认

## 有关打包生成最终的应用
- 最好在虚拟环境下打包, 可以减少包大小, 个人的结果在30M以下(MacOS应用)
- 如果你打包超过这个值可能要考虑是否存在问题(MacOS的包通常是最大的)
- 唯一确信需要提前准备的包是`PyMySQL`和`cryptography`(后者虽没有直接使用, 但前者需要后者)
- 这两个包下载完之后再添加`pyinstaller`
- 个人是个用PyCharm的懒人, 似乎在安装这些包之后会多出一些其他的包, 由于平时很少导包, 几乎都是需要自己重写包的情况, 就看着PyCharm中的简介删删减减了一些, 如果漏掉了什么请帮我指出
- 打包命令`pyinstaller src/School_Books_Management_System.py -w -i src/assets/images/icon.ico`

### 有关tkinter
- tkinter是一个Python内置的模块,至少Python官方是这么说的
- 但对于部分类Unix系统中Python不包含tkinter模块
- 例如MacOS中brew就提示了这一点, `brew info python`可获得相关信息
- 对于很多Linux系统也可以改为安装python-tk来解决
- 对于PyCharm则是安装future package(实在不知道怎么装等PyCharm反义一会就会有提示了)

## 关于贡献者
- 在一个全是导包的项目里提贡献者真的没有什么意义, 但毕竟这涉及到这门课分数的评定
- 本次开发一直在使用GitHub Desktop, 结果整个几乎全部做完了才发现本地设置的账号有问题, 所以显示的贡献者有两人
- 但这两人均是本人

## 关于改写项目(如果真的有的话)
- 这个项目写地真的很一般, 整个项目都是我一个赶出来的, 里面估计还会有BUG, 但是就这样了
- 如果说这个项目大部分地方都能算是凑合, GUI的设计真的就是rubbish
- 我真的没有什么美术天分, 然后在短短的几天内边干这干那地摸鱼边做完的这个项目我也没什么精神去做GUI设计了
- 所有的数据都是用`0.618:1`给算出来的, 后面的部分干脆就在Adobe XD中随便画了画
- 如果你真的想借鉴, 建议先把所有的`.place(……)`的部分改为`.pack()`, 看看每个页面有几个控件然后自己给画画GUI的好

## 写在最后的话
- 有关项目的开发流程可以通过查看GitHub来了解.
- https://github.com/LiuJiLan/Python_Course_Design
