# -*- coding:UTF-8 -*-
'''
Created on 2016-9-6
说说列表相关AW
@author: hongzenghui
'''
from Mobile import MobileUtil
from COMMON import Log
from CONFIG.Define import LogLevel

'''
    @功能：检查说说描述
    @para: shuoshuoObject:说说对象内容，请引用ClueRelateObjectDef中的shuoshuoObject对象
    @return: 找到符合描述信息的说说，返回True；否则返回False
    @ hongzenghui  2016-9-6
'''
def check_shuoshuo_description(shuoshuoObject):
    xpath = "//android.widget.TextView[@text='%s']" % shuoshuoObject['description']
    if MobileUtil.wait_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="找到预期描述信息的说说")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="未找到预期描述信息的说说")
        return False
    
'''
    @功能：选择并点击某一说说
    @para: shuoshuoObject:说说对象内容，请引用ClueRelateObjectDef中的shuoshuoObject对象
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2016-9-6
'''
def select_and_click_shuoshuo(shuoshuoObject):
    xpath = "//android.widget.TextView[@text='%s']" % shuoshuoObject['description']
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击说说成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击说说失败")
        return False
    
'''
    @功能：检查评论数量
    @para: shuoshuoObject:说说对象内容，请引用ClueRelateObjectDef中的shuoshuoObject对象
    @return: 数量一致，返回True；否则返回False
    @ hongzenghui  2016-9-6
'''
def check_comment_counts(shuoshuoObject):
    xpath = "//android.widget.TextView[@text='%s']/following-sibling::android.widget.LinearLayout/android.widget.TextView[@text='%s' and @resource-id='com.tianque.linkage:id/comment_num']" % (shuoshuoObject['description'],shuoshuoObject['commentCount'])
    if MobileUtil.wait_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="说说评论数量与预期相符")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="说说评论数量与预期不符")
        return False
    
'''
    @功能：检查点赞数量
    @para: shuoshuoObject:说说对象内容，请引用ClueRelateObjectDef中的shuoshuoObject对象
    @return: 数量一致，返回True；否则返回False
    @ hongzenghui  2016-9-6
'''
def check_agree_counts(shuoshuoObject):
    xpath = "//android.widget.TextView[@text='%s']/following-sibling::android.widget.LinearLayout/android.widget.TextView[@text='%s' and @resource-id='com.tianque.linkage:id/praise_num']" % (shuoshuoObject['description'],shuoshuoObject['agreeCount'])
    if MobileUtil.wait_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="说说点赞数量与预期相符")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="说说点赞数量与预期不符")
        return False
    

'''
    @功能：关注说说
    @para: shuoshuoObject:说说对象内容，请引用ClueRelateObjectDef中的shuoshuoObject对象
    @return: 关注成功，返回True；否则返回False
    @ hongzenghui  2016-9-6
'''
def focus_shuoshuo(shuoshuoObject):
    #点击下拉按钮
    xpath = "//android.widget.TextView[@text='%s']/preceding-sibling::android.widget.LinearLayout/android.widget.ImageView[@resource-id='com.tianque.linkage:id/operation_button']" % shuoshuoObject['description']
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
    @para: shuoshuoObject:说说对象内容，请引用ClueRelateObjectDef中的shuoshuoObject对象
    @return: 删除成功，返回True；否则返回False
    @ hongzenghui  2016-9-6
'''
def delete_shuoshuo(shuoshuoObject):
    #点击下拉按钮
    xpath = "//android.widget.TextView[@text='%s']/preceding-sibling::android.widget.LinearLayout/android.widget.ImageView[@resource-id='com.tianque.linkage:id/operation_button']" % shuoshuoObject['description']
    if MobileUtil.click_element_by_xpath(xpath) is True:
        #点击删除
        xpath = "//android.widget.TextView[@resource-id ='com.tianque.linkage:id/delete']"
        MobileUtil.wait_element_by_xpath(xpath)
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
