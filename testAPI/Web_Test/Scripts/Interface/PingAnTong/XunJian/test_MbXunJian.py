# -*- coding:UTF-8 -*-
'''
Created on 2016-3-25

@author: lhz
'''
from __future__ import unicode_literals
import unittest
from Interface.PingAnJianShe.SystemMgr import SystemMgrIntf
import copy
from Interface.PingAnTong.XunJian import MbXunJianPara, MbXunJianIntf
from Interface.PingAnJianShe.Common import CommonIntf
from CONFIG import InitDefaultPara
from COMMON import CommonUtil, Time
from Interface.PingAnJianShe.XunJian import XunJianPara, XunJianIntf
from CONFIG.InitDefaultPara import orgInit, userInit
import random
class XunJian(unittest.TestCase):
    def setUp(self):
        SystemMgrIntf.initEnv()
        pass
    
    '''
    @功能：企业信息新增,修改,列表查看
    @ lhz  2016-2-29
    ''' 
    def testmInspection_001(self):
        '''巡检--企业新增'''
        #新增单位信息
        issueParam = copy.deepcopy(MbXunJianPara.addCompanyParam)
        issueParam['safeProductionEnterprise.address'] = '中科院'
        issueParam['safeProductionEnterprise.legalPerson'] = '我在学校'
        issueParam['safeProductionEnterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='企业类型', displayName='规上企业') 
        issueParam['safeProductionEnterprise.isEmphasis'] = 'false'
        issueParam['safeProductionEnterprise.name'] = '巡检%s' % CommonUtil.createRandomString(6)
        issueParam['safeProductionEnterprise.gridPerson'] = '%s-%s' % (CommonIntf.getDbQueryResult(dbCommand="select t.id from users t where t.organizationid =  '%s'"%InitDefaultPara.orgInit['DftWangGeOrgId']),CommonIntf.getDbQueryResult(dbCommand="select t.name from users t where t.organizationid ='%s'"%InitDefaultPara.orgInit['DftWangGeOrgId']).decode('utf-8'))
        issueParam['ownerOrg.id'] =  InitDefaultPara.orgInit['DftWangGeOrgId']
        issueParam['safeProductionEnterprise.mobileNumber'] = random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8))
        ret = MbXunJianIntf.xunJianAdd(param=issueParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, '企业信息新增失败')
        Time.wait(1)
        #检查参数
        companyDict = copy.deepcopy(MbXunJianPara.addOrEditCheck)
        companyDict['name'] = issueParam['safeProductionEnterprise.name']
        # 获取查询参数
        ret = MbXunJianIntf.check_addCompany(companyDict, issueParam['ownerOrg.id'], username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, '企业信息查找失败')
        Time.wait(1)

        #修改
        issueParamUpdate = copy.deepcopy(MbXunJianPara.updateCompanyParam) 
        issueParamUpdate['safeProductionEnterprise.id'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from safeproductionenterprise t where t.name =  '%s'"%issueParam['safeProductionEnterprise.name'])
        issueParamUpdate['safeProductionEnterprise.address'] = '中科院50号'
        issueParamUpdate['safeProductionEnterprise.legalPerson'] = '德力西'
        issueParamUpdate['safeProductionEnterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='企业类型', displayName='规上企业') 
        issueParamUpdate['safeProductionEnterprise.isEmphasis'] = 'false'
        issueParamUpdate['safeProductionEnterprise.name'] = '巡检%s' % CommonUtil.createRandomString(6)
        issueParamUpdate['safeProductionEnterprise.gridPerson'] = '%s-%s'%( CommonIntf.getDbQueryResult(dbCommand="select t.id from users t where t.organizationid =  '%s'"%InitDefaultPara.orgInit['DftWangGeOrgId']),CommonIntf.getDbQueryResult(dbCommand="select t.name from users t where t.organizationid =  '%s'"%InitDefaultPara.orgInit['DftWangGeOrgId']).decode('utf-8'))
        issueParamUpdate['ownerOrg.id'] =  InitDefaultPara.orgInit['DftWangGeOrgId']
        issueParamUpdate['safeProductionEnterprise.mobileNumber'] = random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8))  
        ret = MbXunJianIntf.xunJianEdit(issueParamUpdate, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret, '企业信息修改失败')      
        Time.wait(1)
        
        #检查参数
        companyDict = copy.deepcopy(MbXunJianPara.addOrEditCheck)
        companyDict['name'] = issueParamUpdate['safeProductionEnterprise.name']
        # 获取查询参数
        ret = MbXunJianIntf.check_editCompany(companyDict, issueParam['ownerOrg.id'], username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, 'PC端企业信息查找失败')
        Time.wait(1)
 
#新增巡检记录  
    def testmInspection_002(self):
#         '''巡检--新增巡检记录 '''
        #新增单位信息
        issueParam = copy.deepcopy(MbXunJianPara.addCompanyParam)
        issueParam['safeProductionEnterprise.address'] = '地址%s'%CommonUtil.createRandomString()
        issueParam['safeProductionEnterprise.legalPerson'] = '我在学校'
        issueParam['safeProductionEnterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='企业类型', displayName='规上企业') 
        issueParam['safeProductionEnterprise.isEmphasis'] = 'false'
        issueParam['safeProductionEnterprise.name'] = '巡检%s' % CommonUtil.createRandomString(6)
        issueParam['safeProductionEnterprise.gridPerson'] = '%s-%s'%( CommonIntf.getDbQueryResult(dbCommand="select t.id from users t where t.organizationid =  '%s'"%InitDefaultPara.orgInit['DftWangGeOrgId']),CommonIntf.getDbQueryResult(dbCommand="select t.name from users t where t.organizationid =  '%s'"%InitDefaultPara.orgInit['DftWangGeOrgId']).decode('utf-8'))
        issueParam['ownerOrg.id'] =  InitDefaultPara.orgInit['DftWangGeOrgId']
        issueParam['safeProductionEnterprise.mobileNumber'] = random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8))
 
        ret = MbXunJianIntf.xunJianAdd(param=issueParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, '企业信息新增失败')
        Time.wait(1)  
        
        #新增隐患项 
        riskRemarkParam = copy.deepcopy(XunJianPara.enterpriseObject) 
        riskRemarkParam['riskRemark.riskRemarkName'] = '严重隐患备注项%s'%CommonUtil.createRandomString()
        riskRemarkParam['riskRemark.level.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='隐患等级', displayName='不合格') 
        riskRemarkParam['riskRemark.isEnable'] = '1'
        riskRemarkParam['mode'] = 'add'
        riskRemarkParam['riskRemark.riskmarkerType'] = 0 
        riskRemarkParam['riskRemark.orgId.id'] = orgInit['DftJieDaoOrgId']
        riskRemarkParam['isSubmit'] = 'true'  #是否启用：是-true  否-false
        responseDict = XunJianIntf.add_riskRemark(riskRemarkParam, username=userInit['DftShiUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增隐患项失败')      
        
         
#         #新增巡检记录
        recordParam = copy.deepcopy(MbXunJianPara.addXunJianRecord)
        recordParam['inspection.inspectAddress'] = issueParam['safeProductionEnterprise.address']
        recordParam['inspection.limitTime'] = Time.getCurrentDate()
        recordParam['inspection.recordType'] = 0 #（0巡检  1复查）
        recordParam['inspection.inspectResult'] = 0
        recordParam['inspection.inspectTime'] = Time.getCurrentDate()
        recordParam['inspection.inspectUserId'] =  CommonIntf.getDbQueryResult(dbCommand="select t.id from users t where t.organizationid =  '%s'"%InitDefaultPara.orgInit['DftShiOrgId'])
        recordParam['inspection.orgId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        recordParam['riskRemarkIds'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from riskremarks t where t.riskremarkname  = '%s'"%riskRemarkParam['riskRemark.riskRemarkName'])
        recordParam['inspectionRecord.enterprise.id'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from safeproductionenterprise t where t.name =  '%s'"%issueParam['safeProductionEnterprise.name'])
        recordParam['inspection.inspectName'] =  InitDefaultPara.userInit['DftShiUserXM']
        responseDict = MbXunJianIntf.addXunJianRecord(recordParam,username=userInit['DftShiUser'], password='11111111')
        self.assertTrue(responseDict, '新增巡检记录失败')   

                
            
        #检查巡检记录是否新增成功
        checkParam = copy.deepcopy(MbXunJianPara.check_record)
        checkParam['inspectionRecordVo.recordType'] = recordParam['inspection.recordType']
        checkParam['inspectionRecordVo.enterpriseId'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from safeproductionenterprise t where t.name =  '%s'"%issueParam['safeProductionEnterprise.name'])
        checkParam['inspectionRecordVo.orgId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        
        #检查参数
        companyDict = copy.deepcopy(MbXunJianPara.recordAdress)
        companyDict['address'] = recordParam['inspection.inspectAddress']
        # 获取查询参数
        ret = MbXunJianIntf.check_xunjianRecordXq(companyDict, checkParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, '查找到巡检记录详情失败')
        Time.wait(1)
        
        
#新增复查记录
    def testmInspection_003(self):
#         '''巡检--新增复查记录 '''
        
        #新增单位信息
        issueParam = copy.deepcopy(MbXunJianPara.addCompanyParam)
        issueParam['safeProductionEnterprise.address'] = '地址%s'%CommonUtil.createRandomString()
        issueParam['safeProductionEnterprise.legalPerson'] = '我在学校'
        issueParam['safeProductionEnterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='企业类型', displayName='规上企业') 
        issueParam['safeProductionEnterprise.isEmphasis'] = 'false'
        issueParam['safeProductionEnterprise.name'] = '巡检%s' % CommonUtil.createRandomString(6)
        issueParam['safeProductionEnterprise.gridPerson'] = '%s-%s'%( CommonIntf.getDbQueryResult(dbCommand="select t.id from users t where t.organizationid =  '%s'"%InitDefaultPara.orgInit['DftWangGeOrgId']),CommonIntf.getDbQueryResult(dbCommand="select t.name from users t where t.organizationid =  '%s'"%InitDefaultPara.orgInit['DftWangGeOrgId']).decode('utf-8'))
        issueParam['ownerOrg.id'] =  InitDefaultPara.orgInit['DftWangGeOrgId']
        issueParam['safeProductionEnterprise.mobileNumber'] = random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8))
 
        ret = MbXunJianIntf.xunJianAdd(param=issueParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, '企业信息新增失败')
        Time.wait(1)  
        
        #新增隐患项 
        riskRemarkParam = copy.deepcopy(XunJianPara.enterpriseObject) 
        riskRemarkParam['riskRemark.riskRemarkName'] = '严重隐患备注项%s'%CommonUtil.createRandomString()
        riskRemarkParam['riskRemark.level.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='隐患等级', displayName='不合格') 
        riskRemarkParam['riskRemark.isEnable'] = '1'
        riskRemarkParam['mode'] = 'add'
        riskRemarkParam['riskRemark.riskmarkerType'] = 0 
        riskRemarkParam['riskRemark.orgId.id'] = orgInit['DftJieDaoOrgId']
        riskRemarkParam['isSubmit'] = 'true'  #是否启用：是-true  否-false
        responseDict = XunJianIntf.add_riskRemark(riskRemarkParam, username=userInit['DftShiUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增隐患项失败')      
        
         
#         #新增巡检记录
        recordParam = copy.deepcopy(MbXunJianPara.addXunJianRecord)
        recordParam['inspection.inspectAddress'] = issueParam['safeProductionEnterprise.address']
        recordParam['inspection.limitTime'] = Time.getCurrentDate()
        recordParam['inspection.recordType'] = 0 #（0巡检  1复查）
        recordParam['inspection.inspectResult'] = 0
        recordParam['inspection.inspectTime'] = Time.getCurrentDate()
        recordParam['inspection.inspectUserId'] =  CommonIntf.getDbQueryResult(dbCommand="select t.id from users t where t.organizationid =  '%s'"%InitDefaultPara.orgInit['DftShiOrgId'])
        recordParam['inspection.orgId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        recordParam['riskRemarkIds'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from riskremarks t where t.riskremarkname  = '%s'"%riskRemarkParam['riskRemark.riskRemarkName'])
        recordParam['inspectionRecord.enterprise.id'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from safeproductionenterprise t where t.name =  '%s'"%issueParam['safeProductionEnterprise.name'])
        recordParam['inspection.inspectName'] =  InitDefaultPara.userInit['DftShiUserXM']
        responseDict = MbXunJianIntf.addXunJianRecord(recordParam,username=userInit['DftShiUser'], password='11111111')
        self.assertTrue(responseDict, '新增巡检记录失败')   

                
            
        #检查巡检记录是否新增成功
        checkParam = copy.deepcopy(MbXunJianPara.check_record)
        checkParam['inspectionRecordVo.recordType'] = recordParam['inspection.recordType']
        checkParam['inspectionRecordVo.enterpriseId'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from safeproductionenterprise t where t.name =  '%s'"%issueParam['safeProductionEnterprise.name'])
        checkParam['inspectionRecordVo.orgId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        
        #检查参数
        companyDict = copy.deepcopy(MbXunJianPara.recordAdress)
        companyDict['address'] = recordParam['inspection.inspectAddress']
        # 获取查询参数
        ret = MbXunJianIntf.check_xunjianRecordXq(companyDict, checkParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, '查找到巡检记录详情失败')
        Time.wait(1)
        
        
        #新增复查记录
        checkRecord = copy.deepcopy(MbXunJianPara.reCheck)  
        checkRecord['inspection.inspectResult'] = 0 #0代表检查不合格,1 代表合格
        checkRecord['solveIds'] = recordParam['riskRemarkIds']
        checkRecord['inspection.inspectTime'] = Time.getCurrentDate()
        checkRecord['inspection.inspectUserId'] = recordParam['inspection.inspectUserId']
        checkRecord['inspection.inspectAddress'] = recordParam['inspection.inspectAddress']
        checkRecord['inspection.orgId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        checkRecord['inspectionRecord.enterprise.id'] = recordParam['inspectionRecord.enterprise.id']
        checkRecord['inspectionRecord.recordType'] = recordParam['inspection.recordType']
        checkRecord['inspection.inspectName'] = recordParam['inspection.inspectName']
        checkRecord['inspection.id'] = CommonIntf.getDbQueryResult(dbCommand="select t.id  from inspection t where t.inspectaddress = '%s'"%recordParam['inspection.inspectAddress'])
        ret = MbXunJianIntf.addXunJianReCheck(checkRecord,  username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, '新增复查记录失败')
        Time.wait(1)

        #检查复查记录
        checkRecord2 = copy.deepcopy(MbXunJianPara.check_reCheck)  
        checkRecord2['recordType'] = checkRecord['inspectionRecord.recordType']
        checkRecord2['enterpriseId'] = checkRecord['inspectionRecord.enterprise.id']
        checkRecord2['inspectionId'] =  CommonIntf.getDbQueryResult(dbCommand="select t.id  from inspection t where t.inspectionid = '%s'"%checkRecord['inspection.id'])
        ret = MbXunJianIntf.XunJianReCheck(checkRecord2, checkRecord['inspection.inspectAddress'], username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, '复查记录检查失败')
        Time.wait(1)
        
        
        #高级搜索 
    def testmInspection_004(self):
#         '''巡检--高级搜索 '''
        
        #新增单位信息
        issueParam = copy.deepcopy(MbXunJianPara.addCompanyParam)
        issueParam['safeProductionEnterprise.address'] = '地址%s'%CommonUtil.createRandomString()
        issueParam['safeProductionEnterprise.legalPerson'] = '我在学校'
        issueParam['safeProductionEnterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='企业类型', displayName='规上企业') 
        issueParam['safeProductionEnterprise.isEmphasis'] = 'false'
        issueParam['safeProductionEnterprise.name'] = '巡检%s' % CommonUtil.createRandomString(6)
        issueParam['safeProductionEnterprise.gridPerson'] = '%s-%s'%( CommonIntf.getDbQueryResult(dbCommand="select t.id from users t where t.organizationid =  '%s'"%InitDefaultPara.orgInit['DftWangGeOrgId']),CommonIntf.getDbQueryResult(dbCommand="select t.name from users t where t.organizationid =  '%s'"%InitDefaultPara.orgInit['DftWangGeOrgId']).decode('utf-8'))
        issueParam['ownerOrg.id'] =  InitDefaultPara.orgInit['DftWangGeOrgId']
        issueParam['safeProductionEnterprise.mobileNumber'] = random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8))
 
        ret = MbXunJianIntf.xunJianAdd(param=issueParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, '第一条企业信息新增失败')
        Time.wait(1)  
        
        #新增单位信息
        issueParam2 = copy.deepcopy(MbXunJianPara.addCompanyParam)
        issueParam2['safeProductionEnterprise.address'] = '地址%s'%CommonUtil.createRandomString()
        issueParam2['safeProductionEnterprise.legalPerson'] = '我在学校2'
        issueParam2['safeProductionEnterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='企业类型', displayName='规上企业') 
        issueParam2['safeProductionEnterprise.isEmphasis'] = 'false'
        issueParam2['safeProductionEnterprise.name'] = '巡检%s' % CommonUtil.createRandomString(6)
        issueParam2['safeProductionEnterprise.gridPerson'] = '%s-%s'%( CommonIntf.getDbQueryResult(dbCommand="select t.id from users t where t.organizationid =  '%s'"%InitDefaultPara.orgInit['DftWangGeOrgId']),CommonIntf.getDbQueryResult(dbCommand="select t.name from users t where t.organizationid =  '%s'"%InitDefaultPara.orgInit['DftWangGeOrgId']).decode('utf-8'))
        issueParam2['ownerOrg.id'] =  InitDefaultPara.orgInit['DftWangGeOrgId']
        issueParam2['safeProductionEnterprise.mobileNumber'] = random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8))
 
        ret = MbXunJianIntf.xunJianAdd(param=issueParam2, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, '第二条企业信息新增失败')
        Time.wait(1)
        
        #高级搜索 根据企业名称查询 期望中的...
        companyDict = copy.deepcopy(MbXunJianPara.checkSearchParam)
        companyDict['name'] = issueParam['safeProductionEnterprise.name']
        ret = MbXunJianIntf.search(issueParam['safeProductionEnterprise.name'],companyDict, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, '搜索期望中企业名称失败')
        Time.wait(1)
        
        #高级搜索 根据企业名称查询  不期望中的...
        companyDict = copy.deepcopy(MbXunJianPara.addOrEditCheck)
        companyDict['name'] = issueParam['safeProductionEnterprise.name']
        ret = MbXunJianIntf.searchNot(issueParam2['safeProductionEnterprise.name'], companyDict,username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertFalse(ret, '搜索不期望中企业名称搜索失败')
        Time.wait(1)
        
        #高级搜索 根据企业地址查询 期望中的...
        companyDict = copy.deepcopy(MbXunJianPara.addOrEditCheck)
        companyDict['address'] = issueParam['safeProductionEnterprise.address']
        ret = MbXunJianIntf.search(issueParam['safeProductionEnterprise.address'], companyDict,username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, '搜索期望中企业地址失败')
        Time.wait(1)

        #高级搜索 根据企业地址查询 不期望中的...
        companyDict = copy.deepcopy(MbXunJianPara.addOrEditCheck)
        companyDict['address'] = issueParam['safeProductionEnterprise.address']
        ret = MbXunJianIntf.searchAddressNot(issueParam2['safeProductionEnterprise.address'], companyDict,username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertFalse(ret, '搜索不期望中企业地址失败')
        Time.wait(1)


        
    
    def tearDown(self):
            pass
if __name__ == "__main__":
    suite = unittest.TestSuite()
#     suite.addTest(XunJian("testmInspection_001")) 
#     suite.addTest(XunJian("testmInspection_002")) 
#     suite.addTest(XunJian("testmInspection_003")) 
    suite.addTest(XunJian("testmInspection_004")) 
    
    results = unittest.TextTestRunner().run(suite)
    pass
            