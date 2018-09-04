# -*- coding:UTF-8 -*-
'''
Created on 2016-9-18
设置页面相关操作
@author: hongzenghui
'''
from Mobile import MobileUtil
from COMMON import Log
from CONFIG.Define import LogLevel

'''
    @功能：修改密码
    @para: userInfo:用户信息对象内容，请引用MyRelateObjectDef中的userInfo对象
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2016-9-18
'''
def modify_password(userInfo):
    xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/update_password']"
    if MobileUtil.click_element_by_xpath(xpath) is False:
        Log.LogOutput(LogLevel.ERROR, message="点击修改密码失败")
        return False
    xpath = "//android.widget.EditText[@resource-id='com.tianque.linkage:id/password1']"
    if MobileUtil.input_element_by_xpath(xpath, userInfo['newPassword']) is False:
        return False
    xpath = "//android.widget.EditText[@resource-id='com.tianque.linkage:id/password2']"
    if MobileUtil.input_element_by_xpath(xpath, userInfo['verifyPassword']) is False:
        return False
    xpath = "//android.widget.TextView[@text='确定']"
    if MobileUtil.click_element_by_xpath(xpath) is False:
        Log.LogOutput(LogLevel.ERROR, message="修改密码失败")
        return False
    Log.LogOutput(LogLevel.DEBUG, message="检查积分成功") 
    return True
    
'''
    @功能：点击退出按钮
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2016-9-18
'''
def click_exit_button():
    xpath = "//android.widget.Button[@resource-id='com.tianque.linkage:id/exit']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击退出成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击退出失败")
        return False