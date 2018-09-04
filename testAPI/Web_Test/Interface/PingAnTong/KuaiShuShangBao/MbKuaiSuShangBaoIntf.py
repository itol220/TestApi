# -*- coding:UTF-8 -*-
'''
Created on 2016-4-7

@author: lhz
'''
from __future__ import unicode_literals
from Web_Test.CONFIG.Define import LogLevel
from Web_Test.Interface.PingAnTong.pingAnTongHttpCommon import pingantong_post
from Web_Test.COMMON import Log, CommonUtil
import copy
from Web_Test.CONFIG import InitDefaultPara
import json
from Web_Test.Interface.PingAnTong.KuaiShuShangBao import MbKuaiSuShangBaoPara
'''
    @功能：手机快速上报
    @para:Para
    @return:    true/false
    @author:  lhz 2016-4-7
'''  
def KuaiShuShangBaoAdd(param,username = None,password = None):
    Log.LogOutput(level=LogLevel.INFO, message = '进入到快速上报中.....')
    try:    
        response = pingantong_post(url='/mobile/issueNewMobileManage/addIssueAndSubmit.action', postdata=param , username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, '快速上报新增成功')
            return True
        else:
                Log.LogOutput(LogLevel.ERROR, '快速上报新增失败')
                return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '快速上报新增过程中失败')
        return False 
    
'''
    @功能：手机检查快速上报检查
    @para:Para
    @return:    true/false
    @author:  lhz 2016-4-7
'''      
def check_KuaiShuShangBao(companyDict,username,password):   
    Log.LogOutput(level=LogLevel.INFO, message = '进入到快速上报检查中.....')   
    try: 
        searchParam =  copy.deepcopy(MbKuaiSuShangBaoPara.check_reportParam)
        searchParam['orgId'] = InitDefaultPara.orgInit['DftShengOrgId'] #要到上一级中查看
        response = pingantong_post(url='/mobile/issueNewMobileManage/findNeedDoIssueList.action',postdata=searchParam, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取要查询的参数
        #对比查询出来的数据和要查询的是否一样
        if CommonUtil.findDictInDictlist(companyDict,responseDict['rows']) is True:
            Log.LogOutput(message = '查找到快速上报数据')
            return True
        else:
            Log.LogOutput(message = '没查找到快速上报数据')
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '查找快速上报过程中失败')
        return False  
    
    
    
    
    
    