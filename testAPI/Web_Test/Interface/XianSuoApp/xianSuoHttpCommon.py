# -*- coding:UTF-8 -*-
'''
Created on 2016-1-27

@author: hongzenghui
'''
from __future__ import unicode_literals
from COMMON import Log
from COMMON.CommonUtil import httpResponseResultDeal
from CONFIG import Global
from CONFIG.Define import LogLevel
from pydes import pyDes
import binascii
import copy
import json
import md5
import requests

sidNumber = None
appkey =Global.XianSuoAppKey
secretkey =Global.XianSuoSecretKey

'''
    @功能：线索登录方法
    @para:
    @return:True/False
    @author:  chenhui 2016-6-8
'''  
def xiansuo_login(mobile=None, password=None, mobileType="ios"):
    global sidNumber
    paramString=''
    
    if mobile is None or password is None: 
        m1 = md5.new()
        m1.update(Global.XianSuoDftPassword)
        m2=md5.new()
        #需要排序的字典
        sortDict={"mobile":Global.XianSuoDftMobile, "password":m1.hexdigest(), "tqmobile":"true","mobileType":mobileType,"appKey":appkey}
        sortKeyList=sorted(sortDict.keys(),key=lambda d:d[0])
        #拼接key、value字符串
        for item in sortKeyList:
            paramString=paramString+item+str(sortDict[item])#value可能为int等类型，需要转换为str类型
        #需要参与md5运算的字符串，还要加上secretKey的值，不需要加上该key
        paramString=secretkey+paramString
        m2.update(paramString)
        #运算结果转成大写
        sign=m2.hexdigest().upper()
        postData = {"mobile":Global.XianSuoDftMobile,"password":m1.hexdigest(),"tqmobile":"true","mobileType":mobileType,
                    "appKey":appkey,"sign":sign}
#         print postData
    else:
        m1 = md5.new()
        m1.update(password)
        m2=md5.new()
        #需要排序的字典
        sortDict={"mobile":mobile, "password":m1.hexdigest(), "tqmobile":"true","mobileType":mobileType,"appKey":appkey}
        sortKeyList=sorted(sortDict.keys(),key=lambda d:d[0])
        for item in sortKeyList:
            paramString=paramString+item+str(sortDict[item])#value可能为int等类型，需要转换为str类型
        #需要参与md5运算的字符串，还要加上secretKey的值，不需要加上该key
        paramString=secretkey+paramString
        m2.update(paramString)
        #运算结果转成大写
        sign=m2.hexdigest().upper()
        postData = {"mobile":mobile, "password":m1.hexdigest(), "tqmobile":"true","mobileType":mobileType,
                    "appKey":appkey,"sign":sign}
    response = requests.get("%s/api/clue/loginDubboService/loginNew" % Global.XianSuoShouJiDaiLiUrl,params=postData)
#     print response.text
    try:
        jsonData = json.loads(response.text)
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "登录失败，请检查 登录参数信息")
        return False

    if jsonData['success'] is True and jsonData['response']['success'] is True:
        Log.LogOutput(LogLevel.DEBUG, u"正常登录")
        sidNumber=jsonData['response']['module']['sid']
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, "登录失败，请检查 登录参数信息")
        return False

'''
    @功能：线索post方法
    @para:
    @return:   response
    @author:  chenhui 2016-6-8
'''  
def xiansuo_post(url=None, postdata=None, headers=None, files=None, mobile=Global.XianSuoDftMobile, password = Global.XianSuoDftPassword):
    global sidNumber
    if xiansuo_login(mobile=mobile, password=password) is True:        
        m2=md5.new()
        #字典是按引用传递参数，防止修改原始参数，采用深度copy
        postdata2=copy.deepcopy(postdata)
        postdata2["appKey"]=appkey
        #将请求参数进行json格式化编码，转为了string类型
        jdata = json.dumps(postdata2)
        #在字符串前面加上secretkey
        paramString=secretkey+jdata
        #进行md5加密
        m2.update(paramString)
        #获得sign
        sign=m2.hexdigest().upper()
        #将sid和sign加入请求头
        headersSend = {"sid":sidNumber,"sign":sign}
        if headers is not None:
            headersSend.update(headers)
        response = requests.post("%s%s" % (Global.XianSuoShouJiDaiLiUrl,url),data=jdata,files=files,headers=headersSend)
        return httpResponseResultDeal(response)
    else:
        raise AssertionError, "Login Failed"

'''
    @功能：线索get方法
    @para:
    @return:   response
    @author:  chenhui 2016-6-8
'''      
def xiansuo_get(url = None, param = None, headers=None, mobile=Global.XianSuoDftMobile, password = Global.XianSuoDftPassword):
    global sidNumber
    paramString=''
    if xiansuo_login(mobile=mobile, password=password) is True:
        m2=md5.new()
        #需要排序的字典
        #字典是按引用传递参数，防止修改原始参数，采用深度copy
        param2=copy.deepcopy(param)
        #添加appKey字典项
        param2['appKey']=appkey
        paramList=sorted(param2.keys(),key=lambda d:d[0])
#         print paramList
        for item in paramList:
            paramString=paramString+item+str(param2[item])#value可能为int类型，需要转换成str类型
        #需要参与md5运算的字符串，还要加上secretKey的值，不需要加上该key
        paramString=secretkey+paramString
        m2.update(paramString)
        #运算结果转成大写
        sign=m2.hexdigest().upper()
        #添加sign字典项
        param2['sign']=sign
        #将sid和sign加入请求头
        headersSend = {"sid":sidNumber,"sign":sign}
        if headers is not None:
            headersSend.update(headers)       
        response = requests.get("%s%s" % (Global.XianSuoShouJiDaiLiUrl,url), params=param2,headers=headersSend)
        return httpResponseResultDeal(response)
    else:
        raise AssertionError, "Login Failed"
'''
    @功能：获取登录后的sid
    @para:
    @return:   sid
    @author:  chenhui 2016-6-14
'''         
def getLoginSid(mobile=Global.XianSuoDftMobile, password = Global.XianSuoDftPassword):
#     global sidNumber
    Log.LogOutput(message='初始值：'+str(sidNumber))
    if xiansuo_login(mobile=mobile, password=password) is True:        
        Log.LogOutput(message='登录后值：'+str(sidNumber))
        return sidNumber
    else:
        Log.LogOutput(LogLevel.ERROR,message='登录失败')
        return None
    
'''
    @功能：以固定sid发送post请求
    @para:
    @return:   response
    @author:  chenhui 2016-6-14
'''         
def postWithSid(sid=None,url=None, postdata=None, headers=None, files=None, mobile=Global.XianSuoDftMobile, password = Global.XianSuoDftPassword):
    if xiansuo_login(mobile=mobile, password=password) is True:
        Log.LogOutput(message="第二次登录后，获取的sid是："+str(sidNumber))
        Log.LogOutput(message="本次post请求使用的sid是："+str(sid))      
        m2=md5.new()
        #字典是按引用传递参数，防止修改原始参数，采用深度copy
        postdata2=copy.deepcopy(postdata)
        postdata2["appKey"]=appkey
        #将请求参数进行json格式化编码，转为了string类型
        jdata = json.dumps(postdata2)
        #在字符串前面加上secretkey
        paramString=secretkey+jdata
        #进行md5加密
        m2.update(paramString)
        #获得sign
        sign=m2.hexdigest().upper()
        #将sid和sign加入请求头
        headersSend = {"sid":sid,"sign":sign}
        if headers is not None:
            headersSend.update(headers)
        response = requests.post("%s%s" % (Global.XianSuoShouJiDaiLiUrl,url),data=jdata,files=files,headers=headersSend)
        return httpResponseResultDeal(response)
    else:
        raise AssertionError, "Login Failed"
    
'''
    @功能：不需要登录，直接发送post请求，专门用于无需登录的接口，如注册、获取验证码
    @para:
    @return:   response
    @author:  chenhui 2016-6-16
'''
def xiansuo_post2(url=None, postdata=None, headers=None, files=None, mobile=None, password = None):
#     global sidNumber
    m2=md5.new()
    #字典是按引用传递参数，防止修改原始参数，采用深度copy
    postdata2=copy.deepcopy(postdata)
    postdata2["appKey"]=appkey
    #将请求参数进行json格式化编码，转为了string类型
    jdata = json.dumps(postdata2)
    #在字符串前面加上secretkey
    paramString=secretkey+jdata
    #进行md5加密
    m2.update(paramString)
    #获得sign
    sign=m2.hexdigest().upper()
    #将sid和sign加入请求头
    headersSend = {"sign":sign}
    if headers is not None:
        headersSend.update(headers)
    response = requests.post("%s%s" % (Global.XianSuoShouJiDaiLiUrl,url),data=jdata,files=files,headers=headersSend)
    return httpResponseResultDeal(response) 
    
'''
    @功能：des加密
    @para:输入字典项{'key':'','value':''}
    @return:    加密后的结果
    @author:  chenhui 2016-4-6
'''  
def desEncrypt(para):
    k = pyDes.des(str(para['key']),pyDes.CBC, str(''), pad=None,padmode=pyDes.PAD_PKCS5)
    d = k.encrypt(str(para['value']))
    return binascii.b2a_base64(d).strip()