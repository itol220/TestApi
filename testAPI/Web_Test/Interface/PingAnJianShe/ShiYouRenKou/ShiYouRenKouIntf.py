# -*- coding:UTF-8 -*-
'''
Created on 2015-11-16
@author: chenyan
'''
from __future__ import unicode_literals
from COMMON import Log, CommonUtil
from COMMON.CommonUtil import findDictInDictlist
from CONFIG.Define import LogLevel
from CONFIG.InitDefaultPara import orgInit, userInit
from Interface.PingAnJianShe.Common import CommonIntf
from Interface.PingAnJianShe.ShiYouRenKou import ShiYouRenKouPara
from Interface.PingAnJianShe.pingAnJianSheHttpCommon import pinganjianshe_post, \
    pinganjianshe_get
import copy
import json
from CONFIG import Global

'''
    @实有人口 > 户籍人口 
    @功能： 新增测试自动化网格下的户籍人口信息
    @para: 
    @return: 如果添加成功，则返回True；否则返回False  
'''    
def add_HuJiRenKou(HuJiRenKouDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增户籍人口开始..")        
    response = pinganjianshe_post(url='/baseinfo/householdStaff/maintainHouseholdStaffBaseInfo.action', postdata=HuJiRenKouDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增户籍人口成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增户籍人口失败")
    return response

'''  
    @功能： 修改测试自动化网格下的户籍人口信息
    @para: 
    @return: 如果修改成功，则返回True；否则返回False  
'''
def edit_ShiYouRenKou(HuJiRenKouDict, username = None, password = None):  
    Log.LogOutput(LogLevel.INFO, "修改户籍人口开始..")  
    response = pinganjianshe_post(url='/baseinfo/householdStaff/maintainHouseholdStaffBaseInfo.action', postdata=HuJiRenKouDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "修改人口成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "修改人口失败")
    return response

'''
    @功能： 新增测试自动化网格下的户籍人口的户主信息
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
'''    
def add_HuZhuMassage(HuJiRenKouDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增户籍人口的户主信息开始..")        
    response = pinganjianshe_post(url='/baseinfo/householdStaff/maintainHouseholdStaffBusinessInfo.action', postdata=HuJiRenKouDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增户籍人口的户主信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增户籍人口的户主信息失败")
    return response

'''  
    @功能： 取消测试自动化网格下的死亡户籍人口信息
    @para: 
    @return: 如果取消成功成功，则返回True；否则返回False  
'''
def deathcancel_ShiYouRenKou(HuJiRenKouDict, username = None, password = None):   
    Log.LogOutput(LogLevel.INFO, "取消人口死亡操作开始..")  
    response = pinganjianshe_get(url='/baseinfo/householdStaff/updateDeathOfHouseholdStaff.action', param=HuJiRenKouDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "取消死亡成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "取消死亡失败")
    return response

'''  
    @功能： 删除测试自动化网格下的户籍人口信息
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
'''
def delete_HuJiRenKou(HuJiRenKouDict, username = None, password = None):  
    Log.LogOutput(LogLevel.INFO, "删除户籍人口开始..")
    response = pinganjianshe_get(url='/baseinfo/householdStaff/deleteHouseholdStaff.action', param=HuJiRenKouDict,username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除户籍人口成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "删除户籍人口失败")    
    return response 

'''  
    @功能： 注销测试自动化网格下的户籍人口信息
    @para: 
    @return: 如果注销成功，则返回True；否则返回False  
'''
def logout_HuJiRenKou(HuJiRenKouDict, username = None, password = None):  
    Log.LogOutput(LogLevel.INFO, "注销户籍人口开始..")
    response = pinganjianshe_post(url='/baseinfo/householdStaff/updateEmphasiseById.action', postdata=HuJiRenKouDict,username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "注销人口成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "注销人口失败")     
    return response 

'''  
    @功能： 取消注销测试自动化网格下的户籍人口信息
    @para: 
    @return: 如果取消注销成功，则返回True；否则返回False  
'''
def logoutCancel_HuJiRenKou(HuJiRenKouDict, username = None, password = None):  
    Log.LogOutput(LogLevel.INFO, "取消注销户籍人口操作开始..")
    response = pinganjianshe_get(url='/baseinfo/householdStaff/updateEmphasiseById.action', param=HuJiRenKouDict,username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "取消注销成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "取消注销失败")     
    return response

'''  
    @功能： 搜索测试自动化网格下的户籍人口信息
    @para: 
    @return: 如果搜索成功，则返回True；否则返回False  
'''
def search_HuJiRenKou(renKouDict, orgId=None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "搜索户籍人口开始..")
    try:
        compDict = copy.deepcopy(ShiYouRenKouPara.getHuJiOrgDict)
        compDict['orgId']= orgId
        response = pinganjianshe_get(url='/baseinfo/householdStaff/findHouseholdStaffByOrgId.action', param=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(renKouDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "搜索人口成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "搜索人口失败")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查服务记录信息失败")
        return False

'''  
    @功能： 导入测试自动化网格下的人口信息
    @para: 
    @return: 如果导入成功，则返回True；否则返回False  
'''
def import_RenKou(data, files=None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导入人口信息开始..")
    response = pinganjianshe_post(url='/dataTransfer/importToDomain.action', postdata=data, files=files, username=username, password = password)
#    print response.text   
    return response

'''  
    @功能： 导出测试自动化网格下的户籍人口信息
    @para: 
    @return: 如果导出成功，则返回True；否则返回False  
'''    
def downLoad_HuJiRenKou(dldata, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导出户籍人口开始..")
    response = pinganjianshe_post(url='/baseinfo/householdStaff/downloadHouseholdStaff.action', postdata=dldata, username=username, password = password)   
    return response

'''  
    @功能： 新增测试自动化网格下辖区管理中组织机构的成员信息
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
'''
def add_FuWuChengYuan(fuWuDict, username = None, password = None):  
    Log.LogOutput(LogLevel.INFO, "新增成员库成员开始..")
    response = pinganjianshe_get(url='/plugin/serviceTeam/serviceTeamMember/addServiceTeamMemberBase.action', param=fuWuDict,username=username, password=password)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增成员库成员成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增成员库成员失败")     
    return response 

'''  
    @功能： 添加测试自动化网格下户籍人口中的服务成员信息
    @para: 
    @return: 如果添加成功，则返回True；否则返回False  
'''
def add_serviceMemberHuJiRenKou(serviceDict, username = None, password = None):  
    Log.LogOutput(LogLevel.INFO, "户籍人口添加服务成员开始..")
    response = pinganjianshe_get(url='/plugin/serviceTeam/router/routerManage/addObjectAndMemberRelation.action', param=serviceDict,username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "添加服务人员成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "添加服务人员失败")     
    return response 

'''  
    @功能： 删除测试自动化网格下户籍人口中的服务成员信息
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
'''
def delete_serviceMemberHuJiRenKou(serviceDict, username = None, password = None):  
    Log.LogOutput(LogLevel.INFO, "户籍人口中删除服务成员开始..")
    response = pinganjianshe_get(url='/plugin/serviceTeam/router/routerManage/deleteServiceMemberWithObject.action', param=serviceDict,username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除服务人员成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "删除服务人员失败")     
    return response 

'''  
    @功能： 测试自动化网格下户籍人口中卸任服务成员
    @para: 
    @return: 如果卸任成功，则返回True；否则返回False  
'''
def leave_serviceMemberHuJiRenKou(serviceDict, username = None, password = None):  
    Log.LogOutput(LogLevel.INFO, "户籍人口中卸任服务成员开始..")
    response = pinganjianshe_get(url='/plugin/serviceTeam/router/routerManage/leaveOrBackOnDuty.action', param=serviceDict,username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "卸任服务人员成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "卸任服务人员失败")     
    return response 

'''  
    @功能： 测试自动化网格下户籍人口中将卸任的服务成员重新担任
    @para: 
    @return: 如果重新担任成功，则返回True；否则返回False  
'''
def back_serviceMemberHuJiRenKou(serviceDict, username = None, password = None):  
    Log.LogOutput(LogLevel.INFO, "将户籍人口中卸任的服务成员重新担任开始..")
    response = pinganjianshe_get(url='/plugin/serviceTeam/router/routerManage/leaveOrBackOnDuty.action', param=serviceDict,username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "服务人员重新担任成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "服务人员重新担任失败")     
    return response 

'''  
    @功能：  检查测试自动化网格下户籍人口中卸任的服务人员信息
    @para:  getServiceMemberDict：检查时传入的确定唯一人口的信息
    @return: 如果检查成功，则返回True；否则返回False  
'''
def check_leaveServiceMember(serviceDict, objectId = None,onDuty=None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "户籍人口中检查服务人员开始..")
    try:
        compDict = copy.deepcopy(ShiYouRenKouPara.getLeaveServiceMemberDict)
        compDict['serviceMemberVo.objectId']= objectId
        compDict['serviceMemberVo.onDuty']= onDuty
        response = pinganjianshe_post(url='/plugin/serviceTeam/router/routerManage/findServiceMembersByServiceMemberVo.action', postdata=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(serviceDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到人口信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到人口信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查人口信息失败")
        return False

'''  
    @功能：  检查测试自动化网格下户籍人口中的服务人员信息
    @para:  getServiceMemberDict：检查时传入的确定唯一人口的信息
    @return: 如果检查成功，则返回True；否则返回False  
'''
def check_serviceMember(serviceDict, objectType=None, objectId = None,username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "户籍人口中检查服务人员开始..")
    try:
        compDict = copy.deepcopy(ShiYouRenKouPara.getServiceMemberDict)
        compDict['serviceMemberVo.objectType']= objectType
        compDict['serviceMemberVo.objectId']= objectId
        response = pinganjianshe_post(url='/plugin/serviceTeam/router/routerManage/findServiceMembersByServiceMemberVo.action', postdata=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(serviceDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到人口信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到人口信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查人口信息失败")
        return False

'''  
    @功能： 添加测试自动化网格下户籍人口中的监护人信息
    @para: 
    @return: 如果添加成功，则返回True；否则返回False  
'''
def add_serviceGuardersHuJiRenKou(GuardersDict, username = None, password = None):  
    Log.LogOutput(LogLevel.INFO, "户籍人口中添加监护人开始..")
    response = pinganjianshe_post(url='/plugin/serviceTeam/router/routerManage/addObjectAndGuardersRelation.action', postdata=GuardersDict,username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "添加监护人员成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "添加监护人员失败")     
    return response 

'''  
    @功能： 修改测试自动化网格下户籍人口中的监护人信息
    @para: 
    @return: 如果修改成功，则返回True；否则返回False  
'''
def edit_serviceGuardersHuJiRenKou(GuardersDict, username = None, password = None):  
    Log.LogOutput(LogLevel.INFO, "户籍人口中修改监护人开始..")
    response = pinganjianshe_post(url='/plugin/serviceTeam/router/routerManage/editObjectAndGuardersRelation.action', postdata=GuardersDict,username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "添加修改人员成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "添加修改人员失败")     
    return response 

'''  
    @功能： 删除测试自动化网格下户籍人口中的监护人信息
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
'''
def delete_serviceGuardersHuJiRenKou(GuardersDict, username = None, password = None):  
    Log.LogOutput(LogLevel.INFO, "户籍人口中添加监护人开始..")
    response = pinganjianshe_post(url='/plugin/serviceTeam/router/routerManage/deleteServiceGuardersWithObject.action', postdata=GuardersDict,username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除监护人员成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "删除监护人员失败")     
    return response 

'''  
    @功能： 添加测试自动化网格下户籍人口中的服务事件信息
    @para: 
    @return: 如果添加成功，则返回True；否则返回False  
'''
def add_serviceRecordHuJiRenKou(RecordDict, username = None, password = None):  
    Log.LogOutput(LogLevel.INFO, "户籍人口中添加服务事件开始..")
    response = pinganjianshe_post(url='/plugin/serviceTeam/serviceRecord/addServiceRecord.action', postdata=RecordDict,username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "添加服务事件成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "添加服务事件失败")     
    return response 

'''  
    @功能： 修改测试自动化网格下户籍人口中的服务事件信息
    @para: 
    @return: 如果修改成功，则返回True；否则返回False  
'''
def edit_serviceRecordHuJiRenKou(RecordDict, username = None, password = None):  
    Log.LogOutput(LogLevel.INFO, "户籍人口中修改服务事件开始..")
    response = pinganjianshe_post(url='/plugin/serviceTeam/serviceRecord/editServiceRecord.action', postdata=RecordDict,username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "修改服务事件成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "修改服务事件失败")     
    return response

'''  
    @功能： 删除测试自动化网格下户籍人口中的服务事件信息
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
'''
def delete_serviceRecordHuJiRenKou(RecordDict, username = None, password = None):  
    Log.LogOutput(LogLevel.INFO, "户籍人口中删除服务事件开始..")
    response = pinganjianshe_get(url='/plugin/serviceTeam/serviceRecord/deleteServiceRecords.action', param=RecordDict,username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除服务事件成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "删除服务事件失败")     
    return response

'''
    @功能：获取户籍人口对应的服务记录列表
    @return:    response
    @author:  chenhui 2016-05-19
'''   
def get_serviceRecordHuJiRenKou(listpara,username=userInit['DftWangGeUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "正在获取户籍人口对应的服务记录列表")
    response = pinganjianshe_get(url='/plugin/serviceTeam/serviceRecord/findServiceRecords.action',param=listpara,username=username,password=password)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "获取户籍人口对应的服务记录列表成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "获取户籍人口对应的服务记录列表失败")     
    return response


'''
    @功能：服务记录转事件
    @return:    response
    @author:  chenhui 2016-05-19
'''   
def serviceRecordToIssue(listpara,username=userInit['DftWangGeUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "服务记录转事件")
    response = pinganjianshe_post(url='/issues/issueManage/addServiceRecordIssue.action',postdata=listpara,username=username,password=password)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "服务记录转事件成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "服务记录转事件失败")     
    return response


'''  
    @功能：  检查测试自动化网格下户籍人口中的服务事件信息
    @para:  getServiceRecordDict：检查时传入的确定唯一性的信息
    @return: 如果检查成功，则返回True；否则返回False  
'''
def check_serviceRecord(RecordDict, objectIds=None, orgId = None,username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查户籍人口中的服务事件开始..")
    try:
        compDict = copy.deepcopy(ShiYouRenKouPara.getServiceRecordDict)
        compDict['objectIds']= objectIds
        compDict['serviceRecordVo.organization.id']= orgId
        response = pinganjianshe_get(url='/plugin/serviceTeam/serviceRecord/findServiceRecords.action', param=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(RecordDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到服务记录信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到服务记录信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查服务记录信息失败")
        return False

'''  
    @功能： 将测试自动化网格下的户籍人口转为流动人口
    @para: 
    @return: 如果转移成功，则返回True；否则返回False  
'''
def transfer_HuJiRenKou(HuJiRenKouDict, username = None, password = None):  
    Log.LogOutput(LogLevel.INFO, "户籍人口转为流动人口开始..")
    response = pinganjianshe_get(url='/baseinfo/householdStaff/toFloatingPopulation.action', param=HuJiRenKouDict,username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "转为流动人口成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "转为流动人口失败")     
    return response 

'''  
    @功能： 将测试自动化网格下的户籍人口转移到测试自动化网格1下
    @para: 
    @return: 如果转移成功，则返回True；否则返回False  
'''
def transfer_toWangGe(HuJiRenKouDict, username = None, password = None):  
    Log.LogOutput(LogLevel.INFO, "当前户籍人口信息转移到其他网格开始..")
    response = pinganjianshe_post(url='/transferManage/transfer.action', postdata=HuJiRenKouDict,username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "转移人口成功")
    else:
        Log.LogOutput(LogLevel.WARN, "转移人口失败")     
    return response 

'''  
    @功能： 检查测试自动化网格下的户籍人口中是否存在该id信息
    @para: getHuJiOrgDict：检查时需要传入的字典项
    @return: 如果检查成功，则返回True；否则返回False  
'''
def check_housePopulation(renKouDict, orgId=None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查户籍人口中是否有当前id信息开始..")
    try:
        compDict = copy.deepcopy(ShiYouRenKouPara.getHuJiOrgDict)
        compDict['orgId']= orgId
        response = pinganjianshe_get(url='/baseinfo/householdStaff/findHouseholdStaffByOrgId.action', param=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(renKouDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到户籍人口中存在该人口信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到户籍人口中存在该人口信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查人口信息失败")
        return False

'''  
    @功能： 检查测试自动化网格下的流动人口中是否存在该id信息
    @para: getLiuDongOrgDict：检查时需要传入的字典项
    @return: 如果检查成功，则返回True；否则返回False  
'''
def check_floatingPopulation(renKouDict, orgId=None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查流动人口中是否有当前id信息开始..")
    try:
        compDict = copy.deepcopy(ShiYouRenKouPara.getLiuDongOrgDict)
        compDict['organizationId']= orgId
        response = pinganjianshe_get(url='/baseinfo/floatingPopulationManage/findFloatingPopulations.action', param=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(renKouDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到流动人口中存在该人口信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到流动人口中存在该人口信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查人口信息失败")
        return False

'''  
    @功能： 检查测试自动化网格下的未落户人口中是否存在该id信息
    @para: getWeiLuoHuDict：检查时需要传入的字典项
    @return: 如果检查成功，则返回True；否则返回False  
'''    
def check_unsettledPopulation(renKouDict, orgId=None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查未落户人口中是否有当前id信息开始..")
    try:
        compDict = copy.deepcopy(ShiYouRenKouPara.getWeiLuoHuDict)
        compDict['orgId']= orgId
        response = pinganjianshe_get(url='/baseinfo/unsettledPopulationManage/getUnsettledPopulationByIdCardNo.action', param=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(renKouDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "未落户人口中存在该人口信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未落户人口中不存在该人口信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查人口信息失败")
        return False

'''  
    @功能： 检查测试自动化网格下的户籍人口信息
    @para: getHuJiOrgDict：检查时需要传入的字典项
    @return: 如果检查成功，则返回True；否则返回False  
''' 
def check_HuJiPopulation(renKouDict, orgId=None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查户籍人口信息开始..")
    try:
        compDict = copy.deepcopy(ShiYouRenKouPara.getHuJiOrgDict)
        compDict['orgId']= orgId
        response = pinganjianshe_get(url='/baseinfo/householdStaff/findHouseholdStaffByOrgId.action', param=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(renKouDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到户籍人口信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到户籍人口信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查户籍人口信息失败")
        return False
    
''' 
    @流动人口 
    @功能： 新增测试自动化网格下的流动人口信息
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
''' 
def add_LiuDongRenKou(LiuDongRenKouDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增流动人口开始..")
    response = pinganjianshe_post(url='/baseinfo/floatingPopulationManage/maintainFloatingPopulationBaseInfo.action', postdata=LiuDongRenKouDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增流动人口成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增流动人口失败")
    return response


'''
    @功能：修改流动人口
    @return:    response
    @author:  chenhui 2016-5-16
'''  
def upd_LiuDongRenKou(para,username=userInit['DftJieDaoUser'],password='11111111'):
    infostr='修改流动人口'
    Log.LogOutput(LogLevel.INFO, infostr)
    response = pinganjianshe_post(url='/baseinfo/floatingPopulationManage/maintainFloatingPopulationBaseInfo.action', postdata=para,username=username,password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, infostr+"成功")
    else:
            Log.LogOutput(LogLevel.DEBUG, infostr+"失败")
    return response

'''
    @功能：查询流动人口
    @return:    response
    @author:  chenhui 2016-5-16
'''  
def search_LiuDongRenKou(para,username=userInit['DftJieDaoUser'],password='11111111'):
    infostr='查询流动人口'
    Log.LogOutput(LogLevel.INFO, infostr)
    response = pinganjianshe_post(url='/baseinfo/floatingPopulationManage/searchFloatingPopulation.action', postdata=para,username=username,password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, infostr+"成功")
    else:
            Log.LogOutput(LogLevel.DEBUG, infostr+"失败")
    return response

'''
    @功能：检查数据是否存在于流动人口查询后的列表中
    @return:    response
    @author:  chenhui 2016-05-16
'''   
def checkLiuDongSearchList(checkpara,searchpara,username=userInit['DftWangGeUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "正在验证数据正确性")
    try:
        response = search_LiuDongRenKou(para=searchpara,username=username,password=password)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False
''' 
    @功能： 删除测试自动化网格下的流动人口信息
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
''' 
def delete_LiuDongRenKou(LiuDongRenKouDict, username = None, password = None):  
    Log.LogOutput(LogLevel.INFO, "删除流动人口开始..")
    response = pinganjianshe_get(url='/baseinfo/floatingPopulationManage/deleteFloatingPopulation.action', param=LiuDongRenKouDict,username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除流动人口成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "删除流动人口失败")    
    return response

''' 
    @功能： 将测试自动化网格下的流动人口信息转为户籍人口信息
    @para: 
    @return: 如果转移成功，则返回True；否则返回False  
''' 
def transfer_LiuDongRenKou(LiuDongRenKouDict, username = None, password = None):  
    Log.LogOutput(LogLevel.INFO, "将流动人口转为户籍人口开始..")
    response = pinganjianshe_get(url='/baseinfo/floatingPopulationManage/toHouseholdStaff.action', param=LiuDongRenKouDict,username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "转为户籍人口成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "转为户籍人口失败")     
    return response 

''' 
    @功能： 检查测试自动化网格下的流动人口信息
    @para: getLiuDongOrgDict：检查时需要传入的字典项
    @return: 如果检查成功，则返回True；否则返回False  
''' 
def check_LiuDongpopulation(renKouDict, orgId=None, username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "检查流动人口开始..")
        compDict = copy.deepcopy(ShiYouRenKouPara.getLiuDongOrgDict)
        compDict['organizationId']= orgId
        response = pinganjianshe_get(url='/baseinfo/floatingPopulationManage/findFloatingPopulations.action', param=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(renKouDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到流动人口信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到流动人口信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查流动人口信息失败")
        return False
    
'''  
    @功能： 导出测试自动化网格下的流动人口信息
    @para: 
    @return: 如果导出成功，则返回True；否则返回False  
'''    
def downLoad_LiuDongRenKou(dldata, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导出流动人口开始..")
    response = pinganjianshe_post(url='/baseinfo/floatingPopulationManage/downloadFloatingPopulation.action', postdata=dldata, username=username, password = password)   
    return response
    
'''
    @未落户人口 
    @功能： 新增测试自动化网格下的未落户人口信息
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
''' 
def add_WeiLuoHuRenKou(WeiLuoHuRenKouDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增未落户人口开始..")
    response = pinganjianshe_post(url='/baseinfo/unsettledPopulationManage/maintainUnsettledPopulationBaseInfo.action', postdata=WeiLuoHuRenKouDict, username=username, password=password)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增未落户人口成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增未落户人口失败")
    return response   

'''
    @功能：检查数据是否存在于未落户人口快速搜索后的列表中
    @return:    response
    @author:  chenhui 2016-05-16
'''   
def checkWeiLuoHuFastSearchList(checkpara,searchpara,username=userInit['DftWangGeUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "正在验证快速搜索结果正确性")
    try:
        response = pinganjianshe_get(url='/baseinfo/unsettledPopulationSearch/fastSearchUnsettledPopulation.action',param=searchpara,username=username,password=password)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False

'''
    @功能：检查数据是否存在于未落户人口高级搜索后的列表中
    @return:    response
    @author:  chenhui 2016-05-16
'''   
def checkWeiLuoHuSeniorSearchList(checkpara,searchpara,username=userInit['DftWangGeUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "正在验证高级查询结果正确性")
    try:
        response = pinganjianshe_get(url='/baseinfo/unsettledPopulationSearch/searchUnsettledPopulation.action',param=searchpara,username=username,password=password)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False
                
'''
    @功能： 删除测试自动化网格下的未落户人口信息
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
'''    
def delete_WeiLuoHuRenKou(WeiLuoHuRenKouDict, username = None, password = None):  
    Log.LogOutput(LogLevel.INFO, "删除未落户人口开始..")
    response = pinganjianshe_get(url='/baseinfo/unsettledPopulationManage/deleteUnsettledPopulation.action', param=WeiLuoHuRenKouDict,username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除未落户人口成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "删除未落户人口失败")    
    return response

'''
    @功能： 将测试自动化网格下的未落户人口信息转为落户人口
    @para: 
    @return: 如果转移成功，则返回True；否则返回False  
''' 
def transfer_WeiLuoHuRenKou(WeiLuoHuRenKouDict, username = None, password = None):  
    Log.LogOutput(LogLevel.INFO, "将未落户人口转移为落户人口开始")
    response = pinganjianshe_post(url='/baseinfo/householdStaff/maintainHouseholdStaffBaseInfo.action', postdata=WeiLuoHuRenKouDict,username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "转为落户人口成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "转为落户人口失败")     
    return response 

'''
    @功能： 检查测试自动化网格下的未落户人口信息
    @para: getWeiLuoHuDict：检查时需要传入的字典项
    @return: 如果检查成功，则返回True；否则返回False  
''' 
def check_WeiLuoHupopulation(renKouDict, orgId=None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查未落户人口开始..")
    try:
        compDict = copy.deepcopy(ShiYouRenKouPara.getWeiLuoHuDict)
        compDict['orgId']= orgId
        response = pinganjianshe_get(url='/baseinfo/unsettledPopulationManage/findUnsettledPopulations.action', param=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(renKouDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到未落户人口信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到未落户人口信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查未落户人口信息失败")
        return False

'''  
    @功能： 导出测试自动化网格下的未落户人口信息
    @para: 
    @return: 如果导出成功，则返回True；否则返回False  
'''    
def downLoad_WeiLuoHuRenKou(dldata, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导出未落户人口开始..")
    response = pinganjianshe_post(url='/baseinfo/unsettledPopulationSearch/downloadUnsettledPopulation.action', postdata=dldata, username=username, password = password)   
    return response


'''
    @境外人口
    @功能： 新增测试自动化网格下的境外人口信息
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
''' 
def add_JingWaiRenKou(JingWaiRenKouDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增境外人口开始..")
    response = pinganjianshe_post(url='/baseinfo/overseaPersonnelManage/maintainOverseaPersonnelBaseInfo.action', postdata=JingWaiRenKouDict, username=username, password=password)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增境外人口成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增境外人口失败")
    return response
'''
    @功能：检查数据是否存在于境外人员快速搜索后的列表中
    @return:    response
    @author:  chenhui 2016-05-16
'''   
def checkJingWaiFastSearchList(checkpara,searchpara,username=userInit['DftWangGeUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "正在验证快速搜索结果正确性")
    try:
        response = pinganjianshe_post(url='/baseinfo/overseaPersonnelSearch/fastSearchOverseaPersonnel.action',postdata=searchpara,username=username,password=password)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False

'''
    @功能：检查数据是否存在于境外人员高级搜索后的列表中
    @return:    response
    @author:  chenhui 2016-05-16
'''   
def checkJingWaiSeniorSearchList(checkpara,searchpara,username=userInit['DftWangGeUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "正在验证高级查询结果正确性")
    try:
        response = pinganjianshe_post(url='/baseinfo/overseaPersonnelSearch/searchOverseaPersonnel.action',postdata=searchpara,username=username,password=password)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False

'''
    @功能： 删除测试自动化网格下的境外人口信息
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
''' 
def delete_JingWaiRenKou(JinWaiRenKouDict, username = None, password = None):  
    Log.LogOutput(LogLevel.INFO, "删除境外人口开始..")
    response = pinganjianshe_get(url='/baseinfo/overseaPersonnelManage/deleteOverseaPersonnel.action', param=JinWaiRenKouDict,username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除境外人口成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "删除境外人口失败")    
    return response

'''
    @功能： 检查测试自动化网格下的境外人口信息
    @para: getJingWaiOrgDict：检查时需要传入的字典项
    @return: 如果检查成功，则返回True；否则返回False  
''' 
def check_JingWaipopulation(renKouDict, orgId=None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查境外人口开始..")
    try:
        compDict = copy.deepcopy(ShiYouRenKouPara.getJingWaiOrgDict)
        compDict['orgId']= orgId
        response = pinganjianshe_get(url='/baseinfo/overseaPersonnelManage/overseaPersonnelList.action', param=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(renKouDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到境外人口信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到境外人口信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查境外人口信息失败")
        return False

'''  
    @功能： 导出测试自动化网格下的境外人口信息
    @para: 
    @return: 如果导出成功，则返回True；否则返回False  
'''    
def downLoad_JingWaiRenKou(dldata, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导出境外人口开始..")
    response = pinganjianshe_post(url='/baseinfo/overseaPersonnelSearch/downloadOverseaPersonnel.action', postdata=dldata, username=username, password = password)   
    return response
 

'''
    @户籍家庭
    @功能： 新增测试自动化网格下的户籍家庭信息
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
''' 
def add_houseFamily(houseFamilyDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增户籍家庭开始..")
    response = pinganjianshe_get(url='/baseinfo/houseFamily/addHouseFamily.action', param=houseFamilyDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增户籍家庭成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增户籍家庭失败")
    return response   

'''
    @功能： 删除测试自动化网格下的户籍家庭信息
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
''' 
def delete_houseFamily(houseFamilyDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "删除户籍家庭开始..")
    response = pinganjianshe_get(url='/baseinfo/houseFamily/deleteByIds.action', param=houseFamilyDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除户籍家庭成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "删除户籍家庭失败")
    return response  

'''
    @功能： 检查测试自动化网格下的户籍家庭信息
    @para: getHouseFamilyDict：检查时需要传入的字典项
    @return: 如果检查成功，则返回True；否则返回False  
''' 
def check_houseFamily(familyDict, orgId=None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查户籍家庭开始..")
    try:
        compDict = copy.deepcopy(ShiYouRenKouPara.getHouseFamilyDict)
        compDict['orgId']= orgId
        response = pinganjianshe_get(url='/baseinfo/houseFamily/findHouseFamilyByOrgId.action', param=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(familyDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到户籍家庭信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到户籍家庭信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查户籍家庭信息失败")
        return False

'''
    @功能： 新增测试自动化网格下户籍家庭中的家庭成员信息
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
'''     
def add_houseMember(houseFamilyDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增家庭成员开始..")
    response = pinganjianshe_get(url='/baseinfo/houseFamily/addFamilyMemberById.action', param=houseFamilyDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增家庭成员成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增家庭成员失败")
    return response 

'''
    @功能： 检查测试自动化网格下户籍家庭中的家庭成员信息
    @para: getHouseMemberDict：检查时需要传入的字典项
    @return: 如果检查成功，则返回True；否则返回False  
''' 
def check_houseMember(familyDict, orgId=None, houseFamilyId=None,  username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查家庭成员开始..")
    try:
        compDict = copy.deepcopy(ShiYouRenKouPara.getHouseMemberDict)
        compDict['orgId'] = orgId
        compDict['houseFamily.id'] = houseFamilyId
        response = pinganjianshe_get(url='/baseinfo/householdStaff/findHouseholdStaffByOrgIdAndId.action', param=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(familyDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到家庭成员信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到家庭成员信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查家庭成员信息失败")
        return False
    
'''
    @功能： 移除测试自动化网格下户籍家庭中的家庭成员信息
    @para: 
    @return: 如果移除成功，则返回True；否则返回False  
''' 
def remove_houseMember(houseFamilyDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "移除家庭成员开始..")
    response = pinganjianshe_get(url='/baseinfo/houseFamily/removeHouseMember.action', param=houseFamilyDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "移除家庭成员成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "移除家庭成员失败")
    return response  

'''
    @功能： 转移测试自动化网格下户籍家庭中的家庭成员信息
    @para: 
    @return: 如果转移成功，则返回True；否则返回False  
''' 
def transfer_houseMember(houseFamilyDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "转移家庭成员开始..")
    response = pinganjianshe_get(url='/baseinfo/houseFamily/transferFamily.action', param=houseFamilyDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "转移家庭成员成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "转移家庭成员失败")
    return response     

'''
    @功能： 新增测试自动化网格下的走访记录
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
'''    
def add_viewDataManage(viewDataDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增走访记录开始..")        
    response = pinganjianshe_post(url='/baseinfo/viewdataManage/addViewdata.action', postdata=viewDataDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增走访记录成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增走访记录失败")
    return response

'''
    @功能： 修改测试自动化网格下的走访记录
    @para: 
    @return: 如果修改成功，则返回True；否则返回False  
'''    
def edit_viewDataManage(viewDataDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "修改走访记录开始..")        
    response = pinganjianshe_post(url='/baseinfo/viewdataManage/updateViewdata.action', postdata=viewDataDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "修改走访记录成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "修改走访记录失败")
    return response

'''
    @功能： 删除测试自动化网格下的走访记录
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
'''    
def delete_viewDataManage(viewDataDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "删除走访记录开始..")        
    response = pinganjianshe_get(url='/baseinfo/viewdataManage/deleteViewdata.action', param=viewDataDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除走访记录成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "删除走访记录失败")
    return response

'''
    @功能： 搜索测试自动化网格下走访记录中的走访记录信息
    @para: 
    @return: 如果搜索成功，则返回True；否则返回False  
''' 
def search_viewDataManage(viewDataDict, orgId=None, viewName=None,username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "搜索走访记录信息开始..")
    try:
        compDict = copy.deepcopy(ShiYouRenKouPara.searchViewDataDict)
        compDict['searchViewdataVo.orgId'] = orgId
        compDict['searchViewdataVo.viewName'] = viewName
        response = pinganjianshe_get(url='/baseinfo/viewdataManage/findViewdatasBySearchViewdataVo.action', param=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(viewDataDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "搜索到走访记录信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未搜索到走访记录信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "搜索走访记录信息失败")
        return False

'''
    @功能： 将测试自动化网格下的走访记录生产民情日志
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
'''    
def sent_viewDataManage(viewDataDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "走访记录生产民情日志开始..")        
    response = pinganjianshe_post(url='/plugin/sentimentLogManage/addSentimentLog.action', postdata=viewDataDict, username=username, password=password)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "生产民情日志成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "生产民情日志失败")
    return response

    
'''
    @功能： 检查测试自动化网格下走访记录中的走访记录信息
    @para: 
    @return: 如果检查成功，则返回True；否则返回False  
''' 
def check_viewDataManage(viewDataDict, orgId=None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查走访记录信息开始..")
    try:
        compDict = copy.deepcopy(ShiYouRenKouPara.getViewDataDict)
        compDict['searchViewdataVo.orgId'] = orgId
        response = pinganjianshe_get(url='/baseinfo/viewdataManage/findViewdatasBySearchViewdataVo.action', param=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(viewDataDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到走访记录信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到走访记录信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查走访记录信息失败")
        return False
    

'''
    @重点人员 > 刑满释放人员
    @功能： 新增测试自动化网格下的刑满释放人员信息
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
''' 
def add_xingManShiFang(xingManShiFangDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增刑满释放人员开始..")
    response = pinganjianshe_post(url='/baseinfo/positiveInfoManage/savePositiveInfoBaseInfo.action', postdata=xingManShiFangDict, username=username, password=password)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增刑满释放人员成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增刑满释放人员失败")
    return response  

'''
    @功能：检查数据是否存在于刑释解教人员快速搜索后的列表中
    @return:    response
    @author:  chenhui 2016-05-17
'''   
def checkXingShiFastSearchList(checkpara,searchpara,username=userInit['DftWangGeUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "正在验证快速搜索结果正确性")
    try:
        response = pinganjianshe_post(url='/baseinfo/searchPositiveInfo/fastSearch.action',postdata=searchpara,username=username,password=password)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False

'''
    @功能：检查数据是否存在于刑释解教人员高级搜索后的列表中
    @return:    response
    @author:  chenhui 2016-05-17
'''   
def checkXingShiSeniorSearchList(checkpara,searchpara,username=userInit['DftWangGeUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "正在验证高级结果正确性")
    try:
        response = pinganjianshe_post(url='/baseinfo/searchPositiveInfo/findPositiveInfosByQueryCondition.action',postdata=searchpara,username=username,password=password)
        responseDict=json.loads(response.text)
        print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False
        
'''  
    @功能： 测试自动化网格下的刑满释放人员信息取消关注
    @para: 
    @return: 如果注销成功，则返回True；否则返回False  
'''
def logout_xingManShiFang(xingManShiFangDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "刑满释放取消关注开始..")
    response = pinganjianshe_post(url='/baseinfo/positiveInfoManage/updateEmphasiseById.action', postdata=xingManShiFangDict,username=username, password=password)
    if response.result is True:       
        Log.LogOutput(LogLevel.INFO, "人员取消关注成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "人员取消关注失败")     
    return response         

'''
    @功能： 删除测试自动化网格下的刑满释放人员信息
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
''' 
def delete_xingManShiFang(xingManShiFangDict, username = None, password = None):  
    Log.LogOutput(LogLevel.INFO, "删除刑满释放人员开始..")
    response = pinganjianshe_get(url='/baseinfo/positiveInfoManage/deletePositiveInfoByIds.action', param=xingManShiFangDict,username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除刑满释放人员成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "删除刑满释放人员失败")    
    return response 

'''
    @功能： 检查测试自动化网格下的刑满释放人员信息
    @para: getPopulationDict：检查时需要传入的字典项
    @return: 如果检查成功，则返回True；否则返回False  
''' 
def check_xingManShiFang(xingManShiFangDict, orgId=None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查刑满释放人员开始..")
    try:
        compDict = copy.deepcopy(ShiYouRenKouPara.getPopulationDict)
        compDict['organizationId']= orgId
        response = pinganjianshe_post(url='/baseinfo/positiveInfoManage/positiveInfoList.action', postdata=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(xingManShiFangDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到刑满释放人员信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到刑满释放人员信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查刑满释放人员信息失败")
        return False

'''  
    @功能： 导出测试自动化网格下的刑满释放人员信息
    @para: 
    @return: 如果导出成功，则返回True；否则返回False  
'''    
def downLoad_XingShiRenYuan(dldata, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导出刑满释放人员开始..")
    response = pinganjianshe_post(url='/baseinfo/searchPositiveInfo/downloadPositiveInfo.action', postdata=dldata, username=username, password = password)   
    return response


'''
    @社区矫正人员
    @功能： 新增测试自动化网格下的社区矫正人员信息
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
''' 
def add_sheQuJiaoZheng(sheQuJiaoZhengDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增社区矫正人员开始..")
    response = pinganjianshe_post(url='/baseinfo/rectificativePersonManage/maintainRectificativePersonBaseInfo.action', postdata=sheQuJiaoZhengDict, username=username, password=password)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增社区矫正人员成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增社区矫正人员失败")
    return response   

'''
    @功能： 将测试自动化网格下的社区矫正人员转为刑满释放人员
    @para: 
    @return: 如果转移成功，则返回True；否则返回False  
''' 
def transfer_JiaoZhengRenYuan(sheQuJiaoZhengDict, username = None, password = None):  
    Log.LogOutput(LogLevel.INFO, "将社区矫正人员转为刑满释放人员开始..")
    response = pinganjianshe_post(url='/baseinfo/positiveInfoManage/savePositiveInfoBaseInfo.action', postdata=sheQuJiaoZhengDict,username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "转为刑满释放成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "转为刑满释放失败")     
    return response 

'''
    @功能： 删除测试自动化网格下的社区矫正人员信息
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
''' 
def delete_JiaoZhengRenYuan(sheQuJiaoZhengDict, username = None, password = None):  
    Log.LogOutput(LogLevel.INFO, "删除社区矫正人员开始..")
    response = pinganjianshe_get(url='/baseinfo/rectificativePersonManage/deleteRectificativePersonByIds.action', param=sheQuJiaoZhengDict,username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除社区矫正人员成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "删除社区矫正人员失败")    
    return response

'''
    @功能： 检查测试自动化网格下的社区矫正人员信息
    @para: getPopulationDict：检查时需要传入的字典项
    @return: 如果检查成功，则返回True；否则返回False  
''' 
def check_sheQuJiaoZheng(sheQuJiaoZhengDict, orgId=None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查社区矫正人员开始..")
    try:
        compDict = copy.deepcopy(ShiYouRenKouPara.getPopulationDict)
        compDict['organizationId']= orgId
        response = pinganjianshe_post(url='/baseinfo/rectificativePersonManage/rectificativePersonList.action', postdata=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
#         print response.text
        if CommonUtil.findDictInDictlist(sheQuJiaoZhengDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到社区矫正人员信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到社区矫正人员信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查社区矫正人员信息失败")
        return False

'''  
    @功能： 导出测试自动化网格下的社区矫正人员信息
    @para: 
    @return: 如果导出成功，则返回True；否则返回False  
'''    
def downLoad_JiaoZhengRenYuan(dldata, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导出社区矫正人员开始..")
    response = pinganjianshe_post(url='/baseinfo/searchRectificativePerson/downloadRectificativePerson.action', postdata=dldata, username=username, password = password)   
    return response
    
  
'''
    @精神病人员
    @功能： 新增测试自动化网格下的精神病人员信息
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
''' 
def add_jingShengBingRenYuan(psychosisDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增精神病人员开始..")
    response = pinganjianshe_post(url='/baseinfo/mentalPatientManage/maintainMentalPatientBaseInfo.action', postdata=psychosisDict, username=username, password=password)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增精神病人员成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增精神病人员失败")
    return response   

'''
    @功能： 删除测试自动化网格下的精神病人员信息
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
''' 
def delete_jingShengBingRenYuan(psychosisDict, username = None, password = None):  
    Log.LogOutput(LogLevel.INFO, "删除精神病人员开始..")
    response = pinganjianshe_get(url='/baseinfo/mentalPatientManage/deleteMentalPatientByIds.action', param=psychosisDict,username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除精神病人员成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "删除精神病人员失败")    
    return response


'''  
    @功能： 测试自动化网格下的精神病人员信息取消关注
    @para: 
    @return: 如果注销成功，则返回True；否则返回False  
'''
def logout_jingShengBingRenYuan(psychosisDict, username = None, password = None):  
    Log.LogOutput(LogLevel.INFO, "精神病人员取消关注开始..")
    response = pinganjianshe_post(url='/baseinfo/mentalPatientManage/updateEmphasiseById.action', postdata=psychosisDict,username=username, password=password)
#    print response.text
#     if response.result is True:
#         Log.LogOutput(LogLevel.INFO, "人员取消关注成功")
#     else:
#         Log.LogOutput(LogLevel.ERROR, "人员取消关注失败")     
    return response 


'''
    @功能： 检查测试自动化网格下的精神病人员信息
    @para: getPopulationDict：检查时需要传入的字典项
    @return: 如果检查成功，则返回True；否则返回False  
''' 
def check_jingShengBingRenYuan(psychosisDict, orgId=None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查精神病人员开始..")
    try:
        compDict = copy.deepcopy(ShiYouRenKouPara.getPopulationDict)
        compDict['organizationId']= orgId
        response = pinganjianshe_post(url='/baseinfo/mentalPatientManage/mentalPatientList.action', postdata=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(psychosisDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到精神病人员信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到精神病人员信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查精神病人员信息失败")
        return False

'''  
    @功能： 导出测试自动化网格下的精神病人员信息
    @para: 
    @return: 如果导出成功，则返回True；否则返回False  
'''    
def downLoad_jingShengBingRenYuan(dldata, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导出精神病人员开始..")
    response = pinganjianshe_post(url='/baseinfo/searchMentalPatient/downloadMentalPatient.action', postdata=dldata, username=username, password = password)   
    return response
    

'''
    @吸毒人员
    @功能： 新增测试自动化网格下的吸毒人员信息
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
''' 
def add_xiDuRenYuan(xiDuRenYuanDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增吸毒人员开始..")
    response = pinganjianshe_post(url='/baseinfo/druggyManage/maintainDruggyBaseInfo.action', postdata=xiDuRenYuanDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增吸毒人员成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增吸毒人员失败")
    return response  

'''
    @功能： 删除测试自动化网格下的吸毒人员信息
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
''' 
def delete_xiDuRenYuan(xiDuRenYuanDict, username = None, password = None):  
    Log.LogOutput(LogLevel.INFO, "删除吸毒人员开始..")
    response = pinganjianshe_get(url='/baseinfo/druggyManage/deleteDruggyByIds.action', param=xiDuRenYuanDict,username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除吸毒人员成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "删除吸毒人员失败")    
    return response

'''
    @功能： 检查测试自动化网格下的吸毒人员信息
    @para: getPopulationDict：检查时需要传入的字典项
    @return: 如果检查成功，则返回True；否则返回False  
''' 
def check_xiDuRenYuan(xiDuRenYuanDict, orgId=None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查吸毒人员开始..")
    try:
        compDict = copy.deepcopy(ShiYouRenKouPara.getPopulationDict)
        compDict['organizationId']= orgId
        response = pinganjianshe_post(url='/baseinfo/druggyManage/druggyList.action', postdata=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(xiDuRenYuanDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到吸毒人员信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到吸毒人员信息")
            return False    
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查吸毒人员信息失败")
        return False  

'''  
    @功能： 导出测试自动化网格下的吸毒人员信息
    @para: 
    @return: 如果导出成功，则返回True；否则返回False  
'''    
def downLoad_xiDuRenYuan(dldata, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导出吸毒人员开始..")
    response = pinganjianshe_post(url='/baseinfo/searchDruggy/downloadDruggy.action', postdata=dldata, username=username, password = password)   
    return response
    
    
'''
    @重点青少年
    @功能： 新增测试自动化网格下的重点青少人员信息
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
''' 
def add_zhongDianQingShaoNian(qingShaoNianDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增重点青少年开始..")
    response = pinganjianshe_post(url='/baseinfo/idleYouthManage/maintainIdleYouthBaseInfo.action', postdata=qingShaoNianDict, username=username, password=password)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增重点青少年成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增重点青少年失败")
    return response  

'''
    @功能： 删除测试自动化网格下的重点青少年信息
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
''' 
def delete_zhongDianQingShaoNian(qingShaoNianDict, username = None, password = None):  
    Log.LogOutput(LogLevel.INFO, "删除重点青少年开始..")
    response = pinganjianshe_get(url='/baseinfo/idleYouthManage/deleteIdleYouthByIds.action', param=qingShaoNianDict,username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除重点青少年成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "删除重点青少年失败")    
    return response 

'''
    @功能： 检查测试自动化网格下的重点青少年信息
    @para: getPopulationDict：检查时需要传入的字典项
    @return: 如果检查成功，则返回True；否则返回False  
''' 
def check_zhongDianQingShaoNian(qingShaoNianDict, orgId=None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查重点青少年开始..")
    try:
        compDict = copy.deepcopy(ShiYouRenKouPara.getPopulationDict)
        compDict['organizationId']= orgId
        response = pinganjianshe_post(url='/baseinfo/idleYouthManage/idleYouthList.action', postdata=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(qingShaoNianDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到重点青少年信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到重点青少年信息")
            return False    
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查重点青少年信息失败")
        return False       

 
'''
    @重点上访人员
    @功能： 新增测试自动化网格下的重点上访人员信息
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
''' 
def add_shangFangRenYuan(shangFangDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增重点上访人员开始..")
    response = pinganjianshe_post(url='/baseinfo/superiorVisitManage/maintainSuperiorVisitBaseInfo.action', postdata=shangFangDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增上访人员成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增上访人员失败")
    return response

'''
    @功能： 删除测试自动化网格下的重点上访人员信息
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
''' 
def delete_shangFangRenYuan(shangFangDict, username = None, password = None):  
    Log.LogOutput(LogLevel.INFO, "删除重点上访人员开始..")
    response = pinganjianshe_get(url='/baseinfo/superiorVisitManage/deleteSuperiorVisitByIds.action', param=shangFangDict,username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除上访人员成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "删除上访人员失败")    
    return response    

'''
    @功能： 检查测试自动化网格下的重点上访人员信息
    @para: getPopulationDict：检查时需要传入的字典项
    @return: 如果检查成功，则返回True；否则返回False  
''' 
def check_shangFangRenYuan(shangFangDict, orgId=None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查重点上访人员开始..")
    try:
        compDict = copy.deepcopy(ShiYouRenKouPara.getPopulationDict)
        compDict['organizationId']= orgId
        response = pinganjianshe_post(url='/baseinfo/superiorVisitManage/superiorVisitList.action', postdata=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(shangFangDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到上访人员信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到上访人员信息")
            return False   
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查重点上访人员信息失败")
        return False
    
'''  
    @功能： 导出测试自动化网格下的重点上访人员信息
    @para: 
    @return: 如果导出成功，则返回True；否则返回False  
'''    
def downLoad_shangFangRenYuan(dldata, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导出重点上访人员开始..")
    response = pinganjianshe_post(url='/baseinfo/searchSuperiorVisit/downloadSuperiorVisit.action', postdata=dldata, username=username, password = password)   
    return response

 
'''
    @危险品从业人员
    @功能： 新增测试自动化网格下的危险品从业人员信息
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
''' 
def add_weiXianPingCongYeRenYuan(practitionerDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增危险品从业人员开始..")
    response = pinganjianshe_post(url='/baseinfo/dangerousGoodsPractitionerManage/maintainDangerousGoodsPractitionerBaseInfo.action', postdata=practitionerDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增危险品从业人员成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增危险品从业人员失败")
    return response   

'''
    @功能： 删除测试自动化网格下的危险品从业人员信息
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
'''
def delete_weiXianPingCongYeRenYuan(practitionerDict, username = None, password = None):  
    Log.LogOutput(LogLevel.INFO, "删除危险品从业人员开始..")
    response = pinganjianshe_get(url='/baseinfo/dangerousGoodsPractitionerManage/deleteDangerousGoodsPractitionerByIds.action', param=practitionerDict,username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除危险品从业人员成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "删除危险品从业人员失败")    
    return response  

'''
    @功能： 检查测试自动化网格下的危险品从业人员信息
    @para: getPopulationDict：检查时需要传入的字典项
    @return: 如果检查成功，则返回True；否则返回False  
''' 
def check_weiXianPingCongYeRenYuan(practitionerDict, orgId=None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查危险品从业人员开始..")
    try:
        compDict = copy.deepcopy(ShiYouRenKouPara.getPopulationDict)
        compDict['organizationId']= orgId
        response = pinganjianshe_post(url='/baseinfo/dangerousGoodsPractitionerManage/dangerousGoodsPractitionerList.action', postdata=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(practitionerDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到危险品从业人员信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到危险品从业人员信息")
            return False  
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查危险品从业人员信息失败")
        return False

'''  
    @功能： 导出测试自动化网格下的危险品从业人员信息
    @para: 
    @return: 如果导出成功，则返回True；否则返回False  
'''    
def downLoad_weiXianPingCongYeRenYuan(dldata, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导出危险品从业人员开始..")
    response = pinganjianshe_post(url='/baseinfo/searchDangerousGoodsPractitioner/downloadDangerousGoodsPractitioner.action', postdata=dldata, username=username, password = password)   
    return response


'''
    @其他人员
    @功能： 新增测试自动化网格下的其他人员信息
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
''' 
def add_qiTaRenYuan(otherDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增其他人员开始..")
    response = pinganjianshe_post(url='/baseinfo/otherAttentionPersonnelManage/maintainOtherAttentionPersonnelBaseInfo.action', postdata=otherDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增其他人员成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增其他人员失败")
    return response  

'''
    @功能： 删除测试自动化网格下的其他人员信息
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
'''
def delete_qiTaRenYuan(otherDict, username = None, password = None):  
    Log.LogOutput(LogLevel.INFO, "删除其他人员开始..")
    response = pinganjianshe_get(url='/baseinfo/otherAttentionPersonnelManage/deleteOtherAttentionPersonnelByIds.action', param=otherDict,username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除其他人员成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "删除其他人员失败")    
    return response   

'''
    @功能： 检查测试自动化网格下的其他人员信息
    @para: getPopulationDict：检查时需要传入的字典项
    @return: 如果检查成功，则返回True；否则返回False  
''' 
def check_qiTaRenYuan(otherDict, orgId=None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查其他人员开始..")
    try:
        compDict = copy.deepcopy(ShiYouRenKouPara.getPopulationDict)
        compDict['organizationId']= orgId
        response = pinganjianshe_post(url='/baseinfo/otherAttentionPersonnelManage/otherAttentionPersonnelList.action', postdata=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(otherDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到其他人员信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到其他人员信息")
            return False  
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查其他人员信息失败")
        return False
  
'''  
    @功能： 导出测试自动化网格下的其他人员信息
    @para: 
    @return: 如果导出成功，则返回True；否则返回False  
'''    
def downLoad_qiTaRenYuan(dldata, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导出其他人员开始..")
    response = pinganjianshe_post(url='/baseinfo/searchOtherAttentionPersonnel/downloadOtherAttentionPersonnel.action', postdata=dldata, username=username, password = password)   
    return response
  
     

'''
    @关怀对象 > 见义勇为
    @功能： 新增测试自动化网格下的见义勇为人员信息
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
'''
def add_jianYiYongWei(jianYiYongWeiDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增见义勇为开始..")
    response = pinganjianshe_post(url='/baseinfo/samaritanPeopleManage/mainSamaritanPeopleBaseInfo.action', postdata=jianYiYongWeiDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增见义勇为人员成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增见义勇为人员失败")
    return response 

'''
    @功能： 删除测试自动化网格下的见义勇为人员信息
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
''' 
def delete_jianYiYongWei(jianYiYongWeiDict, username = None, password = None):  
    Log.LogOutput(LogLevel.INFO, "删除见义勇为开始..")
    response = pinganjianshe_get(url='/baseinfo/samaritanPeopleManage/deleteSamaritanPeopleByIds.action', param=jianYiYongWeiDict,username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除见义勇为人员成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "删除见义勇为人员失败")    
    return response     

'''
    @功能： 检查测试自动化网格下的见义勇为人员信息
    @para: getPopulationDict：检查时需要传入的字典项
    @return: 如果检查成功，则返回True；否则返回False  
'''
def check_jianYiYongWei(jianYiYongWeiDict, orgId=None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查见义勇为开始..")
    try:
        compDict = copy.deepcopy(ShiYouRenKouPara.getPopulationDict)
        compDict['organizationId']= orgId
        response = pinganjianshe_post(url='/baseinfo/samaritanPeopleManage/samaritanPeopleList.action', postdata=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(jianYiYongWeiDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到见义勇为人员信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到见义勇为人员信息")
            return False  
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查见义勇为人员信息失败")
        return False

'''  
    @功能： 导出测试自动化网格下的见义勇为人员信息
    @para: 
    @return: 如果导出成功，则返回True；否则返回False  
'''    
def downLoad_jianYiYongWei(dldata, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导出见义勇为人员开始..")
    response = pinganjianshe_post(url='/baseinfo/searchSamaritanPeople/downloadSamaritanPeople.action', postdata=dldata, username=username, password = password)   
    return response
  

'''
    @老年人
    @功能： 新增测试自动化网格下的老年人信息
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
''' 
def add_laoNianRen(laoNianRenDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增老年人开始..")
    response = pinganjianshe_post(url='/baseinfo/elderlyPeopleManage/mainElderPeopleBaseInfo.action', postdata=laoNianRenDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增老年人成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增老年人失败")
    return response 

'''
    @功能： 删除测试自动化网格下的老年人信息
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
''' 
def delete_laoNianRen(laoNianRenDict, username = None, password = None):  
    Log.LogOutput(LogLevel.INFO, "删除老年人开始..")
    response = pinganjianshe_get(url='/baseinfo/elderlyPeopleManage/deleteElderlyPeopleByIds.action', param=laoNianRenDict,username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除老年人成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "删除老年人失败")    
    return response   

'''
    @功能： 检查测试自动化网格下的老年人信息
    @para: getPopulationDict：检查时需要传入的字典项
    @return: 如果检查成功，则返回True；否则返回False  
''' 
def check_laoNianRen(laoNianRenDict, orgId=None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查老年人开始..")
    try:
        compDict = copy.deepcopy(ShiYouRenKouPara.getPopulationDict)
        compDict['organizationId']= orgId
        response = pinganjianshe_post(url='/baseinfo/elderlyPeopleManage/elderlyPeopleList.action', postdata=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(laoNianRenDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到老年人信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到老年人信息")
            return False  
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查老年人信息失败")
        return False

'''  
    @功能： 导出测试自动化网格下的老年人信息
    @para: 
    @return: 如果导出成功，则返回True；否则返回False  
'''    
def downLoad_laoNianRen(dldata, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导出老年人开始..")
    response = pinganjianshe_post(url='/baseinfo/searchElderlyPeople/downloadElderlyPeople.action', postdata=dldata, username=username, password = password)   
    return response

 
'''
    @残疾人
    @功能： 新增测试自动化网格下的残疾人信息
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
'''
def add_canJiRen(canJiRenDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增残疾人开始..")
    response = pinganjianshe_post(url='/baseinfo/handicappedManage/maintainHandicappedBaseInfo.action', postdata=canJiRenDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增残疾人成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增残疾人失败")
    return response  

'''
    @功能： 删除测试自动化网格下的残疾人信息
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
''' 
def delete_canJiRen(canJiRenDict, username = None, password = None):  
    Log.LogOutput(LogLevel.INFO, "删除残疾人开始..")
    response = pinganjianshe_get(url='/baseinfo/handicappedManage/deleteHandicappedByIds.action', param=canJiRenDict,username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除残疾人成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "删除残疾人失败")    
    return response    

'''
    @功能： 检查测试自动化网格下的残疾人信息
    @para: getPopulationDict：检查时需要传入的字典项
    @return: 如果检查成功，则返回True；否则返回False  
'''
def check_canJiRen(canJiRenDict, orgId=None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查残疾人开始..")
    try:
        compDict = copy.deepcopy(ShiYouRenKouPara.getPopulationDict)
        compDict['organizationId']= orgId
        response = pinganjianshe_post(url='/baseinfo/handicappedManage/handicappedList.action', postdata=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(canJiRenDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到残疾人信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到残疾人信息")
            return False 
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查残疾人信息失败")
        return False

'''  
    @功能： 导出测试自动化网格下的残疾人信息
    @para: 
    @return: 如果导出成功，则返回True；否则返回False  
'''    
def downLoad_canJiRen(dldata, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导出残疾人开始..")
    response = pinganjianshe_post(url='/baseinfo/searchHandicapped/downloadHandicapped.action', postdata=dldata, username=username, password = password)   
    return response


'''
    @优抚对象
    @功能： 新增测试自动化网格下的优抚对象信息
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
''' 
def add_youFuDuiXiang(youFuDuiXiangDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增优抚对象开始..")
    response = pinganjianshe_post(url='/baseinfo/optimalObjectManage/maintainOptimalObjectBaseInfo.action', postdata=youFuDuiXiangDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增优抚对象成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增优抚对象失败")
    return response   

'''
    @功能： 删除测试自动化网格下的优抚对象信息
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
'''
def delete_youFuDuiXiang(youFuDuiXiangDict, username = None, password = None):  
    Log.LogOutput(LogLevel.INFO, "删除优抚对象开始..")
    response = pinganjianshe_get(url='/baseinfo/optimalObjectManage/deleteOptimalObjectByIds.action', param=youFuDuiXiangDict,username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除优抚对象成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "删除优抚对象失败")    
    return response 

'''
    @功能： 检查测试自动化网格下的优抚对象信息
    @para: getPopulationDict：检查时需要传入的字典项
    @return: 如果检查成功，则返回True；否则返回False  
'''
def check_youFuDuiXiang(youFuDuiXiangDict, orgId=None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查优抚对象开始..")
    try:
        compDict = copy.deepcopy(ShiYouRenKouPara.getPopulationDict)
        compDict['organizationId']= orgId
        response = pinganjianshe_post(url='/baseinfo/optimalObjectManage/optimalObjectList.action', postdata=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(youFuDuiXiangDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到优抚对象信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到优抚对象信息")
            return False 
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查优抚对象信息失败")
        return False

'''  
    @功能： 导出测试自动化网格下的优抚对象信息
    @para: 
    @return: 如果导出成功，则返回True；否则返回False  
'''    
def downLoad_youFuDuiXiang(dldata, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导出优抚对象开始..")
    response = pinganjianshe_post(url='/baseinfo/searchOptimalObject/downloadOptimalObject.action', postdata=dldata, username=username, password = password)   
    return response


'''
    @需要救助人员
    @功能： 新增测试自动化网格下的需要救助人员信息
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
'''
def add_xuYaoJiuZhuRenYuan(jiuZhuDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增需要救助人员开始..")
    response = pinganjianshe_post(url='/baseinfo/aidNeedPopulationManage/saveAidNeedPopulationInfo.action', postdata=jiuZhuDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增需要救助人员成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增需要救助人员失败")
    return response   

'''
    @功能： 删除测试自动化网格下的需要救助人员信息
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
''' 
def delete_xuYaoJiuZhuRenYuan(jiuZhuDict, username = None, password = None):  
    Log.LogOutput(LogLevel.INFO, "删除需要救助人员开始..")
    response = pinganjianshe_get(url='/baseinfo/aidNeedPopulationManage/deleteAidNeedPopulationByIds.action', param=jiuZhuDict,username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除需要救助人员成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "删除需要救助人员失败")    
    return response 

'''
    @功能： 检查测试自动化网格下的需要救助人员信息
    @para: getPopulationDict：检查时需要传入的字典项
    @return: 如果检查成功，则返回True；否则返回False  
''' 
def check_xuYaoJiuZhuRenYuan(jiuZhuDict, orgId=None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查需要救助人员开始..")
    try:
        compDict = copy.deepcopy(ShiYouRenKouPara.getPopulationDict)
        compDict['organizationId']= orgId
        response = pinganjianshe_post(url='/baseinfo/aidNeedPopulationManage/aidNeedPopulationList.action', postdata=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(jiuZhuDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到需要救助人员信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到需要救助人员信息")
            return False   
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查需要救助人员信息失败")
        return False

'''  
    @功能： 导出测试自动化网格下的需要救助人员信息
    @para: 
    @return: 如果导出成功，则返回True；否则返回False  
'''    
def downLoad_xuYaoJiuZhuRenYuan(dldata, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导出需要救助人员开始..")
    response = pinganjianshe_post(url='/baseinfo/searchAidNeedPopulation/downloadAidNeedPopulation.action', postdata=dldata, username=username, password = password)   
    return response
 

'''
    @失业人员
    @功能： 新增测试自动化网格下的失业人员信息
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
''' 
def add_shiYeRenYuan(shiYeDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增失业人员开始..")
    response = pinganjianshe_post(url='/baseinfo/unemployedPeopleManage/mainUnemployedPeopleBaseInfo.action', postdata=shiYeDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增失业人员成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增失业人员失败")
    return response  

'''
    @功能： 删除测试自动化网格下的失业人员信息
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
''' 
def delete_shiYeRenYuan(shiYeDict, username = None, password = None):  
    Log.LogOutput(LogLevel.INFO, "删除失业人员开始..")
    response = pinganjianshe_get(url='/baseinfo/unemployedPeopleManage/deleteUnemployedPeopleByIds.action', param=shiYeDict,username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除失业人员成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "删除失业人员失败")    
    return response  

'''
    @功能： 检查测试自动化网格下的失业人员信息
    @para: getPopulationDict：检查时需要传入的字典项
    @return: 如果检查成功，则返回True；否则返回False  
''' 
def check_shiYeRenYuan(shiYeDict, orgId=None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查失业人员开始..")
    try:
        compDict = copy.deepcopy(ShiYouRenKouPara.getPopulationDict)
        compDict['organizationId']= orgId
        response = pinganjianshe_post(url='/baseinfo/unemployedPeopleManage/unemployedPeopleList.action', postdata=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(shiYeDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到失业人员信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到失业人员信息")
            return False   
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查失业人员信息失败")
        return False

'''  
    @功能： 导出测试自动化网格下的失业人员信息
    @para: 
    @return: 如果导出成功，则返回True；否则返回False  
'''    
def downLoad_shiYeRenYuan(dldata, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导出失业人员开始..")
    response = pinganjianshe_post(url='/baseinfo/searchUnemployedPeople/downloadUnemployedPeople.action', postdata=dldata, username=username, password = password)   
    return response

     
'''
    @育龄妇女
    @功能： 新增测试自动化网格下的育龄妇女人员信息
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
'''
def add_yuLingFuNv(yuLingDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增育龄妇女开始..")
    response = pinganjianshe_post(url='/baseinfo/nurturesWomenManage/maintainNurturesWomenBaseInfo.action', postdata=yuLingDict, username=username, password=password)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增育龄妇女成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增育龄妇女失败")
    return response  

'''
    @功能： 删除测试自动化网格下的育龄妇女信息
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
''' 
def delete_yuLingFuNv(yuLingDict, username = None, password = None):  
    Log.LogOutput(LogLevel.INFO, "删除育龄妇女开始..")
    response = pinganjianshe_get(url='/baseinfo/nurturesWomenManage/deleteNurturesWomenByIds.action', param=yuLingDict,username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除育龄妇女成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "删除育龄妇女失败")    
    return response   

'''
    @功能： 检查测试自动化网格下的育龄妇女信息
    @para: getPopulationDict：检查时需要传入的字典项
    @return: 如果检查成功，则返回True；否则返回False  
''' 
def check_yuLingFuNv(yuLingDict, orgId=None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查育龄妇女开始..")
    try:
        compDict = copy.deepcopy(ShiYouRenKouPara.getPopulationDict)
        compDict['organizationId']= orgId
        response = pinganjianshe_post(url='/baseinfo/nurturesWomenManage/nurturesWomenList.action', postdata=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(yuLingDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到育龄妇女信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到育龄妇女信息")
            return False   
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查育龄妇女信息失败")
        return False

'''  
    @功能： 导出测试自动化网格下的育龄妇女信息
    @para: 
    @return: 如果导出成功，则返回True；否则返回False  
'''    
def downLoad_yuLingFuNv(dldata, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导出育龄妇女开始..")
    response = pinganjianshe_post(url='/baseinfo/searchNurturesWomen/downloadNurturesWomen.action', postdata=dldata, username=username, password = password)   
    return response

     
'''
    @侨属
    @功能： 新增测试自动化网格下的侨属信息
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
'''
def add_qiaoShu(qiaoShuDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增侨属开始..")
    response = pinganjianshe_post(url='/abroadDependent/abroadDependentManage/addAbroadDependentBaseInfo.action', postdata=qiaoShuDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增侨属成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增侨属失败")
    return response   

'''
    @功能： 删除测试自动化网格下的侨属人员信息
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
''' 
def delete_qiaoShu(qiaoShuDict, username = None, password = None):  
    Log.LogOutput(LogLevel.INFO, "删除侨属开始..")
    response = pinganjianshe_get(url='/abroadDependent/abroadDependentManage/deleteAbroadDependent.action', param=qiaoShuDict,username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除侨属成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "删除侨属失败")    
    return response   


'''
    @功能： 检查测试自动化网格下的侨属人员信息
    @para: getQiaoShuDict：检查时需要传入的字典项
    @return: 如果检查成功，则返回True；否则返回False  
''' 
def check_qiaoShu(qiaoShuDict, orgId=None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查侨属开始..")
    try:
        compDict = copy.deepcopy(ShiYouRenKouPara.getQiaoShuDict)
        compDict['abroadDependent.organization.id']= orgId
        response = pinganjianshe_post(url='/abroadDependent/abroadDependentManage/findAbroadDependentsPage.action', postdata=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(qiaoShuDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到侨属信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到侨属信息")
            return False   
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查侨属信息失败")
        return False
     
'''
    @失地家庭
    @功能： 新增测试自动化网格下的失地家庭信息
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
'''
def add_shiDiJiaTing(lostDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增失地家庭开始..")
    response = pinganjianshe_post(url='/baseinfo/lostEarthManage/mainLostEarthBaseInfo.action', postdata=lostDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增失地家庭成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增失地家庭失败")
    return response   

'''
    @功能： 删除测试自动化网格下的失地家庭信息
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
''' 
def delete_shiDiJiaTing(lostDict, username = None, password = None):  
    Log.LogOutput(LogLevel.INFO, "删除失地家庭开始..")
    response = pinganjianshe_get(url='/baseinfo/lostEarthManage/deleteLostEarthByIds.action', param=lostDict,username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除失地家庭成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "删除失地家庭失败")    
    return response

'''
    @功能： 检查测试自动化网格下的失地家庭信息
    @para: getPopulationDict：检查时需要传入的字典项
    @return: 如果检查成功，则返回True；否则返回False  
''' 
def check_shiDiJiaTing(lostDict, orgId=None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查失地家庭开始..")
    try:
        compDict = copy.deepcopy(ShiYouRenKouPara.getPopulationDict)
        compDict['organizationId']= orgId
        response = pinganjianshe_post(url='/baseinfo/lostEarthManage/lostEarthList.action', postdata=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(lostDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到失地家庭信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到失地家庭信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查失地家庭信息失败")
        return False

'''  
    @功能： 导出测试自动化网格下的失地家庭信息
    @para: 
    @return: 如果导出成功，则返回True；否则返回False  
'''    
def downLoad_shiDiJiaTing(dldata, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导出失地家庭开始..")
    response = pinganjianshe_post(url='/baseinfo/searchLostEarth/downloadLostEarth.action', postdata=dldata, username=username, password = password)   
    return response


'''
    @求职人员
    @功能： 新增测试自动化网格下的求职人员信息
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
'''
def add_qiuZhiRenYuan(qiuZhiDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增求职人员开始")
    response = pinganjianshe_post(url='/baseinfo/bewerBungManage/addBewerBungBaseInfo.action', postdata=qiuZhiDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增求职人员成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增求职人员失败")
    return response   

'''
    @功能： 删除测试自动化网格下的求职人员信息
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
''' 
def delete_qiuZhiRenYuan(qiuZhiDict, username = None, password = None):  
    Log.LogOutput(LogLevel.INFO, "删除求职人员开始")
    response = pinganjianshe_get(url='/baseinfo/bewerBungManage/deleteBewerBungByIds.action', param=qiuZhiDict,username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除求职人员成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "删除求职人员失败")    
    return response

'''
    @功能： 检查测试自动化网格下的求职人员信息
    @para: getPopulationDict：检查时需要传入的字典项
    @return: 如果检查成功，则返回True；否则返回False  
''' 
def check_qiuZhiRenYuan(qiuZhiDict, orgId=None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查求职人员开始")
    try:
        compDict = copy.deepcopy(ShiYouRenKouPara.getPopulationDict)
        compDict['organizationId']= orgId
        response = pinganjianshe_post(url='/baseinfo/bewerBungManage/bewerBungList.action', postdata=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(qiuZhiDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到求职人员信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到求职人员信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查求职人员信息失败")
        return False

'''  
    @功能： 导出测试自动化网格下的求职人员信息
    @para: 
    @return: 如果导出成功，则返回True；否则返回False  
'''    
def downLoad_qiuZhiRenYuan(dldata, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导出求职人员开始..")
    response = pinganjianshe_post(url='/baseinfo/searchBewerBung/downloadBewerBung.action', postdata=dldata, username=username, password = password)   
    return response

    
'''
    @青少年
    @功能： 新增测试自动化网格下的青少年信息
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
'''
def add_qingShaoNian(qingShaoNianDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增青少年开始")
    response = pinganjianshe_post(url='/baseinfo/youthManage/mainYouthBaseInfo.action', postdata=qingShaoNianDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增青少年成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增青少年失败")
    return response 

'''
    @功能： 检查测试自动化网格下的重点青少年信息
    @para: getPopulationDict：检查时需要传入的字典项
    @return: 如果检查成功，则返回True；否则返回False  
''' 
def check_qingShaoNian(qingShaoNianDict, orgId=None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查青少年开始..")
    try:
        compDict = copy.deepcopy(ShiYouRenKouPara.getPopulationDict)
        compDict['organizationId']= orgId
        response = pinganjianshe_post(url='/baseinfo/youthManage/youthList.action', postdata=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(qingShaoNianDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到青少年信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到青少年信息")
            return False    
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查青少年信息失败")
        return False   

'''  
    @功能： 导出测试自动化网格下的青少年信息
    @para: 
    @return: 如果导出成功，则返回True；否则返回False  
'''    
def downLoad_qingShaoNian(dldata, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导出青少年开始..")
    response = pinganjianshe_post(url='/baseinfo/searchYouth/downloadYouth.action', postdata=dldata, username=username, password = password)   
    return response     
    
    
'''
    @功能： 删除测试自动化网格下的户籍、流动、未落户、境外人口、重点人员、关怀对象、失业人员、育龄妇女、侨属、失地家庭、求职人员
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
'''    
def deleteAllPopulation():
    try:
        #实有人口
        #删除户籍人口
            compDict = copy.deepcopy(ShiYouRenKouPara.getHuJiOrgDict)
            compDict['orgId']= orgInit['DftSheQuOrgId']
            response = pinganjianshe_get(url='/baseinfo/householdStaff/findHouseholdStaffByOrgId.action', param=compDict)
            responseDict = json.loads(response.text)
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无户籍人口')
            else:
                for dictListItem in responseDict['rows']:
                    deleteDict = {'householdStaffVo.idStr':dictListItem['id']}
                    delete_HuJiRenKou(deleteDict)
        #删除流动人口
            compDict = copy.deepcopy(ShiYouRenKouPara.getLiuDongOrgDict)
            compDict['organizationId']= orgInit['DftSheQuOrgId']
            response = pinganjianshe_get(url='/baseinfo/floatingPopulationManage/findFloatingPopulations.action', param=compDict)
            responseDict = json.loads(response.text)
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无流动人口')
            else:
                for dictListItem in responseDict['rows']:
                    deleteDict = copy.deepcopy(ShiYouRenKouPara.delLiuDongDict)
                    deleteDict['floatingPopulationIds']=dictListItem['id']
                    delete_LiuDongRenKou(deleteDict)
        #删除未落户人口
            compDict = copy.deepcopy(ShiYouRenKouPara.getWeiLuoHuDict)
            compDict['orgId']= orgInit['DftSheQuOrgId']
            response = pinganjianshe_get(url='/baseinfo/unsettledPopulationManage/findUnsettledPopulations.action', param=compDict)
            responseDict = json.loads(response.text)
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无未落户人口')
            else:
                for dictListItem in responseDict['rows']:
                    deleteDict = copy.deepcopy(ShiYouRenKouPara.delWeiLuoHuDict)
                    deleteDict['unsettledPopulationIds']=dictListItem['id']
                    delete_WeiLuoHuRenKou(deleteDict) 
        #删除境外人口
            compDict = copy.deepcopy(ShiYouRenKouPara.getJingWaiOrgDict)
            compDict['orgId']= orgInit['DftSheQuOrgId']
            response = pinganjianshe_get(url='/baseinfo/overseaPersonnelManage/overseaPersonnelList.action', param=compDict)
            responseDict = json.loads(response.text)
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无境外人口')
            else:
                for dictListItem in responseDict['rows']:
                    deleteDict = copy.deepcopy(ShiYouRenKouPara.delJingWaiDict)
                    deleteDict['deleteIds']=dictListItem['id']
                    delete_JingWaiRenKou(deleteDict) 
    
        #删除户籍家庭        
            compDict = copy.deepcopy(ShiYouRenKouPara.getHouseFamilyDict)
            compDict['orgId']= orgInit['DftSheQuOrgId']
            response = pinganjianshe_get(url='/baseinfo/houseFamily/findHouseFamilyByOrgId.action', param=compDict)  
            responseDict = json.loads(response.text)
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无户籍家庭')
            else:
    #             for dictListItem in responseDict['rows']:
                    deleteDict = copy.deepcopy(ShiYouRenKouPara.deleteFamilyObject)
                    deleteDict['ids']=responseDict['rows'][0]['censusRegisterFamily']['id']
                    delete_houseFamily(deleteDict) 
        #删除走访记录        
            compDict = copy.deepcopy(ShiYouRenKouPara.getViewDataDict)
            compDict['searchViewdataVo.orgId'] = orgInit['DftSheQuOrgId']
            response = pinganjianshe_get(url='/baseinfo/viewdataManage/findViewdatasBySearchViewdataVo.action', param=compDict)  
            responseDict = json.loads(response.text)
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无走访记录')
            else:
                for dictListItem in responseDict['rows']:
                    deleteDict = copy.deepcopy(ShiYouRenKouPara.deleteDict)
                    deleteDict['ids']=dictListItem['id']
                    delete_viewDataManage(deleteDict) 
                  
    except Exception,e:
        Log.LogOutput(LogLevel.ERROR, '删除失败'+str(e))
        return False     
    return True


#重点青少年查找列表所有id并删除
def zhongDianQingShaoNianDelAll(username = None ,password = None):
    Log.LogOutput(LogLevel.DEBUG, "进入到重点青少年信息列表....")
    try:
        #重点青少年
        compDict = copy.deepcopy(ShiYouRenKouPara.getPopulationDict)
        compDict['organizationId']= orgInit['DftWangGeOrgId']
        response = pinganjianshe_get(url='/baseinfo/idleYouthManage/idleYouthList.action', param=compDict)
        responseDict = json.loads(response.text)
        if responseDict['records'] == 0:
            Log.LogOutput(LogLevel.DEBUG, '无重点青少年')
        else:
            for dictListItem in responseDict['rows']:
                deleteDict = copy.deepcopy(ShiYouRenKouPara.deleteDict)
                deleteDict['populationIds']=dictListItem['id']
                delete_zhongDianQingShaoNian(deleteDict) 
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '查找重点青少年信息过程中失败')
        return False  
    
'''
    @功能：检查数据是否存在于矫正人员快速搜索后的列表中
    @return:    response
    @author:  chenhui 2016-05-18
'''   
def checkJiaoZhengFastSearchList(checkpara,searchpara,username=userInit['DftWangGeUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "正在验证快速搜索结果正确性")
    try:
        response = pinganjianshe_post(url='/baseinfo/searchRectificativePerson/fastSearch.action',postdata=searchpara,username=username,password=password)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False

'''
    @功能：检查数据是否存在于矫正人员高级搜索后的列表中
    @return:    response
    @author:  chenhui 2016-05-18
'''   
def checkJiaoZhengSeniorSearchList(checkpara,searchpara,username=userInit['DftWangGeUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "正在验证高级结果正确性")
    try:
        response = pinganjianshe_post(url='/baseinfo/searchRectificativePerson/findRectificativePersonsByQueryCondition.action',postdata=searchpara,username=username,password=password)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False

'''
    @功能：检查数据是否存在于精神病人员快速搜索后的列表中
    @return:    response
    @author:  chenhui 2016-05-18
'''   
def checkJingShenBingFastSearchList(checkpara,searchpara,username=userInit['DftWangGeUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "正在验证快速搜索结果正确性")
    try:
        response = pinganjianshe_post(url='/baseinfo/searchMentalPatient/fastSearch.action',postdata=searchpara,username=username,password=password)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False

'''
    @功能：检查数据是否存在于精神病人员高级搜索后的列表中
    @return:    response
    @author:  chenhui 2016-05-18
'''   
def checkJingShenBingSeniorSearchList(checkpara,searchpara,username=userInit['DftWangGeUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "正在验证高级结果正确性")
    try:
        response = pinganjianshe_post(url='/baseinfo/searchMentalPatient/findMentalPatientsByQueryCondition.action',postdata=searchpara,username=username,password=password)
        responseDict=json.loads(response.text)
        print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False
        
'''
    @功能：检查数据是否存在于吸毒人员快速搜索后的列表中
    @return:    response
    @author:  chenhui 2016-05-18
'''   
def checkXiDuFastSearchList(checkpara,searchpara,username=userInit['DftWangGeUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "正在验证快速搜索结果正确性")
    try:
        response = pinganjianshe_post(url='/baseinfo/searchDruggy/fastSearch.action',postdata=searchpara,username=username,password=password)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False

'''
    @功能：检查数据是否存在于吸毒人员高级搜索后的列表中
    @return:    response
    @author:  chenhui 2016-05-18
'''   
def checkXiDuSeniorSearchList(checkpara,searchpara,username=userInit['DftWangGeUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "正在验证高级结果正确性")
    try:
        response = pinganjianshe_post(url='/baseinfo/searchDruggy/findDruggysByQueryCondition.action',postdata=searchpara,username=username,password=password)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False

'''
    @功能：检查数据是否存在于重点青少年人员快速搜索后的列表中
    @return:    response
    @author:  chenhui 2016-05-18
'''   
def checkZhongDianQingShaoNianFastSearchList(checkpara,searchpara,username=userInit['DftWangGeUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "正在验证快速搜索结果正确性")
    try:
        response = pinganjianshe_post(url='/baseinfo/searchIdleYouth/fastSearch.action',postdata=searchpara,username=username,password=password)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False

'''
    @功能：检查数据是否存在于重点青少年人员高级搜索后的列表中
    @return:    response
    @author:  chenhui 2016-05-18
'''   
def checkZhongDianQingShaoNianSeniorSearchList(checkpara,searchpara,username=userInit['DftWangGeUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "正在验证高级结果正确性")
    try:
        response = pinganjianshe_post(url='/baseinfo/searchIdleYouth/findIdleYouthsByQueryCondition.action',postdata=searchpara,username=username,password=password)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False
        
'''
    @功能：检查数据是否存在于重点上访人员快速搜索后的列表中
    @return:    response
    @author:  chenhui 2016-05-18
'''   
def checkZhongDianShangFangFastSearchList(checkpara,searchpara,username=userInit['DftWangGeUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "正在验证快速搜索结果正确性")
    try:
        response = pinganjianshe_post(url='/baseinfo/searchSuperiorVisit/fastSearch.action',postdata=searchpara,username=username,password=password)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False

'''
    @功能：检查数据是否存在于重点上访人员高级搜索后的列表中
    @return:    response
    @author:  chenhui 2016-05-18
'''   
def checkZhongDianShangFangSeniorSearchList(checkpara,searchpara,username=userInit['DftWangGeUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "正在验证高级结果正确性")
    try:
        response = pinganjianshe_post(url='/baseinfo/searchSuperiorVisit/findSuperiorVisitsByQueryCondition.action',postdata=searchpara,username=username,password=password)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False
        
'''
    @功能：检查数据是否存在于危险品从业人员快速搜索后的列表中
    @return:    response
    @author:  chenhui 2016-05-18
'''   
def checkWeiXianPingCongYeFastSearchList(checkpara,searchpara,username=userInit['DftWangGeUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "正在验证快速搜索结果正确性")
    try:
        response = pinganjianshe_post(url='/baseinfo/searchDangerousGoodsPractitioner/fastSearch.action',postdata=searchpara,username=username,password=password)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False

'''
    @功能：检查数据是否存在于危险品从业人员高级搜索后的列表中
    @return:    response
    @author:  chenhui 2016-05-18
'''   
def checkWeiXianPingCongYeSeniorSearchList(checkpara,searchpara,username=userInit['DftWangGeUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "正在验证高级结果正确性")
    try:
        response = pinganjianshe_post(url='/baseinfo/searchDangerousGoodsPractitioner/findDangerousGoodsPractitionersByQueryCondition.action',postdata=searchpara,username=username,password=password)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False
        
'''
    @功能：检查数据是否存在于其他人员快速搜索后的列表中
    @return:    response
    @author:  chenhui 2016-05-18
'''   
def checkQiTaFastSearchList(checkpara,searchpara,username=userInit['DftWangGeUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "正在验证快速搜索结果正确性")
    try:
        response = pinganjianshe_post(url='/baseinfo/searchOtherAttentionPersonnel/fastSearch.action',postdata=searchpara,username=username,password=password)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False

'''
    @功能：检查数据是否存在于其他人员高级搜索后的列表中
    @return:    response
    @author:  chenhui 2016-05-18
'''   
def checkQiTaSeniorSearchList(checkpara,searchpara,username=userInit['DftWangGeUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "正在验证高级结果正确性")
    try:
        response = pinganjianshe_post(url='/baseinfo/searchOtherAttentionPersonnel/findOtherAttentionPersonnelsByQueryCondition.action',postdata=searchpara,username=username,password=password)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False

'''
    @功能：检查数据是否存在于传销人员快速搜索后的列表中
    @return:    response
    @author:  chenhui 2016-05-18
'''   
def checkChuanXiaoFastSearchList(checkpara,searchpara,username=userInit['DftWangGeUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "正在验证快速搜索结果正确性")
    try:
        response = pinganjianshe_post(url='/baseinfo/searchRectificativePerson/fastSearch.action',postdata=searchpara,username=username,password=password)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False

'''
    @功能：检查数据是否存在于传销人员高级搜索后的列表中
    @return:    response
    @author:  chenhui 2016-05-18
'''   
def checkChuanXiaoSeniorSearchList(checkpara,searchpara,username=userInit['DftWangGeUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "正在验证高级结果正确性")
    try:
        response = pinganjianshe_post(url='/baseinfo/searchPyramidSchemes/findPyramidSchemessByQueryCondition.action',postdata=searchpara,username=username,password=password)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False

'''
    @功能：检查数据是否存在于见义勇为人员快速搜索后的列表中
    @return:    response
    @author:  chenhui 2016-05-18
'''   
def checkJianYiYongWeiFastSearchList(checkpara,searchpara,username=userInit['DftWangGeUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "正在验证快速搜索结果正确性")
    try:
        response = pinganjianshe_post(url='/baseinfo/searchSamaritanPeople/fastSearch.action',postdata=searchpara,username=username,password=password)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False

'''
    @功能：检查数据是否存在于见义勇为人员高级搜索后的列表中
    @return:    response
    @author:  chenhui 2016-05-18
'''   
def checkJianYiYongWeiSeniorSearchList(checkpara,searchpara,username=userInit['DftWangGeUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "正在验证高级结果正确性")
    try:
        response = pinganjianshe_post(url='/baseinfo/searchSamaritanPeople/findSamaritanPeoplesByQueryCondition.action',postdata=searchpara,username=username,password=password)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False
        
'''
    @功能：检查数据是否存在于老年人员快速搜索后的列表中
    @return:    response
    @author:  chenhui 2016-05-18
'''   
def checkLaoNianFastSearchList(checkpara,searchpara,username=userInit['DftWangGeUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "正在验证快速搜索结果正确性")
    try:
        response = pinganjianshe_post(url='/baseinfo/searchElderlyPeople/fastSearch.action',postdata=searchpara,username=username,password=password)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False

'''
    @功能：检查数据是否存在于老年人员高级搜索后的列表中
    @return:    response
    @author:  chenhui 2016-05-18
'''   
def checkLaoNianSeniorSearchList(checkpara,searchpara,username=userInit['DftWangGeUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "正在验证高级结果正确性")
    try:
        response = pinganjianshe_post(url='/baseinfo/searchElderlyPeople/findElderlyPeoplesByQueryCondition.action',postdata=searchpara,username=username,password=password)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False
        
'''
    @功能：检查数据是否存在于残疾人员快速搜索后的列表中
    @return:    response
    @author:  chenhui 2016-05-18
'''   
def checkCanJiFastSearchList(checkpara,searchpara,username=userInit['DftWangGeUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "正在验证快速搜索结果正确性")
    try:
        response = pinganjianshe_post(url='/baseinfo/searchHandicapped/fastSearch.action',postdata=searchpara,username=username,password=password)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False

'''
    @功能：检查数据是否存在于残疾人员高级搜索后的列表中
    @return:    response
    @author:  chenhui 2016-05-18
'''   
def checkCanJiSeniorSearchList(checkpara,searchpara,username=userInit['DftWangGeUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "正在验证高级结果正确性")
    try:
        response = pinganjianshe_post(url='/baseinfo/searchHandicapped/findHandicappedsByQueryCondition.action',postdata=searchpara,username=username,password=password)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False
        
'''
    @功能：检查数据是否存在于优抚对象人员快速搜索后的列表中
    @return:    response
    @author:  chenhui 2016-05-18
'''   
def checkYouFuDuiXiangFastSearchList(checkpara,searchpara,username=userInit['DftWangGeUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "正在验证快速搜索结果正确性")
    try:
        response = pinganjianshe_post(url='/baseinfo/searchOptimalObject/fastSearch.action',postdata=searchpara,username=username,password=password)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False

'''
    @功能：检查数据是否存在于优抚对象人员高级搜索后的列表中
    @return:    response
    @author:  chenhui 2016-05-18
'''   
def checkYouFuDuiXiangSeniorSearchList(checkpara,searchpara,username=userInit['DftWangGeUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "正在验证高级结果正确性")
    try:
        response = pinganjianshe_post(url='/baseinfo/searchOptimalObject/findOptimalObjectsByQueryCondition.action',postdata=searchpara,username=username,password=password)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False
        
'''
    @功能：检查数据是否存在于需要救助人员快速搜索后的列表中
    @return:    response
    @author:  chenhui 2016-05-18
'''   
def checkXuYaoJiuZhuFastSearchList(checkpara,searchpara,username=userInit['DftWangGeUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "正在验证快速搜索结果正确性")
    try:
        response = pinganjianshe_post(url='/baseinfo/searchAidNeedPopulation/fastSearch.action',postdata=searchpara,username=username,password=password)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False

'''
    @功能：检查数据是否存在于需要救助人员高级搜索后的列表中
    @return:    response
    @author:  chenhui 2016-05-18
'''   
def checkXuYaoJiuZhuSeniorSearchList(checkpara,searchpara,username=userInit['DftWangGeUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "正在验证高级结果正确性")
    try:
        response = pinganjianshe_post(url='/baseinfo/searchAidNeedPopulation/findAidNeedPopulationsByQueryCondition.action',postdata=searchpara,username=username,password=password)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False
        
'''
    @功能：检查数据是否存在于失业人员快速搜索后的列表中
    @return:    response
    @author:  chenhui 2016-05-18
'''   
def checkShiYeFastSearchList(checkpara,searchpara,username=userInit['DftWangGeUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "正在验证快速搜索结果正确性")
    try:
        response = pinganjianshe_post(url='/baseinfo/searchUnemployedPeople/fastSearch.action',postdata=searchpara,username=username,password=password)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False

'''
    @功能：检查数据是否存在于失业人员高级搜索后的列表中
    @return:    response
    @author:  chenhui 2016-05-18
'''   
def checkShiYeSeniorSearchList(checkpara,searchpara,username=userInit['DftWangGeUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "正在验证高级结果正确性")
    try:
        response = pinganjianshe_post(url='/baseinfo/searchUnemployedPeople/findUnemployedPeoplesByQueryCondition.action',postdata=searchpara,username=username,password=password)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False
        
'''
    @功能：检查数据是否存在于育龄妇女人员快速搜索后的列表中
    @return:    response
    @author:  chenhui 2016-05-18
'''   
def checkYuLingFuNvFastSearchList(checkpara,searchpara,username=userInit['DftWangGeUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "正在验证快速搜索结果正确性")
    try:
        response = pinganjianshe_post(url='/baseinfo/searchNurturesWomen/fastSearch.action',postdata=searchpara,username=username,password=password)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False

'''
    @功能：检查数据是否存在于育龄妇女人员高级搜索后的列表中
    @return:    response
    @author:  chenhui 2016-05-18
'''   
def checkYuLingFuNvSeniorSearchList(checkpara,searchpara,username=userInit['DftWangGeUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "正在验证高级结果正确性")
    try:
        response = pinganjianshe_post(url='/baseinfo/searchNurturesWomen/findNurturesWomensByQueryCondition.action',postdata=searchpara,username=username,password=password)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False
        
'''
    @功能：检查数据是否存在于乔属人员快速搜索后的列表中
    @return:    response
    @author:  chenhui 2016-05-18
'''   
def checkQiaoShuFastSearchList(checkpara,searchpara,username=userInit['DftWangGeUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "正在验证快速搜索结果正确性")
    try:
        response = pinganjianshe_get(url='/abroadDependent/abroadDependentManage/findAbroadDependentsPage.action',param=searchpara,username=username,password=password)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False

'''
    @功能：检查数据是否存在于乔属人员高级搜索后的列表中
    @return:    response
    @author:  chenhui 2016-05-18
'''   
def checkQiaoShuSeniorSearchList(checkpara,searchpara,username=userInit['DftWangGeUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "正在验证高级结果正确性")
    try:
        response = pinganjianshe_get(url='/abroadDependent/abroadDependentManage/findAbroadDependentsPage.action',param=searchpara,username=username,password=password)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False
        
'''
    @功能：检查数据是否存在于失地家庭人员快速搜索后的列表中
    @return:    response
    @author:  chenhui 2016-05-18
'''   
def checkShiDiJiaTingFastSearchList(checkpara,searchpara,username=userInit['DftWangGeUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "正在验证快速搜索结果正确性")
    try:
        response = pinganjianshe_post(url='/baseinfo/searchLostEarth/fastSearch.action',postdata=searchpara,username=username,password=password)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False

'''
    @功能：检查数据是否存在于失地家庭人员高级搜索后的列表中
    @return:    response
    @author:  chenhui 2016-05-18
'''   
def checkShiDiJiaTingSeniorSearchList(checkpara,searchpara,username=userInit['DftWangGeUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "正在验证高级结果正确性")
    try:
        response = pinganjianshe_post(url='/baseinfo/searchLostEarth/findLostEarthsByQueryCondition.action',postdata=searchpara,username=username,password=password)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False
        
'''
    @功能：检查数据是否存在于求职人员人员快速搜索后的列表中
    @return:    response
    @author:  chenhui 2016-05-18
'''   
def checkQiuZhiFastSearchList(checkpara,searchpara,username=userInit['DftWangGeUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "正在验证快速搜索结果正确性")
    try:
        response = pinganjianshe_post(url='/baseinfo/searchBewerBung/fastSearch.action',postdata=searchpara,username=username,password=password)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False

'''
    @功能：检查数据是否存在于求职人员人员高级搜索后的列表中
    @return:    response
    @author:  chenhui 2016-05-18
'''   
def checkQiuZhiSeniorSearchList(checkpara,searchpara,username=userInit['DftWangGeUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "正在验证高级结果正确性")
    try:
        response = pinganjianshe_post(url='/baseinfo/searchBewerBung/findBewerBungsByQueryCondition.action',postdata=searchpara,username=username,password=password)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False