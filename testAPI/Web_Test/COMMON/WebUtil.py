# -*- coding: UTF-8 -*-
'''
Created on 2015-10-5

@author: ho
'''
from __future__ import unicode_literals
import time
from Web_Test.CONFIG import Global
from Web_Test.COMMON import Log
from Web_Test.CONFIG.Global import DefaultUrl
from Web_Test.CONFIG.Define import LogLevel, BrowserType
from selenium import webdriver

def wait(second = None):
    Log.LogOutput(LogLevel.DEBUG, "等待%s秒" % second)
    time.sleep(second)
    
def driver_init(browserType=BrowserType.IE):
    if(browserType == BrowserType.IE):
        driver = webdriver.Ie()
    Global.driver = driver
    return driver
    
def open_browser(url=DefaultUrl):
    driver = Global.driver
    driver.get(url)

def close_browser():
    driver = Global.driver
    driver.close()
    
def maximize_browser():
    driver = Global.driver
    driver.maximize_window()
    
def click_element_by_xpath(xpath =None, timeout = 5):
    driver = Global.driver
    #获取当前时间
    currentTime = time.time()
    #超时时间
    timeOut = currentTime + timeout
    
    element = None
    #循环查找
    while(currentTime < timeOut):
        try:
            element = driver.find_element_by_xpath(xpath)
            break
        except:
            wait(3)
            currentTime = time.time()
    if(element is not None):
        element.click()
        return True
    else:
        return False

def click_element_by_id(id = None, timeout = 5):
    driver = Global.driver
    #获取当前时间
    currentTime = time.time()
    #超时时间
    timeOut = currentTime + timeout
    
    element = None
    #循环查找
    while(currentTime < timeOut):
        try:
            element = driver.find_elements_by_id(id)
            break
        except:
            wait(3)
            currentTime = time.time()
    if(element is not None):
        element.click()
        return True
    else:
        return False

def click_element_by_name(name = None, timeout = 5):
    driver = Global.driver
    #获取当前时间
    currentTime = time.time()
    #超时时间
    timeOut = currentTime + timeout
    
    element = None
    #循环查找
    while(currentTime < timeOut):
        try:
            element = driver.find_element_by_name(name)
            break
        except:
            wait(3)
            currentTime = time.time()
    if(element is not None):
        element.click()
        return True
    else:
        return False
    
def input_element_by_xpath(xpath = None, text = None, timeout = 30):
    driver = Global.driver
    #获取当前时间
    currentTime = time.time()
    #超时时间
    timeOut = currentTime + timeout
    
    element = None
    #循环查找
    while(currentTime < timeOut):
        try:
            element = driver.find_element_by_xpath(xpath)
            break
        except:
            wait(3)
            currentTime = time.time()
    if(element is not None):
        element.send_keys(text)
        return True
    else:
        return False

def input_element_by_name(name = None, text = None, timeout = 5):
    driver = Global.driver
    #获取当前时间
    currentTime = time.time()
    #超时时间
    timeOut = currentTime + timeout
    
    element = None
    #循环查找
    while(currentTime < timeOut):
        try:
            element = driver.find_element_by_name(name)
            break
        except:
            wait(3)
            currentTime = time.time()
    if(element is not None):
        element.send_keys(text)
        return True
    else:
        return False

def input_element_by_id(id = None, text = None, timeout = 5):
    driver = Global.driver
    #获取当前时间
    currentTime = time.time()
    #超时时间
    timeOut = currentTime + timeout
    
    element = None
    #循环查找
    while(currentTime < timeOut):
        try:
            element = driver.find_elements_by_id(id)
            break
        except:
            wait(3)
            currentTime = time.time()
    if(element is not None):
        element.send_keys(text)
        return True
    else:
        return False
           
def wait_element_by_xpath(xpath = None, timeout = 30):
    driver = Global.driver
    #获取当前时间
    currentTime = time.time()
    #超时时间
    timeOut = currentTime + timeout
    #循环查找
    while(currentTime < timeOut):
        try:
            element = driver.find_element_by_xpath(xpath)
            return True
        except:
            wait(3)
            currentTime = time.time()
    Log.LogOutput(LogLevel.INFO, message='无法找到控件')
    return False

def wait_element_by_id(id = None, timeout = 30):
    driver = Global.driver
    #获取当前时间
    currentTime = time.time()
    #超时时间
    timeOut = currentTime + timeout
    #循环查找
    while(currentTime < timeOut):
        try:
            element = driver.find_element_by_id(id)
            return True
        except:
            wait(3)
            currentTime = time.time()
    return False
            
def scroll_browser_to_bottom(driver):
    if driver is None:
        driver = Global.driver
        
    js="var q=document.documentElement.scrollTop=100000"  
    driver.execute_script(js)  
    time.sleep(3)
    
def scroll_browser_to_top(driver):
    if driver is None:
        driver = Global.driver
        
    js="var q=document.documentElement.scrollTop=0"  
    driver.execute_script(js)  
    time.sleep(3)
        