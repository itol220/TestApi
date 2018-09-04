# -*- coding:UTF-8 -*-
'''
Created on 2016-3-31

@author: N-133
'''
from __future__ import unicode_literals
from COMMON import Log
from COMMON.CommonUtil import findDictInDictlist
from CONFIG.Define import LogLevel
from CONFIG.InitDefaultPara import userInit, orgInit, clueOrgInit
from Interface.PingAnJianShe.pingAnJianSheHttpCommon import pinganjianshe_post, \
    pinganjianshe_get
from Interface.XianSuoApp.GongGaoLan.XsGongGaoLanPara import GongGaoLieBiao
from Interface.XianSuoApp.xianSuoHttpCommon import xiansuo_post, xiansuo_get
import copy
import json


'''
    @功能：PC新增公告
    @return:    response
    @author:  chenhui 2016-03-31
'''  
def addClueProclamation(para, username = userInit['DftQuUser'], password = '11111111'):
    Log.LogOutput(level=LogLevel.INFO, message='新增公告')
    response = pinganjianshe_post(url='/clueManage/clueInformationManage/addClueProclamation.action', postdata=para, username=username, password=password)
    #print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "新增公告成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "新增公告失败")
    return response

'''
    @功能：PC获取公告列表
    @return:    response
    @author:  chenhui 2016-4-5
'''  
def getClueProclamationList(para, username = userInit['DftQuUser'], password = '11111111'):
    Log.LogOutput(level=LogLevel.INFO, message='获取公告列表')
    response = pinganjianshe_post(url='/clueManage/clueInformationManage/findClueInformationPageBySearchsInfoVo.action', postdata=para, username=username, password=password)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "获取列表成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "获取列表失败")
    return response

'''
    @功能：PC修改公告状态
    @return:    response
    @author:  chenhui 2016-04-5
'''  
def updClueProclamationState(para, username = userInit['DftQuUser'], password = '11111111'):
    Log.LogOutput(level=LogLevel.INFO, message='修改公告状态')
    response = pinganjianshe_post(url='/clueManage/clueInformationManage/updateInformationShowStateByIds.action', postdata=para, username=username, password=password)
    #print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "修改公告状态成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "修改公告状态失败")
    return response

'''
    @功能：大江东区下删除所有实时动态
    @return:    response
    @author:  chenhui 2017-04-01
'''  
def delAllClueProclamation():
    Log.LogOutput(level=LogLevel.INFO, message='删除所有公告信息')
    #获取列表
    listPara=copy.deepcopy(GongGaoLieBiao)
    listPara['searchInfoVo.information.orgId']=clueOrgInit['DftQuOrgId']
    response=getClueProclamationList(para=listPara)
    responseDict=json.loads(response.text)
    if responseDict['records'] == 0:
        Log.LogOutput(message='列表数据为空，无需清除')
    else:
            #存储所有ID
            arr=[]
            for dictListItem in responseDict['rows']:
                arr.append(dictListItem['information']['id'])
            #将所有数组中的事件ID转化为字符串参数值，以，隔开
            arrString=''
            for i in range(0,len(arr)):
                if i==0:
                    arrString=str(arr[i])
                else:
                    arrString=arrString+','+str(arr[i])
            deleteDict = {'ids':str(arrString)}
            response=pinganjianshe_get(url='/clueManage/clueInformationManage/updateInformationDelStateByIds.action',param=deleteDict)
    #print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "删除公告成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "删除公告失败")
    return response

'''
    @功能：获取公告列表
    @return:    response
    @author:  chenhui 2016-04-5
'''  
def getNoticeList(para):
    Log.LogOutput(level=LogLevel.INFO, message='获取公告列表')
    response = xiansuo_post(url='/api/clue/informationDubboService/findNoticesForPageForMobile', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "获取公告列表成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "获取公告列表失败")
    return response    


    '''
    @功能： 通过app公告列表检测是否获取成功
    @para: 
    @return: 如果检查成功，则返回True；否则返回False  
    @author:  chenhui 2016-4-5
    '''    
def checkNoticeInList(checkPara,listPara):
    try:
        Log.LogOutput(LogLevel.INFO, "检查记录是否存在于列表中")
        response=getNoticeList(para=listPara)
        responseDict = json.loads(response.text)
        listDict= responseDict['response']['module']['rows']
        #定义一个空列表
        newList=[]
        #重新组装待检查列表
        for item in listDict:
            newList.append(item['information'])
        #调用检查列表参数
        if findDictInDictlist(checkPara, newList) is True:
            Log.LogOutput(LogLevel.DEBUG, "检测成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "检测失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '检测异常')
            return False

'''
    @功能：获取公告详细信息
    @return:    response
    @author:  chenhui 2016-04-5
'''  
def getNoticeInfo(para):
    Log.LogOutput(level=LogLevel.INFO, message='获取公告详细信息')
    response = xiansuo_get(url='/api/clue/informationDubboService/getNoticesById', param=para)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "获取公告成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "获取公告失败")
    #print response.text
    return response    
    
'''
    @功能： 获取手机端运维公告列表
    @para:     XsGongGaoLanPara.shouJiYunWeiGongGaoLieBiao
    @return:   response
    @author:  chenhui 2016-12-9
'''
def get_mobile_operation_notice_list(para):
    info='获取手机端运维公告列表'
    Log.LogOutput(message=info)
    response = xiansuo_post(url='/api/clue/operationNoticeDubboService/findOperationNoticeForPageForMobile', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功")
    else:
            Log.LogOutput(LogLevel.ERROR, info+"失败")
    return response

'''
    @功能： 检查手机端运维公告列表
    @para:     listPara:    XsGongGaoLanPara.shouJiYunWeiGongGaoLieBiao
                    checkPara:    XsGongGaoLanPara.
    @return:   response
    @author:  chenhui 2016-12-9
'''
def check_mobile_operation_notice_list(checkPara,listPara):
    try:
        info='检查手机端运维公告列表'
        Log.LogOutput(LogLevel.INFO, info)
        response=get_mobile_operation_notice_list(para=listPara)
        responseDict = json.loads(response.text)
        listDict= responseDict['response']['module']['rows']
        #调用检查列表参数
        if findDictInDictlist(checkPara, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, info+"成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, info+'异常')
            return False