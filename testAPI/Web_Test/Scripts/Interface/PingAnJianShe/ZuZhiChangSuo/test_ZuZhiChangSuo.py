# -*- coding:UTF-8 -*-
'''
Created on 2015-11-24

@author: N-133
'''
from __future__ import unicode_literals
import copy
from COMMON import  Time
from COMMON import CommonUtil
from Interface.PingAnJianShe.Common import CommonIntf
from Interface.PingAnJianShe.ZuZhiChangSuo import ZuZhiChangSuoPara,\
    ZuZhiChangSuoIntf
from Interface.PingAnJianShe.SystemMgr import SystemMgrIntf
import unittest
from CONFIG import InitDefaultPara
from CONFIG.InitDefaultPara import orgInit
from Interface.PingAnJianShe.XiaQuGuanLi import XiaQuGuanLiIntf

# reload(sys)
# sys.setdefaultencoding('utf-8')

class ZuZhiChangSuo(unittest.TestCase):

    def setUp(self):
        SystemMgrIntf.initEnv()
        ZuZhiChangSuoIntf.deleteAllPopulation()
        pass
    
#     新增服务成员
    def testPremise_01(self):
        """新增服务成员"""
        XiaQuGuanLiIntf.xiaQuGuanLiMemberDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        Premise_01Param = copy.deepcopy(ZuZhiChangSuoPara.FuWuChengYuanObject) 
        Premise_01Param['serviceTeamMemberBase.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        Premise_01Param['serviceTeamMemberBase.job'] = '测试职位3'
        Premise_01Param['serviceTeamMemberBase.name'] = '测试服务成员'
        Premise_01Param['isSubmit'] = 'true'
        Premise_01Param['serviceTeamMemberBase.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别(男、女)', displayName='男')
        Premise_01Param['serviceTeamMemberBase.mobile'] = '13011111111'
        responseDict = ZuZhiChangSuoIntf.addFuWuChengYuan(FuWuChengYuanDict=Premise_01Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
#            查看服务人员
        param = copy.deepcopy(ZuZhiChangSuoPara.ChaKanRenYuanObject)
        param['name'] = Premise_01Param['serviceTeamMemberBase.name'] 
        param['job'] = Premise_01Param['serviceTeamMemberBase.job'] 
        ret = ZuZhiChangSuoIntf.checkFuWuChengYuanCompany(companyDict=param, orgId=Premise_01Param['serviceTeamMemberBase.org.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')
#         删除服务人员
        deleteParam = copy.deepcopy(ZuZhiChangSuoPara.delFuWuChengYuan)
        deleteParam['mode'] ='delete'
        deleteParam['selectedIds'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from Serviceteammemberbase t where t.name='测试服务成员'")
        ret = ZuZhiChangSuoIntf.deleteFuWuRenYuan(deleteParam,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        XiaQuGuanLiIntf.xiaQuGuanLiMemberDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        pass
    
#         新增实有单位
    def testCase_01(self):
        """新增/查看实有单位"""
#         新增实有单位
        ZZCSCase_01Param = copy.deepcopy(ZuZhiChangSuoPara.ShiYouDanWeiObject) 
        ZZCSCase_01Param['organizationId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        ZZCSCase_01Param['location.companyName'] = '测试单位%s'% CommonUtil.createRandomString()
        ZZCSCase_01Param['mode'] = 'add'
        ZZCSCase_01Param['location.companyAddress'] = '测试地址1'
        ZZCSCase_01Param['location.businessLicenseNo'] = '营业执照号码1'
        ZZCSCase_01Param['location.orgCode'] = '组织机构代码1'
        responseDict = ZuZhiChangSuoIntf.addShiYouDanWei(ShiYouDanWeiDict=ZZCSCase_01Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        
#            查看实有单位
        param = copy.deepcopy(ZuZhiChangSuoPara.ChaKanDanWeiObject)
        param['companyName'] = ZZCSCase_01Param['location.companyName']
        param['companyAddress'] = ZZCSCase_01Param['location.companyAddress']
        ret = ZuZhiChangSuoIntf.checkShiYouDanWeiCompany(companyDict=param, orgId=ZZCSCase_01Param['organizationId'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')
        pass
    
#     修改实有单位
    def testCase_02(self):
        """修改实有单位"""
#         新增实有单位
        ZZCSCase_01Param = copy.deepcopy(ZuZhiChangSuoPara.ShiYouDanWeiObject) 
        ZZCSCase_01Param['organizationId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        ZZCSCase_01Param['location.companyName'] = '测试单位'
        ZZCSCase_01Param['mode'] = 'add'
        ZZCSCase_01Param['location.companyAddress'] = '测试地址1'
        ZZCSCase_01Param['location.businessLicenseNo'] = '营业执照号码1'
        ZZCSCase_01Param['location.orgCode'] = '组织机构代码1'
        responseDict = ZuZhiChangSuoIntf.addShiYouDanWei(ShiYouDanWeiDict=ZZCSCase_01Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
#            查看实有单位
        param = copy.deepcopy(ZuZhiChangSuoPara.ChaKanDanWeiObject)
        param['companyName'] = ZZCSCase_01Param['location.companyName']
        param['companyAddress'] = ZZCSCase_01Param['location.companyAddress']
        ret = ZuZhiChangSuoIntf.checkShiYouDanWeiCompany(companyDict=param, orgId=ZZCSCase_01Param['organizationId'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')
#         修改实有单位
        ZZCSCase_02Param = copy.deepcopy(ZuZhiChangSuoPara.ShiYouDanWeiObject) 
        ZZCSCase_02Param['organizationId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        ZZCSCase_02Param['location.organization.orgName'] =InitDefaultPara.orgInit['DftWangGeOrg']
        ZZCSCase_02Param['location.companyName'] = '修改测试名称'
        ZZCSCase_02Param['mode'] = 'edit'
        ZZCSCase_02Param['location.companyAddress'] = '修改测试地址'
        ZZCSCase_02Param['location.businessLicenseNo'] = '修改营业执照号码'
        ZZCSCase_02Param['location.orgCode'] = '修改组织机构代码'
        ret = ZuZhiChangSuoIntf.modifyShiYouDanWei(modifyObject=ZZCSCase_02Param,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '修改失败')
#         查看是否修改成功
        param = copy.deepcopy(ZuZhiChangSuoPara.ChaKanDanWeiObject)
        param['companyName'] = ZZCSCase_02Param['location.companyName']
        param['companyAddress'] = ZZCSCase_02Param['location.companyAddress']
        ret = ZuZhiChangSuoIntf.checkShiYouDanWeiCompany(companyDict=param, orgId=ZZCSCase_02Param['organizationId'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')
        pass
  
# 新增巡场情况   
    def testCase_03(self):
        """新增巡场情况"""
        XiaQuGuanLiIntf.xiaQuGuanLiMemberDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
#         新增服务成员
        Premise_01Param = copy.deepcopy(ZuZhiChangSuoPara.FuWuChengYuanObject) 
        Premise_01Param['serviceTeamMemberBase.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        Premise_01Param['serviceTeamMemberBase.job'] = '测试职位3'
        Premise_01Param['serviceTeamMemberBase.name'] = '测试服务成员'
        Premise_01Param['isSubmit'] = 'true'
        Premise_01Param['serviceTeamMemberBase.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别(男、女)', displayName='男')
        Premise_01Param['serviceTeamMemberBase.mobile'] = '13011111111'
        responseDict = ZuZhiChangSuoIntf.addFuWuChengYuan(FuWuChengYuanDict=Premise_01Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        #            查看服务人员
        param = copy.deepcopy(ZuZhiChangSuoPara.ChaKanRenYuanObject)
        param['name'] = Premise_01Param['serviceTeamMemberBase.name'] 
        param['job'] = Premise_01Param['serviceTeamMemberBase.job'] 
        ret = ZuZhiChangSuoIntf.checkFuWuChengYuanCompany(companyDict=param, orgId=Premise_01Param['serviceTeamMemberBase.org.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')
        
#         新增实有单位
        ZZCSCase_01Param = copy.deepcopy(ZuZhiChangSuoPara.ShiYouDanWeiObject) 
        ZZCSCase_01Param['organizationId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        ZZCSCase_01Param['location.companyName'] = '测试单位'
        ZZCSCase_01Param['mode'] = 'add'
        ZZCSCase_01Param['location.companyAddress'] = '测试地址1'
        ZZCSCase_01Param['location.businessLicenseNo'] = '营业执照号码1'
        ZZCSCase_01Param['location.orgCode'] = '组织机构代码1'
        responseDict = ZuZhiChangSuoIntf.addShiYouDanWei(ShiYouDanWeiDict=ZZCSCase_01Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
#            查看实有单位
        param = copy.deepcopy(ZuZhiChangSuoPara.ChaKanDanWeiObject)
        param['companyName'] = ZZCSCase_01Param['location.companyName']
        param['companyAddress'] = ZZCSCase_01Param['location.companyAddress']
        ret = ZuZhiChangSuoIntf.checkShiYouDanWeiCompany(companyDict=param, orgId=ZZCSCase_01Param['organizationId'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')
        
#         新增巡场记录
        ZZCSCase_04Param = copy.deepcopy(ZuZhiChangSuoPara.XunChangQingKuangObject) 
        ZZCSCase_04Param['serviceRecord.organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        ZZCSCase_04Param['serviceRecord.recordType'] = '0'
        ZZCSCase_04Param['mode'] = 'add'
        ZZCSCase_04Param['isSubmit'] = 'true'
        ZZCSCase_04Param['serviceRecord.userOrgId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        ZZCSCase_04Param['serviceRecord.occurDate'] = Time.getCurrentDate()
        ZZCSCase_04Param['serviceRecord.occurPlace'] = '服务地点%s'%CommonUtil.createRandomString()
        ZZCSCase_04Param['serviceRecord.serviceMembers'] = '%s-测试服务成员-0'%CommonIntf.getDbQueryResult(dbCommand = "select t.id from SERVICETEAMMEMBERBASE t where t.name='测试服务成员'")
        ZZCSCase_04Param['serviceRecord.serviceObjects'] = '%s-测试单位-actualCompany'%CommonIntf.getDbQueryResult(dbCommand = "select t.id from actualCompany t where t.companyname='测试单位'")
        responseDict = ZuZhiChangSuoIntf.addXunChangQingKuang(XunChangQingKuangDict=ZZCSCase_04Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        
#         查看巡场情况是否新增成功
        param = copy.deepcopy(ZuZhiChangSuoPara.ChaKanXunChangQingKuang)
        param['occurPlace'] = ZZCSCase_04Param['serviceRecord.occurPlace']
        ret = ZuZhiChangSuoIntf.checkXunChangQingKuangiCompany(companyDict=param, OrgId=ZZCSCase_04Param['serviceRecord.organization.id'] ,username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')
        
#         删除服务人员
        deleteParam = copy.deepcopy(ZuZhiChangSuoPara.delFuWuChengYuan)
        deleteParam['mode'] ='delete'
        deleteParam['selectedIds'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from Serviceteammemberbase t where t.name='测试服务成员'")
        ret = ZuZhiChangSuoIntf.deleteFuWuRenYuan(deleteParam,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        XiaQuGuanLiIntf.xiaQuGuanLiMemberDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')  
        pass
    
#     新增/修改安全生产重点
    def testCase_04(self):
        """新增/修改安全生产重点"""
        testCase_04Param = copy.deepcopy(ZuZhiChangSuoPara.addAnQuanShengChan) 
        testCase_04Param['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_04Param['enterprise.name'] = '测试安全生产重点%s' % CommonUtil.createRandomString()
        testCase_04Param['enterprise.keyType'] = 'safetyProductionKey'
        testCase_04Param['mode'] = 'add'
        testCase_04Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_04Param['placeTypeName'] = '安全生产重点'
        testCase_04Param['enterprise.address'] = '测试地址1'
        testCase_04Param['enterprise.legalPerson'] = '法人代表1'
        testCase_04Param['enterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='企业类型', displayName='规上企业')
        responseDict = ZuZhiChangSuoIntf.addAnQuanShengChan(AnQuanShengChanDict=testCase_04Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')        
        
#         查看新增安全生产重点
        param = copy.deepcopy(ZuZhiChangSuoPara.ChaKanAnQuanShengChan)
        param['name'] = testCase_04Param['enterprise.name']
        ret = ZuZhiChangSuoIntf.checkAnQuanShengChan(companyDict=param, orgId=testCase_04Param['ownerOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')       

#         修改安全生产重点
        testCase_05Param = copy.deepcopy(ZuZhiChangSuoPara.UpdateAnQuanShengChan) 
        testCase_05Param['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_05Param['enterprise.name'] = '测试安全生产重点1%s' % CommonUtil.createRandomString()
        testCase_05Param['enterprise.keyType'] = 'safetyProductionKey'
        testCase_05Param['mode'] = 'edit'
        testCase_05Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_05Param['placeTypeName'] = '安全生产重点'
        testCase_05Param['enterprise.address'] = '测试地址1'
        testCase_05Param['enterprise.legalPerson'] = '法人代表1'
        testCase_05Param['enterprise.id'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from ENTERPRISES t where t.name='%s' and t.keytype='%s'"%(testCase_04Param['enterprise.name'] ,testCase_05Param['enterprise.keyType'] ))
        testCase_05Param['enterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='企业类型', displayName='规上企业')
        responseDict = ZuZhiChangSuoIntf.UpdateAnQuanShengChan(AnQuanShengChanDict=testCase_05Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改失败')        

#         查看修改安全生产重点
        param = copy.deepcopy(ZuZhiChangSuoPara.ChaKanAnQuanShengChan)
        param['name'] = testCase_05Param['enterprise.name']
        ret = ZuZhiChangSuoIntf.checkAnQuanShengChan(companyDict=param, orgId=testCase_04Param['ownerOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')       

        pass    
    
    
    def testCase_05(self):
        """新增/修改消防安全重点"""
#         新增消防安全重点
        testCase_05Param = copy.deepcopy(ZuZhiChangSuoPara.addXiaoFangAnQuan) 
        testCase_05Param['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_05Param['enterprise.name'] = '测试场所名称%s' % CommonUtil.createRandomString()
        testCase_05Param['enterprise.keyType'] = 'fireSafetyKey'
        testCase_05Param['mode'] = 'add'
        testCase_05Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_05Param['placeTypeName'] = '消防安全重点'
        testCase_05Param['enterprise.address'] = '测试场所地址1'
        testCase_05Param['enterprise.legalPerson'] = '测试负责人'
        testCase_05Param['enterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='消防安全重点类别', displayName='商场')
        responseDict = ZuZhiChangSuoIntf.addXiaoFangAnQuan(XiaoFangAnQuanDict=testCase_05Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')     
        
#         查看消防安全重点
        param = copy.deepcopy(ZuZhiChangSuoPara.XiaoFangAnQuan)
        param['name'] = testCase_05Param['enterprise.name']
        param['address'] = testCase_05Param['enterprise.address']
        ret = ZuZhiChangSuoIntf.checkXiaoFangAnQuanCompany(companyDict=param, OrgId=testCase_05Param['ownerOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')      
        
#         修改消防安全重点
        testCase_06Param = copy.deepcopy(ZuZhiChangSuoPara.UpdateXiaoFangAnQuan) 
        testCase_06Param['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_06Param['enterprise.name'] = '测试场所名称1%s' % CommonUtil.createRandomString()
        testCase_06Param['enterprise.keyType'] = 'fireSafetyKey'
        testCase_06Param['mode'] = 'edit'
        testCase_06Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_06Param['placeTypeName'] = '消防安全重点'
        testCase_06Param['enterprise.address'] = '测试场所地址1'
        testCase_06Param['enterprise.legalPerson'] = '测试负责人'
        testCase_06Param['enterprise.id'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from ENTERPRISES t where t.name='%s' and t.keytype='%s'"%(testCase_05Param['enterprise.name'] ,testCase_05Param['enterprise.keyType']  ))
        testCase_06Param['enterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='消防安全重点类别', displayName='商场')
        responseDict = ZuZhiChangSuoIntf.UpdateXiaoFangAnQuan(XiaoFangAnQuanDict=testCase_06Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改失败')            

#         查看消防安全重点
        param = copy.deepcopy(ZuZhiChangSuoPara.XiaoFangAnQuan)
        param['name'] = testCase_06Param['enterprise.name']
        param['address'] = testCase_06Param['enterprise.address']
        ret = ZuZhiChangSuoIntf.checkXiaoFangAnQuanCompany(companyDict=param, OrgId=testCase_05Param['ownerOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')      

        pass
    
    def testCase_06(self):
        """新增/修改治安重点"""
#         新增治安重点
        testCase_06Param = copy.deepcopy(ZuZhiChangSuoPara.addZhiAnZhongDian) 
        testCase_06Param['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_06Param['enterprise.name'] = '测试场所名称%s' % CommonUtil.createRandomString()
        testCase_06Param['enterprise.keyType'] = 'securityKey'
        testCase_06Param['mode'] = 'add'
        testCase_06Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_06Param['placeTypeName'] = '治安重点'
        testCase_06Param['enterprise.address'] = '测试场所地址1'
        testCase_06Param['enterprise.legalPerson'] = '测试负责人'
        testCase_06Param['enterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='治安重点类别', displayName='城乡结合部')
        responseDict = ZuZhiChangSuoIntf.addZhiAnZhongDian(ZhiAnZhongDianDict=testCase_06Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')           
        
#         查看治安重点
        param = copy.deepcopy(ZuZhiChangSuoPara.ZhiAnZhongDian)
        param['name'] = testCase_06Param['enterprise.name']
        param['address'] = testCase_06Param['enterprise.address']
        ret = ZuZhiChangSuoIntf.checkZhiAnZhongDianCompany(companyDict=param, OrgId=testCase_06Param['ownerOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')              
        
#         修改治安重点
        testCase_07Param = copy.deepcopy(ZuZhiChangSuoPara.UpdateZhiAnZhongDian) 
        testCase_07Param['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_07Param['enterprise.name'] = '测试场所名称%s' % CommonUtil.createRandomString()
        testCase_07Param['enterprise.keyType'] = 'securityKey'
        testCase_07Param['mode'] = 'add'
        testCase_07Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_07Param['placeTypeName'] = '治安重点'
        testCase_07Param['enterprise.address'] = '测试场所地址1'
        testCase_07Param['enterprise.legalPerson'] = '测试负责人'
        testCase_07Param['enterprise.id'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from ENTERPRISES t where t.name='%s' and t.keytype='%s'"%(testCase_06Param['enterprise.name'] ,testCase_06Param['enterprise.keyType']  ))
        testCase_07Param['enterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='治安重点类别', displayName='城乡结合部')
        responseDict = ZuZhiChangSuoIntf.UpdateZhiAnZhongDian(ZhiAnZhongDianDict=testCase_07Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改失败')              
        
#         查看治安重点
        param = copy.deepcopy(ZuZhiChangSuoPara.ZhiAnZhongDian)
        param['name'] = testCase_07Param['enterprise.name']
        param['address'] = testCase_07Param['enterprise.address']
        ret = ZuZhiChangSuoIntf.checkZhiAnZhongDianCompany(companyDict=param, OrgId=testCase_06Param['ownerOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')           
        
        pass    
    
    def testCase_07(self):
        """新增/修改学校"""
#         新增学校
        testCase_07Param = copy.deepcopy(ZuZhiChangSuoPara.addXueXiao) 
        testCase_07Param['orgId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_07Param['school.chineseName'] = '测试学校名称%s' % CommonUtil.createRandomString()
        testCase_07Param['school.kind.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='学校性质', displayName='公办')
        testCase_07Param['mode'] = 'add'
        testCase_07Param['school.hasCertificate'] = '请选择'
        testCase_07Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_07Param['placeTypeName'] = '学校'
        testCase_07Param['school.address'] = '测试学校地址1'
        testCase_07Param['school.president'] = '测试校长'
        testCase_07Param['school.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='学校类型', displayName='小学')
        responseDict = ZuZhiChangSuoIntf.addXueXiao(XueXiaoDict=testCase_07Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')  

#         查看学校
        param = copy.deepcopy(ZuZhiChangSuoPara.XueXiao)
        param['chineseName'] = testCase_07Param['school.chineseName']
        param['address'] = testCase_07Param['school.address']
        ret = ZuZhiChangSuoIntf.checkXueXiaoCompany(companyDict=param, OrgId=testCase_07Param['orgId'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')    

#         修改学校
        testCase_08Param = copy.deepcopy(ZuZhiChangSuoPara.UpdateXueXiao) 
        testCase_08Param['orgId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_08Param['school.chineseName'] = '测试学校名称11%s' % CommonUtil.createRandomString()
        testCase_08Param['school.kind.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='学校性质', displayName='公办')
        testCase_08Param['mode'] = 'edit'
        testCase_08Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_08Param['placeTypeName'] = '学校'
        testCase_08Param['school.address'] = '测试学校地址1'
        testCase_08Param['school.president'] = '测试校长'
        testCase_08Param['school.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='学校类型', displayName='小学')
        testCase_08Param['school.orgInternalCode'] =CommonIntf.getDbQueryResult(dbCommand="select t.orginternalcode from SCHOOLS t where t.chinesename='%s'"%testCase_07Param['school.chineseName'] )
        testCase_08Param['school.organization.id'] =InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_08Param['school.createUser'] =InitDefaultPara.userInit['DftWangGeUser']
        testCase_08Param['school.createDate'] =Time.getCurrentDateAndTime()
        testCase_08Param['school.hasCertificate'] ='false'
        testCase_08Param['school.id'] =CommonIntf.getDbQueryResult(dbCommand="select t.id from SCHOOLS t where t.chinesename='%s'"%testCase_07Param['school.chineseName'] )
        responseDict = ZuZhiChangSuoIntf.UpdateXueXiao(XueXiaoDict=testCase_08Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改失败')  

#         查看学校
        param = copy.deepcopy(ZuZhiChangSuoPara.XueXiao)
        param['chineseName'] = testCase_08Param['school.chineseName']
        param['address'] = testCase_08Param['school.address']
        ret = ZuZhiChangSuoIntf.checkXueXiaoCompany(companyDict=param, OrgId=testCase_07Param['orgId'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')    

        pass    
    
    def testCase_08(self):
        """新增/修改医院"""
#         新增医院
        testCase_08Param = copy.deepcopy(ZuZhiChangSuoPara.addYiYuan) 
        testCase_08Param['organizationId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_08Param['hospital.hospitalName'] = '测试医院名称%s' % CommonUtil.createRandomString()
        testCase_08Param['hospital.personLiableTelephone'] = '1234-12341234'
        testCase_08Param['mode'] = 'add'
        testCase_08Param['hospital.organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_08Param['hospital.personLiableMobileNumber'] = '13411111111'
        testCase_08Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_08Param['hospital.address'] = '测试医院地址1'
        testCase_08Param['hospital.personLiable'] = '测试综治负责人'
        responseDict = ZuZhiChangSuoIntf.addYiYuan(YiYuanDict=testCase_08Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')  
        
#         查看医院
        param = copy.deepcopy(ZuZhiChangSuoPara.YiYuan)
        param['hospitalName'] = testCase_08Param['hospital.hospitalName']
        param['address'] = testCase_08Param['hospital.address']
        ret = ZuZhiChangSuoIntf.checkYiYuanCompany(companyDict=param, OrgId=testCase_08Param['organizationId'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')           
        
#         修改医院
        testCase_09Param = copy.deepcopy(ZuZhiChangSuoPara.UpdateYiYuan) 
        testCase_09Param['organizationId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_09Param['hospital.hospitalName'] = '测试医院名称11%s' % CommonUtil.createRandomString()
        testCase_09Param['hospital.personLiableTelephone'] = '1234-12341234'
        testCase_09Param['mode'] = 'edit'
        testCase_09Param['hospital.id'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from hospitals t where t.hospitalname='%s'"%testCase_08Param['hospital.hospitalName'])
        testCase_09Param['hospital.organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_09Param['hospital.personLiableMobileNumber'] = '13411111111'
        testCase_09Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_09Param['hospital.address'] = '测试医院地址1'
        testCase_09Param['hospital.personLiable'] = '测试综治负责人'
        responseDict = ZuZhiChangSuoIntf.UpdateYiYuan(YiYuanDict=testCase_09Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改失败')  

#         查看医院
        param = copy.deepcopy(ZuZhiChangSuoPara.YiYuan)
        param['hospitalName'] = testCase_09Param['hospital.hospitalName']
        param['address'] = testCase_09Param['hospital.address']
        ret = ZuZhiChangSuoIntf.checkYiYuanCompany(companyDict=param, OrgId=testCase_08Param['organizationId'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')     
        
        pass    
    
    def testCase_09(self):
        """新增/修改危险化学品单位"""
#         新增危险化学品单位
        testCase_09Param = copy.deepcopy(ZuZhiChangSuoPara.addWeiXianHuaXuePing) 
        testCase_09Param['organizationId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_09Param['location.unitName'] = '测试单位名称%s' % CommonUtil.createRandomString()
        testCase_09Param['mode'] = 'add'
        testCase_09Param['location.organization.orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        responseDict = ZuZhiChangSuoIntf.addWeiXianHuaXuePing(WeiXianHuaXuePingDict=testCase_09Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')  

#         查看危险化学品单位
        param = copy.deepcopy(ZuZhiChangSuoPara.WeiXianHuaXuePing)
        param['unitName'] = testCase_09Param['location.unitName']
        ret = ZuZhiChangSuoIntf.checkWeiXianHuaXuePingCompany(companyDict=param, OrgId=testCase_09Param['organizationId'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')      

#         修改危险化学品单位
        testCase_009Param = copy.deepcopy(ZuZhiChangSuoPara.UpdateWeiXianHuaXuePing) 
        testCase_009Param['organizationId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_009Param['location.organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_009Param['location.unitName'] = '测试单位名称11%s' % CommonUtil.createRandomString()
        testCase_009Param['mode'] = 'edit'
        testCase_009Param['location.id'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from DANGEROUSCHEMICALSUNIT t where t.unitname='%s'"%testCase_09Param['location.unitName'])
        testCase_009Param['location.organization.orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        responseDict = ZuZhiChangSuoIntf.UpdateWeiXianHuaXuePing(WeiXianHuaXuePingDict=testCase_009Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改失败')  

#         查看危险化学品单位
        param = copy.deepcopy(ZuZhiChangSuoPara.WeiXianHuaXuePing)
        param['unitName'] = testCase_009Param['location.unitName']
        ret = ZuZhiChangSuoIntf.checkWeiXianHuaXuePingCompany(companyDict=param, OrgId=testCase_09Param['organizationId'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')      

        pass    
    
    def testCase_10(self):
        """新增/修改上网服务单位"""
#         新增上网服务单位
        testCase_10Param = copy.deepcopy(ZuZhiChangSuoPara.addShangWanFuWu) 
        testCase_10Param['location.organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_10Param['location.placeName'] = '测试单位名称%s' % CommonUtil.createRandomString()
        testCase_10Param['mode'] = 'add'
        testCase_10Param['ajaxUrl'] = '/baseinfo/internetBarManage/hasDuplicateInternetBarLocation.action'
        testCase_10Param['location.organization.orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        responseDict = ZuZhiChangSuoIntf.addShangWanFuWu(ShangWanFuWuDict=testCase_10Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')          
        
#         查看上网服务单位
        param = copy.deepcopy(ZuZhiChangSuoPara.ShangWanFuWu)
        param['placeName'] = testCase_10Param['location.placeName']
        ret = ZuZhiChangSuoIntf.checkShangWanFuWuCompany(companyDict=param, OrgId=testCase_10Param['location.organization.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')      
  
#         修改上网服务单位
        testCase_100Param = copy.deepcopy(ZuZhiChangSuoPara.UpdateShangWanFuWu) 
        testCase_100Param['location.organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_100Param['location.placeName'] = '测试单位名称11%s' % CommonUtil.createRandomString()
        testCase_100Param['mode'] = 'edit'
        testCase_100Param['location.id'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from INTERNETBAR t where t.placename='%s'"%testCase_10Param['location.placeName'])
        testCase_100Param['ajaxUrl'] = '/baseinfo/internetBarManage/hasDuplicateInternetBarLocation.action'
        testCase_100Param['location.organization.orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        responseDict = ZuZhiChangSuoIntf.UpdateShangWanFuWu(ShangWanFuWuDict=testCase_100Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改失败')    

#         查看上网服务单位
        param = copy.deepcopy(ZuZhiChangSuoPara.ShangWanFuWu)
        param['placeName'] = testCase_100Param['location.placeName']
        ret = ZuZhiChangSuoIntf.checkShangWanFuWuCompany(companyDict=param, OrgId=testCase_10Param['location.organization.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')      
        
        pass    
    
    
    def testCase_11(self):
        """新增/修改公共场所"""
#         新增公共场所
        testCase_11Param = copy.deepcopy(ZuZhiChangSuoPara.addShangWanFuWu) 
        testCase_11Param['location.organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_11Param['location.placeName'] = '测试公共场所名称%s' % CommonUtil.createRandomString()
        testCase_11Param['location.placeAddress'] = '测试场所地址'
        testCase_11Param['mode'] = 'add'
        testCase_11Param['ajaxUrl'] = '/baseinfo/publicPlaceManage/hasDuplicatePublicPlaceLocation.action'
        testCase_11Param['location.organization.orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        responseDict = ZuZhiChangSuoIntf.addGongGongChangSuo(GongGongChangSuoDict=testCase_11Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')        
        
#         查看公共场所
        param = copy.deepcopy(ZuZhiChangSuoPara.GongGongChangSuo)
        param['placeName'] = testCase_11Param['location.placeName']
        ret = ZuZhiChangSuoIntf.checkGongGongChangSuoCompany(companyDict=param, OrgId=testCase_11Param['location.organization.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')              

#         修改公共场所
        testCase_111Param = copy.deepcopy(ZuZhiChangSuoPara.UpdateShangWanFuWu1) 
        testCase_111Param['location.organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_111Param['location.placeName'] = '测试公共场所名称11%s' % CommonUtil.createRandomString()
        testCase_111Param['location.placeAddress'] = '测试场所地址'
        testCase_111Param['mode'] = 'edit'
        testCase_111Param['location.id'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from PUBLICPLACE t where t.placename='%s'"%testCase_11Param['location.placeName'])
        testCase_111Param['ajaxUrl'] = '/baseinfo/publicPlaceManage/hasDuplicatePublicPlaceLocation.action'
        testCase_111Param['location.organization.orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        responseDict = ZuZhiChangSuoIntf.UpdateShangWanFuWu1(GongGongChangSuoDict=testCase_111Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改失败')

#         查看公共场所
        param = copy.deepcopy(ZuZhiChangSuoPara.GongGongChangSuo)
        param['placeName'] = testCase_111Param['location.placeName']
        ret = ZuZhiChangSuoIntf.checkGongGongChangSuoCompany(companyDict=param, OrgId=testCase_11Param['location.organization.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败') 
        
        pass    
    
    def testCase_12(self):
        """新增/修改公共复杂场所"""
#         新增公共复杂场所
        testCase_12Param = copy.deepcopy(ZuZhiChangSuoPara.addGongGongFuZaChangSuo) 
        testCase_12Param['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_12Param['commonComplexPlace.name'] = '测试公共复杂场所名称%s' % CommonUtil.createRandomString()
        testCase_12Param['commonComplexPlace.legalPerson'] = '测试负责人'
        testCase_12Param['mode'] = 'add'
        testCase_12Param['commonComplexPlace_orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        responseDict = ZuZhiChangSuoIntf.addGongGongFuZaChangSuo(GongGongFuZaChangSuoDict=testCase_12Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')             
        
#         查看公共复杂场所
        param = copy.deepcopy(ZuZhiChangSuoPara.GongGongFuZaChangSuo)
        param['name'] = testCase_12Param['commonComplexPlace.name']
        ret = ZuZhiChangSuoIntf.checkGongGongFuZaChangSuoCompany(companyDict=param, OrgId=testCase_12Param['ownerOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')              
        
#         修改公共复杂场所
        testCase_122Param = copy.deepcopy(ZuZhiChangSuoPara.UpdateGongGongFuZaChangSuo) 
        testCase_122Param['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_122Param['commonComplexPlace.name'] = '测试公共复杂场所名称11%s' % CommonUtil.createRandomString()
        testCase_122Param['commonComplexPlace.legalPerson'] = '测试负责人'
        testCase_122Param['mode'] = 'edit'
        testCase_122Param['commonComplexPlace.id'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from COMMONCOMPLEXPLACES t where t.name='%s'"%testCase_12Param['commonComplexPlace.name'] )
        testCase_122Param['commonComplexPlace_orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        responseDict = ZuZhiChangSuoIntf.UpdateGongGongFuZaChangSuo(GongGongFuZaChangSuoDict=testCase_122Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改失败')        
        
#         查看公共复杂场所
        param = copy.deepcopy(ZuZhiChangSuoPara.GongGongFuZaChangSuo)
        param['name'] = testCase_122Param['commonComplexPlace.name']
        ret = ZuZhiChangSuoIntf.checkGongGongFuZaChangSuoCompany(companyDict=param, OrgId=testCase_12Param['ownerOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')                           
        
        pass    
    
    def testCase_13(self):
        """新增/修改特种行业"""
#         新增特种行业
        testCase_13Param = copy.deepcopy(ZuZhiChangSuoPara.addGongGongFuZaChangSuo) 
        testCase_13Param['organizationId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_13Param['specialTrade.name'] = '测试特种行业名称%s' % CommonUtil.createRandomString()
        testCase_13Param['specialTrade.personLiable'] = '测试负责人'
        testCase_13Param['specialTrade.address'] = '测试企业地址'
        testCase_13Param['specialTrade.organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_13Param['specialTrade.personLiableTelephone'] = '0571-12345678'
        testCase_13Param['specialTrade.personLiableMobileNumber'] = '13411111111'
        testCase_13Param['specialTrade.type.id'] =  CommonIntf.getIdByDomainAndDisplayName(domainName='特种行业类型', displayName='旅馆')
        testCase_13Param['specialTrade.legalPerson'] = '测试法人代表'
        testCase_13Param['mode'] = 'add'
        testCase_13Param['specialTrade.organization.orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        responseDict = ZuZhiChangSuoIntf.addTeZhongHangYe(TeZhongHangYeDict=testCase_13Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')           
        
#         查看特种行业
        param = copy.deepcopy(ZuZhiChangSuoPara.TeZhongHangYe)
        param['name'] = testCase_13Param['specialTrade.name']
        ret = ZuZhiChangSuoIntf.checkTeZhongHangYeCompany(companyDict=param, OrgId=testCase_13Param['organizationId'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')           
        
#         修改特种行业
        testCase_133Param = copy.deepcopy(ZuZhiChangSuoPara.updatetezhonghangye) 
        testCase_133Param['organizationId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_133Param['specialTrade.name'] = '测试特种行业名称11%s' % CommonUtil.createRandomString()
        testCase_133Param['specialTrade.personLiable'] = '测试负责人'
        testCase_133Param['specialTrade.address'] = '测试企业地址'
        testCase_133Param['specialTrade.organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_133Param['specialTrade.personLiableTelephone'] = '0571-12345678'
        testCase_133Param['specialTrade.personLiableMobileNumber'] = '13411111111'
        testCase_133Param['specialTrade.type.id'] =  CommonIntf.getIdByDomainAndDisplayName(domainName='特种行业类型', displayName='旅馆')
        testCase_133Param['specialTrade.legalPerson'] = '测试法人代表'
        testCase_133Param['mode'] = 'edit'
        testCase_133Param['specialTrade.id'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from SPECIALTRADES t where t.name='%s'"%testCase_13Param['specialTrade.name'] )
        testCase_133Param['specialTrade.organization.orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        responseDict = ZuZhiChangSuoIntf.addTeZhongHangYe(TeZhongHangYeDict=testCase_133Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改失败')              

#         查看特种行业
        param = copy.deepcopy(ZuZhiChangSuoPara.TeZhongHangYe)
        param['name'] = testCase_133Param['specialTrade.name']
        ret = ZuZhiChangSuoIntf.checkTeZhongHangYeCompany(companyDict=param, OrgId=testCase_13Param['organizationId'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')               
        
        pass    
    
    def testCase_14(self):
        """新增/修改其他场所"""
#         新增其他场所
        testCase_14Param = copy.deepcopy(ZuZhiChangSuoPara.addQiTaChangSuo) 
        testCase_14Param['organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_14Param['otherLocale.name'] = '测试场所名称%s' % CommonUtil.createRandomString()
        testCase_14Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_14Param['otherLocale.type.id'] =  CommonIntf.getIdByDomainAndDisplayName(domainName='其他场所类型', displayName='个体诊所')
        testCase_14Param['mode'] = 'add'
        responseDict = ZuZhiChangSuoIntf.addQiTaChangSuo(QiTaChangSuoDict=testCase_14Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')             
         
#         查看其他场所
        param = copy.deepcopy(ZuZhiChangSuoPara.QiTaChangSuo)
        param['name'] = testCase_14Param['otherLocale.name']
        ret = ZuZhiChangSuoIntf.checkQiTaChangSuoCompany(companyDict=param, OrgId=testCase_14Param['organization.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')                    
         
#         修改其他场所
        testCase_144Param = copy.deepcopy(ZuZhiChangSuoPara.UpdateQiTaChangSuo) 
        testCase_144Param['organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_144Param['otherLocale.name'] = '测试场所名称11%s' % CommonUtil.createRandomString()
        testCase_144Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_144Param['otherLocale.type.id'] =  CommonIntf.getIdByDomainAndDisplayName(domainName='其他场所类型', displayName='个体诊所')
        testCase_144Param['mode'] = 'edit'
        testCase_144Param['otherLocale.id'] =  CommonIntf.getDbQueryResult(dbCommand="select t.id from OTHERLOCALES t where t.name='%s'"%testCase_14Param['otherLocale.name'] )
        responseDict = ZuZhiChangSuoIntf.UpdateQiTaChangSuo(QiTaChangSuoDict=testCase_144Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改失败')       
        
#         查看其他场所
        param = copy.deepcopy(ZuZhiChangSuoPara.QiTaChangSuo)
        param['name'] = testCase_144Param['otherLocale.name']
        ret = ZuZhiChangSuoIntf.checkQiTaChangSuoCompany(companyDict=param, OrgId=testCase_14Param['organization.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')                 
         
        pass    
         
    def testCase_15(self):
        """新增/修改社会组织"""
#         新增社会组织
        testCase_15Param = copy.deepcopy(ZuZhiChangSuoPara.addSheHuiZuZhi) 
        testCase_15Param['organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_15Param['newSocietyOrganizations.name'] = '测试组织名称%s' % CommonUtil.createRandomString()
        testCase_15Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_15Param['newSocietyOrganizations.type.id'] =  CommonIntf.getIdByDomainAndDisplayName(domainName='社会组织类型', displayName='社会团体')
        testCase_15Param['placeTypeName'] = '社会组织'
        testCase_15Param['keyType'] = 'newSocietyOrganizations'
        testCase_15Param['mode'] = 'add'
        testCase_15Param['newSocietyOrganizations.subType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='社会组织类型分类', displayName='学术性团体')
        testCase_15Param['newSocietyOrganizations.legalPerson'] = '测试法定代表人'
        responseDict = ZuZhiChangSuoIntf.addSheHuiZuZhi(SheHuiZuZhiDict=testCase_15Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')              
        
#         查看社会组织
        param = copy.deepcopy(ZuZhiChangSuoPara.SheHuiZuZhi)
        param['name'] = testCase_15Param['newSocietyOrganizations.name']
        ret = ZuZhiChangSuoIntf.checkSheHuiZuZhiCompany(companyDict=param, OrgId=testCase_15Param['organization.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')  
        
#         修改社会组织
        testCase_155Param = copy.deepcopy(ZuZhiChangSuoPara.updateSheHuiZuZhi) 
        testCase_155Param['organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_155Param['newSocietyOrganizations.name'] = '测试组织名称11%s' % CommonUtil.createRandomString()
        testCase_155Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_155Param['newSocietyOrganizations.type.id'] =  CommonIntf.getIdByDomainAndDisplayName(domainName='社会组织类型', displayName='社会团体')
        testCase_155Param['placeTypeName'] = '社会组织'
        testCase_155Param['keyType'] = 'newSocietyOrganizations'
        testCase_155Param['mode'] = 'edit'
        testCase_155Param['newSocietyOrganizations.id'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from NEWSOCIETYORGANIZATIONS t where t.name='%s'"%testCase_15Param['newSocietyOrganizations.name'] )
        testCase_155Param['newSocietyOrganizations.legalPerson'] = '测试法定代表人'
        responseDict = ZuZhiChangSuoIntf.updateSheHuiZuZhi(SheHuiZuZhiDict=testCase_155Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改失败')          
        
#         查看社会组织
        param = copy.deepcopy(ZuZhiChangSuoPara.SheHuiZuZhi)
        param['name'] = testCase_155Param['newSocietyOrganizations.name']
        ret = ZuZhiChangSuoIntf.checkSheHuiZuZhiCompany(companyDict=param, OrgId=testCase_15Param['organization.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')          
        
        pass

    def testCase_16(self):
        """新增/修改新经济组织"""
#         新增新经济组织
        testCase_16Param = copy.deepcopy(ZuZhiChangSuoPara.addXinJingJiZuZhi) 
        testCase_16Param['newEconomicOrganizationsDomain.organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_16Param['newEconomicOrganizationsDomain.name'] = '测试名称%s' % CommonUtil.createRandomString()
        testCase_16Param['newEconomicOrganizationsDomain.organization.orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_16Param['newEconomicOrganizationsDomain.style.id'] =  CommonIntf.getIdByDomainAndDisplayName(domainName='新经济组织类别', displayName='个体工商户')
        testCase_16Param['newEconomicOrganizationsDomain.residence'] = '测试住所'
        testCase_16Param['newEconomicOrganizationsDomain.licenseNumber'] = '测试营业执照号码%s'% CommonUtil.createRandomString()
        testCase_16Param['mode'] = 'add'
        testCase_16Param['newEconomicOrganizationsDomain.validityStartDate'] = '2015-12-08'
        testCase_16Param['newEconomicOrganizationsDomain.validityEndDate'] = '2015-12-09'
        testCase_16Param['newEconomicOrganizationsDomain.chief'] = '测试负责人'
        responseDict = ZuZhiChangSuoIntf.addXinJingJiZuZhi(XinJingJiZuZhiDict=testCase_16Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')           
        
#         查看新经济组织
        param = copy.deepcopy(ZuZhiChangSuoPara.XinJingJiZuZhi)
        param['name'] = testCase_16Param['newEconomicOrganizationsDomain.name']
        ret = ZuZhiChangSuoIntf.checkXinJingJiZuZhiCompany(companyDict=param, OrgId=testCase_16Param['newEconomicOrganizationsDomain.organization.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')          
        
#         修改新经济组织
        testCase_166Param = copy.deepcopy(ZuZhiChangSuoPara.updateXinJingJiZuZhi) 
        testCase_166Param['newEconomicOrganizationsDomain.organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_166Param['newEconomicOrganizationsDomain.name'] = '测试名称11%s' % CommonUtil.createRandomString()
        testCase_166Param['newEconomicOrganizationsDomain.organization.orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_166Param['newEconomicOrganizationsDomain.style.id'] =  CommonIntf.getIdByDomainAndDisplayName(domainName='新经济组织类别', displayName='个体工商户')
        testCase_166Param['newEconomicOrganizationsDomain.residence'] = '测试住所'
        testCase_166Param['newEconomicOrganizationsDomain.licenseNumber'] = '测试营业执照号码%s'% CommonUtil.createRandomString()
        testCase_166Param['mode'] = 'edit'
        testCase_166Param['newEconomicOrganizationsDomain.id'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from NEWECONOMICORGANIZATIONS t where t.residence='%s'"%testCase_16Param['newEconomicOrganizationsDomain.name'] )
        testCase_166Param['newEconomicOrganizationsDomain.validityStartDate'] = '2015-12-08'
        testCase_166Param['newEconomicOrganizationsDomain.validityEndDate'] = '2015-12-09'
        testCase_166Param['newEconomicOrganizationsDomain.chief'] = '测试负责人'
        responseDict = ZuZhiChangSuoIntf.updateXinJingJiZuZhi(XinJingJiZuZhiDict=testCase_166Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改失败')           
        
#         查看新经济组织
        param = copy.deepcopy(ZuZhiChangSuoPara.XinJingJiZuZhi)
        param['name'] = testCase_166Param['newEconomicOrganizationsDomain.name']
        ret = ZuZhiChangSuoIntf.checkXinJingJiZuZhiCompany(companyDict=param, OrgId=testCase_16Param['newEconomicOrganizationsDomain.organization.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')               
        
        pass    

    def testCase_17(self):
        """新增/修改规上企业"""
#         新增规上企业
        testCase_17Param = copy.deepcopy(ZuZhiChangSuoPara.addGuiShangQiYe) 
        testCase_17Param['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_17Param['enterprise.name'] = '测试企业名称%s' % CommonUtil.createRandomString()
        testCase_17Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_17Param['enterprise.keyType'] =  'enterpriseKey'
        testCase_17Param['enterprise.address'] = '测试企业地址%s'% CommonUtil.createRandomString()
        testCase_17Param['placeTypeName'] = '规上企业'
        testCase_17Param['mode'] = 'add'
        testCase_17Param['enterprise.legalPerson'] = '测试法人代表'
        responseDict = ZuZhiChangSuoIntf.addGuiShangQiYe(GuiShangQiYeDict=testCase_17Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败') 

#         查看规上企业
        param = copy.deepcopy(ZuZhiChangSuoPara.GuiShangQiYe)
        param['address'] = testCase_17Param['enterprise.address']
        param['name'] = testCase_17Param['enterprise.name']
        ret = ZuZhiChangSuoIntf.checkGuiShangQiYeCompany(companyDict=param, OrgId=testCase_17Param['ownerOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')   
        
#         修改规上企业
        testCase_177Param = copy.deepcopy(ZuZhiChangSuoPara.updateGuiShangQiYe) 
        testCase_177Param['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_177Param['enterprise.name'] = '测试企业名称11%s' % CommonUtil.createRandomString()
        testCase_177Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_177Param['enterprise.keyType'] =  'enterpriseKey'
        testCase_177Param['enterprise.address'] = '测试企业地址%s'% CommonUtil.createRandomString()
        testCase_177Param['placeTypeName'] = '规上企业'
        testCase_177Param['mode'] = 'edit'
        testCase_177Param['enterprise.id'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from ENTERPRISES t where t.name='%s' and t.keytype='%s'"%(testCase_17Param['enterprise.name'] ,testCase_17Param['enterprise.keyType']   ))
        testCase_177Param['enterprise.legalPerson'] = '测试法人代表'
        responseDict = ZuZhiChangSuoIntf.updateGuiShangQiYe(GuiShangQiYeDict=testCase_177Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改失败') 

#         查看规上企业
        param = copy.deepcopy(ZuZhiChangSuoPara.GuiShangQiYe)
        param['address'] = testCase_177Param['enterprise.address']
        param['name'] = testCase_177Param['enterprise.name']
        ret = ZuZhiChangSuoIntf.checkGuiShangQiYeCompany(companyDict=param, OrgId=testCase_17Param['ownerOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')           

        pass        
    
    def testCase_18(self):
        """新增/修改规下企业"""
#         新增规下企业
        testCase_18Param = copy.deepcopy(ZuZhiChangSuoPara.addGuiXiaQiYe) 
        testCase_18Param['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_18Param['enterprise.name'] = '测试企业名称%s' % CommonUtil.createRandomString()
        testCase_18Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_18Param['enterprise.keyType'] =  'enterpriseDownKey'
        testCase_18Param['enterprise.address'] = '测试企业地址%s'% CommonUtil.createRandomString()
        testCase_18Param['placeTypeName'] = '规上企业'
        testCase_18Param['mode'] = 'add'
        testCase_18Param['enterprise.legalPerson'] = '测试法人代表'
        ZuZhiChangSuoIntf.addGuiXiaQiYe(GuiXiaQiYeDict=testCase_18Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')

#         查看规下企业
        param = copy.deepcopy(ZuZhiChangSuoPara.GuiXiaQiYe)
        param['address'] = testCase_18Param['enterprise.address']
        param['name'] = testCase_18Param['enterprise.name']
        ret = ZuZhiChangSuoIntf.checkGuiXiaQiYeCompany(companyDict=param, OrgId=testCase_18Param['ownerOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')   
        
#         修改规下企业
        testCase_188Param = copy.deepcopy(ZuZhiChangSuoPara.UpdateGuiXiaQiYe) 
        testCase_188Param['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_188Param['enterprise.name'] = '测试企业名称11%s' % CommonUtil.createRandomString()
        testCase_188Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_188Param['enterprise.keyType'] =  'enterpriseDownKey'
        testCase_188Param['enterprise.address'] = '测试企业地址%s'% CommonUtil.createRandomString()
        testCase_188Param['placeTypeName'] = '规上企业'
        testCase_188Param['mode'] = 'edit'
        testCase_188Param['enterprise.id'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from ENTERPRISES t where t.name='%s' and t.keytype='%s'"%(testCase_18Param['enterprise.name']  ,testCase_18Param['enterprise.keyType']   ))
        testCase_188Param['enterprise.legalPerson'] = '测试法人代表'
        ZuZhiChangSuoIntf.UpdateGuiXiaQiYe(GuiXiaQiYeDict=testCase_188Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')

#         查看规下企业
        param = copy.deepcopy(ZuZhiChangSuoPara.GuiXiaQiYe)
        param['address'] = testCase_188Param['enterprise.address']
        param['name'] = testCase_188Param['enterprise.name']
        ret = ZuZhiChangSuoIntf.checkGuiXiaQiYeCompany(companyDict=param, OrgId=testCase_18Param['ownerOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')          

        pass    

    def testCase_19(self):
        """新增/修改无证无照场所"""
#         新增无证无照场所
        testCase_19Param = copy.deepcopy(ZuZhiChangSuoPara.addWuZhengWuZhao) 
        testCase_19Param['orgId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_19Param['withoutPlace.proprietor'] = '测试经营者%s' % CommonUtil.createRandomString()
        testCase_19Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_19Param['withoutPlace.enteringORimport'] =  'entering'
        testCase_19Param['withoutPlace.mobileNumber'] = '123456'
        testCase_19Param['withoutPlace.operateAddress'] = '测试经营地址%s'% CommonUtil.createRandomString()
        testCase_19Param['lawtypes'] = CommonIntf.getIdByDomainAndDisplayName(domainName='违法类型', displayName='食品安全')
        testCase_19Param['withoutPlace.disposetype.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='处理情况', displayName='未处理')
        testCase_19Param['mode'] = 'add'
        testCase_19Param['withoutPlace.findDate'] = '2015-12-09'
        responseDict = ZuZhiChangSuoIntf.addWuZhengWuZhao(WuZhengWuZhaoDict=testCase_19Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')         
        
#         查看无证无照场所
        param = copy.deepcopy(ZuZhiChangSuoPara.WuZhengWuZhao)
        param['proprietor'] = testCase_19Param['withoutPlace.proprietor']
        ret = ZuZhiChangSuoIntf.checkWuZhengWuZhaoCompany(companyDict=param, OrgId=testCase_19Param['orgId'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')        
        
#         修改无证无照场所
        testCase_199Param = copy.deepcopy(ZuZhiChangSuoPara.updateWuZhengWuZhao) 
        testCase_199Param['orgId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_199Param['withoutPlace.proprietor'] = '测试经营者11%s' % CommonUtil.createRandomString()
        testCase_199Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_199Param['withoutPlace.enteringORimport'] =  'entering'
        testCase_199Param['withoutPlace.mobileNumber'] = '123456'
        testCase_199Param['withoutPlace.operateAddress'] = '测试经营地址%s'% CommonUtil.createRandomString()
        testCase_199Param['lawtypes'] = CommonIntf.getIdByDomainAndDisplayName(domainName='违法类型', displayName='食品安全')
        testCase_199Param['withoutPlace.disposetype.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='处理情况', displayName='未处理')
        testCase_199Param['mode'] = 'edit'
        testCase_199Param['withoutPlace.id'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from WITHOUTPLACE t where t.proprietor='%s'"%testCase_19Param['withoutPlace.proprietor'] )
        testCase_199Param['withoutPlace.organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_199Param['withoutPlace.findDate'] = '2015-12-09'
        responseDict = ZuZhiChangSuoIntf.updateWuZhengWuZhao(WuZhengWuZhaoDict=testCase_199Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改失败')         
        
#         查看无证无照场所
        param = copy.deepcopy(ZuZhiChangSuoPara.WuZhengWuZhao)
        param['proprietor'] = testCase_199Param['withoutPlace.proprietor']
        ret = ZuZhiChangSuoIntf.checkWuZhengWuZhaoCompany(companyDict=param, OrgId=testCase_19Param['orgId'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')             
        
        pass  
    
    def testCase_20(self):
        """新增治安管理负责人"""
#         新增服务成员
        XiaQuGuanLiIntf.xiaQuGuanLiMemberDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        Premise_01Param = copy.deepcopy(ZuZhiChangSuoPara.FuWuChengYuanObject) 
        Premise_01Param['serviceTeamMemberBase.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        Premise_01Param['serviceTeamMemberBase.job'] = '测试职位3'
        Premise_01Param['serviceTeamMemberBase.name'] = '测试服务成员%s'% CommonUtil.createRandomString()
        Premise_01Param['isSubmit'] = 'true'
        Premise_01Param['serviceTeamMemberBase.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别(男、女)', displayName='男')
        Premise_01Param['serviceTeamMemberBase.mobile'] = '13011111111'
        responseDict = ZuZhiChangSuoIntf.addFuWuChengYuan(FuWuChengYuanDict=Premise_01Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        #            查看服务人员
        param = copy.deepcopy(ZuZhiChangSuoPara.ChaKanRenYuanObject)
        param['name'] = Premise_01Param['serviceTeamMemberBase.name'] 
        param['job'] = Premise_01Param['serviceTeamMemberBase.job'] 
        ret = ZuZhiChangSuoIntf.checkFuWuChengYuanCompany(companyDict=param, orgId=Premise_01Param['serviceTeamMemberBase.org.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')
        
#         新增实有单位
        ZZCSCase_01Param = copy.deepcopy(ZuZhiChangSuoPara.ShiYouDanWeiObject) 
        ZZCSCase_01Param['organizationId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        ZZCSCase_01Param['location.companyName'] = '测试单位'
        ZZCSCase_01Param['mode'] = 'add'
        ZZCSCase_01Param['location.companyAddress'] = '测试地址1'
        ZZCSCase_01Param['location.businessLicenseNo'] = '营业执照号码1'
        ZZCSCase_01Param['location.orgCode'] = '组织机构代码1'
        responseDict = ZuZhiChangSuoIntf.addShiYouDanWei(ShiYouDanWeiDict=ZZCSCase_01Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
#            查看实有单位
        param = copy.deepcopy(ZuZhiChangSuoPara.ChaKanDanWeiObject)
        param['companyName'] = ZZCSCase_01Param['location.companyName']
        param['companyAddress'] = ZZCSCase_01Param['location.companyAddress']
        ret = ZuZhiChangSuoIntf.checkShiYouDanWeiCompany(companyDict=param, orgId=ZZCSCase_01Param['organizationId'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')
        
#         新增治安管理负责人
        testCase_20Param = copy.deepcopy(ZuZhiChangSuoPara.addGuanLiZhiAn) 
        testCase_20Param['serviceMemberWithObject.memberId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from SERVICETEAMMEMBERBASE t where t.name='%s'"%(Premise_01Param['serviceTeamMemberBase.name']))
        testCase_20Param['serviceMemberWithObject.objectId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from actualCompany t where t.companyname='测试单位'")
        testCase_20Param['serviceMemberWithObject.objectName'] = '测试单位'
        testCase_20Param['serviceMemberWithObject.objectType'] = 'actualCompany'
        testCase_20Param['serviceMemberWithObject.objectLogout'] = '1'
        testCase_20Param['serviceMemberWithObject.onDuty'] = '1'
        testCase_20Param['serviceMemberWithObject.teamMember'] = '1'
        responseDict = ZuZhiChangSuoIntf.addGuanLiZhiAn(GuanLiZhiAnDict=testCase_20Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        
#            查看治安管理负责人
        param = copy.deepcopy(ZuZhiChangSuoPara.ChaKanDanWeiObject)
        param['memberName'] = Premise_01Param['serviceTeamMemberBase.name']
        param['memberId'] = testCase_20Param['serviceMemberWithObject.memberId'] 
        ret = ZuZhiChangSuoIntf.checkGuanLiZhiAnCompany(companyDict=param, objectId=testCase_20Param['serviceMemberWithObject.objectId'],objectName=testCase_20Param['serviceMemberWithObject.objectName'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')
        XiaQuGuanLiIntf.xiaQuGuanLiMemberDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        pass      
    

    def testCase_21(self):
        """转移实有单位"""
#         新增实有单位
        ZZCSCase_01Param = copy.deepcopy(ZuZhiChangSuoPara.ShiYouDanWeiObject) 
        ZZCSCase_01Param['organizationId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        ZZCSCase_01Param['location.companyName'] = '测试单位'
        ZZCSCase_01Param['mode'] = 'add'
        ZZCSCase_01Param['location.companyAddress'] = '测试地址1'
        ZZCSCase_01Param['location.businessLicenseNo'] = '营业执照号码1'
        ZZCSCase_01Param['location.orgCode'] = '组织机构代码1'
        responseDict = ZuZhiChangSuoIntf.addShiYouDanWei(ShiYouDanWeiDict=ZZCSCase_01Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
#            查看实有单位
        param = copy.deepcopy(ZuZhiChangSuoPara.ChaKanDanWeiObject)
        param['companyName'] = ZZCSCase_01Param['location.companyName']
        param['companyAddress'] = ZZCSCase_01Param['location.companyAddress']
        ret = ZuZhiChangSuoIntf.checkShiYouDanWeiCompany(companyDict=param, orgId=ZZCSCase_01Param['organizationId'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')        
        
#         转移实有单位
        testCase_21Param = copy.deepcopy(ZuZhiChangSuoPara.zhuanYi) 
        testCase_21Param['orgId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_21Param['toOrgId'] = InitDefaultPara.orgInit['DftWangGeOrgId1']
        testCase_21Param['ids'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from actualCompany t where t.companyname='测试单位'")
        responseDict = ZuZhiChangSuoIntf.zhuanYi(zhuanYiDict=testCase_21Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
#         self.assertTrue(responseDict.result, '转移失败')        
        
#       查看转移实有单位
        param = copy.deepcopy(ZuZhiChangSuoPara.ChaKanDanWeiObject)
        param['companyName'] = ZZCSCase_01Param['location.companyName']
        param['companyAddress'] = ZZCSCase_01Param['location.companyAddress']
        ret = ZuZhiChangSuoIntf.checkzhuanYiCompany(companyDict=param, OrgId=testCase_21Param['toOrgId'],username=InitDefaultPara.userInit['DftWangGeUser1'],password='11111111')         
        self.assertTrue(ret, '查找失败')         
        
        pass        
    
    def testCase_22(self):
        """导入导出实有单位"""
#         新增实有单位
        ZZCSCase_01Param = copy.deepcopy(ZuZhiChangSuoPara.ShiYouDanWeiObject) 
        ZZCSCase_01Param['organizationId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        ZZCSCase_01Param['location.companyName'] = '测试单位%s'% CommonUtil.createRandomString()
        ZZCSCase_01Param['mode'] = 'add'
        ZZCSCase_01Param['location.companyAddress'] = '测试地址1'
        ZZCSCase_01Param['location.businessLicenseNo'] = '营业执照号码1'
        ZZCSCase_01Param['location.orgCode'] = '组织机构代码1'
        responseDict = ZuZhiChangSuoIntf.addShiYouDanWei(ShiYouDanWeiDict=ZZCSCase_01Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        
#            查看实有单位
        param = copy.deepcopy(ZuZhiChangSuoPara.ChaKanDanWeiObject)
        param['companyName'] = ZZCSCase_01Param['location.companyName']
        param['companyAddress'] = ZZCSCase_01Param['location.companyAddress']
        ret = ZuZhiChangSuoIntf.checkShiYouDanWeiCompany(companyDict=param, orgId=ZZCSCase_01Param['organizationId'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')
        
#        导入实有单位        
        testCase_22 = copy.deepcopy(ZuZhiChangSuoPara.dataShiYouDanWei)
        testCase_22['dataType']='actualCompany'
        testCase_22['templates']='ACTUALCOMPANY'
        files = {'upload': ('test.xls', open('C:/autotest_file/shiyoudanwei.xls', 'rb'),'applicationnd.ms-excel')}
        ZuZhiChangSuoIntf.dataShiYouDanWei(testCase_22, files=files,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')         

        param = copy.deepcopy(ZuZhiChangSuoPara.ChaKanDanWeiObject)
        param['companyName'] = '测试单位名称'
        param['companyAddress'] = '测试单位地址'
        ret = ZuZhiChangSuoIntf.checkShiYouDanWeiCompany(param, orgId=orgInit['DftWangGeOrgId'],username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')          
        self.assertTrue(ret, '查找导入实有单位失败')
        
        
#         导出实有单位
        downLoad = copy.deepcopy(ZuZhiChangSuoPara.dldataShiYouDanWei)
        downLoad['organizationId']=orgInit['DftWangGeOrgId']
        response = ZuZhiChangSuoIntf.dldataShiYouRenKou(downLoad, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')         
        with open("C:/autotest_file/testshiyoudanwei.xls", "wb") as code:
            code.write(response.content)
            
        ret = CommonUtil.checkExcelCellValue(param['companyName'], 'testshiyoudanwei.xls','实有单位表', 'A4')          
        self.assertTrue(ret, '导出失败')        
        pass   
    
    def testCase_23(self):    
        """导出安全生产重点"""
#         新增安全生产重点
        testCase_04Param = copy.deepcopy(ZuZhiChangSuoPara.addAnQuanShengChan) 
        testCase_04Param['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_04Param['enterprise.name'] = '测试安全生产重点%s' % CommonUtil.createRandomString()
        testCase_04Param['enterprise.keyType'] = 'safetyProductionKey'
        testCase_04Param['mode'] = 'add'
        testCase_04Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_04Param['placeTypeName'] = '安全生产重点'
        testCase_04Param['enterprise.address'] = '测试地址1'
        testCase_04Param['enterprise.legalPerson'] = '法人代表1'
        testCase_04Param['enterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='企业类型', displayName='规上企业')
        responseDict = ZuZhiChangSuoIntf.addAnQuanShengChan(AnQuanShengChanDict=testCase_04Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')        
        
#         查看新增安全生产重点
        param = copy.deepcopy(ZuZhiChangSuoPara.ChaKanAnQuanShengChan)
        param['name'] = testCase_04Param['enterprise.name']
        ret = ZuZhiChangSuoIntf.checkAnQuanShengChan(companyDict=param, orgId=testCase_04Param['ownerOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')       
                
        downLoad = copy.deepcopy(ZuZhiChangSuoPara.dldataAnQuanShengChanZhongDian)
        downLoad['orgId']=orgInit['DftWangGeOrgId']
        response = ZuZhiChangSuoIntf.dldataAnQuanShengChan(downLoad,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')         
        with open("C:/autotest_file/anquanshengchanzhongdian.xls", "wb") as code:
            code.write(response.content)
            
        ret = CommonUtil.checkExcelCellValue(testCase_04Param['enterprise.name'], 'anquanshengchanzhongdian.xls','安全生产重点', 'A4')          
        self.assertTrue(ret, '导出失败')        
        pass   

    def testCase_24(self):    
        """导出消防安全重点"""
#         新增消防安全重点
        testCase_05Param = copy.deepcopy(ZuZhiChangSuoPara.addXiaoFangAnQuan) 
        testCase_05Param['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_05Param['enterprise.name'] = '测试场所名称%s' % CommonUtil.createRandomString()
        testCase_05Param['enterprise.keyType'] = 'fireSafetyKey'
        testCase_05Param['mode'] = 'add'
        testCase_05Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_05Param['placeTypeName'] = '消防安全重点'
        testCase_05Param['enterprise.address'] = '测试场所地址1'
        testCase_05Param['enterprise.legalPerson'] = '测试负责人'
        testCase_05Param['enterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='消防安全重点类别', displayName='商场')
        responseDict = ZuZhiChangSuoIntf.addXiaoFangAnQuan(XiaoFangAnQuanDict=testCase_05Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')     
        
#         查看消防安全重点
        param = copy.deepcopy(ZuZhiChangSuoPara.XiaoFangAnQuan)
        param['name'] = testCase_05Param['enterprise.name']
        param['address'] = testCase_05Param['enterprise.address']
        ret = ZuZhiChangSuoIntf.checkXiaoFangAnQuanCompany(companyDict=param, OrgId=testCase_05Param['ownerOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')      
                
        downLoad = copy.deepcopy(ZuZhiChangSuoPara.dldataXiaoFangAnQuan)
        downLoad['orgId']=orgInit['DftWangGeOrgId']
        response = ZuZhiChangSuoIntf.dldataXiaoFangAnQuan(downLoad,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')         
        with open("C:/autotest_file/xiaofanganquan.xls", "wb") as code:
            code.write(response.content)
            
        ret = CommonUtil.checkExcelCellValue(testCase_05Param['enterprise.name'], 'xiaofanganquan.xls','消防安全重点', 'A4')          
        self.assertTrue(ret, '导出失败')        
        pass   
    
    def testCase_25(self):    
        """导出治安重点"""
#         新增治安重点
        testCase_06Param = copy.deepcopy(ZuZhiChangSuoPara.addZhiAnZhongDian) 
        testCase_06Param['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_06Param['enterprise.name'] = '测试场所名称%s' % CommonUtil.createRandomString()
        testCase_06Param['enterprise.keyType'] = 'securityKey'
        testCase_06Param['mode'] = 'add'
        testCase_06Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_06Param['placeTypeName'] = '治安重点'
        testCase_06Param['enterprise.address'] = '测试场所地址1'
        testCase_06Param['enterprise.legalPerson'] = '测试负责人'
        testCase_06Param['enterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='治安重点类别', displayName='城乡结合部')
        responseDict = ZuZhiChangSuoIntf.addZhiAnZhongDian(ZhiAnZhongDianDict=testCase_06Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')           
        
#         查看治安重点
        param = copy.deepcopy(ZuZhiChangSuoPara.ZhiAnZhongDian)
        param['name'] = testCase_06Param['enterprise.name']
        param['address'] = testCase_06Param['enterprise.address']
        ret = ZuZhiChangSuoIntf.checkZhiAnZhongDianCompany(companyDict=param, OrgId=testCase_06Param['ownerOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')     
                
        downLoad = copy.deepcopy(ZuZhiChangSuoPara.dldataZhiAnZhongDian)
        downLoad['orgId']=orgInit['DftWangGeOrgId']
        response = ZuZhiChangSuoIntf.dldataZhiAnZhongDian(downLoad,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')         
        with open("C:/autotest_file/zhianzhongdian.xls", "wb") as code:
            code.write(response.content)
            
        ret = CommonUtil.checkExcelCellValue(testCase_06Param['enterprise.name'], 'zhianzhongdian.xls','治安重点', 'A4')          
        self.assertTrue(ret, '导出失败')        
        pass   
    
    def testCase_26(self):    
        """导出学校"""
#         新增学校
        testCase_07Param = copy.deepcopy(ZuZhiChangSuoPara.addXueXiao) 
        testCase_07Param['orgId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_07Param['school.chineseName'] = '测试学校名称%s' % CommonUtil.createRandomString()
        testCase_07Param['school.kind.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='学校性质', displayName='公办')
        testCase_07Param['mode'] = 'add'
        testCase_07Param['school.hasCertificate'] = '请选择'
        testCase_07Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_07Param['placeTypeName'] = '学校'
        testCase_07Param['school.address'] = '测试学校地址1'
        testCase_07Param['school.president'] = '测试校长'
        testCase_07Param['school.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='学校类型', displayName='小学')
        responseDict = ZuZhiChangSuoIntf.addXueXiao(XueXiaoDict=testCase_07Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')  

#         查看学校
        param = copy.deepcopy(ZuZhiChangSuoPara.XueXiao)
        param['chineseName'] = testCase_07Param['school.chineseName']
        param['address'] = testCase_07Param['school.address']
        ret = ZuZhiChangSuoIntf.checkXueXiaoCompany(companyDict=param, OrgId=testCase_07Param['orgId'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')    
                
        downLoad = copy.deepcopy(ZuZhiChangSuoPara.dldataXueXiao)
        downLoad['orgId']=orgInit['DftWangGeOrgId']
        response = ZuZhiChangSuoIntf.dldataXueXiao(downLoad,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')         
        with open("C:/autotest_file/xuexiao.xls", "wb") as code:
            code.write(response.content)
            
        ret = CommonUtil.checkExcelCellValue(testCase_07Param['school.chineseName'], 'xuexiao.xls','学校', 'A4')          
        self.assertTrue(ret, '导出失败')        
        pass   
    
    def testCase_27(self):    
        """导出医院"""
#         新增医院
        testCase_08Param = copy.deepcopy(ZuZhiChangSuoPara.addYiYuan) 
        testCase_08Param['organizationId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_08Param['hospital.hospitalName'] = '测试医院名称%s' % CommonUtil.createRandomString()
        testCase_08Param['hospital.personLiableTelephone'] = '1234-12341234'
        testCase_08Param['mode'] = 'add'
        testCase_08Param['hospital.organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_08Param['hospital.personLiableMobileNumber'] = '13411111111'
        testCase_08Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_08Param['hospital.address'] = '测试医院地址1'
        testCase_08Param['hospital.personLiable'] = '测试综治负责人'
        responseDict = ZuZhiChangSuoIntf.addYiYuan(YiYuanDict=testCase_08Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')  
        
#         查看医院
        param = copy.deepcopy(ZuZhiChangSuoPara.YiYuan)
        param['hospitalName'] = testCase_08Param['hospital.hospitalName']
        param['address'] = testCase_08Param['hospital.address']
        ret = ZuZhiChangSuoIntf.checkYiYuanCompany(companyDict=param, OrgId=testCase_08Param['organizationId'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')    
                
        downLoad = copy.deepcopy(ZuZhiChangSuoPara.dldataYiYuan)
        downLoad['organizationId']=orgInit['DftWangGeOrgId']
        response = ZuZhiChangSuoIntf.dldataYiYuan(downLoad,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')         
        with open("C:/autotest_file/yiyuan.xls", "wb") as code:
            code.write(response.content)
            
        ret = CommonUtil.checkExcelCellValue(testCase_08Param['hospital.hospitalName'], 'yiyuan.xls','医院信息', 'A4')          
        self.assertTrue(ret, '导出失败')        
        pass       
    
    def testCase_28(self):    
        """导出危险化学品单位"""
#         新增危险化学品单位
        testCase_09Param = copy.deepcopy(ZuZhiChangSuoPara.addWeiXianHuaXuePing) 
        testCase_09Param['organizationId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_09Param['location.unitName'] = '测试单位名称%s' % CommonUtil.createRandomString()
        testCase_09Param['mode'] = 'add'
        testCase_09Param['location.organization.orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        responseDict = ZuZhiChangSuoIntf.addWeiXianHuaXuePing(WeiXianHuaXuePingDict=testCase_09Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')  

#         查看危险化学品单位
        param = copy.deepcopy(ZuZhiChangSuoPara.WeiXianHuaXuePing)
        param['unitName'] = testCase_09Param['location.unitName']
        ret = ZuZhiChangSuoIntf.checkWeiXianHuaXuePingCompany(companyDict=param, OrgId=testCase_09Param['organizationId'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败') 
                
        downLoad = copy.deepcopy(ZuZhiChangSuoPara.dldataWeiXianHuaXuePing)
        downLoad['organizationId']=orgInit['DftWangGeOrgId']
        response = ZuZhiChangSuoIntf.dldataWeiXianHuaXuePing(downLoad,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')         
        with open("C:/autotest_file/weixianhuaxueping.xls", "wb") as code:
            code.write(response.content)
            
        ret = CommonUtil.checkExcelCellValue( testCase_09Param['location.unitName'], 'weixianhuaxueping.xls','危险化学品单位表', 'A4')          
        self.assertTrue(ret, '导出失败')        
        pass        
    
    def testCase_29(self):    
        """导出上网服务单位"""
#         新增上网服务单位
        testCase_10Param = copy.deepcopy(ZuZhiChangSuoPara.addShangWanFuWu) 
        testCase_10Param['location.organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_10Param['location.placeName'] = '测试单位名称%s' % CommonUtil.createRandomString()
        testCase_10Param['mode'] = 'add'
        testCase_10Param['ajaxUrl'] = '/baseinfo/internetBarManage/hasDuplicateInternetBarLocation.action'
        testCase_10Param['location.organization.orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        responseDict = ZuZhiChangSuoIntf.addShangWanFuWu(ShangWanFuWuDict=testCase_10Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')          
        
#         查看上网服务单位
        param = copy.deepcopy(ZuZhiChangSuoPara.ShangWanFuWu)
        param['placeName'] = testCase_10Param['location.placeName']
        ret = ZuZhiChangSuoIntf.checkShangWanFuWuCompany(companyDict=param, OrgId=testCase_10Param['location.organization.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')      
                
        downLoad = copy.deepcopy(ZuZhiChangSuoPara.dldataShangWanFuWu)
        downLoad['organizationId']=orgInit['DftWangGeOrgId']
        response = ZuZhiChangSuoIntf.dldataShangWanFuWu(downLoad,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')         
        with open("C:/autotest_file/shangwangfuwu.xls", "wb") as code:
            code.write(response.content)
            
        ret = CommonUtil.checkExcelCellValue( testCase_10Param['location.placeName'], 'shangwangfuwu.xls','上网服务单位', 'A4')          
        self.assertTrue(ret, '导出失败')        
        pass                  
    
    def testCase_30(self):    
        """导出公共场所"""
#         新增公共场所
        testCase_11Param = copy.deepcopy(ZuZhiChangSuoPara.addShangWanFuWu) 
        testCase_11Param['location.organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_11Param['location.placeName'] = '测试公共场所名称%s' % CommonUtil.createRandomString()
        testCase_11Param['location.placeAddress'] = '测试场所地址'
        testCase_11Param['mode'] = 'add'
        testCase_11Param['ajaxUrl'] = '/baseinfo/publicPlaceManage/hasDuplicatePublicPlaceLocation.action'
        testCase_11Param['location.organization.orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        responseDict = ZuZhiChangSuoIntf.addGongGongChangSuo(GongGongChangSuoDict=testCase_11Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')        
        
#         查看公共场所
        param = copy.deepcopy(ZuZhiChangSuoPara.GongGongChangSuo)
        param['placeName'] = testCase_11Param['location.placeName']
        ret = ZuZhiChangSuoIntf.checkGongGongChangSuoCompany(companyDict=param, OrgId=testCase_11Param['location.organization.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')     
                
        downLoad = copy.deepcopy(ZuZhiChangSuoPara.dldataGongGongChangSuo)
        downLoad['organizationId']=orgInit['DftWangGeOrgId']
        response = ZuZhiChangSuoIntf.dldataGongGongChangSuo(downLoad,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')         
        with open("C:/autotest_file/gonggongchangsuo.xls", "wb") as code:
            code.write(response.content)
            
        ret = CommonUtil.checkExcelCellValue( testCase_11Param['location.placeName'] , 'gonggongchangsuo.xls','公共场所表', 'A4')          
        self.assertTrue(ret, '导出失败')        
        pass                   
    
    def testCase_31(self):    
        """导出公共复杂场所"""
#         新增公共复杂场所
        testCase_12Param = copy.deepcopy(ZuZhiChangSuoPara.addGongGongFuZaChangSuo) 
        testCase_12Param['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_12Param['commonComplexPlace.name'] = '测试公共复杂场所名称%s' % CommonUtil.createRandomString()
        testCase_12Param['commonComplexPlace.legalPerson'] = '测试负责人'
        testCase_12Param['mode'] = 'add'
        testCase_12Param['commonComplexPlace_orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        responseDict = ZuZhiChangSuoIntf.addGongGongFuZaChangSuo(GongGongFuZaChangSuoDict=testCase_12Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')             
        
#         查看公共复杂场所
        param = copy.deepcopy(ZuZhiChangSuoPara.GongGongFuZaChangSuo)
        param['name'] = testCase_12Param['commonComplexPlace.name']
        ret = ZuZhiChangSuoIntf.checkGongGongFuZaChangSuoCompany(companyDict=param, OrgId=testCase_12Param['ownerOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')        
                
        downLoad = copy.deepcopy(ZuZhiChangSuoPara.dldataGongGongFuZaChangSuo)
        downLoad['organizationId']=orgInit['DftWangGeOrgId']
        response = ZuZhiChangSuoIntf.dldataGongGongFuZaChangSuo(downLoad,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')         
        with open("C:/autotest_file/gonggongfuzachangsuo.xls", "wb") as code:
            code.write(response.content)
            
        ret = CommonUtil.checkExcelCellValue( testCase_12Param['commonComplexPlace.name'] , 'gonggongfuzachangsuo.xls','公共复杂场所', 'A4')          
        self.assertTrue(ret, '导出失败')        
        pass          
    
    def testCase_32(self):    
        """导出特种行业"""
#         新增特种行业
        testCase_13Param = copy.deepcopy(ZuZhiChangSuoPara.addGongGongFuZaChangSuo) 
        testCase_13Param['organizationId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_13Param['specialTrade.name'] = '测试特种行业名称%s' % CommonUtil.createRandomString()
        testCase_13Param['specialTrade.personLiable'] = '测试负责人'
        testCase_13Param['specialTrade.address'] = '测试企业地址'
        testCase_13Param['specialTrade.organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_13Param['specialTrade.personLiableTelephone'] = '0571-12345678'
        testCase_13Param['specialTrade.personLiableMobileNumber'] = '13411111111'
        testCase_13Param['specialTrade.type.id'] =  CommonIntf.getIdByDomainAndDisplayName(domainName='特种行业类型', displayName='旅馆')
        testCase_13Param['specialTrade.legalPerson'] = '测试法人代表'
        testCase_13Param['mode'] = 'add'
        testCase_13Param['specialTrade.organization.orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        responseDict = ZuZhiChangSuoIntf.addTeZhongHangYe(TeZhongHangYeDict=testCase_13Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')           
        
#         查看特种行业
        param = copy.deepcopy(ZuZhiChangSuoPara.TeZhongHangYe)
        param['name'] = testCase_13Param['specialTrade.name']
        ret = ZuZhiChangSuoIntf.checkTeZhongHangYeCompany(companyDict=param, OrgId=testCase_13Param['organizationId'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')      
                
        downLoad = copy.deepcopy(ZuZhiChangSuoPara.dldataTeZhongHangYe)
        downLoad['organizationId']=orgInit['DftWangGeOrgId']
        response = ZuZhiChangSuoIntf.dldataTeZhongHangYe(downLoad,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')         
        with open("C:/autotest_file/tezhonghangye.xls", "wb") as code:
            code.write(response.content)
            
        ret = CommonUtil.checkExcelCellValue(testCase_13Param['specialTrade.name'] , 'tezhonghangye.xls','特种行业', 'A3')          
        self.assertTrue(ret, '导出失败')        
        pass         
    
    def testCase_33(self):    
        """导出其他场所"""
#         新增其他场所
        testCase_14Param = copy.deepcopy(ZuZhiChangSuoPara.addQiTaChangSuo) 
        testCase_14Param['organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_14Param['otherLocale.name'] = '测试场所名称%s' % CommonUtil.createRandomString()
        testCase_14Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_14Param['otherLocale.type.id'] =  CommonIntf.getIdByDomainAndDisplayName(domainName='其他场所类型', displayName='个体诊所')
        testCase_14Param['mode'] = 'add'
        responseDict = ZuZhiChangSuoIntf.addQiTaChangSuo(QiTaChangSuoDict=testCase_14Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')             
         
#         查看其他场所
        param = copy.deepcopy(ZuZhiChangSuoPara.QiTaChangSuo)
        param['name'] = testCase_14Param['otherLocale.name']
        ret = ZuZhiChangSuoIntf.checkQiTaChangSuoCompany(companyDict=param, OrgId=testCase_14Param['organization.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')        
                
        downLoad = copy.deepcopy(ZuZhiChangSuoPara.dldataQiTaChangSuo)
        downLoad['orgId']=orgInit['DftWangGeOrgId']
        response = ZuZhiChangSuoIntf.dldataQiTaChangSuo(downLoad,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')         
        with open("C:/autotest_file/qitachangsuo.xls", "wb") as code:
            code.write(response.content)
            
        ret = CommonUtil.checkExcelCellValue(testCase_14Param['otherLocale.name'] , 'qitachangsuo.xls','其他场所', 'A4')          
        self.assertTrue(ret, '导出失败')        
        pass         
    
    def testCase_34(self):    
        """导出社会组织"""
#         新增社会组织
        testCase_15Param = copy.deepcopy(ZuZhiChangSuoPara.addSheHuiZuZhi) 
        testCase_15Param['organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_15Param['newSocietyOrganizations.name'] = '测试组织名称%s' % CommonUtil.createRandomString()
        testCase_15Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_15Param['newSocietyOrganizations.type.id'] =  CommonIntf.getIdByDomainAndDisplayName(domainName='社会组织类型', displayName='社会团体')
        testCase_15Param['placeTypeName'] = '社会组织'
        testCase_15Param['keyType'] = 'newSocietyOrganizations'
        testCase_15Param['mode'] = 'add'
        testCase_15Param['newSocietyOrganizations.subType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='社会组织类型分类', displayName='学术性团体')
        testCase_15Param['newSocietyOrganizations.legalPerson'] = '测试法定代表人'
        responseDict = ZuZhiChangSuoIntf.addSheHuiZuZhi(SheHuiZuZhiDict=testCase_15Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')              
        
#         查看社会组织
        param = copy.deepcopy(ZuZhiChangSuoPara.SheHuiZuZhi)
        param['name'] = testCase_15Param['newSocietyOrganizations.name']
        ret = ZuZhiChangSuoIntf.checkSheHuiZuZhiCompany(companyDict=param, OrgId=testCase_15Param['organization.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')       
                
        downLoad = copy.deepcopy(ZuZhiChangSuoPara.dldataSheHuiZuZhi)
        downLoad['organizationId']=orgInit['DftWangGeOrgId']
        response = ZuZhiChangSuoIntf.dldataSheHuiZuZhi(downLoad,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')         
        with open("C:/autotest_file/shehuizuzhi.xls", "wb") as code:
            code.write(response.content)
            
        ret = CommonUtil.checkExcelCellValue(testCase_15Param['newSocietyOrganizations.name'] , 'shehuizuzhi.xls','社会组织表', 'A4')          
        self.assertTrue(ret, '导出失败')        
        pass                
    
    def testCase_35(self):    
        """导出新经济组织"""
#         新增新经济组织
        testCase_16Param = copy.deepcopy(ZuZhiChangSuoPara.addXinJingJiZuZhi) 
        testCase_16Param['newEconomicOrganizationsDomain.organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_16Param['newEconomicOrganizationsDomain.name'] = '测试名称%s' % CommonUtil.createRandomString()
        testCase_16Param['newEconomicOrganizationsDomain.organization.orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_16Param['newEconomicOrganizationsDomain.style.id'] =  CommonIntf.getIdByDomainAndDisplayName(domainName='新经济组织类别', displayName='个体工商户')
        testCase_16Param['newEconomicOrganizationsDomain.residence'] = '测试住所'
        testCase_16Param['newEconomicOrganizationsDomain.licenseNumber'] = '测试营业执照号码%s'% CommonUtil.createRandomString()
        testCase_16Param['mode'] = 'add'
        testCase_16Param['newEconomicOrganizationsDomain.validityStartDate'] = '2015-12-08'
        testCase_16Param['newEconomicOrganizationsDomain.validityEndDate'] = '2015-12-09'
        testCase_16Param['newEconomicOrganizationsDomain.chief'] = '测试负责人'
        responseDict = ZuZhiChangSuoIntf.addXinJingJiZuZhi(XinJingJiZuZhiDict=testCase_16Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')           
        
#         查看新经济组织
        param = copy.deepcopy(ZuZhiChangSuoPara.XinJingJiZuZhi)
        param['name'] = testCase_16Param['newEconomicOrganizationsDomain.name']
        ret = ZuZhiChangSuoIntf.checkXinJingJiZuZhiCompany(companyDict=param, OrgId=testCase_16Param['newEconomicOrganizationsDomain.organization.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')      
                
        downLoad = copy.deepcopy(ZuZhiChangSuoPara.dldataXinJingJiZuZhi)
        downLoad['organizationId']=orgInit['DftWangGeOrgId']
        response = ZuZhiChangSuoIntf.dldataXinJingJiZuZhi(downLoad,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')         
        with open("C:/autotest_file/xinjingjizuzhi.xls", "wb") as code:
            code.write(response.content)
            
        ret = CommonUtil.checkExcelCellValue(testCase_16Param['newEconomicOrganizationsDomain.name']  , 'xinjingjizuzhi.xls','新经济组织信息', 'A4')          
        self.assertTrue(ret, '导出失败')        
        pass                    

    def testCase_36(self):    
        """导出规上企业"""
#         新增规上企业
        testCase_17Param = copy.deepcopy(ZuZhiChangSuoPara.addGuiShangQiYe) 
        testCase_17Param['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_17Param['enterprise.name'] = '测试企业名称%s' % CommonUtil.createRandomString()
        testCase_17Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_17Param['enterprise.keyType'] =  'enterpriseKey'
        testCase_17Param['enterprise.address'] = '测试企业地址%s'% CommonUtil.createRandomString()
        testCase_17Param['placeTypeName'] = '规上企业'
        testCase_17Param['mode'] = 'add'
        testCase_17Param['enterprise.legalPerson'] = '测试法人代表'
        responseDict = ZuZhiChangSuoIntf.addGuiShangQiYe(GuiShangQiYeDict=testCase_17Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败') 

#         查看规上企业
        param = copy.deepcopy(ZuZhiChangSuoPara.GuiShangQiYe)
        param['address'] = testCase_17Param['enterprise.address']
        param['name'] = testCase_17Param['enterprise.name']
        ret = ZuZhiChangSuoIntf.checkGuiShangQiYeCompany(companyDict=param, OrgId=testCase_17Param['ownerOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')  
                
        downLoad = copy.deepcopy(ZuZhiChangSuoPara.dldataGuiShangQiYe)
        downLoad['orgId']=orgInit['DftWangGeOrgId']
        response = ZuZhiChangSuoIntf.dldataGuiShangQiYe(downLoad,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')         
        with open("C:/autotest_file/guishangqiye.xls", "wb") as code:
            code.write(response.content)
            
        ret = CommonUtil.checkExcelCellValue(testCase_17Param['enterprise.name'] , 'guishangqiye.xls','规上企业', 'A4')          
        self.assertTrue(ret, '导出失败')        
        pass                  
    
    def testCase_37(self):    
        """导出规下企业"""
#         新增规下企业
        testCase_18Param = copy.deepcopy(ZuZhiChangSuoPara.addGuiXiaQiYe) 
        testCase_18Param['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_18Param['enterprise.name'] = '测试企业名称%s' % CommonUtil.createRandomString()
        testCase_18Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_18Param['enterprise.keyType'] =  'enterpriseDownKey'
        testCase_18Param['enterprise.address'] = '测试企业地址%s'% CommonUtil.createRandomString()
        testCase_18Param['placeTypeName'] = '规上企业'
        testCase_18Param['mode'] = 'add'
        testCase_18Param['enterprise.legalPerson'] = '测试法人代表'
        ZuZhiChangSuoIntf.addGuiXiaQiYe(GuiXiaQiYeDict=testCase_18Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')

#         查看规下企业
        param = copy.deepcopy(ZuZhiChangSuoPara.GuiXiaQiYe)
        param['address'] = testCase_18Param['enterprise.address']
        param['name'] = testCase_18Param['enterprise.name']
        ret = ZuZhiChangSuoIntf.checkGuiXiaQiYeCompany(companyDict=param, OrgId=testCase_18Param['ownerOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')   
                
        downLoad = copy.deepcopy(ZuZhiChangSuoPara.dldataGuiXiaQiYe)
        downLoad['orgId']=orgInit['DftWangGeOrgId']
        response = ZuZhiChangSuoIntf.dldataGuiXiaQiYe(downLoad,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')         
        with open("C:/autotest_file/guixiaqiye.xls", "wb") as code:
            code.write(response.content)
            
        ret = CommonUtil.checkExcelCellValue(testCase_18Param['enterprise.name'] , 'guixiaqiye.xls','规下企业', 'A4')          
        self.assertTrue(ret, '导出失败')        
        pass             
    
    def testCase_38(self):    
        """导出无证无照场所"""
#         新增无证无照场所
        testCase_19Param = copy.deepcopy(ZuZhiChangSuoPara.addWuZhengWuZhao) 
        testCase_19Param['orgId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_19Param['withoutPlace.proprietor'] = '测试经营者%s' % CommonUtil.createRandomString()
        testCase_19Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_19Param['withoutPlace.enteringORimport'] =  'entering'
        testCase_19Param['withoutPlace.mobileNumber'] = '123456'
        testCase_19Param['withoutPlace.operateAddress'] = '测试经营地址%s'% CommonUtil.createRandomString()
        testCase_19Param['lawtypes'] = CommonIntf.getIdByDomainAndDisplayName(domainName='违法类型', displayName='食品安全')
        testCase_19Param['withoutPlace.disposetype.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='处理情况', displayName='未处理')
        testCase_19Param['mode'] = 'add'
        testCase_19Param['withoutPlace.findDate'] = '2015-12-09'
        responseDict = ZuZhiChangSuoIntf.addWuZhengWuZhao(WuZhengWuZhaoDict=testCase_19Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')         
        
#         查看无证无照场所
        param = copy.deepcopy(ZuZhiChangSuoPara.WuZhengWuZhao)
        param['proprietor'] = testCase_19Param['withoutPlace.proprietor']
        ret = ZuZhiChangSuoIntf.checkWuZhengWuZhaoCompany(companyDict=param, OrgId=testCase_19Param['orgId'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')    
                
        downLoad = copy.deepcopy(ZuZhiChangSuoPara.dldataWuZhengWuZhao)
        downLoad['orgId']=orgInit['DftWangGeOrgId']
        downLoad['withoutPlaceVo.orgId']=orgInit['DftWangGeOrgId']
        response = ZuZhiChangSuoIntf.dldataWuZhengWuZhao(downLoad,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')         
        with open("C:/autotest_file/wuzhengwuzhao.xls", "wb") as code:
            code.write(response.content)
            
        ret = CommonUtil.checkExcelCellValue(testCase_19Param['withoutPlace.proprietor'] , 'wuzhengwuzhao.xls','无证无照场所', 'A4')          
        self.assertTrue(ret, '导出失败')        
        pass                  
    
    def testCase_39(self):    
        """新增/修改安全生产企业"""
#         新增服务人员        
        XiaQuGuanLiIntf.xiaQuGuanLiMemberDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        Premise_01Param = copy.deepcopy(ZuZhiChangSuoPara.FuWuChengYuanObject) 
        Premise_01Param['serviceTeamMemberBase.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        Premise_01Param['serviceTeamMemberBase.job'] = '测试职位3'
        Premise_01Param['serviceTeamMemberBase.name'] = '测试服务成员'
        Premise_01Param['isSubmit'] = 'true'
        Premise_01Param['serviceTeamMemberBase.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别(男、女)', displayName='男')
        Premise_01Param['serviceTeamMemberBase.mobile'] = '13011111111'
        responseDict = ZuZhiChangSuoIntf.addFuWuChengYuan(FuWuChengYuanDict=Premise_01Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
#            查看服务人员
        param = copy.deepcopy(ZuZhiChangSuoPara.ChaKanRenYuanObject)
        param['name'] = Premise_01Param['serviceTeamMemberBase.name'] 
        param['job'] = Premise_01Param['serviceTeamMemberBase.job'] 
        ret = ZuZhiChangSuoIntf.checkFuWuChengYuanCompany(companyDict=param, orgId=Premise_01Param['serviceTeamMemberBase.org.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')        
        
#         新增安全生产企业
        testCase_19Param = copy.deepcopy(ZuZhiChangSuoPara.addAnQuanShengChan) 
        testCase_19Param['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_19Param['safeProductionEnterprise.name'] = '测试名称%s' % CommonUtil.createRandomString()
        testCase_19Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_19Param['safeProductionEnterprise.legalPerson'] =  '1111111111111111'
        testCase_19Param['safeProductionEnterprise.mobileNumber'] = '13412341234'
        testCase_19Param['safeProductionEnterprise.address'] = '测试地址%s'% CommonUtil.createRandomString()
        testCase_19Param['safeProductionEnterprise.gridPerson'] = '%s-测试服务成员'%CommonIntf.getDbQueryResult(dbCommand = "select t.id from SERVICETEAMMEMBERBASE t where t.name='测试服务成员'")
        testCase_19Param['safeProductionEnterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='企业类型', displayName='规上企业')
        testCase_19Param['mode'] = 'add'
        responseDict = ZuZhiChangSuoIntf.addAnQuanShengchan(AnQuanShengChanDict=testCase_19Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')         
        
#         查看安全生产企业
        param = copy.deepcopy(ZuZhiChangSuoPara.AnQuanShengChan)
        param['name'] = testCase_19Param['safeProductionEnterprise.name']
        ret = ZuZhiChangSuoIntf.checkAnQuanShengChanCompany(companyDict=param, OrgId=testCase_19Param['ownerOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')    
        
#         修改安全生产企业
        testCase_190Param = copy.deepcopy(ZuZhiChangSuoPara.updateAnQuanShengChan) 
        testCase_190Param['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_190Param['safeProductionEnterprise.name'] = '测试名称1%s' % CommonUtil.createRandomString()
        testCase_190Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_190Param['safeProductionEnterprise.legalPerson'] =  '1111111111111111'
        testCase_190Param['safeProductionEnterprise.mobileNumber'] = '13412341234'
        testCase_190Param['safeProductionEnterprise.address'] = '测试地址%s'% CommonUtil.createRandomString()
        testCase_190Param['safeProductionEnterprise.gridPerson'] = '%s-测试服务成员'%CommonIntf.getDbQueryResult(dbCommand = "select t.id from SERVICETEAMMEMBERBASE t where t.name='测试服务成员'")
        testCase_190Param['safeProductionEnterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='企业类型', displayName='规上企业')
        testCase_190Param['safeProductionEnterprise.id'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from SAFEPRODUCTIONENTERPRISE t where t.name='%s'"%testCase_19Param['safeProductionEnterprise.name'] )
        testCase_190Param['mode'] = 'edit'
        responseDict = ZuZhiChangSuoIntf.updateAnQuanShengchan(AnQuanShengChanDict=testCase_190Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改失败')         
        
#         巡检模块中查看安全生产企业
        param = copy.deepcopy(ZuZhiChangSuoPara.AnQuanShengChan)
        param['name'] = testCase_190Param['safeProductionEnterprise.name']
        ret = ZuZhiChangSuoIntf.checkanQuanShengChanCompany(companyDict=param, OrgId=testCase_19Param['ownerOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')            
                
        pass       

    def testCase_40(self):    
        """导出安全生产企业"""
#         新增服务人员        
        XiaQuGuanLiIntf.xiaQuGuanLiMemberDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        Premise_01Param = copy.deepcopy(ZuZhiChangSuoPara.FuWuChengYuanObject) 
        Premise_01Param['serviceTeamMemberBase.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        Premise_01Param['serviceTeamMemberBase.job'] = '测试职位3'
        Premise_01Param['serviceTeamMemberBase.name'] = '测试服务成员'
        Premise_01Param['isSubmit'] = 'true'
        Premise_01Param['serviceTeamMemberBase.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别(男、女)', displayName='男')
        Premise_01Param['serviceTeamMemberBase.mobile'] = '13011111111'
        responseDict = ZuZhiChangSuoIntf.addFuWuChengYuan(FuWuChengYuanDict=Premise_01Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
#            查看服务人员
        param = copy.deepcopy(ZuZhiChangSuoPara.ChaKanRenYuanObject)
        param['name'] = Premise_01Param['serviceTeamMemberBase.name'] 
        param['job'] = Premise_01Param['serviceTeamMemberBase.job'] 
        ret = ZuZhiChangSuoIntf.checkFuWuChengYuanCompany(companyDict=param, orgId=Premise_01Param['serviceTeamMemberBase.org.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')        
        
#         新增安全生产企业
        testCase_19Param = copy.deepcopy(ZuZhiChangSuoPara.addAnQuanShengChan) 
        testCase_19Param['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        testCase_19Param['safeProductionEnterprise.name'] = '测试名称%s' % CommonUtil.createRandomString()
        testCase_19Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        testCase_19Param['safeProductionEnterprise.legalPerson'] =  '1111111111111111'
        testCase_19Param['safeProductionEnterprise.mobileNumber'] = '13412341234'
        testCase_19Param['safeProductionEnterprise.address'] = '测试地址%s'% CommonUtil.createRandomString()
        testCase_19Param['safeProductionEnterprise.gridPerson'] = '%s-测试服务成员'%CommonIntf.getDbQueryResult(dbCommand = "select t.id from SERVICETEAMMEMBERBASE t where t.name='测试服务成员'")
        testCase_19Param['safeProductionEnterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='企业类型', displayName='规上企业')
        testCase_19Param['mode'] = 'add'
        responseDict = ZuZhiChangSuoIntf.addAnQuanShengchan(AnQuanShengChanDict=testCase_19Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')         
        
#         查看安全生产企业
        param = copy.deepcopy(ZuZhiChangSuoPara.AnQuanShengChan)
        param['name'] = testCase_19Param['safeProductionEnterprise.name']
        ret = ZuZhiChangSuoIntf.checkAnQuanShengChanCompany(companyDict=param, OrgId=testCase_19Param['ownerOrg.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')    
           
                
#        导出安全生产企业       
        downLoad = copy.deepcopy(ZuZhiChangSuoPara.dldataAnQuanShengChan)
        downLoad['orgId']=orgInit['DftWangGeOrgId']
        response = ZuZhiChangSuoIntf.dldataAnQuanShengchan(downLoad,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')         
        with open("C:/autotest_file/anquanshengchan.xls", "wb") as code:
            code.write(response.content)
             
        ret = CommonUtil.checkExcelCellValue(testCase_19Param['safeProductionEnterprise.name'] , 'anquanshengchan.xls','安全生产企业', 'B4')          
        self.assertTrue(ret, '导出失败')        
        pass       
    
    def tearDown(self):
        pass    
    
    
if __name__ == "__main__":
    suite = unittest.TestSuite()
#     suite.addTest(ZuZhiChangSuo("testPremise_01"))
#     suite.addTest(ZuZhiChangSuo("testCase_01"))
#     suite.addTest(ZuZhiChangSuo("testCase_02"))
#     suite.addTest(ZuZhiChangSuo("testCase_03"))
#     suite.addTest(ZuZhiChangSuo("testCase_04"))
#     suite.addTest(ZuZhiChangSuo("testCase_05"))
#     suite.addTest(ZuZhiChangSuo("testCase_06"))
#     suite.addTest(ZuZhiChangSuo("testCase_07"))
#     suite.addTest(ZuZhiChangSuo("testCase_08"))    
#     suite.addTest(ZuZhiChangSuo("testCase_09"))      
#     suite.addTest(ZuZhiChangSuo("testCase_10"))     
#     suite.addTest(ZuZhiChangSuo("testCase_11"))    
#     suite.addTest(ZuZhiChangSuo("testCase_12"))      
#     suite.addTest(ZuZhiChangSuo("testCase_13"))         
#     suite.addTest(ZuZhiChangSuo("testCase_14"))             
#     suite.addTest(ZuZhiChangSuo("testCase_15"))       
#     suite.addTest(ZuZhiChangSuo("testCase_16"))             
#     suite.addTest(ZuZhiChangSuo("testCase_17"))           
#     suite.addTest(ZuZhiChangSuo("testCase_18"))            
#     suite.addTest(ZuZhiChangSuo("testCase_19"))            
#     suite.addTest(ZuZhiChangSuo("testCase_20"))  
#     suite.addTest(ZuZhiChangSuo("testCase_21"))  
#     suite.addTest(ZuZhiChangSuo("testCase_22"))  
#     suite.addTest(ZuZhiChangSuo("testCase_23"))  
#     suite.addTest(ZuZhiChangSuo("testCase_24"))    
#     suite.addTest(ZuZhiChangSuo("testCase_25"))        
#     suite.addTest(ZuZhiChangSuo("testCase_26"))        
#     suite.addTest(ZuZhiChangSuo("testCase_27"))  
#     suite.addTest(ZuZhiChangSuo("testCase_28"))  
#     suite.addTest(ZuZhiChangSuo("testCase_29"))  
#     suite.addTest(ZuZhiChangSuo("testCase_30"))  
#     suite.addTest(ZuZhiChangSuo("testCase_31"))  
#     suite.addTest(ZuZhiChangSuo("testCase_32"))      
#     suite.addTest(ZuZhiChangSuo("testCase_33"))   
#     suite.addTest(ZuZhiChangSuo("testCase_34"))       
#     suite.addTest(ZuZhiChangSuo("testCase_35"))   
#     suite.addTest(ZuZhiChangSuo("testCase_36"))   
#     suite.addTest(ZuZhiChangSuo("testCase_37"))   
#     suite.addTest(ZuZhiChangSuo("testCase_38"))   
#     suite.addTest(ZuZhiChangSuo("testCase_39"))  
#     suite.addTest(ZuZhiChangSuo("testCase_40"))  
    results = unittest.TextTestRunner().run(suite)
    pass