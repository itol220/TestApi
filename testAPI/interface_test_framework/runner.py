# -*- coding: utf-8 -*-
# @Author  : hanzilong

import ddt,os,time,unittest
from interface_test_framework.public.HTMLTestReportCN import HTMLTestRunner
from interface_test_framework.public.emails import SendMail
from interface_test_framework.public.get_excel import get_case
from interface_test_framework.public.log import Log
from interface_test_framework.public.test_assert import TestApi

#测试用例文档地址
path1=os.getcwd() +"\\case\\testcase.xlsx"
data_test = get_case(path1)  
@ddt.ddt
class MyTest(unittest.TestCase):
    u"""搜索功能"""
    # @classmethod
    # def setUpClass(cls):
    #     cls.testApi = TestApi()

    def setUp(self):
        pass
    def tearDown(self):
        pass
    @ddt.data(*data_test)
    def test_api(self,data_test):
        api = TestApi(url=data_test['url'], key=data_test['key'], connent=data_test['coneent'], fangshi=data_test['fangshi'])
        Log.info(r'输入参数：url:%s,key:%s,参数:%s,请求方式：%s'%(data_test['url'],data_test['key'],data_test['coneent'],data_test['fangshi']))
        apijson = api.getJson()
        Log.info(r"结果返回码%s"%apijson)
        qingwang=(data_test['assert'])
        self.assertEqual(apijson,qingwang,msg="预期和实际的不一致")
if __name__ == '__main__':
    #生成Html测试报告

    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(MyTest))
    # suite=unittest.main()
    now=time.strftime("%Y-%m-%d %Hh_%Mm", time.localtime(time.time()))
    filename=os.getcwd() +"\\reports\\"+now+"_report.html"
    fl=open(filename,'wb')
    runer=HTMLTestRunner(
    stream=fl,
    title=u'搜索功能测试报告',
    description=u'用例执行情况：',
    tester=u'hanzilong'
    )
    runer.run(suite)
    fl.close()
    #发送测试报告到邮箱
    dir =os.getcwd() +'\\reports'  # 指定文件目录
    file = SendMail.find_new_file(dir)  # 查找最新的html文件
    #邮箱附件地址
    attach_xlsx=os.getcwd() +"\\case\\testcase.xlsx"
    SendMail.mails(file,attach_xlsx)  # 发送html内容邮件

