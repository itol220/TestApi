# -*- coding:UTF-8 -*-
'''
Created on 2015-11-16

@author: chenyan
'''
from __future__ import unicode_literals
from COMMON import CommonUtil, Log, Time
from COMMON.CommonUtil import createRandomString
from CONFIG import InitDefaultPara
from CONFIG.Define import LogLevel
from CONFIG.InitDefaultPara import orgInit, userInit
from Interface.PingAnJianShe.Common import CommonIntf
from Interface.PingAnJianShe.ShiJianChuLi import ShiJianChuLiPara, \
    ShiJianChuLiIntf
from Interface.PingAnJianShe.ShiYouRenKou import ShiYouRenKouIntf, \
    ShiYouRenKouPara
from Interface.PingAnJianShe.SystemMgr import SystemMgrIntf
from Interface.PingAnJianShe.XiaQuGuanLi import XiaQuGuanLiIntf
import copy
import json
import time
import unittest



# reload(sys)
# sys.setdefaultencoding('utf-8')

class ShiYouRenKou(unittest.TestCase):

    def setUp(self):
        SystemMgrIntf.initEnv()
        ShiYouRenKouIntf.deleteAllPopulation()
        pass

#实有人口
  
    def testHuJiPopulationAdd_01(self):
        """实有人口>户籍人口信息新增"""
        LiuDongParam_01 = copy.deepcopy(ShiYouRenKouPara.populationObject) 
        LiuDongParam_01['population.organization.id'] = orgInit['DftWangGeOrgId']
        LiuDongParam_01['population.actualPopulationType'] = 'floatingPopulation'
        LiuDongParam_01['population.organization.orgName'] = orgInit['DftWangGeOrg']
        LiuDongParam_01['population.idCardNo'] = '111111111111001'
        LiuDongParam_01['population.name'] = 'test01'
        LiuDongParam_01['population.isHaveHouse1'] = 'null'         
        responseDict = ShiYouRenKouIntf.add_LiuDongRenKou(LiuDongRenKouDict=LiuDongParam_01, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增流动人口失败') 

        HuJiParam_01 = copy.deepcopy(ShiYouRenKouPara.populationObject) 
        HuJiParam_01['mode']='add'
        HuJiParam_01['population.organization.id'] = orgInit['DftWangGeOrgId']
        HuJiParam_01['population.organization.orgName'] = orgInit['DftWangGeOrg']   
        HuJiParam_01['population.name'] = 'test1'        
        HuJiParam_01['population.idCardNo'] = LiuDongParam_01['population.idCardNo']
        HuJiParam_01['population.isHaveHouse1'] = 'null'   
        HuJiParam_01['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')          
        
        param_01 = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)      
        param_01['idCardNo'] = HuJiParam_01['population.idCardNo']       

        ret_01 = ShiYouRenKouIntf.check_HuJiPopulation(param_01, orgId=HuJiParam_01['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        if ret_01 is True:
            Log.LogOutput(LogLevel.DEBUG, "当前户籍人口中存在该id人口信息,请重新输入id信息")
        else:         
            ret_02 = ShiYouRenKouIntf.check_floatingPopulation(param_01, orgId=LiuDongParam_01['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111') 
            if ret_02 is True:        
                Log.LogOutput(LogLevel.DEBUG, "流动人口中存在该id人口信息,请重新输入id信息")   
                HuJiParam_01['population.idCardNo'] = '111111111110011'
                responseDict = ShiYouRenKouIntf.add_HuJiRenKou(HuJiRenKouDict=HuJiParam_01, username=userInit['DftWangGeUser'], password='11111111')
                self.assertTrue(responseDict.result, '新增户籍人口失败')   
                param_01['idCardNo'] = HuJiParam_01['population.idCardNo']    
                param_01['name'] = HuJiParam_01['population.name'] 
                ret = ShiYouRenKouIntf.check_HuJiPopulation(param_01, orgId=HuJiParam_01['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
                self.assertTrue(ret, '查找户籍人口失败')           
            else:  
                responseDict = ShiYouRenKouIntf.add_HuJiRenKou(HuJiRenKouDict=HuJiParam_01, username=userInit['DftWangGeUser'], password='11111111')
                self.assertTrue(responseDict.result, '新增户籍人口失败')       
                param_01['name'] = HuJiParam_01['population.name'] 
                ret = ShiYouRenKouIntf.check_HuJiPopulation(param_01, orgId=HuJiParam_01['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
                self.assertTrue(ret, '查找户籍人口失败')
                pass
 
    def testHuJiPopulationDetele_02(self):
        """实有人口>户籍人口信息批量删除"""

        HuJiParam_02 = copy.deepcopy(ShiYouRenKouPara.populationObject) 
        HuJiParam_02['mode']='add'
        HuJiParam_02['population.organization.id'] = orgInit['DftWangGeOrgId']
        HuJiParam_02['population.organization.orgName'] = orgInit['DftWangGeOrg']
        HuJiParam_02['population.idCardNo'] = '111111111111120'
        HuJiParam_02['population.name'] = 'test2'
        HuJiParam_02['population.isHaveHouse1'] = 'null'         
        responseDict = ShiYouRenKouIntf.add_HuJiRenKou(HuJiRenKouDict=HuJiParam_02, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口失败')    
        
        newHuJiParam = copy.deepcopy(ShiYouRenKouPara.populationObject) 
        newHuJiParam['mode']='add'
        newHuJiParam['population.organization.id'] = orgInit['DftWangGeOrgId']
        newHuJiParam['population.organization.orgName'] = orgInit['DftWangGeOrg']
        newHuJiParam['population.idCardNo'] = '111111111111121'
        newHuJiParam['population.name'] = 'test21'
        newHuJiParam['population.isHaveHouse1'] = 'null'         
        responseDict = ShiYouRenKouIntf.add_HuJiRenKou(HuJiRenKouDict=newHuJiParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口失败')     
         
        deleteParam = copy.deepcopy(ShiYouRenKouPara.delHuJiDict)
        deleteParam['householdStaffVo.idStr'] = str(CommonIntf.getDbQueryResult(dbCommand = "select t.id from householdstaffs t where t.idcardno='%s'" % HuJiParam_02['population.idCardNo']))+','+str(CommonIntf.getDbQueryResult(dbCommand = "select t.id from householdstaffs t where t.idcardno='%s'" % newHuJiParam['population.idCardNo']))
        ret = ShiYouRenKouIntf.delete_HuJiRenKou(deleteParam,username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret.result, '删除户籍人口失败') 
                       
        param_02 = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        param_02['name'] = HuJiParam_02['population.name']       
        param_02['idCardNo'] = HuJiParam_02['population.idCardNo']
        ret = ShiYouRenKouIntf.check_HuJiPopulation(param_02, orgId=HuJiParam_02['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '已删除人口在列表中依然存在') 
         
        param_02['name'] = newHuJiParam['population.name']       
        param_02['idCardNo'] = newHuJiParam['population.idCardNo']
        ret = ShiYouRenKouIntf.check_HuJiPopulation(param_02, orgId=newHuJiParam['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '已删除人口在列表中依然存在') 
       
        pass 
    
    def testHuJiPopulationEdit_03(self): 
        """实有人口>户籍人口信息修改"""     
        
        HuJiParam_03 = copy.deepcopy(ShiYouRenKouPara.populationObject) 
        HuJiParam_03['mode']='add'
        HuJiParam_03['population.organization.id'] = orgInit['DftWangGeOrgId']
        HuJiParam_03['population.organization.orgName'] = orgInit['DftWangGeOrg']
        HuJiParam_03['population.idCardNo'] = '111111111111130'
        HuJiParam_03['population.name'] = 'test3'
        HuJiParam_03['population.isHaveHouse1'] = 'null'         
        responseDict = ShiYouRenKouIntf.add_HuJiRenKou(HuJiRenKouDict=HuJiParam_03, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口失败')
        
        editParam = copy.deepcopy(ShiYouRenKouPara.populationObject) 
        editParam['mode']='edit'
        editParam['population.id']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from householdstaffs t where t.idcardno='%s' and t.name='%s'" % (HuJiParam_03['population.idCardNo'],HuJiParam_03['population.name']))
        editParam['population.organization.id'] = HuJiParam_03['population.organization.id']
        editParam['population.organization.orgName'] = HuJiParam_03['population.organization.orgName']  
        editParam['population.idCardNo'] = HuJiParam_03['population.idCardNo']
        editParam['population.name'] = '测试'
        editParam['population.isHaveHouse1'] = 'null'    
        responseDict = ShiYouRenKouIntf.edit_ShiYouRenKou(HuJiRenKouDict=editParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改户籍人口失败')

        param_03 = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        param_03['name'] = editParam['population.name']       
        param_03['idCardNo'] = editParam['population.idCardNo']
        ret = ShiYouRenKouIntf.check_HuJiPopulation(param_03, orgId=editParam['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找户籍人口失败')
         
        pass

    def testHuJiPopulationSearch_04(self):      
        """实有人口>户籍人口信息搜索"""
        
        HuJiParam_04 = copy.deepcopy(ShiYouRenKouPara.populationObject) 
        HuJiParam_04['mode']='add'
        HuJiParam_04['population.organization.id'] = orgInit['DftWangGeOrgId']
        HuJiParam_04['population.organization.orgName'] = orgInit['DftWangGeOrg']
        HuJiParam_04['population.idCardNo'] = '111111111111140'
        HuJiParam_04['population.name'] = 'test4'
        HuJiParam_04['population.isHaveHouse1'] = 'null'         
        responseDict = ShiYouRenKouIntf.add_HuJiRenKou(HuJiRenKouDict=HuJiParam_04, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口失败')
        
        NewHuJiParam_01 = copy.deepcopy(ShiYouRenKouPara.populationObject) 
        NewHuJiParam_01['mode']='add'
        NewHuJiParam_01['population.organization.id'] = orgInit['DftWangGeOrgId']
        NewHuJiParam_01['population.organization.orgName'] = orgInit['DftWangGeOrg']
        NewHuJiParam_01['population.idCardNo'] = '111111111111141'
        NewHuJiParam_01['population.name'] = 'test41'
        NewHuJiParam_01['population.isHaveHouse1'] = 'null'         
        responseDict = ShiYouRenKouIntf.add_HuJiRenKou(HuJiRenKouDict=NewHuJiParam_01, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口失败')
        
        NewHuJiParam_02 = copy.deepcopy(ShiYouRenKouPara.populationObject) 
        NewHuJiParam_02['mode']='add'
        NewHuJiParam_02['population.organization.id'] = orgInit['DftWangGeOrgId']
        NewHuJiParam_02['population.organization.orgName'] = orgInit['DftWangGeOrg']
        NewHuJiParam_02['population.idCardNo'] = '111111111111142'
        NewHuJiParam_02['population.name'] = 'test42'
        NewHuJiParam_02['population.isHaveHouse1'] = 'null'         
        responseDict = ShiYouRenKouIntf.add_HuJiRenKou(HuJiRenKouDict=NewHuJiParam_02, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口失败')

        param_04 = copy.deepcopy(ShiYouRenKouPara.searchHuJiOrgDict)
        param_04['name'] = NewHuJiParam_01['population.name']       
        param_04['idCardNo'] = NewHuJiParam_01['population.idCardNo']
        ret = ShiYouRenKouIntf.search_HuJiRenKou(param_04, orgId=NewHuJiParam_01['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '搜索人口失败')
         
        pass
 
    def testHuJiPopulationImportAndDownLoad_05(self):
        """实有人口>户籍人口信息 导入/导出"""
         
        importHuJiparam_05 = copy.deepcopy(ShiYouRenKouPara.data)
        importHuJiparam_05['dataType']='householdStaffData'
        importHuJiparam_05['templates']='HOUSEHOLDSTAFF'
        files = {'upload': ('test.xls', open('C:/autotest_file/importHuJiPopulation.xls', 'rb'),'applicationnd.ms-excel')}
        ret = ShiYouRenKouIntf.import_RenKou(importHuJiparam_05, files=files,username=userInit['DftWangGeUser'], password='11111111')         
         
        param_05 = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        param_05['name'] = '户籍导入测试'
        param_05['idCardNo'] = '111111111111169'
        ret = ShiYouRenKouIntf.check_HuJiPopulation(param_05, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')          
        self.assertTrue(ret, '查找人口失败')
                                
        downLoadHuJiparam_05 = copy.deepcopy(ShiYouRenKouPara.dlHuJiData)
        downLoadHuJiparam_05['searchMode']='noFast_noAdvanced_search'
        downLoadHuJiparam_05['orgId']=orgInit['DftWangGeOrgId']
        response = ShiYouRenKouIntf.downLoad_HuJiRenKou(downLoadHuJiparam_05, username=userInit['DftWangGeUser'], password='11111111')         
        Time.wait(2)
        with open("C:/autotest_file/downLoadHuJiPopulation.xls", "wb") as code:
            code.write(response.content)
            
        ret = CommonUtil.checkExcelCellValue(param_05['name'], 'downLoadHuJiPopulation.xls','户籍人口清单', 'A4')          
        self.assertTrue(ret, '导出失败')
                         
        pass
    
    def testHuJiPopulationLogout_06(self):
        """实有人口> 注销/取消注销已有户籍人口信息"""

        HuJiParam_06 = copy.deepcopy(ShiYouRenKouPara.populationObject) 
        HuJiParam_06['mode']='add'
        HuJiParam_06['population.organization.id'] = orgInit['DftWangGeOrgId']
        HuJiParam_06['population.organization.orgName'] = orgInit['DftWangGeOrg']
        HuJiParam_06['population.idCardNo'] = '111111111111162'
        HuJiParam_06['population.name'] = 'test666'
        HuJiParam_06['population.isHaveHouse1'] = 'null'         
        responseDict = ShiYouRenKouIntf.add_HuJiRenKou(HuJiRenKouDict=HuJiParam_06, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口失败')
        
        param_06 = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        param_06['name'] = HuJiParam_06['population.name']       
        param_06['idCardNo'] = HuJiParam_06['population.idCardNo']
        ret = ShiYouRenKouIntf.check_HuJiPopulation(param_06, orgId=HuJiParam_06['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找人口失败')
        
        detaileParam = copy.deepcopy(ShiYouRenKouPara.logoutHuJiDict)
        detaileParam['populationIds'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from householdstaffs t where t.idcardno='%s' and t.name='%s'" % (HuJiParam_06['population.idCardNo'],HuJiParam_06['population.name']))
        detaileParam['population.logoutDetail.logout'] = '1'
        detaileParam['population.logoutDetail.logoutDate'] = Time.getCurrentDateAndTime()
        detaileParam['population.logoutDetail.logoutReason'] = '注销'
        ret = ShiYouRenKouIntf.logout_HuJiRenKou(detaileParam,username=userInit['DftWangGeUser'], password='11111111')
#         self.assertTrue(ret.result, '注销人口失败') 
        
        ret = ShiYouRenKouIntf.check_HuJiPopulation(param_06, orgId=HuJiParam_06['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '已注销人口在列表中依然存在')     
        
        detailecancelParam = copy.deepcopy(ShiYouRenKouPara.logoutHuJiDict)
        detailecancelParam['population.logoutDetail.logout'] = '0'
        detailecancelParam['populationIds'] = detaileParam['populationIds']
        ret = ShiYouRenKouIntf.logoutCancel_HuJiRenKou(detailecancelParam,username=userInit['DftWangGeUser'], password='11111111')
#         self.assertTrue(ret.result, '取消注销人口失败') 
        
        ret = ShiYouRenKouIntf.check_HuJiPopulation(param_06, orgId=HuJiParam_06['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '已取消注销人口在列表中不存在')          
                    
        pass   

    def testHuJiPopulationDeathCancel_07(self):  
        """实有人口>户籍人口修改死亡状态/取消死亡状态"""    
        
        HuJiParam_07 = copy.deepcopy(ShiYouRenKouPara.populationObject) 
        HuJiParam_07['mode']='add'
        HuJiParam_07['population.organization.id'] = orgInit['DftWangGeOrgId']
        HuJiParam_07['population.organization.orgName'] = orgInit['DftWangGeOrg']
        HuJiParam_07['population.idCardNo'] = '111111111111170'
        HuJiParam_07['population.name'] = 'test7'
        HuJiParam_07['population.isHaveHouse1'] = 'null' 
#         HuJiParam_07['population.death'] = 'true'  #新增人口死亡
        responseDict = ShiYouRenKouIntf.add_HuJiRenKou(HuJiRenKouDict=HuJiParam_07, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口失败')
        
        editDeathParam = copy.deepcopy(ShiYouRenKouPara.populationObject) 
        editDeathParam['mode']='edit'
        editDeathParam['population.id']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from householdstaffs t where t.idcardno='%s' and t.name='%s'" % (HuJiParam_07['population.idCardNo'],HuJiParam_07['population.name']))
        editDeathParam['population.organization.id'] = HuJiParam_07['population.organization.id']
        editDeathParam['population.organization.orgName'] = HuJiParam_07['population.organization.orgName']  
        editDeathParam['population.idCardNo'] = HuJiParam_07['population.idCardNo']
        editDeathParam['population.name'] = 'ceshi'
        editDeathParam['population.isHaveHouse1'] = 'null'    
        editDeathParam['population.death'] = 'true'   #修改人口死亡
        responseDict = ShiYouRenKouIntf.edit_ShiYouRenKou(HuJiRenKouDict=editDeathParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改户籍人口失败')
                
        deathcancelParam = copy.deepcopy(ShiYouRenKouPara.populationObject)
        deathcancelParam['population.death'] = 'false'
        deathcancelParam['householdStaffIds'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from householdstaffs t where t.idcardno='%s' and t.name='%s'" % (editDeathParam['population.idCardNo'],editDeathParam['population.name']))
        ret = ShiYouRenKouIntf.deathcancel_ShiYouRenKou(deathcancelParam,username=userInit['DftWangGeUser'], password='11111111')
#         self.assertTrue(ret.result, '取消死亡人口失败') 
        
        param_07 = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        param_07['name'] = editDeathParam['population.name']       
        param_07['idCardNo'] = editDeathParam['population.idCardNo']
        ret = ShiYouRenKouIntf.check_HuJiPopulation(param_07, orgId=editDeathParam['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找人口失败')
        pass

    def testHuJiPopulationServiceAdd_08(self):
        """管理服务成员,添加服务人员"""
        XiaQuGuanLiIntf.xiaQuGuanLiMemberDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        HuJiParam_08 = copy.deepcopy(ShiYouRenKouPara.populationObject) 
        HuJiParam_08['mode']='add'
        HuJiParam_08['population.organization.id'] = orgInit['DftWangGeOrgId']
        HuJiParam_08['population.organization.orgName'] = orgInit['DftWangGeOrg']
        HuJiParam_08['population.idCardNo'] = '111111111111180'
        HuJiParam_08['population.name'] = 'test8'
        HuJiParam_08['population.isHaveHouse1'] = 'null'         
        responseDict = ShiYouRenKouIntf.add_HuJiRenKou(HuJiRenKouDict=HuJiParam_08, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口失败')
        
        fuWuParam = copy.deepcopy(ShiYouRenKouPara.fuWuRenYuanDict)      
        fuWuParam['serviceTeamMemberBase.org.id'] = orgInit['DftWangGeOrgId']
        fuWuParam['serviceTeamMemberBase.name'] = '服务%s'%CommonUtil.createRandomString()
        fuWuParam['serviceTeamMemberBase.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别(男、女)', displayName='男')     
        fuWuParam['serviceTeamMemberBase.mobile'] = '13011111111'
        responseDict = ShiYouRenKouIntf.add_FuWuChengYuan(fuWuDict=fuWuParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增成员失败')        
         
        MemberParam = copy.deepcopy(ShiYouRenKouPara.serviceMemberDict)      
        MemberParam['serviceMemberWithObject.memberId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from Serviceteammemberbase t where t.name='%s'" % (fuWuParam['serviceTeamMemberBase.name']))
        MemberParam['serviceMemberWithObject.objectType'] = 'householdStaff'
        MemberParam['serviceMemberWithObject.objectName'] = HuJiParam_08['population.name']   
        MemberParam['serviceMemberWithObject.objectId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from householdstaffs t where t.idcardno='%s' and t.name='%s'" % (HuJiParam_08['population.idCardNo'],HuJiParam_08['population.name']))
        MemberParam['serviceMemberWithObject.teamMember'] = '1'
        MemberParam['serviceMemberWithObject.onDuty'] = '1'
        MemberParam['serviceMemberWithObject.objectLogout'] = '1' 
        responseDict = ShiYouRenKouIntf.add_serviceMemberHuJiRenKou(serviceDict=MemberParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增服务人员失败')
         
        Memberparam_08 = copy.deepcopy(ShiYouRenKouPara.checkServiceMemberDict)
        Memberparam_08['memberName'] = fuWuParam['serviceTeamMemberBase.name']      
        Memberparam_08['memberId'] = MemberParam['serviceMemberWithObject.memberId']
        ret = ShiYouRenKouIntf.check_serviceMember(Memberparam_08, objectType=MemberParam['serviceMemberWithObject.objectType'],objectId=MemberParam['serviceMemberWithObject.objectId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找服务人口失败')
        XiaQuGuanLiIntf.xiaQuGuanLiMemberDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        pass

    def testHuJiPopulationServiceDelete_08(self):
        """管理服务成员,删除服务人员"""
        XiaQuGuanLiIntf.xiaQuGuanLiMemberDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        HuJiParam_08 = copy.deepcopy(ShiYouRenKouPara.populationObject) 
        HuJiParam_08['mode']='add'
        HuJiParam_08['population.organization.id'] = orgInit['DftWangGeOrgId']
        HuJiParam_08['population.organization.orgName'] = orgInit['DftWangGeOrg']
        HuJiParam_08['population.idCardNo'] = '111111111111181'
        HuJiParam_08['population.name'] = 'test8'
        HuJiParam_08['population.isHaveHouse1'] = 'null'         
        responseDict = ShiYouRenKouIntf.add_HuJiRenKou(HuJiRenKouDict=HuJiParam_08, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口失败')
        
        fuWuParam = copy.deepcopy(ShiYouRenKouPara.fuWuRenYuanDict)      
        fuWuParam['serviceTeamMemberBase.org.id'] = orgInit['DftWangGeOrgId']
        fuWuParam['serviceTeamMemberBase.name'] = '服务%s'%CommonUtil.createRandomString()
        fuWuParam['serviceTeamMemberBase.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别(男、女)', displayName='男')     
        fuWuParam['serviceTeamMemberBase.mobile'] = '13011111111'
        responseDict = ShiYouRenKouIntf.add_FuWuChengYuan(fuWuDict=fuWuParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增成员失败')        
         
        MemberParam = copy.deepcopy(ShiYouRenKouPara.serviceMemberDict)      
        MemberParam['serviceMemberWithObject.memberId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from Serviceteammemberbase t where t.name='%s'" % (fuWuParam['serviceTeamMemberBase.name']))
        MemberParam['serviceMemberWithObject.objectType'] = 'householdStaff'
        MemberParam['serviceMemberWithObject.objectName'] = HuJiParam_08['population.name']   
        MemberParam['serviceMemberWithObject.objectId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from householdstaffs t where t.idcardno='%s' and t.name='%s'" % (HuJiParam_08['population.idCardNo'],HuJiParam_08['population.name']))
        MemberParam['serviceMemberWithObject.teamMember'] = '1'
        MemberParam['serviceMemberWithObject.onDuty'] = '1'
        MemberParam['serviceMemberWithObject.objectLogout'] = '1'    
        responseDict = ShiYouRenKouIntf.add_serviceMemberHuJiRenKou(serviceDict=MemberParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增服务人员失败')
        
        deleteParam = copy.deepcopy(ShiYouRenKouPara.deleteServiceMemberDict)
        deleteParam['selectedIds'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from serviceMemberHasObject t where t.memberid='%s'" % (MemberParam['serviceMemberWithObject.memberId']))
        ret = ShiYouRenKouIntf.delete_serviceMemberHuJiRenKou(deleteParam,username=userInit['DftWangGeUser'], password='11111111')
#         self.assertTrue(ret.result, '删除服务人员失败') 
        
        Memberparam_08 = copy.deepcopy(ShiYouRenKouPara.checkServiceMemberDict)
        Memberparam_08['memberName'] = fuWuParam['serviceTeamMemberBase.name']      
        Memberparam_08['memberId'] = MemberParam['serviceMemberWithObject.memberId']
        ret = ShiYouRenKouIntf.check_serviceMember(Memberparam_08, objectType=MemberParam['serviceMemberWithObject.objectType'],objectId=MemberParam['serviceMemberWithObject.objectId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '已删除的服务人员在列表中依然存在')
        XiaQuGuanLiIntf.xiaQuGuanLiMemberDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        pass

    def testHuJiPopulationServiceLeaveOrBack_08(self):
        """管理服务成员,卸任/重新担任服务人员"""
        XiaQuGuanLiIntf.xiaQuGuanLiMemberDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        HuJiParam_08 = copy.deepcopy(ShiYouRenKouPara.populationObject) 
        HuJiParam_08['mode']='add'
        HuJiParam_08['population.organization.id'] = orgInit['DftWangGeOrgId']
        HuJiParam_08['population.organization.orgName'] = orgInit['DftWangGeOrg']
        HuJiParam_08['population.idCardNo'] = '111111111111182'
        HuJiParam_08['population.name'] = 'test8'
        HuJiParam_08['population.isHaveHouse1'] = 'null'         
        responseDict = ShiYouRenKouIntf.add_HuJiRenKou(HuJiRenKouDict=HuJiParam_08, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口失败')
        
        fuWuParam = copy.deepcopy(ShiYouRenKouPara.fuWuRenYuanDict)      
        fuWuParam['serviceTeamMemberBase.org.id'] = orgInit['DftWangGeOrgId']
        fuWuParam['serviceTeamMemberBase.name'] = '服务1%s'%CommonUtil.createRandomString()
        fuWuParam['serviceTeamMemberBase.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别(男、女)', displayName='男')     
        fuWuParam['serviceTeamMemberBase.mobile'] = '13011111111'
        responseDict = ShiYouRenKouIntf.add_FuWuChengYuan(fuWuDict=fuWuParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增成员失败')        
         
        MemberParam = copy.deepcopy(ShiYouRenKouPara.serviceMemberDict)      
        MemberParam['serviceMemberWithObject.memberId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from Serviceteammemberbase t where t.name='%s'" % (fuWuParam['serviceTeamMemberBase.name']))
        MemberParam['serviceMemberWithObject.objectType'] = 'householdStaff'
        MemberParam['serviceMemberWithObject.objectName'] = HuJiParam_08['population.name']   
        MemberParam['serviceMemberWithObject.objectId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from householdstaffs t where t.idcardno='%s' and t.name='%s'" % (HuJiParam_08['population.idCardNo'],HuJiParam_08['population.name']))
        MemberParam['serviceMemberWithObject.teamMember'] = '1'
        MemberParam['serviceMemberWithObject.onDuty'] = '1'
        MemberParam['serviceMemberWithObject.objectLogout'] = '1'    
        responseDict = ShiYouRenKouIntf.add_serviceMemberHuJiRenKou(serviceDict=MemberParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增服务人员失败')
        
        leaveParam = copy.deepcopy(ShiYouRenKouPara.leaveOrBackServiceMemberDict)
        leaveParam['serviceMemberWithObject.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from serviceMemberHasObject t where t.memberid='%s'" % (MemberParam['serviceMemberWithObject.memberId']))
        leaveParam['serviceMemberWithObject.onDuty'] = '0'
        leaveParam['serviceMemberWithObject.memberId'] = MemberParam['serviceMemberWithObject.memberId']
        ret = ShiYouRenKouIntf.leave_serviceMemberHuJiRenKou(leaveParam,username=userInit['DftWangGeUser'], password='11111111')
#         self.assertTrue(ret.result, '卸任服务人员失败') 
        
        Memberparam_08 = copy.deepcopy(ShiYouRenKouPara.checkServiceMemberDict)
        Memberparam_08['memberName'] = fuWuParam['serviceTeamMemberBase.name']      
        Memberparam_08['memberId'] = MemberParam['serviceMemberWithObject.memberId']
        ret = ShiYouRenKouIntf.check_leaveServiceMember(Memberparam_08, objectId=MemberParam['serviceMemberWithObject.objectId'],onDuty = '0',username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '在曾任筛选下,检查不到该卸任的服务人员信息')
        
        backParam = copy.deepcopy(ShiYouRenKouPara.leaveOrBackServiceMemberDict)
        backParam['serviceMemberWithObject.id'] = leaveParam['serviceMemberWithObject.id']
        backParam['serviceMemberWithObject.onDuty'] = '1'
        backParam['serviceMemberWithObject.memberId'] = leaveParam['serviceMemberWithObject.memberId']
        ret = ShiYouRenKouIntf.back_serviceMemberHuJiRenKou(backParam,username=userInit['DftWangGeUser'], password='11111111')
#         self.assertTrue(ret.result, '重新担任失败') 
        
        ret = ShiYouRenKouIntf.check_serviceMember(Memberparam_08, objectType=MemberParam['serviceMemberWithObject.objectType'],objectId=MemberParam['serviceMemberWithObject.objectId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找服务人口失败')               
        XiaQuGuanLiIntf.xiaQuGuanLiMemberDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        pass
 
    def testHuJiPopulationGuardersAdd_08(self):
        """管理服务成员添加监护人员"""
        
        HuJiParam_08 = copy.deepcopy(ShiYouRenKouPara.populationObject) 
        HuJiParam_08['mode']='add'
        HuJiParam_08['population.organization.id'] = orgInit['DftWangGeOrgId']
        HuJiParam_08['population.organization.orgName'] = orgInit['DftWangGeOrg']
        HuJiParam_08['population.idCardNo'] = '111111111111185'
        HuJiParam_08['population.name'] = 'test08'
        HuJiParam_08['population.isHaveHouse1'] = 'null'         
        responseDict = ShiYouRenKouIntf.add_HuJiRenKou(HuJiRenKouDict=HuJiParam_08, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口失败')
 
        GuardersParam = copy.deepcopy(ShiYouRenKouPara.serviceGuardersDict) 
        GuardersParam['serviceTeamMemberVo.org.id'] = HuJiParam_08['population.organization.id']
        GuardersParam['serviceTeamGuarders.serviceGuardersWithObject.objectType'] = 'householdStaff'
        GuardersParam['serviceTeamGuarders.serviceGuardersWithObject.objectName'] = HuJiParam_08['population.name']   
        GuardersParam['serviceTeamGuarders.serviceGuardersWithObject.objectId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from householdstaffs t where t.idcardno='%s' and t.name='%s'" % (HuJiParam_08['population.idCardNo'],HuJiParam_08['population.name']))
        GuardersParam['serviceTeamGuarders.serviceGuardersWithObject.teamMember'] = '0'
        GuardersParam['isSubmit'] = 'true'    
        GuardersParam['serviceTeamGuarders.guarderName'] = '监护人员%s'%CommonUtil.createRandomString()
        GuardersParam['serviceTeamGuarders.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别(男、女)', displayName='男')
        GuardersParam['serviceTeamGuarders.relation'] = '家属'
        responseDict = ShiYouRenKouIntf.add_serviceGuardersHuJiRenKou(GuardersDict=GuardersParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增监护人员失败')
         
        guardersParam_08 = copy.deepcopy(ShiYouRenKouPara.checkServiceMemberDict)     
        guardersParam_08['memberId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from serviceTeamGuarders t where t.Guardername='%s'"%(GuardersParam['serviceTeamGuarders.guarderName']))
        ret = ShiYouRenKouIntf.check_serviceMember(guardersParam_08, objectType=GuardersParam['serviceTeamGuarders.serviceGuardersWithObject.objectType'],objectId=GuardersParam['serviceTeamGuarders.serviceGuardersWithObject.objectId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找监护人员失败')
        pass
    
    def testHuJiPopulationGuardersDelete_08(self):
        """管理服务成员删除监护人员信息"""
        
        HuJiParam_08 = copy.deepcopy(ShiYouRenKouPara.populationObject) 
        HuJiParam_08['mode']='add'
        HuJiParam_08['population.organization.id'] = orgInit['DftWangGeOrgId']
        HuJiParam_08['population.organization.orgName'] = orgInit['DftWangGeOrg']
        HuJiParam_08['population.idCardNo'] = '111111111111186'
        HuJiParam_08['population.name'] = 'test08'
        HuJiParam_08['population.isHaveHouse1'] = 'null'         
        responseDict = ShiYouRenKouIntf.add_HuJiRenKou(HuJiRenKouDict=HuJiParam_08, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口失败')
 
        GuardersParam = copy.deepcopy(ShiYouRenKouPara.serviceGuardersDict) 
        GuardersParam['serviceTeamMemberVo.org.id'] = HuJiParam_08['population.organization.id']
        GuardersParam['serviceTeamGuarders.serviceGuardersWithObject.objectType'] = 'householdStaff'
        GuardersParam['serviceTeamGuarders.serviceGuardersWithObject.objectName'] = HuJiParam_08['population.name']   
        GuardersParam['serviceTeamGuarders.serviceGuardersWithObject.objectId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from householdstaffs t where t.idcardno='%s' and t.name='%s'" % (HuJiParam_08['population.idCardNo'],HuJiParam_08['population.name']))
        GuardersParam['serviceTeamGuarders.serviceGuardersWithObject.teamMember'] = '0'
        GuardersParam['isSubmit'] = 'true'    
        GuardersParam['serviceTeamGuarders.guarderName'] = '监护人员%s'%CommonUtil.createRandomString()
        GuardersParam['serviceTeamGuarders.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别(男、女)', displayName='男')
        GuardersParam['serviceTeamGuarders.relation'] = '家属'
        responseDict = ShiYouRenKouIntf.add_serviceGuardersHuJiRenKou(GuardersDict=GuardersParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增监护人员失败')
        
        deleteParam = copy.deepcopy(ShiYouRenKouPara.deleteServiceMemberDict)
        deleteParam['selectedIds'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from serviceTeamGuarders t where t.Guardername='%s'"%(GuardersParam['serviceTeamGuarders.guarderName']))
        ret = ShiYouRenKouIntf.delete_serviceGuardersHuJiRenKou(deleteParam,username=userInit['DftWangGeUser'], password='11111111')
        #成功后返回值为"1"，结果不好判断
        self.assertTrue(ret.result, '删除监护人员失败')        
         
        guardersParam_08 = copy.deepcopy(ShiYouRenKouPara.checkServiceMemberDict)     
        guardersParam_08['memberId'] = deleteParam['selectedIds']
        ret = ShiYouRenKouIntf.check_serviceMember(guardersParam_08, objectType=GuardersParam['serviceTeamGuarders.serviceGuardersWithObject.objectType'],objectId=GuardersParam['serviceTeamGuarders.serviceGuardersWithObject.objectId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '已删除的监护人员在列表中依然存在')
        pass
    
    def testHuJiPopulationGuardersEdit_08(self):
        """管理服务成员修改监护人员信息"""
        
        HuJiParam_08 = copy.deepcopy(ShiYouRenKouPara.populationObject) 
        HuJiParam_08['mode']='add'
        HuJiParam_08['population.organization.id'] = orgInit['DftWangGeOrgId']
        HuJiParam_08['population.organization.orgName'] = orgInit['DftWangGeOrg']
        HuJiParam_08['population.idCardNo'] = '111111111111187'
        HuJiParam_08['population.name'] = 'test08'
        HuJiParam_08['population.isHaveHouse1'] = 'null'         
        responseDict = ShiYouRenKouIntf.add_HuJiRenKou(HuJiRenKouDict=HuJiParam_08, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口失败')
 
        GuardersParam = copy.deepcopy(ShiYouRenKouPara.serviceGuardersDict) 
        GuardersParam['serviceTeamMemberVo.org.id'] = HuJiParam_08['population.organization.id']
        GuardersParam['serviceTeamGuarders.serviceGuardersWithObject.objectType'] = 'householdStaff'
        GuardersParam['serviceTeamGuarders.serviceGuardersWithObject.objectName'] = HuJiParam_08['population.name']   
        GuardersParam['serviceTeamGuarders.serviceGuardersWithObject.objectId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from householdstaffs t where t.idcardno='%s' and t.name='%s'" % (HuJiParam_08['population.idCardNo'],HuJiParam_08['population.name']))
        GuardersParam['serviceTeamGuarders.serviceGuardersWithObject.teamMember'] = '0'
        GuardersParam['isSubmit'] = 'true'    
        GuardersParam['serviceTeamGuarders.guarderName'] = '监护人员%s'%CommonUtil.createRandomString()
        GuardersParam['serviceTeamGuarders.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别(男、女)', displayName='男')
        GuardersParam['serviceTeamGuarders.relation'] = '家属'
        responseDict = ShiYouRenKouIntf.add_serviceGuardersHuJiRenKou(GuardersDict=GuardersParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增监护人员失败')
        
        editParam = copy.deepcopy(ShiYouRenKouPara.serviceGuardersDict) 
        editParam['serviceTeamGuarders.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from serviceTeamGuarders t where t.Guardername='%s'"%(GuardersParam['serviceTeamGuarders.guarderName']))
        editParam['isSubmit'] = 'true'    
        editParam['serviceTeamGuarders.guarderName'] = '监护人员'
        editParam['serviceTeamGuarders.gender.id'] = GuardersParam['serviceTeamGuarders.gender.id']
        editParam['serviceTeamGuarders.relation'] = GuardersParam['serviceTeamGuarders.relation']
        responseDict = ShiYouRenKouIntf.edit_serviceGuardersHuJiRenKou(GuardersDict=editParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改监护人员失败')       
          
        guardersParam_08 = copy.deepcopy(ShiYouRenKouPara.checkServiceMemberDict)     
        guardersParam_08['memberId'] = editParam['serviceTeamGuarders.id']
        ret = ShiYouRenKouIntf.check_serviceMember(guardersParam_08, objectType=GuardersParam['serviceTeamGuarders.serviceGuardersWithObject.objectType'],objectId=GuardersParam['serviceTeamGuarders.serviceGuardersWithObject.objectId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找监护人员失败')
        pass
 
    def testHuJiPopulationServiceRecordAdd_09(self):
        """添加管理服务记录"""
        try:
            HuJiParam_09 = copy.deepcopy(ShiYouRenKouPara.populationObject) 
            HuJiParam_09['mode']='add'
            HuJiParam_09['population.organization.id'] = orgInit['DftWangGeOrgId']
            HuJiParam_09['population.organization.orgName'] = orgInit['DftWangGeOrg']
            HuJiParam_09['population.idCardNo'] = '111111111111190'
            HuJiParam_09['population.name'] = 'test9'+createRandomString()
            HuJiParam_09['population.isHaveHouse1'] = 'null'         
            responseDict1 = ShiYouRenKouIntf.add_HuJiRenKou(HuJiRenKouDict=HuJiParam_09, username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict1.result, '新增户籍人口失败')    
    #         print json.loads(responseDict1.text)['id']
            fuWuParam_09 = copy.deepcopy(ShiYouRenKouPara.fuWuRenYuanDict)      
            fuWuParam_09['serviceTeamMemberBase.org.id'] = orgInit['DftWangGeOrgId']
            fuWuParam_09['serviceTeamMemberBase.name'] = '服务人员姓名%s'%CommonUtil.createRandomString()
            fuWuParam_09['serviceTeamMemberBase.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别(男、女)', displayName='男')     
            fuWuParam_09['serviceTeamMemberBase.mobile'] = '13011111111'
            responseDict2 = ShiYouRenKouIntf.add_FuWuChengYuan(fuWuDict=fuWuParam_09, username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict2.result, '新增成员失败')    
    #         print   json.loads(responseDict2.text)['baseId']
            RecordParam = copy.deepcopy(ShiYouRenKouPara.serviceRecordDict) 
            RecordParam['mode'] = 'add'   
            RecordParam['serviceRecord.userOrgId']=orgInit['DftWangGeOrgId'] 
            RecordParam['serviceRecord.organization.id'] = orgInit['DftWangGeOrgId']  
            RecordParam['isSubmit'] = 'true'
            RecordParam['serviceRecord.occurDate'] = Time.getCurrentDate()
            RecordParam['serviceRecord.occurPlace'] = '服务地点%s'%CommonUtil.createRandomString()
            RecordParam['serviceRecord.serviceMembers'] = str(json.loads(responseDict2.text)['baseId'])+'-'+fuWuParam_09['serviceTeamMemberBase.name'] +'-0'
            RecordParam['serviceRecord.serviceJoiners']='服务参与人'+createRandomString()
            RecordParam['serviceRecord.serviceObjects'] = str(json.loads(responseDict1.text)['id'])+'-'+HuJiParam_09['population.name']+'-householdStaff'
            RecordParam['serviceRecord.serviceContent']='服务内容'+createRandomString()
            responseDict3 = ShiYouRenKouIntf.add_serviceRecordHuJiRenKou(RecordDict=RecordParam, username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict3.result, '新增服务事件失败')
            param_09 = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
            param_09['occurDate'] = RecordParam['serviceRecord.occurDate']       
            param_09['occurPlace'] = RecordParam['serviceRecord.occurPlace']
            ret = ShiYouRenKouIntf.check_serviceRecord(param_09, objectIds=CommonIntf.getDbQueryResult(dbCommand = "select t.id from householdstaffs t where t.idcardno='%s' and t.name='%s'" % (HuJiParam_09['population.idCardNo'],HuJiParam_09['population.name'])),orgId=HuJiParam_09['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
            self.assertTrue(ret, '查找服务事件失败')
            #补充用例，服务记录转事件
            #获取户籍人口服务记录列表
            listPara=copy.deepcopy(ShiYouRenKouPara.personServiceRecopdListPara)
            listPara['objectIds']=json.loads(responseDict1.text)['id']
            listPara['serviceRecordVo.organization.id']=orgInit['DftWangGeOrgId']
            listPara['serviceRecordVo.displayYear']=time.strftime("%Y")
            responseDict4=ShiYouRenKouIntf.get_serviceRecordHuJiRenKou(listpara=listPara)
            self.assertTrue(responseDict4.result, '服务记录列表获取失败')
            #转事件参数
            para=copy.deepcopy(ShiYouRenKouPara.serviceRecordToIssuePara)
            para['issue.occurOrg.id']=orgInit['DftWangGeOrgId']
            para['sourceType']=CommonIntf.getDbQueryResult(dbCommand='''select id from propertydicts pr where pr.displayname = '人工录入' and pr.propertydomainid=(
               select id from propertydomains where domainName like '来源方式')''')
            para['issue.subject']='服务记录转事件'+createRandomString()
            para['selectOrgName']=orgInit['DftWangGeOrg']
            para['issue.occurLocation']=RecordParam['serviceRecord.occurPlace']
            para['issue.occurDate']=RecordParam['serviceRecord.occurDate']
            para['issueRelatedPeopleNames']=HuJiParam_09['population.name']+'-'+str(json.loads(responseDict1.text)['id'])+'-householdStaff'
            para['issueRelatedPeopleNames']=fuWuParam_09['serviceTeamMemberBase.name'] 
            para['issueRelatedPeopleNameBaks1']=fuWuParam_09['serviceTeamMemberBase.name']
            para['issueRelatedPeopleTelephones']=fuWuParam_09['serviceTeamMemberBase.mobile']
            para['selectRelatedPeople']=str(json.loads(responseDict1.text)['id'])+'-householdStaff-'+HuJiParam_09['population.name']
            para['issue.relatePeopleCount']='2'
            para['selectedTypes']=CommonIntf.getDbQueryResult(dbCommand="select id from issuetypes i where i.domainid=(select id from issuetypedomains where module='core' and domainName='矛盾纠纷') and i.issuetypename='医患纠纷'")
            para['issue.issueContent']=RecordParam['serviceRecord.serviceContent']
            para['serviceRecordAddIssue.serviceRecordId']=json.loads(responseDict4.text)['rows'][0]['id']
            responseDict5=ShiYouRenKouIntf.serviceRecordToIssue(listpara=para)
            self.assertTrue(responseDict5.result, '服务记录转事件失败')
            #验证转事件功能
            checkParam=copy.deepcopy(ShiJianChuLiPara.IssueCheckPara)
            checkParam['subject']=para['issue.subject']
            checkParam['occurDateString']=para['issue.occurDate']
            ret=ShiJianChuLiIntf.checkIssue(checkIssueDict=checkParam,username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(ret, '全部事项列表中没有找到对应的事件')
            Log.LogOutput(level=LogLevel.DEBUG, message='服务记录转事件验证通过') 
        finally:
            #清空事件
            ShiJianChuLiIntf.shiJianChuLiInitEnv() 
            #清空所有服务记录
            XiaQuGuanLiIntf.deleteAllServiceRecord(year=time.strftime("%Y"))
            #清空所有服务成员
            XiaQuGuanLiIntf.xiaQuGuanLiMemberDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
       
        pass

    def testHuJiPopulationServiceRecordEdit_09(self):
        """修改管理服务记录"""
        XiaQuGuanLiIntf.xiaQuGuanLiMemberDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        HuJiParam_09 = copy.deepcopy(ShiYouRenKouPara.populationObject) 
        HuJiParam_09['mode']='add'
        HuJiParam_09['population.organization.id'] = orgInit['DftWangGeOrgId']
        HuJiParam_09['population.organization.orgName'] = orgInit['DftWangGeOrg']
        HuJiParam_09['population.idCardNo'] = '111111111111190'
        HuJiParam_09['population.name'] = 'test9'
        HuJiParam_09['population.isHaveHouse1'] = 'null'         
        responseDict = ShiYouRenKouIntf.add_HuJiRenKou(HuJiRenKouDict=HuJiParam_09, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口失败')    
        
        fuWuParam_09 = copy.deepcopy(ShiYouRenKouPara.fuWuRenYuanDict)      
        fuWuParam_09['serviceTeamMemberBase.org.id'] = orgInit['DftWangGeOrgId']
        fuWuParam_09['serviceTeamMemberBase.name'] = '服务%s'%CommonUtil.createRandomString()
        fuWuParam_09['serviceTeamMemberBase.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别(男、女)', displayName='男')     
        fuWuParam_09['serviceTeamMemberBase.mobile'] = '13011111111'
        responseDict = ShiYouRenKouIntf.add_FuWuChengYuan(fuWuDict=fuWuParam_09, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增成员失败')    
          
        RecordParam = copy.deepcopy(ShiYouRenKouPara.serviceRecordDict) 
        RecordParam['mode'] = 'add'         
        RecordParam['serviceRecord.userOrgId'] = orgInit['DftWangGeOrgId'] 
        RecordParam['serviceRecord.organization.id'] = orgInit['DftWangGeOrgId']  
        RecordParam['isSubmit'] = 'true'
        RecordParam['serviceRecord.occurDate'] = '2015-12-04'
        RecordParam['serviceRecord.occurPlace'] = '地点%s'%CommonUtil.createRandomString()
        RecordParam['serviceRecord.serviceMembers'] = str(CommonIntf.getDbQueryResult(dbCommand = "select t.id from Serviceteammemberbase  t where t.name='%s'" %(fuWuParam_09['serviceTeamMemberBase.name'])))+'-服务-0'
        RecordParam['serviceRecord.serviceObjects'] = str(CommonIntf.getDbQueryResult(dbCommand = "select t.id from householdstaffs t where t.idcardno='%s' and t.name='%s'" % (HuJiParam_09['population.idCardNo'],HuJiParam_09['population.name'])))+'-'+HuJiParam_09['population.name']+'-householdStaff'  
        RecordParam['serviceRecord.serviceContent'] = "服务内容默认"
        RecordParam["serviceRecord.visitSituation.id"] = CommonIntf.getIdByDomainAndDisplayName(domainName='走访情况', displayName='无')
        responseDict = ShiYouRenKouIntf.add_serviceRecordHuJiRenKou(RecordDict=RecordParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增服务事件失败')
        
        editRecordParam = copy.deepcopy(ShiYouRenKouPara.serviceRecordDict) 
        editRecordParam['mode'] = 'edit'
        editRecordParam['serviceRecord.userOrgId'] = orgInit['DftWangGeOrgId']
        editRecordParam['serviceRecord.organization.id'] = orgInit['DftWangGeOrgId']  
        editRecordParam['serviceRecord.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from serviceRecords t where t.occurPlace='%s' and t.serviceObjects='%s'" % (RecordParam['serviceRecord.occurPlace'],HuJiParam_09['population.name']))      
        editRecordParam['serviceRecord.occurDate'] = RecordParam['serviceRecord.occurDate']
        editRecordParam['serviceRecord.occurPlace'] = '地点qq%s'%CommonUtil.createRandomString()
        editRecordParam['serviceRecord.serviceMembers'] = RecordParam['serviceRecord.serviceMembers']
        editRecordParam['serviceRecord.serviceObjects'] = RecordParam['serviceRecord.serviceObjects']
        editRecordParam['serviceRecord.serviceContent'] = RecordParam['serviceRecord.serviceContent']
        editRecordParam["serviceRecord.visitSituation.id"] = CommonIntf.getIdByDomainAndDisplayName(domainName='走访情况', displayName='无')
        editRecordParam['serviceRecord.createUser'] = userInit['DftWangGeUser']
        responseDict = ShiYouRenKouIntf.edit_serviceRecordHuJiRenKou(RecordDict=editRecordParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改服务事件失败')
          
        param_09 = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        param_09['occurDate'] = editRecordParam['serviceRecord.occurDate']       
        param_09['occurPlace'] = editRecordParam['serviceRecord.occurPlace']
        ret = ShiYouRenKouIntf.check_serviceRecord(param_09, objectIds=CommonIntf.getDbQueryResult(dbCommand = "select t.id from householdstaffs t where t.idcardno='%s' and t.name='%s'" % (HuJiParam_09['population.idCardNo'],HuJiParam_09['population.name'])),orgId=HuJiParam_09['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找服务事件失败')
        XiaQuGuanLiIntf.xiaQuGuanLiMemberDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        pass

    def testHuJiPopulationServiceRecordDelete_09(self):
        """删除管理服务记录"""
        XiaQuGuanLiIntf.xiaQuGuanLiMemberDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        HuJiParam_09 = copy.deepcopy(ShiYouRenKouPara.populationObject) 
        HuJiParam_09['mode']='add'
        HuJiParam_09['population.organization.id'] = orgInit['DftWangGeOrgId']
        HuJiParam_09['population.organization.orgName'] = orgInit['DftWangGeOrg']
        HuJiParam_09['population.idCardNo'] = '111111111111190'
        HuJiParam_09['population.name'] = 'test9'
        HuJiParam_09['population.isHaveHouse1'] = 'null'         
        responseDict = ShiYouRenKouIntf.add_HuJiRenKou(HuJiRenKouDict=HuJiParam_09, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口失败')    
        
        fuWuParam_09 = copy.deepcopy(ShiYouRenKouPara.fuWuRenYuanDict)      
        fuWuParam_09['serviceTeamMemberBase.org.id'] = orgInit['DftWangGeOrgId']
        fuWuParam_09['serviceTeamMemberBase.name'] = '服务%s'%CommonUtil.createRandomString()
        fuWuParam_09['serviceTeamMemberBase.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别(男、女)', displayName='男')     
        fuWuParam_09['serviceTeamMemberBase.mobile'] = '13011111111'
        responseDict = ShiYouRenKouIntf.add_FuWuChengYuan(fuWuDict=fuWuParam_09, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增成员失败')    
          
        RecordParam = copy.deepcopy(ShiYouRenKouPara.serviceRecordDict) 
        RecordParam['mode'] = 'add'   
        RecordParam['serviceRecord.organization.id'] = orgInit['DftWangGeOrgId']  
        RecordParam['isSubmit'] = 'true'
        RecordParam['serviceRecord.occurDate'] = '2015-12-04'
        RecordParam['serviceRecord.occurPlace'] = '地点%s'%CommonUtil.createRandomString()
        RecordParam['serviceRecord.serviceMembers'] = str(CommonIntf.getDbQueryResult(dbCommand = "select t.id from Serviceteammemberbase  t where t.name='%s'" %(fuWuParam_09['serviceTeamMemberBase.name'])))+'-服务-0'
        RecordParam['serviceRecord.serviceObjects'] = str(CommonIntf.getDbQueryResult(dbCommand = "select t.id from householdstaffs t where t.idcardno='%s' and t.name='%s'" % (HuJiParam_09['population.idCardNo'],HuJiParam_09['population.name'])))+'-'+HuJiParam_09['population.name']+'-householdStaff'  
        RecordParam['serviceRecord.serviceContent'] = '服务记录内容'
        responseDict = ShiYouRenKouIntf.add_serviceRecordHuJiRenKou(RecordDict=RecordParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增服务事件失败')
        
        deleteRecordParam = copy.deepcopy(ShiYouRenKouPara.deleteServiceRecordDict) 
        deleteRecordParam['mode'] = 'delete'   
        deleteRecordParam['recordIds'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from serviceRecords t where t.occurPlace='%s' and t.serviceObjects='%s'" % (RecordParam['serviceRecord.occurPlace'],HuJiParam_09['population.name']))  
        responseDict = ShiYouRenKouIntf.delete_serviceRecordHuJiRenKou(RecordDict=deleteRecordParam, username=userInit['DftWangGeUser'], password='11111111')
#         self.assertTrue(responseDict.result, '删除服务事件失败')
          
        param_09 = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        param_09['occurDate'] = RecordParam['serviceRecord.occurDate']       
        param_09['occurPlace'] = RecordParam['serviceRecord.occurPlace']
        ret = ShiYouRenKouIntf.check_serviceRecord(param_09, objectIds=CommonIntf.getDbQueryResult(dbCommand = "select t.id from householdstaffs t where t.idcardno='%s' and t.name='%s'" % (HuJiParam_09['population.idCardNo'],HuJiParam_09['population.name'])),orgId=HuJiParam_09['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '删除的服务事件在列表中依然存在')
        XiaQuGuanLiIntf.xiaQuGuanLiMemberDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        pass

    def testHuJiPopulationTransfer_10(self):
        """实有人口>户籍人口转为流动人口"""

        HuJiParam_10 = copy.deepcopy(ShiYouRenKouPara.populationObject) 
        HuJiParam_10['mode']='add'
        HuJiParam_10['population.organization.id'] = orgInit['DftWangGeOrgId']
        HuJiParam_10['population.organization.orgName'] = orgInit['DftWangGeOrg']
        HuJiParam_10['population.idCardNo'] = '111111111111100'
        HuJiParam_10['population.name'] = 'test10'
        HuJiParam_10['population.isHaveHouse1'] = 'null'         
        responseDict = ShiYouRenKouIntf.add_HuJiRenKou(HuJiRenKouDict=HuJiParam_10, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口失败')
         
        param_10 = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        param_10['name'] = HuJiParam_10['population.name']       
        param_10['idCardNo'] = HuJiParam_10['population.idCardNo']
        ret = ShiYouRenKouIntf.check_HuJiPopulation(param_10, orgId=HuJiParam_10['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找人口失败')
         
        transferParam = copy.deepcopy(ShiYouRenKouPara.populationObject)
        transferParam['population.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from householdstaffs t where t.idcardno='%s' and t.name='%s'" % (HuJiParam_10['population.idCardNo'],HuJiParam_10['population.name']))
        ret = ShiYouRenKouIntf.transfer_HuJiRenKou(transferParam,username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret.result, '转为流动人口失败') 
         
        ret = ShiYouRenKouIntf.check_HuJiPopulation(param_10, orgId=HuJiParam_10['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '已转移人口在列表中依然存在')
        
        checkParam_10 = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)  
        checkParam_10['name'] = HuJiParam_10['population.name']   
        checkParam_10['idCardNo'] = HuJiParam_10['population.idCardNo']
        ret = ShiYouRenKouIntf.check_LiuDongpopulation(checkParam_10, orgId=HuJiParam_10['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找人口失败')
        
        pass   

    def testTransferToWangGe_13(self):
        """当前网格下的实有人口信息转到其他网格"""

        HuJiParam_13 = copy.deepcopy(ShiYouRenKouPara.populationObject) 
        HuJiParam_13['mode']='add'
        HuJiParam_13['population.organization.id'] = orgInit['DftWangGeOrgId']
        HuJiParam_13['population.organization.orgName'] = orgInit['DftWangGeOrg']
        HuJiParam_13['population.idCardNo'] = '111111111111300'
        HuJiParam_13['population.name'] = 'test13'
        HuJiParam_13['population.isHaveHouse1'] = 'null'         
        responseDict = ShiYouRenKouIntf.add_HuJiRenKou(HuJiRenKouDict=HuJiParam_13, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口失败')
        
        param_13 = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        param_13['name'] = HuJiParam_13['population.name']       
        param_13['idCardNo'] = HuJiParam_13['population.idCardNo']
        ret = ShiYouRenKouIntf.check_HuJiPopulation(param_13, orgId=HuJiParam_13['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找人口失败')
        
        transferParam_13 = copy.deepcopy(ShiYouRenKouPara.transferObject)
        transferParam_13['orgId'] = HuJiParam_13['population.organization.id']
        transferParam_13['Ids'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from householdstaffs t where t.idcardno='%s' and t.name='%s'" % (HuJiParam_13['population.idCardNo'],HuJiParam_13['population.name']))
        transferParam_13['toOrgId'] = orgInit['DftWangGeOrgId1']
        transferParam_13['type'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']
        ret = ShiYouRenKouIntf.transfer_toWangGe(transferParam_13,username=userInit['DftWangGeUser'], password='11111111')
#         self.assertTrue(ret.result, '转移人口失败') 
        
        checkParam_13 = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)  
        checkParam_13['name'] = HuJiParam_13['population.name']   
        checkParam_13['idCardNo'] = HuJiParam_13['population.idCardNo']
        ret = ShiYouRenKouIntf.check_HuJiPopulation(checkParam_13, orgId=orgInit['DftWangGeOrgId1'],username=userInit['DftWangGeUser1'], password='11111111')         
        self.assertTrue(ret, '查找人口失败')
        
        ret = ShiYouRenKouIntf.check_HuJiPopulation(checkParam_13, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser1'], password='11111111')         
        self.assertFalse(ret, '转移的人口在当前网格中依然存在，转移失败')
        
        pass 


    def testLiuDongPopulationAdd_01(self):
        """实有人口>流动人口信息新增"""
        HuJiParam_01 = copy.deepcopy(ShiYouRenKouPara.populationObject) 
        HuJiParam_01['mode']='add'
        HuJiParam_01['population.organization.id'] = orgInit['DftWangGeOrgId']
        HuJiParam_01['population.organization.orgName'] = orgInit['DftWangGeOrg']
        HuJiParam_01['population.idCardNo'] = '111111111110001'
        HuJiParam_01['population.name'] = 'test2'
        HuJiParam_01['population.isHaveHouse1'] = 'null'         
        responseDict = ShiYouRenKouIntf.add_HuJiRenKou(HuJiRenKouDict=HuJiParam_01, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口失败') 
     
        LiuDongParam_01 = copy.deepcopy(ShiYouRenKouPara.populationObject) 
        LiuDongParam_01['population.organization.id'] = orgInit['DftWangGeOrgId']
        LiuDongParam_01['population.actualPopulationType'] = 'floatingPopulation'
        LiuDongParam_01['population.organization.orgName'] = orgInit['DftWangGeOrg']
        LiuDongParam_01['population.idCardNo'] = HuJiParam_01['population.idCardNo']
        LiuDongParam_01['population.name'] = 'test01'
        LiuDongParam_01['population.isHaveHouse1'] = 'null'           
        
        LiuParam_01 = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)     
        LiuParam_01['idCardNo'] = LiuDongParam_01['population.idCardNo']
        ret_01 = ShiYouRenKouIntf.check_housePopulation(LiuParam_01, orgId=LiuDongParam_01['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111') 
        if ret_01 is True:        
            Log.LogOutput(LogLevel.DEBUG, "当前实有人口中存在该id人口信息,请重新输入id信息")  
            LiuDongParam_01['population.idCardNo'] = '111111111110011'    
            responseDict = ShiYouRenKouIntf.add_LiuDongRenKou(LiuDongRenKouDict=LiuDongParam_01, username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增流动人口失败')  
            LiuParam_01['idCardNo'] = LiuDongParam_01['population.idCardNo']     
            LiuParam_01['name'] = LiuDongParam_01['population.name'] 
            ret = ShiYouRenKouIntf.check_LiuDongpopulation(LiuParam_01, orgId=LiuDongParam_01['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
            self.assertTrue(ret, '查找流动人口失败')        
        else:               
            responseDict = ShiYouRenKouIntf.add_LiuDongRenKou(LiuDongRenKouDict=LiuDongParam_01, username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增流动人口失败')       
            LiuParam_01['name'] = LiuDongParam_01['population.name'] 
            ret = ShiYouRenKouIntf.check_LiuDongpopulation(LiuParam_01, orgId=LiuDongParam_01['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
            self.assertTrue(ret, '查找流动人口失败')  
        #补充修改功能
#         print responseDict.text
        updPara=copy.deepcopy(ShiYouRenKouPara.populationObject)
        updPara['mode']='edit'
        updPara['population.id']=json.loads(responseDict.text)['id']
        updPara['population.organization.id']=LiuDongParam_01['population.organization.id']
        updPara['population.actualPopulationType']=LiuDongParam_01['population.actualPopulationType'] 
        updPara['population.organization.orgName']=LiuDongParam_01['population.organization.orgName']
        updPara['population.idCardNo']=LiuDongParam_01['population.idCardNo']
        updPara['population.name']=LiuDongParam_01['population.name']+'修改'
        updPara['population.isHaveHouse1']='null'
        res1=ShiYouRenKouIntf.upd_LiuDongRenKou(para=updPara)
        self.assertTrue(res1.result, '修改流动人口失败')
        #检查修改功能
        LiuParam_01['name']=updPara['population.name']
        ret1 = ShiYouRenKouIntf.check_LiuDongpopulation(LiuParam_01, orgId=LiuDongParam_01['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret1, '查找流动人口失败')
        pass


    def testLiuDongPopulationSearch_01(self):
        '''实有人口-流动人口快速搜索、高级查询'''
        #新增流动人口
        LiuDongParam_01 = copy.deepcopy(ShiYouRenKouPara.populationObject) 
        LiuDongParam_01['population.organization.id'] = orgInit['DftWangGeOrgId']
        LiuDongParam_01['population.actualPopulationType'] = 'floatingPopulation'
        LiuDongParam_01['population.organization.orgName'] = orgInit['DftWangGeOrg']
        LiuDongParam_01['population.idCardNo'] = '111111111111111'
        LiuDongParam_01['population.name'] = 'test'+createRandomString()
        LiuDongParam_01['population.isHaveHouse1'] = 'null'
        LiuDongParam_01['population.nativePlaceAddress']='户籍详址'+createRandomString()
        LiuDongParam_01['population.usedName']='别名'+createRandomString()
        #新增两条流动人口
        response1 = ShiYouRenKouIntf.add_LiuDongRenKou(LiuDongRenKouDict=LiuDongParam_01, username=userInit['DftWangGeUser'], password='11111111')
#         print response1.text
        self.assertTrue(response1.result, '新增流动人口失败')
        LiuDongParam_02=copy.deepcopy(LiuDongParam_01)
        LiuDongParam_02['population.idCardNo'] = '111111111111112'
        LiuDongParam_02['population.name'] = 'test'+createRandomString()
        LiuDongParam_02['population.nativePlaceAddress']='户籍详址'+createRandomString()
        LiuDongParam_02['population.usedName']='别名'+createRandomString()
        response2 = ShiYouRenKouIntf.add_LiuDongRenKou(LiuDongRenKouDict=LiuDongParam_02, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(response2.result, '新增流动人口失败')        
        #姓名快捷搜索
        searchPara1=copy.deepcopy(ShiYouRenKouPara.kuaiSuSouSuo)
        searchPara1['organizationId']=orgInit['DftWangGeOrgId']
        searchPara1['searchFloatingPopulationVo.fastSearchKeyWords']=LiuDongParam_01['population.name']
        checkPara1={'name':LiuDongParam_01['population.name']}
        checkPara2={'name':LiuDongParam_02['population.name']}
        result11=ShiYouRenKouIntf.checkLiuDongSearchList(checkpara=checkPara1,searchpara=searchPara1)
        self.assertTrue(result11, '通过姓名快速查询失败')
        result12=ShiYouRenKouIntf.checkLiuDongSearchList(checkpara=checkPara2,searchpara=searchPara1)
        self.assertFalse(result12,'通过姓名快速查询失败')
        Log.LogOutput( message='通过姓名快速查询验证成功！')
        #身份证快速搜素
        searchPara2=copy.deepcopy(ShiYouRenKouPara.kuaiSuSouSuo)
        searchPara2['organizationId']=orgInit['DftWangGeOrgId']
        searchPara2['searchFloatingPopulationVo.fastSearchKeyWords']=LiuDongParam_01['population.idCardNo']
        result21=ShiYouRenKouIntf.checkLiuDongSearchList(checkpara=checkPara1,searchpara=searchPara2)
        self.assertTrue(result21, '通过身份证快速查询失败')
        result22=ShiYouRenKouIntf.checkLiuDongSearchList(checkpara=checkPara2,searchpara=searchPara2)
        self.assertFalse(result22,'通过身份证快速查询失败')
        Log.LogOutput( message='通过身份证快速查询验证成功！')
        #户籍地详址高级搜索
        searchPara3=copy.deepcopy(ShiYouRenKouPara.kuaiSuSouSuo)
        searchPara3['organizationId']=orgInit['DftWangGeOrgId']
        searchPara3['searchFloatingPopulationVo.nativePlaceAddress']=LiuDongParam_01['population.nativePlaceAddress']
        result31=ShiYouRenKouIntf.checkLiuDongSearchList(checkpara=checkPara1,searchpara=searchPara3)
        self.assertTrue(result31, '通过户籍地址高级查询失败')
        result32=ShiYouRenKouIntf.checkLiuDongSearchList(checkpara=checkPara2,searchpara=searchPara3)
        self.assertFalse(result32,'通过户籍地址高级查询失败')
        Log.LogOutput( message='通过户籍地址高级查询验证成功！')
        #其他地址高级搜索
        searchPara4=copy.deepcopy(ShiYouRenKouPara.kuaiSuSouSuo)
        searchPara4['organizationId']=orgInit['DftWangGeOrgId']
        searchPara4['searchFloatingPopulationVo.usedName']=LiuDongParam_01['population.usedName']
        result41=ShiYouRenKouIntf.checkLiuDongSearchList(checkpara=checkPara1,searchpara=searchPara4)
        self.assertTrue(result41, '通过别名高级查询失败')
        result42=ShiYouRenKouIntf.checkLiuDongSearchList(checkpara=checkPara2,searchpara=searchPara4)
        self.assertFalse(result42,'通过别名高级查询失败')
        Log.LogOutput( message='通过别名高级查询验证成功！')          
        pass
        
    def testLiuDongPopulationDelete_02(self):
        """删除流动人口"""
     
        LiuDongParam_02 = copy.deepcopy(ShiYouRenKouPara.populationObject) 
        LiuDongParam_02['population.organization.id'] = orgInit['DftWangGeOrgId']
        LiuDongParam_02['population.actualPopulationType'] = 'floatingPopulation'
        LiuDongParam_02['population.organization.orgName'] = orgInit['DftWangGeOrg']
        LiuDongParam_02['population.idCardNo'] = '111111111111002'
        LiuDongParam_02['population.name'] = 'test02'
        LiuDongParam_02['population.isHaveHouse1'] = 'null'         
        responseDict = ShiYouRenKouIntf.add_LiuDongRenKou(LiuDongRenKouDict=LiuDongParam_02, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增流动人口失败')         
        
        LiuDongDeleteParam = copy.deepcopy(ShiYouRenKouPara.delLiuDongDict)
        LiuDongDeleteParam['floatingPopulationIds'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from floatingPopulations t where t.idcardno='%s'" % LiuDongParam_02['population.idCardNo'])
        ret = ShiYouRenKouIntf.delete_LiuDongRenKou(LiuDongDeleteParam,username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret.result, '删除流动人口失败') 
                        
        LiuParam_02 = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        LiuParam_02['name'] = LiuDongParam_02['population.name']       
        LiuParam_02['idCardNo'] = LiuDongParam_02['population.idCardNo']
        ret = ShiYouRenKouIntf.check_LiuDongpopulation(LiuParam_02, orgId=LiuDongParam_02['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '已删除人口在列表中依然存在')        
        pass

    def testLiuDongPopulationTransfer_11(self):
        """实有人口>流动人口转为户籍人口"""

        LiuDongParam_11 = copy.deepcopy(ShiYouRenKouPara.populationObject) 
        LiuDongParam_11['population.organization.id'] = orgInit['DftWangGeOrgId']
        LiuDongParam_11['population.actualPopulationType'] = 'floatingPopulation'
        LiuDongParam_11['population.organization.orgName'] = orgInit['DftWangGeOrg']
        LiuDongParam_11['population.idCardNo'] = '111111111111011'
        LiuDongParam_11['population.name'] = 'test11'
        LiuDongParam_11['population.isHaveHouse1'] = 'null'         
        responseDict = ShiYouRenKouIntf.add_LiuDongRenKou(LiuDongRenKouDict=LiuDongParam_11, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增流动人口失败') 
        
        LiuParam_11 = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        LiuParam_11['name'] = LiuDongParam_11['population.name']       
        LiuParam_11['idCardNo'] = LiuDongParam_11['population.idCardNo']
        ret = ShiYouRenKouIntf.check_LiuDongpopulation(LiuParam_11, orgId=LiuDongParam_11['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找流动人口失败')
        
        LiuDongTransferParam = copy.deepcopy(ShiYouRenKouPara.populationObject)
        LiuDongTransferParam['population.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from floatingPopulations t where t.idcardno='%s' and t.name='%s'" % (LiuDongParam_11['population.idCardNo'],LiuDongParam_11['population.name']))
        ret = ShiYouRenKouIntf.transfer_LiuDongRenKou(LiuDongTransferParam,username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret.result, '转为户籍人口失败') 
        
        ret = ShiYouRenKouIntf.check_LiuDongpopulation(LiuParam_11, orgId=LiuDongParam_11['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '已转移人口在列表中依然存在')
        
        checkParam_11 = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)  
        checkParam_11['name'] = LiuDongParam_11['population.name']   
        checkParam_11['idCardNo'] = LiuDongParam_11['population.idCardNo']
        ret = ShiYouRenKouIntf.check_HuJiPopulation(checkParam_11, orgId=LiuDongParam_11['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找人口失败')
        
        pass   

    def testLiuDongPopulationImportAndDownLoad_26(self):
        """实有人口>流动人口信息 导入/导出"""
         
        importHuJiparam = copy.deepcopy(ShiYouRenKouPara.data)
        importHuJiparam['dataType']='floatingPopulationData'
        importHuJiparam['templates']='FLOATINGPOPULATION'
        files = {'upload': ('test.xls', open('C:/autotest_file/importLiuDongPopulation.xls', 'rb'),'applicationnd.ms-excel')}
        ret = ShiYouRenKouIntf.import_RenKou(importHuJiparam, files=files,username=userInit['DftWangGeUser'], password='11111111')         
        
        param = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        param['name'] = '流动导入测试'      
        param['idCardNo'] = '111111111111170'
        ret = ShiYouRenKouIntf.check_LiuDongpopulation(param, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找流动人口失败') 
                                
        downLoadHuJiparam = copy.deepcopy(ShiYouRenKouPara.dlLiuDongData)
        downLoadHuJiparam['organizationId']=orgInit['DftWangGeOrgId']
        response = ShiYouRenKouIntf.downLoad_LiuDongRenKou(downLoadHuJiparam, username=userInit['DftWangGeUser'], password='11111111')         
        with open("C:/autotest_file/downLoadLiuDongPopulation.xls", "wb") as code:
            code.write(response.content)
            
        ret = CommonUtil.checkExcelCellValue(param['name'], 'downLoadLiuDongPopulation.xls','流动人口清单', 'A4')          
        self.assertTrue(ret, '导出失败')
                         
        pass

    def testWeiLuoHuPopulationAdd_01(self):
        """实有人口>未落户人口新增"""
     
        WeiLuoHuParam_01 = copy.deepcopy(ShiYouRenKouPara.unsettledPopulationObject) 
        WeiLuoHuParam_01['mode'] = 'success'
        WeiLuoHuParam_01['ownerOrg.id'] = orgInit['DftWangGeOrgId']
        WeiLuoHuParam_01['unsettledPopulation.organization.id'] = orgInit['DftWangGeOrgId']
        WeiLuoHuParam_01['unsettledPopulation.organization.orgName'] = orgInit['DftWangGeOrg']
        WeiLuoHuParam_01['unsettledPopulation.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        WeiLuoHuParam_01['unsettledPopulation.idCardNo'] = '111111111110001'
        WeiLuoHuParam_01['unsettledPopulation.name'] = 'test001'+createRandomString()
        WeiLuoHuParam_01['unsettledPopulation.isHaveHouse1'] = 'null'         
        responseDict = ShiYouRenKouIntf.add_WeiLuoHuRenKou(WeiLuoHuRenKouDict=WeiLuoHuParam_01, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增未落户人口失败')        
        
        WeiParam_01= copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        WeiParam_01['name'] = WeiLuoHuParam_01['unsettledPopulation.name']     
        WeiParam_01['idCardNo'] = WeiLuoHuParam_01['unsettledPopulation.idCardNo']
        ret = ShiYouRenKouIntf.check_WeiLuoHupopulation(WeiParam_01, orgId=WeiLuoHuParam_01['unsettledPopulation.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找未落户人口失败')    
        
        #补充修改功能
#         print responseDict.text
        WeiLuoHuParam_01['mode']='edit'
        WeiLuoHuParam_01['unsettledPopulation.id']=json.loads(responseDict.text)['id']
        WeiLuoHuParam_01['unsettledPopulation.idCardNo']='111111111110002'
        WeiLuoHuParam_01['unsettledPopulation.name']='test002'+createRandomString()
        #新增、修改时用的同一个接口
        responseDict = ShiYouRenKouIntf.add_WeiLuoHuRenKou(WeiLuoHuRenKouDict=WeiLuoHuParam_01, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改未落户人口失败')            
        WeiParam_02= copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        WeiParam_02['name'] = WeiLuoHuParam_01['unsettledPopulation.name']     
        WeiParam_02['idCardNo'] = WeiLuoHuParam_01['unsettledPopulation.idCardNo']
        ret = ShiYouRenKouIntf.check_WeiLuoHupopulation(WeiParam_02, orgId=WeiLuoHuParam_01['unsettledPopulation.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找未落户人口失败')
        Log.LogOutput( message='修改未落户人口成功！')          
        pass
    
    def testWeiLuoHuPopulationSearch_01(self):
        """实有人口>未落户人口快速检索、高级查询"""
        #新增两条未落户人员
        WeiLuoHuParam_01 = copy.deepcopy(ShiYouRenKouPara.unsettledPopulationObject) 
        WeiLuoHuParam_01['mode'] = 'success'
        WeiLuoHuParam_01['ownerOrg.id'] = orgInit['DftWangGeOrgId']
        WeiLuoHuParam_01['unsettledPopulation.organization.id'] = orgInit['DftWangGeOrgId']
        WeiLuoHuParam_01['unsettledPopulation.organization.orgName'] = orgInit['DftWangGeOrg']
        WeiLuoHuParam_01['unsettledPopulation.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        WeiLuoHuParam_01['unsettledPopulation.idCardNo'] = '111111111110001'
        WeiLuoHuParam_01['unsettledPopulation.name'] = 'test001'+createRandomString()
        WeiLuoHuParam_01['unsettledPopulation.isHaveHouse1'] = 'null'     
        WeiLuoHuParam_01['unsettledPopulation.certificateNo']='001'+createRandomString()
        WeiLuoHuParam_01['unsettledPopulation.usedName']='usedname001'+createRandomString()
        responseDict = ShiYouRenKouIntf.add_WeiLuoHuRenKou(WeiLuoHuRenKouDict=WeiLuoHuParam_01, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增未落户人口失败')
        #第二条
        WeiLuoHuParam_02 = copy.deepcopy(ShiYouRenKouPara.unsettledPopulationObject) 
        WeiLuoHuParam_02['mode'] = 'success'
        WeiLuoHuParam_02['ownerOrg.id'] = orgInit['DftWangGeOrgId']
        WeiLuoHuParam_02['unsettledPopulation.organization.id'] = orgInit['DftWangGeOrgId']
        WeiLuoHuParam_02['unsettledPopulation.organization.orgName'] = orgInit['DftWangGeOrg']
        WeiLuoHuParam_02['unsettledPopulation.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        WeiLuoHuParam_02['unsettledPopulation.idCardNo'] = '111111111110002'
        WeiLuoHuParam_02['unsettledPopulation.name'] = 'test001'+createRandomString()
        WeiLuoHuParam_02['unsettledPopulation.isHaveHouse1'] = 'null'   
        WeiLuoHuParam_02['unsettledPopulation.certificateNo']='002'+createRandomString()
        WeiLuoHuParam_02['unsettledPopulation.usedName']='usedname002'+createRandomString()      
        responseDict = ShiYouRenKouIntf.add_WeiLuoHuRenKou(WeiLuoHuRenKouDict=WeiLuoHuParam_02, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增未落户人口失败')     
        #根据姓名快速查询
        searchPara1=copy.deepcopy(ShiYouRenKouPara.weiLuoHuChaXun)
        searchPara1['orgId']=orgInit['DftWangGeOrgId']
        searchPara1['unsettledPopulationCondition.fastSearchKeyWords']= WeiLuoHuParam_01['unsettledPopulation.name']
        checkPara1={'name':WeiLuoHuParam_01['unsettledPopulation.name']}
        checkPara2={'name':WeiLuoHuParam_02['unsettledPopulation.name']}
        result11=ShiYouRenKouIntf.checkWeiLuoHuFastSearchList(checkpara=checkPara1,searchpara=searchPara1)
        self.assertTrue(result11, '通过姓名快速查询失败')
        result12=ShiYouRenKouIntf.checkWeiLuoHuFastSearchList(checkpara=checkPara2,searchpara=searchPara1)
        self.assertFalse(result12,'通过姓名快速查询失败')
        Log.LogOutput( message='通过姓名快速查询验证成功！')
        #根据身份证快速查询
        searchPara2=copy.deepcopy(ShiYouRenKouPara.weiLuoHuChaXun)
        searchPara2['orgId']=orgInit['DftWangGeOrgId']
        searchPara2['unsettledPopulationCondition.fastSearchKeyWords']= WeiLuoHuParam_01['unsettledPopulation.idCardNo'] 
        result21=ShiYouRenKouIntf.checkWeiLuoHuFastSearchList(checkpara=checkPara1,searchpara=searchPara2)
        self.assertTrue(result21, '通过身份证快速查询失败')
        result22=ShiYouRenKouIntf.checkWeiLuoHuFastSearchList(checkpara=checkPara2,searchpara=searchPara2)
        self.assertFalse(result22,'通过身份证快速查询失败')
        Log.LogOutput( message='通过身份证快速查询验证成功！') 
        #高级搜索,通过曾用名搜索  
        searchPara3=copy.deepcopy(ShiYouRenKouPara.weiLuoHuGaoJiChaXun)
        searchPara3['orgId']=orgInit['DftWangGeOrgId']
        searchPara3['unsettledPopulationCondition.usedName']= WeiLuoHuParam_01['unsettledPopulation.usedName']
        result31=ShiYouRenKouIntf.checkWeiLuoHuSeniorSearchList(checkpara=checkPara1,searchpara=searchPara3)
        self.assertTrue(result31, '通过曾用名高级查询失败')
        result32=ShiYouRenKouIntf.checkWeiLuoHuSeniorSearchList(checkpara=checkPara2,searchpara=searchPara3)
        self.assertFalse(result32,'通过曾用名高级查询失败')
        Log.LogOutput( message='通过曾用名高级查询验证成功！')         
        #高级搜索,通过持证编号搜索
        searchPara4=copy.deepcopy(ShiYouRenKouPara.weiLuoHuGaoJiChaXun)
        searchPara4['orgId']=orgInit['DftWangGeOrgId']
        searchPara4['unsettledPopulationCondition.certificateNo']= WeiLuoHuParam_01['unsettledPopulation.certificateNo']
        result41=ShiYouRenKouIntf.checkWeiLuoHuSeniorSearchList(checkpara=checkPara1,searchpara=searchPara4)
        self.assertTrue(result41, '通过持证编号高级查询失败')
        result42=ShiYouRenKouIntf.checkWeiLuoHuSeniorSearchList(checkpara=checkPara2,searchpara=searchPara4)
        self.assertFalse(result42,'通过持证编号高级查询失败')
        Log.LogOutput( message='通过持证编号高级查询验证成功！')            
        pass
    def testWeiLuoHuPopulationDetele_02(self):
        """删除未落户人口"""
     
        WeiLuoHuParam_02 = copy.deepcopy(ShiYouRenKouPara.unsettledPopulationObject) 
        WeiLuoHuParam_02['mode'] = 'success'
        WeiLuoHuParam_02['ownerOrg.id'] = orgInit['DftWangGeOrgId']
        WeiLuoHuParam_02['unsettledPopulation.organization.id'] = orgInit['DftWangGeOrgId']
        WeiLuoHuParam_02['unsettledPopulation.organization.orgName'] = orgInit['DftWangGeOrg']
        WeiLuoHuParam_02['unsettledPopulation.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        WeiLuoHuParam_02['unsettledPopulation.idCardNo'] = '111111111110002'
        WeiLuoHuParam_02['unsettledPopulation.name'] = 'test002'
        WeiLuoHuParam_02['unsettledPopulation.isHaveHouse1'] = 'null'         
        responseDict = ShiYouRenKouIntf.add_WeiLuoHuRenKou(WeiLuoHuRenKouDict=WeiLuoHuParam_02, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增未落户人口失败')        
         
        WeiDeleteParam_02 = copy.deepcopy(ShiYouRenKouPara.delWeiLuoHuDict)
        WeiDeleteParam_02['unsettledPopulationIds'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from unsettledPopulations t where t.name='%s'and t.idCardNo='%s'" % (WeiLuoHuParam_02['unsettledPopulation.name'],WeiLuoHuParam_02['unsettledPopulation.idCardNo'])                                                               )
        ret = ShiYouRenKouIntf.delete_WeiLuoHuRenKou(WeiDeleteParam_02,username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret.result, '删除未落户人口失败') 
                           
        WeiParam_02 = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        WeiParam_02['name'] = WeiLuoHuParam_02['unsettledPopulation.name']     
        WeiParam_02['idCardNo'] = WeiLuoHuParam_02['unsettledPopulation.idCardNo']
        ret = ShiYouRenKouIntf.check_WeiLuoHupopulation(WeiParam_02, orgId=WeiLuoHuParam_02['unsettledPopulation.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '已删除人口在列表中依然存在')        
        pass

    def testWeiLuoHuPopulationTransfer_12(self):
        """实有人口>未落户人口转为户籍人口"""

        WeiLuoHuParam_12 = copy.deepcopy(ShiYouRenKouPara.unsettledPopulationObject) 
        WeiLuoHuParam_12['mode'] = 'success'
        WeiLuoHuParam_12['ownerOrg.id'] = orgInit['DftWangGeOrgId']
        WeiLuoHuParam_12['unsettledPopulation.organization.id'] = orgInit['DftWangGeOrgId']
        WeiLuoHuParam_12['unsettledPopulation.organization.orgName'] = orgInit['DftWangGeOrg']
        WeiLuoHuParam_12['unsettledPopulation.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        WeiLuoHuParam_12['unsettledPopulation.idCardNo'] = '111111111110012'
        WeiLuoHuParam_12['unsettledPopulation.name'] = 'test12'
        WeiLuoHuParam_12['unsettledPopulation.isHaveHouse1'] = 'null'         
        responseDict = ShiYouRenKouIntf.add_WeiLuoHuRenKou(WeiLuoHuRenKouDict=WeiLuoHuParam_12, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增未落户人口失败') 
        
        WeiParam_12 = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        WeiParam_12['name'] = WeiLuoHuParam_12['unsettledPopulation.name']     
        WeiParam_12['idCardNo'] = WeiLuoHuParam_12['unsettledPopulation.idCardNo']
        ret = ShiYouRenKouIntf.check_WeiLuoHupopulation(WeiParam_12, orgId=WeiLuoHuParam_12['unsettledPopulation.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找未落户人口失败')
        
        WeiTransferParam = copy.deepcopy(ShiYouRenKouPara.populationObject) 
        WeiTransferParam['mode']='add'
        WeiTransferParam['population.organization.id'] = orgInit['DftWangGeOrgId']
        WeiTransferParam['population.organization.orgName'] = orgInit['DftWangGeOrg']
        WeiTransferParam['population.idCardNo'] = WeiLuoHuParam_12['unsettledPopulation.idCardNo']
        WeiTransferParam['population.name'] = WeiLuoHuParam_12['unsettledPopulation.name']
        WeiTransferParam['population.isHaveHouse1'] = WeiLuoHuParam_12['unsettledPopulation.isHaveHouse1']
        ret = ShiYouRenKouIntf.transfer_WeiLuoHuRenKou(WeiTransferParam,username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret.result, '转为落户人口失败') 
        
        WeiDeleteParam_12 = copy.deepcopy(ShiYouRenKouPara.delWeiLuoHuDict)
        WeiDeleteParam_12['unsettledPopulationIds'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from unsettledPopulations t where t.name='%s'and t.idCardNo='%s'" % (WeiLuoHuParam_12['unsettledPopulation.name'],WeiLuoHuParam_12['unsettledPopulation.idCardNo'])                                                               )
        ret = ShiYouRenKouIntf.delete_WeiLuoHuRenKou(WeiDeleteParam_12,username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret.result, '删除未落户人口失败') 
             
        ret = ShiYouRenKouIntf.check_WeiLuoHupopulation(WeiParam_12, orgId=WeiLuoHuParam_12['unsettledPopulation.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '已转移人口在列表中依然存在')
        
        checkParam_12 = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)  
        checkParam_12['name'] = WeiLuoHuParam_12['unsettledPopulation.name']   
        checkParam_12['idCardNo'] = WeiLuoHuParam_12['unsettledPopulation.idCardNo']
        ret = ShiYouRenKouIntf.check_HuJiPopulation(checkParam_12, orgId=WeiLuoHuParam_12['unsettledPopulation.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找人口失败')
        
        pass   

    def testWeiLuoHuPopulationImportAndDownLoad_27(self):
        """实有人口>未落户人口信息 导入/导出"""
         
        importHuJiparam = copy.deepcopy(ShiYouRenKouPara.data)
        importHuJiparam['dataType']='unsettledPopulationData'
        importHuJiparam['templates']='UNSETTLEDPOPULATION'
        files = {'upload': ('test.xls', open('C:/autotest_file/importWeiLuoHuPopulation.xls', 'rb'),'applicationnd.ms-excel')}
        ret = ShiYouRenKouIntf.import_RenKou(importHuJiparam, files=files,username=userInit['DftWangGeUser'], password='11111111')         
        
        param= copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        param['name'] = '未落户导入测试'     
        param['idCardNo'] = '111111111111171' 
        ret = ShiYouRenKouIntf.check_WeiLuoHupopulation(param, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找未落户人口失败')
                                
        downLoadHuJiparam = copy.deepcopy(ShiYouRenKouPara.dlWeiLuoHuData)
        downLoadHuJiparam['orgId']=orgInit['DftWangGeOrgId']
        response = ShiYouRenKouIntf.downLoad_WeiLuoHuRenKou(downLoadHuJiparam, username=userInit['DftWangGeUser'], password='11111111')         
        with open("C:/autotest_file/downLoadWeiLuoHuPopulation.xls", "wb") as code:
            code.write(response.content)
            
        ret = CommonUtil.checkExcelCellValue(param['name'], 'downLoadWeiLuoHuPopulation.xls','未落户人口清单', 'A4')          
        self.assertTrue(ret, '导出失败')
                         
        pass
    

    def testJingWaiPopulationAdd_01(self):
        """实有人口>境外人员信息新增"""
     
        JingWaiParam_01 = copy.deepcopy(ShiYouRenKouPara.overseaPopulationObject) 
        JingWaiParam_01['mode'] = 'success'
        JingWaiParam_01['overseaPersonnel.organization.id'] = orgInit['DftWangGeOrgId']
        JingWaiParam_01['overseaPersonnel.englishName'] = 'www'
        JingWaiParam_01['overseaPersonnel.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        JingWaiParam_01['overseaPersonnel.certificateType.id'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from propertydicts t where t.displayname='旅游证'" )
        JingWaiParam_01['overseaPersonnel.certificateNo'] = '343'
        JingWaiParam_01['overseaPersonnel.isHaveHouse1'] = 'null'         
        responseDict = ShiYouRenKouIntf.add_JingWaiRenKou(JingWaiRenKouDict=JingWaiParam_01, username=userInit['DftWangGeUser'], password='11111111') 
        self.assertTrue(responseDict.result, '新增境外人口失败')        
        
        JingParam_01 = copy.deepcopy(ShiYouRenKouPara.checkJingWaiOrgDict)
        JingParam_01['englishName'] = JingWaiParam_01['overseaPersonnel.englishName']     
        JingParam_01['certificateType'] = {"id":JingWaiParam_01['overseaPersonnel.certificateType.id']}  
        JingParam_01['certificateNo'] = JingWaiParam_01['overseaPersonnel.certificateNo']
        ret = ShiYouRenKouIntf.check_JingWaipopulation(JingParam_01, orgId=JingWaiParam_01['overseaPersonnel.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找境外人口失败')  
        
        #补充修改用例
        JingWaiParam_01['overseaPersonnel.id']=json.loads(responseDict.text)['id']
        JingWaiParam_01['overseaPersonnel.englishName']='upd'+createRandomString()
        JingWaiParam_01['certificateType']=CommonIntf.getDbQueryResult(dbCommand="select t.id from propertydicts t where t.displayname='港澳出入证'" )
        JingWaiParam_01['certificateNo']='123456'
        #修改境外人员，与新增是同一接口
        responseDict = ShiYouRenKouIntf.add_JingWaiRenKou(JingWaiRenKouDict=JingWaiParam_01, username=userInit['DftWangGeUser'], password='11111111') 
        self.assertTrue(responseDict.result, '修改境外人口失败')
        JingParam_01['englishName'] = JingWaiParam_01['overseaPersonnel.englishName']     
        JingParam_01['certificateType'] = {"id":JingWaiParam_01['overseaPersonnel.certificateType.id']}  
        JingParam_01['certificateNo'] = JingWaiParam_01['overseaPersonnel.certificateNo']
        ret = ShiYouRenKouIntf.check_JingWaipopulation(JingParam_01, orgId=JingWaiParam_01['overseaPersonnel.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找境外人口失败')
        Log.LogOutput( message='境外人员修改成功')  
        pass

    def testJingWaiPopulationSearch_01(self):
        '''境外人员-快速检索、高级查询'''
        #新增两条境外人员
        JingWaiParam_01 = copy.deepcopy(ShiYouRenKouPara.overseaPopulationObject) 
        JingWaiParam_01['mode'] = 'success'
        JingWaiParam_01['overseaPersonnel.organization.id'] = orgInit['DftWangGeOrgId']
        JingWaiParam_01['overseaPersonnel.englishName'] = 'Lucy'
        JingWaiParam_01['overseaPersonnel.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        JingWaiParam_01['overseaPersonnel.certificateType.id'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from propertydicts t where t.displayname='旅游证'" )
        JingWaiParam_01['overseaPersonnel.certificateNo'] = '001'
        JingWaiParam_01['overseaPersonnel.isHaveHouse1'] = 'null'
        JingWaiParam_01['overseaPersonnel.nationality']='美国'
        JingWaiParam_01['overseaPersonnel.name']='张三'
        responseDict = ShiYouRenKouIntf.add_JingWaiRenKou(JingWaiRenKouDict=JingWaiParam_01, username=userInit['DftWangGeUser'], password='11111111') 
        self.assertTrue(responseDict.result, '新增境外人口失败')
        #第二条
        JingWaiParam_02 = copy.deepcopy(ShiYouRenKouPara.overseaPopulationObject) 
        JingWaiParam_02['mode'] = 'success'
        JingWaiParam_02['overseaPersonnel.organization.id'] = orgInit['DftWangGeOrgId']
        JingWaiParam_02['overseaPersonnel.englishName'] = 'Lily'
        JingWaiParam_02['overseaPersonnel.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='女')
        JingWaiParam_02['overseaPersonnel.certificateType.id'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from propertydicts t where t.displayname='护照'" )
        JingWaiParam_02['overseaPersonnel.certificateNo'] = '002'
        JingWaiParam_02['overseaPersonnel.isHaveHouse1'] = 'null'
        JingWaiParam_02['overseaPersonnel.nationality']='英国'
        JingWaiParam_02['overseaPersonnel.name']='李四'
        responseDict = ShiYouRenKouIntf.add_JingWaiRenKou(JingWaiRenKouDict=JingWaiParam_02, username=userInit['DftWangGeUser'], password='11111111') 
        self.assertTrue(responseDict.result, '新增境外人口失败')        
        #英文名快速检索
        searchPara1=copy.deepcopy(ShiYouRenKouPara.jingWaiFastSearch)
        searchPara1['orgId']=orgInit['DftWangGeOrgId']
        searchPara1['searchOverseaPersonnelVo.fastSearchKeyWords']= JingWaiParam_01['overseaPersonnel.englishName']
        checkPara1={'englishName':JingWaiParam_01['overseaPersonnel.englishName']}
        checkPara2={'englishName':JingWaiParam_02['overseaPersonnel.englishName']}
        result11=ShiYouRenKouIntf.checkJingWaiFastSearchList(checkpara=checkPara1,searchpara=searchPara1)
        self.assertTrue(result11, '通过英文名快速查询失败')
        result12=ShiYouRenKouIntf.checkJingWaiFastSearchList(checkpara=checkPara2,searchpara=searchPara1)
        self.assertFalse(result12,'通过英文名快速查询失败')
        Log.LogOutput( message='通过英文名快速查询验证成功！')
        #根据证件号码快速查询
        searchPara2=copy.deepcopy(ShiYouRenKouPara.weiLuoHuChaXun)
        searchPara2['orgId']=orgInit['DftWangGeOrgId']
        searchPara2['searchOverseaPersonnelVo.fastSearchKeyWords']= JingWaiParam_01['overseaPersonnel.certificateNo'] 
        result21=ShiYouRenKouIntf.checkJingWaiFastSearchList(checkpara=checkPara1,searchpara=searchPara2)
        self.assertTrue(result21, '通过证件号码快速查询失败')
        result22=ShiYouRenKouIntf.checkJingWaiFastSearchList(checkpara=checkPara2,searchpara=searchPara2)
        self.assertFalse(result22,'通过证件号码快速查询失败')
        Log.LogOutput( message='通过证件号码快速查询验证成功！')  
        #境外高级搜索
        #高级搜索,通过中文名搜索  
        searchPara3=copy.deepcopy(ShiYouRenKouPara.weiLuoHuGaoJiChaXun)
        searchPara3['orgId']=orgInit['DftWangGeOrgId']
        searchPara3['searchOverseaPersonnelVo.chineseName']= JingWaiParam_01['overseaPersonnel.name']
        result31=ShiYouRenKouIntf.checkJingWaiSeniorSearchList(checkpara=checkPara1,searchpara=searchPara3)
        self.assertTrue(result31, '通过中文名高级查询失败')
        result32=ShiYouRenKouIntf.checkJingWaiSeniorSearchList(checkpara=checkPara2,searchpara=searchPara3)
        self.assertFalse(result32,'通过中文名高级查询失败')
        Log.LogOutput( message='通过中文名高级查询验证成功！')         
        #高级搜索,通过国籍搜索
        searchPara4=copy.deepcopy(ShiYouRenKouPara.weiLuoHuGaoJiChaXun)
        searchPara4['orgId']=orgInit['DftWangGeOrgId']
        searchPara4['searchOverseaPersonnelVo.nationality']= JingWaiParam_01['overseaPersonnel.nationality']
        result41=ShiYouRenKouIntf.checkJingWaiSeniorSearchList(checkpara=checkPara1,searchpara=searchPara4)
        self.assertTrue(result41, '通过国籍高级查询失败')
        result42=ShiYouRenKouIntf.checkJingWaiSeniorSearchList(checkpara=checkPara2,searchpara=searchPara4)
        self.assertFalse(result42,'通过国籍高级查询失败')
        Log.LogOutput( message='通过国籍高级查询验证成功！')        
        pass
    def testJingWaiPopulationDetele_02(self):
        """境外人口信息删除"""
     
        JingWaiParam_02 = copy.deepcopy(ShiYouRenKouPara.overseaPopulationObject) 
        JingWaiParam_02['mode'] = 'success'
        JingWaiParam_02['overseaPersonnel.organization.id'] = orgInit['DftWangGeOrgId']
        JingWaiParam_02['overseaPersonnel.englishName'] = 'ddd'
        JingWaiParam_02['overseaPersonnel.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        JingWaiParam_02['overseaPersonnel.certificateType.id'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from propertydicts t where t.displayname='旅游证'" )
        JingWaiParam_02['overseaPersonnel.certificateNo'] = '12345'
        JingWaiParam_02['overseaPersonnel.isHaveHouse1'] = 'null'         
        responseDict = ShiYouRenKouIntf.add_JingWaiRenKou(JingWaiRenKouDict=JingWaiParam_02, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增境外人口失败')        
                 
        JingdeleteParam = copy.deepcopy(ShiYouRenKouPara.delJingWaiDict)
        JingdeleteParam['deleteIds'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from overseaPersonnel t where t.certificatetype='%s'and t.certificateno='%s'" % (JingWaiParam_02['overseaPersonnel.certificateType.id'],JingWaiParam_02['overseaPersonnel.certificateNo'])                                                              )
        ret = ShiYouRenKouIntf.delete_JingWaiRenKou(JingdeleteParam,username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret.result, '删除境外人口失败') 
           
        Jingparam_02 = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        Jingparam_02['englishName'] = JingWaiParam_02['overseaPersonnel.englishName']     
        Jingparam_02['certificateType'] = {"displaySeq":0,"id":int(JingWaiParam_02['overseaPersonnel.certificateType.id']),"internalId":0}  
        Jingparam_02['idCardNo'] = JingWaiParam_02['overseaPersonnel.certificateNo']
        ret = ShiYouRenKouIntf.check_JingWaipopulation(Jingparam_02, orgId=JingWaiParam_02['overseaPersonnel.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '已删除人口在列表中依然存在')        
        pass

    def testJingWaiPopulationImportAndDownLoad_28(self):
        """实有人口>境外人口信息 导入/导出"""
         
        importHuJiparam = copy.deepcopy(ShiYouRenKouPara.data)
        importHuJiparam['dataType']='overseaPersonnel'
        importHuJiparam['templates']='OVERSEASTAFF'
        files = {'upload': ('test.xls', open('C:/autotest_file/importJingWaiPopulation.xls', 'rb'),'applicationnd.ms-excel')}
        ret = ShiYouRenKouIntf.import_RenKou(importHuJiparam, files=files,username=userInit['DftWangGeUser'], password='11111111')         
        
        param = copy.deepcopy(ShiYouRenKouPara.checkJingWaiOrgDict)
        param['englishName'] = 'test'        
        param['certificateNo'] = '111'
        ret = ShiYouRenKouIntf.check_JingWaipopulation(param, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找境外人口失败')        

        downLoadHuJiparam = copy.deepcopy(ShiYouRenKouPara.dlJingWaiHuData)
        downLoadHuJiparam['orgId']=orgInit['DftWangGeOrgId']
        response = ShiYouRenKouIntf.downLoad_JingWaiRenKou(downLoadHuJiparam, username=userInit['DftWangGeUser'], password='11111111')         
        with open("C:/autotest_file/downLoadJingWaiPopulation.xls", "wb") as code:
            code.write(response.content)
            
        ret = CommonUtil.checkExcelCellValue(param['englishName'], 'downLoadJingWaiPopulation.xls','境外人员清单', 'A4')          
        self.assertTrue(ret, '导出失败')
                         
        pass


    def testHouseFamilyAdd_14(self):
        """实有人口>户籍家庭信息新增"""

        HuJiParam_14 = copy.deepcopy(ShiYouRenKouPara.populationObject) 
        HuJiParam_14['mode']='add'
        HuJiParam_14['population.organization.id'] = orgInit['DftWangGeOrgId']
        HuJiParam_14['population.organization.orgName'] = orgInit['DftWangGeOrg']
        HuJiParam_14['population.idCardNo'] = '111111111110014'
        HuJiParam_14['population.name'] = 'test14'
        HuJiParam_14['population.isHaveHouse1'] = 'null'         
        responseDict = ShiYouRenKouIntf.add_HuJiRenKou(HuJiRenKouDict=HuJiParam_14, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口失败') 
             
        familyParam_14 = copy.deepcopy(ShiYouRenKouPara.houseFamilyObject) 
        familyParam_14['newHouseHold.accountNumber'] = '01%s'%CommonUtil.createRandomString()
        familyParam_14['newHouseHold.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from householdstaffs t where t.idcardno='%s' and t.name='%s'" % (HuJiParam_14['population.idCardNo'],HuJiParam_14['population.name']))
        familyParam_14['orgId'] = HuJiParam_14['population.organization.id']        
        responseDict = ShiYouRenKouIntf.add_houseFamily(houseFamilyDict=familyParam_14, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍家庭失败')        
        
        param_14 = copy.deepcopy(ShiYouRenKouPara.checkHouseFamilyDict)
#         param_14['censusRegisterFamily'] = {"accountNumber":familyParam_14['newHouseHold.accountNumber'],"id":CommonIntf.getDbQueryResult(dbCommand = "select t.id from censusregisterfamilys t where t.accountnumber='%s'"% familyParam_14['newHouseHold.accountNumber'])}    #105.8070
        param_14['censusRegisterFamily'] = {"accountNumber":familyParam_14['newHouseHold.accountNumber'],"id":CommonIntf.getDbQueryResult(dbCommand = "select t.id from censusregisterfamilys t where t.accountnumber='%s'"% familyParam_14['newHouseHold.accountNumber']),"viewdataList":[]}   #136.8080 
        param_14['id'] = familyParam_14['newHouseHold.id']
        ret = ShiYouRenKouIntf.check_houseFamily(param_14, orgId=HuJiParam_14['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找户籍家庭失败')
        pass

    def testHouseFamilyDelete_14(self):
        """户籍家庭 批量删除"""

        HuJiParam_14 = copy.deepcopy(ShiYouRenKouPara.populationObject) 
        HuJiParam_14['mode']='add'
        HuJiParam_14['population.organization.id'] = orgInit['DftWangGeOrgId']
        HuJiParam_14['population.organization.orgName'] = orgInit['DftWangGeOrg']
        HuJiParam_14['population.idCardNo'] = '111111111110014'
        HuJiParam_14['population.name'] = 'test14'
        HuJiParam_14['population.isHaveHouse1'] = 'null'         
        responseDict = ShiYouRenKouIntf.add_HuJiRenKou(HuJiRenKouDict=HuJiParam_14, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口失败') 
        
        newHuJiParam_14 = copy.deepcopy(ShiYouRenKouPara.populationObject) 
        newHuJiParam_14['mode']='add'
        newHuJiParam_14['population.organization.id'] = orgInit['DftWangGeOrgId']
        newHuJiParam_14['population.organization.orgName'] = orgInit['DftWangGeOrg']
        newHuJiParam_14['population.idCardNo'] = '111111111110114'
        newHuJiParam_14['population.name'] = 'test114'
        newHuJiParam_14['population.isHaveHouse1'] = 'null'         
        responseDict = ShiYouRenKouIntf.add_HuJiRenKou(HuJiRenKouDict=newHuJiParam_14, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口失败') 
             
        familyParam_14 = copy.deepcopy(ShiYouRenKouPara.houseFamilyObject) 
        familyParam_14['newHouseHold.accountNumber'] = '01%s'%CommonUtil.createRandomString()
        familyParam_14['newHouseHold.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from householdstaffs t where t.idcardno='%s' and t.name='%s'" % (HuJiParam_14['population.idCardNo'],HuJiParam_14['population.name']))
        familyParam_14['orgId'] = HuJiParam_14['population.organization.id']        
        responseDict = ShiYouRenKouIntf.add_houseFamily(houseFamilyDict=familyParam_14, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍家庭失败')    
        
        newFamilyParam_14 = copy.deepcopy(ShiYouRenKouPara.houseFamilyObject) 
        newFamilyParam_14['newHouseHold.accountNumber'] = '01%s'%CommonUtil.createRandomString()
        newFamilyParam_14['newHouseHold.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from householdstaffs t where t.idcardno='%s' and t.name='%s'" % (newHuJiParam_14['population.idCardNo'],newHuJiParam_14['population.name']))
        newFamilyParam_14['orgId'] = newHuJiParam_14['population.organization.id']        
        responseDict = ShiYouRenKouIntf.add_houseFamily(houseFamilyDict=newFamilyParam_14, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍家庭失败') 
        
        familyId_14 = copy.deepcopy(ShiYouRenKouPara.familyObject) 
        familyId_14['familyid'] = CommonIntf.getDbQueryResult(dbCommand = "select t.familyid from householdstaffs t where t.idcardno='%s'" % HuJiParam_14['population.idCardNo'])

        newFamilyId_14 = copy.deepcopy(ShiYouRenKouPara.familyObject) 
        newFamilyId_14['familyid'] = CommonIntf.getDbQueryResult(dbCommand = "select t.familyid from householdstaffs t where t.idcardno='%s'" % newHuJiParam_14['population.idCardNo'])

        
    #有成员的户籍家庭不可以删除，先删除户籍人口
        deleteParam = copy.deepcopy(ShiYouRenKouPara.delHuJiDict)
        deleteParam['householdStaffVo.idStr'] = str(CommonIntf.getDbQueryResult(dbCommand = "select t.id from householdstaffs t where t.idcardno='%s'" % HuJiParam_14['population.idCardNo']))+','+str(CommonIntf.getDbQueryResult(dbCommand = "select t.id from householdstaffs t where t.idcardno='%s'" % newHuJiParam_14['population.idCardNo']))
        ret = ShiYouRenKouIntf.delete_HuJiRenKou(deleteParam,username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret.result, '删除户籍人口失败')
        
        deleteFamilyParam_14 = copy.deepcopy(ShiYouRenKouPara.deleteFamilyObject) 
        deleteFamilyParam_14['ids'] =  str(familyId_14['familyid'])+','+str(newFamilyId_14['familyid'])     
        responseDict = ShiYouRenKouIntf.delete_houseFamily(houseFamilyDict=deleteFamilyParam_14, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍家庭失败')    
        
        param_14 = copy.deepcopy(ShiYouRenKouPara.checkHouseFamilyDict)
        param_14['censusRegisterFamily'] = {"accountNumber":familyParam_14['newHouseHold.accountNumber'],"id":CommonIntf.getDbQueryResult(dbCommand = "select t.id from censusregisterfamilys t where t.accountnumber='%s'"% familyParam_14['newHouseHold.accountNumber'])}    
        param_14['id'] = familyParam_14['newHouseHold.id']
        ret = ShiYouRenKouIntf.check_houseFamily(param_14, orgId=HuJiParam_14['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '删除的户籍家庭在列表中依然存在')
        
        param_14['id'] = newFamilyParam_14['newHouseHold.id']
        ret = ShiYouRenKouIntf.check_houseFamily(param_14, orgId=HuJiParam_14['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '删除的户籍家庭在列表中依然存在')
        pass
    
    def testHouseMemberAddRemove_15(self):
        """实有人口>户籍家庭信息中管理成员信息（新增、移除家庭成员）"""

        HuJiParam_15 = copy.deepcopy(ShiYouRenKouPara.populationObject) 
        HuJiParam_15['mode']='add'
        HuJiParam_15['population.organization.id'] = orgInit['DftWangGeOrgId']
        HuJiParam_15['population.organization.orgName'] = orgInit['DftWangGeOrg']
        HuJiParam_15['population.idCardNo'] = '111111111110015'
        HuJiParam_15['population.name'] = 'test15'
        HuJiParam_15['population.isHaveHouse1'] = 'null'         
        responseDict = ShiYouRenKouIntf.add_HuJiRenKou(HuJiRenKouDict=HuJiParam_15, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口失败') 
             
        familyParam_15 = copy.deepcopy(ShiYouRenKouPara.houseFamilyObject) 
        familyParam_15['newHouseHold.accountNumber'] = '01%s'%CommonUtil.createRandomString()
        familyParam_15['newHouseHold.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from householdstaffs t where t.idcardno='%s' and t.name='%s'" % (HuJiParam_15['population.idCardNo'],HuJiParam_15['population.name']))
        familyParam_15['orgId'] = HuJiParam_15['population.organization.id']        
        responseDict = ShiYouRenKouIntf.add_houseFamily(houseFamilyDict=familyParam_15, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍家庭失败')   
        
        NewHuJiParam_15 = copy.deepcopy(ShiYouRenKouPara.populationObject) 
        NewHuJiParam_15['mode']='add'
        NewHuJiParam_15['population.organization.id'] = orgInit['DftWangGeOrgId']
        NewHuJiParam_15['population.organization.orgName'] = orgInit['DftWangGeOrg']
        NewHuJiParam_15['population.idCardNo'] = '111111111110115'
        NewHuJiParam_15['population.name'] = 'test015'
        NewHuJiParam_15['population.isHaveHouse1'] = 'null'         
        responseDict = ShiYouRenKouIntf.add_HuJiRenKou(HuJiRenKouDict=NewHuJiParam_15, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口失败')   
        
        familyMemberParam = copy.deepcopy(ShiYouRenKouPara.houseMemberObject) 
        familyMemberParam['orgId'] = HuJiParam_15['population.organization.id'] 
        familyMemberParam['houseFamilyId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from censusregisterfamilys t where t.accountnumber='%s'"% familyParam_15['newHouseHold.accountNumber'])
        familyMemberParam['householdStaffId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from householdstaffs t where t.idcardno='%s' and t.name='%s'" % (NewHuJiParam_15['population.idCardNo'],NewHuJiParam_15['population.name']))
        familyMemberParam['accountNumber'] = familyParam_15['newHouseHold.accountNumber']              
        responseDict = ShiYouRenKouIntf.add_houseMember(houseFamilyDict=familyMemberParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增家庭成员失败')              
        
        familyParam = copy.deepcopy(ShiYouRenKouPara.checkHouseMemberDict)
        familyParam['idCardNo'] = NewHuJiParam_15['population.idCardNo']     
        familyParam['name'] = NewHuJiParam_15['population.name']
        ret = ShiYouRenKouIntf.check_houseMember(familyParam,orgId=NewHuJiParam_15['population.organization.id'],houseFamilyId=familyMemberParam['houseFamilyId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找家庭成员失败')
        
        deteleMemberParam = copy.deepcopy(ShiYouRenKouPara.houseMemberObject) 
        deteleMemberParam['householdStaffId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from householdstaffs t where t.idcardno='%s' and t.name='%s'" % (NewHuJiParam_15['population.idCardNo'],NewHuJiParam_15['population.name']))
        responseDict = ShiYouRenKouIntf.remove_houseMember(houseFamilyDict=deteleMemberParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '移除家庭成员失败')              
        
        ret = ShiYouRenKouIntf.check_houseMember(familyParam,orgId=NewHuJiParam_15['population.organization.id'],houseFamilyId=familyMemberParam['houseFamilyId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '已移除的家庭成员在列表中依然存在')
        pass

    def testHouseMemberTransfer_16(self):
        """实有人口>户籍家庭信息中管理成员信息（转移家庭成员）"""

        HuJiParam_16 = copy.deepcopy(ShiYouRenKouPara.populationObject) 
        HuJiParam_16['mode']='add'
        HuJiParam_16['population.organization.id'] = orgInit['DftWangGeOrgId']
        HuJiParam_16['population.organization.orgName'] = orgInit['DftWangGeOrg']
        HuJiParam_16['population.idCardNo'] = '111111111110016'
        HuJiParam_16['population.name'] = 'test16'
        HuJiParam_16['population.isHaveHouse1'] = 'null'         
        responseDict = ShiYouRenKouIntf.add_HuJiRenKou(HuJiRenKouDict=HuJiParam_16, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口失败')  
        
        NewHuJiParam_16 = copy.deepcopy(ShiYouRenKouPara.populationObject) 
        NewHuJiParam_16['mode']='add'
        NewHuJiParam_16['population.organization.id'] = orgInit['DftWangGeOrgId']
        NewHuJiParam_16['population.organization.orgName'] = orgInit['DftWangGeOrg']
        NewHuJiParam_16['population.idCardNo'] = '111111111110116'
        NewHuJiParam_16['population.name'] = 'test016'
        NewHuJiParam_16['population.isHaveHouse1'] = 'null'         
        responseDict = ShiYouRenKouIntf.add_HuJiRenKou(HuJiRenKouDict=NewHuJiParam_16, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口失败')   
        
        NewHuJiParam_016 = copy.deepcopy(ShiYouRenKouPara.populationObject) 
        NewHuJiParam_016['mode']='add'
        NewHuJiParam_016['population.organization.id'] = orgInit['DftWangGeOrgId']
        NewHuJiParam_016['population.organization.orgName'] = orgInit['DftWangGeOrg']
        NewHuJiParam_016['population.idCardNo'] = '111111111101116'
        NewHuJiParam_016['population.name'] = 'test0016'
        NewHuJiParam_016['population.isHaveHouse1'] = 'null'         
        responseDict = ShiYouRenKouIntf.add_HuJiRenKou(HuJiRenKouDict=NewHuJiParam_016, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口失败')
        
        familyParam_16 = copy.deepcopy(ShiYouRenKouPara.houseFamilyObject) 
        familyParam_16['newHouseHold.accountNumber'] = '01%s'%CommonUtil.createRandomString()
        familyParam_16['newHouseHold.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from householdstaffs t where t.idcardno='%s' and t.name='%s'" % (HuJiParam_16['population.idCardNo'],HuJiParam_16['population.name']))
        familyParam_16['orgId'] = HuJiParam_16['population.organization.id']        
        responseDict = ShiYouRenKouIntf.add_houseFamily(houseFamilyDict=familyParam_16, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍家庭失败')  
             
        NewfamilyParam_16 = copy.deepcopy(ShiYouRenKouPara.houseFamilyObject) 
        NewfamilyParam_16['newHouseHold.accountNumber'] = '01%s'%CommonUtil.createRandomString()
        NewfamilyParam_16['newHouseHold.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from householdstaffs t where t.idcardno='%s' and t.name='%s'" % (NewHuJiParam_16['population.idCardNo'],NewHuJiParam_16['population.name']))
        NewfamilyParam_16['orgId'] = NewHuJiParam_16['population.organization.id']        
        responseDict = ShiYouRenKouIntf.add_houseFamily(houseFamilyDict=NewfamilyParam_16, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍家庭失败')  
        
        familyMemberParam_16 = copy.deepcopy(ShiYouRenKouPara.houseMemberObject) 
        familyMemberParam_16['orgId'] = NewHuJiParam_016['population.organization.id'] 
        familyMemberParam_16['houseFamilyId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from censusregisterfamilys t where t.accountnumber='%s'"% familyParam_16['newHouseHold.accountNumber'])
        familyMemberParam_16['householdStaffId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from householdstaffs t where t.idcardno='%s' and t.name='%s'" % (NewHuJiParam_016['population.idCardNo'],NewHuJiParam_016['population.name']))
        familyMemberParam_16['accountNumber'] = familyParam_16['newHouseHold.accountNumber']              
        responseDict = ShiYouRenKouIntf.add_houseMember(houseFamilyDict=familyMemberParam_16, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增家庭成员失败')              
        
        transferMemberParam_16 = copy.deepcopy(ShiYouRenKouPara.houseMemberObject) 
        transferMemberParam_16['householdStaffId'] = familyMemberParam_16['householdStaffId']
        transferMemberParam_16['houseFamilyId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from censusregisterfamilys t where t.accountnumber='%s'"% NewfamilyParam_16['newHouseHold.accountNumber'])
        responseDict = ShiYouRenKouIntf.transfer_houseMember(houseFamilyDict=transferMemberParam_16, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '转移家庭成员失败')              
        
        param_16 = copy.deepcopy(ShiYouRenKouPara.checkHouseMemberDict)
        param_16['accountNumber'] = familyMemberParam_16['accountNumber']
        param_16['censusRegisterFamily'] = {"id":familyMemberParam_16['houseFamilyId']}    
        param_16['idCardNo'] = NewHuJiParam_016['population.idCardNo']     
        param_16['name'] = NewHuJiParam_016['population.name']
        ret = ShiYouRenKouIntf.check_houseMember(param_16,orgId=NewHuJiParam_016['population.organization.id'],houseFamilyId=familyMemberParam_16['houseFamilyId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '转移家庭成员失败')
#         ret = ShiYouRenKouIntf.check_houseMember(param,orgId=NewHuJiParam['population.organization.id'],houseFamilyId=familyMemberParam['houseFamilyId'],username=userInit['DftWangGeUser'], password='11111111')         
#         self.assertFalse(ret, '已移除的家庭成员在列表中依然存在')
        pass

    def testFamilyViewAdd_24(self):
        """实有人口>户籍家庭管理走访记录"""

        HuJiParam = copy.deepcopy(ShiYouRenKouPara.populationObject) 
        HuJiParam['mode']='add'
        HuJiParam['population.organization.id'] = orgInit['DftWangGeOrgId']
        HuJiParam['population.organization.orgName'] = orgInit['DftWangGeOrg']
        HuJiParam['population.idCardNo'] = '111111111110014'
        HuJiParam['population.name'] = 'test14'
        HuJiParam['population.isHaveHouse1'] = 'null'         
        responseDict = ShiYouRenKouIntf.add_HuJiRenKou(HuJiRenKouDict=HuJiParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口失败') 
             
        familyParam = copy.deepcopy(ShiYouRenKouPara.houseFamilyObject) 
        familyParam['newHouseHold.accountNumber'] = '01%s'%CommonUtil.createRandomString()
        familyParam['newHouseHold.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from householdstaffs t where t.idcardno='%s' and t.name='%s'" % (HuJiParam['population.idCardNo'],HuJiParam['population.name']))
        familyParam['orgId'] = HuJiParam['population.organization.id']        
        responseDict = ShiYouRenKouIntf.add_houseFamily(houseFamilyDict=familyParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍家庭失败')  
        
        viewDataParam = copy.deepcopy(ShiYouRenKouPara.viewDataObject) 
        viewDataParam['mode']='houseFamilyAdd'
        viewDataParam['viewdata.fromSystem'] = '0'
        viewDataParam['viewdata.organization.id'] = orgInit['DftWangGeOrgId']
        viewDataParam['viewdata.status'] = '0'      # 0:未转民情日志状态   1：转民情日志后的状态
        viewDataParam['viewdata.viewName'] = '走访人%s'%CommonUtil.createRandomString() 
        viewDataParam['viewdata.family.householdName'] = CommonIntf.getDbQueryResult(dbCommand = "select t.familyid from householdstaffs t where t.idcardno='%s'" % HuJiParam['population.idCardNo'])
        viewDataParam['viewdata.viewInfo'] = '走访内容%s'%CommonUtil.createRandomString() 
        responseDict = ShiYouRenKouIntf.add_viewDataManage(viewDataDict=viewDataParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增走访记录失败')           
 
        viewDataCheckParam = copy.deepcopy(ShiYouRenKouPara.checkViewDataDict)
        viewDataCheckParam['viewName'] = viewDataParam['viewdata.viewName']       
        viewDataCheckParam['id'] = CommonIntf.getDbQueryResult(dbCommand = "select id from viewdatas p where p.viewname = '%s'"%viewDataParam['viewdata.viewName']) 
        ret = ShiYouRenKouIntf.check_viewDataManage(viewDataCheckParam, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找走访记录失败')        
        pass       
        
    
    def testViewDataAdd_19(self):
        """实有人口>走访记录新增"""
        HuJiParam_19 = copy.deepcopy(ShiYouRenKouPara.populationObject) 
        HuJiParam_19['mode']='add'
        HuJiParam_19['population.organization.id'] = orgInit['DftWangGeOrgId']
        HuJiParam_19['population.organization.orgName'] = orgInit['DftWangGeOrg']
        HuJiParam_19['population.idCardNo'] = '111111111110019'
        HuJiParam_19['population.name'] = 'test19'
        HuJiParam_19['population.isHaveHouse1'] = 'null'   
        HuJiParam_19['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        responseDict = ShiYouRenKouIntf.add_HuJiRenKou(HuJiRenKouDict=HuJiParam_19, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口失败')       
  
        HuZhuParam_19 = copy.deepcopy(ShiYouRenKouPara.huzhuObject) 
        HuZhuParam_19['mode']='add'
        HuZhuParam_19['population.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from householdstaffs t where t.idcardno='%s'" % HuJiParam_19['population.idCardNo'])
        HuZhuParam_19['population.organization.id'] = HuJiParam_19['population.organization.id']
        HuZhuParam_19['dailogName'] = 'householdStaffPopulationDialog'
        HuZhuParam_19['population.organization.orgName'] = orgInit['DftWangGeOrg']
        HuZhuParam_19['population.idCardNo'] = HuJiParam_19['population.idCardNo']
        HuZhuParam_19['population.accountNumber'] = '01%s'%CommonUtil.createRandomString()   #户号    
        HuZhuParam_19['population.relationShipWithHead.id'] = CommonIntf.getDbQueryResult(dbCommand = "select id from propertydicts p where p.displayname = '本人'") 
        HuZhuParam_19['population.residentStatus.id'] = CommonIntf.getDbQueryResult(dbCommand = "select id from propertydicts p where p.displayname = '人户同在'") 
        responseDict = ShiYouRenKouIntf.add_HuZhuMassage(HuJiRenKouDict=HuZhuParam_19, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口的户主信息失败')    
  
        viewDataParam_19 = copy.deepcopy(ShiYouRenKouPara.viewDataObject) 
        viewDataParam_19['mode']='add'
        viewDataParam_19['viewdata.fromSystem'] = '0'
        viewDataParam_19['viewdata.organization.id'] = orgInit['DftWangGeOrgId']
        viewDataParam_19['viewdata.status'] = '0'      # 0:未转民情日志状态   1：转民情日志后的状态
        viewDataParam_19['viewdata.viewName'] = '走访人%s'%CommonUtil.createRandomString() 
        viewDataParam_19['viewdata.family.householdName'] = CommonIntf.getDbQueryResult(dbCommand = "select t.familyid from householdstaffs t where t.idcardno='%s'" % HuJiParam_19['population.idCardNo'])
        viewDataParam_19['viewdata.viewInfo'] = '走访内容%s'%CommonUtil.createRandomString() 
        responseDict = ShiYouRenKouIntf.add_viewDataManage(viewDataDict=viewDataParam_19, username=userInit['DftWangGeUser'], password='11111111')
#         self.assertTrue(responseDict.result, '新增走访记录失败')       
          
        viewDataCheckParam_19 = copy.deepcopy(ShiYouRenKouPara.checkViewDataDict)
        viewDataCheckParam_19['viewName'] = viewDataParam_19['viewdata.viewName']       
        viewDataCheckParam_19['id'] = CommonIntf.getDbQueryResult(dbCommand = "select id from viewdatas p where p.viewname = '%s'"%viewDataParam_19['viewdata.viewName']) 
        ret = ShiYouRenKouIntf.check_viewDataManage(viewDataCheckParam_19, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找走访记录失败')        
        pass 
 
    def testViewDataEdit_20(self):
        """实有人口>走访记录修改"""
        HuJiParam_20 = copy.deepcopy(ShiYouRenKouPara.populationObject) 
        HuJiParam_20['mode']='add'
        HuJiParam_20['population.organization.id'] = orgInit['DftWangGeOrgId']
        HuJiParam_20['population.organization.orgName'] = orgInit['DftWangGeOrg']
        HuJiParam_20['population.idCardNo'] = '111111111110020'
        HuJiParam_20['population.name'] = 'test20'
        HuJiParam_20['population.isHaveHouse1'] = 'null'   
        HuJiParam_20['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        responseDict = ShiYouRenKouIntf.add_HuJiRenKou(HuJiRenKouDict=HuJiParam_20, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口失败')       
  
        HuZhuParam_20 = copy.deepcopy(ShiYouRenKouPara.huzhuObject) 
        HuZhuParam_20['mode']='add'
        HuZhuParam_20['population.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from householdstaffs t where t.idcardno='%s'" % HuJiParam_20['population.idCardNo'])
        HuZhuParam_20['population.organization.id'] = HuJiParam_20['population.organization.id']
        HuZhuParam_20['dailogName'] = 'householdStaffPopulationDialog'
        HuZhuParam_20['population.organization.orgName'] = orgInit['DftWangGeOrg']
        HuZhuParam_20['population.idCardNo'] = HuJiParam_20['population.idCardNo']
        HuZhuParam_20['population.accountNumber'] = '01%s'%CommonUtil.createRandomString()   #户号    
        HuZhuParam_20['population.relationShipWithHead.id'] = CommonIntf.getDbQueryResult(dbCommand = "select id from propertydicts p where p.displayname = '本人'") 
        HuZhuParam_20['population.residentStatus.id'] = CommonIntf.getDbQueryResult(dbCommand = "select id from propertydicts p where p.displayname = '人户同在'") 
        responseDict = ShiYouRenKouIntf.add_HuZhuMassage(HuJiRenKouDict=HuZhuParam_20, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口的户主信息失败')     
  
        viewDataParam_20 = copy.deepcopy(ShiYouRenKouPara.viewDataObject) 
        viewDataParam_20['mode']='add'
        viewDataParam_20['viewdata.fromSystem'] = '0'
        viewDataParam_20['viewdata.organization.id'] = orgInit['DftWangGeOrgId']
        viewDataParam_20['viewdata.status'] = '0'
        viewDataParam_20['viewdata.viewName'] = '走访人%s'%CommonUtil.createRandomString() 
        viewDataParam_20['viewdata.family.householdName'] = CommonIntf.getDbQueryResult(dbCommand = "select t.familyid from householdstaffs t where t.idcardno='%s'" % HuJiParam_20['population.idCardNo'])
        viewDataParam_20['viewdata.viewInfo'] = '走访内容%s'%CommonUtil.createRandomString() 
        responseDict = ShiYouRenKouIntf.add_viewDataManage(viewDataParam_20, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增走访记录失败')     
        
        editViewDataParam_20 = copy.deepcopy(ShiYouRenKouPara.viewDataObject) 
        editViewDataParam_20['mode'] ='edit'
        editViewDataParam_20['viewdata.id'] = CommonIntf.getDbQueryResult(dbCommand = "select id from viewdatas p where p.viewname = '%s'"% viewDataParam_20['viewdata.viewName'])
        editViewDataParam_20['viewdata.fromSystem'] = viewDataParam_20['viewdata.fromSystem']
        editViewDataParam_20['viewdata.organization.id'] = viewDataParam_20['viewdata.organization.id']
        editViewDataParam_20['viewdata.status'] = viewDataParam_20['viewdata.status']
        editViewDataParam_20['viewdata.viewName'] = '修改走访人%s'%CommonUtil.createRandomString() 
        editViewDataParam_20['viewdata.family.householdName'] = viewDataParam_20['viewdata.family.householdName']
        editViewDataParam_20['viewdata.viewInfo'] = '修改走访内容%s'%CommonUtil.createRandomString() 
        responseDict = ShiYouRenKouIntf.edit_viewDataManage(editViewDataParam_20, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改走访记录失败')  
          
        viewDataCheckParam_20 = copy.deepcopy(ShiYouRenKouPara.checkViewDataDict)
        viewDataCheckParam_20['viewName'] = editViewDataParam_20['viewdata.viewName']       
        viewDataCheckParam_20['id'] = CommonIntf.getDbQueryResult(dbCommand = "select id from viewdatas p where p.viewname = '%s'"%editViewDataParam_20['viewdata.viewName']) 
        ret = ShiYouRenKouIntf.check_viewDataManage(viewDataCheckParam_20, orgId=viewDataParam_20['viewdata.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找走访记录失败')        
        pass 
    
    def testViewDataDelete_21(self):
        """实有人口>走访记录删除"""
        HuJiParam_21 = copy.deepcopy(ShiYouRenKouPara.populationObject) 
        HuJiParam_21['mode']='add'
        HuJiParam_21['population.organization.id'] = orgInit['DftWangGeOrgId']
        HuJiParam_21['population.organization.orgName'] = orgInit['DftWangGeOrg']
        HuJiParam_21['population.idCardNo'] = '111111111110021'
        HuJiParam_21['population.name'] = 'test21'
        HuJiParam_21['population.isHaveHouse1'] = 'null'   
        HuJiParam_21['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        responseDict = ShiYouRenKouIntf.add_HuJiRenKou(HuJiRenKouDict=HuJiParam_21, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口失败')       
  
        HuZhuParam_21 = copy.deepcopy(ShiYouRenKouPara.huzhuObject) 
        HuZhuParam_21['mode']='add'
        HuZhuParam_21['population.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from householdstaffs t where t.idcardno='%s'" % HuJiParam_21['population.idCardNo'])
        HuZhuParam_21['population.organization.id'] = HuJiParam_21['population.organization.id']
        HuZhuParam_21['dailogName'] = 'householdStaffPopulationDialog'
        HuZhuParam_21['population.organization.orgName'] = orgInit['DftWangGeOrg']
        HuZhuParam_21['population.idCardNo'] = HuJiParam_21['population.idCardNo']
        HuZhuParam_21['population.accountNumber'] = '01%s'%CommonUtil.createRandomString()   #户号    
        HuZhuParam_21['population.relationShipWithHead.id'] = CommonIntf.getDbQueryResult(dbCommand = "select id from propertydicts p where p.displayname = '本人'") 
        HuZhuParam_21['population.residentStatus.id'] = CommonIntf.getDbQueryResult(dbCommand = "select id from propertydicts p where p.displayname = '人户同在'") 
        responseDict = ShiYouRenKouIntf.add_HuZhuMassage(HuJiRenKouDict=HuZhuParam_21, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口的户主信息失败')    
  
        viewDataParam_21 = copy.deepcopy(ShiYouRenKouPara.viewDataObject) 
        viewDataParam_21['mode']='add'
        viewDataParam_21['viewdata.fromSystem'] = '0'
        viewDataParam_21['viewdata.organization.id'] = orgInit['DftWangGeOrgId']
        viewDataParam_21['viewdata.status'] = '0'
        viewDataParam_21['viewdata.viewName'] = '走访人%s'%CommonUtil.createRandomString() 
        viewDataParam_21['viewdata.family.householdName'] = CommonIntf.getDbQueryResult(dbCommand = "select t.familyid from householdstaffs t where t.idcardno='%s'" % HuJiParam_21['population.idCardNo'])
        viewDataParam_21['viewdata.viewInfo'] = '走访内容%s'%CommonUtil.createRandomString() 
        responseDict = ShiYouRenKouIntf.add_viewDataManage(viewDataParam_21, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增走访记录失败')     
        
        newViewDataParam_21 = copy.deepcopy(ShiYouRenKouPara.viewDataObject) 
        newViewDataParam_21['mode']='add'
        newViewDataParam_21['viewdata.fromSystem'] = '0'
        newViewDataParam_21['viewdata.organization.id'] = orgInit['DftWangGeOrgId']
        newViewDataParam_21['viewdata.status'] = '0'
        newViewDataParam_21['viewdata.viewName'] = '新增走访人%s'%CommonUtil.createRandomString() 
        newViewDataParam_21['viewdata.family.householdName'] = CommonIntf.getDbQueryResult(dbCommand = "select t.familyid from householdstaffs t where t.idcardno='%s'" % HuJiParam_21['population.idCardNo'])
        newViewDataParam_21['viewdata.viewInfo'] = '新增走访内容%s'%CommonUtil.createRandomString() 
        responseDict = ShiYouRenKouIntf.add_viewDataManage(newViewDataParam_21, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增走访记录失败')  
        
        deleteParam_21 = copy.deepcopy(ShiYouRenKouPara.deleteDict)
        deleteParam_21['ids'] = str(CommonIntf.getDbQueryResult(dbCommand = "select id from viewdatas p where p.viewname = '%s'"%viewDataParam_21['viewdata.viewName']))+','+ str(CommonIntf.getDbQueryResult(dbCommand = "select id from viewdatas p where p.viewname = '%s'"%newViewDataParam_21['viewdata.viewName']))
        responseDict = ShiYouRenKouIntf.delete_viewDataManage(deleteParam_21, username=userInit['DftWangGeUser'], password='11111111')          
        self.assertTrue(responseDict.result, '删除走访记录失败')  
          
        viewDataCheckParam_21 = copy.deepcopy(ShiYouRenKouPara.checkViewDataDict)
        viewDataCheckParam_21['viewName'] = viewDataParam_21['viewdata.viewName']       
        viewDataCheckParam_21['id'] = CommonIntf.getDbQueryResult(dbCommand = "select id from viewdatas p where p.viewname = '%s'"%viewDataParam_21['viewdata.viewName']) 
        ret = ShiYouRenKouIntf.check_viewDataManage(viewDataCheckParam_21, orgId=viewDataParam_21['viewdata.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '删除的走访记录在列表中依然存在，删除失败')        
        
        viewDataCheckParam_21['viewName'] = newViewDataParam_21['viewdata.viewName']       
        viewDataCheckParam_21['id'] = CommonIntf.getDbQueryResult(dbCommand = "select id from viewdatas p where p.viewname = '%s'"%newViewDataParam_21['viewdata.viewName']) 
        ret = ShiYouRenKouIntf.check_viewDataManage(viewDataCheckParam_21, orgId=newViewDataParam_21['viewdata.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '删除的走访记录在列表中依然存在，删除失败')        
        
        pass

    def testViewDataSearch_22(self):
        """实有人口>走访记录查询"""
        HuJiParam_22 = copy.deepcopy(ShiYouRenKouPara.populationObject) 
        HuJiParam_22['mode']='add'
        HuJiParam_22['population.organization.id'] = orgInit['DftWangGeOrgId']
        HuJiParam_22['population.organization.orgName'] = orgInit['DftWangGeOrg']
        HuJiParam_22['population.idCardNo'] = '111111111110022'
        HuJiParam_22['population.name'] = 'test22'
        HuJiParam_22['population.isHaveHouse1'] = 'null'   
        HuJiParam_22['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        responseDict = ShiYouRenKouIntf.add_HuJiRenKou(HuJiRenKouDict=HuJiParam_22, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口失败')       
  
        HuZhuParam_22 = copy.deepcopy(ShiYouRenKouPara.huzhuObject) 
        HuZhuParam_22['mode']='add'
        HuZhuParam_22['population.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from householdstaffs t where t.idcardno='%s'" % HuJiParam_22['population.idCardNo'])
        HuZhuParam_22['population.organization.id'] = HuJiParam_22['population.organization.id']
        HuZhuParam_22['dailogName'] = 'householdStaffPopulationDialog'
        HuZhuParam_22['population.organization.orgName'] = orgInit['DftWangGeOrg']
        HuZhuParam_22['population.idCardNo'] = HuJiParam_22['population.idCardNo']
        HuZhuParam_22['population.accountNumber'] = '01%s'%CommonUtil.createRandomString()   #户号    
        HuZhuParam_22['population.relationShipWithHead.id'] = CommonIntf.getDbQueryResult(dbCommand = "select id from propertydicts p where p.displayname = '本人'") 
        HuZhuParam_22['population.residentStatus.id'] = CommonIntf.getDbQueryResult(dbCommand = "select id from propertydicts p where p.displayname = '人户同在'") 
        responseDict = ShiYouRenKouIntf.add_HuZhuMassage(HuJiRenKouDict=HuZhuParam_22, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口的户主信息失败')   
  
        viewDataParam_22 = copy.deepcopy(ShiYouRenKouPara.viewDataObject) 
        viewDataParam_22['mode']='add'
        viewDataParam_22['viewdata.fromSystem'] = '0'
        viewDataParam_22['viewdata.organization.id'] = orgInit['DftWangGeOrgId']
        viewDataParam_22['viewdata.status'] = '0'
        viewDataParam_22['viewdata.viewName'] = '走访人%s'%CommonUtil.createRandomString() 
        viewDataParam_22['viewdata.family.householdName'] = CommonIntf.getDbQueryResult(dbCommand = "select t.familyid from householdstaffs t where t.idcardno='%s'" % HuJiParam_22['population.idCardNo'])
        viewDataParam_22['viewdata.viewInfo'] = '走访内容%s'%CommonUtil.createRandomString() 
        responseDict = ShiYouRenKouIntf.add_viewDataManage(viewDataParam_22, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增走访记录失败')     
        
        newViewDataParam_22 = copy.deepcopy(ShiYouRenKouPara.viewDataObject) 
        newViewDataParam_22['mode']='add'
        newViewDataParam_22['viewdata.fromSystem'] = '0'
        newViewDataParam_22['viewdata.organization.id'] = orgInit['DftWangGeOrgId']
        newViewDataParam_22['viewdata.status'] = '0'
        newViewDataParam_22['viewdata.viewName'] = '新增走访人%s'%CommonUtil.createRandomString() 
        newViewDataParam_22['viewdata.family.householdName'] = CommonIntf.getDbQueryResult(dbCommand = "select t.familyid from householdstaffs t where t.idcardno='%s'" % HuJiParam_22['population.idCardNo'])
        newViewDataParam_22['viewdata.viewInfo'] = '新增走访内容%s'%CommonUtil.createRandomString() 
        responseDict = ShiYouRenKouIntf.add_viewDataManage(newViewDataParam_22, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增走访记录失败')  
          
        searchParam_22 = copy.deepcopy(ShiYouRenKouPara.checkViewDataDict)
        searchParam_22['viewName'] = viewDataParam_22['viewdata.viewName']       
        searchParam_22['id'] = CommonIntf.getDbQueryResult(dbCommand = "select id from viewdatas p where p.viewname = '%s'"%viewDataParam_22['viewdata.viewName']) 
        ret = ShiYouRenKouIntf.search_viewDataManage(searchParam_22, orgId=viewDataParam_22['viewdata.organization.id'],viewName=viewDataParam_22['viewdata.viewName'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '搜索走访记录失败') 
        pass
 
    def testViewDataSent_23(self):
        """实有人口>将走访记录生产为民情日志信息"""
        HuJiParam_23 = copy.deepcopy(ShiYouRenKouPara.populationObject) 
        HuJiParam_23['mode']='add'
        HuJiParam_23['population.organization.id'] = orgInit['DftWangGeOrgId']
        HuJiParam_23['population.organization.orgName'] = orgInit['DftWangGeOrg']
        HuJiParam_23['population.idCardNo'] = '111111111110023'
        HuJiParam_23['population.name'] = 'test23'
        HuJiParam_23['population.isHaveHouse1'] = 'null'   
        HuJiParam_23['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        responseDict = ShiYouRenKouIntf.add_HuJiRenKou(HuJiRenKouDict=HuJiParam_23, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口失败')       
  
        HuZhuParam_23 = copy.deepcopy(ShiYouRenKouPara.huzhuObject) 
        HuZhuParam_23['mode']='add'
        HuZhuParam_23['population.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from householdstaffs t where t.idcardno='%s'" % HuJiParam_23['population.idCardNo'])
        HuZhuParam_23['population.organization.id'] = HuJiParam_23['population.organization.id']
        HuZhuParam_23['dailogName'] = 'householdStaffPopulationDialog'
        HuZhuParam_23['population.organization.orgName'] = orgInit['DftWangGeOrg']
        HuZhuParam_23['population.idCardNo'] = HuJiParam_23['population.idCardNo']
        HuZhuParam_23['population.accountNumber'] = '01%s'%CommonUtil.createRandomString()   #户号    
        HuZhuParam_23['population.relationShipWithHead.id'] = CommonIntf.getDbQueryResult(dbCommand = "select id from propertydicts p where p.displayname = '本人'") 
        HuZhuParam_23['population.residentStatus.id'] = CommonIntf.getDbQueryResult(dbCommand = "select id from propertydicts p where p.displayname = '人户同在'") 
        responseDict = ShiYouRenKouIntf.add_HuZhuMassage(HuJiRenKouDict=HuZhuParam_23, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增户籍人口的户主信息失败')   
  
        viewDataParam_23 = copy.deepcopy(ShiYouRenKouPara.viewDataObject) 
        viewDataParam_23['mode']='add'
        viewDataParam_23['viewdata.fromSystem'] = '0'
        viewDataParam_23['viewdata.organization.id'] = orgInit['DftWangGeOrgId']
        viewDataParam_23['viewdata.status'] = '0'      # 0:未转民情日志状态   1：转民情日志后的状态
        viewDataParam_23['viewdata.viewName'] = '走访人%s'%CommonUtil.createRandomString() 
        viewDataParam_23['viewdata.family.householdName'] = CommonIntf.getDbQueryResult(dbCommand = "select t.familyid from householdstaffs t where t.idcardno='%s'" % HuJiParam_23['population.idCardNo'])
        viewDataParam_23['viewdata.viewInfo'] = '走访内容%s'%CommonUtil.createRandomString() 
        responseDict = ShiYouRenKouIntf.add_viewDataManage(viewDataParam_23, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增走访记录失败') 
        
        sentViewDataParam_23 = copy.deepcopy(ShiYouRenKouPara.sentViewDataObject) 
        sentViewDataParam_23['issueNew.viewDataIds'] = CommonIntf.getDbQueryResult(dbCommand = "select id from viewdatas p where p.viewname = '%s'"%viewDataParam_23['viewdata.viewName']) 
        sentViewDataParam_23['issueNew.occurOrg.id'] = viewDataParam_23['viewdata.organization.id']
        sentViewDataParam_23['issueNew.subject'] = '标题%s'%CommonUtil.createRandomString()
        sentViewDataParam_23['eventOccurOrgSelector'] = orgInit['DftWangGeOrg']
        sentViewDataParam_23['issueNew.createPerson'] = userInit['DftWangGeUser'] 
        sentViewDataParam_23['issueNew.sourcePerson'] = viewDataParam_23['viewdata.viewName']
        sentViewDataParam_23['issueNew.issueTypeName'] = '工作心得体会'     #日志分类：工作心得体会,工作问题咨询,工作信息记录
        sentViewDataParam_23['issueNew.issueContent'] = viewDataParam_23['viewdata.viewInfo'] #+<br />
        responseDict = ShiYouRenKouIntf.sent_viewDataManage(sentViewDataParam_23, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '生成民情日志失败')              
          
        viewDataCheckParam_23 = copy.deepcopy(ShiYouRenKouPara.checkViewDataDict)
        viewDataCheckParam_23['viewName'] = viewDataParam_23['viewdata.viewName']       
        viewDataCheckParam_23['id'] = CommonIntf.getDbQueryResult(dbCommand = "select id from viewdatas p where p.viewname = '%s'"%viewDataParam_23['viewdata.viewName']) 
        viewDataCheckParam_23['status'] = 1   #生产民情日志状态 
        ret = ShiYouRenKouIntf.check_viewDataManage(viewDataCheckParam_23, orgId=viewDataParam_23['viewdata.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找走访记录失败')        
        pass 
 
 
#重点人员


    def testXingManShiFangPopulationAdd_17(self):
        """重点人员>刑满释放人员新增"""
        jiaoZhengParam_17 = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
        jiaoZhengParam_17['mode']='add'
        jiaoZhengParam_17['population.organization.id'] = orgInit['DftWangGeOrgId']
        jiaoZhengParam_17['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']
        jiaoZhengParam_17['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['sheQuJiaoZhengRenYuan']
        jiaoZhengParam_17['population.organization.orgName'] = orgInit['DftWangGeOrg']
        jiaoZhengParam_17['population.idCardNo'] = '331100199711220001'
        jiaoZhengParam_17['population.name'] = '矫正人员'
        jiaoZhengParam_17['actualPersonType'] = jiaoZhengParam_17['population.actualPopulationType']
        jiaoZhengParam_17['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        jiaoZhengParam_17['population.isHaveHouse1'] = 'null'   
        jiaoZhengParam_17['population.accusation'] = '矫正罪名'
        jiaoZhengParam_17['population.executeType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '监外执行罪犯'") 
        jiaoZhengParam_17['population.rectifyStartDate'] = '2015-12-01'
        jiaoZhengParam_17['population.rectifyEndDate'] = '2015-12-31'     
        responseDict = ShiYouRenKouIntf.add_sheQuJiaoZheng(sheQuJiaoZhengDict=jiaoZhengParam_17, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增社区矫正人员失败') 
  
        xingShiParam_17 = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
        xingShiParam_17['mode']='add'
        xingShiParam_17['population.organization.id'] = orgInit['DftWangGeOrgId']
        xingShiParam_17['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人口or流动人口
        xingShiParam_17['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['xingManShiFangRenYuan']
        xingShiParam_17['population.organization.orgName'] = orgInit['DftWangGeOrg']
        xingShiParam_17['population.idCardNo'] = jiaoZhengParam_17['population.idCardNo']
        xingShiParam_17['population.name'] = '刑满释放人员'
        xingShiParam_17['actualPersonType'] = xingShiParam_17['population.actualPopulationType']
        xingShiParam_17['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        xingShiParam_17['population.isHaveHouse1'] = 'null'   
        xingShiParam_17['population.caseReason'] = 'Reason'
        xingShiParam_17['population.positiveInfoType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '刑释人员'") 
        xingShiParam_17['population.laborEduAddress'] = '劳教所'
        xingShiParam_17['population.imprisonmentDate'] = '2weeks'
        xingShiParam_17['population.releaseOrBackDate'] = '2015-12-01'  
        
        xingShiCheckParam_17 = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        xingShiCheckParam_17['idCardNo'] = xingShiParam_17['population.idCardNo']
        ret_01 = ShiYouRenKouIntf.check_sheQuJiaoZheng(xingShiCheckParam_17, orgId=jiaoZhengParam_17['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        if ret_01 is True:        
            Log.LogOutput(LogLevel.DEBUG, "社区矫正人员中存在该id人口信息,请重新输入id信息")   
            xingShiParam_17['population.idCardNo'] = '331100199711220000'
            responseDict = ShiYouRenKouIntf.add_xingManShiFang(xingManShiFangDict=xingShiParam_17, username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增刑满释放人员失败')   
            xingShiCheckParam_17['idCardNo'] = xingShiParam_17['population.idCardNo']    
            xingShiCheckParam_17['name'] = xingShiParam_17['population.name'] 
            ret_02 = ShiYouRenKouIntf.check_xingManShiFang(xingShiCheckParam_17, orgId=xingShiParam_17['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
            self.assertTrue(ret_02, '查找刑满释放人员失败')        
        else:  
            responseDict = ShiYouRenKouIntf.add_xingManShiFang(xingManShiFangDict=xingShiParam_17, username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增刑满释放人员失败')    
            xingShiCheckParam_17['name'] = xingShiParam_17['population.name']   
            ret_03 = ShiYouRenKouIntf.check_xingManShiFang(xingShiCheckParam_17, orgId=xingShiParam_17['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
            self.assertTrue(ret_03, '查找刑满释放人员失败')       
            
        ret = ShiYouRenKouIntf.check_HuJiPopulation(xingShiCheckParam_17, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '没有检查到户籍人口下对应的刑释人员信息')
        #补充修改用例
        updPara=copy.deepcopy(xingShiParam_17)
        updPara['mode']='edit'
        updPara['population.id']=json.loads(responseDict.text)['id']
        updPara['population.idCardNo']='331100199711220000'
        updPara['population.birthday']='1997-11-22'
        updPara['population.name']=xingShiParam_17['population.name']+createRandomString()
        updPara['population.releaseOrBackDate']='2016-1-1'
        updPara['population.laborEduAddress']=xingShiParam_17['population.laborEduAddress']+createRandomString()
        updPara['population.caseReason']=xingShiParam_17['population.caseReason']+createRandomString()
        updPara['population.imprisonmentDate']=xingShiParam_17['population.imprisonmentDate']+createRandomString()
        res1 = ShiYouRenKouIntf.add_xingManShiFang(xingManShiFangDict=updPara, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(res1.result, '修改刑满释放人员失败')
        #验证修改功能
        xingShiCheckParam_17['name'] = updPara['population.name']
        ret_04 = ShiYouRenKouIntf.check_xingManShiFang(xingShiCheckParam_17, orgId=updPara['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret_04, '查找刑满释放人员失败')
        Log.LogOutput(message='修改刑满释放人员成功') 
        #补充删除功能
        ShiYouRenKouIntf.delete_xingManShiFang(xingManShiFangDict={'populationIds':updPara['population.id']}, username = userInit['DftWangGeUser'], password = '11111111')
        #验证删除功能
        ret_05 = ShiYouRenKouIntf.check_xingManShiFang(xingShiCheckParam_17, orgId=updPara['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret_05, '查找刑满释放人员失败')
        Log.LogOutput(message='删除验证通过')       
        pass     
    def testXingShiSearch_17(self):
        '''刑满释放人员-查询'''
        #快速搜索
        #新增两条数据
        addPara1 = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
        addPara1['mode']='add'
        addPara1['population.organization.id'] = orgInit['DftWangGeOrgId']
        addPara1['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人口or流动人口
        addPara1['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['xingManShiFangRenYuan']
        addPara1['population.organization.orgName'] = orgInit['DftWangGeOrg']
        addPara1['population.idCardNo'] = '331100199711220000'
        addPara1['population.name'] = '刑满释放人员'+createRandomString()
        addPara1['actualPersonType'] = addPara1['population.actualPopulationType']
        addPara1['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        addPara1['population.isHaveHouse1'] = 'null'   
        addPara1['population.caseReason'] = 'Reason'+createRandomString()
        addPara1['population.positiveInfoType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '刑释人员'") 
        addPara1['population.laborEduAddress'] = '劳教所'+createRandomString()
        addPara1['population.imprisonmentDate'] = '2weeks'
        addPara1['population.releaseOrBackDate'] = '2015-12-01'  
        xingShiCheckParam_17 = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        xingShiCheckParam_17['idCardNo'] = addPara1['population.idCardNo']
        responseDict = ShiYouRenKouIntf.add_xingManShiFang(xingManShiFangDict=addPara1, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增刑满释放人员失败')
        #第二条
        addPara2 = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
        addPara2['mode']='add'
        addPara2['population.organization.id'] = orgInit['DftWangGeOrgId']
        addPara2['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人口or流动人口
        addPara2['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['xingManShiFangRenYuan']
        addPara2['population.organization.orgName'] = orgInit['DftWangGeOrg']
        addPara2['population.idCardNo'] = '331100199711220001'
        addPara2['population.name'] = '刑满释放人员'+createRandomString()
        addPara2['actualPersonType'] = addPara2['population.actualPopulationType']
        addPara2['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        addPara2['population.isHaveHouse1'] = 'null'   
        addPara2['population.caseReason'] = 'Reason'+createRandomString()
        addPara2['population.positiveInfoType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '刑释人员'") 
        addPara2['population.laborEduAddress'] = '劳教所'+createRandomString()
        addPara2['population.imprisonmentDate'] = '2weeks'
        addPara2['population.releaseOrBackDate'] = '2015-12-01'  
        xingShiCheckParam_17 = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        xingShiCheckParam_17['idCardNo'] = addPara2['population.idCardNo']
        responseDict = ShiYouRenKouIntf.add_xingManShiFang(xingManShiFangDict=addPara2, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增刑满释放人员失败')
        #姓名快速检索
        searchPara1=copy.deepcopy(ShiYouRenKouPara.xingManShiFangFastSearch)
        searchPara1['organizationId']=orgInit['DftWangGeOrgId']
        searchPara1['searchPositiveInfoVo.fastSearchKeyWords']= addPara1['population.name']
        checkPara1={'name':addPara1['population.name']}
        checkPara2={'name':addPara2['population.name']}
        result11=ShiYouRenKouIntf.checkXingShiFastSearchList(checkpara=checkPara1,searchpara=searchPara1)
        self.assertTrue(result11, '通过姓名快速查询失败')
        result12=ShiYouRenKouIntf.checkXingShiFastSearchList(checkpara=checkPara2,searchpara=searchPara1)
        self.assertFalse(result12,'通过姓名快速查询失败')
        Log.LogOutput( message='通过姓名快速查询验证成功！')
        #根据身份证快速查询
        searchPara2=copy.deepcopy(ShiYouRenKouPara.xingManShiFangFastSearch)
        searchPara2['organizationId']=orgInit['DftWangGeOrgId']
        searchPara2['searchPositiveInfoVo.fastSearchKeyWords']= addPara1['population.idCardNo']
        result21=ShiYouRenKouIntf.checkXingShiFastSearchList(checkpara=checkPara1,searchpara=searchPara2)
        self.assertTrue(result21, '通过身份证快速查询失败')
        result22=ShiYouRenKouIntf.checkXingShiFastSearchList(checkpara=checkPara2,searchpara=searchPara2)
        self.assertFalse(result22,'通过身份证快速查询失败')
        Log.LogOutput( message='通过身份证快速查询验证成功！')  
        #境外高级搜索
        #高级搜索,通过原罪名搜索  
        searchPara3=copy.deepcopy(ShiYouRenKouPara.xingManShiFangSeniorSearch)
        searchPara3['organizationId']=orgInit['DftWangGeOrgId']
        searchPara3['searchPositiveInfoVo.caseReason']= addPara1['population.caseReason']
        result31=ShiYouRenKouIntf.checkXingShiSeniorSearchList(checkpara=checkPara1,searchpara=searchPara3)
        self.assertTrue(result31, '通过原罪名高级查询失败')
        result32=ShiYouRenKouIntf.checkXingShiSeniorSearchList(checkpara=checkPara2,searchpara=searchPara3)
        self.assertFalse(result32,'通过原罪名高级查询失败')
        Log.LogOutput( message='通过原罪名高级查询验证成功！')         
        #高级搜索,通过劳教场所搜索
        searchPara4=copy.deepcopy(ShiYouRenKouPara.xingManShiFangSeniorSearch)
        searchPara4['organizationId']=orgInit['DftWangGeOrgId']
        searchPara4['searchPositiveInfoVo.laborEduAddress']= addPara1['population.laborEduAddress']
        result41=ShiYouRenKouIntf.checkXingShiSeniorSearchList(checkpara=checkPara1,searchpara=searchPara4)
        self.assertTrue(result41, '通过劳教场所高级查询失败')
        result42=ShiYouRenKouIntf.checkXingShiSeniorSearchList(checkpara=checkPara2,searchpara=searchPara4)
        self.assertFalse(result42,'通过劳教场所高级查询失败')
        Log.LogOutput( message='通过劳教场所高级查询验证成功！')        
        pass
    
    def testXingShiTransfer_25(self):
        """重点人员>刑满释放人员转为社区矫正人员"""
        xingShiParam = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
        xingShiParam['mode']='add'
        xingShiParam['population.organization.id'] = orgInit['DftWangGeOrgId']
        xingShiParam['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人口or流动人口
        xingShiParam['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['xingManShiFangRenYuan']
        xingShiParam['population.organization.orgName'] = orgInit['DftWangGeOrg']
        xingShiParam['population.idCardNo'] = '330000199911110025'
        xingShiParam['population.name'] = '刑满释放人员'
        xingShiParam['actualPersonType'] = xingShiParam['population.actualPopulationType']
        xingShiParam['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        xingShiParam['population.isHaveHouse1'] = 'null'   
        xingShiParam['population.caseReason'] = 'Reason'
        xingShiParam['population.positiveInfoType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '刑释人员'") 
        xingShiParam['population.laborEduAddress'] = '劳教所'
        xingShiParam['population.imprisonmentDate'] = '2weeks'
        xingShiParam['population.releaseOrBackDate'] = Time.getCurrentDate()
        responseDict = ShiYouRenKouIntf.add_xingManShiFang(xingManShiFangDict=xingShiParam, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增刑满释放人员失败')   
            
        transferParam = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
        transferParam['mode']='add'
        transferParam['population.organization.id'] = xingShiParam['population.organization.id']
        transferParam['population.actualPopulationType'] = xingShiParam['population.actualPopulationType']
        transferParam['population.attentionPopulationType'] = xingShiParam['population.attentionPopulationType']
        transferParam['population.organization.orgName'] = xingShiParam['population.organization.orgName']
        transferParam['population.idCardNo'] = xingShiParam['population.idCardNo']
        transferParam['population.name'] = xingShiParam['population.name']
        transferParam['actualPersonType'] = transferParam['population.actualPopulationType']
        transferParam['population.gender.id'] = xingShiParam['population.gender.id'] 
        transferParam['population.isHaveHouse1'] = xingShiParam['population.isHaveHouse1']   
        transferParam['population.accusation'] = '矫正罪名'
        transferParam['population.executeType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '监外执行罪犯'") 
        transferParam['population.rectifyStartDate'] = '2015-12-01'
        transferParam['population.rectifyEndDate'] = '2016-3-30'     
        ret = ShiYouRenKouIntf.add_sheQuJiaoZheng(transferParam,username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret.result, '转为刑满释放失败') 

        CheckParam = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        CheckParam['idCardNo'] = xingShiParam['population.idCardNo']
        ret_01 = ShiYouRenKouIntf.check_sheQuJiaoZheng(CheckParam, orgId=xingShiParam['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret_01, '在社区矫正列表下检查到转移的人口信息') 
        
        ret_02 = ShiYouRenKouIntf.check_xingManShiFang(CheckParam, orgId=xingShiParam['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret_02, '已转移的人口在列表中依然存在，转移失败') 

    def testXingShiPopulationImportAndDownLoad_29(self):
        """重点人员>刑释人员信息 导入/导出"""
         
        importHuJiparam = copy.deepcopy(ShiYouRenKouPara.data)
        importHuJiparam['dataType']='positiveInfo'
        importHuJiparam['templates']='POSITIVEINFO_syncActualPopulation'
        files = {'upload': ('test.xls', open('C:/autotest_file/importXingShiPopulation.xls', 'rb'),'applicationnd.ms-excel')}
        ret = ShiYouRenKouIntf.import_RenKou(importHuJiparam, files=files,username=userInit['DftWangGeUser'], password='11111111')         
        
        param = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        param['name'] = '刑释导入测试'      
        param['idCardNo'] = '111111111111173'
        ret = ShiYouRenKouIntf.check_xingManShiFang(param, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找刑满释放人员失败') 
                                
        downLoadHuJiparam = copy.deepcopy(ShiYouRenKouPara.dlZhongDianData)
        downLoadHuJiparam['organizationId']=orgInit['DftWangGeOrgId']
        response = ShiYouRenKouIntf.downLoad_XingShiRenYuan(downLoadHuJiparam, username=userInit['DftWangGeUser'], password='11111111')         
        with open("C:/autotest_file/downLoadXingShiPopulation.xls", "wb") as code:
            code.write(response.content)
            
        ret = CommonUtil.checkExcelCellValue(param['name'], 'downLoadXingShiPopulation.xls','刑满释放人员清单', 'A4')          
        self.assertTrue(ret, '导出失败')
                         
        pass
        
  
    def testSheQuJiaoZhengPopulationAdd_17(self):
        """重点人员>社区矫正人员新增"""
        
        xingShiParam_17 = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
        xingShiParam_17['mode']='add'
        xingShiParam_17['population.organization.id'] = orgInit['DftWangGeOrgId']
        xingShiParam_17['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['liuDongRenKou']
        xingShiParam_17['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['xingManShiFangRenYuan']
        xingShiParam_17['population.organization.orgName'] = orgInit['DftWangGeOrg']
        xingShiParam_17['population.idCardNo'] = '331100199711200001'
        xingShiParam_17['population.name'] = '刑满释放人员'
        xingShiParam_17['actualPersonType'] = xingShiParam_17['population.actualPopulationType']
        xingShiParam_17['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        xingShiParam_17['population.isHaveHouse1'] = 'null'   
        xingShiParam_17['population.caseReason'] = 'Reason'
        xingShiParam_17['population.positiveInfoType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '刑释人员'") 
        xingShiParam_17['population.laborEduAddress'] = '劳教所'
        xingShiParam_17['population.imprisonmentDate'] = '2weeks'
        xingShiParam_17['population.releaseOrBackDate'] = '2015-12-01'  
        responseDict = ShiYouRenKouIntf.add_xingManShiFang(xingManShiFangDict=xingShiParam_17, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增刑满释放人员失败')       
  
        jiaoZhengParam_17 = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
        jiaoZhengParam_17['mode']='add'
        jiaoZhengParam_17['population.organization.id'] = orgInit['DftWangGeOrgId']
        jiaoZhengParam_17['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['liuDongRenKou']  #属于户籍人口or流动人口
        jiaoZhengParam_17['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['sheQuJiaoZhengRenYuan']
        jiaoZhengParam_17['population.organization.orgName'] = orgInit['DftWangGeOrg']
        jiaoZhengParam_17['population.idCardNo'] = xingShiParam_17['population.idCardNo']
        jiaoZhengParam_17['population.name'] = '矫正人员'
        jiaoZhengParam_17['actualPersonType'] = jiaoZhengParam_17['population.actualPopulationType']
        jiaoZhengParam_17['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        jiaoZhengParam_17['population.isHaveHouse1'] = 'null'   
        jiaoZhengParam_17['population.accusation'] = '矫正罪名'
        jiaoZhengParam_17['population.executeType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '监外执行罪犯'") 
        jiaoZhengParam_17['population.rectifyStartDate'] = '2015-12-01'
        jiaoZhengParam_17['population.rectifyEndDate'] = '2015-12-31'     
        
        jiaoZhengCheckParam_17 = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        jiaoZhengCheckParam_17['idCardNo'] = jiaoZhengParam_17['population.idCardNo']
        ret_01 = ShiYouRenKouIntf.check_xingManShiFang(jiaoZhengCheckParam_17, orgId=xingShiParam_17['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        if ret_01 is True:        
            Log.LogOutput(LogLevel.DEBUG, "刑满释放人员中存在该id人口信息,请重新输入id信息")   
            jiaoZhengParam_17['population.idCardNo'] = '330000199711200011'
            responseDict = ShiYouRenKouIntf.add_sheQuJiaoZheng(sheQuJiaoZhengDict=jiaoZhengParam_17, username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增社区矫正人员失败')       
            jiaoZhengCheckParam_17['idCardNo'] = jiaoZhengParam_17['population.idCardNo']    
            jiaoZhengCheckParam_17['name'] = jiaoZhengParam_17['population.name'] 
            ret_02 = ShiYouRenKouIntf.check_sheQuJiaoZheng(jiaoZhengCheckParam_17, orgId=jiaoZhengParam_17['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
            self.assertTrue(ret_02, '查找社区矫正人员失败')        
        else:  
            responseDict = ShiYouRenKouIntf.add_sheQuJiaoZheng(sheQuJiaoZhengDict=jiaoZhengParam_17, username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增社区矫正人员失败')       
            jiaoZhengCheckParam_17['name'] = jiaoZhengParam_17['population.name'] 
            ret_03 = ShiYouRenKouIntf.check_sheQuJiaoZheng(jiaoZhengCheckParam_17, orgId=jiaoZhengParam_17['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
            self.assertTrue(ret_03, '查找社区矫正人员失败')  
            
        ret = ShiYouRenKouIntf.check_LiuDongpopulation(jiaoZhengCheckParam_17, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '没有检查到流动人口下对应的社区矫正人员信息')  
        #社区矫正修改
        updPara=copy.deepcopy(jiaoZhengParam_17)
        updPara['mode']='edit'
        updPara['population.id']=json.loads(responseDict.text)['id']
        updPara['population.name']='矫正人员'+createRandomString()
        updPara['population.accusation']='矫正罪名'+createRandomString()
        updPara['population.usedName']='曾用名'+createRandomString()
        responseDict = ShiYouRenKouIntf.add_sheQuJiaoZheng(sheQuJiaoZhengDict=updPara, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增社区矫正人员失败')       
        jiaoZhengCheckParam_17['name'] = updPara['population.name'] 
        ret_04 = ShiYouRenKouIntf.check_sheQuJiaoZheng(jiaoZhengCheckParam_17, orgId=updPara['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret_04, '查找社区矫正人员失败')
        Log.LogOutput(message='修改验证通过')
        #删除
        ShiYouRenKouIntf.delete_JiaoZhengRenYuan(sheQuJiaoZhengDict={'populationIds':updPara['population.id']}, username = userInit['DftWangGeUser'], password='11111111')
        ret_05 = ShiYouRenKouIntf.check_sheQuJiaoZheng(jiaoZhengCheckParam_17, orgId=updPara['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret_05, '查询验证失败')
        Log.LogOutput(message='查询验证成功')                  
        pass 
    
    def testJiaoZhengSearch_17(self):
        addPara1 = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
        addPara1['mode']='add'
        addPara1['population.organization.id'] = orgInit['DftWangGeOrgId']
        addPara1['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['liuDongRenKou']  #属于户籍人口or流动人口
        addPara1['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['sheQuJiaoZhengRenYuan']
        addPara1['population.organization.orgName'] = orgInit['DftWangGeOrg']
        addPara1['population.idCardNo'] = '331100199711200001'
        addPara1['population.name'] = '矫正人员'+createRandomString()
        addPara1['actualPersonType'] = addPara1['population.actualPopulationType']
        addPara1['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        addPara1['population.isHaveHouse1'] = 'null'   
        addPara1['population.accusation'] = '矫正罪名'+createRandomString()
        addPara1['population.executeType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '监外执行罪犯'") 
        addPara1['population.rectifyStartDate'] = '2015-12-01'
        addPara1['population.rectifyEndDate'] = '2015-12-31'
        addPara1['population.nativePlaceAddress']='户籍地详址'+createRandomString() 
        responseDict = ShiYouRenKouIntf.add_sheQuJiaoZheng(sheQuJiaoZhengDict=addPara1, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增社区矫正人员失败')
        #第二条
        addPara2 = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
        addPara2['mode']='add'
        addPara2['population.organization.id'] = orgInit['DftWangGeOrgId']
        addPara2['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['liuDongRenKou']  #属于户籍人口or流动人口
        addPara2['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['sheQuJiaoZhengRenYuan']
        addPara2['population.organization.orgName'] = orgInit['DftWangGeOrg']
        addPara2['population.idCardNo'] = '331100199711200002'
        addPara2['population.name'] = '矫正人员'+createRandomString()
        addPara2['actualPersonType'] = addPara2['population.actualPopulationType']
        addPara2['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        addPara2['population.isHaveHouse1'] = 'null'   
        addPara2['population.accusation'] = '矫正罪名'+createRandomString()
        addPara2['population.executeType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '监外执行罪犯'") 
        addPara2['population.rectifyStartDate'] = '2016-2-01'
        addPara2['population.rectifyEndDate'] = '2016-2-29'  
        addPara2['population.nativePlaceAddress']='户籍地详址'+createRandomString()    
        responseDict = ShiYouRenKouIntf.add_sheQuJiaoZheng(sheQuJiaoZhengDict=addPara2, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增社区矫正人员失败')               
        #根据姓名快速检索
        searchPara1=copy.deepcopy(ShiYouRenKouPara.fastSearch)
        searchPara1['organizationId']=orgInit['DftWangGeOrgId']
        searchPara1['searchRectificativePersonVo.isEmphasis']='0'
        searchPara1['searchRectificativePersonVo.fastSearchKeyWords']= addPara1['population.name']
        checkPara1={'name':addPara1['population.name']}
        checkPara2={'name':addPara2['population.name']}
        result11=ShiYouRenKouIntf.checkJiaoZhengFastSearchList(checkpara=checkPara1,searchpara=searchPara1)
        self.assertTrue(result11, '通过姓名快速查询失败')
        result12=ShiYouRenKouIntf.checkJiaoZhengFastSearchList(checkpara=checkPara2,searchpara=searchPara1)
        self.assertFalse(result12,'通过姓名快速查询失败')
        Log.LogOutput( message='通过姓名快速查询验证成功！')
        #根据身份证快速查询
        searchPara2=copy.deepcopy(searchPara1)
        searchPara2['searchRectificativePersonVo.fastSearchKeyWords']= addPara1['population.idCardNo']
        result21=ShiYouRenKouIntf.checkJiaoZhengFastSearchList(checkpara=checkPara1,searchpara=searchPara2)
        self.assertTrue(result21, '通过身份证快速查询失败')
        result22=ShiYouRenKouIntf.checkJiaoZhengFastSearchList(checkpara=checkPara2,searchpara=searchPara2)
        self.assertFalse(result22,'通过身份证快速查询失败')
        Log.LogOutput( message='通过身份证快速查询验证成功！')
        #高级搜索,通过户籍地详址搜索  
        searchPara3=copy.deepcopy(ShiYouRenKouPara.jiaoZhengSeniorSearch)
        searchPara3['organizationId']=orgInit['DftWangGeOrgId']
        searchPara3['searchRectificativePersonVo.nativePlaceAddress']= addPara1['population.nativePlaceAddress']
        result31=ShiYouRenKouIntf.checkJiaoZhengSeniorSearchList(checkpara=checkPara1,searchpara=searchPara3)
        self.assertTrue(result31, '通过户籍地详址高级查询失败')
        result32=ShiYouRenKouIntf.checkJiaoZhengSeniorSearchList(checkpara=checkPara2,searchpara=searchPara3)
        self.assertFalse(result32,'通过户籍地详址高级查询失败')
        Log.LogOutput( message='通过户籍地详址高级查询验证成功！')         
        #高级搜索,通过矫正日期搜索
        searchPara4=copy.deepcopy(ShiYouRenKouPara.jiaoZhengSeniorSearch)
        searchPara4['organizationId']=orgInit['DftWangGeOrgId']
        searchPara4['searchRectificativePersonVo.rectifyStartDate']= addPara1['population.rectifyStartDate']
        searchPara4['searchRectificativePersonVo.rectifyEndDate']=addPara1['population.rectifyEndDate']
        result41=ShiYouRenKouIntf.checkJiaoZhengSeniorSearchList(checkpara=checkPara1,searchpara=searchPara4)
        self.assertTrue(result41, '通过矫正日期高级查询失败')
        result42=ShiYouRenKouIntf.checkJiaoZhengSeniorSearchList(checkpara=checkPara2,searchpara=searchPara4)
        self.assertFalse(result42,'通过矫正日期高级查询失败')
        Log.LogOutput( message='通过矫正日期高级查询验证成功！')                    
        pass
    
    def testJiaoZhengTransfer_18(self):
        """重点人员>社区矫正人员转为刑满释放人员"""

        jiaoZhengParam_18 = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
        jiaoZhengParam_18['mode']='add'
        jiaoZhengParam_18['population.organization.id'] = orgInit['DftWangGeOrgId']
        jiaoZhengParam_18['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']
        jiaoZhengParam_18['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['sheQuJiaoZhengRenYuan']
        jiaoZhengParam_18['population.organization.orgName'] = orgInit['DftWangGeOrg']
        jiaoZhengParam_18['population.idCardNo'] = '331110199711220005'
        jiaoZhengParam_18['population.name'] = '矫正人员'
        jiaoZhengParam_18['actualPersonType'] = jiaoZhengParam_18['population.actualPopulationType']
        jiaoZhengParam_18['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        jiaoZhengParam_18['population.isHaveHouse1'] = 'null'   
        jiaoZhengParam_18['population.accusation'] = '矫正罪名'
        jiaoZhengParam_18['population.executeType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '监外执行罪犯'") 
        jiaoZhengParam_18['population.rectifyStartDate'] = '2015-12-01'
        jiaoZhengParam_18['population.rectifyEndDate'] = '2015-12-31'     
        responseDict = ShiYouRenKouIntf.add_sheQuJiaoZheng(sheQuJiaoZhengDict=jiaoZhengParam_18, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增社区矫正人员失败')       
          
        transferParam = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
        transferParam['mode']='add'
        transferParam['population.organization.id'] = jiaoZhengParam_18['population.organization.id'] 
        transferParam['population.actualPopulationType'] = jiaoZhengParam_18['population.actualPopulationType']
        transferParam['population.attentionPopulationType'] = jiaoZhengParam_18['population.attentionPopulationType'] 
        transferParam['population.organization.orgName'] = jiaoZhengParam_18['population.organization.orgName']
        transferParam['population.idCardNo'] = jiaoZhengParam_18['population.idCardNo']
        transferParam['population.name'] = jiaoZhengParam_18['population.name']
        transferParam['actualPersonType'] = jiaoZhengParam_18['actualPersonType']
        transferParam['population.gender.id'] = jiaoZhengParam_18['population.gender.id']
        transferParam['population.isHaveHouse1'] = jiaoZhengParam_18['population.isHaveHouse1']  
        transferParam['population.caseReason'] = '刑释原因'
        transferParam['population.positiveInfoType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '刑释人员'") 
        transferParam['population.laborEduAddress'] = '劳教所'
        transferParam['population.imprisonmentDate'] = '2周'
        transferParam['population.releaseOrBackDate'] = '2015-12-01'             
        ret = ShiYouRenKouIntf.transfer_JiaoZhengRenYuan(transferParam,username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(ret.result, '转为刑满释放失败') 
        
        CheckParam = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        CheckParam['name'] = jiaoZhengParam_18['population.name']       
        CheckParam['idCardNo'] = jiaoZhengParam_18['population.idCardNo']
        ret_01 = ShiYouRenKouIntf.check_xingManShiFang(CheckParam, orgId=jiaoZhengParam_18['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret_01, '在刑释人员列表下检查到转移的人口信息') 
        
        ret_02 = ShiYouRenKouIntf.check_sheQuJiaoZheng(CheckParam, orgId=jiaoZhengParam_18['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret_02, '已转移的人口在列表中依然存在，转移失败') 
        
        pass   

    def testJiaoZhengPopulationImportAndDownLoad_30(self):
        """重点人员>矫正人员信息 导入/导出"""
         
        importHuJiparam = copy.deepcopy(ShiYouRenKouPara.data)
        importHuJiparam['dataType']='rectificativePerson'
        importHuJiparam['templates']='RECTIFICATIVEPERSON_syncActualPopulation'
        files = {'upload': ('test.xls', open('C:/autotest_file/importJiaoZhengPopulation.xls', 'rb'),'applicationnd.ms-excel')}
        ret = ShiYouRenKouIntf.import_RenKou(importHuJiparam, files=files,username=userInit['DftWangGeUser'], password='11111111')         
        
        param = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        param['name'] = '矫正导入测试'      
        param['idCardNo'] = '111111111111174'
        ret = ShiYouRenKouIntf.check_sheQuJiaoZheng(param, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找社区矫正人员失败') 
                                
        downLoadHuJiparam = copy.deepcopy(ShiYouRenKouPara.dlZhongDianData)
        downLoadHuJiparam['organizationId']=orgInit['DftWangGeOrgId']
        response = ShiYouRenKouIntf.downLoad_JiaoZhengRenYuan(downLoadHuJiparam, username=userInit['DftWangGeUser'], password='11111111')         
        with open("C:/autotest_file/downLoadJiaoZhengPopulation.xls", "wb") as code:
            code.write(response.content)
            
        ret = CommonUtil.checkExcelCellValue(param['name'], 'downLoadJiaoZhengPopulation.xls','社区矫正人员清单', 'A4')          
        self.assertTrue(ret, '导出失败')
                         
        pass

   
    def testJingShenBingPopulationAdd_17(self):
        """重点人员>精神病人员新增"""
  
        psychosisParam_17= copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
        psychosisParam_17['mode']='add'
        psychosisParam_17['population.organization.id'] = orgInit['DftWangGeOrgId']
        psychosisParam_17['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人口or流动人口
        psychosisParam_17['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['jingShenBingRenYuan']
        psychosisParam_17['population.organization.orgName'] = orgInit['DftWangGeOrg']
        psychosisParam_17['population.idCardNo'] = '332200199711220000'
        psychosisParam_17['population.name'] = '精神病人员'
        psychosisParam_17['actualPersonType'] = psychosisParam_17['population.actualPopulationType']
        psychosisParam_17['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        psychosisParam_17['population.isHaveHouse1'] = 'null'   
        psychosisParam_17['population.dangerLevel.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='危险程度', displayName='低')   
        responseDict = ShiYouRenKouIntf.add_jingShengBingRenYuan(psychosisDict=psychosisParam_17, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增精神病人员失败')       
          
        psychosisCheckParam_17 = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        psychosisCheckParam_17['name'] = psychosisParam_17['population.name']       
        psychosisCheckParam_17['idCardNo'] = psychosisParam_17['population.idCardNo']
        ret = ShiYouRenKouIntf.check_jingShengBingRenYuan(psychosisCheckParam_17, orgId=psychosisParam_17['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找精神病人员失败')   
        
        ret = ShiYouRenKouIntf.check_HuJiPopulation(psychosisCheckParam_17, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '没有检查到户籍人口下对应的精神病人员信息')
        #补充修改用例
        updPara=copy.deepcopy(psychosisParam_17)
        updPara['mode']='edit'
        updPara['population.id']=json.loads(responseDict.text)['id']
        updPara['population.name']='精神病人员'+createRandomString()
        updPara['population.dangerLevel.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='危险程度', displayName='中')
        responseDict = ShiYouRenKouIntf.add_jingShengBingRenYuan(psychosisDict=updPara, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改精神病人员失败')
        #验证修改功能
        psychosisCheckParam_17['name']= updPara['population.name']
        ret = ShiYouRenKouIntf.check_jingShengBingRenYuan(psychosisCheckParam_17, orgId=updPara['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找精神病人员失败')
        Log.LogOutput( message='修改验证通过')
        #删除
        res=ShiYouRenKouIntf.delete_jingShengBingRenYuan(psychosisDict={'populationIds':updPara['population.id']}, username = userInit['DftWangGeUser'], password = '11111111')
        self.assertTrue(res.result, '删除失败')
        #验证删除功能
        psychosisCheckParam_17['name']= updPara['population.name']
        ret = ShiYouRenKouIntf.check_jingShengBingRenYuan(psychosisCheckParam_17, orgId=updPara['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '查找精神病人员失败')
        Log.LogOutput( message='删除验证通过')
        pass 
    def testJingShenBingSearch_17(self):
        '''精神病人员查询'''
        #第一条
        addPara1= copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
        addPara1['mode']='add'
        addPara1['population.organization.id'] = orgInit['DftWangGeOrgId']
        addPara1['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人口or流动人口
        addPara1['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['jingShenBingRenYuan']
        addPara1['population.organization.orgName'] = orgInit['DftWangGeOrg']
        addPara1['population.idCardNo'] = '332200199711220001'
        addPara1['population.name'] = '精神病人员'+createRandomString()
        addPara1['actualPersonType'] = addPara1['population.actualPopulationType']
        addPara1['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        addPara1['population.isHaveHouse1'] = 'null'   
        addPara1['population.dangerLevel.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='危险程度', displayName='低')
        addPara1['population.nativePlaceAddress']='户籍地详址'+createRandomString()   
        responseDict = ShiYouRenKouIntf.add_jingShengBingRenYuan(psychosisDict=addPara1, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增精神病人员失败')
        #第二条
        addPara2= copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
        addPara2['mode']='add'
        addPara2['population.organization.id'] = orgInit['DftWangGeOrgId']
        addPara2['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人口or流动人口
        addPara2['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['jingShenBingRenYuan']
        addPara2['population.organization.orgName'] = orgInit['DftWangGeOrg']
        addPara2['population.idCardNo'] = '332200199711220002'
        addPara2['population.name'] = '精神病人员'+createRandomString()
        addPara2['actualPersonType'] = addPara2['population.actualPopulationType']
        addPara2['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='女')
        addPara2['population.isHaveHouse1'] = 'null'   
        addPara2['population.dangerLevel.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='危险程度', displayName='中')
        addPara2['population.nativePlaceAddress']='户籍地详址'+createRandomString()   
        responseDict = ShiYouRenKouIntf.add_jingShengBingRenYuan(psychosisDict=addPara2, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增精神病人员失败')
        #根据姓名快速检索
        searchPara1=copy.deepcopy(ShiYouRenKouPara.fastSearch)
        searchPara1['organizationId']=orgInit['DftWangGeOrgId']
        searchPara1['searchMentalPatientVo.isEmphasis']='0'
        searchPara1['searchMentalPatientVo.fastSearchKeyWords']= addPara1['population.name']
        checkPara1={'name':addPara1['population.name']}
        checkPara2={'name':addPara2['population.name']}
        result11=ShiYouRenKouIntf.checkJingShenBingFastSearchList(checkpara=checkPara1,searchpara=searchPara1)
        self.assertTrue(result11, '通过姓名快速查询失败')
        result12=ShiYouRenKouIntf.checkJingShenBingFastSearchList(checkpara=checkPara2,searchpara=searchPara1)
        self.assertFalse(result12,'通过姓名快速查询失败')
        Log.LogOutput( message='通过姓名快速查询验证成功！')
        #根据身份证快速查询
        searchPara2=copy.deepcopy(searchPara1)
        searchPara2['searchMentalPatientVo.fastSearchKeyWords']= addPara1['population.idCardNo']
        result21=ShiYouRenKouIntf.checkJingShenBingFastSearchList(checkpara=checkPara1,searchpara=searchPara2)
        self.assertTrue(result21, '通过身份证快速查询失败')
        result22=ShiYouRenKouIntf.checkJingShenBingFastSearchList(checkpara=checkPara2,searchpara=searchPara2)
        self.assertFalse(result22,'通过身份证快速查询失败')
        Log.LogOutput( message='通过身份证快速查询验证成功！')
        #高级搜索,通过户籍地详址搜索  
        searchPara3=copy.deepcopy(ShiYouRenKouPara.seniorSearch)
        searchPara3['organizationId']=orgInit['DftWangGeOrgId']
        searchPara3['searchMentalPatientVo.isEmphasis']='-1'
        searchPara3['searchMentalPatientVo.isDeath']='-1'
        searchPara3['searchMentalPatientVo.hasIsTreatType.code']='-1'
        searchPara3['searchMentalPatientVo.hasServiceTeamMember']='-1'
        searchPara3['searchMentalPatientVo.hasServiceTeamRecord']='-1'
        searchPara3['searchMentalPatientVo.nativePlaceAddress']= addPara1['population.nativePlaceAddress']
        result31=ShiYouRenKouIntf.checkJingShenBingSeniorSearchList(checkpara=checkPara1,searchpara=searchPara3)
        self.assertTrue(result31, '通过户籍地详址高级查询失败')
        result32=ShiYouRenKouIntf.checkJingShenBingSeniorSearchList(checkpara=checkPara2,searchpara=searchPara3)
        self.assertFalse(result32,'通过户籍地详址高级查询失败')
        Log.LogOutput( message='通过户籍地详址高级查询验证成功！')         
        #高级搜索,通过性别搜索
        searchPara4=copy.deepcopy(searchPara3)
        searchPara4['organizationId']=orgInit['DftWangGeOrgId']
        searchPara4['searchMentalPatientVo.genderId']= addPara1['population.gender.id']
        searchPara4['searchMentalPatientVo.nativePlaceAddress']=''
        result41=ShiYouRenKouIntf.checkJingShenBingSeniorSearchList(checkpara=checkPara1,searchpara=searchPara4)
        self.assertTrue(result41, '通过性别高级查询失败')
        result42=ShiYouRenKouIntf.checkJingShenBingSeniorSearchList(checkpara=checkPara2,searchpara=searchPara4)
        self.assertFalse(result42,'通过性别高级查询失败')
        Log.LogOutput( message='通过性别高级查询验证成功！')         
        
        pass
    def testJingShenBingPopulationImportAndDownLoad_31(self):
        """重点人员>精神病人员信息 导入/导出"""
         
        importHuJiparam = copy.deepcopy(ShiYouRenKouPara.data)
        importHuJiparam['dataType']='mentalPatient'
        importHuJiparam['templates']='MENTALPATIENT_syncActualPopulation'
        files = {'upload': ('test.xls', open('C:/autotest_file/importJingShenBingPopulation.xls', 'rb'),'applicationnd.ms-excel')}
        ret = ShiYouRenKouIntf.import_RenKou(importHuJiparam, files=files,username=userInit['DftWangGeUser'], password='11111111')         
        
        param = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        param['name'] = '精神病人员导入测试'      
        param['idCardNo'] = '111111111111175'
        ret = ShiYouRenKouIntf.check_jingShengBingRenYuan(param, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找精神病人员失败') 
                                
        downLoadHuJiparam = copy.deepcopy(ShiYouRenKouPara.dlZhongDianData)
        downLoadHuJiparam['organizationId']=orgInit['DftWangGeOrgId']
        response = ShiYouRenKouIntf.downLoad_jingShengBingRenYuan(downLoadHuJiparam, username=userInit['DftWangGeUser'], password='11111111')         
        with open("C:/autotest_file/downLoadjingShengBingPopulation.xls", "wb") as code:
            code.write(response.content)
            
        ret = CommonUtil.checkExcelCellValue(param['name'], 'downLoadjingShengBingPopulation.xls','精神病人员清单', 'A4')          
        self.assertTrue(ret, '导出失败')
                         
        pass


    def testXiDuPopulationAdd_17(self):
        """重点人员>吸毒人员新增"""
  
        xiDuParam_17 = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
        xiDuParam_17['mode']='add'
        xiDuParam_17['population.organization.id'] = orgInit['DftWangGeOrgId']
        xiDuParam_17['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于会人口or流动人口
        xiDuParam_17['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['xiDuRenYuan']
        xiDuParam_17['population.organization.orgName'] = orgInit['DftWangGeOrg']
        xiDuParam_17['population.idCardNo'] = '333300199711220000'
        xiDuParam_17['population.name'] = '吸毒人员'
        xiDuParam_17['actualPersonType'] = xiDuParam_17['population.actualPopulationType']
        xiDuParam_17['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        xiDuParam_17['population.isHaveHouse1'] = 'null'   
        xiDuParam_17['population.detoxicateCase.id'] = CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '强制戒毒'")  
        responseDict = ShiYouRenKouIntf.add_xiDuRenYuan(xiDuRenYuanDict=xiDuParam_17, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增吸毒人员失败')       
          
        druggyCheckParam_17 = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        druggyCheckParam_17['name'] = xiDuParam_17['population.name']       
        druggyCheckParam_17['idCardNo'] = xiDuParam_17['population.idCardNo']
        ret = ShiYouRenKouIntf.check_xiDuRenYuan(druggyCheckParam_17, orgId=xiDuParam_17['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找吸毒人员失败')   
        
        ret = ShiYouRenKouIntf.check_HuJiPopulation(druggyCheckParam_17, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '没有检查到户籍人口下对应的吸毒人员信息')
        #补充修改用例
        updPara=copy.deepcopy(xiDuParam_17)
        updPara['mode']='edit'
        updPara['population.id']=json.loads(responseDict.text)['id']
        updPara['population.name']='吸毒人员'+createRandomString()
        updPara['population.detoxicateCase.id'] = CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '自愿戒毒'")  
        responseDict = ShiYouRenKouIntf.add_xiDuRenYuan(xiDuRenYuanDict=updPara, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改吸毒人员失败')
        #验证修改功能
        druggyCheckParam_17['name']= updPara['population.name']
        ret = ShiYouRenKouIntf.check_xiDuRenYuan(druggyCheckParam_17, orgId=updPara['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找吸毒人员失败')
        Log.LogOutput( message='修改功能验证通过')
        #删除
        res=ShiYouRenKouIntf.delete_xiDuRenYuan(xiDuRenYuanDict={'populationIds':updPara['population.id']}, username = userInit['DftWangGeUser'], password = '11111111')
        self.assertTrue(res.result, '删除失败')
        #验证删除功能
        druggyCheckParam_17['name']= updPara['population.name']
        ret = ShiYouRenKouIntf.check_xiDuRenYuan(druggyCheckParam_17, orgId=updPara['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '删除失败')
        Log.LogOutput( message='删除验证通过')     
        pass 
    def testXiDuSearch_17(self):
        '''吸毒人员查询'''
        addPara1 = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
        addPara1['mode']='add'
        addPara1['population.organization.id'] = orgInit['DftWangGeOrgId']
        addPara1['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于会人口or流动人口
        addPara1['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['xiDuRenYuan']
        addPara1['population.organization.orgName'] = orgInit['DftWangGeOrg']
        addPara1['population.idCardNo'] = '333300198711220001'
        addPara1['population.name'] = '吸毒人员'+createRandomString()
        addPara1['actualPersonType'] = addPara1['population.actualPopulationType']
        addPara1['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        addPara1['population.isHaveHouse1'] = 'null'   
        addPara1['population.detoxicateCase.id'] = CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '强制戒毒'")  
        addPara1['population.nativePlaceAddress']='户籍地详址'+createRandomString()
        addPara1['population.drugType']='毒品种类'+createRandomString()
        responseDict = ShiYouRenKouIntf.add_xiDuRenYuan(xiDuRenYuanDict=addPara1, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增吸毒人员失败')       
        #第二条
        addPara2 = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
        addPara2['mode']='add'
        addPara2['population.organization.id'] = orgInit['DftWangGeOrgId']
        addPara2['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于会人口or流动人口
        addPara2['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['xiDuRenYuan']
        addPara2['population.organization.orgName'] = orgInit['DftWangGeOrg']
        addPara2['population.idCardNo'] = '333300198711220002'
        addPara2['population.name'] = '吸毒人员'+createRandomString()
        addPara2['actualPersonType'] = addPara2['population.actualPopulationType']
        addPara2['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        addPara2['population.isHaveHouse1'] = 'null'   
        addPara2['population.detoxicateCase.id'] = CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '强制戒毒'")  
        addPara2['population.nativePlaceAddress']='户籍地详址'+createRandomString()
        addPara2['population.drugType']='毒品种类'+createRandomString()
        responseDict = ShiYouRenKouIntf.add_xiDuRenYuan(xiDuRenYuanDict=addPara2, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增吸毒人员失败')       
        #根据姓名快速检索
        searchPara1=copy.deepcopy(ShiYouRenKouPara.fastSearch)
        searchPara1['organizationId']=orgInit['DftWangGeOrgId']
        searchPara1['searchDruggyVo.isEmphasis']='0'
        searchPara1['searchDruggyVo.fastSearchKeyWords']= addPara1['population.name']
        checkPara1={'name':addPara1['population.name']}
        checkPara2={'name':addPara2['population.name']}
        result11=ShiYouRenKouIntf.checkXiDuFastSearchList(checkpara=checkPara1,searchpara=searchPara1)
        self.assertTrue(result11, '通过姓名快速查询失败')
        result12=ShiYouRenKouIntf.checkXiDuFastSearchList(checkpara=checkPara2,searchpara=searchPara1)
        self.assertFalse(result12,'通过姓名快速查询失败')
        Log.LogOutput( message='通过姓名快速查询验证成功！')
        #根据身份证快速查询
        searchPara2=copy.deepcopy(searchPara1)
        searchPara2['searchDruggyVo.fastSearchKeyWords']= addPara1['population.idCardNo']
        result21=ShiYouRenKouIntf.checkXiDuFastSearchList(checkpara=checkPara1,searchpara=searchPara2)
        self.assertTrue(result21, '通过身份证快速查询失败')
        result22=ShiYouRenKouIntf.checkXiDuFastSearchList(checkpara=checkPara2,searchpara=searchPara2)
        self.assertFalse(result22,'通过身份证快速查询失败')
        Log.LogOutput( message='通过身份证快速查询验证成功！')
        #高级搜索,通过户籍地详址搜索  
        searchPara3=copy.deepcopy(ShiYouRenKouPara.seniorSearch)
        searchPara3['organizationId']=orgInit['DftWangGeOrgId']
        searchPara3['searchDruggyVo.isEmphasis']='-1'
        searchPara3['searchDruggyVo.isDeath']='-1'
        searchPara3['searchDruggyVo.hasIsTreatType.code']='-1'
        searchPara3['searchDruggyVo.hasServiceTeamMember']='-1'
        searchPara3['searchDruggyVo.hasServiceTeamRecord']='-1'
        searchPara3['searchDruggyVo.nativePlaceAddress']= addPara1['population.nativePlaceAddress']
        result31=ShiYouRenKouIntf.checkXiDuSeniorSearchList(checkpara=checkPara1,searchpara=searchPara3)
        self.assertTrue(result31, '通过户籍地详址高级查询失败')
        result32=ShiYouRenKouIntf.checkXiDuSeniorSearchList(checkpara=checkPara2,searchpara=searchPara3)
        self.assertFalse(result32,'通过户籍地详址高级查询失败')
        Log.LogOutput( message='通过户籍地详址高级查询验证成功！')         
        #高级搜索,通过滥用毒品种类搜索
        searchPara4=copy.deepcopy(searchPara3)
        searchPara4['organizationId']=orgInit['DftWangGeOrgId']
        searchPara4['searchDruggyVo.drugType']= addPara1['population.drugType']
        searchPara4['searchDruggyVo.nativePlaceAddress']=''
        result41=ShiYouRenKouIntf.checkXiDuSeniorSearchList(checkpara=checkPara1,searchpara=searchPara4)
        self.assertTrue(result41, '通过滥用毒品种类高级查询失败')
        result42=ShiYouRenKouIntf.checkXiDuSeniorSearchList(checkpara=checkPara2,searchpara=searchPara4)
        self.assertFalse(result42,'通过滥用毒品种类高级查询失败')
        Log.LogOutput( message='通过滥用毒品种类高级查询验证成功！')  


        
        pass
    def testXiDuPopulationImportAndDownLoad_32(self):
        """重点人员>吸毒人员信息 导入/导出"""
         
        importHuJiparam = copy.deepcopy(ShiYouRenKouPara.data)
        importHuJiparam['dataType']='druggy'
        importHuJiparam['templates']='DRUGGY_syncActualPopulation'
        files = {'upload': ('test.xls', open('C:/autotest_file/importXiDuPopulation.xls', 'rb'),'applicationnd.ms-excel')}
        ret = ShiYouRenKouIntf.import_RenKou(importHuJiparam, files=files,username=userInit['DftWangGeUser'], password='11111111')         
        
        param = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        param['name'] = '吸毒人员导入测试'      
        param['idCardNo'] = '111111111111176'
        ret = ShiYouRenKouIntf.check_xiDuRenYuan(param, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找吸毒人员失败') 
                                
        downLoadHuJiparam = copy.deepcopy(ShiYouRenKouPara.dlZhongDianData)
        downLoadHuJiparam['organizationId']=orgInit['DftWangGeOrgId']
        response = ShiYouRenKouIntf.downLoad_xiDuRenYuan(downLoadHuJiparam, username=userInit['DftWangGeUser'], password='11111111')         
        with open("C:/autotest_file/downLoadXiDuPopulation.xls", "wb") as code:
            code.write(response.content)
            
        ret = CommonUtil.checkExcelCellValue(param['name'], 'downLoadXiDuPopulation.xls','吸毒人员表', 'A4')          
        self.assertTrue(ret, '导出失败')
                         
        pass


    def testZhongDianQingShaoNianAdd_17(self):
        """重点人员>重点青少年新增"""
        ShiYouRenKouIntf.zhongDianQingShaoNianDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        qingShaoNianParam_17 = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
        qingShaoNianParam_17['mode']='add'
        qingShaoNianParam_17['population.organization.id'] = orgInit['DftWangGeOrgId']
        qingShaoNianParam_17['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人口or流动人口
        qingShaoNianParam_17['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['zhongDianQingShaoNian']
        qingShaoNianParam_17['population.organization.orgName'] = orgInit['DftWangGeOrg']
        qingShaoNianParam_17['population.idCardNo'] = '334400199711220000'
        qingShaoNianParam_17['population.name'] = '重点青少年'
        qingShaoNianParam_17['actualPersonType'] = qingShaoNianParam_17['population.actualPopulationType']
        qingShaoNianParam_17['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        qingShaoNianParam_17['population.isHaveHouse1'] = 'null'  
        qingShaoNianParam_17['staffTypeIds'] =CommonIntf.getIdByDomainAndDisplayName(domainName='闲散青少年人员类型', displayName='闲散青少年')     #人员类型，根据字段找对应id    
        responseDict = ShiYouRenKouIntf.add_zhongDianQingShaoNian(qingShaoNianDict=qingShaoNianParam_17, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增重点青少年失败')       
          
        idleYouthCheckParam_17 = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        idleYouthCheckParam_17['name'] = qingShaoNianParam_17['population.name']       
        idleYouthCheckParam_17['idCardNo'] = qingShaoNianParam_17['population.idCardNo']
        ret = ShiYouRenKouIntf.check_zhongDianQingShaoNian(idleYouthCheckParam_17, orgId=qingShaoNianParam_17['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找重点青少年失败')

        ret = ShiYouRenKouIntf.check_HuJiPopulation(idleYouthCheckParam_17, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '没有检查到户籍人口下对应的重点青少年人员信息')
#         ShiYouRenKouIntf.zhongDianQingShaoNianDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        #补充修改用例
        updPara=copy.deepcopy(qingShaoNianParam_17)
        updPara['mode']='edit'
        updPara['population.id']=json.loads(responseDict.text)['id']
        updPara['population.name']='重点青少年'+createRandomString()
        updPara['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='女')
        responseDict = ShiYouRenKouIntf.add_zhongDianQingShaoNian(qingShaoNianDict=updPara, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改重点青少年失败')
        #验证修改功能
        idleYouthCheckParam_17['name']= updPara['population.name']
        ret = ShiYouRenKouIntf.check_zhongDianQingShaoNian(idleYouthCheckParam_17, orgId=updPara['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找重点青少年失败')
        Log.LogOutput( message='修改功能验证通过')
        #删除
        res=ShiYouRenKouIntf.delete_zhongDianQingShaoNian(qingShaoNianDict={'populationIds':updPara['population.id']}, username = userInit['DftWangGeUser'], password = '11111111')
        self.assertTrue(res.result, '删除失败')
        #验证删除功能
        idleYouthCheckParam_17['name']= updPara['population.name']
        ret = ShiYouRenKouIntf.check_zhongDianQingShaoNian(idleYouthCheckParam_17, orgId=updPara['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '删除失败')
        Log.LogOutput( message='删除验证通过')
        pass 

    def testZhongDianQingShaoNianSearch_17(self):
        '''重点青少年查询'''
        ShiYouRenKouIntf.zhongDianQingShaoNianDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        addPara1 = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
        addPara1['mode']='add'
        addPara1['population.organization.id'] = orgInit['DftWangGeOrgId']
        addPara1['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人口or流动人口
        addPara1['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['zhongDianQingShaoNian']
        addPara1['population.organization.orgName'] = orgInit['DftWangGeOrg']
        addPara1['population.idCardNo'] = '334400199711220001'
        addPara1['population.name'] = '重点青少年'+createRandomString()
        addPara1['actualPersonType'] = addPara1['population.actualPopulationType']
        addPara1['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        addPara1['population.isHaveHouse1'] = 'null'   
        addPara1['staffTypeIds'] =CommonIntf.getIdByDomainAndDisplayName(domainName='闲散青少年人员类型', displayName='闲散青少年')   #人员类型，根据字段找对应id    
        addPara1['population.nativePlaceAddress']='户籍地详址'+createRandomString()
        responseDict = ShiYouRenKouIntf.add_zhongDianQingShaoNian(qingShaoNianDict=addPara1, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增重点青少年失败')  
        #第二条
        addPara2 = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
        addPara2['mode']='add'
        addPara2['population.organization.id'] = orgInit['DftWangGeOrgId']
        addPara2['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人口or流动人口
        addPara2['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['zhongDianQingShaoNian']
        addPara2['population.organization.orgName'] = orgInit['DftWangGeOrg']
        addPara2['population.idCardNo'] = '334400199711220002'
        addPara2['population.name'] = '重点青少年'+createRandomString()
        addPara2['actualPersonType'] = addPara2['population.actualPopulationType']
        addPara2['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        addPara2['population.isHaveHouse1'] = 'null'   
        addPara2['staffTypeIds']= CommonIntf.getIdByDomainAndDisplayName(domainName='闲散青少年人员类型', displayName='流浪乞讨青少年')
#         addPara2['staffTypeIds'] = CommonIntf.getDbQueryResult(dbCommand="select id from propertydicts pr where pr.displayname = '流浪乞讨青少年' and pr.propertydomainid=(select id from propertydomains where domainName like '闲散青少年人员类型')")   #人员类型，根据字段找对应id    
        addPara2['population.nativePlaceAddress']='户籍地详址'+createRandomString()
        responseDict = ShiYouRenKouIntf.add_zhongDianQingShaoNian(qingShaoNianDict=addPara2, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增重点青少年失败')
        #根据姓名快速检索
        searchPara1=copy.deepcopy(ShiYouRenKouPara.fastSearch)
        searchPara1['organizationId']=orgInit['DftWangGeOrgId']
        searchPara1['searchIdleYouthVo.isEmphasis']='0'
        searchPara1['searchIdleYouthVo.fastSearchKeyWords']= addPara1['population.name']
        checkPara1={'name':addPara1['population.name']}
        checkPara2={'name':addPara2['population.name']}
        result11=ShiYouRenKouIntf.checkZhongDianQingShaoNianFastSearchList(checkpara=checkPara1,searchpara=searchPara1)
        self.assertTrue(result11, '通过姓名快速查询失败')
        result12=ShiYouRenKouIntf.checkZhongDianQingShaoNianFastSearchList(checkpara=checkPara2,searchpara=searchPara1)
        self.assertFalse(result12,'通过姓名快速查询失败')
        Log.LogOutput( message='通过姓名快速查询验证成功！')
        #根据身份证快速查询
        searchPara2=copy.deepcopy(searchPara1)
        searchPara2['searchIdleYouthVo.fastSearchKeyWords']= addPara1['population.idCardNo']
        result21=ShiYouRenKouIntf.checkZhongDianQingShaoNianFastSearchList(checkpara=checkPara1,searchpara=searchPara2)
        self.assertTrue(result21, '通过身份证快速查询失败')
        result22=ShiYouRenKouIntf.checkZhongDianQingShaoNianFastSearchList(checkpara=checkPara2,searchpara=searchPara2)
        self.assertFalse(result22,'通过身份证快速查询失败')
        Log.LogOutput( message='通过身份证快速查询验证成功！')                       
        #高级搜索,通过户籍地详址搜索  
        searchPara3=copy.deepcopy(ShiYouRenKouPara.seniorSearch)
        searchPara3['organizationId']=orgInit['DftWangGeOrgId']
        searchPara3['searchIdleYouthVo.isEmphasis']='-1'
        searchPara3['searchIdleYouthVo.isDeath']='-1'
        searchPara3['searchIdleYouthVo.hasServiceTeamMember']='-1'
        searchPara3['searchIdleYouthVo.hasServiceTeamRecord']='-1'
        searchPara3['searchIdleYouthVo.nativePlaceAddress']= addPara1['population.nativePlaceAddress']
        result31=ShiYouRenKouIntf.checkZhongDianQingShaoNianSeniorSearchList(checkpara=checkPara1,searchpara=searchPara3)
        self.assertTrue(result31, '通过户籍地详址高级查询失败')
        result32=ShiYouRenKouIntf.checkZhongDianQingShaoNianSeniorSearchList(checkpara=checkPara2,searchpara=searchPara3)
        self.assertFalse(result32,'通过户籍地详址高级查询失败')
        Log.LogOutput( message='通过户籍地详址高级查询验证成功！')         
        #高级搜索,通过人员类型搜索
        searchPara4=copy.deepcopy(searchPara3)
        searchPara4['organizationId']=orgInit['DftWangGeOrgId']
        searchPara4['staffTypeIds']= addPara1['staffTypeIds']
        searchPara4['searchIdleYouthVo.nativePlaceAddress']=''
        result41=ShiYouRenKouIntf.checkZhongDianQingShaoNianSeniorSearchList(checkpara=checkPara1,searchpara=searchPara4)
        self.assertTrue(result41, '通过人员类型高级查询失败')
        result42=ShiYouRenKouIntf.checkZhongDianQingShaoNianSeniorSearchList(checkpara=checkPara2,searchpara=searchPara4)
        self.assertFalse(result42,'通过人员类型高级查询失败')
        Log.LogOutput( message='通过人员类型高级查询验证成功！')          
        pass
#重点青少年导出接口同户籍人口


    def testZhongDianShangFangRenYuanAdd_17(self):
        """重点人员>重点上访对象新增"""
  
        shangFangParam_17 = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
        shangFangParam_17['mode']='add'
        shangFangParam_17['population.organization.id'] = orgInit['DftWangGeOrgId']
        shangFangParam_17['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人员or流动人口
        shangFangParam_17['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['zhongDianShangFangRenYuan']
        shangFangParam_17['population.organization.orgName'] = orgInit['DftWangGeOrg']
        shangFangParam_17['population.idCardNo'] = '335500199711220000'
        shangFangParam_17['population.name'] = '重点上访人员'
        shangFangParam_17['actualPersonType'] = shangFangParam_17['population.actualPopulationType']
        shangFangParam_17['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        shangFangParam_17['population.isHaveHouse1'] = 'null'   
        shangFangParam_17['population.visitReason'] = '上访原因'       
        responseDict = ShiYouRenKouIntf.add_shangFangRenYuan(shangFangDict=shangFangParam_17, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增上访人员失败')       
          
        shangFangCheckParam_17 = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        shangFangCheckParam_17['name'] = shangFangParam_17['population.name']       
        shangFangCheckParam_17['idCardNo'] = shangFangParam_17['population.idCardNo']
        ret = ShiYouRenKouIntf.check_shangFangRenYuan(shangFangCheckParam_17, orgId=shangFangParam_17['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找上访人员失败')
        
        ret = ShiYouRenKouIntf.check_HuJiPopulation(shangFangCheckParam_17, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '没有检查到户籍人口下对应的重点上访人员信息')
        #补充修改用例
        updPara=copy.deepcopy(shangFangParam_17)
        updPara['mode']='edit'
        updPara['population.id']=json.loads(responseDict.text)['id']
        updPara['population.name']='重点上访人员'+createRandomString()
        updPara['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='女')
        responseDict = ShiYouRenKouIntf.add_shangFangRenYuan(shangFangDict=updPara, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改重点上访人员失败')
        #验证修改功能
        shangFangCheckParam_17['name']= updPara['population.name']
        ret = ShiYouRenKouIntf.check_shangFangRenYuan(shangFangCheckParam_17, orgId=updPara['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找重点上访人员失败')
        Log.LogOutput( message='修改功能验证通过')
        #删除
        res=ShiYouRenKouIntf.delete_shangFangRenYuan(shangFangDict={'populationIds':updPara['population.id']}, username = userInit['DftWangGeUser'], password = '11111111')
        self.assertTrue(res.result, '删除失败')
        #验证删除功能
        shangFangCheckParam_17['name']= updPara['population.name']
        ret = ShiYouRenKouIntf.check_shangFangRenYuan(shangFangCheckParam_17, orgId=updPara['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '删除失败')
        Log.LogOutput( message='删除验证通过')        
        pass
     
    def testZhongDianShangFangSearch_17(self):
        '''重点上方人员查询'''
        addPara1 = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
        addPara1['mode']='add'
        addPara1['population.organization.id'] = orgInit['DftWangGeOrgId']
        addPara1['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人员or流动人口
        addPara1['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['zhongDianShangFangRenYuan']
        addPara1['population.organization.orgName'] = orgInit['DftWangGeOrg']
        addPara1['population.idCardNo'] = '335500199711220001'
        addPara1['population.name'] = '重点上访人员'+createRandomString()
        addPara1['actualPersonType'] = addPara1['population.actualPopulationType']
        addPara1['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        addPara1['population.isHaveHouse1'] = 'null'   
        addPara1['population.visitReason'] = '上访原因'       
        addPara1['population.nativePlaceAddress']='户籍地详址'+createRandomString()
        addPara1['population.visitState.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='上访状态', displayName='问题已解决')
        responseDict = ShiYouRenKouIntf.add_shangFangRenYuan(shangFangDict=addPara1, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增上访人员失败')
        #第二条
        addPara2 = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
        addPara2['mode']='add'
        addPara2['population.organization.id'] = orgInit['DftWangGeOrgId']
        addPara2['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人员or流动人口
        addPara2['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['zhongDianShangFangRenYuan']
        addPara2['population.organization.orgName'] = orgInit['DftWangGeOrg']
        addPara2['population.idCardNo'] = '335500199711220002'
        addPara2['population.name'] = '重点上访人员'+createRandomString()
        addPara2['actualPersonType'] = addPara2['population.actualPopulationType']
        addPara2['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        addPara2['population.isHaveHouse1'] = 'null'   
        addPara2['population.visitReason'] = '上访原因'       
        addPara2['population.nativePlaceAddress']='户籍地详址'+createRandomString()
        addPara2['population.visitState.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='上访状态', displayName='问题未解决')
        responseDict = ShiYouRenKouIntf.add_shangFangRenYuan(shangFangDict=addPara2, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增上访人员失败')                  
        #根据姓名快速检索
        searchPara1=copy.deepcopy(ShiYouRenKouPara.fastSearch)
        searchPara1['organizationId']=orgInit['DftWangGeOrgId']
        searchPara1['searchSuperiorVisitVo.isEmphasis']='0'
        searchPara1['searchSuperiorVisitVo.fastSearchKeyWords']= addPara1['population.name']
        checkPara1={'name':addPara1['population.name']}
        checkPara2={'name':addPara2['population.name']}
        result11=ShiYouRenKouIntf.checkZhongDianShangFangFastSearchList(checkpara=checkPara1,searchpara=searchPara1)
        self.assertTrue(result11, '通过姓名快速查询失败')
        result12=ShiYouRenKouIntf.checkZhongDianShangFangFastSearchList(checkpara=checkPara2,searchpara=searchPara1)
        self.assertFalse(result12,'通过姓名快速查询失败')
        Log.LogOutput( message='通过姓名快速查询验证成功！')
        #根据身份证快速查询
        searchPara2=copy.deepcopy(searchPara1)
        searchPara2['searchSuperiorVisitVo.fastSearchKeyWords']= addPara1['population.idCardNo']
        result21=ShiYouRenKouIntf.checkZhongDianShangFangFastSearchList(checkpara=checkPara1,searchpara=searchPara2)
        self.assertTrue(result21, '通过身份证快速查询失败')
        result22=ShiYouRenKouIntf.checkZhongDianShangFangFastSearchList(checkpara=checkPara2,searchpara=searchPara2)
        self.assertFalse(result22,'通过身份证快速查询失败')
        Log.LogOutput( message='通过身份证快速查询验证成功！')    
        #高级搜索,通过户籍地详址搜索  
        searchPara3=copy.deepcopy(ShiYouRenKouPara.seniorSearch)
        searchPara3['organizationId']=orgInit['DftWangGeOrgId']
        searchPara3['searchSuperiorVisitVo.isEmphasis']='-1'
        searchPara3['searchSuperiorVisitVo.isDeath']='-1'
        searchPara3['searchSuperiorVisitVo.hasServiceTeamMember']='-1'
        searchPara3['searchSuperiorVisitVo.hasServiceTeamRecord']='-1'
        searchPara3['searchSuperiorVisitVo.nativePlaceAddress']= addPara1['population.nativePlaceAddress']
        result31=ShiYouRenKouIntf.checkZhongDianShangFangSeniorSearchList(checkpara=checkPara1,searchpara=searchPara3)
        self.assertTrue(result31, '通过户籍地详址高级查询失败')
        result32=ShiYouRenKouIntf.checkZhongDianShangFangSeniorSearchList(checkpara=checkPara2,searchpara=searchPara3)
        self.assertFalse(result32,'通过户籍地详址高级查询失败')
        Log.LogOutput( message='通过户籍地详址高级查询验证成功！')         
        #高级搜索,通过上访状态搜索
        searchPara4=copy.deepcopy(searchPara3)
        searchPara4['organizationId']=orgInit['DftWangGeOrgId']
        searchPara4['searchSuperiorVisitVo.visitState.id']= addPara1['population.visitState.id']
        searchPara4['searchSuperiorVisitVo.nativePlaceAddress']=''
        result41=ShiYouRenKouIntf.checkZhongDianShangFangSeniorSearchList(checkpara=checkPara1,searchpara=searchPara4)
        self.assertTrue(result41, '通过上访状态高级查询失败')
        result42=ShiYouRenKouIntf.checkZhongDianShangFangSeniorSearchList(checkpara=checkPara2,searchpara=searchPara4)
        self.assertFalse(result42,'通过上访状态高级查询失败')
        Log.LogOutput( message='通过上访状态高级查询验证成功！')        
        
            
        pass
    def testShangFangPopulationImportAndDownLoad_34(self):
        """重点人员>重点上访人员信息 导入/导出"""
         
        importHuJiparam = copy.deepcopy(ShiYouRenKouPara.data)
        importHuJiparam['dataType']='superiorVisit'
        importHuJiparam['templates']='SUPERIORVISIT_syncActualPopulation'
        files = {'upload': ('test.xls', open('C:/autotest_file/importZhongDianShangFangPopulation.xls', 'rb'),'applicationnd.ms-excel')}
        ret = ShiYouRenKouIntf.import_RenKou(importHuJiparam, files=files,username=userInit['DftWangGeUser'], password='11111111')         
        
        param = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        param['name'] = '重点上访人员导入测试'      
        param['idCardNo'] = '111111111111178'
        ret = ShiYouRenKouIntf.check_shangFangRenYuan(param, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找上访人员失败') 
                                
        downLoadHuJiparam = copy.deepcopy(ShiYouRenKouPara.dlZhongDianData)
        downLoadHuJiparam['organizationId']=orgInit['DftWangGeOrgId']
        response = ShiYouRenKouIntf.downLoad_shangFangRenYuan(downLoadHuJiparam, username=userInit['DftWangGeUser'], password='11111111')         
        with open("C:/autotest_file/downLoadShangFangPopulation.xls", "wb") as code:
            code.write(response.content)
            
        ret = CommonUtil.checkExcelCellValue(param['name'], 'downLoadShangFangPopulation.xls','重点上访人员清单', 'A4')          
        self.assertTrue(ret, '导出失败')
                         
        pass


    def testWeiXianPinCongYeRenYuanAdd_17(self):
        """重点人员>危险品从业人员新增"""
  
        practitionerParam_17 = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
        practitionerParam_17['mode']='add'
        practitionerParam_17['population.organization.id'] = orgInit['DftWangGeOrgId']
        practitionerParam_17['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']   #属于户籍人员or流动人员
        practitionerParam_17['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['weiXianPingCongYeRenYuan']
        practitionerParam_17['population.organization.orgName'] = orgInit['DftWangGeOrg']
        practitionerParam_17['population.idCardNo'] = '336600199711220000'
        practitionerParam_17['population.name'] = '危险品从业人员'
        practitionerParam_17['actualPersonType'] = practitionerParam_17['population.actualPopulationType']
        practitionerParam_17['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        practitionerParam_17['population.isHaveHouse1'] = 'null'   
        practitionerParam_17['population.dangerousWorkingType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='危险从业类别', displayName='其他')  #危险从业类别，选择id
        practitionerParam_17['population.legalPerson'] = '法人代表'  
        practitionerParam_17['population.legalPersonMobileNumber'] = '11111111111' 
        practitionerParam_17['population.legalPersonTelephone'] = '3333333'  
        practitionerParam_17['population.workUnit'] = '工作单位'       
        responseDict = ShiYouRenKouIntf.add_weiXianPingCongYeRenYuan(practitionerDict=practitionerParam_17, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增危险品从业人员失败')       
          
        practitionerCheckParam_17 = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        practitionerCheckParam_17['name'] = practitionerParam_17['population.name']       
        practitionerCheckParam_17['idCardNo'] = practitionerParam_17['population.idCardNo']
        ret = ShiYouRenKouIntf.check_weiXianPingCongYeRenYuan(practitionerCheckParam_17, orgId=practitionerParam_17['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找危险品从业人员失败')
        
        ret = ShiYouRenKouIntf.check_HuJiPopulation(practitionerCheckParam_17, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '没有检查到户籍人口下对应的危险品从业人员信息')
        #补充修改用例
        updPara=copy.deepcopy(practitionerParam_17)
        updPara['mode']='edit'
        updPara['population.id']=json.loads(responseDict.text)['id']
        updPara['population.name']='危险品从业人员'+createRandomString()
        updPara['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='女')
        responseDict = ShiYouRenKouIntf.add_weiXianPingCongYeRenYuan(updPara, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改危险品从业人员失败')
        #验证修改功能
        practitionerCheckParam_17['name']= updPara['population.name']
        ret = ShiYouRenKouIntf.check_weiXianPingCongYeRenYuan(practitionerCheckParam_17, orgId=updPara['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找危险品从业人员失败')
        Log.LogOutput( message='修改功能验证通过')
        #删除
        res=ShiYouRenKouIntf.delete_weiXianPingCongYeRenYuan(practitionerDict={'populationIds':updPara['population.id']}, username = userInit['DftWangGeUser'], password = '11111111')
        self.assertTrue(res.result, '删除失败')
        #验证删除功能
        practitionerCheckParam_17['name']= updPara['population.name']
        ret = ShiYouRenKouIntf.check_weiXianPingCongYeRenYuan(practitionerCheckParam_17, orgId=updPara['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '删除失败')
        Log.LogOutput( message='删除验证通过')        
        pass 
    def testWeiXianPingCongYeSearch_17(self):
        '''危险品从业人员'''
        #第一条
        addPara1 = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
        addPara1['mode']='add'
        addPara1['population.organization.id'] = orgInit['DftWangGeOrgId']
        addPara1['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']   #属于户籍人员or流动人员
        addPara1['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['weiXianPingCongYeRenYuan']
        addPara1['population.organization.orgName'] = orgInit['DftWangGeOrg']
        addPara1['population.idCardNo'] = '336600199711220001'
        addPara1['population.name'] = '危险品从业人员'+createRandomString()
        addPara1['actualPersonType'] = addPara1['population.actualPopulationType']
        addPara1['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        addPara1['population.isHaveHouse1'] = 'null'   
        addPara1['population.dangerousWorkingType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='危险从业类别', displayName='民爆')  #危险从业类别，选择id
        addPara1['population.legalPerson'] = '法人代表'+createRandomString()
        addPara1['population.legalPersonMobileNumber'] = '11111111111' 
        addPara1['population.legalPersonTelephone'] = '3333333'  
        addPara1['population.workUnit'] = '工作单位'       
        addPara1['population.nativePlaceAddress']='户籍地详址'+createRandomString()
        responseDict = ShiYouRenKouIntf.add_weiXianPingCongYeRenYuan(practitionerDict=addPara1, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增危险品从业人员失败')         
        #第二条
        addPara2 = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
        addPara2['mode']='add'
        addPara2['population.organization.id'] = orgInit['DftWangGeOrgId']
        addPara2['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']   #属于户籍人员or流动人员
        addPara2['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['weiXianPingCongYeRenYuan']
        addPara2['population.organization.orgName'] = orgInit['DftWangGeOrg']
        addPara2['population.idCardNo'] = '336600199711220002'
        addPara2['population.name'] = '危险品从业人员'+createRandomString()
        addPara2['actualPersonType'] = addPara2['population.actualPopulationType']
        addPara2['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        addPara2['population.isHaveHouse1'] = 'null'   
        addPara2['population.dangerousWorkingType.id'] =CommonIntf.getIdByDomainAndDisplayName(domainName='危险从业类别', displayName='化工') #危险从业类别，选择id
        addPara2['population.legalPerson'] = '法人代表'+createRandomString()
        addPara2['population.legalPersonMobileNumber'] = '11111111111' 
        addPara2['population.legalPersonTelephone'] = '3333333'  
        addPara2['population.workUnit'] = '工作单位'       
        addPara2['population.nativePlaceAddress']='户籍地详址'+createRandomString()
        responseDict = ShiYouRenKouIntf.add_weiXianPingCongYeRenYuan(practitionerDict=addPara2, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增危险品从业人员失败') 
        #根据姓名快速检索
        searchPara1=copy.deepcopy(ShiYouRenKouPara.fastSearch)
        searchPara1['organizationId']=orgInit['DftWangGeOrgId']
        searchPara1['searchDangerousGoodsPractitionerVo.isEmphasis']='0'
        searchPara1['searchDangerousGoodsPractitionerVo.fastSearchKeyWords']= addPara1['population.name']
        checkPara1={'name':addPara1['population.name']}
        checkPara2={'name':addPara2['population.name']}
        result11=ShiYouRenKouIntf.checkWeiXianPingCongYeFastSearchList(checkpara=checkPara1,searchpara=searchPara1)
        self.assertTrue(result11, '通过姓名快速查询失败')
        result12=ShiYouRenKouIntf.checkWeiXianPingCongYeFastSearchList(checkpara=checkPara2,searchpara=searchPara1)
        self.assertFalse(result12,'通过姓名快速查询失败')
        Log.LogOutput( message='通过姓名快速查询验证成功！')
        #根据身份证快速查询
        searchPara2=copy.deepcopy(searchPara1)
        searchPara2['searchDangerousGoodsPractitionerVo.fastSearchKeyWords']= addPara1['population.idCardNo']
        result21=ShiYouRenKouIntf.checkWeiXianPingCongYeFastSearchList(checkpara=checkPara1,searchpara=searchPara2)
        self.assertTrue(result21, '通过身份证快速查询失败')
        result22=ShiYouRenKouIntf.checkWeiXianPingCongYeFastSearchList(checkpara=checkPara2,searchpara=searchPara2)
        self.assertFalse(result22,'通过身份证快速查询失败')
        Log.LogOutput( message='通过身份证快速查询验证成功！')        
        #高级搜索,通过户籍地详址搜索  
        searchPara3=copy.deepcopy(ShiYouRenKouPara.seniorSearch)
        searchPara3['organizationId']=orgInit['DftWangGeOrgId']
        searchPara3['searchDangerousGoodsPractitionerVo.isEmphasis']='-1'
        searchPara3['searchDangerousGoodsPractitionerVo.isDeath']='-1'
        searchPara3['searchDangerousGoodsPractitionerVo.hasServiceTeamMember']='-1'
        searchPara3['searchDangerousGoodsPractitionerVo.hasServiceTeamRecord']='-1'
        searchPara3['searchDangerousGoodsPractitionerVo.nativePlaceAddress']= addPara1['population.nativePlaceAddress']
        result31=ShiYouRenKouIntf.checkWeiXianPingCongYeSeniorSearchList(checkpara=checkPara1,searchpara=searchPara3)
        self.assertTrue(result31, '通过户籍地详址高级查询失败')
        result32=ShiYouRenKouIntf.checkWeiXianPingCongYeSeniorSearchList(checkpara=checkPara2,searchpara=searchPara3)
        self.assertFalse(result32,'通过户籍地详址高级查询失败')
        Log.LogOutput( message='通过户籍地详址高级查询验证成功！')         
        #高级搜索,通过企业法人代表搜索
        searchPara4=copy.deepcopy(searchPara3)
        searchPara4['organizationId']=orgInit['DftWangGeOrgId']
        searchPara4['searchDangerousGoodsPractitionerVo.legalPerson']= addPara1['population.legalPerson']
        searchPara4['searchDangerousGoodsPractitionerVo.nativePlaceAddress']=''
        result41=ShiYouRenKouIntf.checkWeiXianPingCongYeSeniorSearchList(checkpara=checkPara1,searchpara=searchPara4)
        self.assertTrue(result41, '通过企业法人代表高级查询失败')
        result42=ShiYouRenKouIntf.checkWeiXianPingCongYeSeniorSearchList(checkpara=checkPara2,searchpara=searchPara4)
        self.assertFalse(result42,'通过企业法人代表高级查询失败')
        Log.LogOutput( message='通过企业法人代表高级查询验证成功！') 
        #高级搜索,通过危险从业类别搜索
        searchPara5=copy.deepcopy(searchPara3)
        searchPara5['organizationId']=orgInit['DftWangGeOrgId']
        searchPara5['searchDangerousGoodsPractitionerVo.dangerousWorkingType.id']= addPara1['population.dangerousWorkingType.id']
        searchPara5['searchDangerousGoodsPractitionerVo.nativePlaceAddress']=''
        result51=ShiYouRenKouIntf.checkWeiXianPingCongYeSeniorSearchList(checkpara=checkPara1,searchpara=searchPara5)
        self.assertTrue(result51, '通过危险从业类别高级查询失败')
        result52=ShiYouRenKouIntf.checkWeiXianPingCongYeSeniorSearchList(checkpara=checkPara2,searchpara=searchPara5)
        self.assertFalse(result52,'通过危险从业类别高级查询失败')
        Log.LogOutput( message='通过危险从业类别高级查询验证成功！')              
        pass
    def testWeiXianPopulationImportAndDownLoad_35(self):
        """重点人员>危险品从业人员信息 导入/导出"""
         
        importHuJiparam = copy.deepcopy(ShiYouRenKouPara.data)
        importHuJiparam['dataType']='dangerousGoodsPractitioner'
        importHuJiparam['templates']='DANGEROUSGOODSPRACTITIONER_syncActualPopulation'
        files = {'upload': ('test.xls', open('C:/autotest_file/importWeiXianPingCongYePopulation.xls', 'rb'),'applicationnd.ms-excel')}
        ret = ShiYouRenKouIntf.import_RenKou(importHuJiparam, files=files,username=userInit['DftWangGeUser'], password='11111111')         
        
        param = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        param['name'] = '危险品从业人员导入测试'      
        param['idCardNo'] = '111111111111179'
        ret = ShiYouRenKouIntf.check_weiXianPingCongYeRenYuan(param, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找危险品从业人员失败') 
                                
        downLoadHuJiparam = copy.deepcopy(ShiYouRenKouPara.dlZhongDianData)
        downLoadHuJiparam['organizationId']=orgInit['DftWangGeOrgId']
        response = ShiYouRenKouIntf.downLoad_weiXianPingCongYeRenYuan(downLoadHuJiparam, username=userInit['DftWangGeUser'], password='11111111')         
        with open("C:/autotest_file/downLoadWeiXianPingCongYePopulation.xls", "wb") as code:
            code.write(response.content)
            
        ret = CommonUtil.checkExcelCellValue(param['name'], 'downLoadWeiXianPingCongYePopulation.xls','危险品从业人员清单', 'A4')          
        self.assertTrue(ret, '导出失败')
                         
        pass


    def testQiTaRenYuanAdd_17(self):
        """重点人员>其他人员新增"""
  
        otherParam_17 = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
        otherParam_17['mode']='add'
        otherParam_17['population.organization.id'] = orgInit['DftWangGeOrgId']
        otherParam_17['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人员or流动人员
        otherParam_17['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['qiTaRenYuan']
        otherParam_17['population.organization.orgName'] = orgInit['DftWangGeOrg']
        otherParam_17['population.idCardNo'] = '337700199711220000'
        otherParam_17['population.name'] = '其他人员'
        otherParam_17['actualPersonType'] = otherParam_17['population.actualPopulationType']
        otherParam_17['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        otherParam_17['population.isHaveHouse1'] = 'null'   
        otherParam_17['population.attentionExtent.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='关注程度', displayName='一般')  #关注程度，选择id，可以不填
        otherParam_17['population.attentionReason'] = '关注原因'   #可以不填      
        responseDict = ShiYouRenKouIntf.add_qiTaRenYuan(otherDict=otherParam_17, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增其他人员失败')       
          
        otherCheckParam_17 = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        otherCheckParam_17['name'] = otherParam_17['population.name']       
        otherCheckParam_17['idCardNo'] = otherParam_17['population.idCardNo']
        ret = ShiYouRenKouIntf.check_qiTaRenYuan(otherCheckParam_17, orgId=otherParam_17['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找其他人员失败')
        
        ret = ShiYouRenKouIntf.check_HuJiPopulation(otherCheckParam_17, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '没有检查到户籍人口下对应的其他人员信息')
        #补充修改用例
        updPara=copy.deepcopy(otherParam_17)
        updPara['mode']='edit'
        updPara['population.id']=json.loads(responseDict.text)['id']
        updPara['population.name']='其他人员'+createRandomString()
        updPara['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='女')
        responseDict = ShiYouRenKouIntf.add_qiTaRenYuan(updPara, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改其他人员失败')
        #验证修改功能
        otherCheckParam_17['name']= updPara['population.name']
        ret = ShiYouRenKouIntf.check_qiTaRenYuan(otherCheckParam_17, orgId=updPara['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找其他人员失败')
        Log.LogOutput( message='修改功能验证通过')
        #删除
        res=ShiYouRenKouIntf.delete_qiTaRenYuan({'populationIds':updPara['population.id']}, username = userInit['DftWangGeUser'], password = '11111111')
        self.assertTrue(res.result, '删除失败')
        #验证删除功能
        otherCheckParam_17['name']= updPara['population.name']
        ret = ShiYouRenKouIntf.check_qiTaRenYuan(otherCheckParam_17, orgId=updPara['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '删除失败')
        Log.LogOutput( message='删除验证通过')
        pass 

    def testQiTaRenYuanSearch_17(self):
        '''其他人员查询'''
        addPara1 = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
        addPara1['mode']='add'
        addPara1['population.organization.id'] = orgInit['DftWangGeOrgId']
        addPara1['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人员or流动人员
        addPara1['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['qiTaRenYuan']
        addPara1['population.organization.orgName'] = orgInit['DftWangGeOrg']
        addPara1['population.idCardNo'] = '337700199711220001'
        addPara1['population.name'] = '其他人员'+createRandomString()
        addPara1['actualPersonType'] = addPara1['population.actualPopulationType']
        addPara1['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        addPara1['population.isHaveHouse1'] = 'null'   
        addPara1['population.attentionExtent.id'] =CommonIntf.getIdByDomainAndDisplayName(domainName='关注程度', displayName='中等') #关注程度，选择id，可以不填
        addPara1['population.attentionReason'] = '关注原因'+createRandomString()   #可以不填      
        addPara1['population.nativePlaceAddress']='户籍地详址'+createRandomString()
        responseDict = ShiYouRenKouIntf.add_qiTaRenYuan(otherDict=addPara1, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增其他人员失败')  
        #第二条
        addPara2 = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
        addPara2['mode']='add'
        addPara2['population.organization.id'] = orgInit['DftWangGeOrgId']
        addPara2['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人员or流动人员
        addPara2['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['qiTaRenYuan']
        addPara2['population.organization.orgName'] = orgInit['DftWangGeOrg']
        addPara2['population.idCardNo'] = '337700199711220002'
        addPara2['population.name'] = '其他人员'+createRandomString()
        addPara2['actualPersonType'] = addPara2['population.actualPopulationType']
        addPara2['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        addPara2['population.isHaveHouse1'] = 'null'   
        addPara2['population.attentionExtent.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='关注程度', displayName='严重') #关注程度，选择id，可以不填
        addPara2['population.attentionReason'] = '关注原因'+createRandomString()   #可以不填      
        addPara2['population.nativePlaceAddress']='户籍地详址'+createRandomString()
        responseDict = ShiYouRenKouIntf.add_qiTaRenYuan(otherDict=addPara2, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增其他人员失败')
        #根据姓名快速检索
        searchPara1=copy.deepcopy(ShiYouRenKouPara.fastSearch)
        searchPara1['organizationId']=orgInit['DftWangGeOrgId']
        searchPara1['searchOtherAttentionPersonnelVo.isEmphasis']='0'
        searchPara1['searchOtherAttentionPersonnelVo.fastSearchKeyWords']= addPara1['population.name']
        checkPara1={'name':addPara1['population.name']}
        checkPara2={'name':addPara2['population.name']}
        result11=ShiYouRenKouIntf.checkQiTaFastSearchList(checkpara=checkPara1,searchpara=searchPara1)
        self.assertTrue(result11, '通过姓名快速查询失败')
        result12=ShiYouRenKouIntf.checkQiTaFastSearchList(checkpara=checkPara2,searchpara=searchPara1)
        self.assertFalse(result12,'通过姓名快速查询失败')
        Log.LogOutput( message='通过姓名快速查询验证成功！')
        #根据身份证快速查询
        searchPara2=copy.deepcopy(searchPara1)
        searchPara2['searchOtherAttentionPersonnelVo.fastSearchKeyWords']= addPara1['population.idCardNo']
        result21=ShiYouRenKouIntf.checkQiTaFastSearchList(checkpara=checkPara1,searchpara=searchPara2)
        self.assertTrue(result21, '通过身份证快速查询失败')
        result22=ShiYouRenKouIntf.checkQiTaFastSearchList(checkpara=checkPara2,searchpara=searchPara2)
        self.assertFalse(result22,'通过身份证快速查询失败')
        Log.LogOutput( message='通过身份证快速查询验证成功！')    
        
        #高级搜索,通过户籍地详址搜索  
        searchPara3=copy.deepcopy(ShiYouRenKouPara.seniorSearch)
        searchPara3['organizationId']=orgInit['DftWangGeOrgId']
        searchPara3['searchOtherAttentionPersonnelVo.isEmphasis']='-1'
        searchPara3['searchOtherAttentionPersonnelVo.isDeath']='-1'
        searchPara3['searchOtherAttentionPersonnelVo.hasServiceTeamMember']='-1'
        searchPara3['searchOtherAttentionPersonnelVo.hasServiceTeamRecord']='-1'
        searchPara3['searchOtherAttentionPersonnelVo.nativePlaceAddress']= addPara1['population.nativePlaceAddress']
        result31=ShiYouRenKouIntf.checkQiTaSeniorSearchList(checkpara=checkPara1,searchpara=searchPara3)
        self.assertTrue(result31, '通过户籍地详址高级查询失败')
        result32=ShiYouRenKouIntf.checkQiTaSeniorSearchList(checkpara=checkPara2,searchpara=searchPara3)
        self.assertFalse(result32,'通过户籍地详址高级查询失败')
        Log.LogOutput( message='通过户籍地详址高级查询验证成功！')         
        #高级搜索,通过关注原因搜索
        searchPara4=copy.deepcopy(searchPara3)
        searchPara4['organizationId']=orgInit['DftWangGeOrgId']
        searchPara4['searchOtherAttentionPersonnelVo.attentionReason']= addPara1['population.attentionReason']
        searchPara4['searchOtherAttentionPersonnelVo.nativePlaceAddress']=''
        result41=ShiYouRenKouIntf.checkQiTaSeniorSearchList(checkpara=checkPara1,searchpara=searchPara4)
        self.assertTrue(result41, '通过关注原因高级查询失败')
        result42=ShiYouRenKouIntf.checkQiTaSeniorSearchList(checkpara=checkPara2,searchpara=searchPara4)
        self.assertFalse(result42,'通过关注原因高级查询失败')
        Log.LogOutput( message='通过关注原因高级查询验证成功！')         
        
                           
        pass    
    def testQiTaPopulationImportAndDownLoad_36(self):
        """重点人员>其他人员信息 导入/导出"""
         
        importHuJiparam = copy.deepcopy(ShiYouRenKouPara.data)
        importHuJiparam['dataType']='otherAttentionPersonnel'
        importHuJiparam['templates']='OTHERATTENTIONPERSONNEL_syncActualPopulation'
        files = {'upload': ('test.xls', open('C:/autotest_file/importQiTaPopulation.xls', 'rb'),'applicationnd.ms-excel')}
        ret = ShiYouRenKouIntf.import_RenKou(importHuJiparam, files=files,username=userInit['DftWangGeUser'], password='11111111')         
        
        param = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        param['name'] = '其他人员导入测试'      
        param['idCardNo'] = '111111111111180'
        ret = ShiYouRenKouIntf.check_qiTaRenYuan(param, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找其他人员失败') 
                                
        downLoadHuJiparam = copy.deepcopy(ShiYouRenKouPara.dlZhongDianData)
        downLoadHuJiparam['organizationId']=orgInit['DftWangGeOrgId']
        response = ShiYouRenKouIntf.downLoad_qiTaRenYuan(downLoadHuJiparam, username=userInit['DftWangGeUser'], password='11111111')         
        with open("C:/autotest_file/downLoadQiTaPopulation.xls", "wb") as code:
            code.write(response.content)
            
        ret = CommonUtil.checkExcelCellValue(param['name'], 'downLoadQiTaPopulation.xls','其他人员表', 'A4')          
        self.assertTrue(ret, '导出失败')
                         
        pass    
    

#关怀对象



    def testJianYiYongWeiAdd_17(self):
        """关怀对象>见义勇为人员新增"""
  
        samaritanParam_17 = copy.deepcopy(ShiYouRenKouPara.guanHuaiDuiXiangObject) 
        samaritanParam_17['mode']='add'
        samaritanParam_17['population.organization.id'] = orgInit['DftWangGeOrgId']
        samaritanParam_17['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']   #属于户籍人员or流动人员
        samaritanParam_17['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['jianYiYongWei']
        samaritanParam_17['population.organization.orgName'] = orgInit['DftWangGeOrg']
        samaritanParam_17['population.idCardNo'] = '330000199711229901'
        samaritanParam_17['population.name'] = '见义勇为人员'
        samaritanParam_17['actualPersonType'] = samaritanParam_17['population.actualPopulationType']
        samaritanParam_17['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        samaritanParam_17['population.isHaveHouse1'] = 'null'   
        samaritanParam_17['population.occurrenceDate'] = '2015-12-05'  
        samaritanParam_17['population.sureDate'] = '2015-12-06' 
        samaritanParam_17['population.medicalInsurance'] = 'false'  
        samaritanParam_17['population.socialInsurance'] = 'false'  
        samaritanParam_17['population.minLivingStandard'] = 'false'  
        samaritanParam_17['population.poorFamilies'] = 'false'  
        samaritanParam_17['population.mainEvent'] = '主要事迹'     
        responseDict = ShiYouRenKouIntf.add_jianYiYongWei(jianYiYongWeiDict=samaritanParam_17, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增见义勇为人员失败')       
          
        samaritanCheckParam_17 = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        samaritanCheckParam_17['name'] = samaritanParam_17['population.name']       
        samaritanCheckParam_17['idCardNo'] = samaritanParam_17['population.idCardNo']
        ret = ShiYouRenKouIntf.check_jianYiYongWei(samaritanCheckParam_17, orgId=samaritanParam_17['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找见义勇为人员失败')
        
        ret = ShiYouRenKouIntf.check_HuJiPopulation(samaritanCheckParam_17, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '没有检查到户籍人口下对应的见义勇为人员信息')
        #补充修改用例
        updPara=copy.deepcopy(samaritanParam_17)
        updPara['mode']='edit'
        updPara['population.id']=json.loads(responseDict.text)['id']
        updPara['population.name']='见义勇为人员'+createRandomString()
        updPara['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='女')
        responseDict = ShiYouRenKouIntf.add_jianYiYongWei(updPara, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改见义勇为人员失败')
        #验证修改功能
        samaritanCheckParam_17['name']= updPara['population.name']
        ret = ShiYouRenKouIntf.check_jianYiYongWei(samaritanCheckParam_17, orgId=updPara['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找见义勇为人员失败')
        Log.LogOutput( message='修改功能验证通过')
        #删除
        res=ShiYouRenKouIntf.delete_jianYiYongWei({'populationIds':updPara['population.id']}, username = userInit['DftWangGeUser'], password = '11111111')
#         self.assertTrue(res.result, '删除失败')
        #验证删除功能
        samaritanCheckParam_17['name']= updPara['population.name']
        ret = ShiYouRenKouIntf.check_jianYiYongWei(samaritanCheckParam_17, orgId=updPara['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '删除失败')
        Log.LogOutput( message='删除验证通过')        
        pass 

    def testJianYiYongWeiSearch_17(self):
        '''见义勇为查询'''
        addPara1 = copy.deepcopy(ShiYouRenKouPara.guanHuaiDuiXiangObject) 
        addPara1['mode']='add'
        addPara1['population.organization.id'] = orgInit['DftWangGeOrgId']
        addPara1['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']   #属于户籍人员or流动人员
        addPara1['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['jianYiYongWei']
        addPara1['population.organization.orgName'] = orgInit['DftWangGeOrg']
        addPara1['population.idCardNo'] = '330000199711229901'
        addPara1['population.name'] = '见义勇为人员'+createRandomString()
        addPara1['actualPersonType'] = addPara1['population.actualPopulationType']
        addPara1['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        addPara1['population.isHaveHouse1'] = 'null'   
        addPara1['population.occurrenceDate'] = '2015-12-05'  
        addPara1['population.sureDate'] = '2015-12-06' 
        addPara1['population.medicalInsurance'] = 'false'  
        addPara1['population.socialInsurance'] = 'false'  
        addPara1['population.minLivingStandard'] = 'false'  
        addPara1['population.poorFamilies'] = 'false'  
        addPara1['population.mainEvent'] = '主要事迹'+createRandomString()  
        addPara1['population.nativePlaceAddress']='户籍地详址'+createRandomString()
        responseDict = ShiYouRenKouIntf.add_jianYiYongWei(jianYiYongWeiDict=addPara1, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增见义勇为人员失败') 
        #第二条
        addPara2 = copy.deepcopy(ShiYouRenKouPara.guanHuaiDuiXiangObject) 
        addPara2['mode']='add'
        addPara2['population.organization.id'] = orgInit['DftWangGeOrgId']
        addPara2['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']   #属于户籍人员or流动人员
        addPara2['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['jianYiYongWei']
        addPara2['population.organization.orgName'] = orgInit['DftWangGeOrg']
        addPara2['population.idCardNo'] = '330000199711229902'
        addPara2['population.name'] = '见义勇为人员'+createRandomString()
        addPara2['actualPersonType'] = addPara2['population.actualPopulationType']
        addPara2['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        addPara2['population.isHaveHouse1'] = 'null'   
        addPara2['population.occurrenceDate'] = '2015-12-05'  
        addPara2['population.sureDate'] = '2015-12-06' 
        addPara2['population.medicalInsurance'] = 'false'  
        addPara2['population.socialInsurance'] = 'false'  
        addPara2['population.minLivingStandard'] = 'false'  
        addPara2['population.poorFamilies'] = 'false'  
        addPara2['population.mainEvent'] = '主要事迹'+createRandomString()  
        addPara2['population.nativePlaceAddress']='户籍地详址'+createRandomString()
        responseDict = ShiYouRenKouIntf.add_jianYiYongWei(jianYiYongWeiDict=addPara2, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增见义勇为人员失败') 
        #根据姓名快速检索
        searchPara1=copy.deepcopy(ShiYouRenKouPara.fastSearch)
        searchPara1['organizationId']=orgInit['DftWangGeOrgId']
        searchPara1['searchSamaritanPeopleVo.isEmphasis']='0'
        searchPara1['searchSamaritanPeopleVo.fastSearchKeyWords']= addPara1['population.name']
        checkPara1={'name':addPara1['population.name']}
        checkPara2={'name':addPara2['population.name']}
        result11=ShiYouRenKouIntf.checkJianYiYongWeiFastSearchList(checkpara=checkPara1,searchpara=searchPara1)
        self.assertTrue(result11, '通过姓名快速查询失败')
        result12=ShiYouRenKouIntf.checkJianYiYongWeiFastSearchList(checkpara=checkPara2,searchpara=searchPara1)
        self.assertFalse(result12,'通过姓名快速查询失败')
        Log.LogOutput( message='通过姓名快速查询验证成功！')
        #根据身份证快速查询
        searchPara2=copy.deepcopy(searchPara1)
        searchPara2['searchSamaritanPeopleVo.fastSearchKeyWords']= addPara1['population.idCardNo']
        result21=ShiYouRenKouIntf.checkJianYiYongWeiFastSearchList(checkpara=checkPara1,searchpara=searchPara2)
        self.assertTrue(result21, '通过身份证快速查询失败')
        result22=ShiYouRenKouIntf.checkJianYiYongWeiFastSearchList(checkpara=checkPara2,searchpara=searchPara2)
        self.assertFalse(result22,'通过身份证快速查询失败')
        Log.LogOutput( message='通过身份证快速查询验证成功！')    
        #高级搜索,通过户籍地详址搜索  
        searchPara3=copy.deepcopy(ShiYouRenKouPara.seniorSearch)
        searchPara3['organizationId']=orgInit['DftWangGeOrgId']
        searchPara3['searchSamaritanPeopleVo.isEmphasis']='-1'
        searchPara3['searchSamaritanPeopleVo.isDeath']='-1'
        searchPara3['searchSamaritanPeopleVo.hasServiceTeamMember']='-1'
        searchPara3['searchSamaritanPeopleVo.hasServiceTeamRecord']='-1'
        searchPara3['searchSamaritanPeopleVo.nativePlaceAddress']= addPara1['population.nativePlaceAddress']
        result31=ShiYouRenKouIntf.checkJianYiYongWeiSeniorSearchList(checkpara=checkPara1,searchpara=searchPara3)
        self.assertTrue(result31, '通过户籍地详址高级查询失败')
        result32=ShiYouRenKouIntf.checkJianYiYongWeiSeniorSearchList(checkpara=checkPara2,searchpara=searchPara3)
        self.assertFalse(result32,'通过户籍地详址高级查询失败')
        Log.LogOutput( message='通过户籍地详址高级查询验证成功！')         
        #高级搜索,通过主要事迹搜索
        searchPara4=copy.deepcopy(searchPara3)
        searchPara4['organizationId']=orgInit['DftWangGeOrgId']
        searchPara4['searchSamaritanPeopleVo.mainEvent']= addPara1['population.mainEvent']
        searchPara4['searchSamaritanPeopleVo.nativePlaceAddress']=''
        result41=ShiYouRenKouIntf.checkJianYiYongWeiSeniorSearchList(checkpara=checkPara1,searchpara=searchPara4)
        self.assertTrue(result41, '通过主要事迹高级查询失败')
        result42=ShiYouRenKouIntf.checkJianYiYongWeiSeniorSearchList(checkpara=checkPara2,searchpara=searchPara4)
        self.assertFalse(result42,'通过主要事迹高级查询失败')
        Log.LogOutput( message='通过主要事迹高级查询验证成功！')            
        pass
    
    
    def testJianYiYongWeiImportAndDownLoad_37(self):     #导入卡死
        """关怀对象>见义勇为人员信息 导入/导出"""
         
        importHuJiparam = copy.deepcopy(ShiYouRenKouPara.data)
        importHuJiparam['dataType']='samaritanPeople'
        importHuJiparam['templates']='SAMARITANPEOPLE_syncActualPopulation'
        files = {'upload': ('test.xls', open('C:/autotest_file/importJianYiYongWei.xls', 'rb'),'applicationnd.ms-excel')}
        ret = ShiYouRenKouIntf.import_RenKou(importHuJiparam, files=files,username=userInit['DftWangGeUser'], password='11111111')         
        
        param = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        param['name'] = '见义勇为导入测试'      
        param['idCardNo'] = '111111111111181'
        ret = ShiYouRenKouIntf.check_jianYiYongWei(param, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找见义勇为人员失败') 
                                
        downLoadHuJiparam = copy.deepcopy(ShiYouRenKouPara.dlZhongDianData)
        downLoadHuJiparam['organizationId']=orgInit['DftWangGeOrgId']
        response = ShiYouRenKouIntf.downLoad_jianYiYongWei(downLoadHuJiparam, username=userInit['DftWangGeUser'], password='11111111')         
        with open("C:/autotest_file/downLoadJianYiYongWei.xls", "wb") as code:
            code.write(response.content)
            
        ret = CommonUtil.checkExcelCellValue(param['name'], 'downLoadJianYiYongWei.xls','见义勇为人员清单', 'A4')          
        self.assertTrue(ret, '导出失败')
                         
        pass

    
    def testLaoNianRenAdd_17(self):
        """关怀对象>老年人新增"""
  
        laoNianParam_17 = copy.deepcopy(ShiYouRenKouPara.guanHuaiDuiXiangObject) 
        laoNianParam_17['mode']='add'
        laoNianParam_17['population.organization.id'] = orgInit['DftWangGeOrgId']
        laoNianParam_17['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人员or流动人员
        laoNianParam_17['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['laoNianRen']
        laoNianParam_17['population.organization.orgName'] = orgInit['DftWangGeOrg']
        laoNianParam_17['population.idCardNo'] = '337700195511220000'  #如果不在60岁以上，则需提示输入正确id在60以上的?
        laoNianParam_17['population.name'] = '老年人'
        laoNianParam_17['actualPersonType'] = laoNianParam_17['population.actualPopulationType']
        laoNianParam_17['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        laoNianParam_17['population.isHaveHouse1'] = 'null'   
        laoNianParam_17['population.attentionExtent.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='关注程度', displayName='一般')    #关注程度选择的id，不是必填项
        laoNianParam_17['population.elderPeopleId'] = '111'     #老年人证号，不是必填项
        laoNianParam_17['population.peopleType.id'] =CommonIntf.getIdByDomainAndDisplayName(domainName='人员类型', displayName='未知')     #人员类型选择的id，不是必填项
        responseDict = ShiYouRenKouIntf.add_laoNianRen(laoNianRenDict=laoNianParam_17, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增老年人失败')       
          
        elderlyCheckParam_17 = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        elderlyCheckParam_17['name'] = laoNianParam_17['population.name']       
        elderlyCheckParam_17['idCardNo'] = laoNianParam_17['population.idCardNo']
        ret = ShiYouRenKouIntf.check_laoNianRen(elderlyCheckParam_17, orgId=laoNianParam_17['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找老年人失败')
        
        ret = ShiYouRenKouIntf.check_HuJiPopulation(elderlyCheckParam_17, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '没有检查到户籍人口下对应的老年人信息')
        #补充修改用例
        updPara=copy.deepcopy(laoNianParam_17)
        updPara['mode']='edit'
        updPara['population.id']=json.loads(responseDict.text)['id']
        updPara['population.name']='老年人'+createRandomString()
        updPara['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='女')
        responseDict = ShiYouRenKouIntf.add_laoNianRen(updPara, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改老年人失败')
        #验证修改功能
        elderlyCheckParam_17['name']= updPara['population.name']
        ret = ShiYouRenKouIntf.check_laoNianRen(elderlyCheckParam_17, orgId=updPara['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找老年人失败')
        Log.LogOutput( message='修改功能验证通过')
        #删除
        res=ShiYouRenKouIntf.delete_laoNianRen({'populationIds':updPara['population.id']}, username = userInit['DftWangGeUser'], password = '11111111')
#         self.assertTrue(res.result, '删除失败')
        #验证删除功能
        elderlyCheckParam_17['name']= updPara['population.name']
        ret = ShiYouRenKouIntf.check_laoNianRen(elderlyCheckParam_17, orgId=updPara['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '删除失败')
        Log.LogOutput( message='删除验证通过')
        
        pass 

    def testLaoNianRenSearch_17(self):
        '''老年人查询'''
        addPara1 = copy.deepcopy(ShiYouRenKouPara.guanHuaiDuiXiangObject) 
        addPara1['mode']='add'
        addPara1['population.organization.id'] = orgInit['DftWangGeOrgId']
        addPara1['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人员or流动人员
        addPara1['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['laoNianRen']
        addPara1['population.organization.orgName'] = orgInit['DftWangGeOrg']
        addPara1['population.idCardNo'] = '337700195511220001'  #如果不在60岁以上，则需提示输入正确id在60以上的?
        addPara1['population.name'] = '老年人'+createRandomString()
        addPara1['actualPersonType'] = addPara1['population.actualPopulationType']
        addPara1['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        addPara1['population.isHaveHouse1'] = 'null'   
        addPara1['population.attentionExtent.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='关注程度', displayName='中等')    #关注程度选择的id，不是必填项
        addPara1['population.elderPeopleId'] = '111111'     #老年人证号，不是必填项
        addPara1['population.peopleType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='人员类型', displayName='低保')    #人员类型选择的id，不是必填项
        addPara1['population.nativePlaceAddress']='户籍地详址'+createRandomString()
        responseDict = ShiYouRenKouIntf.add_laoNianRen(laoNianRenDict=addPara1, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增老年人失败')  
        #第二条
        addPara2 = copy.deepcopy(ShiYouRenKouPara.guanHuaiDuiXiangObject) 
        addPara2['mode']='add'
        addPara2['population.organization.id'] = orgInit['DftWangGeOrgId']
        addPara2['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人员or流动人员
        addPara2['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['laoNianRen']
        addPara2['population.organization.orgName'] = orgInit['DftWangGeOrg']
        addPara2['population.idCardNo'] = '337700195511220002'  #如果不在60岁以上，则需提示输入正确id在60以上的?
        addPara2['population.name'] = '老年人'+createRandomString()
        addPara2['actualPersonType'] = addPara2['population.actualPopulationType']
        addPara2['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        addPara2['population.isHaveHouse1'] = 'null'   
        addPara2['population.attentionExtent.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='关注程度', displayName='严重')    #关注程度选择的id，不是必填项
        addPara2['population.elderPeopleId'] = '222222'     #老年人证号，不是必填项
        addPara2['population.peopleType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='人员类型', displayName='特困')      #人员类型选择的id，不是必填项
        addPara2['population.nativePlaceAddress']='户籍地详址'+createRandomString()
        responseDict = ShiYouRenKouIntf.add_laoNianRen(laoNianRenDict=addPara2, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增老年人失败')
        #根据姓名快速检索
        searchPara1=copy.deepcopy(ShiYouRenKouPara.fastSearch)
        searchPara1['organizationId']=orgInit['DftWangGeOrgId']
        searchPara1['searchElderlyPeopleVo.isEmphasis']='0'
        searchPara1['searchElderlyPeopleVo.fastSearchKeyWords']= addPara1['population.name']
        checkPara1={'name':addPara1['population.name']}
        checkPara2={'name':addPara2['population.name']}
        result11=ShiYouRenKouIntf.checkLaoNianFastSearchList(checkpara=checkPara1,searchpara=searchPara1)
        self.assertTrue(result11, '通过姓名快速查询失败')
        result12=ShiYouRenKouIntf.checkLaoNianFastSearchList(checkpara=checkPara2,searchpara=searchPara1)
        self.assertFalse(result12,'通过姓名快速查询失败')
        Log.LogOutput( message='通过姓名快速查询验证成功！')
        #根据身份证快速查询
        searchPara2=copy.deepcopy(searchPara1)
        searchPara2['searchElderlyPeopleVo.fastSearchKeyWords']= addPara1['population.idCardNo']
        result21=ShiYouRenKouIntf.checkLaoNianFastSearchList(checkpara=checkPara1,searchpara=searchPara2)
        self.assertTrue(result21, '通过身份证快速查询失败')
        result22=ShiYouRenKouIntf.checkLaoNianFastSearchList(checkpara=checkPara2,searchpara=searchPara2)
        self.assertFalse(result22,'通过身份证快速查询失败')
        Log.LogOutput( message='通过身份证快速查询验证成功！')   
        #高级搜索,通过户籍地详址搜索  
        searchPara3=copy.deepcopy(ShiYouRenKouPara.seniorSearch)
        searchPara3['organizationId']=orgInit['DftWangGeOrgId']
        searchPara3['searchElderlyPeopleVo.isEmphasis']='-1'
        searchPara3['searchElderlyPeopleVo.isDeath']='-1'
        searchPara3['searchElderlyPeopleVo.hasServiceTeamMember']='-1'
        searchPara3['searchElderlyPeopleVo.hasServiceTeamRecord']='-1'
        searchPara3['searchElderlyPeopleVo.nativePlaceAddress']= addPara1['population.nativePlaceAddress']
        result31=ShiYouRenKouIntf.checkLaoNianSeniorSearchList(checkpara=checkPara1,searchpara=searchPara3)
        self.assertTrue(result31, '通过户籍地详址高级查询失败')
        result32=ShiYouRenKouIntf.checkLaoNianSeniorSearchList(checkpara=checkPara2,searchpara=searchPara3)
        self.assertFalse(result32,'通过户籍地详址高级查询失败')
        Log.LogOutput( message='通过户籍地详址高级查询验证成功！')         
        #高级搜索,通过老年证号搜索
        searchPara4=copy.deepcopy(searchPara3)
        searchPara4['organizationId']=orgInit['DftWangGeOrgId']
        searchPara4['searchElderlyPeopleVo.elderPeopleId']= addPara1['population.elderPeopleId']
        searchPara4['searchElderlyPeopleVo.nativePlaceAddress']=''
        result41=ShiYouRenKouIntf.checkLaoNianSeniorSearchList(checkpara=checkPara1,searchpara=searchPara4)
        self.assertTrue(result41, '通过老年证号高级查询失败')
        result42=ShiYouRenKouIntf.checkLaoNianSeniorSearchList(checkpara=checkPara2,searchpara=searchPara4)
        self.assertFalse(result42,'通过老年证号高级查询失败')
        Log.LogOutput( message='通过老年证号高级查询验证成功！')
        #高级搜索,通过人员类型搜索
        searchPara5=copy.deepcopy(searchPara3)
        searchPara5['organizationId']=orgInit['DftWangGeOrgId']
        searchPara5['searchElderlyPeopleVo.peopleType']= addPara1['population.peopleType.id']
        searchPara5['searchElderlyPeopleVo.nativePlaceAddress']=''
        result41=ShiYouRenKouIntf.checkLaoNianSeniorSearchList(checkpara=checkPara1,searchpara=searchPara4)
        self.assertTrue(result41, '通过人员类型高级查询失败')
        result42=ShiYouRenKouIntf.checkLaoNianSeniorSearchList(checkpara=checkPara2,searchpara=searchPara4)
        self.assertFalse(result42,'通过人员类型高级查询失败')
        Log.LogOutput( message='通过人员类型高级查询验证成功！')
        pass
    
    def testLaoNianRenImportAndDownLoad_38(self):
        """关怀对象>老年人信息 导入/导出"""
         
        importHuJiparam = copy.deepcopy(ShiYouRenKouPara.data)
        importHuJiparam['dataType']='elderlyPeople'
        importHuJiparam['templates']='ELDERLYPEOPLE_syncActualPopulation'
        files = {'upload': ('test.xls', open('C:/autotest_file/importLaoNianRen.xls', 'rb'),'applicationnd.ms-excel')}
        ret = ShiYouRenKouIntf.import_RenKou(importHuJiparam, files=files,username=userInit['DftWangGeUser'], password='11111111')         
        
        param = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        param['name'] = '老年人导入测试'      
        param['idCardNo'] = '330000195511110000'
        ret = ShiYouRenKouIntf.check_laoNianRen(param, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找老年人失败') 
                                
        downLoadHuJiparam = copy.deepcopy(ShiYouRenKouPara.dlZhongDianData)
        downLoadHuJiparam['organizationId']=orgInit['DftWangGeOrgId']
        response = ShiYouRenKouIntf.downLoad_laoNianRen(downLoadHuJiparam, username=userInit['DftWangGeUser'], password='11111111')         
        with open("C:/autotest_file/downLoadLaoNianRen.xls", "wb") as code:
            code.write(response.content)
            
        ret = CommonUtil.checkExcelCellValue(param['name'], 'downLoadLaoNianRen.xls','老年人员清单', 'A4')          
        self.assertTrue(ret, '导出失败')
                         
        pass

                 
    def testCanJiRenAdd_17(self):
        """关怀对象>残疾人新增"""
  
        canJiParam_17 = copy.deepcopy(ShiYouRenKouPara.guanHuaiDuiXiangObject) 
        canJiParam_17['mode']='add'
        canJiParam_17['population.organization.id'] = orgInit['DftWangGeOrgId']
        canJiParam_17['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人员or流动人员
        canJiParam_17['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['canJiRen']
        canJiParam_17['population.organization.orgName'] = orgInit['DftWangGeOrg']
        canJiParam_17['population.idCardNo'] = '330000199711228800'  
        canJiParam_17['population.name'] = '残疾人'
        canJiParam_17['actualPersonType'] = canJiParam_17['population.actualPopulationType']
        canJiParam_17['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        canJiParam_17['population.isHaveHouse1'] = 'null'   
        canJiParam_17['population.hadDisabilityCard'] = 'true'    
        canJiParam_17['population.disabilityCardNo'] = '111'     
        responseDict = ShiYouRenKouIntf.add_canJiRen(canJiRenDict=canJiParam_17, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增残疾人失败')       
          
        handicappedCheckParam_17 = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        handicappedCheckParam_17['name'] = canJiParam_17['population.name']       
        handicappedCheckParam_17['idCardNo'] = canJiParam_17['population.idCardNo']
        ret = ShiYouRenKouIntf.check_canJiRen(handicappedCheckParam_17, orgId=canJiParam_17['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找残疾人失败')
        
        ret = ShiYouRenKouIntf.check_HuJiPopulation(handicappedCheckParam_17, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '没有检查到户籍人口下对应的残疾人信息')
        #补充修改用例
        updPara=copy.deepcopy(canJiParam_17)
        updPara['mode']='edit'
        updPara['population.id']=json.loads(responseDict.text)['id']
        updPara['population.name']='残疾人'+createRandomString()
        updPara['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='女')
        responseDict = ShiYouRenKouIntf.add_canJiRen(updPara, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改残疾人失败')
        #验证修改功能
        handicappedCheckParam_17['name']= updPara['population.name']
        ret = ShiYouRenKouIntf.check_canJiRen(handicappedCheckParam_17, orgId=updPara['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找残疾人失败')
        Log.LogOutput( message='修改功能验证通过')
        #删除
        res=ShiYouRenKouIntf.delete_canJiRen({'populationIds':updPara['population.id']}, username = userInit['DftWangGeUser'], password = '11111111')
        self.assertTrue(res.result, '删除失败')
        #验证删除功能
        handicappedCheckParam_17['name']= updPara['population.name']
        ret = ShiYouRenKouIntf.check_canJiRen(handicappedCheckParam_17, orgId=updPara['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '删除失败')
        Log.LogOutput( message='删除验证通过')
        pass
     
    def testCanJiRenSearch_17(self):
        '''残疾人查询'''
        #第一条
        addPara1 = copy.deepcopy(ShiYouRenKouPara.guanHuaiDuiXiangObject) 
        addPara1['mode']='add'
        addPara1['population.organization.id'] = orgInit['DftWangGeOrgId']
        addPara1['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人员or流动人员
        addPara1['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['canJiRen']
        addPara1['population.organization.orgName'] = orgInit['DftWangGeOrg']
        addPara1['population.idCardNo'] = '330000199711228801'  
        addPara1['population.name'] = '残疾人'+createRandomString()
        addPara1['actualPersonType'] = addPara1['population.actualPopulationType']
        addPara1['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        addPara1['population.isHaveHouse1'] = 'null'   
        addPara1['population.hadDisabilityCard'] = 'true'    
        addPara1['population.disabilityCardNo'] = '111'     
        addPara1['population.nativePlaceAddress']='户籍地详址'+createRandomString()
        responseDict = ShiYouRenKouIntf.add_canJiRen(canJiRenDict=addPara1, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增残疾人失败')          
        #第二条
        addPara2 = copy.deepcopy(ShiYouRenKouPara.guanHuaiDuiXiangObject) 
        addPara2['mode']='add'
        addPara2['population.organization.id'] = orgInit['DftWangGeOrgId']
        addPara2['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人员or流动人员
        addPara2['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['canJiRen']
        addPara2['population.organization.orgName'] = orgInit['DftWangGeOrg']
        addPara2['population.idCardNo'] = '330000199711228802'  
        addPara2['population.name'] = '残疾人'+createRandomString()
        addPara2['actualPersonType'] = addPara2['population.actualPopulationType']
        addPara2['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        addPara2['population.isHaveHouse1'] = 'null'   
        addPara2['population.hadDisabilityCard'] = 'true'    
        addPara2['population.disabilityCardNo'] = '222'     
        addPara2['population.nativePlaceAddress']='户籍地详址'+createRandomString()
        responseDict = ShiYouRenKouIntf.add_canJiRen(canJiRenDict=addPara2, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增残疾人失败')  
        #根据姓名快速检索
        searchPara1=copy.deepcopy(ShiYouRenKouPara.fastSearch)
        searchPara1['organizationId']=orgInit['DftWangGeOrgId']
        searchPara1['searchHandicappedVo.isEmphasis']='0'
        searchPara1['searchHandicappedVo.fastSearchKeyWords']= addPara1['population.name']
        checkPara1={'name':addPara1['population.name']}
        checkPara2={'name':addPara2['population.name']}
        result11=ShiYouRenKouIntf.checkCanJiFastSearchList(checkpara=checkPara1,searchpara=searchPara1)
        self.assertTrue(result11, '通过姓名快速查询失败')
        result12=ShiYouRenKouIntf.checkCanJiFastSearchList(checkpara=checkPara2,searchpara=searchPara1)
        self.assertFalse(result12,'通过姓名快速查询失败')
        Log.LogOutput( message='通过姓名快速查询验证成功！')
        #根据身份证快速查询
        searchPara2=copy.deepcopy(searchPara1)
        searchPara2['searchHandicappedVo.fastSearchKeyWords']= addPara1['population.idCardNo']
        result21=ShiYouRenKouIntf.checkCanJiFastSearchList(checkpara=checkPara1,searchpara=searchPara2)
        self.assertTrue(result21, '通过身份证快速查询失败')
        result22=ShiYouRenKouIntf.checkCanJiFastSearchList(checkpara=checkPara2,searchpara=searchPara2)
        self.assertFalse(result22,'通过身份证快速查询失败')
        Log.LogOutput( message='通过身份证快速查询验证成功！')
        #高级搜索,通过户籍地详址搜索  
        searchPara3=copy.deepcopy(ShiYouRenKouPara.seniorSearch)
        searchPara3['organizationId']=orgInit['DftWangGeOrgId']
        searchPara3['searchHandicappedVo.isEmphasis']='-1'
        searchPara3['searchHandicappedVo.isDeath']='-1'
        searchPara3['searchHandicappedVo.hasServiceTeamMember']='-1'
        searchPara3['searchHandicappedVo.hasServiceTeamRecord']='-1'
        searchPara3['searchHandicappedVo.nativePlaceAddress']= addPara1['population.nativePlaceAddress']
        result31=ShiYouRenKouIntf.checkCanJiSeniorSearchList(checkpara=checkPara1,searchpara=searchPara3)
        self.assertTrue(result31, '通过户籍地详址高级查询失败')
        result32=ShiYouRenKouIntf.checkCanJiSeniorSearchList(checkpara=checkPara2,searchpara=searchPara3)
        self.assertFalse(result32,'通过户籍地详址高级查询失败')
        Log.LogOutput( message='通过户籍地详址高级查询验证成功！')         
        #高级搜索,通过残疾证号搜索
        searchPara4=copy.deepcopy(searchPara3)
        searchPara4['organizationId']=orgInit['DftWangGeOrgId']
        searchPara4['searchHandicappedVo.disabilityCardNo']= addPara1['population.disabilityCardNo'] 
        searchPara4['searchHandicappedVo.nativePlaceAddress']=''
        result41=ShiYouRenKouIntf.checkCanJiSeniorSearchList(checkpara=checkPara1,searchpara=searchPara4)
        self.assertTrue(result41, '通过残疾证号高级查询失败')
        result42=ShiYouRenKouIntf.checkCanJiSeniorSearchList(checkpara=checkPara2,searchpara=searchPara4)
        self.assertFalse(result42,'通过残疾证号高级查询失败')
        Log.LogOutput( message='通过残疾证号高级查询验证成功！')
        pass
    
    def testCanJiRenImportAndDownLoad_39(self):
        """关怀对象>残疾人信息 导入/导出"""
         
        importHuJiparam = copy.deepcopy(ShiYouRenKouPara.data)
        importHuJiparam['dataType']='handicapped'
        importHuJiparam['templates']='HANDICAPPED_syncActualPopulation'
        files = {'upload': ('test.xls', open('C:/autotest_file/importCanJiRen.xls', 'rb'),'applicationnd.ms-excel')}
        ret = ShiYouRenKouIntf.import_RenKou(importHuJiparam, files=files,username=userInit['DftWangGeUser'], password='11111111')         
        
        Time.wait(2)
        param = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        param['name'] = '残疾人导入测试'      
        param['idCardNo'] = '111111111111182'
        ret = ShiYouRenKouIntf.check_canJiRen(param, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找残疾人失败') 
                                
        downLoadHuJiparam = copy.deepcopy(ShiYouRenKouPara.dlZhongDianData)
        downLoadHuJiparam['organizationId']=orgInit['DftWangGeOrgId']
        response = ShiYouRenKouIntf.downLoad_canJiRen(downLoadHuJiparam, username=userInit['DftWangGeUser'], password='11111111')         
        with open("C:/autotest_file/downLoadCanJiRen.xls", "wb") as code:
            code.write(response.content)
            
        ret = CommonUtil.checkExcelCellValue(param['name'], 'downLoadCanJiRen.xls','残疾人清单', 'A4')          
        self.assertTrue(ret, '导出失败')
                         
        pass


    def testYouFuDuiXiangAdd_17(self):
        """关怀对象>优抚对象新增"""
  
        youFuParam_17 = copy.deepcopy(ShiYouRenKouPara.guanHuaiDuiXiangObject) 
        youFuParam_17['mode']='add'
        youFuParam_17['population.organization.id'] = orgInit['DftWangGeOrgId']
        youFuParam_17['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人员or流动人员
        youFuParam_17['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['youFuDuiXiang']
        youFuParam_17['population.organization.orgName'] = orgInit['DftWangGeOrg']
        youFuParam_17['population.idCardNo'] = '330000199711227700'  
        youFuParam_17['population.name'] = '优抚对象'
        youFuParam_17['actualPersonType'] = youFuParam_17['population.actualPopulationType']
        youFuParam_17['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        youFuParam_17['population.isHaveHouse1'] = 'null'   
        youFuParam_17['population.optimalCardNo'] = '11111'        
        responseDict = ShiYouRenKouIntf.add_youFuDuiXiang(youFuDuiXiangDict=youFuParam_17, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增优抚对象失败')       
          
        optimalCheckParam_17 = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        optimalCheckParam_17['name'] = youFuParam_17['population.name']       
        optimalCheckParam_17['idCardNo'] = youFuParam_17['population.idCardNo']
        ret = ShiYouRenKouIntf.check_youFuDuiXiang(optimalCheckParam_17, orgId=youFuParam_17['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找优抚对象失败')

        ret = ShiYouRenKouIntf.check_HuJiPopulation(optimalCheckParam_17, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '没有检查到户籍人口下对应的优抚对象信息')
        #补充修改用例
        updPara=copy.deepcopy(youFuParam_17)
        updPara['mode']='edit'
        updPara['population.id']=json.loads(responseDict.text)['id']
        updPara['population.name']='优抚对象'+createRandomString()
        updPara['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='女')
        responseDict = ShiYouRenKouIntf.add_youFuDuiXiang(updPara, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改优抚对象失败')
        #验证修改功能
        optimalCheckParam_17['name']= updPara['population.name']
        ret = ShiYouRenKouIntf.check_youFuDuiXiang(optimalCheckParam_17, orgId=updPara['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找优抚对象失败')
        Log.LogOutput( message='修改功能验证通过')
        #删除
        res=ShiYouRenKouIntf.delete_youFuDuiXiang({'populationIds':updPara['population.id']}, username = userInit['DftWangGeUser'], password = '11111111')
        self.assertTrue(res.result, '删除失败')
        #验证删除功能
        optimalCheckParam_17['name']= updPara['population.name']
        ret = ShiYouRenKouIntf.check_youFuDuiXiang(optimalCheckParam_17, orgId=updPara['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '删除失败')
        Log.LogOutput( message='删除验证通过')        
        pass 

    def testYouFuDuiXiangSearch_17(self):
        '''优抚对象查询'''
        #第一条
        addPara1 = copy.deepcopy(ShiYouRenKouPara.guanHuaiDuiXiangObject) 
        addPara1['mode']='add'
        addPara1['population.organization.id'] = orgInit['DftWangGeOrgId']
        addPara1['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人员or流动人员
        addPara1['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['youFuDuiXiang']
        addPara1['population.organization.orgName'] = orgInit['DftWangGeOrg']
        addPara1['population.idCardNo'] = '330000199711227701'  
        addPara1['population.name'] = '优抚对象'+createRandomString()
        addPara1['actualPersonType'] = addPara1['population.actualPopulationType']
        addPara1['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        addPara1['population.isHaveHouse1'] = 'null'   
        addPara1['population.optimalCardNo'] = '11111'  
        addPara1['population.nativePlaceAddress']='户籍地详址'+createRandomString()        
        responseDict = ShiYouRenKouIntf.add_youFuDuiXiang(youFuDuiXiangDict=addPara1, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增优抚对象失败')    
        #第二条
        addPara2 = copy.deepcopy(ShiYouRenKouPara.guanHuaiDuiXiangObject) 
        addPara2['mode']='add'
        addPara2['population.organization.id'] = orgInit['DftWangGeOrgId']
        addPara2['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人员or流动人员
        addPara2['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['youFuDuiXiang']
        addPara2['population.organization.orgName'] = orgInit['DftWangGeOrg']
        addPara2['population.idCardNo'] = '330000199711227700'  
        addPara2['population.name'] = '优抚对象'+createRandomString()
        addPara2['actualPersonType'] = addPara2['population.actualPopulationType']
        addPara2['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        addPara2['population.isHaveHouse1'] = 'null'   
        addPara2['population.optimalCardNo'] = '222222'  
        addPara2['population.nativePlaceAddress']='户籍地详址'+createRandomString()        
        responseDict = ShiYouRenKouIntf.add_youFuDuiXiang(youFuDuiXiangDict=addPara2, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增优抚对象失败')
        #根据姓名快速检索
        searchPara1=copy.deepcopy(ShiYouRenKouPara.fastSearch)
        searchPara1['organizationId']=orgInit['DftWangGeOrgId']
        searchPara1['searchOptimalObjectVo.isEmphasis']='0'
        searchPara1['searchOptimalObjectVo.fastSearchKeyWords']= addPara1['population.name']
        checkPara1={'name':addPara1['population.name']}
        checkPara2={'name':addPara2['population.name']}
        result11=ShiYouRenKouIntf.checkYouFuDuiXiangFastSearchList(checkpara=checkPara1,searchpara=searchPara1)
        self.assertTrue(result11, '通过姓名快速查询失败')
        result12=ShiYouRenKouIntf.checkYouFuDuiXiangFastSearchList(checkpara=checkPara2,searchpara=searchPara1)
        self.assertFalse(result12,'通过姓名快速查询失败')
        Log.LogOutput( message='通过姓名快速查询验证成功！')
        #根据身份证快速查询
        searchPara2=copy.deepcopy(searchPara1)
        searchPara2['searchOptimalObjectVo.fastSearchKeyWords']= addPara1['population.idCardNo']
        result21=ShiYouRenKouIntf.checkYouFuDuiXiangFastSearchList(checkpara=checkPara1,searchpara=searchPara2)
        self.assertTrue(result21, '通过身份证快速查询失败')
        result22=ShiYouRenKouIntf.checkYouFuDuiXiangFastSearchList(checkpara=checkPara2,searchpara=searchPara2)
        self.assertFalse(result22,'通过身份证快速查询失败')
        Log.LogOutput( message='通过身份证快速查询验证成功！')
        #高级搜索,通过户籍地详址搜索  
        searchPara3=copy.deepcopy(ShiYouRenKouPara.seniorSearch)
        searchPara3['organizationId']=orgInit['DftWangGeOrgId']
        searchPara3['searchOptimalObjectVo.isEmphasis']='-1'
        searchPara3['searchOptimalObjectVo.isDeath']='-1'
        searchPara3['searchOptimalObjectVo.hasServiceTeamMember']='-1'
        searchPara3['searchOptimalObjectVo.hasServiceTeamRecord']='-1'
        searchPara3['searchOptimalObjectVo.nativePlaceAddress']= addPara1['population.nativePlaceAddress']
        result31=ShiYouRenKouIntf.checkYouFuDuiXiangSeniorSearchList(checkpara=checkPara1,searchpara=searchPara3)
        self.assertTrue(result31, '通过户籍地详址高级查询失败')
        result32=ShiYouRenKouIntf.checkYouFuDuiXiangSeniorSearchList(checkpara=checkPara2,searchpara=searchPara3)
        self.assertFalse(result32,'通过户籍地详址高级查询失败')
        Log.LogOutput( message='通过户籍地详址高级查询验证成功！')         
        #高级搜索,通过优待证号搜索
        searchPara4=copy.deepcopy(searchPara3)
        searchPara4['organizationId']=orgInit['DftWangGeOrgId']
        searchPara4['searchOptimalObjectVo.optimalCardNo']= addPara1['population.optimalCardNo'] 
        searchPara4['searchOptimalObjectVo.nativePlaceAddress']=''
        result41=ShiYouRenKouIntf.checkYouFuDuiXiangSeniorSearchList(checkpara=checkPara1,searchpara=searchPara4)
        self.assertTrue(result41, '通过优待证号高级查询失败')
        result42=ShiYouRenKouIntf.checkYouFuDuiXiangSeniorSearchList(checkpara=checkPara2,searchpara=searchPara4)
        self.assertFalse(result42,'通过优待证号高级查询失败')
        Log.LogOutput( message='通过优待证号高级查询验证成功！')         
        pass
    
    def testYouFuDuiXiangImportAndDownLoad_40(self):
        """关怀对象>优抚对象信息 导入/导出"""
         
        importHuJiparam = copy.deepcopy(ShiYouRenKouPara.data)
        importHuJiparam['dataType']='optimalObject'
        importHuJiparam['templates']='OPTIMALOBJECT_syncActualPopulation'
        files = {'upload': ('test.xls', open('C:/autotest_file/importYouFuDuiXiang.xls', 'rb'),'applicationnd.ms-excel')}
        ret = ShiYouRenKouIntf.import_RenKou(importHuJiparam, files=files,username=userInit['DftWangGeUser'], password='11111111')         
        
        param = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        param['name'] = '优抚对象导入测试'      
        param['idCardNo'] = '111111111111182'
        ret = ShiYouRenKouIntf.check_youFuDuiXiang(param, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找优抚对象失败') 
                                
        downLoadHuJiparam = copy.deepcopy(ShiYouRenKouPara.dlZhongDianData)
        downLoadHuJiparam['organizationId']=orgInit['DftWangGeOrgId']
        response = ShiYouRenKouIntf.downLoad_youFuDuiXiang(downLoadHuJiparam, username=userInit['DftWangGeUser'], password='11111111')         
        with open("C:/autotest_file/downLoadYouFuDuiXiang.xls", "wb") as code:
            code.write(response.content)
            
        ret = CommonUtil.checkExcelCellValue(param['name'], 'downLoadYouFuDuiXiang.xls','优抚对象清单', 'A4')          
        self.assertTrue(ret, '导出失败')
                         
        pass


    def testXuYaoJiuZhuRenYuanAdd_17(self):
        """关怀对象>需要救助人员新增"""
  
        jiuZhuParam_17 = copy.deepcopy(ShiYouRenKouPara.guanHuaiDuiXiangObject) 
        jiuZhuParam_17['mode']='add'
        jiuZhuParam_17['population.organization.id'] = orgInit['DftWangGeOrgId']
        jiuZhuParam_17['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人员or流动人员
        jiuZhuParam_17['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['xuYaoJiuZhuRenYuan']
        jiuZhuParam_17['population.organization.orgName'] = orgInit['DftWangGeOrg']
        jiuZhuParam_17['population.idCardNo'] = '330000199711226600'  
        jiuZhuParam_17['population.name'] = '需要救助人员'
        jiuZhuParam_17['actualPersonType'] = jiuZhuParam_17['population.actualPopulationType']
        jiuZhuParam_17['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        jiuZhuParam_17['population.isHaveHouse1'] = 'null'   
        jiuZhuParam_17['population.aidReason.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='救助原因', displayName='无劳力（孤幼）')       
        responseDict = ShiYouRenKouIntf.add_xuYaoJiuZhuRenYuan(jiuZhuDict=jiuZhuParam_17, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增需要救助人员失败')       
          
        aidNeedCheckParam_17 = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        aidNeedCheckParam_17['name'] = jiuZhuParam_17['population.name']       
        aidNeedCheckParam_17['idCardNo'] = jiuZhuParam_17['population.idCardNo']
        ret = ShiYouRenKouIntf.check_xuYaoJiuZhuRenYuan(aidNeedCheckParam_17, orgId=jiuZhuParam_17['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找需要救助人员失败')

        ret = ShiYouRenKouIntf.check_HuJiPopulation(aidNeedCheckParam_17, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '没有检查到户籍人口下对应的需要救助人员信息')
        #补充修改用例
        updPara=copy.deepcopy(jiuZhuParam_17)
        updPara['mode']='edit'
        updPara['population.id']=json.loads(responseDict.text)['id']
        updPara['population.name']='需要救助对象'+createRandomString()
        updPara['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='女')
        responseDict = ShiYouRenKouIntf.add_xuYaoJiuZhuRenYuan(updPara, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改需要救助对象失败')
        #验证修改功能
        aidNeedCheckParam_17['name']= updPara['population.name']
        ret = ShiYouRenKouIntf.check_xuYaoJiuZhuRenYuan(aidNeedCheckParam_17, orgId=updPara['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找需要救助对象失败')
        Log.LogOutput( message='修改功能验证通过')
        #删除
        res=ShiYouRenKouIntf.delete_xuYaoJiuZhuRenYuan({'populationIds':updPara['population.id']}, username = userInit['DftWangGeUser'], password = '11111111')
        self.assertTrue(res.result, '删除失败')
        #验证删除功能
        aidNeedCheckParam_17['name']= updPara['population.name']
        ret = ShiYouRenKouIntf.check_xuYaoJiuZhuRenYuan(aidNeedCheckParam_17, orgId=updPara['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '删除失败')
        Log.LogOutput( message='删除验证通过')        
        pass 

    def testXuYaoJiuZhuRenYuanSearch_17(self):
        '''需要救助人员查询'''
        addPara1 = copy.deepcopy(ShiYouRenKouPara.guanHuaiDuiXiangObject) 
        addPara1['mode']='add'
        addPara1['population.organization.id'] = orgInit['DftWangGeOrgId']
        addPara1['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人员or流动人员
        addPara1['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['xuYaoJiuZhuRenYuan']
        addPara1['population.organization.orgName'] = orgInit['DftWangGeOrg']
        addPara1['population.idCardNo'] = '330000199711226601'  
        addPara1['population.name'] = '需要救助人员'+createRandomString()
        addPara1['actualPersonType'] = addPara1['population.actualPopulationType']
        addPara1['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        addPara1['population.isHaveHouse1'] = 'null'   
        addPara1['population.aidReason.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='救助原因', displayName='无劳力（孤幼）')       
        addPara1['population.nativePlaceAddress']='户籍地详址'+createRandomString()
        responseDict = ShiYouRenKouIntf.add_xuYaoJiuZhuRenYuan(jiuZhuDict=addPara1, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增需要救助人员失败')   
        #第二条
        addPara2 = copy.deepcopy(ShiYouRenKouPara.guanHuaiDuiXiangObject) 
        addPara2['mode']='add'
        addPara2['population.organization.id'] = orgInit['DftWangGeOrgId']
        addPara2['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人员or流动人员
        addPara2['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['xuYaoJiuZhuRenYuan']
        addPara2['population.organization.orgName'] = orgInit['DftWangGeOrg']
        addPara2['population.idCardNo'] = '330000199711226602'  
        addPara2['population.name'] = '需要救助人员'+createRandomString()
        addPara2['actualPersonType'] = addPara2['population.actualPopulationType']
        addPara2['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        addPara2['population.isHaveHouse1'] = 'null'   
        addPara2['population.aidReason.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='救助原因', displayName='未就业')       
        addPara2['population.nativePlaceAddress']='户籍地详址'+createRandomString()
        responseDict = ShiYouRenKouIntf.add_xuYaoJiuZhuRenYuan(jiuZhuDict=addPara2, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增需要救助人员失败')
        #根据姓名快速检索
        searchPara1=copy.deepcopy(ShiYouRenKouPara.fastSearch)
        searchPara1['organizationId']=orgInit['DftWangGeOrgId']
        searchPara1['searchAidNeedPopulationVo.isEmphasis']='0'
        searchPara1['searchAidNeedPopulationVo.fastSearchKeyWords']= addPara1['population.name']
        checkPara1={'name':addPara1['population.name']}
        checkPara2={'name':addPara2['population.name']}
        result11=ShiYouRenKouIntf.checkXuYaoJiuZhuFastSearchList(checkpara=checkPara1,searchpara=searchPara1)
        self.assertTrue(result11, '通过姓名快速查询失败')
        result12=ShiYouRenKouIntf.checkXuYaoJiuZhuFastSearchList(checkpara=checkPara2,searchpara=searchPara1)
        self.assertFalse(result12,'通过姓名快速查询失败')
        Log.LogOutput( message='通过姓名快速查询验证成功！')
        #根据身份证快速查询
        searchPara2=copy.deepcopy(searchPara1)
        searchPara2['searchAidNeedPopulationVo.fastSearchKeyWords']= addPara1['population.idCardNo']
        result21=ShiYouRenKouIntf.checkXuYaoJiuZhuFastSearchList(checkpara=checkPara1,searchpara=searchPara2)
        self.assertTrue(result21, '通过身份证快速查询失败')
        result22=ShiYouRenKouIntf.checkXuYaoJiuZhuFastSearchList(checkpara=checkPara2,searchpara=searchPara2)
        self.assertFalse(result22,'通过身份证快速查询失败')
        Log.LogOutput( message='通过身份证快速查询验证成功！')  
        #高级搜索,通过户籍地详址搜索  
        searchPara3=copy.deepcopy(ShiYouRenKouPara.seniorSearch)
        searchPara3['organizationId']=orgInit['DftWangGeOrgId']
        searchPara3['searchAidNeedPopulationVo.isEmphasis']='-1'
        searchPara3['searchAidNeedPopulationVo.isDeath']='-1'
        searchPara3['searchAidNeedPopulationVo.hasServiceTeamMember']='-1'
        searchPara3['searchAidNeedPopulationVo.hasServiceTeamRecord']='-1'
        searchPara3['searchAidNeedPopulationVo.nativePlaceAddress']= addPara1['population.nativePlaceAddress']
        result31=ShiYouRenKouIntf.checkXuYaoJiuZhuSeniorSearchList(checkpara=checkPara1,searchpara=searchPara3)
        self.assertTrue(result31, '通过户籍地详址高级查询失败')
        result32=ShiYouRenKouIntf.checkXuYaoJiuZhuSeniorSearchList(checkpara=checkPara2,searchpara=searchPara3)
        self.assertFalse(result32,'通过户籍地详址高级查询失败')
        Log.LogOutput( message='通过户籍地详址高级查询验证成功！')         
        #高级搜索,通过救助原因搜索
        searchPara4=copy.deepcopy(searchPara3)
        searchPara4['organizationId']=orgInit['DftWangGeOrgId']
        searchPara4['searchAidNeedPopulationVo.aidReason.id']= addPara1['population.aidReason.id']
        searchPara4['searchAidNeedPopulationVo.nativePlaceAddress']=''
        result41=ShiYouRenKouIntf.checkXuYaoJiuZhuSeniorSearchList(checkpara=checkPara1,searchpara=searchPara4)
        self.assertTrue(result41, '通过救助原因高级查询失败')
        result42=ShiYouRenKouIntf.checkXuYaoJiuZhuSeniorSearchList(checkpara=checkPara2,searchpara=searchPara4)
        self.assertFalse(result42,'通过救助原因高级查询失败')
        Log.LogOutput( message='通过救助原因高级查询验证成功！')        
        pass
    
    def testJiuZhuPopulationImportAndDownLoad_41(self):
        """关怀对象>需要救助人员信息 导入/导出"""
         
        importHuJiparam = copy.deepcopy(ShiYouRenKouPara.data)
        importHuJiparam['dataType']='aidNeedPopulation'
        importHuJiparam['templates']='AIDNEEDPOPULATION_syncActualPopulation'
        files = {'upload': ('test.xls', open('C:/autotest_file/importJiuZhuPopulation.xls', 'rb'),'applicationnd.ms-excel')}
        ret = ShiYouRenKouIntf.import_RenKou(importHuJiparam, files=files,username=userInit['DftWangGeUser'], password='11111111')         
        
        param = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        param['name'] = '需要救助人员导入测试'      
        param['idCardNo'] = '111111111111183'
        ret = ShiYouRenKouIntf.check_xuYaoJiuZhuRenYuan(param, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找需要救助人员失败') 
                                
        downLoadHuJiparam = copy.deepcopy(ShiYouRenKouPara.dlZhongDianData)
        downLoadHuJiparam['organizationId']=orgInit['DftWangGeOrgId']
        response = ShiYouRenKouIntf.downLoad_xuYaoJiuZhuRenYuan(downLoadHuJiparam, username=userInit['DftWangGeUser'], password='11111111')         
        with open("C:/autotest_file/downLoadJiuZhuPopulation.xls", "wb") as code:
            code.write(response.content)
            
        ret = CommonUtil.checkExcelCellValue(param['name'], 'downLoadJiuZhuPopulation.xls','需要救助人员清单', 'A4')          
        self.assertTrue(ret, '导出失败')
                         
        pass


    def testShiYeRenYuanAdd_17(self):
        """失业人员 新增"""
  
        shiYeParam_17 = copy.deepcopy(ShiYouRenKouPara.renYuanObject) 
        shiYeParam_17['mode']='add'
        shiYeParam_17['population.organization.id'] = orgInit['DftWangGeOrgId']
        shiYeParam_17['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人员or流动人员
        shiYeParam_17['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['shiYeRenYuan']
        shiYeParam_17['population.organization.orgName'] = orgInit['DftWangGeOrg']
        shiYeParam_17['population.idCardNo'] = '330000199711225500'  
        shiYeParam_17['population.name'] = '失业人员'
        shiYeParam_17['actualPersonType'] = shiYeParam_17['population.actualPopulationType']
        shiYeParam_17['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        shiYeParam_17['population.isHaveHouse1'] = 'null'   
        shiYeParam_17['population.unemploymentDate'] = '2015-12-02'        
        responseDict = ShiYouRenKouIntf.add_shiYeRenYuan(shiYeDict=shiYeParam_17, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失业人员失败')       
          
        unemployedCheckParam_17 = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        unemployedCheckParam_17['name'] = shiYeParam_17['population.name']       
        unemployedCheckParam_17['idCardNo'] = shiYeParam_17['population.idCardNo']
        ret = ShiYouRenKouIntf.check_shiYeRenYuan(unemployedCheckParam_17, orgId=shiYeParam_17['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找失业人员失败')

        ret = ShiYouRenKouIntf.check_HuJiPopulation(unemployedCheckParam_17, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '没有检查到户籍人口下对应的失业人员信息')
        #补充修改用例
        updPara=copy.deepcopy(shiYeParam_17)
        updPara['mode']='edit'
        updPara['population.id']=json.loads(responseDict.text)['id']
        updPara['population.name']='失业人员'+createRandomString()
        updPara['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='女')
        responseDict = ShiYouRenKouIntf.add_shiYeRenYuan(updPara, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改失业人员失败')
        #验证修改功能
        unemployedCheckParam_17['name']= updPara['population.name']
        ret = ShiYouRenKouIntf.check_shiYeRenYuan(unemployedCheckParam_17, orgId=updPara['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找失业人员失败')
        Log.LogOutput( message='修改功能验证通过')
        #删除
        res=ShiYouRenKouIntf.delete_shiYeRenYuan({'populationIds':updPara['population.id']}, username = userInit['DftWangGeUser'], password = '11111111')
#         self.assertTrue(res.result, '删除失败')
        #验证删除功能
        unemployedCheckParam_17['name']= updPara['population.name']
        ret = ShiYouRenKouIntf.check_shiYeRenYuan(unemployedCheckParam_17, orgId=updPara['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '删除失败')
        Log.LogOutput( message='删除验证通过')        
        pass 

    def testShiYeRenYuanSearch_17(self):
        '''失业人员查询'''
        addPara1 = copy.deepcopy(ShiYouRenKouPara.renYuanObject) 
        addPara1['mode']='add'
        addPara1['population.organization.id'] = orgInit['DftWangGeOrgId']
        addPara1['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人员or流动人员
        addPara1['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['shiYeRenYuan']
        addPara1['population.organization.orgName'] = orgInit['DftWangGeOrg']
        addPara1['population.idCardNo'] = '330000199711225501'  
        addPara1['population.name'] = '失业人员'+createRandomString()
        addPara1['actualPersonType'] = addPara1['population.actualPopulationType']
        addPara1['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        addPara1['population.isHaveHouse1'] = 'null'   
        addPara1['population.unemploymentDate'] = '2015-12-02'        
        addPara1['population.nativePlaceAddress']='户籍地详址'+createRandomString()
        addPara1['population.registerNumber']='111111'
        responseDict = ShiYouRenKouIntf.add_shiYeRenYuan(shiYeDict=addPara1, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失业人员失败')       
        #第二条
        addPara2 = copy.deepcopy(ShiYouRenKouPara.renYuanObject) 
        addPara2['mode']='add'
        addPara2['population.organization.id'] = orgInit['DftWangGeOrgId']
        addPara2['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人员or流动人员
        addPara2['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['shiYeRenYuan']
        addPara2['population.organization.orgName'] = orgInit['DftWangGeOrg']
        addPara2['population.idCardNo'] = '330000199711225502'  
        addPara2['population.name'] = '失业人员'+createRandomString()
        addPara2['actualPersonType'] = addPara2['population.actualPopulationType']
        addPara2['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        addPara2['population.isHaveHouse1'] = 'null'   
        addPara2['population.unemploymentDate'] = '2015-12-02'        
        addPara2['population.nativePlaceAddress']='户籍地详址'+createRandomString()
        addPara2['population.registerNumber']='222222'
        responseDict = ShiYouRenKouIntf.add_shiYeRenYuan(shiYeDict=addPara2, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失业人员失败')
        #根据姓名快速检索
        searchPara1=copy.deepcopy(ShiYouRenKouPara.fastSearch)
        searchPara1['organizationId']=orgInit['DftWangGeOrgId']
        searchPara1['searchUnemployedPeopleVo.isEmphasis']='0'
        searchPara1['searchUnemployedPeopleVo.fastSearchKeyWords']= addPara1['population.name']
        checkPara1={'name':addPara1['population.name']}
        checkPara2={'name':addPara2['population.name']}
        result11=ShiYouRenKouIntf.checkShiYeFastSearchList(checkpara=checkPara1,searchpara=searchPara1)
        self.assertTrue(result11, '通过姓名快速查询失败')
        result12=ShiYouRenKouIntf.checkShiYeFastSearchList(checkpara=checkPara2,searchpara=searchPara1)
        self.assertFalse(result12,'通过姓名快速查询失败')
        Log.LogOutput( message='通过姓名快速查询验证成功！')
        #根据身份证快速查询
        searchPara2=copy.deepcopy(searchPara1)
        searchPara2['searchUnemployedPeopleVo.fastSearchKeyWords']= addPara1['population.idCardNo']
        result21=ShiYouRenKouIntf.checkShiYeFastSearchList(checkpara=checkPara1,searchpara=searchPara2)
        self.assertTrue(result21, '通过身份证快速查询失败')
        result22=ShiYouRenKouIntf.checkShiYeFastSearchList(checkpara=checkPara2,searchpara=searchPara2)
        self.assertFalse(result22,'通过身份证快速查询失败')
        Log.LogOutput( message='通过身份证快速查询验证成功！')
        #高级搜索,通过户籍地详址搜索  
        searchPara3=copy.deepcopy(ShiYouRenKouPara.seniorSearch)
        searchPara3['organizationId']=orgInit['DftWangGeOrgId']
        searchPara3['searchUnemployedPeopleVo.isEmphasis']='-1'
        searchPara3['searchUnemployedPeopleVo.isDeath']='-1'
        searchPara3['searchUnemployedPeopleVo.hasServiceTeamMember']='-1'
        searchPara3['searchUnemployedPeopleVo.hasServiceTeamRecord']='-1'
        searchPara3['searchUnemployedPeopleVo.nativePlaceAddress']= addPara1['population.nativePlaceAddress']
        result31=ShiYouRenKouIntf.checkShiYeSeniorSearchList(checkpara=checkPara1,searchpara=searchPara3)
        self.assertTrue(result31, '通过户籍地详址高级查询失败')
        result32=ShiYouRenKouIntf.checkShiYeSeniorSearchList(checkpara=checkPara2,searchpara=searchPara3)
        self.assertFalse(result32,'通过户籍地详址高级查询失败')
        Log.LogOutput( message='通过户籍地详址高级查询验证成功！')         
        #高级搜索,通过登记证号搜索
        searchPara4=copy.deepcopy(searchPara3)
        searchPara4['organizationId']=orgInit['DftWangGeOrgId']
        searchPara4['searchUnemployedPeopleVo.registerNumber']= addPara1['population.registerNumber']
        searchPara4['searchUnemployedPeopleVo.nativePlaceAddress']=''
        result41=ShiYouRenKouIntf.checkShiYeSeniorSearchList(checkpara=checkPara1,searchpara=searchPara4)
        self.assertTrue(result41, '通过登记证号高级查询失败')
        result42=ShiYouRenKouIntf.checkShiYeSeniorSearchList(checkpara=checkPara2,searchpara=searchPara4)
        self.assertFalse(result42,'通过登记证号高级查询失败')
        Log.LogOutput( message='通过登记证号高级查询验证成功！')       
        pass
    
    def testShiYePopulationImportAndDownLoad_42(self):
        """失业人员信息 导入/导出"""
         
        importHuJiparam = copy.deepcopy(ShiYouRenKouPara.data)
        importHuJiparam['dataType']='unemployedPeople'
        importHuJiparam['templates']='UNEMPLOYEDPEOPLE_syncActualPopulation'
        files = {'upload': ('test.xls', open('C:/autotest_file/importShiYePopulation.xls', 'rb'),'applicationnd.ms-excel')}
        ret = ShiYouRenKouIntf.import_RenKou(importHuJiparam, files=files,username=userInit['DftWangGeUser'], password='11111111')         
        
        param = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        param['name'] = '失业人员导入测试'      
        param['idCardNo'] = '111111111111184'
        ret = ShiYouRenKouIntf.check_shiYeRenYuan(param, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找失业人员失败') 
                                
        downLoadHuJiparam = copy.deepcopy(ShiYouRenKouPara.dlZhongDianData)
        downLoadHuJiparam['organizationId']=orgInit['DftWangGeOrgId']
        response = ShiYouRenKouIntf.downLoad_shiYeRenYuan(downLoadHuJiparam, username=userInit['DftWangGeUser'], password='11111111')         
        with open("C:/autotest_file/downLoadShiYePopulation.xls", "wb") as code:
            code.write(response.content)
            
        ret = CommonUtil.checkExcelCellValue(param['name'], 'downLoadShiYePopulation.xls','失业人员清单', 'A4')          
        self.assertTrue(ret, '导出失败')
                         
        pass


    def testYuLingFuNvAdd_17(self):
        """育龄妇女 新增 """
  
        yuLingParam_17 = copy.deepcopy(ShiYouRenKouPara.renYuanObject) 
        yuLingParam_17['mode']='add'
        yuLingParam_17['population.organization.id'] = orgInit['DftWangGeOrgId']
        yuLingParam_17['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人员or流动人员
        yuLingParam_17['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['yuLingFuNv']
        yuLingParam_17['population.organization.orgName'] = orgInit['DftWangGeOrg']
        yuLingParam_17['population.idCardNo'] = '330000199711224400'  
        yuLingParam_17['population.name'] = '育龄妇女'
        yuLingParam_17['actualPersonType'] = yuLingParam_17['population.actualPopulationType']
        yuLingParam_17['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        yuLingParam_17['population.isHaveHouse1'] = 'null'   
        yuLingParam_17['population.population.attentionExtent.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='关注程度', displayName='一般')
        yuLingParam_17['population.boyNumber'] = '1' 
        yuLingParam_17['population.girlNumber'] = '0' 
        yuLingParam_17['population.manCurrentAddressType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='现居地址', displayName='商品房')
        responseDict = ShiYouRenKouIntf.add_yuLingFuNv(yuLingDict=yuLingParam_17, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增育龄妇女失败')       
          
        nurturesCheckParam_17 = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        nurturesCheckParam_17['name'] = yuLingParam_17['population.name']       
        nurturesCheckParam_17['idCardNo'] = yuLingParam_17['population.idCardNo']
        ret = ShiYouRenKouIntf.check_yuLingFuNv(nurturesCheckParam_17, orgId=yuLingParam_17['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找育龄妇女失败')

        ret = ShiYouRenKouIntf.check_HuJiPopulation(nurturesCheckParam_17, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '没有检查到户籍人口下对应的育龄妇女信息')
        #补充修改用例
        updPara=copy.deepcopy(yuLingParam_17)
        updPara['mode']='edit'
        updPara['population.id']=json.loads(responseDict.text)['id']
        updPara['population.name']='育龄妇女'+createRandomString()
        updPara['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='女')
        responseDict = ShiYouRenKouIntf.add_yuLingFuNv(updPara, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改育龄妇女失败')
        #验证修改功能
        nurturesCheckParam_17['name']= updPara['population.name']
        ret = ShiYouRenKouIntf.check_yuLingFuNv(nurturesCheckParam_17, orgId=updPara['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找育龄妇女失败')
        Log.LogOutput( message='修改功能验证通过')
        #删除
        res=ShiYouRenKouIntf.delete_yuLingFuNv({'populationIds':updPara['population.id']}, username = userInit['DftWangGeUser'], password = '11111111')
#         self.assertTrue(res.result, '删除失败')
        #验证删除功能
        nurturesCheckParam_17['name']= updPara['population.name']
        ret = ShiYouRenKouIntf.check_yuLingFuNv(nurturesCheckParam_17, orgId=updPara['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '删除失败')
        Log.LogOutput( message='删除验证通过')        
        pass 

    def testYuLingFuNvSearch_17(self):
        '''育龄妇女查询'''
        addPara1 = copy.deepcopy(ShiYouRenKouPara.renYuanObject) 
        addPara1['mode']='add'
        addPara1['population.organization.id'] = orgInit['DftWangGeOrgId']
        addPara1['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人员or流动人员
        addPara1['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['yuLingFuNv']
        addPara1['population.organization.orgName'] = orgInit['DftWangGeOrg']
        addPara1['population.idCardNo'] = '330000199711224401'  
        addPara1['population.name'] = '育龄妇女'+createRandomString()
        addPara1['actualPersonType'] = addPara1['population.actualPopulationType']
        addPara1['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        addPara1['population.isHaveHouse1'] = 'null'   
        addPara1['population.population.attentionExtent.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='关注程度', displayName='一般')
        addPara1['population.boyNumber'] = '1' 
        addPara1['population.girlNumber'] = '0' 
        addPara1['population.manCurrentAddressType.id'] =CommonIntf.getIdByDomainAndDisplayName(domainName='现居地址', displayName='商品房')
        addPara1['population.nativePlaceAddress']='户籍地详址'+createRandomString()
        responseDict = ShiYouRenKouIntf.add_yuLingFuNv(yuLingDict=addPara1, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增育龄妇女失败')   
        #第二条
        addPara2 = copy.deepcopy(ShiYouRenKouPara.renYuanObject) 
        addPara2['mode']='add'
        addPara2['population.organization.id'] = orgInit['DftWangGeOrgId']
        addPara2['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人员or流动人员
        addPara2['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['yuLingFuNv']
        addPara2['population.organization.orgName'] = orgInit['DftWangGeOrg']
        addPara2['population.idCardNo'] = '330000199711224402'  
        addPara2['population.name'] = '育龄妇女'+createRandomString()
        addPara2['actualPersonType'] = addPara2['population.actualPopulationType']
        addPara2['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        addPara2['population.isHaveHouse1'] = 'null'   
        addPara2['population.population.attentionExtent.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='关注程度', displayName='中等')
        addPara2['population.boyNumber'] = '1' 
        addPara2['population.girlNumber'] = '2' 
        addPara2['population.manCurrentAddressType.id'] =CommonIntf.getIdByDomainAndDisplayName(domainName='现居地址', displayName='商品房')
        addPara2['population.nativePlaceAddress']='户籍地详址'+createRandomString()
        responseDict = ShiYouRenKouIntf.add_yuLingFuNv(yuLingDict=addPara2, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增育龄妇女失败')
        #根据姓名快速检索
        searchPara1=copy.deepcopy(ShiYouRenKouPara.fastSearch)
        searchPara1['organizationId']=orgInit['DftWangGeOrgId']
        searchPara1['searchNurturesWomenVo.isEmphasis']='0'
        searchPara1['searchNurturesWomenVo.fastSearchKeyWords']= addPara1['population.name']
        checkPara1={'name':addPara1['population.name']}
        checkPara2={'name':addPara2['population.name']}
        result11=ShiYouRenKouIntf.checkYuLingFuNvFastSearchList(checkpara=checkPara1,searchpara=searchPara1)
        self.assertTrue(result11, '通过姓名快速查询失败')
        result12=ShiYouRenKouIntf.checkYuLingFuNvFastSearchList(checkpara=checkPara2,searchpara=searchPara1)
        self.assertFalse(result12,'通过姓名快速查询失败')
        Log.LogOutput( message='通过姓名快速查询验证成功！')
        #根据身份证快速查询
        searchPara2=copy.deepcopy(searchPara1)
        searchPara2['searchNurturesWomenVo.fastSearchKeyWords']= addPara1['population.idCardNo']
        result21=ShiYouRenKouIntf.checkYuLingFuNvFastSearchList(checkpara=checkPara1,searchpara=searchPara2)
        self.assertTrue(result21, '通过身份证快速查询失败')
        result22=ShiYouRenKouIntf.checkYuLingFuNvFastSearchList(checkpara=checkPara2,searchpara=searchPara2)
        self.assertFalse(result22,'通过身份证快速查询失败')
        Log.LogOutput( message='通过身份证快速查询验证成功！')
        #高级搜索,通过户籍地详址搜索  
        searchPara3=copy.deepcopy(ShiYouRenKouPara.seniorSearch)
        searchPara3['organizationId']=orgInit['DftWangGeOrgId']
        searchPara3['searchNurturesWomenVo.isEmphasis']='-1'
        searchPara3['searchNurturesWomenVo.isDeath']='-1'
        searchPara3['searchNurturesWomenVo.hasServiceTeamMember']='-1'
        searchPara3['searchNurturesWomenVo.hasServiceTeamRecord']='-1'
        searchPara3['searchNurturesWomenVo.nativePlaceAddress']= addPara1['population.nativePlaceAddress']
        result31=ShiYouRenKouIntf.checkYuLingFuNvSeniorSearchList(checkpara=checkPara1,searchpara=searchPara3)
        self.assertTrue(result31, '通过户籍地详址高级查询失败')
        result32=ShiYouRenKouIntf.checkYuLingFuNvSeniorSearchList(checkpara=checkPara2,searchpara=searchPara3)
        self.assertFalse(result32,'通过户籍地详址高级查询失败')
        Log.LogOutput( message='通过户籍地详址高级查询验证成功！')         
        #高级搜索,通过子女数搜索
        searchPara4=copy.deepcopy(searchPara3)
        searchPara4['organizationId']=orgInit['DftWangGeOrgId']
        searchPara4['searchNurturesWomenVo.childNumberStart']= '0'
        searchPara4['searchNurturesWomenVo.childNumberEnd']= '2'
        searchPara4['searchNurturesWomenVo.nativePlaceAddress']=''
        result41=ShiYouRenKouIntf.checkYuLingFuNvSeniorSearchList(checkpara=checkPara1,searchpara=searchPara4)
        self.assertTrue(result41, '通过子女数高级查询失败')
        result42=ShiYouRenKouIntf.checkYuLingFuNvSeniorSearchList(checkpara=checkPara2,searchpara=searchPara4)
        self.assertFalse(result42,'通过子女数高级查询失败')
        Log.LogOutput( message='通过子女数高级查询验证成功！')        
        pass
    
    def testYuLingFuNvImportAndDownLoad_43(self):
        """育龄妇女信息 导入/导出"""
         
        importHuJiparam = copy.deepcopy(ShiYouRenKouPara.data)
        importHuJiparam['dataType']='nurturesWomen'
        importHuJiparam['templates']='NURTURESWOMEN_syncActualPopulation'
        files = {'upload': ('test.xls', open('C:/autotest_file/importYuLingFuNv.xls', 'rb'),'applicationnd.ms-excel')}
        ret = ShiYouRenKouIntf.import_RenKou(importHuJiparam, files=files,username=userInit['DftWangGeUser'], password='11111111')         
        
        Time.wait(2)
        param = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        param['name'] = '育龄妇女导入测试'      
        param['idCardNo'] = '330000198811120000'
        ret = ShiYouRenKouIntf.check_yuLingFuNv(param, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找育龄妇女失败') 
                                
        downLoadHuJiparam = copy.deepcopy(ShiYouRenKouPara.dlZhongDianData)
        downLoadHuJiparam['organizationId']=orgInit['DftWangGeOrgId']
        response = ShiYouRenKouIntf.downLoad_yuLingFuNv(downLoadHuJiparam, username=userInit['DftWangGeUser'], password='11111111')         
        with open("C:/autotest_file/downLoadYuLingFuNv.xls", "wb") as code:
            code.write(response.content)
            
        ret = CommonUtil.checkExcelCellValue(param['name'], 'downLoadYuLingFuNv.xls','育龄妇女清单', 'A4')          
        self.assertTrue(ret, '导出失败')
                         
        pass


    def testQiaoShuAdd_17(self):
        """侨属人员 新增 """
  
        qiaoShuParam_17 = copy.deepcopy(ShiYouRenKouPara.renYuanObject) 
        qiaoShuParam_17['mode']='add'
        qiaoShuParam_17['population.organization.id'] = orgInit['DftWangGeOrgId']
        qiaoShuParam_17['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人员or流动人员
        qiaoShuParam_17['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['qiaoShu']
        qiaoShuParam_17['population.organization.orgName'] = orgInit['DftWangGeOrg']
        qiaoShuParam_17['population.idCardNo'] = '330000199711223300'  
        qiaoShuParam_17['population.name'] = '侨属'
        qiaoShuParam_17['actualPersonType'] = qiaoShuParam_17['population.actualPopulationType']
        qiaoShuParam_17['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        qiaoShuParam_17['population.isHaveHouse1'] = 'null'   
        qiaoShuParam_17['population.abroadDependentsType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='侨属类别', displayName='归侨')
        qiaoShuParam_17['population.abroadDependents'] = '1'  
        responseDict = ShiYouRenKouIntf.add_qiaoShu(qiaoShuDict=qiaoShuParam_17, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增侨属失败')       
          
        abroadCheckParam_17 = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        abroadCheckParam_17['name'] = qiaoShuParam_17['population.name']       
        abroadCheckParam_17['idCardNo'] = qiaoShuParam_17['population.idCardNo']
        ret = ShiYouRenKouIntf.check_qiaoShu(abroadCheckParam_17, orgId=qiaoShuParam_17['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找侨属失败')

        ret = ShiYouRenKouIntf.check_HuJiPopulation(abroadCheckParam_17, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '没有检查到户籍人口下对应的侨属信息')
        #补充修改用例
        updPara=copy.deepcopy(qiaoShuParam_17)
        updPara['mode']='edit'
        updPara['population.id']=json.loads(responseDict.text)['id']
        updPara['population.name']='乔属'+createRandomString()
        updPara['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='女')
        responseDict = ShiYouRenKouIntf.add_qiaoShu(updPara, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改乔属失败')
        #验证修改功能
        abroadCheckParam_17['name']= updPara['population.name']
        ret = ShiYouRenKouIntf.check_qiaoShu(abroadCheckParam_17, orgId=updPara['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找乔属失败')
        Log.LogOutput( message='修改功能验证通过')
        #删除
        res=ShiYouRenKouIntf.delete_qiaoShu({'ids':updPara['population.id']}, username = userInit['DftWangGeUser'], password = '11111111')
        self.assertTrue(res.result, '删除失败')
        #验证删除功能
        abroadCheckParam_17['name']= updPara['population.name']
        ret = ShiYouRenKouIntf.check_qiaoShu(abroadCheckParam_17, orgId=updPara['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '删除失败')
        Log.LogOutput( message='删除验证通过')        
        pass 

    def testQiaoShuSearch_17(self):
        '''乔属查询'''
        #第一条
        addPara1 = copy.deepcopy(ShiYouRenKouPara.renYuanObject) 
        addPara1['mode']='add'
        addPara1['population.organization.id'] = orgInit['DftWangGeOrgId']
        addPara1['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人员or流动人员
        addPara1['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['qiaoShu']
        addPara1['population.organization.orgName'] = orgInit['DftWangGeOrg']
        addPara1['population.idCardNo'] = '330000199711223301'  
        addPara1['population.name'] = '侨属'+createRandomString()
        addPara1['actualPersonType'] = addPara1['population.actualPopulationType']
        addPara1['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        addPara1['population.isHaveHouse1'] = 'null'   
        addPara1['population.abroadDependentsType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='侨属类别', displayName='归侨')
        addPara1['population.abroadDependents'] = '1'  
        addPara1['population.nativePlaceAddress']='户籍地详址'+createRandomString()
        responseDict = ShiYouRenKouIntf.add_qiaoShu(qiaoShuDict=addPara1, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增侨属失败')          
        #第二条
        addPara2 = copy.deepcopy(ShiYouRenKouPara.renYuanObject) 
        addPara2['mode']='add'
        addPara2['population.organization.id'] = orgInit['DftWangGeOrgId']
        addPara2['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人员or流动人员
        addPara2['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['qiaoShu']
        addPara2['population.organization.orgName'] = orgInit['DftWangGeOrg']
        addPara2['population.idCardNo'] = '330000199711223302'  
        addPara2['population.name'] = '侨属'+createRandomString()
        addPara2['actualPersonType'] = addPara2['population.actualPopulationType']
        addPara2['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        addPara2['population.isHaveHouse1'] = 'null'   
        addPara2['population.abroadDependentsType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='侨属类别', displayName='台胞')
        addPara2['population.abroadDependents'] = '1'  
        addPara2['population.nativePlaceAddress']='户籍地详址'+createRandomString()
        responseDict = ShiYouRenKouIntf.add_qiaoShu(qiaoShuDict=addPara2, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增侨属失败')      
        
        #根据姓名快速检索
        searchPara1=copy.deepcopy(ShiYouRenKouPara.fastSearch)
        searchPara1['abroadDependent.organization.id']=orgInit['DftWangGeOrgId']
        searchPara1['abroadDependent.isEmphasis']='0'
        searchPara1['abroadDependent.whetherDeath']='0'
        searchPara1['abroadDependent.fastSearchKeyWords']= addPara1['population.name']
        checkPara1={'name':addPara1['population.name']}
        checkPara2={'name':addPara2['population.name']}
        result11=ShiYouRenKouIntf.checkQiaoShuFastSearchList(checkpara=checkPara1,searchpara=searchPara1)
        self.assertTrue(result11, '通过姓名快速查询失败')
        result12=ShiYouRenKouIntf.checkQiaoShuFastSearchList(checkpara=checkPara2,searchpara=searchPara1)
        self.assertFalse(result12,'通过姓名快速查询失败')
        Log.LogOutput( message='通过姓名快速查询验证成功！')
        #根据身份证快速查询
        searchPara2=copy.deepcopy(searchPara1)
        searchPara2['abroadDependent.fastSearchKeyWords']= addPara1['population.idCardNo']
        result21=ShiYouRenKouIntf.checkQiaoShuFastSearchList(checkpara=checkPara1,searchpara=searchPara2)
        self.assertTrue(result21, '通过身份证快速查询失败')
        result22=ShiYouRenKouIntf.checkQiaoShuFastSearchList(checkpara=checkPara2,searchpara=searchPara2)
        self.assertFalse(result22,'通过身份证快速查询失败')
        Log.LogOutput( message='通过身份证快速查询验证成功！')
        #高级搜索,通过户籍地详址搜索  
        searchPara3=copy.deepcopy(ShiYouRenKouPara.seniorSearch)
        searchPara3['abroadDependent.organization.id']=orgInit['DftWangGeOrgId']
        searchPara3['abroadDependent.isEmphasis']='-1'
        searchPara3['abroadDependent.whetherDeath']='-1'
        searchPara3['abroadDependent.nativePlaceAddress']= addPara1['population.nativePlaceAddress']
        result31=ShiYouRenKouIntf.checkQiaoShuSeniorSearchList(checkpara=checkPara1,searchpara=searchPara3)
        self.assertTrue(result31, '通过户籍地详址高级查询失败')
        result32=ShiYouRenKouIntf.checkQiaoShuSeniorSearchList(checkpara=checkPara2,searchpara=searchPara3)
        self.assertFalse(result32,'通过户籍地详址高级查询失败')
        Log.LogOutput( message='通过户籍地详址高级查询验证成功！')         
        #高级搜索,通过乔属类别搜索
        searchPara4=copy.deepcopy(searchPara3)
        searchPara4['organizationId']=orgInit['DftWangGeOrgId']
        searchPara4['abroadDependent.abroadDependentsType.id']=addPara1['population.abroadDependentsType.id']
        searchPara4['abroadDependent.nativePlaceAddress']=''
        result41=ShiYouRenKouIntf.checkQiaoShuSeniorSearchList(checkpara=checkPara1,searchpara=searchPara4)
        self.assertTrue(result41, '通过乔属类别高级查询失败')
        result42=ShiYouRenKouIntf.checkQiaoShuSeniorSearchList(checkpara=checkPara2,searchpara=searchPara4)
        self.assertFalse(result42,'通过乔属类别高级查询失败')
        Log.LogOutput( message='通过乔属类别高级查询验证成功！')        
        
        
            
        pass
    
    def testShiDiJiaTingAdd_17(self):
        """失地家庭 新增 """
  
        shiDiParam_17 = copy.deepcopy(ShiYouRenKouPara.renYuanObject) 
        shiDiParam_17['mode']='add'
        shiDiParam_17['population.organization.id'] = orgInit['DftWangGeOrgId']
        shiDiParam_17['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人员or流动人员
        shiDiParam_17['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['shiDiJiaTing']
        shiDiParam_17['population.organization.orgName'] = orgInit['DftWangGeOrg']
        shiDiParam_17['population.idCardNo'] = '330000199711222200'  
        shiDiParam_17['population.name'] = '失地家庭'
        shiDiParam_17['actualPersonType'] = shiDiParam_17['population.actualPopulationType']
        shiDiParam_17['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        shiDiParam_17['population.isHaveHouse1'] = 'null'   
        shiDiParam_17['population.lostEarthDate'] = '2015-12-05'   
        shiDiParam_17['population.lostEarthReason.id'] =CommonIntf.getIdByDomainAndDisplayName(domainName='失地原因', displayName='征收征用') #失地原因，非必填项
        responseDict = ShiYouRenKouIntf.add_shiDiJiaTing(lostDict=shiDiParam_17, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失地家庭失败')       
          
        lostCheckParam_17 = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        lostCheckParam_17['name'] = shiDiParam_17['population.name']       
        lostCheckParam_17['idCardNo'] = shiDiParam_17['population.idCardNo']
        ret = ShiYouRenKouIntf.check_shiDiJiaTing(lostCheckParam_17, orgId=shiDiParam_17['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找失地家庭失败')

        ret = ShiYouRenKouIntf.check_HuJiPopulation(lostCheckParam_17, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '没有检查到户籍人口下对应的失地家庭信息')
        #补充修改用例
        updPara=copy.deepcopy(shiDiParam_17)
        updPara['mode']='edit'
        updPara['population.id']=json.loads(responseDict.text)['id']
        updPara['population.name']='失地家庭'+createRandomString()
        updPara['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='女')
        responseDict = ShiYouRenKouIntf.add_shiDiJiaTing(updPara, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改失地家庭失败')
        #验证修改功能
        lostCheckParam_17['name']= updPara['population.name']
        ret = ShiYouRenKouIntf.check_shiDiJiaTing(lostCheckParam_17, orgId=updPara['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '修改验证失败')
        Log.LogOutput( message='修改功能验证通过')
        #删除
        res=ShiYouRenKouIntf.delete_shiDiJiaTing({'populationIds':updPara['population.id']}, username = userInit['DftWangGeUser'], password = '11111111')
#         self.assertTrue(res.result, '删除失败')
        #验证删除功能
        lostCheckParam_17['name']= updPara['population.name']
        ret = ShiYouRenKouIntf.check_shiDiJiaTing(lostCheckParam_17, orgId=updPara['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '删除失败')
        Log.LogOutput( message='删除验证通过')        
        pass 

    def testShiDiJiaTingSearch_17(self):
        '''失地家庭查询'''
        addPara1 = copy.deepcopy(ShiYouRenKouPara.renYuanObject) 
        addPara1['mode']='add'
        addPara1['population.organization.id'] = orgInit['DftWangGeOrgId']
        addPara1['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人员or流动人员
        addPara1['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['shiDiJiaTing']
        addPara1['population.organization.orgName'] = orgInit['DftWangGeOrg']
        addPara1['population.idCardNo'] = '330000199711222201'  
        addPara1['population.name'] = '失地家庭'+createRandomString()
        addPara1['actualPersonType'] = addPara1['population.actualPopulationType']
        addPara1['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        addPara1['population.isHaveHouse1'] = 'null'   
        addPara1['population.lostEarthDate'] = '2015-12-05'   
        addPara1['population.lostEarthReason.id'] =CommonIntf.getIdByDomainAndDisplayName(domainName='失地原因', displayName='征收征用')#失地原因，非必填项
        addPara1['population.nativePlaceAddress']='户籍地详址'+createRandomString()
        responseDict = ShiYouRenKouIntf.add_shiDiJiaTing(lostDict=addPara1, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失地家庭失败')      
        #第二条
        addPara2 = copy.deepcopy(ShiYouRenKouPara.renYuanObject) 
        addPara2['mode']='add'
        addPara2['population.organization.id'] = orgInit['DftWangGeOrgId']
        addPara2['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人员or流动人员
        addPara2['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['shiDiJiaTing']
        addPara2['population.organization.orgName'] = orgInit['DftWangGeOrg']
        addPara2['population.idCardNo'] = '330000199711222202'  
        addPara2['population.name'] = '失地家庭'+createRandomString()
        addPara2['actualPersonType'] = addPara2['population.actualPopulationType']
        addPara2['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
        addPara2['population.isHaveHouse1'] = 'null'   
        addPara2['population.lostEarthDate'] = '2016-3-05'   
        addPara2['population.lostEarthReason.id'] =CommonIntf.getIdByDomainAndDisplayName(domainName='失地原因', displayName='村集体使用') #失地原因，非必填项
        addPara2['population.nativePlaceAddress']='户籍地详址'+createRandomString()
        responseDict = ShiYouRenKouIntf.add_shiDiJiaTing(lostDict=addPara2, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失地家庭失败')
        #根据姓名快速检索
        searchPara1=copy.deepcopy(ShiYouRenKouPara.fastSearch)
        searchPara1['organizationId']=orgInit['DftWangGeOrgId']
        searchPara1['searchLostEarthVo.isEmphasis']='0'
        searchPara1['searchLostEarthVo.fastSearchKeyWords']= addPara1['population.name']
        checkPara1={'name':addPara1['population.name']}
        checkPara2={'name':addPara2['population.name']}
        result11=ShiYouRenKouIntf.checkShiDiJiaTingFastSearchList(checkpara=checkPara1,searchpara=searchPara1)
        self.assertTrue(result11, '通过姓名快速查询失败')
        result12=ShiYouRenKouIntf.checkShiDiJiaTingFastSearchList(checkpara=checkPara2,searchpara=searchPara1)
        self.assertFalse(result12,'通过姓名快速查询失败')
        Log.LogOutput( message='通过姓名快速查询验证成功！')
        #根据身份证快速查询
        searchPara2=copy.deepcopy(searchPara1)
        searchPara2['searchLostEarthVo.fastSearchKeyWords']= addPara1['population.idCardNo']
        result21=ShiYouRenKouIntf.checkShiDiJiaTingFastSearchList(checkpara=checkPara1,searchpara=searchPara2)
        self.assertTrue(result21, '通过身份证快速查询失败')
        result22=ShiYouRenKouIntf.checkShiDiJiaTingFastSearchList(checkpara=checkPara2,searchpara=searchPara2)
        self.assertFalse(result22,'通过身份证快速查询失败')
        Log.LogOutput( message='通过身份证快速查询验证成功！')   
        #高级搜索,通过户籍地详址搜索  
        searchPara3=copy.deepcopy(ShiYouRenKouPara.seniorSearch)
        searchPara3['organizationId']=orgInit['DftWangGeOrgId']
        searchPara3['searchLostEarthVo.isEmphasis']='-1'
        searchPara3['searchLostEarthVo.isDeath']='-1'
        searchPara3['searchLostEarthVo.hasServiceTeamMember']='-1'
        searchPara3['searchLostEarthVo.hasServiceTeamRecord']='-1'
        searchPara3['searchLostEarthVo.nativePlaceAddress']= addPara1['population.nativePlaceAddress']
        result31=ShiYouRenKouIntf.checkShiDiJiaTingSeniorSearchList(checkpara=checkPara1,searchpara=searchPara3)
        self.assertTrue(result31, '通过户籍地详址高级查询失败')
        result32=ShiYouRenKouIntf.checkShiDiJiaTingSeniorSearchList(checkpara=checkPara2,searchpara=searchPara3)
        self.assertFalse(result32,'通过户籍地详址高级查询失败')
        Log.LogOutput( message='通过户籍地详址高级查询验证成功！')         
        #高级搜索,通过失地日期搜索
        searchPara4=copy.deepcopy(searchPara3)
        searchPara4['organizationId']=orgInit['DftWangGeOrgId']
        searchPara4['searchLostEarthVo.lostEarthDateFrom']= '2015-12-1'
        searchPara4['searchLostEarthVo.lostEarthDateEnd']= '2015-12-31'
        searchPara4['searchLostEarthVo.nativePlaceAddress']=''
        result41=ShiYouRenKouIntf.checkShiDiJiaTingSeniorSearchList(checkpara=checkPara1,searchpara=searchPara4)
        self.assertTrue(result41, '通过失地日期高级查询失败')
        result42=ShiYouRenKouIntf.checkShiDiJiaTingSeniorSearchList(checkpara=checkPara2,searchpara=searchPara4)
        self.assertFalse(result42,'通过失地日期高级查询失败')
        Log.LogOutput( message='通过失地日期高级查询验证成功！')        
        #高级搜索,通过失地原因搜索
        searchPara5=copy.deepcopy(searchPara3)
        searchPara5['organizationId']=orgInit['DftWangGeOrgId']
        searchPara5['searchLostEarthVo.lostEarthReason.id']= addPara1['population.lostEarthReason.id']
        searchPara5['searchLostEarthVo.nativePlaceAddress']=''
        result51=ShiYouRenKouIntf.checkShiDiJiaTingSeniorSearchList(checkpara=checkPara1,searchpara=searchPara5)
        self.assertTrue(result51, '通过失地原因高级查询失败')
        result52=ShiYouRenKouIntf.checkShiDiJiaTingSeniorSearchList(checkpara=checkPara2,searchpara=searchPara5)
        self.assertFalse(result52,'通过失地原因高级查询失败')
        Log.LogOutput( message='通过失地原因高级查询验证成功！')                           
        pass
    
    def testShiDiJiaTingImportAndDownLoad_44(self):
        """失地家庭信息 导入/导出"""
         
        importHuJiparam = copy.deepcopy(ShiYouRenKouPara.data)
        importHuJiparam['dataType']='lostEarth'
        importHuJiparam['templates']='LOSTEARTH_syncActualPopulation'
        files = {'upload': ('test.xls', open('C:/autotest_file/importShiDiJiaTing.xls', 'rb'),'applicationnd.ms-excel')}
        ret = ShiYouRenKouIntf.import_RenKou(importHuJiparam, files=files,username=userInit['DftWangGeUser'], password='11111111')         
        
        param = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        param['name'] = '失地家庭导入测试'      
        param['idCardNo'] = '111111111111186'
        ret = ShiYouRenKouIntf.check_shiDiJiaTing(param, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找失地家庭失败') 
                                
        downLoadHuJiparam = copy.deepcopy(ShiYouRenKouPara.dlZhongDianData)
        downLoadHuJiparam['organizationId']=orgInit['DftWangGeOrgId']
        response = ShiYouRenKouIntf.downLoad_shiDiJiaTing(downLoadHuJiparam, username=userInit['DftWangGeUser'], password='11111111')         
        with open("C:/autotest_file/downLoadShiDiJiaTing.xls", "wb") as code:
            code.write(response.content)
            
        ret = CommonUtil.checkExcelCellValue(param['name'], 'downLoadShiDiJiaTing.xls','失地家庭信息表', 'B4')          
        self.assertTrue(ret, '导出失败')
                         
        pass


    def testQiuZhiRenYuanAdd_17(self):
        """求职人员 新增 """
  
        qiuZhiParam_17 = copy.deepcopy(ShiYouRenKouPara.renYuanObject) 
        qiuZhiParam_17['mode']='add'
        qiuZhiParam_17['population.organization.id'] = orgInit['DftWangGeOrgId']
        qiuZhiParam_17['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人员or流动人员        
        qiuZhiParam_17['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['qiuZhiRenYuan']
        qiuZhiParam_17['population.organization.orgName'] = orgInit['DftWangGeOrg']
        qiuZhiParam_17['population.idCardNo'] = '330000199711221100'  
        qiuZhiParam_17['population.name'] = '求职人员'
        qiuZhiParam_17['population.isHaveHouse1'] = 'null'   
        qiuZhiParam_17['population.unemployedDate'] = '2015-12-05'   
        qiuZhiParam_17['population.endDateOfUnemploymentMoney'] = '2015-12-05'   
        responseDict = ShiYouRenKouIntf.add_qiuZhiRenYuan(qiuZhiDict=qiuZhiParam_17, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增求职人员失败')       
          
        bewerBungCheckParam_17 = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        bewerBungCheckParam_17['name'] = qiuZhiParam_17['population.name']       
        bewerBungCheckParam_17['idCardNo'] = qiuZhiParam_17['population.idCardNo']
        ret = ShiYouRenKouIntf.check_qiuZhiRenYuan(bewerBungCheckParam_17, orgId=qiuZhiParam_17['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找求职人员失败') 
        
        ret = ShiYouRenKouIntf.check_HuJiPopulation(bewerBungCheckParam_17, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '没有检查到户籍人口下对应的求职人员信息')
        #补充修改用例
        updPara=copy.deepcopy(qiuZhiParam_17)
        updPara['mode']='edit'
        updPara['population.id']=json.loads(responseDict.text)['id']
        updPara['population.name']='失地家庭'+createRandomString()
        updPara['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='女')
        responseDict = ShiYouRenKouIntf.add_qiuZhiRenYuan(updPara, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改求职人员失败')
        #验证修改功能
        bewerBungCheckParam_17['name']= updPara['population.name']
        ret = ShiYouRenKouIntf.check_qiuZhiRenYuan(bewerBungCheckParam_17, orgId=updPara['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '修改验证失败')
        Log.LogOutput( message='修改功能验证通过')
        #删除
        res=ShiYouRenKouIntf.delete_qiuZhiRenYuan({'populationIds':updPara['population.id']}, username = userInit['DftWangGeUser'], password = '11111111')
        self.assertTrue(res.result, '删除失败')
        #验证删除功能
        bewerBungCheckParam_17['name']= updPara['population.name']
        ret = ShiYouRenKouIntf.check_qiuZhiRenYuan(bewerBungCheckParam_17, orgId=updPara['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertFalse(ret, '删除失败')
        Log.LogOutput( message='删除验证通过')
        pass     

    def testQiuZhiRenYuanSearch_17(self):
        '''求职人员查询'''
        addPara1 = copy.deepcopy(ShiYouRenKouPara.renYuanObject) 
        addPara1['mode']='add'
        addPara1['population.organization.id'] = orgInit['DftWangGeOrgId']
        addPara1['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人员or流动人员        
        addPara1['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['qiuZhiRenYuan']
        addPara1['population.organization.orgName'] = orgInit['DftWangGeOrg']
        addPara1['population.idCardNo'] = '330000199711221101'  
        addPara1['population.name'] = '求职人员'+createRandomString()
        addPara1['population.isHaveHouse1'] = 'null'   
        addPara1['population.unemployedDate'] = '2015-12-05'   
        addPara1['population.endDateOfUnemploymentMoney'] = '2015-12-05'   
        addPara1['population.nativePlaceAddress']='户籍地详址'+createRandomString()
        addPara1['population.jobIntention']='求职意向'+createRandomString()
        addPara1['population.lastOccupation']='原职业'+createRandomString()
        addPara1['population.skill.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='技能特长', displayName='木工') #失地原因，非必填项
        responseDict = ShiYouRenKouIntf.add_qiuZhiRenYuan(qiuZhiDict=addPara1, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增求职人员失败')
        #第二条
        addPara2 = copy.deepcopy(ShiYouRenKouPara.renYuanObject) 
        addPara2['mode']='add'
        addPara2['population.organization.id'] = orgInit['DftWangGeOrgId']
        addPara2['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人员or流动人员        
        addPara2['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['qiuZhiRenYuan']
        addPara2['population.organization.orgName'] = orgInit['DftWangGeOrg']
        addPara2['population.idCardNo'] = '330000199711221102'  
        addPara2['population.name'] = '求职人员'+createRandomString()
        addPara2['population.isHaveHouse1'] = 'null'   
        addPara2['population.unemployedDate'] = '2015-12-05'   
        addPara2['population.endDateOfUnemploymentMoney'] = '2015-12-05'   
        addPara2['population.nativePlaceAddress']='户籍地详址'+createRandomString()
        addPara2['population.jobIntention']='求职意向'+createRandomString()
        addPara2['population.lastOccupation']='原职业'+createRandomString()
        addPara2['population.skill.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='技能特长', displayName='驾驶员') #失地原因，非必填项
        responseDict = ShiYouRenKouIntf.add_qiuZhiRenYuan(qiuZhiDict=addPara2, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增求职人员失败')      
        #根据姓名快速检索
        searchPara1=copy.deepcopy(ShiYouRenKouPara.fastSearch)
        searchPara1['organizationId']=orgInit['DftWangGeOrgId']
        searchPara1['searchBewerBungVo.isEmphasis']='0'
        searchPara1['searchBewerBungVo.fastSearchKeyWords']= addPara1['population.name']
        checkPara1={'name':addPara1['population.name']}
        checkPara2={'name':addPara2['population.name']}
        result11=ShiYouRenKouIntf.checkQiuZhiFastSearchList(checkpara=checkPara1,searchpara=searchPara1)
        self.assertTrue(result11, '通过姓名快速查询失败')
        result12=ShiYouRenKouIntf.checkQiuZhiFastSearchList(checkpara=checkPara2,searchpara=searchPara1)
        self.assertFalse(result12,'通过姓名快速查询失败')
        Log.LogOutput( message='通过姓名快速查询验证成功！')
        #根据身份证快速查询
        searchPara2=copy.deepcopy(searchPara1)
        searchPara2['searchBewerBungVo.fastSearchKeyWords']= addPara1['population.idCardNo']
        result21=ShiYouRenKouIntf.checkQiuZhiFastSearchList(checkpara=checkPara1,searchpara=searchPara2)
        self.assertTrue(result21, '通过身份证快速查询失败')
        result22=ShiYouRenKouIntf.checkQiuZhiFastSearchList(checkpara=checkPara2,searchpara=searchPara2)
        self.assertFalse(result22,'通过身份证快速查询失败')
        Log.LogOutput( message='通过身份证快速查询验证成功！')   
        #高级搜索,通过户籍地详址搜索  
        searchPara3=copy.deepcopy(ShiYouRenKouPara.seniorSearch)
        searchPara3['organizationId']=orgInit['DftWangGeOrgId']
        searchPara3['searchBewerBungVo.isEmphasis']='-1'
        searchPara3['searchBewerBungVo.isDeath']='-1'
        searchPara3['searchBewerBungVo.hasServiceTeamMember']='-1'
        searchPara3['searchBewerBungVo.hasServiceTeamRecord']='-1'
        searchPara3['searchBewerBungVo.nativePlaceAddress']= addPara1['population.nativePlaceAddress']
        result31=ShiYouRenKouIntf.checkQiuZhiSeniorSearchList(checkpara=checkPara1,searchpara=searchPara3)
        self.assertTrue(result31, '通过户籍地详址高级查询失败')
        result32=ShiYouRenKouIntf.checkQiuZhiSeniorSearchList(checkpara=checkPara2,searchpara=searchPara3)
        self.assertFalse(result32,'通过户籍地详址高级查询失败')
        Log.LogOutput( message='通过户籍地详址高级查询验证成功！')         
        #高级搜索,通过原职业搜索
        searchPara4=copy.deepcopy(searchPara3)
        searchPara4['organizationId']=orgInit['DftWangGeOrgId']
        searchPara4['searchBewerBungVo.lastOccupation']= addPara1['population.lastOccupation']
        searchPara4['searchBewerBungVo.nativePlaceAddress']=''
        result41=ShiYouRenKouIntf.checkQiuZhiSeniorSearchList(checkpara=checkPara1,searchpara=searchPara4)
        self.assertTrue(result41, '通过原职业高级查询失败')
        result42=ShiYouRenKouIntf.checkQiuZhiSeniorSearchList(checkpara=checkPara2,searchpara=searchPara4)
        self.assertFalse(result42,'通过原职业高级查询失败')
        Log.LogOutput( message='通过原职业高级查询验证成功！')        
        #高级搜索,通过技能特长搜索
        searchPara5=copy.deepcopy(searchPara3)
        searchPara5['organizationId']=orgInit['DftWangGeOrgId']
        searchPara5['searchBewerBungVo.skillId']= addPara1['population.skill.id']
        searchPara5['searchBewerBungVo.nativePlaceAddress']=''
        result51=ShiYouRenKouIntf.checkQiuZhiSeniorSearchList(checkpara=checkPara1,searchpara=searchPara5)
        self.assertTrue(result51, '通过技能特长高级查询失败')
        result52=ShiYouRenKouIntf.checkQiuZhiSeniorSearchList(checkpara=checkPara2,searchpara=searchPara5)
        self.assertFalse(result52,'通过技能特长高级查询失败')
        Log.LogOutput( message='通过技能特长高级查询验证成功！')                 
        pass
    
    def testQiuZhiPopulationImportAndDownLoad_45(self):
        """求职人员信息 导入/导出"""
         
        importHuJiparam = copy.deepcopy(ShiYouRenKouPara.data)
        importHuJiparam['dataType']='bewerBung'
        importHuJiparam['templates']='BEWERBUNG_syncActualPopulation'
        files = {'upload': ('test.xls', open('C:/autotest_file/importQiuZhiPopulation.xls', 'rb'),'applicationnd.ms-excel')}
        ret = ShiYouRenKouIntf.import_RenKou(importHuJiparam, files=files,username=userInit['DftWangGeUser'], password='11111111')         
        
        param = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        param['name'] = '求职人员导入测试'      
        param['idCardNo'] = '111111111111187'
        ret = ShiYouRenKouIntf.check_qiuZhiRenYuan(param, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找求职人员失败') 
                                
        downLoadHuJiparam = copy.deepcopy(ShiYouRenKouPara.dlZhongDianData)
        downLoadHuJiparam['organizationId']=orgInit['DftWangGeOrgId']
        response = ShiYouRenKouIntf.downLoad_qiuZhiRenYuan(downLoadHuJiparam, username=userInit['DftWangGeUser'], password='11111111')         
        with open("C:/autotest_file/downLoadQiuZhiPopulation.xls", "wb") as code:
            code.write(response.content)
            
        ret = CommonUtil.checkExcelCellValue(param['name'], 'downLoadQiuZhiPopulation.xls','求职人员清单', 'A4')          
        self.assertTrue(ret, '导出失败')
                         
        pass

    
    def testQingShaoNianAdd_17(self):
        """青少年 新增 """
  
        qingShaoNianParam_17 = copy.deepcopy(ShiYouRenKouPara.renYuanObject) 
        qingShaoNianParam_17['mode']='add'
        qingShaoNianParam_17['population.organization.id'] = orgInit['DftWangGeOrgId']
        qingShaoNianParam_17['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人员or流动人员        
        qingShaoNianParam_17['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['qingShaoNian']
        qingShaoNianParam_17['population.organization.orgName'] = orgInit['DftWangGeOrg']
        qingShaoNianParam_17['population.idCardNo'] = '330000199411220009' 
#         qingShaoNianParam_17['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
         
        qingShaoNianParam_17['population.name'] = '青少年'
        qingShaoNianParam_17['actualPersonType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']
        qingShaoNianParam_17['population.isHaveHouse1'] = 'null'   
#         qingShaoNianParam_17['population.birthday'] = '2015-12-05'   
        responseDict = ShiYouRenKouIntf.add_qingShaoNian(qingShaoNianParam_17, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增青少年失败')       
          
        qingShaoNianCheckParam_17 = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        qingShaoNianCheckParam_17['name'] = qingShaoNianParam_17['population.name']       
        qingShaoNianCheckParam_17['idCardNo'] = qingShaoNianParam_17['population.idCardNo']
        ret = ShiYouRenKouIntf.check_qingShaoNian(qingShaoNianCheckParam_17, orgId=qingShaoNianParam_17['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找青少年失败') 
        
        ret = ShiYouRenKouIntf.check_HuJiPopulation(qingShaoNianCheckParam_17, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '没有检查到户籍人口下对应的青少年信息')

        pass 

    def testQingShaoNianImportAndDownLoad_46(self):
        """青少年信息 导入/导出"""
         
        importHuJiparam = copy.deepcopy(ShiYouRenKouPara.data)
        importHuJiparam['dataType']='youth'
        importHuJiparam['templates']='YOUTH_syncActualPopulation'
        files = {'upload': ('test.xls', open('C:/autotest_file/importQingShaoNian.xls', 'rb'),'applicationnd.ms-excel')}
        ret = ShiYouRenKouIntf.import_RenKou(importHuJiparam, files=files,username=userInit['DftWangGeUser'], password='11111111')         
        
        param = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
        param['name'] = '青少年导入测试'      
        param['idCardNo'] = '331023199901012323'
        ret = ShiYouRenKouIntf.check_qingShaoNian(param, orgId=orgInit['DftWangGeOrgId'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找青少年失败') 
                                
        downLoadHuJiparam = copy.deepcopy(ShiYouRenKouPara.dlZhongDianData)
        downLoadHuJiparam['organizationId']=orgInit['DftWangGeOrgId']
        response = ShiYouRenKouIntf.downLoad_qingShaoNian(downLoadHuJiparam, username=userInit['DftWangGeUser'], password='11111111')         
        with open("C:/autotest_file/downLoadQingShaoNian.xls", "wb") as code:
            code.write(response.content)
            
        ret = CommonUtil.checkExcelCellValue(param['name'], 'downLoadQingShaoNian.xls','青少年清单', 'A4')          
        self.assertTrue(ret, '导出失败')
                         
        pass

      
    def tearDown(self):
        pass
    
if __name__ == "__main__":
    suite = unittest.TestSuite()
 
##实有人口    
#户籍人口
#     suite.addTest(ShiYouRenKou("testHuJiPopulationAdd_01"))
#     suite.addTest(ShiYouRenKou("testHuJiPopulationDetele_02"))
#     suite.addTest(ShiYouRenKou("testHuJiPopulationEdit_03"))
#     suite.addTest(ShiYouRenKou("testHuJiPopulationSearch_04"))
#     suite.addTest(ShiYouRenKou("testHuJiPopulationImportAndDownLoad_05"))
#     suite.addTest(ShiYouRenKou("testHuJiPopulationLogout_06"))
#     suite.addTest(ShiYouRenKou("testHuJiPopulationDeathCancel_07"))
#     suite.addTest(ShiYouRenKou("testHuJiPopulationServiceAdd_08"))
#     suite.addTest(ShiYouRenKou("testHuJiPopulationServiceDelete_08"))
#     suite.addTest(ShiYouRenKou("testHuJiPopulationServiceLeaveOrBack_08"))
#     suite.addTest(ShiYouRenKou("testHuJiPopulationGuardersAdd_08"))
#     suite.addTest(ShiYouRenKou("testHuJiPopulationGuardersDelete_08"))
#     suite.addTest(ShiYouRenKou("testHuJiPopulationGuardersEdit_08"))
#     suite.addTest(ShiYouRenKou("testHuJiPopulationServiceRecordAdd_09"))
#     suite.addTest(ShiYouRenKou("testHuJiPopulationServiceRecordEdit_09"))
#     suite.addTest(ShiYouRenKou("testHuJiPopulationServiceRecordDelete_09"))
#     suite.addTest(ShiYouRenKou("testHuJiPopulationTransfer_10"))
#     suite.addTest(ShiYouRenKou("testTransferToWangGe_13"))
#  
#流动人口
#     suite.addTest(ShiYouRenKou("testLiuDongPopulationAdd_01"))
#     suite.addTest(ShiYouRenKou("testLiuDongPopulationDelete_02"))
#     suite.addTest(ShiYouRenKou("testLiuDongPopulationTransfer_11"))
#     suite.addTest(ShiYouRenKou("testLiuDongPopulationImportAndDownLoad_26"))
#       
#未落户人口
#     suite.addTest(ShiYouRenKou("testWeiLuoHuPopulationAdd_01"))
#     suite.addTest(ShiYouRenKou("testWeiLuoHuPopulationDetele_02"))
#     suite.addTest(ShiYouRenKou("testWeiLuoHuPopulationTransfer_12"))
#     suite.addTest(ShiYouRenKou("testWeiLuoHuPopulationImportAndDownLoad_27"))
#      
#境外人口
#     suite.addTest(ShiYouRenKou("testJingWaiPopulationAdd_01"))
#     suite.addTest(ShiYouRenKou("testJingWaiPopulationDetele_02"))
#     suite.addTest(ShiYouRenKou("testJingWaiPopulationImportAndDownLoad_28"))
#  
#户籍家庭
#     suite.addTest(ShiYouRenKou("testHouseFamilyAdd_14"))
#     suite.addTest(ShiYouRenKou("testHouseFamilyDelete_14"))
#     suite.addTest(ShiYouRenKou("testHouseMemberAddRemove_15"))
#     suite.addTest(ShiYouRenKou("testHouseMemberTransfer_16"))
#     suite.addTest(ShiYouRenKou("testFamilyViewAdd_24"))
 
# #走访记录
#     suite.addTest(ShiYouRenKou("testViewDataAdd_19"))
#     suite.addTest(ShiYouRenKou("testViewDataEdit_20"))
#     suite.addTest(ShiYouRenKou("testViewDataDelete_21"))
#     suite.addTest(ShiYouRenKou("testViewDataSearch_22"))
#     suite.addTest(ShiYouRenKou("testViewDataSent_23"))
# 
# 
# ##重点人员
#刑满释放人员
#     suite.addTest(ShiYouRenKou("testXingManShiFangPopulationAdd_17"))
#     suite.addTest(ShiYouRenKou("testXingShiTransfer_25"))
#     suite.addTest(ShiYouRenKou("testXingShiSearch_17"))
#     suite.addTest(ShiYouRenKou("testXingShiPopulationImportAndDownLoad_29"))
#社区矫正人员
#     suite.addTest(ShiYouRenKou("testSheQuJiaoZhengPopulationAdd_17"))
#     suite.addTest(ShiYouRenKou("testJiaoZhengTransfer_18"))
#     suite.addTest(ShiYouRenKou("testJiaoZhengSearch_17"))
#     suite.addTest(ShiYouRenKou("testJiaoZhengPopulationImportAndDownLoad_30"))
#精神病员
#     suite.addTest(ShiYouRenKou("testJingShenBingPopulationAdd_17"))
#     suite.addTest(ShiYouRenKou("testJingShenBingSearch_17"))
#     suite.addTest(ShiYouRenKou("testJingShenBingPopulationImportAndDownLoad_31"))
#吸毒人员
#     suite.addTest(ShiYouRenKou("testXiDuPopulationAdd_17"))
#     suite.addTest(ShiYouRenKou("testXiDuSearch_17"))
#     suite.addTest(ShiYouRenKou("testXiDuPopulationImportAndDownLoad_32"))
#重点青少年
#     suite.addTest(ShiYouRenKou("testZhongDianQingShaoNianAdd_17"))
#     suite.addTest(ShiYouRenKou("testZhongDianQingShaoNianSearch_17"))
#重点上访人员
#     suite.addTest(ShiYouRenKou("testZhongDianShangFangRenYuanAdd_17"))
#     suite.addTest(ShiYouRenKou("testZhongDianShangFangSearch_17"))
#     suite.addTest(ShiYouRenKou("testShangFangPopulationImportAndDownLoad_34"))
#危险品从业人员
#     suite.addTest(ShiYouRenKou("testWeiXianPinCongYeRenYuanAdd_17"))
#     suite.addTest(ShiYouRenKou("testWeiXianPingCongYeSearch_17"))
#     suite.addTest(ShiYouRenKou("testWeiXianPopulationImportAndDownLoad_35"))
#其他人员
#     suite.addTest(ShiYouRenKou("testQiTaRenYuanAdd_17"))
#     suite.addTest(ShiYouRenKou("testQiTaRenYuanSearch_17"))
#     suite.addTest(ShiYouRenKou("testQiTaPopulationImportAndDownLoad_36"))
 
##关怀对象
#见义勇为
#     suite.addTest(ShiYouRenKou("testJianYiYongWeiAdd_17"))
#     suite.addTest(ShiYouRenKou("testJianYiYongWeiSearch_17"))
#     suite.addTest(ShiYouRenKou("testJianYiYongWeiImportAndDownLoad_37"))
#老年人
#     suite.addTest(ShiYouRenKou("testLaoNianRenAdd_17"))
#     suite.addTest(ShiYouRenKou("testLaoNianRenSearch_17"))
#     suite.addTest(ShiYouRenKou("testLaoNianRenImportAndDownLoad_38"))
#残疾人
#     suite.addTest(ShiYouRenKou("testCanJiRenAdd_17"))
#     suite.addTest(ShiYouRenKou("testCanJiRenSearch_17"))
#     suite.addTest(ShiYouRenKou("testCanJiRenImportAndDownLoad_39"))
#优抚对象
#     suite.addTest(ShiYouRenKou("testYouFuDuiXiangAdd_17"))
#     suite.addTest(ShiYouRenKou("testYouFuDuiXiangSearch_17"))
#     suite.addTest(ShiYouRenKou("testYouFuDuiXiangImportAndDownLoad_40"))
#需要救助人员
#     suite.addTest(ShiYouRenKou("testXuYaoJiuZhuRenYuanAdd_17"))
#     suite.addTest(ShiYouRenKou("testXuYaoJiuZhuRenYuanSearch_17"))
#     suite.addTest(ShiYouRenKou("testJiuZhuPopulationImportAndDownLoad_41"))
     
#失业人员
#     suite.addTest(ShiYouRenKou("testShiYeRenYuanAdd_17"))
#     suite.addTest(ShiYouRenKou("testShiYeRenYuanSearch_17"))
#     suite.addTest(ShiYouRenKou("testShiYePopulationImportAndDownLoad_42"))
#育龄妇女
#     suite.addTest(ShiYouRenKou("testYuLingFuNvAdd_17"))
#     suite.addTest(ShiYouRenKou("testYuLingFuNvSearch_17"))
#     suite.addTest(ShiYouRenKou("testYuLingFuNvImportAndDownLoad_43"))
#侨属
#     suite.addTest(ShiYouRenKou("testQiaoShuAdd_17"))
#     suite.addTest(ShiYouRenKou("testQiaoShuSearch_17"))
#失地家庭
#     suite.addTest(ShiYouRenKou("testShiDiJiaTingAdd_17"))
#     suite.addTest(ShiYouRenKou("testShiDiJiaTingSearch_17"))
#     suite.addTest(ShiYouRenKou("testShiDiJiaTingImportAndDownLoad_44"))
#求职人员
#     suite.addTest(ShiYouRenKou("testQiuZhiRenYuanAdd_17"))
#     suite.addTest(ShiYouRenKou("testQiuZhiRenYuanSearch_17"))
#     suite.addTest(ShiYouRenKou("testQiuZhiPopulationImportAndDownLoad_45"))
#青少年
#     suite.addTest(ShiYouRenKou("testQingShaoNianAdd_17"))
#     suite.addTest(ShiYouRenKou("testQingShaoNianImportAndDownLoad_46"))
  
    results = unittest.TextTestRunner().run(suite)
    pass
