# -*- coding:UTF-8 -*-
'''
Created on 2016-1-12

@author: N-254
'''
from appium import webdriver
from Web_Test.CONFIG import Global
import time
from Web_Test.COMMON import Time
import os
from appium.webdriver.common.touch_action import TouchAction

'''
    @功能：     初始化driver对象
    @para: 无
    @return: 返回driver句柄
    @ hongzenghui  2016-1-13
'''
def MobileDriverInit():
    p = os.popen('tasklist /FI "IMAGENAME eq node.exe"')
    count = p.read().count("node.exe")
    if count == 0:
        os.startfile('c:\\autotest_file\\startAppium.bat')
        Time.wait(30)
    driver = None
    desired_caps = {}
    desired_caps['platformName'] = Global.PlatformName
    desired_caps['platformVersion'] = Global.PlatformVersion
    desired_caps['deviceName'] = Global.DeviceName
    desired_caps['app'] = "%s/PingAnTong.apk" % Global.AppPath
    desired_caps['appPackage'] = Global.PackageName
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    desired_caps['noReset'] = True
    desired_caps['appActivity'] = '.common.view.module.enter.WelcomeActivity'  
#     desired_caps['appWaitActivity'] = '.com.tianque.ecommunity.plugin.syssetting.enter.LoginActivity'
    print (u"[%s][INFO][初始化应用开始...]" % time.strftime("%Y-%m-%d %H:%M:%S"))
    try: 
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        print (u"[%s][INFO][初始化应用完成]" % time.strftime("%Y-%m-%d %H:%M:%S"))
        Global.driver = driver
    except Exception as e:
        print (u"[%s][INFO][初始化应用失败:%s]" % (time.strftime("%Y-%m-%d %H:%M:%S"),e))
    return driver

'''
    @功能：     重连driver对象，如果driver已经存在，直接返回，如果没有，则创建driver
    @para: 无
    @return: 返回driver句柄
    @ hongzenghui  2016-1-13
'''
def MobileDriverReconnect():
    p = os.popen('tasklist /FI "IMAGENAME eq node.exe"')
    count = p.read().count("node.exe")
    if count == 0:
        os.startfile('c:\\autotest_file\\startAppium.bat')
        Time.wait(30)
    driver = None
    desired_caps = {}
    desired_caps['platformName'] = Global.PlatformName
    desired_caps['platformVersion'] = Global.PlatformVersion
    desired_caps['deviceName'] = Global.DeviceName
    desired_caps['app'] = "%s/PingAnTong.apk" % Global.AppPath
    desired_caps['appPackage'] = Global.PackageName
    desired_caps['noReset'] = True
#     desired_caps['newCommandTimeout'] = 3600
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
#     desired_caps['appActivity'] = '.common.view.module.enter.WelcomeActivity'  
    print (u"[%s][INFO][初始化应用开始...]" % time.strftime("%Y-%m-%d %H:%M:%S"))
    try: 
        driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps, ifReconnect=True)
        print (u"[%s][INFO][初始化应用完成]" % time.strftime("%Y-%m-%d %H:%M:%S"))
        Global.driver = driver
    except Exception as e:
        print (u"[%s][INFO][初始化应用失败:%s]" % (time.strftime("%Y-%m-%d %H:%M:%S"),e))
    return driver

'''
    @功能：     释放driver对象
    @para: 无
    @return: 
    @ hongzenghui  2017-10-11
'''
def MobileDriverClose():
    driver = Global.driver
    driver.quit()

'''
    @功能：     重启app
    @para: 无
    @return: 
    @ hongzenghui  2016-1-13
'''
def start_app():
    driver = Global.driver
    driver.launch_app()
    
'''
    @功能：     关闭app
    @para: 无
    @return: 
    @ hongzenghui  2016-1-13
'''
def close_app():
    driver = Global.driver
    driver.close_app()

'''
    @功能：     通过xpath点击
    @para: 
    xpath:用于定位元素的xpath信息
    timeout:超时时间
    @return: 点击成功，返回True;否则返回False
    @ hongzenghui  2016-1-13
'''  
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
            Time.wait(1)
            currentTime = time.time()
    if(element is not None):        
#         os.system("adb shell input tap %s %s" % (element.location['x'],element.location['y'])) 
        element.click()
#         print "x:%s,y:%s" % (element.location['x'],element.location['y'])
#         TouchAction(driver).press(x=element.location['x'], y=element.location['y']).release().perform()
        return True
    else:
        return False
    
'''
    @功能：     通过id点击
    @para: 
    id:用于定位元素的id信息
    timeout:超时时间
    @return: 点击成功，返回True;否则返回False
    @ hongzenghui  2016-1-13
'''     
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
        except:
            Time.wait(1)
            currentTime = time.time()
    if(element is not None):
        element.click()
        return True
    else:
        return False

'''
    @功能：     通过name点击
    @para: 
    name:用于定位元素的name信息
    timeout:超时时间
    @return: 点击成功，返回True;否则返回False
    @ hongzenghui  2016-1-13
'''
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
        except:
            Time.wait(1)
            currentTime = time.time()
    if(element is not None):
        element.click()
        return True
    else:
        return False

'''
    @功能：     通过xpath输入
    @para: 
    xpath:用于定位元素的xpath信息
    text:输入的文字信息
    timeout:超时时间
    @return: 点击成功，返回True;否则返回False
    @ hongzenghui  2016-1-13
'''  
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
            Time.wait(1)
            currentTime = time.time()
    if(element is not None):
#         element.click()
        element.send_keys(u'%s' % text)
        os.system("adb shell input keyevent 61")
        return True
    else:
        return False
    
'''
    @功能：     通过xpath输入
    @para: 
    xpath:用于定位元素的xpath信息
    text:输入的文字信息
    timeout:超时时间
    @return: 点击成功，返回True;否则返回False
    @ hongzenghui  2016-1-13
'''  
def clear_and_input_element_by_xpath(xpath = None, text = None, timeout = 30):
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
            Time.wait(1)
            currentTime = time.time()
    if(element is not None):
        textOrg = element.get_attribute('text')
        element.click()
        driver.keyevent(122)
        for i in range(0,len(textOrg)):
            driver.keyevent(112)
        element.send_keys(u'%s' % text)
        return True
    else:
        return False

'''
    @功能：     通过name输入
    @para: 
    name:用于定位元素的name信息
    text:输入的文字信息
    timeout:超时时间
    @return: 点击成功，返回True;否则返回False
    @ hongzenghui  2016-1-13
'''  
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
        except:
            Time.wait(1)
            currentTime = time.time()
    if(element is not None):
        element.send_keys(text)
        return True
    else:
        return False

'''
    @功能：     通过id输入
    @para: 
    id:用于定位元素的id信息
    text:输入的文字信息
    timeout:超时时间
    @return: 点击成功，返回True;否则返回False
    @ hongzenghui  2016-1-13
''' 
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
        except:
            Time.wait(1)
            currentTime = time.time()
    if(element is not None):
        element.send_keys(text)
        return True
    else:
        return False
    
'''
    @功能：     在页面中查找控件并返回
    @para: 
    xpath:用于定位元素的xpath信息
    timeout:等待超时时间
    @return: 元素查找到，返回元素对象;否则返回None
    @ hongzenghui  2016-1-13
'''     
def find_element_by_xpath(xpath = None, timeout = 10):
    driver = Global.driver
    #获取当前时间
    currentTime = time.time()
    #超时时间
    timeOut = currentTime + timeout
    #循环查找
    while(currentTime < timeOut):
        try:
            element = driver.find_element_by_xpath(xpath)
            return element
        except:
            Time.wait(1)
            currentTime = time.time()
    return None

'''
    @功能：     在页面中查找所有符合条件的控件并返回
    @para: 
    xpath:用于定位元素的xpath信息
    timeout:等待超时时间
    @return: 元素查找到，返回元素对象;否则返回None
    @ hongzenghui  2016-1-13
'''     
def find_elements_by_xpath(xpath = None, timeout = 10):
    driver = Global.driver
    #获取当前时间
    currentTime = time.time()
    #超时时间
    timeOut = currentTime + timeout
    #循环查找
    while(currentTime < timeOut):
        try:
            elements = driver.find_elements_by_xpath(xpath)
            return elements
        except:
            Time.wait(1)
            currentTime = time.time()
    return None

'''
    @功能：     在超时时间内查找某一元素
    @para: 
    xpath:用于定位元素的xpath信息
    timeout:等待超时时间
    @return: 元素查找到，返回True;否则返回False
    @ hongzenghui  2016-1-13
'''     
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
            Time.wait(1)
            currentTime = time.time()
    print (u"[%s][WARN][无法找到控件]" % time.strftime("%Y-%m-%d %H:%M:%S"))
    return False

'''
    @功能：     截屏操作，默认存到d:/logs目录
    @para: 
    @return: 元素查找到，返回True;否则返回False
    @ hongzenghui  2016-1-13
'''     
def screen_shot():
    driver = Global.driver
    currentTime = time.strftime("%Y-%m-%d-%H-%M-%S")
    filePath = "C:/autotest_file/logs/%s.png" % currentTime
    try:
        driver.get_screenshot_as_file(filePath)
        message='ScreenShot-%s' % filePath
        print (u"[%s][DEBUG][%s]" % (currentTime,message))
        return True
    except:
        print (u"[%s][ERROR][截屏失败]" % currentTime)
        return False

'''
    @功能：     向上滑动
    @para: 
    @return: 滑动成功，返回True;否则返回False
    @ hongzenghui  2016-1-13
'''     
def swipe_up():
    driver = Global.driver
    currentTime = time.strftime("%Y-%m-%d %H:%M:%S")
    try:
        width = driver.get_window_size()['width']
        height = driver.get_window_size()['height']
        driver.swipe(width/2,height*3/4,width/2,height/4)
#         print u"[%s][WARN][%s]" % (currentTime,message)
        return True
    except:
        print (u"[%s][ERROR][向上滑动失败]" % currentTime)
        return False
    
'''
    @功能：     往左滑动
    @para: 
    @return: 滑动成功，返回True;否则返回False
    @ hongzenghui  2016-8-15
'''     
def swipe_left():
    driver = Global.driver
    currentTime = time.strftime("%Y-%m-%d-%H-%M-%S")
    try:
        width = driver.get_window_size()['width']
        height = driver.get_window_size()['height']
        driver.swipe(width*3/4,height/2,width/4,height/2)
#         print u"[%s][WARN][%s]" % (currentTime,message)
        return True
    except:
        print (u"[%s][ERROR][向左滑动失败]" % currentTime)
        return False
    
'''
    @功能：     从一个控件移到另一个控件
    @para: 
    @return: 滑动成功，返回True;否则返回False
    @ hongzenghui  2016-8-29
'''     
def move_from_one_element_to_another(xpathOrg = None,xpathDst = None):
    driver = Global.driver
    currentTime = time.strftime("%Y-%m-%d-%H-%M-%S")
    try:
        eleOrg = driver.find_element_by_xpath(xpathOrg)
        eleDst = driver.find_element_by_xpath(xpathDst)
        driver.drag_and_drop(eleOrg,eleDst)
#         print u"[%s][WARN][%s]" % (currentTime,message)
        return True
    except:
        print (u"[%s][ERROR][控件滑动失败]" % (currentTime))
        return False
    
'''
    @功能：    通过坐标点击
    @para: 
    @return: 滑动成功，返回True;否则返回False
    @ hongzenghui  2016-8-29
'''     
def click_by_position(x = None,y = None):
    driver = Global.driver   
    currentTime = time.strftime("%Y-%m-%d %H:%M:%S") 
    try:
        TouchAction(driver).press(x=x, y=y).release().perform()
#         print u"[%s][WARN][%s]" % (currentTime,message)
        return True
    except Exception as e:
        print (e)
        print (u"[%s][ERROR][控件滑动失败]" % currentTime)
        return False