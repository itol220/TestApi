# -*- coding:UTF-8 -*-
'''
Created on 2016-3-7

@author: N-286
'''
from __future__ import unicode_literals
from COMMON import Log
from CONFIG.InitDefaultPara import userInit
from Interface.PingAnJianShe.SystemMgr import SystemMgrIntf
from Interface.PingAnTong.DengLuDengChu.MbDengLuDengChuIntf import \
    getCurrentLoginUser
from Interface.PingAnTong.pingAnTongHttpCommon import pingantong_login
import unittest

class MbDengLuDengChu(unittest.TestCase):


    def setUp(self):
        SystemMgrIntf.initEnv()
        pass

    '''
    @功能：职能部门登录
    @ chenhui 2016-3-7
    '''
    def testmRiChangBanGong_001(self):
        '''登录登出-职能部门登录'''
        res1=pingantong_login(userName=userInit['DftQuFuncUser'],passWord='11111111')
        self.assertTrue(res1,'街道职能部门登录失败')
        Log.LogOutput(message='街道职能部门登录成功！')
        res2=getCurrentLoginUser(username = userInit['DftQuFuncUser'])
        self.assertEquals(userInit['DftQuFuncUser'], res2['userName'], '返回当前用户信息接口有误')
        Log.LogOutput(message='返回当前职能部门用户信息接口正确！')
        pass

    '''
    @功能：行政部门登录
    @ chenhui 2016-3-7
    '''
    def testmRiChangBanGong_002(self):
        '''登录登出-行政部门登录'''
        res1=pingantong_login(userName=userInit['DftJieDaoUser'],passWord='11111111')
        self.assertTrue(res1,'街道行政部门登录失败')
        Log.LogOutput(message='街道行政部门登录成功！')
        res2=getCurrentLoginUser(username = userInit['DftJieDaoUser'])
        self.assertEquals(userInit['DftJieDaoUser'], res2['userName'], '返回当前用户信息接口有误')
        Log.LogOutput(message='返回当前行政部门用户信息接口正确！')
        pass
    
    def tearDown(self):
        pass


if  __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    suite = unittest.TestSuite()
    suite.addTest(MbDengLuDengChu("testmRiChangBanGong_001"))
    results = unittest.TextTestRunner().run(suite)
    pass
