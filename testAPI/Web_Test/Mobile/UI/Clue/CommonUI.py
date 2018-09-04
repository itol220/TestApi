# -*- coding:UTF-8 -*-
'''
Created on 2016-10-14
订单确认页面相关操作
@author: chenhui
'''
from COMMON import Log
from CONFIG import Global
from CONFIG.Define import LogLevel
from Mobile import MobileUtil
from extend import Appium_Extend
# import tempfile

'''
    @功能：点击返回按钮
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ chenhui  2016-9-23
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
    @功能：比较图片
    @para: element：需要比较的图片元素；picPath源图片路径
    @return: 点击成功，返回True；否则返回False
    @ chenhui  2016-10-20
'''    
def image_compare(element,picPath):    
    if element is None:
        Log.LogOutput(LogLevel.DEBUG, message="未找到任何图片")
        return False
    else:
        extend = Appium_Extend(Global.driver)
        firstResult = False
        load = extend.load_image(picPath)
        firstResult = extend.get_screenshot_by_element(element).same_as(load, 50)
        if firstResult is True:
            Log.LogOutput(LogLevel.DEBUG, message="图片比对成功")
            return True
        else:
            Log.LogOutput(LogLevel.ERROR, message="图片比对失败")
            return False
        
'''
    @功能：采用sift算法比较图片
    @para: element：需要比较的图片元素；picPath源图片路径
    @return: 点击成功，返回True；否则返回False
    @ chenhui  2016-10-21
'''    
# def image_compare_with_sift(element,picPath):
#     elementPicturePath=tempfile.gettempdir() + "/temp_screen.png" 
#     if element is None:
#         Log.LogOutput(LogLevel.DEBUG, message="未找到任何图片")
#         return False
#     else:
#         extend = Appium_Extend(Global.driver)
#         #对元素进行截图
#         extend.get_screenshot_by_element(element)
#         result=MobileUtil.sift_compare_picture(elementPicturePath, picPath, rate=0.5)
#         if result is True:
#             Log.LogOutput(LogLevel.DEBUG, message="图片比对成功")
#             return True
#         else:
#             Log.LogOutput(LogLevel.ERROR, message="图片比对失败")
#             return False
        
    