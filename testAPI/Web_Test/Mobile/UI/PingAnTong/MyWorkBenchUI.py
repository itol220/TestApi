# -*- coding:UTF-8 -*-
'''
Created on 2016-1-15

@author: N-254
'''
from Mobile import MobileUtil
from CONFIG.Define import LogLevel
from COMMON import Log

'''
    @功能：     进入事件处理模块
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2017-9-28
'''

def enter_to_issue():
    xpath = "//android.widget.TextView[@text='事件处理']"
    if MobileUtil.click_element_by_xpath(xpath,30) is not None:
        Log.LogOutput(LogLevel.DEBUG, message="进入事件处理成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="进入事件处理失败")
        return False
    
'''
    @功能：     进入实有人口模块下的实有人口
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2017-9-28
'''

def enter_to_population():
    xpath = "//android.widget.TextView[@text='实有人口']"
    #点击实有人口图标
    MobileUtil.click_element_by_xpath(xpath,30)
    #进入实有人口子菜单
    xpath = "//android.widget.TextView[@text='实有人口']"
    if MobileUtil.click_element_by_xpath(xpath,30) is not None:
        Log.LogOutput(LogLevel.DEBUG, message="进入实有人口成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="进入实有人口失败")
        return False
    
'''
    @功能：     进入实有人口模块下的重点人员
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2017-9-28
'''

def enter_to_key_personal():
    xpath = "//android.widget.TextView[@text='实有人口']"
    #点击实有人口图标
    MobileUtil.click_element_by_xpath(xpath,30)
    #进入实有人口子菜单
    xpath = "//android.widget.TextView[@text='重点人员']"
    if MobileUtil.click_element_by_xpath(xpath,30) is not None:
        Log.LogOutput(LogLevel.DEBUG, message="进入重点人员成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="进入重点人员成功")
        return False
    
'''
    @功能：     进入实有人口模块下的关怀对象
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2017-9-28
'''

def enter_to_caring_personal():
    xpath = "//android.widget.TextView[@text='实有人口']"
    #点击实有人口图标
    MobileUtil.click_element_by_xpath(xpath,30)
    #进入实有人口子菜单
    xpath = "//android.widget.TextView[@text='关怀对象']"
    if MobileUtil.click_element_by_xpath(xpath,30) is not None:
        Log.LogOutput(LogLevel.DEBUG, message="进入关怀对象成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="进入关怀对象功")
        return False
    
'''
    @功能：     进入实有房屋模块
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2017-9-28
'''

def enter_to_real_houses():
    xpath = "//android.widget.TextView[@text='实有房屋']"
    #点击实有房屋图标
    if MobileUtil.click_element_by_xpath(xpath,30) is not None:
        Log.LogOutput(LogLevel.DEBUG, message="进入实有房屋成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="进入实有房屋失败")
        return False
    
'''
    @功能：     进入组织场所模块下的重点场所
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2017-9-28
'''

def enter_to_key_place():
    xpath = "//android.widget.TextView[@text='组织场所']"
    #点击组织场所图标
    MobileUtil.click_element_by_xpath(xpath,30)
    #进入重点场所子菜单
    xpath = "//android.widget.TextView[@text='重点场所']"
    if MobileUtil.click_element_by_xpath(xpath,30) is not None:
        Log.LogOutput(LogLevel.DEBUG, message="进入重点场所成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="进入重点场所失败")
        return False
    
'''
    @功能：     进入组织场所模块下的两新组织
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2017-9-28
'''

def enter_to_liangxin_org():
    xpath = "//android.widget.TextView[@text='组织场所']"
    #点击组织场所图标
    MobileUtil.click_element_by_xpath(xpath,30)
    #进入两新组织子菜单
    xpath = "//android.widget.TextView[@text='两新组织']"
    if MobileUtil.click_element_by_xpath(xpath,30) is not None:
        Log.LogOutput(LogLevel.DEBUG, message="进入两新组织成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="进入两新组织失败")
        return False
    
'''
    @功能：     进入组织场所模块下的企业
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2017-9-28
'''

def enter_to_enterprise():
    xpath = "//android.widget.TextView[@text='组织场所']"
    #点击组织场所图标
    MobileUtil.click_element_by_xpath(xpath,30)
    #进入企业子菜单
    xpath = "//android.widget.TextView[@text='企业]"
    if MobileUtil.click_element_by_xpath(xpath,30) is not None:
        Log.LogOutput(LogLevel.DEBUG, message="进入企业成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="进入企业失败")
        return False
    
'''
    @功能：     检查是否进入主页界面
    @para: 
    @return: 处于主页界面，返回True；否则返回False
    @ hongzenghui  2016-1-26
'''

def check_in_workbench():
    xpath = "//android.widget.TextView[@text='我的工作台']"
    if MobileUtil.find_element_by_xpath(xpath,30) is not None:
        Log.LogOutput(LogLevel.DEBUG, message="当前处于我的工作台界面")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="当前不处于我的工作台界面")
        return False
