# -*- coding:UTF-8 -*-
'''
Created on 2017-10-11

@author: N-254
'''
from Mobile import MobileUtil
from COMMON import Log
from CONFIG.Define import LogLevel

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
    @功能：     点击修改钮
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2017年10月11日
'''

def click_modify_button():
    xpath = "//android.widget.TextView[@resource-id='com.tianque.ecommunity.plugin.issue:id/menu_id_edit']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击修改按钮成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击修改按钮失败")
        return False 
    
'''
    @功能：     点击办理按钮
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2017年10月11日
'''

def click_process_button():
    xpath = "//android.widget.TextView[@resource-id='com.tianque.ecommunity.plugin.issue:id/menu_id_submit']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击办理按钮成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击办理按钮失败")
        return False 
    
'''
    @功能：     检查事件标题
    @para: issueObject：事件对象  IssueRelatePara.issueObject
    @return: 检查成功，返回True；否则返回False
    @ hongzenghui  2017-10-11
'''    
   
def check_issue_subject(issueObject):
    xpath = "//android.widget.TextView[@resource-id='com.tianque.ecommunity.plugin.issue:id/txt' and @text='%s']" % issueObject['subject']
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
    @ hongzenghui  2017-10-11
'''    
   
def check_issue_description(issueObject):
    xpath = "//android.widget.TextView[@resource-id='com.tianque.ecommunity.plugin.issue:id/txt' and @text='%s']" % issueObject['description']
    if MobileUtil.find_element_by_xpath(xpath) is not None:
        Log.LogOutput(LogLevel.DEBUG, message="事件描述检查成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="事件描述检查失败")
        return False  
    
'''
    @功能：     检查事件类别
    @para: issueObject：事件对象  IssueRelatePara.issueObject
    @return: 检查成功，返回True；否则返回False
    @ hongzenghui  2017-10-11
'''    
   
def check_issue_type(issueObject):
    xpath = "//android.widget.TextView[@resource-id='com.tianque.ecommunity.plugin.issue:id/sw_type' and @text='%s']" % issueObject['type']
    if MobileUtil.find_element_by_xpath(xpath) is not None:
        Log.LogOutput(LogLevel.DEBUG, message="事件类型检查成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="事件类型检查失败")
        return False