# -*- coding:UTF-8 -*-
'''
Created on 2016-6-14

@author: N-133
'''
from __future__ import unicode_literals
from COMMON import Log
from COMMON.CommonUtil import findDictInDictlist
from CONFIG import Global, InitDefaultPara
from CONFIG.Define import LogLevel
from Interface.PingAnJianShe.ShiJianChuLi import ShiJianChuLiIntf
from Interface.XianSuoApp.xianSuoHttpCommon import xiansuo_post
from Interface.YunWeiPingTai.XiTongPeiZhi import XiTongPeiZhiPara, \
    XiTongPeiZhiIntf
import copy
import json
import random

'''
    @功能： 设置积分，默认设置为0
    @para: 
    @return: 
    @author:  chenhui 2016-6-14
'''    
def setPointByMobile(mobile=Global.XianSuoDftMobile,point=0):
    Log.LogOutput( message='设置积分')
    ShiJianChuLiIntf.exeDbQuery(dbCommand="update pointsstatistics_2016 p set p.sumpoints=%s where p.userid=(select id from \
    users where mobile='%s' ) "%(point,mobile),dbUser=Global.XianSuoYunWeiInfo['DbUser'],dbPass=Global.XianSuoYunWeiInfo['DbPass'])
#表更新，加了年份后缀
'''
    @功能： 删除积分规则
    @para: 
    @return: 
    @author:  chenhui 2016-6-14
'''    
def deletePointRuleByDb(departmentno=InitDefaultPara.clueOrgInit['DftQuOrgDepNo']):
    Log.LogOutput(message='删除积分规则')
    ShiJianChuLiIntf.exeDbQuery(dbCommand="delete from pointsrules p where p.departmentno='%s'"%departmentno\
                                    ,dbUser=Global.XianSuoYunWeiInfo['DbUser'],dbPass=Global.XianSuoYunWeiInfo['DbPass'])


'''
    @功能： 删除积分兑换记录
    @para: 
    @return: 
    @author:  chenhui 2016-6-14
'''    
def deleteExchangeRecord(mobile=Global.XianSuoDftMobile):
    Log.LogOutput(message='删除兑换记录')
    ShiJianChuLiIntf.exeDbQuery(dbCommand="delete from exchangerecords e where e.userid=(select id from users where mobile ='%s')"%mobile\
                                    ,dbUser=Global.XianSuoYunWeiInfo['DbUser'],dbPass=Global.XianSuoYunWeiInfo['DbPass'])
       

'''
    @功能： 查看商品列表
    @para: 
    @return:   
    @author:  chenhui 2016-6-15
'''
def getMerchandiseListForMobile(para):
    info='查看手机端商品列表'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuo_post(url='/api/clue/goodsConfigurationMobileDubboService/findGoodsConfigurationListForMobile', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 通过商品名称获取商品id
    @para: 商品名称
    @return:   成功返回id，失败返回-1
    @author:  chenhui 2017-5-17
'''
def get_goods_id_by_name(name):
    info='通过商品名称获取商品id'
    Log.LogOutput(LogLevel.INFO, info)
    listPara={
                'tqmobile':'true',
                'departmentNo':InitDefaultPara.clueOrgInit['DftQuOrgDepNo'],
                'mobileType':'ios',
                'page':'1',
                'rows':'100'
                  }
    response=getMerchandiseListForMobile(listPara)
    try:
        resDict=json.loads(response.text)
        for item in resDict['response']['module']['rows']:
            if item['goodsName']==name:
                Log.LogOutput(message='查找到id')
                return item['id']
        Log.LogOutput(message='查找id失败')
        return -1
    except Exception,e:
        Log.LogOutput(message='查找id异常'+str(e))
        return -1

'''
    @功能： 查看商品详情
    @para: 
    @return:   
    @author:  chenhui 2016-6-15
'''
def getMerchandiseDetailForMobile(para):
    info='查看手机端商品详情'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuo_post(url='/api/clue/goodsConfigurationMobileDubboService/getGoodsConfigurationById', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 检查商品是否存在于商品列表中
    @para: 
    @return:   
    @author:  chenhui 2016-6-15
'''
def checkMerchandiseInListForMobile(listpara,checkpara):
    try:
        info='验证商品是否能够在手机端商品列表显示'
        Log.LogOutput(LogLevel.INFO, info)
        result=getMerchandiseListForMobile(para=listpara)
        resultDict=json.loads(result.text)
        if resultDict['response']['module']['records']==0:
            Log.LogOutput(LogLevel.DEBUG, "列表无数据")
            return False
        listDict= resultDict['response']['module']['rows']
        if findDictInDictlist(checkpara, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, info+"成功!")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, info+'异常')
            print result.text
            return False 

       
'''
    @功能： 积分兑换商品
    @para: 
    @return:   
    @author:  chenhui 2016-6-15
'''
def exchangeMerchandise(para):
    info='积分兑换商品'
    Log.LogOutput(LogLevel.INFO, info)
#     response = xiansuo_post(url='/api/clue/exchangeRecordMobileDubboService/addExchangeRecord', postdata=para)
#接口更新
#     response = xiansuo_post(url='/api/clue/exchangeRecordMobileDubboService/addExchangeRecordNew', postdata=para)
    response = xiansuo_post(url='/api/clue/exchangeRecordMobileDubboService/addExchangeRecordTwo', postdata=para)
#    print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response    


'''
    @功能： 查看兑换记录
    @para: 
    @return:   
    @author:  chenhui 2016-6-15
'''
def getExchangeRecord(para):
    info='查看手机端积分兑换记录'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuo_post(url='/api/clue/exchangeRecordMobileDubboService/findExchangeRecordListForMobile', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response    

'''
    @功能： 检查兑换记录列表是否正确
    @para: listpara:    XsJiFenShangChengPara.DuiHuanJiLu
                checkpara:
    
    @return:   
    @author:  chenhui 2016-6-15
'''
def checkExchangeRecord(listpara,checkpara):
    try:
        info='检查手机端兑换记录'
        Log.LogOutput(LogLevel.INFO, info)
        result=getExchangeRecord(para=listpara)
        resultDict=json.loads(result.text)
        listDict= resultDict['response']['module']['rows'][0]['exchangeRecord']
        #将字典listDict转为列表,[listDict]
        if findDictInDictlist(checkpara, [listDict]) is True:
            Log.LogOutput(LogLevel.DEBUG, info+"成功!")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, info+'异常')
            return False 
        
'''
    @功能：     生成一个随机数字字符串，默认6位
    @para: 
    length: 随机数位数，默认为6位
    @return: 返回一个包含大小写字母和数字的字符串
'''

def createRandomNumber(length=6):
    code_list = []
    #用于存储返回的随机数字列表
    random_string=''
    for i in range(10): # 0-9数字
        code_list.append(str(i))
    for j in range(length):
        #将返回的[]转为str类型,并追加到random_string后
        random_string+=''.join(random.sample(code_list, 1))
    return random_string

'''
    @功能： 初始化积分配置
    @para: 
    @return:   
    @author:  chenhui 2016-9-27
'''
def initPointSetting():
    param = copy.deepcopy(XiTongPeiZhiPara.updateJiFenPeiZhi)
    param['pointsSetting.id'] =1
    param['pointsSetting.points'] = 6
    param['pointsSetting.todayMaxPoints']=0
    if XiTongPeiZhiIntf.updateJiFenPeiZhi(param).result is False:
        Log.LogOutput(LogLevel.ERROR, '积分爆料初始化配置出错')
        return False
    param['pointsSetting.id'] =2
    param['pointsSetting.points'] = 5
    param['pointsSetting.todayMaxPoints']=10
    if XiTongPeiZhiIntf.updateJiFenPeiZhi(param).result is False:
        Log.LogOutput(LogLevel.ERROR, '积分关注初始化配置出错')
        return False
    param['pointsSetting.id'] =3
    param['pointsSetting.points'] = 3
    param['pointsSetting.todayMaxPoints']=6
    if XiTongPeiZhiIntf.updateJiFenPeiZhi(param).result is False:
        Log.LogOutput(LogLevel.ERROR, '积分点赞初始化配置出错')
        return False
    param['pointsSetting.id'] =4
    param['pointsSetting.points'] = 4
    param['pointsSetting.todayMaxPoints']=8
    if XiTongPeiZhiIntf.updateJiFenPeiZhi(param).result is False:
        Log.LogOutput(LogLevel.ERROR, '积分评论初始化配置出错')
        return False
    param['pointsSetting.id'] =5
    param['pointsSetting.points'] = 7
    param['pointsSetting.todayMaxPoints']=14
    if XiTongPeiZhiIntf.updateJiFenPeiZhi(param).result is False:
        Log.LogOutput(LogLevel.ERROR, '积分受理初始化配置出错')
        return False
    param['pointsSetting.id'] =6
    param['pointsSetting.points'] = 10
    param['pointsSetting.todayMaxPoints']=20
    if XiTongPeiZhiIntf.updateJiFenPeiZhi(param).result is False:
        Log.LogOutput(LogLevel.ERROR, '积分用户邀请初始化配置出错')
        return False
    param['pointsSetting.id'] =7
    param['pointsSetting.points'] = 2
    param['pointsSetting.todayMaxPoints']=4
    if XiTongPeiZhiIntf.updateJiFenPeiZhi(param).result is False:
        Log.LogOutput(LogLevel.ERROR, '积分用户评分初始化配置出错')
        return False
    param['pointsSetting.id'] =8
    param['pointsSetting.points'] = 1
    param['pointsSetting.todayMaxPoints']=0
    if XiTongPeiZhiIntf.updateJiFenPeiZhi(param).result is False:
        Log.LogOutput(LogLevel.ERROR, '积分每日签到初始化配置出错')
        return False
    param['pointsSetting.id'] =9
    param['pointsSetting.points'] = 5
    param['pointsSetting.todayMaxPoints']=0
    if XiTongPeiZhiIntf.updateJiFenPeiZhi(param).result is False:
        Log.LogOutput(LogLevel.ERROR, '积分连续签到初始化配置出错')
        return False
    param['pointsSetting.id'] =10
    param['pointsSetting.points'] = 20
    param['pointsSetting.todayMaxPoints']=0
    if XiTongPeiZhiIntf.updateJiFenPeiZhi(param).result is False:
        Log.LogOutput(LogLevel.ERROR, '积分注册初始化配置出错')
        return False
    return True

'''
    @功能： 获取banner图信息
    @para: XsJiFenShangChengPara.BannerPicInfo
    @return:   response
    @author:  chenhui 2016-11-24
'''
def getBannerInfo(para):
    info='获取banner图信息'
    Log.LogOutput(message=info)
    response = xiansuo_post(url='/api/clue/goodsConfigurationMobileDubboService/findStoreImageConfigurationListForMobileNew', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功")
    else:
            Log.LogOutput(LogLevel.ERROR, info+"失败")
    return response

'''
    @功能： 检查Banner图信息是否与后台新增一致
    @para: XsJiFenShangChengPara.BannerPicInfo
        checkPara:XsJiFenShangChengPara.BannerPicInfoCheck
    @return:   
    @author:  chenhui 2016-11-24
'''
def checkBannerInfo(para,checkpara):
    try:
        info='检查Banner信息'
        Log.LogOutput(LogLevel.INFO, info)
        result=getBannerInfo(para=para)
        resultDict=json.loads(result.text)
        listDict= resultDict['response']['module']
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
    @功能： 获取大转盘信息
    @para: XsJiFenShangChengPara.DaZhuanPanPeiZhi
    @return:   response
    @author:  chenhui 2016-11-25
'''
def getlotteryAllocationInfo(para):
    info='手机端获取大转盘信息'
    Log.LogOutput(message=info)
    response = xiansuo_post(url='/api/clue/lotteryAllocationMobileDubboService/getLotteryAllocationByDepartmentNo', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功")
    else:
            Log.LogOutput(LogLevel.ERROR, info+"失败")
    return response   

'''
    @功能： 检查Banner图信息是否与后台新增一致
    @para: XsJiFenShangChengPara.DaZhuanPanPeiZhi
        checkPara:XsJiFenShangChengPara.DaZhuanPanPeiZhiCheck
    @return:   
    @author:  chenhui 2016-11-25
'''
def checklotteryAllocationInfo(para,checkpara):
    try:
        info='检查Banner信息'
        Log.LogOutput(LogLevel.INFO, info)
        result=getlotteryAllocationInfo(para=para)
        resultDict=json.loads(result.text)
        listDict= resultDict['response']['module']
        #将字典listDict转为列表,[listDict]
        if findDictInDictlist(checkpara, [listDict]) is True:
            Log.LogOutput(LogLevel.DEBUG, info+"成功!")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, info+'异常')
            return False 
        
'''
    @功能： 用户抽奖
    @para: XsJiFenShangChengPara.ChouJiang
    @return:   response
    @author:  chenhui 2016-11-25
'''
def addLotteryRecord(para):
    info='用户抽奖'
    Log.LogOutput(message=info)
    response = xiansuo_post(url='/api/clue/lotteryAllocationMobileDubboService/addLotteryRecord', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功")
    else:
            Log.LogOutput(LogLevel.ERROR, info+"失败")
#            Log.LogOutput(message=response.text)
    return response   

'''
    @功能： 获取用户抽奖列表
    @para: XsJiFenShangChengPara.ZhongJiangJiLu
    @return:   response
    @author:  chenhui 2016-12-2
'''
def getLotteryRecordListForMobile(para):
    info='获取用户抽奖列表'
    Log.LogOutput(message=info)
    response = xiansuo_post(url='/api/clue/lotteryAllocationMobileDubboService/findLotteryRecordListForMobile', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功")
    else:
            Log.LogOutput(LogLevel.ERROR, info+"失败")
    return response   

'''
    @功能： 检查手机端中奖纪录列表
    @para: XsJiFenShangChengPara.ZhongJiangJiLu
        checkPara:XsJiFenShangChengPara.ZhongJiangJiLuJianCha
    @return:   
    @author:  chenhui 2016-12-5
'''
def checkLotteryListForMobile(para,checkpara):
    try:
        info='检查手机端中奖纪录列表'
        Log.LogOutput(LogLevel.INFO, info)
        result=getLotteryRecordListForMobile(para=para)
        resultDict=json.loads(result.text)
        if resultDict['response']['module']['records']==0:
            Log.LogOutput(message='列表数据为0')
            return False
        listDict= resultDict['response']['module']['rows']
        #拼接新的待检查列表
        newList=[]
        for item in listDict:
            newList.append(item['lotteryRecord'])
        #在newList中查找字典项
        if findDictInDictlist(checkpara, newList) is True:
            Log.LogOutput(LogLevel.DEBUG, info+"成功!")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, info+'异常')
            return False 

'''
    @功能： 补充中奖人信息
    @para: XsJiFenShangChengPara.ZhongJiangXinXiBuChong
    @return:   response
    @author:  chenhui 2016-12-2
'''
def updateLotteryRecordForMobile(para):
    info='补充中奖人信息'
    Log.LogOutput(message=info)
    response = xiansuo_post(url='/api/clue/lotteryAllocationMobileDubboService/updateLotteryRecord', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功")
    else:
            Log.LogOutput(LogLevel.ERROR, info+"失败")
    return response
        
'''
    @功能： 获取余额信息
    @para:{ "departmentNo": 959595,
                "tqmobile": "true"}
    @return:   response
    @author:  chenhui 2016-12-1
'''
def getBalance(para):
    info='获取余额信息'
    Log.LogOutput(message=info)
    response = xiansuo_post(url='/api/clue/goodsConfigurationMobileDubboService/getActiveTimeConfigurationByDepartmentNo', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功")
    else:
            Log.LogOutput(LogLevel.ERROR, info+"失败")
    return response   

'''
    @功能： 检查余额信息显示是否正确
    @para: { "departmentNo": 959595,
                "tqmobile": "true"}
        checkPara:{
                "activityNo": '',
                "balanceShow": 0}
    @return:   
    @author:  chenhui 2016-11-25
'''
def checkBalanceInfo(para,checkpara):
    try:
        info='检查商品余额信息'
        Log.LogOutput(LogLevel.INFO, info)
        result=getBalance(para=para)
        resultDict=json.loads(result.text)
        listDict= resultDict['response']['module']
        #将字典listDict转为列表,[listDict]
        if findDictInDictlist(checkpara, [listDict]) is True:
            Log.LogOutput(LogLevel.DEBUG, info+"成功!")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, info+'异常')
            return False 
        
'''
    @功能： 手机端获取积分规则
    @para:{ "departmentNo": 959595,
                "tqmobile": "true"}
    @return:   response
    @author:  chenhui 2016-12-1
'''
def getPointRule(para):
    info='手机端获取积分规则'
    Log.LogOutput(message=info)
    response = xiansuo_post(url='/api/clue/pointsStatisticsDubboService/getPointsruleByDepartmentNo', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功")
    else:
            Log.LogOutput(LogLevel.ERROR, info+"失败")
    return response   