# --coding:GBK --

import time
import json
import re
import lxml
import logging
import jsonpath
import requests
import queue
from config import *
from urllib.parse import quote
from de_duplication import Dupler
from bs4 import BeautifulSoup




# 初始化确认
if reback is True:
    delm()


# filn =0
# cn = 0
# fln = 0
# al =0
# status = 4
# flag = 1
q = queue.Queue()
# 过滤、成功、失败、总量，状态，失败率，过滤率
# Statatus =['启动中','正在运行','发生错误','运行结束','停止']
info = [0,0,0,0,4,1]
from qemail import Send_MSG

# 日志
logger = logging.getLogger('INFO_')
logger1 = logging.getLogger('ERRO_')
logger.setLevel(level=logging.INFO)
logger1.setLevel(level=logging.ERROR)
handler = logging.FileHandler(CSDN['log_path'])
handler1 = logging.FileHandler(CSDN['erro_log_path'])
handler.setLevel(logging.INFO)
handler1.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s  - %(message)s')
formatter1=logging.Formatter('%(asctime)s - %(message)s')
handler.setFormatter(formatter)
handler1.setFormatter(formatter1)
logger.addHandler(handler)
logger1.addHandler(handler1)


class Filter(Dupler):
    def __init__(self,config,data):
        global info
        global q
        super(Filter, self).__init__()
        self.confi = config
        self.data = data
        self.info = info
        self.q = q
        # print('*************************'*3)
        # print(config)
        # print(self.confi['consume'])
        # print(self.confi['fl_title'])
        # print(self.confi['fl_url'])
        # print('*************************' * 3)

    def consum(self):
        f = 0
        csm = self.confi['consume']
        title = self.data[0]
        if csm is not []:
            for i in csm:
                if re.search(i, title) is not None:
                    f += 1
                    continue
                else:
                    continue
        if f >=1:
            return 0 # success
        else:
            self.info[0] += 1
            return 1 # 过滤

    def title_filt(self):
        f = 0
        fli = self.confi['fl_title']
        title = self.data[0]
        if fli is not []:
            for i in fli:
                if re.search(i, title) is not None:
                    f = 1
                    return f
                else:
                    f = 0
                    continue
            return f
        else:
            return f

    def url_filter(self):
        f = 0
        fli = self.confi['fl_url']
        title = self.data[1]
        if fli is not []:
            for i in fli:
                if re.search(i, title) is not None:
                    f=1
                    return f
                else:
                    f=0
                    continue
        return f

    def time_filter(self):
        f = 0
        fli = int(self.confi['flag'])
        time_ = int(self.data[2].split('-')[0])
        if int(time.gmtime()[0])-time_ >= fli:
            f=1 # faill
            return f
        else:
            return f

    def run(self):
        if self.consum() == 0:
            f1 = self.title_filt()
            f2 = self.url_filter()
            f3 =self.time_filter()
            time.sleep(0.02)
            if {f1,f2,f3} != {0,1} | {0}:
                self.info[0] +=1
            else:
                finger = self.reques_see(self.data[1])
                if finger == 0:
                    self.q.put(self.data[1])
                if finger== -1:
                    info[0] +=1
            print()


def get_all_url(keword):
    global info
    for k in keword:
        logger.info(f'开始收集相关链接------->{k}')
        keword = quote(k)
        first_url = ['https://so.csdn.net/api/v2/search?q=“{}”&t=all&p={}&s=0&tm=0&lv=-1&ft=0&l=&u=&platform=pc',
                     'https://so.csdn.net/api/v2/search?q={}&t=specialcolumn&p={}&s=0&tm=0&lv=-1&ft=0&l=&u=&platform=pc']
        for first_url in first_url:
            for t in range(1,MPage):
                try:
                    url = first_url.format(keword,t)
                    respon = requests.get(url=url,headers=HEADERS,timeout=slpt)
                    respon.encoding = respon.apparent_encoding
                    data = json.loads(respon.text)
                    title = jsonpath.jsonpath(data,'$..title')
                    url = jsonpath.jsonpath(data,'$..url_location')
                    create_time_str = jsonpath.jsonpath(data,'$..create_time_str')
                    for i in range(len(url)):
                        info[3] +=1
                        yield [title[i],url[i],create_time_str[i]]
                    time.sleep(slpt)
                    if t == 20:
                        break
                    else:
                        continue
                except Exception as e:
                    logger1.error(f'文章下载出错:{e}')
                    pass

def download1(url):
    global info
    try:
        news = requests.get(url=url,headers=HEADERS,timeout=3)
        news.encoding = news.apparent_encoding
        soup = BeautifulSoup(news.text, 'lxml')
        with open(CSDN['save_path']+'/information.doc', 'a+', encoding='UTF-8') as f:
            for i in soup.findAll(name='div', attrs={'id': 'content_views'}):
                f.write(i.text.strip() + '\n')
        info[1] += 1
        info[4] = 1
    except Exception as e:
        logger.info(f'{Statatus[2]}......:{e}')
        logger1.error(f'文章下载出错:{e}')
        info[2] +=1
        info[4] = 2
    finally:
        time.sleep(0.5)
        return 0

def crawl(conf):
    global singl
    global info
    if conf['email'] is not 'None':
        qq = str(conf['email'][0])
        em = conf['email'][1]
        print(qq,em)
        message = Send_MSG(qqnum=qq,qqemail=em)
        info[4] = 1
        logger.info('开始采集 相关链接......')
        print('start---------------crawl')
        data = get_all_url(conf['key_word'])
        logger.info('相关链接采集成功，开始进行过滤与下载操作......')
        message.send_messige('通知',f'{time.asctime(),qq}你好:{conf} 正在进行' )
        for data in data:
            print(data[0])
            flter = Filter(config=conf,data=data)
            flter.run() #  ---->q
            info[4] = 1
        while True:
            if q.empty() is False:
                time.sleep(1)
                download1(q.get())
                print(info)
            else:
                print('****')
                print(info)
                break
        logger.info(f"\n文章采集成功，文件保存在:{CSDN['save_path']}+'information.doc'")
        message.send_messige(f"通知:\n文章采集成功，文件保存在:\n{CSDN['save_path']}/information.doc")
        info[4] = 3
        info[5] = 1
    else:
        info[4] = 1
        logger.info('开始采集 相关链接......')
        print('start---------------crawl')
        data = get_all_url(conf['key_word'])
        logger.info('相关链接采集成功，开始进行过滤与下载操作......')
        for data in data:
            flter = Filter(config=conf, data=data)
            flter.run()  # ---->q
            info[4] = 1
        while True:
            if q.empty() is False:
                time.sleep(1)
                download1(q.get())
                print(info)
            else:
                print('****')
                print(info)
                break
        logger.info(f"\n文章采集成功，文件保存在:{CSDN['save_path']}".replace(r'./', '\\') + '......\n')
        info[4] = 3
        info[5] = 1
