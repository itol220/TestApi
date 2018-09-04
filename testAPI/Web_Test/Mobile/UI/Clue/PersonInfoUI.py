# -*- coding:UTF-8 -*-
'''
Created on 2016-9-19
我的信息页面相关操作
@author: hongzenghui
'''
from Mobile import MobileUtil
from COMMON import Log, Time
from CONFIG.Define import LogLevel

'''
    @功能：点击返回按钮
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2016-9-19
'''
def click_back_button():
    xpath = "//android.widget.ImageView[@resource-id='com.tianque.linkage:id/left_icon']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击返回按钮成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击返回按钮失败")
        return False

'''
    @功能：更改头像
    @para: 
    @return: 更改成功，返回True；否则返回False
    @ hongzenghui  2016-9-19
'''
def modify_head_picture():
    #点击头像按钮
    xpath = "//android.widget.ImageView[@resource-id='com.tianque.linkage:id/user_head']"
    if MobileUtil.click_element_by_xpath(xpath) is False:
        return False
    Time.wait(2)
    #头像只能修改，不能清除，先选择第二张图片
    xpath = "//android.widget.ImageView[@resource-id='com.tianque.linkage:id/iv']"
    elements = MobileUtil.find_elements_by_xpath(xpath)
    elements[2].click()
    #点击完成按钮
    xpath = "//android.widget.TextView[@text='完成']"
    if MobileUtil.click_element_by_xpath(xpath) is False:
        return False
    #再点击头像
    xpath = "//android.widget.ImageView[@resource-id='com.tianque.linkage:id/user_head']"
    if MobileUtil.click_element_by_xpath(xpath) is False:
        return False
    Time.wait(2)
    #切换回第一张“湖”
    xpath = "//android.widget.ImageView[@resource-id='com.tianque.linkage:id/iv']"
    elements = MobileUtil.find_elements_by_xpath(xpath)
    elements[1].click()
    #点击完成按钮
    xpath = "//android.widget.TextView[@text='完成']"
    if MobileUtil.click_element_by_xpath(xpath) is False:
        return False
    Log.LogOutput(LogLevel.DEBUG, message="修改头像完成")
    return True
    
'''
    @功能：更改昵称
    @para: userInfo:用户信息对象内容，请引用MyRelateObjectDef中的userInfo对象
    @return: 更改成功，返回True；否则返回False
    @ hongzenghui  2016-9-19
'''
def modify_nick_name(userInfo):
    #点击昵称按钮
    xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/user_nick']"
    if MobileUtil.click_element_by_xpath(xpath) is False:
        Log.LogOutput(LogLevel.ERROR, message="修改昵称失败")
        return False
    xpath = "//android.widget.EditText[@resource-id='com.tianque.linkage:id/content']"
    if MobileUtil.clear_and_input_element_by_xpath(xpath, userInfo['nickName']) is False:
        Log.LogOutput(LogLevel.ERROR, message="修改昵称失败")
        return False
    xpath = "//android.widget.TextView[@text='保存']"
    if MobileUtil.click_element_by_xpath(xpath) is False:
        Log.LogOutput(LogLevel.ERROR, message="修改昵称失败")
        return False
    Log.LogOutput(LogLevel.DEBUG, message="修改昵称完成")
    return True

'''
    @功能：更改常住地址
    @para: userInfo:用户信息对象内容，请引用MyRelateObjectDef中的userInfo对象
    @return: 更改成功，返回True；否则返回False
    @ hongzenghui  2016-9-19
'''
def modify_address(userInfo):
    #点击常驻地址
    xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/user_address']"
    if MobileUtil.click_element_by_xpath(xpath) is False:
        Log.LogOutput(LogLevel.ERROR, message="修改常驻地址失败")
        return False
    xpath = "//android.widget.EditText[@resource-id='com.tianque.linkage:id/content']"
    if MobileUtil.clear_and_input_element_by_xpath(xpath, userInfo['address']) is False:
        Log.LogOutput(LogLevel.ERROR, message="修改常驻地址失败")
        return False
    xpath = "//android.widget.TextView[@text='保存']"
    if MobileUtil.click_element_by_xpath(xpath) is False:
        Log.LogOutput(LogLevel.ERROR, message="修改常驻地址失败")
        return False
    Log.LogOutput(LogLevel.DEBUG, message="修改常驻地址完成")
    return True

'''
    @功能：检查常住地址
    @para: userInfo:用户信息对象内容，请引用MyRelateObjectDef中的userInfo对象
    @return: 检查成功，返回True；否则返回False
    @ hongzenghui  2016-9-19
'''
def check_address(userInfo):
    xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/user_address' and @text='%s']" % userInfo['address']
    if MobileUtil.wait_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="检查常住地址成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="检查常住地址失败")
        return False