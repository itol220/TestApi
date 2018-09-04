# -*- coding:UTF-8 -*-
'''
Created on 2015-11-5

@author: N-254
'''
from __future__ import unicode_literals
from COMMON import CommonUtil, Log
from COMMON.CommonUtil import checkExcelCellValue, regMatchString
from COMMON.Time import getLinuxDateAndTime, getCurrentDateAndTime, setLinuxTime
from CONFIG import Global
from CONFIG.Define import LogLevel
from CONFIG.InitDefaultPara import userInit
from Interface.PingAnJianShe import ShiJianChuLi
from Interface.PingAnJianShe.Common import CommonIntf
from Interface.PingAnJianShe.Common.CommonIntf import getOrgInfoByAccount
from Interface.PingAnJianShe.ShiJianChuLi.ShiJianChuLiPara import *
from Interface.PingAnJianShe.pingAnJianSheHttpCommon import pinganjianshe_post, \
    pinganjianshe_get
from Interface.PingAnTong.ShiJianChuLi.MbShiJianChuLiIntf import \
    mDeleteAllSelfIssueType
import copy
import cx_Oracle
import json
import os
import paramiko
import time
import xlrd

def addIssue(issueDict, username = userInit['DftJieDaoUser'], password = '11111111'):
    Log.LogOutput(level=LogLevel.INFO, message='新增事件')
    response = pinganjianshe_post(url='/issues/issueManage/addIssue.action', postdata=issueDict, username=username, password=password)
#     Log.LogOutput(LogLevel.DEBUG,response.text)
    responseDict = json.loads(response.text)
    return responseDict

    '''
    @功能：新增事件2
    @para: 
    @return: 返回response  
    @author:  chenhui 2016-6-22
    '''    
def addIssue2(issueDict, username = userInit['DftJieDaoUser'], password = '11111111'):
    Log.LogOutput(level=LogLevel.INFO, message='新增事件')
    response = pinganjianshe_post(url='/issues/issueManage/addIssue.action', postdata=issueDict, username=username, password=password)
#     Log.LogOutput(LogLevel.DEBUG,response.text)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "新增事件成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "新增事件失败")    
    return response

def pushIssueToFire(issueId, username = None, password = None):
    response = pinganjianshe_get(url='/issues/issueManage/shengPingTaiPushIssueForFire.action', param={'issue.id':issueId},username=username, password = password)
    if response.result is True:
        return True
    else:
        return False
def deleteIssue(keyid, username=None, password=None):
    response = pinganjianshe_get(url='/issues/issueManage/deleteIssue.action', param={'keyId':keyid}, username=username, password=password)
#    print response.text
    if response.text == 'true':
        Log.LogOutput(level=LogLevel.DEBUG, message='删除成功')
        return True   
    else:
        Log.LogOutput(level=LogLevel.ERROR, message='删除失败')
        return False
              
def checkIssue(checkIssueDict,username=None, password=None):
    issueListPara = copy.deepcopy(ShiJianChuLi.ShiJianChuLiPara.issueListPara)
    issueListPara['organization.id'] = CommonIntf.getOrgInfoByAccount(username)['orgId']
    response = pinganjianshe_get(url='/issues/issueNewManage/findMyAllIssues.action', param=issueListPara, username=username, password=password)   
    responseDict = json.loads(response.text)
    listDict = responseDict['rows']
#    Log.LogOutput(level=LogLevel.DEBUG, message='listDict:%s'%listDict)
    if CommonUtil.findDictInDictlist(checkIssueDict, listDict) is True:
        Log.LogOutput(message='查找事件成功')
        return True
    else:
        Log.LogOutput(LogLevel.ERROR,message="查找事件失败")
        return False

def updIssue(issueDict, username=None, password=None):
    Log.LogOutput(message='正在修改事件')
    issueDict['issue.occurOrg.id']=CommonIntf.getOrgInfoByAccount(username)['orgId']
    response = pinganjianshe_post(url='/issues/issueManage/updateIssue.action', postdata=issueDict, username=username, password=password)
    return response

def viewIssue(issueDict,username=None,password=None):
    orgId=CommonIntf.getOrgInfoByAccount(username)['orgId']
    response = pinganjianshe_get(url='/mobile/issueMobileManage/findNeedDoIssueList.action', param={'orgId':orgId}, username=username, password=password)
#     print '查看事件结果%s'%response.text
    responseDict = json.loads(response.text)
    listDict = responseDict['rows']
    if CommonUtil.findDictInDictlist(issueDict, listDict) is True:
        Log.LogOutput(message='查看事件成功')
        return True
    else:
        Log.LogOutput(LogLevel.ERROR,message="查看事件失败")
        return False
    
def searchMyToDoIssue(issueDict,username=None,password=None):
    response=pinganjianshe_get(url='/issues/searchIssue/searchIssue.action', param=issueDict, username=username, password=password)
#      response.text是个Unicode对象，需要先转化成string
    src=response.text#.encode("utf-8")
#如果传入的是单值
    if issueDict['searchIssueVo.inputFrom']==''or issueDict['searchIssueVo.inputFrom'] is None:
        return CommonUtil.regMatchString(src,issueDict['searchIssueVo.subject'])
    else:
        return CommonUtil.regMatchString(src,issueDict['searchIssueVo.subject'])and CommonUtil.regMatchString(src,issueDict['searchIssueVo.inputFrom'])

    
    '''
    @功能：     我的待办事项刷新
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
    @author:  chenhui 2015-11-25
    '''  
def myTodoIssueRefresh(username=None,password=None):
    param=copy.deepcopy(woDeDaiBanLieBiao)
    response=pinganjianshe_get(url='/issues/issueManage/findMyNeedDo.action', param=param, username=username, password=password)
    return response

    '''
    @功能：     删除测试自动化省下的所有待办、已办结事项
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
    @author:  chenhui 2015-11-25
    '''    
def deleteAllIssues():
    try:
        #删除下辖待办事项
        Log.LogOutput(message='正在清空所有事件数据...')
        issueList = copy.deepcopy(xiaXiaDaiBanLieBiao)
        issueList['keyId']= orgInit['DftShengOrgId']
        response = pinganjianshe_get(url='/issues/issueManage/findJurisdictionsNeedDoList.action', param=issueList,username=userInit['DftShengUser'],password='11111111')
        responseDict = json.loads(response.text)
        if responseDict['records'] == 0:
            Log.LogOutput(LogLevel.DEBUG, '<-----下辖待办列表已无事件,无需删除------>')
        else:
            for dictListItem in responseDict['rows']:
                deleteDict = {'deleteIds':dictListItem['issueId']}
                response=pinganjianshe_get(url='/issues/issueManage/deleteIssuess.action',param=deleteDict)
                if response.result is True:
                    Log.LogOutput(LogLevel.INFO, '******下辖待办列表删除事件成功******')
                else:
                    Log.LogOutput(LogLevel.ERROR, '!!!!!!下辖待办列表删除事件失败!!!!!!')   
        #删除下辖已办结事件列表
        issueList2 = copy.deepcopy(xiaXiaYiBanJieLieBiao)
        issueList2['keyid']= orgInit['DftShengOrgId']
        response2 = pinganjianshe_get(url='/issues/issueManage/findJurisdictionsDoneList.action', param=issueList,username=userInit['DftShengUser'],password='11111111')
        responseDict2 = json.loads(response2.text)
        if responseDict2['records'] == 0:
            Log.LogOutput(LogLevel.DEBUG, '------下辖已办结列表已无事件,无需删除------')
        else:
            for dictListItem2 in responseDict2['rows']:
                deleteDict2 = {'deleteIds':dictListItem2['issueId']}
                response2=pinganjianshe_get(url='/issues/issueManage/deleteIssuess.action',param=deleteDict2)
                if response2.result is True:
                    Log.LogOutput(LogLevel.INFO, '******下辖已办结列表删除事件成功******')
                else:
                    Log.LogOutput(LogLevel.ERROR, '!!!!!!下辖已办结列表删除失败!!!!!!')    
    except Exception :
        Log.LogOutput(LogLevel.ERROR, '事件删除失败')
        return False 

def deleteAllIssues2():
    try:
        #删除下辖待办事项
        Log.LogOutput(message='正在清空所有事件数据...')
        issueList = copy.deepcopy(xiaXiaDaiBanLieBiao)
        issueList['keyId']= orgInit['DftShengOrgId']
        response = pinganjianshe_get(url='/issues/issueManage/findJurisdictionsNeedDoList.action', param=issueList,username=userInit['DftShengUser'],password='11111111')
        responseDict = json.loads(response.text)
        if responseDict['records'] == 0:
            Log.LogOutput(LogLevel.DEBUG, '<-----下辖待办列表已无事件,无需删除------>')
        else:
            #存储所有事件ID
            arr=[]
            i=0
            for dictListItem in responseDict['rows']:
                arr.append(str(dictListItem['issueId']))
            #先判断该事件是否被锁定，如果锁定，则先解锁
                if  isDocked(para={'keyId':dictListItem['issueId']}) is True:
                    #解锁
                    unDocked(para={'issue.id':dictListItem['issueId']})
                    i=i+1
            #将所有数组中的事件ID转化为字符串参数值，以，隔开
            deleteDict = {'deleteIds':','.join(arr)}
            response=pinganjianshe_get(url='/issues/issueManage/deleteIssuess.action',param=deleteDict)
            if response.result is True:
                Log.LogOutput(LogLevel.INFO, '******下辖待办列表删除事件成功******')
            else:
                Log.LogOutput(LogLevel.ERROR, '!!!!!!下辖待办列表删除事件失败!!!!!!') 
                raise Exception('下辖待办列表删除失败')
        #删除下辖已办结事件列表
        issueList2 = copy.deepcopy(xiaXiaYiBanJieLieBiao)
        issueList2['keyid']= orgInit['DftShengOrgId']
        response2 = pinganjianshe_get(url='/issues/issueManage/findJurisdictionsDoneList.action', param=issueList,username=userInit['DftShengUser'],password='11111111')
        responseDict2 = json.loads(response2.text)
        if responseDict2['records'] == 0:
            Log.LogOutput(LogLevel.DEBUG, '------下辖已办结列表已无事件,无需删除------')
        else:
            arr2=[]
            for dictListItem2 in responseDict2['rows']:
                arr2.append(str(dictListItem2['issueId']))
        #将所有数组中的事件ID转化为字符串参数值，以，隔开
        
            deleteDict2 = {'deleteIds':','.join(arr2)}
            response2=pinganjianshe_get(url='/issues/issueManage/deleteIssuess.action',param=deleteDict2)
            if response2.result is True:
                Log.LogOutput(LogLevel.INFO, '******下辖已办结列表删除事件成功******')
            else:
                Log.LogOutput(LogLevel.ERROR, '!!!!!!下辖已办结列表删除失败!!!!!!')
                raise Exception('下辖已办结列表删除失败')
    except Exception :
        Log.LogOutput(LogLevel.ERROR, '事件删除异常')
        raise Exception('下辖已办结列表删除失败')
        return False 
                  

    '''
    @功能：     事件督办并验证
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
    @author:  chenhui 2015-11-25
    '''  
def superviseIssue(issueDict,username=None,password=None):
    #督办前加入延时等待，解决督办列表中检查fail的问题
    time.sleep(1)
    response = dealIssue(issueDict,username=username,password=password)#pinganjianshe_get(url='/issues/issueManage/dealIssue.action', param=issueDict,username=username,password=password)
#     print response.text
    if response.result is True:
        Log.LogOutput(message='正在进行督办验证')
#定义督办列表参数        
        superviseIssuesPara=copy.deepcopy(superviseIssueListPara)
        superviseIssuesPara['issueVO.createOrg.id']=orgInit['DftShengOrgId']
        superviseIssuesPara['supervisePageType']='notDoneSupervise'
#省级用户登录，查看督办列表
        rs=pinganjianshe_get(url='/issues/issueManage/findSuperviseIssues.action', param=superviseIssuesPara,username=userInit['DftShengUser'],password='11111111')
#         print rs.text
        if rs.result is True:
            responseDict = json.loads(rs.text)
            superviseIssueList=responseDict['rows']
            checkPara=copy.deepcopy(superviseIssueCheckPara)
            checkPara['issueId']=issueDict['operation.issue.id']
            checkPara['userName']=issueDict['operation.dealUserName']
            if issueDict['dealCode']=='86':#红牌
                checkPara['supervisionState']=200
                if CommonUtil.findDictInDictlist(checkPara, superviseIssueList) is True:
                    Log.LogOutput(message='红牌督办成功')
                    return True
                else:
                    Log.LogOutput(message="红牌督办失败")
                    return False
            if issueDict['dealCode']=='83':#黄牌
                checkPara['supervisionState']=100
                if CommonUtil.findDictInDictlist(checkPara, superviseIssueList) is True:
                    Log.LogOutput(message='黄牌督办成功')
                    return True
                else:
                    Log.LogOutput(message="黄牌督办失败")
                    return False
            if issueDict['dealCode']=='81':#普通
                checkPara['supervisionState']=1
                if CommonUtil.findDictInDictlist(checkPara, superviseIssueList) is True:
                    Log.LogOutput(message='普通督办成功')
                    return True
                else:
                    Log.LogOutput(message="普通督办失败")
                    return False
            if issueDict['dealCode']=='88':#取消
                checkPara['supervisionState']=-1
                if CommonUtil.findDictInDictlist(checkPara, superviseIssueList) is True:
                    Log.LogOutput(message='取消督办失败')
                    return False
                else:
                    Log.LogOutput(message="取消督办成功")
                    return True
        else:
            Log.LogOutput(message='督办/取消督办异常')        
            return False
    '''
    @功能：     事件加急并验证
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
    @author:  chenhui 2015-11-25
    '''          
def urgentIssue(issueDict,username=None,password=None):
    response = dealIssue(issueDict,username=username,password=password)#pinganjianshe_get(url='/issues/issueManage/dealIssue.action', param=issueDict,username=username,password=password)
#    print response.text
    if response.result is True:
        Log.LogOutput(message='正在进行加急验证')
        downToDoListPara=copy.deepcopy(xiaXiaDaiBanLieBiao)
        downToDoListPara['keyId']=issueDict['operation.dealOrg.id']
 
        rs = pinganjianshe_get(url='/issues/issueManage/findJurisdictionsNeedDoList.action', param=downToDoListPara,username=username,password='11111111')
#        print rs.text
        if rs.result is True:
            responseDict = json.loads(rs.text)
            responseList=responseDict['rows']
#             print responseDict
#             print responseList
#定义加急列表参数        
            checkUrgentIssue=copy.deepcopy(xiaXiaDaiBanJianCha)
            checkUrgentIssue['issueId']=issueDict['operation.issue.id']
            checkUrgentIssue['urgent']=1
            checkUrgentIssue['issueStepId']=issueDict['keyId']
            if issueDict['dealCode']=='1001':
                if CommonUtil.findDictInDictlist(checkUrgentIssue, responseList) is True:
                        Log.LogOutput(message='加急成功')
                        return True
                else:
                        Log.LogOutput(LogLevel.ERROR,message="加急失败")
                        return False
            if issueDict['dealCode']=='1011':
                if CommonUtil.findDictInDictlist(checkUrgentIssue, responseList) is False:
                        Log.LogOutput(message='取消加急成功')
                        return True
                else:
                        Log.LogOutput(message="取消加急失败")
                        return False
        else:
            Log.LogOutput(message='加急/取消加急异常')        
            return False
     
    '''
    @功能：     事件操作，包括加急、上报、交办、回退、办结、督办、领导批示、历史遗留、宣传案例等公共接口
    @para: 
    @return:    返回response对象
    @author:  chenhui 2015-11-27
    '''          
def dealIssue(issueDict,username=userInit['DftJieDaoUser'],password='11111111'):

    response = pinganjianshe_get(url='/issues/issueManage/dealIssue.action', param=issueDict,username=username,password=password)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "事件操作成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "事件操作失败")
    return response

    '''
    @功能：     事件置顶操作
    @para: 
    @return:    返回response对象
    @author:  chenhui 2015-11-27
    '''          
def topIssue(issueDict,username=None,password=None):
    response = pinganjianshe_get(url='/issues/issueManage/topNeedDoIssue.action', param=issueDict,username=username,password=password)
#     print response.text
    return response

    '''
    @功能：下辖事项待办列表
    @para: xiaXiaDaiBanLieBiao={
                     'keyId':'',
                     'seachValue':'all',
                     '_search':'false',
                     'nd':'',
                     'rows':'200',
                     'page':'1',
                     'sidx':'iu.createDate',
                     'sord':'desc'
                     }
    @return:    response
    @author:  chenhui 2015-11-27
    '''    
def downIssueToDoList(issueDict,username=None,password=None):
    response = pinganjianshe_get(url='/issues/issueManage/findJurisdictionsNeedDoList.action', param=issueDict,username=username,password=password)
#     print response.text
    return response


    '''
    @功能：检查下辖事项待办列表中是否有checkParam字典项数据
    @para: xiaXiaDaiBanLieBiao={
                     'keyId':'',
                     'seachValue':'all',
                     '_search':'false',
                     'nd':'',
                     'rows':'200',
                     'page':'1',
                     'sidx':'iu.createDate',
                     'sord':'desc'
                     }
                     checkParam：xiaXiaDaiBanJianCha
                     issueDict={'operation.dealOrg.id',}
    @return:    True or False
    @author:  chenhui 2015-11-27
    '''    
def checkDownIssueToDoList(checkParam,issueDict,username=None,password=None):
    downIssueListPara=copy.deepcopy(xiaXiaDaiBanLieBiao)
    downIssueListPara['keyId']=issueDict['operation.dealOrg.id']
    response = downIssueToDoList(issueDict=downIssueListPara,username=username,password=password)
#    print response.text
    if response.result is True:
        rsDict=json.loads(response.text)
        rsDictList1=rsDict['rows']
#        print "rsDictList1"+str(rsDictList1)
#        print checkParam
        if CommonUtil.findDictInDictlist(checkParam, rsDictList1) is True:
            Log.LogOutput(message='下辖待办事项列表存在该数据！')
            return True
#         print response.text
        return False
    else:
        Log.LogOutput(message='下辖待办事项列表接口出现异常！')
        return False


    '''
    @功能：下辖事项已办结列表
    @para: xiaXiaYiBanJieLieBiao={
                    'keyId':'',
                    '_search':'false',
                    'nd':',',
                    'rows':'200',
                    'page':'1',
                    'sidx':'createDate',
                    'sord':'desc'
                    }
    @return:    response
    @author:  chenhui 2015-11-27
    '''    
def downIssueDoneList(issueDict,username=None,password=None):
    response = pinganjianshe_get(url='/issues/issueManage/findJurisdictionsDoneList.action', param=issueDict,username=username,password=password)
#    print response.text
    return response


    '''
    @功能：检查下辖事项已办结列表中是否有checkParam字典项数据
    @para: xiaXiaDaiBanLieBiao={
                     'keyId':'',
                     'seachValue':'all',
                     '_search':'false',
                     'nd':'',
                     'rows':'200',
                     'page':'1',
                     'sidx':'iu.createDate',
                     'sord':'desc'
                     }
                     checkParam：xiaXiaYiBanJieLieBiao
                     
    @return:    True or False
    @author:  chenhui 2015-11-27
    '''    
def checkDownIssueDoneList(checkParam,issueDict,username=None,password=None):
    #下辖待办列表发送参数
    downIssueListPara=copy.deepcopy(xiaXiaDaiBanLieBiao)
    downIssueListPara['keyId']=issueDict['operation.dealOrg.id']
    response = downIssueDoneList(issueDict=downIssueListPara,username=username,password=password)
    if response.result is True:
        rsDict=json.loads(response.text)
        rsDictList1=rsDict['rows']
        if CommonUtil.findDictInDictlist(checkParam, rsDictList1) is True:
            Log.LogOutput(message='下辖已办结事项列表存在该数据！')
            return True
#    print response.text
        return False
    else:
        Log.LogOutput(message='下辖已办结事项列表接口出现异常！')
        return False
    
    
'''
    @功能：验证宣传案例功能
    @para: issueDict={'keyId':None} 事件ID               
    @return:    true false
    @author:  chenhui 2015-12-7
''' 
def checkPublicCase(mode=None,checkPara=None,issueDict=None,username=userInit['DftJieDaoUser'],password='11111111'):
    try:
        if mode=='set':#设置宣传案例
            Log.LogOutput(message='正在验证设置宣传案例功能...')
            response=setPublicCase(issueDict=issueDict,username=username,password=password)
#            Log.LogOutput(LogLevel.DEBUG,response.text)
            if response.result is True:
                #宣传案例页面可以找到，true
                check1=findPublicIssueBySub(checkParam=checkPara, username=username, password=password)          
                if check1 is True:
                    return True
                else:
                    return False
            else:
                return False
        if mode=='cancel':#取消宣传案例
            Log.LogOutput(message='正在验证取消宣传案例功能')
            response=calPublicCase(issueDict=issueDict,username=username,password=password)
#            Log.LogOutput(LogLevel.DEBUG,response.text)
            if response.result is True:
                #宣传案例页面不显示
                check1=findPublicIssueBySub(checkParam=checkPara, username=username, password=password)          
                if check1 is False:
                    return True 
                else:
                    return False
            else:
                return False
    except Exception ,e:
            Log.LogOutput(LogLevel.ERROR, '宣传案例验证出现异常！'+str(e))
            return False    
'''
    @功能：查看待办事件数,包括我的待办事件数和下辖待办事件数
    @para: issueDict={'keyId':None,'seachValue':None(all)}               
    @return:    待办事件数
    @author:  chenhui 2015-11-30
'''  
def getIssueToDoNum(issueDict=None,username=None,password=None):
    if issueDict is None:#我的待办事件数
        response = pinganjianshe_get(url='/issues/issueManage/getCountUpcoming.action',username=username,password=password)
    else:#下辖事件数
        response = pinganjianshe_get(url='/issues/issueManage/getJurisdictionsNeedDoCountUpcoming.action', param=issueDict,username=username,password=password)
    return response.text




    '''
    @功能：通过主题来查找”登录用户“的历史遗留页面是否存在数据，如果匹配到，则返回True，如果找不到，返回false
    @para: checkParam包含字典项'issueSubject',:事件主题名称; 用户名默认为街道            
    @return:    待办事件数
    @author:  chenhui 2015-12-7
    '''  
def findHistoricalIssueBySub(checkParam,username=userInit['DftJieDaoUser'],password='11111111'):
        if checkParam['subject'] is None:
            Log.LogOutput(message="传入参数错误，请确保传入的参数字典项带有'subject'，且不为空")
            return False
        else:
            listPara={
                    'keyId':CommonIntf.getOrgInfoByAccount(username)['orgId'],
                    'page':'1',
                    'rows':'50',
                    'sidx':'issueId',
                    'sord':'desc',
                    }
            response=pinganjianshe_get(url='/issues/issueManage/findMyHistoricalIssues.action',param=listPara,username=username,password=password)
            src=response.text
            return CommonUtil.regMatchString(src,checkParam['subject'])




'''
    @功能：通过主题来查找”登录用户“的宣传案例页面是否存在数据，如果匹配到，则返回True，如果找不到，返回false
    @para: checkParam包含字典项'issueSubject',:事件主题名称; 用户名默认为街道            
    @return:    待办事件数
    @author:  chenhui 2015-12-7
'''  
def findPublicIssueBySub(checkParam,username=userInit['DftJieDaoUser'],password='11111111'):
        if checkParam['subject'] is None:
            Log.LogOutput(message="传入参数错误，请确保传入的参数字典项带有'subject'，且不为空")
            return False
        else:
            listPara={
                    'keyId':CommonIntf.getOrgInfoByAccount(username)['orgId'],
                    'page':'1',
                    'rows':'50',
                    'sidx':'issueId',
                    'sord':'desc',
                    }
            response=pinganjianshe_get(url='/issues/issueManage/findMyPublicltyIssues.action',param=listPara,username=username,password=password)
            src=response.text
            return CommonUtil.regMatchString(src,checkParam['subject'])
                
        
'''
    @功能：通过主题来查找事件是否存在页面，如果匹配到，则返回True，如果找不到，返回false
    @para: issueDict={'orgId':None,'issueSubject:None'}  ,issueStatus:Done已办事件页面；Complete已办结页面；Todo待办事项页面            
    @return:    待办事件数
    @author:  chenhui 2015-11-30
'''  
def checkIssueBySub(issueStatus,issuePara=None,username=None,password=None):
    
    lssueList={'keyId':issuePara['orgId'],
                            'page':'1',
                            'rows':'200',
                            'sidx':'issueId',
                            'sord':'desc'}
    if issueStatus=='Done':   #我的已办事件页面
        response = pinganjianshe_get(url='/issues/issueManage/findMyDone.action',param=lssueList,username=username,password=password)
    #      response.text是个Unicode对象，需要先转化成string
        src=response.text
        return CommonUtil.regMatchString(src,issuePara['issueSubject'])
    if issueStatus=='Todo':#我的待办事件页面
        response = pinganjianshe_get(url='/issues/issueManage/findMyNeedDo.action',param=lssueList,username=username,password=password)
    #      response.text是个Unicode对象，需要先转化成string
        src=response.text
        return CommonUtil.regMatchString(src,issuePara['issueSubject'])        
    if issueStatus=='Complete':#我的已办结事件页面 
        response = pinganjianshe_get(url='/issues/issueManage/findMyCompleted.action',param=lssueList,username=username,password=password)
    #      response.text是个Unicode对象，需要先转化成string
        src=response.text
        return CommonUtil.regMatchString(src,issuePara['issueSubject'])
    else:
        Log.LogOutput(message='checkIssueBySub参数异常')
        return False   

    '''
    @功能：设置允许网格用户越级上报给街道
    @para: issueDict={'issueBypassList[0].orgId':None,'issueBypassList[0].isBypass:None'}            
    @return:    True/False
    @author:  chenhui 2015-12-2
    '''    
def setIssueByPass(issueDict,username=None,password=None):
    try:
        if issueDict['issueBypassList[0].isBypass'] is True:
            Log.LogOutput(message='正在设置允许网格用户越级上报')    
            response = pinganjianshe_get(url='/sysadmin/issueBypassManage/updateIssueBypassList.action',param=issueDict,username=username,password=password)
    #        print response.text
            if response.text=='\"true\"' :
                Log.LogOutput(message='设置越级上报成功')
                return True
            else:
                Log.LogOutput(message='设置越级上报失败')
                return False
        elif issueDict['issueBypassList[0].isBypass'] is False:
            Log.LogOutput(message='正在设置禁止网格用户越级上报')
            response = pinganjianshe_get(url='/sysadmin/issueBypassManage/updateIssueBypassList.action',param=issueDict,username=username,password=password)
    #        print response.text
            if response.text=='\"true\"':
                Log.LogOutput(message='取消越级上报成功')
                return True
            else:
                Log.LogOutput(message='取消越级上报失败')
                return False
        else:
            Log.LogOutput(message='参数错误，请检查传入参数')   
            return False
    except Exception :
            Log.LogOutput(LogLevel.ERROR, '事件设置越级上报出现异常！')
    '''
    @功能：设置宣传案例
    @para: issueDict={'keyId':None},事件ID            
    @return:    response.text
    @author:  chenhui 2015-12-7
    '''      
def setPublicCase(issueDict,username=None,password=None):
    response = pinganjianshe_get(url='/issues/issueManage/publicltyCass.action',param=issueDict,username=username,password=password)
    return response


    '''
    @功能：取消宣传案例
    @para: issueDict={'keyId':None},事件ID            
    @return:    response.text
    @author:  chenhui 2015-12-7
    '''      
def calPublicCase(issueDict,username=None,password=None):
    response = pinganjianshe_get(url='/issues/issueManage/cancelPublicltyCass.action',param=issueDict,username=username,password=password)
    return response

    '''
    @功能：回撤
    @para: issueDict={'keyId':None},事件ID            
    @return:    response.text
    @author:  chenhui 2015-12-7
    '''  
def revocationIssue(issueDict,username=userInit['DftJieDaoUser'],password='11111111'):
    response=pinganjianshe_get(url='/issues/issueManage/revocationIssue.action',param=issueDict,username=username,password=password)
    return response

    '''
    @功能：验证撤回功能
    @para: issueDict={'keyId':None},事件ID    checkPara={'issueSubject':,}         
    @return:    response.text
    @author:  chenhui 2015-12-7
    '''  
def checkRevocationIssue(dealType,checkPara,issueDict,username=userInit['DftJieDaoUser'],password='11111111'):
    try:
        Log.LogOutput(message='正在验证事件撤回功能')
        revocationIssue(issueDict=issueDict,username=username,password=password)
        if dealType=='交办':#交办
            #我的待办事件数为1
            check1=getIssueToDoNum(username=username,password=password)
            #我的已办事项中不存在指定主题的数据
            issuePara={'orgId':getOrgInfoByAccount(username),'issueSubject':checkPara['issueSubject']}
            check2=checkIssueBySub(issueStatus='Done',issuePara=issuePara,username=username,password=password)
            #交办单位的我的事件数为0
            check3=getIssueToDoNum(username=userInit['DftSheQuUser'],password=password)
            if check1 =='1' and check2 is False and check3 =='0':
                Log.LogOutput( message='交办撤回成功')
                return True
            else:
                Log.LogOutput( LogLevel.ERROR,message='交办撤回失败')
                return False
        if dealType=='上报':#上报
            #我的待办事件数为1
            check1=getIssueToDoNum(username=username,password=password)
            #我的已办事项中不存在指定主题的数据
            issuePara={'orgId':getOrgInfoByAccount(username),'issueSubject':checkPara['issueSubject']}
            check2=checkIssueBySub(issueStatus='Done',issuePara=issuePara,username=username,password=password)
            #上报单位的我的事件数为0
            check3=getIssueToDoNum(username=userInit['DftQuUser'],password=password)
            
            if check1 =='1' and check2 is False and check3 =='0':
                Log.LogOutput( message='上报撤回成功')
                return True
            else:
                Log.LogOutput( LogLevel.ERROR,message='上报撤回失败')
                return False
    except Exception :
            Log.LogOutput(LogLevel.ERROR, '事件撤回操作验证出现异常！')
            
    '''
    @功能：验证回撤功能
    @para: issueDict={'keyId':None},事件ID    
    @return:    response
    @author:  chenhui 2015-12-8
    '''  
def addIssueOrg(issueDict,username=userInit['DftJieDaoUser'],password='11111111'):
    response=pinganjianshe_get(url='/issues/issueManage/validataAdditionalSpecialAssign.action',param=issueDict,username=username,password=password)   
    return response

    '''
    @功能：验证设置历史遗留功能
    @para: issueDict   
    @return:    true/false
    @author:  chenhui 2015-12-8
    '''   
def checkSetHistory(checkParam=None,username=userInit['DftJieDaoUser'],password='11111111'):
    try:
        #历史遗留页面有数据
        check1=findHistoricalIssueBySub(checkParam=checkParam,username=username,password=password)
        #我的事项中无数据，0
        check2=getIssueToDoNum(username=username,password=password)
        #下辖待办事件数为1
        issueDict2={
                    'keyId':orgInit['DftJieDaoOrgId'],
                    'seachValue':'all'
                    }           
        check3=getIssueToDoNum(issueDict=issueDict2,username=username,password=password)
        if check1 is True and check2 =='0' and check3=='1':                            
                return True
        else:
                return False
    except Exception :
            Log.LogOutput(LogLevel.ERROR, '事件设置历史遗留验证出现异常！')
            
    '''
    @功能：验证取消历史遗留功能
    @para: issueDict   
    @return:    True/False
    @author:  chenhui 2015-12-8
    '''  
def checkCancelHistoryIssue(checkParam=None,username=userInit['DftJieDaoUser'],password='11111111'):
    try:
        #历史遗留页面无数据
        check1=findHistoricalIssueBySub(checkParam=checkParam,username=username,password=password)
        #我的待办事件数为1
        check2=getIssueToDoNum(username=username,password=password)
        
        if check1 is False and check2 =='1':
            Log.LogOutput(message='取消历史遗留检查点验证通过')
            return True
        else:
            Log.LogOutput(message='取消历史遗留检查点验证失败')
            return False
    except Exception :
        Log.LogOutput(LogLevel.ERROR, '事件取消历史遗留功能验证出现异常！')
    '''
    @功能：验证事件处理中功能
    @para: issueDict   
    @return:True/False
    @author:  chenhui 2015-12-8
    '''  
def checkHandleIssue(checkParam,issueDict,username=userInit['DftJieDaoUser'],password='11111111'):
    try:
        #下辖待办事件存在该数据，True
        check1=checkDownIssueToDoList(checkParam=checkParam,issueDict=issueDict,username=username,password=password)    
        #我的待办事件数仍然为1    
        check2=getIssueToDoNum(username=username,password=password)
        if check1 is True and check2 =='1':
            Log.LogOutput(message='事件处理中验证通过')
            return True
        else:
            Log.LogOutput(message='事件处理中验证不通过')
            return False
    except Exception :
        Log.LogOutput(LogLevel.ERROR, '事件处理中验证出现异常！')

    '''
    @功能：验证事件结案功能
    @para: issueDict   
    @return:True/False
    @author:  chenhui 2015-12-8
    '''        
def checkCompleteIssue(checkParam,issueDict,username=userInit['DftJieDaoUser'],password='11111111'):
    try:
        #下辖已办结事件存在该数据，True
        check1=checkDownIssueDoneList(checkParam=checkParam,issueDict=issueDict,username=username,password=password)    
        #我的待办事件数为0    
        check2=getIssueToDoNum(username=username,password=password)
        if check1 is True and check2 =='0':
            Log.LogOutput(message='事件结案验证通过')
            return True
        else:
            Log.LogOutput(message='事件结案验证不通过')
            return False
    except Exception :
        Log.LogOutput(LogLevel.ERROR, '事件结案验证出现异常！')

    '''
    @功能：验证事件上报功能
    @para: issueDict   
    @return:True/False
    @author:  chenhui 2015-12-8
    '''  
def checkReportIssue(checkParam,issueDict,username=userInit['DftJieDaoUser'],password='11111111'):
    try:
        Log.LogOutput(message='事件处理上报验证中')
        #如果没有抄告
        if issueDict['tellOrgIds']=='':
            check1=checkDownIssueToDoList(checkParam=checkParam,issueDict=issueDict,username=username,password=password)
            check2=checkDownIssueToDoList(checkParam=checkParam,issueDict=issueDict,username=userInit['DftQuUser'],password=password)
            check3=getIssueToDoNum(username=username,password=password)
            check4=getIssueToDoNum(username=userInit['DftQuUser'],password=password)
            
            #街道已办事项页面存在该事件
            check5=checkIssueBySub(issueStatus='Done',issuePara={'orgId':orgInit['DftJieDaoOrgId'],'issueSubject':checkParam['subject']},username=username,password=password)
#            print check1,check2,check3,check4,check5
            if check1 is True and check2 is True and check3=='0'and check4=='1' and check5 is True:
                Log.LogOutput(message='事件普通上报验证通过！')
                return True
            else:
                Log.LogOutput(message='事件普通上报验证失败！')
                return False
            #如果有抄告对象
        if issueDict['tellOrgIds']==orgInit['DftQuFuncOrgId']:
            #街道的下辖待办事项存在数据
            check1=checkDownIssueToDoList(checkParam=checkParam,issueDict=issueDict,username=username,password=password)
            #区的下辖待办存在数据
            check2=checkDownIssueToDoList(checkParam=checkParam,issueDict=issueDict,username=userInit['DftQuUser'],password=password)
            #街道我的待处理事件数为0
            check3=getIssueToDoNum(username=username,password=password)
            #区我的待处理事件数为1
            check4=getIssueToDoNum(username=userInit['DftQuUser'],password=password)
            #街道我的已办事件中存在该事件
            check5=checkIssueBySub(issueStatus='Done',issuePara={'orgId':orgInit['DftJieDaoOrgId'],'issueSubject':checkParam['subject']},username=username,password=password)
            #区职能部门的待处理事件数为1
            check6=getIssueToDoNum(username=userInit['DftQuFuncUser'],password=password)
            #区职能部门的下辖待办列表，待阅读状态的数据不为空，dealState: 140
            checkParam['dealState']=140
            issueDict['operation.dealOrg.id']=orgInit['DftQuFuncOrgId']
            check7=checkDownIssueToDoList(checkParam=checkParam,issueDict=issueDict,username=userInit['DftQuUser'],password=password)
        #               print check7
            if check1 is True and check2 is True and check3=='0'and check4=='1' and check5 is True and check6=='1' and check7 is True:
                Log.LogOutput(message='事件上报并抄告验证通过！')
                return True
            else:
                Log.LogOutput(message='事件上报并抄告验证失败！')
                return False
    except Exception :
        Log.LogOutput(LogLevel.ERROR, '事件上报验证出现异常！')

    '''
    @功能：验证事件阅读功能
    @para: issueDict   
    @return:True/False
    @author:  chenhui 2015-12-8
    '''  
def checkReadIssue(checkParam,issueDict,username=userInit['DftJieDaoUser'],password='11111111'):
    try:
        Log.LogOutput(message='正在验证阅读事件功能...')
        if issueDict['operation.dealOrg.id']==orgInit['DftQuFuncOrgId']:#上报到区职能部门阅读
            Log.LogOutput(message='街道上报到区职能部门阅读验证中')
            #区职能部门下辖待办事项中没有该事件
            check1=checkDownIssueToDoList(checkParam=checkParam,issueDict=issueDict,username=username,password=password)
            #区职能部门中我的待办事件数为0                
            check2=getIssueToDoNum(username=username,password=password)
            #区行政部门中我的待办事件数仍然为1，不受影响
            check3=getIssueToDoNum(username=userInit['DftQuUser'],password=password)
            #区职能部门中我的已办事项存在该事件
            check4=checkIssueBySub(issueStatus='Done',issuePara={'orgId':orgInit['DftQuFuncOrgId'],'issueSubject':checkParam['subject']},username=username,password=password)
            
            if  check1 is False and check2=='0'and check3=='1' and check4 is True:
                Log.LogOutput(message='事件阅读验证成功！')
                return True
            else:
                Log.LogOutput(level=LogLevel.ERROR,message='事件阅读验证失败！')
                return False
        if issueDict['operation.dealOrg.id']==orgInit['DftJieDaoFuncOrgId']:#交办到街道职能部门阅读
            Log.LogOutput(message='事件处理交办到街道职能部门阅读验证中')
            #街道职能部门我待办事项数据为0
            check1=getIssueToDoNum(username=username,password=password)
            #街道职能部门我的已办事项中存在数据
            check2=checkIssueBySub(issueStatus='Done',issuePara={'orgId':orgInit['DftJieDaoFuncOrgId'],'issueSubject':checkParam['subject']},username=username,password=password)
            if check1 =='0'and check2 is True:
                Log.LogOutput(message='事件阅读验证成功！')
                return True
            else:
                Log.LogOutput(level=LogLevel.ERROR,message='事件阅读验证失败！')
                return False
        else:
            Log.LogOutput(level=LogLevel.ERROR,message='验证没有执行，请检查传入参数！')
            return False
    except Exception :
        Log.LogOutput(LogLevel.ERROR, '事件阅读验证出现异常！')
        
    '''
    @功能：验证事件追加功能
    @para: issueDict   
    @return:True/False
    @author:  chenhui 2015-12-8
    '''  
def checkAddOrg(username=userInit['DftJieDaoUser'],password='11111111'):
    try:
        Log.LogOutput( message='正在验证追加部门功能')
        #执行追加操作对当前街道层级没有影响，街道层级待办事项为0
        check1=getIssueToDoNum(username=username,password=password)
        #原协办的街道职能部门的待办事件数仍然为1
        check2=getIssueToDoNum(username=userInit['DftJieDaoFuncUser'],password=password)
        #新追加的协办职能部门待办事件数也为1
        check3=getIssueToDoNum(username=userInit['DftJieDaoFuncUser1'],password=password)
        if check1 =='0' and check2=='1' and check3=='1':
            Log.LogOutput(message='追加部门验证通过！')
            return True
        else:
            Log.LogOutput(LogLevel.ERROR, '追加部门验证失败！')
            return False
    except Exception :
            Log.LogOutput(LogLevel.ERROR, '事件追加部门验证出现异常！')
    '''
    @功能：验证事件受理功能
    @para: issueDict   
    @return:True/False
    @author:  chenhui 2015-12-10
    '''  
def checkAcceptIssue(checkParam,issueDict,username=userInit['DftJieDaoUser'],password='11111111'):
    try:
        Log.LogOutput(message='事件处理受理功能验证中')
        #区待办事件数不变，还是1
        check1=getIssueToDoNum(username=username,password=password)
        #区下辖待办事项列表存在该数据，事件状态为处理中，dealState: 120
        check2=checkDownIssueToDoList(checkParam=checkParam,issueDict=issueDict,username=username,password=password)          
        #街道上报给区受理验证
        if    check1=='1'and check2 is True and username==userInit['DftQuUser']:            
            Log.LogOutput(message='街道上报给区受理验证通过')
            return True
        if check1=='1'and check2 is False and username==userInit['DftSheQuUser']:
            Log.LogOutput(message='街道交办给社区受理验证通过')
            return True
        else:
            Log.LogOutput(LogLevel.ERROR,message='事件受理验证失败！')
            return False
    except Exception :
            Log.LogOutput(LogLevel.ERROR, '事件受理验证出现异常！')
            
    '''
    @功能：验证事件回退功能
    @para: issueDict   
    @return:True/False
    @author:  chenhui 2015-12-11
    '''  
def checkBackIssue(checkParam,issueDict,username=userInit['DftJieDaoUser'],password='11111111'):
    try:
        Log.LogOutput(message='事件处理回退验证中')
        #区部门我的待办事件数变为0
        check1=getIssueToDoNum(username=username,password=password)
        #区部门我的已办事项存在该事件
        check2=checkIssueBySub(issueStatus='Done',issuePara={'orgId':orgInit['DftQuOrgId'],'issueSubject':checkParam['subject']},username=username,password=password)
        #街道我的待办事件数为1
        check3=getIssueToDoNum(username=userInit['DftJieDaoUser'],password=password) 
        #街道下辖待办事项中存在改事件，状态为110，待受理
        check4=checkDownIssueToDoList(checkParam=checkParam,issueDict=issueDict,username=userInit['DftJieDaoUser'],password=password)

        if check1=='0'and check2 is True and check3=='1'and check4 is True:
            Log.LogOutput(message='回退检查点验证通过')
            return True
        else:
            Log.LogOutput(LogLevel.ERROR,message='回退检查点验证失败')
            return False
    except Exception :
            Log.LogOutput(LogLevel.ERROR, '事件回退验证出现异常！')
            

    '''
    @功能：验证事件越级上报功能
    @para: issueDict   
    @return:True/False
    @author:  chenhui 2015-12-11
    '''  
def checkBypassIssue(checkParam,issueDict,username=userInit['DftJieDaoUser'],password='11111111'):
    try:
        Log.LogOutput(message='事件越级上报功能验证中')
        #网格部门我的待办事件数变为0
        check1=getIssueToDoNum(username=userInit['DftWangGeUser'],password=password)
        #网格部门我的已办事项存在该事件
        check2=checkIssueBySub(issueStatus='Done',issuePara={'orgId':orgInit['DftWangGeOrgId'],'issueSubject':checkParam['subject']},username=userInit['DftWangGeUser'],password=password)
        #街道我的待办事件数为1
        check3=getIssueToDoNum(username=userInit['DftJieDaoUser'],password=password) 
        #街道下辖待办事项中存在改事件，状态为110，待受理
        check4=checkDownIssueToDoList(checkParam=checkParam,issueDict=issueDict,username=userInit['DftJieDaoUser'],password=password)

        if check1=='0'and check2 is True and check3=='1'and check4 is True:
            Log.LogOutput(message='越级上报检查点验证通过')
            return True
        else:
            Log.LogOutput(LogLevel.ERROR,message='越级上报检查点验证失败')
            return False
    except Exception ,e:
            
            Log.LogOutput(LogLevel.ERROR, '事件越级上报验证出现异常！'+str(e))
            
 
    '''
    @功能：验证事件交办功能
    @para: issueDict ，checkParam  
    @return:True/False
    @author:  chenhui 2015-12-11
    '''  
def checkAssignIssue(checkParam,issueDict,username=userInit['DftJieDaoUser'],password='11111111'):           
    try:
        if issueDict['tellOrgIds']==''and issueDict['specialAssignType']=='':
            Log.LogOutput(message='事件处理普通交办无抄告验证中')
            #街道我的待办事件数变为0
            check1=getIssueToDoNum(username=username,password=password)
            #街道我的已办事件存在数据
            check2=checkIssueBySub(issueStatus='Done',issuePara={'orgId':orgInit['DftJieDaoOrgId'],'issueSubject':checkParam['subject']},username=username,password=password)
            #社区我的待办事件数为1
            check3=getIssueToDoNum(username=userInit['DftSheQuUser'],password=password)
            #街道下辖待办事项列表存在数据，状态为110，待受理状态
            check4=checkDownIssueToDoList(checkParam=checkParam,issueDict=issueDict,username=userInit['DftJieDaoUser'],password=password)
#                print check4
            if check1=='0'and check2 is True and check3=='1' and check4 is True:
                Log.LogOutput(message='普通交办功能验证通过')
                return True
            else:
                Log.LogOutput(LogLevel.ERROR,message='普通交办功能验证失败')
                return False
                #普通交办并抄告
        if issueDict['tellOrgIds']==orgInit['DftJieDaoFuncOrgId'] and issueDict['specialAssignType']=='':
            Log.LogOutput(message='事件处理普通交办并抄告验证中')
            #街道我的待办事件数变为0
            check1=getIssueToDoNum(username=username,password=password)
            #街道我的已办事件存在数据
            check2=checkIssueBySub(issueStatus='Done',issuePara={'orgId':orgInit['DftJieDaoOrgId'],'issueSubject':checkParam['subject']},username=username,password=password)
            #社区我的待办事件数为1
            check3=getIssueToDoNum(username=userInit['DftSheQuUser'],password=password)
            #社区下辖待办事项列表存在数据，状态为110，待受理状态
            check4=checkDownIssueToDoList(checkParam=checkParam,issueDict=issueDict,username=userInit['DftSheQuUser'],password=password)
            #被抄告的街道职能部门我的待办事件数为1
            check5=getIssueToDoNum(username=userInit['DftJieDaoFuncUser'],password=password)
            #被抄告的街道职能部门下辖待办事项存在数据，状态为140，待阅读
            checkParam['dealState']=140
            #复制参数，防止对原参数造成影响，同时设置为街道职能部门的下辖事项
            issueDict2=copy.deepcopy(issueDict)
            issueDict2['operation.dealOrg.id']=orgInit['DftJieDaoFuncOrgId']#下辖组织机构选择街道职能部门
            check6=checkDownIssueToDoList(checkParam=checkParam,issueDict=issueDict2,username=userInit['DftJieDaoFuncUser'],password=password)
            
            if check1=='0'and check2 is True and check3=='1' and check4 is True and check5=='1' and check6 is True:
                Log.LogOutput(message='普通交办并抄告功能验证通过')
                return True
            else:
                Log.LogOutput(LogLevel.ERROR,message='普通交办并抄告功能验证失败')
                return False
    except Exception,e :
        Log.LogOutput(LogLevel.ERROR, '事件普通交办验证出现异常！'+str(e))       
            
            
    '''
    @功能：验证事件共同办理功能
    @para: issueDict   checkParam
    @return:True/False
    @author:  chenhui 2015-12-13
    '''  
def checkCommonHandelIssue(checkParam,issueDict,username=userInit['DftJieDaoUser'],password='11111111'):
    try:
        Log.LogOutput(message='事件处理共同办理验证中')
        #街道我的待办事件数为0
        check1=getIssueToDoNum(username=username,password=password)
        #街道我的下辖待办事项不为空，状态为110，待受理
        check2=checkDownIssueToDoList(checkParam=checkParam,issueDict=issueDict,username=username,password=password)
        #街道已办事件中存在数据,true
        check3=checkIssueBySub(issueStatus='Done',issuePara={'orgId':orgInit['DftJieDaoOrgId'],'issueSubject':checkParam['subject']},username=username,password=password)
        #社区我的待办事件数为1
        check4=getIssueToDoNum(username=userInit['DftSheQuUser'],password=password)
        
        if check1=='0' and check2 is True and check3 is True and check4 =='1' :
            Log.LogOutput(message='共同办理功能验证通过')
            return True
        else:
            Log.LogOutput(LogLevel.ERROR,message='共同办理功能验证失败')
            return False
    except Exception,e :
        Log.LogOutput(LogLevel.ERROR, '事件共同办理验证出现异常！'+str(e))
        
        
        
    '''
    @功能：验证事件回复功能
    @para: issueDict   checkParam
    @return:True/False
    @author:  chenhui 2015-12-13
    '''  
def checkReplyIssue(checkParam,issueDict,username=userInit['DftJieDaoUser'],password='11111111'):
    try:
        Log.LogOutput(message='事件处理共同办理回复验证中')
        #社区我的待办事件数为0
        check1=getIssueToDoNum(username=username,password=password)
        #社区我的已办事项数据不为空,true
        check2=checkIssueBySub(issueStatus='Done',issuePara={'orgId':orgInit['DftSheQuOrgId'],'issueSubject':checkParam['subject']},username=username,password=password)
        #街道我的事项待办事件数为1
        check3=getIssueToDoNum(username=userInit['DftJieDaoUser'],password=password)
        #街道下辖事项列表存在数据，状态为待受理，dealState 110，true
        issueDict['operation.dealOrg.id']=orgInit['DftJieDaoOrgId']#查找街道下辖事件
        check4=checkDownIssueToDoList(checkParam=checkParam,issueDict=issueDict,username=userInit['DftJieDaoUser'],password=password)
    
        if check1=='0' and check2 is True and check3=='1' and check4 is True:
                Log.LogOutput(message='共同办理回复验证通过')
                return True
        else:
                Log.LogOutput(LogLevel.ERROR,'共同办理回复验证失败')
    except Exception,e :
        Log.LogOutput(LogLevel.ERROR, '事件回复验证出现异常！'+str(e)) 


    '''
    @功能：验证事件协同办理功能
    @para: issueDict   checkParam
    @return:True/False
    @author:  chenhui 2015-12-13
    '''  
def checkCooperateIssue(checkParam,issueDict,username=userInit['DftJieDaoUser'],password='11111111'):
    try:
        Log.LogOutput(message='事件处理协同办理验证中')
        #街道我的待办事件数为0
        check1=getIssueToDoNum(username=username,password=password)
        #街道我的下辖待办事项不为空，状态为110，待受理
        check2=checkDownIssueToDoList(checkParam=checkParam,issueDict=issueDict,username=username,password=password)
        #街道已办事件中存在数据,true
        check3=checkIssueBySub(issueStatus='Done',issuePara={'orgId':orgInit['DftJieDaoOrgId'],'issueSubject':checkParam['subject']},username=username,password=password)
        #街道职能部门的下辖待办事项页面存在数据，状态为110，待受理
        check4=checkDownIssueToDoList(checkParam=checkParam,issueDict=issueDict,username=userInit['DftJieDaoFuncUser'],password=password)
        #街道职能部门我的待办事件数为1
        check5=getIssueToDoNum(username=userInit['DftJieDaoFuncUser'],password=password)
        #社区行政部门我的待办事件数为1
        check6=getIssueToDoNum(username=userInit['DftSheQuUser'],password=password)                                   
              
        if check1=='0' and check2 is True and check3 is True and check4 is True and check5 =='1' and check6=='1': 
            Log.LogOutput(message='协同办理功能验证通过')
            return True
        else:
            Log.LogOutput(LogLevel.ERROR,'协同办理功能验证失败')
            return False
    except Exception,e :
        Log.LogOutput(LogLevel.ERROR, '事件协同办理验证出现异常！'+str(e))
        
        
    '''
    @功能：评价事件
    @para: issueDict=issueEvaluateParam
    @return:response.text
    @author:  chenhui 2015-12-13
    '''  
def evaluateIssue(issueDict,username=userInit['DftJieDaoUser'],password='11111111'):
    Log.LogOutput(level=LogLevel.INFO, message='评价事件')
    response = pinganjianshe_post(url='/issues/issueManage/issueEvaluate.action', postdata=issueDict, username=username, password=password)
    
    if response.result is True:
        Log.LogOutput(message='评价事件成功！')
        Log.LogOutput(LogLevel.DEBUG,response.text)
        return response
    else:
        Log.LogOutput(level=LogLevel.DEBUG,message='评价事件失败！'+response.text)      
        return response   
    
    
'''
    @功能：通过主题来查找”登录用户“的4个报表统计页面，如果匹配到，则返回True，如果找不到，返回false
    @para: checkParam包含字典项'issueSubject',:事件主题名称; 用户名默认为街道 checkParam={issueTypeName,subject}           
    @return:    true/false
    @author:  chenhui 2015-12-14
'''  
def findMyTypeIssueBySub(checkParam,username=userInit['DftJieDaoUser'],password='11111111'):
    if checkParam['subject'] is None or checkParam['issueTypeName'] is None:
        Log.LogOutput(message="传入参数错误，请确保传入的参数字典项带有'subject'，且不为空")
        return False
    
    listPara=copy.deepcopy(bbtjPara)
    listPara['orgId']=CommonIntf.getOrgInfoByAccount(username)['orgId']
    listPara['requestType']='mine'
    if  checkParam['issueTypeName']=='矛盾纠纷': 
        listPara['searchTestIndividuallyVo.issueTypeDomainName']=checkParam['issueTypeName'] 
        response=pinganjianshe_get(url='/testIndividually/searchTestIndividuallyManageNew/searchTestIndividually.action',param=listPara,username=username,password=password)
        
    if  checkParam['issueTypeName']=='治安、安全隐患':
        listPara['searchSecuritytroubleVo.issueTypeDomainName']=checkParam['issueTypeName']
        response=pinganjianshe_get(url='/issue/searchIssueSecuritytroubleManage/searchIssueSecuritytrouble.action',param=listPara,username=username,password=password)
    
    if  checkParam['issueTypeName']=='民生服务':
        listPara['searchPeopleLiveServiceVo.issueTypeDomainName']=checkParam['issueTypeName']
        response=pinganjianshe_get(url='/peopleLiveService/searchPeopleLiveServiceManage/searchPeopleLiveService.action',param=listPara,username=username,password=password)
    
    if  checkParam['issueTypeName']=='其他':
        listPara['searchOtherTypeVo.issueTypeDomainName']=checkParam['issueTypeName']
        response=pinganjianshe_get(url='/issueOtherType/searchOtherTypeManage/searchOtherType.action',param=listPara,username=username,password=password)
    
    src=response.text#.encode("utf-8")
    return CommonUtil.regMatchString(src,checkParam['subject'])
    
'''
    @功能：新增事件限时办结规则
    @para:           
    @return:    response
    @author:  chenhui 2015-12-15
'''  
def addIssueCompleteLimitConfig(issueDict,username=userInit['DftJieDaoUser'],password='11111111'):
    Log.LogOutput( message='新增限时办结规则')
    response=pinganjianshe_get(url='/issue/issueCompleteLimitConfigManage/addIssueCompleteLimitConfig.action',param=issueDict,username=username,password=password)
    return response

'''
    @功能：检查限时办结-全部事项列表中是否存在交办的事件
    @para:           
    @return:    true/false
    @author:  chenhui 2015-12-16
'''  
def checkIssueCompleteLimitList(checkPara,issueDict,username=userInit['DftJieDaoUser'],password='11111111'):
    try:
        Log.LogOutput( message='正在验证限时办结列表中是否存在交办的事件')
        response=pinganjianshe_get(url='/issues/issueCompleteLimitManage/findMyAllIssues.action',param=issueDict,username=username,password=password)
        if response.result is False:
            Log.LogOutput(LogLevel.ERROR,'请求结果异常，请检查输入参数')
            return False
        responseDict = json.loads(response.text)
#        Log.LogOutput(level=LogLevel.DEBUG, message=responseDict)
        if responseDict['records']=='0':
            Log.LogOutput(LogLevel.DEBUG,'列表数据为空！')
            return False
        else:
            listDict = responseDict['rows']
            if CommonUtil.findDictInDictlist(checkPara, listDict) is True:
                Log.LogOutput(message='列表有数据，并且查找数据成功')
                return True
            else:
                Log.LogOutput(message="列表有数据，但是查找数据失败")
                return False
    except Exception,e :
        Log.LogOutput(LogLevel.ERROR, '限时办结列表验证出现异常！'+str(e))    
        return response
    
    
'''
    @功能：新增事件延时申请
    @para:           
    @return:    response
    @author:  chenhui 2015-12-17
'''  
def applyIssueDelay(issueDict,username=userInit['DftJieDaoUser'],password='11111111'):
    Log.LogOutput( message='正在申请延时办结')
    response=pinganjianshe_get(url='/issues/issueCompleteDelayManage/addIssueCompleteDelay.action',param=issueDict,username=username,password=password)
#     Log.LogOutput(LogLevel.DEBUG,response.text)
    return response

'''
    @功能：检查限时办结-延时设置列表中是否存在申请延时的事件
    @para:           
    @return:    true/false
    @author:  chenhui 2015-12-17
'''  
def checkIssueDelayApply(checkPara,issueDict,username=userInit['DftJieDaoUser'],password='11111111'):
    try:
        Log.LogOutput( message='正在验证限期办结-延时设置列表中是否存在申请延时的事件')
        response=pinganjianshe_get(url='/issues/issueCompleteLimitManage/findDelayAllIssues.action',param=issueDict,username=username,password=password)
        if response.result is False:
            Log.LogOutput(LogLevel.ERROR,'请求结果异常，请检查输入参数')
            return False
        responseDict = json.loads(response.text)
#         Log.LogOutput(level=LogLevel.DEBUG, message=responseDict)
        if responseDict['records']=='0':
            Log.LogOutput(LogLevel.DEBUG,'列表数据为空！')
            return False
        else:
            listDict = responseDict['rows']
            if CommonUtil.findDictInDictlist(checkPara, listDict) is True:
                Log.LogOutput(message='列表有数据，并且查找数据成功')
                return True
            else:
                Log.LogOutput(message="列表有数据，但是查找数据失败")
                return False
    except Exception,e :
        Log.LogOutput(LogLevel.ERROR, '限时办结列表验证出现异常！'+str(e))    
        return False
    
    
'''
    @功能：设置延时
    @para:           
    @return:    response
    @author:  chenhui 2015-12-17
'''  
def setDelay(issueDict,username=userInit['DftJieDaoUser'],password='11111111'):
    Log.LogOutput( message='正在设置允许的延时时间')
    response=pinganjianshe_get(url='/issues/issueCompleteDelayManage/setDelay.action',param=issueDict,username=username,password=password)
    return response

'''
    @功能：新增工作简报
    @para:           
    @return:    response
    @author:  chenhui 2015-12-17
'''  
def addWorkBulletin(workParam,username=userInit['DftJieDaoUser'],password='11111111'):
    print workParam
    Log.LogOutput( message='正在新增工作简报')
    response=pinganjianshe_get(url='/baseinfo/workBulletinManage/addWorkBulletin.action',param=workParam,username=username,password=password)
    Log.LogOutput(LogLevel.DEBUG,response.text)
    return response



'''
    @功能：导出下辖全部事项
    @para:           
    @return:    response
    @author:  chenhui 2015-12-18
'''  
def dlIssue(issueDict,username=userInit['DftJieDaoUser'],password='11111111'):
    Log.LogOutput( message='正在导出全部事项...')
    #查询后导出接口
    if issueDict.has_key('searchIssueVo.targeOrgId'):
        response=pinganjianshe_post(url='/issues/issueManage/downloadSearchJurisdictionsAllIssues.action',postdata=issueDict,username=username,password=password)
    #直接导出接口
    else:
        response=pinganjianshe_post(url='/issues/issueManage/downJurisdictionsAllIssues.action',postdata=issueDict,username=username,password=password)
#        print response.text
    path='C:/autotest_file/downAllIssuesExportSheet.xls'
#    path2=u'C:/autotest_file/下辖全部事项导出清单2.xls'
    with open(path,'wb') as code:
            code.write(response.content)
    return response



'''
    @功能：检查下辖事项-全部事项列表导出的数据单元格内容是否正确
    @para:           
    @return:    true/false
    @author:  chenhui 2015-12-17
'''  
def checkDlIssueList(checkPara,username=userInit['DftJieDaoUser'],password='11111111'):
    try:
#         check1=checkExcelCellValue(checkPara['serialNumber'][0],u'下辖全部事项导出清单.xls', u'下辖事项清单','A4')
#         check2=checkExcelCellValue(checkPara['subject'][0],u'下辖全部事项导出清单.xls', u'下辖事项清单','B4')
        check1=checkExcelCellValue(checkPara['serialNumber'][0],'downAllIssuesExportSheet.xls', '下辖事项清单','A4')
        check2=checkExcelCellValue(checkPara['subject'][0],'downAllIssuesExportSheet.xls', '下辖事项清单','B4')
        if check1 is True and check2 is True:
            return True
        else:
            return False
    except Exception,e :
            Log.LogOutput(LogLevel.ERROR, '验证出现异常！'+str(e))
            return False

'''
    @功能：检查下辖事项-全部事项列表导出的数据单元格记录行数
    @para:           
    @return:记录行数
    @author:  chenhui 2015-12-18
'''  
def getExcelCellRowNum(fileName, sheetName):
    newFileName = "c:/autotest_file/%s" % fileName
    try:
        data = xlrd.open_workbook(newFileName)
    except Exception,e:
        Log.LogOutput(LogLevel.ERROR, "打开文件失败"+str(e))
        return -1
    try:
        count=3#从第三行开始读    
        cellExactValue = data.sheet_by_name(sheetName).cell(count,0).value
    except Exception,e:
        Log.LogOutput(LogLevel.ERROR, "导出文件数据为空"+str(e))
        return -1
    try:
        while cellExactValue is not None:
            count=count+1
            cellExactValue = data.sheet_by_name(sheetName).cell(count,0).value
        return count-3
    except Exception ,e:
            Log.LogOutput(LogLevel.DEBUG, '已经读到行末尾,返回行数！'+str(e))
            return count-3    



'''
    @功能：检查下辖事项-全部事项列表所有记录数
    @para:           
    @return:记录行数
    @author:  chenhui 2015-12-18
'''  
def getDownAllIssueTotalNum(issueDict,username=userInit['DftJieDaoUser'],password='11111111'):
    Log.LogOutput( message='正在获取下辖全部事项总数')
    response=pinganjianshe_get(url='/issues/issueManage/findJurisdictionsAllIssues.action',param=issueDict,username=username,password=password)
    responseDict=json.loads(response.text)
    return responseDict['records']


'''
    @功能：检查下辖事项-全部事项列表查询
    @para:           
    @return:response
    @author:  chenhui 2015-12-18
'''  
def searchDownAllIssue(issueDict,username=userInit['DftJieDaoUser'],password='11111111'):
    Log.LogOutput( message='查询下辖全部事件中')
    response=pinganjianshe_get(url='/issues/searchIssue/searchJurisdictionsAllIssues.action',param=issueDict,username=username,password=password)
    return response


'''
    @功能：绩效考核设置，督办扣分、正常加分标准
    @para:           
    @return:response
    @author:  chenhui 2015-12-24
'''  
def setScoreStandard (issueDict,username=userInit['DftJieDaoUser'],password='11111111'):
    Log.LogOutput( message='设置绩效考核扣分标准')
    response=pinganjianshe_get(url='/issueAccessConfigManage/saveSet.action',param=issueDict,username=username,password=password)
#     Log.LogOutput(LogLevel.DEBUG,response.text)
    return response

'''
    @功能：绩效考核设置，行政部门时限标准，受理、办理时限
    @para:           
    @return:response
    @author:  chenhui 2015-12-24
'''  
def addTimeLimitStandard (issueDict,username=userInit['DftJieDaoUser'],password='11111111'):
    Log.LogOutput( message='设置绩效考核行政部门时限标准')
    response=pinganjianshe_post(url='/timeLimitStandardManage/addTimeLimitStandard.action',postdata=issueDict,username=username,password=password)
#     print response.text
#     Log.LogOutput(LogLevel.DEBUG,response.text)
    return response


'''
    @功能：issueOvertimeHandlerJob设置时间并重新启动
    @para:           
    @return:true/false
    @author:  chenhui 2015-12-24
'''  
def setIssueOvertimeHandlerJob (issueDict,username=userInit['DftJieDaoUser'],password='11111111'):
    Log.LogOutput( message='设置事件超时自动督办job时间')
    try:
        #获取该JOB在task表中的id
        id=getDbQueryResult(dbCommand = "select id from task t where t.name='issueOvertimeHandlerJob'")
        jobPara1={
                   'task.id':id,
                   'task.closed':'0'
                   }
        #关闭该job
        Log.LogOutput(message='关闭job')
        response1=pinganjianshe_get(url='/task/taskManage/changeTask.action',param=jobPara1,username=username,password=password)
        Log.LogOutput(LogLevel.DEBUG,response1.text)
        #修改job时间
        Log.LogOutput(message='修改job时间')
        jobPara2=copy.deepcopy(jobPara1)
        jobPara2['task.name']='issueOvertimeHandlerJob'
        jobPara2['task.taskGroup']='issueOvertimeHandlerJob'
        jobPara2['task.taskPloy.id']=id
        #修改job运行时间
        jobPara2['task.Data']=issueDict['task.Data']
        jobPara2['task.description']='issueOvertimeHandlerJob'
        response2=pinganjianshe_get(url='/task/taskManage/updateTask.action',param=jobPara2,username=username,password=password)
        Log.LogOutput(LogLevel.DEBUG,response2.text)
        
        #开启job
        Log.LogOutput(message='启动job')
        jobPara1['task.closed']='1'
        response3=pinganjianshe_get(url='/task/taskManage/changeTask.action',param=jobPara1,username=username,password=password)
        Log.LogOutput(LogLevel.DEBUG,response3.text)
        Log.LogOutput(message='JOB已经开启，当前服务器时间为'+getLinuxDateAndTime())
        if response1.result and response2.result and response3.result:
            return True
        else:
            return False
    except Exception,e:
            Log.LogOutput(LogLevel.ERROR, '设置JOB时间出现异常！'+str(e))
            
'''
    @功能：获取服务器的时间，然后加上或者减去n秒并返回，格式为%s%m%h
    @para:延迟秒数           
    @return:返回延迟后的时间，格式为%s%m%h * * ?
    @author:  chenhui 2015-12-24
'''  
def setJobDelayTime (username="root",password=Global.PingAnJianSheAppServRootPass,seconds='30'):
    serverIp = Global.PingAnJianSheUrl.split(':',2)[1].lstrip('/')#'anhaooray.oicp.net'
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(serverIp, 22, username=username, password=password, timeout=4)
#    client.connect(serverIp, 22105, username=username, password=password, timeout=4)
    Log.LogOutput(LogLevel.DEBUG,'当前服务器时间为：'+getLinuxDateAndTime())
    command='date +%S%t%M%t%H --date="+'+seconds +' second"'
    stdin,stdout,stderr=client.exec_command(command)
    retLines = stdout.readlines()
    client.close()
    str1=retLines[0].replace("\n"," ")
    #去除\t，并格式化返回结果为：%s%m%h * * ?
    str1=str1.replace('\t',' ')+'* * ?'
    Log.LogOutput(LogLevel.DEBUG,message='修改JOB执行时间为: '+str1)
    return str1


'''
    @功能：JOB监控中制定的JOB是否执行成功
    @para:checkPara['jobName']job名称
    @param checkPara['jobSuccess']:job执行结果           
    @return:    true/false
    @author:  chenhui 2015-12-25
'''  
def checkJobComplete(checkPara,username=userInit['DftJieDaoUser'],password='11111111'):
#     try:
        Log.LogOutput(message='正在JOB监控中检测job是否运行成功')
        listPara={
                    'grade':'-1',
                    '_search':'false',
                    'rows':'200',
                    'page':'1',
                    'sidx':'startDate',
                    'sord':'desc'
                  }
        response=pinganjianshe_get(url='/sysadmin/jobMonitor/findJobMonitor.action',param=listPara,username=username,password=password)
        if response.result:
            responseDict=json.loads(response.text)
            if responseDict['total']==0:
                Log.LogOutput(message='JOB尚未开始执行，请耐心等待...')
                return False
            else:
                listDict=responseDict['rows']
#                Log.LogOutput(LogLevel.DEBUG,listDict)
                for item in listDict:
                    if regMatchString(item['jobname'].lower(),checkPara['jobName'].lower()):
                        Log.LogOutput(LogLevel.DEBUG,'查找到JOB对应的jobname')
#                        print item
                        if 'success' in item and item['success'] is True:
                            Log.LogOutput(message='JOB执行成功！JOB开始执行时间为：'+item['startDate'])
                            return True
                        elif 'success' in item and item['success'] is False:
                            Log.LogOutput(LogLevel.ERROR,message='JOB执行失败！')
                            return False
                        else:
                            Log.LogOutput(message='JOB还没执行结束')
                            return False
            return False
        if not response.result:
            Log.LogOutput(message='请求出错！')
            return False
            
#     except Exception,e :
#             Log.LogOutput(LogLevel.ERROR, '出现异常！'+str(e))
#             return False
        
'''
    @功能：清空数据表
    @para:
    @return:    true/false
    @author:  chenhui 2015-12-25
'''  
def clearTable(tableName=None):
    try:
        #首先确定是否存在该表
        if getDbQueryResult(dbCommand="select count(*) from user_tables u where u.TABLE_NAME='%s'"%tableName.upper())==0:
            Log.LogOutput(LogLevel.ERROR,message='该表不存在，请先创建表！')
            return True
        #删除前先查询表，如果本身不存在数据，那么跳过
        rs0=getDbQueryResult(dbCommand = "select count(*) from %s"%tableName)
        if rs0!=0:
            #删除表数据
            Log.LogOutput(LogLevel.DEBUG,'表中存在数据，正在清除表'+tableName)
            exeDbQuery(dbCommand ="delete from %s"%tableName)
            #查询表数据
            rs=getDbQueryResult(dbCommand = "select count(*) from %s"%tableName)
            if rs ==0:
                Log.LogOutput(message=tableName+'表数据已成功清除！')
            else:
                Log.LogOutput(LogLevel.ERROR,message=tableName+'表中仍然有'+str(rs)+'条数据，清除失败！')
    except Exception,e :
            Log.LogOutput(LogLevel.ERROR, '清除'+tableName+'表数据过程出现异常！'+str(e))
            

'''
    @功能：获取行政部门绩效考核打分记录数组
    @para:           
    @return:      {
                        addPointByPerson: 0         人工加分
                        amoutPoint: 108               总分
                        assessmentUser: 8            其他打分
                        audited: false
                        deductPointByPerson: 0    人工扣分
                        internalId: 0代表行政部门  1代表职能部门
                        org: {id: 911, maxCode: 0}
                        orgName: "测试自动化社区"
                        redAmout: 0                      红牌扣分
                        yellowAmout: 0                 黄牌扣分
                        }
    @author:  chenhui 2015-12-25
'''  
def getRegradedPoint(issuePara,username=userInit['DftJieDaoUser'],password='11111111'):
    try:
        Log.LogOutput(message='正在获取行政部门绩效考核打分数据')
        response=pinganjianshe_get(url='/statAnalyse/statRegradedPointManage/findStatRegradedPoints.action',param=issuePara,username=username,password=password)
#         Log.LogOutput(LogLevel.DEBUG,response.text)
        responseDict=json.loads(response.text)
        listDict=responseDict['rows']
        #列表只有一行，直接返回第一行
        for item in listDict:
            if item is not None:
                return item
            else:
                return None
    except Exception,e :
            Log.LogOutput(LogLevel.ERROR, '验证出现异常！'+str(e))            


'''
    @功能：     执行SQL语句，主要是删除
    @para: command 要执行是sql语句
    @return: 
    @author: 陈辉 2015-12-25
'''

def exeDbQuery(dbCommand = None, dbIp=Global.PingAnJianSheDbIp, dbInstance=Global.PingAnJianSheDbInstance, dbUser=Global.PingAnJianSheDbUser, dbPass=Global.PingAnJianSheDbPass):
    if Global.simulationEnvironment is True:
        Log.LogOutput(1,'仿真环境，禁止数据库操作')
        raise RuntimeError('仿真环境，禁止数据库操作')
    else:
        os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
        conn = cx_Oracle.connect(dbUser, dbPass,"%s:1521/%s" % (dbIp,dbInstance))
    #    conn = cx_Oracle.connect(dbUser, dbPass,"%s:21521/%s" % (dbIp,dbInstance))
        cursor = conn.cursor()
        cursor.execute(dbCommand)
        cursor.close ()
        #提交！！
        conn.commit()
        conn.close() 
    

'''
    @功能：验证下辖督办列表中是否存在所要查找的字典项
    @para:checkPara:{issueId,dealState,supervisionState}
    @param issueDict=superviseIssuesList
    @return:    true/false
    @author:  chenhui 2015-12-28
'''  
def checkSuperviseIssue(checkPara,issueDict,username=userInit['DftJieDaoUser'],password='11111111'):
    try:
        #未办督办列表
        if issueDict['supervisePageType']=='notDoneSupervise':
            Log.LogOutput( message='正在验证下辖督办列表-未办督办页面是否存在待检查事件')
        if issueDict['supervisePageType']=='doneSupervise':
            Log.LogOutput( message='正在验证下辖督办列表-已办督办页面是否存在待检查事件')
        if issueDict['supervisePageType']=='allSupervise':
            Log.LogOutput( message='正在验证下辖督办列表-全部督办页面是否存在待检查事件')
        
        
        response=pinganjianshe_get(url='/issues/issueManage/findSuperviseIssues.action',param=issueDict,username=username,password=password)
        if response.result is False:
            Log.LogOutput(LogLevel.ERROR,'请求结果异常，请检查输入参数')
            return False
        responseDict = json.loads(response.text)
        
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
                return False
    except Exception,e :
        Log.LogOutput(LogLevel.ERROR, '下辖督办列表验证出现异常！'+str(e))    
        return False
    
'''
    @功能：初始化事件模块数据
    @para:
    @param 
    @return:
    @author:  chenhui 2016-2-2
'''  
def shiJianChuLiInitEnv():
    if Global.simulationEnvironment is False:
        #插入“其他”类型
        if getDbQueryResult(dbCommand="select count(*) from issuetypes i where i.domainid='4'")==0:
            insertsql="""
                insert into issuetypes
                values(s_issuetypes.nextval,null,(select id from issuetypedomains where module='core' and domainName='其他'),1,0,1,1,'其他',
                 '其他','qt','qita',null,'admin','admin',sysdate,sysdate)
                           """
            exeDbQuery(dbCommand=insertsql)
    #如果工作日历没有设置，则设置2016年工作日历
        if getDbQueryResult(dbCommand="select count(*) from workcalendars w where w.year='2016'")==0:
            Log.LogOutput(LogLevel.INFO, "2016工作日历没有创建，即将初始化工作日历..")
            response = pinganjianshe_post(url='/sysadmin/workCalendarManger/addWorkCalendar.action', postdata={'workCalendar.year':'2016'}, username='admin', password='admin')
    #         print response.text
            if response.result is True and getDbQueryResult(dbCommand="select count(*) from workcalendars w where w.year='2016'")==366:
                Log.LogOutput(message='2016工作日历初始化成果')
        #清除自定义分类
        mDeleteAllSelfIssueType()
        #清空所有事件数据
        deleteAllIssues2()
    else:
        #清空所有事件数据
        deleteAllIssues2()

'''
    @功能：判断事件是否处于锁定状态
    @para:           
    @return:    response
    @author:  chenhui 2016-10-25
'''  
def isDocked(para,username=userInit['DftShengUser'],password='11111111'):
#     Log.LogOutput( message='判断事件是否处于锁定状态')
    try:
        response=pinganjianshe_get(url='/issues/issueManage/isDocked.action',param=para,username=username,password=password)
        if response.result is False:
#             Log.LogOutput(message='事件处于正常状态')
            return False
        elif response.result is True:
            Log.LogOutput(level=LogLevel.DEBUG, message='事件处于锁定状态')
            return True
    except Exception,e:
        print str(e)
        raise Exception('判断事件是否锁定出现异常')
 
'''
    @功能：事件解锁
    @para:           
    @return:    response
    @author:  chenhui 2016-10-25
'''  
def unDocked(para,username=userInit['DftShengUser'],password='11111111'):
    Log.LogOutput( message='事件解锁')
    try:
        response=pinganjianshe_get(url='/issues/issueManage/issueUnlock.action',param=para,username=username,password=password)
        if response.result is True:
            Log.LogOutput(message='事件解锁成功')
            return True
        elif response.result is False:
            Log.LogOutput(level=LogLevel.DEBUG, message='事件解锁失败')
            return False
    except Exception,e:
        print str(e)
        raise Exception('事件解锁出现异常')
        return False   