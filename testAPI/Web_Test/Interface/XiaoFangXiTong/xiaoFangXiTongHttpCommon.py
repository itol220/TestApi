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

sidNumber = None

def xiaofang_login(userName=None, passWord=None):
    global sidNumber
    if userName is None or passWord is None: 
        postData = {"userName":Global.XiaoFangInfo['ShengXiaoFangXiTongUser'],"password":Global.XiaoFangInfo['ShengXiaoFangXiTongPass']}
    else:
        postData = {"userName":userName, "password":passWord}
    response = requests.post("%s/sessionManage/login.action" % Global.XiaoFangInfo['ShengXiaoFangXiTongUrl'],data=postData)
    if response.text == "true":
#         Log.LogOutput(LogLevel.DEBUG, u"正常登录")
        setCookieInfo = response.headers['Set-Cookie']
        sidInfo = setCookieInfo.split(';')
        sidNumber = sidInfo[0]
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, "登录失败，请检查 登录参数信息")
#         raise AssertionError, "Login Failed"
        return False
    
def xiaofang_get(url = None, param = None, headers=None, username=Global.XiaoFangInfo['ShengXiaoFangXiTongUser'], password = Global.XiaoFangInfo['ShengXiaoFangXiTongPass']):
    global sidNumber
    if xiaofang_login(userName=username, passWord=password) is True:
        headersSend = {"Cookie":"%s" % sidNumber}
        if headers is not None:
            headersSend.update(headers)
        response = requests.get("%s%s" % (Global.XiaoFangInfo['ShengXiaoFangXiTongUrl'],url), params=param, headers=headersSend)
        return httpResponseResultDeal(response)
    else:
        raise AssertionError, "Login Failed"
    
def xiaofang_post(url=None, postdata=None, headers=None, files=None, username=Global.XiaoFangInfo['ShengXiaoFangXiTongUser'], password = Global.XiaoFangInfo['ShengXiaoFangXiTongPass']):
    global sidNumber
    if xiaofang_login(userName=username, passWord=password) is True:        
        headersSend = {"Cookie":"%s" % sidNumber}
        if headers is not None:
            headersSend.update(headers)
        response = requests.post("%s%s" % (Global.XiaoFangInfo['ShengXiaoFangXiTongUrl'],url),data=postdata,files=files,headers=headersSend)
        return httpResponseResultDeal(response)
    else:
        raise AssertionError, "Login Failed"
