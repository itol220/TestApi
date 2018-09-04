# -*- coding:UTF-8 -*-
'''
Created on 2016-4-8

@author: N-286
'''
from __future__ import unicode_literals
from COMMON import Log
from COMMON.CommonUtil import findDictInDictlist
from CONFIG.Define import LogLevel
from Interface.YunWeiPingTai.yunWeiPingTaiHttpCommon import xiansuoyunwei_post
import json
import copy
from Interface.YunWeiPingTai.YongHuGuanLi import YwYongHuGuanLiPara

'''
    @功能：查询手机用户、列表显示
    @return:    response
    @author:  chenhui 2016-04-11
'''  
def searchUser(para):
    Log.LogOutput(LogLevel.INFO, "查询用户")
    response = xiansuoyunwei_post(url='/userManage/findUserList', postdata=para)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "查询用户成功")
    else:
            Log.LogOutput(LogLevel.DEBUG, "查询用户失败")
    return response

'''
    @功能：检查用户是否存在于列表字典中
    @para:
    listpara:获取用户列表，请调用YwYongHuGuanLiPara中的getClueUserManageListPara对象
    checkpara:检查用户信息，请调用YwYongHuGuanLiPara中的checkClueUserManageListPara对象
    @return: 检查成功返回True,否则返回False
    @author:  chenhui 2016-04-11
'''   
def checkUserInUserManagerList(checkpara,listpara):
    Log.LogOutput(LogLevel.INFO, "检查用户是否在运维管理平台-用户管理列表中")
    try:
        response = searchUser(para=listpara)
        responseDict=json.loads(response.text)
#         #print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "用户存在于列表中")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "用户不存在于列表中")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '出现异常')
            return False

'''
    @功能：禁号
    @userId:用户id信息
    @return:成功则返回True;否则返回False
    @author:  chenhui 2016-04-11
'''  
def disable_user(userId):
    userDict = {
                "ids[]":userId
                }
    Log.LogOutput(LogLevel.INFO, "开始进行禁号操作......")
    response = xiansuoyunwei_post(url='/userManage/toDisable', postdata=userDict)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "禁号成功")
        return True
    else:
        Log.LogOutput(LogLevel.DEBUG, "禁号失败")
        return False

'''
    @功能：解禁
    @para:
    userId: 用户id
    @return: 解禁成功，返回True;否则返回False
    @author:  chenhui 2016-04-11
'''  
def enable_user(userId):
    Log.LogOutput(LogLevel.INFO, "解禁")
    userDict = {
                "ids[]":userId
                }
    response = xiansuoyunwei_post(url='/userManage/toUnDisable', postdata=userDict)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "解禁成功")
        return True
    else:
        Log.LogOutput(LogLevel.DEBUG, "解禁失败")
        return False

'''
    @功能：删除用户
    @para:
    userId:用户id信息
    @return: 删除成功，返回True;否则返回False
    @author:  chenhui 2016-04-11
'''  
def delete_user(userId):
    Log.LogOutput(LogLevel.INFO, "删除")
    userDict = {
                "ids[]":userId
                }
    response = xiansuoyunwei_post(url='/userManage/deleteUsers', postdata=userDict)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除成功")
        return True
    else:
        Log.LogOutput(LogLevel.DEBUG, "删除失败")
        return False

'''
    @功能：检查用户是否在运维管理平台-在线用户列表中
    @para:
    listpara:获取在线用户列表，请调用YwYongHuGuanLiIntf中的zaiXianYongHuGuanLiLieBiao
    checkpara：检查在线用户列表参数，请调用YwYongHuGuanLiIntf中的checkOnlineUserPara
    @return：检查成功，返回True;否则返回False
    @author:  chenhui 2016-4-7
'''  
def check_online_user_list(checkpara,listpara):
    Log.LogOutput(LogLevel.INFO, "检查用户是否在运维管理平台-在线用户列表中")
    try:
        response = xiansuoyunwei_post(url='/onLineUserManage/onLineUserList', postdata=listpara)
        responseDict=json.loads(response.text)
#         #print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "用户存在于在线列表中")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "用户不存在于在线列表中")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '出现异常')
            return False
        
'''
    @功能：通过用户手机号获取id信息
    @para:
    mobile:在线用户手机号
    @return：检查成功，返回ID信息;否则返回None
    @author:  chenhui 2016-4-7
'''  
def get_online_user_id_by_mobile(mobile):
    Log.LogOutput(LogLevel.INFO, "通过手机号获取在线用户列表id信息")
    userDict = copy.deepcopy(YwYongHuGuanLiPara.zaiXianYongHuGuanLiLieBiao)
    try:
        response = xiansuoyunwei_post(url='/onLineUserManage/onLineUserList', postdata=userDict)
        responseDict=json.loads(response.text)
        for item in responseDict['rows']:
            if item['userName'] == mobile:
                Log.LogOutput(LogLevel.DEBUG, "找到手机号对应的在线用户，返回ID")
                return item['id']
        else:
            Log.LogOutput(LogLevel.WARN, "无法找到对应的在线用户，返回None")
            return None
    except Exception:
        Log.LogOutput(LogLevel.WARN, '查找在线用户过程异常，返回None')
        return None
      
'''
    @功能：注销用户
    @para:
    userId:用户id信息
    @return：注销成功，返回True;否则返回False
    @author:  chenhui 2016-04-11
'''  
def logout_user(userId):
    Log.LogOutput(LogLevel.INFO, "开始注销用户......")
    userDict = {
                "ids[]":userId
                }
    response = xiansuoyunwei_post(url='/onLineUserManage/sessionLogout', postdata=userDict)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "注销成功")
        return True
    else:
        Log.LogOutput(LogLevel.DEBUG, "注销失败")
        return False