# -*- coding:UTF-8 -*-
'''
Created on 2016-9-23

@author: chenhui
'''
from __future__ import unicode_literals
from COMMON import Time, CommonUtil
from CONFIG import Global
from Interface.XianSuoApp.BaoLiao import XsBaoLiaoPara
from Interface.XianSuoApp.BaoLiao.XsBaoLiaoIntf import addXianSuo
from Interface.XianSuoApp.JiFenShangCheng import XsJiFenShangChengIntf
from Interface.XianSuoApp.JiFenShangCheng.XsJiFenShangChengIntf import \
    getOrderList, cancelOrder, confirmOrder
from Interface.YunWeiPingTai.XiTongPeiZhi import XiTongPeiZhiPara, \
    XiTongPeiZhiIntf
from Mobile import MobileUtil
from Mobile.Define.Clue import MyRelateObjectDef, PointRelateObjectDef
from Mobile.Define.Clue.PointRelateObjectDef import OrderListPara
from Mobile.Logic.Clue import ClueCommonLogic, ClueCommonLogic, PointRelateLogic
from Mobile.MobileUtil import start_app
from Mobile.UI.Clue import PointMallUI, MainPageUI, PersonalUI, OrderConfirmUI, \
    ExchangeRecordUI, CommonUI, GoodsDetailUI
import copy
import json
import time
import unittest


class PointMall(unittest.TestCase):
    def setUp(self):
#         SystemMgrIntf.initEnv()
        #初始积分值设为0
        XsJiFenShangChengIntf.setPointByMobile()
        #清空测试自动化区下的积分规则
        XsJiFenShangChengIntf.deletePointRuleByDb()
        #清空测试自动化区下的积分商品
        XsJiFenShangChengIntf.deleteGoods()
        #清空默认用户的兑换记录
        XsJiFenShangChengIntf.deleteExchangeRecord()
        #删除测试自动化区下的所有活动
        XsJiFenShangChengIntf.delAllActivity()
        #打开应用
        MobileUtil.MobileDriverInit()
        #初始化状态回到首页页面
        ClueCommonLogic.return_main_page()
        pass 
    
    '''
    @功能：兑换话费积分并检查
    @ chenhui  2016-9-23
    ''' 
    def testPoint_001(self):
        #配置积分
        ret=XsJiFenShangChengIntf.initPointSetting()
        self.assertTrue(ret, '积分配置出错')
        #新增一条线索，此时积分为6
        testPremise = copy.deepcopy(XsBaoLiaoPara.xinZeng2) 
        response = addXianSuo(testPremise)
        self.assertTrue(response.result, '新增线索失败') 
        #后台添加商品
        ret=XsJiFenShangChengIntf.initMerchandiseSetting()
        self.assertTrue(ret, '初始化商品出错')
        #后台配置活动时间
        ret=XsJiFenShangChengIntf.initActivitySetting()
        self.assertTrue(ret, '初始化配置活动时间失败')
#         #等待10s，过快进入我的页面，会导致登录状态判断异常
#         time.sleep(10)
        #需要重新登录
        userInfo = copy.deepcopy(MyRelateObjectDef.userInfo)
#         ClueCommonLogic.clue_login(userInfo)
        #进入我的-积分商城页面
        MainPageUI.click_personal_menu()
        ret=PersonalUI.check_in_personal_page()
        self.assertTrue(ret, '检查页面位于我的出错')
        #刷新我的页面
        PersonalUI.refresh_page_of_mine()
        #重新登录
        ret=PersonalUI.relogin(userInfo)
        self.assertTrue(ret, '重新登录失败')
        #验证我的页面积分显示
        userInfo['point']=6        
        ret=PersonalUI.check_point(userInfo)
        self.assertTrue(ret, '我的页面积分显示错误')
        PersonalUI.click_point_mall()
        ret=PointMallUI.check_in_point_mall_page()
        self.assertTrue(ret, '进入积分商城页面失败')        
        #验证积分商城页面区域和积分是否正确
        PointObject=copy.deepcopy(PointRelateObjectDef.PointObject)
        PointObject['location']='测试自动化区'
        PointObject['score']=6
        ret=PointMallUI.check_location_and_point(PointObject)
        self.assertTrue(ret, '检查区域和积分显示错误')
        #验证本期话费兑余额与可兑换数额显示是否正确
        PointObject['totalBalance']=30
        PointObject['personalBalance']=20
        ret=PointMallUI.check_exchange_balance(PointObject)
        self.assertTrue(ret, '验证本期话费兑余额与可兑换数额显示错误')
        #验证商品显示
        PointObject['goodsName']='10元话费'
        PointObject['exchangePersonNum']=0
        PointObject['goodsUnitPoint']=5
        ret=PointRelateLogic.check_goods_in_list(PointObject)
        self.assertTrue(ret,'检测商品单价、名称、已兑换人数出错')
        #验证商品图片是否正确
        time.sleep(3)
        PointObject['goodsPicturePath']='C:\\autotest_file\\AppImage\\point_mall_lake.png'
        res=PointMallUI.check_picture_in_point_mall_list(PointObject)
        self.assertTrue(res, '图片比对失败！')
        
        #兑换商品
        #addMerchandisePara['goodsConfiguration.goodsName']
        res1=PointRelateLogic.exchange_phone_card(PointObject)
        self.assertTrue(res1, '商品兑换出错')
        #姓名和身份证都为空
        PointObject['name']=''
        PointObject['idNum']=''
        res2=PointRelateLogic.submit_info_supply(PointObject)
        self.assertFalse(res2, '姓名和身份证都为空点击提交按钮验证通过！')
        #姓名不为空，身份证为空
        PointObject['name']='张三'
        PointObject['idNum']=''
        res3=PointRelateLogic.submit_info_supply(PointObject)
        self.assertFalse(res3, '身份证为空点击提交按钮验证通过！')
        #姓名为空，身份证不为空
        PointObject['name']=''
        PointObject['idNum']='111111111111111'
        res4=PointRelateLogic.submit_info_supply(PointObject)
        self.assertFalse(res4, '姓名为空点击提交按钮验证通过！')
        #姓名身份证都不为空，但是身份证输入错误
        PointObject['name']='张三'
        PointObject['idNum']='123456789012345678'
        res5=PointRelateLogic.submit_info_supply(PointObject)
        self.assertFalse(res5, '身份证输入错误信息点击提交按钮验证通过！')
        #姓名和身份证输入都正确
        PointObject['name']='张三'
        PointObject['idNum']='111111111111111'
        res6=PointRelateLogic.submit_info_supply(PointObject)
        self.assertTrue(res6, '身份证输入正确信息点击提交按钮验证通过！')
        #验证积分扣除数额是否正确
        PointObject['restPoint']=1
        ret=OrderConfirmUI.check_rest_point_in_order_confirm_page(PointObject)
        self.assertTrue(ret, '订单确认页面剩余积分验证错误')
        #进入兑换记录页面
        OrderConfirmUI.click_exchange_record_button_in_confirm_page()
        PointObject['state']='处理中'
        ret=ExchangeRecordUI.check_exchange_state(PointObject)
        self.assertTrue(ret, '兑换记录检测失败')
        #后台取消订单
        orderListPara=copy.deepcopy(OrderListPara)
        response=getOrderList(para=orderListPara)
        cancelPara={
                    'id':json.loads(response.text)['rows'][0]['id']
                    }
        cancelOrder(para=cancelPara)
        #刷新兑换记录页面并检查
        MobileUtil.swipe_down()
        PointObject['state']='失败'
        ret=ExchangeRecordUI.check_exchange_state(PointObject)
        self.assertTrue(ret, '兑换记录检测失败') 
        #点击返回按钮，进入兑换确认页面
        CommonUI.click_back_button()
        #点击继续兑换按钮
        OrderConfirmUI.click_continue_exchange_button()
        PointRelateLogic.exchange_phone_card(PointObject)
        PointRelateLogic.submit_info_supply(PointObject)
        #后台确认订单
        response2=getOrderList(para=orderListPara)
        confirmPara={
                    'ids[]':json.loads(response2.text)['rows'][0]['id']
                    }
        ret=confirmOrder(para=confirmPara).result
        self.assertTrue(ret, '后台确认兑换失败')
        #再次进入兑换记录页面
        OrderConfirmUI.click_exchange_record_button_in_confirm_page()
        PointObject['state']='成功'
        ret=ExchangeRecordUI.check_exchange_state(PointObject)
        self.assertTrue(ret, '兑换记录检测失败')
        #点击返回按钮，查看剩余积分数是否正确
        CommonUI.click_back_button()
        PointObject['restPoint']=1
        ret=OrderConfirmUI.check_rest_point_in_order_confirm_page(PointObject)
        self.assertTrue(ret, '订单确认页面剩余积分数验证正确')
        #点击继续兑换按钮
        OrderConfirmUI.click_continue_exchange_button()
        #检查页面区域和积分显示是否正确
        PointObject['score']=1
        ret=PointMallUI.check_location_and_point(PointObject)
        self.assertTrue(ret, '检查区域和积分显示错误')
        #验证本期话费兑余额与可兑换数额显示是否正确
        PointObject['totalBalance']=20
        PointObject['personalBalance']=10
        ret=PointMallUI.check_exchange_balance(PointObject)
        self.assertTrue(ret, '验证本期话费兑余额与可兑换数额显示错误')
        #验证商品已兑换人数显示2,失败那次也算
        PointObject['exchangePersonNum']=2
        ret=PointRelateLogic.check_goods_in_list(PointObject)
        self.assertTrue(ret,'检测商品已兑换人数出错')   
        pass
    
    '''
    @功能：验证实物商品积分兑换功能
    @ chenhui  2016-10-08
    ''' 
    def testPoint_002(self):
        #配置积分
        ret=XsJiFenShangChengIntf.initPointSetting()
        self.assertTrue(ret, '积分配置出错')
        #新增一条线索，此时积分为6
        testPremise = copy.deepcopy(XsBaoLiaoPara.xinZeng2) 
        response = addXianSuo(testPremise)
        self.assertTrue(response.result, '新增线索失败') 
        #后台添加实物卡
        ret=XsJiFenShangChengIntf.initMerchandiseSetting(goodstype='实物')
        self.assertTrue(ret, '初始化商品出错')
        #后台配置活动时间，暂时保留
        ret=XsJiFenShangChengIntf.initActivitySetting()
        self.assertTrue(ret, '初始化配置活动时间失败')
#         #等待10s，过快进入我的页面，会导致登录状态判断异常
#         time.sleep(10)
        #需要重新登录
        userInfo = copy.deepcopy(MyRelateObjectDef.userInfo)
        #进入我的-积分商城页面
        MainPageUI.click_personal_menu()
        ret=PersonalUI.check_in_personal_page()
        self.assertTrue(ret, '检查页面位于我的出错')
        #刷新我的页面
        PersonalUI.refresh_page_of_mine()
        #重新登录
        ret=PersonalUI.relogin(userInfo)
        self.assertTrue(ret, '重新登录失败')
        #验证我的页面积分显示
        userInfo['point']=6
        ret=PersonalUI.check_point(userInfo)
        self.assertTrue(ret, '我的页面积分显示错误')
        PersonalUI.click_point_mall()
        ret=PointMallUI.check_in_point_mall_page()
        self.assertTrue(ret, '进入积分商城页面失败')        
        #验证积分商城页面区域和积分是否正确
        PointObject=copy.deepcopy(PointRelateObjectDef.PointObject)
        PointObject['location']='测试自动化区'
        PointObject['score']=6
        ret=PointMallUI.check_location_and_point(PointObject)
        self.assertTrue(ret, '检查区域和积分显示错误')
#         #验证本期话费兑余额与可兑换数额显示是否正确
#         PointObject['totalBalance']=30
#         PointObject['personalBalance']=20
#         ret=PointMallUI.check_exchange_balance(PointObject)
#         self.assertTrue(ret, '验证本期话费兑余额与可兑换数额显示错误')
        #验证商品显示
        PointObject['goodsName']='实物测试'
        PointObject['exchangePersonNum']=0
        PointObject['stock']=2
        PointObject['goodsUnitPoint']=5
        PointObject['goodsDetail']='商品详情'
        PointObject['exchangeNum']=1
        PointObject['totalPoints']=5
        ret=PointRelateLogic.check_goods_in_list(PointObject)
        self.assertTrue(ret,'检测商品单价、名称、已兑换人数或库存出错')
        #兑换商品
        #addMerchandisePara['goodsConfiguration.goodsName']
        
#         res1=PointRelateLogic.exchange_real_entity(PointObject)
        PointMallUI.click_exchange_button(PointObject)
        #检查相关信息
        res=PointRelateLogic.check_goods_detail_in_entity_page(PointObject)
        self.assertTrue(res, '检查商品详情第一页面的标题、单位积分、已兑换人数、库存、商品详情信息失败')
        #点击立即兑换按钮
        GoodsDetailUI.click_immediately_exchange_button()
        #检查页面相关信息
        res=PointRelateLogic.check_goods_detail_in_entity_page2(PointObject)
        self.assertTrue(res, '检查商品详情第二页面的标题、单位积分、默认兑换数量和总计积分错误')
        #检查点击加号、减号总计数据变化是否正确
        res=PointRelateLogic.check_plus_minus(PointObject)
        self.assertTrue(res, '加减号功能验证出错')
        #点击确定按钮
        GoodsDetailUI.click_confirm_exchange_button()
        res=OrderConfirmUI.check_in_order_confirm_page()
        self.assertTrue(res, '订单确认页面检测失败')
        #验证积分扣除数额是否正确
        PointObject['restPoint']=1
        ret=OrderConfirmUI.check_rest_point_in_order_confirm_page(PointObject)
        self.assertTrue(ret, '订单确认页面剩余积分验证错误')
        #进入兑换记录页面
        OrderConfirmUI.click_exchange_record_button_in_confirm_page()
        PointObject['state']='处理中'
        ret=ExchangeRecordUI.check_exchange_state(PointObject)
        self.assertTrue(ret, '兑换记录检测失败')
        #后台取消订单
        orderListPara=copy.deepcopy(OrderListPara)
        response=getOrderList(para=orderListPara)
        cancelPara={
                    'id':json.loads(response.text)['rows'][0]['id']
                    }
        cancelOrder(para=cancelPara)
        #刷新兑换记录页面并检查
        MobileUtil.swipe_down()
        PointObject['state']='失败'
        ret=ExchangeRecordUI.check_exchange_state(PointObject)
        self.assertTrue(ret, '兑换记录检测失败') 
        #点击返回按钮，进入兑换确认页面
        CommonUI.click_back_button()
        #点击继续兑换按钮
        OrderConfirmUI.click_continue_exchange_button()
        PointRelateLogic.exchange_real_entity(PointObject)
        #后台确认订单
        response2=getOrderList(para=orderListPara)
        confirmPara={
                    'ids[]':json.loads(response2.text)['rows'][0]['id']
                    }
        ret=confirmOrder(para=confirmPara).result
        self.assertTrue(ret, '后台确认兑换失败')
        #再次进入兑换记录页面
        OrderConfirmUI.click_exchange_record_button_in_confirm_page()
        PointObject['state']='成功'
        ret=ExchangeRecordUI.check_exchange_state(PointObject)
        self.assertTrue(ret, '兑换记录检测失败')
        #点击返回按钮，查看剩余积分数是否正确
        CommonUI.click_back_button()
        PointObject['restPoint']=1
        ret=OrderConfirmUI.check_rest_point_in_order_confirm_page(PointObject)
        self.assertTrue(ret, '订单确认页面剩余积分数验证正确')
        #点击继续兑换按钮
        OrderConfirmUI.click_continue_exchange_button()
        #检查页面区域和积分显示是否正确
        PointObject['score']=1
        ret=PointMallUI.check_location_and_point(PointObject)
        self.assertTrue(ret, '检查区域和积分显示错误')
        #验证商品已兑换人数显示,失败那次不算
        PointObject['exchangePersonNum']=1
        PointObject['stock']=1
        ret=PointRelateLogic.check_goods_in_list(PointObject)
        self.assertTrue(ret,'检测商品已兑换人数出错')   
        pass
    
    '''
    @功能：积分规则
    @ chenhui  2016-9-23
    ''' 
    def testPoint_003(self):
        pointRulePara=copy.deepcopy(XiTongPeiZhiPara.updateJiFenGuiZhe)
        pointRulePara['departmentNo']='959595'
#         pointRulePara['id']=XiTongPeiZhiIntf.getPointRuleId({"departmentNo":"959595"})
        pointRulePara['notice']='天阙tianque123'
        rs1=XiTongPeiZhiIntf.updateJiFenGuiZhe(pointRulePara)
        self.assertTrue(rs1.result, '设置积分规则出错')
        #手机端查看显示是否正确
        MainPageUI.click_personal_menu()
        ret=PersonalUI.check_in_personal_page()
        self.assertTrue(ret, '检查页面位于我的出错')
        #重新登录
        userInfo = copy.deepcopy(MyRelateObjectDef.userInfo)
        if PersonalUI.check_is_login() is False:
            ret=PersonalUI.relogin(userInfo)
            self.assertTrue(ret, '重新登录失败')
        #进入积分商城-积分规则按钮
        PersonalUI.click_point_mall()
        PointMallUI.click_point_rule_button()
        ret=PointMallUI.check_in_point_rule_page()
        self.assertTrue(ret, '检查当前页是否位于积分规则页面出错')
        #验证积分内容
        PointObject=copy.deepcopy(PointRelateObjectDef.PointObject)
        PointObject['rule']=pointRulePara['notice']
        res2=PointMallUI.check_point_rule(PointObject)
        self.assertTrue(res2, '积分规则验证失败')
#         #修改积分为js代码,js代码页面直接转换，不方便通过接口设置
#         pointRulePara['notice']='''<javascript>alert("test")<javascript/>'''
#         pointRulePara['id']=XiTongPeiZhiIntf.getPointRuleId({"departmentNo":"959595"})
#         res3=XiTongPeiZhiIntf.updateJiFenGuiZhe(pointRulePara)
#         self.assertTrue(res3.result, '设置积分规则出错')
#         #手机端再次验证
#         PointMallUI.click_back_button()
#         PointMallUI.click_point_rule_button()
#         ret=PointMallUI.check_in_point_rule_page()
#         self.assertTrue(ret, '检查当前页是否位于积分规则页面出错')
#         PointObject['rule']=pointRulePara['notice']
#         res4=PointMallUI.check_point_rule(PointObject)
#         self.assertTrue(res4, '积分规则验证失败')
        
        pass
    
    def tearDown(self):
        pass
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(PointMall("testPoint_001")) 
    results = unittest.TextTestRunner().run(suite)
    pass
