# -*- coding:UTF-8 -*-
'''
Created on 2015-12-22

@author: lhz
'''
from __future__ import unicode_literals
from COMMON import Log, CommonUtil
from CONFIG import InitDefaultPara
from CONFIG.Define import LogLevel
from CONFIG.InitDefaultPara import orgInit, userInit
from Interface.PingAnJianShe.Common import CommonIntf
from Interface.PingAnJianShe.XiaQuGuanLi import XiaQuGuanLiPara
from Interface.PingAnJianShe.pingAnJianSheHttpCommon import pinganjianshe_post, \
    pinganjianshe_get
import copy
import json
import time

#辖区管理--编辑辖区管理信息
def editXiaQuGuanLi(issueDict, username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "辖区管理--编辑辖区管理信息....")
    try:    
        response = pinganjianshe_post(url='/baseinfo/villageProfile/updateOrAddVillageProfile.action', postdata=issueDict , username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "编辑辖区管理信息成功")
            return True
        else:
                Log.LogOutput(LogLevel.ERROR, "编辑辖区管理信息失败")
                return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '编辑辖区管理信息过程中失败')
        return False  

#辖区管理--编辑辖区管理信息检查点
def editXiaQuGuanLi_check(paramedit,username = None , password = None):
    Log.LogOutput(LogLevel.DEBUG, "辖区管理--编辑辖区管理信息....")
    editParam_check = copy.deepcopy(XiaQuGuanLiPara.xiaQuGuanLiSearch) 
    editParam_check['organization.id'] =  InitDefaultPara.orgInit['DftShengOrgId']
    editParam_check['mode'] = 'upGrids'
    response = pinganjianshe_get(url='/baseinfo/villageProfile/getIntroductionAndOrgById.action', param = editParam_check, username=username, password=password)  
    responseDict = json.loads(response.content)  
    if responseDict['introduction'] == paramedit['introduction']  :
        Log.LogOutput(message = '查找到辖区管理信息')
        return True
    else:
        Log.LogOutput(message = "没查找到辖区管理信息")
        return False
    

#辖区管理--编辑领导班子介绍
def xiaQuGuanLiLeader(param,username = None,password = None):
    Log.LogOutput(LogLevel.DEBUG, "辖区管理--编辑领导班子介绍....")
    try:    
        response = pinganjianshe_post(url='/baseinfo/villageProfile/updateLeaderTeam.action', postdata=param , username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "编辑领导班子信息成功")
            return True
        else:
                Log.LogOutput(LogLevel.ERROR, "编辑领导班子信息失败")
                return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '编辑领导班子信息过程中失败')
        return False
   
#辖区管理--新增领导班子介绍
def xiaQuGuanLiLeaderAdd(param,username = None,password = None):
    Log.LogOutput(LogLevel.DEBUG, "辖区管理--新增领导班子介绍....")
    try:    
        response = pinganjianshe_post(url='/baseinfo/villageProfile/addLeaderTeam.action', postdata=param , username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "新增领导班子信息成功")
            return True
        else:
                Log.LogOutput(LogLevel.ERROR, "新增领导班子信息失败")
                return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '新增领导班子信息过程中失败')
        return False


#辖区管理--删除领导班子介绍
def xiaQuGuanLiLeaderDel (param,username = None,password = None):
    Log.LogOutput(LogLevel.DEBUG, "辖区管理--删除领导班子介绍....")
    try:    
        response = pinganjianshe_get(url='/baseinfo/villageProfile/deleteLeaderTeam.action', param=param , username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "删除领导班子信息成功")
            return True
        else:
                Log.LogOutput(LogLevel.ERROR, "删除领导班子信息失败")
                return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '删除领导班子信息过程中失败')
        return False
    
#组织机构--删除辖区队伍
def xiaQuGuanLiXQDWDel (param,username = None,password = None):
    Log.LogOutput(LogLevel.DEBUG, "辖区管理--删除领导班子介绍....")
    try:    
        response = pinganjianshe_get(url='/baseinfo/villageProfile/deleteLeaderTeamByIds.action', param=param , username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "删除领导班子信息成功")
            return True
        else:
                Log.LogOutput(LogLevel.ERROR, "删除领导班子信息失败")
                return False
    except Exception , e:
        Log.LogOutput(LogLevel.ERROR, '删除领导班子信息过程中失败')
        return False
    
    
#写辖区领导班子批量删除
def xiaQuGuanLiLeaderDelAll(username = None ,password = None):
    Log.LogOutput(LogLevel.DEBUG, "进入到辖区领导班子（辖区队伍）批量删除中....")
    try:
        ParamList = copy.deepcopy(XiaQuGuanLiPara.xiaQuDuiWuListParam)  
        ParamList['leaderTeamsVo.organization.id'] = InitDefaultPara.orgInit['DftShiOrgId']
        response = pinganjianshe_get(url='/baseinfo/villageProfile/findLeaderList.action',param=ParamList, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取的数据集合
        record = responseDict['records']
        if record == 0 :
            Log.LogOutput(level=LogLevel.DEBUG, message='辖区队伍列表无数据')
        else:
            for dictListItem in responseDict['rows']:
                deleteDict = {'leaderTeamsIds':dictListItem['id']}
                xiaQuGuanLiXQDWDel(deleteDict,username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '查找成员库信息过程中失败')
        return False  
    
    

#辖区管理--编辑基础信息
def xiaQuGuanLiBaseInforEdit(param,username = None,password = None):
    Log.LogOutput(LogLevel.DEBUG, "辖区管理--编辑基础信息....")
    try:   
        response = pinganjianshe_post(url='/baseinfo/villageProfile/updateOrAddVillageProfile.action', postdata=param , username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "编辑基础信息成功")
            return True
        else:
                Log.LogOutput(LogLevel.ERROR, "编辑基础信息失败")
                return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '编辑基础信息过程中失败')
        return False

#辖区管理--编辑图片
def uploadImage(param,files=None,username = None,password = None):
    Log.LogOutput(LogLevel.DEBUG, "辖区管理--编辑图片....")
    try:   
        response = pinganjianshe_post(url='/baseinfo/villageProfile/updateOrSaveVillageProfileImgUrl.action', postdata=param , files=files, username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "编辑图片成功")
            return True
        else:
            Log.LogOutput(LogLevel.ERROR, "编辑图片失败")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '编辑图片过程中失败')
        return False
    
#组织机构--综治组织新增
def xiaQuGuanLiLeaderOraginationAdd(param,username = None,password = None):
    Log.LogOutput(LogLevel.DEBUG, "组织机构--综治组织新增....")
    try:    
        response = pinganjianshe_post(url='/baseinfo/primaryOrgManage/addPrimaryOrg.action', postdata=param , username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "新增综治组织信息成功")
            return True
        else:
                Log.LogOutput(LogLevel.ERROR, "新增综治组织信息失败")
                return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '新增综治组织信息过程中失败')
        return False
    
    
#组织机构--综治组织编辑
def xiaQuGuanLiLeaderOraginationEdit(param,username = None,password = None):
    Log.LogOutput(LogLevel.DEBUG, "组织机构--综治组织修改....")
    try: 
        response = pinganjianshe_post(url='/baseinfo/primaryOrgManage/editPrimaryOrg.action', postdata=param , username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "修改综治组织信息成功")
            return True
        else:
                Log.LogOutput(LogLevel.ERROR, "修改综治组织信息失败")
                return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '修改综治组织信息过程中失败')
        return False  
    
#新增综治组织检查点
def checkxiaQuGuanLiLeaderOragination(param,username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "进入到辖区管理--组织机构--综治组织检查点开始....")
    ParamList = copy.deepcopy(XiaQuGuanLiPara.oragnizationList)  
    ParamList['primaryOrgVo.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
    ParamList['primaryOrgVo.teamClass.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='组织大类', displayName='综治组织')
    try:
        response = pinganjianshe_post(url='/baseinfo/primaryOrgManage/findPrimaryOrgs.action',postdata=ParamList, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取的数据集合
        listDict = responseDict['rows']
        #获取要查询的参数
        #对比查询出来的数据和要查询的是否一样
        if CommonUtil.findDictInDictlist(param,listDict) is True:
            Log.LogOutput(message = '名称在列表中存在')
            return True
        else:
            Log.LogOutput(message = "名称在列表中不存在")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '信息搜索过程中失败')
        return False      
    
      
#删除综治组织
def xiaQuGuanLiLeaderOraginationDel(param , username = None ,password = None):
        Log.LogOutput(LogLevel.DEBUG, "进入综治组织删除中....") 
        response = pinganjianshe_get(url='/baseinfo/primaryOrgManage/deletePrimaryOrg.action',param=param, username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "综治组织删除成功")
            return True
        else:
            Log.LogOutput(LogLevel.ERROR, "综治组织删除失败")
            return False    
    
#检查删除综治组织
def search_check(username = None ,password = None):
    Log.LogOutput(LogLevel.DEBUG, "进入到查找综治组织....")
    try:    
        ParamList = copy.deepcopy(XiaQuGuanLiPara.oragnizationList)  
        ParamList['primaryOrgVo.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        ParamList['primaryOrgVo.teamClass.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='组织大类', displayName='综治组织')
        ParamList['primaryOrgVo.displayLevel'] = "allJurisdiction"
        response = pinganjianshe_get(url='/baseinfo/primaryOrgManage/findPrimaryOrgs.action',param=ParamList, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取的数据集合
        record = responseDict['records']
        if record == 0 :
            Log.LogOutput(level=LogLevel.DEBUG, message='综治组织信息列表无数据')
            return True
        else:
            Log.LogOutput(level=LogLevel.DEBUG, message='综治组织信息存在数据') 
            return False 
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '综治组织信息数据搜索过程中失败')
        return False  
    
    
    
  
#查找列表所有id并删除
def xiaQuGuanLiLeaderOraginationDelAll(username = None ,password = None):
    Log.LogOutput(LogLevel.DEBUG, "进入到综治组织查找基础信息....")
    try:
        getListDict = copy.deepcopy(XiaQuGuanLiPara.oragnizationList)  
        getListDict['primaryOrgVo.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        getListDict['primaryOrgVo.teamClass.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='组织大类', displayName='综治组织')
        getListDict['primaryOrgVo.displayLevel'] = "allJurisdiction"
        response = pinganjianshe_get(url='/baseinfo/primaryOrgManage/findPrimaryOrgs.action',param=getListDict, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取的数据集合
        record = responseDict['records']
        if record == 0 :
            Log.LogOutput(level=LogLevel.DEBUG, message='基础信息列表无数据')
        else:
            for dictListItem in responseDict['rows']:
                deleteDict = {'selectedIds':dictListItem['id']}
                xiaQuGuanLiLeaderOraginationDel(deleteDict,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '查找基础信息过程中失败')
        return False      
    
#综治组织导出
def exportData(param,username = None,password = None):
    Log.LogOutput(LogLevel.DEBUG, "进入到导出数据开始....")
    response = pinganjianshe_post(url='/baseinfo/primaryOrgManage/downloadPrimaryOrg.action',postdata=param, username=username, password=password) 
    return response


#新增综治组织维护成员检查点
def checkxiaQuGuanLiLeaderOraginationMember(username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "进入到辖区管理--组织机构--综治组织维护成员检查点开始....")
    ParamList = copy.deepcopy(XiaQuGuanLiPara.oragnizationList)  
    ParamList['primaryOrgVo.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
    ParamList['primaryOrgVo.teamClass.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='组织大类', displayName='综治组织')
    try:
        response = pinganjianshe_post(url='/baseinfo/primaryOrgManage/findPrimaryOrgs.action',postdata=ParamList, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取的数据集合
        listDict = responseDict['rows']
        #获取添加的成员数量
        if listDict[0]['memberNum'] >0 :
            Log.LogOutput(message = '综治组织添加维护成员成功')
            return True
        else:
            Log.LogOutput(message = "综治组织添加维护成员失败")
            return False

    except Exception:
        Log.LogOutput(LogLevel.ERROR, '综治组织维护成员过程中失败')
        return False  



 
    
#组织机构--成员库 新增
def memberAdd(param,username = None,password = None):
    Log.LogOutput(LogLevel.DEBUG, "组织机构--成员库新增....")
    try:    
        response = pinganjianshe_post(url='/plugin/serviceTeam/serviceTeamMember/addServiceTeamMemberBase.action', postdata=param , username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "组织机构--成员库新增信息成功")
            return True
        else:
                Log.LogOutput(LogLevel.ERROR, "组织机构--成员库新增信息失败")
                return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '组织机构--成员库新增信息过程中失败')
        return False    
    
#组织机构--成员库 检查点
def  checkPersonList(param,username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "进入组织机构--成员库 检查点开始....")
    ParamList = copy.deepcopy(XiaQuGuanLiPara.personList)  
    ParamList['serviceTeamMemberVo.orgScope'] = 'sameGrade'
    ParamList['serviceTeamMemberVo.org.Id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
    ParamList['serviceTeamMemberVo.nameIsDuplicate'] = '0'
    try:
        response = pinganjianshe_post(url='/plugin/serviceTeam/serviceTeamMember/findServiceTeamMemberBases.action',postdata=ParamList, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取的数据集合
        listDict = responseDict['rows']
        #获取要查询的参数
        #对比查询出来的数据和要查询的是否一样
        if CommonUtil.findDictInDictlist(param,listDict) is True:
            Log.LogOutput(message = '名称在列表中存在')
            return True
        else:
            Log.LogOutput(message = "名称在列表中不存在")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '信息搜索过程中失败')
        return False      
        
    
#组织机构--修改成员库
def memberEdit(param,username = None,password = None):
    Log.LogOutput(LogLevel.DEBUG, "组织机构--成员库修改....")
    try:    
        response = pinganjianshe_post(url='/plugin/serviceTeam/serviceTeamMember/editServiceTeamMemberBase.action', postdata=param , username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "组织机构--成员库修改信息成功")
            return True
        else:
                Log.LogOutput(LogLevel.ERROR, "组织机构--成员库修改信息失败")
                return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '组织机构--成员库修改信息过程中失败')
        return False    
    
    
#组织机构--删除成员库    
def memberDel(param,username = None,password = None):
    Log.LogOutput(LogLevel.DEBUG, "组织机构--成员库删除....")   
    response = pinganjianshe_get(url='/plugin/serviceTeam/serviceTeamMember/deleteServiceTeamMember.action',param=param, username=username, password=password)
#     print response.text
    if isinstance(response.result,int):
        response.result=True
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "成员库删除成功")
            return True
    else:
            Log.LogOutput(LogLevel.ERROR, "成员库删除失败")
            return False    
        
#组织机构--成员库查找列表所有id并删除
def xiaQuGuanLiMemberDelAll(username = None ,password = None):
    Log.LogOutput(LogLevel.DEBUG, "进入到成员库基础信息....")
    try:
        ParamList = copy.deepcopy(XiaQuGuanLiPara.personList)  
        ParamList['serviceTeamMemberVo.orgScope'] = 'sameGrade'
        ParamList['serviceTeamMemberVo.org.Id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        ParamList['serviceTeamMemberVo.nameIsDuplicate'] = '0'
        response = pinganjianshe_get(url='/plugin/serviceTeam/serviceTeamMember/findServiceTeamMemberBases.action',param=ParamList, username=username, password=password)
#         print response.text
        responseDict = json.loads(response.text)
        #获取的数据集合
        record = responseDict['records']
        if record == 0 :
            Log.LogOutput(level=LogLevel.DEBUG, message='成员库列表无数据')
        else:
            for dictListItem in responseDict['rows']:
                deleteDict = {'selectedIds':dictListItem['baseId']}
                memberDel(deleteDict,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '查找成员库信息过程中失败')
        return False      
    
    
#检查删除成员库
def search_memberCheck(username = None ,password = None):
    Log.LogOutput(LogLevel.DEBUG, "进入到查找成员库....")
    try:    
        ParamList = copy.deepcopy(XiaQuGuanLiPara.personList)  
        ParamList['serviceTeamMemberVo.orgScope'] = 'sameGrade'
        ParamList['serviceTeamMemberVo.org.Id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        ParamList['serviceTeamMemberVo.nameIsDuplicate'] = '0'
        response = pinganjianshe_get(url='/plugin/serviceTeam/serviceTeamMember/findServiceTeamMemberBases.action',param=ParamList, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取的数据集合
        record = responseDict['records']
        if record == 0 :
            Log.LogOutput(level=LogLevel.DEBUG, message='成员库列表无数据')
            return True
        else:
            Log.LogOutput(level=LogLevel.DEBUG, message='成员库列表存在数据') 
            return False 
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '成员库列表信息数据搜索过程中失败')
        return False  
    
    
def search_memberOrg(param,username = None ,password = None):    
    Log.LogOutput(LogLevel.DEBUG, "进入到综治组织维护成员中....")
    try:    
        response = pinganjianshe_get(url='/plugin/serviceTeam/serviceTeamManage/addServiceTeamMember.action', param=param , username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "组织机构--综治组织维护成员成功")
            return True
        else:
                Log.LogOutput(LogLevel.ERROR, "组织机构--z综治组织维护成员失败")
                return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '组织机构--综治组织维护成员过程中失败')
        return False     
    
#组织机构--综治组织--维护成员信息 移除功能
def remove_memberOrg(param,username = None ,password = None):    
    Log.LogOutput(LogLevel.DEBUG, "进入到综治组织维护成员移除中....")
    try:    
        response = pinganjianshe_get(url='/plugin/serviceTeam/serviceTeamManage/removeServiceTeamMember.action', param=param , username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "组织机构--综治组织维护成员移除成功")
            return True
        else:
                Log.LogOutput(LogLevel.ERROR, "组织机构--综治组织维护成员移除失败")
                return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '组织机构--综治组织维护成员移除过程中失败')
        return False  
    
#新增综治组织移除维护成员检查点
def checkRemoveMember(username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "进入到辖区管理--组织机构--综治组织移除维护成员检查点开始....")
    ParamList = copy.deepcopy(XiaQuGuanLiPara.oragnizationList)  
    ParamList['primaryOrgVo.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
    ParamList['primaryOrgVo.teamClass.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='组织大类', displayName='综治组织')
    try:
        response = pinganjianshe_post(url='/baseinfo/primaryOrgManage/findPrimaryOrgs.action',postdata=ParamList, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取的数据集合
        listDict = responseDict['rows']
        #获取添加的成员数量
        if listDict[0]['memberNum'] == 0 :
            Log.LogOutput(message = '综治组织中没成员存在')
            return True
        else:
            Log.LogOutput(message = "综治组织有成员存在")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '综治组织维护成员过程中失败')
        return False      
    
# 组织机构--综治组织--维护成员信息  离职功能   
def memberLiZhi(param,username = None ,password = None):   
    Log.LogOutput(LogLevel.DEBUG, "进入到综治组织维护成员离职中....")
    try:    
        response = pinganjianshe_get(url='/plugin/serviceTeam/serviceTeamManage/updateServiceTeamMemberOnDuty.action', param=param , username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "组织机构--综治组织维护成员离职成功")
            return True
        else:
                Log.LogOutput(LogLevel.ERROR, "组织机构--综治组织维护成员离职失败")
                return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '组织机构--综治组织维护成员离职过程中失败')
        return False 
    
# 组织机构--综治组织--维护成员信息  重新担任功能   
def memberCXDR(param,username = None ,password = None):   
    Log.LogOutput(LogLevel.DEBUG, "进入到综治组织维护成员重新担任中....")
    try:    
        response = pinganjianshe_get(url='/plugin/serviceTeam/serviceTeamManage/updateServiceTeamMemberOnDuty.action', param=param , username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "组织机构--综治组织维护成员重新担任成功")
            return True
        else:
                Log.LogOutput(LogLevel.ERROR, "组织机构--综治组织维护成员重新担任失败")
                return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '组织机构--综治组织维护成员重新担任过程中失败')
        return False     
    
# 组织机构--辖区队伍  导出功能   
def exportXqDW(param,username = None ,password = None): 
    Log.LogOutput(LogLevel.DEBUG, "进入到组织机构辖区队伍导出中....")
    response = pinganjianshe_get(url='/baseinfo/villageProfile/downloadLeader.action', param=param , username=username, password=password)
    return response    

#组织机构--服务团队 新增
def addTeam(param,username = None ,password = None): 
    Log.LogOutput(LogLevel.DEBUG, "进入到组织机构服务团队新增中....")
    try:    
        response = pinganjianshe_post(url='/plugin/serviceTeam/serviceTeamManage/addServiceTeam.action', postdata=param , username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "组织机构--服务团队新增成功")
            return True
        else:
            Log.LogOutput(LogLevel.ERROR, "组织机构--服务团队新增失败")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '组织机构--服务团队新增过程中失败')
        return False       
    
#组织机构--服务团队 修改
def editTeam(param,username = None ,password = None): 
    Log.LogOutput(LogLevel.DEBUG, "进入到组织机构服务团队新增中....")
    try:    
        response = pinganjianshe_post(url='/plugin/serviceTeam/serviceTeamManage/editServiceTeam.action', postdata=param , username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "组织机构--服务团队修改成功")
            return True
        else:
                Log.LogOutput(LogLevel.ERROR, "组织机构--服务团队修改失败")
                return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '组织机构--服务团队修改过程中失败')
        return False 
   
            
def teamList(param,username = None ,password = None): 
    Log.LogOutput(LogLevel.DEBUG, "进入到组织机构服务团队列表中....")
    try:
        ParamList = copy.deepcopy(XiaQuGuanLiPara.TeamList)
        ParamList['serviceTeamVo.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        ParamList['serviceTeamVo.displayLevel'] = 'sameGrade'
        ParamList['serviceTeamVo.logOut'] = 0
        response = pinganjianshe_get(url='/plugin/serviceTeam/serviceTeamManage/findServiceTeams.action',param=ParamList, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取的数据集合
        listDict = responseDict['rows']
        #获取要查询的参数
        #对比查询出来的数据和要查询的是否一样
        if CommonUtil.findDictInDictlist(param,listDict) is True:
            Log.LogOutput(message = '名称在列表中存在')
            return True
        else:
           
            Log.LogOutput(message = "名称在列表中不存在")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '信息搜索过程中失败')
        return False  
    
    
def remove_team(param,username = None ,password = None):    
    Log.LogOutput(LogLevel.DEBUG, "进入到组织机构服务团队移除中....")
    try:    
        response = pinganjianshe_get(url='/plugin/serviceTeam/serviceTeamManage/deleteServiceTeam.action', param=param , username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "组织机构--组织机构服务团队移除成功")
            return True
        else:
                Log.LogOutput(LogLevel.ERROR, "组织机构服务团队移除失败")
                return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '组织机构服务团队移除过程中失败')
        return False


#服务团队批量删除
def xiaQuGuanLiTeamDelAll(username = None ,password = None):
    Log.LogOutput(LogLevel.DEBUG, "进入到组织机构服务团队批量删除....")
    try:
        ParamList = copy.deepcopy(XiaQuGuanLiPara.TeamList)  
        ParamList['serviceTeamVo.displayLevel'] = 'sameGrade'
        ParamList['serviceTeamVo.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        ParamList['serviceTeamVo.logOut'] = '0'
        response = pinganjianshe_get(url='/plugin/serviceTeam/serviceTeamManage/findServiceTeams.action',param=ParamList, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取的数据集合
        record = responseDict['records']
        if record == 0 :
            Log.LogOutput(level=LogLevel.DEBUG, message='服务团队列表无数据')
        else:
            for dictListItem in responseDict['rows']:
                deleteDict = {'selectedIds':dictListItem['id']}
                remove_team(deleteDict,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '查找服务团队信息过程中失败')
        return False      
    


def checkTeamrem(username = None ,password = None): 
    Log.LogOutput(LogLevel.DEBUG, "进入到检查组织机构服务团队是否移除成功中....")
    try:
        ParamList = copy.deepcopy(XiaQuGuanLiPara.TeamList)
        ParamList['serviceTeamVo.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        ParamList['serviceTeamVo.displayLevel'] = 'sameGrade'
        ParamList['serviceTeamVo.logOut'] = 0
        response = pinganjianshe_get(url='/plugin/serviceTeam/serviceTeamManage/findServiceTeams.action',param=ParamList, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取的数据条数
        record = responseDict['records']
        if record == 0 :
            Log.LogOutput(message = '组织机构服务团队移除成功')
            return True
        else :
            Log.LogOutput(message = '组织机构服务团队移除失败')
            return False
   
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '信息搜索过程中失败')
        return False   
    
# 组织机构--服务团队  导出功能   
def exportTeam(username = None ,password = None): 
    Log.LogOutput(LogLevel.DEBUG, "进入到组织机构服务团队  导出中....")
    ParamList = copy.deepcopy(XiaQuGuanLiPara.TeamList)
    ParamList['serviceTeamVo.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
    ParamList['serviceTeamVo.displayLevel'] = 'sameGrade'
    ParamList['serviceTeamVo.logOut'] = 0
    response = pinganjianshe_get(url='/plugin/serviceTeam/serviceTeamManage/exportServiceTeam.action', param = ParamList , username=username, password=password)
    return response  

# 组织机构--服务团队  解散功能   
def dismissTeam(param,username = None ,password = None): 
    Log.LogOutput(LogLevel.DEBUG, "进入到组织机构服务团队  解散中....")
    try:    
        response = pinganjianshe_post(url='/plugin/serviceTeam/serviceTeamManage/logOutServiceTeam.action', postdata = param , username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "组织机构--组织机构服务团队解散成功")
            return True
        else:
                Log.LogOutput(LogLevel.ERROR, "组织机构服务团队解散失败")
                return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '组织机构服务团队解散过程中失败')
        return False
    
#组织机构--成员库--维护对象
def weiHuDuiXiang(param,username = None ,password = None): 
    Log.LogOutput(LogLevel.DEBUG, "进入到组织机构成员库  维护对象中....")
    try:    
        response = pinganjianshe_get(url='/plugin/serviceTeam/serviceObject/addServiceObjectFromMember.action', param = param , username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "组织机构--成员库 维护对象成功")
            return True
        else:
                Log.LogOutput(LogLevel.ERROR, "组织机构--成员库 维护对象失败")
                return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '组织机构--成员库 维护对象过程中失败')
        return False

#组织机构--成员库--检测查重
def jianCeChaChong(param,username = None ,password = None): 
    Log.LogOutput(LogLevel.DEBUG, "进入到组织机构成员库  检测查重中....")
    try:    
        response = pinganjianshe_post(url='/plugin/serviceTeam/serviceTeamMember/newCombineServiceTeamMembers.action', postdata = param , username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "组织机构--成员库 检测查重成功")
            return True
        else:
                Log.LogOutput(LogLevel.ERROR, "组织机构--成员库 检测查重失败")
                return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '组织机构--成员库 检测查重过程中失败')
        return False

#组织机构--成员库--层级转移
def cengJiZhuanYi(param,username = None ,password = None): 
    Log.LogOutput(LogLevel.DEBUG, "进入到组织机构成员库  层级转移中....")
    try:    
        response = pinganjianshe_post(url='/plugin/serviceTeam/serviceTeamMember/changeOrg.action', postdata = param , username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "组织机构--成员库 层级转移成功")
            return True
        else:
                Log.LogOutput(LogLevel.ERROR, "组织机构--成员库 层级转移失败")
                return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '组织机构--成员库 层级转移过程中失败')
        return False


#组织机构--成员库 -- 导出
def exportMember(param,username = None ,password = None): 
    Log.LogOutput(LogLevel.DEBUG, "进入到组织机构成员库  导出中....")
    response = pinganjianshe_post(url='/plugin/serviceTeam/serviceTeamMember/exportServiceTeamMember.action', postdata = param , username=username, password=password)
    return response


#组织机构--成员库 -- 导入
def importMember(Param,files,username = None ,password = None): 
    Log.LogOutput(LogLevel.DEBUG, "进入到组织机构成员库  导入中....")
    response = pinganjianshe_post(url='/dataTransfer/importToDomain.action', postdata = Param ,files=files,username=username, password=password)
    return response   

#组织机构--成员库 -- 显示姓名重复记录
def lookNames(param,username = None ,password = None): 
    response = pinganjianshe_post(url='/plugin/serviceTeam/serviceTeamManage/findServiceTeams.action',postdata=param, username=username, password=password) 
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "组织机构--成员库 显示姓名重复记录成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, "组织机构--成员库 显示姓名重复记录失败")
        return False 


# 新增服务成员
def addFuWuChengYuan(FuWuChengYuanDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增服务成员开始")
    response = pinganjianshe_post(url='/plugin/serviceTeam/serviceTeamMember/addServiceTeamMemberBase.action', postdata=FuWuChengYuanDict, username=username, password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "新增服务成员成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "新增服务成员失败")
    return response

# 查看服务成员是否新增成功
def checkFuWuChengYuanCompany(companyDict, orgId=None, username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "查看服务成员开始")
        compDict = copy.deepcopy(XiaQuGuanLiPara.getFuWuChengYuan)
        compDict['serviceTeamMemberVo.org.Id']= InitDefaultPara.orgInit['DftWangGeOrgId']
        response = pinganjianshe_get(url='/plugin/serviceTeam/serviceTeamMember/findServiceTeamMemberBases.action', param=compDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict= responseDict['rows']
        if CommonUtil.findDictInDictlist(companyDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "查找服务成员成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查找服务成员失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查看失败')
            return False      
    
#         删除服务人员
def deleteFuWuRenYuan(FuWuRenYuanDict, username = None, password = None):  
        Log.LogOutput(LogLevel.INFO, "删除服务人员开始")
        response = pinganjianshe_get(url='/plugin/serviceTeam/serviceTeamMember/deleteServiceTeamMember.action', param=FuWuRenYuanDict,username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "删除服务人员成功")
        else:
            Log.LogOutput(LogLevel.ERROR, "删除服务人员失败")    
            return response    

# 新增实有单位
def addShiYouDanWei(ShiYouDanWeiDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增实有单位开始")
    response = pinganjianshe_post(url='/baseinfo/actualCompanyManage/maintainBaseInfo.action', postdata=ShiYouDanWeiDict, username=username, password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "新增实有单位成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "新增实有单位失败")
    return response


# 查看实有单位是否新增成功
def checkShiYouDanWeiCompany(companyDict, orgId=None, username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "查看实有单位开始")
        compDict = copy.deepcopy(XiaQuGuanLiPara.ChaKanShiYouDanWeiObject)
        compDict['organizationId']= InitDefaultPara.orgInit['DftWangGeOrgId']
        response = pinganjianshe_get(url='/baseinfo/actualCompanyManage/actualCompanyList.action', param=compDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict= responseDict['rows']
        if CommonUtil.findDictInDictlist(companyDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "查找实有单位成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查找实有单位失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查看失败')
            return False                  


def deleteAllPopulation():
    try:
#     删除实有单位
        compDict = copy.deepcopy(XiaQuGuanLiPara.ChaKanShiYouDanWeiObject)
        compDict['organizationId']= orgInit['DftWangGeOrgId']
        response = pinganjianshe_get(url='/baseinfo/actualCompanyManage/actualCompanyList.action', param=compDict)
        responseDict = json.loads(response.text)
        if responseDict['records'] == 0:
            Log.LogOutput(LogLevel.DEBUG, '无实有单位')  
        else:
                for dictListItem in responseDict['rows']:
                        deleteDict = {'locationIds':dictListItem['id']}
                        deleteShiYouDanWei(deleteDict)
                        
#      删除记录                
        compDict = copy.deepcopy(XiaQuGuanLiPara.getXunChangQingKuang)
        compDict['serviceRecordVo.organization.id']= orgInit['DftWangGeOrgId']
        response = pinganjianshe_get(url='/plugin/serviceTeam/serviceRecord/findServiceRecords.action', param=compDict)
        responseDict = json.loads(response.text)
        if responseDict['records'] == 0:
            Log.LogOutput(LogLevel.DEBUG, '无记录')  
        else:
                for dictListItem in responseDict['rows']:
                        deleteDict = {'recordIds':dictListItem['id']}
                        deletejilu(deleteDict)
                        
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '删除失败')
            return False     
                        
# 删除实有单位
def deleteShiYouDanWei(ShiYouDanWeiDict, username = None, password = None):  
        Log.LogOutput(LogLevel.INFO, "删除实有单位开始")
        response = pinganjianshe_get(url='/baseinfo/actualCompanyManage/deleteActualCompanyByIds.action', param=ShiYouDanWeiDict,username=username, password=password)
#         print response.text
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "删除实有单位成功")
        else:
            Log.LogOutput(LogLevel.ERROR, "删除实有单位失败")    
            return response    

# 删除记录
def deletejilu(jiluDict, username = None, password = None):  
        Log.LogOutput(LogLevel.INFO, "删除记录开始")
        response = pinganjianshe_get(url='/plugin/serviceTeam/serviceRecord/deleteServiceRecords.action', param=jiluDict,username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "删除记录成功")
        else:
            Log.LogOutput(LogLevel.ERROR, "删除记录失败")    
            return response                                 

# 删除民情日志
def deleteminqinrizhi(minqinrizhiDict, username = None, password = None):  
        Log.LogOutput(LogLevel.INFO, "删除民情日志开始")
        response = pinganjianshe_get(url='/peopleLog/peopleLogManage/deletePeopleLog.action', param=minqinrizhiDict,username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "删除民情日志成功")
        else:
            Log.LogOutput(LogLevel.ERROR, "删除民情日志失败")    
            return response      
        
# 新增记录
def addjilu(jiluDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增记录开始")
    response = pinganjianshe_post(url='/plugin/serviceTeam/serviceRecord/addServiceRecord.action', postdata=jiluDict, username=username, password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "新增记录成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "新增记录失败")
    return response

# 查看记录是否新增成功
def checkXunChangQingKuangiCompany(companyDict, OrgId=None, username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "查看记录开始")
        compDict = copy.deepcopy(XiaQuGuanLiPara.getXunChangQingKuang)
        compDict['serviceRecordVo.organization.id']= OrgId
        response = pinganjianshe_get(url='/plugin/serviceTeam/serviceRecord/findServiceRecords.action', param=compDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict= responseDict['rows']
        if CommonUtil.findDictInDictlist(companyDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "查看记录成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查看记录失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查看失败')
            return False  
        
# 修改记录    
def modifyxiugaijilu(modifyObject,username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "修改记录开始")
    response = pinganjianshe_post(url='/plugin/serviceTeam/serviceRecord/editServiceRecord.action', postdata=modifyObject,username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "修改记录成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "修改记录失败")
    return response

# 生成民情日志
def addscmingqinrizhi(scmingqinrizhiDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "生成民情日志开始")
    response = pinganjianshe_post(url='/peopleLog/peopleLogManage/maintainPeopleLogFromServiceRecord.action', postdata=scmingqinrizhiDict, username=username, password=password)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "生成民情日志成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "生成民情日志失败")
    return response

# 查看民情日志是否新增成功
def checkXunminqinrizhiCompany(companyDict, username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "查看民情日志开始")
        compDict = copy.deepcopy(XiaQuGuanLiPara.minqinrizhi)
        response = pinganjianshe_get(url='/peopleLog/peopleLogManage/peopleLogList.action', param=compDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict= responseDict['rows']
        if CommonUtil.findDictInDictlist(companyDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "查看民情日志成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查看民情日志失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查看失败')
            return False  

# 导出记录
def dldataShiYouRenKou(dldata, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导出实有单位开始..")
    response = pinganjianshe_post(url='/plugin/serviceTeam/serviceRecord/downloadServiceRecord.action', postdata=dldata, username=username, password = password)   
    return response                              

#高级搜索 期望中的[ps:输入列表中存在的数据进行查询]
def chaxundaibanrizhi(issueDict, username = None, password = None):
        getListDict = copy.deepcopy(XiaQuGuanLiPara.goajisousuo)
        getListDict['serviceRecordVo.organization.id']= InitDefaultPara.orgInit['DftWangGeOrgId']
        getListDict['serviceRecordVo.occurPlace']= issueDict['serviceRecord.occurPlace']
        response = pinganjianshe_get(url='/plugin/serviceTeam/serviceRecord/findServiceRecords.action',param=getListDict, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取的数据集合
        record = responseDict['records']
        if record == 0 :
            Log.LogOutput(level=LogLevel.DEBUG, message='记录库数据搜索失败')
            return False 
        else:
            Log.LogOutput(level=LogLevel.DEBUG, message='记录库数据搜索成功') 
            return True

#搜索 期望中的[ps:输入列表中不存在的数据进行查询]
def Companychaxundaibanrizhi(issueDict, company,username = None, password = None):
        getListDict = copy.deepcopy(XiaQuGuanLiPara.goajisousuo)
        getListDict['serviceRecordVo.organization.id']= InitDefaultPara.orgInit['DftWangGeOrgId']
        getListDict['serviceRecordVo.occurPlace']= issueDict['serviceRecord.occurPlace']
        getListDictCheck = copy.deepcopy(XiaQuGuanLiPara.getchaxundaibanrizhi) 
        getListDictCheck['subject']= company
        response = pinganjianshe_get(url='/plugin/serviceTeam/serviceRecord/findServiceRecords.action',param=getListDict, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取的数据集合
        listDict = responseDict['rows']
        record = responseDict['records']
        if record == 0 :
            Log.LogOutput(level=LogLevel.DEBUG, message='记录库数据搜索失败')
            return False 
        else:
                if CommonUtil.findDictInDictlist(getListDictCheck,listDict) is True:
                    Log.LogOutput(message = '不存在的数据匹配成功')
                    return True
                else:
                    Log.LogOutput(message = "不存在的数据匹配失败")
                return False
                Log.LogOutput(level=LogLevel.DEBUG, message='记录库数据搜索成功') 
                return True    
            
'''
    @功能删除辖区管理-记录库所有测试自动化省下的服务记录
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
    @author:  chenhui 2016-5-19
'''    
def deleteAllServiceRecord(year='2016',username=userInit['DftShengUser'],password='11111111'):
    try:
        #删除所有服务记录
        Log.LogOutput(message='正在清空%s年所有测试自动化省下的服务记录...'%year)
        listPara = copy.deepcopy(XiaQuGuanLiPara.serviceRecordListPara)
        listPara['serviceRecordVo.organization.id']=orgInit['DftShengOrgId']
        listPara['serviceRecordVo.displayYear']=year
        response = pinganjianshe_get(url='/plugin/serviceTeam/serviceRecord/findServiceRecords.action', param=listPara,username=username,password=password)
        responseDict = json.loads(response.text)
        if responseDict['records'] == 0:
            Log.LogOutput(LogLevel.DEBUG, '服务记录为空')
        else:
            for dictListItem in responseDict['rows']:
                deleteDict = {
                        'mode':'delete',
                        'recordIds':dictListItem['id']
                              }
                response=pinganjianshe_get(url='/plugin/serviceTeam/serviceRecord/deleteServiceRecords.action',param=deleteDict)
                if response.result is True:
                    Log.LogOutput(LogLevel.INFO,'删除成功')
                else:
                    Log.LogOutput(LogLevel.ERROR, '删除失败')   
    except Exception :
        Log.LogOutput(LogLevel.ERROR, '服务记录删除异常')
        return False     