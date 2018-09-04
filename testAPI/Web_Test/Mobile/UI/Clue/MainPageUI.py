# -*- coding:UTF-8 -*-
'''
Created on 2016-8-15

@author: N-254
'''
from Mobile import MobileUtil
from COMMON import Log
from CONFIG.Define import LogLevel
from Mobile.Define.Clue import OthersObjectDef
import copy

'''
    @功能：区域选择
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2016-8-15
'''
def area_select():
    xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/left_text']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="区域选择点击成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="区域选择点击失败")
        return False
    
'''
    @功能：收件箱点击
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2016-8-15
'''
def click_unread_message():
    xpath = "//android.widget.LinearLayout[@resource-id='com.tianque.linkage:id/rl_right']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="未读消息点击成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="未读消息点击失败")
        return False
    
'''
    @功能：点击轮播信息
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2016-8-15
'''
def click_lunbo_info(text=None):
    xpath = "//android.widget.TextView[@text='%s']" % text
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击轮播内容成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击轮播内容失败")
        return False
    
'''
    @功能：点击爆料广场
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2016-8-15
''' 
def click_baoliao_square():
    xpath = "//android.widget.TextView[@text='爆料广场']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击爆料广场成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击爆料广场失败")
        return False
    
'''
    @功能：获取爆料统计
    @para: 
    @return: 返回爆料统计对象，包含今日新增数量，本周办结数量，全省本周办结数量
    @ hongzenghui  2016-8-15
''' 
def get_baoliao_count():
    xpath1 = "//android.widget.TextView[@text='今日新增']/following-sibling::android.widget.TextView[1]"
    xpath2 = "//android.widget.TextView[@text='本周办结']/following-sibling::android.widget.TextView[1]"
    xpath3 = "//android.widget.TextView[@text='全省本周办结']/following-sibling::android.widget.TextView[1]"
    baoliaoCountObject = copy.deepcopy(OthersObjectDef.baoliaoCount) 
    baoliaoCountObject['todayAdd'] = MobileUtil.find_element_by_xpath(xpath1).text
    baoliaoCountObject['weekComplete'] = MobileUtil.find_element_by_xpath(xpath2).text
    baoliaoCountObject['allProviceWeekComplete'] = MobileUtil.find_element_by_xpath(xpath3).text
    Log.LogOutput(LogLevel.DEBUG, message="今日新增统计:%s,本周办结统计:%s,全省本周办结统计:%s" % (baoliaoCountObject['todayAdd'],baoliaoCountObject['weekComplete'],baoliaoCountObject['allProviceWeekComplete']))
    return baoliaoCountObject

'''
    @功能：点击说说
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2016-8-15
''' 
def click_shuoshuo():
    xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/module_topic']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击说说成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击说说失败")
        return False
    
'''
    @功能：点击平安宣传
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2016-8-15
''' 
def click_safe_propaganda():
    xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/module_propaganda']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击平安宣传成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击平安宣传失败")
        return False
    
'''
    @功能：点击便民服务
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2016-8-15
''' 
def click_bianmin_service():
    xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/module_service']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击便民服务成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击便民服务失败")
        return False
    
'''
    @功能：点击我的爆料
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2016-8-15
''' 
def click_my_clue():
    xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/module_my_clue']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击我的爆料成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击我的爆料失败")
        return False
    
'''
    @功能：点击首页菜单
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2016-8-15
''' 
def click_firstpage_menu():
    xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/tab_main']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击首页菜单成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击首页菜单失败")
        return False
    
'''
    @功能：点击广场菜单
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2016-8-15
''' 
def click_square_menu():
    xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/tab_information']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击广场菜单成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击广场菜单失败")
        return False
    
'''
    @功能：点击爆料按钮
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2016-8-15
''' 
def click_add_clue_menu():
    xpath = "//android.widget.ImageView[@resource-id='com.tianque.linkage:id/edit_information']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击爆料按钮成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击爆料按钮失败")
        return False
    
'''
    @功能：点击公告菜单
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2016-8-15
''' 
def click_notice_menu():
    xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/tab_notice']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击公告菜单成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击公告菜单失败")
        return False
    
'''
    @功能：点击我的菜单
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2016-8-15
''' 
def click_personal_menu():
    xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/tab_personal']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击我的菜单成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击我的菜单失败")
        return False
    
'''
    @功能：检查是否在主页
    @para: 
    @return: 处于主页，返回True；否则返回False
    @ hongzenghui  2016-9-21
''' 
def check_in_main_page():
    xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/module_propaganda']"
    if MobileUtil.wait_element_by_xpath(xpath,20) is True:
        Log.LogOutput(LogLevel.DEBUG, message="当前处于主页")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="当前未处于主页")
        return False