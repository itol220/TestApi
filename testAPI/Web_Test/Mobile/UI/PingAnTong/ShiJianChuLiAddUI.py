# -*- coding:UTF-8 -*-
'''
Created on 2017-9-28

@author: N-254
'''
from Mobile import MobileUtil
from COMMON import Log, CommonUtil
from CONFIG.Define import LogLevel
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
    @功能：     输入事件名称
    @para: issueObject：事件对象  IssueRelatePara.issueObject
    @return: 输入成功，返回True；否则返回False
    @ hongzenghui  2017-9-28
'''

def input_issue_subject(issueObject):
    xpath = "//android.widget.LinearLayout[@resource-id='com.tianque.ecommunity.plugin.issue:id/sw_topic']/android.widget.EditText"
    if MobileUtil.input_element_by_xpath(xpath, issueObject['subject']) is not None:
        Log.LogOutput(LogLevel.DEBUG, message="输入事件名称成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="输入事件名称失败")
        return False
    
'''
    @功能：     输入事件简述
    @para: issueObject：事件对象  IssueRelatePara.issueObject
    @return: 输入成功，返回True；否则返回False
    @ hongzenghui  2017-9-28
'''

def input_issue_description(issueObject):
    xpath = "//android.widget.LinearLayout[@resource-id='com.tianque.ecommunity.plugin.issue:id/sw_incident_situation']/android.widget.EditText"
    if MobileUtil.input_element_by_xpath(xpath, issueObject['description']) is True:
        Log.LogOutput(LogLevel.DEBUG, message="输入事件简述成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="输入事件简述失败")
        return False

'''
    @功能：     选择发生网格
    @para: issueObject：事件对象  IssueRelatePara.issueObject
    @return: 输入成功，返回True；否则返回False
    @ hongzenghui  2017-9-28
'''

def select_issue_occur_grid(issueObject):    
    if CommonUtil.regMatchString(issueObject['occueGrid'],'-'):
        #表示需要选择下辖组织机构
        xpath = "//android.widget.TextView[@resource-id='com.tianque.ecommunity.plugin.issue:id/sw_grid_selector']"
        MobileUtil.click_element_by_xpath(xpath)
        #选择过程先不写
#         if MobileUtil.input_element_by_xpath(xpath, issueDesc) is not None:
#             Log.LogOutput(LogLevel.DEBUG, message="输入事件简述成功")
#             return True
#         else:
#             Log.LogOutput(LogLevel.ERROR, message="输入事件简述失败")
#             return False
        pass
    else:
        #表示发生网格为当前网格，不操作
        return True
    
'''
    @功能：     输入事件发生地点
    @para: issueObject：事件对象  IssueRelatePara.issueObject
    @return: 输入成功，返回True；否则返回False
    @ hongzenghui  2017-9-28
'''

def input_issue_occur_addr(issueObject):
    xpath = "//android.widget.LinearLayout[@resource-id='com.tianque.ecommunity.plugin.issue:id/sw_occur_location']/android.widget.EditText"
    if MobileUtil.input_element_by_xpath(xpath, issueObject['address']) is True:
        Log.LogOutput(LogLevel.DEBUG, message="输入事件发生地点成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="输入事件发生地点失败")
        return False
    
'''
    @功能：     选择事件类型
    @para: issueObject：事件对象  IssueRelatePara.issueObject 
    @return: 选择成功，返回True；否则返回False
    @ hongzenghui  2017-9-28
'''

def select_issue_type(issueObject):
    xpath = "//android.widget.TextView[@resource-id='com.tianque.ecommunity.plugin.issue:id/sw_type']"
    if MobileUtil.click_element_by_xpath(xpath) is False:
        return False   
    issueTypeList = issueObject['type'].split('-')
    for issueTypeItem in issueTypeList:
        xpath = "//android.widget.TextView[@text='%s']" % issueTypeItem
        if MobileUtil.click_element_by_xpath(xpath) is True:
            Log.LogOutput(LogLevel.DEBUG, message="事件类别：%s选择成功" % issueTypeItem)
            continue
        else:
            Log.LogOutput(LogLevel.ERROR, message="事件类别：%s选择失败" % issueTypeItem)
            return False
    Log.LogOutput(LogLevel.DEBUG, message="事件类别选择完成")
    
'''
    @功能：     输入涉及人数
    @para: issueObject：事件对象  IssueRelatePara.issueObject
    @return: 输入成功，返回True；否则返回False
    @ hongzenghui  2017-9-28
'''

def input_issue_relate_people_count(issueObject):
    xpath = "//android.widget.LinearLayout[@resource-id='com.tianque.ecommunity.plugin.issue:id/sw_involved_people_num']/android.widget.EditText"
    if MobileUtil.input_element_by_xpath(xpath, issueObject['peopleNo']) is True:
        Log.LogOutput(LogLevel.DEBUG, message="输入事件涉及人数成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="输入事件涉及人数失败")
        return False
    
'''
    @功能：     输入当事人信息
    @para: issueObject：事件对象  IssueRelatePara.issueObject
    @return: 输入成功，返回True；否则返回False
    @ hongzenghui  2017-9-28
'''

def input_issue_relate_people_info(issueObject):
    for name,telephone in issueObject['peopleInfo'].items():
        xpath = "//android.widget.EditText[@resource-id='com.tianque.ecommunity.plugin.issue:id/person_name']"
        if MobileUtil.input_element_by_xpath(xpath, name) is True:
            Log.LogOutput(LogLevel.DEBUG, message="输入事件当事人姓名成功")
        else:
            Log.LogOutput(LogLevel.ERROR, message="输入事件当事人姓名失败")
            return False
        xpath = "//android.widget.EditText[@resource-id='com.tianque.ecommunity.plugin.issue:id/person_mobile']"
        if MobileUtil.input_element_by_xpath(xpath, telephone) is True:
            Log.LogOutput(LogLevel.DEBUG, message="输入事件当事人电话成功")
        else:
            Log.LogOutput(LogLevel.ERROR, message="输入事件当事人电话失败")
            return False

'''
    @功能：     添加附件
    @para: 
    @return: 添加成功，返回True；否则返回False
    @ hongzenghui  2017-9-30
'''  
       
def add_picture_from_camera():
    #点击相机图标
    xpath = "//android.widget.ImageView[@resource-id='com.tianque.ecommunity.plugin.issue:id/sw_canmera']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击相机按钮成功")
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击相机按钮失败")
        return False
    
    #选择从图库选取
    if PublicUI.select_picture_from_lib() is True:
        Log.LogOutput(LogLevel.DEBUG, message="从图库选择照片完成")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="从图库选择照片异常")
        return False

'''
    @功能：     点击保存草稿按钮
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2017-9-30
'''

def click_save_as_draft_button():
    xpath = "//android.widget.TextView[@resource-id='com.tianque.ecommunity.plugin.issue:id/menu_id_save']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击保存草稿成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击保存草稿失败")
        return False
    
'''
    @功能：     点击提交按钮
    @para: 
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2017-9-30
'''

def click_submit_button():
    xpath = "//android.widget.TextView[@resource-id='com.tianque.ecommunity.plugin.issue:id/menu_id_submit']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击提交成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击提交失败")
        return False