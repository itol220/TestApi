# -*- coding:UTF-8 -*-
'''
Created on 2015-11-10

@author: N-254
'''
from Web_Test.CONFIG import Global
import os
import cx_Oracle

'''
    @功能：     获取sql查询语句的返回值
    @para: command 带执行的db查询
    @return: 存在返回第一个字段值,否则返回None
    @ hongzenghui  2015-11-10
'''

def getDbQueryResult(dbCommand = None, dbIp=Global.PingAnJianSheDbIp, dbInstance=Global.PingAnJianSheDbInstance, dbUser=Global.PingAnJianSheDbUser, dbPass=Global.PingAnJianSheDbPass):
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    conn = cx_Oracle.connect(dbUser, dbPass,"%s:1521/%s" % (dbIp,dbInstance))
    cursor = conn.cursor()
    #取当前用户的orgid
    cursor.execute(dbCommand)
    exeRet = cursor.fetchone()
    cursor.close ()
    conn.close() 
    if exeRet is None:
#         Log.LogOutput(level=LogLevel.INFO, message = "无法找到相应记录")
        return None
    else:
#         Log.LogOutput(level=LogLevel.INFO, message = "找到相应记录")
        return exeRet[0]



'''
    @功能：     获取sql查询语句的多个返回值
    @para: command 带执行的db查询
    @return: 存在返回第一个字段值,否则返回None
    @ lhz  2015-11-23
'''

def getDbQueryResultList(dbCommand = None, dbIp=Global.PingAnJianSheDbIp, dbInstance=Global.PingAnJianSheDbInstance, dbUser=Global.PingAnJianSheDbUser, dbPass=Global.PingAnJianSheDbPass):
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    conn = cx_Oracle.connect(dbUser, dbPass,"%s:1521/%s" % (dbIp,dbInstance))
    #conn = cx_Oracle.connect(dbUser, dbPass,"%s:21521/%s" % ('anhaooray.oicp.net',dbInstance))
    cursor = conn.cursor()
    #取当前用户的orgid
    cursor.execute(dbCommand)
    exeRet = cursor.fetchmany(500)
    cursor.close ()
    conn.close() 
    if exeRet is None:
#         Log.LogOutput(level=LogLevel.INFO, message = "无法找到相应记录")
        return None
    else:
#         Log.LogOutput(level=LogLevel.INFO, message = "找到相应记录")
        return exeRet
'''
    @功能：     通过域名和和显示名获取id信息
    @para: domainName: 类型所在的域名
           displayName: 类型的显示名
    @return: 返回id
    @ hongzenghui  2015-11-10
'''

def getIdByDomainAndDisplayName(domainName = None,displayName = None, databaseIp = Global.PingAnJianSheDbIp, databaseInstance=Global.PingAnJianSheDbInstance, databaseUser=Global.PingAnJianSheDbUser, databasePass = Global.PingAnJianSheDbPass):
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    conn = cx_Oracle.connect(databaseUser, databasePass,"%s:1521/%s" % (databaseIp,databaseInstance))
    cursor = conn.cursor()
    
    dbCommand = "select t.id from PROPERTYDICTS t where t.propertydomainid = (select p.id from PROPERTYDOMAINS p where p.domainname='%s') and t.displayname='%s'" % (domainName,displayName)
    #取当前用户的orgid
    cursor.execute(dbCommand)
    exeRet = cursor.fetchone()
    if exeRet is None:
        return None
    else:
#         print exeRet[0]
        cursor.close ()
        conn.close() 
        return exeRet[0]

'''
    @功能：     通过账号查询org信息
    @para: account: 待查询的账号
    @return: 返回一个dict,内容包含orgId、orgName、orgFullName三个字段   
    @ hongzenghui  2015-11-10
'''

def getOrgInfoByAccount(account = None,databaseIp = Global.PingAnJianSheDbIp, databaseInstance=Global.PingAnJianSheDbInstance, databaseUser=Global.PingAnJianSheDbUser, databasePass = Global.PingAnJianSheDbPass):
    orgInfo = {'orgId':None,
               'orgName':None,
               'orgFullPathName':None
               }
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    conn = cx_Oracle.connect(databaseUser, databasePass,"%s:1521/%s" % (databaseIp,databaseInstance))
    cursor = conn.cursor()
    #取当前用户的orgid
    cursor.execute("select p.organizationid from USERS p where p.username='%s'" % account)
    exeRet = cursor.fetchone()
    orgInfo['orgId'] = exeRet[0]
    #取当前用户的orgName
    cursor.execute("select t.ORGNAME from ORGANIZATIONS t where t.id = (select p.organizationid from USERS p where p.username = '%s')" % account)
    exeRet = cursor.fetchone()
    orgInfo['orgName'] = exeRet[0]
#     Log.LogOutput(LogLevel.INFO, "ORGNAME：%s" % orgInfo['orgName'])
    #取当前用户全路径的orgName，格式为 A->B->C->D
    cursor.execute("select t.parentid from ORGANIZATIONS t where t.id = '%s'"  % orgInfo['orgId'])
    exeRet = cursor.fetchone()
    parentId = exeRet[0]
    orgInfo['orgFullName'] = orgInfo['orgName']
    while(parentId!=1):
        cursor.execute("select t.ORGNAME from ORGANIZATIONS t where t.id = '%s'" % parentId)
        exeRet = cursor.fetchone()
        orgInfo['orgFullName'] = "%s->%s" % (exeRet[0],orgInfo['orgFullName'])
        if exeRet[0]=="中国":
            break
        cursor.execute("select t.parentid from ORGANIZATIONS t where t.id = '%s'" % parentId)
        exeRet = cursor.fetchone()
        parentId = exeRet[0]
    cursor.close ()
    conn.close() 
    return orgInfo