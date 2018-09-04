# -*- coding:UTF-8 -*-
'''
Created on 2018年1月4日11:04:48

@author: slp
'''
from Web_Test.COMMON import Log, Util
from Web_Test.CONFIG.Define import LogLevel
import json
from Web_Test.Interface.QuanKeCaiJi.common import QuanKeCaiJiHttpCommon

'''
    @功能： 新增留言
    @para: 留言dict
    username:用户名
    password:密码
    @return: 如果添加成功，则返回True；否则返回False  
'''    
def leave_message( leaveMessageDict, toCheckMessage = None , username = None, password = None ):
    Log.LogOutput( LogLevel.INFO, "留言方法开始" )
#     TeamOfficeDict['railwayTeamOffice.railwayTeamPerson.jobRank.id'] = TeamOfficeDict['railwayTeamOffice.jobRanks.id']  
    response = QuanKeCaiJiHttpCommon.quan_ke_cai_ji_21100_post( url = '/leaveMessage/addLeaveMessage', postdata = leaveMessageDict, username = username, password = password )
    if response.result is True:
        Log.LogOutput( LogLevel.INFO, "新增留言成功" )
        
        if toCheckMessage is None:
            return json.loads( response.text )
        else:
            return Util.checkMessageInHttpResponse( response, toCheckMessage )
    else:
        Log.LogOutput( LogLevel.ERROR, "新增留言失败" )
        if toCheckMessage is  None:
            return False
        return Util.checkMessageInHttpResponse( response, toCheckMessage )
        
        
