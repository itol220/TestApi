# -*- coding: utf-8 -*-
# @Author  : hanzilong

import email.mime.multipart
import os,smtplib,time
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.utils import formataddr


class SendMail:
    def mails(self,file,attach_xlsx):
        my_sender='----@qq.com'    # 发件人邮箱账号
        my_pass = '-----'              # 发件人邮箱密码(当时申请smtp给的口令)
        my_user='395122991@qq.com'      # 收件人邮箱账号，我这边发送给自己
        msg = email.mime.multipart.MIMEMultipart()  # 生成包含多个邮件体的对象
        msg['From']=formataddr(["发件人昵称",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["收件人昵称",my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        msg['Subject']="邮件主题-测试" +t               # 邮件的主题，也可以说是标题
        # 读取html文件内容
        f = open(file, 'rb')
        mail_body = f.read()
        f.close()
        # 邮件正文,将文件正文当成附件发送,当正文内容很多时,提高效率
        txt = email.mime.text.MIMEText(mail_body,'html','utf-8')
        msg.attach(txt)
        # # xlsx附件   
        # attach_xlsx=os.getcwd() +"\\case\\testcase.xlsx"
        part = MIMEApplication(open(attach_xlsx,'rb').read())
        part.add_header('Content-Disposition', 'attachment', filename="case.xlsx")
        msg.attach(part)
        # # jpg图片附件
        # jpgpart = MIMEApplication(open(attach_jpg, 'rb').read())
        # jpgpart.add_header('Content-Disposition', 'attachment', filename='接口测试框架.jpg')
        # msg.attach(jpgpart)
        server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是465
        server.login(my_sender,my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,[my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()# 关闭连接
        print("邮件发送成功")
    def find_new_file(self,dir):
        '''查找目录下最新的文件'''
        file_lists = os.listdir(dir)
        file_lists.sort(key=lambda fn: os.path.getmtime(dir + "\\" + fn)
                        if not os.path.isdir(dir + "\\" + fn)
                        else 0)
        # print('最新的文件为： ' + file_lists[-1])
        file = os.path.join(dir, file_lists[-1])
        print('完整文件路径：', file)
        return file

    # dir = 'F:\\untitled7\\reports'  # 指定文件目录
    # file = find_new_file(dir)  # 查找最新的html文件
    # mails(file)  # 发送html内容邮件