# -*- coding:UTF-8 -*-
'''
Created on 2016-3-24

@author: lhz
'''
from __future__ import unicode_literals
from COMMON import Log, CommonUtil
from CONFIG.Define import LogLevel
from Interface.PingAnTong.pingAnTongHttpCommon import pingantong_post
from Interface.PingAnTong.XunJian import MbXunJianPara
import copy
import json
from Interface.PingAnJianShe.pingAnJianSheHttpCommon import pinganjianshe_get
from CONFIG import InitDefaultPara
'''
    @功能：手机巡检新增企业信息
    @para:Para
    @return:    true/false
    @author:  lhz 2016-3-35
'''  
def xunJianAdd(param,username = None,password = None):
    Log.LogOutput(level=LogLevel.INFO, message = '巡检--新增企业信息.....')
    try:    
        response = pingantong_post(url='/mobile/safeProductionEnterpriseMobileManage/addSafeProductionEnterpriseForMobile.action', postdata=param , username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, '巡检新增企业信息成功')
            return True
        else:
            Log.LogOutput(LogLevel.ERROR, '巡检新增企业信息失败')
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '巡检新增企业信息过程中失败')
        return False  
    
#修改巡检企业信息    
def xunJianEdit(param,username = None,password = None):
    Log.LogOutput(level=LogLevel.INFO, message = '巡检--修改企业信息.....')
    try:    
        response = pingantong_post(url='/mobile/safeProductionEnterpriseMobileManage/updateSafeProductionEnterpriseForMobile.action', postdata=param , username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, '巡检修改企业信息成功')
            return True
        else:
                Log.LogOutput(LogLevel.ERROR, '巡检修改企业信息失败')
                return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '巡检修改企业信息过程中失败')
        return False      
    
'''
    @功能：检查新增的企业是否列表显示
'''  
#列表查找
def check_addCompany(companyDict,orgId = None,username = None, password = None):
    try: 
        Log.LogOutput(LogLevel.DEBUG, "进入到查找新增企业是否成功.....")
        getListDict =  copy.deepcopy(MbXunJianPara.companyListParam)
        getListDict['orgId'] =  orgId 
        response = pingantong_post(url='/mobile/safeProductionEnterpriseMobileManage/findSafeProductionEnterpriseForMobile.action',postdata=getListDict, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取要查询的参数
        #对比查询出来的数据和要查询的是否一样
        if CommonUtil.findDictInDictlist(companyDict,responseDict['Data']['rows']) is True:
            Log.LogOutput(message = '查找到企业')
            return True
        else:
            Log.LogOutput(message = '没查找到企业')
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '查找企业信息过程中失败')
        return False     
    
'''
    @功能：PC端检查新增的企业是否列表显示
'''  
#列表查找
def check_editCompany(companyDict,orgId = None,username = None, password = None):
    try: 
        Log.LogOutput(LogLevel.DEBUG, "进入到PC端查找企业信息.....")
        getListDict =  copy.deepcopy(MbXunJianPara.companyListPcParam)
        getListDict['orgId'] =  orgId  
        response = pinganjianshe_get(url='/baseinfo/safeProductionEnterpriseManage/findSafeProductionEnterpriseForListPage.action',param=getListDict, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取要查询的参数
        #对比查询出来的数据和要查询的是否一样
        if CommonUtil.findDictInDictlist(companyDict,responseDict['rows']) is True:
            Log.LogOutput(message = '查找到企业')
            return True
        else:
            Log.LogOutput(message = '没查找到企业')
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '查找企业信息过程中失败')
        return False        
 
    
#新增巡检记录    
def addXunJianRecord(param,username = None,password = None):
    Log.LogOutput(level=LogLevel.INFO, message = '巡检--新增巡检记录.....')
    try:    
        response = pingantong_post(url='/mobile/inspectionRecordMobileManage/addInspectionForMobile.action', postdata=param , username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, '新增巡检记录成功')
            return True
        else:
                Log.LogOutput(LogLevel.ERROR, '新增巡检记录失败')
                return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '新增巡检记录过程中失败')
        return False  
    

'''
    @功能：     
#检查巡检记录
'''  
#列表查找
def check_xunjianRecord(companyDict,orgId = None,username = None, password = None):
    try: 
        Log.LogOutput(LogLevel.DEBUG, "进入到检查巡检记录中.....")
        getListDict =  copy.deepcopy(MbXunJianPara.check_record)
        getListDict['recordType'] =  orgId  
        response = pinganjianshe_get(url='/baseinfo/safeProductionEnterpriseManage/findSafeProductionEnterpriseForListPage.action',param=getListDict, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取要查询的参数
        #对比查询出来的数据和要查询的是否一样
        if CommonUtil.findDictInDictlist(companyDict,responseDict['rows']) is True:
            Log.LogOutput(message = '查找到企业')
            return True
        else:
            Log.LogOutput(message = '没查找到企业')
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '查找企业信息过程中失败')
        return False   
    
    
'''
    @功能：     
#检查巡检记录详情
'''  
#列表查找
def check_xunjianRecordXq(companyDict,checkParam,username = None, password = None):
    try: 
        Log.LogOutput(LogLevel.DEBUG, "进入到检查巡检记录详情中中.....")
        response = pingantong_post(url='/mobile/inspectionRecordMobileManage/findInspectionRecordForMobile.action',postdata=checkParam, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取要查询的参数
        #对比查询出来的数据和要查询的是否一样
        if CommonUtil.findDictInDictlist(companyDict,responseDict['Data']['rows']) is True:
            Log.LogOutput(message = '查找到巡检记录详情')
            return True
        else:
            Log.LogOutput(message = '没查找到巡检记录详情')
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '查找巡检记录详情过程中失败')
        return False 
    
        
    
#新增复查记录    
def addXunJianReCheck(param,username = None,password = None):
    Log.LogOutput(level=LogLevel.INFO, message = '巡检--新增复查记录.....')
    try:    
        response = pingantong_post(url='/mobile/inspectionRecordMobileManage/reviewInspectionForMobile.action', postdata=param , username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, '新增复查记录成功')
            return True
        else:
                Log.LogOutput(LogLevel.ERROR, '新增复查记录失败')
                return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '新增复查记录过程中失败')
        return False    
    
#检查复查记录    
def XunJianReCheck(param, companyDict,username = None,password = None):
    Log.LogOutput(level=LogLevel.INFO, message = '巡检--新增复查记录检查.....')
    try:    
        response = pingantong_post(url='/mobile/inspectionRecordMobileManage/viewReviewInspectionRecordForMobile.action', postdata=param , username=username, password=password)
        responseDict = json.loads(response.text)
        if CommonUtil.regMatchString(companyDict,responseDict['Data']['enterprise']['address']) is True:
            Log.LogOutput(message = '查找到复查记录')
            return True
        else:
            Log.LogOutput(message = '没查找到复查记录')
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '查找复查记录过程中失败')
        return False  




#高级搜索 不期望中的 企业名称
def searchNot(param,companyDict,username = None, password = None):
    try: 
        Log.LogOutput(LogLevel.DEBUG, "进入到高级搜索企业名称不期望中.....")
        searchParam =  copy.deepcopy(MbXunJianPara.searchParam)
        searchParam['orgId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        searchParam['safeProductionEnterprise.fastSearchKeyWords'] = companyDict['name']
        response = pingantong_post(url='/mobile/safeProductionEnterpriseMobileManage/findSafeProductionEnterpriseForMobile.action',postdata=searchParam, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取要查询的参数
        #对比查询出来的数据和要查询的是否一样
        if CommonUtil.findDictInDictlist(param,responseDict['Data']['rows']) is True:
            Log.LogOutput(message = '查找到不期望中的企业名称')
            return True
        else:
            Log.LogOutput(message = '没查找到不期望中企业名称')
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '查找不期望中企业名称信息过程中失败')
        return False  
    
    
#高级搜索 不期望中的
def searchAddressNot(param,companyDict,username = None, password = None):
    try: 
        Log.LogOutput(LogLevel.DEBUG, "进入到高级搜索企业地址不期望中.....")
        searchParam =  copy.deepcopy(MbXunJianPara.searchParam)
        searchParam['orgId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        searchParam['safeProductionEnterprise.address'] = companyDict['address']
        response = pingantong_post(url='/mobile/safeProductionEnterpriseMobileManage/findSafeProductionEnterpriseForMobile.action',postdata=searchParam, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取要查询的参数
        #对比查询出来的数据和要查询的是否一样
        if CommonUtil.findDictInDictlist(param,responseDict['Data']['rows']) is True:
            Log.LogOutput(message = '查找到不期望中的企业地址')
            return True
        else:
            Log.LogOutput(message = '没查找到不期望中企业地址')
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '查找不期望中企业地址信息过程中失败')
        return False      
    
#高级搜索 期望中的[ps:输入列表中存在的数据进行查询]
def search(param,companyDict,username = None, password = None):
        Log.LogOutput(LogLevel.DEBUG, "进入到高级搜索企业名称期望中.....")
        searchParam =  copy.deepcopy(MbXunJianPara.searchParam)
        searchParam['orgId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        searchParam['safeProductionEnterprise.fastSearchKeyWords'] = companyDict['name']
        searchParam['safeProductionEnterprise.address'] = companyDict['address']
        response = pingantong_post(url='/mobile/safeProductionEnterpriseMobileManage/findSafeProductionEnterpriseForMobile.action',postdata=searchParam, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取的数据集合
        record = responseDict['Data']['records']
        if record == 0 :
            Log.LogOutput(level=LogLevel.DEBUG, message='企业信息数据搜索失败')
            return False 
        else:
                Log.LogOutput(level=LogLevel.DEBUG, message='企业信息数据搜索成功') 
                return True
            

    
      
    