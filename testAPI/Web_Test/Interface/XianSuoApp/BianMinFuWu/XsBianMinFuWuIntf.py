# -*- coding:UTF-8 -*-
'''
Created on 2016-4-8

@author: N-286
'''
from __future__ import unicode_literals
from COMMON import Log
from COMMON.CommonUtil import findDictInDictlist
from CONFIG.Define import LogLevel
from Interface.XianSuoApp.BianMinFuWu.XsBianMinFuWuPara import \
    changYongDianHuaLieBiao
from Interface.XianSuoApp.xianSuoHttpCommon import xiansuo_post
from Interface.YunWeiPingTai.yunWeiPingTaiHttpCommon import xiansuoyunwei_post
import copy
import json

'''
    @功能：PC运维管理平台新增电话分类 
    @para: 
    @return: response  
    @author:  chenhui 2016-4-8
'''  
def addPhoneCategory(para):
    Log.LogOutput(LogLevel.INFO, "新增电话分类")
    response = xiansuoyunwei_post(url='/companyCategoryManage/addCompanyCategory', postdata=para)
    #print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "新增电话分类成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "新增电话分类失败")
    return response

    '''
    @功能： PC运维管理平台电话管理
    @para: 
    @return: response  
    @author:  chenhui 2016-4-8
    '''  
def addPhone(para):
    Log.LogOutput(LogLevel.INFO, "新增电话")
    response = xiansuoyunwei_post(url='/companyPhoneManage/addCompanyPhone', postdata=para)
    #print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "新增电话成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "新增电话失败")
    return response    

    '''
    @功能： app查看便民电话
    @para: 
    @return: response  
    @author:  chenhui 2016-4-8
    '''    
def viewPhoneList(para):
    Log.LogOutput(LogLevel.INFO, "查看电话")
    response = xiansuo_post(url='/api/clue/companyPhoneDubboService/findCompanyPhoneListByCompanyName', postdata=para)
    #print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "查看电话成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "查看电话失败")
    return response

    '''
    @功能： 通过查看编码服务列表检查新增是否成功
    @para: 
    @return: 如果检查成功，则返回True；否则返回False  
    @author:  chenhui 2016-4-8
    '''    
def checkPhoneInList(checkPara,listPara):
    try:
        Log.LogOutput(LogLevel.INFO, "检查记录是否存在于便民服务中")
        response=viewPhoneList(para=listPara)
        responseDict = json.loads(response.text)
#         print response.text
        listDict= responseDict['response']['module']['rows']
        if findDictInDictlist(checkPara, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "检测电话成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "检测电话失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '检测异常')
            return False
    
    '''
    @功能： 删除全部便民服务电话
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
    @author:  chenhui 2016-4-8
    '''    
def deleteAllPhones():
    try:
        Log.LogOutput(message='正在清空所有便民服务...')
        listPara = copy.deepcopy(changYongDianHuaLieBiao)
        #print listPara
        response = xiansuoyunwei_post(url='/companyCategoryManage/findCompanyCategoryList', postdata=listPara)
        #print response.text
        responseDict = json.loads(response.text)
        if responseDict['records'] == 0:
            Log.LogOutput(LogLevel.DEBUG, '列表数据为空')
        else:
            #存储所有ID
            arr=[]
            for dictListItem in responseDict['rows']:
                arr.append(dictListItem['id'])
            deleteDict = {'ids[]':tuple(arr)}
            #print deleteDict
            response=xiansuoyunwei_post(url='/companyCategoryManage/deleteCompanyCategorys',postdata=deleteDict)
            if response.result is True:
                Log.LogOutput(LogLevel.INFO, '*删除成功*')
            else:
                Log.LogOutput(LogLevel.ERROR, '删除失败!')   
    except Exception :
        Log.LogOutput(LogLevel.ERROR, '删除异常')
        return False 