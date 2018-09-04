'''
Created on 2016-9-21
页面跳转方面的逻辑
@author: hongzenghui
'''
from COMMON import Log
from CONFIG.Define import LogLevel
from Mobile.UI.Clue import MainPageUI, SquareUI, PersonalUI

'''
    @功能：首页跳转到爆料列表
    @para: 
    @return: 跳转成功，返回True；否则返回False
    @ hongzenghui  2016-9-21
'''

def ShouYe2BaoLiaoLieBiao():
    if MainPageUI.click_square_menu() is True:
        return True
    else:
        return False
    
'''
    @功能：首页跳转到说说列表
    @para: 
    @return: 跳转成功，返回True；否则返回False
    @ hongzenghui  2016-9-21
'''

def ShouYe2ShuoShuoLieBiao():
    if MainPageUI.click_square_menu() is False:
        return False
    if SquareUI.click_shuoshuo_tab() is False:
        return False
    return True

'''
    @功能：首页跳转到平安宣传
    @para: 
    @return: 跳转成功，返回True；否则返回False
    @ hongzenghui  2016-9-21
'''

def ShouYe2PingAnXuanChuan():
    if MainPageUI.click_safe_propaganda() is False:
        return False
    return True

'''
    @功能：首页跳转到平安宣传
    @para: 
    @return: 跳转成功，返回True；否则返回False
    @ hongzenghui  2016-9-21
'''

def ShouYe2BianMinFuWu():
    if MainPageUI.click_bianmin_service() is False:
        return False
    return True

'''
    @功能：首页跳转到我的爆料
    @para: 
    @return: 跳转成功，返回True；否则返回False
    @ hongzenghui  2016-9-21
'''

def ShouYe2WoDeBaoLiao():
    if MainPageUI.click_my_clue() is False:
        return False
    return True

'''
    @功能：首页跳转到公告
    @para: 
    @return: 跳转成功，返回True；否则返回False
    @ hongzenghui  2016-9-21
'''

def ShouYe2GongGao():
    if MainPageUI.click_notice_menu() is False:
        return False
    return True

'''
    @功能：平安宣传转到首页
    @para: 
    @return: 跳转成功，返回True；否则返回False
    @ hongzenghui  2016-9-21
'''

def PingAnXuanChuan2ShouYe():
    return True

'''
    @功能：便民服务转到首页
    @para: 
    @return: 跳转成功，返回True；否则返回False
    @ hongzenghui  2016-9-21
'''

def BianMinFuWu2ShouYe():
    return True

'''
    @功能：公告转到首页
    @para: 
    @return: 跳转成功，返回True；否则返回False
    @ hongzenghui  2016-9-21
'''

def GongGao2ShouYe():
    if MainPageUI.click_firstpage_menu() is False:
        return False
    return True

'''
    @功能：我的转到首页
    @para: 
    @return: 跳转成功，返回True；否则返回False
    @ hongzenghui  2016-9-21
'''

def WoDe2ShouYe():
    if MainPageUI.click_firstpage_menu() is False:
        return False
    return True

def Shouye2WoDe():
    if MainPageUI.click_firstpage_menu() is False:
        return False
    return True

'''
    @功能：首页跳转“我的”页面
    @para: 
    @return: 跳转成功，返回True；否则返回False
    @chenhui  2016-9-23
'''

def ShouYe2WoDe():
    if MainPageUI.click_personal_menu() is False:
        return False
    return True

'''
    @功能：我的”页面跳转“积分商城”
    @para: 
    @return: 跳转成功，返回True；否则返回False
    @chenhui  2016-9-23
'''

def WoDe2JiFenShangCheng():
    if PersonalUI.click_point_mall() is False:
        return False
    return True

