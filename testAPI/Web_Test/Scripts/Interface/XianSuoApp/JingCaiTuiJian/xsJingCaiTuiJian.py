# -*- coding:UTF-8 -*-
'''
Created on 2016-12-19

@author: N-66
'''
from __future__ import unicode_literals
import unittest
from Interface.PingAnJianShe.XianSuoGuanLi import XianSuoGuanLiIntf
from Interface.PingAnJianShe.XianSuoGuanLi import XianSuoGuanLiPara
from Interface.XianSuoApp.BaoLiao import XsBaoLiaoPara
from Interface.XianSuoApp.BaoLiao import XsBaoLiaoIntf
import copy
from COMMON.CommonUtil import createRandomString
from CONFIG import InitDefaultPara
from Interface.XianSuoApp.ShouYe import XsShouYeIntf

class XsJingCaiTuiJian(unittest.TestCase):
    def setUp(self):
        XianSuoGuanLiIntf.delete_all_pinganxuanchuan()
        XianSuoGuanLiIntf.delete_all_shishidongtai()  
        XsBaoLiaoIntf.deleteAllClues()                  
        pass
    
    def testcase1(self):
        #新增1条平安宣传,1条实时动态，1条爆料,addPara1为平安宣传，2为实时动态，3为爆料
        addPara1 = copy.deepcopy(XianSuoGuanLiPara.addPingAnXuanChuanDict)
        addPara1["informationVo.information.title"] = "平安宣传%s"%createRandomString()
        addPara1["informationVo.information.contentText"] = "平安宣传转精彩推荐%s"%createRandomString()
        addPara2 = copy.deepcopy(XianSuoGuanLiPara.addPingAnXuanChuanDict)
        addPara2['infoType'] = 1 #infotype为1的时候，表示新增的是实时动态 
        addPara2["informationVo.information.title"] = "实时动态%s"%createRandomString()
        addPara2["informationVo.information.contentText"] = "实时动态转精彩推荐%s"%createRandomString()
        addPara3 = copy.deepcopy(XsBaoLiaoPara.XinZeng)
        addPara3['information']['contentText'] = '事件描述%s' %createRandomString()
        addPara3['information']['baiduX'] = '120.4989885463861'
        addPara3['information']['baiduY'] = '30.27759299562879'
        addPara3['information']['x'] = '120.488114380334'
        addPara3['information']['y'] = '30.27759299562879'         
        addPara3['information']['address'] = 'addres%s'%createRandomString()
        response1 = XianSuoGuanLiIntf.add_pinganxuanchuan(addPara1)
        response2 = XianSuoGuanLiIntf.add_pinganxuanchuan(addPara2)
        response3 = XsBaoLiaoIntf.addXianSuo(addPara3)
        self.assertTrue(response1, '新增平安宣传已经失败，无法进行下一步验证')
        self.assertTrue(response2, '新增实时动态已经失败，无法进行下一步验证')
        self.assertTrue(response3, '新增爆料已经失败，无法进行下一步验证')
        #把平安宣传，实时动态，爆料设置为精彩推荐
        updatePara1 = copy.deepcopy(XianSuoGuanLiPara.updatePingAnXuanChuanStateDict)
        updatePara1['ids'] = XianSuoGuanLiIntf.get_pinganxuanchuan_id_by_title(pingAnXuanChuanTitle=addPara1["informationVo.information.title"])
        updatePara1['showState'] =2
        updatePara2 = copy.deepcopy(XianSuoGuanLiPara.updatePingAnXuanChuanStateDict)
        updatePara2['ids'] = XianSuoGuanLiIntf.get_shishidongtai_id_by_title(shiShiDongTaiTitle=addPara2["informationVo.information.title"])
        updatePara2['showState'] =2
        updatePara3 = copy.deepcopy(XianSuoGuanLiPara.updatePingAnXuanChuanStateDict)
        updatePara3['ids'] = XianSuoGuanLiIntf.get_clue_id_by_description(addPara3['information']['contentText'])
        updatePara3['showState'] = 2    
        ret1 = XianSuoGuanLiIntf.update_pinganxuanchuan_state(updatePara1)
        ret2 = XianSuoGuanLiIntf.update_pinganxuanchuan_state(updatePara2)
        ret3 = XianSuoGuanLiIntf.update_pinganxuanchuan_state(updatePara3)
        self.assertTrue(ret1,"更改平安宣传状态失败，无法进行下一步验证")
        self.assertTrue(ret2,"更改实时动态状态失败，无法进行下一步验证")
        self.assertTrue(ret3,"更改爆料状态失败，无法进行下一步验证")
        #手机端检查是否能看到精彩推荐
        searchDict ={
                 'tqmobile':'true',
                 'departmentNo':InitDefaultPara.clueOrgInit['DftQuOrgDepNo'],
                 }
        compareDict1 = copy.deepcopy(XianSuoGuanLiPara.jingCaiTuiJianSearchResult)
        compareDict1['informationId'] = updatePara1['ids']
        compareDict1['contentText'] = addPara1["informationVo.information.contentText"]
        compareDict2 = copy.deepcopy(XianSuoGuanLiPara.jingCaiTuiJianSearchResult)
        compareDict2['informationId'] = updatePara2['ids']
        compareDict2['contentText'] = addPara2["informationVo.information.contentText"]
        compareDict3 = copy.deepcopy(XianSuoGuanLiPara.jingCaiTuiJianSearchResult)
        compareDict3['informationId'] = updatePara3['ids']
        compareDict3['contentText'] = addPara3['information']['contentText']
        ret1 = XsShouYeIntf.check_shouye_jingcaituijian_result(compareDict1,searchDict)
        ret2 = XsShouYeIntf.check_shouye_jingcaituijian_result(compareDict2,searchDict)
        ret3 = XsShouYeIntf.check_shouye_jingcaituijian_result(compareDict3,searchDict)
        self.assertTrue(ret1, '检查平安宣传转精彩推荐失败')
        self.assertTrue(ret2, '检查实时动态转精彩推荐失败')
        self.assertTrue(ret3, '检查爆料转精彩推荐失败')
        pass 
    def tearTown(self):
        pass
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(XsJingCaiTuiJian("testcase1"))
    results = unittest.TextTestRunner().run(suite)
    pass     
