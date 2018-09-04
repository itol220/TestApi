# -*- coding:UTF-8 -*-
'''
Created on 2016-8-15

@author: N-254
'''
from Mobile import MobileUtil
from COMMON import Log, Time
from CONFIG.Define import LogLevel
from Mobile.UI.Clue import MainPageUI, PersonalUI, LoginUI


def clue_login(userInfo):  
    if MainPageUI.check_in_main_page() is True:
        Log.LogOutput(LogLevel.DEBUG, "当前已经登录并处于首页，无需登录")
        return True
    else: 
        #判断是否进入引导页
        xpath = "//android.support.v4.view.ViewPager[@resource-id='com.tianque.linkage:id/loading_viewpager']"
        if MobileUtil.wait_element_by_xpath(xpath) is True:
            Log.LogOutput(LogLevel.DEBUG, "进入引导页")
        else:
            Log.LogOutput(LogLevel.DEBUG, "未处于引导页") 
            return False
        Time.wait(1)
        #第一引导页翻页
        MobileUtil.swipe_left()
        Time.wait(1)
        #第二引导页翻页
        MobileUtil.swipe_left()
        Time.wait(1)
        #第三引导页翻页
        MobileUtil.swipe_left()
        Time.wait(1)
        #确认是否看到“我要爆料”按钮
        xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/start_app']"
        if MobileUtil.wait_element_by_xpath(xpath):
            Log.LogOutput(LogLevel.DEBUG, "翻页成功")
        else:
            Log.LogOutput(LogLevel.ERROR, "翻页失败")
            return False
        #点击进入首页
        MobileUtil.click_element_by_xpath(xpath)
        #判断是否进入首页
        if MainPageUI.check_in_main_page() is True:
            Log.LogOutput(LogLevel.DEBUG, "进入到首页")
            #然后点击一下爆料，取消引导提示框
            MainPageUI.click_add_clue_menu()
            #点击我的
            MainPageUI.click_personal_menu()
            #点击未登录
            PersonalUI.click_personal_nick()
            #输入用户名
            LoginUI.input_mobile_number(userInfo)
            #输入密码
            LoginUI.input_password(userInfo)
            #点击登录
            LoginUI.click_login_button()
            #点击首页
            MainPageUI.click_firstpage_menu()
            return True
        else:
            Log.LogOutput(LogLevel.WARN, "进入首页失败")
            return False

def return_main_page():
    #如果已经在主页了，就无需返回
    if MainPageUI.check_in_main_page() is True:
        return True
    #如果有返回按钮，则点击返回按钮
    xpath="//android.widget.ImageView[@resource-id='com.tianque.linkage:id/left_icon']"
    while (MobileUtil.wait_element_by_xpath(xpath,timeout=10)):
        Log.LogOutput(message='点击返回按钮')
        MobileUtil.click_element_by_xpath(xpath)
    #连续点击返回按钮后，若还不是在主页页面，则点击“主页按钮”
    if MainPageUI.check_in_main_page() is False:
        #点击首页按钮
        xpath2="//android.widget.TextView[@resource-id='com.tianque.linkage:id/tab_main']"
        MobileUtil.click_element_by_xpath(xpath2)
    if MainPageUI.check_in_main_page() is True:
        return True
    raise Exception('返回首页过程中出现异常')
    