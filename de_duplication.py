# --coding:GBK --
import os
import re
import hashlib
from config import CSDN

class Dupler:
    """
    过滤策略
    """
    def __init__(self):
        self.pth = CSDN['remenber']
        if os.path.isfile(self.pth):
            if os.path.getsize(self.pth) != 0:
                pass
            else:
                with open(self.pth,'a+',encoding='gbk')as f:
                    f.write('======'*10+'\n')
        else:
            with open(self.pth,'a+')as f:
                f.write('======'*10+'\n')

    def hash_md5(self,str_):
        """
        md5 数据压缩
        :param str_:
        :return:
        """
        md5 = hashlib.md5()
        md5.update(str_.encode('UTF-8'))
        ret = md5.hexdigest()
        return ret

    def finger_save(self,finger):
        """
        指纹保存
        :param finger:
        :return:
        """
        with open(self.pth, 'a+', encoding='gbk')as f:
            f.write(finger + '\n')

    def reques_see(self,str_):
        """
        指纹校验
        :param str_:
        :return:
        """
        finger = open(self.pth,'r').read()
        finger_ = self.hash_md5(str_)
        if re.search(re.compile(finger_),finger) is not None:
            return -1 # faill
        else:
            self.finger_save(finger_)
            return 0 # success

# 测试
if __name__ == '__main__':
    finger = open(CSDN['remenber'], 'r').read()
    if re.search(re.compile('7dd6e59ccc9f8aad6483be098d2ef1be'), finger) is not None:
        print('ok')
    else:
        print('no')
