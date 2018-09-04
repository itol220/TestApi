# -*- coding:UTF-8 -*-
'''
Created on 2016-3-7

@author: N-286
'''
from __future__ import unicode_literals
from Web_Test.COMMON import Log
from Web_Test.CONFIG.Define import LogLevel
from Web_Test.CONFIG.InitDefaultPara import userInit
from Web_Test.Interface.PingAnTong.pingAnTongHttpCommon import pingantong_post, \
    pingantong_get
import json

'''
    @功能：手机新增事件
    @para:issueAddPara
    @return:    true/false
    @author:  chenhui 2016-1-27
'''  
def getCurrentLoginUser(para=None, username = userInit['DftJieDaoUser'], password = '11111111'):
    Log.LogOutput(level=LogLevel.INFO, message='获取当前登录用户信息')
    response = pingantong_get(url='/mobile/userMobileManage/getCurrentLoginUser.action', param=para, username=username, password=password)
#     Log.LogOutput(LogLevel.DEBUG,response.text)
    resDict=json.loads(response.text)
    return resDict