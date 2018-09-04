# -*- coding:UTF-8 -*-
'''
Created on 2015-11-24

@author: N-133
'''
from __future__ import unicode_literals
from Web_Test.COMMON import Log, CommonUtil
from Web_Test.CONFIG.Define import LogLevel
from Web_Test.Interface.XianSuoApp.xianSuoHttpCommon import xiansuo_post, xiansuo_get
import copy
from Web_Test.Interface.PingAnTong.XianSuo import XianSuoPara
import json
from Web_Test.Interface.PingAnJianShe.pingAnJianSheHttpCommon import pinganjianshe_get


'''
    @功能：手机新增线索
    @XianSuoPara.XinZeng
    @return:    response
    @author:  chenguiliang 2016-03-08
'''  

# 新增线索
def addXianSuo(XianSuoDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增线索开始")
    response = xiansuo_post(url='/informationDubboService/addInformationForMobile', postdata=XianSuoDict)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "新增线索成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "新增线索失败")
    return response

# 查看线索是否新增成功
def checkxiansuoCompany(companyDict,  username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "查看线索开始")
        compDict = copy.deepcopy(XianSuoPara.chakanxiansuo)
        response = pinganjianshe_get(url='/clueManage/clueInformationManage/findClueInformationPageBySearchsInfoVo.action', param=compDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict= responseDict['rows']
        if CommonUtil.findDictInDictlist(companyDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "查看线索成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查看线索失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查看失败')
            return False  
