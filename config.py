# --coding:GBK --
import random,os


# 是否每次运行前 初始化
reback = False

# 请求延迟
slpt = 5


# 具体文章片数 = Mpage * 36 * key_word
MPage = 20

# 运行状态
Statatus =['启动中','正在运行','发生错误','运行结束','停止']

CSDN = {
    'log_path':'./CN_DOM/info.txt',
    'erro_log_path':'./CN_DOM/erro.txt',
    'save_path':'./CN_DOM',
    'remenber':'./CN_DOM/remenber.csv',
    'email':'NONE',

    # 用户输入，关键字、最近几年的内容、文档标题必须存在的内容.
    # 深度学习相关
    'key_word':['深度学习面试','AI面试','人工智面试'],
    'flag':3, #
    'consume': ['深度学习', '机器学习', '面试', '考试', '问题', '大厂', 'AI',
               '人工智能', '学习', '总结', '知识'],  # 文章标题确认，不包含其中任何两项直接过滤

    # 通用配置，过滤标题以及url存在这些字符的内容,一般不用修改，通用配置
    'fl_url':['book','download','GitChart','weixin'], # url 包含这些过滤掉
    'fl_title':['资源','下载','PDF','价格，’目录','指导手册','课程','大全'
                '书籍','前端','实战','宝典'], # 标题 过滤
 }

# 初始化，更新源文件
def inite():
    paths = ['log_path','erro_log_path','remenber','save_path']
    for i in paths:
        if os.path.isfile(CSDN[i]):
            try:
                os.makedirs(CSDN[i])
            except Exception as e :
                print(e)

def check_and_creat_dir():
    '''
    判断文件是否存在，文件路径不存在则创建文件夹
    :param file_url: 文件路径，包含文件名
    :return:
    '''
    paths = ['log_path', 'erro_log_path', 'remenber']
    for file_url in paths:
        file_gang_list = CSDN[file_url].split('/')
        if len(file_gang_list) > 1:
            [fname, fename] = os.path.split(CSDN[file_url])
            print(fname, fename)
            if not os.path.exists(fname):
                try:
                    os.makedirs(fname)
                except:
                    pass
            else:
                return None
            # 还可以直接创建空文件

        else:
            return None

check_and_creat_dir()


# 用户须知
foruser = '\n   该系统用于辅助用户收集技术类博文、试题等\n'\
          '学习资料,用户可以根据需要对配置文件进行修改\n'\
          '以实现不同的数据收集需求，系统运行被严格限速,\n'\
          '没有企图、设计破解网站加密等破坏他人权益行为\n'\
          '使用者应当限制自己的收集行为,不能频繁使用。系\n'\
          '统每次运行访问都会产生记录文件默认情况系统不\n'\
          '会清理，如果您想每次运行都初始化系统,见说明\n'\
          '直接修改配置,问题联系3173362514@qq.com。如果\n'\
          '有侵犯您的权益的行为希望您及时反馈，好及时处\n' \
          '理,减少您的损失。后期系统会继续升级。希望在\n' \
          '学习上可以帮助大家。最后祝您生活愉快、学有所\n' \
          '成、事业顺利!'

# 信息
infomation = '系统默认应用启动前后不就行初始化，保留历史数据用于以后校验,防止重复抓取、' \
             '如果想修改，请将config.py下的 "reback"设为True，其他配置请查阅config.py 文件'

#
helpinfo = '1、进入系统后请查阅用户须知。                            \n' \
           '2、进入配置，输入收集文件的保存地址。                      \n' \
           '3、如果配置完成，就可以进入控制面板，可以开启命令进行收集任务。 \n' \
           '4、控制面板你可以查看大致相同运行状况，也可以强制终止任务。    \n' \
           '5、程序运行中请不要关闭面板，以免程序异常退出。              \n' \
           '6、程序每次运行都会产生记录文件，用于过滤数据，如果想要进行初始化\n' \
           '   操作请删除目录下DOM/remenber.csv 文件                 \n' \
           '7、该系统主要是用于辅助用户收集一些信息，不能对数据进行精细化过滤.\n' \
           '   需要用户进一步操作。                                  \n' \
           '8、对于系统运行产生的记录文件请查阅当前目录下的CO_DOM文件夹。\n'\
           '9、系统正处于升级阶段，目前收录的网站ttps://so.csdn.net/，数据量\n' \
           '   有限，后期将进行网站收录工作，敬请期待。\n'



# 系统监控信号
app_singlers = {
    'exsit':False,  # 退出
    'menu':False,   # 菜单
    'monitor':False, # 监控
    'config':False, # 配置
    'systemsport':False, # 支持
    'crawl':False,
    'help':False,
}

def getheaders():
    """
    随机请求头
    :return:
    """
    user_agent_list_2 = [
        # Opera
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60",
        "Opera/8.0 (Windows NT 5.1; U; en)",
        "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50",
        # Firefox
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
        "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
        # Safari
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
        # chrome
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
        # 360
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        # 淘宝浏览器
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
        # 猎豹浏览器
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
        # QQ浏览器
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        # sogou浏览器
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)",
        # maxthon浏览器
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36",
        # UC浏览器
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36",
    ]

    # 一部分 PC端的
    user_agent_list_1 = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]
    user_agent_list = user_agent_list_1+user_agent_list_2
    UserAgent = random.choice(user_agent_list)
    headers = {'User-Agent':UserAgent}
    print(headers)
    return headers
# 可以配置随机请求头--->pass
HEADERS= getheaders()


def delm():
    paths = ['log_path','erro_log_path','remenber']
    for i in paths:
        if os.path.isfile(CSDN[i]):
            try:
                os.remove(CSDN[i])
            except Exception as e :
                print(e)



