# -*- coding:UTF-8 -*-
#JiFenShangChengIntf
'''
Created on 2016-11-23

@author: N-286
'''
from __future__ import unicode_literals
from COMMON import Log, Time
from COMMON.CommonUtil import findDictInDictlist
from CONFIG import Global
from CONFIG.Define import LogLevel
from CONFIG.InitDefaultPara import clueOrgInit
from Interface.PingAnJianShe.Common.CommonIntf import getDbQueryResult
from Interface.PingAnJianShe.ShiJianChuLi.ShiJianChuLiIntf import exeDbQuery
from Interface.XianSuoApp.JiFenShangCheng.XsJiFenShangChengIntf import \
    createRandomNumber
from Interface.YunWeiPingTai.JiFenShangCheng import JiFenShangChengPara
from Interface.YunWeiPingTai.XiTongPeiZhi import XiTongPeiZhiPara, \
    XiTongPeiZhiIntf
from Interface.YunWeiPingTai.yunWeiPingTaiHttpCommon import xiansuoyunwei_post
import copy
import json
import time

'''
    @功能：初始化积分配置，每日积分上限为0
    @return:    true/false
    @author:  chenhui 2016-11-30
'''  
def initPointSetting():
        #初始化积分配置
        param = copy.deepcopy(XiTongPeiZhiPara.updateJiFenPeiZhi)
        param['pointsSetting.id'] =1
        param['pointsSetting.points'] = 1
        param['pointsSetting.todayMaxPoints']=0
        if XiTongPeiZhiIntf.updateJiFenPeiZhi(param).result is False:
            Log.LogOutput(LogLevel.ERROR, '积分爆料初始化配置出错')
            return False
        param['pointsSetting.id'] =2
        param['pointsSetting.points'] = 2
        param['pointsSetting.todayMaxPoints']=0
        if XiTongPeiZhiIntf.updateJiFenPeiZhi(param).result is False:
            Log.LogOutput(LogLevel.ERROR, '积分关注初始化配置出错')
            return False
        param['pointsSetting.id'] =3
        param['pointsSetting.points'] = 3
        param['pointsSetting.todayMaxPoints']=0
        if XiTongPeiZhiIntf.updateJiFenPeiZhi(param).result is False:
            Log.LogOutput(LogLevel.ERROR, '积分点赞初始化配置出错')
            return False
        param['pointsSetting.id'] =4
        param['pointsSetting.points'] = 4
        param['pointsSetting.todayMaxPoints']=0
        if XiTongPeiZhiIntf.updateJiFenPeiZhi(param).result is False:
            Log.LogOutput(LogLevel.ERROR, '积分评论初始化配置出错')
            return False
        param['pointsSetting.id'] =5
        param['pointsSetting.points'] = 5
        param['pointsSetting.todayMaxPoints']=0
        if XiTongPeiZhiIntf.updateJiFenPeiZhi(param).result is False:
            Log.LogOutput(LogLevel.ERROR, '积分受理初始化配置出错')
            return False
        param['pointsSetting.id'] =6
        param['pointsSetting.points'] = 6
        param['pointsSetting.todayMaxPoints']=0
        if XiTongPeiZhiIntf.updateJiFenPeiZhi(param).result is False:
            Log.LogOutput(LogLevel.ERROR, '积分用户邀请初始化配置出错')
            return False
        param['pointsSetting.id'] =7
        param['pointsSetting.points'] = 7
        param['pointsSetting.todayMaxPoints']=0
        if XiTongPeiZhiIntf.updateJiFenPeiZhi(param).result is False:
            Log.LogOutput(LogLevel.ERROR, '积分用户评分初始化配置出错')
            return False
        param['pointsSetting.id'] =8
        param['pointsSetting.points'] = 8
        param['pointsSetting.todayMaxPoints']=0
        if XiTongPeiZhiIntf.updateJiFenPeiZhi(param).result is False:
            Log.LogOutput(LogLevel.ERROR, '积分每日签到初始化配置出错')
            return False
        param['pointsSetting.id'] =9
        param['pointsSetting.points'] = 9
        param['pointsSetting.todayMaxPoints']=0
        if XiTongPeiZhiIntf.updateJiFenPeiZhi(param).result is False:
            Log.LogOutput(LogLevel.ERROR, '积分连续签到初始化配置出错')
            return False
        param['pointsSetting.id'] =10
        param['pointsSetting.points'] = 10
        param['pointsSetting.todayMaxPoints']=0
        if XiTongPeiZhiIntf.updateJiFenPeiZhi(param).result is False:
            Log.LogOutput(LogLevel.ERROR, '积分注册初始化配置出错')

'''
    @功能：通过积分配置获取各项条件符合后能够加的积分数
    @param para: JiFenShangChengPara.PointType
    @return:    response
    @author:  chenhui 2017-5-17
'''  
def get_add_point_by_id(PointType):
    info='获取所需积分数'
    Log.LogOutput(LogLevel.INFO, info)
    para=JiFenShangChengPara.getPointConfigPara
    response = xiansuoyunwei_post(url='/pointsSettingManage/findPointsSettingList', postdata=para)
    resDict=json.loads(response.text)
    for item in resDict['rows']:
        if item['pointsType']==PointType:
            Log.LogOutput(message=info+'成功')
            return item['points']
    Log.LogOutput(message=info+'失败')
   
'''
    @功能：通过积分配置获取各项条件符合后每天能够加的积分上限
    @param para: JiFenShangChengPara.PointType
    @return:    response
    @author:  chenhui 2017-5-17
'''  
def get_point_limit_by_id(PointType):
    info='获取每日积分上限'
    Log.LogOutput(LogLevel.INFO, info)
    para=JiFenShangChengPara.getPointConfigPara
    response = xiansuoyunwei_post(url='/pointsSettingManage/findPointsSettingList', postdata=para)
    resDict=json.loads(response.text)
    for item in resDict['rows']:
        if item['pointsType']==PointType:
            Log.LogOutput(message=info+'成功')
            return item['todayMaxPoints']
    Log.LogOutput(message=info+'失败')
        
'''
    @功能：新增转盘抽奖
    @param para: JiFenShangChengPara.ZhuanPanChouJiangXinZeng
                    files:
    @return:    response
    @author:  chenhui 2016-11-23
'''  
def addLotteryAllocation(para,files):
    info='新增转盘抽奖'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/lotteryAllocationManage/addLotteryAllocation', postdata=para,files=files)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功")
    else:
        Log.LogOutput(LogLevel.ERROR, info+"失败")
    return response

'''
    @功能：修改转盘抽奖配置
    @param :JiFenShangChengPara.ZhuanPanChouJiangXiuGai
            files:JiFenShangChengPara.DaZhuanPanFile
    @return:    response
    @author:  chenhui 2016-11-23
'''  
def updLotteryAllocation(para,files=None):
    info='修改转盘抽奖配置'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/lotteryAllocationManage/updateLotteryAllocation', postdata=para,files=files)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功")
    else:
        Log.LogOutput(LogLevel.ERROR, info+"失败")
    return response

'''
    @功能：删除转盘抽奖配置
    @param :{ids[]:''}
    @return:    response
    @author:  chenhui 2016-11-23
'''  
def delLotteryAllocation(para):
    info='删除转盘抽奖配置'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/lotteryAllocationManage/deleteLotteryAllocations', postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功")
    else:
        Log.LogOutput(LogLevel.ERROR, info+"失败")
    return response

'''
    @功能：获取转盘抽奖配置列表
    @param :JiFenShangChengPara.ZhuanPanChouJiangLieBiao
    @return:    response
    @author:  chenhui 2016-11-23
'''  
def getLotteryAllocationList(para):
    info='获取转盘抽奖配置列表'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/lotteryAllocationManage/findLotteryAllocationList', postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功")
    else:
        Log.LogOutput(LogLevel.ERROR, info+"失败")
    return response

'''
    @功能： 检查PC端大转盘配置列表
    @param: para:    JiFenShangChengPara.ZhuanPanChouJiangLieBiao
        checkPara:    JiFenShangChengPara.ZhuanPanChouJiangLieBiaoJianCha
    @return:   true/false
    @author:  chenhui 2016-12-2
'''
def checkLotteryAllocationList(para,checkpara):
    try:
        info='检查PC端大转盘配置列表'
        Log.LogOutput(LogLevel.INFO, info)
        result=getLotteryAllocationList(para=para)
        resultDict=json.loads(result.text)
        listDict= resultDict['rows']
        if findDictInDictlist(checkpara, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, info+"成功!")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, info+'异常')
            return False 
        
'''
    @功能：开启转盘抽奖
    @param :{ids[]:''}
    @return:    response
    @author:  chenhui 2016-11-23
'''  
def openLotteryAllocation(para):
    info='开启转盘抽奖'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/lotteryAllocationManage/updateOpenStates', postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功")
    else:
        Log.LogOutput(LogLevel.ERROR, info+"失败")
    return response

'''
    @功能：关闭转盘抽奖
    @param :{'ids[]':''}
    @return:    response
    @author:  chenhui 2016-11-23
'''  
def closeLotteryAllocation(para):
    info='关闭转盘抽奖'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/lotteryAllocationManage/updateCloseStates', postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功")
    else:
        Log.LogOutput(LogLevel.ERROR, info+"失败")
    return response

'''
    @功能：获取奖品配置列表
    @param :JiFenShangChengPara.JiangPingPeiZhiLieBiao
    @return:    response
    @author:  chenhui 2016-11-23
'''  
def getPrizeSettingList(para):
    info='获取奖品配置列表'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/prizeSettingManage/findPrizeSettingList', postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功")
    else:
        Log.LogOutput(LogLevel.ERROR, info+"失败")
    return response

'''
    @功能： 检查PC端奖品配置列表
    @param: para:    JiFenShangChengPara.JiangPingPeiZhiLieBiao
        checkPara:    JiFenShangChengPara.JiangPingPeiZhiLieBiaoJianCha
    @return:   
    @author:  chenhui 2016-12-2
'''
def checkPrizeSettingList(para,checkpara):
    try:
        info='检查PC端奖品配置列表'
        Log.LogOutput(LogLevel.INFO, info)
        result=getPrizeSettingList(para=para)
        resultDict=json.loads(result.text)
        listDict= resultDict['rows']
        if findDictInDictlist(checkpara, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, info+"成功!")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, info+'异常')
            return False 
        
'''
    @功能：根据奖品等级获取列表prizeSetting.id
    @param :JiFenShangChengPara.JiangPingPeiZhiLieBiao
    @return:    id,若没有找到，则返回0
    @author:  chenhui 2016-11-23
'''  
def getIdByGrade(listpara,prizeGrade):
    info='根据奖品等级获取列表prizeSetting.id'
    Log.LogOutput(LogLevel.INFO, info)
    res=getPrizeSettingList(listpara)
    resDict=json.loads(res.text)
    for item in resDict['rows']:
        if item['prizeGrade']==prizeGrade:
            Log.LogOutput(message='根据奖品等级获取id成功')
            return item['id']
    return 0
'''
    @功能：配置奖品
    @param :JiFenShangChengPara.JiangPingPeiZhi
              file:JiFenShangChengPara.JiangPinPeiZhiFile1
    @return:    response
    @author:  chenhui 2016-11-23
'''  
def setPrize(para,files):
    info='配置奖品'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/prizeSettingManage/updatePrizeSetting', postdata=para,files=files)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功")
    else:
        Log.LogOutput(LogLevel.ERROR, info+"失败")
    return response

'''
    @功能：删除所有的大转盘配置
    @param :{ids[]:''}
    @return:    true/false
    @author:  chenhui 2016-11-23
'''  
def delAllLotteryAllocation():
    info='删除所有转盘抽奖'
    Log.LogOutput(LogLevel.INFO, info)
    para=copy.deepcopy(JiFenShangChengPara.ZhuanPanChouJiangLieBiao)
    response=getLotteryAllocationList(para=para)
    responseDict=json.loads(response.text)
    if responseDict['records']==0:
        Log.LogOutput(message='列表为空，无需删除')
        return True
    else:
        for item in responseDict['rows']:
            delPara={
                     'ids[]':item['id']
                     }
            res=delLotteryAllocation(para=delPara)
            if res.result is False:
                raise Exception('删除转盘抽奖出现异常！')
                return False
        return True
    
'''
    @功能：新增积分商城banner图
    @param para: JiFenShangChengPara.BannerPicAdd
                    files:
    @return:    response
    @author:  chenhui 2016-11-24
'''  
def addBannerPic(para,files):
    info='新增积分商城Banner图'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/storeImageConfigurationManage/addStoreImageConfiguration', postdata=para,files=files)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功")
    else:
            Log.LogOutput(LogLevel.ERROR, info+"失败")
    return response

'''
    @功能：新增积分商城banner图
    @param para: JiFenShangChengPara.BannerPicUpd
                    files:
    @return:    response
    @author:  chenhui 2016-12-2
'''  
def updBannerPic(para,files=None):
    info='修改积分商城Banner图'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/storeImageConfigurationManage/updateStoreImageConfiguration', postdata=para,files=files)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功")
    else:
            Log.LogOutput(LogLevel.ERROR, info+"失败")
    return response


'''
    @功能：获取积分商城Banner图列表
    @param para: JiFenShangChengPara.BannerPicList
    @return:    response
    @author:  chenhui 2016-11-24
'''  
def getBannerPicList(para):
    info='获取积分商城Banner图列表'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/storeImageConfigurationManage/findStoreImageConfigurationList', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功")
    else:
            Log.LogOutput(LogLevel.ERROR, info+"失败")
    return response

'''
    @功能： 检查PC端Banner图
    @param: para:    JiFenShangChengPara.BannerPicList
        checkPara:    JiFenShangChengPara.DuiHuanJiLuJianCha
    @return:   
    @author:  chenhui 2016-12-2
'''
def checkBannerPicInPcList(para,checkpara):
    try:
        info='检查PC端Banner图'
        Log.LogOutput(LogLevel.INFO, info)
        result=getBannerPicList(para=para)
        resultDict=json.loads(result.text)
        listDict= resultDict['rows']
        if findDictInDictlist(checkpara, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, info+"成功!")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, info+'异常')
            return False 

'''
    @功能：删除积分商城banner图
    @param para: {'ids[]':''}
    @return:    response
    @author:  chenhui 2016-11-24
'''  
def delBannerPic(para):
    info='删除积分商城Banner图'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/storeImageConfigurationManage/deleteStoreImageConfigurations', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功")
    else:
            Log.LogOutput(LogLevel.ERROR, info+"失败")
    return response

'''
    @功能：删除积分商城后台所有banner图
    @return:    true/false
    @author:  chenhui 2016-11-24
'''  
def delAllBannerPic():
    info='删除积分商城后台所有banner图'
    Log.LogOutput(LogLevel.INFO, info)
    listPara=copy.deepcopy(JiFenShangChengPara.BannerPicList)
    res=getBannerPicList(listPara)
    resDict=json.loads(res.text)
    if resDict['records']==0:
        Log.LogOutput(message='列表数据为空，无需删除')
        return True
    for item in resDict['rows']:
        para={
              'ids[]':item['id']
              }
        result=delBannerPic(para)
        if result.result is False:
            raise Exception('删除转盘抽奖出现异常！')
            return False
    return True

'''
    @功能：关闭Banner图
    @param :{ids[]:''}
    @return:    response
    @author:  chenhui 2016-11-25
'''  
def closeBannerPic(para):
    info='关闭Banner图'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/storeImageConfigurationManage/unEnable', postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功")
    else:
        Log.LogOutput(LogLevel.ERROR, info+"失败")
    return response

'''
    @功能：关闭Banner图
    @param :{ids[]:''}
    @return:    response
    @author:  chenhui 2016-11-25
'''  
def openBannerPic(para):
    info='打开Banner图'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/storeImageConfigurationManage/enable', postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功")
    else:
        Log.LogOutput(LogLevel.ERROR, info+"失败")
    return response

'''
    @功能： 获取后台积分商城-兑换记录列表
    @para: JiFenShangChengPara.DuiHuanJiLuLieBiao
    @return:   
    @author:  chenhui 2016-9-29
'''
def getOrderList(para):
    response = xiansuoyunwei_post(url='/exchangeRecordManage/findExchangeRecordList', postdata=para)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "获取兑换记录订单列表成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "获取兑换记录订单列表失败")
    return response


'''
    @功能： 后台积分商城兑换记录-取消订单
    @para: {'id':''}
    @return:   
    @author:  chenhui 2016-9-29
'''
def cancelOrder(para):
    response = xiansuoyunwei_post(url='/exchangeRecordManage/cancelOrder', postdata=para)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "取消兑换记录订单成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "取消兑换记录订单失败")
    return response

'''
    @功能： 后台积分商城兑换记录-确认订单
    @para: 
    @return:   response
    @author:  chenhui 2016-9-29
'''
def confirmOrder(para):
    
    response = xiansuoyunwei_post(url='/exchangeRecordManage/confirmExchangeMobileCard', postdata=para)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "兑换记录确认兑换成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "兑换记录确认兑换失败")
    return response

'''
    @功能：通过运维管理平台获取积分信息
    @return:    -1,0,和数字类型
    @author:  chenhui 2016-4-11
'''  
def getPersonalPointsOnPcByUsername(para,userId):
    Log.LogOutput(LogLevel.INFO, "通过userId从PC端获取个人积分信息")
    response = xiansuoyunwei_post(url='/pointsStatisticsManage/findPointsStatisticsList', postdata=para)
#     print response.text
    if response.result is True:
            responseDictList=json.loads(response.text)['rows']
            for item in responseDictList:
                if item['userId']==userId:
                    Log.LogOutput(message='通过userId从PC端获取个人积分成功')
                    return item['sumPoints']
            Log.LogOutput(message='userId没有相应的积分')
            return 0
    else:
            Log.LogOutput(LogLevel.ERROR, "通过userId从PC端获取个人积分信息失败")
            return -1

'''
    @功能：获取抽奖记录列表
    @param :JiFenShangChengPara.ChouJiangJiLuLieBiao
    @return:    response
    @author:  chenhui 2016-12-2
'''  
def getLotteryRecordList(para):
    info='获取抽奖记录列表'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/lotteryRecordManage/findLotteryRecordList', postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功")
    else:
        Log.LogOutput(LogLevel.ERROR, info+"失败")
    return response

'''
    @功能： 检查PC端大转盘配置列表
    @param: para:    JiFenShangChengPara.ChouJiangJiLuLieBiao
        checkPara:    JiFenShangChengPara.ChouJiangJiLuLieBiaoJianCha
    @return:   true/false
    @author:  chenhui 2016-12-2
'''
def checkLotteryRecordList(para,checkpara):
    try:
        info='检查PC端大转盘抽奖记录列表'
        Log.LogOutput(LogLevel.INFO, info)
        result=getLotteryRecordList(para=para)
        resultDict=json.loads(result.text)
        listDict= resultDict['rows']
        if findDictInDictlist(checkpara, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, info+"成功!")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, info+'异常')
            return False 

'''
    @功能： 后台积分商城抽奖记录-确认兑换
    @para:     {'ids[]':''}
    @return:   response
    @author:  chenhui 2016-12-5
'''
def confirmLottery(para):
    response = xiansuoyunwei_post(url='/lotteryRecordManage/confirmExchangeMobileCard', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "抽奖记录确认兑换成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "抽奖记录确认兑换失败")
    return response 

'''
    @功能： 后台积分商城抽奖记录-取消兑换
    @para:     {'id':''}
    @return:   response
    @author:  chenhui 2016-12-5
'''
def cancelLottery(para):
    response = xiansuoyunwei_post(url='/lotteryRecordManage/cancelOrder', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "抽奖记录取消兑换成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "抽奖记录取消兑换失败")
    return response 

'''
    @功能： 添加PC端中奖纪录备注
    @para: {'ids':'',    'remarks':''}
    @return: true/false
    @author:  chenhui 2016-12-5
'''
def updateLotteryRemark(para):
    info='添加PC端中奖纪录备注'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/lotteryRecordManage/updateRemarks', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 获取积分规则id
    @para: departmentNo
    @return:   response
    @author:  chenhui 2016-6-14
'''
def get_point_rule_id_by_depNo(para):
    info='获取区域积分规则id'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/pointsRuleManage/getPointsRuleByDepartmentNo', postdata=para)
#     print response.text
    try:
        resDict=json.loads(response.text)
        Log.LogOutput(message="获取id成功")
        return resDict['id']
    except Exception,e:
        Log.LogOutput(message="获取id出现异常"+str(e))
        return -1 
    
'''
    @功能： 设置积分规则
    @para: JiFenShangChengPara.JiFenGuiZe
    @return:   response
    @author:  chenhui 2016-6-14
'''
def setPointRules(para):
    info='设置积分规则'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/pointsRuleManage/updatePointsRule', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 删除测试自动化省下的商品
    @para: 
    @return:   
    @author:  chenhui 2016-6-14
'''
def deleteGoods():
    try:
        listPara=copy.deepcopy(JiFenShangChengPara.ShangPinLieBiao)
        response = xiansuoyunwei_post(url='/goodsConfigurationManage/findGoodsConfigurationList', postdata=listPara)
#         print response.text
        resDict=json.loads(response.text)
        if resDict['records']==0:
            Log.LogOutput(message='商品数量为0')
            return True
        else:
            arr=[]
            for item in resDict['rows']:
                arr.append(item['id'])
            deleteDict = {'ids[]':tuple(arr)}
            response2 = xiansuoyunwei_post(url='/goodsConfigurationManage/deleteGoodsConfigurations', postdata=deleteDict)
#             print response2.text
            if response2.result is True:
                Log.LogOutput(LogLevel.INFO, '*商品删除成功*')
            else:
                Log.LogOutput(LogLevel.DEBUG, '商品删除失败!')  
    except Exception :
        Log.LogOutput(LogLevel.ERROR, '商品删除异常')
        return False 
    
'''
    @功能： 新增商品
    @para: JiFenShangChengPara.ShangPinXinZeng
    @return: true/false
    @author:  chenhui 2016-6-15
'''
def addMerchandise(para,files):
    info='新增商品'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/goodsConfigurationManage/addGoodsConfiguration', postdata=para,files=files)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response     

'''
    @功能： 修改商品
    @para: JiFenShangChengPara.ShangPinXiuGai
    @return: true/false
    @author:  chenhui 2016-11-29
'''
def updMerchandise(para,files):
    info='修改商品'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/goodsConfigurationManage/updateGoodsConfiguration', postdata=para,files=files)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response   

'''
    @功能： 删除商品
    @para: {'ids[]':''}
    @return: true/false
    @author:  chenhui 2016-11-29
'''
def delMerchandise(para):
    info='删除商品'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/goodsConfigurationManage/deleteGoodsConfigurations', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response   

'''
    @功能： 获取PC端商品列表
    @para: JiFenShangChengPara.ShangPinLieBiao
    @return: true/false
    @author:  chenhui 2016-11-29
'''
def getMerchandiseList(para):
    info='获取PC端商品列表'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/goodsConfigurationManage/findGoodsConfigurationList', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response
 
'''
    @功能： 检查PC端商品信息是否与新增一致
    @para: JiFenShangChengPara.ShangPinLieBiao
        checkPara:JiFenShangChengPara.ShangPinLieBiaoCheck
    @return:   
    @author:  chenhui 2016-11-25
'''
def checkMerchandiseInList(para,checkpara):
    try:
        info='检查PC端商品信息是否与新增一致'
        Log.LogOutput(LogLevel.INFO, info)
        result=getMerchandiseList(para=para)
        resultDict=json.loads(result.text)
        listDict= resultDict['rows']
        if findDictInDictlist(checkpara, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, info+"成功!")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, info+'异常')
            return False 
         
'''
    @功能： 下架商品
    @para: {'ids[]':''}
    @return:   response
    @author:  chenhui 2016-11-29
'''
def closeMerchandise(para):
    info='下架商品'
    Log.LogOutput(message=info)
    response = xiansuoyunwei_post(url='/goodsConfigurationManage/unEnable', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功")
    else:
            Log.LogOutput(LogLevel.ERROR, info+"失败")
    return response  

'''
    @功能： 上架商品
    @para: {'ids[]':''}
    @return:   response
    @author:  chenhui 2016-11-29
'''
def openMerchandise(para):
    info='上架商品'
    Log.LogOutput(message=info)
    response = xiansuoyunwei_post(url='/goodsConfigurationManage/enable', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功")
    else:
            Log.LogOutput(LogLevel.ERROR, info+"失败")
    return response  

'''
    @功能：从数据库中删除兑换记录
    @return:    response
    @author:  chenhui 2016-11-30
'''  
def deleteExchangeRecords(dbUser=Global.XianSuoYunWeiInfo['DbUser'], dbPass=Global.XianSuoYunWeiInfo['DbPass']):
    try:
        Log.LogOutput(LogLevel.INFO, "清除兑换记录")
        count=getDbQueryResult(dbCommand="select count (*) from exchangerecords where departmentno='%s'"%clueOrgInit['DftQuOrgDepNo'],dbUser=dbUser, dbPass=dbPass)
        #print count
        if count>0:
            dbCommand="delete from exchangerecords where departmentno = '%s'"%clueOrgInit['DftQuOrgDepNo'] 
            exeDbQuery(dbCommand = dbCommand, dbUser=dbUser, dbPass=dbPass)
        return True
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '清除兑换记录异常')
            raise Exception('清除兑换记录异常')    
'''
    @功能：从数据库中删除抽奖记录
    @return:    response
    @author:  chenhui 2016-12-2
'''  
def deleteLotteryRecords(dbUser=Global.XianSuoYunWeiInfo['DbUser'], dbPass=Global.XianSuoYunWeiInfo['DbPass']):
    try:
        Log.LogOutput(LogLevel.INFO, "清除抽奖记录")
        count=getDbQueryResult(dbCommand="select count (*) from lotteryrecords where departmentno='%s'"%clueOrgInit['DftQuOrgDepNo'],dbUser=dbUser, dbPass=dbPass)
        #print count
        if count>0:
            dbCommand="delete from lotteryrecords where departmentno = '%s'"%clueOrgInit['DftQuOrgDepNo'] 
            exeDbQuery(dbCommand = dbCommand, dbUser=dbUser, dbPass=dbPass)
        return True
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '清除抽奖记录异常')
            raise Exception('清除抽奖记录异常')
        
'''
    @功能： 确认兑换
    @para: JiFenShangChengPara.ShiWuZiQu
    @return:   response
    @author:  chenhui 2016-12-1
'''
def confirmPhysicalGoodsExchange(para):
    info='确认兑换'
    Log.LogOutput(message=info)
    response = xiansuoyunwei_post(url='/exchangeRecordManage/confirmExchangePhysicalGoods', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功")
    else:
            Log.LogOutput(LogLevel.ERROR, info+"失败")
    return response


'''
    @功能： 获取PC端兑换记录列表
    @para: JiFenShangChengPara.DuiHuanJiLuLieBiao
    @return: true/false
    @author:  chenhui 2016-12-1
'''
def getExchangeRecordList(para):
    info='获取PC端兑换记录列表'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/exchangeRecordManage/findExchangeRecordList', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 检查PC端商品信息是否与新增一致
    @para: JiFenShangChengPara.DuiHuanJiLuLieBiao
        checkPara:JiFenShangChengPara.DuiHuanJiLuJianCha
    @return:   
    @author:  chenhui 2016-12-1
'''
def checkExchangeRecordInList(para,checkpara):
    try:
        info='检查PC端商品信息是否与新增一致'
        Log.LogOutput(LogLevel.INFO, info)
        result=getExchangeRecordList(para=para)
        resultDict=json.loads(result.text)
        listDict= resultDict['rows']
        if findDictInDictlist(checkpara, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, info+"成功!")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, info+'异常')
            return False 
        
'''
    @功能： 添加PC端商品备注
    @para: {'ids':'',    'remarks':''}
    @return: true/false
    @author:  chenhui 2016-12-1
'''
def updateRemark(para):
    info='添加PC端商品备注'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/exchangeRecordManage/updateRemarks', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 新增活动配置
    @para: JiFenShangChengPara.HuoDongXinZeng
    @return:   
    @author:  chenhui 2016-9-27
'''
def addActivity(para):
    info='新增活动'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/activeTimeConfigurationManage/addActiveTimeConfiguration', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response  

'''
    @功能： 修改活动配置
    @para: JiFenShangChengPara.HuoDongXiuGai
    @return:   
    @author:  chenhui 2016-12-1
'''
def updActivity(para):
    info='修改活动配置'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/activeTimeConfigurationManage/updateActiveTimeConfiguration', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response  

'''
    @功能： 获取活动配置列表
    @para: JiFenShangChengPara.HuoDongLieBiao
    @return:   
    @author:  chenhui 2016-9-27
'''
def getActivityList(para):
    info='获取活动配置列表'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/activeTimeConfigurationManage/findActiveTimeConfigurationList', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response  

'''
    @功能： 检查PC活动列表
    @para: JiFenShangChengPara.HuoDongLieBiao
        checkPara:JiFenShangChengPara.HuoDongJianCha
    @return:   true/false
    @author:  chenhui 2016-12-1
'''
def checkInActivityList(para,checkpara):
    try:
        info='检查PC活动列表'
        Log.LogOutput(LogLevel.INFO, info)
        result=getActivityList(para=para)
        resultDict=json.loads(result.text)
        if resultDict['records']==0:
            Log.LogOutput(LogLevel.DEBUG, '列表无数据')
            return False
        listDict= resultDict['rows']
        if findDictInDictlist(checkpara, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, info+"成功!")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, info+'异常')
            return False 
        
'''
    @功能： 暂停活动配置
    @para: {"ids[]":''}
    @return:   
    @author:  chenhui 2016-9-27
'''
def stopActivity(para):
    info='停止活动'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/activeTimeConfigurationManage/unEnable', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 开启活动配置
    @para: {"ids[]":''}
    @return:   
    @author:  chenhui 2016-12-1
'''
def startActivity(para):
    info='开启活动'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/activeTimeConfigurationManage/enable', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 设置显示余额
    @para: {"ids[]":''}
    @return:   response
    @author:  chenhui 2016-12-1
'''
def showBalance(para):
    info='设置显示余额'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/activeTimeConfigurationManage/show', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 设置不显示余额
    @para: {"ids[]":''}
    @return:   respone
    @author:  chenhui 2016-12-1
'''
def unshowBalance(para):
    info='设置不显示余额'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/activeTimeConfigurationManage/unShow', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 删除活动配置
    @para: {'ids[]':''}
    @return:   
    @author:  chenhui 2016-9-27
'''
def delActivity(para):
    info='删除活动'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/activeTimeConfigurationManage/deleteActiveTimeConfigurations', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 删除测试自动化区下的所有活动配置
    @para: 
    @return:   
    @author:  chenhui 2016-9-27
'''
def delAllActivity():
    listPara={
            'activeTimeConfiguration.departmentNo':clueOrgInit['DftQuOrgDepNo'],
            '_search':'false',
            'rows':'20',
            'page':'1',
            'sidx':'id',
            'sord':'desc'          
                          }
    response=getActivityList(para=listPara)
#     print response.text
    if response.result is False:
        Log.LogOutput(LogLevel.ERROR, '获取活动配置列表失败')
        return False
    listDict=json.loads(response.text)
    if listDict['records']==0:
        Log.LogOutput(LogLevel.ERROR,message='列表数为0，无需删除')
        return True
    delPara={
             'ids[]':''
             }
    #声明一list，用于存储id
    temp=[]
    for item in listDict['rows']:
        temp.append(item['id'])
    #将list转为tuple
    delPara['ids[]']=tuple(temp)
#     print delPara['ids[]']
    info='删除测试自动化区下所有活动'
    Log.LogOutput(LogLevel.INFO, info)
    #停止所有活动
    response2=stopActivity(para=delPara)
    if response2.result is False:
        Log.LogOutput(LogLevel.ERROR, message='停止活动失败')
        return False
    #删除所有activity
    response3=delActivity(para=delPara)
    if response3.result is False:
        Log.LogOutput(LogLevel.ERROR, message='删除失败')
        return False
    Log.LogOutput(message='活动删除成功！')
    return True



'''
    @功能： 初始化后台商品配置
    @para: 
    @return:   
    @author:  chenhui 2016-9-27
'''
def initMerchandiseSetting(goodstype='手机卡'):
    
    addMerchandisePara=copy.deepcopy(JiFenShangChengPara.ShangPinXinZeng)
    if goodstype=='手机卡':
        addMerchandisePara['goodsConfiguration.goodsType']=0 
        addMerchandisePara['goodsConfiguration.goodsName']='10元话费'
        addMerchandisePara['goodsConfiguration.quota']=10
        addMerchandisePara['goodsConfiguration.exchangePoints']=5
        addMerchandisePara['goodsConfiguration.goodsNo']='S'+time.strftime("%Y%m%d%H%M%S")+createRandomNumber(length=3)
        #文件参数
        files = {
                 'iosImgValue':open('C:/autotest_file/AppImage/school.png', 'rb'),
                'androidImgValue':open('C:/autotest_file/AppImage/lake.png','rb')
                }     
        return addMerchandise(para=addMerchandisePara,files=files)
    #实物
    else:
        addMerchandisePara['goodsConfiguration.goodsNo']='S'+time.strftime("%Y%m%d%H%M%S")+createRandomNumber(length=3)
        addMerchandisePara['goodsConfiguration.goodsName']='实物测试'
        addMerchandisePara['goodsConfiguration.exchangePoints']=5
        addMerchandisePara['goodsConfiguration.goodsProfile']='商品简介'
        addMerchandisePara['goodsConfiguration.goodsDetails']='商品详情'
        addMerchandisePara['goodsConfiguration.goodsNum']=2
        files = {
                 'iosImgValue':open('C:/autotest_file/Tulips.jpg', 'rb'),
                'androidImgValue':open('C:/autotest_file/Penguins.jpg','rb')
                }   
        return addMerchandise(para=addMerchandisePara,files=files)
        
'''
    @功能： 初始化后台活动配置
    @para: 
    @return:   
    @author:  chenhui 2016-9-27
'''
def initActivitySetting():
    addActivityPara={
            'startDate':Time.getCurrentDate(),
            'endDate':Time.getCurrentDate(),
            'activeTimeConfiguration.goodsType':'0',
            'activeTimeConfiguration.exchangeCeiling':'20',
            'activeTimeConfiguration.goodsTotal':'30',
            'activeTimeConfiguration.departmentNo':clueOrgInit['DftQuOrgDepNo'],
            'activeTimeConfiguration.orgName':clueOrgInit['DftQuOrg'],
                     }
    addActivityPara['activeTimeConfiguration.activityNo']='HD'+time.strftime("%Y%m")+addActivityPara['activeTimeConfiguration.departmentNo']+createRandomNumber(length=4)
    return addActivity(para=addActivityPara).result      