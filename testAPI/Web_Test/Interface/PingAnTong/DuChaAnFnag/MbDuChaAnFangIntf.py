# -*- coding:UTF-8 -*-
'''
Created on 2016-4-7

@author: lhz
'''
from __future__ import unicode_literals
from Web_Test.COMMON import Log, CommonUtil
from Web_Test.CONFIG.Define import LogLevel
from Web_Test.Interface.PingAnTong.pingAnTongHttpCommon import pingantong_post
import copy
from Web_Test.Interface.PingAnTong.DuChaAnFnag import MbDuChaAnFangPara
from Web_Test.CONFIG import InitDefaultPara
import json
from Web_Test.Interface.PingAnJianShe.pingAnJianSheHttpCommon import pinganjianshe_post
'''
    @功能：督查暗访新增
    @para:Para
    @return:    true/false
    @author:  lhz 2016-4-7
''' 
def KuaiShuShangBaoAdd(param,username = None,password = None):
    Log.LogOutput(level=LogLevel.INFO, message = '进入到督查暗访新增中.....')
    try:  
        response = pingantong_post(url='/mobile/secretSupervisionMobileManage/addSecretSupervisionForMobile.action', postdata=param , username=username, password=password)
        print (response.content)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, '督查暗访新增成功')
            return response
        else:
                Log.LogOutput(LogLevel.ERROR, '督查暗访新增失败')
                return response
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '督查暗访新增过程中失败')
        return response  
    
    
'''
    @功能：督查暗访检查
    @para:Para
    @return:    true/false
    @author:  lhz 2016-4-7
'''      
def check_KuaiShuShangBao(companyDict,username,password):   
    Log.LogOutput(level=LogLevel.INFO, message = '进入到督查暗访检查中.....')   
    try: 
        searchParam =  copy.deepcopy(MbDuChaAnFangPara.duChaAnFangListParam)
        searchParam['secretSupervisionVo.orgId'] =  InitDefaultPara.orgInit['DftJieDaoOrgId']
        response = pingantong_post(url='/mobile/secretSupervisionMobileManage/findSecretSupervisionForMobile.action',postdata=searchParam, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取要查询的参数
        #对比查询出来的数据和要查询的是否一样
        if CommonUtil.findDictInDictlist(companyDict,responseDict['Data']['rows']) is True:
            Log.LogOutput(message = '查找到督查暗访数据')
            return True
        else:
            Log.LogOutput(message = '没查找到督查暗访数据')
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '查找督查暗访过程中失败')
        return False     
    
'''
    @功能：督查暗访删除
    @para:Para
    @return:    true/false
    @author:  lhz 2016-4-7
''' 
def KuaiShuShangBaoDel(param,username = None,password = None):
    Log.LogOutput(level=LogLevel.INFO, message = '进入到督查暗访删除中.....')
    try:    
        response = pingantong_post(url='/mobile/secretSupervisionMobileManage/deleteSecretSupervisionForMobile.action', postdata=param , username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, '督查暗访删除成功')
            return True
        else:
                Log.LogOutput(LogLevel.ERROR, '督查暗访删除失败')
                return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '督查暗访删除过程中失败')
        return False      
    

'''
    @功能：督查暗访 高级搜索  --检查地址
    @param 
    @return:    true/false
    @author:  lhz 2016-4-7
'''  
#列表查找
def searchDuChaAnFangAddress(companyDict,param,username = None, password = None):
    try: 
        Log.LogOutput(LogLevel.DEBUG, "进入到督查暗访搜索企业地址中【期望中】....")
        getListDict =  copy.deepcopy(MbDuChaAnFangPara.searchDuChaAnFangParam)
        getListDict['secretSupervisionVo.checkAddress'] = companyDict['checkAddress']
        getListDict['secretSupervisionVo.orgId'] = InitDefaultPara.orgInit['DftJieDaoOrgId']
        response = pingantong_post(url='/mobile/secretSupervisionMobileManage/findSecretSupervisionForMobile.action',postdata=getListDict, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取的数据集合
        record = responseDict['Data']['records']
        if record == 0 :
            Log.LogOutput(level=LogLevel.DEBUG, message='信息数据搜索失败')
            return False 
        else:
                Log.LogOutput(level=LogLevel.DEBUG, message='信息数据搜索成功') 
                return True
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '搜索信息过程中失败')
        return False 
        
         
#搜索 期望中的[ps:输入列表中不存在的数据进行查询] 督查暗访 企业地址搜索
def searchDuChaAnFangAddressNot(companyDict,unit,orgId = None,username = None, password = None):
        Log.LogOutput(LogLevel.DEBUG, "进入到督查暗访搜索企业地址中【不期望中】....") 
        getListDict =  copy.deepcopy(MbDuChaAnFangPara.searchDuChaAnFangParam)
        getListDict['secretSupervisionVo.checkAddress'] = companyDict['checkAddress']
        getListDict['secretSupervisionVo.orgId'] = InitDefaultPara.orgInit['DftJieDaoOrgId']
        response = pingantong_post(url='/mobile/secretSupervisionMobileManage/findSecretSupervisionForMobile.action',postdata=getListDict, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取的数据集合
        record = responseDict['Data']['records']
        if record == 0 :
            Log.LogOutput(level=LogLevel.DEBUG, message='基础信息数据搜索失败')
            return False 
        else:
                if CommonUtil.findDictInDictlist(companyDict,responseDict['Data']['rows']) is True:
                    Log.LogOutput(message = '不存在的督查暗访企业地址匹配成功')
                    return True
                else:
                    Log.LogOutput(message = "不存在的督查暗访企业地址匹配失败")
                return False
                Log.LogOutput(level=LogLevel.DEBUG, message='不存在的督查暗访企业地址搜索过程中失败') 
                return True    
            
#PC端督查暗访 受理中心转事件
def TransferEvents(param, username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "PC端督查暗访 受理中心转事件中..")        
        response = pinganjianshe_post(url='/issues/issueManage/turnIssueAcceptCenter.action', postdata=param, username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "督查暗访 受理中心转事件成功")
            return response
        else:
            Log.LogOutput(LogLevel.ERROR, "督查暗访 受理中心转事件失败")
            return response
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '搜索信息过程中失败')
        return response         
            
#PC端事件处理 结案
def eventClosed(param, username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "PC端督查暗访 事件处理结案中..")        
        response = pinganjianshe_post(url='/issues/issueManage/dealIssue.action', postdata=param, username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "督查暗访 事件处理结案成功")
            return response
        else:
            Log.LogOutput(LogLevel.ERROR, "督查暗访 事件处理结案失败")
            return response
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '督查暗访 事件处理结案过程中失败')
        return response         

#督查暗访删除
def duChaAnFangDel(param , username = None, password = None):
    try:
        print (param)
        Log.LogOutput(LogLevel.INFO, "进入督查暗访删除中..")        
        response = pingantong_post(url='/mobile/secretSupervisionMobileManage/deleteSecretSupervisionForMobile.action', postdata=param, username=username, password=password)
        print (response.content)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "督查暗访删除成功")
            return response
        else:
            Log.LogOutput(LogLevel.ERROR, "督查暗访删除失败")
            return response
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '督查暗访删除过程中失败')
        return response      

            
            
               
         
     
    