# -*- coding:UTF-8 -*-
'''
Created on 2016-1-27

@author: hongzenghui
'''
import requests
from Web_Test.CONFIG import Global
from Web_Test.COMMON import Log
from Web_Test.CONFIG.Define import LogLevel
from Web_Test.COMMON.CommonUtil import httpResponseResultDeal

sidNumber = None

def pingantong_login(userName=None, passWord=None):
    global sidNumber
    if userName is None or passWord is None: 
        postData = {"userName":Global.PingAnJianSheUser,"password":Global.PingAnJianShePass,"tqmobile":"true"}
    else:
        postData = {"userName":userName, "password":passWord, "tqmobile":"true"}
    response = requests.post("%s/mobile/sessionManageMobileManage/login.action" % Global.ShouJiDaiLiUrl,data=postData)
#     responseObject = httpResponseResultDeal(response)
    if response.text == "true":
        Log.LogOutput(LogLevel.DEBUG, u"正常登录")
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
    
    
def pingantong_get(url = None, param = None, headers=None, username=Global.PingAnJianSheUser, password = Global.PingAnJianShePass):
    global sidNumber
    if pingantong_login(userName=username, passWord=password) is True:
        headersSend = {"Cookie":sidNumber}
        if headers is not None:
            headersSend.update(headers)
        response = requests.get("%s%s" % (Global.ShouJiDaiLiUrl,url), params=param, headers=headersSend)
        return httpResponseResultDeal(response)
    else:
        raise AssertionError ("Login Failed")
    
def pingantong_post(url=None, postdata=None, headers=None, files=None, username=Global.PingAnJianSheUser, password = Global.PingAnJianShePass):
    global sidNumber
    if pingantong_login(userName=username, passWord=password) is True:        
        headersSend = {"Cookie":sidNumber}
        if headers is not None:
            headersSend.update(headers)
        response = requests.post("%s%s" % (Global.ShouJiDaiLiUrl,url),data=postdata,files=files,headers=headersSend)
        return httpResponseResultDeal(response)
    else:
        raise AssertionError ("Login Failed")
        
    
