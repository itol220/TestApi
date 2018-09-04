# -*- coding:UTF-8 -*-
'''
Created on 2017-10-11
事件办理页面
@author: N-254
'''
from Mobile import MobileUtil
from COMMON import Log
from CONFIG.Define import LogLevel
from Mobile.Define.PingAnTong.IssueRelatedPara import IssueProcessType
from Mobile.UI.PingAnTong import PublicUI
from CONFIG import Global

'''
    @功能：     点击返回按钮
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2017年10月11日
'''

def click_back_button():
    xpath = "//android.view.ViewGroup[@resource-id='com.tianque.ecommunity.plugin.issue:id/toolbar']/android.widget.ImageButton"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击返回按钮成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击返回按钮失败")
        return False
    
'''
    @功能：     点击确定按钮
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2017年10月11日
'''

def click_confirm_button():
    xpath = "//android.widget.TextView[@resource-id='com.tianque.ecommunity.plugin.issue:id/submit']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击确定按钮成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击确定按钮失败")
        return False
    
'''
    @功能：     选择事件处理类型
    @para: issueObject：事件对象  IssueRelatePara.issueObject
    @return: 选择成功，返回True；否则返回False
    @ hongzenghui  2017年10月11日
'''

def select_issue_process_type(issueObject):
    xpath = "//android.widget.TextView[@resource-id='com.tianque.ecommunity.plugin.issue:id/ss_action_type']"
    if MobileUtil.click_element_by_xpath(xpath) is False:
        Log.LogOutput(LogLevel.ERROR, message="点击类型选择按钮失败")
        return True
    if issueObject['processType'] == IssueProcessType.BANLIZHONG:
        xpath = "//android.widget.TextView[@text='办理中']"
    elif issueObject['processType'] == IssueProcessType.SHANGBAO:
        xpath = "//android.widget.TextView[@text='上报']"
    elif issueObject['processType'] == IssueProcessType.JIAOBAN or issueObject['processType'] == IssueProcessType.XIETONGBANLI:
        xpath = "//android.widget.TextView[@text='交办']"
    elif issueObject['processType'] == IssueProcessType.HUITUI:
        xpath = "//android.widget.TextView[@text='回退']"
    elif issueObject['processType'] == IssueProcessType.JIEAN:
        xpath = "//android.widget.TextView[@text='结案']"
    elif issueObject['processType'] == IssueProcessType.HUIFU:
        xpath = "//android.widget.TextView[@text='回复']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="选择操作类型成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="选择操作类型失败")
        return False
    
'''
    @功能：     输入事件处理意见
    @para: issueObject：事件对象  IssueRelatePara.issueObject
    @return: 选择成功，返回True；否则返回False
    @ hongzenghui  2017年10月11日
'''

def input_issue_process_opinion(issueObject):
    xpath = "//android.widget.TextView[contains(@text,'办理意见')]/following-sibling::android.widget.LinearLayout/android.widget.EditText"
    if MobileUtil.input_element_by_xpath(xpath, issueObject['processOpinion']) is True:
        Log.LogOutput(LogLevel.DEBUG, message="输入办理意见成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="输入办理意见失败")
        return False
    
'''
    @功能：     添加办理附件照片
    @para: 
    @return: 选择成功，返回True；否则返回False
    @ hongzenghui  2017年10月11日
'''

def add_process_picture(issueObject):
    xpath = "//android.widget.ImageView[@resource-id='com.tianque.ecommunity.plugin.issue:id/img_view']"
    if MobileUtil.click_element_by_xpath(xpath) is False:
        Log.LogOutput(LogLevel.ERROR, message="点击添加图片按钮失败")
        return False
    #选择从图库选取
    if PublicUI.select_picture_from_lib() is True:
        Log.LogOutput(LogLevel.DEBUG, message="从图库选择照片完成")
    else:
        Log.LogOutput(LogLevel.ERROR, message="从图库选择照片异常")
        return False
    
'''
    @功能：     选择主办单位
    @para: issueObject：事件对象  IssueRelatePara.issueObject
    @return: 选择成功，返回True；否则返回False
    @ hongzenghui  2017年10月11日
'''

def select_host_org(issueObject):
    #点主办单位选择
    xpath = "//android.widget.TextView[@resource-id='com.tianque.ecommunity.plugin.issue:id/sw_organizers']"
    if MobileUtil.click_element_by_xpath(xpath) is False:
        Log.LogOutput(LogLevel.ERROR, message="点击主办部门选择按钮失败")
        return False
    else:
        Log.LogOutput(LogLevel.DEBUG, message="点击主办部门选择按钮成功")
        
    #选择部门
    xpath = "//android.widget.TextView[@text='%s']" % issueObject['jiaobanOrg']
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="选择主办部门成功")
    else:
        Log.LogOutput(LogLevel.ERROR, message="选择主办部门异常")
        return False
    
    #选择用户
    if issueObject['jiaobanUser'] is not None:
        xpath = "//android.widget.TextView[@text='%s']" % issueObject['jiaobanUser']
        if MobileUtil.click_element_by_xpath(xpath) is False:
            Log.LogOutput(LogLevel.ERROR, message="选择主办部门的特定用户异常")
            return False
        else:
            Log.LogOutput(LogLevel.DEBUG, message="选择主办部门的特定用户成功")
            
    #点击确定按钮
    xpath = "//android.widget.TextView[@resource-id='com.tianque.ecommunity.plugin.issue:id/confirm']"
    if MobileUtil.click_element_by_xpath(xpath) is False:
        Log.LogOutput(LogLevel.ERROR, message="点击确定按钮异常")
        return False
    else:
        Log.LogOutput(LogLevel.DEBUG, message="点击确定按钮成功")
        return True
    
'''
    @功能：     点击协同办理按钮
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2017年10月11日
'''

def click_xietongbanli_button():
    xpath = "//android.widget.CheckBox[@resource-id='com.tianque.ecommunity.plugin.issue:id/ss_coordination_handle']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击协同办理按钮成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击协同办理按钮失败")
        return False

'''
    @功能：     选择协办单位
    @para: issueObject：事件对象  IssueRelatePara.issueObject
    @return: 选择成功，返回True；否则返回False
    @ hongzenghui  2017年10月11日
'''

def select_coordination_org(issueObject):
    #点协办单位选择
    xpath = "//android.widget.TextView[@resource-id='com.tianque.ecommunity.plugin.issue:id/sw_co_rganizer']"
    if MobileUtil.click_element_by_xpath(xpath) is False:
        Log.LogOutput(LogLevel.ERROR, message="点击协办单位选择按钮失败")
        return False
    else:
        Log.LogOutput(LogLevel.DEBUG, message="点击协办单位选择按钮成功")
        
    #选择部门
    xpath = "//android.widget.TextView[@text='%s']" % issueObject['xiebanOrg']
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="选择协办部门成功")
    else:
        Log.LogOutput(LogLevel.ERROR, message="选择协办部门异常")
        return False
    
    #选择用户
    if issueObject['xiebanUser'] is not None:
        xpath = "//android.widget.TextView[@text='%s']" % issueObject['xiebanUser']
        if MobileUtil.click_element_by_xpath(xpath) is False:
            Log.LogOutput(LogLevel.ERROR, message="选择协办部门的特定用户异常")
            return False
        else:
            Log.LogOutput(LogLevel.DEBUG, message="选择协办部门的特定用户成功")
            
    #点击确定按钮
    xpath = "//android.widget.TextView[@resource-id='com.tianque.ecommunity.plugin.issue:id/confirm']"
    if MobileUtil.click_element_by_xpath(xpath) is False:
        Log.LogOutput(LogLevel.ERROR, message="点击确定按钮异常")
        return False
    else:
        Log.LogOutput(LogLevel.DEBUG, message="点击确定按钮成功")
        return True