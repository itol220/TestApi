# -*- coding:UTF-8 -*-
'''
Created on 2016-1-27

@author: hongzenghui
'''
from __future__ import unicode_literals
import requests
from CONFIG import Global
from COMMON import Log
from CONFIG.Define import LogLevel
from COMMON.CommonUtil import httpResponseResultDeal
import base64
import md5
import json

sidNumber = None

def xiansuoyunwei_login(username=None, password=None):
    global sidNumber
    m1 = md5.new()
    if username is None or password is None: 
        m1.update(Global.XianSuoYunWeiInfo['XianSuoYunWeiPassword'])      
        postData = {"userName":Global.XianSuoYunWeiInfo['XianSuoYunWeiUsername'],"password":m1.hexdigest(),"submit":""}
    else:
        m1.update(password)
        postData = {"userName":username, "password":m1.hexdigest(), "submit":""}
    response = requests.post("%s/adminLogin/doLogin" % Global.XianSuoYunWeiInfo['XianSuoYunWeiUrl'],data=postData)
#     responseObject = httpResponseResultDeal(response)
    try:
        jsonData = json.loads(response.text)
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "登录失败，请检查 登录参数信息")
        return False

    if jsonData.has_key('login_error') is False:
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

def xiansuoyunwei_post(url=None, postdata=None, headers=None, files=None, username=Global.XianSuoYunWeiInfo['XianSuoYunWeiUsername'], password = Global.XianSuoYunWeiInfo['XianSuoYunWeiPassword']):
    global sidNumber
    if xiansuoyunwei_login(username=username, password=password) is True:        
        headersSend = {"Cookie":sidNumber}
        if headers is not None:
            headersSend.update(headers)
        response = requests.post("%s%s" % (Global.XianSuoYunWeiInfo['XianSuoYunWeiUrl'],url),data=postdata,files=files,headers=headersSend)
        return httpResponseResultDeal(response)
    else:
        raise AssertionError, "Login Failed"
    
def xiansuoyunwei_get(url = None, param = None, headers=None, username=Global.XianSuoYunWeiInfo['XianSuoYunWeiUsername'], password = Global.XianSuoYunWeiInfo['XianSuoYunWeiPassword']):
    global sidNumber
    if xiansuoyunwei_login(username=username, password=password) is True:
        headersSend = {"Cookie":sidNumber}
        if headers is not None:
            headersSend.update(headers)
        response = requests.get("%s%s" % (Global.XianSuoYunWeiInfo['XianSuoYunWeiUrl'],url), params=param, headers=headersSend)
        return httpResponseResultDeal(response)
    else:
        raise AssertionError, "Login Failed"