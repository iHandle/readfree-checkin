## Readfree自动签到脚本

使用cookie的Readfree自动签到脚本，支持将签到结果推动到iPhone.
PS: 现在Readfree的cookie有效期只有一周，所以如果你要什么更好的解决办法，欢迎一起讨论.

### 使用方法

#### 修改脚本
1. `cookie`字典有三处标记了[此处需要修改]的地方.使用Chrome等浏览器手动登录Readfree后可以获取cookie，然后根据对应的字段修改字典的值.（ [Chrome查看cookie参考](https://www.cnblogs.com/zj0208/p/6249759.html) ）
2. 将`confirm`函数的`url`中标记为[此处需要修改为你的Readfree用户名]修改好.
3. 如果需要使用Bark推送，根据注释提示修改`bark_url`，然后去掉最后两行代码的注释.（[Bark使用方法](https://github.com/Finb/Bark/blob/master/README.md)）

#### 依赖部署(已部署的请忽略)
1. python环境:  [Python 环境搭建](http://www.runoob.com/python/python-install.html)
2. 依赖模块: `pip install beautifulsoup4, requests`

#### 定时运行
以Linux为例，使用crontab定时运行脚本，每天`00:00`的时候就会自动签到.（[crontab教程](http://www.runoob.com/linux/linux-comm-crontab.html)）

根据`readfree.py`放置的目录给crontab添加以下格式的定时计划:

	@daily python PATH_TO_YOUR_readfree.py >/dev/null 2>&1

假如你的`readfree.py`文件是放在目录`/home/abc`下的，那么以上命令应该改为:

	@daily python /home/abc/readfree.py >/dev/null 2>&1

`>/dev/null 2>&1` 语句含义: 不会输出任何信息到控制台，也不会有任何信息输出到文件中。

#### 注意事项
注意检查Linux的时区是否为东8区. 否则crontab执行脚本的时间会与你设想的时间不一样.

	date -R

### 博客
[readfree.me自动签到脚本(python)](https://www.jianshu.com/p/2828d36b9ba5)