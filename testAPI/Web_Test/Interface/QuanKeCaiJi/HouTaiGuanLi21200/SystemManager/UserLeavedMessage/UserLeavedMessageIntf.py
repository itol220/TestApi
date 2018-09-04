# -*- coding:UTF-8 -*-
'''
Created on 2018年1月5日15:48:02

@author: slp
'''
from COMMON import Log, CommonUtil
from CONFIG.Define import LogLevel
import json
from Interface.QuanKeCaiJi.common import QuanKeCaiJiHttpCommon
from Interface.QuanKeCaiJi.HouTaiGuanLi21200.SystemManager.UserLeavedMessage import UserLeavedMessagePara

'''
@attention: 
@see:  查询留言列表
@since: 2018年1月5日16:35:35
@author: 孙留平
'''
def searchUserLeavedMessageList( searchUserLeavedMessageDict = None,
                                 username = None,
                                 password = None ):
    Log.LogOutput( LogLevel.INFO, "开始查询留言信息列表" )
    
    if searchUserLeavedMessageDict is None:
        searchUserLeavedMessageDict = UserLeavedMessagePara.searchUserLeavedMessageDict
    
    response = QuanKeCaiJiHttpCommon.quan_ke_cai_ji_21200_post( 
               "/leaveMessage/searchLeaveMessage",
                searchUserLeavedMessageDict,
                username = username,
                password = password )
    
    if response.result is True:
        Log.LogOutput( LogLevel.INFO, "查询留言信息列表成功" )
        
        leavedMessageList = json.loads( response.text )
        Log.LogOutput( LogLevel.DEBUG,
                        "查询到的留言信息列表:\n%s" % leavedMessageList )
        return leavedMessageList
    else:
        Log.LogOutput( LogLevel.ERROR, "查询留言信息列表失败" )
        return False

'''
@see:  检查留言信息中是否存在一条记录
@since: 2018年1月5日16:35:21
@author: 孙留平
'''
def checkMessageInLeavedMessageList(
                                 toCheckMessageDict ,
                                 leavedMessageList = None,
                                 username = None,
                                 password = None):
    if leavedMessageList is None:
        leavedMessageList = searchUserLeavedMessageList()
    
    if leavedMessageList is False:
        return False
    
#     leavedMessageList = json.loads( leavedMessageList['rows'] )
    
    result = CommonUtil.findDictInDictlist( toCheckMessageDict,
                                          leavedMessageList['rows'] )
    if result is False:
        Log.LogOutput( LogLevel.ERROR, "在【%s】中查找【%s】失败" % 
                        ( leavedMessageList, toCheckMessageDict ) )
    else :
        Log.LogOutput( LogLevel.DEBUG, "在【%s】中查找【%s】成功" % 
                        ( leavedMessageList, toCheckMessageDict ) )
    return result
