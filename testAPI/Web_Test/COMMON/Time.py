# -*- coding: UTF-8 -*-
'''
Created on 2015-11-10

@author: N-254
'''
from Web_Test.CONFIG import Global
from Web_Test.Interface.PingAnJianShe.Common.CommonIntf import getDbQueryResult
import datetime
import paramiko
import time

def enum(**enums):
    return type('Enum', (), enums)

TimeMoveType = enum(PLUS=0,MINUS=1)
TimeCalcType = enum(WORKDAY=0,CALENDARDAY=1)

'''
    @功能：     时间等待
    @para:
    second: 要等待的秒数
    @return: 
    @ hongzenghui  2016-1-13
'''
def wait(second = None):
    print (u"[%s][INFO][等待%s秒...]" % (time.strftime("%Y-%m-%d %H:%M:%S"),second))
    time.sleep(second)
    
'''
    @功能：     查询当前日期
    @para:
    @return: 返回日期格式  “2015-11-10”
    @ hongzenghui  2015-11-10
'''

def getCurrentDate():
    return time.strftime("%Y-%m-%d")

'''
    @功能：     查询当前时间
    @para:
    @return: 返回日期格式  “2015-11-10”
    @ hongzenghui  2015-11-10
'''

def getCurrentTime():
    return time.strftime("%H:%M:%S")

'''
    @功能：     查询当前日期和时间
    @para:
    @return: 返回日期格式  “2015-11-10 15:09:00”
    @ hongzenghui  2015-11-10
'''

def getCurrentDateAndTime():
    return time.strftime("%Y-%m-%d %H:%M:%S")

'''
    @功能：     查询linux应用服务器日期和时间
    @para:
    username:用户名
    password:密码
    @return: 返回日期格式  “2015-11-10 15:09:00”
    @ hongzenghui  2015-11-10
'''

def getLinuxDateAndTime(username="root",password=Global.PingAnJianSheAppServRootPass):
    serverIp = Global.PingAnJianSheUrl.split(':',2)[1].lstrip('/')
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(serverIp, 22, username=username, password=password, timeout=4)
    stdin, stdout, stderr = client.exec_command('date "+%Y-%m-%d %H:%M:%S"')
    retLines = stdout.readlines()
#     for std in retLines:
#         retTime = std,
    client.close()
    return retLines[0].replace("\n","")

'''
    @功能：     在指定时间基础上往前或往后推特定时间
    @para:
    standardTime: 基准时间,格式为 “2015-11-11 20:01:01”
    addDay: 时间移动天数，默认为0
    addHour:时间移动小时数，默认为0
    addMinute:时间移动分数，默认为0
    addSecond:时间移动秒数，默认为0
    moveType: 时间移动类型，如果为PLUS，即时间往后推;如果为MINUS，则时间往前移，默认为MINUS
    calcType: 时间计算类型，如果为WORKDAY，即按照工作日算;如果为CALENDARDAY，即按照自然日计算，默认为CALENDARDAY
    @return: 返回时间格式  “2015-11-10 15:09:00”
    @ hongzenghui  2015-12-14
'''

def moveTime(standardTime=None,addDay=0,addHour=0,addMinute=0,addSecond=0,moveType=TimeMoveType.PLUS,calcType=TimeCalcType.CALENDARDAY):
    dateStandardTime = datetime.datetime.strptime(standardTime, "%Y-%m-%d %H:%M:%S")
    moveSeconds = addHour*3600 + addMinute*60 + addSecond
    actualDay = addDay
    if calcType == TimeCalcType.WORKDAY: #按照工作日计算       
        if addDay == 0:
#             Log.LogOutput(level=LogLevel.WARN, message='按照工作日方式统计，天数不可为0')
            print (u"[%s][WARN][按照工作日方式统计，天数不可为0]" % time.strftime("%Y-%m-%d %H:%M:%S"))
            return None
        else:
            actualDay = 0
            day=0
            dstDateTime = dateStandardTime
            strDstDateTime = None            
            while day!=addDay:
                if moveType == TimeMoveType.PLUS:
                    dstDateTime = dstDateTime + datetime.timedelta(days = 1)
                else:
                    dstDateTime = dstDateTime + datetime.timedelta(days = -1)
                strDstDateTime = dstDateTime.strftime("%Y-%m-%d")                
                dbCommand = "select * from WORKCALENDARS t where t.actualdate = to_date('%s','yyyy-mm-dd') and t.holiday <>7 and t.holiday<>1" % strDstDateTime
                if getDbQueryResult(dbCommand) is not None: 
                    day = day + 1
                actualDay = actualDay + 1
    if moveType == TimeMoveType.PLUS:
        dstDateTime = dateStandardTime + datetime.timedelta(days = actualDay,seconds=moveSeconds) 
    else:
        dstDateTime = dateStandardTime + datetime.timedelta(days = 0-actualDay,seconds=0-moveSeconds)
    strDstDateTime = dstDateTime.strftime("%Y-%m-%d %H:%M:%S")
    return strDstDateTime


'''
    @功能：在原有功能基础上增加了返回格式参数，以便根据需要的格式进行返回
    @para:
    standardTime: 基准时间,格式为 “2015-11-11 20:01:01”
    addDay: 时间移动天数，默认为0
    addHour:时间移动小时数，默认为0
    addMinute:时间移动分数，默认为0
    addSecond:时间移动秒数，默认为0
    moveType: 时间移动类型，如果为PLUS，即时间往后推;如果为MINUS，则时间往前移，默认为MINUS
    calcType: 时间计算类型，如果为WORKDAY，即按照工作日算;如果为CALENDARDAY，即按照自然日计算，默认为CALENDARDAY
    @return: 返回时间格式  自定义，默认返回格式为“%Y-%m-%d”
    @ chenhui  2016-4-19
'''
def moveTime2(standardTime=None,addDay=0,addHour=0,addMinute=0,addSecond=0,moveType=TimeMoveType.MINUS,calcType=TimeCalcType.CALENDARDAY,returnFormat="%Y-%m-%d"):
    dateStandardTime = datetime.datetime.strptime(standardTime, "%Y-%m-%d %H:%M:%S")
    moveSeconds = addHour*3600 + addMinute*60 + addSecond
    actualDay = addDay
    if calcType == TimeCalcType.WORKDAY: #按照工作日计算       
        if addDay == 0:
#             Log.LogOutput(level=LogLevel.WARN, message='按照工作日方式统计，天数不可为0')
            print (u"[%s][WARN][按照工作日方式统计，天数不可为0]" % time.strftime("%Y-%m-%d %H:%M:%S"))
            return None
        else:
            actualDay = 0
            day=0
            dstDateTime = dateStandardTime
            strDstDateTime = None            
            while day!=addDay:
                if moveType == TimeMoveType.PLUS:
                    dstDateTime = dstDateTime + datetime.timedelta(days = 1)
                else:
                    dstDateTime = dstDateTime + datetime.timedelta(days = -1)
                strDstDateTime = dstDateTime.strftime("%Y-%m-%d")                
                dbCommand = "select * from WORKCALENDARS t where t.actualdate = to_date('%s','yyyy-mm-dd') and t.holiday <>7 and t.holiday<>1" % strDstDateTime
                if getDbQueryResult(dbCommand) is not None: 
                    day = day + 1
                actualDay = actualDay + 1
    if moveType == TimeMoveType.PLUS:
        dstDateTime = dateStandardTime + datetime.timedelta(days = actualDay,seconds=moveSeconds) 
    else:
        dstDateTime = dateStandardTime + datetime.timedelta(days = 0-actualDay,seconds=0-moveSeconds)
    strDstDateTime = dstDateTime.strftime(returnFormat)
    return strDstDateTime

'''
    @功能：设置服务器的时间
    @para:Data='2016-1-27 18:18:18'         
    @return:返回延迟后的时间，格式为%s%m%h * * ?
    @author:  chenhui 2016-1-18
'''  
def setLinuxTime (data,username="root",password=Global.PingAnJianSheAppServRootPass):
    serverIp = Global.PingAnJianSheUrl.split(':',2)[1].lstrip('/')#'anhaooray.oicp.net'
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(serverIp, 22, username=username, password=password, timeout=4)
    print (u"[%s][INFO][%s]" % (time.strftime('%Y-%m-%d %H:%M:%S'),u"当前服务器时间为： %s" % getLinuxDateAndTime()))
    command='date -s  "%s"'%data
    stdin,stdout,stderr=client.exec_command(command)
    retLines = stdout.readlines()
    client.close()
    print (u"[%s][INFO][%s]" % (time.strftime('%Y-%m-%d %H:%M:%S'),u"修改后linux服务器时间为: %s" % getLinuxDateAndTime()))
            