# -*- coding:UTF-8 -*-
'''
Created on 2016-3-21

@author: chenyan
'''
from __future__ import unicode_literals
from Interface.PingAnJianShe.pingAnJianSheHttpCommon import pinganjianshe_post,\
pinganjianshe_get
import json
import copy
from COMMON import Log, CommonUtil
from CONFIG.Define import LogLevel
from CONFIG.InitDefaultPara import orgInit,userInit
from Interface.PingAnJianShe.Common import CommonIntf
from Interface.PingAnJianShe.XunJian import XunJianPara
    




'''
    @隐患项备注设置
    @功能： 新增测试自动化街道下的隐患项信息
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
'''    
def add_riskRemark(riskRemarkDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增隐患项信息开始..")        
    response = pinganjianshe_post(url='/inspection/riskRemarkManage/addRiskRemark.action', postdata=riskRemarkDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增隐患项信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增隐患项信息失败")
    return response

'''
    @隐患项备注设置
    @功能： 修改测试自动化街道下的隐患项信息
    @para: 
    @return: 如果修改成功，则返回True；否则返回False  
'''    
def edit_riskRemark(riskRemarkDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "修改隐患项信息开始..")        
    response = pinganjianshe_post(url='/inspection/riskRemarkManage/updateRiskRemark.action', postdata=riskRemarkDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "修改隐患项信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "修改隐患项信息失败")
    return response

'''
    @隐患项备注设置
    @功能： 删除测试自动化街道下的隐患项信息
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
'''    
def delete_riskRemark(riskRemarkDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "删除隐患项信息开始..")        
    response = pinganjianshe_get(url='/inspection/riskRemarkManage/deleteRiskRemark.action', param=riskRemarkDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除隐患项信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "删除隐患项信息失败")
    return response

'''  
    @功能：  检查测试自动化街道下的隐患项信息
    @para:  
    @return: 如果检查成功，则返回True；否则返回False  
'''
def check_riskRemark(riskRemarkDict, orgId = None, riskmarkerType = None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查隐患项信息开始..")
    try:
        compDict = copy.deepcopy(XunJianPara.getRiskRemarkData)
        compDict['riskRemark.orgId.id']= orgId
        compDict['riskRemark.riskmarkerType']= riskmarkerType
        response = pinganjianshe_get(url='/inspection/riskRemarkManage/findRiskRemark.action', param=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(riskRemarkDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到隐患项信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到隐患项信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查隐患项信息失败")
        return False
    
'''  
    @功能：  搜索测试自动化街道下的隐患项信息
    @para:  
    @return: 如果搜索成功，则返回True；否则返回False  
'''
def search_riskRemark(riskRemarkDict, orgId = None, riskmarkerType = None, riskRemarkName = None,username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "搜索隐患项信息开始..")
    try:
        compDict = copy.deepcopy(XunJianPara.getRiskRemarkData)
        compDict['riskRemark.orgId.id']= orgId
        compDict['riskRemark.riskmarkerType']= riskmarkerType
        compDict['riskRemark.riskRemarkName']= riskRemarkName
        response = pinganjianshe_get(url='/inspection/riskRemarkManage/findRiskRemark.action', param=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(riskRemarkDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到隐患项信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到隐患项信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查隐患项信息失败")
        return False

'''
    @隐患项备注设置
    @功能：选择一条测试自动化街道下的隐患项信息上移/下移/置顶
    @para: 
    @return: 如果上移成功，则返回True；否则返回False  
'''    
def move_riskRemark(riskRemarkDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "上移/下移/置顶隐患项信息开始..")        
    response = pinganjianshe_post(url='/inspection/riskRemarkManage/moveRiskRemarker.action', postdata=riskRemarkDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "上移/下移/置顶隐患项信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "上移/下移/置顶隐患项信息失败")
    return response
    


'''
    @企业 > 企业信息
    @功能： 新增测试自动化网格下的企业信息
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
'''    
def add_enterprise(enterpriseDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增企业信息开始..")        
    response = pinganjianshe_post(url='/baseinfo/safeProductionEnterpriseManage/addSafeProductionEnterprise.action', postdata=enterpriseDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增企业信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增企业信息失败")
    return response


'''
    @企业 > 企业信息
    @功能： 添加测试自动化网格下的巡检记录信息
    @para: 
    @return: 如果添加成功，则返回True；否则返回False  
'''    
def add_InspectionRecord(inspectionDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "添加巡检记录开始..")        
    response = pinganjianshe_post(url='/inspection/inspectionRecord/addInspection.action', postdata=inspectionDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "添加巡检记录成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "添加巡检记录失败")
    return response


'''  
    @功能：  检查测试自动化网格下企业中的企业信息
    @para:  
    @return: 如果检查成功，则返回True；否则返回False  
'''
def check_enterprise(enterpriseDict, orgId = None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查企业信息开始..")
    try:
        compDict = copy.deepcopy(XunJianPara.getEnterpriseData)
        compDict['orgId']= orgId
        response = pinganjianshe_get(url='/baseinfo/safeProductionEnterpriseManage/findSafeProductionEnterpriseForListPage.action', param=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(enterpriseDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到企业信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到企业信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查企业信息失败")
        return False
    
'''  
    @功能：  检查测试自动化网格下的巡检工作中的巡检记录信息
    @para:  
    @return: 如果检查成功，则返回True；否则返回False  
'''
def check_InspectionRecord(inspectionDict, orgId = None,recordType=None,mode=None, name=None,state=None,inspectName=None,sourceType=None,username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查巡检工作中的巡检记录信息开始..")
    try:
        compDict = copy.deepcopy(XunJianPara.getInspectionData)
        compDict['inspectionRecordVo.orgId']= orgId
        compDict['inspectionRecordVo.recordType']= recordType
        compDict['mode']= mode
        compDict['inspectionRecordVo.name']= name
        compDict['inspectionRecordVo.state']= state
        compDict['inspectionRecordVo.inspectName']=inspectName
        compDict['inspectionRecordVo.sourceType']=sourceType
        response = pinganjianshe_get(url='/inspection/inspectionRecord/findInspectionRecordForListPage.action', param=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)       
        if CommonUtil.findDictInDictlist(inspectionDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到巡检记录信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到巡检记录信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查巡检记录信息失败")
        return False

'''  
    @功能： 导入测试自动化网格下的信息
    @para: 
    @return: 如果导入成功，则返回True；否则返回False  
'''
def import_Data(data, files=None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导入信息开始..")
    response = pinganjianshe_post(url='/dataTransfer/importToDomain.action', postdata=data, files=files, username=username, password = password)   
    return response

'''  
    @功能： 导出测试自动化网格下的企业信息
    @para: 
    @return: 如果导出成功，则返回True；否则返回False  
'''    
def downLoad_QiYe(dldata, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导出企业开始..")
    response = pinganjianshe_post(url='/baseinfo/searchSafeProductionEnterprise/downloadSafeProductionEnterprise.action', postdata=dldata, username=username, password = password)   
    return response

'''
    @企业 > 企业信息
    @功能： 划分测试自动化网格下的企业信息
    @para: 
    @return: 如果划分成功，则返回True；否则返回False  
'''    
def dispatchEnterpriseDivision(inspectionDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "划分企业信息开始..")        
    response = pinganjianshe_get(url='/baseinfo/safeProductionEnterpriseManage/enterpriseDivision.action', param=inspectionDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "划分企业信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "划分企业信息失败")
    return response

'''  
    @功能：  搜索测试自动化网格下企业中的企业信息
    @para:  
    @return: 如果搜索成功，则返回True；否则返回False  
'''
def search_enterprise(enterpriseDict, orgId =None, fastSearchKeyWords = None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "搜索企业信息开始..")
    try:
        compDict = copy.deepcopy(XunJianPara.searchEnterpriseData)
        compDict['orgId']= orgId
        compDict['enterpriseSearchCondition.fastSearchKeyWords']= fastSearchKeyWords
        response = pinganjianshe_get(url='/baseinfo/searchSafeProductionEnterprise/fastSearch.action', param=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(enterpriseDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "搜索到企业信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未搜索到企业信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "搜索企业信息失败")
        return False
    
'''  
    @功能：  高级搜索测试自动化网格下企业中的企业信息
    @para:  
    @return: 如果高级搜索成功，则返回True；否则返回False  
'''
def advancedSearch_enterprise(enterpriseDict, orgId =None, name = None, isEmphasis=None,username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "高级搜索企业信息开始..")
    try:
        compDict = copy.deepcopy(XunJianPara.advancedSearchEnterpriseData)
        compDict['orgId']= orgId
        compDict['enterpriseSearchCondition.name']= name
        compDict['enterpriseSearchCondition.isEmphasis']= isEmphasis
        response = pinganjianshe_get(url='/baseinfo/searchSafeProductionEnterprise/searchSafeProductionEnterprise.action', param=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(enterpriseDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "高级搜索到企业信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未搜索到企业信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "高级搜索企业信息失败")
        return False
    
'''
    @企业 > 企业信息
    @功能： 修改测试自动化网格下的企业信息
    @para: 
    @return: 如果修改成功，则返回True；否则返回False  
'''    
def edit_enterprise(enterpriseDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "修改企业信息开始..")        
    response = pinganjianshe_post(url='/baseinfo/safeProductionEnterpriseManage/updateSafeProductionEnterprise.action', postdata=enterpriseDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "修改企业信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "修改企业信息失败")
    return response

'''
    @企业 > 企业信息
    @功能： 删除测试自动化网格下的企业信息
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
'''    
def delete_enterprise(enterpriseDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "删除企业信息开始..")        
    response = pinganjianshe_get(url='/baseinfo/safeProductionEnterpriseManage/deleteSafeProductionEnterprise.action', param=enterpriseDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除企业信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "删除企业信息失败")
    return response


'''  
    @功能：  搜索测试自动化网格下巡检工作中的巡检记录信息
    @para:  
    @return: 如果搜索成功，则返回True；否则返回False  
'''
def search_inspection(inspectionDict, orgId =None, fastSearchKeyWords = None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "搜索巡检记录信息开始..")
    try:
        compDict = copy.deepcopy(XunJianPara.searchEnterpriseData)
        compDict['orgId']= orgId
        compDict['enterpriseSearchCondition.fastSearchKeyWords']= fastSearchKeyWords
        response = pinganjianshe_get(url='/baseinfo/searchSafeProductionEnterprise/fastSearch.action', param=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(inspectionDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "搜索到巡检记录信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未搜索到巡检记录信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "搜索巡检记录信息失败")
        return False

    
'''  
    @功能：  高级搜索测试自动化网格下企业中的企业信息
    @para:  
    @return: 如果高级搜索成功，则返回True；否则返回False  
'''
def advancedSearch_inspection(inspectionDict, orgId =None, name = None, isEmphasis=None,username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "高级搜索巡检记录信息开始..")
    try:
        compDict = copy.deepcopy(XunJianPara.advancedSearchEnterpriseData)
        compDict['orgId']= orgId
        compDict['enterpriseSearchCondition.name']= name
        compDict['enterpriseSearchCondition.isEmphasis']= isEmphasis
        response = pinganjianshe_get(url='/baseinfo/searchSafeProductionEnterprise/searchSafeProductionEnterprise.action', param=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(inspectionDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "高级搜索到巡检记录信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未搜索到巡检记录信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "高级搜索巡检记录信息失败")
        return False
    

'''  
    @功能： 导出测试自动化网格下的企业巡检记录信息
    @para: 
    @return: 如果导出成功，则返回True；否则返回False  
'''    
def downLoad_XunJian(dldata, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导出企业巡检记录信息开始..")
    response = pinganjianshe_post(url='/inspection/inspectionRecord/downloadInspectionRecord.action', postdata=dldata, username=username, password = password)   
    return response

'''
    @企业 > 企业信息
    @功能： 复查测试自动化网格下企业不合格的巡检记录
    @para: 
    @return: 如果复查成功，则返回True；否则返回False  
'''    
def review_inspection(inspectionDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "复查企业不合格巡检记录信息开始..")        
    response = pinganjianshe_post(url='/inspection/inspectionRecord/reviewInspection.action', postdata=inspectionDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "复查企业不合格巡检记录信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "复查企业不合格巡检记录信息失败")
    return response


'''
    @受理中心
    @功能： 将测试自动化网格下受理中心中的巡检记录转事件
    @para: 
    @return: 如果复查成功，则返回True；否则返回False  
'''    
def turnIssueAcceptCenter(issueDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "巡检记录转事件开始..")        
    response = pinganjianshe_post(url='/issues/issueManage/turnIssueAcceptCenter.action', postdata=issueDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "巡检记录转事件成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "巡检记录转事件失败")
    return response

'''
    @事件处理
    @功能： 将测试自动化网格下事件处理中的巡检记录转事件办理结案
    @para: 
    @return: 如果结案成功，则返回True；否则返回False  
'''    
def deal_Issue(issueDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "办理巡检记录转事件结案开始..")        
    response = pinganjianshe_get(url='/issues/issueManage/dealIssue.action', param=issueDict,username=username,password=password)
    return response
#     if response.result is True:
#         Log.LogOutput(LogLevel.INFO, "巡检记录转事件结案成功")
#     else:
#         Log.LogOutput(LogLevel.ERROR, "巡检记录转事件结案失败")
#     return response

'''  
    @功能：  检查测试自动化网格下事件处理列表是否有事件记录
    @para:  
    @return: 如果检查成功，则返回True；否则返回False  
'''
def check_issues(issuesDict, orgId = None,searchYear=None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查事件列表下转事件是否成功开始..")
    try:
        compDict = copy.deepcopy(XunJianPara.issueListPara)
        compDict['organization.id']= orgId
        compDict['searchYear']= searchYear
        response = pinganjianshe_get(url='/issues/issueNewManage/findMyAllIssues.action', param=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)       
        if CommonUtil.findDictInDictlist(issuesDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到转事件后的事件信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到转事件信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查转事件信息失败")
        return False
    
'''
    @受理中心
    @功能： 删除测试自动化网格下已办结的企业信息
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
'''    
def delete_AcceptCenter(supervisionDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "删除已办结的企业信息开始..")        
    response = pinganjianshe_post(url='/inspection/acceptCenter/deleteInspectionRecordById.action', postdata=supervisionDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除已办结的企业信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "删除已办结的企业信息失败")
    return response    



'''
    @受理中心
    @功能： 高级搜索测试自动化网格下受理中心中的巡检记录信息
    @para: 
    @return: 如果搜索成功，则返回True；否则返回False  
'''    
# def search_AcceptCenter(inspectionDict, username = None, password = None):
#     Log.LogOutput(LogLevel.INFO, "高级搜索受理中心中的巡检记录信息开始..")        
#     response = pinganjianshe_get(url='/inspection/inspectionRecord/findInspectionRecordForListPage.action', param=inspectionDict, username=username, password=password)
#     if response.result is True:
#         Log.LogOutput(LogLevel.INFO, "搜索到受理中心中的巡检记录信息")
#     else:
#         Log.LogOutput(LogLevel.ERROR, "未搜索到受理中心中的巡检记录信息")
#     return response

def search_AcceptCenter(inspectionDict, orgId = None,mode=None, name=None,inspectAddress=None,username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查巡检工作中的巡检记录信息开始..")
    try:
        compDict = copy.deepcopy(XunJianPara.serachInspectionData)
        compDict['inspectionRecordVo.orgId']= orgId
        compDict['mode']= mode
        compDict['inspectionRecordVo.name']= name
        compDict['inspectionRecordVo.inspectAddress']= inspectAddress
        response = pinganjianshe_get(url='/inspection/inspectionRecord/findInspectionRecordForListPage.action', param=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)       
        if CommonUtil.findDictInDictlist(inspectionDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到巡检记录信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到巡检记录信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查巡检记录信息失败")
        return False



'''
    @督查暗访
    @功能： 新增测试自动化街道下的督查暗访信息时判断是否有单位信息
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
'''    
def supervision(supervisionDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增督查暗访记录时单位信息。。开始..")        
    response = pinganjianshe_post(url='/baseinfo/safeProductionEnterpriseManage/getSafeProductionEnterpriseByName.action', postdata=supervisionDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增督查暗访信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增督查暗访信息失败")
    return response

'''
    @督查暗访
    @功能： 新增测试自动化街道下的督查暗访信息
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
'''    
def add_supervision(supervisionDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增督查暗访信息开始..")        
    response = pinganjianshe_post(url='/inspection/secretSupervision/addSecretSupervision.action', postdata=supervisionDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增督查暗访信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增督查暗访信息失败")
    return response

'''
    @督查暗访
    @功能： 删除测试自动化街道下已办结的督查暗访信息
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
'''    
def delete_supervision(supervisionDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "删除已办结的督查暗访信息开始..")        
    response = pinganjianshe_post(url='/inspection/secretSupervision/deleteSecretSupervision.action', postdata=supervisionDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除已办结的督查暗访信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "删除已办结的督查暗访信息失败")
    return response


'''  
    @功能：  检查测试自动化街道下的督查暗访记录信息
    @para:  
    @return: 如果检查成功，则返回True；否则返回False  
'''
def check_Supervision(supervisionDict, orgId = None,checkCompanyName=None, checkAddress=None,state=None,username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查督查暗访记录信息开始..")
    try:
        compDict = copy.deepcopy(XunJianPara.getSupervisionData)
        compDict['secretSupervisionVo.orgId']= orgId
        compDict['secretSupervisionVo.checkCompanyName']= checkCompanyName
        compDict['secretSupervisionVo.checkAddress']= checkAddress
        #compDict['secretSupervisionVo.state']= state
        response = pinganjianshe_get(url='/inspection/secretSupervision/findSecretSupervisionForListPage.action', param=compDict,username=username, password = password)  
        responseDict = json.loads(response.text) 
        if CommonUtil.findDictInDictlist(supervisionDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到督查暗访记录信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到督查暗访记录信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查督查暗访记录信息失败")
        return False
 
    
    
'''
    @出租房
    @功能： 新增测试自动化网格下的出租房信息
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
'''    
def add_rental(rentalDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增出租房信息开始..")   
    response = pinganjianshe_post(url='/baseinfo/rentalManage/addRental.action', postdata=rentalDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增出租房信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增出租房信息失败")
    return response

'''
    @出租房
    @功能： 修改测试自动化网格下的出租房信息
    @para: 
    @return: 如果修改成功，则返回True；否则返回False  
'''    
def edit_rental(rentalDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "修改出租房信息开始..")        
    response = pinganjianshe_post(url='/baseinfo/rentalManage/updateRental.action', postdata=rentalDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "修改出租房信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "修改出租房信息失败")
    return response

'''
    @出租房
    @功能： 删除测试自动化网格下的出租房信息
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
'''    
def delete_rental(rentalDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "删除出租房信息开始..")        
    response = pinganjianshe_get(url='/baseinfo/rentalManage/deleteRental.action', param=rentalDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除出租房信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "删除出租房信息失败")
    return response

'''  
    @功能：  检查测试自动化网格下出租房中的出租房信息
    @para:  
    @return: 如果检查成功，则返回True；否则返回False  
'''
def check_rental(rentalDict, orgId = None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查出租房信息开始..")
    try:
        compDict = copy.deepcopy(XunJianPara.getEnterpriseData)
        compDict['orgId']= orgId
        response = pinganjianshe_get(url='/baseinfo/rentalManage/findRentalForListPage.action', param=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(rentalDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到出租房信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到出租房信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查出租房信息失败")
        return False
    
'''  
    @功能：  搜索测试自动化网格下出租房中的出租房信息
    @para:  
    @return: 如果搜索成功，则返回True；否则返回False  
'''
def fastSearch_rental(orgId =None, fastSearchKeyWords = None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "搜索出租房信息开始..")
    compDict = copy.deepcopy(XunJianPara.fastSearchRentalData)
    compDict['orgId']= orgId
    compDict['rentalVo.fastSearchKeyWords']= fastSearchKeyWords
    response = pinganjianshe_get(url='/baseinfo/rentalManage/fastSearch.action', param=compDict,username=username, password = password)  
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "搜索出租房信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "搜索出租房信息失败")
    return response
    
'''  
    @功能：  高级搜索测试自动化网格下出租房中的出租房信息
    @para:  
    @return: 如果高级搜索成功，则返回True；否则返回False  
'''
def search_rental(orgId =None, name = None, isStop = None,username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "高级搜索出租房信息开始..")
    compDict = copy.deepcopy(XunJianPara.searchRentalData)
    compDict['orgId']= orgId
    compDict['rentalVo.name']= name
    compDict['rentalVo.isStop']= isStop
    response = pinganjianshe_get(url='/baseinfo/rentalManage/searchRental.action', param=compDict,username=username, password = password)  
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "高级搜索出租房信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "高级搜索出租房信息失败")
    return response

'''
    @出租房
    @功能： 划分测试自动化网格下的出租房信息
    @para: 
    @return: 如果划分成功，则返回True；否则返回False  
'''    
def dispatchRentalDivision(rentalDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "划分出租房信息开始..")        
    response = pinganjianshe_get(url='/baseinfo/rentalManage/rentalDivision.action', param=rentalDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "划分出租房信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "划分出租房信息失败")
    return response

'''  
    @功能： 导出测试自动化网格下的出租房信息
    @para: 
    @return: 如果导出成功，则返回True；否则返回False  
'''    
def downLoad_Rental(dldata, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导出出租房开始..")
    response = pinganjianshe_post(url='/baseinfo/rentalManage/downloadRental.action', postdata=dldata, username=username, password = password)   
    return response

'''
    @出租房
    @功能： 添加测试自动化网格下出租房的巡检记录信息
    @para: 
    @return: 如果添加成功，则返回True；否则返回False  
'''    
def add_InspectionRentalRecord(rentalDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "添加出租房巡检记录开始..")        
    response = pinganjianshe_post(url='/inspection/inspectionRecordForRental/addInspection.action', postdata=rentalDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "添加出租房巡检记录成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "添加出租房巡检记录失败")
    return response

'''  
    @功能：  检查测试自动化网格下出租房巡检工作中的巡检记录信息
    @para:  
    @return: 如果检查成功，则返回True；否则返回False  
'''
def check_RentalRecord(rentalDict, orgId = None,sourceType=None,recordType=None,mode=None, name=None,state=None,username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查出租房巡检工作中的巡检记录信息开始..")
    try:
        compDict = copy.deepcopy(XunJianPara.getRentalData)
        compDict['inspectionRecordVo.orgId']= orgId
        compDict['inspectionRecordVo.sourceType']= sourceType   #？
        compDict['inspectionRecordVo.recordType']= recordType
        compDict['mode']= mode
        compDict['inspectionRecordVo.name']= name
        compDict['inspectionRecordVo.state']= state
#         compDict['inspectionRecordVo.inspe ctName']=inspectName
        response = pinganjianshe_get(url='/inspection/inspectionRecordForRental/findInspectionRecordForListPage.action', param=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)       
        if CommonUtil.findDictInDictlist(rentalDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到巡检记录信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到巡检记录信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查巡检记录信息失败")
        return False
    
'''
    @出租房
    @功能： 复查测试自动化网格下出租房不合格的巡检记录
    @para: 
    @return: 如果复查成功，则返回True；否则返回False  
'''    
def review_RentalRecord(rentalDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "复查出租房不合格巡检记录信息开始..")        
    response = pinganjianshe_post(url='/inspection/inspectionRecordForRental/reviewInspection.action', postdata=rentalDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "复查出租房不合格巡检记录信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "复查出租房不合格巡检记录信息失败")
    return response

    




def deleteAllXunJian():
    try:
        #删除企业信息
        if CommonIntf.getDbQueryResult(dbCommand="select count(*) from SafeProductionEnterprise ") != 0:    
            compDict = copy.deepcopy(XunJianPara.getEnterpriseData)
            compDict['orgId']= orgInit['DftWangGeOrgId']
            response = pinganjianshe_get(url='/baseinfo/safeProductionEnterpriseManage/findSafeProductionEnterpriseForListPage.action', param=compDict)  
            responseDict = json.loads(response.text)
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无企业信息')
            else:
                for dictListItem in responseDict['rows']:
                    deleteDict = {'selectIds':dictListItem['id']}
                    delete_enterprise(deleteDict)
                    
        #删除出租房信息
        if CommonIntf.getDbQueryResult(dbCommand="select count(*) from rental ") != 0:    
            compDict = copy.deepcopy(XunJianPara.getEnterpriseData)
            compDict['orgId']= orgInit['DftWangGeOrgId']
            response = pinganjianshe_get(url='/baseinfo/rentalManage/findRentalForListPage.action', param=compDict)  
            responseDict = json.loads(response.text)
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无出租房信息')
            else:
                for dictListItem in responseDict['rows']:
                    deleteDict = {'selectIds':dictListItem['id']}
                    delete_rental(deleteDict)

        
        #删除企业隐患备注项信息
#         if CommonIntf.getDbQueryResult(dbCommand="select count(*) from HOUSEHOLDSTAFFS t where t.orgid='%s'" % orgInit['DftWangGeOrgId']) != 0:   #？
            compDict = copy.deepcopy(XunJianPara.getRiskRemarkData)
            compDict['riskRemark.orgId.id']= orgInit['DftJieDaoOrgId']
            compDict['riskRemark.riskmarkerType']= '0'     #企业-0  出租房-1
            response = pinganjianshe_get(url='/inspection/riskRemarkManage/findRiskRemark.action', param=compDict,username=userInit['DftJieDaoUser'], password='11111111')  
            responseDict = json.loads(response.text)        
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无隐患项信息')
            else:
                for dictListItem in responseDict['rows']:
                    deleteDict = {'riskRemarkIds':dictListItem['id']}
                    delete_riskRemark(deleteDict)
                    
        #删除出租房隐患备注项信息
#         if CommonIntf.getDbQueryResult(dbCommand="select count(*) from Rental ") != 0:   
            compDict = copy.deepcopy(XunJianPara.getRiskRemarkData)
            compDict['riskRemark.orgId.id']= orgInit['DftJieDaoOrgId']
            compDict['riskRemark.riskmarkerType']= '1'     #企业-0  出租房-1
            response = pinganjianshe_get(url='/inspection/riskRemarkManage/findRiskRemark.action', param=compDict,username=userInit['DftJieDaoUser'], password='11111111')  
            responseDict = json.loads(response.text)        
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无隐患项信息')
            else:
                for dictListItem in responseDict['rows']:
                    deleteDict = {'riskRemarkIds':dictListItem['id']}
                    delete_riskRemark(deleteDict)
                    
  
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '删除失败')
        return False     
    return True        




#出租屋统计
def check_RentalTongj(rentalDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "查询统计--出租屋巡检统计开始..")
    try:
        compDict = copy.deepcopy(XunJianPara.rentalTongJiTiaoJian)
        compDict['staticsVo.orgId'] = orgInit['DftWangGeOrgId']
        response = pinganjianshe_get(url='/inspection/rentalStatics/findRentalStatics.action', param=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)    
        print rentalDict 
        print response.text
        if CommonUtil.findDictInDictlist(rentalDict, responseDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到出租屋巡检统计信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到出租屋巡检统计信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查出租屋巡检统计失败")
        return False            


#出租屋统计导出
def rentalExport (param , username = None ,password = None):
    Log.LogOutput(LogLevel.INFO, "查询统计---出租屋统计导出....")
    response = pinganjianshe_get(url='/inspection/rentalStatics/exportRentalStatics.action',param = param, username=username, password = password)   
    return response


#出租屋统计人员导出
def rentalExportPerson (param , username = None ,password = None):
    Log.LogOutput(LogLevel.INFO, "查询统计---出租屋统计人员导出....")
    response = pinganjianshe_get(url='/inspection/rentalStatics/exportGridPerson.action',param = param, username=username, password = password)   
    return response

#督查暗访统计
def  inspectionTongJi (rentalDict,username = None , password = None):
    Log.LogOutput(LogLevel.INFO, "查询统计-- 督查暗访统计开始..")
    try:
        compDict = copy.deepcopy(XunJianPara.inspectionParam)
        compDict['searchStaticsVo.orgId'] = orgInit['DftJieDaoOrgId']
        response = pinganjianshe_get(url='/inspection/secretSupervisionStatics/findSecretSupervisionStatistical.action', param=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)    
        if CommonUtil.findDictInDictlist(rentalDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到 督查暗访统计信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到 督查暗访统计统计信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查 督查暗访统计统计失败")
        return False     
    
    
    
    
    

