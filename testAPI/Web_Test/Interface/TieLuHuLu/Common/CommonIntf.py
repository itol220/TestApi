# -*- coding:UTF-8 -*-
'''
Created on 2017-7-10

@author: Administrator
'''
from CONFIG import Global
import os
import cx_Oracle

'''
    @功能：     通过域名和和显示名获取id信息
    @para: domainName: 类型所在的域名
           displayName: 类型的显示名
    @return: 返回id
    @ hongzenghui  2017-7-10
'''

def getIdByDomainAndDisplayName(domainName = None,displayName = None, databaseIp = Global.TieLuHuLuInfo['DbIp'], databaseInstance=Global.TieLuHuLuInfo['DbInstance'], databaseUser=Global.TieLuHuLuInfo['DbUser'], databasePass = Global.TieLuHuLuInfo['DbPass']):
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    conn = cx_Oracle.connect(databaseUser, databasePass,"%s:1521/%s" % (databaseIp,databaseInstance))
    cursor = conn.cursor()
    
    dbCommand = "select t.id from PROPERTYDICTS t where t.domainname = '%s' and t.displayname='%s'" % (domainName,displayName)
    print dbCommand
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
    
def clearTeamMembers( teamofficeid = None, databaseIp = Global.TieLuHuLuInfo['DbIp'], databaseInstance=Global.TieLuHuLuInfo['DbInstance'], databaseUser=Global.TieLuHuLuInfo['DbUser'], databasePass = Global.TieLuHuLuInfo['DbPass']):
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    conn = cx_Oracle.connect(databaseUser, databasePass,"%s:1521/%s" % (databaseIp,databaseInstance))
    cursor = conn.cursor()
    
    dbCommand = "update RAILWAYTEAMPERSONS t set t.isdeleted='1' where t.teamofficeid = %s" % (teamofficeid)
    print dbCommand
    #取当前用户的orgid
    cursor.execute(dbCommand)


    cursor.close ()
    #提交！！
    conn.commit()
    conn.close() 


    
    
    
    