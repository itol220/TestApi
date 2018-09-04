import json,random,string,time,pymysql.cursors,hashlib,xlrd,yagmail,os,smtplib
from jsonschema import validate
from requests import Session
from .recursion import GetDictParam
from config import config

from email.mime.text import MIMEText
from email.header import Header



class HttpHandler(GetDictParam):
    def __init__(self):
        super(HttpHandler,self).__init__()
        self.session = Session()
        # self.headers = {
        #
        # }

    # def mobile(self):
    #     patten = ['138','139','140','155','158','147','131','132']
    #     mobile = random.choice(patten) + ''.join(random.sample(string.digits,8))
    #     return mobile
    #
    def newName(self):
        '''新增随机内容'''
        newName = '测试' + ''.join(random.sample(string.digits,6)) + random.choice(string.ascii_letters)
        return newName
    #
    def updateName(self):
        '''修改随机内容'''
        updateName = '修改' + ''.join(random.sample(string.digits,7)) + random.choice(string.ascii_letters)
        return updateName

    # def mail(self):
    #     # 发送邮箱服务器
    #     smtpserver = 'smtp.sina.com'
    #     # 发送邮箱用户/密码
    #     user = 'username@sina.com'
    #     password = '123456'
    #     # 发送邮箱
    #     sender = 'username@sina.com'
    #     # 接收邮箱
    #     receiver = 'receive@126.com'
    #     # 发送邮件主题
    #     subject = 'Python email test'
    #
    #     # 编写HTML类型的邮件正文
    #     msg = MIMEText('<html><h1>你好！</h1></html>', 'html', 'utf-8')
    #     msg['Subject'] = Header(subject, 'utf-8')
    #
    #     # 连接发送邮件
    #     smtp = smtplib.SMTP()
    #     smtp.connect(smtpserver)
    #     smtp.login(user, password)
    #     smtp.sendmail(sender, receiver, msg.as_string())
    #     smtp.quit()

    def mail(self,maillist=None):
        '''发送测试报告到邮箱'''
        yag = yagmail.SMTP(user="panjinming@i3020.com",password="am123456.",host="smtp.i3020.com",encoding="utf-8")
        contents = "官网最新接口测试报告，请用浏览器打开查看"
        yag.send(maillist,"官网接口测试报告",contents,r"C:\Users\kk\PycharmProjects\testAPI\report\测试报告.html")


    def read_excel(self,sheet,rows,cols):
        '''读取excel值'''
        osPath = r"C:\Users\kk\PycharmProjects\testAPI\report\test.xlsx"
        workbook = xlrd.open_workbook(osPath)
        table = workbook.sheets()[sheet]
        return table.cell_value(rows,cols)

    def db_seleect(self,db=None,sql=None):
        '''查询数据库'''
        config_zjh = {"host": "47.97.23.104 ", "port": 3306,
                      "user": "zhangjinhong", "passwd": "zjh*djkj@HZ2018",
                      "db": db, "charset": "utf8"}
        db = pymysql.connect(**config_zjh)
        # 创建游标
        cursor = db.cursor()
        # sql = 'select * from dj_account'  # where id=93930'
        cursor.execute(sql)  # execute执行一个数据库查询和命令
        results = cursor.fetchall()  # 返回给客户端执行后的数据,
        # 关闭数据库连接
        cursor.close()  # 关闭游标
        db.close()  # 关闭连接
        return results[0][0]

    def get(self,url=None):
        '''get'''
        resp = self.session.get(url=url).text
        return resp

    def post(self,url=None,data=None,json=None):
        '''post'''
        resp = self.session.post(url=url,json=json).text if json else self.session.post(url,data=data).text
        return resp

    def sign(self,token=None,uid=None,uid_check=None):
        '''sign生成规则'''
        if not uid_check: token,uid = str(config.sign_IOS_data["timeline"])[0:4],config.login_data["cpn"]
        sign_str = "{}{}{}{}{}hzdjkj16{}{}".format(config.sign_IOS_data["ai"],config.sign_IOS_data["vc"],
                                               config.sign_IOS_data["dt"],config.sign_IOS_data["os"],token,
                                                     str(config.sign_IOS_data["timeline"])[-6::],uid)
        return hashlib.md5(f"{sign_str}{len(sign_str)}".encode()).hexdigest()

    def logOut(self,msg=None):
        '''日志输出'''
        time1 = time.strftime('%Y-%m-%d %H:%M:%S')
        print(f"{time1}————{msg}......")



    # def selector_issue(self,rows=None,seKey=None,id=None):
    #     idList = []
    #     for item in rows:
    #         if item[seKey] == id:
    #             idList.append(item)
    #     return idList[0] if idList != [] else '列表中不存在该处理类型的事件'




    @classmethod
    def valid_json(cls,myjson,class_name,schname):
        """ 按照jsonSchema格式校验jsonkey、jsonkeyType、jsonCount """
        schfile = 'schema/%s/%s.json' % (class_name,schname)
        with open(schfile,'r',encoding='utf-8') as f:
            mysch = json.load(f)
        try:
            validate(myjson,mysch)
        except Exception as e:
            print(e)
        else:
            return True
        finally:
            pass











