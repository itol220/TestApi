# -*- coding:UTF-8 -*-
'''
Created on 2015-12-8

@author: chenyan
'''
from __future__ import unicode_literals
import unittest
import copy
from COMMON import Log,CommonUtil,Time
from CONFIG.Define import LogLevel
from CONFIG.InitDefaultPara import orgInit,userInit
from Interface.PingAnJianShe.SystemMgr import SystemMgrIntf
from Interface.PingAnJianShe.Common import CommonIntf
from Interface.PingAnJianShe.ShiYouFangWu import ShiYouFangWuIntf,\
    ShiYouFangWuPara
from Interface.PingAnJianShe.ShiYouRenKou import ShiYouRenKouIntf,\
    ShiYouRenKouPara
from Interface.PingAnJianShe.XiaQuGuanLi import XiaQuGuanLiIntf
from CONFIG import InitDefaultPara

 
class ShiYouFangWu(unittest.TestCase):

    def setUp(self):
        SystemMgrIntf.initEnv()
        ShiYouRenKouIntf.deleteAllPopulation()
        ShiYouFangWuIntf.deleteAllActualHouse()
        pass

    def testShiYouFangWuAdd_01(self):
        '''新增实有房屋'''

        houseParam_01 = copy.deepcopy(ShiYouFangWuPara.houseObject) 
        houseParam_01['dailogName']='actualHouseMaintanceDialog'
        houseParam_01['houseInfo.organization.id'] = orgInit['DftWangGeOrgId']
        houseParam_01['mode']='add'
        houseParam_01['isUseFrom'] = 'actualHouse'
        houseParam_01['houseInfo.organization.orgName'] = orgInit['DftWangGeOrg']
        houseParam_01['houseInfo.addressType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '现居住址类型') and p.displayname = '其他'")
        houseParam_01['currentAddressType'] = houseParam_01['houseInfo.addressType.id'] 
        houseParam_01['houseInfo.address'] = '新增房屋%s'%CommonUtil.createRandomString() 
        houseParam_01['houseInfo.isRentalHouse'] = 'false'      
        responseDict = ShiYouFangWuIntf.add_ShiYouFangWu(fangWuDict=houseParam_01, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增实有房屋失败')       
                      
        param_01 = copy.deepcopy(ShiYouFangWuPara.checkFangWuDict)
        param_01['address'] = houseParam_01['houseInfo.address']       
        param_01['id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from houseInfo t where t.address='%s'" % (houseParam_01['houseInfo.address']))
        ret = ShiYouFangWuIntf.check_ShiYouFangWu(param_01, orgId=houseParam_01['houseInfo.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找实有房屋失败') 
        
        pass 

    def testShiYouFangWuDelete_03(self):
        '''批量删除实有房屋'''

        houseParam_03 = copy.deepcopy(ShiYouFangWuPara.houseObject) 
        houseParam_03['dailogName']='actualHouseMaintanceDialog'
        houseParam_03['houseInfo.organization.id'] = orgInit['DftWangGeOrgId']
        houseParam_03['mode']='add'
        houseParam_03['isUseFrom'] = 'actualHouse'
        houseParam_03['houseInfo.organization.orgName'] = orgInit['DftWangGeOrg']
        houseParam_03['houseInfo.addressType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '现居住址类型') and p.displayname = '其他'")
        houseParam_03['currentAddressType'] = houseParam_03['houseInfo.addressType.id']   
        houseParam_03['houseInfo.address'] = '新增房屋%s'%CommonUtil.createRandomString() 
        houseParam_03['houseInfo.isRentalHouse'] = 'false'      
        responseDict = ShiYouFangWuIntf.add_ShiYouFangWu(fangWuDict=houseParam_03, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增实有房屋失败')  
        
        newHouseParam = copy.deepcopy(ShiYouFangWuPara.houseObject) 
        newHouseParam['dailogName']='actualHouseMaintanceDialog'
        newHouseParam['houseInfo.organization.id'] = orgInit['DftWangGeOrgId']
        newHouseParam['mode']='add'
        newHouseParam['isUseFrom'] = 'actualHouse'
        newHouseParam['houseInfo.organization.orgName'] = orgInit['DftWangGeOrg']
        newHouseParam['houseInfo.addressType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '现居住址类型') and p.displayname = '其他'")
        newHouseParam['currentAddressType'] = newHouseParam['houseInfo.addressType.id']   
        newHouseParam['houseInfo.address'] = '新增房屋1%s'%CommonUtil.createRandomString() 
        newHouseParam['houseInfo.isRentalHouse'] = 'false'      
        responseDict = ShiYouFangWuIntf.add_ShiYouFangWu(fangWuDict=newHouseParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增实有房屋失败') 
        
        deleteparam_03 = copy.deepcopy(ShiYouFangWuPara.deleteFangWuDict)
        deleteparam_03['houseIds'] = str(CommonIntf.getDbQueryResult(dbCommand = "select t.id from houseInfo t where t.address='%s'" % (houseParam_03['houseInfo.address'])))+','+str(CommonIntf.getDbQueryResult(dbCommand = "select t.id from houseInfo t where t.address='%s'" % (newHouseParam['houseInfo.address'])))
        ret = ShiYouFangWuIntf.delete_ShiYouFangWu(deleteparam_03,username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '删除实有房屋失败')             
                      
        param_03 = copy.deepcopy(ShiYouFangWuPara.checkFangWuDict)
        param_03['address'] = houseParam_03['houseInfo.address']       
        param_03['id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from houseInfo t where t.address='%s'" % (houseParam_03['houseInfo.address']))
        ret = ShiYouFangWuIntf.check_ShiYouFangWu(param_03, orgId=houseParam_03['houseInfo.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '列表中仍然存在删除的实有房屋信息，删除失败') 
        
        param_03['address'] = newHouseParam['houseInfo.address']       
        param_03['id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from houseInfo t where t.address='%s'" % (newHouseParam['houseInfo.address']))
        ret = ShiYouFangWuIntf.check_ShiYouFangWu(param_03, orgId=newHouseParam['houseInfo.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '列表中仍然存在删除的实有房屋信息，删除失败')
        
        pass 

    def testShiYouFangWuEdit_04(self):
        '''修改实有房屋'''

        houseParam_04 = copy.deepcopy(ShiYouFangWuPara.houseObject) 
        houseParam_04['dailogName']='actualHouseMaintanceDialog'
        houseParam_04['houseInfo.organization.id'] = orgInit['DftWangGeOrgId']
        houseParam_04['mode']='add'
        houseParam_04['isUseFrom'] = 'actualHouse'
        houseParam_04['houseInfo.organization.orgName'] = orgInit['DftWangGeOrg']
        houseParam_04['houseInfo.addressType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '现居住址类型') and p.displayname = '其他'")
        houseParam_04['currentAddressType'] = houseParam_04['houseInfo.addressType.id']    
        houseParam_04['houseInfo.address'] = '新增房屋%s'%CommonUtil.createRandomString() 
        houseParam_04['houseInfo.isRentalHouse'] = 'false'      
        responseDict = ShiYouFangWuIntf.add_ShiYouFangWu(fangWuDict=houseParam_04, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增实有房屋失败')  
        
        editParam_04 = copy.deepcopy(ShiYouFangWuPara.houseObject) 
        editParam_04['dailogName']=houseParam_04['dailogName']
        editParam_04['houseInfo.organization.id'] = houseParam_04['houseInfo.organization.id'] 
        editParam_04['mode']='edit'
        editParam_04['houseInfo.id']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from houseInfo t where t.address='%s'" % (houseParam_04['houseInfo.address']))
        editParam_04['isUseFrom'] = 'actualHouse'
        editParam_04['houseInfo.organization.orgName'] = orgInit['DftWangGeOrg']
        editParam_04['houseInfo.addressType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '现居住址类型') and p.displayname = '其他'")
        editParam_04['currentAddressType'] = editParam_04['houseInfo.addressType.id']   
        editParam_04['houseInfo.address'] = '修改为出租房%s'%CommonUtil.createRandomString() 
        editParam_04['houseInfo.isRentalHouse'] = 'true'    
        editParam_04['houseInfo.rentalPerson'] = '房东信息'  
        editParam_04['houseInfo.rentalType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='出租房类别', displayName='套房') 
        editParam_04['houseInfo.hiddenDangerLevel.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='隐患程度', displayName='安全') 
        responseDict = ShiYouFangWuIntf.edit_ShiYouFangWu(editDict=editParam_04, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改实有房屋失败')              
                      
        param_04 = copy.deepcopy(ShiYouFangWuPara.checkFangWuDict)
        param_04['address'] = editParam_04['houseInfo.address']       
        param_04['id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rentalHouse t where t.address='%s'" % (houseParam_04['houseInfo.address']))
        ret = ShiYouFangWuIntf.check_ChuZuFang(param_04, orgId=editParam_04['houseInfo.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找房屋失败') 
        
        pass 
    
    def testShiYouFangWuSearch_05(self):
        '''搜索实有房屋'''

        houseParam_05 = copy.deepcopy(ShiYouFangWuPara.houseObject) 
        houseParam_05['dailogName']='actualHouseMaintanceDialog'
        houseParam_05['houseInfo.organization.id'] = orgInit['DftWangGeOrgId']
        houseParam_05['mode']='add'
        houseParam_05['isUseFrom'] = 'actualHouse'
        houseParam_05['houseInfo.organization.orgName'] = orgInit['DftWangGeOrg']
        houseParam_05['houseInfo.addressType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '现居住址类型') and p.displayname = '其他'")
        houseParam_05['currentAddressType'] = houseParam_05['houseInfo.addressType.id']    
        houseParam_05['houseInfo.address'] = '新增房屋%s'%CommonUtil.createRandomString() 
        houseParam_05['houseInfo.isRentalHouse'] = 'false'      
        responseDict = ShiYouFangWuIntf.add_ShiYouFangWu(fangWuDict=houseParam_05, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增实有房屋失败')     
        
        newHouseParam_1 = copy.deepcopy(ShiYouFangWuPara.houseObject) 
        newHouseParam_1['dailogName']='actualHouseMaintanceDialog'
        newHouseParam_1['houseInfo.organization.id'] = orgInit['DftWangGeOrgId']
        newHouseParam_1['mode']='add'
        newHouseParam_1['isUseFrom'] = 'actualHouse'
        newHouseParam_1['houseInfo.organization.orgName'] = orgInit['DftWangGeOrg']
        newHouseParam_1['houseInfo.addressType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '现居住址类型') and p.displayname = '其他'")
        newHouseParam_1['currentAddressType'] = newHouseParam_1['houseInfo.addressType.id']   
        newHouseParam_1['houseInfo.address'] = '新增房屋%s'%CommonUtil.createRandomString() 
        newHouseParam_1['houseInfo.isRentalHouse'] = 'false'      
        responseDict = ShiYouFangWuIntf.add_ShiYouFangWu(fangWuDict=newHouseParam_1, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增实有房屋失败')   
        
        newHouseParam_2 = copy.deepcopy(ShiYouFangWuPara.houseObject) 
        newHouseParam_2['dailogName']='actualHouseMaintanceDialog'
        newHouseParam_2['houseInfo.organization.id'] = orgInit['DftWangGeOrgId']
        newHouseParam_2['mode']='add'
        newHouseParam_2['isUseFrom'] = 'actualHouse'
        newHouseParam_2['houseInfo.organization.orgName'] = orgInit['DftWangGeOrg']
        newHouseParam_2['houseInfo.addressType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '现居住址类型') and p.displayname = '其他'")
        newHouseParam_2['currentAddressType'] = newHouseParam_2['houseInfo.addressType.id']   
        newHouseParam_2['houseInfo.address'] = '新增房屋%s'%CommonUtil.createRandomString() 
        newHouseParam_2['houseInfo.isRentalHouse'] = 'false'      
        responseDict = ShiYouFangWuIntf.add_ShiYouFangWu(fangWuDict=newHouseParam_2, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增实有房屋失败')          
                      
        param_05 = copy.deepcopy(ShiYouFangWuPara.checkFangWuDict)
        param_05['address'] = houseParam_05['houseInfo.address']       
        param_05['id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from houseInfo t where t.address='%s'" % (houseParam_05['houseInfo.address']))
        ret = ShiYouFangWuIntf.search_ShiYouFangWu(param_05, orgId=houseParam_05['houseInfo.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找实有房屋失败') 
        
        pass 

    def testShiYouFangWuImportAndDownLoad_06(self):
        """导入、导出户籍人口信息"""
         
        importFangWuparam_06 = copy.deepcopy(ShiYouFangWuPara.data)
        importFangWuparam_06['dataType']='actualHouseData'
        importFangWuparam_06['templates']='ACTUALHOUSE'
        files = {'upload': ('test.xls', open('C:/autotest_file/importShiYouFangWu.xls', 'rb'),'applicationnd.ms-excel')}
        ret = ShiYouFangWuIntf.import_ShiYouFangWu(importFangWuparam_06, files=files,username=userInit['DftWangGeUser'], password='11111111')         
         
        param_06 = copy.deepcopy(ShiYouFangWuPara.checkFangWuDict)
        param_06['address'] = '导入测试'      
        param_06['id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from houseInfo t where t.address='%s'" % (param_06['address']))
        ret = ShiYouFangWuIntf.search_ShiYouFangWu(param_06, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找实有房屋失败')
                                
        downLoadFangWuparam_06 = copy.deepcopy(ShiYouFangWuPara.dlData)
        downLoadFangWuparam_06['orgId']=orgInit['DftWangGeOrgId']
        response = ShiYouFangWuIntf.downLoad_ShiYouFangWu(downLoadFangWuparam_06, username=userInit['DftWangGeUser'], password='11111111')         
        with open("C:/autotest_file/downLoadShiYouFangWu.xls", "wb") as code:
            code.write(response.content)
             
        ret = CommonUtil.checkExcelCellValue(param_06['address'], 'downLoadShiYouFangWu.xls','实有房屋信息', 'c4')         
        self.assertTrue(ret, '导出失败')
                         
        pass

    def testZhuHuXinXiAdd_07(self):
        '''实有房屋添加住户信息'''

        houseParam_07 = copy.deepcopy(ShiYouFangWuPara.houseObject) 
        houseParam_07['dailogName']='actualHouseMaintanceDialog'
        houseParam_07['houseInfo.organization.id'] = orgInit['DftWangGeOrgId']
        houseParam_07['mode']='add'
        houseParam_07['isUseFrom'] = 'actualHouse'
        houseParam_07['houseInfo.organization.orgName'] = orgInit['DftWangGeOrg']
        houseParam_07['houseInfo.addressType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '现居住址类型') and p.displayname = '其他'")
        houseParam_07['currentAddressType'] = houseParam_07['houseInfo.addressType.id']  
        houseParam_07['houseInfo.address'] = '新增房屋11%s'%CommonUtil.createRandomString() 
        houseParam_07['houseInfo.isRentalHouse'] = 'false'      
        responseDict = ShiYouFangWuIntf.add_ShiYouFangWu(fangWuDict=houseParam_07, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增实有房屋失败')      
        
        HuJiParam = copy.deepcopy(ShiYouRenKouPara.populationObject) 
        HuJiParam['mode']='add'
        HuJiParam['population.organization.id'] = orgInit['DftWangGeOrgId']
        HuJiParam['population.organization.orgName'] = orgInit['DftWangGeOrg']
        HuJiParam['population.idCardNo'] = '111111111111110'
        HuJiParam['population.name'] = 'test1'
        HuJiParam['population.isHaveHouse1'] = 'null'         
        responseDict = ShiYouRenKouIntf.add_HuJiRenKou(HuJiRenKouDict=HuJiParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口失败')               
                      
        zhuHuparam_07 = copy.deepcopy(ShiYouFangWuPara.zhuHuDict)
        zhuHuparam_07['houseHasActualPopulation.houseId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from houseInfo t where t.address='%s'" % (houseParam_07['houseInfo.address']))    
        zhuHuparam_07['houseHasActualPopulation.populationId'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from householdstaffs t where t.name='%s' and t.idCardNo='%s'" % (HuJiParam['population.name'],HuJiParam['population.idCardNo']))  
        zhuHuparam_07['houseHasActualPopulation.populationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']
        ret = ShiYouFangWuIntf.add_ZhuHuXinXi(zhuHuparam_07, username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '添加住户信息失败') 
        
        param_07 = copy.deepcopy(ShiYouFangWuPara.checkFangWuDict)
        param_07['certificateNumber'] = HuJiParam['population.idCardNo']     
        param_07['personName'] = HuJiParam['population.name']
        ret = ShiYouFangWuIntf.check_ZhuHuXinXi(param_07, houseId=zhuHuparam_07['houseHasActualPopulation.houseId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找住户信息失败') 
        
        pass 

    def testZhuHuXinXiChange_07(self):
        '''实有房屋住户信息变更住址'''

        houseParam_07 = copy.deepcopy(ShiYouFangWuPara.houseObject) 
        houseParam_07['dailogName']='actualHouseMaintanceDialog'
        houseParam_07['houseInfo.organization.id'] = orgInit['DftWangGeOrgId']
        houseParam_07['mode']='add'
        houseParam_07['isUseFrom'] = 'actualHouse'
        houseParam_07['houseInfo.organization.orgName'] = orgInit['DftWangGeOrg']
        houseParam_07['houseInfo.addressType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '现居住址类型') and p.displayname = '其他'")
        houseParam_07['currentAddressType'] = houseParam_07['houseInfo.addressType.id']   
        houseParam_07['houseInfo.address'] = '新增房屋11%s'%CommonUtil.createRandomString() 
        houseParam_07['houseInfo.isRentalHouse'] = 'false'      
        responseDict = ShiYouFangWuIntf.add_ShiYouFangWu(fangWuDict=houseParam_07, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增实有房屋失败')    
        
        newHouseParam_07 = copy.deepcopy(ShiYouFangWuPara.houseObject) 
        newHouseParam_07['dailogName']='actualHouseMaintanceDialog'
        newHouseParam_07['houseInfo.organization.id'] = orgInit['DftWangGeOrgId']
        newHouseParam_07['mode']='add'
        newHouseParam_07['isUseFrom'] = 'actualHouse'
        newHouseParam_07['houseInfo.organization.orgName'] = orgInit['DftWangGeOrg']
        newHouseParam_07['houseInfo.addressType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '现居住址类型') and p.displayname = '其他'")
        newHouseParam_07['currentAddressType'] = newHouseParam_07['houseInfo.addressType.id']   
        newHouseParam_07['houseInfo.address'] = '新增房屋2%s'%CommonUtil.createRandomString() 
        newHouseParam_07['houseInfo.isRentalHouse'] = 'false'      
        responseDict = ShiYouFangWuIntf.add_ShiYouFangWu(fangWuDict=newHouseParam_07, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增实有房屋失败')   
        
        HuJiParam = copy.deepcopy(ShiYouRenKouPara.populationObject) 
        HuJiParam['mode']='add'
        HuJiParam['population.organization.id'] = orgInit['DftWangGeOrgId']
        HuJiParam['population.organization.orgName'] = orgInit['DftWangGeOrg']
        HuJiParam['population.idCardNo'] = '111111111111112'
        HuJiParam['population.name'] = 'test2'
        HuJiParam['population.isHaveHouse1'] = 'null'         
        responseDict = ShiYouRenKouIntf.add_HuJiRenKou(HuJiRenKouDict=HuJiParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口失败')               
                      
        zhuHuparam_07 = copy.deepcopy(ShiYouFangWuPara.zhuHuDict)
        zhuHuparam_07['houseHasActualPopulation.houseId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from houseInfo t where t.address='%s'" % (houseParam_07['houseInfo.address']))    
        zhuHuparam_07['houseHasActualPopulation.populationId'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from householdstaffs t where t.name='%s' and t.idCardNo='%s'" % (HuJiParam['population.name'],HuJiParam['population.idCardNo']))  
        zhuHuparam_07['houseHasActualPopulation.populationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']
        ret = ShiYouFangWuIntf.add_ZhuHuXinXi(zhuHuparam_07, username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '添加住户信息失败') 
        
        changeZhuHuparam_07 = copy.deepcopy(ShiYouFangWuPara.zhuHuDict)
        changeZhuHuparam_07['houseHasActualPopulation.houseId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from houseInfo t where t.address='%s'" % (newHouseParam_07['houseInfo.address']))    
        changeZhuHuparam_07['houseHasActualPopulation.populationId'] = zhuHuparam_07['houseHasActualPopulation.populationId'] 
        changeZhuHuparam_07['houseHasActualPopulation.populationType'] = zhuHuparam_07['houseHasActualPopulation.populationType']
        ret = ShiYouFangWuIntf.add_ZhuHuXinXi(changeZhuHuparam_07, username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '住户信息变更住址失败')        
        
        param_07 = copy.deepcopy(ShiYouFangWuPara.checkFangWuDict)
        param_07['certificateNumber'] = HuJiParam['population.idCardNo']     
        param_07['personName'] = HuJiParam['population.name']
        ret = ShiYouFangWuIntf.check_ZhuHuXinXi(param_07, houseId=changeZhuHuparam_07['houseHasActualPopulation.houseId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找住户信息失败') 
        
        pass 

    def testZhuHuXinXiDelete_07(self):
        '''实有房屋移除住户信息'''

        houseParam_07 = copy.deepcopy(ShiYouFangWuPara.houseObject) 
        houseParam_07['dailogName']='actualHouseMaintanceDialog'
        houseParam_07['houseInfo.organization.id'] = orgInit['DftWangGeOrgId']
        houseParam_07['mode']='add'
        houseParam_07['isUseFrom'] = 'actualHouse'
        houseParam_07['houseInfo.organization.orgName'] = orgInit['DftWangGeOrg']
        houseParam_07['houseInfo.addressType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '现居住址类型') and p.displayname = '其他'")
        houseParam_07['currentAddressType'] = houseParam_07['houseInfo.addressType.id']   
        houseParam_07['houseInfo.address'] = '新增房屋3%s'%CommonUtil.createRandomString() 
        houseParam_07['houseInfo.isRentalHouse'] = 'false'      
        responseDict = ShiYouFangWuIntf.add_ShiYouFangWu(fangWuDict=houseParam_07, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增实有房屋失败')      
        
        HuJiParam = copy.deepcopy(ShiYouRenKouPara.populationObject) 
        HuJiParam['mode']='add'
        HuJiParam['population.organization.id'] = orgInit['DftWangGeOrgId']
        HuJiParam['population.organization.orgName'] = orgInit['DftWangGeOrg']
        HuJiParam['population.idCardNo'] = '111111111111113'
        HuJiParam['population.name'] = 'test3'
        HuJiParam['population.isHaveHouse1'] = 'null'         
        responseDict = ShiYouRenKouIntf.add_HuJiRenKou(HuJiRenKouDict=HuJiParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口失败')               
                      
        zhuHuparam_07 = copy.deepcopy(ShiYouFangWuPara.zhuHuDict)
        zhuHuparam_07['houseHasActualPopulation.houseId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from houseInfo t where t.address='%s'" % (houseParam_07['houseInfo.address']))    
        zhuHuparam_07['houseHasActualPopulation.populationId'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from householdstaffs t where t.name='%s' and t.idCardNo='%s'" % (HuJiParam['population.name'],HuJiParam['population.idCardNo']))  
        zhuHuparam_07['houseHasActualPopulation.populationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']
        ret = ShiYouFangWuIntf.add_ZhuHuXinXi(zhuHuparam_07, username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '添加住户信息失败') 
        
        param_07 = copy.deepcopy(ShiYouFangWuPara.checkFangWuDict)
        param_07['certificateNumber'] = HuJiParam['population.idCardNo']     
        param_07['personName'] = HuJiParam['population.name']
        ret = ShiYouFangWuIntf.check_ZhuHuXinXi(param_07, houseId=zhuHuparam_07['houseHasActualPopulation.houseId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找住户信息失败') 
        
        deleteZhuHuparam_07 = copy.deepcopy(ShiYouFangWuPara.zhuHuDict)
        deleteZhuHuparam_07['houseHasActualPopulation.houseId'] = zhuHuparam_07['houseHasActualPopulation.houseId']
        deleteZhuHuparam_07['houseHasActualPopulation.populationId'] = zhuHuparam_07['houseHasActualPopulation.populationId'] 
        deleteZhuHuparam_07['houseHasActualPopulation.populationType'] = zhuHuparam_07['houseHasActualPopulation.populationType']
        ret = ShiYouFangWuIntf.delete_ZhuHuXinXi(deleteZhuHuparam_07, username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '删除住户信息失败')        
        
        ret = ShiYouFangWuIntf.check_ZhuHuXinXi(param_07, houseId=zhuHuparam_07['houseHasActualPopulation.houseId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '删除的住户信息在列表中依然存在') 
        
        pass 

    def testShiYouFangWuTransfer_08(self):
        '''将测试自动化网格下的实有房屋转移到测试自动化网格1下'''

        houseParam_08 = copy.deepcopy(ShiYouFangWuPara.houseObject) 
        houseParam_08['dailogName']='actualHouseMaintanceDialog'
        houseParam_08['houseInfo.organization.id'] = orgInit['DftWangGeOrgId']
        houseParam_08['mode']='add'
        houseParam_08['isUseFrom'] = 'actualHouse'
        houseParam_08['houseInfo.organization.orgName'] = orgInit['DftWangGeOrg']
        houseParam_08['houseInfo.addressType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '现居住址类型') and p.displayname = '其他'")
        houseParam_08['currentAddressType'] = houseParam_08['houseInfo.addressType.id']   
        houseParam_08['houseInfo.address'] = '新增房屋%s'%CommonUtil.createRandomString() 
        houseParam_08['houseInfo.isRentalHouse'] = 'false'      
        responseDict = ShiYouFangWuIntf.add_ShiYouFangWu(fangWuDict=houseParam_08, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增实有房屋失败')  
        
        transferParam_08 = copy.deepcopy(ShiYouFangWuPara.transferFangWuDict) 
        transferParam_08['orgId'] = orgInit['DftWangGeOrgId']
        transferParam_08['toOrgId'] = orgInit['DftWangGeOrgId1']
        transferParam_08['ids'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from houseInfo t where t.address='%s'" % (houseParam_08['houseInfo.address']))
        transferParam_08['type'] ='actualHouse'
        transferParam_08['isTransfer'] = 'true'
        responseDict = ShiYouFangWuIntf.transfer_ShiYouFangWu(transferDict=transferParam_08, username=userInit['DftWangGeUser'], password='11111111')
#         self.assertTrue(responseDict.result, '转移实有房屋失败')              
                      
        param_08 = copy.deepcopy(ShiYouFangWuPara.checkFangWuDict)
        param_08['address'] = houseParam_08['houseInfo.address']       
        param_08['id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from houseInfo t where t.address='%s'" % (houseParam_08['houseInfo.address']))
        ret = ShiYouFangWuIntf.check_ShiYouFangWu(param_08, orgId=transferParam_08['orgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '查找房屋失败') 
        
        #检查测试自动化网格1中查看转移的房屋信息是否存在
        ret = ShiYouFangWuIntf.check_ShiYouFangWu(param_08, orgId=transferParam_08['toOrgId'],username=userInit['DftWangGeUser1'], password='11111111')         
        Log.LogOutput(LogLevel.INFO, " 测试自动化网格1中存在该转移的房屋信息，转移成功")
        self.assertTrue(ret, '查找房屋失败')         
        
        pass 

    def testChuZuFangAdd_02(self):
        '''新增出租房'''    

        houseParam_02 = copy.deepcopy(ShiYouFangWuPara.houseObject) 
        houseParam_02['dailogName']='rentalHouseMaintanceDialog'
        houseParam_02['houseInfo.organization.id'] = orgInit['DftWangGeOrgId']
        houseParam_02['mode']='add'
        houseParam_02['isUseFrom'] = 'actualHouse'
        houseParam_02['houseInfo.organization.orgName'] = orgInit['DftWangGeOrg']
        houseParam_02['houseInfo.addressType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '现居住址类型') and p.displayname = '其他'")
        houseParam_02['currentAddressType'] = houseParam_02['houseInfo.addressType.id']   
        houseParam_02['houseInfo.address'] = '出租房%s'%CommonUtil.createRandomString() 
        houseParam_02['houseInfo.isRentalHouse'] = 'true'      
        responseDict = ShiYouFangWuIntf.add_ShiYouFangWu(fangWuDict=houseParam_02, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增实有房失败')       
                   
        rentalParam_02 = copy.deepcopy(ShiYouFangWuPara.rentalObject) 
        rentalParam_02['houseInfo.organization.id'] = houseParam_02['houseInfo.organization.id']
        rentalParam_02['houseInfo.houseId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rentalHouse t where t.address='%s'" % (houseParam_02['houseInfo.address']))
        rentalParam_02['houseInfo.orgInternalCode'] = CommonIntf.getDbQueryResult(dbCommand = "select t.orginternalcode from ORGANIZATIONS t where t.orgname='%s'" % (rentalParam_02['houseInfo.organization.id']))
        rentalParam_02['dailogName']='rentalHouseMaintanceDialog'
        rentalParam_02['mode']='add'
        rentalParam_02['houseInfo.id'] = str(CommonIntf.getDbQueryResult(dbCommand = "select max(t.id) from RENTALHOUSE t"))
        rentalParam_02['houseInfo.isEmphasis'] = '0'
        rentalParam_02['houseInfo.rentalPerson'] = '房东'
        rentalParam_02['houseInfo.rentalType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '套房'")   
        rentalParam_02['houseInfo.hiddenDangerLevel.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='隐患程度', displayName='安全')
        responseDict = ShiYouFangWuIntf.add_ChuZuFang(chuZuDict=rentalParam_02, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增出租房失败')  
                      
        param_02 = copy.deepcopy(ShiYouFangWuPara.checkFangWuDict)
        param_02['address'] = houseParam_02['houseInfo.address']       
        param_02['id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rentalHouse t where t.address='%s'" % (houseParam_02['houseInfo.address']))
        ret = ShiYouFangWuIntf.check_ChuZuFang(param_02, orgId=houseParam_02['houseInfo.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找出租房失败') 
        
        pass 

    def testChuZuFangLogOut_02(self):
        '''注销/取消注销出租房信息'''    

        houseParam_02 = copy.deepcopy(ShiYouFangWuPara.houseObject) 
        houseParam_02['dailogName']='rentalHouseMaintanceDialog'
        houseParam_02['houseInfo.organization.id'] = orgInit['DftWangGeOrgId']
        houseParam_02['mode']='add'
        houseParam_02['isUseFrom'] = 'actualHouse'
        houseParam_02['houseInfo.organization.orgName'] = orgInit['DftWangGeOrg']
        houseParam_02['houseInfo.addressType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '现居住址类型') and p.displayname = '其他'")
        houseParam_02['currentAddressType'] = houseParam_02['houseInfo.addressType.id']  
        houseParam_02['houseInfo.address'] = '出租房%s'%CommonUtil.createRandomString() 
        houseParam_02['houseInfo.isRentalHouse'] = 'true'      
        responseDict = ShiYouFangWuIntf.add_ShiYouFangWu(fangWuDict=houseParam_02, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增实有房失败')       
                   
        rentalParam_02 = copy.deepcopy(ShiYouFangWuPara.rentalObject) 
        rentalParam_02['houseInfo.organization.id'] = houseParam_02['houseInfo.organization.id']
        rentalParam_02['houseInfo.houseId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rentalHouse t where t.address='%s'" % (houseParam_02['houseInfo.address']))
        rentalParam_02['houseInfo.orgInternalCode'] = CommonIntf.getDbQueryResult(dbCommand = "select t.orginternalcode from ORGANIZATIONS t where t.orgname='%s'" % (rentalParam_02['houseInfo.organization.id']))
        rentalParam_02['dailogName']='rentalHouseMaintanceDialog'
        rentalParam_02['mode']='add'
        rentalParam_02['houseInfo.id'] = str(CommonIntf.getDbQueryResult(dbCommand = "select max(t.id) from RENTALHOUSE t"))
        rentalParam_02['houseInfo.isEmphasis'] = '0'
        rentalParam_02['houseInfo.rentalPerson'] = '房东'
        rentalParam_02['houseInfo.rentalType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '套房'")   
        rentalParam_02['houseInfo.hiddenDangerLevel.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='隐患程度', displayName='安全')
        responseDict = ShiYouFangWuIntf.add_ChuZuFang(chuZuDict=rentalParam_02, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增出租房失败')  
                      
        param_02 = copy.deepcopy(ShiYouFangWuPara.checkFangWuDict)
        param_02['address'] = houseParam_02['houseInfo.address']       
        param_02['id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rentalHouse t where t.address='%s'" % (houseParam_02['houseInfo.address']))
        ret = ShiYouFangWuIntf.check_ChuZuFang(param_02, orgId=houseParam_02['houseInfo.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找出租房失败') 
        
        logOut_02 = copy.deepcopy(ShiYouFangWuPara.FangWuDict)
        logOut_02['houseIds'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rentalHouse t where t.address='%s'" % (houseParam_02['houseInfo.address']))       
        logOut_02['houseInfo.isEmphasis'] = '1'  #是否注销通过该字段来判定
        logOut_02['houseInfo.logOutTime'] = Time.getCurrentDate()
        logOut_02['houseInfo.logOutReason'] = '注销原因'
        ret = ShiYouFangWuIntf.logOut_ChuZuFang(logOut_02, username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '注销出租房失败')        
        
        logOutCancel_02 = copy.deepcopy(ShiYouFangWuPara.FangWuDict)
        logOutCancel_02['houseIds'] = logOut_02['houseIds']     
        logOutCancel_02['houseInfo.isEmphasis'] = '0'  #是否注销通过该字段来判定
        ret = ShiYouFangWuIntf.logOutCancel_ChuZuFang(logOutCancel_02, username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '取消注销出租房失败') 
        
        ret = ShiYouFangWuIntf.check_ChuZuFang(param_02, orgId=houseParam_02['houseInfo.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找出租房失败')         
        
        pass

    def testChuZuFangDelete_03(self):
        '''批量删除出租房信息'''    

        houseParam_03 = copy.deepcopy(ShiYouFangWuPara.houseObject) 
        houseParam_03['dailogName']='rentalHouseMaintanceDialog'
        houseParam_03['houseInfo.organization.id'] = orgInit['DftWangGeOrgId']
        houseParam_03['mode']='add'
        houseParam_03['isUseFrom'] = 'actualHouse'
        houseParam_03['houseInfo.organization.orgName'] = orgInit['DftWangGeOrg']
        houseParam_03['houseInfo.addressType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '现居住址类型') and p.displayname = '其他'")
        houseParam_03['currentAddressType'] = houseParam_03['houseInfo.addressType.id']    
        houseParam_03['houseInfo.address'] = '出租房%s'%CommonUtil.createRandomString() 
        houseParam_03['houseInfo.isRentalHouse'] = 'true'      
        responseDict = ShiYouFangWuIntf.add_ShiYouFangWu(fangWuDict=houseParam_03, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增实有房失败')       
                    
        rentalParam_03 = copy.deepcopy(ShiYouFangWuPara.rentalObject) 
        rentalParam_03['houseInfo.organization.id'] = houseParam_03['houseInfo.organization.id']
        rentalParam_03['houseInfo.houseId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rentalHouse t where t.address='%s'" % (houseParam_03['houseInfo.address']))
        rentalParam_03['houseInfo.orgInternalCode'] = CommonIntf.getDbQueryResult(dbCommand = "select t.orginternalcode from ORGANIZATIONS t where t.orgname='%s'" % (rentalParam_03['houseInfo.organization.id']))
        rentalParam_03['dailogName']='rentalHouseMaintanceDialog'
        rentalParam_03['mode']='add'
        rentalParam_03['houseInfo.id'] = str(CommonIntf.getDbQueryResult(dbCommand = "select max(t.id) from RENTALHOUSE t"))
        rentalParam_03['houseInfo.isEmphasis'] = '0'
        rentalParam_03['houseInfo.rentalPerson'] = '房东'
        rentalParam_03['houseInfo.rentalType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '套房'")   
        rentalParam_03['houseInfo.hiddenDangerLevel.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='隐患程度', displayName='安全')
        responseDict = ShiYouFangWuIntf.add_ChuZuFang(chuZuDict=rentalParam_03, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增出租房失败')  
        
        newHouseParam_03 = copy.deepcopy(ShiYouFangWuPara.houseObject) 
        newHouseParam_03['dailogName']='rentalHouseMaintanceDialog'
        newHouseParam_03['houseInfo.organization.id'] = orgInit['DftWangGeOrgId']
        newHouseParam_03['mode']='add'
        newHouseParam_03['isUseFrom'] = 'actualHouse'
        newHouseParam_03['houseInfo.organization.orgName'] = orgInit['DftWangGeOrg']
        newHouseParam_03['houseInfo.addressType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '现居住址类型') and p.displayname = '其他'")
        newHouseParam_03['currentAddressType'] = newHouseParam_03['houseInfo.addressType.id']   
        newHouseParam_03['houseInfo.address'] = '出租房%s'%CommonUtil.createRandomString() 
        newHouseParam_03['houseInfo.isRentalHouse'] = 'true'
        print newHouseParam_03 
        responseDict = ShiYouFangWuIntf.add_ShiYouFangWu(fangWuDict=newHouseParam_03, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增实有房失败')       
                   
        newRentalParam_03 = copy.deepcopy(ShiYouFangWuPara.rentalObject) 
        newRentalParam_03['houseInfo.organization.id'] = newHouseParam_03['houseInfo.organization.id']
        newRentalParam_03['houseInfo.houseId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rentalHouse t where t.address='%s'" % (newHouseParam_03['houseInfo.address']))
        newRentalParam_03['houseInfo.orgInternalCode'] = CommonIntf.getDbQueryResult(dbCommand = "select t.orginternalcode from ORGANIZATIONS t where t.orgname='%s'" % (newRentalParam_03['houseInfo.organization.id']))
        newRentalParam_03['dailogName']='rentalHouseMaintanceDialog'
        newRentalParam_03['mode']='add'
        newRentalParam_03['houseInfo.id'] = str(CommonIntf.getDbQueryResult(dbCommand = "select max(t.id) from RENTALHOUSE t"))
        newRentalParam_03['houseInfo.isEmphasis'] = '0'
        newRentalParam_03['houseInfo.rentalPerson'] = '房东'
        newRentalParam_03['houseInfo.rentalType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '套房'")   
        newRentalParam_03['houseInfo.hiddenDangerLevel.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='隐患程度', displayName='安全')
        responseDict = ShiYouFangWuIntf.add_ChuZuFang(chuZuDict=newRentalParam_03, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增出租房失败')
        
        deleteParam_03 = copy.deepcopy(ShiYouFangWuPara.deleteFangWuDict)
        deleteParam_03['houseIds'] = str(CommonIntf.getDbQueryResult(dbCommand = "select t.id from RENTALHOUSE t where t.address='%s'" % (houseParam_03['houseInfo.address'])))+','+str(CommonIntf.getDbQueryResult(dbCommand = "select t.id from RENTALHOUSE t where t.address='%s'" % (newHouseParam_03['houseInfo.address'])))
        ret = ShiYouFangWuIntf.delete_ChuZuFang(deleteParam_03,username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '删除出租房失败')    
        
        param_03 = copy.deepcopy(ShiYouFangWuPara.checkFangWuDict)
        param_03['address'] = houseParam_03['houseInfo.address']       
        param_03['id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rentalHouse t where t.address='%s'" % (houseParam_03['houseInfo.address']))
        ret = ShiYouFangWuIntf.check_ChuZuFang(param_03, orgId=newHouseParam_03['houseInfo.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '列表中仍然存在删除的出租房信息，删除失败')       
                      
        param_03 = copy.deepcopy(ShiYouFangWuPara.checkFangWuDict)
        param_03['address'] = newHouseParam_03['houseInfo.address']       
        param_03['id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rentalHouse t where t.address='%s'" % (newHouseParam_03['houseInfo.address']))
        ret = ShiYouFangWuIntf.check_ChuZuFang(param_03, orgId=newHouseParam_03['houseInfo.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '列表中仍然存在删除的出租房信息，删除失败')  
        
        pass
    
    def testChuZuFangZhuHuXinXiAdd_07(self):
        '''出租房添加住户信息'''

        houseParam_07 = copy.deepcopy(ShiYouFangWuPara.houseObject) 
        houseParam_07['dailogName']='rentalHouseMaintanceDialog'
        houseParam_07['houseInfo.organization.id'] = orgInit['DftWangGeOrgId']
        houseParam_07['mode']='add'
        houseParam_07['isUseFrom'] = 'actualHouse'
        houseParam_07['houseInfo.organization.orgName'] = orgInit['DftWangGeOrg']
        houseParam_07['houseInfo.addressType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '现居住址类型') and p.displayname = '其他'")
        houseParam_07['currentAddressType'] = houseParam_07['houseInfo.addressType.id']    
        houseParam_07['houseInfo.address'] = '出租房%s'%CommonUtil.createRandomString() 
        houseParam_07['houseInfo.isRentalHouse'] = 'true'      
        responseDict = ShiYouFangWuIntf.add_ShiYouFangWu(fangWuDict=houseParam_07, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增实有房失败')       
                   
        rentalParam_07 = copy.deepcopy(ShiYouFangWuPara.rentalObject) 
        rentalParam_07['houseInfo.organization.id'] = houseParam_07['houseInfo.organization.id']
        rentalParam_07['houseInfo.houseId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rentalHouse t where t.address='%s'" % (houseParam_07['houseInfo.address']))
        rentalParam_07['houseInfo.orgInternalCode'] = CommonIntf.getDbQueryResult(dbCommand = "select t.orginternalcode from ORGANIZATIONS t where t.orgname='%s'" % (rentalParam_07['houseInfo.organization.id']))
        rentalParam_07['dailogName']='rentalHouseMaintanceDialog'
        rentalParam_07['mode']='add'
        rentalParam_07['houseInfo.id'] = str(CommonIntf.getDbQueryResult(dbCommand = "select max(t.id) from RENTALHOUSE t"))
        rentalParam_07['houseInfo.isEmphasis'] = '0'
        rentalParam_07['houseInfo.rentalPerson'] = '房东'
        rentalParam_07['houseInfo.rentalType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '套房'")   
        rentalParam_07['houseInfo.hiddenDangerLevel.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='隐患程度', displayName='安全')
        responseDict = ShiYouFangWuIntf.add_ChuZuFang(chuZuDict=rentalParam_07, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增出租房失败')      
        
        HuJiParam = copy.deepcopy(ShiYouRenKouPara.populationObject) 
        HuJiParam['mode']='add'
        HuJiParam['population.organization.id'] = orgInit['DftWangGeOrgId']
        HuJiParam['population.organization.orgName'] = orgInit['DftWangGeOrg']
        HuJiParam['population.idCardNo'] = '111111111111121'
        HuJiParam['population.name'] = '住户'
        HuJiParam['population.isHaveHouse1'] = 'null'         
        responseDict = ShiYouRenKouIntf.add_HuJiRenKou(HuJiRenKouDict=HuJiParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口失败')               
                      
        zhuHuparam_07 = copy.deepcopy(ShiYouFangWuPara.zhuHuDict)
        zhuHuparam_07['houseHasActualPopulation.houseId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from houseInfo t where t.address='%s'" % (houseParam_07['houseInfo.address']))    
        zhuHuparam_07['houseHasActualPopulation.populationId'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from householdstaffs t where t.name='%s' and t.idCardNo='%s'" % (HuJiParam['population.name'],HuJiParam['population.idCardNo']))  
        zhuHuparam_07['houseHasActualPopulation.populationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']
        ret = ShiYouFangWuIntf.add_ZhuHuXinXi(zhuHuparam_07, username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '添加住户信息失败') 
        
        param_07 = copy.deepcopy(ShiYouFangWuPara.checkFangWuDict)
        param_07['certificateNumber'] = HuJiParam['population.idCardNo']     
        param_07['personName'] = HuJiParam['population.name']
        ret = ShiYouFangWuIntf.check_ZhuHuXinXi(param_07, houseId=zhuHuparam_07['houseHasActualPopulation.houseId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找住户信息失败') 
        
        pass 

    def testZhiAnFuZeRenAdd_09(self):
        '''出租房添加治安负责人信息'''
        XiaQuGuanLiIntf.xiaQuGuanLiMemberDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        houseParam_09 = copy.deepcopy(ShiYouFangWuPara.houseObject) 
        houseParam_09['dailogName']='rentalHouseMaintanceDialog'
        houseParam_09['houseInfo.organization.id'] = orgInit['DftWangGeOrgId']
        houseParam_09['mode']='add'
        houseParam_09['isUseFrom'] = 'actualHouse'
        houseParam_09['houseInfo.organization.orgName'] = orgInit['DftWangGeOrg']
        houseParam_09['houseInfo.addressType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '现居住址类型') and p.displayname = '其他'")
        houseParam_09['currentAddressType'] = houseParam_09['houseInfo.addressType.id']     
        houseParam_09['houseInfo.address'] = '出租房%s'%CommonUtil.createRandomString() 
        houseParam_09['houseInfo.isRentalHouse'] = 'true'      
        responseDict = ShiYouFangWuIntf.add_ShiYouFangWu(fangWuDict=houseParam_09, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增实有房失败')       
                   
        rentalParam_09 = copy.deepcopy(ShiYouFangWuPara.rentalObject) 
        rentalParam_09['houseInfo.organization.id'] = houseParam_09['houseInfo.organization.id']
        rentalParam_09['houseInfo.houseId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rentalHouse t where t.address='%s'" % (houseParam_09['houseInfo.address']))
        rentalParam_09['houseInfo.orgInternalCode'] = CommonIntf.getDbQueryResult(dbCommand = "select t.orginternalcode from ORGANIZATIONS t where t.orgname='%s'" % (rentalParam_09['houseInfo.organization.id']))
        rentalParam_09['dailogName']='rentalHouseMaintanceDialog'
        rentalParam_09['mode']='add'
        rentalParam_09['houseInfo.id'] = str(CommonIntf.getDbQueryResult(dbCommand = "select max(t.id) from RENTALHOUSE t"))
        rentalParam_09['houseInfo.isEmphasis'] = '0'
        rentalParam_09['houseInfo.rentalPerson'] = '房东'
        rentalParam_09['houseInfo.rentalType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '套房'")   
        rentalParam_09['houseInfo.hiddenDangerLevel.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='隐患程度', displayName='安全')
        responseDict = ShiYouFangWuIntf.add_ChuZuFang(chuZuDict=rentalParam_09, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增出租房失败')     
        
        fuWuParam = copy.deepcopy(ShiYouRenKouPara.fuWuRenYuanDict)      
        fuWuParam['serviceTeamMemberBase.org.id'] = orgInit['DftWangGeOrgId']
        fuWuParam['serviceTeamMemberBase.name'] = '服务%s'%CommonUtil.createRandomString()
        fuWuParam['serviceTeamMemberBase.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别(男、女)', displayName='男')     
        fuWuParam['serviceTeamMemberBase.mobile'] = '13011111111'
        responseDict = ShiYouRenKouIntf.add_FuWuChengYuan(fuWuDict=fuWuParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增成员失败')              
                      
        fuZeRenparam_09 = copy.deepcopy(ShiYouFangWuPara.addFuZeRenDict)
        fuZeRenparam_09['serviceMemberWithObject.memberId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from Serviceteammemberbase t where t.name='%s'" % (fuWuParam['serviceTeamMemberBase.name']))    
        fuZeRenparam_09['serviceMemberWithObject.objectType'] = 'RENTALHOUSE' 
        fuZeRenparam_09['serviceMemberWithObject.objectName'] = houseParam_09['houseInfo.address']
        fuZeRenparam_09['serviceMemberWithObject.objectId'] = rentalParam_09['houseInfo.id'] 
        fuZeRenparam_09['serviceMemberWithObject.teamMember'] = '1'
        fuZeRenparam_09['serviceMemberWithObject.onDuty'] = '1'
        fuZeRenparam_09['serviceMemberWithObject.objectLogout'] = '1'
        ret = ShiYouFangWuIntf.add_ZhiAnFuZeRen(fuZeRenDict=fuZeRenparam_09, username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '添加治安负责人信息失败') 
        
        param_09 = copy.deepcopy(ShiYouFangWuPara.checkFuZeRenDict)
        param_09['memberId'] = fuZeRenparam_09['serviceMemberWithObject.memberId']
        param_09['memberName'] = fuWuParam['serviceTeamMemberBase.name']
        ret = ShiYouFangWuIntf.check_ZhiAnFuZeRen(param_09, objectId=fuZeRenparam_09['serviceMemberWithObject.objectId'],objectName=houseParam_09['houseInfo.address'],onDuty='1',username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找治安负责人信息失败') 
        XiaQuGuanLiIntf.xiaQuGuanLiMemberDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        pass
    
    def testZhiAnFuZeRenDelete_10(self):
        '''出租房删除治安负责人信息'''
        XiaQuGuanLiIntf.xiaQuGuanLiMemberDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        houseParam_10 = copy.deepcopy(ShiYouFangWuPara.houseObject) 
        houseParam_10['dailogName']='rentalHouseMaintanceDialog'
        houseParam_10['houseInfo.organization.id'] = orgInit['DftWangGeOrgId']
        houseParam_10['mode']='add'
        houseParam_10['isUseFrom'] = 'actualHouse'
        houseParam_10['houseInfo.organization.orgName'] = orgInit['DftWangGeOrg']
        houseParam_10['houseInfo.addressType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '现居住址类型') and p.displayname = '其他'")
        houseParam_10['currentAddressType'] = houseParam_10['houseInfo.addressType.id']    
        houseParam_10['houseInfo.address'] = '出租房%s'%CommonUtil.createRandomString() 
        houseParam_10['houseInfo.isRentalHouse'] = 'true'      
        responseDict = ShiYouFangWuIntf.add_ShiYouFangWu(fangWuDict=houseParam_10, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增实有房失败')       
                   
        rentalParam_10 = copy.deepcopy(ShiYouFangWuPara.rentalObject) 
        rentalParam_10['houseInfo.organization.id'] = houseParam_10['houseInfo.organization.id']
        rentalParam_10['houseInfo.houseId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rentalHouse t where t.address='%s'" % (houseParam_10['houseInfo.address']))
        rentalParam_10['houseInfo.orgInternalCode'] = CommonIntf.getDbQueryResult(dbCommand = "select t.orginternalcode from ORGANIZATIONS t where t.orgname='%s'" % (rentalParam_10['houseInfo.organization.id']))
        rentalParam_10['dailogName']='rentalHouseMaintanceDialog'
        rentalParam_10['mode']='add'
        rentalParam_10['houseInfo.id'] = str(CommonIntf.getDbQueryResult(dbCommand = "select max(t.id) from RENTALHOUSE t"))
        rentalParam_10['houseInfo.isEmphasis'] = '0'
        rentalParam_10['houseInfo.rentalPerson'] = '房东'
        rentalParam_10['houseInfo.rentalType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '套房'")   
        rentalParam_10['houseInfo.hiddenDangerLevel.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='隐患程度', displayName='安全')
        responseDict = ShiYouFangWuIntf.add_ChuZuFang(chuZuDict=rentalParam_10, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增出租房失败')    
        
        fuWuParam = copy.deepcopy(ShiYouRenKouPara.fuWuRenYuanDict)      
        fuWuParam['serviceTeamMemberBase.org.id'] = orgInit['DftWangGeOrgId']
        fuWuParam['serviceTeamMemberBase.name'] = '服务%s'%CommonUtil.createRandomString()
        fuWuParam['serviceTeamMemberBase.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别(男、女)', displayName='男')     
        fuWuParam['serviceTeamMemberBase.mobile'] = '13011111111'
        responseDict = ShiYouRenKouIntf.add_FuWuChengYuan(fuWuDict=fuWuParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增成员失败')               
                      
        fuZeRenparam_10 = copy.deepcopy(ShiYouFangWuPara.addFuZeRenDict)
        fuZeRenparam_10['serviceMemberWithObject.memberId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from Serviceteammemberbase t where t.name='%s'" % (fuWuParam['serviceTeamMemberBase.name']))    
        fuZeRenparam_10['serviceMemberWithObject.objectType'] = 'RENTALHOUSE' 
        fuZeRenparam_10['serviceMemberWithObject.objectName'] = houseParam_10['houseInfo.address']
        fuZeRenparam_10['serviceMemberWithObject.objectId'] = rentalParam_10['houseInfo.id'] 
        fuZeRenparam_10['serviceMemberWithObject.teamMember'] = '1'
        fuZeRenparam_10['serviceMemberWithObject.onDuty'] = '1'
        fuZeRenparam_10['serviceMemberWithObject.objectLogout'] = '1'
        ret = ShiYouFangWuIntf.add_ZhiAnFuZeRen(fuZeRenDict=fuZeRenparam_10, username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '添加治安负责人信息失败') 
         
        deleteParam_10 = copy.deepcopy(ShiYouFangWuPara.deleteFuZeRenDict)
        deleteParam_10['selectedIds'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from serviceMemberHasObject t where t.memberid='%s'" % (fuZeRenparam_10['serviceMemberWithObject.memberId'])) 
        ret = ShiYouFangWuIntf.delete_ZhiAnFuZeRen(deleteParam_10,username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '删除治安负责人失败')     
  
        param_10 = copy.deepcopy(ShiYouFangWuPara.checkFuZeRenDict)
        param_10['memberId'] = fuZeRenparam_10['serviceMemberWithObject.memberId']
        param_10['memberName'] = fuWuParam['serviceTeamMemberBase.name']
        ret = ShiYouFangWuIntf.check_ZhiAnFuZeRen(param_10, objectId=fuZeRenparam_10['serviceMemberWithObject.objectId'],objectName=houseParam_10['houseInfo.address'],onDuty='1',username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '列表中仍然存在删除的治安负责人信息，删除失败')         
        XiaQuGuanLiIntf.xiaQuGuanLiMemberDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        pass
    
    def testZhiAnFuZeRenLeave_10(self):
        '''出租房中卸任治安负责人'''
        XiaQuGuanLiIntf.xiaQuGuanLiMemberDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        houseParam_10 = copy.deepcopy(ShiYouFangWuPara.houseObject) 
        houseParam_10['dailogName']='rentalHouseMaintanceDialog'
        houseParam_10['houseInfo.organization.id'] = orgInit['DftWangGeOrgId']
        houseParam_10['mode']='add'
        houseParam_10['isUseFrom'] = 'actualHouse'
        houseParam_10['houseInfo.organization.orgName'] = orgInit['DftWangGeOrg']
        houseParam_10['houseInfo.addressType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '现居住址类型') and p.displayname = '其他'")
        houseParam_10['currentAddressType'] = houseParam_10['houseInfo.addressType.id']   
        houseParam_10['houseInfo.address'] = '出租房%s'%CommonUtil.createRandomString() 
        houseParam_10['houseInfo.isRentalHouse'] = 'true'      
        responseDict = ShiYouFangWuIntf.add_ShiYouFangWu(fangWuDict=houseParam_10, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增实有房失败')       
                   
        rentalParam_10 = copy.deepcopy(ShiYouFangWuPara.rentalObject) 
        rentalParam_10['houseInfo.organization.id'] = houseParam_10['houseInfo.organization.id']
        rentalParam_10['houseInfo.houseId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rentalHouse t where t.address='%s'" % (houseParam_10['houseInfo.address']))
        rentalParam_10['houseInfo.orgInternalCode'] = CommonIntf.getDbQueryResult(dbCommand = "select t.orginternalcode from ORGANIZATIONS t where t.orgname='%s'" % (rentalParam_10['houseInfo.organization.id']))
        rentalParam_10['dailogName']='rentalHouseMaintanceDialog'
        rentalParam_10['mode']='add'
        rentalParam_10['houseInfo.id'] = str(CommonIntf.getDbQueryResult(dbCommand = "select max(t.id) from RENTALHOUSE t"))
        rentalParam_10['houseInfo.isEmphasis'] = '0'
        rentalParam_10['houseInfo.rentalPerson'] = '房东'
        rentalParam_10['houseInfo.rentalType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '套房'")   
        rentalParam_10['houseInfo.hiddenDangerLevel.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='隐患程度', displayName='安全')
        responseDict = ShiYouFangWuIntf.add_ChuZuFang(chuZuDict=rentalParam_10, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增出租房失败')      
        
        newFuWuParam = copy.deepcopy(ShiYouRenKouPara.fuWuRenYuanDict)      
        newFuWuParam['serviceTeamMemberBase.org.id'] = orgInit['DftWangGeOrgId']
        newFuWuParam['serviceTeamMemberBase.name'] = '服务%s'%CommonUtil.createRandomString()
        newFuWuParam['serviceTeamMemberBase.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别(男、女)', displayName='男')     
        newFuWuParam['serviceTeamMemberBase.mobile'] = '13011111111'
        responseDict = ShiYouRenKouIntf.add_FuWuChengYuan(fuWuDict=newFuWuParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增成员失败')              
        
        newFuZeRenparam_10 = copy.deepcopy(ShiYouFangWuPara.addFuZeRenDict)
        newFuZeRenparam_10['serviceMemberWithObject.memberId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from Serviceteammemberbase t where t.name='%s'" % (newFuWuParam['serviceTeamMemberBase.name']))    
        newFuZeRenparam_10['serviceMemberWithObject.objectType'] = 'RENTALHOUSE' 
        newFuZeRenparam_10['serviceMemberWithObject.objectName'] = houseParam_10['houseInfo.address']
        newFuZeRenparam_10['serviceMemberWithObject.objectId'] = rentalParam_10['houseInfo.id'] 
        newFuZeRenparam_10['serviceMemberWithObject.teamMember'] = '1'
        newFuZeRenparam_10['serviceMemberWithObject.onDuty'] = '1'
        newFuZeRenparam_10['serviceMemberWithObject.objectLogout'] = '1'
        ret = ShiYouFangWuIntf.add_ZhiAnFuZeRen(fuZeRenDict=newFuZeRenparam_10, username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '添加治安负责人信息失败')        
        
        leaveParam_10 = copy.deepcopy(ShiYouFangWuPara.leaveFuZeRenDict)
        leaveParam_10['serviceMemberWithObject.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from serviceMemberHasObject t where t.memberid='%s'" % (newFuZeRenparam_10['serviceMemberWithObject.memberId'])) 
        leaveParam_10['serviceMemberWithObject.onDuty'] = '0'
        leaveParam_10['serviceMemberWithObject.memberId'] = newFuZeRenparam_10['serviceMemberWithObject.memberId']
        ret = ShiYouFangWuIntf.leave_ZhiAnFuZeRen(leaveParam_10,username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '卸任治安负责人失败')             
        
        param_10 = copy.deepcopy(ShiYouFangWuPara.checkFuZeRenDict)
        param_10['memberId'] = newFuZeRenparam_10['serviceMemberWithObject.memberId']
        param_10['memberName'] = newFuWuParam['serviceTeamMemberBase.name']
        ret = ShiYouFangWuIntf.check_ZhiAnFuZeRen(param_10, objectId=newFuZeRenparam_10['serviceMemberWithObject.objectId'],objectName=houseParam_10['houseInfo.address'],onDuty='0',username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '列表中曾任筛选下不存在该负责人信息，卸任失败') 
        XiaQuGuanLiIntf.xiaQuGuanLiMemberDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        pass

    def testZhiAnFuZeRenBack_10(self):
        '''将出租房中移除治安负责人重新担任'''
        XiaQuGuanLiIntf.xiaQuGuanLiMemberDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        houseParam_10 = copy.deepcopy(ShiYouFangWuPara.houseObject) 
        houseParam_10['dailogName']='rentalHouseMaintanceDialog'
        houseParam_10['houseInfo.organization.id'] = orgInit['DftWangGeOrgId']
        houseParam_10['mode']='add'
        houseParam_10['isUseFrom'] = 'actualHouse'
        houseParam_10['houseInfo.organization.orgName'] = orgInit['DftWangGeOrg']
        houseParam_10['houseInfo.addressType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '现居住址类型') and p.displayname = '其他'")
        houseParam_10['currentAddressType'] = houseParam_10['houseInfo.addressType.id']   
        houseParam_10['houseInfo.address'] = '出租房%s'%CommonUtil.createRandomString() 
        houseParam_10['houseInfo.isRentalHouse'] = 'true'      
        responseDict = ShiYouFangWuIntf.add_ShiYouFangWu(fangWuDict=houseParam_10, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增实有房失败')       
                   
        rentalParam_10 = copy.deepcopy(ShiYouFangWuPara.rentalObject) 
        rentalParam_10['houseInfo.organization.id'] = houseParam_10['houseInfo.organization.id']
        rentalParam_10['houseInfo.houseId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rentalHouse t where t.address='%s'" % (houseParam_10['houseInfo.address']))
        rentalParam_10['houseInfo.orgInternalCode'] = CommonIntf.getDbQueryResult(dbCommand = "select t.orginternalcode from ORGANIZATIONS t where t.orgname='%s'" % (rentalParam_10['houseInfo.organization.id']))
        rentalParam_10['dailogName']='rentalHouseMaintanceDialog'
        rentalParam_10['mode']='add'
        rentalParam_10['houseInfo.id'] = str(CommonIntf.getDbQueryResult(dbCommand = "select max(t.id) from RENTALHOUSE t"))
        rentalParam_10['houseInfo.isEmphasis'] = '0'
        rentalParam_10['houseInfo.rentalPerson'] = '房东'
        rentalParam_10['houseInfo.rentalType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '套房'")   
        rentalParam_10['houseInfo.hiddenDangerLevel.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='隐患程度', displayName='安全')
        responseDict = ShiYouFangWuIntf.add_ChuZuFang(chuZuDict=rentalParam_10, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增出租房失败')      
        
        newFuWuParam = copy.deepcopy(ShiYouRenKouPara.fuWuRenYuanDict)      
        newFuWuParam['serviceTeamMemberBase.org.id'] = orgInit['DftWangGeOrgId']
        newFuWuParam['serviceTeamMemberBase.name'] = '服务%s'%CommonUtil.createRandomString()
        newFuWuParam['serviceTeamMemberBase.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别(男、女)', displayName='男')     
        newFuWuParam['serviceTeamMemberBase.mobile'] = '13011111111'
        responseDict = ShiYouRenKouIntf.add_FuWuChengYuan(fuWuDict=newFuWuParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增成员失败')              
        
        newFuZeRenparam_10 = copy.deepcopy(ShiYouFangWuPara.addFuZeRenDict)
        newFuZeRenparam_10['serviceMemberWithObject.memberId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from Serviceteammemberbase t where t.name='%s'" % (newFuWuParam['serviceTeamMemberBase.name']))    
        newFuZeRenparam_10['serviceMemberWithObject.objectType'] = 'RENTALHOUSE' 
        newFuZeRenparam_10['serviceMemberWithObject.objectName'] = houseParam_10['houseInfo.address']
        newFuZeRenparam_10['serviceMemberWithObject.objectId'] = rentalParam_10['houseInfo.id'] 
        newFuZeRenparam_10['serviceMemberWithObject.teamMember'] = '1'
        newFuZeRenparam_10['serviceMemberWithObject.onDuty'] = '1'
        newFuZeRenparam_10['serviceMemberWithObject.objectLogout'] = '1'
        ret = ShiYouFangWuIntf.add_ZhiAnFuZeRen(fuZeRenDict=newFuZeRenparam_10, username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '添加治安负责人信息失败')        
        
        leaveParam_10 = copy.deepcopy(ShiYouFangWuPara.leaveFuZeRenDict)
        leaveParam_10['serviceMemberWithObject.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from serviceMemberHasObject t where t.memberid='%s'" % (newFuZeRenparam_10['serviceMemberWithObject.memberId'])) 
        leaveParam_10['serviceMemberWithObject.onDuty'] = '0'
        leaveParam_10['serviceMemberWithObject.memberId'] = newFuZeRenparam_10['serviceMemberWithObject.memberId']
        ret = ShiYouFangWuIntf.leave_ZhiAnFuZeRen(leaveParam_10,username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '卸任治安负责人失败')             
        
        param_10 = copy.deepcopy(ShiYouFangWuPara.checkFuZeRenDict)
        param_10['memberId'] = newFuZeRenparam_10['serviceMemberWithObject.memberId']
        param_10['memberName'] = newFuWuParam['serviceTeamMemberBase.name']
        ret = ShiYouFangWuIntf.check_ZhiAnFuZeRen(param_10, objectId=newFuZeRenparam_10['serviceMemberWithObject.objectId'],objectName=houseParam_10['houseInfo.address'],onDuty='0',username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '列表中曾任筛选下不存在该负责人信息，卸任失败') 
        
        backParam_10 = copy.deepcopy(ShiYouFangWuPara.leaveFuZeRenDict)
        backParam_10['serviceMemberWithObject.id'] = leaveParam_10['serviceMemberWithObject.id']
        backParam_10['serviceMemberWithObject.onDuty'] = '1'
        backParam_10['serviceMemberWithObject.memberId'] = leaveParam_10['serviceMemberWithObject.memberId']
        ret = ShiYouFangWuIntf.leave_ZhiAnFuZeRen(backParam_10,username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '治安负责人重新担任失败')     
        
        ret = ShiYouFangWuIntf.check_ZhiAnFuZeRen(param_10, objectId=newFuZeRenparam_10['serviceMemberWithObject.objectId'],objectName=houseParam_10['houseInfo.address'],onDuty='1',username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '列表中不存在该负责人信息，重新担任失败')    
        XiaQuGuanLiIntf.xiaQuGuanLiMemberDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        pass

    def testXunChangQingKuangAdd_11(self):
        '''出租房添加巡场情况'''
        XiaQuGuanLiIntf.xiaQuGuanLiMemberDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        houseParam_11 = copy.deepcopy(ShiYouFangWuPara.houseObject) 
        houseParam_11['dailogName']='rentalHouseMaintanceDialog'
        houseParam_11['houseInfo.organization.id'] = orgInit['DftWangGeOrgId']
        houseParam_11['mode']='add'
        houseParam_11['isUseFrom'] = 'actualHouse'
        houseParam_11['houseInfo.organization.orgName'] = orgInit['DftWangGeOrg']
        houseParam_11['houseInfo.addressType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '现居住址类型') and p.displayname = '其他'")
        houseParam_11['currentAddressType'] = houseParam_11['houseInfo.addressType.id']   
        houseParam_11['houseInfo.address'] = '出租房%s'%CommonUtil.createRandomString() 
        houseParam_11['houseInfo.isRentalHouse'] = 'true'      
        responseDict = ShiYouFangWuIntf.add_ShiYouFangWu(fangWuDict=houseParam_11, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增实有房失败')       
                   
        rentalParam_11 = copy.deepcopy(ShiYouFangWuPara.rentalObject) 
        rentalParam_11['houseInfo.organization.id'] = houseParam_11['houseInfo.organization.id']
        rentalParam_11['houseInfo.houseId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rentalHouse t where t.address='%s'" % (houseParam_11['houseInfo.address']))
        rentalParam_11['houseInfo.orgInternalCode'] = CommonIntf.getDbQueryResult(dbCommand = "select t.orginternalcode from ORGANIZATIONS t where t.orgname='%s'" % (rentalParam_11['houseInfo.organization.id']))
        rentalParam_11['dailogName']='rentalHouseMaintanceDialog'
        rentalParam_11['mode']='add'
        rentalParam_11['houseInfo.id'] = str(CommonIntf.getDbQueryResult(dbCommand = "select max(t.id) from RENTALHOUSE t"))
        rentalParam_11['houseInfo.isEmphasis'] = '0'
        rentalParam_11['houseInfo.rentalPerson'] = '房东'
        rentalParam_11['houseInfo.rentalType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '套房'")   
        rentalParam_11['houseInfo.hiddenDangerLevel.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='隐患程度', displayName='安全')
        responseDict = ShiYouFangWuIntf.add_ChuZuFang(chuZuDict=rentalParam_11, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增出租房失败')   
        
        fuWuParam = copy.deepcopy(ShiYouRenKouPara.fuWuRenYuanDict)      
        fuWuParam['serviceTeamMemberBase.org.id'] = orgInit['DftWangGeOrgId']
        fuWuParam['serviceTeamMemberBase.name'] = '服务%s'%CommonUtil.createRandomString()
        fuWuParam['serviceTeamMemberBase.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别(男、女)', displayName='男')     
        fuWuParam['serviceTeamMemberBase.mobile'] = '13011111111'
        responseDict = ShiYouRenKouIntf.add_FuWuChengYuan(fuWuDict=fuWuParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增成员失败')   
        
        RecordParam = copy.deepcopy(ShiYouFangWuPara.serviceRecordObject) 
        RecordParam['mode']='add'
        RecordParam['serviceRecord.userOrgId'] = orgInit['DftWangGeOrgId']
        RecordParam['serviceRecord.organization.id'] = orgInit['DftWangGeOrgId']
        RecordParam['serviceRecord.teamId'] = '0'
        RecordParam['isSubmit'] = 'true'
        RecordParam['serviceRecord.occurDate'] = Time.getCurrentDate() 
        RecordParam['serviceRecord.occurPlace'] = '服务地点'   
        RecordParam['serviceRecord.serviceMembers'] = str(CommonIntf.getDbQueryResult(dbCommand = "select t.id from Serviceteammemberbase t where t.name='%s'" % (fuWuParam['serviceTeamMemberBase.name'])))+'-'+fuWuParam['serviceTeamMemberBase.name']+'-0'
        RecordParam['serviceRecord.recordType'] = ShiYouFangWuPara.recordTypeDict['paiChaLei']
        RecordParam['serviceRecord.serviceObjects'] = str(CommonIntf.getDbQueryResult(dbCommand = "select t.id from RENTALHOUSE t where t.address='%s'" % (houseParam_11['houseInfo.address'])))+'-'+houseParam_11['houseInfo.address']+'-RENTALHOUSE'
        responseDict = ShiYouFangWuIntf.add_XunChangQingKuang(xunChangDict=RecordParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增巡场情况失败')               
        
        param_11 = copy.deepcopy(ShiYouFangWuPara.checkRecordDict)
        param_11['id'] = CommonIntf.getDbQueryResult(dbCommand = "select max(t.id) from serviceRecords t")
        ret = ShiYouFangWuIntf.check_XunChangQingKuang(param_11, objectIds=CommonIntf.getDbQueryResult(dbCommand = "select t.id from RENTALHOUSE t where t.address='%s'" % (houseParam_11['houseInfo.address'])),orgId=RecordParam['serviceRecord.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找巡场情况失败') 
        XiaQuGuanLiIntf.xiaQuGuanLiMemberDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        pass 

    def testXunChangQingKuangEdit_12(self):
        '''出租房添加巡场情况'''
        XiaQuGuanLiIntf.xiaQuGuanLiMemberDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        houseParam_12 = copy.deepcopy(ShiYouFangWuPara.houseObject) 
        houseParam_12['dailogName']='rentalHouseMaintanceDialog'
        houseParam_12['houseInfo.organization.id'] = orgInit['DftWangGeOrgId']
        houseParam_12['mode']='add'
        houseParam_12['isUseFrom'] = 'actualHouse'
        houseParam_12['houseInfo.organization.orgName'] = orgInit['DftWangGeOrg']
        houseParam_12['houseInfo.addressType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '现居住址类型') and p.displayname = '其他'")
        houseParam_12['currentAddressType'] = houseParam_12['houseInfo.addressType.id']    
        houseParam_12['houseInfo.address'] = '出租房%s'%CommonUtil.createRandomString() 
        houseParam_12['houseInfo.isRentalHouse'] = 'true'      
        responseDict = ShiYouFangWuIntf.add_ShiYouFangWu(fangWuDict=houseParam_12, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增实有房失败')       
                   
        rentalParam_12 = copy.deepcopy(ShiYouFangWuPara.rentalObject) 
        rentalParam_12['houseInfo.organization.id'] = houseParam_12['houseInfo.organization.id']
        rentalParam_12['houseInfo.houseId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rentalHouse t where t.address='%s'" % (houseParam_12['houseInfo.address']))
        rentalParam_12['houseInfo.orgInternalCode'] = CommonIntf.getDbQueryResult(dbCommand = "select t.orginternalcode from ORGANIZATIONS t where t.orgname='%s'" % (rentalParam_12['houseInfo.organization.id']))
        rentalParam_12['dailogName']='rentalHouseMaintanceDialog'
        rentalParam_12['mode']='add'
        rentalParam_12['houseInfo.id'] = str(CommonIntf.getDbQueryResult(dbCommand = "select max(t.id) from RENTALHOUSE t"))
        rentalParam_12['houseInfo.isEmphasis'] = '0'
        rentalParam_12['houseInfo.rentalPerson'] = '房东'
        rentalParam_12['houseInfo.rentalType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '套房'")   
        rentalParam_12['houseInfo.hiddenDangerLevel.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='隐患程度', displayName='安全')
        responseDict = ShiYouFangWuIntf.add_ChuZuFang(chuZuDict=rentalParam_12, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增出租房失败')   
        
        fuWuParam = copy.deepcopy(ShiYouRenKouPara.fuWuRenYuanDict)      
        fuWuParam['serviceTeamMemberBase.org.id'] = orgInit['DftWangGeOrgId']
        fuWuParam['serviceTeamMemberBase.name'] = '服务%s'%CommonUtil.createRandomString()
        fuWuParam['serviceTeamMemberBase.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别(男、女)', displayName='男')     
        fuWuParam['serviceTeamMemberBase.mobile'] = '13011111111'
        responseDict = ShiYouRenKouIntf.add_FuWuChengYuan(fuWuDict=fuWuParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增成员失败')   
        
        RecordParam = copy.deepcopy(ShiYouFangWuPara.serviceRecordObject) 
        RecordParam['mode']='add'
        RecordParam['serviceRecord.userOrgId'] = '1'
        RecordParam['serviceRecord.organization.id'] = orgInit['DftWangGeOrgId']
        RecordParam['serviceRecord.teamId'] = '0'
        RecordParam['isSubmit'] = 'true'
        RecordParam['serviceRecord.occurDate'] = Time.getCurrentDate()  
        RecordParam['serviceRecord.occurPlace'] = '服务地点%s'%CommonUtil.createRandomString()   
        RecordParam['serviceRecord.serviceMembers'] = str(CommonIntf.getDbQueryResult(dbCommand = "select t.id from Serviceteammemberbase t where t.name='%s'" % (fuWuParam['serviceTeamMemberBase.name'])))+'-'+fuWuParam['serviceTeamMemberBase.name']+'-0'
        RecordParam['serviceRecord.recordType'] = ShiYouFangWuPara.recordTypeDict['paiChaLei']
        RecordParam['serviceRecord.serviceObjects'] = str(CommonIntf.getDbQueryResult(dbCommand = "select t.id from RENTALHOUSE t where t.address='%s'" % (houseParam_12['houseInfo.address'])))+'-'+houseParam_12['houseInfo.address']+'-RENTALHOUSE'
        responseDict = ShiYouFangWuIntf.add_XunChangQingKuang(xunChangDict=RecordParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增巡场情况失败')               
        
        param_12 = copy.deepcopy(ShiYouFangWuPara.checkRecordDict)
        param_12['id'] = CommonIntf.getDbQueryResult(dbCommand = "select max(t.id) from serviceRecords t")
        ret = ShiYouFangWuIntf.check_XunChangQingKuang(param_12, objectIds=CommonIntf.getDbQueryResult(dbCommand = "select t.id from RENTALHOUSE t where t.address='%s'" % (houseParam_12['houseInfo.address'])),orgId=RecordParam['serviceRecord.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找巡场情况失败') 
        
        editRecordParam = copy.deepcopy(ShiYouFangWuPara.serviceRecordObject) 
        editRecordParam['mode']='edit'
        editRecordParam['serviceRecord.userOrgId'] = RecordParam['serviceRecord.userOrgId']
        editRecordParam['serviceRecord.organization.id'] = RecordParam['serviceRecord.organization.id']
        editRecordParam['serviceRecord.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from serviceRecords t where t.occurplace='%s'" % (RecordParam['serviceRecord.occurPlace']))
        editRecordParam['serviceRecord.teamId'] = RecordParam['serviceRecord.teamId']
        editRecordParam['isSubmit'] = RecordParam['isSubmit']
        editRecordParam['serviceRecord.occurDate'] = RecordParam['serviceRecord.occurDate']  
        editRecordParam['serviceRecord.occurPlace'] = RecordParam['serviceRecord.occurPlace']   
        editRecordParam['serviceRecord.serviceMembers'] = str(CommonIntf.getDbQueryResult(dbCommand = "select t.id from Serviceteammemberbase t where t.name='%s'" % (fuWuParam['serviceTeamMemberBase.name'])))+'-'+fuWuParam['serviceTeamMemberBase.name']+'-0'
        editRecordParam['serviceRecord.recordType'] = ShiYouFangWuPara.recordTypeDict['zhengGaiLei']
        editRecordParam['serviceRecord.serviceObjects'] = RecordParam['serviceRecord.serviceObjects']
        responseDict = ShiYouFangWuIntf.edit_XunChangQingKuang(xunChangDict=editRecordParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改巡场情况失败') 
        
        param_12['id'] = CommonIntf.getDbQueryResult(dbCommand = "select max(t.id) from serviceRecords t")
        ret = ShiYouFangWuIntf.check_XunChangQingKuang(param_12, objectIds=CommonIntf.getDbQueryResult(dbCommand = "select t.id from RENTALHOUSE t where t.address='%s'" % (houseParam_12['houseInfo.address'])),orgId=RecordParam['serviceRecord.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找巡场情况失败')                   
        XiaQuGuanLiIntf.xiaQuGuanLiMemberDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        pass 
    
    def testXunChangQingKuangDelete_12(self):
        '''出租房添加巡场情况'''
        XiaQuGuanLiIntf.xiaQuGuanLiMemberDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        houseParam_12 = copy.deepcopy(ShiYouFangWuPara.houseObject) 
        houseParam_12['dailogName']='rentalHouseMaintanceDialog'
        houseParam_12['houseInfo.organization.id'] = orgInit['DftWangGeOrgId']
        houseParam_12['mode']='add'
        houseParam_12['isUseFrom'] = 'actualHouse'
        houseParam_12['houseInfo.organization.orgName'] = orgInit['DftWangGeOrg']
        houseParam_12['houseInfo.addressType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '现居住址类型') and p.displayname = '其他'")
        houseParam_12['currentAddressType'] = houseParam_12['houseInfo.addressType.id']    
        houseParam_12['houseInfo.address'] = '出租房%s'%CommonUtil.createRandomString() 
        houseParam_12['houseInfo.isRentalHouse'] = 'true'      
        responseDict = ShiYouFangWuIntf.add_ShiYouFangWu(fangWuDict=houseParam_12, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增实有房失败')       
                   
        rentalParam_12 = copy.deepcopy(ShiYouFangWuPara.rentalObject) 
        rentalParam_12['houseInfo.organization.id'] = houseParam_12['houseInfo.organization.id']
        rentalParam_12['houseInfo.houseId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rentalHouse t where t.address='%s'" % (houseParam_12['houseInfo.address']))
        rentalParam_12['houseInfo.orgInternalCode'] = CommonIntf.getDbQueryResult(dbCommand = "select t.orginternalcode from ORGANIZATIONS t where t.orgname='%s'" % (rentalParam_12['houseInfo.organization.id']))
        rentalParam_12['dailogName']='rentalHouseMaintanceDialog'
        rentalParam_12['mode']='add'
        rentalParam_12['houseInfo.id'] = str(CommonIntf.getDbQueryResult(dbCommand = "select max(t.id) from RENTALHOUSE t"))
        rentalParam_12['houseInfo.isEmphasis'] = '0'
        rentalParam_12['houseInfo.rentalPerson'] = '房东'
        rentalParam_12['houseInfo.rentalType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '套房'")   
        rentalParam_12['houseInfo.hiddenDangerLevel.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='隐患程度', displayName='安全')
        responseDict = ShiYouFangWuIntf.add_ChuZuFang(chuZuDict=rentalParam_12, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增出租房失败')   
        
        fuWuParam = copy.deepcopy(ShiYouRenKouPara.fuWuRenYuanDict)      
        fuWuParam['serviceTeamMemberBase.org.id'] = orgInit['DftWangGeOrgId']
        fuWuParam['serviceTeamMemberBase.name'] = '服务%s'%CommonUtil.createRandomString()
        fuWuParam['serviceTeamMemberBase.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别(男、女)', displayName='男')     
        fuWuParam['serviceTeamMemberBase.mobile'] = '13011111111'
        responseDict = ShiYouRenKouIntf.add_FuWuChengYuan(fuWuDict=fuWuParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增成员失败')   
        
        RecordParam = copy.deepcopy(ShiYouFangWuPara.serviceRecordObject) 
        RecordParam['mode']='add'
        RecordParam['serviceRecord.userOrgId'] = '1'
        RecordParam['serviceRecord.organization.id'] = orgInit['DftWangGeOrgId']
        RecordParam['serviceRecord.teamId'] = '0'
        RecordParam['isSubmit'] = 'true'
        RecordParam['serviceRecord.occurDate'] = Time.getCurrentDate()
        RecordParam['serviceRecord.occurPlace'] = '服务地点%s'%CommonUtil.createRandomString()   
        RecordParam['serviceRecord.serviceMembers'] = str(CommonIntf.getDbQueryResult(dbCommand = "select t.id from Serviceteammemberbase t where t.name='%s'" % (fuWuParam['serviceTeamMemberBase.name'])))+'-'+fuWuParam['serviceTeamMemberBase.name']+'-0'
        RecordParam['serviceRecord.recordType'] = ShiYouFangWuPara.recordTypeDict['paiChaLei']
        RecordParam['serviceRecord.serviceObjects'] = str(CommonIntf.getDbQueryResult(dbCommand = "select t.id from RENTALHOUSE t where t.address='%s'" % (houseParam_12['houseInfo.address'])))+'-'+houseParam_12['houseInfo.address']+'-RENTALHOUSE'
        responseDict = ShiYouFangWuIntf.add_XunChangQingKuang(xunChangDict=RecordParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增巡场情况失败')               
        
        param_12 = copy.deepcopy(ShiYouFangWuPara.checkRecordDict)
        param_12['id'] = CommonIntf.getDbQueryResult(dbCommand = "select max(t.id) from serviceRecords t")
        ret = ShiYouFangWuIntf.check_XunChangQingKuang(param_12, objectIds=CommonIntf.getDbQueryResult(dbCommand = "select t.id from RENTALHOUSE t where t.address='%s'" % (houseParam_12['houseInfo.address'])),orgId=RecordParam['serviceRecord.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找巡场情况失败')       
        
        deleteparam_12 = copy.deepcopy(ShiYouFangWuPara.deleteFangWuDict)
        deleteparam_12['mode'] = 'delete'
        deleteparam_12['recordIds'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from serviceRecords t where t.occurplace='%s'" % (RecordParam['serviceRecord.occurPlace']))
        ret = ShiYouFangWuIntf.delete_XunChangQingKuang(deleteparam_12,username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '删除实有房屋失败')             
                      
        ret = ShiYouFangWuIntf.check_XunChangQingKuang(param_12, objectIds=CommonIntf.getDbQueryResult(dbCommand = "select t.id from RENTALHOUSE t where t.address='%s'" % (houseParam_12['houseInfo.address'])),orgId=RecordParam['serviceRecord.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '删除的巡场情况信息仍然存在')          
        XiaQuGuanLiIntf.xiaQuGuanLiMemberDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        pass 

    def tearDown(self):
        pass
if __name__ == "__main__":
    suite = unittest.TestSuite()
    
#实有房屋
#     suite.addTest(ShiYouFangWu("testShiYouFangWuAdd_01"))
#     suite.addTest(ShiYouFangWu("testShiYouFangWuDelete_03"))
#    suite.addTest(ShiYouFangWu("testShiYouFangWuEdit_04"))   
#     suite.addTest(ShiYouFangWu("testShiYouFangWuSearch_05")) 
#     suite.addTest(ShiYouFangWu("testShiYouFangWuImportAndDownLoad_06"))
#     suite.addTest(ShiYouFangWu("testZhuHuXinXiAdd_07")) 
#     suite.addTest(ShiYouFangWu("testZhuHuXinXiChange_07"))
#     suite.addTest(ShiYouFangWu("testZhuHuXinXiDelete_07")) 
#     suite.addTest(ShiYouFangWu("testShiYouFangWuTransfer_08")) 
#    
#出租房   
#     suite.addTest(ShiYouFangWu("testChuZuFangAdd_02"))
#     suite.addTest(ShiYouFangWu("testChuZuFangLogOut_02"))
#     suite.addTest(ShiYouFangWu("testChuZuFangDelete_03"))
#     suite.addTest(ShiYouFangWu("testChuZuFangZhuHuXinXiAdd_07")) 
#     suite.addTest(ShiYouFangWu("testZhiAnFuZeRenAdd_09"))   
#     suite.addTest(ShiYouFangWu("testZhiAnFuZeRenDelete_10"))   
#     suite.addTest(ShiYouFangWu("testZhiAnFuZeRenLeave_10"))
#     suite.addTest(ShiYouFangWu("testZhiAnFuZeRenBack_10"))
#     suite.addTest(ShiYouFangWu("testXunChangQingKuangAdd_11"))  
#     suite.addTest(ShiYouFangWu("testXunChangQingKuangEdit_12"))  
    suite.addTest(ShiYouFangWu("testXunChangQingKuangDelete_12"))  


    results = unittest.TextTestRunner().run(suite)
    pass
