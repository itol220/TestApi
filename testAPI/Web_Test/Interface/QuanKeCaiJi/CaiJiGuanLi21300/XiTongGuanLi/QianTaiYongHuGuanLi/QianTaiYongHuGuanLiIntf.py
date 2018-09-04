# -*- coding:UTF-8 -*-
'''
Created on 2018年1月4日11:04:48

@author: slp
'''
from COMMON import Log
from CONFIG.Define import LogLevel
import json
from Interface.QuanKeCaiJi.common import QuanKeCaiJiHttpCommon

'''
    @功能： 新增留言
    @para: 留言dict
    username:用户名
    password:密码
    @return: 如果添加成功，则返回True；否则返回False  
'''    
def leave_message( leaveMessageDict, toCheckMessage = None , username = None, password = None ):
    Log.LogOutput( LogLevel.INFO, "留言开始" )
#     TeamOfficeDict['railwayTeamOffice.railwayTeamPerson.jobRank.id'] = TeamOfficeDict['railwayTeamOffice.jobRanks.id']  
    response = QuanKeCaiJiHttpCommon.quan_ke_cai_ji_post( url = '/leaveMessage/addLeaveMessage', postdata = leaveMessageDict, username = username, password = password )
    if response.result is True:
        Log.LogOutput( LogLevel.INFO, "新增留言成功" )
        return json.loads( response.text )
    else:
        Log.LogOutput( LogLevel.ERROR, "新增留言失败" )
        if toCheckMessage is  None:
            return False
        
        Log.LogOutput( LogLevel.DEBUG, "\n需要检查提示信息，\n响应：[%s],\n待检查信息：[%s]," % ( response.text, toCheckMessage ) )
        if toCheckMessage in response.text:
            Log.LogOutput( LogLevel.INFO, "检查成功!!!" )
            return True
        else:
            Log.LogOutput( LogLevel.ERROR, "检查失败!!!" )
            return False
