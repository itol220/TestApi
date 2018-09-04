# -*- coding:UTF-8 -*-
'''
Created on 2016-6-13

@author: N-66
'''
import copy
import json
from COMMON import Log,CommonUtil
from CONFIG.Define import LogLevel
from Interface.XiaoFangXiTong import xiaoFangXiTongHttpCommon
from Interface.XiaoFangXiTong.XuanChuanPeiXun import XuanChuanPeiXunPara
from Interface.XiaoFangXiTong.Common.InitDefaultPara import orgInit


def Add_PeiXunHuoDong(PeiXunHuoDongDict,username=None,password=None):
        Log.LogOutput(LogLevel.INFO, "新增培训活动开始")
        response=xiaoFangXiTongHttpCommon.xiaofang_post(url='/fire/fireTrainingInfoManage/saveFireTrainingInfo.action',postdata=PeiXunHuoDongDict,username=username,password=password)
        return response 
    
    

def Get_PeiXunHuoDong(PeiXunHuoDongDict,username=None,password=None):
    try:
        Log.LogOutput(LogLevel.INFO, "查看培训活动开始")
        compDict = copy.deepcopy(XuanChuanPeiXunPara.GetPeiXunHuoDong)
        compDict['orgId']=orgInit['DftSheQuOrgId']
        response = xiaoFangXiTongHttpCommon.xiaofang_get(url='/fire/fireTrainingInfoManage/getFireTrainingInfoList.action', param=compDict,username=username, password = password)
        responseDict = json.loads(response.text)                    
        listDict= responseDict['rows']
        if CommonUtil.findDictInDictlist(PeiXunHuoDongDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "查看培训活动成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查看培训活动失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查看失败')
            return False     
 
def Edit_PeiXunHuoDong(PeiXunHuoDongDict,username=None,password=None):
    Log.LogOutput(LogLevel.INFO,'修改培训活动开始..')
    response=xiaoFangXiTongHttpCommon.xiaofang_post(url='/fire/fireTrainingInfoManage/saveFireTrainingInfo.action',postdata=PeiXunHuoDongDict,username=username,password=password)
    return response        
#         
# def Check_PeiXunHuoDong(PeiXunHuoDongDict,username=None,password=None):
#     try:
#         Log.LogOutput(LogLevel.INFO, "查看培训活动详细开始")
#         compDict={'fireTrainingInfoId':''
#                   }
#         response = xiaoFangXiTongHttpCommon.xiaofangxitong_post(url='/fire/fireTrainingInfoManage/getFireTrainingInfoList.action', postdata=compDict,username=username, password = password)          
                  
def Del_PeiXunHuoDong(PeiXunHuoDongDict,username=None,password=None):
    Log.LogOutput(LogLevel.INFO, '删除培训活动开始..')
    response = xiaoFangXiTongHttpCommon.xiaofang_get(url='/fire/fireTrainingInfoManage/deletefireTrainingInfoById.action', param=PeiXunHuoDongDict,username=username, password = password)
    return response
    
def Add_XuanChuanHuoDong(XuanChuanHuoDongDict,username=None,password=None):    
    Log.LogOutput(LogLevel.INFO,'新增宣传活动开始..')
    response=xiaoFangXiTongHttpCommon.xiaofang_post(url='/fire/firePublicInfoManage/saveFirePublicInfo.action',postdata=XuanChuanHuoDongDict,username=username,password=password)
    return response

def Get_XuanChuanHuoDong(XuanChuanHuoDongDict,username=None,password=None):
    try:
        Log.LogOutput(LogLevel.INFO, "查看宣传活动开始")
        compDict = copy.deepcopy(XuanChuanPeiXunPara.GetPeiXunHuoDong)
        compDict['orgId']=orgInit['DftWangGeOrgId']
        response = xiaoFangXiTongHttpCommon.xiaofang_get(url='/fire/firePublicInfoManage/getFirePublicInfoListByParam.action', param=compDict,username=username, password = password)
        responseDict = json.loads(response.text)   
        listDict= responseDict['rows']
        if CommonUtil.findDictInDictlist(XuanChuanHuoDongDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "查看宣传活动成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查看宣传活动失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查看失败')
            return False     

def Edit_XuanChuanHuoDong(XuanChuanHuoDongDict,username=None,password=None):
    Log.LogOutput(LogLevel.INFO,'修改宣传活动开始..')
    response=xiaoFangXiTongHttpCommon.xiaofang_post(url='/fire/firePublicInfoManage/saveFirePublicInfo.action',postdata=XuanChuanHuoDongDict,username=username,password=password)
    return response

def Del_XuanChuanHuoDong(XuanChuanHuoDongDict,username=None,password=None):
    Log.LogOutput(LogLevel.INFO,'删除宣传活动开始..')
    response=xiaoFangXiTongHttpCommon.xiaofang_get(url='/fire/firePublicInfoManage/deleteFirePublicInfoById.action', param=XuanChuanHuoDongDict,username=username, password = password)
    return response                                    

def Add_XueXiZiLiao(XueXiZiLiaoDict,username=None,password=None):
    Log.LogOutput(LogLevel.INFO,'新增学习资料开始..')
    response=xiaoFangXiTongHttpCommon.xiaofang_post(url='/fire/fireNoticeManage/saveFireNoticeInfo.action',postdata=XueXiZiLiaoDict,username=username,password=password)
    return response

def Get_XueXiZiLiao(XueXiZiLiaoDict,username=None,password=None):
    try:
        compDict=copy.deepcopy(XuanChuanPeiXunPara.GetXueXiZiLiao)
        compDict['orgId']=orgInit['DftSheQuOrgId']
        compDict['queryParameter.orgId']=compDict['orgId']
        response = xiaoFangXiTongHttpCommon.xiaofang_get(url='/fire/fireNoticeManage/getFireNoticeInfoByParam.action', param=compDict,username=username, password = password)
        responseDict = json.loads(response.text)   
        listDict= responseDict['rows']
        if CommonUtil.findDictInDictlist(XueXiZiLiaoDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "查看学习资料成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查看学习资料失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查看失败')
            return False
def Edit_XueXiZiLiao(XueXiZiLiaoDict,username=None,password=None):
    Log.LogOutput(LogLevel.INFO,'修改学习资料开始..')
    xiaoFangXiTongHttpCommon.xiaofang_post(url='/fire/fireNoticeManage/saveFireNoticeInfo.action',postdata=XueXiZiLiaoDict,username=username,password=password)

def Del_XueXiZiLiao(XueXiZiLiaoDict,username=None,password=None):
    Log.LogOutput(LogLevel.INFO,'删除学习资料开始..')
    xiaoFangXiTongHttpCommon.xiaofang_get(url='/fire/fireNoticeManage/deleteFireNoticeById.action', param=XueXiZiLiaoDict,username=username, password = password)
    
    
    
    
    
    
    
    
    
    
    
