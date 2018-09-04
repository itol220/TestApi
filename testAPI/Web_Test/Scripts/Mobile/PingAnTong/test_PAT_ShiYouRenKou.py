# -*- coding:UTF-8 -*-
'''
Created on 2017-09-28

@author: hongzenghui
'''
from __future__ import unicode_literals
import unittest
from Interface.PingAnJianShe.SystemMgr import SystemMgrIntf
from Mobile import MobileUtil
import copy
from Mobile.Define.PingAnTong import CommonModuePara, \
    PopulationRelatedPara
from Mobile.Logic.PingAnTong import CommonModule, ShiJianChuLiLogic
from Mobile.UI.PingAnTong import MyWorkBenchUI, ShiJianChuLiListUI,\
    ShiJianChuLiAddUI, PopupWindowProcessUI, ShiJianChuLiDetailUI,\
    ShiJianChuLiBanLiUI, PopulationAddUI
from Mobile.Define.PingAnTong.CommonModuePara import PopupProcessType,\
    ModuleName
from Mobile.Define.PingAnTong.IssueRelatedPara import IssueProcessState,\
    IssueProcessType, IssueClassifyMenu
from CONFIG import Global, InitDefaultPara
from COMMON import CommonUtil


class PAT_ShiJianChuLi(unittest.TestCase):

    def setUp(self):
#         SystemMgrIntf.initEnv()
#         MobileUtil.MobileDriverInit()
        MobileUtil.MobileDriverReconnect()
        pass
    
    def testIssueAdd_001(self):
        '''事件新增功能'''
#         #登录
#         loginDict = copy.deepcopy(CommonModuePara.loginDict)
#         loginDict['username'] = InitDefaultPara.userInit['DftJieDaoUser']
#         ret = CommonModule.pingantong_login(loginDict)
#         self.assertTrue(ret, '登录失败')
#                            
#         #进入事件处理模块
#         CommonModule.enter_to_module(ModuleName.SHIYOURENKOU)
        
        #事件对象
        populationObject = copy.deepcopy(PopulationRelatedPara.populationObject)
        populationObject['subject'] = 'testIssueFlow%s' % CommonUtil.createRandomString(6)
        populationObject['baseInfo']['idCardNo'] = '330726198202211311'
        PopulationAddUI.base_input_idcard_no(populationObject)
#         ret = ShiJianChuLiLogic.add_issue(issueObject)
#         self.assertTrue(ret, '新增事件失败')
          

        pass
    
    

    def tearDown(self):    
        pass

if  __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(PAT_ShiJianChuLi("testIssueAdd_001"))
    results = unittest.TextTestRunner().run(suite)
    pass
