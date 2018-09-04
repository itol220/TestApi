# -*- coding:UTF-8 -*-
'''
Created on 2018年1月4日09:40:04

@author: sunliuping
'''
# import md5
from Web_Test.CONFIG import Global
import requests
from Web_Test.COMMON import Log
from Web_Test.CONFIG.Define import LogLevel
from Web_Test.COMMON.CommonUtil import httpResponseResultDeal
import json
import hashlib
md5 = hashlib.md5()
sidNumber = None
sidNumber_21300 = None
sidNumber_21200 = None
sidNumber_21400 = None
jSessionId = None

# 全科采集21100登录
def quan_ke_cai_ji_21100_login( username = None, password = None ):
    global sidNumber
    global jSessionId
    
    # 先访问index.jsp获取同意的jsessionId
    s = requests.Session()
    indexLoginJspResponse = s.get( "%s%s/login.jsp" 
                                          % ( Global.QuanKeCaiJiInfo['QuanKeCaiJiUrlBase'],
                                              Global.QuanKeCaiJiInfo['QuanKeCaiJi21100Port'] ) )
    
    jSessionId = indexLoginJspResponse.cookies.values()[0]
    
#     m1 = md5.new()
    if username is None or password is None: 
#         m1.update( Global.QuanKeCaiJiInfo['QuanKeCaiJiPassword'] )      
#         postData = {"userName":Global.QuanKeCaiJiInfo['QuanKeCaiJiUsername'], "password":m1.hexdigest() }
        postData = {"userName":Global.QuanKeCaiJiInfo['QuanKeCaiJiUsername'],
                     "password":Global.QuanKeCaiJiInfo['QuanKeCaiJiPassword'] }
    else:
#         m1.update(password)
#         postData = {"userName":username, "password":m1.hexdigest()}
        postData = {"userName":username, "password":password}
    
#     print postData
    response = s.post( "%s/login" % 
                              Global.QuanKeCaiJiInfo['QuanKeCaiJiUrl'],
                              data = postData )
#     print response.text
    responseTextDict = json.loads( str( response.text ) )
    
    if responseTextDict.has_key( "success" ):
        if responseTextDict['success'] == 'true' or responseTextDict['success'] is True:
#             print "quan ke cai ji 21100 login success"
            setCookieInfo = response.headers['Set-Cookie']
            cookieDeal = setCookieInfo.split( ';' )
            sidNumber = cookieDeal[0]
            return True
        else:
            Log.LogOutput( LogLevel.ERROR, "全科采集21100 登录失败，请检查 登录参数信息" )
            return False
    
def quan_ke_cai_ji_21100_get( url = None,
                              param = None,
                              headers = None,
                              username = Global.PingAnJianSheUser,
                              password = Global.PingAnJianShePass ):
    global sidNumber
    if quan_ke_cai_ji_21100_login( username = username,
                                   password = password ) is True:
        headersSend = {"Cookie":sidNumber}
        if headers is not None:
            headersSend.update( headers )
        wholeUrl = "%s%s" % ( Global.QuanKeCaiJiInfo['QuanKeCaiJiUrl'], url )
#         print "请求URL：[%s],\n请求内容[%s]" % ( wholeUrl, postdata )
        response = requests.get( wholeUrl,
                                 params = param,
                                 headers = headersSend )
        return httpResponseResultDeal( response )
    else:
        raise AssertionError("Login Failed")
    
def quan_ke_cai_ji_21100_post( url = None,
                               postdata = None,
                               headers = None,
                               files = None,
                               username = Global.QuanKeCaiJiInfo['QuanKeCaiJiUsername'],
                               password = Global.QuanKeCaiJiInfo['QuanKeCaiJiPassword'] ):
    global sidNumber
    if quan_ke_cai_ji_21100_login( username = username,
                                   password = password ) is True:        
        headersSend = {"Cookie":sidNumber}
        if headers is not None:
            headersSend.update( headers )
        wholeUrl = "%s%s" % ( Global.QuanKeCaiJiInfo['QuanKeCaiJiUrl'], url )
#         print "请求URL：[%s],\n请求内容[%s]" % ( wholeUrl, postdata )
        response = requests.post( wholeUrl ,
                                  data = postdata,
                                  files = files,
                                  headers = headersSend )
        return httpResponseResultDeal( response )
    else:
        raise AssertionError("Login Failed")
    '''
    21200基本接口开始
    '''
# 全科采集21100登录
def quan_ke_cai_ji_21200_login( username = None, password = None ):
    global sidNumber_21200
    
    # 先访问index.jsp获取同意的jsessionId
    s = requests.Session()
    s.get( "%s%s/index.jsp" 
                          % ( Global.QuanKeCaiJiInfo['QuanKeCaiJiUrlBase'],
                              Global.QuanKeCaiJiInfo['QuanKeCaiJi21200Port'] ) )
    
    m1 = md5.new()
    if username is None or password is None: 
        m1.update( Global.QuanKeCaiJiInfo['QuanKeCaiJiPassword21200'] ) 
        postData = {"userName":Global.QuanKeCaiJiInfo['QuanKeCaiJiUsername21200'],
                     "password":m1.hexdigest() }
    else:
        m1.update( password )
        postData = {"userName":username, "password":password}
    
    
    
#     response = requests.post( 
    response = s.post( 
                             "%s%s/adminLogin/doLogin" % 
                             ( Global.QuanKeCaiJiInfo['QuanKeCaiJiUrlBase'],
                               Global.QuanKeCaiJiInfo['QuanKeCaiJi21200Port'] ),
                               data = postData )
#     print response.text
#     print response.url
    responseTextDict = json.loads( str( response.text ) )
    
    if responseTextDict.has_key( "success" ):
        if responseTextDict['success'] == 'true' or responseTextDict['success'] is True:
#             print "quan ke cai ji 21200 login success"
            setCookieInfo = response.headers['Set-Cookie']
#             print setCookieInfo
            cookieDeal = setCookieInfo.split( ';' )
            sidNumber_21200 = cookieDeal[0]
            return True
        else:
            Log.LogOutput( LogLevel.ERROR, "全科采集21200 登录失败，请检查 登录参数信息" )
            return False
    
def quan_ke_cai_ji_21200_get( url = None,
                              param = None,
                              headers = None,
                              username = Global.QuanKeCaiJiInfo['QuanKeCaiJiUsername21200'],
                              password = Global.QuanKeCaiJiInfo['QuanKeCaiJiPassword21200'] ):
    global sidNumber_21200
    if quan_ke_cai_ji_21200_login( username = username,
                                   password = password ) is True:
        headersSend = {"Cookie":sidNumber_21200}
        if headers is not None:
            headersSend.update( headers )
        wholeUrl = "%s%s%s" % ( Global.QuanKeCaiJiInfo['QuanKeCaiJiUrlBase'],
                                 Global.QuanKeCaiJiInfo['QuanKeCaiJi21200Port'],
                                 url )
        print ("get请求URL：[%s],\n" % ( wholeUrl ))
        response = requests.get( wholeUrl,
                                 params = param,
                                 headers = headersSend )
        return httpResponseResultDeal( response )
    else:
        raise AssertionError ("Login Failed")
    
def quan_ke_cai_ji_21200_post( url = None,
                               postdata = None,
                               headers = None,
                               files = None,
                               username = Global.QuanKeCaiJiInfo['QuanKeCaiJiUsername21200'],
                               password = Global.QuanKeCaiJiInfo['QuanKeCaiJiPassword21200'] ):
    global sidNumber_21200
    if quan_ke_cai_ji_21200_login( username = username,
                                   password = password ) is True:        
        headersSend = {"Cookie":sidNumber_21200}
#         print  "headersSend:%s" % headersSend
        if headers is not None:
            headersSend.update( headers )
        wholeUrl = "%s%s%s" % ( Global.QuanKeCaiJiInfo['QuanKeCaiJiUrlBase'],
                              Global.QuanKeCaiJiInfo['QuanKeCaiJi21200Port'],
                              url )
        
        print ("quan_ke_cai_ji_21200_post请求\nURL：[%s],\n请求内容[%s]" % ( wholeUrl, postdata ))
        response = requests.post( wholeUrl ,
                                  data = postdata,
                                  files = files,
                                  headers = headersSend )
        print ("post返回内容:%s" % response.text)
        return httpResponseResultDeal( response )
    else:
        raise AssertionError ("Login Failed")
    '''
    21200基本接口结束
    '''

# 21300登录
def quan_ke_cai_ji_21300_login( username = None, password = None ):
    global sidNumber
    global sidNumber_21300
    global jSessionId
    
    # 以21100的登录为准，拿到sid
    if quan_ke_cai_ji_21100_login( username, password ) is True:
        sidNumber_21300 = sidNumber
        headersSend = {}
#         headersSend["Cookie"] = "%s;%s" % ( sidNumber_21300, "JSESSIONID=%s" % jSessionId )
        headersSend["Cookie"] = "%s" % ( sidNumber_21300 )
        headersSend['Upgrade-Insecure-Requests'] = '1'
#         headersSend['Referer'] = "%s%s/index.jsp" % ( Global.QuanKeCaiJiInfo['QuanKeCaiJiUrlBase'], Global.QuanKeCaiJiInfo['QuanKeCaiJi21100Port'] )
        print (headersSend)
#         response = requests.get( "%s%s/adminLogin/doLogin/loginByCsid.action" % ( Global.QuanKeCaiJiInfo['QuanKeCaiJiUrlBase'], Global.QuanKeCaiJiInfo['QuanKeCaiJi21300Port'] ) , headers = headersSend )
        s = requests.Session()
        response = s.get( "%s%s/adminLogin/doLogin/loginByCsid.action" 
                          % ( Global.QuanKeCaiJiInfo['QuanKeCaiJiUrlBase'],
                               Global.QuanKeCaiJiInfo['QuanKeCaiJi21300Port'] ) , headers = headersSend )
        
        print  ("[loginByCsid.action:]%s" % response.url)
#         response = s.get( "%s%s/index.jsp;%s" % 
#                           ( Global.QuanKeCaiJiInfo['QuanKeCaiJiUrlBase'],
#                             Global.QuanKeCaiJiInfo['QuanKeCaiJi21300Port'] ,
#                                sidNumber_21300 ) )
#                           headers = headersSend )
        
#         print "[/index.jsp:]%s" % response.text
#         print "[/index.jsp:]%s" % response.content
        Log.LogOutput( LogLevel.INFO, "全科采集21100跳转21300成功" )
        return True
    Log.LogOutput( LogLevel.ERROR, "全科采集21100跳转21300失败，请检查 登录参数信息" )
    return False
        
def quan_ke_cai_ji_21300_get( url = None,
                              param = None,
                              headers = None,
                              username = Global.PingAnJianSheUser,
                              password = Global.PingAnJianShePass ):
    global sidNumber_21300
    global jSessionId
    if quan_ke_cai_ji_21300_login( username = username,
                                   password = password ) is True:
#         headersSend = {"Cookie":sidNumber_21300}
#         headersSend = {}
#         headersSend["Cookie"] = "%s;%s" % ( sidNumber_21300,
#                                             "JSESSIONID=%s" % jSessionId )
#         headersSend["Content-Type"] = "application/json;charset=UTF-8"
#         headersSend["Cookie"] = "JSESSIONID=%s" % jSessionId 
#         if headers is not None:
#             headersSend.update( headers )
        wholeUrl = "%s%s%s" % ( Global.QuanKeCaiJiInfo['QuanKeCaiJiUrlBase'] ,
                                Global.QuanKeCaiJiInfo['QuanKeCaiJi21300Port'],
                                url )
#         print "请求URL：[%s],\n请求内容[%s]" % ( wholeUrl, postdata )
        response = requests.get( wholeUrl,
                                 params = param )
#                                  headers = headersSend )
        return httpResponseResultDeal( response )
    else:
        raise AssertionError ("Login Failed")
    
def quan_ke_cai_ji_21300_post( url = None,
                               postdata = None,
                               headers = None,
                               files = None,
                               username = Global.QuanKeCaiJiInfo['QuanKeCaiJiUsername'],
                               password = Global.QuanKeCaiJiInfo['QuanKeCaiJiPassword'] ):
    global sidNumber_21300
    global jSessionId
    if quan_ke_cai_ji_21300_login( username = username,
                                   password = password ) is True:        
#         headersSend = {"Cookie":sidNumber_21300}
        headersSend = {}
#         headersSend["Cookie"] = "%s;%s" % ( sidNumber_21300, "JSESSIONID=%s" % jSessionId )
#         headersSend["Content-Type"] = "application/json;charset=UTF-8"
#         headersSend["Cookie"] = "JSESSIONID=%s" % jSessionId 
        if headers is not None:
            headersSend.update( headers )
        wholeUrl = "%s%s%s" % ( Global.QuanKeCaiJiInfo['QuanKeCaiJiUrlBase'],
                                Global.QuanKeCaiJiInfo['QuanKeCaiJi21300Port'],
                                 url )
        print ("请求URL：[%s],\n请求内容[%s]" % ( wholeUrl, postdata ))
        print (headersSend)
        response = requests.post( wholeUrl ,
                                  data = postdata,
                                  files = files,
#                                    headers = headersSend ,
                                   allow_redirects = True )
        
        print ("头%s" % response.headers)
        return httpResponseResultDeal( response )
    else:
        raise AssertionError ("Login Failed")
