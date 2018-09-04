# -*- coding:UTF-8 -*-
'''
Created on 2017-7-10

@author: Administrator
'''
import md5
from CONFIG import Global
import requests
from COMMON import Log
from CONFIG.Define import LogLevel
from COMMON.CommonUtil import httpResponseResultDeal

sidNumber = None
def tieluhulu_login(username=None, password=None):
    global sidNumber
    m1 = md5.new()
    if username is None or password is None: 
        m1.update(Global.TieLuHuLuInfo['TieLuHuLuPassword'])      
        postData = {"userName":Global.TieLuHuLuInfo['TieLuHuLuUsername'],"password":m1.hexdigest(),"passwordshow":Global.TieLuHuLuInfo['TieLuHuLuPassword']}
    else:
        m1.update(password)
        postData = {"userName":username, "password":m1.hexdigest(), "passwordshow":password}
    response = requests.post("%s/sessionManage/login.action" % Global.TieLuHuLuInfo['TieLuHuLuUrl'],data=postData)
    if response.text == "true":
        print "login success"
        setCookieInfo = response.headers['Set-Cookie']
        cookieDeal = setCookieInfo.split(';')
        sidNumber = cookieDeal[0]
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, "登录失败，请检查 登录参数信息")
        return False
    
def tieluhulu_get(url = None, param = None, headers=None, username=Global.PingAnJianSheUser, password = Global.PingAnJianShePass):
    global sidNumber
    if tieluhulu_login(username=username, password=password) is True:
        headersSend = {"Cookie":sidNumber}
        if headers is not None:
            headersSend.update(headers)
        response = requests.get("%s%s" % (Global.TieLuHuLuInfo['TieLuHuLuUrl'],url), params=param, headers=headersSend)
        return httpResponseResultDeal(response)
    else:
        raise AssertionError, "Login Failed"
    
def tieluhulu_post(url=None, postdata=None, headers=None, files=None, username=Global.PingAnJianSheUser, password = Global.PingAnJianShePass):
    global sidNumber
    if tieluhulu_login(username=username, password=password) is True:        
        headersSend = {"Cookie":sidNumber}
        if headers is not None:
            headersSend.update(headers)
        response = requests.post("%s%s" % (Global.TieLuHuLuInfo['TieLuHuLuUrl'],url),data=postdata,files=files,headers=headersSend)
        return httpResponseResultDeal(response)
    else:
        raise AssertionError, "Login Failed"
