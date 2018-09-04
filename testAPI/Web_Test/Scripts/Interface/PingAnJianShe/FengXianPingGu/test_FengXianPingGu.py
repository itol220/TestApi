# -*- coding:UTF-8 -*-
'''
Created on 2015-11-18

@author: N-266
'''
from __future__ import unicode_literals
import unittest
import copy
from Interface.PingAnJianShe.FengXianPingGu import FengPingPara,\
      FengPingIntf
from Interface.PingAnJianShe.Common import CommonIntf
from Interface.PingAnJianShe.FengXianPingGu.FengPingPara import PlanInfo
from Interface.PingAnJianShe.FengXianPingGu.FengPingPara import Status
from Interface.PingAnJianShe.FengXianPingGu.FengPingPara import PlanAdjust
from Interface.PingAnJianShe.FengXianPingGu.FengPingPara import EvaluateType
from Interface.PingAnJianShe.FengXianPingGu.FengPingPara import AssessmentMode
from Interface.PingAnJianShe.FengXianPingGu.FengPingPara import Delegate
from Interface.PingAnJianShe.FengXianPingGu.FengPingPara import Conclusion
from Interface.PingAnJianShe.FengXianPingGu.FengPingPara import Record
from Interface.PingAnJianShe.FengXianPingGu.FengPingPara import RiskExpertSex
from Interface.PingAnJianShe.FengXianPingGu.FengPingPara import RiskExpertSkillTitle
from Interface.PingAnJianShe.FengXianPingGu.FengPingPara import RiskExpertBelongIndustry
from Interface.PingAnJianShe.FengXianPingGu.FengPingPara import Classification
from Interface.PingAnJianShe.FengXianPingGu.FengPingPara import ProjectType
from CONFIG import InitDefaultPara
from CONFIG.InitDefaultPara import orgInit,userInit
from COMMON import Time, CommonUtil
# from Interface.PingAnJianShe.SystemMgr import SystemMgrIntf
from Interface.PingAnJianShe.SystemMgr import SystemMgrIntf
class FengXianPingGu(unittest.TestCase):
 
    def setUp(self):
        SystemMgrIntf.initEnv()
        FengPingIntf.deleteAllRisk()
        pass
#     def setUp(self):
#         pass
    def tearDown(self):       
        pass
    def testRisk_01(self):#新增风险评估>计划项目
        """风险评估>计划管理，新增项目"""
        riskParam = copy.deepcopy(FengPingPara.riskObject) 
        riskParam['riskProjectReport.createOrg.id'] =InitDefaultPara.orgInit['DftWangGeOrgId']
        riskParam['riskProjectReport.importMatterName']='好的%s' % CommonUtil.createRandomString()   
        riskParam['riskProjectReport.projectLeader']='决策主体1'
        riskParam['riskProjectReport.projectClassification.id']=CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '重大工程项目'")#Classification.ONE
        riskParam['riskProjectReport.projectType.id']=CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '农村征地'")#ProjectType.YI
        riskParam['riskProjectReport.beginYearFiling']=PlanInfo.INPLAN
        riskParam['riskProjectReport.memo']='概述'
        riskParam['mode']='add' 
        responseDict = FengPingIntf.addRisk(riskDict=riskParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        #查看是否新增成功
        param = copy.deepcopy(FengPingPara.checkObject)
        param['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret = FengPingIntf.checkAddRisk(riskDict=param, orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')    
        self.assertTrue(ret, '查找失败')
        pass
    def testRisk_02(self):#风险评估>修改计划项目
        """风险评估>计划管理，修改计划项目"""
        riskParam = copy.deepcopy(FengPingPara.riskObject) 
        riskParam['riskProjectReport.createOrg.id'] =InitDefaultPara.orgInit['DftWangGeOrgId']
        riskParam['riskProjectReport.importMatterName']='好的%s' % CommonUtil.createRandomString()   
        riskParam['riskProjectReport.projectLeader']='决策主体1'
        riskParam['riskProjectReport.projectClassification.id']=CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '重大工程项目'")#Classification.ONE
        riskParam['riskProjectReport.projectType.id']=CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '农村征地'")#ProjectType.YI
        riskParam['riskProjectReport.beginYearFiling']=PlanInfo.INPLAN
        riskParam['riskProjectReport.memo']='概述'
        riskParam['mode']='add' 
        responseDict = FengPingIntf.addRisk(riskDict=riskParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        #查看是否新增成功
        param = copy.deepcopy(FengPingPara.checkObject)
        param['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret = FengPingIntf.checkAddRisk(riskDict=param, orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')    
        self.assertTrue(ret, '查找失败')
        #再修改新增的项目
        riskParam['riskProjectReport.createOrg.id'] =InitDefaultPara.orgInit['DftWangGeOrgId']
        riskParam['riskProjectReport.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        riskParam['mode'] = 'edit'
        riskParam['riskProjectReport.importMatterName'] ='修改后的项目名称'
        riskParam['riskProjectReport.projectLeader']='修改后的决策主体'
        riskParam['riskProjectReport.projectClassification.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='项目分类', displayName='重大工程项目')
        riskParam['riskProjectReport.projectType.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='项目类别', displayName='公益事业')
        riskParam['riskProjectReport.beginYearFiling']=PlanInfo.INPLAN
        riskParam['riskProjectReport.memo']='修改后的概述'
        print riskParam['riskProjectReport.id']
        ret = FengPingIntf.updateRisk(riskObject=riskParam,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '修改失败')
        #检查是否修改成功
        updateParam = copy.deepcopy(FengPingPara.checkObject)
        updateParam['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret = FengPingIntf.checkUpdateRisk(updateParam, orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')   
        self.assertTrue(ret, '修改项目失败')
        pass
    def testRisk_03(self):#风险评估>计划管理，删除项目
        """风险评估>计划管理，删除项目"""
        #先新增1个项目
        riskParam = copy.deepcopy(FengPingPara.riskObject) 
        riskParam['riskProjectReport.createOrg.id'] =InitDefaultPara.orgInit['DftWangGeOrgId']
        riskParam['riskProjectReport.importMatterName']='好的%s' % CommonUtil.createRandomString()   
        riskParam['riskProjectReport.projectLeader']='决策主体1'
        riskParam['riskProjectReport.projectClassification.id']=CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '重大工程项目'")#Classification.ONE
        riskParam['riskProjectReport.projectType.id']=CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '农村征地'")#ProjectType.YI
        riskParam['riskProjectReport.beginYearFiling']=PlanInfo.INPLAN
        riskParam['riskProjectReport.memo']='概述'
        riskParam['mode']='add' 
        responseDict = FengPingIntf.addRisk(riskDict=riskParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        #查看是否新增成功
        param = copy.deepcopy(FengPingPara.checkObject)
        param['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret = FengPingIntf.checkAddRisk(riskDict=param, orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')    
        self.assertTrue(ret, '查找失败')
        #再删除该项目
        deleteParam = copy.deepcopy(FengPingPara.deleteObject)
        deleteParam['riskProjectReport.createOrg.id'] =InitDefaultPara.orgInit['DftWangGeOrgId']
        deleteParam['riskProjectReportIds'] =CommonIntf.getDbQueryResult(dbCommand = "select t.id from RiskProjectReport t where t.importMatterName='%s'" % riskParam['riskProjectReport.importMatterName'])
        ret = FengPingIntf.deleteRisk(riskObject=deleteParam,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '删除失败')
        #检查是否删除成功
        checkDeleteRisk=copy.deepcopy(FengPingPara.checkObject)
        checkDeleteRisk['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret = FengPingIntf.checkDeleteRisk(riskDict=checkDeleteRisk,orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertFalse(ret, '查找项目失败')
        pass
    def testRisk_04(self):#暂缓和取消暂缓计划项目
        """风险评估>计划管理，暂缓和取消暂缓项目"""
        riskParam = copy.deepcopy(FengPingPara.riskObject) 
        riskParam['riskProjectReport.createOrg.id'] =InitDefaultPara.orgInit['DftWangGeOrgId']
        riskParam['riskProjectReport.importMatterName']='好的%s' % CommonUtil.createRandomString()   
        riskParam['riskProjectReport.projectLeader']='决策主体1'
        riskParam['riskProjectReport.projectClassification.id']=CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '重大工程项目'")#Classification.ONE
        riskParam['riskProjectReport.projectType.id']=CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '农村征地'")#ProjectType.YI
        riskParam['riskProjectReport.beginYearFiling']=PlanInfo.INPLAN
        riskParam['riskProjectReport.memo']='概述'
        riskParam['mode']='add' 
        responseDict = FengPingIntf.addRisk(riskDict=riskParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        #查看是否新增成功
        param = copy.deepcopy(FengPingPara.checkObject)
        param['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret = FengPingIntf.checkAddRisk(riskDict=param, orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')    
        self.assertTrue(ret, '查找失败')
        #再暂缓该项目
        zanHuanParam = copy.deepcopy(FengPingPara.zanhuanObject)
        zanHuanParam['riskProjectReportIds'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from RiskProjectReport t where t.importMatterName='%s'" % riskParam['riskProjectReport.importMatterName'])
        zanHuanParam['riskProjectReport.status']=Status.POSTPONE
        ret = FengPingIntf.zanhuanRisk(riskDict=zanHuanParam,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '暂缓失败')
        #检查暂缓是否成功
        riskParam['riskProjectReport.createOrg.id'] =InitDefaultPara.orgInit['DftWangGeOrgId']
        riskParam['riskProjectReport.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        riskParam['mode'] = 'edit'
        riskParam['riskProjectReport.importMatterName'] =riskParam['riskProjectReport.importMatterName']
        riskParam['riskProjectReport.projectLeader']='暂缓时操作的决策主体'
        riskParam['riskProjectReport.projectClassification.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='项目分类', displayName='重大工程项目')
        riskParam['riskProjectReport.projectType.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='项目类别', displayName='公益事业')
        riskParam['riskProjectReport.beginYearFiling']=PlanInfo.INPLAN
        riskParam['riskProjectReport.memo']='暂缓时操作的概述'
        ret = FengPingIntf.checkZanHuanRisk(riskObject=riskParam,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '操作项目成功，暂缓失败')
        #取消暂缓
        zanHuanParam = copy.deepcopy(FengPingPara.zanhuanObject)
        zanHuanParam['riskProjectReportIds'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from RiskProjectReport t where t.importMatterName='%s'" % riskParam['riskProjectReport.importMatterName'])
        zanHuanParam['riskProjectReport.status']=Status.NOPOSTPONE
        ret = FengPingIntf.QuXiaozanhuanRisk(riskDict=zanHuanParam,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '取消暂缓失败')
        #检查取消暂缓是否成功
        riskParam['riskProjectReport.createOrg.id'] =InitDefaultPara.orgInit['DftWangGeOrgId']
        riskParam['riskProjectReport.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        riskParam['mode'] = 'edit'
        riskParam['riskProjectReport.importMatterName'] =riskParam['riskProjectReport.importMatterName']
        riskParam['riskProjectReport.projectLeader']='修改后的决策主体'
        riskParam['riskProjectReport.projectClassification.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='项目分类', displayName='重大工程项目')
        riskParam['riskProjectReport.projectType.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='项目类别', displayName='公益事业')
        riskParam['riskProjectReport.beginYearFiling']=PlanInfo.INPLAN
        riskParam['riskProjectReport.memo']='修改后的概述'
        ret = FengPingIntf.checkQuXiaoZanHuanRisk(riskDict=riskParam,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '操作项目失败，取消暂缓失败')
        pass
    def testRisk_05(self):#调整和取消调整项目
        """风险评估>计划管理，调整和取消调整项目"""
        #先新增1个项目
        riskParam = copy.deepcopy(FengPingPara.riskObject) 
        riskParam['riskProjectReport.createOrg.id'] =InitDefaultPara.orgInit['DftWangGeOrgId']
        riskParam['riskProjectReport.importMatterName']='好的%s' % CommonUtil.createRandomString()   
        riskParam['riskProjectReport.projectLeader']='决策主体1'
        riskParam['riskProjectReport.projectClassification.id']=CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '重大工程项目'")#Classification.ONE
        riskParam['riskProjectReport.projectType.id']=CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '农村征地'")#ProjectType.YI
        riskParam['riskProjectReport.beginYearFiling']=PlanInfo.INPLAN
        riskParam['riskProjectReport.memo']='概述'
        riskParam['mode']='add' 
        responseDict = FengPingIntf.addRisk(riskDict=riskParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        #查看是否新增成功
        param = copy.deepcopy(FengPingPara.checkObject)
        param['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret = FengPingIntf.checkAddRisk(riskDict=param, orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')    
        self.assertTrue(ret, '查找失败')
        #调整
        adjustParam = copy.deepcopy(FengPingPara.zanhuanObject)
        adjustParam['adjustmentIds'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from RiskProjectReport t where t.importMatterName='%s'" % riskParam['riskProjectReport.importMatterName'])
        adjustParam['riskProjectReport.adjustmentDetail.adjustment']=PlanAdjust.ADJUST
        adjustParam['riskProjectReport.adjustmentDetail.adjustmentReason']='计划调整没有原因1'
        adjustParam['riskProjectReport.adjustmentDetail.adjustmentDate']='2015-10-10'
        ret = FengPingIntf.adjustRisk(riskDict=adjustParam,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '调整失败')
        #检查调整是否成功
        checkAdjustParam=copy.deepcopy(FengPingPara.checkObject)
        checkAdjustParam['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret = FengPingIntf.checkAdjustRisk(riskDict=checkAdjustParam,orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertFalse(ret, '查找项目失败')
        #取消调整
        adjustParam=copy.deepcopy(FengPingPara.quXiaoAdjustObject)
        adjustParam['riskProjectReport.adjustmentDetail.adjustment']=PlanAdjust.NOADJUST
        adjustParam['adjustmentIds']=CommonIntf.getDbQueryResult(dbCommand="select t.id from RiskProjectReport t where t.importMatterName='%s'" % riskParam['riskProjectReport.importMatterName'])
        ret = FengPingIntf.QuXiaoAdjustRisk(riskDict=adjustParam,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '取消调整失败')
        #检查取消调整是否成功
        riskParam['riskProjectReport.createOrg.id'] =InitDefaultPara.orgInit['DftWangGeOrgId']
        riskParam['riskProjectReport.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        riskParam['mode'] = 'edit'
        riskParam['riskProjectReport.importMatterName'] =riskParam['riskProjectReport.importMatterName']
        riskParam['riskProjectReport.projectLeader']='修改后的决策主体'
        riskParam['riskProjectReport.projectClassification.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='项目分类', displayName='重大工程项目')
        riskParam['riskProjectReport.projectType.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='项目类别', displayName='公益事业')
        riskParam['riskProjectReport.beginYearFiling']=PlanInfo.INPLAN
        riskParam['riskProjectReport.memo']='修改后的概述'
        ret = FengPingIntf.checkQuXiaoAdjustRisk(riskDict=riskParam,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '操作项目失败，取消调整失败')
        pass
    def testRisk_06(self):#评估立项--保存
        """风险评估>计划管理，保存项目"""
        #先新增1个项目
        riskParam = copy.deepcopy(FengPingPara.riskObject) 
        riskParam['riskProjectReport.createOrg.id'] =InitDefaultPara.orgInit['DftWangGeOrgId']
        riskParam['riskProjectReport.importMatterName']='好的%s' % CommonUtil.createRandomString()   
        riskParam['riskProjectReport.projectLeader']='决策主体1'
        riskParam['riskProjectReport.projectClassification.id']=CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '重大工程项目'")#Classification.ONE
        riskParam['riskProjectReport.projectType.id']=CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '农村征地'")#ProjectType.YI
        riskParam['riskProjectReport.beginYearFiling']=PlanInfo.INPLAN
        riskParam['riskProjectReport.memo']='概述'
        riskParam['mode']='add' 
        responseDict = FengPingIntf.addRisk(riskDict=riskParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        #查看是否新增成功
        param = copy.deepcopy(FengPingPara.checkObject)
        param['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret = FengPingIntf.checkAddRisk(riskDict=param, orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')    
        self.assertTrue(ret, '查找失败')
        #在评估立项>保存
        InitiationParam = copy.deepcopy(FengPingPara.initiationObject) 
        InitiationParam['riskProjectReport.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        InitiationParam['riskProjectReport.bodyOrg']='88'   
        InitiationParam['riskProjectReport.startDate']='2015-11-19'
        InitiationParam['riskProjectReport.endDate']='2015-11-19'
        InitiationParam['riskProjectReport.assessmentWarn']='30'
        InitiationParam['riskProjectReport.evaluateType']=EvaluateType.EVALUATE
        InitiationParam['riskProjectReport.reviewSuggestion']='审批意见立项'
        InitiationParam['modeTemp']='addOrUpdate'  
        responseDict = FengPingIntf.SaveInitiationRisk(riskDict=InitiationParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '评估立项项目保存失败')
    def testRisk_07(self) :#评估立项提交 
        """风险评估>计划管理，提交项目"""
        #1.先新增1个项目
        riskParam = copy.deepcopy(FengPingPara.riskObject) 
        riskParam['riskProjectReport.createOrg.id'] =InitDefaultPara.orgInit['DftWangGeOrgId']
        riskParam['riskProjectReport.importMatterName']='omgwuwu风险项目%s'%CommonUtil.createRandomString()
        riskParam['riskProjectReport.projectLeader']='决策主体1'
        riskParam['riskProjectReport.projectClassification.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='项目分类', displayName='重大工程项目')
        riskParam['riskProjectReport.projectType.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='项目类别', displayName='公益事业')
        riskParam['riskProjectReport.beginYearFiling']=PlanInfo.INPLAN
        riskParam['riskProjectReport.memo']='概述'
        riskParam['mode']='add'  
        responseDict = FengPingIntf.addRisk(riskDict=riskParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        #查看是否新增成功
        param = copy.deepcopy(FengPingPara.checkObject)
        param['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret = FengPingIntf.checkAddRisk(riskDict=param, orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')    
        self.assertTrue(ret, '查找失败')
        #评估立项--提交
        InitiationParam=copy.deepcopy(FengPingPara.initiationObject) 
        InitiationParam['riskProjectReport.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        InitiationParam['riskProjectReport.bodyOrg']='评估主体'   
        InitiationParam['riskProjectReport.startDate']='2015-11-19'
        InitiationParam['riskProjectReport.endDate']='2015-11-19'
        InitiationParam['riskProjectReport.assessmentWarn']='30'
        InitiationParam['riskProjectReport.evaluateType']=EvaluateType.EVALUATE
        InitiationParam['riskProjectReport.reviewSuggestion']='概述'
        InitiationParam['modeTemp']='submit'  
        ret = FengPingIntf.SubmitInitiationRisk(riskDict=InitiationParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '评估立项，项目提交失败')
        #验证是否可以检查到评估立项提交成功的项目
        param = copy.deepcopy(FengPingPara.checkInitiation)
        param['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret = FengPingIntf.checkSubmitInitiationRisk(riskDict=param, orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '检查评估立项提交失败')
        pass
    def testRisk_08(self):#制定评估方案保存
        """风险评估>评估实施，制定评估方案保存项目"""
        #先新增1个项目
        riskParam = copy.deepcopy(FengPingPara.riskObject) 
        riskParam['riskProjectReport.createOrg.id'] =InitDefaultPara.orgInit['DftWangGeOrgId']
        riskParam['riskProjectReport.importMatterName']='好的%s' % CommonUtil.createRandomString()   
        riskParam['riskProjectReport.projectLeader']='决策主体1'
        riskParam['riskProjectReport.projectClassification.id']=CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '重大工程项目'")#Classification.ONE
        riskParam['riskProjectReport.projectType.id']=CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '农村征地'")#ProjectType.YI
        riskParam['riskProjectReport.beginYearFiling']=PlanInfo.INPLAN
        riskParam['riskProjectReport.memo']='概述'
        riskParam['mode']='add' 
        responseDict = FengPingIntf.addRisk(riskDict=riskParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        #查看是否新增成功
        param = copy.deepcopy(FengPingPara.checkObject)
        param['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret = FengPingIntf.checkAddRisk(riskDict=param, orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')    
        self.assertTrue(ret, '查找失败')
        #然后对该项目进行评估立项并提交
        InitiationParam=copy.deepcopy(FengPingPara.initiationObject) 
        InitiationParam['riskProjectReport.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        InitiationParam['riskProjectReport.bodyOrg']='评估主体'   
        InitiationParam['riskProjectReport.startDate']=Time.getCurrentDate()
        InitiationParam['riskProjectReport.endDate']=Time.getCurrentDate()
        InitiationParam['riskProjectReport.assessmentWarn']='30'
        InitiationParam['riskProjectReport.evaluateType']=EvaluateType.EVALUATE
        InitiationParam['riskProjectReport.reviewSuggestion']='概述'
        InitiationParam['modeTemp']='submit'  
        ret = FengPingIntf.SubmitInitiationRisk(riskDict=InitiationParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '评估立项提交失败')
        #再对项目进行制定评估方案并保存
        makeplanParam=copy.deepcopy(FengPingPara.makeplanObject)
        makeplanParam['riskAssessPlan.project.id']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        makeplanParam['modeTemp']='addOrUpdate'
        makeplanParam['assessmentMode']=AssessmentMode.GONGGAO
        makeplanParam['riskAssessPlan.assessmentMode']='%s,' % AssessmentMode.GONGGAO 
        makeplanParam['riskAssessPlan.bodyOrg']='评估主体'
        makeplanParam['riskAssessPlan.leader']='评估主体责任人'
        makeplanParam['riskAssessPlan.riskEstimate']='风险点预估'
        makeplanParam['riskAssessPlan.request']='评估要求'
        responseDict=FengPingIntf.saveMakePlanRisk(riskDict=makeplanParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict, '制定评估方案保存失败')
        pass
     
    def testRisk_09(self):#制定评估方案并提交，评估方式为公示公告
        """风险评估>评估立项，制定评估方案提交项目"""
        #先新增1个项目
        riskParam = copy.deepcopy(FengPingPara.riskObject) 
        riskParam['riskProjectReport.createOrg.id'] =InitDefaultPara.orgInit['DftWangGeOrgId']
        riskParam['riskProjectReport.importMatterName']='好的%s' % CommonUtil.createRandomString()   
        riskParam['riskProjectReport.projectLeader']='决策主体1'
        riskParam['riskProjectReport.projectClassification.id']=CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '重大工程项目'")#Classification.ONE
        riskParam['riskProjectReport.projectType.id']=CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '农村征地'")#ProjectType.YI
        riskParam['riskProjectReport.beginYearFiling']=PlanInfo.INPLAN
        riskParam['riskProjectReport.memo']='概述'
        riskParam['mode']='add' 
        responseDict = FengPingIntf.addRisk(riskDict=riskParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        #查看是否新增成功
        param = copy.deepcopy(FengPingPara.checkObject)
        param['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret = FengPingIntf.checkAddRisk(riskDict=param, orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')    
        self.assertTrue(ret, '查找失败')
        #2.对该项目进行评估立项
        InitiationParam=copy.deepcopy(FengPingPara.initiationObject) 
        InitiationParam['riskProjectReport.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        InitiationParam['riskProjectReport.bodyOrg']='评估主体11111111111111111'   
        InitiationParam['riskProjectReport.startDate']='2015-11-30'
        InitiationParam['riskProjectReport.endDate']='2015-11-30'
        InitiationParam['riskProjectReport.assessmentWarn']='30'
        InitiationParam['riskProjectReport.evaluateType']=EvaluateType.EVALUATE
        InitiationParam['riskProjectReport.reviewSuggestion']='概述'
        InitiationParam['modeTemp']='submit'  
        ret = FengPingIntf.SubmitInitiationRisk(riskDict=InitiationParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '评估立项提交失败')
        #3.对该项目制定评估方案并提交
        makeplanParam=copy.deepcopy(FengPingPara.makeplanObject)
        makeplanParam['riskAssessPlan.project.id']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        makeplanParam['modeTemp']='submit'
        makeplanParam['assessmentMode']=AssessmentMode.GONGGAO 
        makeplanParam['riskAssessPlan.assessmentMode']=AssessmentMode.GONGGAO 
        makeplanParam['riskAssessPlan.bodyOrg']=InitiationParam['riskProjectReport.bodyOrg']
        makeplanParam['riskAssessPlan.commissionRisk']=Delegate.NO
        makeplanParam['riskAssessPlan.leader']='评估主体责任人'
        makeplanParam['riskAssessPlan.riskEstimate']='风险点预估'
        makeplanParam['riskAssessPlan.request']='评估要求'
        ret=FengPingIntf.SubmitMakeplanRisk(riskDict=makeplanParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '制定评估方案提交失败')
        #4.是否可以检查到提交成功的评估方案
        lookPlanParam=copy.deepcopy(FengPingPara.lookPlanParam)
        lookPlanParam['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret = FengPingIntf.checkSubmitMakeplanRisk(riskDict=lookPlanParam,orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '检查制定评估方案提交失败')
        pass
    def testRisk_09_1(self):#制定评估方案并提交，评估方式为网上联评
        """风险评估>评估立项，制定评估方案并提交，评估方式为网上联评"""
        riskParam = copy.deepcopy(FengPingPara.riskObject) 
        riskParam['riskProjectReport.createOrg.id'] =InitDefaultPara.orgInit['DftWangGeOrgId']
        riskParam['riskProjectReport.importMatterName']='好的%s' % CommonUtil.createRandomString()   
        riskParam['riskProjectReport.projectLeader']='决策主体1'
        riskParam['riskProjectReport.projectClassification.id']=CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '重大工程项目'")#Classification.ONE
        riskParam['riskProjectReport.projectType.id']=CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '农村征地'")#ProjectType.YI
        riskParam['riskProjectReport.beginYearFiling']=PlanInfo.INPLAN
        riskParam['riskProjectReport.memo']='概述'
        riskParam['mode']='add' 
        responseDict = FengPingIntf.addRisk(riskDict=riskParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        #查看是否新增成功
        param = copy.deepcopy(FengPingPara.checkObject)
        param['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret = FengPingIntf.checkAddRisk(riskDict=param, orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')    
        self.assertTrue(ret, '查找失败')
        #2.对该项目进行评估立项
        InitiationParam=copy.deepcopy(FengPingPara.initiationObject) 
        InitiationParam['riskProjectReport.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        InitiationParam['riskProjectReport.bodyOrg']='评估主体11111111111111111'   
        InitiationParam['riskProjectReport.startDate']='2015-11-30'
        InitiationParam['riskProjectReport.endDate']='2015-11-30'
        InitiationParam['riskProjectReport.assessmentWarn']='30'
        InitiationParam['riskProjectReport.evaluateType']=EvaluateType.EVALUATE
        InitiationParam['riskProjectReport.reviewSuggestion']='概述'
        InitiationParam['modeTemp']='submit'  
        ret = FengPingIntf.SubmitInitiationRisk(riskDict=InitiationParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '评估立项提交失败')
        #3.对该项目制定评估方案并提交
        makeplanParam=copy.deepcopy(FengPingPara.makeplanObject)
        makeplanParam['riskAssessPlan.project.id']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        makeplanParam['modeTemp']='submit'
        makeplanParam['assessmentMode']=AssessmentMode.WANGPING 
        makeplanParam['riskAssessPlan.assessmentMode']=AssessmentMode.WANGPING 
        makeplanParam['riskAssessPlan.bodyOrg']=InitiationParam['riskProjectReport.bodyOrg']
        makeplanParam['riskAssessPlan.commissionRisk']=Delegate.NO
        makeplanParam['riskAssessPlan.leader']='评估主体责任人'
        makeplanParam['riskAssessPlan.riskEstimate']='风险点预估'
        makeplanParam['riskAssessPlan.request']='评估要求'
        makeplanParam['riskAssessPlan.orgids']=InitDefaultPara.orgInit['DftWangGeOrgId']
        ret=FengPingIntf.SubmitMakeplanRisk(riskDict=makeplanParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '制定评估方案提交失败')
        #4.是否可以检查到提交成功的评估方案
        lookPlanParam=copy.deepcopy(FengPingPara.lookPlanParam)
        lookPlanParam['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret = FengPingIntf.checkSubmitMakeplanRisk(riskDict=lookPlanParam,orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '检查制定评估方案提交失败')
        pass
    def testRisk_09_2(self):#制定评估方案并提交，评估方式为专家论证
        """风险评估>评估立项，制定评估方案并提交，评估方式为专家论证"""
        riskParam = copy.deepcopy(FengPingPara.riskObject) 
        riskParam['riskProjectReport.createOrg.id'] =InitDefaultPara.orgInit['DftWangGeOrgId']
        riskParam['riskProjectReport.importMatterName']='好的%s' % CommonUtil.createRandomString()   
        riskParam['riskProjectReport.projectLeader']='决策主体1'
        riskParam['riskProjectReport.projectClassification.id']=CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '重大工程项目'")#Classification.ONE
        riskParam['riskProjectReport.projectType.id']=CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '农村征地'")#ProjectType.YI
        riskParam['riskProjectReport.beginYearFiling']=PlanInfo.INPLAN
        riskParam['riskProjectReport.memo']='概述'
        riskParam['mode']='add' 
        responseDict = FengPingIntf.addRisk(riskDict=riskParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        #查看是否新增成功
        param = copy.deepcopy(FengPingPara.checkObject)
        param['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret = FengPingIntf.checkAddRisk(riskDict=param, orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')    
        self.assertTrue(ret, '查找失败')
        #2.对该项目进行评估立项
        InitiationParam=copy.deepcopy(FengPingPara.initiationObject) 
        InitiationParam['riskProjectReport.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        InitiationParam['riskProjectReport.bodyOrg']='评估主体11111111111111111'   
        InitiationParam['riskProjectReport.startDate']='2015-11-30'
        InitiationParam['riskProjectReport.endDate']='2015-11-30'
        InitiationParam['riskProjectReport.assessmentWarn']='30'
        InitiationParam['riskProjectReport.evaluateType']=EvaluateType.EVALUATE
        InitiationParam['riskProjectReport.reviewSuggestion']='概述'
        InitiationParam['modeTemp']='submit'  
        ret = FengPingIntf.SubmitInitiationRisk(riskDict=InitiationParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '评估立项提交失败')
        #3.对该项目制定评估方案并提交
        makeplanParam=copy.deepcopy(FengPingPara.makeplanObject)
        makeplanParam['riskAssessPlan.project.id']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        makeplanParam['modeTemp']='submit'
        makeplanParam['assessmentMode']=AssessmentMode.ZHUANJIA
        makeplanParam['riskAssessPlan.assessmentMode']=AssessmentMode.ZHUANJIA 
        makeplanParam['riskAssessPlan.bodyOrg']=InitiationParam['riskProjectReport.bodyOrg']
        makeplanParam['riskAssessPlan.commissionRisk']=Delegate.NO
        makeplanParam['riskAssessPlan.leader']='评估主体责任人'
        makeplanParam['riskAssessPlan.riskEstimate']='风险点预估'
        makeplanParam['riskAssessPlan.request']='评估要求'
        ret=FengPingIntf.SubmitMakeplanRisk(riskDict=makeplanParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '制定评估方案提交失败')
        #4.是否可以检查到提交成功的评估方案
        lookPlanParam=copy.deepcopy(FengPingPara.lookPlanParam)
        lookPlanParam['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret = FengPingIntf.checkSubmitMakeplanRisk(riskDict=lookPlanParam,orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '检查制定评估方案提交失败')
        pass
    def testRisk_09_3(self):#制定评估方案并提交，评估方式为公示公告.委托评估
        """风险评估>评估立项，制定评估方案并提交，评估方式为专家论证"""
        #先新增1个项目
        riskParam = copy.deepcopy(FengPingPara.riskObject) 
        riskParam['riskProjectReport.createOrg.id'] =InitDefaultPara.orgInit['DftWangGeOrgId']
        riskParam['riskProjectReport.importMatterName']='好的%s' % CommonUtil.createRandomString()   
        riskParam['riskProjectReport.projectLeader']='决策主体1'
        riskParam['riskProjectReport.projectClassification.id']=CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '重大工程项目'")#Classification.ONE
        riskParam['riskProjectReport.projectType.id']=CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '农村征地'")#ProjectType.YI
        riskParam['riskProjectReport.beginYearFiling']=PlanInfo.INPLAN
        riskParam['riskProjectReport.memo']='概述'
        riskParam['mode']='add' 
        responseDict = FengPingIntf.addRisk(riskDict=riskParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        #查看是否新增成功
        param = copy.deepcopy(FengPingPara.checkObject)
        param['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret = FengPingIntf.checkAddRisk(riskDict=param, orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')    
        self.assertTrue(ret, '查找失败')
        #2.对该项目进行评估立项
        InitiationParam=copy.deepcopy(FengPingPara.initiationObject) 
        InitiationParam['riskProjectReport.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        InitiationParam['riskProjectReport.bodyOrg']='评估主体11111111111111111'   
        InitiationParam['riskProjectReport.startDate']='2015-11-30'
        InitiationParam['riskProjectReport.endDate']='2015-11-30'
        InitiationParam['riskProjectReport.assessmentWarn']='30'
        InitiationParam['riskProjectReport.evaluateType']=EvaluateType.EVALUATE
        InitiationParam['riskProjectReport.reviewSuggestion']='概述'
        InitiationParam['modeTemp']='submit'  
        ret = FengPingIntf.SubmitInitiationRisk(riskDict=InitiationParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '评估立项提交失败')
        #3.对该项目制定评估方案并提交
        makeplanParam=copy.deepcopy(FengPingPara.makeplanObject)
        makeplanParam['riskAssessPlan.project.id']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        makeplanParam['modeTemp']='submit'
        makeplanParam['assessmentMode']=AssessmentMode.GONGGAO 
        makeplanParam['riskAssessPlan.assessmentMode']=AssessmentMode.GONGGAO 
        makeplanParam['riskAssessPlan.bodyOrg']=InitiationParam['riskProjectReport.bodyOrg']
        makeplanParam['riskAssessPlan.commissionRisk']=Delegate.YES
        makeplanParam['riskAssessPlan.implementBody']='第三方评估机构啊'
        makeplanParam['riskAssessPlan.implementResponsible']='第三方评估责任人'
        makeplanParam['riskAssessPlan.implementPhone']='13111111111'
        makeplanParam['riskAssessPlan.leader']='评估主体责任人'
        makeplanParam['riskAssessPlan.riskEstimate']='风险点预估'
        makeplanParam['riskAssessPlan.request']='评估要求'
        ret=FengPingIntf.SubmitMakeplanRisk(riskDict=makeplanParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '制定评估方案提交失败')
        #4.是否可以检查到提交成功的评估方案
        lookPlanParam=copy.deepcopy(FengPingPara.lookPlanParam)
        lookPlanParam['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret = FengPingIntf.checkSubmitMakeplanRisk(riskDict=lookPlanParam,orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '检查制定评估方案提交失败')
        pass
    def testRisk_10(self):#评估实施>评估，保存
        """风险评估>评估实施，评估并保存项目"""
        #先新增1个项目
        riskParam = copy.deepcopy(FengPingPara.riskObject) 
        riskParam['riskProjectReport.createOrg.id'] =InitDefaultPara.orgInit['DftWangGeOrgId']
        riskParam['riskProjectReport.importMatterName']='好的%s' % CommonUtil.createRandomString()   
        riskParam['riskProjectReport.projectLeader']='决策主体1'
        riskParam['riskProjectReport.projectClassification.id']=CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '重大工程项目'")#Classification.ONE
        riskParam['riskProjectReport.projectType.id']=CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '农村征地'")#ProjectType.YI
        riskParam['riskProjectReport.beginYearFiling']=PlanInfo.INPLAN
        riskParam['riskProjectReport.memo']='概述'
        riskParam['mode']='add' 
        responseDict = FengPingIntf.addRisk(riskDict=riskParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        #查看是否新增成功
        param = copy.deepcopy(FengPingPara.checkObject)
        param['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret = FengPingIntf.checkAddRisk(riskDict=param, orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')    
        self.assertTrue(ret, '查找失败')
        #评估立项--提交
        InitiationParam=copy.deepcopy(FengPingPara.initiationObject) 
        InitiationParam['riskProjectReport.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        InitiationParam['riskProjectReport.bodyOrg']='评估主体'   
        InitiationParam['riskProjectReport.startDate']='2015-11-19'
        InitiationParam['riskProjectReport.endDate']='2015-11-19'
        InitiationParam['riskProjectReport.assessmentWarn']='30'
        InitiationParam['riskProjectReport.evaluateType']=EvaluateType.EVALUATE
        InitiationParam['riskProjectReport.reviewSuggestion']='概述'
        InitiationParam['modeTemp']='submit'  
        ret = FengPingIntf.SubmitInitiationRisk(riskDict=InitiationParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '评估立项提交失败1')
        #验证是否可以检查到评估立项提交成功的项目
        param = copy.deepcopy(FengPingPara.checkInitiation)
        param['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret = FengPingIntf.checkSubmitInitiationRisk(riskDict=param, orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '检查评估立项提交失败')
        #制定评估方案并提交
        makeplanParam=copy.deepcopy(FengPingPara.makeplanObject)
        makeplanParam['riskAssessPlan.project.id']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        makeplanParam['modeTemp']='submit'
        makeplanParam['riskAssessPlan.assessmentMode']=AssessmentMode.GONGGAO
        makeplanParam['riskAssessPlan.bodyOrg']='评估主体'
        makeplanParam['riskAssessPlan.leader']='评估主体责任人'
        makeplanParam['riskAssessPlan.riskEstimate']='风险点预估'
        makeplanParam['riskAssessPlan.request']='评估要求'
        ret=FengPingIntf.SubmitMakeplanRisk(riskDict=makeplanParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '制定评估方案提交失败')
        #评估实施，保存
        measureParam=copy.deepcopy(FengPingPara.measureObject)
        measureParam['riskAssessMeasure.projectReport.id']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='%s'" % riskParam['riskProjectReport.importMatterName'])
        measureParam['mode']='save'
        measureParam['riskAssessMeasure.assessType']=makeplanParam['riskAssessPlan.assessmentMode']
        measureParam['riskAssessMeasure.advice']='公告内容'
        measureParam['riskAssessMeasure.announcementStartDate']='2015-11-30'
        measureParam['riskAssessMeasure.announcementEndDate']='2015-11-30'
        measureParam['riskAssessMeasure.announcementStyle']='公告方式'
        measureParam['riskAssessMeasure.announcementAdvice']='公告反馈意见1111111111111111'
        ret = FengPingIntf.saveMeasureRisk(riskDict=measureParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '公示公告信息保存失败')
        pass
    def testRisk_10_1(self):#评估实施>评估提交，评估方式为网上联评
        """风险评估>评估实施，评估并提交项目项目，评估方式为网上联评"""
        riskParam = copy.deepcopy(FengPingPara.riskObject) 
        riskParam['riskProjectReport.createOrg.id'] =InitDefaultPara.orgInit['DftWangGeOrgId']
        riskParam['riskProjectReport.importMatterName']='好的%s' % CommonUtil.createRandomString()   
        riskParam['riskProjectReport.projectLeader']='决策主体1'
        riskParam['riskProjectReport.projectClassification.id']=CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '重大工程项目'")#Classification.ONE
        riskParam['riskProjectReport.projectType.id']=CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '农村征地'")#ProjectType.YI
        riskParam['riskProjectReport.beginYearFiling']=PlanInfo.INPLAN
        riskParam['riskProjectReport.memo']='概述'
        riskParam['mode']='add' 
        responseDict = FengPingIntf.addRisk(riskDict=riskParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        #查看是否新增成功
        param = copy.deepcopy(FengPingPara.checkObject)
        param['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret = FengPingIntf.checkAddRisk(riskDict=param, orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')    
        self.assertTrue(ret, '查找失败')
        #2.对该项目进行评估立项
        InitiationParam=copy.deepcopy(FengPingPara.initiationObject) 
        InitiationParam['riskProjectReport.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        InitiationParam['riskProjectReport.bodyOrg']='评估主体11111111111111111'   
        InitiationParam['riskProjectReport.startDate']='2015-11-30'
        InitiationParam['riskProjectReport.endDate']='2015-11-30'
        InitiationParam['riskProjectReport.assessmentWarn']='30'
        InitiationParam['riskProjectReport.evaluateType']=EvaluateType.EVALUATE
        InitiationParam['riskProjectReport.reviewSuggestion']='概述'
        InitiationParam['modeTemp']='submit'  
        ret = FengPingIntf.SubmitInitiationRisk(riskDict=InitiationParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '评估立项提交失败')
        #3.对该项目制定评估方案并提交
        makeplanParam=copy.deepcopy(FengPingPara.makeplanObject)
        makeplanParam['riskAssessPlan.project.id']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        makeplanParam['modeTemp']='submit'
        makeplanParam['assessmentMode']=AssessmentMode.WANGPING 
        makeplanParam['riskAssessPlan.assessmentMode']=AssessmentMode.WANGPING 
        makeplanParam['riskAssessPlan.bodyOrg']=InitiationParam['riskProjectReport.bodyOrg']
        makeplanParam['riskAssessPlan.commissionRisk']=Delegate.NO
        makeplanParam['riskAssessPlan.leader']='评估主体责任人'
        makeplanParam['riskAssessPlan.riskEstimate']='风险点预估'
        makeplanParam['riskAssessPlan.request']='评估要求'
        makeplanParam['riskAssessPlan.orgids']=InitDefaultPara.orgInit['DftWangGeOrgId']
        ret=FengPingIntf.SubmitMakeplanRisk(riskDict=makeplanParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '制定评估方案提交失败')
        #4.是否可以检查到提交成功的评估方案
        lookPlanParam=copy.deepcopy(FengPingPara.lookPlanParam)
        lookPlanParam['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret = FengPingIntf.checkSubmitMakeplanRisk(riskDict=lookPlanParam,orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '检查制定评估方案提交失败')
        #5.评估实施>评估，保存
        measureParam=copy.deepcopy(FengPingPara.WangPing)
        measureParam['riskAssessMeasure.projectReport.id']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='%s'" % riskParam['riskProjectReport.importMatterName'])
        measureParam['riskAssessMeasure.assessType']=makeplanParam['riskAssessPlan.assessmentMode']
        measureParam['riskAssessMeasure.assessMember']='小组成员'
        measureParam['riskAssessMeasure.advice']='评估意见'
        measureParam['riskAssessMeasure.onlineDate']=Time.getCurrentDate()
        measureParam['mode']='save'
        ret = FengPingIntf.saveMeasureRisk_1(riskDict=measureParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '公示公告信息保存失败')
        #6.评估实施>评估，提交
        submitParam=copy.deepcopy(FengPingPara.submitMeasureObject)
        submitParam['ids']= CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='%s'" % riskParam['riskProjectReport.importMatterName'])
        ret=FengPingIntf.SubmitmeasureRisk(riskDict=submitParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '评估实施>评估，提交失败')
        #6.检查评估实施>评估是否提交成功
        checkPar=copy.deepcopy(FengPingPara.measureParam)
        checkPar['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret=FengPingIntf.checkSubmitMeasureRisk_01(riskDict=checkPar,orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '评估实施>评估，提交失败')
        pass
    def testRisk_10_2(self):#评估实施>评估提交，评估方式为专家论证
        """风险评估>评估实施，评估并保存项目，评估方式为专家论证"""
        riskParam = copy.deepcopy(FengPingPara.riskObject) 
        riskParam['riskProjectReport.createOrg.id'] =InitDefaultPara.orgInit['DftWangGeOrgId']
        riskParam['riskProjectReport.importMatterName']='好的%s' % CommonUtil.createRandomString()   
        riskParam['riskProjectReport.projectLeader']='决策主体1'
        riskParam['riskProjectReport.projectClassification.id']=CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '重大工程项目'")#Classification.ONE
        riskParam['riskProjectReport.projectType.id']=CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '农村征地'")#ProjectType.YI
        riskParam['riskProjectReport.beginYearFiling']=PlanInfo.INPLAN
        riskParam['riskProjectReport.memo']='概述'
        riskParam['mode']='add' 
        responseDict = FengPingIntf.addRisk(riskDict=riskParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        #查看是否新增成功
        param = copy.deepcopy(FengPingPara.checkObject)
        param['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret = FengPingIntf.checkAddRisk(riskDict=param, orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')    
        self.assertTrue(ret, '查找失败')
        #2.对该项目进行评估立项
        InitiationParam=copy.deepcopy(FengPingPara.initiationObject) 
        InitiationParam['riskProjectReport.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        InitiationParam['riskProjectReport.bodyOrg']='评估主体11111111111111111'   
        InitiationParam['riskProjectReport.startDate']='2015-11-30'
        InitiationParam['riskProjectReport.endDate']='2015-11-30'
        InitiationParam['riskProjectReport.assessmentWarn']='30'
        InitiationParam['riskProjectReport.evaluateType']=EvaluateType.EVALUATE
        InitiationParam['riskProjectReport.reviewSuggestion']='概述'
        InitiationParam['modeTemp']='submit'  
        ret = FengPingIntf.SubmitInitiationRisk(riskDict=InitiationParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '评估立项提交失败')
        #3.对该项目制定评估方案并提交
        makeplanParam=copy.deepcopy(FengPingPara.makeplanObject)
        makeplanParam['riskAssessPlan.project.id']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        makeplanParam['modeTemp']='submit'
        makeplanParam['assessmentMode']=AssessmentMode.ZHUANJIA 
        makeplanParam['riskAssessPlan.assessmentMode']=AssessmentMode.ZHUANJIA 
        makeplanParam['riskAssessPlan.bodyOrg']=InitiationParam['riskProjectReport.bodyOrg']
        makeplanParam['riskAssessPlan.commissionRisk']=Delegate.NO
        makeplanParam['riskAssessPlan.leader']='评估主体责任人'
        makeplanParam['riskAssessPlan.riskEstimate']='风险点预估'
        makeplanParam['riskAssessPlan.request']='评估要求'
        makeplanParam['riskAssessPlan.orgids']=InitDefaultPara.orgInit['DftWangGeOrgId']
        ret=FengPingIntf.SubmitMakeplanRisk(riskDict=makeplanParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '制定评估方案提交失败')
        #4.是否可以检查到提交成功的评估方案
        lookPlanParam=copy.deepcopy(FengPingPara.lookPlanParam)
        lookPlanParam['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret = FengPingIntf.checkSubmitMakeplanRisk(riskDict=lookPlanParam,orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '检查制定评估方案提交失败')
        
        #新增专家
        expertParam=copy.deepcopy(FengPingPara.addExpert)
        expertParam['mode']='add'
        expertParam['riskExpert.name']='test%s' % CommonUtil.createRandomString()
        expertParam['riskExpert.sex.id']=RiskExpertSex.BOY
        expertParam['riskExpert.skillTitle.id']=RiskExpertSkillTitle.PROFESSOR
        
        expertParam['riskExpert.belongIndustry.id']=RiskExpertBelongIndustry.NONG
        ret = FengPingIntf.addExpert(riskDict=expertParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '新增失败')
        #5.评估实施>评估，保存
        measureParam=copy.deepcopy(FengPingPara.ExpertObject)
        measureParam['mode']='save'
        measureParam['saveOrSubmitType']='typeIsSave'
        measureParam['operationType']='edit'
        measureParam['riskAssessMeasure.projectReport.id']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='%s'" % riskParam['riskProjectReport.importMatterName'])
        measureParam['riskAssessMeasure.assessType']=makeplanParam['riskAssessPlan.assessmentMode']
        measureParam['riskAssessMeasure.argumentationFormPeople']='论证组织人'
        measureParam['riskAssessMeasure.argumentationTitle']='论证主题'
        measureParam['riskAssessMeasure.argumentationDate']='2015-12-09'
        measureParam['riskAssessMeasure.argumentationAddress']='地点'
        measureParam['riskAssessMeasure.assessMember']= CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskexperts t where t.name='%s'" % expertParam['riskExpert.name'])
        measureParam['riskAssessMeasure.argumentationRecordPelple']='记录人'
        measureParam['riskAssessMeasure.argumentationRecordSituation']='情况记录'
        measureParam['riskAssessMeasure.argumentationOneCompletion']='论证初步结论'
        ret = FengPingIntf.saveMeasureRisk_1(riskDict=measureParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '专家论证保存失败')
        #6.评估实施>评估，提交
        submitParam=copy.deepcopy(FengPingPara.ExpertObject)
        submitParam['ids']= CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='%s'" % riskParam['riskProjectReport.importMatterName'])
        ret=FengPingIntf.SubmitmeasureRisk(riskDict=submitParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '评估实施>评估，提交失败')
        #6.检查评估实施>评估是否提交成功
        checkPar=copy.deepcopy(FengPingPara.measureParam)
        checkPar['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret=FengPingIntf.checkSubmitMeasureRisk_02(riskDict=checkPar,orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '评估实施>评估，提交失败')
        pass
    def testRisk_11(self):#评估实施>评估，提交，评估方式为公式公告
        """风险评估>评估实施，评估并保存项目，评估方式为公示公告"""
        #先新增1个项目
        riskParam = copy.deepcopy(FengPingPara.riskObject) 
        riskParam['riskProjectReport.createOrg.id'] =InitDefaultPara.orgInit['DftWangGeOrgId']
        riskParam['riskProjectReport.importMatterName']='好的%s' % CommonUtil.createRandomString()   
        riskParam['riskProjectReport.projectLeader']='决策主体1'
        riskParam['riskProjectReport.projectClassification.id']=CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '重大工程项目'")#Classification.ONE
        riskParam['riskProjectReport.projectType.id']=CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '农村征地'")#ProjectType.YI
        riskParam['riskProjectReport.beginYearFiling']=PlanInfo.INPLAN
        riskParam['riskProjectReport.memo']='概述'
        riskParam['mode']='add' 
        responseDict = FengPingIntf.addRisk(riskDict=riskParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        #查看是否新增成功
        param = copy.deepcopy(FengPingPara.checkObject)
        param['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret = FengPingIntf.checkAddRisk(riskDict=param, orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')    
        self.assertTrue(ret, '查找失败')
        #评估立项--提交
        InitiationParam=copy.deepcopy(FengPingPara.initiationObject) 
        InitiationParam['riskProjectReport.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        InitiationParam['riskProjectReport.bodyOrg']='评估主体'   
        InitiationParam['riskProjectReport.startDate']='2015-11-19'
        InitiationParam['riskProjectReport.endDate']='2015-11-19'
        InitiationParam['riskProjectReport.assessmentWarn']='30'
        InitiationParam['riskProjectReport.evaluateType']=EvaluateType.EVALUATE
        InitiationParam['riskProjectReport.reviewSuggestion']='概述'
        InitiationParam['modeTemp']='submit'  
        ret = FengPingIntf.SubmitInitiationRisk(riskDict=InitiationParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '评估立项提交失败1')
        #验证是否可以检查到评估立项提交成功的项目
        param = copy.deepcopy(FengPingPara.checkInitiation)
        param['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret = FengPingIntf.checkSubmitInitiationRisk(riskDict=param, orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '检查评估立项提交失败')
        #制定评估方案并提交
        makeplanParam=copy.deepcopy(FengPingPara.makeplanObject)
        makeplanParam['riskAssessPlan.project.id']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        makeplanParam['modeTemp']='submit'
        makeplanParam['riskAssessPlan.assessmentMode']=AssessmentMode.GONGGAO
        makeplanParam['riskAssessPlan.bodyOrg']='评估主体'
        makeplanParam['riskAssessPlan.leader']='评估主体责任人'
        makeplanParam['riskAssessPlan.riskEstimate']='风险点预估'
        makeplanParam['riskAssessPlan.request']='评估要求'
        ret=FengPingIntf.SubmitMakeplanRisk(riskDict=makeplanParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '制定评估方案提交失败')
        #评估实施，保存
        measureParam=copy.deepcopy(FengPingPara.measureObject)
        measureParam['riskAssessMeasure.projectReport.id']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='%s'" % riskParam['riskProjectReport.importMatterName'])
        measureParam['mode']='save'
        measureParam['riskAssessMeasure.assessType']=makeplanParam['riskAssessPlan.assessmentMode']
        measureParam['riskAssessMeasure.advice']='公告内容'
        measureParam['riskAssessMeasure.announcementStartDate']='2015-11-30'
        measureParam['riskAssessMeasure.announcementEndDate']='2015-11-30'
        measureParam['riskAssessMeasure.announcementStyle']='公告方式'
        measureParam['riskAssessMeasure.announcementAdvice']='公告反馈意见1111111111111111'
        ret = FengPingIntf.saveMeasureRisk(riskDict=measureParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '公示公告信息保存失败')
        #5.评估实施>评估，提交
        submitParam=copy.deepcopy(FengPingPara.submitMeasureObject)
        submitParam['ids']= CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='%s'" % riskParam['riskProjectReport.importMatterName'])
        ret=FengPingIntf.SubmitmeasureRisk(riskDict=submitParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '评估实施>评估，提交失败')
        #6.检查评估实施>评估是否提交成功
        checkPar=copy.deepcopy(FengPingPara.measureParam)
        checkPar['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret=FengPingIntf.checkSubmitMeasureRisk(riskDict=checkPar,orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '评估实施>评估，提交失败')
        pass
    def testRisk_12(self):#风险评估>评估报告>评估建议,保存
        """风险评估>评估报告，评估建议并保存项目"""
        #1.先新增1个项目
        riskParam = copy.deepcopy(FengPingPara.riskObject) 
        riskParam['riskProjectReport.createOrg.id'] =InitDefaultPara.orgInit['DftWangGeOrgId']
        riskParam['riskProjectReport.importMatterName']='omgwuwu风险项目%s'%CommonUtil.createRandomString()
        riskParam['riskProjectReport.projectLeader']='决策主体1'
        riskParam['riskProjectReport.projectClassification.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='项目分类', displayName='重大工程项目')
        riskParam['riskProjectReport.projectType.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='项目类别', displayName='公益事业')
        riskParam['riskProjectReport.beginYearFiling']=PlanInfo.INPLAN
        riskParam['riskProjectReport.memo']='概述'
        riskParam['mode']='add'  
        responseDict = FengPingIntf.addRisk(riskDict=riskParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        #查看是否新增成功
        param = copy.deepcopy(FengPingPara.checkObject)
        param['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret = FengPingIntf.checkAddRisk(riskDict=param, orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')    
        self.assertTrue(ret, '查找失败')
        #评估立项--提交
        InitiationParam=copy.deepcopy(FengPingPara.initiationObject) 
        InitiationParam['riskProjectReport.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        InitiationParam['riskProjectReport.bodyOrg']='评估主体'   
        InitiationParam['riskProjectReport.startDate']='2015-11-19'
        InitiationParam['riskProjectReport.endDate']='2015-11-19'
        InitiationParam['riskProjectReport.assessmentWarn']='30'
        InitiationParam['riskProjectReport.evaluateType']=EvaluateType.EVALUATE
        InitiationParam['riskProjectReport.reviewSuggestion']='概述'
        InitiationParam['modeTemp']='submit'  
        ret = FengPingIntf.SubmitInitiationRisk(riskDict=InitiationParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '评估立项提交失败1')
        #验证是否可以检查到评估立项提交成功的项目
        param = copy.deepcopy(FengPingPara.checkInitiation)
        param['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret = FengPingIntf.checkSubmitInitiationRisk(riskDict=param, orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '检查评估立项提交失败')
        #制定评估方案并提交
        makeplanParam=copy.deepcopy(FengPingPara.makeplanObject)
        makeplanParam['riskAssessPlan.project.id']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        makeplanParam['modeTemp']='submit'
        makeplanParam['riskAssessPlan.assessmentMode']=AssessmentMode.GONGGAO
        makeplanParam['riskAssessPlan.bodyOrg']='评估主体'
        makeplanParam['riskAssessPlan.leader']='评估主体责任人'
        makeplanParam['riskAssessPlan.riskEstimate']='风险点预估'
        makeplanParam['riskAssessPlan.request']='评估要求'
        ret=FengPingIntf.SubmitMakeplanRisk(riskDict=makeplanParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '制定评估方案提交失败')
        #评估实施，保存
        measureParam=copy.deepcopy(FengPingPara.measureObject)
        measureParam['riskAssessMeasure.projectReport.id']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='%s'" % riskParam['riskProjectReport.importMatterName'])
        measureParam['mode']='save'
        measureParam['riskAssessMeasure.assessType']=makeplanParam['riskAssessPlan.assessmentMode']
        measureParam['riskAssessMeasure.advice']='公告内容'
        measureParam['riskAssessMeasure.announcementStartDate']='2015-11-30'
        measureParam['riskAssessMeasure.announcementEndDate']='2015-11-30'
        measureParam['riskAssessMeasure.announcementStyle']='公告方式'
        measureParam['riskAssessMeasure.announcementAdvice']='公告反馈意见1111111111111111'
        ret = FengPingIntf.saveMeasureRisk(riskDict=measureParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '公示公告信息保存失败')
        #5.评估实施>评估，提交
        submitParam=copy.deepcopy(FengPingPara.submitMeasureObject)
        submitParam['ids']= CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='%s'" % riskParam['riskProjectReport.importMatterName'])
        ret=FengPingIntf.SubmitmeasureRisk(riskDict=submitParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '评估实施>评估，提交失败')
        #6.检查评估实施>评估是否提交成功
        checkPar=copy.deepcopy(FengPingPara.measureParam)
        checkPar['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret=FengPingIntf.checkSubmitMeasureRisk(riskDict=checkPar,orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '评估实施>评估，提交失败')
        #6.评估报告>评估建议，保存
        suggestParam=copy.deepcopy(FengPingPara.AssessSuggest)
        suggestParam['riskAssessSuggest.project.id']=CommonIntf.getDbQueryResult(dbCommand="select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        suggestParam['mode']='success'
        suggestParam['flag']='false'
        suggestParam['riskAssessSuggest.riskPoint']='风险点'
        suggestParam['riskAssessSuggest.precaution']='预防措施'
        suggestParam['riskAssessSuggest.riskLevel.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='风险等级', displayName='高')
        suggestParam['riskAssessSuggest.suggest.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='建议', displayName='准予实施')
        suggestParam['riskAssessSuggest.advice']='评估意见'
        ret=FengPingIntf.SaveRiskSuggest(riskDict=suggestParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111') 
        self.assertTrue(ret, '评估建议保存失败')
        pass
    def testRisk_13(self):#风险评估>评估报告>评估建议，提交
        """风险评估>评估报告，评估建议并保存项目"""
        #先新增1个项目
        riskParam = copy.deepcopy(FengPingPara.riskObject) 
        riskParam['riskProjectReport.createOrg.id'] =InitDefaultPara.orgInit['DftWangGeOrgId']
        riskParam['riskProjectReport.importMatterName']='风险评估112%s' % CommonUtil.createRandomString()   
        riskParam['riskProjectReport.projectLeader']='决策主体1'
        riskParam['riskProjectReport.projectClassification.id']=Classification.ONE
        riskParam['riskProjectReport.projectType.id']=ProjectType.YI
        riskParam['riskProjectReport.beginYearFiling']=PlanInfo.INPLAN
        riskParam['riskProjectReport.memo']='概述'
        riskParam['mode']='add'  
        responseDict = FengPingIntf.addRisk(riskDict=riskParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        #查看是否新增成功
        param = copy.deepcopy(FengPingPara.checkObject)
        param['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret = FengPingIntf.checkAddRisk(riskDict=param, orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')    
        self.assertTrue(ret, '查找失败')
        #2.对该项目进行评估立项
        InitiationParam=copy.deepcopy(FengPingPara.initiationObject) 
        InitiationParam['riskProjectReport.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        InitiationParam['riskProjectReport.bodyOrg']='评估主体11111111111111111'   
        InitiationParam['riskProjectReport.startDate']='2015-11-19'
        InitiationParam['riskProjectReport.endDate']='2015-11-19'
        InitiationParam['riskProjectReport.assessmentWarn']='30'
        InitiationParam['riskProjectReport.evaluateType']=EvaluateType.EVALUATE
        InitiationParam['riskProjectReport.reviewSuggestion']='概述'
        InitiationParam['modeTemp']='submit'  
        ret = FengPingIntf.SubmitInitiationRisk(riskDict=InitiationParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '评估立项提交失败1')
        #3.对该项目制定评估方案并提交
        makeplanParam=copy.deepcopy(FengPingPara.makeplanObject)
        makeplanParam['riskAssessPlan.project.id']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        makeplanParam['modeTemp']='submit'
        makeplanParam['riskAssessPlan.assessmentMode']=AssessmentMode.GONGGAO 
        makeplanParam['riskAssessPlan.bodyOrg']=InitiationParam['riskProjectReport.bodyOrg']
        makeplanParam['riskAssessPlan.leader']='评估主体责任人'
        makeplanParam['riskAssessPlan.riskEstimate']='风险点预估'
        makeplanParam['riskAssessPlan.request']='评估要求'
        ret=FengPingIntf.SubmitMakeplanRisk(riskDict=makeplanParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        print ret
        self.assertTrue(ret, '制定评估方案提交失败')
        #4.评估实施>评估，保存
        measureParam=copy.deepcopy(FengPingPara.measureObject)
        measureParam['riskAssessMeasure.projectReport.id']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='%s'" % riskParam['riskProjectReport.importMatterName'])
        measureParam['mode']='save'
        measureParam['riskAssessMeasure.assessType']=makeplanParam['riskAssessPlan.assessmentMode']
        measureParam['riskAssessMeasure.advice']='公告内容'
        measureParam['riskAssessMeasure.announcementStartDate']='2015-11-30'
        measureParam['riskAssessMeasure.announcementEndDate']='2015-11-30'
        measureParam['riskAssessMeasure.announcementStyle']='提交的时候保存的'
        measureParam['riskAssessMeasure.announcementAdvice']='提交时候保存的'
        ret = FengPingIntf.saveMeasureRisk(riskDict=measureParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '公示公告信息保存失败')
        #5.评估实施>评估，提交
        measureParam=copy.deepcopy(FengPingPara.measureObject)
        measureParam['ids']=CommonIntf.getDbQueryResult(dbCommand="select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        ret=FengPingIntf.SubmitmeasureRisk(riskDict=measureParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '评估提交失败')
        #6.评估报告>评估建议，提交
        suggestParam=copy.deepcopy(FengPingPara.AssessSuggest)
        suggestParam['riskAssessSuggest.project.id']=CommonIntf.getDbQueryResult(dbCommand="select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        suggestParam['mode']='success'
        suggestParam['flag']='true'
        suggestParam['riskAssessSuggest.riskPoint']='提交时风险点'
        suggestParam['riskAssessSuggest.precaution']='提交时预防措施'
        suggestParam['riskAssessSuggest.riskLevel.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='风险等级', displayName='高')
        suggestParam['riskAssessSuggest.suggest.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='建议', displayName='准予实施')
        suggestParam['riskAssessSuggest.advice']='提交时评估意见'
        ret=FengPingIntf.SubmitRiskSuggest(riskDict=suggestParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '评估建议提交失败')
        #7.检查评估报告>评估建议，提交
        checkParam=copy.deepcopy(FengPingPara.checkSuggestParam)
        checkParam['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret=FengPingIntf.CheckSubmitRiskSuggest(riskDict=checkParam,orgId=riskParam['riskProjectReport.createOrg.id'], username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '检查评估建议提交失败')
        pass
  
    
    def testRisk_14(self):#决策结果>决策意见，保存
        """风险评估>决策结果，决策意见并保存"""
        riskParam = copy.deepcopy(FengPingPara.riskObject) 
        riskParam['riskProjectReport.createOrg.id'] =InitDefaultPara.orgInit['DftWangGeOrgId']
        riskParam['riskProjectReport.importMatterName']='好的%s' % CommonUtil.createRandomString()   
        riskParam['riskProjectReport.projectLeader']='决策主体1'
        riskParam['riskProjectReport.projectClassification.id']=CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '重大工程项目'")#Classification.ONE
        riskParam['riskProjectReport.projectType.id']=CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '农村征地'")#ProjectType.YI
        riskParam['riskProjectReport.beginYearFiling']=PlanInfo.INPLAN
        riskParam['riskProjectReport.memo']='概述'
        riskParam['mode']='add' 
        responseDict = FengPingIntf.addRisk(riskDict=riskParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        #查看是否新增成功
        param = copy.deepcopy(FengPingPara.checkObject)
        param['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret = FengPingIntf.checkAddRisk(riskDict=param, orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')    
        self.assertTrue(ret, '查找失败')
        #2.对该项目进行评估立项
        InitiationParam=copy.deepcopy(FengPingPara.initiationObject) 
        InitiationParam['riskProjectReport.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        InitiationParam['riskProjectReport.bodyOrg']='评估主体11111111111111111'   
        InitiationParam['riskProjectReport.startDate']='2015-11-19'
        InitiationParam['riskProjectReport.endDate']='2015-11-19'
        InitiationParam['riskProjectReport.assessmentWarn']='30'
        InitiationParam['riskProjectReport.evaluateType']=EvaluateType.EVALUATE
        InitiationParam['riskProjectReport.reviewSuggestion']='概述'
        InitiationParam['modeTemp']='submit'  
        ret = FengPingIntf.SubmitInitiationRisk(riskDict=InitiationParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '评估立项提交失败1')
        #3.对该项目制定评估方案并提交
        makeplanParam=copy.deepcopy(FengPingPara.makeplanObject)
        makeplanParam['riskAssessPlan.project.id']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        makeplanParam['modeTemp']='submit'
        makeplanParam['riskAssessPlan.assessmentMode']=AssessmentMode.GONGGAO 
        makeplanParam['riskAssessPlan.bodyOrg']=InitiationParam['riskProjectReport.bodyOrg']
        makeplanParam['riskAssessPlan.leader']='评估主体责任人'
        makeplanParam['riskAssessPlan.riskEstimate']='风险点预估'
        makeplanParam['riskAssessPlan.request']='评估要求'
        ret=FengPingIntf.SubmitMakeplanRisk(riskDict=makeplanParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '制定评估方案提交失败')
        #4.评估实施>评估，保存
        measureParam=copy.deepcopy(FengPingPara.measureObject)
        measureParam['riskAssessMeasure.projectReport.id']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='%s'" % riskParam['riskProjectReport.importMatterName'])
        measureParam['mode']='save'
        measureParam['riskAssessMeasure.assessType']=makeplanParam['riskAssessPlan.assessmentMode']
        measureParam['riskAssessMeasure.advice']='公告内容'
        measureParam['riskAssessMeasure.announcementStartDate']='2015-11-30'
        measureParam['riskAssessMeasure.announcementEndDate']='2015-11-30'
        measureParam['riskAssessMeasure.announcementStyle']='提交的时候保存的'
        measureParam['riskAssessMeasure.announcementAdvice']='提交时候保存的'
        ret = FengPingIntf.saveMeasureRisk(riskDict=measureParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '公示公告信息保存失败')
        #5.评估实施>评估，提交
        measureParam=copy.deepcopy(FengPingPara.measureObject)
        measureParam['ids']=CommonIntf.getDbQueryResult(dbCommand="select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        responseDict=FengPingIntf.SubmitmeasureRisk(riskDict=measureParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '评估提交失败')
        #6.评估报告>评估建议，提交
        suggestParam=copy.deepcopy(FengPingPara.AssessSuggest)
        suggestParam['riskAssessSuggest.project.id']=CommonIntf.getDbQueryResult(dbCommand="select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        suggestParam['mode']='success'
        suggestParam['flag']='true'
        suggestParam['riskAssessSuggest.riskPoint']='提交时风险点'
        suggestParam['riskAssessSuggest.precaution']='提交时预防措施'
        suggestParam['riskAssessSuggest.riskLevel.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='风险等级', displayName='高')
        suggestParam['riskAssessSuggest.suggest.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='建议', displayName='准予实施')
        suggestParam['riskAssessSuggest.advice']='提交时评估意见'
        responseDict=FengPingIntf.SubmitRiskSuggest(riskDict=suggestParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '评估建议提交失败')
        #8.决策结果>决策意见，保存
        riskDecisionAdvice=copy.deepcopy(FengPingPara.RiskDecisionAdvice)
        riskDecisionAdvice['riskDecisionAdvice.project.id']=CommonIntf.getDbQueryResult(dbCommand="select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        riskDecisionAdvice['mode']='success'
        riskDecisionAdvice['flag']='false'
        riskDecisionAdvice['participantNames']='小明'
        riskDecisionAdvice['hearingPersonNameBaks1']='小明'
        riskDecisionAdvice['riskDecisionAdvice.occurTime']='2015-10-10'
        riskDecisionAdvice['riskDecisionAdvice.address']='地点'
        riskDecisionAdvice['riskDecisionAdvice.recorder']='记录人'
        riskDecisionAdvice['riskDecisionAdvice.advice']='决策意见'
        riskDecisionAdvice['riskDecisionAdvice.projectLeader']=riskParam['riskProjectReport.projectLeader']
        riskDecisionAdvice['riskDecisionAdvice.leader']='决策责任人'
        riskDecisionAdvice['riskDecisionAdvice.measures']='决策具体措施'
        riskDecisionAdvice['riskDecisionAdvice.suggest.id']=Conclusion.YES
        riskDecisionAdvice['riskDecisionAdvice.project.proplanExecutionStartdate']='2015-10-10'
        riskDecisionAdvice['riskDecisionAdvice.project.proplanExecutionEnddate']='2015-10-11'
        riskDecisionAdvice['riskDecisionAdvice.record']=Record.NO
        
        ret=FengPingIntf.SaveriskDecisionAdvice(riskDict=riskDecisionAdvice, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        pass
    def testRisk_15(self):#决策结果>决策意见，提交
        """风险评估>决策结果，决策意见并提交"""
        #1.先新增1个项目
        riskParam = copy.deepcopy(FengPingPara.riskObject) 
        riskParam['riskProjectReport.createOrg.id'] =InitDefaultPara.orgInit['DftWangGeOrgId']
        riskParam['riskProjectReport.importMatterName']='omgwuwu风险项目%s'%CommonUtil.createRandomString()
        riskParam['riskProjectReport.projectLeader']='决策主体1'
        riskParam['riskProjectReport.projectClassification.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='项目分类', displayName='重大工程项目')
        riskParam['riskProjectReport.projectType.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='项目类别', displayName='公益事业')
        riskParam['riskProjectReport.beginYearFiling']=PlanInfo.INPLAN
        riskParam['riskProjectReport.memo']='概述'
        riskParam['mode']='add'  
        responseDict = FengPingIntf.addRisk(riskDict=riskParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        #查看是否新增成功
        param = copy.deepcopy(FengPingPara.checkObject)
        param['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret = FengPingIntf.checkAddRisk(riskDict=param, orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')    
        self.assertTrue(ret, '查找失败')
        #2.对该项目进行评估立项并提交
        InitiationParam=copy.deepcopy(FengPingPara.initiationObject) 
        InitiationParam['riskProjectReport.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        InitiationParam['riskProjectReport.bodyOrg']='评估主体11111111111111111'   
        InitiationParam['riskProjectReport.startDate']='2015-11-19'
        InitiationParam['riskProjectReport.endDate']='2015-11-19'
        InitiationParam['riskProjectReport.assessmentWarn']='30'
        InitiationParam['riskProjectReport.evaluateType']=EvaluateType.EVALUATE
        InitiationParam['riskProjectReport.reviewSuggestion']='概述'
        InitiationParam['modeTemp']='submit'  
        ret = FengPingIntf.SubmitInitiationRisk(riskDict=InitiationParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '评估立项提交失败1')
        #验证是否可以检查到评估立项提交成功的项目
        param = copy.deepcopy(FengPingPara.checkInitiation)
        param['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret = FengPingIntf.checkSubmitInitiationRisk(riskDict=param, orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '检查评估立项提交失败')
        
        #3.对该项目制定评估方案并提交
        makeplanParam=copy.deepcopy(FengPingPara.makeplanObject)
        makeplanParam['riskAssessPlan.project.id']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        makeplanParam['modeTemp']='submit'
        makeplanParam['riskAssessPlan.assessmentMode']=AssessmentMode.GONGGAO 
        makeplanParam['riskAssessPlan.bodyOrg']=InitiationParam['riskProjectReport.bodyOrg']
        makeplanParam['riskAssessPlan.leader']='评估主体责任人'
        makeplanParam['riskAssessPlan.riskEstimate']='风险点预估'
        makeplanParam['riskAssessPlan.request']='评估要求'
        ret=FengPingIntf.SubmitMakeplanRisk(riskDict=makeplanParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '制定评估方案提交失败')
        #4.是否可以检查到提交成功的评估方案
        lookPlanParam=copy.deepcopy(FengPingPara.lookPlanParam)
        lookPlanParam['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret = FengPingIntf.checkSubmitMakeplanRisk(riskDict=lookPlanParam,orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '检查制定评估方案提交失败')
        #4.评估实施>评估，保存
        measureParam=copy.deepcopy(FengPingPara.measureObject)
        measureParam['riskAssessMeasure.projectReport.id']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='%s'" % riskParam['riskProjectReport.importMatterName'])
        measureParam['mode']='save'
        measureParam['riskAssessMeasure.assessType']=makeplanParam['riskAssessPlan.assessmentMode']
        measureParam['riskAssessMeasure.advice']='公告内容'
        measureParam['riskAssessMeasure.announcementStartDate']='2015-11-30'
        measureParam['riskAssessMeasure.announcementEndDate']='2015-11-30'
        measureParam['riskAssessMeasure.announcementStyle']='提交的时候保存的'
        measureParam['riskAssessMeasure.announcementAdvice']='提交时候保存的'
        ret = FengPingIntf.saveMeasureRisk(riskDict=measureParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '公示公告信息保存失败')
        #5.评估实施>评估，提交
        measureParam=copy.deepcopy(FengPingPara.measureObject)
        measureParam['ids']=CommonIntf.getDbQueryResult(dbCommand="select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        responseDict=FengPingIntf.SubmitmeasureRisk(riskDict=measureParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '评估提交失败')
        #6.检查评估实施>评估是否提交成功
        checkPar=copy.deepcopy(FengPingPara.measureParam)
        checkPar['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret=FengPingIntf.checkSubmitMeasureRisk(riskDict=checkPar,orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '评估实施>评估，提交失败')
        #6.评估报告>评估建议，提交
        suggestParam=copy.deepcopy(FengPingPara.AssessSuggest)
        suggestParam['riskAssessSuggest.project.id']=CommonIntf.getDbQueryResult(dbCommand="select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        suggestParam['mode']='success'
        suggestParam['flag']='true'
        suggestParam['riskAssessSuggest.riskPoint']='提交时风险点'
        suggestParam['riskAssessSuggest.precaution']='提交时预防措施'
        suggestParam['riskAssessSuggest.riskLevel.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='风险等级', displayName='高')
        suggestParam['riskAssessSuggest.suggest.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='建议', displayName='准予实施')
        suggestParam['riskAssessSuggest.advice']='提交时评估意见'
        ret=FengPingIntf.SubmitRiskSuggest(riskDict=suggestParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '评估建议提交失败')
        #7.检查评估报告>评估建议，提交
        checkParam=copy.deepcopy(FengPingPara.checkSuggestParam)
        checkParam['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret=FengPingIntf.CheckSubmitRiskSuggest(riskDict=checkParam,orgId=riskParam['riskProjectReport.createOrg.id'], username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '检查评估建议提交失败')
       
        #8.决策结果>决策意见，提交
        riskDecisionAdvice=copy.deepcopy(FengPingPara.RiskDecisionAdvice)
        riskDecisionAdvice['riskDecisionAdvice.project.id']=CommonIntf.getDbQueryResult(dbCommand="select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        riskDecisionAdvice['mode']='success'
        riskDecisionAdvice['flag']='true'
        riskDecisionAdvice['participantNames']='小明'
        riskDecisionAdvice['hearingPersonNameBaks1']='小明'
        riskDecisionAdvice['riskDecisionAdvice.occurTime']='2015-10-10'
        riskDecisionAdvice['riskDecisionAdvice.address']='地点'
        riskDecisionAdvice['riskDecisionAdvice.recorder']='记录人'
        riskDecisionAdvice['riskDecisionAdvice.advice']='决策意见'
        riskDecisionAdvice['riskDecisionAdvice.projectLeader']=riskParam['riskProjectReport.projectLeader']
        riskDecisionAdvice['riskDecisionAdvice.leader']='决策责任人'
        riskDecisionAdvice['riskDecisionAdvice.measures']='决策具体措施'
        riskDecisionAdvice['riskDecisionAdvice.suggest.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='建议', displayName='准予实施')
        riskDecisionAdvice['riskDecisionAdvice.project.proplanExecutionStartdate']='2015-10-10'
        riskDecisionAdvice['riskDecisionAdvice.project.proplanExecutionEnddate']='2015-10-11'
        riskDecisionAdvice['riskDecisionAdvice.record']=Record.NO
        ret=FengPingIntf.SubmitRiskDecisionAdvice(riskDict=riskDecisionAdvice, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '决策意见提交失败1')
        #检查决策结果>决策意见是否提交成功
        checkAdvice=copy.deepcopy(FengPingPara.checkRiskDecisionAdvice)
        checkAdvice['importMatterName']= riskParam['riskProjectReport.importMatterName']
        ret=FengPingIntf.CheckSubmitRiskDecisionAdvice(riskDict=checkAdvice, orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '检查决策意见提交失败')
        pass

    def testRisk_16(self):#归档
        """风险评估>决策结果，归档项目"""
        #1.先新增1个项目
        riskParam = copy.deepcopy(FengPingPara.riskObject) 
        riskParam['riskProjectReport.createOrg.id'] =InitDefaultPara.orgInit['DftWangGeOrgId']
        riskParam['riskProjectReport.importMatterName']='好的%s' % CommonUtil.createRandomString()   
        riskParam['riskProjectReport.projectLeader']='决策主体1'
        riskParam['riskProjectReport.projectClassification.id']=CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '重大工程项目'")#Classification.ONE
        riskParam['riskProjectReport.projectType.id']=CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '农村征地'")#ProjectType.YI
        riskParam['riskProjectReport.beginYearFiling']=PlanInfo.INPLAN
        riskParam['riskProjectReport.memo']='概述'
        riskParam['mode']='add' 
        responseDict = FengPingIntf.addRisk(riskDict=riskParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        #查看是否新增成功
        param = copy.deepcopy(FengPingPara.checkObject)
        param['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret = FengPingIntf.checkAddRisk(riskDict=param, orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')    
        self.assertTrue(ret, '查找失败')
        #2.对该项目进行评估立项
        InitiationParam=copy.deepcopy(FengPingPara.initiationObject) 
        InitiationParam['riskProjectReport.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        InitiationParam['riskProjectReport.bodyOrg']='评估主体11111111111111111'   
        InitiationParam['riskProjectReport.startDate']='2015-11-19'
        InitiationParam['riskProjectReport.endDate']='2015-11-19'
        InitiationParam['riskProjectReport.assessmentWarn']='30'
        InitiationParam['riskProjectReport.evaluateType']=EvaluateType.EVALUATE
        InitiationParam['riskProjectReport.reviewSuggestion']='概述'
        InitiationParam['modeTemp']='submit'  
        ret = FengPingIntf.SubmitInitiationRisk(riskDict=InitiationParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '评估立项提交失败')
        #3.对该项目制定评估方案并提交
        makeplanParam=copy.deepcopy(FengPingPara.makeplanObject)
        makeplanParam['riskAssessPlan.project.id']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        makeplanParam['modeTemp']='submit'
        makeplanParam['riskAssessPlan.assessmentMode']=AssessmentMode.GONGGAO 
        makeplanParam['riskAssessPlan.bodyOrg']=InitiationParam['riskProjectReport.bodyOrg']
        makeplanParam['riskAssessPlan.leader']='评估主体责任人'
        makeplanParam['riskAssessPlan.riskEstimate']='风险点预估'
        makeplanParam['riskAssessPlan.request']='评估要求'
        ret=FengPingIntf.SubmitMakeplanRisk(riskDict=makeplanParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '制定评估方案提交失败')
#         #4.评估实施>评估，保存
        measureParam=copy.deepcopy(FengPingPara.measureObject)
        measureParam['riskAssessMeasure.projectReport.id']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='%s'" % riskParam['riskProjectReport.importMatterName'])
        measureParam['mode']='save'
        measureParam['riskAssessMeasure.assessType']=makeplanParam['riskAssessPlan.assessmentMode']
        measureParam['riskAssessMeasure.advice']='公告内容'
        measureParam['riskAssessMeasure.announcementStartDate']='2015-11-30'
        measureParam['riskAssessMeasure.announcementEndDate']='2015-11-30'
        measureParam['riskAssessMeasure.announcementStyle']='提交的时候保存的'
        measureParam['riskAssessMeasure.announcementAdvice']='提交时候保存的'
        ret = FengPingIntf.saveMeasureRisk(riskDict=measureParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '公示公告信息保存失败')
        #5.评估实施>评估，提交
        measureParam=copy.deepcopy(FengPingPara.measureObject)
        measureParam['ids']=CommonIntf.getDbQueryResult(dbCommand="select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        responseDict=FengPingIntf.SubmitmeasureRisk(riskDict=measureParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '评估提交失败')
        #6.评估报告>评估建议，提交
        suggestParam=copy.deepcopy(FengPingPara.AssessSuggest)
        suggestParam['riskAssessSuggest.project.id']=CommonIntf.getDbQueryResult(dbCommand="select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        suggestParam['mode']='success'
        suggestParam['flag']='true'
        suggestParam['riskAssessSuggest.riskPoint']='提交时风险点'
        suggestParam['riskAssessSuggest.precaution']='提交时预防措施'
        suggestParam['riskAssessSuggest.riskLevel.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='风险等级', displayName='高')
        suggestParam['riskAssessSuggest.suggest.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='建议', displayName='准予实施')
        suggestParam['riskAssessSuggest.advice']='提交时评估意见'
        ret=FengPingIntf.SubmitRiskSuggest(riskDict=suggestParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '评估建议提交失败')
        #8.决策结果>决策意见，提交
        riskDecisionAdvice=copy.deepcopy(FengPingPara.RiskDecisionAdvice)
        riskDecisionAdvice['riskDecisionAdvice.project.id']=CommonIntf.getDbQueryResult(dbCommand="select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        riskDecisionAdvice['mode']='success'
        riskDecisionAdvice['flag']='true'
        riskDecisionAdvice['participantNames']='小明'
        riskDecisionAdvice['hearingPersonNameBaks1']='小明'
        riskDecisionAdvice['riskDecisionAdvice.occurTime']='2015-10-10'
        riskDecisionAdvice['riskDecisionAdvice.address']='地点'
        riskDecisionAdvice['riskDecisionAdvice.recorder']='记录人'
        riskDecisionAdvice['riskDecisionAdvice.advice']='决策意见'
        riskDecisionAdvice['riskDecisionAdvice.projectLeader']=riskParam['riskProjectReport.projectLeader']
        riskDecisionAdvice['riskDecisionAdvice.leader']='决策责任人'
        riskDecisionAdvice['riskDecisionAdvice.measures']='决策具体措施'
        riskDecisionAdvice['riskDecisionAdvice.suggest.id']=Conclusion.YES
        riskDecisionAdvice['riskDecisionAdvice.project.proplanExecutionStartdate']='2015-10-10'
        riskDecisionAdvice['riskDecisionAdvice.project.proplanExecutionEnddate']='2015-10-11'
        riskDecisionAdvice['riskDecisionAdvice.record']=Record.NO
        ret=FengPingIntf.SubmitRiskDecisionAdvice(riskDict=riskDecisionAdvice, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '决策意见提交失败')
        #检查决策结果>决策意见是否提交成功
        checkAdvice=copy.deepcopy(FengPingPara.checkRiskDecisionAdvice)
        checkAdvice['importMatterName']= riskParam['riskProjectReport.importMatterName']
        ret=FengPingIntf.CheckSubmitRiskDecisionAdvice(riskDict=checkAdvice, orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '检查决策意见提交失败')
        #归档
        archiveParam=copy.deepcopy(FengPingPara.ArchiveParam)
        archiveParam['riskDecisionTrackEvent.project.id']=CommonIntf.getDbQueryResult(dbCommand="select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        ret=FengPingIntf.Riskarchive(riskDict=archiveParam,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '归档失败')
        #检查归档是否成功
        checkArchiveParam=copy.deepcopy(FengPingPara.checkRiskDecisionAdvice)
        checkArchiveParam['importMatterName']= riskParam['riskProjectReport.importMatterName']
        ret=FengPingIntf.CheckRiskArchive(riskDict=checkArchiveParam, orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '检查归档失败')
        pass
    def testRisk_17(self):#回退
        """风险评估>决策实施跟踪，回退项目到决策结果"""
        #先新增1个项目
        riskParam = copy.deepcopy(FengPingPara.riskObject) 
        riskParam['riskProjectReport.createOrg.id'] =InitDefaultPara.orgInit['DftWangGeOrgId']
        riskParam['riskProjectReport.importMatterName']='风险评估%s' % CommonUtil.createRandomString()   
        riskParam['riskProjectReport.projectLeader']='决策主体1'
        riskParam['riskProjectReport.projectClassification.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='项目分类', displayName='重大工程项目')
        riskParam['riskProjectReport.projectType.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='项目类别', displayName='公益事业')
        riskParam['riskProjectReport.beginYearFiling']=PlanInfo.INPLAN
        riskParam['riskProjectReport.memo']='概述'
        riskParam['mode']='add'  
        responseDict = FengPingIntf.addRisk(riskDict=riskParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        #查看是否新增成功
        param = copy.deepcopy(FengPingPara.checkObject)
        param['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret = FengPingIntf.checkAddRisk(riskDict=param, orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')    
        self.assertTrue(ret, '查找失败')
        
        #然后对该项目进行评估立项并提交
        InitiationParam=copy.deepcopy(FengPingPara.initiationObject) 
        InitiationParam['riskProjectReport.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        InitiationParam['riskProjectReport.bodyOrg']='评估主体'   
        InitiationParam['riskProjectReport.startDate']='2015-11-19'
        InitiationParam['riskProjectReport.endDate']='2015-11-19'
        InitiationParam['riskProjectReport.assessmentWarn']='30'
        InitiationParam['riskProjectReport.evaluateType']=EvaluateType.EVALUATE
        InitiationParam['riskProjectReport.reviewSuggestion']='概述'
        InitiationParam['modeTemp']='submit'  
        ret = FengPingIntf.SubmitInitiationRisk(riskDict=InitiationParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '评估立项提交失败')
        #制定评估方案并提交
        makeplanParam=copy.deepcopy(FengPingPara.makeplanObject)
        makeplanParam['riskAssessPlan.project.id']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        makeplanParam['modeTemp']='submit'
        makeplanParam['riskAssessPlan.assessmentMode']='%s,' % AssessmentMode.GONGGAO 
        makeplanParam['riskAssessPlan.bodyOrg']='评估主体'
        makeplanParam['riskAssessPlan.leader']='评估主体责任人'
        makeplanParam['riskAssessPlan.riskEstimate']='风险点预估'
        makeplanParam['riskAssessPlan.request']='评估要求'
        ret=FengPingIntf.SubmitMakeplanRisk(riskDict=makeplanParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '制定评估方案提交失败')
        #回退
        backParam=copy.deepcopy(FengPingPara.backObject)
        backParam['ids']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        ret=FengPingIntf.backRisk(riskDict=backParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '回退失败')
        #检查是否回退成功
        checkBackParam=copy.deepcopy(FengPingPara.CheckBackParam)
        checkBackParam['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret=FengPingIntf.checkBackRisk(riskDict=checkBackParam, orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '回退失败')
        pass
    def testRisk_18(self):#专家库>新增专家
        """风险评估>专家库，新增专家"""
        #新增专家
        expertParam=copy.deepcopy(FengPingPara.addExpert)
        expertParam['mode']='add'
        expertParam['riskExpert.name']='专家2%s' % CommonUtil.createRandomString()
        expertParam['riskExpert.sex.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='性别(男、女)', displayName='男')
        expertParam['riskExpert.skillTitle.id']=RiskExpertSkillTitle.PROFESSOR
        
        expertParam['riskExpert.belongIndustry.id']=RiskExpertBelongIndustry.NONG
        ret = FengPingIntf.addExpert(riskDict=expertParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '新增失败')
        #检查新增专家是否成功
        checkAddParam=copy.deepcopy(FengPingPara.checkAddParam)
        checkAddParam['name']=expertParam['riskExpert.name']
        ret = FengPingIntf.checkAddExpert(riskDict=checkAddParam,username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')    
        self.assertTrue(ret, '查找失败')
        #修改专家
        updateExpert=copy.deepcopy(FengPingPara.addExpert)
        updateExpert['riskExpert.name']='修改%s'% CommonUtil.createRandomString()
        updateExpert['riskExpert.sex.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='性别(男、女)', displayName='男')
        updateExpert['riskExpert.skillTitle.id']=RiskExpertSkillTitle.PROFESSOR
        updateExpert['riskExpert.belongIndustry.id']=RiskExpertBelongIndustry.NONG
        updateExpert['mode']='edit'
        ret = FengPingIntf.updateExpert(riskDict=updateExpert, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '修改失败')
        #检查修改专家是否成功
        checkAddParam=copy.deepcopy(FengPingPara.checkAddParam)
        checkAddParam['name']=expertParam['riskExpert.name']
        ret = FengPingIntf.checkUpdateExpert(riskDict=checkAddParam,username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')    
        self.assertTrue(ret, '查找失败')
        pass
    

    def testRisk_19(self):
        '''风险评估>计划管理，导入、导出'''
        importRisk=copy.deepcopy(FengPingPara.importRisk)
        importRisk['dataType']='RISKPROJECTREPORT'
        importRisk['templates']='RISKPROJECTREPORT_KEY'
        files = {'upload': ('test.xls', open('C:/autotest_file/importRisk.xls', 'rb'),'applicationnd.ms-excel')}
        ret = FengPingIntf.importRisk(importRisk, files=files,username=userInit['DftWangGeUser'], password='11111111')         
         
        #检查导入
        checkImportRisk=copy.deepcopy(FengPingPara.checkObject)
        checkImportRisk['importMatterName']='测试导入'
        ret=FengPingIntf.checkAddRisk(checkImportRisk, orgId=orgInit['DftWangGeOrgId'], password='11111111')
        self.assertTrue(ret, '查找项目失败')
        pass
    def testRisk_20(self):
        '''风险评估>项目导出'''
        #1.先新增1个项目
        riskParam = copy.deepcopy(FengPingPara.riskObject) 
        riskParam['riskProjectReport.createOrg.id'] =InitDefaultPara.orgInit['DftWangGeOrgId']
        riskParam['riskProjectReport.importMatterName']='omgwuwu风险项目%s'%CommonUtil.createRandomString()
        riskParam['riskProjectReport.projectLeader']='决策主体1'
        riskParam['riskProjectReport.projectClassification.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='项目分类', displayName='重大工程项目')
        riskParam['riskProjectReport.projectType.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='项目类别', displayName='公益事业')
        riskParam['riskProjectReport.beginYearFiling']=PlanInfo.INPLAN
        riskParam['riskProjectReport.memo']='概述'
        riskParam['mode']='add'  
        responseDict = FengPingIntf.addRisk(riskDict=riskParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        #查看是否新增成功
        param = copy.deepcopy(FengPingPara.checkObject)
        param['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret = FengPingIntf.checkAddRisk(riskDict=param, orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')    
        self.assertTrue(ret, '查找失败')
        #2.对该项目进行评估立项并提交
        InitiationParam=copy.deepcopy(FengPingPara.initiationObject) 
        InitiationParam['riskProjectReport.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        InitiationParam['riskProjectReport.bodyOrg']='评估主体11111111111111111'   
        InitiationParam['riskProjectReport.startDate']='2015-11-19'
        InitiationParam['riskProjectReport.endDate']='2015-11-19'
        InitiationParam['riskProjectReport.assessmentWarn']='30'
        InitiationParam['riskProjectReport.evaluateType']=EvaluateType.EVALUATE
        InitiationParam['riskProjectReport.reviewSuggestion']='概述'
        InitiationParam['modeTemp']='submit'  
        ret = FengPingIntf.SubmitInitiationRisk(riskDict=InitiationParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '评估立项提交失败1')
        #验证是否可以检查到评估立项提交成功的项目
        param = copy.deepcopy(FengPingPara.checkInitiation)
        param['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret = FengPingIntf.checkSubmitInitiationRisk(riskDict=param, orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '检查评估立项提交失败')
        
        #3.对该项目制定评估方案并提交
        makeplanParam=copy.deepcopy(FengPingPara.makeplanObject)
        makeplanParam['riskAssessPlan.project.id']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        makeplanParam['modeTemp']='submit'
        makeplanParam['riskAssessPlan.assessmentMode']=AssessmentMode.GONGGAO 
        makeplanParam['riskAssessPlan.bodyOrg']=InitiationParam['riskProjectReport.bodyOrg']
        makeplanParam['riskAssessPlan.leader']='评估主体责任人'
        makeplanParam['riskAssessPlan.riskEstimate']='风险点预估'
        makeplanParam['riskAssessPlan.request']='评估要求'
        ret=FengPingIntf.SubmitMakeplanRisk(riskDict=makeplanParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '制定评估方案提交失败')
        #4.是否可以检查到提交成功的评估方案
        lookPlanParam=copy.deepcopy(FengPingPara.lookPlanParam)
        lookPlanParam['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret = FengPingIntf.checkSubmitMakeplanRisk(riskDict=lookPlanParam,orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '检查制定评估方案提交失败')
        #4.评估实施>评估，保存
        measureParam=copy.deepcopy(FengPingPara.measureObject)
        measureParam['riskAssessMeasure.projectReport.id']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskProjectReport t where t.importMatterName='%s'" % riskParam['riskProjectReport.importMatterName'])
        measureParam['mode']='save'
        measureParam['riskAssessMeasure.assessType']=makeplanParam['riskAssessPlan.assessmentMode']
        measureParam['riskAssessMeasure.advice']='公告内容'
        measureParam['riskAssessMeasure.announcementStartDate']='2015-11-30'
        measureParam['riskAssessMeasure.announcementEndDate']='2015-11-30'
        measureParam['riskAssessMeasure.announcementStyle']='提交的时候保存的'
        measureParam['riskAssessMeasure.announcementAdvice']='提交时候保存的'
        ret = FengPingIntf.saveMeasureRisk(riskDict=measureParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '公示公告信息保存失败')
        #5.评估实施>评估，提交
        measureParam=copy.deepcopy(FengPingPara.measureObject)
        measureParam['ids']=CommonIntf.getDbQueryResult(dbCommand="select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        responseDict=FengPingIntf.SubmitmeasureRisk(riskDict=measureParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '评估提交失败')
        #6.检查评估实施>评估是否提交成功
        checkPar=copy.deepcopy(FengPingPara.measureParam)
        checkPar['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret=FengPingIntf.checkSubmitMeasureRisk(riskDict=checkPar,orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '评估实施>评估，提交失败')
        #6.评估报告>评估建议，提交
        suggestParam=copy.deepcopy(FengPingPara.AssessSuggest)
        suggestParam['riskAssessSuggest.project.id']=CommonIntf.getDbQueryResult(dbCommand="select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        suggestParam['mode']='success'
        suggestParam['flag']='true'
        suggestParam['riskAssessSuggest.riskPoint']='提交时风险点'
        suggestParam['riskAssessSuggest.precaution']='提交时预防措施'
        suggestParam['riskAssessSuggest.riskLevel.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='风险等级', displayName='高')
        suggestParam['riskAssessSuggest.suggest.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='建议', displayName='准予实施')
        suggestParam['riskAssessSuggest.advice']='提交时评估意见'
        ret=FengPingIntf.SubmitRiskSuggest(riskDict=suggestParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '评估建议提交失败')
        #7.检查评估报告>评估建议，提交
        checkParam=copy.deepcopy(FengPingPara.checkSuggestParam)
        checkParam['importMatterName']=riskParam['riskProjectReport.importMatterName']
        ret=FengPingIntf.CheckSubmitRiskSuggest(riskDict=checkParam,orgId=riskParam['riskProjectReport.createOrg.id'], username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '检查评估建议提交失败')
       
        #8.决策结果>决策意见，提交
        riskDecisionAdvice=copy.deepcopy(FengPingPara.RiskDecisionAdvice)
        riskDecisionAdvice['riskDecisionAdvice.project.id']=CommonIntf.getDbQueryResult(dbCommand="select t.id from riskProjectReport t where t.importMatterName='"+riskParam['riskProjectReport.importMatterName']+"'")
        riskDecisionAdvice['mode']='success'
        riskDecisionAdvice['flag']='true'
        riskDecisionAdvice['participantNames']='小明'
        riskDecisionAdvice['hearingPersonNameBaks1']='小明'
        riskDecisionAdvice['riskDecisionAdvice.occurTime']='2015-10-10'
        riskDecisionAdvice['riskDecisionAdvice.address']='地点'
        riskDecisionAdvice['riskDecisionAdvice.recorder']='记录人'
        riskDecisionAdvice['riskDecisionAdvice.advice']='决策意见'
        riskDecisionAdvice['riskDecisionAdvice.projectLeader']=riskParam['riskProjectReport.projectLeader']
        riskDecisionAdvice['riskDecisionAdvice.leader']='决策责任人'
        riskDecisionAdvice['riskDecisionAdvice.measures']='决策具体措施'
        riskDecisionAdvice['riskDecisionAdvice.suggest.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='建议', displayName='准予实施')
        riskDecisionAdvice['riskDecisionAdvice.project.proplanExecutionStartdate']='2015-10-10'
        riskDecisionAdvice['riskDecisionAdvice.project.proplanExecutionEnddate']='2015-10-11'
        riskDecisionAdvice['riskDecisionAdvice.record']=Record.NO
        ret=FengPingIntf.SubmitRiskDecisionAdvice(riskDict=riskDecisionAdvice, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '决策意见提交失败1')
        #检查决策结果>决策意见是否提交成功
        checkAdvice=copy.deepcopy(FengPingPara.checkRiskDecisionAdvice)
        checkAdvice['importMatterName']= riskParam['riskProjectReport.importMatterName']
        ret=FengPingIntf.CheckSubmitRiskDecisionAdvice(riskDict=checkAdvice, orgId=riskParam['riskProjectReport.createOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '检查决策意见提交失败')
        #再导出这个项目
        downLoadRisk = copy.deepcopy(FengPingPara.downLoadRisk)
        downLoadRisk['riskProjectReport.createOrgId'] =InitDefaultPara.orgInit['DftWangGeOrgId']
        response = FengPingIntf.downLoadRisk(downLoadRisk, username=userInit['DftWangGeUser'], password='11111111')         
        with open("C:/autotest_file/test.xls", "wb") as code:
            code.write(response.content)
            
        ret = CommonUtil.checkExcelCellValue('omgwuwu风险项目', 'test.xls','决策实施跟踪清单', 'B4')          
        self.assertTrue(ret, '导出失败')
                         
        pass
if __name__ == "__main__":
    suite = unittest.TestSuite()
#     suite.addTest(FengXianPingGu("tearDown"))
#     suite.addTest(FengXianPingGu("testRisk_01"))#风险评估>计划管理，新增计划项目
#     suite.addTest(FengXianPingGu("testRisk_02"))#风险评估>计划管理，修改计划项目
#     suite.addTest(FengXianPingGu("testRisk_03"))#风险评估>计划管理，删除计划项目
#     suite.addTest(FengXianPingGu("testRisk_04"))#风险评估>计划管理，暂缓和取消暂缓计划项目
#     suite.addTest(FengXianPingGu("testRisk_05"))#风险评估>计划管理，调整和取消调整计划项目
#     suite.addTest(FengXianPingGu("testRisk_06"))#风险评估>计划管理，评估立项保存
#     suite.addTest(FengXianPingGu("testRisk_07"))#风险评估>计划管理，评估立项提交
#     suite.addTest(FengXianPingGu("testRisk_08"))#风险评估>评估立项>制定评估方案保存
#     suite.addTest(FengXianPingGu("testRisk_09"))#风险评估>评估立项>制定评估方案提交
#     suite.addTest(FengXianPingGu("testRisk_10"))#风险评估>评估实施，保存
#     suite.addTest(FengXianPingGu("testRisk_10_1"))#风险评估>评估实施>评估，提交，评估方式为网上联评
#     suite.addTest(FengXianPingGu("testRisk_10_2"))#风险评估>评估实施>评估，提交，评估方式为网上联评
#     suite.addTest(FengXianPingGu("testRisk_11"))#风险评估>评估实施>评估，提交，评估方式为公示公告
#     suite.addTest(FengXianPingGu("testRisk_12"))#风险评估>评估报告>评估建议，保存
#     suite.addTest(FengXianPingGu("testRisk_13"))#风险评估>评估报告>评估建议，提交
#     suite.addTest(FengXianPingGu("testRisk_14"))#决策结果>决策意见，保存
#     suite.addTest(FengXianPingGu("testRisk_15"))#决策结果>决策意见，提交
#     suite.addTest(FengXianPingGu("testRisk_16"))#归档
#     suite.addTest(FengXianPingGu("testRisk_17"))#回退
#     suite.addTest(FengXianPingGu("testRisk_18"))#新增专家
#     suite.addTest(FengXianPingGu("testRisk_09_1"))#制定评估方案并提交，评估方式为网上联评
#     suite.addTest(FengXianPingGu("testRisk_09_2"))#制定评估方案并提交，评估方式为专家论证
#     suite.addTest(FengXianPingGu("testRisk_09_3"))#制定评估方案并提交，评估方式为公示公告.委托评估
#     suite.addTest(FengXianPingGu("testRisk_19"))
#     suite.addTest(FengXianPingGu("testRisk_20"))
    results = unittest.TextTestRunner().run(suite)
    pass