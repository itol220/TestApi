# -*- coding:UTF-8 -*-
'''
Created on 2015-12-21

@author: N-133
'''
from __future__ import unicode_literals
from Interface.PingAnJianShe.SystemMgr import SystemMgrIntf
import unittest
from Interface.PingAnJianShe.MinQingRiZhi import MinQingRiZhiIntf,\
    MinQingRiZhiPara
from Interface.PingAnJianShe import MinQingRiZhi
import copy
from CONFIG import InitDefaultPara
from Interface.PingAnJianShe.Common import CommonIntf
from COMMON import CommonUtil, Time

class MinQingRiZhi(unittest.TestCase):

    def setUp(self):
        SystemMgrIntf.initEnv()
        MinQingRiZhiIntf.deleteAllMinQingRiZi()
        pass
    
#     新增工作问题咨询
    def testCase_01(self):
        """新增工作问题咨询"""
        testCase_01 = copy.deepcopy(MinQingRiZhiPara.addGongZuoWenTi) 
        testCase_01['issueNew.occurOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_01['eventOccurOrgSelector'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_01['issueNew.subject'] = '测试问题咨询%s'% CommonUtil.createRandomString()
        testCase_01['mode'] = 'add'
        testCase_01['issueNew.issueContent'] = '日志内容'
        testCase_01['issueNew.issueTypeName'] = '工作问题咨询'
        responseDict = MinQingRiZhiIntf.addGongZuoWenTi(GongZuoWenTiDict=testCase_01, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        
#      查看工作问题咨询
        param = copy.deepcopy(MinQingRiZhiPara.GongZuoWenTi)
        param['subject'] = testCase_01['issueNew.subject'] 
        ret = MinQingRiZhiIntf.checkGongZuoWenTiCompany(companyDict=param, OrgId=testCase_01['issueNew.occurOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')

        pass


    def testCase_02(self):
        """新增工作心得体会"""
#         新增工作心得体会
        testCase_02 = copy.deepcopy(MinQingRiZhiPara.addGongZuoXinDe) 
        testCase_02['issueNew.occurOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_02['eventOccurOrgSelector'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_02['issueNew.subject'] = '测试心得体会%s'% CommonUtil.createRandomString()
        testCase_02['mode'] = 'add'
        testCase_02['issueNew.issueContent'] = '日志内容'
        testCase_02['issueNew.issueTypeName'] = '工作心得体会'
        responseDict = MinQingRiZhiIntf.addGongZuoXinDe(GongZuoXinDeDict=testCase_02, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        
#      查看工作心得体会
        param = copy.deepcopy(MinQingRiZhiPara.GongZuoXinDe)
        param['subject'] = testCase_02['issueNew.subject'] 
        ret = MinQingRiZhiIntf.checkGongZuoXinDeCompany(companyDict=param, OrgId=testCase_02['issueNew.occurOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')

        pass  

    def testCase_03(self):
        """新增工作信息记录"""
#         新增工作信息记录
        testCase_03 = copy.deepcopy(MinQingRiZhiPara.addGongZuoXinXi) 
        testCase_03['issueNew.occurOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_03['eventOccurOrgSelector'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_03['issueNew.subject'] = '测试信息记录%s'% CommonUtil.createRandomString()
        testCase_03['mode'] = 'add'
        testCase_03['issueNew.issueContent'] = '日志内容'
        testCase_03['issueNew.issueTypeName'] = '工作信息记录'
        responseDict = MinQingRiZhiIntf.addGongZuoXinXi(GongZuoXinXiDict=testCase_03, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        
#      查看工作信息记录
        param = copy.deepcopy(MinQingRiZhiPara.GongZuoXinXi)
        param['subject'] = testCase_03['issueNew.subject'] 
        ret = MinQingRiZhiIntf.checkGongZuoXinXiCompany(companyDict=param, OrgId=testCase_03['issueNew.occurOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')        
               
        pass  

    def testCase_04(self):
        """查看下辖待办"""
#         新增下辖待办
        testCase_04 = copy.deepcopy(MinQingRiZhiPara.addGongZuoWenTi) 
        testCase_04['issueNew.occurOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_04['eventOccurOrgSelector'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_04['issueNew.subject'] = '测试问题咨询%s'% CommonUtil.createRandomString()
        testCase_04['mode'] = 'add'
        testCase_04['issueNew.issueContent'] = '日志内容'
        testCase_04['issueNew.issueTypeName'] = '工作问题咨询'
        responseDict = MinQingRiZhiIntf.addGongZuoWenTi(GongZuoWenTiDict=testCase_04, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        
#      查看下辖待办
        param = copy.deepcopy(MinQingRiZhiPara.GongZuoWenTi)
        param['subject'] = testCase_04['issueNew.subject'] 
        ret = MinQingRiZhiIntf.checkXiaXiaDaiBanCompany(companyDict=param, OrgId=testCase_04['issueNew.occurOrg.id'],username=InitDefaultPara.userInit['DftSheQuUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')
        
        pass  


    def testCase_05(self):
        """查看下辖已办"""
#         新增下辖已办
        testCase_05 = copy.deepcopy(MinQingRiZhiPara.addGongZuoXinDe) 
        testCase_05['issueNew.occurOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_05['eventOccurOrgSelector'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_05['issueNew.subject'] = '测试心得体会%s'% CommonUtil.createRandomString()
        testCase_05['mode'] = 'add'
        testCase_05['issueNew.issueContent'] = '日志内容'
        testCase_05['issueNew.issueTypeName'] = '工作心得体会'
        responseDict = MinQingRiZhiIntf.addGongZuoXinDe(GongZuoXinDeDict=testCase_05, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        
#      查看下辖已办
        param = copy.deepcopy(MinQingRiZhiPara.GongZuoXinDe)
        param['subject'] = testCase_05['issueNew.subject'] 
        ret = MinQingRiZhiIntf.checkXiaXiaYiBanCompany(companyDict=param, OrgId=testCase_05['issueNew.occurOrg.id'],username=InitDefaultPara.userInit['DftSheQuUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')        
        
        
        pass 

    def testCase_06(self):
        """新增点评"""
#         新增下辖待办
        testCase_04 = copy.deepcopy(MinQingRiZhiPara.addGongZuoWenTi) 
        testCase_04['issueNew.occurOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_04['eventOccurOrgSelector'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_04['issueNew.subject'] = '测试问题咨询%s'% CommonUtil.createRandomString()
        testCase_04['mode'] = 'add'
        testCase_04['issueNew.issueContent'] = '日志内容'
        testCase_04['issueNew.issueTypeName'] = '工作问题咨询'
        responseDict = MinQingRiZhiIntf.addGongZuoWenTi(GongZuoWenTiDict=testCase_04, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        
#      查看下辖待办
        param = copy.deepcopy(MinQingRiZhiPara.GongZuoWenTi)
        param['subject'] = testCase_04['issueNew.subject'] 
        ret = MinQingRiZhiIntf.checkXiaXiaDaiBanCompany(companyDict=param, OrgId=testCase_04['issueNew.occurOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')
        
#       新增点评
        testCase_06 = copy.deepcopy(MinQingRiZhiPara.adddianping) 
        testCase_06['issueLogNew.issue.id'] = CommonIntf.getDbQueryResult(dbCommand = "select i.id from issues i where i.subject='%s'" % (testCase_04['issueNew.subject']))
        testCase_06['issueLogNew.issueStep.id'] = CommonIntf.getDbQueryResult(dbCommand = "select i.currentstep from issues i where i.subject='%s'" % (testCase_04['issueNew.subject']))
        testCase_06['issueLogNew.content'] = '点评内容'
        responseDict = MinQingRiZhiIntf.adddianping(dianpingDict=testCase_06, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增点评失败')

#     查看点评
        param = copy.deepcopy(MinQingRiZhiPara.dianping)
        param['subject'] = testCase_04['issueNew.subject']
        ret = MinQingRiZhiIntf.checkdianpingCompany(companyDict=param, OrgId=testCase_04['issueNew.occurOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')
        
        pass  

    def testCase_07(self):
        """修改待办日志"""
#         新增待办日志
        testCase_04 = copy.deepcopy(MinQingRiZhiPara.addGongZuoWenTi) 
        testCase_04['issueNew.occurOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_04['eventOccurOrgSelector'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_04['issueNew.subject'] = '测试问题咨询%s'% CommonUtil.createRandomString()
        testCase_04['mode'] = 'add'
        testCase_04['issueNew.issueContent'] = '日志内容'
        testCase_04['issueNew.issueTypeName'] = '工作问题咨询'
        responseDict = MinQingRiZhiIntf.addGongZuoWenTi(GongZuoWenTiDict=testCase_04, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        
#      查看待办日志
        param = copy.deepcopy(MinQingRiZhiPara.GongZuoWenTi)
        param['subject'] = testCase_04['issueNew.subject'] 
        ret = MinQingRiZhiIntf.checkXiaXiaDaiBanCompany(companyDict=param, OrgId=testCase_04['issueNew.occurOrg.id'],username=InitDefaultPara.userInit['DftSheQuUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')

#    修改待办日志    
        testCase_07 = copy.deepcopy(MinQingRiZhiPara.editrizhi) 
        testCase_07['issueNew.id'] =  CommonIntf.getDbQueryResult(dbCommand = "select i.id from issues i where i.subject='%s'" % (testCase_04['issueNew.subject']))
        testCase_07['issueNew.occurOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_07['issueNew.subject'] = '测试日志标题%s'% CommonUtil.createRandomString()
        testCase_07['mode'] = 'edit'
        testCase_07['eventOccurOrgSelector'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_07['issueNew.issueContent'] = '日志内容'
        testCase_07['issueNew.issueTypeName'] = '工作问题咨询'
        responseDict = MinQingRiZhiIntf.modifyRiZhi(RiZhiObject=testCase_07, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改失败')

#      查看待办日志
        param = copy.deepcopy(MinQingRiZhiPara.GongZuoWenTi)
        param['subject'] = testCase_07['issueNew.subject'] 
        ret = MinQingRiZhiIntf.checkXiaXiaDaiBanCompany(companyDict=param, OrgId=testCase_07['issueNew.occurOrg.id'],username=InitDefaultPara.userInit['DftSheQuUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')        
        pass  

    def testCase_08(self):
        """修改已办日志"""
#         新增下辖已办
        testCase_05 = copy.deepcopy(MinQingRiZhiPara.addGongZuoXinDe) 
        testCase_05['issueNew.occurOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_05['eventOccurOrgSelector'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_05['issueNew.subject'] = '测试心得体会%s'% CommonUtil.createRandomString()
        testCase_05['mode'] = 'add'
        testCase_05['issueNew.issueContent'] = '日志内容'
        testCase_05['issueNew.issueTypeName'] = '工作心得体会'
        responseDict = MinQingRiZhiIntf.addGongZuoXinDe(GongZuoXinDeDict=testCase_05, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        
#      查看下辖已办
        param = copy.deepcopy(MinQingRiZhiPara.GongZuoXinDe)
        param['subject'] = testCase_05['issueNew.subject'] 
        ret = MinQingRiZhiIntf.checkXiaXiaYiBanCompany(companyDict=param, OrgId=testCase_05['issueNew.occurOrg.id'],username=InitDefaultPara.userInit['DftSheQuUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')        

#     修改已办日志
        testCase_08 = copy.deepcopy(MinQingRiZhiPara.editrizhi) 
        testCase_08['issueNew.id'] =  CommonIntf.getDbQueryResult(dbCommand = "select i.id from issues i where i.subject='%s'" % (testCase_05['issueNew.subject']))
        testCase_08['issueNew.occurOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_08['issueNew.subject'] = '测试日志标题%s'% CommonUtil.createRandomString()
        testCase_08['mode'] = 'edit'
        testCase_08['eventOccurOrgSelector'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_08['issueNew.issueContent'] = '日志内容'
        testCase_08['issueNew.issueTypeName'] = '工作心得体会'
        responseDict = MinQingRiZhiIntf.modifyRiZhi(RiZhiObject=testCase_08, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改失败')

#      查看已办日志
        param = copy.deepcopy(MinQingRiZhiPara.GongZuoWenTi)
        param['subject'] = testCase_08['issueNew.subject'] 
        ret = MinQingRiZhiIntf.checkXiaXiaYiBanCompany(companyDict=param, OrgId=testCase_08['issueNew.occurOrg.id'],username=InitDefaultPara.userInit['DftSheQuUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')            
        pass  


    def testCase_09(self):
        """查找待办日志"""
#         新增待办日志
        testCase_04 = copy.deepcopy(MinQingRiZhiPara.addGongZuoWenTi) 
        testCase_04['issueNew.occurOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_04['eventOccurOrgSelector'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_04['issueNew.subject'] = '测试问题咨询%s'% CommonUtil.createRandomString()
        testCase_04['mode'] = 'add'
        testCase_04['issueNew.issueContent'] = '日志内容'
        testCase_04['issueNew.issueTypeName'] = '工作问题咨询'
        responseDict = MinQingRiZhiIntf.addGongZuoWenTi(GongZuoWenTiDict=testCase_04, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')

        # 第一种情况:根据企业名称搜索 
        issueParamSearch = copy.deepcopy(MinQingRiZhiPara.addGongZuoWenTi) 
        issueParamSearch['issueNew.subject'] = testCase_04['issueNew.subject']
        ret = MinQingRiZhiIntf.chaxundaibanrizhi(issueParamSearch, username=InitDefaultPara.userInit['DftShiUser'], password='11111111');
        self.assertTrue(ret, '企业信息搜索失败')
        ret = MinQingRiZhiIntf.Companychaxundaibanrizhi(issueParamSearch, company='abcdabcd', username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertFalse(ret, '数据匹配失败')

        
        pass  
    
    
    def testCase_10(self):
        """日志结案"""
#         新增待办日志
        testCase_04 = copy.deepcopy(MinQingRiZhiPara.addGongZuoWenTi) 
        testCase_04['issueNew.occurOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_04['eventOccurOrgSelector'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_04['issueNew.subject'] = '测试问题咨询%s'% CommonUtil.createRandomString()
        testCase_04['mode'] = 'add'
        testCase_04['issueNew.issueContent'] = '日志内容'
        testCase_04['issueNew.issueTypeName'] = '工作问题咨询'
        responseDict = MinQingRiZhiIntf.addGongZuoWenTi(GongZuoWenTiDict=testCase_04, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
  
#        办理待办日志
        param = copy.deepcopy(MinQingRiZhiPara.banLi)
        param['mode'] = 'deal'
        param['issuesKeyId'] = CommonIntf.getDbQueryResult(dbCommand = "select i.id from issues i where i.subject='%s'" % (testCase_04['issueNew.subject']))
        param['keyId'] = CommonIntf.getDbQueryResult(dbCommand = "select i.id from issuesteps i where i.issue='%s'" % (param['issuesKeyId']))
        ret = MinQingRiZhiIntf.dealGongZuoWenTi(GongZuoWenTiDict=param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')         
 
        
#    办理状态为结案
        testCase_10 = copy.deepcopy(MinQingRiZhiPara.jiean) 
        testCase_10['operation.dealOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_10['operation.issue.id'] = param['issuesKeyId'] 
        testCase_10['keyId'] = param['keyId']
        testCase_10['operation.dealUserName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_10['operation.mobile'] = InitDefaultPara.userInit['DftWangGeUserSJ']
        testCase_10['dealCode'] = '31'
        testCase_10['dealTime'] = Time.getCurrentDate()
        testCase_10['transferToType'] = 'true'
        testCase_10['operation.content'] = testCase_04['issueNew.subject']
        responseDict = MinQingRiZhiIntf.addjiedan(jiedanDict=testCase_10, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '办理失败')

#      查看结案
        param = copy.deepcopy(MinQingRiZhiPara.GongZuoWenTi)
        param['subject'] = testCase_04['issueNew.subject'] 
        ret = MinQingRiZhiIntf.checkjieanCompany(companyDict=param, OrgId=testCase_04['issueNew.occurOrg.id'],username=InitDefaultPara.userInit['DftSheQuUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')            
        pass
    def testCase_11(self):
        """日志办理中"""
#         新增待办日志
        testCase_04 = copy.deepcopy(MinQingRiZhiPara.addGongZuoWenTi) 
        testCase_04['issueNew.occurOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_04['eventOccurOrgSelector'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_04['issueNew.subject'] = '测试问题咨询%s'% CommonUtil.createRandomString()
        testCase_04['mode'] = 'add'
        testCase_04['issueNew.issueContent'] = '日志内容'
        testCase_04['issueNew.issueTypeName'] = '工作问题咨询'
        responseDict = MinQingRiZhiIntf.addGongZuoWenTi(GongZuoWenTiDict=testCase_04, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
  
#        办理待办日志
        param = copy.deepcopy(MinQingRiZhiPara.banLi)
        param['mode'] = 'deal'
        param['issuesKeyId'] = CommonIntf.getDbQueryResult(dbCommand = "select i.id from issues i where i.subject='%s'" % (testCase_04['issueNew.subject']))
        param['keyId'] = CommonIntf.getDbQueryResult(dbCommand = "select i.id from issuesteps i where i.issue='%s'" % (param['issuesKeyId']))
        ret = MinQingRiZhiIntf.dealGongZuoWenTi(GongZuoWenTiDict=param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')         
 
        
#    办理状态为办理中
        testCase_11 = copy.deepcopy(MinQingRiZhiPara.banlizhong) 
        testCase_11['operation.dealOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_11['operation.issue.id'] = param['issuesKeyId'] 
        testCase_11['keyId'] = param['keyId']
        testCase_11['operation.dealUserName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_11['operation.mobile'] = InitDefaultPara.userInit['DftWangGeUserSJ']
        testCase_11['dealCode'] = '1'
        testCase_11['dealTime'] = Time.getCurrentDate()
        testCase_11['transferToType'] = 'true'
        testCase_11['operation.content'] = testCase_04['issueNew.subject']
        responseDict = MinQingRiZhiIntf.addbanlizhong(banlizhongDict=testCase_11, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '办理失败')

#      查看办理中
        param = copy.deepcopy(MinQingRiZhiPara.GongZuoWenTi)
        param['subject'] = testCase_04['issueNew.subject'] 
        ret = MinQingRiZhiIntf.checkbanlizhongCompany(companyDict=param, OrgId=testCase_04['issueNew.occurOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')   
        pass
    def testCase_12(self):
        """日志上报"""
#         新增待办日志
        testCase_04 = copy.deepcopy(MinQingRiZhiPara.addGongZuoWenTi) 
        testCase_04['issueNew.occurOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_04['eventOccurOrgSelector'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_04['issueNew.subject'] = '测试问题咨询%s'% CommonUtil.createRandomString()
        testCase_04['mode'] = 'add'
        testCase_04['issueNew.issueContent'] = '日志内容'
        testCase_04['issueNew.issueTypeName'] = '工作问题咨询'
        responseDict = MinQingRiZhiIntf.addGongZuoWenTi(GongZuoWenTiDict=testCase_04, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
  
#        办理待办日志
        param = copy.deepcopy(MinQingRiZhiPara.banLi)
        param['mode'] = 'deal'
        param['issuesKeyId'] = CommonIntf.getDbQueryResult(dbCommand = "select i.id from issues i where i.subject='%s'" % (testCase_04['issueNew.subject']))
        param['keyId'] = CommonIntf.getDbQueryResult(dbCommand = "select i.id from issuesteps i where i.issue='%s'" % (param['issuesKeyId']))
        ret = MinQingRiZhiIntf.dealGongZuoWenTi(GongZuoWenTiDict=param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')         
 
        
#    办理状态为上报
        testCase_12 = copy.deepcopy(MinQingRiZhiPara.shangbao) 
        testCase_12['operation.dealOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_12['operation.targeOrg.id'] = InitDefaultPara.orgInit['DftSheQuOrgId']
        testCase_12['operation.issue.id'] = param['issuesKeyId'] 
        testCase_12['keyId'] = param['keyId']
        testCase_12['operation.dealUserName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_12['operation.mobile'] = InitDefaultPara.userInit['DftWangGeUserSJ']
        testCase_12['dealCode'] = '41'
        testCase_12['themainOrgid'] = InitDefaultPara.orgInit['DftSheQuOrgId']
        testCase_12['transferToType'] = 'true'
        testCase_12['operation.content'] = testCase_04['issueNew.subject']
        responseDict = MinQingRiZhiIntf.addshangbao(shangbaoDict=testCase_12, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '办理失败')

#      查看上报
        param = copy.deepcopy(MinQingRiZhiPara.GongZuoWenTi)
        param['subject'] = testCase_04['issueNew.subject'] 
        ret = MinQingRiZhiIntf.checkshangbaoCompany(companyDict=param, OrgId=testCase_04['issueNew.occurOrg.id'],username=InitDefaultPara.userInit['DftSheQuUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')    
        pass
    def testCase_13(self):
        """日志交办"""
#         新增待办日志
        testCase_04 = copy.deepcopy(MinQingRiZhiPara.addGongZuoWenTi) 
        testCase_04['issueNew.occurOrg.id'] = InitDefaultPara.orgInit['DftSheQuOrgId']
        testCase_04['eventOccurOrgSelector'] = InitDefaultPara.orgInit['DftSheQuOrg']
        testCase_04['issueNew.subject'] = '测试问题咨询%s'% CommonUtil.createRandomString()
        testCase_04['mode'] = 'add'
        testCase_04['issueNew.issueContent'] = '日志内容'
        testCase_04['issueNew.issueTypeName'] = '工作问题咨询'
        responseDict = MinQingRiZhiIntf.addGongZuoWenTi(GongZuoWenTiDict=testCase_04, username=InitDefaultPara.userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
  
#        办理待办日志
        param = copy.deepcopy(MinQingRiZhiPara.banLi)
        param['mode'] = 'deal'
        param['issuesKeyId'] = CommonIntf.getDbQueryResult(dbCommand = "select i.id from issues i where i.subject='%s'" % (testCase_04['issueNew.subject']))
        param['keyId'] = CommonIntf.getDbQueryResult(dbCommand = "select i.id from issuesteps i where i.issue='%s'" % (param['issuesKeyId']))
        ret = MinQingRiZhiIntf.dealGongZuoWenTi(GongZuoWenTiDict=param, username=InitDefaultPara.userInit['DftSheQuUser'], password='11111111')         
        
#    办理状态为交办
        testCase_13 = copy.deepcopy(MinQingRiZhiPara.jiaoban) 
        testCase_13['operation.dealOrg.id'] = InitDefaultPara.orgInit['DftSheQuOrgId']
        testCase_13['operation.issue.id'] = param['issuesKeyId'] 
        testCase_13['keyId'] = param['keyId']
        testCase_13['operation.dealUserName'] = InitDefaultPara.userInit['DftSheQuUserXM']
        testCase_13['operation.mobile'] = InitDefaultPara.userInit['DftSheQuUserSJ']
        testCase_13['dealCode'] = '21'
        testCase_13['themainOrgid'] =str( InitDefaultPara.orgInit['DftWangGeOrgId'])+"-"+str(CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.username='%s'" % (InitDefaultPara.userInit['DftWangGeUser'])))
        testCase_13['transferToType'] = 'true'
        testCase_13['operation.content'] = testCase_04['issueNew.subject']
        responseDict = MinQingRiZhiIntf.addjiaoban(jiaobanDict=testCase_13, username=InitDefaultPara.userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '办理失败')

#      查看交办
        param = copy.deepcopy(MinQingRiZhiPara.GongZuoWenTi)
        param['subject'] = testCase_04['issueNew.subject'] 
        ret = MinQingRiZhiIntf.checkjiaobanCompany(companyDict=param, OrgId=testCase_04['issueNew.occurOrg.id'],username=InitDefaultPara.userInit['DftSheQuUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')      
        pass
    def tearDown(self):
        pass  

if __name__ == "__main__":
    suite = unittest.TestSuite()
#     suite.addTest(MinQingRiZhi("testCase_01"))
#     suite.addTest(MinQingRiZhi("testCase_02"))    
#     suite.addTest(MinQingRiZhi("testCase_03")) 
#     suite.addTest(MinQingRiZhi("testCase_04"))
#     suite.addTest(MinQingRiZhi("testCase_05"))    
#     suite.addTest(MinQingRiZhi("testCase_06"))   
#     suite.addTest(MinQingRiZhi("testCase_07")) 
#     suite.addTest(MinQingRiZhi("testCase_08"))      
#     suite.addTest(MinQingRiZhi("testCase_09"))          
#     suite.addTest(MinQingRiZhi("testCase_10"))      
#     suite.addTest(MinQingRiZhi("testCase_11"))     
#     suite.addTest(MinQingRiZhi("testCase_12")) 
    suite.addTest(MinQingRiZhi("testCase_13"))                       
    results = unittest.TextTestRunner().run(suite)
    pass