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
from Mobile.Define.PingAnTong import CommonModuePara, IssueRelatedPara
from Mobile.Logic.PingAnTong import CommonModule, ShiJianChuLiLogic
from Mobile.UI.PingAnTong import MyWorkBenchUI, ShiJianChuLiListUI,\
    ShiJianChuLiAddUI, PopupWindowProcessUI, ShiJianChuLiDetailUI,\
    ShiJianChuLiBanLiUI
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
        #登录
        loginDict = copy.deepcopy(CommonModuePara.loginDict)
        loginDict['username'] = InitDefaultPara.userInit['DftJieDaoUser']
        ret = CommonModule.pingantong_login(loginDict)
        self.assertTrue(ret, '登录失败')
                           
        #进入事件处理模块
        CommonModule.enter_to_module(ModuleName.SHIJIANCHULI)
        
        #事件对象
        issueObject = copy.deepcopy(IssueRelatedPara.issueObject)
        issueObject['subject'] = 'testIssueFlow%s' % CommonUtil.createRandomString(6)
        issueObject['description'] = 'issueAddAndJiaoban' 
        issueObject['type'] = '其他-其他'
        issueObject['peopleInfo'] = {'asan':'13588806928'}
        issueObject['peopleNo'] = 2
        issueObject['attchment'] = False
        ret = ShiJianChuLiLogic.add_issue(issueObject)
        self.assertTrue(ret, '新增事件失败')
        PopupWindowProcessUI.popup_window_process(promptMessage='是否立即办理', processType=PopupProcessType.NO)
          
        #事件检查
        issueObject['state'] = IssueProcessState.PROCESSING
        ret = ShiJianChuLiLogic.check_issue_info_in_list(issueObject)
        self.assertTrue(ret, '检查事件失败')
          
        #事件交办给社区
        issueObject['processType'] = IssueProcessType.JIAOBAN
        issueObject['jiaobanOrg'] = InitDefaultPara.orgInit['DftSheQuOrg']
        issueObject['jiaobanUser'] = InitDefaultPara.userInit['DftSheQuUserXM']
        issueObject['processOpinion'] = 'jiaobanshequ'
        ret = ShiJianChuLiLogic.process_issue(issueObject)
        self.assertTrue(ret, '交办事件失败')
          
        #退出并用社区账号重新登录
        MobileUtil.close_app()
        MobileUtil.start_app()
        loginDict['username'] = InitDefaultPara.userInit['DftSheQuUser']
        CommonModule.pingantong_login(loginDict)
        #进入事件处理模块
        CommonModule.enter_to_module(ModuleName.SHIJIANCHULI)
        
        #社区账号检查事件信息
        issueObject['state'] = IssueProcessState.UNPROCESS
        ret = ShiJianChuLiLogic.check_issue_info_in_list(issueObject)
        self.assertTrue(ret, '检查事件失败')
          
        #受理并上报
        issueObject['processType'] = IssueProcessType.SHANGBAO
        issueObject['needAccept'] = True
        issueObject['jiaobanOrg'] = None
        issueObject['jiaobanUser'] = None
        issueObject['processOpinion'] = 'shangbaojiedao'
        ret = ShiJianChuLiLogic.process_issue(issueObject)
        self.assertTrue(ret, '上报事件失败')
  
        #用街道账号重新登录
        MobileUtil.close_app()
        MobileUtil.start_app()
        loginDict['username'] = InitDefaultPara.userInit['DftJieDaoUser']
        CommonModule.pingantong_login(loginDict)
        #进入事件处理模块
        CommonModule.enter_to_module(ModuleName.SHIJIANCHULI)
          
        #街道用户重新检查事件
        ret = ShiJianChuLiLogic.check_issue_info_in_list(issueObject)
        self.assertTrue(ret, '检查事件失败')
          
        #受理并协同办理
        issueObject['processType'] = IssueProcessType.XIETONGBANLI
        issueObject['needAccept'] = True
        issueObject['jiaobanOrg'] = InitDefaultPara.orgInit['DftJieDaoFuncOrg']
        issueObject['jiaobanUser'] = InitDefaultPara.userInit['DftJieDaoFuncUserXM']
        issueObject['xiebanOrg'] = InitDefaultPara.orgInit['DftJieDaoFuncOrg1']
        issueObject['xiebanUser'] = InitDefaultPara.userInit['DftJieDaoFuncUserXM1']
        issueObject['processOpinion'] = 'xietongbanli'
        ret = ShiJianChuLiLogic.process_issue(issueObject)
        self.assertTrue(ret, '协同办理事件失败')
  
        #使用街道职能登录
        MobileUtil.close_app()
        MobileUtil.start_app()
        loginDict['username'] = InitDefaultPara.userInit['DftJieDaoFuncUser1']
        CommonModule.pingantong_login(loginDict)
        #进入事件处理模块
        CommonModule.enter_to_module(ModuleName.SHIJIANCHULI)
           
        #检查事件信息
        ret = ShiJianChuLiLogic.check_issue_info_in_list(issueObject)
        self.assertTrue(ret, '街道职能检查事件失败')
          
        #完成办理
        issueObject['processType'] = IssueProcessType.HUIFU
        issueObject['needAccept'] = True
        issueObject['jiaobanOrg'] = None
        issueObject['jiaobanUser'] = None
        issueObject['xiebanOrg'] = None
        issueObject['xiebanUser'] = None
        issueObject['processOpinion'] = '街道职能完成处理'

        ret = ShiJianChuLiLogic.process_issue(issueObject)
        self.assertTrue(ret, '职能部门完成办理失败')
        
        #使用街道职能登录
        MobileUtil.close_app()
        MobileUtil.start_app()
        loginDict['username'] = InitDefaultPara.userInit['DftJieDaoFuncUser']
        CommonModule.pingantong_login(loginDict)
        #进入事件处理模块
        CommonModule.enter_to_module(ModuleName.SHIJIANCHULI)
           
        #检查事件信息
        ret = ShiJianChuLiLogic.check_issue_info_in_list(issueObject)
        self.assertTrue(ret, '街道职能检查事件失败')
        
        #结案
        issueObject['processType'] = IssueProcessType.JIEAN
        issueObject['needAccept'] = True
        issueObject['jiaobanOrg'] = None
        issueObject['jiaobanUser'] = None
        issueObject['xiebanOrg'] = None
        issueObject['xiebanUser'] = None
        issueObject['processOpinion'] = '事件结案'

        ret = ShiJianChuLiLogic.process_issue(issueObject)
        self.assertTrue(ret, '职能部门结案失败')
        
        #使用街道账号登录
        MobileUtil.close_app()
        MobileUtil.start_app()
        loginDict['username'] = InitDefaultPara.userInit['DftJieDaoUser']
        CommonModule.pingantong_login(loginDict)
        #进入事件处理模块
        CommonModule.enter_to_module(ModuleName.SHIJIANCHULI)
        #进入我的已办结
        ShiJianChuLiLogic.select_issue_classify_menu(IssueClassifyMenu.WODEYIBANJIE)
        
        #检查事件信息
        issueObject['state'] = IssueProcessState.PROCESSED       
        ret = ShiJianChuLiLogic.check_issue_info_in_list(issueObject)
        self.assertTrue(ret, '街道账号在已办结查找失败')

        pass
    
    

    def tearDown(self):    
        pass

if  __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(PAT_ShiJianChuLi("testIssueAdd_001"))
    results = unittest.TextTestRunner().run(suite)
    pass
