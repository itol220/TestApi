# -*- coding:UTF-8 -*-
'''
Created on 2016-8-16
新增爆料页面相关操作
@author: hongzenghui
'''
from Mobile import MobileUtil
from COMMON import Log, Time
from CONFIG.Define import LogLevel

'''
    @功能：点击返回按钮
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2016-9-20
'''
def click_back_button():
    xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/left_text']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击返回按钮成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击返回按钮失败")
        return False
    

'''
    @功能：点击地址选择
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2016-8-15
'''
def click_location_select():
    #点击地址选择
    xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/choose_location']"
    if MobileUtil.click_element_by_xpath(xpath) is False:
        Log.LogOutput(LogLevel.DEBUG, message="点击地址选择失败")
        return False
    #判断是否定位成功
    xpath = "//android.widget.EditText[contains(@text,'西湖区')]"
    if MobileUtil.wait_element_by_xpath(xpath) is False:
        Log.LogOutput(LogLevel.DEBUG, message="定位失败")
    #点击提交按钮
    xpath = "//android.widget.Button[@resource-id='com.tianque.linkage:id/confirm']"
    if MobileUtil.click_element_by_xpath(xpath) is False:
        Log.LogOutput(LogLevel.DEBUG, message="点击提交按钮失败")
        return False
    Log.LogOutput(LogLevel.DEBUG, message="地址选择完成")
    return True
    
'''
    @功能：选择主题
    @para: clueObject 线索对象内容，请引用ClueRelateObjectDef中的clueObject对象
    @return: 选择成功，返回True；否则返回False
    @ hongzenghui  2016-9-6
'''
def select_subject(clueObject):
    xpath = "//android.widget.TextView[@text='%s' and @resource-id='com.tianque.linkage:id/theme_label']" % clueObject['subject']
    if MobileUtil.click_element_by_xpath(xpath) is False:
        Log.LogOutput(LogLevel.ERROR, message="选择主题失败")
        return False
    else:
        Log.LogOutput(LogLevel.DEBUG, message="选择主题成功")
        return True
    
'''
    @功能：爆料信息输入
    @para: clueObject 线索对象内容，请引用ClueRelateObjectDef中的clueObject对象
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2016-8-15
'''
def input_clue_content(clueObject):
    xpath = "//android.widget.EditText[@resource-id='com.tianque.linkage:id/content']"
    if MobileUtil.input_element_by_xpath(xpath, clueObject['description']) is True:
        Log.LogOutput(LogLevel.DEBUG, message="爆料信息输入成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="爆料信息输入失败")
        return False
    
'''
    @功能：图片选择
    @para: 线索对象内容，请引用ClueRelateObjectDef中的clueObject对象
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2016-8-15
'''
def add_clue_picture(clueObject):
    #无需添加图片
    if not clueObject['picture']['lakePic'] and not clueObject['picture']['schoolPic'] and \
        not clueObject['picture']['treePic'] and not clueObject['picture']['catPic'] and \
        not clueObject['picture']['penguinsPic'] and not clueObject['picture']['londonPic']:
        return True
    xpath = "//android.widget.ImageView[@resource-id='com.tianque.linkage:id/image_view']"
    if MobileUtil.click_element_by_xpath(xpath) is False:
        Log.LogOutput(LogLevel.DEBUG, message="添加图片按钮点击失败") 
    Time.wait(2)
    xpath = "//android.widget.ImageView[@resource-id='com.tianque.linkage:id/check']"
    elements = MobileUtil.find_elements_by_xpath(xpath) 
    if elements is None:
        return False
    if clueObject['picture']['lakePic'] is True:
        elements[0].click()
    if clueObject['picture']['schoolPic'] is True:
        elements[1].click()
    if clueObject['picture']['treePic'] is True:
        elements[2].click()
    if clueObject['picture']['catPic'] is True:
        elements[3].click()
    if clueObject['picture']['penguinsPic'] is True:
        elements[4].click()
    if clueObject['picture']['londonPic'] is True:
        elements[5].click()
    xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/finish_button']"
    if MobileUtil.click_element_by_xpath(xpath) is False:
        Log.LogOutput(LogLevel.DEBUG, message="完成按钮点击失败") 
    Log.LogOutput(LogLevel.DEBUG, message="图片选择完成")  
    return True

'''
    @功能：点击发布按钮
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2016-8-15
'''
def click_release_button():
    xpath = "//android.widget.TextView[@text='发布']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击发布按钮成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击发布按钮失败")
        return False
    
'''
    @功能：判断是否处于爆料发布页面
    @para: 
    @return: 在发布页面，返回True；否则返回False
    @ hongzenghui  2016-9-20
'''
def check_in_clue_realease_page():
    xpath = "//android.widget.TextView[@text='爆料' and @resource-id='com.tianque.linkage:id/action_bar_title']"
    if MobileUtil.wait_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="当前处于爆料发布页面")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="当前未处于爆料发布页面")
        return False