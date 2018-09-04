# -*- coding:UTF-8 -*-
'''
Created on 2016-10-14
商品详情页面相关操作
@author: chenhui
'''
from COMMON import Log
from CONFIG import Global
from CONFIG.Define import LogLevel
from Mobile import MobileUtil
from Mobile.UI.Clue import CommonUI
from extend import Appium_Extend

'''
    @功能：点击商品详情页面的确定兑换按钮
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ chenhui  2016-9-23
'''
def click_confirm_exchange_button():
    xpath = "//android.widget.Button[@text='确定兑换' and @resource-id='com.tianque.linkage:id/bt_ok']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击确定兑换按钮成功")
        return True
    else:
        Log.LogOutput(LogLevel.DEBUG, message="点击确定兑换按钮失败")
        return False

'''
    @功能：点击商品详情页面的"+"按钮
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ chenhui  2016-10-14
'''
def click_plus_button():
    xpath = "//android.widget.ImageView[@resource-id='com.tianque.linkage:id/iv_plus']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击“+”按钮成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击“+”按钮失败")
        return False
    
'''
    @功能：点击商品详情页面的"-"按钮
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ chenhui  2016-10-14
'''
def click_minus_button():
    xpath = "//android.widget.ImageView[@resource-id='com.tianque.linkage:id/iv_jian']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击“-”按钮成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击“-”按钮失败")
        return False
    
'''
    @功能：检查是否在商品详情页面
    @para: 
    @return: 处于主页，返回True；否则返回False
    @chenhui  2016-9-23
''' 
def check_in_goods_detail_page():
    xpath = "//android.widget.TextView[@text='商品详情' and @resource-id='com.tianque.linkage:id/action_bar_title']"
    if MobileUtil.wait_element_by_xpath(xpath,10) is True:
        Log.LogOutput(LogLevel.DEBUG, message="当前处于商品详情页面")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="当前未处于商品详情页面")
        return False   


'''
    @功能：点击实物商品详情页面的立即兑换按钮
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ chenhui  2016-10-08
'''
def click_immediately_exchange_button():
    xpath = "//android.widget.ImageView[@resource-id='com.tianque.linkage:id/iv_ok']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击立即兑换按钮成功")
        return True
    else:

        Log.LogOutput(LogLevel.DEBUG, message="点击立即兑换按钮失败")
        return False
    
'''
    @功能：检查实物-商品详情页面标题
    @para: 
    @return: 处于主页，返回True；否则返回False
    @chenhui  2016-10-14
''' 
def check_title_in_entity_page(PointObject):
    xpath = "//android.widget.TextView[@text='%s' and @resource-id='com.tianque.linkage:id/tv_type']"%PointObject['goodsName']
    if MobileUtil.wait_element_by_xpath(xpath,5) is True:
        Log.LogOutput(LogLevel.DEBUG, message="检查标题正确")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="检查标日错误")
        return False
        
'''
    @功能：检查实物-商品详情页面积分显示
    @para: 
    @return: 处于主页，返回True；否则返回False
    @chenhui  2016-10-14
''' 
def check_point_in_entity_page(PointObject):
    xpath = "//android.widget.TextView[@text='%s积分' and @resource-id='com.tianque.linkage:id/tv_integral']"%PointObject['goodsUnitPoint']
    if MobileUtil.wait_element_by_xpath(xpath,5) is True:
        Log.LogOutput(LogLevel.DEBUG, message="检查积分正确")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="检查积分错误")
        return False
    
'''
    @功能：检查实物-商品详情页面已兑换人数
    @para: 
    @return: 处于主页，返回True；否则返回False
    @chenhui  2016-10-14
''' 
def check_exchangedPersonNum_in_entity_page(PointObject):
    xpath = "//android.widget.TextView[@text='%s人已兑换' and @resource-id='com.tianque.linkage:id/tv_exchange']"%PointObject['exchangePersonNum']
    if MobileUtil.wait_element_by_xpath(xpath,5) is True:
        Log.LogOutput(LogLevel.DEBUG, message="检查已兑换人数正确")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="检查已兑换人数错误")
        return False
    
'''
    @功能：检查实物-商品详情页面库存
    @para: 
    @return: 处于主页，返回True；否则返回False
    @chenhui  2016-10-14
''' 
def check_stock_in_entity_page(PointObject):
    xpath = "//android.widget.TextView[@text='库存%s件' and @resource-id='com.tianque.linkage:id/tv_stock']"%PointObject['stock']
    if MobileUtil.wait_element_by_xpath(xpath,5) is True:
        Log.LogOutput(LogLevel.DEBUG, message="检查库存正确")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="检查库存错误")
        return False   
    

'''
    @功能：检查实物-商品详情页面商品详情
    @para: 
    @return: 处于主页，返回True；否则返回False
    @chenhui  2016-10-14
''' 
def check_goods_detail_in_entity_page(PointObject):
    xpath = "//android.widget.TextView[@text='%s' and @resource-id='com.tianque.linkage:id/tv_details']"%PointObject['goodsDetail']
    if MobileUtil.wait_element_by_xpath(xpath,5) is True:
        Log.LogOutput(LogLevel.DEBUG, message="检查商品详情信息正确")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="检查商品详情信息错误")
        return False   
    
'''
    @功能：检查实物-兑换数量
    @para: 
    @return: 处于主页，返回True；否则返回False
    @chenhui  2016-10-14
''' 
def check_exchange_goods_count_in_entity_page(PointObject):
    xpath = "//android.widget.TextView[@text='%s' and @resource-id='com.tianque.linkage:id/tv_number']"%PointObject['exchangeNum']
    if MobileUtil.wait_element_by_xpath(xpath,5) is True:
        Log.LogOutput(LogLevel.DEBUG, message="检查兑换数量正确")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="检查兑换数量错误")
        return False   

'''
    @功能：检查实物-总计积分
    @para: 
    @return: 处于主页，返回True；否则返回False
    @chenhui  2016-10-14
''' 
def check_total_point_count_in_entity_page(PointObject):
    xpath = "//android.widget.TextView[@text='%s积分' and @resource-id='com.tianque.linkage:id/tv_all_integral']"%PointObject['totalPoints']
    if MobileUtil.wait_element_by_xpath(xpath,5) is True:
        Log.LogOutput(LogLevel.DEBUG, message="检查总计积分正确")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="检查总计积分错误")
        return False 
    
'''
    @功能：检查积分商城-商品详情页面图片
    @para: PointObject
    @return: 状态检查一致，返回True；否则返回False
    @ chenhui  2016-10-20
'''
def check_picture_in_goods_detail_list(PointObject):
    xpath = "//android.widget.ImageView[@resource-id='com.tianque.linkage:id/imageView']"
    element = MobileUtil.find_element_by_xpath(xpath)
    return CommonUI.image_compare(element, PointObject['goodsPicturePath'])
#     return CommonUI.image_compare_with_sift(element, PointObject['goodsPicturePath'])