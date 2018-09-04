# -*- coding:UTF-8 -*-
'''
Created on 2016-8-17
爆料相关逻辑AW，如爆料新增、爆料检查等
para: clueObject为线索对象，请引用ClueRelateObjectDef中的clueObject字典
@author: hongzenghui
'''
from Mobile.UI.Clue import MainPageUI, ClueAddUI, ClueListUI, ClueDetailUI

'''
    @功能：新增爆料
    @para: clueObject:爆料对象内容，请引用ClueRelateObjectDef中的clueObject对象
    @return: 新增成功，返回True；否则返回False
    @ hongzenghui  2016-9-6
'''
def add_clue(clueObject):
    #点击爆料按钮
    if MainPageUI.click_add_clue_menu() is False:
        return False
    #点击位置选择
    if clueObject['address'] is not None:
        if ClueAddUI.click_location_select() is False:
            return False
    #选择主题
    if clueObject['subject'] is not None:
        if ClueAddUI.select_subject(clueObject) is False:
            return False
    #输入内容
    if clueObject['description'] is not None:
        if ClueAddUI.input_clue_content(clueObject) is False:
            return False
    #添加图片
    if ClueAddUI.add_clue_picture(clueObject) is False:
        return False
    #点击发布
    if ClueAddUI.click_release_button() is False:
        return False
    return True

'''
    @功能：在爆料列表检查爆料是否存在
    @para: clueObject:爆料对象内容，请引用ClueRelateObjectDef中的clueObject对象
    @return: 检查成功，返回True；否则返回False
    @ hongzenghui  2016-9-20
'''
def check_clue_in_list(clueObject):
    #检查爆料内容
    if clueObject['description'] is not None:
        if ClueListUI.check_clue_description(clueObject) is False:
            return False
    #检查主题
    if clueObject['subject'] is not None:
        if ClueListUI.check_clue_subject(clueObject) is False:
            return False
    #检查图片（因同一张图片每次爆料在列表中展示的像素不一致，影响检查结果，暂不检查，如需检查，可进详情查看）
    if clueObject['picture']['lakePic'] or clueObject['picture']['schoolPic'] or\
    clueObject['picture']['treePic'] or clueObject['picture']['catPic'] or \
    clueObject['picture']['penguinsPic'] or clueObject['picture']['londonPic']:
        pass
    #检查状态
    if clueObject['status'] is not None:
        if ClueListUI.check_clue_status(clueObject) is False:
            return False
    #检查官方回复数量
    if clueObject['officialReplyCount'] is not None:
        if ClueListUI.check_official_reply_counts(clueObject) is False:
            return False
    #检查评论数量
    if clueObject['commentCount'] is not None:
        if ClueListUI.check_comment_counts(clueObject) is False:
            return False
    #检查点赞数量
    if clueObject['agreeCount'] is not None:
        if ClueListUI.check_agree_counts(clueObject) is False:
            return False
    return True

'''
    @功能：在爆料详情页面检查爆料信息
    @para: clueObject:爆料对象内容，请引用ClueRelateObjectDef中的clueObject对象
    @return: 检查成功，返回True；否则返回False
    @ hongzenghui  2016-9-20
'''
def check_clue_in_detail(clueObject):
    #从列表进入详情
    if ClueListUI.select_and_click_clue(clueObject) is False:
        return False
    #检查爆料内容
    if clueObject['description'] is not None:
        if ClueDetailUI.check_clue_description(clueObject) is False:
            return False
    #检查主题
    if clueObject['subject'] is not None:
        pass
    #检查图片
    if clueObject['picture']['lakePic'] or clueObject['picture']['schoolPic'] or\
    clueObject['picture']['treePic'] or clueObject['picture']['catPic'] or \
    clueObject['picture']['penguinsPic'] or clueObject['picture']['londonPic']:
        if ClueDetailUI.check_clue_picture(clueObject) is False:
            return False
    #检查状态
    if clueObject['status'] is not None:
        if ClueDetailUI.check_clue_status(clueObject) is False:
            return False
    #检查官方回复内容（非事件回复）
    if clueObject['officialReplyContent'] is not None:
        if ClueDetailUI.check_official_reply_notby_event(clueObject) is False:
            return False
    #检查官方回复内容（事件流转）
    if clueObject['officialReplyEventFlow']['reportContent'] is not None:
        if ClueDetailUI.check_official_reply_by_event(clueObject) is False:
            return False
    #检查评论内容
    if clueObject['commentContent'] is not None:
        if ClueDetailUI.check_comment_content(clueObject) is False:
            return False
    return True