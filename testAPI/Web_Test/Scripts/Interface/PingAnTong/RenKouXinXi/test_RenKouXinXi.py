# -*- coding:UTF-8 -*-
'''
Created on 2016-1-28

@author: chenyan
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
from Interface.PingAnTong.RenKouXinXi import RenKouXinXiIntf,\
    RenKouXinXiPara
from Interface.PingAnJianShe.ShiYouRenKou import ShiYouRenKouIntf,\
    ShiYouRenKouPara
from Interface.PingAnJianShe.XiaQuGuanLi import XiaQuGuanLiIntf
from CONFIG import InitDefaultPara


class RenKouXinXi(unittest.TestCase):

    def setUp(self):
        SystemMgrIntf.initEnv()
        ShiYouRenKouIntf.deleteAllPopulation()
        pass
    
    def testHuJiPopulation_01(self):
        """新增、修改户籍人口"""
    #新增户籍人口 --必填项验证
        HuJiParam_01 = copy.deepcopy(RenKouXinXiPara.populationObject) 
        HuJiParam_01['householdStaff.name'] ='必填项测试%s'%CommonUtil.createRandomString() 
        HuJiParam_01['householdStaff.organization.id'] = orgInit['DftWangGeOrgId']
        HuJiParam_01['householdStaff.idCardNo'] = '330000195501040000' 
        #验证姓名必填
        HuJiParam_01['householdStaff.name'] =''
        responseDict = RenKouXinXiIntf.add_HuJi(HuJiRenKouDict=HuJiParam_01, username=userInit['DftWangGeUser'], password='11111111')
        self.assertFalse(responseDict.result, '新增户籍人口姓名必填项为空仍能新增，验证失败') 
        Log.LogOutput(LogLevel.DEBUG, "新增户籍人口姓名必填项不能为空")
        HuJiParam_01['householdStaff.name'] ='测试%s'%CommonUtil.createRandomString() 
        
        #验证所属网格必填-（有且只有在网格下才可新增）
        HuJiParam_01['householdStaff.organization.id'] = ''
        responseDict = RenKouXinXiIntf.add_HuJi(HuJiRenKouDict=HuJiParam_01, username=userInit['DftWangGeUser'], password='11111111')
        self.assertFalse(responseDict.result, '新增户籍人口所属网格必填项为空仍能新增，验证失败') 
        Log.LogOutput(LogLevel.DEBUG, "新增户籍人口所属网格必填项不能为空")
        HuJiParam_01['householdStaff.organization.id'] = orgInit['DftSheQuOrgId']
        if HuJiParam_01['householdStaff.organization.id']!=orgInit['DftWangGeOrgId'] :
            Log.LogOutput(LogLevel.DEBUG, "新增户籍人口时所属网格必须为片组片格")
            HuJiParam_01['householdStaff.organization.id'] = orgInit['DftWangGeOrgId']
            
            #验证身份证必填
            HuJiParam_01['householdStaff.idCardNo'] = ''   
            responseDict = RenKouXinXiIntf.add_HuJi(HuJiRenKouDict=HuJiParam_01, username=userInit['DftWangGeUser'], password='11111111')
            self.assertFalse(responseDict.result, '新增户籍人口身份证必填项为空仍能新增，验证失败') 
            Log.LogOutput(LogLevel.DEBUG, "新增户籍人口身份证必填项不能为空")
            HuJiParam_01['householdStaff.idCardNo'] = '330000195501040000'   #性别根据身份证来确定，如何获取？
#             HuJiParam_01['householdStaff.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='女')

            responseDict = RenKouXinXiIntf.add_HuJi(HuJiRenKouDict=HuJiParam_01, username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增户籍人口失败')       

        
    #新增流动人口
        liuDongParam_01 = copy.deepcopy(RenKouXinXiPara.liuDongObject) 
        liuDongParam_01['houseInfo.organization.id'] = orgInit['DftWangGeOrgId']
        liuDongParam_01['tqmobile'] = 'true'
        liuDongParam_01['orgId'] = orgInit['DftWangGeOrgId']
        liuDongParam_01['floatingPopulation.name'] ='测试%s'%CommonUtil.createRandomString() 
        liuDongParam_01['floatingPopulation.organization.id'] = orgInit['DftWangGeOrgId']
        liuDongParam_01['floatingPopulation.idCardNo'] = '330000195501040001'
        liuDongParam_01['floatingPopulation.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='女')
        liuDongParam_01['floatingPopulation.maritalState.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '未婚'")   #婚姻状况
        liuDongParam_01['floatingPopulation.schooling.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '博士'")  #文化程度
        liuDongParam_01['floatingPopulation.politicalBackground.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '中国共产党党员'")  #政治面貌   
        liuDongParam_01['floatingPopulation.nation.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '汉族'")  #民族
        liuDongParam_01['floatingPopulation.province'] = '浙江省'  #户籍地址省
        liuDongParam_01['floatingPopulation.city'] = '杭州市'  #户籍地址市
        liuDongParam_01['floatingPopulation.district'] = '西湖区'  #户籍地址县
        liuDongParam_01['floatingPopulation.houseAddress'] = "%s%s%s" % (liuDongParam_01['floatingPopulation.province'],liuDongParam_01['floatingPopulation.city'],liuDongParam_01['floatingPopulation.district'])  #户籍地址:省、市、县
        liuDongParam_01['floatingPopulation.isHaveHouse'] = 'false'  #有无住所:true-有 ，false-没有（默认）
#         liuDongParam_01['floatingPopulation.currentAddress'] = '现居地址%s'%CommonUtil.createRandomString()  #true:现居地址
        liuDongParam_01['floatingPopulation.noHouseReason'] = '无住所原因%s'%CommonUtil.createRandomString()  #false:无住所原因
 
        #流入人口信息
        liuDongParam_01['floatingPopulation.inflowingReason.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '务工经商'")  #流入原因
        liuDongParam_01['floatingPopulation.inflowingDate'] = '2015-2-4'
        liuDongParam_01['floatingPopulation.expectedDatedue'] = '2016-2-17'
        liuDongParam_01['floatingPopulation.stayLocationType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '租赁房屋'")  #暂住处所
        liuDongParam_01['floatingPopulation.hasMarriedProve'] = 'false'
        
        responseDict = RenKouXinXiIntf.add_LiuDong(LiuDongRenKouDict=liuDongParam_01, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增流动人口失败') 

        
    #新增户籍个人信息
        HuJiParam = copy.deepcopy(RenKouXinXiPara.populationObject) 
        HuJiParam['tqmobile'] = 'true'
        HuJiParam['orgId'] = orgInit['DftWangGeOrgId']
        HuJiParam['householdStaff.name'] ='户籍人口测试%s'%CommonUtil.createRandomString() 
        HuJiParam['householdStaff.organization.id'] = orgInit['DftWangGeOrgId']
        HuJiParam['householdStaff.idCardNo'] = HuJiParam_01['householdStaff.idCardNo']   #性别根据身份证来确定，如何获取？
        HuJiParam['householdStaff.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='女')
        HuJiParam['householdStaff.maritalState.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '未婚'")   #婚姻状况
        HuJiParam['householdStaff.schooling.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '博士'")  #文化程度
        HuJiParam['householdStaff.politicalBackground.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '中国共产党党员'")  #政治面貌   
        HuJiParam['householdStaff.nation.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '汉族'")  #民族
        HuJiParam['householdStaff.province'] = '浙江省'  #户籍地址省
        HuJiParam['householdStaff.city'] = '杭州市'  #户籍地址市
        HuJiParam['householdStaff.district'] = '西湖区'  #户籍地址县
        HuJiParam['householdStaff.houseAddress'] = "%s%s%s" % (HuJiParam['householdStaff.province'],HuJiParam['householdStaff.city'],HuJiParam['householdStaff.district'])  #户籍地址:省、市、县
        HuJiParam['householdStaff.isHaveHouse'] = 'true'  #有无住所:true-有 ，false-没有（默认）
        HuJiParam_01['householdStaff.currentAddress'] = '现居地址%s'%CommonUtil.createRandomString()  #true:现居地址
#         HuJiParam['householdStaff.noHouseReason'] = '无住所原因%s'%CommonUtil.createRandomString()  #false:无住所原因
        # 选填项
        HuJiParam['householdStaff.usedName'] = '曾用名%s'%CommonUtil.createRandomString() 
        HuJiParam['householdStaff.nativePlaceAddress'] = '户籍地详址'
        HuJiParam['householdStaff.otherAddress'] = '其他住址'
        HuJiParam['householdStaff.nativePoliceStation'] = '户籍派出所'
        HuJiParam['householdStaff.mobileNumber'] = '18700000001'
        HuJiParam['householdStaff.telephone'] = '3921000'
        HuJiParam['householdStaff.email'] = '123456789@qq.com'
        HuJiParam['householdStaff.career.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '工业'")  #职业
        HuJiParam['householdStaff.workUnit'] = '工作单位或就读学校'
        HuJiParam['householdStaff.stature'] = '170'  #身高
        HuJiParam['householdStaff.bloodType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = 'A型'")  #血型
        HuJiParam['householdStaff.faith.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '无'")  #宗教信仰
        HuJiParam['householdStaff.remark'] = '备注'
        
    #户籍信息
        HuJiParam['householdStaff.accountNumber'] = '1'
        HuJiParam['householdStaff.relationShipWithHead.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '本人'")
        HuJiParam['householdStaff.residentStatus.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '人户同在'")
    # 选填项  
        HuJiParam['householdStaff.homePhone'] = '1111111'
        HuJiParam['householdStaff.outGone'] = 'false'
        
    #住房信息   -前提：个人信息中选择有住房信息，才会出现该字段 ，（即‘isHaveHouse’为‘true’时）
        HuJiParam['houseInfo.address'] = HuJiParam_01['householdStaff.currentAddress']
        
        HuJiParam['houseInfo.houseUses.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '个人住宅'")  #房屋用途
        HuJiParam['houseInfo.propertyTypes.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '个人'")  #产权人类型
        HuJiParam['houseInfo.name'] = '产权人名称'
        HuJiParam['houseInfo.certificateType.id'] = HuJiParam_01['householdStaff.currentAddress']
        HuJiParam['houseInfo.certificateNumbe'] = HuJiParam_01['householdStaff.currentAddress']
        HuJiParam['houseInfo.propertyPersonMobile'] = HuJiParam_01['householdStaff.currentAddress']
        HuJiParam['houseInfo.propertyPersonTel'] = HuJiParam_01['householdStaff.currentAddress']
        HuJiParam['houseInfo.isRentalHouse'] = HuJiParam_01['householdStaff.currentAddress']
        HuJiParam['houseInfo.remark'] = '备注'
        HuJiParam['houseInfo.rentalHouse.rentalType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '套房'")  #出租房类型
        HuJiParam['houseInfo.rentalHouse.hiddenDangerLevel.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '严重'")  #隐患程度
        HuJiParam['houseInfo.rentalHouse.rentalPerson'] = '房东姓名'
        HuJiParam['houseInfo.rentalHouse.usage.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '宿舍'")  #出租用途
        HuJiParam['houseInfo.rentalHouse.rentalHouseProperty.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '私房'")  #出租屋性质
        HuJiParam['houseInfo.rentalHouse.rentalTelephone'] = '3611111'
        HuJiParam['houseInfo.rentalHouse.rentalMobileNumber'] = '13700000000'
        HuJiParam['houseInfo.rentalHouse.lessorAddress'] = '出租人地址'
        
        param_01 = copy.deepcopy(RenKouXinXiPara.checkPopulationDict)      
        param_01['idCardNo'] = HuJiParam['householdStaff.idCardNo'] 
    #检查户籍人口中是否存在该id的人口信息 
        ret_01 = RenKouXinXiIntf.check_Population(param_01,orgId=orgInit['DftWangGeOrgId'],populationType='RESIDENT', username=userInit['DftWangGeUser'], password='11111111') 
        if ret_01 is True:
            Log.LogOutput(LogLevel.DEBUG, "户籍人口中存在该id人口信息,请重新输入id信息")
            HuJiParam['householdStaff.idCardNo'] = liuDongParam_01['floatingPopulation.idCardNo']
        #检查流动人口中是否存在该id的人口信息
            param_01['idCardNo'] = HuJiParam['householdStaff.idCardNo']
            ret_02 = RenKouXinXiIntf.check_Population(param_01, orgId=orgInit['DftWangGeOrgId'],populationType='TRAMPRESIDENT',username=userInit['DftWangGeUser'], password='11111111') 
            if ret_02 is True:        
                Log.LogOutput(LogLevel.DEBUG, "流动人口中存在该id人口信息,请重新输入id信息") 
                HuJiParam['householdStaff.idCardNo'] = '330000195501040002'    
                responseDict = RenKouXinXiIntf.add_HuJi(HuJiRenKouDict=HuJiParam, username=userInit['DftWangGeUser'], password='11111111')
                self.assertTrue(responseDict.result, '新增户籍人口失败')  
                param_01['idCardNo'] = HuJiParam['householdStaff.idCardNo']     
                ret = RenKouXinXiIntf.check_Population(param_01,orgId=orgInit['DftWangGeOrgId'],populationType='RESIDENT', username=userInit['DftWangGeUser'], password='11111111') 
                self.assertTrue(ret, '查找户籍人口失败')
            else:               
                responseDict = RenKouXinXiIntf.add_HuJi(HuJiRenKouDict=HuJiParam, username=userInit['DftWangGeUser'], password='11111111')
                self.assertTrue(responseDict.result, '新增户籍人口失败')   
                param_01['idCardNo'] = HuJiParam['householdStaff.idCardNo']    
                ret = RenKouXinXiIntf.check_Population(param_01,orgId=orgInit['DftWangGeOrgId'],populationType='RESIDENT', username=userInit['DftWangGeUser'], password='11111111') 
                self.assertTrue(ret, '查找户籍人口失败')
        else:   
    #检查流动人口中是否存在该id的人口信息  
            ret_03 = RenKouXinXiIntf.check_Population(param_01, populationType='TRAMPRESIDENT',username=userInit['DftWangGeUser'], password='11111111') 
            if ret_03 is True:        
                Log.LogOutput(LogLevel.DEBUG, "流动人口中存在该id人口信息,请重新输入id信息") 
                HuJiParam['householdStaff.idCardNo'] = '330000195501040002'    
                responseDict = RenKouXinXiIntf.add_HuJi(HuJiRenKouDict=HuJiParam, username=userInit['DftWangGeUser'], password='11111111')
                self.assertTrue(responseDict.result, '新增户籍人口失败')      
                param_01['idCardNo'] = HuJiParam['householdStaff.idCardNo'] 
                ret = RenKouXinXiIntf.check_Population(param_01,orgId=orgInit['DftWangGeOrgId'],populationType='RESIDENT', username=userInit['DftWangGeUser'], password='11111111') 
                self.assertTrue(ret, '查找户籍人口失败')
            else:               
                responseDict = RenKouXinXiIntf.add_HuJi(HuJiRenKouDict=HuJiParam, username=userInit['DftWangGeUser'], password='11111111')
                self.assertTrue(responseDict.result, '新增户籍人口失败')   
                param_01['idCardNo'] = HuJiParam['householdStaff.idCardNo']    
                ret = RenKouXinXiIntf.check_Population(param_01,orgId=orgInit['DftWangGeOrgId'],populationType='RESIDENT', username=userInit['DftWangGeUser'], password='11111111') 
                self.assertTrue(ret, '查找户籍人口失败')
                
    #修改户籍人口    
        editParam_01 = copy.deepcopy(RenKouXinXiPara.editPopulationObject) 
        editParam_01['householdStaff.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from householdstaffs t where t.idcardno='%s' and t.name='%s'" % (HuJiParam['householdStaff.idCardNo'],HuJiParam['householdStaff.name']))
        editParam_01['tqmobile'] = 'true'
        editParam_01['orgId'] = orgInit['DftWangGeOrgId']
        editParam_01['householdStaff.name'] ='修改测试%s'%CommonUtil.createRandomString() 
        editParam_01['householdStaff.organization.id'] = orgInit['DftWangGeOrgId']
        editParam_01['householdStaff.idCardNo'] = HuJiParam['householdStaff.idCardNo']    #性别根据身份证来确定，如何获取？
        editParam_01['householdStaff.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='女')
        editParam_01['householdStaff.maritalState.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '未婚'")   #婚姻状况
        editParam_01['householdStaff.schooling.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '博士'")  #文化程度
        editParam_01['householdStaff.politicalBackground.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '中国共产党党员'")  #政治面貌   
        editParam_01['householdStaff.nation.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '汉族'")  #民族
        editParam_01['householdStaff.province'] = '浙江省'  #户籍地址省
        editParam_01['householdStaff.city'] = '杭州市'  #户籍地址市
        editParam_01['householdStaff.district'] = '西湖区'  #户籍地址县
#         editParam_01['householdStaff.houseAddress'] = "%s%s%s" % (editParam_01['householdStaff.province'],HuJiParam_01['householdStaff.city'],HuJiParam_01['householdStaff.district'])  #户籍地址:省、市、县
        editParam_01['householdStaff.isHaveHouse'] = 'false'  #有无住所:true/false
#         editParam_01['householdStaff.currentAddress'] = '现居地址%s'%CommonUtil.createRandomString()  #true:现居地址
        editParam_01['householdStaff.noHouseReason'] = '无住所原因%s'%CommonUtil.createRandomString()  #false:无住所原因
        editParam_01['householdStaff.outGone'] = 'false'
        responseDict = RenKouXinXiIntf.edit_HuJi(editParam_01, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改户籍人口失败')

    #检查手机端新增的人口详细信息  
        param = copy.deepcopy(RenKouXinXiPara.checkPopulationDict)      
        param['idCardNo'] = editParam_01['householdStaff.idCardNo']         
        ret = RenKouXinXiIntf.check_HuJi(param,populationId=editParam_01['householdStaff.id'] , username=userInit['DftWangGeUser'], password='11111111') 
        self.assertTrue(ret, '查找户籍人口的详细信息失败')
                
    #检查手机端新增的人口信息是否与pc端同步
        ret = ShiYouRenKouIntf.check_HuJiPopulation(param_01, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        
        self.assertTrue(ret, '查找户籍人口失败')
          
        pass

    def testDepartmentCheck_02(self):
        """不同部门检查户籍人口"""
    #新增户籍人口
        HuJiParam_02 = copy.deepcopy(RenKouXinXiPara.populationObject) 
        HuJiParam_02['tqmobile'] = 'true'
        HuJiParam_02['orgId'] = orgInit['DftWangGeOrgId']
        HuJiParam_02['householdStaff.name'] ='不同部门检查测试%s'%CommonUtil.createRandomString() 
        HuJiParam_02['householdStaff.organization.id'] = orgInit['DftWangGeOrgId']
        HuJiParam_02['householdStaff.idCardNo'] = '330000195501040022'   #性别根据身份证来确定，如何获取？
        HuJiParam_02['householdStaff.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='女')
        HuJiParam_02['householdStaff.maritalState.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '未婚'")   #婚姻状况
        HuJiParam_02['householdStaff.schooling.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '博士'")  #文化程度
        HuJiParam_02['householdStaff.politicalBackground.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '中国共产党党员'")  #政治面貌   
        HuJiParam_02['householdStaff.nation.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '汉族'")  #民族
        HuJiParam_02['householdStaff.province'] = '浙江省'  #户籍地址省
        HuJiParam_02['householdStaff.city'] = '杭州市'  #户籍地址市
        HuJiParam_02['householdStaff.district'] = '西湖区'  #户籍地址县
        HuJiParam_02['householdStaff.houseAddress'] = "%s%s%s" % (HuJiParam_02['householdStaff.province'],HuJiParam_02['householdStaff.city'],HuJiParam_02['householdStaff.district'])  #户籍地址:省、市、县
        HuJiParam_02['householdStaff.isHaveHouse'] = 'false'  #有无住所:true/false
#         HuJiParam_02['householdStaff.currentAddress'] = '现居地址%s'%CommonUtil.createRandomString()  #true:现居地址
        HuJiParam_02['householdStaff.noHouseReason'] = '无住所原因%s'%CommonUtil.createRandomString()  #false:无住所原因

        responseDict = RenKouXinXiIntf.add_HuJi(HuJiRenKouDict=HuJiParam_02, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口失败') 

    #检查网格下新增的户籍人口信息（存在）        
        param = copy.deepcopy(RenKouXinXiPara.checkPopulationDict)      
        param['idCardNo'] = HuJiParam_02['householdStaff.idCardNo'] 
        ret = RenKouXinXiIntf.check_Population(param,orgId=orgInit['DftWangGeOrgId'],populationType='RESIDENT', username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找户籍人口失败')

    #检查不同部门下新增的户籍人口信息（不存在）           
        ret = RenKouXinXiIntf.check_Population(param,orgId=orgInit['DftWangGeOrgId1'],populationType='RESIDENT', username=userInit['DftWangGeUser1'], password='11111111')         
        self.assertFalse(ret, '自动化网格下新增的人口信息在网格1下可以检查到，部门检查失败')
      
    def testLiuDongPopulation_04(self):
        """新增、修改流动人口"""
    #新增户籍人口
        HuJiParam_04 = copy.deepcopy(RenKouXinXiPara.populationObject) 
        HuJiParam_04['tqmobile'] = 'true'
        HuJiParam_04['orgId'] = orgInit['DftWangGeOrgId']
        HuJiParam_04['householdStaff.name'] ='测试%s'%CommonUtil.createRandomString() 
        HuJiParam_04['householdStaff.organization.id'] = orgInit['DftWangGeOrgId']
        HuJiParam_04['householdStaff.idCardNo'] = '330000195501040014'   #性别根据身份证来确定，如何获取？
        HuJiParam_04['householdStaff.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='女')
        HuJiParam_04['householdStaff.maritalState.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '未婚'")   #婚姻状况
        HuJiParam_04['householdStaff.schooling.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '博士'")  #文化程度
        HuJiParam_04['householdStaff.politicalBackground.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '中国共产党党员'")  #政治面貌   
        HuJiParam_04['householdStaff.nation.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '汉族'")  #民族
        HuJiParam_04['householdStaff.province'] = '浙江省'  #户籍地址省
        HuJiParam_04['householdStaff.city'] = '杭州市'  #户籍地址市
        HuJiParam_04['householdStaff.district'] = '西湖区'  #户籍地址县
        HuJiParam_04['householdStaff.houseAddress'] = "%s%s%s" % (HuJiParam_04['householdStaff.province'],HuJiParam_04['householdStaff.city'],HuJiParam_04['householdStaff.district'])  #户籍地址:省、市、县
        HuJiParam_04['householdStaff.isHaveHouse'] = 'false'  #有无住所:true/false
#         HuJiParam_04['householdStaff.currentAddress'] = '现居地址%s'%CommonUtil.createRandomString()  #true:现居地址
        HuJiParam_04['householdStaff.noHouseReason'] = '无住所原因%s'%CommonUtil.createRandomString()  #false:无住所原因

    #户籍信息
        HuJiParam_04['householdStaff.accountNumber'] = '01'
        HuJiParam_04['householdStaff.relationShipWithHead.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '本人'")
        HuJiParam_04['householdStaff.residentStatus.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '人户同在'")

        responseDict = RenKouXinXiIntf.add_HuJi(HuJiRenKouDict=HuJiParam_04, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口失败') 
        
    #新增流动人口
        liuDongParam_04 = copy.deepcopy(RenKouXinXiPara.liuDongObject) 
        liuDongParam_04['houseInfo.organization.id'] = orgInit['DftWangGeOrgId']
        liuDongParam_04['tqmobile'] = 'true'
        liuDongParam_04['orgId'] = orgInit['DftWangGeOrgId']
        liuDongParam_04['floatingPopulation.name'] ='测试%s'%CommonUtil.createRandomString() 
        liuDongParam_04['floatingPopulation.organization.id'] = orgInit['DftWangGeOrgId']
        liuDongParam_04['floatingPopulation.idCardNo'] = '330000195501040015'
        liuDongParam_04['floatingPopulation.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='女')
        liuDongParam_04['floatingPopulation.maritalState.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '未婚'")   #婚姻状况
        liuDongParam_04['floatingPopulation.schooling.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '博士'")  #文化程度
        liuDongParam_04['floatingPopulation.politicalBackground.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '中国共产党党员'")  #政治面貌   
        liuDongParam_04['floatingPopulation.nation.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '汉族'")  #民族
        liuDongParam_04['floatingPopulation.province'] = '浙江省'  #户籍地址省
        liuDongParam_04['floatingPopulation.city'] = '杭州市'  #户籍地址市
        liuDongParam_04['floatingPopulation.district'] = '西湖区'  #户籍地址县
        liuDongParam_04['floatingPopulation.houseAddress'] = "%s%s%s" % (liuDongParam_04['floatingPopulation.province'],liuDongParam_04['floatingPopulation.city'],liuDongParam_04['floatingPopulation.district'])  #户籍地址:省、市、县
        liuDongParam_04['floatingPopulation.isHaveHouse'] = 'false'  #有无住所:true/false
#         liuDongParam_04['floatingPopulation.currentAddress'] = '现居地址%s'%CommonUtil.createRandomString()  #true:现居地址
        liuDongParam_04['floatingPopulation.noHouseReason'] = '无住所原因%s'%CommonUtil.createRandomString()  #false:无住所原因
 
        #流入人口信息
        liuDongParam_04['floatingPopulation.inflowingReason.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '务工经商'")  #流入原因
        liuDongParam_04['floatingPopulation.inflowingDate'] = '2015-2-4'
        liuDongParam_04['floatingPopulation.expectedDatedue'] = '2016-2-17'
        liuDongParam_04['floatingPopulation.stayLocationType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '租赁房屋'")  #暂住处所
        liuDongParam_04['floatingPopulation.hasMarriedProve'] = 'false'
        
        responseDict = RenKouXinXiIntf.add_LiuDong(LiuDongRenKouDict=liuDongParam_04, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增流动人口失败') 
        
    #新增流动人口的个人信息                
        liuDongParam = copy.deepcopy(RenKouXinXiPara.liuDongObject) 
        liuDongParam['houseInfo.organization.id'] = orgInit['DftWangGeOrgId']
        liuDongParam['tqmobile'] = 'true'
        liuDongParam['orgId'] = orgInit['DftWangGeOrgId']
        liuDongParam['floatingPopulation.name'] ='新增流动人口测试%s'%CommonUtil.createRandomString() 
        liuDongParam['floatingPopulation.organization.id'] = orgInit['DftWangGeOrgId']
        liuDongParam['floatingPopulation.idCardNo'] = liuDongParam_04['floatingPopulation.idCardNo']
        liuDongParam['floatingPopulation.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='女')
        liuDongParam['floatingPopulation.maritalState.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '未婚'")   #婚姻状况
        liuDongParam['floatingPopulation.schooling.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '博士'")  #文化程度
        liuDongParam['floatingPopulation.politicalBackground.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '中国共产党党员'")  #政治面貌   
        liuDongParam['floatingPopulation.nation.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '汉族'")  #民族
        liuDongParam['floatingPopulation.province'] = '浙江省'  #户籍地址省
        liuDongParam['floatingPopulation.city'] = '杭州市'  #户籍地址市
        liuDongParam['floatingPopulation.district'] = '西湖区'  #户籍地址县
        liuDongParam['floatingPopulation.houseAddress'] = "%s%s%s" % (liuDongParam['floatingPopulation.province'],liuDongParam['floatingPopulation.city'],liuDongParam['floatingPopulation.district'])  #户籍地址:省、市、县
        liuDongParam['floatingPopulation.isHaveHouse'] = 'false'  #有无住所:true/false
#         liuDongParam['floatingPopulation.currentAddress'] = '现居地址%s'%CommonUtil.createRandomString()  #true:现居地址
        liuDongParam['floatingPopulation.noHouseReason'] = '无住所原因%s'%CommonUtil.createRandomString()  #false:无住所原因
 
    #流入人口信息
        liuDongParam['floatingPopulation.inflowingReason.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '务工经商'")  #流入原因
        liuDongParam['floatingPopulation.inflowingDate'] = '2015-2-4'
        liuDongParam['floatingPopulation.expectedDatedue'] = '2016-2-17'
        liuDongParam['floatingPopulation.stayLocationType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '租赁房屋'")  #暂住处所
        liuDongParam['floatingPopulation.hasMarriedProve'] = 'false'
    #住房信息
#         liuDongParam['houseInfo.address'] = liuDongParam['floatingPopulation.currentAddress']
        
        param_04 = copy.deepcopy(RenKouXinXiPara.checkPopulationDict)      
        param_04['idCardNo'] = liuDongParam['floatingPopulation.idCardNo'] 

    #检查流动人口中是否存在该id的人口信息 
        ret_01 = RenKouXinXiIntf.check_Population(param_04,orgId=orgInit['DftWangGeOrgId'],populationType='TRAMPRESIDENT', username=userInit['DftWangGeUser'], password='11111111') 
        if ret_01 is True:
            Log.LogOutput(LogLevel.DEBUG, "流动人口中存在该id人口信息,请重新输入id信息")
            liuDongParam['floatingPopulation.idCardNo'] = HuJiParam_04['householdStaff.idCardNo']
    #检查户籍人口中是否存在该id的人口信息  
            param_04['idCardNo'] = liuDongParam['floatingPopulation.idCardNo'] 
            ret_02 = RenKouXinXiIntf.check_Population(param_04, orgId=orgInit['DftWangGeOrgId'],populationType='RESIDENT',username=userInit['DftWangGeUser'], password='11111111') 
            if ret_02 is True:        
                Log.LogOutput(LogLevel.DEBUG, "户籍人口中存在该id人口信息,请重新输入id信息")     
                liuDongParam['floatingPopulation.idCardNo'] = '330000195501040016'
                responseDict = RenKouXinXiIntf.add_LiuDong(LiuDongRenKouDict=liuDongParam, username=userInit['DftWangGeUser'], password='11111111')
                self.assertTrue(responseDict.result, '新增流动人口失败') 
                param_04['idCardNo'] = liuDongParam['floatingPopulation.idCardNo'] 
                ret = RenKouXinXiIntf.check_Population(param_04, orgId=orgInit['DftWangGeOrgId'],populationType='TRAMPRESIDENT',username=userInit['DftWangGeUser'], password='11111111') 
                self.assertTrue(ret, '查找流动人口失败')          
            else:     
                responseDict = RenKouXinXiIntf.add_LiuDong(LiuDongRenKouDict=liuDongParam, username=userInit['DftWangGeUser'], password='11111111')
                self.assertTrue(responseDict.result, '新增流动人口失败') 
                param_04['idCardNo'] = liuDongParam['floatingPopulation.idCardNo'] 
                ret = RenKouXinXiIntf.check_Population(param_04, orgId=orgInit['DftWangGeOrgId'],populationType='TRAMPRESIDENT',username=userInit['DftWangGeUser'], password='11111111') 
                self.assertTrue(ret, '查找流动人口失败')       
        else:   
    #检查户籍人口中是否存在该id的人口信息  
            param_04['idCardNo'] = liuDongParam['floatingPopulation.idCardNo'] 
            ret_02 = RenKouXinXiIntf.check_Population(param_04, populationType='RESIDENT',username=userInit['DftWangGeUser'], password='11111111') 
            if ret_02 is True:        
                Log.LogOutput(LogLevel.DEBUG, "户籍人口中存在该id人口信息,请重新输入id信息")     
                liuDongParam['floatingPopulation.idCardNo'] = '330000195501040016'
                responseDict = RenKouXinXiIntf.add_LiuDong(LiuDongRenKouDict=liuDongParam, username=userInit['DftWangGeUser'], password='11111111')
                self.assertTrue(responseDict.result, '新增流动人口失败') 
                param_04['idCardNo'] = liuDongParam['floatingPopulation.idCardNo'] 
                ret = RenKouXinXiIntf.check_Population(param_04, orgId=orgInit['DftWangGeOrgId'],populationType='TRAMPRESIDENT',username=userInit['DftWangGeUser'], password='11111111') 
                self.assertTrue(ret, '查找流动人口失败')          
            else:     
                responseDict = RenKouXinXiIntf.add_LiuDong(LiuDongRenKouDict=liuDongParam, username=userInit['DftWangGeUser'], password='11111111')
                self.assertTrue(responseDict.result, '新增流动人口失败') 
                param_04['idCardNo'] = liuDongParam['floatingPopulation.idCardNo'] 
                ret = RenKouXinXiIntf.check_Population(param_04, orgId=orgInit['DftWangGeOrgId'], populationType='TRAMPRESIDENT',username=userInit['DftWangGeUser'], password='11111111') 
                self.assertTrue(ret, '查找流动人口失败') 
                
    #修改流动人口
        editParam_04 = copy.deepcopy(RenKouXinXiPara.liuDongObject) 
        editParam_04['floatingPopulation.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from floatingPopulations t where t.idcardno='%s' and t.name='%s'" % (liuDongParam['floatingPopulation.idCardNo'],liuDongParam['floatingPopulation.name'])) 
        editParam_04['houseInfo.organization.id'] = orgInit['DftWangGeOrgId']
        editParam_04['tqmobile'] = 'true'
        editParam_04['orgId'] = orgInit['DftWangGeOrgId']
        editParam_04['floatingPopulation.name'] ='修改流动人口测试%s'%CommonUtil.createRandomString() 
        editParam_04['floatingPopulation.organization.id'] = orgInit['DftWangGeOrgId']
        editParam_04['floatingPopulation.idCardNo'] = liuDongParam['floatingPopulation.idCardNo']
        editParam_04['floatingPopulation.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='女')
        editParam_04['floatingPopulation.maritalState.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '未婚'")   #婚姻状况
        editParam_04['floatingPopulation.schooling.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '博士'")  #文化程度
        editParam_04['floatingPopulation.politicalBackground.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '中国共产党党员'")  #政治面貌   
        editParam_04['floatingPopulation.nation.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '汉族'")  #民族
        editParam_04['floatingPopulation.province'] = '浙江省'  #户籍地址省
        editParam_04['floatingPopulation.city'] = '杭州市'  #户籍地址市
        editParam_04['floatingPopulation.district'] = '西湖区'  #户籍地址县
        editParam_04['floatingPopulation.houseAddress'] = "%s%s%s" % (editParam_04['floatingPopulation.province'],editParam_04['floatingPopulation.city'],editParam_04['floatingPopulation.district'])  #户籍地址:省、市、县
        editParam_04['floatingPopulation.isHaveHouse'] = 'false'  #有无住所:true/false
#         editParam_04['floatingPopulation.currentAddress'] = '现居地址%s'%CommonUtil.createRandomString()  #true:现居地址
        editParam_04['floatingPopulation.noHouseReason'] = '无住所原因%s'%CommonUtil.createRandomString()  #false:无住所原因
 
        #流入人口信息
        editParam_04['floatingPopulation.inflowingReason.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '务工经商'")  #流入原因
        editParam_04['floatingPopulation.inflowingDate'] = '2015-2-4'
        editParam_04['floatingPopulation.expectedDatedue'] = '2016-2-17'
        editParam_04['floatingPopulation.stayLocationType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '租赁房屋'")  #暂住处所
        editParam_04['floatingPopulation.hasMarriedProve'] = 'false'
        
        responseDict = RenKouXinXiIntf.edit_LiuDong(LiuDongRenKouDict=editParam_04, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改流动人口失败') 
        
    #检查手机端新增的人口详细信息   
        param = copy.deepcopy(RenKouXinXiPara.checkPopulationDict)      
        param['idCardNo'] = editParam_04['floatingPopulation.idCardNo']         
        ret = RenKouXinXiIntf.check_LiuDong(param,populationId=editParam_04['floatingPopulation.id'] , username=userInit['DftWangGeUser'], password='11111111') 
        self.assertTrue(ret, '查找流动人口的详细信息失败')
                
    #检查手机端新增的人口信息是否与pc端同步-check2
        ret = ShiYouRenKouIntf.check_LiuDongpopulation(param_04, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找流动人口失败')
           
        pass

    def testJingWaiPopulation_05(self):
        """新增、修改境外人口"""
    #境外人口的个人信息
        jingWaiParam_05 = copy.deepcopy(RenKouXinXiPara.jingWaiObject) 
        jingWaiParam_05['tqmobile'] = 'true'
        jingWaiParam_05['orgId'] = orgInit['DftWangGeOrgId']
        jingWaiParam_05['overseaPersonnel.name'] ='境外人口测试%s'%CommonUtil.createRandomString() 
        jingWaiParam_05['overseaPersonnel.organization.id'] = orgInit['DftWangGeOrgId']
        jingWaiParam_05['overseaPersonnel.englishName'] = 'ceshi'
        jingWaiParam_05['overseaPersonnel.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='女')
        jingWaiParam_05['overseaPersonnel.certificateType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '旅游证'")   #证件种类
        jingWaiParam_05['overseaPersonnel.certificateNo'] = '1100'
        jingWaiParam_05['overseaPersonnel.isHaveHouse'] = 'false'
#         jingWaiParam_05['overseaPersonnel.currentAddress'] = '现居地址%s'%CommonUtil.createRandomString()  #true:现居地址
        jingWaiParam_05['overseaPersonnel.noHouseReason'] = '无住所原因%s'%CommonUtil.createRandomString()  #false:无住所原因
        
        jingWaiParam_05['overseaPersonnel.birthday'] = '2016-02-17'
        jingWaiParam_05['overseaPersonnel.profession.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '工程师'")   #职业
        jingWaiParam_05['overseaPersonnel.nationality'] = '美国'  #国籍
        jingWaiParam_05['overseaPersonnel.inflowReason'] = '流入原因%s'%CommonUtil.createRandomString()
        jingWaiParam_05['overseaPersonnel.arrivalTime'] = '2016-02-01'
        jingWaiParam_05['overseaPersonnel.leaveTime'] = '2017-02-17'
        jingWaiParam_05['overseaPersonnel.remark'] = '备注'

    #住房信息
#         jingWaiParam_08['houseInfo.address'] = jingWaiParam_08['overseaPersonnel.currentAddress']

        responseDict = RenKouXinXiIntf.add_JingWai(JingWaiRenKouDict=jingWaiParam_05, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增境外人口失败') 
    
    #在境外人口列表中检查境外人口是否新增成功    
        param_05 = copy.deepcopy(RenKouXinXiPara.checkPopulationDict)      
        param_05['certificateNo'] = jingWaiParam_05['overseaPersonnel.certificateNo'] 
        ret = RenKouXinXiIntf.check_Population(param_05, orgId=orgInit['DftWangGeOrgId'],populationType='OVERSEAPERSONNEL',username=userInit['DftWangGeUser'], password='11111111') 
        self.assertTrue(ret, '查找境外人口失败')
        
        editParam_05 = copy.deepcopy(RenKouXinXiPara.jingWaiObject) 
        editParam_05['tqmobile'] = 'true'
        editParam_05['orgId'] = orgInit['DftWangGeOrgId']
        editParam_05['overseaPersonnel.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from overseaPersonnel t where t.certificatetype='%s'and t.certificateno='%s'" % (jingWaiParam_05['overseaPersonnel.certificateType.id'],jingWaiParam_05['overseaPersonnel.certificateNo']))
        editParam_05['overseaPersonnel.name'] ='修改境外人口测试%s'%CommonUtil.createRandomString() 
        editParam_05['overseaPersonnel.organization.id'] = orgInit['DftWangGeOrgId']
        editParam_05['overseaPersonnel.englishName'] = 'ceshi'
        editParam_05['overseaPersonnel.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='女')
        editParam_05['overseaPersonnel.certificateType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '旅游证'")   #证件种类
        editParam_05['overseaPersonnel.certificateNo'] = '1100'
        editParam_05['overseaPersonnel.isHaveHouse'] = 'false'
#         editParam_05['overseaPersonnel.currentAddress'] = '现居地址%s'%CommonUtil.createRandomString()  #true:现居地址
        editParam_05['overseaPersonnel.noHouseReason'] = '无住所原因%s'%CommonUtil.createRandomString()  #false:无住所原因

        responseDict = RenKouXinXiIntf.edit_JingWai(JingWaiRenKouDict=editParam_05, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改境外人口失败') 
        
    #检查手机端新增境外人口的详细信息
        param = copy.deepcopy(RenKouXinXiPara.checkJingWaiDict)      
        param['certificateNo'] = editParam_05['overseaPersonnel.certificateNo']         
        ret = RenKouXinXiIntf.check_JingWai(param,overseaPersonnelId=editParam_05['overseaPersonnel.id'] , username=userInit['DftWangGeUser'], password='11111111') 
        self.assertTrue(ret, '查找境外人口失败')        
        
    #检查手机端新增的人口信息是否与pc端同步-check2 
        ret = ShiYouRenKouIntf.check_JingWaipopulation(param_05, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找境外人口失败')                   
        
        pass
    
    def testHuJiPopulationSearch_06(self):
        """搜索户籍人口信息"""
    #新增户籍人口1
        HuJiParam_06 = copy.deepcopy(RenKouXinXiPara.populationObject) 
        HuJiParam_06['tqmobile'] = 'true'
        HuJiParam_06['orgId'] = orgInit['DftWangGeOrgId']
        HuJiParam_06['householdStaff.name'] ='新增户籍人口测试1%s'%CommonUtil.createRandomString() 
        HuJiParam_06['householdStaff.organization.id'] = orgInit['DftWangGeOrgId']
        HuJiParam_06['householdStaff.idCardNo'] = '330000195501040026'   #性别根据身份证来确定，如何获取？
        HuJiParam_06['householdStaff.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='女')
        HuJiParam_06['householdStaff.maritalState.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '未婚'")   #婚姻状况
        HuJiParam_06['householdStaff.schooling.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '博士'")  #文化程度
        HuJiParam_06['householdStaff.politicalBackground.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '中国共产党党员'")  #政治面貌   
        HuJiParam_06['householdStaff.nation.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '汉族'")  #民族
        HuJiParam_06['householdStaff.province'] = '浙江省'  #户籍地址省
        HuJiParam_06['householdStaff.city'] = '杭州市'  #户籍地址市
        HuJiParam_06['householdStaff.district'] = '西湖区'  #户籍地址县
        HuJiParam_06['householdStaff.houseAddress'] = "%s%s%s" % (HuJiParam_06['householdStaff.province'],HuJiParam_06['householdStaff.city'],HuJiParam_06['householdStaff.district'])  #户籍地址:省、市、县
        HuJiParam_06['householdStaff.isHaveHouse'] = 'false'  #有无住所:true/false
#         HuJiParam_06['householdStaff.currentAddress'] = '现居地址%s'%CommonUtil.createRandomString()  #true:现居地址
        HuJiParam_06['householdStaff.noHouseReason'] = '无住所原因%s'%CommonUtil.createRandomString()  #false:无住所原因

    #户籍信息
        HuJiParam_06['householdStaff.accountNumber'] = '01'
        HuJiParam_06['householdStaff.relationShipWithHead.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '本人'")
        HuJiParam_06['householdStaff.residentStatus.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '人户同在'")

        responseDict = RenKouXinXiIntf.add_HuJi(HuJiRenKouDict=HuJiParam_06, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口失败')   
        
    #新增户籍人口2
        newHuJiParam_06 = copy.deepcopy(RenKouXinXiPara.populationObject) 
        newHuJiParam_06['tqmobile'] = 'true'
        newHuJiParam_06['orgId'] = orgInit['DftWangGeOrgId']
        newHuJiParam_06['householdStaff.name'] ='新增户籍人口测试2%s'%CommonUtil.createRandomString() 
        newHuJiParam_06['householdStaff.organization.id'] = orgInit['DftWangGeOrgId']
        newHuJiParam_06['householdStaff.idCardNo'] = '330000195501040226'   #性别根据身份证来确定，如何获取？
        newHuJiParam_06['householdStaff.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='女')
        newHuJiParam_06['householdStaff.maritalState.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '未婚'")   #婚姻状况
        newHuJiParam_06['householdStaff.schooling.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '博士'")  #文化程度
        newHuJiParam_06['householdStaff.politicalBackground.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '中国共产党党员'")  #政治面貌   
        newHuJiParam_06['householdStaff.nation.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '汉族'")  #民族
        newHuJiParam_06['householdStaff.province'] = '浙江省'  #户籍地址省
        newHuJiParam_06['householdStaff.city'] = '杭州市'  #户籍地址市
        newHuJiParam_06['householdStaff.district'] = '西湖区'  #户籍地址县
        newHuJiParam_06['householdStaff.houseAddress'] = "%s%s%s" % (newHuJiParam_06['householdStaff.province'],newHuJiParam_06['householdStaff.city'],newHuJiParam_06['householdStaff.district'])  #户籍地址:省、市、县
        newHuJiParam_06['householdStaff.isHaveHouse'] = 'false'  #有无住所:true/false
#         newHuJiParam_06['householdStaff.currentAddress'] = '现居地址%s'%CommonUtil.createRandomString()  #true:现居地址
        newHuJiParam_06['householdStaff.noHouseReason'] = '无住所原因%s'%CommonUtil.createRandomString()  #false:无住所原因

    #户籍信息
        newHuJiParam_06['householdStaff.accountNumber'] = '01'
        newHuJiParam_06['householdStaff.relationShipWithHead.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '本人'")
        newHuJiParam_06['householdStaff.residentStatus.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '人户同在'")

        responseDict = RenKouXinXiIntf.add_HuJi(HuJiRenKouDict=newHuJiParam_06, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口失败')      
        
    #搜索户籍人口1（存在）
        param = copy.deepcopy(RenKouXinXiPara.searchDict) 
        param['name'] = HuJiParam_06['householdStaff.name']   
        param['idCardNo'] = HuJiParam_06['householdStaff.idCardNo']       
        ret = RenKouXinXiIntf.search_Population(param,populationType='RESIDENT',name=HuJiParam_06['householdStaff.name'], idCardNo='',username=userInit['DftWangGeUser'], password='11111111') 
        self.assertTrue(ret, '搜索户籍人口失败')     
        
    #搜索户籍人口2（不存在）
        param = copy.deepcopy(RenKouXinXiPara.searchDict) 
        param['name'] = newHuJiParam_06['householdStaff.name']   
        param['idCardNo'] = newHuJiParam_06['householdStaff.idCardNo']       
        ret = RenKouXinXiIntf.search_Population(param,populationType='RESIDENT',name=HuJiParam_06['householdStaff.name'], idCardNo='',username=userInit['DftWangGeUser'], password='11111111') 
        self.assertFalse(ret, '不符合搜索条件的户籍人口在列表中依然存在，搜索失败') 
        
        pass

    def testHuJiPopulationService_07(self):
        """户籍人口添加服务记录信息"""
    #新增户籍人口
        HuJiParam_07 = copy.deepcopy(RenKouXinXiPara.populationObject) 
        HuJiParam_07['tqmobile'] = 'true'
        HuJiParam_07['orgId'] = orgInit['DftWangGeOrgId']
        HuJiParam_07['householdStaff.name'] ='户籍人口新增服务记录测试%s'%CommonUtil.createRandomString() 
        HuJiParam_07['householdStaff.organization.id'] = orgInit['DftWangGeOrgId']
        HuJiParam_07['householdStaff.idCardNo'] = '330000195501040027'   #性别根据身份证来确定，如何获取？
        HuJiParam_07['householdStaff.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='女')
        HuJiParam_07['householdStaff.maritalState.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '未婚'")   #婚姻状况
        HuJiParam_07['householdStaff.schooling.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '博士'")  #文化程度
        HuJiParam_07['householdStaff.politicalBackground.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '中国共产党党员'")  #政治面貌   
        HuJiParam_07['householdStaff.nation.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '汉族'")  #民族
        HuJiParam_07['householdStaff.province'] = '浙江省'  #户籍地址省
        HuJiParam_07['householdStaff.city'] = '杭州市'  #户籍地址市
        HuJiParam_07['householdStaff.district'] = '西湖区'  #户籍地址县
        HuJiParam_07['householdStaff.houseAddress'] = "%s%s%s" % (HuJiParam_07['householdStaff.province'],HuJiParam_07['householdStaff.city'],HuJiParam_07['householdStaff.district'])  #户籍地址:省、市、县
        HuJiParam_07['householdStaff.isHaveHouse'] = 'false'  #有无住所:true/false
#         HuJiParam_07['householdStaff.currentAddress'] = '现居地址%s'%CommonUtil.createRandomString()  #true:现居地址
        HuJiParam_07['householdStaff.noHouseReason'] = '无住所原因%s'%CommonUtil.createRandomString()  #false:无住所原因

    #户籍信息
        HuJiParam_07['householdStaff.accountNumber'] = '01'
        HuJiParam_07['householdStaff.relationShipWithHead.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '本人'")
        HuJiParam_07['householdStaff.residentStatus.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '人户同在'")

        responseDict = RenKouXinXiIntf.add_HuJi(HuJiRenKouDict=HuJiParam_07, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口失败') 

    #新增服务成员
        fuWuParam = copy.deepcopy(ShiYouRenKouPara.fuWuRenYuanDict)      
        fuWuParam['serviceTeamMemberBase.org.id'] = orgInit['DftWangGeOrgId']
        fuWuParam['serviceTeamMemberBase.name'] = '服务1%s'%CommonUtil.createRandomString()
        fuWuParam['serviceTeamMemberBase.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别(男、女)', displayName='男')     
        fuWuParam['serviceTeamMemberBase.mobile'] = '13011111112'
        responseDict = ShiYouRenKouIntf.add_FuWuChengYuan(fuWuDict=fuWuParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增成员失败')

    #新增服务记录
        serviceParam_07 = copy.deepcopy(RenKouXinXiPara.serviceRecordObject) 
        serviceParam_07['tqmobile'] = 'true'
        serviceParam_07['serviceRecord.userOrgId'] = orgInit['DftWangGeOrgId']
        serviceParam_07['serviceRecord.serviceJoiners'] = '服务参与者'  #选填
        serviceParam_07['serviceRecord.teamId'] = '0'
        serviceParam_07['serviceRecord.occurDate'] = Time.getCurrentDate()
        serviceParam_07['serviceRecord.serviceObjects'] = "%s-%s-householdStaff" % (CommonIntf.getDbQueryResult(dbCommand = "select t.id from householdstaffs t where t.idcardno='%s' and t.name='%s'" % (HuJiParam_07['householdStaff.idCardNo'],HuJiParam_07['householdStaff.name'])),HuJiParam_07['householdStaff.name'])
        serviceParam_07['serviceRecord.organization.id'] = orgInit['DftWangGeOrgId']
        serviceParam_07['serviceRecord.serviceContent'] = '服务内容%s'%CommonUtil.createRandomString()   #选填
        serviceParam_07['serviceRecord.serviceMembers'] = "%s-%s-0" % (CommonIntf.getDbQueryResult(dbCommand = "select t.id from Serviceteammemberbase t where t.name='%s'" % (fuWuParam['serviceTeamMemberBase.name'])),fuWuParam['serviceTeamMemberBase.name'])
        serviceParam_07['serviceRecord.occurPlace'] = '服务地点%s'%CommonUtil.createRandomString() 
        responseDict = RenKouXinXiIntf.add_serviceRecord(serviceParam_07, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口的服务记录失败')      
           
    #在服务记录列表中检查服务记录是否新增成功    
        param_07 = copy.deepcopy(RenKouXinXiPara.checkServiceRecordDict)      
        param_07['serviceMembers'] = fuWuParam['serviceTeamMemberBase.name']
        param_07['serviceContent'] = serviceParam_07['serviceRecord.serviceContent']
        ret = RenKouXinXiIntf.check_serviceRecord(param_07,objectIds=CommonIntf.getDbQueryResult(dbCommand = "select t.id from householdstaffs t where t.idcardno='%s' and t.name='%s'" % (HuJiParam_07['householdStaff.idCardNo'],HuJiParam_07['householdStaff.name'])), populationType='householdStaff',username=userInit['DftWangGeUser'], password='11111111') 
        self.assertTrue(ret, '查找户籍人口中的服务记录信息失败')        
 
    #修改服务记录
        editParam_07 = copy.deepcopy(RenKouXinXiPara.serviceRecordObject) 
        editParam_07['serviceRecord.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from serviceRecords t where t.occurPlace='%s' and t.serviceObjects='%s'" % (serviceParam_07['serviceRecord.occurPlace'],HuJiParam_07['householdStaff.name']))
        editParam_07['tqmobile'] = 'true'
        editParam_07['serviceRecord.userOrgId'] = orgInit['DftWangGeOrgId']
        editParam_07['serviceRecord.serviceJoiners'] = '修改服务参与者'  #选填
        editParam_07['serviceRecord.teamId'] = '0'
        editParam_07['serviceRecord.occurDate'] = Time.getCurrentDate()
        editParam_07['serviceRecord.serviceObjects'] = "%s-%s-householdStaff" % (CommonIntf.getDbQueryResult(dbCommand = "select t.id from householdstaffs t where t.idcardno='%s' and t.name='%s'" % (HuJiParam_07['householdStaff.idCardNo'],HuJiParam_07['householdStaff.name'])),HuJiParam_07['householdStaff.name'])
        editParam_07['serviceRecord.organization.id'] = orgInit['DftWangGeOrgId']
        editParam_07['serviceRecord.serviceContent'] = '修改服务内容%s'%CommonUtil.createRandomString()   #选填
        editParam_07['serviceRecord.serviceMembers'] = "%s-%s-0" % (CommonIntf.getDbQueryResult(dbCommand = "select t.id from Serviceteammemberbase t where t.name='%s'" % (fuWuParam['serviceTeamMemberBase.name'])),fuWuParam['serviceTeamMemberBase.name'])
        editParam_07['serviceRecord.occurPlace'] = '修改服务地点%s'%CommonUtil.createRandomString() 
        responseDict = RenKouXinXiIntf.edit_serviceRecord(editParam_07, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改户籍人口的服务记录信息失败')   
        
    #检查手机端户籍人口下新增服务记录的详细信息
        param = copy.deepcopy(RenKouXinXiPara.checkServiceRecordDict)   
        param['serviceMembers'] = fuWuParam['serviceTeamMemberBase.name']   
        param['serviceContent'] = editParam_07['serviceRecord.serviceContent']        
        ret = RenKouXinXiIntf.check_Record(param,serviceRecordId=CommonIntf.getDbQueryResult(dbCommand = "select t.id from serviceRecords t where t.occurPlace='%s' and t.serviceObjects='%s'" % (editParam_07['serviceRecord.occurPlace'] ,HuJiParam_07['householdStaff.name'])) , username=userInit['DftWangGeUser'], password='11111111') 
        self.assertTrue(ret, '查找户籍人口服务记录的详细信息失败')  
        
        XiaQuGuanLiIntf.xiaQuGuanLiMemberDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')      
#         
#     #检查手机端户籍人口下新增的服务记录是否与pc端同步-check2 
#         param_07 = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
#         param_07['occurDate'] = editParam_07['serviceRecord.occurDate']      
#         param_07['occurPlace'] = editParam_07['serviceRecord.occurPlace']
#         ret = ShiYouRenKouIntf.check_serviceRecord(param_07, objectIds=CommonIntf.getDbQueryResult(dbCommand = "select t.id from serviceRecords t where t.occurPlace='%s' and t.serviceObjects='%s'" % (serviceParam_07['serviceRecord.occurPlace'],HuJiParam_07['householdStaff.name'])),username=userInit['DftWangGeUser'], password='11111111')         
#         self.assertTrue(ret, '查找服务事件失败')
#         XiaQuGuanLiIntf.xiaQuGuanLiMemberDelAll(username=userInit['DftWangGeUser'], password='11111111')
        
        pass               

    def testHuJiPopulationServiceDelete_08(self):
        """户籍人口删除服务记录信息"""
    #新增户籍人口
        HuJiParam_08 = copy.deepcopy(RenKouXinXiPara.populationObject) 
        HuJiParam_08['tqmobile'] = 'true'
        HuJiParam_08['orgId'] = orgInit['DftWangGeOrgId']
        HuJiParam_08['householdStaff.name'] ='户籍人口新增服务记录搜索测试%s'%CommonUtil.createRandomString() 
        HuJiParam_08['householdStaff.organization.id'] = orgInit['DftWangGeOrgId']
        HuJiParam_08['householdStaff.idCardNo'] = '330000195501040028'   #性别根据身份证来确定，如何获取？
        HuJiParam_08['householdStaff.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='女')
        HuJiParam_08['householdStaff.maritalState.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '未婚'")   #婚姻状况
        HuJiParam_08['householdStaff.schooling.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '博士'")  #文化程度
        HuJiParam_08['householdStaff.politicalBackground.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '中国共产党党员'")  #政治面貌   
        HuJiParam_08['householdStaff.nation.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '汉族'")  #民族
        HuJiParam_08['householdStaff.province'] = '浙江省'  #户籍地址省
        HuJiParam_08['householdStaff.city'] = '杭州市'  #户籍地址市
        HuJiParam_08['householdStaff.district'] = '西湖区'  #户籍地址县
        HuJiParam_08['householdStaff.houseAddress'] = "%s%s%s" % (HuJiParam_08['householdStaff.province'],HuJiParam_08['householdStaff.city'],HuJiParam_08['householdStaff.district'])  #户籍地址:省、市、县
        HuJiParam_08['householdStaff.isHaveHouse'] = 'false'  #有无住所:true/false
#         HuJiParam_08['householdStaff.currentAddress'] = '现居地址%s'%CommonUtil.createRandomString()  #true:现居地址
        HuJiParam_08['householdStaff.noHouseReason'] = '无住所原因%s'%CommonUtil.createRandomString()  #false:无住所原因

    #户籍信息
        HuJiParam_08['householdStaff.accountNumber'] = '01'
        HuJiParam_08['householdStaff.relationShipWithHead.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '本人'")
        HuJiParam_08['householdStaff.residentStatus.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '人户同在'")

        responseDict = RenKouXinXiIntf.add_HuJi(HuJiRenKouDict=HuJiParam_08, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口失败') 

    #新增服务成员
        fuWuParam = copy.deepcopy(ShiYouRenKouPara.fuWuRenYuanDict)      
        fuWuParam['serviceTeamMemberBase.org.id'] = orgInit['DftWangGeOrgId']
        fuWuParam['serviceTeamMemberBase.name'] = '服务1%s'%CommonUtil.createRandomString()
        fuWuParam['serviceTeamMemberBase.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别(男、女)', displayName='男')     
        fuWuParam['serviceTeamMemberBase.mobile'] = '13000000001'
        responseDict = ShiYouRenKouIntf.add_FuWuChengYuan(fuWuDict=fuWuParam, username=userInit['DftWangGeUser'], password='11111111')
#         self.assertTrue(responseDict.result, '新增成员失败') 

    #新增服务记录1
        serviceParam_08 = copy.deepcopy(RenKouXinXiPara.serviceRecordObject) 
        serviceParam_08['tqmobile'] = 'true'
        serviceParam_08['serviceRecord.userOrgId'] = orgInit['DftWangGeOrgId']
        serviceParam_08['serviceRecord.serviceJoiners'] = '服务参与者1'  #选填
        serviceParam_08['serviceRecord.teamId'] = '0'
        serviceParam_08['serviceRecord.occurDate'] = Time.getCurrentDate()
        serviceParam_08['serviceRecord.serviceObjects'] = "%s-%s-householdStaff" % (CommonIntf.getDbQueryResult(dbCommand = "select t.id from householdstaffs t where t.idcardno='%s' and t.name='%s'" % (HuJiParam_08['householdStaff.idCardNo'],HuJiParam_08['householdStaff.name'])),HuJiParam_08['householdStaff.name'])
        serviceParam_08['serviceRecord.organization.id'] = orgInit['DftWangGeOrgId']
        serviceParam_08['serviceRecord.serviceContent'] = '服务内容1%s'%CommonUtil.createRandomString()   #选填
        serviceParam_08['serviceRecord.serviceMembers'] = "%s-%s-0" % (CommonIntf.getDbQueryResult(dbCommand = "select t.id from Serviceteammemberbase t where t.name='%s'" % (fuWuParam['serviceTeamMemberBase.name'])),fuWuParam['serviceTeamMemberBase.name'])
        serviceParam_08['serviceRecord.occurPlace'] = '服务地点1%s'%CommonUtil.createRandomString() 
        responseDict = RenKouXinXiIntf.add_serviceRecord(serviceParam_08, username=userInit['DftWangGeUser'], password='11111111')
#         self.assertTrue(responseDict.result, '新增户籍人口的服务记录失败')      
        
    #删除服务记录
        deleteParam = copy.deepcopy(RenKouXinXiPara.deleteServiceRecordDict)      
        deleteParam['recordIds'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from serviceRecords t where t.occurPlace='%s' and t.serviceObjects='%s'" % (serviceParam_08['serviceRecord.occurPlace'],HuJiParam_08['householdStaff.name']))
        ret = RenKouXinXiIntf.delete_serviceRecord(deleteParam,username=userInit['DftWangGeUser'], password='11111111') 
        self.assertTrue(ret, '删除户籍人口中的服务记录信息失败') 

    #在服务记录列表中搜索指定服务记录
        param = copy.deepcopy(RenKouXinXiPara.checkServiceRecordDict)      
        param['serviceMembers'] = fuWuParam['serviceTeamMemberBase.name']
        param['serviceObjects'] = HuJiParam_08['householdStaff.name']
        ret = RenKouXinXiIntf.check_serviceRecord(param,objectIds=CommonIntf.getDbQueryResult(dbCommand = "select t.id from householdstaffs t where t.idcardno='%s' and t.name='%s'" % (HuJiParam_08['householdStaff.idCardNo'],HuJiParam_08['householdStaff.name'])), populationType='householdStaff',username=userInit['DftWangGeUser'], password='11111111') 
        self.assertFalse(ret, '查找户籍人口中的服务记录信息失败')    
        XiaQuGuanLiIntf.xiaQuGuanLiMemberDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        pass


    def testXingShiPopulation_09(self):
        """新增、修改刑释人员信息"""
    #新增刑释人员
        XingShiParam = copy.deepcopy(RenKouXinXiPara.teShuRenQunObject) 
        XingShiParam['tqmobile'] = 'true'
        XingShiParam['orgId'] = orgInit['DftWangGeOrgId']
        XingShiParam['population.actualPopulationType'] = 'householdStaff'
        XingShiParam['population.name'] ='刑释人员测试%s'%CommonUtil.createRandomString() 
        XingShiParam['population.organization.id'] = orgInit['DftWangGeOrgId']
        XingShiParam['population.idCardNo'] = '330000195501040029'   #性别根据身份证来确定，如何获取？
        XingShiParam['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='女')
        XingShiParam['population.maritalState.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '未婚'")   #婚姻状况
        XingShiParam['population.schooling.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '博士'")  #文化程度
        XingShiParam['population.politicalBackground.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '中国共产党党员'")  #政治面貌   
        XingShiParam['population.nation.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '汉族'")  #民族
        XingShiParam['population.province'] = '浙江省'  #户籍地址省
        XingShiParam['population.city'] = '杭州市'  #户籍地址市
        XingShiParam['population.district'] = '西湖区'  #户籍地址县
        XingShiParam['population.houseAddress'] = "%s%s%s" % (XingShiParam['population.province'],XingShiParam['population.city'],XingShiParam['population.district'])  #户籍地址:省、市、县
        XingShiParam['population.isHaveHouse'] = 'false'  #有无住所:true/false
#         XingShiParam['population.currentAddress'] = '现居地址%s'%CommonUtil.createRandomString()  #true:现居地址
        XingShiParam['population.noHouseReason'] = '无住所原因%s'%CommonUtil.createRandomString()  #false:无住所原因
 
        XingShiParam['population.positiveInfoType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '刑释人员'")   #人员类型：刑释人员、解教人员
        XingShiParam['population.caseReason'] = '原罪名'
        XingShiParam['population.imprisonmentDate'] = '3周'  #原判刑期
        XingShiParam['population.laborEduAddress'] = '劳教场所'
        XingShiParam['population.releaseOrBackDate'] = Time.getCurrentDate()
        
        #验证刑释解教人员中的人员类型必填
        XingShiParam['population.positiveInfoType.id'] =''
        responseDict = RenKouXinXiIntf.add_XingShiRenYuan(XingShiParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertFalse(responseDict.result, '新增刑释人员时人员类型必填项为空仍能新增，验证失败') 
        Log.LogOutput(LogLevel.DEBUG, "新增刑释人员时人员类型必填项不能为空")
        XingShiParam['population.positiveInfoType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '刑释人员'")   #人员类型：刑释人员、解教人员
        #验证刑释解教人员中的原罪名必填
        XingShiParam['population.caseReason'] = ''
        responseDict = RenKouXinXiIntf.add_XingShiRenYuan(XingShiParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertFalse(responseDict.result, '新增刑释人员时原罪名必填项为空仍能新增，验证失败') 
        Log.LogOutput(LogLevel.DEBUG, "新增刑释人员时原罪名必填项不能为空")        
        XingShiParam['population.caseReason'] = '原罪名'
        #验证刑释解教人员中的原判刑期必填
        XingShiParam['population.imprisonmentDate'] =''
        responseDict = RenKouXinXiIntf.add_XingShiRenYuan(XingShiParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertFalse(responseDict.result, '新增刑释人员时原判刑期必填项为空仍能新增，验证失败') 
        Log.LogOutput(LogLevel.DEBUG, "新增刑释人员时原判刑期必填项不能为空")         
        XingShiParam['population.imprisonmentDate'] = '3周'  #原判刑期
        #验证刑释解教人员中的劳教场所必填
        XingShiParam['population.laborEduAddress'] =  ''
        responseDict = RenKouXinXiIntf.add_XingShiRenYuan(XingShiParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertFalse(responseDict.result, '新增刑释人员时劳教场所必填项为空仍能新增，验证失败') 
        Log.LogOutput(LogLevel.DEBUG, "新增刑释人员时劳教场所必填项不能为空")        
        XingShiParam['population.laborEduAddress'] = '劳教场所'
        #验证刑释解教人员中的解教（刑释）日期必填
        XingShiParam['population.releaseOrBackDate'] = ''
        responseDict = RenKouXinXiIntf.add_XingShiRenYuan(XingShiParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertFalse(responseDict.result, '新增刑释人员时解教（刑释）日期必填项为空仍能新增，验证失败') 
        Log.LogOutput(LogLevel.DEBUG, "新增刑释人员时解教（刑释）日期必填项不能为空")          
        XingShiParam['population.releaseOrBackDate'] = Time.getCurrentDate()
         
        XingShiParam['population.attentionExtent.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '严管'")   #管控等级：严管、普管、二级宽管、一级宽管
        XingShiParam['population.criminalBehavior'] = '犯罪行为'
        XingShiParam['population.agoProfession.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '工业'")   #原职业：工业、农林牧渔、服务业、危险品业、娱乐业、其他、烟花爆竹、非煤矿山、、、、、、
        XingShiParam['population.isRepeat'] = '0' #是否累犯：0-否（默认）、1-是
        XingShiParam['population.isCrime'] = 'false'  #本年度是否重犯：false-否（默认）、true-是
#         XingShiParam['population.crimeDate'] = ''  #重犯日期
        XingShiParam['population.resettlementDate'] = Time.getCurrentDate()
        XingShiParam['population.noResettlementReason'] = '未安置原因'

        responseDict = RenKouXinXiIntf.add_XingShiRenYuan(XingShiParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增刑释人员失败') 
        
    #检查手机端新增的刑释人员信息
        param = copy.deepcopy(RenKouXinXiPara.checkPopulationDict)      
        param['idCardNo'] = XingShiParam['population.idCardNo']     
        ret = RenKouXinXiIntf.check_Population(param,orgId=orgInit['DftWangGeOrgId'],populationType='POSITIVEINFO', username=userInit['DftWangGeUser'], password='11111111') 
        self.assertTrue(ret, '查找刑释人员失败')      
        
    #修改刑释人员
        editParam = copy.deepcopy(RenKouXinXiPara.teShuRenQunObject) 
        editParam['population.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from positiveinfos t where t.idcardno='%s'" % XingShiParam['population.idCardNo'])
        editParam['tqmobile'] = 'true'
        editParam['orgId'] = orgInit['DftWangGeOrgId']
        editParam['population.actualPopulationType'] = 'householdStaff'
        editParam['population.attentionPopulationType'] = 'positiveInfo'
        editParam['population.name'] ='修改测试%s'%CommonUtil.createRandomString() 
        editParam['population.organization.id'] = orgInit['DftWangGeOrgId']
        editParam['population.idCardNo'] = XingShiParam['population.idCardNo']
        editParam['population.gender.id'] = XingShiParam['population.gender.id']
        editParam['population.maritalState.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '未婚'")   #婚姻状况
        editParam['population.schooling.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '博士'")  #文化程度
        editParam['population.politicalBackground.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '中国共产党党员'")  #政治面貌   
        editParam['population.nation.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '汉族'")  #民族
        editParam['population.province'] = '浙江省'  #户籍地址省
        editParam['population.city'] = '杭州市'  #户籍地址市
        editParam['population.district'] = '西湖区'  #户籍地址县
        editParam['population.houseAddress'] = "%s%s%s" % (editParam['population.province'],editParam['population.city'],editParam['population.district'])  #户籍地址:省、市、县
        editParam['population.isHaveHouse'] = 'false'  #有无住所:true/false
#         editParam['population.currentAddress'] = '现居地址%s'%CommonUtil.createRandomString()  #true:现居地址
        editParam['population.noHouseReason'] = '无住所原因%s'%CommonUtil.createRandomString()  #false:无住所原因

        editParam['population.positiveInfoType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '刑释人员'")   #人员类型：刑释人员、解教人员
        editParam['population.caseReason'] = '修改原罪名'
        editParam['population.imprisonmentDate'] = '3周'  #原判刑期
        editParam['population.laborEduAddress'] = '修改劳教场所'
        editParam['population.releaseOrBackDate'] = Time.getCurrentDate()   
        responseDict = RenKouXinXiIntf.edit_XingShiRenYuan(editParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改刑释人员失败') 
        
    #检查手机端新增刑释人员的详细信息
        param = copy.deepcopy(RenKouXinXiPara.checkPopulationDict)      
        param['idCardNo'] = editParam['population.idCardNo']     
        ret = RenKouXinXiIntf.check_XingShi(param,populationId=editParam['population.id'], username=userInit['DftWangGeUser'], password='11111111') 
        self.assertTrue(ret, '查找刑释人员失败') 
        
    #检查手机端新增的刑释人员信息是否与pc端同步
        ret_01 = ShiYouRenKouIntf.check_xingManShiFang(param, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret_01, '查找刑满释放人员失败') 
        
#     #检查对应户籍人口下是否存在该新增刑释人员信息   -存在bug
#         ret_02 = RenKouXinXiIntf.check_Population(param,orgId=orgInit['DftWangGeOrgId'],populationType='RESIDENT', username=userInit['DftWangGeUser'], password='11111111') 
#         self.assertTrue(ret_02, '查找户籍人口失败')   
#  
#     #检查手机端新增的刑释人员信息是否同步到pc端的户籍人口中
#         ret_03 = ShiYouRenKouIntf.check_HuJiPopulation(param, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
#         self.assertTrue(ret_03, '查找户籍人口失败')    
        
        pass

    def testJiaoZhengPopulation_10(self):
        """新增、修改矫正人员信息"""
    #新增矫正人员
        jiaoZhengParam= copy.deepcopy(RenKouXinXiPara.teShuRenQunObject) 
        jiaoZhengParam['tqmobile'] = 'true'
        jiaoZhengParam['orgId'] = orgInit['DftWangGeOrgId']
        jiaoZhengParam['population.actualPopulationType'] = 'householdStaff'
        jiaoZhengParam['population.name'] ='矫正人员测试%s'%CommonUtil.createRandomString() 
        jiaoZhengParam['population.organization.id'] = orgInit['DftWangGeOrgId']
        jiaoZhengParam['population.idCardNo'] = '330000195501040030'   
        jiaoZhengParam['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='女')
        jiaoZhengParam['population.maritalState.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '未婚'")   #婚姻状况
        jiaoZhengParam['population.schooling.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '博士'")  #文化程度
        jiaoZhengParam['population.politicalBackground.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '中国共产党党员'")  #政治面貌   
        jiaoZhengParam['population.nation.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '汉族'")  #民族
        jiaoZhengParam['population.province'] = '浙江省'  #户籍地址省
        jiaoZhengParam['population.city'] = '杭州市'  #户籍地址市
        jiaoZhengParam['population.district'] = '西湖区'  #户籍地址县
        jiaoZhengParam['population.houseAddress'] = "%s%s%s" % (jiaoZhengParam['population.province'],jiaoZhengParam['population.city'],jiaoZhengParam['population.district'])  #户籍地址:省、市、县
        jiaoZhengParam['population.isHaveHouse'] = 'false'  #有无住所:true/false
#         jiaoZhengParam['population.currentAddress'] = '现居地址%s'%CommonUtil.createRandomString()  #true:现居地址
        jiaoZhengParam['population.noHouseReason'] = '无住所原因%s'%CommonUtil.createRandomString()  #false:无住所原因

        jiaoZhengParam['population.accusation'] = '罪名'
        jiaoZhengParam['population.executeType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '监外执行罪犯'")   #刑法执行类别：监外执行罪犯、管制人员、缓刑人员、假释人员、其他
        jiaoZhengParam['population.rectifyStartDate'] = Time.getCurrentDate()
        jiaoZhengParam['population.rectifyEndDate'] = '2020-1-1'

        #验证矫正人员中的社区矫正日期必填
        jiaoZhengParam['population.rectifyStartDate'] = ''
        responseDict = RenKouXinXiIntf.add_jiaoZhengRenYuan(jiaoZhengParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertFalse(responseDict.result, '新增矫正人员时社区矫正日期必填项为空仍能新增，验证失败') 
        Log.LogOutput(LogLevel.DEBUG, "新增矫正人员时社区矫正日期必填项不能为空") 
        jiaoZhengParam['population.rectifyStartDate'] = Time.getCurrentDate()
        #验证矫正人员中的社区矫正日期至（即截止日期）必填
        jiaoZhengParam['population.rectifyEndDate'] = ''
        responseDict = RenKouXinXiIntf.add_jiaoZhengRenYuan(jiaoZhengParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertFalse(responseDict.result, '新增矫正人员时社区矫正日期至（即截止日期）必填项为空仍能新增，验证失败') 
        Log.LogOutput(LogLevel.DEBUG, "新增矫正人员时社区矫正日期至（即截止日期）必填项不能为空") 
        jiaoZhengParam['population.rectifyEndDate'] = '2020-1-1'
        
        jiaoZhengParam['population.attentionExtent.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '严管'")   #管控等级：严管、普管、二级宽管、一级宽管
        jiaoZhengParam['population.penaltyTerm'] = '原判刑期'
        jiaoZhengParam['population.recentSituation'] = '近况描述'
        
        responseDict = RenKouXinXiIntf.add_jiaoZhengRenYuan(jiaoZhengParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增矫正人员失败') 
        
    #检查手机端新增的矫正人员信息
        param = copy.deepcopy(RenKouXinXiPara.checkPopulationDict)      
        param['idCardNo'] = jiaoZhengParam['population.idCardNo']     
        ret = RenKouXinXiIntf.check_Population(param,orgId=orgInit['DftWangGeOrgId'],populationType='RECTIFICATIVEPERSON', username=userInit['DftWangGeUser'], password='11111111') 
        self.assertTrue(ret, '查找矫正人员失败')      
        
    #修改矫正人员
        editParam = copy.deepcopy(RenKouXinXiPara.teShuRenQunObject) 
        editParam['population.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rectificativePersons  t where t.idcardno='%s'" % jiaoZhengParam['population.idCardNo'])
        editParam['tqmobile'] = 'true'
        editParam['orgId'] = orgInit['DftWangGeOrgId']
        editParam['population.attentionPopulationType'] = 'rectificativePerson'
        editParam['population.name'] ='修改测试%s'%CommonUtil.createRandomString() 
        editParam['population.organization.id'] = orgInit['DftWangGeOrgId']
        editParam['population.idCardNo'] = jiaoZhengParam['population.idCardNo']
        editParam['population.gender.id'] = jiaoZhengParam['population.gender.id']
        editParam['population.actualPopulationType'] = 'householdStaff'
        
        editParam['population.maritalState.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '未婚'")   #婚姻状况
        editParam['population.schooling.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '博士'")  #文化程度
        editParam['population.politicalBackground.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '中国共产党党员'")  #政治面貌   
        editParam['population.nation.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '汉族'")  #民族
        editParam['population.province'] = '浙江省'  #户籍地址省
        editParam['population.city'] = '杭州市'  #户籍地址市
        editParam['population.district'] = '西湖区'  #户籍地址县
        editParam['population.houseAddress'] = "%s%s%s" % (editParam['population.province'],editParam['population.city'],editParam['population.district'])  #户籍地址:省、市、县
        editParam['population.isHaveHouse'] = 'false'  #有无住所:true/false
#         editParam['population.currentAddress'] = '现居地址%s'%CommonUtil.createRandomString()  #true:现居地址
        editParam['population.noHouseReason'] = '无住所原因%s'%CommonUtil.createRandomString()  #false:无住所原因

        editParam['population.accusation'] = '罪名'
        editParam['population.executeType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '监外执行罪犯'")   #刑法执行类别：监外执行罪犯、管制人员、缓刑人员、假释人员、其他
        editParam['population.rectifyStartDate'] = Time.getCurrentDate()
        editParam['population.rectifyEndDate'] = '2020-1-1'   
        responseDict = RenKouXinXiIntf.edit_jiaoZhengRenYuan(editParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改矫正人员失败') 
         
    #检查手机端新增矫正人员的详细信息
        param = copy.deepcopy(RenKouXinXiPara.checkPopulationDict)      
        param['idCardNo'] = editParam['population.idCardNo']     
        ret = RenKouXinXiIntf.check_jiaoZheng(param,populationId=editParam['population.id'], username=userInit['DftWangGeUser'], password='11111111') 
        self.assertTrue(ret, '查找矫正人员失败') 
        
    #检查手机端新增的矫正人员信息是否与pc端同步
        ret_01 = ShiYouRenKouIntf.check_sheQuJiaoZheng(param, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret_01, '查找社区矫正人员失败')  
         
#     #检查对应户籍人口下是否存在该新增矫正人员信息  -存在bug
#         ret_02 = RenKouXinXiIntf.check_Population(param,orgId=orgInit['DftWangGeOrgId'],populationType='RESIDENT', username=userInit['DftWangGeUser'], password='11111111') 
#         self.assertTrue(ret_02, '查找户籍人口失败')   
#          
#     #检查手机端新增的矫正人员信息是否同步到pc端的户籍人口中
#         ret_03 = ShiYouRenKouIntf.check_HuJiPopulation(param, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
#         self.assertTrue(ret_03, '查找户籍人口失败')    
        
        pass

    def testJingShengPopulation_11(self):
        """新增、修改精神病人员信息"""
    #新增精神病人员
        jingShenParam = copy.deepcopy(RenKouXinXiPara.teShuRenQunObject) 
        jingShenParam['tqmobile'] = 'true'
        jingShenParam['orgId'] = orgInit['DftWangGeOrgId']
        jingShenParam['population.actualPopulationType'] = 'householdStaff'
        jingShenParam['population.name'] ='精神病人员测试%s'%CommonUtil.createRandomString() 
        jingShenParam['population.organization.id'] = orgInit['DftWangGeOrgId']
        jingShenParam['population.idCardNo'] = '330000195501040031'   #性别根据身份证来确定，如何获取？
        jingShenParam['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='女')
        jingShenParam['population.maritalState.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '未婚'")   #婚姻状况
        jingShenParam['population.schooling.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '博士'")  #文化程度
        jingShenParam['population.politicalBackground.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '中国共产党党员'")  #政治面貌   
        jingShenParam['population.nation.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '汉族'")  #民族
        jingShenParam['population.province'] = '浙江省'  #户籍地址省
        jingShenParam['population.city'] = '杭州市'  #户籍地址市
        jingShenParam['population.district'] = '西湖区'  #户籍地址县
        jingShenParam['population.houseAddress'] = "%s%s%s" % (jingShenParam['population.province'],jingShenParam['population.city'],jingShenParam['population.district'])  #户籍地址:省、市、县
        jingShenParam['population.isHaveHouse'] = 'false'  #有无住所:true/false
#         jingShenParam['population.currentAddress'] = '现居地址%s'%CommonUtil.createRandomString()  #true:现居地址
        jingShenParam['population.noHouseReason'] = '无住所原因%s'%CommonUtil.createRandomString()  #false:无住所原因

        jingShenParam['population.dangerLevel.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '高'")   #危险程度：高、中、低

        #验证精神病人员中的危险程度必填
        jingShenParam['population.dangerLevel.id'] = ''
        responseDict = RenKouXinXiIntf.add_jingShenBingRenYuan(jingShenParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertFalse(responseDict.result, '新增精神病人员时危险程度必填项为空仍能新增，验证失败') 
        Log.LogOutput(LogLevel.DEBUG, "新增精神病人员时危险程度必填项不能为空") 
        jingShenParam['population.dangerLevel.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '高'")   #危险程度：高、中、低
        
        jingShenParam['population.psychosisName'] = '患病名称'
        jingShenParam['population.treat'] = 'true'  #是否接受过治疗：false-否（默认） 、true-是
        jingShenParam['population.cureDepartment'] = '康复机构'  #前提：接受过治疗
        
        responseDict = RenKouXinXiIntf.add_jingShenBingRenYuan(jingShenParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增精神病人员失败') 
        
    #检查手机端新增的精神病人员信息
        param = copy.deepcopy(RenKouXinXiPara.checkPopulationDict)      
        param['idCardNo'] = jingShenParam['population.idCardNo']     
        ret = RenKouXinXiIntf.check_Population(param,orgId=orgInit['DftWangGeOrgId'],populationType='MENTALPATIENT', username=userInit['DftWangGeUser'], password='11111111') 
        self.assertTrue(ret, '查找矫正人员失败')      
        
    #修改精神病人员
        editParam = copy.deepcopy(RenKouXinXiPara.teShuRenQunObject) 
        editParam['population.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from MENTALPATIENTS  t where t.idcardno='%s'" % jingShenParam['population.idCardNo'])
        editParam['tqmobile'] = 'true'
        editParam['orgId'] = orgInit['DftWangGeOrgId']
        editParam['population.actualPopulationType'] = 'householdStaff'
        editParam['population.attentionPopulationType'] = 'mentalPatient'
        editParam['population.name'] ='修改测试%s'%CommonUtil.createRandomString() 
        editParam['population.organization.id'] = orgInit['DftWangGeOrgId']
        editParam['population.idCardNo'] = jingShenParam['population.idCardNo']
        editParam['population.gender.id'] = jingShenParam['population.gender.id']
        editParam['population.maritalState.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '未婚'")   #婚姻状况
        editParam['population.schooling.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '博士'")  #文化程度
        editParam['population.politicalBackground.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '中国共产党党员'")  #政治面貌   
        editParam['population.nation.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '汉族'")  #民族
        editParam['population.province'] = '浙江省'  #户籍地址省
        editParam['population.city'] = '杭州市'  #户籍地址市
        editParam['population.district'] = '西湖区'  #户籍地址县
        editParam['population.houseAddress'] = "%s%s%s" % (editParam['population.province'],editParam['population.city'],editParam['population.district'])  #户籍地址:省、市、县
        editParam['population.isHaveHouse'] = 'false'  #有无住所:true/false
#         editParam['population.currentAddress'] = '现居地址%s'%CommonUtil.createRandomString()  #true:现居地址
        editParam['population.noHouseReason'] = '无住所原因%s'%CommonUtil.createRandomString()  #false:无住所原因

        editParam['population.dangerLevel.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '高'")   #危险程度：高、中、低
        
        responseDict = RenKouXinXiIntf.edit_jingShenBingRenYuan(editParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改精神病人员失败') 
         
    #检查手机端新增精神病人员的详细信息
        param = copy.deepcopy(RenKouXinXiPara.checkPopulationDict)      
        param['idCardNo'] = editParam['population.idCardNo']     
        ret = RenKouXinXiIntf.check_jingSheng(param,populationId=editParam['population.id'], username=userInit['DftWangGeUser'], password='11111111') 
        self.assertTrue(ret, '查找精神病人员失败') 
        
    #检查手机端新增的精神病人员信息是否与pc端同步
        ret_01 = ShiYouRenKouIntf.check_jingShengBingRenYuan(param, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret_01, '查找精神病人员失败')  
         
#     #检查对应户籍人口下是否存在该新增精神病人员信息  -存在bug
#         ret_02 = RenKouXinXiIntf.check_Population(param,orgId=orgInit['DftWangGeOrgId'],populationType='RESIDENT', username=userInit['DftWangGeUser'], password='11111111') 
#         self.assertTrue(ret_02, '查找户籍人口失败')   
#          
#     #检查手机端新增的精神病人员信息是否同步到pc端的户籍人口中
#         ret_03 = ShiYouRenKouIntf.check_HuJiPopulation(param, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
#         self.assertTrue(ret_03, '查找户籍人口失败')    
        
        pass

    def testXiDuPopulation_12(self):
        """新增、修改吸毒人员信息"""
    #新增吸毒人员
        xiDuParam = copy.deepcopy(RenKouXinXiPara.teShuRenQunObject) 
        xiDuParam['tqmobile'] = 'true'
        xiDuParam['orgId'] = orgInit['DftWangGeOrgId']
        xiDuParam['population.actualPopulationType'] = 'householdStaff'
        xiDuParam['population.name'] ='吸毒人员测试%s'%CommonUtil.createRandomString() 
        xiDuParam['population.organization.id'] = orgInit['DftWangGeOrgId']
        xiDuParam['population.idCardNo'] = '330000195501040032'   #性别根据身份证来确定，如何获取？
        xiDuParam['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='女')
        xiDuParam['population.maritalState.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '未婚'")   #婚姻状况
        xiDuParam['population.schooling.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '博士'")  #文化程度
        xiDuParam['population.politicalBackground.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '中国共产党党员'")  #政治面貌   
        xiDuParam['population.nation.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '汉族'")  #民族
        xiDuParam['population.province'] = '浙江省'  #户籍地址省
        xiDuParam['population.city'] = '杭州市'  #户籍地址市
        xiDuParam['population.district'] = '西湖区'  #户籍地址县
        xiDuParam['population.houseAddress'] = "%s%s%s" % (xiDuParam['population.province'],xiDuParam['population.city'],xiDuParam['population.district'])  #户籍地址:省、市、县
        xiDuParam['population.isHaveHouse'] = 'false'  #有无住所:true/false
#         xiDuParam['population.currentAddress'] = '现居地址%s'%CommonUtil.createRandomString()  #true:现居地址
        xiDuParam['population.noHouseReason'] = '无住所原因%s'%CommonUtil.createRandomString()  #false:无住所原因

        xiDuParam['population.detoxicateCase.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '强制戒毒'")   #戒毒情况：强制戒毒、劳教戒毒、期限戒毒、自愿戒毒、社区戒毒、其他、社区康复

        #验证吸毒人员中的戒毒情况必填
        xiDuParam['population.detoxicateCase.id'] = ''
        responseDict = RenKouXinXiIntf.add_xiDuRenYuan(xiDuParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertFalse(responseDict.result, '新增吸毒人员时戒毒情况必填项为空仍能新增，验证失败') 
        Log.LogOutput(LogLevel.DEBUG, "新增吸毒人员时戒毒情况必填项不能为空")         
        xiDuParam['population.detoxicateCase.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '强制戒毒'")   #戒毒情况：强制戒毒、劳教戒毒、期限戒毒、自愿戒毒、社区戒毒、其他、社区康复        

        xiDuParam['population.attentionExtent.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '一般'")   #关注程度：一般、中等、严重
        xiDuParam['population.detoxicateCondition.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '在吸'")   #吸毒状态：在吸、停吸
        xiDuParam['population.drugSource.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '其他'")   #毒品来源：黑市购买、亲朋提供、偷窃、医生处方、其他
        xiDuParam['population.drugReason.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '一般'")   #关注程度：一般、中等、严重
        xiDuParam['population.ferretOutDate'] = Time.getCurrentDate()
        xiDuParam['population.drugFristDate'] = '2015-1-1' #首吸时间>查获时间 -待验证
        xiDuParam['population.controlActuality'] = '管控现状'  
        xiDuParam['population.drugType'] = '滥用毒品种类' 
        xiDuParam['population.adanon'] = 'false'  #是否服美沙酮戒毒：false-否（默认） true-是
        
        responseDict = RenKouXinXiIntf.add_xiDuRenYuan(xiDuParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增吸毒人员失败') 
        
    #检查手机端新增的吸毒人员信息
        param = copy.deepcopy(RenKouXinXiPara.checkPopulationDict)      
        param['idCardNo'] = xiDuParam['population.idCardNo']     
        ret = RenKouXinXiIntf.check_Population(param,orgId=orgInit['DftWangGeOrgId'],populationType='DRUGGY', username=userInit['DftWangGeUser'], password='11111111') 
        self.assertTrue(ret, '查找吸毒人员失败')      
        
    #修改吸毒人员
        editParam = copy.deepcopy(RenKouXinXiPara.teShuRenQunObject) 
        editParam['population.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from DRUGGYS  t where t.idcardno='%s'" % xiDuParam['population.idCardNo'])
        editParam['tqmobile'] = 'true'
        editParam['orgId'] = orgInit['DftWangGeOrgId']
        editParam['population.actualPopulationType'] = 'householdStaff'
        editParam['population.attentionPopulationType'] = 'druggy'
        editParam['population.name'] ='修改测试%s'%CommonUtil.createRandomString() 
        editParam['population.organization.id'] = orgInit['DftWangGeOrgId']
        editParam['population.idCardNo'] = xiDuParam['population.idCardNo']
        editParam['population.gender.id'] = xiDuParam['population.gender.id']
        editParam['population.maritalState.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '未婚'")   #婚姻状况
        editParam['population.schooling.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '博士'")  #文化程度
        editParam['population.politicalBackground.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '中国共产党党员'")  #政治面貌   
        editParam['population.nation.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '汉族'")  #民族
        editParam['population.province'] = '浙江省'  #户籍地址省
        editParam['population.city'] = '杭州市'  #户籍地址市
        editParam['population.district'] = '西湖区'  #户籍地址县
        editParam['population.houseAddress'] = "%s%s%s" % (editParam['population.province'],editParam['population.city'],editParam['population.district'])  #户籍地址:省、市、县
        editParam['population.isHaveHouse'] = 'false'  #有无住所:true/false
#         editParam['population.currentAddress'] = '现居地址%s'%CommonUtil.createRandomString()  #true:现居地址
        editParam['population.noHouseReason'] = '无住所原因%s'%CommonUtil.createRandomString()  #false:无住所原因

        editParam['population.detoxicateCase.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '强制戒毒'")   #戒毒情况：强制戒毒、劳教戒毒、期限戒毒、自愿戒毒、社区戒毒、其他、社区康复

        editParam['population.attentionExtent.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '一般'")   #关注程度：一般、中等、严重
        editParam['population.detoxicateCondition.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '在吸'")   #吸毒状态：在吸、停吸
        editParam['population.drugSource.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '其他'")   #毒品来源：黑市购买、亲朋提供、偷窃、医生处方、其他
        editParam['population.drugReason.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '一般'")   #关注程度：一般、中等、严重
        editParam['population.ferretOutDate'] = Time.getCurrentDate()
        editParam['population.drugFristDate'] = '2015-1-1' #首吸时间>查获时间 -待验证
        editParam['population.controlActuality'] = '管控现状'  
        editParam['population.drugType'] = '滥用毒品种类' 
        editParam['population.adanon'] = 'false'  #是否服美沙酮戒毒：false-否（默认） true-是        
        responseDict = RenKouXinXiIntf.edit_xiDuRenYuan(editParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改吸毒人员失败') 
         
    #检查手机端新增吸毒人员的详细信息
        param = copy.deepcopy(RenKouXinXiPara.checkPopulationDict)      
        param['idCardNo'] = editParam['population.idCardNo']     
        ret = RenKouXinXiIntf.check_xiDu(param,populationId=editParam['population.id'], username=userInit['DftWangGeUser'], password='11111111') 
        self.assertTrue(ret, '查找吸毒人员失败') 
        
    #检查手机端新增的吸毒人员信息是否与pc端同步
        ret = ShiYouRenKouIntf.check_xiDuRenYuan(param, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找吸毒人员失败')   
         
#     #检查对应户籍人口下是否存在该新增吸毒人员信息  -存在bug
#         ret_02 = RenKouXinXiIntf.check_Population(param,orgId=orgInit['DftWangGeOrgId'],populationType='RESIDENT', username=userInit['DftWangGeUser'], password='11111111') 
#         self.assertTrue(ret_02, '查找户籍人口失败')   
#          
#     #检查手机端新增的吸毒人员信息是否同步到pc端的户籍人口中
#         ret_03 = ShiYouRenKouIntf.check_HuJiPopulation(param, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
#         self.assertTrue(ret_03, '查找户籍人口失败')    
        
        pass

    def testZhongDianQingShaoNian_13(self):
        """新增、修改重点青少年信息"""
    #新增重点青少年
        qingShaoNianParam = copy.deepcopy(RenKouXinXiPara.teShuRenQunObject) 
        qingShaoNianParam['tqmobile'] = 'true'
        qingShaoNianParam['orgId'] = orgInit['DftWangGeOrgId']
        qingShaoNianParam['population.actualPopulationType'] = 'householdStaff'
        qingShaoNianParam['population.name'] ='重点青少年测试%s'%CommonUtil.createRandomString() 
        qingShaoNianParam['population.organization.id'] = orgInit['DftWangGeOrgId']
        qingShaoNianParam['population.idCardNo'] = '330000199501040033'   #性别根据身份证来确定，如何获取？ *(青少年年龄小于25周岁)*
        qingShaoNianParam['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='女')
        qingShaoNianParam['population.maritalState.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '未婚'")   #婚姻状况
        qingShaoNianParam['population.schooling.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '博士'")  #文化程度
        qingShaoNianParam['population.politicalBackground.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '中国共产党党员'")  #政治面貌   
        qingShaoNianParam['population.nation.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '汉族'")  #民族
        qingShaoNianParam['population.province'] = '浙江省'  #户籍地址省
        qingShaoNianParam['population.city'] = '杭州市'  #户籍地址市
        qingShaoNianParam['population.district'] = '西湖区'  #户籍地址县
        qingShaoNianParam['population.houseAddress'] = "%s%s%s" % (qingShaoNianParam['population.province'],qingShaoNianParam['population.city'],qingShaoNianParam['population.district'])  #户籍地址:省、市、县
        qingShaoNianParam['population.isHaveHouse'] = 'false'  #有无住所:true/false
#         qingShaoNianParam['population.currentAddress'] = '现居地址%s'%CommonUtil.createRandomString()  #true:现居地址
        qingShaoNianParam['population.noHouseReason'] = '无住所原因%s'%CommonUtil.createRandomString()  #false:无住所原因

        # 存在bug（新增添加提交后，查看时该项未保存）       
        qingShaoNianParam['population.staffTypeUpdateIds'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '闲散青少年'")   #人员类型（可多选）：闲散青少年、不良行为青少年、流浪乞讨青少年、服刑在教人员未成年子女、农村留守儿童、其他  
         
        qingShaoNianParam['population.attentionExtent.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '一般'")   #关注程度：一般、中等、严重
        qingShaoNianParam['population.workCondition'] = '工作情况'  
         
        responseDict = RenKouXinXiIntf.add_zhongDianQingShaoNian(qingShaoNianParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增重点青少年失败') 
        
    #检查手机端新增的重点青少年信息
        param = copy.deepcopy(RenKouXinXiPara.checkPopulationDict)      
        param['idCardNo'] = qingShaoNianParam['population.idCardNo']     
        ret = RenKouXinXiIntf.check_Population(param,orgId=orgInit['DftWangGeOrgId'],populationType='IDLEYOUTH', username=userInit['DftWangGeUser'], password='11111111') 
        self.assertTrue(ret, '查找重点青少年失败')      
        
    #修改重点青少年
        editParam = copy.deepcopy(RenKouXinXiPara.teShuRenQunObject) 
        editParam['population.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from idleYouths  t where t.idcardno='%s'" % qingShaoNianParam['population.idCardNo'])
        editParam['tqmobile'] = 'true'
        editParam['orgId'] = orgInit['DftWangGeOrgId']
        editParam['population.attentionPopulationType'] = 'idleYouth'
        editParam['population.name'] ='修改测试%s'%CommonUtil.createRandomString() 
        editParam['population.organization.id'] = orgInit['DftWangGeOrgId']
        editParam['population.idCardNo'] = qingShaoNianParam['population.idCardNo']
        editParam['population.gender.id'] = qingShaoNianParam['population.gender.id']
        editParam['population.maritalState.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '未婚'")   #婚姻状况
        editParam['population.schooling.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '博士'")  #文化程度
        editParam['population.politicalBackground.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '中国共产党党员'")  #政治面貌   
        editParam['population.nation.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '汉族'")  #民族
        editParam['population.province'] = '浙江省'  #户籍地址省
        editParam['population.city'] = '杭州市'  #户籍地址市
        editParam['population.district'] = '西湖区'  #户籍地址县
        editParam['population.houseAddress'] = "%s%s%s" % (editParam['population.province'],editParam['population.city'],editParam['population.district'])  #户籍地址:省、市、县
        editParam['population.isHaveHouse'] = 'false'  #有无住所:true/false
#         editParam['population.currentAddress'] = '现居地址%s'%CommonUtil.createRandomString()  #true:现居地址
        editParam['population.noHouseReason'] = '无住所原因%s'%CommonUtil.createRandomString()  #false:无住所原因

        editParam['population.staffTypeUpdateIds'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '闲散青少年'")   #- *存在bug（新增添加提交后，查看时该项未保存）*  人员类型（可多选）：闲散青少年、不良行为青少年、流浪乞讨青少年、服刑在教人员未成年子女、农村留守儿童、其他  

        responseDict = RenKouXinXiIntf.edit_zhongDianQingShaoNian(editParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改重点青少年失败') 
         
    #检查手机端新增重点青少年的详细信息
        param = copy.deepcopy(RenKouXinXiPara.checkPopulationDict)      
        param['idCardNo'] = editParam['population.idCardNo']     
        ret = RenKouXinXiIntf.check_zhongDianQingShaoNian(param,populationId=editParam['population.id'], username=userInit['DftWangGeUser'], password='11111111') 
        self.assertTrue(ret, '查找重点青少年失败') 
        
    #检查手机端新增的重点青少年信息是否与pc端同步
        ret = ShiYouRenKouIntf.check_zhongDianQingShaoNian(param, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找重点青少年失败')   
         
#     #检查对应户籍人口下是否存在该新增吸毒人员信息  -存在bug
#         ret_02 = RenKouXinXiIntf.check_Population(param,orgId=orgInit['DftWangGeOrgId'],populationType='RESIDENT', username=userInit['DftWangGeUser'], password='11111111') 
#         self.assertTrue(ret_02, '查找户籍人口失败')   
#          
#     #检查手机端新增的吸毒人员信息是否同步到pc端的户籍人口中
#         ret_03 = ShiYouRenKouIntf.check_HuJiPopulation(param, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
#         self.assertTrue(ret_03, '查找户籍人口失败')    
        
        pass

    def testShangFangDuiXiang_14(self):
        """新增、修改重点上访人员信息"""  
    #新增重点上访人员
        shangFangParam = copy.deepcopy(RenKouXinXiPara.teShuRenQunObject) 
        shangFangParam['tqmobile'] = 'true'
        shangFangParam['orgId'] = orgInit['DftWangGeOrgId']
        shangFangParam['population.actualPopulationType'] = 'householdStaff'
        shangFangParam['population.name'] ='重点上访人员测试%s'%CommonUtil.createRandomString() 
        shangFangParam['population.organization.id'] = orgInit['DftWangGeOrgId']
        shangFangParam['population.idCardNo'] = '330000195501040034'   #性别根据身份证来确定，如何获取？
        shangFangParam['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='女')
        shangFangParam['population.maritalState.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '未婚'")   #婚姻状况
        shangFangParam['population.schooling.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '博士'")  #文化程度
        shangFangParam['population.politicalBackground.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '中国共产党党员'")  #政治面貌   
        shangFangParam['population.nation.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '汉族'")  #民族
        shangFangParam['population.province'] = '浙江省'  #户籍地址省
        shangFangParam['population.city'] = '杭州市'  #户籍地址市
        shangFangParam['population.district'] = '西湖区'  #户籍地址县
        shangFangParam['population.houseAddress'] = "%s%s%s" % (shangFangParam['population.province'],shangFangParam['population.city'],shangFangParam['population.district'])  #户籍地址:省、市、县
        shangFangParam['population.isHaveHouse'] = 'false'  #有无住所:true/false
#         shangFangParam['population.currentAddress'] = '现居地址%s'%CommonUtil.createRandomString()  #true:现居地址
        shangFangParam['population.noHouseReason'] = '无住所原因%s'%CommonUtil.createRandomString()  #false:无住所原因

        shangFangParam['population.visitReason'] = '上访原因'

        #验证重点上访人员中的上访原因必填
        shangFangParam['population.visitReason'] =  ''
        responseDict = RenKouXinXiIntf.add_shangFangRenYuan(shangFangParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertFalse(responseDict.result, '新增重点上访人员时上访原因必填项为空仍能新增，验证失败') 
        Log.LogOutput(LogLevel.DEBUG, "新增重点上访人员时上访原因必填项不能为空")         
        shangFangParam['population.visitReason'] = '上访原因'
        
        shangFangParam['population.attentionExtent.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '一般'")   #关注程度：一般、中等、严重
        shangFangParam['population.visitType'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '进京访'")    #类型详情：进京访、进省访
        shangFangParam['population.visitState.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '问题已解决'")   #上访状态：问题已解决、问题未解决
  
        responseDict = RenKouXinXiIntf.add_shangFangRenYuan(shangFangParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增重点上访人员失败') 
        
    #检查手机端新增的重点上访人员信息
        param = copy.deepcopy(RenKouXinXiPara.checkPopulationDict)      
        param['idCardNo'] = shangFangParam['population.idCardNo']     
        ret = RenKouXinXiIntf.check_Population(param,orgId=orgInit['DftWangGeOrgId'],populationType='SUPERIORVISIT', username=userInit['DftWangGeUser'], password='11111111') 
        self.assertTrue(ret, '查找重点上访人员失败')      
        
    #修改重点上访人员    
        editParam = copy.deepcopy(RenKouXinXiPara.teShuRenQunObject) 
        editParam['population.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from superiorVisits  t where t.idcardno='%s'" % shangFangParam['population.idCardNo'])
        editParam['tqmobile'] = 'true'
        editParam['orgId'] = orgInit['DftWangGeOrgId']
        editParam['population.actualPopulationType'] = 'householdStaff'
        editParam['population.attentionPopulationType'] = 'superiorVisit'
        editParam['population.name'] ='修改测试%s'%CommonUtil.createRandomString() 
        editParam['population.organization.id'] = orgInit['DftWangGeOrgId']
        editParam['population.idCardNo'] = shangFangParam['population.idCardNo']
        editParam['population.gender.id'] = shangFangParam['population.gender.id']
        editParam['population.maritalState.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '未婚'")   #婚姻状况
        editParam['population.schooling.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '博士'")  #文化程度
        editParam['population.politicalBackground.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '中国共产党党员'")  #政治面貌   
        editParam['population.nation.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '汉族'")  #民族
        editParam['population.province'] = '浙江省'  #户籍地址省
        editParam['population.city'] = '杭州市'  #户籍地址市
        editParam['population.district'] = '西湖区'  #户籍地址县
        editParam['population.houseAddress'] = "%s%s%s" % (editParam['population.province'],editParam['population.city'],editParam['population.district'])  #户籍地址:省、市、县
        editParam['population.isHaveHouse'] = 'false'  #有无住所:true/false
#         editParam['population.currentAddress'] = '现居地址%s'%CommonUtil.createRandomString()  #true:现居地址
        editParam['population.noHouseReason'] = '无住所原因%s'%CommonUtil.createRandomString()  #false:无住所原因

        editParam['population.visitReason'] = '修改上访原因'
        responseDict = RenKouXinXiIntf.edit_shangFangRenYuan(editParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改重点上访人员失败') 
         
    #检查手机端新增重点上访人员的详细信息
        param = copy.deepcopy(RenKouXinXiPara.checkPopulationDict)      
        param['idCardNo'] = editParam['population.idCardNo']     
        ret = RenKouXinXiIntf.check_shangFangRenYuan(param,populationId=editParam['population.id'], username=userInit['DftWangGeUser'], password='11111111') 
        self.assertTrue(ret, '查找重点上访人员失败') 
        
    #检查手机端新增的重点上访人员信息是否与pc端同步
        ret_01 = ShiYouRenKouIntf.check_shangFangRenYuan(param, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret_01, '查找重点上访人员失败')
         
#     #检查对应户籍人口下是否存在该新增重点上访人员信息  -存在bug
#         ret_02 = RenKouXinXiIntf.check_Population(param,orgId=orgInit['DftWangGeOrgId'],populationType='RESIDENT', username=userInit['DftWangGeUser'], password='11111111') 
#         self.assertTrue(ret_02, '查找户籍人口失败')   
#          
#     #检查手机端新增的重点上访人员信息是否同步到pc端的户籍人口中
#         ret_03 = ShiYouRenKouIntf.check_HuJiPopulation(param, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
#         self.assertTrue(ret_03, '查找户籍人口失败')    
        
        pass

    def testWeiXianPingCongYe_15(self):
        """新增、修改危险品从业人员信息"""
    #新增危险品从业人员
        practitionerParam = copy.deepcopy(RenKouXinXiPara.teShuRenQunObject) 
        practitionerParam['tqmobile'] = 'true'
        practitionerParam['orgId'] = orgInit['DftWangGeOrgId']
        practitionerParam['population.actualPopulationType'] = 'householdStaff'
        practitionerParam['population.name'] ='危险品从业人员测试%s'%CommonUtil.createRandomString() 
        practitionerParam['population.organization.id'] = orgInit['DftWangGeOrgId']
        practitionerParam['population.idCardNo'] = '330000199501040035'   #性别根据身份证来确定，如何获取？ *(青少年年龄小于25周岁)*
        practitionerParam['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='女')
        practitionerParam['population.maritalState.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '未婚'")   #婚姻状况
        practitionerParam['population.schooling.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '博士'")  #文化程度
        practitionerParam['population.politicalBackground.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '中国共产党党员'")  #政治面貌   
        practitionerParam['population.nation.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '汉族'")  #民族
        practitionerParam['population.province'] = '浙江省'  #户籍地址省
        practitionerParam['population.city'] = '杭州市'  #户籍地址市
        practitionerParam['population.district'] = '西湖区'  #户籍地址县
        practitionerParam['population.houseAddress'] = "%s%s%s" % (practitionerParam['population.province'],practitionerParam['population.city'],practitionerParam['population.district'])  #户籍地址:省、市、县
        practitionerParam['population.isHaveHouse'] = 'false'  #有无住所:true/false
#         practitionerParam['population.currentAddress'] = '现居地址%s'%CommonUtil.createRandomString()  #true:现居地址
        practitionerParam['population.noHouseReason'] = '无住所原因%s'%CommonUtil.createRandomString()  #false:无住所原因

        practitionerParam['population.dangerousWorkingType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '民爆'")   #危险品从业类别：民爆、化工、其他  
        practitionerParam['population.legalPerson'] = '法人代表'  
        practitionerParam['population.legalPersonMobileNumber'] = '18100000000' #手机号必须是1开始的11位数字  
        practitionerParam['population.legalPersonTelephone'] = '3621000'  
        practitionerParam['population.workUnit'] = '工作单位或就读学校'   #不能输入特殊字符

        #验证危险品从业人员中的危险品从业类别必填
        practitionerParam['population.dangerousWorkingType.id'] = ''
        responseDict = RenKouXinXiIntf.add_practitioner(practitionerParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertFalse(responseDict.result, '新增危险品从业人员时危险品从业类别必填项为空仍能新增，验证失败') 
        Log.LogOutput(LogLevel.DEBUG, "新增危险品从业人员时危险品从业类别必填项不能为空")         
        practitionerParam['population.dangerousWorkingType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '民爆'")   #危险品从业类别：民爆、化工、其他  
        #验证危险品从业人员中的法人代表必填
        practitionerParam['population.legalPerson'] = ''
        responseDict = RenKouXinXiIntf.add_practitioner(practitionerParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertFalse(responseDict.result, '新增危险品从业人员时法人代表必填项为空仍能新增，验证失败') 
        Log.LogOutput(LogLevel.DEBUG, "新增危险品从业人员时法人代表别必填项不能为空")        
        practitionerParam['population.legalPerson'] = '法人代表'  
        #验证危险品从业人员中的企业法人手机号必填
        practitionerParam['population.legalPersonMobileNumber'] =  ''
        responseDict = RenKouXinXiIntf.add_practitioner(practitionerParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertFalse(responseDict.result, '新增危险品从业人员时企业法人手机号必填项为空仍能新增，验证失败') 
        Log.LogOutput(LogLevel.DEBUG, "新增危险品从业人员时企业法人手机号别必填项不能为空")  
        practitionerParam['population.legalPersonMobileNumber'] = '18100000000' #手机号必须是1开始的11位数字  
        #验证危险品从业人员中的企业法人联系电话必填
        practitionerParam['population.legalPersonTelephone'] = ''
        responseDict = RenKouXinXiIntf.add_practitioner(practitionerParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertFalse(responseDict.result, '新增危险品从业人员时企业法人联系电话必填项为空仍能新增，验证失败') 
        Log.LogOutput(LogLevel.DEBUG, "新增危险品从业人员时企业法人联系电话别必填项不能为空")
        practitionerParam['population.legalPersonTelephone'] = '3621000'  
        #验证危险品从业人员中的工作单位或就读学校必填
        practitionerParam['population.workUnit'] = ''
        responseDict = RenKouXinXiIntf.add_practitioner(practitionerParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertFalse(responseDict.result, '新增危险品从业人员时工作单位或就读学校必填项为空仍能新增，验证失败') 
        Log.LogOutput(LogLevel.DEBUG, "新增危险品从业人员时工作单位或就读学校别必填项不能为空")        
        practitionerParam['population.workUnit'] = '工作单位或就读学校'   #不能输入特殊字符

        practitionerParam['population.attentionExtent.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '一般'")   #关注程度：一般、中等、严重
        practitionerParam['population.workingCertificate'] = '从业资格证书'  
        practitionerParam['population.workingCertificateNo'] = '123'  #从业资格证书号 
        practitionerParam['population.periodOfValidityStart'] = '2015-1-1'  #资格证书有效期
        practitionerParam['population.periodOfValidityEnd'] = Time.getCurrentDate()
         
        responseDict = RenKouXinXiIntf.add_practitioner(practitionerParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增危险品从业人员失败') 
        
    #检查手机端新增的危险品从业人员信息
        param = copy.deepcopy(RenKouXinXiPara.checkPopulationDict)      
        param['idCardNo'] = practitionerParam['population.idCardNo']     
        ret = RenKouXinXiIntf.check_Population(param,orgId=orgInit['DftWangGeOrgId'],populationType='DANGEROUSGOODSPRACTITIONER', username=userInit['DftWangGeUser'], password='11111111') 
        self.assertTrue(ret, '查找危险品从业人员失败')      
        
    #修改危险品从业人员
        editParam = copy.deepcopy(RenKouXinXiPara.teShuRenQunObject) 
        editParam['population.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from dangerousGoodsPractitioners  t where t.idcardno='%s'" % practitionerParam['population.idCardNo'])
        editParam['tqmobile'] = 'true'
        editParam['orgId'] = orgInit['DftWangGeOrgId']
        editParam['population.actualPopulationType'] = 'householdStaff'
        editParam['population.attentionPopulationType'] = 'dangerousGoodsPractitioner'
        editParam['population.name'] ='修改测试%s'%CommonUtil.createRandomString() 
        editParam['population.organization.id'] = orgInit['DftWangGeOrgId']
        editParam['population.idCardNo'] = practitionerParam['population.idCardNo']
        editParam['population.gender.id'] = practitionerParam['population.gender.id']
        editParam['population.maritalState.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '未婚'")   #婚姻状况
        editParam['population.schooling.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '博士'")  #文化程度
        editParam['population.politicalBackground.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '中国共产党党员'")  #政治面貌   
        editParam['population.nation.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '汉族'")  #民族
        editParam['population.province'] = '浙江省'  #户籍地址省
        editParam['population.city'] = '杭州市'  #户籍地址市
        editParam['population.district'] = '西湖区'  #户籍地址县
        editParam['population.houseAddress'] = "%s%s%s" % (editParam['population.province'],editParam['population.city'],editParam['population.district'])  #户籍地址:省、市、县
        editParam['population.isHaveHouse'] = 'false'  #有无住所:true/false
#         editParam['population.currentAddress'] = '现居地址%s'%CommonUtil.createRandomString()  #true:现居地址
        editParam['population.noHouseReason'] = '无住所原因%s'%CommonUtil.createRandomString()  #false:无住所原因

        editParam['population.dangerousWorkingType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '民爆'")   #危险品从业类别：民爆、化工、其他  
        editParam['population.legalPerson'] = '法人代表'  
        editParam['population.legalPersonMobileNumber'] = '18100000000' #手机号必须是1开始的11位数字  
        editParam['population.legalPersonTelephone'] = '3621000'  
        editParam['population.workUnit'] = '工作单位或就读学校'   #不能输入特殊字符

        responseDict = RenKouXinXiIntf.edit_practitioner(editParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改危险品从业人员失败') 
         
    #检查手机端新增危险品从业人员的详细信息
        param = copy.deepcopy(RenKouXinXiPara.checkPopulationDict)      
        param['idCardNo'] = editParam['population.idCardNo']     
        ret = RenKouXinXiIntf.check_practitioner(param,populationId=editParam['population.id'], username=userInit['DftWangGeUser'], password='11111111') 
        self.assertTrue(ret, '查找危险品从业人员失败') 
        
    #检查手机端新增的重危险品从业人员信息是否与pc端同步
        ret_01 = ShiYouRenKouIntf.check_weiXianPingCongYeRenYuan(param, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret_01, '查找危险品从业人员失败')   
         
#     #检查对应户籍人口下是否存在该新增危险品从业人员信息  -存在bug
#         ret_02 = RenKouXinXiIntf.check_Population(param,orgId=orgInit['DftWangGeOrgId'],populationType='RESIDENT', username=userInit['DftWangGeUser'], password='11111111') 
#         self.assertTrue(ret_02, '查找户籍人口失败')   
#          
#     #检查手机端新增的危险品从业人员信息是否同步到pc端的户籍人口中
#         ret_03 = ShiYouRenKouIntf.check_HuJiPopulation(param, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
#         self.assertTrue(ret_03, '查找户籍人口失败')    
        
        pass

    def testJiaoZhengtransfer_16(self):
        """矫正人员转为刑释人员"""
    #新增矫正人员
        jiaoZhengParam = copy.deepcopy(RenKouXinXiPara.teShuRenQunObject) 
        jiaoZhengParam['tqmobile'] = 'true'
        jiaoZhengParam['orgId'] = orgInit['DftWangGeOrgId']
        jiaoZhengParam['population.actualPopulationType'] = 'householdStaff'
        jiaoZhengParam['population.name'] ='矫正转刑释测试%s'%CommonUtil.createRandomString() 
        jiaoZhengParam['population.organization.id'] = orgInit['DftWangGeOrgId']
        jiaoZhengParam['population.idCardNo'] = '330000199501010036'
        jiaoZhengParam['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='女')
        jiaoZhengParam['population.maritalState.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '未婚'")   #婚姻状况
        jiaoZhengParam['population.schooling.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '博士'")  #文化程度
        jiaoZhengParam['population.politicalBackground.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '中国共产党党员'")  #政治面貌   
        jiaoZhengParam['population.nation.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '汉族'")  #民族
        jiaoZhengParam['population.province'] = '浙江省'  #户籍地址省
        jiaoZhengParam['population.city'] = '杭州市'  #户籍地址市
        jiaoZhengParam['population.district'] = '西湖区'  #户籍地址县
        jiaoZhengParam['population.houseAddress'] = "%s%s%s" % (jiaoZhengParam['population.province'],jiaoZhengParam['population.city'],jiaoZhengParam['population.district'])  #户籍地址:省、市、县
        jiaoZhengParam['population.isHaveHouse'] = 'false'  #有无住所:true/false
#         jiaoZhengParam['population.currentAddress'] = '现居地址%s'%CommonUtil.createRandomString()  #true:现居地址
        jiaoZhengParam['population.noHouseReason'] = '无住所原因%s'%CommonUtil.createRandomString()  #false:无住所原因

        jiaoZhengParam['population.accusation'] = '罪名'
        jiaoZhengParam['population.executeType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '监外执行罪犯'")   #刑法执行类别：监外执行罪犯、管制人员、缓刑人员、假释人员、其他
        jiaoZhengParam['population.rectifyStartDate'] = Time.getCurrentDate()
        jiaoZhengParam['population.rectifyEndDate'] = '2020-1-1'
        
        responseDict = RenKouXinXiIntf.add_jiaoZhengRenYuan(jiaoZhengParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增矫正人员失败') 

    #新增刑释人员
        XingShiParam = copy.deepcopy(RenKouXinXiPara.teShuRenQunObject) 
        XingShiParam['population.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rectificativePersons  t where t.idcardno='%s'" % jiaoZhengParam['population.idCardNo'])
        XingShiParam['population.attentionPopulationType'] = 'rectificativePerson'     
        XingShiParam['tqmobile'] = 'true'
        XingShiParam['orgId'] = orgInit['DftWangGeOrgId']
        XingShiParam['population.actualPopulationType'] = 'householdStaff'
        XingShiParam['population.name'] =jiaoZhengParam['population.name']
        XingShiParam['population.organization.id'] = jiaoZhengParam['population.organization.id']
        XingShiParam['population.idCardNo'] = jiaoZhengParam['population.idCardNo'] 
        XingShiParam['population.gender.id'] = jiaoZhengParam['population.gender.id']
        XingShiParam['population.maritalState.id'] = jiaoZhengParam['population.maritalState.id']
        XingShiParam['population.schooling.id'] = jiaoZhengParam['population.schooling.id']
        XingShiParam['population.politicalBackground.id'] = jiaoZhengParam['population.politicalBackground.id']   
        XingShiParam['population.nation.id'] = jiaoZhengParam['population.nation.id']
        XingShiParam['population.province'] = jiaoZhengParam['population.province']
        XingShiParam['population.city'] = jiaoZhengParam['population.city'] 
        XingShiParam['population.district'] = jiaoZhengParam['population.district']
        XingShiParam['population.houseAddress'] = jiaoZhengParam['population.houseAddress'] 
        XingShiParam['population.isHaveHouse'] = jiaoZhengParam['population.isHaveHouse']
#         XingShiParam['population.currentAddress'] = jiaoZhengParam['population.currentAddress']
        XingShiParam['population.noHouseReason'] = jiaoZhengParam['population.noHouseReason']

        XingShiParam['population.positiveInfoType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '刑释人员'")   #人员类型：刑释人员、解教人员
        XingShiParam['population.caseReason'] = '原罪名'
        XingShiParam['population.imprisonmentDate'] = '3周'  #原判刑期
        XingShiParam['population.laborEduAddress'] = '劳教场所'
        XingShiParam['population.releaseOrBackDate'] = Time.getCurrentDate()

        responseDict = RenKouXinXiIntf.add_XingShiRenYuan(XingShiParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增刑释人员失败') 

    #检查手机端的刑释人员列表下矫正转刑释的人员信息（存在）
        param = copy.deepcopy(RenKouXinXiPara.checkPopulationDict)      
        param['idCardNo'] = XingShiParam['population.idCardNo']     
        ret = RenKouXinXiIntf.check_Population(param,orgId=orgInit['DftWangGeOrgId'],populationType='POSITIVEINFO', username=userInit['DftWangGeUser'], password='11111111') 
        self.assertTrue(ret, '查找刑释人员失败') 
        
    #检查手机端的矫正人员列表下矫正转刑释的人员信息（不存在）
        param = copy.deepcopy(RenKouXinXiPara.checkPopulationDict) 
        param['idCardNo'] = jiaoZhengParam['population.idCardNo']     
        ret = RenKouXinXiIntf.check_Population(param,orgId=orgInit['DftWangGeOrgId'],populationType='RECTIFICATIVEPERSON', username=userInit['DftWangGeUser'], password='11111111') 
        self.assertFalse(ret, '矫正转刑释的人员，在矫正人员列表下依然存在，操作失败') 

    def tearDown(self):
        pass
    
if __name__ == "__main__":
    suite = unittest.TestSuite() 
 
##实有人口    
#    suite.addTest(RenKouXinXi("testHuJiPopulation_01"))
#     suite.addTest(RenKouXinXi("testDepartmentCheck_02"))
#     suite.addTest(RenKouXinXi("testLiuDongPopulation_04"))
#     suite.addTest(RenKouXinXi("testJingWaiPopulation_05"))
#     suite.addTest(RenKouXinXi("testHuJiPopulationSearch_06"))
#     suite.addTest(RenKouXinXi("testHuJiPopulationService_07"))
#     suite.addTest(RenKouXinXi("testHuJiPopulationServiceDelete_08"))
    
#     suite.addTest(RenKouXinXi("testXingShiPopulation_09"))
#    suite.addTest(RenKouXinXi("testJiaoZhengPopulation_10"))
#    suite.addTest(RenKouXinXi("testJingShengPopulation_11"))
#     suite.addTest(RenKouXinXi("testXiDuPopulation_12"))
#     suite.addTest(RenKouXinXi("testZhongDianQingShaoNian_13"))    
#     suite.addTest(RenKouXinXi("testShangFangDuiXiang_14"))    
#    suite.addTest(RenKouXinXi("testWeiXianPingCongYe_15"))    
    suite.addTest(RenKouXinXi("testJiaoZhengtransfer_16"))    
    
    results = unittest.TextTestRunner().run(suite)
    pass

