# -*- coding: UTF-8 -*-
'''
Created on 2016-8-11

@author: N-254
'''
from Mobile import MobileUtil
from extend import Appium_Extend
from COMMON import Log
from CONFIG.Define import LogLevel
from CONFIG import Global, InitDefaultPara
from Mobile.Logic.Clue import ClueCommonLogic, ClueRelateLogic, ShuoShuoRelateLogic
from Mobile.UI.Clue import MainPageUI, ClueAddUI, LoginUI, RegistAccountUI,\
    ClueListUI, ClueDetailUI, PersonalUI, SettingUI, PersonInfoUI
from Mobile.Define.Clue import ClueRelateObjectDef, MyRelateObjectDef
import copy

#手机GUI自动化样例代码
driver = MobileUtil.MobileDriverReconnect()
# driver = MobileUtil.MobileDriverInit()
# MobileUtil.close_app()
# MobileUtil.start_app()

Log.LogOutput(LogLevel.INFO, message=Global.driver.page_source)
# driver.quit()
#----------------------------------
#临时测试区域
# PersonalUI.click_point_mall()
# PersonInfoUI.modify_head_picture()
# clueObject = copy.deepcopy(ClueRelateObjectDef.clueObject)
# clueObject['officialReplyEventFlow']['reportContent']='上报'
# clueObject['officialReplyEventFlow']['closeContent'] = '结案了'
# ClueDetailUI.check_official_reply_by_event(clueObject)
# xpathOpen = "//android.widget.TextView[@text='展开']"
# xpathReport = "//android.widget.TextView[@text='%s 上报%s ']/following-sibling::android.widget.LinearLayout/android.widget.TextView[@text='%s']" \
#     % (InitDefaultPara.xianSuoOrgInit['DftJieDaoOrg'],InitDefaultPara.xianSuoOrgInit['DftQuOrg'],clueObject['officialReplyEventFlow']['reportContent'])
# xpathReport = "//android.widget.TextView[@text='%s 上报%s ']/following-sibling::android.widget.LinearLayout" \
#     % (InitDefaultPara.xianSuoOrgInit['DftJieDaoOrg'],InitDefaultPara.xianSuoOrgInit['DftQuOrg'])
# print xpathReport
# MobileUtil.wait_element_by_xpath(xpathReport)
# MobileUtil.click_element_by_xpath(xpathOpen)
#----------------------------------

# # 登录
userInfo = copy.deepcopy(MyRelateObjectDef.userInfo)
# userInfo['mobilePhone']='15967127465'
# userInfo['password']='111111'
# LoginUI.input_mobile_number(userInfo)
# LoginUI.input_password(userInfo)
# LoginUI.click_login_button()
# userInfo['cityName']='测试自动化市'
# # RegistAccountUI.select_city(userInfo)
# driver.quit()
# userInfo['newPassword']='111111'
# userInfo['verifyPassword']='111111'
# SettingUI.modify_password(userInfo)
# #程序打开
# ClueCommonLogic.clue_login(userInfo)
# userInfo['nickName'] = 'nickname'
# userInfo['address']='常住地址'
# PersonInfoUI.modify_address(userInfo)

#爆料
clueObject = copy.deepcopy(ClueRelateObjectDef.clueObject)
clueObject['description'] = "爆料内容dddddd7" 
# clueObject['officialReplyCount'] = '7'
# clueObject['commentCount'] = '1'
# clueObject['agreeCount'] = '1'
# clueObject['status']= "新增"
# clueObject['officialReplyContent'] = '感谢参与，已经结案'
# clueObject['commentContent']='评论一下'
# clueObject['picture']['lakePic'] = True
# clueObject['picture']['schoolPic'] = True
# clueObject['picture']['treePic'] = True
# clueObject['picture']['catPic'] = True
# clueObject['picture']['penguinsPic'] = True
# clueObject['picture']['londonPic'] = True
# ClueRelateLogic.add_clue(clueObject)
# ClueAddUI.input_clue_content(clueObject)
# ret = ClueRelateLogic.check_clue_in_list(clueObject)
# print ret
#发表说说
shuoshuoObject = copy.deepcopy(ClueRelateObjectDef.shuoshuoObject)
shuoshuoObject['description'] = "说说测试一"
shuoshuoObject['picture']['lakePic'] = True
shuoshuoObject['picture']['schoolPic'] = True
shuoshuoObject['picture']['treePic'] = True
shuoshuoObject['picture']['catPic'] = True
shuoshuoObject['picture']['penguinsPic'] = True
shuoshuoObject['picture']['londonPic'] = True
# SpeakRelateLogic.add_shuoshou(shuoshuoObject)
# MainPageUI.click_add_clue_menu()

# #图片比对
# driver = MobileUtil.MobileDriverInit()
# #图片处理样例
extend = Appium_Extend(driver)
xpath = "//android.widget.TextView[@text='ssddd']/following-sibling::android.widget.LinearLayout/android.widget.ImageView"
# xpath = "//android.widget.GridView/android.widget.ImageView"
elements = driver.find_elements_by_xpath(xpath)
i = 1
load = extend.load_image('C:\\autotest_file\\AppImage\\lakeInList.png')
for element in elements:
    extend.get_screenshot_by_element(element).write_to_file("f:/screen", "pic%s" % i)
#     firstResult = extend.get_screenshot_by_element(element).same_as(load, 0)
#     print firstResult
    i = i +1
# load = extend.load_image("f:\\screen\\image.png")
# result = extend.get_screenshot_by_element(element).same_as(load, 0)
# print result

# # 选择区域
# xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/left_text']"
# MobileUtil.click_element_by_xpath(xpath)
# #选择大江东
# xpath = "//android.widget.TextView[@text='杭州大江东产业集聚区']"
# MobileUtil.click_element_by_xpath(xpath)
# #点击我的信息
# xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/tab_personal']"
# MobileUtil.click_element_by_xpath(xpath)
# #点击未登录
# xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/user_nick']"
# MobileUtil.click_element_by_xpath(xpath)
# #登录用户名输入
# xpath = "//android.widget.EditText[@resource-id='com.tianque.linkage:id/login_account']"
# MobileUtil.input_element_by_xpath(xpath, "13588806927")
# #登录密码输入
# xpath = "//android.widget.EditText[@resource-id='com.tianque.linkage:id/login_password']"
# MobileUtil.input_element_by_xpath(xpath, "11111111")
# #点击登录
# xpath = "//android.widget.Button[@resource-id='com.tianque.linkage:id/login_btn']"
# MobileUtil.click_element_by_xpath(xpath)
# #点击爆料
# xpath = "//android.widget.LinearLayout[@resource-id='com.tianque.linkage:id/tab_bar']/android.widget.TextView[3]"
# MobileUtil.click_element_by_xpath(xpath)
# #输入爆料内容
# xpath = "//android.widget.EditText[@resource-id='com.tianque.linkage:id/content']"
# MobileUtil.input_element_by_xpath(xpath, "这是一个测试爆料")
# #点击位置选择
# xpath = "//android.widget.TextView[@resource-id='com.tianque.linkage:id/choose_location']"
# MobileUtil.click_element_by_xpath(xpath)
# #输入地址
# xpath = "//android.widget.EditText[@resource-id='com.tianque.linkage:id/search_key']"
# el = driver.find_element_by_xpath(xpath)
# text = el.get_attribute('text')
# el.click()
# driver.keyevent(122)
# for i in range(0,len(text)):
#     driver.keyevent(112)
# MobileUtil.input_element_by_xpath(xpath, "浙江省杭州市萧山区义新桥")
# #确认
# xpath = "//android.widget.Button[@resource-id='com.tianque.linkage:id/confirm']"
# MobileUtil.click_element_by_xpath(xpath)
# #提交
# xpath = "//android.widget.Button[@resource-id='com.tianque.linkage:id/right_btn']"
# MobileUtil.click_element_by_xpath(xpath)
# #进信息广场
# xpath = "//android.widget.TextView[@text='信息广场']"
# MobileUtil.click_element_by_xpath(xpath)
