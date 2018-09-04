# -*- coding:UTF-8 -*-
'''
Created on 2016-10-14
订单确认页面相关操作
@author: chenhui
'''
from Mobile import MobileUtil
from COMMON import Log
from CONFIG.Define import LogLevel

'''
    @功能：检查兑换记录状态，过程包含了检查兑换记录
    @para: PointObject:积分对象内容
    @return: 检查成功，返回True；否则返回False
    @ chenhui  2016-9-23
'''
def check_exchange_state(PointObject):
    xpath = "//android.widget.TextView[contains(@text,'%s')]/following-sibling::android.widget.TextView[@resource-id='com.tianque.linkage:id/record_state' and @text='%s']" % (PointObject['goodsName'],PointObject['state'])
#     print xpath
    if MobileUtil.wait_element_by_xpath(xpath) is True:
        Log.LogOutput(LogLevel.DEBUG, message="检查兑换记录状态成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, message="检查兑换记录状态失败")
        return False