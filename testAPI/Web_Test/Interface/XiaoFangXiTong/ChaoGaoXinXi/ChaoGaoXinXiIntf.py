# -*- coding:UTF-8 -*-

'''
Created on 2016-6-16

@author: N-66
'''
from __future__ import unicode_literals
from Interface.XiaoFangXiTong import xiaoFangXiTongHttpCommon
from CONFIG.Define import LogLevel
from COMMON import Log, CommonUtil
import copy
import json
from Interface.XiaoFangXiTong.ChaoGaoXinXi import ChaoGaoXinXiPara

def add_ChaoGao(ChaoGaoDict,username=None,password=None):
    xiaoFangXiTongHttpCommon.xiaofang_post(url='/fire/firetrapNoticeManage/saveOrUpdateFiretrapNotice.action',postdata=ChaoGaoDict,username=username,password=password)
    Log.LogOutput(LogLevel.INFO,'新增抄告成功..')

def audit_Approve(Dict,username=None,password=None):
    xiaoFangXiTongHttpCommon.xiaofang_post(url='/fire/firetrapNoticeApproveManage/saveOrUpdateFiretrapNoticeApprove.action',postdata=Dict,username=username,password=password)
    Log.LogOutput(LogLevel.INFO,'站长审批开始..')
    
def add_ZhiFa(Dict,username=None,password=None):   
    xiaoFangXiTongHttpCommon.xiaofang_post(url='/fire/lawEnforcementInfoManage/saveLawEnforcementInfo.action',postdata=Dict,username=username,password=password)
    Log.LogOutput(LogLevel.INFO,'新增执法开始..')

def check_ZhangZhanChaoGao(ZhangZhanChaoGaoDict,username=None,password=None):   
    try:
        Log.LogOutput(LogLevel.INFO, "站长查看抄告开始")
        compareDict=copy.deepcopy(ChaoGaoXinXiPara.GetZhangZhanChaoGao)
        compareDict['orgId']='410'
        rs=xiaoFangXiTongHttpCommon.xiaofang_get(url='/fire/firetrapNoticeManage/queryFiretrapNoticeListOfApprove.action',param=compareDict,username='zdhjd@',password='11111111')
        responseDict=json.loads(rs.text)
        listDict=responseDict['rows']
        if CommonUtil.findDictInDictlist(ZhangZhanChaoGaoDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "站长查看抄告成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "站长查看超过失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查看失败')
            return False 

def check_LingDaoShenPi(LingDaoShenPiDict,username=None,password=None):
    try:
        Log.LogOutput(LogLevel.INFO, "领导查看审批开始")
        compareDict=copy.deepcopy(ChaoGaoXinXiPara.GetLingDaoShenPi)
        compareDict['orgId']='410'
        rs=xiaoFangXiTongHttpCommon.xiaofang_get(url='/fire/firetrapNoticeManage/queryFiretrapNoticeListOfApprove.action',param=compareDict,username='zdhjd@',password='11111111')
        responseDict=json.loads(rs.text)
        listDict=responseDict['rows']
        if CommonUtil.findDictInDictlist(LingDaoShenPiDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "领导查看抄告成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "领导查看抄告失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.DEBUG, "查看失败")
            return False
        
def check_ZhiFa(ZhiFaDict,username=None,password=None):
    try:
        Log.LogOutput(LogLevel.INFO, "查看执法开始")
        compareDict=copy.deepcopy(ChaoGaoXinXiPara.GetZhiFa)
        rs=xiaoFangXiTongHttpCommon.xiaofang_get(url='/fire/firetrapSuperviseManage/getFiretrapSuperviseList.action',param=compareDict,username='zdhjd@',password='11111111')
        responseDict=json.loads(rs.text)
        listDict=responseDict['rows']
        if CommonUtil.findDictInDictlist(ZhiFaDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "执法查看成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "执法查看失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.DEBUG, "查看失败")
            return False
            

        
    
    
    