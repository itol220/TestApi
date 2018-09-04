# -*- coding:UTF-8 -*-
'''
Created on 2017-9-28

@author: N-254
'''
from Mobile import MobileUtil
from CONFIG.Define import LogLevel
from COMMON import Log
from Mobile.Define.PingAnTong.IssueRelatedPara import IssueProcessState
    
'''
    @功能：     进入我的待办
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2017-10-18
'''

def enter_to_my_need_done():
    xpath = "//android.widget.TextView[@resource-id='com.tianque.ecommunity.plugin.issue:id/bar_title']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击菜单选择成功")
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击菜单选择失败")
        return False
    xpath = "//android.widget.TextView[@text='我的待办']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="进入我的待办成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="进入我的待办失败")
        return False
    
'''
    @功能：     进入我的已办
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2017-10-18
'''

def enter_to_my_have_done():
    xpath = "//android.widget.TextView[@resource-id='com.tianque.ecommunity.plugin.issue:id/bar_title']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击菜单选择成功")
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击菜单选择失败")
        return False
    xpath = "//android.widget.TextView[@text='我的已办']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="进入我的已办成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="进入我的已办失败")
        return False
    
'''
    @功能：     进入我的已办结
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2017-10-18
'''

def enter_to_my_complete():
    xpath = "//android.widget.TextView[@resource-id='com.tianque.ecommunity.plugin.issue:id/bar_title']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击菜单选择成功")
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击菜单选择失败")
        return False
    xpath = "//android.widget.TextView[@text='我的已办结']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="进入我的已办结成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="进入我的已办结失败")
        return False
    
'''
    @功能：     进入下辖待办
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2017-10-18
'''

def enter_to_xiaxia_need_done():
    xpath = "//android.widget.TextView[@resource-id='com.tianque.ecommunity.plugin.issue:id/bar_title']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击菜单选择成功")
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击菜单选择失败")
        return False
    xpath = "//android.widget.TextView[@text='下辖待办']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="进入下辖待办成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="进入下辖待办失败")
        return False
    
'''
    @功能：     进入下辖已办结
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2017-10-18
'''

def enter_to_xiaxia_complete():
    xpath = "//android.widget.TextView[@resource-id='com.tianque.ecommunity.plugin.issue:id/bar_title']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击菜单选择成功")
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击菜单选择失败")
        return False
    xpath = "//android.widget.TextView[@text='下辖已办结']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="进入下辖已办结成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="进入下辖已办结失败")
        return False

'''
    @功能：     点击新增按钮
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2017-9-28
'''

def click_add_issue_button():
    xpath = "//android.widget.TextView[@resource-id='com.tianque.ecommunity.plugin.issue:id/menu_id_add']"
    if MobileUtil.click_element_by_xpath(xpath,30) is True:
        Log.LogOutput(LogLevel.DEBUG, message="进入事件处理成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="进入事件处理失败")
        return False
    
'''
    @功能：     检查事件标题
    @para: issueObject：事件对象  IssueRelatePara.issueObject
    @return: 检查成功，返回True；否则返回False
    @ hongzenghui  2017-9-30
'''    
   
def check_issue_subject(issueObject):
    xpath = "//android.widget.TextView[@resource-id='com.tianque.ecommunity.plugin.issue:id/txt_event_title' and @text='%s']" % issueObject['subject']
    if MobileUtil.find_element_by_xpath(xpath) is not None:
        Log.LogOutput(LogLevel.DEBUG, message="找到标题为'%s'的事件" % issueObject['subject'])
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="未找到标题为'%s'的事件" % issueObject['subject'])
        return False
    
'''
    @功能：     检查事件描述
    @para: issueObject：事件对象  IssueRelatePara.issueObject
    @return: 检查成功，返回True；否则返回False
    @ hongzenghui  2017-9-30
'''    
   
def check_issue_description(issueObject):
    xpath = "//android.widget.TextView[@text='%s']/following-sibling::android.widget.TextView[@resource-id='com.tianque.ecommunity.plugin.issue:id/txt_event_description' and @text='%s']" % (issueObject['subject'],issueObject['description'])
    if MobileUtil.find_element_by_xpath(xpath) is not None:
        Log.LogOutput(LogLevel.DEBUG, message="找到描述为'%s'的事件" % issueObject['description'])
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="未找到描述为'%s'的事件" % issueObject['description'])
        return False    
    
'''
    @功能：     检查事件状态
    @para: issueObject：事件对象  IssueRelatePara.issueObject
    @return: 检查成功，返回True；否则返回False
    @ hongzenghui  2017-9-30
'''    
   
def check_issue_deal_state(issueObject):
    if issueObject['state'] is not None:
        if issueObject['state'] == IssueProcessState.UNPROCESS:
            xpath = "//android.widget.TextView[@text='%s']/following-sibling::android.widget.RelativeLayout/android.widget.TextView[@resource-id='com.tianque.ecommunity.plugin.issue:id/txt_event_state' and @text='待受理']" % issueObject['subject']
        elif issueObject['state'] == IssueProcessState.PROCESSING:
            xpath = "//android.widget.TextView[@text='%s']/following-sibling::android.widget.RelativeLayout/android.widget.TextView[@resource-id='com.tianque.ecommunity.plugin.issue:id/txt_event_state' and @text='办理中']" % issueObject['subject']
        elif issueObject['state'] == IssueProcessState.PROCESSED:
            xpath = "//android.widget.TextView[@text='%s']/following-sibling::android.widget.RelativeLayout/android.widget.TextView[@resource-id='com.tianque.ecommunity.plugin.issue:id/txt_event_state' and @text='已完成']" % issueObject['subject']        
    if MobileUtil.find_element_by_xpath(xpath) is not None:
        Log.LogOutput(LogLevel.DEBUG, message="找到预期状态的事件")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="未找到预期状态的事件")
        return False   
    
'''
    @功能：     办理事件
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2017-9-28
'''

def process_issue(issueObject):
    xpath = "//android.widget.TextView[@resource-id='com.tianque.ecommunity.plugin.issue:id/txt_event_title' and @text='%s']/../../../following-sibling::android.widget.LinearLayout/android.widget.TextView[@resource-id='com.tianque.ecommunity.plugin.issue:id/txt_event_btn_handle' and @text='办理']" % issueObject['subject']
    if MobileUtil.click_element_by_xpath(xpath,30) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击事件办理成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击事件办理失败")
        return False 
    
'''
    @功能：     受理事件
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2017-9-28
'''

def accept_issue(issueObject):
    xpath = "//android.widget.TextView[@resource-id='com.tianque.ecommunity.plugin.issue:id/txt_event_title' and @text='%s']/../../../following-sibling::android.widget.LinearLayout/android.widget.TextView[@resource-id='com.tianque.ecommunity.plugin.issue:id/txt_event_btn_handle' and @text='受理']" % issueObject['subject']
    if MobileUtil.click_element_by_xpath(xpath,30) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击事件办理成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击事件办理失败")
        return False
        