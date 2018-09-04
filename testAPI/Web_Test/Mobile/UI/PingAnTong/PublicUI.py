# -*- coding:UTF-8 -*-
'''
Created on 2017-10-11
跟手机交互，整个APP公用的界面，如图片选择
@author: N-254
'''
from Mobile import MobileUtil
from CONFIG.Define import LogLevel
from COMMON import Log

'''
    @功能：     从图库中选择图片
    @para: 
    @return: 添加成功，返回True；否则返回False
    @ hongzenghui  2017-10-11
'''

def select_picture_from_lib():
    #选择从图库选取
    xpath = "//android.widget.Button[@resource-id='com.tianque.ecommunity.plugin.issue:id/btn_pick_photo']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击从图库选择成功")
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击从图库选择失败")
        return False
    #进入照片
    xpath = "//android.widget.ImageView[@resource-id='com.tianque.ecommunity:id/photoalbum_item_image']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击进入图片选择成功")
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击进入图片选择失败")
        return False
    
    #选取图片
    xpath = "//android.widget.RelativeLayout[@index='1']/android.widget.RelativeLayout/android.widget.ImageView[@resource-id='com.tianque.ecommunity:id/photo_select']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="选择第二张图片成功")
    else:
        Log.LogOutput(LogLevel.ERROR, message="选择第二张图片失败")
        return False
    
    #点击完成
    xpath = "//android.widget.Button[@resource-id='com.tianque.ecommunity:id/finishBtn']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击完成按钮成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击完成按钮失败")
        return False