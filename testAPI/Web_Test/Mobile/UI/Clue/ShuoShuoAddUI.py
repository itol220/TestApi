# -*- coding:UTF-8 -*-
'''
Created on 2016-9-6
新增说说页面相关操作
@author: hongzenghui
'''
from Mobile import MobileUtil
from COMMON import Log, Time
from CONFIG.Define import LogLevel

'''
    @功能：点击取消按钮
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2016-9-6
'''
def click_cancel_button():
    xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/left_text']"
    if MobileUtil.click_element_by_xpath(xpath) is False:
        Log.LogOutput(LogLevel.ERROR, message="点击取消按钮失败")
        return False
    else:
        Log.LogOutput(LogLevel.DEBUG, message="点击取消按钮成功")
        return True
    
'''
    @功能：点击发布按钮
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2016-9-6
'''
def click_publish_button():
    xpath = "//android.widget.TextView[@text='发布']"
    if MobileUtil.click_element_by_xpath(xpath) is False:
        Log.LogOutput(LogLevel.ERROR, message="点击发布按钮失败")
        return False
    else:
        Log.LogOutput(LogLevel.DEBUG, message="点击发布按钮成功")
        return True
    
'''
    @功能：选择主题
    @para: shuoshuoObject:说说对象内容，请引用ClueRelateObjectDef中的shuoshuoObject对象
    @return: 选择成功，返回True；否则返回False
    @ hongzenghui  2016-9-6
'''
def select_subject(shuoshuoObject):
    xpath = "//android.widget.TextView[@text='%s' and @resource-id='com.tianque.linkage:id/theme_label']" % shuoshuoObject['subject']
    if MobileUtil.click_element_by_xpath(xpath) is False:
        Log.LogOutput(LogLevel.ERROR, message="选择主题失败")
        return False
    else:
        Log.LogOutput(LogLevel.DEBUG, message="选择主题成功")
        return True
    
'''
    @功能：输入内容
    @para: shuoshuoObject:说说对象内容，请引用ClueRelateObjectDef中的shuoshuoObject对象
    @return: 输入成功，返回True；否则返回False
    @ hongzenghui  2016-9-6
'''
def input_shuoshuo_description(shuoshuoObject):
    xpath = "//android.widget.EditText[@resource-id='com.tianque.linkage:id/content']"
    if MobileUtil.input_element_by_xpath(xpath, shuoshuoObject['description']) is False:
        Log.LogOutput(LogLevel.ERROR, message="输入说说内容失败")
        return False
    else:
        Log.LogOutput(LogLevel.DEBUG, message="输入说说内容成功")
        return True
    
'''
    @功能：图片选择
    @para: shuoshuoObject:说说对象内容，请引用ClueRelateObjectDef中的shuoshuoObject对象
    @return: 选择成功，返回True；否则返回False
    @ hongzenghui  2016-9-6
'''
def add_shuoshuo_picture(shuoshuoObject):
    #无需添加图片
    if not shuoshuoObject['picture']['lakePic'] and not shuoshuoObject['picture']['schoolPic'] and \
        not shuoshuoObject['picture']['treePic'] and not shuoshuoObject['picture']['catPic'] and \
        not shuoshuoObject['picture']['penguinsPic'] and not shuoshuoObject['picture']['londonPic']:
        return True
    xpath = "//android.widget.ImageView[@resource-id='com.tianque.linkage:id/image_view']"
    if MobileUtil.click_element_by_xpath(xpath) is False:
        Log.LogOutput(LogLevel.DEBUG, message="添加图片按钮点击失败") 
    Time.wait(2)
    xpath = "//android.widget.ImageView[@resource-id='com.tianque.linkage:id/check']"
    elements = MobileUtil.find_elements_by_xpath(xpath) 
    if elements is None:
        return False
    if shuoshuoObject['picture']['lakePic'] is True:
        elements[0].click()
    if shuoshuoObject['picture']['schoolPic'] is True:
        elements[1].click()
    if shuoshuoObject['picture']['treePic'] is True:
        elements[2].click()
    if shuoshuoObject['picture']['catPic'] is True:
        elements[3].click()
    if shuoshuoObject['picture']['penguinsPic'] is True:
        elements[4].click()
    if shuoshuoObject['picture']['londonPic'] is True:
        elements[5].click()
    xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/finish_button']"
    if MobileUtil.click_element_by_xpath(xpath) is False:
        Log.LogOutput(LogLevel.DEBUG, message="完成按钮点击失败") 
    Log.LogOutput(LogLevel.DEBUG, message="图片选择完成")  
    return True
    
    