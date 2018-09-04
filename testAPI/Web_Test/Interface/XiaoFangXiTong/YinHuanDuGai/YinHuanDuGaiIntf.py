# -*- coding:UTF-8 -*-
'''
Created on 2016-6-7

@author: chenyan
'''
from __future__ import unicode_literals
from CONFIG.Define import LogLevel

import copy
import json
from Interface.XiaoFangXiTong.YinHuanDuGai import YinHuanDuGaiPara
from COMMON import Log, CommonUtil
from Interface.XiaoFangXiTong.xiaoFangXiTongHttpCommon import xiaofang_post,\
    xiaofang_get
from Interface.XiaoFangXiTong.Common import CommonIntf
from Interface.XiaoFangXiTong.Common.InitDefaultPara import orgInit




'''
    @功能： 单位类型配置
'''    
def add_SaveSuperviseType(Dict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增单位类型开始..")        
    response = xiaofang_post(url='/sysCodeManage/saveSuperviseType.action', postdata=Dict, username=username, password=password)
    return response
# 
# '''  
#     @功能： 检查隐患项
#     @para: 
#     @return: 如果检查成功，则返回True；否则返回False  
# '''
# def check_PreviewList(Dict, previewData=None, username = None, password = None):
#     Log.LogOutput(LogLevel.DEBUG, "检查住户信息开始..")
#     try:
#         compDict = copy.deepcopy(YinHuanDuGaiPara.PreviewList)
#         compDict['previewData']= previewData
#         response = xiaofangxitong_post(url='/sysCodeManage/getPreviewList.action', param=compDict,username=username, password = password)  
#         responseDict = json.loads(response.text)
#         if CommonUtil.findDictInDictlist(Dict, responseDict['rows']) is True:
#             Log.LogOutput(LogLevel.DEBUG, "检查到住户信息信息")
#             return True
#         else:
#             Log.LogOutput(LogLevel.DEBUG, "未检查到住户信息信息")
#             return False
#     except Exception:
#         Log.LogOutput(LogLevel.ERROR, "检查实有房屋信息失败")
#         return False
#     

'''
    @功能： 单位火灾隐患类型配置
'''    
def add_Type(Dict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "配置火灾隐患类型开始..")        
    response = xiaofang_post(url='/sysCodeManage/saveSuperviseTypeItem.action', postdata=Dict, username=username, password=password)
    return response

'''
    @功能： 新增/修改单位
'''    
def addOrEdit_fireCompany(Dict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增/修改单位开始..")        
    response = xiaofang_post(url='/fire/fireCompanyInfoManage/saveOrUpdateFireCompanyInfo.action', postdata=Dict, username=username, password=password)
    return response

'''
    @功能： 删除单位
'''    
def delete_fireCompany(Dict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "删除单位开始..")        
    response = xiaofang_get(url='/fire/fireCompanyInfoManage/deleteFireCompanyInfo.action', param=Dict, username=username, password=password)
    return response

'''  
    @功能： 搜索/检查单位信息
    @para: 
    @return: 如果搜索/检查成功，则返回True；否则返回False  
'''
def check_fireCompany(Dict, orgId=None, companyName=None,levelShow=None,username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "搜索/检查单位信息开始..")
    try:
        compDict = copy.deepcopy(YinHuanDuGaiPara.getFireCompanyDict)
        compDict['orgId']= orgId  
        compDict['fireCompanyInfo.companyName']= companyName  
        compDict['fireCompanyInfo.levelShow']= levelShow  
        response = xiaofang_get(url='/fire/fireCompanyInfoManage/queryFireCompanyInfoForSelectList.action', param=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
#         print response.text
        if CommonUtil.findDictInDictlist(Dict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "搜索/检查到单位信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未搜索/检查到单位信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "搜索/检查单位信息失败")
        return False


'''  
    @功能： 导入单位信息
    @para: 
    @return: 如果导入成功，则返回True；否则返回False  
'''
def import_DanWei(data, files=None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导入单位信息开始..")
    response = xiaofang_post(url='/dataCommon/importToDomain.action', postdata=data, files=files, username=username, password = password)   
    return response

'''  
    @功能： 导出测试自动化网格下的户籍人口信息
    @para: 
    @return: 如果导出成功，则返回True；否则返回False  
'''    
def downLoad_DanWei(dldata, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导出单位开始..")
    response = xiaofang_post(url='/fire/fireCompanyInfoManage/downloadFireCompanyInfo.action', postdata=dldata, username=username, password = password)   
    return response
    
    
'''
    @功能： 转移单位
'''    
def change_fireCompany(Dict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "转移单位开始..")        
    response = xiaofang_post(url='/plugin/fireCompanyChange/orgfireCompanyChange/changeCompanyInfo.action', postdata=Dict, username=username, password=password)
    return response


'''
    @功能： 单位添加日常检查
'''    
def saveFiretrapSupervise(Dict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "单位添加日常检查开始..")        
    response = xiaofang_post(url='/fire/firetrapSuperviseManage/saveFiretrapSupervise.action', postdata=Dict, username=username, password=password)
    return response

'''  
    @功能： 搜索/检查
    @para: 
    @return: 如果搜索/检查成功，则返回True；否则返回False  
'''
def check_saveFiretrapSupervise(Dict,companyName=None, orgId=None, allStateSearch=None,publicString=None,username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "搜索/检查开始..")
    try:
        compDict = copy.deepcopy(YinHuanDuGaiPara.getSaveFiretrapSuperviseDict)
        compDict['firetrapSupervise.fireCompanyInfo.companyName']=companyName
        compDict['queryParameter.orgId']= orgId  
        compDict['queryParameter.allStateSearch']= allStateSearch  
        compDict['queryParameter.publicString']= publicString  
        response = xiaofang_get(url='/fire/firetrapSuperviseManage/getFiretrapSuperviseList.action', param=compDict,username=username, password = password)  
        print response.text
        responseDict = json.loads(response.text)
        for item in responseDict['rows']:
            if CommonUtil.findDictInDictlist(Dict, [item['fireCompanyInfo']]) is True:
                Log.LogOutput(LogLevel.DEBUG, "搜索/检查到信息")
                return responseDict
            else:
                Log.LogOutput(LogLevel.DEBUG, "未搜索/检查到信息")
                return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "搜索/检查失败")
        return False


'''
    @功能： 删除日常检查
'''    
def delete_saveFiretrapSupervise(Dict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "删除日常检查开始..")        
    response = xiaofang_get(url='/fire/companyCheckRecordManage/deleteCompanyCheckRecord.action', param=Dict, username=username, password=password)
    return response

'''
    @功能： 复查
'''    
def SaveFiretrapReview(Dict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "复查开始..")        
    response = xiaofang_post(url='/fire/firetrapReviewManage/saveFiretrapReview.action', postdata=Dict, username=username, password=password)
    return response

'''
    @功能： 上报
'''    
def saveCompanyCheckRecordTask(Dict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "上报开始..")        
    response = xiaofang_post(url='/fire/companyCheckRecordManage/saveCompanyCheckRecordTask.action', postdata=Dict, username=username, password=password)
    return response

'''  
    @功能： 搜索/检查
    @para: 
    @return: 如果搜索/检查成功，则返回True；否则返回False  
'''
def check_CompanyCheckRecordTask(Dict, orgId=None, allStateSearch=None,publicString=None,username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "搜索/检查开始..")
    try:
        compDict = copy.deepcopy(YinHuanDuGaiPara.getCompanyCheckRecordTaskDict)
        compDict['queryParameter.orgId']= orgId  
        compDict['queryParameter.allStateSearch']= allStateSearch  
        compDict['queryParameter.publicString']= publicString  
        response = xiaofang_get(url='/fire/firetrapSuperviseManage/getFiretrapSuperviseList.action', param=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        for item in responseDict['rows']:
            if CommonUtil.findDictInDictlist(Dict, [item['fireCompanyInfo']]) is True:
                Log.LogOutput(LogLevel.DEBUG, "搜索/检查到信息")
                return responseDict
            else:
                Log.LogOutput(LogLevel.DEBUG, "未搜索/检查到信息")
                return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "搜索/检查失败")
        return False

    
'''
    @功能： 删除上报督改检查项
'''    
def delete_FiretrapReview(Dict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "删除上报督改检查项开始..")        
    response = xiaofang_get(url='/fire/companyCheckRecordManage/deleteCompanyCheckRecord.action', param=Dict, username=username, password=password)
    return response
    
'''
    @功能： 单位添加举报检查
'''    
def saveComplaintHandle(Dict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "单位添加举报检查开始..")        
    response = xiaofang_post(url='/fire/companyCheckRecordManage/saveComplaintHandleInfo.action', postdata=Dict, username=username, password=password)
    return response

'''
    @功能： 新增/修改专项任务
'''    
def saveFirecheckTask(Dict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增/修改专项任务..")        
    response = xiaofang_post(url='/fire/firecheckTaskManage/saveFirecheckTask.action', postdata=Dict, username=username, password=password)
    return response
    
'''
    @功能： 检查专项任务
'''  
def checkSaveFirecheckTask(companyDict, orgId=None, username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "检查专项任务开始..")
        compDict = copy.deepcopy(YinHuanDuGaiPara.getFirecheckTaskDict)
        compDict['getorgId']= orgId
        response = xiaofang_get(url='/fire/firecheckTaskManage/getFirecheckTaskList.action', param=compDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict= responseDict['rows']
        if CommonUtil.findDictInDictlist(companyDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到专项任务信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到专项任务信息")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '检查专项任务失败')
            return False  
        
'''
    @功能： 删除专项任务
'''    
def deleteSaveFirecheckTask(Dict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "删除专项任务开始..")        
    response = xiaofang_get(url='/fire/firecheckTaskManage/deleteFirecheckTaskById.action', param=Dict, username=username, password=password)
    return response
    
'''
    @功能： 专项任务分派
'''    
def saveTaskItem(Dict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "专项任务分派开始..")        
    response = xiaofang_get(url='/fire/firecheckTaskManage/saveTaskItem.action', param=Dict, username=username, password=password)
    return response
    
'''
    @功能： 保存分派专项任务
'''    
def saveItem(Dict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "保存分派专项任务开始..")        
    response = xiaofang_get(url='/fire/firecheckTaskManage/doFirecheckTask.action', param=Dict, username=username, password=password)
    return response
    
'''  
    @功能： 检查/搜索专项任务
    @para: 
    @return: 如果检查/搜索成功，则返回True；否则返回False  
'''
def check_saveTaskItem(Dict,state=None, orgId=None, companyName=None,allStateSearch=None,publicString=None,username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "检查/搜索专项任务开始..")
    try:
        compDict = copy.deepcopy(YinHuanDuGaiPara.getSaveTaskItemDict)
        compDict['orgId']= orgId 
        compDict['state']= state 
        compDict['firetrapSupervise.fireCompanyInfo.companyName']=companyName
        compDict['queryParameter.orgId']= orgId  
        compDict['queryParameter.allStateSearch']= allStateSearch  
        compDict['queryParameter.publicString']= publicString  
        response = xiaofang_get(url='/fire/firetrapSuperviseManage/getFiretrapSuperviseList.action', param=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        for item in responseDict['rows']:
            if CommonUtil.findDictInDictlist(Dict, [item['fireCompanyInfo']]) is True:
                Log.LogOutput(LogLevel.DEBUG, "检查/搜索到专项任务信息")
                return responseDict
            else:
                Log.LogOutput(LogLevel.DEBUG, "未检查/搜索到专项任务信息")
                return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查/搜索专项任务失败")
        return False

'''
    @功能： 删除专项任务
'''    
def delete_saveTaskItem(Dict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "删除专项任务开始..")        
    response = xiaofang_get(url='/fire/companyCheckRecordManage/deleteCompanyCheckRecord.action', param=Dict, username=username, password=password)
    return response

'''
    @功能： 分派
'''    
def assignCheckRecord(Dict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "分派开始..")        
    response = xiaofang_post(url='/fire/companyCheckRecordManage/assignCheckRecord.action', postdata=Dict, username=username, password=password)
    return response

'''  
    @功能： 搜索/检查分派
    @para: 
    @return: 如果搜索/检查分派成功，则返回True；否则返回False  
'''
def check_assignCheckRecord(Dict,companyName=None, orgId=None, allStateSearch=None,publicString=None,username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "搜索/检查分派开始..")
    try:
        compDict = copy.deepcopy(YinHuanDuGaiPara.getAssignCheckRecordDict)
#         compDict['firetrapSupervise.fireCompanyInfo.companyName']=companyName
        compDict['queryParameter.orgId']= orgId  
        compDict['queryParameter.allStateSearch']= allStateSearch  
        compDict['queryParameter.publicString']= publicString  
        response = xiaofang_get(url='/fire/firetrapSuperviseManage/getFiretrapSuperviseListForAssign.action', param=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        for item in responseDict['rows']:
            if CommonUtil.findDictInDictlist(Dict, [item['fireCompanyInfo']]) is True:
                Log.LogOutput(LogLevel.DEBUG, "搜索/检查到信息")
                return responseDict
            else:
                Log.LogOutput(LogLevel.DEBUG, "未搜索/检查到信息")
                return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "搜索/检查失败")
        return False

'''  
    @功能： 搜索/检查下辖检查记录
    @para: 
    @return: 如果搜索/检查成功，则返回True；否则返回False  
'''
def check_SubordinateList(Dict,companyName=None,query=None, orgId=None, allStateSearch=None,publicString=None,username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "搜索/检查下辖检查记录开始..")
    try:
        compDict = copy.deepcopy(YinHuanDuGaiPara.getSubordinateListDict)
        compDict['firetrapSupervise.fireCompanyInfo.companyName']=companyName
        compDict['orgId']= orgId 
        compDict['queryParameter.orgId']= orgId  
        compDict['firetrapSupervise.orgIdForSearch']= orgId  
        compDict['queryParameter.allStateSearch']= allStateSearch  
        compDict['queryParameter.publicString']= publicString  
        compDict['firetrapSupervise.query']= 'query'
        response = xiaofang_get(url='/fire/subordinateController/subordinateList.action', param=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        for item in responseDict['rows']:
            if CommonUtil.findDictInDictlist(Dict, [item['fireCompanyInfo']]) is True:
                Log.LogOutput(LogLevel.DEBUG, "搜索/检查到信息")
                return responseDict
            else:
                Log.LogOutput(LogLevel.DEBUG, "未搜索/检查到信息")
                return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "搜索/检查失败")
        return False

'''
    @功能： 删除下辖检查记录
'''    
def delete_SubordinateList(Dict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "删除下辖检查记录..")        
    response = xiaofang_get(url='/fire/subordinateController/deleteCompanyCheckRecord.action', param=Dict, username=username, password=password)
    return response

'''  
    @功能： 导出下辖检查记录
    @para: 
    @return: 如果导出成功，则返回True；否则返回False  
'''    
def downLoad_JiLu(dldata, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导出记录开始..")
    response = xiaofang_post(url='/fire/subordinateController/downloadSubordinate.action', postdata=dldata, username=username, password = password)   
    return response
 
 
 
def deleteAllDanWei():
    try:
        #删除单位信息
#         if CommonIntf.getDbQueryResult(dbCommand="select count(*) from fire_company_info_id ") != 0:    
            compDict = copy.deepcopy(YinHuanDuGaiPara.getFireCompanyDict)
            compDict['orgId']= orgInit['DftWangGeOrgId1']  
            compDict['fireCompanyInfo.levelShow']= 1  
            response = xiaofang_get(url='/fire/fireCompanyInfoManage/queryFireCompanyInfoForSelectList.action', param=compDict)  
            responseDict = json.loads(response.text)
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无单位信息')
            else:
                for dictListItem in responseDict['rows']:
                    deleteDict = copy.deepcopy(YinHuanDuGaiPara.deleteFireCompanyDict)
                    deleteDict['fireCompanyInfo.updateDept'] = {orgInit['DftWangGeOrgId1']}  
                    deleteDict['fireCompanyInfo.fireCompanyInfoId'] = {dictListItem['fireCompanyInfoId']}
                    delete_fireCompany(deleteDict)
                    
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '删除失败')
        return False     
    return True      