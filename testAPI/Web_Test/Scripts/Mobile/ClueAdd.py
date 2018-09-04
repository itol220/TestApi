# -*- coding:UTF-8 -*-
'''
Created on 2016-2-29

@author: lhz
'''
from __future__ import unicode_literals
import unittest
import copy
from COMMON import Time
from Mobile.Define.Clue import ClueRelateObjectDef, MyRelateObjectDef
from Mobile.Logic.Clue import ClueRelateLogic, ClueCommonLogic
from Mobile.UI.Clue import ClueAddUI
from Mobile import MobileUtil
from Mobile.Define.Clue.ClueRelateObjectDef import ClueStatus
class ClueAdd(unittest.TestCase):
    def setUp(self):
#         SystemMgrIntf.initEnv()
        #打开应用
        MobileUtil.MobileDriverInit()
        pass 
    '''
    @功能：新增爆料并检查
    @ hzh  2016-9-20
    ''' 
    def clueAdd_001(self):
        #先登录
        userInfo = copy.deepcopy(MyRelateObjectDef.userInfo)
        ClueCommonLogic.clue_login(userInfo)
        '''爆料新增--基本功能'''
        #新增爆料，地址和内容都不填写
        clueObject = copy.deepcopy(ClueRelateObjectDef.clueObject) 
        clueObject['address'] = None 
        ClueRelateLogic.add_clue(clueObject)
        #无法爆料成功，当前应该处于爆料页面
        ret = ClueAddUI.check_in_clue_realease_page()
        self.assertTrue(ret, '不填写地址和内容，爆料成功')
        #返回首页
        ClueAddUI.click_back_button()
          
        #不设置地址,但输入内容
        clueObject['address'] = None
        clueObject['description'] = '爆料内容'
        ClueRelateLogic.add_clue(clueObject)
        #无法爆料成功，当前应该处于爆料页面
        ret = ClueAddUI.check_in_clue_realease_page()
        self.assertTrue(ret, '不输入地址，爆料成功')
        #返回首页
        ClueAddUI.click_back_button()
          
        #设置地址,但不输入内容
        clueObject['address'] = '中国浙江省杭州市西湖区学院路'
        clueObject['description'] = None
        ClueRelateLogic.add_clue(clueObject)
        #无法爆料成功，当前应该处于爆料页面
        ret = ClueAddUI.check_in_clue_realease_page()
        self.assertTrue(ret, '不输入内容，爆料成功')
        #返回首页
        ClueAddUI.click_back_button()
        
        #同时输入爆料内容
        clueObject['description'] = '爆料内容abcdef' 
        clueObject['subject'] = '测试主题'
        clueObject['picture']['lakePic'] = True
#         clueObject['picture']['catPic'] = True
#         clueObject['picture']['penguinsPic'] = True
        ret = ClueRelateLogic.add_clue(clueObject)
        self.assertTrue(ret, '输入地址和内容，爆料不成功')
        
        #在爆料列表检查爆料
        clueObject['status'] = ClueStatus.ADD
        ret = ClueRelateLogic.check_clue_in_list(clueObject)
        self.assertTrue(ret, '列表中检查爆料失败')
        
        #在爆料详情检查爆料
        ret = ClueRelateLogic.check_clue_in_detail(clueObject)
        self.assertTrue(ret, '详情中检查爆料失败')
        Time.wait(1)   
        pass
    def tearDown(self):
#         Global.driver.quit()
        pass
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(ClueAdd("clueAdd_001")) 
    results = unittest.TextTestRunner().run(suite)
    pass
        