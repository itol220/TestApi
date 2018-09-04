# -*- coding:UTF-8 -*-
'''
Created on 2017-10-12
事件处理相关逻辑AW
@author: N-254
'''
from Mobile.UI.PingAnTong import ShiJianChuLiListUI, ShiJianChuLiAddUI,\
    ShiJianChuLiBanLiUI, PopupWindowProcessUI
from Mobile.Define.PingAnTong.CommonModuePara import PopupProcessType
from Mobile.Define.PingAnTong.IssueRelatedPara import IssueProcessType,\
    IssueClassifyMenu
from COMMON import Time

'''
    @功能：     新增事件
    @para: issueObject：事件对象  IssueRelatePara.issueObject
    @return: 新增成功，返回True；否则返回False
    @ hongzenghui  2017-10-12
'''

def add_issue(issueObject):
    #点击新增按钮 
    if ShiJianChuLiListUI.click_add_issue_button() is False:
        return False
    
    #选择事件类型
    if issueObject['type'] is not None:
        if ShiJianChuLiAddUI.select_issue_type(issueObject) is False:
            return False
        
    #输入标题
    if issueObject['subject'] is not None:
        if ShiJianChuLiAddUI.input_issue_subject(issueObject) is False:
            return False
    #输入描述
    if issueObject['description'] is not None:
        if ShiJianChuLiAddUI.input_issue_description(issueObject) is False:
            return False
    #选择发生网格
    if issueObject['occueGrid'] is not None:
        if ShiJianChuLiAddUI.select_issue_occur_grid(issueObject) is False:
            return False
    #输入发生地点
    if issueObject['address'] is not None:
        if ShiJianChuLiAddUI.input_issue_occur_addr(issueObject) is False:
            return False
    
    #输入当事人信息
    if issueObject['peopleInfo'] is not None:
        if ShiJianChuLiAddUI.input_issue_relate_people_info(issueObject) is False:
            return False
    #输入涉及人数
    if issueObject['peopleNo'] is not None:
        if ShiJianChuLiAddUI.input_issue_relate_people_count(issueObject) is False:
            return False
        Time.wait(1)
    #添加图片附件
    if issueObject['attchment'] is not None:
        if ShiJianChuLiAddUI.add_picture_from_camera() is False:
            return False
    #点击提交按钮
    if ShiJianChuLiAddUI.click_submit_button() is False:
        return False
    return True
    
'''
    @功能：     新增事件成草稿
    @para: issueObject：事件对象  IssueRelatePara.issueObject
    @return: 新增成功，返回True；否则返回False
    @ hongzenghui  2017-10-12
'''

def add_issue_as_draft(issueObject):
    #点击新增按钮 
    if ShiJianChuLiListUI.click_add_issue_button() is False:
        return False
    #输入标题
    if issueObject['subject'] is not None:
        if ShiJianChuLiAddUI.input_issue_subject(issueObject) is False:
            return False
    #输入描述
    if issueObject['description'] is not None:
        if ShiJianChuLiAddUI.input_issue_subject(issueObject) is False:
            return False
    #选择发生网格
    if issueObject['occueGrid'] is not None:
        if ShiJianChuLiAddUI.select_issue_occur_grid(issueObject) is False:
            return False
    #输入发生地点
    if issueObject['address'] is not None:
        if ShiJianChuLiAddUI.input_issue_occur_addr(issueObject) is False:
            return False
    #选择事件类型
    if issueObject['type'] is not None:
        if ShiJianChuLiAddUI.select_issue_type(issueObject) is False:
            return False
    #输入当事人信息
    if issueObject['peopleInfo'] is not None:
        if ShiJianChuLiAddUI.input_issue_relate_people_info(issueObject) is False:
            return False
    #输入涉及人数
    if issueObject['peopleNo'] is not None:
        if ShiJianChuLiAddUI.input_issue_relate_people_count(issueObject) is False:
            return False
    #添加图片附件
    if issueObject['attchment'] is not None:
        if ShiJianChuLiAddUI.add_picture_from_camera() is False:
            return False
    #点击保存草稿按钮
    if ShiJianChuLiAddUI.click_save_as_draft_button() is False:
        return False
    return True
    
'''
    @功能：     列表中检查事件
    @para: issueObject：事件对象  IssueRelatePara.issueObject
    @return: 检查成功，返回True；否则返回False
    @ hongzenghui  2017-10-13
'''

def check_issue_info_in_list(issueObject):
    #检查主题
    if issueObject['subject'] is not None:
        if ShiJianChuLiListUI.check_issue_subject(issueObject) is False:
            return False
    #检查描述
    if issueObject['description'] is not None:
        if ShiJianChuLiListUI.check_issue_description(issueObject) is False:
            return False
    #检查状态
    if issueObject['state'] is not None:
        if ShiJianChuLiListUI.check_issue_deal_state(issueObject) is False:
            return False
    return True

'''
    @功能：     处理事件
    @para: issueObject：事件对象  IssueRelatePara.issueObject
    @return: 处理成功，返回True；否则返回False
    @ hongzenghui  2017-10-13
'''

def process_issue(issueObject):
    #先受理
    if issueObject['needAccept'] is True:
        if ShiJianChuLiListUI.accept_issue(issueObject) is False:
            return False
        if PopupWindowProcessUI.popup_window_process(processType=PopupProcessType.ACCEPT) is False:
            return False
    #点击办理
    if ShiJianChuLiListUI.process_issue(issueObject) is False:
        return False
    #选择操作类型
    if issueObject['processType'] is not None:
        if ShiJianChuLiBanLiUI.select_issue_process_type(issueObject) is False:
            return False 
        else:
            #点击协同办理
            if issueObject['processType'] == IssueProcessType.XIETONGBANLI:
                if ShiJianChuLiBanLiUI.click_xietongbanli_button() is False:
                    return False
    #选择主办单位
    if issueObject['jiaobanOrg'] is not None:
        if ShiJianChuLiBanLiUI.select_host_org(issueObject) is False:
            return False  
    #选择协办部门
    if issueObject['xiebanOrg'] is not None:
        if ShiJianChuLiBanLiUI.select_coordination_org(issueObject) is False:
            return False
    #输入办理意见
    if issueObject['processOpinion'] is not None:
        if ShiJianChuLiBanLiUI.input_issue_process_opinion(issueObject) is False:
            return False
    #点击确定按钮
    if ShiJianChuLiBanLiUI.click_confirm_button() is False:
        return False
    return True


'''
    @功能：     选择事件分类菜单
    @para: classifyMenu:分类菜单，分为"我的待办"、"我的已办"、"我的已办结"、"下辖待办"、"下辖已办结", IssueRelatedPara.IssueClassifyMenu
    @return: 点击成功，返回True；否则返回False
    @ hongzenghui  2017-10-18
'''

def select_issue_classify_menu(classifyMenu):
    if classifyMenu == IssueClassifyMenu.WODEDAIBAN:
        ret = ShiJianChuLiListUI.enter_to_my_need_done()
    elif classifyMenu == IssueClassifyMenu.WODEYIBAN:
        ret = ShiJianChuLiListUI.enter_to_my_have_done()
    elif classifyMenu == IssueClassifyMenu.WODEYIBANJIE:
        ret = ShiJianChuLiListUI.enter_to_my_complete()
    elif classifyMenu == IssueClassifyMenu.XIAXIADAIBAN:
        ret = ShiJianChuLiListUI.enter_to_xiaxia_need_done()
    elif classifyMenu == IssueClassifyMenu.XIAXIAYIBANJIE:
        ret = ShiJianChuLiListUI.enter_to_xiaxia_complete()
    if ret is True:
        return True
    else:
        return False
