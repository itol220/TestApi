# -*- coding:UTF-8 -*-
'''
Created on 2016-4-8

@author: hongzenghui
'''
from __future__ import unicode_literals
from COMMON import Log, Time
from COMMON.Time import TimeMoveType
from CONFIG import Global
from CONFIG.Define import LogLevel
from Interface.PingAnJianShe.Common import CommonIntf
from Interface.PingAnJianShe.ShiJianChuLi.ShiJianChuLiIntf import exeDbQuery
import datetime
import paramiko
import time

def getDbQueryResultYunWei(dbCommand = None, dbIp=Global.XianSuoYunWeiInfo['DbIp'], dbInstance=Global.XianSuoYunWeiInfo['DbInstance'], dbUser=Global.XianSuoYunWeiInfo['DbUser'], dbPass=Global.XianSuoYunWeiInfo['DbPass']):
    return CommonIntf.getDbQueryResult(dbCommand = dbCommand, dbIp=dbIp, dbInstance=dbInstance, dbUser=dbUser, dbPass=dbPass)

def getDbQueryResultListYunWei(dbCommand = None, dbIp=Global.XianSuoYunWeiInfo['DbIp'], dbInstance=Global.XianSuoYunWeiInfo['DbInstance'], dbUser=Global.XianSuoYunWeiInfo['DbUser'], dbPass=Global.XianSuoYunWeiInfo['DbPass']):
    return CommonIntf.getDbQueryResultList(dbCommand = dbCommand, dbIp=dbIp, dbInstance=dbInstance, dbUser=dbUser, dbPass=dbPass)

'''
    @功能：     执行SQL语句，主要是删除
    @para: command 要执行是sql语句
    @return: 
    @author: 陈辉 2015-4-11
'''
def exeDbQueryYunWei(dbCommand = None, dbIp=Global.XianSuoYunWeiInfo['DbIp'], dbInstance=Global.XianSuoYunWeiInfo['DbInstance'], dbUser=Global.XianSuoYunWeiInfo['DbUser'], dbPass=Global.XianSuoYunWeiInfo['DbPass']):
    return exeDbQuery(dbCommand = dbCommand, dbIp=dbIp, dbInstance=dbInstance, dbUser=dbUser, dbPass=dbPass)

'''
    @功能：清空数据表
    @para:
    @return:    true/false
    @author:  chenhui 2015-12-25
'''  
def clearTableYunWei(tableName=None):
    try:
        #首先确定是否存在该表
        if getDbQueryResultYunWei(dbCommand="select count(*) from user_tables u where u.TABLE_NAME='%s'"%tableName.upper())==0:
            Log.LogOutput(LogLevel.ERROR,message='该表不存在，请先创建表！')
        #删除前先查询表，如果本身不存在数据，那么跳过
        rs0=getDbQueryResultYunWei(dbCommand = "select count(*) from %s"%tableName)
        if rs0!=0:
            #删除表数据
            Log.LogOutput(LogLevel.DEBUG,'表中存在数据，正在清除表'+tableName)
            exeDbQueryYunWei(dbCommand ="delete from %s"%tableName)
            #查询表数据
            rs=getDbQueryResultYunWei(dbCommand = "select count(*) from %s"%tableName)
            if rs ==0:
                Log.LogOutput(message=tableName+'表数据已成功清除！')
            else:
                Log.LogOutput(LogLevel.ERROR,message=tableName+'表中仍然有'+str(rs)+'条数据，清除失败！')
    except Exception,e :
            Log.LogOutput(LogLevel.ERROR, '清除'+tableName+'表数据过程出现异常！'+str(e))

'''
    @功能：     获取linux应用服务器日期和时间
    @para:
    username:用户名
    password:密码
    @return: 返回日期格式  “2015-11-10 15:09:00”
    @ hongzenghui  2015-11-10
'''

def getLinuxDateAndTimeYunWei(username="root",password=Global.XianSuoYunWeiInfo['ServRootPass'],serverIp=Global.XianSuoYunWeiInfo['XianSuoYunWeiUrl']):
    serverIp = serverIp.split(':',2)[1].lstrip('/')
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
    @功能：设置运维平台服务器的时间
    @para:Data='2016-1-27 18:18:18'         
    @return:返回延迟后的时间，格式为%s%m%h * * ?
    @author:  chenhui 2016-4-12
'''  
def setLinuxTimeYunWei (data,username="root",password=Global.XianSuoYunWeiInfo['ServRootPass'],serverIp=Global.XianSuoYunWeiInfo['XianSuoYunWeiUrl']):
    newServerIp = serverIp.split(':',2)[1].lstrip('/')#'anhaooray.oicp.net'
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(newServerIp, 22, username=username, password=password, timeout=4)
    print u"[%s][INFO][%s]" % (time.strftime('%Y-%m-%d %H:%M:%S'),u"当前服务器时间为： %s" % getLinuxDateAndTimeYunWei(username=username,password=password,serverIp=serverIp))
    command='date -s  "%s"'%data
    stdin,stdout,stderr=client.exec_command(command)
    retLines = stdout.readlines()
    client.close()
    print u"[%s][INFO][%s]" % (time.strftime('%Y-%m-%d %H:%M:%S'),u"修改后linux服务器时间为: %s" % getLinuxDateAndTimeYunWei(username=username,password=password,serverIp=serverIp))
    
'''
    @功能：根据pc上当前日期，来设置运维平台服务器当前周的周几
    @para:    weekday=0,1,2,3...7数字,代表周一~周日,如果输入0，则设置为pc上的当前日期
    @return:返回延迟后的时间，格式为%s%m%h * * ?
    @author:  chenhui 2016-11-30
'''  
def setWeekdayOnYunWeiLinuxServer (weekday,username="root",password=Global.XianSuoYunWeiInfo['ServRootPass'],serverIp=Global.XianSuoYunWeiInfo['XianSuoYunWeiUrl']):
    if weekday>7 or weekday<0:
        raise Exception("参数错误，weekday只能输入0-7的整数")
    #从pc端获取当前标准时间
    data=Time.getCurrentDateAndTime()
    #获取今天周几数，1代表周一
    todayWeekNo=datetime.datetime.now().weekday()+1
    if weekday<todayWeekNo:
        strDstDateTime=Time.moveTime(data, todayWeekNo-weekday,moveType=TimeMoveType.MINUS)
    elif weekday>todayWeekNo:
        strDstDateTime=Time.moveTime(data, weekday-todayWeekNo,moveType=TimeMoveType.PLUS)
    else:
        strDstDateTime=data
    newServerIp = serverIp.split(':',2)[1].lstrip('/')#'anhaooray.oicp.net'
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(newServerIp, 22, username=username, password=password, timeout=4)
    print u"[%s][INFO][%s]" % (time.strftime('%Y-%m-%d %H:%M:%S'),u"当前服务器时间为： %s" % getLinuxDateAndTimeYunWei(username=username,password=password,serverIp=serverIp))
    command='date -s  "%s"'%strDstDateTime
    stdin,stdout,stderr=client.exec_command(command)
    retLines = stdout.readlines()
    client.close()
    print u"[%s][INFO][%s]" % (time.strftime('%Y-%m-%d %H:%M:%S'),u"修改后linux服务器时间为: %s" % getLinuxDateAndTimeYunWei(username=username,password=password,serverIp=serverIp))