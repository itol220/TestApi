# -*- coding:UTF-8 -*-
'''
Created on 2015-12-16

@author: N-266
'''
from __future__ import unicode_literals
import json
import copy
from CONFIG.Define import LogLevel
from COMMON import CommonUtil
from Interface.PingAnJianShe.pingAnJianSheHttpCommon import pinganjianshe_post,\
pinganjianshe_get
from Interface.PingAnJianShe.YiJiangDaiBu import YiJiangDaiBuPara
from COMMON import Log, Time
from CONFIG.InitDefaultPara import orgInit,userInit
from Interface.PingAnJianShe.Common import CommonIntf
def applyReward(rewardDict, username = None, password = None):#以奖代补>数据录入情况>申请
        Log.LogOutput(LogLevel.INFO, "开始申请")
        response = pinganjianshe_post(url='/rewardtosubsidies/RewardToSubsidiesManager/applyForRewardToSubsidies.action', postdata=rewardDict, username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, '申请成功')
        else:
            Log.LogOutput(LogLevel.ERROR, '申请失败')
        return response

def CheckapplyReward(rewardDict, username = None, password = None):#以奖代补>审核批准>检查申请
    
    try:
        Log.LogOutput(LogLevel.INFO, "开始检查申请")
        getRiskDict = copy.deepcopy(YiJiangDaiBuPara.findApplyReward)
        getRiskDict['rewardToSubsidieId']= CommonIntf.getDbQueryResult(dbCommand = "select max(t.id) from rewardtosubsidies t")
        response = pinganjianshe_get(url='/rewardToSubsidies/rewardToSubsidiesStep/findRewardtoSubsidieIssuesListForPage.action', param=getRiskDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict=responseDict['rows']
        if CommonUtil.findDictInDictlist(rewardDict,listDict) is True:
            Log.LogOutput(LogLevel.INFO, "检查申请成功")
            return True
        else:
            Log.LogOutput(LogLevel.ERROR, "检查申请失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '检查失败')
            return False
def AgreeApplyReward(rewardDict, username = None, password = None):#以奖代补>审核批准>批准
        Log.LogOutput(LogLevel.INFO, "开始批准")
        response = pinganjianshe_post(url='/rewardToSubsidies/rewardToSubsidiesStep/agree.action', postdata=rewardDict, username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, '批准成功')
        else:
            Log.LogOutput(LogLevel.ERROR, '批准失败')
        return response
def CheckAgreeApplyReward(rewardDict, username = None, password = None):#以奖代补>审核批准>检查批准
    try:
        Log.LogOutput(LogLevel.INFO, "开始检查批准")
        getRewardDict = copy.deepcopy(YiJiangDaiBuPara.FindAgreeIssue)
        getRewardDict['searchVo.orgId']=orgInit['DftWangGeOrgId']
        response = pinganjianshe_get(url='/rewardToSubsidies/rewardToSubsidiesStep/findRewardToSubsidiesStepForPage.action', param=getRewardDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict=responseDict['rows']
        
        if CommonUtil.findDictInDictlist(rewardDict,listDict) is True:
            Log.LogOutput(LogLevel.INFO, "检查批准成功")
            return True
        else:
            Log.LogOutput(LogLevel.ERROR, "检查批准失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '检查失败')
            return False

def ReportReward(rewardDict, username = None, password = None):#以奖代补>审核批准>上报
        Log.LogOutput(LogLevel.INFO, "开始上报")
        response = pinganjianshe_post(url='/rewardToSubsidies/rewardToSubsidiesStep/reportedSubmit.action', postdata=rewardDict, username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, '上报成功')
        else:
            Log.LogOutput(LogLevel.ERROR, '上报失败')
        return response
def CheckReportReward(rewardDict, username = None, password = None):#以奖代补>审核批准>检查上报
    try:
        Log.LogOutput(LogLevel.INFO, "开始检查上报")
        getRewardDict = copy.deepcopy(YiJiangDaiBuPara.FindAgreeIssue)
        getRewardDict['searchVo.orgId']=orgInit['DftSheQuOrgId']
        response = pinganjianshe_get(url='/rewardToSubsidies/rewardToSubsidiesStep/findRewardToSubsidiesStepForPage.action', param=getRewardDict,username=username, password= password)
        responseDict = json.loads(response.text)
        listDict=responseDict['rows']
        if CommonUtil.findDictInDictlist(rewardDict,listDict) is True:
            Log.LogOutput(LogLevel.INFO, "检查上报成功")
            return True
        else:
            Log.LogOutput(LogLevel.ERROR, "检查上报失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '检查失败')
            return False
def DisagreeReward(rewardDict, username = None, password = None):#以奖代补>审核批准>否决
        Log.LogOutput(LogLevel.INFO, "开始否决")
        response = pinganjianshe_post(url='/rewardToSubsidies/rewardToSubsidiesStep/disAgree.action', postdata=rewardDict, username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, '否决成功')
        else:
            Log.LogOutput(LogLevel.ERROR, '否决失败')
        return response
def CheckDisagree(rewardDict, username = None, password = None):#以奖代补>审核批准>检查否决
    try:
        Log.LogOutput(LogLevel.INFO, "开始检查否决")
        getRewardDict = copy.deepcopy(YiJiangDaiBuPara.FindAgreeIssue)
        getRewardDict['searchVo.orgId']=orgInit['DftWangGeOrgId']
        response = pinganjianshe_get(url='/rewardToSubsidies/rewardToSubsidiesStep/findRewardToSubsidiesStepForPage.action', param=getRewardDict,username=username, password= password)
        responseDict = json.loads(response.text)
        listDict=responseDict['rows']
        if CommonUtil.findDictInDictlist(rewardDict,listDict) is True:
            Log.LogOutput(LogLevel.INFO, "检查否决成功")
            return True
        else:
            Log.LogOutput(LogLevel.ERROR, "检查否决失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '检查失败')
            return False
def UpdteReward(rewardDict, username = None, password = None):#以奖代补>审核批准>事件清单编辑
        response = pinganjianshe_get(url='/rewardToSubsidies/rewardToSubsidiesStep/updateRewardtoSubsidieIssues.action', param=rewardDict,username=username, password= password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "事件处理清单编辑删除成功")
            return True
        else:
            Log.LogOutput(LogLevel.ERROR, "事件处理清单编辑删除失败")
            return False
def checkUpdteReward(rewardDict, username = None, password = None):#检查事件处理清单编辑删除是否成功
    try:
        Log.LogOutput(LogLevel.INFO, "开始检查事件处理清单编辑删除")
        getRewardDict = copy.deepcopy(YiJiangDaiBuPara.findIssue)
        getRewardDict['rewardToSubsidieId']=CommonIntf.getDbQueryResult(dbCommand = "select max(t.id) from rewardtosubsidies t")
        response = pinganjianshe_get(url='/rewardToSubsidies/rewardToSubsidiesStep/findRewardtoSubsidieIssuesListForPage.action', param=getRewardDict,username=username, password= password)
        responseDict = json.loads(response.text)
        listDict=responseDict['rows']
        if CommonUtil.findDictInDictlist(rewardDict,listDict) is True:
            Log.LogOutput(LogLevel.ERROR, "检查事件处理清单编辑删除失败")
            return True
        else:
            Log.LogOutput(LogLevel.INFO, "检查事件处理清单编辑删除成功")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '检查失败')
            return False
def ResetReward(rewardDict, username = None, password = None):#以奖代补>审核批准>重置
        response = pinganjianshe_get(url='/rewardToSubsidies/rewardToSubsidiesStep/reset.action', param=rewardDict,username=username, password= password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "重置成功")
            return True
        else:
            Log.LogOutput(LogLevel.ERROR, "重置失败")
            return False
def checkResetReward(rewardDict,username = None, password = None):#检查重置是否成功
    try:
        Log.LogOutput(LogLevel.INFO, "开始检查重置")
        getRewardDict = copy.deepcopy(YiJiangDaiBuPara.findReset)
        getRewardDict['searchVo.orgId']=orgInit['DftWangGeOrgId']
        response = pinganjianshe_get(url='/rewardToSubsidies/rewardToSubsidiesStep/findRewardToSubsidiesStepForPage.action', param=getRewardDict,username=username, password= password)
        responseDict = json.loads(response.text)
        listDict=responseDict['rows']
        if CommonUtil.findDictInDictlist(rewardDict,listDict) is True:
            Log.LogOutput(LogLevel.INFO, "检查重置成功")
            return True
        else:
            Log.LogOutput(LogLevel.ERROR, "检查重置失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '检查失败')
            return False
def DeleteReward(rewardDict, username = None, password = None):#以奖代补>审核批准>删除
        response = pinganjianshe_get(url='/rewardToSubsidies/rewardToSubsidiesStep/deleteApproval.action', param=rewardDict,username=username, password= password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "删除待处理状态数据成功")
            return True
        else:
            Log.LogOutput(LogLevel.ERROR, "删除待处理状态数据失败")
            return False
def checkDeleteReward(rewardDict,username = None, password = None):#检查重置是否成功
    try:
        Log.LogOutput(LogLevel.INFO, "开始检查删除")
        getRewardDict = copy.deepcopy(YiJiangDaiBuPara.findReset)
        getRewardDict['searchVo.orgId']=orgInit['DftWangGeOrgId']
        response = pinganjianshe_get(url='/rewardToSubsidies/rewardToSubsidiesStep/findRewardToSubsidiesStepForPage.action', param=getRewardDict,username=username, password= password)
        responseDict = json.loads(response.text)
        listDict=responseDict['rows']
        if CommonUtil.findDictInDictlist(rewardDict,listDict) is True:
            Log.LogOutput(LogLevel.ERROR, "检查删除失败")
            return True
        else:
            Log.LogOutput(LogLevel.INFO, "检查删除成功")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '检查失败')
            return False
def deleteAllReward():#全部删除
    try:
        rewardDict = copy.deepcopy(YiJiangDaiBuPara.findDelete)
        rewardDict['searchVo.orgId']= orgInit['DftWangGeOrgId']
        response = pinganjianshe_get(url='/rewardToSubsidies/rewardToSubsidiesStep/findRewardToSubsidiesStepForPage.action', param=rewardDict)
        responseDict = json.loads(response.text)
        if responseDict['records'] == 0:
            Log.LogOutput(LogLevel.DEBUG, '无待处理状态记录')
        else:
            for dictListItem in responseDict['rows']:
                if dictListItem['status'] == 1:
                    deleteDict = copy.deepcopy(YiJiangDaiBuPara.deleteReward)
                    deleteDict['applyIds']=dictListItem['rewardToSubsidieId']
                    DeleteReward(deleteDict)
                else :
                    Log.LogOutput(LogLevel.DEBUG, '无待处理状态记录')

    except Exception:
        Log.LogOutput(LogLevel.ERROR, '删除待处理数据失败')
        return False     
    return True  
       
def findByStatus(rewardDict, username = None, password = None):
        getListDict = copy.deepcopy(YiJiangDaiBuPara.findSearchReward)
        getListDict['searchVo.orgId']= orgInit['DftWangGeOrgId']
        getListDict['searchVo.status']= 1
        response = pinganjianshe_get(url='/rewardToSubsidies/rewardToSubsidiesStep/findRewardToSubsidiesStepForPage.action',param=getListDict, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取的数据集合
        record = responseDict['records']
        if record == 0 :
            Log.LogOutput(level=LogLevel.DEBUG, message='筛选数据失败')
            return False
        else:
                Log.LogOutput(level=LogLevel.DEBUG, message='筛选数据成功') 
                return True
def CheckFindByStatus(rewardDict, username = None, password = None):
        getListDict = copy.deepcopy(YiJiangDaiBuPara.findSearchReward)
        getListDict['searchVo.orgId']= orgInit['DftWangGeOrgId']
        getListDict['searchVo.status']= 1
        response = pinganjianshe_get(url='/rewardToSubsidies/rewardToSubsidiesStep/findRewardToSubsidiesStepForPage.action',param=getListDict, username=username, password=password)
        responseDict = json.loads(response.text)
        listDict=responseDict['rows']
        #获取的数据集合
        record = responseDict['records']
        if CommonUtil.findDictInDictlist(rewardDict,listDict) is True:
            Log.LogOutput(LogLevel.ERROR, "检查筛选成功")
            return True
        else:
            Log.LogOutput(LogLevel.INFO, "检查筛选失败")
            return False
#         if record == 0 :
#             Log.LogOutput(level=LogLevel.DEBUG, message='筛选数据失败')
#             return False
#         else:
#                 Log.LogOutput(level=LogLevel.DEBUG, message='筛选数据成功') 
#                 return True

def checkCountReward(rewardDict,orgId=None,username = None, password = None):#
    try:
        Log.LogOutput(LogLevel.INFO, "开始统计")
        getRewardDict = copy.deepcopy(YiJiangDaiBuPara.findCountReward)
        getRewardDict['orgId']=orgInit['DftWangGeOrgId']
        getRewardDict['beginDate']='2015-12-01'
        getRewardDict['endDate']=Time.getCurrentDate()
        getRewardDict['applyOrApprover']=1
        response = pinganjianshe_get(url='/rewardToSubsidies/reportStatistical/reportStatistical.action', param=getRewardDict,username=username, password= password)
        responseDict = json.loads(response.text)
        listDict=responseDict['rows']
        if CommonUtil.findDictInDictlist(rewardDict,listDict) is True:
            Log.LogOutput(LogLevel.ERROR, "检查统计成功")
            return True
        else:
            Log.LogOutput(LogLevel.INFO, "检查统计失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '检查失败')
            return False
        
def AdvancedSearch(rewardDict, username = None, password = None):
        getListDict = copy.deepcopy(YiJiangDaiBuPara.AdvancedSearch)
        getListDict['searchIssueVo.currentOrgId']= orgInit['DftWangGeOrgId']
        getListDict['searchIssueVo.name']=rewardDict['searchIssueVo.name']
        response = pinganjianshe_get(url='/rewardtosubsidies/RewardToSubsidiesManager/findIssueByConditions.action',param=getListDict, username=username, password=password)
        
        responseDict = json.loads(response.text)
        #获取的数据集合
        record = responseDict['records']
        if record == 0 :
            Log.LogOutput(level=LogLevel.DEBUG, message='高级搜索失败')
            return False
        else:
                Log.LogOutput(level=LogLevel.DEBUG, message='高级搜索成功') 
                return True
def checkAdvancedSearch(rewardDict, username = None, password = None):#检查高级搜索是否
        getListDict = copy.deepcopy(YiJiangDaiBuPara.AdvancedSearch)
        getListDict['searchIssueVo.currentOrgId']= orgInit['DftWangGeOrgId']
        getListDict['searchIssueVo.name']=rewardDict['searchIssueVo.name']
        response = pinganjianshe_get(url='/rewardtosubsidies/RewardToSubsidiesManager/findIssueByConditions.action',param=getListDict, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取的数据集合
        record = responseDict['records']
        if record == 0 :
            Log.LogOutput(level=LogLevel.DEBUG, message='检查高级搜索成功')
            return True
        else:
            Log.LogOutput(level=LogLevel.DEBUG, message='检查高级搜索失败') 
            return False
def addIssue(issueDict, username = userInit['DftJieDaoUser'], password = '11111111'):
    Log.LogOutput(level=LogLevel.INFO, message='新增事件')
    response = pinganjianshe_post(url='/issues/issueManage/addIssue.action', postdata=issueDict, username=username, password=password)
    responseDict = json.loads(response.text)
    return responseDict

def checkIssue(checkIssueDict,username=None, password=None):
    issueListPara = copy.deepcopy(YiJiangDaiBuPara.issueListPara)
    issueListPara['organization.id'] = CommonIntf.getOrgInfoByAccount(username)['orgId']
    response = pinganjianshe_get(url='/issues/issueNewManage/findMyAllIssues.action', param=issueListPara, username=username, password=password)   
    responseDict = json.loads(response.text)
    listDict = responseDict['rows']
    if CommonUtil.findDictInDictlist(checkIssueDict, listDict) is True:
        Log.LogOutput(message='查找事件成功')
        return True
    else:
        Log.LogOutput(message="查找事件失败")
        return False