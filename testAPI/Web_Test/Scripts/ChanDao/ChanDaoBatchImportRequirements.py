# -*- coding: UTF-8 -*-
'''
Created on 2017-12-21

@author: n-313
'''
from Sweb.ChanDao import ChanDaoOperations, ChanDaoElements, PathUtil
from CONFIG import Global
from selenium import webdriver

from Sweb.ChanDao.ChanDaoDefine import FirstLevelMenu, SecondLevelMenu
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from COMMON import WebUtil


chromedriver = PathUtil.get_current_workspace_root_path()+"\\\\chromedriver"
driver = Global.driver = webdriver.Chrome(chromedriver)
driver.get(ChanDaoElements.Url)
driver.maximize_window()
ChanDaoOperations.chandao_login()
      
ChanDaoOperations.chose_first_level_menu(FirstLevelMenu.Product)
ChanDaoOperations.chose_product("万达城")
ChanDaoOperations.chose_second_level_menu(SecondLevelMenu.Requirement)
  
dataFilePath = "E:\\requirement_templet.xlsx";
table = ChanDaoOperations.getTableFromExcelFile(dataFilePath)
 
rowNum = table.nrows
 
#已经添加的总数据
totalCount = 0
print "一共要添加%s条数据" % rowNum
for rowItem in range(1,rowNum):
    needToClickBatchAdd = False
    needToClickSave = False
    ChanDaoOperations.click_raise_requirement(batchRaise = True)
    addCounts = 0
    requirementData = ChanDaoOperations.readRowDataFromExcelFile(table, rowItem)
     
    #是10的倍数,放在第十行
    addIndex = 0 
     
    if rowNum - totalCount < 10:
        if rowNum == totalCount:
            needToClickSave = True
        needToClickBatchAdd = False
         
    if rowItem % 10 == 0:
        addIndex = 9
        needToClickBatchAdd = True
        needToClickSave = True
    else:
        addIndex = rowItem % 10 - 1
     
     
    totalCount = totalCount  + 1
     
    print "当前索引:%s,待写入位置%s" % (rowItem,addIndex)
    
    #如果到了底部，往下翻
    if addIndex >=9:
        WebUtil.scroll_browser_to_bottom(driver)
    #增加一条数据
    ChanDaoOperations.add_one_requirement(requirementData, addIndex)
     
    print "已经添加了%s条数据" % totalCount
    if needToClickSave :
        ChanDaoOperations.click_save_button()
         
    #点击保存之后，继续添加需要点击批量添加
    if needToClickBatchAdd :
        ChanDaoOperations.click_raise_requirement(True)
         
time.sleep(10)
driver.quit()
