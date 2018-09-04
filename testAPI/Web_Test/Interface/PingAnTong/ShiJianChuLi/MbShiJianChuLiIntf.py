# -*- coding:UTF-8 -*-
'''
Created on 2015-11-5

@author: N-254
'''
from __future__ import unicode_literals
from Web_Test.COMMON import CommonUtil, Log
from Web_Test.COMMON.CommonUtil import checkExcelCellValue, regMatchString
from Web_Test.COMMON.Time import getLinuxDateAndTime
from Web_Test.CONFIG import Global
from Web_Test.CONFIG.Define import LogLevel
from Web_Test.CONFIG.InitDefaultPara import userInit,orgInit
from Web_Test.Interface.PingAnJianShe import ShiJianChuLi
from Web_Test.Interface.PingAnJianShe.Common import CommonIntf
from Web_Test.Interface.PingAnJianShe.Common.CommonIntf import getOrgInfoByAccount, \
    getDbQueryResultList,getDbQueryResult
from Web_Test.Interface.PingAnJianShe.ShiJianChuLi.ShiJianChuLiPara import *
from Web_Test.Interface.PingAnJianShe.pingAnJianSheHttpCommon import pinganjianshe_post, \
    pinganjianshe_get
from Web_Test.Interface.PingAnTong.pingAnTongHttpCommon import pingantong_post, \
    pingantong_get
import copy
import cx_Oracle
import json
import os
import paramiko
import xlrd


'''
    @功能：手机新增事件
    @para:issueAddPara
    @return:    true/false
    @author:  chenhui 2016-1-27
'''  
def mAddIssue(para, username = userInit['DftJieDaoUser'], password = '11111111'):
    Log.LogOutput(level=LogLevel.INFO, message='新增事件')
    response = pingantong_post(url='/mobile/issueNewMobileManage/addIssue.action', postdata=para, username=username, password=password)
#    Log.LogOutput(LogLevel.DEBUG,response.text)
    return response

'''
    @功能：手机查看事件
    @para:issueAddPara
    @return:    true/false
    @author:  chenhui 2016-1-27
'''  
def mViewIssue(para, username = userInit['DftJieDaoUser'], password = '11111111'):
    Log.LogOutput(level=LogLevel.INFO, message='查看事件')
    response = pingantong_post(url='/mobile/issueNewMobileManage/viewIssueDetail.action', postdata=para, username=username, password=password)
#     Log.LogOutput(LogLevel.DEBUG,response.text)
    responseDict=json.loads(response.text)
    return responseDict

'''
    @功能：手机我的待办列表显示
    @para:myTodoIssueListPara
    @return:    response
    @author:  chenhui 2016-1-27
'''  
def mMyTodoList(para, username = userInit['DftJieDaoUser'], password = '11111111'):
    Log.LogOutput(level=LogLevel.DEBUG, message='显示我的待办事项列表数据')
    response = pingantong_post(url='/mobile/issueNewMobileManage/findNeedDoIssueList.action', postdata=para, username=username, password=password)
#     Log.LogOutput(LogLevel.DEBUG,response.text)
    return response
    
'''
    @功能：手机我的已办列表显示
    @para:myTodoIssueListPara
    @return:    response
    @author:  chenhui 2016-2-23
'''  
def mMyDoneList(para, username = userInit['DftJieDaoUser'], password = '11111111'):
    Log.LogOutput(level=LogLevel.DEBUG, message='显示我的已办事项列表数据')
    response = pingantong_post(url='/mobile/issueNewMobileManage/searchDoneIssues.action', postdata=para, username=username, password=password)
#     Log.LogOutput(LogLevel.DEBUG,response.text)
    return response

'''
    @功能：手机我的已办列表显示
    @para:myTodoIssueListPara
    @return:    response
    @author:  chenhui 2016-2-23
'''  
def mMyCompleteList(para, username = userInit['DftJieDaoUser'], password = '11111111'):
    Log.LogOutput(level=LogLevel.DEBUG, message='显示我的已办结事项列表数据')
    response = pingantong_post(url='/mobile/issueNewMobileManage/findCompletedIssues.action', postdata=para, username=username, password=password)
#     Log.LogOutput(LogLevel.DEBUG,response.text)
    return response

'''
    @功能：手机我的已办列表显示
    @para:myTodoIssueListPara
    @return:    response
    @author:  chenhui 2016-2-23
'''  
def mMyLimitList(para, username = userInit['DftJieDaoUser'], password = '11111111'):
    Log.LogOutput(level=LogLevel.DEBUG, message='显示我的限时办结事项列表数据')
    response = pingantong_post(url='/mobile/issueCompleteLimitMobileManage/findMyAllIssues.action', postdata=para, username=username, password=password)
#     Log.LogOutput(LogLevel.DEBUG,response.text)
    return response

'''
    @功能：手机我的下辖待办列表显示
    @para:myTodoIssueListPara
    @return:    response
    @author:  chenhui 2016-2-23
'''  
def mMyDownTodoList(para, username = userInit['DftJieDaoUser'], password = '11111111'):
    Log.LogOutput(level=LogLevel.DEBUG, message='显示我的下辖待办事项列表数据')
    response = pingantong_post(url='/mobile/issueNewMobileManage/findMyJurisdictionsNeedDo.action', postdata=para, username=username, password=password)
#     Log.LogOutput(LogLevel.DEBUG,response.text)
    return response

'''
    @功能：手机我的下辖待办列表显示
    @para:myTodoIssueListPara
    @return:    response
    @author:  chenhui 2016-2-23
'''  
def mMyDownCompleteList(para, username = userInit['DftJieDaoUser'], password = '11111111'):
    Log.LogOutput(level=LogLevel.DEBUG, message='显示我的下辖已办结事项列表数据')
    response = pingantong_post(url='/mobile/issueNewMobileManage/findJurisdictionsDoneIssues.action', postdata=para, username=username, password=password)
#     Log.LogOutput(LogLevel.DEBUG,response.text)
    return response

'''
    @功能：检查事件是否存在于我的待办事项列表中
    @para:checkPara:{issueId,dealState,supervisionState}
    @param 
    @return:    true/false
    @author:  chenhui 2016-1-27
'''  
def mCheckIssueInMyTodoList(checkPara,listPara,username=userInit['DftJieDaoUser'],password='11111111'):
    try:
        response=mMyTodoList(para=listPara,username=username)
        Log.LogOutput( message='正在验证我的待办页面是否存在待检查事件')
        if response.result is False:
            Log.LogOutput(LogLevel.ERROR,'请求结果异常，请检查输入参数listPara')
            return False
        responseDict = json.loads(response.text)
#         Log.LogOutput(level=LogLevel.DEBUG, message=response.text)
        if responseDict['records']==0:
            Log.LogOutput(LogLevel.DEBUG,'列表数据为空！')
            return False
        else:
            listDict = responseDict['rows']
            if CommonUtil.findDictInDictlist(checkPara, listDict) is True:
                Log.LogOutput(message='列表有数据，并且查找数据成功')
                return True
            else:
                Log.LogOutput(message="列表有数据，但是查找数据失败")
                Log.LogOutput(level=LogLevel.DEBUG, message=response.text)
                return False
    except Exception as e :
        Log.LogOutput(LogLevel.ERROR, '我的待办列表验证出现异常！'+str(e))    
        return False
    
'''
    @功能：检查事件是否存在于我的已办事项列表中
    @para:checkPara:{issueId,dealState,supervisionState}
    @param 
    @return:    true/false
    @author:  chenhui 2016-2-23
'''  
   
def mCheckIssueInMyDoneList(checkPara,listPara,username=userInit['DftJieDaoUser'],password='11111111'):
    try:
        response=mMyDoneList(para=listPara,username=username)
        Log.LogOutput( message='正在验证我的已办页面是否存在待检查事件')
        if response.result is False:
            Log.LogOutput(LogLevel.ERROR,'请求结果异常，请检查输入参数listPara')
            return False
        responseDict = json.loads(response.text)
#         Log.LogOutput(level=LogLevel.DEBUG, message=response.text)
        if responseDict['records']==0:
            Log.LogOutput(LogLevel.DEBUG,'列表数据为空！')
            return False
        else:
            listDict = responseDict['rows']
            if CommonUtil.findDictInDictlist(checkPara, listDict) is True:
                Log.LogOutput(message='列表有数据，并且查找数据成功')
                return True
            else:
                Log.LogOutput(message="列表有数据，但是查找数据失败")
                Log.LogOutput(level=LogLevel.DEBUG, message=response.text)
                return False
    except Exception as e :
        Log.LogOutput(LogLevel.ERROR, '我的已办列表验证出现异常！'+str(e))    
        return False

'''
    @功能：检查事件是否存在于我的已办结事项列表中
    @para:checkPara:{issueId,dealState,supervisionState}
    @param 
    @return:    true/false
    @author:  chenhui 2016-2-23
'''  
   
def mCheckIssueInMyCompleteList(checkPara,listPara,username=userInit['DftJieDaoUser'],password='11111111'):
    try:
        response=mMyCompleteList(para=listPara,username=username)
        Log.LogOutput( message='正在验证我的已办结页面是否存在待检查事件')
        if response.result is False:
            Log.LogOutput(LogLevel.ERROR,'请求结果异常，请检查输入参数listPara')
            return False
        responseDict = json.loads(response.text)
#        Log.LogOutput(level=LogLevel.DEBUG, message=response.text)
        if responseDict['records']==0:
            Log.LogOutput(LogLevel.DEBUG,'列表数据为空！')
            return False
        else:
            listDict = responseDict['rows']
            if CommonUtil.findDictInDictlist(checkPara, listDict) is True:
                Log.LogOutput(message='列表有数据，并且查找数据成功')
                return True
            else:
                Log.LogOutput(message="列表有数据，但是查找数据失败")
                Log.LogOutput(level=LogLevel.DEBUG, message=response.text)
                return False
    except Exception as e :
        Log.LogOutput(LogLevel.ERROR, '我的已办结列表验证出现异常！'+str(e))    
        return False

'''
    @功能：检查事件是否存在于我的限时办结事项列表中
    @para:checkPara:{issueId,dealState,supervisionState}
    @param 
    @return:    true/false
    @author:  chenhui 2016-2-23
'''  
   
def mCheckIssueInMyLimitList(checkPara,listPara,username=userInit['DftJieDaoUser'],password='11111111'):
    try:
        response=mMyLimitList(para=listPara,username=username)
        Log.LogOutput( message='正在验证我的限时办结页面是否存在待检查事件')
        if response.result is False:
            Log.LogOutput(LogLevel.ERROR,'请求结果异常，请检查输入参数listPara')
            return False
        responseDict = json.loads(response.text)
#         Log.LogOutput(level=LogLevel.DEBUG, message=response.text)
        if responseDict['records']==0:
            Log.LogOutput(LogLevel.DEBUG,'列表数据为空！')
            return False
        else:
            listDict = responseDict['rows']
            if CommonUtil.findDictInDictlist(checkPara, listDict) is True:
                Log.LogOutput(message='列表有数据，并且查找数据成功')
                return True
            else:
                Log.LogOutput(message="列表有数据，但是查找数据失败")
                Log.LogOutput(level=LogLevel.DEBUG, message=response.text)
                return False
    except Exception as e :
        Log.LogOutput(LogLevel.ERROR, '我的已办结列表验证出现异常！'+str(e))    
        return False
      
'''
    @功能：检查事件是否存在于我的下辖待办事项列表中
    @para:checkPara:{issueId,dealState,supervisionState}
    @param 
    @return:    true/false
    @author:  chenhui 2016-2-23
'''  
   
def mCheckIssueInMyDownTodoList(checkPara,listPara,username=userInit['DftJieDaoUser'],password='11111111'):
    try:
        response=mMyDownTodoList(para=listPara,username=username)
        Log.LogOutput( message='正在验证我的下辖待办页面是否存在待检查事件')
        if response.result is False:
            Log.LogOutput(LogLevel.ERROR,'请求结果异常，请检查输入参数listPara')
            return False
        responseDict = json.loads(response.text)
#         Log.LogOutput(level=LogLevel.DEBUG, message=response.text)
        if responseDict['records']==0:
            Log.LogOutput(LogLevel.DEBUG,'列表数据为空！')
            return False
        else:
            listDict = responseDict['rows']
            if CommonUtil.findDictInDictlist(checkPara, listDict) is True:
                Log.LogOutput(message='列表有数据，并且查找数据成功')
                return True
            else:
                Log.LogOutput(message="列表有数据，但是查找数据失败")
                Log.LogOutput(level=LogLevel.DEBUG, message=response.text)
                return False
    except Exception as e :
        Log.LogOutput(LogLevel.ERROR, '我的下辖待办列表验证出现异常！'+str(e))    
        return False
    
'''
    @功能：检查事件是否存在于我的下辖已办结事项列表中
    @para:checkPara:{issueId,dealState,supervisionState}
    @param 
    @return:    true/false
    @author:  chenhui 2016-2-23
'''  
   
def mCheckIssueInMyDownCompleteList(checkPara,listPara,username=userInit['DftJieDaoUser'],password='11111111'):
    try:
        response=mMyDownCompleteList(para=listPara,username=username)
        Log.LogOutput( message='正在验证我的下辖已办结页面是否存在待检查事件')
        if response.result is False:
            Log.LogOutput(LogLevel.ERROR,'请求结果异常，请检查输入参数listPara')
            return False
        responseDict = json.loads(response.text)
#         Log.LogOutput(level=LogLevel.DEBUG, message=response.text)
        if responseDict['records']==0:
            Log.LogOutput(LogLevel.DEBUG,'列表数据为空！')
            return False
        else:
            listDict = responseDict['rows']
            if CommonUtil.findDictInDictlist(checkPara, listDict) is True:
                Log.LogOutput(message='列表有数据，并且查找数据成功')
                return True
            else:
                Log.LogOutput(message="列表有数据，但是查找数据失败")
                Log.LogOutput(level=LogLevel.DEBUG, message=response.text)
                return False
    except Exception as e :
        Log.LogOutput(LogLevel.ERROR, '我的下辖已办结列表验证出现异常！'+str(e))    
        return False
    
'''
    @功能：手机我的待办新增页面查找事件大类
    @para: tqmobile、orgId
    @return:    responseDict
    @author:  chenhui 2016-2-3
'''  
def mFindHeadingType(para, username = userInit['DftJieDaoUser'], password = '11111111'):
    Log.LogOutput(level=LogLevel.DEBUG, message='返回事件大类')
    response = pingantong_post(url='/mobile/issueTypeMobileManage/findHeadingType.action', postdata=para, username=username, password=password)
#     Log.LogOutput(LogLevel.DEBUG,response.text)
    responseDict=json.loads(response.text)
    return responseDict

'''
    @功能：手机我的待办新增页面查找事件小类
    @para: 
    @return:    responseDict
    @author:  chenhui 2016-2-4
'''  
def mFindSmallType(para, username = userInit['DftJieDaoUser'], password = '11111111'):
    Log.LogOutput(level=LogLevel.DEBUG, message='返回事件小类')
    response = pingantong_post(url='/mobile/issueTypeMobileManage/findChildrenByParentId.action', postdata=para, username=username, password=password)
#     Log.LogOutput(LogLevel.DEBUG,response.text)
    responseDict=json.loads(response.text)
    return responseDict

'''
    @功能：设置自定义大类、小类
    @para: 
    @return:    
    @author:  chenhui 2016-2-3
'''  
def mInitSelfIssueType(username = 'admin', password = 'admin'):
    #判断自动化区下有无设置自定义大类
    response = pinganjianshe_post(url='/issues/selfdomIssuetype/findSelfdomIssueTypeDomains.action', postdata={'orgId':orgInit['DftQuOrgId']}, username=username, password=password)
    responseDict=json.loads(response.text)
    #如果list为空
    if not len(responseDict):
        Log.LogOutput(message='没有自定义事件类型，将初始化自定义事件类型')
        #新增大类
        para1={
               'selfdomIssueTypeDomain.organization.id':orgInit['DftQuOrgId'],
               'selfdomIssueTypeDomain.domainName':'测试大类1'
               }
        response1 = pinganjianshe_post(url='/issues/selfdomIssuetype/addSelfdomIssuetypeDomain.action', postdata=para1, username=username, password=password)
        responseDict1=json.loads(response1.text)
        para1['selfdomIssueTypeDomain.domainName']='测试大类2'
        response2 = pinganjianshe_post(url='/issues/selfdomIssuetype/addSelfdomIssuetypeDomain.action', postdata=para1, username=username, password=password)
        responseDict2=json.loads(response2.text)
        #新增小类
        spara1={
                'mode':'addSelfdomIssueType',
                'selfdomIssueType.id':'',
                'selfdomIssueType.domain.id':responseDict1['id'],
                'selfdomIssueType.indexId':'',
                'selfdomIssueType.enabled':'',
                'selfdomIssueType.typeName':'测试小类1.1'
                }
        r10=pinganjianshe_post(url='/issues/selfdomIssuetype/addSelfdomIssueType.action', postdata=spara1, username=username, password=password)
        spara1['selfdomIssueType.typeName']='测试小类1.2'
        r11=pinganjianshe_post(url='/issues/selfdomIssuetype/addSelfdomIssueType.action', postdata=spara1, username=username, password=password)
        spara2={
                'mode':'addSelfdomIssueType',
                'selfdomIssueType.id':'',
                'selfdomIssueType.domain.id':responseDict2['id'],
                'selfdomIssueType.indexId':'',
                'selfdomIssueType.enabled':'',
                'selfdomIssueType.typeName':'测试小类2.1'
                }
        r20=pinganjianshe_post(url='/issues/selfdomIssuetype/addSelfdomIssueType.action', postdata=spara2, username=username, password=password)
        spara2['selfdomIssueType.typeName']='测试小类2.2'
        r21=pinganjianshe_post(url='/issues/selfdomIssuetype/addSelfdomIssueType.action', postdata=spara2, username=username, password=password)
        
        #创建关联
        rpara={
               'selectIds':str(json.loads(r10.text)['id'])+',1'
               }
        pinganjianshe_post(url='/issues/selfdomIssuetype/addSelfdomIssueType.action', postdata=rpara, username=username, password=password)
        rpara['selectIds']=str(json.loads(r11.text)['id'])+',20'
        pinganjianshe_post(url='/issues/selfdomIssuetype/addSelfdomIssueType.action', postdata=rpara, username=username, password=password)
        rpara['selectIds']=str(json.loads(r20.text)['id'])+',32'
        pinganjianshe_post(url='/issues/selfdomIssuetype/addSelfdomIssueType.action', postdata=rpara, username=username, password=password)
        rpara['selectIds']=str(json.loads(r21.text)['id'])+',%s'%(getDbQueryResult(dbCommand ="select id from issuetypes where domainid='4'"))
        pinganjianshe_post(url='/issues/selfdomIssuetype/addSelfdomIssueType.action', postdata=rpara, username=username, password=password)
    else:
        Log.LogOutput(message='自定义类型已存在')
        
'''
    @功能：停用所有自定义小类
    @para: 
    @return:    
    @author:  chenhui 2016-2-4
'''  
def mStopAllSelfIssueType(username = userInit['DftShiUser'], password = '11111111'):
    Log.LogOutput( message='停用所有小类')
    rsList=getDbQueryResultList(dbCommand="select id from selfdomissuetypes")
    para={
             'ids':rsList,
             'enabled':2 
              }
    pinganjianshe_post(url='/issues/selfdomIssuetype/enabledOperate.action', postdata=para, username=username, password=password)

'''
    @功能：删除所有自定义小类和大类
    @para: 
    @return:    
    @author:  chenhui 2016-2-4
'''  
def mDeleteAllSelfIssueType(username = userInit['DftShiUser'], password = '11111111'):
    if Global.simulationEnvironment is False:
        #如果存在小类，则删除小类
        if getDbQueryResult(dbCommand="select count(*) from selfdomissuetypes") !=0:
            Log.LogOutput( message='删除所有小类')
            rsList=getDbQueryResultList(dbCommand="select id from selfdomissuetypes")
            para={
                     'ids':rsList
                      }
            pinganjianshe_post(url='/issues/selfdomIssuetype/deleteSelfdomIssueTypeByIds.action', postdata=para, username=username, password=password)
        #删除大类
        response=pinganjianshe_post(url='/issues/selfdomIssuetype/findSelfdomIssueTypeDomains.action',postdata={'orgId':orgInit['DftQuOrgId']}, username=username, password=password)
        dict=json.loads(response.text)
        #如果存在大类,则删除
        if  len(dict):
            Log.LogOutput( message='删除所有大类')
            #获取列表大类id并删除
            para2={
                       'selfdomIssueTypeDomain.id':''
                        }
            for item in dict:
                para2['selfdomIssueTypeDomain.id']=item['id']
                pinganjianshe_post(url='/issues/selfdomIssuetype/deleteSelfdomIssueTypeDomainById.action', postdata=para2, username=username, password=password)
    else:
        Log.LogOutput(message='仿真环境，跳过小类删除')
'''
    @功能：手机处理事件
    @para: 
    @return:    responseDict
    @author:  chenhui 2016-2-22
'''  
def mDealIssue(para, username = userInit['DftJieDaoUser'], password = '11111111'):
    Log.LogOutput(level=LogLevel.DEBUG, message='处理事件...')
    response = pingantong_post(url='/mobile/issueNewMobileManage/dealIssue.action', postdata=para, username=username, password=password)
    Log.LogOutput(LogLevel.DEBUG,'dealIssue：'+response.text)
    responseDict=json.loads(response.text)
    return responseDict

'''
    @功能：手机处理事件
    @para: 
    @return:    responseDict
    @author:  chenhui 2016-2-26
'''  
def mApplyIssueDelay(para, username = userInit['DftJieDaoUser'], password = '11111111'):
    Log.LogOutput(level=LogLevel.DEBUG, message='延时申请...')
    response = pingantong_post(url='/mobile/issueCompleteLimitMobileManage/addIssueCompleteDelay.action', postdata=para, username=username, password=password)
    
    if response.text is False:
        Log.LogOutput(LogLevel.DEBUG,'申请延时返回出错：'+response.text)
    responseDict=json.loads(response.text)
    return responseDict
