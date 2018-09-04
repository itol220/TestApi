# -*- coding:UTF-8 -*-
'''
Created on 2016-1-14

@author: N-254
'''
from Mobile import MobileUtil
from COMMON import Log
from CONFIG.Define import LogLevel
'''
    @功能：     跳过手势设置
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2016-1-13
'''
def skip_setting():
    xpath = "//android.widget.TextView[@resource-id='com.tianque.ecommunity.plugin.syssetting:id/right_text']"
    if MobileUtil.click_element_by_xpath(xpath,timeout=10) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击跳过设置按钮成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击跳过设置按钮失败")
        return False