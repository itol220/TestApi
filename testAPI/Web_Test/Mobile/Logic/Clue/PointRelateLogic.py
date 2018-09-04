# -*- coding:UTF-8 -*-
'''
Created on 2016-9-23
积分商城相关逻辑操作
@author: chenhui
'''
from COMMON import Log
from CONFIG.Define import LogLevel
from Mobile import MobileUtil
from Mobile.UI.Clue import PointMallUI, GoodsDetailUI, InforSupplyUI, \
    OrderConfirmUI, ExchangeRecordUI


'''
    @功能：检查积分规则文本内容
    @para: PointObject:积分对象内容
    @return: 检查成功，返回True；否则返回False
    @ chenhui  2016-9-23
'''
def check_rule_text(PointObject):
    if PointObject is not None:
        #点击积分规则按钮
        if PointMallUI.click_point_rule_button() is False:
            return False
        if PointMallUI.check_point_rule(PointObject) is False:
            return False
    return True


'''
    @功能：检查兑换记录状态，过程包含了检查兑换记录
    @para: PointObject:积分对象内容
    @return: 检查成功，返回True；否则返回False
    @ chenhui  2016-9-23
'''
def check_exchange_record_in_list(PointObject):
    if PointObject is not None:
        #点击兑换记录按钮
        if PointMallUI.click_exchange_record_button() is False:
            return False
        if ExchangeRecordUI.check_exchange_state(PointObject) is False:
            return False
    return True


'''
    @功能：检查商品是否位于积分商城主页列表中
    @para: PointObject:积分对象内容,PointObject['goodsName'],PointObject['exchangePersonNum'],PointObject['goodsUnitPoint']
    @return: 检查成功，返回True；否则返回False
    @ chenhui  2016-9-23
'''
def check_goods_in_list(PointObject):
    if PointObject is not None:
        #检查商品名称
        if PointMallUI.check_goodsname_in_list(PointObject) is False:
            return False
        #检查已兑换人数
        if PointMallUI.check_exchanged_person_num_in_list(PointObject) is False:
            return False
        #检查单个商品所需积分数
        if PointMallUI.check_goods_unit_point_in_list(PointObject) is False:
            return False
        #检查实物类型的商品库存
        if PointObject['stock'] is not None:
            return PointMallUI.check_stock(PointObject)
    return True

'''
    @功能：兑换手机卡
    @para: pointObject:爆料对象内容，请引用PointRelateObjectDef中的pointObject对象
    @return: 新增成功，返回True；否则返回False
    @ chenhui  2016-9-23
'''
def exchange_phone_card(PointObject):
    if PointMallUI.check_in_point_mall_page() is False:
        return False
    #点击“兑换按钮”
    if PointMallUI.click_exchange_button(PointObject) is False:
        return False
    if GoodsDetailUI.check_in_goods_detail_page() is False:
        return False
    #检查详情页面图片
    if GoodsDetailUI.check_picture_in_goods_detail_list(PointObject) is False:
        return False
    #点击确定兑换按钮
    if GoodsDetailUI.click_confirm_exchange_button() is False:
        return False
    if InforSupplyUI.check_in_infor_supply_page() is False:
        return False
    return True
#     #点击提交按钮
#     if InforSupplyUI.click_submit_button() is False:
#         return False
#     if PointMallUI.check_in_order_confirm_page() is False:
#         return False
    
'''
    @功能：兑换实物
    @para: pointObject:爆料对象内容，请引用PointRelateObjectDef中的pointObject对象
    @return: 新增成功，返回True；否则返回False
    @ chenhui  2016-10-08
'''
def exchange_real_entity(PointObject):
    if PointMallUI.check_in_point_mall_page() is False:
        return False
    #点击“兑换按钮”
    if PointMallUI.click_exchange_button(PointObject) is False:
        return False
    if GoodsDetailUI.check_in_goods_detail_page() is False:
        return False
    #实物商品详情页面检查标题、所需积分、已兑换人数、库存、商品详情
    
    
    #点击立即兑换按钮
    if GoodsDetailUI.click_immediately_exchange_button() is False:
        return False
    #点击确定兑换
    if GoodsDetailUI.click_confirm_exchange_button() is False:
        return False
    #检查是否位于订单确认页面
    if OrderConfirmUI.check_in_order_confirm_page() is False:
        return False
    return True

    
'''
    @功能：提交信息补充
    @para: pointObject:爆料对象内容，请引用PointRelateObjectDef中的pointObject对象
    @return: 新增成功，返回True；否则返回False
    @ chenhui  2016-9-26
'''
def submit_info_supply(PointObject):
    if  InforSupplyUI.check_in_infor_supply_page() is False:
        return False
    if InforSupplyUI.clear_and_input_name(PointObject) is False:
        return False
    if InforSupplyUI.clear_and_input_idnum(PointObject) is False:
        return False
    if InforSupplyUI.click_submit_button() is False:
        return False
    #如果仍然处于信息补充页面，说明页面验证没通过，直接返回False
    if InforSupplyUI.check_in_infor_supply_page() is True:
        return False
    if OrderConfirmUI.check_in_order_confirm_page() is False:
        return False
    return True


'''
    @功能：检查实物商品详情页面第一页的商品标题、单位积分、已兑换人数、库存和商品详情信息
    @para: pointObject:爆料对象内容，请引用PointRelateObjectDef中的pointObject对象
    @return: 新增成功，返回True；否则返回False
    @ chenhui  2016-10-14
'''
def check_goods_detail_in_entity_page(PointObject):
    #检查是否位于详情页
    if GoodsDetailUI.check_in_goods_detail_page() is False:
        return False
    #检查标题
    if GoodsDetailUI.check_title_in_entity_page(PointObject) is False:
        return False
    #检查单位积分数
    if GoodsDetailUI.check_point_in_entity_page(PointObject) is False:
        return False
    #检查已兑换人数
    if GoodsDetailUI.check_exchangedPersonNum_in_entity_page(PointObject) is False:
        return False
    #检查库存
    if GoodsDetailUI.check_stock_in_entity_page(PointObject)is False:
        return False
    #检查商品详情
    if GoodsDetailUI.check_goods_detail_in_entity_page(PointObject) is False:
        return False
    return True


'''
    @功能：检查实物商品详情页第二页面的商品标题、单位积分、已兑换人数、库存和商品详情信息
    @para: pointObject:爆料对象内容，请引用PointRelateObjectDef中的pointObject对象
    @return: 新增成功，返回True；否则返回False
    @ chenhui  2016-10-14
'''
def check_goods_detail_in_entity_page2(PointObject):
    #检查是否位于详情页
    if GoodsDetailUI.check_in_goods_detail_page() is False:
        return False
    #检查标题
    if GoodsDetailUI.check_title_in_entity_page(PointObject) is False:
        return False
    #检查单位积分数
    if GoodsDetailUI.check_point_in_entity_page(PointObject) is False:
        return False
    #检查默认兑换数
    if GoodsDetailUI.check_exchange_goods_count_in_entity_page(PointObject) is False:
        return False
    #检查默认共计积分数
    if GoodsDetailUI.check_total_point_count_in_entity_page(PointObject) is False:
        return False
    return True

'''
    @功能：检查点击实物商品详情页第二页面的加号、减号后对应数据变化是否正确
    @para: pointObject:爆料对象内容，请引用PointRelateObjectDef中的pointObject对象
    @return: 新增成功，返回True；否则返回False
    @ chenhui  2016-10-14
'''
def check_plus_minus(PointObject):
    #检查是否位于详情页
    if GoodsDetailUI.check_in_goods_detail_page() is False:
        return False
    #检查默认兑换数量
    if GoodsDetailUI.check_exchange_goods_count_in_entity_page(PointObject) is False:
        return False
    #检查默认所需积分数
    if GoodsDetailUI.check_total_point_count_in_entity_page(PointObject) is False:
        return False
    #点击+
    if GoodsDetailUI.click_plus_button() is False:
        return False
    PointObject['exchangeNum']=PointObject['exchangeNum']*2
    PointObject['totalPoints']=PointObject['totalPoints']*2
    #检查兑换数量
    if GoodsDetailUI.check_exchange_goods_count_in_entity_page(PointObject) is False:
        return False
    #检查所需积分数
    if GoodsDetailUI.check_total_point_count_in_entity_page(PointObject) is False:
        return False
    #点击-
    if GoodsDetailUI.click_minus_button() is False:
        return False
    PointObject['exchangeNum']=PointObject['exchangeNum']/2
    PointObject['totalPoints']=PointObject['totalPoints']/2    
    #检查兑换数量
    if GoodsDetailUI.check_exchange_goods_count_in_entity_page(PointObject) is False:
        return False
    #检查所需积分数
    if GoodsDetailUI.check_total_point_count_in_entity_page(PointObject) is False:
        return False    
    return True