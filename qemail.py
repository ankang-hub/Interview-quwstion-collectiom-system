# --coding:GBK --

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr



class Send_MSG:
    """
    �ʼ�����
    """
    def __init__(self,qqnum,qqemail):
        self.myName = '3173362514'
        self.myId = "3173362514@qq.com"
        self.myPasword = "oabffbvpoqawdgjg"
        self.saveName = qqnum
        self.saveId = qqemail

    def send_messige(self, title=None, message=None):
        try:
            msg = MIMEText(message, 'plain', 'utf-8')
            msg['From'] = formataddr([self.myId, self.myName])  # ������Ķ�Ӧ�����������ǳơ������������˺�
            msg['To'] = formataddr([self.saveId, self.saveName])  # ������Ķ�Ӧ�ռ��������ǳơ��ռ��������˺�
            msg['Subject'] = title  # �ʼ������⣬Ҳ����˵�Ǳ���
            server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # �����������е�SMTP���������˿���25
            server.login(self.myId, self.myPasword)  # �����ж�Ӧ���Ƿ����������˺š�������Ȩ��
            server.sendmail(self.myId, [self.saveId, ], msg.as_string())  # �����ж�Ӧ���Ƿ����������˺š��ռ��������˺š������ʼ�
            server.quit()  # �ر�����
        except Exception as E:  # ��� try �е����û��ִ�У����ִ������� ret=False
            print('Send Message fail Because : {} '.format(E))
        finally:
            print('Send Message Finash ')
