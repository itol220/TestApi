# -*- coding:UTF-8 -*-
'''
Created on 2016-4-8

@author: N-286
'''
from __future__ import unicode_literals
from COMMON import Log
from COMMON.CommonUtil import findDictInDictlist
from CONFIG import Global
from CONFIG.Define import LogLevel
from Interface.XianSuoApp.xianSuoHttpCommon import xiansuo_post
from Interface.YunWeiPingTai.yunWeiPingTaiHttpCommon import xiansuoyunwei_post
import json
from CONFIG import InitDefaultPara


'''
    @功能：获取积分排名信息
    @param para:  {'tqmobile':'true',    'departmentNo':InitDefaultPara.xianSuoOrgInit['DftQuOrgIdNo']}
    @return:    response
    @author:  chenhui 2016-4-8
'''  
def getPersonalPoints(para):
    Log.LogOutput(LogLevel.INFO, "获取个人积分排名信息")
    response = xiansuo_post(url='/api/clue/pointsStatisticsDubboService/getPointsStatisticsForMobileByUserId', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "获取个人积分排名信息成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "获取个人积分排名信息失败")
    return response

'''
    @功能：获取个人积分
    @param para:  {'tqmobile':'true','departmentNo':InitDefaultPara.clueOrgInit['DftQuOrgDepNo']}
    @return:    response
    @author:  chenhui 2016-4-8
'''  
def getPersonalPointsToNum(para,mobile=Global.XianSuoDftMobile, password=Global.XianSuoDftPassword):
    Log.LogOutput(LogLevel.INFO, "获取个人积分排名信息")
    response = xiansuo_post(url='/api/clue/pointsStatisticsDubboService/getPointsStatisticsForMobileByUserId', postdata=para,mobile=mobile,password=password)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "获取个人积分排名信息成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "获取个人积分排名信息失败")
            return
    return json.loads(response.text)['response']['module']['pointsStatistics']['sumPoints']

'''
    @功能：获取积分列表
    @return:    response
    @param :     XsPaiHangBangPara.getPersonalPointRankingList
    @author:  chenhui 2016-11-8
'''  
def getPointsList(para):
    Log.LogOutput(LogLevel.INFO, "获取积分列表")
    response = xiansuo_post(url='/api/clue/pointsStatisticsDubboService/findPointsStatisticsListForMobileByUserId', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "获取积分列表成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "获取积分列表失败")
    return response


'''
    @功能：获取区县积分列表成功
    @return:    response
    @param :    XsPaiHangBangPara.getPersonalPointListPara
    @author:  chenhui 2016-11-9
'''  
def getPointsInCountyList(para):
    Log.LogOutput(LogLevel.INFO, "获取区县积分列表")
    response = xiansuo_post(url='/api/clue/pointsStatisticsDubboService/findPointsStatisticsListForMobile', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "获取区县积分列表成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "获取区县积分列表失败")
    return response

'''
    @功能：检查个人积分字典是否位于积分列表中
    @param :  checkDict:    XsPaiHangBangPara.checkPersonalPointListPara
                    listpara:        XsPaiHangBangPara.getPersonalPointListPara
    @return:    True/False
    @author:  chenhui 2016-11-8
'''  
def checkPersonalPointInList(checkDict, listpara):
    try:
        info='检查个人积分是否位于积分列表中'
        Log.LogOutput(LogLevel.INFO, info)
        result=getPointsList(para=listpara)
        resultDict=json.loads(result.text)
        listDict= resultDict['response']['module']['rows']
        newList=[]
        for item in listDict:
            newList.append(item['pointsStatistics'])
        #将字典listDict转为列表,[listDict]
        for item in newList:
            if checkDict==item:
#         if findDictInDictlist(checkpara, newList) is True:
                Log.LogOutput(LogLevel.DEBUG, info+"成功!")
                return True
#         else:
        Log.LogOutput(LogLevel.DEBUG, info+"失败!")
        return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, info+'异常')
            return False 


'''
    @功能：检查个人积分字典是否位于区县积分列表中
    @param : checkDict:    XsPaiHangBangPara.checkPersonalPointListPara
                    listpara:    XsPaiHangBangPara.getPointsInCountyListPara
    @return:    True/False
    @author:  chenhui 2016-11-8
'''  
def checkPersonalPointInCountyList(checkDict, listpara):
    try:
        info='检查个人积分是否位于区县积分列表中'
        Log.LogOutput(LogLevel.INFO, info)
        result=getPointsInCountyList(para=listpara)
#         print result.text
        resultDict=json.loads(result.text)
        total=resultDict['response']['module']['total']
        count=1
        #该接口数据每页返回10行
        while count<=total:
            listDict= resultDict['response']['module']['rows']
            newList=[]
            for item in listDict:
                newList.append(item['pointsStatistics'])
            #将字典listDict转为列表,[listDict]
            for item in newList:
    #             if checkDict==listDict:
                if findDictInDictlist(checkDict, newList) is True:
                    Log.LogOutput(LogLevel.DEBUG, info+"成功!")
                    return True
            count=count+1
            listpara['page']=count
            result=getPointsInCountyList(para=listpara)
            resultDict=json.loads(result.text)
            print listpara['page']
    #         else:
        Log.LogOutput(LogLevel.DEBUG, info+"失败!")
        return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, info+'异常')
            return False
               
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
    @功能：通过个人排行榜信息获取用户id
    @return:  userId  
    @author:  chenhui 2016-4-11
''' 
def getUserIdByPersonalPoints():
    Log.LogOutput(LogLevel.INFO, "通过个人排行榜信息获取用户id开始---")
    try:
        para1={
                   'tqmobile':'true',
                   'departmentNo':InitDefaultPara.clueOrgInit['DftQuOrgDepNo']
                   }
        result=getPersonalPoints(para=para1)
#         print result.text
        resultDict=json.loads(result.text)
        userId=resultDict['response']['module']['pointsStatistics']['userId']
        Log.LogOutput(message='获取用户id成功，并返回')
        return userId
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '获取用户id过程中异常')
        return False