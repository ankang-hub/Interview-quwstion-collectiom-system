# --coding:GBK --

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr



class Send_MSG:
    """
    邮件发送
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
            msg['From'] = formataddr([self.myId, self.myName])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            msg['To'] = formataddr([self.saveId, self.saveName])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            msg['Subject'] = title  # 邮件的主题，也可以说是标题
            server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
            server.login(self.myId, self.myPasword)  # 括号中对应的是发件人邮箱账号、邮箱授权码
            server.sendmail(self.myId, [self.saveId, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
        except Exception as E:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
            print('Send Message fail Because : {} '.format(E))
        finally:
            print('Send Message Finash ')
