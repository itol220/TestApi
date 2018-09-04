# -*- coding:UTF-8 -*-
'''
Created on 2016-1-26

@author: N-254
'''
from Mobile.UI.PingAnTong import LoginMainUI, ShouShiSettingUI, MyWorkBenchUI
from COMMON import Log
from CONFIG.Define import LogLevel
from Mobile.Define.PingAnTong.CommonModuePara import ModuleName

'''
    @功能：     用户登录
    @para: 
    LoginCtrlDict: 登录流程控制字典
    @return: 登录成功，返回True；否则返回False
    @ hongzenghui  2016-1-26
'''

def pingantong_login(loginDict):
    #输入密码
    if loginDict['password'] is not None:
        if LoginMainUI.input_password(loginDict['password']) is False:
            return False
        
    #输入用户名
    if loginDict['username'] is not None:
        if LoginMainUI.input_username(loginDict['username']) is False:
            return False
    
    #点击登录按钮
    if LoginMainUI.click_login_button() is False:
        return False
    #手势密码处理
    if loginDict['shouShiMiMa'] is False:
        if ShouShiSettingUI.skip_setting() is False:
            return False
    #检查是否登录到主页面
    if MyWorkBenchUI.check_in_workbench() is False:
        return False
    return True

'''
    @功能：     进入不同模块
    @para: moduleName：模块名称  CommonModuePara.ModuleName
    @return: 进入成功，返回True；否则返回False
    @ hongzenghui  2017-10-18
'''

def enter_to_module(moduleName):
    if moduleName == ModuleName.SHIJIANCHULI:
        ret = MyWorkBenchUI.enter_to_issue()
    elif moduleName == ModuleName.SHIYOURENKOU:
        ret = MyWorkBenchUI.enter_to_population()
    elif moduleName == ModuleName.ZHONGDIANRENYUAN:
        ret = MyWorkBenchUI.enter_to_key_personal()
    elif moduleName == ModuleName.GUANHUAIDUIXIANG:
        ret = MyWorkBenchUI.enter_to_caring_personal()
    elif moduleName == ModuleName.SHIYOUFANGWU:
        ret = MyWorkBenchUI.enter_to_real_houses()
    elif moduleName == ModuleName.ZHONGDIANCHANGSUO:
        ret = MyWorkBenchUI.enter_to_key_place()
    elif moduleName == ModuleName.LIANGXINZUZHI:
        ret = MyWorkBenchUI.enter_to_liangxin_org()
    elif moduleName == ModuleName.QIYE:
        ret = MyWorkBenchUI.enter_to_enterprise()
    if ret is True:
        return True
    else:
        return False