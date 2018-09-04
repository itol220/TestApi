# -*- coding:UTF-8 -*-
'''
Created on 2016-9-6
广场页UI操作，主要包括爆料和说说切换
@author: hongzenghui
'''
from Mobile import MobileUtil
from COMMON import Log
from CONFIG.Define import LogLevel

'''
    @功能：点击爆料tab
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2016-9-6
'''

def click_baoliao_tab():
    xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/btn_news']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击爆料tab成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击爆料tab失败")
        return False
    
    
'''
    @功能：点击说说tab
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2016-9-6
'''

def click_shuoshuo_tab():
    xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/btn_talk']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击说说tab成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击说说tab失败")
        return False