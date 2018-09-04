# -*- coding: UTF-8 -*-
'''
Created on 2015-10-4

@author: ho
'''

from selenium import webdriver
import time
from Web_Test.COMMON import Log, Util, CommonUtil
from Web_Test.CONFIG.Global import LogLevel
from Web_Test.CONFIG import Global
import sys
import cx_Oracle
import os

# os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
# print sys.path
# conn = cx_Oracle.connect( "zhejiang_trunk", "zhejiang_trunk","192.168.1.240:1521/tianque")  
# cursor = conn.cursor()
# cursor.execute ("select t.ORGNAME from ORGANIZATIONS t where t.id = (select p.organizationid from USERS p where p.username = 'hjd1@hzsg')")
# rows = cursor.fetchall() 
# print rows
# print type(rows)
# print rows[0]
# print type(rows[0])
# print rows[0][0]
# cursor.close ()
# conn.close() 
orgInfo = CommonUtil.getOrgInfoByAccount(account = 'hjd1@hzsg',databaseIp = Global.PingAnJianSheDbIp, databaseInstance = Global.PingAnJianSheDbInstance, databaseUser=Global.PingAnJianSheDbUser, databasePass = Global.PingAnJianSheDbPass)
print (orgInfo['orgId'])
print (orgInfo['orgName'])
print (orgInfo['orgFullName'])
# driver = webdriver.Ie()
# driver = Util.driver_init()
# Log.LogOutput(LogLevel.DEBUG, "this is test sample")
# # driver.get("http://www.baidu.com")
# Util.open_browser()
# time.sleep(5)
# Util.wait_element_by_xpath(xpath='//*[@id="kw"]')
# driver.find_element_by_id("kw").send_keys("selenium")
# driver.find_element_by_id("su").click()
# driver.quit()