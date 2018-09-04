# -*- coding:UTF-8 -*-
'''
Created on 2015-10-5

@author: ho
'''
from __future__ import unicode_literals
from Web_Test.CONFIG.Define import LogLevel
import time
from Web_Test.CONFIG import Global
from Web_Test.Mobile import MobileUtil

def LogOutput(level=LogLevel.INFO, message=""):
    currentTime = time.strftime('%Y-%m-%d %H:%M:%S')
    if(level == LogLevel.INFO):
        print (u"[%s][INFO][%s]" % (currentTime,message))
    elif(level == LogLevel.DEBUG):
        print (u"[%s][DEBUG][%s]" % (currentTime,message))
    elif(level == LogLevel.ERROR):
        print (u"[%s][ERROR][%s]" % (currentTime,message))
        if Global.driver is not None:
            MobileUtil.screen_shot()
    elif(level == LogLevel.WARN):
        print (u"[%s][WARN][%s]" % (currentTime,message))
    else:
        print ("log level set error!")
        