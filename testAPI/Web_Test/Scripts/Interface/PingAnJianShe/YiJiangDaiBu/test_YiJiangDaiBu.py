# -*- coding:UTF-8 -*-
'''
Created on 2015-11-18

@author: N-266
'''
from __future__ import unicode_literals
import unittest
import copy
from Interface.PingAnJianShe.Common import CommonIntf
from CONFIG import InitDefaultPara
from CONFIG.InitDefaultPara import orgInit, userInit
from COMMON import Time, CommonUtil
from Interface.PingAnJianShe.YiJiangDaiBu import YiJiangDaiBuPara, \
    YiJiangDaiBuIntf
from Interface.PingAnJianShe.SystemMgr import SystemMgrIntf
class YiJingDaiBu(unittest.TestCase):
    def setUp(self):
        SystemMgrIntf.initEnv()
        YiJiangDaiBuIntf.deleteAllReward()
        pass
    def tearDown(self):        
        pass
    def testReward_01(self):#以奖代补>数据录入情况，申请
        '''以奖代补>数据录入情况>申请'''
        #新增事件
        issueParam = copy.deepcopy(YiJiangDaiBuPara.issueObject2) 
        issueParam['issue.occurDate']=Time.getCurrentDate()
        issueParam['issue.subject'] = '事件主题%s' % CommonUtil.createRandomString()
        responseDict = YiJiangDaiBuIntf.addIssue(issueDict=issueParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict, '新增事件失败')
        
        #在以奖代补里面申请
        applyParam=copy.deepcopy(YiJiangDaiBuPara.ApplyReward)
        applyParam['rewardToSubsidies[0].userId']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.name='%s'" % InitDefaultPara.userInit['DftWangGeUserXM'])
        applyParam['rewardToSubsidies[0].orgId']=orgInit['DftWangGeOrgId']
        applyParam['rewardToSubsidies[0].serviceNumber']='0'
        applyParam['issueIdsStr']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from ISSUES t where t.subject='"+issueParam['issue.subject']+"'")
        applyParam['content']='申请内容'
        applyParam['searchIssueVo.currentOrgId']=orgInit['DftWangGeOrgId']
        applyParam['searchIssueVo.inputFrom']='2015-12-01'
        applyParam['searchIssueVo.inputEnd']=Time.getCurrentDate()
        applyParam['userId']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.name='%s'" % InitDefaultPara.userInit['DftWangGeUserXM'])
        applyParam['applyIssueIds']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from ISSUES t where t.subject='"+issueParam['issue.subject']+"'")
        ret = YiJiangDaiBuIntf.applyReward(rewardDict=applyParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '申请失败')
        #检查是否申请成功
        checkApplyParam=copy.deepcopy(YiJiangDaiBuPara.CheckApplyReward) 
        checkApplyParam['subject']= issueParam['issue.subject']
        ret = YiJiangDaiBuIntf.CheckapplyReward(rewardDict=checkApplyParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '检查申请失败')
        pass
    def testReward_02(self):#以奖代补>数据录入情况，批准
        '''以奖代补>审核批准>批准'''
        #先新增1个事件
        issueParam = copy.deepcopy(YiJiangDaiBuPara.issueObject) 
        issueParam['issue.isDefault'] = 'true'
        issueParam['issue.subject'] = '事件主题%s' % CommonUtil.createRandomString() 
        issueParam['selectOrgName']=orgInit['DftJieDaoOrg']
        issueParam['issue.occurOrg.id']=orgInit['DftJieDaoOrgId']
        issueParam['issue.occurLocation'] = '发生地点'
        issueParam['issue.occurDate']=Time.getCurrentDate()
        issueParam['issueRelatedPeopleNames'] = '张三'
        issueParam['issueRelatedPeopleTelephones'] = '13588807624'
        issueParam['issue.relatePeopleCount'] = '3'
        issueParam['selectedTypes'] ='13'
        issueParam['issue.issueContent'] = '事件内容'
        issueParam['issue.sourceKind.id']=YiJiangDaiBuPara.issueObject2['issue.sourceKind.id']
        responseDict = YiJiangDaiBuIntf.addIssue(issueDict=issueParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict, '新增事件失败')
        #在以奖代补里面申请
        applyParam=copy.deepcopy(YiJiangDaiBuPara.ApplyReward)
        applyParam['rewardToSubsidies[0].userId']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.name='%s'" % InitDefaultPara.userInit['DftWangGeUserXM'])
        applyParam['rewardToSubsidies[0].orgId']=orgInit['DftWangGeOrgId']
        applyParam['rewardToSubsidies[0].serviceNumber']='0'
        applyParam['issueIdsStr']=CommonIntf.getDbQueryResult(dbCommand = "select * from ISSUES t where t.subject='"+issueParam['issue.subject']+"'")
        applyParam['content']='第一次申请内容2222222222222222%s' % CommonUtil.createRandomString() 
        applyParam['searchIssueVo.currentOrgId']=orgInit['DftWangGeOrgId']
        applyParam['searchIssueVo.inputFrom']='2015-12-01'
        applyParam['searchIssueVo.inputEnd']=Time.getCurrentDate()
        applyParam['userId']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.name='%s'" % InitDefaultPara.userInit['DftWangGeUserXM'])
        applyParam['applyIssueIds']=CommonIntf.getDbQueryResult(dbCommand = "select * from ISSUES t where t.subject='"+issueParam['issue.subject']+"'")
        ret = YiJiangDaiBuIntf.applyReward(rewardDict=applyParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '申请失败')
        #检查是否申请成功
        checkApplyParam=copy.deepcopy(YiJiangDaiBuPara.CheckApplyReward) 
        checkApplyParam['subject']= issueParam['issue.subject']
        ret = YiJiangDaiBuIntf.CheckapplyReward(rewardDict=checkApplyParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '检查申请失败')
        #在审核批准里批准这条事件
        agreeIssueParam=copy.deepcopy(YiJiangDaiBuPara.AgreeIssue)
        agreeIssueParam['rewardToSubsidiesStep.rewardToSubsidieId']=CommonIntf.getDbQueryResult(dbCommand = "select max(t.id) from rewardtosubsidies t")
        agreeIssueParam['rewardToSubsidiesStep.previouStep']=CommonIntf.getDbQueryResult(dbCommand = "select max(t.id) from rewardtosubsidiestep t")
        agreeIssueParam['rewardToSubsidiesStep.orgId']=orgInit['DftWangGeOrgId']
        agreeIssueParam['rewardToSubsidiesStep.orgCode']='.1.1.1.1.'
        agreeIssueParam['rewardToSubsidiesStep.operateUserId']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.name='%s'" % InitDefaultPara.userInit['DftWangGeUserXM'])
        agreeIssueParam['rewardToSubsidiesStep.money']='10'
        agreeIssueParam['rewardToSubsidiesStep.currentOrgId']=orgInit['DftWangGeOrgId']
        agreeIssueParam['rewardToSubsidiesStep.content']='批准的内容%s' % CommonUtil.createRandomString() 
        agreeIssueParam['agreedIssueIds']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from ISSUES t where t.subject='"+issueParam['issue.subject']+"'")
        ret = YiJiangDaiBuIntf.AgreeApplyReward(rewardDict=agreeIssueParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '批准申请失败')
        #检查批准是否成功
        checkAgreeIssueParam=copy.deepcopy(YiJiangDaiBuPara.CheckAgreeIssue)
        checkAgreeIssueParam['id']=CommonIntf.getDbQueryResult(dbCommand = "select max(t.id) from rewardtosubsidiestep t")
        checkAgreeIssueParam['rewardToSubsidieId']=CommonIntf.getDbQueryResult(dbCommand = "select max(t.id) from rewardtosubsidies t")
        checkAgreeIssueParam['status']=CommonIntf.getDbQueryResult( dbCommand = "select t.status from rewardtosubsidiestep t where t.content='"+agreeIssueParam['rewardToSubsidiesStep.content']+"'")
        ret = YiJiangDaiBuIntf.CheckAgreeApplyReward(checkAgreeIssueParam,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '检查批准失败')
        pass
    def testReward_03(self):#以奖代补>审核批准>上报
        '''以奖代补>审核批准>上报'''
        #先新增1个事件
        issueParam = copy.deepcopy(YiJiangDaiBuPara.issueObject) 
        issueParam['issue.isDefault'] = 'true'
        issueParam['issue.subject'] = '事件主题%s' % CommonUtil.createRandomString() 
        issueParam['selectOrgName']=orgInit['DftJieDaoOrg']
        issueParam['issue.occurOrg.id']=orgInit['DftJieDaoOrgId']
        issueParam['issue.occurLocation'] = '发生地点'
        issueParam['issue.occurDate']=Time.getCurrentDate()
        issueParam['issueRelatedPeopleNames'] = '张三'
        issueParam['issueRelatedPeopleTelephones'] = '13588807624'
        issueParam['issue.relatePeopleCount'] = '3'
        issueParam['selectedTypes'] ='13'
        issueParam['issue.issueContent'] = '事件内容'
        issueParam['issue.sourceKind.id']=YiJiangDaiBuPara.issueObject2['issue.sourceKind.id']
        responseDict = YiJiangDaiBuIntf.addIssue(issueDict=issueParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict, '新增事件失败')
        #在以奖代补里面申请
        applyParam=copy.deepcopy(YiJiangDaiBuPara.ApplyReward)
        applyParam['rewardToSubsidies[0].userId']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.name='%s'" % InitDefaultPara.userInit['DftWangGeUserXM'])
        applyParam['rewardToSubsidies[0].orgId']=orgInit['DftWangGeOrgId']
        applyParam['rewardToSubsidies[0].serviceNumber']='0'
        applyParam['issueIdsStr']=CommonIntf.getDbQueryResult(dbCommand = "select * from ISSUES t where t.subject='"+issueParam['issue.subject']+"'")
        applyParam['content']='第一次申请内容2222222222222222%s' % CommonUtil.createRandomString() 
        applyParam['searchIssueVo.currentOrgId']=orgInit['DftWangGeOrgId']
        applyParam['searchIssueVo.inputFrom']='2015-12-01'
        applyParam['searchIssueVo.inputEnd']=Time.getCurrentDate()
        applyParam['userId']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.name='%s'" % InitDefaultPara.userInit['DftWangGeUserXM'])
        applyParam['applyIssueIds']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from ISSUES t where t.subject='"+issueParam['issue.subject']+"'")
        ret = YiJiangDaiBuIntf.applyReward(rewardDict=applyParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '申请失败')
        #检查是否申请成功
        checkApplyParam=copy.deepcopy(YiJiangDaiBuPara.CheckApplyReward) 
        checkApplyParam['subject']= issueParam['issue.subject']
        ret = YiJiangDaiBuIntf.CheckapplyReward(rewardDict=checkApplyParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '检查申请失败')
        #上报
        reportIssueParam=copy.deepcopy(YiJiangDaiBuPara.ReportIssue)
        reportIssueParam['rewardToSubsidiesStep.content']='自动上报666%s'% CommonUtil.createRandomString() 
        reportIssueParam['stepIds']=CommonIntf.getDbQueryResult(dbCommand = "select max(t.id) from rewardtosubsidiestep t")
        ret = YiJiangDaiBuIntf.ReportReward(reportIssueParam,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '检查申请失败')
        #检查上报是否成功
        checkReportIssueParam=copy.deepcopy(YiJiangDaiBuPara.CheckAgreeIssue)
        checkReportIssueParam['id']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from ISSUES t where t.subject='"+reportIssueParam['rewardToSubsidiesStep.content']+"'")
        checkReportIssueParam['rewardToSubsidieId']=CommonIntf.getDbQueryResult(dbCommand = "select max(t.id) from rewardtosubsidies t")
        checkReportIssueParam['status']=CommonIntf.getDbQueryResult(dbCommand = "select t.status from rewardtosubsidiestep t  where t.id = (select max(t.id) from rewardtosubsidiestep t)")
        ret = YiJiangDaiBuIntf.CheckReportReward(checkReportIssueParam,username=InitDefaultPara.userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(ret, '检查上报失败了')
        pass
    def testReward_04(self):#以奖代补>审核批准>否决
        '''以奖代补>审核批准>否决'''
        #先新增1个事件
        issueParam = copy.deepcopy(YiJiangDaiBuPara.issueObject) 
        issueParam['issue.isDefault'] = 'true'
        issueParam['issue.subject'] = '事件主题%s' % CommonUtil.createRandomString() 
        issueParam['selectOrgName']=orgInit['DftJieDaoOrg']
        issueParam['issue.occurOrg.id']=orgInit['DftJieDaoOrgId']
        issueParam['issue.occurLocation'] = '发生地点'
        issueParam['issue.occurDate']=Time.getCurrentDate()
        issueParam['issueRelatedPeopleNames'] = '张三'
        issueParam['issueRelatedPeopleTelephones'] = '13588807624'
        issueParam['issue.relatePeopleCount'] = '3'
        issueParam['selectedTypes'] ='13'
        issueParam['issue.issueContent'] = '事件内容'
        issueParam['issue.sourceKind.id']=YiJiangDaiBuPara.issueObject2['issue.sourceKind.id']
        responseDict = YiJiangDaiBuIntf.addIssue(issueDict=issueParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict, '新增事件失败')
        #在以奖代补里面申请
        applyParam=copy.deepcopy(YiJiangDaiBuPara.ApplyReward)
        applyParam['rewardToSubsidies[0].userId']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.name='%s'" % InitDefaultPara.userInit['DftWangGeUserXM'])
        applyParam['rewardToSubsidies[0].orgId']=orgInit['DftWangGeOrgId']
        applyParam['rewardToSubsidies[0].serviceNumber']='0'
        applyParam['issueIdsStr']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from ISSUES t where t.subject='"+issueParam['issue.subject']+"'")
        applyParam['content']='第一次申请内容2222222222222222%s' % CommonUtil.createRandomString() 
        applyParam['searchIssueVo.currentOrgId']=orgInit['DftWangGeOrgId']
        applyParam['searchIssueVo.inputFrom']='2015-12-01'
        applyParam['searchIssueVo.inputEnd']=Time.getCurrentDate()
        applyParam['userId']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.name='%s'" % InitDefaultPara.userInit['DftWangGeUserXM'])
        applyParam['applyIssueIds']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from ISSUES t where t.subject='"+issueParam['issue.subject']+"'")
        ret = YiJiangDaiBuIntf.applyReward(rewardDict=applyParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '申请失败')
        #检查是否申请成功
        checkApplyParam=copy.deepcopy(YiJiangDaiBuPara.CheckApplyReward) 
        checkApplyParam['subject']= issueParam['issue.subject']
        ret = YiJiangDaiBuIntf.CheckapplyReward(rewardDict=checkApplyParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '检查申请失败')
        #再否决这条申请
        disagreeParam=copy.deepcopy(YiJiangDaiBuPara.Dissagree)
        disagreeParam['rewardToSubsidiesStep.content']='否决时填写的内容%s' % CommonUtil.createRandomString() 
        disagreeParam['stepIds']=CommonIntf.getDbQueryResult(dbCommand = "select max(t.id) from rewardtosubsidiestep t")
        ret = YiJiangDaiBuIntf.DisagreeReward(rewardDict=disagreeParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '检查申请失败')
        #检查否决是否成功
        checkDisagreeParam=copy.deepcopy(YiJiangDaiBuPara.CheckAgreeIssue)
        checkDisagreeParam['id']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from ISSUES t where t.subject='"+disagreeParam['rewardToSubsidiesStep.content']+"'")
        checkDisagreeParam['rewardToSubsidieId']=CommonIntf.getDbQueryResult(dbCommand = "select max(t.id) from rewardtosubsidies t")
        checkDisagreeParam['status']=CommonIntf.getDbQueryResult( dbCommand = "select t.status from rewardtosubsidiestep t where t.content='"+disagreeParam['rewardToSubsidiesStep.content']+"'")
        ret = YiJiangDaiBuIntf.CheckDisagree(rewardDict=checkDisagreeParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '检查否决失败')
        pass
    def testReward_05(self):#以奖代补>审核批准>事件清单编辑
        '''以奖代补>审核批准>事件清单编辑'''
        #先新增1个事件
        issueParam = copy.deepcopy(YiJiangDaiBuPara.issueObject) 
        issueParam['issue.isDefault'] = 'true'
        issueParam['issue.subject'] = '事件主题%s' % CommonUtil.createRandomString() 
        issueParam['selectOrgName']=orgInit['DftJieDaoOrg']
        issueParam['issue.occurOrg.id']=orgInit['DftJieDaoOrgId']
        issueParam['issue.occurLocation'] = '发生地点'
        issueParam['issue.occurDate']=Time.getCurrentDate()
        issueParam['issueRelatedPeopleNames'] = '张三'
        issueParam['issueRelatedPeopleTelephones'] = '13588807624'
        issueParam['issue.relatePeopleCount'] = '3'
        issueParam['selectedTypes'] ='13'
        issueParam['issue.issueContent'] = '事件内容'
        issueParam['issue.sourceKind.id']=YiJiangDaiBuPara.issueObject2['issue.sourceKind.id']
        responseDict = YiJiangDaiBuIntf.addIssue(issueDict=issueParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict, '新增事件失败')
        #在以奖代补里面申请
        applyParam=copy.deepcopy(YiJiangDaiBuPara.ApplyReward)
        applyParam['rewardToSubsidies[0].userId']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.name='%s'" % InitDefaultPara.userInit['DftWangGeUserXM'])
        applyParam['rewardToSubsidies[0].orgId']=orgInit['DftWangGeOrgId']
        applyParam['rewardToSubsidies[0].serviceNumber']='0'
        applyParam['issueIdsStr']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from ISSUES t where t.subject='"+issueParam['issue.subject']+"'")
        applyParam['content']='第一次申请内容2222222222222222%s' % CommonUtil.createRandomString() 
        applyParam['searchIssueVo.currentOrgId']=orgInit['DftWangGeOrgId']
        applyParam['searchIssueVo.inputFrom']='2015-12-01'
        applyParam['searchIssueVo.inputEnd']=Time.getCurrentDate()
        applyParam['userId']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.name='%s'" % InitDefaultPara.userInit['DftWangGeUserXM'])
        applyParam['applyIssueIds']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from ISSUES t where t.subject='"+issueParam['issue.subject']+"'")
        ret = YiJiangDaiBuIntf.applyReward(rewardDict=applyParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '申请失败')
        #检查是否申请成功
        checkApplyParam=copy.deepcopy(YiJiangDaiBuPara.CheckApplyReward) 
        checkApplyParam['subject']= issueParam['issue.subject']
        ret = YiJiangDaiBuIntf.CheckapplyReward(rewardDict=checkApplyParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '检查申请失败')
        #事件清单编辑
        updateRewardParam=copy.deepcopy(YiJiangDaiBuPara.UpdateReward)
        updateRewardParam['rewardtoSubsidieIssues.rewardToSubsidieId']=CommonIntf.getDbQueryResult(dbCommand = "select max(t.id) from rewardtosubsidies t")
        updateRewardParam['rewardtoSubsidieIssues.issueId']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from ISSUES t where t.subject='"+issueParam['issue.subject']+"'")
        ret = YiJiangDaiBuIntf.UpdteReward(rewardDict=updateRewardParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '事件处理清单编辑删除失败')
        #检查删除是否成功
        checkUpdateParam=copy.deepcopy(YiJiangDaiBuPara.checkReward)
        checkUpdateParam['subject']=issueParam['issue.subject']
        checkUpdateParam['issueId']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from ISSUES t where t.subject='"+issueParam['issue.subject']+"'")
        ret = YiJiangDaiBuIntf.checkUpdteReward(rewardDict=checkUpdateParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertFalse(ret, '事件处理清单编辑删除失败')
        pass
    def testReward_06(self):#以奖代补>审核批准>重置
        '''以奖代补>审核批准>重置'''
        #先新增1个事件
        issueParam = copy.deepcopy(YiJiangDaiBuPara.issueObject) 
        issueParam['issue.isDefault'] = 'true'
        issueParam['issue.subject'] = '事件主题%s' % CommonUtil.createRandomString() 
        issueParam['selectOrgName']=orgInit['DftJieDaoOrg']
        issueParam['issue.occurOrg.id']=orgInit['DftJieDaoOrgId']
        issueParam['issue.occurLocation'] = '发生地点'
        issueParam['issue.occurDate']=Time.getCurrentDate()
        issueParam['issueRelatedPeopleNames'] = '张三'
        issueParam['issueRelatedPeopleTelephones'] = '13588807624'
        issueParam['issue.relatePeopleCount'] = '3'
        issueParam['selectedTypes'] ='13'
        issueParam['issue.issueContent'] = '事件内容'
        issueParam['issue.sourceKind.id']=YiJiangDaiBuPara.issueObject2['issue.sourceKind.id']
        responseDict = YiJiangDaiBuIntf.addIssue(issueDict=issueParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict, '新增事件失败')
        #在以奖代补里面申请
        applyParam=copy.deepcopy(YiJiangDaiBuPara.ApplyReward)
        applyParam['rewardToSubsidies[0].userId']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.name='%s'" % InitDefaultPara.userInit['DftWangGeUserXM'])
        applyParam['rewardToSubsidies[0].orgId']=orgInit['DftWangGeOrgId']
        applyParam['rewardToSubsidies[0].serviceNumber']='0'
        applyParam['issueIdsStr']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from ISSUES t where t.subject='"+issueParam['issue.subject']+"'")
        applyParam['content']='申请是为了重置%s' % CommonUtil.createRandomString() 
        applyParam['searchIssueVo.currentOrgId']=orgInit['DftWangGeOrgId']
        applyParam['searchIssueVo.inputFrom']='2015-12-01'
        applyParam['searchIssueVo.inputEnd']=Time.getCurrentDate()
        applyParam['userId']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.name='%s'" % InitDefaultPara.userInit['DftWangGeUserXM'])
        applyParam['applyIssueIds']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from ISSUES t where t.subject='"+issueParam['issue.subject']+"'")
        ret = YiJiangDaiBuIntf.applyReward(rewardDict=applyParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '申请失败')
        #检查是否申请成功
        checkApplyParam=copy.deepcopy(YiJiangDaiBuPara.CheckApplyReward) 
        checkApplyParam['subject']= issueParam['issue.subject']
        ret = YiJiangDaiBuIntf.CheckapplyReward(rewardDict=checkApplyParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '检查申请失败')
        #重置
        resetRewardParam=copy.deepcopy(YiJiangDaiBuPara.resetReward)
        resetRewardParam['stepIds']=CommonIntf.getDbQueryResult(dbCommand = "select max(t.id) from rewardtosubsidiestep t ")
        ret = YiJiangDaiBuIntf.ResetReward(rewardDict=resetRewardParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '检查申请失败')
        #检查重置是否成功
        checkResetReward=copy.deepcopy(YiJiangDaiBuPara.checkReset)
        checkResetReward['id']=CommonIntf.getDbQueryResult(dbCommand = "select max(t.id) from rewardtosubsidiestep t")
        checkResetReward['money']=0
        checkResetReward['status']=CommonIntf.getDbQueryResult(dbCommand = "select t.status from rewardtosubsidiestep t  where t.id = (select max(t.id) from rewardtosubsidiestep t)")
        ret = YiJiangDaiBuIntf.checkResetReward(rewardDict=checkResetReward,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '检查重置失败')
        pass
    def testReward_07(self):#以奖代补>审核批准>删除
        '''以奖代补>审核批准>删除'''
        #先新增1个事件
        issueParam = copy.deepcopy(YiJiangDaiBuPara.issueObject) 
        issueParam['issue.isDefault'] = 'true'
        issueParam['issue.subject'] = '事件主题%s' % CommonUtil.createRandomString() 
        issueParam['selectOrgName']=orgInit['DftJieDaoOrg']
        issueParam['issue.occurOrg.id']=orgInit['DftJieDaoOrgId']
        issueParam['issue.occurLocation'] = '发生地点'
        issueParam['issue.occurDate']=Time.getCurrentDate()
        issueParam['issueRelatedPeopleNames'] = '张三'
        issueParam['issueRelatedPeopleTelephones'] = '13588807624'
        issueParam['issue.relatePeopleCount'] = '3'
        issueParam['selectedTypes'] ='13'
        issueParam['issue.issueContent'] = '事件内容'
        issueParam['issue.sourceKind.id']=YiJiangDaiBuPara.issueObject2['issue.sourceKind.id']
        responseDict = YiJiangDaiBuIntf.addIssue(issueDict=issueParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict, '新增事件失败')
        #在以奖代补里面申请
        applyParam=copy.deepcopy(YiJiangDaiBuPara.ApplyReward)
        applyParam['rewardToSubsidies[0].userId']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.name='%s'" % InitDefaultPara.userInit['DftWangGeUserXM'])
        applyParam['rewardToSubsidies[0].orgId']=orgInit['DftWangGeOrgId']
        applyParam['rewardToSubsidies[0].serviceNumber']='0'
        applyParam['issueIdsStr']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from ISSUES t where t.subject='"+issueParam['issue.subject']+"'")
        applyParam['content']='申请是为了重置%s' % CommonUtil.createRandomString() 
        applyParam['searchIssueVo.currentOrgId']=orgInit['DftWangGeOrgId']
        applyParam['searchIssueVo.inputFrom']='2015-12-01'
        applyParam['searchIssueVo.inputEnd']=Time.getCurrentDate()
        applyParam['userId']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.name='%s'" % InitDefaultPara.userInit['DftWangGeUserXM'])
        applyParam['applyIssueIds']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from ISSUES t where t.subject='"+issueParam['issue.subject']+"'")
        ret = YiJiangDaiBuIntf.applyReward(rewardDict=applyParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '申请失败')
        #检查是否申请成功
        checkApplyParam=copy.deepcopy(YiJiangDaiBuPara.CheckApplyReward) 
        checkApplyParam['subject']= issueParam['issue.subject']
        ret = YiJiangDaiBuIntf.CheckapplyReward(rewardDict=checkApplyParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '检查申请失败')
        #删除
        deleteRewardParam=copy.deepcopy(YiJiangDaiBuPara.deleteReward)
        deleteRewardParam['applyIds']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from rewardtosubsidies t where t.content='%s'" % applyParam['content'])
        ret = YiJiangDaiBuIntf.DeleteReward(rewardDict=deleteRewardParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '删除失败')
        #检查删除是否成功
        checkDeleteParam=copy.deepcopy(YiJiangDaiBuPara.checkDelete)
        checkDeleteParam['id']=CommonIntf.getDbQueryResult(dbCommand = "select max(t.id) from rewardtosubsidies t")
        ret = YiJiangDaiBuIntf.checkDeleteReward(rewardDict=deleteRewardParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertFalse(ret, '删除失败')
        pass
    def testReward_08(self):#以奖代补>审核批准>状态筛选
        '''以奖代补>审核批准>状态筛选'''
        #先新增1个事件
        issueParam = copy.deepcopy(YiJiangDaiBuPara.issueObject) 
        issueParam['issue.isDefault'] = 'true'
        issueParam['issue.subject'] = '事件主题%s' % CommonUtil.createRandomString() 
        issueParam['selectOrgName']=orgInit['DftJieDaoOrg']
        issueParam['issue.occurOrg.id']=orgInit['DftJieDaoOrgId']
        issueParam['issue.occurLocation'] = '发生地点'
        issueParam['issue.occurDate']=Time.getCurrentDate()
        issueParam['issueRelatedPeopleNames'] = '张三'
        issueParam['issueRelatedPeopleTelephones'] = '13588807624'
        issueParam['issue.relatePeopleCount'] = '3'
        issueParam['selectedTypes'] ='13'
        issueParam['issue.issueContent'] = '事件内容'
        issueParam['issue.sourceKind.id']=YiJiangDaiBuPara.issueObject2['issue.sourceKind.id']
        responseDict = YiJiangDaiBuIntf.addIssue(issueDict=issueParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict, '新增事件失败')
        #在以奖代补里面申请
        applyParam=copy.deepcopy(YiJiangDaiBuPara.ApplyReward)
        applyParam['rewardToSubsidies[0].userId']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.name='%s'" % InitDefaultPara.userInit['DftWangGeUserXM'])
        applyParam['rewardToSubsidies[0].orgId']=orgInit['DftWangGeOrgId']
        applyParam['rewardToSubsidies[0].serviceNumber']='0'
        applyParam['issueIdsStr']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from ISSUES t where t.subject='"+issueParam['issue.subject']+"'")
        applyParam['content']='申请是为了重置%s' % CommonUtil.createRandomString() 
        applyParam['searchIssueVo.currentOrgId']=orgInit['DftWangGeOrgId']
        applyParam['searchIssueVo.inputFrom']='2015-12-01'
        applyParam['searchIssueVo.inputEnd']=Time.getCurrentDate()
        applyParam['userId']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.name='%s'" % InitDefaultPara.userInit['DftWangGeUserXM'])
        applyParam['applyIssueIds']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from ISSUES t where t.subject='"+issueParam['issue.subject']+"'")
        ret = YiJiangDaiBuIntf.applyReward(rewardDict=applyParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '申请失败')
        #检查是否申请成功
        checkApplyParam=copy.deepcopy(YiJiangDaiBuPara.CheckApplyReward) 
        checkApplyParam['subject']= issueParam['issue.subject']
        ret = YiJiangDaiBuIntf.CheckapplyReward(rewardDict=checkApplyParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '检查申请失败')
        #筛选待处理数据
        searchParam=copy.deepcopy(YiJiangDaiBuPara.searchReward)
        searchParam['status']=CommonIntf.getDbQueryResult(dbCommand = "select t.status from rewardtosubsidiestep t  where t.id = (select max(t.id) from rewardtosubsidiestep t)")
        ret = YiJiangDaiBuIntf.findByStatus(rewardDict=searchParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '检查筛选失败')
        #检查筛选是否成功
        searchParam=copy.deepcopy(YiJiangDaiBuPara.searchReward)
        searchParam['status']=CommonIntf.getDbQueryResult(dbCommand = "select t.status from rewardtosubsidiestep t  where t.id = (select max(t.id) from rewardtosubsidiestep t)")
        ret = YiJiangDaiBuIntf.CheckFindByStatus(rewardDict=searchParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '检查筛选失败')
        pass
    def testReward_09(self):#以奖代补>审核批准>以奖代补汇总表
        '''以奖代补>以奖代补汇总表'''
        #先新增1个事件
        issueParam = copy.deepcopy(YiJiangDaiBuPara.issueObject) 
        issueParam['issue.isDefault'] = 'true'
        issueParam['issue.subject'] = '事件主题%s' % CommonUtil.createRandomString() 
        issueParam['selectOrgName']=orgInit['DftJieDaoOrg']
        issueParam['issue.occurOrg.id']=orgInit['DftJieDaoOrgId']
        issueParam['issue.occurLocation'] = '发生地点'
        issueParam['issue.occurDate']=Time.getCurrentDate()
        issueParam['issueRelatedPeopleNames'] = '张三'
        issueParam['issueRelatedPeopleTelephones'] = '13588807624'
        issueParam['issue.relatePeopleCount'] = '3'
        issueParam['selectedTypes'] ='13'
        issueParam['issue.issueContent'] = '事件内容'
        issueParam['issue.sourceKind.id']=YiJiangDaiBuPara.issueObject2['issue.sourceKind.id']
        responseDict = YiJiangDaiBuIntf.addIssue(issueDict=issueParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict, '新增事件失败')
        #在以奖代补里面申请
        applyParam=copy.deepcopy(YiJiangDaiBuPara.ApplyReward)
        applyParam['rewardToSubsidies[0].userId']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.name='%s'" % InitDefaultPara.userInit['DftWangGeUserXM'])
        applyParam['rewardToSubsidies[0].orgId']=orgInit['DftWangGeOrgId']
        applyParam['rewardToSubsidies[0].serviceNumber']='0'
        applyParam['issueIdsStr']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from ISSUES t where t.subject='"+issueParam['issue.subject']+"'")
        applyParam['content']='申请是为了重置%s' % CommonUtil.createRandomString() 
        applyParam['searchIssueVo.currentOrgId']=orgInit['DftWangGeOrgId']
        applyParam['searchIssueVo.inputFrom']='2015-12-01'
        applyParam['searchIssueVo.inputEnd']=Time.getCurrentDate()
        applyParam['userId']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.name='%s'" % InitDefaultPara.userInit['DftWangGeUserXM'])
        applyParam['applyIssueIds']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from ISSUES t where t.subject='"+issueParam['issue.subject']+"'")
        ret = YiJiangDaiBuIntf.applyReward(rewardDict=applyParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '申请失败')
        #检查是否申请成功
        checkApplyParam=copy.deepcopy(YiJiangDaiBuPara.CheckApplyReward) 
        checkApplyParam['subject']= issueParam['issue.subject']
        ret = YiJiangDaiBuIntf.CheckapplyReward(rewardDict=checkApplyParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '检查申请失败')
        #筛选待处理数据
        countParam=copy.deepcopy(YiJiangDaiBuPara.countReward)
        countParam['finishAuditNumber']=CommonIntf.getDbQueryResult(dbCommand = "select count(*) from rewardtosubsidiestep t where t.status in (3,4) and t.orgid='%s'"%(orgInit['DftWangGeOrgId']))
        countParam['hasreportedNumber']=CommonIntf.getDbQueryResult(dbCommand = "select count(*) from rewardtosubsidiestep t where t.status=2 and t.orgid='%s'"%(orgInit['DftWangGeOrgId']))
        countParam['waitAuditNumber']=CommonIntf.getDbQueryResult(dbCommand = "select count(*) from rewardtosubsidiestep t where t.status=1 and t.orgid='%s'"%(orgInit['DftWangGeOrgId']))
        countParam['rewardMoney']=CommonIntf.getDbQueryResult(dbCommand = "select sum(money) as money from rewardtosubsidiestep t where t.status=3 and t.orgid='%s'"%(orgInit['DftWangGeOrgId']))
        print "审核完成%s"%countParam['finishAuditNumber']
        print "待审核%s"%countParam['waitAuditNumber']
        print "审核中%s"%countParam['hasreportedNumber']
        print "奖励金额%s"%countParam['rewardMoney']
        ret = YiJiangDaiBuIntf.checkCountReward(rewardDict=countParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '统计失败')
        pass
    def testReward_10(self):#以奖代补>数据录入情况>高级搜索
        AdvancedSearchParam=copy.deepcopy(YiJiangDaiBuPara.findAdvancedSearch)
        AdvancedSearchParam['searchIssueVo.name']=InitDefaultPara.userInit['DftWangGeUserXM']
        responseDict = YiJiangDaiBuIntf.AdvancedSearch(rewardDict=AdvancedSearchParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict, '高级搜索失败')
        #检查高级搜索是否成功
        checkAdvancedSearch=copy.deepcopy(YiJiangDaiBuPara.findAdvancedSearch)
        checkAdvancedSearch['searchIssueVo.name']='网格121212'#AdvancedSearchParam['searchIssueVo.name']
        responseDict = YiJiangDaiBuIntf.checkAdvancedSearch(rewardDict=checkAdvancedSearch, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict, '检查高级搜索失败')
        pass
if __name__ == "__main__":
    suite = unittest.TestSuite()
#     suite.addTest(YiJingDaiBu("tearDown"))
#     suite.addTest(YiJingDaiBu("testReward_01"))#以奖代补>数据录入情况>申请
#     suite.addTest(YiJingDaiBu("testReward_02"))#以奖代补>审核批准>批准
#     suite.addTest(YiJingDaiBu("testReward_03"))#以奖代补>审核批准>上报
#     suite.addTest(YiJingDaiBu("testReward_04"))#以奖代补>审核批准>否决
#     suite.addTest(YiJingDaiBu("testReward_05"))#以奖代补>审核批准>事件清单编辑
#     suite.addTest(YiJingDaiBu("testReward_06"))#以奖代补>审核批准>重置
#     suite.addTest(YiJingDaiBu("testReward_07"))#以奖代补>审核批准>删除
#     suite.addTest(YiJingDaiBu("testReward_08"))#以奖代补>审核批准>状态筛选
#     suite.addTest(YiJingDaiBu("testReward_09"))#以奖代补>审核批准>以奖代补汇总表
#     suite.addTest(YiJingDaiBu("testReward_10"))#以奖代补>数据录入情况>高级搜索
    results = unittest.TextTestRunner().run(suite)
    pass
