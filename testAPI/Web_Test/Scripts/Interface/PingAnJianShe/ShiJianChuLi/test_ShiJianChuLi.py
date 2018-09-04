# -*- coding:UTF-8 -*-
'''
Created on 2015-11-14

@author: N-286
'''
from __future__ import unicode_literals
from COMMON import Log, Time
from COMMON.CommonUtil import createRandomString
from COMMON.Time import getLinuxDateAndTime, moveTime, TimeMoveType, \
    TimeCalcType
from CONFIG import Global
from CONFIG.Define import LogLevel
from CONFIG.InitDefaultPara import orgInit, userInit
from Interface.PingAnJianShe import ShiJianChuLi
from Interface.PingAnJianShe.Common import CommonIntf
from Interface.PingAnJianShe.Common.CommonIntf import getDbQueryResult
from Interface.PingAnJianShe.RiChangBanGong.RiChangBanGongIntf import runJob
from Interface.PingAnJianShe.ShiJianChuLi import ShiJianChuLiPara, \
    ShiJianChuLiIntf
from Interface.PingAnJianShe.ShiJianChuLi.ShiJianChuLiIntf import \
    revocationIssue, checkRevocationIssue, addIssueOrg, dealIssue, checkSetHistory, \
    checkCancelHistoryIssue, checkHandleIssue, checkCompleteIssue, checkReportIssue, \
    checkReadIssue, checkAddOrg, checkAcceptIssue, checkBackIssue, setIssueByPass, \
    checkBypassIssue, checkAssignIssue, checkCommonHandelIssue, checkReplyIssue, \
    checkCooperateIssue, checkPublicCase, addIssue, evaluateIssue, \
    findMyTypeIssueBySub, addIssueCompleteLimitConfig, checkIssueCompleteLimitList, \
    applyIssueDelay, checkIssueDelayApply, setDelay, dlIssue, checkDlIssueList, \
    getExcelCellRowNum, getDownAllIssueTotalNum, searchDownAllIssue, \
    setScoreStandard, addTimeLimitStandard, setJobDelayTime, clearTable, \
    getRegradedPoint, exeDbQuery, checkSuperviseIssue, shiJianChuLiInitEnv
from Interface.PingAnJianShe.ShiJianChuLi.ShiJianChuLiPara import \
    issueEvaluateParam, dowonAllIssueSearchPara, superviseIssuesList
from Interface.PingAnJianShe.SystemMgr import SystemMgrIntf
import copy
import json
import time
import unittest
# from Interface.PingAnJianShe.ShiJianChuLi.test_ShiJianChuLiPara import \
#     xiaXiaDaiBanJianCha, issueCompleteLimitConfigParam

class Shijianchuli(unittest.TestCase):


    def setUp(self):
        SystemMgrIntf.initEnv()
        shiJianChuLiInitEnv() 
        pass
    
    '''
    @功能：我的事项-待办事项新增功能 
    @ chenhui 2015-11-25
    '''
    def testIssue_001(self):
        '''我的事项-待办事项新增功能'''
        #新增事件
        issueParam = copy.deepcopy(ShiJianChuLiPara.issueObject) 
        issueParam['issue.isDefault'] = 'true'
        issueParam['issue.subject'] = '事件主题'
        issueParam['selectOrgName']=orgInit['DftJieDaoOrg']
        issueParam['issue.occurOrg.id']=CommonIntf.getDbQueryResult("select id from organizations o where o.orgname='%s'"%issueParam['selectOrgName'])
        issueParam['issue.occurLocation'] = '发生地点'
#      issueParam['issue.occurDate'] = '2015-11-05'#日期返回为'2015-11-05'
        issueParam['issue.occurDate']=Time.getCurrentDate()
        issueParam['issueRelatedPeopleNames'] = '张三'
        issueParam['issueRelatedPeopleTelephones'] = '13588807624'
        issueParam['issue.relatePeopleCount'] = '3'
        issueParam['selectedTypes'] ='13'
        issueParam['issue.issueContent'] = '事件内容'
        issueParam['issue.sourceKind.id']=ShiJianChuLiPara.issueObject2['issue.sourceKind.id']
#        print 'sourceKind id=%s'%issueParam['issue.sourceKind.id']#'515'#515代表人工录入 1840代表巡检录入
        responseDict = ShiJianChuLiIntf.addIssue(issueDict=issueParam, username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(responseDict, '新增事件失败')
        #验证事件是否新增成功
        
        checkParam=copy.deepcopy(ShiJianChuLiPara.IssueCheckPara)
        checkParam['subject']=issueParam['issue.subject']
        checkParam['occurDateString']=issueParam['issue.occurDate']
        ret=ShiJianChuLiIntf.checkIssue(checkIssueDict=checkParam,username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(ret, '全部事项列表中没有找到对应的事件')
        Log.LogOutput(level=LogLevel.DEBUG, message='新增事件通过')
        
        #修改事件
#        print responseDict['issueId']
        issueParam2=copy.deepcopy(ShiJianChuLiPara.issueObject)
        issueParam2['issue.isDefault'] = 'true'
        issueParam2['issue.subject'] = '事件主题1'
        issueParam2['selectOrgName']=orgInit['DftJieDaoOrg']
        issueParam2['issue.occurLocation'] = '发生地点1'
#      issueParam['issue.occurDate'] = '2015-11-05'#日期返回为'2015-11-05'
        issueParam2['issue.occurDate']='2015-06-06'
        issueParam2['issueRelatedPeopleNames'] = '张三1'
        issueParam2['issueRelatedPeopleTelephones'] = '13333333333'
        issueParam2['issue.relatePeopleCount'] = '1'
        issueParam2['selectedTypes'] ='11'
        issueParam2['issue.issueContent'] = '事件内容1'
        issueParam2['issue.sourceKind.id']=ShiJianChuLiPara.issueObject2['issue.sourceKind.id']#515代表人工录入 1840代表巡检录入
        issueParam2['issue.id']=responseDict['issueId']
        issueParam2['issue.serialNumber']=responseDict['serialNumber']

        result=ShiJianChuLiIntf.updIssue(issueDict=issueParam2, username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(result, '更新事件失败')
        #查看事件并验证修改的事件是否正确
#        print 'result:%s '%result
        checkParam2=copy.deepcopy(ShiJianChuLiPara.IssueCheckPara)
        checkParam2['subject']=issueParam2['issue.subject']
        checkParam2['occurDateString']=issueParam2['issue.occurDate']
#        checkParam2['sourceKind']={'displaySeq':0,'internalId':0,'id':int(issueParam2['issue.sourceKind.id'])}
        result2=ShiJianChuLiIntf.viewIssue(issueDict=checkParam2, username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(result2, '查看事件失败')

        pass
    '''
    @功能：我的事项-待办事项新增必填项验证 bug:主要当事人姓名必填项验证错误
    @ chenhui 2015-11-25
    '''
    def testIssue_002(self):
        '''我的事项-待办事项新增必填项验证'''
        issueParam = copy.deepcopy(ShiJianChuLiPara.issueObject) 
        issueParam['issue.isDefault'] = 'true'
#必填项均为空        
        issueParam['selectOrgName']=orgInit['DftJieDaoOrg']
        issueParam['issue.occurOrg.id']=orgInit['DftJieDaoOrgId']
        response = ShiJianChuLiIntf.addIssue2(issueDict=issueParam)
        self.assertFalse(response.result,'验证信息不通过')
        Log.LogOutput(level=LogLevel.INFO, message='全部字段必填项验证通过!')
#      验证事件名称输入一个字符，其他必填项填写正确，返回结果
        issueParam['issue.subject'] = '事'
        issueParam['issue.occurDate']=Time.getCurrentDate()
        issueParam['issue.issueContent'] = '事件内容'
        issueParam['selectedTypes'] ='13'
        issueParam['issueRelatedPeopleNames'] = '张三'
        issueParam['issue.relatePeopleCount'] = '3'
        issueParam['selectOrgName']=orgInit['DftJieDaoOrg']
        issueParam['issue.occurOrg.id']=CommonIntf.getDbQueryResult("select id from organizations o where o.orgname='%s'"%issueParam['selectOrgName'])

        response = ShiJianChuLiIntf.addIssue2(issueDict=issueParam, username=userInit['DftJieDaoUser'], password='11111111')
        self.assertFalse(response.result,'验证信息不通过')
    #验证事件名称输入字符数超过51，其他必填项正确
        issueParam['issue.subject'] = '一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十1'
        response = ShiJianChuLiIntf.addIssue2(issueDict=issueParam, username=userInit['DftJieDaoUser'], password='11111111')
        self.assertFalse(response.result,'验证不通过')
        Log.LogOutput(level=LogLevel.INFO, message='事件名称字符数验证通过!')
        issueParam['issue.subject'] = '事件'
    #验证事件名称输入刚好50，其他必填项正确
        issueParam['issue.subject'] = '一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十'
        response = ShiJianChuLiIntf.addIssue2(issueDict=issueParam, username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(response.result,'验证不通过')
        Log.LogOutput(level=LogLevel.INFO, message='事件名称字符数验证通过!')
        issueParam['issue.subject'] = '事件'     
        
#验证发生时间为空，返回信息是否正确      
        issueParam['issue.occurDate']=''
        response = ShiJianChuLiIntf.addIssue2(issueDict=issueParam, username=userInit['DftJieDaoUser'], password='11111111')
        self.assertFalse(response.result,'验证不通过')
        Log.LogOutput(level=LogLevel.INFO, message='事件发生时间必填项验证通过!')
        issueParam['issue.occurDate']=Time.getCurrentDate()
#验证事件类型为空
        issueParam['selectedTypes'] =''
        response = ShiJianChuLiIntf.addIssue2(issueDict=issueParam, username=userInit['DftJieDaoUser'], password='11111111')
        self.assertFalse(response.result,'验证不通过')
        Log.LogOutput(level=LogLevel.INFO, message='事件类型必填项验证通过!')
        issueParam['selectedTypes'] ='2'
 
#验证主要当事人字段   
    #主要当事人输入为空
 
        issueParam['issueRelatedPeopleNames'] = ''
        response = ShiJianChuLiIntf.addIssue2(issueDict=issueParam, username=userInit['DftJieDaoUser'], password='11111111')
#         self.assertEqual(responseDict["message"],'姓名不能为空','主要当事人姓名必填项验证错误' )
        self.assertFalse(response.result,'验证不通过')
        Log.LogOutput(level=LogLevel.INFO, message='主要当事人姓名必填项验证通过!') 
    #主要当事人输入一个字符
        try:
            issueParam['issueRelatedPeopleNames'] = '一'
            response = ShiJianChuLiIntf.addIssue2(issueDict=issueParam, username=userInit['DftJieDaoUser'], password='11111111')
#            print responseDict
            self.assertFalse(response.result,'主要当事人输入一个字符验证不通过')
            Log.LogOutput(level=LogLevel.INFO, message='主要当事人姓名输入一个字符验证通过!')
        except Exception,e :
            Log.LogOutput(LogLevel.ERROR, '验证出现异常！异常信息:%s' % e)
             
#    主要当事人输入21个字符
        try:
            issueParam['issueRelatedPeopleNames'] =' 一二三四五六七八九十'
            response = ShiJianChuLiIntf.addIssue2(issueDict=issueParam, username=userInit['DftJieDaoUser'], password='11111111')
#            print responseDict
            self.assertFalse(response.result,'主要当事人姓名输入21个字符验证不通过')
            Log.LogOutput(level=LogLevel.INFO, message='主要当事人姓名输入21个字符验证通过!') 
        except Exception,e :
            Log.LogOutput(LogLevel.ERROR, '验证出现异常！异常信息:%s' % e)  
##验证事件内容字符数超过800,有bug
        try:
            issueParam['issueRelatedPeopleNames'] = '张三'
            issueParam['issue.occurDate']=Time.getCurrentDate()
            issueParam['issue.issueContent']='一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十1'
            response = ShiJianChuLiIntf.addIssue2(issueDict=issueParam, username=userInit['DftJieDaoUser'], password='11111111')
#            print responseDict
            self.assertFalse(response.result,'事件内容超过最大字符数验证不通过')
            Log.LogOutput(level=LogLevel.INFO, message='事件内容最大字符数验证通过!')
        except Exception,e :
            Log.LogOutput(LogLevel.ERROR, '验证出现异常！异常信息:%s' % e)    
                  
        pass
    
    '''
    @功能：我的事项-待办事项查询功能 
    @ chenhui 2015-11-25
    '''
    def testIssue_003(self):
        '''我的事项-待办事项查询功能 '''
#新增事件
        issueParam = copy.deepcopy(ShiJianChuLiPara.issueObject) 
        issueParam['issue.isDefault'] = 'true'
        issueParam['issue.subject'] = '事件主题'
        issueParam['selectOrgName']=orgInit['DftJieDaoOrg']
        issueParam['issue.occurOrg.id']=CommonIntf.getDbQueryResult("select id from organizations o where o.orgname='%s'"%issueParam['selectOrgName'])
        issueParam['issue.occurLocation'] = '发生地点'
        issueParam['issue.occurDate'] = '2015-11-05'#日期返回为'2015-11-05'
#        issueParam['issue.occurDate']=Time.getCurrentDate()
        issueParam['issueRelatedPeopleNames'] = '张三'
        issueParam['issueRelatedPeopleTelephones'] = '13588807624'
        issueParam['issue.relatePeopleCount'] = '3'
        issueParam['selectedTypes'] ='13'
        issueParam['issue.issueContent'] = '事件内容'
#        issueParam['issue.sourceKind.id']='515'#515代表人工录入 1840代表巡检录入
    
        responseDict = ShiJianChuLiIntf.addIssue(issueDict=issueParam, username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(responseDict, '新增事件失败')
#新增第二条数据           
        issueParam['issue.subject'] = '第二条事件'
        issueParam['issue.occurDate']=Time.getCurrentDate()
        issueParam['issue.occurLocation'] = '杭州天阙'
        responseDict = ShiJianChuLiIntf.addIssue(issueDict=issueParam, username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(responseDict, '新增事件失败') 
#查询已存在的事件标题        
        sIssuePara=copy.deepcopy(ShiJianChuLiPara.issureSearchPara)
        sIssuePara['searchIssueVo.subject']=issueParam['issue.subject']
        sIssuePara['searchIssueVo.targeOrgId']=orgInit['DftJieDaoOrgId']

        rs=ShiJianChuLiIntf.searchMyToDoIssue(sIssuePara, username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(rs,'单条件查询结果错误')
#查询不存在的事件标题
        sIssuePara['searchIssueVo.subject']='这个事件标题并不存在'
        rs=ShiJianChuLiIntf.searchMyToDoIssue(sIssuePara, username=userInit['DftJieDaoUser'], password='11111111')
        self.assertFalse(rs,'单条件查询结果错误')        
        Log.LogOutput(level=LogLevel.DEBUG, message='单条件查询结果正确')
#查询已存在的事件标题和发生地点两个条件              
        sIssuePara['searchIssueVo.inputFrom']=issueParam['issue.occurDate']
        sIssuePara['searchIssueVo.subject']=issueParam['issue.subject']
#         print sIssuePara['searchIssueVo.inputFrom']
        rs=ShiJianChuLiIntf.searchMyToDoIssue(sIssuePara, username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(rs,'多条件查询结果错误')
        Log.LogOutput(level=LogLevel.DEBUG, message='多条件查询结果正确')
#查询时事件标题存在，发生日期不存在
        sIssuePara['searchIssueVo.inputFrom']='2999-3-3'
#         print sIssuePara['searchIssueVo.inputFrom']
        rs=ShiJianChuLiIntf.searchMyToDoIssue(sIssuePara, username=userInit['DftJieDaoUser'], password='11111111')
        self.assertFalse(rs,'多条件查询结果错误') 
        pass
    '''
    @功能：我的事项-待办事项督办功能 
    @ chenhui 2015-11-26
    '''
    def testIssue_004(self):
        '''我的事项-待办事项督办功能 '''
#新增事件
        issueParam = copy.deepcopy(ShiJianChuLiPara.issueObject) 
        issueParam['issue.isDefault'] = 'true'
        issueParam['issue.subject'] = '事件主题'
        issueParam['selectOrgName']=orgInit['DftJieDaoOrg']
        issueParam['issue.occurOrg.id']=CommonIntf.getDbQueryResult("select id from organizations o where o.orgname='%s'"%issueParam['selectOrgName'])
        issueParam['issue.occurLocation'] = '发生地点'
#        issueParam['issue.occurDate'] = '2015-11-05'#日期返回为'2015-11-05'
        issueParam['issue.occurDate']=Time.getCurrentDate()
        issueParam['issueRelatedPeopleNames'] = '张三'
        issueParam['issueRelatedPeopleTelephones'] = '13588807624'
        issueParam['issue.relatePeopleCount'] = '3'
        issueParam['selectedTypes'] ='13'
        issueParam['issue.issueContent'] = '事件内容'
#        issueParam['issue.sourceKind.id']='515'#515代表人工录入 1840代表巡检录入      
        rs=ShiJianChuLiIntf.addIssue(issueDict=issueParam, username=userInit['DftJieDaoUser'], password='11111111')
        
        sIssuePara=copy.deepcopy(ShiJianChuLiPara.superviseIssue)
        
        sIssuePara['operation.dealOrg.id']=orgInit['DftJieDaoOrgId']
        sIssuePara['operation.issue.id']=rs['issueId']
        sIssuePara['keyId']=CommonIntf.getDbQueryResult("select currentstep from issues i where i.id='%s'"%sIssuePara['operation.issue.id'])

        sIssuePara['dealCode']='81'#普通督办
        sIssuePara['operation.dealUserName']=userInit['DftJieDaoUserXM']
        sIssuePara['operation.mobile']=userInit['DftJieDaoUserSJ']
        sIssuePara['operation.content']='督办内容'
        result=ShiJianChuLiIntf.superviseIssue(issueDict=sIssuePara,username=userInit['DftJieDaoUser'],password='11111111')
        self.assertTrue(result,'普通督办验证失败')
        #再次普通督办          
        result=ShiJianChuLiIntf.superviseIssue(issueDict=sIssuePara,username=userInit['DftJieDaoUser'],password='11111111')
        self.assertFalse(result,'再次普通督办验证失败')
        Log.LogOutput(message="再次普通督办验证通过")
        
        sIssuePara['dealCode']='83'#黄牌督办
        result=ShiJianChuLiIntf.superviseIssue(issueDict=sIssuePara,username=userInit['DftJieDaoUser'],password='11111111')
        self.assertTrue(result,'黄牌督办验证失败')
        
        sIssuePara['dealCode']='86'#红牌督办
        result=ShiJianChuLiIntf.superviseIssue(issueDict=sIssuePara,username=userInit['DftJieDaoUser'],password='11111111')
        self.assertTrue(result,'红牌督办验证失败')
        
        sIssuePara['dealCode']='83'#红牌督办后接着黄牌督办
        result=ShiJianChuLiIntf.superviseIssue(issueDict=sIssuePara,username=userInit['DftJieDaoUser'],password='11111111')
        self.assertFalse(result,'黄牌督办验证失败') 
        Log.LogOutput(message="红牌督办后接着黄牌督办验证通过")
        
        sIssuePara['dealCode']='88'#取消督办
        result=ShiJianChuLiIntf.superviseIssue(issueDict=sIssuePara,username=userInit['DftJieDaoUser'],password='11111111')
        self.assertTrue(result,'取消督办验证失败')
        #再次取消督办，程序出现bug        
#         sIssuePara['dealCode']='88'#取消督办
#         result=ShiJianChuLiIntf.superviseIssue(issueDict=sIssuePara,username=userInit['DftJieDaoUser'],password='11111111')
#         self.assertFalse(result,'取消督办验证失败')
        pass
    '''
    @功能：我的事项-待办事项加急
    @ chenhui 2015-11-26
    '''   
    def testIssue_005(self):
        '''我的事项-待办事项加急'''
        issueParam = copy.deepcopy(ShiJianChuLiPara.issueObject) 
        issueParam['issue.isDefault'] = 'true'
        issueParam['issue.subject'] = '事件主题'
        issueParam['selectOrgName']=orgInit['DftJieDaoOrg']
        issueParam['issue.occurOrg.id']=CommonIntf.getDbQueryResult("select id from organizations o where o.orgname='%s'"%issueParam['selectOrgName'])
        issueParam['issue.occurLocation'] = '发生地点'
#        issueParam['issue.occurDate'] = '2015-11-05'#日期返回为'2015-11-05'
        issueParam['issue.occurDate']=Time.getCurrentDate()
        issueParam['issueRelatedPeopleNames'] = '张三'
        issueParam['issueRelatedPeopleTelephones'] = '13588807624'
        issueParam['issue.relatePeopleCount'] = '3'
        issueParam['selectedTypes'] ='13'
        issueParam['issue.issueContent'] = '事件内容'
#        issueParam['issue.sourceKind.id']='515'#515代表人工录入 1840代表巡检录入      
        rs=ShiJianChuLiIntf.addIssue(issueDict=issueParam, username=userInit['DftJieDaoUser'], password='11111111')
#         print rs
        sIssuePara=copy.deepcopy(ShiJianChuLiPara.superviseIssue)     
        sIssuePara['operation.dealOrg.id']=orgInit['DftJieDaoOrgId']
        sIssuePara['operation.issue.id']=rs['issueId']
        sIssuePara['keyId']=CommonIntf.getDbQueryResult("select currentstep from issues i where i.id='%s'"%sIssuePara['operation.issue.id'])

        sIssuePara['dealCode']='1001'#加急
        sIssuePara['operation.dealUserName']=userInit['DftJieDaoUserXM']
        sIssuePara['operation.mobile']=userInit['DftJieDaoUserSJ']
        sIssuePara['operation.content']='加急内容'
        result=ShiJianChuLiIntf.urgentIssue(issueDict=sIssuePara,username=userInit['DftJieDaoUser'],password='11111111')
        self.assertTrue(result,'事件加急验证失败')
#对已经加急的事件继续加急
        result=ShiJianChuLiIntf.urgentIssue(issueDict=sIssuePara,username=userInit['DftJieDaoUser'],password='11111111')
        self.assertFalse(result,'事件加急验证失败')
        
        sIssuePara['dealCode']='1011'#取消加急
        result=ShiJianChuLiIntf.urgentIssue(issueDict=sIssuePara,username=userInit['DftJieDaoUser'],password='11111111')
        self.assertTrue(result,'事件加急验证失败')
#对已经取消加急的事件再次取消加急        
        result=ShiJianChuLiIntf.urgentIssue(issueDict=sIssuePara,username=userInit['DftJieDaoUser'],password='11111111')
        self.assertFalse(result,'事件加急验证失败')
        pass
    
    '''
    @功能：我的事项-待办事项领导批示
    @ chenhui 2015-11-26
    '''  
    def testIssue_006(self):
        '''我的事项-待办事项领导批示'''
        issueParam = copy.deepcopy(ShiJianChuLiPara.issueObject) 
        issueParam['issue.isDefault'] = 'true'
        issueParam['issue.subject'] = '事件主题'
        issueParam['selectOrgName']=orgInit['DftJieDaoOrg']
        issueParam['issue.occurOrg.id']=CommonIntf.getDbQueryResult("select id from organizations o where o.orgname='%s'"%issueParam['selectOrgName'])
        issueParam['issue.occurLocation'] = '发生地点'
#        issueParam['issue.occurDate'] = '2015-11-05'#日期返回为'2015-11-05'
        issueParam['issue.occurDate']=Time.getCurrentDate()
        issueParam['issueRelatedPeopleNames'] = '张三'
        issueParam['issueRelatedPeopleTelephones'] = '13588807624'
        issueParam['issue.relatePeopleCount'] = '3'
        issueParam['selectedTypes'] ='13'
        issueParam['issue.issueContent'] = '事件内容'
#        issueParam['issue.sourceKind.id']='515'#515代表人工录入 1840代表巡检录入      
        rs=ShiJianChuLiIntf.addIssue(issueDict=issueParam, username=userInit['DftJieDaoUser'], password='11111111')
        
        sIssuePara=copy.deepcopy(ShiJianChuLiPara.superviseIssue)     
        sIssuePara['operation.dealOrg.id']=orgInit['DftJieDaoOrgId']
        sIssuePara['operation.issue.id']=rs['issueId']
        sIssuePara['keyId']=CommonIntf.getDbQueryResult("select currentstep from issues i where i.id='%s'"%sIssuePara['operation.issue.id'])

        sIssuePara['dealCode']='51'#批示
        sIssuePara['operation.dealUserName']=userInit['DftJieDaoUserXM']
        sIssuePara['operation.mobile']=userInit['DftJieDaoUserSJ']
        sIssuePara['operation.content']='批示内容'
        result=ShiJianChuLiIntf.dealIssue(issueDict=sIssuePara,username=userInit['DftJieDaoUser'],password='11111111')
        self.assertTrue(result.result, '领导批示失败！')
        Log.LogOutput(message="领导批示验证通过")
#验证批示必填项批示内容为空
        sIssuePara['operation.content']=''
        result=ShiJianChuLiIntf.dealIssue(issueDict=sIssuePara,username=userInit['DftJieDaoUser'],password='11111111')
        self.assertFalse(result.result, '领导批示内容必填验证失败！')
        Log.LogOutput(message="领导批示内容必填验证通过")
# #验证必填项输入超过1000个字符
#         sIssuePara['operation.content']='一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十1'
#         result=ShiJianChuLiIntf.dealIssue(issueDict=sIssuePara,username=userInit['DftJieDaoUser'],password='11111111')
#         print result.text
#         str='\"批注内容最多1000个字!\\n\"'
# #        print str
#         self.assertEqual(result.text,str, '领导批示内容输入字符数验证失败！')
#         Log.LogOutput(message="领导批示内容输入字符数超过边界值验证通过")
#刚好输入1000个字符
        sIssuePara['operation.content']='一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十'
        result=ShiJianChuLiIntf.dealIssue(issueDict=sIssuePara,username=userInit['DftJieDaoUser'],password='11111111')        
        self.assertTrue(result.result,'边界值输入字符失败！')
        Log.LogOutput(message="领导批示内容边界值输入验证通过")
        pass
    '''
    @功能：我的事项-待办事项历史遗留
    @ chenhui 2015-11-26
    '''  
    def testIssue_007(self):
        '''我的事项-待办事项历史遗留'''
        issueParam = copy.deepcopy(ShiJianChuLiPara.issueObject2)     
        rs=ShiJianChuLiIntf.addIssue(issueDict=issueParam, username=userInit['DftJieDaoUser'], password='11111111')
        #历史遗留参数
        sIssuePara={'keyId':None,'dealCode':None}
        sIssuePara['keyId']=rs['issueStepId']
        sIssuePara['dealCode']='1101'#历史遗留
#      设置检查参数
        checkPara=copy.deepcopy(ShiJianChuLiPara.xiaXiaDaiBanJianCha)
        checkPara['issueId']=rs['issueId']
        checkPara['dealState']=120
        checkPara['subject']=issueParam['issue.subject']
        #设置历史遗留
        result=dealIssue(issueDict=sIssuePara)
        self.assertTrue(result.result ,'设置历史遗留操作失败！')
        Log.LogOutput(message='设置历史遗留验证中')
        result=checkSetHistory(checkParam=checkPara)
        
        self.assertTrue(result, '设置历史遗留失败！')
        Log.LogOutput(message="设置历史遗留验证通过")
        
        #取消历史遗留
        Log.LogOutput(message='正在进行取消历史遗留验证...')
        sIssuePara2={'keyId':rs['issueStepId'],'dealCode':'1111'}
        result2=dealIssue(issueDict=sIssuePara2)
        self.assertTrue(result2, '取消历史遗留失败！')
        Log.LogOutput(message='取消历史遗留成功，正在验证取消功能')
        result3=checkCancelHistoryIssue(checkParam=checkPara)
        
        self.assertTrue(result3, '取消历史遗留失败！')
        Log.LogOutput(message="取消历史遗留验证通过")
        
        pass
    '''
    @功能：我的事项-待办事项置顶
    @ chenhui 2015-11-27
    '''      
    def testIssue_008(self):
        '''我的事项-待办事项置顶'''
        issueParam = copy.deepcopy(ShiJianChuLiPara.issueObject2)     
        rs=ShiJianChuLiIntf.addIssue(issueDict=issueParam, username=userInit['DftJieDaoUser'], password='11111111')
        #置顶参数   
        para={
        'topIssue.issueId':rs['issueId'],
        'topIssue.issueTag':'1'
        }
        result=ShiJianChuLiIntf.topIssue(issueDict=para, username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(result.result, '置顶失败！')
        Log.LogOutput(message="置顶功能验证通过")
        result=ShiJianChuLiIntf.topIssue(issueDict=para, username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(result.result, '取消置顶失败！')
        Log.LogOutput(message="取消置顶功能验证通过")
        pass
    '''
    @功能：我的事项-事件办理中、结案功能
    @ chenhui 2015-11-27
    '''     
    def testIssue_009(self):
        '''我的事项-事件办理中、结案功能'''
        #新增事件
        issueParam = copy.deepcopy(ShiJianChuLiPara.issueObject2)     
        rs=ShiJianChuLiIntf.addIssue(issueDict=issueParam, username=userInit['DftJieDaoUser'], password='11111111')
        #设置办理中参数
        sIssuePara=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)        
        sIssuePara['operation.dealOrg.id']=orgInit['DftJieDaoOrgId']
        sIssuePara['operation.issue.id']=rs['issueId']
        sIssuePara['keyId']=rs['issueStepId']      
        sIssuePara['operation.dealUserName']=userInit['DftJieDaoUserXM']
        sIssuePara['operation.mobile']=userInit['DftJieDaoUserSJ']
        sIssuePara['operation.content']='事件处理'      
        sIssuePara['dealCode']='1'#办理中
        #设置检查参数
        checkPara=copy.deepcopy(ShiJianChuLiPara.xiaXiaDaiBanJianCha)
        checkPara['issueId']=rs['issueId']
        checkPara['dealState']=120#rsDict['dealState']
        checkPara['subject']=issueParam['issue.subject']
        #处理事件
        result=dealIssue(issueDict=sIssuePara)
        self.assertTrue(result.result, '事件操作失败!')
        Log.LogOutput(message='事件操作结束，正在验证中')
        #验证处理操作
        result1=checkHandleIssue(checkParam=checkPara,issueDict=sIssuePara)
        self.assertTrue(result1,'事件“办理中”失败！')
        
        sIssuePara['dealCode']='31'#结案
        sIssuePara['dealTime']=Time.getCurrentDate()
        sIssuePara['transferToType']='true'
        checkPara['dealState']=1000
        
        #结案
        result=dealIssue(issueDict=sIssuePara)
        self.assertTrue(result.result, '事件操作失败!')
        #验证结案功能
        Log.LogOutput(message='事件操作结束，正在验证中')
        result2=checkCompleteIssue(checkParam=checkPara,issueDict=sIssuePara)
        self.assertTrue(result2,'事件“结案”失败！')
        pass
    
    '''
    @功能：我的事项-事件上报
    @ chenhui 2015-11-30
    '''     
    def testIssue_010(self):
        '''我的事项-事件上报'''
        #新增事件
        issueParam = copy.deepcopy(ShiJianChuLiPara.issueObject2)   
        rs=ShiJianChuLiIntf.addIssue(issueDict=issueParam, username=userInit['DftJieDaoUser'], password='11111111')
        
#街道上报给区        
        sIssuePara=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)        
        sIssuePara['operation.dealOrg.id']=orgInit['DftJieDaoOrgId']
        sIssuePara['operation.issue.id']=rs['issueId']
        sIssuePara['keyId']=rs['issueStepId']      
        sIssuePara['operation.dealUserName']=userInit['DftJieDaoUserXM']
        sIssuePara['operation.mobile']=userInit['DftJieDaoUserSJ']
        sIssuePara['operation.content']='上报事件'
        sIssuePara['operation.targeOrg.id']=orgInit['DftQuOrgId']
        sIssuePara['themainOrgid']=orgInit['DftQuOrgId']        
        sIssuePara['dealCode']='41'#上报
        #设置检查参数
        checkPara=copy.deepcopy(ShiJianChuLiPara.xiaXiaDaiBanJianCha)
        checkPara['issueId']=rs['issueId']
        checkPara['dealState']=110
        checkPara['subject']=issueParam['issue.subject']
        #街道上报事件
        Log.LogOutput(message='街道上报事件中')
        result=dealIssue(issueDict=sIssuePara)
        self.assertTrue(result.result,'事件“普通上报”失败！')
        Log.LogOutput(message='普通上报验证中...')
        #验证普通上报功能
        r=checkReportIssue(checkParam=checkPara,issueDict=sIssuePara)
        self.assertTrue(r, '普通上报验证失败')
#清空数据
        Log.LogOutput(message='清空数据')        
        ShiJianChuLi.ShiJianChuLiIntf.deleteAllIssues()
# #上报并抄告
# #重新新增
        rs=ShiJianChuLiIntf.addIssue(issueDict=issueParam, username=userInit['DftJieDaoUser'], password='11111111')
        #重新定义参数，rs相关参数需要更新
        sIssuePara['operation.issue.id']=rs['issueId']
        sIssuePara['keyId']=rs['issueStepId']  
        checkPara['issueId']=rs['issueId']
        sIssuePara['tellOrgIds']=orgInit['DftQuFuncOrgId']#('',orgInit['DftQuFuncOrgId'])
        Log.LogOutput(message='街道上报并抄告事件中')
        #上报并抄告
        result2=dealIssue(issueDict=sIssuePara)
        self.assertTrue(result2.result,'事件“上报并抄告”失败！')
        Log.LogOutput(message='上报并抄告验证中...')
        #验证上报并抄告功能
        r2=checkReportIssue(checkParam=checkPara,issueDict=sIssuePara)
        self.assertTrue(r2, '上报并抄告验证失败')
        pass  
    
    
    '''
    @功能：我的事项-事件阅读
    @ chenhui 2015-11-30
    '''         
    def testIssue_011(self):
        '''我的事项-事件阅读 '''
        issueParam = copy.deepcopy(ShiJianChuLiPara.issueObject2) 
        rs=ShiJianChuLiIntf.addIssue(issueDict=issueParam, username=userInit['DftJieDaoUser'], password='11111111')
#        设置阅读参数
        sIssuePara=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)        
        sIssuePara['operation.dealOrg.id']=orgInit['DftJieDaoOrgId']
        sIssuePara['operation.issue.id']=rs['issueId']
        sIssuePara['keyId']=rs['issueStepId']      
        sIssuePara['operation.dealUserName']=userInit['DftJieDaoUserXM']
        sIssuePara['operation.mobile']=userInit['DftJieDaoUserSJ']      
        sIssuePara['dealCode']='71'#阅读

#       新增事件直接阅读
        Log.LogOutput(message='正在验证新增事件后直接阅读...')
        result=dealIssue(issueDict=sIssuePara)
        Log.LogOutput(level=LogLevel.DEBUG, message=result.text)
        self.assertFalse(result.result,'事件新增直接“阅读”验证失败！')
        Log.LogOutput(message='事件新增直接阅读验证成功')
#         上报抄告并阅读
        Log.LogOutput(message='正在上报事件并抄告区职能部门...')
        sIssuePara['operation.content']='上报事件'
        sIssuePara['operation.targeOrg.id']=orgInit['DftQuOrgId']
        sIssuePara['themainOrgid']=orgInit['DftQuOrgId']  
        sIssuePara['tellOrgIds']=orgInit['DftQuFuncOrgId']      
        sIssuePara['dealCode']='41'#上报
        result=dealIssue(issueDict=sIssuePara)
#上报后，issueStepSd+1
        self.assertTrue(result.result,'事件“上报并抄告”失败！')
        Log.LogOutput(message='上报并抄告成功，即将验证阅读功能...')
#         阅读
#阅读时，keyId（issueStepId再加1）
        sIssuePara2={
                     'operation.dealOrg.id':orgInit['DftQuFuncOrgId'],
                     'operation.issue.id':sIssuePara['operation.issue.id'],
                     'operation.dealUserName':userInit['DftQuFuncUserXM'],
                     'operation.mobile':userInit['DftQuFuncUserSJ'],
                     'dealCode':'71',
                     'keyId':sIssuePara['keyId']+2
                     }
#         设置检查参数
        checkPara=copy.deepcopy(ShiJianChuLiPara.xiaXiaDaiBanJianCha)
        checkPara['issueId']=rs['issueId']
        checkPara['subject']=issueParam['issue.subject']
        checkPara['dealState']=500
        checkPara['keyId']=orgInit['DftQuFuncOrgId']
        #阅读事件
        Log.LogOutput(message='阅读事件')
        r=dealIssue(issueDict=sIssuePara2,username=userInit['DftQuFuncUser'])
        self.assertTrue(r.result, '阅读失败')
        #验证阅读
        result=checkReadIssue(checkParam=checkPara,issueDict=sIssuePara2,username=userInit['DftQuFuncUser'])
        self.assertTrue(result,'事件抄告后阅读失败！')
        Log.LogOutput(message='上报并抄告后阅读验证成功')
        
        pass    
    
    '''
    @功能：我的事项-事件受理
    @ chenhui 2015-12-1
    '''     
    
    def testIssue_012(self):
        '''我的事项-事件受理'''
        #新增事件         
        issueParam = copy.deepcopy(ShiJianChuLiPara.issueObject2) 
        rs=ShiJianChuLiIntf.addIssue(issueDict=issueParam, username=userInit['DftJieDaoUser'], password='11111111')
        #街道上报给区,设置上报参数        
        sIssuePara=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)        
        sIssuePara['operation.dealOrg.id']=orgInit['DftJieDaoOrgId']
        sIssuePara['operation.issue.id']=rs['issueId']
        sIssuePara['keyId']=rs['issueStepId']      
        sIssuePara['operation.dealUserName']=userInit['DftJieDaoUserXM']
        sIssuePara['operation.mobile']=userInit['DftJieDaoUserSJ']
        sIssuePara['operation.content']='上报事件'
        sIssuePara['operation.targeOrg.id']=orgInit['DftQuOrgId']
        sIssuePara['themainOrgid']=orgInit['DftQuOrgId']
        #上报        
        sIssuePara['dealCode']='41'
        #设置检查参数
        checkPara=copy.deepcopy(ShiJianChuLiPara.xiaXiaDaiBanJianCha)
        checkPara['issueId']=rs['issueId']
        checkPara['dealState']=110
        checkPara['subject']=issueParam['issue.subject']
        #上报事件
        Log.LogOutput(message='上报事件')
        result=dealIssue(issueDict=sIssuePara)
        self.assertTrue(result.result, '上报失败！')

        Log.LogOutput(message='事件上报成功！')
        
        #受理参数设置
        sIssuePara2={
                     'operation.dealOrg.id':orgInit['DftQuOrgId'],
                     'operation.issue.id':sIssuePara['operation.issue.id'],
                     'operation.dealUserName':userInit['DftQuUserXM'],
                     'operation.mobile':userInit['DftQuUserSJ'],
                     'dealCode':'61',
                     'keyId':sIssuePara['keyId']+1
                     }
        checkPara['dealState']=120
        result2=dealIssue(issueDict=sIssuePara2,username=userInit['DftQuUser'])
        self.assertTrue(result2.result,'事件上报后受理失败！')
#      验证上报受理功能
        r2=checkAcceptIssue(checkParam=checkPara,issueDict=sIssuePara2,username=userInit['DftQuUser'])
        self.assertTrue(r2, '上报受理失败')
        Log.LogOutput(message='上报并受理验证成功')      
        pass
    
    '''
    @功能：我的事项-事件回退
    @ chenhui 2015-12-1
    '''         
    def testIssue_013(self):
        '''我的事项，事件回退'''
        #新增事件         
        issueParam = copy.deepcopy(ShiJianChuLiPara.issueObject2) 
        rs=ShiJianChuLiIntf.addIssue(issueDict=issueParam, username=userInit['DftJieDaoUser'], password='11111111')
        #街道上报给区,设置上报参数        
        sIssuePara=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)        
        sIssuePara['operation.dealOrg.id']=orgInit['DftJieDaoOrgId']
        sIssuePara['operation.issue.id']=rs['issueId']
        sIssuePara['keyId']=rs['issueStepId']      
        sIssuePara['operation.dealUserName']=userInit['DftJieDaoUserXM']
        sIssuePara['operation.mobile']=userInit['DftJieDaoUserSJ']
        sIssuePara['operation.content']='上报事件'
        sIssuePara['operation.targeOrg.id']=orgInit['DftQuOrgId']
        sIssuePara['themainOrgid']=orgInit['DftQuOrgId']
        #上报        
        sIssuePara['dealCode']='41'
        rs2=ShiJianChuLiIntf.dealIssue(issueDict=sIssuePara,username=userInit['DftJieDaoUser'],password='11111111')
        if rs2.result is True:
#            print rs2.text
            Log.LogOutput(message='上报事件成功')
        
    #受理
        Log.LogOutput(message='事件正在受理中...')     
        sIssuePara2={
                     'operation.dealOrg.id':orgInit['DftQuOrgId'],
                     'operation.issue.id':sIssuePara['operation.issue.id'],
                     'operation.dealUserName':userInit['DftQuUserXM'],
                     'operation.mobile':userInit['DftQuUserSJ'],
                     'dealCode':'61',
                     'keyId':sIssuePara['keyId']+1
                     }
        result=ShiJianChuLiIntf.dealIssue(issueDict=sIssuePara2,username=userInit['DftQuUser'],password='11111111')
        self.assertTrue(result.result, '事件受理失败！')
        #设置检查参数   
        checkPara=copy.deepcopy(ShiJianChuLiPara.xiaXiaDaiBanJianCha)
        checkPara['issueId']=rs['issueId']
        checkPara['dealState']=110
        checkPara['subject']=issueParam['issue.subject']   
        #设置回退参数
        sIssuePara3=copy.deepcopy(ShiJianChuLiPara.dealIssuePara) 
        sIssuePara3['operation.dealOrg.id']=orgInit['DftQuOrgId']
        sIssuePara3['operation.issue.id']=sIssuePara2['operation.issue.id']
        sIssuePara3['keyId']=sIssuePara2['keyId']
        sIssuePara3['operation.dealUserName']=userInit['DftQuUserXM'],
        sIssuePara3['operation.mobile']=userInit['DftQuUserSJ']
        sIssuePara3['dealCode']='200'
        sIssuePara3['operation.content']='回退事件'
        #回退操作
        result3=dealIssue(issueDict=sIssuePara3,username=userInit['DftQuUser'])
        self.assertTrue(result3, '事件回退失败！')
        #验证回退功能
        rs2=checkBackIssue(issueDict=sIssuePara3, checkParam=checkPara, username=userInit['DftQuUser'], password='11111111')
        self.assertTrue(rs2, '事件回退功能验证失败')
        Log.LogOutput(message='事件回退功能验证通过')    
        pass  
    
    '''
    @功能：我的事项-越级上报
    @ chenhui 2015-12-2
    '''     
    def testIssue_014(self):
        '''我的事项，越级上报'''
        if Global.simulationEnvironment is False:
            try:
                #新增事件
                issueParam = copy.deepcopy(ShiJianChuLiPara.issueObject2) 
                rs=ShiJianChuLiIntf.addIssue(issueDict=issueParam, username=userInit['DftWangGeUser'], password='11111111')
                #网格上报给街道,设置上报参数        
                sIssuePara=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)        
                sIssuePara['operation.dealOrg.id']=orgInit['DftJieDaoOrgId']
                sIssuePara['operation.issue.id']=rs['issueId']
                sIssuePara['keyId']=rs['issueStepId']      
                sIssuePara['operation.dealUserName']=userInit['DftWangGeUserXM']
                sIssuePara['operation.mobile']=userInit['DftWangGeUserSJ']
                sIssuePara['operation.content']='上报事件'
                sIssuePara['operation.targeOrg.id']=orgInit['DftJieDaoOrgId']
                sIssuePara['themainOrgid']=orgInit['DftJieDaoOrgId']
                #不设置，直接上报        
                byPassPara={'issueBypassList[0].orgId':orgInit['DftWangGeOrgId'],'issueBypassList[0].isBypass':False}
                res=ShiJianChuLiIntf.setIssueByPass(issueDict=byPassPara)       
                sIssuePara['dealCode']='41'        
                response=dealIssue(issueDict=sIssuePara, username=userInit['DftWangGeUser'], password='11111111')
                Log.LogOutput(LogLevel.DEBUG, response.text)
                self.assertFalse(response.result,'越级上报出错验证失败')
                Log.LogOutput(message='事件没设置上报权限情况下，越级上报出错验证成功')
            
            #系统管理中设置越级上报，网格可以越级上报给街道
            #以下代码可能存在异常，导致恢复禁止越级上报的初始设置没有执行，故捕捉异常
                byPassPara={'issueBypassList[0].orgId':orgInit['DftWangGeOrgId'],'issueBypassList[0].isBypass':True}
                res=setIssueByPass(issueDict=byPassPara)
                self.assertTrue(res, '越级上报设置成功')
                #设置好越级上报之后，再次越级上报
                response=dealIssue(issueDict=sIssuePara, username=userInit['DftWangGeUser'], password='11111111')
                self.assertTrue(response.result,'越级上报失败')
                Log.LogOutput(LogLevel.DEBUG, response.text)
                Log.LogOutput(message='越级上报操作成功')
                #设置检查参数
                checkPara=copy.deepcopy(ShiJianChuLiPara.xiaXiaDaiBanJianCha)
                checkPara['issueId']=rs['issueId']
                checkPara['dealState']=110
                checkPara['subject']=issueParam['issue.subject']   
                #验证越级上报功能
                checkBypassIssue(checkParam=checkPara,issueDict=sIssuePara,username=userInit['DftWangGeUser'],password='11111111')
                Log.LogOutput(message='事件越级上报成功')
    #         except Exception, e:
    #             Log.LogOutput(LogLevel.ERROR, '事件越级上报验证过程出现异常！'+str(e))
                
            finally:
                #设置回不允许越级上报
                byPassPara={'issueBypassList[0].orgId':orgInit['DftWangGeOrgId'],'issueBypassList[0].isBypass':False}
                res=ShiJianChuLiIntf.setIssueByPass(issueDict=byPassPara)
                self.assertTrue(res,'取消越级上报设置成功')
        else:
            Log.LogOutput(message='仿真环境，跳过测试')
        pass   
 
 
    '''
    @功能：我的事项-正常交办
    @ chenhui 2015-12-2
    '''     
    def testIssue_015(self):
        '''我的事项-正常交办'''
        #设置新增参数
        #新增事件
        issueParam = copy.deepcopy(ShiJianChuLiPara.issueObject2) 
        rs=ShiJianChuLiIntf.addIssue(issueDict=issueParam, username=userInit['DftJieDaoUser'], password='11111111')
        #街道交办给社区,设置交办参数        
        sIssuePara=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)        
        sIssuePara['operation.dealOrg.id']=orgInit['DftJieDaoOrgId']
        sIssuePara['operation.issue.id']=rs['issueId']
        sIssuePara['keyId']=rs['issueStepId']      
        sIssuePara['operation.dealUserName']=userInit['DftJieDaoUserXM']
        sIssuePara['operation.mobile']=userInit['DftJieDaoUserSJ']
        sIssuePara['operation.content']='普通交办事件'
        sIssuePara['operation.targeOrg.id']=orgInit['DftSheQuOrgId']
        sIssuePara['themainOrgid']=orgInit['DftSheQuOrgId']
        #交办状态代码       
        sIssuePara['dealCode']='21'
        #设置检查参数，待受理状态为110
        checkPara=copy.deepcopy(ShiJianChuLiPara.xiaXiaDaiBanJianCha)
        checkPara['issueId']=rs['issueId']
        checkPara['dealState']=110
        checkPara['subject']=issueParam['issue.subject']
        #执行交办并验证
        dealIssue(issueDict=sIssuePara)
        result=checkAssignIssue(checkParam=checkPara,issueDict=sIssuePara,username=userInit['DftJieDaoUser'],password='11111111')
        self.assertTrue(result,'事件“普通交办”失败！')
        Log.LogOutput(message='普通交办验证成功')
        Log.LogOutput(message='普通交办后受理验证中')
        #受理参数设置
        sIssuePara2={
                     'operation.dealOrg.id':orgInit['DftSheQuOrgId'],
                     'operation.issue.id':sIssuePara['operation.issue.id'],
                     'operation.dealUserName':userInit['DftSheQuUserXM'],
                     'operation.mobile':userInit['DftSheQuUserSJ'],
                     'dealCode':'61',
                     'keyId':sIssuePara['keyId']+1
                     }
        checkPara['dealState']=120
        result=dealIssue(issueDict=sIssuePara2,username=userInit['DftSheQuUser'])
        self.assertTrue(result.result,'事件交办后受理失败！')
        result2=checkAcceptIssue(checkParam=checkPara,issueDict=sIssuePara2,username=userInit['DftSheQuUser'])
        self.assertTrue(result2, '交办并受理验证失败')
        
        pass
    
    '''
    @功能：我的事项-交办并抄告阅读
    @ chenhui 2015-12-3
    '''     
    def testIssue_016(self):
        '''我的事项-交办并抄告阅读'''
        #设置新增参数
        #新增事件
        issueParam = copy.deepcopy(ShiJianChuLiPara.issueObject2) 
        rs=ShiJianChuLiIntf.addIssue(issueDict=issueParam, username=userInit['DftJieDaoUser'], password='11111111')
        #街道交办给社区,设置交办参数        
        sIssuePara=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)        
        sIssuePara['operation.dealOrg.id']=orgInit['DftJieDaoOrgId']
        sIssuePara['operation.issue.id']=rs['issueId']
        sIssuePara['keyId']=rs['issueStepId']      
        sIssuePara['operation.dealUserName']=userInit['DftJieDaoUserXM']
        sIssuePara['operation.mobile']=userInit['DftJieDaoUserSJ']
        sIssuePara['operation.content']='交办并抄告事件'
        sIssuePara['operation.targeOrg.id']=orgInit['DftSheQuOrgId']
        sIssuePara['themainOrgid']=orgInit['DftSheQuOrgId']
        sIssuePara['tellOrgIds']=orgInit['DftJieDaoFuncOrgId']
        sIssuePara['operation.dealDeadline']='2030-12-31'
        
        #交办状态代码       
        sIssuePara['dealCode']='21'
        #设置检查参数，待受理状态为110
        checkPara=copy.deepcopy(ShiJianChuLiPara.xiaXiaDaiBanJianCha)
        checkPara['issueId']=rs['issueId']
        checkPara['dealState']=110
        checkPara['subject']=issueParam['issue.subject']
        #执行交办并抄告
        result=dealIssue(issueDict=sIssuePara)
        self.assertTrue(result.result,'事件“普通交办并抄告”失败！')
        #验证交办并抄告
        result2=checkAssignIssue(checkParam=checkPara,issueDict=sIssuePara)
        self.assertTrue(result2,'普通交办抄告验证失败')
        
        #阅读参数设置
        sIssuePara2={
                     'operation.dealOrg.id':orgInit['DftJieDaoFuncOrgId'],
                     'operation.issue.id':sIssuePara['operation.issue.id'],
                     'operation.dealUserName':userInit['DftJieDaoFuncUserXM'],
                     'operation.mobile':userInit['DftJieDaoFuncUserSJ'],
                     'dealCode':'71',
                     'keyId':sIssuePara['keyId']+2
                     }
        checkPara['dealState']=500
        checkPara['keyId']=orgInit['DftJieDaoFuncOrgId']
        #执行阅读事件操作
        result=dealIssue(issueDict=sIssuePara2,username=userInit['DftJieDaoFuncUser'])
        self.assertTrue(result,'事件交办后阅读失败！')
        #验证阅读功能
        result2=checkReadIssue(checkParam=checkPara,issueDict=sIssuePara2,username=userInit['DftJieDaoFuncUser'])
        self.assertTrue(result2, '交办后阅读失败！')
        pass
    
    '''
    @功能：我的事项-共同办理
    @ chenhui 2015-12-4
    '''     
    def testIssue_017(self):
        '''我的事项-共同办理'''
        #新增事件
        issueParam = copy.deepcopy(ShiJianChuLiPara.issueObject2) 
        rs=ShiJianChuLiIntf.addIssue(issueDict=issueParam, username=userInit['DftJieDaoUser'], password='11111111')
        #街道交办给社区,设置交办参数        
        sIssuePara=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)        
        sIssuePara['operation.dealOrg.id']=orgInit['DftJieDaoOrgId']
        sIssuePara['operation.issue.id']=rs['issueId']
        sIssuePara['keyId']=rs['issueStepId']      
        sIssuePara['operation.dealUserName']=userInit['DftJieDaoUserXM']
        sIssuePara['operation.mobile']=userInit['DftJieDaoUserSJ']
        sIssuePara['togetherHandle']='true'#新加共同办理字典项
        sIssuePara['transferToType']='false'
        sIssuePara['themainOrgid']=str(orgInit['DftSheQuOrgId'])+'-'+str(CommonIntf.getDbQueryResult(dbCommand ="select id from users u where u.username='zdhsq@'"))
        
        sIssuePara['operation.content']='共同办理'
#        sIssuePara['operation.targeOrg.id']=orgInit['DftSheQuOrgId']
        sIssuePara['themainOrgid']=orgInit['DftSheQuOrgId']
        sIssuePara['tellOrgIds']=orgInit['DftJieDaoFuncOrgId']
        sIssuePara['operation.dealDeadline']='2030-12-31'
        sIssuePara['specialAssignType']='1'
        #交办状态代码       
        sIssuePara['dealCode']='21'
        #设置检查参数，待受理状态为110
        checkPara=copy.deepcopy(ShiJianChuLiPara.xiaXiaDaiBanJianCha)
        checkPara['issueId']=rs['issueId']
        checkPara['dealState']=110
        checkPara['subject']=issueParam['issue.subject']
        #执行交办并验证
        Log.LogOutput(message='共同办理交办事件')
        r=dealIssue(issueDict=sIssuePara)
        self.assertTrue(r.result,'共同办理交办失败！')
        result=checkCommonHandelIssue(checkParam=checkPara,issueDict=sIssuePara)
        self.assertTrue(result,'事件“共同办理”失败！')
        #验证后续受理、回复操作
        Log.LogOutput(message='共同办理后受理并回复')
        #受理参数设置
        sIssuePara2={
                     'operation.dealOrg.id':orgInit['DftSheQuOrgId'],
                     'operation.issue.id':sIssuePara['operation.issue.id'],
                     'operation.dealUserName':userInit['DftSheQuUserXM'],
                     'operation.mobile':userInit['DftSheQuUserSJ'],
                     'dealCode':'61',
                     'keyId':sIssuePara['keyId']+2
                     }
        result2=dealIssue(issueDict=sIssuePara2, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(result2.result, '共同办理受理异常！')
        Log.LogOutput(message='共同办理受理成功！')
        #回复
        #设置回复参数
        sIssuePara3=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)
        sIssuePara3['operation.dealOrg.id']=orgInit['DftSheQuOrgId']
        sIssuePara3['operation.issue.id']=sIssuePara['operation.issue.id']
        sIssuePara3['keyId']=sIssuePara['keyId']+2
        sIssuePara3['operation.dealUserName']=userInit['DftSheQuUserXM']
        sIssuePara3['operation.mobile']=userInit['DftSheQuUserSJ']
        sIssuePara3['dealCode']='22'#回复
        sIssuePara3['operation.content']='回复意见'
        
        #设置下辖列表检查参数，待受理状态为110
        checkPara3=copy.deepcopy(ShiJianChuLiPara.xiaXiaDaiBanJianCha)
        checkPara3['issueId']=rs['issueId']
        checkPara3['dealState']=120#我的待办中是待受理110，而下辖是处理中120..
        checkPara3['subject']=issueParam['issue.subject']
        Log.LogOutput(message='事件回复中')
        r3=dealIssue(issueDict=sIssuePara3,username=userInit['DftSheQuUser'])
        self.assertTrue(r3, '事件共同办理回复失败')
        checkReplyIssue(checkParam=checkPara3,issueDict=sIssuePara3,username=userInit['DftSheQuUser'],password='11111111')
        pass



    '''
    @功能：我的事项-事件协同办理
    @ chenhui 2015-12-7
    '''     
    def testIssue_018(self):
        '''我的事项-事件协同办理'''
        #新增事件
        issueParam = copy.deepcopy(ShiJianChuLiPara.issueObject2) 
        rs=ShiJianChuLiIntf.addIssue(issueDict=issueParam, username=userInit['DftJieDaoUser'], password='11111111')
        #街道交办给社区和街道职能部门,设置交办参数        
        sIssuePara=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)        
        sIssuePara['operation.dealOrg.id']=orgInit['DftJieDaoOrgId']
        sIssuePara['operation.issue.id']=rs['issueId']
        sIssuePara['keyId']=rs['issueStepId']      
        sIssuePara['operation.dealUserName']=userInit['DftJieDaoUserXM']
        sIssuePara['operation.mobile']=userInit['DftJieDaoUserSJ']
        sIssuePara['synergyHandle']='true'#新加协同办理字典项
        sIssuePara['transferToType']='true'
        sIssuePara['themainOrgid']=orgInit['DftSheQuOrgId']
        sIssuePara['secondaryOrgid']=orgInit['DftJieDaoFuncOrgId']      
        sIssuePara['operation.content']='协同办理'
        sIssuePara['operation.dealDeadline']='2030-12-31'
        sIssuePara['specialAssignType']='2'
        #交办状态代码       
        sIssuePara['dealCode']='21'
        #设置检查参数，待受理状态为110
        checkPara=copy.deepcopy(ShiJianChuLiPara.xiaXiaDaiBanJianCha)
        checkPara['issueId']=rs['issueId']
        checkPara['dealState']=110
        checkPara['subject']=issueParam['issue.subject']
        #执行交办并验证
        Log.LogOutput(message='协同办理事件交办中')
        r=dealIssue(issueDict=sIssuePara)
        self.assertTrue(r.result,'事件交办协同办理失败')
        result=checkCooperateIssue(checkParam=checkPara,issueDict=sIssuePara,username=userInit['DftJieDaoUser'],password='11111111')
        self.assertTrue(result,'事件“协同办理”失败！')
#        Log.LogOutput(message='协同办理验证成功')
        #验证后续受理、回复操作
        Log.LogOutput(message='协同办理后续操作验证中')

        #主办单位社区受理参数设置
        sIssuePara2={
                     'operation.dealOrg.id':orgInit['DftSheQuOrgId'],
                     'operation.issue.id':sIssuePara['operation.issue.id'],
                     'operation.dealUserName':userInit['DftSheQuUserXM'],
                     'operation.mobile':userInit['DftSheQuUserSJ'],
                     'dealCode':'61',
                     'keyId':sIssuePara['keyId']+1
                     }
        result2=dealIssue(issueDict=sIssuePara2, username=userInit['DftSheQuUser'], password='11111111')
#        print result2.text
        self.assertTrue(result2.result, '主办单位社区受理异常！')
        Log.LogOutput(message='主办单位社区受理成功！')
        
        #协办单位街道职能部门受理参数设置
        sIssuePara3={
                     'operation.dealOrg.id':orgInit['DftJieDaoFuncOrgId'],
                     'operation.issue.id':sIssuePara['operation.issue.id'],
                     'operation.dealUserName':userInit['DftJieDaoFuncUserXM'],
                     'operation.mobile':userInit['DftJieDaoFuncUserSJ'],
                     'dealCode':'61',
                     'keyId':sIssuePara['keyId']+2
                     }
        
        result3=dealIssue(issueDict=sIssuePara3, username=userInit['DftJieDaoFuncUser'], password='11111111')
#        print result2.text
        self.assertTrue(result3.result, '协办单位街道职能部门受理异常！')
        Log.LogOutput(message='协办单位街道职能部门受理成功！')
        
        #主办单位社区直接结案(有bug，原社管已经修复，SOA还有问题)
        
        Log.LogOutput(message='正在验证主办单位不等回复直接结案！')
        sIssuePara4=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)        
        sIssuePara4['operation.dealOrg.id']=orgInit['DftSheQuOrgId']
        sIssuePara4['operation.issue.id']=rs['issueId']
        sIssuePara4['keyId']=sIssuePara['keyId']+1     
        sIssuePara4['operation.dealUserName']=userInit['DftSheQuUserXM']
        sIssuePara4['operation.mobile']=userInit['DftSheQuUserSJ']
        sIssuePara4['operation.content']='事件处理'       
        sIssuePara4['dealCode']='31'#办结
        sIssuePara4['dealTime']=Time.getCurrentDate()
        sIssuePara4['transferToType']='true'
#         result4=dealIssue(issueDict=sIssuePara4, username=userInit['DftSheQuUser'], password='11111111')
#        Log.LogOutput(LogLevel.DEBUG, result4.text)
#         self.assertFalse(result4.result,'直接结案没有返回错误')
#         Log.LogOutput(message="直接结案会返回错误信息验证通过！")
        
        Log.LogOutput(message="正在验证主办单位正常办理中操作！")
        #验证主办单位办理中
        sIssuePara5=copy.deepcopy(sIssuePara4)
        sIssuePara5['dealCode']='1'#办理中
        sIssuePara5['keyId']=sIssuePara['keyId']+1
        sIssuePara5['operation.content']='主办单位社区正在事件处理中...'   
        result5=dealIssue(issueDict=sIssuePara5, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(result5.result,'事件“处理中”失败！')
        Log.LogOutput(message="主办单位正常办理中验证通过！")
        
        #验证协办单位正常办理中
        Log.LogOutput(message="正在验证协办单位正常办理中操作！")
        sIssuePara6=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)
        sIssuePara6['operation.dealOrg.id']=orgInit['DftJieDaoFuncOrgId']
        sIssuePara6['operation.issue.id']=rs['issueId']
        sIssuePara6['operation.dealUserName']=userInit['DftJieDaoFuncUserXM']
        sIssuePara6['operation.mobile']=userInit['DftJieDaoFuncUserSJ']       
        sIssuePara6['dealCode']='1'#办理中
        sIssuePara6['keyId']=sIssuePara['keyId']+2
        sIssuePara6['operation.content']='协办部门街道职能部门正在事件处理中...'
        result6=dealIssue(issueDict=sIssuePara6,username=userInit['DftJieDaoFuncUser'], password='11111111')
#        print result6.text
        self.assertTrue(result6.result,'协办单位事件“处理中”失败！')
        Log.LogOutput(message="协办单位正常办理验证通过！")
        
        Log.LogOutput(message="协办单位回复验证中...")
        #协办单位回复   
        #设置回复参数
        sIssuePara7=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)
        sIssuePara7['operation.dealOrg.id']=orgInit['DftSheQuOrgId']
        sIssuePara7['operation.issue.id']=sIssuePara['operation.issue.id']
        sIssuePara7['keyId']=sIssuePara['keyId']+2
        sIssuePara7['operation.dealUserName']=userInit['DftSheQuUserXM']
        sIssuePara7['operation.mobile']=userInit['DftSheQuUserSJ']
        sIssuePara7['dealCode']='22'#回复
        sIssuePara7['operation.content']='协办单位回复意见'
        result7=dealIssue(issueDict=sIssuePara7,username=userInit['DftJieDaoFuncUser'], password='11111111')
#        print result7.text
        self.assertTrue(result7.result,'协办单位事件“回复”失败！')
        Log.LogOutput(message="协办单位正常回复功能通过！")
        
        Log.LogOutput(message="正在验证主办单位正常结案操作...")
        sIssuePara4['keyId']=sIssuePara['keyId']+1
        result4=dealIssue(issueDict=sIssuePara4, username=userInit['DftSheQuUser'], password='11111111')
#        print result4.text
        self.assertTrue(result4.result,'事件“办结”失败！')
        Log.LogOutput(message="协办单位回复后，主办单位结案功能通过！")
        
        Log.LogOutput(message="协同办理整体功能验证通过")
        
        pass

    '''
    @功能：我的事项-宣传案例,屏蔽了新增直接设置宣传案例验证
    @ chenhui 2015-12-7
    '''     
    def testIssue_019(self):
        '''我的事项-宣传案例'''
        #新增事件
        issueParam = copy.deepcopy(ShiJianChuLiPara.issueObject2) 
        rs=ShiJianChuLiIntf.addIssue(issueDict=issueParam, username=userInit['DftJieDaoUser'], password='11111111')
        #验证新增直接设置宣传案例(有bug)
#         Log.LogOutput( message='验证新增事件后，直接设置宣传案例是否有错误信息')     
#         sIssuePara0={'keyId':rs['issueId']  }
        #设置检查参数
#         checkPara0={'subject':issueParam['issue.subject']}
#         result0=ShiJianChuLiIntf.checkPublicCase(mode='set',checkPara=checkPara0,issueDict=sIssuePara0)
#         self.assertFalse(result0, '新增事件直接设置宣传案例验证错误')
#         Log.LogOutput(message='新增事件直接设置宣传案例验证通过！')
        
        #验证新增直接取消设置案例(原社管已经修复，SOA有bug)
#         Log.LogOutput( message='验证新增事件后，直接取消宣传案例是否有错误信息')     
#         sIssuePara1={'keyId':rs['issueId']  }
        #设置检查参数
#         checkPara1={'subject':issueParam['issue.subject']}
#         result1=ShiJianChuLiIntf.checkPublicCase(mode='cancel',checkPara=checkPara1,issueDict=sIssuePara1)
#         self.assertFalse(result1, '新增事件直接设置宣传案例验证错误')
#         Log.LogOutput(message='新增事件直接设置宣传案例验证通过！')
        
        #结案
        sIssuePara=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)        
        sIssuePara['operation.dealOrg.id']=orgInit['DftJieDaoOrgId']
        sIssuePara['operation.issue.id']=rs['issueId']
        sIssuePara['keyId']=rs['issueStepId']      
        sIssuePara['operation.dealUserName']=userInit['DftJieDaoUserXM']
        sIssuePara['operation.mobile']=userInit['DftJieDaoUserSJ']
        sIssuePara['operation.content']='事件处理'
        sIssuePara['dealCode']='31'#结案
        sIssuePara['dealTime']=Time.getCurrentDate()
        sIssuePara['transferToType']='true'
        result=dealIssue(issueDict=sIssuePara,username=userInit['DftJieDaoUser'],password='11111111')
#        print result.text
        self.assertTrue(result,'事件“结案”失败！')
        Log.LogOutput( message='事件办结成功')
        #设置宣传案例
        sIssuePara2={'keyId':rs['issueId']  }
        #设置检查参数
        checkPara2={'subject':issueParam['issue.subject']}
#        result2=ShiJianChuLiIntf.setPublicCase(issueDict=sIssuePara2)
        result2=checkPublicCase(mode='set',checkPara=checkPara2,issueDict=sIssuePara2)
        self.assertTrue(result2,'设置宣传案例失败')
        Log.LogOutput( message='设置宣传案例验证通过')
        
        #取消宣传案例
        sIssuePara3={'keyId':rs['issueId']  }
        checkPara3={'subject':issueParam['issue.subject']}
        result3=checkPublicCase(mode='cancel',checkPara=checkPara3,issueDict=sIssuePara3)
        self.assertTrue(result3,'取消宣传案例失败')
        Log.LogOutput( message='取消宣传案例验证通过')
        pass

    '''
    @功能：我的事项-撤回
    @ chenhui 2015-12-8
    '''     
    def testIssue_020(self):
        '''我的事项-撤回'''
        #新增事件
        issueParam = copy.deepcopy(ShiJianChuLiPara.issueObject2) 
        rs=ShiJianChuLiIntf.addIssue(issueDict=issueParam, username=userInit['DftJieDaoUser'], password='11111111')
        #直接撤回
        Log.LogOutput(message='新增直接撤回')
        issueDict={'keyId':rs['issueId']}
        result0=revocationIssue(issueDict=issueDict)
        self.assertFalse(result0.result, '新增事件直接回撤没有返回错误信息')
        Log.LogOutput(message='新增直接撤回回返回错误信息，验证通过')
        
        #交办撤回
        #街道交办给社区,设置交办参数        
        sIssuePara=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)        
        sIssuePara['operation.dealOrg.id']=orgInit['DftJieDaoOrgId']
        sIssuePara['operation.issue.id']=rs['issueId']
        sIssuePara['keyId']=rs['issueStepId']      
        sIssuePara['operation.dealUserName']=userInit['DftJieDaoUserXM']
        sIssuePara['operation.mobile']=userInit['DftJieDaoUserSJ']
        sIssuePara['operation.content']='普通交办事件'
        sIssuePara['operation.targeOrg.id']=orgInit['DftSheQuOrgId']
        sIssuePara['themainOrgid']=orgInit['DftSheQuOrgId']
        sIssuePara['dealCode']='21'
        
        result1=ShiJianChuLiIntf.dealIssue(issueDict=sIssuePara, username=userInit['DftJieDaoUser'], password='11111111')
        if result1.result is True:
            Log.LogOutput(message='交办成功，验证撤回功能')
#            print result1.text
            rs1=checkRevocationIssue(dealType='交办',checkPara={'issueSubject':issueParam['issue.subject']},issueDict=issueDict,username=userInit['DftJieDaoUser'],password='11111111')
            self.assertTrue(rs1, msg='交办撤回失败')
            Log.LogOutput(message='交办撤回成功！')
        else:
            Log.LogOutput(message='交办功能出现异常')
        
        #上报后撤回
        sIssuePara2=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)        
        sIssuePara2['operation.dealOrg.id']=orgInit['DftJieDaoOrgId']
        sIssuePara2['operation.issue.id']=rs['issueId']
        sIssuePara2['keyId']=rs['issueStepId']      
        sIssuePara2['operation.dealUserName']=userInit['DftJieDaoUserXM']
        sIssuePara2['operation.mobile']=userInit['DftJieDaoUserSJ']
        sIssuePara2['operation.content']='上报事件'
        sIssuePara2['operation.targeOrg.id']=orgInit['DftQuOrgId']
        sIssuePara2['themainOrgid']=orgInit['DftQuOrgId']        
        sIssuePara2['dealCode']='41'#上报
        
        result2=ShiJianChuLiIntf.dealIssue(issueDict=sIssuePara2,username=userInit['DftJieDaoUser'],password='11111111')
        if result2.result is True:
            Log.LogOutput(message='上报成功，验证撤回功能')
#            print result2.text
            rs2=checkRevocationIssue(dealType='上报',checkPara={'issueSubject':issueParam['issue.subject']},issueDict=issueDict,username=userInit['DftJieDaoUser'],password='11111111')
            self.assertTrue(rs2, msg='上报撤回失败')
            Log.LogOutput(message='上报撤回成功！')
        else:
            Log.LogOutput(message='上报功能出现异常')
        
        #交办后受理
        result3=ShiJianChuLiIntf.dealIssue(issueDict=sIssuePara, username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(result3,'交办过程中出现错误')
        #社区受理
        #受理参数设置
        sIssuePara3={
                     'operation.dealOrg.id':orgInit['DftSheQuOrgId'],
                     'operation.issue.id':sIssuePara2['operation.issue.id'],
                     'operation.dealUserName':userInit['DftSheQuUserXM'],
                     'operation.mobile':userInit['DftSheQuUserSJ'],
                     'dealCode':'61',
                     'keyId':sIssuePara2['keyId']+3
                     }
        rs3=ShiJianChuLiIntf.dealIssue(issueDict=sIssuePara3, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(rs3.result,'受理过程中出现错误')
        Log.LogOutput(message='事件受理成功，正在验证受理后撤回操作是否会返回错误信息')
        #验证社区受理后撤回会返回错误信息
        r=revocationIssue(issueDict=issueDict,username=userInit['DftSheQuUser'],password='11111111')
        self.assertFalse(r.result,'受理后撤回返回错误信息验证失败')
        Log.LogOutput(message='受理后撤回会返回错误信息验证通过！')
        #验证社区受理后，街道撤回操作会返回错误信息
        r2=revocationIssue(issueDict=issueDict,username=userInit['DftJieDaoUser'],password='11111111')
        self.assertFalse(r2.result, msg='社区受理后，街道撤回返回错误信息验证失败')
        Log.LogOutput(message='社区受理后，街道撤回会返回错误信息验证通过！')
        #清空事件
        ShiJianChuLi.ShiJianChuLiIntf.deleteAllIssues()
        
        #验证上报到区，区级阅读后撤回
        #重新新增事件
        Log.LogOutput(message='重新新增事件，验证上报阅读后的撤回功能')
        issueParam2 = copy.deepcopy(ShiJianChuLiPara.issueObject2)
        
        rs22=ShiJianChuLiIntf.addIssue(issueDict=issueParam2, username=userInit['DftJieDaoUser'], password='11111111')
        #设置上报参数
        sIssuePara22=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)        
        sIssuePara22['operation.dealOrg.id']=orgInit['DftJieDaoOrgId']
        sIssuePara22['operation.issue.id']=rs22['issueId']
        sIssuePara22['keyId']=rs22['issueStepId']      
        sIssuePara22['operation.dealUserName']=userInit['DftJieDaoUserXM']
        sIssuePara22['operation.mobile']=userInit['DftJieDaoUserSJ']
        sIssuePara22['operation.content']='上报事件'
        sIssuePara22['operation.targeOrg.id']=orgInit['DftQuOrgId']
        sIssuePara22['themainOrgid']=orgInit['DftQuOrgId']        
        sIssuePara22['dealCode']='41'
        sIssuePara22['tellOrgIds']=orgInit['DftQuFuncOrgId']
#        print sIssuePara22
        result4=dealIssue(issueDict=sIssuePara22,username=userInit['DftJieDaoUser'],password='11111111')
#        print result4.text
        self.assertTrue(result4.result,'上报失败')
        Log.LogOutput(message='上报成功，验证撤回功能')
        #区职能部门阅读事件
        sIssuePara4={
                     'operation.dealOrg.id':orgInit['DftQuFuncOrgId'],
                     'operation.issue.id':sIssuePara22['operation.issue.id'],
                     'operation.dealUserName':userInit['DftQuFuncUserXM'],
                     'operation.mobile':userInit['DftQuFuncUserSJ'],
                     'dealCode':'71',
                     'keyId':rs22['issueStepId']+2
                     }
        issueDict2={'keyId':rs22['issueId']}
        result5=dealIssue(issueDict=sIssuePara4,username=userInit['DftQuFuncUser'],password='11111111')
        self.assertTrue(result5.result,'事件抄告后阅读失败！')
        Log.LogOutput(message='区职能部门阅读成功') 
        
        #验证区阅读后撤回会返回错误信息
        Log.LogOutput(message='验证区职能部门阅读后，立即撤回会返回错误信息...') 
        r5=revocationIssue(issueDict=issueDict2,username=userInit['DftQuFuncUser'],password='11111111')
#        print r5.text
        self.assertFalse(r5.result,'阅读后撤回返回错误信息验证失败')
        Log.LogOutput(message='区职能部门阅读后立即撤回会返回错误信息验证通过！')  
        
        #验证区职能部门阅读后，街道部门撤回功能
        Log.LogOutput(message='验证区职能部门阅读后，街道部门撤回功能...') 
        r6=revocationIssue(issueDict=issueDict2,username=userInit['DftJieDaoUser'],password='11111111')
#        print r6.text
        self.assertFalse(r6.result,'区职能部门阅读后，街道撤回没有返回错误信息')
        Log.LogOutput(message='区职能部阅读后，街道撤回会返回错误信息验证通过！')
        
        #办结后撤回，返回异常信息  
        Log.LogOutput(message='清空事件')
        ShiJianChuLi.ShiJianChuLiIntf.deleteAllIssues()
        #重新新增事件
        Log.LogOutput(message='重新新增事件，验证结案后的撤回功能')
        issueParam3 = copy.deepcopy(ShiJianChuLiPara.issueObject2)
        rs33=ShiJianChuLiIntf.addIssue(issueDict=issueParam3, username=userInit['DftJieDaoUser'], password='11111111')
        #设置结案参数
        sIssuePara33=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)        
        sIssuePara33['operation.dealOrg.id']=orgInit['DftJieDaoOrgId']
        sIssuePara33['operation.issue.id']=rs33['issueId']
        sIssuePara33['keyId']=rs33['issueStepId']      
        sIssuePara33['operation.dealUserName']=userInit['DftJieDaoUserXM']
        sIssuePara33['operation.mobile']=userInit['DftJieDaoUserSJ']
        sIssuePara33['operation.content']='验证事件结案后撤回'
        sIssuePara33['dealCode']='31'
        sIssuePara['dealTime']=Time.getCurrentDate()
        sIssuePara['transferToType']='true'
        result6=dealIssue(issueDict=sIssuePara33, username=userInit['DftJieDaoUser'], password='11111111')
#        print result6.text
        self.assertTrue(result6.result, '事件办结失败')
        Log.LogOutput(message='事件办结成功！')
        Log.LogOutput(message='正在进行办结后撤回操作验证')
        r7=revocationIssue(issueDict=issueDict2,username=userInit['DftJieDaoUser'],password='11111111')
#        print r7.text
        self.assertFalse(r7.result, '办结后立即撤回，没有返回错误信息')        
        Log.LogOutput(message='事件结案后立即撤回，会返回错误信息，验证通过！')
        
        pass   
 
 
    '''
    @功能：我的事项-追加部门异常情况验证
    @ chenhui 2015-12-8
    '''     
    def testIssue_021(self):
        '''我的事项-追加部门异常情况验证'''
        #新增事件
        issueParam = copy.deepcopy(ShiJianChuLiPara.issueObject2) 
        rs=ShiJianChuLiIntf.addIssue(issueDict=issueParam, username=userInit['DftJieDaoUser'], password='11111111')
        #直接追加部门
        Log.LogOutput(message='验证新增事件直接追加部门会返回错误信息')
        result=addIssueOrg(issueDict={'keyId':rs['issueId']})

        self.assertFalse(result.result,'直接追加部门验证失败')
        Log.LogOutput( message='新增事件直接追加部门返回错误信息，验证通过！')
        
        #普通交办事件后追加部门
        #街道交办给社区,设置交办参数
        Log.LogOutput(message='普通交办事件并追加部门会返回错误信息')        
        sIssuePara=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)        
        sIssuePara['operation.dealOrg.id']=orgInit['DftJieDaoOrgId']
        sIssuePara['operation.issue.id']=rs['issueId']
        sIssuePara['keyId']=rs['issueStepId']      
        sIssuePara['operation.dealUserName']=userInit['DftJieDaoUserXM']
        sIssuePara['operation.mobile']=userInit['DftJieDaoUserSJ']
        sIssuePara['operation.content']='普通交办事件'
        sIssuePara['operation.targeOrg.id']=orgInit['DftSheQuOrgId']
        sIssuePara['themainOrgid']=orgInit['DftSheQuOrgId']
        #交办状态代码       
        sIssuePara['dealCode']='21'
        
        result1=ShiJianChuLiIntf.dealIssue(issueDict=sIssuePara, username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(result1.result)
        Log.LogOutput(message='普通交办成功，即将进行追加部门验证...')
        #追加部门       
        result=addIssueOrg(issueDict={'keyId':rs['issueId']})
        self.assertFalse(result.result,'追加部门验证失败')
        Log.LogOutput( message='普通交办事件后追加部门返回错误信息，验证通过！')
        
        #撤回事件
        r=revocationIssue(issueDict={'keyId':rs['issueId']},username=userInit['DftJieDaoUser'],password='11111111')
#        print r.text
        self.assertTrue(r.result)
        Log.LogOutput(message='撤回普通交办事件成功')
        #设置上报参数
        sIssuePara2=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)        
        sIssuePara2['operation.dealOrg.id']=orgInit['DftJieDaoOrgId']
        sIssuePara2['operation.issue.id']=rs['issueId']
        sIssuePara2['keyId']=rs['issueStepId']      
        sIssuePara2['operation.dealUserName']=userInit['DftJieDaoUserXM']
        sIssuePara2['operation.mobile']=userInit['DftJieDaoUserSJ']
        sIssuePara2['operation.content']='上报事件'
        sIssuePara2['operation.targeOrg.id']=orgInit['DftQuOrgId']
        sIssuePara2['themainOrgid']=orgInit['DftQuOrgId']        
        sIssuePara2['dealCode']='41'#上报
        result2=ShiJianChuLiIntf.dealIssue(issueDict=sIssuePara2, username=userInit['DftJieDaoUser'], password='11111111')
#        print result2.text
        self.assertTrue(result2.result)
        Log.LogOutput(message='上报成功，即将进行追加部门验证...')
        #追加部门
        result22=addIssueOrg(issueDict={'keyId':rs['issueId']})
        self.assertFalse(result22.result, '追加验证失败')
        Log.LogOutput( message='上报事件后追加部门返回错误信息，验证通过！')
        #撤回
        r=revocationIssue(issueDict={'keyId':rs['issueId']},username=userInit['DftJieDaoUser'],password='11111111')
        self.assertTrue(r.result)
        Log.LogOutput(message='撤回普通交办事件成功')
        #清空数据
        Log.LogOutput(message='清空数据')
        ShiJianChuLi.ShiJianChuLiIntf.deleteAllIssues()
        
        #重新新增数据
        Log.LogOutput(message='重新新增事件并追加部门')
        rs=ShiJianChuLiIntf.addIssue(issueDict=issueParam, username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(rs, '新增失败')
        #结案
        sIssuePara3=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)        
        sIssuePara3['operation.dealOrg.id']=orgInit['DftJieDaoOrgId']
        sIssuePara3['operation.issue.id']=rs['issueId']
        sIssuePara3['keyId']=rs['issueStepId']      
        sIssuePara3['operation.dealUserName']=userInit['DftJieDaoUserXM']
        sIssuePara3['operation.mobile']=userInit['DftJieDaoUserSJ']
        sIssuePara3['operation.content']='结案'
        sIssuePara3['dealCode']='31'#结案
        sIssuePara['dealTime']=Time.getCurrentDate()
        sIssuePara['transferToType']='true'
        result3=ShiJianChuLiIntf.dealIssue(issueDict=sIssuePara3,username=userInit['DftJieDaoUser'],password='11111111')
        self.assertTrue(result3.result,'事件“结案”失败！')
        Log.LogOutput(message='事件办结成功,即将验证追加部门功能')
        #追加部门
        result33=addIssueOrg(issueDict={'keyId':rs['issueId']})
        self.assertFalse(result33.result, '追加部门验证失败')
        Log.LogOutput( message='办结事件后追加部门返回错误信息，验证通过！')
        
        pass
       
    '''
    @功能：我的事项-协同办理和共同办理后的追加部门
    @ chenhui 2015-12-8
    '''     
    def testIssue_022(self):
        '''我的事项-协同办理和共同办理后的追加部门'''
        #新增事件
        issueParam = copy.deepcopy(ShiJianChuLiPara.issueObject2) 
        rs=ShiJianChuLiIntf.addIssue(issueDict=issueParam, username=userInit['DftJieDaoUser'], password='11111111')
        #街道交办给社区和街道职能部门,设置交办参数        
        sIssuePara=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)        
        sIssuePara['operation.dealOrg.id']=orgInit['DftJieDaoOrgId']
        sIssuePara['operation.issue.id']=rs['issueId']
        sIssuePara['keyId']=rs['issueStepId']      
        sIssuePara['operation.dealUserName']=userInit['DftJieDaoUserXM']
        sIssuePara['operation.mobile']=userInit['DftJieDaoUserSJ']
        sIssuePara['synergyHandle']='true'#新加协同办理字典项
        sIssuePara['transferToType']='true'
        sIssuePara['themainOrgid']=orgInit['DftSheQuOrgId']
        sIssuePara['secondaryOrgid']=orgInit['DftJieDaoFuncOrgId']      
        sIssuePara['operation.content']='协同办理'
        sIssuePara['operation.dealDeadline']='2030-12-31'
        #协同办理标志参数
        sIssuePara['specialAssignType']='2'
        #交办状态代码       
        sIssuePara['dealCode']='21'
        #执行交办并验证
        result=dealIssue(issueDict=sIssuePara)
        self.assertTrue(result.result, '协同交办失败')
        Log.LogOutput(message='协同交办成功，执行追加部门操作中...')
        #执行追加部门并验证
        r=addIssueOrg(issueDict={'keyId':rs['issueId']})
        self.assertTrue(r,'追加入口打开失败')
        Log.LogOutput(message='追加入口打开，允许追加')
        #真正执行追加操作
        #追加协办单位
        #设置追加协办单位参数
        sIssuePara2=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)        
        sIssuePara2['operation.dealOrg.id']=orgInit['DftJieDaoOrgId']
        sIssuePara2['operation.issue.id']=rs['issueId']
        sIssuePara2['keyId']=rs['issueStepId']      
        sIssuePara2['operation.dealUserName']=userInit['DftJieDaoUserXM']
        sIssuePara2['operation.mobile']=userInit['DftJieDaoUserSJ']
        sIssuePara2['transferToType']='true'
        sIssuePara2['operation.content']='追加部门操作！！'
        #协同办理标志参数
        sIssuePara2['specialAssignType']='2'
        #交办状态代码       
        sIssuePara2['dealCode']='23'
        #不设置追加部门，直接追加，验证错误信息
        Log.LogOutput(message='验证不设置追加的部门，直接提交，是否返回错误信息')
        result2=dealIssue(issueDict=sIssuePara2)

        self.assertFalse(result2.result,'事件不设置追加部门，直接追加返回错误信息验证失败！')
        Log.LogOutput(message='不设置追加部门，直接操作返回错误信息验证通过')
        #设置追加部门，并验证
        
        Log.LogOutput(message='执行正常追加操作')
        sIssuePara2['secondaryOrgid']=orgInit['DftJieDaoFuncOrgId1']#追加的协办单位的orgId
        sIssuePara2['tag']=orgInit['DftSheQuOrg']

        result22=dealIssue(issueDict=sIssuePara2)
        self.assertTrue(result22.result, '追加操作失败')
        #验证追加功能
        result3=checkAddOrg()
        self.assertTrue(result3,'追加失败！')
        pass
    
    '''
    @功能：我的事项-已办结事项-评价
    @ chenhui 2015-12-14
    '''      
    def testIssue_023(self):
        '''我的事项-已办结事项-评价'''
        #新增事件
        issueParam = copy.deepcopy(ShiJianChuLiPara.issueObject2)     
        rs=ShiJianChuLiIntf.addIssue(issueDict=issueParam, username=userInit['DftJieDaoUser'], password='11111111')
        #设置办理中参数
        sIssuePara=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)        
        sIssuePara['operation.dealOrg.id']=orgInit['DftJieDaoOrgId']
        sIssuePara['operation.issue.id']=rs['issueId']
        sIssuePara['keyId']=rs['issueStepId']      
        sIssuePara['operation.dealUserName']=userInit['DftJieDaoUserXM']
        sIssuePara['operation.mobile']=userInit['DftJieDaoUserSJ']
        sIssuePara['operation.content']='事件结案'      
        sIssuePara['dealCode']='31'#办理中
        sIssuePara['dealTime']=Time.getCurrentDate()
        sIssuePara['transferToType']='true'
        #验证评价功能
        #设置评价参数
        sIssuePara2=copy.deepcopy(issueEvaluateParam)
        #验证必填项
        Log.LogOutput( message='验证评价必填项')
        result2=evaluateIssue(issueDict=sIssuePara2)
        self.assertFalse(result2.result,'评价失败')
        #验证未结案，直接评价
        sIssuePara2['issueEvaluate.issue.id']=rs['issueId']
        sIssuePara2['issueEvaluate.evaluateTime']=Time.getCurrentDate()
        sIssuePara2['score']='3'
        sIssuePara2['issueEvaluate.evaluateType']='3'
        sIssuePara2['issueEvaluate.evaluateContent']='评价内容'
        Log.LogOutput( message='验证未办结事项直接评价会返回错误信息')
        result2=evaluateIssue(issueDict=sIssuePara2)
        result2Json=json.loads(result2.text)
        self.assertEqual(result2Json['message'],'该事件未办结，不能评价！')
        Log.LogOutput(message='事件未结案直接评价返回错误信息验证通过')
        #验证只输入必填项评价
        result2=evaluateIssue(issueDict=sIssuePara2)
        self.assertTrue(result2, '事件评价失败')
        #办结后评价
        Log.LogOutput(message='验证结案后再评价功能')
        Log.LogOutput(message='正在办结事件')
        result=dealIssue(issueDict=sIssuePara)
        self.assertTrue(result.result, '事件结案失败!')
        #评价事件
        result3=evaluateIssue(issueDict=sIssuePara2)
        self.assertTrue(result3, '事件评价失败')
        
        pass
    
    '''
    @功能：我的事项-报表统计
    @ chenhui 2015-12-14
    '''      
    def testIssue_024(self):
        '''我的事项-报表统计'''
        #新增矛盾纠纷类型的事件
        issueParam = copy.deepcopy(ShiJianChuLiPara.issueObject2)     
        rs=ShiJianChuLiIntf.addIssue(issueDict=issueParam, username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(rs, '新增失败')
        #设置检查参数
        checkParam={
                    'subject':issueParam['issue.subject'],
                    'issueTypeName':'矛盾纠纷'
                    }
        #验证报表统计列表显示功能
        check1=findMyTypeIssueBySub(checkParam=checkParam)
        checkParam['issueTypeName']='治安、安全隐患'
        check2=findMyTypeIssueBySub(checkParam=checkParam)
        checkParam['issueTypeName']='民生服务'
        check3=findMyTypeIssueBySub(checkParam=checkParam)
        checkParam['issueTypeName']='其他'
        check4=findMyTypeIssueBySub(checkParam=checkParam)
        if check1 is True and check2 is False and check3 is False and check4 is False:
            Log.LogOutput(message='矛盾纠纷类型列表正确')
        else:
            Log.LogOutput(LogLevel.ERROR,message='矛盾纠纷类型列表错误')
        #修改事件类型为治安、安全隐患
        issueParam['issue.id']=rs['issueId']
        issueParam['issue.serialNumber']=rs['serialNumber']
        issueParam['selectedTypes']=getDbQueryResult(dbCommand ="select id from issuetypes i where i.domainid=(select id from issuetypedomains where module='core' and domainName='治安、安全隐患') and i.issuetypename='安全生产'")
        r=ShiJianChuLiIntf.updIssue(issueDict=issueParam, username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(r.result, '事件修改失败')
        
        #验证报表统计列表显示功能
        checkParam['issueTypeName']='矛盾纠纷'
        check1=findMyTypeIssueBySub(checkParam=checkParam)
        checkParam['issueTypeName']='治安、安全隐患'
        check2=findMyTypeIssueBySub(checkParam=checkParam)
        checkParam['issueTypeName']='民生服务'
        check3=findMyTypeIssueBySub(checkParam=checkParam)
        checkParam['issueTypeName']='其他'
        check4=findMyTypeIssueBySub(checkParam=checkParam)
        if check1 is False and check2 is True and check3 is False and check4 is False:
            Log.LogOutput(message='治安、安全隐患类型列表正确')
        else:
            Log.LogOutput(LogLevel.ERROR,message='治安、安全隐患类型列表错误')
            
        #修改事件类型为民生服务
        issueParam['selectedTypes']=getDbQueryResult(dbCommand ="select id from issuetypes i where i.domainid=(select id from issuetypedomains where module='core' and domainName='民生服务') and i.issuetypename='教育'")
        r=ShiJianChuLiIntf.updIssue(issueDict=issueParam, username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(r.result, '事件修改失败') 
        #验证报表统计列表显示功能
        checkParam['issueTypeName']='矛盾纠纷'
        check1=findMyTypeIssueBySub(checkParam=checkParam)
        checkParam['issueTypeName']='治安、安全隐患'
        check2=findMyTypeIssueBySub(checkParam=checkParam)
        checkParam['issueTypeName']='民生服务'
        check3=findMyTypeIssueBySub(checkParam=checkParam)
        checkParam['issueTypeName']='其他'
        check4=findMyTypeIssueBySub(checkParam=checkParam)
        if check1 is False and check2 is False and check3 is True and check4 is False:
            Log.LogOutput(message='民生服务类型列表正确')
        else:
            Log.LogOutput(LogLevel.ERROR,message='民生服务类型列表错误')
               
        #修改为其他       
        issueParam['selectedTypes']=getDbQueryResult(dbCommand = "select id from issuetypes i where i.domainid=(select id from issuetypedomains where module='core' and domainName='其他') and i.issuetypename='其他'")
        r=ShiJianChuLiIntf.updIssue(issueDict=issueParam, username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(r.result, '事件修改失败')
        #验证报表统计列表显示功能
        checkParam['issueTypeName']='矛盾纠纷'
        check1=findMyTypeIssueBySub(checkParam=checkParam)
        checkParam['issueTypeName']='治安、安全隐患'
        check2=findMyTypeIssueBySub(checkParam=checkParam)
        checkParam['issueTypeName']='民生服务'
        check3=findMyTypeIssueBySub(checkParam=checkParam)
        checkParam['issueTypeName']='其他'
        check4=findMyTypeIssueBySub(checkParam=checkParam)
        if check1 is False and check2 is False and check3 is False and check4 is True:
            Log.LogOutput(message='其他类型列表正确')
        else:
            Log.LogOutput(LogLevel.ERROR,message='其他类型列表错误')
                   
        pass    
    
    
    '''
    @功能：我的事项-限时办结
    @ chenhui 2015-12-15
    '''      
    def testIssue_025(self):
        '''我的事项-限时办结规则设置及列表显示'''
        #街道账号设置街道和直属下辖社区的限时办结规则
        #设置办结规则参数
        sIssuePara=copy.deepcopy(ShiJianChuLiPara.issueCompleteLimitConfigParam)        
        sIssuePara['mode']='add'
        sIssuePara['organization.id']=CommonIntf.getOrgInfoByAccount('zdhjd@')['orgId']
        sIssuePara['issueCompleteLimitConfig.organization.id']=sIssuePara['organization.id']
        sIssuePara['issueCompleteLimitConfig.limitDay']='4'
        sIssuePara['issueCompleteLimitConfig.normalDay']='3'
        sIssuePara['issueCompleteLimitConfig.expireDay']='1'
        sIssuePara['issueCompleteLimitConfig.enable']='1'
        result=addIssueCompleteLimitConfig(issueDict=sIssuePara)
        self.assertTrue(result,'新增限时办结规则失败')
        #新增事件
        issueParam = copy.deepcopy(ShiJianChuLiPara.issueObject2)     
        rs=addIssue(issueDict=issueParam, username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(rs,'新增失败')
        #交办事件
        sIssuePara1=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)        
        sIssuePara1['operation.dealOrg.id']=orgInit['DftJieDaoOrgId']
        sIssuePara1['operation.issue.id']=rs['issueId']
        sIssuePara1['keyId']=rs['issueStepId']      
        sIssuePara1['operation.dealUserName']=userInit['DftJieDaoUserXM']
        sIssuePara1['operation.mobile']=userInit['DftJieDaoUserSJ']
        sIssuePara1['operation.content']='普通交办事件'
        sIssuePara1['operation.targeOrg.id']=orgInit['DftSheQuOrgId']
        sIssuePara1['themainOrgid']=orgInit['DftSheQuOrgId']
        #交办状态代码       
        sIssuePara1['dealCode']='21'
        Log.LogOutput( message='事件交办中')
        #执行交办并验证
        result=dealIssue(issueDict=sIssuePara1)
        self.assertTrue(result.result,'交办失败')
        #验证社区限时办结列表是否有该事件
        #设置检查参数
        checkParam={
                    'issueId':rs['issueId'],
                    'subject':rs['subject'],
                    'serialNumber':rs['serialNumber']
                    }
        #设置限时办结-全部事项列表请求参数
        sIssuePara2={
                    'issueCompleteLimitVo.targeOrgId':orgInit['DftSheQuOrgId'],
                    'issueCompleteLimitVo.limitStatus':'',
                    'issueCompleteLimitVo.limitDayOrder':'0',
                    'page':'1',
                    '_search':'false',
                    'rows':'200',
                    'sidx':'lastdealdate',
                    'sord':'desc'
                    }
        result2=checkIssueCompleteLimitList(checkPara=checkParam,issueDict=sIssuePara2,username=userInit['DftSheQuUser'])
        self.assertTrue(result2,'限时办结列表验证失败')
        Log.LogOutput(message='事件交办后，限时办结列表显示功能验证通过')
        
        #申请延时
        #设置限期办结-延时设置参数
        sIssuePara3={
                    'mode':'add',
                    'issueCompleteDelay.id':'',
                    'issueCompleteDelay.organization.id':'',
                    'issueCompleteDelay.issue.id':rs['issueId'],
                    'issueCompleteDelay.orgId':orgInit['DftSheQuOrgId'],
                    'issueCompleteDelay.reason':'延时原因',
                    'issueCompleteDelay.applyDays':'100'
                     }
        response=applyIssueDelay(issueDict=sIssuePara3,username=userInit['DftSheQuUser'])
        self.assertTrue(response.result,'申请延时失败！')
        Log.LogOutput(message='验证延时申请后街道是否收到')
        #设置街道“延时设置”列表显示参数
        sIssuePara4=copy.deepcopy(sIssuePara2)
        sIssuePara4['issueCompleteLimitVo.targeOrgId']=orgInit['DftJieDaoOrgId']
        #检查参数不变，仍然是checkParam
        checkIssueDelayApply(checkPara=checkParam,issueDict=sIssuePara4)
        Log.LogOutput(message='街道“延时设置”列表中存在数据，申请延时验证通过！')
        
        
        #验证多次重复申请延时
#         Log.LogOutput(message='正在验证再次申请延时能否返回错误信息')
#         response1=applyIssueDelay(issueDict=sIssuePara3,username=userInit['DftSheQuUser'])
#         self.assertFalse(response1.result,'再次申请延时会返回错误信息验证失败')
#         Log.LogOutput(message='多次申请延时返回错误信息验证通过')
        #街道层级拒绝延时
        #设置设置延时参数-拒绝
        responseDict=json.loads(response.text)
        Log.LogOutput(message='街道层级拒绝延时')
        sIssuePara41={
                    'mode':'setDelay',
                    'issueCompleteDelay.id':responseDict['id'],#可能报错
                    'issueCompleteDelay.organization.id':orgInit['DftSheQuOrgId'],
                    'issueCompleteDelay.issue.id':rs['issueId'],
                    'issueCompleteDelay.isAudit':'2',
                    'issueCompleteDelay.orgId':orgInit['DftJieDaoOrgId'],
                    'issueCompleteDelay.reason':sIssuePara3['issueCompleteDelay.reason'],
                    'issueCompleteDelay.applyDays':sIssuePara3['issueCompleteDelay.applyDays']
                     }
        response4=setDelay(issueDict=sIssuePara41)
        self.assertTrue(response4.result, '设置延时失败')
        #设置检查参数，验证设置延时列表数据是否正确，延时天数为0
        Log.LogOutput(message='正在验证列表中是否存在延时设置后的数据')
        checkParam4=copy.deepcopy(checkParam)
        checkParam4['delayDays']=0
        r=checkIssueDelayApply(checkPara=checkParam4,issueDict=sIssuePara4)
        self.assertTrue(r, '验证失败')
        Log.LogOutput(message='延时设置-拒绝成功！')
        
#         #再次拒绝
#         Log.LogOutput(message='验证多次拒绝是否会返回错误信息')
#         response41=setDelay(issueDict=sIssuePara41)
#         self.assertFalse(response41.result, '再次拒绝会返回错误信息验证失败！')
#         Log.LogOutput(message='再次拒绝会返回错误信息验证成功')
        #再次申请延时，并批准
        Log.LogOutput(message='再次申请延时')
        response5=applyIssueDelay(issueDict=sIssuePara3,username=userInit['DftSheQuUser'])
        
        responseDict5=json.loads(response5.text)
        Log.LogOutput(message='验证街道层级批准延时功能')
        #设置设置延时-批准参数
        sIssuePara5={
            'mode':'setDelay',
            'issueCompleteDelay.id':responseDict5['id'],
            'issueCompleteDelay.organization.id':orgInit['DftSheQuOrgId'],
            'issueCompleteDelay.issue.id':rs['issueId'],
            'issueCompleteDelay.isAudit':'1',
            'issueCompleteDelay.orgId':orgInit['DftJieDaoOrgId'],
            'issueCompleteDelay.reason':sIssuePara41['issueCompleteDelay.reason'],
            'issueCompleteDelay.applyDays':sIssuePara41['issueCompleteDelay.applyDays'],
            'issueCompleteDelay.approvalDays':600
             }
        setDelay(issueDict=sIssuePara5)
        Log.LogOutput(message='正在验证批准延时功能')
        checkParam5=copy.deepcopy(checkParam)
        checkParam5['delayDays']=sIssuePara5['issueCompleteDelay.approvalDays']
        r=checkIssueDelayApply(checkPara=checkParam5,issueDict=sIssuePara4)
        self.assertTrue(r,'验证失败')
        Log.LogOutput(message='设置延时-批准成功！')
#         #再次批准
#         Log.LogOutput(message='验证多次批准是否返回错误信息')
#         result6=setDelay(issueDict=sIssuePara5)
#         self.assertFalse(result6.result, '多次重复批准返回错误信息验证失败')
#         Log.LogOutput(message='多次重复批准返回错误信息验证成功！')
        pass    
 
 
    '''
    @功能：我的事项-下辖全部事项-导出
    @ chenhui 2015-12-18
    '''      
    def testIssue_026(self):
        '''下辖全部事项-导出'''   
        #新增事件
        issueParam = copy.deepcopy(ShiJianChuLiPara.issueObject2)
        issueParam['issue.subject']='事件主题'+createRandomString()
        rs=ShiJianChuLiIntf.addIssue(issueDict=issueParam, username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(rs, '新增失败')
        #上报事件
        sIssuePara=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)
        sIssuePara['operation.dealOrg.id']=orgInit['DftJieDaoOrgId']
        sIssuePara['operation.issue.id']=rs['issueId']
        sIssuePara['keyId']=rs['issueStepId']      
        sIssuePara['operation.dealUserName']=userInit['DftJieDaoUserXM']
        sIssuePara['operation.mobile']=userInit['DftJieDaoUserSJ']
        sIssuePara['operation.content']='上报事件'
        sIssuePara['operation.targeOrg.id']=orgInit['DftQuOrgId']
        sIssuePara['themainOrgid']=orgInit['DftQuOrgId']        
        sIssuePara['dealCode']='41'#上报
         
        Log.LogOutput(message='街道上报事件中')
        result=dealIssue(issueDict=sIssuePara)
        self.assertTrue(result.result,'事件“普通上报”失败！')
        Log.LogOutput(message='事件上报成功')
        #区受理
        sIssuePara0={
                     'operation.dealOrg.id':orgInit['DftSheQuOrgId'],
                     'operation.issue.id':sIssuePara['operation.issue.id'],
                     'operation.dealUserName':userInit['DftSheQuUserXM'],
                     'operation.mobile':userInit['DftSheQuUserSJ'],
                     'dealCode':'61',
                     'keyId':sIssuePara['keyId']+1
                     }
        result0=dealIssue(issueDict=sIssuePara0,username=userInit['DftQuUser'])
        self.assertTrue(result0.result,'区受理失败！')
        Log.LogOutput(message='事件受理成功')
         
        #区交办给街道
        sIssuePara1=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)        
        sIssuePara1['operation.dealOrg.id']=orgInit['DftQuOrgId']
        sIssuePara1['operation.issue.id']=rs['issueId']
        sIssuePara1['keyId']=rs['issueStepId']+1      
        sIssuePara1['operation.dealUserName']=userInit['DftQuUserXM']
        sIssuePara1['operation.mobile']=userInit['DftQuUserSJ']
        sIssuePara1['operation.content']='普通交办事件'
        sIssuePara1['operation.targeOrg.id']=orgInit['DftJieDaoOrgId']
        sIssuePara1['themainOrgid']=orgInit['DftJieDaoOrgId']
        #交办状态代码       
        sIssuePara1['dealCode']='21'
        result1=dealIssue(issueDict=sIssuePara1,username=userInit['DftQuUser'])
        self.assertTrue(result1.result, '交办失败！')
        Log.LogOutput(message='事件交办成功')
        #街道受理
        sIssuePara2={
                     'operation.dealOrg.id':orgInit['DftSheQuOrgId'],
                     'operation.issue.id':sIssuePara['operation.issue.id'],
                     'operation.dealUserName':userInit['DftSheQuUserXM'],
                     'operation.mobile':userInit['DftSheQuUserSJ'],
                     'dealCode':'61',
                     'keyId':sIssuePara['keyId']+2
                     }
        result2=dealIssue(issueDict=sIssuePara2,username=userInit['DftJieDaoUser'])
         
#        print result2.text
        self.assertTrue(result2.result,'街道受理失败！')
        Log.LogOutput(message='事件受理成功')
        #街道结案
        sIssuePara3=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)        
        sIssuePara3['operation.dealOrg.id']=orgInit['DftJieDaoOrgId']
        sIssuePara3['operation.issue.id']=rs['issueId']
        sIssuePara3['keyId']=rs['issueStepId']+2      
        sIssuePara3['operation.dealUserName']=userInit['DftJieDaoUserXM']
        sIssuePara3['operation.mobile']=userInit['DftJieDaoUserSJ']
        sIssuePara3['operation.content']='办结事件'
        sIssuePara3['operation.targeOrg.id']=orgInit['DftJieDaoOrgId']
        sIssuePara3['themainOrgid']=orgInit['DftJieDaoOrgId']
        sIssuePara3['dealCode']='31'
        sIssuePara['dealTime']=Time.getCurrentDate()
        sIssuePara['transferToType']='true'
        result3=dealIssue(issueDict=sIssuePara3)
        self.assertTrue(result3.result, '事件结案失败!')
        Log.LogOutput(message='事件结案成功')
        #设置导出参数
         
        dlPara={
                'organization.id':orgInit['DftJieDaoOrgId'],
                'fastSearchType':'all',
                'searchYear':time.strftime('%Y'),
                'page':'1',
                '_search':'false',
                'rows':'20',
                'sidx':'lastDealDate',
                'sord':'desc',
                'pageOnly':'true'
                }
        dlIssue(issueDict=dlPara)
        #定义两个数组，用于存储serialNumber和subject内容
        sum=[]
        sub=[]
        sum.append(rs['serialNumber'])#.decode('utf-8'))
        sub.append(rs['subject'])
        checkPara={
                 'serialNumber':sum,
                 'subject':sub,
                   }
        r=checkDlIssueList(checkPara=checkPara)
        self.assertTrue(r, '导出数据匹配失败')
        Log.LogOutput(message='导出单条数据成功！')
        #新增29条事件，并存储其主题值和序列号
        for i in range(1,30):
            issueParam['issue.subject']='事件主题'+createRandomString()
            rs=addIssue(issueDict=issueParam)
            checkPara['serialNumber'].append(rs['serialNumber'])    #sun
            checkPara['subject'].append(rs['subject'])                      #sub
        #导出本页数据，并验证每行数据是否正确
        dlIssue(issueDict=dlPara)
#         rowNum=getExcelCellRowNum(u'下辖全部事项导出清单.xls',u'下辖事项清单')
        rowNum=getExcelCellRowNum('downAllIssuesExportSheet.xls',u'下辖事项清单')
        print rowNum
        self.assertEqual(rowNum, 20, '导出本页数据错误')
        Log.LogOutput(message='导出本页数目正确')
             
        #验证导出全部数据是否正确
        Log.LogOutput(message='验证导出全部数据功能是否正确')
        dlPara['pageOnly']='false'
        dlIssue(issueDict=dlPara)
        rowNum=getExcelCellRowNum('downAllIssuesExportSheet.xls',u'下辖事项清单')
        #获取下辖全部事件列表中总的记录数
        downAllIssueListPara={
                                'organization.id':orgInit['DftJieDaoOrgId'],
                                'page':'1',
                                '_search':'false',
                                'rows':'20',
                                'sidx':'createDate',
                                'sord':'desc'
                              }
        totalIssueNum=getDownAllIssueTotalNum(issueDict=downAllIssueListPara)
        self.assertEqual(rowNum, totalIssueNum, '导出全部事件数据错误!')
        Log.LogOutput(message='导出全部事件数据正确')
        
        #验证空查询后导出全部数据
        rs=ShiJianChuLiIntf.addIssue(issueDict=issueParam, username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(rs, '新增失败')
        
        Log.LogOutput(message='验证查询后导出功能')
        #设置查询参数
        searchPara=copy.deepcopy(dowonAllIssueSearchPara)
        searchPara['searchIssueVo.targeOrgId']=orgInit['DftJieDaoOrgId'],
        searchPara['searchIssueVo.dealOrgId']=orgInit['DftJieDaoOrgId']
        searchPara['searchIssueVo.serialNumber']=rs['serialNumber']
        
        Log.LogOutput(LogLevel.DEBUG,'查询参数为  '+searchPara['searchIssueVo.serialNumber'])     
        r=searchDownAllIssue(issueDict=searchPara)
        Log.LogOutput(LogLevel.DEBUG,'查询结果返回  '+r.text)
        #导出全部数据
        searchPara['pageOnly']='false'      
        r2=dlIssue(issueDict=searchPara)
        Log.LogOutput(LogLevel.DEBUG,r2.result)
        #获取导出的数据数目
        rowNum=getExcelCellRowNum('downAllIssuesExportSheet.xls',u'下辖事项清单')
        self.assertEqual(rowNum,1, '查询服务单号后导出功能异常')
        Log.LogOutput(message='查询服务单号后导出功能正常')
        pass
    
    
    '''
    @功能：我的事项-绩效考核-其他打分，涉及事件的上报、交办和结案操作时，会自动加分，无需job，回退不加分，但是有记录；新增、阅读和受理都没有记录也不加分
    @ chenhui 2015-12-24
    '''      
    def testIssue_027(self):
        '''我的事项-绩效考核-其他打分'''
        if Global.simulationEnvironment is False:
    #         clearTable(tableName='regradedPoints')#行政部门绩效考核打分表
            orgcode=getDbQueryResult(dbCommand ="select o.orginternalcode from organizations o where o.orgname='测试自动化省'")+'%'
            exeDbQuery(dbCommand ="delete from  regradedPoints r where r.targeorginternalcode like '%s'"%orgcode)
            #设置绩效考核督办扣分标准，只有首次设置时，issueAccessConfig.id为空
            sIssuePara1={
                        'issueAccessConfig.createOrg.id':orgInit['DftJieDaoOrgId'],
                        'issueAccessConfig.id': getDbQueryResult(dbCommand = "select t.id from issueAccessConfig t where t.createOrgId=%s"%orgInit['DftJieDaoOrgId']),
                        'issueAccessConfig.yellowCardScores':3,
                        'issueAccessConfig.redCardScores':6,
                        'issueAccessConfig.normalScores':2,
                        }
            response=setScoreStandard(issueDict=sIssuePara1)
            self.assertTrue(response.result,'绩效考核扣分标准设置失败！')
            Log.LogOutput(LogLevel.INFO, '街道层级绩效考核扣分标准设置成功！')
            
            #验证正常新增事件，不加分
            #社区新增事件
            Log.LogOutput(message='验证正常新增事件，不加分')
            issueParam = copy.deepcopy(ShiJianChuLiPara.issueObject2) 
            rs=addIssue(issueDict=issueParam, username=userInit['DftSheQuUser'], password='11111111')
            self.assertTrue(rs,'新增事件失败！' )
            para={
                  'year':time.strftime("%Y"),
                  'month':time.strftime("%m"),
                  'internalId':'0',#0代表行政部门
                  'targeOrgId':orgInit['DftJieDaoOrgId'],
                  '_search':'false',
                  'rows':'20',
                  'page':'1',
                  'sidx':'vOrg.id',
                  'sord':'asc',
                  }
            rsDict=getRegradedPoint(issuePara=para)
            self.assertEqual(rsDict['assessmentUser'],0, '事件新增操作后，打分结果错误')
            Log.LogOutput(message='事件“新增”操作后绩效考核自动打分结果正确,分数是：'+str(rsDict['assessmentUser']))
              
            #验证办理中操作后，是否会加分
            Log.LogOutput(message='验证处理中操作后，不加分')
            sIssuePara=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)        
            sIssuePara['operation.dealOrg.id']=orgInit['DftSheQuOrgId']
            sIssuePara['operation.issue.id']=rs['issueId']
            sIssuePara['keyId']=rs['issueStepId']      
            sIssuePara['operation.dealUserName']=userInit['DftSheQuUserXM']
            sIssuePara['operation.mobile']=userInit['DftSheQuUserSJ']
            sIssuePara['operation.content']='事件处理'      
            sIssuePara['dealCode']='1'#办理中
            result=dealIssue(issueDict=sIssuePara,username=userInit['DftSheQuUser'])
            self.assertTrue(result.result, '事件操作失败!')
            Log.LogOutput(message='事件处理中操作成功！验证是否加分')
            rsDict=getRegradedPoint(issuePara=para)
            self.assertEqual(rsDict['assessmentUser'],0, '办理中操作后，打分结果错误')
            Log.LogOutput(message='事件“办理中”操作后绩效考核自动打分结果正确，分数是：'+str(rsDict['assessmentUser']))
            
            #验证正常办结后是否加分，加分
            Log.LogOutput(message='验证正常办结后是否自动加分')
            sIssuePara['dealCode']='31'#结案
            sIssuePara['dealTime']=Time.getCurrentDate()
            sIssuePara['transferToType']='true'
            result=dealIssue(issueDict=sIssuePara,username=userInit['DftSheQuUser'])
            self.assertTrue(result.result, '事件办结操作失败!')
            Log.LogOutput(message='事件结案操作成功，正在验证自动打分结果是否正确')
            rsDict=getRegradedPoint(issuePara=para)
            self.assertEqual(rsDict['assessmentUser'],sIssuePara1['issueAccessConfig.normalScores'], '结案操作后，打分结果错误')
            Log.LogOutput(message='事件“结案”操作后绩效考核自动打分结果正确,分数是：'+str(rsDict['assessmentUser']))
            
            #验证社区上报事件，加分
            Log.LogOutput(message='验证正常上报后是否自动加分')
            rs3=addIssue(issueDict=issueParam, username=userInit['DftSheQuUser'], password='11111111')
            sIssuePara3=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)
            sIssuePara3['operation.dealOrg.id']=orgInit['DftSheQuOrgId']
            sIssuePara3['operation.issue.id']=rs3['issueId']
            sIssuePara3['keyId']=rs3['issueStepId']      
            sIssuePara3['operation.dealUserName']=userInit['DftSheQuUserXM']
            sIssuePara3['operation.mobile']=userInit['DftSheQuUserSJ']
            sIssuePara3['operation.content']='上报事件'
            sIssuePara3['operation.targeOrg.id']=orgInit['DftJieDaoOrgId']
            sIssuePara3['themainOrgid']=orgInit['DftJieDaoOrgId']        
            sIssuePara3['dealCode']='41'#上报
            result3=dealIssue(issueDict=sIssuePara3,username=userInit['DftSheQuUser'])
            self.assertTrue(result3.result, '事件上报操作失败!')
            Log.LogOutput(message='事件上报操作成功，正在验证自动打分结果是否正确')
            rsDict=getRegradedPoint(issuePara=para)
            self.assertEqual(rsDict['assessmentUser'],sIssuePara1['issueAccessConfig.normalScores']*2, '上报操作后，打分结果错误')
            Log.LogOutput(message='事件“上报”操作后绩效考核自动打分结果正确,分数是：'+str(rsDict['assessmentUser']))
            
            #验证社区交办事件，加分
            Log.LogOutput(message='验证正常交办后是否自动加分')
            rs4=addIssue(issueDict=issueParam, username=userInit['DftSheQuUser'], password='11111111')
            sIssuePara4=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)        
            sIssuePara4['operation.dealOrg.id']=orgInit['DftSheQuOrgId']
            sIssuePara4['operation.issue.id']=rs4['issueId']
            sIssuePara4['keyId']=rs4['issueStepId']      
            sIssuePara4['operation.dealUserName']=userInit['DftSheQuUserXM']
            sIssuePara4['operation.mobile']=userInit['DftSheQuUserSJ']
            sIssuePara4['operation.content']='普通交办事件'
            sIssuePara4['operation.targeOrg.id']=orgInit['DftWangGeOrgId']
            sIssuePara4['themainOrgid']=orgInit['DftWangGeOrgId']
            #交办状态代码       
            sIssuePara4['dealCode']='21'
            result4=dealIssue(issueDict=sIssuePara4,username=userInit['DftSheQuUser'])
            self.assertTrue(result4.result, '事件交办操作失败!')
            Log.LogOutput(message='事件交办操作成功，正在验证自动打分结果是否正确')
            rsDict=getRegradedPoint(issuePara=para)
            self.assertEqual(rsDict['assessmentUser'],sIssuePara1['issueAccessConfig.normalScores']*3, '交办操作后，打分结果错误')
            Log.LogOutput(message='事件“交办”操作后绩效考核自动打分结果正确,分数是：'+str(rsDict['assessmentUser']))
            
            #验证社区受理事件，不加分
            Log.LogOutput(message='验证正常受理是否自动加分')
            Log.LogOutput(message='街道新增事件，并交办给社区')
            rs5=addIssue(issueDict=issueParam, username=userInit['DftJieDaoUser'], password='11111111')
            sIssuePara5=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)        
            sIssuePara5['operation.dealOrg.id']=orgInit['DftJieDaoOrgId']
            sIssuePara5['operation.issue.id']=rs5['issueId']
            sIssuePara5['keyId']=rs5['issueStepId']      
            sIssuePara5['operation.dealUserName']=userInit['DftJieDaoUserXM']
            sIssuePara5['operation.mobile']=userInit['DftJieDaoUserSJ']
            sIssuePara5['operation.content']='普通交办事件'
            sIssuePara5['operation.targeOrg.id']=orgInit['DftSheQuOrgId']
            sIssuePara5['themainOrgid']=orgInit['DftSheQuOrgId']
            #交办状态代码       
            sIssuePara5['dealCode']='21'
            result5=dealIssue(issueDict=sIssuePara5,username=userInit['DftJieDaoUser'])
            self.assertTrue(result5.result, '事件交办操作失败!')
            Log.LogOutput(message='社区受理事件中..')
            sIssuePara52={
                         'operation.dealOrg.id':orgInit['DftSheQuOrgId'],
                         'operation.issue.id':rs5['issueId'],
                         'operation.dealUserName':userInit['DftSheQuUserXM'],
                         'operation.mobile':userInit['DftSheQuUserSJ'],
                         'dealCode':'61',
                         'keyId':sIssuePara5['keyId']+1
                         }
            result52=dealIssue(issueDict=sIssuePara52,username=userInit['DftSheQuUser'])
            self.assertTrue(result52.result,'社区受理失败！')
            Log.LogOutput(message='事件受理操作成功，正在验证自动打分结果是否正确')
            rsDict=getRegradedPoint(issuePara=para)
            self.assertEqual(rsDict['assessmentUser'],sIssuePara1['issueAccessConfig.normalScores']*3, '受理操作后，打分结果错误')
            Log.LogOutput(message='事件“受理”操作后绩效考核自动打分结果正确,分数是：'+str(rsDict['assessmentUser']))
            
            #验证社区回退事件，不加分
            Log.LogOutput(message='验证正常回退后是否自动加分')
            #设置回退参数
            sIssuePara6=copy.deepcopy(ShiJianChuLiPara.dealIssuePara) 
            sIssuePara6['operation.dealOrg.id']=orgInit['DftSheQuOrgId']
            sIssuePara6['operation.issue.id']=sIssuePara52['operation.issue.id']
            sIssuePara6['keyId']=sIssuePara52['keyId']
            sIssuePara6['operation.dealUserName']=userInit['DftSheQuUserXM'],
            sIssuePara6['operation.mobile']=userInit['DftSheQuUserSJ']
            sIssuePara6['dealCode']='200'
            sIssuePara6['operation.content']='回退事件'
            result6=dealIssue(issueDict=sIssuePara6,username=userInit['DftSheQuUser'])
            self.assertTrue(result6.result,'社区回退失败！')
            Log.LogOutput(message='事件回退操作成功，正在验证自动打分结果是否正确')
            rsDict=getRegradedPoint(issuePara=para)
            self.assertEqual(rsDict['assessmentUser'],sIssuePara1['issueAccessConfig.normalScores']*3, '回退操作后，打分结果错误')
            Log.LogOutput(message='事件“回退”操作后绩效考核自动打分结果正确,分数是：'+str(rsDict['assessmentUser']))
            
            #清空打分表
    #         clearTable(tableName='regradedPoints')#行政部门绩效考核打分表
        else:
            Log.LogOutput( message='仿真环境，跳过测试')
        pass
    
    '''
    @功能：我的事项-绩效考核-事件受理黄牌、红牌自动督办自动扣分
    @ chenhui 2015-12-27
    '''         
    def testIssue_028(self):
        '''事件受理黄牌、红牌自动督办自动扣分'''
        if Global.simulationEnvironment is False:        
            #初始化数据
            #清空job监控表
            clearTable(tableName='JOBMONITOR')#job监控表
            #清空打分表
    #         clearTable(tableName='regradedPoints')#行政部门绩效考核打分表
            orgcode=getDbQueryResult(dbCommand ="select o.orginternalcode from organizations o where o.orgname='测试自动化省'")+'%'
            exeDbQuery(dbCommand ="delete from  regradedPoints r where r.targeorginternalcode like '%s'"%orgcode)
            #设置绩效考核督办扣分标准，只有首次设置时，issueAccessConfig.id为空
            sIssuePara1={
                        'issueAccessConfig.createOrg.id':orgInit['DftJieDaoOrgId'],
                        'issueAccessConfig.id': getDbQueryResult(dbCommand = "select t.id from issueAccessConfig t where t.createOrgId=%s"%orgInit['DftJieDaoOrgId']),
                        'issueAccessConfig.yellowCardScores':3,
                        'issueAccessConfig.redCardScores':6,
                        'issueAccessConfig.normalScores':2,
                        }
            response=setScoreStandard(issueDict=sIssuePara1)
            self.assertTrue(response.result,'绩效考核扣分标准设置失败！')
            Log.LogOutput(LogLevel.INFO, '街道层级绩效考核扣分标准设置成功！')
            #设置行政部门时限标准
            sIssuePara2={
                        'mode':'add',
                        'timeLimitStandard.id':'',
                        'timeLimitStandard.pageType':'Administrative',
                        'timeLimitStandard.orgType.id':'',
                        'timeLimitStandard.org.id':orgInit['DftJieDaoOrgId'],
                        'timeLimitStandard.isDirectlyJurisdiction':'true',
                        'timeLimitStandard.yellowLimitAccept':'1',
                        'timeLimitStandard.yellowLimitHandle':'3',
                        'timeLimitStandard.redLimitAccept':'5',
                        'timeLimitStandard.redLimitHandle':'7',
                        'timeLimitStandard.remark':'备注',
                         }
            response2=addTimeLimitStandard(issueDict=sIssuePara2)
    #         self.assertTrue(response2.result,'绩效考核行政部门时限标准设置失败！')
            
            Log.LogOutput(LogLevel.INFO, '街道层级绩效考核行政部门时限标准设置成功！')
             
            Log.LogOutput(message='验证事件受理黄牌督办')
            #街道新增事件
            Log.LogOutput(message='街道新增事件，并交办给社区')
            issueParam = copy.deepcopy(ShiJianChuLiPara.issueObject2) 
            rs=addIssue(issueDict=issueParam, username=userInit['DftJieDaoUser'], password='11111111')
            sIssuePara=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)        
            sIssuePara['operation.dealOrg.id']=orgInit['DftJieDaoOrgId']
            sIssuePara['operation.issue.id']=rs['issueId']
            sIssuePara['keyId']=rs['issueStepId']      
            sIssuePara['operation.dealUserName']=userInit['DftJieDaoUserXM']
            sIssuePara['operation.mobile']=userInit['DftJieDaoUserSJ']
            sIssuePara['operation.content']='普通交办事件'
            sIssuePara['operation.targeOrg.id']=orgInit['DftSheQuOrgId']
            sIssuePara['themainOrgid']=orgInit['DftSheQuOrgId']
            #交办状态代码       
            sIssuePara['dealCode']='21'
            result=dealIssue(issueDict=sIssuePara,username=userInit['DftJieDaoUser'])
            self.assertTrue(result.result, '事件交办操作失败!')
            Log.LogOutput(message='交办成功，验证超时自动督办功能')
    #         print getDbQueryResult(dbCommand = "select lastdealdate from issues s where s.id='%s'"%rs['issueId'])
            updDealTime=moveTime(standardTime=getLinuxDateAndTime(),addDay=2,addMinute=1,moveType=TimeMoveType.MINUS,calcType=TimeCalcType.WORKDAY)
            #日期格式中的后半句分钟，如果也是mm，就跟前面的月份重复了，oracle中庸mi代替mm
            dbc="update issueSteps  s set s.entrydate =to_date('%s','yyyy-MM-dd HH24:mi:ss') where s.issue='%s'"%(updDealTime,rs['issueId'])
    #        dbc="update issues s set s.lastdealdate =to_date('%s','yyyy-MM-dd HH24:mi:ss') where s.id='%s'"%(updDealTime,rs['issueId'])
            exeDbQuery(dbCommand=dbc)
            newDealTime= getDbQueryResult(dbCommand = "select entrydate from issueSteps  s where s.issue='%s'"%rs['issueId'])
            Log.LogOutput(LogLevel.DEBUG,'修改后的lastdealdate时间是：'+str(newDealTime))
            #运行job
            jobTimePara={
                         'task.Data':setJobDelayTime(seconds='10'),
                         'task.name':'issueOvertimeHandlerJob',
                         'job.name':'issueOvertimeHandlerJob'
                         }
            runJob(jobPara=jobTimePara)
    
            #验证自动督办是否成功
            Log.LogOutput(message='正在验证自动督办是否成功..')
            sIssuePara3=copy.deepcopy(superviseIssuesList)
            sIssuePara3['issueVO.createOrg.id']=orgInit['DftQuOrgId']
            checkPara3={
                        'issueId':rs['issueId'],
                        'dealState':110,
                        'supervisionState':100,#黄牌督办标志
                        }
            result3=checkSuperviseIssue(checkPara=checkPara3,issueDict=sIssuePara3,username=userInit['DftQuUser'])
            self.assertTrue(result3, '自动督办验证失败！')
            Log.LogOutput(message='黄牌自动督办成功！验证督办后的打分功能')
            #验证黄牌督办后扣分是否正确
            para={
                  'year':time.strftime("%Y"),
                  'month':time.strftime("%m"),
                  'internalId':'0',#0代表行政部门
                  'targeOrgId':orgInit['DftJieDaoOrgId'],
                  '_search':'false',
                  'rows':'20',
                  'page':'1',
                  'sidx':'vOrg.id',
                  'sord':'asc',
                  }
            rsDict=getRegradedPoint(issuePara=para)
            self.assertEqual(rsDict['yellowAmout'],sIssuePara1['issueAccessConfig.yellowCardScores'], '事件超时受理黄牌督办操作后，打分结果错误')
            Log.LogOutput(message='事件受理黄牌自动督办后绩效考核自动打分结果正确,分数是：'+str(rsDict['yellowAmout']))
             
             
            #验证红牌受理自动督办和打分
            #改成6天前
            updDealTime2=moveTime(standardTime=getLinuxDateAndTime(),addDay=6,addMinute=1,moveType=TimeMoveType.MINUS,calcType=TimeCalcType.WORKDAY)
            #日期格式中的后半句分钟，如果也是mm，就跟前面的月份重复了，oracle中用mi代替mm
            dbc2="update issueSteps  s set s.entrydate =to_date('%s','yyyy-MM-dd HH24:mi:ss') where s.issue='%s'"%(updDealTime2,rs['issueId'])
    #        dbc="update issues s set s.lastdealdate =to_date('%s','yyyy-MM-dd HH24:mi:ss') where s.id='%s'"%(updDealTime,rs['issueId'])
            exeDbQuery(dbCommand=dbc2)
            newDealTime2= getDbQueryResult(dbCommand = "select entrydate from issueSteps  s where s.issue='%s'"%rs['issueId'])
            Log.LogOutput(LogLevel.DEBUG,'修改后的lastdealdate时间是：'+str(newDealTime2))
    #      设置JOB延后执行时间参数，延后·10s
            jobTimePara={
                         'task.Data':setJobDelayTime(seconds='10'),
                         'task.name':'issueOvertimeHandlerJob',
                         'job.name':'issueOvertimeHandlerJob'
                         }
            runJob(jobPara=jobTimePara)
            #验证受理自动督办是否成功
            Log.LogOutput(message='正在验证受理自动督办是否成功..')
            sIssuePara4=copy.deepcopy(superviseIssuesList)
            sIssuePara4['issueVO.createOrg.id']=orgInit['DftQuOrgId']
            checkPara4={
                        'issueId':rs['issueId'],
                        'dealState':110,
                        'supervisionState':200
                        #红牌督办标志
                        }
            #等待10s后再检查，这个地方有延迟
            time.sleep(10)
            result4=checkSuperviseIssue(checkPara=checkPara4,issueDict=sIssuePara4,username=userInit['DftQuUser'])
            self.assertTrue(result4, '自动督办验证失败！')
            Log.LogOutput(message='红牌自动督办成功！验证督办后的打分功能')
            #验证受理红牌督办后扣分是否正确
            para={
                  'year':time.strftime("%Y"),
                  'month':time.strftime("%m"),
                  'internalId':'0',#0代表行政部门
                  'targeOrgId':orgInit['DftJieDaoOrgId'],
                  '_search':'false',
                  'rows':'20',
                  'page':'1',
                  'sidx':'vOrg.id',
                  'sord':'asc',
                  }
            rsDict=getRegradedPoint(issuePara=para)
            self.assertEqual(rsDict['redAmout'],sIssuePara1['issueAccessConfig.redCardScores'], '事件超时受理红牌督办操作后，打分结果错误')
            Log.LogOutput(message='事件受理红牌自动督办后绩效考核自动打分结果正确,分数是：'+str(rsDict['redAmout']))
        else:
            Log.LogOutput(message='仿真环境，跳过测试')
        pass
    

    '''
    @功能：我的事项-绩效考核-事件办理中自动黄牌、红牌督办和自动扣分
    @ chenhui 2015-12-28
    '''         
    def testIssue_029(self):
        '''事件办理中自动黄牌、红牌督办和自动扣分'''
        if Global.simulationEnvironment is False:
            #初始化数据
            #清空job监控表
            clearTable(tableName='JOBMONITOR')#job监控表
            #清空打分表
    #         clearTable(tableName='regradedPoints')#行政部门绩效考核打分表
            orgcode=getDbQueryResult(dbCommand ="select o.orginternalcode from organizations o where o.orgname='测试自动化省'")+'%'
            exeDbQuery(dbCommand ="delete from  regradedPoints r where r.targeorginternalcode like '%s'"%orgcode)
            #设置绩效考核督办扣分标准，只有首次设置时，issueAccessConfig.id为空
            sIssuePara1={
                        'issueAccessConfig.createOrg.id':orgInit['DftJieDaoOrgId'],
                        'issueAccessConfig.id': getDbQueryResult(dbCommand = "select t.id from issueAccessConfig t where t.createOrgId=%s"%orgInit['DftJieDaoOrgId']),
                        'issueAccessConfig.yellowCardScores':3,
                        'issueAccessConfig.redCardScores':6,
                        'issueAccessConfig.normalScores':2,
                        }
            response=setScoreStandard(issueDict=sIssuePara1)
            self.assertTrue(response.result,'绩效考核扣分标准设置失败！')
            Log.LogOutput(LogLevel.INFO, '街道层级绩效考核扣分标准设置成功！')
            #设置行政部门时限标准
            sIssuePara2={
                        'mode':'add',
                        'timeLimitStandard.id':'',
                        'timeLimitStandard.pageType':'Administrative',
                        'timeLimitStandard.orgType.id':'',
                        'timeLimitStandard.org.id':orgInit['DftJieDaoOrgId'],
                        'timeLimitStandard.isDirectlyJurisdiction':'true',
                        'timeLimitStandard.yellowLimitAccept':'1',
                        'timeLimitStandard.yellowLimitHandle':'3',
                        'timeLimitStandard.redLimitAccept':'5',
                        'timeLimitStandard.redLimitHandle':'7',
                        'timeLimitStandard.remark':'备注',
                         }
            response2=addTimeLimitStandard(issueDict=sIssuePara2)
    #         self.assertTrue(response2.result,'绩效考核行政部门时限标准设置失败！')
            Log.LogOutput(LogLevel.INFO, '街道层级绩效考核行政部门时限标准设置成功！')
            
            Log.LogOutput(message='验证事件受理黄牌督办')
            #街道新增事件
            Log.LogOutput(message='街道新增事件，并交办给社区')
            issueParam = copy.deepcopy(ShiJianChuLiPara.issueObject2) 
            rs=addIssue(issueDict=issueParam, username=userInit['DftJieDaoUser'], password='11111111')
            sIssuePara=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)        
            sIssuePara['operation.dealOrg.id']=orgInit['DftJieDaoOrgId']
            sIssuePara['operation.issue.id']=rs['issueId']
            sIssuePara['keyId']=rs['issueStepId']      
            sIssuePara['operation.dealUserName']=userInit['DftJieDaoUserXM']
            sIssuePara['operation.mobile']=userInit['DftJieDaoUserSJ']
            sIssuePara['operation.content']='普通交办事件'
            sIssuePara['operation.targeOrg.id']=orgInit['DftSheQuOrgId']
            sIssuePara['themainOrgid']=orgInit['DftSheQuOrgId']
            #交办状态代码       
            sIssuePara['dealCode']='21'
            result=dealIssue(issueDict=sIssuePara,username=userInit['DftJieDaoUser'])
            self.assertTrue(result.result, '事件交办操作失败!')
            Log.LogOutput(message='交办成功，等待社区受理')
            #社区受理事件
            #受理参数设置
            sIssuePara22={
                         'operation.dealOrg.id':orgInit['DftSheQuOrgId'],
                         'operation.issue.id':sIssuePara['operation.issue.id'],
                         'operation.dealUserName':userInit['DftSheQuUserXM'],
                         'operation.mobile':userInit['DftSheQuUserSJ'],
                         'dealCode':'61',
                         'keyId':sIssuePara['keyId']+1
                         }
            result22=dealIssue(issueDict=sIssuePara22,username=userInit['DftSheQuUser'])
            self.assertTrue(result22.result,'事件交办后受理失败！')
            Log.LogOutput(message='事件受理成功')
            #修改事件步骤字段的lastdealdate
            oldDealTime=getDbQueryResult(dbCommand = "select lastdealdate from issuesteps s where s.issue='%s'"%rs['issueId'])
            Log.LogOutput(LogLevel.DEBUG,'修改前的lastdealdate时间是：'+str(oldDealTime))
            updDealTime=moveTime(standardTime=getLinuxDateAndTime(),addDay=4,addMinute=1,moveType=TimeMoveType.MINUS,calcType=TimeCalcType.WORKDAY)
            #日期格式中的后半句分钟，如果也是mm，就跟前面的月份重复了，oracle中用mi代替mm
            dbc="update issuesteps  s set s.lastdealdate =to_date('%s','yyyy-MM-dd HH24:mi:ss') where s.issue='%s'"%(updDealTime,rs['issueId'])
    #        dbc="update issues s set s.lastdealdate =to_date('%s','yyyy-MM-dd HH24:mi:ss') where s.id='%s'"%(updDealTime,rs['issueId'])
            exeDbQuery(dbCommand=dbc)
            newDealTime= getDbQueryResult(dbCommand = "select lastdealdate from issueSteps  s where s.issue='%s'"%rs['issueId'])
            Log.LogOutput(LogLevel.DEBUG,'修改后的lastdealdate时间是：'+str(newDealTime))
                    
    #      设置JOB延后执行时间参数，延后·10s
            jobTimePara={
                         'task.Data':setJobDelayTime(seconds='10'),
                         'task.name':'issueOvertimeHandlerJob',
                         'job.name':'issueOvertimeHandlerJob'
                         }
            runJob(jobPara=jobTimePara)
            #验证自动督办是否成功
            Log.LogOutput(message='正在验证自动督办是否成功..')
            sIssuePara3=copy.deepcopy(superviseIssuesList)
            sIssuePara3['issueVO.createOrg.id']=orgInit['DftQuOrgId']
            checkPara3={
                        'issueId':rs['issueId'],
                        'dealState':120,
                        'supervisionState':100,
                        }
            result3=checkSuperviseIssue(checkPara=checkPara3,issueDict=sIssuePara3,username=userInit['DftQuUser'])
            self.assertTrue(result3, '自动督办验证失败！')
            Log.LogOutput(message='黄牌自动督办成功！验证督办后的打分功能')
            #验证事件办理中黄牌督办后扣分是否正确
            para={
                  'year':time.strftime("%Y"),
                  'month':time.strftime("%m"),
                  'internalId':'0',#0代表行政部门
                  'targeOrgId':orgInit['DftJieDaoOrgId'],
                  '_search':'false',
                  'rows':'20',
                  'page':'1',
                  'sidx':'vOrg.id',
                  'sord':'asc',
                  }
            rsDict=getRegradedPoint(issuePara=para)
            self.assertEqual(rsDict['yellowAmout'],sIssuePara1['issueAccessConfig.yellowCardScores'], '事件超时办理中黄牌督办操作后，打分结果错误')
            Log.LogOutput(message='事件办理中黄牌自动督办后绩效考核自动打分结果正确,分数是：'+str(rsDict['yellowAmout']))
            #验证事件办理中红牌督办后扣分是否正确
            #改成8天前
            updDealTime2=moveTime(standardTime=getLinuxDateAndTime(),addDay=8,addMinute=1,moveType=TimeMoveType.MINUS,calcType=TimeCalcType.WORKDAY)
            #日期格式中的后半句分钟，如果也是mm，就跟前面的月份重复了，oracle中用mi代替mm
            dbc2="update issueSteps  s set s.lastdealdate =to_date('%s','yyyy-MM-dd HH24:mi:ss') where s.issue='%s'"%(updDealTime2,rs['issueId'])
    #        dbc="update issues s set s.lastdealdate =to_date('%s','yyyy-MM-dd HH24:mi:ss') where s.id='%s'"%(updDealTime,rs['issueId'])
            exeDbQuery(dbCommand=dbc2)
            newDealTime2= getDbQueryResult(dbCommand = "select lastdealdate from issueSteps  s where s.issue='%s'"%rs['issueId'])
            Log.LogOutput(LogLevel.DEBUG,'修改后的lastdealdate时间是：'+str(newDealTime2))
            
    #      设置JOB延后执行时间参数，默认延后30s
            jobTimePara={
                         'task.Data':setJobDelayTime(),
                         'task.name':'issueOvertimeHandlerJob',
                         'job.name':'issueOvertimeHandlerJob'
                         }
            runJob(jobPara=jobTimePara)
            #验证事件办理中自动督办是否成功
            Log.LogOutput(message='正在验证办理中自动督办是否成功..')
            sIssuePara4=copy.deepcopy(superviseIssuesList)
            sIssuePara4['issueVO.createOrg.id']=orgInit['DftQuOrgId']
            checkPara4={
                        'issueId':rs['issueId'],
                        'dealState':120,
                        'supervisionState':200,#红牌督办标志
                        }
            time.sleep(30)
            result4=checkSuperviseIssue(checkPara=checkPara4,issueDict=sIssuePara4,username=userInit['DftQuUser'])
            self.assertTrue(result4, '自动督办验证失败！')
            Log.LogOutput(message='红牌自动督办成功！验证督办后的打分功能')
            #验证受理红牌督办后扣分是否正确
            para={
                  'year':time.strftime("%Y"),
                  'month':time.strftime("%m"),
                  'internalId':'0',#0代表行政部门
                  'targeOrgId':orgInit['DftJieDaoOrgId'],
                  '_search':'false',
                  'rows':'20',
                  'page':'1',
                  'sidx':'vOrg.id',
                  'sord':'asc',
                  }
            rsDict=getRegradedPoint(issuePara=para)
            self.assertEqual(rsDict['redAmout'],sIssuePara1['issueAccessConfig.redCardScores'], '事件超时受理红牌督办操作后，打分结果错误')
            Log.LogOutput(message='事件办理中红牌自动督办后绩效考核自动打分结果正确,分数是：'+str(rsDict['redAmout']))
        else:
            Log.LogOutput(message='仿真环境，跳过测试')
        pass
    
    def tearDown(self):    
        pass

if  __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    suite = unittest.TestSuite()
#    suite.addTest(Shijianchuli("testHttpGet"))
#    suite.addTest(Shijianchuli("testIssueAdd_Upd_Del"))
    suite.addTest(Shijianchuli("testIssue_029"))
#    suite.addTest(Shijianchuli("testHttpPost"))
    results = unittest.TextTestRunner().run(suite)
    pass
