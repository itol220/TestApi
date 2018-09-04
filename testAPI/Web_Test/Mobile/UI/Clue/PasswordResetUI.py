# -*- coding:UTF-8 -*-
'''
Created on 2016-8-18
密码重置页面
@author: hongzenghui
'''
from Mobile import MobileUtil
from COMMON import Log
from CONFIG.Define import LogLevel

'''
    @功能：输入手机号
    @para: userInfo 用户信息对象，请引用MyRelateObjectDef中的userInfo字典
    @return: 输入成功，返回True；否则返回False
    @ hongzenghui  2016-8-18
'''
def input_mobile_number(userInfo):
    xpath = "//android.widget.EditText[@resource-id='com.tianque.linkage:id/phone_number']"
    if MobileUtil.input_element_by_xpath(xpath,userInfo['mobilePhone']) is True:
        Log.LogOutput(LogLevel.DEBUG, message="输入手机号成功")
        return False
    else:
        Log.LogOutput(LogLevel.ERROR, message="输入手机号失败")
        return False
    
'''
    @功能：输入验证码
    @para: userInfo 用户信息对象，请引用MyRelateObjectDef中的userInfo字典
    @return: 输入成功，返回True；否则返回False
    @ hongzenghui  2016-8-18
'''
def input_verify_code(userInfo):
    xpath = "//android.widget.EditText[@resource-id='com.tianque.linkage:id/msm_authcode']"
    if MobileUtil.input_element_by_xpath(xpath,userInfo['verifyCode']) is True:
        Log.LogOutput(LogLevel.DEBUG, message="输入验证码成功")
        return False
    else:
        Log.LogOutput(LogLevel.ERROR, message="输入验证码失败")
        return False
    
'''
    @功能：点击获取验证码
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2016-8-15
'''
def click_get_verifyCode_button():
    xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/count_down_button']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击获取验证码按钮成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击获取验证码按钮失败")
        return False
    
'''
    @功能：输入新密码
    @para: userInfo 用户信息对象，请引用MyRelateObjectDef中的userInfo字典
    @return: 输入成功，返回True；否则返回False
    @ hongzenghui  2016-8-18
'''
def input_new_password(userInfo):
    xpath = "//android.widget.EditText[@resource-id='com.tianque.linkage:id/password1']"
    if MobileUtil.input_element_by_xpath(xpath,userInfo['newPassword']) is True:
        Log.LogOutput(LogLevel.DEBUG, message="输入新密码成功")
        return False
    else:
        Log.LogOutput(LogLevel.ERROR, message="输入新密码失败")
        return False
    
'''
    @功能：输入确认密码
    @para: userInfo 用户信息对象，请引用MyRelateObjectDef中的userInfo字典
    @return: 输入成功，返回True；否则返回False
    @ hongzenghui  2016-8-18
'''
def input_verify_password(userInfo):
    xpath = "//android.widget.EditText[@resource-id='com.tianque.linkage:id/password2']"
    if MobileUtil.input_element_by_xpath(xpath,userInfo['verifyPassword']) is True:
        Log.LogOutput(LogLevel.DEBUG, message="输入确认密码成功")
        return False
    else:
        Log.LogOutput(LogLevel.ERROR, message="输入确认密码失败")
        return False
    
'''
    @功能：点击确定按钮
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2016-8-15
'''
def click_commit_button():
    xpath = "//android.widget.Button[@resource-id='com.tianque.linkage:id/commit']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击确定按钮成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击确定按钮失败")
        return False