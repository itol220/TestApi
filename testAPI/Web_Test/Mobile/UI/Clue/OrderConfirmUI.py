# -*- coding:UTF-8 -*-
'''
Created on 2016-10-14
订单确认页面相关操作
@author: chenhui
'''
from Mobile import MobileUtil
from COMMON import Log
from CONFIG.Define import LogLevel

'''
    @功能：点击继续兑换按钮
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ chenhui  2016-9-23
'''
def click_exchange_record_button_in_confirm_page():
    xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/tv_check']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击兑换记录按钮成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击兑换记录按钮失败")
        return False
    
'''
    @功能：点击继续兑换按钮
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ chenhui  2016-9-23
'''
def click_continue_exchange_button():
    xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/tv_continue_to_exchange']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击提交按钮成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击提交按钮失败")
        return False
    
'''
    @功能：检查是否在订单确认页面
    @para: 
    @return: 处于主页，返回True；否则返回False
    @chenhui  2016-9-23
''' 
def check_in_order_confirm_page():
    xpath = "//android.widget.TextView[@text='订单确认' and @resource-id='com.tianque.linkage:id/action_bar_title']"
    if MobileUtil.wait_element_by_xpath(xpath,5) is True:
        Log.LogOutput(LogLevel.DEBUG, message="当前处于订单确认页面")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="当前未处于订单确认页面")
        return False
    
'''
    @功能：检查订单确认页面剩余积分值
    @para: PointObject['restPoint']
    @return: 处于主页，返回True；否则返回False
    @chenhui  2016-9-29
''' 
def check_rest_point_in_order_confirm_page(PointObject):
    xpath = "//android.widget.TextView[@text='%s' and @resource-id='com.tianque.linkage:id/tv_score']"%PointObject['restPoint']
    if MobileUtil.wait_element_by_xpath(xpath,5) is True:
        Log.LogOutput(LogLevel.DEBUG, message="订单确认页面所剩积分验证正确")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="订单确认页面所剩积分验证错误")
        return False