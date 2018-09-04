# -*- coding:UTF-8 -*-
'''
Created on 2016-8-16
首页逻辑AW
@author: N-254
'''
from Mobile.Define.Clue.CommonDefine import LunboType
from Mobile.UI.Clue import MainPageUI
from COMMON import Log
from CONFIG.Define import LogLevel


'''
    @功能：检查首页轮播内容
    @para: 
    lunboType: 可以为公告、爆料  
    lunboObject: 轮播对象，公告或爆料，请引用OthersObjectDef下面的公告对象或者ClueRelateObjectDef下的爆料对象
    @return: 检查成功，返回True;否则返回False
    @ hongzenghui  2016-8-16
'''
def check_lunbo_content(lunboType=LunboType.NOTICE,lunboObject):
    #检查公告
    if lunboType==LunboType.NOTICE:
        MainPageUI.click_lunbo_info(lunboObject['subject'])
        #标题检查
        subjectRet = False
        #内容检查
        contentRet = False
        if subjectRet and contentRet:
            Log.LogOutput(LogLevel.DEBUG, message="公告信息检查成功")
        else:
            Log.LogOutput(LogLevel.WARN, message="公告信息检查失败")
        return True
    #检查爆料
    else:
        Log.LogOutput(LogLevel.ERROR, message="爆料信息肩擦成功")
        return False
    