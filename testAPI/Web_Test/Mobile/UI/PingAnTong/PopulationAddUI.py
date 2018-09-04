# -*- coding:UTF-8 -*-
'''
Created on 2017-10-18

@author: N-254
'''
from Mobile import MobileUtil
from COMMON import Log
from CONFIG.Define import LogLevel

'''
    @功能：     输入身份证
    @para: populationObject：事件对象  PopulationRelatePara.populationObject
    @return: 输入成功，返回True；否则返回False
    @ hongzenghui  2017-9-28
'''

def base_input_idcard_no(populationObject):
    xpath = "//android.widget.TextView[@resource-id='com.tianque.ecommunity.plugin.population:id/ap_fix_idCard']"
    if MobileUtil.click_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="点击身份证输入成功")
    else:
        Log.LogOutput(LogLevel.ERROR, message="点击身份证输入失败")
        return False
    for i in range(len(populationObject['baseInfo']['idCardNo'])):
        if populationObject['baseInfo']['idCardNo'][i] == '0':
            xpath = "//android.widget.Button[@resource-id='com.tianque.ecommunity:id/btn0']"
        elif populationObject['baseInfo']['idCardNo'][i] == '1':
            xpath = "//android.widget.Button[@resource-id='com.tianque.ecommunity:id/btn1']"
        elif populationObject['baseInfo']['idCardNo'][i] == '2':
            xpath = "//android.widget.Button[@resource-id='com.tianque.ecommunity:id/btn2']"
        elif populationObject['baseInfo']['idCardNo'][i] == '3':
            xpath = "//android.widget.Button[@resource-id='com.tianque.ecommunity:id/btn3']"
        elif populationObject['baseInfo']['idCardNo'][i] == '4':
            xpath = "//android.widget.Button[@resource-id='com.tianque.ecommunity:id/btn4']"
        elif populationObject['baseInfo']['idCardNo'][i] == '5':
            xpath = "//android.widget.Button[@resource-id='com.tianque.ecommunity:id/btn5']"
        elif populationObject['baseInfo']['idCardNo'][i] == '6':
            xpath = "//android.widget.Button[@resource-id='com.tianque.ecommunity:id/btn6']"
        elif populationObject['baseInfo']['idCardNo'][i] == '7':
            xpath = "//android.widget.Button[@resource-id='com.tianque.ecommunity:id/btn7']"
        elif populationObject['baseInfo']['idCardNo'][i] == '8':
            xpath = "//android.widget.Button[@resource-id='com.tianque.ecommunity:id/btn8']"
        elif populationObject['baseInfo']['idCardNo'][i] == '9':
            xpath = "//android.widget.Button[@resource-id='com.tianque.ecommunity:id/btn9']"
        elif populationObject['baseInfo']['idCardNo'][i] == 'X':
            xpath = "//android.widget.Button[@resource-id='com.tianque.ecommunity:id/btnX']"
        if MobileUtil.click_element_by_xpath(xpath) is False:
            Log.LogOutput(LogLevel.ERROR, message="输入身份证号失败")
            return False
    Log.LogOutput(LogLevel.DEBUG, message="输入身份证成功")
    return True