如果之前没在ubuntu上安装过postgre那么这玩意绝对是顶级折磨，下面把我走的弯路说一下，希望后面的同志能够一遍成功少走弯路：

我建议别按照他给的readme里面的内容去配置postgre，这里有一篇博客，按照他这个配置：

[(2条消息) 如何在Ubuntu 22.04系统上安装PostgreSQL 15数据库 ?_鸠摩智首席音效师的博客-CSDN博客](https://blog.csdn.net/xiaochong0302/article/details/128032478)

一直配置到$ psql --version这条命令就可以

然后根据readme中的内容：

\

psql --user postgres

然后你可能发现登录不上，告诉你是authentic什么乱七八糟的，然后参考这篇文章：

[(2条消息) psql: error: FATAL: Peer authentication failed for user “postgres“_FatalFlower的博客-CSDN博客](https://blog.csdn.net/FatalFlower/article/details/114025262)

把能改的都改成trust，然后重新启动postgre服务，怎么重启呢？看这里：因为确实有的时候重启也会遇到问题，说什么没有这个server乱七八糟的。

[(2条消息) PostgreSQL启动，停止命令(重启)_postgresql启动命令_小龙哒的博客-CSDN博客](https://blog.csdn.net/u014131617/article/details/108262000#:~:text=PostgreSQL启动，停止命令 (重启) 1 1.先查看是否有postgresql服务,2 2. 关闭服务 3 3.启动服务)

然后按照readme里的内容把什么数据库、用户都创建好了，再看看他给的命令能不能执行了：

\

psql --user holocleanuser -W holo

应该就是可以的

我配置这玩意配置了三个半小时，我的评价就是别按照他的流程去下载那个postgre，很服。