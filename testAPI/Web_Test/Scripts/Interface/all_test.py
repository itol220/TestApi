# -*- coding:UTF-8 -*-
'''
Created on 2015-10-22

@author: N-254
'''
from __future__ import unicode_literals
import sys 
sys.path.append("/Scripts/Interface")
# from ShiYouRenKou import *
# from XianSuoGuanLi import *
import unittest
import HTMLTestRunner
import all_caselist

# sys.path.append("/selenium_use_case/test_case")
#获取数组方法
# reload(sys)
# sys.setdefaultencoding('utf-8')
alltestnames = all_caselist.caselist()
print alltestnames
suite = unittest.TestSuite()
if __name__ == '__main__':
    # 这里我们可以使用defaultTestLoader.loadTestsFromNames(),
    # 但如果不提供一个良好的错误消息时，它无法加载测试
    # 所以我们加载所有单独的测试，这样将会提高脚本错误的确定。
    for test in alltestnames:
        try:
        #最关键的就是这一句，循环执行数据数的里的用例。
            suite.addTest(unittest.defaultTestLoader.loadTestsFromName(test))
        except Exception:
            print 'ERROR: Skipping tests from "%s".' % test
            try:
                __import__(test)
            except ImportError:
                print 'Could not import the test module.'
            else:
                print 'Could not load the test suite.'
    from traceback import print_exc
    print_exc()
print
print 'Running the tests...'
filename = 'D:\\AutoTest\workspace\\SOAInterfaceAutoTest\\test_result.html'
fp = file(filename, 'wb')
runner =HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='平安信息系统后台接口测试报告',
        description='平安信息系统后台十大模块自动化测试结果')
runner.run(suite)