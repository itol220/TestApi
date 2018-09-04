# -*- coding:UTF-8 -*-
'''
Created on 2015-11-24

@author: N-133
'''
from __future__ import unicode_literals
from COMMON import Log, Time
from COMMON.CommonUtil import createRandomString
from CONFIG import InitDefaultPara, Global
from CONFIG.InitDefaultPara import clueOrgInit
from Interface.XianSuoApp.BaoLiao import XsBaoLiaoPara, XsBaoLiaoIntf
from Interface.XianSuoApp.BaoLiao.XsBaoLiaoIntf import deleteAllClues
from Interface.XianSuoApp.GongZuoTai.XsGongZuoTaiIntf import initUser
from Interface.XianSuoApp.JiFenShangCheng import XsJiFenShangChengPara, \
    XsJiFenShangChengIntf
from Interface.XianSuoApp.JiFenShangCheng.XsJiFenShangChengIntf import \
    setPointByMobile, deletePointRuleByDb, getMerchandiseListForMobile, \
    checkMerchandiseInListForMobile, getMerchandiseDetailForMobile, \
    exchangeMerchandise, deleteExchangeRecord, checkExchangeRecord, \
    createRandomNumber
from Interface.XianSuoApp.JiFenShangCheng.XsJiFenShangChengPara import \
    JiFenDuiHuan, DuiHuanJiLu
from Interface.XianSuoApp.PaiHangBang import XsPaiHangBangIntf
from Interface.XianSuoApp.PaiHangBang.XsPaiHangBangIntf import getPersonalPoints
from Interface.XianSuoApp.XinXiGuangChang import XsInformationSquareIntf, \
    XsInformationSquarePara
from Interface.YunWeiPingTai.JiFenShangCheng import JiFenShangChengPara, \
    JiFenShangChengIntf
from Interface.YunWeiPingTai.JiFenShangCheng.JiFenShangChengIntf import \
    delAllLotteryAllocation, deleteGoods, setPointRules, addMerchandise
from Interface.YunWeiPingTai.JiFenShangCheng.JiFenShangChengPara import \
    ShangPinXinZeng, JiFenGuiZe, GoodsType, Operators, ShippingMethod, PointType
import copy
import json
import time
import unittest



class XsPointMall(unittest.TestCase):

    def setUp(self):
        initUser()
#         SystemMgrIntf.initEnv()''
        deleteAllClues()
        if Global.simulationEnvironment is False:
            #积分清零
            setPointByMobile()
            #清空测试自动化区下的积分规则
            deletePointRuleByDb()
            #清空默认用户的兑换记录
            deleteExchangeRecord()
        #清空测试自动化区下的积分商品
        deleteGoods()
        #删除活动
        JiFenShangChengIntf.delAllActivity()
        #清空转盘抽奖配置
        delAllLotteryAllocation()
        #清空Banner图配置
        JiFenShangChengIntf.delAllBannerPic()
        pass
    
    def test_XsJiFenShangCheng_01(self):
        """积分商城-805-积分兑换"""
        #获取区域积分规则id
        pointRuleId=JiFenShangChengIntf.get_point_rule_id_by_depNo({'departmentNo':InitDefaultPara.clueOrgInit['DftQuOrgDepNo']})
        #设置区积分规则
        if pointRuleId ==-1:
            addPointRulePara=copy.deepcopy(JiFenGuiZe)
            result=setPointRules(para=addPointRulePara)
            self.assertTrue(result.result, '设置积分规则失败')
        #新增后台商品
        addMerchandisePara=copy.deepcopy(ShangPinXinZeng)
        addMerchandisePara['goodsConfiguration.goodsNum']=10
        addMerchandisePara['goodsConfiguration.exchangePoints']=3
        addMerchandisePara['goodsConfiguration.goodsNo']='S'+time.strftime("%Y%m%d%H%M%S")+createRandomNumber(length=3)
        addMerchandisePara['goodsConfiguration.quota']='100'
        addMerchandisePara['goodsConfiguration.shippingMethod']='0'
        #文件参数
        files = {
                 'iosImgValue':open('C:/autotest_file/Tulips.jpg', 'rb'),
                'androidImgValue':open('C:/autotest_file/Penguins.jpg','rb')
                }
#         files = [ ('iosImgValue',('Tulips.jpg',open('C:/autotest_file/Tulips.jpg', 'rb'),'image/jpeg')),
#                 ('androidImgValue',('Penguins.jpg',open('C:/autotest_file/Penguins.jpg','rb'),'image/jpeg'))
#                 ]
        result=addMerchandise(para=addMerchandisePara,files=files)
        #设置初始积分为10
        if Global.simulationEnvironment is False:
            setPointByMobile(point=10)
        #获取积分
        getPointPara={'tqmobile':'true','departmentNo':InitDefaultPara.clueOrgInit['DftQuOrgDepNo']}
        pointNum1=XsPaiHangBangIntf.getPersonalPointsToNum(getPointPara)
#         print pointNum1
        #如果积分少于10，则通过爆料方式新增积分
        while pointNum1<10:
            addBaoLiaoPara=copy.deepcopy(XsBaoLiaoPara.xinZeng2)    
            #调用新增爆料的方法
            XsBaoLiaoIntf.addXianSuo(XianSuoDict=addBaoLiaoPara)
            pointNum1=XsPaiHangBangIntf.getPersonalPointsToNum(getPointPara)
            print pointNum1
        #查看手机端商品列表
        listPara={
                'tqmobile':'true',
                'departmentNo':InitDefaultPara.clueOrgInit['DftQuOrgDepNo'],
                'mobileType':'ios',
                'page':'1',
                'rows':'100'
                  }
        res=getMerchandiseListForMobile(para=listPara)
        self.assertTrue(res.result, '获取手机商品列表出错')
        checkPara={
            'departmentNo':addMerchandisePara['goodsConfiguration.departmentNo'],
            'exchangePoints':addMerchandisePara['goodsConfiguration.exchangePoints'],#兑换需要积分
            'goodsDetails':addMerchandisePara['goodsConfiguration.goodsDetails'],
            'goodsName':addMerchandisePara['goodsConfiguration.goodsName'],
            'goodsNum':addMerchandisePara['goodsConfiguration.goodsNum'],
            'goodsProfile':addMerchandisePara['goodsConfiguration.goodsProfile'],
            'goodsType' :addMerchandisePara['goodsConfiguration.goodsType'],
            'orgName':addMerchandisePara['goodsConfiguration.orgName'],
            'state':0
                   }
        result=checkMerchandiseInListForMobile(listpara=listPara,checkpara=checkPara)
        self.assertTrue(result, '手机端查看商品列表失败')
        #查看商品详情
        viewPara={
                'tqmobile':'true',
                'mobileType':'ios',
                'id':XsJiFenShangChengIntf.get_goods_id_by_name(addMerchandisePara['goodsConfiguration.goodsName'])
                  }
        result2=getMerchandiseDetailForMobile(para=viewPara)
        self.assertTrue(result2.result,'获取详情失败')
        #验证详情是否正确
        resultDict2=json.loads(result2.text)
        checkPara2={
            'departmentNo':resultDict2['response']['module']['departmentNo'],
            'exchangePoints':resultDict2['response']['module']['exchangePoints'],#兑换需要积分
            'goodsDetails':resultDict2['response']['module']['goodsDetails'],
            'goodsName':resultDict2['response']['module']['goodsName'],
            'goodsNum':resultDict2['response']['module']['goodsNum'],
            'goodsProfile':resultDict2['response']['module']['goodsProfile'],
            'goodsType' :resultDict2['response']['module']['goodsType'],
            'orgName':resultDict2['response']['module']['orgName'],
            'state':0
                   }
        print resultDict2['response']['module']['goodsNum']
        result3=checkMerchandiseInListForMobile(listpara=listPara,checkpara=checkPara2)
        self.assertTrue(result3, '手机端获取商品详情失败')
        #积分不足的情况下兑换，只适用于非仿真环境
        resDict3=XsInformationSquareIntf.getUserLogin(mobile=Global.XianSuoDftMobile,password=Global.XianSuoDftPassword)
        exchangePara=copy.deepcopy(JiFenDuiHuan)
        exchangePara['userNickName']=resDict3['response']['module']['nickName']
        exchangePara['userId']=resDict3['response']['module']['id']
        exchangePara['userMobile']=resDict3['response']['module']['mobile']
        exchangePara['goodsName']=resultDict2['response']['module']['goodsName']
        exchangePara['goodsType']=resultDict2['response']['module']['goodsType']
        exchangePara['exchangeNum']=4#10-3*4,积分不足
        exchangePara['exchangePoints']=resultDict2['response']['module']['exchangePoints']*exchangePara['exchangeNum']#兑换所需总积分
        exchangePara['departmentNo']=resultDict2['response']['module']['departmentNo']
        exchangePara['orgName']=resultDict2['response']['module']['orgName']
        exchangePara['goodsConfigurationId']=resultDict2['response']['module']['id']
        exchangePara['exchangeOverDate']=2
        exchangePara['name']='张三'
        exchangePara['IdentityCard']='111111111111111'
        exchangePara['goodsNo']=addMerchandisePara['goodsConfiguration.goodsNo']
        if Global.simulationEnvironment is False:
            result4=exchangeMerchandise(para=exchangePara) 
            self.assertFalse(result4.result, '积分兑换')
        #正常兑换
        exchangePara['exchangeNum']=3
        exchangePara['exchangePoints']=resultDict2['response']['module']['exchangePoints']*exchangePara['exchangeNum']#兑换所需总积分
        print exchangePara['exchangePoints']
        result5=exchangeMerchandise(para=exchangePara)
        self.assertTrue(result5.result, '积分兑换')
        resultDict5=json.loads(result5.text)
        #验证兑换记录是否正确
        viewExchangeRecordPara=copy.deepcopy(DuiHuanJiLu)
        viewExchangeRecordPara['userId']=exchangePara['userId']
        checkExchangeRecordPara={
            'departmentNo':resultDict5['response']['module']['departmentNo'],
            'exchangeCode':resultDict5['response']['module']['exchangeCode'],
            'exchangeNum':exchangePara['exchangeNum'],                
            'exchangePoints':exchangePara['exchangePoints'],
            'goodsConfigurationId':exchangePara['goodsConfigurationId'],
            'goodsName':exchangePara['goodsName'],
            'goodsType':exchangePara['goodsType'],
            'id':resultDict5['response']['module']['id'],
            'orgName':exchangePara['orgName'],
            'userMobile':exchangePara['userMobile'],
            'userNickName':exchangePara['userNickName'],
                                 }
        result6=checkExchangeRecord(listpara=viewExchangeRecordPara,checkpara=checkExchangeRecordPara)
        self.assertTrue(result6, '查看兑换记录列表验证失败')
        #验证兑换后商品库存与用户剩余积分数是否正确
        result7=getMerchandiseDetailForMobile(para=viewPara)
        self.assertTrue(result7.result,'获取详情失败')
        #验证详情是否正确
        resultDict7=json.loads(result7.text)
        #商品库存7
        self.assertEqual(resultDict7['response']['module']['goodsNum'], addMerchandisePara['goodsConfiguration.goodsNum']-exchangePara['exchangeNum'], '库存验证失败')
        #商品已经兑换数量
        self.assertEqual(resultDict7['response']['module']['hasExchangeNum'], exchangePara['exchangeNum'], '商品已经兑换数量验证失败')
        #用户剩余积分数
        #获取个人积分
        pointNum2=XsPaiHangBangIntf.getPersonalPointsToNum(getPointPara)
        print pointNum2
        self.assertEqual(pointNum1-pointNum2,exchangePara['exchangeNum']*3 , '积分扣除验证失败')
        Log.LogOutput( message='积分扣除正确')
        pass    
 
    def test_XsJiFenShangCheng_02(self):
        '''积分商城-后台配置对手机端的影响-879、796、854(Banner图跳，转类型为“大转盘”)'''
        #配置大转盘
        addPara=copy.deepcopy(JiFenShangChengPara.ZhuanPanChouJiangXinZeng2)
        DaZhuanPanFile={
                        'iosImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/dazhuanpan.png', 'rb'),
                        'androidImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/dazhuanpan.png', 'rb')    
                }
        response1=JiFenShangChengIntf.addLotteryAllocation(para=addPara,files=DaZhuanPanFile)
        self.assertTrue(response1.result, '新增大转盘配置出错')
#         print type(json.loads(response1.text))
        lotteryAllocationId=json.loads(response1.text)['id']
        #配置奖项
        listPara=copy.deepcopy(JiFenShangChengPara.JiangPingPeiZhiLieBiao)
        listPara['prizeSetting.lotteryAllocationId']=lotteryAllocationId
        #设置一号奖品参数
        prizePara1=copy.deepcopy(JiFenShangChengPara.JiangPingPeiZhi)
        prizePara1['prizeSetting.id']=JiFenShangChengIntf.getIdByGrade(listPara, prizeGrade=1)
        prizePara1['prizeSetting.goodsType']=1
        prizePara1['prizeSetting.prizeName']='Iphone7'
        prizePara1['prizeSetting.prizeNumber']='100'
        prizePara1['prizeSetting.shippingMethod']='1'
        prizePara1['prizeSetting.intervalStart']='1'
        prizePara1['prizeSetting.intervalEnd']='10'
        files1={
        'iosImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/ip7.png', 'rb'),
        'androidImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/ip7.png', 'rb')    
                }
        JiFenShangChengIntf.setPrize(para=prizePara1, files=files1)
        #设置二号奖品参数
        prizePara2=copy.deepcopy(JiFenShangChengPara.JiangPingPeiZhi)
        prizePara2['prizeSetting.id']=JiFenShangChengIntf.getIdByGrade(listPara, prizeGrade=2)
        prizePara2['prizeSetting.goodsType']=1
        prizePara2['prizeSetting.prizeName']='iwatch'
        prizePara2['prizeSetting.prizeNumber']='100'
        prizePara2['prizeSetting.shippingMethod']='0'
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
        prizePara3['prizeSetting.goodsType']=0
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
        prizePara4['prizeSetting.goodsType']=0
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
        prizePara5['prizeSetting.goodsType']=0
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
        prizePara6['prizeSetting.goodsType']=0
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
        prizePara7['prizeSetting.goodsType']=2
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
        prizePara8['prizeSetting.goodsType']=3
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
        #开始测试手机接口
        getBannerPicInfoPara=copy.deepcopy(XsJiFenShangChengPara.BannerPicInfo)
        #检查Banner图相关信息参数是否正确
        checkPara=copy.deepcopy(XsJiFenShangChengPara.BannerPicInfoCheck)
        checkPara['contentText']=addBannerPara['storeImageConfiguration.contentText']
        checkPara['title']=addBannerPara['storeImageConfiguration.title']
        checkPara['lotteryAllocationId']=lotteryAllocationId
        checkPara['jumpType']=addBannerPara['storeImageConfiguration.jumpType']
        response3=XsJiFenShangChengIntf.checkBannerInfo(para=getBannerPicInfoPara,checkpara=checkPara)
        self.assertTrue(response3, 'Banner图配置验证出现错误')
        #后台关闭Banner图，验证手机端是否能够接收banner图信息
        JiFenShangChengIntf.closeBannerPic(para={'ids[]':json.loads(response2.text)['id']})
        response3=XsJiFenShangChengIntf.checkBannerInfo(para=getBannerPicInfoPara,checkpara=checkPara)
        self.assertFalse(response3, 'Banner图配置关闭功能验证出现错误')
        Log.LogOutput( message='Banner图打开功能正常')
        #再次打开Banner图，并验证打开功能是否正确
        JiFenShangChengIntf.openBannerPic(para={'ids[]':json.loads(response2.text)['id']})
        response3=XsJiFenShangChengIntf.checkBannerInfo(para=getBannerPicInfoPara,checkpara=checkPara)
        self.assertTrue(response3, 'Banner图配置关闭功能验证出现错误')
        Log.LogOutput( message='Banner图关闭功能正常')
        #验证手机端获取的大转盘信息是否正确
        personalDict=XsInformationSquareIntf.getUserLogin(mobile=Global.XianSuoDftMobile,password=Global.XianSuoDftPassword)
        #获取大转盘信息参数
        para=copy.deepcopy(XsJiFenShangChengPara.DaZhuanPanPeiZhi)
        para['userId']=personalDict['response']['module']['id']
        para['lotteryAllocationId']=lotteryAllocationId
        #检查大转盘信息参数
        lotteryAllocationCheckPara=copy.deepcopy(XsJiFenShangChengPara.DaZhuanPanPeiZhiCheck)
        lotteryAllocationCheckPara['lotteryActivityNo']=addPara['lotteryAllocation.lotteryActivityNo']
        lotteryAllocationCheckPara['activityDetails']=addPara['lotteryAllocation.activityDetails']
        lotteryAllocationCheckPara['lotteryPoints']=addPara['lotteryAllocation.lotteryPoints']
        lotteryAllocationCheckPara['userLotteryDayNumber']=addPara['lotteryAllocation.lotteryDayNumber']
        response4=XsJiFenShangChengIntf.checklotteryAllocationInfo(para, lotteryAllocationCheckPara)
        self.assertTrue(response4, '手机端获取大转盘信息验证错误')
        Log.LogOutput(message='手机端获取大转盘信息验证通过')
        #关闭大转盘，验证获取信息是否成功，依然成功
        JiFenShangChengIntf.closeLotteryAllocation({'ids[]':lotteryAllocationId})
        response4=XsJiFenShangChengIntf.checklotteryAllocationInfo(para, lotteryAllocationCheckPara)
        self.assertTrue(response4, '关闭大转盘手机端验证失败')
        Log.LogOutput(message='手机端获取大转盘信息验证通过')
        #关闭大转盘，验证抽奖功能是否失败
        #设置积分
        if Global.simulationEnvironment is False:
            setPointByMobile(point=100)
        getPointPara={'tqmobile':'true','departmentNo':InitDefaultPara.clueOrgInit['DftQuOrgDepNo']}
        pointNum1=XsPaiHangBangIntf.getPersonalPointsToNum(getPointPara)
        while pointNum1<20:
            addBaoLiaoPara=copy.deepcopy(XsBaoLiaoPara.xinZeng2)    
            #调用新增爆料的方法
            XsBaoLiaoIntf.addXianSuo(XianSuoDict=addBaoLiaoPara)
            pointNum1=XsPaiHangBangIntf.getPersonalPointsToNum(getPointPara)

        addLotteryPara=copy.deepcopy(XsJiFenShangChengPara.ChouJiang)
        addLotteryPara['lotteryActivityNo']=addPara['lotteryAllocation.lotteryActivityNo']
        response5=XsJiFenShangChengIntf.addLotteryRecord(para=addLotteryPara)
        self.assertFalse(response5.result, '关闭大转盘的情况下抽奖验证失败')
        #开启大转盘，再次验证
        JiFenShangChengIntf.openLotteryAllocation({'ids[]':lotteryAllocationId})
        response5=XsJiFenShangChengIntf.addLotteryRecord(para=addLotteryPara)
        self.assertTrue(response5.result, '开启大转盘的情况下抽奖验证失败')
        #验证抽奖后积分是否减少所设置数目
        pointNum2=XsPaiHangBangIntf.getPersonalPointsToNum(getPointPara)
        #如果获得的奖项不是七等奖,那么积分减1,如果是七等奖，则加9
        if json.loads(response5.text)['response']['module']['prizeGrade']==7:
            self.assertEqual(pointNum2-pointNum1, 9, '积分奖励验证失败')
        else:
            self.assertEqual(pointNum1-pointNum2, 1, '积分扣除验证失败')
        Log.LogOutput( message='积分扣除正确')
        self.assertEqual(json.loads(response5.text)['response']['module']['userLotteryDayNumber'], 998, '积分扣除验证失败')
        Log.LogOutput( message='每日剩余可抽奖次数正确')
        #将每日可抽奖次数设置为1，验证是否可以抽奖
        addPara['lotteryAllocation.id']=lotteryAllocationId
        addPara['lotteryAllocation.lotteryDayNumber']=1
        result2=JiFenShangChengIntf.updLotteryAllocation(para=addPara,files=DaZhuanPanFile)
        self.assertTrue(result2.result, '修改大转盘失败')
        #再次抽奖,由于之前已经抽过，预期为失败
        response6=XsJiFenShangChengIntf.addLotteryRecord(para=addLotteryPara)
        self.assertFalse(response6.result, '每日可抽奖次数达到上限后抽奖验证失败')
        Log.LogOutput(message='每日可抽奖次数达到上限后抽奖验证成功')
        #恢复每天抽奖上限为999
        addPara['lotteryAllocation.lotteryDayNumber']=999
        JiFenShangChengIntf.updLotteryAllocation(para=addPara,files=DaZhuanPanFile)
        Log.LogOutput(message='恢复每天抽奖上限次数成功')
        #将每个奖品设置为0，然后抽奖，验证抽奖结果是否都转为8等奖
        #设置一号奖品参数
        prizePara1['prizeSetting.prizeNumber']='0'
        files1={
        'iosImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/ip7.png', 'rb'),
        'androidImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/ip7.png', 'rb')    
                }
        JiFenShangChengIntf.setPrize(para=prizePara1, files=files1)
        #设置二号奖品参数
        prizePara2['prizeSetting.prizeNumber']='0'
        files2={
        'iosImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/iWatch.png', 'rb'),
        'androidImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/iWatch.png', 'rb')      
                }
        JiFenShangChengIntf.setPrize(para=prizePara2, files=files2)
        #设置三号奖品参数
        prizePara3['prizeSetting.prizeNumber']='0'
        files3={
        'iosImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/500.png', 'rb'),
        'androidImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/500.png', 'rb')      
                }
        JiFenShangChengIntf.setPrize(para=prizePara3, files=files3)        
        #设置四号奖品参数 
        prizePara4['prizeSetting.prizeNumber']='0'
        files4={
        'iosImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/100.png', 'rb'),
        'androidImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/100.png', 'rb')      
                }
        JiFenShangChengIntf.setPrize(para=prizePara4, files=files4)          
        #设置五号奖品参数 
        prizePara5['prizeSetting.prizeNumber']='0'
        files5={
        'iosImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/50.png', 'rb'),
        'androidImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/50.png', 'rb')      
                }
        JiFenShangChengIntf.setPrize(para=prizePara5, files=files5)  
        #设置六号奖品参数
        prizePara6['prizeSetting.prizeNumber']='0'
        files6={
        'iosImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/10.png', 'rb'),
        'androidImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/10.png', 'rb')      
                }
        JiFenShangChengIntf.setPrize(para=prizePara6, files=files6)           
        #设置七号奖品参数
        prizePara7['prizeSetting.prizeNumber']='0'
        files7={
        'iosImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/10points.png', 'rb'),
        'androidImgValue':open('C:/autotest_file/XianSuoChouJiangPeiTu/10points.png', 'rb')      
                }
        JiFenShangChengIntf.setPrize(para=prizePara7, files=files7)          
        #再抽10次奖，结果都是八等奖
        for i in range(10):
            Log.LogOutput(message="第"+str(i)+"次抽奖")
            res=XsJiFenShangChengIntf.addLotteryRecord(para=addLotteryPara)
            self.assertEquals(json.loads(res.text)['response']['module']['prizeGrade'],8, "抽奖结果不正确")
        Log.LogOutput(message='奖品数量为0后抽奖验证成功')        
        pass    
    
    def test_XsJiFenShangCheng_03(self):
        """积分商城-验证删除爆料、取消关注、删除评论是否会减少积分803"""
        #初始化积分配置
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
        myPoints0=XsPaiHangBangIntf.getPersonalPointsToNum(para1)
        print myPoints0
        #新增一条线索，查看积分是否+1
        addPara=copy.deepcopy(XsBaoLiaoPara.xinZeng2)
        res1=XsBaoLiaoIntf.addXianSuo(addPara)
        self.assertTrue(res1.result, '新增线索失败')
        myPoints1=XsPaiHangBangIntf.getPersonalPointsToNum(para1)
        print myPoints1
        #获取新增爆料可加积分数
        pointnum=JiFenShangChengIntf.get_add_point_by_id(PointType.BAOLIAO)
        print pointnum
        self.assertEquals(myPoints1, myPoints0+pointnum, '新增爆料后积分累计不正确')
        Log.LogOutput( message='新增爆料后积分累计正确')
        
        listPara={
                'tqmobile':'true',
                'page':'1',
                'rows':'100'
                  }
        lsr=XsBaoLiaoIntf.viewSchedule(para=listPara)
        #查看进度列表结果字典项
        lsrDict=json.loads(lsr.text)
        #新增评论+4
        addcompara=copy.deepcopy(XsInformationSquarePara.addCommentPara)
        addcompara['informationId']=lsrDict['response']['module']['rows'][0]['information']['id']
        addcompara['commentUserId']=lsrDict['response']['module']['rows'][0]['information']['publishUserId']
        addcompara['commentType']=0
        result1=XsInformationSquareIntf.addComment(para=addcompara)
        self.assertTrue(result1.text, '新增评论失败')
        myPoints2=XsPaiHangBangIntf.getPersonalPointsToNum(para1)
        pointnum2=JiFenShangChengIntf.get_add_point_by_id(PointType.PINGLUN)
        self.assertEquals(myPoints2, myPoints1+pointnum2, '新增评论后积分累计不正确')
        Log.LogOutput( message='新增评论后积分累计正确')
        #删除评论，积分不减少
        delCommentForCluePara=copy.deepcopy(XsBaoLiaoPara.delCommentCluePara)
        delCommentForCluePara['id']=json.loads(result1.text)['response']['module']['id']
        XsBaoLiaoIntf.delete_comment_for_clue(delCommentForCluePara)
        myPoints3=XsPaiHangBangIntf.getPersonalPointsToNum(para1)
        self.assertEquals(myPoints3, myPoints2, '删除评论后积分累计不正确')
        Log.LogOutput( message='删除评论后积分累计正确')
        
        #新增关注，+2
        addConPara=copy.deepcopy(XsInformationSquarePara.addConPara)
        addConPara['tqmobile']='true'
        addConPara['informationId']=lsrDict['response']['module']['rows'][0]['information']['id']
        addConPara['concernUserId']=lsrDict['response']['module']['rows'][0]['information']['publishUserId']
        result2=XsInformationSquareIntf.addConcern(para=addConPara)
        self.assertTrue(result2.result, '新增关注失败')
        myPoints4=XsPaiHangBangIntf.getPersonalPointsToNum(para1)
        pointnum4=JiFenShangChengIntf.get_add_point_by_id(PointType.GUANZHU)
        self.assertEquals(myPoints4, myPoints3+pointnum4, '新增关注后积分累计不正确')
        Log.LogOutput( message='新增关注后积分累计正确')
        #取消关注，不减积分
        CancelConcernPara=copy.deepcopy(XsBaoLiaoPara.CancelConcernPara)
        CancelConcernPara['informationId']=addConPara['informationId']
        CancelConcernPara['concernUserId']=addConPara['concernUserId']
        XsBaoLiaoIntf.cancel_Concern_for_clue(CancelConcernPara)
        myPoints5=XsPaiHangBangIntf.getPersonalPointsToNum(para1)
        self.assertEquals(myPoints5, myPoints4, '取消关注后积分累计不正确')
        Log.LogOutput( message='取消关注后积分累计正确')   
        print myPoints5
        #再次新增两条爆料，达到上限，只加6
        addPara2=copy.deepcopy(XsBaoLiaoPara.xinZeng2)
        addPara2['information']['contentText']='第二条爆料'+createRandomString()
        XsBaoLiaoIntf.addXianSuo(addPara)
        addPara3=copy.deepcopy(XsBaoLiaoPara.xinZeng2)
        addPara3['information']['contentText']='第三条爆料'+createRandomString()
        XsBaoLiaoIntf.addXianSuo(addPara)
        
        myPoints6=XsPaiHangBangIntf.getPersonalPointsToNum(para1)
        print myPoints6
        self.assertEquals(myPoints6, myPoints5+2, '新增爆料后积分累计不正确')
        Log.LogOutput( message='新增爆料后积分累计正确')
        #删除三条爆料
        deleteAllClues()
        myPoints7=XsPaiHangBangIntf.getPersonalPointsToNum(para1)
        print myPoints7
        self.assertEquals(myPoints7, myPoints6-3, '删除爆料后积分累计不正确')
        Log.LogOutput( message='删除爆料后积分累计正确')        
        pass
    
    def test_XsJiFenShangCheng_04(self):
        """积分商城-806-积分兑换话费功能"""
        #新增后台商品
        addMerchandisePara=copy.deepcopy(ShangPinXinZeng)
        addMerchandisePara['goodsConfiguration.goodsType']=GoodsType.PHONECARD
        addMerchandisePara['goodsConfiguration.goodsNum']=10
        addMerchandisePara['goodsConfiguration.exchangePoints']=3
        addMerchandisePara['goodsConfiguration.goodsNo']='S'+time.strftime("%Y%m%d%H%M%S")+createRandomNumber(length=3)
        addMerchandisePara['goodsConfiguration.quota']='10'
        addMerchandisePara['goodsConfiguration.operators']=Operators.ALL
        addMerchandisePara['goodsConfiguration.shippingMethod']=ShippingMethod.JISONG
        #文件参数
        files = {
                 'iosImgValue':open('C:/autotest_file/Tulips.jpg', 'rb'),
                'androidImgValue':open('C:/autotest_file/Penguins.jpg','rb')
                }
#         files = [ ('iosImgValue',('Tulips.jpg',open('C:/autotest_file/Tulips.jpg', 'rb'),'image/jpeg')),
#                 ('androidImgValue',('Penguins.jpg',open('C:/autotest_file/Penguins.jpg','rb'),'image/jpeg'))
#                 ]
        addMerchandise(para=addMerchandisePara,files=files)
        
        #配置活动
        addActivityPara={
                'startDate':Time.getCurrentDate(),
                'endDate':Time.getCurrentDate(),
                'activeTimeConfiguration.goodsType':'0',
                'activeTimeConfiguration.exchangeCeiling':'10',
                'activeTimeConfiguration.goodsTotal':'60',
                'activeTimeConfiguration.departmentNo':InitDefaultPara.clueOrgInit['DftQuOrgDepNo'],
                'activeTimeConfiguration.orgName':InitDefaultPara.clueOrgInit['DftQuOrg'],
                         }
        addActivityPara['activeTimeConfiguration.activityNo']='HD'+time.strftime("%Y%m")+addActivityPara['activeTimeConfiguration.departmentNo']+createRandomNumber(length=4)
        JiFenShangChengIntf.addActivity(addActivityPara)        
        #设置初始积分为10
        if Global.simulationEnvironment is False:
            setPointByMobile(point=10)
        getPointPara={'tqmobile':'true','departmentNo':InitDefaultPara.clueOrgInit['DftQuOrgDepNo']}
        pointNum1=XsPaiHangBangIntf.getPersonalPointsToNum(getPointPara)
        while pointNum1<10:
            addBaoLiaoPara=copy.deepcopy(XsBaoLiaoPara.xinZeng2)    
            #调用新增爆料的方法
            XsBaoLiaoIntf.addXianSuo(XianSuoDict=addBaoLiaoPara)
            pointNum1=XsPaiHangBangIntf.getPersonalPointsToNum(getPointPara)
        #查看手机端商品列表
        listPara={
                'tqmobile':'true',
                'departmentNo':InitDefaultPara.clueOrgInit['DftQuOrgDepNo'],
                'mobileType':'ios',
                'page':'1',
                'rows':'100'
                  }
        res=getMerchandiseListForMobile(para=listPara)
        self.assertTrue(res.result, '获取手机商品列表出错')
        checkPara={
            'departmentNo':addMerchandisePara['goodsConfiguration.departmentNo'],
            'exchangePoints':addMerchandisePara['goodsConfiguration.exchangePoints'],#兑换需要积分
            'goodsDetails':addMerchandisePara['goodsConfiguration.goodsDetails'],
            'goodsName':addMerchandisePara['goodsConfiguration.goodsName'],
            'goodsNum':addMerchandisePara['goodsConfiguration.goodsNum'],
            'goodsProfile':addMerchandisePara['goodsConfiguration.goodsProfile'],
            'goodsType' :addMerchandisePara['goodsConfiguration.goodsType'],
            'orgName':addMerchandisePara['goodsConfiguration.orgName'],
            'state':0
                   }
        result=checkMerchandiseInListForMobile(listpara=listPara,checkpara=checkPara)
        self.assertTrue(result, '手机端查看商品列表失败')
        #查看商品详情
        viewPara={
                'tqmobile':'true',
                'mobileType':'ios',
                'id':XsJiFenShangChengIntf.get_goods_id_by_name(addMerchandisePara['goodsConfiguration.goodsName'])
                  }
        result2=getMerchandiseDetailForMobile(para=viewPara)
        self.assertTrue(result2.result,'获取详情失败')
        #验证详情是否正确
        resultDict2=json.loads(result2.text)
        checkPara2={
            'departmentNo':resultDict2['response']['module']['departmentNo'],
            'exchangePoints':resultDict2['response']['module']['exchangePoints'],#兑换需要积分
            'goodsDetails':resultDict2['response']['module']['goodsDetails'],
            'goodsName':resultDict2['response']['module']['goodsName'],
            'goodsNum':resultDict2['response']['module']['goodsNum'],
            'goodsProfile':resultDict2['response']['module']['goodsProfile'],
            'goodsType' :resultDict2['response']['module']['goodsType'],
            'orgName':resultDict2['response']['module']['orgName'],
            'state':0
                   }
        result3=checkMerchandiseInListForMobile(listpara=listPara,checkpara=checkPara2)
        self.assertTrue(result3, '手机端获取商品详情失败')
        #积分兑换
        resDict3=XsInformationSquareIntf.getUserLogin(mobile=Global.XianSuoDftMobile,password=Global.XianSuoDftPassword)
        exchangePara=copy.deepcopy(JiFenDuiHuan)
        exchangePara['userNickName']=resDict3['response']['module']['nickName']
        exchangePara['userId']=resDict3['response']['module']['id']
        exchangePara['userMobile']=resDict3['response']['module']['mobile']
        exchangePara['goodsName']=resultDict2['response']['module']['goodsName']
        exchangePara['goodsType']=addMerchandisePara['goodsConfiguration.goodsType']#resultDict2['response']['module']['goodsType']
        exchangePara['exchangeNum']=1
        exchangePara['exchangePoints']=resultDict2['response']['module']['exchangePoints']*exchangePara['exchangeNum']#兑换所需总积分
        exchangePara['departmentNo']=resultDict2['response']['module']['departmentNo']
        exchangePara['orgName']=resultDict2['response']['module']['orgName']
        exchangePara['goodsConfigurationId']=resultDict2['response']['module']['id']
        exchangePara['exchangeOverDate']=2
        exchangePara['name']='张三'
        exchangePara['IdentityCard']='111111111111111'
        exchangePara['quota']=addMerchandisePara['goodsConfiguration.quota']
        exchangePara['operators']=addMerchandisePara['goodsConfiguration.operators']
        exchangePara['goodsNo']=addMerchandisePara['goodsConfiguration.goodsNo']
        exchangePara['shippingMethod']=addMerchandisePara['goodsConfiguration.shippingMethod']
#         exchangePara['apiVersion']='3'
        exchangePara['activityNo']=addActivityPara['activeTimeConfiguration.activityNo']
        #正常兑换
        exchangePara['exchangeNum']=1
        exchangePara['exchangePoints']=resultDict2['response']['module']['exchangePoints']*exchangePara['exchangeNum']#兑换所需总积分
        result5=exchangeMerchandise(para=exchangePara)
        self.assertTrue(result5.result, '积分兑换')
        resultDict5=json.loads(result5.text)
        #验证兑换记录是否正确
        viewExchangeRecordPara=copy.deepcopy(DuiHuanJiLu)
        viewExchangeRecordPara['userId']=exchangePara['userId']
        checkExchangeRecordPara={
            'departmentNo':resultDict5['response']['module']['departmentNo'],
            'exchangeNum':exchangePara['exchangeNum'],                
            'exchangePoints':exchangePara['exchangePoints'],
            'goodsConfigurationId':exchangePara['goodsConfigurationId'],
            'goodsName':exchangePara['goodsName'],
            'goodsType':exchangePara['goodsType'],
            'id':resultDict5['response']['module']['id'],
            'orgName':exchangePara['orgName'],
            'userMobile':exchangePara['userMobile'],
            'userNickName':exchangePara['userNickName'],
                                 }
        result6=checkExchangeRecord(listpara=viewExchangeRecordPara,checkpara=checkExchangeRecordPara)
        self.assertTrue(result6, '查看兑换记录列表验证失败')
        #验证兑换后商品库存与用户剩余积分数是否正确
        result7=getMerchandiseDetailForMobile(para=viewPara)
        self.assertTrue(result7.result,'获取详情失败')
        #验证详情是否正确
        resultDict7=json.loads(result7.text)
        #商品已经兑换数量
        self.assertEqual(resultDict7['response']['module']['hasExchangeNum'], exchangePara['exchangeNum'], '商品已经兑换数量验证失败')
        #用户剩余积分数
        #获取个人积分
        para8={
               'tqmobile':'true',
               'departmentNo':InitDefaultPara.clueOrgInit['DftQuOrgDepNo']
               }
        result8=getPersonalPoints(para=para8)
        self.assertTrue(result8.result, '获取个人积分信息失败')
        resultDict8=json.loads(result8.text)
        pointNum2=XsPaiHangBangIntf.getPersonalPointsToNum(getPointPara)
        print pointNum2
        self.assertEqual(pointNum1-pointNum2, 3, '积分扣除验证失败')
        Log.LogOutput( message='积分扣除正确')
        #验证超过个人兑换上限是否报错
        result9=exchangeMerchandise(para=exchangePara)
        self.assertFalse(result9.result, '积分兑换')
        
        pass    
        
    def tearDown(self):
        pass    
    
    
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(XsPointMall("test_XsJiFenShangCheng_02"))
    results = unittest.TextTestRunner().run(suite)
    pass    