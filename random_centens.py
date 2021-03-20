# --coding:utf-8 --

import os
import re
import random
from lxml.html import etree
import requests
from config import HEADERS
from bs4 import BeautifulSoup



def rand_cts():
    """
    随机一句
    :return:
    """
    with open('./bg/centens.txt', 'r', encoding='gbk')as f:
        cs = f.read().strip().split('\n')
        li = list()
        for i in cs:
            li.append(i.strip())
        return random.choice(li)

rand_cts()


def weather():
    """
    界面天气
    :return:
    """
    url = 'https://tianqi.so.com/weather/101270101'
    try:
        news = requests.get(url=url, headers=HEADERS, timeout=1)
        news.encoding = news.apparent_encoding
        soup = BeautifulSoup(news.text, 'lxml')
        weather = re.search('当前天气信息天气：(.*)空气质量',soup.text).group(1).replace('℃','℃ ')
        city = soup.find(name='strong',attrs={'class':'change-title'}).string
        if weather and city is not None:
            weainfo = '今日天气:%s %s '%(city,weather)
            return weainfo
        else:
            return '今日天气: 没有获取到信息'
    except:
        return '今日天气: 没有获取到信息'
