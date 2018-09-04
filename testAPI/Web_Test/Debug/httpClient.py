# -*- coding:UTF-8 -*-
'''
Created on 2015-10-20

@author: ho
'''
import unittest
import requests
from Web_Test.CONFIG import Global
import sys

class Test(unittest.TestCase):

    
    def testName(self):
#         reload(sys)
#         sys.setdefaultencoding('utf-8')
#         timeString = time.strftime("%a %b %m %H:%M:%S")
#         yearString = time.strftime("%Y")
#         currentTime = "%s UTC+0800 %s" % (timeString,yearString)
#         print currentTime
#         response = requests.get(Global.PingAnJianSheUrl)
#         jsessionInfo = response.headers['Set-Cookie'].lstrip('JSESSIONID=') 
#         jsessionList = jsessionInfo.split(';')  
#         jsessionId =  jsessionList[0]   
#         print jsessionId
        
#         headers = {"Cookie":"JSESSIONID=%s" % jsessionId}
#         print headers
#         postData = {"password":"admin","userName":"admin"}
#         print postData
#         response1 = requests.post("%s/sessionManage/login.action" % Global.PingAnJianSheUrl,Data=postData)
#         response1.encoding = 'utf-8'
#         print response1.encoding
#         print response1.text
#         setCookieInfo = response1.headers['Set-Cookie']
#         sidInfo = setCookieInfo.split(';')
#         print sidInfo[0]
#         
#         headers = {"Cookie":sidInfo[0]}
#         print headers
#         postData = {'searchMode':'noFast_noAdvanced_search','orgId':'5','householdStaffVo.logout':'0','householdStaffVo.isDeath':'0'}
#         response1 = requests.get("%s/baseinfo/householdStaff/findHouseholdStaffByOrgId.action" % Global.PingAnJianSheUrl,params=postData,headers=headers)
#         print response1.url
#         print response1.text
#         pass
        print (sys.path)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()