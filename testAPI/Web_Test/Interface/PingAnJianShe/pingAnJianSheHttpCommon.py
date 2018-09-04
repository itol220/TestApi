# -*- coding:UTF-8 -*-
'''
Created on 2015-10-21

@author: N-254
'''
import requests
from CONFIG import Global
from COMMON import Log
from CONFIG.Define import LogLevel
from COMMON.CommonUtil import httpResponseResultDeal
import json

sidNumber = None

def pinganjianshe_login(userName=None, passWord=None):
    global sidNumber
    if userName is None or passWord is None: 
        postData = {"userName":Global.PingAnJianSheUser,"password":Global.PingAnJianShePass}
    else:
        postData = {"userName":userName, "password":passWord}
    response = requests.post("%s/sessionManage/login.action" % Global.PingAnJianSheUrl,data=postData)
#     responseObject = httpResponseResultDeal(response)
    if response.text == "true":
#         Log.LogOutput(LogLevel.DEBUG, u"正常登录")
        setCookieInfo = response.headers['Set-Cookie']
        cookieDeal = setCookieInfo.split(',')
        for coolieItem in cookieDeal:
            sidInfo = coolieItem.split(';')
            if 'sid' in sidInfo[0]:
                sidNumber = sidInfo[0]
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, "登录失败，请检查 登录参数信息")
#         raise AssertionError, "Login Failed"
        return False
    
def renzhengzhongxin_login(userName=None, passWord=None):
    global sidNumber
    if userName is None or passWord is None: 
        postData = {"userName":Global.PingAnJianSheUser,"password":Global.PingAnJianShePass}
    else:
        postData = {"userName":userName, "password":passWord}
    response = requests.post("%s/sysadmin/loginManage/login" % Global.RenZhengZhongXinUrl,data=postData)
#     print response.text
    responseObject = httpResponseResultDeal(response)
    if responseObject.result is True:
        responseDict = json.loads(responseObject.text)  
        if responseDict['login_stat'] == "loginSuccess":
            Log.LogOutput(LogLevel.DEBUG, u"正常登录")
            sidNumber = responseDict['newSession']['sessionId']
#             print "sidNumber:%s" % sidNumber
            return True
        else:
            Log.LogOutput(LogLevel.ERROR, "登录失败，请检查 登录参数信息")
            return False
    else:
        Log.LogOutput(LogLevel.ERROR, "登录失败，请检查 登录参数信息")
        return False
    
def pinganjianshe_get(url = None, param = None, headers=None, username=Global.PingAnJianSheUser, password = Global.PingAnJianShePass):
    global sidNumber
    if pinganjianshe_login(userName=username, passWord=password) is True:
        headersSend = {"Cookie":sidNumber}
        if headers is not None:
            headersSend.update(headers)
        response = requests.get("%s%s" % (Global.PingAnJianSheUrl,url), params=param, headers=headersSend)
        return httpResponseResultDeal(response)
    else:
        raise AssertionError, "Login Failed"
    
def pinganjianshe_post(url=None, postdata=None, headers=None, files=None, username=Global.PingAnJianSheUser, password = Global.PingAnJianShePass):
    global sidNumber
    if pinganjianshe_login(userName=username, passWord=password) is True:        
        headersSend = {"Cookie":sidNumber}
        if headers is not None:
            headersSend.update(headers)
        response = requests.post("%s%s" % (Global.PingAnJianSheUrl,url),data=postdata,files=files,headers=headersSend)
        return httpResponseResultDeal(response)
    else:
        raise AssertionError, "Login Failed"
def renzhengzhongxin_get(url = None, param = None, headers=None, username=Global.PingAnJianSheUser, password = Global.PingAnJianShePass):
    global sidNumber
    if renzhengzhongxin_login(userName=username, passWord=password) is True:
        headersSend = {"Cookie":"sid=%s" % sidNumber}
        if headers is not None:
            headersSend.update(headers)
        response = requests.get("%s%s" % (Global.RenZhengZhongXinUrl,url), params=param, headers=headersSend)
        return httpResponseResultDeal(response)
    else:
        raise AssertionError, "Login Failed"
    
def renzhengzhongxin_post(url=None, postdata=None, headers=None, files=None, username=Global.PingAnJianSheUser, password = Global.PingAnJianShePass):
    global sidNumber
    if renzhengzhongxin_login(userName=username, passWord=password) is True:        
        headersSend = {"Cookie":"sid=%s" % sidNumber}
        if headers is not None:
            headersSend.update(headers)
        response = requests.post("%s%s" % (Global.RenZhengZhongXinUrl,url),data=postdata,files=files,headers=headersSend)
        return httpResponseResultDeal(response)
    else:
        raise AssertionError, "Login Failed"
        
    
