import unittest
import yagmail

from BeautifulReport import BeautifulReport


def run():
    '''执行测试用例'''
    sutie = unittest.defaultTestLoader.discover('cases', pattern='test_*.py')
    report = BeautifulReport(sutie)
    report.report(filename='Interface_test_report', description='接口测试', log_path='report')


# def mail():
#     '''发送测试报告到邮箱'''
#     yag = yagmail.SMTP(user='812844831@qq.com', password='gbfsmyrpucjtbbjc', host='smtp.qq.com', encoding='utf-8')
#     contents = ('API最新接口测试报告，请用浏览器打开查看报告详情')
#     yag.send(['wangpeng@ccclubs.com','liujinping@ccclubs.com'], '接口测试报告', contents, ('report/Interface_test_report.html'))

if __name__=='__main__':
    run()
    # mail()