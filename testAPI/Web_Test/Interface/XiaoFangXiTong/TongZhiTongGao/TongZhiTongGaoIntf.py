# -*- coding:UTF-8 -*-
'''
Created on 2016-6-7

@author: maoxy
'''
from __future__ import unicode_literals
from COMMON import Log,CommonUtil
from CONFIG.Define import LogLevel
from Interface.XiaoFangXiTong import xiaoFangXiTongHttpCommon
from COMMON.CommonUtil import findDictInDictlist
import json
from Interface.XiaoFangXiTong.TongZhiTongGao import TongZhiTongGaoPara
import copy





def Add_TongZhiTongGao(TongZhiTongGaoDict,username=None,password=None):
    Log.LogOutput(LogLevel.INFO,'新增通知通告开始..')
    response=xiaoFangXiTongHttpCommon.xiaofang_post(url='/fire/fireNoticeManage/saveFireNoticeInfo.action',postdata=TongZhiTongGaoDict,username=username,password=password)
#     print response.text
#     print response.result
    return response

def Get_TongZhiTongGao(TongZhiTongGaoDict,username=None,password=None):
    try:
        Log.LogOutput(LogLevel.INFO, "查看通知通告开始")
        compDict = copy.deepcopy(TongZhiTongGaoPara.GetTongZhiTongGao)
        compDict['queryParameter.orgId']='1'
        response = xiaoFangXiTongHttpCommon.xiaofang_get(url='/fire/fireNoticeManage/getFireNoticeInfoByParam.action', param=compDict,username=username, password = password)
        responseDict = json.loads(response.text)                    
        listDict= responseDict['rows']
        if CommonUtil.findDictInDictlist(TongZhiTongGaoDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "查看通知通告成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查看通知通告失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查看失败')
            return False 
 
def Edit_TongZhiTongGao(TongZhiTongGaoDict,username=None,password=None):
    Log.LogOutput(LogLevel.INFO,'修改通知通告开始..')
    response=xiaoFangXiTongHttpCommon.xiaofang_post(url='/fire/fireNoticeManage/saveFireNoticeInfo.action',postdata=TongZhiTongGaoDict,username=username,password=password)
#     if response.result is True:
#         Log.LogOutput(LogLevel.INFO,'修改通知通告成功..')
#     else:
#         Log.LogOutput(LogLevel.INFO,'修改通知通告失败..')
    return response
 
def Del_TongZhiTongGao(TongZhiTongGaoDict,username=None,password=None):
    Log.LogOutput(LogLevel.INFO, message='删除通知通告开始..')
    response=xiaoFangXiTongHttpCommon.xiaofang_get(url='/fire/fireNoticeManage/deleteFireNoticeById.action',param=TongZhiTongGaoDict,username=username,password=password)
#     if response.result is True:
#         Log.LogOutput(LogLevel.INFO, message='删除通知通告成功..')
#     else:
#         Log.LogOutput(LogLevel.INFO,'删除通知通告失败..')
    return response   

     
    
    
    
    
    
    
    
    
    
    


