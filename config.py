# --coding:GBK --
import random,os


# �Ƿ�ÿ������ǰ ��ʼ��
reback = False

# �����ӳ�
slpt = 5


# ��������Ƭ�� = Mpage * 36 * key_word
MPage = 20

# ����״̬
Statatus =['������','��������','��������','���н���','ֹͣ']

CSDN = {
    'log_path':'./CN_DOM/info.txt',
    'erro_log_path':'./CN_DOM/erro.txt',
    'save_path':'./CN_DOM',
    'remenber':'./CN_DOM/remenber.csv',
    'email':'NONE',

    # �û����룬�ؼ��֡������������ݡ��ĵ����������ڵ�����.
    # ���ѧϰ���
    'key_word':['���ѧϰ����','AI����','�˹�������'],
    'flag':3, #
    'consume': ['���ѧϰ', '����ѧϰ', '����', '����', '����', '��', 'AI',
               '�˹�����', 'ѧϰ', '�ܽ�', '֪ʶ'],  # ���±���ȷ�ϣ������������κ�����ֱ�ӹ���

    # ͨ�����ã����˱����Լ�url������Щ�ַ�������,һ�㲻���޸ģ�ͨ������
    'fl_url':['book','download','GitChart','weixin'], # url ������Щ���˵�
    'fl_title':['��Դ','����','PDF','�۸񣬡�Ŀ¼','ָ���ֲ�','�γ�','��ȫ'
                '�鼮','ǰ��','ʵս','����'], # ���� ����
 }

# ��ʼ��������Դ�ļ�
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
    �ж��ļ��Ƿ���ڣ��ļ�·���������򴴽��ļ���
    :param file_url: �ļ�·���������ļ���
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
            # ������ֱ�Ӵ������ļ�

        else:
            return None

check_and_creat_dir()


# �û���֪
foruser = '\n   ��ϵͳ���ڸ����û��ռ������಩�ġ������\n'\
          'ѧϰ����,�û����Ը�����Ҫ�������ļ������޸�\n'\
          '��ʵ�ֲ�ͬ�������ռ�����ϵͳ���б��ϸ�����,\n'\
          'û����ͼ������ƽ���վ���ܵ��ƻ�����Ȩ����Ϊ\n'\
          'ʹ����Ӧ�������Լ����ռ���Ϊ,����Ƶ��ʹ�á�ϵ\n'\
          'ͳÿ�����з��ʶ��������¼�ļ�Ĭ�����ϵͳ��\n'\
          '�������������ÿ�����ж���ʼ��ϵͳ,��˵��\n'\
          'ֱ���޸�����,������ϵ3173362514@qq.com�����\n'\
          '���ַ�����Ȩ�����Ϊϣ������ʱ�������ü�ʱ��\n' \
          '��,����������ʧ������ϵͳ�����������ϣ����\n' \
          'ѧϰ�Ͽ��԰�����ҡ����ף��������졢ѧ����\n' \
          '�ɡ���ҵ˳��!'

# ��Ϣ
infomation = 'ϵͳĬ��Ӧ������ǰ�󲻾��г�ʼ����������ʷ���������Ժ�У��,��ֹ�ظ�ץȡ��' \
             '������޸ģ��뽫config.py�µ� "reback"��ΪTrue���������������config.py �ļ�'

#
helpinfo = '1������ϵͳ��������û���֪��                            \n' \
           '2���������ã������ռ��ļ��ı����ַ��                      \n' \
           '3�����������ɣ��Ϳ��Խ��������壬���Կ�����������ռ����� \n' \
           '4�������������Բ鿴������ͬ����״����Ҳ����ǿ����ֹ����    \n' \
           '5�������������벻Ҫ�ر���壬��������쳣�˳���              \n' \
           '6������ÿ�����ж��������¼�ļ������ڹ������ݣ������Ҫ���г�ʼ��\n' \
           '   ������ɾ��Ŀ¼��DOM/remenber.csv �ļ�                 \n' \
           '7����ϵͳ��Ҫ�����ڸ����û��ռ�һЩ��Ϣ�����ܶ����ݽ��о�ϸ������.\n' \
           '   ��Ҫ�û���һ��������                                  \n' \
           '8������ϵͳ���в����ļ�¼�ļ�����ĵ�ǰĿ¼�µ�CO_DOM�ļ��С�\n'\
           '9��ϵͳ�����������׶Σ�Ŀǰ��¼����վttps://so.csdn.net/��������\n' \
           '   ���ޣ����ڽ�������վ��¼�����������ڴ���\n'



# ϵͳ����ź�
app_singlers = {
    'exsit':False,  # �˳�
    'menu':False,   # �˵�
    'monitor':False, # ���
    'config':False, # ����
    'systemsport':False, # ֧��
    'crawl':False,
    'help':False,
}

def getheaders():
    """
    �������ͷ
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
        # �Ա������
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
        # �Ա������
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
        # QQ�����
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        # sogou�����
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)",
        # maxthon�����
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36",
        # UC�����
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36",
    ]

    # һ���� PC�˵�
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
# ���������������ͷ--->pass
HEADERS= getheaders()


def delm():
    paths = ['log_path','erro_log_path','remenber']
    for i in paths:
        if os.path.isfile(CSDN[i]):
            try:
                os.remove(CSDN[i])
            except Exception as e :
                print(e)



