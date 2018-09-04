# -*- coding:UTF-8 -*-
'''
Created on 2016-4-12

@author: N-286
'''
from __future__ import unicode_literals
from COMMON import Log
from CONFIG.Define import LogLevel
from Interface.XianSuoApp.xianSuoHttpCommon import xiansuo_post
from Interface.YunWeiPingTai.yunWeiPingTaiHttpCommon import xiansuoyunwei_post, \
    xiansuoyunwei_get
import json


'''
    @功能：线索信息统计分析
    @return:    response
    @author:  chenhui 2016-04-12
'''  
def doJob(para):
    Log.LogOutput(LogLevel.INFO, "运行线索信息统计job")
    response = xiansuoyunwei_get(url='/informationStatisticsManage/doJob', param=para)
#执行成功后，返回结果为空
    return response

'''
    @功能：线索信息统计分析
    @return:    responseDict
    @author:  chenhui 2016-04-12
'''  
def getStaticAnalysisList(para):
    Log.LogOutput(LogLevel.INFO, "获取线索统计结果列表")
    response = xiansuoyunwei_post(url='/informationStatisticsManage/findInformationStatisticsList', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "获取线索统计结果列表成功")
    else:
            Log.LogOutput(LogLevel.DEBUG, "获取线索统计结果列表失败")
    return json.loads(response.text)

'''
    @功能：对线索办结进行评分
    @return:    response
    @author:  chenhui 2016-04-12
'''  
def addScoreToClue(para):
    Log.LogOutput(LogLevel.INFO, "对办结线索进行评分")
    response = xiansuo_post(url='/api/clue/informationDubboService/updateScoreById', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "评分成功")
    else:
            Log.LogOutput(LogLevel.DEBUG, "评分失败")
    return response