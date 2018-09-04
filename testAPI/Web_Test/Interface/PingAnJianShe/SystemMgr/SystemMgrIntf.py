# -*- coding:UTF-8 -*-
'''
Created on 2015-11-10

@author: N-254
'''
from __future__ import unicode_literals
from COMMON import Time, Log
from CONFIG import Global
from CONFIG.Define import LogLevel
from CONFIG.InitDefaultPara import roleInit, orgInit, userInit, clueOrgInit, \
    clueUserInit
from Interface.PingAnJianShe.Common import CommonIntf
from Interface.PingAnJianShe.SystemMgr import SystemMgrPara
from Interface.PingAnJianShe.pingAnJianSheHttpCommon import pinganjianshe_post, \
    renzhengzhongxin_post
import copy

'''
    @功能：     添加默认岗位，岗位包含所有层级
    @para: 
    @return: 如果添加成功，则返回True；否则返回False  
    @ hongzenghui 2015-11-11 
'''
# def createDefaultRenZhengRole(roleName=roleInit['DftRoleName']):
#     if CommonIntf.getDbQueryResult(dbCommand="select * from roles t where t.rolename='%s'" % roleName) is not None:
# #         Log.LogOutput(level=LogLevel.INFO, message='待添加的岗位已经存在，无需添加')       
#         return True
#     else:
#         roleObject = copy.deepcopy(SystemMgrPara.renzhengRoleObject)
#         roleObject['mode']='copy'
#         roleObject['role.createDate']= Time.getCurrentDateAndTime()
#         roleObject['role.id']='20069503'
#         roleObject['role.roleName']= roleName
#         roleObject['role.workBenchType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName = '工作台类型', displayName = '中层') 
#         countryId = CommonIntf.getIdByDomainAndDisplayName(domainName='网格分级', displayName='全国')
#         provinceId = CommonIntf.getIdByDomainAndDisplayName(domainName='网格分级', displayName='省')
#         countyId = CommonIntf.getIdByDomainAndDisplayName(domainName='网格分级', displayName='县（区）')
#         villageId = CommonIntf.getIdByDomainAndDisplayName(domainName='网格分级', displayName='村（社区）')
#         unitVillageId = CommonIntf.getIdByDomainAndDisplayName(domainName='网格分级', displayName='联村（社区组织）')
#         segmentId = CommonIntf.getIdByDomainAndDisplayName(domainName='网格分级', displayName='片组片格')
#         townId = CommonIntf.getIdByDomainAndDisplayName(domainName='网格分级', displayName='乡镇（街道）')
#         cityId = CommonIntf.getIdByDomainAndDisplayName(domainName='网格分级', displayName='市')
#         roleObject['useInLevelIds'] = [countryId,provinceId,countyId,villageId,unitVillageId,segmentId,townId,cityId]        
#         response = renzhengzhongxin_post(url='/sysadmin/role/copyRole.json', postdata=roleObject, username=Global.PingAnJianSheUser, password=Global.PingAnJianShePass)
#         if response.result is False:
#             Log.LogOutput(level=LogLevel.DEBUG, message='默认岗位添加失败') 
#             return False
#         else:
#             Log.LogOutput(level=LogLevel.DEBUG, message='默认岗位添加成功') 
#             return True
        
def createDefaultRole(roleName=roleInit['DftRoleName']):
    if CommonIntf.getDbQueryResult(dbCommand="select * from roles t where t.rolename='%s'" % roleName) is not None:
#         Log.LogOutput(level=LogLevel.INFO, message='待添加的岗位已经存在，无需添加')       
        return True
    else:
        roleObject = copy.deepcopy(SystemMgrPara.roleObject)
        roleObject['mode']='copy'
        roleObject['role.createDate']= Time.getCurrentDateAndTime()
        roleObject['role.id']='1'
        roleObject['role.roleName']= roleName
        roleObject['role.workBenchType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName = '工作台类型', displayName = '中层') 
        countryId = CommonIntf.getIdByDomainAndDisplayName(domainName='网格分级', displayName='全国')
        provinceId = CommonIntf.getIdByDomainAndDisplayName(domainName='网格分级', displayName='省')
        countyId = CommonIntf.getIdByDomainAndDisplayName(domainName='网格分级', displayName='县（区）')
        villageId = CommonIntf.getIdByDomainAndDisplayName(domainName='网格分级', displayName='村（社区）')
        unitVillageId = CommonIntf.getIdByDomainAndDisplayName(domainName='网格分级', displayName='联村（社区组织）')
        segmentId = CommonIntf.getIdByDomainAndDisplayName(domainName='网格分级', displayName='片组片格')
        townId = CommonIntf.getIdByDomainAndDisplayName(domainName='网格分级', displayName='乡镇（街道）')
        cityId = CommonIntf.getIdByDomainAndDisplayName(domainName='网格分级', displayName='市')
        roleObject['role.useInLevel.id'] = cityId
        roleObject['role.useInLevelIds.0'] = cityId
        roleObject['useInLevelIds'] = [countryId,provinceId,countyId,villageId,unitVillageId,segmentId,townId,cityId]        
#         response = pinganjianshe_post(url='/sysadmin/roleManage/copyRole.action', postdata=roleObject, username=Global.RenZhengZhongXinAdminUser, password=Global.RenZhengZhongXinAdminPass)
        response = renzhengzhongxin_post(url='/sysadmin/role/copyRole.json', postdata=roleObject, username=Global.RenZhengZhongXinAdminUser, password=Global.RenZhengZhongXinAdminPass)
        if response.result is False:
            Log.LogOutput(level=LogLevel.DEBUG, message='默认岗位添加失败') 
            return False
        else:
            Log.LogOutput(level=LogLevel.DEBUG, message='默认岗位添加成功') 
            return True
        
'''
    @功能：     添加省级部门
    @para: provinceOrgName：部门名称，默认为测试自动化省
    @return: 如果添加成功，则返回True；否则返回False  
    @ hongzenghui 2015-11-11 
'''

def addProvinceOrg(provinceOrgName=orgInit['DftShengOrg']):
    if CommonIntf.getDbQueryResult(dbCommand="select * from ORGANIZATIONS t where t.orgname='%s'" % provinceOrgName) is not None:
#         Log.LogOutput(level=LogLevel.INFO, message='待添加的省已经存在，无需添加')       
        return True
    else:
        orgObject = copy.deepcopy(SystemMgrPara.orgnizationObject)
        orgObject['departmentNoC']='95'
        orgObject['organization.orgLevel.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='网格分级', displayName='省')
        orgObject['organization.orgName']= provinceOrgName
        orgObject['organization.orgType.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='网格类型', displayName='行政区域')
        orgObject['organization.parentOrg.id']= '1'
        response = renzhengzhongxin_post(url='/sysadmin/orgManage/ajaxAddOrganization', postdata=orgObject, username=Global.RenZhengZhongXinAdminUser, password=Global.RenZhengZhongXinAdminPass)
        if response.result is False:
            Log.LogOutput(level=LogLevel.DEBUG, message='添加省级部门失败') 
            return False
        else:   
            Log.LogOutput(level=LogLevel.DEBUG, message='添加省级部门成功') 
            return True
        
'''
    @功能：     添加省级职能部门
    @para: provinceFuncOrgName：职能部门名称，默认为测试自动化省公安部
    provinceOrgName:待添加的职能部门所在的省
    @return: 如果添加成功，则返回True；否则返回False  
    @ hongzenghui 2015-11-11 
'''

def addProvinceFuncOrg(provinceFuncOrgName=orgInit['DftShengFuncOrg'],provinceOrgName=orgInit['DftShengOrg'],funcOrgType=orgInit['DftShengFuncOrgType']):
    if CommonIntf.getDbQueryResult(dbCommand="select * from ORGANIZATIONS t where t.orgname='%s'" % provinceFuncOrgName) is not None:
#         Log.LogOutput(level=LogLevel.INFO, message='待添加的省职能部门已经存在，无需添加')       
        return True
    else:
        orgObject = copy.deepcopy(SystemMgrPara.orgnizationObject)
        orgObject['departmentNoC']='jt'
        orgObject['departmentNoF']=CommonIntf.getDbQueryResult(dbCommand="select t.departmentno from ORGANIZATIONS t where t.orgname='%s'" % provinceOrgName)
        orgObject['organization.functionalOrgType.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='职能部门类型', displayName='%s' % funcOrgType)
        orgObject['organization.orgLevel.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='网格分级', displayName='市')
        orgObject['organization.orgName']= provinceFuncOrgName
        orgObject['organization.orgType.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='网格类型', displayName='职能部门')
        orgObject['organization.parentOrg.id']= CommonIntf.getDbQueryResult(dbCommand="select t.id from ORGANIZATIONS t where t.orgname='%s'" % provinceOrgName)
        response = renzhengzhongxin_post(url='/sysadmin/orgManage/ajaxAddOrganization', postdata=orgObject, username=Global.RenZhengZhongXinAdminUser, password=Global.RenZhengZhongXinAdminPass)
        if response.result is False:
            Log.LogOutput(level=LogLevel.DEBUG, message='添加省级职能部门失败') 
            return False
        else:   
            Log.LogOutput(level=LogLevel.DEBUG, message='添加省级职能部门成功') 
            return True
        
'''
    @功能：     添加市级部门
    @para: cityOrgName：部门名称，默认为测试自动化市
    provinceName：待添加的市所在的省名称
    @return: 如果添加成功，则返回True；否则返回False  
    @ hongzenghui 2015-11-11 
'''

def addCityOrg(cityOrgName=orgInit['DftShiOrg'],provinceName=orgInit['DftShengOrg']):
    if CommonIntf.getDbQueryResult(dbCommand="select * from ORGANIZATIONS t where t.orgname='%s'" % cityOrgName) is not None:
#         Log.LogOutput(level=LogLevel.INFO, message='待添加的市已经存在，无需添加')       
        return True
    else:
        orgObject = copy.deepcopy(SystemMgrPara.orgnizationObject)
        orgObject['departmentNoC']=CommonIntf.getDbQueryResult(dbCommand="select t.departmentno from ORGANIZATIONS t where t.orgname='%s'" % provinceName)
        orgObject['departmentNoF']=CommonIntf.getDbQueryResult(dbCommand="select t.departmentno from ORGANIZATIONS t where t.orgname='%s'" % provinceName)
        orgObject['organization.orgLevel.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='网格分级', displayName='市')
        orgObject['organization.orgName']= cityOrgName
        orgObject['organization.orgType.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='网格类型', displayName='行政区域')
        orgObject['organization.parentOrg.id']= CommonIntf.getDbQueryResult(dbCommand="select t.id from ORGANIZATIONS t where t.orgname='%s'" % provinceName)
        response = renzhengzhongxin_post(url='/sysadmin/orgManage/ajaxAddOrganization', postdata=orgObject, username=Global.RenZhengZhongXinAdminUser, password=Global.RenZhengZhongXinAdminPass)
        if response.result is False:
            Log.LogOutput(level=LogLevel.DEBUG, message='添加市级部门失败') 
            return False
        else:   
            Log.LogOutput(level=LogLevel.DEBUG, message='添加市级部门成功') 
            return True

'''
    @功能：     添加市级职能部门
    @para: cityFuncOrgName：职能部门名称，默认为测试自动化市公安部
    cityOrgName:待添加的职能部门所在的市
    @return: 如果添加成功，则返回True；否则返回False  
    @ hongzenghui 2015-11-11 
'''

def addCityFuncOrg(cityFuncOrgName=orgInit['DftShiFuncOrg'],cityOrgName=orgInit['DftShiOrg'],funcOrgType=orgInit['DftShiFuncOrgType']):
    if CommonIntf.getDbQueryResult(dbCommand="select * from ORGANIZATIONS t where t.orgname='%s'" % cityFuncOrgName) is not None:
#         Log.LogOutput(level=LogLevel.INFO, message='待添加的市职能部门已经存在，无需添加')       
        return True
    else:
        orgObject = copy.deepcopy(SystemMgrPara.orgnizationObject)
        if cityFuncOrgName==orgInit['DftShiFuncOrg']:
            orgObject['departmentNoC']='1jt'
        else:
            orgObject['departmentNoC']='6jt'
        orgObject['departmentNoF']=CommonIntf.getDbQueryResult(dbCommand="select t.departmentno from ORGANIZATIONS t where t.orgname='%s'" % cityOrgName)
        orgObject['organization.functionalOrgType.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='职能部门类型', displayName='%s' % funcOrgType)
        orgObject['organization.orgLevel.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='网格分级', displayName='县（区）')
        orgObject['organization.orgName']= cityFuncOrgName
        orgObject['organization.orgType.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='网格类型', displayName='职能部门')
        orgObject['organization.parentOrg.id']= CommonIntf.getDbQueryResult(dbCommand="select t.id from ORGANIZATIONS t where t.orgname='%s'" % cityOrgName)
        response = renzhengzhongxin_post(url='/sysadmin/orgManage/ajaxAddOrganization', postdata=orgObject, username=Global.RenZhengZhongXinAdminUser, password=Global.RenZhengZhongXinAdminPass)
        if response.result is False:
            Log.LogOutput(level=LogLevel.DEBUG, message='添加市级职能部门失败') 
            return False
        else:   
            Log.LogOutput(level=LogLevel.DEBUG, message='添加市级职能部门成功') 
            return True

'''
    @功能：     添加区县部门
    @para: districtOrgName：部门名称，默认为测试区
    cityName：待添加的区所在的市名称
    @return: 如果添加成功，则返回True；否则返回False  
    @ hongzenghui 2015-11-11 
'''

def addDistrictOrg(districtOrgName=orgInit['DftQuOrg'],cityName=orgInit['DftShiOrg']):
    if CommonIntf.getDbQueryResult(dbCommand="select * from ORGANIZATIONS t where t.orgname='%s'" % districtOrgName) is not None:
#         Log.LogOutput(level=LogLevel.INFO, message='待添加的区已经存在，无需添加')       
        return True
    else:
        orgObject = copy.deepcopy(SystemMgrPara.orgnizationObject)
        orgObject['departmentNoC']=CommonIntf.getDbQueryResult(dbCommand="select t.departmentno from ORGANIZATIONS t where t.orgname='%s'" % cityName)
        orgObject['departmentNoF']=CommonIntf.getDbQueryResult(dbCommand="select t.departmentno from ORGANIZATIONS t where t.orgname='%s'" % cityName)[0:2]
        orgObject['organization.orgLevel.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='网格分级', displayName='县（区）')
        orgObject['organization.orgName']= districtOrgName
        orgObject['organization.orgType.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='网格类型', displayName='行政区域')
        orgObject['organization.parentOrg.id']= CommonIntf.getDbQueryResult(dbCommand="select t.id from ORGANIZATIONS t where t.orgname='%s'" % cityName)
        response = renzhengzhongxin_post(url='/sysadmin/orgManage/ajaxAddOrganization', postdata=orgObject, username=Global.RenZhengZhongXinAdminUser, password=Global.RenZhengZhongXinAdminPass)
        if response.result is False:
            Log.LogOutput(level=LogLevel.DEBUG, message='添加区县级部门失败') 
            return False
        else:   
            Log.LogOutput(level=LogLevel.DEBUG, message='添加区县级部门成功') 
            return True

'''
    @功能：     添加区级职能部门
    @para: districtFuncOrgName：职能部门名称，默认为测试自动化区公安部
    districtOrgName:待添加的职能部门所在的区
    @return: 如果添加成功，则返回True；否则返回False  
    @ hongzenghui 2015-11-11 
'''

def addDistrictFuncOrg(districtFuncOrgName=orgInit['DftQuFuncOrg'],districtOrgName=orgInit['DftQuOrg'],funcOrgType=orgInit['DftQuFuncOrgType']):
    if CommonIntf.getDbQueryResult(dbCommand="select * from ORGANIZATIONS t where t.orgname='%s'" % districtFuncOrgName) is not None:
#         Log.LogOutput(level=LogLevel.INFO, message='待添加的区职能部门已经存在，无需添加')       
        return True
    else:
        orgObject = copy.deepcopy(SystemMgrPara.orgnizationObject)
        if districtFuncOrgName == orgInit['DftQuFuncOrg']:
            orgObject['departmentNoC']='2jt'
        else:
            orgObject['departmentNoC']='4jt'
        orgObject['departmentNoF']=CommonIntf.getDbQueryResult(dbCommand="select t.departmentno from ORGANIZATIONS t where t.orgname='%s'" % districtOrgName)
        orgObject['organization.functionalOrgType.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='职能部门类型', displayName='%s' % funcOrgType)
        orgObject['organization.orgLevel.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='网格分级', displayName='乡镇（街道）')
        orgObject['organization.orgName']= districtFuncOrgName
        orgObject['organization.orgType.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='网格类型', displayName='职能部门')
        orgObject['organization.parentOrg.id']= CommonIntf.getDbQueryResult(dbCommand="select t.id from ORGANIZATIONS t where t.orgname='%s'" % districtOrgName)
        response = renzhengzhongxin_post(url='/sysadmin/orgManage/ajaxAddOrganization', postdata=orgObject, username=Global.RenZhengZhongXinAdminUser, password=Global.RenZhengZhongXinAdminPass)
        if response.result is False:
            Log.LogOutput(level=LogLevel.DEBUG, message='添加区级职能部门失败') 
            return False
        else:   
            Log.LogOutput(level=LogLevel.DEBUG, message='添加区级职能部门成功') 
            return True

        
'''
    @功能：     添加街道部门
    @para: streetOrgName：部门名称，默认为测试自动化街道
    districtName：待添加的街道所在的区名称
    @return: 如果添加成功，则返回True；否则返回False  
    @ hongzenghui 2015-11-11 
'''

def addStreetOrg(streetOrgName=orgInit['DftJieDaoOrg'],districtName=orgInit['DftQuOrg']):
    if CommonIntf.getDbQueryResult(dbCommand="select * from ORGANIZATIONS t where t.orgname='%s'" % streetOrgName) is not None:
#         Log.LogOutput(level=LogLevel.INFO, message='待添加的街道已经存在，无需添加')       
        return True
    else:
        orgObject = copy.deepcopy(SystemMgrPara.orgnizationObject)
        orgObject['departmentNoC']=CommonIntf.getDbQueryResult(dbCommand="select t.departmentno from ORGANIZATIONS t where t.orgname='%s'" % districtName)
        orgObject['departmentNoF']=CommonIntf.getDbQueryResult(dbCommand="select t.departmentno from ORGANIZATIONS t where t.orgname='%s'" % districtName)[0:2]
        orgObject['organization.orgLevel.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='网格分级', displayName='乡镇（街道）')
        orgObject['organization.orgName']= streetOrgName
        orgObject['organization.orgType.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='网格类型', displayName='行政区域')
        orgObject['organization.parentOrg.id']= CommonIntf.getDbQueryResult(dbCommand="select t.id from ORGANIZATIONS t where t.orgname='%s'" % districtName)
        response = renzhengzhongxin_post(url='/sysadmin/orgManage/ajaxAddOrganization', postdata=orgObject, username=Global.RenZhengZhongXinAdminUser, password=Global.RenZhengZhongXinAdminPass)
        if response.result is False:
            Log.LogOutput(level=LogLevel.DEBUG, message='添加街道级部门失败') 
            return False
        else:   
            Log.LogOutput(level=LogLevel.DEBUG, message='添加街道级部门成功') 
            return True

'''
    @功能：     添加街道级职能部门
    @para: streetFuncOrgName：职能部门名称，默认为测试自动化街道公安部
    streetOrgName:待添加的职能部门所在的街道
    @return: 如果添加成功，则返回True；否则返回False  
    @ hongzenghui 2015-11-11 
'''

def addStreetFuncOrg(streetFuncOrgName=orgInit['DftJieDaoFuncOrg'],streetOrgName=orgInit['DftJieDaoOrg'],funcOrgType=orgInit['DftJieDaoFuncOrgType']):
    if CommonIntf.getDbQueryResult(dbCommand="select * from ORGANIZATIONS t where t.orgname='%s'" % streetFuncOrgName) is not None:
#         Log.LogOutput(level=LogLevel.INFO, message='待添加的街道职能部门已经存在，无需添加')       
        return True
    else:
        orgObject = copy.deepcopy(SystemMgrPara.orgnizationObject)
        if streetFuncOrgName == orgInit['DftJieDaoFuncOrg']:
            orgObject['departmentNoC']='3jt'
        else:
            orgObject['departmentNoC']='5jt'
        orgObject['departmentNoF']=CommonIntf.getDbQueryResult(dbCommand="select t.departmentno from ORGANIZATIONS t where t.orgname='%s'" % streetOrgName)
        orgObject['organization.functionalOrgType.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='职能部门类型', displayName='%s' % funcOrgType)
        orgObject['organization.orgLevel.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='网格分级', displayName='村（社区）')
        orgObject['organization.orgName']= streetFuncOrgName
        orgObject['organization.orgType.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='网格类型', displayName='职能部门')
        orgObject['organization.parentOrg.id']= CommonIntf.getDbQueryResult(dbCommand="select t.id from ORGANIZATIONS t where t.orgname='%s'" % streetOrgName)
        response = renzhengzhongxin_post(url='/sysadmin/orgManage/ajaxAddOrganization', postdata=orgObject, username=Global.RenZhengZhongXinAdminUser, password=Global.RenZhengZhongXinAdminPass)
        if response.result is False:
            Log.LogOutput(level=LogLevel.DEBUG, message='添加街道级职能部门失败') 
            return False
        else:   
            Log.LogOutput(level=LogLevel.DEBUG, message='添加街道职能部门成功') 
            return True
      
'''
    @功能：     添加社区部门
    @para: communityOrgName：部门名称，默认为测试社区
    streetName：待添加的社区所在的街道名称
    @return: 如果添加成功，则返回True；否则返回False  
    @ hongzenghui 2015-11-11 
'''

def addCommunityOrg(communityOrgName=orgInit['DftSheQuOrg'],streetName=orgInit['DftJieDaoOrg'],):
    if CommonIntf.getDbQueryResult(dbCommand="select * from ORGANIZATIONS t where t.orgname='%s'" % communityOrgName) is not None:
#         Log.LogOutput(level=LogLevel.INFO, message='待添加的社区已经存在，无需添加')       
        return True
    else:
        orgObject = copy.deepcopy(SystemMgrPara.orgnizationObject)
        orgObject['departmentNoC']=CommonIntf.getDbQueryResult(dbCommand="select t.departmentno from ORGANIZATIONS t where t.orgname='%s'" % streetName)
        orgObject['departmentNoF']=CommonIntf.getDbQueryResult(dbCommand="select t.departmentno from ORGANIZATIONS t where t.orgname='%s'" % streetName)[0:2]
        orgObject['organization.orgLevel.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='网格分级', displayName='村（社区）')
        orgObject['organization.orgName']= communityOrgName
        orgObject['organization.orgType.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='网格类型', displayName='行政区域')
        orgObject['organization.parentOrg.id']= CommonIntf.getDbQueryResult(dbCommand="select t.id from ORGANIZATIONS t where t.orgname='%s'" % streetName)
        response = renzhengzhongxin_post(url='/sysadmin/orgManage/ajaxAddOrganization', postdata=orgObject, username=Global.RenZhengZhongXinAdminUser, password=Global.RenZhengZhongXinAdminPass)
        if response.result is False:
            Log.LogOutput(level=LogLevel.DEBUG, message='添加社区级部门失败') 
            return False
        else:   
            Log.LogOutput(level=LogLevel.DEBUG, message='添加社区级部门成功') 
            return True
        
'''
    @功能：     添加网格部门
    @para: segmentOrgName：部门名称，默认为自动化网格
    communityName：待添加的网格所在的社区名称
    @return: 如果添加成功，则返回True；否则返回False  
    @ hongzenghui 2015-11-11 
'''

def addSegmentOrg(segmentOrgName=orgInit['DftWangGeOrg'],communityName=orgInit['DftSheQuOrg']):
    if CommonIntf.getDbQueryResult(dbCommand="select * from ORGANIZATIONS t where t.orgname='%s'" % segmentOrgName) is not None:
#         Log.LogOutput(level=LogLevel.INFO, message='待添加的网格已经存在，无需添加')       
        return True
    else:
        orgObject = copy.deepcopy(SystemMgrPara.orgnizationObject)
        deptNo = CommonIntf.getDbQueryResult(dbCommand="select max(t.departmentno) from ORGANIZATIONS t where t.parentid=(select p.id from ORGANIZATIONS p where p.orgname='%s')" % communityName)
        if deptNo is None:
            deptNoF="%s%s" % (CommonIntf.getDbQueryResult(dbCommand="select t.departmentno from ORGANIZATIONS t where t.orgname='%s'" % communityName),CommonIntf.getDbQueryResult(dbCommand="select t.departmentno from ORGANIZATIONS t where t.orgname='%s'" % communityName)[0:2])
        else:
            deptNoF=str(int(deptNo)+1)
        orgObject['departmentNoF']=deptNoF
        orgObject['organization.orgLevel.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='网格分级', displayName='片组片格')
        orgObject['organization.orgName']= segmentOrgName
        orgObject['organization.orgType.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='网格类型', displayName='行政区域')
        orgObject['organization.parentOrg.id']= CommonIntf.getDbQueryResult(dbCommand="select t.id from ORGANIZATIONS t where t.orgname='%s'" % communityName)
        response = renzhengzhongxin_post(url='/sysadmin/orgManage/ajaxAddOrganization', postdata=orgObject, username=Global.RenZhengZhongXinAdminUser, password=Global.RenZhengZhongXinAdminPass)
        if response.result is False:
            Log.LogOutput(level=LogLevel.DEBUG, message='添加网格级部门失败') 
            return False
        else:   
            Log.LogOutput(level=LogLevel.DEBUG, message='添加网格级部门成功') 
            return True

'''
    @功能：     添加默认组织
    @para: 
    @return: 成功返回True 失败返回False 
    @ hongzenghui 2015-11-23
'''

def addDefaultOrg():
    
    ret=addProvinceOrg() and addProvinceFuncOrg() and \
        addCityOrg() and addCityFuncOrg() and \
        addDistrictOrg()  and addDistrictFuncOrg() and \
        addDistrictFuncOrg(districtFuncOrgName=orgInit['DftQuMinBanFuncOrg'],districtOrgName=orgInit['DftQuOrg'],funcOrgType=orgInit['DftQuMinBanFuncOrgType']) and \
        addStreetOrg() and addStreetFuncOrg() and \
        addStreetFuncOrg(streetFuncOrgName=orgInit['DftJieDaoFuncOrg1'],streetOrgName=orgInit['DftJieDaoOrg'],funcOrgType=orgInit['DftJieDaoFuncOrgType1']) and \
        addCommunityOrg() and addSegmentOrg() and \
        addSegmentOrg(segmentOrgName=orgInit['DftWangGeOrg1'])

    if ret is True:
        return True
    else:
        return False
             
'''
    @功能：     添加用户
    @para: userObject：用户对象字典
    @return: 返回报文响应 
    @ hongzenghui 2015-11-12 
'''
       
def addUser(userObject):
    response = renzhengzhongxin_post(url='/sysadmin/userManage/addUser', postdata=userObject, username=Global.RenZhengZhongXinAdminUser, password=Global.RenZhengZhongXinAdminPass)
    return response

'''
    @功能：     添加初始化默认用户
    @para: 
    @return: 返回成功返回true,否则返回false
    @ hongzenghui 2015-11-12 
'''

def addDefaultUser():
    initResult = True
    userObject = copy.deepcopy(SystemMgrPara.userObject)
    #公共属性
    userObject['confirmPwd']= Global.NewUserDefaultPassword
    userObject['user.password']=Global.NewUserDefaultPassword
    userObject['mode']='add'
    userObject['roleIds']=CommonIntf.getDbQueryResult(dbCommand="select t.id from roles t where t.rolename='%s'" % roleInit['DftRoleName'])
    
    #省级用户添加    
    if CommonIntf.getDbQueryResult(dbCommand="select * from users t where t.username='%s'" % userInit['DftShengUser']) is not None:
#         Log.LogOutput(level=LogLevel.INFO, message='待添加的默认省级用户已经存在，无需添加')
        pass
    else:
        #省级用户属性
        userObject['organizationId']=CommonIntf.getDbQueryResult(dbCommand="select t.id from ORGANIZATIONS t where t.orgname='%s'" % orgInit['DftShengOrg'])
        userObject['user.mobile']=userInit['DftShengUserSJ']
        userObject['user.userName']=userInit['DftShengUser'].split('@')[0]
        userObject['user.name']=userInit['DftShengUserXM']
        userObject['user.vpdn']='@sg.vpdn.hz'
        response = addUser(userObject)
        if response.result is False:
            Log.LogOutput(level=LogLevel.DEBUG, message='添加省级用户失败') 
            initResult = False
        else:   
            Log.LogOutput(level=LogLevel.DEBUG, message='添加省级用户成功')
            
    #省级职能用户添加    
    if CommonIntf.getDbQueryResult(dbCommand="select * from users t where t.username='%s'" % userInit['DftShengFuncUser']) is not None:
#         Log.LogOutput(level=LogLevel.INFO, message='待添加的默认省级职能用户已经存在，无需添加')
        pass
    else:
        #省级职能用户属性
        userObject['organizationId']=CommonIntf.getDbQueryResult(dbCommand="select t.id from ORGANIZATIONS t where t.orgname='%s'" % orgInit['DftShengFuncOrg'])
        userObject['user.mobile']=userInit['DftShengFuncUserSJ']
        userObject['user.userName']=userInit['DftShengFuncUser'].split('@')[0]
        userObject['user.name']=userInit['DftShengFuncUserXM']
        userObject['user.vpdn']='@sg.vpdn.hz'
        response = addUser(userObject)
        if response.result is False:
            Log.LogOutput(level=LogLevel.DEBUG, message='添加省级职能用户失败') 
            initResult = False
        else:   
            Log.LogOutput(level=LogLevel.DEBUG, message='添加省级职能用户成功') 
            
    #市级用户添加    
    if CommonIntf.getDbQueryResult(dbCommand="select * from users t where t.username='%s'" % userInit['DftShiUser']) is not None:
#         Log.LogOutput(level=LogLevel.INFO, message='待添加的默认市级用户已经存在，无需添加')
        pass
    else:
        #市级用户属性
        userObject['organizationId']=CommonIntf.getDbQueryResult(dbCommand="select t.id from ORGANIZATIONS t where t.orgname='%s'" % orgInit['DftShiOrg'])
        userObject['user.mobile']=userInit['DftShiUserSJ']
        userObject['user.userName']=userInit['DftShiUser'].split('@')[0]
        userObject['user.name']=userInit['DftShiUserXM']
        userObject['user.vpdn']='@'
        response = addUser(userObject)
        if response.result is False:
            Log.LogOutput(level=LogLevel.DEBUG, message='添加市级用户失败') 
            initResult = False
        else:   
            Log.LogOutput(level=LogLevel.DEBUG, message='添加市级用户成功')
            
    #市级职能用户添加    
    if CommonIntf.getDbQueryResult(dbCommand="select * from users t where t.username='%s'" % userInit['DftShiFuncUser']) is not None:
#         Log.LogOutput(level=LogLevel.INFO, message='待添加的默认市级职能用户已经存在，无需添加')
        pass
    else:
        #省级职能用户属性
        userObject['organizationId']=CommonIntf.getDbQueryResult(dbCommand="select t.id from ORGANIZATIONS t where t.orgname='%s'" % orgInit['DftShiFuncOrg'])
        userObject['user.mobile']=userInit['DftShiFuncUserSJ']
        userObject['user.userName']=userInit['DftShiFuncUser'].split('@')[0]
        userObject['user.name']=userInit['DftShiFuncUserXM']
        userObject['user.vpdn']='@'
        response = addUser(userObject)
        if response.result is False:
            Log.LogOutput(level=LogLevel.DEBUG, message='添加市级职能用户失败') 
            initResult = False
        else:   
            Log.LogOutput(level=LogLevel.DEBUG, message='添加市级职能用户成功') 
    
    #区级用户添加    
    if CommonIntf.getDbQueryResult(dbCommand="select * from users t where t.username='%s'" % userInit['DftQuUser']) is not None:
#         Log.LogOutput(level=LogLevel.INFO, message='待添加的默认区级用户已经存在，无需添加')
        pass
    else:
        #区级用户属性
        userObject['organizationId']=CommonIntf.getDbQueryResult(dbCommand="select t.id from ORGANIZATIONS t where t.orgname='%s'" % orgInit['DftQuOrg'])
        userObject['user.mobile']=userInit['DftQuUserSJ']
        userObject['user.userName']=userInit['DftQuUser'].split('@')[0]
        userObject['user.name']=userInit['DftQuUserXM']
        userObject['user.vpdn']='@'
        response = addUser(userObject)
        if response.result is False:
            Log.LogOutput(level=LogLevel.DEBUG, message='添加区级用户失败') 
            initResult = False
        else:   
            Log.LogOutput(level=LogLevel.DEBUG, message='添加区级用户成功')
            
    #区级公安部职能用户添加    
    if CommonIntf.getDbQueryResult(dbCommand="select * from users t where t.username='%s'" % userInit['DftQuFuncUser']) is not None:
#         Log.LogOutput(level=LogLevel.INFO, message='待添加的默认区级职能用户已经存在，无需添加')
        pass
    else:
        #区级职能用户属性
        userObject['organizationId']=CommonIntf.getDbQueryResult(dbCommand="select t.id from ORGANIZATIONS t where t.orgname='%s'" % orgInit['DftQuFuncOrg'])
        userObject['user.mobile']=userInit['DftQuFuncUserSJ']
        userObject['user.userName']=userInit['DftQuFuncUser'].split('@')[0]
        userObject['user.name']=userInit['DftQuFuncUserXM']
        userObject['user.vpdn']='@'
        response = addUser(userObject)
        if response.result is False:
            Log.LogOutput(level=LogLevel.DEBUG, message='添加区级职能用户失败') 
            initResult = False
        else:   
            Log.LogOutput(level=LogLevel.DEBUG, message='添加区级职能用户成功')
            
    #区级名办中心职能用户添加    
    if CommonIntf.getDbQueryResult(dbCommand="select * from users t where t.username='%s'" % userInit['DftQuMinBanFuncUser']) is not None:
#         Log.LogOutput(level=LogLevel.INFO, message='待添加的默认区级职能用户已经存在，无需添加')
        pass
    else:
        #区级民办中心职能用户属性
        userObject['organizationId']=CommonIntf.getDbQueryResult(dbCommand="select t.id from ORGANIZATIONS t where t.orgname='%s'" % orgInit['DftQuMinBanFuncOrg'])
        userObject['user.mobile']=userInit['DftQuMinBanFuncUserSJ']
        userObject['user.userName']=userInit['DftQuMinBanFuncUser'].split('@')[0]
        userObject['user.name']=userInit['DftQuMinBanFuncUserXM']
        userObject['user.vpdn']='@'
        response = addUser(userObject)
        if response.result is False:
            Log.LogOutput(level=LogLevel.DEBUG, message='添加区级民办职能用户失败') 
            initResult = False
        else:   
            Log.LogOutput(level=LogLevel.DEBUG, message='添加区级民办职能用户成功')
            
    #街道用户添加    
    if CommonIntf.getDbQueryResult(dbCommand="select * from users t where t.username='%s'" % userInit['DftJieDaoUser']) is not None:
#         Log.LogOutput(level=LogLevel.INFO, message='待添加的默认街道用户已经存在，无需添加')
        pass
    else:
        #街道用户属性
        userObject['organizationId']=CommonIntf.getDbQueryResult(dbCommand="select t.id from ORGANIZATIONS t where t.orgname='%s'" % orgInit['DftJieDaoOrg'])
        userObject['user.mobile']=userInit['DftJieDaoUserSJ']
        userObject['user.userName']=userInit['DftJieDaoUser'].split('@')[0]
        userObject['user.name']=userInit['DftJieDaoUserXM']
        userObject['user.vpdn']='@'
        response = addUser(userObject)
        if response.result is False:
            Log.LogOutput(level=LogLevel.DEBUG, message='添加街道用户失败') 
            initResult = False
        else:   
            Log.LogOutput(level=LogLevel.DEBUG, message='添加街道用户成功')
            
    #街道公安部门职能用户添加    
    if CommonIntf.getDbQueryResult(dbCommand="select * from users t where t.username='%s'" % userInit['DftJieDaoFuncUser']) is not None:
#         Log.LogOutput(level=LogLevel.INFO, message='待添加的默认街道职能用户已经存在，无需添加')
        pass
    else:
        #街道职能用户属性
        userObject['organizationId']=CommonIntf.getDbQueryResult(dbCommand="select t.id from ORGANIZATIONS t where t.orgname='%s'" % orgInit['DftJieDaoFuncOrg'])
        userObject['user.mobile']=userInit['DftJieDaoFuncUserSJ']
        userObject['user.userName']=userInit['DftJieDaoFuncUser'].split('@')[0]
        userObject['user.name']=userInit['DftJieDaoFuncUserXM']
        userObject['user.vpdn']='@'
        response = addUser(userObject)
        if response.result is False:
            Log.LogOutput(level=LogLevel.DEBUG, message='添加街道职能用户失败') 
            initResult = False
        else:   
            Log.LogOutput(level=LogLevel.DEBUG, message='添加街道职能用户成功')
    
    #街道民政部门职能用户添加    
    if CommonIntf.getDbQueryResult(dbCommand="select * from users t where t.username='%s'" % userInit['DftJieDaoFuncUser1']) is not None:
#         Log.LogOutput(level=LogLevel.INFO, message='待添加的默认街道职能用户已经存在，无需添加')
        pass
    else:
        #街道职能用户属性
        userObject['organizationId']=CommonIntf.getDbQueryResult(dbCommand="select t.id from ORGANIZATIONS t where t.orgname='%s'" % orgInit['DftJieDaoFuncOrg1'])
        userObject['user.mobile']=userInit['DftJieDaoFuncUserSJ1']
        userObject['user.userName']=userInit['DftJieDaoFuncUser1'].split('@')[0]
        userObject['user.name']=userInit['DftJieDaoFuncUserXM1']
        userObject['user.vpdn']='@'
        response = addUser(userObject)
        if response.result is False:
            Log.LogOutput(level=LogLevel.DEBUG, message='添加街道职能用户1失败') 
            initResult = False
        else:   
            Log.LogOutput(level=LogLevel.DEBUG, message='添加街道职能用户1成功')
                    
    #社区用户添加    
    if CommonIntf.getDbQueryResult(dbCommand="select * from users t where t.username='%s'" % userInit['DftSheQuUser']) is not None:
#         Log.LogOutput(level=LogLevel.INFO, message='待添加的默认社区用户已经存在，无需添加')
        pass
    else:
        #社区用户属性
        userObject['organizationId']=CommonIntf.getDbQueryResult(dbCommand="select t.id from ORGANIZATIONS t where t.orgname='%s'" % orgInit['DftSheQuOrg'])
        userObject['user.mobile']=userInit['DftSheQuUserSJ']
        userObject['user.userName']=userInit['DftSheQuUser'].split('@')[0]
        userObject['user.name']=userInit['DftSheQuUserXM']
        userObject['user.vpdn']='@'
        response = addUser(userObject)
        if response.result is False:
            Log.LogOutput(level=LogLevel.DEBUG, message='添加社区用户失败') 
            initResult = False
        else:   
            Log.LogOutput(level=LogLevel.DEBUG, message='添加社区用户成功')
            
    #网格用户添加    
    if CommonIntf.getDbQueryResult(dbCommand="select * from users t where t.username='%s'" % userInit['DftWangGeUser']) is not None:
#         Log.LogOutput(level=LogLevel.INFO, message='待添加的默认网格用户已经存在，无需添加')
        pass
    else:
        #网格用户属性
        userObject['organizationId']=CommonIntf.getDbQueryResult(dbCommand="select t.id from ORGANIZATIONS t where t.orgname='%s'" % orgInit['DftWangGeOrg'])
        userObject['user.mobile']=userInit['DftWangGeUserSJ']
        userObject['user.userName']=userInit['DftWangGeUser'].split('@')[0]
        userObject['user.name']=userInit['DftWangGeUserXM']
        userObject['user.vpdn']='@'
        response = addUser(userObject)
        if response.result is False:
            Log.LogOutput(level=LogLevel.DEBUG, message='添加网格用户失败') 
            initResult = False
        else:   
            Log.LogOutput(level=LogLevel.DEBUG, message='添加网格用户成功')
    #网格用户1添加 
    if CommonIntf.getDbQueryResult(dbCommand="select * from users t where t.username='%s'" % userInit['DftWangGeUser1']) is not None:
#         Log.LogOutput(level=LogLevel.INFO, message='待添加的默认网格用户1已经存在，无需添加')
        pass
    else:
        #网格用户属性
        userObject['organizationId']=CommonIntf.getDbQueryResult(dbCommand="select t.id from ORGANIZATIONS t where t.orgname='%s'" % orgInit['DftWangGeOrg1'])
        userObject['user.mobile']=userInit['DftWangGeUserSJ1']
        userObject['user.userName']=userInit['DftWangGeUser1'].split('@')[0]
        userObject['user.name']=userInit['DftWangGeUserXM1']
        userObject['user.vpdn']='@'
        response = addUser(userObject)
        if response.result is False:
            Log.LogOutput(level=LogLevel.DEBUG, message='添加网格用户1失败') 
            initResult = False
        else:   
            Log.LogOutput(level=LogLevel.DEBUG, message='添加网格用户1成功')
    return initResult

'''
    @功能：     添加线索大江东地区初始化默认用户
    @para: 
    @return: 返回成功返回true,否则返回false
    @ chenhui 2017-3-30 
'''

def addClueDefaultUser():
    initResult = True
    userObject = copy.deepcopy(SystemMgrPara.userObject)
    #公共属性
    userObject['confirmPwd']= Global.NewUserDefaultPassword
    userObject['user.password']=Global.NewUserDefaultPassword
    userObject['mode']='add'
    userObject['roleIds']=CommonIntf.getDbQueryResult(dbCommand="select t.id from roles t where t.rolename='%s'" % roleInit['DftRoleName'])
    
    #省级用户添加    
    if CommonIntf.getDbQueryResult(dbCommand="select * from users t where t.username='%s'" % clueUserInit['DftShengUser']) is not None:
#         Log.LogOutput(level=LogLevel.INFO, message='待添加的默认省级用户已经存在，无需添加')
        pass
    else:
        #省级用户属性
        userObject['organizationId']=CommonIntf.getDbQueryResult(dbCommand="select t.id from ORGANIZATIONS t where t.orgname='%s'" % clueOrgInit['DftShengOrg'])
        userObject['user.mobile']=clueUserInit['DftShengUserSJ']
        userObject['user.userName']=clueUserInit['DftShengUser'].split('@')[0]
        userObject['user.name']=clueUserInit['DftShengUserXM']
        userObject['user.vpdn']='@sg.vpdn.hz'
        response = addUser(userObject)
        if response.result is False:
            Log.LogOutput(level=LogLevel.DEBUG, message='添加省级用户失败') 
            initResult = False
        else:   
            Log.LogOutput(level=LogLevel.DEBUG, message='添加省级用户成功')
            
            
    #市级用户添加    
    if CommonIntf.getDbQueryResult(dbCommand="select * from users t where t.username='%s'" % clueUserInit['DftShiUser']) is not None:
#         Log.LogOutput(level=LogLevel.INFO, message='待添加的默认市级用户已经存在，无需添加')
        pass
    else:
        #市级用户属性
        userObject['organizationId']=CommonIntf.getDbQueryResult(dbCommand="select t.id from ORGANIZATIONS t where t.orgname='%s'" % clueOrgInit['DftShiOrg'])
        userObject['user.mobile']=clueUserInit['DftShiUserSJ']
        userObject['user.userName']=clueUserInit['DftShiUser'].split('@')[0]
        userObject['user.name']=userInit['DftShiUserXM']
        userObject['user.vpdn']='@'
        response = addUser(userObject)
        if response.result is False:
            Log.LogOutput(level=LogLevel.DEBUG, message='添加市级用户失败') 
            initResult = False
        else:   
            Log.LogOutput(level=LogLevel.DEBUG, message='添加市级用户成功')
            
    
    #区级用户添加    
    if CommonIntf.getDbQueryResult(dbCommand="select * from users t where t.username='%s'" % clueUserInit['DftQuUser']) is not None:
#         Log.LogOutput(level=LogLevel.INFO, message='待添加的默认区级用户已经存在，无需添加')
        pass
    else:
        #区级用户属性
        userObject['organizationId']=CommonIntf.getDbQueryResult(dbCommand="select t.id from ORGANIZATIONS t where t.orgname='%s'" % clueOrgInit['DftQuOrg'])
        userObject['user.mobile']=clueUserInit['DftQuUserSJ']
        userObject['user.userName']=clueUserInit['DftQuUser'].split('@')[0]
        userObject['user.name']=clueUserInit['DftQuUserXM']
        userObject['user.vpdn']='@'
        response = addUser(userObject)
        if response.result is False:
            Log.LogOutput(level=LogLevel.DEBUG, message='添加区级用户失败') 
            initResult = False
        else:   
            Log.LogOutput(level=LogLevel.DEBUG, message='添加区级用户成功')
            
            
    #街道用户添加    
    if CommonIntf.getDbQueryResult(dbCommand="select * from users t where t.username='%s'" % clueUserInit['DftJieDaoUser']) is not None:
#         Log.LogOutput(level=LogLevel.INFO, message='待添加的默认街道用户已经存在，无需添加')
        pass
    else:
        #街道用户属性
        userObject['organizationId']=CommonIntf.getDbQueryResult(dbCommand="select t.id from ORGANIZATIONS t where t.orgname='%s'" % clueOrgInit['DftJieDaoOrg'])
        userObject['user.mobile']=clueUserInit['DftJieDaoUserSJ']
        userObject['user.userName']=clueUserInit['DftJieDaoUser'].split('@')[0]
        userObject['user.name']=clueUserInit['DftJieDaoUserXM']
        userObject['user.vpdn']='@'
        response = addUser(userObject)
        if response.result is False:
            Log.LogOutput(level=LogLevel.DEBUG, message='添加街道用户失败') 
            initResult = False
        else:   
            Log.LogOutput(level=LogLevel.DEBUG, message='添加街道用户成功')
            
                    
    #社区用户添加    
    if CommonIntf.getDbQueryResult(dbCommand="select * from users t where t.username='%s'" % clueUserInit['DftSheQuUser']) is not None:
#         Log.LogOutput(level=LogLevel.INFO, message='待添加的默认社区用户已经存在，无需添加')
        pass
    else:
        #社区用户属性
        userObject['organizationId']=CommonIntf.getDbQueryResult(dbCommand="select t.id from ORGANIZATIONS t where t.orgname='%s'" % clueOrgInit['DftSheQuOrg'])
        userObject['user.mobile']=clueUserInit['DftSheQuUserSJ']
        userObject['user.userName']=clueUserInit['DftSheQuUser'].split('@')[0]
        userObject['user.name']=clueUserInit['DftSheQuUserXM']
        userObject['user.vpdn']='@'
        response = addUser(userObject)
        if response.result is False:
            Log.LogOutput(level=LogLevel.DEBUG, message='添加社区用户失败') 
            initResult = False
        else:   
            Log.LogOutput(level=LogLevel.DEBUG, message='添加社区用户成功')
            
    #网格用户1添加    
    if CommonIntf.getDbQueryResult(dbCommand="select * from users t where t.username='%s'" % clueUserInit['DftWangGeUser1']) is not None:
#         Log.LogOutput(level=LogLevel.INFO, message='待添加的默认网格用户已经存在，无需添加')
        pass
    else:
        #网格用户1属性
        userObject['organizationId']=CommonIntf.getDbQueryResult(dbCommand="select t.id from ORGANIZATIONS t where t.orgname='%s'" % clueOrgInit['DftWangGeOrg1'])
        userObject['user.mobile']=clueUserInit['DftWangGeUserSJ1']
        userObject['user.userName']=clueUserInit['DftWangGeUser1'].split('@')[0]
        userObject['user.name']=clueUserInit['DftWangGeUserXM1']
        userObject['user.vpdn']='@'
        response = addUser(userObject)
        if response.result is False:
            Log.LogOutput(level=LogLevel.DEBUG, message='添加网格用户1失败') 
            initResult = False
        else:   
            Log.LogOutput(level=LogLevel.DEBUG, message='添加网格用户1成功')
    #网格用户2添加 
    if CommonIntf.getDbQueryResult(dbCommand="select * from users t where t.username='%s'" % clueUserInit['DftWangGeUser2']) is not None:
#         Log.LogOutput(level=LogLevel.INFO, message='待添加的默认网格用户1已经存在，无需添加')
        pass
    else:
        #网格用户属性
        userObject['organizationId']=CommonIntf.getDbQueryResult(dbCommand="select t.id from ORGANIZATIONS t where t.orgname='%s'" % clueOrgInit['DftWangGeOrg2'])
        userObject['user.mobile']=clueUserInit['DftWangGeUserSJ2']
        userObject['user.userName']=clueUserInit['DftWangGeUser2'].split('@')[0]
        userObject['user.name']=clueUserInit['DftWangGeUserXM2']
        userObject['user.vpdn']='@'
        response = addUser(userObject)
        if response.result is False:
            Log.LogOutput(level=LogLevel.DEBUG, message='添加网格用户2失败') 
            initResult = False
        else:   
            Log.LogOutput(level=LogLevel.DEBUG, message='添加网格用户2成功')
    return initResult

'''
    @功能：     初始化环境中的默认岗位、组织、用户
    @para: 
    @return: 返回成功返回true,否则返回false
    @ hongzenghui 2015-11-23 
'''
def initEnv():
    createDefaultRole()
    addDefaultOrg()
    addDefaultClueOrg()
    addDefaultUser()
    addClueDefaultUser()
    pass

'''
    @功能：     线索用户认证
    @para: 
    mobile：认证的手机号
    userName：认证的用户
    @return: 返回成功返回true,否则返回false
    @ hongzenghui 2016-11-23 
'''
def clueUserCertified(mobile=Global.XianSuoDftMobile,userName=userInit['DftQuUser']):
    userId = CommonIntf.getDbQueryResult(dbCommand="select t.id from USERS t where t.username='%s'" % userName)
    certifyDict = {
                   "clueMobile":mobile,
                   "userName":userName,
                   "userId":userId
                   }
    
    response = pinganjianshe_post(url='/clueManage/clueUserManage/systemUserCertified.action', postdata=certifyDict, username=Global.RenZhengZhongXinAdminUser, password=Global.RenZhengZhongXinAdminPass)
    if response.result is False:
        Log.LogOutput(level=LogLevel.DEBUG, message='线索用户认证失败') 
        return False
    else:
        Log.LogOutput(level=LogLevel.DEBUG, message='线索用户认证成功') 
        return True

'''
    @功能：     添加线索省级部门
    @para: provinceOrgName：部门名称，默认为浙江省
    @return: 如果添加成功，则返回True；否则返回False  
    @ chenhui 2017-3-29 
'''

def addClueProvinceOrg(provinceOrgName=clueOrgInit['DftShengOrg']):
    if CommonIntf.getDbQueryResult(dbCommand="select * from ORGANIZATIONS t where t.orgname='%s'" % provinceOrgName) is not None:
#         Log.LogOutput(level=LogLevel.INFO, message='待添加的省已经存在，无需添加')       
        return True
    else:
        orgObject = copy.deepcopy(SystemMgrPara.orgnizationObject)
        orgObject['departmentNoC']=clueOrgInit['DftShengOrgDepNo']
        orgObject['organization.orgLevel.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='网格分级', displayName='省')
        orgObject['organization.orgName']= provinceOrgName
        orgObject['organization.orgType.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='网格类型', displayName='行政区域')
        orgObject['organization.parentOrg.id']= '1'
        response = renzhengzhongxin_post(url='/sysadmin/orgManage/ajaxAddOrganization', postdata=orgObject, username=Global.RenZhengZhongXinAdminUser, password=Global.RenZhengZhongXinAdminPass)
        if response.result is False:
            Log.LogOutput(level=LogLevel.DEBUG, message='添加省级部门失败') 
            return False
        else:   
            Log.LogOutput(level=LogLevel.DEBUG, message='添加省级部门成功') 
            return True
        
'''
    @功能：     添加线索市级部门
    @para: cityOrgName：部门名称，默认为杭州市
    provinceName：待添加的市所在的省名称
    @return: 如果添加成功，则返回True；否则返回False  
    @ chenhui 2017-3-29 
'''

def addClueCityOrg(cityOrgName=clueOrgInit['DftShiOrg'],provinceName=clueOrgInit['DftShengOrg']):
    if CommonIntf.getDbQueryResult(dbCommand="select * from ORGANIZATIONS t where t.orgname='%s'" % cityOrgName) is not None:
#         Log.LogOutput(level=LogLevel.INFO, message='待添加的市已经存在，无需添加')       
        return True
    else:
        orgObject = copy.deepcopy(SystemMgrPara.orgnizationObject)
        orgObject['departmentNoC']=clueOrgInit['DftShiOrgDepNo'][-2:]
        orgObject['departmentNoF']=clueOrgInit['DftShengOrgDepNo']
        orgObject['organization.orgLevel.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='网格分级', displayName='市')
        orgObject['organization.orgName']= cityOrgName
        orgObject['organization.orgType.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='网格类型', displayName='行政区域')
        orgObject['organization.parentOrg.id']= CommonIntf.getDbQueryResult(dbCommand="select t.id from ORGANIZATIONS t where t.orgname='%s'" % provinceName)
        response = renzhengzhongxin_post(url='/sysadmin/orgManage/ajaxAddOrganization', postdata=orgObject, username=Global.RenZhengZhongXinAdminUser, password=Global.RenZhengZhongXinAdminPass)
        if response.result is False:
            Log.LogOutput(level=LogLevel.DEBUG, message='添加市级部门失败') 
            return False
        else:   
            Log.LogOutput(level=LogLevel.DEBUG, message='添加市级部门成功') 
            return True      
        
'''
    @功能：     添加线索区县部门
    @para: districtOrgName：部门名称，默认为杭州大江东产业集聚区
    cityName：待添加的区所在的市名称
    @return: 如果添加成功，则返回True；否则返回False  
    @ chenhui: 2017-3-29 
'''

def addClueDistrictOrg(districtOrgName=clueOrgInit['DftQuOrg'],cityName=clueOrgInit['DftShiOrg']):
    if CommonIntf.getDbQueryResult(dbCommand="select * from ORGANIZATIONS t where t.orgname='%s'" % districtOrgName) is not None:
#         Log.LogOutput(level=LogLevel.INFO, message='待添加的区已经存在，无需添加')       
        return True
    else:
        orgObject = copy.deepcopy(SystemMgrPara.orgnizationObject)
        orgObject['departmentNoC']=clueOrgInit['DftQuOrgDepNo'][-2:]
        orgObject['departmentNoF']=clueOrgInit['DftShiOrgDepNo']
        orgObject['organization.orgLevel.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='网格分级', displayName='县（区）')
        orgObject['organization.orgName']= districtOrgName
        orgObject['organization.orgType.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='网格类型', displayName='行政区域')
        orgObject['organization.parentOrg.id']= CommonIntf.getDbQueryResult(dbCommand="select t.id from ORGANIZATIONS t where t.orgname='%s'" % cityName)
        response = renzhengzhongxin_post(url='/sysadmin/orgManage/ajaxAddOrganization', postdata=orgObject, username=Global.RenZhengZhongXinAdminUser, password=Global.RenZhengZhongXinAdminPass)
#         print response.text
        if response.result is False:
            Log.LogOutput(level=LogLevel.DEBUG, message='添加区县级部门失败') 
            return False
        else:   
            Log.LogOutput(level=LogLevel.DEBUG, message='添加区县级部门成功') 
            return True     
        
'''
    @功能：     添加线索街道部门
    @para: streetOrgName：部门名称，默认为义蓬街道
    districtName：待添加的街道所在的区名称
    @return: 如果添加成功，则返回True；否则返回False  
    @ chenhui 2017-3-29 
'''

def addClueStreetOrg(streetOrgName=clueOrgInit['DftJieDaoOrg'],districtName=clueOrgInit['DftQuOrg']):
    if CommonIntf.getDbQueryResult(dbCommand="select * from ORGANIZATIONS t where t.orgname='%s'" % streetOrgName) is not None:
#         Log.LogOutput(level=LogLevel.INFO, message='待添加的街道已经存在，无需添加')       
        return True
    else:
        orgObject = copy.deepcopy(SystemMgrPara.orgnizationObject)
        orgObject['departmentNoC']=clueOrgInit['DftJieDaoOrgDepNo'][-3:]#'005'
        orgObject['departmentNoF']=clueOrgInit['DftQuOrgDepNo']#'330111'
        orgObject['organization.orgLevel.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='网格分级', displayName='乡镇（街道）')
        orgObject['organization.orgName']= streetOrgName
        orgObject['organization.orgType.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='网格类型', displayName='行政区域')
        orgObject['organization.parentOrg.id']= CommonIntf.getDbQueryResult(dbCommand="select t.id from ORGANIZATIONS t where t.orgname='%s'" % districtName)
        response = renzhengzhongxin_post(url='/sysadmin/orgManage/ajaxAddOrganization', postdata=orgObject, username=Global.RenZhengZhongXinAdminUser, password=Global.RenZhengZhongXinAdminPass)
#         print response.text
        if response.result is False:
            Log.LogOutput(level=LogLevel.DEBUG, message='添加街道级部门失败') 
            return False
        else:   
            Log.LogOutput(level=LogLevel.DEBUG, message='添加街道级部门成功') 
            return True
        
'''
    @功能：     添加线索社区部门
    @para: communityOrgName：部门名称，默认为义蓬村
    streetName：待添加的社区所在的街道名称
    @return: 如果添加成功，则返回True；否则返回False  
    @ chenhui 2017-3-29 
'''

def addClueCommunityOrg(communityOrgName=clueOrgInit['DftSheQuOrg'],streetName=clueOrgInit['DftJieDaoOrg'],):
    if CommonIntf.getDbQueryResult(dbCommand="select * from ORGANIZATIONS t where t.orgname='%s'" % communityOrgName) is not None:
#         Log.LogOutput(level=LogLevel.INFO, message='待添加的社区已经存在，无需添加')       
        return True
    else:
        orgObject = copy.deepcopy(SystemMgrPara.orgnizationObject)
        orgObject['departmentNoC']=clueOrgInit['DftSheQuOrgDepNo'][-3:]#'221'
        orgObject['departmentNoF']=clueOrgInit['DftJieDaoOrgDepNo']#'330111005'
        orgObject['organization.orgLevel.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='网格分级', displayName='村（社区）')
        orgObject['organization.orgName']= communityOrgName
        orgObject['organization.orgType.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='网格类型', displayName='行政区域')
        orgObject['organization.parentOrg.id']= CommonIntf.getDbQueryResult(dbCommand="select t.id from ORGANIZATIONS t where t.orgname='%s'" % streetName)
        response = renzhengzhongxin_post(url='/sysadmin/orgManage/ajaxAddOrganization', postdata=orgObject, username=Global.RenZhengZhongXinAdminUser, password=Global.RenZhengZhongXinAdminPass)
        if response.result is False:
            Log.LogOutput(level=LogLevel.DEBUG, message='添加社区级部门失败') 
            return False
        else:   
            Log.LogOutput(level=LogLevel.DEBUG, message='添加社区级部门成功') 
            return True
        
'''
    @功能：     添加网格部门
    @para: segmentOrgName：部门名称，默认为07232201义蓬村第一网格
    communityName：待添加的网格所在的社区名称
    @return: 如果添加成功，则返回True；否则返回False  
    @ hongzenghui 2015-11-11 
'''

def addClueSegmentOrg(segmentOrgName=clueOrgInit['DftWangGeOrg1'],communityName=clueOrgInit['DftSheQuOrg'],departmentNo=clueOrgInit['DftWangGeOrgDepNo1']):
    if CommonIntf.getDbQueryResult(dbCommand="select * from ORGANIZATIONS t where t.orgname='%s'" % segmentOrgName) is not None:
#         Log.LogOutput(level=LogLevel.INFO, message='待添加的网格已经存在，无需添加')       
        return True
    else:
        orgObject = copy.deepcopy(SystemMgrPara.orgnizationObject)
        orgObject['departmentNoC']=departmentNo[-3:]
        orgObject['departmentNoF']=clueOrgInit['DftSheQuOrgDepNo']#'330111005221'
        orgObject['organization.orgLevel.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='网格分级', displayName='片组片格')
        orgObject['organization.orgName']= segmentOrgName
        orgObject['organization.orgType.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='网格类型', displayName='行政区域')
        orgObject['organization.parentOrg.id']= CommonIntf.getDbQueryResult(dbCommand="select t.id from ORGANIZATIONS t where t.orgname='%s'" % communityName)
        response = renzhengzhongxin_post(url='/sysadmin/orgManage/ajaxAddOrganization', postdata=orgObject, username=Global.RenZhengZhongXinAdminUser, password=Global.RenZhengZhongXinAdminPass)
#         print response.text
        if response.result is False:
            Log.LogOutput(level=LogLevel.DEBUG, message='添加网格级部门失败') 
            return False
        else:   
            Log.LogOutput(level=LogLevel.DEBUG, message='添加网格级部门成功') 
            return True

'''
    @功能：     添加线索默认组织
    @para: 
    @return: 成功返回True 失败返回False 
    @ chenhui 2017-3-29
'''

def addDefaultClueOrg():
    ret=addClueProvinceOrg() and addClueCityOrg() and \
        addClueDistrictOrg()   and addClueStreetOrg() and \
        addClueCommunityOrg() and addSegmentOrg() and \
        addClueSegmentOrg(segmentOrgName=clueOrgInit['DftWangGeOrg1'],departmentNo=clueOrgInit['DftWangGeOrgDepNo1'])and \
        addClueSegmentOrg(segmentOrgName=clueOrgInit['DftWangGeOrg2'],departmentNo=clueOrgInit['DftWangGeOrgDepNo2'])

    if ret is True:
        return True
    else:
        return False