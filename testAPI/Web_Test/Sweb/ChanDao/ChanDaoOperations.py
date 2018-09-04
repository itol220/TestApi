# -*- coding: UTF-8 -*-
'''
Created on 2017-12-21

@author: n-313
'''
from COMMON import WebUtil, Log
from Sweb.ChanDao import ChanDaoElements
import xlrd
import time
from CONFIG.Define import LogLevel

#禅道登录
def chandao_login(username = None,password = None):
    if username is None:
        username = ChanDaoElements.LoginUsername
        
    if password is None:
        password = ChanDaoElements.LoginPassword
        
    if WebUtil.input_element_by_xpath(ChanDaoElements.LoginUsernameInput,username) is False:
        return False
    
    if WebUtil.input_element_by_xpath(ChanDaoElements.LoginPasswordInput,password) is False:
        return False
    
    if WebUtil.click_element_by_xpath(ChanDaoElements.LoginSubmitButton) is False:
        return False
 
#选择顶级菜单   
def chose_first_level_menu(to_choose_first_level_menu = None):
    print ChanDaoElements.ToChooseFirstMenu % to_choose_first_level_menu
    return WebUtil.click_element_by_xpath(ChanDaoElements.ToChooseFirstMenu % to_choose_first_level_menu)

#选择下级菜单
def chose_second_level_menu(to_choose_second_level_menu = None):
    return WebUtil.click_element_by_xpath(ChanDaoElements.ToChooseSecondMenu % to_choose_second_level_menu)

#选择产品
def chose_product(toChooseProduct = None):
    return WebUtil.click_element_by_xpath(ChanDaoElements.ToChooseProject % toChooseProduct)

#选择提需求，是否批量提取
def click_raise_requirement(batchRaise = False):
    
    if  batchRaise:
        return WebUtil.click_element_by_xpath("//*[contains(@class,'btn btn-primary dropdown-toggle')]")and WebUtil.click_element_by_xpath("//*[text()='批量添加']")
    
    return    WebUtil.click_element_by_xpath("//*[text()='提需求']")

#从表格中读取一个table，方便后续使用table
def getTableFromExcelFile(filePath,sheetName=None):
    try:
        data = xlrd.open_workbook(filePath)
    except Exception,e:
        Log.LogOutput(LogLevel.ERROR, "打开文件%s失败" % filePath)
        Log.LogOutput(LogLevel.ERROR, e)
        return False
    if sheetName is None:
        table = data.sheet_by_index(0)
    else:
        table = data.sheet_by_name('u%s' % sheetName)
    
    if table is not None:
        return table
    
    return None

#从表格中读取一条数据
def readRowDataFromExcelFile(table,rowIndex = 1):
    ChanDaoElements.requirementData['productName'] = table.cell(rowIndex,0).value
    ChanDaoElements.requirementData['moduleName'] = table.cell(rowIndex,1).value
    ChanDaoElements.requirementData['plan'] = table.cell(rowIndex,2).value
    ChanDaoElements.requirementData['requirementName'] = table.cell(rowIndex,3).value
    ChanDaoElements.requirementData['requirementDesc'] = table.cell(rowIndex,4).value
    ChanDaoElements.requirementData['acceptanceStandard'] = table.cell(rowIndex,5).value
    ChanDaoElements.requirementData['requirementSource'] = table.cell(rowIndex,6).value
    ChanDaoElements.requirementData['priorityLevel'] = table.cell(rowIndex,7).value
    ChanDaoElements.requirementData['priorityLevel'] = table.cell(rowIndex,8).value
    ChanDaoElements.requirementData['keywords'] = table.cell(rowIndex,9).value
    return ChanDaoElements.requirementData

#添加一条需求，在批量添加的时候
def add_one_requirement(requirementData,toAddIndex=0):
    print '开始添加一个需求,需求内容:' 
    print requirementData
    
    if requirementData['requirementName'] is  None or requirementData['requirementName'] == '':
        Log.LogOutput(LogLevel.ERROR,"需求不能为空,不添加!!!" )
        return
    
    #产品名称
    if requirementData['productName'] is not None and requirementData['productName'] != '':
#         WebUtil.input_element_by_xpath(xpath, text, timeout)
        pass
    
    #模块名称
    if requirementData['moduleName'] is not None and requirementData['moduleName'] != '':
#         WebUtil.input_element_by_xpath(xpath, text, timeout)
        pass
    
    #所属计划
    if requirementData['plan'] is not None and requirementData['plan'] != '':
#         WebUtil.input_element_by_xpath(xpath, text, timeout)
        pass
    
    #需求名称
    print "需求名称" + requirementData['requirementName']
    if requirementData['requirementName'] is not None and requirementData['requirementName'] != '':
        if WebUtil.input_element_by_xpath("//*[@id='title[%s]']" % toAddIndex,requirementData['requirementName']) is False:
            return False
    
    #需求描述
    if requirementData['requirementDesc'] is not None and requirementData['requirementDesc'] != '':
        if WebUtil.input_element_by_xpath("//*[@id='spec[%s]']" % toAddIndex,requirementData['requirementDesc']) is False:
            return False
     
    #优先级
    if requirementData['priorityLevel'] is not None and requirementData['priorityLevel'] != '':
        if WebUtil.click_element_by_xpath("//*[@id='pri%s']" % toAddIndex) is False:
            return False
        time.sleep(500)
        if WebUtil.click_element_by_xpath("//*[@id='pri%s']/*[text()='%s']" % (toAddIndex,requirementData['priorityLevel'])) is False:
            return False
        
    
    #预计工时
    if requirementData['estimatedWorkingHours'] is not None and requirementData['estimatedWorkingHours'] != '':
        if WebUtil.input_element_by_xpath("//*[@id='estimate[%s]']" % toAddIndex) is False:
            return False
    print '一个需求添加完毕'
    return True

#批量输入完毕之后点击保存
def click_save_button():
    return WebUtil.scroll_browser_to_bottom() and WebUtil.click_element_by_xpath("//table[@class='table table-form table-fixed with-border']//*[@id='submit']")