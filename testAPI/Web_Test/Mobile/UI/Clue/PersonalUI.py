# -*- coding:UTF-8 -*-
'''
Created on 2016-9-18
我的页面相关操作
@author: hongzenghui
'''
from COMMON import Log, Time
from CONFIG.Define import LogLevel
from Mobile import MobileUtil
from Mobile.UI.Clue import MainPageUI, LoginUI
import time

'''
    @功能：点击设置按钮
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2016-9-18
'''
def click_setting_button():
    xpath = "//android.widget.LinearLayout[@resource-id='com.tianque.linkage:id/rl_right']/android.widget.LinearLayout/android.widget.ImageView"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击设置按钮成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击设置按钮失败")
        return False
    
'''
    @功能：点击个人昵称
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2016-9-18
'''
def click_personal_nick():
    xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/user_nick']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击昵称成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击昵称失败")
        return False
    
'''
    @功能：检查昵称
    @para: userInfo:用户信息对象内容，请引用MyRelateObjectDef中的userInfo对象
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2016-9-18
'''
def check_nick_name(userInfo):
    xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/user_nick' and @text='%s']" % userInfo['nickName']
    if MobileUtil.wait_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="检查昵称成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="检查昵称失败")
        return False
    
'''
    @功能：检查积分
    @para: userInfo:用户信息对象内容，请引用MyRelateObjectDef中的userInfo对象
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2016-9-18
'''
def check_point(userInfo):
    xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/user_score' and @text='%s']" % userInfo['point']
    if MobileUtil.wait_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="检查积分成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="检查积分失败")
        return False
    
'''
    @功能：点击排行榜
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2016-9-18
'''
def click_ranking_list():
    xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/module_rank']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击排行榜按钮成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击排行榜按钮失败")
        return False
    
'''
    @功能：点击积分商城
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2016-9-18
'''
def click_point_mall():
    xpath = "//android.widget.RelativeLayout[@resource-id='com.tianque.linkage:id/score_mall']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击积分商城按钮成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击积分商城按钮失败")
        return False
    
'''
    @功能：点击我的爆料
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2016-9-18
'''
def click_clue_of_my():
    xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/my_module_clue']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击我的爆料成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击我的爆料失败")
        return False
    
'''
    @功能：点击我的说说
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2016-9-18
'''
def click_shuoshuo_of_my():
    xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/my_module_topic']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击我的说说成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击我的说说失败")
        return False
    
'''
    @功能：点击我的评论
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2016-9-18
'''
def click_comment_of_my():
    xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/my_module_comment']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击我的评论成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击我的评论失败")
        return False
    
'''
    @功能：点击我的关注
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2016-9-18
'''
def click_focus_of_my():
    xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/my_module_attention']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击我的评论成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击我的评论失败")
        return False
    
'''
    @功能：检查是否位于“我的”页面
    @para: MyRelateObjectDef对象参数
    @return: 点击成功，返回True；否则返回False
    @ chenhui  2016-9-29
'''
def check_in_personal_page():
    xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/action_bar_title' and @text='我的']"
    if MobileUtil.wait_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="位于“我的”页面")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="不在“我的”页面")
        return False

'''
    @功能：检查是否位于“我的”页面
    @para: MyRelateObjectDef对象参数
    @return: 点击成功，返回True；否则返回False
    @ chenhui  2016-9-29
'''
def check_is_login():
    xpath1 = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/user_nick' and @text='未登录']"
    if MobileUtil.wait_element_by_xpath(xpath1,timeout=10) is True:
        Log.LogOutput(LogLevel.DEBUG, message="目前处于未登录状态")
        return False
    #如果排行榜有“排行”两个字，代表是登录状态
    xpath2="//android.widget.TextView[@resource-id='com.tianque.linkage:id/user_rank_layout' and @text='排行']"
    if MobileUtil.wait_element_by_xpath(xpath2,timeout=10) is True:
        Log.LogOutput(LogLevel.DEBUG, message="目前处于登录状态")
        return True    
    raise Exception('检测登录状态过程出现异常')

'''
    @功能：未登录状态时，先登录
    @para: MyRelateObjectDef对象参数
    @return: 点击成功，返回True；否则返回False
    @ chenhui  2016-9-29
'''
def relogin(userInfo):
    #首先判断是否位于我的页面
    if  check_in_personal_page() is False:
        return False
    #是否处于未登录状态
    if check_is_login() is False:
        #进入登录界面
        click_personal_nick()
        #输入用户名
        LoginUI.input_mobile_number(userInfo)
        #输入密码
        LoginUI.input_password(userInfo)
        #点击登录
        LoginUI.click_login_button()
        #先刷新页面
        refresh_page_of_mine()
        #判断是否登录成功
        if check_is_login() is True:
            Log.LogOutput(message='重新登录成功')
            return True
        else:
            Log.LogOutput(message='重新登录失败')
            return False
    return True

'''
    @功能：刷新我的页面,通过点击首页与点击我的两个按钮，切换两个页面来实现刷新功能
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ chenhui  2016-9-29
'''
def refresh_page_of_mine():
    time.sleep(5)
    if MainPageUI.click_firstpage_menu() is False:
        return False
    if MainPageUI.click_personal_menu() is False:
        return False
    Log.LogOutput(message='我的页面刷新成功')
    return True
