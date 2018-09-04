# -*- coding:UTF-8 -*-
'''
Created on 2016-9-23
积分商城页面相关操作
@author: chenhui
'''
from COMMON import Log, CommonUtil
from CONFIG import Global
from CONFIG.Define import LogLevel
from Mobile import MobileUtil
from Mobile.UI.Clue import CommonUI
from extend import Appium_Extend

    
'''
    @功能：点击积分规则按钮
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ chenhui  2016-9-23
'''
def click_point_rule_button():
    xpath = "//android.widget.TextView[@text='积分规则']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击积分规则按钮成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击积分规则按钮失败")
        return False   


'''
    @功能：点击兑换记录按钮
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ chenhui  2016-9-23
'''
def click_exchange_record_button():
    xpath = "//android.widget.LinearLayout[@text='兑换记录']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击积分兑换记录按钮成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击积分兑换记录按钮失败")
        return False
    
'''
    @功能：点击去兑换按钮
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ chenhui  2016-9-23
'''
def click_exchange_button(PointObject):
    xpath = "//android.widget.TextView[@text='%s']/parent::android.widget.RelativeLayout/following-sibling::android.widget.TextView[@text='去兑换']"%PointObject['goodsName']
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击去兑换按钮成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击去兑换按钮失败")
        return False

               
'''
    @功能：检查积分规则
    @para: PointObject:积分对象内容
    @return: 检查成功，返回True；否则返回False
    @ chenhui  2016-9-23
'''
def check_point_rule(PointObject):
    xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/text' and @text='%s']" % PointObject['rule']
    if MobileUtil.wait_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="检查积分规则成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="检查积分规则失败")
        return False    
    
    
'''
    @功能：检查区域和积分
    @para: PointObject:积分对象内容
    @return: 检查成功，返回True；否则返回False
    @ chenhui  2016-9-23
'''
def check_location_and_point(PointObject):
    xpath1 = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/tv_org_name' and @text='%s']" % PointObject['location']
    if MobileUtil.wait_element_by_xpath(xpath1) is True:
        Log.LogOutput(LogLevel.DEBUG, message="检查区域成功")
    else:
        Log.LogOutput(LogLevel.ERROR, message="检查区域失败")
        return False      
    xpath2 = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/tv_my_score' and @text='%s 积分']" % PointObject['score']
    if MobileUtil.wait_element_by_xpath(xpath2) is True:
        Log.LogOutput(LogLevel.DEBUG, message="检查积分成功")
    else:
        Log.LogOutput(LogLevel.ERROR, message="检查积分失败")
        return False  
    return True

    
'''
    @功能：检查余额和可兑换数额
    @para: PointObject:积分对象内容
    @return: 检查成功，返回True；否则返回False
    @ chenhui  2016-9-23
'''
def check_exchange_balance(PointObject):
    xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/tv_active_prompt' and @text='本期话费兑换余额 %s 元，您还能兑换 %s 元']" % (PointObject['totalBalance'],PointObject['personalBalance'])
    if MobileUtil.wait_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="检查兑换记录状态成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="检查兑换记录状态失败")
        return False
    

'''
    @功能：检查商品名称是否在商品列表中
    @para: PointObject:积分对象内容
    @return: 检查成功，返回True；否则返回False
    @ chenhui  2016-9-23
'''
def check_goodsname_in_list(PointObject):
    xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/tv_type' and @text='%s']" %PointObject['goodsName']
#     print xpath
    if MobileUtil.wait_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="检查商品名称列表成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="检查商品名称列表失败")
        return False

'''
    @功能：检查已兑换人数
    @para: PointObject:积分对象内容
    @return: 检查成功，返回True；否则返回False
    @ chenhui  2016-9-23
'''
def check_exchanged_person_num_in_list(PointObject):
    xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/tv_type' and @text='%s']/following-sibling::android.widget.LinearLayout/android.widget.TextView[@text='%s人已兑换'] " %(PointObject['goodsName'],PointObject['exchangePersonNum'])
#     print xpath
    if MobileUtil.wait_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="检查列表中已兑换人数成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="检查列表中已兑换人数失败")
        return False

'''
    @功能：检查库存
    @para: PointObject:积分对象内容
    @return: 检查成功，返回True；否则返回False
    @ chenhui  2016-10-08
'''
def check_stock(PointObject):
    xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/tv_type' and @text='%s']/following-sibling::android.widget.LinearLayout/android.widget.TextView[@text='库存%s件'] " %(PointObject['goodsName'],PointObject['stock'])
#     print xpath
    if MobileUtil.wait_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="检查列表中库存成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="检查列表中库存失败")
        return False
           
'''
    @功能：检查单个商品所需积分列表
    @para: PointObject:积分对象内容
    @return: 检查成功，返回True；否则返回False
    @ chenhui  2016-9-23
'''
def check_goods_unit_point_in_list(PointObject):
    xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/tv_type' and @text='%s']/following-sibling::android.widget.TextView[@text='%s积分' and @resource-id='com.tianque.linkage:id/tv_integral']" % (PointObject['goodsName'],PointObject['goodsUnitPoint'])
#     print xpath
    if MobileUtil.wait_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="检查列表中单个商品所需积分数成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="检查列表中单个商品所需积分数失败")
        return False
    
'''
    @功能：检查是否在积分商城页面
    @para: 
    @return: 处于主页，返回True；否则返回False
    @chenhui  2016-9-23
''' 
def check_in_point_mall_page():
    xpath = "//android.widget.TextView[@text='积分商城' and @resource-id='com.tianque.linkage:id/action_bar_title']"
    if MobileUtil.wait_element_by_xpath(xpath,20) is True:
        Log.LogOutput(LogLevel.DEBUG, message="当前处于积分商城页面")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="当前未处于积分商城页面")
        return False

'''
    @功能：检查是否在积分规则页面
    @para: 
    @return: 处于主页，返回True；否则返回False
    @chenhui  2016-9-30
''' 
def check_in_point_rule_page():
    xpath = "//android.widget.TextView[@text='积分规则' and @resource-id='com.tianque.linkage:id/action_bar_title']"
    if MobileUtil.wait_element_by_xpath(xpath,20) is True:
        Log.LogOutput(LogLevel.DEBUG, message="当前处于积分规则页面")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="当前未处于积分规则页面")
        return False
        
       
'''
    @功能：检查是否在兑换记录页面
    @para: 
    @return: 处于主页，返回True；否则返回False
    @chenhui  2016-9-23
''' 
def check_in_exchange_record_page():
    xpath = "//android.widget.TextView[@text='兑换记录' and @resource-id='com.tianque.linkage:id/action_bar_title']"
    if MobileUtil.wait_element_by_xpath(xpath,20) is True:
        Log.LogOutput(LogLevel.DEBUG, message="当前处于兑换记录页面")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="当前未处于兑换记录页面")
        return False
    
'''
    @功能：检查爆料图片
    @para: PointObject
    @return: 状态检查一致，返回True；否则返回False
    @ chenhui  2016-10-20
'''
def check_picture_in_point_mall_list(PointObject):
    xpath = "//android.widget.ImageView[@resource-id='com.tianque.linkage:id/imageView']"
    element = MobileUtil.find_element_by_xpath(xpath)
    return CommonUI.image_compare(element, PointObject['goodsPicturePath'])
#     return CommonUI.image_compare_with_sift(element, PointObject['goodsPicturePath'])