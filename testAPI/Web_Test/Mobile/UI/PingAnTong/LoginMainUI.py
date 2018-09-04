# -*- coding:UTF-8 -*-
'''
Created on 2016-1-12
登录界面操作AW
@author: hongzenghui
'''
from Mobile import MobileUtil
from COMMON import Log
from CONFIG.Define import LogLevel

'''
    @功能：     输入账号
    @para: 
    username: 账号信息
    @return: 输入成功，返回True；否则返回False
    @ hongzenghui  2016-1-13
'''
def input_username(username=None):
    #清空用户名
    xpath = "//android.widget.ImageView[@resource-id='com.tianque.ecommunity.plugin.syssetting:id/all_delte']"
    MobileUtil.click_element_by_xpath(xpath)
    #输入用户名
    xpath = "//android.widget.EditText[@resource-id='com.tianque.ecommunity.plugin.syssetting:id/accounts']"
    if MobileUtil.input_element_by_xpath(xpath, username) is True:
        Log.LogOutput(LogLevel.DEBUG, message="输入用户名%s成功" % username)
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="输入用户名%s失败" % username)
        return False
    
'''
    @功能：     输入密码
    @para: 
    password: 账号信息
    @return: 输入成功，返回True；否则返回False
    @ hongzenghui  2016-1-13
'''
def input_password(password=None):
    xpath = "//android.widget.EditText[@resource-id='com.tianque.ecommunity.plugin.syssetting:id/password']"
    if MobileUtil.input_element_by_xpath(xpath, password) is True:
        Log.LogOutput(LogLevel.DEBUG, message="输入密码%s成功" % password)
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="输入密码%s失败" % password)
        return False
    
'''
    @功能：     点击登录按钮
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2016-1-13
'''
def click_login_button():
    xpath = "//android.widget.Button[@resource-id='com.tianque.ecommunity.plugin.syssetting:id/sign_in_button']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击登录按钮成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击登录按钮失败")
        return False
