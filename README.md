# Interview-quwstion-collectiom-system
Use web crawler to collect interview questionsUse web crawler to collect interview questions.

## 可以自己修改filter 和配置文件进行网站收录，目前就收录了一个网站
## 仅用于学习研究不得用于商业用途
--
--
## 1、配主要置模块

    time
    os
    bs4
    jsonpath
    lxml
    threading
    requestes
    tkinter


## 2、目录、文件说明
 ### 目录

    bg : 背景图片目录
    CN_DOM ：默认的获取文件保安存路劲(获取文件、记录文件)
    IP : 自动收集网络开放代理并进行校验保存（文档/数据库）
    
### 文件

    config.py : 配置文件，可以通过修改参数实现不同的抓取需求
    de_duplication.py : MD5 指纹生产已保存，以及下载审查，防止重复抓取
    fliter : 过滤策略文件与爬虫文件（包含文件过滤与下载的方法）
    atoconfig.py : 获取用户配置修改默认配置
    qemail.py : 邮件
    random_centes.py : 随机一句、天气函数
    singlers.py : 线程终止
    welcom.py : 界面 、逻辑函数
    A2.0.py ： 入口

## 3、运行方法：
    运行 A2.0.py 文件.

##4、 其他抓取需求或者路径修改：

    方法一、修改config.py 文件的参数：具体看config.py 文件
    方法二、 界面传入

