# -*- coding:UTF-8 -*-
'''
Created on 2016-4-13

@author: lhz
'''
#新建平台消息
from __future__ import unicode_literals
from Web_Test.CONFIG.Define import LogLevel
from Web_Test.Interface.PingAnTong.pingAnTongHttpCommon import pingantong_post
from Web_Test.COMMON import Log, CommonUtil
from Web_Test.Interface.PingAnTong.XiaoXi import MbXiaoXiPara
import copy
import json
def newMessage(param , username = None , password = None):
    Log.LogOutput(LogLevel.DEBUG, "消息 --新建平台消息....")
    try:    
        response = pingantong_post(url = '/mobile/outboxPlatformMessageMobileManage/sendPlatformMessage.action', postdata=param , username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "消息 --新建平台消息成功")
            return True
        else:
            Log.LogOutput(LogLevel.ERROR, "消息 --新建平台消息失败")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '消息 --新建平台消息过程中失败')
        return False    
    
    
#查找发件箱内容  
def check_sendMessage(companyDict,username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "查找发件箱内容开始。。。")
        compDict = copy.deepcopy(MbXiaoXiPara.lookMessage)
        response = pingantong_post(url='/mobile/outboxPlatformMessageMobileManage/findOutboxPlatformMessage.action', postdata=compDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict= responseDict['rows'] 
        if CommonUtil.findDictInDictlist(companyDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "查找发件箱内容成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查找发件箱内容失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查找发件箱内容过程中失败')
            return False  
           
#查看收信人是否收到消息     
def check_ReceiveMessage(companyDict,username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "检验收信人是否收到消息。。。")
        compDict = copy.deepcopy(MbXiaoXiPara.lookMessage)
        response = pingantong_post(url='/mobile/inboxPlatformMessageMobileManage/findInboxPlatformMessageList.action', postdata=compDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict= responseDict['rows'] 
        if CommonUtil.findDictInDictlist(companyDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "收信人成功收到消息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "收信人无法收到消息")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查找收信人是否收到消息程中失败')
            return False 
        
                 
#查看收信人是否收到消息     
def check_ReceiveMessagePC(companyDict,username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "检验PC端收信人是否收到消息。。。")
        compDict = copy.deepcopy(MbXiaoXiPara.lookMessage)
        response = pingantong_post(url='/mobile/inboxPlatformMessageMobileManage/findInboxPlatformMessageList.action', postdata=compDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict= responseDict['rows'] 
        if CommonUtil.findDictInDictlist(companyDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "收信人成功收到消息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "收信人无法收到消息")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查找收信人是否收到消息程中失败')
            return False   
        
#回复消息        
def replyMessage(param , username = None , password = None):
    print (param)
    Log.LogOutput(LogLevel.DEBUG, "消息 --回复平台消息....")
    try:    
        response = pingantong_post(url = '/mobile/inboxPlatformMessageMobileManage/replyPlatformMessage.action', postdata=param , username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "消息 --回复平台消息成功")
            return True
        else:
                Log.LogOutput(LogLevel.ERROR, "消息 --回复平台消息失败")
                return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '消息 --回复平台消息过程中失败')
        return False           
        
#删除消息
def deleteMessage(param , username = None , password = None):
    Log.LogOutput(LogLevel.DEBUG, "消息 --删除平台消息....")
    try:    
        compDict = copy.deepcopy(MbXiaoXiPara.deleteMessage)
        compDict['ids'] = 615
        response = pingantong_post(url = '/mobile/outboxPlatformMessageMobileManage/findOutboxPlatformMessage.action', postdata=compDict , username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "消息 --删除平台消息成功")
            return True
        else:
                Log.LogOutput(LogLevel.ERROR, "消息 --删除平台消息失败")
                return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '消息 --删除平台消息过程中失败')
        return False                 
     