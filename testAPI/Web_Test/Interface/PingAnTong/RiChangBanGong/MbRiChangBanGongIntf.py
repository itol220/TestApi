# -*- coding:UTF-8 -*-
'''
Created on 2016-3-7

@author: N-286
'''
from __future__ import unicode_literals
from Web_Test.COMMON import Log, CommonUtil
from Web_Test.CONFIG.Define import LogLevel
from Web_Test.CONFIG.Global import simulationEnvironment
from Web_Test.CONFIG.InitDefaultPara import userInit
from Web_Test.Interface.PingAnJianShe.RiChangBanGong.RiChangBanGongIntf import \
    richangBanGongInitEnv
from Web_Test.Interface.PingAnJianShe.ShiJianChuLi.ShiJianChuLiIntf import clearTable
from Web_Test.Interface.PingAnTong.pingAnTongHttpCommon import pingantong_post, \
    pingantong_get
import json

#不可用于仿真环境
def MbRiChangBanGongInit():
    #加仿真环境判断，防止误操作
    if simulationEnvironment is False:
        #工作日志附件和数据表
        clearTable(tableName='WORKDIARYLOGATTACHFILES')
        clearTable(tableName='workdiarys')
        #会议活动文件其他附件和数据表
        clearTable(tableName='NEWDAILYLOGATTACHFILES')
        clearTable(tableName='newWorkingRecords')
        richangBanGongInitEnv()
    pass

'''
    @功能：手机新增工作日志
    @para:issueAddPara
    @return:    true/false
    @author:  chenhui 2016-3-7
'''  
def mAddWorkDiary(para=None, username = userInit['DftJieDaoUser'], password = '11111111'):
    Log.LogOutput(level=LogLevel.INFO, message='新增工作日志')
    response = pingantong_get(url='/mobile/dailyLogWorkDiaryManage/addWorkDiary.action', param=para, username=username, password=password)
#     Log.LogOutput(LogLevel.DEBUG,response.text)
    return response

'''
    @功能：手机工作日志列表显示
    @para:
    @return:    response
    @author:  chenhui 2016-3-7
'''  
def mWorkDairyList(para, username = userInit['DftJieDaoUser'], password = '11111111'):
    Log.LogOutput(level=LogLevel.DEBUG, message='显示工作日志列表数据')
    response = pingantong_post(url='/mobile/dailyLogWorkDiaryManage/searchWorkDiary.action', postdata=para, username=username, password=password)
#     Log.LogOutput(LogLevel.DEBUG,response.text)
    return response

'''
    @功能：检查工作日志是否存在于列表中
    @para:checkPara:{workUserName,workPlace,workTime,workTime}
    @param 
    @return:    true/false
    @author:  chenhui 2016-3-7
'''  
def mCheckWorkDairyInList(checkPara,listPara,username=userInit['DftJieDaoUser'],password='11111111'):
    try:
        response=mWorkDairyList(para=listPara,username=username)
        Log.LogOutput( message='正在验证工作日志列表是否存在待检查日志')
        if response.result is False:
            Log.LogOutput(LogLevel.ERROR,'请求结果异常，请检查输入参数listPara')
            return False
        responseDict = json.loads(response.text)
#         Log.LogOutput(level=LogLevel.DEBUG, message=response.text)
        if responseDict['records']==0:
            Log.LogOutput(LogLevel.DEBUG,'列表数据为空！')
            return False
        else:
            listDict = responseDict['rows']
            if CommonUtil.findDictInDictlist(checkPara, listDict) is True:
                Log.LogOutput(message='列表有数据，并且查找数据成功')
                return True
            else:
                Log.LogOutput(message="列表有数据，但是查找数据失败")
#                 Log.LogOutput(level=LogLevel.DEBUG, message=response.text)
                return False
    except Exception as e :
        Log.LogOutput(LogLevel.ERROR, '验证出现异常！'+str(e))    
        return False
    
'''
    @功能：手机修改工作日志
    @para:
    @return:    true/false
    @author:  chenhui 2016-3-7
'''  
def mUpdWorkDiary(para=None, username = userInit['DftJieDaoUser'], password = '11111111'):
    Log.LogOutput(level=LogLevel.INFO, message='修改工作日志')
    response = pingantong_get(url='/mobile/dailyLogWorkDiaryManage/updateWorkDiary.action', param=para, username=username, password=password)
#    Log.LogOutput(LogLevel.DEBUG,response.text)
    return response

'''
    @功能：手机查看工作日志
    @para:
    @return:    true/false
    @author:  chenhui 2016-3-7
'''  
def mViewWorkDiary(para=None, username = userInit['DftJieDaoUser'], password = '11111111'):
    Log.LogOutput(level=LogLevel.INFO, message='查看工作日志')
    response = pingantong_get(url='/mobile/dailyLogWorkDiaryManage/getWorkDiaryById.action', param=para, username=username, password=password)
#     Log.LogOutput(LogLevel.DEBUG,response.text)
    return response

'''
    @功能：检查工作日志是否存在于查看页面
    @para:checkPara:{workUserName,workPlace,workTime,workTime}
    @param 
    @return:    true/false
    @author:  chenhui 2016-3-7
'''  
def mCheckWorkDairyInViewpage(checkPara,viewPara,username=userInit['DftJieDaoUser'],password='11111111'):
    try:
        response=mViewWorkDiary(para=viewPara,username=username)
        Log.LogOutput( message='正在验证工作日志查看页面是否存在待检查日志')
        if response.result is False:
            Log.LogOutput(LogLevel.ERROR,'请求结果异常，请检查输入参数viewPara')
            return False
        responseDict = json.loads(response.text)
#         Log.LogOutput(level=LogLevel.DEBUG, message=response.text)
        if findDic1tInDict2(checkPara, responseDict) is True:
            Log.LogOutput(message='查找数据成功')
            return True
        else:
            Log.LogOutput(message="查找数据失败")
            Log.LogOutput(level=LogLevel.DEBUG, message=response.text)
            return False
    except Exception as e :
        Log.LogOutput(LogLevel.ERROR, '验证出现异常！'+str(e))    
        return False
    
'''
    @功能：     比较两个字典Dict1和Dict2的键值
    @para: 
    Dict1: 待比较的字典 或者字典列表
    Dict: 待查找的字典
    @return: 如果Dict2中包含Dict1中所有不为None的键，且键值相同，则返回True；否则返回False   
'''
def findDic1tInDict2(Dict1,Dict2):
    compareResult = False
#     for dictItem in DictList:
    itemExist = 0
    for (d,x) in Dict1.items():
        if x is None:
            continue
        keyValue = (d,x)
        if Dict2.items().count(keyValue) > 0:
            continue
        else:
            itemExist = -1
            break
    if itemExist == 0:
        compareResult = True     
    return compareResult

'''
    @功能：手机新增工作台账
    @para:issueAddPara
    @return:    true/false
    @author:  chenhui 2016-3-8
'''  
def mAddMeet(para=None, username = userInit['DftJieDaoUser'], password = '11111111'):
    Log.LogOutput(level=LogLevel.INFO, message='新增工作台账')
    response = pingantong_post(url='/mobile/workingRecordMobileManage/addNewWorkingRecordForMobile.action', postdata=para, username=username, password=password)
#    print response.text
    Log.LogOutput(LogLevel.DEBUG,response.text)
    return response    

'''
    @功能：手机修改会议
    @para:
    @return:    true/false
    @author:  chenhui 2016-3-8
'''  
def mUpdMeet(para=None, username = userInit['DftJieDaoUser'], password = '11111111'):
    Log.LogOutput(level=LogLevel.INFO, message='修改工作台账')
    response = pingantong_get(url='/mobile/workingRecordMobileManage/updateNewWorkingRecordForMobile.action', param=para, username=username, password=password)
#     Log.LogOutput(LogLevel.DEBUG,'修改会议'+response.text)
    return response

'''
    @功能：手机会议列表显示
    @para:
    @return:    response
    @author:  chenhui 2016-3-8
'''  
def mMeetList(para, username = userInit['DftJieDaoUser'], password = '11111111'):
    Log.LogOutput(level=LogLevel.DEBUG, message='显示工作台账列表数据')
    response = pingantong_post(url='/mobile/workingRecordMobileManage/findNewWorkingRecordForMobile.action', postdata=para, username=username, password=password)
#     Log.LogOutput(LogLevel.DEBUG,response.text)
    return response

'''
    @功能：检查工作台账是否存在于列表中
    @para:checkPara:{name,content}
    @param 
    @return:    true/false
    @author:  chenhui 2016-3-8
'''  
def mCheckMeetInList(checkPara,listPara,username=userInit['DftJieDaoUser'],password='11111111'):
    try:
        response=mMeetList(para=listPara,username=username)
#         print response.text
        Log.LogOutput( message='正在验证工作台账列表是否存在待检查数据')
        if response.result is False:
            Log.LogOutput(LogLevel.ERROR,'请求结果异常，请检查输入参数listPara')
            return False
        responseDict = json.loads(response.text)
#         Log.LogOutput(level=LogLevel.DEBUG, message=response.text)
        if responseDict['records']==0:
            Log.LogOutput(LogLevel.DEBUG,'列表数据为空！')
            return False
        else:
            listDict = responseDict['rows']
            if CommonUtil.findDictInDictlist(checkPara, listDict) is True:
                Log.LogOutput(message='列表有数据，并且查找数据成功')
                return True
            else:
                Log.LogOutput(message="列表有数据，但是查找数据失败")
#                 Log.LogOutput(level=LogLevel.DEBUG, message=response.text)
                return False
    except Exception as e :
        Log.LogOutput(LogLevel.ERROR, '验证出现异常！'+str(e))    
        return False