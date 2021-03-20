# --coding:GBK --
import time
import threading
import tkinter as tk
import tkinter.messagebox
from config import *
from PIL import Image,ImageTk
from atoconfig import autconfig
from singlers import stop_thread
from filter import crawl,info
from random_centens import rand_cts,weather


user_conf = {}

def app_welcom(wea):
    """
    系统入口
    :param wea:
    :return:
    """
    app = tk.Tk()
    app.title('A2.0')
    app.geometry('800x650')
    app.resizable(0,0)
    #app.attributes('-alpha', 0.9)
    image2 = Image.open('./bg/bg1.jpg')
    background_image = ImageTk.PhotoImage(image2)
    background_label = tkinter.Label(app, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=0.92)
    tk.Label(app, text="A2.0技术型试题资料采集辅助系统", justify='center',bg='aqua',
             height=3, width=36,fg='black', font=('楷体' ,32,)).place(x=0,y=0)
    tk.Label(app, text="专注于互联网技术试题资料", justify='left',bg='cyan',
             height=2, width=70, font=('楷体', 18,)).place(x=0, y=110)

    tk.Label(app, text=f"{rand_cts()}", justify='left',fg='slateblue',
             height=2, width=36, font=("楷体", 18,)).place(x=0,y=200)

    tk.Label(app, text=f"{wea}", justify='left', fg='slateblue',
             height=2, width=120, font=("楷体", 10,)).place(x=0, y=570)

    tk.Label(app, text='注意：改应用仅为学习研究不得用于商业用途!',font=("黑体", 10), bg='red', justify='left',
             ).place(x=10,y=600)
    tk.Label(app, text='问题请联系: QQ:3173362514@qq.com。',font=("黑体", 10), justify='left').place(x=10,y=625)

    # 时间 显示
    def gettime():
        var1.set('日期:'+time.strftime("%y/%m/%d"))
        var2.set('时间:'+time.strftime("%H:%M:%S"))
        app.after(1000, gettime)
    var1 = tk.StringVar()
    var2 = tk.StringVar()
    tk.Label(app, textvariable=var1, fg='darkred', font=("黑体", 10)).place(x=690,y=600)
    tk.Label(app, textvariable=var2, fg='darkred', font=("黑体", 10)).place(x=690, y=625)


    def qto_manu():
        """
        信号更新，进入菜单
        :return:
        """
        global app_singlers
        app_singlers['menu'] = True

        app.destroy()

    def quit():
        """
        信号更新
        :return:
        """
        global app_singlers
        app_singlers['exsit'] = True
        app.destroy()

    tk.Button(app, text="退出系统", width=15, bg='lime', font=("黑体", 15), height=2, command=quit).place(x=350, y=500)
    tk.Button(app, text="进入系统", width=15, bg='lime', font=("黑体", 15), height=2, command=qto_manu).place(x=350, y=400)
    gettime()
    app.mainloop()





def app_help(wea):
    """
    系统入口
    :param wea:
    :return:
    """
    app = tk.Tk()
    app.title('A2.0')
    app.geometry('800x650')
    app.resizable(0,0)
    #app.attributes('-alpha', 0.9)
    image2 = Image.open('./bg/bg1.jpg')
    background_image = ImageTk.PhotoImage(image2)
    background_label = tkinter.Label(app, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=0.92)
    tk.Label(app, text="帮助文档", justify='center',bg='aqua',
             height=3, width=36,fg='black', font=('楷体' ,32,)).place(x=0,y=0)
    tk.Label(app, text= '\n\n 使用方法：\n\n'+helpinfo, justify='left', fg='black',bg='ivory',
             height=20, width=90,font=("楷体", 13,)).place(x=0, y=135)
    tk.Label(app, text=f"{wea}", justify='left', fg='slateblue',
             height=2, width=120, font=("楷体", 10,)).place(x=0, y=570)

    tk.Label(app, text='注意：改应用仅为学习研究不得用于商业用途!',font=("黑体", 10), bg='red', justify='left',
             ).place(x=10,y=600)
    tk.Label(app, text='问题请联系: QQ:3173362514@qq.com。',font=("黑体", 10), justify='left').place(x=10,y=625)

    # 时间 显示
    def gettime():
        var1.set('日期:'+time.strftime("%y/%m/%d"))
        var2.set('时间:'+time.strftime("%H:%M:%S"))
        app.after(1000, gettime)
    var1 = tk.StringVar()
    var2 = tk.StringVar()
    app.after(1,gettime())
    tk.Label(app, textvariable=var1, fg='darkred', font=("黑体", 10)).place(x=690,y=600)
    tk.Label(app, textvariable=var2, fg='darkred', font=("黑体", 10)).place(x=690, y=625)

    # 返回菜单
    def rback():
        """
        返回菜单，更新参数
        :return:
        """
        global app_singlers
        # 停止前返回信号,，开启菜单信号，关闭面板
        info[5] = 3  # info
        app_singlers['exsit'] = False
        app_singlers['menu'] = True
        app_singlers['monitor'] = False
        app_singlers['config'] = False
        app_singlers['systemsport'] = False
        app_singlers['help'] = False
        # 确认配置弹窗：
        app.destroy()  # 界面关闭

    def quit():
        """
        退出系统，更新参数
        :return:
        """
        global app_singlers
        app_singlers['exsit'] = True
        app_singlers['menu'] = False
        app_singlers['monitor'] = False
        app_singlers['config'] = False
        app_singlers['systemsport'] = False
        app_singlers['help'] = False
        app.destroy()

    tk.Button(app, text="返回菜单", width=15, bg='green', font=("黑体", 14), height=2, command=rback).place(x=150, y=510)
    tk.Button(app, text="退出系统", width=15, bg='green', font=("黑体", 14), height=2, command=quit).place(x=500, y=510)
    app.mainloop()

def manu(wea):
    """
    菜单窗口.
    :param wea:
    :return:
    """
    app = tk.Tk()
    app.title('A2.0')
    app.geometry('800x650')
    app.resizable(0, 0)
    # app.attributes('-alpha', 0.9)
    image2 = Image.open('./bg/bg1.jpg')
    background_image = ImageTk.PhotoImage(image2)
    background_label = tkinter.Label(app, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=0.92)
    tk.Label(app, text="A2.0技术型试题资料采集辅助系统", justify='center', bg='aqua',
             height=3, width=36, fg='black', font=('楷体', 32,)).place(x=0, y=0)
    tk.Label(app, text=f"{rand_cts()}", justify='left', fg='slateblue',
             height=4, width=33, font=("楷体", 20,)).place(x=0, y=135)
    tk.Label(app, text="\n用户须知!\n"+foruser, justify='left', fg='red',
             height=20,width=55,font=("楷体", 12,)).place(x=0,y=249)
    tk.Label(app, text="菜单", justify='right', fg='tomato',
             height=4, width=30, font=("楷体", 22,)).place(x=400, y=135)
    tk.Label(app, text=f"{wea}", justify='left', fg='slateblue',
             height=2, width=120, font=("楷体", 10,)).place(x=0, y=570)
    tk.Label(app, text='注意：改应用仅为学习研究不得用于商业用途!', bg='red',font=("黑体", 10), justify='left',
             ).place(x=10, y=600)
    tk.Label(app, text='问题请联系: QQ:3173362514@qq.com。',font=("黑体", 10), justify='right').place(x=10, y=625)

    # 时间 显示
    def gettime():
        """
        屏幕时间刷新
        :return:
        """
        var1.set('日期:' + time.strftime("%y/%m/%d"))
        var2.set('时间:' + time.strftime("%H:%M:%S"))
        app.after(1000, gettime)

    var1 = tk.StringVar()
    var2 = tk.StringVar()
    tk.Label(app, textvariable=var1, fg='darkred', font=("黑体", 10)).place(x=690, y=600)
    tk.Label(app, textvariable=var2, fg='darkred', font=("黑体", 10)).place(x=690, y=625)

    def sport():
        """
        进入帮助面板，信号更新
        :return:
        """
        global app_singlers
        app_singlers['systemsport'] = True
        app_singlers['monitor'] = False
        app_singlers['menu'] = False
        app_singlers['config'] = False
        app_singlers['exsit'] = False
        app.destroy()

    def quit_go_monitor():
        """
        进入监控面板，更新信号
        :return:
        """
        su = tkinter.messagebox.askokcancel('提醒','进入控制面板前请先配置收集参数\n'
                                                 '您确认已经配置好了吗？')
        if su:
            global app_singlers
            app_singlers['monitor'] = True
            app_singlers['menu'] = False
            app_singlers['config'] = False
            app_singlers['exsit'] = False
            app.destroy()
        else:
            pass

    def config():
        """
        菜单进入配置，更新信号
        :return:
        """
        global app_singlers
        app_singlers['exsit'] = False
        app_singlers['menu'] = False
        app_singlers['monitor'] = False
        app_singlers['config'] = True
        app.destroy()

    def help():
        """
        更新信号，进入帮助
        :return:
        """
        global app_singlers
        app_singlers['exsit'] = False
        app_singlers['menu'] = False
        app_singlers['monitor'] = False
        app_singlers['config'] = False
        app_singlers['help'] = True
        app.destroy()

    def quit():
        """
        系统退出信号，信号更新
        :return:
        """
        global app_singlers
        app_singlers['exsit'] = True
        app_singlers['menu'] = False
        app_singlers['monitor'] = False
        app_singlers['config'] = False
        app.destroy()
    def peoxies():
        tkinter.messagebox.showinfo('提示','代理维护中，还未开放')


    gettime()
    # 免费代理
    tk.Button(app, text="收集配置", width=15, bg='deepskyblue', font=("黑体", 14), height=2, command=config).place(x=550, y=364)
    tk.Button(app, text="代理设置", width=15, bg='deepskyblue', font=("黑体", 14), height=2, command=peoxies).place(x=550, y=312)
    tk.Button(app, text="监控面板", width=15, bg='deepskyblue', font=("黑体", 14), height=2, command=quit_go_monitor).place(x=550, y=416)
    tk.Button(app, text="系统支持", width=15, bg='deepskyblue', font=("黑体", 14), height=2, command=sport).place(x=550,
                                                                                                             y=260)
    tk.Button(app, text="使用帮助", width=36, bg='green', font=("黑体", 14), height=2, command=help).place(x=445, y=468)
    tk.Button(app, text="退出系统", justify='center', width=36, bg='green', font=("黑体", 14), height=2, command=quit).place(x=445, y=520)
    app.mainloop()

def configer(wea):
    """
    修改控制面板
    :param wea:
    :return:
    """
    app = tk.Tk()
    app.title('A2.0')
    app.geometry('800x650')
    app.resizable(0, 0)
    image2 = Image.open('./bg/bg1.jpg')
    background_image = ImageTk.PhotoImage(image2)
    background_label = tkinter.Label(app, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=0.92)
    tk.Label(app, text="A2.0采集系统配置", justify='center',bg='yellow',
             height=1, width=16, font=('楷体', 32,)).place(x=240, y=30)
    tk.Label(app, text='保存文件夹 :', justify='left',bg='aqua', height=1, width=12, font=("楷体", 16,)).place(x=30, y=165)
    tk.Label(app, text='限定几年内:',justify='left',bg='aqua', height=1, width=12, font=("楷体", 16,)).place(x=30,y=210)
    tk.Label(app, text='搜索关键字:', justify='left',bg='aqua',height=1, width=12, font=("楷体", 16,)).place(x=30,y=260)
    tk.Label(app, text='过滤关键字:',justify='left', bg='aqua',height=1, width=12, font=("楷体", 16,)).place(x=30,y=310)
    tk.Label(app, text='需包含字符: ',justify='left',bg='aqua', height=1, width=12, font=("楷体", 16,)).place(x=30,y=360)
    tk.Label(app, text='QQ email: ', justify='left', bg='aqua', height=1, width=12, font=("楷体", 16,)).place(x=30, y=410)
    tk.Label(app, text='提示：如果不希望邮件通知，可以不用输入: ', justify='left', bg='orange', height=1, width=40, font=("楷体", 16,)).place(x=30, y=500)

    # 范例
    tk.Label(app, text='D:/example1/example2 ',bg='royalblue', justify='left', height=1, width=30, font=("楷体", 16,)).place(x=440, y=165)
    tk.Label(app, text='3', justify='left', bg='royalblue',height=1, width=30, font=("楷体", 16,)).place(x=440, y=210)
    tk.Label(app, text='深度学习，面试，机器学习', bg='royalblue',justify='left', height=1, width=30, font=("楷体", 16,)).place(x=440, y=260)
    tk.Label(app, text='培训，java，大全', justify='left',bg='royalblue', height=1, width=30, font=("楷体", 16)).place(x=440, y=310)
    tk.Label(app, text='深度学习，面试,总结', justify='left',bg='royalblue', height=1, width=30, font=("楷体", 16,)).place(x=440, y=360)
    tk.Label(app, text='111111,111111@qq.com', justify='left', bg='royalblue', height=1, width=30, font=("楷体", 16,)).place(x=440,
                                                                                                                 y=410)


    text0 = tk.Text(app,bg='tan', width=20, height=1, font=("楷体", 15,))
    text0.place(x=200, y=168)
    text0.delete(0.0, tk.END)
    text0.insert(tk.INSERT, '')
    text0.update()

    text1 = tk.Text(app,bg='tan', width=20, height=1,font=("楷体", 15,))
    text1.place(x=200,y=213)
    text1.delete(0.0, tk.END)
    text1.insert(tk.INSERT, 3)
    text1.update()

    text2 = tk.Text(app, bg='tan',width=20, height=1, font=("楷体", 15,))
    text2.place(x=200, y=264)
    text2.delete(0.0, tk.END)
    text2.insert(tk.INSERT, '')
    text2.update()

    text3 = tk.Text(app,bg='tan', width=20, height=1, font=("楷体", 15,))
    text3.place(x=200, y=313)
    text3.delete(0.0, tk.END)
    text3.insert(tk.INSERT,'')
    text3.update()

    text4 = tk.Text(app, bg='tan',width=20, height=1, font=("楷体", 15,))
    text4.place(x=200, y=363)
    text4.delete(0.0, tk.END)
    text4.insert(tk.INSERT, '')
    text4.update()

    text5 = tk.Text(app, bg='tan', width=20, height=1, font=("楷体", 15,))
    text5.place(x=200, y=413)
    text5.delete(0.0, tk.END)
    text5.insert(tk.INSERT, 'None')
    text5.update()
    tkinter.messagebox.showwarning('注意', "过滤信息与关键字有多个的以中文','分割、"
                                        "建议尽可能多一些过滤字符因为它会直接影响结果准确率!")
    def get_conf():
        """
        获取用户的配置
        :return: dic---{}
        """
        global user_conf
        save_path = text0.get(0.0,tk.END).strip()
        flag = text1.get(0.0,tk.END).strip()
        key_word = text2.get(0.0,tk.END).strip()
        fl_title = text3.get(0.0,tk.END).strip()
        consum = text4.get(0.0,tk.END).strip()
        qqemail = text5.get(0.0,tk.END).strip()
        consumconfig = {}
        consumconfig['save_path'] = save_path
        consumconfig['flag'] = flag
        consumconfig['key_word'] =  key_word
        consumconfig['fl_title'] = fl_title
        consumconfig['consume'] = consum
        consumconfig['email'] = qqemail
        if os.path.isabs(save_path) is False:
            tkinter.messagebox.showerror('错误','请确认路径是否正确')
        else:
            ask = tkinter.messagebox.askokcancel('请确认',str(consumconfig).replace(',','\n')+'\n确认提交吗？')
            if ask:
                    tkinter.messagebox.showinfo('成功','配置完成。')
                    tk.Button(app, text="提交", width=15, bg='green', font=("黑体", 14), height=2, command=get_conf).place(
                        x=25, y=530)
        user_conf = consumconfig


    def gettime2():
        """
        时间刷新
        :return:
        """
        var3.set('日期:' + time.strftime("%y/%m/%d"))
        var4.set('时间:' + time.strftime("%H:%M:%S"))
        app.after(1000, gettime2)

    def rback():
        """
        返回菜单，更新参数
        :return:
        """
        global app_singlers
        # 停止前返回信号,，开启菜单信号，关闭面板
        info[5] = 3   # info
        app_singlers['exsit'] = False
        app_singlers['menu'] = True
        app_singlers['monitor'] = False
        app_singlers['config'] = False
        # 确认配置弹窗：
        app.destroy() # 界面关闭

    # 退出系统
    def quit():
        global app_singlers
        app_singlers['exsit'] = True
        app_singlers['menu'] = False
        app_singlers['monitor'] = False
        app_singlers['config'] = False
        app.destroy()

    var3 = tk.StringVar()
    var4 = tk.StringVar()
    gettime2()
    tk.Button(app, text="返回菜单", width=15, bg='green', font=("黑体", 14), height=2, command=rback).place(x=340, y=530)
    tk.Button(app, text="退出系统", width=15, bg='green', font=("黑体", 14), height=2, command=quit).place(x=620, y=530)
    tk.Button(app, text="提交", width=15, bg='red', font=("黑体", 14), height=2, command=get_conf).place(x=25, y=530)
    tk.Label(app, text='备注：改应用仅为学习研究不得用于商业用途!', bg='red',font=("黑体", 10), justify='left',
             ).place(x=10,y=600)
    tk.Label(app, text='问题请联系: QQ:3173362514@qq.com。', font=("黑体", 10),justify='right').place(x=10,y=625)
    tk.Label(app, textvariable=var3, fg='black', font=("黑体", 10)).place(x=690, y=600)
    tk.Label(app, textvariable=var4, fg='black', font=("黑体", 10)).place(x=690, y=625)
    gettime2()
    app.mainloop()

def systemsport(wea):
    """
    系统支持面吧
    :param wea:
    :return:
    """
    app = tk.Tk()
    app.title('A.1.0')
    app.geometry('800x650')
    app.resizable(0, 0)
    image2 = Image.open('./bg/bg1.jpg')
    background_image = ImageTk.PhotoImage(image2)
    tkinter.Label(app, image=background_image).place(x=0, y=0, relwidth=1, relheight=0.92)
    tk.Label(app, text="系统支持", justify='center', bg='aqua',
             height=3, width=36, fg='black', font=('楷体', 32,)).place(x=0, y=0)
    tk.Label(app, text='注意：改应用仅为学习研究不得用于商业用途!', bg='red', font=("黑体", 10), justify='left',
             ).place(x=10, y=600)
    tk.Label(app, text='问题请联系: QQ:3173362514@qq.com。', font=("黑体", 10), justify='right').place(x=10, y=625)
    tk.Label(app, text=f"{wea}", justify='left', fg='slateblue',
             height=2, width=120, font=("楷体", 10,)).place(x=0, y=570)
    tk.Label(app, text='已收录网站如下:\n',height=4,width=30,bg='spring green', font=("黑体", 20), justify='left',
            ).place(x=400, y=206)
    tk.Label(app, height=5, bg='spring green', width=35, font=("黑体", 18), justify='left',
             ).place(x=400, y=300)
    tk.Label(app, text='https://www.csdn.net/', height=5, bg='spring green', width=35, font=("黑体", 18), justify='left',
             ).place(x=400, y=340)

    tk.Label(app, text='1、技术类面试题资料辅助采集。', font=("黑体", 16), justify='left',
            ).place(x=10, y=206)
    tk.Label(app, text='2、技术类学习博文辅助采集。', font=("黑体", 16), justify='left',
             ).place(x=10, y=246)
    tk.Label(app, text='3、技术类问题解决方案辅助收集。', font=("黑体", 16), justify='left',
             ).place(x=10, y=286)
    tk.Label(app, text='5，实时天气', font=("黑体", 16), justify='left',
             ).place(x=10, y=366)
    tk.Label(app, text='6，实时天气', font=("黑体", 16), justify='left',
             ).place(x=10, y=366)
    tk.Label(app, text='4、Email 邮件通知', font=("黑体", 16), justify='left',
             ).place(x=10, y=326)
    # tk.Label(app, text='系统设计的初心是辅助老师收集深度学习类试题其他类型收集效果不能保证！', font=("黑体", 17), justify='left',
    #          ).place(x=0, y=137)

    def gettime():
        """
        窗口时间更新
        :return:
        """
        var1.set('日期:' + time.strftime("%y/%m/%d"))
        var2.set('时间:' + time.strftime("%H:%M:%S"))
        app.after(1000, gettime)

    var1 = tk.StringVar()
    var2 = tk.StringVar()
    tk.Label(app, textvariable=var1, fg='darkred', font=("黑体", 10)).place(x=690, y=600)
    tk.Label(app, textvariable=var2, fg='darkred', font=("黑体", 10)).place(x=690, y=625)
    gettime()

    # 返回菜单
    def rback():
        """
        返回菜单，更新参数
        :return:
        """
        global info
        global app_singlers
        # 停止前返回信号,，开启菜单信号，关闭面板
        info[5] = 3  # info
        app_singlers['exsit'] = False
        app_singlers['menu'] = True
        app_singlers['monitor'] = False
        app_singlers['config'] = False
        app_singlers['systemsport'] = False
        # 确认配置弹窗：
        app.destroy()  # 界面关闭

    def quit():
        """
        退出系统，更新参数
        :return:
        """
        global app_singlers
        app_singlers['exsit'] = True
        app_singlers['menu'] = False
        app_singlers['monitor'] = False
        app_singlers['config'] = False
        app_singlers['systemsport'] = False
        app.destroy()

    tk.Button(app, text="返回菜单", width=15, bg='green', font=("黑体", 14), height=2, command=rback).place(x=150, y=510)
    tk.Button(app, text="退出系统", width=15, bg='green', font=("黑体", 14), height=2, command=quit).place(x=500, y=510)
    app.mainloop()




def monitor(wea,newconf):
    """
    控制面板
    :param wea: 天气信息
    :return:
    """
    app = tk.Tk()
    app.title('A2.0')
    app.geometry('800x650')
    app.resizable(0, 0)
    image2 = Image.open('./bg/bg1.jpg')
    background_image = ImageTk.PhotoImage(image2)
    background_label = tkinter.Label(app, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=0.92)
    tk.Label(app, text="采集辅助系统监控面板", justify='center', bg='cyan',
             height=3, width=36, fg='black', font=('楷体', 32,)).place(x=0, y=0)
    # tk.Label(app, text='系统运行趋势', bg='yellow', height=1, width=15, font=("楷体", 16,)).place(x=500, y=160)
    tk.Label(app, text='状态', bg='red', height=1, width=8, font=("楷体", 16,)).place(x=20, y=160)
    tk.Label(app, text='总数量',bg='yellow', height=1, width=8, font=("楷体", 16,)).place(x=20, y=210)
    tk.Label(app, text='过滤量',bg='seagreen', height=1, width=8, font=("楷体", 16,)).place(x=20, y=260)
    tk.Label(app, text='失败量',bg='tomato', height=1, width=8, font=("楷体", 16,)).place(x=20, y=310)
    tk.Label(app, text='成功量', bg='lime',height=1, width=8, font=("楷体", 16,)).place(x=20, y=360)
    tk.Label(app, text='失败率',bg='salmon', height=1, width=8, font=("楷体", 16,)).place(x=20, y=410)
    tk.Label(app, text='过滤率', bg='gold',height=1, width=8, font=("楷体", 16,)).place(x=20, y=460)
    tk.Label(app, text='文件(M)',bg='lime', height=1, width=8, font=("楷体", 16,)).place(x=20, y=510)
    tk.Label(app, text=f"{wea}", justify='left', fg='slateblue',
             height=2, width=120, font=("楷体", 10,)).place(x=0, y=570)
    ucon = ''
    for i, j in newconf.items():
        j = str(j).replace('[','').replace(']','').strip()
        jsr = ''
        con = 0
        for a in j:
            con += 1
            if con%40 is 0:
                jsr += a+'\n    '
            else:
                jsr += a
        j = jsr + '\n'
        ucon += '%s:%s\n' % (str(i), j)
    tkinter.Label(app, text='\n\n\n您的部分相关配置如下:\n\n'+(ucon),justify='left',height=25, width=85,font=("黑体", 10)).place(x=220, y=160)
    tk.Label(app, text='备注：改应用仅为学习研究不得用于商业用途!', bg='red', font=("黑体", 10), justify='left').place(x=10, y=600)
    tk.Label(app, text='问题请联系: QQ:3173362514@qq.com。', font=("黑体", 10), justify='right').place(x=10, y=625)
    text1 = tk.Text(app, width=8, height=2)
    text1.place(x=150, y=210)

    text2 = tk.Text(app, width=8, height=2)
    text2.place(x=150,y=260)

    text3 = tk.Text(app, width=8, height=2)
    text3.place(x=150,y=310)
    text4 = tk.Text(app, width=8, height=2)
    text4.place(x=150,y=360)

    text5 = tk.Text(app, width=8, height=2)
    text5.place(x=150,y=410)

    text6 = tk.Text(app, width=8, height=2)
    text6.place(x=150,y=460)

    text7 = tk.Text(app, width=8, height=2)
    text7.place(x=150,y=510)

    text8 = tk.Text(app, width=8, height=2)
    text8.place(x=150,y=160)

    def refreshText():
        """
        窗口更新
        :return:
        """
        text1.delete(0.0, tk.END)
        text1.insert(tk.INSERT,info[3])
        text1.update()
        text2.delete(0.0, tk.END)
        text2.insert(tk.INSERT, info[0])
        text2.update()
        text3.delete(0.0, tk.END)
        text3.insert(tk.INSERT, info[2])
        text3.update()
        text4.delete(0.0, tk.END)
        text4.insert(tk.INSERT, info[1])
        text4.update()
        text8.delete(0.0, tk.END)
        text8.insert(tk.INSERT, Statatus[info[4]])
        text8.update()
        try:
            s = os.path.getsize(CSDN['save_path'].replace(r'\\','/')+'/information.doc') /(1024*1024)
            text7.delete(0.0, tk.END)
            text7.insert(tk.INSERT, '%0.2f' % s)
            text7.update()
        except Exception as e:
            text7.delete(0.0, tk.END)
            text7.insert(tk.INSERT, '%0.3f' % 0)
            text7.update()
        if info[3] == 0:
            text5.delete(0.0, tk.END)
            text5.insert(tk.INSERT, 0)
            text5.update()

            text6.delete(0.0, tk.END)
            text6.insert(tk.INSERT, 0)
            text6.update()
        else:
            f = '%0.3f'%(info[2]/info[3])
            s = '%0.3f'%(info[0]/info[3])
            text5.delete(0.0, tk.END)
            text5.insert(tk.INSERT, f)
            text5.update()

            text6.delete(0.0, tk.END)
            text6.insert(tk.INSERT, s)
            text6.update()
        app.after(3000, refreshText)

    global t
    t = threading.Thread(target=crawl, args=(newconf,))
    def star():
        """
        开起爬虫命令，更新信号参数
        :return:
        """
        global info
        global app_singlers
        app_singlers['crawl'] = True # 爬虫开启信号
        info[5] = 2  # -----》开启  # ------》状态
        global t
        print(info)
        if t.isAlive() is True:
            print('started 1')
        else:
            try:
                t.start()
                print('start 2')
            except:
                t = threading.Thread(target=crawl,args=(newconf,))
                t.start()
                print('start 3' )

    def stop():
        """
        停止爬虫，更新信号参数
        :return:
        """
        global info
        global app_singlers
        global t
        info[5] = 1 # -----> 停爬虫信号
        info[4] = 4 # 状态
        app_singlers['crawl'] = False # -爬虫暂停信号
        if t.isAlive() is True:
            stop_thread(t)
            print('stop 1')
        else:
            try:
                stop_thread(t)
                print('stoped 2')
            except:
                print('stoped 3')


    def path_sav():
        """
        提示用户数据存储路径
        :return:
        """
        p = CSDN['save_path']
        tkinter.messagebox.showinfo('提示',p)

    def quit():
        """
        退出系统，更新信号
        :return:
        """
        global info
        sur = tkinter.messagebox.askokcancel('警告','确认退出吗，如果退出任务将不能继续进行！')
        if sur is True:
            info[5] =3 # 状态 退出系统
            global app_singlers
            app_singlers['exsit'] = True
            app_singlers['menu'] = False
            app_singlers['monitor'] = False
            app_singlers['crawl'] = False # 退出信号初始化
            try:
                stop_thread(t)
            except:
                pass
            finally:
                app.destroy()
        else:
            pass

        # 时间 显示
    def gettime2():
        """
        屏幕时间更新
        :return:
        """
        var3.set('日期:' + time.strftime("%y/%m/%d"))
        var4.set('时间:' + time.strftime("%H:%M:%S"))
        app.after(1000, gettime2)
    var3 = tk.StringVar()
    var4 = tk.StringVar()
    gettime2()
    tk.Label(app, textvariable=var3, fg='black', font=("黑体", 10)).place(x=700, y=600)
    tk.Label(app, textvariable=var4, fg='black', font=("黑体", 10)).place(x=700, y=625)

    # 返回菜单
    def rback():
        """
        返回菜单
        :return:
        """
        global info
        global app_singlers
        # 停止前返回信号,，开启菜单信号，关闭面板
        info[5] = 3   # info
        sur = tkinter.messagebox.askokcancel('警告', '确认返回吗，如果返回进行的任务将不能继续进行！')
        if sur:
            app_singlers['exsit'] = False
            app_singlers['menu'] = True
            app_singlers['monitor'] = False
            app_singlers['crawl'] = False
            # 确认配置弹窗：
        try:
            stop_thread(t)
            app.destroy() # 界面关闭
        except:
            app.destroy()
            pass
        finally:
            info = [0, 0, 0, 0, 4, 2]

    tk.Button(app, text="开始",bg='lime', width=10, command=star).place(x=300,y=510)
    tk.Button(app,text='终止',bg='lime', width=10, command=stop).place(x=400,y=510)
    tk.Button(app, text="退出系统",bg='red', width=10, command=quit).place(x=700,y=510)
    tk.Button(app,text="文件路径", bg='lime',width=10, command=path_sav).place(x=600,y=510)
    tk.Button(app,text="返回菜单",bg='lime',width=10,command=rback).place(x=500,y=510)
    app.after(1, refreshText)
    app.mainloop()


def monitor_center(wea,conf):
    """
    控制面板逻辑函数
    :return:
    """
    global app_singlers
    wea = weather()
    try:
        monitor(wea,conf)
    except Exception as e:
        print('ERRO：',e,'welcom.py 746')
def rulinning():
    """
    界面运行函数，捕捉信号打开相应窗口
    :return:
    """
    inite()
    print('系统欢迎界面')
    wea = weather()
    app_welcom(wea)
    i = 0
    while True:
        i = i+1
        print('界面信号变化：',app_singlers)
        if app_singlers['menu'] is True:
            print('进入菜单页面')
            manu(wea)
        if app_singlers['config'] is True:
            print('界面信号变化：', app_singlers)
            print('进入配置！')
            configer(wea)
        if app_singlers['exsit'] is True:
            print('界面信号变化：', app_singlers)
            print('退出系统！')
            break
        if app_singlers['monitor'] is True:
            print(user_conf)
            newconfig = autconfig(user_conf)
            time.sleep(0.01)
            print(newconfig,'''----------''') # --------------修改的配置
            print('界面信号变化：', app_singlers)
            print('进入监控面板')
            monitor_center(wea,newconfig)

        if app_singlers['help'] is True:
            print('界面信号变化：', app_singlers)
            print('进入使用帮助')
            app_help(wea)

        if app_singlers['systemsport'] is True:
            print('界面信号变化：', app_singlers)
            print('进入支持')
            systemsport(wea)
        if i >100000:
            raise SystemExit from Statatus
        else:
            print('继续捕捉界面信号')
            continue




if __name__ == '__main__':
     rulinning()
