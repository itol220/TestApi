# -*- coding:UTF-8 -*-
'''
Created on 2016-9-17
说说相关逻辑AW，如说说新增、说说检查等
@author: hongzenghui
'''
from Mobile.UI.Clue import MainPageUI, SquareUI, ShuoShuoAddUI
from COMMON import Time

'''
    @功能：说说爆料
    @para: shuoshuoObject:说说对象内容，请引用ClueRelateObjectDef中的shuoshuoObject对象
    @return: 新增成功，返回True；否则返回False
    @ hongzenghui  2016-9-6
'''

def add_shuoshou(shuoshuoObject):
    #点击进入广场列表
    if MainPageUI.click_square_menu() is False:
        return False
    #点击说说tab
    if SquareUI.click_shuoshuo_tab() is False:
        return False
    Time.wait(2)
    #点击发表说说按钮
    if MainPageUI.click_add_clue_menu() is False:
        return False
    #选择主题
    if shuoshuoObject['subject'] is not None:
        if ShuoShuoAddUI.select_subject(shuoshuoObject) is False:
            return False
    #输入内容
    if shuoshuoObject['description'] is not None:
        if ShuoShuoAddUI.input_shuoshuo_description(shuoshuoObject) is False:
            return False
    #添加图片
    if ShuoShuoAddUI.add_shuoshuo_picture(shuoshuoObject) is False:
        return False
    #点击发布
    if ShuoShuoAddUI.click_publish_button() is False:
        return False
    return True