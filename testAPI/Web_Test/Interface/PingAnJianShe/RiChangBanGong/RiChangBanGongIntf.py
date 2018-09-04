# -*- coding:UTF-8 -*-
'''
Created on 2015-12-22

@author: chenyan
'''
from __future__ import unicode_literals
from COMMON import Log, CommonUtil
from COMMON.Time import getLinuxDateAndTime, getCurrentTime, \
    getCurrentDateAndTime, setLinuxTime
from CONFIG import Global
from CONFIG.Define import LogLevel
from CONFIG.InitDefaultPara import orgInit, userInit
from Interface.PingAnJianShe.Common import CommonIntf
from Interface.PingAnJianShe.Common.CommonIntf import getDbQueryResult
from Interface.PingAnJianShe.RiChangBanGong import RiChangBanGongPara
from Interface.PingAnJianShe.RiChangBanGong.RiChangBanGongPara import \
    conflictRptNormalDelPara
from Interface.PingAnJianShe.ShiJianChuLi.ShiJianChuLiIntf import exeDbQuery, \
    clearTable, checkJobComplete, setJobDelayTime
from Interface.PingAnJianShe.pingAnJianSheHttpCommon import pinganjianshe_post, \
    pinganjianshe_get
import copy
import json
import paramiko
import time

'''  
    @功能： 初始化日常办公模块环境
    @para: 
    @return:   
'''
def richangBanGongInitEnv():
    try:
        #1.如果工作日历没有设置，则设置2016年工作日历
        if getDbQueryResult(dbCommand="select count(*) from workcalendars w where w.year='2016'")==0:
            Log.LogOutput(LogLevel.INFO, "2016工作日历没有创建，即将初始化工作日历..")
            response = pinganjianshe_post(url='/sysadmin/workCalendarManger/addWorkCalendar.action', postdata={'workCalendar.year':'2016'}, username='admin', password='admin')
            if response.result is True and getDbQueryResult(dbCommand="select count(*) from workcalendars w where w.year='2016'")==366:
                Log.LogOutput(message='2016工作日历初始化成果')
        #2.台账目录如果为空，则创建工作目录
        #行政部门台账目录
        clearTable(tableName='JOBMONITOR')#job监控表
        if getDbQueryResult(dbCommand="select count(*) from DailyYears d where d.dailytype='0' and d.yeardate='2016'")==0:
            Log.LogOutput(message='台账目录没有生成，即将生成台账目录')
            #点击新增-确定台账类型后，即产生dailyYear.id
            para1={
                  'mode':'add',
                  'dailyType':0
                  }
            pinganjianshe_post(url='/plugin/seniorAccountManage/dispatchOperate.action', postdata=para1, username='admin', password='admin')
            dailyYearPara1={
                    'dailyYear.id':getDbQueryResult(dbCommand="select max(id) from DailyYears"),
                    'dailyYear.dailyType':0,
                    'dailyYear.yearDate':2016
                    }
            response1=pinganjianshe_post(url='/plugin/seniorAccountManage/addSeniorDailyDirectory.action', postdata=dailyYearPara1, username='admin', password='admin')
            responseDict1=json.loads(response1.text)
            taskPara1={
                    'task.dailyyearid':responseDict1['id'],
                    'task.applicationobject':responseDict1['dailyType'],
                    'task.name':'2016年工作台账模版',
                    'task.yeardate':2016,
                    #应用层级
                    'task.applicationLevel':(getDbQueryResult(dbCommand="select id from propertydicts p where p.displayname='村（社区）'"),\
                                             getDbQueryResult(dbCommand="select id from propertydicts p where p.displayname='乡镇（街道）'"),\
                                             getDbQueryResult(dbCommand="select id from propertydicts p where p.displayname='县（区）'"),\
                                             getDbQueryResult(dbCommand="select id from propertydicts p where p.displayname='市'"),\
                                             getDbQueryResult(dbCommand="select id from propertydicts p where p.displayname='省'"))
                      } 
            #批量创建
            pinganjianshe_post(url='/plugin/taskListManage/addTaskList.action', postdata=taskPara1, username='admin', password='admin')
        #职能部门台账目录    
        if getDbQueryResult(dbCommand="select count(*) from DailyYears d where d.dailytype='1' and d.yeardate='2016'")==0:
            para2={
                  'mode':'add',
                  'dailyType':1
                  }
            pinganjianshe_post(url='/plugin/seniorAccountManage/dispatchOperate.action', postdata=para2, username='admin', password='admin')
    
            dailyYearPara2={
                    'dailyYear.id':getDbQueryResult(dbCommand="select max(id) from DailyYears"),
                    'dailyYear.dailyType':1,
                    'dailyYear.yearDate':2016
                    }
            response2=pinganjianshe_post(url='/plugin/seniorAccountManage/addSeniorDailyDirectory.action', postdata=dailyYearPara2, username='admin', password='admin')
            responseDict2=json.loads(response2.text)
            taskPara2={
                    'task.dailyyearid':responseDict2['id'],
                    'task.applicationobject':responseDict2['dailyType'],
                    'task.name':'2016年职能部门台账模版',
                    'task.yeardate':2016,
                    #应用层级
                    'task.applicationLevel':(getDbQueryResult(dbCommand="select id from propertydicts p where p.displayname='村（社区）'"),\
                                             getDbQueryResult(dbCommand="select id from propertydicts p where p.displayname='乡镇（街道）'"),\
                                             getDbQueryResult(dbCommand="select id from propertydicts p where p.displayname='县（区）'"),\
                                             getDbQueryResult(dbCommand="select id from propertydicts p where p.displayname='市'"),\
                                             getDbQueryResult(dbCommand="select id from propertydicts p where p.displayname='省'"))
                      }
            #批量创建模板 
            pinganjianshe_post(url='/plugin/taskListManage/addTaskList.action', postdata=taskPara2, username='admin', password='admin')
            #启动job
            #首先将服务器时间改为1月26日
            data='2016-1-26 '+getCurrentTime()
            setLinuxTime(data=data)
            #      设置JOB：batchCreateDailyJob名称和延后执行时间参数，默认延后30s
            jobTimePara={
                         'task.Data':setJobDelayTime(),
                         'task.name':'batchCreateDailyJob',
                         'job.name':'batchCreateDailyJob'
                         }
            runJob(jobPara=jobTimePara)
            
        #3.如果没有1月份的报表，则优先初始化1月份表结构，再通过执行job，生成2月表结构
        #插入事件“其他”类型
        if getDbQueryResult(dbCommand="select count(*) from issuetypes i where i.domainid='4'")==0:
            insertsql="""
                insert into issuetypes
                values(s_issuetypes.nextval,null,(select id from issuetypedomains where module='core' and domainName='其他'),1,0,1,1,'其他',
                 '其他','qt','qita',null,'admin','admin',sysdate,sysdate)
                           """
            exeDbQuery(dbCommand=insertsql)
        #原来的方式通过sql创建1月份表，再通过job生成2月份表，现为了提高性能，直接采用sql方式生成2016年全年表结构 
        
        for i in range(1,13):
            if getDbQueryResult(dbCommand="select count(*) from user_tables u where u.TABLE_NAME='CONFLICTRPTNORMAL_2016_%s'"%i)==0:
                initTable(year_mon="2016_"+str("%d")%i)

# #         initTable(year_mon='2016_1')
#         if getDbQueryResult(dbCommand="select count(*) from user_tables u where u.TABLE_NAME='CONFLICTRPTNORMAL_2016_2'")==0:
#             #首先将服务器时间改为2016年1月26日
#             Data='2016-1-26 '+getCurrentTime()
#             setLinuxTime(Data=Data)
#             #运行JOB：ConverImportantLastMonthAddToInventorJob
#             jobTimePara1={
#                          'task.Data':setJobDelayTime(),
#                          'task.name':'ConverImportantLastMonthAddToInventorJob',
#                          'job.name':'ConverImportantLastMonthAddToInventorJob'
#                          }
#             runJob(jobPara=jobTimePara1)
#             #设置JOB:newStateConflictAnalyzingDataJob的名称和延后执行时间
#             jobTimePara2={
#                          'task.Data':setJobDelayTime(),
#                          'task.name':'newStateConflictAnalyzingDataJob',
#                          'job.name':'newStateConflictAnalyzingDataJob'
#                          }
#             runJob(jobPara=jobTimePara2)
#             #设置JOB：converLastMonthAddToInventorJob名称和延后执行时间参数，延后·10s
#             jobTimePara3={
#                          'task.Data':setJobDelayTime(),
#                          'task.name':'converLastMonthAddToInventorJob',
#                          'job.name':'converLastMonthAddToInventorJob'
#                          }
#             runJob(jobPara=jobTimePara3)
#             if getDbQueryResult(dbCommand="select count(*) from user_tables u where u.TABLE_NAME='CONFLICTRPTNORMAL_2016_2'")!=0 :
#                 Log.LogOutput(message='表结构创建成功！')
#             #将服务器时间改回正确时间
#             setLinuxTime(Data=getCurrentDateAndTime())

    finally:
        #4.清空表数据
        deleteAllReport()
        #5.将初始日期时间调整正确
#         linuxTime=getLinuxDateAndTime()
#         localTime=getCurrentDateAndTime()
#         if linuxTime !=localTime:
#             Log.LogOutput(message='服务器时间与本地时间不一致，正在调整服务器时间')
#             setLinuxTime(Data=getCurrentDateAndTime())
'''  
    @功能： 新增测试自动化社区下台账的会议、文件、活动、其他记录
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
'''
def add_WorkingRecord(WorkingDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增记录开始..")
    response = pinganjianshe_post(url='/newWorkingRecord/newWorkingRecordManage/dispatchBusiness.action', postdata=WorkingDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增记录成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增记录失败")
    return response

'''  
    @功能： 修改测试自动化社区下台账的会议、文件、活动、其他记录
    @para: 
    @return: 如果修改成功，则返回True；否则返回False  
'''
def edit_WorkingRecord(WorkingDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "修改记录开始..")
    response = pinganjianshe_post(url='/newWorkingRecord/newWorkingRecordManage/dispatchBusiness.action', postdata=WorkingDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "修改记录成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "修改记录失败")
    return response

'''  
    @功能： 删除测试自动化社区下台账的会议、文件、活动、其他记录
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
'''
def delete_WorkingRecord(WorkingDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "删除记录开始..")
    response = pinganjianshe_get(url='/newWorkingRecord/newWorkingRecordManage/deleteWorkingRecordByIds.action', param=WorkingDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除记录成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "删除记录失败")
    return response

'''  
    @功能： 转移测试自动化社区下台账的会议、文件、活动、其他记录
    @para: 
    @return: 如果转移成功，则返回True；否则返回False  
'''
def transfer_WorkingRecord(WorkingDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "转移记录开始..")
    response = pinganjianshe_get(url='/newWorkingRecord/newWorkingRecordManage/transferWorkingRecord.action', param=WorkingDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "转移记录成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "转移记录失败")
    return response

'''  
    @功能： 将测试自动化街道中辖区台账下台账的会议、文件、活动、其他记录复制
    @para: 
    @return: 如果复制成功，则返回True；否则返回False  
'''
def copy_WorkingRecord(WorkingDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "复制记录开始..")
    response = pinganjianshe_get(url='/newWorkingRecord/newWorkingRecordManage/copyToMyWorkingRecord.action', param=WorkingDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "复制记录成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "复制记录失败")
    return response

'''  
    @功能： 检查测试自动化社区下台账的会议、文件、活动、其他记录
    @para: 
    @return: 如果检查成功，则返回True；否则返回False  
'''
def check_WorkingRecord(WorkingDict, orgId=None, dailyDirectoryId=None,username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "检查记录开始..")
    try:
        compDict = copy.deepcopy(RiChangBanGongPara.getRecordDict)
        compDict['newWorkingRecordVo.organization.id']= orgId
        compDict['newWorkingRecordVo.dailyDirectoryId']= dailyDirectoryId 
        response = pinganjianshe_get(url='/newWorkingRecord/newWorkingRecordManage/newWorkingRecordList.action', param=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(WorkingDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到记录信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到记录信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查记录信息失败")
        return False


'''  
    @功能： 新增测试自动化社区下我的资料下的资料信息
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
'''
def add_MyProfile(ProfileDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增资料开始..")
    response = pinganjianshe_post(url='/resourcePool/myProfileManage/addMyProfile.action', postdata=ProfileDict, username=username, password=password)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增资料成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增资料失败")
    return response

'''  
    @功能： 修改测试自动化社区下我的资料下的资料信息
    @para: 
    @return: 如果修改成功，则返回True；否则返回False  
'''
def edit_MyProfile(ProfileDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "修改资料开始..")
    response = pinganjianshe_post(url='/resourcePool/myProfileManage/updateMyProfile.action', postdata=ProfileDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "修改资料成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "修改资料失败")
    return response

'''  
    @功能： 根据测试自动化社区下我的资料名称获取资料的id
    @para: 
    @return: 如果修改成功，则返回id；否则返回-1  
'''
def get_myprofile_id_by_name(name, username = userInit['DftSheQuUser'], password = "11111111"):
    Log.LogOutput(LogLevel.INFO, "获取我的资料id开始..")
    getListPara={
                'resourcePoolTypeId':CommonIntf.getDbQueryResult(dbCommand = "select p.displayseq from propertydicts  p where p.displayname = '法律法规'"),
                'searchType':'0',
                '_search':'false',
                'rows':'20',
                'page':'1',
                'sidx':'id',
                'sord':'desc',
                 }
    response = pinganjianshe_get(url='/resourcePool/myProfileManage/findMyProfileForList.action', param=getListPara, username=username, password=password)
#     print response.text
    try:
        resDict=json.loads(response.text)
        for item in resDict['rows']:
            if item['name']==name:
                Log.LogOutput(message="成功查找到id")
                return item['id']
        Log.LogOutput(message="没有查找到id")
        return -1
    except Exception,e:
        Log.LogOutput(message="查找id出现异常"+str(e))
        return -1
'''  
    @功能： 搜索测试自动化社区下我的资料下的资料信息
    @para: 
    @return: 如果搜索成功，则返回True；否则返回False  
'''
def search_MyProfile(ProfileDict, typeId=None, name=None,username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "搜索资料信息开始..")
    try:
        compDict = copy.deepcopy(RiChangBanGongPara.searchProfileObject)
        compDict['resourcePoolType.id']= typeId
        compDict['myProfile.name']= name
        response = pinganjianshe_post(url='/resourcePool/myProfileManage/searchMyProfile.action', postdata=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(ProfileDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "搜索到资料信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "搜索查到资料信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查资料信息失败")
        return False

'''  
    @功能： 删除测试自动化社区下我的资料下的资料信息
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
'''
def delete_MyProfile(ProfileDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "删除资料开始..")
    response = pinganjianshe_get(url='/resourcePool/myProfileManage/deleteMyProfile.action', param=ProfileDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除资料成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "删除资料失败")
    return response

'''  
    @功能： 设置资料共享时的查看权限
    @para: 
    @return: 如果设置成功，则返回response.text  
'''
def viewObject(cacheDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "设置共享权限开始..")
    response = pinganjianshe_get(url='/viewObject/ajaxSaveViewObjectToCache.action', param=cacheDict, username=username, password=password)
    responseDict=json.loads(response.text)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "设置共享权限成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "设置共享权限失败")
    return responseDict['id']

'''  
    @功能： 检查测试自动化社区下资料否共享成功
    @para: 
    @return: 如果检查成功，则返回True；否则返回False  
'''
def check_sharingMyProfile(ProfileDict, typeId=None, username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "检查资料是否共享成功开始..")
    try:
        compDict = copy.deepcopy(RiChangBanGongPara.getProfileDict)
        compDict['resourcePoolTypeId']= typeId
        response = pinganjianshe_get(url='/resourcePool/sharingFilesManage/findSharingFilesList.action', param=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(ProfileDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到资料信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到资料信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查资料信息失败")
        return False

'''  
    @功能： 分享测试自动化社区下我的资料下的资料信息
    @para: 
    @return: 如果分享成功，则返回True；否则返回False  
'''
def share_MyProfile(ProfileDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "分享资料信息开始..")
    response = pinganjianshe_post(url='/resourcePool/myProfileManage/addUserMyProfilePermission.action', postdata=ProfileDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "分享资料信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "分享资料信息失败")
    return response

'''  
    @功能： 取消分享测试自动化社区下我的资料下的资料信息
    @para: 
    @return: 如果取消分享成功，则返回True；否则返回False  
'''
def cancelSharing_MyProfile(ProfileDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "资料信息取消分享开始..")
    response = pinganjianshe_get(url='/resourcePool/myProfileManage/cancelSharingMyProfile.action', param=ProfileDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "资料信息取消分享成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "资料信息取消分享失败")
    return response

'''  
    @功能： 检查测试自动化社区下我的资料下的资料信息
    @para: 
    @return: 如果检查成功，则返回True；否则返回False  
'''
def check_MyProfile(ProfileDict, typeId=None, username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "检查资料信息开始..")
    try:
        compDict = copy.deepcopy(RiChangBanGongPara.getProfileDict)
        compDict['resourcePoolTypeId']= typeId
        response = pinganjianshe_get(url='/resourcePool/myProfileManage/findMyProfileForList.action', param=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(ProfileDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到资料信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到资料信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查资料信息失败")
        return False


'''  
    @功能： 新增测试自动化社区层级下发文管理中的发文信息
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
'''
def add_DocumentsManag(documentDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增发文信息开始..")
    response = pinganjianshe_post(url='/documents/dispatchDocumentsManage/addDispatchDocuments.action', postdata=documentDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增发文信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增发文信息失败")
    return response

'''  
    @功能： 批量删除测试自动化社区层级下发文管理中的发文信息
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
'''
def delete_DocumentsManag(documentDict, sidx=None, username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "删除发文信息开始..")
    response = pinganjianshe_get(url='/documents/dispatchDocumentsManage/deleteDispatchDocById.action', param=documentDict, username=username, password=password)
    if response.result is True:        
        Log.LogOutput(LogLevel.INFO, "删除发文信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "删除发文信息失败")
    return response

'''  
    @功能： 搜索测试自动化社区层级下发文管理中的发文信息
    @para: 
    @return: 如果搜索成功，则返回True；否则返回False  
'''
def search_DocumentsManag(documentDict, sidx=None, username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "搜索发文信息开始..")
    response = pinganjianshe_post(url='/documents/dispatchDocumentsManage/searchDispatchDocuments.action', postdata=documentDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "搜索发文信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "搜索发文信息失败")
    return response

'''  
    @功能： 修改测试自动化社区层级下发文管理中的发文信息
    @para: 
    @return: 如果修改成功，则返回True；否则返回False  
'''
def edit_DocumentsManag(documentDict, sidx=None, username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "修改发文信息开始..")
    response = pinganjianshe_post(url='/documents/dispatchDocumentsManage/updateDispatchDocuments.action', postdata=documentDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "修改发文信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "修改发文信息失败")
    return response

'''  
    @功能： 再次编辑测试自动化社区层级下发文管理中的发文信息
    @para: 
    @return: 如果再次编辑成功，则返回True；否则返回False  
'''
def editAgain_DocumentsManag(documentDict, sidx=None, username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "再次编辑发文信息开始..")
    response = pinganjianshe_post(url='/documents/dispatchDocumentsManage/editAgainDispatchDocuments.action', postdata=documentDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "再次编辑发文信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "再次编辑发文信息失败")
    return response

'''  
    @功能： 将测试自动化社区层级下发文管理中的发文信息同步到资料库
    @para: 
    @return: 如果同步成功，则返回True；否则返回False  
'''
def synch_DocumentsManag(documentDict, sidx=None, username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "将发文信息同步到资料库开始..")
    response = pinganjianshe_post(url='/documents/dispatchDocumentsManage/synchToMyProfile.action', postdata=documentDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "发文信息同步到资料库成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "发文信息同步到资料库失败")
    return response

'''  
    @功能： 将测试自动化社区层级下发文管理中的发文信息同步到台账
    @para: 
    @return: 如果同步成功，则返回True；否则返回False  
'''
def synch_Documents(documentDict, sidx=None, username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "将发文信息同步到台账开始..")
    response = pinganjianshe_post(url='/newWorkingRecord/newWorkingRecordManage/synchroDispathDocumentToWorkingRecord.action', postdata=documentDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "发文信息同步到台账成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "发文信息同步到台账失败")
    return response

'''  
    @功能： 发送测试自动化社区层级下发文管理中的发文信息
    @para: 
    @return: 如果发送成功，则返回True；否则返回False  
'''
def send_Documents(documentDict, sidx=None, username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "发送发文信息开始..")
    response = pinganjianshe_get(url='/documents/dispatchDocumentsManage/sendDocuments.action', param=documentDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "发送发文信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "发送发文信息失败")
    return response

'''  
    @功能： 撤回测试自动化社区层级下发文管理中已经发出的发文信息
    @para: 
    @return: 如果撤回成功，则返回True；否则返回False  
'''
def withdraw_Documents(documentDict, sidx=None, username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "撤回已发送发文信息开始..")
    response = pinganjianshe_get(url='/documents/dispatchDocumentsManage/withdraw.action', param=documentDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "撤回发文信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "撤回发文信息失败")
    return response

'''  
    @功能： 搜索测试自动化网格层级下发文管理中的收文信息
    @para: 
    @return: 如果搜索成功，则返回True；否则返回False  
'''
def search_ReceiveDocumentsManag(documentDict, sidx=None, username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "搜索收文信息开始..")
    response = pinganjianshe_post(url='/documents/receiveDocumentsManage/searchReceiveDocuments.action', postdata=documentDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "搜索收文信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "搜索收文信息失败")
    return response

'''  
    @功能： 签收测试自动化网格层级下收文管理中的收文信息
    @para: 
    @return: 如果签收成功，则返回True；否则返回False  
'''
def receive_DocumentsManag(documentDict, username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "签收文件信息开始..")
    response = pinganjianshe_get(url='/documents/receiveDocumentsManage/receiveDocuments.action', param=documentDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "签收文件信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "签收文件信息失败")
    return response

'''  
    @功能： 阅读测试自动化网格层级下收文管理中已签收的文件信息
    @para: 
    @return: 如果阅读成功，则返回True；否则返回False  
'''
def read_DocumentsManag(documentDict, username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "阅读文件信息开始..")
    response = pinganjianshe_get(url='/documents/receiveDocumentsManage/operateReceiveDocuments.action', param=documentDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "阅读文件信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "阅读文件信息失败")
    return response

'''  
    @功能： 转发测试自动化社区层级下发文管理中的发文信息
    @para: 
    @return: 如果转发成功，则返回True；否则返回False  
'''
def transmit_DocumentsManag(documentDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "转发发文信息开始..")
    response = pinganjianshe_post(url='/documents/dispatchDocumentsManage/transmitDocuments.action', postdata=documentDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "转发发文信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "转发发文信息失败")
    return response

'''  
    @功能： 批量删除测试自动化社区层级下收文管理中的收文信息
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
'''
def delete_Documents(documentDict, sidx=None, username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "删除收文信息开始..")
    response = pinganjianshe_get(url='/documents/receiveDocumentsManage/deleteReceiveDoc.action', param=documentDict, username=username, password=password)
    if response.result is True:        
        Log.LogOutput(LogLevel.INFO, "删除收文信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "删除收文信息失败")
    return response

'''  
    @功能： 检查测试自动化社区层级下发文管理中的发文信息是否发送成功
    @para: 
    @return: 如果检查成功，则返回True；否则返回False  
'''
def check_Documents(documentDict, sidx=None, username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "检查发文信息是否发送成功开始..")
    try:
        compDict = copy.deepcopy(RiChangBanGongPara.getDocumentDict)
        compDict['sidx']= sidx  
        response = pinganjianshe_get(url='/documents/receiveDocumentsManage/receiveDocumentsList.action', param=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(documentDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到发文信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到发文信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查发文信息失败")
        return False

'''  
    @功能： 检查测试自动化社区层级下发文管理中的发文信息
    @para: 
    @return: 如果检查成功，则返回True；否则返回False  
'''
def check_DocumentsManag(documentDict, sidx=None, username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "检查发文信息开始..")
    try:
        compDict = copy.deepcopy(RiChangBanGongPara.getDocumentDict)
        compDict['sidx']= sidx  
        response = pinganjianshe_get(url='/documents/dispatchDocumentsManage/dispatchDocumentsList.action', param=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(documentDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到发文信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到发文信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查发文信息失败")
        return False
    
'''  
    @功能： 检查测试自动化社区层级下发文管理中的收文信息
    @para: 
    @return: 如果检查成功，则返回True；否则返回False  
'''
def check_Manag(documentDict, sidx=None, username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "检查收文信息开始..")
    try:
        compDict = copy.deepcopy(RiChangBanGongPara.getDocumentDict)
        compDict['sidx']= sidx  
        response = pinganjianshe_get(url='/documents/receiveDocumentsManage/receiveDocumentsList.action', param=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(documentDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到收文信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到收文信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查发文信息失败")
        return False

'''  
    @功能： 搜索测试自动化网格层级下公文查询中的公文信息
    @para: 
    @return: 如果搜索成功，则返回True；否则返回False  
'''
def search_GongWenManag(documentDict, username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "搜索公文信息开始..")
    response = pinganjianshe_post(url='/documents/dispatchDocumentsManage/searchAllDocuments.action', postdata=documentDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "搜索公文信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "搜索公文信息失败")
    return response


'''  
    @功能： 新增测试自动化社区层级下民情日志中日志信息
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
'''
def add_logManage(manageDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增日志信息开始..")
    response = pinganjianshe_post(url='/peopleLog/peopleLogManage/maintainPeopleLog.action', postdata=manageDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增日志信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增日志信息失败")
    return response

'''  
    @功能： 修改测试自动化社区层级下民情日志中日志信息
    @para: 
    @return: 如果修改成功，则返回True；否则返回False  
'''
def edit_logManage(manageDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "修改日志信息开始..")
    response = pinganjianshe_post(url='/peopleLog/peopleLogManage/maintainPeopleLog.action', postdata=manageDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "修改日志信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "修改日志信息失败")
    return response

'''  
    @功能： 搜素测试自动化社区层级下民情日志中日志信息
    @para: 
    @return: 如果搜素成功，则返回True；否则返回False  
'''
def search_logManage(manageDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "搜素日志信息开始..")
    response = pinganjianshe_post(url='/peopleLog/searchPeopleLog/findPeopleLogByQueryCondition.action', postdata=manageDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "搜素日志信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "搜素日志信息失败")
    return response

'''  
    @功能： 批量删除测试自动化社区层级下民情日志中日志信息
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
'''
def delete_logManage(manageDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "删除日志信息开始..")
    response = pinganjianshe_get(url='/peopleLog/peopleLogManage/deletePeopleLog.action', param=manageDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除日志信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "删除日志信息失败")
    return response

'''  
    @功能： 检查测试自动化社区层级下民情日志中日志信息
    @para: 
    @return: 如果检查成功，则返回True；否则返回False  
'''
def check_logManage(manageDict,  username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "检查日志信息开始..")
    try:
        compDict = copy.deepcopy(RiChangBanGongPara.getLogManageDict)
        response = pinganjianshe_post(url='/peopleLog/peopleLogManage/peopleLogList.action', postdata=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(manageDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到日志信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到日志信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查日志信息失败")
        return False

'''  
    @功能： 点评测试自动化社区层级下民情日志中下辖日志信息
    @para: 
    @return: 如果点评成功，则返回True；否则返回False  
'''
def comment_logManage(manageDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "点评下辖日志信息开始..")
    response = pinganjianshe_get(url='/peopleLog/peopleLogManage/saveComment.action', param=manageDict, username=username, password=password)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "点评日志信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "点评日志信息失败")
    return response

'''  
    @功能： 通过日志标题获取测试自动化社区层级下民情日志中下辖日志id
    @para: 
    @return: 成功返回id；失败返回-1  
'''
def get_log_id_by_title(title=None, username=userInit['DftSheQuUser'], password='11111111'):
    Log.LogOutput(LogLevel.INFO, "获取日志id开始..")
    getListPara={
            'organizationId':orgInit['DftSheQuOrgId'],
            'isPeer':'true',
            '_search':'false',
            'rows':'200',
            'page':'1',
            'sidx':'id',
            'sord':'desc',
                 }
    response = pinganjianshe_post(url='/peopleLog/peopleLogManage/subLogList.action', postdata=getListPara, username=username, password=password)
#     print response.text
    try:
        resDict=json.loads(response.text)
        for item in resDict['rows']:
            if item['title']==title:
                Log.LogOutput(message='成功获取id')
                return item['id']
        Log.LogOutput(message='没有找到id')
        return -1
    except Exception,e:
        Log.LogOutput(message='查找id异常'+str(e))
        return -1
        
'''  
    @功能： 检查测试自动化社区层级下民情日志中下辖日志点评信息
    @para: 
    @return: 如果检查成功，则返回True；否则返回False  
'''
def check_commentManage(manageDict,  username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "我的点评下检查日志点评情况开始..")
    try:
        compDict = copy.deepcopy(RiChangBanGongPara.getCommentManageDict)
        response = pinganjianshe_post(url='/peopleLog/commentLogManage/myCommentList.action', postdata=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(manageDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到日志的点评情况")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到日志的点评情况")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查日志点评情况失败")
        return False

'''  
    @功能： 搜索测试自动化社区层级下民情日志中我的点评下的日志信息
    @para: 
    @return: 如果搜索成功，则返回True；否则返回False  
'''
def search_commentLog(manageDict,  username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "我的点评模块下搜索点评日志开始..")
    response = pinganjianshe_post(url='/peopleLog/searchCommentLog/findCommentLogByQueryCondition.action', postdata=manageDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "搜素点评日志成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "搜素点评日志失败")
    return response

'''  
    @功能： 搜索测试自动化社区层级下民情日志中的下辖日志信息
    @para: 
    @return: 如果搜索成功，则返回True；否则返回False  
'''
def search_comment(manageDict,  username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "搜索下辖日志信息开始..")
    response = pinganjianshe_post(url='/peopleLog/searchCommentLog/findSubLogByQueryCondition.action', postdata=manageDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "搜素下辖日志信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "搜素下辖日志信息失败")
    return response


'''  
    @功能： 新增测试自动化社区层级下的工作日志信息
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
'''
def add_workDiary(diaryDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增工作日志信息开始..")
    response = pinganjianshe_post(url='/dailyLog/workDiaryManage/addWorkDiary.action', postdata=diaryDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增工作日志信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增工作日志信息失败")
    return response

'''  
    @功能： 批量删除测试自动化社区层级下的工作日志信息
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
'''
def delete_workDiary(diaryDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "删除工作日志信息开始..")
    response = pinganjianshe_get(url='/dailyLog/workDiaryManage/deleteWorkDiaryById.action', param=diaryDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除工作日志信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "删除工作日志信息失败")
    return response

'''  
    @功能： 修改测试自动化社区层级下的工作日志信息
    @para: 
    @return: 如果修改成功，则返回True；否则返回False  
'''
def edit_workDiary(diaryDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "修改工作日志信息开始..")
    response = pinganjianshe_post(url='/dailyLog/workDiaryManage/editWorkDiary.action', postdata=diaryDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "修改工作日志信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "修改工作日志信息失败")
    return response

'''  
    @功能： 搜索测试自动化社区层级下的工作日志信息
    @para: 
    @return: 如果搜索成功，则返回True；否则返回False  
'''
def search_workDiary(diaryDict, orgId = None, diaryType = None,  username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "高级搜索工作日志信息开始..")
    try:
        compDict = copy.deepcopy(RiChangBanGongPara.searchDiaryObject)
        compDict['searchWorkDiaryVo.organization.id']= orgId
        compDict['searchWorkDiaryVo.diaryType']= diaryType 
        response = pinganjianshe_get(url='/dailyLog/searchWorkDiary/searchWorkDiary.action', param=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(diaryDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "搜索到工作日志信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未搜索到工作日志信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查工作日志信息")
        return False    
'''
    @功能： 检查测试自动化社区层级下的工作日志信息
    @para: 
    @return: 如果检查成功，则返回True；否则返回False  
'''
def check_workDiary(diaryDict,  username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "检查工作日志信息开始..")
    try:
        compDict = copy.deepcopy(RiChangBanGongPara.getCommentManageDict)
        response = pinganjianshe_get(url='/dailyLog/workDiaryManage/findWorkDiaryForPageByOrgId.action', param=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(diaryDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到工作日志信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到工作日志信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查工作日志信息")
        return False

    
    
'''
    @功能： 删除测试自动化社区下所有的
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
'''    
def deleteAllRecords():
    try:
        #台账
        #删除会议记录
        if CommonIntf.getDbQueryResult(dbCommand="select count(*) from NEWWORKINGRECORDS t where t.orgid='%s'" % orgInit['DftWangGeOrgId']) != 0: 
            compDict = copy.deepcopy(RiChangBanGongPara.getRecordDict)
            compDict['newWorkingRecordVo.organization.id']= orgInit['DftSheQuOrgId']
            compDict['newWorkingRecordVo.dailyDirectoryId']= CommonIntf.getDbQueryResult(dbCommand = "select t.id from DailyDirectorys t where t.shortname='会议' and t.dailyyearid = (select a.id from dailyyears a where a.makedorgid= '910' and a.name='2015年工作台账模版')")
            response = pinganjianshe_get(url='/newWorkingRecord/newWorkingRecordManage/newWorkingRecordList.action', param=compDict)  
            responseDict = json.loads(response.text)
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无会议记录')
            else:
                for dictListItem in responseDict['rows']:
                    deleteDict = {'ids':dictListItem['id']}
                    delete_WorkingRecord(deleteDict)
        #删除文件记录
        if CommonIntf.getDbQueryResult(dbCommand="select count(*) from NEWWORKINGRECORDS t where t.orgid='%s'" % orgInit['DftWangGeOrgId']) != 0:
            compDict = copy.deepcopy(RiChangBanGongPara.getRecordDict)
            compDict['newWorkingRecordVo.organization.id']= orgInit['DftSheQuOrgId']
            compDict['newWorkingRecordVo.dailyDirectoryId']= CommonIntf.getDbQueryResult(dbCommand = "select t.id from DailyDirectorys t where t.shortname='文件' and t.dailyyearid = (select a.id from dailyyears a where a.makedorgid= '910' and a.name='2015年工作台账模版')")
            response = pinganjianshe_get(url='/newWorkingRecord/newWorkingRecordManage/newWorkingRecordList.action', param=compDict)  
            responseDict = json.loads(response.text)
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无文件记录')
            else:
                for dictListItem in responseDict['rows']:
                    deleteDict = {'ids':dictListItem['id']} 
                    delete_WorkingRecord(deleteDict)
        #删除活动记录
        if CommonIntf.getDbQueryResult(dbCommand="select count(*) from NEWWORKINGRECORDS t where t.orgid='%s'" % orgInit['DftWangGeOrgId']) != 0:
            compDict = copy.deepcopy(RiChangBanGongPara.getRecordDict)
            compDict['newWorkingRecordVo.organization.id']= orgInit['DftSheQuOrgId']
            compDict['newWorkingRecordVo.dailyDirectoryId']= CommonIntf.getDbQueryResult(dbCommand = "select t.id from DailyDirectorys t where t.shortname='活动' and t.dailyyearid = (select a.id from dailyyears a where a.makedorgid= '910' and a.name='2015年工作台账模版')")
            response = pinganjianshe_get(url='/newWorkingRecord/newWorkingRecordManage/newWorkingRecordList.action', param=compDict)  
            responseDict = json.loads(response.text)
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无活动记录')
            else:
                for dictListItem in responseDict['rows']:
                    deleteDict = {'ids':dictListItem['id']} 
                    delete_WorkingRecord(deleteDict)
        #删除其他记录
        if CommonIntf.getDbQueryResult(dbCommand="select count(*) from NEWWORKINGRECORDS t where t.orgid='%s'" % orgInit['DftWangGeOrgId']) != 0:
            compDict = copy.deepcopy(RiChangBanGongPara.getRecordDict)
            compDict['newWorkingRecordVo.organization.id']= orgInit['DftSheQuOrgId']
            compDict['newWorkingRecordVo.dailyDirectoryId']= CommonIntf.getDbQueryResult(dbCommand = "select t.id from DailyDirectorys t where t.shortname='其他' and t.dailyyearid = (select a.id from dailyyears a where a.makedorgid= '910' and a.name='2015年工作台账模版')")
            response = pinganjianshe_get(url='/newWorkingRecord/newWorkingRecordManage/newWorkingRecordList.action', param=compDict)  
            responseDict = json.loads(response.text)
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无其他动记录')
            else:
                for dictListItem in responseDict['rows']:
                    deleteDict = {'ids':dictListItem['id']} 
                    delete_WorkingRecord(deleteDict)
        #我的资料        
        #删除法律法规资料
        if CommonIntf.getDbQueryResult(dbCommand="select count(*) from MYPROFILES t where t.orgid='%s'" % orgInit['DftWangGeOrgId']) != 0:
            compDict = copy.deepcopy(RiChangBanGongPara.getProfileDict)
            compDict['resourcePoolTypeId']= CommonIntf.getDbQueryResult(dbCommand = "select p.displayseq from propertydicts  p where p.displayname = '法律法规'") 
            response = pinganjianshe_get(url='/resourcePool/myProfileManage/findMyProfileForList.action', param=compDict)  
            responseDict = json.loads(response.text)
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无法律法规资料')
            else:
                for dictListItem in responseDict['rows']:
                    deleteDict = {'ids':dictListItem['id']} 
                    delete_MyProfile(deleteDict)
            #删除规章制度资料
            compDict = copy.deepcopy(RiChangBanGongPara.getProfileDict)
            compDict['resourcePoolTypeId']= CommonIntf.getDbQueryResult(dbCommand = "select p.displayseq from propertydicts  p where p.displayname = '规章制度'") 
            response = pinganjianshe_get(url='/resourcePool/myProfileManage/findMyProfileForList.action', param=compDict)  
            responseDict = json.loads(response.text)
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无规章制度资料')
            else:
                for dictListItem in responseDict['rows']:
                    deleteDict = {'ids':dictListItem['id']} 
                    delete_MyProfile(deleteDict)
            #删除政策文件资料
            compDict = copy.deepcopy(RiChangBanGongPara.getProfileDict)
            compDict['resourcePoolTypeId']= CommonIntf.getDbQueryResult(dbCommand = "select p.displayseq from propertydicts  p where p.displayname = '政策文件'") 
            response = pinganjianshe_get(url='/resourcePool/myProfileManage/findMyProfileForList.action', param=compDict)  
            responseDict = json.loads(response.text)
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无政策文件资料')
            else:
                for dictListItem in responseDict['rows']:
                    deleteDict = {'ids':dictListItem['id']} 
                    delete_MyProfile(deleteDict)
            #删除经验材料资料
            compDict = copy.deepcopy(RiChangBanGongPara.getProfileDict)
            compDict['resourcePoolTypeId']= CommonIntf.getDbQueryResult(dbCommand = "select p.displayseq from propertydicts  p where p.displayname = '经验材料'") 
            response = pinganjianshe_get(url='/resourcePool/myProfileManage/findMyProfileForList.action', param=compDict)  
            responseDict = json.loads(response.text)
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无经验材料资料')
            else:
                for dictListItem in responseDict['rows']:
                    deleteDict = {'ids':dictListItem['id']} 
                    delete_MyProfile(deleteDict)
            #删除调研报告资料
            compDict = copy.deepcopy(RiChangBanGongPara.getProfileDict)
            compDict['resourcePoolTypeId']= CommonIntf.getDbQueryResult(dbCommand = "select p.displayseq from propertydicts  p where p.displayname = '调研报告'") 
            response = pinganjianshe_get(url='/resourcePool/myProfileManage/findMyProfileForList.action', param=compDict)  
            responseDict = json.loads(response.text)
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无调研报告资料')
            else:
                for dictListItem in responseDict['rows']:
                    deleteDict = {'ids':dictListItem['id']} 
                    delete_MyProfile(deleteDict)
            #删除简报资料
            compDict = copy.deepcopy(RiChangBanGongPara.getProfileDict)
            compDict['resourcePoolTypeId']= CommonIntf.getDbQueryResult(dbCommand = "select p.displayseq from propertydicts  p where p.displayname = '简报'") 
            response = pinganjianshe_get(url='/resourcePool/myProfileManage/findMyProfileForList.action', param=compDict)  
            responseDict = json.loads(response.text)
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无简报资料')
            else:
                for dictListItem in responseDict['rows']:
                    deleteDict = {'ids':dictListItem['id']} 
                    delete_MyProfile(deleteDict)
            #删除其他资料
            compDict = copy.deepcopy(RiChangBanGongPara.getProfileDict)
            compDict['resourcePoolTypeId']= CommonIntf.getDbQueryResult(dbCommand = "select p.displayseq from propertydicts  p where p.displayname = '其他'") 
            response = pinganjianshe_get(url='/resourcePool/myProfileManage/findMyProfileForList.action', param=compDict)  
            responseDict = json.loads(response.text)
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无其他资料')
            else:
                for dictListItem in responseDict['rows']:
                    deleteDict = {'ids':dictListItem['id']} 
                    delete_MyProfile(deleteDict)
            #删除宣传教育资料
            compDict = copy.deepcopy(RiChangBanGongPara.getProfileDict)
            compDict['resourcePoolTypeId']= CommonIntf.getDbQueryResult(dbCommand = "select p.displayseq from propertydicts  p where p.displayname = '宣传教育'") 
            response = pinganjianshe_get(url='/resourcePool/myProfileManage/findMyProfileForList.action', param=compDict)  
            responseDict = json.loads(response.text)
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无宣传教育资料')
            else:
                for dictListItem in responseDict['rows']:
                    deleteDict = {'ids':dictListItem['id']} 
                    delete_MyProfile(deleteDict)
                

        #公文管理    ——  当前用社区账号登录（注：不同账号下的发文和收文模块信息不同  ）
        #删除发文信息——>未发送的可删除，已发送的不能删除    
        if CommonIntf.getDbQueryResult(dbCommand="select count(*) from DOCUMENTS t where t.orgid='%s'" % orgInit['DftWangGeOrgId']) != 0:
            compDict = copy.deepcopy(RiChangBanGongPara.getDocumentDict)
            compDict['sidx']= 'createDate'
            response = pinganjianshe_get(url='/documents/dispatchDocumentsManage/dispatchDocumentsList.action', param=compDict) 
            responseDict = json.loads(response.text)
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无可删除的发文信息')
            else:
                for dictListItem in responseDict['rows']:
                    if dictListItem['dispatchState'] == 'sended':
                        Log.LogOutput(LogLevel.DEBUG, '无可删除的发文信息')
                    else:
                        deleteDict = {'deleteIds':dictListItem['id']} 
                        delete_DocumentsManag(deleteDict)
        #删除收文信息——>已签收并且已阅读的收文信息可删除，未签收或者为阅读的收文信息不能删除
        if CommonIntf.getDbQueryResult(dbCommand="select count(*) from DOCUMENTS t where t.orgid='%s'" % orgInit['DftSheQuOrgId']) != 0:
            compDict = copy.deepcopy(RiChangBanGongPara.getDocumentDict)
            compDict['sidx']= 'dispatchDate'  
            response = pinganjianshe_get(url='/documents/receiveDocumentsManage/receiveDocumentsList.action', param=compDict,username=userInit['DftSheQuUser'], password='11111111')  
            responseDict = json.loads(response.text)
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无可删除的收文信息')
            else:
                for dictListItem in responseDict['rows']:
                    if dictListItem['signState'] == 'sign':
                        Log.LogOutput(LogLevel.DEBUG, '无可删除的收文信息')
                    else:
                        deleteDict = {'selectedIds':dictListItem['id']} 
                        delete_Documents(deleteDict)
        #民情日志            
        #删除我的日志               
        if CommonIntf.getDbQueryResult(dbCommand="select count(*) from PEOPLELOG t where t.orgid='%s'" % orgInit['DftWangGeOrgId']) != 0:           
            compDict = copy.deepcopy(RiChangBanGongPara.getLogManageDict)
            response = pinganjianshe_post(url='/peopleLog/peopleLogManage/peopleLogList.action', postdata=compDict)  
            responseDict = json.loads(response.text)
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无我的日志信息')
            else:
                for dictListItem in responseDict['rows']:
                    deleteDict = {'logIds':dictListItem['id']} 
                    delete_logManage(deleteDict) 
        #工作日志            
        #删除工作日志 ——>只能删除类型为‘其他’的工作日志    （注：先搜索类型为其他的事件，在获取当前页面的id信息删除）       
        if CommonIntf.getDbQueryResult(dbCommand="select count(*) from DOCUMENTS t where t.orgid='%s'" % orgInit['DftSheQuOrgId']) != 0:   
            compDict = copy.deepcopy(RiChangBanGongPara.getCommentManageDict)
            response = pinganjianshe_get(url='/dailyLog/workDiaryManage/findWorkDiaryForPageByOrgId.action', param=compDict)  
            responseDict = json.loads(response.text)
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无工作日志信息')
            else:
                compDict = copy.deepcopy(RiChangBanGongPara.searchDiaryObject)
                compDict['searchWorkDiaryVo.organization.id']= orgInit['DftSheQuOrgId']
                compDict['searchWorkDiaryVo.diaryType']= CommonIntf.getDbQueryResult(dbCommand ="select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '工作日志类型') and p.displayname = '其他'" ) 
                response = pinganjianshe_get(url='/dailyLog/searchWorkDiary/searchWorkDiary.action', param=compDict)  
                responseDict01 = json.loads(response.text)
                for dictListItem in responseDict01['rows']:
                    deleteDict = {'selectedIds':dictListItem['id']} 
                    delete_workDiary(deleteDict) 
                                          
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '删除失败')
        return False     
    return True



'''
    @功能： 新增矛盾纠纷排查报表记录清单
    @para: 
    @return: 返回response类
'''    
def addConflictRecord(para,username=userInit['DftSheQuUser'],password='11111111'):
    Log.LogOutput(level=LogLevel.INFO, message='新增矛盾纠纷排查报表记录')
    response = pinganjianshe_post(url='/conflictRpt/conflictRptListManage/addConflictReord.action', postdata=para, username=username, password=password)
    Log.LogOutput(LogLevel.DEBUG,'response.text:'+response.text)
#    responseDict = json.loads(response.text)
    return response.text

'''
    @功能： 新增矛盾纠纷排查报表记录清单
    @para: 
    @return: 返回response类
    @author: chenhui 2016-1-4
'''    
def updConflictRecord(para,username=userInit['DftSheQuUser'],password='11111111'):
    Log.LogOutput(level=LogLevel.INFO, message='修改矛盾纠纷排查报表记录')
    response = pinganjianshe_post(url='/conflictRpt/conflictRptListManage/updateConflictReord.action', postdata=para, username=username, password=password)
    Log.LogOutput(LogLevel.DEBUG,'response.text:'+response.text)
#    responseDict = json.loads(response.text)
    return response.text

'''  
    @功能： 检查测试自动化社区层级矛盾纠纷排查报表新增是否成功
    @para: 
    @return: 如果检查成功，则返回True；否则返回False 
    @author: chenhui 2016-1-4 
'''
def checkConflictRecord(checkPara, listPara, username = userInit['DftSheQuUser'], password = '11111111'):
    Log.LogOutput(LogLevel.DEBUG, "检查新增报表..")
    try:
        response = pinganjianshe_post(url='/conflictRpt/conflictRptListManage/findConflictRptList.action', postdata=listPara,username=username, password = password)  
        responseDict = json.loads(response.text)
#        Log.LogOutput(LogLevel.DEBUG, response.text)
        if responseDict['records']==0:
            Log.LogOutput(LogLevel.DEBUG,'报表数为0，新增失败！')
            return False
        if CommonUtil.findDictInDictlist(checkPara, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到报表信息，新增验证成功！")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到报表信息")
            Log.LogOutput(LogLevel.DEBUG, response.text)
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查报表信息失败")
        return False

'''  
    @功能： 检查测试自动化社区层级矛盾纠纷排查报表修改是否成功
    @para: 
    @return: 如果检查成功，则返回True；否则返回False
    @author: chenhui 2016-1-7  
'''
def checkConflictRecordUpd(checkPara, viewPara, username = userInit['DftSheQuUser'], password = '11111111'):
    Log.LogOutput(LogLevel.DEBUG, "检查修改报表..")
    try:
        response = pinganjianshe_post(url='/conflictRpt/conflictRptDatasManage/getConflictRptDatasType.action', postdata=viewPara,username=username, password = password)  
        responseDict = json.loads(response.text)
#        Log.LogOutput(LogLevel.DEBUG, responseDict)
        if str(responseDict['conflictAnalyZingRpt']['totalSuccNum'])==checkPara['totalSuccNum'] and str(responseDict['conflictRpt']['dealPerson'])==checkPara['dealPerson'] and str(responseDict['conflictRpt']['lister'])==checkPara['lister']:
            Log.LogOutput(message='修改验证成功')
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到报表信息，修改验证失败")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查报表信息失败")
        return False   
'''
    @功能： 新增普通矛盾纠纷排查报表清单
    @para: 
    @return: 返回response类 
    @author: chenhui 2016-1-4
'''    
def addConflictNormal(para,username=userInit['DftSheQuUser'],password='11111111'):
    Log.LogOutput(level=LogLevel.INFO, message='新增普通矛盾纠纷排查报表')
    response = pinganjianshe_post(url='/ConflictRpt/ConflictRptNormalManage/addConflictRptNormal.action', postdata=para, username=username, password=password)
    Log.LogOutput(LogLevel.DEBUG,'response.text:'+response.text)
    responseDict = json.loads(response.text)
    return responseDict

'''
    @功能： 修改普通矛盾纠纷排查报表清单
    @para: 
    @return: 返回response类 
    @author: chenhui 2016-1-4
'''    
def updConflictNormal(para,username=userInit['DftSheQuUser'],password='11111111'):
    Log.LogOutput(level=LogLevel.INFO, message='修改普通矛盾纠纷排查报表')
    response = pinganjianshe_post(url='/ConflictRpt/ConflictRptNormalManage/updateConflictRptNormal.action', postdata=para, username=username, password=password)
    Log.LogOutput(LogLevel.DEBUG,'response.text:'+response.text)
    responseDict = json.loads(response.text)
    return responseDict


'''  
    @功能： 检查测试自动化社区层级普通矛盾纠纷排查报表新增是否成功
    @para: 
    @return: 如果检查成功，则返回True；否则返回False
    @author: chenhui 2016-1-4  
'''
def checkConflictNormal(checkPara, listPara, username = userInit['DftSheQuUser'], password = '11111111'):
    Log.LogOutput(LogLevel.DEBUG, "检查普通报表..")
    try:
        response = pinganjianshe_post(url='/ConflictRpt/ConflictRptNormalManage/conflictRptNormalList.action', postdata=listPara,username=username, password = password)  
        responseDict = json.loads(response.text)
#         Log.LogOutput(LogLevel.DEBUG, responseDict)
        if responseDict['records']==0:
            Log.LogOutput(LogLevel.DEBUG,'报表数为0，新增失败！')
            return False
        if CommonUtil.findDictInDictlist(checkPara, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到普通报表信息，验证成功！")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到普通报表信息")
            Log.LogOutput(LogLevel.DEBUG, response.text)
            return False
    except Exception ,e:
        Log.LogOutput(LogLevel.ERROR, "检查普通报表信息出现异常"+str(e))
        return False   

'''
    @功能： 获取普通矛盾纠纷排查报表清单数量
    @para: 
    @return: num{'add','success'} 
    @author: chenhui 2016-1-4
'''    
def getConflictNormalListNum(para,username=userInit['DftSheQuUser'],password='11111111'):
    num={
         'add':'',
         'success':''
         }
    para['confilictState']='1'
    Log.LogOutput(level=LogLevel.INFO, message='正在获取普通清单新增数和成功数')
    response1 = pinganjianshe_post(url='/ConflictRpt/ConflictRptNormalManage/conflictRptNormalList.action', postdata=para, username=username, password=password)
#    Log.LogOutput(LogLevel.DEBUG,'response.text:'+response1.text)
    responseDict1 = json.loads(response1.text)
    para['confilictState']='2'
    response2 = pinganjianshe_post(url='/ConflictRpt/ConflictRptNormalManage/conflictRptNormalList.action', postdata=para, username=username, password=password)
#    Log.LogOutput(LogLevel.DEBUG,'response.text:'+response2.text)
    responseDict2 = json.loads(response2.text)
    num['add']=responseDict1['records']
    num['success']=responseDict2['records']
    return num

'''  
    @功能： 导入测试自动化社区下的普通矛盾纠纷清单
    @para: 
    @return: ticketId,传递给检查错误接口，然后返回相应错误  
'''
def importConflictRptNormal(data, files=None, username = userInit['DftSheQuUser'], password = '11111111'):
    Log.LogOutput(LogLevel.INFO, "开始导入矛盾纠纷普通清单..")
    response = pinganjianshe_post(url='/dataTransfer/importToDomain.action', postdata=data, files=files, username=username, password = password)   
    #返回非json字符串，需要自己解析 
    #{ticketId:'ec9dde4b-e2bb-4337-87ed-dbe1f231824f',uploadFileName:'conflict_impt.xls',threadId:'2489',errorMessageExcelName:'6b6a9f31-e192-497c-84fa-37acb660d2e5'}
    Log.LogOutput(LogLevel.DEBUG,response.text)
    strlist = response.text.split('\'')
    ticketId= strlist[1]
    return ticketId
    
    '''  
    @功能： 导入测试自动化社区下的普通或者重大矛盾纠纷清单
    @para: 
    @return: ticketId,传递给检查错误接口，然后返回相应错误  
    '''
def getImportConflictRptMsgByTicketId(para,username=userInit['DftSheQuUser'], password = '11111111'):
    Log.LogOutput( message='获取导入操作返回信息')
    response = pinganjianshe_post(url='/ticket/getDataImportTicketByTicketId.action', postdata=para, username=username, password=password)
    responseDict=json.loads(response.text)
    Log.LogOutput(LogLevel.DEBUG,response.text)
    return responseDict
'''
    @功能： 新增重大矛盾纠纷排查报表
    @para: 
    @return: 返回response类 
    @author: chenhui 2016-1-4 
'''    
def addConflictImpt(para,username=userInit['DftSheQuUser'],password='11111111'):
    Log.LogOutput(level=LogLevel.INFO, message='新增重大矛盾纠纷排查报表')
    response = pinganjianshe_post(url='/conflictRpt/conflictRptManage/addConflictRptimpt.action', postdata=para, username=username, password=password)
#    Log.LogOutput(LogLevel.DEBUG,'response.text:'+response.text)
    responseDict = json.loads(response.text)
    return responseDict


'''
    @功能： 修改重大矛盾纠纷排查报表
    @para: 
    @return: 返回response类  
    @author: chenhui 2016-1-7
'''    
def updConflictImpt(para,username=userInit['DftSheQuUser'],password='11111111'):
    Log.LogOutput(level=LogLevel.INFO, message='修改重大矛盾纠纷排查报表')
    response = pinganjianshe_post(url='/conflictRpt/conflictRptManage/editConflictRptimpt.action', postdata=para, username=username, password=password)
    Log.LogOutput(LogLevel.DEBUG,'response.text:'+response.text)
    responseDict = json.loads(response.text)
    return responseDict

'''  
    @功能： 检查测试自动化社区层级重大矛盾纠纷排查报表新增、修改是否成功
    @para: 
    @return: 如果检查成功，则返回True；否则返回False 
    @author: chenhui 2016-1-7 
'''
def checkConflictImpt(checkPara, listPara, username = userInit['DftSheQuUser'], password = '11111111'):
    Log.LogOutput(LogLevel.DEBUG, "检查重大纠纷报表..")
    try:
        response = pinganjianshe_post(url='/conflictRpt/conflictRptManage/findConflictRptimptList.action', postdata=listPara,username=username, password = password)  
        responseDict = json.loads(response.text)
#         Log.LogOutput(LogLevel.DEBUG, responseDict)
        if responseDict['records']==0:
            Log.LogOutput(LogLevel.DEBUG,'报表数为0，新增失败！')
            return False
        if CommonUtil.findDictInDictlist(checkPara, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到重大报表信息，验证成功！")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到重大报表信息")
            Log.LogOutput(LogLevel.DEBUG, response.text)
            return False
    except Exception,e:
        Log.LogOutput(LogLevel.ERROR, "检查重大报表信息出现异常"+str(e))
        Log.LogOutput(LogLevel.ERROR, response.text)
        return False   
    
'''  
    @功能： 导入测试自动化社区下的重大矛盾纠纷清单
    @para: 
    @return: ticketId,传递给检查错误接口，然后返回相应错误  
'''
def importConflictRptImpt(data, files=None, username = userInit['DftSheQuUser'], password = '11111111'):
    Log.LogOutput(LogLevel.INFO, "开始导入矛盾纠纷重大清单..")
    response = pinganjianshe_post(url='/dataTransfer/importToDomain.action', postdata=data, files=files, username=username, password = password)   
    #返回非json字符串，需要自己解析 
    #{ticketId:'ec9dde4b-e2bb-4337-87ed-dbe1f231824f',uploadFileName:'conflict_impt.xls',threadId:'2489',errorMessageExcelName:'6b6a9f31-e192-497c-84fa-37acb660d2e5'}
    Log.LogOutput(LogLevel.DEBUG,response.text)
    strlist = response.text.split('\'')
    ticketId= strlist[1]
    return ticketId

'''  
    @功能： 获取重大清单统计数据
    @para: 
    @return: responseDict  
'''
def getConflictRptImptDataCount(para,username = userInit['DftSheQuUser'], password = '11111111'):
    response = pinganjianshe_post(url='/conflictRpt/conflictRptDatasManage/getSelfConflictRptImptCount.action', postdata=para,username=username, password = password)
    responseDict=json.loads(response.text)
    return responseDict

'''  
    @功能： 获取下个月的新增记录表页面年度累计默认数据
    @para: 
    @return: responseDict  
'''
def getConflictRptDataByYear(para,username = userInit['DftSheQuUser'], password = '11111111'):
    Log.LogOutput(message='获取社区新增二月份报表时年度累计默认数据')
    response = pinganjianshe_post(url='/conflictRpt/conflictRptDatasManage/getConflictRptDatasType.action', postdata=para,username=username, password = password)
    responseDict=json.loads(response.text)
    return responseDict['conflictRptDataList']

'''  
    @功能： 获取同月街道层级的新增记录表页面年度累计默认数据
    @para: 
    @return: responseDict  
'''
def getConflictRptDataByYear2(para,username = userInit['DftJieDaoUser'], password = '11111111'):
    Log.LogOutput(message='获取街道新增一月份报表时年度累计默认数据')
    response = pinganjianshe_post(url='/conflictRpt/conflictRptDatasManage/getJurisdictionDatas.action', postdata=para,username=username, password = password)
#    print response.text
    responseDict=json.loads(response.text)
    return responseDict

'''  
    @功能： 获取2016年1月社区层级的新增记录表页面总况默认数据
    @para: 
    @return: responseDict  
'''
def getConflictRptDatasType(para,username = userInit['DftSheQuUser'], password = '11111111'):
    Log.LogOutput(message='获取社区运行事件job后，新增一月份报表时年度累计默认数据')
    response = pinganjianshe_post(url='/conflictRpt/conflictRptDatasManage/getConflictRptDatasType.action', postdata=para,username=username, password = password)
    responseDict=json.loads(response.text)
#    Log.LogOutput(message=response.text)
    return responseDict


'''  
    @功能： 删除普通矛盾纠纷报表
    @para: 
    @return: 如果检查成功，则返回True；否则返回False  
    @author: chenhui 2016-1-6
'''
def delConflictNormal(listPara, username = userInit['DftSheQuUser'], password = '11111111'):
    #首先通过列表接口获取ids
    response1 = pinganjianshe_post(url='/ConflictRpt/ConflictRptNormalManage/conflictRptNormalList.action', postdata=listPara,username=username, password = password)
    responseDict1 = json.loads(response1.text)
    rows=responseDict1['rows']
    Log.LogOutput(LogLevel.DEBUG, responseDict1)
    if responseDict1['records']==0:
        Log.LogOutput('列表中无数据,无需删除')
        return False
    delPara=copy.deepcopy(conflictRptNormalDelPara)
    delPara['ids']=rows[0]['id']
    delPara['yearDate']=listPara['yearDate']
    delPara['reportTime']=listPara['reportTime']
    Log.LogOutput(message='正在删除普通报表数据')
    response2=pinganjianshe_post(url='/ConflictRpt/ConflictRptNormalManage/deleteConflictRptNormal.action', postdata=delPara,username=username, password = password)
    return response2.result

'''  
    @功能： 检查普通矛盾纠纷报表是否删除成功
    @para: 
    @return: 如果检查成功，则返回True；否则返回False  
    @author: chenhui 2016-1-6
'''
def checkConflictNormalDel(listPara, username = userInit['DftSheQuUser'], password = '11111111'):
    Log.LogOutput(LogLevel.DEBUG, "检查删除普通报表..")
    try:
        response = pinganjianshe_post(url='/ConflictRpt/ConflictRptNormalManage/conflictRptNormalList.action', postdata=listPara,username=username, password = password)  
        responseDict = json.loads(response.text)
#        Log.LogOutput(LogLevel.DEBUG, responseDict)
        if responseDict['records']==0:
            Log.LogOutput(LogLevel.DEBUG,'报表数为0，删除成功！')
            return True
        else:
            return False
    except Exception,e:
        Log.LogOutput(LogLevel.ERROR, "获取普通矛盾纠纷列表接口出现异常"+str(e))
        return False   

'''
    @功能： 获取普通矛盾纠纷排查报表清单数量
    @para: 
    @return: num{'add','success'} 
    @author: chenhui 2016-1-4
'''    
def getConflictImptListNum(para,username=userInit['DftSheQuUser'],password='11111111'):
    num={
         'add':'',
         'success':''
         }
    para['conflictRptImpt.status']='1'#新增
    Log.LogOutput(level=LogLevel.INFO, message='正在获取重大清单新增数和成功数')
    response1 = pinganjianshe_post(url='/conflictRpt/conflictRptManage/findConflictRptimptList.action', postdata=para, username=username, password=password)
#    Log.LogOutput(LogLevel.DEBUG,'response.text:'+response1.text)
    responseDict1 = json.loads(response1.text)
    para['conflictRptImpt.status']='2'#化解
    response2 = pinganjianshe_post(url='/conflictRpt/conflictRptManage/findConflictRptimptList.action', postdata=para, username=username, password=password)
#    Log.LogOutput(LogLevel.DEBUG,'response.text:'+response2.text)
    responseDict2 = json.loads(response2.text)
    num['add']=responseDict1['records']
    num['success']=responseDict2['records']
    return num
  
'''  
    @功能： 删除重大矛盾纠纷报表
    @para: 
    @return: 如果检查成功，则返回True；否则返回False 
    @author: chenhui 2016-1-6 
'''
def delConflictImpt(para, username = userInit['DftSheQuUser'], password = '11111111'):
    response=pinganjianshe_post(url='/conflictRpt/conflictRptManage/deleteConflictRptimpt.action', postdata=para,username=username, password = password)
    Log.LogOutput(LogLevel.DEBUG, response.text)
    
'''  
    @功能： 检查重大矛盾纠纷报表是否删除成功
    @para: 
    @return: 如果检查成功，则返回True；否则返回False  
    @author: chenhui 2016-1-6
'''
def checkConflictImptDel(para, username = userInit['DftSheQuUser'], password = '11111111'):
    Log.LogOutput(LogLevel.DEBUG, "检查删除重大报表..")
    try:
        response = pinganjianshe_post(url='/conflictRpt/conflictRptManage/findConflictRptimptList.action', postdata=para,username=username, password = password)  
        responseDict = json.loads(response.text)
        Log.LogOutput(LogLevel.DEBUG, responseDict)
        if responseDict['records']==0:
            Log.LogOutput(LogLevel.DEBUG,'报表数为0，删除成功！')
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG,'报表数为'+str(responseDict['records'])+'，删除失败！')
            return False
    except Exception,e:
        Log.LogOutput(LogLevel.ERROR, "验证删除时出现异常"+str(e))
        return False      
    
'''  
    @功能： 删除矛盾纠纷记录
    @para: 
    @return: 如果检查成功，则返回True；否则返回False
    @author: chenhui 2016-1-6  
'''
def delConflictRecord(para, username = userInit['DftSheQuUser'], password = '11111111'):
    response=pinganjianshe_post(url='/conflictRpt/conflictRptListManage/deleteConflictRpt.action', postdata=para,username=username, password = password)
    Log.LogOutput(LogLevel.DEBUG, response.text)

'''  
    @功能： 检查删除矛盾纠纷排查报表记录是否成功
    @para: 
    @return: 如果检查成功，则返回True；否则返回False  
    @author: chenhui 2016-1-7
'''
def checkConflictRecordDel(para, username = userInit['DftSheQuUser'], password = '11111111'):
    Log.LogOutput(LogLevel.DEBUG, "检查删除报表记录..")
    try:
        response = pinganjianshe_post(url='/conflictRpt/conflictRptListManage/findConflictRptList.action', postdata=para,username=username, password = password)  
        responseDict = json.loads(response.text)
        Log.LogOutput(LogLevel.DEBUG, responseDict)
        if responseDict['records']==0:
            Log.LogOutput(LogLevel.DEBUG,'报表记录数为0，删除成功！')
            return True
        else:
            return False
    except Exception,e:
        Log.LogOutput(LogLevel.ERROR, "验证删除时出现异常"+str(e))
        return False   
    

'''  
    @功能： 从数据库清空所有报表的数据
    @para: 
    @return:   
    @author: chenhui 2016-1-6
'''    
def deleteAllReport():
    #清空2016年每个月的8张表
    for i in range(1,13):
#         if getDbQueryResult(dbCommand="select count(*) from conflictRptRecord c where c.month='%d'"%i )!=0:
        clearTable(tableName='ConflictRptnormal_2016_'+str(i))
        clearTable(tableName='CONFLICTRPTIMPT_2016_'+str(i))
        clearTable(tableName='CONFLICTRPT_2016_'+str(i))
        clearTable(tableName='CONFLICTRPTDATAS_2016_'+str(i))
        clearTable(tableName='CONFLICTRPT_JOB_2016_'+str(i))
        clearTable(tableName='CONFLICTRPTDATAS_JOB_2016_'+str(i))
        clearTable(tableName='CONFLICTRPTNORMAL_JOB_2016_'+str(i))
        clearTable(tableName='CONFLICTRPTIMPT_JOB_2016_'+str(i))
    #最后清除记录表
    clearTable(tableName='conflictRptRecord')
    #清空社会治安重点地区排查整治清单表数据
    clearTable(tableName='keyAreasOfInvestigationInfos')
    clearTable(tableName='keyAreasAttachFiles')
    #清空季报
    clearTable(tableName='workingRecords')
'''  
    @功能： 初始化日常办公表结构
    @para: 2016_1 2016_2
    @return:   True / False
    @author: chenhui 2016-2-1
'''    
def initTable(year_mon):
    #CONFLICTRPTNORMAL_2016_1
    if getDbQueryResult(dbCommand="select count(*) from user_tables u where u.TABLE_NAME='CONFLICTRPTNORMAL_%s'"%year_mon)==0:
        sql1='create table ConflictRptnormal_%s'%year_mon+'''
        (
          id                  number(10) primary key not null,
          issueid             number(10),    
          createorgcode            varchar2(32) not null,
          delorgcode               varchar2(32) ,
          name                varchar2(150) not null,
          delsign           number(1) default 0,
          state               number(10) not null,
          type                number(10) not null,
          recorddate           date,
          dealdate            date,
          departmentandperson varchar2(500),
          createdate          date,
          createuser          varchar2(32),
          updatedate          date,
          updateuser          varchar2(32),
          reportAfterOrgLevel NUMBER(10)
        )
        
        '''
        exeDbQuery(dbCommand=sql1)
        #CONFLICTRPTIMPT_2016_1
    if getDbQueryResult(dbCommand="select count(*) from user_tables u where u.TABLE_NAME='CONFLICTRPTIMPT_%s'"%year_mon)==0:   
        sql2='create table CONFLICTRPTIMPT_%s'%year_mon+"""
        (
          ID               NUMBER(10) not null,
          ORGID            NUMBER(10) not null,
          ORGINTERNALCODE  VARCHAR2(32) not null,
          issueId        number(10),
          STATUS           NUMBER(10) not null,
          DISPUTESTYPE     VARCHAR2(500) not null,
          INVOLVESITUATION VARCHAR2(300) not null,
          BASICSITUATION   VARCHAR2(3000) not null,
          ONDUTYTARGET     VARCHAR2(3000),
          WORKINGMEASURE   VARCHAR2(3000) ,
          DEVELOPSITUATION VARCHAR2(3000) ,
          CREATEUSER       VARCHAR2(32) not null,
          UPDATEUSER       VARCHAR2(32),
          CREATEDATE       DATE not null,
          UPDATEDATE       DATE,
          DELORGCODE       VARCHAR2(32),
          DELSIGN          NUMBER(1) DEFAULT 0,
          reportAfterOrgLevel NUMBER(10),
          constraint pkCONFLICTRPTIMPT_"""+'%s primary key  (id))'%year_mon
        exeDbQuery(dbCommand=sql2)
    #CONFLICTRPT_2016_1
    if getDbQueryResult(dbCommand="select count(*) from user_tables u where u.TABLE_NAME='CONFLICTRPT_%s'"%year_mon)==0:
        sql3='create table CONFLICTRPT_%s'%year_mon+"""
        (
          id                  NUMBER(10) not null,
          orgid               NUMBER(10) not null,
          orgcode             VARCHAR2(32) not null,
          name                VARCHAR2(100),
          submitstate         NUMBER(10) default 0 not null,
          submittime          DATE,
          backtime            DATE,
          lister              VARCHAR2(60),
          dealperson          VARCHAR2(60),
          createuser          VARCHAR2(30) not null,
          updateuser          VARCHAR2(32),
          createdate          DATE not null,
          updatedate          DATE,
          expiredentering     NUMBER(1) default 0,
          num_0_50            NUMBER(10),
          num_50_100          NUMBER(10),
          num_100_500         NUMBER(10),
          num_500_            NUMBER(10),
          urgereport          NUMBER(10) default 0 not null,
          reportdatavalidate  NUMBER(10) default 0 not null,
          year_num_0_50       NUMBER(10),
          year_num_50_100     NUMBER(10),
          year_num_100_500    NUMBER(10),
          year_num_500_       NUMBER(10),
          totalsuccnum        NUMBER(10),
          totalsuccnum_year   NUMBER(10),
          urgereportdate      DATE,
          dailyyearid         NUMBER(10),
          newdailydirectoryid NUMBER(10),
          yeartotalpc         NUMBER(10),
          yeartotaltc         NUMBER(10),
          yeartotalcl         NUMBER(10),
          totalpc             NUMBER(10),
          totaltc             NUMBER(10),
          totalcl             NUMBER(10),
          centralizedDetection NUMBER(10) default 0,
          yearCentralizedDetection NUMBER(10) default 0,
          district_totalpc              NUMBER(10) default 0,
          district_totaltc              NUMBER(10) default 0,
          district_totalcl              NUMBER(10) default 0,
          district_totalsucc            NUMBER(10) default 0,
          town_totalpc                  NUMBER(10) default 0,
          town_totaltc                  NUMBER(10) default 0,
          town_totalcl                  NUMBER(10) default 0,
          town_totalsucc                NUMBER(10) default 0,
          village_totalpc               NUMBER(10) default 0,
          village_totaltc               NUMBER(10) default 0,
          village_totalcl               NUMBER(10) default 0,
          village_totalsucc             NUMBER(10) default 0,
          district_num_0_50             NUMBER(10) default 0,
          district_num_50_100           NUMBER(10) default 0,
          district_num_100_500          NUMBER(10) default 0,
          district_num_500_             NUMBER(10) default 0,
          town_num_0_50                 NUMBER(10) default 0,
          town_num_50_100               NUMBER(10) default 0,
          town_num_100_500              NUMBER(10) default 0,
          town_num_500_                 NUMBER(10) default 0,
          village_num_0_50              NUMBER(10) default 0,
          village_num_50_100            NUMBER(10) default 0,
          village_num_100_500           NUMBER(10) default 0,
          village_num_500_              NUMBER(10) default 0,
          district_centralizeddetection NUMBER(10) default 0,
          town_centralizeddetection     NUMBER(10) default 0,
          village_centralizeddetection  NUMBER(10) default 0,
          constraint pkCONFLICTRPT_"""+'%s primary key  (id))'%year_mon
        exeDbQuery(dbCommand=sql3)
    #CONFLICTRPTDATAS_2016_1
    if getDbQueryResult(dbCommand="select count(*) from user_tables u where u.TABLE_NAME='CONFLICTRPTDATAS_%s'"%year_mon)==0:
        sql4='create table CONFLICTRPTDATAS_%s'%year_mon+"""
        (
          id               NUMBER(10) not null,
          conflictrptid    NUMBER(10) not null,
          investigationnum NUMBER(10),
          mediationnum     NUMBER(10),
          inventorynum     NUMBER(10) default 0,
          successnum       NUMBER(10) default 0,
          conflicttype     NUMBER(10),
          orgcode          VARCHAR2(32) not null,
          orglevel         NUMBER(10) not null,
          isimpt           NUMBER(10) default 0,
          yearnumpc        NUMBER(10),
          yearnumtc        NUMBER(10),
          yearnumsucc      NUMBER(10) default 0,
          yearnumcl        NUMBER(10) default 0,
          constraint pkCONFLICTRPTDATAS_"""+'%s primary key  (id))'%year_mon
        exeDbQuery(dbCommand=sql4)
    #CONFLICTRPT_JOB_2016_1
    if getDbQueryResult(dbCommand="select count(*) from user_tables u where u.TABLE_NAME='CONFLICTRPT_JOB_%s'"%year_mon)==0:
        sql5='create table CONFLICTRPT_JOB_%s'%year_mon+"""
        (
          id                NUMBER(10) not null,
          orgid             NUMBER(10) not null,
          orgcode           VARCHAR2(32) not null,
          name              VARCHAR2(100),
          createuser        VARCHAR2(30) not null,
          updateuser        VARCHAR2(32),
          createdate        DATE not null,
          updatedate        DATE,
          num_0_50          NUMBER(10),
          num_50_100        NUMBER(10),
          num_100_500       NUMBER(10),
          num_500_          NUMBER(10),
          year_num_0_50     NUMBER(10),
          year_num_50_100   NUMBER(10),
          year_num_100_500  NUMBER(10),
          year_num_500_     NUMBER(10),
          totalsuccnum      NUMBER(10),
          totalsuccnum_year NUMBER(10),
            constraint pkCONFLICTRPT_JOB_"""+'%s primary key  (id))'%year_mon
        exeDbQuery(dbCommand=sql5)
    #CONFLICTRPTDATAS_JOB_2016_1
    if getDbQueryResult(dbCommand="select count(*) from user_tables u where u.TABLE_NAME='CONFLICTRPTDATAS_JOB_%s'"%year_mon)==0:
        sql6='create table CONFLICTRPTDATAS_JOB_%s'%year_mon+"""
        (
          id               NUMBER(10) not null,
          conflictrptid    NUMBER(10) not null,
          investigationnum NUMBER(10),
          mediationnum     NUMBER(10),
          inventorynum     NUMBER(10),
          successnum       NUMBER(10),
          yearaccumulative NUMBER(10),
          conflicttype     VARCHAR2(100),
          orgcode          VARCHAR2(32),
          orglevel         NUMBER(10),
           constraint pkCONFLICTRPTDATAS_JOB_"""+'%s primary key  (id))'%year_mon
        exeDbQuery(dbCommand=sql6)   
    #CONFLICTRPTNORMAL_JOB_2016_1
    if getDbQueryResult(dbCommand="select count(*) from user_tables u where u.TABLE_NAME='CONFLICTRPTNORMAL_JOB_%s'"%year_mon)==0:
        sql7='create table CONFLICTRPTNORMAL_JOB_%s'%year_mon+"""
        (
          id            NUMBER(10) not null,
          issueid       NUMBER(10),
          createorgcode VARCHAR2(32) not null,
          name          VARCHAR2(150) not null,
          state         NUMBER(10) not null,
          type          NUMBER(10) not null,
          orglevel      NUMBER(10),
          recorddate    DATE,
          createdate    DATE,
          createuser    VARCHAR2(32),
          updatedate    DATE,
          updateuser    VARCHAR2(32),
          issuecreatedate  date,
          issuelastdealdate  date,
          constraint pkCONFLICTRPTNORMAL_"""+'%s primary key  (id))'%year_mon
        exeDbQuery(dbCommand=sql7) 
    #CONFLICTRPTIMPT_JOB_2016_1
    if getDbQueryResult(dbCommand="select count(*) from user_tables u where u.TABLE_NAME='CONFLICTRPTIMPT_JOB_%s'"%year_mon)==0:
        sql8='create table CONFLICTRPTIMPT_JOB_%s'%year_mon+"""
        (
          id            NUMBER(10) not null,
          issueid       NUMBER(10),
          createorgcode VARCHAR2(32) not null,
          name          VARCHAR2(150) not null,
          state         NUMBER(10) not null,
          type          NUMBER(10) not null,
          orglevel      NUMBER(10),
          recorddate    DATE,
          createdate    DATE,
          createuser    VARCHAR2(32),
          updatedate    DATE,
          updateuser    VARCHAR2(32),
          issuecreatedate  date,
          issuelastdealdate  date,
          constraint pkCONFLICTRPTIMPT_JOB_"""+'%s primary key  (id))'%year_mon
        exeDbQuery(dbCommand=sql8)
    
    
'''  
    @功能： 上报矛盾纠纷记录
    @para: 
    @return: 如果检查成功，则返回True；否则返回False
    @author: chenhui 2016-1-6  
'''
def reportConflictRecord(para, username = userInit['DftSheQuUser'], password = '11111111'):
    Log.LogOutput(LogLevel.DEBUG, "上报矛盾纠纷报表月报记录..")
    response=pinganjianshe_post(url='/conflictRpt/conflictRptListManage/reportedConflictReport.action', postdata=para,username=username, password = password)
    Log.LogOutput(LogLevel.DEBUG, response.text)    
    return response
    
    
'''  
    @功能： 回退矛盾纠纷记录
    @para: 
    @return: 如果检查成功，则返回True；否则返回False
    @author: chenhui 2016-1-6  
'''
def backConflictRecord(para, username = userInit['DftJieDaoUser'], password = '11111111'):
    Log.LogOutput(LogLevel.DEBUG, "回退矛盾纠纷报表月报记录..")
    response=pinganjianshe_post(url='/daily/socialConflictReordManage/reportBack.action', postdata=para,username=username, password = password)
    Log.LogOutput(LogLevel.DEBUG, response.text)    
    return response    
    
    
'''  
    @功能： 检查矛盾纠纷排查报表记录是否上报成功
    @para: 
    @return: 返回上报状态码，0表示未上报，1表示已上报，2表示已回退  
    @author: chenhui 2016-1-7
'''
def checkReportRecord(listPara, username = userInit['DftSheQuUser'], password = '11111111'):
    Log.LogOutput(LogLevel.DEBUG, "验证上报报表状态..")
    try:
        response = pinganjianshe_post(url='/conflictRpt/conflictRptListManage/findConflictRptList.action', postdata=listPara,username=username, password = password)  
        responseDict = json.loads(response.text)
#        Log.LogOutput(LogLevel.DEBUG, response.text)
        if responseDict['rows'][0]['submitState']==1:
            Log.LogOutput(message="检测到上报状态为'已上报'") 
            return 1
        if responseDict['rows'][0]['submitState']==2:
            Log.LogOutput(message="检测到上报状态为'已回退'") 
            return 2
        if responseDict['rows'][0]['submitState']==0:
            Log.LogOutput(message="检测到上报状态为'未上报'") 
            return 0
    except Exception,e:
        Log.LogOutput(LogLevel.ERROR, "验证时出现异常"+str(e))
        Log.LogOutput(LogLevel.ERROR, response.text) 
        return None
    
'''
    @功能： 新增社会治安重点地区排查整治清单
    @para: 
    @return: 返回response类 
    @author: chenhui 2016-1-18
'''    
def addSocialSecurit(para,username=userInit['DftSheQuUser'],password='11111111'):
    Log.LogOutput(level=LogLevel.INFO, message='新增社会治安重点地区排查整治清单')
    response = pinganjianshe_post(url='/daily/keyAreasOfInvestigationInfoManage/addKeyAreasOfInvestigationInfo.action', postdata=para, username=username, password=password)
#    Log.LogOutput(LogLevel.DEBUG,'response.text:'+response.text)
    responseDict = json.loads(response.text)
    return responseDict

'''
    @功能： 修改社会治安重点地区排查整治清单
    @para: 
    @return: 返回response类 
    @author: chenhui 2016-1-18
'''    
def updSocialSecurit(para,username=userInit['DftSheQuUser'],password='11111111'):
    Log.LogOutput(level=LogLevel.INFO, message='修改社会治安重点地区排查整治清单')
    response = pinganjianshe_post(url='/daily/keyAreasOfInvestigationInfoManage/editKeyAreasOfInvestigationInfo.action', postdata=para, username=username, password=password)
#    Log.LogOutput(LogLevel.DEBUG,'response.text:'+response.text)
    responseDict = json.loads(response.text)
    return responseDict


'''
    @功能： 删除社会治安重点地区排查整治清单
    @para: 
    @return: 返回response类 
    @author: chenhui 2016-1-18
'''    
def delSocialSecurit(para,username=userInit['DftSheQuUser'],password='11111111'):
    Log.LogOutput(level=LogLevel.INFO, message='删除社会治安重点地区排查整治清单')
    response = pinganjianshe_post(url='/daily/keyAreasOfInvestigationInfoManage/deleteKeyAreasOfInvestigationInfoById.action', postdata=para, username=username, password=password)
    Log.LogOutput(LogLevel.DEBUG,'response.text:'+response.text)
    return response


'''  
    @功能： 检查测试自动化社区层级社会治安重点地区排查整治清单新增、修改功能
    @para: 
    @return: 如果检查成功，则返回True；否则返回False 
    @author: chenhui 2016-1-18 
'''
def checkSocialSecurit(checkPara, listPara, username = userInit['DftSheQuUser'], password = '11111111'):
    Log.LogOutput(LogLevel.DEBUG, "检查社会治安重点地区排查整治清单列表数据..")
    try:
        response = pinganjianshe_post(url='/daily/keyAreasOfInvestigationInfoManage/findKeyAreasOfInvestigationInfos.action', postdata=listPara,username=username, password = password)  
        responseDict = json.loads(response.text)
#        Log.LogOutput(LogLevel.DEBUG, responseDict)
        if responseDict['records']==0:
            Log.LogOutput(LogLevel.DEBUG,'报表数为0，检查数据失败！')
            return False
        if CommonUtil.findDictInDictlist(checkPara, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到数据，验证成功！")
            return True
        else:
            Log.LogOutput(LogLevel.ERROR, "未检查到数据，验证失败！")
            return False
    except Exception,e:
        Log.LogOutput(LogLevel.ERROR, "检查报表信息出现异常"+str(e))
        return False 
    
'''  
    @功能： 上报社会治安重点地区排查整治清单
    @para: 
    @return: 如果检查成功，则返回True；否则返回False 
    @author: chenhui 2016-1-18 
'''
def reportSocialSecurit(para, username = userInit['DftSheQuUser'], password = '11111111'):
    Log.LogOutput(LogLevel.DEBUG, "上报社会治安重点地区排查整治清单..")
    response=pinganjianshe_post(url='/daily/keyAreasOfInvestigationInfoManage/reportedKeyAreasOfInvestigationInfoById.action', postdata=para,username=username, password = password)
#    Log.LogOutput(LogLevel.DEBUG, response.text)    
    return response

'''  
    @功能： 回退社会治安重点地区排查整治清单
    @para: 
    @return: 如果检查成功，则返回True；否则返回False 
    @author: chenhui 2016-1-18 
'''
def backSocialSecurit(para, username = userInit['DftSheQuUser'], password = '11111111'):
    Log.LogOutput(LogLevel.DEBUG, "回退社会治安重点地区排查整治清单..")
    response=pinganjianshe_post(url='/daily/keyAreasOfInvestigationInfoManage/backKeyAreasOfInvestigationInfo.action', postdata=para,username=username, password = password)
#    Log.LogOutput(LogLevel.DEBUG, response.text)    
    return response

'''
    @功能： 新增社会治安重点地区排查整治季报
    @para: 
    @return: 返回response类 
    @author: chenhui 2016-1-18
'''    
def addSocialSecuritRpt(para,username=userInit['DftSheQuUser'],password='11111111'):
    Log.LogOutput(level=LogLevel.INFO, message='新增社会治安重点地区排查整治季报')
    response = pinganjianshe_post(url='/workingRecord/societyInvestigationRemediationManage/addSocietyInvestigationRemediation.action', postdata=para, username=username, password=password)
#    Log.LogOutput(LogLevel.DEBUG,'response.text:'+response.text)
    responseDict = json.loads(response.text)
    return responseDict

'''
    @功能： 修改社会治安重点地区排查整治季报
    @para: 
    @return: 返回response类 
    @author: chenhui 2016-1-18
'''    
def updSocialSecuritRpt(para,username=userInit['DftSheQuUser'],password='11111111'):
    Log.LogOutput(level=LogLevel.INFO, message='修改社会治安重点地区排查整治季报')
    response = pinganjianshe_post(url='/workingRecord/societyInvestigationRemediationManage/updateSocietyInvestigationRemediation.action', postdata=para, username=username, password=password)
#    Log.LogOutput(LogLevel.DEBUG,'response.text:'+response.text)
    responseDict = json.loads(response.text)
    return responseDict

'''
    @功能： 删除社会治安重点地区排查整治季报
    @para: 
    @return: 返回response类 
    @author: chenhui 2016-2-2
'''    
def delSocialSecuritRpt(para,username=userInit['DftSheQuUser'],password='11111111'):
    Log.LogOutput(level=LogLevel.INFO, message='删除社会治安重点地区排查整治季报')
    response = pinganjianshe_post(url='/workingRecord/societyInvestigationRemediationManage/deleteSocietyInvestigationRemediation.action', postdata=para, username=username, password=password)
#    Log.LogOutput(LogLevel.DEBUG,'response.text:'+response.text)
    responseDict = json.loads(response.text)
    return responseDict

'''  
    @功能： 上报社会治安重点地区排查整治清单
    @para: 
    @return: 如果检查成功，则返回True；否则返回False 
    @author: chenhui 2016-1-18 
'''
def reportSocialSecuritRpt(para, username = userInit['DftSheQuUser'], password = '11111111'):
    Log.LogOutput(LogLevel.DEBUG, "上报社会治安重点地区排查整治季报..")
    response=pinganjianshe_post(url='/workingRecord/societyInvestigationRemediationManage/reportSocietyInvestigationRemediation.action', postdata=para,username=username, password = password)
    responseDict=json.loads(response.text)    
    return responseDict

'''  
    @功能： 回退社会治安重点地区排查整治季报
    @para: 
    @return: 如果检查成功，则返回True；否则返回False 
    @author: chenhui 2016-2-2
'''
def backSocialSecuritRpt(para, username = userInit['DftJieDaoUser'], password = '11111111'):
    Log.LogOutput(LogLevel.DEBUG, "回退社会治安重点地区排查整治季报..")
    response=pinganjianshe_post(url='/daily/socialConflictReordManage/reportBack.action', postdata=para,username=username, password = password)
#    Log.LogOutput(LogLevel.DEBUG, response.text) 
    responseDict=json.loads(response.text)
    return responseDict

'''  
    @功能： 检查季报新增、修改功能
    @para: 
    @return: 如果检查成功，则返回True；否则返回False 
    @author: chenhui 2016-2-2 
'''
def checkSocialSecuritRpt(checkPara, listPara, username = userInit['DftSheQuUser'], password = '11111111'):
    Log.LogOutput(LogLevel.DEBUG, "检查社会治安重点地区排查整治季报列表数据..")
    try:
        response = pinganjianshe_post(url='/workingRecord/societyInvestigationRemediationManage/societyInvestigationRemediationList.action', postdata=listPara,username=username, password = password)  
        responseDict = json.loads(response.text)
#        Log.LogOutput(LogLevel.DEBUG, responseDict)
        if responseDict['records']==0:
            Log.LogOutput(LogLevel.DEBUG,'报表数为0，检查数据失败！')
            return False
        if CommonUtil.findDictInDictlist(checkPara, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到数据！")
            return True
        else:
            Log.LogOutput(LogLevel.ERROR, "未检查到数据！")
            return False
    except Exception,e:
        Log.LogOutput(LogLevel.ERROR, "检查报表信息出现异常"+str(e))
        return False 
    
'''  
    @功能： 获取街道新增默认数据
    @para: 
    @return: 如果检查成功，则返回True；否则返回False 
    @author: chenhui 2016-2-2 
'''
def getSocialSecuritRptDataByReportTime(para, username = userInit['DftJieDaoUser'], password = '11111111'):
    Log.LogOutput(LogLevel.DEBUG, "获取街道层级社会治安重点地区排查整治季报新增默认数据..")
    response=pinganjianshe_post(url='/workingRecord/societyInvestigationRemediationManage/getSocietyInvestigationRemediationByReportTime.action', postdata=para,username=username, password = password)
    responseDict=json.loads(response.text)
    return responseDict

'''
    @功能：获取Job当前状态，0代表关闭，1代表开启
    @para:           
    @return:0/1
    @author:  chenhui 2016-01-20
'''  
def getJobState (listPara,jobname,username=userInit['DftQuUser'],password='11111111'):
    Log.LogOutput(message='正在获取JOB状态...')
    response=pinganjianshe_get(url='/task/taskManage/taskList.action',param=listPara,username=username,password=password)
    responseDict=json.loads(response.text)
    for item in responseDict['rows']:
        if item['name']==jobname:
            Log.LogOutput(LogLevel.DEBUG,message='查找到job,返回job状态为:'+str(item['closed']))
            return item['closed']
    Log.LogOutput(LogLevel.ERROR,message='没有找到JOB')
'''
    @功能：Job设置时间并重新启动
    @para:           
    @return:true/false
    @author:  chenhui 2015-01-20
'''  
def runJob (jobPara,username=userInit['DftSheQuUser'],password='11111111'):
    Log.LogOutput( message='设置job执行时间')
    try:
        #获取该JOB在task表中的id
        taskId=getDbQueryResult(dbCommand = "select id from task t where t.name='%s'"%jobPara['task.name'])
        taskGroup=getDbQueryResult(dbCommand = "select TASKGROUP from task t where t.name='%s'"%jobPara['task.name'])
        taskDescription=getDbQueryResult(dbCommand = "select description from task t where t.name='%s'"%jobPara['task.name'])
        if taskId is None or taskGroup is None or taskDescription is None:
            Log.LogOutput(LogLevel.ERROR, '该JOB在数据库中不存在！请联系开发人员添加sql!!!')
            return False
        
        #如果该job没有关闭，则关闭该job
        jobListPara={
                    'rows':200,
                    'page':1,
                    'sidx':'id',
                    'sord':'desc',
                     }
        jobPara1={
                   'task.id':taskId,
                   'task.closed':'0'
                   }
        #0代表关闭，1代表开启，如果是开启状态，则关闭
        if getJobState(listPara=jobListPara,jobname=jobPara['task.name'])==1:
            Log.LogOutput(message='该job处于开启状态，先关闭job')
            response1=pinganjianshe_get(url='/task/taskManage/changeTask.action',param=jobPara1,username=username,password=password)
            if response1.result is True:
                Log.LogOutput(message='关闭job成功！')
            else:
                Log.LogOutput(LogLevel.ERROR,message='关闭job失败!')
#            Log.LogOutput(LogLevel.DEBUG,response1.text)
        #修改job时间
        Log.LogOutput(message='修改job时间')
        jobPara2=copy.deepcopy(jobPara1)
        jobPara2['task.name']=jobPara['task.name']
        jobPara2['task.taskGroup']=taskGroup
        jobPara2['task.taskPloy.id']=taskId
        #修改job运行时间
        jobPara2['task.Data']=jobPara['task.Data']
        jobPara2['task.description']=taskDescription
        response2=pinganjianshe_get(url='/task/taskManage/updateTask.action',param=jobPara2,username=username,password=password)
#        Log.LogOutput(LogLevel.DEBUG,response2.text)
        
        #开启job
        Log.LogOutput(message='启动job')
        jobPara1['task.closed']='1'
        response3=pinganjianshe_get(url='/task/taskManage/changeTask.action',param=jobPara1,username=username,password=password)
#        Log.LogOutput(LogLevel.DEBUG,response3.text)
        Log.LogOutput(message='JOB已经开启，当前服务器时间为'+getLinuxDateAndTime())
        #因job设置成30s后启动，这里也只要等待30s后再去检查即可
        time.sleep(30)
        #在JOB监控中监测该JOB是否执行成功
        checkPara={
                   'jobName':jobPara['job.name'],#注意首字母大小写
                   'jobSuccess':'true',
                   }
        #等待JOB执行结果
        #设置等待间隔，每隔5s检查一次，总共检查10次，如果超过10次，就认为超时
        waitTime=5
        #设置等待次数
        count=0
        while (True):    
            r=checkJobComplete(checkPara=checkPara)
            if r is True:
                break
            else:
                Log.LogOutput( message='等待%d秒后再检查JOB是否执行完毕...'%waitTime)
                count=count+1
                if count>=5:#检查5次
                    Log.LogOutput(LogLevel.ERROR,'等待job超时，请延长task.config参数中setDelay()方法的超时参数')
                    break
                time.sleep(waitTime)
        if response2.result and response3.result and r :
            return True
        else:
            return False
    except Exception,e:
            Log.LogOutput(LogLevel.ERROR, '运行JOB出现异常！'+str(e))