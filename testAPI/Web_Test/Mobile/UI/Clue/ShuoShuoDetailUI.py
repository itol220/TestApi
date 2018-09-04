# -*- coding:UTF-8 -*-
'''
Created on 2016-9-6
说说详情页AW
@author: hongzenghui
'''
from Mobile import MobileUtil
from CONFIG.Define import LogLevel
from COMMON import Log
from extend import Appium_Extend
from CONFIG import Global

'''
    @功能：点击返回按钮
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2016-8-29
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
    @功能：检查说说描述
    @para: shuoshuoObject:说说对象内容，请引用ClueRelateObjectDef中的shuoshuoObject对象
    @return: 说说描述信息一致，返回True；否则返回False
    @ hongzenghui  2016-9-6
'''
def check_shuoshuo_description(shuoshuoObject):
    xpath = "//android.widget.TextView[@text='%s' and @resource-id='com.tianque.linkage:id/content']" % shuoshuoObject['description']
    if MobileUtil.wait_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="说说描述检查通过")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="说说描述检查失败")
        return False
    
'''
    @功能：检查说说浏览数
    @para: shuoshuoObject:说说对象内容，请引用ClueRelateObjectDef中的shuoshuoObject对象
    @return: 说说浏览数一致，返回True；否则返回False
    @ hongzenghui  2016-9-6
'''
def check_shuoshuo_browser_count(shuoshuoObject):
    xpath = "//android.widget.TextView[@text='浏览数 %s' and @resource-id='com.tianque.linkage:id/tv_browser']" % shuoshuoObject['browseCount']
    if MobileUtil.wait_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="说说浏览数检查通过")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="说说浏览数检查失败")
        return False
    
'''
    @功能：关注说说
    @para: 
    @return: 关注成功，返回True；否则返回False
    @ hongzenghui  2016-9-6
'''
def focus_shuoshuo():
    #点击下拉按钮
    xpath = "//android.widget.ImageView[@resource-id='com.tianque.linkage:id/operation_button']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        #点击关注
        xpath = "//android.widget.TextView[@resource-id ='com.tianque.linkage:id/concern']"
        MobileUtil.wait_element_by_xpath(xpath)
        MobileUtil.click_element_by_xpath(xpath)
        Log.LogOutput(LogLevel.DEBUG, message="关注说说成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="关注说说失败")
        return False
    
'''
    @功能：删除说说
    @para: 
    @return: 删除成功，返回True；否则返回False
    @ hongzenghui  2016-9-6
'''
def delete_shuoshuo():
    #点击下拉按钮
    xpath = "//android.widget.ImageView[@resource-id='com.tianque.linkage:id/operation_button']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        #点击关注
        xpath = "//android.widget.TextView[@resource-id ='com.tianque.linkage:id/delete']"
        if MobileUtil.wait_element_by_xpath(xpath) is False:
            return False
        if MobileUtil.click_element_by_xpath(xpath) is False:
            return False
        #弹框确认
        xpath = "//android.widget.TextView[@text ='你确定要删除吗？']"
        if MobileUtil.wait_element_by_xpath(xpath) is False:
            return False
        else:
            xpath = "//android.widget.Button[@resource-id = 'com.tianque.linkage:id/tq_dialog_cancel']"
            if MobileUtil.click_element_by_xpath(xpath) is False:
                return False
        Log.LogOutput(LogLevel.DEBUG, message="删除说说成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="删除说说失败")
        return False
    
'''
    @功能：检查说说图片
    @para: shuoshuoObject:说说对象内容，请引用ClueRelateObjectDef中的shuoshuoObject对象
    @return: 状态检查一致，返回True；否则返回False
    @ hongzenghui  2016-9-6
'''
def check_shuoshuo_picture(shuoshuoObject):
    xpath = "//android.widget.GridView/android.widget.ImageView"
    elements = MobileUtil.find_elements_by_xpath(xpath)
    if elements is None:
        Log.LogOutput(LogLevel.DEBUG, message="未找到任何图片")
        return True
    else:
        extend = Appium_Extend(Global.driver)
        firstResult = False
        secondResult = False
        thirdResult = False
        fouthResult = False
        fifthResult = False
        sixResult = False
        if shuoshuoObject['picture']['lakePic'] is True:
            load = extend.load_image(shuoshuoObject['picture']['lakePicPath'])
            for element in elements:
                firstResult = extend.get_screenshot_by_element(element).same_as(load, 0)
                if firstResult is True:
                    Log.LogOutput(LogLevel.DEBUG, message="图片-湖-比对成功")
                    break
        if shuoshuoObject['picture']['schoolPic'] is True:
            load = extend.load_image(shuoshuoObject['picture']['schoolPicPath'])
            for element in elements:
                secondResult = extend.get_screenshot_by_element(element).same_as(load, 0)
                if secondResult is True:
                    Log.LogOutput(LogLevel.DEBUG, message="图片-学校-比对成功")
                    break
        if shuoshuoObject['picture']['treePic'] is True:
            load = extend.load_image(shuoshuoObject['picture']['treePicPath'])
            for element in elements:
                thirdResult = extend.get_screenshot_by_element(element).same_as(load, 0)
                if thirdResult is True:
                    Log.LogOutput(LogLevel.DEBUG, message="图片-树-比对成功")
                    break
        if shuoshuoObject['picture']['catPic'] is True:
            load = extend.load_image(shuoshuoObject['picture']['catPicPath'])
            for element in elements:
                fouthResult = extend.get_screenshot_by_element(element).same_as(load, 0)
                if fouthResult is True:
                    Log.LogOutput(LogLevel.DEBUG, message="图片-猫-比对成功")
                    break
        if shuoshuoObject['picture']['penguinsPic'] is True:
            load = extend.load_image(shuoshuoObject['picture']['penguinsPicPath'])
            for element in elements:
                fifthResult = extend.get_screenshot_by_element(element).same_as(load, 0)
                if fifthResult is True:
                    Log.LogOutput(LogLevel.DEBUG, message="图片-企鹅-比对成功")
                    break
        if shuoshuoObject['picture']['londonPic'] is True:
            load = extend.load_image(shuoshuoObject['picture']['londonPicPath'])
            for element in elements:
                sixResult = extend.get_screenshot_by_element(element).same_as(load, 0)
                if sixResult is True:
                    Log.LogOutput(LogLevel.DEBUG, message="图片-伦敦-比对成功")
                    break
    if firstResult and secondResult and thirdResult and fouthResult and fifthResult and sixResult:
        Log.LogOutput(LogLevel.DEBUG, message="图片比对成功")
        return True
    else:
        Log.LogOutput(LogLevel.DEBUG, message="图片比对失败")
        return True
    
'''
    @功能：点击点赞
    @para: 
    @return: 点击点赞成功，返回True；否则返回False
    @ hongzenghui  2016年9月18日
'''
def click_agree_menu():
    xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/praise_num']"
    if MobileUtil.wait_element_by_xpath(xpath):
        Log.LogOutput(LogLevel.DEBUG, message="点击点赞成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击点赞失败")
        return False
    

'''
    @功能：发表评论
    @para: shuoshuoObject:说说对象内容，请引用ClueRelateObjectDef中的shuoshuoObject对象
    @return: 评论发表成功，返回True；否则返回False
    @ hongzenghui  2016-8-29
'''
def input_comment(shuoshuoObject):
    xpath = "//android.widget.EditText[@resource-id='com.tianque.linkage:id/input_edit']"
    if MobileUtil.input_element_by_xpath(xpath, shuoshuoObject['commentContent']):
        Log.LogOutput(LogLevel.DEBUG, message="输入评论成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="输入评论失败")
        return False
    
'''
    @功能：点击评论发送按钮
    @para: 
    @return: 点击评论发送按钮成功，返回True；否则返回False
    @ hongzenghui 2016-9-18
'''
def click_comment_send_button():
    xpath = "//android.widget.Button[@resource-id='com.tianque.linkage:id/add_comment_btn']"
    if MobileUtil.click_element_by_xpath(xpath):
        Log.LogOutput(LogLevel.DEBUG, message="点击评论发送按钮成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击评论发送按钮失败")
        return False