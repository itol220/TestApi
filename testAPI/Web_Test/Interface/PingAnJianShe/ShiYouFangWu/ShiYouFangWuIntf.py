# -*- coding:UTF-8 -*-
'''
Created on 2015-12-8

@author: chenyan
'''
from __future__ import unicode_literals
from Interface.PingAnJianShe.pingAnJianSheHttpCommon import pinganjianshe_post,\
pinganjianshe_get
import json
import copy
from COMMON import Log, CommonUtil
from CONFIG.Define import LogLevel
from Interface.PingAnJianShe.ShiYouFangWu import ShiYouFangWuPara
from CONFIG.InitDefaultPara import orgInit
from Interface.PingAnJianShe.Common import CommonIntf


'''  
    @功能： 新增测试自动化网格下的实有房屋信息
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
'''
def add_ShiYouFangWu(fangWuDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增实有房屋开始..")
    response = pinganjianshe_post(url='/baseinfo/actualHouseManage/maintainHouseInfo.action', postdata=fangWuDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增实有房屋成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增实有房屋失败")
    return response

'''  
    @功能： 修改测试自动化网格下的实有房屋信息
    @para: 
    @return: 如果修改成功，则返回True；否则返回False  
'''
def edit_ShiYouFangWu(editDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "修改实有房屋开始..")
    response = pinganjianshe_post(url='/baseinfo/actualHouseManage/maintainHouseInfo.action', postdata=editDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "修改实有房屋成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "修改实有房屋失败")
    return response

'''  
    @功能： 删除测试自动化网格下的实有房屋信息
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
'''
def delete_ShiYouFangWu(deleteDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "删除实有房屋开始..")
    response = pinganjianshe_post(url='/baseinfo/actualHouseManage/deleteHouseInfo.action', postdata=deleteDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除实有房屋成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "删除实有房屋失败")
    return response

'''  
    @功能： 搜索测试自动化网格下的实有房屋信息
    @para: 
    @return: 如果搜索成功，则返回True；否则返回False  
'''
def search_ShiYouFangWu(searchDict, orgId=None,username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "搜索实有房屋开始..")
    try:
        compDict = copy.deepcopy(ShiYouFangWuPara.getFangWuDict)
        compDict['orgId']= orgId
        response = pinganjianshe_get(url='/baseinfo/actualHouseManage/searchHouseInfo.action', param=compDict,username=username, password = password)
#         print response.text  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(searchDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "搜索实有房屋成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "搜索实有房屋失败")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "搜索实有房屋失败")
        return False
    
'''  
    @功能： 导入测试自动化网格下的实有房屋信息
    @para: 
    @return: 如果导入成功，则返回True；否则返回False  
'''
def import_ShiYouFangWu(data, files=None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导入实有房屋开始..")
    response = pinganjianshe_post(url='/dataTransfer/importToDomain.action', postdata=data, files=files, username=username, password = password)   
    return response

'''  
    @功能： 导出测试自动化网格下的实有房屋信息
    @para: 
    @return: 如果导出成功，则返回True；否则返回False  
'''    
def downLoad_ShiYouFangWu(dldata, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导出实有房屋开始..")
    response = pinganjianshe_post(url='/baseinfo/actualHouseManage/downloadHouseInfo.action', postdata=dldata, username=username, password = password)   
    return response

'''  
    @功能： 添加测试自动化网格下实有房屋的住户信息
    @para: 
    @return: 如果添加成功，则返回True；否则返回False  
'''
def add_ZhuHuXinXi(zhuHuDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增住户信息开始..")
    response = pinganjianshe_post(url='/baseinfo/actualHouseManage/addHouseHasActualPopulation.action', postdata=zhuHuDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增住户信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增住户信息失败")
    return response

'''  
    @功能： 删除测试自动化网格下实有房屋的住户信息
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
'''
def delete_ZhuHuXinXi(zhuHuDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "删除住户信息开始..")
    response = pinganjianshe_get(url='/baseinfo/actualHouseManage/deleteHouseHasActualPopulationByPopulationTypeAndHouseId.action', param=zhuHuDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除住户信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "删除住户信息失败")
    return response

'''  
    @功能： 检查测试自动化网格下实有房屋的住户信息
    @para: 
    @return: 如果检查成功，则返回True；否则返回False  
'''
def check_ZhuHuXinXi(zhuHuDict, houseId=None, username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "检查住户信息开始..")
    try:
        compDict = copy.deepcopy(ShiYouFangWuPara.getZhuHuDict)
        compDict['houseId']= houseId
        response = pinganjianshe_get(url='/baseinfo/actualHousePopulation/findLivingInHousePopulationInfos.action', param=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(zhuHuDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到住户信息信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到住户信息信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查实有房屋信息失败")
        return False
    
'''  
    @功能： 将测试自动化网格下的实有房屋信息转移到测试自动化网格1中
    @para: 
    @return: 如果转移成功，则返回True；否则返回False  
'''
def transfer_ShiYouFangWu(transferDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "转移实有房屋开始..")
    response = pinganjianshe_post(url='/transferManage/transfer.action', postdata=transferDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "转移实有房屋成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "转移实有房屋失败")
    return response

'''  
    @功能： 检查测试自动化网格下的实有房屋信息
    @para: 
    @return: 如果检查成功，则返回True；否则返回False  
'''
def check_ShiYouFangWu(fangWuDict, orgId=None, username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "检查实有房屋开始..")
    try:
        compDict = copy.deepcopy(ShiYouFangWuPara.getFangWuDict)
        compDict['orgId']= orgId
        response = pinganjianshe_get(url='/baseinfo/actualHouseManage/houseInfoList.action', param=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(fangWuDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到实有房屋信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到实有房屋信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查实有房屋信息失败")
        return False
    

'''  
    @功能： 新增测试自动化网格下的出租房信息
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
'''
def add_ChuZuFang(chuZuDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增出租房开始..")
    response = pinganjianshe_post(url='/baseinfo/rentalHouseManage/maintainRentalHouse.action', postdata=chuZuDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增出租房成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增出租房失败")
    return response

'''  
    @功能： 注销测试自动化网格下的出租房信息
    @para: 
    @return: 如果注销成功，则返回True；否则返回False  
'''
def logOut_ChuZuFang(chuZuDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "注销出租房信息开始..")
    response = pinganjianshe_post(url='/baseinfo/rentalHouseManage/updateEmphasiseById.action', postdata=chuZuDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "注销出租房信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "注销出租房信息失败")
    return response

'''  
    @功能： 取消注销测试自动化网格下的出租房信息
    @para: 
    @return: 如果取消注销成功，则返回True；否则返回False  
'''
def logOutCancel_ChuZuFang(chuZuDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "取消注销出租房信息开始..")
    response = pinganjianshe_get(url='/baseinfo/rentalHouseManage/updateEmphasiseById.action', param=chuZuDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "取消注销出租房信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "取消注销出租房信息失败")
    return response

'''  
    @功能： 删除测试自动化网格下的出租房信息
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
'''
def delete_ChuZuFang(chuZuDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "删除出租房开始..")
    response = pinganjianshe_get(url='/baseinfo/rentalHouseManage/deleteHouseInfo.action', param=chuZuDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除出租房成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "删除出租房失败")
    return response

'''  
    @功能： 添加测试自动化网格下出租房中的治安负责人信息
    @para: 
    @return: 如果添加成功，则返回True；否则返回False  
'''
def add_ZhiAnFuZeRen(fuZeRenDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增治安负责人开始..")
    response = pinganjianshe_get(url='/plugin/serviceTeam/router/routerManage/addObjectAndMemberRelation.action', param=fuZeRenDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增治安负责人成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增治安负责人失败")
    return response

'''  
    @功能： 删除测试自动化网格下实有房屋中的治安负责人信息
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
'''
def delete_ZhiAnFuZeRen(deleteDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "删除治安负责人开始..")
    response = pinganjianshe_get(url='/plugin/serviceTeam/router/routerManage/deleteServiceMemberWithObject.action', param=deleteDict, username=username, password=password)
#     print response.text,response.result
    if isinstance(response.result,int):
        response.result=True
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除治安负责人成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "删除治安负责人失败")
    return response

'''  
    @功能： 将测试自动化网格下实有房屋中的治安负责人卸任/重新担任
    @para: 
    @return: 如果卸任/重新担任成功，则返回True；否则返回False  
'''
def leave_ZhiAnFuZeRen(leaveOrBackDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "治安负责人卸任/重新担任开始..")
    response = pinganjianshe_get(url='/plugin/serviceTeam/router/routerManage/leaveOrBackOnDuty.action', param=leaveOrBackDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "治安负责人卸任/重新担任成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "治安负责人卸任/重新担任失败")
    return response

'''  
    @功能： 检查测试自动化网格下出租房中的治安负责人信息
    @para: 
    @return: 如果检查成功，则返回True；否则返回False  
'''
def check_ZhiAnFuZeRen(fuZeRen, objectId=None, objectName = None,onDuty = None,username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "检查治安负责人开始..")
    try:
        compDict = copy.deepcopy(ShiYouFangWuPara.getFuZeRenDict)
        compDict['serviceMemberVo.objectId']= objectId
        compDict['serviceMemberVo.objectName']= objectName
        compDict['serviceMemberVo.onDuty']= onDuty
        response = pinganjianshe_post(url='/plugin/serviceTeam/router/routerManage/findServiceMembersByServiceMemberVo.action', postdata=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(fuZeRen, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到治安负责人信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到治安负责人信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查治安负责人信息失败")
        return False

'''  
    @功能： 添加测试自动化网格下出租房中的巡场情况信息
    @para: 
    @return: 如果添加成功，则返回True；否则返回False  
'''
def add_XunChangQingKuang(xunChangDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增巡场情况开始..")
    response = pinganjianshe_post(url='/plugin/serviceTeam/serviceRecord/addServiceRecord.action', postdata=xunChangDict, username=username, password=password)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增巡场情况成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增巡场情况失败")
    return response

'''  
    @功能： 修改测试自动化网格下出租房中的巡场情况信息
    @para: 
    @return: 如果修改成功，则返回True；否则返回False  
'''
def edit_XunChangQingKuang(xunChangDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "修改巡场情况开始..")
    response = pinganjianshe_post(url='/plugin/serviceTeam/serviceRecord/editServiceRecord.action', postdata=xunChangDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "修改巡场情况成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "修改巡场情况失败")
    return response

'''  
    @功能： 删除测试自动化网格下出租房中的巡场情况信息
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
'''
def delete_XunChangQingKuang(xunChangDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "删除巡场情况开始..")
    response = pinganjianshe_get(url='/plugin/serviceTeam/serviceRecord/deleteServiceRecords.action', param=xunChangDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除巡场情况成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "删除巡场情况失败")
    return response

'''  
    @功能： 检查测试自动化网格下出租房中的治安负责人信息
    @para: 
    @return: 如果检查成功，则返回True；否则返回False  
'''
def check_XunChangQingKuang(xunChangDict, objectIds=None, orgId = None,username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "检查巡场情况开始..")
    try:
        compDict = copy.deepcopy(ShiYouFangWuPara.getRecordDict)
        compDict['objectIds']= objectIds
        compDict['serviceRecordVo.organization.id']= orgId
        response = pinganjianshe_post(url='/plugin/serviceTeam/serviceRecord/findServiceRecords.action', postdata=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(xunChangDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到巡场情况信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到巡场情况信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查巡场情况信息失败")
        return False

'''  
    @功能： 检查测试自动化网格下的出租房信息
    @para: 
    @return: 如果检查成功，则返回True；否则返回False  
'''
def check_ChuZuFang(chuZuDict, orgId=None, username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "检查出租房开始..")
    try:
        compDict = copy.deepcopy(ShiYouFangWuPara.getChuZuDict)
        compDict['orgId']= orgId
        response = pinganjianshe_get(url='/baseinfo/rentalHouseManage/searchHouseInfo.action', param=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(chuZuDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到出租房信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到出租房信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查出租房信息失败")
        return False
    
    
'''
    @功能： 删除测试自动化网格下的实有房屋，出租房信息
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
'''    
def deleteAllActualHouse():
    try:
        #删除实有房屋
        if CommonIntf.getDbQueryResult(dbCommand='select count(*) from HOUSEINFO') != 0: 
            compDict = copy.deepcopy(ShiYouFangWuPara.deleteFangWuDict)
            compDict['orgId']= orgInit['DftSheQuOrgId']
            response = pinganjianshe_get(url='/baseinfo/actualHouseManage/houseInfoList.action', param=compDict)  
            responseDict = json.loads(response.text)
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无实有房屋')
            else:
                for dictListItem in responseDict['rows']:
                    deleteDict = {'houseIds':dictListItem['id']}
                    delete_ShiYouFangWu(deleteDict)
        #删除出租房
        if CommonIntf.getDbQueryResult(dbCommand='select count(*) from HOUSEINFO') != 0: 
            compDict = copy.deepcopy(ShiYouFangWuPara.getChuZuDict)
            compDict['orgId']= orgInit['DftSheQuOrgId']
            response = pinganjianshe_get(url='/baseinfo/rentalHouseManage/searchHouseInfo.action', param=compDict)  
            responseDict = json.loads(response.text)
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无出租房')
            else:
                for dictListItem in responseDict['rows']:
                    deleteDict = copy.deepcopy(ShiYouFangWuPara.deleteFangWuDict)
                    deleteDict['houseIds']=dictListItem['id']
                    delete_ChuZuFang(deleteDict)
                                                 
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '删除失败')
        return False     
    return True