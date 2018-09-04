# -*- coding:UTF-8 -*-
'''
Created on 2016-8-18
注册界面
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
def input_mobile_phone(userInfo):
    xpath = "//android.widget.EditText[@resource-id='com.tianque.linkage:id/registe_number']"
    if MobileUtil.input_element_by_xpath(xpath,userInfo['mobilePhone']) is True:
        Log.LogOutput(LogLevel.DEBUG, message="输入手机号成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="输入手机号失败")
        return False

'''
    @功能：输入验证码
    @para: userInfo 用户信息对象，请引用MyRelateObjectDef中的userInfo字典
    @return: 输入成功，返回True；否则返回False
    @ hongzenghui  2016-8-18
'''
def input_verifyCode(userInfo):
    xpath = "//android.widget.EditText[@resource-id='com.tianque.linkage:id/registe_authcode']"
    if MobileUtil.input_element_by_xpath(xpath,userInfo['verifyCode']) is True:
        Log.LogOutput(LogLevel.DEBUG, message="输入验证码成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="输入验证码失败")
        return False
    
'''
    @功能：点击获取验证码
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2016-8-15
'''
def click_get_authCode_button():
    xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/count_down_button']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击获取验证码按钮成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击获取验证码按钮失败")
        return False
    
'''
    @功能：输入密码
    @para: userInfo 用户信息对象，请引用MyRelateObjectDef中的userInfo字典
    @return: 输入成功，返回True；否则返回False
    @ hongzenghui  2016-8-18
'''
def input_regist_password(userInfo):
    xpath = "//android.widget.EditText[@resource-id='com.tianque.linkage:id/registe_password']"
    if MobileUtil.input_element_by_xpath(xpath,userInfo['password']) is True:
        Log.LogOutput(LogLevel.DEBUG, message="输入注册密码成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="输入注册密码失败")
        return False
    
'''
    @功能：输入邀请码
    @para: userInfo 用户信息对象，请引用MyRelateObjectDef中的userInfo字典
    @return: 输入成功，返回True；否则返回False
    @ hongzenghui  2016-8-18
'''
def input_invite_code(userInfo):
    xpath = "//android.widget.EditText[@resource-id='com.tianque.linkage:id/registe_code']"
    if MobileUtil.input_element_by_xpath(xpath,userInfo['inviteCode']) is True:
        Log.LogOutput(LogLevel.DEBUG, message="输入邀请码成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="输入邀请码失败")
        return False

'''
    @功能：选择所属街道的市
    @para: userInfo 用户信息对象，请引用MyRelateObjectDef中的userInfo字典
    @return: 选择成功，返回True；否则返回False
    @ hongzenghui  2016-8-18
'''
def select_city(userInfo):
    xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/city']"
    if MobileUtil.click_element_by_xpath(xpath) is False:
        Log.LogOutput(LogLevel.DEBUG, message="点击所属市失败")
    xpath = "//android.widget.TextView[@text='%s']" % userInfo['cityName']
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="选择所属市成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="选择所属市失败")
        return False

'''
    @功能：选择所属街道的区
    @para: userInfo 用户信息对象，请引用MyRelateObjectDef中的userInfo字典
    @return: 选择成功，返回True；否则返回False
    @ hongzenghui  2016-8-18
'''
def select_distric(userInfo):
    xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/area']"
    if MobileUtil.click_element_by_xpath(xpath) is False:
        Log.LogOutput(LogLevel.DEBUG, message="点击所属区失败")
    xpath = "//android.widget.TextView[@text='%s']" % userInfo['districName']
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="选择所属区成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="选择所属区失败")
        return False
    
'''
    @功能：选择所属街道
    @para: userInfo 用户信息对象，请引用MyRelateObjectDef中的userInfo字典
    @return: 选择成功，返回True；否则返回False
    @ hongzenghui  2016-8-18
'''
def select_street(userInfo):
    xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/street']"
    if MobileUtil.click_element_by_xpath(xpath) is False:
        Log.LogOutput(LogLevel.DEBUG, message="点击所属街道失败")
    xpath = "//android.widget.TextView[@text='%s']" % userInfo['streetName']
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="选择所属街道成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="选择所属街道失败")
        return False

'''
    @功能：点击同意用户注册协议按钮
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2016-8-18
'''
def click_agree_regist_button():
    xpath = "//android.widget.CheckBox[@resource-id='com.tianque.linkage:id/registe_agree']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击同意注册协议成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击同意注册协议失败")
        return False
  
'''
    @功能：点击注册按钮
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2016-8-18
'''
def click_regist_button():
    xpath = "//android.widget.Button[@resource-id='com.tianque.linkage:id/registe']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击注册按钮成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击注册按钮失败")
        return False