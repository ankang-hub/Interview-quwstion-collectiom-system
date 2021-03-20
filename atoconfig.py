# --coding:GBK --

import os
from config import CSDN



def autconfig(newconf):
    """
    获取用户自定义配置，更新 源文件
    :return: dic
    """
    try:
        if newconf == {}:
            print('未配置')
            return CSDN
        else:
            print('用户配置')
            CSDN['save_path'] = newconf['save_path']
            if os.path.isdir(newconf['save_path']):
                pass
            else:
                os.makedirs(newconf['save_path'])
            CSDN['flag'] = newconf['flag']
            CSDN['key_word'] = newconf['key_word'].replace(',','/').replace('，','/').split('/')
            for i in newconf['fl_title'].replace(',','/').replace('，','/').split('/'):
                CSDN['fl_title'].append(i)
            CSDN['consume'] = newconf['consume'].replace(',','/').replace('，','/').split('/')
            CSDN['email'] = newconf['email']
            return CSDN
    except Exception as e:
        print(e)





