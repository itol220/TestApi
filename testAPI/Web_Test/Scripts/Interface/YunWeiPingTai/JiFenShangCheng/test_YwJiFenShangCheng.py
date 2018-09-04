# -*- coding:UTF-8 -*-
'''
Created on 2016-11-29

@author: chenhui
'''
from __future__ import unicode_literals
from COMMON import Log, Time, CommonUtil
from COMMON.Time import getCurrentDateAndTime, moveTime2, TimeMoveType, \
    TimeCalcType
from CONFIG import InitDefaultPara, Global
from CONFIG.InitDefaultPara import orgInit, userInit, clueOrgInit
from Interface.PingAnJianShe.ShiJianChuLi import ShiJianChuLiPara
from Interface.PingAnJianShe.ShiJianChuLi.ShiJianChuLiIntf import dealIssue, \
    deleteAllIssues2
from Interface.XianSuoApp.BaoLiao import XsBaoLiaoPara, XsBaoLiaoIntf
from Interface.XianSuoApp.BaoLiao.XsBaoLiaoIntf import addXianSuo, \
    deleteAllClues, viewSchedule
from Interface.XianSuoApp.GongZuoTai import XsGongZuoTaiIntf, XsGongZuoTaiPara
from Interface.XianSuoApp.JiFenShangCheng import XsJiFenShangChengIntf, \
    XsJiFenShangChengPara
from Interface.XianSuoApp.JiFenShangCheng.XsJiFenShangChengIntf import \
    createRandomNumber, checkMerchandiseInListForMobile, exchangeMerchandise, \
    checkExchangeRecord
from Interface.XianSuoApp.JiFenShangCheng.XsJiFenShangChengPara import \
    JiFenDuiHuan, DuiHuanJiLu, ReceiveState
from Interface.XianSuoApp.PaiHangBang import XsPaiHangBangIntf
from Interface.XianSuoApp.WoDeXinXi import XsMyInformationIntf
from Interface.XianSuoApp.WoDeXinXi.XsMyInformationIntf import encodeToMd5
from Interface.XianSuoApp.XinXiGuangChang import XsInformationSquareIntf, \
    XsInformationSquarePara
from Interface.XianSuoApp.XinXiGuangChang.XsInformationSquareIntf import \
    addConcern, addPraise, addComment
from Interface.XianSuoApp.XinXiGuangChang.XsInformationSquarePara import \
    addPraisePara, addCommentPara
from Interface.XianSuoApp.xianSuoHttpCommon import desEncrypt
from Interface.YunWeiPingTai.JiFenShangCheng import JiFenShangChengPara, \
    JiFenShangChengIntf
from Interface.YunWeiPingTai.JiFenShangCheng.JiFenShangChengIntf import \
    delAllLotteryAllocation
from Interface.YunWeiPingTai.JiFenShangCheng.JiFenShangChengPara import JumpType, \
    LotteryAllocationState, GoodsType, ShippingMethod, ExchangeState
from Interface.YunWeiPingTai.TongJiFenXi import TongJiFenXiPara, TongJiFenXiIntf
from Interface.YunWeiPingTai.XiTongPeiZhi import XiTongPeiZhiIntf, \
    XiTongPeiZhiPara
from Interface.YunWeiPingTai.YunWeiCommon import YunWeiCommonIntf
from Interface.YunWeiPingTai.YunWeiCommon.YunWeiCommonIntf import \
    getLinuxDateAndTimeYunWei
import copy
import datetime
import json
import time
import unittest

class YwJiFenShangCheng(unittest.TestCase):
    #仿真环境不可用,加判断防止误操作
    def setUp(self):
        if Global.simulationEnvironment is False:
            #清空测试自动化区下的积分规则
            XsJiFenShangChengIntf.deletePointRuleByDb()
            #清空兑换记录
            JiFenShangChengIntf.deleteExchangeRecords()
            #删除用户'12345678901'
            XsGongZuoTaiIntf.deleteUserFromDb(mobile='12345678901')
            #清空抽奖记录
            JiFenShangChengIntf.deleteLotteryRecords()
        #清空测试自动化区下的积分商品
        JiFenShangChengIntf.deleteGoods()
        #清空线索
        deleteAllClues()
        #清空事件列表
        deleteAllIssues2()
        #删除活动
        JiFenShangChengIntf.delAllActivity()
        #清空转盘抽奖配置
        delAllLotteryAllocation()
        #清空所有banner图
        JiFenShangChengIntf.delAllBannerPic()
        pass
    
    def test_YwJiFenShangCheng_01(self):
        '''运维平台-积分商城实物配置-610'''
        #新增后台商品,默认上架状态
        addMerchandisePara=copy.deepcopy(JiFenShangChengPara.ShangPinXinZeng)
        addMerchandisePara['goodsConfiguration.goodsNum']=10
        addMerchandisePara['goodsConfiguration.exchangePoints']=3
        addMerchandisePara['goodsConfiguration.goodsNo']='S'+time.strftime("%Y%m%d%H%M%S")+createRandomNumber(length=3)
#         addMerchandisePara['goodsConfiguration.quota']=100
        addMerchandisePara['goodsConfiguration.shippingMethod']='0'
        #文件参数
        files = {
                 'iosImgValue':open('C:/autotest_file/Tulips.jpg', 'rb'),
                'androidImgValue':open('C:/autotest_file/Penguins.jpg','rb')
                }     
#         files = [ ('iosImgValue',('Tulips.jpg',open('C:/autotest_file/Tulips.jpg', 'rb'),'image/jpeg')),
#                 ('androidImgValue',('Penguins.jpg',open('C:/autotest_file/Penguins.jpg','rb'),'image/jpeg'))
#                 ]
        result=JiFenShangChengIntf.addMerchandise(para=addMerchandisePara,files=files)
        goodsId=json.loads(result.text)['id']
        #检查PC端列表
        checkPcPara=copy.deepcopy(JiFenShangChengPara.ShangPinLieBiaoCheck)
        checkPcPara['goodsName']=addMerchandisePara['goodsConfiguration.goodsName']
        checkPcPara['goodsProfile']=addMerchandisePara['goodsConfiguration.goodsProfile']
        checkPcPara['goodsDetails']=addMerchandisePara['goodsConfiguration.goodsDetails']
        checkPcPara['goodsType']=addMerchandisePara['goodsConfiguration.goodsType']
        checkPcPara['exchangePoints']=addMerchandisePara['goodsConfiguration.exchangePoints']
#         checkPcPara['quota']=addMerchandisePara['goodsConfiguration.quota']
        checkPcPara['goodsNo']=addMerchandisePara['goodsConfiguration.goodsNo']
        listPcpara=copy.deepcopy(JiFenShangChengPara.ShangPinLieBiao)
        result=JiFenShangChengIntf.checkMerchandiseInList(listPcpara,checkPcPara)
        self.assertTrue(result, '检查PC端商品列表出错')
        #查看手机端商品列表
        listPara=copy.deepcopy(XsJiFenShangChengPara.ShouJiShangPingLieBiao)
        res=XsJiFenShangChengIntf.getMerchandiseListForMobile(para=listPara)
        self.assertTrue(res.result, '获取手机商品列表出错')
        checkPara=copy.deepcopy(XsJiFenShangChengPara.ShouJiShangPingLieBiaoJianCha)
        checkPara['departmentNo']=addMerchandisePara['goodsConfiguration.departmentNo']
        checkPara['exchangePoints']=addMerchandisePara['goodsConfiguration.exchangePoints']#兑换需要积分
        checkPara['goodsDetails']=addMerchandisePara['goodsConfiguration.goodsDetails']
        checkPara['goodsName']=addMerchandisePara['goodsConfiguration.goodsName']
        checkPara['goodsNum']=addMerchandisePara['goodsConfiguration.goodsNum']
        checkPara['goodsProfile']=addMerchandisePara['goodsConfiguration.goodsProfile']
        checkPara['goodsType']=addMerchandisePara['goodsConfiguration.goodsType']
        checkPara['orgName']=addMerchandisePara['goodsConfiguration.orgName']
        checkPara['goodsNo']=addMerchandisePara['goodsConfiguration.goodsNo']
        result=checkMerchandiseInListForMobile(listpara=listPara,checkpara=checkPara)
        self.assertTrue(result, '手机端查看商品列表失败')
        #将商品下架,手机端检查失败
        para={'ids[]':goodsId}
        JiFenShangChengIntf.closeMerchandise(para)
        result=checkMerchandiseInListForMobile(listpara=listPara,checkpara=checkPara)
        self.assertFalse(result, '手机端查看商品列表成功')
        #将商品上架，手机端检查成功
        JiFenShangChengIntf.openMerchandise(para)
        result=checkMerchandiseInListForMobile(listpara=listPara,checkpara=checkPara)
        self.assertTrue(result, '手机端查看商品列表失败')
        Log.LogOutput(message='商品上架、下架功能正常')      
        #修改商品
        updMerchandisePara=copy.deepcopy(JiFenShangChengPara.ShangPinXiuGai)
        updMerchandisePara['goodsConfiguration.id']=goodsId
        updMerchandisePara['goodsConfiguration.goodsNum']=1
        updMerchandisePara['goodsConfiguration.exchangePoints']=2
        JiFenShangChengIntf.updMerchandise(para=updMerchandisePara,files=files)
        #PC端列表检查修改是否正确
        checkPcPara['exchangePoints']=updMerchandisePara['goodsConfiguration.exchangePoints']#兑换需要积分
        checkPcPara['goodsDetails']=updMerchandisePara['goodsConfiguration.goodsDetails']
        checkPcPara['goodsName']=updMerchandisePara['goodsConfiguration.goodsName']
        checkPcPara['goodsNum']=updMerchandisePara['goodsConfiguration.goodsNum']
        checkPcPara['goodsProfile']=updMerchandisePara['goodsConfiguration.goodsProfile']
        result=JiFenShangChengIntf.checkMerchandiseInList(listPcpara,checkPcPara)
        self.assertTrue(result, '检查PC端商品列表出错')        
        #手机端列表检查修改是否正确
        checkPara['exchangePoints']=updMerchandisePara['goodsConfiguration.exchangePoints']#兑换需要积分
        checkPara['goodsDetails']=updMerchandisePara['goodsConfiguration.goodsDetails']
        checkPara['goodsName']=updMerchandisePara['goodsConfiguration.goodsName']
        checkPara['goodsNum']=updMerchandisePara['goodsConfiguration.goodsNum']
        checkPara['goodsProfile']=updMerchandisePara['goodsConfiguration.goodsProfile']        
        result=checkMerchandiseInListForMobile(listpara=listPara,checkpara=checkPara)
        self.assertTrue(result, '手机端查看商品列表失败')
        #修改功能验证通过
        Log.LogOutput(message='修改功能验证通过')
        #删除商品
        JiFenShangChengIntf.delMerchandise({'ids[]':goodsId})
        #PC端验证
        result=JiFenShangChengIntf.checkMerchandiseInList(listPcpara,checkPcPara)
        self.assertFalse(result, '检查PC端商品列表出错')
        #手机端验证
        result=checkMerchandiseInListForMobile(listpara=listPara,checkpara=checkPara)
        self.assertFalse(result, '手机端查看商品列表失败')
        Log.LogOutput(message='删除验证通过!')                     
        pass
    
    def test_YwJiFenShangCheng_02(self):
        '''运维平台-积分商城手机卡配置-884'''
        #新增后台商品,默认上架状态
        addMerchandisePara=copy.deepcopy(JiFenShangChengPara.ShangPinXinZeng)
        addMerchandisePara['goodsConfiguration.goodsType']=0
        addMerchandisePara['goodsConfiguration.goodsNum']=10
        addMerchandisePara['goodsConfiguration.exchangePoints']=3
        addMerchandisePara['goodsConfiguration.goodsNo']='S'+time.strftime("%Y%m%d%H%M%S")+createRandomNumber(length=3)
        addMerchandisePara['goodsConfiguration.quota']=100
        addMerchandisePara['goodsConfiguration.operators']=0
        addMerchandisePara['goodsConfiguration.goodsDetails']=None
        #文件参数
        files = {
                 'iosImgValue':open('C:/autotest_file/Tulips.jpg', 'rb'),
                'androidImgValue':open('C:/autotest_file/Penguins.jpg','rb')
                }     
#         files = [ ('iosImgValue',('Tulips.jpg',open('C:/autotest_file/Tulips.jpg', 'rb'),'image/jpeg')),
#                 ('androidImgValue',('Penguins.jpg',open('C:/autotest_file/Penguins.jpg','rb'),'image/jpeg'))
#                 ]
        result=JiFenShangChengIntf.addMerchandise(para=addMerchandisePara,files=files)
        goodsId=json.loads(result.text)['id']
        #检查PC端列表
        checkPcPara=copy.deepcopy(JiFenShangChengPara.ShangPinLieBiaoCheck)
        checkPcPara['goodsName']=addMerchandisePara['goodsConfiguration.goodsName']
        checkPcPara['goodsProfile']=addMerchandisePara['goodsConfiguration.goodsProfile']
#         checkPcPara['goodsDetails']=addMerchandisePara['goodsConfiguration.goodsDetails']
        checkPcPara['goodsType']=addMerchandisePara['goodsConfiguration.goodsType']
        checkPcPara['exchangePoints']=addMerchandisePara['goodsConfiguration.exchangePoints']
        checkPcPara['quota']=addMerchandisePara['goodsConfiguration.quota']
        checkPcPara['goodsNo']=addMerchandisePara['goodsConfiguration.goodsNo']
        listPcpara=copy.deepcopy(JiFenShangChengPara.ShangPinLieBiao)
        result=JiFenShangChengIntf.checkMerchandiseInList(listPcpara,checkPcPara)
        self.assertTrue(result, '检查PC端商品列表出错')
        #查看手机端商品列表
        listPara=copy.deepcopy(XsJiFenShangChengPara.ShouJiShangPingLieBiao)
        res=XsJiFenShangChengIntf.getMerchandiseListForMobile(para=listPara)
        self.assertTrue(res.result, '获取手机商品列表出错')
        checkPara=copy.deepcopy(XsJiFenShangChengPara.ShouJiShangPingLieBiaoJianCha)
        checkPara['departmentNo']=addMerchandisePara['goodsConfiguration.departmentNo']
        checkPara['exchangePoints']=addMerchandisePara['goodsConfiguration.exchangePoints']#兑换需要积分
#         checkPara['goodsDetails']=addMerchandisePara['goodsConfiguration.goodsDetails']
        checkPara['goodsName']=addMerchandisePara['goodsConfiguration.goodsName']
        checkPara['goodsNum']=addMerchandisePara['goodsConfiguration.goodsNum']
        checkPara['goodsProfile']=addMerchandisePara['goodsConfiguration.goodsProfile']
        checkPara['goodsType']=addMerchandisePara['goodsConfiguration.goodsType']
        checkPara['orgName']=addMerchandisePara['goodsConfiguration.orgName']
        checkPara['goodsNo']=addMerchandisePara['goodsConfiguration.goodsNo']
        result=checkMerchandiseInListForMobile(listpara=listPara,checkpara=checkPara)
        self.assertTrue(result, '手机端查看商品列表失败')
        #将商品下架,手机端检查失败
        para={'ids[]':goodsId}
        JiFenShangChengIntf.closeMerchandise(para)
        result=checkMerchandiseInListForMobile(listpara=listPara,checkpara=checkPara)
        self.assertFalse(result, '手机端查看商品列表成功')
        #将商品上架，手机端检查成功
        JiFenShangChengIntf.openMerchandise(para)
        result=checkMerchandiseInListForMobile(listpara=listPara,checkpara=checkPara)
        self.assertTrue(result, '手机端查看商品列表失败')
        Log.LogOutput(message='商品上架、下架功能正常')      
        #修改商品
        updMerchandisePara=copy.deepcopy(JiFenShangChengPara.ShangPinXiuGai)
        updMerchandisePara['goodsConfiguration.id']=goodsId
        updMerchandisePara['goodsConfiguration.goodsNum']=1
        updMerchandisePara['goodsConfiguration.exchangePoints']=2
        JiFenShangChengIntf.updMerchandise(para=updMerchandisePara,files=files)
        #PC端列表检查修改是否正确
        checkPcPara['exchangePoints']=updMerchandisePara['goodsConfiguration.exchangePoints']#兑换需要积分
#         checkPcPara['goodsDetails']=updMerchandisePara['goodsConfiguration.goodsDetails']
        checkPcPara['goodsName']=updMerchandisePara['goodsConfiguration.goodsName']
        checkPcPara['goodsNum']=updMerchandisePara['goodsConfiguration.goodsNum']
        checkPcPara['goodsProfile']=updMerchandisePara['goodsConfiguration.goodsProfile']
        result=JiFenShangChengIntf.checkMerchandiseInList(listPcpara,checkPcPara)
        self.assertTrue(result, '检查PC端商品列表出错')        
        #手机端列表检查修改是否正确
        checkPara['exchangePoints']=updMerchandisePara['goodsConfiguration.exchangePoints']#兑换需要积分
#         checkPara['goodsDetails']=updMerchandisePara['goodsConfiguration.goodsDetails']
        checkPara['goodsName']=updMerchandisePara['goodsConfiguration.goodsName']
        checkPara['goodsNum']=updMerchandisePara['goodsConfiguration.goodsNum']
        checkPara['goodsProfile']=updMerchandisePara['goodsConfiguration.goodsProfile']        
        result=checkMerchandiseInListForMobile(listpara=listPara,checkpara=checkPara)
        self.assertTrue(result, '手机端查看商品列表失败')
        #修改功能验证通过
        Log.LogOutput(message='修改功能验证通过')
        #删除商品
        JiFenShangChengIntf.delMerchandise({'ids[]':goodsId})
        #PC端验证
        result=JiFenShangChengIntf.checkMerchandiseInList(listPcpara,checkPcPara)
        self.assertFalse(result, '检查PC端商品列表出错')
        #手机端验证
        result=checkMerchandiseInListForMobile(listpara=listPara,checkpara=checkPara)
        self.assertFalse(result, '手机端查看商品列表失败')
        Log.LogOutput(message='删除验证通过!')                     
        pass

    def test_YwJiFenShangCheng_03(self):
        '''运维平台-积分商城商品搜索-885'''
        #新增后台商品,默认上架状态
        addMerchandisePara=copy.deepcopy(JiFenShangChengPara.ShangPinXinZeng)
        addMerchandisePara['goodsConfiguration.goodsNum']=10
        addMerchandisePara['goodsConfiguration.exchangePoints']=3
        addMerchandisePara['goodsConfiguration.goodsNo']='S'+time.strftime("%Y%m%d%H%M%S")+createRandomNumber(length=3)
#         addMerchandisePara['goodsConfiguration.quota']=100
        addMerchandisePara['goodsConfiguration.shippingMethod']='0'
        #文件参数
        files = {
                 'iosImgValue':open('C:/autotest_file/Tulips.jpg', 'rb'),
                'androidImgValue':open('C:/autotest_file/Penguins.jpg','rb')
                }     
#         files = [ ('iosImgValue',('Tulips.jpg',open('C:/autotest_file/Tulips.jpg', 'rb'),'image/jpeg')),
#                 ('androidImgValue',('Penguins.jpg',open('C:/autotest_file/Penguins.jpg','rb'),'image/jpeg'))
#                 ]
        JiFenShangChengIntf.addMerchandise(para=addMerchandisePara,files=files)
        #新增第二条
        addMerchandisePara2=copy.deepcopy(JiFenShangChengPara.ShangPinXinZeng)
        addMerchandisePara2['goodsConfiguration.goodsType']=0
        addMerchandisePara2['goodsConfiguration.goodsNum']=10
        addMerchandisePara2['goodsConfiguration.exchangePoints']=3
        addMerchandisePara2['goodsConfiguration.goodsNo']='S'+time.strftime("%Y%m%d%H%M%S")+createRandomNumber(length=3)
        addMerchandisePara2['goodsConfiguration.quota']=100
        addMerchandisePara2['goodsConfiguration.operators']=0
        addMerchandisePara2['goodsConfiguration.goodsDetails']=None
        #商品名称参数重新设置，以免与第一条重复
        addMerchandisePara2['goodsConfiguration.goodsName']='商品名称' + CommonUtil.createRandomString()
        files = {
                 'iosImgValue':open('C:/autotest_file/Tulips.jpg', 'rb'),
                'androidImgValue':open('C:/autotest_file/Penguins.jpg','rb')
                }    
        JiFenShangChengIntf.addMerchandise(para=addMerchandisePara2,files=files)
        
        #数据1检查参数
        checkPcPara1=copy.deepcopy(JiFenShangChengPara.ShangPinLieBiaoCheck)
        checkPcPara1['goodsName']=addMerchandisePara['goodsConfiguration.goodsName']
        checkPcPara1['goodsProfile']=addMerchandisePara['goodsConfiguration.goodsProfile']
        checkPcPara1['goodsDetails']=addMerchandisePara['goodsConfiguration.goodsDetails']
        checkPcPara1['goodsType']=addMerchandisePara['goodsConfiguration.goodsType']
        checkPcPara1['exchangePoints']=addMerchandisePara['goodsConfiguration.exchangePoints']
        checkPcPara1['goodsNo']=addMerchandisePara['goodsConfiguration.goodsNo']
        listPcpara=copy.deepcopy(JiFenShangChengPara.ShangPinLieBiao)
        #不添加搜索参数时，列表中可以检测到数据
        listPcpara['goodsConfiguration.goodsName']=''
        result1=JiFenShangChengIntf.checkMerchandiseInList(listPcpara,checkPcPara1)
        self.assertTrue(result1, '检查PC端商品列表出错')
        #列表参数添加搜索参数，列表中依然可以检测到数据
        listPcpara['goodsConfiguration.goodsName']=addMerchandisePara['goodsConfiguration.goodsName']
        result1=JiFenShangChengIntf.checkMerchandiseInList(listPcpara,checkPcPara1)
        self.assertTrue(result1, '检查PC端商品列表出错')
            
        #数据2检查参数
        checkPcPara2=copy.deepcopy(JiFenShangChengPara.ShangPinLieBiaoCheck)
        checkPcPara2['goodsName']=addMerchandisePara2['goodsConfiguration.goodsName']
        checkPcPara2['goodsProfile']=addMerchandisePara2['goodsConfiguration.goodsProfile']
        checkPcPara2['goodsType']=addMerchandisePara2['goodsConfiguration.goodsType']
        checkPcPara2['exchangePoints']=addMerchandisePara2['goodsConfiguration.exchangePoints']
        checkPcPara2['quota']=addMerchandisePara2['goodsConfiguration.quota']
        checkPcPara2['goodsNo']=addMerchandisePara2['goodsConfiguration.goodsNo']
        #不添加搜索参数时，列表中可以检测到数据
        listPcpara['goodsConfiguration.goodsName']=''
        result2=JiFenShangChengIntf.checkMerchandiseInList(listPcpara,checkPcPara2)
        self.assertTrue(result2, '检查PC端商品列表出错')
        #列表参数添加搜索参数，列表中不可以检测到数据
        listPcpara['goodsConfiguration.goodsName']=addMerchandisePara['goodsConfiguration.goodsName']
        result2=JiFenShangChengIntf.checkMerchandiseInList(listPcpara,checkPcPara2)
        self.assertFalse(result2, '检查PC端商品列表出错')
        Log.LogOutput( message='搜索功能验证通过！')    
        pass  
    
    def test_YwJiFenShangCheng_04(self):
        """运维平台-积分商城-积分配置-490/802"""
        #初始化积分配置
        if Global.simulationEnvironment is False:
            #仿真环境跳过
            JiFenShangChengIntf.initPointSetting()
            #获取登录信息
            resDict=XsInformationSquareIntf.getUserLogin()
            self.assertEqual(resDict['success'], True, '登录验证失败')      
            #获取个人积分
            para1={
                   'tqmobile':'true',
                   'departmentNo':clueOrgInit['DftQuOrgDepNo']
                   }
            result1=XsPaiHangBangIntf.getPersonalPoints(para=para1)
            result1Dict=json.loads(result1.text)
            myPoints0=result1Dict['response']['module']['pointsStatistics']['sumPoints']
            userId=result1Dict['response']['module']['pointsStatistics']['userId']
        #新增一条线索，查看积分是否+1
            addPara=copy.deepcopy(XsBaoLiaoPara.xinZeng2)
            res1=addXianSuo(addPara)
            self.assertTrue(res1.result, '新增线索失败')
            myPoints1=XsPaiHangBangIntf.getPersonalPointsToNum(para1)
            self.assertEquals(myPoints1, myPoints0+1, '新增爆料后积分累计不正确')
            Log.LogOutput( message='新增爆料后积分累计正确')
            #关注线索，查看积分是否加2
            listPara={
                    'tqmobile':'true',
                    'page':'1',
                    'rows':'100'
                      }
            lsr=viewSchedule(para=listPara)
            #查看进度列表结果字典项
            lsrDict=json.loads(lsr.text)
        #新增关注，+2
            addConPara=copy.deepcopy(XsInformationSquarePara.addConPara)
            addConPara['tqmobile']='true'
            addConPara['informationId']=lsrDict['response']['module']['rows'][0]['information']['id']
            addConPara['concernUserId']=lsrDict['response']['module']['rows'][0]['information']['publishUserId']
            res=addConcern(para=addConPara)
            self.assertTrue(res.result, '新增关注失败')
            myPoints2=XsPaiHangBangIntf.getPersonalPointsToNum(para1)
            self.assertEquals(myPoints2, myPoints1+2, '新增关注后积分累计不正确')
            Log.LogOutput( message='新增关注后积分累计正确')
        #新增点赞+3
            addpara=copy.deepcopy(addPraisePara)
            addpara['praiseUserId']=lsrDict['response']['module']['rows'][0]['information']['publishUserId']
            addpara['informationId']=lsrDict['response']['module']['rows'][0]['information']['id']
            res2=addPraise(para=addpara)
            self.assertTrue(res2.result, '新增点赞失败')
            myPoints3=XsPaiHangBangIntf.getPersonalPointsToNum(para1)
            self.assertEquals(myPoints3, myPoints2+3, '新增点赞后积分累计不正确')
            Log.LogOutput( message='新增点赞后积分累计正确')
        #新增评论+4
            addcompara=copy.deepcopy(addCommentPara)
            addcompara['informationId']=lsrDict['response']['module']['rows'][0]['information']['id']
            addcompara['commentUserId']=lsrDict['response']['module']['rows'][0]['information']['publishUserId']
            addcompara['commentType']=0
            res3=addComment(para=addcompara)
            self.assertTrue(res3.text, '新增评论失败')
            myPoints4=XsPaiHangBangIntf.getPersonalPointsToNum(para1)
            self.assertEquals(myPoints4, myPoints3+4, '新增评论后积分累计不正确')
            Log.LogOutput( message='新增评论后积分累计正确')        
        #事件受理，是否加5
            #转事件参数
            addIssuePara=copy.deepcopy(XsInformationSquarePara.culeToIssuePara)
            addIssuePara['information.id']=lsrDict['response']['module']['rows'][0]['information']['id']
            addIssuePara['information.nickName']=lsrDict['response']['module']['rows'][0]['information']['nickName']
            addIssuePara['issue.occurLocation']=lsrDict['response']['module']['rows'][0]['information']['address']
            addIssuePara['issue.issueContent']=lsrDict['response']['module']['rows'][0]['information']['contentText']
            #转事件
    #         addIssuePara['issue.occurDate']=getLinuxDateAndTimeYunWei()
            #发生时间默认往前一小时
            addIssuePara['issue.occurDate']=moveTime2(standardTime=getLinuxDateAndTimeYunWei(),addDay=0,addHour=1,addMinute=0,addSecond=0,moveType=TimeMoveType.MINUS,calcType=TimeCalcType.CALENDARDAY,returnFormat="%Y-%m-%d %H:%M:%S")
            isRes=XsInformationSquareIntf.clueToIssue(para=addIssuePara)
            #等待积分更新
            Time.wait(3)
            myPoints5=XsPaiHangBangIntf.getPersonalPointsToNum(para1)
            self.assertEquals(myPoints5, myPoints4+5, '转事件后积分累计不正确')
            Log.LogOutput( message='转事件积分累计正确')
        #邀请用户+6
            result6=XsInformationSquareIntf.getUserInfo({'tqmobile':'true','id':userId})
            result6Dict=json.loads(result6.text)
            #使用没注册过的用户进行注册
            #获取验证码
            
            #产生一个手机随机号码
            registMobile='123%s'%str(createRandomNumber(length=8))
            count=YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand="select count(*)  from users w where w.mobile='%s'" % registMobile)
            while count>=1:
                registMobile='123%s'%str(createRandomNumber(length=8))
            #获取验证码
            #调用获取验证码方法
            XsGongZuoTaiIntf.getValidateCode(mobile=registMobile)
            userAddPara=copy.deepcopy(XsGongZuoTaiPara.userAddPara)
            #mobileKey采用15位随机数字，防止重复测试时失败
            userAddPara['mobileKey']=createRandomNumber(length=15)
            userAddPara['mobile']=registMobile
            desPara={
                     'key':time.strftime("%Y%m%d"),
                     'value':userAddPara['mobileKey']
            }
            userAddPara['mobileKeyEncrypt']=desEncrypt(para=desPara)
            userAddPara['password']=encodeToMd5('111111')
            res=XsGongZuoTaiIntf.addUser(para=userAddPara)
            self.assertTrue(res.result, '未注册过的手机号注册验证失败')
            Log.LogOutput( message='未注册过的手机号注册验证成功!')
            resDict=json.loads(res.text)
            #采用注册用户新增邀请码
            addInvitePara=copy.deepcopy(XsGongZuoTaiPara.YaoQingMaXinZeng)
            addInvitePara['id']=resDict['response']['module']['id']
            addInvitePara['inviteCode']=result6Dict['response']['module']['inviteCode']
            print addInvitePara
            XsGongZuoTaiIntf.addInviteCode(addInvitePara,mobile=registMobile)
            #验证原用户积分是否+6
            Time.wait(3)
            myPoints6=XsPaiHangBangIntf.getPersonalPointsToNum(para1)
    #         print myPoints5,myPoints6
            self.assertEquals(myPoints6, myPoints5+6, '邀请朋友后积分累计不正确')
            Log.LogOutput( message='邀请朋友后积分累计正确')        
        #用户评分+7
            isResDict=json.loads(isRes.text)
            issuePara=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)
            issuePara['operation.dealOrg.id']=orgInit['DftJieDaoOrgId']
            issuePara['operation.dealUserName']=userInit['DftJieDaoUserXM']
            issuePara['operation.mobile']=userInit['DftJieDaoUserSJ']
            issuePara['operation.content']='结案'       
            issuePara['dealCode']='31'
            issuePara['operation.issue.id']=isResDict['issueId']
            issuePara['keyId']=isResDict['issueStepId']        
            #办结
            result=dealIssue(issueDict=issuePara)
            self.assertTrue(result.result, '办结失败')
            #评价
            #事件评分参数
            addScorePara=copy.deepcopy(TongJiFenXiPara.PingFen)
            addScorePara['publishUserId']=lsrDict['response']['module']['rows'][0]['information']['publishUserId']
            addScorePara['id']=lsrDict['response']['module']['rows'][0]['information']['id']
            addScorePara['score']=5
            TongJiFenXiIntf.addScoreToClue(para=addScorePara)
            #验证评分后积分是否+7
            myPoints7=XsPaiHangBangIntf.getPersonalPointsToNum(para1)
            self.assertEquals(myPoints7, myPoints6+7, '事件评分后积分累计不正确')
            Log.LogOutput( message='事件评分后积分累计正确')
        #验证签到后积分是否+8
            signInPara={'tqmobile':'true','departmentNo':clueOrgInit['DftQuOrgDepNo']}
            #判断当日是否签到
            if XsMyInformationIntf.getUserSignInState({'tqmobile':'true'}) is False:
                #今日签到
                XsMyInformationIntf.userSignIn(signInPara)
                #验证签到后是否+8
                myPoints8=XsPaiHangBangIntf.getPersonalPointsToNum(para1)
                self.assertEquals(myPoints8, myPoints7+8, '签到后积分累计不正确')
                Log.LogOutput( message='签到后积分累计正确----------')
                XsMyInformationIntf.getUserSignInState({'tqmobile':'true'})
            else:
                #如果已经签到过，则积分不变
                myPoints8=myPoints7
            print myPoints8
            #获取当前星期几，如果是星期一，则测试连续签到功能，如果不是，则跳过。该功能每周只能测试一次
            todayWeekNo=datetime.datetime.now().weekday()+1
            if todayWeekNo==1:
                #统计本周签到次数
                count=0
                #验证连续签到后积分是否+9
                try:
                    for i in range(1,8):
                        YunWeiCommonIntf.setWeekdayOnYunWeiLinuxServer(i)
                        #统计累计签到次数
                        if XsMyInformationIntf.getUserSignInState({'tqmobile':'true'}) is False:
                            #今日签到
                            XsMyInformationIntf.userSignIn(signInPara)
                            signResult=XsMyInformationIntf.getUserSignInState({'tqmobile':'true'})
                            print signResult
                            self.assertTrue(signResult,'今日签到失败！')
                            count=count+1
                    if count !=0:
                        #0表示本周已经全部签到过了，再次签到无效，连续签到不会增加积分
                        Time.wait(3)
                        myPoints9=XsPaiHangBangIntf.getPersonalPointsToNum(para1)
                        print myPoints9-myPoints8
                        print count
                        self.assertEquals(myPoints9, myPoints8+65, '连续签到后积分累计不正确')
                        Log.LogOutput( message='连续签到后积分累计正确')
                    else:
                        Log.LogOutput( message='跳过本周连续签到后积分统计验证')
                finally:
        #             将服务器时间改回正确时间
                    YunWeiCommonIntf.setLinuxTimeYunWei(data=getCurrentDateAndTime())        
            #验证注册后基础积分是否为10
            myPoints10=XsPaiHangBangIntf.getPersonalPointsToNum(para1,mobile='12345678901',password='111111')
            self.assertEquals(myPoints10,10, '注册后初始积分不正确')
            Log.LogOutput( message='注册后初始积分正确')
            pass
    
    def test_YwJiFenShangCheng_05(self):
        """运维平台-积分商城-兑换记录-886"""
        #新增后台商品,默认上架状态
        addMerchandisePara=copy.deepcopy(JiFenShangChengPara.ShangPinXinZeng)
        addMerchandisePara['goodsConfiguration.goodsNum']=10
        addMerchandisePara['goodsConfiguration.exchangePoints']=3
        addMerchandisePara['goodsConfiguration.goodsNo']='S'+time.strftime("%Y%m%d%H%M%S")+createRandomNumber(length=3)
#         addMerchandisePara['goodsConfiguration.quota']=100
        addMerchandisePara['goodsConfiguration.shippingMethod']='0'
        #文件参数
        files = {
                 'iosImgValue':open('C:/autotest_file/Tulips.jpg', 'rb'),
                'androidImgValue':open('C:/autotest_file/Penguins.jpg','rb')
                }     
#         files = [ ('iosImgValue',('Tulips.jpg',open('C:/autotest_file/Tulips.jpg', 'rb'),'image/jpeg')),
#                 ('androidImgValue',('Penguins.jpg',open('C:/autotest_file/Penguins.jpg','rb'),'image/jpeg'))
#                 ]
        result=JiFenShangChengIntf.addMerchandise(para=addMerchandisePara,files=files)
        goodsId=json.loads(result.text)['id']
        #设置初始积分为10
        if Global.simulationEnvironment is False:
            XsJiFenShangChengIntf.setPointByMobile(point=10)
        getPointPara={'tqmobile':'true','departmentNo':InitDefaultPara.clueOrgInit['DftQuOrgDepNo']}
        pointNum1=XsPaiHangBangIntf.getPersonalPointsToNum(getPointPara)
        while pointNum1<10:
            addBaoLiaoPara=copy.deepcopy(XsBaoLiaoPara.xinZeng2)    
            #调用新增爆料的方法
            XsBaoLiaoIntf.addXianSuo(XianSuoDict=addBaoLiaoPara)
            pointNum1=XsPaiHangBangIntf.getPersonalPointsToNum(getPointPara)
        #自取实物兑换
        resDict3=XsInformationSquareIntf.getUserLogin(mobile=Global.XianSuoDftMobile,password=Global.XianSuoDftPassword)
        exchangePara=copy.deepcopy(JiFenDuiHuan)
        exchangePara['userNickName']=resDict3['response']['module']['nickName']
        exchangePara['userId']=resDict3['response']['module']['id']
        exchangePara['userMobile']=resDict3['response']['module']['mobile']
        exchangePara['goodsName']=addMerchandisePara['goodsConfiguration.goodsName']
        exchangePara['goodsType']=addMerchandisePara['goodsConfiguration.goodsType']
        exchangePara['exchangeNum']=4
        exchangePara['exchangePoints']=addMerchandisePara['goodsConfiguration.exchangePoints']
        exchangePara['departmentNo']=addMerchandisePara['goodsConfiguration.departmentNo']
        exchangePara['orgName']=addMerchandisePara['goodsConfiguration.orgName']
        exchangePara['goodsConfigurationId']=goodsId
        exchangePara['exchangeOverDate']=''
        exchangePara['name']='张三'
        exchangePara['IdentityCard']='111111111111111'
        exchangePara['goodsNo']=addMerchandisePara['goodsConfiguration.goodsNo']
        exchangePara['shippingMethod']=addMerchandisePara['goodsConfiguration.shippingMethod']
#         exchangePara['receiptUser']='接收用户'
#         exchangePara['receiptAdress']='接收地址'
#         exchangePara['receiptMobile']='12345678901'
        result4=exchangeMerchandise(para=exchangePara) 
        self.assertTrue(result4.result, '自取实物兑换失败')
        #后台兑换
        exchangeCode=json.loads(result4.text)['response']['module']['exchangeCode']
        confirmPara=copy.deepcopy(JiFenShangChengPara.ShiWuZiQu)
        confirmPara['id']=json.loads(result4.text)['response']['module']['id']
        confirmPara['userMobile']=exchangePara['userMobile']
        confirmPara['exchangeCode']='123'
        #输入错误的兑换码进行兑换
        res=JiFenShangChengIntf.confirmPhysicalGoodsExchange(confirmPara)
        self.assertFalse(res.result, '兑换验证失败!')
        #输入错误的手机号码进行兑换
        confirmPara['userMobile']='11111111111'
        confirmPara['exchangeCode']=exchangeCode
        res=JiFenShangChengIntf.confirmPhysicalGoodsExchange(confirmPara)
        self.assertFalse(res.result, '兑换验证失败!')
        #输入正确的手机和兑换码
        confirmPara['userMobile']=exchangePara['userMobile']
        res=JiFenShangChengIntf.confirmPhysicalGoodsExchange(confirmPara)
        self.assertTrue(res.result, '兑换验证失败!')
        #添加备注
        addRemarkPara={
                       'ids':confirmPara['id'],
                       'remarks':'备注内容'+CommonUtil.createRandomString()
                       }
        JiFenShangChengIntf.updateRemark(addRemarkPara)
        #检查兑换和备注后列表字段显示是否正确
        checkConfirmPara=copy.deepcopy(JiFenShangChengPara.DuiHuanJiLuJianCha)
        checkConfirmPara['exchangeCode']=exchangeCode
        checkConfirmPara['exchangeState']=1
        checkConfirmPara['remarks']=addRemarkPara['remarks']
        listPara=copy.deepcopy(JiFenShangChengPara.DuiHuanJiLuLieBiao)
        res=JiFenShangChengIntf.checkExchangeRecordInList(listPara,checkConfirmPara)
        self.assertTrue(res, '检查兑换记录列表失败')
        #验证手机端显示
        #验证兑换记录是否正确
        viewExchangeRecordPara=copy.deepcopy(DuiHuanJiLu)
        viewExchangeRecordPara['userId']=exchangePara['userId']
        checkExchangeRecordPara={
            'exchangeCode':exchangeCode,
            'id':confirmPara['id'],
            'userMobile':exchangePara['userMobile'],
            'userNickName':exchangePara['userNickName'],
            'exchangeState':checkConfirmPara['exchangeState']
                                 }
        res=checkExchangeRecord(listpara=viewExchangeRecordPara,checkpara=checkExchangeRecordPara)
        self.assertTrue(res, '查看手机端兑换记录列表验证失败')
        
        #新增一条手机卡类型的商品
        addMerchandisePara2=copy.deepcopy(JiFenShangChengPara.ShangPinXinZeng)
        addMerchandisePara2['goodsConfiguration.goodsType']=0
        addMerchandisePara2['goodsConfiguration.goodsNum']=10
        addMerchandisePara2['goodsConfiguration.exchangePoints']=3
        addMerchandisePara2['goodsConfiguration.goodsNo']='S'+time.strftime("%Y%m%d%H%M%S")+createRandomNumber(length=3)
        addMerchandisePara2['goodsConfiguration.quota']=10
        addMerchandisePara2['goodsConfiguration.operators']=0
        addMerchandisePara2['goodsConfiguration.goodsDetails']=None
        addMerchandisePara2['goodsConfiguration.goodsName']='手机卡' + CommonUtil.createRandomString()
        addMerchandisePara2['goodsConfiguration.shippingMethod']=1
        files = {
                 'iosImgValue':open('C:/autotest_file/Tulips.jpg', 'rb'),
                'androidImgValue':open('C:/autotest_file/Penguins.jpg','rb')
                }    
        result2=JiFenShangChengIntf.addMerchandise(para=addMerchandisePara2,files=files)
        goodsId2=json.loads(result2.text)['id']
        #配置活动
        addActivityPara={
                'startDate':Time.getCurrentDate(),
                'endDate':Time.getCurrentDate(),
                'activeTimeConfiguration.goodsType':'0',
                'activeTimeConfiguration.exchangeCeiling':'20',
                'activeTimeConfiguration.goodsTotal':'30',
                'activeTimeConfiguration.departmentNo':'959595',
                'activeTimeConfiguration.orgName':'自动化区',
                         }
        addActivityPara['activeTimeConfiguration.activityNo']='HD'+time.strftime("%Y%m")+addActivityPara['activeTimeConfiguration.departmentNo']+createRandomNumber(length=4)
        JiFenShangChengIntf.addActivity(addActivityPara)
        #兑换
        exchangePara2=copy.deepcopy(JiFenDuiHuan)
        exchangePara2['userNickName']=resDict3['response']['module']['nickName']
        exchangePara2['userId']=resDict3['response']['module']['id']
        exchangePara2['userMobile']=resDict3['response']['module']['mobile']
        exchangePara2['goodsName']=addMerchandisePara2['goodsConfiguration.goodsName']
        exchangePara2['goodsType']=addMerchandisePara2['goodsConfiguration.goodsType']
        exchangePara2['exchangeNum']=1
        exchangePara2['exchangePoints']=addMerchandisePara2['goodsConfiguration.exchangePoints']
        exchangePara2['departmentNo']=addMerchandisePara2['goodsConfiguration.departmentNo']
        exchangePara2['orgName']=addMerchandisePara2['goodsConfiguration.orgName']
        exchangePara2['goodsConfigurationId']=goodsId2
#         exchangePara2['exchangeOverDate']=''
        exchangePara2['name']='张三'
        exchangePara2['IdentityCard']='111111111111111'
        exchangePara2['goodsNo']=addMerchandisePara2['goodsConfiguration.goodsNo']
        exchangePara2['shippingMethod']=addMerchandisePara2['goodsConfiguration.shippingMethod']
        exchangePara2['receiptUser']='接收用户'
        exchangePara2['receiptAdress']='接收地址'
        exchangePara2['receiptMobile']='12345678901'
        exchangePara2['operators']=0
        exchangePara2['activityNo']=addActivityPara['activeTimeConfiguration.activityNo']
        exchangePara2['quota']=addMerchandisePara2['goodsConfiguration.quota']
        result2=exchangeMerchandise(para=exchangePara2) 
        self.assertTrue(result2.result, '自取手机卡兑换失败')
        #后台取消订单
        res=JiFenShangChengIntf.cancelOrder({'id':json.loads(result2.text)['response']['module']['id']})
        self.assertTrue(res.result, '取消订单失败!')
        #检查列表状态
        checkConfirmPara2=copy.deepcopy(JiFenShangChengPara.DuiHuanJiLuJianCha)
        checkConfirmPara2['exchangeState']=2
        checkConfirmPara2['goodsName']=addMerchandisePara2['goodsConfiguration.goodsName']
        listPara=copy.deepcopy(JiFenShangChengPara.DuiHuanJiLuLieBiao)
        res=JiFenShangChengIntf.checkExchangeRecordInList(listPara,checkConfirmPara2)
        self.assertTrue(res, '检查兑换记录列表失败')
        #检查手机端兑换记录显示
        viewExchangeRecordPara2=copy.deepcopy(DuiHuanJiLu)
        viewExchangeRecordPara2['userId']=exchangePara2['userId']
        checkExchangeRecordPara2={
            'id':json.loads(result2.text)['response']['module']['id'],
            'userMobile':exchangePara2['userMobile'],
            'userNickName':exchangePara2['userNickName'],
            'exchangeState':checkConfirmPara2['exchangeState']
                                 }
        res=checkExchangeRecord(listpara=viewExchangeRecordPara2,checkpara=checkExchangeRecordPara2)
        self.assertTrue(res, '查看手机端兑换记录列表验证失败')            
        pass
    
    def test_YwJiFenShangCheng_06(self):
        """运维平台-积分商城-兑换记录高级搜索-612仿真跳过"""
        if Global.simulationEnvironment is False:        
            try:
                #第一条商品兑换时间改为2016-6-6
                data='2016-6-6 '+Time.getCurrentTime()
                YunWeiCommonIntf.setLinuxTimeYunWei(data)
                #新增后台商品,默认上架状态
                addMerchandisePara=copy.deepcopy(JiFenShangChengPara.ShangPinXinZeng)
                addMerchandisePara['goodsConfiguration.goodsNum']=10
                addMerchandisePara['goodsConfiguration.exchangePoints']=3
                addMerchandisePara['goodsConfiguration.goodsNo']='S'+time.strftime("%Y%m%d%H%M%S")+createRandomNumber(length=3)
        #         addMerchandisePara['goodsConfiguration.quota']=100
                addMerchandisePara['goodsConfiguration.shippingMethod']='0'
                #文件参数
                files = {
                         'iosImgValue':open('C:/autotest_file/Tulips.jpg', 'rb'),
                        'androidImgValue':open('C:/autotest_file/Penguins.jpg','rb')
                        }     
                result=JiFenShangChengIntf.addMerchandise(para=addMerchandisePara,files=files)
                goodsId=json.loads(result.text)['id']
                #设置初始积分为100
                XsJiFenShangChengIntf.setPointByMobile(point=100)
                #自取实物兑换
                resDict3=XsInformationSquareIntf.getUserLogin(mobile=Global.XianSuoDftMobile,password=Global.XianSuoDftPassword)
                exchangePara=copy.deepcopy(JiFenDuiHuan)
                exchangePara['userNickName']=resDict3['response']['module']['nickName']
                exchangePara['userId']=resDict3['response']['module']['id']
                exchangePara['userMobile']=resDict3['response']['module']['mobile']
                exchangePara['goodsName']=addMerchandisePara['goodsConfiguration.goodsName']
                exchangePara['goodsType']=addMerchandisePara['goodsConfiguration.goodsType']
                exchangePara['exchangeNum']=4
                exchangePara['exchangePoints']=addMerchandisePara['goodsConfiguration.exchangePoints']
                exchangePara['departmentNo']=addMerchandisePara['goodsConfiguration.departmentNo']
                exchangePara['orgName']=addMerchandisePara['goodsConfiguration.orgName']
                exchangePara['goodsConfigurationId']=goodsId
                exchangePara['exchangeOverDate']=''
                exchangePara['name']='张三'
                exchangePara['IdentityCard']='111111111111111'
                exchangePara['goodsNo']=addMerchandisePara['goodsConfiguration.goodsNo']
                exchangePara['shippingMethod']=addMerchandisePara['goodsConfiguration.shippingMethod']
        #         exchangePara['receiptUser']='接收用户'
        #         exchangePara['receiptAdress']='接收地址'
        #         exchangePara['receiptMobile']='12345678901'
                result4=exchangeMerchandise(para=exchangePara) 
                self.assertTrue(result4.result, '自取实物兑换失败')
                #后台兑换
                exchangeCode=json.loads(result4.text)['response']['module']['exchangeCode']
                confirmPara=copy.deepcopy(JiFenShangChengPara.ShiWuZiQu)
                confirmPara['id']=json.loads(result4.text)['response']['module']['id']
                confirmPara['userMobile']=exchangePara['userMobile']
                confirmPara['exchangeCode']=exchangeCode
                #输入正确的手机和兑换码
                res=JiFenShangChengIntf.confirmPhysicalGoodsExchange(confirmPara)
                self.assertTrue(res.result, '兑换验证失败!')
            finally:
                    #恢复正常事件
                    data=Time.getCurrentDateAndTime()
                    YunWeiCommonIntf.setLinuxTimeYunWei(data)
            #新增一条手机卡类型的商品
            addMerchandisePara2=copy.deepcopy(JiFenShangChengPara.ShangPinXinZeng)
            addMerchandisePara2['goodsConfiguration.goodsType']=0
            addMerchandisePara2['goodsConfiguration.goodsNum']=10
            addMerchandisePara2['goodsConfiguration.exchangePoints']=3
            addMerchandisePara2['goodsConfiguration.goodsNo']='S'+time.strftime("%Y%m%d%H%M%S")+createRandomNumber(length=3)
            addMerchandisePara2['goodsConfiguration.quota']=10
            addMerchandisePara2['goodsConfiguration.operators']=0
            addMerchandisePara2['goodsConfiguration.goodsDetails']=None
            addMerchandisePara2['goodsConfiguration.goodsName']='手机卡' + CommonUtil.createRandomString()
            addMerchandisePara2['goodsConfiguration.shippingMethod']=1
            files = {
                     'iosImgValue':open('C:/autotest_file/Tulips.jpg', 'rb'),
                    'androidImgValue':open('C:/autotest_file/Penguins.jpg','rb')
                    }    
            result2=JiFenShangChengIntf.addMerchandise(para=addMerchandisePara2,files=files)
            goodsId2=json.loads(result2.text)['id']
            #配置活动
            addActivityPara={
                    'startDate':Time.getCurrentDate(),
                    'endDate':Time.getCurrentDate(),
                    'activeTimeConfiguration.goodsType':'0',
                    'activeTimeConfiguration.exchangeCeiling':'20',
                    'activeTimeConfiguration.goodsTotal':'30',
                    'activeTimeConfiguration.departmentNo':'959595',
                    'activeTimeConfiguration.orgName':'自动化区',
                             }
            addActivityPara['activeTimeConfiguration.activityNo']='HD'+time.strftime("%Y%m")+addActivityPara['activeTimeConfiguration.departmentNo']+createRandomNumber(length=4)
            JiFenShangChengIntf.addActivity(addActivityPara)
            #兑换
            exchangePara2=copy.deepcopy(JiFenDuiHuan)
            exchangePara2['userNickName']=resDict3['response']['module']['nickName']
            exchangePara2['userId']=resDict3['response']['module']['id']
            exchangePara2['userMobile']=resDict3['response']['module']['mobile']
            exchangePara2['goodsName']=addMerchandisePara2['goodsConfiguration.goodsName']
            exchangePara2['goodsType']=addMerchandisePara2['goodsConfiguration.goodsType']
            exchangePara2['exchangeNum']=1
            exchangePara2['exchangePoints']=addMerchandisePara2['goodsConfiguration.exchangePoints']
            exchangePara2['departmentNo']=addMerchandisePara2['goodsConfiguration.departmentNo']
            exchangePara2['orgName']=addMerchandisePara2['goodsConfiguration.orgName']
            exchangePara2['goodsConfigurationId']=goodsId2
    #         exchangePara2['exchangeOverDate']=''
            exchangePara2['name']='张三'
            exchangePara2['IdentityCard']='111111111111111'
            exchangePara2['goodsNo']=addMerchandisePara2['goodsConfiguration.goodsNo']
            exchangePara2['shippingMethod']=addMerchandisePara2['goodsConfiguration.shippingMethod']
            exchangePara2['receiptUser']='接收用户'
            exchangePara2['receiptAdress']='接收地址'
            exchangePara2['receiptMobile']='12345678901'
            exchangePara2['operators']=0
            exchangePara2['activityNo']=addActivityPara['activeTimeConfiguration.activityNo']
            exchangePara2['quota']=addMerchandisePara2['goodsConfiguration.quota']
            result2=exchangeMerchandise(para=exchangePara2) 
            self.assertTrue(result2.result, '自取手机卡兑换失败')
            #后台取消订单
            res=JiFenShangChengIntf.cancelOrder({'id':json.loads(result2.text)['response']['module']['id']})
            self.assertTrue(res.result, '取消订单失败!')
            #高级查询
            #查询物品类型
            listPara=copy.deepcopy(JiFenShangChengPara.DuiHuanJiLuLieBiao)
            listPara['exchangeRecord.goodsType']=0
            listPara['exchangeRecord.exchangeState']=''
            listPara['exchangeRecord.orderNo']=''
            listPara['startDate']='2016-6-6'
            listPara['endDate']=Time.getCurrentDate()
            #检查搜索后的数据是否正确goodsType为0的存在
            checkPara=copy.deepcopy(JiFenShangChengPara.DuiHuanJiLuJianCha)
    #         checkPara['exchangeState']=2
    #         checkPara['goodsName']=addMerchandisePara2['goodsConfiguration.goodsName']
            checkPara['goodsType']=listPara['exchangeRecord.goodsType']
            res=JiFenShangChengIntf.checkExchangeRecordInList(listPara,checkPara)
            self.assertTrue(res, '检查兑换记录列表失败')
            #goodsType为1的不存在
            checkPara['goodsType']=1
            res=JiFenShangChengIntf.checkExchangeRecordInList(listPara,checkPara)
            self.assertFalse(res, '检查兑换记录列表失败')
            Log.LogOutput( message='物品类型搜索验证通过')
            #兑换状态查询
            listPara['exchangeRecord.goodsType']=''
            listPara['exchangeRecord.exchangeState']=2
            checkPara['goodsType']=None
            checkPara['exchangeState']=2
            res=JiFenShangChengIntf.checkExchangeRecordInList(listPara,checkPara)
            self.assertTrue(res, '检查兑换记录列表失败')
            checkPara['exchangeState']=1
            res=JiFenShangChengIntf.checkExchangeRecordInList(listPara,checkPara)
            self.assertFalse(res, '检查兑换记录列表失败')
            Log.LogOutput( message='兑换状态搜索验证通过')
            #搜索订单编号orderNo
            listPara['exchangeRecord.exchangeState']=''
            result=JiFenShangChengIntf.getExchangeRecordList(listPara)
            orderNo1=json.loads(result.text)['rows'][0]['orderNo']
            orderNo2=json.loads(result.text)['rows'][1]['orderNo']
            listPara['exchangeRecord.orderNo']=orderNo1
            checkPara['exchangeState']=None
            checkPara['orderNo']=orderNo1
            res=JiFenShangChengIntf.checkExchangeRecordInList(listPara,checkPara)
            self.assertTrue(res, '检查兑换记录列表失败')
            checkPara['orderNo']=orderNo2
            res=JiFenShangChengIntf.checkExchangeRecordInList(listPara,checkPara)
            self.assertFalse(res, '检查兑换记录列表失败')
            Log.LogOutput( message='订单编号搜索验证通过')
            #搜索申请兑换开始时间和结束时间
            listPara['exchangeRecord.orderNo']=''
            listPara['startDate']=Time.getCurrentDate()
            checkPara['orderNo']=None
            #第一条数据是2016-6-6兑换的，第二条数据是今天兑换的
            checkPara['goodsName']=addMerchandisePara2['goodsConfiguration.goodsName']
            res=JiFenShangChengIntf.checkExchangeRecordInList(listPara,checkPara)
            self.assertTrue(res, '检查兑换记录列表失败')
            checkPara['goodsName']=addMerchandisePara['goodsConfiguration.goodsName']
            res=JiFenShangChengIntf.checkExchangeRecordInList(listPara,checkPara)
            self.assertFalse(res, '检查兑换记录列表失败')              
            pass    

    def test_YwJiFenShangCheng_07(self):
        """运维平台-积分商城-活动时间配置（新增、修改、删除、查询）-795"""
        #新增
        addActivityPara={
                'startDate':Time.getCurrentDate(),
                'endDate':Time.getCurrentDate(),
                'activeTimeConfiguration.goodsType':'0',
                'activeTimeConfiguration.exchangeCeiling':20,
                'activeTimeConfiguration.goodsTotal':30,
                'activeTimeConfiguration.departmentNo':clueOrgInit['DftQuOrgDepNo'],
                'activeTimeConfiguration.orgName':'杭州大江东产业集聚区',
                         }
        addActivityPara['activeTimeConfiguration.activityNo']='HD'+time.strftime("%Y%m")+addActivityPara['activeTimeConfiguration.departmentNo']+createRandomNumber(length=4)
        res=JiFenShangChengIntf.addActivity(addActivityPara)
        resDict=json.loads(res.text)
        listPara=copy.deepcopy(JiFenShangChengPara.HuoDongLieBiao)
        checkPara={
                'activityNo':addActivityPara['activeTimeConfiguration.activityNo'],
                'goodsTotal':addActivityPara['activeTimeConfiguration.goodsTotal'],
                'departmentNo':addActivityPara['activeTimeConfiguration.departmentNo'],
                'exchangeCeiling':addActivityPara['activeTimeConfiguration.exchangeCeiling']          
                   }
        result=JiFenShangChengIntf.checkInActivityList(listPara, checkPara)
        self.assertTrue(result, '列表检查新增功能失败')
        #修改活动
        updPara={
                'activeTimeConfiguration.id':resDict['id'],
                'startDate':addActivityPara['startDate'],
                'endDate':addActivityPara['endDate'],
                'activeTimeConfiguration.goodsType':addActivityPara['activeTimeConfiguration.goodsType'],
                'activeTimeConfiguration.exchangeCeiling':addActivityPara['activeTimeConfiguration.exchangeCeiling'],
                'exchangeCeilingUp':10,
                'activeTimeConfiguration.goodsTotal':addActivityPara['activeTimeConfiguration.goodsTotal'],
                'goodsTotalUp':20,
                'activeTimeConfiguration.activityNo':addActivityPara['activeTimeConfiguration.activityNo']
                 }
        JiFenShangChengIntf.updActivity(updPara)
        #检查修改是否正确
        checkPara['exchangeCeiling']=updPara['exchangeCeilingUp']+addActivityPara['activeTimeConfiguration.exchangeCeiling']
        checkPara['goodsTotal']=updPara['goodsTotalUp']+addActivityPara['activeTimeConfiguration.goodsTotal']
        result=JiFenShangChengIntf.checkInActivityList(listPara, checkPara)
        self.assertTrue(result, '列表检查新增功能失败')
        #查询
        searchPara=copy.deepcopy(JiFenShangChengPara.HuoDongLieBiao)
        searchPara['activeTimeConfiguration.activityNo']='123'
        result=JiFenShangChengIntf.checkInActivityList(searchPara, checkPara)
        self.assertFalse(result, '列表检查新增功能失败')
        searchPara['activeTimeConfiguration.activityNo']=addActivityPara['activeTimeConfiguration.activityNo']
        result=JiFenShangChengIntf.checkInActivityList(searchPara, checkPara)
        self.assertTrue(result, '列表检查新增功能失败')
        Log.LogOutput( message='查询功能验证通过!')
        #删除
        JiFenShangChengIntf.delActivity({"ids[]":resDict['id']})
        #验证删除是否正确
        result=JiFenShangChengIntf.checkInActivityList(searchPara, checkPara)
        self.assertFalse(result, '列表检查新增功能失败')
        Log.LogOutput( message='删除功能验证通过!')        
        pass
    
    def test_YwJiFenShangCheng_08(self):
        """运维平台-积分商城-活动时间配置启用/停用余额显示/不显示-887"""
        #设置初始积分为10
        if Global.simulationEnvironment is False:
            XsJiFenShangChengIntf.setPointByMobile(point=10)
        getPointPara={'tqmobile':'true','departmentNo':InitDefaultPara.clueOrgInit['DftQuOrgDepNo']}
        pointNum1=XsPaiHangBangIntf.getPersonalPointsToNum(getPointPara)
        while pointNum1<10:
            addBaoLiaoPara=copy.deepcopy(XsBaoLiaoPara.xinZeng2)    
            #调用新增爆料的方法
            XsBaoLiaoIntf.addXianSuo(XianSuoDict=addBaoLiaoPara)
            pointNum1=XsPaiHangBangIntf.getPersonalPointsToNum(getPointPara)
        #新增
        addActivityPara={
                'startDate':Time.getCurrentDate(),
                'endDate':Time.getCurrentDate(),
                'activeTimeConfiguration.goodsType':'0',
                'activeTimeConfiguration.exchangeCeiling':20,
                'activeTimeConfiguration.goodsTotal':30,
                'activeTimeConfiguration.departmentNo':clueOrgInit['DftQuOrgDepNo'],
                'activeTimeConfiguration.orgName':'杭州大江东产业集聚区',
                         }
        addActivityPara['activeTimeConfiguration.activityNo']='HD'+time.strftime("%Y%m")+addActivityPara['activeTimeConfiguration.departmentNo']+createRandomNumber(length=4)
        res=JiFenShangChengIntf.addActivity(addActivityPara)
        resDict=json.loads(res.text) 
        #新增手机卡类型的商品
        addMerchandisePara=copy.deepcopy(JiFenShangChengPara.ShangPinXinZeng)
        addMerchandisePara['goodsConfiguration.goodsType']=0
        addMerchandisePara['goodsConfiguration.goodsNum']=10
        addMerchandisePara['goodsConfiguration.exchangePoints']=3
        addMerchandisePara['goodsConfiguration.goodsNo']='S'+time.strftime("%Y%m%d%H%M%S")+createRandomNumber(length=3)
        addMerchandisePara['goodsConfiguration.quota']=10
        addMerchandisePara['goodsConfiguration.operators']=0
        addMerchandisePara['goodsConfiguration.goodsDetails']=None
        addMerchandisePara['goodsConfiguration.goodsName']='手机卡' + CommonUtil.createRandomString()
        addMerchandisePara['goodsConfiguration.shippingMethod']=1
        files = {
                 'iosImgValue':open('C:/autotest_file/Tulips.jpg', 'rb'),
                'androidImgValue':open('C:/autotest_file/Penguins.jpg','rb')
                }    
        result=JiFenShangChengIntf.addMerchandise(para=addMerchandisePara,files=files)
        goodsId=json.loads(result.text)['id']   
        #停用
        JiFenShangChengIntf.stopActivity({"ids[]":resDict['id']})
        #兑换
        resDict3=XsInformationSquareIntf.getUserLogin(mobile=Global.XianSuoDftMobile,password=Global.XianSuoDftPassword)
        exchangePara=copy.deepcopy(JiFenDuiHuan)
        exchangePara['userNickName']=resDict3['response']['module']['nickName']
        exchangePara['userId']=resDict3['response']['module']['id']
        exchangePara['userMobile']=resDict3['response']['module']['mobile']
        exchangePara['goodsName']=addMerchandisePara['goodsConfiguration.goodsName']
        exchangePara['goodsType']=addMerchandisePara['goodsConfiguration.goodsType']
        exchangePara['exchangeNum']=1
        exchangePara['exchangePoints']=addMerchandisePara['goodsConfiguration.exchangePoints']
        exchangePara['departmentNo']=addMerchandisePara['goodsConfiguration.departmentNo']
        exchangePara['orgName']=addMerchandisePara['goodsConfiguration.orgName']
        exchangePara['goodsConfigurationId']=goodsId
#         exchangePara['exchangeOverDate']=''
        exchangePara['name']='张三'
        exchangePara['IdentityCard']='111111111111111'
        exchangePara['goodsNo']=addMerchandisePara['goodsConfiguration.goodsNo']
        exchangePara['shippingMethod']=addMerchandisePara['goodsConfiguration.shippingMethod']
        exchangePara['receiptUser']='接收用户'
        exchangePara['receiptAdress']='接收地址'
        exchangePara['receiptMobile']='12345678901'
        exchangePara['operators']=0
        exchangePara['activityNo']=addActivityPara['activeTimeConfiguration.activityNo']
        exchangePara['quota']=addMerchandisePara['goodsConfiguration.quota']
        result=exchangeMerchandise(para=exchangePara) 
#         self.assertFalse(result.result, '自取手机卡兑换失败')#此处有bug
        #启用
        JiFenShangChengIntf.startActivity({"ids[]":resDict['id']})
        result=exchangeMerchandise(para=exchangePara) 
        self.assertTrue(result.result, '自取手机卡兑换失败')
        Log.LogOutput( message='活动配置启动、暂停验证通过')
        #设置不显示余额
        JiFenShangChengIntf.unshowBalance({"ids[]":resDict['id']})
        #查看手机端能否显示余额信息
        para={ "departmentNo": clueOrgInit['DftQuOrgDepNo'],
                "tqmobile": "true"}
        checkBalancePara={
        "activityNo": addActivityPara['activeTimeConfiguration.activityNo'],
        "balanceShow": 1
        }
        result=XsJiFenShangChengIntf.checkBalanceInfo(para, checkBalancePara)
        self.assertTrue(result, '手机端检查余额信息失败')
        #设置显示余额
        JiFenShangChengIntf.showBalance({"ids[]":resDict['id']})
        checkBalancePara['balanceShow']=0
        result=XsJiFenShangChengIntf.checkBalanceInfo(para, checkBalancePara)
        self.assertTrue(result, '手机端检查余额信息失败')        
        pass
    
    def test_YwJiFenShangCheng_09(self):
        """运维平台-积分商城-积分规则，手机端进行查看-492、801"""
        #获取积分规则
        para={'departmentNo':clueOrgInit['DftQuOrgDepNo']}
        response=XiTongPeiZhiIntf.getPointRule(para=para)
#      修改积分规则
        param1 = copy.deepcopy(XiTongPeiZhiPara.updateJiFenGuiZhe)
        if response.result is True:
            param1['id'] =json.loads(response.text)['id']
        param1['departmentNo'] = clueOrgInit['DftQuOrgDepNo']
#         param1['userName'] = clueOrgInit['DftJieDaoUserName']
#         param1['updateUserId'] = clueOrgInit['DftJieDaoUserId']
        param1['notice'] = '测试积分规则%s'% CommonUtil.createRandomString()
        ret = XiTongPeiZhiIntf.updateJiFenGuiZhe(param1)         
        self.assertTrue(ret, '修改失败')    
#      查看是否修改成功
        param = copy.deepcopy(XiTongPeiZhiPara.GuanJianZhi)
        param['notice'] = param1['notice']
        ret = XiTongPeiZhiIntf.chakanJiFenGuiZhe(companyDict=param,departmentNo=param1['departmentNo'])         
        self.assertTrue(ret, '查找失败')
        #手机端验证
        param2={ "departmentNo": clueOrgInit['DftQuOrgDepNo'],
                "tqmobile": "true"}
        result=XsJiFenShangChengIntf.getPointRule(para=param2)
        resultDict=json.loads(result.text)
        self.assertEquals(param['notice'], resultDict['response']['module'], '手机端获取的积分规则与pc端不一致')
        pass
    
    def test_YwJiFenShangCheng_10(self):
        """运维平台-积分商城活动图片配置(跳转类型为“详情”)-796"""
        #清空banner图设置
        JiFenShangChengIntf.delAllBannerPic()
        #配置详情页
        #配置积分商城banner图
        addBannerPara=copy.deepcopy(JiFenShangChengPara.BannerPicAdd)
        addBannerPara['storeImageConfiguration.jumpType']=JumpType.XIANGQING
        addBannerPara['storeImageConfiguration.title']='详情Banner图%s'%CommonUtil.createRandomString()
        addBannerPara['storeImageConfiguration.contentText']='正文内容%s'%CommonUtil.createRandomString()
        bannerfile={
                      'iosImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/banner-android.png', 'rb'),
                      'androidImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/banner-ios.png', 'rb')        
                    }
        response=JiFenShangChengIntf.addBannerPic(para=addBannerPara,files=bannerfile)
        self.assertTrue(response.result, '新增banner图失败')
        id=json.loads(response.text)['id']
        #PC端检查新增是否正常
        listPara=copy.deepcopy(JiFenShangChengPara.BannerPicList)
        checkPara1=copy.deepcopy(JiFenShangChengPara.BannerPicCheck)
        checkPara1['title']=addBannerPara['storeImageConfiguration.title']
        checkPara1['contentText']=addBannerPara['storeImageConfiguration.contentText']
        checkPara1['jumpType']=addBannerPara['storeImageConfiguration.jumpType']
        res1=JiFenShangChengIntf.checkBannerPicInPcList(para=listPara,checkpara=checkPara1)
        self.assertTrue(res1, '新增banner图列表检查失败')
        #开始测试手机接口
        getBannerPicInfoPara=copy.deepcopy(XsJiFenShangChengPara.BannerPicInfo)
        #检查Banner图相关信息参数是否正确
        checkPara11=copy.deepcopy(XsJiFenShangChengPara.BannerPicInfoCheck)
        checkPara11['contentText']=addBannerPara['storeImageConfiguration.contentText']
        checkPara11['title']=addBannerPara['storeImageConfiguration.title']
        checkPara11['jumpType']=addBannerPara['storeImageConfiguration.jumpType']
        response2=XsJiFenShangChengIntf.checkBannerInfo(para=getBannerPicInfoPara,checkpara=checkPara11)
        self.assertTrue(response2, 'Banner图配置验证出现错误')
        #后台关闭Banner图，验证手机端是否能够接收banner图信息
        JiFenShangChengIntf.closeBannerPic(para={'ids[]':id})
        response3=XsJiFenShangChengIntf.checkBannerInfo(para=getBannerPicInfoPara,checkpara=checkPara11)
        self.assertFalse(response3, 'Banner图配置关闭功能验证出现错误')
        Log.LogOutput( message='Banner图打开功能正常')
        #再次打开Banner图，并验证打开功能是否正确
        JiFenShangChengIntf.openBannerPic(para={'ids[]':id})
        response3=XsJiFenShangChengIntf.checkBannerInfo(para=getBannerPicInfoPara,checkpara=checkPara11)
        self.assertTrue(response3, 'Banner图配置关闭功能验证出现错误')
        Log.LogOutput( message='Banner图关闭功能正常')
        #修改banner图
        updBannerPara=copy.deepcopy(JiFenShangChengPara.BannerPicUpd)
        updBannerPara['storeImageConfiguration.id']=id
        updBannerPara['storeImageConfiguration.title']='详情Banner图修改'
        updBannerPara['storeImageConfiguration.contentText']='正文内容修改'
        bannerfile={
                      'iosImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/banner-android.png', 'rb'),
                      'androidImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/banner-ios.png', 'rb')        
                    }
        response2=JiFenShangChengIntf.updBannerPic(para=updBannerPara,files=bannerfile)
        self.assertTrue(response2.result, '修改banner图失败')
        #PC端检查修改是否正常
        listPara=copy.deepcopy(JiFenShangChengPara.BannerPicList)
        checkPara2=copy.deepcopy(JiFenShangChengPara.BannerPicCheck)
        checkPara2['title']=updBannerPara['storeImageConfiguration.title']
        checkPara2['contentText']=updBannerPara['storeImageConfiguration.contentText']
        checkPara2['jumpType']=addBannerPara['storeImageConfiguration.jumpType']#跳转类型不变
        res2=JiFenShangChengIntf.checkBannerPicInPcList(para=listPara,checkpara=checkPara2)
        self.assertTrue(res2, 'PC端修改banner图列表检查失败')
        #手机端检查Banner图相关信息参数是否正确
        checkPara22=copy.deepcopy(XsJiFenShangChengPara.BannerPicInfoCheck)
        checkPara22['contentText']=updBannerPara['storeImageConfiguration.contentText']
        checkPara22['title']=updBannerPara['storeImageConfiguration.title']
        checkPara22['jumpType']=addBannerPara['storeImageConfiguration.jumpType']#跳转类型不变
        response2=XsJiFenShangChengIntf.checkBannerInfo(para=getBannerPicInfoPara,checkpara=checkPara22)
        self.assertTrue(response2, '手机端Banner图配置验证出现错误')
        #查询，需要再加一条数据
        response=JiFenShangChengIntf.addBannerPic(para=addBannerPara,files=bannerfile)
        self.assertTrue(response.result, '新增banner图失败')
        #搜索参数与列表参数一样
        searchPara=copy.deepcopy(JiFenShangChengPara.BannerPicList)
        #以修改后的标题来作为搜索条件，传入修改后检查参数，检查结果为true
        searchPara['storeImageConfiguration.title']=updBannerPara['storeImageConfiguration.title']
        res3=JiFenShangChengIntf.checkBannerPicInPcList(para=searchPara,checkpara=checkPara2)
        self.assertTrue(res3, '查询结果错误')
        #以第二次新增的标题作为检查参数，传入第二条检查参数，检查结果为false
        res4=JiFenShangChengIntf.checkBannerPicInPcList(para=searchPara,checkpara=checkPara1)
        self.assertFalse(res4, '查询结果错误')
        Log.LogOutput(message='查询功能正常')
        #删除
        JiFenShangChengIntf.delAllBannerPic()
        #手机端检查
        response2=XsJiFenShangChengIntf.checkBannerInfo(para=getBannerPicInfoPara,checkpara=checkPara22)
        self.assertFalse(response2, '手机端Banner图配置验证出现错误')
        response3=XsJiFenShangChengIntf.checkBannerInfo(para=getBannerPicInfoPara,checkpara=checkPara11)
        self.assertFalse(response3, '手机端Banner图配置验证出现错误')
        Log.LogOutput(message='删除功能正常')           
        pass

    def test_YwJiFenShangCheng_11(self):
        """运维平台-积分商城转盘抽奖新增、修改、查看-866"""
        #配置大转盘
        addPara=copy.deepcopy(JiFenShangChengPara.ZhuanPanChouJiangXinZeng2)
        DaZhuanPanFile={
                        'iosImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/dazhuanpan.png', 'rb'),
                        'androidImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/dazhuanpan.png', 'rb')    
                }
        response1=JiFenShangChengIntf.addLotteryAllocation(para=addPara,files=DaZhuanPanFile)
        self.assertTrue(response1.result, '新增大转盘配置出错')
        lotteryAllocationId=json.loads(response1.text)['id']
        listPara=copy.deepcopy(JiFenShangChengPara.ZhuanPanChouJiangLieBiao)
        checkPara=copy.deepcopy(JiFenShangChengPara.ZhuanPanChouJiangLieBiaoJianCha)
        checkPara['activityDetails']=addPara['lotteryAllocation.activityDetails']
        checkPara['lotteryActivityNo']=addPara['lotteryAllocation.lotteryActivityNo']
        checkPara['lotteryDayNumber']=addPara['lotteryAllocation.lotteryDayNumber']
        checkPara['lotteryPoints']=addPara['lotteryAllocation.lotteryPoints']
        checkPara['accuracy']=addPara['lotteryAllocation.accuracy']
        res1=JiFenShangChengIntf.checkLotteryAllocationList(listPara, checkPara)
        self.assertTrue(res1, '新增大转盘出错')
        #修改
        updPara=copy.deepcopy(JiFenShangChengPara.ZhuanPanChouJiangXiuGai)
        updPara['lotteryAllocation.id']=lotteryAllocationId
        updPara['lotteryAllocation.activityDetails']='活动详情修改'
        updPara['lotteryAllocation.lotteryDayNumber']=666
        updPara['lotteryAllocation.lotteryPoints']=10
        updPara['lotteryAllocation.accuracy']=100
        response2=JiFenShangChengIntf.updLotteryAllocation(para=updPara,files=DaZhuanPanFile)
        self.assertTrue(response2.result, '修改大转盘配置出错')
        checkPara2=copy.deepcopy(JiFenShangChengPara.ZhuanPanChouJiangLieBiaoJianCha)
        checkPara2['activityDetails']=updPara['lotteryAllocation.activityDetails']
#         checkPara2['lotteryActivityNo']=updPara['lotteryAllocation.lotteryActivityNo']
        checkPara2['lotteryDayNumber']=updPara['lotteryAllocation.lotteryDayNumber']
        checkPara2['lotteryPoints']=updPara['lotteryAllocation.lotteryPoints']
        checkPara2['accuracy']=updPara['lotteryAllocation.accuracy']
        res2=JiFenShangChengIntf.checkLotteryAllocationList(listPara, checkPara2)
        self.assertTrue(res2, '修改大转盘出错')         
        Log.LogOutput( message='修改成功')
        #删除
        JiFenShangChengIntf.delLotteryAllocation(para={'ids[]':lotteryAllocationId})
        res3=JiFenShangChengIntf.checkLotteryAllocationList(listPara, checkPara2)
        self.assertFalse(res3, '删除大转盘出错')         
        Log.LogOutput( message='删除成功')        
        pass    

    def test_YwJiFenShangCheng_12(self):
        """运维平台-积分商城转盘抽奖开启、关闭功能-869"""
        #配置大转盘
        addPara=copy.deepcopy(JiFenShangChengPara.ZhuanPanChouJiangXinZeng2)
        DaZhuanPanFile={
                        'iosImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/dazhuanpan.png', 'rb'),
                        'androidImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/dazhuanpan.png', 'rb')    
                }
        response1=JiFenShangChengIntf.addLotteryAllocation(para=addPara,files=DaZhuanPanFile)
        self.assertTrue(response1.result, '新增大转盘配置出错')
        lotteryAllocationId=json.loads(response1.text)['id']
        listPara=copy.deepcopy(JiFenShangChengPara.ZhuanPanChouJiangLieBiao)
        checkPara=copy.deepcopy(JiFenShangChengPara.ZhuanPanChouJiangLieBiaoJianCha)
        checkPara['activityDetails']=addPara['lotteryAllocation.activityDetails']
        checkPara['lotteryActivityNo']=addPara['lotteryAllocation.lotteryActivityNo']
        checkPara['lotteryDayNumber']=addPara['lotteryAllocation.lotteryDayNumber']
        checkPara['lotteryPoints']=addPara['lotteryAllocation.lotteryPoints']
        checkPara['accuracy']=addPara['lotteryAllocation.accuracy']
        #新增默认状态为关闭
        checkPara['state']=LotteryAllocationState.CLOSE
        res1=JiFenShangChengIntf.checkLotteryAllocationList(listPara, checkPara)
        self.assertTrue(res1, '新增大转默盘默认状态检查出错')
        #开启
        JiFenShangChengIntf.openLotteryAllocation(para={'ids[]':lotteryAllocationId})
        #检查状态改为开启
        checkPara['state']=LotteryAllocationState.OPEN
        res1=JiFenShangChengIntf.checkLotteryAllocationList(listPara, checkPara)
        self.assertTrue(res1, '开启大转默盘后状态检查出错')
        #关闭
        JiFenShangChengIntf.closeLotteryAllocation(para={'ids[]':lotteryAllocationId})
        #检查状态改为开启
        checkPara['state']=LotteryAllocationState.CLOSE
        res1=JiFenShangChengIntf.checkLotteryAllocationList(listPara, checkPara)
        self.assertTrue(res1, '关闭大转默盘后状态检查出错')
        Log.LogOutput( message='开启、关闭功能验证通过！')
        pass

    def test_YwJiFenShangCheng_13(self):
        """运维平台-积分商城转盘抽奖查询、刷新功能-870"""
        addPara1=copy.deepcopy(JiFenShangChengPara.ZhuanPanChouJiangXinZeng2)
        DaZhuanPanFile={
                        'iosImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/dazhuanpan.png', 'rb'),
                        'androidImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/dazhuanpan.png', 'rb')    
                }
        response1=JiFenShangChengIntf.addLotteryAllocation(para=addPara1,files=DaZhuanPanFile)
        self.assertTrue(response1.result, '新增大转盘配置出错')
        #新增第二条
        addPara2=copy.deepcopy(JiFenShangChengPara.ZhuanPanChouJiangXinZeng2)
        addPara2['startDate']='2016-6-6'
        addPara2['endDate']='2016-6-6'
        addPara2['lotteryAllocation.lotteryActivityNo']='ZP' + time.strftime("%Y%m%d") + InitDefaultPara.clueOrgInit['DftQuOrgDepNo'] + createRandomNumber(4)
        response2=JiFenShangChengIntf.addLotteryAllocation(para=addPara2,files=DaZhuanPanFile)
        self.assertTrue(response2.result, '新增大转盘配置出错')
        #搜索
        searchPara=copy.deepcopy(JiFenShangChengPara.ZhuanPanChouJiangLieBiao)
        searchPara['lotteryAllocation.lotteryActivityNo']=addPara1['lotteryAllocation.lotteryActivityNo']
        checkPara1=copy.deepcopy(JiFenShangChengPara.ZhuanPanChouJiangLieBiaoJianCha)
        checkPara1['lotteryActivityNo']=addPara1['lotteryAllocation.lotteryActivityNo']
        #根据第一条数据的活动单号查询，并检查结果列表，预期为true
        res1=JiFenShangChengIntf.checkLotteryAllocationList(searchPara, checkPara1)
        self.assertTrue(res1, '查询出错')
        #根据第二条数据的活动单号来检查结果列表，预期为false
        checkPara2=copy.deepcopy(JiFenShangChengPara.ZhuanPanChouJiangLieBiaoJianCha)
        checkPara2['lotteryActivityNo']=addPara2['lotteryAllocation.lotteryActivityNo']
        res2=JiFenShangChengIntf.checkLotteryAllocationList(searchPara, checkPara2)
        self.assertFalse(res2, '查询出错')
        Log.LogOutput( message='通过活动编号查询功能验证通过!')
        #刷新
        searchPara['lotteryAllocation.lotteryActivityNo']=''
        checkPara1['lotteryActivityNo']=addPara1['lotteryAllocation.lotteryActivityNo']
        #根据第一条数据的活动单号查询，并检查结果列表，预期为true
        res1=JiFenShangChengIntf.checkLotteryAllocationList(searchPara, checkPara1)
        self.assertTrue(res1, '刷新出错')
        #根据第二条数据的活动单号来检查结果列表，预期为true
        checkPara2['lotteryActivityNo']=addPara2['lotteryAllocation.lotteryActivityNo']
        res2=JiFenShangChengIntf.checkLotteryAllocationList(searchPara, checkPara2)        
        self.assertTrue(res2, '刷新出错')
        Log.LogOutput( message='刷新功能验证通过!')
        pass
    
    def test_YwJiFenShangCheng_14(self):
        """运维平台-积分商城转盘奖品配置-876"""
        #配置大转盘
        addPara=copy.deepcopy(JiFenShangChengPara.ZhuanPanChouJiangXinZeng2)
        DaZhuanPanFile={
                        'iosImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/dazhuanpan.png', 'rb'),
                        'androidImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/dazhuanpan.png', 'rb')    
                }
        response1=JiFenShangChengIntf.addLotteryAllocation(para=addPara,files=DaZhuanPanFile)
        self.assertTrue(response1.result, '新增大转盘配置出错')
        lotteryAllocationId=json.loads(response1.text)['id']
        #配置奖项
        listPara=copy.deepcopy(JiFenShangChengPara.JiangPingPeiZhiLieBiao)
        listPara['prizeSetting.lotteryAllocationId']=lotteryAllocationId
        #设置一号奖品参数
        prizePara1=copy.deepcopy(JiFenShangChengPara.JiangPingPeiZhi)
        prizePara1['prizeSetting.id']=JiFenShangChengIntf.getIdByGrade(listPara, prizeGrade=1)
        prizePara1['prizeSetting.goodsType']=GoodsType.PHYSICAL
        prizePara1['prizeSetting.prizeName']='Iphone7'
        prizePara1['prizeSetting.prizeNumber']=100
        prizePara1['prizeSetting.shippingMethod']=ShippingMethod.JISONG
        prizePara1['prizeSetting.intervalStart']=1
        prizePara1['prizeSetting.intervalEnd']=10
        files1={
        'iosImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/ip7.png', 'rb'),
        'androidImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/ip7.png', 'rb')    
                }
        JiFenShangChengIntf.setPrize(para=prizePara1, files=files1)
        #设置二号奖品参数
        prizePara2=copy.deepcopy(JiFenShangChengPara.JiangPingPeiZhi)
        prizePara2['prizeSetting.id']=JiFenShangChengIntf.getIdByGrade(listPara, prizeGrade=2)
        prizePara2['prizeSetting.goodsType']=GoodsType.PHYSICAL
        prizePara2['prizeSetting.prizeName']='iwatch'
        prizePara2['prizeSetting.prizeNumber']='100'
        prizePara2['prizeSetting.shippingMethod']=ShippingMethod.ZIQU
        prizePara2['prizeSetting.intervalStart']='11'
        prizePara2['prizeSetting.intervalEnd']='20'
        files2={
        'iosImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/iWatch.png', 'rb'),
        'androidImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/iWatch.png', 'rb')      
                }
        JiFenShangChengIntf.setPrize(para=prizePara2, files=files2)
        #设置三号奖品参数
        prizePara3=copy.deepcopy(JiFenShangChengPara.JiangPingPeiZhi)
        prizePara3['prizeSetting.id']=JiFenShangChengIntf.getIdByGrade(listPara, prizeGrade=3)
        prizePara3['prizeSetting.goodsType']=GoodsType.PHONECARD
        prizePara3['prizeSetting.prizeName']='500话费充值卡'
        prizePara3['prizeSetting.prizeNumber']='100'
        prizePara3['prizeSetting.shippingMethod']=None
        prizePara3['prizeSetting.intervalStart']='21'
        prizePara3['prizeSetting.intervalEnd']='30'
        prizePara3['prizeSetting.quota']='500'
        files3={
        'iosImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/500.png', 'rb'),
        'androidImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/500.png', 'rb')      
                }
        JiFenShangChengIntf.setPrize(para=prizePara3, files=files3)        
        #设置四号奖品参数 
        prizePara4=copy.deepcopy(JiFenShangChengPara.JiangPingPeiZhi)
        prizePara4['prizeSetting.id']=JiFenShangChengIntf.getIdByGrade(listPara, prizeGrade=4)
        prizePara4['prizeSetting.goodsType']=GoodsType.PHONECARD
        prizePara4['prizeSetting.prizeName']='100话费充值卡'
        prizePara4['prizeSetting.prizeNumber']='100'
        prizePara4['prizeSetting.shippingMethod']=None
        prizePara4['prizeSetting.intervalStart']='31'
        prizePara4['prizeSetting.intervalEnd']='40'
        prizePara4['prizeSetting.quota']='100'
        files4={
        'iosImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/100.png', 'rb'),
        'androidImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/100.png', 'rb')      
                }
        JiFenShangChengIntf.setPrize(para=prizePara4, files=files4)          
        #设置五号奖品参数 
        prizePara5=copy.deepcopy(JiFenShangChengPara.JiangPingPeiZhi)
        prizePara5['prizeSetting.id']=JiFenShangChengIntf.getIdByGrade(listPara, prizeGrade=5)
        prizePara5['prizeSetting.goodsType']=GoodsType.PHONECARD
        prizePara5['prizeSetting.prizeName']='50话费充值卡'
        prizePara5['prizeSetting.prizeNumber']='100'
        prizePara5['prizeSetting.shippingMethod']=None
        prizePara5['prizeSetting.intervalStart']='41'
        prizePara5['prizeSetting.intervalEnd']='50'
        prizePara5['prizeSetting.quota']='50'
        files5={
        'iosImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/50.png', 'rb'),
        'androidImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/50.png', 'rb')      
                }
        JiFenShangChengIntf.setPrize(para=prizePara5, files=files5)  
        #设置六号奖品参数
        prizePara6=copy.deepcopy(JiFenShangChengPara.JiangPingPeiZhi)
        prizePara6['prizeSetting.id']=JiFenShangChengIntf.getIdByGrade(listPara, prizeGrade=6)
        prizePara6['prizeSetting.goodsType']=GoodsType.PHONECARD
        prizePara6['prizeSetting.prizeName']='10话费充值卡'
        prizePara6['prizeSetting.prizeNumber']='100'
        prizePara6['prizeSetting.shippingMethod']=None
        prizePara6['prizeSetting.intervalStart']='51'
        prizePara6['prizeSetting.intervalEnd']='60'
        prizePara6['prizeSetting.quota']='10'
        files6={
        'iosImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/10.png', 'rb'),
        'androidImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/10.png', 'rb')      
                }
        JiFenShangChengIntf.setPrize(para=prizePara6, files=files6)           
        #设置七号奖品参数
        prizePara7=copy.deepcopy(JiFenShangChengPara.JiangPingPeiZhi)
        prizePara7['prizeSetting.id']=JiFenShangChengIntf.getIdByGrade(listPara, prizeGrade=7)
        prizePara7['prizeSetting.goodsType']=GoodsType.POINT
        prizePara7['prizeSetting.prizeName']='10积分'
        prizePara7['prizeSetting.prizeNumber']='100'
        prizePara7['prizeSetting.shippingMethod']=None
        prizePara7['prizeSetting.intervalStart']='61'
        prizePara7['prizeSetting.intervalEnd']='70'
        prizePara7['prizeSetting.quota']='10'
        files7={
        'iosImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/10points.png', 'rb'),
        'androidImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/10points.png', 'rb')      
                }
        JiFenShangChengIntf.setPrize(para=prizePara7, files=files7)          
        #设置八号奖品参数
        prizePara8=copy.deepcopy(JiFenShangChengPara.JiangPingPeiZhi)
        prizePara8['prizeSetting.id']=JiFenShangChengIntf.getIdByGrade(listPara, prizeGrade=8)
        prizePara8['prizeSetting.goodsType']=GoodsType.NONE
        prizePara8['prizeSetting.prizeName']='谢谢参与'
        prizePara8['prizeSetting.prizeNumber']=None
        prizePara8['prizeSetting.shippingMethod']=None
        prizePara8['prizeSetting.intervalStart']='71'
        prizePara8['prizeSetting.intervalEnd']='80'
        prizePara8['prizeSetting.quota']=None
        files8={
        'iosImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/thx.png', 'rb'),
        'androidImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/thx.png', 'rb')      
                }
        JiFenShangChengIntf.setPrize(para=prizePara8, files=files8)   
        #检查一号奖品在列表中是否正确
        JiFenShangChengIntf.getPrizeSettingList(listPara)
        checkPara=copy.deepcopy(JiFenShangChengPara.JiangPingPeiZhiLieBiaoJianCha)
        checkPara['id']=prizePara1['prizeSetting.id']
        checkPara['prizeNumber']=prizePara1['prizeSetting.prizeNumber']
        checkPara['prizeName']=prizePara1['prizeSetting.prizeName']
        checkPara['shippingMethod']=prizePara1['prizeSetting.shippingMethod']
        checkPara['intervalStart']=prizePara1['prizeSetting.intervalStart']
        checkPara['intervalEnd']=prizePara1['prizeSetting.intervalEnd']
        res=JiFenShangChengIntf.checkPrizeSettingList(para=listPara,checkpara=checkPara)
        self.assertTrue(res, '检查一号奖品成功')
        Log.LogOutput(message='商品配置列表检查成功')
        pass
    
    def test_YwJiFenShangCheng_15(self):
        """运维平台- 验证订单操作功能-883"""
        #配置大转盘
        addPara=copy.deepcopy(JiFenShangChengPara.ZhuanPanChouJiangXinZeng2)
        DaZhuanPanFile={
                        'iosImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/dazhuanpan.png', 'rb'),
                        'androidImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/dazhuanpan.png', 'rb')    
                }
        response1=JiFenShangChengIntf.addLotteryAllocation(para=addPara,files=DaZhuanPanFile)
        self.assertTrue(response1.result, '新增大转盘配置出错')
        lotteryAllocationId=json.loads(response1.text)['id']
        #配置奖项
        listPara=copy.deepcopy(JiFenShangChengPara.JiangPingPeiZhiLieBiao)
        listPara['prizeSetting.lotteryAllocationId']=lotteryAllocationId
        #设置一号奖品参数
        prizePara1=copy.deepcopy(JiFenShangChengPara.JiangPingPeiZhi)
        prizePara1['prizeSetting.id']=JiFenShangChengIntf.getIdByGrade(listPara, prizeGrade=1)
        prizePara1['prizeSetting.goodsType']=GoodsType.PHYSICAL
        prizePara1['prizeSetting.prizeName']='Iphone7'
        prizePara1['prizeSetting.prizeNumber']=100
        prizePara1['prizeSetting.shippingMethod']=ShippingMethod.JISONG
        prizePara1['prizeSetting.intervalStart']=1
        prizePara1['prizeSetting.intervalEnd']=10
        files1={
        'iosImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/ip7.png', 'rb'),
        'androidImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/ip7.png', 'rb')    
                }
        JiFenShangChengIntf.setPrize(para=prizePara1, files=files1)
        #设置二号奖品参数
        prizePara2=copy.deepcopy(JiFenShangChengPara.JiangPingPeiZhi)
        prizePara2['prizeSetting.id']=JiFenShangChengIntf.getIdByGrade(listPara, prizeGrade=2)
        prizePara2['prizeSetting.goodsType']=GoodsType.PHYSICAL
        prizePara2['prizeSetting.prizeName']='iwatch'
        prizePara2['prizeSetting.prizeNumber']='100'
        prizePara2['prizeSetting.shippingMethod']=ShippingMethod.ZIQU
        prizePara2['prizeSetting.intervalStart']='11'
        prizePara2['prizeSetting.intervalEnd']='20'
        files2={
        'iosImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/iWatch.png', 'rb'),
        'androidImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/iWatch.png', 'rb')      
                }
        JiFenShangChengIntf.setPrize(para=prizePara2, files=files2)
        #设置三号奖品参数
        prizePara3=copy.deepcopy(JiFenShangChengPara.JiangPingPeiZhi)
        prizePara3['prizeSetting.id']=JiFenShangChengIntf.getIdByGrade(listPara, prizeGrade=3)
        prizePara3['prizeSetting.goodsType']=GoodsType.PHONECARD
        prizePara3['prizeSetting.prizeName']='500话费充值卡'
        prizePara3['prizeSetting.prizeNumber']='100'
        prizePara3['prizeSetting.shippingMethod']=None
        prizePara3['prizeSetting.intervalStart']='21'
        prizePara3['prizeSetting.intervalEnd']='30'
        prizePara3['prizeSetting.quota']='500'
        files3={
        'iosImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/500.png', 'rb'),
        'androidImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/500.png', 'rb')      
                }
        JiFenShangChengIntf.setPrize(para=prizePara3, files=files3)        
        #设置四号奖品参数 
        prizePara4=copy.deepcopy(JiFenShangChengPara.JiangPingPeiZhi)
        prizePara4['prizeSetting.id']=JiFenShangChengIntf.getIdByGrade(listPara, prizeGrade=4)
        prizePara4['prizeSetting.goodsType']=GoodsType.PHONECARD
        prizePara4['prizeSetting.prizeName']='100话费充值卡'
        prizePara4['prizeSetting.prizeNumber']='100'
        prizePara4['prizeSetting.shippingMethod']=None
        prizePara4['prizeSetting.intervalStart']='31'
        prizePara4['prizeSetting.intervalEnd']='40'
        prizePara4['prizeSetting.quota']='100'
        files4={
        'iosImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/100.png', 'rb'),
        'androidImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/100.png', 'rb')      
                }
        JiFenShangChengIntf.setPrize(para=prizePara4, files=files4)          
        #设置五号奖品参数 
        prizePara5=copy.deepcopy(JiFenShangChengPara.JiangPingPeiZhi)
        prizePara5['prizeSetting.id']=JiFenShangChengIntf.getIdByGrade(listPara, prizeGrade=5)
        prizePara5['prizeSetting.goodsType']=GoodsType.PHONECARD
        prizePara5['prizeSetting.prizeName']='50话费充值卡'
        prizePara5['prizeSetting.prizeNumber']='100'
        prizePara5['prizeSetting.shippingMethod']=None
        prizePara5['prizeSetting.intervalStart']='41'
        prizePara5['prizeSetting.intervalEnd']='50'
        prizePara5['prizeSetting.quota']='50'
        files5={
        'iosImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/50.png', 'rb'),
        'androidImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/50.png', 'rb')      
                }
        JiFenShangChengIntf.setPrize(para=prizePara5, files=files5)  
        #设置六号奖品参数
        prizePara6=copy.deepcopy(JiFenShangChengPara.JiangPingPeiZhi)
        prizePara6['prizeSetting.id']=JiFenShangChengIntf.getIdByGrade(listPara, prizeGrade=6)
        prizePara6['prizeSetting.goodsType']=GoodsType.PHONECARD
        prizePara6['prizeSetting.prizeName']='10话费充值卡'
        prizePara6['prizeSetting.prizeNumber']='100'
        prizePara6['prizeSetting.shippingMethod']=None
        prizePara6['prizeSetting.intervalStart']='51'
        prizePara6['prizeSetting.intervalEnd']='60'
        prizePara6['prizeSetting.quota']='10'
        files6={
        'iosImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/10.png', 'rb'),
        'androidImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/10.png', 'rb')      
                }
        JiFenShangChengIntf.setPrize(para=prizePara6, files=files6)           
        #设置七号奖品参数
        prizePara7=copy.deepcopy(JiFenShangChengPara.JiangPingPeiZhi)
        prizePara7['prizeSetting.id']=JiFenShangChengIntf.getIdByGrade(listPara, prizeGrade=7)
        prizePara7['prizeSetting.goodsType']=GoodsType.POINT
        prizePara7['prizeSetting.prizeName']='10积分'
        prizePara7['prizeSetting.prizeNumber']='100'
        prizePara7['prizeSetting.shippingMethod']=None
        prizePara7['prizeSetting.intervalStart']='61'
        prizePara7['prizeSetting.intervalEnd']='70'
        prizePara7['prizeSetting.quota']='10'
        files7={
        'iosImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/10points.png', 'rb'),
        'androidImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/10points.png', 'rb')      
                }
        JiFenShangChengIntf.setPrize(para=prizePara7, files=files7)          
        #设置八号奖品参数
        prizePara8=copy.deepcopy(JiFenShangChengPara.JiangPingPeiZhi)
        prizePara8['prizeSetting.id']=JiFenShangChengIntf.getIdByGrade(listPara, prizeGrade=8)
        prizePara8['prizeSetting.goodsType']=GoodsType.NONE
        prizePara8['prizeSetting.prizeName']='谢谢参与'
        prizePara8['prizeSetting.prizeNumber']=None
        prizePara8['prizeSetting.shippingMethod']=None
        prizePara8['prizeSetting.intervalStart']='71'
        prizePara8['prizeSetting.intervalEnd']='80'
        prizePara8['prizeSetting.quota']=None
        files8={
        'iosImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/thx.png', 'rb'),
        'androidImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/thx.png', 'rb')      
                }
        JiFenShangChengIntf.setPrize(para=prizePara8, files=files8)
        #配置积分商城banner图
        addBannerPara=copy.deepcopy(JiFenShangChengPara.BannerPicAdd)
        addBannerPara['storeImageConfiguration.jumpType']=1
        addBannerPara['storeImageConfiguration.title']='大转盘Banner图'
        addBannerPara['storeImageConfiguration.lotteryAllocationId']=lotteryAllocationId
        addBannerPara['storeImageConfiguration.contentText']='正文内容'
        bannerfile={
                      'iosImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/banner-android.png', 'rb'),
                      'androidImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/banner-ios.png', 'rb')        
                    }
        response2=JiFenShangChengIntf.addBannerPic(para=addBannerPara,files=bannerfile)
        self.assertTrue(response2.result, '新增banner图失败')        
        #设置积分
        #设置初始积分为10
        if Global.simulationEnvironment is False:
            XsJiFenShangChengIntf.setPointByMobile(point=10)
        getPointPara={'tqmobile':'true','departmentNo':InitDefaultPara.clueOrgInit['DftQuOrgDepNo']}
        pointNum1=XsPaiHangBangIntf.getPersonalPointsToNum(getPointPara)
        while pointNum1<10:
            addBaoLiaoPara=copy.deepcopy(XsBaoLiaoPara.xinZeng2)    
            #调用新增爆料的方法
            XsBaoLiaoIntf.addXianSuo(XianSuoDict=addBaoLiaoPara)
            pointNum1=XsPaiHangBangIntf.getPersonalPointsToNum(getPointPara)
        #开启大转盘活动
        JiFenShangChengIntf.openLotteryAllocation({'ids[]':lotteryAllocationId})
        #抽奖
        addLotteryPara=copy.deepcopy(XsJiFenShangChengPara.ChouJiang)
        addLotteryPara['lotteryActivityNo']=addPara['lotteryAllocation.lotteryActivityNo']
        response1=XsJiFenShangChengIntf.addLotteryRecord(para=addLotteryPara)
        self.assertTrue(response1.result, '抽奖验证失败')
        lotteryRecordId=json.loads(response1.text)['response']['module']['lotteryRecordId']
        resDict1=json.loads(response1.text)
        listPara=copy.deepcopy(JiFenShangChengPara.ChouJiangJiLuLieBiao)
        JiFenShangChengIntf.getLotteryRecordList(para=listPara)
        checkPara=copy.deepcopy(JiFenShangChengPara.ChouJiangJiLuLieBiaoJianCha)
        checkPara['goodsName']=resDict1['response']['module']['prizeName']
        checkPara['goodsType']=resDict1['response']['module']['goodsType']
        goodsType=resDict1['response']['module']['goodsType']
        resDict2=XsInformationSquareIntf.getUserLogin(mobile=Global.XianSuoDftMobile,password=Global.XianSuoDftPassword)
        #如果中奖类型是积分，状态为已兑换
        if goodsType==GoodsType.POINT:
            checkPara['exchangeState']=ExchangeState.YIDUIHUAN
        else:
            checkPara['exchangeState']=ExchangeState.WEIDUIHUAN
        res=JiFenShangChengIntf.checkLotteryRecordList(listPara, checkPara)
        self.assertTrue(res, '兑换状态检查失败')
        #如果中奖类型为空，即八等奖，则不可以进行确认兑换操作,这里后台缺少判断
#         if goodsType==GoodsType.NONE:
#             res=JiFenShangChengIntf.confirmLottery(para={'ids[]':lotteryRecordId})
#             self.assertFalse(res.result, '确认兑换失败')
        #如果中奖类型为手机充值卡
        if goodsType==GoodsType.PHONECARD:
            #PC确认兑换
            res=JiFenShangChengIntf.confirmLottery(para={'ids[]':lotteryRecordId})
            self.assertTrue(res.result, '确认兑换失败')
            #检查PC端兑换状态
            checkPara['exchangeState']=ExchangeState.YIDUIHUAN
            res=JiFenShangChengIntf.checkLotteryRecordList(listPara, checkPara)
            self.assertTrue(res, '兑换状态检查失败')
            #手机端信息补充
            updPara=copy.deepcopy(XsJiFenShangChengPara.ZhongJiangXinXiBuChong)
            updPara['id']=lotteryRecordId
            #补充中奖信息
            XsJiFenShangChengIntf.updateLotteryRecordForMobile(updPara)
            #手机端进行验证
            mListPara=copy.deepcopy(XsJiFenShangChengPara.ZhongJiangJiLu)
            mListPara['userId']=resDict2['response']['module']['id']
            XsJiFenShangChengIntf.getLotteryRecordListForMobile(mListPara)
            mCheckPara=copy.deepcopy(XsJiFenShangChengPara.ZhongJiangJiLuJianCha)
            mCheckPara['prizeGrade']=resDict1['response']['module']['prizeGrade']
            mCheckPara['exchangeState']=ExchangeState.YIDUIHUAN
            mCheckPara['receiveState']=ReceiveState.YILINGQU
            mCheckPara['goodsType']=goodsType
            res=XsJiFenShangChengIntf.checkLotteryListForMobile(mListPara, mCheckPara)
            self.assertTrue(res,'手机端检查状态失败')
        if goodsType==GoodsType.PHYSICAL:
            #对实物进行取消兑换操作
            res=JiFenShangChengIntf.cancelLottery(para={'id':lotteryRecordId})
            self.assertTrue(res.result, '确认兑换失败')
            #检查兑换状态
            checkPara['exchangeState']=ExchangeState.QUXIAO
            res=JiFenShangChengIntf.checkLotteryRecordList(listPara, checkPara)
            self.assertTrue(res, '兑换状态检查失败')
            #手机端检查兑换状态
            mListPara=copy.deepcopy(XsJiFenShangChengPara.ZhongJiangJiLu)
            mListPara['userId']=resDict2['response']['module']['id']
#             XsJiFenShangChengIntf.getLotteryRecordListForMobile(mListPara)
            mCheckPara=copy.deepcopy(XsJiFenShangChengPara.ZhongJiangJiLuJianCha)
            mCheckPara['prizeGrade']=resDict1['response']['module']['prizeGrade']
            mCheckPara['exchangeState']=ExchangeState.QUXIAO
#             mCheckPara['receiveState']=ReceiveState.WEILINGQU
            mCheckPara['goodsType']=goodsType
            mCheckPara['shippingMethod']=resDict1['response']['module']['shippingMethod']
            res=XsJiFenShangChengIntf.checkLotteryListForMobile(mListPara, mCheckPara)
            self.assertTrue(res,'手机端检查状态失败')
        #备注功能
        updateRemarkPara={'ids':lotteryRecordId,
                           'remarks':'备注'+CommonUtil.createRandomString()}     
        JiFenShangChengIntf.updateLotteryRemark(updateRemarkPara)
        #检查列表备注显示是否正确
        checkRemarkPara={
                'id':updateRemarkPara['ids'],
                'remarks':updateRemarkPara['remarks']
                         }
        res=JiFenShangChengIntf.checkLotteryRecordList(listPara, checkRemarkPara)
        self.assertTrue(res, '备注内容检查失败')
        
    def tearDown(self):
        pass    

    
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(YwJiFenShangCheng("test_YwJiFenShangCheng_15"))
    results = unittest.TextTestRunner().run(suite)
    pass   