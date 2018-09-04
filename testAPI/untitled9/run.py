# -*- coding:utf-8 -*-
from unittest import TestSuite,makeSuite
import HTMLTestRunner,time
from testCase import getDetailByIdTest,createDevTest

a=TestSuite()
a.addTest(makeSuite(getDetailByIdTest))
a.addTest(makeSuite(createDevTest))
time=time.strftime("%y%m%d%H%M%S")
b=file("./result%s"%time+".html","wb")
c=HTMLTestRunner.HTMLTestRunner(stream=b,title=u"接口测试报告")
c.run(a)
b.close()
