
import unittest,os
from lib import HttpHandler
from BeautifulReport import BeautifulReport


if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover('tests',pattern='test_*.py')
    report = BeautifulReport(suite)
    report.report(filename='测试报告',description='测试daefult报告',log_path='report')
    HttpHandler().mail(["panjinming@i3020.com"])



