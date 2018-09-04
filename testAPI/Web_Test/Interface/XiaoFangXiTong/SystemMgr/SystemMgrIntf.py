# -*- coding:UTF-8 -*-
'''
Created on 2015-11-10

@author: N-254
'''
from __future__ import unicode_literals
import copy
from COMMON import Time, Log
from CONFIG import Global
from CONFIG.Define import LogLevel

from Interface.XiaoFangXiTong.Common import CommonIntf
from Interface.XiaoFangXiTong.SystemMgr import SystemMgrPara
from Interface.XiaoFangXiTong.xiaoFangXiTongHttpCommon import xiaofang_post
from Interface.XiaoFangXiTong.Common.InitDefaultPara import roleInit, orgInit,\
    userInit

'''
    @功能：     添加消防默认岗位，岗位为全国层级
    @para: 
    @return: 如果添加成功，则返回True；否则返回False  
    @ hongzenghui 2016-6-8
'''
def createDefaultXiaoFangRole():
    result = True
    for roleName in roleInit.values():       
        if CommonIntf.getDbQueryResult(dbCommand="select * from roles t where t.rolename='%s'" % roleName) is not None:
            Log.LogOutput(level=LogLevel.INFO, message='待添加的岗位已经存在，无需添加')       
            continue
        else:
            roleObject = {}
            roleObject['mode']='copy'
            roleObject['role.createDate']= Time.getCurrentDateAndTime()
            roleObject['role.id']='1'
            roleObject['role.roleName']= roleName
            roleObject['role.workBenchType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName = '工作台类型', displayName = '中层') 
            if roleName=='测试自动化省岗位':
                roleObject['role.useInLevel.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='网格分级', displayName='省')     
            elif roleName == "测试自动化市岗位":
                roleObject['role.useInLevel.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='网格分级', displayName='市')
            elif roleName == "测试自动化区岗位":
                roleObject['role.useInLevel.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='网格分级', displayName='县（区）')
            elif roleName == "测试自动化街道岗位":
                roleObject['role.useInLevel.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='网格分级', displayName='乡镇（街道）')
            elif roleName == "测试自动化社区岗位":
                roleObject['role.useInLevel.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='网格分级', displayName='村（社区）')
            elif roleName == "测试自动化网格岗位":
                roleObject['role.useInLevel.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='网格分级', displayName='片组片格')
            roleObject['role.roleLevel'] = 0 #常量，表示其他
            response = xiaofang_post(url='/sysadmin/roleManage/addRole.action', postdata=roleObject, username=Global.XiaoFangInfo['ShengXiaoFangXiTongUser'], password=Global.XiaoFangInfo['ShengXiaoFangXiTongPass'])
            if response.result is False:
                Log.LogOutput(level=LogLevel.DEBUG, message='%s岗位添加失败' % roleName)
                result = result and False 
            else:
                Log.LogOutput(level=LogLevel.DEBUG, message='%s岗位添加成功' % roleName) 
                result = result and True
    return result
    
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
        orgObject['departmentNoC']='96'
        orgObject['organization.orgLevel.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='网格分级', displayName='省')
        orgObject['organization.orgName']= provinceOrgName
        orgObject['organization.orgType.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='网格类型', displayName='行政区域')
        orgObject['organization.parentOrg.id']= '1'
        response = xiaofang_post(url='/sysadmin/orgManage/ajaxAddOrganization.action', postdata=orgObject, username=Global.RenZhengZhongXinAdminUser, password=Global.RenZhengZhongXinAdminPass)
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
        orgObject['departmentNoC']='0jt'
        orgObject['departmentNoF']=CommonIntf.getDbQueryResult(dbCommand="select t.departmentno from ORGANIZATIONS t where t.orgname='%s'" % provinceOrgName)
#         orgObject['organization.functionalOrgType.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='职能部门类型', displayName='%s' % funcOrgType)
        orgObject['organization.orgLevel.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='网格分级', displayName='市')
        orgObject['organization.orgName']= provinceFuncOrgName
        orgObject['organization.orgType.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='网格类型', displayName='职能部门')
        orgObject['organization.parentOrg.id']= CommonIntf.getDbQueryResult(dbCommand="select t.id from ORGANIZATIONS t where t.orgname='%s'" % provinceOrgName)
        response = xiaofang_post(url='/sysadmin/orgManage/ajaxAddOrganization.action', postdata=orgObject, username=Global.RenZhengZhongXinAdminUser, password=Global.RenZhengZhongXinAdminPass)
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
        response = xiaofang_post(url='/sysadmin/orgManage/ajaxAddOrganization.action', postdata=orgObject, username=Global.RenZhengZhongXinAdminUser, password=Global.RenZhengZhongXinAdminPass)
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
        response = xiaofang_post(url='/sysadmin/orgManage/ajaxAddOrganization.action', postdata=orgObject, username=Global.RenZhengZhongXinAdminUser, password=Global.RenZhengZhongXinAdminPass)
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
        response = xiaofang_post(url='/sysadmin/orgManage/ajaxAddOrganization.action', postdata=orgObject, username=Global.RenZhengZhongXinAdminUser, password=Global.RenZhengZhongXinAdminPass)
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
        response = xiaofang_post(url='/sysadmin/orgManage/ajaxAddOrganization.action', postdata=orgObject, username=Global.RenZhengZhongXinAdminUser, password=Global.RenZhengZhongXinAdminPass)
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
        response = xiaofang_post(url='/sysadmin/orgManage/ajaxAddOrganization.action', postdata=orgObject, username=Global.RenZhengZhongXinAdminUser, password=Global.RenZhengZhongXinAdminPass)
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
        response = xiaofang_post(url='/sysadmin/orgManage/ajaxAddOrganization.action', postdata=orgObject, username=Global.RenZhengZhongXinAdminUser, password=Global.RenZhengZhongXinAdminPass)
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
        response = xiaofang_post(url='/sysadmin/orgManage/ajaxAddOrganization.action', postdata=orgObject, username=Global.RenZhengZhongXinAdminUser, password=Global.RenZhengZhongXinAdminPass)
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
        response = xiaofang_post(url='/sysadmin/orgManage/ajaxAddOrganization.action', postdata=orgObject, username=Global.RenZhengZhongXinAdminUser, password=Global.RenZhengZhongXinAdminPass)
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
    response = xiaofang_post(url='/sysadmin/userManage/addUser.action', postdata=userObject, username=Global.RenZhengZhongXinAdminUser, password=Global.RenZhengZhongXinAdminPass)
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
    
    #省级用户添加    
    if CommonIntf.getDbQueryResult(dbCommand="select * from users t where t.username='%s'" % userInit['DftShengUser']) is not None:
#         Log.LogOutput(level=LogLevel.INFO, message='待添加的默认省级用户已经存在，无需添加')
        pass
    else:
        #省级用户属性
        userObject['organizationId']=CommonIntf.getDbQueryResult(dbCommand="select t.id from ORGANIZATIONS t where t.orgname='%s'" % orgInit['DftShengOrg'])
        userObject['user.mobile']=userInit['DftShengUserSJ']
        userObject['user.workPhone']=userInit['DftShengUserSJ']
        userObject['user.userName']=userInit['DftShengUser'].split('@')[0]
        userObject['user.name']=userInit['DftShengUserXM']
        userObject['user.vpdn']='@sg.vpdn.hz'
        userObject['roleIds']=CommonIntf.getDbQueryResult(dbCommand="select t.id from roles t where t.rolename='%s'" % roleInit['DftShengRoleName'])
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
        userObject['user.workPhone']=userInit['DftShengFuncUserSJ']
        userObject['user.userName']=userInit['DftShengFuncUser'].split('@')[0]
        userObject['user.name']=userInit['DftShengFuncUserXM']
        userObject['user.vpdn']='@sg.vpdn.hz'
        userObject['roleIds']=CommonIntf.getDbQueryResult(dbCommand="select t.id from roles t where t.rolename='%s'" % roleInit['DftShengRoleName'])
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
        userObject['user.workPhone']=userInit['DftShiUserSJ']
        userObject['user.userName']=userInit['DftShiUser'].split('@')[0]
        userObject['user.name']=userInit['DftShiUserXM']
        userObject['user.vpdn']='@'
        userObject['roleIds']=CommonIntf.getDbQueryResult(dbCommand="select t.id from roles t where t.rolename='%s'" % roleInit['DftShiRoleName'])
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
        userObject['user.workPhone']=userInit['DftShiFuncUserSJ']
        userObject['user.userName']=userInit['DftShiFuncUser'].split('@')[0]
        userObject['user.name']=userInit['DftShiFuncUserXM']
        userObject['user.vpdn']='@'
        userObject['roleIds']=CommonIntf.getDbQueryResult(dbCommand="select t.id from roles t where t.rolename='%s'" % roleInit['DftShiRoleName'])
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
        userObject['user.workPhone']=userInit['DftQuUserSJ']
        userObject['user.userName']=userInit['DftQuUser'].split('@')[0]
        userObject['user.name']=userInit['DftQuUserXM']
        userObject['user.vpdn']='@'
        userObject['roleIds']=CommonIntf.getDbQueryResult(dbCommand="select t.id from roles t where t.rolename='%s'" % roleInit['DftQuRoleName'])
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
        userObject['user.workPhone']=userInit['DftQuFuncUserSJ']
        userObject['user.userName']=userInit['DftQuFuncUser'].split('@')[0]
        userObject['user.name']=userInit['DftQuFuncUserXM']
        userObject['user.vpdn']='@'
        userObject['roleIds']=CommonIntf.getDbQueryResult(dbCommand="select t.id from roles t where t.rolename='%s'" % roleInit['DftQuRoleName'])
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
        userObject['user.workPhone']=userInit['DftQuMinBanFuncUserSJ']
        userObject['user.userName']=userInit['DftQuMinBanFuncUser'].split('@')[0]
        userObject['user.name']=userInit['DftQuMinBanFuncUserXM']
        userObject['user.vpdn']='@'
        userObject['roleIds']=CommonIntf.getDbQueryResult(dbCommand="select t.id from roles t where t.rolename='%s'" % roleInit['DftQuRoleName'])
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
        userObject['user.workPhone']=userInit['DftJieDaoUserSJ']
        userObject['user.userName']=userInit['DftJieDaoUser'].split('@')[0]
        userObject['user.name']=userInit['DftJieDaoUserXM']
        userObject['user.vpdn']='@'
        userObject['roleIds']=CommonIntf.getDbQueryResult(dbCommand="select t.id from roles t where t.rolename='%s'" % roleInit['DftJieDaoRoleName'])
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
        userObject['user.workPhone']=userInit['DftJieDaoFuncUserSJ']
        userObject['user.userName']=userInit['DftJieDaoFuncUser'].split('@')[0]
        userObject['user.name']=userInit['DftJieDaoFuncUserXM']
        userObject['user.vpdn']='@'
        userObject['roleIds']=CommonIntf.getDbQueryResult(dbCommand="select t.id from roles t where t.rolename='%s'" % roleInit['DftJieDaoRoleName'])
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
        userObject['user.workPhone']=userInit['DftJieDaoFuncUserSJ1']
        userObject['user.userName']=userInit['DftJieDaoFuncUser1'].split('@')[0]
        userObject['user.name']=userInit['DftJieDaoFuncUserXM1']
        userObject['user.vpdn']='@'
        userObject['roleIds']=CommonIntf.getDbQueryResult(dbCommand="select t.id from roles t where t.rolename='%s'" % roleInit['DftJieDaoRoleName'])
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
        userObject['user.workPhone']=userInit['DftSheQuUserSJ']
        userObject['user.userName']=userInit['DftSheQuUser'].split('@')[0]
        userObject['user.name']=userInit['DftSheQuUserXM']
        userObject['user.vpdn']='@'
        userObject['roleIds']=CommonIntf.getDbQueryResult(dbCommand="select t.id from roles t where t.rolename='%s'" % roleInit['DftSheQuRoleName'])
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
        userObject['user.workPhone']=userInit['DftWangGeUserSJ']
        userObject['user.userName']=userInit['DftWangGeUser'].split('@')[0]
        userObject['user.name']=userInit['DftWangGeUserXM']
        userObject['user.vpdn']='@'
        userObject['roleIds']=CommonIntf.getDbQueryResult(dbCommand="select t.id from roles t where t.rolename='%s'" % roleInit['DftWangGeRoleName'])
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
        userObject['user.workPhone']=userInit['DftWangGeUserSJ1']
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
    @功能：     初始化环境中的默认岗位、组织、用户
    @para: 
    @return: 返回成功返回true,否则返回false
    @ hongzenghui 2015-11-23 
'''
def initEnv():
    createDefaultXiaoFangRole()
    addDefaultOrg()
    addDefaultUser()
    pass
            