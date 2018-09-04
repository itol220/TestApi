# -*- coding:UTF-8 -*-
'''
Created on 2016-3-8

@author: chanyan
'''
from __future__ import unicode_literals
import unittest
import copy
from COMMON import Log
from COMMON import CommonUtil
from COMMON import Time
from CONFIG.Define import LogLevel
from CONFIG.InitDefaultPara import orgInit,userInit
from Interface.PingAnJianShe.SystemMgr import SystemMgrIntf
from Interface.PingAnJianShe.Common import CommonIntf
from Interface.PingAnTong.FangWuXinXi import FangWuXinXiIntf,\
    FangWuXinXiPara
from Interface.PingAnTong.RenKouXinXi import RenKouXinXiIntf,\
    RenKouXinXiPara
from Interface.PingAnJianShe.ShiYouFangWu import ShiYouFangWuIntf
from Interface.PingAnJianShe.ShiYouRenKou import ShiYouRenKouIntf

class FangWuXinXi(unittest.TestCase):

    def setUp(self):
        SystemMgrIntf.initEnv()
        ShiYouRenKouIntf.deleteAllPopulation()
        ShiYouFangWuIntf.deleteAllActualHouse()
        pass
    
    def testFangWuXinXi_01(self):
        """新增、修改房屋信息"""
    #新增房屋信息
        FangWParam = copy.deepcopy(FangWuXinXiPara.fangWuObject) 
        FangWParam['tqmobile'] = 'ture'
        FangWParam['houseInfo.organization.id'] = orgInit['DftWangGeOrgId']
        FangWParam['houseInfo.address'] = '房屋准确地址'
        FangWParam['houseInfo.addressType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '现居住址类型') and p.displayname = '其他'")
 
        #验证所属网格必填
        FangWParam['houseInfo.organization.id'] =''
        responseDict = FangWuXinXiIntf.add_FangWu(FangWParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertFalse(responseDict.result, '新增房屋信息所属网格必填项为空仍能新增，验证失败') 
        Log.LogOutput(LogLevel.DEBUG, "新增房屋信息所属网格必填项不能为空")
        FangWParam['houseInfo.organization.id'] = orgInit['DftWangGeOrgId']
        #验证房屋准确地址必填
        FangWParam['houseInfo.address'] =''
        responseDict = FangWuXinXiIntf.add_FangWu(FangWParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertFalse(responseDict.result, '新增房屋信息房屋准确地址必填项为空仍能新增，验证失败') 
        Log.LogOutput(LogLevel.DEBUG, "新增房屋信息房屋准确地址必填项不能为空")        
        FangWParam['houseInfo.address'] = '房屋准确地址%s'%CommonUtil.createRandomString()
        #验证现居住址类型必填
        FangWParam['houseInfo.addressType.id'] = ''
        responseDict = FangWuXinXiIntf.add_FangWu(FangWParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertFalse(responseDict.result, '新增房屋信息现居住址类型必填项为空仍能新增，验证失败') 
        Log.LogOutput(LogLevel.DEBUG, "新增房屋信息现居住址类型必填项不能为空")        
        FangWParam['houseInfo.addressType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '现居住址类型') and p.displayname = '其他'")
 
        FangWParam['houseInfo.isRentalHouse'] = 'true' #是否为出租房：false-否（默认） true-是
        FangWParam['houseInfo.buildingName'] = '建筑物名称%s'%CommonUtil.createRandomString()
        FangWParam['houseInfo.propertyName'] = '物管单位%s'%CommonUtil.createRandomString()
        FangWParam['houseInfo.houseOwner'] = '业主%s'%CommonUtil.createRandomString()
        FangWParam['houseInfo.buildingUses.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '住宅'")   #建筑物用途：住宅、商业、办公、工业、综合、仓储、其他
        FangWParam['houseInfo.houseOwnerIdCardNo'] = '330000195501010001'
        FangWParam['houseInfo.telephone'] = '3610000' #代表人电话
        FangWParam['houseInfo.houseDoorModel'] = '房屋类型%s'%CommonUtil.createRandomString()
        FangWParam['houseInfo.builtYear'] = '2015-10-10 15:09:00'
        FangWParam['houseInfo.houseArea'] = '100'  #面积
        FangWParam['houseInfo.houseStructure.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '钢结构'")   #房屋结构
        FangWParam['houseInfo.houseUses.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '个人住宅'")   #房屋用途
        FangWParam['houseInfo.houseInfo.ownProperty.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '自有产权'")   #房屋来源？
        FangWParam['houseInfo.housingVouchers.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '房屋所有权证'")   #房屋凭证
        FangWParam['houseInfo.houseRightNumber'] = '111' #房屋权证号
        FangWParam['houseInfo.houseRightNumberDate'] = Time.getCurrentDateAndTime()
    #土地信息         
        FangWParam['houseInfo.landDocuments.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '国有土地使用权证'")   #土地凭证
        FangWParam['houseInfo.landRightsNumbe'] = '222' #土地权证号
        FangWParam['houseInfo.landRightsNumbeDate'] = Time.getCurrentDateAndTime()
        FangWParam['houseInfo.propertyTypes.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '单位'")   #产权人类型
        FangWParam['houseInfo.name'] = '产权人姓名%s'%CommonUtil.createRandomString()
        FangWParam['houseInfo.certificateType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '营业执照'")   #证件类型
        FangWParam['houseInfo.certificateNumbe'] = '333' #证件号码
        FangWParam['houseInfo.propertyPersonTel'] = '3710000' #产权人电话
        FangWParam['houseInfo.propertyPersonMobile'] = '13900000000'
        FangWParam['houseInfo.remark'] = '备注'
    #出租信息        
        FangWParam['houseInfo.rentalPerson'] = '房东姓名%s'%CommonUtil.createRandomString()
        FangWParam['houseInfo.rentalType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '套房'")   #出租房类型
        FangWParam['houseInfo.hiddenDangerLevel.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '一般'")   #隐患程度
            
        FangWParam['houseInfo.houseFileNum'] = '01' #租赁备案证号
        FangWParam['houseInfo.usage.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '宿舍'")   #出租用途
        FangWParam['houseInfo.lessorType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '个人'")   #出租人类型
        FangWParam['houseInfo.registDate'] = '2015-11-10 15:09:00'
        FangWParam['houseInfo.lessorDate'] = Time.getCurrentDateAndTime()
        FangWParam['houseInfo.rentalHouseProperty.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '私房'")   #出租房性质
        FangWParam['houseInfo.mangerTypes.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '甲'")   #管理类型
        FangWParam['houseInfo.rentalCertificateType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '营业执照'")   #证件类型
        FangWParam['houseInfo.rentalCertificateNumbe'] = '444' #证件号码
        FangWParam['houseInfo.rentalTelephone'] = '3820000'
        FangWParam['houseInfo.rentalMobileNumber'] = '13820000000'
        FangWParam['houseInfo.lessorAddress'] = '房主地址'
        FangWParam['houseInfo.roomNumber'] = '3' #房间数
        FangWParam['houseInfo.limitPersons'] = '3' #限住人数
        FangWParam['houseInfo.rentMonth'] = '800' #月租金
        FangWParam['houseInfo.hiddenRectification'] = '隐患情况%s'%CommonUtil.createRandomString()
 
        responseDict = FangWuXinXiIntf.add_FangWu(FangWParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增房屋信息失败')       
       
    #检查手机端新增的房屋信息
        param = copy.deepcopy(FangWuXinXiPara.checkFangWuDict)    
        param['address'] = FangWParam['houseInfo.address'] 
        param['id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from houseInfo t where t.address='%s'" % (FangWParam['houseInfo.address']))     
        ret = FangWuXinXiIntf.check_House(param,orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111') 
        self.assertTrue(ret, '查找房屋信息失败') 
        
         
    #修改房屋信息
        editParam = copy.deepcopy(FangWuXinXiPara.fangWuObject) 
        editParam['houseInfo.id'] =CommonIntf.getDbQueryResult(dbCommand = "select t.id from houseInfo t where t.address='%s'" % (FangWParam['houseInfo.address']))
        editParam['houseInfo.organization.id'] = orgInit['DftWangGeOrgId']
        editParam['houseInfo.address'] = '修改房屋准确地址%s'%CommonUtil.createRandomString()
        editParam['houseInfo.addressType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '现居住址类型') and p.displayname = '其他'")
        responseDict = FangWuXinXiIntf.edit_FangWu(editParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改房屋信息失败') 
         
    #检查手机端新增房屋信息的详细信息
        param = copy.deepcopy(FangWuXinXiPara.checkFangWuDict)    
        param['address'] = editParam['houseInfo.address'] 
        param['id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from houseInfo t where t.address='%s'" % (editParam['houseInfo.address']))     
        ret = FangWuXinXiIntf.check_FangWu(param,houseInfoId=editParam['houseInfo.id'],username=userInit['DftWangGeUser'], password='11111111') 
        self.assertTrue(ret, '查找房屋的详细信息失败')  

    #检查手机端新增的房屋信息是否与pc端同步        
        ret = ShiYouFangWuIntf.check_ShiYouFangWu(param, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找实有房屋失败')
        
        pass

    def testFangWuXinXiSearch_03(self):
        """搜素房屋信息"""
    #新增房屋信息1
        FangWParam = copy.deepcopy(FangWuXinXiPara.fangWuObject) 
        FangWParam['tqmobile'] = 'ture'
        FangWParam['houseInfo.organization.id'] = orgInit['DftWangGeOrgId']
        FangWParam['houseInfo.address'] = '房屋准确地址测试1'
        FangWParam['houseInfo.addressType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '现居住址类型') and p.displayname = '其他'")
        responseDict = FangWuXinXiIntf.add_FangWu(FangWParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增房屋信息失败')  
 
    #新增房屋信息2
        newFangWParam = copy.deepcopy(FangWuXinXiPara.fangWuObject) 
        newFangWParam['tqmobile'] = 'ture'
        newFangWParam['houseInfo.organization.id'] = orgInit['DftWangGeOrgId']
        newFangWParam['houseInfo.address'] = '房屋准确地址测试2'
        newFangWParam['houseInfo.addressType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '现居住址类型') and p.displayname = '其他'")
        responseDict = FangWuXinXiIntf.add_FangWu(newFangWParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增房屋信息失败')   
         
    #搜素房屋信息
        param = copy.deepcopy(FangWuXinXiPara.checkFangWuDict)    
        param['address'] = FangWParam['houseInfo.address'] 
        param['id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from houseInfo t where t.address='%s'" % (FangWParam['houseInfo.address']))     
        ret = FangWuXinXiIntf.search_House(param,orgId=orgInit['DftWangGeOrgId'],address=FangWParam['houseInfo.address'],username=userInit['DftWangGeUser'], password='11111111') 
        self.assertTrue(ret, '搜素房屋的详细信息失败')  
 
    def testChuZuFang_06(self):
        """新增、修改出租房信息"""
    #新增出租房信息
        ChuZuFangParam = copy.deepcopy(FangWuXinXiPara.fangWuObject) 
        ChuZuFangParam['tqmobile'] = 'ture'
        ChuZuFangParam['houseInfo.organization.id'] = orgInit['DftWangGeOrgId']
        ChuZuFangParam['houseInfo.address'] = '出租房房屋准确地址%s'%CommonUtil.createRandomString()
        ChuZuFangParam['houseInfo.addressType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '现居住址类型') and p.displayname = '其他'")
        ChuZuFangParam['houseInfo.isRentalHouse'] = 'true' #出租房 true（默认）即必填
 
        ChuZuFangParam['houseInfo.buildingName'] = '建筑物名称%s'%CommonUtil.createRandomString()
        ChuZuFangParam['houseInfo.propertyName'] = '物管单位%s'%CommonUtil.createRandomString()
        ChuZuFangParam['houseInfo.houseOwner'] = '业主%s'%CommonUtil.createRandomString()
        ChuZuFangParam['houseInfo.buildingUses.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '住宅'")   #建筑物用途：住宅、商业、办公、工业、综合、仓储、其他
        ChuZuFangParam['houseInfo.houseOwnerIdCardNo'] = '330000195501010001'
        ChuZuFangParam['houseInfo.telephone'] = '3610000' #代表人电话
        ChuZuFangParam['houseInfo.houseDoorModel'] = '房屋类型%s'%CommonUtil.createRandomString()
        ChuZuFangParam['houseInfo.builtYear'] = '2015-10-10 15:09:00'
        ChuZuFangParam['houseInfo.houseArea'] = '100'  #面积
        ChuZuFangParam['houseInfo.houseStructure.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '钢结构'")   #房屋结构
        ChuZuFangParam['houseInfo.houseUses.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '个人住宅'")   #房屋用途
        ChuZuFangParam['houseInfo.houseInfo.ownProperty.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '自有产权'")   #房屋来源？
        ChuZuFangParam['houseInfo.housingVouchers.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '房屋所有权证'")   #房屋凭证
        ChuZuFangParam['houseInfo.houseRightNumber'] = '111' #房屋权证号
        ChuZuFangParam['houseInfo.houseRightNumberDate'] = Time.getCurrentDateAndTime()
    #土地信息         
        ChuZuFangParam['houseInfo.landDocuments.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '国有土地使用权证'")   #土地凭证
        ChuZuFangParam['houseInfo.landRightsNumbe'] = '222' #土地权证号
        ChuZuFangParam['houseInfo.landRightsNumbeDate'] = Time.getCurrentDateAndTime()
        ChuZuFangParam['houseInfo.propertyTypes.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '单位'")   #产权人类型
        ChuZuFangParam['houseInfo.name'] = '产权人姓名%s'%CommonUtil.createRandomString()
        ChuZuFangParam['houseInfo.certificateType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '营业执照'")   #证件类型
        ChuZuFangParam['houseInfo.certificateNumbe'] = '333' #证件号码
        ChuZuFangParam['houseInfo.propertyPersonTel'] = '3710000' #产权人电话
        ChuZuFangParam['houseInfo.propertyPersonMobile'] = '13900000000'
        ChuZuFangParam['houseInfo.remark'] = '备注'
    #出租信息        
        ChuZuFangParam['houseInfo.rentalPerson'] = '房东姓名%s'%CommonUtil.createRandomString()
        ChuZuFangParam['houseInfo.rentalType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '套房'")   #出租房类型
        ChuZuFangParam['houseInfo.hiddenDangerLevel.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '一般'")   #隐患程度
            
        ChuZuFangParam['houseInfo.houseFileNum'] = '01' #租赁备案证号
        ChuZuFangParam['houseInfo.usage.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '宿舍'")   #出租用途
        ChuZuFangParam['houseInfo.lessorType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '个人'")   #出租人类型
        ChuZuFangParam['houseInfo.registDate'] = '2015-11-10 15:09:00'
        ChuZuFangParam['houseInfo.lessorDate'] = Time.getCurrentDateAndTime()
        ChuZuFangParam['houseInfo.rentalHouseProperty.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '私房'")   #出租房性质
        ChuZuFangParam['houseInfo.mangerTypes.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '甲'")   #管理类型
        ChuZuFangParam['houseInfo.rentalCertificateType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '营业执照'")   #证件类型
        ChuZuFangParam['houseInfo.rentalCertificateNumbe'] = '444' #证件号码
        ChuZuFangParam['houseInfo.rentalTelephone'] = '3820000'
        ChuZuFangParam['houseInfo.rentalMobileNumber'] = '13820000000'
        ChuZuFangParam['houseInfo.lessorAddress'] = '房主地址'
        ChuZuFangParam['houseInfo.roomNumber'] = '3' #房间数
        ChuZuFangParam['houseInfo.limitPersons'] = '3' #限住人数
        ChuZuFangParam['houseInfo.rentMonth'] = '800' #月租金
        ChuZuFangParam['houseInfo.hiddenRectification'] = '隐患情况%s'%CommonUtil.createRandomString()
 
        responseDict = FangWuXinXiIntf.add_ChuZuFang(ChuZuFangParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增出租房失败')       
       
    #检查手机端新增的房屋信息
        param = copy.deepcopy(FangWuXinXiPara.checkFangWuDict)    
        param['address'] = ChuZuFangParam['houseInfo.address'] 
        param['id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from houseInfo t where t.address='%s'" % (ChuZuFangParam['houseInfo.address']))     
        ret = FangWuXinXiIntf.check_House(param,orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111') 
        self.assertTrue(ret, '查找出租房失败') 
        
#            
#     #修改房屋信息 --修改提交异常代码（bug）
#         editParam = copy.deepcopy(FangWuXinXiPara.fangWuObject) 
#         editParam['houseInfo.id'] =CommonIntf.getDbQueryResult(dbCommand = "select t.id from houseInfo t where t.address='%s'" % (ChuZuFangParam['houseInfo.address']))
#         editParam['houseInfo.organization.id'] = orgInit['DftWangGeOrgId']
#         editParam['houseInfo.address'] = '修改房屋准确地址%s'%CommonUtil.createRandomString()
#         editParam['houseInfo.addressType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '现居住址类型') and p.displayname = '其他'")
#         responseDict = FangWuXinXiIntf.edit_ChuZuFang(editParam, username=userInit['DftWangGeUser'], password='11111111')
#         self.assertTrue(responseDict.result, '修改出租房失败') 
            
    #检查手机端新增房屋信息的详细信息
        param = copy.deepcopy(FangWuXinXiPara.checkFangWuDict)    
        param['address'] = ChuZuFangParam['houseInfo.address'] 
        param['id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rentalHouse t where t.address='%s'" % (ChuZuFangParam['houseInfo.address']))     
        ret = FangWuXinXiIntf.check_ChuZuFang(param,houseInfoId=CommonIntf.getDbQueryResult(dbCommand = "select t.id from houseInfo t where t.address='%s'" % (ChuZuFangParam['houseInfo.address'])),username=userInit['DftWangGeUser'], password='11111111') 
        self.assertTrue(ret, '查找出租房的详细信息失败')  
  
    #检查手机端新增的房屋信息是否与pc端同步  
        param['id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rentalHouse t where t.address='%s'" % (ChuZuFangParam['houseInfo.address']))      
        ret = ShiYouFangWuIntf.check_ChuZuFang(param, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找出租房失败')
        
        pass        

    def testChuZuFangSearch_07(self):
        """搜素出租房信息"""
    #新增出租房信息1
        ChuZuFangParam = copy.deepcopy(FangWuXinXiPara.fangWuObject) 
        ChuZuFangParam['tqmobile'] = 'ture'
        ChuZuFangParam['houseInfo.organization.id'] = orgInit['DftWangGeOrgId']
        ChuZuFangParam['houseInfo.address'] = '出租房房屋准确地址1'
        ChuZuFangParam['houseInfo.addressType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '现居住址类型') and p.displayname = '其他'")
        ChuZuFangParam['houseInfo.isRentalHouse'] = 'true' #出租房 true（默认）即必填
        responseDict = FangWuXinXiIntf.add_ChuZuFang(ChuZuFangParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增出租房失败')   
 
    #新增出租房信息2
        newChuZuFangParam = copy.deepcopy(FangWuXinXiPara.fangWuObject) 
        newChuZuFangParam['tqmobile'] = 'ture'
        newChuZuFangParam['houseInfo.organization.id'] = orgInit['DftWangGeOrgId']
        newChuZuFangParam['houseInfo.address'] = '出租房房屋准确地址2'
        newChuZuFangParam['houseInfo.addressType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '现居住址类型') and p.displayname = '其他'")
        newChuZuFangParam['houseInfo.isRentalHouse'] = 'true' #出租房 true（默认）即必填
        responseDict = FangWuXinXiIntf.add_ChuZuFang(newChuZuFangParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增出租房失败')    
         
    #搜素房屋信息
        param = copy.deepcopy(FangWuXinXiPara.checkFangWuDict)    
        param['address'] = ChuZuFangParam['houseInfo.address'] 
        param['id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from houseInfo t where t.address='%s'" % (ChuZuFangParam['houseInfo.address']))     
        ret = FangWuXinXiIntf.search_House(param,orgId=orgInit['DftWangGeOrgId'],address=ChuZuFangParam['houseInfo.address'],username=userInit['DftWangGeUser'], password='11111111') 
        self.assertTrue(ret, '搜素房屋的详细信息失败')  
     
    def testZhuHuXinXiAdd_04(self):
        """添加房屋的住户信息"""
    #新增户籍人口
        HuJiParam = copy.deepcopy(RenKouXinXiPara.populationObject) 
        HuJiParam['tqmobile'] = 'ture'
        HuJiParam['orgId'] = orgInit['DftWangGeOrgId']
        HuJiParam['householdStaff.name'] ='测试%s'%CommonUtil.createRandomString() 
        HuJiParam['householdStaff.organization.id'] = orgInit['DftWangGeOrgId']
        HuJiParam['householdStaff.idCardNo'] = '330000199501040004'  
        HuJiParam['householdStaff.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='女')
        responseDict = RenKouXinXiIntf.add_HuJi(HuJiRenKouDict=HuJiParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口失败') 
        
    #新增房屋信息
        FangWParam = copy.deepcopy(FangWuXinXiPara.fangWuObject) 
        FangWParam['tqmobile'] = 'ture'
        FangWParam['houseInfo.organization.id'] = orgInit['DftWangGeOrgId']
        FangWParam['houseInfo.address'] = '房屋准确地址'
        FangWParam['houseInfo.addressType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '现居住址类型') and p.displayname = '其他'")
        responseDict = FangWuXinXiIntf.add_FangWu(FangWParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增房屋信息失败')   
        
    #房屋住户信息添加
        zhuHuparam = copy.deepcopy(FangWuXinXiPara.zhuHuDict)
        zhuHuparam['houseHasActualPopulation.houseId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from houseInfo t where t.address='%s'" % (FangWParam['houseInfo.address']))    
        zhuHuparam['Tenements'] = '%s-%s' % (CommonIntf.getDbQueryResult(dbCommand="select t.id from householdstaffs t where t.name='%s' and t.idCardNo='%s'" % (HuJiParam['householdStaff.name'],HuJiParam['householdStaff.idCardNo'])),'householdStaff')  
        ret = FangWuXinXiIntf.add_ZhuHuXinXi(zhuHuparam, username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '添加住户信息失败')    
       
    #检查房屋新增的住户信息
        param = copy.deepcopy(FangWuXinXiPara.checkFangWuDict)    
        param['certificateNumber'] = HuJiParam['householdStaff.idCardNo']
        param['personName'] = HuJiParam['householdStaff.name']     
        ret = FangWuXinXiIntf.check_ZhuHuXinXi(param,orgId=orgInit['DftWangGeOrgId'],houseId=zhuHuparam['houseHasActualPopulation.houseId'],username=userInit['DftWangGeUser'], password='11111111') 
        self.assertTrue(ret, '查找房屋住户信息失败')  

    #检查手机端房屋新增的住户信息与PC端同步        
        ret = ShiYouFangWuIntf.check_ZhuHuXinXi(param, houseId=zhuHuparam['houseHasActualPopulation.houseId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找住户信息失败') 
    
        pass

    def testZhuHuXinXiDelete_05(self):
        """删除房屋的住户信息"""
    #新增户籍人口1
        HuJiParam = copy.deepcopy(RenKouXinXiPara.populationObject) 
        HuJiParam['tqmobile'] = 'ture'
        HuJiParam['orgId'] = orgInit['DftWangGeOrgId']
        HuJiParam['householdStaff.name'] ='测试%s'%CommonUtil.createRandomString() 
        HuJiParam['householdStaff.organization.id'] = orgInit['DftWangGeOrgId']
        HuJiParam['householdStaff.idCardNo'] = '330000199501040005'   
        HuJiParam['householdStaff.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='女')
        responseDict = RenKouXinXiIntf.add_HuJi(HuJiRenKouDict=HuJiParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口失败') 
        
    #新增户籍人口2
        newHuJiParam = copy.deepcopy(RenKouXinXiPara.populationObject) 
        newHuJiParam['tqmobile'] = 'ture'
        newHuJiParam['orgId'] = orgInit['DftWangGeOrgId']
        newHuJiParam['householdStaff.name'] ='测试%s'%CommonUtil.createRandomString() 
        newHuJiParam['householdStaff.organization.id'] = orgInit['DftWangGeOrgId']
        newHuJiParam['householdStaff.idCardNo'] = '330000199501040015'   
        newHuJiParam['householdStaff.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='女')
        responseDict = RenKouXinXiIntf.add_HuJi(HuJiRenKouDict=newHuJiParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口失败')
        
    #新增房屋信息
        FangWParam = copy.deepcopy(FangWuXinXiPara.fangWuObject) 
        FangWParam['tqmobile'] = 'ture'
        FangWParam['houseInfo.organization.id'] = orgInit['DftWangGeOrgId']
        FangWParam['houseInfo.address'] = '房屋准确地址'
        FangWParam['houseInfo.addressType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '现居住址类型') and p.displayname = '其他'")
        responseDict = FangWuXinXiIntf.add_FangWu(FangWParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增房屋信息失败')   
        
    #房屋住户信息添加
        zhuHuparam = copy.deepcopy(FangWuXinXiPara.zhuHuDict)
        zhuHuparam['houseHasActualPopulation.houseId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from houseInfo t where t.address='%s'" % (FangWParam['houseInfo.address']))    
        zhuHuparam['Tenements'] = '%s-%s' % (CommonIntf.getDbQueryResult(dbCommand="select t.id from householdstaffs t where t.name='%s' and t.idCardNo='%s'" % (HuJiParam['householdStaff.name'],HuJiParam['householdStaff.idCardNo'])),'householdStaff')  
        ret = FangWuXinXiIntf.add_ZhuHuXinXi(zhuHuparam, username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '添加住户信息失败') 
        
        zhuHuparam['Tenements'] = '%s-%s' % (CommonIntf.getDbQueryResult(dbCommand="select t.id from householdstaffs t where t.name='%s' and t.idCardNo='%s'" % (newHuJiParam['householdStaff.name'],newHuJiParam['householdStaff.idCardNo'])),'householdStaff')  
        ret = FangWuXinXiIntf.add_ZhuHuXinXi(zhuHuparam, username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '添加住户信息失败')   
        
    #删除房屋住户信息
        zhuHuparam = copy.deepcopy(FangWuXinXiPara.zhuHuDict)
        zhuHuparam['houseHasActualPopulation.houseId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from houseInfo t where t.address='%s'" % (FangWParam['houseInfo.address']))    
        zhuHuparam['Tenements'] = '%s-%s' % (CommonIntf.getDbQueryResult(dbCommand="select t.id from householdstaffs t where t.name='%s' and t.idCardNo='%s'" % (HuJiParam['householdStaff.name'],HuJiParam['householdStaff.idCardNo'])),'householdStaff')  
        ret = FangWuXinXiIntf.delete_ZhuHuXinXi(zhuHuparam, username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '删除住户信息失败') 
       
    #检查房屋住户信息
        param = copy.deepcopy(FangWuXinXiPara.checkFangWuDict)    
        param['certificateNumber'] = HuJiParam['householdStaff.idCardNo']
        param['personName'] = HuJiParam['householdStaff.name']     
        ret = FangWuXinXiIntf.check_ZhuHuXinXi(param,orgId=orgInit['DftWangGeOrgId'],houseId=zhuHuparam['houseHasActualPopulation.houseId'],username=userInit['DftWangGeUser'], password='11111111') 
        self.assertFalse(ret, '删除的房屋住户信息在当前列表中依然存在，删除失败')  

        param['certificateNumber'] = newHuJiParam['householdStaff.idCardNo']
        param['personName'] = newHuJiParam['householdStaff.name']          
        ret = FangWuXinXiIntf.check_ZhuHuXinXi(param,orgId=orgInit['DftWangGeOrgId'],houseId=zhuHuparam['houseHasActualPopulation.houseId'],username=userInit['DftWangGeUser'], password='11111111') 
        self.assertTrue(ret, '查找房屋住户信息失败')
    
        pass
    
    def tearDown(self):
        pass
    
if __name__ == "__main__":
    suite = unittest.TestSuite() 
 
##房屋信息  
#     suite.addTest(FangWuXinXi("testFangWuXinXi_01"))
#     suite.addTest(FangWuXinXi("testFangWuXinXiSearch_03"))
#     suite.addTest(FangWuXinXi("testChuZuFang_06"))
#     suite.addTest(FangWuXinXi("testChuZuFangSearch_07"))    
#     suite.addTest(FangWuXinXi("testZhuHuXinXiAdd_04"))
#     suite.addTest(FangWuXinXi("testZhuHuXinXiDelete_05"))
    
    results = unittest.TextTestRunner().run(suite)
    pass
    
