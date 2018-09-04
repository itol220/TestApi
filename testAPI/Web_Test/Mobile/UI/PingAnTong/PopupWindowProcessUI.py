# -*- coding:UTF-8 -*-
'''
Created on 2017-9-30
弹出框处理
@author: N-254
'''
from Mobile.Define.PingAnTong.CommonModuePara import PopupProcessType
from Mobile import MobileUtil
from COMMON import Log
from CONFIG.Define import LogLevel

'''
    @功能：     弹出框处理
    @para:  promptMessage:提示信息
            processType: 选择是或者否，请传入CommonModuePara.PopupProcessType.OK 或者CommonModuePara.PopupProcessType.NO
    @return: 处理成功，返回True；否则返回False
    @ hongzenghui  2017-9-30
'''

def popup_window_process(promptMessage=None,processType=PopupProcessType.OK):
    if promptMessage is not None:
        xpath = "//android.widget.TextView[contains(@text,'%s')]" % promptMessage
        if MobileUtil.find_element_by_xpath(xpath) is not None:
            Log.LogOutput(LogLevel.DEBUG, message="检测提示信息成功")
        else:
            Log.LogOutput(LogLevel.ERROR, message="检测提示信息失败")
            return False
    #事件新增后的办理提示框
    if processType == PopupProcessType.OK:
        xpath = "//android.widget.TextView[@resource-id='com.tianque.ecommunity.plugin.issue:id/ok']"
        if MobileUtil.click_element_by_xpath(xpath):
            Log.LogOutput(LogLevel.DEBUG, message="点击确定成功")
            return True
        else:
            Log.LogOutput(LogLevel.ERROR, message="点击确定失败")
            return False
    #事件新增后的办理提示框
    elif processType == PopupProcessType.NO:
        xpath = "//android.widget.TextView[@resource-id='com.tianque.ecommunity.plugin.issue:id/no']"
        if MobileUtil.click_element_by_xpath(xpath):
            Log.LogOutput(LogLevel.DEBUG, message="点击取消成功")
            return True
        else:
            Log.LogOutput(LogLevel.ERROR, message="点击取消失败")
            return False
    #事件受理按钮点击后的提示框
    elif processType == PopupProcessType.ACCEPT:
        xpath = "//android.widget.TextView[@resource-id='com.tianque.ecommunity.plugin.issue:id/accept_and_hear_case']"
        if MobileUtil.click_element_by_xpath(xpath):
            Log.LogOutput(LogLevel.DEBUG, message="点击受理成功")
            return True
        else:
            Log.LogOutput(LogLevel.ERROR, message="点击受理失败")
            return False
    #事件受理按钮点击后的提示框
    elif processType == PopupProcessType.ACCEPTANDPROCESS:
        xpath = "//android.widget.TextView[@resource-id='com.tianque.ecommunity.plugin.issue:id/accept_and_hear_case_and_transaction']"
        if MobileUtil.click_element_by_xpath(xpath):
            Log.LogOutput(LogLevel.DEBUG, message="点击受理并办理成功")
            return True
        else:
            Log.LogOutput(LogLevel.ERROR, message="点击受理并办理失败")
            return False
    #事件受理按钮点击后的提示框
    elif processType == PopupProcessType.CANCEL:
        xpath = "//android.widget.TextView[@resource-id='com.tianque.ecommunity.plugin.issue:id/cancel']"
        if MobileUtil.click_element_by_xpath(xpath):
            Log.LogOutput(LogLevel.DEBUG, message="点击取消成功")
            return True
        else:
            Log.LogOutput(LogLevel.ERROR, message="点击取消失败")
            return False