# -*- coding:UTF-8 -*-

'''
Created on 2015-12-22

@author: lhz
'''
from __future__ import unicode_literals
import unittest
import copy
from COMMON import  CommonUtil,Time
from Interface.PingAnJianShe.Common import CommonIntf
from CONFIG import InitDefaultPara 
from Interface.PingAnJianShe.XiaQuGuanLi import XiaQuGuanLiPara, XiaQuGuanLiIntf
from Interface.PingAnJianShe.ShiYouRenKou import ShiYouRenKouPara,\
    ShiYouRenKouIntf
from CONFIG.InitDefaultPara import orgInit, userInit
from Interface.PingAnJianShe.SystemMgr import SystemMgrIntf
import random
    
class XiaQuGuanLi(unittest.TestCase):

    def setUp(self):
        SystemMgrIntf.initEnv()
        ''' 综治组织批量删除'''
        XiaQuGuanLiIntf.xiaQuGuanLiLeaderOraginationDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        """成员库信息批量删除 """  
        XiaQuGuanLiIntf.xiaQuGuanLiMemberDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        '''辖区队伍批量删除  '''
        XiaQuGuanLiIntf.xiaQuGuanLiLeaderDelAll(username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        ''' 服务团队批量删除'''
        XiaQuGuanLiIntf.xiaQuGuanLiTeamDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        XiaQuGuanLiIntf.deleteAllPopulation()
        pass
    
                                                                   
    # 1.验证基础信息是否能新增 成功    
    def test_xqgl_01(self):
        """辖区管理信息编辑""" 
        #新增单位信息
        editParam = copy.deepcopy(XiaQuGuanLiPara.xiaQuGuanLiEdit) 
        editParam['villageProfile.organization.id']= InitDefaultPara.orgInit['DftShengOrgId']
        editParam['villageProfile.introduction']='22'
        editParam['mode'] = 'editIntroduction'
        ret = XiaQuGuanLiIntf.editXiaQuGuanLi(issueDict=editParam,username=InitDefaultPara.userInit['DftShengUser'], password='11111111')
        self.assertTrue(ret, '辖区管理信息编辑失败')
        Time.wait(1)
        # #检查  新增的数据是否存在 
        # 复制一份儿检查项【ps：方面重新赋值使用】
        param = copy.deepcopy(XiaQuGuanLiPara.xiaQuGuanLiEdit_check)
        # 获取查询参数
        param['introduction'] = editParam['villageProfile.introduction']
        ret = XiaQuGuanLiIntf.editXiaQuGuanLi_check(paramedit=param, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, '辖区管理信息查找失败')
        
    def test_xqgl_02(self):      
        """辖区管理图片上传  """
        param = copy.deepcopy(XiaQuGuanLiPara.imageUpload)
#         param['upload'] = 'C:/autotest_file/00e93901213fb80e0eaf5c6737d12f2eb9389407.jpg'
        param['villageProfile.id'] = ''
        param['villageProfile.organization.id'] = InitDefaultPara.orgInit['DftSheQuOrgId']
        files = {'upload': ('00e93901213fb80e0eaf5c6737d12f2eb9389407.jpg', open('C:/autotest_file/00e93901213fb80e0eaf5c6737d12f2eb9389407.jpg', 'rb'),'image/jpeg')}
        ret = XiaQuGuanLiIntf.uploadImage(param=param, files=files, username=InitDefaultPara.userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(ret, '辖区管理编辑图片失败')       
 
    #辖区管理--编辑辖区领导班子介绍   
    #脚本检查点有问题，需要调整
#     def test_xqgl_03(self): 
#         #新增
#         ParamAdd = copy.deepcopy(XiaQuGuanLiPara.xiaQuGuanLiLeader)   
#         ParamAdd['mode'] = 'add'
#         ParamAdd['leaderTeams.organization.orgInternalCode'] = ''
#         ParamAdd['leaderTeams.organization.id'] = InitDefaultPara.orgInit['DftShengOrgId']
#         ParamAdd['leaderTeams.name'] = '领导班子%s' % CommonUtil.createRandomString(6)
#         ParamAdd['leaderTeams.gender'] = '1'
#         ParamAdd['leaderTeams.duty'] = '简介'
#         ret = XiaQuGuanLiIntf.xiaQuGuanLiLeaderAdd(param=ParamAdd, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')        
#         self.assertTrue(ret, '新增领导班子信息查找失败')  
#         Time.wait(1)
#         """辖区管理--编辑辖区领导班子介绍    """
#         Param = copy.deepcopy(XiaQuGuanLiPara.xiaQuGuanLiLeader)   
#         Param['mode'] = 'edit'
#         Param['leaderTeams.name'] = '领导班子%s' % CommonUtil.createRandomString(6)
#         Param['leaderTeams.id'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from leaderTeams t where t.name = '%s'" %ParamAdd['leaderTeams.name'])
#         Param['leaderTeams.organization.orgInternalCode'] = ''
#         Param['leaderTeams.organization.id'] = InitDefaultPara.orgInit['DftShengOrgId']
#         Param['leaderTeams.gender'] = '2' 
#         Param['leaderTeams.duty'] = '简介2'
#         ret = XiaQuGuanLiIntf.xiaQuGuanLiLeader(param=Param, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')        
#         self.assertTrue(ret, '编辑领导班子信息失败')        
  
    #辖区管理--新增辖区领导班子介绍   
    #脚本检查点有问题，需要调整 
#     def test_XiaQuGuanLiLeaderIntrAdd_04(self):
#         """辖区管理--新增辖区领导班子介绍    """
#         Param = copy.deepcopy(XiaQuGuanLiPara.xiaQuGuanLiLeader)   
#         Param['mode'] = 'add'
#         Param['leaderTeams.organization.orgInternalCode'] = ''
#         Param['leaderTeams.organization.id'] = InitDefaultPara.orgInit['DftShengOrgId']
#         Param['leaderTeams.name'] = '领导班子'
#         Param['leaderTeams.gender'] = '1'
#         Param['leaderTeams.duty'] = '简介'
#         ret = XiaQuGuanLiIntf.xiaQuGuanLiLeaderAdd(param=Param, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')        
#         self.assertTrue(ret, '新增领导班子信息查找失败')  

    #辖区管理--删除辖区领导班子介绍   
    #脚本检查点有问题，需要调整 
#     def test_xqgl_05(self): 
#         """辖区管理--删除辖区领导班子介绍    """
#         
#         #新增辖区领导班子
#         Param = copy.deepcopy(XiaQuGuanLiPara.xiaQuGuanLiLeader)   
#         Param['mode'] = 'add'
#         Param['leaderTeams.organization.orgInternalCode'] = ''
#         Param['leaderTeams.organization.id'] = InitDefaultPara.orgInit['DftShengOrgId']
#         Param['leaderTeams.name'] = '领导班子'
#         Param['leaderTeams.gender'] = '1'
#         Param['leaderTeams.duty'] = '简介'
#         ret = XiaQuGuanLiIntf.xiaQuGuanLiLeaderAdd(param=Param, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')        
#         self.assertTrue(ret, '新增领导班子信息查找失败')  
#         Time.wait(1)
#         delParam = copy.deepcopy(XiaQuGuanLiPara.xiaQuGuanLiDel)
#         delParam['leaderTeams.id'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from leaderTeams t where t.name = '%s'"%Param['leaderTeams.name'])
#         ret = XiaQuGuanLiIntf.xiaQuGuanLiLeaderDel(param=delParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
#         self.assertTrue(ret, '删除领导班子信息查找失败') 
        
    #辖区管理--基础信息编辑
    #脚本逻辑有问题，需要调整
#     def test_xqgl_06(self): 
#         """辖区管理--基础信息编辑    """
#         
#         Param = copy.deepcopy(XiaQuGuanLiPara.baseInformation)   
#         Param['mode'] = 'baseVillageProfile'
#         Param['villageProfile.id'] = '92'
#         Param['villageProfile.organization.id'] = InitDefaultPara.orgInit['DftSheQuOrgId']
#         Param['villageProfile.gridNum'] = '55'
#         Param['villageProfile.doors'] = '领导班000'
#         Param['villageProfile.villagers'] = '1'
#         Param['villageProfile.villageRingsters'] = '简介'
#         ret = XiaQuGuanLiIntf.xiaQuGuanLiBaseInforEdit(param=Param, username=InitDefaultPara.userInit['DftSheQuUser'], password='11111111')        
#         self.assertTrue(ret, '基础信息编辑查找失败') 
        
         

    #辖区管理--组织机构--综治组织新增
    def test_xqgl_07(self): 
        """辖区管理--组织机构--综治组织新增    """
        Param = copy.deepcopy(XiaQuGuanLiPara.oragnizationAddParam)   
        Param['mode'] = 'add'
        Param['primaryOrg.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        Param['primaryOrg.teamClass.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='组织大类', displayName='综治组织')
        Param['primaryOrg.org.orgName'] = '测试自动化省->测试自动化市->测试自动化区->测试自动化街道->测试自动化社区->测试自动化网格'    
        Param['primaryOrg.teamType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='基层综治组织类型', displayName='综治委')
        Param['primaryOrg.name'] = InitDefaultPara.orgInit['DftWangGeOrg']+'综治组织'
        Param['primaryOrg.detailName'] = 'dddfd'
        Param['primaryOrg.remark'] = '天阙科技000%s' % CommonUtil.createRandomString(6) 
        Param['primaryOrg.detailName'] = '111' 
 
        ret = XiaQuGuanLiIntf.xiaQuGuanLiLeaderOraginationAdd(param=Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        self.assertTrue(ret, '综治组织新增失败')    
        Time.wait(1)
        #检查点
        ParamCheck = copy.deepcopy(XiaQuGuanLiPara.oragnizationAddParam_check) 
        ParamCheck['detailName'] =  Param['primaryOrg.detailName']             
        ret = XiaQuGuanLiIntf.checkxiaQuGuanLiLeaderOragination(param=ParamCheck, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        self.assertTrue(ret, '综治组织新增检查失败')   
          
          
    #辖区管理--组织机构--综治组织修改
    def test_xqgl_08(self): 
        """辖区管理--组织机构--综治组织修改    """
        ParamAdd = copy.deepcopy(XiaQuGuanLiPara.oragnizationAddParam)   
        ParamAdd['mode'] = 'add'
        ParamAdd['primaryOrg.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        ParamAdd['primaryOrg.teamClass.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='组织大类', displayName='综治组织')
        ParamAdd['primaryOrg.org.orgName'] = '测试自动化省->测试自动化市->测试自动化区->测试自动化街道->测试自动化社区->测试自动化网格'    
        ParamAdd['primaryOrg.teamType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='基层综治组织类型', displayName='综治办')
        ParamAdd['primaryOrg.name'] = InitDefaultPara.orgInit['DftWangGeOrg']+'综治组织'
        ParamAdd['primaryOrg.detailName'] = '天阙科技05%s' % CommonUtil.createRandomString(6)
 
        ret = XiaQuGuanLiIntf.xiaQuGuanLiLeaderOraginationAdd(param=ParamAdd, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        self.assertTrue(ret, '综治组织新增失败') 
        Time.wait(1)
        Param = copy.deepcopy(XiaQuGuanLiPara.oragnizationAddParam)   
        Param['mode'] = 'edit'
        Param['primaryOrg.id'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from primaryorganizations t where t.detailname = '%s'"%ParamAdd['primaryOrg.detailName'])
        Param['primaryOrg.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        Param['primaryOrg.teamClass.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='组织大类', displayName='综治组织')
        #Param['primaryOrg.org.orgName'] = '测试自动化省->测试自动化市->测试自动化区->测试自动化街道->测试自动化社区->测试自动化网格'    
        Param['primaryOrg.teamType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='基层综治组织类型', displayName='综治委')
        Param['primaryOrg.name'] = InitDefaultPara.orgInit['DftWangGeOrg']+'综治组织'
        Param['primaryOrg.detailName'] = '天阙科技%s' % CommonUtil.createRandomString(6)
        Param['primaryOrg.remark'] = '5654'  
  
        ret = XiaQuGuanLiIntf.xiaQuGuanLiLeaderOraginationEdit(param=Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        self.assertTrue(ret, '综治组织修改失败')         
        Time.wait(1)
        #检查点
        ParamCheck = copy.deepcopy(XiaQuGuanLiPara.oragnizationAddParam_check) 
        ParamCheck['detailName'] =  Param['primaryOrg.detailName']             
        ret = XiaQuGuanLiIntf.checkxiaQuGuanLiLeaderOragination(param=ParamCheck, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        self.assertTrue(ret, '综治组织修改检查失败')  
           
           
    #辖区管理--组织机构--综治组织删除
    def test_xqgl_09(self): 
        """辖区管理--组织机构--综治组织删除    """
        
        #新增
        Param = copy.deepcopy(XiaQuGuanLiPara.oragnizationAddParam)   
        Param['mode'] = 'add'
        Param['primaryOrg.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        Param['primaryOrg.teamClass.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='组织大类', displayName='综治组织')
        Param['primaryOrg.org.orgName'] = '测试自动化省->测试自动化市->测试自动化区->测试自动化街道->测试自动化社区->测试自动化网格'    
        Param['primaryOrg.teamType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='基层综治组织类型', displayName='综治委')
        Param['primaryOrg.name'] = InitDefaultPara.orgInit['DftWangGeOrg']+'综治组织'
        Param['primaryOrg.detailName'] = 'dddfd'
        Param['primaryOrg.remark'] = '222'
        Param['primaryOrg.detailName'] = '天阙科技000%s' % CommonUtil.createRandomString(6) 
 
        ret = XiaQuGuanLiIntf.xiaQuGuanLiLeaderOraginationAdd(param=Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        self.assertTrue(ret, '综治组织新增失败')   
        Time.wait(1)
        ParamDel = copy.deepcopy(XiaQuGuanLiPara.oragnizationDelete) 
        ParamDel['mode'] = 'delete'
        ParamDel['selectedIds'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from primaryorganizations t where t.detailname = '%s'"%Param['primaryOrg.detailName'])
        
        ret = XiaQuGuanLiIntf.xiaQuGuanLiLeaderOraginationDel(param=ParamDel, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
#         self.assertTrue(ret, '综治组织删除失败')     
        Time.wait(1)
        #检查点
        ret = XiaQuGuanLiIntf.search_check(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        self.assertTrue(ret, '综治组织删除检查失败')  
                 
    #批量删除
    def test_xqgl_10(self):  
        """综治组织信息批量删除 """ 
        XiaQuGuanLiIntf.xiaQuGuanLiLeaderOraginationDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111') 
        ##检查点
        ret = XiaQuGuanLiIntf.search_check(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111') 
        self.assertTrue(ret, '综治组织删除检查失败')             
       
    def test_xqgl_11(self): 
        """辖区管理--组织机构--综治组织导出    """
        
        Param = copy.deepcopy(XiaQuGuanLiPara.oragnizationAddParam)   
        Param['mode'] = 'add'
        Param['primaryOrg.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        Param['primaryOrg.teamClass.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='组织大类', displayName='综治组织')
        Param['primaryOrg.org.orgName'] = '测试自动化省->测试自动化市->测试自动化区->测试自动化街道->测试自动化社区->测试自动化网格'    
        Param['primaryOrg.teamType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='基层综治组织类型', displayName='综治委')
        Param['primaryOrg.name'] = InitDefaultPara.orgInit['DftWangGeOrg']+'综治组织'
        Param['primaryOrg.detailName'] = 'dddfd'
        Param['primaryOrg.remark'] = '天阙科技000%s' % CommonUtil.createRandomString(6) 
        Param['primaryOrg.detailName'] = '111' 
 
        ret = XiaQuGuanLiIntf.xiaQuGuanLiLeaderOraginationAdd(param=Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        self.assertTrue(ret, '综治组织新增失败')    
        Time.wait(1)
        downLoadCompany = copy.deepcopy(XiaQuGuanLiPara.oragnizationExport)
        downLoadCompany['primaryOrgVo.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        downLoadCompany['primaryOrgVo.displayLevel'] = 'allJurisdiction'
        downLoadCompany['primaryOrgVo.teamClass.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='组织大类', displayName='综治组织')
        downLoadCompany['primaryOrgVo.teamClass.internalId'] = 0
        downLoadCompany['primaryOrgVo.teamClass.displayName']='综治组织'
        ret = XiaQuGuanLiIntf.exportData(downLoadCompany, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111'); 
        with open("C:/autotest_file/organization .xls", "wb") as code:
            code.write(ret.content)
        pass 
        #检查点
        ret=CommonUtil.checkExcelCellValue(Param['primaryOrg.detailName'],"organization .xls" , "组织机构", "B4")
        self.assertTrue(ret, '综治组织导出检查失败')  
         
    def test_xqgl_12(self): 
        """辖区管理--组织机构--成员库新增    """
        #新增
        Param = copy.deepcopy(XiaQuGuanLiPara.personParam)   
        Param['serviceTeamMemberBase.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        Param['serviceTeamMemberBase.name'] = '成员库%s' % CommonUtil.createRandomString(6) 
        Param['serviceTeamMemberBase.gender.id'] =  CommonIntf.getIdByDomainAndDisplayName(domainName='性别(男、女)', displayName='男') 
        Param['serviceTeamMemberBase.mobile'] = random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8))
        Param['positionInTeam'] = ''
        Param['isSubmit'] = 'true' 
        
        ret = XiaQuGuanLiIntf.memberAdd(param=Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        self.assertTrue(ret, '成员库新增失败') 
        Time.wait(1) 
        #检查点
        ParamCheck = copy.deepcopy(XiaQuGuanLiPara.personCheck)
        ParamCheck['name'] = Param['serviceTeamMemberBase.name']
        ret = XiaQuGuanLiIntf.checkPersonList(param=ParamCheck, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        self.assertTrue(ret, '成员库新增检查失败') 
        Time.wait(1)
        pass
    def test_xqgl_13(self): 
        """辖区管理--组织机构--成员库修改    """
        #新增
        Param = copy.deepcopy(XiaQuGuanLiPara.personParam)   
        Param['serviceTeamMemberBase.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        Param['serviceTeamMemberBase.name'] = '服务%s' % CommonUtil.createRandomString(6) 
        Param['serviceTeamMemberBase.gender.id'] =  CommonIntf.getIdByDomainAndDisplayName(domainName='性别(男、女)', displayName='男') 
        Param['serviceTeamMemberBase.mobile'] = random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8))
        Param['isSubmit'] = 'true' 
        
        ret = XiaQuGuanLiIntf.memberAdd(param=Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        self.assertTrue(ret, '成员库新增失败') 
        Time.wait(1) 
        #修改
        ParamEdit = copy.deepcopy(XiaQuGuanLiPara.personParam)   
        ParamEdit['serviceTeamMemberBase.id'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from SERVICETEAMMEMBERBASE t  where t.name ='%s'"%Param['serviceTeamMemberBase.name'])
        ParamEdit['serviceTeamMemberBase.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        ParamEdit['serviceTeamMemberBase.name'] = '服务%s' % CommonUtil.createRandomString(6) 
        ParamEdit['serviceTeamMemberBase.gender.id'] =  CommonIntf.getIdByDomainAndDisplayName(domainName='性别(男、女)', displayName='男') 
        ParamEdit['serviceTeamMemberBase.mobile'] = random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8))
        ParamEdit['isSubmit'] = 'true'        
        
        ret = XiaQuGuanLiIntf.memberEdit(param=ParamEdit, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        self.assertTrue(ret, '成员库修改失败')  
        Time.wait(1)
        #检查点
        ParamCheck = copy.deepcopy(XiaQuGuanLiPara.personCheck)
        ParamCheck['name'] = ParamEdit['serviceTeamMemberBase.name']
        ret = XiaQuGuanLiIntf.checkPersonList(param=ParamCheck, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        self.assertTrue(ret, '成员库修改检查失败') 
                
    def test_xqgl_14(self):  
        """辖区管理--组织机构--成员库删除     """        
        #新增
        Param = copy.deepcopy(XiaQuGuanLiPara.personParam)   
        Param['serviceTeamMemberBase.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        Param['serviceTeamMemberBase.name'] = '服务%s' % CommonUtil.createRandomString(6) 
        Param['serviceTeamMemberBase.gender.id'] =  CommonIntf.getIdByDomainAndDisplayName(domainName='性别(男、女)', displayName='男') 
        Param['serviceTeamMemberBase.mobile'] = random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8))
        Param['isSubmit'] = 'true' 
        
        ret = XiaQuGuanLiIntf.memberAdd(param=Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        self.assertTrue(ret, '成员库新增失败')  
        Time.wait(1)
        ParamDel = copy.deepcopy(XiaQuGuanLiPara.personDel) 
        ParamDel['selectedIds'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from SERVICETEAMMEMBERBASE t  where t.name ='%s'"%Param['serviceTeamMemberBase.name'])
        ParamDel['mode'] = 'delete'        
        ret = XiaQuGuanLiIntf.memberDel(param=ParamDel, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
#         self.assertTrue(ret, '成员库删除失败')                
        Time.wait(1)
        #检查点
        ParamCheck = copy.deepcopy(XiaQuGuanLiPara.personCheck)
        ParamCheck['name'] = Param['serviceTeamMemberBase.name']
        ret = XiaQuGuanLiIntf.checkPersonList(param=ParamCheck, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        self.assertFalse(ret, '成员库删除检查失败') 
        
    def test_xqgl_15(self): 
        """成员库信息批量删除 """    
        XiaQuGuanLiIntf.xiaQuGuanLiMemberDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111') 
           
        #检查点
        ret = XiaQuGuanLiIntf.search_memberCheck(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        self.assertTrue(ret, '成员库批量删除检查失败')          
        
    def test_xqgl_16(self): 
        '''综治组织维护成员 '''
        #新增
        Param = copy.deepcopy(XiaQuGuanLiPara.oragnizationAddParam)   
        Param['mode'] = 'add'
        Param['primaryOrg.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        Param['primaryOrg.teamClass.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='组织大类', displayName='综治组织')
        Param['primaryOrg.org.orgName'] = '测试自动化省->测试自动化市->测试自动化区->测试自动化街道->测试自动化社区->测试自动化网格'    
        Param['primaryOrg.teamType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='基层综治组织类型', displayName='综治委')
        Param['primaryOrg.name'] = InitDefaultPara.orgInit['DftWangGeOrg']+'综治组织'
        Param['primaryOrg.detailName'] = 'dddfd'
        Param['primaryOrg.remark'] = '222'
        Param['primaryOrg.detailName'] = '天阙科技000%s' % CommonUtil.createRandomString(6) 
 
        ret = XiaQuGuanLiIntf.xiaQuGuanLiLeaderOraginationAdd(param=Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        self.assertTrue(ret, '综治组织新增失败')  
        Time.wait(1)
        #成员库新增
        ParamMember = copy.deepcopy(XiaQuGuanLiPara.personParam)   
        ParamMember['serviceTeamMemberBase.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        ParamMember['serviceTeamMemberBase.name'] = '服务%s' % CommonUtil.createRandomString(6) 
        ParamMember['serviceTeamMemberBase.gender.id'] =  CommonIntf.getIdByDomainAndDisplayName(domainName='性别(男、女)', displayName='男') 
        ParamMember['serviceTeamMemberBase.mobile'] = random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8))
        ParamMember['isSubmit'] = 'true' 
        
        ret = XiaQuGuanLiIntf.memberAdd(param=ParamMember, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        self.assertTrue(ret, '成员库新增失败')      
        Time.wait(1)
        
        ParamAdd = copy.deepcopy(XiaQuGuanLiPara.memberAdd) 
        ParamAdd['serviceTeamMember.baseId']= CommonIntf.getDbQueryResult(dbCommand="select t.id from SERVICETEAMMEMBERBASE t  where t.name ='%s'"%ParamMember['serviceTeamMemberBase.name'])
        ParamAdd['serviceTeamMember.teamId']= CommonIntf.getDbQueryResult(dbCommand="select t.id from primaryorganizations t where t.detailname = '%s'"%Param['primaryOrg.detailName'])
        ParamAdd['serviceTeamMember.isTeam']= '1'
        ParamAdd['serviceTeamMember.position.id']= CommonIntf.getIdByDomainAndDisplayName(domainName='综治组织职务', displayName='主任')
        ParamAdd['serviceTeamMember.onDuty']= '1'
        
        ret = XiaQuGuanLiIntf.search_memberOrg(param=ParamAdd, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        self.assertTrue(ret, '综治组织维护成员失败')         
        Time.wait(1)
        #检查点
        ret = XiaQuGuanLiIntf.checkxiaQuGuanLiLeaderOraginationMember(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        self.assertTrue(ret, '综治组织维护成员检查失败')         
            
    def test_xqgl_17(self): 
        '''综治组织维护成员移除成员 '''
        #新增
        Param = copy.deepcopy(XiaQuGuanLiPara.oragnizationAddParam)   
        Param['mode'] = 'add'
        Param['primaryOrg.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        Param['primaryOrg.teamClass.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='组织大类', displayName='综治组织')
        Param['primaryOrg.org.orgName'] = '测试自动化省->测试自动化市->测试自动化区->测试自动化街道->测试自动化社区->测试自动化网格'    
        Param['primaryOrg.teamType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='基层综治组织类型', displayName='综治委')
        Param['primaryOrg.name'] = InitDefaultPara.orgInit['DftWangGeOrg']+'综治组织'
        Param['primaryOrg.detailName'] = 'dddfd'
        Param['primaryOrg.remark'] = '222'
        Param['primaryOrg.detailName'] = '天阙科技000%s' % CommonUtil.createRandomString(6) 
 
        ret = XiaQuGuanLiIntf.xiaQuGuanLiLeaderOraginationAdd(param=Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        self.assertTrue(ret, '综治组织新增失败')  
        Time.wait(1)
        #成员库新增
        ParamMember = copy.deepcopy(XiaQuGuanLiPara.personParam)   
        ParamMember['serviceTeamMemberBase.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        ParamMember['serviceTeamMemberBase.name'] = '服务%s' % CommonUtil.createRandomString(6) 
        ParamMember['serviceTeamMemberBase.gender.id'] =  CommonIntf.getIdByDomainAndDisplayName(domainName='性别(男、女)', displayName='男') 
        ParamMember['serviceTeamMemberBase.mobile'] = random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8))
        ParamMember['isSubmit'] = 'true' 
        ret = XiaQuGuanLiIntf.memberAdd(param=ParamMember, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        self.assertTrue(ret, '成员库新增失败')      
        Time.wait(1)
        
        ParamAdd = copy.deepcopy(XiaQuGuanLiPara.memberAdd) 
        ParamAdd['serviceTeamMember.baseId']= CommonIntf.getDbQueryResult(dbCommand="select t.id from SERVICETEAMMEMBERBASE t  where t.name ='%s'"%ParamMember['serviceTeamMemberBase.name'])
        ParamAdd['serviceTeamMember.teamId']= CommonIntf.getDbQueryResult(dbCommand="select t.id from primaryorganizations t where t.detailname ='%s'"%Param['primaryOrg.detailName'])
        ParamAdd['serviceTeamMember.isTeam']= '1'
        ParamAdd['serviceTeamMember.position.id']= CommonIntf.getIdByDomainAndDisplayName(domainName='综治组织职务', displayName='主任')
        ParamAdd['serviceTeamMember.onDuty']= '1'
        ret = XiaQuGuanLiIntf.search_memberOrg(param=ParamAdd, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        self.assertTrue(ret, '综治组织维护成员失败') 
        Time.wait(1)
        ParamRemove = copy.deepcopy(XiaQuGuanLiPara.memberRemove) 
        ParamRemove['serviceTeamMemberVo.baseId'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from SERVICETEAMMEMBERBASE t  where t.name ='%s' "%ParamMember['serviceTeamMemberBase.name'])
        ParamRemove['serviceTeamMemberVo.teamId'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from primaryorganizations t where t.detailname = '%s' "%Param['primaryOrg.detailName'])
        ParamRemove['serviceTeamMemberVo.isTeam'] = 1
        ret = XiaQuGuanLiIntf.remove_memberOrg(param = ParamRemove,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')  
        self.assertTrue(ret, '综治组织维护成员移除失败')
        Time.wait(1)       
        
        #检查点
        ret = XiaQuGuanLiIntf.checkRemoveMember(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        self.assertTrue(ret, '综治组织移除成员检查失败')            
                       
        
    def test_xqgl_18(self): 
        '''综治组织维护成员离职 '''
        #新增综治组织
        Param = copy.deepcopy(XiaQuGuanLiPara.oragnizationAddParam)   
        Param['mode'] = 'add'
        Param['primaryOrg.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        Param['primaryOrg.teamClass.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='组织大类', displayName='综治组织')
        Param['primaryOrg.org.orgName'] = '测试自动化省->测试自动化市->测试自动化区->测试自动化街道->测试自动化社区->测试自动化网格'    
        Param['primaryOrg.teamType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='基层综治组织类型', displayName='综治委')
        Param['primaryOrg.name'] = InitDefaultPara.orgInit['DftWangGeOrg']+'综治组织'
        Param['primaryOrg.detailName'] = 'dddfd'
        Param['primaryOrg.remark'] = '222'
        Param['primaryOrg.detailName'] = '天阙科技000%s' % CommonUtil.createRandomString(6) 
        ret = XiaQuGuanLiIntf.xiaQuGuanLiLeaderOraginationAdd(param=Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        self.assertTrue(ret, '综治组织新增失败')  
        Time.wait(1)
        #可选成员库新增
        ParamMember = copy.deepcopy(XiaQuGuanLiPara.personParam)   
        ParamMember['serviceTeamMemberBase.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        ParamMember['serviceTeamMemberBase.name'] = '服务%s' % CommonUtil.createRandomString(6) 
        ParamMember['serviceTeamMemberBase.gender.id'] =  CommonIntf.getIdByDomainAndDisplayName(domainName='性别(男、女)', displayName='男') 
        ParamMember['serviceTeamMemberBase.mobile'] = random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8))
        ParamMember['isSubmit'] = 'true' 
        ret = XiaQuGuanLiIntf.memberAdd(param=ParamMember, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        self.assertTrue(ret, '成员库新增失败')      
        Time.wait(1)
        #添加成员
        ParamAdd = copy.deepcopy(XiaQuGuanLiPara.memberAdd) 
        ParamAdd['serviceTeamMember.baseId']= CommonIntf.getDbQueryResult(dbCommand="select t.id from SERVICETEAMMEMBERBASE t  where t.name ='%s' " %ParamMember['serviceTeamMemberBase.name'])
        ParamAdd['serviceTeamMember.teamId']= CommonIntf.getDbQueryResult(dbCommand="select t.id from primaryorganizations t where t.detailname = '%s' " % Param['primaryOrg.detailName'])
        ParamAdd['serviceTeamMember.isTeam']= '1'
        ParamAdd['serviceTeamMember.position.id']= CommonIntf.getIdByDomainAndDisplayName(domainName='综治组织职务', displayName='主任')
        ParamAdd['serviceTeamMember.onDuty']= '1'
        ret = XiaQuGuanLiIntf.search_memberOrg(param=ParamAdd, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        self.assertTrue(ret, '综治组织维护成员失败') 
        Time.wait(1)
        #离职
        ParamliZhi = copy.deepcopy(XiaQuGuanLiPara.danRenZhiWei) 
        ParamliZhi['count'] = 0 
        ParamliZhi['serviceTeamMemberVo.memberId'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from SERVICETEAMMEMBERBASE t  where t.name ='%s' " % ParamMember['serviceTeamMemberBase.name'])
        ParamliZhi['serviceTeamMemberVo.onDuty'] = 0
        ParamliZhi['serviceTeamMemberVo.isTeam'] = 1
        ParamliZhi['serviceTeamMemberVo.teamId'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from primaryorganizations t where t.detailname = '%s' "%Param['primaryOrg.detailName'])
        ret = XiaQuGuanLiIntf.memberLiZhi(param=ParamliZhi, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
#         self.assertTrue(ret, '综治组织维护成员离职失败')        
        #检查点
        ret = XiaQuGuanLiIntf.checkRemoveMember(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        self.assertTrue(ret, '综治组织离职成员失败')  
        
        
        
    def test_xqgl_19(self): 
        '''综治组织维护成员重新担任 '''
        #新增综治组织
        Param = copy.deepcopy(XiaQuGuanLiPara.oragnizationAddParam)   
        Param['mode'] = 'add'
        Param['primaryOrg.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        Param['primaryOrg.teamClass.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='组织大类', displayName='综治组织')
        Param['primaryOrg.org.orgName'] = '测试自动化省->测试自动化市->测试自动化区->测试自动化街道->测试自动化社区->测试自动化网格'    
        Param['primaryOrg.teamType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='基层综治组织类型', displayName='综治委')
        Param['primaryOrg.name'] = InitDefaultPara.orgInit['DftWangGeOrg']+'综治组织'
        Param['primaryOrg.detailName'] = 'dddfd'
        Param['primaryOrg.remark'] = '222'
        Param['primaryOrg.detailName'] = '天阙科技000%s' % CommonUtil.createRandomString(6) 
        ret = XiaQuGuanLiIntf.xiaQuGuanLiLeaderOraginationAdd(param=Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        self.assertTrue(ret, '综治组织新增失败')  
        Time.wait(1)
        #可选成员库新增
        ParamMember = copy.deepcopy(XiaQuGuanLiPara.personParam)   
        ParamMember['serviceTeamMemberBase.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        ParamMember['serviceTeamMemberBase.name'] = '服务%s' % CommonUtil.createRandomString(6) 
        ParamMember['serviceTeamMemberBase.gender.id'] =  CommonIntf.getIdByDomainAndDisplayName(domainName='性别(男、女)', displayName='男') 
        ParamMember['serviceTeamMemberBase.mobile'] = random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8))
        ParamMember['isSubmit'] = 'true' 
        ret = XiaQuGuanLiIntf.memberAdd(param=ParamMember, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        self.assertTrue(ret, '成员库新增失败')      
        Time.wait(1)
        #添加成员
        ParamAdd = copy.deepcopy(XiaQuGuanLiPara.memberAdd) 
        ParamAdd['serviceTeamMember.baseId']= CommonIntf.getDbQueryResult(dbCommand="select t.id from SERVICETEAMMEMBERBASE t  where t.name ='%s'"%ParamMember['serviceTeamMemberBase.name'])
        ParamAdd['serviceTeamMember.teamId']= CommonIntf.getDbQueryResult(dbCommand="select t.id from primaryorganizations t where t.detailname = '%s'"%Param['primaryOrg.detailName'])
        ParamAdd['serviceTeamMember.isTeam']= '1'
        ParamAdd['serviceTeamMember.position.id']= CommonIntf.getIdByDomainAndDisplayName(domainName='综治组织职务', displayName='主任')
        ParamAdd['serviceTeamMember.onDuty']= '1'
        ret = XiaQuGuanLiIntf.search_memberOrg(param=ParamAdd, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        self.assertTrue(ret, '综治组织维护成员失败') 
        Time.wait(1)
        #离职
        ParamliZhi = copy.deepcopy(XiaQuGuanLiPara.danRenZhiWei) 
        ParamliZhi['count'] = 0 
        ParamliZhi['serviceTeamMemberVo.memberId'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from SERVICETEAMMEMBERBASE t  where t.name ='%s'"%ParamMember['serviceTeamMemberBase.name'])
        ParamliZhi['serviceTeamMemberVo.onDuty'] = 0
        ParamliZhi['serviceTeamMemberVo.isTeam'] = 1
        ParamliZhi['serviceTeamMemberVo.teamId'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from primaryorganizations t where t.detailname = '%s'"%Param['primaryOrg.detailName'])
        ret = XiaQuGuanLiIntf.memberLiZhi(param=ParamliZhi, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
#         self.assertTrue(ret, '综治组织维护成员离职失败')   
        Time.wait(1)
        #重新担任
        ParamliZhi = copy.deepcopy(XiaQuGuanLiPara.danRenZhiWei) 
        ParamliZhi['count'] = 0 
        ParamliZhi['serviceTeamMemberVo.memberId'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from SERVICETEAMMEMBERBASE t  where t.name ='%s'"%ParamMember['serviceTeamMemberBase.name'])
        ParamliZhi['serviceTeamMemberVo.onDuty'] = 1
        ParamliZhi['serviceTeamMemberVo.isTeam'] = 1
        ParamliZhi['serviceTeamMemberVo.teamId'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from primaryorganizations t where t.detailname = '%s'"%Param['primaryOrg.detailName'])
        ret = XiaQuGuanLiIntf.memberCXDR(param=ParamliZhi, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
#         self.assertTrue(ret, '综治组织维护成员重新担任失败') 
        Time.wait(1)
        #检查点
        ret = XiaQuGuanLiIntf.checkRemoveMember(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        self.assertFalse(ret, '综治组织离职成员失败') 
        
    def test_xqgl_20(self): 
        ''' 辖区队伍导出'''   
        #新增辖区队伍
        ParamAdd = copy.deepcopy(XiaQuGuanLiPara.xiaQuGuanLiLeader)   
        ParamAdd['mode'] = 'add'
        ParamAdd['leaderTeams.organization.orgInternalCode'] = ''
        ParamAdd['leaderTeams.organization.id'] = InitDefaultPara.orgInit['DftShiOrgId']
        ParamAdd['leaderTeams.name'] = '领导班子%s' % CommonUtil.createRandomString(6)
        ParamAdd['leaderTeams.gender'] = '1'
        ParamAdd['leaderTeams.duty'] = '简介'
        ret = XiaQuGuanLiIntf.xiaQuGuanLiLeaderAdd(param=ParamAdd, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')        
        self.assertTrue(ret, '新增领导班子信息查找失败')  
        Time.wait(1)
        Param = copy.deepcopy(XiaQuGuanLiPara.export_xqdw)  
        Param['leaderTeamsVo.organization.id'] =  InitDefaultPara.orgInit['DftShiOrgId']   
        Param['organization.id'] = InitDefaultPara.orgInit['DftShiOrgId'] 
        ret = XiaQuGuanLiIntf.exportXqDW(param=Param, username=InitDefaultPara.userInit['DftShiUser'], password='11111111') 
        with open("C:/autotest_file/xiaquduiwu.xls", "wb") as code:
            code.write(ret.content)
        pass 
          
        
    def test_xqgl_21(self):   
        '''组织机构--服务团队 新增'''   
        #新增
        Param = copy.deepcopy(XiaQuGuanLiPara.addTeam)
        Param['mode'] = 'add'
        Param['isSubmit'] = 'true'
        Param['serviceTeam.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        Param['serviceTeam.org.orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        Param['serviceTeam.teamType.id'] =  CommonIntf.getIdByDomainAndDisplayName(domainName='服务团队类型-插件', displayName='安全建设')
        Param['serviceTeam.teamName'] = '服务团队%s' % CommonUtil.createRandomString(6)
        Param['serviceTeam.buildDate'] = Time.getCurrentDate()
        Param['serviceTeam.remark'] = '8'
        
        ret = XiaQuGuanLiIntf.addTeam(param=Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        self.assertTrue(ret, '新增服务团队信息失败')  
        Time.wait(1)
        #检查点
        ParamName = copy.deepcopy(XiaQuGuanLiPara.checkTeamName)
        ParamName['teamName'] = Param['serviceTeam.teamName']
        
        ret = XiaQuGuanLiIntf.teamList(param=ParamName, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        self.assertTrue(ret, '服务团队信息检查失败') 
               
    def test_xqgl_22(self):   
        '''组织机构--服务团队 修改'''   
        #新增
        Param = copy.deepcopy(XiaQuGuanLiPara.addTeam)
        Param['mode'] = 'add'
        Param['isSubmit'] = 'true'
        Param['serviceTeam.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        Param['serviceTeam.org.orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        Param['serviceTeam.teamType.id'] =  CommonIntf.getIdByDomainAndDisplayName(domainName='服务团队类型-插件', displayName='安全建设')
        Param['serviceTeam.teamName'] = '服务团队%s' % CommonUtil.createRandomString(6)
        Param['serviceTeam.buildDate'] = Time.getCurrentDate()
        Param['serviceTeam.remark'] = '8'
        
        ret = XiaQuGuanLiIntf.addTeam(param=Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        self.assertTrue(ret, '新增服务团队信息失败')  
        Time.wait(1)
        #修改
        ParamEdit = copy.deepcopy(XiaQuGuanLiPara.addTeam)
        ParamEdit['mode'] = 'edit'
        ParamEdit['serviceTeam.id'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from serviceTeams t  where t.name ='%s'"% Param['serviceTeam.teamName'])
        ParamEdit['serviceTeam.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        ParamEdit['serviceTeam.org.orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        ParamEdit['serviceTeam.teamType.id'] =  CommonIntf.getIdByDomainAndDisplayName(domainName='服务团队类型-插件', displayName='矛盾调解')
        ParamEdit['serviceTeam.teamName'] = '服务团队%s' % CommonUtil.createRandomString(6)
        ParamEdit['serviceTeam.buildDate'] = Time.getCurrentDate()
        ParamEdit['serviceTeam.remark'] = '8'
        
        ret = XiaQuGuanLiIntf.editTeam(param=ParamEdit, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        self.assertTrue(ret, '修改服务团队信息失败')  
        Time.wait(1)
        #检查点
        ParamName = copy.deepcopy(XiaQuGuanLiPara.checkTeamName)
        ParamName['teamName'] = ParamEdit['serviceTeam.teamName']
         
        ret = XiaQuGuanLiIntf.teamList(param=ParamName, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        self.assertTrue(ret, '服务团队信息检查失败')         
    
    
    def test_xqgl_23(self):   
        '''组织机构--服务团队 删除'''   
        #新增
        Param = copy.deepcopy(XiaQuGuanLiPara.addTeam)
        Param['mode'] = 'add'
        Param['isSubmit'] = 'true'
        Param['serviceTeam.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        Param['serviceTeam.org.orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        Param['serviceTeam.teamType.id'] =  CommonIntf.getIdByDomainAndDisplayName(domainName='服务团队类型-插件', displayName='安全建设')
        Param['serviceTeam.teamName'] = '服务团队%s' % CommonUtil.createRandomString(6)
        Param['serviceTeam.buildDate'] = Time.getCurrentDate()
        Param['serviceTeam.remark'] = '8'
        
        ret = XiaQuGuanLiIntf.addTeam(param=Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        self.assertTrue(ret, '新增服务团队信息失败') 
        Time.wait(1)  
        ParamDelete = copy.deepcopy(XiaQuGuanLiPara.deleteTeam) 
        ParamDelete['mode'] = 'delete' 
        ParamDelete['selectedIds'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from serviceTeams t  where t.name ='%s'"% Param['serviceTeam.teamName'])     
         
        ret = XiaQuGuanLiIntf.remove_team(param=ParamDelete, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
#         self.assertTrue(ret, '删除服务团队信息失败') 
        Time.wait(1)
        #检查点
        ret = XiaQuGuanLiIntf.checkTeamrem(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        self.assertTrue(ret, '服务团队信息检查失败') 
      
    def test_xqgl_24(self):   
        '''组织机构--服务团队 导出'''   
        #新增
        Param = copy.deepcopy(XiaQuGuanLiPara.addTeam)
        Param['mode'] = 'add'
        Param['isSubmit'] = 'true'
        Param['serviceTeam.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        Param['serviceTeam.org.orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        Param['serviceTeam.teamType.id'] =  CommonIntf.getIdByDomainAndDisplayName(domainName='服务团队类型-插件', displayName='安全建设')
        Param['serviceTeam.teamName'] = '服务团队%s' % CommonUtil.createRandomString(6)
        Param['serviceTeam.buildDate'] = Time.getCurrentDate()
        Param['serviceTeam.remark'] = '8'
        
        ret = XiaQuGuanLiIntf.addTeam(param=Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        self.assertTrue(ret, '新增服务团队信息失败')  
        Time.wait(1)
        ret = XiaQuGuanLiIntf.exportTeam(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111') 
        with open("C:/autotest_file/fuWuTuanDui.xls", "wb") as code:
            code.write(ret.content)
        pass 
    
        #检查点
        ret=CommonUtil.checkExcelCellValue(Param['serviceTeam.teamName'],"fuWuTuanDui.xls" , "服务团队清单", "A4")        
        self.assertTrue(ret, '服务团队信息导出检查失败')   
    
        
    def test_xqgl_25(self):   
        '''组织机构--服务团队 解散'''   
        #新增
        Param = copy.deepcopy(XiaQuGuanLiPara.addTeam)
        Param['mode'] = 'add'
        Param['isSubmit'] = 'true'
        Param['serviceTeam.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        Param['serviceTeam.org.orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        Param['serviceTeam.teamType.id'] =  CommonIntf.getIdByDomainAndDisplayName(domainName='服务团队类型-插件', displayName='安全建设')
        Param['serviceTeam.teamName'] = '服务团队%s' % CommonUtil.createRandomString(6)
        Param['serviceTeam.buildDate'] = Time.getCurrentDate()
        Param['serviceTeam.remark'] = '8'
        
        ret = XiaQuGuanLiIntf.addTeam(param=Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        self.assertTrue(ret, '新增服务团队信息失败')  
        Time.wait(1)
        ParamDiss = copy.deepcopy(XiaQuGuanLiPara.dismissTeam)   
        ParamDiss['serviceTeam.logOutTime'] = Time.getCurrentDate() 
        ParamDiss['serviceTeam.logOutReason'] = '444'
        ParamDiss['serviceTeam.id'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from serviceTeams t  where t.name ='%s'"% Param['serviceTeam.teamName'])
        ret = XiaQuGuanLiIntf.dismissTeam(param=ParamDiss, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        self.assertTrue(ret, '服务团队解散失败')  
         
    def test_xqgl_26(self): 
        """辖区管理--组织机构--成员库维护对象新增    """
        ShiYouRenKouIntf.deleteAllPopulation()
        #新增
        Param = copy.deepcopy(XiaQuGuanLiPara.personParam)   
        Param['serviceTeamMemberBase.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        Param['serviceTeamMemberBase.name'] = '成员库%s' % CommonUtil.createRandomString(6) 
        Param['serviceTeamMemberBase.gender.id'] =  CommonIntf.getIdByDomainAndDisplayName(domainName='性别(男、女)', displayName='男') 
        Param['serviceTeamMemberBase.mobile'] = random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8))
        Param['isSubmit'] = 'true' 
        ret = XiaQuGuanLiIntf.memberAdd(param=Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        self.assertTrue(ret, '成员库新增失败')  
        Time.wait(1)
        ##新增流动人口
        LiuDongParam_01 = copy.deepcopy(ShiYouRenKouPara.populationObject) 
        LiuDongParam_01['population.organization.id'] = orgInit['DftWangGeOrgId']
        LiuDongParam_01['population.actualPopulationType'] = 'floatingPopulation'
        LiuDongParam_01['population.organization.orgName'] = orgInit['DftWangGeOrg']
        LiuDongParam_01['population.idCardNo'] = '420621199105235756'
        LiuDongParam_01['population.name'] = 'test0233'
        LiuDongParam_01['population.isHaveHouse1'] = 'null'       
                      
        responseDict = ShiYouRenKouIntf.add_LiuDongRenKou(LiuDongRenKouDict=LiuDongParam_01, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增流动人口失败') 
        Time.wait(1) 
        LiuParam_01 = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)     
        LiuParam_01['idCardNo'] = LiuDongParam_01['population.idCardNo']     
        LiuParam_01['name'] = LiuDongParam_01['population.name'] 
        ret = ShiYouRenKouIntf.check_LiuDongpopulation(LiuParam_01, orgId=LiuDongParam_01['population.organization.id'],username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '查找流动人口失败')  
        pass
               
        weiHuDuiXiangParam = copy.deepcopy(XiaQuGuanLiPara.weiHuDuiXiang)   
        weiHuDuiXiangParam['baseId'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from SERVICETEAMMEMBERBASE t  where t.name ='%s'"%Param['serviceTeamMemberBase.name'])
        weiHuDuiXiangParam['objectType'] = 'floatingPopulation'
        objectIds = CommonIntf.getDbQueryResult(dbCommand = "select t.id from floatingPopulations t where t.idcardno='%s'" % LiuDongParam_01['population.idCardNo']) 
        weiHuDuiXiangParam['objectIdsAndNames'] = str(objectIds) +'-'+LiuDongParam_01['population.name']
        ret = XiaQuGuanLiIntf.weiHuDuiXiang(weiHuDuiXiangParam,username=userInit['DftWangGeUser'], password='11111111')         
        self.assertTrue(ret, '维护对象失败') 
        
        
    def test_xqgl_27(self): 
        """辖区管理--组织机构--成员库检测查重   """
        #新增
        Param = copy.deepcopy(XiaQuGuanLiPara.personParam)   
        Param['serviceTeamMemberBase.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        Param['serviceTeamMemberBase.name'] = '成员库%s' % CommonUtil.createRandomString(6) 
        Param['serviceTeamMemberBase.gender.id'] =  CommonIntf.getIdByDomainAndDisplayName(domainName='性别(男、女)', displayName='男') 
        Param['serviceTeamMemberBase.mobile'] = random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8))
        Param['isSubmit'] = 'true' 
        ret = XiaQuGuanLiIntf.memberAdd(param=Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        self.assertTrue(ret, '成员库新增失败')  
        Time.wait(1)
        
        #新增
        Param2 = copy.deepcopy(XiaQuGuanLiPara.personParam)   
        Param2['serviceTeamMemberBase.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        Param2['serviceTeamMemberBase.name'] = '成员库%s' % CommonUtil.createRandomString(6)  
        Param2['serviceTeamMemberBase.gender.id'] =  CommonIntf.getIdByDomainAndDisplayName(domainName='性别(男、女)', displayName='男') 
        Param2['serviceTeamMemberBase.mobile'] = random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8))
        Param2['isSubmit'] = 'true' 
        ret = XiaQuGuanLiIntf.memberAdd(param=Param2, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        self.assertTrue(ret, '成员库新增失败')  
        Time.wait(1)
        jcczParam = copy.deepcopy(XiaQuGuanLiPara.jianCeChaChong) 
        jcczParam['selectedIds'] = 0
        jcczParam['serviceTeamMemberVo.name'] = Param['serviceTeamMemberBase.name'] 
#         jcczParam['serviceTeamMemberVo.mobile'] = Param['serviceTeamMemberBase.mobile']
        jcczParam['serviceTeamMemberVo.baseId'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from SERVICETEAMMEMBERBASE t  where t.mobile = '"+Param['serviceTeamMemberBase.mobile']+"' and  t.name ='%s'"%Param['serviceTeamMemberBase.name'])
        jcczParam['serviceTeamMemberVo.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        jcczParam['combineSelectedIds'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from SERVICETEAMMEMBERBASE t  where t.name ='%s'"%Param2['serviceTeamMemberBase.name'])
        jcczParam['serviceTeamMemberBase.name '] =  Param2['serviceTeamMemberBase.name']
        
        ret = XiaQuGuanLiIntf.jianCeChaChong(param=jcczParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        self.assertTrue(ret, '检测查重失败')      
        Time.wait(1)
        #检查点
        ParamCheck = copy.deepcopy(XiaQuGuanLiPara.personCheck)
        ParamCheck['name'] = jcczParam['serviceTeamMemberVo.name']
        ParamCheck['mobile'] = Param['serviceTeamMemberBase.mobile']
        ret = XiaQuGuanLiIntf.checkPersonList(param=ParamCheck, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        self.assertTrue(ret, '成员库检测查重失败') 
        
    def test_xqgl_28(self): 
        """辖区管理--组织机构--成员库层级转移    """
        #新增
        Param = copy.deepcopy(XiaQuGuanLiPara.personParam)   
        Param['serviceTeamMemberBase.org.id'] = InitDefaultPara.orgInit['DftShiOrgId']
        Param['serviceTeamMemberBase.name'] = '成员库%s' % CommonUtil.createRandomString(6) 
        Param['serviceTeamMemberBase.gender.id'] =  CommonIntf.getIdByDomainAndDisplayName(domainName='性别(男、女)', displayName='男') 
        Param['serviceTeamMemberBase.mobile'] = random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8))
        Param['isSubmit'] = 'true' 
        ret = XiaQuGuanLiIntf.memberAdd(param=Param, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')        
        self.assertTrue(ret, '成员库新增失败')          
        Time.wait(1)
        cjParam = copy.deepcopy(XiaQuGuanLiPara.cengJiZhuanYi) 
        cjParam['orgId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        cjParam['selectedIds'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from SERVICETEAMMEMBERBASE t  where t.name = '%s'" % Param['serviceTeamMemberBase.name'])
        ret = XiaQuGuanLiIntf.cengJiZhuanYi(param=cjParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')        
#         self.assertTrue(ret, '层级转移失败') 
        
        #临时修改，这个方法不太合适，需要另写一个方法检查成员库
        ret = XiaQuGuanLiIntf.search_memberCheck(username = InitDefaultPara.userInit['DftWangGeUser'] ,password='11111111')
        self.assertFalse(ret, '成员库数据不为空') 
        
    def test_xqgl_29(self): 
        """辖区管理--组织机构--成员库导出    """
        #新增
        Param = copy.deepcopy(XiaQuGuanLiPara.personParam)   
        Param['serviceTeamMemberBase.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        Param['serviceTeamMemberBase.name'] = '成员库%s' % CommonUtil.createRandomString(6) 
        Param['serviceTeamMemberBase.gender.id'] =  CommonIntf.getIdByDomainAndDisplayName(domainName='性别(男、女)', displayName='男') 
        Param['serviceTeamMemberBase.mobile'] = random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8))
        Param['isSubmit'] = 'true' 
        ret = XiaQuGuanLiIntf.memberAdd(param=Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        self.assertTrue(ret, '成员库新增失败')         
        Time.wait(1)
        exportParam = copy.deepcopy(XiaQuGuanLiPara.personList) 
        exportParam['serviceTeamMemberVo.orgScope'] = 'sameGrade'
        exportParam['serviceTeamMemberVo.org.Id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        exportParam['serviceTeamMemberVo.nameIsDuplicate'] = 0
        ret = XiaQuGuanLiIntf.exportMember(exportParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111'); 
        with open("C:/autotest_file/member.xls", "wb") as code:
            code.write(ret.content)
        
        #检查点
        ret=CommonUtil.checkExcelCellValue(Param['serviceTeamMemberBase.name'],"member.xls" , "成员库清单", "A4")
        self.assertTrue(ret, '成员库导出检查失败')   
                 
    def test_xqgl_30(self): 
        """辖区管理--组织机构--成员库导入  """  
        Param = copy.deepcopy(XiaQuGuanLiPara.importMember) 
        Param['dataType']='serviceTeamMemberBase'
        Param['templates']='SERVICETEAMMEMBERBASE'
        files = {'upload': ('importMember.xls', open('C:/autotest_file/importMember.xls', 'rb'),'applicationnd.ms-excel')}
        XiaQuGuanLiIntf.importMember(Param=Param, files=files,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')    
        #检查点
        ParamCheck = copy.deepcopy(XiaQuGuanLiPara.personCheck)
        ParamCheck['name'] = '张三'
        ret = XiaQuGuanLiIntf.checkPersonList(param=ParamCheck, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
        self.assertTrue(ret, '成员库导入检查失败')                 
                 
#     def test_xqgl_31 (self):  
#         """辖区管理--组织机构--成员库显示姓名重复记录  """ 
#         #新增第一个
#         Param1 = copy.deepcopy(XiaQuGuanLiPara.personParam)   
#         Param1['serviceTeamMemberBase.id'] = ''
#         Param1['addTeam'] = ''
#         Param1['serviceTeamMemberBase.org.id'] = InitDefaultPara.orgInit['DftShiOrgId']
#         Param1['serviceTeamMemberBase.name'] = '成员库%s' % CommonUtil.createRandomString(6) 
#         Param1['serviceTeamMemberBase.gender.id'] = '91'
#         Param1['serviceTeamMemberBase.job'] = ''
#         Param1['serviceTeamMemberBase.birthday'] = ''    
#         Param1['serviceTeamMemberBase.mobile'] = ''
#         Param1['serviceTeamMemberBase.homePhone'] = ''
#         Param1['serviceTeamMemberBase.remark'] = ''
#         Param1['positionInTeam'] = ''
#         Param1['isSubmit'] = 'true' 
#         ret = XiaQuGuanLiIntf.memberAdd(param=Param1, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')        
#         self.assertTrue(ret, '成员库新增失败') 
#         
#         #新增第二个
#         Param2 = copy.deepcopy(XiaQuGuanLiPara.personParam)   
#         Param2['serviceTeamMemberBase.id'] = ''
#         Param2['addTeam'] = ''
#         Param2['serviceTeamMemberBase.org.id'] = InitDefaultPara.orgInit['DftShiOrgId']
#         Param2['serviceTeamMemberBase.name'] =  Param1['serviceTeamMemberBase.name'] 
#         Param2['serviceTeamMemberBase.gender.id'] = '91'
#         Param2['serviceTeamMemberBase.job'] = ''
#         Param2['serviceTeamMemberBase.birthday'] = ''    
#         Param2['serviceTeamMemberBase.mobile'] = ''
#         Param2['serviceTeamMemberBase.homePhone'] = ''
#         Param2['serviceTeamMemberBase.remark'] = ''
#         Param2['positionInTeam'] = ''
#         Param2['isSubmit'] = 'true' 
#         ret = XiaQuGuanLiIntf.memberAdd(param=Param2, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')        
#         self.assertTrue(ret, '成员库新增失败') 
#         
#         
#         #新增第三个
#         Param3 = copy.deepcopy(XiaQuGuanLiPara.personParam)   
#         Param3['serviceTeamMemberBase.id'] = ''
#         Param3['addTeam'] = ''
#         Param3['serviceTeamMemberBase.org.id'] = InitDefaultPara.orgInit['DftShiOrgId']
#         Param3['serviceTeamMemberBase.name'] = '成员库%s' % CommonUtil.createRandomString(6) 
#         Param3['serviceTeamMemberBase.gender.id'] = '91'
#         Param3['serviceTeamMemberBase.job'] = ''
#         Param3['serviceTeamMemberBase.birthday'] = ''    
#         Param3['serviceTeamMemberBase.mobile'] = ''
#         Param3['serviceTeamMemberBase.homePhone'] = ''
#         Param3['serviceTeamMemberBase.remark'] = ''
#         Param3['positionInTeam'] = ''
#         Param3['isSubmit'] = 'true' 
#         ret = XiaQuGuanLiIntf.memberAdd(param=Param3, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')        
#         self.assertTrue(ret, '成员库新增失败') 
#         
#         #检查点
#         ParamCheck = copy.deepcopy(XiaQuGuanLiPara.personCheck)
#         ParamCheck['name'] = Param2['serviceTeamMemberBase.name']
#         ret = XiaQuGuanLiIntf.checkPersonList(param=ParamCheck, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')        
#         self.assertFalse(ret, '成员库新增检查失败') 
#         
# #         lookParam = copy.deepcopy(XiaQuGuanLiPara.personParam)
# #         lookParam['serviceTeamMemberVo.orgScope'] = 'sameGrade'
# #         lookParam['serviceTeamMemberVo.org.Id'] = InitDefaultPara.orgInit['DftShiOrgId']
# #         lookParam['serviceTeamMemberVo.nameIsDuplicate'] = '1'
# #         ret = XiaQuGuanLiIntf.lookNames(param=lookParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')        
# #         self.assertTrue(ret, '成员库检查名称是否重复失败') 
        
                 
#新增记录库                     
    def test_xqgl_34(self):
        '''新增记录库'''
#         新增服务成员
        Premise_01Param = copy.deepcopy(XiaQuGuanLiPara.FuWuChengYuanObject) 
        Premise_01Param['serviceTeamMemberBase.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        Premise_01Param['serviceTeamMemberBase.job'] = '测试职位3'
        Premise_01Param['serviceTeamMemberBase.name'] = '测试服务成员%s'% CommonUtil.createRandomString()
        Premise_01Param['isSubmit'] = 'true'
        Premise_01Param['serviceTeamMemberBase.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别(男、女)', displayName='男')
        Premise_01Param['serviceTeamMemberBase.mobile'] = random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8))
        responseDict = XiaQuGuanLiIntf.addFuWuChengYuan(FuWuChengYuanDict=Premise_01Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        Time.wait(1)
#            查看服务人员
        param = copy.deepcopy(XiaQuGuanLiPara.ChaKanRenYuanObject)
        param['name'] = Premise_01Param['serviceTeamMemberBase.name'] 
        param['job'] = Premise_01Param['serviceTeamMemberBase.job'] 
        ret = XiaQuGuanLiIntf.checkFuWuChengYuanCompany(companyDict=param, orgId=Premise_01Param['serviceTeamMemberBase.org.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')
        Time.wait(1)

#         新增实有单位
        ZZCSCase_01Param = copy.deepcopy(XiaQuGuanLiPara.ShiYouDanWeiObject) 
        ZZCSCase_01Param['organizationId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        ZZCSCase_01Param['location.companyName'] = '测试单位%s'% CommonUtil.createRandomString()
        ZZCSCase_01Param['mode'] = 'add'
        ZZCSCase_01Param['location.companyAddress'] = '测试地址1'
        ZZCSCase_01Param['location.businessLicenseNo'] = '营业执照号码1'
        ZZCSCase_01Param['location.orgCode'] = '组织机构代码1'
        responseDict = XiaQuGuanLiIntf.addShiYouDanWei(ShiYouDanWeiDict=ZZCSCase_01Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        Time.wait(1)

#            查看实有单位
        param = copy.deepcopy(XiaQuGuanLiPara.ChaKanDanWeiObject)
        param['companyName'] = ZZCSCase_01Param['location.companyName']
        param['companyAddress'] = ZZCSCase_01Param['location.companyAddress']
        ret = XiaQuGuanLiIntf.checkShiYouDanWeiCompany(companyDict=param, orgId=ZZCSCase_01Param['organizationId'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')   
        Time.wait(1)
#            新增记录
        test_xiaQuGuanLiJiLuKu_34 = copy.deepcopy(XiaQuGuanLiPara.jilu) 
        test_xiaQuGuanLiJiLuKu_34['serviceRecord.organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        test_xiaQuGuanLiJiLuKu_34['serviceRecord.userOrgId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        test_xiaQuGuanLiJiLuKu_34['serviceRecord.teamId'] = '0'
        test_xiaQuGuanLiJiLuKu_34['isSubmit'] = 'true'
        test_xiaQuGuanLiJiLuKu_34['mode'] = 'add'
        id=CommonIntf.getDbQueryResult(dbCommand = "select t.id from actualCompany t where t.companyname ='%s'" % ZZCSCase_01Param['location.companyName'])
        test_xiaQuGuanLiJiLuKu_34['serviceRecord.serviceObjects'] = "%s-%s-actualCompany" %(id,ZZCSCase_01Param['location.companyName'])
        test_xiaQuGuanLiJiLuKu_34['serviceRecord.occurDate'] = Time.getCurrentDate()
        test_xiaQuGuanLiJiLuKu_34['serviceRecord.occurPlace'] = '服务地点'
        id2=CommonIntf.getDbQueryResult(dbCommand = "select t.id from SERVICETEAMMEMBERBASE t where t.name ='%s'" % Premise_01Param['serviceTeamMemberBase.name'])
        test_xiaQuGuanLiJiLuKu_34['serviceRecord.serviceMembers'] = "%s-%s-0" % (id2,Premise_01Param['serviceTeamMemberBase.name'])
        test_xiaQuGuanLiJiLuKu_34['serviceRecord.recordType'] = '1'
        test_xiaQuGuanLiJiLuKu_34["serviceRecord.serviceContent"] = '服务记录默认内容'
        
        responseDict = XiaQuGuanLiIntf.addjilu(jiluDict=test_xiaQuGuanLiJiLuKu_34, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        Time.wait(1)

#         查看记录是否新增成功
        param = copy.deepcopy(XiaQuGuanLiPara.ChaKanXunChangQingKuang)
        param['occurPlace'] = test_xiaQuGuanLiJiLuKu_34['serviceRecord.occurPlace']
        ret = XiaQuGuanLiIntf.checkXunChangQingKuangiCompany(companyDict=param, OrgId=test_xiaQuGuanLiJiLuKu_34['serviceRecord.organization.id'] ,username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')
        Time.wait(1)

#         删除服务人员
        deleteParam = copy.deepcopy(XiaQuGuanLiPara.delFuWuChengYuan)
        deleteParam['mode'] ='delete'
        deleteParam['selectedIds'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from SERVICETEAMMEMBERBASE t where t.name ='%s'" % Premise_01Param['serviceTeamMemberBase.name'])
        ret = XiaQuGuanLiIntf.deleteFuWuRenYuan(deleteParam,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
                 
        pass       
  

    def test_xqgl_35(self):
        """修改记录 """
#         新增服务成员
        Premise_01Param = copy.deepcopy(XiaQuGuanLiPara.FuWuChengYuanObject) 
        Premise_01Param['serviceTeamMemberBase.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        Premise_01Param['serviceTeamMemberBase.job'] = '测试职位3'
        Premise_01Param['serviceTeamMemberBase.name'] = '测试服务成员%s'% CommonUtil.createRandomString()
        Premise_01Param['isSubmit'] = 'true'
        Premise_01Param['serviceTeamMemberBase.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别(男、女)', displayName='男')
        Premise_01Param['serviceTeamMemberBase.mobile'] = random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8))
        responseDict = XiaQuGuanLiIntf.addFuWuChengYuan(FuWuChengYuanDict=Premise_01Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        Time.wait(1)
#            查看服务人员
        param = copy.deepcopy(XiaQuGuanLiPara.ChaKanRenYuanObject)
        param['name'] = Premise_01Param['serviceTeamMemberBase.name'] 
        param['job'] = Premise_01Param['serviceTeamMemberBase.job'] 
        ret = XiaQuGuanLiIntf.checkFuWuChengYuanCompany(companyDict=param, orgId=Premise_01Param['serviceTeamMemberBase.org.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')
        Time.wait(1)
        
#         新增实有单位
        ZZCSCase_01Param = copy.deepcopy(XiaQuGuanLiPara.ShiYouDanWeiObject) 
        ZZCSCase_01Param['organizationId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        ZZCSCase_01Param['location.companyName'] = '测试单位%s'% CommonUtil.createRandomString()
        ZZCSCase_01Param['mode'] = 'add'
        ZZCSCase_01Param['location.companyAddress'] = '测试地址1'
        ZZCSCase_01Param['location.businessLicenseNo'] = '营业执照号码1'
        ZZCSCase_01Param['location.orgCode'] = '组织机构代码1'
        responseDict = XiaQuGuanLiIntf.addShiYouDanWei(ShiYouDanWeiDict=ZZCSCase_01Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        Time.wait(1)
        
#            查看实有单位
        param = copy.deepcopy(XiaQuGuanLiPara.ChaKanDanWeiObject)
        param['companyName'] = ZZCSCase_01Param['location.companyName']
        param['companyAddress'] = ZZCSCase_01Param['location.companyAddress']
        ret = XiaQuGuanLiIntf.checkShiYouDanWeiCompany(companyDict=param, orgId=ZZCSCase_01Param['organizationId'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败') 
        Time.wait(1)       

#            新增记录
        test_xiaQuGuanLiJiLuKu_34 = copy.deepcopy(XiaQuGuanLiPara.jilu) 
        test_xiaQuGuanLiJiLuKu_34['serviceRecord.organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        test_xiaQuGuanLiJiLuKu_34['serviceRecord.userOrgId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        test_xiaQuGuanLiJiLuKu_34['serviceRecord.teamId'] = '0'
        test_xiaQuGuanLiJiLuKu_34['isSubmit'] = 'true'
        test_xiaQuGuanLiJiLuKu_34['mode'] = 'add'
        id=CommonIntf.getDbQueryResult(dbCommand = "select t.id from actualCompany t where t.companyname ='%s'" % ZZCSCase_01Param['location.companyName'])
        test_xiaQuGuanLiJiLuKu_34['serviceRecord.serviceObjects'] = "%s-%s-actualCompany" %(id,ZZCSCase_01Param['location.companyName'])
        test_xiaQuGuanLiJiLuKu_34['serviceRecord.occurDate'] = Time.getCurrentDate()
        test_xiaQuGuanLiJiLuKu_34['serviceRecord.occurPlace'] = '服务地点'
        id2=CommonIntf.getDbQueryResult(dbCommand = "select t.id from SERVICETEAMMEMBERBASE t where t.name ='%s'" % Premise_01Param['serviceTeamMemberBase.name'])
        test_xiaQuGuanLiJiLuKu_34['serviceRecord.serviceMembers'] = "%s-%s-0" % (id2,Premise_01Param['serviceTeamMemberBase.name'])
        test_xiaQuGuanLiJiLuKu_34['serviceRecord.recordType'] = '1'
        test_xiaQuGuanLiJiLuKu_34["serviceRecord.serviceContent"] = '服务记录默认内容'
        responseDict = XiaQuGuanLiIntf.addjilu(jiluDict=test_xiaQuGuanLiJiLuKu_34, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        Time.wait(1)
#         查看记录是否新增成功
        param = copy.deepcopy(XiaQuGuanLiPara.ChaKanXunChangQingKuang)
        param['occurPlace'] = test_xiaQuGuanLiJiLuKu_34['serviceRecord.occurPlace']
        ret = XiaQuGuanLiIntf.checkXunChangQingKuangiCompany(companyDict=param, OrgId=test_xiaQuGuanLiJiLuKu_34['serviceRecord.organization.id'] ,username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')
        Time.wait(1)

#        修改记录
        test_xiaQuGuanLiTeamDelAll_35 = copy.deepcopy(XiaQuGuanLiPara.xiugaijilu) 
        test_xiaQuGuanLiTeamDelAll_35['serviceRecord.organization.id'] = test_xiaQuGuanLiJiLuKu_34['serviceRecord.organization.id']
        test_xiaQuGuanLiTeamDelAll_35['serviceRecord.userOrgId'] = test_xiaQuGuanLiJiLuKu_34['serviceRecord.userOrgId']
        test_xiaQuGuanLiTeamDelAll_35['serviceRecord.teamId'] = test_xiaQuGuanLiJiLuKu_34['serviceRecord.teamId'] 
        test_xiaQuGuanLiTeamDelAll_35['mode'] = 'edit'
        test_xiaQuGuanLiTeamDelAll_35['serviceRecord.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from servicerecords t where t.occurplace='服务地点'")
        test_xiaQuGuanLiTeamDelAll_35['serviceRecord.serviceMembers'] = test_xiaQuGuanLiJiLuKu_34['serviceRecord.serviceMembers']
        test_xiaQuGuanLiTeamDelAll_35['serviceRecord.serviceObjects'] = test_xiaQuGuanLiJiLuKu_34['serviceRecord.serviceObjects'] 
        test_xiaQuGuanLiTeamDelAll_35['serviceRecord.occurDate'] = Time.getCurrentDate()
        test_xiaQuGuanLiTeamDelAll_35['serviceRecord.occurPlace'] = '测试服务地点'
        test_xiaQuGuanLiTeamDelAll_35['serviceRecord.recordType'] = '1'
        test_xiaQuGuanLiTeamDelAll_35["serviceRecord.serviceContent"] = test_xiaQuGuanLiJiLuKu_34["serviceRecord.serviceContent"]
        responseDict = XiaQuGuanLiIntf.modifyxiugaijilu(modifyObject=test_xiaQuGuanLiTeamDelAll_35, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改失败')        
        Time.wait(1)

#         查看记录是否修改成功
        param = copy.deepcopy(XiaQuGuanLiPara.ChaKanXunChangQingKuang)
        param['occurPlace'] = test_xiaQuGuanLiTeamDelAll_35['serviceRecord.occurPlace']
        ret = XiaQuGuanLiIntf.checkXunChangQingKuangiCompany(companyDict=param, OrgId=test_xiaQuGuanLiTeamDelAll_35['serviceRecord.organization.id'] ,username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')
        Time.wait(1)
#         删除服务人员
        deleteParam = copy.deepcopy(XiaQuGuanLiPara.delFuWuChengYuan)
        deleteParam['mode'] ='delete'
        deleteParam['selectedIds'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from SERVICETEAMMEMBERBASE t where t.name ='%s'" % Premise_01Param['serviceTeamMemberBase.name'])
        ret = XiaQuGuanLiIntf.deleteFuWuRenYuan(deleteParam,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        pass
        
    def test_xqgl_36(self):
        """生成民情日志 """
#         新增服务成员
        Premise_01Param = copy.deepcopy(XiaQuGuanLiPara.FuWuChengYuanObject) 
        Premise_01Param['serviceTeamMemberBase.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        Premise_01Param['serviceTeamMemberBase.job'] = '测试职位3'
        Premise_01Param['serviceTeamMemberBase.name'] = '测试服务成员%s'% CommonUtil.createRandomString()
        Premise_01Param['isSubmit'] = 'true'
        Premise_01Param['serviceTeamMemberBase.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别(男、女)', displayName='男')
        Premise_01Param['serviceTeamMemberBase.mobile'] = random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8))
        responseDict = XiaQuGuanLiIntf.addFuWuChengYuan(FuWuChengYuanDict=Premise_01Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        Time.wait(1)
#            查看服务人员
        param = copy.deepcopy(XiaQuGuanLiPara.ChaKanRenYuanObject)
        param['name'] = Premise_01Param['serviceTeamMemberBase.name'] 
        param['job'] = Premise_01Param['serviceTeamMemberBase.job'] 
        ret = XiaQuGuanLiIntf.checkFuWuChengYuanCompany(companyDict=param, orgId=Premise_01Param['serviceTeamMemberBase.org.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')
        Time.wait(1)
        
#         新增实有单位
        ZZCSCase_01Param = copy.deepcopy(XiaQuGuanLiPara.ShiYouDanWeiObject) 
        ZZCSCase_01Param['organizationId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        ZZCSCase_01Param['location.companyName'] = '测试单位%s'% CommonUtil.createRandomString()
        ZZCSCase_01Param['mode'] = 'add'
        ZZCSCase_01Param['location.companyAddress'] = '测试地址1'
        ZZCSCase_01Param['location.businessLicenseNo'] = '营业执照号码1'
        ZZCSCase_01Param['location.orgCode'] = '组织机构代码1'
        responseDict = XiaQuGuanLiIntf.addShiYouDanWei(ShiYouDanWeiDict=ZZCSCase_01Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        Time.wait(1)
        
#            查看实有单位
        param = copy.deepcopy(XiaQuGuanLiPara.ChaKanDanWeiObject)
        param['companyName'] = ZZCSCase_01Param['location.companyName']
        param['companyAddress'] = ZZCSCase_01Param['location.companyAddress']
        ret = XiaQuGuanLiIntf.checkShiYouDanWeiCompany(companyDict=param, orgId=ZZCSCase_01Param['organizationId'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')
        Time.wait(1)        

#            新增记录
        test_xiaQuGuanLiJiLuKu_34 = copy.deepcopy(XiaQuGuanLiPara.jilu) 
        test_xiaQuGuanLiJiLuKu_34['serviceRecord.organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        test_xiaQuGuanLiJiLuKu_34['serviceRecord.userOrgId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        test_xiaQuGuanLiJiLuKu_34['serviceRecord.teamId'] = '0'
        test_xiaQuGuanLiJiLuKu_34['isSubmit'] = 'true'
        test_xiaQuGuanLiJiLuKu_34['mode'] = 'add'
        id=CommonIntf.getDbQueryResult(dbCommand = "select t.id from actualCompany t where t.companyname ='%s'" % ZZCSCase_01Param['location.companyName'])
        test_xiaQuGuanLiJiLuKu_34['serviceRecord.serviceObjects'] = "%s-%s-actualCompany" %(id,ZZCSCase_01Param['location.companyName'])
        test_xiaQuGuanLiJiLuKu_34['serviceRecord.occurDate'] = Time.getCurrentDate()
        test_xiaQuGuanLiJiLuKu_34['serviceRecord.occurPlace'] = '服务地点'
        id2=CommonIntf.getDbQueryResult(dbCommand = "select t.id from SERVICETEAMMEMBERBASE t where t.name ='%s'" % Premise_01Param['serviceTeamMemberBase.name'])
        test_xiaQuGuanLiJiLuKu_34['serviceRecord.serviceMembers'] = "%s-%s-0" % (id2,Premise_01Param['serviceTeamMemberBase.name'])
        test_xiaQuGuanLiJiLuKu_34['serviceRecord.recordType'] = '1'
        test_xiaQuGuanLiJiLuKu_34["serviceRecord.serviceContent"] = '服务记录默认内容'
        responseDict = XiaQuGuanLiIntf.addjilu(jiluDict=test_xiaQuGuanLiJiLuKu_34, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        Time.wait(1)

#         查看记录是否新增成功
        param = copy.deepcopy(XiaQuGuanLiPara.ChaKanXunChangQingKuang)
        param['occurPlace'] = test_xiaQuGuanLiJiLuKu_34['serviceRecord.occurPlace']
        ret = XiaQuGuanLiIntf.checkXunChangQingKuangiCompany(companyDict=param, OrgId=test_xiaQuGuanLiJiLuKu_34['serviceRecord.organization.id'] ,username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')
        Time.wait(1)

#        生成民情日志
        test_xiaQuGuanLiTeamDelAll_36 = copy.deepcopy(XiaQuGuanLiPara.scmingqinrizhi) 
        test_xiaQuGuanLiTeamDelAll_36['peopleLog.userId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from users t where t.username='%s'" % (InitDefaultPara.userInit['DftWangGeUser']))
        test_xiaQuGuanLiTeamDelAll_36['peopleLog.serviceRecordId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from servicerecords t where t.occurplace='%s'" %test_xiaQuGuanLiJiLuKu_34['serviceRecord.occurPlace'])
        test_xiaQuGuanLiTeamDelAll_36['peopleLog.organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        test_xiaQuGuanLiTeamDelAll_36['peopleLog.isAttachment'] = 'false'
        test_xiaQuGuanLiTeamDelAll_36['peopleLog.organization.orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
        test_xiaQuGuanLiTeamDelAll_36['peopleLog.belonger'] = '测试服务成员'
        test_xiaQuGuanLiTeamDelAll_36['peopleLog.publishDate'] = Time.getCurrentDate()
        test_xiaQuGuanLiTeamDelAll_36['peopleLog.address'] = '服务地点'
        test_xiaQuGuanLiTeamDelAll_36['peopleLog.title'] = '标题'
        test_xiaQuGuanLiTeamDelAll_36['peopleLog.contents'] = '内容'
        responseDict = XiaQuGuanLiIntf.addscmingqinrizhi(scmingqinrizhiDict=test_xiaQuGuanLiTeamDelAll_36, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        Time.wait(1)

#         查看民情日志是否新增成功
        param = copy.deepcopy(XiaQuGuanLiPara.chakanminqinrizhi)
        param['title'] = test_xiaQuGuanLiTeamDelAll_36['peopleLog.title']
        ret = XiaQuGuanLiIntf.checkXunminqinrizhiCompany(companyDict=param ,username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')
        Time.wait(1)

#         删除服务人员
        deleteParam = copy.deepcopy(XiaQuGuanLiPara.delFuWuChengYuan)
        deleteParam['mode'] ='delete'
        deleteParam['selectedIds'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from SERVICETEAMMEMBERBASE t where t.name ='%s'" % Premise_01Param['serviceTeamMemberBase.name'])
        ret = XiaQuGuanLiIntf.deleteFuWuRenYuan(deleteParam,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')       

#         删除民情日志        
        deleteParam = copy.deepcopy(XiaQuGuanLiPara.delminqinrizhi)
        deleteParam['logIds'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from PEOPLELOG t where t.title='%s'" %test_xiaQuGuanLiTeamDelAll_36['peopleLog.title'])
        ret = XiaQuGuanLiIntf.deleteminqinrizhi(deleteParam,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')    
        
        pass

    def test_xqgl_37(self):
        """导出 """
#         新增服务成员
        Premise_01Param = copy.deepcopy(XiaQuGuanLiPara.FuWuChengYuanObject) 
        Premise_01Param['serviceTeamMemberBase.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        Premise_01Param['serviceTeamMemberBase.job'] = '测试职位3'
        Premise_01Param['serviceTeamMemberBase.name'] = '测试服务成员%s'% CommonUtil.createRandomString()
        Premise_01Param['isSubmit'] = 'true'
        Premise_01Param['serviceTeamMemberBase.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别(男、女)', displayName='男')
        Premise_01Param['serviceTeamMemberBase.mobile'] = random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8))
        responseDict = XiaQuGuanLiIntf.addFuWuChengYuan(FuWuChengYuanDict=Premise_01Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        Time.wait(1)
#查看服务人员
        param = copy.deepcopy(XiaQuGuanLiPara.ChaKanRenYuanObject)
        param['name'] = Premise_01Param['serviceTeamMemberBase.name'] 
        param['job'] = Premise_01Param['serviceTeamMemberBase.job'] 
        ret = XiaQuGuanLiIntf.checkFuWuChengYuanCompany(companyDict=param, orgId=Premise_01Param['serviceTeamMemberBase.org.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')
        Time.wait(1)
        
#新增实有单位
        ZZCSCase_01Param = copy.deepcopy(XiaQuGuanLiPara.ShiYouDanWeiObject) 
        ZZCSCase_01Param['organizationId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        ZZCSCase_01Param['location.companyName'] = '测试单位%s'% CommonUtil.createRandomString()
        ZZCSCase_01Param['mode'] = 'add'
        ZZCSCase_01Param['location.companyAddress'] = '测试地址1'
        ZZCSCase_01Param['location.businessLicenseNo'] = '营业执照号码1'
        ZZCSCase_01Param['location.orgCode'] = '组织机构代码1'
        responseDict = XiaQuGuanLiIntf.addShiYouDanWei(ShiYouDanWeiDict=ZZCSCase_01Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        Time.wait(1)
        
#查看实有单位
        param = copy.deepcopy(XiaQuGuanLiPara.ChaKanDanWeiObject)
        param['companyName'] = ZZCSCase_01Param['location.companyName']
        param['companyAddress'] = ZZCSCase_01Param['location.companyAddress']
        ret = XiaQuGuanLiIntf.checkShiYouDanWeiCompany(companyDict=param, orgId=ZZCSCase_01Param['organizationId'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败') 
        Time.wait(1)       

#新增记录
        test_xiaQuGuanLiJiLuKu_34 = copy.deepcopy(XiaQuGuanLiPara.jilu) 
        test_xiaQuGuanLiJiLuKu_34['serviceRecord.organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        test_xiaQuGuanLiJiLuKu_34['serviceRecord.userOrgId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        test_xiaQuGuanLiJiLuKu_34['serviceRecord.teamId'] = '0'
        test_xiaQuGuanLiJiLuKu_34['isSubmit'] = 'true'
        test_xiaQuGuanLiJiLuKu_34['mode'] = 'add'
        id=CommonIntf.getDbQueryResult(dbCommand = "select t.id from actualCompany t where t.companyname ='%s'" % ZZCSCase_01Param['location.companyName'])
        test_xiaQuGuanLiJiLuKu_34['serviceRecord.serviceObjects'] = "%s-%s-actualCompany" %(id,ZZCSCase_01Param['location.companyName'])
        test_xiaQuGuanLiJiLuKu_34['serviceRecord.occurDate'] = Time.getCurrentDate()
        test_xiaQuGuanLiJiLuKu_34['serviceRecord.occurPlace'] = '服务地点'
        id2=CommonIntf.getDbQueryResult(dbCommand = "select t.id from SERVICETEAMMEMBERBASE t where t.name ='%s'" % Premise_01Param['serviceTeamMemberBase.name'])
        test_xiaQuGuanLiJiLuKu_34['serviceRecord.serviceMembers'] = "%s-%s-0" % (id2,Premise_01Param['serviceTeamMemberBase.name'])
        test_xiaQuGuanLiJiLuKu_34['serviceRecord.recordType'] = '1'
        test_xiaQuGuanLiJiLuKu_34["serviceRecord.serviceContent"] = '服务记录默认内容'
        responseDict = XiaQuGuanLiIntf.addjilu(jiluDict=test_xiaQuGuanLiJiLuKu_34, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        Time.wait(1)
#查看记录是否新增成功
        param = copy.deepcopy(XiaQuGuanLiPara.ChaKanXunChangQingKuang)
        param['occurPlace'] = test_xiaQuGuanLiJiLuKu_34['serviceRecord.occurPlace']
        ret = XiaQuGuanLiIntf.checkXunChangQingKuangiCompany(companyDict=param, OrgId=test_xiaQuGuanLiJiLuKu_34['serviceRecord.organization.id'] ,username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')
        Time.wait(1)
#导出记录
        downLoad = copy.deepcopy(XiaQuGuanLiPara.dldataShiYouDanWei)
        downLoad['serviceRecordVo.organization.id']=orgInit['DftWangGeOrgId']
        response = XiaQuGuanLiIntf.dldataShiYouRenKou(downLoad, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')         
        with open("C:/autotest_file/testjiluku.xls", "wb") as code:
            code.write(response.content)
            
        ret = CommonUtil.checkExcelCellValue('服务地点', 'testjiluku.xls','服务记录清单', 'B4')          
        self.assertTrue(ret, '导出失败')   

#删除服务人员
        deleteParam = copy.deepcopy(XiaQuGuanLiPara.delFuWuChengYuan)
        deleteParam['mode'] ='delete'
        deleteParam['selectedIds'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from SERVICETEAMMEMBERBASE t where t.name ='%s'" % Premise_01Param['serviceTeamMemberBase.name'])
        ret = XiaQuGuanLiIntf.deleteFuWuRenYuan(deleteParam,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')                    
        pass
                   

    def test_xqgl_38(self):
        """记录库高级搜素 """
#新增服务成员
        Premise_01Param = copy.deepcopy(XiaQuGuanLiPara.FuWuChengYuanObject) 
        Premise_01Param['serviceTeamMemberBase.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        Premise_01Param['serviceTeamMemberBase.job'] = '测试职位3'
        Premise_01Param['serviceTeamMemberBase.name'] = '测试服务成员%s'% CommonUtil.createRandomString()
        Premise_01Param['isSubmit'] = 'true'
        Premise_01Param['serviceTeamMemberBase.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别(男、女)', displayName='男')
        Premise_01Param['serviceTeamMemberBase.mobile'] = random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8))
        responseDict = XiaQuGuanLiIntf.addFuWuChengYuan(FuWuChengYuanDict=Premise_01Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        Time.wait(1)
#查看服务人员
        param = copy.deepcopy(XiaQuGuanLiPara.ChaKanRenYuanObject)
        param['name'] = Premise_01Param['serviceTeamMemberBase.name'] 
        param['job'] = Premise_01Param['serviceTeamMemberBase.job'] 
        ret = XiaQuGuanLiIntf.checkFuWuChengYuanCompany(companyDict=param, orgId=Premise_01Param['serviceTeamMemberBase.org.id'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')
        Time.wait(1)
        
#新增实有单位
        ZZCSCase_01Param = copy.deepcopy(XiaQuGuanLiPara.ShiYouDanWeiObject) 
        ZZCSCase_01Param['organizationId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        ZZCSCase_01Param['location.companyName'] = '测试单位%s'% CommonUtil.createRandomString()
        ZZCSCase_01Param['mode'] = 'add'
        ZZCSCase_01Param['location.companyAddress'] = '测试地址1'
        ZZCSCase_01Param['location.businessLicenseNo'] = '营业执照号码1'
        ZZCSCase_01Param['location.orgCode'] = '组织机构代码1'
        responseDict = XiaQuGuanLiIntf.addShiYouDanWei(ShiYouDanWeiDict=ZZCSCase_01Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        Time.wait(1)
#查看实有单位
        param = copy.deepcopy(XiaQuGuanLiPara.ChaKanDanWeiObject)
        param['companyName'] = ZZCSCase_01Param['location.companyName']
        param['companyAddress'] = ZZCSCase_01Param['location.companyAddress']
        ret = XiaQuGuanLiIntf.checkShiYouDanWeiCompany(companyDict=param, orgId=ZZCSCase_01Param['organizationId'],username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')        
        Time.wait(1)
#新增记录
        test_xiaQuGuanLiJiLuKu_34 = copy.deepcopy(XiaQuGuanLiPara.jilu) 
        test_xiaQuGuanLiJiLuKu_34['serviceRecord.organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        test_xiaQuGuanLiJiLuKu_34['serviceRecord.userOrgId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        test_xiaQuGuanLiJiLuKu_34['serviceRecord.teamId'] = '0'
        test_xiaQuGuanLiJiLuKu_34['isSubmit'] = 'true'
        test_xiaQuGuanLiJiLuKu_34['mode'] = 'add'
        id=CommonIntf.getDbQueryResult(dbCommand = "select t.id from actualCompany t where t.companyname ='%s'" % ZZCSCase_01Param['location.companyName'])
        test_xiaQuGuanLiJiLuKu_34['serviceRecord.serviceObjects'] = "%s-%s-actualCompany" %(id,ZZCSCase_01Param['location.companyName'])
        test_xiaQuGuanLiJiLuKu_34['serviceRecord.occurDate'] = Time.getCurrentDate()
        test_xiaQuGuanLiJiLuKu_34['serviceRecord.occurPlace'] = '服务地点'
        id2=CommonIntf.getDbQueryResult(dbCommand = "select t.id from SERVICETEAMMEMBERBASE t where t.name ='%s'" % Premise_01Param['serviceTeamMemberBase.name'])
        test_xiaQuGuanLiJiLuKu_34['serviceRecord.serviceMembers'] = "%s-%s-0" % (id2,Premise_01Param['serviceTeamMemberBase.name'])
        test_xiaQuGuanLiJiLuKu_34['serviceRecord.recordType'] = '1'
        test_xiaQuGuanLiJiLuKu_34["serviceRecord.serviceContent"] = '服务记录默认内容'
        responseDict = XiaQuGuanLiIntf.addjilu(jiluDict=test_xiaQuGuanLiJiLuKu_34, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增失败')
        Time.wait(1)

#查看记录是否新增成功
        param = copy.deepcopy(XiaQuGuanLiPara.ChaKanXunChangQingKuang)
        param['occurPlace'] = test_xiaQuGuanLiJiLuKu_34['serviceRecord.occurPlace']
        ret = XiaQuGuanLiIntf.checkXunChangQingKuangiCompany(companyDict=param, OrgId=test_xiaQuGuanLiJiLuKu_34['serviceRecord.organization.id'] ,username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')         
        self.assertTrue(ret, '查找失败')
        Time.wait(1)
        # 第一种情况:根据服务地点搜索 
        issueParamSearch = copy.deepcopy(XiaQuGuanLiPara.jilu) 
        issueParamSearch['serviceRecord.occurPlace'] = test_xiaQuGuanLiJiLuKu_34['serviceRecord.occurPlace']
        ret = XiaQuGuanLiIntf.chaxundaibanrizhi(issueParamSearch, username=InitDefaultPara.userInit['DftShiUser'], password='11111111');
        self.assertTrue(ret, '企业信息搜索失败')
        Time.wait(1)
        ret = XiaQuGuanLiIntf.Companychaxundaibanrizhi(issueParamSearch, company='abcdabcd', username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertFalse(ret, '数据匹配失败')
        Time.wait(1)
#         删除服务人员
        deleteParam = copy.deepcopy(XiaQuGuanLiPara.delFuWuChengYuan)
        deleteParam['mode'] ='delete'
        deleteParam['selectedIds'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from SERVICETEAMMEMBERBASE t where t.name ='%s'" % Premise_01Param['serviceTeamMemberBase.name'])
        ret = XiaQuGuanLiIntf.deleteFuWuRenYuan(deleteParam,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111') 
        pass

    def tearDown(self):

        pass
    
    
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(XiaQuGuanLi("test_xqgl_38"))
      
    results = unittest.TextTestRunner().run(suite)
    pass
        
    
        

