# -*- coding:UTF-8 -*-
'''
Created on 2016-8-25
爆料详情页AW
@author: hongzenghui
'''
from Mobile import MobileUtil
from COMMON import Log, Time
from CONFIG.Define import LogLevel
from CONFIG import Global, InitDefaultPara
from extend import Appium_Extend

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
    @功能：检查爆料状态
    @para: clueObject 线索对象内容，请引用ClueRelateObjectDef中的clueObject对象
    @return: 状态检查一致，返回True；否则返回False
    @ hongzenghui  2016-8-29
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
    @功能：检查爆料描述
    @para: clueObject 线索对象内容，请引用ClueRelateObjectDef中的clueObject对象
    @return: 爆料描述信息一致，返回True；否则返回False
    @ hongzenghui  2016-8-29
'''
def check_clue_description(clueObject):
    xpath = "//android.widget.TextView[contains(@text,'%s') and @resource-id='com.tianque.linkage:id/content']" % clueObject['description']
    if MobileUtil.wait_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="爆料描述检查通过")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="爆料描述检查失败")
        return False
    
'''
    @功能：检查爆料浏览数
    @para: clueObject 线索对象内容，请引用ClueRelateObjectDef中的clueObject对象
    @return: 爆料描述信息一致，返回True；否则返回False
    @ hongzenghui  2016-8-29
'''
def check_clue_browser_count(clueObject):
    xpath = "//android.widget.TextView[@text='浏览数 %s' and @resource-id='com.tianque.linkage:id/tv_browser']" % clueObject['browseCount']
    if MobileUtil.wait_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="爆料浏览数检查通过")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="爆料浏览数检查失败")
        return False
    
'''
    @功能：关注爆料
    @para: 
    @return: 关注成功，返回True；否则返回False
    @ hongzenghui  2016-8-29
'''
def focus_clue():
    #点击下拉按钮
    xpath = "//android.widget.ImageView[@resource-id='com.tianque.linkage:id/operation_button']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        #点击关注
        xpath = "//android.widget.TextView[@resource-id ='com.tianque.linkage:id/concern']"
        MobileUtil.wait_element_by_xpath(xpath)
        MobileUtil.click_element_by_xpath(xpath)
        Log.LogOutput(LogLevel.DEBUG, message="关注爆料成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="关注爆料失败")
        return False

'''
    @功能：分享爆料
    @para: 
    @return: 分享成功，返回True；否则返回False
    @ hongzenghui  2016-8-29
'''
def share_clue():
    #点击下拉按钮
    xpath = "//android.widget.ImageView[@resource-id='com.tianque.linkage:id/operation_button']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        #点击关注
        xpath = "//android.widget.TextView[@resource-id ='com.tianque.linkage:id/share']"
        MobileUtil.wait_element_by_xpath(xpath)
        MobileUtil.click_element_by_xpath(xpath)
        Log.LogOutput(LogLevel.DEBUG, message="分享爆料成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="分享爆料失败")
        return False
  
'''
    @功能：删除爆料
    @para: 
    @return: 删除成功，返回True；否则返回False
    @ hongzenghui  2016-8-29
'''
def delete_clue():
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
        Log.LogOutput(LogLevel.DEBUG, message="删除爆料成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="删除爆料失败")
        return False 
    
'''
    @功能：检查爆料图片
    @para: clueObject 线索对象内容，请引用ClueRelateObjectDef中的clueObject对象
    @return: 状态检查一致，返回True；否则返回False
    @ hongzenghui  2016-8-22
'''
def check_clue_picture(clueObject):
    xpath = "//android.widget.GridView/android.widget.ImageView"
    elements = MobileUtil.find_elements_by_xpath(xpath)
    if elements is None:
        Log.LogOutput(LogLevel.DEBUG, message="未找到任何图片")
        return False
    else:
        extend = Appium_Extend(Global.driver)
        firstResult = False
        secondResult = False
        thirdResult = False
        fouthResult = False
        fifthResult = False
        sixResult = False
        if clueObject['picture']['lakePic'] is True:
            load = extend.load_image(clueObject['picture']['lakePicPath'])
            for element in elements:
                firstResult = extend.get_screenshot_by_element(element).same_as(load, 50)
                if firstResult is True:
                    Log.LogOutput(LogLevel.DEBUG, message="图片-湖-比对成功")
                    break
        else:
            firstResult = True
            
        if clueObject['picture']['schoolPic'] is True:
            load = extend.load_image(clueObject['picture']['schoolPicPath'])
            for element in elements:
                secondResult = extend.get_screenshot_by_element(element).same_as(load, 50)
                if secondResult is True:
                    Log.LogOutput(LogLevel.DEBUG, message="图片-学校-比对成功")
                    break
        else:
            secondResult = True
            
        if clueObject['picture']['treePic'] is True:
            load = extend.load_image(clueObject['picture']['treePicPath'])
            for element in elements:
                thirdResult = extend.get_screenshot_by_element(element).same_as(load, 50)
                if thirdResult is True:
                    Log.LogOutput(LogLevel.DEBUG, message="图片-树-比对成功")
                    break
        else:
            thirdResult = True
            
        if clueObject['picture']['catPic'] is True:
            load = extend.load_image(clueObject['picture']['catPicPath'])
            for element in elements:
                fouthResult = extend.get_screenshot_by_element(element).same_as(load, 50)
                if fouthResult is True:
                    Log.LogOutput(LogLevel.DEBUG, message="图片-猫-比对成功")
                    break
        else:
            fouthResult = True
            
        if clueObject['picture']['penguinsPic'] is True:
            load = extend.load_image(clueObject['picture']['penguinsPicPath'])
            for element in elements:
                fifthResult = extend.get_screenshot_by_element(element).same_as(load, 50)
                if fifthResult is True:
                    Log.LogOutput(LogLevel.DEBUG, message="图片-企鹅-比对成功")
                    break
        else:
            fifthResult = True
            
        if clueObject['picture']['londonPic'] is True:
            load = extend.load_image(clueObject['picture']['londonPicPath'])
            for element in elements:
                sixResult = extend.get_screenshot_by_element(element).same_as(load, 50)
                if sixResult is True:
                    Log.LogOutput(LogLevel.DEBUG, message="图片-伦敦-比对成功")
                    break
        else:
            sixResult = True
            
    if firstResult and secondResult and thirdResult and fouthResult and fifthResult and sixResult:
        Log.LogOutput(LogLevel.DEBUG, message="图片比对成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="图片比对失败")
        return False
    
'''
    @功能：检查爆料地址
    @para: clueObject 线索对象内容，请引用ClueRelateObjectDef中的clueObject对象
    @return: 爆料地址信息一致，返回True；否则返回False
    @ hongzenghui  2016-8-29
'''
def check_clue_address(clueObject):
    xpath = "//android.widget.TextView[contains(@text,'%s') and @resource-id='com.tianque.linkage:id/address']" % clueObject['address']
    if MobileUtil.wait_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="爆料地址检查通过")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="爆料地址检查失败")
        return False
    
'''
    @功能：检查官方回复内容(不走事件流程)
    @para: clueObject 线索对象内容，请引用ClueRelateObjectDef中的clueObject对象
    @return: 直官方回复内容展示信息一致，返回True；否则返回False
    @ hongzenghui  2016-8-29
'''
def check_official_reply_notby_event(clueObject):
    #官方回复信息
    xpath = "//android.widget.TextView[contains(@text,'%s') and @resource-id='com.tianque.linkage:id/state_desc']" % clueObject['officialReplyContent']
    #结案状态
    xpath1 = "//android.widget.TextView[@text='%s']/preceding-sibling::android.widget.LinearLayout/android.widget.TextView[@text='结案' and @resource-id='com.tianque.linkage:id/tv_progress']" % InitDefaultPara.xianSuoOrgInit['DftQuOrg']
    if MobileUtil.wait_element_by_xpath(xpath) and MobileUtil.wait_element_by_xpath(xpath1):
        Log.LogOutput(LogLevel.DEBUG, message="爆料官方回复检查通过")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="爆料官方回复检查失败")
        return False
    
'''
    @功能：检查官方回复内容(走事件流程)
    @para: clueObject 线索对象内容，请引用ClueRelateObjectDef中的clueObject对象
    @return: 官方回复内容展示信息一致，返回True；否则返回False
    @ hongzenghui  2016-8-29
'''
def check_official_reply_by_event(clueObject):
    #点击办理展开
    xpathOpen = "//android.widget.ImageView [@resource-id='com.tianque.linkage:id/iv_close']"
    MobileUtil.click_element_by_xpath(xpathOpen)
    Log.LogOutput(LogLevel.DEBUG, message="点击完成")
    Time.wait(1)
    #界面滑动到底部
    xpathDst= "//android.widget.TextView[@text='已评：']"
    xpathSrc= "//android.widget.TextView[@text='办理' and @resource-id='com.tianque.linkage:id/tv_progress']"
    MobileUtil.move_from_one_element_to_another(xpathSrc, xpathDst)
    Time.wait(1)
    #上报信息查看
    xpathReport = "//android.widget.TextView[@text='%s 上报%s ']/following-sibling::android.widget.LinearLayout/android.widget.TextView[@text='%s']" \
    % (InitDefaultPara.xianSuoOrgInit['DftJieDaoOrg'],InitDefaultPara.xianSuoOrgInit['DftQuOrg'],clueObject['officialReplyEventFlow']['reportContent'])
    #结案信息查看
    xpathClose = "//android.widget.TextView[@text='结案']/../following-sibling::android.widget.TextView[@text='%s']/following-sibling::android.widget.TextView[@text='%s']" \
    % (clueObject['officialReplyEventFlow']['closeContent'],InitDefaultPara.xianSuoOrgInit['DftQuOrg'])
    if MobileUtil.wait_element_by_xpath(xpathReport) and MobileUtil.wait_element_by_xpath(xpathClose):
        Log.LogOutput(LogLevel.DEBUG, message="爆料事件流程检查通过")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="爆料事件流程检查失败")
        return False

'''
    @功能：点击评论菜单
    @para: 
    @return: 点击评论菜单成功，返回True；否则返回False
    @ hongzenghui  2016-8-29
'''
def click_comment_menu():
    xpath = "//android.widget.TextView[contains(@text,'评论') and @resource-id='com.tianque.linkage:id/public_comment_btn']"
    if MobileUtil.wait_element_by_xpath(xpath):
        Log.LogOutput(LogLevel.DEBUG, message="点击评论成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击评论失败")
        return False
    

'''
    @功能：发表评论
    @para: clueObject 线索对象内容，请引用ClueRelateObjectDef中的clueObject对象
    @return: 评论发表成功，返回True；否则返回False
    @ hongzenghui  2016-8-29
'''
def input_comment(clueObject):
    xpath = "//android.widget.EditText[@resource-id='com.tianque.linkage:id/input_edit']"
    if MobileUtil.input_element_by_xpath(xpath, clueObject['commentContent']):
        Log.LogOutput(LogLevel.DEBUG, message="输入评论成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="输入评论失败")
        return False
    
'''
    @功能：点击评论发送按钮
    @para: 
    @return: 点击评论发送按钮成功，返回True；否则返回False
    @ hongzenghui  2016-8-30
'''
def click_comment_send_button():
    xpath = "//android.widget.Button[@resource-id='com.tianque.linkage:id/add_comment_btn']"
    if MobileUtil.click_element_by_xpath(xpath):
        Log.LogOutput(LogLevel.DEBUG, message="点击评论发送按钮成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击评论发送按钮失败")
        return False
    
'''
    @功能：检查评论内容
    @para: clueObject 线索对象内容，请引用ClueRelateObjectDef中的clueObject对象
    @return: 检查评论内容成功，返回True；否则返回False
    @ hongzenghui  2016-8-30
'''
def check_comment_content(clueObject):
    xpath = "//android.widget.Button[@resource-id='com.tianque.linkage:id/add_comment_btn']"
    if MobileUtil.click_element_by_xpath(xpath):
        Log.LogOutput(LogLevel.DEBUG, message="点击评论发送按钮成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击评论发送按钮失败")
        return False