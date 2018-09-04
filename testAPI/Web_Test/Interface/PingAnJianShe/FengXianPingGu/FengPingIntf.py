# -*- coding:UTF-8 -*-
'''
Created on 2015-11-18

@author: N-266
'''
from __future__ import unicode_literals
import json
from Web_Test.Interface.PingAnJianShe.FengXianPingGu import FengPingPara
from Web_Test.CONFIG.InitDefaultPara import orgInit
import copy
from Web_Test.CONFIG.Define import LogLevel
from Web_Test.COMMON import Log, CommonUtil
from Web_Test.Interface.PingAnJianShe.pingAnJianSheHttpCommon import pinganjianshe_post,\
pinganjianshe_get

def addRisk(riskDict, username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "新增计划项目开始")
        response = pinganjianshe_post(url='/risk/riskProjectReport/addRiskProjectReport.action', postdata=riskDict, username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, '新增计划项目成功')
        else:
            Log.LogOutput(LogLevel.ERROR, '新增计划项目失败')
        return response
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '新增失败')
        return False  
# 检查是否可以查询到新增的计划项目    —— 搜索功能
def checkAddRisk(riskDict, orgId=None, username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "开始检查新增的计划项目")
        getRiskDict = copy.deepcopy(FengPingPara.checkLookPlanParam)
        getRiskDict['riskProjectReport.createOrgId']= orgInit['DftWangGeOrgId']
        response = pinganjianshe_get(url='/risk/riskProjectReport/findRiskProjectReportPage.action', param=getRiskDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict=responseDict['rows']
        if CommonUtil.findDictInDictlist(riskDict, listDict) is True:       
            Log.LogOutput(LogLevel.DEBUG, "新增成功，检查到计划项目")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "新增失败，未检查到计划项目")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '检查失败')
            return False  
#修改
def updateRisk(riskObject,username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "开始修改计划项目")
        response = pinganjianshe_post(url='/risk/riskProjectReport/updateRiskProjectReport.action', postdata=riskObject,username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, '修改计划项目成功')
        else:
            Log.LogOutput(LogLevel.ERROR, '修改计划项目失败')
        return response
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '检查失败')
        return False

#检查修改是否成功
def checkUpdateRisk(riskDict, orgId=None, username = None, password = None):
    try: 
        Log.LogOutput(LogLevel.INFO, "开始检查修改计划项目")
        getRiskDict = copy.deepcopy(FengPingPara.getRiskOrgDict)
        getRiskDict['riskProjectReport.id']= orgId
        response = pinganjianshe_get(url='/risk/riskProjectReport/findRiskProjectReportPage.action', param=getRiskDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict=responseDict['rows']
        if CommonUtil.findDictInDictlist(riskDict, listDict) is True:
            Log.LogOutput(LogLevel.INFO, "检查到修改的计划项目")
            return True
        else:
            Log.LogOutput(LogLevel.ERROR, "未检查到修改的计划项目")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '检查失败')
        return False
def deleteRisk(riskObject,username = None, password = None):#删除
    try:
        Log.LogOutput(LogLevel.INFO, "开始删除项目")
        response = pinganjianshe_get(url='/risk/riskProjectReport/deleteRiskProjectReportById.action', param=riskObject,username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "删除项目成功")
        else:
            Log.LogOutput(LogLevel.ERROR, "删除项目失败")
        return response
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '检查失败')
        return False
def deleteRisk_1(riskObject,username = None, password = None):#删除
    try:
        Log.LogOutput(LogLevel.INFO, "开始删除项目")
        response = pinganjianshe_get(url='/risk/riskDecisionTrackEvent/deleteRiskDecisionTrackEventById.action', param=riskObject,username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "决策实施跟踪删除项目成功")
        else:
            Log.LogOutput(LogLevel.ERROR, "决策实施跟踪删除项目失败")
        return response
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '检查失败')
        return False

#验证删除是否成功
def checkDeleteRisk(riskDict, orgId=None,username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "开始检查删除项目")
        getRiskDict = copy.deepcopy(FengPingPara.getRiskOrgDict)
        getRiskDict['riskProjectReportIds']= orgId
        response = pinganjianshe_get(url='/risk/riskProjectReport/findRiskProjectReportPage.action', param=riskDict,username=username, password = password)
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(riskDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到项目")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到项目，项目可能已经被删除")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '检查失败')
        return False

def zanhuanRisk(riskDict,username = None, password = None):#暂缓
    try:
        Log.LogOutput(LogLevel.INFO, "开始暂缓项目")
        response = pinganjianshe_get(url='/risk/riskProjectReport/operationRiskProjectReport.action', param=riskDict,username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "暂缓项目操作成功")
        else:
            Log.LogOutput(LogLevel.ERROR, "暂缓项目操作失败")
        return response
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '检查失败')
        return False
def checkZanHuanRisk(riskObject,username = None, password = None):#通过修改项目的方式，检查暂缓是否成功
    try:
        Log.LogOutput(LogLevel.INFO, "开始检查暂缓项目")
        response = pinganjianshe_post(url='/risk/riskProjectReport/updateRiskProjectReport.action', postdata=riskObject,username=username, password=password)
        if CommonUtil.regMatchString(response.text,"计划管理被暂缓"):
            Log.LogOutput(LogLevel.INFO, '操作项目失败,暂缓项目成功')
            return True
        else:
            Log.LogOutput(LogLevel.ERROR, '操作项目成功，暂缓失败')
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '检查失败')
        return False
def QuXiaozanhuanRisk(riskDict,username = None, password = None):#取消暂缓
    try:
        Log.LogOutput(LogLevel.INFO, "开始取消暂缓项目")
        response = pinganjianshe_get(url='/risk/riskProjectReport/operationRiskProjectReport.action', param=riskDict,username=username, password=password)
    #     Log.LogOutput(LogLevel.DEBUG, response.text)
        responseDict = json.loads(response.text)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "取消暂缓项目成功")
        else:
            Log.LogOutput(LogLevel.ERROR, "取消暂缓项目失败")
        return responseDict
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '检查失败')
        return False
#验证取消暂缓是否成功
def checkQuXiaoZanHuanRisk(riskDict, orgId=None,username = None, password = None):#检查取消暂缓是否成功
    try:
        Log.LogOutput(LogLevel.INFO, "开始检查取消暂缓项目")
        response = pinganjianshe_get(url='/risk/riskProjectReport/updateRiskProjectReport.action', param=riskDict,username=username, password = password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, '操作项目成功，取消暂缓成功')
            return True
        else:
            Log.LogOutput(LogLevel.ERROR, '操作项目失败，取消暂缓失败')
            return False
        return response
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '检查失败')
        return False
        
#调整
def adjustRisk(riskDict,username = None, password = None):#调整项目
    try:
        Log.LogOutput(LogLevel.INFO, "开始调整项目")
        response = pinganjianshe_get(url='/risk/riskProjectReport/updateAdjustmentByIds.action', param=riskDict,username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "调整项目成功")
            return True
        else:
            Log.LogOutput(LogLevel.ERROR, "调整项目失败")
            return False
        return response
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '检查失败')
        return False
def checkAdjustRisk(riskDict, orgId=None,username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "开始检查调整的项目")
        getRiskDict = copy.deepcopy(FengPingPara.getRiskOrgDict)
        getRiskDict['riskProjectReportIds']= orgId
        response = pinganjianshe_get(url='/risk/riskProjectReport/findRiskProjectReportPage.action', param=riskDict,username=username, password = password)
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(riskDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到项目,项目调整失败")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到项目，项目调整成功")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '检查失败')
        return False


def QuXiaoAdjustRisk(riskDict,username = None, password = None):#取消调整
    try:
        Log.LogOutput(LogLevel.INFO, "开始取消调整项目") 
        response = pinganjianshe_get(url='/risk/riskProjectReport/updateAdjustmentByIds.action', param=riskDict,username=username, password=password)
        responseDict = json.loads(response.text)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "取消调整项目成功操作")
        else:
            Log.LogOutput(LogLevel.ERROR, "取消调整项目失败")
        return responseDict
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '检查失败')
        return False
def checkQuXiaoAdjustRisk(riskDict, orgId=None,username = None, password = None):#检查取消调整是否成功
    try:
        Log.LogOutput(LogLevel.INFO, "开始检查取消调整项目") 
        response = pinganjianshe_get(url='/risk/riskProjectReport/updateRiskProjectReport.action', param=riskDict,username=username, password = password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, '操作项目成功，取消调整成功')
            return True
        else:
            Log.LogOutput(LogLevel.ERROR, '操作项目失败，取消计划调整失败')
            return False
        return response
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '检查失败')
        return False

def SaveInitiationRisk(riskDict, username = None, password = None):#保存评估立项
    try:
        Log.LogOutput(LogLevel.INFO, "开始检查评估立项保存的项目") 
        response = pinganjianshe_post(url='/risk/riskProjectReport/evaluatePlan.action', postdata=riskDict, username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO,'评估立项保存成功')
        else:
            Log.LogOutput(LogLevel.ERROR,'评估立项保存失败')
        return response
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '检查失败')
        return False


#评估立项-提交
def SubmitInitiationRisk(riskDict, username = None, password = None):#提交评估立项
    try:
        Log.LogOutput(LogLevel.INFO, "开始提交评估立项的项目") 
        response = pinganjianshe_post(url='/risk/riskProjectReport/evaluatePlan.action', postdata=riskDict, username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "评估立项提交成功")
        else:
            Log.LogOutput(LogLevel.ERROR,"评估立项提交失败")
        return response.result
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '检查失败')
        return False
#验证是否可以检查到评估立项提交成功的项目
def checkSubmitInitiationRisk(riskDict, orgId=None, username = None, password = None):#检查提交评估立项
    try:
        Log.LogOutput(LogLevel.INFO, "开始检查提交评估立项的项目") 
        getRiskDict = copy.deepcopy(FengPingPara.checkInitiationObject)
        getRiskDict['riskProjectReport.createOrgId']= orgId
        response = pinganjianshe_get(url='/risk/riskProjectReport/findRiskProjectReportPage.action', param=getRiskDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict=responseDict['rows']
        if CommonUtil.findDictInDictlist(riskDict,listDict) is True:
            Log.LogOutput(LogLevel.INFO, "查询到项目，评估立项提交成功")
            return True
        else:
            Log.LogOutput(LogLevel.ERROR, "未查询到项目，评估立项提交失败")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '检查失败')
        return False

def saveMakePlanRisk(riskDict,orgId=None,username=None,password=None):#制定评估方案>保存
#     getRiskDict = copy.deepcopy(FengPingPara.getRiskOrgDict)
#     getRiskDict['riskProjectReport.createOrgId']= orgId
    try:
        Log.LogOutput(LogLevel.INFO, "开始检查制定评估方案>保存的项目")
        response = pinganjianshe_post(url='/risk/riskProjectReport/makeAssessPlan.action',postdata=riskDict,username=username,password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, '制定评估方案保存成功')
        else:
            Log.LogOutput(LogLevel.ERROR, '评估方案保存失败')
        return response
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '检查失败')
        return False
def SubmitMakeplanRisk(riskDict,username=None,password=None):#制定评估方案>提交
    try:
        Log.LogOutput(LogLevel.INFO, "开始检查制定评估方案>提交项目") 
        response = pinganjianshe_post(url='/risk/riskProjectReport/makeAssessPlan.action',postdata=riskDict,username=username,password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, '制定评估方案提交成功')
        else:
            Log.LogOutput(LogLevel.ERROR,'评估方案提交失败')
        return response
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '检查失败')
        return False

def checkSubmitMakeplanRisk(riskDict, orgId=None, username = None, password = None):#检查制定评估方案提交
    try:
        Log.LogOutput(LogLevel.INFO, "开始检查制定评估方案>提交的项目")
        getRiskDict = copy.deepcopy(FengPingPara.checkMakeplanObject)
        getRiskDict['riskProjectReport.createOrgId']= orgInit['DftWangGeOrgId']
        response = pinganjianshe_get(url='/risk/riskAssessMeasure/findRiskAssessMeasurePage.action', param=getRiskDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict=responseDict['rows']
        if CommonUtil.findDictInDictlist(riskDict,listDict) is True:
            Log.LogOutput(LogLevel.INFO, "检查制定评估方案提交成功")
            return True
        else:
            Log.LogOutput(LogLevel.ERROR, "检查制定评估方案提交失败")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '检查失败')
        return False


def saveMeasureRisk(riskDict,username=None,password=None): #评估实施>评估，保存
    try:
        Log.LogOutput(LogLevel.INFO, "开始评估实施>评估，保存项目")
        response=pinganjianshe_post(url='/risk/riskAssessMeasure/addRiskAssessMeasure.action',postdata=riskDict,username=username,password=password)
        if response.result is True:       
            Log.LogOutput(LogLevel.INFO, '公示公告信息保存成功')
        else:
            Log.LogOutput(LogLevel.ERROR, '公示公告信息保存失败')
        return response
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '检查失败')
        return False
def saveMeasureRisk_1(riskDict,username=None,password=None): #评估实施>评估，保存
    try:
        Log.LogOutput(LogLevel.INFO, "开始评估实施>评估，保存项目")
        response=pinganjianshe_post(url='/risk/riskAssessMeasure/addRiskAssessMeasure.action',postdata=riskDict,username=username,password=password)
        if response.result is True:       
            Log.LogOutput(LogLevel.INFO, '公示公告信息保存成功')
        else:
            Log.LogOutput(LogLevel.ERROR, '公示公告信息保存失败')
        return response
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '检查失败')
        return False
# 评估实施>评估，提交
def SubmitmeasureRisk(riskDict,username=None,password=None):#评估实施>评估，提交
    try:
        Log.LogOutput(LogLevel.INFO, "开始评估实施>评估，提交项目")
        response=pinganjianshe_post(url='/risk/riskAssessMeasure/submitRiskAssessMeasure.action',postdata=riskDict,username=username,password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO,'评估实施提交成功')
        else:
            Log.LogOutput(LogLevel.ERROR,'评估实施提交失败')
        return response
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '检查失败')
        return False
#检查评估实施>提交，是否提交成功
def checkSubmitMeasureRisk(riskDict,orgId=None,username=None,password=None):#检查评估实施>评估，提交
    try:
        Log.LogOutput(LogLevel.INFO, "开始检查评估实施>评估，提交")
        getRiskDict = copy.deepcopy(FengPingPara.checkMeasureRisk)
        getRiskDict['riskProjectReport.createOrgId']= orgId
        response = pinganjianshe_get(url='/risk/riskAssessSuggest/findRiskAssessSuggestPage.action', param=getRiskDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict=responseDict['rows']
        if CommonUtil.findDictInDictlist(riskDict,listDict) is True:
            Log.LogOutput(LogLevel.INFO, "查询到项目，评估实施提交成功")
            return True
        else:
            Log.LogOutput(LogLevel.ERROR, "检查评估实施提交失败")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '检查失败')
        return False
#检查评估实施>提交，是否提交成功，评估方式为网上联评
def checkSubmitMeasureRisk_01(riskDict,orgId=None,username=None,password=None):#检查评估实施>评估，提交
    try:
        Log.LogOutput(LogLevel.INFO, "开始检查评估实施>评估，提交")
        getRiskDict = copy.deepcopy(FengPingPara.checkMeasureRisk)
        getRiskDict['riskProjectReport.createOrgId']= orgId
        response = pinganjianshe_get(url='/risk/riskAssessSuggest/findRiskAssessSuggestPage.action', param=getRiskDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict=responseDict['rows']
        if CommonUtil.findDictInDictlist(riskDict,listDict) is True:
            Log.LogOutput(LogLevel.INFO, "查询到项目，评估实施提交成功")
            return True
        else:
            Log.LogOutput(LogLevel.ERROR, "检查评估实施提交失败")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '检查失败')
        return False
def checkSubmitMeasureRisk_02(riskDict,orgId=None,username=None,password=None):#检查评估实施>评估，提交
    try:
        Log.LogOutput(LogLevel.INFO, "开始检查评估实施>评估，提交") 
        getRiskDict = copy.deepcopy(FengPingPara.checkMeasureRisk)
        getRiskDict['riskProjectReport.createOrgId']= orgId
        response = pinganjianshe_get(url='/risk/riskAssessSuggest/findRiskAssessSuggestPage.action', param=getRiskDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict=responseDict['rows']
        if CommonUtil.findDictInDictlist(riskDict,listDict) is True:
            Log.LogOutput(LogLevel.INFO, "查询到项目，评估实施提交成功")
            return True
        else:
            Log.LogOutput(LogLevel.ERROR, "检查评估实施提交失败")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '检查失败')
        return False
def deleteAllRisk():#全部删除
    try:
        riskDict = copy.deepcopy(FengPingPara.getRiskOrgDict)
        riskDict['riskProjectReport.createOrgId']= orgInit['DftWangGeOrgId']
        response = pinganjianshe_get(url='/risk/riskProjectReport/findRiskProjectReportPage.action', param=riskDict)
        responseDict = json.loads(response.text)
        if responseDict['records'] == 0:
            Log.LogOutput(LogLevel.DEBUG, '无风险项目')
        else:
            for dictListItem in responseDict['rows']:
                deleteDict = {'riskProjectReportIds':dictListItem['id']}
                deleteRisk(deleteDict)
#     except Exception , e:
#         Log.LogOutput(LogLevel.ERROR, '项目删除失败')
#         return False     
#     return True  
        Log.LogOutput(LogLevel.INFO, "开始删除决策实施跟踪的项目") 
        riskDict = copy.deepcopy(FengPingPara.deleteAllRisk_1)
        riskDict['riskProjectReport.createOrgId']= orgInit['DftWangGeOrgId']
        response = pinganjianshe_get(url='/risk/riskDecisionTrackEvent/findRiskDecisionTrackEventPage.action', param=riskDict)
        responseDict = json.loads(response.text)
        if responseDict['records'] == 0:
            Log.LogOutput(LogLevel.DEBUG, '无风险项目')
        else:
            for dictListItem in responseDict['rows']:
                deleteDict_1 = {'riskProjectReportIds':dictListItem['projectId']}
                deleteRisk_1(deleteDict_1)
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '决策实施跟踪项目删除失败')
        return False     

# 回退
def backRisk(riskDict,username=None,password=None):
    try:
        Log.LogOutput(LogLevel.INFO, "开始回退") 
        response=pinganjianshe_post(url='/risk/riskAssessMeasure/backRiskAssessMeasure.action', postdata=riskDict, username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, '回退成功')
        else:
            Log.LogOutput(LogLevel.ERROR, '回退失败')
        return response
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '检查失败')
        return False

def checkBackRisk(riskDict,orgId=None,username=None,password=None):#检查回退是否成功
    try:
        Log.LogOutput(LogLevel.INFO, "开始检查回退是否成功") 
        getRiskDict = copy.deepcopy(FengPingPara.GetBackParam)
        getRiskDict['riskProjectReport.createOrgId']= orgId
        response = pinganjianshe_get(url='/risk/riskProjectReport/findRiskProjectReportPage.action', param=getRiskDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict=responseDict['rows']
        if CommonUtil.findDictInDictlist(riskDict,listDict) is True:
            Log.LogOutput(LogLevel.INFO, "查询到项目，回退项目成功")
            return True
        else:
            Log.LogOutput(LogLevel.ERROR, "未查询到项目，回退项目失败")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '检查失败')
        return False
    
#评估报告>评估建议>保存
def SaveRiskSuggest(riskDict,username=None,password=None):#评估报告>评估建议>保存
    try:
        Log.LogOutput(LogLevel.INFO, "开始评估报告>评估建议>保存") 
        response=pinganjianshe_post(url='/risk/riskAssessSuggest/submitRiskAssessSuggest.action',postdata=riskDict,username=username,password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO,'评估建议保存成功')
        else:
            Log.LogOutput(LogLevel.ERROR, '评估建议保存失败')
        return response
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '检查失败')
        return False
def SubmitRiskSuggest(riskDict,username=None,password=None): #评估报告>评估建议>提交
    try:
        Log.LogOutput(LogLevel.INFO, "开始评估报告>评估建议>提交") 
        response=pinganjianshe_post(url='/risk/riskAssessSuggest/submitRiskAssessSuggest.action',postdata=riskDict,username=username,password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, '评估建议提交成功')
        else:
            Log.LogOutput(LogLevel.ERROR, '评估建议提交失败')
        return response
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '检查失败')
        return False
def CheckSubmitRiskSuggest(riskDict,orgId=None,username=None,password=None):#检查>评估报告>评估建议>提交
    try:
        Log.LogOutput(LogLevel.INFO, "开始检查>评估报告>评估建议>提交") 
        getRiskDict = copy.deepcopy(FengPingPara.getRiskOrgDict)
        getRiskDict['riskProjectReport.createOrgId']= orgId
        response = pinganjianshe_get(url='/risk/riskDecisionAdvice/findRiskDecisionAdvicePage.action', param=getRiskDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict=responseDict['rows']
        if CommonUtil.findDictInDictlist(riskDict,listDict) is True:
            Log.LogOutput(LogLevel.INFO, "查询到项目，评估建议提交成功")
            return True
        else:
            Log.LogOutput(LogLevel.ERROR, "未查询到项目，评估建议提交失败")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '检查失败')
        return False
#决策结果>决策意见保存
def SaveriskDecisionAdvice(riskDict,username=None,password=None):#决策结果>决策意见保存
    try:
        Log.LogOutput(LogLevel.INFO, "开始决策结果>决策意见保存") 
        response=pinganjianshe_post(url='/risk/riskDecisionAdvice/makeRiskDecisionAdvice.action',postdata=riskDict,username=username,password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO,'决策意见保存成功')
        else:
            Log.LogOutput(LogLevel.ERROR, '评估建议保存失败')
        return response
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '检查失败')
        return False
def SubmitRiskDecisionAdvice(riskDict,username=None,password=None):#决策结果>决策意见提交
    try:
        Log.LogOutput(LogLevel.INFO, "开始决策结果>决策意见提交") 
        response=pinganjianshe_post(url='/risk/riskDecisionAdvice/makeRiskDecisionAdvice.action',postdata=riskDict,username=username,password=password)
        
        if response.result is True:
            Log.LogOutput(LogLevel.INFO,'决策意见提交成功')
        else:
            Log.LogOutput(LogLevel.ERROR, '决策意见提交失败')
        return response
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '检查失败')
        return False
def CheckSubmitRiskDecisionAdvice(riskDict,orgId=None,username=None,password=None):#检查>决策结果>决策意见提交
    try:
        Log.LogOutput(LogLevel.INFO, "开始检查决策结果>决策意见提交") 
        getRiskDict = copy.deepcopy(FengPingPara.CheckAdvice)
        getRiskDict['riskProjectReport.createOrgId']= orgId
        response = pinganjianshe_get(url='/risk/riskDecisionTrackEvent/findRiskDecisionTrackEventPage.action', param=getRiskDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict=responseDict['rows']
        if CommonUtil.findDictInDictlist(riskDict,listDict) is True:
           
            Log.LogOutput(LogLevel.INFO, "查询到项目，决策意见提交成功")
            return True
        else:
            Log.LogOutput(LogLevel.ERROR, "未查询到项目，决策意见提交失败")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '检查失败')
        return False
def Riskarchive(riskDict,username=None,password=None):#评估报告>评估建议>保存
    try:
        Log.LogOutput(LogLevel.INFO, "开始检查保存评估建议") 
        response=pinganjianshe_post(url='/risk/riskDecisionTrackEvent/archiveRiskTacking.action',postdata=riskDict,username=username,password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO,'归档成功')
        else:
            Log.LogOutput(LogLevel.ERROR, '归档失败')
        return response
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '检查失败')
        return False
def CheckRiskArchive(riskDict,orgId=None,username=None,password=None):
    try:
        Log.LogOutput(LogLevel.INFO, "开始检查项目归档")
        getRiskDict = copy.deepcopy(FengPingPara.CheckArchiveParam)
        getRiskDict['riskProjectReport.createOrgId']= orgId
        response = pinganjianshe_get(url='/risk/riskArchive/findAllRiskArchiveForPage.action', param=getRiskDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict=responseDict['rows']
        if CommonUtil.findDictInDictlist(riskDict,listDict) is True:
            Log.LogOutput(LogLevel.INFO, "查询到项目，归档成功")
            return True
        else:
            Log.LogOutput(LogLevel.ERROR, "未查询到项目，归档失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '检查失败')
            return False
def addExpert(riskDict,username=None,password=None):#专家库>添加专家
    try:
        Log.LogOutput(LogLevel.INFO, "开始添加专家")
        response=pinganjianshe_post(url='/risk/riskExpert/addRiskExpert.action',postdata=riskDict,username=username,password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO,'新增专家成功')
            return True
        else:
            Log.LogOutput(LogLevel.ERROR, '新增专家失败')
            return False
        return response
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '检查失败')
        return False
def checkAddExpert(riskDict,orgId=None,username=None,password=None):#检查添加专家是否成功
    try:
        Log.LogOutput(LogLevel.INFO, "开始检查添加专家是否成功")
        getRiskDict = copy.deepcopy(FengPingPara.CheckArchiveParam)
        response = pinganjianshe_get(url='/risk/riskExpert/findRiskExpertPage.action', param=getRiskDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict=responseDict['rows']
        if CommonUtil.findDictInDictlist(riskDict,listDict) is True:
            Log.LogOutput(LogLevel.INFO, "查询到专家，新增专家成功")
            return True
        else:
            Log.LogOutput(LogLevel.ERROR, "未查询到专家，新增专家失败")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '检查失败')
        return False
def updateExpert(riskDict,username=None,password=None):#专家库>修改专家
    try:
        Log.LogOutput(LogLevel.INFO, "开始修改专家")
        response=pinganjianshe_post(url='/risk/riskExpert/updateRiskExpert.action',postdata=riskDict,username=username,password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO,'修改专家成功')
        else:
            Log.LogOutput(LogLevel.ERROR, '修改专家失败')
        return response
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '检查失败')
        return False
def checkUpdateExpert(riskDict,orgId=None,username=None,password=None):#检查添加专家是否成功
    try:
        Log.LogOutput(LogLevel.INFO, "开始检查添加专家是否成功")
        getRiskDict = copy.deepcopy(FengPingPara.CheckArchiveParam)
        response = pinganjianshe_get(url='/risk/riskExpert/findRiskExpertPage.action', param=getRiskDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict=responseDict['rows']
        if CommonUtil.findDictInDictlist(riskDict,listDict) is True:
            Log.LogOutput(LogLevel.INFO, "查询到专家，修改专家成功")
            return True
        else:
            Log.LogOutput(LogLevel.ERROR, "未查询到专家，修改专家失败")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '检查失败')
        return False
def importRisk(data, files=None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导入风险项目开始..")
    response = pinganjianshe_post(url='/dataTransfer/importToDomain.action', postdata=data, files=files, username=username, password = password)   
    return response
def downLoadRisk(dldata, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导出风险项目开始..")
    response = pinganjianshe_post(url='/risk/riskDecisionTrackEvent/downloadRiskDecisionTrackEvent.action', postdata=dldata, username=username, password = password)   
    return response


# def checkUpdateExpert(riskDict,username = None, password = None):#检查修改专家是否成功
#  try:
#     Log.LogOutput(LogLevel.INFO, "开始检查修改专家")
#     getRiskDict = copy.deepcopy(FengPingPara.checkUpdateExpert)
# #     getRiskDict['riskProjectReport.createOrgId']= orgInit['DftWangGeOrgId']
#     response = pinganjianshe_get(url='/risk/riskExpert/viewRiskExpert.action', param=getRiskDict,username=username, password = password)
#     responseDict = json.loads(response.text)
#     print responseDict
#     listDict=responseDict['rows']
#     if CommonUtil.findDictInDictlist(riskDict,listDict) is True:
#         Log.LogOutput(LogLevel.INFO, "修改专家成功")
#         return True
#     else:
#         Log.LogOutput(LogLevel.ERROR, "修改专家失败")
#         return False
#  except Exception:
#             Log.LogOutput(LogLevel.ERROR, '检查失败')
#             return False
