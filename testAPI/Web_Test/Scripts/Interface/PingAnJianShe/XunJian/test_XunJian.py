# -*- coding:UTF-8 -*-
'''
Created on 2016-3-21

@author: chenyan
'''
from __future__ import unicode_literals
import unittest
import copy,time
from COMMON import Log
from COMMON import Time
from COMMON import CommonUtil
from CONFIG.Define import LogLevel
from Interface.PingAnJianShe.Common import CommonIntf
from Interface.PingAnJianShe.SystemMgr import SystemMgrIntf
from CONFIG.InitDefaultPara import orgInit,userInit
from Interface.PingAnJianShe.XunJian import XunJianIntf,\
    XunJianPara
from Interface.PingAnJianShe.ShiJianChuLi import ShiJianChuLiPara
import json



class XunJian(unittest.TestCase):

    def setUp(self):
#         SystemMgrIntf.initEnv()
        XunJianIntf.deleteAllXunJian()
        pass

#企业信息

    def testEnterpriseAdd_01(self):
        """企业 新增"""
    #新增企业信息
        enterpriseParam = copy.deepcopy(XunJianPara.enterpriseObject) 
        enterpriseParam['mode'] = 'addInspection'
        enterpriseParam['ownerOrg.id'] = orgInit['DftWangGeOrgId']
        enterpriseParam['orgName'] = orgInit['DftWangGeOrg']
        enterpriseParam['safeProductionEnterprise.name'] = '企业名称%s'%CommonUtil.createRandomString()
        enterpriseParam['safeProductionEnterprise.address'] = '企业地址%s'%CommonUtil.createRandomString()
        enterpriseParam['safeProductionEnterprise.legalPerson'] = '法人代表%s'%CommonUtil.createRandomString()     
        enterpriseParam['safeProductionEnterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='企业类型', displayName='规上企业')
        enterpriseParam['safeProductionEnterprise.landlordName'] = '房东姓名%s'%CommonUtil.createRandomString()
        enterpriseParam['safeProductionEnterprise.landlordMobile'] = '11111111111'
        enterpriseParam['safeProductionEnterprise.safeProductiontype.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='安全生产企业类型', displayName='一般企业')
        enterpriseParam['safeProductionEnterprise.mobileNumber'] = '11111111112'
        enterpriseParam['safeProductionEnterprise.businessLicense'] = 'aaaaaa'
        enterpriseParam['safeProductionEnterprise.employeeAmount'] = '100'
        enterpriseParam['safeProductionEnterprise.isEmphasis'] = 'false'  #是否注销
        enterpriseParam['safeProductionEnterprise.gridPerson'] = '%s-%s'%( CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.username= '%s' " % userInit['DftWangGeUser1']),orgInit['DftWangGeOrg1'])  

#         #验证所属网格必填
#         enterpriseParam['orgName']  =''
#         responseDict = XunJianIntf.add_enterprise(enterpriseParam, username=userInit['DftWangGeUser'], password='11111111')
#         print responseDict.result
#         self.assertTrue(responseDict.result, '新增企业所属网格必填项为空仍能新增，验证失败') 
#         Log.LogOutput(LogLevel.DEBUG, "新增企业所属网格必填项不能为空")
#         enterpriseParam['orgName'] = orgInit['DftWangGeOrg']  
#         
            #验证企业名称必填
        enterpriseParam['safeProductionEnterprise.name']  =''
        responseDict = XunJianIntf.add_enterprise(enterpriseParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertFalse(responseDict.result, '新增企业企业名称必填项为空仍能新增，验证失败') 
        Log.LogOutput(LogLevel.DEBUG, "新增企业企业名称必填项不能为空")
        enterpriseParam['safeProductionEnterprise.name'] = '企业名称%s'%CommonUtil.createRandomString() 
#         
#         #验证企业地址必填
#         enterpriseParam['safeProductionEnterprise.address'] =''
#         responseDict = XunJianIntf.add_enterprise(enterpriseParam, username=userInit['DftWangGeUser'], password='11111111')
#         self.assertTrue(responseDict.result, '新增企业企业地址必填项为空仍能新增，验证失败') 
#         Log.LogOutput(LogLevel.DEBUG, "新增企业企业地址必填项不能为空")
#         enterpriseParam['safeProductionEnterprise.address'] = '企业地址%s'%CommonUtil.createRandomString()
#         
#         #验证法人代表必填
#         enterpriseParam['safeProductionEnterprise.legalPerson']  =''
#         responseDict = XunJianIntf.add_enterprise(enterpriseParam, username=userInit['DftWangGeUser'], password='11111111')
#         self.assertTrue(responseDict.result, '新增企业法人代表必填项为空仍能新增，验证失败') 
#         Log.LogOutput(LogLevel.DEBUG, "新增企业法人代表必填项不能为空")
#         enterpriseParam['safeProductionEnterprise.legalPerson'] = '法人代表%s'%CommonUtil.createRandomString()  
#     
#         #验证企业类型必填
#         enterpriseParam['safeProductionEnterprise.type.id'] =''
#         responseDict = XunJianIntf.add_enterprise(enterpriseParam, username=userInit['DftWangGeUser'], password='11111111')
#         self.assertTrue(responseDict.result, '新增企业企业类型必填项为空仍能新增，验证失败') 
#         Log.LogOutput(LogLevel.DEBUG, "新增企业企业类型必填项不能为空")
#         enterpriseParam['safeProductionEnterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='企业类型', displayName='规上企业') 
    
#         #验证手机号码必填
#         enterpriseParam['safeProductionEnterprise.mobileNumber'] =''
#         responseDict = XunJianIntf.add_enterprise(enterpriseParam, username=userInit['DftWangGeUser'], password='11111111')
#         self.assertFalse(responseDict.result, '新增企业手机号码必填项为空仍能新增，验证失败') 
#         Log.LogOutput(LogLevel.DEBUG, "新增企业手机号码必填项不能为空")
#         enterpriseParam['safeProductionEnterprise.mobileNumber'] = '11111111111' 
#  
#         #验证所属网格员必填
#         enterpriseParam['safeProductionEnterprise.gridPerson']  =''
#         responseDict = XunJianIntf.add_enterprise(enterpriseParam, username=userInit['DftWangGeUser'], password='11111111')
#         self.assertFalse(responseDict.result, '新增企业所属网格员必填项为空仍能新增，验证失败') 
#         Log.LogOutput(LogLevel.DEBUG, "新增企业所属网格员必填项不能为空")
#         enterpriseParam['safeProductionEnterprise.gridPerson'] = '%s-%s'%( CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.username= '%s' " % userInit['DftWangGeUser1']),orgInit['DftWangGeOrg1'])
             
        responseDict = XunJianIntf.add_enterprise(enterpriseParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增企业失败') 
        
    #检查新增的企业信息  
        checkParam = copy.deepcopy(XunJianPara.checkEnterpriseDict)
        checkParam['name'] = enterpriseParam['safeProductionEnterprise.name']    
        ret = XunJianIntf.check_enterprise(checkParam, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '未检查到企业信息') 
        pass
  
    def testInspectionRecordAdd_02(self):
        """企业>巡检记录 添加"""
    #新增出租房严重隐患项信息
        riskRemarkParam = copy.deepcopy(XunJianPara.riskRemarkObject) 
        riskRemarkParam['riskRemark.riskRemarkName'] = '严重隐患备注项%s'%CommonUtil.createRandomString()
        riskRemarkParam['riskRemark.level.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='隐患等级', displayName='严重')   # 不合格：2014  严重：2015  
        riskRemarkParam['riskRemark.isEnable'] = '1'  #启用-1  禁用-0
        riskRemarkParam['mode'] = 'add'
        riskRemarkParam['riskRemark.riskmarkerType'] = '0'     #企业-0  出租房-1
        riskRemarkParam['riskRemark.orgId.id'] = orgInit['DftJieDaoOrgId']
        riskRemarkParam['isSubmit'] = 'true'  
        responseDict = XunJianIntf.add_riskRemark(riskRemarkParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增隐患项失败') 
        
    #新增出租房不合格隐患项信息
        newRiskRemarkParam = copy.deepcopy(XunJianPara.riskRemarkObject) 
        newRiskRemarkParam['riskRemark.riskRemarkName'] = '不合格隐患备注项%s'%CommonUtil.createRandomString()
        newRiskRemarkParam['riskRemark.level.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='隐患等级', displayName='不合格')   # 不合格：2014  严重：2015  
        newRiskRemarkParam['riskRemark.isEnable'] = '1'  #启用-1  禁用-0
        newRiskRemarkParam['mode'] = 'add'
        newRiskRemarkParam['riskRemark.riskmarkerType'] = '0'     #企业-0  出租房-1
        newRiskRemarkParam['riskRemark.orgId.id'] = orgInit['DftJieDaoOrgId']
        newRiskRemarkParam['isSubmit'] = 'true'  
        responseDict = XunJianIntf.add_riskRemark(newRiskRemarkParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增隐患项失败') 
        
    #新增企业信息
        enterpriseParam = copy.deepcopy(XunJianPara.enterpriseObject) 
        enterpriseParam['mode'] = 'addInspection'
        enterpriseParam['ownerOrg.id'] = orgInit['DftWangGeOrgId']
        enterpriseParam['orgName'] = orgInit['DftWangGeOrg']
        enterpriseParam['safeProductionEnterprise.name'] = '企业名称%s'%CommonUtil.createRandomString()
        enterpriseParam['safeProductionEnterprise.address'] = '企业地址%s'%CommonUtil.createRandomString()
        enterpriseParam['safeProductionEnterprise.legalPerson'] = '法人代表%s'%CommonUtil.createRandomString()     
        enterpriseParam['safeProductionEnterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='企业类型', displayName='规上企业')
        enterpriseParam['safeProductionEnterprise.landlordName'] = '房东姓名%s'%CommonUtil.createRandomString()
        enterpriseParam['safeProductionEnterprise.landlordMobile'] = '11111111111'
        enterpriseParam['safeProductionEnterprise.safeProductiontype.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='安全生产企业类型', displayName='一般企业')
        enterpriseParam['safeProductionEnterprise.mobileNumber'] = '11111111112'
        enterpriseParam['safeProductionEnterprise.businessLicense'] = 'aaaaaa'
        enterpriseParam['safeProductionEnterprise.employeeAmount'] = '100'
        enterpriseParam['safeProductionEnterprise.isEmphasis'] = 'false'  #是否注销
        enterpriseParam['safeProductionEnterprise.gridPerson'] = '%s-%s'%( CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.username= '%s' " % userInit['DftWangGeUser']),orgInit['DftWangGeOrg'])
        responseDict = XunJianIntf.add_enterprise(enterpriseParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增企业失败') 
        
    #新增合格的巡检记录信息
        inspectionParam = copy.deepcopy(XunJianPara.inspectionObject) 
        inspectionParam['mode'] = 'addInspectionRecord'
        inspectionParam['inspection.orgId'] = enterpriseParam['ownerOrg.id'] 
        inspectionParam['safeProductionEnterprise.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from SafeProductionEnterprise t where t.name='%s' " % enterpriseParam['safeProductionEnterprise.name'])
        inspectionParam['safeProductionEnterprise.name'] = enterpriseParam['safeProductionEnterprise.name'] 
        inspectionParam['inspectionRecord.enterprise.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from SafeProductionEnterprise t where t.name='%s' " % enterpriseParam['safeProductionEnterprise.name'])
        inspectionParam['inspection.inspectTime'] = Time.getCurrentDate()
        inspectionParam['inspection.inspectAddress'] = enterpriseParam['safeProductionEnterprise.address']
        inspectionParam['inspection.inspectResult'] = '1' #合格：1 不合格：0  严重：2
        inspectionParam['inspection.limitTime'] = Time.getCurrentDate()
        inspectionParam['inspection.inspectUserId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.organizationid='%s' " % enterpriseParam['ownerOrg.id'] ) 
        inspectionParam['inspection.inspectName'] = userInit['DftWangGeUserXM']
        inspectionParam['inspection.remark'] = '描述%s'%CommonUtil.createRandomString()
        responseDict = XunJianIntf.add_InspectionRecord(inspectionParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '巡检记录添加失败') 

    #在巡检工作的巡检记录下检查新增合格的巡检记录信息      
        checkParam = copy.deepcopy(XunJianPara.checkEnterpriseDict)
        checkParam['name'] = enterpriseParam['safeProductionEnterprise.name']   
        ret = XunJianIntf.check_InspectionRecord(checkParam, orgId=orgInit['DftWangGeOrgId'],mode = 'inspectionRecord',username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '未检查到巡检信息') 
     
    #新增不合格的巡检记录信息   
        newInspectionParam = copy.deepcopy(XunJianPara.inspectionObject)         
        newInspectionParam['mode'] = 'addInspectionRecord'
        newInspectionParam['inspection.orgId'] = enterpriseParam['ownerOrg.id'] 
        newInspectionParam['safeProductionEnterprise.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from SafeProductionEnterprise t where t.name='%s' " % enterpriseParam['safeProductionEnterprise.name'])
        newInspectionParam['safeProductionEnterprise.name'] = enterpriseParam['safeProductionEnterprise.name'] 
        newInspectionParam['inspectionRecord.enterprise.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from SafeProductionEnterprise t where t.name='%s' " % enterpriseParam['safeProductionEnterprise.name'])
        newInspectionParam['inspection.inspectTime'] = Time.getCurrentDate()
        newInspectionParam['inspection.inspectAddress'] = enterpriseParam['safeProductionEnterprise.address']
        newInspectionParam['riskRemarkName'] = 'on' #?
        newInspectionParam['inspection.inspectResult'] = '0' #合格：1 不合格：0  严重：2
        newInspectionParam['inspection.limitTime'] = Time.getCurrentDate()
        newInspectionParam['inspection.inspectUserId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.organizationid='%s' " % enterpriseParam['ownerOrg.id'] ) 
        newInspectionParam['inspection.inspectName'] = userInit['DftWangGeUserXM']
        newInspectionParam['riskRemarkIds'] = '2' #?合格：空
        newInspectionParam['inspection.remark'] = '描述%s'%CommonUtil.createRandomString()
        responseDict = XunJianIntf.add_InspectionRecord(newInspectionParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '巡检记录添加失败') 

    #在巡检工作的待复查下检查新增不合格的巡检记录信息     
        checkParam = copy.deepcopy(XunJianPara.checkEnterpriseDict)
        checkParam['name'] = enterpriseParam['safeProductionEnterprise.name']    
        ret = XunJianIntf.check_InspectionRecord(checkParam, orgId=orgInit['DftWangGeOrgId'],mode = 'reviewRecord',username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '未检查到待复查的巡检记录信息') 

    #新增严重的巡检记录信息
        inspectionParam_3 = copy.deepcopy(XunJianPara.inspectionObject) 
        inspectionParam_3['mode'] = 'addInspectionRecord'
        inspectionParam_3['inspection.orgId'] = enterpriseParam['ownerOrg.id'] 
        inspectionParam_3['safeProductionEnterprise.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from SafeProductionEnterprise t where t.name='%s' " % enterpriseParam['safeProductionEnterprise.name'])
        inspectionParam_3['safeProductionEnterprise.name'] = enterpriseParam['safeProductionEnterprise.name'] 
        inspectionParam_3['inspectionRecord.enterprise.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from SafeProductionEnterprise t where t.name='%s' " % enterpriseParam['safeProductionEnterprise.name'])
        inspectionParam_3['inspection.inspectTime'] = Time.getCurrentDate()
        inspectionParam_3['inspection.inspectAddress'] = enterpriseParam['safeProductionEnterprise.address']
        inspectionParam_3['inspection.inspectResult'] = '2'  #合格：1 不合格：0  严重：2
        inspectionParam_3['inspection.limitTime'] = Time.getCurrentDate()
        inspectionParam_3['inspection.inspectUserId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.organizationid='%s' " % enterpriseParam['ownerOrg.id'] ) 
        inspectionParam_3['inspection.inspectName'] = userInit['DftWangGeUserXM']
        inspectionParam_3['inspection.remark'] = '描述%s'%CommonUtil.createRandomString()
        responseDict = XunJianIntf.add_InspectionRecord(inspectionParam_3, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '巡检记录添加失败') 

    #在受理中心检查新增严重的巡检记录信息     
        checkParam = copy.deepcopy(XunJianPara.checkEnterpriseDict)
        checkParam['name'] = inspectionParam_3['safeProductionEnterprise.name']  
        ret = XunJianIntf.check_InspectionRecord(checkParam, orgId=orgInit['DftWangGeOrgId'],mode = 'acceptCenterRecord',sourceType='1',username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '受理中心未检查到新增的严重企业巡检记录')

        pass

    def testQiYeImportAndDownLoad_03(self):  #导出匹配失败
        """企业信息 导入/导出"""
        importHuJiparam = copy.deepcopy(XunJianPara.data)
        importHuJiparam['dataType']='safeProductionEnterprise'
        importHuJiparam['templates']='SAFEPRODUCTIONENTERPRISE'
        files = {'upload': ('test.xls', open('C:/autotest_file/importQiYe.xls', 'rb'),'applicationnd.ms-excel')}
        ret = XunJianIntf.import_Data(importHuJiparam, files=files,username=userInit['DftWangGeUser'], password='11111111')         
         
        checkParam = copy.deepcopy(XunJianPara.checkEnterpriseDict)
        checkParam['name'] = '企业导入测试'   
        ret = XunJianIntf.check_enterprise(checkParam, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '未检查到企业信息') 
                                
                                
                                
                                
        #导出信息
        #新增企业信息
        enterpriseParam = copy.deepcopy(XunJianPara.enterpriseObject) 
        enterpriseParam['mode'] = 'addInspection'
        enterpriseParam['ownerOrg.id'] = orgInit['DftWangGeOrgId']
        enterpriseParam['orgName'] = orgInit['DftWangGeOrg']
        enterpriseParam['safeProductionEnterprise.name'] = '企业名称%s'%CommonUtil.createRandomString()
        enterpriseParam['safeProductionEnterprise.address'] = '企业地址%s'%CommonUtil.createRandomString()
        enterpriseParam['safeProductionEnterprise.legalPerson'] = '法人代表%s'%CommonUtil.createRandomString()     
        enterpriseParam['safeProductionEnterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='企业类型', displayName='规上企业')
        enterpriseParam['safeProductionEnterprise.landlordName'] = '房东姓名%s'%CommonUtil.createRandomString()
        enterpriseParam['safeProductionEnterprise.landlordMobile'] = '11111111111'
        enterpriseParam['safeProductionEnterprise.safeProductiontype.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='安全生产企业类型', displayName='一般企业')
        enterpriseParam['safeProductionEnterprise.mobileNumber'] = '11111111112'
        enterpriseParam['safeProductionEnterprise.businessLicense'] = 'aaaaaa'
        enterpriseParam['safeProductionEnterprise.employeeAmount'] = '100'
        enterpriseParam['safeProductionEnterprise.isEmphasis'] = 'false'  #是否注销
        enterpriseParam['safeProductionEnterprise.gridPerson'] = '%s-%s'%( CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.username= '%s' " % userInit['DftWangGeUser']),orgInit['DftWangGeOrg'])
        responseDict = XunJianIntf.add_enterprise(enterpriseParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增企业失败')                         
                                
        downLoadHuJiparam = copy.deepcopy(XunJianPara.dlData)
        downLoadHuJiparam['orgId']=orgInit['DftWangGeOrgId']
        downLoadHuJiparam['pageOnly']='true'   #导出全部数据:false 导出本页数据:true
        response = XunJianIntf.downLoad_QiYe(downLoadHuJiparam, username=userInit['DftWangGeUser'], password='11111111')  
        with open("C:/autotest_file/downLoadQiYe.xls", "wb") as code:
            code.write(response.content)

    #匹配失败 
        ret = CommonUtil.checkExcelCellValue(enterpriseParam['safeProductionEnterprise.name'], 'downLoadQiYe.xls','安全生产企业', 'B4')   
        self.assertTrue(ret, '导出匹配失败')
        pass

    def testEnterpriseDispatch_04(self):
        """划分企业"""
    #新增企业信息
        enterpriseParam = copy.deepcopy(XunJianPara.enterpriseObject) 
        enterpriseParam['mode'] = 'addInspection'
        enterpriseParam['ownerOrg.id'] = orgInit['DftWangGeOrgId']
        enterpriseParam['orgName'] = orgInit['DftWangGeOrg']
        enterpriseParam['safeProductionEnterprise.name'] = '企业名称%s'%CommonUtil.createRandomString()
        enterpriseParam['safeProductionEnterprise.address'] = '企业地址%s'%CommonUtil.createRandomString()
        enterpriseParam['safeProductionEnterprise.legalPerson'] = '法人代表%s'%CommonUtil.createRandomString()     
        enterpriseParam['safeProductionEnterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='企业类型', displayName='规上企业')
        enterpriseParam['safeProductionEnterprise.landlordName'] = '房东姓名%s'%CommonUtil.createRandomString()
        enterpriseParam['safeProductionEnterprise.landlordMobile'] = '11111111111'
        enterpriseParam['safeProductionEnterprise.safeProductiontype.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='安全生产企业类型', displayName='一般企业')
        enterpriseParam['safeProductionEnterprise.mobileNumber'] = '11111111112'
        enterpriseParam['safeProductionEnterprise.businessLicense'] = 'aaaaaa'
        enterpriseParam['safeProductionEnterprise.employeeAmount'] = '100'
        enterpriseParam['safeProductionEnterprise.isEmphasis'] = 'false'  #是否注销
        enterpriseParam['safeProductionEnterprise.gridPerson'] = '%s-%s'%( CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.username= '%s' " % userInit['DftWangGeUser']),orgInit['DftWangGeOrg'])
        responseDict = XunJianIntf.add_enterprise(enterpriseParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增企业失败') 

    #对企业划分 
        dispatchParam = copy.deepcopy(XunJianPara.dispatchDict)
        dispatchParam['selectIds'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from safeproductionenterprise t where t.name='%s'" % enterpriseParam['safeProductionEnterprise.name'])
        dispatchParam['userId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.organizationid='%s' " % orgInit['DftWangGeOrgId1'] )
        ret = XunJianIntf.dispatchEnterpriseDivision(dispatchParam, username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '划分企业信息失败')         

    #检查企业记录中划分后所属负责人信息
        checkParam = copy.deepcopy(XunJianPara.checkEnterpriseDict)
        checkParam['name'] = enterpriseParam['safeProductionEnterprise.name']    
        checkParam['gridPerson'] = userInit['DftWangGeUserXM1']
        ret = XunJianIntf.check_enterprise(checkParam, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '未检查到企业信息') 
        
        pass

    def testEnterpriseSearch_05(self):
        """企业>巡检记录 搜索"""
    #新增企业信息1
        enterpriseParam = copy.deepcopy(XunJianPara.enterpriseObject) 
        enterpriseParam['mode'] = 'addInspection'
        enterpriseParam['ownerOrg.id'] = orgInit['DftWangGeOrgId']
        enterpriseParam['orgName'] = orgInit['DftWangGeOrg']
        enterpriseParam['safeProductionEnterprise.name'] = '企业名称%s'%CommonUtil.createRandomString()
        enterpriseParam['safeProductionEnterprise.address'] = '企业地址%s'%CommonUtil.createRandomString()
        enterpriseParam['safeProductionEnterprise.legalPerson'] = '法人代表%s'%CommonUtil.createRandomString()     
        enterpriseParam['safeProductionEnterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='企业类型', displayName='规上企业')
        enterpriseParam['safeProductionEnterprise.landlordName'] = '房东姓名%s'%CommonUtil.createRandomString()
        enterpriseParam['safeProductionEnterprise.landlordMobile'] = '11111111111'
        enterpriseParam['safeProductionEnterprise.safeProductiontype.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='安全生产企业类型', displayName='一般企业')
        enterpriseParam['safeProductionEnterprise.mobileNumber'] = '11111111112'
        enterpriseParam['safeProductionEnterprise.businessLicense'] = 'aaaaaa'
        enterpriseParam['safeProductionEnterprise.employeeAmount'] = '100'
        enterpriseParam['safeProductionEnterprise.isEmphasis'] = 'false'  #是否注销
        enterpriseParam['safeProductionEnterprise.gridPerson'] = '%s-%s'%( CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.username= '%s' " % userInit['DftWangGeUser']),orgInit['DftWangGeOrg'])
        responseDict = XunJianIntf.add_enterprise(enterpriseParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增企业失败') 
        
    #新增企业信息2
        newEnterpriseParam = copy.deepcopy(XunJianPara.enterpriseObject) 
        newEnterpriseParam['mode'] = 'addInspection'
        newEnterpriseParam['ownerOrg.id'] = orgInit['DftWangGeOrgId']
        newEnterpriseParam['orgName'] = orgInit['DftWangGeOrg']
        newEnterpriseParam['safeProductionEnterprise.name'] = '企业名称2%s'%CommonUtil.createRandomString()
        newEnterpriseParam['safeProductionEnterprise.address'] = '企业地址%s'%CommonUtil.createRandomString()
        newEnterpriseParam['safeProductionEnterprise.legalPerson'] = '法人代表%s'%CommonUtil.createRandomString()     
        newEnterpriseParam['safeProductionEnterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='企业类型', displayName='规下企业')
        newEnterpriseParam['safeProductionEnterprise.landlordName'] = '房东姓名%s'%CommonUtil.createRandomString()
        newEnterpriseParam['safeProductionEnterprise.landlordMobile'] = '11111111111'
        newEnterpriseParam['safeProductionEnterprise.safeProductiontype.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='安全生产企业类型', displayName='劳动密集型企业')
        newEnterpriseParam['safeProductionEnterprise.mobileNumber'] = '11111111111'
        newEnterpriseParam['safeProductionEnterprise.businessLicense'] = 'aaaaaa'
        newEnterpriseParam['safeProductionEnterprise.employeeAmount'] = '100'
        newEnterpriseParam['safeProductionEnterprise.isEmphasis'] = 'false'  #是否注销
        newEnterpriseParam['safeProductionEnterprise.gridPerson'] = '%s-%s'%( CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.username= '%s' " % userInit['DftWangGeUser']),orgInit['DftWangGeOrg'])  
        responseDict = XunJianIntf.add_enterprise(newEnterpriseParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增企业失败') 

    #搜索企业信息1   
        searchParam = copy.deepcopy(XunJianPara.checkEnterpriseDict)
        searchParam['name'] = enterpriseParam['safeProductionEnterprise.name']    
        ret = XunJianIntf.search_enterprise(searchParam, orgId=orgInit['DftWangGeOrgId'],fastSearchKeyWords=enterpriseParam['safeProductionEnterprise.name'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '未搜索到企业信息') 
    
    #高级搜索企业信息2    
        advancedSearch_Param = copy.deepcopy(XunJianPara.checkEnterpriseDict)
        advancedSearch_Param['name'] = newEnterpriseParam['safeProductionEnterprise.name']    
        ret = XunJianIntf.advancedSearch_enterprise(advancedSearch_Param, orgId=orgInit['DftWangGeOrgId'],name=newEnterpriseParam['safeProductionEnterprise.name'],isEmphasis='false',username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '未搜索到企业信息') 
        pass

    def testEnterpriseEdit_06(self):
        """企业信息 修改"""
    #新增企业信息
        enterpriseParam = copy.deepcopy(XunJianPara.enterpriseObject) 
        enterpriseParam['mode'] = 'edit'
        enterpriseParam['ownerOrg.id'] = orgInit['DftWangGeOrgId']
        enterpriseParam['orgName'] = orgInit['DftWangGeOrg']
        enterpriseParam['safeProductionEnterprise.name'] = '企业名称%s'%CommonUtil.createRandomString()
        enterpriseParam['safeProductionEnterprise.address'] = '企业地址%s'%CommonUtil.createRandomString()
        enterpriseParam['safeProductionEnterprise.legalPerson'] = '法人代表%s'%CommonUtil.createRandomString()     
        enterpriseParam['safeProductionEnterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='企业类型', displayName='规上企业')
        enterpriseParam['safeProductionEnterprise.landlordName'] = '房东姓名%s'%CommonUtil.createRandomString()
        enterpriseParam['safeProductionEnterprise.landlordMobile'] = '11111111111'
        enterpriseParam['safeProductionEnterprise.safeProductiontype.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='安全生产企业类型', displayName='一般企业')
        enterpriseParam['safeProductionEnterprise.mobileNumber'] = '11111111112'
        enterpriseParam['safeProductionEnterprise.businessLicense'] = 'aaaaaa'
        enterpriseParam['safeProductionEnterprise.employeeAmount'] = '100'
        enterpriseParam['safeProductionEnterprise.isEmphasis'] = 'false'  #是否注销
        enterpriseParam['safeProductionEnterprise.gridPerson'] = '%s-%s'%( CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.username= '%s' " % userInit['DftWangGeUser']),orgInit['DftWangGeOrg'])
        responseDict = XunJianIntf.add_enterprise(enterpriseParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增企业失败') 
        
    #修改企业信息
        editParam = copy.deepcopy(XunJianPara.enterpriseObject) 
        editParam['mode'] = 'addInspection'
        editParam['ownerOrg.id'] = orgInit['DftWangGeOrgId']
        editParam['orgName'] = orgInit['DftWangGeOrg']
        editParam['safeProductionEnterprise.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from safeproductionenterprise t where t.name='%s'" % enterpriseParam['safeProductionEnterprise.name'])
        editParam['safeProductionEnterprise.name'] = '修改企业名称%s'%CommonUtil.createRandomString()
        editParam['safeProductionEnterprise.address'] = '修改企业地址%s'%CommonUtil.createRandomString()
        editParam['safeProductionEnterprise.legalPerson'] = enterpriseParam['safeProductionEnterprise.legalPerson']     
        editParam['safeProductionEnterprise.type.id'] = enterpriseParam['safeProductionEnterprise.type.id']
        editParam['safeProductionEnterprise.landlordName'] = enterpriseParam['safeProductionEnterprise.landlordName']
        editParam['safeProductionEnterprise.landlordMobile'] = enterpriseParam['safeProductionEnterprise.landlordMobile']        
        editParam['safeProductionEnterprise.safeProductiontype.id'] = enterpriseParam['safeProductionEnterprise.safeProductiontype.id']
        editParam['safeProductionEnterprise.mobileNumber'] = enterpriseParam['safeProductionEnterprise.mobileNumber']
        editParam['safeProductionEnterprise.businessLicense'] = enterpriseParam['safeProductionEnterprise.businessLicense']
        editParam['safeProductionEnterprise.employeeAmount'] = enterpriseParam['safeProductionEnterprise.employeeAmount']
        editParam['safeProductionEnterprise.isEmphasis'] = enterpriseParam['safeProductionEnterprise.isEmphasis']
        editParam['safeProductionEnterprise.gridPerson'] = enterpriseParam['safeProductionEnterprise.gridPerson']  
        responseDict = XunJianIntf.edit_enterprise(editParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改企业失败') 
        
    #检查修改后的企业信息  
        checkParam = copy.deepcopy(XunJianPara.checkEnterpriseDict)
        checkParam['name'] = editParam['safeProductionEnterprise.name']    
        ret = XunJianIntf.check_enterprise(checkParam, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '未检查到企业信息') 
        pass

    def testEnterpriseDelete_07(self):
        """企业信息 删除"""
    #新增企业信息1
        enterpriseParam = copy.deepcopy(XunJianPara.enterpriseObject) 
        enterpriseParam['mode'] = 'addInspection'
        enterpriseParam['ownerOrg.id'] = orgInit['DftWangGeOrgId']
        enterpriseParam['orgName'] = orgInit['DftWangGeOrg']
        enterpriseParam['safeProductionEnterprise.name'] = '企业名称%s'%CommonUtil.createRandomString()
        enterpriseParam['safeProductionEnterprise.address'] = '企业地址%s'%CommonUtil.createRandomString()
        enterpriseParam['safeProductionEnterprise.legalPerson'] = '法人代表%s'%CommonUtil.createRandomString()     
        enterpriseParam['safeProductionEnterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='企业类型', displayName='规上企业')
        enterpriseParam['safeProductionEnterprise.landlordName'] = '房东姓名%s'%CommonUtil.createRandomString()
        enterpriseParam['safeProductionEnterprise.landlordMobile'] = '11111111111'
        enterpriseParam['safeProductionEnterprise.safeProductiontype.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='安全生产企业类型', displayName='一般企业')
        enterpriseParam['safeProductionEnterprise.mobileNumber'] = '11111111112'
        enterpriseParam['safeProductionEnterprise.businessLicense'] = 'aaaaaa'
        enterpriseParam['safeProductionEnterprise.employeeAmount'] = '100'
        enterpriseParam['safeProductionEnterprise.isEmphasis'] = 'false'  #是否注销
        enterpriseParam['safeProductionEnterprise.gridPerson'] = '%s-%s'%( CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.username= '%s' " % userInit['DftWangGeUser']),orgInit['DftWangGeOrg'])
        responseDict = XunJianIntf.add_enterprise(enterpriseParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增企业失败') 
        
    #新增企业信息2
        newEnterpriseParam = copy.deepcopy(XunJianPara.enterpriseObject) 
        newEnterpriseParam['mode'] = 'addInspection'
        newEnterpriseParam['ownerOrg.id'] = orgInit['DftWangGeOrgId']
        newEnterpriseParam['orgName'] = orgInit['DftWangGeOrg']
        newEnterpriseParam['safeProductionEnterprise.name'] = '企业名称2%s'%CommonUtil.createRandomString()
        newEnterpriseParam['safeProductionEnterprise.address'] = '企业地址%s'%CommonUtil.createRandomString()
        newEnterpriseParam['safeProductionEnterprise.legalPerson'] = '法人代表%s'%CommonUtil.createRandomString()     
        newEnterpriseParam['safeProductionEnterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='企业类型', displayName='规下企业')
        newEnterpriseParam['safeProductionEnterprise.landlordName'] = '房东姓名%s'%CommonUtil.createRandomString()
        newEnterpriseParam['safeProductionEnterprise.landlordMobile'] = '11111111111'
        newEnterpriseParam['safeProductionEnterprise.safeProductiontype.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='安全生产企业类型', displayName='劳动密集型企业')
        newEnterpriseParam['safeProductionEnterprise.mobileNumber'] = '11111111111'
        newEnterpriseParam['safeProductionEnterprise.businessLicense'] = 'aaaaaa'
        newEnterpriseParam['safeProductionEnterprise.employeeAmount'] = '100'
        newEnterpriseParam['safeProductionEnterprise.isEmphasis'] = 'false'  #是否注销
        newEnterpriseParam['safeProductionEnterprise.gridPerson'] = '%s-%s'%( CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.username= '%s' " % userInit['DftWangGeUser']),orgInit['DftWangGeOrg'])  
        responseDict = XunJianIntf.add_enterprise(newEnterpriseParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增企业失败') 

    #删除企业信息  
        deleteParam = copy.deepcopy(XunJianPara.dispatchDict)
        deleteParam['selectIds'] = '%s,%s'%(CommonIntf.getDbQueryResult(dbCommand = "select t.id from safeproductionenterprise t where t.name='%s'" % enterpriseParam['safeProductionEnterprise.name']),CommonIntf.getDbQueryResult(dbCommand = "select t.id from safeproductionenterprise t where t.name='%s'" % newEnterpriseParam['safeProductionEnterprise.name'])) 
        ret = XunJianIntf.delete_enterprise(deleteParam, username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '未搜索到企业信息') 
        
    #检查删除后的企业信息 不存在
        checkParam = copy.deepcopy(XunJianPara.checkEnterpriseDict)
        checkParam['name'] = enterpriseParam['safeProductionEnterprise.name']    
        ret = XunJianIntf.check_enterprise(checkParam, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '被删除的企业信息1在列表中依然存在，删除失败') 
        
        checkParam['name'] = newEnterpriseParam['safeProductionEnterprise.name']    
        ret = XunJianIntf.check_enterprise(checkParam, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '被删除的企业信息2在列表中依然存在，删除失败') 
        
        pass


#巡检工作


    def testInspectionRecordSearch_08(self):
        """企业>巡检记录 搜索"""
    #新增企业信息1
        enterpriseParam = copy.deepcopy(XunJianPara.enterpriseObject) 
        enterpriseParam['mode'] = 'addInspection'
        enterpriseParam['ownerOrg.id'] = orgInit['DftWangGeOrgId']
        enterpriseParam['orgName'] = orgInit['DftWangGeOrg']
        enterpriseParam['safeProductionEnterprise.name'] = '1企业名称%s'%CommonUtil.createRandomString()
        enterpriseParam['safeProductionEnterprise.address'] = '企业地址%s'%CommonUtil.createRandomString()
        enterpriseParam['safeProductionEnterprise.legalPerson'] = '法人代表%s'%CommonUtil.createRandomString()     
        enterpriseParam['safeProductionEnterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='企业类型', displayName='规上企业')
        enterpriseParam['safeProductionEnterprise.landlordName'] = '房东姓名%s'%CommonUtil.createRandomString()
        enterpriseParam['safeProductionEnterprise.landlordMobile'] = '11111111111'
        enterpriseParam['safeProductionEnterprise.safeProductiontype.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='安全生产企业类型', displayName='一般企业')
        enterpriseParam['safeProductionEnterprise.mobileNumber'] = '11111111112'
        enterpriseParam['safeProductionEnterprise.businessLicense'] = 'aaaaaa'
        enterpriseParam['safeProductionEnterprise.employeeAmount'] = '100'
        enterpriseParam['safeProductionEnterprise.isEmphasis'] = 'false'  #是否注销
        enterpriseParam['safeProductionEnterprise.gridPerson'] = '%s-%s'%( CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.username= '%s' " % userInit['DftWangGeUser']),orgInit['DftWangGeOrg'])
        responseDict = XunJianIntf.add_enterprise(enterpriseParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增企业失败') 
        
    #新增合格的巡检记录信息1
        inspectionParam = copy.deepcopy(XunJianPara.inspectionObject) 
        inspectionParam['mode'] = 'addInspectionRecord'
        inspectionParam['inspection.orgId'] = enterpriseParam['ownerOrg.id'] 
        inspectionParam['safeProductionEnterprise.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from SafeProductionEnterprise t where t.name='%s' " % enterpriseParam['safeProductionEnterprise.name'])
        inspectionParam['safeProductionEnterprise.name'] = enterpriseParam['safeProductionEnterprise.name'] 
        inspectionParam['inspectionRecord.enterprise.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from SafeProductionEnterprise t where t.name='%s' " % enterpriseParam['safeProductionEnterprise.name'])
        inspectionParam['inspection.inspectTime'] = Time.getCurrentDate()
        inspectionParam['inspection.inspectAddress'] = enterpriseParam['safeProductionEnterprise.address']
        inspectionParam['inspection.inspectResult'] = '1'  #合格：1 不合格：0  严重：2
        inspectionParam['inspection.limitTime'] = Time.getCurrentDate()
        inspectionParam['inspection.inspectUserId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.organizationid='%s' " % enterpriseParam['ownerOrg.id'] ) 
        inspectionParam['inspection.inspectName'] = userInit['DftWangGeUserXM']
        inspectionParam['inspection.remark'] = '描述1%s'%CommonUtil.createRandomString()
        responseDict = XunJianIntf.add_InspectionRecord(inspectionParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '巡检记录添加失败') 
        
    #新增企业信息2
        newEnterpriseParam = copy.deepcopy(XunJianPara.enterpriseObject) 
        newEnterpriseParam['mode'] = 'addInspection'
        newEnterpriseParam['ownerOrg.id'] = orgInit['DftWangGeOrgId']
        newEnterpriseParam['orgName'] = orgInit['DftWangGeOrg']
        newEnterpriseParam['safeProductionEnterprise.name'] = '2企业名称%s'%CommonUtil.createRandomString()
        newEnterpriseParam['safeProductionEnterprise.address'] = '企业地址%s'%CommonUtil.createRandomString()
        newEnterpriseParam['safeProductionEnterprise.legalPerson'] = '法人代表%s'%CommonUtil.createRandomString()     
        newEnterpriseParam['safeProductionEnterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='企业类型', displayName='规上企业')
        newEnterpriseParam['safeProductionEnterprise.landlordName'] = '房东姓名%s'%CommonUtil.createRandomString()
        newEnterpriseParam['safeProductionEnterprise.landlordMobile'] = '11111111111'
        newEnterpriseParam['safeProductionEnterprise.safeProductiontype.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='安全生产企业类型', displayName='一般企业')
        newEnterpriseParam['safeProductionEnterprise.mobileNumber'] = '11111111112'
        newEnterpriseParam['safeProductionEnterprise.businessLicense'] = 'aaaaaa'
        newEnterpriseParam['safeProductionEnterprise.employeeAmount'] = '100'
        newEnterpriseParam['safeProductionEnterprise.isEmphasis'] = 'false'  #是否注销
        newEnterpriseParam['safeProductionEnterprise.gridPerson'] = '%s-%s'%( CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.username= '%s' " % userInit['DftWangGeUser']),orgInit['DftWangGeOrg'])
        responseDict = XunJianIntf.add_enterprise(newEnterpriseParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增企业失败') 
     
    #新增合格的巡检记录信息   2
        newInspectionParam = copy.deepcopy(XunJianPara.inspectionObject)         
        newInspectionParam['mode'] = 'addInspectionRecord'
        newInspectionParam['inspection.orgId'] = newEnterpriseParam['ownerOrg.id'] 
        newInspectionParam['safeProductionEnterprise.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from SafeProductionEnterprise t where t.name='%s' " % newEnterpriseParam['safeProductionEnterprise.name'])
        newInspectionParam['safeProductionEnterprise.name'] = newEnterpriseParam['safeProductionEnterprise.name'] 
        newInspectionParam['inspectionRecord.enterprise.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from SafeProductionEnterprise t where t.name='%s' " % newEnterpriseParam['safeProductionEnterprise.name'])
        newInspectionParam['inspection.inspectTime'] = Time.getCurrentDate()
        newInspectionParam['inspection.inspectAddress'] = newEnterpriseParam['safeProductionEnterprise.address']
        newInspectionParam['inspection.inspectResult'] = '1'  #合格：1 不合格：0  严重：2
        newInspectionParam['inspection.limitTime'] = Time.getCurrentDate()
        newInspectionParam['inspection.inspectUserId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.organizationid='%s' " % newEnterpriseParam['ownerOrg.id'] ) 
        newInspectionParam['inspection.inspectName'] = userInit['DftWangGeUserXM']
        newInspectionParam['inspection.remark'] = '描述2%s'%CommonUtil.createRandomString()
        responseDict = XunJianIntf.add_InspectionRecord(newInspectionParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '巡检记录添加失败') 

    #搜索巡检记录信息1   
        searchParam = copy.deepcopy(XunJianPara.checkEnterpriseDict)
        searchParam['name'] = enterpriseParam['safeProductionEnterprise.name']    
        ret = XunJianIntf.check_InspectionRecord(searchParam, orgId=orgInit['DftWangGeOrgId'],mode = 'inspectionRecord',name = enterpriseParam['safeProductionEnterprise.name'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '未搜索到巡检信息') 
    
    #高级搜索巡检记录信息2    
        advancedSearch_Param = copy.deepcopy(XunJianPara.checkEnterpriseDict)
        advancedSearch_Param['name'] = newInspectionParam['safeProductionEnterprise.name']    
        ret = XunJianIntf.check_InspectionRecord(searchParam, orgId=orgInit['DftWangGeOrgId'],mode = 'inspectionRecord',name = enterpriseParam['safeProductionEnterprise.name'],state='1',username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '未搜索到巡检信息') 

    #搜索不符合条件的巡检记录信息    
        advancedSearch_Param = copy.deepcopy(XunJianPara.checkEnterpriseDict)
        advancedSearch_Param['name'] = '巡检记录'
        ret = XunJianIntf.check_InspectionRecord(searchParam, orgId=orgInit['DftWangGeOrgId'],mode = 'inspectionRecord',name = '巡检记录',state='1',username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '搜索到不符合条件的巡检记录信息，搜素失败')         
        pass
        
    def testXunJianDownLoad_09(self):
        """巡检记录信息 导出"""
    #新增企业信息
        enterpriseParam = copy.deepcopy(XunJianPara.enterpriseObject) 
        enterpriseParam['mode'] = 'addInspection'
        enterpriseParam['ownerOrg.id'] = orgInit['DftWangGeOrgId']
        enterpriseParam['orgName'] = orgInit['DftWangGeOrg']
        enterpriseParam['safeProductionEnterprise.name'] = '导出企业名称%s'%CommonUtil.createRandomString()
        enterpriseParam['safeProductionEnterprise.address'] = '企业地址%s'%CommonUtil.createRandomString()
        enterpriseParam['safeProductionEnterprise.legalPerson'] = '法人代表%s'%CommonUtil.createRandomString()     
        enterpriseParam['safeProductionEnterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='企业类型', displayName='规上企业')
        enterpriseParam['safeProductionEnterprise.landlordName'] = '房东姓名%s'%CommonUtil.createRandomString()
        enterpriseParam['safeProductionEnterprise.landlordMobile'] = '11111111111'
        enterpriseParam['safeProductionEnterprise.safeProductiontype.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='安全生产企业类型', displayName='一般企业')
        enterpriseParam['safeProductionEnterprise.mobileNumber'] = '11111111112'
        enterpriseParam['safeProductionEnterprise.businessLicense'] = 'aaaaaa'
        enterpriseParam['safeProductionEnterprise.employeeAmount'] = '100'
        enterpriseParam['safeProductionEnterprise.isEmphasis'] = 'false'  #是否注销
        enterpriseParam['safeProductionEnterprise.gridPerson'] = '%s-%s'%( CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.username= '%s' " % userInit['DftWangGeUser']),orgInit['DftWangGeOrg'])
        responseDict = XunJianIntf.add_enterprise(enterpriseParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增企业失败') 
        
    #新增合格的巡检记录信息
        inspectionParam = copy.deepcopy(XunJianPara.inspectionObject) 
        inspectionParam['mode'] = 'addInspectionRecord'
        inspectionParam['inspection.orgId'] = enterpriseParam['ownerOrg.id'] 
        inspectionParam['safeProductionEnterprise.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from SafeProductionEnterprise t where t.name='%s' " % enterpriseParam['safeProductionEnterprise.name'])
        inspectionParam['safeProductionEnterprise.name'] = enterpriseParam['safeProductionEnterprise.name'] 
        inspectionParam['inspectionRecord.enterprise.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from SafeProductionEnterprise t where t.name='%s' " % enterpriseParam['safeProductionEnterprise.name'])
        inspectionParam['inspection.inspectTime'] = Time.getCurrentDate()
        inspectionParam['inspection.inspectAddress'] = enterpriseParam['safeProductionEnterprise.address']
        inspectionParam['inspection.inspectResult'] = '1' #? 合格：1 不合格：0
        inspectionParam['inspection.limitTime'] = Time.getCurrentDate()
        inspectionParam['inspection.inspectUserId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.organizationid='%s' " % enterpriseParam['ownerOrg.id'] ) 
        inspectionParam['inspection.inspectName'] = userInit['DftWangGeUserXM']
        inspectionParam['inspection.remark'] = '描述%s'%CommonUtil.createRandomString()
        responseDict = XunJianIntf.add_InspectionRecord(inspectionParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '巡检记录添加失败') 
     
    #导出企业巡检记录信息                            
        downLoadHuJiparam = copy.deepcopy(XunJianPara.dlXunJianData)
        downLoadHuJiparam['inspectionRecordVo.orgId']=orgInit['DftWangGeOrgId']
        downLoadHuJiparam['mode']='inspectionRecord'
        downLoadHuJiparam['pageOnly']='true'  #导出全部数据:false 导出本页数据:true
        response = XunJianIntf.downLoad_XunJian(downLoadHuJiparam, username=userInit['DftWangGeUser'], password='11111111')         
        with open("C:/autotest_file/downLoadXunJian.xls", "wb") as code:
            code.write(response.content)

    #检查导出信息
        checkParam = copy.deepcopy(XunJianPara.checkEnterpriseDict)   
        checkParam['name'] = enterpriseParam['safeProductionEnterprise.name']
        ret = CommonUtil.checkExcelCellValue(checkParam['name'], 'downLoadXunJian.xls','巡检记录', 'A4')          
        self.assertTrue(ret, '导出失败')
        pass

    def testInspectionRecordReview_10(self):
        """企业>巡检记录 复查"""
    #新增企业信息 1
        enterpriseParam = copy.deepcopy(XunJianPara.enterpriseObject) 
        enterpriseParam['mode'] = 'addInspection'
        enterpriseParam['ownerOrg.id'] = orgInit['DftWangGeOrgId']
        enterpriseParam['orgName'] = orgInit['DftWangGeOrg']
        enterpriseParam['safeProductionEnterprise.name'] = '企业名称%s'%CommonUtil.createRandomString()
        enterpriseParam['safeProductionEnterprise.address'] = '企业地址%s'%CommonUtil.createRandomString()
        enterpriseParam['safeProductionEnterprise.legalPerson'] = '法人代表%s'%CommonUtil.createRandomString()     
        enterpriseParam['safeProductionEnterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='企业类型', displayName='规上企业')
        enterpriseParam['safeProductionEnterprise.landlordName'] = '房东姓名%s'%CommonUtil.createRandomString()
        enterpriseParam['safeProductionEnterprise.landlordMobile'] = '11111111111'
        enterpriseParam['safeProductionEnterprise.safeProductiontype.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='安全生产企业类型', displayName='一般企业')
        enterpriseParam['safeProductionEnterprise.mobileNumber'] = '11111111112'
        enterpriseParam['safeProductionEnterprise.businessLicense'] = 'aaaaaa'
        enterpriseParam['safeProductionEnterprise.employeeAmount'] = '100'
        enterpriseParam['safeProductionEnterprise.isEmphasis'] = 'false'  #是否注销
        enterpriseParam['safeProductionEnterprise.gridPerson'] = '%s-%s'%( CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.username= '%s' " % userInit['DftWangGeUser']),orgInit['DftWangGeOrg'])
        responseDict = XunJianIntf.add_enterprise(enterpriseParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增企业失败') 
     
    #复查不合格的巡检记录信息   （复查合格）   
        reviewParam = copy.deepcopy(XunJianPara.reviewInspectionObject)
        reviewParam['mode'] = 'success'  
        reviewParam['inspection.orgId'] = enterpriseParam['ownerOrg.id']
        reviewParam['inspection.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from inspection t where t.id =(select max(id) from inspection)")+1   
        reviewParam['inspection.inspectAddress'] = enterpriseParam['safeProductionEnterprise.address']
        reviewParam['inspectionRecord.enterprise.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from safeproductionenterprise t where t.name='%s'" % enterpriseParam['safeProductionEnterprise.name'])
        reviewParam['inspection.inspectTime'] = Time.getCurrentDate()
        reviewParam['isSolve2'] = 'true' #复查合格 true  不合格 false
        reviewParam['inspection.inspectResult'] = '1'  #复查合格 1   不合格 0
        reviewParam['inspection.inspectUserId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.organizationid='%s' " % enterpriseParam['ownerOrg.id'] )
        reviewParam['inspection.inspectName'] = userInit['DftWangGeUserXM']
        reviewParam['solveIds'] = '2,'    
        ret = XunJianIntf.review_inspection(reviewParam, username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '复查企业不合格巡检记录失败')         

    #在检查记录列表中检查复查后的巡检记录信息
        checkParam = copy.deepcopy(XunJianPara.checkEnterpriseDict)
        checkParam['name'] = enterpriseParam['safeProductionEnterprise.name']   
        ret = XunJianIntf.check_InspectionRecord(checkParam, orgId=orgInit['DftWangGeOrgId'],mode = 'inspectionRecord',username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '未检查到巡检信息') 

    #在待检查列表中该复查后的巡检记录信息不存在     
        checkParam = copy.deepcopy(XunJianPara.checkEnterpriseDict)
        checkParam['name'] = enterpriseParam['safeProductionEnterprise.name']    
        ret = XunJianIntf.check_InspectionRecord(checkParam, orgId=orgInit['DftWangGeOrgId'],mode = 'reviewRecord',username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '复查后的巡检记录在带复查列表中依然存在，复查失败') 
        
    #复查不合格的巡检记录信息   （复查不合格）   
        newReviewParam = copy.deepcopy(XunJianPara.reviewInspectionObject)
        newReviewParam['mode'] = 'success'  
        newReviewParam['inspection.orgId'] = enterpriseParam['ownerOrg.id']
        newReviewParam['inspection.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from inspection t where t.id =(select max(id) from inspection)")+1   
        newReviewParam['inspection.inspectAddress'] = enterpriseParam['safeProductionEnterprise.address']
        newReviewParam['inspectionRecord.enterprise.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from safeproductionenterprise t where t.name='%s'" % enterpriseParam['safeProductionEnterprise.name'])
        newReviewParam['inspection.inspectTime'] = Time.getCurrentDate()
        newReviewParam['isSolve2'] = 'false' #复查合格 true  不合格 false
        newReviewParam['inspection.inspectResult'] = '0'  #复查合格 1   不合格 0
        newReviewParam['inspection.inspectUserId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.organizationid='%s' " % enterpriseParam['ownerOrg.id'] ) 
        newReviewParam['inspection.inspectName'] = userInit['DftWangGeUserXM']
        newReviewParam['noSolveIds'] = '2,'     #?
        ret = XunJianIntf.review_inspection(newReviewParam, username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '复查企业不合格巡检记录失败')         
 
    #在检查记录列表中检查复查后的巡检记录信息
        checkParam = copy.deepcopy(XunJianPara.checkEnterpriseDict)
        checkParam['name'] = enterpriseParam['safeProductionEnterprise.name']   
        ret = XunJianIntf.check_InspectionRecord(checkParam, orgId=orgInit['DftWangGeOrgId'],mode = 'inspectionRecord',username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '未检查到巡检信息') 
 
    #在待检查列表中该复查后的巡检记录信息不存在     
        checkParam = copy.deepcopy(XunJianPara.checkEnterpriseDict)
        checkParam['name'] = enterpriseParam['safeProductionEnterprise.name']    
        ret = XunJianIntf.check_InspectionRecord(checkParam, orgId=orgInit['DftWangGeOrgId'],mode = 'reviewRecord',username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '复查后的巡检记录在带复查列表中依然存在，复查失败') 
         
    #在检查受理中心列表中检查复查后未整改的巡检记录信息
        checkParam = copy.deepcopy(XunJianPara.checkEnterpriseDict)
        checkParam['name'] = enterpriseParam['safeProductionEnterprise.name']   
        ret = XunJianIntf.check_InspectionRecord(checkParam, orgId=orgInit['DftWangGeOrgId'],mode = 'acceptCenterRecord',username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '在受理中心列表中未检查到未整改的巡检记录信息')
        pass



#受理中心



    def testTurnIssueAcceptCenter_12(self):  
        """企业>巡检记录 转事件"""
        
    #新增隐患项信息
        riskRemarkParam = copy.deepcopy(XunJianPara.riskRemarkObject) 
        riskRemarkParam['riskRemark.riskRemarkName'] = '严重隐患备注项%s'%CommonUtil.createRandomString()
        riskRemarkParam['riskRemark.level.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='隐患等级', displayName='严重') # 不合格：2014  严重：2015  
        riskRemarkParam['riskRemark.isEnable'] = '1'
        riskRemarkParam['mode'] = 'add'
        riskRemarkParam['riskRemark.riskmarkerType'] = '0'     
        riskRemarkParam['riskRemark.orgId.id'] = orgInit['DftJieDaoOrgId']
        riskRemarkParam['isSubmit'] = 'true'  #是否启用：是-true  否-false
        responseDict = XunJianIntf.add_riskRemark(riskRemarkParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增隐患项失败')         
        
    #新增企业信息
        enterpriseParam = copy.deepcopy(XunJianPara.enterpriseObject) 
        enterpriseParam['mode'] = 'addInspection'
        enterpriseParam['ownerOrg.id'] = orgInit['DftWangGeOrgId']
        enterpriseParam['orgName'] = orgInit['DftWangGeOrg']
        enterpriseParam['safeProductionEnterprise.name'] = '转事件企业名称%s'%CommonUtil.createRandomString()
        enterpriseParam['safeProductionEnterprise.address'] = '企业地址%s'%CommonUtil.createRandomString()
        enterpriseParam['safeProductionEnterprise.legalPerson'] = '法人代表%s'%CommonUtil.createRandomString()     
        enterpriseParam['safeProductionEnterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='企业类型', displayName='规上企业')
        enterpriseParam['safeProductionEnterprise.landlordName'] = '房东姓名%s'%CommonUtil.createRandomString()
        enterpriseParam['safeProductionEnterprise.landlordMobile'] = '11111111111'
        enterpriseParam['safeProductionEnterprise.safeProductiontype.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='安全生产企业类型', displayName='一般企业')
        enterpriseParam['safeProductionEnterprise.mobileNumber'] = '11111111112'
        enterpriseParam['safeProductionEnterprise.businessLicense'] = 'aaaaaa'
        enterpriseParam['safeProductionEnterprise.employeeAmount'] = '100'
        enterpriseParam['safeProductionEnterprise.isEmphasis'] = 'false'  #是否注销
        enterpriseParam['safeProductionEnterprise.gridPerson'] = '%s-%s'%( CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.username= '%s' " % userInit['DftWangGeUser']),orgInit['DftWangGeOrg'])
        responseDict = XunJianIntf.add_enterprise(enterpriseParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增企业失败') 
        
    #新增严重的巡检记录信息
        inspectionParam = copy.deepcopy(XunJianPara.inspectionObject)         
        inspectionParam['mode'] = 'addInspectionRecord'
        inspectionParam['inspection.orgId'] = enterpriseParam['ownerOrg.id'] 
        inspectionParam['safeProductionEnterprise.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from SafeProductionEnterprise t where t.name='%s' " % enterpriseParam['safeProductionEnterprise.name'])
        inspectionParam['safeProductionEnterprise.name'] = enterpriseParam['safeProductionEnterprise.name'] 
        inspectionParam['inspectionRecord.enterprise.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from SafeProductionEnterprise t where t.name='%s' " % enterpriseParam['safeProductionEnterprise.name'])
        inspectionParam['inspection.inspectTime'] = Time.getCurrentDate()
        inspectionParam['inspection.inspectAddress'] = enterpriseParam['safeProductionEnterprise.address']
        inspectionParam['riskRemarkName'] = 'on' #合格时：为空  不合格，严重时：on
        inspectionParam['inspection.inspectResult'] = '2' # 合格：1 不合格：0  严重：2
        inspectionParam['inspection.limitTime'] = Time.getCurrentDate()
        inspectionParam['inspection.inspectUserId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.organizationid='%s' " % enterpriseParam['ownerOrg.id'] ) 
        inspectionParam['inspection.inspectName'] = userInit['DftWangGeUserXM']
        inspectionParam['riskRemarkIds'] = '2' #合格：空  不合格，严重时：2
        inspectionParam['inspection.remark'] = '描述%s'%CommonUtil.createRandomString()
        responseDict = XunJianIntf.add_InspectionRecord(inspectionParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '巡检记录添加失败') 
        
    #将待转的巡检记录转事件处理    
        turnIssueParam = copy.deepcopy(XunJianPara.turnIssueObject)
        turnIssueParam['issue.occurOrg.id'] = inspectionParam['inspection.orgId']
        turnIssueParam['inspectionIds'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from inspection t where t.inspectaddress='%s'" % enterpriseParam['safeProductionEnterprise.address'])
        turnIssueParam['dataSource'] = 'inspectionIssue'
        turnIssueParam['issue.subject'] = '企业-%s'% enterpriseParam['safeProductionEnterprise.name']
        turnIssueParam['selectOrgName'] = inspectionParam['inspection.inspectName']
        turnIssueParam['issue.occurLocation'] = inspectionParam['inspection.inspectName']
        turnIssueParam['issue.occurDate'] = Time.getCurrentDate()
        turnIssueParam['eatHours'] = time.strftime("%I")
        turnIssueParam['eatMinute'] = time.strftime("%M")
        turnIssueParam['selectedTypes'] = '1'  #事件类型   
        turnIssueParam['issueRelatedPeopleNames'] = enterpriseParam['safeProductionEnterprise.legalPerson']
        turnIssueParam['issueRelatedPeopleTelephones'] = enterpriseParam['safeProductionEnterprise.mobileNumber']
        turnIssueParam['issue.relatePeopleCount'] = '10'  #人数
        turnIssueParam['issue.issueContent'] = riskRemarkParam['riskRemark.riskRemarkName']
        ret = XunJianIntf.turnIssueAcceptCenter(turnIssueParam, username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '巡检记录转事件失败') 

#     #在检查受理中心列表中检查该巡检记录的状态
#         checkParam = copy.deepcopy(XunJianPara.checkEnterpriseDict)
#         checkParam['name'] = enterpriseParam['safeProductionEnterprise.name']   
#         checkParam['state'] = '5'  #受理状态： 待流转-3 办理中-5  
#         ret = XunJianIntf.check_InspectionRecord(checkParam, orgId=orgInit['DftWangGeOrgId'],mode = 'acceptCenterRecord',username=userInit['DftWangGeUser'], password='11111111')         
#         self.assertTrue(ret, '在受理中心列表中巡检记录信息状态为改变')
        
    #验证事件处理模块下是否有转移的巡检记录信息
        checkParam=copy.deepcopy(ShiJianChuLiPara.IssueCheckPara)
        checkParam['subject']=turnIssueParam['issue.subject']
        ret=XunJianIntf.check_issues(checkParam,orgId=orgInit['DftWangGeOrgId'],searchYear=time.strftime("%Y"),username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(ret, '全部事项列表中没有找到对应的事件')

    def testRecordSearch_13(self): #高级搜索？
        """受理中心检查记录 搜索 """
    #新增企业信息 1
        enterpriseParam = copy.deepcopy(XunJianPara.enterpriseObject) 
        enterpriseParam['mode'] = 'addInspection'
        enterpriseParam['ownerOrg.id'] = orgInit['DftWangGeOrgId']
        enterpriseParam['orgName'] = orgInit['DftWangGeOrg']
        enterpriseParam['safeProductionEnterprise.name'] = '企业名称1%s'%CommonUtil.createRandomString()
        enterpriseParam['safeProductionEnterprise.address'] = '企业地址%s'%CommonUtil.createRandomString()
        enterpriseParam['safeProductionEnterprise.legalPerson'] = '法人代表%s'%CommonUtil.createRandomString()     
        enterpriseParam['safeProductionEnterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='企业类型', displayName='规上企业')
        enterpriseParam['safeProductionEnterprise.landlordName'] = '房东姓名%s'%CommonUtil.createRandomString()
        enterpriseParam['safeProductionEnterprise.landlordMobile'] = '11111111111'
        enterpriseParam['safeProductionEnterprise.safeProductiontype.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='安全生产企业类型', displayName='一般企业')
        enterpriseParam['safeProductionEnterprise.mobileNumber'] = '11111111112'
        enterpriseParam['safeProductionEnterprise.businessLicense'] = 'aaaaaa'
        enterpriseParam['safeProductionEnterprise.employeeAmount'] = '100'
        enterpriseParam['safeProductionEnterprise.isEmphasis'] = 'false'  #是否注销
        enterpriseParam['safeProductionEnterprise.gridPerson'] = '%s-%s'%( CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.username= '%s' " % userInit['DftWangGeUser']),orgInit['DftWangGeOrg'])
        responseDict = XunJianIntf.add_enterprise(enterpriseParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增企业失败') 
         
    #新增严重的巡检记录信息 1
        inspectionParam = copy.deepcopy(XunJianPara.inspectionObject)         
        inspectionParam['mode'] = 'addInspectionRecord'
        inspectionParam['inspection.orgId'] = enterpriseParam['ownerOrg.id'] 
        inspectionParam['safeProductionEnterprise.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from SafeProductionEnterprise t where t.name='%s' " % enterpriseParam['safeProductionEnterprise.name'])
        inspectionParam['safeProductionEnterprise.name'] = enterpriseParam['safeProductionEnterprise.name'] 
        inspectionParam['inspectionRecord.enterprise.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from SafeProductionEnterprise t where t.name='%s' " % enterpriseParam['safeProductionEnterprise.name'])
        inspectionParam['inspection.inspectTime'] = Time.getCurrentDate()
        inspectionParam['inspection.inspectAddress'] = enterpriseParam['safeProductionEnterprise.address']
        inspectionParam['riskRemarkName'] = 'on' #合格时：为空  不合格，严重时：on
        inspectionParam['inspection.inspectResult'] = '2' # 合格：1 不合格：0  严重：2
        inspectionParam['inspection.limitTime'] = Time.getCurrentDate()
        inspectionParam['inspection.inspectUserId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.organizationid='%s' " % enterpriseParam['ownerOrg.id'] ) 
        inspectionParam['inspection.inspectName'] = userInit['DftWangGeUserXM']
        inspectionParam['riskRemarkIds'] = '2' #合格：空  不合格，严重时：2
        inspectionParam['inspection.remark'] = '描述%s'%CommonUtil.createRandomString()
        responseDict = XunJianIntf.add_InspectionRecord(inspectionParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '巡检记录添加失败')
        
    #新增企业信息 2
        newEnterpriseParam = copy.deepcopy(XunJianPara.enterpriseObject) 
        newEnterpriseParam['mode'] = 'addInspection'
        newEnterpriseParam['ownerOrg.id'] = orgInit['DftWangGeOrgId']
        newEnterpriseParam['orgName'] = orgInit['DftWangGeOrg']
        newEnterpriseParam['safeProductionEnterprise.name'] = '企业名称2%s'%CommonUtil.createRandomString()
        newEnterpriseParam['safeProductionEnterprise.address'] = '企业地址%s'%CommonUtil.createRandomString()
        newEnterpriseParam['safeProductionEnterprise.legalPerson'] = '法人代表%s'%CommonUtil.createRandomString()     
        newEnterpriseParam['safeProductionEnterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='企业类型', displayName='规上企业')
        newEnterpriseParam['safeProductionEnterprise.landlordName'] = '房东姓名%s'%CommonUtil.createRandomString()
        newEnterpriseParam['safeProductionEnterprise.landlordMobile'] = '11111111111'
        newEnterpriseParam['safeProductionEnterprise.safeProductiontype.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='安全生产企业类型', displayName='一般企业')
        newEnterpriseParam['safeProductionEnterprise.mobileNumber'] = '11111111112'
        newEnterpriseParam['safeProductionEnterprise.businessLicense'] = 'aaaaaa'
        newEnterpriseParam['safeProductionEnterprise.employeeAmount'] = '100'
        newEnterpriseParam['safeProductionEnterprise.isEmphasis'] = 'false'  #是否注销
        newEnterpriseParam['safeProductionEnterprise.gridPerson'] = '%s-%s'%( CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.username= '%s' " % userInit['DftWangGeUser']),orgInit['DftWangGeOrg'])
        responseDict = XunJianIntf.add_enterprise(newEnterpriseParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增企业失败') 
        
    #新增严重的巡检记录信息 2
        newInspectionParam = copy.deepcopy(XunJianPara.inspectionObject)         
        newInspectionParam['mode'] = 'addInspectionRecord'
        newInspectionParam['inspection.orgId'] = newEnterpriseParam['ownerOrg.id'] 
        newInspectionParam['safeProductionEnterprise.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from SafeProductionEnterprise t where t.name='%s' " % newEnterpriseParam['safeProductionEnterprise.name'])
        newInspectionParam['safeProductionEnterprise.name'] = newEnterpriseParam['safeProductionEnterprise.name'] 
        newInspectionParam['inspectionRecord.enterprise.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from SafeProductionEnterprise t where t.name='%s' " % newEnterpriseParam['safeProductionEnterprise.name'])
        newInspectionParam['inspection.inspectTime'] = Time.getCurrentDate()
        newInspectionParam['inspection.inspectAddress'] = newEnterpriseParam['safeProductionEnterprise.address']
        newInspectionParam['riskRemarkName'] = 'on' #合格时：为空  不合格，严重时：on
        newInspectionParam['inspection.inspectResult'] = '2' # 合格：1 不合格：0  严重：2
        newInspectionParam['inspection.limitTime'] = Time.getCurrentDate()
        newInspectionParam['inspection.inspectUserId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.organizationid='%s' " % newEnterpriseParam['ownerOrg.id'] ) 
        newInspectionParam['inspection.inspectName'] = userInit['DftWangGeUserXM']
        newInspectionParam['riskRemarkIds'] = '2' #合格：空  不合格，严重时：2
        newInspectionParam['inspection.remark'] = '描述%s'%CommonUtil.createRandomString()
        responseDict = XunJianIntf.add_InspectionRecord(newInspectionParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '巡检记录添加失败')

    #搜索巡检记录信息1   
        searchParam = copy.deepcopy(XunJianPara.checkEnterpriseDict)
        searchParam['name'] = enterpriseParam['safeProductionEnterprise.name']    
        ret = XunJianIntf.check_InspectionRecord(searchParam, orgId=orgInit['DftWangGeOrgId'],mode = 'acceptCenterRecord',inspectName = userInit['DftWangGeUserXM'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '未搜索到巡检信息') 
    
    #高级搜索巡检记录信息2    
        advancedSearch_Param = copy.deepcopy(XunJianPara.checkEnterpriseDict)
        advancedSearch_Param['name'] = newEnterpriseParam['safeProductionEnterprise.name']    
        ret = XunJianIntf.search_AcceptCenter(advancedSearch_Param, orgId=orgInit['DftWangGeOrgId'],mode = 'acceptCenterRecord',name = newEnterpriseParam['safeProductionEnterprise.name'],inspectAddress=newInspectionParam['inspection.inspectAddress'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '高级搜索失败') 
         
    #高级搜索不符合条件的巡检记录信息     
        advancedSearch_Param = copy.deepcopy(XunJianPara.checkEnterpriseDict)
        advancedSearch_Param['name'] = '巡检记录'    
        ret = XunJianIntf.check_InspectionRecord(advancedSearch_Param, orgId=orgInit['DftWangGeOrgId'],mode = 'acceptCenterRecord',name = '巡检记录',username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '未搜索到巡检信息') 
        pass

    def testRecordDelete_14(self):   
        """受理中心检查记录 删除 """
    #新增隐患项信息
        riskRemarkParam = copy.deepcopy(XunJianPara.riskRemarkObject) 
        riskRemarkParam['riskRemark.riskRemarkName'] = '严重隐患备注项%s'%CommonUtil.createRandomString()
        riskRemarkParam['riskRemark.level.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='隐患等级', displayName='严重') # 不合格：2014  严重：2015  
        riskRemarkParam['riskRemark.isEnable'] = '1'
        riskRemarkParam['mode'] = 'add'
        riskRemarkParam['riskRemark.riskmarkerType'] = '0'     
        riskRemarkParam['riskRemark.orgId.id'] = orgInit['DftJieDaoOrgId']
        riskRemarkParam['isSubmit'] = 'true'  #是否启用：是-true  否-false
        responseDict = XunJianIntf.add_riskRemark(riskRemarkParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增隐患项失败')         
        
    #新增企业信息
        enterpriseParam = copy.deepcopy(XunJianPara.enterpriseObject) 
        enterpriseParam['mode'] = 'addInspection'
        enterpriseParam['ownerOrg.id'] = orgInit['DftWangGeOrgId']
        enterpriseParam['orgName'] = orgInit['DftWangGeOrg']
        enterpriseParam['safeProductionEnterprise.name'] = '转事件企业名称%s'%CommonUtil.createRandomString()
        enterpriseParam['safeProductionEnterprise.address'] = '企业地址%s'%CommonUtil.createRandomString()
        enterpriseParam['safeProductionEnterprise.legalPerson'] = '法人代表%s'%CommonUtil.createRandomString()     
        enterpriseParam['safeProductionEnterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='企业类型', displayName='规上企业')
        enterpriseParam['safeProductionEnterprise.landlordName'] = '房东姓名%s'%CommonUtil.createRandomString()
        enterpriseParam['safeProductionEnterprise.landlordMobile'] = '11111111111'
        enterpriseParam['safeProductionEnterprise.safeProductiontype.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='安全生产企业类型', displayName='一般企业')
        enterpriseParam['safeProductionEnterprise.mobileNumber'] = '11111111112'
        enterpriseParam['safeProductionEnterprise.businessLicense'] = 'aaaaaa'
        enterpriseParam['safeProductionEnterprise.employeeAmount'] = '100'
        enterpriseParam['safeProductionEnterprise.isEmphasis'] = 'false'  #是否注销
        enterpriseParam['safeProductionEnterprise.gridPerson'] = '%s-%s'%( CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.username= '%s' " % userInit['DftWangGeUser']),orgInit['DftWangGeOrg'])
        responseDict = XunJianIntf.add_enterprise(enterpriseParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增企业失败') 
        
    #新增严重的巡检记录信息
        inspectionParam = copy.deepcopy(XunJianPara.inspectionObject)         
        inspectionParam['mode'] = 'addInspectionRecord'
        inspectionParam['inspection.orgId'] = enterpriseParam['ownerOrg.id'] 
        inspectionParam['safeProductionEnterprise.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from SafeProductionEnterprise t where t.name='%s' " % enterpriseParam['safeProductionEnterprise.name'])
        inspectionParam['safeProductionEnterprise.name'] = enterpriseParam['safeProductionEnterprise.name'] 
        inspectionParam['inspectionRecord.enterprise.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from SafeProductionEnterprise t where t.name='%s' " % enterpriseParam['safeProductionEnterprise.name'])
        inspectionParam['inspection.inspectTime'] = Time.getCurrentDate()
        inspectionParam['inspection.inspectAddress'] = enterpriseParam['safeProductionEnterprise.address']
        inspectionParam['riskRemarkName'] = 'on' #合格时：为空  不合格，严重时：on
        inspectionParam['inspection.inspectResult'] = '2' # 合格：1 不合格：0  严重：2
        inspectionParam['inspection.limitTime'] = Time.getCurrentDate()
        inspectionParam['inspection.inspectUserId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.organizationid='%s' " % enterpriseParam['ownerOrg.id'] ) 
        inspectionParam['inspection.inspectName'] = userInit['DftWangGeUserXM']
        inspectionParam['riskRemarkIds'] = '2' #合格：空  不合格，严重时：2
        inspectionParam['inspection.remark'] = '描述%s'%CommonUtil.createRandomString()
        responseDict = XunJianIntf.add_InspectionRecord(inspectionParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '巡检记录添加失败') 
        
    #将待转的巡检记录转事件处理    
        turnIssueParam = copy.deepcopy(XunJianPara.turnIssueObject)
        turnIssueParam['issue.occurOrg.id'] = inspectionParam['inspection.orgId']
        turnIssueParam['inspectionIds'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from inspection t where t.inspectaddress='%s'" % enterpriseParam['safeProductionEnterprise.address'])
        turnIssueParam['dataSource'] = 'inspectionIssue'
        turnIssueParam['issue.subject'] = '企业-%s'% enterpriseParam['safeProductionEnterprise.name']
        turnIssueParam['selectOrgName'] = inspectionParam['inspection.inspectName']
        turnIssueParam['issue.occurLocation'] = inspectionParam['inspection.inspectName']
        turnIssueParam['issue.occurDate'] = Time.getCurrentDate()
        turnIssueParam['eatHours'] = time.strftime("%I")
        turnIssueParam['eatMinute'] = time.strftime("%M")
        turnIssueParam['selectedTypes'] = '1'  #事件类型   
        turnIssueParam['issueRelatedPeopleNames'] = enterpriseParam['safeProductionEnterprise.legalPerson']
        turnIssueParam['issueRelatedPeopleTelephones'] = enterpriseParam['safeProductionEnterprise.mobileNumber']
        turnIssueParam['issue.relatePeopleCount'] = '10'  #人数
        turnIssueParam['issue.issueContent'] = riskRemarkParam['riskRemark.riskRemarkName']
        rs = XunJianIntf.turnIssueAcceptCenter(turnIssueParam, username=userInit['DftWangGeUser'], password='11111111')         
        responseDict = json.loads(rs.text)
        self.assertTrue(rs, '巡检记录转事件失败') 
        
    #验证事件处理模块下是否有转移的巡检记录信息
        checkParam=copy.deepcopy(ShiJianChuLiPara.IssueCheckPara)
        checkParam['subject']=turnIssueParam['issue.subject']
        ret=XunJianIntf.check_issues(checkParam,orgId=orgInit['DftWangGeOrgId'],searchYear=time.strftime("%Y"),username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(ret, '全部事项列表中没有找到对应的事件')

    #设置结案参数
        sIssuePara=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)        
        sIssuePara['operation.dealOrg.id']=orgInit['DftWangGeOrgId']
        sIssuePara['operation.issue.id']=responseDict['issueId']
        sIssuePara['keyId']=responseDict['issueStepId']      
        sIssuePara['operation.dealUserName']=userInit['DftWangGeUserXM']
        sIssuePara['operation.mobile']=userInit['DftWangGeUserSJ']
        sIssuePara['dealCode']='31' #结案
        sIssuePara['dealTime']=Time.getCurrentDate()
        sIssuePara['operation.content']='事件处理'  
    #事件结案
        result=XunJianIntf.deal_Issue(issueDict=sIssuePara,username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(result.result, '事件操作失败!')
        
    #删除已办结的企业巡检信息
        delParam = copy.deepcopy(XunJianPara.deleteDict)
        delParam['enterpriseId'] = inspectionParam['safeProductionEnterprise.id']
        delParam['id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from inspection t where t.inspectaddress='%s'" % enterpriseParam['safeProductionEnterprise.address'])
        delParam['inspectionId'] = inspectionParam['inspectionRecord.enterprise.id'] 
        delParam['isSecretSupervision'] = 'true'
        ret =  XunJianIntf.delete_AcceptCenter(delParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret.result,'督查暗访删除失败')
        
    #在受理中心检查已删除的企业巡检记录信息     
        checkParam = copy.deepcopy(XunJianPara.checkRentalDict)
        checkParam['name'] = enterpriseParam['safeProductionEnterprise.name']
        ret = XunJianIntf.check_InspectionRecord(checkParam, orgId=orgInit['DftWangGeOrgId'],mode = 'acceptCenterRecord',username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '删除的企业巡检记录依然存在，删除失败')
 
 
 #督查暗访
 
 
 
    def testsecretSupervisionAdd_15(self):
        """督查暗访记录 新增 """
    #新增督查暗访记录 
        getSupervisionParam = copy.deepcopy(XunJianPara.supervisionObject) 
        getSupervisionParam['safeProductionEnterprise.name'] = '检查单位%s'%CommonUtil.createRandomString()
        getSupervisionParam['orgId'] = orgInit['DftJieDaoOrgId']
        response = XunJianIntf.supervision(getSupervisionParam, username=userInit['DftJieDaoUser'], password='11111111')
    
        supervisionParam = copy.deepcopy(XunJianPara.supervisionObject) 
        supervisionParam['secretSupervision.checkSubject'] = '检查科目%s'%CommonUtil.createRandomString()
        supervisionParam['secretSupervision.checkTime'] = Time.getCurrentDate()
        supervisionParam['secretSupervision.checkCompanyName'] = getSupervisionParam['safeProductionEnterprise.name']
        supervisionParam['secretSupervision.checkAddress'] = '检查地址%s'%CommonUtil.createRandomString()
        supervisionParam['secretSupervision.checkLegalPerson'] = '法人代表1%s'%CommonUtil.createRandomString()
        supervisionParam['secretSupervision.mobileNumber'] = '13000000000'
        supervisionParam['secretSupervision.findProblems'] = '检查结果%s'%CommonUtil.createRandomString()     
        supervisionParam['secretSupervision.requires'] = '要求%s'%CommonUtil.createRandomString()
        supervisionParam['mode'] = 'add'
        supervisionParam['isSubmit'] = 'true'
        supervisionParam['secretSupervision.orgId'] = getSupervisionParam['orgId'] 
        responseDict = XunJianIntf.add_supervision(supervisionParam, username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')  
        
    #检查新增的督查暗访记录信息 
        checkParam = copy.deepcopy(XunJianPara.checkSupervisionDict)
        checkParam['checkAddress'] = supervisionParam['secretSupervision.checkAddress']  
        ret = XunJianIntf.check_Supervision(checkParam, orgId=orgInit['DftJieDaoOrgId'],username=userInit['DftJieDaoUser'], password='11111111')         
        self.assertTrue(ret, '未检查到督查暗访信息') 
        
    #在检查受理中心列表中检查督查暗访新增的巡检记录信息
        checkParam = copy.deepcopy(XunJianPara.checkSupervisionDict)
        checkParam['checkAddress'] = supervisionParam['secretSupervision.checkAddress']  
        ret = XunJianIntf.check_Supervision(checkParam, orgId=orgInit['DftJieDaoOrgId'],state='3',username=userInit['DftJieDaoUser'], password='11111111')         
        self.assertTrue(ret, '未检查到督查暗访信息')        

        pass

    def testsecretSupervisionSearch_16(self):
        """督查暗访记录 搜索 """
    #新增督查暗访记录 1
        getSupervisionParam = copy.deepcopy(XunJianPara.supervisionObject) 
        getSupervisionParam['safeProductionEnterprise.name'] = '检查单位1%s'%CommonUtil.createRandomString()
        getSupervisionParam['orgId'] = orgInit['DftJieDaoOrgId']
        response = XunJianIntf.supervision(getSupervisionParam, username=userInit['DftJieDaoUser'], password='11111111')
    
        supervisionParam = copy.deepcopy(XunJianPara.supervisionObject) 
        supervisionParam['secretSupervision.checkSubject'] = '检查科目%s'%CommonUtil.createRandomString()
        supervisionParam['secretSupervision.checkTime'] = Time.getCurrentDate()
        supervisionParam['secretSupervision.checkCompanyName'] = getSupervisionParam['safeProductionEnterprise.name']
        supervisionParam['secretSupervision.checkAddress'] = '检查地址%s'%CommonUtil.createRandomString()
        supervisionParam['secretSupervision.checkLegalPerson'] = '法人代表1%s'%CommonUtil.createRandomString()
        supervisionParam['secretSupervision.mobileNumber'] = '13000000000'
        supervisionParam['secretSupervision.findProblems'] = '检查结果%s'%CommonUtil.createRandomString()     
        supervisionParam['secretSupervision.requires'] = '要求%s'%CommonUtil.createRandomString()
        supervisionParam['mode'] = 'add'
        supervisionParam['isSubmit'] = 'true'
        supervisionParam['secretSupervision.orgId'] = getSupervisionParam['orgId'] 
        responseDict = XunJianIntf.add_supervision(supervisionParam, username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')  
        
    #新增督查暗访记录 2
        newGetSupervisionParam = copy.deepcopy(XunJianPara.supervisionObject) 
        newGetSupervisionParam['safeProductionEnterprise.name'] = '检查单位2%s'%CommonUtil.createRandomString()
        newGetSupervisionParam['orgId'] = orgInit['DftJieDaoOrgId']
        response = XunJianIntf.supervision(newGetSupervisionParam, username=userInit['DftJieDaoUser'], password='11111111')
    
        newSupervisionParam = copy.deepcopy(XunJianPara.supervisionObject) 
        newSupervisionParam['secretSupervision.checkSubject'] = '检查科目%s'%CommonUtil.createRandomString()
        newSupervisionParam['secretSupervision.checkTime'] = Time.getCurrentDate()
        newSupervisionParam['secretSupervision.checkCompanyName'] = getSupervisionParam['safeProductionEnterprise.name']
        newSupervisionParam['secretSupervision.checkAddress'] = '检查地址%s'%CommonUtil.createRandomString()
        newSupervisionParam['secretSupervision.checkLegalPerson'] = '法人代表1%s'%CommonUtil.createRandomString()
        newSupervisionParam['secretSupervision.mobileNumber'] = '13100000000'
        newSupervisionParam['secretSupervision.findProblems'] = '检查结果%s'%CommonUtil.createRandomString()     
        newSupervisionParam['secretSupervision.requires'] = '要求%s'%CommonUtil.createRandomString()
        newSupervisionParam['mode'] = 'add'
        newSupervisionParam['isSubmit'] = 'true'
        newSupervisionParam['secretSupervision.orgId'] = getSupervisionParam['orgId'] 
        responseDict = XunJianIntf.add_supervision(newSupervisionParam, username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')  
        
    #搜索新增的督查暗访记录信息 
        checkParam = copy.deepcopy(XunJianPara.checkSupervisionDict)
        checkParam['checkAddress'] = supervisionParam['secretSupervision.checkAddress']  
        ret = XunJianIntf.check_Supervision(checkParam, orgId=orgInit['DftJieDaoOrgId'],checkCompanyName=getSupervisionParam['safeProductionEnterprise.name'],username=userInit['DftJieDaoUser'], password='11111111')         
        self.assertTrue(ret, '未搜索到督查暗访信息') 
        
    #高级搜索新增的督查暗访记录信息 
        checkParam = copy.deepcopy(XunJianPara.checkSupervisionDict)
        checkParam['checkAddress'] = supervisionParam['secretSupervision.checkAddress']  
        ret = XunJianIntf.check_Supervision(checkParam, orgId=orgInit['DftJieDaoOrgId'],checkCompanyName=getSupervisionParam['safeProductionEnterprise.name'],checkAddress=supervisionParam['secretSupervision.checkAddress'],username=userInit['DftJieDaoUser'], password='11111111')         
        self.assertTrue(ret, '未高级搜索到督查暗访信息') 
        
    #搜索不符合条件的督查暗访记录信息 
        checkParam = copy.deepcopy(XunJianPara.checkSupervisionDict)
        checkParam['checkAddress'] = '检查单位'
        ret = XunJianIntf.check_Supervision(checkParam, orgId=orgInit['DftJieDaoOrgId'],checkCompanyName='检查单位',username=userInit['DftJieDaoUser'], password='11111111')         
        self.assertFalse(ret, '搜索到督查暗访信息')         
        pass

    def testsecretSupervisionDelete_17(self):  #只可删除已办结？
        """督查暗访记录 删除 """
    #新增督查暗访记录 
        getSupervisionParam = copy.deepcopy(XunJianPara.supervisionObject) 
        getSupervisionParam['safeProductionEnterprise.name'] = '检查单位1%s'%CommonUtil.createRandomString()
        getSupervisionParam['orgId'] = orgInit['DftJieDaoOrgId']
        response = XunJianIntf.supervision(getSupervisionParam, username=userInit['DftJieDaoUser'], password='11111111')
    
        supervisionParam = copy.deepcopy(XunJianPara.supervisionObject) 
        supervisionParam['secretSupervision.checkSubject'] = '检查科目%s'%CommonUtil.createRandomString()
        supervisionParam['secretSupervision.checkTime'] = Time.getCurrentDate()
        supervisionParam['secretSupervision.checkCompanyName'] = getSupervisionParam['safeProductionEnterprise.name']
        supervisionParam['secretSupervision.checkAddress'] = '检查地址%s'%CommonUtil.createRandomString()
        supervisionParam['secretSupervision.checkLegalPerson'] = '法人代表1%s'%CommonUtil.createRandomString()
        supervisionParam['secretSupervision.mobileNumber'] = '13000000000'
        supervisionParam['secretSupervision.findProblems'] = '检查结果%s'%CommonUtil.createRandomString()     
        supervisionParam['secretSupervision.requires'] = '要求%s'%CommonUtil.createRandomString()
        supervisionParam['mode'] = 'add'
        supervisionParam['isSubmit'] = 'true'
        supervisionParam['secretSupervision.orgId'] = getSupervisionParam['orgId'] 
        responseDict = XunJianIntf.add_supervision(supervisionParam, username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')    
        
    #将待转的巡检记录转事件处理    
        turnIssueParam = copy.deepcopy(XunJianPara.turnIssueObject)
        turnIssueParam['issue.occurOrg.id'] = getSupervisionParam['orgId']
        turnIssueParam['inspectionIds'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from inspection t where t.inspectaddress='%s'" % supervisionParam['secretSupervision.checkAddress'])
        turnIssueParam['dataSource'] = 'inspectionIssue'
        turnIssueParam['issue.subject'] = '督查暗访-%s'% getSupervisionParam['safeProductionEnterprise.name']
        turnIssueParam['selectOrgName'] = orgInit['DftJieDaoOrg']
        turnIssueParam['issue.occurLocation'] = userInit['DftJieDaoUserXM']
        turnIssueParam['issue.occurDate'] = Time.getCurrentDate()
        turnIssueParam['eatHours'] = time.strftime("%I")
        turnIssueParam['eatMinute'] = time.strftime("%M")
        turnIssueParam['selectedTypes'] = '1'  #事件类型   
        turnIssueParam['issueRelatedPeopleNames'] = supervisionParam['secretSupervision.checkLegalPerson']
        turnIssueParam['issueRelatedPeopleTelephones'] = supervisionParam['secretSupervision.mobileNumber']
        turnIssueParam['issue.relatePeopleCount'] = '10'  #人数
        turnIssueParam['issue.issueContent'] = '%s,%s'%(supervisionParam['secretSupervision.findProblems'] ,supervisionParam['secretSupervision.requires'])
        rs = XunJianIntf.turnIssueAcceptCenter(turnIssueParam, username=userInit['DftJieDaoUser'], password='11111111')  
        responseDict = json.loads(rs.text)
        self.assertTrue(rs, '巡检记录转事件失败') 
        
    #验证事件处理模块下是否有转移的巡检记录信息
        checkParam=copy.deepcopy(ShiJianChuLiPara.IssueCheckPara)
        checkParam['subject']=turnIssueParam['issue.subject']
        ret=XunJianIntf.check_issues(checkParam,orgId=orgInit['DftJieDaoOrgId'],searchYear=time.strftime("%Y"),username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(ret, '全部事项列表中没有找到对应的事件')
        
    #设置结案参数
        sIssuePara=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)        
        sIssuePara['operation.dealOrg.id']=orgInit['DftJieDaoOrgId']
        sIssuePara['operation.issue.id']=responseDict['issueId']
        sIssuePara['keyId']=responseDict['issueStepId']      
        sIssuePara['operation.dealUserName']=userInit['DftJieDaoUserXM']
        sIssuePara['operation.mobile']=userInit['DftJieDaoUserSJ']
        sIssuePara['dealCode']='31' #结案
        sIssuePara['dealTime']=Time.getCurrentDate()
        sIssuePara['operation.content']='事件处理'  
    #事件结案
        result=XunJianIntf.deal_Issue(issueDict=sIssuePara,username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(result.result, '事件操作失败!')
        
    #督查暗访删除
        delParam = copy.deepcopy(XunJianPara.deleteParam)
        delParam['selectIds'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from secretsupervision t where t.checkcompanyname='%s'"% getSupervisionParam['safeProductionEnterprise.name'])
        ret =  XunJianIntf.delete_supervision(delParam, username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(ret.result,'督查暗访删除失败')
        
    #检查新增的督查暗访记录信息 
        checkParam = copy.deepcopy(XunJianPara.checkSupervisionDict)
        checkParam['checkAddress'] = supervisionParam['secretSupervision.checkAddress']  
        ret = XunJianIntf.check_Supervision(checkParam, orgId=orgInit['DftJieDaoOrgId'],username=userInit['DftJieDaoUser'], password='11111111')         
        self.assertFalse(ret, '删除的督查暗访信息仍然存在，删除失败') 
        pass
    
    def testsecretSupervisionCheck_18(self):  #不同状态？
        """查看不同状态下的督查暗访记录 """
    #新增督查暗访记录 1
        getSupervisionParam = copy.deepcopy(XunJianPara.supervisionObject) 
        getSupervisionParam['safeProductionEnterprise.name'] = '检查单位1%s'%CommonUtil.createRandomString()
        getSupervisionParam['orgId'] = orgInit['DftJieDaoOrgId']
        response = XunJianIntf.supervision(getSupervisionParam, username=userInit['DftJieDaoUser'], password='11111111')
    
        supervisionParam = copy.deepcopy(XunJianPara.supervisionObject) 
        supervisionParam['secretSupervision.checkSubject'] = '检查科目%s'%CommonUtil.createRandomString()
        supervisionParam['secretSupervision.checkTime'] = Time.getCurrentDate()
        supervisionParam['secretSupervision.checkCompanyName'] = getSupervisionParam['safeProductionEnterprise.name']
        supervisionParam['secretSupervision.checkAddress'] = '检查地址%s'%CommonUtil.createRandomString()
        supervisionParam['secretSupervision.checkLegalPerson'] = '法人代表1%s'%CommonUtil.createRandomString()
        supervisionParam['secretSupervision.mobileNumber'] = '13000000000'
        supervisionParam['secretSupervision.findProblems'] = '检查结果%s'%CommonUtil.createRandomString()     
        supervisionParam['secretSupervision.requires'] = '要求%s'%CommonUtil.createRandomString()
        supervisionParam['mode'] = 'add'
        supervisionParam['isSubmit'] = 'true'
        supervisionParam['secretSupervision.orgId'] = getSupervisionParam['orgId'] 
        responseDict = XunJianIntf.add_supervision(supervisionParam, username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败') 
        
    #查看待流转记录  即：state='3'
        checkParam = copy.deepcopy(XunJianPara.checkSupervisionDict)
        checkParam['checkAddress'] = supervisionParam['secretSupervision.checkAddress']  
        #ret = XunJianIntf.check_Supervision(checkParam, orgId=orgInit['DftJieDaoOrgId'],state='3',checkAddress = checkParam['checkAddress'],username=userInit['DftJieDaoUser'], password='11111111')         
        ret = XunJianIntf.check_Supervision(checkParam, orgId=orgInit['DftJieDaoOrgId'],checkAddress = checkParam['checkAddress'],username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(ret, '未检查到待流转督查暗访信息') 
    
    #将待转的巡检记录转事件处理  
        turnIssueParam = copy.deepcopy(XunJianPara.turnIssueObject)
        turnIssueParam['issue.occurOrg.id'] = getSupervisionParam['orgId']
        turnIssueParam['inspectionIds'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from inspection t where t.inspectaddress='%s'" % supervisionParam['secretSupervision.checkAddress'])
        turnIssueParam['dataSource'] = 'inspectionIssue'
        turnIssueParam['issue.subject'] = '督查暗访-%s'% getSupervisionParam['safeProductionEnterprise.name']
        turnIssueParam['selectOrgName'] = orgInit['DftJieDaoOrg']
        turnIssueParam['issue.occurLocation'] = userInit['DftJieDaoUserXM']
        turnIssueParam['issue.occurDate'] = Time.getCurrentDate()
        turnIssueParam['eatHours'] = time.strftime("%I")
        turnIssueParam['eatMinute'] = time.strftime("%M")
        turnIssueParam['selectedTypes'] = '1'  #事件类型   
        turnIssueParam['issueRelatedPeopleNames'] = supervisionParam['secretSupervision.checkLegalPerson']
        turnIssueParam['issueRelatedPeopleTelephones'] = supervisionParam['secretSupervision.mobileNumber']
        turnIssueParam['issue.relatePeopleCount'] = '10'  #人数
        turnIssueParam['issue.issueContent'] = '%s,%s'%(supervisionParam['secretSupervision.findProblems'] ,supervisionParam['secretSupervision.requires'])
        rs = XunJianIntf.turnIssueAcceptCenter(turnIssueParam, username=userInit['DftJieDaoUser'], password='11111111')  
        responseDict = json.loads(rs.text)
        self.assertTrue(rs, '巡检记录转事件失败') 
        
    #查看办理中记录  即：state='5'   
        checkParam = copy.deepcopy(XunJianPara.checkSupervisionDict)
        checkParam['checkAddress'] = supervisionParam['secretSupervision.checkAddress']  
        #ret = XunJianIntf.check_Supervision(checkParam, orgId=orgInit['DftJieDaoOrgId'],state='5',checkAddress = checkParam['checkAddress'],username=userInit['DftJieDaoUser'], password='11111111')         
        ret = XunJianIntf.check_Supervision(checkParam, orgId=orgInit['DftJieDaoOrgId'],checkAddress = checkParam['checkAddress'],username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(ret, '未检查到办理中督查暗访信息') 
 
    #设置结案参数
        sIssuePara=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)        
        sIssuePara['operation.dealOrg.id']=orgInit['DftJieDaoOrgId']
        sIssuePara['operation.issue.id']=responseDict['issueId']
        sIssuePara['keyId']=responseDict['issueStepId']      
        sIssuePara['operation.dealUserName']=userInit['DftJieDaoUserXM']
        sIssuePara['operation.mobile']=userInit['DftJieDaoUserSJ']
        sIssuePara['dealCode']='31' #结案
        sIssuePara['dealTime']=Time.getCurrentDate()
        sIssuePara['operation.content']='事件处理'  
    #事件结案
        result=XunJianIntf.deal_Issue(issueDict=sIssuePara,username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(result.result, '事件操作失败!')
         
        Time.wait(2)
   
    #查看已办结记录  即：state='6'    
        checkParam = copy.deepcopy(XunJianPara.checkSupervisionDict)
        checkParam['checkAddress'] = supervisionParam['secretSupervision.checkAddress']  
        #ret = XunJianIntf.check_Supervision(checkParam, orgId=orgInit['DftJieDaoOrgId'],state='6',username=userInit['DftJieDaoUser'], password='11111111')         
        ret = XunJianIntf.check_Supervision(checkParam, orgId=orgInit['DftJieDaoOrgId'],username=userInit['DftJieDaoUser'], checkAddress = checkParam['checkAddress'] ,password='11111111')
        self.assertTrue(ret, '未检查到已办结的督查暗访信息') 
        pass
      
    
#隐患项备注设置



    def testriskRemarkAdd_19(self):  
        """新增隐患备注项"""
        
    #新增企业隐患项信息
        riskRemarkParam = copy.deepcopy(XunJianPara.riskRemarkObject) 
        riskRemarkParam['riskRemark.riskRemarkName'] = '严重隐患备注项%s'%CommonUtil.createRandomString()
        riskRemarkParam['riskRemark.level.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='隐患等级', displayName='严重')   # 不合格：2014  严重：2015  
        riskRemarkParam['riskRemark.isEnable'] = '1'  #启用-1  禁用-0
        riskRemarkParam['mode'] = 'add'
        riskRemarkParam['riskRemark.riskmarkerType'] = '0'     #企业-0  出租房-1
        riskRemarkParam['riskRemark.orgId.id'] = orgInit['DftJieDaoOrgId']
        riskRemarkParam['isSubmit'] = 'true'  
        responseDict = XunJianIntf.add_riskRemark(riskRemarkParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增隐患项失败')    

    #检查新增的企业隐患项信息 
        checkParam = copy.deepcopy(XunJianPara.checkRiskRemarkDict)
        checkParam['riskRemarkName'] = riskRemarkParam['riskRemark.riskRemarkName']
        checkParam['id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskremarks t where t.riskremarkname='%s'" % (riskRemarkParam['riskRemark.riskRemarkName']))
        ret = XunJianIntf.check_riskRemark(checkParam, orgId=orgInit['DftJieDaoOrgId'],riskmarkerType=riskRemarkParam['riskRemark.riskmarkerType'],username=userInit['DftJieDaoUser'], password='11111111')         
        self.assertTrue(ret, '未检查到企业隐患项信息 ') 
        
    #新增出租房隐患项信息
        newRiskRemarkParam = copy.deepcopy(XunJianPara.riskRemarkObject) 
        newRiskRemarkParam['riskRemark.riskRemarkName'] = '不合格隐患备注项%s'%CommonUtil.createRandomString()
        newRiskRemarkParam['riskRemark.level.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='隐患等级', displayName='不合格')   # 不合格：2014  严重：2015  
        newRiskRemarkParam['riskRemark.isEnable'] = '1'  #启用-1  禁用-0
        newRiskRemarkParam['mode'] = 'add'
        newRiskRemarkParam['riskRemark.riskmarkerType'] = '1'     #企业-0  出租房-1
        newRiskRemarkParam['riskRemark.orgId.id'] = orgInit['DftJieDaoOrgId']
        newRiskRemarkParam['isSubmit'] = 'true'  
        responseDict = XunJianIntf.add_riskRemark(newRiskRemarkParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增隐患项失败')    

    #检查新增的出租房隐患项信息 
        checkParam = copy.deepcopy(XunJianPara.checkRiskRemarkDict)
        checkParam['riskRemarkName'] = newRiskRemarkParam['riskRemark.riskRemarkName']
        checkParam['id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskremarks t where t.riskremarkname='%s'" % (newRiskRemarkParam['riskRemark.riskRemarkName']))
        ret = XunJianIntf.check_riskRemark(checkParam, orgId=orgInit['DftJieDaoOrgId'],riskmarkerType=newRiskRemarkParam['riskRemark.riskmarkerType'],username=userInit['DftJieDaoUser'], password='11111111')         
        self.assertTrue(ret, '未检查到出租房隐患项信息 ') 
        pass
    
    def testriskRemarkEdit_20(self):  
        """隐患备注项信息 修改"""
        
    #新增企业隐患项信息
        riskRemarkParam = copy.deepcopy(XunJianPara.riskRemarkObject) 
        riskRemarkParam['riskRemark.riskRemarkName'] = '严重隐患备注项%s'%CommonUtil.createRandomString()
        riskRemarkParam['riskRemark.level.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='隐患等级', displayName='严重')   # 不合格：2014  严重：2015  
        riskRemarkParam['riskRemark.isEnable'] = '0'   #启用-1  禁用-0
        riskRemarkParam['mode'] = 'add'
        riskRemarkParam['riskRemark.riskmarkerType'] = '0'     #企业-0  出租房-1
        riskRemarkParam['riskRemark.orgId.id'] = orgInit['DftJieDaoOrgId']
        riskRemarkParam['isSubmit'] = 'true'  
        responseDict = XunJianIntf.add_riskRemark(riskRemarkParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增隐患项失败')    
        
    #修改企业隐患项信息
        editRiskRemarkParam = copy.deepcopy(XunJianPara.riskRemarkObject) 
        editRiskRemarkParam['riskRemark.riskRemarkName'] = '修改严重隐患备注项%s'%CommonUtil.createRandomString()
        editRiskRemarkParam['riskRemark.level.id'] = riskRemarkParam['riskRemark.level.id']  
        editRiskRemarkParam['riskRemark.isEnable'] = '1'   #启用-1  禁用-0
        editRiskRemarkParam['mode'] = 'edit'
        editRiskRemarkParam['riskRemark.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskremarks t where t.riskremarkname='%s'" % (riskRemarkParam['riskRemark.riskRemarkName']))
        responseDict = XunJianIntf.edit_riskRemark(editRiskRemarkParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增隐患项失败')

    #检查新增的企业隐患项信息 
        checkParam = copy.deepcopy(XunJianPara.checkRiskRemarkDict)
        checkParam['riskRemarkName'] = editRiskRemarkParam['riskRemark.riskRemarkName']
        checkParam['id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskremarks t where t.riskremarkname='%s'" % (editRiskRemarkParam['riskRemark.riskRemarkName']))
        ret = XunJianIntf.check_riskRemark(checkParam, orgId=orgInit['DftJieDaoOrgId'],riskmarkerType=riskRemarkParam['riskRemark.riskmarkerType'],username=userInit['DftJieDaoUser'], password='11111111')         
        self.assertTrue(ret, '未检查到企业隐患项信息 ') 
        
    #新增出租房隐患项信息
        newRiskRemarkParam = copy.deepcopy(XunJianPara.riskRemarkObject) 
        newRiskRemarkParam['riskRemark.riskRemarkName'] = '不合格隐患备注项%s'%CommonUtil.createRandomString()
        newRiskRemarkParam['riskRemark.level.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='隐患等级', displayName='不合格')   # 不合格：2014  严重：2015  
        newRiskRemarkParam['riskRemark.isEnable'] =  '0'   #启用-1  禁用-0
        newRiskRemarkParam['mode'] = 'add'
        newRiskRemarkParam['riskRemark.riskmarkerType'] = '1'     #企业-0  出租房-1
        newRiskRemarkParam['riskRemark.orgId.id'] = orgInit['DftJieDaoOrgId']
        newRiskRemarkParam['isSubmit'] = 'true'  
        responseDict = XunJianIntf.add_riskRemark(newRiskRemarkParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增隐患项失败')    
         
    #修改出租房隐患项信息
        editNewRiskRemarkParam = copy.deepcopy(XunJianPara.riskRemarkObject) 
        editNewRiskRemarkParam['riskRemark.riskRemarkName'] = '修改不合格隐患备注项%s'%CommonUtil.createRandomString()
        editNewRiskRemarkParam['riskRemark.level.id'] = newRiskRemarkParam['riskRemark.level.id']  
        editNewRiskRemarkParam['riskRemark.isEnable'] = '1'
        editNewRiskRemarkParam['mode'] = 'edit'
        editNewRiskRemarkParam['riskRemark.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskremarks t where t.riskremarkname='%s'" % (newRiskRemarkParam['riskRemark.riskRemarkName']))
        responseDict = XunJianIntf.edit_riskRemark(editNewRiskRemarkParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增隐患项失败')
 
    #检查新增的出租房隐患项信息 
        checkParam = copy.deepcopy(XunJianPara.checkRiskRemarkDict)
        checkParam['riskRemarkName'] = editNewRiskRemarkParam['riskRemark.riskRemarkName']
        checkParam['id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskremarks t where t.riskremarkname='%s'" % (editNewRiskRemarkParam['riskRemark.riskRemarkName']))
        ret = XunJianIntf.check_riskRemark(checkParam, orgId=orgInit['DftJieDaoOrgId'],riskmarkerType=editNewRiskRemarkParam['riskRemark.riskmarkerType'],username=userInit['DftJieDaoUser'], password='11111111')         
        self.assertTrue(ret, '未检查到出租房隐患项信息 ') 
        pass

    def testriskRemarkDelete_21(self):  
        """隐患备注项信息 删除"""
        
    #新增企业隐患项信息
        riskRemarkParam = copy.deepcopy(XunJianPara.riskRemarkObject) 
        riskRemarkParam['riskRemark.riskRemarkName'] = '严重隐患备注项%s'%CommonUtil.createRandomString()
        riskRemarkParam['riskRemark.level.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='隐患等级', displayName='严重')   # 不合格：2014  严重：2015  
        riskRemarkParam['riskRemark.isEnable'] = '1'   #启用-1  禁用-0
        riskRemarkParam['mode'] = 'add'
        riskRemarkParam['riskRemark.riskmarkerType'] = '0'     #企业-0  出租房-1
        riskRemarkParam['riskRemark.orgId.id'] = orgInit['DftJieDaoOrgId']
        riskRemarkParam['isSubmit'] = 'true'  
        responseDict = XunJianIntf.add_riskRemark(riskRemarkParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增隐患项失败') 
        
    #删除企业隐患项信息
        deleteRiskRemarkParam = copy.deepcopy(XunJianPara.deleteRiskRemarkData) 
        deleteRiskRemarkParam['riskRemarkIds'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskremarks t where t.riskremarkname='%s'" % (riskRemarkParam['riskRemark.riskRemarkName']))
        responseDict = XunJianIntf.delete_riskRemark(deleteRiskRemarkParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增隐患项失败')
 
    #检查企业隐患项信息
        checkParam = copy.deepcopy(XunJianPara.checkRiskRemarkDict)
        checkParam['riskRemarkName'] = riskRemarkParam['riskRemark.riskRemarkName']
        checkParam['id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskremarks t where t.riskremarkname='%s'" % (riskRemarkParam['riskRemark.riskRemarkName']))
        ret = XunJianIntf.check_riskRemark(checkParam, orgId=orgInit['DftJieDaoOrgId'],riskmarkerType=riskRemarkParam['riskRemark.riskmarkerType'],username=userInit['DftJieDaoUser'], password='11111111')         
        self.assertFalse(ret, '删除的企业隐患项信息在列表中依然存在，删除失败') 

    #新增出租房隐患项信息
        newRiskRemarkParam = copy.deepcopy(XunJianPara.riskRemarkObject) 
        newRiskRemarkParam['riskRemark.riskRemarkName'] = '不合格隐患备注项%s'%CommonUtil.createRandomString()
        newRiskRemarkParam['riskRemark.level.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='隐患等级', displayName='不合格')   # 不合格：2014  严重：2015  
        newRiskRemarkParam['riskRemark.isEnable'] =  '1'   #启用-1  禁用-0
        newRiskRemarkParam['mode'] = 'add'
        newRiskRemarkParam['riskRemark.riskmarkerType'] = '1'     #企业-0  出租房-1
        newRiskRemarkParam['riskRemark.orgId.id'] = orgInit['DftJieDaoOrgId']
        newRiskRemarkParam['isSubmit'] = 'true'  
        responseDict = XunJianIntf.add_riskRemark(newRiskRemarkParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增隐患项失败')    
         
    #删除出租房隐患项信息
        deleteRiskRemarkParam = copy.deepcopy(XunJianPara.deleteRiskRemarkData) 
        deleteRiskRemarkParam['riskRemarkIds'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskremarks t where t.riskremarkname='%s'" % (newRiskRemarkParam['riskRemark.riskRemarkName']))
        responseDict = XunJianIntf.delete_riskRemark(deleteRiskRemarkParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增隐患项失败')
 
    #检查新增的出租房隐患项信息 
        checkParam = copy.deepcopy(XunJianPara.checkRiskRemarkDict)
        checkParam['riskRemarkName'] = newRiskRemarkParam['riskRemark.riskRemarkName']
        checkParam['id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskremarks t where t.riskremarkname='%s'" % (newRiskRemarkParam['riskRemark.riskRemarkName']))
        ret = XunJianIntf.check_riskRemark(checkParam, orgId=orgInit['DftJieDaoOrgId'],riskmarkerType=newRiskRemarkParam['riskRemark.riskmarkerType'],username=userInit['DftJieDaoUser'], password='11111111')         
        self.assertFalse(ret, '删除的企业隐患项信息在列表中依然存在，删除失败') 
        pass

    def testriskRemarkSearch_22(self):  
        """隐患备注项信息 搜索"""
        
    #新增企业隐患项信息1
        riskRemarkParam_1 = copy.deepcopy(XunJianPara.riskRemarkObject) 
        riskRemarkParam_1['riskRemark.riskRemarkName'] = '不合格隐患备注项%s'%CommonUtil.createRandomString()
        riskRemarkParam_1['riskRemark.level.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='隐患等级', displayName='不合格')   # 不合格：2014  严重：2015  
        riskRemarkParam_1['riskRemark.isEnable'] = '1'   #启用-1  禁用-0
        riskRemarkParam_1['mode'] = 'add'
        riskRemarkParam_1['riskRemark.riskmarkerType'] = '0'     #企业-0  出租房-1
        riskRemarkParam_1['riskRemark.orgId.id'] = orgInit['DftJieDaoOrgId']
        riskRemarkParam_1['isSubmit'] = 'true'  
        responseDict = XunJianIntf.add_riskRemark(riskRemarkParam_1, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增隐患项失败') 
        
    #新增企业隐患项信息2
        riskRemarkParam_2 = copy.deepcopy(XunJianPara.riskRemarkObject) 
        riskRemarkParam_2['riskRemark.riskRemarkName'] = '严重隐患备注项%s'%CommonUtil.createRandomString()
        riskRemarkParam_2['riskRemark.level.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='隐患等级', displayName='严重')   # 不合格：2014  严重：2015  
        riskRemarkParam_2['riskRemark.isEnable'] = '1'   #启用-1  禁用-0
        riskRemarkParam_2['mode'] = 'add'
        riskRemarkParam_2['riskRemark.riskmarkerType'] = '0'     #企业-0  出租房-1
        riskRemarkParam_2['riskRemark.orgId.id'] = orgInit['DftJieDaoOrgId']
        riskRemarkParam_2['isSubmit'] = 'true'  
        responseDict = XunJianIntf.add_riskRemark(riskRemarkParam_2, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增隐患项失败') 
 
    #搜索企业隐患项信息
        searchParam = copy.deepcopy(XunJianPara.checkRiskRemarkDict)
        searchParam['riskRemarkName'] = riskRemarkParam_1['riskRemark.riskRemarkName']
        searchParam['id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskremarks t where t.riskremarkname='%s'" % (riskRemarkParam_1['riskRemark.riskRemarkName']))
        ret = XunJianIntf.search_riskRemark(searchParam, orgId=orgInit['DftJieDaoOrgId'],riskmarkerType=riskRemarkParam_1['riskRemark.riskmarkerType'],riskRemarkName=riskRemarkParam_1['riskRemark.riskRemarkName'],username=userInit['DftJieDaoUser'], password='11111111')         
        self.assertTrue(ret, '搜索失败') 
        
    #搜索不符合条件的企业隐患项信息
        searchParam = copy.deepcopy(XunJianPara.checkRiskRemarkDict)
        ret = XunJianIntf.search_riskRemark(searchParam, orgId=orgInit['DftJieDaoOrgId'],riskmarkerType=riskRemarkParam_1['riskRemark.riskmarkerType'],riskRemarkName='隐患项',username=userInit['DftJieDaoUser'], password='11111111')         
        self.assertFalse(ret, '搜索到不符合条件的隐患项信息，搜素失败') 

    #新增出租房隐患项信息1
        newRiskRemarkParam_1 = copy.deepcopy(XunJianPara.riskRemarkObject) 
        newRiskRemarkParam_1['riskRemark.riskRemarkName'] = '不合格隐患备注项%s'%CommonUtil.createRandomString()
        newRiskRemarkParam_1['riskRemark.level.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='隐患等级', displayName='不合格')   # 不合格：2014  严重：2015  
        newRiskRemarkParam_1['riskRemark.isEnable'] =  '1'   #启用-1  禁用-0
        newRiskRemarkParam_1['mode'] = 'add'
        newRiskRemarkParam_1['riskRemark.riskmarkerType'] = '1'     #企业-0  出租房-1
        newRiskRemarkParam_1['riskRemark.orgId.id'] = orgInit['DftJieDaoOrgId']
        newRiskRemarkParam_1['isSubmit'] = 'true'  
        responseDict = XunJianIntf.add_riskRemark(newRiskRemarkParam_1, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增隐患项失败')    
        
    #新增出租房隐患项信息2
        newRiskRemarkParam_2 = copy.deepcopy(XunJianPara.riskRemarkObject) 
        newRiskRemarkParam_2['riskRemark.riskRemarkName'] = '严格隐患备注项%s'%CommonUtil.createRandomString()
        newRiskRemarkParam_2['riskRemark.level.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='隐患等级', displayName='严格')   # 不合格：2014  严重：2015  
        newRiskRemarkParam_2['riskRemark.isEnable'] =  '1'   #启用-1  禁用-0
        newRiskRemarkParam_2['mode'] = 'add'
        newRiskRemarkParam_2['riskRemark.riskmarkerType'] = '1'     #企业-0  出租房-1
        newRiskRemarkParam_2['riskRemark.orgId.id'] = orgInit['DftJieDaoOrgId']
        newRiskRemarkParam_2['isSubmit'] = 'true'  
        responseDict = XunJianIntf.add_riskRemark(newRiskRemarkParam_2, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增隐患项失败')   
         
    #搜索出租房隐患项信息
        searchParam = copy.deepcopy(XunJianPara.checkRiskRemarkDict)
        searchParam['riskRemarkName'] = newRiskRemarkParam_1['riskRemark.riskRemarkName']
        searchParam['id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskremarks t where t.riskremarkname='%s'" % (newRiskRemarkParam_1['riskRemark.riskRemarkName']))
        ret = XunJianIntf.search_riskRemark(searchParam, orgId=orgInit['DftJieDaoOrgId'],riskmarkerType=newRiskRemarkParam_1['riskRemark.riskmarkerType'],riskRemarkName=newRiskRemarkParam_1['riskRemark.riskRemarkName'],username=userInit['DftJieDaoUser'], password='11111111')         
        self.assertTrue(ret, '搜索失败') 

    #搜索不符合条件的出租房隐患项信息
        searchParam = copy.deepcopy(XunJianPara.checkRiskRemarkDict)
        ret = XunJianIntf.search_riskRemark(searchParam, orgId=orgInit['DftJieDaoOrgId'],riskmarkerType=riskRemarkParam_1['riskRemark.riskmarkerType'],riskRemarkName='隐患项',username=userInit['DftJieDaoUser'], password='11111111')         
        self.assertFalse(ret, '搜索到不符合条件的隐患项信息，搜素失败')         
        pass

    def testriskRemarkMove_23(self):  
        """隐患备注项信息 上移/下移"""

    #新增企业隐患项信息1
        riskRemarkParam_1 = copy.deepcopy(XunJianPara.riskRemarkObject) 
        riskRemarkParam_1['riskRemark.riskRemarkName'] = '1不合格隐患备注项%s'%CommonUtil.createRandomString()
        riskRemarkParam_1['riskRemark.level.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='隐患等级', displayName='不合格')   # 不合格：2014  严重：2015  
        riskRemarkParam_1['riskRemark.isEnable'] = '1'   #启用-1  禁用-0
        riskRemarkParam_1['mode'] = 'add'
        riskRemarkParam_1['riskRemark.riskmarkerType'] = '0'     #企业-0  出租房-1
        riskRemarkParam_1['riskRemark.orgId.id'] = orgInit['DftJieDaoOrgId']
        riskRemarkParam_1['isSubmit'] = 'true'  
        responseDict = XunJianIntf.add_riskRemark(riskRemarkParam_1, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增隐患项失败') 
        
    #新增企业隐患项信息2
        riskRemarkParam_2 = copy.deepcopy(XunJianPara.riskRemarkObject) 
        riskRemarkParam_2['riskRemark.riskRemarkName'] = '2严重隐患备注项%s'%CommonUtil.createRandomString()
        riskRemarkParam_2['riskRemark.level.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='隐患等级', displayName='严重')   # 不合格：2014  严重：2015  
        riskRemarkParam_2['riskRemark.isEnable'] = '1'   #启用-1  禁用-0
        riskRemarkParam_2['mode'] = 'add'
        riskRemarkParam_2['riskRemark.riskmarkerType'] = '0'     #企业-0  出租房-1
        riskRemarkParam_2['riskRemark.orgId.id'] = orgInit['DftJieDaoOrgId']
        riskRemarkParam_2['isSubmit'] = 'true'  
        responseDict = XunJianIntf.add_riskRemark(riskRemarkParam_2, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增隐患项失败') 
        
    #将企业隐患项信息2上移
        toPreviousParam = copy.deepcopy(XunJianPara.checkRiskRemarkDict)
        toPreviousParam['riskRemark.riskmarkerType'] = riskRemarkParam_2['riskRemark.riskmarkerType']
        toPreviousParam['mode'] = 'toPrevious'
        toPreviousParam['riskRemark.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskremarks t where t.riskremarkname='%s'" % (riskRemarkParam_2['riskRemark.riskRemarkName']))
        toPreviousParam['riskRemark.indexId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.indexId from riskremarks t where t.riskremarkname='%s'" % (riskRemarkParam_2['riskRemark.riskRemarkName']))  #该隐患项在列表中的排序
        toPreviousParam['count'] = '2'  #当前列表下隐患项条数
        ret = XunJianIntf.move_riskRemark(toPreviousParam,username=userInit['DftJieDaoUser'], password='11111111')         
        self.assertTrue(ret, '上移失败') 

    #检查企业隐患项信息2是否上移成功
        checkParam = copy.deepcopy(XunJianPara.checkRiskRemarkDict)
        checkParam['riskRemarkName'] = riskRemarkParam_2['riskRemark.riskRemarkName']
        checkParam['indexId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.indexId from riskremarks t where t.riskremarkname='%s'" % (riskRemarkParam_2['riskRemark.riskRemarkName']))
        ret = XunJianIntf.check_riskRemark(checkParam, orgId=orgInit['DftJieDaoOrgId'],riskmarkerType=riskRemarkParam_2['riskRemark.riskmarkerType'],username=userInit['DftJieDaoUser'], password='11111111')         
        self.assertTrue(ret, '未检查到企业隐患项信息 ')  
        
    #将企业隐患项信息2下移
        toNextParam = copy.deepcopy(XunJianPara.checkRiskRemarkDict)
        toNextParam['riskRemark.riskmarkerType'] = riskRemarkParam_2['riskRemark.riskmarkerType']
        toNextParam['mode'] = 'toNext'
        toNextParam['riskRemark.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskremarks t where t.riskremarkname='%s'" % (riskRemarkParam_2['riskRemark.riskRemarkName']))
        toNextParam['riskRemark.indexId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.indexId from riskremarks t where t.riskremarkname='%s'" % (riskRemarkParam_2['riskRemark.riskRemarkName']))  #该隐患项在列表中的排序
        toNextParam['count'] = '2'  #当前列表下隐患项条数
        ret = XunJianIntf.move_riskRemark(toNextParam,username=userInit['DftJieDaoUser'], password='11111111')         
        self.assertTrue(ret, '下移失败') 

    #检查企业隐患项信息2是否下移成功
        checkParam = copy.deepcopy(XunJianPara.checkRiskRemarkDict)
        checkParam['riskRemarkName'] = riskRemarkParam_2['riskRemark.riskRemarkName']
        checkParam['indexId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.indexId from riskremarks t where t.riskremarkname='%s'" % (riskRemarkParam_2['riskRemark.riskRemarkName']))
        ret = XunJianIntf.check_riskRemark(checkParam, orgId=orgInit['DftJieDaoOrgId'],riskmarkerType=riskRemarkParam_2['riskRemark.riskmarkerType'],username=userInit['DftJieDaoUser'], password='11111111')         
        self.assertTrue(ret, '未检查到企业隐患项信息 ')  
        
    #新增出租房隐患项信息1
        newRiskRemarkParam_1 = copy.deepcopy(XunJianPara.riskRemarkObject) 
        newRiskRemarkParam_1['riskRemark.riskRemarkName'] = '不合格隐患备注项%s'%CommonUtil.createRandomString()
        newRiskRemarkParam_1['riskRemark.level.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='隐患等级', displayName='不合格')   # 不合格：2014  严重：2015  
        newRiskRemarkParam_1['riskRemark.isEnable'] =  '1'   #启用-1  禁用-0
        newRiskRemarkParam_1['mode'] = 'add'
        newRiskRemarkParam_1['riskRemark.riskmarkerType'] = '1'     #企业-0  出租房-1
        newRiskRemarkParam_1['riskRemark.orgId.id'] = orgInit['DftJieDaoOrgId']
        newRiskRemarkParam_1['isSubmit'] = 'true'  
        responseDict = XunJianIntf.add_riskRemark(newRiskRemarkParam_1, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增隐患项失败')    
        
    #新增出租房隐患项信息2
        newRiskRemarkParam_2 = copy.deepcopy(XunJianPara.riskRemarkObject) 
        newRiskRemarkParam_2['riskRemark.riskRemarkName'] = '严格隐患备注项%s'%CommonUtil.createRandomString()
        newRiskRemarkParam_2['riskRemark.level.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='隐患等级', displayName='严格')   # 不合格：2014  严重：2015  
        newRiskRemarkParam_2['riskRemark.isEnable'] =  '1'   #启用-1  禁用-0
        newRiskRemarkParam_2['mode'] = 'add'
        newRiskRemarkParam_2['riskRemark.riskmarkerType'] = '1'     #企业-0  出租房-1
        newRiskRemarkParam_2['riskRemark.orgId.id'] = orgInit['DftJieDaoOrgId']
        newRiskRemarkParam_2['isSubmit'] = 'true'  
        responseDict = XunJianIntf.add_riskRemark(newRiskRemarkParam_2, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增隐患项失败')   

    #将出租房隐患项信息2上移
        toPreviousParam = copy.deepcopy(XunJianPara.checkRiskRemarkDict)
        toPreviousParam['riskRemark.riskmarkerType'] = riskRemarkParam_2['riskRemark.riskmarkerType']
        toPreviousParam['mode'] = 'toPrevious'
        toPreviousParam['riskRemark.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskremarks t where t.riskremarkname='%s'" % (newRiskRemarkParam_2['riskRemark.riskRemarkName']))
        toPreviousParam['riskRemark.indexId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.indexId from riskremarks t where t.riskremarkname='%s'" % (newRiskRemarkParam_2['riskRemark.riskRemarkName']))  #该隐患项在列表中的排序
        toPreviousParam['count'] = '2'  #当前列表下隐患项条数
        ret = XunJianIntf.move_riskRemark(toPreviousParam,username=userInit['DftJieDaoUser'], password='11111111')         
        self.assertTrue(ret, '上移失败') 

    #检查出租房隐患项信息2是否上移成功
        checkParam = copy.deepcopy(XunJianPara.checkRiskRemarkDict)
        checkParam['riskRemarkName'] = newRiskRemarkParam_2['riskRemark.riskRemarkName']
        checkParam['indexId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.indexId from riskremarks t where t.riskremarkname='%s'" % (newRiskRemarkParam_2['riskRemark.riskRemarkName']))
        ret = XunJianIntf.check_riskRemark(checkParam, orgId=orgInit['DftJieDaoOrgId'],riskmarkerType=newRiskRemarkParam_2['riskRemark.riskmarkerType'],username=userInit['DftJieDaoUser'], password='11111111')         
        self.assertTrue(ret, '未检查到出租房隐患项信息 ')  

    #将出租房隐患项信息2下移
        toNextParam = copy.deepcopy(XunJianPara.checkRiskRemarkDict)
        toNextParam['riskRemark.riskmarkerType'] = riskRemarkParam_2['riskRemark.riskmarkerType']
        toNextParam['mode'] = 'toNext'
        toNextParam['riskRemark.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskremarks t where t.riskremarkname='%s'" % (newRiskRemarkParam_2['riskRemark.riskRemarkName']))
        toNextParam['riskRemark.indexId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.indexId from riskremarks t where t.riskremarkname='%s'" % (newRiskRemarkParam_2['riskRemark.riskRemarkName']))  #该隐患项在列表中的排序
        toNextParam['count'] = '2'  #当前列表下隐患项条数
        ret = XunJianIntf.move_riskRemark(toNextParam,username=userInit['DftJieDaoUser'], password='11111111')         
        self.assertTrue(ret, '下移失败') 

    #检查出租房隐患项信息2是否下移成功
        checkParam = copy.deepcopy(XunJianPara.checkRiskRemarkDict)
        checkParam['riskRemarkName'] = newRiskRemarkParam_2['riskRemark.riskRemarkName']
        checkParam['indexId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.indexId from riskremarks t where t.riskremarkname='%s'" % (newRiskRemarkParam_2['riskRemark.riskRemarkName']))
        ret = XunJianIntf.check_riskRemark(checkParam, orgId=orgInit['DftJieDaoOrgId'],riskmarkerType=newRiskRemarkParam_2['riskRemark.riskmarkerType'],username=userInit['DftJieDaoUser'], password='11111111')         
        self.assertTrue(ret, '未检查到出租房隐患项信息 ')  

    def testriskRemarkMove_24(self):  
        """隐患备注项信息 置顶"""
    #新增企业隐患项信息1
        riskRemarkParam_1 = copy.deepcopy(XunJianPara.riskRemarkObject) 
        riskRemarkParam_1['riskRemark.riskRemarkName'] = '1不合格隐患备注项%s'%CommonUtil.createRandomString()
        riskRemarkParam_1['riskRemark.level.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='隐患等级', displayName='不合格')   # 不合格：2014  严重：2015  
        riskRemarkParam_1['riskRemark.isEnable'] = '1'   #启用-1  禁用-0
        riskRemarkParam_1['mode'] = 'add'
        riskRemarkParam_1['riskRemark.riskmarkerType'] = '0'     #企业-0  出租房-1
        riskRemarkParam_1['riskRemark.orgId.id'] = orgInit['DftJieDaoOrgId']
        riskRemarkParam_1['isSubmit'] = 'true'  
        responseDict = XunJianIntf.add_riskRemark(riskRemarkParam_1, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增隐患项失败') 
        
    #新增企业隐患项信息2
        riskRemarkParam_2 = copy.deepcopy(XunJianPara.riskRemarkObject) 
        riskRemarkParam_2['riskRemark.riskRemarkName'] = '2严重隐患备注项%s'%CommonUtil.createRandomString()
        riskRemarkParam_2['riskRemark.level.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='隐患等级', displayName='严重')   # 不合格：2014  严重：2015  
        riskRemarkParam_2['riskRemark.isEnable'] = '1'   #启用-1  禁用-0
        riskRemarkParam_2['mode'] = 'add'
        riskRemarkParam_2['riskRemark.riskmarkerType'] = '0'     #企业-0  出租房-1
        riskRemarkParam_2['riskRemark.orgId.id'] = orgInit['DftJieDaoOrgId']
        riskRemarkParam_2['isSubmit'] = 'true'  
        responseDict = XunJianIntf.add_riskRemark(riskRemarkParam_2, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增隐患项失败') 
        
    #将企业隐患项信息2置顶
        toFirstParam = copy.deepcopy(XunJianPara.checkRiskRemarkDict)
        toFirstParam['riskRemark.riskmarkerType'] = riskRemarkParam_2['riskRemark.riskmarkerType']
        toFirstParam['mode'] = 'toFirst'
        toFirstParam['riskRemark.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskremarks t where t.riskremarkname='%s'" % (riskRemarkParam_2['riskRemark.riskRemarkName']))
        toFirstParam['riskRemark.indexId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.indexId from riskremarks t where t.riskremarkname='%s'" % (riskRemarkParam_2['riskRemark.riskRemarkName']))  #该隐患项在列表中的排序
        toFirstParam['count'] = '2'  #当前列表下隐患项条数
        ret = XunJianIntf.move_riskRemark(toFirstParam,username=userInit['DftJieDaoUser'], password='11111111')         
        self.assertTrue(ret, '置顶失败') 

    #检查企业隐患项信息2是否置顶成功
        checkParam = copy.deepcopy(XunJianPara.checkRiskRemarkDict)
        checkParam['riskRemarkName'] = riskRemarkParam_2['riskRemark.riskRemarkName']
        checkParam['indexId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.indexId from riskremarks t where t.riskremarkname='%s'" % (riskRemarkParam_2['riskRemark.riskRemarkName']))
        ret = XunJianIntf.check_riskRemark(checkParam, orgId=orgInit['DftJieDaoOrgId'],riskmarkerType=riskRemarkParam_2['riskRemark.riskmarkerType'],username=userInit['DftJieDaoUser'], password='11111111')         
        self.assertTrue(ret, '未检查到企业隐患项信息 ')  
 
        
    #新增出租房隐患项信息1
        newRiskRemarkParam_1 = copy.deepcopy(XunJianPara.riskRemarkObject) 
        newRiskRemarkParam_1['riskRemark.riskRemarkName'] = '不合格隐患备注项%s'%CommonUtil.createRandomString()
        newRiskRemarkParam_1['riskRemark.level.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='隐患等级', displayName='不合格')   # 不合格：2014  严重：2015  
        newRiskRemarkParam_1['riskRemark.isEnable'] =  '1'   #启用-1  禁用-0
        newRiskRemarkParam_1['mode'] = 'add'
        newRiskRemarkParam_1['riskRemark.riskmarkerType'] = '1'     #企业-0  出租房-1
        newRiskRemarkParam_1['riskRemark.orgId.id'] = orgInit['DftJieDaoOrgId']
        newRiskRemarkParam_1['isSubmit'] = 'true'  
        responseDict = XunJianIntf.add_riskRemark(newRiskRemarkParam_1, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增隐患项失败')    
        
    #新增出租房隐患项信息2
        newRiskRemarkParam_2 = copy.deepcopy(XunJianPara.riskRemarkObject) 
        newRiskRemarkParam_2['riskRemark.riskRemarkName'] = '严格隐患备注项%s'%CommonUtil.createRandomString()
        newRiskRemarkParam_2['riskRemark.level.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='隐患等级', displayName='严格')   # 不合格：2014  严重：2015  
        newRiskRemarkParam_2['riskRemark.isEnable'] =  '1'   #启用-1  禁用-0
        newRiskRemarkParam_2['mode'] = 'add'
        newRiskRemarkParam_2['riskRemark.riskmarkerType'] = '1'     #企业-0  出租房-1
        newRiskRemarkParam_2['riskRemark.orgId.id'] = orgInit['DftJieDaoOrgId']
        newRiskRemarkParam_2['isSubmit'] = 'true'  
        responseDict = XunJianIntf.add_riskRemark(newRiskRemarkParam_2, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增隐患项失败')   

    #将出租房隐患项信息2置顶
        toFirstParam = copy.deepcopy(XunJianPara.checkRiskRemarkDict)
        toFirstParam['riskRemark.riskmarkerType'] = riskRemarkParam_2['riskRemark.riskmarkerType']
        toFirstParam['mode'] = 'toFirst'
        toFirstParam['riskRemark.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskremarks t where t.riskremarkname='%s'" % (newRiskRemarkParam_2['riskRemark.riskRemarkName']))
        toFirstParam['riskRemark.indexId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.indexId from riskremarks t where t.riskremarkname='%s'" % (newRiskRemarkParam_2['riskRemark.riskRemarkName']))  #该隐患项在列表中的排序
        toFirstParam['count'] = '2'  #当前列表下隐患项条数
        ret = XunJianIntf.move_riskRemark(toFirstParam,username=userInit['DftJieDaoUser'], password='11111111')         
        self.assertTrue(ret, '置顶失败') 

    #检查出租房隐患项信息2是否置顶成功
        checkParam = copy.deepcopy(XunJianPara.checkRiskRemarkDict)
        checkParam['riskRemarkName'] = newRiskRemarkParam_2['riskRemark.riskRemarkName']
        checkParam['indexId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.indexId from riskremarks t where t.riskremarkname='%s'" % (newRiskRemarkParam_2['riskRemark.riskRemarkName']))
        ret = XunJianIntf.check_riskRemark(checkParam, orgId=orgInit['DftJieDaoOrgId'],riskmarkerType=newRiskRemarkParam_2['riskRemark.riskmarkerType'],username=userInit['DftJieDaoUser'], password='11111111')         
        self.assertTrue(ret, '未检查到出租房隐患项信息 ')  
        pass




#出租房信息



    def testRentalAdd_25(self):
        """出租房 新增"""
    #新增出租信息
        rentalParam = copy.deepcopy(XunJianPara.rentalObject) 
        rentalParam['mode'] = 'add'
        rentalParam['ownerOrg.id'] = orgInit['DftWangGeOrgId']
        rentalParam['orgName'] = orgInit['DftWangGeOrg']
        rentalParam['rental.name'] = '出租房名称%s'%CommonUtil.createRandomString()
        rentalParam['rental.address'] = '出租房地址%s'%CommonUtil.createRandomString()
        rentalParam['rental.owner'] = '出租人姓名%s'%CommonUtil.createRandomString()     
        rentalParam['rental.ownerPhone'] = '11111111111'
        rentalParam['rental.rentalType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='出租房类型', displayName='居住出租房')
        rentalParam['rental.rentalFloor'] = '3'
        rentalParam['rental.rentalArea'] = '100'
        rentalParam['rental.rentalStructure.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='出租房结构', displayName='钢结构')
        rentalParam['rental.rentedNumber'] = '3'
        rentalParam['rental.police'] = '派出所负责民警%s'%CommonUtil.createRandomString()
        rentalParam['rental.isStop'] = 'false'  #是否停租
        rentalParam['rental.dangerSituation'] = '隐患情况%s'%CommonUtil.createRandomString()  
        rentalParam['rental.gridPerson'] = '%s-%s'%( CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.username= '%s' " % userInit['DftWangGeUser1']),orgInit['DftWangGeOrg1'])

        #验证所属网格必填
        rentalParam['ownerOrg.id']  =''
        responseDict = XunJianIntf.add_rental(rentalParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertFalse(responseDict.result, '新增出租房所属网格必填项为空仍能新增，验证失败') 
        Log.LogOutput(LogLevel.DEBUG, "新增出租房所属网格必填项不能为空")
        rentalParam['ownerOrg.id'] = orgInit['DftWangGeOrgId']
        
        #验证出租房名称必填
        rentalParam['rental.name'] =''
        responseDict = XunJianIntf.add_rental(rentalParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertFalse(responseDict.result, '新增出租房出租房名称必填项为空仍能新增，验证失败') 
        Log.LogOutput(LogLevel.DEBUG, "新增出租房出租房名称必填项不能为空")
        rentalParam['rental.name'] = '出租房名称%s'%CommonUtil.createRandomString()
        
        #验证出租房地址必填
        rentalParam['rental.address'] =''
        responseDict = XunJianIntf.add_rental(rentalParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertFalse(responseDict.result, '新增企业企业地址必填项为空仍能新增，验证失败') 
        Log.LogOutput(LogLevel.DEBUG, "新增企业企业地址必填项不能为空")
        rentalParam['rental.address'] = '出租房地址%s'%CommonUtil.createRandomString()
        
        #验证出租人姓名必填
        rentalParam['rental.owner'] =''
        responseDict = XunJianIntf.add_rental(rentalParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertFalse(responseDict.result, '新增出租房出租人姓名必填项为空仍能新增，验证失败') 
        Log.LogOutput(LogLevel.DEBUG, "新增出租房出租人姓名必填项不能为空")
        rentalParam['rental.owner'] = '出租人姓名%s'%CommonUtil.createRandomString()    
    
        #验证出租房类型必填
        rentalParam['rental.rentalType.id'] =''
        responseDict = XunJianIntf.add_rental(rentalParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertFalse(responseDict.result, '新增出租房出租房类型必填项为空仍能新增，验证失败') 
        Log.LogOutput(LogLevel.DEBUG, "新增出租房出租房类型必填项不能为空")
        rentalParam['rental.rentalType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='出租房类型', displayName='居住出租房') 

        #验证出租人电话必填
        rentalParam['rental.ownerPhone'] =''
        responseDict = XunJianIntf.add_rental(rentalParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertFalse(responseDict.result, '新增出租房出租人电话必填项为空仍能新增，验证失败') 
        Log.LogOutput(LogLevel.DEBUG, "新增出租房出租人电话必填项不能为空")
        rentalParam['rental.ownerPhone'] = '11111111111' 
  
#         #验证所属责任人必填
#         rentalParam['rental.gridPerson'] =''
#         responseDict = XunJianIntf.add_rental(rentalParam, username=userInit['DftWangGeUser'], password='11111111')
#         self.assertFalse(responseDict.result, '新增出租房所属责任人必填项为空仍能新增，验证失败') 
#         Log.LogOutput(LogLevel.DEBUG, "新增出租房所属责任人必填项不能为空")
#         rentalParam['rental.gridPerson'] = '%s-%s'%( CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.username= '%s' " % userInit['DftWangGeUser1']),orgInit['DftWangGeOrg1'])
         
        responseDict = XunJianIntf.add_rental(rentalParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增出租房失败') 
        
    #检查新增的出租房信息  
        checkParam = copy.deepcopy(XunJianPara.checkRentalDict)
        checkParam['name'] = rentalParam['rental.name']   
        ret = XunJianIntf.check_rental(checkParam, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '未检查到出租房信息') 
        pass

    def testRentalEdit_26(self):
        """出租房 修改"""
    #新增出租信息
        rentalParam = copy.deepcopy(XunJianPara.rentalObject) 
        rentalParam['mode'] = 'add'
        rentalParam['ownerOrg.id'] = orgInit['DftWangGeOrgId']
        rentalParam['orgName'] = orgInit['DftWangGeOrg']
        rentalParam['rental.name'] = '出租房名称%s'%CommonUtil.createRandomString()
        rentalParam['rental.address'] = '出租房地址%s'%CommonUtil.createRandomString()
        rentalParam['rental.owner'] = '出租人姓名%s'%CommonUtil.createRandomString()     
        rentalParam['rental.ownerPhone'] = '11111111111'
        rentalParam['rental.rentalType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='出租房类型', displayName='居住出租房')
        rentalParam['rental.rentalFloor'] = '3'
        rentalParam['rental.rentalArea'] = '100'
        rentalParam['rental.rentalStructure.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='出租房结构', displayName='钢结构')
        rentalParam['rental.rentedNumber'] = '3'
        rentalParam['rental.police'] = '派出所负责民警%s'%CommonUtil.createRandomString()
        rentalParam['rental.isStop'] = 'false'  #是否停租
        rentalParam['rental.dangerSituation'] = '隐患情况%s'%CommonUtil.createRandomString()  
        rentalParam['rental.gridPerson'] = '%s-%s'%( CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.username= '%s' " % userInit['DftWangGeUser1']),orgInit['DftWangGeOrg1'])
        responseDict = XunJianIntf.add_rental(rentalParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增出租房失败') 
        
    #修改出租信息
        editRentalParam = copy.deepcopy(XunJianPara.rentalObject) 
        editRentalParam['mode'] = 'edit'
        editRentalParam['ownerOrg.id'] = rentalParam['ownerOrg.id']
        editRentalParam['rental.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rental t where t.name='%s'" % rentalParam['rental.name'])
        editRentalParam['orgName'] = orgInit['DftWangGeOrg']
        editRentalParam['rental.name'] = '修改出租房名称%s'%CommonUtil.createRandomString()
        editRentalParam['rental.address'] = '修改出租房地址%s'%CommonUtil.createRandomString()
        editRentalParam['rental.owner'] = '修改出租人姓名%s'%CommonUtil.createRandomString()     
        editRentalParam['rental.ownerPhone'] = rentalParam['rental.ownerPhone']
        editRentalParam['rental.rentalType.id'] = rentalParam['rental.rentalType.id']
        editRentalParam['rental.rentalFloor'] = rentalParam['rental.rentalFloor']
        editRentalParam['rental.rentalArea'] = rentalParam['rental.rentalArea']
        editRentalParam['rental.rentalStructure.id'] = rentalParam['rental.rentalStructure.id']
        editRentalParam['rental.rentedNumber'] = rentalParam['rental.rentedNumber']
        editRentalParam['rental.police'] = rentalParam['rental.police']
        editRentalParam['rental.isStop'] = rentalParam['rental.isStop']
        editRentalParam['rental.dangerSituation'] = rentalParam['rental.dangerSituation']  
        editRentalParam['rental.gridPerson'] = rentalParam['rental.gridPerson']
        responseDict = XunJianIntf.edit_rental(editRentalParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改出租房失败') 
        
    #检查出租房信息  
        checkParam = copy.deepcopy(XunJianPara.checkRentalDict)
        checkParam['name'] = editRentalParam['rental.name']   
        ret = XunJianIntf.check_rental(checkParam, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '未检查到出租房信息') 
        pass

    def testRentalDelete_27(self):
        """出租房 删除"""
    #新增出租信息1
        rentalParam = copy.deepcopy(XunJianPara.rentalObject) 
        rentalParam['mode'] = 'add'
        rentalParam['ownerOrg.id'] = orgInit['DftWangGeOrgId']
        rentalParam['orgName'] = orgInit['DftWangGeOrg']
        rentalParam['rental.name'] = '出租房名称%s'%CommonUtil.createRandomString()
        rentalParam['rental.address'] = '出租房地址%s'%CommonUtil.createRandomString()
        rentalParam['rental.owner'] = '出租人姓名%s'%CommonUtil.createRandomString()     
        rentalParam['rental.ownerPhone'] = '11111111111'
        rentalParam['rental.rentalType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='出租房类型', displayName='居住出租房')
        rentalParam['rental.rentalFloor'] = '3'
        rentalParam['rental.rentalArea'] = '100'
        rentalParam['rental.rentalStructure.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='出租房结构', displayName='钢结构')
        rentalParam['rental.rentedNumber'] = '3'
        rentalParam['rental.police'] = '派出所负责民警%s'%CommonUtil.createRandomString()
        rentalParam['rental.isStop'] = 'false'  #是否停租
        rentalParam['rental.dangerSituation'] = '隐患情况%s'%CommonUtil.createRandomString()  
        rentalParam['rental.gridPerson'] = '%s-%s'%( CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.username= '%s' " % userInit['DftWangGeUser1']),orgInit['DftWangGeOrg1'])
        responseDict = XunJianIntf.add_rental(rentalParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增出租房失败') 
        
    #新增出租信息2
        newRentalParam = copy.deepcopy(XunJianPara.rentalObject) 
        newRentalParam['mode'] = 'add'
        newRentalParam['ownerOrg.id'] = orgInit['DftWangGeOrgId']
        newRentalParam['orgName'] = orgInit['DftWangGeOrg']
        newRentalParam['rental.name'] = '出租房名称%s'%CommonUtil.createRandomString()
        newRentalParam['rental.address'] = '出租房地址%s'%CommonUtil.createRandomString()
        newRentalParam['rental.owner'] = '出租人姓名%s'%CommonUtil.createRandomString()     
        newRentalParam['rental.ownerPhone'] = '11111111111'
        newRentalParam['rental.rentalType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='出租房类型', displayName='居住出租房')
        newRentalParam['rental.rentalFloor'] = '3'
        newRentalParam['rental.rentalArea'] = '100'
        newRentalParam['rental.rentalStructure.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='出租房结构', displayName='钢结构')
        newRentalParam['rental.rentedNumber'] = '3'
        newRentalParam['rental.police'] = '派出所负责民警%s'%CommonUtil.createRandomString()
        newRentalParam['rental.isStop'] = 'false'  #是否停租
        newRentalParam['rental.dangerSituation'] = '隐患情况%s'%CommonUtil.createRandomString()  
        newRentalParam['rental.gridPerson'] = '%s-%s'%( CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.username= '%s' " % userInit['DftWangGeUser1']),orgInit['DftWangGeOrg1'])
        responseDict = XunJianIntf.add_rental(newRentalParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增出租房失败') 

    #删除出租房信息  
        deleteParam = copy.deepcopy(XunJianPara.deleteRentalDict)
        deleteParam['selectIds'] = '%s,%s'%(CommonIntf.getDbQueryResult(dbCommand = "select t.id from rental t where t.name='%s'" % rentalParam['rental.name']),CommonIntf.getDbQueryResult(dbCommand = "select t.id from rental t where t.name='%s'" % newRentalParam['rental.name'])) 
        ret = XunJianIntf.delete_rental(deleteParam, username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '未搜索到出租房信息') 
        
    #检查删除后的企业信息 不存在
        checkParam = copy.deepcopy(XunJianPara.checkRentalDict)
        checkParam['name'] = rentalParam['rental.name']   
        ret = XunJianIntf.check_rental(checkParam, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '被删除的企业信息1在列表中依然存在，删除失败') 
        
        checkParam['name'] = newRentalParam['rental.name']   
        ret = XunJianIntf.check_rental(checkParam, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '被删除的企业信息1在列表中依然存在，删除失败')
        
        pass

    def testRentalSearch_28(self):
        """出租房 搜索"""
    #新增出租信息1
        rentalParam = copy.deepcopy(XunJianPara.rentalObject) 
        rentalParam['mode'] = 'add'
        rentalParam['ownerOrg.id'] = orgInit['DftWangGeOrgId']
        rentalParam['orgName'] = orgInit['DftWangGeOrg']
        rentalParam['rental.name'] = '出租房名称%s'%CommonUtil.createRandomString()
        rentalParam['rental.address'] = '出租房地址%s'%CommonUtil.createRandomString()
        rentalParam['rental.owner'] = '出租人姓名%s'%CommonUtil.createRandomString()     
        rentalParam['rental.ownerPhone'] = '11111111111'
        rentalParam['rental.rentalType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='出租房类型', displayName='居住出租房')
        rentalParam['rental.rentalFloor'] = '3'
        rentalParam['rental.rentalArea'] = '100'
        rentalParam['rental.rentalStructure.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='出租房结构', displayName='钢结构')
        rentalParam['rental.rentedNumber'] = '3'
        rentalParam['rental.police'] = '派出所负责民警%s'%CommonUtil.createRandomString()
        rentalParam['rental.isStop'] = 'false'  #是否停租
        rentalParam['rental.dangerSituation'] = '隐患情况%s'%CommonUtil.createRandomString()  
        rentalParam['rental.gridPerson'] = '%s-%s'%( CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.username= '%s' " % userInit['DftWangGeUser1']),orgInit['DftWangGeOrg1'])
        responseDict = XunJianIntf.add_rental(rentalParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增出租房失败') 
        
    #新增出租信息2
        rentalParam_2 = copy.deepcopy(XunJianPara.rentalObject) 
        rentalParam_2['mode'] = 'add'
        rentalParam_2['ownerOrg.id'] = orgInit['DftWangGeOrgId']
        rentalParam_2['orgName'] = orgInit['DftWangGeOrg']
        rentalParam_2['rental.name'] = '出租房名称%s'%CommonUtil.createRandomString()
        rentalParam_2['rental.address'] = '出租房地址%s'%CommonUtil.createRandomString()
        rentalParam_2['rental.owner'] = '出租人姓名%s'%CommonUtil.createRandomString()     
        rentalParam_2['rental.ownerPhone'] = '11111111111'
        rentalParam_2['rental.rentalType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='出租房类型', displayName='居住出租房')
        rentalParam_2['rental.rentalFloor'] = '3'
        rentalParam_2['rental.rentalArea'] = '100'
        rentalParam_2['rental.rentalStructure.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='出租房结构', displayName='钢结构')
        rentalParam_2['rental.rentedNumber'] = '3'
        rentalParam_2['rental.police'] = '派出所负责民警%s'%CommonUtil.createRandomString()
        rentalParam_2['rental.isStop'] = 'false'  #是否停租
        rentalParam_2['rental.dangerSituation'] = '隐患情况%s'%CommonUtil.createRandomString()  
        rentalParam_2['rental.gridPerson'] = '%s-%s'%( CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.username= '%s' " % userInit['DftWangGeUser1']),orgInit['DftWangGeOrg1'])
        responseDict = XunJianIntf.add_rental(rentalParam_2, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增出租房失败') 
        
    #新增出租信息3
        rentalParam_3 = copy.deepcopy(XunJianPara.rentalObject) 
        rentalParam_3['mode'] = 'add'
        rentalParam_3['ownerOrg.id'] = orgInit['DftWangGeOrgId']
        rentalParam_3['orgName'] = orgInit['DftWangGeOrg']
        rentalParam_3['rental.name'] = '出租房名称%s'%CommonUtil.createRandomString()
        rentalParam_3['rental.address'] = '出租房地址%s'%CommonUtil.createRandomString()
        rentalParam_3['rental.owner'] = '出租人姓名%s'%CommonUtil.createRandomString()     
        rentalParam_3['rental.ownerPhone'] = '11111111111'
        rentalParam_3['rental.rentalType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='出租房类型', displayName='居住出租房')
        rentalParam_3['rental.rentalFloor'] = '3'
        rentalParam_3['rental.rentalArea'] = '100'
        rentalParam_3['rental.rentalStructure.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='出租房结构', displayName='钢结构')
        rentalParam_3['rental.rentedNumber'] = '3'
        rentalParam_3['rental.police'] = '派出所负责民警%s'%CommonUtil.createRandomString()
        rentalParam_3['rental.isStop'] = 'true'  #是否停租
        rentalParam_3['rental.dangerSituation'] = '隐患情况%s'%CommonUtil.createRandomString()  
        rentalParam_3['rental.gridPerson'] = '%s-%s'%( CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.username= '%s' " % userInit['DftWangGeUser1']),orgInit['DftWangGeOrg1'])
        responseDict = XunJianIntf.add_rental(rentalParam_3, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增出租房失败') 

    #搜索出租房信息1   
        ret = XunJianIntf.fastSearch_rental(orgId=orgInit['DftWangGeOrgId'],fastSearchKeyWords=rentalParam['rental.name'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '未搜索到企业信息') 
        
    #搜索不符合条件的出租房信息 
        ret = XunJianIntf.fastSearch_rental(orgId=orgInit['DftWangGeOrgId'],fastSearchKeyWords='出租房',username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '未搜索到企业信息') 
    
    #高级搜索出租房信息2（未停租）    
        ret = XunJianIntf.search_rental(orgId=orgInit['DftWangGeOrgId'],name=rentalParam_2['rental.name'],isStop=rentalParam_2['rental.isStop'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '未搜索到企业信息') 
        
    #检查已停租的出租房信息在列表中不显示
        checkParam = copy.deepcopy(XunJianPara.checkRentalDict)
        checkParam['name'] = rentalParam_3['rental.name']   
        ret = XunJianIntf.check_rental(checkParam, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '检查到已停租的出租房信息')         
        
    #高级搜索出租房信息3（已停租）    
        ret = XunJianIntf.search_rental(orgId=orgInit['DftWangGeOrgId'],name=rentalParam_3['rental.name'],isStop=rentalParam_3['rental.isStop'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '未搜索到企业信息') 
        pass
    
    def testRentalDispatch_29(self):
        """出租房划分"""
    #新增出租信息
        rentalParam = copy.deepcopy(XunJianPara.rentalObject) 
        rentalParam['mode'] = 'add'
        rentalParam['ownerOrg.id'] = orgInit['DftWangGeOrgId']
        rentalParam['orgName'] = orgInit['DftWangGeOrg']
        rentalParam['rental.name'] = '出租房名称%s'%CommonUtil.createRandomString()
        rentalParam['rental.address'] = '出租房地址%s'%CommonUtil.createRandomString()
        rentalParam['rental.owner'] = '出租人姓名%s'%CommonUtil.createRandomString()     
        rentalParam['rental.ownerPhone'] = '11111111111'
        rentalParam['rental.rentalType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='出租房类型', displayName='居住出租房')
        rentalParam['rental.rentalFloor'] = '3'
        rentalParam['rental.rentalArea'] = '100'
        rentalParam['rental.rentalStructure.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='出租房结构', displayName='钢结构')
        rentalParam['rental.rentedNumber'] = '3'
        rentalParam['rental.police'] = '派出所负责民警%s'%CommonUtil.createRandomString()
        rentalParam['rental.isStop'] = 'false'  #是否停租
        rentalParam['rental.dangerSituation'] = '隐患情况%s'%CommonUtil.createRandomString()  
        rentalParam['rental.gridPerson'] = '%s-%s'%( CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.username= '%s' " % userInit['DftWangGeUser1']),orgInit['DftWangGeOrg1'])
        responseDict = XunJianIntf.add_rental(rentalParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增出租房失败') 

    #对企业划分 
        dispatchParam = copy.deepcopy(XunJianPara.dispatchDict)
        dispatchParam['selectIds'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rental t where t.name='%s'" % rentalParam['rental.name'])
        dispatchParam['userId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.organizationid='%s' " % orgInit['DftWangGeOrgId1'] )
        ret = XunJianIntf.dispatchRentalDivision(dispatchParam, username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '划分出租房信息失败')         

    #检查出租房划分后的所属负责人信息  
        checkParam = copy.deepcopy(XunJianPara.checkRentalDict)
        checkParam['name'] = rentalParam['rental.name']   
        checkParam['gridPerson'] = userInit['DftWangGeUserXM1']
        ret = XunJianIntf.check_rental(checkParam, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '未检查到出租房信息')  

        pass
    
    def testRentalImportAndDownLoad_30(self):
        """出租房信息 导入/导出"""
         
        importHuJiparam = copy.deepcopy(XunJianPara.data)
        importHuJiparam['dataType']='rentalInfo'
        importHuJiparam['templates']='RENTALINFO'
        files = {'upload': ('test.xls', open('C:/autotest_file/importChuZuFang.xls', 'rb'),'applicationnd.ms-excel')}
        ret = XunJianIntf.import_Data(importHuJiparam, files=files,username=userInit['DftWangGeUser'], password='11111111')         
        
        checkParam = copy.deepcopy(XunJianPara.checkEnterpriseDict)
        checkParam['name'] = '出租房导入测试'   
        ret = XunJianIntf.check_rental(checkParam, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '未检查到出租房信息') 
                                
        downLoadHuJiparam = copy.deepcopy(XunJianPara.dlData)
        downLoadHuJiparam['orgId']=orgInit['DftWangGeOrgId']
        downLoadHuJiparam['pageOnly']='true'  #导出全部数据:false 导出本页数据:true
        response = XunJianIntf.downLoad_Rental(downLoadHuJiparam, username=userInit['DftWangGeUser'], password='11111111')         
        with open("C:/autotest_file/downLoadChuZuFang.xls", "wb") as code:
            code.write(response.content)

    #匹配失败？     匹配方法更新？       
        ret = CommonUtil.checkExcelCellValue(checkParam['name'], 'downLoadChuZuFang.xls','出租房信息', 'C4')          
        self.assertTrue(ret, '导出失败')
                         
        pass

    def testRentalRecordAdd_31(self):
        """出租房>巡检记录 添加"""
    #新增出租房严重隐患项信息
        riskRemarkParam = copy.deepcopy(XunJianPara.riskRemarkObject) 
        riskRemarkParam['riskRemark.riskRemarkName'] = '严重隐患备注项%s'%CommonUtil.createRandomString()
        riskRemarkParam['riskRemark.level.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='隐患等级', displayName='严重')   # 不合格：2014  严重：2015  
        riskRemarkParam['riskRemark.isEnable'] = '1'  #启用-1  禁用-0
        riskRemarkParam['mode'] = 'add'
        riskRemarkParam['riskRemark.riskmarkerType'] = '1'     #企业-0  出租房-1
        riskRemarkParam['riskRemark.orgId.id'] = orgInit['DftJieDaoOrgId']
        riskRemarkParam['isSubmit'] = 'true'  
        responseDict = XunJianIntf.add_riskRemark(riskRemarkParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增隐患项失败') 
        
    #新增出租房不合格隐患项信息
        newRiskRemarkParam = copy.deepcopy(XunJianPara.riskRemarkObject) 
        newRiskRemarkParam['riskRemark.riskRemarkName'] = '不合格隐患备注项%s'%CommonUtil.createRandomString()
        newRiskRemarkParam['riskRemark.level.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='隐患等级', displayName='不合格')   # 不合格：2014  严重：2015  
        newRiskRemarkParam['riskRemark.isEnable'] = '1'  #启用-1  禁用-0
        newRiskRemarkParam['mode'] = 'add'
        newRiskRemarkParam['riskRemark.riskmarkerType'] = '1'     #企业-0  出租房-1
        newRiskRemarkParam['riskRemark.orgId.id'] = orgInit['DftJieDaoOrgId']
        newRiskRemarkParam['isSubmit'] = 'true'  
        responseDict = XunJianIntf.add_riskRemark(newRiskRemarkParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增隐患项失败') 
        
    #新增出租信息
        rentalParam = copy.deepcopy(XunJianPara.rentalObject) 
        rentalParam['mode'] = 'add'
        rentalParam['ownerOrg.id'] = orgInit['DftWangGeOrgId']
        rentalParam['orgName'] = orgInit['DftWangGeOrg']
        rentalParam['rental.name'] = '出租房名称%s'%CommonUtil.createRandomString()
        rentalParam['rental.address'] = '出租房地址%s'%CommonUtil.createRandomString()
        rentalParam['rental.owner'] = '出租人姓名%s'%CommonUtil.createRandomString()     
        rentalParam['rental.ownerPhone'] = '11111111111'
        rentalParam['rental.rentalType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='出租房类型', displayName='居住出租房')
        rentalParam['rental.rentalFloor'] = '3'
        rentalParam['rental.rentalArea'] = '100'
        rentalParam['rental.rentalStructure.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='出租房结构', displayName='钢结构')
        rentalParam['rental.rentedNumber'] = '3'
        rentalParam['rental.police'] = '派出所负责民警%s'%CommonUtil.createRandomString()
        rentalParam['rental.isStop'] = 'false'  #是否停租
        rentalParam['rental.dangerSituation'] = '隐患情况%s'%CommonUtil.createRandomString()  
        rentalParam['rental.gridPerson'] = '%s-%s'%( CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.username= '%s' " % userInit['DftWangGeUser1']),orgInit['DftWangGeOrg1'])
        responseDict = XunJianIntf.add_rental(rentalParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增出租房失败') 
        
    #新增合格的巡检记录信息
        inspectionParam = copy.deepcopy(XunJianPara.inspectionRentalObject) 
        inspectionParam['mode'] = 'addInspectionRecord'
        inspectionParam['inspection.orgId'] = rentalParam['ownerOrg.id'] 
        inspectionParam['rental.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rental t where t.name='%s'" % rentalParam['rental.name'])
        inspectionParam['rental.name'] = rentalParam['rental.name'] 
        inspectionParam['inspectionRecord.enterprise.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rental t where t.name='%s'" % rentalParam['rental.name'])
        inspectionParam['inspection.inspectTime'] = Time.getCurrentDate()
        inspectionParam['inspection.inspectAddress'] = rentalParam['rental.address']
        inspectionParam['inspection.inspectResult'] = '1'  #合格：1 不合格：0  严重：2
        inspectionParam['inspection.limitTime'] = Time.getCurrentDate()
        inspectionParam['inspection.inspectUserId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.organizationid='%s' " % rentalParam['ownerOrg.id']) 
        inspectionParam['inspection.inspectName'] = userInit['DftWangGeUserXM']
        inspectionParam['inspection.remark'] = '描述%s'%CommonUtil.createRandomString()
        responseDict = XunJianIntf.add_InspectionRentalRecord(inspectionParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '巡检记录添加失败') 
        
    #在巡检工作的巡检记录下检查新增合格的巡检记录信息      
        checkParam = copy.deepcopy(XunJianPara.checkRentalDict)
        checkParam['name'] = rentalParam['rental.name'] 
        ret = XunJianIntf.check_RentalRecord(checkParam, orgId=orgInit['DftWangGeOrgId'],sourceType='4',recordType='1',mode = 'inspectionRecord',username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '未检查到巡检信息') 
     
    #新增不合格的巡检记录信息   
        newInspectionParam = copy.deepcopy(XunJianPara.inspectionObject)         
        newInspectionParam['mode'] = 'addInspectionRecord'
        newInspectionParam['inspection.orgId'] = rentalParam['ownerOrg.id'] 
        newInspectionParam['rental.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rental t where t.name='%s'" % rentalParam['rental.name'])
        newInspectionParam['rental.name'] = rentalParam['rental.name']  
        newInspectionParam['inspectionRecord.enterprise.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rental t where t.name='%s'" % rentalParam['rental.name'])
        newInspectionParam['inspection.inspectTime'] = Time.getCurrentDate()
        newInspectionParam['inspection.inspectAddress'] = rentalParam['rental.address']
        newInspectionParam['riskRemarkName'] = 'on' 
        newInspectionParam['inspection.inspectResult'] = '0'  #合格：1 不合格：0  严重：2
        newInspectionParam['inspection.limitTime'] = Time.getCurrentDate()
        newInspectionParam['inspection.inspectUserId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.organizationid='%s' " % rentalParam['ownerOrg.id']) 
        newInspectionParam['inspection.inspectName'] = userInit['DftWangGeUserXM']
        newInspectionParam['riskRemarkIds'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskremarks t where t.riskremarkname='%s'" % (newRiskRemarkParam['riskRemark.riskRemarkName']))
        newInspectionParam['inspection.remark'] = '描述%s'%CommonUtil.createRandomString()
        responseDict = XunJianIntf.add_InspectionRentalRecord(newInspectionParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '巡检记录添加失败') 

    #在巡检工作的待复查下检查新增不合格的巡检记录信息     (注：待复查下搜索与查看接口一致)
        checkParam = copy.deepcopy(XunJianPara.checkRentalDict)
        checkParam['name'] = newInspectionParam['rental.name']    
        ret = XunJianIntf.check_RentalRecord(checkParam, orgId=orgInit['DftWangGeOrgId'],recordType='1',mode = 'reviewRecord',username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '未检查到待复查的巡检记录信息') 
        
    #新增严重的巡检记录信息   
        inspectionParam_3 = copy.deepcopy(XunJianPara.inspectionRentalObject) 
        inspectionParam_3['mode'] = 'addInspectionRecord'
        inspectionParam_3['inspection.orgId'] = rentalParam['ownerOrg.id'] 
        inspectionParam_3['rental.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rental t where t.name='%s'" % rentalParam['rental.name'])
        inspectionParam_3['rental.name'] = rentalParam['rental.name'] 
        inspectionParam_3['inspectionRecord.enterprise.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rental t where t.name='%s'" % rentalParam['rental.name'])
        inspectionParam_3['inspection.inspectTime'] = Time.getCurrentDate()
        inspectionParam_3['inspection.inspectAddress'] = rentalParam['rental.address']
        inspectionParam_3['inspection.inspectResult'] = '2'  #合格：1 不合格：0  严重：2
        inspectionParam_3['inspection.limitTime'] = Time.getCurrentDate()
        inspectionParam_3['inspection.inspectUserId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.organizationid='%s' " % rentalParam['ownerOrg.id']) 
        inspectionParam_3['inspection.inspectName'] = userInit['DftWangGeUserXM']
        inspectionParam_3['inspection.remark'] = '描述%s'%CommonUtil.createRandomString()
        responseDict = XunJianIntf.add_InspectionRentalRecord(inspectionParam_3, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '巡检记录添加失败') 

    #在受理中心检查新增严重的巡检记录信息     
        checkParam = copy.deepcopy(XunJianPara.checkRentalDict)
        checkParam['name'] = inspectionParam_3['rental.name']  
        ret = XunJianIntf.check_InspectionRecord(checkParam, orgId=orgInit['DftWangGeOrgId'],mode = 'acceptCenterRecord',username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '受理中心未检查到新增的出租房巡检记录')
        pass


#出租房巡检工作


    def testRentalRecordSearch_32(self):
        """出租房>巡检记录 搜索"""
    #新增出租信息1
        rentalParam = copy.deepcopy(XunJianPara.rentalObject) 
        rentalParam['mode'] = 'add'
        rentalParam['ownerOrg.id'] = orgInit['DftWangGeOrgId']
        rentalParam['orgName'] = orgInit['DftWangGeOrg']
        rentalParam['rental.name'] = '1出租房名称%s'%CommonUtil.createRandomString()
        rentalParam['rental.address'] = '出租房地址%s'%CommonUtil.createRandomString()
        rentalParam['rental.owner'] = '出租人姓名%s'%CommonUtil.createRandomString()     
        rentalParam['rental.ownerPhone'] = '11111111111'
        rentalParam['rental.rentalType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='出租房类型', displayName='居住出租房')
        rentalParam['rental.rentalFloor'] = '3'
        rentalParam['rental.rentalArea'] = '100'
        rentalParam['rental.rentalStructure.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='出租房结构', displayName='钢结构')
        rentalParam['rental.rentedNumber'] = '3'
        rentalParam['rental.police'] = '派出所负责民警%s'%CommonUtil.createRandomString()
        rentalParam['rental.isStop'] = 'false'  #是否停租
        rentalParam['rental.dangerSituation'] = '隐患情况%s'%CommonUtil.createRandomString()  
        rentalParam['rental.gridPerson'] = '%s-%s'%( CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.username= '%s' " % userInit['DftWangGeUser1']),orgInit['DftWangGeOrg1'])
        responseDict = XunJianIntf.add_rental(rentalParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增出租房失败') 
        
    #新增合格的巡检记录信息1
        inspectionParam = copy.deepcopy(XunJianPara.inspectionRentalObject) 
        inspectionParam['mode'] = 'addInspectionRecord'
        inspectionParam['inspection.orgId'] = rentalParam['ownerOrg.id'] 
        inspectionParam['rental.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rental t where t.name='%s'" % rentalParam['rental.name'])
        inspectionParam['rental.name'] = rentalParam['rental.name'] 
        inspectionParam['inspectionRecord.enterprise.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rental t where t.name='%s'" % rentalParam['rental.name'])
        inspectionParam['inspection.inspectTime'] = Time.getCurrentDate()
        inspectionParam['inspection.inspectAddress'] = rentalParam['rental.address']
        inspectionParam['inspection.inspectResult'] = '1'  #合格：1 不合格：0  严重：2
        inspectionParam['inspection.limitTime'] = Time.getCurrentDate()
        inspectionParam['inspection.inspectUserId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.organizationid='%s' " % rentalParam['ownerOrg.id']) 
        inspectionParam['inspection.inspectName'] = userInit['DftWangGeUserXM']
        inspectionParam['inspection.remark'] = '描述%s'%CommonUtil.createRandomString()
        responseDict = XunJianIntf.add_InspectionRentalRecord(inspectionParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '巡检记录添加失败') 
        
    #新增出租信息2
        newRentalParam = copy.deepcopy(XunJianPara.rentalObject) 
        newRentalParam['mode'] = 'add'
        newRentalParam['ownerOrg.id'] = orgInit['DftWangGeOrgId']
        newRentalParam['orgName'] = orgInit['DftWangGeOrg']
        newRentalParam['rental.name'] = '出租房名称%s'%CommonUtil.createRandomString()
        newRentalParam['rental.address'] = '出租房地址%s'%CommonUtil.createRandomString()
        newRentalParam['rental.owner'] = '出租人姓名%s'%CommonUtil.createRandomString()     
        newRentalParam['rental.ownerPhone'] = '11111111111'
        newRentalParam['rental.rentalType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='出租房类型', displayName='居住出租房')
        newRentalParam['rental.rentalFloor'] = '3'
        newRentalParam['rental.rentalArea'] = '100'
        newRentalParam['rental.rentalStructure.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='出租房结构', displayName='钢结构')
        newRentalParam['rental.rentedNumber'] = '3'
        newRentalParam['rental.police'] = '派出所负责民警%s'%CommonUtil.createRandomString()
        newRentalParam['rental.isStop'] = 'false'  #是否停租
        newRentalParam['rental.dangerSituation'] = '隐患情况%s'%CommonUtil.createRandomString()  
        newRentalParam['rental.gridPerson'] = '%s-%s'%( CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.username= '%s' " % userInit['DftWangGeUser1']),orgInit['DftWangGeOrg1'])
        responseDict = XunJianIntf.add_rental(newRentalParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增出租房失败') 
        
    #新增合格的巡检记录信息2
        newInspectionParam = copy.deepcopy(XunJianPara.inspectionRentalObject) 
        newInspectionParam['mode'] = 'addInspectionRecord'
        newInspectionParam['inspection.orgId'] = newRentalParam['ownerOrg.id'] 
        newInspectionParam['rental.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rental t where t.name='%s'" % newRentalParam['rental.name'])
        newInspectionParam['rental.name'] = newRentalParam['rental.name'] 
        newInspectionParam['inspectionRecord.enterprise.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rental t where t.name='%s'" % newRentalParam['rental.name'])
        newInspectionParam['inspection.inspectTime'] = Time.getCurrentDate()
        newInspectionParam['inspection.inspectAddress'] = newRentalParam['rental.address']
        newInspectionParam['inspection.inspectResult'] = '1'  #合格：1 不合格：0  严重：2
        newInspectionParam['inspection.limitTime'] = Time.getCurrentDate()
        newInspectionParam['inspection.inspectUserId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.organizationid='%s' " % newRentalParam['ownerOrg.id']) 
        newInspectionParam['inspection.inspectName'] = userInit['DftWangGeUserXM']
        newInspectionParam['inspection.remark'] = '描述%s'%CommonUtil.createRandomString()
        responseDict = XunJianIntf.add_InspectionRentalRecord(newInspectionParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '巡检记录添加失败')

    #搜索巡检记录信息1   
        searchParam = copy.deepcopy(XunJianPara.checkRentalDict)
        searchParam['name'] = inspectionParam['rental.name']  
        ret = XunJianIntf.check_RentalRecord(searchParam, orgId=orgInit['DftWangGeOrgId'],sourceType='4',recordType='1',mode = 'inspectionRecord',name=inspectionParam['rental.name'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '未搜索到巡检信息') 
    
    #高级搜索巡检记录信息2    
        advancedSearch_Param = copy.deepcopy(XunJianPara.checkRentalDict)
        advancedSearch_Param['name'] = newInspectionParam['rental.name']  
        ret = XunJianIntf.check_RentalRecord(advancedSearch_Param, orgId=orgInit['DftWangGeOrgId'],mode = 'inspectionRecord',name=newInspectionParam['rental.name'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '未搜索到巡检信息') 

    #搜索不符合条件的巡检记录信息    
        advancedSearch_Param = copy.deepcopy(XunJianPara.checkRentalDict)
        advancedSearch_Param['name'] = '巡检记录'
        ret = XunJianIntf.check_RentalRecord(searchParam, orgId=orgInit['DftWangGeOrgId'],sourceType='4',recordType='1',mode = 'inspectionRecord',name='巡检记录',username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '搜索到不符合条件的巡检记录信息，搜素失败') 

    def testRentalDownLoad_33(self):
        """出租房巡检记录信息 导出"""
    #新增出租信息
        rentalParam = copy.deepcopy(XunJianPara.rentalObject) 
        rentalParam['mode'] = 'add'
        rentalParam['ownerOrg.id'] = orgInit['DftWangGeOrgId']
        rentalParam['orgName'] = orgInit['DftWangGeOrg']
        rentalParam['rental.name'] = '导出出租房名称%s'%CommonUtil.createRandomString()
        rentalParam['rental.address'] = '出租房地址%s'%CommonUtil.createRandomString()
        rentalParam['rental.owner'] = '出租人姓名%s'%CommonUtil.createRandomString()     
        rentalParam['rental.ownerPhone'] = '11111111111'
        rentalParam['rental.rentalType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='出租房类型', displayName='居住出租房')
        rentalParam['rental.rentalFloor'] = '3'
        rentalParam['rental.rentalArea'] = '100'
        rentalParam['rental.rentalStructure.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='出租房结构', displayName='钢结构')
        rentalParam['rental.rentedNumber'] = '3'
        rentalParam['rental.police'] = '派出所负责民警%s'%CommonUtil.createRandomString()
        rentalParam['rental.isStop'] = 'false'  #是否停租
        rentalParam['rental.dangerSituation'] = '隐患情况%s'%CommonUtil.createRandomString()  
        rentalParam['rental.gridPerson'] = '%s-%s'%( CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.username= '%s' " % userInit['DftWangGeUser1']),orgInit['DftWangGeOrg1'])
        responseDict = XunJianIntf.add_rental(rentalParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增出租房失败') 
        
    #新增合格的巡检记录信息
        inspectionParam = copy.deepcopy(XunJianPara.inspectionRentalObject) 
        inspectionParam['mode'] = 'addInspectionRecord'
        inspectionParam['inspection.orgId'] = rentalParam['ownerOrg.id'] 
        inspectionParam['rental.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rental t where t.name='%s'" % rentalParam['rental.name'])
        inspectionParam['rental.name'] = rentalParam['rental.name'] 
        inspectionParam['inspectionRecord.enterprise.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rental t where t.name='%s'" % rentalParam['rental.name'])
        inspectionParam['inspection.inspectTime'] = Time.getCurrentDate()
        inspectionParam['inspection.inspectAddress'] = rentalParam['rental.address']
        inspectionParam['inspection.inspectResult'] = '1'  #合格：1 不合格：0  严重：2
        inspectionParam['inspection.limitTime'] = Time.getCurrentDate()
        inspectionParam['inspection.inspectUserId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.organizationid='%s' " % rentalParam['ownerOrg.id']) 
        inspectionParam['inspection.inspectName'] = userInit['DftWangGeUserXM']
        inspectionParam['inspection.remark'] = '描述%s'%CommonUtil.createRandomString()
        responseDict = XunJianIntf.add_InspectionRentalRecord(inspectionParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '巡检记录添加失败') 
     
    #导出出租房巡检记录信息                            
        downLoadHuJiparam = copy.deepcopy(XunJianPara.dlXunJianData)
        downLoadHuJiparam['inspectionRecordVo.orgId']=orgInit['DftWangGeOrgId']
        downLoadHuJiparam['inspectionRecordVo.sourceType']= '4'
        downLoadHuJiparam['inspectionRecordVo.recordType']= '1'
        downLoadHuJiparam['mode']='inspectionRecord'
        downLoadHuJiparam['pageOnly']='true'  #导出全部数据:false 导出本页数据:true
        response = XunJianIntf.downLoad_XunJian(downLoadHuJiparam, username=userInit['DftWangGeUser'], password='11111111')         
        with open("C:/autotest_file/downLoadChuZuFang.xls", "wb") as code:
            code.write(response.content)

    #检查导出信息
        checkParam = copy.deepcopy(XunJianPara.checkRentalDict)   
        checkParam['name'] = inspectionParam['rental.name']
        ret = CommonUtil.checkExcelCellValue(checkParam['name'], 'downLoadChuZuFang.xls','巡检记录', 'A4')          
        self.assertTrue(ret, '检查导出失败')
        pass

    def testRentalRecordReview_34(self): #未成功？
        """出租房>巡检记录 复查"""
    #新增出租房不合格隐患项信息
        newRiskRemarkParam = copy.deepcopy(XunJianPara.riskRemarkObject) 
        newRiskRemarkParam['riskRemark.riskRemarkName'] = '不合格隐患备注项%s'%CommonUtil.createRandomString()
        newRiskRemarkParam['riskRemark.level.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='隐患等级', displayName='不合格')   # 不合格：2014  严重：2015  
        newRiskRemarkParam['riskRemark.isEnable'] = '1'  #启用-1  禁用-0
        newRiskRemarkParam['mode'] = 'add'
        newRiskRemarkParam['riskRemark.riskmarkerType'] = '1'     #企业-0  出租房-1
        newRiskRemarkParam['riskRemark.orgId.id'] = orgInit['DftJieDaoOrgId']
        newRiskRemarkParam['isSubmit'] = 'true'  
        responseDict = XunJianIntf.add_riskRemark(newRiskRemarkParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增隐患项失败') 
        
    #新增出租信息1
        rentalParam = copy.deepcopy(XunJianPara.rentalObject) 
        rentalParam['mode'] = 'add'
        rentalParam['ownerOrg.id'] = orgInit['DftWangGeOrgId']
        rentalParam['orgName'] = orgInit['DftWangGeOrg']
        rentalParam['rental.name'] = '出租房名称%s'%CommonUtil.createRandomString()
        rentalParam['rental.address'] = '出租房地址%s'%CommonUtil.createRandomString()
        rentalParam['rental.owner'] = '出租人姓名%s'%CommonUtil.createRandomString()     
        rentalParam['rental.ownerPhone'] = '11111111111'
        rentalParam['rental.rentalType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='出租房类型', displayName='居住出租房')
        rentalParam['rental.rentalFloor'] = '3'
        rentalParam['rental.rentalArea'] = '100'
        rentalParam['rental.rentalStructure.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='出租房结构', displayName='钢结构')
        rentalParam['rental.rentedNumber'] = '3'
        rentalParam['rental.police'] = '派出所负责民警%s'%CommonUtil.createRandomString()
        rentalParam['rental.isStop'] = 'false'  #是否停租
        rentalParam['rental.dangerSituation'] = '隐患情况%s'%CommonUtil.createRandomString()  
        rentalParam['rental.gridPerson'] = '%s-%s'%( CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.username= '%s' " % userInit['DftWangGeUser1']),orgInit['DftWangGeOrg1'])
        responseDict = XunJianIntf.add_rental(rentalParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增出租房失败') 
        
    #新增不合格的巡检记录信息1
        inspectionParam = copy.deepcopy(XunJianPara.inspectionRentalObject) 
        inspectionParam['mode'] = 'addInspectionRecord'
        inspectionParam['inspection.orgId'] = rentalParam['ownerOrg.id'] 
        inspectionParam['rental.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rental t where t.name='%s'" % rentalParam['rental.name'])
        inspectionParam['rental.name'] = rentalParam['rental.name'] 
        inspectionParam['inspectionRecord.enterprise.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rental t where t.name='%s'" % rentalParam['rental.name'])
        inspectionParam['inspection.inspectTime'] = Time.getCurrentDate()
        inspectionParam['inspection.inspectAddress'] = rentalParam['rental.address']
        inspectionParam['inspection.inspectResult'] = '0'  #合格：1 不合格：0  严重：2
        inspectionParam['inspection.limitTime'] = Time.getCurrentDate()
        inspectionParam['inspection.inspectUserId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.organizationid='%s' " % rentalParam['ownerOrg.id']) 
        inspectionParam['inspection.inspectName'] = userInit['DftWangGeUserXM']
        inspectionParam['riskRemarkIds'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskremarks t where t.riskremarkname='%s'" % (newRiskRemarkParam['riskRemark.riskRemarkName']))
        inspectionParam['inspection.remark'] = '描述%s'%CommonUtil.createRandomString()
        responseDict = XunJianIntf.add_InspectionRentalRecord(inspectionParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '巡检记录添加失败') 
     
    #复查不合格的巡检记录信息   （复查合格）   
        reviewParam = copy.deepcopy(XunJianPara.reviewRentalObject)
        reviewParam['inspectionRecord.recordType'] = '1'
        reviewParam['mode'] = 'success'  
        reviewParam['inspection.orgId'] = inspectionParam['inspection.orgId']
        reviewParam['inspection.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from inspection t where t.inspectaddress='%s'" % rentalParam['rental.address'])   #？
        reviewParam['inspection.inspectAddress'] = inspectionParam['inspection.inspectAddress']
        reviewParam['inspectionRecord.enterprise.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rental t where t.name='%s'" % rentalParam['rental.name'])
        reviewParam['inspection.inspectTime'] = Time.getCurrentDate()
        reviewParam['isSolve222'] = 'true' #复查合格 true  不合格 false
        reviewParam['inspection.inspectResult'] = '1'  #复查合格 1   不合格 0
        reviewParam['inspection.inspectUserId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.organizationid='%s' " % inspectionParam['inspection.orgId'])
        reviewParam['inspection.inspectName'] = userInit['DftWangGeUserXM']
        reviewParam['solveIds'] = '222,'    #?
        reviewParam['inspection.remark'] = '描述%s'%CommonUtil.createRandomString()
        ret = XunJianIntf.review_RentalRecord(reviewParam, username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '复查企业不合格巡检记录失败')         

    #在检查记录列表中检查复查后的巡检记录信息
        checkParam = copy.deepcopy(XunJianPara.checkRentalDict)
        checkParam['name'] = inspectionParam['rental.name'] 
        ret = XunJianIntf.check_RentalRecord(checkParam, orgId=orgInit['DftWangGeOrgId'],sourceType='4',recordType='1',mode = 'inspectionRecord',username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '未检查到巡检信息') 
  
    #在待检查列表中该复查后的巡检记录信息不存在     
        checkParam = copy.deepcopy(XunJianPara.checkRentalDict)
        checkParam['name'] = inspectionParam['rental.name']    
        ret = XunJianIntf.check_RentalRecord(checkParam, orgId=orgInit['DftWangGeOrgId'],recordType='1',mode = 'reviewRecord',username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '复查后的巡检记录在带复查列表中依然存在，复查失败') 
        
    #复查不合格的巡检记录信息   （复查不合格）   
        reviewParam = copy.deepcopy(XunJianPara.reviewRentalObject)
        reviewParam['inspectionRecord.recordType'] = '1'
        reviewParam['mode'] = 'success'  
        reviewParam['inspection.orgId'] = inspectionParam['inspection.orgId']
        reviewParam['inspection.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from inspection t where t.inspectaddress='%s'" % rentalParam['rental.address'])   #？
        reviewParam['inspection.inspectAddress'] = inspectionParam['inspection.inspectAddress']
        reviewParam['inspectionRecord.enterprise.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rental t where t.name='%s'" % rentalParam['rental.name'])
        reviewParam['inspection.inspectTime'] = Time.getCurrentDate()
        reviewParam['isSolve222'] = 'true' #复查合格 true  不合格 false
        reviewParam['inspection.inspectResult'] = '0'  #复查合格 1   不合格 0
        reviewParam['inspection.inspectUserId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.organizationid='%s' " % inspectionParam['inspection.orgId'])
        reviewParam['inspection.inspectName'] = userInit['DftWangGeUserXM']
        reviewParam['solveIds'] = '222,'    #?
        reviewParam['inspection.remark'] = '描述%s'%CommonUtil.createRandomString()
        ret = XunJianIntf.review_RentalRecord(reviewParam, username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '复查企业不合格巡检记录失败')         
        
    #在检查记录列表中检查复查后的巡检记录信息
        checkParam = copy.deepcopy(XunJianPara.checkRentalDict)
        checkParam['name'] = inspectionParam['rental.name'] 
        ret = XunJianIntf.check_RentalRecord(checkParam, orgId=orgInit['DftWangGeOrgId'],sourceType='4',recordType='1',mode = 'inspectionRecord',username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '未检查到巡检信息') 
  
    #在待检查列表中该复查后的巡检记录信息不存在     
        checkParam = copy.deepcopy(XunJianPara.checkRentalDict)
        checkParam['name'] = inspectionParam['rental.name']    
        ret = XunJianIntf.check_RentalRecord(checkParam, orgId=orgInit['DftWangGeOrgId'],recordType='1',mode = 'reviewRecord',username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '复查后的巡检记录在带复查列表中依然存在，复查失败') 
         
    #在检查受理中心列表中检查复查后未整改的巡检记录信息
        checkParam = copy.deepcopy(XunJianPara.checkEnterpriseDict)
        checkParam['name'] = inspectionParam['rental.name']   
        ret = XunJianIntf.check_InspectionRecord(checkParam, orgId=orgInit['DftWangGeOrgId'],mode = 'acceptCenterRecord',sourceType='4',username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '受理中心未检查到新增的严重出租房巡检记录')
        pass


#出租房巡检统计
    def testRentalRecordReview_35(self):
        """出租房>巡检记录 添加"""
        #新增出租房严重隐患项信息
        riskRemarkParam = copy.deepcopy(XunJianPara.riskRemarkObject) 
        riskRemarkParam['riskRemark.riskRemarkName'] = '严重隐患备注项%s'%CommonUtil.createRandomString()
        riskRemarkParam['riskRemark.level.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='隐患等级', displayName='严重')   # 不合格：2014  严重：2015  
        riskRemarkParam['riskRemark.isEnable'] = '1'  #启用-1  禁用-0
        riskRemarkParam['mode'] = 'add'
        riskRemarkParam['riskRemark.riskmarkerType'] = '1'     #企业-0  出租房-1
        riskRemarkParam['riskRemark.orgId.id'] = orgInit['DftJieDaoOrgId']
        riskRemarkParam['isSubmit'] = 'true'  
        responseDict = XunJianIntf.add_riskRemark(riskRemarkParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增隐患项失败') 
        
    #新增出租房不合格隐患项信息
        newRiskRemarkParam = copy.deepcopy(XunJianPara.riskRemarkObject) 
        newRiskRemarkParam['riskRemark.riskRemarkName'] = '不合格隐患备注项%s'%CommonUtil.createRandomString()
        newRiskRemarkParam['riskRemark.level.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='隐患等级', displayName='不合格')   # 不合格：2014  严重：2015  
        newRiskRemarkParam['riskRemark.isEnable'] = '1'  #启用-1  禁用-0
        newRiskRemarkParam['mode'] = 'add'
        newRiskRemarkParam['riskRemark.riskmarkerType'] = '1'     #企业-0  出租房-1
        newRiskRemarkParam['riskRemark.orgId.id'] = orgInit['DftJieDaoOrgId']
        newRiskRemarkParam['isSubmit'] = 'true'  
        responseDict = XunJianIntf.add_riskRemark(newRiskRemarkParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增隐患项失败') 
        
    #新增出租信息
        rentalParam = copy.deepcopy(XunJianPara.rentalObject) 
        rentalParam['mode'] = 'add'
        rentalParam['ownerOrg.id'] = orgInit['DftWangGeOrgId']
        rentalParam['orgName'] = orgInit['DftWangGeOrg']
        rentalParam['rental.name'] = '出租房名称%s'%CommonUtil.createRandomString()
        rentalParam['rental.address'] = '出租房地址%s'%CommonUtil.createRandomString()
        rentalParam['rental.owner'] = '出租人姓名%s'%CommonUtil.createRandomString()     
        rentalParam['rental.ownerPhone'] = '11111111111'
        rentalParam['rental.rentalType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='出租房类型', displayName='居住出租房')
        rentalParam['rental.rentalFloor'] = '3'
        rentalParam['rental.rentalArea'] = '100'
        rentalParam['rental.rentalStructure.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='出租房结构', displayName='钢结构')
        rentalParam['rental.rentedNumber'] = '3'
        rentalParam['rental.police'] = '派出所负责民警%s'%CommonUtil.createRandomString()
        rentalParam['rental.isStop'] = 'false'  #是否停租
        rentalParam['rental.dangerSituation'] = '隐患情况%s'%CommonUtil.createRandomString()  
        rentalParam['rental.gridPerson'] = '%s-%s'%( CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.username= '%s' " % userInit['DftWangGeUser1']),orgInit['DftWangGeOrg1'])
        responseDict = XunJianIntf.add_rental(rentalParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增出租房失败') 
        
    #新增合格的巡检记录信息
        inspectionParam = copy.deepcopy(XunJianPara.inspectionRentalObject) 
        inspectionParam['mode'] = 'addInspectionRecord'
        inspectionParam['inspection.orgId'] = rentalParam['ownerOrg.id'] 
        inspectionParam['rental.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rental t where t.name='%s'" % rentalParam['rental.name'])
        inspectionParam['rental.name'] = rentalParam['rental.name'] 
        inspectionParam['inspectionRecord.enterprise.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rental t where t.name='%s'" % rentalParam['rental.name'])
        inspectionParam['inspection.inspectTime'] = Time.getCurrentDate()
        inspectionParam['inspection.inspectAddress'] = rentalParam['rental.address']
        inspectionParam['inspection.inspectResult'] = '1'  #合格：1 不合格：0  严重：2
        inspectionParam['inspection.limitTime'] = Time.getCurrentDate()
        inspectionParam['inspection.inspectUserId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.organizationid='%s' " % rentalParam['ownerOrg.id']) 
        inspectionParam['inspection.inspectName'] = userInit['DftWangGeUserXM']
        inspectionParam['inspection.remark'] = '描述%s'%CommonUtil.createRandomString()
        responseDict = XunJianIntf.add_InspectionRentalRecord(inspectionParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '巡检记录添加失败') 
        
    #在巡检工作的巡检记录下检查新增合格的巡检记录信息      
        checkParam = copy.deepcopy(XunJianPara.checkRentalDict)
        checkParam['name'] = rentalParam['rental.name'] 
        ret = XunJianIntf.check_RentalRecord(checkParam, orgId=orgInit['DftWangGeOrgId'],sourceType='4',recordType='1',mode = 'inspectionRecord',username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '未检查到巡检信息') 
     
    #新增不合格的巡检记录信息   
        newInspectionParam = copy.deepcopy(XunJianPara.inspectionObject)         
        newInspectionParam['mode'] = 'addInspectionRecord'
        newInspectionParam['inspection.orgId'] = rentalParam['ownerOrg.id'] 
        newInspectionParam['rental.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rental t where t.name='%s'" % rentalParam['rental.name'])
        newInspectionParam['rental.name'] = rentalParam['rental.name']  
        newInspectionParam['inspectionRecord.enterprise.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rental t where t.name='%s'" % rentalParam['rental.name'])
        newInspectionParam['inspection.inspectTime'] = Time.getCurrentDate()
        newInspectionParam['inspection.inspectAddress'] = rentalParam['rental.address']
        newInspectionParam['riskRemarkName'] = 'on' 
        newInspectionParam['inspection.inspectResult'] = '0'  #合格：1 不合格：0  严重：2
        newInspectionParam['inspection.limitTime'] = Time.getCurrentDate()
        newInspectionParam['inspection.inspectUserId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.organizationid='%s' " % rentalParam['ownerOrg.id']) 
        newInspectionParam['inspection.inspectName'] = userInit['DftWangGeUserXM']
        newInspectionParam['riskRemarkIds'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskremarks t where t.riskremarkname='%s'" % (newRiskRemarkParam['riskRemark.riskRemarkName']))
        newInspectionParam['inspection.remark'] = '描述%s'%CommonUtil.createRandomString()
        responseDict = XunJianIntf.add_InspectionRentalRecord(newInspectionParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '巡检记录添加失败') 

    #在巡检工作的待复查下检查新增不合格的巡检记录信息     (注：待复查下搜索与查看接口一致)
        checkParam = copy.deepcopy(XunJianPara.checkRentalDict)
        checkParam['name'] = newInspectionParam['rental.name']    
        ret = XunJianIntf.check_RentalRecord(checkParam, orgId=orgInit['DftWangGeOrgId'],recordType='1',mode = 'reviewRecord',username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '未检查到待复查的巡检记录信息') 
        
    #新增严重的巡检记录信息   
        inspectionParam_3 = copy.deepcopy(XunJianPara.inspectionRentalObject) 
        inspectionParam_3['mode'] = 'addInspectionRecord'
        inspectionParam_3['inspection.orgId'] = rentalParam['ownerOrg.id'] 
        inspectionParam_3['rental.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rental t where t.name='%s'" % rentalParam['rental.name'])
        inspectionParam_3['rental.name'] = rentalParam['rental.name'] 
        inspectionParam_3['inspectionRecord.enterprise.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rental t where t.name='%s'" % rentalParam['rental.name'])
        inspectionParam_3['inspection.inspectTime'] = Time.getCurrentDate()
        inspectionParam_3['inspection.inspectAddress'] = rentalParam['rental.address']
        inspectionParam_3['inspection.inspectResult'] = '2'  #合格：1 不合格：0  严重：2
        inspectionParam_3['inspection.limitTime'] = Time.getCurrentDate()
        inspectionParam_3['inspection.inspectUserId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.organizationid='%s' " % rentalParam['ownerOrg.id']) 
        inspectionParam_3['inspection.inspectName'] = userInit['DftWangGeUserXM']
        inspectionParam_3['inspection.remark'] = '描述%s'%CommonUtil.createRandomString()
        responseDict = XunJianIntf.add_InspectionRentalRecord(inspectionParam_3, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '巡检记录添加失败') 

    #在受理中心检查新增严重的巡检记录信息     
        checkParam = copy.deepcopy(XunJianPara.checkRentalDict)
        checkParam['name'] = inspectionParam_3['rental.name']  
        ret = XunJianIntf.check_InspectionRecord(checkParam, orgId=orgInit['DftWangGeOrgId'],mode = 'acceptCenterRecord',username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '受理中心未检查到新增的出租房巡检记录')
        pass

        """出租房>巡检记录 复查"""
    #新增出租房不合格隐患项信息
        newRiskRemarkParam = copy.deepcopy(XunJianPara.riskRemarkObject) 
        newRiskRemarkParam['riskRemark.riskRemarkName'] = '不合格隐患备注项%s'%CommonUtil.createRandomString()
        newRiskRemarkParam['riskRemark.level.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='隐患等级', displayName='不合格')   # 不合格：2014  严重：2015  
        newRiskRemarkParam['riskRemark.isEnable'] = '1'  #启用-1  禁用-0
        newRiskRemarkParam['mode'] = 'add'
        newRiskRemarkParam['riskRemark.riskmarkerType'] = '1'     #企业-0  出租房-1
        newRiskRemarkParam['riskRemark.orgId.id'] = orgInit['DftJieDaoOrgId']
        newRiskRemarkParam['isSubmit'] = 'true'  
        responseDict = XunJianIntf.add_riskRemark(newRiskRemarkParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增隐患项失败') 
        
    #新增出租信息1
        rentalParam = copy.deepcopy(XunJianPara.rentalObject) 
        rentalParam['mode'] = 'add'
        rentalParam['ownerOrg.id'] = orgInit['DftWangGeOrgId']
        rentalParam['orgName'] = orgInit['DftWangGeOrg']
        rentalParam['rental.name'] = '出租房名称%s'%CommonUtil.createRandomString()
        rentalParam['rental.address'] = '出租房地址%s'%CommonUtil.createRandomString()
        rentalParam['rental.owner'] = '出租人姓名%s'%CommonUtil.createRandomString()     
        rentalParam['rental.ownerPhone'] = '11111111111'
        rentalParam['rental.rentalType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='出租房类型', displayName='居住出租房')
        rentalParam['rental.rentalFloor'] = '3'
        rentalParam['rental.rentalArea'] = '100'
        rentalParam['rental.rentalStructure.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='出租房结构', displayName='钢结构')
        rentalParam['rental.rentedNumber'] = '3'
        rentalParam['rental.police'] = '派出所负责民警%s'%CommonUtil.createRandomString()
        rentalParam['rental.isStop'] = 'false'  #是否停租
        rentalParam['rental.dangerSituation'] = '隐患情况%s'%CommonUtil.createRandomString()  
        rentalParam['rental.gridPerson'] = '%s-%s'%( CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.username= '%s' " % userInit['DftWangGeUser1']),orgInit['DftWangGeOrg1'])
        responseDict = XunJianIntf.add_rental(rentalParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增出租房失败') 
        
    #新增不合格的巡检记录信息1
        inspectionParam = copy.deepcopy(XunJianPara.inspectionRentalObject) 
        inspectionParam['mode'] = 'addInspectionRecord'
        inspectionParam['inspection.orgId'] = rentalParam['ownerOrg.id'] 
        inspectionParam['rental.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rental t where t.name='%s'" % rentalParam['rental.name'])
        inspectionParam['rental.name'] = rentalParam['rental.name'] 
        inspectionParam['inspectionRecord.enterprise.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rental t where t.name='%s'" % rentalParam['rental.name'])
        inspectionParam['inspection.inspectTime'] = Time.getCurrentDate()
        inspectionParam['inspection.inspectAddress'] = rentalParam['rental.address']
        inspectionParam['inspection.inspectResult'] = '0'  #合格：1 不合格：0  严重：2
        inspectionParam['inspection.limitTime'] = Time.getCurrentDate()
        inspectionParam['inspection.inspectUserId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.organizationid='%s' " % rentalParam['ownerOrg.id']) 
        inspectionParam['inspection.inspectName'] = userInit['DftWangGeUserXM']
        inspectionParam['riskRemarkIds'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from riskremarks t where t.riskremarkname='%s'" % (newRiskRemarkParam['riskRemark.riskRemarkName']))
        inspectionParam['inspection.remark'] = '描述%s'%CommonUtil.createRandomString()
        responseDict = XunJianIntf.add_InspectionRentalRecord(inspectionParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '巡检记录添加失败') 
     
    #复查不合格的巡检记录信息   （复查合格）   
        reviewParam = copy.deepcopy(XunJianPara.reviewRentalObject)
        reviewParam['inspectionRecord.recordType'] = '1'
        reviewParam['mode'] = 'success'  
        reviewParam['inspection.orgId'] = inspectionParam['inspection.orgId']
        reviewParam['inspection.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from inspection t where t.inspectaddress='%s'" % rentalParam['rental.address'])   #？
        reviewParam['inspection.inspectAddress'] = inspectionParam['inspection.inspectAddress']
        reviewParam['inspectionRecord.enterprise.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rental t where t.name='%s'" % rentalParam['rental.name'])
        reviewParam['inspection.inspectTime'] = Time.getCurrentDate()
        reviewParam['isSolve222'] = 'true' #复查合格 true  不合格 false
        reviewParam['inspection.inspectResult'] = '1'  #复查合格 1   不合格 0
        reviewParam['inspection.inspectUserId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.organizationid='%s' " % inspectionParam['inspection.orgId'])
        reviewParam['inspection.inspectName'] = userInit['DftWangGeUserXM']
        reviewParam['solveIds'] = '222,'    #?
        reviewParam['inspection.remark'] = '描述%s'%CommonUtil.createRandomString()
        ret = XunJianIntf.review_RentalRecord(reviewParam, username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '复查企业不合格巡检记录失败')         

    #在检查记录列表中检查复查后的巡检记录信息
        checkParam = copy.deepcopy(XunJianPara.checkRentalDict)
        checkParam['name'] = inspectionParam['rental.name'] 
        ret = XunJianIntf.check_RentalRecord(checkParam, orgId=orgInit['DftWangGeOrgId'],sourceType='4',recordType='1',mode = 'inspectionRecord',username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '未检查到巡检信息') 
  
    #在待检查列表中该复查后的巡检记录信息不存在     
        checkParam = copy.deepcopy(XunJianPara.checkRentalDict)
        checkParam['name'] = inspectionParam['rental.name']    
        ret = XunJianIntf.check_RentalRecord(checkParam, orgId=orgInit['DftWangGeOrgId'],recordType='1',mode = 'reviewRecord',username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '复查后的巡检记录在带复查列表中依然存在，复查失败') 
        
    #复查不合格的巡检记录信息   （复查不合格）   
        reviewParam = copy.deepcopy(XunJianPara.reviewRentalObject)
        reviewParam['inspectionRecord.recordType'] = '1'
        reviewParam['mode'] = 'success'  
        reviewParam['inspection.orgId'] = inspectionParam['inspection.orgId']
        reviewParam['inspection.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from inspection t where t.inspectaddress='%s'" % rentalParam['rental.address'])   #？
        reviewParam['inspection.inspectAddress'] = inspectionParam['inspection.inspectAddress']
        reviewParam['inspectionRecord.enterprise.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rental t where t.name='%s'" % rentalParam['rental.name'])
        reviewParam['inspection.inspectTime'] = Time.getCurrentDate()
        reviewParam['isSolve222'] = 'true' #复查合格 true  不合格 false
        reviewParam['inspection.inspectResult'] = '0'  #复查合格 1   不合格 0
        reviewParam['inspection.inspectUserId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.organizationid='%s' " % inspectionParam['inspection.orgId'])
        reviewParam['inspection.inspectName'] = userInit['DftWangGeUserXM']
        reviewParam['solveIds'] = '222,'    #?
        reviewParam['inspection.remark'] = '描述%s'%CommonUtil.createRandomString()
        ret = XunJianIntf.review_RentalRecord(reviewParam, username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '复查企业不合格巡检记录失败')         
        
    #在检查记录列表中检查复查后的巡检记录信息
        checkParam = copy.deepcopy(XunJianPara.checkRentalDict)
        checkParam['name'] = inspectionParam['rental.name'] 
        ret = XunJianIntf.check_RentalRecord(checkParam, orgId=orgInit['DftWangGeOrgId'],sourceType='4',recordType='1',mode = 'inspectionRecord',username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '未检查到巡检信息') 
  
    #在待检查列表中该复查后的巡检记录信息不存在     
        checkParam = copy.deepcopy(XunJianPara.checkRentalDict)
        checkParam['name'] = inspectionParam['rental.name']    
        ret = XunJianIntf.check_RentalRecord(checkParam, orgId=orgInit['DftWangGeOrgId'],recordType='1',mode = 'reviewRecord',username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '复查后的巡检记录在带复查列表中依然存在，复查失败') 
         
    #在检查受理中心列表中检查复查后未整改的巡检记录信息
        checkParam = copy.deepcopy(XunJianPara.checkEnterpriseDict)
        checkParam['name'] = inspectionParam['rental.name']   
        ret = XunJianIntf.check_InspectionRecord(checkParam, orgId=orgInit['DftWangGeOrgId'],mode = 'acceptCenterRecord',sourceType='4',username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '受理中心未检查到新增的严重出租房巡检记录')
     


        #检查统计数
        checkTongJi = copy.deepcopy(XunJianPara.rentalHouseCheck)
#         #出租房总数  因为外面包了一层<a></a>标签 
#         count= CommonIntf.getDbQueryResult(dbCommand = "select count(*) from rental t  where t.createuser = '%s'  " % userInit['DftWangGeUser'])
#         checkTongJi['rentalTotalStr'] = count
#         ##检查数
#         checkCount =  CommonIntf.getDbQueryResult(dbCommand = "select count(distinct(t1.inspectaddress)) from inspection t1 where exists(select id  from rental t where t.address = t1.inspectaddress and  t.createuser ='%s') " % userInit['DftWangGeUser']) 
#         checkTongJi['inspectionRentalNumStr'] = checkCount
#         
#         ##未检查数
#         checkTongJi['noInspectionRentalNumStr'] = count - checkCount
#         ##检查率
#         #checkTongJi['inspectionPercentage'] =  (checkCount *1000)/count*0.001*1000
#         ret = XunJianIntf.check_RentalTongj(checkTongJi,username=userInit['DftWangGeUser'], password='11111111')         
#         self.assertTrue(ret, '出租屋统计查询失败')
# 
#         print '总数' ,checkTongJi['rentalTotalStr']  ,'检查数',checkTongJi['inspectionRentalNumStr'],checkTongJi['noInspectionRentalNumStr'],checkTongJi['inspectionPercentage']


        #巡检
        #总数
        xunJianCount =  CommonIntf.getDbQueryResult(dbCommand = "select count(*) from inspection t1 where exists(select id  from rental t where t.address = t1.inspectaddress and t1.inspecttype = 0 and  t.createuser ='%s') " % userInit['DftWangGeUser'])
        checkTongJi['inspectionTotal'] = xunJianCount
        #合格数
        qualifiedNum =  CommonIntf.getDbQueryResult(dbCommand = "select count(*) from inspection t1 where exists(select id  from rental t where t.address = t1.inspectaddress and t1.inspecttype = 0 and t1.inspectresult = 1 and t.createuser ='%s') " % userInit['DftWangGeUser'])
        checkTongJi['inspectionQualifiedNum'] = qualifiedNum
        #不合格数
        noQualifiedNum = CommonIntf.getDbQueryResult(dbCommand = "select count(*) from inspection t1 where exists(select id  from rental t where t.address = t1.inspectaddress and t1.inspecttype = 0  and t1.inspectresult = 0 and t.createuser ='%s') " % userInit['DftWangGeUser'])
        checkTongJi['inspectionNoQualifiedNum'] = noQualifiedNum
        #严重
        seriousCount = CommonIntf.getDbQueryResult(dbCommand = "select count(*) from inspection t1 where exists(select id  from rental t where t.address = t1.inspectaddress and t1.inspecttype = 0  and t1.inspectresult = 2 and t.createuser ='%s') " % userInit['DftWangGeUser'])
        checkTongJi['inspectionBadlyNum'] = seriousCount
        
        ret = XunJianIntf.check_RentalTongj(checkTongJi,username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '出租屋统计查询失败')
        
#     #出租房巡检统计导出       
#     def testRentalRecordReview_36(self):
#         """出租房>巡检统计导出"""
#         #导出出租房巡检记录信息                            
#         downLoadHuJiparam = copy.deepcopy(XunJianPara.rentalExport)
#         downLoadHuJiparam['staticsVo.orgId']=orgInit['DftWangGeOrgId']
#  
#         response = XunJianIntf.rentalExport(downLoadHuJiparam, username=userInit['DftWangGeUser'], password='11111111')         
#         with open("C:/autotest_file/downLoadchuzufangTongji.xls", "wb") as code:
#             code.write(response.content)
#  
#     #检查导出信息
#         checkParam = copy.deepcopy(XunJianPara.retalExportCheck)   
#         checkParam['inspectionTotal']  =  CommonIntf.getDbQueryResult(dbCommand = "select count(*) from inspection t1 where exists(select id  from rental t where t.address = t1.inspectaddress and t1.inspecttype = 0 and  t.createuser ='%s') " % userInit['DftWangGeUser'])
#         inspectionTotal = checkParam['inspectionTotal'] #类型问题 必须两边都转成String 才可以  求解、？？
#         ret = CommonUtil.checkExcelCellValue(float(inspectionTotal), 'downLoadchuzufangTongji.xls','出租房巡检统计', 'G4')          
#         self.assertTrue(ret, '导出失败')
#         pass
#  
#     #出租房巡检统计人员导出       
#     def testRentalRecordReview_37(self):
#         #导出出租房巡检记录信息                            
#         downLoadHuJiparam = copy.deepcopy(XunJianPara.rentalPerson)
#         downLoadHuJiparam['staticsVo.orgId']=orgInit['DftWangGeOrgId']
#         response = XunJianIntf.rentalExportPerson(downLoadHuJiparam, username=userInit['DftWangGeUser'], password='11111111')         
#         with open("C:/autotest_file/downLoadchuzufangTongjiPerson.xls", "wb") as code:
#             code.write(response.content)
#    
#         ##检查导出信息 
#         checkParam = copy.deepcopy(XunJianPara.retalExportCheck)    
#         checkParam['inspectionTotal']  =  CommonIntf.getDbQueryResult(dbCommand = "select count(*) from  inspection t where  t.inspectaddress = (select t.address from   rental t where t.createuser ='%s' and t.gridperson = '%s') " % (userInit['DftWangGeUser'],userInit['DftWangGeUserXM']))
#         print checkParam['inspectionTotal']
#         inspectionTotal = checkParam['inspectionTotal'] #类型问题 必须两边都转成String 才可以  求解、？？
#         ret = CommonUtil.checkExcelCellValue(str(inspectionTotal), 'downLoadchuzufangTongjiPerson.xls','人员统计', 'H4')          
#         self.assertTrue(ret, '导出失败')
#         pass
#  
# #督查暗访统计
#     def testRentalRecordReview_38(self):
#         """查看不同状态下的督查暗访记录 """
#     #新增督查暗访记录 1
#         getSupervisionParam = copy.deepcopy(XunJianPara.supervisionObject) 
#         getSupervisionParam['safeProductionEnterprise.name'] = '检查单位1%s'%CommonUtil.createRandomString()
#         getSupervisionParam['orgId'] = orgInit['DftJieDaoOrgId']
#         response = XunJianIntf.supervision(getSupervisionParam, username=userInit['DftJieDaoUser'], password='11111111')
#      
#         supervisionParam = copy.deepcopy(XunJianPara.supervisionObject) 
#         supervisionParam['secretSupervision.checkSubject'] = '检查科目%s'%CommonUtil.createRandomString()
#         supervisionParam['secretSupervision.checkTime'] = Time.getCurrentDate()
#         supervisionParam['secretSupervision.checkCompanyName'] = getSupervisionParam['safeProductionEnterprise.name']
#         supervisionParam['secretSupervision.checkAddress'] = '检查地址%s'%CommonUtil.createRandomString()
#         supervisionParam['secretSupervision.checkLegalPerson'] = '法人代表1%s'%CommonUtil.createRandomString()
#         supervisionParam['secretSupervision.mobileNumber'] = '13000000000'
#         supervisionParam['secretSupervision.findProblems'] = '检查结果%s'%CommonUtil.createRandomString()     
#         supervisionParam['secretSupervision.requires'] = '要求%s'%CommonUtil.createRandomString()
#         supervisionParam['mode'] = 'add'
#         supervisionParam['isSubmit'] = 'true'
#         supervisionParam['secretSupervision.orgId'] = getSupervisionParam['orgId'] 
#         responseDict = XunJianIntf.add_supervision(supervisionParam, username=userInit['DftJieDaoUser'], password='11111111')
#         self.assertTrue(responseDict.result, '新增失败') 
#          
#     #查看待流转记录  即：state='3'
#         checkParam = copy.deepcopy(XunJianPara.checkSupervisionDict)
#         checkParam['checkAddress'] = supervisionParam['secretSupervision.checkAddress']  
#         #ret = XunJianIntf.check_Supervision(checkParam, orgId=orgInit['DftJieDaoOrgId'],state='3',checkAddress = checkParam['checkAddress'],username=userInit['DftJieDaoUser'], password='11111111')         
#         ret = XunJianIntf.check_Supervision(checkParam, orgId=orgInit['DftJieDaoOrgId'],checkAddress = checkParam['checkAddress'],username=userInit['DftJieDaoUser'], password='11111111')
#         self.assertTrue(ret, '未检查到待流转督查暗访信息') 
#      
#     #将待转的巡检记录转事件处理  
#         turnIssueParam = copy.deepcopy(XunJianPara.turnIssueObject)
#         turnIssueParam['issue.occurOrg.id'] = getSupervisionParam['orgId']
#         turnIssueParam['inspectionIds'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from inspection t where t.inspectaddress='%s'" % supervisionParam['secretSupervision.checkAddress'])
#         turnIssueParam['dataSource'] = 'inspectionIssue'
#         turnIssueParam['issue.subject'] = '督查暗访-%s'% getSupervisionParam['safeProductionEnterprise.name']
#         turnIssueParam['selectOrgName'] = orgInit['DftJieDaoOrg']
#         turnIssueParam['issue.occurLocation'] = userInit['DftJieDaoUserXM']
#         turnIssueParam['issue.occurDate'] = Time.getCurrentDate()
#         turnIssueParam['eatHours'] = time.strftime("%I")
#         turnIssueParam['eatMinute'] = time.strftime("%M")
#         turnIssueParam['selectedTypes'] = '1'  #事件类型   
#         turnIssueParam['issueRelatedPeopleNames'] = supervisionParam['secretSupervision.checkLegalPerson']
#         turnIssueParam['issueRelatedPeopleTelephones'] = supervisionParam['secretSupervision.mobileNumber']
#         turnIssueParam['issue.relatePeopleCount'] = '10'  #人数
#         turnIssueParam['issue.issueContent'] = '%s,%s'%(supervisionParam['secretSupervision.findProblems'] ,supervisionParam['secretSupervision.requires'])
#         rs = XunJianIntf.turnIssueAcceptCenter(turnIssueParam, username=userInit['DftJieDaoUser'], password='11111111')  
#         responseDict = json.loads(rs.text)
#         self.assertTrue(rs, '巡检记录转事件失败') 
#          
#     #查看办理中记录  即：state='5'   
#         checkParam = copy.deepcopy(XunJianPara.checkSupervisionDict)
#         checkParam['checkAddress'] = supervisionParam['secretSupervision.checkAddress']  
#         #ret = XunJianIntf.check_Supervision(checkParam, orgId=orgInit['DftJieDaoOrgId'],state='5',checkAddress = checkParam['checkAddress'],username=userInit['DftJieDaoUser'], password='11111111')         
#         ret = XunJianIntf.check_Supervision(checkParam, orgId=orgInit['DftJieDaoOrgId'],checkAddress = checkParam['checkAddress'],username=userInit['DftJieDaoUser'], password='11111111')
#         self.assertTrue(ret, '未检查到办理中督查暗访信息') 
#   
#     #设置结案参数
#         sIssuePara=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)        
#         sIssuePara['operation.dealOrg.id']=orgInit['DftJieDaoOrgId']
#         print type(responseDict['issueId'])
#         sIssuePara['operation.issue.id']=responseDict['issueId']
#         sIssuePara['keyId']=responseDict['issueStepId']      
#         sIssuePara['operation.dealUserName']=userInit['DftJieDaoUserXM']
#         sIssuePara['operation.mobile']=userInit['DftJieDaoUserSJ']
#         sIssuePara['dealCode']='31' #结案
#         sIssuePara['dealTime']=Time.getCurrentDate()
#         sIssuePara['operation.content']='事件处理'  
#     #事件结案
#         result=XunJianIntf.deal_Issue(issueDict=sIssuePara,username=userInit['DftJieDaoUser'], password='11111111')
#         self.assertTrue(result.result, '事件操作失败!')
#           
#         Time.wait(2)
#     
#     #查看已办结记录  即：state='6'    
#         checkParam = copy.deepcopy(XunJianPara.checkSupervisionDict)
#         checkParam['checkAddress'] = supervisionParam['secretSupervision.checkAddress']  
#         #ret = XunJianIntf.check_Supervision(checkParam, orgId=orgInit['DftJieDaoOrgId'],state='6',username=userInit['DftJieDaoUser'], password='11111111')         
#         ret = XunJianIntf.check_Supervision(checkParam, orgId=orgInit['DftJieDaoOrgId'],username=userInit['DftJieDaoUser'], checkAddress = checkParam['checkAddress'] ,password='11111111')
#         self.assertTrue(ret, '未检查到已办结的督查暗访信息') 
#          
#         checkParam = copy.deepcopy(XunJianPara.inspectionCheck)   
#         checkParam['checkTotal'] =  CommonIntf.getDbQueryResult(dbCommand = "select  count(*) from secretsupervision t where t.createuser ='%s' " % userInit['DftJieDaoUser'])   
#         print checkParam['checkTotal']
#         ret = XunJianIntf.inspectionTongJi(checkParam, username=userInit['DftJieDaoUser'], password='11111111')
#         self.assertTrue(ret, '未检查到的督查暗访统计信息')        
#         pass    
    def tearDown(self):
        pass
    
if __name__ == "__main__":
    suite = unittest.TestSuite()

#     suite.addTest(XunJian("testEnterpriseAdd_01"))    
#     suite.addTest(XunJian("testInspectionRecordAdd_02"))
#    suite.addTest(XunJian("testQiYeImportAndDownLoad_03"))  
#    suite.addTest(XunJian("testEnterpriseDispatch_04"))
#     suite.addTest(XunJian("testEnterpriseSearch_05"))   
#     suite.addTest(XunJian("testEnterpriseEdit_06"))   
#     suite.addTest(XunJian("testEnterpriseDelete_07"))    
#     suite.addTest(XunJian("testInspectionRecordSearch_08")) 
#     suite.addTest(XunJian("testXunJianDownLoad_09")) 
#     suite.addTest(XunJian("testInspectionRecordReview_10")) 
#     suite.addTest(XunJian("testTurnIssueAcceptCenter_12"))  
#    suite.addTest(XunJian("testRecordSearch_13"))  
#     suite.addTest(XunJian("testRecordDelete_14")) 

#     suite.addTest(XunJian("testsecretSupervisionAdd_15")) 
#     suite.addTest(XunJian("testsecretSupervisionSearch_16"))
#     suite.addTest(XunJian("testsecretSupervisionDelete_17"))  
#    suite.addTest(XunJian("testsecretSupervisionCheck_18")) 

#     suite.addTest(XunJian("testriskRemarkAdd_19")) 
#     suite.addTest(XunJian("testriskRemarkEdit_20")) 
#     suite.addTest(XunJian("testriskRemarkDelete_21")) 
#    suite.addTest(XunJian("testriskRemarkSearch_22")) 
#     suite.addTest(XunJian("testriskRemarkMove_23")) 
#     suite.addTest(XunJian("testriskRemarkMove_24")) 

#    suite.addTest(XunJian("testRentalAdd_25")) 
#     suite.addTest(XunJian("testRentaledit_26")) 
#     suite.addTest(XunJian("testRentalDelete_27")) 
#     suite.addTest(XunJian("testRentalSearch_28")) 
#    suite.addTest(XunJian("testRentalDispatch_29")) 
#    suite.addTest(XunJian("testRentalImportAndDownLoad_30")) 
#    suite.addTest(XunJian("testRentalRecordAdd_31"))  
#     suite.addTest(XunJian("testRentalRecordSearch_32"))  
#    suite.addTest(XunJian("testRentalDownLoad_33"))
#    suite.addTest(XunJian("testRentalRecordReview_34"))  
    suite.addTest(XunJian("testRentalRecordReview_38")) 
    

        
    results = unittest.TextTestRunner().run(suite)
    pass