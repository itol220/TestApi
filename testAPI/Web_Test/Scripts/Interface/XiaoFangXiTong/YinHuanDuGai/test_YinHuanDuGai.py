# -*- coding:UTF-8 -*-
'''
Created on 2016-6-7

@author: chenyan
'''
from __future__ import unicode_literals
import unittest
import copy
from Interface.XiaoFangXiTong.YinHuanDuGai import YinHuanDuGaiPara,\
    YinHuanDuGaiIntf
from COMMON import CommonUtil, Time
from Interface.XiaoFangXiTong.Common import CommonIntf
from Interface.XiaoFangXiTong.Common.InitDefaultPara import orgInit, userInit



class YinHuanDuGai(unittest.TestCase):

    def setUp(self):
#         SystemMgrIntf.initEnv()
        YinHuanDuGaiIntf.deleteAllDanWei()

        pass

    '''
    @功能：单位类型、火灾隐患项配置
    @ chenyan 2016-6-8
    '''
    def testsaveSuperviseType(self):
        # 单位类型配置(居住出租房)——配置县的，县以下自动默认改配置
        Param1 = copy.deepcopy(YinHuanDuGaiPara.saveSuperviseTypeDict) 
        Param1['orgPathName'] = orgInit['DftQuOrg']  #动态获取
        Param1['orgId'] = orgInit['DftQuOrgId']
        Param1['superviseType'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '居住出租房'") 
        responseDict = YinHuanDuGaiIntf.add_SaveSuperviseType(Param1, username='admin', password='admin')
         
        # 火灾隐患项配置
        Param01 = copy.deepcopy(YinHuanDuGaiPara.saveSuperviseType) 
        Param01['superviseTypeItemVo.superviseItemMap'] = ':%s:%s'%(CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_item_id from supervise_item t where t.name ='安全出口疏散通道堵塞'"),CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '督改项等级') and p.displayname = '严重'"))
        Param01['superviseTypeItemVo.superviseItemMap'] = ':%s:%s'%(CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_item_id from supervise_item t where t.name ='安全出口疏散通道数量不足'"),CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '督改项等级') and p.displayname = '一般'"))
        Param01['superviseTypeItemVo.superviseItemMap'] = ':%s:%s'%(CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_item_id from supervise_item t where t.name ='明火灶具未集中使用'"),CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '督改项等级') and p.displayname = '轻微'"))
        Param01['superviseType'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '居住出租房')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%Param1['orgPathName'] )
        Param01['orgId'] = Param1['orgId']
        responseDict = YinHuanDuGaiIntf.add_Type(Param01, username='admin', password='admin')
  
        # 单位类型配置(其他一般单位)——配置县的，县以下自动默认改配置
        Param2 = copy.deepcopy(YinHuanDuGaiPara.saveSuperviseTypeDict) 
        Param2['orgPathName'] = orgInit['DftQuOrg']  #动态获取
        Param2['orgId'] = orgInit['DftQuOrgId']
        Param2['superviseType'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '其他一般单位'")
        responseDict = YinHuanDuGaiIntf.add_SaveSuperviseType(Param2, username='admin', password='admin')
          
        # 火灾隐患项配置
        Param02 = copy.deepcopy(YinHuanDuGaiPara.saveSuperviseType) 
        Param02['superviseTypeItemVo.superviseItemMap'] = ':%s:%s'%(CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_item_id from supervise_item t where t.name ='安全出口疏散通道堵塞'"),CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '督改项等级') and p.displayname = '严重'"))
        Param02['superviseTypeItemVo.superviseItemMap'] = ':%s:%s'%(CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_item_id from supervise_item t where t.name ='安全出口疏散通道数量不足'"),CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '督改项等级') and p.displayname = '一般'"))
        Param02['superviseTypeItemVo.superviseItemMap'] = ':%s:%s'%(CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_item_id from supervise_item t where t.name ='明火灶具未集中使用'"),CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '督改项等级') and p.displayname = '轻微'"))
        Param02['superviseType'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%Param2['orgPathName'] )
        Param02['orgId'] = Param2['orgId']
        responseDict = YinHuanDuGaiIntf.add_Type(Param02, username='admin', password='admin')
   
        # 单位类型配置(小场所通用)——配置县的，县以下自动默认改配置
        Param3 = copy.deepcopy(YinHuanDuGaiPara.saveSuperviseTypeDict) 
        Param3['orgPathName'] = orgInit['DftQuOrg']  #动态获取
        Param3['orgId'] = orgInit['DftQuOrgId']
        Param3['superviseType'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '小场所通用'")
        responseDict = YinHuanDuGaiIntf.add_SaveSuperviseType(Param3, username='admin', password='admin')
            
        # 火灾隐患项配置
        Param03 = copy.deepcopy(YinHuanDuGaiPara.saveSuperviseType) 
        Param03['superviseTypeItemVo.superviseItemMap'] = ':%s:%s'%(CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_item_id from supervise_item t where t.name ='安全出口疏散通道堵塞'"),CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '督改项等级') and p.displayname = '严重'"))
        Param03['superviseTypeItemVo.superviseItemMap'] = ':%s:%s'%(CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_item_id from supervise_item t where t.name ='安全出口疏散通道数量不足'"),CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '督改项等级') and p.displayname = '一般'"))
        Param03['superviseTypeItemVo.superviseItemMap'] = ':%s:%s'%(CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_item_id from supervise_item t where t.name ='明火灶具未集中使用'"),CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '督改项等级') and p.displayname = '轻微'"))
        Param03['superviseType'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '小场所通用')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%Param3['orgPathName'] )
        Param03['orgId'] = Param3['orgId']
        responseDict = YinHuanDuGaiIntf.add_Type(Param03, username='admin', password='admin')
            
        # 单位类型配置(社会福利机构)——配置县的，县以下自动默认改配置
        Param4 = copy.deepcopy(YinHuanDuGaiPara.saveSuperviseTypeDict) 
        Param4['orgPathName'] = orgInit['DftQuOrg']  #动态获取
        Param4['orgId'] = orgInit['DftQuOrgId']
        Param4['superviseType'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '社会福利机构'")
        responseDict = YinHuanDuGaiIntf.add_SaveSuperviseType(Param4, username='admin', password='admin')
            
        # 火灾隐患项配置
        Param04 = copy.deepcopy(YinHuanDuGaiPara.saveSuperviseType) 
        Param04['superviseTypeItemVo.superviseItemMap'] = ':%s:%s'%(CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_item_id from supervise_item t where t.name ='安全出口疏散通道堵塞'"),CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '督改项等级') and p.displayname = '严重'"))
        Param04['superviseTypeItemVo.superviseItemMap'] = ':%s:%s'%(CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_item_id from supervise_item t where t.name ='安全出口疏散通道数量不足'"),CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '督改项等级') and p.displayname = '一般'"))
        Param04['superviseTypeItemVo.superviseItemMap'] = ':%s:%s'%(CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_item_id from supervise_item t where t.name ='明火灶具未集中使用'"),CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '督改项等级') and p.displayname = '轻微'"))
        Param04['superviseType'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '社会福利机构')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%Param4['orgPathName'] )
        Param04['orgId'] = Param4['orgId']
        responseDict = YinHuanDuGaiIntf.add_Type(Param04, username='admin', password='admin')

         
        pass 

    '''
    @功能：新增、修改、删除单位
    @ chenyan 2016-6-13
    '''
    def testFireCompany(self):
        """新增、修改、删除单位"""
        Param = copy.deepcopy(YinHuanDuGaiPara.fireCompanyDict) 
        Param['mode'] = 'add'  
        Param['fireCompanyInfo.createDept'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from ORGANIZATIONS t where t.Orgname='%s'"%orgInit['DftWangGeOrg1']) 
        Param['fireCompanyInfo.importOrAdd'] = '1'
        Param['fireCompanyInfo.orgPathName'] = '%s%s%s%s%s'%(orgInit['DftShiOrg'],orgInit['DftQuOrg'],orgInit['DftJieDaoOrg'],orgInit['DftSheQuOrg'],orgInit['DftWangGeOrg1'])
        Param['fireCompanyInfo.companyName'] = '测试单位%s'%CommonUtil.createRandomString()
        Param['fireCompanyInfo.orgid'] = Param['fireCompanyInfo.createDept']
        Param['companySuperviseTypeIsChange'] = 'true'
        Param['fireCompanyInfo.superviseTypeName'] = '其他一般单位'
        Param['fireCompanyInfo.superviseType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg'])
        Param['fireCompanyInfo.address'] = '测试地址'
        Param['fireCompanyInfo.manger'] = '测试姓名'
        Param['fireCompanyInfo.managerTelephone'] = '18710000000'
        Param['fireCompanyInfo.rentHousePerson'] = '0'
        Param['fireCompanyInfo.industrialCatalogue'] = CommonIntf.getDbQueryResult(dbCommand = "select t.code from fire_company_type t where t.name='电器'")  #行业类别
        Param['businessLicense'] = '1'
        Param['firelicense'] = '1'
        responseDict = YinHuanDuGaiIntf.addOrEdit_fireCompany(Param, username=userInit['DftWangGeUser1'], password='11111111')

        checkParam = copy.deepcopy(YinHuanDuGaiPara.checkFireCompanyDict) 
        checkParam['companyName'] = Param['fireCompanyInfo.companyName'] 
        checkParam['fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param['fireCompanyInfo.companyName'])
        responseDict = YinHuanDuGaiIntf.check_fireCompany(checkParam,orgId=Param['fireCompanyInfo.createDept'], levelShow='1', username=userInit['DftWangGeUser1'], password='11111111')

        editParam = copy.deepcopy(YinHuanDuGaiPara.fireCompanyDict) 
        editParam['mode'] = 'edit'  
        editParam['fireCompanyInfo.fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param['fireCompanyInfo.companyName'])
        editParam['fireCompanyInfo.updateDept'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from ORGANIZATIONS t where t.Orgname='%s'"%orgInit['DftWangGeOrg1']) 
        editParam['fireCompanyInfo.importOrAdd'] = '1'
        editParam['fireCompanyInfo.orgPathName'] = Param['fireCompanyInfo.orgPathName']
        editParam['fireCompanyInfo.companyName'] = '修改测试单位%s'%CommonUtil.createRandomString()
        editParam['fireCompanyInfo.orgid'] = Param['fireCompanyInfo.createDept']
        editParam['companySuperviseTypeIsChange'] = 'true'
        editParam['fireCompanyInfo.superviseTypeName'] = '其他一般单位'
        editParam['fireCompanyInfo.superviseType.id'] = Param['fireCompanyInfo.superviseType.id'] 
        editParam['fireCompanyInfo.address'] = '修改测试地址'
        editParam['fireCompanyInfo.manger'] = '修改测试姓名'
        editParam['fireCompanyInfo.managerTelephone'] = '18710000000'
        editParam['fireCompanyInfo.rentHousePerson'] = '0'
        editParam['fireCompanyInfo.industrialCatalogue'] = CommonIntf.getDbQueryResult(dbCommand = "select t.code from fire_company_type t where t.name='电器'")  #行业类别
        editParam['businessLicense'] = '1'
        editParam['firelicense'] = '1'
        responseDict = YinHuanDuGaiIntf.addOrEdit_fireCompany(editParam,  username=userInit['DftWangGeUser1'], password='11111111')

        deleteParam = copy.deepcopy(YinHuanDuGaiPara.deleteFireCompanyDict) 
        deleteParam['fireCompanyInfo.fireCompanyInfoId'] = editParam['fireCompanyInfo.fireCompanyInfoId']  
        deleteParam['fireCompanyInfo.updateDept'] = editParam['fireCompanyInfo.updateDept']
        responseDict = YinHuanDuGaiIntf.delete_fireCompany(deleteParam,  username=userInit['DftWangGeUser1'], password='11111111')
 
        checkParam = copy.deepcopy(YinHuanDuGaiPara.checkFireCompanyDict) 
        checkParam['fireCompanyInfoId'] = deleteParam['fireCompanyInfo.fireCompanyInfoId']
        responseDict = YinHuanDuGaiIntf.check_fireCompany(checkParam,orgId=Param['fireCompanyInfo.createDept'],levelShow='1', username=userInit['DftWangGeUser1'], password='11111111')
        self.assertFalse(responseDict, '删除的单位在列表中依然存在，删除失败')

        pass

    '''
    @功能：搜索单位
    @ chenyan 2016-6-13
    '''
    def testFireCompany_search(self):
        """搜索单位"""
        Param1 = copy.deepcopy(YinHuanDuGaiPara.fireCompanyDict) 
        Param1['mode'] = 'add'  
        Param1['fireCompanyInfo.createDept'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from ORGANIZATIONS t where t.Orgname='%s'"%orgInit['DftWangGeOrg1']) 
        Param1['fireCompanyInfo.importOrAdd'] = '1'
        Param1['fireCompanyInfo.orgPathName'] = '%s%s%s%s%s'%(orgInit['DftShiOrg'],orgInit['DftQuOrg'],orgInit['DftJieDaoOrg'],orgInit['DftSheQuOrg'],orgInit['DftWangGeOrg1'])
        Param1['fireCompanyInfo.companyName'] = '测试单位%s'%CommonUtil.createRandomString()
        Param1['fireCompanyInfo.orgid'] = Param1['fireCompanyInfo.createDept']
        Param1['companySuperviseTypeIsChange'] = 'true'
        Param1['fireCompanyInfo.superviseTypeName'] = '其他一般单位'
        Param1['fireCompanyInfo.superviseType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg'])
        Param1['fireCompanyInfo.address'] = '测试地址'
        Param1['fireCompanyInfo.manger'] = '测试姓名'
        Param1['fireCompanyInfo.managerTelephone'] = '18710000000'
        Param1['fireCompanyInfo.rentHousePerson'] = '0'
        Param1['fireCompanyInfo.industrialCatalogue'] = CommonIntf.getDbQueryResult(dbCommand = "select t.code from fire_company_type t where t.name='电器'")  #行业类别
        Param1['businessLicense'] = '1'
        Param1['firelicense'] = '1'
        responseDict = YinHuanDuGaiIntf.addOrEdit_fireCompany(Param1, username=userInit['DftWangGeUser1'], password='11111111')

        Param2 = copy.deepcopy(YinHuanDuGaiPara.fireCompanyDict) 
        Param2['mode'] = 'add'  
        Param2['fireCompanyInfo.createDept'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from ORGANIZATIONS t where t.Orgname='%s'"%orgInit['DftWangGeOrg1']) 
        Param2['fireCompanyInfo.importOrAdd'] = '1'
        Param2['fireCompanyInfo.orgPathName'] = '%s%s%s%s%s'%(orgInit['DftShiOrg'],orgInit['DftQuOrg'],orgInit['DftJieDaoOrg'],orgInit['DftSheQuOrg'],orgInit['DftWangGeOrg1'])
        Param2['fireCompanyInfo.companyName'] = '测试单位%s'%CommonUtil.createRandomString()
        Param2['fireCompanyInfo.orgid'] = Param2['fireCompanyInfo.createDept']
        Param2['companySuperviseTypeIsChange'] = 'true'
        Param2['fireCompanyInfo.superviseTypeName'] = '其他一般单位'
        Param2['fireCompanyInfo.superviseType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg'])
        Param2['fireCompanyInfo.address'] = '测试地址'
        Param2['fireCompanyInfo.manger'] = '测试姓名'
        Param2['fireCompanyInfo.managerTelephone'] = '18710000000'
        Param2['fireCompanyInfo.rentHousePerson'] = '0'
        Param2['fireCompanyInfo.industrialCatalogue'] = CommonIntf.getDbQueryResult(dbCommand = "select t.code from fire_company_type t where t.name='电器'")  #行业类别
        Param2['businessLicense'] = '1'
        Param2['firelicense'] = '1'
        responseDict = YinHuanDuGaiIntf.addOrEdit_fireCompany(Param2, username=userInit['DftWangGeUser1'], password='11111111')
 
        Param3 = copy.deepcopy(YinHuanDuGaiPara.fireCompanyDict) 
        Param3['mode'] = 'add'  
        Param3['fireCompanyInfo.createDept'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from ORGANIZATIONS t where t.Orgname='%s'"%orgInit['DftWangGeOrg1']) 
        Param3['fireCompanyInfo.importOrAdd'] = '1'
        Param3['fireCompanyInfo.orgPathName'] = '%s%s%s%s%s'%(orgInit['DftShiOrg'],orgInit['DftQuOrg'],orgInit['DftJieDaoOrg'],orgInit['DftSheQuOrg'],orgInit['DftWangGeOrg1'])
        Param3['fireCompanyInfo.companyName'] = '测试单位%s'%CommonUtil.createRandomString()
        Param3['fireCompanyInfo.orgid'] = Param3['fireCompanyInfo.createDept']
        Param3['companySuperviseTypeIsChange'] = 'true'
        Param3['fireCompanyInfo.superviseTypeName'] = '其他一般单位'
        Param3['fireCompanyInfo.superviseType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg'])
        Param3['fireCompanyInfo.address'] = '测试地址'
        Param3['fireCompanyInfo.manger'] = '测试姓名'
        Param3['fireCompanyInfo.managerTelephone'] = '18710000000'
        Param3['fireCompanyInfo.rentHousePerson'] = '0'
        Param3['fireCompanyInfo.industrialCatalogue'] = CommonIntf.getDbQueryResult(dbCommand = "select t.code from fire_company_type t where t.name='电器'")  #行业类别
        Param3['businessLicense'] = '1'
        Param3['firelicense'] = '1'
        responseDict = YinHuanDuGaiIntf.addOrEdit_fireCompany(Param3, username=userInit['DftWangGeUser1'], password='11111111')
         
        searchParam = copy.deepcopy(YinHuanDuGaiPara.checkFireCompanyDict) 
        searchParam['companyName'] = Param3['fireCompanyInfo.companyName'] 
        searchParam['fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param3['fireCompanyInfo.companyName'])
        responseDict = YinHuanDuGaiIntf.check_fireCompany(searchParam,orgId=Param3['fireCompanyInfo.createDept'],companyName=Param3['fireCompanyInfo.companyName'] , levelShow='1',username=userInit['DftWangGeUser1'], password='11111111')
        pass

    '''
    @功能：导入单位   
    @ chenyan 2016-6-13
    '''
#     def testDanWeiImport(self):
#         """单位信息 导入"""
#           
#         importHuJiparam = copy.deepcopy(YinHuanDuGaiPara.Data)
#         importHuJiparam['dataType']='companyInfoData'
#         importHuJiparam['templates']='COMPANYINFODATA'
#         files = {'upload': ('test.xls', open('C:/autotest_file/importDanWei.xls', 'rb'),'applicationnd.ms-excel')}
#         ret = YinHuanDuGaiIntf.import_DanWei(importHuJiparam, files=files,username=userInit['DftWangGeUser1'], password='11111111')         
#            
#         checkParam = copy.deepcopy(YinHuanDuGaiPara.checkFireCompanyDict) 
#         checkParam['companyName'] = '导入单位测试'   
# #         checkParam['fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%checkParam['companyName'])
#         responseDict = YinHuanDuGaiIntf.check_fireCompany(checkParam,orgId=orgInit['DftWangGeOrgId1'], levelShow='1', username=userInit['DftWangGeUser1'], password='11111111')
#         self.assertTrue(responseDict, '查找单位失败')
# 
# #         downLoadparam = copy.deepcopy(YinHuanDuGaiPara.dlDanWeiData)
# #         downLoadparam['orgId']=orgInit['DftWangGeOrgId1']
# #         print downLoadparam
# #         response = YinHuanDuGaiIntf.downLoad_DanWei(downLoadparam, username=userInit['DftWangGeUser1'], password='11111111')         
# #         print type(response)
# #         with open("C:/autotest_file/downLoadDanWei.xls", "wb") as code:
# #             code.write(response.content)
# #               
# #         ret = CommonUtil.checkExcelCellValue(checkParam['companyName'], 'downLoadDanWei.xls','单位信息', 'B4')          
# #         self.assertTrue(ret, '单元格内容匹配失败')
# 
#         pass

    '''
    @功能：转移单位
    @ chenyan 2016-6-13
    '''
    def testFireCompany_Change(self):
        """转移单位"""
        #新增单位
        Param = copy.deepcopy(YinHuanDuGaiPara.fireCompanyDict) 
        Param['mode'] = 'add'  
        Param['fireCompanyInfo.createDept'] = orgInit['DftWangGeOrgId1'] 
        Param['fireCompanyInfo.importOrAdd'] = '1'
        Param['fireCompanyInfo.orgPathName'] = '%s%s%s%s%s'%(orgInit['DftShiOrg'],orgInit['DftQuOrg'],orgInit['DftJieDaoOrg'],orgInit['DftSheQuOrg'],orgInit['DftWangGeOrg1'])
        Param['fireCompanyInfo.companyName'] = '测试单位%s'%CommonUtil.createRandomString()
        Param['fireCompanyInfo.orgid'] = Param['fireCompanyInfo.createDept']
        Param['companySuperviseTypeIsChange'] = 'true'
        Param['fireCompanyInfo.superviseTypeName'] = '其他一般单位'
        Param['fireCompanyInfo.superviseType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg']) 
        Param['fireCompanyInfo.address'] = '测试地址'
        Param['fireCompanyInfo.manger'] = '测试姓名'
        Param['fireCompanyInfo.managerTelephone'] = '18710000000'
        Param['fireCompanyInfo.rentHousePerson'] = '0'
        Param['fireCompanyInfo.industrialCatalogue'] = CommonIntf.getDbQueryResult(dbCommand = "select t.code from fire_company_type t where t.name='电器'")  #行业类别
        Param['businessLicense'] = '1'
        Param['firelicense'] = '1'
        responseDict = YinHuanDuGaiIntf.addOrEdit_fireCompany(Param, username=userInit['DftWangGeUser1'], password='11111111')
        
        #转移单位
        changeParam = copy.deepcopy(YinHuanDuGaiPara.changeFireCompanyDict) 
        changeParam['companyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param['fireCompanyInfo.companyName'])
        changeParam['orgId'] = Param['fireCompanyInfo.createDept']
        changeParam['orgPangtId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from ORGANIZATIONS t where t.Orgname='%s'"%orgInit['DftSheQuOrg'])   #上一层级orgid
        changeParam['targetOrgId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from ORGANIZATIONS t where t.Orgname='%s'"%orgInit['DftWangGeOrg'])  #转移的orgid
        responseDict = YinHuanDuGaiIntf.change_fireCompany(changeParam, username=userInit['DftWangGeUser1'], password='11111111')

        #网格1下未搜到
        checkParam = copy.deepcopy(YinHuanDuGaiPara.checkFireCompanyDict) 
        checkParam['companyName'] = Param['fireCompanyInfo.companyName'] 
        checkParam['fireCompanyInfoId'] = changeParam['companyInfoId']
        responseDict = YinHuanDuGaiIntf.check_fireCompany(checkParam,orgId=Param['fireCompanyInfo.createDept'], levelShow='1',username=userInit['DftWangGeUser1'], password='11111111')
        self.assertFalse(responseDict, '转移的单位在当前账号下依然存在，转移失败')
         
        #网格下可以搜到转移单位信息
        checkParam = copy.deepcopy(YinHuanDuGaiPara.checkFireCompanyDict) 
        checkParam['companyName'] = '%s[测试自动化网格1]'%Param['fireCompanyInfo.companyName']
        checkParam['fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%checkParam['companyName'])
        responseDict = YinHuanDuGaiIntf.check_fireCompany(checkParam,orgId=orgInit['DftWangGeOrgId'] , levelShow='1',username=userInit['DftWangGeUser'], password='11111111')

    '''
    @功能：单位添加日常检查 
    @ chenyan 2016-6-14
    '''
    def testSaveFiretrapSupervise(self):
        """单位添加日常检查"""
        #新增单位
        Param = copy.deepcopy(YinHuanDuGaiPara.fireCompanyDict) 
        Param['mode'] = 'add'  
        Param['fireCompanyInfo.createDept'] = orgInit['DftWangGeOrgId1'] 
        Param['fireCompanyInfo.importOrAdd'] = '1'
        Param['fireCompanyInfo.orgPathName'] = '%s%s%s%s%s'%(orgInit['DftShiOrg'],orgInit['DftQuOrg'],orgInit['DftJieDaoOrg'],orgInit['DftSheQuOrg'],orgInit['DftWangGeOrg1'])
        Param['fireCompanyInfo.companyName'] = '测试单位%s'%CommonUtil.createRandomString()
        Param['fireCompanyInfo.orgid'] = Param['fireCompanyInfo.createDept']
        Param['companySuperviseTypeIsChange'] = 'true'
        Param['fireCompanyInfo.superviseTypeName'] = '其他一般单位'
        Param['fireCompanyInfo.superviseType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg']) 
        Param['fireCompanyInfo.address'] = '测试地址'
        Param['fireCompanyInfo.manger'] = '测试姓名'
        Param['fireCompanyInfo.managerTelephone'] = '18710000000'
        Param['fireCompanyInfo.rentHousePerson'] = '0'
        Param['fireCompanyInfo.industrialCatalogue'] = CommonIntf.getDbQueryResult(dbCommand = "select t.code from fire_company_type t where t.name='电器'")  #行业类别
        Param['businessLicense'] = '1'
        Param['firelicense'] = '1'
        responseDict = YinHuanDuGaiIntf.addOrEdit_fireCompany(Param, username=userInit['DftWangGeUser1'], password='11111111')

        #添加日常检查
        Param1 = copy.deepcopy(YinHuanDuGaiPara.saveFiretrapSuperviseDict) 
        Param1['isReportFlag'] = 0 
        Param1['calCheckResult'] = 'flag'
        Param1['firetrapSupervise.superviseNo'] = 'DG2016061500008'
        Param1['companyName'] = Param['fireCompanyInfo.companyName']
        Param1['checkDate'] = Time.getCurrentDate()
        Param1['firetrapSupervise.checkAddress'] = Param['fireCompanyInfo.address'] 
        Param1['firetrapSupervise.checkPlace'] = Param['fireCompanyInfo.companyName']
        Param1['checkItemIndexs'] = '1.'
        Param1['checkItemCodes'] = '%s#'% CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_item_id from supervise_type_item t where t.supervise_item_id =%s and t.supervise_type_id =%s"%(CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_item_id from supervise_item t where t.name ='安全出口疏散通道数量不足'"),CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg'] )))  #隐患项
        Param1['firetrapSupervise.reviseDate'] = Time.getCurrentDate()  #整改日期
        Param1['firetrapSupervise.manageName'] = Param['fireCompanyInfo.manger']
        Param1['companyCheckRecord_assignUserNameVo'] = userInit['DftJieDaoUserXM']
        Param1['companyCheckRecord_assignUserVo'] = userInit['DftJieDaoUser']
        Param1['companyCheckRecord_levelOrg'] = '片组片格'
        Param1['companyCheckRecordlevel'] = '村（社区）'
        Param1['companyCheckRecordOrgId'] = orgInit['DftJieDaoOrgId']
        Param1['user.userName'] = userInit['DftJieDaoUser']
        Param1['user.name'] = userInit['DftJieDaoUserXM']
        Param1['user.organization.id'] = orgInit['DftJieDaoOrgId']
        Param1['calculationMode'] = 0
        Param1['firetrapSupervise.signDate'] = Time.getCurrentDate()
        Param1['firetrapSupervise.superviseUserName'] = userInit['DftWangGeUserXM1'] 
        Param1['firetrapSupervise.superviseUser'] = userInit['DftWangGeUser1'] 
        Param1['firetrapSupervise.superviseDate'] = Time.getCurrentDate()
        Param1['operateMode'] = 'add'
        Param1['firetrapSupervise.superviseState'] = 1
        Param1['firetrapSupervise.updateDept'] = orgInit['DftWangGeOrgId1']
        Param1['firetrapSupervise.createDept'] = orgInit['DftWangGeOrgId1']
        Param1['superviseTypeId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg'] )
        Param1['companyCheckRecord.companyManager'] = Param['fireCompanyInfo.manger']
        Param1['companyCheckRecord.assignUser'] = userInit['DftWangGeUser1'] 
        Param1['companyCheckRecord.assignDept'] = orgInit['DftWangGeOrgId1']
        Param1['companyCheckRecord.checkType'] = 1
        Param1['companyCheckRecord.checkUser'] = userInit['DftWangGeUser1'] 
        Param1['companyCheckRecord.fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param['fireCompanyInfo.companyName']) #被检查单位的id
        Param1['companyCheckRecord.checkDate'] = Time.getCurrentDate()
        Param1['checkResult'] = '一般'
        responseDict = YinHuanDuGaiIntf.saveFiretrapSupervise(Param1, username=userInit['DftWangGeUser1'], password='11111111')

        #检查日常量化模块下是否存在新增检查记录
        checkParam = copy.deepcopy(YinHuanDuGaiPara.checkSaveFiretrapSuperviseDict) 
        checkParam['companyName'] = Param['fireCompanyInfo.companyName'] 
        checkParam['fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param['fireCompanyInfo.companyName'])
        responseDict = YinHuanDuGaiIntf.check_saveFiretrapSupervise(checkParam,orgId=Param['fireCompanyInfo.createDept'], allStateSearch='0',publicString='1',username=userInit['DftWangGeUser1'], password='11111111')
        self.assertTrue(responseDict, '检查失败')


    '''
    @功能：单位添加举报检查 
    @ chenyan 2016-6-14
    '''
    def testSaveComplaintHandle(self):
        """单位添加举报检查"""
        #新增单位
        Param = copy.deepcopy(YinHuanDuGaiPara.fireCompanyDict) 
        Param['mode'] = 'add'  
        Param['fireCompanyInfo.createDept'] = orgInit['DftWangGeOrgId1'] 
        Param['fireCompanyInfo.importOrAdd'] = '1'
        Param['fireCompanyInfo.orgPathName'] = '%s%s%s%s%s'%(orgInit['DftShiOrg'],orgInit['DftQuOrg'],orgInit['DftJieDaoOrg'],orgInit['DftSheQuOrg'],orgInit['DftWangGeOrg1'])
        Param['fireCompanyInfo.companyName'] = '测试单位%s'%CommonUtil.createRandomString()
        Param['fireCompanyInfo.orgid'] = Param['fireCompanyInfo.createDept']
        Param['companySuperviseTypeIsChange'] = 'true'
        Param['fireCompanyInfo.superviseTypeName'] = '其他一般单位'
        Param['fireCompanyInfo.superviseType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg']) 
        Param['fireCompanyInfo.address'] = '测试地址'
        Param['fireCompanyInfo.manger'] = '测试姓名'
        Param['fireCompanyInfo.managerTelephone'] = '18710000000'
        Param['fireCompanyInfo.rentHousePerson'] = '0'
        Param['fireCompanyInfo.industrialCatalogue'] = CommonIntf.getDbQueryResult(dbCommand = "select t.code from fire_company_type t where t.name='电器'")  #行业类别
        Param['businessLicense'] = '1'
        Param['firelicense'] = '1'
        responseDict = YinHuanDuGaiIntf.addOrEdit_fireCompany(Param, username=userInit['DftWangGeUser1'], password='11111111')

        #新增单位举报检查
        Param1 = copy.deepcopy(YinHuanDuGaiPara.saveComplaintHandleDict) 
        Param1['companyCheckRecord.source'] = 1
        Param1['complaintHandleInfo.complaintHandleNo'] = 'JB2016061400009'
        Param1['complaintHandleInfo.reporterName'] = '测试'
        Param1['complaintHandleInfo.reporterTelephone'] = '1234567'
        Param1['complaintHandleInfo.compliantManner'] = 0   #举报投诉形式
        Param1['complaintHandleInfo.handleDate'] = Time.getCurrentTime()
        Param1['complaintHandleInfo.handleName'] = '受理人员'
        Param1['complaintHandleInfo.complaintContent'] = '受理内容'
        Param1['companyCheckRecord.fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param['fireCompanyInfo.companyName'])
        Param1['companyCheckRecord.checkType'] = 4
        Param1['companyCheckRecord.dateFrom'] = Time.getCurrentTime()
        Param1['companyCheckRecord.dateTo'] = Time.getCurrentTime()
        responseDict = YinHuanDuGaiIntf.saveComplaintHandle(Param1, username=userInit['DftWangGeUser1'], password='11111111')

        checkParam = copy.deepcopy(YinHuanDuGaiPara.checkSaveFiretrapSuperviseDict) 
        checkParam['fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param['fireCompanyInfo.companyName']) 
        checkParam['companyName'] = Param['fireCompanyInfo.companyName']
        responseDict = YinHuanDuGaiIntf.check_saveFiretrapSupervise(checkParam,orgId=orgInit['DftWangGeOrgId1'] , allStateSearch=0,publicString=4, username=userInit['DftWangGeUser1'], password='11111111')
        self.assertTrue(responseDict, '未检查到举报信息')
        
        pass    


    '''
    @功能：新增、搜索、删除日常检查记录
    @ chenyan 2016-6-16
    '''
    def testFiretrapSupervise(self):
        """新增、搜索、删除日常检查记录"""
        #新增单位1
        Param1 = copy.deepcopy(YinHuanDuGaiPara.fireCompanyDict) 
        Param1['mode'] = 'add'  
        Param1['fireCompanyInfo.createDept'] = orgInit['DftWangGeOrgId1'] 
        Param1['fireCompanyInfo.importOrAdd'] = '1'
        Param1['fireCompanyInfo.orgPathName'] = '%s%s%s%s%s'%(orgInit['DftShiOrg'],orgInit['DftQuOrg'],orgInit['DftJieDaoOrg'],orgInit['DftSheQuOrg'],orgInit['DftWangGeOrg1'])
        Param1['fireCompanyInfo.companyName'] = '测试单位%s'%CommonUtil.createRandomString()
        Param1['fireCompanyInfo.orgid'] = Param1['fireCompanyInfo.createDept']
        Param1['companySuperviseTypeIsChange'] = 'true'
        Param1['fireCompanyInfo.superviseTypeName'] = '其他一般单位'
        Param1['fireCompanyInfo.superviseType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg']) 
        Param1['fireCompanyInfo.address'] = '测试地址'
        Param1['fireCompanyInfo.manger'] = '测试姓名'
        Param1['fireCompanyInfo.managerTelephone'] = '18710000000'
        Param1['fireCompanyInfo.rentHousePerson'] = '0'
        Param1['fireCompanyInfo.industrialCatalogue'] = CommonIntf.getDbQueryResult(dbCommand = "select t.code from fire_company_type t where t.name='电器'")  #行业类别
        Param1['businessLicense'] = '1'
        Param1['firelicense'] = '1'
        responseDict = YinHuanDuGaiIntf.addOrEdit_fireCompany(Param1, username=userInit['DftWangGeUser1'], password='11111111')
 
        #添加日常检查——较好
        Param01 = copy.deepcopy(YinHuanDuGaiPara.saveFiretrapSuperviseDict) 
        Param01['isReportFlag'] = 0 
        Param01['calCheckResult'] = 'flag'
        Param01['firetrapSupervise.superviseNo'] = 'DG2016061500008'
        Param01['companyName'] = Param1['fireCompanyInfo.companyName']
        Param01['checkDate'] = Time.getCurrentDate()
        Param01['firetrapSupervise.checkAddress'] = Param1['fireCompanyInfo.address'] 
        Param01['firetrapSupervise.checkPlace'] = Param1['fireCompanyInfo.companyName']
        Param01['checkItemIndexs'] = '1.'
        Param01['checkItemCodes'] = '%s#'% CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_item_id from supervise_type_item t where t.supervise_item_id =%s and t.supervise_type_id =%s"%(CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_item_id from supervise_item t where t.name ='明火灶具未集中使用'"),CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg'] )))  #隐患项
        Param01['firetrapSupervise.reviseDate'] = Time.getCurrentDate()  #整改日期
        Param01['firetrapSupervise.manageName'] = Param1['fireCompanyInfo.manger']
        Param01['companyCheckRecord_assignUserNameVo'] = userInit['DftJieDaoUserXM']
        Param01['companyCheckRecord_assignUserVo'] = userInit['DftJieDaoUser']
        Param01['companyCheckRecord_levelOrg'] = '片组片格'
        Param01['companyCheckRecordlevel'] = '村（社区）'
        Param01['companyCheckRecordOrgId'] = orgInit['DftJieDaoOrgId']
        Param01['user.userName'] = userInit['DftJieDaoUser']
        Param01['user.name'] = userInit['DftJieDaoUserXM']
        Param01['user.organization.id'] = orgInit['DftJieDaoOrgId']
        Param01['calculationMode'] = 0
        Param01['firetrapSupervise.signDate'] = Time.getCurrentDate()
        Param01['firetrapSupervise.superviseUserName'] = userInit['DftWangGeUserXM1'] 
        Param01['firetrapSupervise.superviseUser'] = userInit['DftWangGeUser1'] 
        Param01['firetrapSupervise.superviseDate'] = Time.getCurrentDate()
        Param01['operateMode'] = 'add'
        Param01['firetrapSupervise.superviseState'] = 1
        Param01['firetrapSupervise.updateDept'] = orgInit['DftWangGeOrgId1']
        Param01['firetrapSupervise.createDept'] = orgInit['DftWangGeOrgId1']
        Param01['superviseTypeId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg'] )
        Param01['companyCheckRecord.companyManager'] = Param1['fireCompanyInfo.manger']
        Param01['companyCheckRecord.assignUser'] = userInit['DftWangGeUser1'] 
        Param01['companyCheckRecord.assignDept'] = orgInit['DftWangGeOrgId1']
        Param01['companyCheckRecord.checkType'] = 1
        Param01['companyCheckRecord.checkUser'] = userInit['DftWangGeUser1'] 
        Param01['companyCheckRecord.fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param1['fireCompanyInfo.companyName']) #被检查单位的id
        Param01['companyCheckRecord.checkDate'] = Time.getCurrentDate()
        Param01['checkResult'] = '较好'
        responseDict = YinHuanDuGaiIntf.saveFiretrapSupervise(Param01, username=userInit['DftWangGeUser1'], password='11111111')

        #新增单位2
        Param2 = copy.deepcopy(YinHuanDuGaiPara.fireCompanyDict) 
        Param2['mode'] = 'add'  
        Param2['fireCompanyInfo.createDept'] = orgInit['DftWangGeOrgId1'] 
        Param2['fireCompanyInfo.importOrAdd'] = '1'
        Param2['fireCompanyInfo.orgPathName'] = '%s%s%s%s%s'%(orgInit['DftShiOrg'],orgInit['DftQuOrg'],orgInit['DftJieDaoOrg'],orgInit['DftSheQuOrg'],orgInit['DftWangGeOrg1'])
        Param2['fireCompanyInfo.companyName'] = '测试单位%s'%CommonUtil.createRandomString()
        Param2['fireCompanyInfo.orgid'] = Param2['fireCompanyInfo.createDept']
        Param2['companySuperviseTypeIsChange'] = 'true'
        Param2['fireCompanyInfo.superviseTypeName'] = '其他一般单位'
        Param2['fireCompanyInfo.superviseType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg']) 
        Param2['fireCompanyInfo.address'] = '测试地址'
        Param2['fireCompanyInfo.manger'] = '测试姓名'
        Param2['fireCompanyInfo.managerTelephone'] = '18710000000'
        Param2['fireCompanyInfo.rentHousePerson'] = '0'
        Param2['fireCompanyInfo.industrialCatalogue'] = CommonIntf.getDbQueryResult(dbCommand = "select t.code from fire_company_type t where t.name='电器'")  #行业类别
        Param2['businessLicense'] = '1'
        Param2['firelicense'] = '1'
        responseDict = YinHuanDuGaiIntf.addOrEdit_fireCompany(Param2, username=userInit['DftWangGeUser1'], password='11111111')

        #添加日常检查——一般
        Param02 = copy.deepcopy(YinHuanDuGaiPara.saveFiretrapSuperviseDict) 
        Param02['isReportFlag'] = 0 
        Param02['calCheckResult'] = 'flag'
        Param02['firetrapSupervise.superviseNo'] = 'DG2016061500008'
        Param02['companyName'] = Param2['fireCompanyInfo.companyName']
        Param02['checkDate'] = Time.getCurrentDate()
        Param02['firetrapSupervise.checkAddress'] = Param2['fireCompanyInfo.address'] 
        Param02['firetrapSupervise.checkPlace'] = Param2['fireCompanyInfo.companyName']
        Param02['checkItemIndexs'] = '1.'
        Param02['checkItemCodes'] = '%s#'% CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_item_id from supervise_type_item t where t.supervise_item_id =%s and t.supervise_type_id =%s"%(CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_item_id from supervise_item t where t.name ='安全出口疏散通道数量不足'"),CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg'] )))  #隐患项
        Param02['firetrapSupervise.reviseDate'] = Time.getCurrentDate()  #整改日期
        Param02['firetrapSupervise.manageName'] = Param2['fireCompanyInfo.manger']
        Param02['companyCheckRecord_assignUserNameVo'] = userInit['DftJieDaoUserXM']
        Param02['companyCheckRecord_assignUserVo'] = userInit['DftJieDaoUser']
        Param02['companyCheckRecord_levelOrg'] = '片组片格'
        Param02['companyCheckRecordlevel'] = '村（社区）'
        Param02['companyCheckRecordOrgId'] = orgInit['DftJieDaoOrgId']
        Param02['user.userName'] = userInit['DftJieDaoUser']
        Param02['user.name'] = userInit['DftJieDaoUserXM']
        Param02['user.organization.id'] = orgInit['DftJieDaoOrgId']
        Param02['calculationMode'] = 0
        Param02['firetrapSupervise.signDate'] = Time.getCurrentDate()
        Param02['firetrapSupervise.superviseUserName'] = userInit['DftWangGeUserXM1'] 
        Param02['firetrapSupervise.superviseUser'] = userInit['DftWangGeUser1'] 
        Param02['firetrapSupervise.superviseDate'] = Time.getCurrentDate()
        Param02['operateMode'] = 'add'
        Param02['firetrapSupervise.superviseState'] = 1
        Param02['firetrapSupervise.updateDept'] = orgInit['DftWangGeOrgId1']
        Param02['firetrapSupervise.createDept'] = orgInit['DftWangGeOrgId1']
        Param02['superviseTypeId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg'] )
        Param02['companyCheckRecord.companyManager'] = Param2['fireCompanyInfo.manger']
        Param02['companyCheckRecord.assignUser'] = userInit['DftWangGeUser1'] 
        Param02['companyCheckRecord.assignDept'] = orgInit['DftWangGeOrgId1']
        Param02['companyCheckRecord.checkType'] = 1
        Param02['companyCheckRecord.checkUser'] = userInit['DftWangGeUser1'] 
        Param02['companyCheckRecord.fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param2['fireCompanyInfo.companyName']) #被检查单位的id
        Param02['companyCheckRecord.checkDate'] = Time.getCurrentDate()
        Param02['checkResult'] = '一般'
        responseDict = YinHuanDuGaiIntf.saveFiretrapSupervise(Param02, username=userInit['DftWangGeUser1'], password='11111111')

        #搜索日常检查记录
        checkParam = copy.deepcopy(YinHuanDuGaiPara.checkSaveFiretrapSuperviseDict) 
        checkParam['companyName'] = Param2['fireCompanyInfo.companyName'] 
        checkParam['fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param2['fireCompanyInfo.companyName'])
        responseDict = YinHuanDuGaiIntf.check_saveFiretrapSupervise(checkParam,companyName=Param2['fireCompanyInfo.companyName'] ,orgId=orgInit['DftWangGeOrgId1'], allStateSearch='1',publicString='1',username=userInit['DftWangGeUser1'], password='11111111')
        self.assertTrue(responseDict, '搜索失败')
        
        #删除日常检查记录
        deleteParam = copy.deepcopy(YinHuanDuGaiPara.deleteSaveFiretrapSuperviseDict) 
        deleteParam['ids'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param1['fireCompanyInfo.companyName'])
        responseDict = YinHuanDuGaiIntf.delete_saveFiretrapSupervise(checkParam,username=userInit['DftWangGeUser1'], password='11111111')

        #检查日常检查记录
        checkParam = copy.deepcopy(YinHuanDuGaiPara.checkSaveFiretrapSuperviseDict) 
        checkParam['companyName'] = Param1['fireCompanyInfo.companyName'] 
        checkParam['fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param1['fireCompanyInfo.companyName'])
        responseDict = YinHuanDuGaiIntf.check_saveFiretrapSupervise(checkParam,orgId=orgInit['DftWangGeOrgId1'], allStateSearch='1',publicString='1',username=userInit['DftWangGeUser1'], password='11111111')
        self.assertFalse(responseDict, '删除的日常检查记录在列表中依然存在，删除失败')


    '''
    @功能：处理日常检查记录
    @ chenyan 2016-6-16
    '''
    def testSaveFiretrapReview(self):
        """处理日常检查记录（三级督改）"""
        #新增单位
        Param = copy.deepcopy(YinHuanDuGaiPara.fireCompanyDict) 
        Param['mode'] = 'add'  
        Param['fireCompanyInfo.createDept'] = orgInit['DftWangGeOrgId1'] 
        Param['fireCompanyInfo.importOrAdd'] = '1'
        Param['fireCompanyInfo.orgPathName'] = '%s%s%s%s%s'%(orgInit['DftShiOrg'],orgInit['DftQuOrg'],orgInit['DftJieDaoOrg'],orgInit['DftSheQuOrg'],orgInit['DftWangGeOrg1'])
        Param['fireCompanyInfo.companyName'] = '测试单位%s'%CommonUtil.createRandomString()
        Param['fireCompanyInfo.orgid'] = Param['fireCompanyInfo.createDept']
        Param['companySuperviseTypeIsChange'] = 'true'
        Param['fireCompanyInfo.superviseTypeName'] = '其他一般单位'
        Param['fireCompanyInfo.superviseType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg']) 
        Param['fireCompanyInfo.address'] = '测试地址'
        Param['fireCompanyInfo.manger'] = '测试姓名'
        Param['fireCompanyInfo.managerTelephone'] = '18710000000'
        Param['fireCompanyInfo.rentHousePerson'] = '0'
        Param['fireCompanyInfo.industrialCatalogue'] = CommonIntf.getDbQueryResult(dbCommand = "select t.code from fire_company_type t where t.name='电器'")  #行业类别
        Param['businessLicense'] = '1'
        Param['firelicense'] = '1'
        responseDict = YinHuanDuGaiIntf.addOrEdit_fireCompany(Param, username=userInit['DftWangGeUser1'], password='11111111')

        #添加日常检查
        Param1 = copy.deepcopy(YinHuanDuGaiPara.saveFiretrapSuperviseDict) 
        Param1['isReportFlag'] = 0 
        Param1['calCheckResult'] = 'flag'
        Param1['firetrapSupervise.superviseNo'] = 'DG2016061700002'
        Param1['companyName'] = Param['fireCompanyInfo.companyName']
        Param1['checkDate'] = Time.getCurrentDate()
        Param1['firetrapSupervise.checkAddress'] = Param['fireCompanyInfo.address'] 
        Param1['firetrapSupervise.checkPlace'] = Param['fireCompanyInfo.companyName']
        Param1['checkItemIndexs'] = '1.'
        Param1['checkItemCodes'] = '%s#'% CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_item_id from supervise_type_item t where t.supervise_item_id =%s and t.supervise_type_id =%s"%(CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_item_id from supervise_item t where t.name ='安全出口疏散通道数量不足'"),CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg'] )))  #隐患项
        Param1['firetrapSupervise.reviseDate'] = Time.getCurrentDate()  #整改日期
        Param1['firetrapSupervise.manageName'] = Param['fireCompanyInfo.manger']
        Param1['companyCheckRecord_assignUserNameVo'] = userInit['DftJieDaoUserXM']
        Param1['companyCheckRecord_assignUserVo'] = userInit['DftJieDaoUser']
        Param1['companyCheckRecord_levelOrg'] = '片组片格'
        Param1['companyCheckRecordlevel'] = '村（社区）'
        Param1['companyCheckRecordOrgId'] = orgInit['DftJieDaoOrgId']
        Param1['user.userName'] = userInit['DftJieDaoUser']
        Param1['user.name'] = userInit['DftJieDaoUserXM']
        Param1['user.organization.id'] = orgInit['DftJieDaoOrgId']
        Param1['calculationMode'] = 0
        Param1['firetrapSupervise.signDate'] = Time.getCurrentDate()
        Param1['firetrapSupervise.superviseUserName'] = userInit['DftWangGeUserXM1'] 
        Param1['firetrapSupervise.superviseUser'] = userInit['DftWangGeUser1'] 
        Param1['firetrapSupervise.superviseDate'] = Time.getCurrentDate()
        Param1['operateMode'] = 'add'
        Param1['firetrapSupervise.superviseState'] = 1
        Param1['firetrapSupervise.updateDept'] = orgInit['DftWangGeOrgId1']
        Param1['firetrapSupervise.createDept'] = orgInit['DftWangGeOrgId1']
        Param1['superviseTypeId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg'] )
        Param1['companyCheckRecord.companyManager'] = Param['fireCompanyInfo.manger']
        Param1['companyCheckRecord.assignUser'] = userInit['DftWangGeUser1'] 
        Param1['companyCheckRecord.assignDept'] = orgInit['DftWangGeOrgId1']
        Param1['companyCheckRecord.checkType'] = 1
        Param1['companyCheckRecord.checkUser'] = userInit['DftWangGeUser1'] 
        Param1['companyCheckRecord.fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param['fireCompanyInfo.companyName']) #被检查单位的id
        Param1['companyCheckRecord.checkDate'] = Time.getCurrentDate()
        Param1['checkResult'] = '一般'
        responseDict = YinHuanDuGaiIntf.saveFiretrapSupervise(Param1, username=userInit['DftWangGeUser1'], password='11111111')

        #复查
        reviewParam1 = copy.deepcopy(YinHuanDuGaiPara.saveFiretrapReviewDict) 
        reviewParam1['calculationMode'] = 0
        reviewParam1['superviseState'] = 1
        reviewParam1['firetrapReview.firetrapReviewNo'] = 'FC2016061700002'
        reviewParam1['companyName'] = Param['fireCompanyInfo.companyName']
        reviewParam1['superviseNo'] = Param1['firetrapSupervise.superviseNo']
        reviewParam1['reviewItems[0].id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_item_id from supervise_type_item t where t.supervise_item_id =%s and t.supervise_type_id =%s"%(CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_item_id from supervise_item t where t.name ='安全出口疏散通道数量不足'"),CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg'] )))  #隐患项
        reviewParam1['reviewItems[0].checkItemId'] = CommonIntf.getDbQueryResult(dbCommand = "select  p.check_item_id from check_item  p where p.firetrap_supervise_id=%s"%CommonIntf.getDbQueryResult(dbCommand = "select t.firetrap_supervise_id from firetrap_supervise t where t.check_place='%s'"%Param['fireCompanyInfo.companyName'])) 
        reviewParam1['reviewItems[0].state'] = 1
        reviewParam1['firetrapReview.reviseState'] = 1 
        reviewParam1['firetrapReview.reviewState'] = 1
        reviewParam1['firetrapReview.reviewPersonName'] = userInit['DftWangGeUserXM1']
        reviewParam1['firetrapReview.reviewPerson'] = userInit['DftWangGeUser1']
        reviewParam1['firetrapReview.reviewDate'] = Time.getCurrentDate()
        reviewParam1['companyCheckRecordId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.company_check_record_id from firetrap_supervise t where t.check_place='%s'"%Param['fireCompanyInfo.companyName']) 
        reviewParam1['operateMode'] = 'add'
        reviewParam1['firetrapReview.updateDept'] = orgInit['DftWangGeOrgId1'] 
        reviewParam1['firetrapReview.createDept'] = orgInit['DftWangGeOrgId1'] 
        reviewParam1['firetrapReview.firetrapSuperviseId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.firetrap_supervise_id from firetrap_supervise t where t.check_place='%s'"%Param['fireCompanyInfo.companyName'])  
        responseDict = YinHuanDuGaiIntf.SaveFiretrapReview(reviewParam1, username=userInit['DftWangGeUser1'], password='11111111')

        #结果为一般的复查不合格上报给社区
        taskParam1 = copy.deepcopy(YinHuanDuGaiPara.saveCompanyCheckRecordTaskDict) 
        taskParam1['oldCheckRecordId'] = reviewParam1['companyCheckRecordId']
        taskParam1['reportState'] = 3
        taskParam1['companyCheckRecord.fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param['fireCompanyInfo.companyName'])
        taskParam1['companyCheckRecord.source'] = 1
        taskParam1['companyCheckRecord.checkType'] = 2
        taskParam1['companyName'] = Param['fireCompanyInfo.companyName']
        taskParam1['address'] = Param['fireCompanyInfo.address'] 
        taskParam1['manger'] = Param['fireCompanyInfo.manger'] 
        taskParam1['managerTelephone'] = Param['fireCompanyInfo.managerTelephone'] 
        taskParam1['companyCheckRecord_assignUserVoto'] = userInit['DftSheQuUserXM']
        taskParam1['companyCheckRecord.assignUser'] = userInit['DftSheQuUser']
        taskParam1['companyCheckRecord_assignDeptVo'] = orgInit['DftSheQuOrg']
        taskParam1['companyCheckRecord.assignDept'] = orgInit['DftSheQuOrgId']
        responseDict = YinHuanDuGaiIntf.saveCompanyCheckRecordTask(taskParam1, username=userInit['DftWangGeUser1'], password='11111111')

        #上报后，在社区的上报督改模块查看上报内容
        checkParam = copy.deepcopy(YinHuanDuGaiPara.checkSaveFiretrapSuperviseDict) 
        checkParam['companyName'] = Param['fireCompanyInfo.companyName']
        checkParam['fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param['fireCompanyInfo.companyName'])
        responseDict = YinHuanDuGaiIntf.check_saveFiretrapSupervise(checkParam,orgId=orgInit['DftSheQuOrgId'], allStateSearch='0',publicString='3',username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict, '检查失败')

        #社区——上报督改模块对改记录进行检查
        Param2 = copy.deepcopy(YinHuanDuGaiPara.saveFiretrapSuperviseDict) 
        Param2['isReportFlag'] = 0 
        Param2['calCheckResult'] = Param1['checkResult'] 
        Param2['firetrapSupervise.superviseNo'] = 'DG2016061700003'
        Param2['companyName'] = Param['fireCompanyInfo.companyName']
        Param2['checkDate'] = Time.getCurrentDate()
        Param2['firetrapSupervise.checkAddress'] = Param['fireCompanyInfo.address'] 
        Param2['firetrapSupervise.checkPlace'] = Param['fireCompanyInfo.companyName']
        Param2['checkItemIndexs'] = '1.'
        Param2['checkItemCodes'] = '%s#'% CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_item_id from supervise_type_item t where t.supervise_item_id =%s and t.supervise_type_id =%s"%(CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_item_id from supervise_item t where t.name ='安全出口疏散通道数量不足'"),CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg'] )))  #隐患项
        Param2['firetrapSupervise.reviseDate'] = Time.getCurrentDate()  #整改日期
        Param2['firetrapSupervise.manageName'] = Param['fireCompanyInfo.manger']
        Param2['companyCheckRecord_assignUserNameVo'] = userInit['DftJieDaoUserXM']
        Param2['companyCheckRecord_assignUserVo'] = userInit['DftJieDaoUser']
        Param2['companyCheckRecord_levelOrg'] = '村（社区）'
        Param2['companyCheckRecordlevel'] = '乡镇（街道）'
        Param2['companyCheckRecordOrgId'] = orgInit['DftJieDaoOrgId']
        Param2['user.userName'] = userInit['DftJieDaoUser']
        Param2['user.name'] = userInit['DftJieDaoUserXM']
        Param2['user.organization.id'] = orgInit['DftJieDaoOrgId']
        Param2['calculationMode'] = 0
        Param2['firetrapSupervise.signDate'] = Time.getCurrentDate()
        Param2['firetrapSupervise.superviseUserName'] = userInit['DftSheQuUserXM'] 
        Param2['firetrapSupervise.superviseUser'] = userInit['DftSheQuUser'] 
        Param2['firetrapSupervise.superviseDate'] = Time.getCurrentDate()
        Param2['operateMode'] = 'add'
        Param2['firetrapSupervise.superviseState'] = 1
        Param2['firetrapSupervise.updateDept'] = orgInit['DftSheQuOrgId']
        Param2['firetrapSupervise.createDept'] = orgInit['DftSheQuOrgId']
        Param2['firetrapSupervise.companyCheckRecordId'] =  CommonIntf.getDbQueryResult(dbCommand = "select t.company_check_record_id from firetrap_supervise t where t.check_place='%s'and t.update_user='%s'"%(Param['fireCompanyInfo.companyName'],userInit['DftWangGeUser1'])) +1
        Param2['superviseTypeId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg'] )
        Param2['companyCheckRecord.companyManager'] = Param['fireCompanyInfo.manger']
        Param2['companyCheckRecord.assignUser'] = userInit['DftSheQuUser'] 
        Param2['companyCheckRecord.assignDept'] = orgInit['DftSheQuOrgId']
        Param2['companyCheckRecord.checkType'] = 1
        Param2['companyCheckRecord.companyCheckRecordId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.company_check_record_id from firetrap_supervise t where t.check_place='%s'and t.update_user='%s'"%(Param['fireCompanyInfo.companyName'],userInit['DftWangGeUser1']))
        Param2['companyCheckRecord.checkUser'] = userInit['DftWangGeUser1'] 
        Param2['companyCheckRecord.fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param['fireCompanyInfo.companyName']) #被检查单位的id
        Param2['companyCheckRecord.checkDate'] = Time.getCurrentDate()
        Param2['checkResult'] = '一般'
        responseDict = YinHuanDuGaiIntf.saveFiretrapSupervise(Param2, username=userInit['DftSheQuUser'], password='11111111')

        #复查
        reviewParam2 = copy.deepcopy(YinHuanDuGaiPara.saveFiretrapReviewDict) 
        reviewParam2['calculationMode'] = 0
        reviewParam2['superviseState'] = 1
        reviewParam2['firetrapReview.firetrapReviewNo'] = 'FC2016061700002'
        reviewParam2['companyName'] = Param['fireCompanyInfo.companyName']
        reviewParam2['superviseNo'] = Param2['firetrapSupervise.superviseNo']
        reviewParam2['reviewItems[0].id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_item_id from supervise_type_item t where t.supervise_item_id =%s and t.supervise_type_id =%s"%(CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_item_id from supervise_item t where t.name ='安全出口疏散通道数量不足'"),CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg'] )))  #隐患项
        reviewParam2['reviewItems[0].checkItemId'] = CommonIntf.getDbQueryResult(dbCommand = "select  p.check_item_id from check_item  p where p.firetrap_supervise_id=%s"%CommonIntf.getDbQueryResult(dbCommand = "select t.firetrap_supervise_id from firetrap_supervise t where t.check_place='%s'and t.create_user ='%s'"%(Param['fireCompanyInfo.companyName'],userInit['DftSheQuUser'])))#"%Param['fireCompanyInfo.companyName'])) +1
        reviewParam2['reviewItems[0].state'] = 1
        reviewParam2['firetrapReview.reviseState'] = 1 
        reviewParam2['firetrapReview.reviewState'] = 1
        reviewParam2['firetrapReview.reviewPersonName'] = userInit['DftSheQuUserXM']
        reviewParam2['firetrapReview.reviewPerson'] = userInit['DftSheQuUser']
        reviewParam2['firetrapReview.reviewDate'] = Time.getCurrentDate()
        reviewParam2['companyCheckRecordId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.company_check_record_id from firetrap_supervise t where t.check_place='%s'and t.create_user ='%s'"%(Param['fireCompanyInfo.companyName'],userInit['DftSheQuUser']))#"%Param['fireCompanyInfo.companyName']) +1
        reviewParam2['operateMode'] = 'add'
        reviewParam2['firetrapReview.updateDept'] = orgInit['DftSheQuOrgId'] 
        reviewParam2['firetrapReview.createDept'] = orgInit['DftSheQuOrgId'] 
        reviewParam2['firetrapReview.firetrapSuperviseId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.firetrap_supervise_id from firetrap_supervise t where t.check_place='%s'and t.create_user ='%s'"%(Param['fireCompanyInfo.companyName'],userInit['DftSheQuUser']))#"%Param['fireCompanyInfo.companyName']) +1
        print reviewParam2
        responseDict = YinHuanDuGaiIntf.SaveFiretrapReview(reviewParam2, username=userInit['DftSheQuUser'], password='11111111')

        #结果为一般的复查不合格上报给街道
        taskParam2 = copy.deepcopy(YinHuanDuGaiPara.saveCompanyCheckRecordTaskDict) 
        taskParam2['oldCheckRecordId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.company_check_record_id from firetrap_supervise t where t.check_place='%s'and t.create_user ='%s'"%(Param['fireCompanyInfo.companyName'],userInit['DftSheQuUser'])) 
        taskParam2['reportState'] = 3
        taskParam2['companyCheckRecord.fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param['fireCompanyInfo.companyName'])
        taskParam2['companyCheckRecord.source'] = 1
        taskParam2['companyCheckRecord.checkType'] = 3
        taskParam2['companyName'] = Param['fireCompanyInfo.companyName']
        taskParam2['address'] = Param['fireCompanyInfo.address'] 
        taskParam2['manger'] = Param['fireCompanyInfo.manger'] 
        taskParam2['managerTelephone'] = Param['fireCompanyInfo.managerTelephone'] 
        taskParam2['companyCheckRecord_assignUserVoto'] = '自动化街道用户1'#userInit['DftJieDaoUserXM']
        taskParam2['companyCheckRecord.assignUser'] = 'zdhjd1@'#userInit['DftJieDaoUser']
        taskParam2['companyCheckRecord_assignDeptVo'] = orgInit['DftJieDaoOrg']
        taskParam2['companyCheckRecord.assignDept'] = orgInit['DftJieDaoOrgId']
        responseDict = YinHuanDuGaiIntf.saveCompanyCheckRecordTask(taskParam2, username=userInit['DftSheQuUser'], password='11111111')
   
        #上报后，在街道的上报督改模块查看上报内容
        checkParam = copy.deepcopy(YinHuanDuGaiPara.checkSaveFiretrapSuperviseDict) 
        checkParam['companyName'] = Param['fireCompanyInfo.companyName']
        checkParam['fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param['fireCompanyInfo.companyName'])
        responseDict = YinHuanDuGaiIntf.check_saveFiretrapSupervise(checkParam,orgId=orgInit['DftJieDaoOrgId'], allStateSearch='0',publicString='3',username='zdhjd1@', password='11111111')
        self.assertTrue(responseDict, '检查失败')

        pass

    '''
    @功能：上报处理（网格新增的严重隐患日常检查，直接上报给街道处理）
    @ chenyan 2016-6-17
    '''
    def testFiretrapReview(self):
        """街道处理上报日常检查记录（跨级上报处理）"""
        #新增单位
        Param = copy.deepcopy(YinHuanDuGaiPara.fireCompanyDict) 
        Param['mode'] = 'add'  
        Param['fireCompanyInfo.createDept'] = orgInit['DftWangGeOrgId1'] 
        Param['fireCompanyInfo.importOrAdd'] = '1'
        Param['fireCompanyInfo.orgPathName'] = '%s%s%s%s%s'%(orgInit['DftShiOrg'],orgInit['DftQuOrg'],orgInit['DftJieDaoOrg'],orgInit['DftSheQuOrg'],orgInit['DftWangGeOrg1'])
        Param['fireCompanyInfo.companyName'] = '测试单位%s'%CommonUtil.createRandomString()
        Param['fireCompanyInfo.orgid'] = Param['fireCompanyInfo.createDept']
        Param['companySuperviseTypeIsChange'] = 'true'
        Param['fireCompanyInfo.superviseTypeName'] = '其他一般单位'
        Param['fireCompanyInfo.superviseType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg']) 
        Param['fireCompanyInfo.address'] = '测试地址'
        Param['fireCompanyInfo.manger'] = '测试姓名'
        Param['fireCompanyInfo.managerTelephone'] = '18710000000'
        Param['fireCompanyInfo.rentHousePerson'] = '0'
        Param['fireCompanyInfo.industrialCatalogue'] = CommonIntf.getDbQueryResult(dbCommand = "select t.code from fire_company_type t where t.name='电器'")  #行业类别
        Param['businessLicense'] = '1'
        Param['firelicense'] = '1'
        responseDict = YinHuanDuGaiIntf.addOrEdit_fireCompany(Param, username=userInit['DftWangGeUser1'], password='11111111')

        #添加日常检查
        Param1 = copy.deepcopy(YinHuanDuGaiPara.saveFiretrapSuperviseDict) 
        Param1['isReportFlag'] = 0 
        Param1['calCheckResult'] = 'flag'
        Param1['firetrapSupervise.superviseNo'] = 'DG2016061700014'
        Param1['companyName'] = Param['fireCompanyInfo.companyName']
        Param1['checkDate'] = Time.getCurrentDate()
        Param1['firetrapSupervise.checkAddress'] = Param['fireCompanyInfo.address'] 
        Param1['firetrapSupervise.checkPlace'] = Param['fireCompanyInfo.companyName']
        Param1['checkItemIndexs'] = '3.'
        Param1['checkItemCodes'] = '%s#'% CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_item_id from supervise_type_item t where t.supervise_item_id =%s and t.supervise_type_id =%s"%(CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_item_id from supervise_item t where t.name ='安全出口疏散通道堵塞'"),CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg'] )))  #隐患项
        Param1['firetrapSupervise.reviseDate'] = Time.getCurrentDate()  #整改日期
        Param1['firetrapSupervise.manageName'] = Param['fireCompanyInfo.manger']
        Param1['companyCheckRecord_assignUserNameVo'] = '自动化街道用户1'#userInit['DftJieDaoUserXM']
        Param1['companyCheckRecord_assignUserVo'] = 'zdhjd1@'# userInit['DftJieDaoUser']
        Param1['companyCheckRecord_levelOrg'] = '片组片格'
        Param1['companyCheckRecordlevel'] = '村（社区）'
        Param1['companyCheckRecordOrgId'] = orgInit['DftJieDaoOrgId']
        Param1['user.userName'] = 'zdhjd1@'#userInit['DftJieDaoUser']
        Param1['user.name'] =  '自动化街道用户1'#userInit['DftJieDaoUserXM']
        Param1['user.organization.id'] = orgInit['DftJieDaoOrgId']
        Param1['calculationMode'] = 0
        Param1['firetrapSupervise.signDate'] = Time.getCurrentDate()
        Param1['firetrapSupervise.superviseUserName'] = '自动化街道用户1'#userInit['DftWangGeUserXM1'] 
        Param1['firetrapSupervise.superviseUser'] = 'zdhjd1@'# userInit['DftWangGeUser1'] 
        Param1['firetrapSupervise.superviseDate'] = Time.getCurrentDate()
        Param1['operateMode'] = 'add'
        Param1['firetrapSupervise.superviseState'] = 1
        Param1['firetrapSupervise.updateDept'] = orgInit['DftWangGeOrgId1']
        Param1['firetrapSupervise.createDept'] = orgInit['DftWangGeOrgId1']
        Param1['superviseTypeId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg'] )
        Param1['companyCheckRecord.companyManager'] = Param['fireCompanyInfo.manger']
        Param1['companyCheckRecord.assignUser'] = userInit['DftWangGeUser1'] 
        Param1['companyCheckRecord.assignDept'] = orgInit['DftWangGeOrgId1']
        Param1['companyCheckRecord.checkType'] = 1
        Param1['companyCheckRecord.checkUser'] = userInit['DftWangGeUser1'] 
        Param1['companyCheckRecord.fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param['fireCompanyInfo.companyName']) #被检查单位的id
        Param1['companyCheckRecord.checkDate'] = Time.getCurrentDate()
        Param1['checkResult'] = '高危'
        responseDict = YinHuanDuGaiIntf.saveFiretrapSupervise(Param1, username=userInit['DftWangGeUser1'], password='11111111')

        #上报后，在街道的上报督改模块查看上报内容
        checkParam = copy.deepcopy(YinHuanDuGaiPara.checkSaveFiretrapSuperviseDict) 
        checkParam['companyName'] = Param['fireCompanyInfo.companyName']
        checkParam['fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param['fireCompanyInfo.companyName'])
        response = YinHuanDuGaiIntf.check_CompanyCheckRecordTask(checkParam,orgId=orgInit['DftJieDaoOrgId'], allStateSearch='0',publicString='3',username='zdhjd1@', password='11111111')
        print response
        for item in response['rows']:
            if item['fireCompanyInfo']['companyName']==Param['fireCompanyInfo.companyName']:
                #街道——上报督改模块对改记录进行检查（未整改的检查后直接抄告执法）
                Param2 = copy.deepcopy(YinHuanDuGaiPara.saveFiretrapSuperviseDict) 
                Param2['isReportFlag'] = 0 
                Param2['calCheckResult'] = Param1['checkResult'] 
                Param2['firetrapSupervise.superviseNo'] = 'DG2016061700015'
                Param2['companyName'] = Param['fireCompanyInfo.companyName']
                Param2['checkDate'] = Time.getCurrentDate()
                Param2['firetrapSupervise.checkAddress'] = Param['fireCompanyInfo.address'] 
                Param2['firetrapSupervise.checkPlace'] = Param['fireCompanyInfo.companyName']
                Param2['checkItemIndexs'] = '3.'
                Param2['checkItemCodes'] = '%s#'% CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_item_id from supervise_type_item t where t.supervise_item_id =%s and t.supervise_type_id =%s"%(CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_item_id from supervise_item t where t.name ='安全出口疏散通道堵塞'"),CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg'] )))  #隐患项
                Param2['firetrapSupervise.manageName'] = Param['fireCompanyInfo.manger']
                Param2['companyCheckRecord_assignUserNameVo'] = '自动化街道用户1'#userInit['DftJieDaoUserXM']
                Param2['companyCheckRecord_assignUserVo'] = 'zdhjd1@'#userInit['DftJieDaoUser']
                Param2['companyCheckRecord_levelOrg'] = '乡镇（街道）'
                Param2['user.userName'] = 'zdhjd1@'#userInit['DftJieDaoUser']
                Param2['user.name'] = '自动化街道用户1'#userInit['DftJieDaoUserXM']
                Param2['user.organization.id'] = orgInit['DftJieDaoOrgId']
                Param2['calculationMode'] = 0
                Param2['firetrapSupervise.signDate'] = Time.getCurrentDate()
                Param2['firetrapSupervise.superviseUserName'] = '自动化街道用户1'#userInit['DftSheQuUserXM'] 
                Param2['firetrapSupervise.superviseUser'] = 'zdhjd1@'#userInit['DftSheQuUser'] 
                Param2['firetrapSupervise.superviseDate'] = Time.getCurrentDate()
                Param2['operateMode'] = 'add'
                Param2['firetrapSupervise.superviseState'] = 1
                Param2['firetrapSupervise.updateDept'] = orgInit['DftJieDaoOrgId']
                Param2['firetrapSupervise.createDept'] = orgInit['DftJieDaoOrgId']
                Param2['firetrapSupervise.companyCheckRecordId'] =  item['companyCheckRecord']['companyCheckRecordId']#CommonIntf.getDbQueryResult(dbCommand = "select t.company_check_record_id from firetrap_supervise t where t.check_place='%s'and t.update_user='%s'"%(Param['fireCompanyInfo.companyName'],userInit['DftWangGeUser1'])) +2
                Param2['superviseTypeId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg'] )
                Param2['companyCheckRecord.companyManager'] = Param['fireCompanyInfo.manger']
                Param2['companyCheckRecord.assignUser'] = 'zdhjd1@'#userInit['DftSheQuUser'] 
                Param2['companyCheckRecord.assignDept'] = orgInit['DftJieDaoOrgId']
                Param2['companyCheckRecord.checkType'] = 3
                Param2['companyCheckRecord.companyCheckRecordId'] = item['companyCheckRecord']['parentId']#CommonIntf.getDbQueryResult(dbCommand = "select t.company_check_record_id from firetrap_supervise t where t.check_place='%s'and t.update_user='%s'"%(Param['fireCompanyInfo.companyName'],userInit['DftWangGeUser1']))+1
                Param2['companyCheckRecord.checkUser'] = 'zdhjd1@'#userInit['DftSheQuUser'] 
                Param2['companyCheckRecord.fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param['fireCompanyInfo.companyName']) #被检查单位的id
                Param2['companyCheckRecord.checkDate'] = Time.getCurrentDate()
                Param2['checkResult'] = '高危'
                responseDict = YinHuanDuGaiIntf.saveFiretrapSupervise(Param2, username=userInit['DftSheQuUser'], password='11111111')
         

        pass

    '''
    @功能：删除上报处理记录
    @ chenyan 2016-6-17
    '''
    def testFiretrapReviewSearchDelete(self):
        """删除上报处理记录"""
        #新增单位
        Param01 = copy.deepcopy(YinHuanDuGaiPara.fireCompanyDict) 
        Param01['mode'] = 'add'  
        Param01['fireCompanyInfo.createDept'] = orgInit['DftWangGeOrgId1'] 
        Param01['fireCompanyInfo.importOrAdd'] = '1'
        Param01['fireCompanyInfo.orgPathName'] = '%s%s%s%s%s'%(orgInit['DftShiOrg'],orgInit['DftQuOrg'],orgInit['DftJieDaoOrg'],orgInit['DftSheQuOrg'],orgInit['DftWangGeOrg1'])
        Param01['fireCompanyInfo.companyName'] = '测试单位%s'%CommonUtil.createRandomString()
        Param01['fireCompanyInfo.orgid'] = Param01['fireCompanyInfo.createDept']
        Param01['companySuperviseTypeIsChange'] = 'true'
        Param01['fireCompanyInfo.superviseTypeName'] = '其他一般单位'
        Param01['fireCompanyInfo.superviseType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg']) 
        Param01['fireCompanyInfo.address'] = '测试地址'
        Param01['fireCompanyInfo.manger'] = '测试姓名'
        Param01['fireCompanyInfo.managerTelephone'] = '18710000000'
        Param01['fireCompanyInfo.rentHousePerson'] = '0'
        Param01['fireCompanyInfo.industrialCatalogue'] = CommonIntf.getDbQueryResult(dbCommand = "select t.code from fire_company_type t where t.name='电器'")  #行业类别
        Param01['businessLicense'] = '1'
        Param01['firelicense'] = '1'
        responseDict = YinHuanDuGaiIntf.addOrEdit_fireCompany(Param01, username=userInit['DftWangGeUser1'], password='11111111')

        #添加日常检查
        Param1 = copy.deepcopy(YinHuanDuGaiPara.saveFiretrapSuperviseDict) 
        Param1['isReportFlag'] = 0 
        Param1['calCheckResult'] = 'flag'
        Param1['firetrapSupervise.superviseNo'] = 'DG2016061700014'
        Param1['companyName'] = Param01['fireCompanyInfo.companyName']
        Param1['checkDate'] = Time.getCurrentDate()
        Param1['firetrapSupervise.checkAddress'] = Param01['fireCompanyInfo.address'] 
        Param1['firetrapSupervise.checkPlace'] = Param01['fireCompanyInfo.companyName']
        Param1['checkItemIndexs'] = '3.'
        Param1['checkItemCodes'] = '%s#'% CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_item_id from supervise_type_item t where t.supervise_item_id =%s and t.supervise_type_id =%s"%(CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_item_id from supervise_item t where t.name ='安全出口疏散通道堵塞'"),CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg'] )))  #隐患项
        Param1['firetrapSupervise.reviseDate'] = Time.getCurrentDate()  #整改日期
        Param1['firetrapSupervise.manageName'] = Param01['fireCompanyInfo.manger']
        Param1['companyCheckRecord_assignUserNameVo'] = '自动化街道用户1'#userInit['DftJieDaoUserXM']
        Param1['companyCheckRecord_assignUserVo'] = 'zdhjd1@'# userInit['DftJieDaoUser']
        Param1['companyCheckRecord_levelOrg'] = '片组片格'
        Param1['companyCheckRecordlevel'] = '村（社区）'
        Param1['companyCheckRecordOrgId'] = orgInit['DftJieDaoOrgId']
        Param1['user.userName'] = 'zdhjd1@'#userInit['DftJieDaoUser']
        Param1['user.name'] =  '自动化街道用户1'#userInit['DftJieDaoUserXM']
        Param1['user.organization.id'] = orgInit['DftJieDaoOrgId']
        Param1['calculationMode'] = 0
        Param1['firetrapSupervise.signDate'] = Time.getCurrentDate()
        Param1['firetrapSupervise.superviseUserName'] = '自动化街道用户1'#userInit['DftWangGeUserXM1'] 
        Param1['firetrapSupervise.superviseUser'] = 'zdhjd1@'# userInit['DftWangGeUser1'] 
        Param1['firetrapSupervise.superviseDate'] = Time.getCurrentDate()
        Param1['operateMode'] = 'add'
        Param1['firetrapSupervise.superviseState'] = 1
        Param1['firetrapSupervise.updateDept'] = orgInit['DftWangGeOrgId1']
        Param1['firetrapSupervise.createDept'] = orgInit['DftWangGeOrgId1']
        Param1['superviseTypeId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg'] )
        Param1['companyCheckRecord.companyManager'] = Param01['fireCompanyInfo.manger']
        Param1['companyCheckRecord.assignUser'] = userInit['DftWangGeUser1'] 
        Param1['companyCheckRecord.assignDept'] = orgInit['DftWangGeOrgId1']
        Param1['companyCheckRecord.checkType'] = 1
        Param1['companyCheckRecord.checkUser'] = userInit['DftWangGeUser1'] 
        Param1['companyCheckRecord.fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param01['fireCompanyInfo.companyName']) #被检查单位的id
        Param1['companyCheckRecord.checkDate'] = Time.getCurrentDate()
        Param1['checkResult'] = '高危'
        responseDict = YinHuanDuGaiIntf.saveFiretrapSupervise(Param1, username=userInit['DftWangGeUser1'], password='11111111')

        #新增单位
        Param02 = copy.deepcopy(YinHuanDuGaiPara.fireCompanyDict) 
        Param02['mode'] = 'add'  
        Param02['fireCompanyInfo.createDept'] = orgInit['DftWangGeOrgId1'] 
        Param02['fireCompanyInfo.importOrAdd'] = '1'
        Param02['fireCompanyInfo.orgPathName'] = '%s%s%s%s%s'%(orgInit['DftShiOrg'],orgInit['DftQuOrg'],orgInit['DftJieDaoOrg'],orgInit['DftSheQuOrg'],orgInit['DftWangGeOrg1'])
        Param02['fireCompanyInfo.companyName'] = '测试单位%s'%CommonUtil.createRandomString()
        Param02['fireCompanyInfo.orgid'] = Param02['fireCompanyInfo.createDept']
        Param02['companySuperviseTypeIsChange'] = 'true'
        Param02['fireCompanyInfo.superviseTypeName'] = '其他一般单位'
        Param02['fireCompanyInfo.superviseType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg']) 
        Param02['fireCompanyInfo.address'] = '测试地址'
        Param02['fireCompanyInfo.manger'] = '测试姓名'
        Param02['fireCompanyInfo.managerTelephone'] = '18710000000'
        Param02['fireCompanyInfo.rentHousePerson'] = '0'
        Param02['fireCompanyInfo.industrialCatalogue'] = CommonIntf.getDbQueryResult(dbCommand = "select t.code from fire_company_type t where t.name='电器'")  #行业类别
        Param02['businessLicense'] = '1'
        Param02['firelicense'] = '1'
        responseDict = YinHuanDuGaiIntf.addOrEdit_fireCompany(Param02, username=userInit['DftWangGeUser1'], password='11111111')

        #添加日常检查
        Param2 = copy.deepcopy(YinHuanDuGaiPara.saveFiretrapSuperviseDict) 
        Param2['isReportFlag'] = 0 
        Param2['calCheckResult'] = 'flag'
        Param2['firetrapSupervise.superviseNo'] = 'DG2016061700014'
        Param2['companyName'] = Param02['fireCompanyInfo.companyName']
        Param2['checkDate'] = Time.getCurrentDate()
        Param2['firetrapSupervise.checkAddress'] = Param02['fireCompanyInfo.address'] 
        Param2['firetrapSupervise.checkPlace'] = Param02['fireCompanyInfo.companyName']
        Param2['checkItemIndexs'] = '3.'
        Param2['checkItemCodes'] = '%s#'% CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_item_id from supervise_type_item t where t.supervise_item_id =%s and t.supervise_type_id =%s"%(CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_item_id from supervise_item t where t.name ='安全出口疏散通道堵塞'"),CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg'] )))  #隐患项
        Param2['firetrapSupervise.reviseDate'] = Time.getCurrentDate()  #整改日期
        Param2['firetrapSupervise.manageName'] = Param02['fireCompanyInfo.manger']
        Param2['companyCheckRecord_assignUserNameVo'] = '自动化街道用户1'#userInit['DftJieDaoUserXM']
        Param2['companyCheckRecord_assignUserVo'] = 'zdhjd1@'# userInit['DftJieDaoUser']
        Param2['companyCheckRecord_levelOrg'] = '片组片格'
        Param2['companyCheckRecordlevel'] = '村（社区）'
        Param2['companyCheckRecordOrgId'] = orgInit['DftJieDaoOrgId']
        Param2['user.userName'] = 'zdhjd1@'#userInit['DftJieDaoUser']
        Param2['user.name'] =  '自动化街道用户1'#userInit['DftJieDaoUserXM']
        Param2['user.organization.id'] = orgInit['DftJieDaoOrgId']
        Param2['calculationMode'] = 0
        Param2['firetrapSupervise.signDate'] = Time.getCurrentDate()
        Param2['firetrapSupervise.superviseUserName'] = '自动化街道用户1'#userInit['DftWangGeUserXM1'] 
        Param2['firetrapSupervise.superviseUser'] = 'zdhjd1@'# userInit['DftWangGeUser1'] 
        Param2['firetrapSupervise.superviseDate'] = Time.getCurrentDate()
        Param2['operateMode'] = 'add'
        Param2['firetrapSupervise.superviseState'] = 1
        Param2['firetrapSupervise.updateDept'] = orgInit['DftWangGeOrgId1']
        Param2['firetrapSupervise.createDept'] = orgInit['DftWangGeOrgId1']
        Param2['superviseTypeId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg'] )
        Param2['companyCheckRecord.companyManager'] = Param02['fireCompanyInfo.manger']
        Param2['companyCheckRecord.assignUser'] = userInit['DftWangGeUser1'] 
        Param2['companyCheckRecord.assignDept'] = orgInit['DftWangGeOrgId1']
        Param2['companyCheckRecord.checkType'] = 1
        Param2['companyCheckRecord.checkUser'] = userInit['DftWangGeUser1'] 
        Param2['companyCheckRecord.fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param02['fireCompanyInfo.companyName']) #被检查单位的id
        Param2['companyCheckRecord.checkDate'] = Time.getCurrentDate()
        Param2['checkResult'] = '高危'
        responseDict = YinHuanDuGaiIntf.saveFiretrapSupervise(Param2, username=userInit['DftWangGeUser1'], password='11111111')

        #搜索上报督改检查
        searchParam = copy.deepcopy(YinHuanDuGaiPara.checkSaveFiretrapSuperviseDict) 
        searchParam['companyName'] = Param01['fireCompanyInfo.companyName']
        searchParam['fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param01['fireCompanyInfo.companyName'])
        response1 = YinHuanDuGaiIntf.check_saveFiretrapSupervise(searchParam,companyName=Param01['fireCompanyInfo.companyName'],orgId=orgInit['DftJieDaoOrgId'], allStateSearch='1',publicString='3',username='zdhjd1@', password='11111111')
        for item in response1['rows']:
            if item['fireCompanyInfo']['companyName']==Param01['fireCompanyInfo.companyName']:
                deleteParam = copy.deepcopy(YinHuanDuGaiPara.deleteFiretrapReviewDict) 
                deleteParam['ids'] = item['companyCheckRecordId']
                responseDict = YinHuanDuGaiIntf.delete_FiretrapReview(deleteParam,  username='zdhjd1@', password='11111111')
 
        #删除后检查
        checkParam = copy.deepcopy(YinHuanDuGaiPara.checkSaveFiretrapSuperviseDict) 
        checkParam['companyName'] = Param01['fireCompanyInfo.companyName']
        checkParam['fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param01['fireCompanyInfo.companyName'])
        response = YinHuanDuGaiIntf.check_saveFiretrapSupervise(checkParam,orgId=orgInit['DftJieDaoOrgId'], allStateSearch='0',publicString='3',username='zdhjd1@', password='11111111')

    '''
    @功能：新增/搜索举报检查 
    @ chenyan 2016-6-17
    '''
    def testComplaintHandle(self):
        """新增/搜索举报检查"""
        #新增单位1
        Param1 = copy.deepcopy(YinHuanDuGaiPara.fireCompanyDict) 
        Param1['mode'] = 'add'  
        Param1['fireCompanyInfo.createDept'] = orgInit['DftWangGeOrgId1'] 
        Param1['fireCompanyInfo.importOrAdd'] = '1'
        Param1['fireCompanyInfo.orgPathName'] = '%s%s%s%s%s'%(orgInit['DftShiOrg'],orgInit['DftQuOrg'],orgInit['DftJieDaoOrg'],orgInit['DftSheQuOrg'],orgInit['DftWangGeOrg1'])
        Param1['fireCompanyInfo.companyName'] = '测试单位%s'%CommonUtil.createRandomString()
        Param1['fireCompanyInfo.orgid'] = Param1['fireCompanyInfo.createDept']
        Param1['companySuperviseTypeIsChange'] = 'true'
        Param1['fireCompanyInfo.superviseTypeName'] = '其他一般单位'
        Param1['fireCompanyInfo.superviseType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg']) 
        Param1['fireCompanyInfo.address'] = '测试地址'
        Param1['fireCompanyInfo.manger'] = '测试姓名'
        Param1['fireCompanyInfo.managerTelephone'] = '18710000000'
        Param1['fireCompanyInfo.rentHousePerson'] = '0'
        Param1['fireCompanyInfo.industrialCatalogue'] = CommonIntf.getDbQueryResult(dbCommand = "select t.code from fire_company_type t where t.name='电器'")  #行业类别
        Param1['businessLicense'] = '1'
        Param1['firelicense'] = '1'
        responseDict = YinHuanDuGaiIntf.addOrEdit_fireCompany(Param1, username=userInit['DftWangGeUser1'], password='11111111')

        #新增单位举报检查1
        Param01 = copy.deepcopy(YinHuanDuGaiPara.saveComplaintHandleDict) 
        Param01['companyCheckRecord.source'] = 1
        Param01['complaintHandleInfo.complaintHandleNo'] = 'JB2016061400009'
        Param01['complaintHandleInfo.reporterName'] = '测试1'
        Param01['complaintHandleInfo.reporterTelephone'] = '1234567'
        Param01['complaintHandleInfo.compliantManner'] = 0   #举报投诉形式
        Param01['complaintHandleInfo.handleDate'] = Time.getCurrentDate()
        Param01['complaintHandleInfo.handleName'] = '受理人员'
        Param01['complaintHandleInfo.complaintContent'] = '受理内容'
        Param01['companyCheckRecord.fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param1['fireCompanyInfo.companyName'])
        Param01['companyCheckRecord.checkType'] = 4
        Param01['companyCheckRecord.dateFrom'] = Time.getCurrentDate()
        Param01['companyCheckRecord.dateTo'] = Time.getCurrentDate()
        responseDict = YinHuanDuGaiIntf.saveComplaintHandle(Param01, username=userInit['DftWangGeUser1'], password='11111111')

        #新增单位2
        Param2 = copy.deepcopy(YinHuanDuGaiPara.fireCompanyDict) 
        Param2['mode'] = 'add'  
        Param2['fireCompanyInfo.createDept'] = orgInit['DftWangGeOrgId1'] 
        Param2['fireCompanyInfo.importOrAdd'] = '1'
        Param2['fireCompanyInfo.orgPathName'] = '%s%s%s%s%s'%(orgInit['DftShiOrg'],orgInit['DftQuOrg'],orgInit['DftJieDaoOrg'],orgInit['DftSheQuOrg'],orgInit['DftWangGeOrg1'])
        Param2['fireCompanyInfo.companyName'] = '测试单位%s'%CommonUtil.createRandomString()
        Param2['fireCompanyInfo.orgid'] = Param2['fireCompanyInfo.createDept']
        Param2['companySuperviseTypeIsChange'] = 'true'
        Param2['fireCompanyInfo.superviseTypeName'] = '其他一般单位'
        Param2['fireCompanyInfo.superviseType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg']) 
        Param2['fireCompanyInfo.address'] = '测试地址'
        Param2['fireCompanyInfo.manger'] = '测试姓名'
        Param2['fireCompanyInfo.managerTelephone'] = '18710000000'
        Param2['fireCompanyInfo.rentHousePerson'] = '0'
        Param2['fireCompanyInfo.industrialCatalogue'] = CommonIntf.getDbQueryResult(dbCommand = "select t.code from fire_company_type t where t.name='电器'")  #行业类别
        Param2['businessLicense'] = '1'
        Param2['firelicense'] = '1'
        responseDict = YinHuanDuGaiIntf.addOrEdit_fireCompany(Param2, username=userInit['DftWangGeUser1'], password='11111111')

        #新增单位举报检查2
        Param02 = copy.deepcopy(YinHuanDuGaiPara.saveComplaintHandleDict) 
        Param02['companyCheckRecord.source'] = 1
        Param02['complaintHandleInfo.complaintHandleNo'] = 'JB2016061400009'
        Param02['complaintHandleInfo.reporterName'] = '测试2'
        Param02['complaintHandleInfo.reporterTelephone'] = '1234567'
        Param02['complaintHandleInfo.compliantManner'] = 3   #举报投诉形式
        Param02['complaintHandleInfo.handleDate'] = Time.getCurrentTime()
        Param02['complaintHandleInfo.handleName'] = '受理人员'
        Param02['complaintHandleInfo.complaintContent'] = '受理内容'
        Param02['companyCheckRecord.fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param2['fireCompanyInfo.companyName'])
        Param02['companyCheckRecord.checkType'] = 4
        Param02['companyCheckRecord.dateFrom'] = Time.getCurrentDate()
        Param02['companyCheckRecord.dateTo'] = Time.getCurrentDate()
        responseDict = YinHuanDuGaiIntf.saveComplaintHandle(Param02, username=userInit['DftWangGeUser1'], password='11111111')

        checkParam = copy.deepcopy(YinHuanDuGaiPara.checkSaveFiretrapSuperviseDict) 
        checkParam['fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param2['fireCompanyInfo.companyName']) 
        checkParam['companyName'] = Param2['fireCompanyInfo.companyName'] 
        responseDict = YinHuanDuGaiIntf.check_saveFiretrapSupervise(checkParam,companyName=Param2['fireCompanyInfo.companyName'],orgId=orgInit['DftWangGeOrgId1'] , allStateSearch=0,publicString=4, username=userInit['DftWangGeUser1'], password='11111111')
        self.assertTrue(responseDict, '未搜索到举报信息')

    '''
    @功能：处理举报检查    
    @ chenyan 2016-6-21
    '''
    def testComplaintHandleReview(self):
        """处理举报检查（三级督改）"""
        #新增单位1
        Param = copy.deepcopy(YinHuanDuGaiPara.fireCompanyDict) 
        Param['mode'] = 'add'  
        Param['fireCompanyInfo.createDept'] = orgInit['DftWangGeOrgId1'] 
        Param['fireCompanyInfo.importOrAdd'] = '1'
        Param['fireCompanyInfo.orgPathName'] = '%s%s%s%s%s'%(orgInit['DftShiOrg'],orgInit['DftQuOrg'],orgInit['DftJieDaoOrg'],orgInit['DftSheQuOrg'],orgInit['DftWangGeOrg1'])
        Param['fireCompanyInfo.companyName'] = '测试单位%s'%CommonUtil.createRandomString()
        Param['fireCompanyInfo.orgid'] = Param['fireCompanyInfo.createDept']
        Param['companySuperviseTypeIsChange'] = 'true'
        Param['fireCompanyInfo.superviseTypeName'] = '其他一般单位'
        Param['fireCompanyInfo.superviseType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg']) 
        Param['fireCompanyInfo.address'] = '测试地址'
        Param['fireCompanyInfo.manger'] = '测试姓名'
        Param['fireCompanyInfo.managerTelephone'] = '18710000000'
        Param['fireCompanyInfo.rentHousePerson'] = '0'
        Param['fireCompanyInfo.industrialCatalogue'] = CommonIntf.getDbQueryResult(dbCommand = "select t.code from fire_company_type t where t.name='电器'")  #行业类别
        Param['businessLicense'] = '1'
        Param['firelicense'] = '1'
        responseDict = YinHuanDuGaiIntf.addOrEdit_fireCompany(Param, username=userInit['DftWangGeUser1'], password='11111111')

        #新增单位举报检查1
        Param01 = copy.deepcopy(YinHuanDuGaiPara.saveComplaintHandleDict) 
        Param01['companyCheckRecord.source'] = 1
        Param01['complaintHandleInfo.complaintHandleNo'] = 'JB2016061400009'
        Param01['complaintHandleInfo.reporterName'] = '测试1'
        Param01['complaintHandleInfo.reporterTelephone'] = '1234567'
        Param01['complaintHandleInfo.compliantManner'] = 0   #举报投诉形式
        Param01['complaintHandleInfo.handleDate'] = Time.getCurrentTime()
        Param01['complaintHandleInfo.handleName'] = '受理人员'
        Param01['complaintHandleInfo.complaintContent'] = '受理内容'
        Param01['companyCheckRecord.fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param['fireCompanyInfo.companyName'])
        Param01['companyCheckRecord.checkType'] = 4
        Param01['companyCheckRecord.dateFrom'] = Time.getCurrentTime()
        Param01['companyCheckRecord.dateTo'] = Time.getCurrentTime()
        responseDict = YinHuanDuGaiIntf.saveComplaintHandle(Param01, username=userInit['DftWangGeUser1'], password='11111111')

        checkParam = copy.deepcopy(YinHuanDuGaiPara.checkSaveFiretrapSuperviseDict) 
        checkParam['fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param['fireCompanyInfo.companyName']) 
        checkParam['companyName'] = Param['fireCompanyInfo.companyName'] 
        response = YinHuanDuGaiIntf.check_saveFiretrapSupervise(checkParam,companyName=Param ['fireCompanyInfo.companyName'],orgId=orgInit['DftWangGeOrgId1'] , allStateSearch=0,publicString=4, username=userInit['DftWangGeUser1'], password='11111111')
        for item in response['rows']:
            if item['fireCompanyInfo']['companyName']==Param['fireCompanyInfo.companyName']:
                #检查举报投诉检查
                Param1 = copy.deepcopy(YinHuanDuGaiPara.saveFiretrapSuperviseDict) 
                Param1['isReportFlag'] = 0 
                Param1['calCheckResult'] = 'flag'
                Param1['firetrapSupervise.superviseNo'] = 'DG2016062100002'
                Param1['companyName'] = Param['fireCompanyInfo.companyName']
                Param1['checkDate'] = Time.getCurrentDate()
                Param1['firetrapSupervise.checkAddress'] = Param['fireCompanyInfo.address'] 
                Param1['firetrapSupervise.checkPlace'] = Param['fireCompanyInfo.companyName']
                Param1['checkItemIndexs'] = '1.'
                Param1['checkItemCodes'] = '%s#'% CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_item_id from supervise_type_item t where t.supervise_item_id =%s and t.supervise_type_id =%s"%(CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_item_id from supervise_item t where t.name ='安全出口疏散通道数量不足'"),CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg'] )))  #隐患项
                Param1['firetrapSupervise.reviseDate'] = Time.getCurrentDate()  #整改日期
                Param1['firetrapSupervise.manageName'] = Param['fireCompanyInfo.manger']
                Param1['companyCheckRecord_assignUserNameVo'] = userInit['DftJieDaoUserXM']
                Param1['companyCheckRecord_assignUserVo'] = userInit['DftJieDaoUser']
                Param1['companyCheckRecord_levelOrg'] = '片组片格'
                Param1['companyCheckRecordlevel'] = '村（社区）'
                Param1['companyCheckRecordOrgId'] = orgInit['DftJieDaoOrgId']
                Param1['user.userName'] = userInit['DftJieDaoUser']
                Param1['user.name'] = userInit['DftJieDaoUserXM']
                Param1['user.organization.id'] = orgInit['DftJieDaoOrgId']
                Param1['calculationMode'] = 0
                Param1['firetrapSupervise.signDate'] = Time.getCurrentDate()
                Param1['firetrapSupervise.superviseUserName'] = userInit['DftWangGeUserXM1'] 
                Param1['firetrapSupervise.superviseUser'] = userInit['DftWangGeUser1'] 
                Param1['firetrapSupervise.superviseDate'] = Time.getCurrentDate()
                Param1['operateMode'] = 'add'
                Param1['firetrapSupervise.superviseState'] = 1
                Param1['firetrapSupervise.updateDept'] = orgInit['DftWangGeOrgId1']
                Param1['firetrapSupervise.createDept'] = orgInit['DftWangGeOrgId1']
                Param1['firetrapSupervise.companyCheckRecordId'] = item['companyCheckRecordId']
                Param1['superviseTypeId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg'] )
                Param1['companyCheckRecord.companyManager'] = Param['fireCompanyInfo.manger']
                Param1['companyCheckRecord.assignUser'] = userInit['DftWangGeUser1'] 
                Param1['companyCheckRecord.assignDept'] = orgInit['DftWangGeOrgId1']
                Param1['companyCheckRecord.checkUser'] = userInit['DftWangGeUser1'] 
                Param1['companyCheckRecord.fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param['fireCompanyInfo.companyName']) #被检查单位的id
                Param1['companyCheckRecord.checkDate'] = Time.getCurrentDate()
                Param1['checkResult'] = '一般'
                responseDict = YinHuanDuGaiIntf.saveFiretrapSupervise(Param1, username=userInit['DftWangGeUser1'], password='11111111')

        #复查
        reviewParam1 = copy.deepcopy(YinHuanDuGaiPara.saveFiretrapReviewDict) 
        reviewParam1['calculationMode'] = 0
        reviewParam1['superviseState'] = 1
        reviewParam1['firetrapReview.firetrapReviewNo'] = 'FC2016062100001'
        reviewParam1['companyName'] = Param['fireCompanyInfo.companyName']
        reviewParam1['superviseNo'] = Param1['firetrapSupervise.superviseNo']
        reviewParam1['reviewItems[0].id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_item_id from supervise_type_item t where t.supervise_item_id =%s and t.supervise_type_id =%s"%(CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_item_id from supervise_item t where t.name ='安全出口疏散通道数量不足'"),CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg'] )))  #隐患项
        reviewParam1['reviewItems[0].checkItemId'] = CommonIntf.getDbQueryResult(dbCommand = "select  p.check_item_id from check_item  p where p.firetrap_supervise_id=%s"%CommonIntf.getDbQueryResult(dbCommand = "select t.firetrap_supervise_id from firetrap_supervise t where t.check_place='%s'"%Param['fireCompanyInfo.companyName'])) 
        reviewParam1['reviewItems[0].state'] = 1
        reviewParam1['firetrapReview.reviseState'] = 1 
        reviewParam1['firetrapReview.reviewState'] = 1
        reviewParam1['firetrapReview.reviewPersonName'] = userInit['DftWangGeUserXM1']
        reviewParam1['firetrapReview.reviewPerson'] = userInit['DftWangGeUser1']
        reviewParam1['firetrapReview.reviewDate'] = Time.getCurrentDate()
        reviewParam1['companyCheckRecordId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.company_check_record_id from firetrap_supervise t where t.check_place='%s'"%Param['fireCompanyInfo.companyName']) 
        reviewParam1['operateMode'] = 'add'
        reviewParam1['firetrapReview.updateDept'] = orgInit['DftWangGeOrgId1'] 
        reviewParam1['firetrapReview.createDept'] = orgInit['DftWangGeOrgId1'] 
        reviewParam1['firetrapReview.firetrapSuperviseId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.firetrap_supervise_id from firetrap_supervise t where t.check_place='%s'"%Param['fireCompanyInfo.companyName'])  
        responseDict = YinHuanDuGaiIntf.SaveFiretrapReview(reviewParam1, username=userInit['DftWangGeUser1'], password='11111111')

        #结果为一般的复查不合格上报给社区
        taskParam1 = copy.deepcopy(YinHuanDuGaiPara.saveCompanyCheckRecordTaskDict) 
        taskParam1['oldCheckRecordId'] = reviewParam1['companyCheckRecordId']
        taskParam1['reportState'] = 3
        taskParam1['companyCheckRecord.fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param['fireCompanyInfo.companyName'])
        taskParam1['companyCheckRecord.source'] = 1
        taskParam1['companyCheckRecord.checkType'] = 2
        taskParam1['companyName'] = Param['fireCompanyInfo.companyName']
        taskParam1['address'] = Param['fireCompanyInfo.address'] 
        taskParam1['manger'] = Param['fireCompanyInfo.manger'] 
        taskParam1['managerTelephone'] = Param['fireCompanyInfo.managerTelephone'] 
        taskParam1['companyCheckRecord_assignUserVoto'] = userInit['DftSheQuUserXM']
        taskParam1['companyCheckRecord.assignUser'] = userInit['DftSheQuUser']
        taskParam1['companyCheckRecord_assignDeptVo'] = orgInit['DftSheQuOrg']
        taskParam1['companyCheckRecord.assignDept'] = orgInit['DftSheQuOrgId']
        responseDict = YinHuanDuGaiIntf.saveCompanyCheckRecordTask(taskParam1, username=userInit['DftWangGeUser1'], password='11111111')

        #上报后，在社区的上报督改模块查看上报内容
        checkParam = copy.deepcopy(YinHuanDuGaiPara.checkSaveFiretrapSuperviseDict) 
        checkParam['companyName'] = Param['fireCompanyInfo.companyName']
        checkParam['fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param['fireCompanyInfo.companyName'])
        responseDict = YinHuanDuGaiIntf.check_saveFiretrapSupervise(checkParam,orgId=orgInit['DftSheQuOrgId'], allStateSearch='0',publicString='3',username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict, '检查失败')

        #社区——上报督改模块对改记录进行检查
        Param2 = copy.deepcopy(YinHuanDuGaiPara.saveFiretrapSuperviseDict) 
        Param2['isReportFlag'] = 0 
        Param2['calCheckResult'] = Param1['checkResult'] 
        Param2['firetrapSupervise.superviseNo'] = 'DG2016061700003'
        Param2['companyName'] = Param['fireCompanyInfo.companyName']
        Param2['checkDate'] = Time.getCurrentDate()
        Param2['firetrapSupervise.checkAddress'] = Param['fireCompanyInfo.address'] 
        Param2['firetrapSupervise.checkPlace'] = Param['fireCompanyInfo.companyName']
        Param2['checkItemIndexs'] = '1.'
        Param2['checkItemCodes'] = '%s#'% CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_item_id from supervise_type_item t where t.supervise_item_id =%s and t.supervise_type_id =%s"%(CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_item_id from supervise_item t where t.name ='安全出口疏散通道数量不足'"),CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg'] )))  #隐患项
        Param2['firetrapSupervise.reviseDate'] = Time.getCurrentDate()  #整改日期
        Param2['firetrapSupervise.manageName'] = Param['fireCompanyInfo.manger']
        Param2['companyCheckRecord_assignUserNameVo'] = userInit['DftJieDaoUserXM']
        Param2['companyCheckRecord_assignUserVo'] = userInit['DftJieDaoUser']
        Param2['companyCheckRecord_levelOrg'] = '村（社区）'
        Param2['companyCheckRecordlevel'] = '乡镇（街道）'
        Param2['companyCheckRecordOrgId'] = orgInit['DftJieDaoOrgId']
        Param2['user.userName'] = userInit['DftJieDaoUser']
        Param2['user.name'] = userInit['DftJieDaoUserXM']
        Param2['user.organization.id'] = orgInit['DftJieDaoOrgId']
        Param2['calculationMode'] = 0
        Param2['firetrapSupervise.signDate'] = Time.getCurrentDate()
        Param2['firetrapSupervise.superviseUserName'] = userInit['DftSheQuUserXM'] 
        Param2['firetrapSupervise.superviseUser'] = userInit['DftSheQuUser'] 
        Param2['firetrapSupervise.superviseDate'] = Time.getCurrentDate()
        Param2['operateMode'] = 'add'
        Param2['firetrapSupervise.superviseState'] = 1
        Param2['firetrapSupervise.updateDept'] = orgInit['DftSheQuOrgId']
        Param2['firetrapSupervise.createDept'] = orgInit['DftSheQuOrgId']
        Param2['firetrapSupervise.companyCheckRecordId'] =  CommonIntf.getDbQueryResult(dbCommand = "select t.company_check_record_id from firetrap_supervise t where t.check_place='%s'and t.update_user='%s'"%(Param['fireCompanyInfo.companyName'],userInit['DftWangGeUser1'])) +1
        Param2['superviseTypeId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg'] )
        Param2['companyCheckRecord.companyManager'] = Param['fireCompanyInfo.manger']
        Param2['companyCheckRecord.assignUser'] = userInit['DftSheQuUser'] 
        Param2['companyCheckRecord.assignDept'] = orgInit['DftSheQuOrgId']
        Param2['companyCheckRecord.checkType'] = 1
        Param2['companyCheckRecord.companyCheckRecordId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.company_check_record_id from firetrap_supervise t where t.check_place='%s'and t.update_user='%s'"%(Param['fireCompanyInfo.companyName'],userInit['DftWangGeUser1']))
        Param2['companyCheckRecord.checkUser'] = userInit['DftWangGeUser1'] 
        Param2['companyCheckRecord.fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param['fireCompanyInfo.companyName']) #被检查单位的id
        Param2['companyCheckRecord.checkDate'] = Time.getCurrentDate()
        Param2['checkResult'] = '一般'
        responseDict = YinHuanDuGaiIntf.saveFiretrapSupervise(Param2, username=userInit['DftSheQuUser'], password='11111111')

        #复查
        reviewParam2 = copy.deepcopy(YinHuanDuGaiPara.saveFiretrapReviewDict) 
        reviewParam2['calculationMode'] = 0
        reviewParam2['superviseState'] = 1
        reviewParam2['firetrapReview.firetrapReviewNo'] = 'FC2016061700002'
        reviewParam2['companyName'] = Param['fireCompanyInfo.companyName']
        reviewParam2['superviseNo'] = Param2['firetrapSupervise.superviseNo']
        reviewParam2['reviewItems[0].id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_item_id from supervise_type_item t where t.supervise_item_id =%s and t.supervise_type_id =%s"%(CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_item_id from supervise_item t where t.name ='安全出口疏散通道数量不足'"),CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg'] )))  #隐患项
        reviewParam2['reviewItems[0].checkItemId'] = CommonIntf.getDbQueryResult(dbCommand = "select  p.check_item_id from check_item  p where p.firetrap_supervise_id=%s"%CommonIntf.getDbQueryResult(dbCommand = "select t.firetrap_supervise_id from firetrap_supervise t where t.check_place='%s'and t.create_user ='%s'"%(Param['fireCompanyInfo.companyName'],userInit['DftSheQuUser'])))#"%Param['fireCompanyInfo.companyName'])) +1
        reviewParam2['reviewItems[0].state'] = 1
        reviewParam2['firetrapReview.reviseState'] = 1 
        reviewParam2['firetrapReview.reviewState'] = 1
        reviewParam2['firetrapReview.reviewPersonName'] = userInit['DftSheQuUserXM']
        reviewParam2['firetrapReview.reviewPerson'] = userInit['DftSheQuUser']
        reviewParam2['firetrapReview.reviewDate'] = Time.getCurrentDate()
        reviewParam2['companyCheckRecordId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.company_check_record_id from firetrap_supervise t where t.check_place='%s'and t.create_user ='%s'"%(Param['fireCompanyInfo.companyName'],userInit['DftSheQuUser']))#"%Param['fireCompanyInfo.companyName']) +1
        reviewParam2['operateMode'] = 'add'
        reviewParam2['firetrapReview.updateDept'] = orgInit['DftSheQuOrgId'] 
        reviewParam2['firetrapReview.createDept'] = orgInit['DftSheQuOrgId'] 
        reviewParam2['firetrapReview.firetrapSuperviseId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.firetrap_supervise_id from firetrap_supervise t where t.check_place='%s'and t.create_user ='%s'"%(Param['fireCompanyInfo.companyName'],userInit['DftSheQuUser']))#"%Param['fireCompanyInfo.companyName']) +1
        responseDict = YinHuanDuGaiIntf.SaveFiretrapReview(reviewParam2, username=userInit['DftSheQuUser'], password='11111111')

        #结果为一般的复查不合格上报给街道
        taskParam2 = copy.deepcopy(YinHuanDuGaiPara.saveCompanyCheckRecordTaskDict) 
        taskParam2['oldCheckRecordId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.company_check_record_id from firetrap_supervise t where t.check_place='%s'and t.create_user ='%s'"%(Param['fireCompanyInfo.companyName'],userInit['DftSheQuUser'])) 
        taskParam2['reportState'] = 3
        taskParam2['companyCheckRecord.fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param['fireCompanyInfo.companyName'])
        taskParam2['companyCheckRecord.source'] = 1
        taskParam2['companyCheckRecord.checkType'] = 3
        taskParam2['companyName'] = Param['fireCompanyInfo.companyName']
        taskParam2['address'] = Param['fireCompanyInfo.address'] 
        taskParam2['manger'] = Param['fireCompanyInfo.manger'] 
        taskParam2['managerTelephone'] = Param['fireCompanyInfo.managerTelephone'] 
        taskParam2['companyCheckRecord_assignUserVoto'] = '自动化街道用户1'#userInit['DftJieDaoUserXM']
        taskParam2['companyCheckRecord.assignUser'] = 'zdhjd1@'#userInit['DftJieDaoUser']
        taskParam2['companyCheckRecord_assignDeptVo'] = orgInit['DftJieDaoOrg']
        taskParam2['companyCheckRecord.assignDept'] = orgInit['DftJieDaoOrgId']
        responseDict = YinHuanDuGaiIntf.saveCompanyCheckRecordTask(taskParam2, username=userInit['DftSheQuUser'], password='11111111')
   
        #上报后，在街道的上报督改模块查看上报内容
        checkParam = copy.deepcopy(YinHuanDuGaiPara.checkSaveFiretrapSuperviseDict) 
        checkParam['companyName'] = Param['fireCompanyInfo.companyName']
        checkParam['fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param['fireCompanyInfo.companyName'])
        responseDict = YinHuanDuGaiIntf.check_saveFiretrapSupervise(checkParam,orgId=orgInit['DftJieDaoOrgId'], allStateSearch='0',publicString='3',username='zdhjd1@', password='11111111')
        self.assertTrue(responseDict, '检查失败')

        pass


    '''
    @功能：新建专项任务增删改查 
    @ chenyan 2016-6-22
    '''
    def testSaveFirecheckTask(self):
        """新建专项任务增删改查 """
        #新增专项任务
        Param1 = copy.deepcopy(YinHuanDuGaiPara.SaveFirecheckTaskDict) 
        Param1['mode'] = 'add'  
        Param1['firecheckTask.taskName'] = '专项任务%s'%CommonUtil.createRandomString()
        Param1['firecheckTask.dateFrom'] = Time.getCurrentDate()
        Param1['firecheckTask.dateTo'] = Time.getCurrentDate()
        Param1['firecheckTask.rentHouseCatalogue'] = '1001101'
        Param1['firecheckTask.everyRandomNum'] = '1'
        responseDict = YinHuanDuGaiIntf.saveFirecheckTask(Param1, username=userInit['DftJieDaoUser'], password='11111111')

        #修改专项任务
        Param2 = copy.deepcopy(YinHuanDuGaiPara.SaveFirecheckTaskDict) 
        Param2['mode'] = 'edit'  
        Param2['firecheckTask.firecheckTaskId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.firecheck_task_id from firecheck_task t where t.task_name ='%s'"%Param1['firecheckTask.taskName'])
        Param2['firecheckTask.taskName'] = '修改专项任务%s'%CommonUtil.createRandomString()
        Param2['firecheckTask.dateFrom'] = Time.getCurrentDate()
        Param2['firecheckTask.dateTo'] = Time.getCurrentDate()
        Param2['firecheckTask.rentHouseCatalogue'] = '1001101'
        Param2['firecheckTask.everyRandomNum'] = '2'
        responseDict = YinHuanDuGaiIntf.saveFirecheckTask(Param2, username=userInit['DftJieDaoUser'], password='11111111')

        #列表中查看
        checkParam = copy.deepcopy(YinHuanDuGaiPara.checkFirecheckTaskDict) 
        checkParam['firecheckTaskId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.firecheck_task_id from firecheck_task t where t.task_name ='%s'"%Param2['firecheckTask.taskName'])
        checkParam['taskName'] = Param2['firecheckTask.taskName']
        responseDict = YinHuanDuGaiIntf.checkSaveFirecheckTask(checkParam,orgId=orgInit['DftJieDaoOrgId'], username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(responseDict, '检查失败')
        
        #删除专项任务
        deleteParam = copy.deepcopy(YinHuanDuGaiPara.deleteFirecheckTaskDict) 
        deleteParam['firecheckTaskId'] = checkParam['firecheckTaskId']
        responseDict = YinHuanDuGaiIntf.deleteSaveFirecheckTask(deleteParam,username=userInit['DftJieDaoUser'], password='11111111')

        checkParam = copy.deepcopy(YinHuanDuGaiPara.checkFirecheckTaskDict) 
        checkParam['firecheckTaskId'] = Param2['firecheckTask.firecheckTaskId']
        checkParam['taskName'] = Param2['firecheckTask.taskName']
        responseDict = YinHuanDuGaiIntf.checkSaveFirecheckTask(checkParam,orgId=orgInit['DftJieDaoOrgId'], username=userInit['DftJieDaoUser'], password='11111111')
        self.assertFalse(responseDict, '删除的专项在列表中依然存在，删除失败')
        pass

    '''
    @功能：专项任务任务分派
    @ chenyan 2016-6-23
    '''
    def testSaveTaskItem(self):
        """专项任务任务分派 """
        #新增单位01
        Param01 = copy.deepcopy(YinHuanDuGaiPara.fireCompanyDict) 
        Param01['mode'] = 'add'  
        Param01['fireCompanyInfo.createDept'] = orgInit['DftWangGeOrgId1']
        Param01['fireCompanyInfo.importOrAdd'] = '1'
        Param01['fireCompanyInfo.orgPathName'] = '%s%s%s%s%s'%(orgInit['DftShiOrg'],orgInit['DftQuOrg'],orgInit['DftJieDaoOrg'],orgInit['DftSheQuOrg'],orgInit['DftWangGeOrg1'])
        Param01['fireCompanyInfo.companyName'] = '测试单位%s'%CommonUtil.createRandomString()
        Param01['fireCompanyInfo.orgid'] = Param01['fireCompanyInfo.createDept']
        Param01['companySuperviseTypeIsChange'] = 'true'
        Param01['fireCompanyInfo.superviseTypeName'] = '其他一般单位'
        Param01['fireCompanyInfo.superviseType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg'])
        Param01['fireCompanyInfo.address'] = '测试地址'
        Param01['fireCompanyInfo.manger'] = '测试姓名'
        Param01['fireCompanyInfo.managerTelephone'] = '18710000000'
        Param01['fireCompanyInfo.rentHousePerson'] = '0'
        Param01['fireCompanyInfo.industrialCatalogue'] = CommonIntf.getDbQueryResult(dbCommand = "select t.code from fire_company_type t where t.name='电器'")  #行业类别
        Param01['businessLicense'] = '1'
        Param01['firelicense'] = '1'
        responseDict = YinHuanDuGaiIntf.addOrEdit_fireCompany(Param01, username=userInit['DftWangGeUser1'], password='11111111')
        
        #新增专项任务1
        Param1 = copy.deepcopy(YinHuanDuGaiPara.SaveFirecheckTaskDict) 
        Param1['mode'] = 'add'  
        Param1['firecheckTask.taskName'] = '专项任务1%s'%CommonUtil.createRandomString()
        Param1['firecheckTask.dateFrom'] = Time.getCurrentDate()
        Param1['firecheckTask.dateTo'] = Time.getCurrentDate()
        Param1['firecheckTask.rentHouseCatalogue'] = '1001101'
        Param1['firecheckTask.everyRandomNum'] = '1'
        responseDict = YinHuanDuGaiIntf.saveFirecheckTask(Param1, username=userInit['DftJieDaoUser'], password='11111111')

        #分派专项任务——分派给社区
        saveTaskParam = copy.deepcopy(YinHuanDuGaiPara.SaveTaskItemDict) 
        saveTaskParam['firecheckTaskId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.firecheck_task_id from firecheck_task t where t.task_name ='%s'"%Param1['firecheckTask.taskName']) 
        saveTaskParam['userLoginId'] = userInit['DftSheQuUser']
        saveTaskParam['orgId'] = orgInit['DftSheQuOrgId']
        saveTaskParam['companyIdList'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param01['fireCompanyInfo.companyName'])
        responseDict = YinHuanDuGaiIntf.saveTaskItem(saveTaskParam, username=userInit['DftJieDaoUser'], password='11111111')

        #保存分派专项任务
        saveParam = copy.deepcopy(YinHuanDuGaiPara.SaveTaskItemDict) 
        saveParam['firecheckTaskId'] = saveTaskParam['firecheckTaskId'] 
        responseDict = YinHuanDuGaiIntf.saveItem(saveParam, username=userInit['DftJieDaoUser'], password='11111111')

        #社区专项任务检查列表中查看
        checkParam = copy.deepcopy(YinHuanDuGaiPara.checkSaveFiretrapSuperviseDict) 
        checkParam['companyName'] = Param01['fireCompanyInfo.companyName'] 
        checkParam['fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param01['fireCompanyInfo.companyName'])
        response = YinHuanDuGaiIntf.check_saveTaskItem(checkParam,state='111',orgId=orgInit['DftSheQuOrgId'], allStateSearch='0',publicString='5',username=userInit['DftSheQuUser'], password='11111111')
        for item in response['rows']:
            if item['fireCompanyInfo']['companyName']==Param01['fireCompanyInfo.companyName']:
                #专项任务检查
                superviseParam = copy.deepcopy(YinHuanDuGaiPara.saveFiretrapSuperviseDict) 
                superviseParam['isReportFlag'] = 0 
                superviseParam['calCheckResult'] = 'flag' 
                superviseParam['firetrapSupervise.superviseNo'] = 'DG2016062300001'
                superviseParam['companyName'] = Param01['fireCompanyInfo.companyName']
                superviseParam['checkDate'] = Time.getCurrentDate()
                superviseParam['firetrapSupervise.checkAddress'] = Param01['fireCompanyInfo.address'] 
                superviseParam['firetrapSupervise.checkPlace'] = Param01['fireCompanyInfo.companyName']
                superviseParam['checkItemIndexs'] = '1.'
                superviseParam['checkItemCodes'] = '%s#'% CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_item_id from supervise_type_item t where t.supervise_item_id =%s and t.supervise_type_id =%s"%(CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_item_id from supervise_item t where t.name ='安全出口疏散通道数量不足'"),CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg'] )))  #隐患项
                superviseParam['firetrapSupervise.reviseDate'] = Time.getCurrentDate()  #整改日期
                superviseParam['firetrapSupervise.manageName'] = Param01['fireCompanyInfo.manger']
                superviseParam['companyCheckRecord_assignUserNameVo'] = userInit['DftJieDaoUserXM']
                superviseParam['companyCheckRecord_assignUserVo'] = userInit['DftJieDaoUser']
                superviseParam['companyCheckRecord_levelOrg'] = '村（社区）'
                superviseParam['companyCheckRecordlevel'] = '乡镇（街道）'
                superviseParam['companyCheckRecordOrgId'] = orgInit['DftJieDaoOrgId']
                superviseParam['user.userName'] = userInit['DftJieDaoUser']
                superviseParam['user.name'] = userInit['DftJieDaoUserXM']
                superviseParam['user.organization.id'] = orgInit['DftJieDaoOrgId']
                superviseParam['calculationMode'] = 0
                superviseParam['firetrapSupervise.signDate'] = Time.getCurrentDate()
                superviseParam['firetrapSupervise.superviseUserName'] = userInit['DftSheQuUserXM'] 
                superviseParam['firetrapSupervise.superviseUser'] = userInit['DftSheQuUser'] 
                superviseParam['firetrapSupervise.superviseDate'] = Time.getCurrentDate()
                superviseParam['operateMode'] = 'add'
                superviseParam['firetrapSupervise.superviseState'] = 1
                superviseParam['firetrapSupervise.updateDept'] = orgInit['DftSheQuOrgId']
                superviseParam['firetrapSupervise.createDept'] = orgInit['DftSheQuOrgId']
                superviseParam['firetrapSupervise.companyCheckRecordId'] =  item['companyCheckRecordId']
                superviseParam['superviseTypeId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg'] )
                superviseParam['companyCheckRecord.companyManager'] = Param01['fireCompanyInfo.manger']
                superviseParam['companyCheckRecord.assignUser'] = userInit['DftSheQuUser'] 
                superviseParam['companyCheckRecord.assignDept'] = orgInit['DftSheQuOrgId']
                superviseParam['companyCheckRecord.checkType'] = 1
                superviseParam['companyCheckRecord.checkUser'] = userInit['DftWangGeUser1'] 
                superviseParam['companyCheckRecord.fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param01['fireCompanyInfo.companyName']) #被检查单位的id
                superviseParam['companyCheckRecord.checkDate'] = Time.getCurrentDate()
                superviseParam['checkResult'] = '一般'
                responseDict = YinHuanDuGaiIntf.saveFiretrapSupervise(superviseParam, username=userInit['DftSheQuUser'], password='11111111')
                
                #复查
                reviewParam2 = copy.deepcopy(YinHuanDuGaiPara.saveFiretrapReviewDict) 
                reviewParam2['calculationMode'] = 0
                reviewParam2['superviseState'] = 1
                reviewParam2['firetrapReview.firetrapReviewNo'] = 'FC2016062300002'
                reviewParam2['companyName'] = Param01['fireCompanyInfo.companyName']
                reviewParam2['superviseNo'] = superviseParam['firetrapSupervise.superviseNo']
                reviewParam2['reviewItems[0].id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_item_id from supervise_type_item t where t.supervise_item_id =%s and t.supervise_type_id =%s"%(CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_item_id from supervise_item t where t.name ='安全出口疏散通道数量不足'"),CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg'] )))  #隐患项
                reviewParam2['reviewItems[0].checkItemId'] = CommonIntf.getDbQueryResult(dbCommand = "select  p.check_item_id from check_item  p where p.firetrap_supervise_id=%s"%CommonIntf.getDbQueryResult(dbCommand = "select t.firetrap_supervise_id from firetrap_supervise t where t.check_place='%s'and t.create_user ='%s'"%(Param01['fireCompanyInfo.companyName'],userInit['DftSheQuUser'])))#"%Param['fireCompanyInfo.companyName'])) +1
                reviewParam2['reviewItems[0].state'] = 1
                reviewParam2['firetrapReview.reviseState'] = 1 
                reviewParam2['firetrapReview.reviewState'] = 1
                reviewParam2['firetrapReview.reviewPersonName'] = userInit['DftSheQuUserXM']
                reviewParam2['firetrapReview.reviewPerson'] = userInit['DftSheQuUser']
                reviewParam2['firetrapReview.reviewDate'] = Time.getCurrentDate()
                reviewParam2['companyCheckRecordId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.company_check_record_id from firetrap_supervise t where t.check_place='%s'and t.create_user ='%s'"%(Param01['fireCompanyInfo.companyName'],userInit['DftSheQuUser']))#"%Param['fireCompanyInfo.companyName']) +1
                reviewParam2['operateMode'] = 'add'
                reviewParam2['firetrapReview.updateDept'] = orgInit['DftSheQuOrgId'] 
                reviewParam2['firetrapReview.createDept'] = orgInit['DftSheQuOrgId'] 
                reviewParam2['firetrapReview.firetrapSuperviseId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.firetrap_supervise_id from firetrap_supervise t where t.check_place='%s'and t.create_user ='%s'"%(Param01['fireCompanyInfo.companyName'],userInit['DftSheQuUser']))#"%Param['fireCompanyInfo.companyName']) +1
                responseDict = YinHuanDuGaiIntf.SaveFiretrapReview(reviewParam2, username=userInit['DftSheQuUser'], password='11111111')

                #结果为一般的复查不合格上报给街道
                taskParam2 = copy.deepcopy(YinHuanDuGaiPara.saveCompanyCheckRecordTaskDict) 
                taskParam2['oldCheckRecordId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.company_check_record_id from firetrap_supervise t where t.check_place='%s'and t.create_user ='%s'"%(Param01['fireCompanyInfo.companyName'],userInit['DftSheQuUser'])) 
                taskParam2['reportState'] = 3
                taskParam2['companyCheckRecord.fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param01['fireCompanyInfo.companyName'])
                taskParam2['companyCheckRecord.source'] = 1
                taskParam2['companyCheckRecord.checkType'] = 3
                taskParam2['companyName'] = Param01['fireCompanyInfo.companyName']
                taskParam2['address'] = Param01['fireCompanyInfo.address'] 
                taskParam2['manger'] = Param01['fireCompanyInfo.manger'] 
                taskParam2['managerTelephone'] = Param01['fireCompanyInfo.managerTelephone'] 
                taskParam2['companyCheckRecord_assignUserVoto'] = '自动化街道用户1'#userInit['DftJieDaoUserXM']
                taskParam2['companyCheckRecord.assignUser'] = 'zdhjd1@'#userInit['DftJieDaoUser']
                taskParam2['companyCheckRecord_assignDeptVo'] = orgInit['DftJieDaoOrg']
                taskParam2['companyCheckRecord.assignDept'] = orgInit['DftJieDaoOrgId']
                responseDict = YinHuanDuGaiIntf.saveCompanyCheckRecordTask(taskParam2, username=userInit['DftSheQuUser'], password='11111111')
           
                #上报后，在街道的上报督改模块查看上报内容
                checkParam = copy.deepcopy(YinHuanDuGaiPara.checkSaveFiretrapSuperviseDict) 
                checkParam['companyName'] = Param01['fireCompanyInfo.companyName']
                checkParam['fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param01['fireCompanyInfo.companyName'])
                responseDict = YinHuanDuGaiIntf.check_saveFiretrapSupervise(checkParam,orgId=orgInit['DftJieDaoOrgId'], allStateSearch='0',publicString='3',username='zdhjd1@', password='11111111')
                self.assertTrue(responseDict, '检查失败')

        #新增单位02
        Param02 = copy.deepcopy(YinHuanDuGaiPara.fireCompanyDict) 
        Param02['mode'] = 'add'  
        Param02['fireCompanyInfo.createDept'] = orgInit['DftWangGeOrgId1']
        Param02['fireCompanyInfo.importOrAdd'] = '1'
        Param02['fireCompanyInfo.orgPathName'] = '%s%s%s%s%s'%(orgInit['DftShiOrg'],orgInit['DftQuOrg'],orgInit['DftJieDaoOrg'],orgInit['DftSheQuOrg'],orgInit['DftWangGeOrg1'])
        Param02['fireCompanyInfo.companyName'] = '测试单位%s'%CommonUtil.createRandomString()
        Param02['fireCompanyInfo.orgid'] = Param01['fireCompanyInfo.createDept']
        Param02['companySuperviseTypeIsChange'] = 'true'
        Param02['fireCompanyInfo.superviseTypeName'] = '其他一般单位'
        Param02['fireCompanyInfo.superviseType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg'])
        Param02['fireCompanyInfo.address'] = '测试地址'
        Param02['fireCompanyInfo.manger'] = '测试姓名'
        Param02['fireCompanyInfo.managerTelephone'] = '18710000000'
        Param02['fireCompanyInfo.rentHousePerson'] = '0'
        Param02['fireCompanyInfo.industrialCatalogue'] = CommonIntf.getDbQueryResult(dbCommand = "select t.code from fire_company_type t where t.name='电器'")  #行业类别
        Param02['businessLicense'] = '1'
        Param02['firelicense'] = '1'
        responseDict = YinHuanDuGaiIntf.addOrEdit_fireCompany(Param02, username=userInit['DftWangGeUser1'], password='11111111')

        #新增专项任务2
        Param2 = copy.deepcopy(YinHuanDuGaiPara.SaveFirecheckTaskDict) 
        Param2['mode'] = 'add'  
        Param2['firecheckTask.taskName'] = '专项任务2%s'%CommonUtil.createRandomString()
        Param2['firecheckTask.dateFrom'] = Time.getCurrentDate()
        Param2['firecheckTask.dateTo'] = Time.getCurrentDate()
        Param2['firecheckTask.rentHouseCatalogue'] = '1001101'
        Param2['firecheckTask.everyRandomNum'] = '1'
        responseDict = YinHuanDuGaiIntf.saveFirecheckTask(Param2, username=userInit['DftJieDaoUser'], password='11111111')
 
        #分派专项任务——分派给社区
        saveTaskParam2 = copy.deepcopy(YinHuanDuGaiPara.SaveTaskItemDict) 
        saveTaskParam2['firecheckTaskId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.firecheck_task_id from firecheck_task t where t.task_name ='%s'"%Param1['firecheckTask.taskName']) 
        saveTaskParam2['userLoginId'] = userInit['DftSheQuUser']
        saveTaskParam2['orgId'] = orgInit['DftSheQuOrgId']
        saveTaskParam2['companyIdList'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param02['fireCompanyInfo.companyName'])
        responseDict = YinHuanDuGaiIntf.saveTaskItem(saveTaskParam2, username=userInit['DftJieDaoUser'], password='11111111')
 
        #保存分派专项任务
        saveParam2 = copy.deepcopy(YinHuanDuGaiPara.SaveTaskItemDict) 
        saveParam2['firecheckTaskId'] = saveTaskParam['firecheckTaskId'] 
        responseDict = YinHuanDuGaiIntf.saveItem(saveParam2, username=userInit['DftJieDaoUser'], password='11111111')
 
        #搜索社区专项任务检查
        searchParam = copy.deepcopy(YinHuanDuGaiPara.checkSaveFiretrapSuperviseDict) 
        searchParam['companyName'] = Param02['fireCompanyInfo.companyName'] 
        searchParam['fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param02['fireCompanyInfo.companyName'])
        response = YinHuanDuGaiIntf.check_saveTaskItem(searchParam,state='111',orgId=orgInit['DftSheQuOrgId'], companyName=Param02['fireCompanyInfo.companyName'],allStateSearch='0',publicString='5',username=userInit['DftSheQuUser'], password='11111111')
        for item in response['rows']:
            if item['fireCompanyInfo']['companyName']==Param02['fireCompanyInfo.companyName']:
                #删除专项任务
                deleteParam = copy.deepcopy(YinHuanDuGaiPara.deleteSaveFiretrapSuperviseDict) 
                deleteParam['ids'] = item['companyCheckRecordId']
                responseDict = YinHuanDuGaiIntf.delete_saveTaskItem(checkParam,username=userInit['DftWangGeUser1'], password='11111111')

                #检查删除专项任务信息
                checkParam = copy.deepcopy(YinHuanDuGaiPara.checkSaveFiretrapSuperviseDict) 
                checkParam['companyName'] = Param02['fireCompanyInfo.companyName'] 
                checkParam['fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param02['fireCompanyInfo.companyName'])
                response = YinHuanDuGaiIntf.check_saveTaskItem(checkParam,state='111',orgId=orgInit['DftSheQuOrgId'], allStateSearch='0',publicString='5',username=userInit['DftSheQuUser'], password='11111111')
#                 self.assertFalse(responseDict, '删除的专项任务在列表中依然存在，删除失败')

    '''
    @功能：上级分派检查   ——>新增单位，行业类别空？
    @ chenyan 2016-6-24
    '''
    def testAssignCheckRecord(self):
        """上级分派检查"""
        #新增单位
        Param01 = copy.deepcopy(YinHuanDuGaiPara.fireCompanyDict) 
        Param01['mode'] = 'add'  
        Param01['fireCompanyInfo.createDept'] = orgInit['DftQuOrgId'] 
        Param01['fireCompanyInfo.belongDept'] = orgInit['DftJieDaoOrgId']
        Param01['fireCompanyInfo.importOrAdd'] = '1'
        Param01['fireCompanyInfo.orgPathName'] = '%s%s%s%s%s'%(orgInit['DftShiOrg'],orgInit['DftQuOrg'],orgInit['DftJieDaoOrg'],'请选择','请选择')
        Param01['fireCompanyInfo.companyNo'] = '09696969600000000008'
        Param01['fireCompanyInfo.companyName'] = '测试单位%s'%CommonUtil.createRandomString()
        Param01['fireCompanyInfo.orgid'] = Param01['fireCompanyInfo.belongDept']
        Param01['companySuperviseTypeIsChange'] = 'true'
        Param01['fireCompanyInfo.superviseTypeName'] = '其他一般单位'
        Param01['fireCompanyInfo.superviseType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg']) 
        Param01['fireCompanyInfo.address'] = '测试地址'
        Param01['fireCompanyInfo.manger'] = '测试姓名'
        Param01['fireCompanyInfo.managerTelephone'] = '18710000000'
        Param01['fireCompanyInfo.rentHousePerson'] = '0'
        Param01['fireCompanyInfo.industrialCatalogue'] = CommonIntf.getDbQueryResult(dbCommand = "select t.code from fire_company_type t where t.name='电器'")  #行业类别
        Param01['businessLicense'] = '1'
        Param01['firelicense'] = '1'
        responseDict = YinHuanDuGaiIntf.addOrEdit_fireCompany(Param01, username=userInit['DftQuUser'], password='11111111')


        #添加日常检查
        Param1 = copy.deepcopy(YinHuanDuGaiPara.saveFiretrapSuperviseDict) 
        Param1['isReportFlag'] = 0 
        Param1['calCheckResult'] = 'flag'
        Param1['firetrapSupervise.superviseNo'] = 'DG2016062400002'
        Param1['companyName'] = Param01['fireCompanyInfo.companyName']
        Param1['checkDate'] = Time.getCurrentDate()
        Param1['firetrapSupervise.checkAddress'] = Param01['fireCompanyInfo.address'] 
        Param1['firetrapSupervise.checkPlace'] = Param01['fireCompanyInfo.companyName']
        Param1['checkItemIndexs'] = '1.'
        Param1['checkItemCodes'] = '%s#'% CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_item_id from supervise_type_item t where t.supervise_item_id =%s and t.supervise_type_id =%s"%(CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_item_id from supervise_item t where t.name ='安全出口疏散通道数量不足'"),CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg'] )))  #隐患项
        Param1['firetrapSupervise.reviseDate'] = Time.getCurrentDate()  #整改日期
        Param1['firetrapSupervise.manageName'] = Param01['fireCompanyInfo.manger']
        Param1['companyCheckRecord_assignUserNameVo'] = '自动化街道用户1'#userInit['DftJieDaoUserXM']
        Param1['companyCheckRecord_assignUserVo'] = 'zdhjd1@'# userInit['DftJieDaoUser']
        Param1['companyCheckRecord_levelOrg'] = '县（区）'
        Param1['companyCheckRecordOrgId'] = orgInit['DftJieDaoOrgId']
        Param1['user.userName'] = 'zdhjd1@'#userInit['DftJieDaoUser']
        Param1['user.name'] =  '自动化街道用户1'#userInit['DftJieDaoUserXM']
        Param1['user.organization.id'] = orgInit['DftJieDaoOrgId']
        Param1['calculationMode'] = 0
        Param1['firetrapSupervise.signDate'] = Time.getCurrentDate()
        Param1['firetrapSupervise.superviseUserName'] = userInit['DftQuUserXM'] 
        Param1['firetrapSupervise.superviseUser'] = userInit['DftQuUser'] 
        Param1['firetrapSupervise.superviseDate'] = Time.getCurrentDate()
        Param1['operateMode'] = 'add'
        Param1['firetrapSupervise.superviseState'] = 1
        Param1['superviseTypeId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg'] )
        Param1['companyCheckRecord.companyManager'] = Param01['fireCompanyInfo.manger']
        Param1['companyCheckRecord.assignUser'] = userInit['DftQuUser'] 
        Param1['companyCheckRecord.assignDept'] = orgInit['DftQuOrgId']
        Param1['companyCheckRecord.checkType'] = 1
        Param1['companyCheckRecord.checkUser'] = userInit['DftQuUser']
        Param1['companyCheckRecord.fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param01['fireCompanyInfo.companyName']) #被检查单位的id
        Param1['companyCheckRecord.checkDate'] = Time.getCurrentDate()
        Param1['checkResult'] = '一般'
        responseDict = YinHuanDuGaiIntf.saveFiretrapSupervise(Param1, username=userInit['DftQuUser'], password='11111111')
  
        checkParam = copy.deepcopy(YinHuanDuGaiPara.checkSaveFiretrapSuperviseDict) 
        checkParam['companyName'] = Param01['fireCompanyInfo.companyName']
        checkParam['fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param01['fireCompanyInfo.companyName'])
        response = YinHuanDuGaiIntf.check_saveFiretrapSupervise(checkParam,orgId=orgInit['DftQuOrgId'], allStateSearch='1',publicString='1',username=userInit['DftQuUser'], password='11111111')
        for item in response['rows']:
            if item['fireCompanyInfo']['companyName']==Param01['fireCompanyInfo.companyName']:
                #分派检查
                Param = copy.deepcopy(YinHuanDuGaiPara.assignCheckRecordDict) 
                Param['companyCheckRecord.companyCheckRecordId'] =  item['companyCheckRecordId']
                Param['companyCheckRecord.source'] = '1'
                responseDict = YinHuanDuGaiIntf.assignCheckRecord(Param, username=userInit['DftQuUser'], password='11111111')
                  
                checkParam = copy.deepcopy(YinHuanDuGaiPara.checkSaveFiretrapSuperviseDict) 
                checkParam['companyName'] = Param01['fireCompanyInfo.companyName']
                checkParam['fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param01['fireCompanyInfo.companyName'])
                response = YinHuanDuGaiIntf.check_assignCheckRecord(checkParam,orgId=orgInit['DftJieDaoOrgId'], allStateSearch='0',publicString='6',username=userInit['DftJieDaoUser'], password='11111111')
                pass


    '''
    @功能：下辖检查记录 ——（以日常量化检查为例，接口一致publicString不同，日常1、上报3、举报4）
    @ chenyan 2016-6-24
    '''
    def testSubordinateList(self):
        """下辖检查记录"""
        #新增单位
        Param = copy.deepcopy(YinHuanDuGaiPara.fireCompanyDict) 
        Param['mode'] = 'add'  
        Param['fireCompanyInfo.createDept'] = orgInit['DftSheQuOrgId'] 
        Param['fireCompanyInfo.importOrAdd'] = '1'
        Param['fireCompanyInfo.orgPathName'] = '%s%s%s%s%s'%(orgInit['DftShiOrg'],orgInit['DftQuOrg'],orgInit['DftJieDaoOrg'],orgInit['DftSheQuOrg'],'请选择')
        Param['fireCompanyInfo.companyName'] = '测试单位%s'%CommonUtil.createRandomString()
        Param['fireCompanyInfo.orgid'] = Param['fireCompanyInfo.createDept']
        Param['companySuperviseTypeIsChange'] = 'true'
        Param['fireCompanyInfo.superviseTypeName'] = '其他一般单位'
        Param['fireCompanyInfo.superviseType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg']) 
        Param['fireCompanyInfo.address'] = '测试地址'
        Param['fireCompanyInfo.manger'] = '测试姓名'
        Param['fireCompanyInfo.managerTelephone'] = '18710000000'
        Param['fireCompanyInfo.rentHousePerson'] = '0'
        Param['fireCompanyInfo.industrialCatalogue'] = CommonIntf.getDbQueryResult(dbCommand = "select t.code from fire_company_type t where t.name='电器'")  #行业类别
        Param['businessLicense'] = '1'
        Param['firelicense'] = '1'
        responseDict = YinHuanDuGaiIntf.addOrEdit_fireCompany(Param, username=userInit['DftSheQuUser'], password='11111111')

        #添加日常检查1
        Param1 = copy.deepcopy(YinHuanDuGaiPara.saveFiretrapSuperviseDict) 
        Param1['isReportFlag'] = 0 
        Param1['calCheckResult'] = 'flage'
        Param1['firetrapSupervise.superviseNo'] = 'DG2016062400003'
        Param1['companyName'] = Param['fireCompanyInfo.companyName']
        Param1['checkDate'] = Time.getCurrentDate()
        Param1['firetrapSupervise.checkAddress'] = Param['fireCompanyInfo.address'] 
        Param1['firetrapSupervise.checkPlace'] = Param['fireCompanyInfo.companyName']
        Param1['checkItemIndexs'] = '1.'
        Param1['checkItemCodes'] = '%s#'% CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_item_id from supervise_type_item t where t.supervise_item_id =%s and t.supervise_type_id =%s"%(CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_item_id from supervise_item t where t.name ='安全出口疏散通道数量不足'"),CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg'] )))  #隐患项
        Param1['firetrapSupervise.reviseDate'] = Time.getCurrentDate()  #整改日期
        Param1['firetrapSupervise.manageName'] = Param['fireCompanyInfo.manger']
        Param1['companyCheckRecord_assignUserNameVo'] = userInit['DftJieDaoUserXM']
        Param1['companyCheckRecord_assignUserVo'] = userInit['DftJieDaoUser']
        Param1['companyCheckRecord_levelOrg'] = '村（社区）'
        Param1['companyCheckRecordlevel'] = '乡镇（街道）'
        Param1['companyCheckRecordOrgId'] = orgInit['DftJieDaoOrgId']
        Param1['user.userName'] = userInit['DftJieDaoUser']
        Param1['user.name'] = userInit['DftJieDaoUserXM']
        Param1['user.organization.id'] = orgInit['DftJieDaoOrgId']
        Param1['calculationMode'] = 0
        Param1['firetrapSupervise.signDate'] = Time.getCurrentDate()
        Param1['firetrapSupervise.superviseUserName'] = userInit['DftSheQuUserXM'] 
        Param1['firetrapSupervise.superviseUser'] = userInit['DftSheQuUser'] 
        Param1['firetrapSupervise.superviseDate'] = Time.getCurrentDate()
        Param1['operateMode'] = 'add'
        Param1['firetrapSupervise.superviseState'] = 1
        Param1['firetrapSupervise.updateDept'] = orgInit['DftSheQuOrgId']
        Param1['firetrapSupervise.createDept'] = orgInit['DftSheQuOrgId']
        Param1['firetrapSupervise.companyCheckRecordId'] =  CommonIntf.getDbQueryResult(dbCommand = "select t.company_check_record_id from firetrap_supervise t where t.check_place='%s'and t.update_user='%s'"%(Param['fireCompanyInfo.companyName'],userInit['DftWangGeUser1']))
        Param1['superviseTypeId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg'] )
        Param1['companyCheckRecord.companyManager'] = Param['fireCompanyInfo.manger']
        Param1['companyCheckRecord.assignUser'] = userInit['DftSheQuUser'] 
        Param1['companyCheckRecord.assignDept'] = orgInit['DftSheQuOrgId']
        Param1['companyCheckRecord.checkType'] = 1
        Param1['companyCheckRecord.companyCheckRecordId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.company_check_record_id from firetrap_supervise t where t.check_place='%s'and t.update_user='%s'"%(Param['fireCompanyInfo.companyName'],userInit['DftWangGeUser1']))
        Param1['companyCheckRecord.checkUser'] = userInit['DftWangGeUser1'] 
        Param1['companyCheckRecord.fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param['fireCompanyInfo.companyName']) #被检查单位的id
        Param1['companyCheckRecord.checkDate'] = Time.getCurrentDate()
        Param1['checkResult'] = '一般'
        responseDict = YinHuanDuGaiIntf.saveFiretrapSupervise(Param1, username=userInit['DftSheQuUser'], password='11111111')

        #新增单位2
        Param02 = copy.deepcopy(YinHuanDuGaiPara.fireCompanyDict) 
        Param02['mode'] = 'add'  
        Param02['fireCompanyInfo.createDept'] = orgInit['DftSheQuOrgId'] 
        Param02['fireCompanyInfo.importOrAdd'] = '1'
        Param02['fireCompanyInfo.orgPathName'] = '%s%s%s%s%s'%(orgInit['DftShiOrg'],orgInit['DftQuOrg'],orgInit['DftJieDaoOrg'],orgInit['DftSheQuOrg'],'请选择')
        Param02['fireCompanyInfo.companyName'] = '测试单位%s'%CommonUtil.createRandomString()
        Param02['fireCompanyInfo.orgid'] = Param02['fireCompanyInfo.createDept']
        Param02['companySuperviseTypeIsChange'] = 'true'
        Param02['fireCompanyInfo.superviseTypeName'] = '其他一般单位'
        Param02['fireCompanyInfo.superviseType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg']) 
        Param02['fireCompanyInfo.address'] = '测试地址'
        Param02['fireCompanyInfo.manger'] = '测试姓名'
        Param02['fireCompanyInfo.managerTelephone'] = '18710000000'
        Param02['fireCompanyInfo.rentHousePerson'] = '0'
        Param02['fireCompanyInfo.industrialCatalogue'] = CommonIntf.getDbQueryResult(dbCommand = "select t.code from fire_company_type t where t.name='电器'")  #行业类别
        Param02['businessLicense'] = '1'
        Param02['firelicense'] = '1'
        responseDict = YinHuanDuGaiIntf.addOrEdit_fireCompany(Param02, username=userInit['DftSheQuUser'], password='11111111')

        #添加日常检查2
        Param2 = copy.deepcopy(YinHuanDuGaiPara.saveFiretrapSuperviseDict) 
        Param2['isReportFlag'] = 0 
        Param2['calCheckResult'] = 'flage'
        Param2['firetrapSupervise.superviseNo'] = 'DG2016062400003'
        Param2['companyName'] = Param02['fireCompanyInfo.companyName']
        Param2['checkDate'] = Time.getCurrentDate()
        Param2['firetrapSupervise.checkAddress'] = Param02['fireCompanyInfo.address'] 
        Param2['firetrapSupervise.checkPlace'] = Param02['fireCompanyInfo.companyName']
        Param2['checkItemIndexs'] = '1.'
        Param2['checkItemCodes'] = '%s#'% CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_item_id from supervise_type_item t where t.supervise_item_id =%s and t.supervise_type_id =%s"%(CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_item_id from supervise_item t where t.name ='安全出口疏散通道数量不足'"),CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg'] )))  #隐患项
        Param2['firetrapSupervise.reviseDate'] = Time.getCurrentDate()  #整改日期
        Param2['firetrapSupervise.manageName'] = Param02['fireCompanyInfo.manger']
        Param2['companyCheckRecord_assignUserNameVo'] = userInit['DftJieDaoUserXM']
        Param2['companyCheckRecord_assignUserVo'] = userInit['DftJieDaoUser']
        Param2['companyCheckRecord_levelOrg'] = '村（社区）'
        Param2['companyCheckRecordlevel'] = '乡镇（街道）'
        Param2['companyCheckRecordOrgId'] = orgInit['DftJieDaoOrgId']
        Param2['user.userName'] = userInit['DftJieDaoUser']
        Param2['user.name'] = userInit['DftJieDaoUserXM']
        Param2['user.organization.id'] = orgInit['DftJieDaoOrgId']
        Param2['calculationMode'] = 0
        Param2['firetrapSupervise.signDate'] = Time.getCurrentDate()
        Param2['firetrapSupervise.superviseUserName'] = userInit['DftSheQuUserXM'] 
        Param2['firetrapSupervise.superviseUser'] = userInit['DftSheQuUser'] 
        Param2['firetrapSupervise.superviseDate'] = Time.getCurrentDate()
        Param2['operateMode'] = 'add'
        Param2['firetrapSupervise.superviseState'] = 1
        Param2['firetrapSupervise.updateDept'] = orgInit['DftSheQuOrgId']
        Param2['firetrapSupervise.createDept'] = orgInit['DftSheQuOrgId']
        Param2['firetrapSupervise.companyCheckRecordId'] =  CommonIntf.getDbQueryResult(dbCommand = "select t.company_check_record_id from firetrap_supervise t where t.check_place='%s'and t.update_user='%s'"%(Param02['fireCompanyInfo.companyName'],userInit['DftWangGeUser1']))
        Param2['superviseTypeId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg'] )
        Param2['companyCheckRecord.companyManager'] = Param02['fireCompanyInfo.manger']
        Param2['companyCheckRecord.assignUser'] = userInit['DftSheQuUser'] 
        Param2['companyCheckRecord.assignDept'] = orgInit['DftSheQuOrgId']
        Param2['companyCheckRecord.checkType'] = 1
        Param2['companyCheckRecord.companyCheckRecordId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.company_check_record_id from firetrap_supervise t where t.check_place='%s'and t.update_user='%s'"%(Param02['fireCompanyInfo.companyName'],userInit['DftWangGeUser1']))
        Param2['companyCheckRecord.checkUser'] = userInit['DftWangGeUser1'] 
        Param2['companyCheckRecord.fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param02['fireCompanyInfo.companyName']) #被检查单位的id
        Param2['companyCheckRecord.checkDate'] = Time.getCurrentDate()
        Param2['checkResult'] = '一般'
        responseDict = YinHuanDuGaiIntf.saveFiretrapSupervise(Param2, username=userInit['DftSheQuUser'], password='11111111')

        searchParam = copy.deepcopy(YinHuanDuGaiPara.checkFireCompanyDict) 
        searchParam['companyName'] = Param02['fireCompanyInfo.companyName'] 
        searchParam['fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param02['fireCompanyInfo.companyName'])
        response = YinHuanDuGaiIntf.check_SubordinateList(searchParam,companyName=Param02['fireCompanyInfo.companyName'],orgId=orgInit['DftJieDaoOrgId'] , allStateSearch='0', publicString='1', query='jurisdiction', username=userInit['DftJieDaoUser'], password='11111111')
        for item in response['rows']:
            if item['fireCompanyInfo']['companyName']==Param02['fireCompanyInfo.companyName']:
                deleteParam = copy.deepcopy(YinHuanDuGaiPara.deleteSubordinateListDict) 
                deleteParam['ids'] = item['companyCheckRecordId']  
                responseDict = YinHuanDuGaiIntf.delete_SubordinateList(deleteParam,  username=userInit['DftJieDaoUser'], password='11111111')
         
                checkParam = copy.deepcopy(YinHuanDuGaiPara.checkFireCompanyDict) 
                checkParam['companyName'] = Param02['fireCompanyInfo.companyName'] 
                checkParam['fireCompanyInfoId'] = searchParam['fireCompanyInfoId'] 
                responseDict = YinHuanDuGaiIntf.check_SubordinateList(checkParam,companyName=Param02['fireCompanyInfo.companyName'],orgId=orgInit['DftJieDaoOrgId'] , allStateSearch='0', publicString='1', query='jurisdiction', username=userInit['DftJieDaoUser'], password='11111111')
                self.assertFalse(responseDict, '删除的在列表中依然存在，删除失败')      
                pass

    '''
    @功能：导出下辖检查记录 ——（以日常量化检查为例，接口一致publicString不同，日常1、上报3、举报4）？
    @ chenyan 2016-6-24
    '''
    def testSubordinateListDownLoad(self):
        """导出下辖检查记录"""
        #新增单位
        Param = copy.deepcopy(YinHuanDuGaiPara.fireCompanyDict) 
        Param['mode'] = 'add'  
        Param['fireCompanyInfo.createDept'] = orgInit['DftSheQuOrgId'] 
        Param['fireCompanyInfo.importOrAdd'] = '1'
        Param['fireCompanyInfo.orgPathName'] = '%s%s%s%s%s'%(orgInit['DftShiOrg'],orgInit['DftQuOrg'],orgInit['DftJieDaoOrg'],orgInit['DftSheQuOrg'],'请选择')
        Param['fireCompanyInfo.companyName'] = '测试单位%s'%CommonUtil.createRandomString()
        Param['fireCompanyInfo.orgid'] = Param['fireCompanyInfo.createDept']
        Param['companySuperviseTypeIsChange'] = 'true'
        Param['fireCompanyInfo.superviseTypeName'] = '其他一般单位'
        Param['fireCompanyInfo.superviseType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg']) 
        Param['fireCompanyInfo.address'] = '测试地址'
        Param['fireCompanyInfo.manger'] = '测试姓名'
        Param['fireCompanyInfo.managerTelephone'] = '18710000000'
        Param['fireCompanyInfo.rentHousePerson'] = '0'
        Param['fireCompanyInfo.industrialCatalogue'] = CommonIntf.getDbQueryResult(dbCommand = "select t.code from fire_company_type t where t.name='电器'")  #行业类别
        Param['businessLicense'] = '1'
        Param['firelicense'] = '1'
        responseDict = YinHuanDuGaiIntf.addOrEdit_fireCompany(Param, username=userInit['DftSheQuUser'], password='11111111')

        #添加日常检查1
        Param1 = copy.deepcopy(YinHuanDuGaiPara.saveFiretrapSuperviseDict) 
        Param1['isReportFlag'] = 0 
        Param1['calCheckResult'] = 'flage'
        Param1['firetrapSupervise.superviseNo'] = 'DG2016062800003'
        Param1['companyName'] = Param['fireCompanyInfo.companyName']
        Param1['checkDate'] = Time.getCurrentDate()
        Param1['firetrapSupervise.checkAddress'] = Param['fireCompanyInfo.address'] 
        Param1['firetrapSupervise.checkPlace'] = Param['fireCompanyInfo.companyName']
        Param1['checkItemIndexs'] = '1.'
        Param1['checkItemCodes'] = '%s#'% CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_item_id from supervise_type_item t where t.supervise_item_id =%s and t.supervise_type_id =%s"%(CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_item_id from supervise_item t where t.name ='安全出口疏散通道数量不足'"),CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg'] )))  #隐患项
        Param1['firetrapSupervise.reviseDate'] = Time.getCurrentDate()  #整改日期
        Param1['firetrapSupervise.manageName'] = Param['fireCompanyInfo.manger']
        Param1['companyCheckRecord_assignUserNameVo'] = userInit['DftJieDaoUserXM']
        Param1['companyCheckRecord_assignUserVo'] = userInit['DftJieDaoUser']
        Param1['companyCheckRecord_levelOrg'] = '村（社区）'
        Param1['companyCheckRecordlevel'] = '乡镇（街道）'
        Param1['companyCheckRecordOrgId'] = orgInit['DftJieDaoOrgId']
        Param1['user.userName'] = userInit['DftJieDaoUser']
        Param1['user.name'] = userInit['DftJieDaoUserXM']
        Param1['user.organization.id'] = orgInit['DftJieDaoOrgId']
        Param1['calculationMode'] = 0
        Param1['firetrapSupervise.signDate'] = Time.getCurrentDate()
        Param1['firetrapSupervise.superviseUserName'] = userInit['DftSheQuUserXM'] 
        Param1['firetrapSupervise.superviseUser'] = userInit['DftSheQuUser'] 
        Param1['firetrapSupervise.superviseDate'] = Time.getCurrentDate()
        Param1['operateMode'] = 'add'
        Param1['firetrapSupervise.superviseState'] = 1
        Param1['firetrapSupervise.updateDept'] = orgInit['DftSheQuOrgId']
        Param1['firetrapSupervise.createDept'] = orgInit['DftSheQuOrgId']
        Param1['firetrapSupervise.companyCheckRecordId'] =  CommonIntf.getDbQueryResult(dbCommand = "select t.company_check_record_id from firetrap_supervise t where t.check_place='%s'and t.update_user='%s'"%(Param['fireCompanyInfo.companyName'],userInit['DftWangGeUser1']))
        Param1['superviseTypeId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg'] )
        Param1['companyCheckRecord.companyManager'] = Param['fireCompanyInfo.manger']
        Param1['companyCheckRecord.assignUser'] = userInit['DftSheQuUser'] 
        Param1['companyCheckRecord.assignDept'] = orgInit['DftSheQuOrgId']
        Param1['companyCheckRecord.checkType'] = 1
        Param1['companyCheckRecord.companyCheckRecordId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.company_check_record_id from firetrap_supervise t where t.check_place='%s'and t.update_user='%s'"%(Param['fireCompanyInfo.companyName'],userInit['DftWangGeUser1']))
        Param1['companyCheckRecord.checkUser'] = userInit['DftWangGeUser1'] 
        Param1['companyCheckRecord.fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%Param['fireCompanyInfo.companyName']) #被检查单位的id
        Param1['companyCheckRecord.checkDate'] = Time.getCurrentDate()
        Param1['checkResult'] = '一般'
        responseDict = YinHuanDuGaiIntf.saveFiretrapSupervise(Param1, username=userInit['DftSheQuUser'], password='11111111')

        downLoadparam = copy.deepcopy(YinHuanDuGaiPara.dlJiLuData)
        downLoadparam['firetrapSupervise.orgIdForSearch']=orgInit['DftJieDaoOrgId']
        downLoadparam['queryParameter.allStateSearch']=0
        downLoadparam['queryParameter.orgId']=orgInit['DftJieDaoOrgId']
        downLoadparam['queryParameter.publicString']=1
        downLoadparam['firetrapSupervise.query']='jurisdiction'  #层级：本级-thelevelOf  直属下辖-jurisdiction
        response = YinHuanDuGaiIntf.downLoad_JiLu(downLoadparam, username='zdhjd1@', password='11111111')         
        with open("C:/autotest_file/downLoadJiLu.xls", "wb") as code:
            code.write(response.content)

        ret = CommonUtil.checkExcelCellValue(Param['fireCompanyInfo.companyName'], 'downLoadJiLu.xls','检查信息表', 'C4')   
        self.assertTrue(ret, '导出匹配失败')
        
        pass
            
    def tearDown(self):
        pass
if __name__ == "__main__":
    suite = unittest.TestSuite()

#     suite.addTest(YinHuanDuGai("testsaveSuperviseType"))
#     suite.addTest(YinHuanDuGai("testFireCompany"))
#     suite.addTest(YinHuanDuGai("testFireCompany_search"))
#     suite.addTest(YinHuanDuGai("testDanWeiImport")) #因天阙云的需求，导入时停在导入界面，关闭导入选择界面，信息有导入，该功能下次迭代修复
#     suite.addTest(YinHuanDuGai("testFireCompany_Change"))
#     suite.addTest(YinHuanDuGai("testSaveFiretrapSupervise")) 
#     suite.addTest(YinHuanDuGai("testSaveComplaintHandle")) 
#     suite.addTest(YinHuanDuGai("testComplaintHandle")) 
#     suite.addTest(YinHuanDuGai("testFiretrapSupervise")) 
#     suite.addTest(YinHuanDuGai("testSaveFiretrapReview")) 
#     suite.addTest(YinHuanDuGai("testFiretrapReview")) 
#     suite.addTest(YinHuanDuGai("testFiretrapReviewSearchDelete")) 
#     suite.addTest(YinHuanDuGai("testComplaintHandleReview")) 
#     suite.addTest(YinHuanDuGai("testSaveFirecheckTask")) 
#     suite.addTest(YinHuanDuGai("testSaveTaskItem")) 
#     suite.addTest(YinHuanDuGai("testAssignCheckRecord"))
#     suite.addTest(YinHuanDuGai("testSubordinateList"))
#     suite.addTest(YinHuanDuGai("testSubordinateListDownLoad")) 
 

    results = unittest.TextTestRunner().run(suite)
    pass

