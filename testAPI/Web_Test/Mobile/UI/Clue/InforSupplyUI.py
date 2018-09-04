# -*- coding:UTF-8 -*-
'''
Created on 2016-10-14
商品信息补充页面相关操作
@author: chenhui
'''
from Mobile import MobileUtil
from COMMON import Log
from CONFIG.Define import LogLevel

'''
    @功能：检查是否在信息补充页面
    @para: 
    @return: 处于主页，返回True；否则返回False
    @chenhui  2016-9-23
''' 
def check_in_infor_supply_page():
    xpath = "//android.widget.TextView[@text='信息补充' and @resource-id='com.tianque.linkage:id/action_bar_title']"
    if MobileUtil.wait_element_by_xpath(xpath,5) is True:
        Log.LogOutput(LogLevel.DEBUG, message="当前处于信息补充页面")
        return True
    else:
        Log.LogOutput(LogLevel.DEBUG, message="当前未处于信息补充页面")
        return False
    
'''
    @功能：点击信息补充页面的提交按钮
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ chenhui  2016-9-23
'''
def click_submit_button():
    xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/tv_submit']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击提交按钮成功")
        return True
    else:
        #防止错误截图，不采用ERROR，只采用DEBUG
        Log.LogOutput(LogLevel.DEBUG, message="点击提交按钮失败")
        return False
    
'''
    @功能：清空并输入姓名
    @para: 
    @return: 处于主页，返回True；否则返回False
    @chenhui  2016-9-23
''' 
def clear_and_input_name(PointObject):
    if PointObject['name'] is None:
        Log.LogOutput(LogLevel.ERROR, message="姓名参数传入错误")
        return False
    xpath =  "//android.widget.EditText[@resource-id='com.tianque.linkage:id/tv_name']"
    if MobileUtil.clear_and_input_element_by_xpath(xpath,PointObject['name'],20) is True:
        Log.LogOutput(LogLevel.DEBUG, message="清空并输入姓名成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="清空并输入姓名失败")
        return False
    
'''
    @功能：清空并输入身份证
    @para: 
    @return: 处于主页，返回True；否则返回False
    @chenhui  2016-9-23
''' 
def clear_and_input_idnum(PointObject):
    if PointObject['idNum'] is None:
        Log.LogOutput(LogLevel.ERROR, message="身份证号参数传入错误")
        return False
    xpath = "//android.widget.EditText[@resource-id='com.tianque.linkage:id/tv_idCard']"
    if MobileUtil.clear_and_input_element_by_xpath(xpath,PointObject['idNum'],10) is True:
        Log.LogOutput(LogLevel.DEBUG, message="清空并输入身份证成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="清空并输入身份证失败")
        return False