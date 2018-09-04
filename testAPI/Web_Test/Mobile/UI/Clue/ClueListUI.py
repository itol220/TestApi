# -*- coding:UTF-8 -*-
'''
Created on 2016-8-19
爆料列表相关AW
@author: hongzenghui
'''
from Mobile import MobileUtil
from COMMON import Log
from CONFIG.Define import LogLevel
from extend import Appium_Extend
from CONFIG import Global

'''
    @功能：检查爆料描述
    @para: clueObject 线索对象内容，请引用ClueRelateObjectDef中的clueObject对象
    @return: 找到符合描述信息的爆料，返回True；否则返回False
    @ hongzenghui  2016-8-22
'''
def check_clue_description(clueObject):
    xpath = "//android.widget.TextView[contains(@text,'%s')]" % clueObject['description']
    if MobileUtil.wait_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="找到预期描述信息的爆料")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="未找到预期描述信息的爆料")
        return False
    
'''
    @功能：检查爆料主题
    @para: clueObject 线索对象内容，请引用ClueRelateObjectDef中的clueObject对象
    @return: 找到符合描述信息的爆料，返回True；否则返回False
    @ hongzenghui  2016-8-22
'''
def check_clue_subject(clueObject):
    xpath = "//android.widget.TextView[contains(@text,'# %s # %s')]" % (clueObject['subject'],clueObject['description'])
    if MobileUtil.wait_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="找到预期主题信息的爆料")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="未找到预期主题信息的爆料")
        return False
    
'''
    @功能：点击爆料主题
    @para: clueObject 线索对象内容，请引用ClueRelateObjectDef中的clueObject对象
    @return: 点击对应爆料的主题，返回True；否则返回False
    @ hongzenghui  2016-9-22
'''
def click_clue_subject(clueObject):
    xpath = "//android.widget.TextView[contains(@text,'# %s # %s')]" % (clueObject['subject'],clueObject['description'])
    element = MobileUtil.find_element_by_xpath(xpath)
    location = element.location
    size = element.size
    #点击左侧主题区域
    x = location["x"] + 20
    y = location["y"] + size["height"]/2
    if MobileUtil.click_by_position(x, y) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击爆料主题成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击爆料主题失败")
        return False

'''
    @功能：检查爆料图片
    @para: clueObject 线索对象内容，请引用ClueRelateObjectDef中的clueObject对象
    @return: 状态检查一致，返回True；否则返回False
    @ hongzenghui  2016-8-22
'''
def check_clue_picture_in_list(clueObject):
    xpath = "//android.widget.TextView[contains(@text,'%s')]/following-sibling::android.widget.LinearLayout/android.widget.ImageView" % clueObject['description']
    elements = MobileUtil.find_elements_by_xpath(xpath)
    if elements is None:
        Log.LogOutput(LogLevel.DEBUG, message="未找到符合爆料内容的任何图片")
        return False
    else:
        extend = Appium_Extend(Global.driver)
        #列表中的图片和详情中的图片之间像素有差异，列表只检测“湖”这张图片，要检测素有图片，请进入详情检测
        firstResult = False
        if clueObject['picture']['lakePic'] is True:
            load = extend.load_image(clueObject['picture']['lakePicListPath'])
            for element in elements:
                firstResult = extend.get_screenshot_by_element(element).same_as(load, 0)
                if firstResult is True:
                    Log.LogOutput(LogLevel.DEBUG, message="图片-湖-比对成功")
                    break
    if firstResult:
        Log.LogOutput(LogLevel.DEBUG, message="图片比对成功")
        return True
    else:
        Log.LogOutput(LogLevel.DEBUG, message="图片比对失败")
        return False
    
'''
    @功能：选择并点击某一爆料
    @para: clueObject 线索对象内容，请引用ClueRelateObjectDef中的clueObject对象
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2016-8-25
'''
def select_and_click_clue(clueObject):
    xpath = "//android.widget.TextView[contains(@text,'%s')]" % clueObject['description']
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击爆料成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击爆料失败")
        return False
    
'''
    @功能：检查爆料状态
    @para: clueObject 线索对象内容，请引用ClueRelateObjectDef中的clueObject对象
    @return: 状态检查一致，返回True；否则返回False
    @ hongzenghui  2016-8-22
'''
def check_clue_status(clueObject):
    xpath = "//android.widget.TextView[contains(@text,'%s')]/preceding-sibling::android.widget.LinearLayout/android.widget.TextView[@resource-id='com.tianque.linkage:id/status' and @text='%s']" % (clueObject['description'],clueObject['status'])
    if MobileUtil.wait_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="爆料状态与预期相符")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="爆料状态与预期不符")
        return False
    
'''
    @功能：检查官方回复数量
    @para: clueObject 线索对象内容，请引用ClueRelateObjectDef中的clueObject对象
    @return: 数量一致，返回True；否则返回False
    @ hongzenghui  2016-8-25
'''
def check_official_reply_counts(clueObject):
    xpath = "//android.widget.TextView[contains(@text,'%s')]/following-sibling::android.widget.LinearLayout/android.widget.TextView[@text='官方回复(%s)']" % (clueObject['description'],clueObject['officialReplyCount'])
    if MobileUtil.wait_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="爆料官方回复数量与预期相符")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="爆料官方回复数量与预期不符")
        return False
    
'''
    @功能：检查评论数量
    @para: clueObject 线索对象内容，请引用ClueRelateObjectDef中的clueObject对象
    @return: 数量一致，返回True；否则返回False
    @ hongzenghui  2016-8-25
'''
def check_comment_counts(clueObject):
    xpath = "//android.widget.TextView[contains(@text,'%s')]/following-sibling::android.widget.LinearLayout/android.widget.TextView[@text='评论(%s)']" % (clueObject['description'],clueObject['commentCount'])
    if MobileUtil.wait_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="爆料评论数量与预期相符")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="爆料评论数量与预期不符")
        return False
    
'''
    @功能：检查点赞数量
    @para: clueObject 线索对象内容，请引用ClueRelateObjectDef中的clueObject对象
    @return: 数量一致，返回True；否则返回False
    @ hongzenghui  2016-8-25
'''
def check_agree_counts(clueObject):
    xpath = "//android.widget.TextView[contains(@text,'%s')]/following-sibling::android.widget.LinearLayout/android.widget.TextView[@text='赞同(%s)']" % (clueObject['description'],clueObject['agreeCount'])
    if MobileUtil.wait_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="爆料点赞数量与预期相符")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="爆料点赞数量与预期不符")
        return False
    
'''
    @功能：关注爆料
    @para: clueObject 线索对象内容，请引用ClueRelateObjectDef中的clueObject对象
    @return: 关注成功，返回True；否则返回False
    @ hongzenghui  2016-8-25
'''
def focus_clue(clueObject):
    #点击下拉按钮
    xpath = "//android.widget.TextView[contains(@text,'%s')]/preceding-sibling::android.widget.LinearLayout/android.widget.ImageView[@resource-id='com.tianque.linkage:id/operation_button']" % clueObject['description']
    if MobileUtil.click_element_by_xpath(xpath) is True:
        #点击爆料
        xpath = "//android.widget.TextView[@resource-id ='com.tianque.linkage:id/concern']"
        MobileUtil.wait_element_by_xpath(xpath)
        MobileUtil.click_element_by_xpath(xpath)
        Log.LogOutput(LogLevel.DEBUG, message="关注爆料成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="关注爆料失败")
        return False
    
'''
    @功能：删除爆料
    @para: clueObject 线索对象内容，请引用ClueRelateObjectDef中的clueObject对象
    @return: 删除成功，返回True；否则返回False
    @ hongzenghui  2016-9-6
'''
def delete_clue(clueObject):
    #点击下拉按钮
    xpath = "//android.widget.TextView[contains(@text,'%s')]/preceding-sibling::android.widget.LinearLayout/android.widget.ImageView[@resource-id='com.tianque.linkage:id/operation_button']" % clueObject['description']
    if MobileUtil.click_element_by_xpath(xpath) is True:
        #点击关注
        xpath = "//android.widget.TextView[@resource-id ='com.tianque.linkage:id/delete']"
        MobileUtil.wait_element_by_xpath(xpath)
        MobileUtil.click_element_by_xpath(xpath)
        Log.LogOutput(LogLevel.DEBUG, message="删除爆料成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="删除爆料失败")
        return False

    