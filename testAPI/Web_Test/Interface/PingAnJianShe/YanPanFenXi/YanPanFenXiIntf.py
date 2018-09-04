# -*- coding:UTF-8 -*-
'''
Created on 2016-2-29

@author: N-286
'''
from __future__ import unicode_literals
from COMMON import Log
from COMMON.CommonUtil import findDictInDictlist
from CONFIG import Global, InitDefaultPara
from CONFIG.Define import LogLevel
from CONFIG.InitDefaultPara import orgInit, userInit, roleInit
from Interface.PingAnJianShe.Common import CommonIntf
from Interface.PingAnJianShe.Common.CommonIntf import getDbQueryResult
from Interface.PingAnJianShe.ShiJianChuLi.ShiJianChuLiIntf import clearTable, \
    deleteAllIssues2, checkJobComplete, exeDbQuery
from Interface.PingAnJianShe.ShiYouRenKou import ShiYouRenKouPara
from Interface.PingAnJianShe.ShiYouRenKou.ShiYouRenKouIntf import \
    delete_HuJiRenKou
from Interface.PingAnJianShe.SystemMgr import SystemMgrPara
from Interface.PingAnJianShe.SystemMgr.SystemMgrIntf import addUser
from Interface.PingAnJianShe.XiaQuGuanLi import XiaQuGuanLiPara
from Interface.PingAnJianShe.XiaQuGuanLi.XiaQuGuanLiIntf import memberDel
from Interface.PingAnJianShe.ZuZhiChangSuo import ZuZhiChangSuoPara
from Interface.PingAnJianShe.ZuZhiChangSuo.ZuZhiChangSuoIntf import \
    deleteAnQuanShengChan
from Interface.PingAnJianShe.pingAnJianSheHttpCommon import pinganjianshe_post, \
    pinganjianshe_get, renzhengzhongxin_get, renzhengzhongxin_post
import copy
import json
import time
from Interface.PingAnJianShe.YanPanFenXi import YanPanFenXiPara




def YanPanFenXiInitEnv():
    clearTable(tableName='JOBMONITOR')#job监控表
    clearTable(tableName='OrgLoginStanals')
    clearTable(tableName='accountloginstanals')
    clearTable(tableName='systemlogs')
#     clearTable(tableName='Leaderviewresults')  #重点人员各月份图表
#     clearTable(tableName='statistichistory_2016_2') #重点人员2月份图表
    deleteAllIssues2()
    #如果工作日历没有设置，则设置2016和2015年工作日历
    initWorkCalendar(year='2015')
    initWorkCalendar(year='2016') 
   
'''
    @功能：初始化工作日历
    @return:    response
    @author:  chenhui 2016-04-22
'''   
def initWorkCalendar(year):
    if getDbQueryResult(dbCommand="select count(*) from workcalendars w where w.year='%s'"%year)==0:
        Log.LogOutput(LogLevel.INFO, year+"年工作日历没有创建，即将初始化工作日历..")
        response = pinganjianshe_post(url='/sysadmin/workCalendarManger/addWorkCalendar.action', postdata={'workCalendar.year':year}, username='admin', password='admin')
        if response.result is True:
            Log.LogOutput(message=year+'年工作日历初始化成功')
            return True
        else:
            Log.LogOutput(message=year+'年工作日历初始化失败')
            return False
    return True
 
'''
    @功能：检查数据是否存在于列表字典列表中
    @return:    response
    @author:  chenhui 2016-04-19
'''   
def checkDictInDictlist(checkpara,listpara,url):
    Log.LogOutput(LogLevel.INFO, "正在验证数据正确性")
    try:
        response = pinganjianshe_get(url=url,param=listpara)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False
        
'''
    @功能：查看所选部门的相关组织机构信息
    @return:    responseDict
    @author:  chenhui 2016-04-19
'''   
def viewOrgInfo(para):
    Log.LogOutput( message='获取部门org信息')
    response=renzhengzhongxin_get(url='/sysadmin/orgManage/ajaxOrganization',param=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(message='获取部门信息成功')
    else:
        Log.LogOutput(message='获取部门信息失败')
    return json.loads(response.text)

'''
    @功能：修改部门
    @return:    response
    @author:  chenhui 2016-04-19
'''   
def updateOrgInfo(para):
    Log.LogOutput( message='修改部门org信息')
    response=renzhengzhongxin_post(url='/sysadmin/orgManage/ajaxUpdateOrganization',postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(message='修改部门信息成功')
    else:
        Log.LogOutput(message='修改部门信息失败')
    return response
'''
    @功能：新增街道职能部门用户2
    @return:    response
    @author:  chenhui 2016-04-20
'''   
def addJieDaoFuncUser():
    userObject = copy.deepcopy(SystemMgrPara.userObject)
    #公共属性
    userObject['confirmPwd']= Global.NewUserDefaultPassword
    userObject['user.password']=Global.NewUserDefaultPassword
#     userObject['mode']='add'
    userObject['roleIds']=CommonIntf.getDbQueryResult(dbCommand="select t.id from roles t where t.rolename='%s'" % roleInit['DftRoleName'])
    #街道公安部门职能用户添加
    if CommonIntf.getDbQueryResult(dbCommand="select * from users t where t.username='zdhjdzn2@'") is not None:
#         Log.LogOutput(level=LogLevel.INFO, message='待添加的默认街道职能用户已经存在，无需添加')
        pass
    else:
        #街道职能用户属性
        userObject['organizationId']=CommonIntf.getDbQueryResult(dbCommand="select t.id from ORGANIZATIONS t where t.orgname='%s'" % orgInit['DftJieDaoFuncOrg'])
        userObject['user.mobile']=userInit['DftJieDaoFuncUserSJ']
        userObject['user.userName']='zdhjdzn2'
        userObject['user.name']='街道职能用户2'
        userObject['user.vpdn']='@'
        response = addUser(userObject)
        if response.result is False:
            Log.LogOutput(level=LogLevel.DEBUG, message='添加街道职能用户失败') 
        else:   
            Log.LogOutput(level=LogLevel.DEBUG, message='添加街道职能用户成功')

'''
    @功能：立即执行job，并检查是否执行成功
    @return:    response
    @author:  chenhui 2016-04-22
'''   
def runJobNow(jobPara):
    try:
        #获取该JOB在task表中的id
        taskId=getDbQueryResult(dbCommand = "select id from task t where t.name='%s'"%jobPara['task.name'])
        taskGroup=getDbQueryResult(dbCommand = "select TASKGROUP from task t where t.name='%s'"%jobPara['task.name'])
        taskDescription=getDbQueryResult(dbCommand = "select description from task t where t.name='%s'"%jobPara['task.name'])
        if taskId is None or taskGroup is None or taskDescription is None:
            Log.LogOutput(LogLevel.ERROR, '该JOB在数据库中不存在！请联系开发人员添加sql!!!')
            return False
        response=pinganjianshe_post(url='/task/taskManage/testJob.action',postdata={'task.id':taskId})
        if response.result :
            Log.LogOutput(message='job启动成功')
        else:
            Log.LogOutput(message='job启动失败')
            return False
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
        if r :
            Log.LogOutput(message='job执行检测结果成功')
            return True
        else:
            Log.LogOutput(message='job执行检测结果失败')
            return False
    except Exception,e:
            Log.LogOutput(LogLevel.ERROR, '运行JOB出现异常！'+str(e))    
            
'''
    @功能：注销
    @return:    response
    @author:  chenhui 2016-04-22
'''   
def pinganjianshe_LogOut():
    Log.LogOutput( message='用户登出')
    para={
            'isIndexJsp':'true',
            'indexPath':'',
            'defaults':'defaults'
          }
    response=pinganjianshe_post(url='/sysadmin/orgManage/ajaxUpdateOrganization',postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(message='登出成功')
    else:
        Log.LogOutput(message='登出失败')
    return response


'''
    @功能：检查登录统计
    @return:    response
    @author:  chenhui 2016-04-22
'''   
def checkOrgLogin(checkpara,listpara,url):
    Log.LogOutput(LogLevel.INFO, "正在验证数据正确性")
    try:
        response = pinganjianshe_get(url=url,param=listpara)
        responseDict=json.loads(response.text)
 #       print response.text
        if findDictInDictlist(checkpara,responseDict['objectDataList']) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False
'''
    @功能：删除所有网格一下的户籍人员
    @return:    response
    @author:  chenhui 2016-04-26
'''  
def deleteAllHouseholdStaff():
    try:
        #删除网格一户籍人口
        if CommonIntf.getDbQueryResult(dbCommand="select count(*) from HOUSEHOLDSTAFFS t where t.orgid='%s'" % orgInit['DftWangGeOrgId']) != 0: 
            compDict = copy.deepcopy(ShiYouRenKouPara.getHuJiOrgDict)
            compDict['orgId']= orgInit['DftWangGeOrgId']
            response = pinganjianshe_get(url='/baseinfo/householdStaff/findHouseholdStaffByOrgId.action', param=compDict)
            responseDict = json.loads(response.text)
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无户籍人口')
            else:
                for dictListItem in responseDict['rows']:
                    deleteDict = {'householdStaffVo.idStr':dictListItem['id']}
                    delete_HuJiRenKou(deleteDict)
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '删除异常')
        return False     
    return True

'''
    @功能：删除所有自动化社区下的成员库所有成员
    @return:    response
    @author:  chenhui 2016-04-26
'''  
def deleteAllMembers():
    Log.LogOutput(LogLevel.DEBUG, "删除成员库....")
    try:
        ParamList = copy.deepcopy(XiaQuGuanLiPara.personList)  
        ParamList['serviceTeamMemberVo.shared']=''
        ParamList['serviceTeamMemberVo.orgScope'] = 'allJurisdiction'
        ParamList['serviceTeamMemberVo.org.Id'] = InitDefaultPara.orgInit['DftSheQuOrgId']
        ParamList['serviceTeamMemberVo.nameIsDuplicate'] = '0'
        response = pinganjianshe_post(url='/plugin/serviceTeam/serviceTeamMember/findServiceTeamMemberBases.action',postdata=ParamList, username=userInit['DftSheQuUser'], password='11111111')
#         print response.text
        responseDict = json.loads(response.text)
        #获取的数据集合
        record = responseDict['records']
        if record == 0 :
            Log.LogOutput(level=LogLevel.DEBUG, message='成员库列表无数据')
        else:
            for dictListItem in responseDict['rows']:
                deleteDict = {'selectedIds':dictListItem['baseId'],'mode':'delete'}
                pinganjianshe_get(url='/plugin/serviceTeam/serviceTeamMember/deleteServiceTeamMember.action',param=deleteDict,username=userInit['DftSheQuUser'], password='11111111')              
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '查找成员库信息过程中失败')
        return False   
'''
    @功能：删除所有自动化社区下的所有安全生产
    @return:    response
    @author:  chenhui 2016-04-26
'''  
def deleteSafetyProduction():
    Log.LogOutput(LogLevel.DEBUG, "删除安全生产信息")
    try:   
# 删除安全生产重点 
        if CommonIntf.getDbQueryResult(dbCommand='select count(*) from SAFEPRODUCTIONENTERPRISE') != 0:                       
            compDict = copy.deepcopy(ZuZhiChangSuoPara.ChaKanAnQuanShengChanbject)
            compDict['orgId']= orgInit['DftSheQuOrgId']
            response = pinganjianshe_get(url='/baseinfo/safetyProductionKeyManage/safetyProductionKeyList.action', param=compDict)
            responseDict = json.loads(response.text)
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '无安全生产重点')  
            else:
                for dictListItem in responseDict['rows']:
                    deleteDict = {'enterPriseIds':dictListItem['id']}
                    deleteAnQuanShengChan(deleteDict)
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '删除安全生产出现异常')
        return False
    
'''
    @功能：删除所有自动化社区下的所有服务记录
    @return:    response
    @author:  chenhui 2016-04-26
'''  
def deleteServiceRecords():
    Log.LogOutput(LogLevel.DEBUG, "删除服务记录")
    try:   
# 删除服务记录
        if CommonIntf.getDbQueryResult(dbCommand="select count(*) from SAFEPRODUCTIONENTERPRISE s where s.orginternalcode like '.2%'") != 0:
            para={
                    'serviceRecordVo.organization.id':orgInit['DftSheQuOrgId'],
                    'serviceRecordVo.displayLevel':'directJurisdiction',
                    'serviceRecordVo.displayYear':time.strftime("%Y"),
                    '_search':'false',
                    'rows':'200',
                    'page':'1',
                    'sidx':'id',
                    'sord':'desc'
                  }                       
            response = pinganjianshe_get(url='/plugin/serviceTeam/serviceRecord/findServiceRecords.action', param=para)
            responseDict = json.loads(response.text)
            if responseDict['records'] == 0:
                Log.LogOutput(LogLevel.DEBUG, '服务记录')  
            else:
                for dictListItem in responseDict['rows']:
                    deleteDict = {
                                  'recordIds':dictListItem['id'],
                                  'mode':'delete'
                                  }
                    response=pinganjianshe_get(url='/plugin/serviceTeam/serviceRecord/deleteServiceRecords.action', param=deleteDict)   
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '删除服务记录出现异常')
        return False    
    
'''
    @功能：检查数据是否存在于网格员手机应用列表中
    @return:    response
    @author:  chenhui 2016-04-19
'''   
def checkDictInMobileGrid(checkpara,listpara):
    Log.LogOutput(LogLevel.INFO, "正在验证数据正确性")
    try:
        response = pinganjianshe_get(url='/gridMobile/gridMobileStatistic/findMobileStatistics.action',param=listpara)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False
        
'''
    @功能：检查数据是否存在于实有人口综合新增查询（新增、新增+更新）统计中
    @return:    response
    @author:  chenhui 2016-06-03
'''   
def checkDictInActualPopulationStatics(checkpara,listpara):
    Log.LogOutput(LogLevel.INFO, "正在验证数据正确性")
    try:
        response = pinganjianshe_get(url='/generalNewQuery/general/queryActualPopulationStatics.action',param=listpara)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False
        
'''
    @功能：检查数据是否存在于重点人员综合新增查询（新增、新增+更新）统计中
    @return:    response
    @author:  chenhui 2016-06-03
'''   
def checkDictInImportantPopulationStatics(checkpara,listpara):
    Log.LogOutput(LogLevel.INFO, "正在验证数据正确性")
    try:
        response = pinganjianshe_get(url='/generalNewQuery/general/queryImportantPersonelStatics.action',param=listpara)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False


'''
    @功能：检查数据是否存在于实有房屋综合新增查询（新增、新增+更新）统计中
    @return:    response
    @author:  chenhui 2016-06-03
'''   
def checkDictInActualHouseStatics(checkpara,listpara):
    Log.LogOutput(LogLevel.INFO, "正在验证数据正确性")
    try:
        response = pinganjianshe_get(url='/generalNewQuery/general/queryActualHouseStatics.action',param=listpara)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False        

'''
    @功能：检查数据是否存在于重点场所综合新增查询（新增、新增+更新）统计中
    @return:    response
    @author:  chenhui 2016-06-03
'''   
def checkDictInImportantPlaceStatics(checkpara,listpara):
    Log.LogOutput(LogLevel.INFO, "正在验证数据正确性")
    try:
        response = pinganjianshe_get(url='/generalNewQuery/general/queryImportantPlaceStatics.action',param=listpara)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False   


        
'''
    @功能：检查数据在重点人员概况中是否被统计到
    @return:    response
    @author:  chenyan 2016-05-05
'''   
def check_ImportantPersonnelGaiKuang(checkpara,orgId=None,tableType=None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "正在验证数据正确性")
    try:
        compDict = copy.deepcopy(YanPanFenXiPara.zhongDianRenYuan)
        compDict['orgId']= orgId
        compDict['tableType']= tableType
        response = pinganjianshe_get(url='/baseinfo/leaderViewManage/personGeneralCondition.action',param=compDict)
        responseDict=json.loads(response.text)
        #用遍历循环来获取固定网格下的字典
        for item in responseDict['rows']:
            if item['statisticsType']=='测试自动化网格':
                a = item  
        if findDictInDictlist(checkpara,[a]) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False
        
'''
    @功能：检查数据在重点人员各月份图表中是否被统计到
    @return:    response
    @author:  chenyan 2016-05-05
'''   
def check_ImportantPersonnelGeYue(checkpara,orgId=None,tableType=None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "正在验证数据正确性")
    try:
        compDict = copy.deepcopy(YanPanFenXiPara.zhongDianRenYuanGeYue)
        compDict['orgId']= orgId
        compDict['tableType']= tableType
        response = pinganjianshe_get(url='/baseinfo/leaderViewManage/monthGeneralConditionNew.action',param=compDict)
        responseDict=json.loads(response.text)
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False
        
'''
    @功能：检查数据在管理服务情况中是否被统计到
    @return:    response
    @author:  chenyan 2016-05-31
'''   
def check_service(checkpara,serviceType=None,queryDateType=None,orgId=None,businessType=None,beginDate=None,endDate=None,logoutType=None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "正在验证数据正确性")
    try:
        compDict = copy.deepcopy(YanPanFenXiPara.serviceDict)
        compDict['serviceType']= serviceType
        compDict['queryDateType']= queryDateType
        compDict['orgId']= orgId
        compDict['businessType']= businessType
        compDict['beginDate']= beginDate
        compDict['endDate']= endDate
        compDict['logoutType']= logoutType
        response = pinganjianshe_get(url='/baseInfoStat/manangedServicesStateManage/serviceState.action',param=compDict)
        responseDict=json.loads(response.text)
        #用遍历循环来获取固定网格下的字典
        for item in responseDict['rows']:
            if item['orgname']=='测试自动化网格':
                a = item  
        if findDictInDictlist(checkpara,[a]) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False
        
'''
    @功能：检查数据在管理服务人员落实情况中是否被统计到
    @return:    response
    @author:  chenyan 2016-05-31
'''   
def check_serviceMember(checkpara,serviceType=None,orgId=None,businessType=None,year=None,month=None,logoutType=None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "正在验证数据正确性")
    try:
        compDict = copy.deepcopy(YanPanFenXiPara.serviceMemberDict)
        compDict['serviceType']= serviceType
        compDict['orgId']= orgId
        compDict['businessType']= businessType
        compDict['year']= year
        compDict['month']= month
        compDict['logoutType']= logoutType
        response = pinganjianshe_get(url='/baseInfoStat/manangedServicesStateManage/serviceMemberAscertain.action',param=compDict)
        responseDict=json.loads(response.text)
        #用遍历循环来获取固定网格下的字典
        for item in responseDict['rows']:
            if item['orgname']=='测试自动化网格':
                a = item  
        if findDictInDictlist(checkpara,[a]) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False



'''
    @功能：检查数据在重点人员模块中是否被统计到
    @return:    response
    @author:  chenyan 2016-05-05
'''   
def check_ImportantPersonnel(checkpara,orgId=None,type=None, year=None,month=None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "正在验证数据正确性")
    try:
        compDict = copy.deepcopy(YanPanFenXiPara.zhongDianRenYuanZongKuang)
        compDict['orgId']= orgId
        compDict['type']= type
        compDict['year']= year
        compDict['month']= month       
        response = pinganjianshe_get(url='/baseInfo/statisticManage/getBaseInfoStatisticList.action',param=compDict)
        responseDict=json.loads(response.text)
    #用遍历循环来获取固定网格下的字典
        for item in responseDict:
            if item['orgName']=='测试自动化网格':
                if findDictInDictlist(checkpara,[item]) is True:
                    Log.LogOutput(LogLevel.DEBUG, "数据存在")
                    return True
                else:
                    Log.LogOutput(LogLevel.DEBUG, "数据不存在")
                    return False

    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False

        
'''
    @功能：检查数据在重点人员模块中是否被统计到
    @return:    response
    @author:  chenyan 2016-05-05
'''   
def check_positiveInfo(checkpara,orgId=None,type=None, year=None,month=None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "正在验证数据正确性")
    try:
        compDict = copy.deepcopy(YanPanFenXiPara.zhongDianRenYuanZongKuang)
        compDict['orgId']= orgId
        compDict['type']= type
        compDict['year']= year
        compDict['month']= month       
        response = pinganjianshe_get(url='/baseInfo/statisticManage/getBaseInfoStatisticList.action',param=compDict)
        responseDict=json.loads(response.text)
    #用遍历循环来获取固定网格下的字典
        for item in responseDict:
            if item['orgName']=='测试自动化网格':
                a = item  
#                 if findDictInDictlist(checkpara,[a]) is True:
#                     Log.LogOutput(LogLevel.DEBUG, "数据存在")
#                     return True
#                 else:
#                     Log.LogOutput(LogLevel.DEBUG, "数据不存在")
#                     return False
                for item1 in a['baseinfoStatisticDetailVo']:
                    if item1['typeName']=='刑释人员':
                        b = item1
                    elif item1['typeName']=='解教人员':
                        c = item1
                    elif item1['typeName']=='合计':
                        d = item1

        if checkpara['typeName']=='刑释人员':
            if findDictInDictlist(checkpara,[b]) is True:
                Log.LogOutput(LogLevel.DEBUG, "数据存在")
                return True
            else:
                Log.LogOutput(LogLevel.DEBUG, "数据不存在")
                return False
        elif checkpara['typeName']=='解教人员':
            if findDictInDictlist(checkpara,[c]) is True:
                Log.LogOutput(LogLevel.DEBUG, "数据存在")
                return True
            else:
                Log.LogOutput(LogLevel.DEBUG, "数据不存在")
                return False
        elif checkpara['typeName']=='合计':                        
            if findDictInDictlist(checkpara,[d]) is True:
                Log.LogOutput(LogLevel.DEBUG, "数据存在")
                return True
            else:
                Log.LogOutput(LogLevel.DEBUG, "数据不存在")
                return False
                        
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False
        
'''
    @功能：检查数据在重点人员刑释人员区域分布图中是否被统计到
    @return:    response
    @author:  chenyan 2016-05-05
'''   
def check_positiveInfoQuYu(checkpara,orgId=None,type=None, year=None,month=None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "正在验证数据正确性")
    try:
        compDict = copy.deepcopy(YanPanFenXiPara.zhongDianRenYuanZongKuang)
        compDict['orgId']= orgId
        compDict['type']= type
        compDict['year']= year
        compDict['month']= month      
#         print  compDict                 
        response = pinganjianshe_get(url='/baseInfo/statisticManage/getStatisticColumn.action',param=compDict)
        responseDict=json.loads(response.text)     
#         print response.content
        list1 = responseDict['categories']
        index1 = list1.index('测试自动化网格')
        index2 = list1.index('测试自动化网格1')
        
        if checkpara['name']=='刑释人员':
            list2=[0,0]
            list2[index1]=2
            list2[index2]=0 
            list2=[list2[index1]]+[list2[index2]]
            checkpara['Data']=list2
#             print checkpara['Data']
        elif checkpara['name']=='解教人员':
            list3=[0,0]
            list3[index1]=1
            list3[index2]=0 
            list3=[list3[index1]]+[list3[index2]]
            checkpara['Data']=list3
        
        if findDictInDictlist(checkpara,responseDict['series']) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False       
                        
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False
        
        

'''
    @功能：检查数据在重点人员重点青少年区域分布图中是否被统计到
    @return:    response
    @author:  chenyan 2016-05-05
'''   
def check_idleYouthQuYu(checkpara,orgId=None,type=None, year=None,month=None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "正在验证数据正确性")
    try:
        compDict = copy.deepcopy(YanPanFenXiPara.zhongDianRenYuanZongKuang)
        compDict['orgId']= orgId
        compDict['type']= type
        compDict['year']= year
        compDict['month']= month       
        response = pinganjianshe_get(url='/baseInfo/statisticManage/getStatisticColumn.action',param=compDict)
        responseDict=json.loads(response.text)     

        list1 = responseDict['categories']
        index1 = list1.index('测试自动化网格')
        index2 = list1.index('测试自动化网格1')
        
        if checkpara['name']=='10岁以下':
            list2=[0,0]
            list2[index1]=0
            list2[index2]=0 
            list2=[list2[index1]]+[list2[index2]]
            checkpara['Data']=list2
        elif checkpara['name']=='10~16岁':
            list3=[0,0]
            list3[index1]=0
            list3[index2]=0 
            list3=[list3[index1]]+[list3[index2]]
            checkpara['Data']=list3
        
        if findDictInDictlist(checkpara,responseDict['series']) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False       
                        
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False
 
 
'''  
    @功能： 测试自动化网格下重点场所中场所取消关注
    @para: 
    @return: 如果取消关注成功，则返回True；否则返回False  
'''
def pdateEmphasise(serviceDict, username = None, password = None):  
    Log.LogOutput(LogLevel.INFO, "重点场所中场所取消关注开始..")
    response = pinganjianshe_post(url='/baseinfo/fireSafetyEnterpriseManage/updateEmphasiseById.action', postdata=serviceDict,username=username, password=password)
#     print response.text
#     if response.result is True:
#         Log.LogOutput(LogLevel.INFO, "场所取消关注成功")
#     else:
#         Log.LogOutput(LogLevel.ERROR, "场所取消关注失败")     
    return response 
 
'''
    @功能：检查数据在重点场所模块中是否被统计到
    @return:    response
    @author:  chenyan 2016-05-05
'''   
def check_ImportantPlace(checkpara,orgId=None,keyType=None, year=None,month=None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "正在验证数据正确性")
    try:
        compDict = copy.deepcopy(YanPanFenXiPara.zhongDianChangSuoZongKuang)
        compDict['orgId']= orgId
        compDict['keyType']= keyType
        compDict['year']= year
        compDict['month']= month       
        response = pinganjianshe_get(url='/baseInfoStat/statisticsPlace/getStatisticsPlaceInfoList.action',param=compDict)
        responseDict=json.loads(response.text)
    #用遍历循环来获取固定网格下的字典
        for item in responseDict:
            if item['orgName']=='测试自动化网格':
                a = item  
                if findDictInDictlist(checkpara,[a]) is True:
                    Log.LogOutput(LogLevel.DEBUG, "数据存在")
                    return True
                else:
                    Log.LogOutput(LogLevel.DEBUG, "数据不存在")
                    return False

    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False


'''
    @功能：检查数据在重点场所模块中是否被统计到
    @return:    response
    @author:  chenyan 2016-05-05
'''   
def check_statAnalysePlace(checkpara,orgId=None,keyType=None, year=None,month=None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "正在验证数据正确性")
    try:
        compDict = copy.deepcopy(YanPanFenXiPara.zhongDianChangSuoZongKuang)
        compDict['orgId']= orgId
        compDict['keyType']= keyType
        compDict['year']= year
        compDict['month']= month       
        response = pinganjianshe_get(url='/baseinfo/statAnalysePlace/findStatAnalysePlace.action',param=compDict)
        responseDict=json.loads(response.text)
    #用遍历循环来获取固定网格下的字典
        for item in responseDict:
            a=item['organization']['orgName']
            if a=='测试自动化网格':
                list = [item]
                if findDictInDictlist(checkpara,list) is True:
                    Log.LogOutput(LogLevel.DEBUG, "数据存在")
                    return True
                else:
                    Log.LogOutput(LogLevel.DEBUG, "数据不存在")
                    return False

    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False


'''
    @功能：检查数据在重点场所安全重点生产区域分布图中是否被统计到
    @return:    response
    @author:  chenyan 2016-05-05
'''   
def check_statAnalysePlaceQuYu(checkpara,orgId=None,keyType=None, year=None,month=None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "正在验证数据正确性")
    try:
        compDict = copy.deepcopy(YanPanFenXiPara.zhongDianChangSuoZongKuang)
        compDict['orgId']= orgId
        compDict['keyType']= keyType
        compDict['year']= year
        compDict['month']= month      
        response = pinganjianshe_get(url='/baseinfo/statAnalysePlace/findStatAnalysePlaceForHighchartColumnVo.action',param=compDict)
        responseDict=json.loads(response.text)     
        list1 = responseDict['categories']
        index1 = list1.index('测试自动化网格')
        index2 = list1.index('测试自动化网格1')
        
        if checkpara['name']=='安全生产重点':
            list2=[0,0]
            list2[index1]=3
            list2[index2]=0 
            list2=[list2[index1]]+[list2[index2]]
            checkpara['Data']=list2
#             print checkpara['Data']
        
        if findDictInDictlist(checkpara,responseDict['series']) is True:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据不存在")
            return False       
                        
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False