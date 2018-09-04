# -*- coding:UTF-8 -*-
'''
Created on 2015-11-24

@author: N-133
'''
from __future__ import unicode_literals
from Web_Test.Interface.PingAnJianShe.pingAnJianSheHttpCommon import pinganjianshe_get,\
    pinganjianshe_post
from Web_Test.COMMON import Log, CommonUtil
import copy
from Web_Test.CONFIG.InitDefaultPara import orgInit
import json
from Web_Test.Interface.PingAnJianShe.MinQingRiZhi import MinQingRiZhiPara
from Web_Test.CONFIG import InitDefaultPara
pinganjianshe_get
from Web_Test.CONFIG.Define import LogLevel


# 新增工作问题咨询
def addGongZuoWenTi(GongZuoWenTiDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增工作问题咨询开始")
    response = pinganjianshe_post(url='/plugin/sentimentLogManage/addSentimentLog.action', postdata=GongZuoWenTiDict, username=username, password=password)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "新增工作问题咨询成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "新增工作问题咨询失败")
    return response


# 查看工作问题咨询
def checkGongZuoWenTiCompany(companyDict, OrgId=None, username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "查看工作问题咨询开始")
        compDict = copy.deepcopy(MinQingRiZhiPara.getGongZuoWenTi)
        compDict['issueNewZhouShan.orgId']=OrgId
        response = pinganjianshe_post(url='/plugin/sentimentLogManage/findMyUndoSentimentLog.action', postdata=compDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict= responseDict['rows']
        if CommonUtil.findDictInDictlist(companyDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "查看工作问题咨询成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查看工作问题咨询失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查看失败')
            return False  

# 新增工作心得体会
def addGongZuoXinDe(GongZuoXinDeDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增工作心得体会开始")
    response = pinganjianshe_post(url='/plugin/sentimentLogManage/addSentimentLog.action', postdata=GongZuoXinDeDict, username=username, password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "新增工作心得体会成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "新增工作心得体会失败")
    return response

# 查看工作心得体会
def checkGongZuoXinDeCompany(companyDict, OrgId=None, username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "查看工作心得体会开始")
        compDict = copy.deepcopy(MinQingRiZhiPara.getGongZuoXinDe)
        compDict['issueNewZhouShan.orgId']=OrgId
        response = pinganjianshe_post(url='/plugin/sentimentLogManage/findMyDonelist.action', postdata=compDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict= responseDict['rows']
        if CommonUtil.findDictInDictlist(companyDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "查看工作心得体会成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查看工作心得体会失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查看失败')
            return False  

# 新增工作信息记录
def addGongZuoXinXi(GongZuoXinXiDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增工作信息记录开始")
    response = pinganjianshe_post(url='/plugin/sentimentLogManage/addSentimentLog.action', postdata=GongZuoXinXiDict, username=username, password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "新增工作信息记录成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "新增工作信息记录失败")
    return response

# 查看工作信息记录
def checkGongZuoXinXiCompany(companyDict, OrgId=None, username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "查看工作信息记录开始")
        compDict = copy.deepcopy(MinQingRiZhiPara.getGongZuoXinXi)
        compDict['issueNewZhouShan.orgId']=OrgId
        response = pinganjianshe_post(url='/plugin/sentimentLogManage/findMyDonelist.action', postdata=compDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict= responseDict['rows']
        if CommonUtil.findDictInDictlist(companyDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "查看工作信息记录成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查看工作信息记录失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查看失败')
            return False  

# 查看下辖待办
def checkXiaXiaDaiBanCompany(companyDict, OrgId=None, username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "查看下辖待办开始")
        compDict = copy.deepcopy(MinQingRiZhiPara.getXiaXiaDaiBan)
        compDict['issueNewZhouShan.orgId']=OrgId
        response = pinganjianshe_post(url='/plugin/sentimentLogManage/findMyUndoSentimentLog.action', postdata=compDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict= responseDict['rows']
        if CommonUtil.findDictInDictlist(companyDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "查看下辖待办成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查看下辖待办失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查看失败')
            return False  

# 查看下辖已办
def checkXiaXiaYiBanCompany(companyDict, OrgId=None, username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "查看下辖已办开始")
        compDict = copy.deepcopy(MinQingRiZhiPara.getXiaXiaYiBan)
        compDict['issueNewZhouShan.orgId']=OrgId
        response = pinganjianshe_post(url='/plugin/sentimentLogManage/findMyDonelist.action', postdata=compDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict= responseDict['rows']
        if CommonUtil.findDictInDictlist(companyDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "查看下辖已办成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查看下辖已办失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查看失败')
            return False  

# 新增点评
def adddianping(dianpingDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增点评开始")
    response = pinganjianshe_post(url='/plugin/sentimentLogManage/commentSentimentLog.action', postdata=dianpingDict, username=username, password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "新增点评成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "新增点评失败")
    return response

# 查看点评
def checkdianpingCompany(companyDict, OrgId=None,username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "查看点评开始")
        compDict = copy.deepcopy(MinQingRiZhiPara.getdianping)
        compDict['issueNewZhouShan.orgId']=OrgId
        response = pinganjianshe_get(url='/plugin/sentimentLogManage/findMyComment.action', param=compDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict= responseDict['rows']
        if CommonUtil.findDictInDictlist(companyDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "查看点评成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查看点评失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查看失败')
            return False  
        


#    修改待办日志    
def modifyRiZhi(RiZhiObject,username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "修改待办日志开始")
    response = pinganjianshe_post(url='/plugin/sentimentLogManage/updateSentimentLog.action', postdata=RiZhiObject,username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "修改待办日志成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "修改待办日志失败")
    return response

#高级搜索 期望中的[ps:输入列表中存在的数据进行查询]
def chaxundaibanrizhi(issueDict, username = None, password = None):
        getListDict = copy.deepcopy(MinQingRiZhiPara.chaxundaibanrizhi)
        getListDict['issueNewZhouShan.orgId']= InitDefaultPara.orgInit['DftWangGeOrgId']
        getListDict['issueNewZhouShan.subject']= issueDict['issueNew.subject']
        response = pinganjianshe_get(url='/plugin/sentimentLogManage/findMyUndoSentimentLog.action',param=getListDict, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取的数据集合
        record = responseDict['records']
        if record == 0 :
            Log.LogOutput(level=LogLevel.DEBUG, message='待办日志数据搜索失败')
            return False 
        else:
                Log.LogOutput(level=LogLevel.DEBUG, message='待办日志数据搜索成功') 
                return True

#搜索 期望中的[ps:输入列表中不存在的数据进行查询]
def Companychaxundaibanrizhi(issueDict, company,username = None, password = None):
        getListDict = copy.deepcopy(MinQingRiZhiPara.chaxundaibanrizhi)
        getListDict['issueNewZhouShan.orgId']= InitDefaultPara.orgInit['DftWangGeOrgId']
        getListDict['issueNewZhouShan.subject']= issueDict['issueNew.subject']
        getListDictCheck = copy.deepcopy(MinQingRiZhiPara.getchaxundaibanrizhi) 
        getListDictCheck['subject']= company
        response = pinganjianshe_get(url='/plugin/sentimentLogManage/findMyUndoSentimentLog.action',param=getListDict, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取的数据集合
        listDict = responseDict['rows']
        record = responseDict['records']
        if record == 0 :
            Log.LogOutput(level=LogLevel.DEBUG, message='待办日志数据搜索失败')
            return False 
        else:
                if CommonUtil.findDictInDictlist(getListDictCheck,listDict) is True:
                    Log.LogOutput(message = '不存在的数据匹配成功')
                    return True
                else:
                    Log.LogOutput(message = "不存在的数据匹配失败")
                return False
                Log.LogOutput(level=LogLevel.DEBUG, message='待办日志数据搜索成功') 
                return True


#   转移实有单位
def zhuanYi(zhuanYiDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "转移实有单位开始")
    response = pinganjianshe_post(url='/transferManage/transfer.action', postdata=zhuanYiDict, username=username, password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "转移实有单位成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "转移实有单位失败")
    return response


# 导入实有单位
def dataShiYouDanWei(data, files=None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导入实有单位开始")
    response = pinganjianshe_post(url='/dataTransfer/importToDomain.action', postdata=data, files=files, username=username, password = password)   
    return response

# 导出实有单位
def dldataShiYouRenKou(dldata, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导出实有单位开始..")
    response = pinganjianshe_post(url='/baseinfo/searchActualCompany/downloadActualCompany.action', postdata=dldata, username=username, password = password)   
    return response

def deleteAllMinQingRiZi():
    try:
#     删除待办日志
        compDict = copy.deepcopy(MinQingRiZhiPara.getGongZuoWenTi)
        compDict['issueNewZhouShan.orgId']= orgInit['DftWangGeOrgId']
        response = pinganjianshe_get(url='/plugin/sentimentLogManage/findMyUndoSentimentLog.action', param=compDict)
        responseDict = json.loads(response.text)
        if responseDict['records'] == 0:
            Log.LogOutput(LogLevel.DEBUG, '无待办日志')  
        else:
                for dictListItem in responseDict['rows']:
                        deleteDict = {'issueNew.id':dictListItem['issueId']}
                        delGongZuoWenTi(deleteDict)
                        
#     删除已办日志
        compDict = copy.deepcopy(MinQingRiZhiPara.getGongZuoXinDe)
        compDict['issueNewZhouShan.orgId']= orgInit['DftWangGeOrgId']
        response = pinganjianshe_get(url='/plugin/sentimentLogManage/findMyDonelist.action', param=compDict)
        responseDict = json.loads(response.text)
        if responseDict['records'] == 0:
            Log.LogOutput(LogLevel.DEBUG, '无已办日志')  
        else:
                for dictListItem in responseDict['rows']:
                        deleteDict = {'issueNew.id':dictListItem['issueId']}
                        delGongZuoXinDe(deleteDict)                        

                               
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '删除异常')
#             raise RuntimeError('删除民情日志异常')
            return False     


# 删除待办日志
def delGongZuoWenTi(GongZuoWenTiDict, username = None, password = None):  
        Log.LogOutput(LogLevel.INFO, "删除待办日志开始")
        response = pinganjianshe_get(url='/plugin/sentimentLogManage/deleteSentimentLog.action', param=GongZuoWenTiDict,username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "删除待办日志成功")
        else:
            Log.LogOutput(LogLevel.ERROR, "删除待办日志失败")    
            return response 

# 删除已办日志
def delGongZuoXinDe(GongZuoXinDeDict, username = None, password = None):  
        Log.LogOutput(LogLevel.INFO, "删除已办日志开始")
        response = pinganjianshe_get(url='/plugin/sentimentLogManage/deleteSentimentLog.action', param=GongZuoXinDeDict,username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "删除已办日志成功")
        else:
            Log.LogOutput(LogLevel.ERROR, "删除已办日志失败")    
            return response 



# 办理工作问题咨询
def dealGongZuoWenTi(GongZuoWenTiDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "办理工作问题咨询开始")
    response = pinganjianshe_get(url='/issues/issueManage/dispatchDeal.action', param=GongZuoWenTiDict, username=username, password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "办理工作问题咨询成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "办理工作问题咨询失败")
    return response

# 办理状态为结案
def addjiedan(jiedanDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "办理状态为结案开始")
    response = pinganjianshe_post(url='/issues/issueManage/dealIssue.action', postdata=jiedanDict, username=username, password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "办理状态为结案成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "办理状态为结案失败")
    return response

# 查看结案
def checkjieanCompany(companyDict, OrgId=None, username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "查看结案开始")
        compDict = copy.deepcopy(MinQingRiZhiPara.getXiaXiaYiBan)
        compDict['issueNewZhouShan.orgId']=OrgId
        response = pinganjianshe_post(url='/plugin/sentimentLogManage/findMyDonelist.action', postdata=compDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict= responseDict['rows']
        if CommonUtil.findDictInDictlist(companyDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "查看结案成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查看结案失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查看失败')
            return False  

# 办理状态为办理中
def addbanlizhong(banlizhongDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "办理状态为办理中开始")
    response = pinganjianshe_post(url='/issues/issueManage/dealIssue.action', postdata=banlizhongDict, username=username, password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "办理状态为办理中成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "办理状态为办理中失败")
    return response

# 查看办理中
def checkbanlizhongCompany(companyDict, OrgId=None, username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "查看办理中开始")
        compDict = copy.deepcopy(MinQingRiZhiPara.getXiaXiaDaiBan)
        compDict['issueNewZhouShan.orgId']=OrgId
        response = pinganjianshe_post(url='/plugin/sentimentLogManage/findMyUndoSentimentLog.action', postdata=compDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict= responseDict['rows']
        if CommonUtil.findDictInDictlist(companyDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "查看办理中成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查看办理中失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查看失败')
            return False  

# 办理状态为上报
def addshangbao(shangbaoDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "办理状态为上报开始")
    response = pinganjianshe_post(url='/issues/issueManage/dealIssue.action', postdata=shangbaoDict, username=username, password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "办理状态为上报成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "办理状态为上报失败")
    return response

# 查看上报
def checkshangbaoCompany(companyDict, OrgId=None, username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "查看上报开始")
        compDict = copy.deepcopy(MinQingRiZhiPara.getXiaXiaYiBan)
        compDict['issueNewZhouShan.orgId']=OrgId
        response = pinganjianshe_post(url='/plugin/sentimentLogManage/findMyDonelist.action', postdata=compDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict= responseDict['rows']
        if CommonUtil.findDictInDictlist(companyDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "查看上报成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查看上报失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查看失败')
            return False  


# 办理状态为交办
def addjiaoban(jiaobanDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "办理状态为交办开始")
    response = pinganjianshe_post(url='/issues/issueManage/dealIssue.action', postdata=jiaobanDict, username=username, password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "办理状态为交办成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "办理状态为交办失败")
    return response

# 查看交办
def checkjiaobanCompany(companyDict, OrgId=None, username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "查看交办开始")
        compDict = copy.deepcopy(MinQingRiZhiPara.getXiaXiaYiBan)
        compDict['issueNewZhouShan.orgId']=OrgId
        response = pinganjianshe_post(url='/plugin/sentimentLogManage/findMyDonelist.action', postdata=compDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict= responseDict['rows']
        if CommonUtil.findDictInDictlist(companyDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "查看交办成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查看交办失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查看失败')
            return False  
        