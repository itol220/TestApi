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
    @功能： 新增用户统计表
    @para: 用户统计表dict
    username:用户名
    password:密码
    @return: 如果添加成功，则返回True；否则返回False  
'''    
def addUserReportTask( addUserReportTaskDict, toCheckMessage = None , username = None, password = None ):
    Log.LogOutput( LogLevel.INFO, "新增用户统计表开始" )
#     TeamOfficeDict['railwayTeamOffice.railwayTeamPerson.jobRank.id'] = TeamOfficeDict['railwayTeamOffice.jobRanks.id']  
    response = QuanKeCaiJiHttpCommon.quan_ke_cai_ji_21300_post( "/userReportTask/addUserReportTask", addUserReportTaskDict, username = username, password = password )
    if response.result is True:
        Log.LogOutput( LogLevel.INFO, "新增用户统计表成功" )
        
        # 有的时候，操作成功，响应中有些关键字段信息也要检查
        if toCheckMessage is not None:
            return Util.checkMessageInHttpResponse( response, toCheckMessage )
        
        return json.loads( response.text )
    else:
        Log.LogOutput( LogLevel.ERROR, "新增用户统计表失败" )
        if toCheckMessage is  None:
            return False
        
        return Util.checkMessageInHttpResponse( response, toCheckMessage )
