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
    ϵͳ���
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
    tk.Label(app, text="A2.0�������������ϲɼ�����ϵͳ", justify='center',bg='aqua',
             height=3, width=36,fg='black', font=('����' ,32,)).place(x=0,y=0)
    tk.Label(app, text="רע�ڻ�����������������", justify='left',bg='cyan',
             height=2, width=70, font=('����', 18,)).place(x=0, y=110)

    tk.Label(app, text=f"{rand_cts()}", justify='left',fg='slateblue',
             height=2, width=36, font=("����", 18,)).place(x=0,y=200)

    tk.Label(app, text=f"{wea}", justify='left', fg='slateblue',
             height=2, width=120, font=("����", 10,)).place(x=0, y=570)

    tk.Label(app, text='ע�⣺��Ӧ�ý�Ϊѧϰ�о�����������ҵ��;!',font=("����", 10), bg='red', justify='left',
             ).place(x=10,y=600)
    tk.Label(app, text='��������ϵ: QQ:3173362514@qq.com��',font=("����", 10), justify='left').place(x=10,y=625)

    # ʱ�� ��ʾ
    def gettime():
        var1.set('����:'+time.strftime("%y/%m/%d"))
        var2.set('ʱ��:'+time.strftime("%H:%M:%S"))
        app.after(1000, gettime)
    var1 = tk.StringVar()
    var2 = tk.StringVar()
    tk.Label(app, textvariable=var1, fg='darkred', font=("����", 10)).place(x=690,y=600)
    tk.Label(app, textvariable=var2, fg='darkred', font=("����", 10)).place(x=690, y=625)


    def qto_manu():
        """
        �źŸ��£�����˵�
        :return:
        """
        global app_singlers
        app_singlers['menu'] = True

        app.destroy()

    def quit():
        """
        �źŸ���
        :return:
        """
        global app_singlers
        app_singlers['exsit'] = True
        app.destroy()

    tk.Button(app, text="�˳�ϵͳ", width=15, bg='lime', font=("����", 15), height=2, command=quit).place(x=350, y=500)
    tk.Button(app, text="����ϵͳ", width=15, bg='lime', font=("����", 15), height=2, command=qto_manu).place(x=350, y=400)
    gettime()
    app.mainloop()





def app_help(wea):
    """
    ϵͳ���
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
    tk.Label(app, text="�����ĵ�", justify='center',bg='aqua',
             height=3, width=36,fg='black', font=('����' ,32,)).place(x=0,y=0)
    tk.Label(app, text= '\n\n ʹ�÷�����\n\n'+helpinfo, justify='left', fg='black',bg='ivory',
             height=20, width=90,font=("����", 13,)).place(x=0, y=135)
    tk.Label(app, text=f"{wea}", justify='left', fg='slateblue',
             height=2, width=120, font=("����", 10,)).place(x=0, y=570)

    tk.Label(app, text='ע�⣺��Ӧ�ý�Ϊѧϰ�о�����������ҵ��;!',font=("����", 10), bg='red', justify='left',
             ).place(x=10,y=600)
    tk.Label(app, text='��������ϵ: QQ:3173362514@qq.com��',font=("����", 10), justify='left').place(x=10,y=625)

    # ʱ�� ��ʾ
    def gettime():
        var1.set('����:'+time.strftime("%y/%m/%d"))
        var2.set('ʱ��:'+time.strftime("%H:%M:%S"))
        app.after(1000, gettime)
    var1 = tk.StringVar()
    var2 = tk.StringVar()
    app.after(1,gettime())
    tk.Label(app, textvariable=var1, fg='darkred', font=("����", 10)).place(x=690,y=600)
    tk.Label(app, textvariable=var2, fg='darkred', font=("����", 10)).place(x=690, y=625)

    # ���ز˵�
    def rback():
        """
        ���ز˵������²���
        :return:
        """
        global app_singlers
        # ֹͣǰ�����ź�,�������˵��źţ��ر����
        info[5] = 3  # info
        app_singlers['exsit'] = False
        app_singlers['menu'] = True
        app_singlers['monitor'] = False
        app_singlers['config'] = False
        app_singlers['systemsport'] = False
        app_singlers['help'] = False
        # ȷ�����õ�����
        app.destroy()  # ����ر�

    def quit():
        """
        �˳�ϵͳ�����²���
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

    tk.Button(app, text="���ز˵�", width=15, bg='green', font=("����", 14), height=2, command=rback).place(x=150, y=510)
    tk.Button(app, text="�˳�ϵͳ", width=15, bg='green', font=("����", 14), height=2, command=quit).place(x=500, y=510)
    app.mainloop()

def manu(wea):
    """
    �˵�����.
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
    tk.Label(app, text="A2.0�������������ϲɼ�����ϵͳ", justify='center', bg='aqua',
             height=3, width=36, fg='black', font=('����', 32,)).place(x=0, y=0)
    tk.Label(app, text=f"{rand_cts()}", justify='left', fg='slateblue',
             height=4, width=33, font=("����", 20,)).place(x=0, y=135)
    tk.Label(app, text="\n�û���֪!\n"+foruser, justify='left', fg='red',
             height=20,width=55,font=("����", 12,)).place(x=0,y=249)
    tk.Label(app, text="�˵�", justify='right', fg='tomato',
             height=4, width=30, font=("����", 22,)).place(x=400, y=135)
    tk.Label(app, text=f"{wea}", justify='left', fg='slateblue',
             height=2, width=120, font=("����", 10,)).place(x=0, y=570)
    tk.Label(app, text='ע�⣺��Ӧ�ý�Ϊѧϰ�о�����������ҵ��;!', bg='red',font=("����", 10), justify='left',
             ).place(x=10, y=600)
    tk.Label(app, text='��������ϵ: QQ:3173362514@qq.com��',font=("����", 10), justify='right').place(x=10, y=625)

    # ʱ�� ��ʾ
    def gettime():
        """
        ��Ļʱ��ˢ��
        :return:
        """
        var1.set('����:' + time.strftime("%y/%m/%d"))
        var2.set('ʱ��:' + time.strftime("%H:%M:%S"))
        app.after(1000, gettime)

    var1 = tk.StringVar()
    var2 = tk.StringVar()
    tk.Label(app, textvariable=var1, fg='darkred', font=("����", 10)).place(x=690, y=600)
    tk.Label(app, textvariable=var2, fg='darkred', font=("����", 10)).place(x=690, y=625)

    def sport():
        """
        ���������壬�źŸ���
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
        ��������壬�����ź�
        :return:
        """
        su = tkinter.messagebox.askokcancel('����','����������ǰ���������ռ�����\n'
                                                 '��ȷ���Ѿ����ú�����')
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
        �˵��������ã������ź�
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
        �����źţ��������
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
        ϵͳ�˳��źţ��źŸ���
        :return:
        """
        global app_singlers
        app_singlers['exsit'] = True
        app_singlers['menu'] = False
        app_singlers['monitor'] = False
        app_singlers['config'] = False
        app.destroy()
    def peoxies():
        tkinter.messagebox.showinfo('��ʾ','����ά���У���δ����')


    gettime()
    # ��Ѵ���
    tk.Button(app, text="�ռ�����", width=15, bg='deepskyblue', font=("����", 14), height=2, command=config).place(x=550, y=364)
    tk.Button(app, text="��������", width=15, bg='deepskyblue', font=("����", 14), height=2, command=peoxies).place(x=550, y=312)
    tk.Button(app, text="������", width=15, bg='deepskyblue', font=("����", 14), height=2, command=quit_go_monitor).place(x=550, y=416)
    tk.Button(app, text="ϵͳ֧��", width=15, bg='deepskyblue', font=("����", 14), height=2, command=sport).place(x=550,
                                                                                                             y=260)
    tk.Button(app, text="ʹ�ð���", width=36, bg='green', font=("����", 14), height=2, command=help).place(x=445, y=468)
    tk.Button(app, text="�˳�ϵͳ", justify='center', width=36, bg='green', font=("����", 14), height=2, command=quit).place(x=445, y=520)
    app.mainloop()

def configer(wea):
    """
    �޸Ŀ������
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
    tk.Label(app, text="A2.0�ɼ�ϵͳ����", justify='center',bg='yellow',
             height=1, width=16, font=('����', 32,)).place(x=240, y=30)
    tk.Label(app, text='�����ļ��� :', justify='left',bg='aqua', height=1, width=12, font=("����", 16,)).place(x=30, y=165)
    tk.Label(app, text='�޶�������:',justify='left',bg='aqua', height=1, width=12, font=("����", 16,)).place(x=30,y=210)
    tk.Label(app, text='�����ؼ���:', justify='left',bg='aqua',height=1, width=12, font=("����", 16,)).place(x=30,y=260)
    tk.Label(app, text='���˹ؼ���:',justify='left', bg='aqua',height=1, width=12, font=("����", 16,)).place(x=30,y=310)
    tk.Label(app, text='������ַ�: ',justify='left',bg='aqua', height=1, width=12, font=("����", 16,)).place(x=30,y=360)
    tk.Label(app, text='QQ email: ', justify='left', bg='aqua', height=1, width=12, font=("����", 16,)).place(x=30, y=410)
    tk.Label(app, text='��ʾ�������ϣ���ʼ�֪ͨ�����Բ�������: ', justify='left', bg='orange', height=1, width=40, font=("����", 16,)).place(x=30, y=500)

    # ����
    tk.Label(app, text='D:/example1/example2 ',bg='royalblue', justify='left', height=1, width=30, font=("����", 16,)).place(x=440, y=165)
    tk.Label(app, text='3', justify='left', bg='royalblue',height=1, width=30, font=("����", 16,)).place(x=440, y=210)
    tk.Label(app, text='���ѧϰ�����ԣ�����ѧϰ', bg='royalblue',justify='left', height=1, width=30, font=("����", 16,)).place(x=440, y=260)
    tk.Label(app, text='��ѵ��java����ȫ', justify='left',bg='royalblue', height=1, width=30, font=("����", 16)).place(x=440, y=310)
    tk.Label(app, text='���ѧϰ������,�ܽ�', justify='left',bg='royalblue', height=1, width=30, font=("����", 16,)).place(x=440, y=360)
    tk.Label(app, text='111111,111111@qq.com', justify='left', bg='royalblue', height=1, width=30, font=("����", 16,)).place(x=440,
                                                                                                                 y=410)


    text0 = tk.Text(app,bg='tan', width=20, height=1, font=("����", 15,))
    text0.place(x=200, y=168)
    text0.delete(0.0, tk.END)
    text0.insert(tk.INSERT, '')
    text0.update()

    text1 = tk.Text(app,bg='tan', width=20, height=1,font=("����", 15,))
    text1.place(x=200,y=213)
    text1.delete(0.0, tk.END)
    text1.insert(tk.INSERT, 3)
    text1.update()

    text2 = tk.Text(app, bg='tan',width=20, height=1, font=("����", 15,))
    text2.place(x=200, y=264)
    text2.delete(0.0, tk.END)
    text2.insert(tk.INSERT, '')
    text2.update()

    text3 = tk.Text(app,bg='tan', width=20, height=1, font=("����", 15,))
    text3.place(x=200, y=313)
    text3.delete(0.0, tk.END)
    text3.insert(tk.INSERT,'')
    text3.update()

    text4 = tk.Text(app, bg='tan',width=20, height=1, font=("����", 15,))
    text4.place(x=200, y=363)
    text4.delete(0.0, tk.END)
    text4.insert(tk.INSERT, '')
    text4.update()

    text5 = tk.Text(app, bg='tan', width=20, height=1, font=("����", 15,))
    text5.place(x=200, y=413)
    text5.delete(0.0, tk.END)
    text5.insert(tk.INSERT, 'None')
    text5.update()
    tkinter.messagebox.showwarning('ע��', "������Ϣ��ؼ����ж����������','�ָ"
                                        "���龡���ܶ�һЩ�����ַ���Ϊ����ֱ��Ӱ����׼ȷ��!")
    def get_conf():
        """
        ��ȡ�û�������
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
            tkinter.messagebox.showerror('����','��ȷ��·���Ƿ���ȷ')
        else:
            ask = tkinter.messagebox.askokcancel('��ȷ��',str(consumconfig).replace(',','\n')+'\nȷ���ύ��')
            if ask:
                    tkinter.messagebox.showinfo('�ɹ�','������ɡ�')
                    tk.Button(app, text="�ύ", width=15, bg='green', font=("����", 14), height=2, command=get_conf).place(
                        x=25, y=530)
        user_conf = consumconfig


    def gettime2():
        """
        ʱ��ˢ��
        :return:
        """
        var3.set('����:' + time.strftime("%y/%m/%d"))
        var4.set('ʱ��:' + time.strftime("%H:%M:%S"))
        app.after(1000, gettime2)

    def rback():
        """
        ���ز˵������²���
        :return:
        """
        global app_singlers
        # ֹͣǰ�����ź�,�������˵��źţ��ر����
        info[5] = 3   # info
        app_singlers['exsit'] = False
        app_singlers['menu'] = True
        app_singlers['monitor'] = False
        app_singlers['config'] = False
        # ȷ�����õ�����
        app.destroy() # ����ر�

    # �˳�ϵͳ
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
    tk.Button(app, text="���ز˵�", width=15, bg='green', font=("����", 14), height=2, command=rback).place(x=340, y=530)
    tk.Button(app, text="�˳�ϵͳ", width=15, bg='green', font=("����", 14), height=2, command=quit).place(x=620, y=530)
    tk.Button(app, text="�ύ", width=15, bg='red', font=("����", 14), height=2, command=get_conf).place(x=25, y=530)
    tk.Label(app, text='��ע����Ӧ�ý�Ϊѧϰ�о�����������ҵ��;!', bg='red',font=("����", 10), justify='left',
             ).place(x=10,y=600)
    tk.Label(app, text='��������ϵ: QQ:3173362514@qq.com��', font=("����", 10),justify='right').place(x=10,y=625)
    tk.Label(app, textvariable=var3, fg='black', font=("����", 10)).place(x=690, y=600)
    tk.Label(app, textvariable=var4, fg='black', font=("����", 10)).place(x=690, y=625)
    gettime2()
    app.mainloop()

def systemsport(wea):
    """
    ϵͳ֧�����
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
    tk.Label(app, text="ϵͳ֧��", justify='center', bg='aqua',
             height=3, width=36, fg='black', font=('����', 32,)).place(x=0, y=0)
    tk.Label(app, text='ע�⣺��Ӧ�ý�Ϊѧϰ�о�����������ҵ��;!', bg='red', font=("����", 10), justify='left',
             ).place(x=10, y=600)
    tk.Label(app, text='��������ϵ: QQ:3173362514@qq.com��', font=("����", 10), justify='right').place(x=10, y=625)
    tk.Label(app, text=f"{wea}", justify='left', fg='slateblue',
             height=2, width=120, font=("����", 10,)).place(x=0, y=570)
    tk.Label(app, text='����¼��վ����:\n',height=4,width=30,bg='spring green', font=("����", 20), justify='left',
            ).place(x=400, y=206)
    tk.Label(app, height=5, bg='spring green', width=35, font=("����", 18), justify='left',
             ).place(x=400, y=300)
    tk.Label(app, text='https://www.csdn.net/', height=5, bg='spring green', width=35, font=("����", 18), justify='left',
             ).place(x=400, y=340)

    tk.Label(app, text='1�����������������ϸ����ɼ���', font=("����", 16), justify='left',
            ).place(x=10, y=206)
    tk.Label(app, text='2��������ѧϰ���ĸ����ɼ���', font=("����", 16), justify='left',
             ).place(x=10, y=246)
    tk.Label(app, text='3�����������������������ռ���', font=("����", 16), justify='left',
             ).place(x=10, y=286)
    tk.Label(app, text='5��ʵʱ����', font=("����", 16), justify='left',
             ).place(x=10, y=366)
    tk.Label(app, text='6��ʵʱ����', font=("����", 16), justify='left',
             ).place(x=10, y=366)
    tk.Label(app, text='4��Email �ʼ�֪ͨ', font=("����", 16), justify='left',
             ).place(x=10, y=326)
    # tk.Label(app, text='ϵͳ��Ƶĳ����Ǹ�����ʦ�ռ����ѧϰ���������������ռ�Ч�����ܱ�֤��', font=("����", 17), justify='left',
    #          ).place(x=0, y=137)

    def gettime():
        """
        ����ʱ�����
        :return:
        """
        var1.set('����:' + time.strftime("%y/%m/%d"))
        var2.set('ʱ��:' + time.strftime("%H:%M:%S"))
        app.after(1000, gettime)

    var1 = tk.StringVar()
    var2 = tk.StringVar()
    tk.Label(app, textvariable=var1, fg='darkred', font=("����", 10)).place(x=690, y=600)
    tk.Label(app, textvariable=var2, fg='darkred', font=("����", 10)).place(x=690, y=625)
    gettime()

    # ���ز˵�
    def rback():
        """
        ���ز˵������²���
        :return:
        """
        global info
        global app_singlers
        # ֹͣǰ�����ź�,�������˵��źţ��ر����
        info[5] = 3  # info
        app_singlers['exsit'] = False
        app_singlers['menu'] = True
        app_singlers['monitor'] = False
        app_singlers['config'] = False
        app_singlers['systemsport'] = False
        # ȷ�����õ�����
        app.destroy()  # ����ر�

    def quit():
        """
        �˳�ϵͳ�����²���
        :return:
        """
        global app_singlers
        app_singlers['exsit'] = True
        app_singlers['menu'] = False
        app_singlers['monitor'] = False
        app_singlers['config'] = False
        app_singlers['systemsport'] = False
        app.destroy()

    tk.Button(app, text="���ز˵�", width=15, bg='green', font=("����", 14), height=2, command=rback).place(x=150, y=510)
    tk.Button(app, text="�˳�ϵͳ", width=15, bg='green', font=("����", 14), height=2, command=quit).place(x=500, y=510)
    app.mainloop()




def monitor(wea,newconf):
    """
    �������
    :param wea: ������Ϣ
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
    tk.Label(app, text="�ɼ�����ϵͳ������", justify='center', bg='cyan',
             height=3, width=36, fg='black', font=('����', 32,)).place(x=0, y=0)
    # tk.Label(app, text='ϵͳ��������', bg='yellow', height=1, width=15, font=("����", 16,)).place(x=500, y=160)
    tk.Label(app, text='״̬', bg='red', height=1, width=8, font=("����", 16,)).place(x=20, y=160)
    tk.Label(app, text='������',bg='yellow', height=1, width=8, font=("����", 16,)).place(x=20, y=210)
    tk.Label(app, text='������',bg='seagreen', height=1, width=8, font=("����", 16,)).place(x=20, y=260)
    tk.Label(app, text='ʧ����',bg='tomato', height=1, width=8, font=("����", 16,)).place(x=20, y=310)
    tk.Label(app, text='�ɹ���', bg='lime',height=1, width=8, font=("����", 16,)).place(x=20, y=360)
    tk.Label(app, text='ʧ����',bg='salmon', height=1, width=8, font=("����", 16,)).place(x=20, y=410)
    tk.Label(app, text='������', bg='gold',height=1, width=8, font=("����", 16,)).place(x=20, y=460)
    tk.Label(app, text='�ļ�(M)',bg='lime', height=1, width=8, font=("����", 16,)).place(x=20, y=510)
    tk.Label(app, text=f"{wea}", justify='left', fg='slateblue',
             height=2, width=120, font=("����", 10,)).place(x=0, y=570)
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
    tkinter.Label(app, text='\n\n\n���Ĳ��������������:\n\n'+(ucon),justify='left',height=25, width=85,font=("����", 10)).place(x=220, y=160)
    tk.Label(app, text='��ע����Ӧ�ý�Ϊѧϰ�о�����������ҵ��;!', bg='red', font=("����", 10), justify='left').place(x=10, y=600)
    tk.Label(app, text='��������ϵ: QQ:3173362514@qq.com��', font=("����", 10), justify='right').place(x=10, y=625)
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
        ���ڸ���
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
        ����������������źŲ���
        :return:
        """
        global info
        global app_singlers
        app_singlers['crawl'] = True # ���濪���ź�
        info[5] = 2  # -----������  # ------��״̬
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
        ֹͣ���棬�����źŲ���
        :return:
        """
        global info
        global app_singlers
        global t
        info[5] = 1 # -----> ͣ�����ź�
        info[4] = 4 # ״̬
        app_singlers['crawl'] = False # -������ͣ�ź�
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
        ��ʾ�û����ݴ洢·��
        :return:
        """
        p = CSDN['save_path']
        tkinter.messagebox.showinfo('��ʾ',p)

    def quit():
        """
        �˳�ϵͳ�������ź�
        :return:
        """
        global info
        sur = tkinter.messagebox.askokcancel('����','ȷ���˳�������˳����񽫲��ܼ������У�')
        if sur is True:
            info[5] =3 # ״̬ �˳�ϵͳ
            global app_singlers
            app_singlers['exsit'] = True
            app_singlers['menu'] = False
            app_singlers['monitor'] = False
            app_singlers['crawl'] = False # �˳��źų�ʼ��
            try:
                stop_thread(t)
            except:
                pass
            finally:
                app.destroy()
        else:
            pass

        # ʱ�� ��ʾ
    def gettime2():
        """
        ��Ļʱ�����
        :return:
        """
        var3.set('����:' + time.strftime("%y/%m/%d"))
        var4.set('ʱ��:' + time.strftime("%H:%M:%S"))
        app.after(1000, gettime2)
    var3 = tk.StringVar()
    var4 = tk.StringVar()
    gettime2()
    tk.Label(app, textvariable=var3, fg='black', font=("����", 10)).place(x=700, y=600)
    tk.Label(app, textvariable=var4, fg='black', font=("����", 10)).place(x=700, y=625)

    # ���ز˵�
    def rback():
        """
        ���ز˵�
        :return:
        """
        global info
        global app_singlers
        # ֹͣǰ�����ź�,�������˵��źţ��ر����
        info[5] = 3   # info
        sur = tkinter.messagebox.askokcancel('����', 'ȷ�Ϸ�����������ؽ��е����񽫲��ܼ������У�')
        if sur:
            app_singlers['exsit'] = False
            app_singlers['menu'] = True
            app_singlers['monitor'] = False
            app_singlers['crawl'] = False
            # ȷ�����õ�����
        try:
            stop_thread(t)
            app.destroy() # ����ر�
        except:
            app.destroy()
            pass
        finally:
            info = [0, 0, 0, 0, 4, 2]

    tk.Button(app, text="��ʼ",bg='lime', width=10, command=star).place(x=300,y=510)
    tk.Button(app,text='��ֹ',bg='lime', width=10, command=stop).place(x=400,y=510)
    tk.Button(app, text="�˳�ϵͳ",bg='red', width=10, command=quit).place(x=700,y=510)
    tk.Button(app,text="�ļ�·��", bg='lime',width=10, command=path_sav).place(x=600,y=510)
    tk.Button(app,text="���ز˵�",bg='lime',width=10,command=rback).place(x=500,y=510)
    app.after(1, refreshText)
    app.mainloop()


def monitor_center(wea,conf):
    """
    ��������߼�����
    :return:
    """
    global app_singlers
    wea = weather()
    try:
        monitor(wea,conf)
    except Exception as e:
        print('ERRO��',e,'welcom.py 746')
def rulinning():
    """
    �������к�������׽�źŴ���Ӧ����
    :return:
    """
    inite()
    print('ϵͳ��ӭ����')
    wea = weather()
    app_welcom(wea)
    i = 0
    while True:
        i = i+1
        print('�����źű仯��',app_singlers)
        if app_singlers['menu'] is True:
            print('����˵�ҳ��')
            manu(wea)
        if app_singlers['config'] is True:
            print('�����źű仯��', app_singlers)
            print('�������ã�')
            configer(wea)
        if app_singlers['exsit'] is True:
            print('�����źű仯��', app_singlers)
            print('�˳�ϵͳ��')
            break
        if app_singlers['monitor'] is True:
            print(user_conf)
            newconfig = autconfig(user_conf)
            time.sleep(0.01)
            print(newconfig,'''----------''') # --------------�޸ĵ�����
            print('�����źű仯��', app_singlers)
            print('���������')
            monitor_center(wea,newconfig)

        if app_singlers['help'] is True:
            print('�����źű仯��', app_singlers)
            print('����ʹ�ð���')
            app_help(wea)

        if app_singlers['systemsport'] is True:
            print('�����źű仯��', app_singlers)
            print('����֧��')
            systemsport(wea)
        if i >100000:
            raise SystemExit from Statatus
        else:
            print('������׽�����ź�')
            continue




if __name__ == '__main__':
     rulinning()
