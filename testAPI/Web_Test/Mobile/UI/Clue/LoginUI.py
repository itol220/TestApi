# -*- coding:UTF-8 -*-
'''
Created on 2016-8-18
登录页面
@author: N-254
'''
from Mobile import MobileUtil
from COMMON import Log
from CONFIG.Define import LogLevel

'''
    @功能：点击返回按钮
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2016-8-18
'''
def click_back_button():
    xpath = "//android.widget.ImageView[@resource-id='com.tianque.linkage:id/left_icon']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击返回按钮成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击返回按钮失败")
        return False

'''
    @功能：输入手机号
    @para: userInfo 用户信息对象，请引用MyRelateObjectDef中的userInfo字典
    @return: 输入成功，返回True；否则返回False
    @ hongzenghui  2016-8-18
'''
def input_mobile_number(userInfo):
    xpath = "//android.widget.EditText[@resource-id='com.tianque.linkage:id/login_account']"
    if MobileUtil.input_element_by_xpath(xpath,userInfo['mobilePhone']) is True:
        Log.LogOutput(LogLevel.DEBUG, message="输入手机号成功")
        return False
    else:
        Log.LogOutput(LogLevel.ERROR, message="输入手机号失败")
        return False
    
'''
    @功能：输入密码
    @para: userInfo 用户信息对象，请引用MyRelateObjectDef中的userInfo字典
    @return: 输入成功，返回True；否则返回False
    @ hongzenghui  2016-8-18
'''
def input_password(userInfo):
    xpath = "//android.widget.EditText[@resource-id='com.tianque.linkage:id/login_password']"
    if MobileUtil.input_element_by_xpath(xpath,userInfo['password']) is True:
        Log.LogOutput(LogLevel.DEBUG, message="输入密码成功")
        return False
    else:
        Log.LogOutput(LogLevel.ERROR, message="输入密码失败")
        return False
    
'''
    @功能：点击登录按钮
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2016-8-18
'''
def click_login_button():
    xpath = "//android.widget.Button[@resource-id='com.tianque.linkage:id/login_btn']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击登录按钮成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击登录按钮失败")
        return False
    
'''
    @功能：点击注册账号按钮
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2016-8-18
'''
def click_regist_button():
    xpath = "//android.widget.Button[@resource-id='com.tianque.linkage:id/registe_btn']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击注册账号按钮成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击注册账号按钮失败")
        return False
    
'''
    @功能：点击忘记密码按钮
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2016-8-18
'''
def click_forget_password_button():
    xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/login_reset_password']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击忘记密码按钮成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击忘记密码按钮失败")
        return False
    
'''
    @功能：检查是否在登录页面
    @para: 
    @return: 在登录页面，返回True；否则返回False
    @ hongzenghui  2016-8-18
'''
def check_whetherIn_loginPage():
    xpath = "//android.widget.Button[@resource-id='com.tianque.linkage:id/login_btn']"
    if MobileUtil.find_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="在注册页面")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="未在注册页面")
        return False