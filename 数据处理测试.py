# --coding:GBK --
from bs4 import BeautifulSoup
import math
import lxml

data = open('./Bk_DOM/测试.html','r',encoding='utf-8').read()
soup = BeautifulSoup(data,'lxml')
info = soup.find_next_sibling(name='div',attrs={'id':'content_views'})

with open('./Bk_DOM/文本.doc','a+',encoding='UTF-8') as f:
    for i in soup.findAll(name='div',attrs={'id':'content_views'}):
        f.write(i.text.strip()+'\n')
