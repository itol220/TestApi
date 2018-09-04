# -*- coding: UTF-8 -*-
'''
Created on 2017-12-21

@author: n-313
'''
from Web_Test.Sweb.ChanDao import ChanDaoElements
import requests
from Web_Test.COMMON import Log
from Web_Test.CONFIG.Define import LogLevel
from Web_Test.CONFIG import Global

def login_and_get_response(username=ChanDaoElements.LoginUsername,password=ChanDaoElements.LoginPassword):
    post_url = "%suser-login.html"%(ChanDaoElements.Url)
    postData = {"account":username,"password":password,"keepLogin[]":"on","referer":"%sproduct-browse-37.html" % ChanDaoElements.Url}
    response = requests.post(post_url,postData,get_userlogin_cookies())
    
    print ("***login_and_get_response 的返回内容%s***" % response.text)
    return response

def get_login_cookies(response = None,username=ChanDaoElements.LoginUsername,password=ChanDaoElements.LoginPassword):
    
    if response is None:
        response = login_and_get_response(username,password)
    
    set_cookies = response.headers['Set-Cookie']
    
    return set_cookies

def login_by_interface_and_get_zentaosid(response = None,username=ChanDaoElements.LoginUsername,password=ChanDaoElements.LoginPassword):
    
    if response is None:
        response = login_and_get_response(username,password)
        
    set_cookie = get_login_cookies(response) 
    
    set_cookie_group_list = set_cookie.split(";")
    
    for set_cookie_item in set_cookie_group_list:
        [key,value] = set_cookie_item.split("=")
        if key == "zentaosid":
            Log.LogOutput(LogLevel.INFO, "获取到禅道的SID为【%s】" % value) 
            Global.zentaosid = value
            return value
    return None

def delete_one_requirement_by_view(requirement_id):
    return

def get_requirements_list():
    
    url = "%sproduct-browse-37.html" % ChanDaoElements.Url
    print (url)
    
    loginCookies = get_login_cookies()
    setCookies = 'lang=zh-cn; device=desktop; theme=default; lastProduct=37; preBranch=0; preProductID=37; storyModule=0; productStoryOrder=id_desc; windowHeight=623; windowWidth=1366;'
    setCookies = "%szentaosid=%s;%s" % (setCookies,Global.zentaosid,loginCookies)
    response = requests.get(url,setCookies)
    print (response.text)
    return response

def add_header_cookies_before_request(request):
    
    cookies = {}
    if  Global.zentaosid is None:
        Global.zentaosid = login_by_interface_and_get_zentaosid()
        
    cookies['Set-Cookie'] = "zentaosid=%s" % Global.zentaosid
    
    request.add_cookie(cookies)
    
# def get_basic_cookies():
#     
#     cookies = {}
#     
#     if  Global.zentaosid is None:
#         Global.zentaosid = login_by_interface_and_get_zentaosid()
#         
#     cookies['Set-Cookie'] = "zentaosid=%s" % Global.zentaosid
#     
#     
#     headers = get_login_cookies()
#     
#     print cookies
#     return cookies

def get_userlogin_cookies():
    get_url = "%suser-login.html" % ChanDaoElements.Url
    response = requests.get(get_url)
    
    cookies = {}
    setCookies = response.headers['Set-Cookie']
    
    setCookieList = setCookies.split(";")
    
    for setCookieItem in setCookieList:
        [key,value] = setCookieItem.split("=",1)
        
        if  "zentaosid" in key:
            Global.zentaosid = value
        cookies[key] = value
    
    return cookies