#
# # "issueLog.targeOrg.id":-1
#
# # "dealTime":2018-04-02
#
#
#
#
#
#
#
# # "android_appversion": 	3.0.0.17
# # import time
# # print(time.strftime("%Y-%m-%d"))
# # a=['1','a','r','t','a','a']
# # list = []
# # for item in a:
# #     if item == 'a':
# #         list.append(item)
# #         break
# # print(list)
# # # print(list)
# import hashlib
# # str = 'qewrqwrqw13112'
# # print(hashlib.md5(str.encode('utf-8')).hexdigest())
# # print(hashlib.sha1(str.encode('utf-8')).hexdigest())
# # print(hashlib.sha224(str.encode('utf-8')).hexdigest())
# # print(hashlib.sha256(str.encode('utf-8')).hexdigest())
# # print(hashlib.sha384(str.encode('utf-8')).hexdigest())
# # print(hashlib.sha512(str.encode('utf-8')).hexdigest())
# # m = hashlib.md5()
# # m.update(str.encode('utf-8'))
# # m1 = m.hexdigest()
# # print(m1)
# import  requests,json
# from lxml import etree
#
# class BaseCrawl:
#     def __init__(self):
#         pass
#
#     def request(self,url,encoding='utf-8'):
#         response = requests.get(url)
#         if response.encoding != 'utf-8':
#             response.encoding = encoding
#         return response.text
#
#     def parse(self,html,xpaths):
#         selector = etree.HTML(html)
#         if isinstance(xpaths,(tuple,list)):
#             return [selector.xpath(xpath) for xpath in xpaths]
#         return selector.xpath(xpaths)
#
#     def output(self,url,xpath):
#         html = self.request(url)
#         return self.parse(html,xpath)
# import yagmail
# def mail(self, maillist=None):
#     '''发送测试报告到邮箱'''
#     yag = yagmail.SMTP(user="panjinming@i3020.com", password="am123456.", host="smtp.i3020.com", encoding="utf-8")
#     contents = "官网最新接口测试报告，请用浏览器打开查看"
#     yag.send(maillist, "官网接口测试报告", contents, r"C:\Users\kk\PycharmProjects\testAPI\report\测试报告.html")
# if __name__ == '__main__':
#     mail(["panjinming@i3020.com"])

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'panjinming@i3020.com'
password = 'am123456.'
receivers = ['812844831@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# mail_msg = """
# <p>Python 邮件发送测试...</p>
# <p><a href="http://www.runoob.com">这是一个链接</a></p>
# """
mail_msg = open(r"C:\Users\kk\PycharmProjects\testAPI\report\测试报告.html","r",encoding="utf-8").read()

message = MIMEText(mail_msg, 'html', 'utf-8')
message['From'] = Header("菜鸟教程", 'utf-8')
message['To'] = Header("测试", 'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP("smtp.i3020.com")
    smtpObj.login(sender,password)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print(e,"Error: 无法发送邮件")

