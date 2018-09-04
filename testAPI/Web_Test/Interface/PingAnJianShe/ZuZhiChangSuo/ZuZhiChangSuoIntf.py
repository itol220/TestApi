# -*- coding:UTF-8 -*-
'''
Created on 2015-11-24

@author: N-133
'''
from __future__ import unicode_literals
from COMMON import Log, CommonUtil
from CONFIG import InitDefaultPara
from CONFIG.Define import LogLevel
from CONFIG.InitDefaultPara import orgInit
from Interface.PingAnJianShe.Common import CommonIntf
from Interface.PingAnJianShe.ZuZhiChangSuo import ZuZhiChangSuoPara
from Interface.PingAnJianShe.pingAnJianSheHttpCommon import pinganjianshe_post, \
    pinganjianshe_get
import copy
import json
import time

# 新增服务成员
def addFuWuChengYuan(FuWuChengYuanDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增服务成员开始")
    response = pinganjianshe_post(url='/plugin/serviceTeam/serviceTeamMember/addServiceTeamMemberBase.action', postdata=FuWuChengYuanDict, username=username, password=password)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "新增服务成员成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "新增服务成员失败")
    return response

# 查看服务成员是否新增成功
def checkFuWuChengYuanCompany(companyDict, orgId=None, username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "查看服务成员开始")
        compDict = copy.deepcopy(ZuZhiChangSuoPara.getFuWuChengYuan)
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
    
#     新增安全生产重点
def addAnQuanShengChan(AnQuanShengChanDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增安全生产重点开始")
    response = pinganjianshe_post(url='/baseinfo/safetyProductionKeyManage/addEnterprise.action', postdata=AnQuanShengChanDict, username=username, password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "新增安全生产重点成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "新增安全生产重点失败")
    return response

#     修改安全生产重点
def UpdateAnQuanShengChan(AnQuanShengChanDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "修改安全生产重点开始")
    response = pinganjianshe_post(url='/baseinfo/safetyProductionKeyManage/updateEnterprise.action', postdata=AnQuanShengChanDict, username=username, password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "修改安全生产重点成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "修改安全生产重点失败")
    return response


# 查看安全生产重点
def checkAnQuanShengChan(companyDict, orgId=None, username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "查看安全生产重点开始")
        compDict = copy.deepcopy(ZuZhiChangSuoPara.ChaKanAnQuanShengChanbject)
        compDict['orgId']= orgId
        response = pinganjianshe_get(url='/baseinfo/safetyProductionKeyManage/safetyProductionKeyList.action', param=compDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict= responseDict['rows']
        if CommonUtil.findDictInDictlist(companyDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "查找安全生产重点成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查找安全生产重点失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查看失败')
            return False  

    
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
        compDict = copy.deepcopy(ZuZhiChangSuoPara.ChaKanShiYouDanWeiObject)
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

# 新增巡场情况
def addXunChangQingKuang(XunChangQingKuangDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增巡场情况开始")
    response = pinganjianshe_post(url='/plugin/serviceTeam/serviceRecord/addServiceRecord.action', postdata=XunChangQingKuangDict, username=username, password=password)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "新增巡场情况成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "新增巡场情况失败")
    return response

# 查看巡场情况是否新增成功
def checkXunChangQingKuangiCompany(companyDict, OrgId=None, username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "查看记录开始")
        compDict = copy.deepcopy(ZuZhiChangSuoPara.getXunChangQingKuang)
        compDict['serviceRecordVo.displayYear']=time.strftime('%Y')
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

# 新增消防安全重点
def addXiaoFangAnQuan(XiaoFangAnQuanDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增消防安全重点开始")
    response = pinganjianshe_post(url='/baseinfo/fireSafetyEnterpriseManage/addFireSafetyEnterprise.action', postdata=XiaoFangAnQuanDict, username=username, password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "新增消防安全重点成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "新增消防安全重点失败")
    return response

# 修改消防安全重点
def UpdateXiaoFangAnQuan(XiaoFangAnQuanDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "修改消防安全重点开始")
    response = pinganjianshe_post(url='/baseinfo/fireSafetyEnterpriseManage/updateFireSafetyEnterprise.action', postdata=XiaoFangAnQuanDict, username=username, password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "修改消防安全重点成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "修改消防安全重点失败")
    return response

# 查看消防安全重点
def checkXiaoFangAnQuanCompany(companyDict, OrgId=None, username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "查看消防安全重点开始")
        compDict = copy.deepcopy(ZuZhiChangSuoPara.getXiaoFangAnQuan)
        compDict['orgId']= OrgId
        response = pinganjianshe_get(url='/baseinfo/fireSafetyEnterpriseManage/fireSafetyEnterpriseList.action', param=compDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict= responseDict['rows']
        if CommonUtil.findDictInDictlist(companyDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "查找消防安全重点成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查找消防安全重点失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查看失败')
            return False  

# 新增治安重点
def addZhiAnZhongDian(ZhiAnZhongDianDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增治安重点开始")
    response = pinganjianshe_post(url='/baseinfo/safetyProductionKeyManage/addEnterprise.action', postdata=ZhiAnZhongDianDict, username=username, password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "新增治安重点成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "新增治安重点失败")
    return response

# 修改治安重点
def UpdateZhiAnZhongDian(ZhiAnZhongDianDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "修改治安重点开始")
    response = pinganjianshe_post(url='/baseinfo/safetyProductionKeyManage/updateEnterprise.action', postdata=ZhiAnZhongDianDict, username=username, password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "修改治安重点成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "修改治安重点失败")
    return response

# 查看治安重点
def checkZhiAnZhongDianCompany(companyDict, OrgId=None, username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "查看治安重点开始")
        compDict = copy.deepcopy(ZuZhiChangSuoPara.getZhiAnZhongDian)
        compDict['orgId']= OrgId
        response = pinganjianshe_get(url='/baseinfo/safetyProductionKeyManage/safetyProductionKeyList.action', param=compDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict= responseDict['rows']
        if CommonUtil.findDictInDictlist(companyDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "查找治安重点成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查找治安重点失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查看失败')
            return False  

# 新增学校
def addXueXiao(XueXiaoDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增学校开始")
    response = pinganjianshe_post(url='/baseinfo/schoolManage/addSchoolAction.action', postdata=XueXiaoDict, username=username, password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "新增学校成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "新增学校失败")
    return response

# 修改学校
def UpdateXueXiao(XueXiaoDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "修改学校开始")
    response = pinganjianshe_post(url='/baseinfo/schoolManage/updateSchoolAction.action', postdata=XueXiaoDict, username=username, password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "修改学校成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "修改学校失败")
    return response

# 查看学校
def checkXueXiaoCompany(companyDict, OrgId=None, username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "查看学校开始")
        compDict = copy.deepcopy(ZuZhiChangSuoPara.getXueXiao)
        compDict['orgId']= OrgId
        response = pinganjianshe_get(url='/baseinfo/schoolManage/schoolList.action', param=compDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict= responseDict['rows']
        if CommonUtil.findDictInDictlist(companyDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "查找学校成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查找学校失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查看失败')
            return False  

# 新增医院
def addYiYuan(YiYuanDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增医院开始")
    response = pinganjianshe_post(url='/baseinfo/hospitalManage/maintainHosptial.action', postdata=YiYuanDict, username=username, password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "新增医院成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "新增医院失败")
    return response

# 修改医院
def UpdateYiYuan(YiYuanDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "修改医院开始")
    response = pinganjianshe_post(url='/baseinfo/hospitalManage/maintainHosptial.action', postdata=YiYuanDict, username=username, password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "修改医院成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "修改医院失败")
    return response

# 查看医院
def checkYiYuanCompany(companyDict, OrgId=None, username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "查看医院开始")
        compDict = copy.deepcopy(ZuZhiChangSuoPara.getYiYuan)
        compDict['organizationId']= OrgId
        response = pinganjianshe_get(url='/baseinfo/hospitalManage/hospitalList.action', param=compDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict= responseDict['rows']
        if CommonUtil.findDictInDictlist(companyDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "查找医院成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查找医院失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查看失败')
            return False  

# 新增危险化学品单位
def addWeiXianHuaXuePing(WeiXianHuaXuePingDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增危险化学品单位开始")
    response = pinganjianshe_post(url='/baseinfo/dangerousChemicalsUnitManage/addDangerousChemicalsUnit.action', postdata=WeiXianHuaXuePingDict, username=username, password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "新增危险化学品单位成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "新增危险化学品单位失败")
    return response

# 修改危险化学品单位
def UpdateWeiXianHuaXuePing(WeiXianHuaXuePingDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "修改危险化学品单位开始")
    response = pinganjianshe_post(url='/baseinfo/dangerousChemicalsUnitManage/addDangerousChemicalsUnit.action', postdata=WeiXianHuaXuePingDict, username=username, password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "修改危险化学品单位成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "修改危险化学品单位失败")
    return response


# 查看危险化学品单位
def checkWeiXianHuaXuePingCompany(companyDict, OrgId=None, username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "查看危险化学品单位开始")
        compDict = copy.deepcopy(ZuZhiChangSuoPara.getWeiXianHuaXuePing)
        compDict['organizationId']= OrgId
        response = pinganjianshe_get(url='/baseinfo/dangerousChemicalsUnitManage/dangerousChemicalsUnitList.action', param=compDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict= responseDict['rows']
        if CommonUtil.findDictInDictlist(companyDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "查找危险化学品单位成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查找危险化学品单位失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查看失败')
            return False  

# 新增上网服务单位
def addShangWanFuWu(ShangWanFuWuDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增上网服务单位开始")
    response = pinganjianshe_post(url='/baseinfo/internetBarManage/saveInternetBar.action', postdata=ShangWanFuWuDict, username=username, password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "新增上网服务单位成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "新增上网服务单位失败")
    return response

# 修改上网服务单位
def UpdateShangWanFuWu(ShangWanFuWuDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "修改上网服务单位开始")
    response = pinganjianshe_post(url='/baseinfo/internetBarManage/saveInternetBar.action', postdata=ShangWanFuWuDict, username=username, password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "修改上网服务单位成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "修改上网服务单位失败")
    return response

# 查看上网服务单位
def checkShangWanFuWuCompany(companyDict, OrgId=None, username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "查看上网服务单位开始")
        compDict = copy.deepcopy(ZuZhiChangSuoPara.getShangWanFuWu)
        compDict['organizationId']= OrgId
        response = pinganjianshe_get(url='/baseinfo/internetBarManage/internetBarList.action', param=compDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict= responseDict['rows']
        if CommonUtil.findDictInDictlist(companyDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "查找上网服务单位成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查找上网服务单位失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查看失败')
            return False  

# 新增公共场所
def addGongGongChangSuo(GongGongChangSuoDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增公共场所开始")
    response = pinganjianshe_post(url='/baseinfo/publicPlaceManage/maintainPublicPlace.action', postdata=GongGongChangSuoDict, username=username, password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "新增公共场所成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "新增公共场所失败")
    return response

# 修改公共场所
def UpdateShangWanFuWu1(GongGongChangSuoDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "修改公共场所开始")
    response = pinganjianshe_post(url='/baseinfo/publicPlaceManage/maintainPublicPlace.action', postdata=GongGongChangSuoDict, username=username, password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "修改公共场所成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "修改公共场所失败")
    return response


# 查看公共场所
def checkGongGongChangSuoCompany(companyDict, OrgId=None, username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "查看公共场所开始")
        compDict = copy.deepcopy(ZuZhiChangSuoPara.getGongGongChangSuo)
        compDict['organizationId']= OrgId
        response = pinganjianshe_get(url='/baseinfo/publicPlaceManage/publicPlaceList.action', param=compDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict= responseDict['rows']
        if CommonUtil.findDictInDictlist(companyDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "查找公共场所成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查找公共场所失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查看失败')
            return False  

# 新增公共复杂场所
def addGongGongFuZaChangSuo(GongGongFuZaChangSuoDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增公共复杂场所开始")
    response = pinganjianshe_post(url='/baseinfo/commonComplexPlaceManage/maintainCommonComplexPlace.action', postdata=GongGongFuZaChangSuoDict, username=username, password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "新增公共复杂场所成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "新增公共复杂场所失败")
    return response

# 修改公共复杂场所
def UpdateGongGongFuZaChangSuo(GongGongFuZaChangSuoDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "修改公共复杂场所开始")
    response = pinganjianshe_post(url='/baseinfo/commonComplexPlaceManage/maintainCommonComplexPlace.action', postdata=GongGongFuZaChangSuoDict, username=username, password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "修改公共复杂场所成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "修改公共复杂场所失败")
    return response

# 查看公共复杂场所
def checkGongGongFuZaChangSuoCompany(companyDict, OrgId=None, username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "查看公共复杂场所开始")
        compDict = copy.deepcopy(ZuZhiChangSuoPara.getGongGongFuZaChangSuo)
        compDict['organizationId']= OrgId
        response = pinganjianshe_get(url='/baseinfo/commonComplexPlaceManage/commonComplexPlaceList.action', param=compDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict= responseDict['rows']
        if CommonUtil.findDictInDictlist(companyDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "查找公共复杂场所成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查找公共复杂场所失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查看失败')
            return False  

# 新增特种行业
def addTeZhongHangYe(TeZhongHangYeDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增特种行业开始")
    response = pinganjianshe_post(url='/baseinfo/specialTradeManage/maintainSpecialTrade.action', postdata=TeZhongHangYeDict, username=username, password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "新增特种行业成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "新增特种行业失败")
    return response

# 修改特种行业
def updatetezhonghangye(TeZhongHangYeDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "修改特种行业开始")
    response = pinganjianshe_post(url='/baseinfo/specialTradeManage/maintainSpecialTrade.action', postdata=TeZhongHangYeDict, username=username, password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "修改特种行业成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "修改特种行业失败")
    return response

# 查看特种行业
def checkTeZhongHangYeCompany(companyDict, OrgId=None, username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "查看特种行业开始")
        compDict = copy.deepcopy(ZuZhiChangSuoPara.getTeZhongHangYe)
        compDict['organizationId']= OrgId
        response = pinganjianshe_get(url='/baseinfo/specialTradeManage/specialTradeList.action', param=compDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict= responseDict['rows']
        if CommonUtil.findDictInDictlist(companyDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "查找特种行业成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查找特种行业失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查看失败')
            return False  

# 新增其他场所
def addQiTaChangSuo(QiTaChangSuoDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增其他场所开始")
    response = pinganjianshe_post(url='/baseinfo/otherLocaleManage/addOtherLocale.action', postdata=QiTaChangSuoDict, username=username, password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "新增其他场所成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "新增其他场所失败")
    return response

# 修改其他场所
def UpdateQiTaChangSuo(QiTaChangSuoDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "修改其他场所开始")
    response = pinganjianshe_post(url='/baseinfo/otherLocaleManage/updateOtherLocale.action', postdata=QiTaChangSuoDict, username=username, password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "修改其他场所成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "修改其他场所失败")
    return response

# 查看其他场所
def checkQiTaChangSuoCompany(companyDict, OrgId=None, username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "查看其他场所开始")
        compDict = copy.deepcopy(ZuZhiChangSuoPara.getQiTaChangSuo)
        compDict['orgId']= OrgId
        response = pinganjianshe_get(url='/baseinfo/otherLocaleManage/otherLocaleList.action', param=compDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict= responseDict['rows']
        if CommonUtil.findDictInDictlist(companyDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "查找其他场所成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查找其他场所失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查看失败')
            return False  

# 新增社会组织
def addSheHuiZuZhi(SheHuiZuZhiDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增社会组织开始")
    response = pinganjianshe_post(url='/baseinfo/newSocietyOrganizationsManage/addNewSocietyOrganizations.action', postdata=SheHuiZuZhiDict, username=username, password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "新增社会组织成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "新增社会组织失败")
    return response

# 修改社会组织
def updateSheHuiZuZhi(SheHuiZuZhiDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "修改社会组织开始")
    response = pinganjianshe_post(url='/baseinfo/newSocietyOrganizationsManage/updateNewSocietyOrganizations.action', postdata=SheHuiZuZhiDict, username=username, password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "修改社会组织成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "修改社会组织失败")
    return response

# 查看社会组织
def checkSheHuiZuZhiCompany(companyDict, OrgId=None, username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "查看社会组织开始")
        compDict = copy.deepcopy(ZuZhiChangSuoPara.getSheHuiZuZhi)
        compDict['organizationId']= OrgId
        response = pinganjianshe_get(url='/baseinfo/newSocietyOrganizationsManage/newSocietyOrganizationsList.action', param=compDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict= responseDict['rows']
        if CommonUtil.findDictInDictlist(companyDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "查找社会组织成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查找社会组织失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查看失败')
            return False  

# 新增新经济组织
def addXinJingJiZuZhi(XinJingJiZuZhiDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增新经济组织开始")
    response = pinganjianshe_post(url='/baseinfo/newEconomicOrganizationsManage/saveNewEconomicOrganizations.action', postdata=XinJingJiZuZhiDict, username=username, password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "新增新经济组织成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "新增新经济组织失败")
    return response

# 修改新经济组织
def updateXinJingJiZuZhi(XinJingJiZuZhiDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "修改新经济组织开始")
    response = pinganjianshe_post(url='/baseinfo/newEconomicOrganizationsManage/saveNewEconomicOrganizations.action', postdata=XinJingJiZuZhiDict, username=username, password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "修改新经济组织成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "修改新经济组织失败")
    return response

# 查看新经济组织
def checkXinJingJiZuZhiCompany(companyDict, OrgId=None, username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "查看新经济组织开始")
        compDict = copy.deepcopy(ZuZhiChangSuoPara.getXinJingJiZuZhi)
        compDict['organizationId']= OrgId
        response = pinganjianshe_get(url='/baseinfo/newEconomicOrganizationsManage/findNewEconomicOrganizations.action', param=compDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict= responseDict['rows']
        if CommonUtil.findDictInDictlist(companyDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "查找新经济组织成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查找新经济组织失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查看失败')
            return False  

# 新增规上企业
def addGuiShangQiYe(GuiShangQiYeDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增规上企业开始")
    response = pinganjianshe_post(url='/baseinfo/safetyProductionKeyManage/addEnterprise.action', postdata=GuiShangQiYeDict, username=username, password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "新增规上企业成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "新增规上企业失败")
    return response

# 修改规上企业
def updateGuiShangQiYe(GuiShangQiYeDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "修改规上企业开始")
    response = pinganjianshe_post(url='/baseinfo/safetyProductionKeyManage/updateEnterprise.action', postdata=GuiShangQiYeDict, username=username, password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "修改规上企业成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "修改规上企业失败")
    return response

# 查看规上企业
def checkGuiShangQiYeCompany(companyDict, OrgId=None, username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "查看规上企业开始")
        compDict = copy.deepcopy(ZuZhiChangSuoPara.getGuiShangQiYe)
        compDict['orgId']= OrgId
        response = pinganjianshe_get(url='/baseinfo/safetyProductionKeyManage/safetyProductionKeyList.action', param=compDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict= responseDict['rows']
        if CommonUtil.findDictInDictlist(companyDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "查找规上企业成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查找规上企业失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查看失败')
            return False  

# 新增规下企业
def addGuiXiaQiYe(GuiXiaQiYeDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增规下企业开始")
    response = pinganjianshe_post(url='/baseinfo/safetyProductionKeyManage/addEnterprise.action', postdata=GuiXiaQiYeDict, username=username, password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "新增规下企业成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "新增规下企业失败")
    return response

# 修改规下企业
def UpdateGuiXiaQiYe(GuiXiaQiYeDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "修改规下企业开始")
    response = pinganjianshe_post(url='/baseinfo/safetyProductionKeyManage/updateEnterprise.action', postdata=GuiXiaQiYeDict, username=username, password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "修改规下企业成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "修改规下企业失败")
    return response

# 查看规下企业
def checkGuiXiaQiYeCompany(companyDict, OrgId=None, username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "查看规下企业开始")
        compDict = copy.deepcopy(ZuZhiChangSuoPara.getGuiXiaQiYe)
        compDict['orgId']= OrgId
        response = pinganjianshe_get(url='/baseinfo/safetyProductionKeyManage/safetyProductionKeyList.action', param=compDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict= responseDict['rows']
        if CommonUtil.findDictInDictlist(companyDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "查找规下企业成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查找规下企业失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查看失败')
            return False  

# 新增无证无照场所
def addWuZhengWuZhao(WuZhengWuZhaoDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增无证无照场所开始")
    response = pinganjianshe_post(url='/baseinfo/withoutPlaceManage/addWithoutPlace.action', postdata=WuZhengWuZhaoDict, username=username, password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "新增无证无照场所成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "新增无证无照场所失败")
    return response

# 新增安全生产企业
def addAnQuanShengchan(AnQuanShengChanDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增安全生产企业开始")
    response = pinganjianshe_post(url='/baseinfo/safeProductionEnterpriseManage/addSafeProductionEnterprise.action', postdata=AnQuanShengChanDict, username=username, password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "新增安全生产企业成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "新增安全生产企业失败")
    return response

# 修改安全生产企业
def updateAnQuanShengchan(AnQuanShengChanDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "修改安全生产企业开始")
    response = pinganjianshe_post(url='/baseinfo/safeProductionEnterpriseManage/updateSafeProductionEnterprise.action', postdata=AnQuanShengChanDict, username=username, password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "修改安全生产企业成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "修改安全生产企业失败")
    return response

# 修改无证无照场所
def updateWuZhengWuZhao(WuZhengWuZhaoDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "修改无证无照场所开始")
    response = pinganjianshe_post(url='/baseinfo/withoutPlaceManage/updateWithoutPlace.action', postdata=WuZhengWuZhaoDict, username=username, password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "修改无证无照场所成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "修改无证无照场所失败")
    return response

# 查看无证无照场所
def checkWuZhengWuZhaoCompany(companyDict, OrgId=None, username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "查看无证无照场所开始")
        compDict = copy.deepcopy(ZuZhiChangSuoPara.getWuZhengWuZhao)
        compDict['orgId']= OrgId
        response = pinganjianshe_get(url='/baseinfo/withoutPlaceManage/withoutPlaceList.action', param=compDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict= responseDict['rows']
        if CommonUtil.findDictInDictlist(companyDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "查找无证无照场所成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查找无证无照场所失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查看失败')
            return False  
        
# 查看安全生产企业
def checkAnQuanShengChanCompany(companyDict, OrgId=None, username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "查看安全生产企业开始")
        compDict = copy.deepcopy(ZuZhiChangSuoPara.getAnQuanShengChan)
        compDict['orgId']= OrgId
        response = pinganjianshe_get(url='/baseinfo/safeProductionEnterpriseManage/findSafeProductionEnterpriseForListPage.action', param=compDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict= responseDict['rows']
        if CommonUtil.findDictInDictlist(companyDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "查看安全生产企业成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查看安全生产企业失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查看失败')
            return False         
        
# 巡检模块中查看安全生产企业
def checkanQuanShengChanCompany(companyDict, OrgId=None, username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "查看安全生产企业开始")
        compDict = copy.deepcopy(ZuZhiChangSuoPara.getAnQuanShengChan)
        compDict['orgId']= OrgId
        response = pinganjianshe_get(url='/baseinfo/safeProductionEnterpriseManage/findSafeProductionEnterpriseForListPage.action', param=compDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict= responseDict['rows']
        if CommonUtil.findDictInDictlist(companyDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "查看安全生产企业成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查看安全生产企业失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查看失败')
            return False            

# 新增治安管理负责人
def addGuanLiZhiAn(GuanLiZhiAnDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增治安管理负责人开始")
    response = pinganjianshe_post(url='/plugin/serviceTeam/router/routerManage/addObjectAndMemberRelation.action', postdata=GuanLiZhiAnDict, username=username, password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "新增治安管理负责人成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "新增治安管理负责人失败")
    return response


# 查看治安管理负责人
def checkGuanLiZhiAnCompany(companyDict, objectId=None,objectName=None, username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "查看治安管理负责人开始")
        compDict = copy.deepcopy(ZuZhiChangSuoPara.getGuanLiZhiAn)
        compDict['serviceMemberVo.objectId']=objectId
        compDict['serviceMemberVo.objectName']=objectName
        response = pinganjianshe_post(url='/plugin/serviceTeam/router/routerManage/findServiceMembersByServiceMemberVo.action', postdata=compDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict= responseDict['rows']
        if CommonUtil.findDictInDictlist(companyDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "查找治安管理负责人成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查找治安管理负责人失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查看失败')
            return False  


# 修改实有单位    
def modifyShiYouDanWei(modifyObject,username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "修改实有单位开始")
    response = pinganjianshe_post(url='/baseinfo/actualCompanyManage/maintainBaseInfo.action', postdata=modifyObject,username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "修改实有单位成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "修改实有单位失败")
    return response

# 转移实有单位
def zhuanYi(zhuanYiDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "转移实有单位开始")
    response = pinganjianshe_post(url='/transferManage/transfer.action', postdata=zhuanYiDict, username=username, password=password)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "转移实有单位成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "转移实有单位失败")
    return response

# 查看转移实有单位
def checkzhuanYiCompany(companyDict, OrgId=None, username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "查看转移实有单位开始")
        compDict = copy.deepcopy(ZuZhiChangSuoPara.getzhuanYi)
        compDict['organizationId']= OrgId
        response = pinganjianshe_get(url='/baseinfo/actualCompanyManage/actualCompanyList.action', param=compDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict= responseDict['rows']
        if CommonUtil.findDictInDictlist(companyDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "查找转移实有单位成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查找转移实有单位失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查看失败')
            return False  

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

# 导出安全生产重点
def dldataAnQuanShengChan(dldata, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导出安全生产重点开始..")
    response = pinganjianshe_post(url='/baseinfo/searchSafetyProductionKey/downloadEnterprise.action', postdata=dldata,username=username, password = password)   
    return response

# 导出消防安全重点
def dldataXiaoFangAnQuan(dldata, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导出消防安全重点开始..")
    response = pinganjianshe_post(url='/baseinfo/searchSafetyProductionKey/downloadEnterprise.action', postdata=dldata,username=username, password = password)   
    return response

# 导出治安重点
def dldataZhiAnZhongDian(dldata, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导出治安重点开始..")
    response = pinganjianshe_post(url='/baseinfo/searchSafetyProductionKey/downloadEnterprise.action', postdata=dldata,username=username, password = password)   
    return response

# 导出学校
def dldataXueXiao(dldata, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导出学校开始..")
    response = pinganjianshe_post(url='/baseinfo/searchSchool/downloadSchool.action', postdata=dldata,username=username, password = password)   
    return response

# 导出医院
def dldataYiYuan(dldata, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导出医院开始..")
    response = pinganjianshe_post(url='/baseinfo/searchHospital/downloadHospital.action', postdata=dldata,username=username, password = password)   
    return response

# 导出危险化学品单位
def dldataWeiXianHuaXuePing(dldata, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导出危险化学品单位开始..")
    response = pinganjianshe_post(url='/baseinfo/searchDangerousChemicalsUnit/downloadDangerousChemicalsUnit.action', postdata=dldata,username=username, password = password)   
    return response

# 导出上网服务单位
def dldataShangWanFuWu(dldata, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导出上网服务单位开始..")
    response = pinganjianshe_post(url='/baseinfo/searchInternetBar/downloadInternetBar.action', postdata=dldata,username=username, password = password)   
    return response

# 导出公共场所
def dldataGongGongChangSuo(dldata, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导出公共场所开始..")
    response = pinganjianshe_post(url='/baseinfo/searchPublicPlace/downloadPublicPlace.action', postdata=dldata,username=username, password = password)   
    return response

# 导出公共复杂场所
def dldataGongGongFuZaChangSuo(dldata, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导出公共复杂场所开始..")
    response = pinganjianshe_post(url='/baseinfo/searchCommonComplexPlace/downloadCommonComplexPlace.action', postdata=dldata,username=username, password = password)   
    return response

# 导出特种行业
def dldataTeZhongHangYe(dldata, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导出特种行业开始..")
    response = pinganjianshe_post(url='/baseinfo/searchSpecialTrade/downloadSpecialTrade.action', postdata=dldata,username=username, password = password)   
    return response

# 导出其他场所
def dldataQiTaChangSuo(dldata, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导出其他场所开始..")
    response = pinganjianshe_post(url='/baseinfo/searchOtherLocale/downloadOtherLocale.action', postdata=dldata,username=username, password = password)   
    return response

# 导出社会组织
def dldataSheHuiZuZhi(dldata, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导出社会组织开始..")
    response = pinganjianshe_post(url='/baseinfo/searchNewSocietyOrganizations/downloadNewSocietyOrganizations.action', postdata=dldata,username=username, password = password)   
    return response

# 导出新经济组织
def dldataXinJingJiZuZhi(dldata, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导出新经济组织开始..")
    response = pinganjianshe_post(url='/baseinfo/newEconomicOrganizationsManage/downloadNewEconomicOrganizations.action', postdata=dldata,username=username, password = password)   
    return response

# 导出规上企业
def dldataGuiShangQiYe(dldata, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导出规上企业开始..")
    response = pinganjianshe_post(url='/baseinfo/searchSafetyProductionKey/downloadEnterprise.action', postdata=dldata,username=username, password = password)   
    return response

# 导出规下企业
def dldataGuiXiaQiYe(dldata, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导出规下企业开始..")
    response = pinganjianshe_post(url='/baseinfo/searchSafetyProductionKey/downloadEnterprise.action', postdata=dldata,username=username, password = password)   
    return response

# 导出无证无照场所
def dldataWuZhengWuZhao(dldata, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导出规下企业开始..")
    response = pinganjianshe_post(url='/baseinfo/withoutPlaceKey/downloadWithoutPlace.action', postdata=dldata,username=username, password = password)   
    return response

# 导出安全生产企业
def dldataAnQuanShengchan(dldata, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "导出安全生产企业开始..")
    response = pinganjianshe_post(url='/baseinfo/searchSafeProductionEnterprise/downloadSafeProductionEnterprise.action', postdata=dldata,username=username, password = password)   
    return response

def deleteAllPopulation():
    try:
#     删除实有单位
        if CommonIntf.getDbQueryResult(dbCommand='select count(*) from ACTUALCOMPANY') != 0: 
            compDict = copy.deepcopy(ZuZhiChangSuoPara.ChaKanShiYouDanWeiObject)
            compDict['organizationId']= orgInit['DftWangGeOrgId']
            response = pinganjianshe_get(url='/baseinfo/actualCompanyManage/actualCompanyList.action', param=compDict)
            responseDict = json.loads(response.text)
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无实有单位')  
            else:
                for dictListItem in responseDict['rows']:
                        deleteDict = {'locationIds':dictListItem['id']}
                        deleteShiYouDanWei(deleteDict)
 
# 删除安全生产重点 
        if CommonIntf.getDbQueryResult(dbCommand='select count(*) from SAFEPRODUCTIONENTERPRISE') != 0:                       
            compDict = copy.deepcopy(ZuZhiChangSuoPara.ChaKanAnQuanShengChanbject)
            compDict['orgId']= orgInit['DftWangGeOrgId']
            response = pinganjianshe_get(url='/baseinfo/safetyProductionKeyManage/safetyProductionKeyList.action', param=compDict)
            responseDict = json.loads(response.text)
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无安全生产重点')  
            else:
                for dictListItem in responseDict['rows']:
                    deleteDict = {'enterPriseIds':dictListItem['id']}
                    deleteAnQuanShengChan(deleteDict)
                         
#  删除消防安全重点
        if CommonIntf.getDbQueryResult(dbCommand='select count(*) from ENTERPRISES') != 0:
            compDict = copy.deepcopy(ZuZhiChangSuoPara.getXiaoFangAnQuan)
            compDict['orgId']= orgInit['DftWangGeOrgId']
            response = pinganjianshe_get(url='/baseinfo/fireSafetyEnterpriseManage/fireSafetyEnterpriseList.action', param=compDict)
            responseDict = json.loads(response.text)
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无消防安全重点')  
            else:
                for dictListItem in responseDict['rows']:
                    deleteDict = {'enterPriseIds':dictListItem['id']}
                    deleteXiaoFangAnQuan(deleteDict)                        
          
#  删除治安重点
        if CommonIntf.getDbQueryResult(dbCommand='select count(*) from ENTERPRISES') != 0:
            compDict = copy.deepcopy(ZuZhiChangSuoPara.getZhiAnZhongDian)
            compDict['orgId']= orgInit['DftWangGeOrgId']
            response = pinganjianshe_get(url='/baseinfo/safetyProductionKeyManage/safetyProductionKeyList.action', param=compDict)
            responseDict = json.loads(response.text)
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无治安重点')  
            else:
                for dictListItem in responseDict['rows']:
                    deleteDict = {'enterPriseIds':dictListItem['id']}
                    deleteZhiAnZhongDian(deleteDict)                     
     
#  删除学校
        if CommonIntf.getDbQueryResult(dbCommand='select count(*) from SCHOOLS') != 0:
            compDict = copy.deepcopy(ZuZhiChangSuoPara.getXueXiao)
            compDict['orgId']= orgInit['DftWangGeOrgId']
            response = pinganjianshe_get(url='/baseinfo/schoolManage/schoolList.action', param=compDict)
            responseDict = json.loads(response.text)
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无学校')  
            else:
                for dictListItem in responseDict['rows']:
                    deleteDict = {'schoolIds':dictListItem['id']}
                    deleteXueXiao(deleteDict)          
                             
#  删除医院
        if CommonIntf.getDbQueryResult(dbCommand='select count(*) from HOSPITALS') != 0:
            compDict = copy.deepcopy(ZuZhiChangSuoPara.getYiYuan)
            compDict['organizationId']= orgInit['DftWangGeOrgId']
            response = pinganjianshe_get(url='/baseinfo/hospitalManage/hospitalList.action', param=compDict)
            responseDict = json.loads(response.text)
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无医院')  
            else:
                for dictListItem in responseDict['rows']:
                    deleteDict = {'locationIds':dictListItem['id']}
                    deleteYiYuan(deleteDict)                                    
             
#  删除危险化学品单位
        if CommonIntf.getDbQueryResult(dbCommand='select count(*) from DANGEROUSCHEMICALSUNIT') != 0:
            compDict = copy.deepcopy(ZuZhiChangSuoPara.getWeiXianHuaXuePing)
            compDict['organizationId']= orgInit['DftWangGeOrgId']
            response = pinganjianshe_get(url='/baseinfo/dangerousChemicalsUnitManage/dangerousChemicalsUnitList.action', param=compDict)
            responseDict = json.loads(response.text)
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无危险化学品单位')  
            else:
                for dictListItem in responseDict['rows']:
                    deleteDict = {'locationIds':dictListItem['id']}
                    deleteWeiXianHuaXuePing(deleteDict)                
                             
#  删除上网服务单位
        if CommonIntf.getDbQueryResult(dbCommand='select count(*) from INTERNETBAR') != 0:
            compDict = copy.deepcopy(ZuZhiChangSuoPara.getShangWanFuWu)
            compDict['organizationId']= orgInit['DftWangGeOrgId']
            response = pinganjianshe_get(url='/baseinfo/internetBarManage/internetBarList.action', param=compDict)
            responseDict = json.loads(response.text)
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无上网服务单位')  
            else:
                for dictListItem in responseDict['rows']:
                    deleteDict = {'locationIds':dictListItem['id']}
                    deleteShangWanFuWu(deleteDict)                                    
                             
                             
#  删除公共场所
        if CommonIntf.getDbQueryResult(dbCommand='select count(*) from PUBLICPLACE') != 0:
            compDict = copy.deepcopy(ZuZhiChangSuoPara.getGongGongChangSuo)
            compDict['organizationId']= orgInit['DftWangGeOrgId']
            response = pinganjianshe_get(url='/baseinfo/publicPlaceManage/publicPlaceList.action', param=compDict)
            responseDict = json.loads(response.text)
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无公共场所')  
            else:
                for dictListItem in responseDict['rows']:
                    deleteDict = {'locationIds':dictListItem['id']}
                    deleteGongGongChangSuo(deleteDict)                                
                         
#  删除公共复杂场所
        if CommonIntf.getDbQueryResult(dbCommand='select count(*) from COMMONCOMPLEXPLACES') != 0:
            compDict = copy.deepcopy(ZuZhiChangSuoPara.getGongGongFuZaChangSuo)
            compDict['organizationId']= orgInit['DftWangGeOrgId']
            response = pinganjianshe_get(url='/baseinfo/commonComplexPlaceManage/commonComplexPlaceList.action', param=compDict)
            responseDict = json.loads(response.text)
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无公共复杂场所')  
            else:
                for dictListItem in responseDict['rows']:
                    deleteDict = {'locationIds':dictListItem['id']}
                    deleteGongGongFuZaChangSuo(deleteDict)        
                         
#  删除特种行业
        if CommonIntf.getDbQueryResult(dbCommand='select count(*) from SPECIALTRADES') != 0:
            compDict = copy.deepcopy(ZuZhiChangSuoPara.getTeZhongHangYe)
            compDict['organizationId']= orgInit['DftWangGeOrgId']
            response = pinganjianshe_get(url='/baseinfo/specialTradeManage/specialTradeList.action', param=compDict)
            responseDict = json.loads(response.text)
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无特种行业')  
            else:
                for dictListItem in responseDict['rows']:
                    deleteDict = {'locationIds':dictListItem['id']}
                    deleteTeZhongHangYe(deleteDict)                            
 
#  删除其他场所
        if CommonIntf.getDbQueryResult(dbCommand='select count(*) from OTHERLOCALES') != 0:
            compDict = copy.deepcopy(ZuZhiChangSuoPara.getQiTaChangSuo)
            compDict['orgId']= orgInit['DftWangGeOrgId']
            response = pinganjianshe_get(url='/baseinfo/otherLocaleManage/otherLocaleList.action', param=compDict)
            responseDict = json.loads(response.text)
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无其他场所')  
            else:
                for dictListItem in responseDict['rows']:
                    deleteDict = {'otherLocaleIds':dictListItem['id']}
                    deleteQiTaChangSuo(deleteDict)                                                       
 
#  删除社会组织
        if CommonIntf.getDbQueryResult(dbCommand='select count(*) from NEWSOCIETYORGANIZATIONS') != 0:
            compDict = copy.deepcopy(ZuZhiChangSuoPara.getSheHuiZuZhi)
            compDict['organizationId']= orgInit['DftWangGeOrgId']
            response = pinganjianshe_get(url='/baseinfo/newSocietyOrganizationsManage/newSocietyOrganizationsList.action', param=compDict)
            responseDict = json.loads(response.text)
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无社会组织')  
            else:
                for dictListItem in responseDict['rows']:
                    deleteDict = {'locationIds':dictListItem['id']}
                    deleteSheHuiZuZhi(deleteDict)    
 
#  删除新经济组织      
        if CommonIntf.getDbQueryResult(dbCommand='select count(*) from NEWECONOMICORGANIZATIONS') != 0:
            compDict = copy.deepcopy(ZuZhiChangSuoPara.getXinJingJiZuZhi)
            compDict['organizationId']= orgInit['DftWangGeOrgId']
            response = pinganjianshe_get(url='/baseinfo/newEconomicOrganizationsManage/findNewEconomicOrganizations.action', param=compDict)
            responseDict = json.loads(response.text)
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无新经济组织')  
            else:
                for dictListItem in responseDict['rows']:
                    deleteDict = {'newEconomicOrganizationsIds':dictListItem['id']}
                    deleteXinJingJiZuZhi(deleteDict)   
  
#  删除规上企业
        if CommonIntf.getDbQueryResult(dbCommand='select count(*) from ENTERPRISES') != 0:
            compDict = copy.deepcopy(ZuZhiChangSuoPara.getGuiShangQiYe)
            compDict['orgId']= orgInit['DftWangGeOrgId']
            response = pinganjianshe_get(url='/baseinfo/safetyProductionKeyManage/safetyProductionKeyList.action', param=compDict)
            responseDict = json.loads(response.text)
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无规上企业')  
            else:
                for dictListItem in responseDict['rows']:
                    deleteDict = {'enterPriseIds':dictListItem['id']}
                    deleteGuiShangQiYe(deleteDict)  
 
#  删除规下企业
        if CommonIntf.getDbQueryResult(dbCommand='select count(*) from ENTERPRISES') != 0:
            compDict = copy.deepcopy(ZuZhiChangSuoPara.getGuiXiaQiYe)
            compDict['orgId']= orgInit['DftWangGeOrgId']
            response = pinganjianshe_get(url='/baseinfo/safetyProductionKeyManage/safetyProductionKeyList.action', param=compDict)
            responseDict = json.loads(response.text)
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无规下企业')  
            else:
                for dictListItem in responseDict['rows']:
                    deleteDict = {'enterPriseIds':dictListItem['id']}
                    deleteGuiXiaQiYe(deleteDict)  
                        
#  删除无证无照场所
        if CommonIntf.getDbQueryResult(dbCommand='select count(*) from WITHOUTPLACE') != 0:
            compDict = copy.deepcopy(ZuZhiChangSuoPara.getWuZhengWuZhao)
            compDict['orgId']= orgInit['DftWangGeOrgId']
            response = pinganjianshe_get(url='/baseinfo/withoutPlaceManage/withoutPlaceList.action', param=compDict)
            responseDict = json.loads(response.text)
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无无证无照场所')  
            else:
                for dictListItem in responseDict['rows']:
                    deleteDict = {'withoutPlaceIds':dictListItem['id']}
                    deleteWuZhengWuZhao(deleteDict)  
                        
#      删除记录
        if CommonIntf.getDbQueryResult(dbCommand='select count(*) from SERVICERECORDS') != 0:                
            compDict = copy.deepcopy(ZuZhiChangSuoPara.getXunChangQingKuang)
            compDict['serviceRecordVo.organization.id']= orgInit['DftWangGeOrgId']
            response = pinganjianshe_get(url='/plugin/serviceTeam/serviceRecord/findServiceRecords.action', param=compDict)
            responseDict = json.loads(response.text)
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无记录')  
            else:
                for dictListItem in responseDict['rows']:
                    deleteDict = {'recordIds':dictListItem['id']}
                    deletejilu(deleteDict)
                    
#      删除安全生产企业
        if CommonIntf.getDbQueryResult(dbCommand='select count(*) from SERVICERECORDS') != 0:                
            compDict = copy.deepcopy(ZuZhiChangSuoPara.getAnQuanShengChanQiYe)
            compDict['orgId']= orgInit['DftWangGeOrgId']
            response = pinganjianshe_get(url='/baseinfo/safeProductionEnterpriseManage/findSafeProductionEnterpriseForListPage.action', param=compDict)
            responseDict = json.loads(response.text)
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无记录')  
            else:
                for dictListItem in responseDict['rows']:
                    deleteDict = {'selectIds':dictListItem['id']}
                    deleteAnQuanShengChanQiYe(deleteDict)                    
                        
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '删除失败')
            return False     
    return True       

# 删除安全生产企业
def deleteAnQuanShengChanQiYe(AnQuanShengChanQiYeDict, username = None, password = None):  
        Log.LogOutput(LogLevel.INFO, "删除安全生产企业开始")
        response = pinganjianshe_get(url='/baseinfo/safeProductionEnterpriseManage/deleteSafeProductionEnterprise.action', param=AnQuanShengChanQiYeDict,username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "删除安全生产企业成功")
        else:
            Log.LogOutput(LogLevel.ERROR, "删除安全生产企业失败")    
            return response 

# 删除实有单位
def deleteShiYouDanWei(ShiYouDanWeiDict, username = None, password = None):  
        Log.LogOutput(LogLevel.INFO, "删除实有单位开始")
        response = pinganjianshe_get(url='/baseinfo/actualCompanyManage/deleteActualCompanyByIds.action', param=ShiYouDanWeiDict,username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "删除实有单位成功")
        else:
            Log.LogOutput(LogLevel.ERROR, "删除实有单位失败")    
            return response 
        
#         删除服务人员
def deleteFuWuRenYuan(FuWuRenYuanDict, username = None, password = None):  
        Log.LogOutput(LogLevel.INFO, "删除服务人员开始")
        response = pinganjianshe_get(url='/plugin/serviceTeam/serviceTeamMember/deleteServiceTeamMember.action', param=FuWuRenYuanDict,username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "删除服务人员成功")
        else:
            Log.LogOutput(LogLevel.ERROR, "删除服务人员失败")    
            return response 

# 删除安全生产重点 
def deleteAnQuanShengChan(AnQuanShengChanDict, username = None, password = None):  
        Log.LogOutput(LogLevel.INFO, "删除安全生产重点开始")
        response = pinganjianshe_get(url='/baseinfo/safetyProductionKeyManage/deleteSafetyProductionKey.action', param=AnQuanShengChanDict,username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "删除安全生产重点成功")
        else:
            Log.LogOutput(LogLevel.ERROR, "删除安全生产重点失败")    
            return response 
        
#  删除消防安全重点
def deleteXiaoFangAnQuan(XiaoFangAnQuanDict, username = None, password = None):  
        Log.LogOutput(LogLevel.INFO, "删除消防安全重点开始")
        response = pinganjianshe_get(url='/baseinfo/safetyProductionKeyManage/deleteEnterprise.action', param=XiaoFangAnQuanDict,username=username, password=password)
#         print response.text
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "删除消防安全重点成功")
        else:
            Log.LogOutput(LogLevel.ERROR, "删除消防安全重点失败")    
            return response 
        
#  删除治安重点
def deleteZhiAnZhongDian(ZhiAnZhongDianDict, username = None, password = None):  
        Log.LogOutput(LogLevel.INFO, "删除治安重点开始")
        response = pinganjianshe_get(url='/baseinfo/safetyProductionKeyManage/deleteSafetyProductionKey.action', param=ZhiAnZhongDianDict,username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "删除治安重点成功")
        else:
            Log.LogOutput(LogLevel.ERROR, "删除治安重点失败")    
            return response    
        
#  删除学校
def deleteXueXiao(XueXiaoDict, username = None, password = None):  
        Log.LogOutput(LogLevel.INFO, "删除学校开始")
        response = pinganjianshe_get(url='/baseinfo/schoolManage/deleteSchool.action', param=XueXiaoDict,username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "删除学校成功")
        else:
            Log.LogOutput(LogLevel.ERROR, "删除学校失败")    
            return response       
        
#  删除医院
def deleteYiYuan(YiYuanDict, username = None, password = None):  
        Log.LogOutput(LogLevel.INFO, "删除医院开始")
        response = pinganjianshe_get(url='/baseinfo/hospitalManage/deleteHospitalByIds.action', param=YiYuanDict,username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "删除医院成功")
        else:
            Log.LogOutput(LogLevel.ERROR, "删除医院失败")    
            return response   
 
#  删除危险化学品单位
def deleteWeiXianHuaXuePing(WeiXianHuaXuePingDict, username = None, password = None):  
        Log.LogOutput(LogLevel.INFO, "删除危险化学品单位开始")
        response = pinganjianshe_get(url='/baseinfo/dangerousChemicalsUnitManage/deleteDangerousChemicalsUnitByIds.action', param=WeiXianHuaXuePingDict,username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "删除危险化学品单位成功")
        else:
            Log.LogOutput(LogLevel.ERROR, "删除危险化学品单位失败")    
            return response         
        
#  删除上网服务单位
def deleteShangWanFuWu(ShangWanFuWuDict, username = None, password = None):  
        Log.LogOutput(LogLevel.INFO, "删除上网服务单位开始")
        response = pinganjianshe_get(url='/baseinfo/internetBarManage/deleteInternetBarByIds.action', param=ShangWanFuWuDict,username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "删除上网服务单位成功")
        else:
            Log.LogOutput(LogLevel.ERROR, "删除上网服务单位失败")    
            return response                  
        
#  删除公共场所
def deleteGongGongChangSuo(GongGongChangSuoDict, username = None, password = None):  
        Log.LogOutput(LogLevel.INFO, "删除公共场所开始")
        response = pinganjianshe_get(url='/baseinfo/publicPlaceManage/deletePublicPlaceByIds.action', param=GongGongChangSuoDict,username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "删除公共场所成功")
        else:
            Log.LogOutput(LogLevel.ERROR, "删除公共场所失败")    
            return response       
        
#  删除公共复杂场所
def deleteGongGongFuZaChangSuo(GongGongFuZaChangSuoDict, username = None, password = None):  
        Log.LogOutput(LogLevel.INFO, "删除公共复杂场所开始")
        response = pinganjianshe_get(url='/baseinfo/commonComplexPlaceManage/deleteCommonComplexPlaceByIds.action', param=GongGongFuZaChangSuoDict,username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "删除公共复杂场所成功")
        else:
            Log.LogOutput(LogLevel.ERROR, "删除公共复杂场所失败")    
            return response             
            
#  删除特种行业
def deleteTeZhongHangYe(TeZhongHangYeDict, username = None, password = None):  
        Log.LogOutput(LogLevel.INFO, "删除特种行业开始")
        response = pinganjianshe_get(url='/baseinfo/specialTradeManage/deleteSpecialTradeByIds.action', param=TeZhongHangYeDict,username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "删除特种行业成功")
        else:
            Log.LogOutput(LogLevel.ERROR, "删除特种行业失败")    
            return response                 
  
#  删除其他场所
def deleteQiTaChangSuo(QiTaChangSuoDict, username = None, password = None):  
        Log.LogOutput(LogLevel.INFO, "删除其他场所开始")
        response = pinganjianshe_get(url='/baseinfo/otherLocaleManage/deleteOtherLocale.action', param=QiTaChangSuoDict,username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "删除其他场所成功")
        else:
            Log.LogOutput(LogLevel.ERROR, "删除其他场所失败")    
            return response           

#  删除社会组织
def deleteSheHuiZuZhi(SheHuiZuZhiDict, username = None, password = None):  
        Log.LogOutput(LogLevel.INFO, "删除社会组织开始")
        response = pinganjianshe_get(url='/baseinfo/newSocietyOrganizationsManage/deleteNewSocietyOrganizationsByIds.action', param=SheHuiZuZhiDict,username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "删除社会组织成功")
        else:
            Log.LogOutput(LogLevel.ERROR, "删除社会组织失败")    
            return response      

#  删除新经济组织
def deleteXinJingJiZuZhi(XinJingJiZuZhiDict, username = None, password = None):  
        Log.LogOutput(LogLevel.INFO, "删除新经济组织开始")
        response = pinganjianshe_get(url='/baseinfo/newEconomicOrganizationsManage/deleteNewEconomicOrganizations.action', param=XinJingJiZuZhiDict,username=username, password=password)
        if response.result is True:              
            Log.LogOutput(LogLevel.INFO, "删除新经济组织成功")
        else:
            Log.LogOutput(LogLevel.ERROR, "删除新经济组织失败")    
            return response      
        
#  删除规上企业
def deleteGuiShangQiYe(GuiShangQiYeDict, username = None, password = None):  
        Log.LogOutput(LogLevel.INFO, "删除规上企业开始")
        response = pinganjianshe_get(url='/baseinfo/safetyProductionKeyManage/deleteEnterprise.action', param=GuiShangQiYeDict,username=username, password=password)
#        print response.text
        if response.result is True:            
            Log.LogOutput(LogLevel.INFO, "删除规上企业成功")
        else:
            Log.LogOutput(LogLevel.ERROR, "删除规上企业失败")    
            return response       
                                             
#  删除规下企业
def deleteGuiXiaQiYe(GuiXiaQiYeDict, username = None, password = None):  
        Log.LogOutput(LogLevel.INFO, "删除规下企业开始")
        response = pinganjianshe_get(url='/baseinfo/safetyProductionKeyManage/deleteEnterprise.action', param=GuiXiaQiYeDict,username=username, password=password)
        if response.result is True:            
            Log.LogOutput(LogLevel.INFO, "删除规下企业成功")
        else:
            Log.LogOutput(LogLevel.ERROR, "删除规下企业失败")    
            return response     
        
#  删除无证无照场所
def deleteWuZhengWuZhao(WuZhengWuZhaoDict, username = None, password = None):  
        Log.LogOutput(LogLevel.INFO, "删除无证无照场所开始")
        response = pinganjianshe_get(url='/baseinfo/withoutPlaceManage/deleteWithoutPlace.action', param=WuZhengWuZhaoDict,username=username, password=password)
        if response.result is True:            
            Log.LogOutput(LogLevel.INFO, "删除无证无照场所成功")
        else:
            Log.LogOutput(LogLevel.ERROR, "删除无证无照场所失败")    
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
