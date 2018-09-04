# -*- coding:UTF-8 -*-
'''
Created on 2015-12-22

@author: chenyan
'''
from __future__ import unicode_literals
from COMMON import Log, CommonUtil, Time
from COMMON.Time import getCurrentTime, getCurrentDateAndTime
from CONFIG.Global import simulationEnvironment
from CONFIG.InitDefaultPara import orgInit, userInit
from Interface.PingAnJianShe.Common import CommonIntf
from Interface.PingAnJianShe.Common.CommonIntf import getDbQueryResult
from Interface.PingAnJianShe.RiChangBanGong import RiChangBanGongIntf, \
    RiChangBanGongPara
from Interface.PingAnJianShe.RiChangBanGong.RiChangBanGongIntf import \
    richangBanGongInitEnv, addConflictRecord, checkConflictRecord, addConflictNormal, \
    checkConflictNormal, addConflictImpt, checkConflictImpt, delConflictNormal, \
    checkConflictNormalDel, delConflictRecord, checkConflictRecordDel, \
    delConflictImpt, checkConflictImptDel, updConflictRecord, checkConflictRecordUpd, \
    updConflictNormal, updConflictImpt, reportConflictRecord, checkReportRecord, \
    deleteAllReport, backConflictRecord, importConflictRptNormal, \
    getImportConflictRptMsgByTicketId, importConflictRptImpt, \
    getConflictRptImptDataCount, getConflictRptDataByYear, getConflictRptDataByYear2, \
    setLinuxTime, runJob, getConflictRptDatasType, getConflictNormalListNum, \
    getConflictImptListNum, addSocialSecurit, checkSocialSecurit, updSocialSecurit, \
    delSocialSecurit, reportSocialSecurit, backSocialSecurit, addSocialSecuritRpt, \
    checkSocialSecuritRpt, updSocialSecuritRpt, delSocialSecuritRpt, \
    reportSocialSecuritRpt, getSocialSecuritRptDataByReportTime, \
    backSocialSecuritRpt
from Interface.PingAnJianShe.RiChangBanGong.RiChangBanGongPara import \
    confictRptRecordPara1, confictRptRecordPara, confictRptRecordListPara, \
    confictRptRecordCheckPara, conflictRptNormalListPara, conflictRptNormalCheckPara, \
    conflictRptNormalPara1, conflictRptImptPara1, conflictRptImptCheckPara, \
    conflictRptImptListPara, conflictRptImptDelPara, confictRptRecordDelPara, \
    confictRptRecordViewPara, conflictRptNormalImportData, conflictRptImptImportData, \
    conflictImptDataCountPara, socialSecurityAddPara, socialSecurityAddPara1, \
    socialSecurityListPara, socialSecurityReportAddPara1, \
    socialSecurityReportListPara, socialSecurityReportReportPara
from Interface.PingAnJianShe.ShiJianChuLi import ShiJianChuLiPara, \
    ShiJianChuLiIntf
from Interface.PingAnJianShe.ShiJianChuLi.ShiJianChuLiIntf import clearTable, \
    setJobDelayTime, deleteAllIssues2, dealIssue
from Interface.PingAnJianShe.SystemMgr import SystemMgrIntf
from Interface.YunWeiPingTai.YunWeiCommon.YunWeiCommonIntf import \
    setLinuxTimeYunWei
import copy
import time
import unittest
    

    
#仿真环境不可用
 
class RiChangBanGong(unittest.TestCase):

    def setUp(self):
        SystemMgrIntf.initEnv()
        #仿真环境不可用，加判断防止误操作
        if simulationEnvironment is False:
            richangBanGongInitEnv()
            RiChangBanGongIntf.deleteAllRecords()
        pass
    
    '''
    @功能：矛盾纠纷排查报表新增
    @ chenhui 2016-1-4
    '''         
    def testConflictRpt_001(self):
        '''新增矛盾纠纷排查报表'''
        #仿真环境下跳过测试
        if simulationEnvironment is True:
            pass
        else:
            clearTable(tableName='conflictRptRecord')
            #单单验证新增功能，报表选择从2016年1月开始
            #设置2016年1月份新增参数
            rptRecdPara=copy.deepcopy(confictRptRecordPara)      
            rptRecdPara['dailyYear.id']=getDbQueryResult(dbCommand = "select id from dailyYears d where d.yeardate='2016' and d.makedorgid='%s'and d.dailytype='0'"%orgInit['DftJieDaoOrgId'])
            rptRecdPara['dailyDirectory.id']=getDbQueryResult(dbCommand ="select id from newdailyDirectorys d where d.dailyyearid='%s' and d.shortname='月报'"%rptRecdPara['dailyYear.id'])
            rptRecdPara['dealPerson']='签发人'
            rptRecdPara['lister']='制表人'
            addConflictRecord(para=rptRecdPara,username=userInit['DftSheQuUser'])
            #验证新增是否成功
            #检查参数
            checkPara=copy.deepcopy(confictRptRecordCheckPara)
            checkPara['dailyYearId']=rptRecdPara['dailyYear.id']
            checkPara['newDailyDirectoryId']=rptRecdPara['dailyDirectory.id']
            checkPara['name']='2016年1月测试自动化社区矛盾纠纷排查情况表'
            #列表显示参数
            listPara=copy.deepcopy(confictRptRecordListPara)
            listPara['conflictRpt.organization.id']=orgInit['DftSheQuOrgId']
            listPara['conflictRpt.newDailyDirectoryId']=rptRecdPara['dailyDirectory.id']
            listPara['yearDate']=rptRecdPara['year']
            result1=checkConflictRecord(checkPara=checkPara,listPara=listPara)
            self.assertTrue(result1, '新增验证失败！')
            
            #新增普通报表
            conflictNormalPara=copy.deepcopy(conflictRptNormalPara1)
            addConflictNormal(para=conflictNormalPara)
            #设置检查参数
            listPara3=copy.deepcopy(conflictRptNormalListPara)
            checkPara3=copy.deepcopy(conflictRptNormalCheckPara)
            checkPara3['dealdate']=conflictNormalPara['conflictRptNormal.dealdate']
            checkPara3['departmentandperson']=conflictNormalPara['conflictRptNormal.departmentandperson']
            checkPara3['name']=conflictNormalPara['conflictRptNormal.name']
            checkPara3['recorddate']=conflictNormalPara['conflictRptNormal.recorddate']
            checkPara3['typeName']='民族宗教'
            result3=checkConflictNormal(checkPara=checkPara3,listPara=listPara3)
            self.assertTrue(result3, '新增普通报表验证失败')
            
            #新增重大报表
            conflictImptPara=copy.deepcopy(conflictRptImptPara1)
            addConflictImpt(para=conflictImptPara)
            
            checkPara4=copy.deepcopy(conflictRptImptCheckPara)
            checkPara4['basicSituation']="基本情况"
            checkPara4['developSituation']="进展情况"
            checkPara4['disputesType']="类型"
            checkPara4['involveSituation']="所涉群体及人数"
            checkPara4['ondutyTarget']="责任单位及责任人"
            checkPara4['workingMeasure']="工作措施"
            
            listPara4=copy.deepcopy(conflictRptImptListPara)
            listPara4['yearDate']='2016'
            listPara4['reportTime']='1'
            result41=checkConflictImpt(checkPara=checkPara4,listPara=listPara4)
            self.assertTrue(result41,'检查新增重大矛盾纠纷报表失败')
            pass
    
    '''
    @功能：矛盾纠纷排查报表删除
    @ chenhui 2015-1-5
    '''         
    def testConflictRpt_002(self):
        '''删除矛盾纠纷排查报表记录、普通报表、重大报表'''
        #仿真环境下跳过测试
        if simulationEnvironment is True:
            pass
        else:
            #删除普通报表
            #首先新增普通报表
            conflictNormalPara=copy.deepcopy(conflictRptNormalPara1)
            addConflictNormal(para=conflictNormalPara)
            #删除普通报表
            listPara1=copy.deepcopy(conflictRptNormalListPara)
            delConflictNormal(listPara=listPara1)
            #检查是否删除成功
            result11=checkConflictNormalDel(listPara=listPara1)
            self.assertTrue(result11, '删除失败')
            
            #删除矛盾纠纷记录
            #首先新增记录
            rptRecdPara=copy.deepcopy(confictRptRecordPara)      
            rptRecdPara['dailyYear.id']=getDbQueryResult(dbCommand = "select id from dailyYears d where d.yeardate='2016' and d.makedorgid='%s'and d.dailytype='0'"%orgInit['DftJieDaoOrgId'])
            rptRecdPara['dailyDirectory.id']=getDbQueryResult(dbCommand ="select id from newdailyDirectorys d where d.dailyyearid='%s' and d.shortname='月报'"%rptRecdPara['dailyYear.id'])
            rptRecdPara['dealPerson']='签发人'
            rptRecdPara['lister']='制表人'
            addConflictRecord(para=rptRecdPara,username=userInit['DftSheQuUser'],password='11111111')
            #删除记录报表
            delPara3=copy.deepcopy(confictRptRecordDelPara)
            delPara3['conflictRpt.id']=getDbQueryResult(dbCommand ="select id from conflictrpt_2016_1")
            delPara3['reportTypeInternalId']=rptRecdPara['reportTypeInternalId']
            delConflictRecord(para=delPara3)
            #检查是否删除成功
            listPara3=copy.deepcopy(confictRptRecordListPara)
            listPara3['conflictRpt.organization.id']=orgInit['DftSheQuOrgId']
            listPara3['conflictRpt.newDailyDirectoryId']=rptRecdPara['dailyDirectory.id']
            listPara3['yearDate']=rptRecdPara['year']
            listPara3['reportTypeInternalId']=rptRecdPara['reportTypeInternalId']
            result33=checkConflictRecordDel(para=listPara3)
            self.assertTrue(result33, '删除失败') 
            
            #删除重大报表
            #1.首先新增记录表
            addConflictRecord(para=rptRecdPara,username=userInit['DftSheQuUser'],password='11111111')
            #2.再新增一重大矛盾纠纷报表
            conflictImptPara=copy.deepcopy(conflictRptImptPara1)
            result2=addConflictImpt(para=conflictImptPara)
            #删除重大报表
            delPara=copy.deepcopy(conflictRptImptDelPara)
            delPara['strIds']=result2['id']
            delPara['yearDate']=conflictImptPara['yearDate']
            delPara['reportTime']=conflictImptPara['reportTime']
            delConflictImpt(para=delPara)
            #检查是否删除成功
            listPara2=copy.deepcopy(conflictRptImptListPara)
            listPara2['yearDate']=conflictImptPara['yearDate']
            listPara2['reportTime']=conflictImptPara['reportTime']
            result22=checkConflictImptDel(para=listPara2)
            self.assertTrue(result22, '重大矛盾纠纷删除验证失败')
            #最后将记录表也删除
            delPara3['conflictRpt.id']=getDbQueryResult(dbCommand ="select id from conflictrpt_2016_1")
            delConflictRecord(para=delPara3)
            pass    
    
    '''
    @功能：重大矛盾纠纷报表和普通矛盾纠纷报表的修改
    @ chenhui 2016-1-7
    '''         
    def testConflictRpt_003(self):
        #仿真环境下跳过测试
        if simulationEnvironment is True:
            pass
        else:
            #新增月报记录表
            #设置2016年1月份新增参数
            rptRecdPara=copy.deepcopy(confictRptRecordPara)      
            rptRecdPara['dailyYear.id']=getDbQueryResult(dbCommand = "select id from dailyYears d where d.yeardate='2016' and d.makedorgid='%s'and d.dailytype='0'"%orgInit['DftJieDaoOrgId'])
            rptRecdPara['dailyDirectory.id']=getDbQueryResult(dbCommand ="select id from newdailyDirectorys d where d.dailyyearid='%s' and d.shortname='月报'"%rptRecdPara['dailyYear.id'])
            rs1=addConflictRecord(para=rptRecdPara,username=userInit['DftSheQuUser'])
            #修改月报
            updPara1=copy.deepcopy(confictRptRecordPara1)
            updPara1['conflictRpt.id']=rs1
            updPara1['dealPerson']='aaa1'
            updPara1['lister']='bbb1'
            result1=updConflictRecord(para=updPara1)
            self.assertEqual(rs1, result1, '新增或者修改失败')
            Log.LogOutput( message='修改完毕，开始验证')
            #验证修改功能
            viewPara1=copy.deepcopy(confictRptRecordViewPara)
            viewPara1['dailyDirectory.id']=rptRecdPara['dailyDirectory.id']
            viewPara1['reportTime']=rptRecdPara['reportTime']
            viewPara1['organization.id']=orgInit['DftSheQuOrgId']
            viewPara1['dailyYear.yearDate']=rptRecdPara['year']
            viewPara1['conflictRpt.id']=rs1
            #设置检查参数
            checkPara1={
             'totalSuccNum':updPara1['conflictRpt.totalSuccNum'],
             'dealPerson':updPara1['dealPerson'],
             'lister':updPara1['lister']  
                       }
            result11=checkConflictRecordUpd(checkPara=checkPara1,viewPara=viewPara1)
            self.assertTrue(result11, '修改验证失败')
            
            #新增普通报表
            conflictNormalPara=copy.deepcopy(conflictRptNormalPara1)
            addConflictNormal(para=conflictNormalPara)
            #修改普通报表
            updPara2=copy.deepcopy(conflictRptNormalPara1)
            updPara2['conflictRptNormal.id']=getDbQueryResult(dbCommand = "select id from ConflictRptnormal_2016_1")
            updPara2['conflictRptNormal.createorgcode']=getDbQueryResult(dbCommand = "select createorgcode from ConflictRptnormal_2016_1")
            updPara2['conflictRptNormal.name']='事项1'
            updPara2['conflictRptNormal.recorddate']=Time.getCurrentDate()
            updPara2['conflictRptNormal.dealdate']='2066-01-01'
            updPara2['selectedTypes']=2
            updPara2['conflictRptNormal.departmentandperson']='责任单位及负责人1'
            updConflictNormal(para=updPara2)
            #验证修改
            checkPara2={
                        'dealdate': updPara2['conflictRptNormal.dealdate'],
                        'departmentandperson':updPara2['conflictRptNormal.departmentandperson'],
                        'name':updPara2['conflictRptNormal.name'],
                        'type':updPara2['selectedTypes'],
                        'recorddate':updPara2['conflictRptNormal.recorddate']
                        }
            listPara2=copy.deepcopy(conflictRptNormalListPara)
            result2=checkConflictNormal(checkPara=checkPara2, listPara=listPara2)
            self.assertTrue(result2, '修改验证失败！')
            #新增重大报表
            conflictImptPara=copy.deepcopy(conflictRptImptPara1)
            result3=addConflictImpt(para=conflictImptPara)
            #修改重大报表
            updPara3=copy.deepcopy(conflictRptImptPara1)
            updPara3['mode']='edit'
            updPara3['conflictRptImpt.id']=result3['id']
            updPara3['conflictRptImpt.basicSituation']='基本情况1'
            updPara3['conflictRptImpt.status']=1
            updPara3['conflictRptImpt.involveSituation']='所涉群体及人数1'
            updPara3['conflictRptImpt.disputesType']='类型1'
            updPara3['conflictRptImpt.ondutyTarget']='责任单位及责任人1'
            updPara3['conflictRptImpt.workingMeasure']='工作措施1'
            updPara3['conflictRptImpt.developSituation']='进展情况1'
            updConflictImpt(para=updPara3)
            #验证修改功能
            checkPara3={
                        'basicSituation': updPara3['conflictRptImpt.basicSituation'],
                        'developSituation': updPara3['conflictRptImpt.developSituation'],
                        'disputesType':updPara3['conflictRptImpt.disputesType'],
                        'id': updPara3['conflictRptImpt.id'],
                        'involveSituation': updPara3['conflictRptImpt.involveSituation'],
                        'ondutyTarget': updPara3['conflictRptImpt.ondutyTarget'],
                        'status': updPara3['conflictRptImpt.status'],
                        'workingMeasure': updPara3['conflictRptImpt.workingMeasure'],
                        }
            listPara3=copy.deepcopy(conflictRptImptListPara)
            listPara3['yearDate']=updPara3['yearDate']
            listPara3['reportTime']=updPara3['reportTime']
            result33=checkConflictImpt(checkPara=checkPara3,listPara=listPara3)
            self.assertTrue(result33, '修改检查失败！')
            pass
    
    '''
    @功能：月报上报
    @ chenhui 2016-1-7
    '''         
    def testConflictRpt_004(self):
        '''矛盾纠纷记录表上报'''
        #仿真环境下跳过测试
        if simulationEnvironment is True:
            pass
        else:
            #新增月报记录表
            #设置2016年1月份新增参数
            rptRecdPara=copy.deepcopy(confictRptRecordPara)      
            rptRecdPara['dailyYear.id']=getDbQueryResult(dbCommand = "select id from dailyYears d where d.yeardate='2016' and d.makedorgid='%s'and d.dailytype='0'"%orgInit['DftJieDaoOrgId'])
            rptRecdPara['dailyDirectory.id']=getDbQueryResult(dbCommand ="select id from newdailyDirectorys d where d.dailyyearid='%s' and d.shortname='月报'"%rptRecdPara['dailyYear.id'])
            
            rs=addConflictRecord(para=rptRecdPara,username=userInit['DftSheQuUser'])
            #上报参数
            para={
                  'id':rs,
                  'reportTypeInternalId':1,
                  }
            
            #验证签发人和制表人为空的情况下直接上报是否有验证信息
            reportConflictRecord(para=para)
            listPara=copy.deepcopy(confictRptRecordListPara)
            listPara['conflictRpt.organization.id']=orgInit['DftSheQuOrgId']
            listPara['conflictRpt.newDailyDirectoryId']=rptRecdPara['dailyDirectory.id']
            listPara['yearDate']=rptRecdPara['year']
            listPara['reportTypeInternalId']=rptRecdPara['reportTypeInternalId']
            result=checkReportRecord(listPara=listPara)
            self.assertEqual(result, 0, '未填写签发人或者制表人直接上报验证错误！')
            #验证正常上报功能
            delPara=copy.deepcopy(confictRptRecordDelPara)
            delPara['conflictRpt.id']=rs
            delPara['reportTypeInternalId']=rptRecdPara['reportTypeInternalId']
            delConflictRecord(para=delPara)
            rptRecdPara['dealPerson']='签发人'
            rptRecdPara['lister']='制表人'
            rs2=addConflictRecord(para=rptRecdPara,username=userInit['DftSheQuUser'])
            #上报参数
            para2={
                  'id':rs2,
                  'reportTypeInternalId':1,
                  }
            reportConflictRecord(para=para2)
            result=checkReportRecord(listPara=listPara)
            self.assertEqual(result, 1, '上报失败！')
            Log.LogOutput( message='上报验证通过')
            #验证已上报的月报重复上报
            Log.LogOutput(message='验证再次重复上报是否返回错误信息')
            result1=reportConflictRecord(para=para2)
            self.assertEqual(result1.text, '\"上报出错,请联系管理员!\"', '重复上报验证失败')
    #        self.assertFalse(result1.result,'重复上报验证失败！')
            #验证排查总是之和不等于起数之和，上报时是否有验证
            Log.LogOutput(message='验证起数之和不等于总排查数，上报会返回错误信息')
            deleteAllReport()
            rptRecdPara2=copy.deepcopy(confictRptRecordPara)
            #起数之和为1 
            rptRecdPara2['conflictRpt.numInFifty']='1'     
            rptRecdPara2['dailyYear.id']=getDbQueryResult(dbCommand = "select id from dailyYears d where d.yeardate='2016' and d.makedorgid='%s'and d.dailytype='0'"%orgInit['DftJieDaoOrgId'])
            rptRecdPara2['dailyDirectory.id']=getDbQueryResult(dbCommand ="select id from newdailyDirectorys d where d.dailyyearid='%s' and d.shortname='月报'"%rptRecdPara['dailyYear.id'])
            
            rs22=addConflictRecord(para=rptRecdPara2,username=userInit['DftSheQuUser'])
            #上报参数
            para22={
                  'id':rs22,
                  'reportTypeInternalId':1,
                  }
            result22=reportConflictRecord(para=para22)
            self.assertFalse(result22.result, '排查数之和不等于起数时，上报没有验证')    
            pass
        
    '''
    @功能：月报回退
    @ chenhui 2016-1-7
    '''         
    def testConflictRpt_005(self):
        '''矛盾纠纷记录表回退'''
        #仿真环境下跳过测试
        if simulationEnvironment is True:
            pass
        else:
    #        deleteAllReport()
            rptRecdPara=copy.deepcopy(confictRptRecordPara)      
            rptRecdPara['dailyYear.id']=getDbQueryResult(dbCommand = "select id from dailyYears d where d.yeardate='2016' and d.makedorgid='%s'and d.dailytype='0'"%orgInit['DftJieDaoOrgId'])
            rptRecdPara['dailyDirectory.id']=getDbQueryResult(dbCommand ="select id from newdailyDirectorys d where d.dailyyearid='%s' and d.shortname='月报'"%rptRecdPara['dailyYear.id'])
            rptRecdPara['dealPerson']='签发人'
            rptRecdPara['lister']='制表人'
            rs=addConflictRecord(para=rptRecdPara,username=userInit['DftSheQuUser'])
            #街道对社区新增状态的月报回退
            Log.LogOutput(message='验证街道对社区新增状态的月报回退，返回错误信息')
            #回退参数
            backPara={
                'mode':'society',
                'dailyLogId':rs,
                'dailyDirectoryId':rptRecdPara['dailyDirectory.id'],
                'organization.id':orgInit['DftSheQuOrgId'],
                'orgId':orgInit['DftJieDaoOrgId'],
                'platformMessage.title':'2016年1月测试自动化社区矛盾纠纷排查情况表退回提醒！',
                'platformMessage.content':'描述',    
                      }
            result0=backConflictRecord(para=backPara, username = userInit['DftJieDaoUser'])
            self.assertFalse(result0.result, '街道回退新增状态的社区月报,回退缺少验证')
            Log.LogOutput(message='街道回退新增状态的社区月报验证成功')
            #上报
            para={
                  'id':rs,
                  'reportTypeInternalId':1,
                  }
            reportConflictRecord(para=para)
            #验证正常回退功能
            Log.LogOutput(message='验证正常回退功能')
            backConflictRecord(para=backPara, username = userInit['DftJieDaoUser'])
            listPara=copy.deepcopy(confictRptRecordListPara)
            listPara['conflictRpt.organization.id']=orgInit['DftSheQuOrgId']
            listPara['conflictRpt.newDailyDirectoryId']=rptRecdPara['dailyDirectory.id']
            listPara['yearDate']=rptRecdPara['year']
            listPara['reportTypeInternalId']=rptRecdPara['reportTypeInternalId']
            result=checkReportRecord(listPara=listPara)
            self.assertEqual(result, 2, '回退失败！')
            Log.LogOutput( message='正常回退验证通过')
            #验证对于已回退状态的月报再次回退应返回错误信息
            Log.LogOutput(message='验证对于已回退状态的月报再次回退')
            result1=backConflictRecord(para=backPara, username = userInit['DftJieDaoUser'])
            self.assertFalse(result1.result, '重复回退验证失败')
            Log.LogOutput(message='重复回退验证成功！')
            #验证跨级回退月报返回错误信息
            #重新上报
            reportConflictRecord(para=para)
            Log.LogOutput(message='验证区跨级回退社区报表')
            backPara['orgId']=orgInit['DftQuOrgId']
            result2=backConflictRecord(para=backPara, username = userInit['DftQuUser'])
            self.assertFalse(result2.result, '区跨级回退社区报表没有返回错误信息，验证失败！')
            Log.LogOutput(message='区跨级回退社区报表有返回错误信息验证成功!')
            pass
    

    '''
    @功能：普通清单、重大清单导入
    @ chenhui 2016-1-15
    '''         
    def testConflictRpt_006(self):
        '''普通、重大矛盾纠纷排查报表的导入功能'''
        #仿真环境下跳过测试
        if simulationEnvironment is True:
            pass
        else:
            #首先新增记录表
            rptRecdPara=copy.deepcopy(confictRptRecordPara)      
            rptRecdPara['dailyYear.id']=getDbQueryResult(dbCommand = "select id from dailyYears d where d.yeardate='2016' and d.makedorgid='%s'and d.dailytype='0'"%orgInit['DftJieDaoOrgId'])
            rptRecdPara['dailyDirectory.id']=getDbQueryResult(dbCommand ="select id from newdailyDirectorys d where d.dailyyearid='%s' and d.shortname='月报'"%rptRecdPara['dailyYear.id'])
            addConflictRecord(para=rptRecdPara,username=userInit['DftSheQuUser'])
            #导入普通空模板
            Log.LogOutput( message='验证导入普通清单空模板是否有错误信息')
            confictRptNormalData=copy.deepcopy(conflictRptNormalImportData)
            files1 = {'upload': ('test.xls', open('C:/autotest_file/conflictRpt/conflict_normal_error.xls', 'rb'),'applicationnd.ms-excel')}
            result1=importConflictRptNormal(confictRptNormalData,files=files1)
            importmsg1={
                        'ticketId':result1,
                        'currentErrorRow':'0',
                        }
            rs1=getImportConflictRptMsgByTicketId(para=importmsg1)
            self.assertEquals(rs1['errorMsgs'][0], '数据为空，请填入数据后重新导入','空模板导入验证失败')
            Log.LogOutput(message='普通清单空模板导入返回错误信息，验证成功')
            #导入普通清单其他错误模板
            files11 = {'upload': ('conflict_normal.xls', open('C:/autotest_file/conflictRpt/conflict_impt.xls', 'rb'),'applicationnd.ms-excel')}
            result11=importConflictRptNormal(confictRptNormalData,files=files11)
            importmsg11={
                        'ticketId':result11,
                        'currentErrorRow':'0',
                        }
            rs11=getImportConflictRptMsgByTicketId(para=importmsg11)
            self.assertEquals(rs11['errorMsgs'][0], '数据模板有误，请下载最新模板','空模板导入验证失败')
            Log.LogOutput(message='普通清单其他错误模板导入返回错误信息，验证成功！')
            #导入普通清单正常模板
            files111 = {'upload': ('conflict_normal.xls', open('C:/autotest_file/conflictRpt/conflict_normal.xls', 'rb'),'applicationnd.ms-excel')}
            result111=importConflictRptNormal(confictRptNormalData,files=files111)
            importmsg111={
                        'ticketId':result111,
                        'currentErrorRow':'0',
                        }
            rs111=getImportConflictRptMsgByTicketId(para=importmsg111)
            self.assertEquals(rs111['description'], "{successMsg:'数据已保存，处理完成'}",'正常模板导入验证失败')
            Log.LogOutput(message='普通清单正常模板导入完毕，准备验证导入数据正确性')
            #验证导入模板中的第一条数据是否导入成功
            Log.LogOutput(message='验证普通清单导入后数据是否正确')
            listPara112=copy.deepcopy(conflictRptNormalListPara)
            checkPara112=copy.deepcopy(conflictRptNormalCheckPara)
            checkPara112['dealdate']='2016-08-08'
            checkPara112['departmentandperson']='责任单位及责任人001'
            checkPara112['name']='导入事项001'
            checkPara112['recorddate']='2016-06-06'
            checkPara112['typeName']='民族宗教'
            result112=checkConflictNormal(checkPara=checkPara112,listPara=listPara112)
            self.assertTrue(result112, '导入失败')
            Log.LogOutput(message='普通清单正常模板导入验证成功！')
            
            #导入重大清单
            #导入空模板
            Log.LogOutput( message='验证导入重大清单空模板是否有错误信息')
            confictRptImptData=copy.deepcopy(conflictRptImptImportData)
            files2 = {'upload': ('test.xls', open('C:/autotest_file/conflictRpt/conflict_impt_error.xls', 'rb'),'applicationnd.ms-excel')}
            result2=importConflictRptImpt(confictRptImptData,files=files2)
            importmsg2={
                        'ticketId':result2,
                        'currentErrorRow':'0',
                                }
            rs2=getImportConflictRptMsgByTicketId(para=importmsg2)
            self.assertEquals(rs2['errorMsgs'][0], '数据为空，请填入数据后重新导入','空模板导入验证失败')
            Log.LogOutput(message='重大清单空模板导入返回错误信息，验证成功')
            #导入重大清单其他错误模板
            files22 = {'upload': ('conflict_impt.xls', open('C:/autotest_file/conflictRpt/conflict_normal.xls', 'rb'),'applicationnd.ms-excel')}
            result22=importConflictRptImpt(confictRptImptData,files=files22)
            importmsg22={
                        'ticketId':result22,
                        'currentErrorRow':'0',
                        }
            rs22=getImportConflictRptMsgByTicketId(para=importmsg22)
            self.assertEquals(rs22['errorMsgs'][0], '数据模板有误，请下载最新模板','空模板导入验证失败')
            Log.LogOutput(message='重大清单其他错误模板导入返回错误信息，验证成功！')
            #导入重大清单正常模板
            files222 = {'upload': ('conflict_impt.xls', open('C:/autotest_file/conflictRpt/conflict_impt.xls', 'rb'),'applicationnd.ms-excel')}
            result222=importConflictRptImpt(confictRptImptData,files=files222)
            importmsg222={
                        'ticketId':result222,
                        'currentErrorRow':'0',
                        }
            rs222=getImportConflictRptMsgByTicketId(para=importmsg222)
            self.assertEquals(rs222['description'], "{successMsg:'数据已保存，处理完成'}",'正常模板导入验证失败')
            Log.LogOutput(message='重大清单正常模板导入完毕，准备验证导入数据正确性')
            #验证导入模板中的第一条数据是否导入成功
            Log.LogOutput(message='验证重大清单导入后数据是否正确')
            listPara222=copy.deepcopy(conflictRptImptListPara)
            listPara222['yearDate']='2016'
            listPara222['reportTime']='1'
            checkPara222=copy.deepcopy(conflictRptImptCheckPara)
            checkPara222['basicSituation']='基本情况001'
            checkPara222['developSituation']='进展情况001'
            checkPara222['disputesType']='导入类型001'
            checkPara222['involveSituation']='所涉群体及人数001'
            checkPara222['ondutyTarget']='责任单位及责任人001'
            checkPara222['workingMeasure']='工作措施001'
            result222=checkConflictImpt(checkPara=checkPara222,listPara=listPara222)
            self.assertTrue(result222, '导入失败')
            Log.LogOutput(message='重大清单正常模板导入验证成功！')
            pass
        
    '''
    @功能：重大矛盾纠纷清单新增数据与记录表数据统计是否一致
    @ chenhui 2016-1-18
    '''         
    def testConflictRpt_007(self):
        '''重大清单统计数据功能'''
        #仿真环境下跳过测试
        if simulationEnvironment is True:
            pass
        else:
            #首先新增记录表
            rptRecdPara=copy.deepcopy(confictRptRecordPara)      
            rptRecdPara['dailyYear.id']=getDbQueryResult(dbCommand = "select id from dailyYears d where d.yeardate='2016' and d.makedorgid='%s'and d.dailytype='0'"%orgInit['DftJieDaoOrgId'])
            rptRecdPara['dailyDirectory.id']=getDbQueryResult(dbCommand ="select id from newdailyDirectorys d where d.dailyyearid='%s' and d.shortname='月报'"%rptRecdPara['dailyYear.id'])
            addConflictRecord(para=rptRecdPara,username=userInit['DftSheQuUser'])
            #新增重大清单 conflictRptImpt.status 0 存量 1 新增(排查) 2 化解(调处)
            conflictImptPara=copy.deepcopy(conflictRptImptPara1)       
            rs=addConflictImpt(para=conflictImptPara)
            #检查记录表中的数据统计是否正确
            conflictImptDataCountParam=copy.deepcopy(conflictImptDataCountPara)
            result=getConflictRptImptDataCount(para=conflictImptDataCountParam)
            Log.LogOutput(message='验证数据正确性..')
            self.assertEqual(result['investigationNum'], 0, '排查数统计错误')
            self.assertEqual(result['stockNum'], 1, '存量数统计错误')
            self.assertEqual(result['successNum'], 0, '化解数统计错误')
            #修改类型为新增
            updPara=copy.deepcopy(conflictRptImptPara1)
            updPara['mode']='edit'
            updPara['conflictRptImpt.id']=rs['id']
            updPara['conflictRptImpt.status']=1
            updConflictImpt(para=updPara)
            result1=getConflictRptImptDataCount(para=conflictImptDataCountPara)
            Log.LogOutput(message='验证数据正确性..')
            self.assertEqual(result1['investigationNum'], 1, '排查数统计错误')
            self.assertEqual(result1['stockNum'], 0, '存量数统计错误')
            self.assertEqual(result1['successNum'], 0, '化解数统计错误')
            #修改类型为化解
            updPara['conflictRptImpt.status']=2
            updConflictImpt(para=updPara)
            result2=getConflictRptImptDataCount(para=conflictImptDataCountPara)
            Log.LogOutput(message='验证数据正确性..')
            self.assertEqual(result2['investigationNum'],0, '排查数统计错误')
            self.assertEqual(result2['stockNum'], 0, '存量数统计错误')
            self.assertEqual(result2['successNum'], 1, '化解数统计错误')
            Log.LogOutput(message='重大矛盾纠纷排查报表统计数据验证通过！')
            pass
        
    '''
    @功能：记录表新增并上报后下个月的初始化报表的年度累计是否正确
    @ chenhui 2016-1-18
    '''         
    def testConflictRpt_008(self):
        '''记录表上报后下个月的默认年度统计数据是否正确'''
        #仿真环境下跳过测试
        if simulationEnvironment is True:
            pass
        else:
    #        deleteAllReport()
            #新增报表并上报
            #设置2016年1月份新增参数
            rptRecdPara=copy.deepcopy(confictRptRecordPara1)      
            rptRecdPara['dailyYear.id']=getDbQueryResult(dbCommand = "select id from dailyYears d where d.yeardate='2016' and d.makedorgid='%s'and d.dailytype='0'"%orgInit['DftJieDaoOrgId'])
            rptRecdPara['dailyDirectory.id']=getDbQueryResult(dbCommand ="select id from newdailyDirectorys d where d.dailyyearid='%s' and d.shortname='月报'"%rptRecdPara['dailyYear.id'])
            
            rs=addConflictRecord(para=rptRecdPara,username=userInit['DftSheQuUser'])
            #上报参数
            para={
                  'id':rs,
                  'reportTypeInternalId':1,
                  }
            rptRecdPara['dealPerson']='签发人'
            rptRecdPara['lister']='制表人'
            reportConflictRecord(para=para)
            #导入重大矛盾纠纷清单
            confictRptImptData=copy.deepcopy(conflictRptImptImportData)
            
            files = {'upload': ('conflict_impt.xls', open('C:/autotest_file/conflictRpt/conflict_impt.xls', 'rb'),'applicationnd.ms-excel')}
            result=importConflictRptImpt(confictRptImptData,files=files)
            importmsg={
                        'ticketId':result,
                        'currentErrorRow':'0',
                        }
            r=getImportConflictRptMsgByTicketId(para=importmsg)
            self.assertEquals(r['description'], "{successMsg:'数据已保存，处理完成'}",'正常模板导入验证失败')
            #验证2月份报表新增页面默认年度累计是否正确
            para={
            'dailyDirectory.id':getDbQueryResult(dbCommand ="select id from newdailyDirectorys d where d.dailyyearid='%s' and d.shortname='月报'"%rptRecdPara['dailyYear.id']),
            'reportTime':'2',
            'organization.id':orgInit['DftSheQuOrgId'],
            'dailyYear.yearDate':'2016',
            'reportTypeInternalId':'1',
            'conflictRpt.id':'',
                }
            dataDict=getConflictRptDataByYear(para=para)
            self.assertEqual(str(dataDict[0]['yearNumPc']), rptRecdPara['conflictRptDatasList[18].yearNumPc'], '年度累计排查默认数据错误')
            self.assertEqual(str(dataDict[0]['yearNumSucc']), rptRecdPara['conflictRptDatasList[18].yearNumSucc'], '年度累计成功默认数据错误')
            self.assertEqual(str(dataDict[1]['yearNumPc']), rptRecdPara['conflictRptDatasList[17].yearNumPc'], '年度累计排查默认数据错误')
            self.assertEqual(str(dataDict[1]['yearNumSucc']), rptRecdPara['conflictRptDatasList[17].yearNumSucc'], '年度累计成功默认数据错误')
            self.assertEqual(str(dataDict[2]['yearNumPc']), rptRecdPara['conflictRptDatasList[16].yearNumPc'], '年度累计排查默认数据错误')
            self.assertEqual(str(dataDict[2]['yearNumSucc']), rptRecdPara['conflictRptDatasList[16].yearNumSucc'], '年度累计成功默认数据错误')
            self.assertEqual(str(dataDict[3]['yearNumPc']), rptRecdPara['conflictRptDatasList[15].yearNumPc'], '年度累计排查默认数据错误')
            self.assertEqual(str(dataDict[3]['yearNumSucc']), rptRecdPara['conflictRptDatasList[15].yearNumSucc'], '年度累计成功默认数据错误')
            self.assertEqual(str(dataDict[4]['yearNumPc']), rptRecdPara['conflictRptDatasList[14].yearNumPc'], '年度累计排查默认数据错误')
            self.assertEqual(str(dataDict[4]['yearNumSucc']), rptRecdPara['conflictRptDatasList[14].yearNumSucc'], '年度累计成功默认数据错误')
            self.assertEqual(str(dataDict[5]['yearNumPc']), rptRecdPara['conflictRptDatasList[13].yearNumPc'], '年度累计排查默认数据错误')
            self.assertEqual(str(dataDict[5]['yearNumSucc']), rptRecdPara['conflictRptDatasList[13].yearNumSucc'], '年度累计成功默认数据错误')
            self.assertEqual(str(dataDict[6]['yearNumPc']), rptRecdPara['conflictRptDatasList[12].yearNumPc'], '年度累计排查默认数据错误')
            self.assertEqual(str(dataDict[6]['yearNumSucc']), rptRecdPara['conflictRptDatasList[12].yearNumSucc'], '年度累计成功默认数据错误')
            self.assertEqual(str(dataDict[7]['yearNumPc']), rptRecdPara['conflictRptDatasList[11].yearNumPc'], '年度累计排查默认数据错误')
            self.assertEqual(str(dataDict[7]['yearNumSucc']), rptRecdPara['conflictRptDatasList[11].yearNumSucc'], '年度累计成功默认数据错误')
            self.assertEqual(str(dataDict[8]['yearNumPc']), rptRecdPara['conflictRptDatasList[10].yearNumPc'], '年度累计排查默认数据错误')
            self.assertEqual(str(dataDict[8]['yearNumSucc']), rptRecdPara['conflictRptDatasList[10].yearNumSucc'], '年度累计成功默认数据错误')
            self.assertEqual(str(dataDict[9]['yearNumPc']), rptRecdPara['conflictRptDatasList[9].yearNumPc'], '年度累计排查默认数据错误')
            self.assertEqual(str(dataDict[9]['yearNumSucc']), rptRecdPara['conflictRptDatasList[9].yearNumSucc'], '年度累计成功默认数据错误')
            self.assertEqual(str(dataDict[10]['yearNumPc']), rptRecdPara['conflictRptDatasList[8].yearNumPc'], '年度累计排查默认数据错误')
            self.assertEqual(str(dataDict[10]['yearNumSucc']), rptRecdPara['conflictRptDatasList[8].yearNumSucc'], '年度累计成功默认数据错误')
            self.assertEqual(str(dataDict[11]['yearNumPc']), rptRecdPara['conflictRptDatasList[7].yearNumPc'], '年度累计排查默认数据错误')
            self.assertEqual(str(dataDict[11]['yearNumSucc']), rptRecdPara['conflictRptDatasList[7].yearNumSucc'], '年度累计成功默认数据错误')
            self.assertEqual(str(dataDict[12]['yearNumPc']), rptRecdPara['conflictRptDatasList[6].yearNumPc'], '年度累计排查默认数据错误')
            self.assertEqual(str(dataDict[12]['yearNumSucc']), rptRecdPara['conflictRptDatasList[6].yearNumSucc'], '年度累计成功默认数据错误')
            self.assertEqual(str(dataDict[13]['yearNumPc']), rptRecdPara['conflictRptDatasList[5].yearNumPc'], '年度累计排查默认数据错误')
            self.assertEqual(str(dataDict[13]['yearNumSucc']), rptRecdPara['conflictRptDatasList[5].yearNumSucc'], '年度累计成功默认数据错误')
            self.assertEqual(str(dataDict[14]['yearNumPc']), rptRecdPara['conflictRptDatasList[4].yearNumPc'], '年度累计排查默认数据错误')
            self.assertEqual(str(dataDict[14]['yearNumSucc']), rptRecdPara['conflictRptDatasList[4].yearNumSucc'], '年度累计成功默认数据错误')
            self.assertEqual(str(dataDict[15]['yearNumPc']), rptRecdPara['conflictRptDatasList[3].yearNumPc'], '年度累计排查默认数据错误')
            self.assertEqual(str(dataDict[15]['yearNumSucc']), rptRecdPara['conflictRptDatasList[3].yearNumSucc'], '年度累计成功默认数据错误')
            self.assertEqual(str(dataDict[16]['yearNumPc']), rptRecdPara['conflictRptDatasList[2].yearNumPc'], '年度累计排查默认数据错误')
            self.assertEqual(str(dataDict[16]['yearNumSucc']), rptRecdPara['conflictRptDatasList[2].yearNumSucc'], '年度累计成功默认数据错误')
            self.assertEqual(str(dataDict[17]['yearNumPc']), rptRecdPara['conflictRptDatasList[1].yearNumPc'], '年度累计排查默认数据错误')
            self.assertEqual(str(dataDict[17]['yearNumSucc']), rptRecdPara['conflictRptDatasList[1].yearNumSucc'], '年度累计成功默认数据错误')
            self.assertEqual(str(dataDict[18]['yearNumPc']), rptRecdPara['conflictRptDatasList[0].yearNumPc'], '年度累计排查默认数据错误')
            self.assertEqual(str(dataDict[18]['yearNumSucc']), rptRecdPara['conflictRptDatasList[0].yearNumSucc'], '年度累计成功默认数据错误')
            self.assertEqual(str(dataDict[19]['yearNumPc']), '1', '重大矛盾纠纷排查数默认显示正确')
            self.assertEqual(str(dataDict[19]['yearNumCl']), '2', '重大矛盾纠纷存量数默认显示正确')
            self.assertEqual(str(dataDict[19]['yearNumSucc']), '3', '重大矛盾纠纷成功数默认显示正确')
            Log.LogOutput( message='2月份默认年度累计数据正确')
            #验证街道新增页面默认年度累计数据是否正确
            #上报1月份报表
            
            para2={
            'dailyDirectory.id':getDbQueryResult(dbCommand ="select id from newdailyDirectorys d where d.dailyyearid='%s' and d.shortname='月报'"%rptRecdPara['dailyYear.id']),
            'reportTime':'1',
            'organization.id':orgInit['DftJieDaoOrgId'],
            'dailyYear.yearDate':'2016',
            'reportTypeInternalId':'1',
            'conflictRpt.id':'',       
                   }
            dataDict2=getConflictRptDataByYear2(para=para2)
            self.assertEqual(str(dataDict2[0]['investigationNum']), rptRecdPara['conflictRptDatasList[0].yearNumPc'], '年度累计排查数错误')
            self.assertEqual(str(dataDict2[0]['successNum']), rptRecdPara['conflictRptDatasList[0].yearNumPc'], '年度累计成功数错误')
            self.assertEqual(str(dataDict2[1]['investigationNum']), rptRecdPara['conflictRptDatasList[5].yearNumPc'], '年度累计排查数错误')
            self.assertEqual(str(dataDict2[1]['successNum']), rptRecdPara['conflictRptDatasList[5].yearNumPc'], '年度累计成功数错误')
            self.assertEqual(str(dataDict2[2]['investigationNum']), rptRecdPara['conflictRptDatasList[10].yearNumPc'], '年度累计排查数错误')
            self.assertEqual(str(dataDict2[2]['successNum']), rptRecdPara['conflictRptDatasList[10].yearNumPc'], '年度累计成功数错误')
            self.assertEqual(str(dataDict2[3]['investigationNum']), rptRecdPara['conflictRptDatasList[12].yearNumPc'], '年度累计排查数错误')
            self.assertEqual(str(dataDict2[3]['successNum']), rptRecdPara['conflictRptDatasList[12].yearNumPc'], '年度累计成功数错误')
            self.assertEqual(str(dataDict2[4]['investigationNum']), rptRecdPara['conflictRptDatasList[1].yearNumPc'], '年度累计排查数错误')
            self.assertEqual(str(dataDict2[4]['successNum']), rptRecdPara['conflictRptDatasList[1].yearNumPc'], '年度累计成功数错误')
            self.assertEqual(str(dataDict2[5]['investigationNum']), rptRecdPara['conflictRptDatasList[13].yearNumPc'], '年度累计排查数错误')
            self.assertEqual(str(dataDict2[5]['successNum']), rptRecdPara['conflictRptDatasList[13].yearNumPc'], '年度累计成功数错误')
            self.assertEqual(str(dataDict2[6]['investigationNum']), rptRecdPara['conflictRptDatasList[3].yearNumPc'], '年度累计排查数错误')
            self.assertEqual(str(dataDict2[6]['successNum']), rptRecdPara['conflictRptDatasList[3].yearNumPc'], '年度累计成功数错误')
            self.assertEqual(str(dataDict2[7]['investigationNum']), rptRecdPara['conflictRptDatasList[4].yearNumPc'], '年度累计排查数错误')
            self.assertEqual(str(dataDict2[7]['successNum']), rptRecdPara['conflictRptDatasList[4].yearNumPc'], '年度累计成功数错误')
            self.assertEqual(str(dataDict2[8]['investigationNum']), rptRecdPara['conflictRptDatasList[7].yearNumPc'], '年度累计排查数错误')
            self.assertEqual(str(dataDict2[8]['successNum']), rptRecdPara['conflictRptDatasList[7].yearNumPc'], '年度累计成功数错误')
            self.assertEqual(str(dataDict2[9]['investigationNum']), rptRecdPara['conflictRptDatasList[16].yearNumPc'], '年度累计排查数错误')
            self.assertEqual(str(dataDict2[9]['successNum']), rptRecdPara['conflictRptDatasList[16].yearNumPc'], '年度累计成功数错误')
            self.assertEqual(str(dataDict2[10]['investigationNum']), rptRecdPara['conflictRptDatasList[2].yearNumPc'], '年度累计排查数错误')
            self.assertEqual(str(dataDict2[10]['successNum']), rptRecdPara['conflictRptDatasList[2].yearNumPc'], '年度累计成功数错误')
            self.assertEqual(str(dataDict2[11]['investigationNum']), rptRecdPara['conflictRptDatasList[6].yearNumPc'], '年度累计排查数错误')
            self.assertEqual(str(dataDict2[11]['successNum']), rptRecdPara['conflictRptDatasList[6].yearNumPc'], '年度累计成功数错误')
            self.assertEqual(str(dataDict2[12]['investigationNum']), rptRecdPara['conflictRptDatasList[17].yearNumPc'], '年度累计排查数错误')
            self.assertEqual(str(dataDict2[12]['successNum']), rptRecdPara['conflictRptDatasList[17].yearNumPc'], '年度累计成功数错误')
            self.assertEqual(str(dataDict2[19]['investigationNum']),'1', '年度累计排查数错误')
            self.assertEqual(str(dataDict2[19]['successNum']),'3', '年度累计成功数错误')
            self.assertEqual(str(dataDict2[19]['inventoryNum']),'2', '年度累计成功数错误')
            self.assertEqual(str(dataDict2[14]['investigationNum']), rptRecdPara['conflictRptDatasList[9].yearNumPc'], '年度累计排查数错误')
            self.assertEqual(str(dataDict2[14]['successNum']), rptRecdPara['conflictRptDatasList[9].yearNumPc'], '年度累计成功数错误')
            self.assertEqual(str(dataDict2[15]['investigationNum']), rptRecdPara['conflictRptDatasList[11].yearNumPc'], '年度累计排查数错误')
            self.assertEqual(str(dataDict2[15]['successNum']), rptRecdPara['conflictRptDatasList[11].yearNumPc'], '年度累计成功数错误')
            self.assertEqual(str(dataDict2[16]['investigationNum']), rptRecdPara['conflictRptDatasList[14].yearNumPc'], '年度累计排查数错误')
            self.assertEqual(str(dataDict2[16]['successNum']), rptRecdPara['conflictRptDatasList[14].yearNumPc'], '年度累计成功数错误')
            self.assertEqual(str(dataDict2[17]['investigationNum']), rptRecdPara['conflictRptDatasList[15].yearNumPc'], '年度累计排查数错误')
            self.assertEqual(str(dataDict2[17]['successNum']), rptRecdPara['conflictRptDatasList[15].yearNumPc'], '年度累计成功数错误')
            self.assertEqual(str(dataDict2[18]['investigationNum']), rptRecdPara['conflictRptDatasList[18].yearNumPc'], '年度累计排查数错误')
            self.assertEqual(str(dataDict2[18]['successNum']), rptRecdPara['conflictRptDatasList[18].yearNumPc'], '年度累计成功数错误')
            self.assertEqual(str(dataDict2[13]['investigationNum']), rptRecdPara['conflictRptDatasList[8].yearNumPc'], '年度累计排查数错误')
            self.assertEqual(str(dataDict2[13]['successNum']), rptRecdPara['conflictRptDatasList[8].yearNumPc'], '年度累计成功数错误')
            Log.LogOutput(message='街道新增报表年度累计默认数据显示正确')
            
            pass
    
 
    '''
    @功能：事件拉取普通清单数据功能
    @ chenhui 2016-1-18
    '''         
    def testConflictRpt_009(self):
        '''事件拉取普通清单job'''
        #仿真环境下跳过测试
        if simulationEnvironment is True:
            pass
        else:
            #标记位，判断try代码块是否有异常
            flag=True
            try: 
                #清空job监控表
                clearTable(tableName='JOBMONITOR')#job监控表
                #清空事件表
                deleteAllIssues2()
                
                #修改服务器时间为2016-1-16
                data='2016-1-16 '+getCurrentTime()
                setLinuxTime(data=data)
                setLinuxTimeYunWei(data=data,password='tianqueshuaige',serverIp='http://192.168.1.108:8080')
                #新增矛盾纠纷类型的事件 issue.important=true
                issueParam = copy.deepcopy(ShiJianChuLiPara.issueObject2)
                issueParam['selectOrgName']=orgInit['DftSheQuOrg']
                issueParam['issue.occurOrg.id']=orgInit['DftSheQuOrgId']
                issueParam['issue.occurDate']='2016-01-16'
                #结案参数
                sIssuePara=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)        
                sIssuePara['operation.dealOrg.id']=orgInit['DftSheQuOrgId']
                sIssuePara['operation.dealUserName']=userInit['DftSheQuUserXM']
                sIssuePara['operation.mobile']=userInit['DftSheQuUserSJ']
                sIssuePara['operation.content']='事件办结'      
                sIssuePara['dealCode']='31'#办理中
                count=1
                for i in range(1,20):
                    for j in range(1,i+1):
                        issueParam['selectedTypes']=i 
                        Log.LogOutput(message="正在新增第%d条事件"%count)
                        rs=ShiJianChuLiIntf.addIssue(issueDict=issueParam, username=userInit['DftSheQuUser'], password='11111111')
                        sIssuePara['operation.issue.id']=rs['issueId']
                        sIssuePara['keyId']=rs['issueStepId']
                        dealIssue(issueDict=sIssuePara,username=userInit['DftSheQuUser'])
                        count=count +1
                #添加非矛盾纠纷类型的干扰事件
                Log.LogOutput(message='添加非矛盾纠纷类型的干扰事件')
                #治安、安全隐患
                issueParam['selectedTypes']=20
                rs20=ShiJianChuLiIntf.addIssue(issueDict=issueParam, username=userInit['DftSheQuUser'], password='11111111')
                sIssuePara['operation.issue.id']=rs20['issueId']
                sIssuePara['keyId']=rs20['issueStepId']
                dealIssue(issueDict=sIssuePara,username=userInit['DftSheQuUser'])
                #民生服务
                issueParam['selectedTypes']=33
                rs33=ShiJianChuLiIntf.addIssue(issueDict=issueParam, username=userInit['DftSheQuUser'], password='11111111')
                sIssuePara['operation.issue.id']=rs33['issueId']
                sIssuePara['keyId']=rs33['issueStepId']
                dealIssue(issueDict=sIssuePara,username=userInit['DftSheQuUser'])
                #其他
                issueParam['selectedTypes']=getDbQueryResult(dbCommand = "select id from issuetypes i where i.domainid='4'")
                rs182=ShiJianChuLiIntf.addIssue(issueDict=issueParam, username=userInit['DftSheQuUser'], password='11111111')
                sIssuePara['operation.issue.id']=rs182['issueId']
                sIssuePara['keyId']=rs182['issueStepId']
                dealIssue(issueDict=sIssuePara,username=userInit['DftSheQuUser'])
                #修改服务器时间为2016-1-27
                data='2016-1-27 '+getCurrentTime()
                setLinuxTime(data=data)
                setLinuxTimeYunWei(data=data,password='tianqueshuaige',serverIp='http://192.168.1.108:8080')
                #      设置JOB：converLastMonthAddToInventorJob名称和延后执行时间参数，延后·10s
                jobTimePara={
                             'task.Data':setJobDelayTime(),
                             'task.name':'converLastMonthAddToInventorJob',
                             'job.name':'converLastMonthAddToInventorJob'
                             }
                runJob(jobPara=jobTimePara)
                #设置JOB:newStateConflictAnalyzingDataJob的名称和延后执行时间
                jobTimePara2={
                             'task.Data':setJobDelayTime(),
                             'task.name':'newStateConflictAnalyzingDataJob',
                             'job.name':'newStateConflictAnalyzingDataJob'
                             }
                runJob(jobPara=jobTimePara2)
                dailyYearId=getDbQueryResult(dbCommand = "select id from dailyYears d where d.yeardate='2016' and d.makedorgid='%s'and d.dailytype='0'"%orgInit['DftJieDaoOrgId'])
                para={
                        'dailyDirectory.id':getDbQueryResult(dbCommand ="select id from newdailyDirectorys d where d.dailyyearid='%s' and d.shortname='月报'"%dailyYearId),
                        'reportTime':1,
                        'organization.id':orgInit['DftSheQuOrgId'],
                        'dailyYear.yearDate':2016,
                        'reportTypeInternalId':1,
                        'conflictRpt.id':'',
                        }
                
                result=getConflictRptDatasType(para=para)
                Log.LogOutput(message='验证记录表事件数据正确性')
                self.assertEqual(result['conflictAnalyzingRptDataList'][0]['successnum'], 19, '其他类型成功数验证不正确')
                self.assertEqual(result['conflictAnalyzingRptDataList'][18]['successnum'], 1, '成功总数验证不正确')
                #验证普通清单数据拉取是否正确：190
                Log.LogOutput(message='验证普通清单排查数和成功数数据正确性')
                para2=copy.deepcopy(conflictRptNormalListPara)
                para2['yearDate']=2016
                result2=getConflictNormalListNum(para=para2)
                self.assertEqual(result2['add'], 190, '普通清单新增数验证错误')
                self.assertEqual(result2['success'], 190, '普通清单成功数验证错误')
                #验证重大清单数据拉取是否正确：0
                Log.LogOutput(message='验证重大清单排查数和成功数数据正确性')
                para3=copy.deepcopy(conflictRptImptListPara)
                para3['yearDate']='2016'
                para3['reportTime']='1'
                result3=getConflictImptListNum(para=para3)
                self.assertEqual(result3['add'], 0, '重大矛盾纠纷排查数验证失败')
                self.assertEqual(result3['success'], 0, '重大矛盾纠纷化解数验证失败')
            except Exception :
                flag=False
            finally:
                #将服务器时间改回正确时间
                setLinuxTime(data=getCurrentDateAndTime())
                setLinuxTimeYunWei(data=getCurrentDateAndTime(),password='tianqueshuaige',serverIp='http://192.168.1.108:8080')
                self.assertTrue(flag, '用例执行过程出现异常')

    '''
    @功能：事件拉取重大清单数据功能
    @ chenhui 2016-1-25
    '''   
    #此脚本跑完，消费者会出现挂掉的情况，暂时不测试      
#     def testConflictRpt_010(self):
#         '''事件拉取重大清单job'''
#         #仿真环境下跳过测试
#         if simulationEnvironment is True:
#             pass
#         else:
#             #标记位，判断try代码块是否有异常
#             flag=True
#             try:
#                 #清空job监控表
#                 clearTable(tableName='JOBMONITOR')#job监控表
#                 deleteAllIssues2()
#                 #再次清空表，出现过初始化未清空表的情况，原因未知
#                 deleteAllReport()
#                 #修改服务器时间为2016-1-16
#                 Data='2016-1-16 '+getCurrentTime()
#                 setLinuxTime(Data=Data)
#                 #新增矛盾纠纷类型的事件 issue.important=true
#                 issueParam = copy.deepcopy(ShiJianChuLiPara.issueObject2)
#                 issueParam['selectOrgName']=orgInit['DftSheQuOrg']
#                 issueParam['issue.occurOrg.id']=orgInit['DftSheQuOrgId']
#                 issueParam['issue.occurDate']='2016-01-16'
#                 issueParam['issue.important']='true'
#                 #结案参数
#                 sIssuePara=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)        
#                 sIssuePara['operation.dealOrg.id']=orgInit['DftSheQuOrgId']
#                 sIssuePara['operation.dealUserName']=userInit['DftSheQuUserXM']
#                 sIssuePara['operation.mobile']=userInit['DftSheQuUserSJ']
#                 sIssuePara['operation.content']='事件办结'      
#                 sIssuePara['dealCode']='31'#办理中
#                 for i in range(1,20):
#                         issueParam['selectedTypes']=i 
#                         Log.LogOutput(message="正在新增第%d条事件"%i)
#                         rs=ShiJianChuLiIntf.addIssue(issueDict=issueParam, username=userInit['DftSheQuUser'], password='11111111')
#                         sIssuePara['operation.issue.id']=rs['issueId']
#                         sIssuePara['keyId']=rs['issueStepId']
#                         dealIssue(issueDict=sIssuePara,username=userInit['DftSheQuUser'])
#                 #添加非矛盾纠纷类型的干扰事件
#                 Log.LogOutput(message='添加非矛盾纠纷类型的干扰事件')
#                 #治安、安全隐患
#                 issueParam['selectedTypes']=20
#                 rs20=ShiJianChuLiIntf.addIssue(issueDict=issueParam, username=userInit['DftSheQuUser'], password='11111111')
#                 sIssuePara['operation.issue.id']=rs20['issueId']
#                 sIssuePara['keyId']=rs20['issueStepId']
#                 dealIssue(issueDict=sIssuePara,username=userInit['DftSheQuUser'])
#                 #民生服务
#                 issueParam['selectedTypes']=33
#                 rs33=ShiJianChuLiIntf.addIssue(issueDict=issueParam, username=userInit['DftSheQuUser'], password='11111111')
#                 sIssuePara['operation.issue.id']=rs33['issueId']
#                 sIssuePara['keyId']=rs33['issueStepId']
#                 dealIssue(issueDict=sIssuePara,username=userInit['DftSheQuUser'])
#                 #其他
#                 issueParam['selectedTypes']=getDbQueryResult(dbCommand = "select id from issuetypes i where i.domainid='4'")
#                 rs182=ShiJianChuLiIntf.addIssue(issueDict=issueParam, username=userInit['DftSheQuUser'], password='11111111')
#                 sIssuePara['operation.issue.id']=rs182['issueId']
#                 sIssuePara['keyId']=rs182['issueStepId']
#                 dealIssue(issueDict=sIssuePara,username=userInit['DftSheQuUser'])
#                 #修改服务器时间为2016-1-27
#                 Data='2016-1-27 '+getCurrentTime()
#                 setLinuxTime(Data=Data)
#                 #      设置JOB：converLastMonthAddToInventorJob名称和延后执行时间参数，默认延后30s
#                 jobTimePara={
#                              'task.Data':setJobDelayTime(),
#                              'task.name':'converLastMonthAddToInventorJob',
#                              'job.name':'converLastMonthAddToInventorJob'
#                              }
#                 runJob(jobPara=jobTimePara)
#                 #设置JOB:newStateConflictAnalyzingDataJob的名称和延后执行时间
#                 jobTimePara2={
#                              'task.Data':setJobDelayTime(),
#                              'task.name':'newStateConflictAnalyzingDataJob',
#                              'job.name':'newStateConflictAnalyzingDataJob'
#                              }
#                 runJob(jobPara=jobTimePara2)
#                 #设置JOB：ConverImportantLastMonthAddToInventorJob，本次测试关键job
#                 jobTimePara3={
#                              'task.Data':setJobDelayTime(),
#                              'task.name':'ConverImportantLastMonthAddToInventorJob',
#                              'job.name':'ConverImportantLastMonthAddToInventorJob'
#                              }
#                 runJob(jobPara=jobTimePara3)
#                 dailyYearId=getDbQueryResult(dbCommand = "select id from dailyYears d where d.yeardate='2016' and d.makedorgid='%s'and d.dailytype='0'"%orgInit['DftJieDaoOrgId'])
#                 para={
#                         'dailyDirectory.id':getDbQueryResult(dbCommand ="select id from newdailyDirectorys d where d.dailyyearid='%s' and d.shortname='月报'"%dailyYearId),
#                         'reportTime':1,
#                         'organization.id':orgInit['DftSheQuOrgId'],
#                         'dailyYear.yearDate':2016,
#                         'reportTypeInternalId':1,
#                         'conflictRpt.id':'',
#                         }
#                 result=getConflictRptDatasType(para=para)
#                 Log.LogOutput(message='验证记录表总况数据正确性')
#                 self.assertEqual(result['conflictAnalyZingRpt']['numInFifty'], 0, '总况排查总数验证不正确')
#                 self.assertEqual(result['conflictAnalyZingRpt']['totalSuccNum'], 0, '成功总数验证不正确')
#                 #验证普通清单数据拉取是否正确：0
#                 Log.LogOutput(message='验证普通清单排查数和成功数数据正确性')
#                 para2=copy.deepcopy(conflictRptNormalListPara)
#                 para2['yearDate']=2016
#                 result2=getConflictNormalListNum(para=para2)
#                 self.assertEqual(result2['add'], 0, '普通清单新增数验证错误')
#                 self.assertEqual(result2['success'], 0, '普通清单成功数验证错误')
#                 #验证重大清单数据拉取是否正确：19
#                 Log.LogOutput(message='验证重大清单排查数和成功数数据正确性')
#                 para3=copy.deepcopy(conflictRptImptListPara)
#                 para3['yearDate']='2016'
#                 para3['reportTime']='1'
#                 result3=getConflictImptListNum(para=para3)
#                 self.assertEqual(result3['add'], 19, '重大矛盾纠纷排查数验证失败')
#                 self.assertEqual(result3['success'], 19, '重大矛盾纠纷化解数验证失败')
#             except Exception,e:
#                 Log.LogOutput(LogLevel.ERROR, str(e))   
#                 flag=False
#             finally:
#                 #将服务器时间改回正确时间
#                 setLinuxTime(Data=getCurrentDateAndTime())
#                 self.assertTrue(flag, '用例执行过程出现异常')
#             pass 
    
    '''
    @功能：社会治安重点地区排查整治清单新增、修改
    @ chenhui 2016-1-18
    '''       
    def testConflictRpt_011(self):
        '''社会治安重点地区排查整治清单新增、修改'''
        #仿真环境下跳过测试
        if simulationEnvironment is True:
            pass
        else:
            #设置新增参数
            para=copy.deepcopy(socialSecurityAddPara1)
            dailyYearId=getDbQueryResult(dbCommand ="select id from dailyYears d where d.yeardate='2016' and d.makedorgid='%s' and d.name='2016年工作台账模版'"%orgInit['DftJieDaoOrgId'])
            para['dailyDirectory.id']=getDbQueryResult(dbCommand ="select id from newdailydirectorys d where d.dailyyearid='%s' and d.shortname='社会治安重点地区排查整治清单'"%dailyYearId)
            rs=addSocialSecurit(para=para)
            #验证新增功能
            checkPara={
                        'areaName': para['keyAreasOfInvestigationInfo.areaName'],
                        'investigationDate': para['keyAreasOfInvestigationInfo.investigationDate'],
                        'mainProblem': para['keyAreasOfInvestigationInfo.mainProblem'],
                        'policiesAndMeasures': para['keyAreasOfInvestigationInfo.policiesAndMeasures'],
                       }
            listPara=copy.deepcopy(socialSecurityListPara)
            listPara['dailyDirectory.id']=para['dailyDirectory.id']
            listPara['organization.id']=orgInit['DftSheQuOrgId']      
            result=checkSocialSecurit(checkPara=checkPara,listPara=listPara)
            self.assertTrue(result)
            #修改
            editPara=copy.deepcopy(socialSecurityAddPara)
            editPara['mode']='edit'
            editPara['keyAreasOfInvestigationInfo.id']=rs['id']
            editPara['keyAreasOfInvestigationInfo.areaName']='地区名称1'
            editPara['keyAreasOfInvestigationInfo.investigationDate']='2016-01-01'
            editPara['keyAreasOfInvestigationInfo.warningOrListing']='警示或挂牌1'
            editPara['keyAreasOfInvestigationInfo.mainProblem']='主要问题1'
            editPara['keyAreasOfInvestigationInfo.policiesAndMeasures']='对策与措施1'
            editPara['keyAreasOfInvestigationInfo.remark']='备注1'
            updSocialSecurit(para=editPara)
            #验证修改功能
            checkPara2={
                        'areaName': editPara['keyAreasOfInvestigationInfo.areaName'],
                        'investigationDate':editPara['keyAreasOfInvestigationInfo.investigationDate'],
                        'mainProblem': editPara['keyAreasOfInvestigationInfo.mainProblem'],
                        'policiesAndMeasures': editPara['keyAreasOfInvestigationInfo.policiesAndMeasures'],
                        'warningOrListing':editPara['keyAreasOfInvestigationInfo.warningOrListing'],
                        'remark':editPara['keyAreasOfInvestigationInfo.remark']
                       }
            result2=checkSocialSecurit(checkPara=checkPara2,listPara=listPara)
            self.assertTrue(result2)
            pass
        
    '''
    @功能：社会治安重点地区排查整治清单新增、修改
    @ chenhui 2016-1-18
    '''       
    def testConflictRpt_012(self):
        '''社会治安重点地区排查整治清单删除'''
        #仿真环境下跳过测试
        if simulationEnvironment is True:
            pass
        else:
            #新增        
            para=copy.deepcopy(socialSecurityAddPara1)
            dailyYearId=getDbQueryResult(dbCommand ="select id from dailyYears d where d.yeardate='2016' and d.makedorgid='%s' and d.name='2016年工作台账模版'"%orgInit['DftJieDaoOrgId'])
            para['dailyDirectory.id']=getDbQueryResult(dbCommand ="select id from newdailydirectorys d where d.dailyyearid='%s' and d.shortname='社会治安重点地区排查整治清单'"%dailyYearId)
            rs=addSocialSecurit(para=para)
            #删除
            delSocialSecurit(para={'keyAreasOfInvestigationInfoids':rs['id']})
            #验证删除功能
            checkPara={
                        'areaName': para['keyAreasOfInvestigationInfo.areaName'],
                        'investigationDate': para['keyAreasOfInvestigationInfo.investigationDate'],
                        'mainProblem': para['keyAreasOfInvestigationInfo.mainProblem'],
                        'policiesAndMeasures': para['keyAreasOfInvestigationInfo.policiesAndMeasures'],
                       }
            listPara=copy.deepcopy(socialSecurityListPara)
            listPara['dailyDirectory.id']=para['dailyDirectory.id']
            listPara['organization.id']=orgInit['DftSheQuOrgId'] 
            result=checkSocialSecurit(checkPara=checkPara,listPara=listPara)
            self.assertFalse(result, '删除验证失败')
            Log.LogOutput( message='删除验证成功！')
            pass
    
    '''
    @功能：社会治安重点地区排查整治清单上报、回退
    @ chenhui 2016-1-18
    '''       
    def testConflictRpt_013(self):
        '''社会治安重点地区排查整治清单上报、回退'''
        #仿真环境下跳过测试
        if simulationEnvironment is True:
            pass
        else:
    #        deleteAllReport()
            #新增
            para=copy.deepcopy(socialSecurityAddPara1)
            dailyYearId=getDbQueryResult(dbCommand ="select id from dailyYears d where d.yeardate='2016' and d.makedorgid='%s' and d.name='2016年工作台账模版'"%orgInit['DftJieDaoOrgId'])
            para['dailyDirectory.id']=getDbQueryResult(dbCommand ="select id from newdailydirectorys d where d.dailyyearid='%s' and d.shortname='社会治安重点地区排查整治清单'"%dailyYearId)
            rs=addSocialSecurit(para=para)
            #上报
            reportPara={
                 'keyAreasOfInvestigationInfoids':rs['id'],
                 'keyAreasOfInvestigationInfo.dailyDirectory.id':para['dailyDirectory.id']      
                        }
            reportSocialSecurit(para=reportPara)
            #验证上报功能
            checkPara1={
                        'status':1,
                        'id': rs['id']
                        }
            listPara1=copy.deepcopy(socialSecurityListPara)
            listPara1['dailyDirectory.id']=para['dailyDirectory.id']
            listPara1['organization.id']=orgInit['DftSheQuOrgId'] 
            r=checkSocialSecurit(checkPara=checkPara1,listPara=listPara1)
            self.assertTrue(r, '社区层级上报验证失败')
            checkPara2={
                        'status':0,
                        'id': rs['id']+1#上报后ID加1，新生成一条数据
                        }
            #街道层级的dailyDirectoryId不同
            dailyYearId2=getDbQueryResult(dbCommand ="select id from dailyYears d where d.yeardate='2016' and d.makedorgid='%s' and d.name='2016年工作台账模版'"%orgInit['DftQuOrgId'])
            dailyDirectoryId=getDbQueryResult(dbCommand ="select id from newdailydirectorys d where d.dailyyearid='%s' and d.shortname='社会治安重点地区排查整治清单'"%dailyYearId2)
            listPara2=copy.deepcopy(socialSecurityListPara)
            listPara2['dailyDirectory.id']= dailyDirectoryId
            listPara2['organization.id']=orgInit['DftJieDaoOrgId'] 
            r2=checkSocialSecurit(checkPara=checkPara2,listPara=listPara2,username=userInit['DftJieDaoUser'])
            self.assertTrue(r2, '街道层级上报验证失败')
            Log.LogOutput( message='上报功能验证通过！')
            #回退
            Log.LogOutput(message='即将验证回退功能..')
            backPara={
                      'keyAreasOfInvestigationInfoids':rs['id']+1,
                      'subOrgIds':orgInit['DftJieDaoOrgId'] ,
                      'platformMessage.title':'治安重点地区排查情况信息回退提醒!',
                      'platformMessage.content':'描述'
                      }
            backSocialSecurit(para=backPara)
            #验证回退功能
            checkPara3={
                        'status':2,
                        'id': rs['id']+1
                        }
            r3=checkSocialSecurit(checkPara=checkPara3,listPara=listPara2,username=userInit['DftJieDaoUser'])
            self.assertFalse(r3, '街道层级回退验证失败')
            checkPara4={
                    'status':2,
                    'id': rs['id']
                    }
            r4=checkSocialSecurit(checkPara=checkPara4,listPara=listPara1)
            self.assertTrue(r4, '社区层级回退验证失败')
            Log.LogOutput( message='回退功能验证通过！')
            pass


    '''
    @功能：社会治安重点地区排查整治季报新增
    @ chenhui 2016-1-18
    '''       
    def testConflictRpt_014(self):
        '''社会治安重点地区排查整治季报新增、修改'''
        #仿真环境下跳过测试
        if simulationEnvironment is True:
            pass
        else:
            #新增
            addPara=copy.deepcopy(socialSecurityReportAddPara1)
            addPara['dailyYear.id']=getDbQueryResult(dbCommand ="select id from dailyYears d where d.yeardate='2016' and d.makedorgid='%s' and d.name='2016年工作台账模版'"%orgInit['DftJieDaoOrgId'])
            addPara['dailyDirectory.id']=getDbQueryResult(dbCommand ="select id from newdailydirectorys d where d.dailyyearid='%s' and d.shortname='季报'"%addPara['dailyYear.id'])
            addPara['societyInvestigationRemediation.name']='2016年第一季度测试自动化社区社会治安重点地区排查整治工作情况表'#'2016%E5%B9%B4%E7%AC%AC%E4%B8%80%E5%AD%A3%E5%BA%A6%E6%B5%8B%E8%AF%95%E8%87%AA%E5%8A%A8%E5%8C%96%E7%A4%BE%E5%8C%BA%E7%A4%BE%E4%BC%9A%E6%B2%BB%E5%AE%89%E9%87%8D%E7%82%B9%E5%9C%B0%E5%8C%BA%E6%8E%92%E6%9F%A5%E6%95%B4%E6%B2%BB%E5%B7%A5%E4%BD%9C%E6%83%85%E5%86%B5%E8%A1%A8'
            result=addSocialSecuritRpt(para=addPara)
            self.assertTrue(result,'新增失败')
            #验证新增
            checkPara={
                       'lister':addPara['societyInvestigationRemediation.lister'],
                       'name':addPara['societyInvestigationRemediation.name']
                       }
            listPara=copy.deepcopy(socialSecurityReportListPara)
            listPara['dailyDirectoryId']=addPara['dailyDirectory.id']
            rs=checkSocialSecuritRpt(checkPara=checkPara,listPara=listPara)
            self.assertTrue(rs, '新增验证失败')
            #修改
            updPara=copy.deepcopy(addPara)
            updPara['societyInvestigationRemediation.id']=result['id']
            updPara['lister']='bbb1'
            updPara['societyInvestigationRemediation.name']='2016年第一季度测试自动化社区社会治安重点地区排查整治工作情况表123'#'2016%E5%B9%B4%E7%AC%AC%E4%B8%80%E5%AD%A3%E5%BA%A6%E6%B5%8B%E8%AF%95%E8%87%AA%E5%8A%A8%E5%8C%96%E7%A4%BE%E5%8C%BA%E7%A4%BE%E4%BC%9A%E6%B2%BB%E5%AE%89%E9%87%8D%E7%82%B9%E5%9C%B0%E5%8C%BA%E6%8E%92%E6%9F%A5%E6%95%B4%E6%B2%BB%E5%B7%A5%E4%BD%9C%E6%83%85%E5%86%B5%E8%A1%A8'
        
            updSocialSecuritRpt(para=updPara)
            #验证修改
            checkPara2={
                       'lister':updPara['societyInvestigationRemediation.lister'],
                       'name':updPara['societyInvestigationRemediation.name']
                       }
            rs2=checkSocialSecuritRpt(checkPara=checkPara2,listPara=listPara)
            self.assertTrue(rs2, '修改验证失败')
            pass    
    
    '''
    @功能：社会治安重点地区排查整治季报删除
    @ chenhui 2016-2-2
    '''       
    def testConflictRpt_015(self):
        '''社会治安重点地区排查整治季报删除'''
        #仿真环境下跳过测试
        if simulationEnvironment is True:
            pass
        else:
            #新增
            addPara=copy.deepcopy(socialSecurityReportAddPara1)
            addPara['dailyYear.id']=getDbQueryResult(dbCommand ="select id from dailyYears d where d.yeardate='2016' and d.makedorgid='%s' and d.name='2016年工作台账模版'"%orgInit['DftJieDaoOrgId'])
            addPara['dailyDirectory.id']=getDbQueryResult(dbCommand ="select id from newdailydirectorys d where d.dailyyearid='%s' and d.shortname='季报'"%addPara['dailyYear.id'])
            addPara['societyInvestigationRemediation.name']='2016年第一季度测试自动化社区社会治安重点地区排查整治工作情况表'#'2016%E5%B9%B4%E7%AC%AC%E4%B8%80%E5%AD%A3%E5%BA%A6%E6%B5%8B%E8%AF%95%E8%87%AA%E5%8A%A8%E5%8C%96%E7%A4%BE%E5%8C%BA%E7%A4%BE%E4%BC%9A%E6%B2%BB%E5%AE%89%E9%87%8D%E7%82%B9%E5%9C%B0%E5%8C%BA%E6%8E%92%E6%9F%A5%E6%95%B4%E6%B2%BB%E5%B7%A5%E4%BD%9C%E6%83%85%E5%86%B5%E8%A1%A8'
            result=addSocialSecuritRpt(para=addPara)
            self.assertTrue(result,'新增失败')
            #删除
            delSocialSecuritRpt(para={'societyInvestigationRemediation.id':result['id']})
            #验证删除
            checkPara={
                       'lister':addPara['societyInvestigationRemediation.lister'],
                       'name':addPara['societyInvestigationRemediation.name']
                       }
            listPara=copy.deepcopy(socialSecurityReportListPara)
            listPara['dailyDirectoryId']=addPara['dailyDirectory.id']
            rs=checkSocialSecuritRpt(checkPara=checkPara,listPara=listPara)
            self.assertFalse(rs, '新增验证失败')
            pass    
    
    '''
    @功能：社会治安重点地区排查整治季报上报
    @ chenhui 2016-2-2
    '''       
    def testConflictRpt_016(self):
        '''社会治安重点地区排查整治季报上报'''
        #仿真环境下跳过测试
        if simulationEnvironment is True:
            pass
        else:
            #新增
            addPara=copy.deepcopy(socialSecurityReportAddPara1)
            addPara['dailyYear.id']=getDbQueryResult(dbCommand ="select id from dailyYears d where d.yeardate='2016' and d.makedorgid='%s' and d.name='2016年工作台账模版'"%orgInit['DftJieDaoOrgId'])
            addPara['dailyDirectory.id']=getDbQueryResult(dbCommand ="select id from newdailydirectorys d where d.dailyyearid='%s' and d.shortname='季报'"%addPara['dailyYear.id'])
            addPara['societyInvestigationRemediation.name']='2016年第一季度测试自动化社区社会治安重点地区排查整治工作情况表'#'2016%E5%B9%B4%E7%AC%AC%E4%B8%80%E5%AD%A3%E5%BA%A6%E6%B5%8B%E8%AF%95%E8%87%AA%E5%8A%A8%E5%8C%96%E7%A4%BE%E5%8C%BA%E7%A4%BE%E4%BC%9A%E6%B2%BB%E5%AE%89%E9%87%8D%E7%82%B9%E5%9C%B0%E5%8C%BA%E6%8E%92%E6%9F%A5%E6%95%B4%E6%B2%BB%E5%B7%A5%E4%BD%9C%E6%83%85%E5%86%B5%E8%A1%A8'
            result=addSocialSecuritRpt(para=addPara)
            self.assertTrue(result,'新增失败')
            #上报
            reportPara=copy.deepcopy(socialSecurityReportReportPara)
            reportPara['societyInvestigationRemediation.id']=result['id']
            reportPara['societyInvestigationRemediation.dailyDirectory.id']=addPara['dailyDirectory.id']
            rs=reportSocialSecuritRpt(para=reportPara)
            #验证上报
            self.assertNotEqual(rs['submitTime'], None, '上报验证失败')
            Log.LogOutput(message='上报成功！')
            pass

    '''
    @功能：社会治安重点地区排查整治季报上报后街道层级新增默认读取的数据是否正确
    @ chenhui 2016-2-2
    '''       
    def testConflictRpt_017(self):
        '''社会治安重点地区排查整治季报上报'''
        #仿真环境下跳过测试
        if simulationEnvironment is True:
            pass
        else:
            #新增
            addPara=copy.deepcopy(socialSecurityReportAddPara1)
            addPara['dailyYear.id']=getDbQueryResult(dbCommand ="select id from dailyYears d where d.yeardate='2016' and d.makedorgid='%s' and d.name='2016年工作台账模版'"%orgInit['DftJieDaoOrgId'])
            addPara['dailyDirectory.id']=getDbQueryResult(dbCommand ="select id from newdailydirectorys d where d.dailyyearid='%s' and d.shortname='季报'"%addPara['dailyYear.id'])
            addPara['societyInvestigationRemediation.name']='2016年第一季度测试自动化社区社会治安重点地区排查整治工作情况表'#'2016%E5%B9%B4%E7%AC%AC%E4%B8%80%E5%AD%A3%E5%BA%A6%E6%B5%8B%E8%AF%95%E8%87%AA%E5%8A%A8%E5%8C%96%E7%A4%BE%E5%8C%BA%E7%A4%BE%E4%BC%9A%E6%B2%BB%E5%AE%89%E9%87%8D%E7%82%B9%E5%9C%B0%E5%8C%BA%E6%8E%92%E6%9F%A5%E6%95%B4%E6%B2%BB%E5%B7%A5%E4%BD%9C%E6%83%85%E5%86%B5%E8%A1%A8'
            result=addSocialSecuritRpt(para=addPara)
            self.assertTrue(result,'新增失败')
            #上报
            reportPara=copy.deepcopy(socialSecurityReportReportPara)
            reportPara['societyInvestigationRemediation.id']=result['id']
            reportPara['societyInvestigationRemediation.dailyDirectory.id']=addPara['dailyDirectory.id']
            reportSocialSecuritRpt(para=reportPara)
            #验证街道账号新增时，默认参数是否正确
            para={
                  'dailyDirectory.id':addPara['dailyDirectory.id'],
                  'reportTime':1
                  }
            Log.LogOutput( message='正在验证街道新增默认数据是否正确')
            data=getSocialSecuritRptDataByReportTime(para=para)
            self.assertEqual(str(data['alreadyRenovateCounty']), addPara['societyInvestigationRemediation.alreadyRenovateCounty'], '数据验证失败')
            self.assertEqual(str(data['alreadyRenovateOther']), addPara['societyInvestigationRemediation.alreadyRenovateOther'], '数据验证失败')
            self.assertEqual(str(data['alreadyRenovateStreet']), addPara['societyInvestigationRemediation.alreadyRenovateStreet'], '数据验证失败')
            self.assertEqual(str(data['alreadyRenovateVillage']), addPara['societyInvestigationRemediation.alreadyRenovateVillage'], '数据验证失败')
            self.assertEqual(str(data['alreadyRenovateSum']), addPara['societyInvestigationRemediation.alreadyRenovateSum'], '数据验证失败')
            self.assertEqual(str(data['brandCity']), addPara['societyInvestigationRemediation.brandCity'], '数据验证失败')
            self.assertEqual(str(data['brandCounty']), addPara['societyInvestigationRemediation.brandCounty'], '数据验证失败')
            self.assertEqual(str(data['brandLand']), addPara['societyInvestigationRemediation.brandLand'], '数据验证失败')
            self.assertEqual(str(data['brandSum']), addPara['societyInvestigationRemediation.brandSum'], '数据验证失败')
            self.assertEqual(str(data['cautionCity']), addPara['societyInvestigationRemediation.cautionCity'], '数据验证失败')
            self.assertEqual(str(data['cautionCounty']), addPara['societyInvestigationRemediation.cautionCounty'], '数据验证失败')
            self.assertEqual(str(data['cautionLand']), addPara['societyInvestigationRemediation.cautionLand'], '数据验证失败')
            self.assertEqual(str(data['cautionSum']), addPara['societyInvestigationRemediation.cautionSum'], '数据验证失败')
            self.assertEqual(str(data['investigationCity']), addPara['societyInvestigationRemediation.investigationCity'], '数据验证失败')
            self.assertEqual(str(data['investigationDistrict']), addPara['societyInvestigationRemediation.investigationDistrict'], '数据验证失败')
            self.assertEqual(str(data['investigationFindDistrict']), addPara['societyInvestigationRemediation.investigationFindDistrict'], '数据验证失败')
            self.assertEqual(str(data['investigationFindOther']), addPara['societyInvestigationRemediation.investigationFindOther'], '数据验证失败')
            self.assertEqual(str(data['investigationFindSum']), addPara['societyInvestigationRemediation.investigationFindSum'], '数据验证失败')
            self.assertEqual(str(data['investigationFindTown']), addPara['societyInvestigationRemediation.investigationFindTown'], '数据验证失败')
            self.assertEqual(str(data['investigationFindVillage']), addPara['societyInvestigationRemediation.investigationFindVillage'], '数据验证失败')
            self.assertEqual(str(data['investigationProvince']), addPara['societyInvestigationRemediation.investigationProvince'], '数据验证失败')
            self.assertEqual(str(data['investigationSum']), addPara['societyInvestigationRemediation.investigationSum'], '数据验证失败')
            self.assertEqual(str(data['nowRenovateCounty']), addPara['societyInvestigationRemediation.nowRenovateCounty'], '数据验证失败')
            self.assertEqual(str(data['nowRenovateOther']), addPara['societyInvestigationRemediation.nowRenovateOther'], '数据验证失败')
            self.assertEqual(str(data['nowRenovateStreet']), addPara['societyInvestigationRemediation.nowRenovateStreet'], '数据验证失败')
            self.assertEqual(str(data['nowRenovateSum']), addPara['societyInvestigationRemediation.nowRenovateSum'], '数据验证失败')
            self.assertEqual(str(data['nowRenovateVillage']), addPara['societyInvestigationRemediation.nowRenovateVillage'], '数据验证失败')
            self.assertEqual(str(data['policeStarting']), addPara['societyInvestigationRemediation.policeStarting'], '数据验证失败')
            self.assertEqual(str(data['policeSum']), addPara['societyInvestigationRemediation.policeSum'], '数据验证失败')
            self.assertEqual(str(data['strikeCrackedSum']), addPara['societyInvestigationRemediation.strikeCrackedSum'], '数据验证失败')
            self.assertEqual(str(data['strikeDadness']), addPara['societyInvestigationRemediation.strikeDadness'], '数据验证失败')
            self.assertEqual(str(data['strikeGangdom']), addPara['societyInvestigationRemediation.strikeGangdom'], '数据验证失败')
            self.assertEqual(str(data['strikePoison']), addPara['societyInvestigationRemediation.strikePoison'], '数据验证失败')
            self.assertEqual(str(data['strikeRob']), addPara['societyInvestigationRemediation.strikeRob'], '数据验证失败')
            self.assertEqual(str(data['strikeViolence']), addPara['societyInvestigationRemediation.strikeViolence'], '数据验证失败')
            Log.LogOutput(message='街道新增数据验证通过！')
            pass
        
        '''
    @功能：社会治安重点地区排查整治季报上报后街道层级新增默认读取的数据是否正确
    @ chenhui 2016-2-2
    '''       
    def testConflictRpt_018(self):
        '''社会治安重点地区排查整治季报回退'''
        #仿真环境下跳过测试
        if simulationEnvironment is True:
            pass
        else:
            #新增
            addPara=copy.deepcopy(socialSecurityReportAddPara1)
            addPara['dailyYear.id']=getDbQueryResult(dbCommand ="select id from dailyYears d where d.yeardate='2016' and d.makedorgid='%s' and d.name='2016年工作台账模版'"%orgInit['DftJieDaoOrgId'])
            addPara['dailyDirectory.id']=getDbQueryResult(dbCommand ="select id from newdailydirectorys d where d.dailyyearid='%s' and d.shortname='季报'"%addPara['dailyYear.id'])
            addPara['societyInvestigationRemediation.name']='2016年第一季度测试自动化社区社会治安重点地区排查整治工作情况表'#'2016%E5%B9%B4%E7%AC%AC%E4%B8%80%E5%AD%A3%E5%BA%A6%E6%B5%8B%E8%AF%95%E8%87%AA%E5%8A%A8%E5%8C%96%E7%A4%BE%E5%8C%BA%E7%A4%BE%E4%BC%9A%E6%B2%BB%E5%AE%89%E9%87%8D%E7%82%B9%E5%9C%B0%E5%8C%BA%E6%8E%92%E6%9F%A5%E6%95%B4%E6%B2%BB%E5%B7%A5%E4%BD%9C%E6%83%85%E5%86%B5%E8%A1%A8'
            result=addSocialSecuritRpt(para=addPara)
            self.assertTrue(result,'新增失败')
            #上报
            reportPara=copy.deepcopy(socialSecurityReportReportPara)
            reportPara['societyInvestigationRemediation.id']=result['id']
            reportPara['societyInvestigationRemediation.dailyDirectory.id']=addPara['dailyDirectory.id']
            reportSocialSecuritRpt(para=reportPara)
            #回退
            backPara=copy.deepcopy(socialSecurityReportReportPara)
            backPara['dailyDirectoryId']=addPara['dailyDirectory.id']
            backPara['dailyLogId']=result['id']
            rs=backSocialSecuritRpt(para=backPara)
            self.assertNotEqual(rs['backTime'], None, '回退验证失败')
            Log.LogOutput(message='回退验证成功！')
            pass
    
#模块： 工作台账
#功能： 新增、修改、删除、转移 会议/文件/活动/其他类的记录 
 
    def testHuiYiJiLuAdd_17(self):
        '''新增会议记录'''

        workingParam_17 = copy.deepcopy(RiChangBanGongPara.workingRecordObject) 
        workingParam_17['mode']='add'
        workingParam_17['fileType']='会议类'
        workingParam_17['newWorkingRecords.RECORDTYPE.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.displayname = '会议类' and p.propertydomainid = (select t.id from propertydomains t where t.domainname = '新工作台帐目录类型')")
        workingParam_17['newWorkingRecords.dailyDirectory.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from DailyDirectorys t where t.shortname='会议' and t.dailyyearid = (select id from dailyYears d where d.yeardate=%s and d.makedorgid=%s and d.dailytype='0')" %(time.strftime("%Y"), orgInit['DftJieDaoOrgId']))      # yeardate：当前年份，  makedorgid：街道层级，即上一层级id，  dailytype : 0-行政部门 ，1-职能部门
        workingParam_17['newWorkingRecords.departmentType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '平安办'")
        workingParam_17['newWorkingRecords.name'] = '会议%s'%CommonUtil.createRandomString() 
        workingParam_17['newWorkingRecords.dealDate'] = Time.getCurrentDate()
        workingParam_17['selectedTypes'] = CommonIntf.getIdByDomainAndDisplayName(domainName='台帐关键字', displayName='平安')   #可多选
        workingParam_17['newWorkingRecords.content'] = '主要内容'  
        responseDict = RiChangBanGongIntf.add_WorkingRecord(workingParam_17, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增会议记录失败')       
                      
        param_17 = copy.deepcopy(RiChangBanGongPara.checkRecordDict)
        param_17['name'] = workingParam_17['newWorkingRecords.name']    
        param_17['id'] = CommonIntf.getDbQueryResult(dbCommand = "select id from newWorkingRecords d where d.name='%s'" % (workingParam_17['newWorkingRecords.name']))
        ret = RiChangBanGongIntf.check_WorkingRecord(param_17, orgId=orgInit['DftSheQuOrgId'],dailyDirectoryId=workingParam_17['newWorkingRecords.dailyDirectory.id'],username=userInit['DftSheQuUser'], password='11111111')         
        self.assertTrue(ret, '查找会议记录失败') 
        
        pass 
    
    def testWenJianJiLuAdd_17(self):
        '''新增文件记录'''

        workingParam_17 = copy.deepcopy(RiChangBanGongPara.workingRecordObject) 
        workingParam_17['mode']='add'
        workingParam_17['fileType']='文件类'
        workingParam_17['newWorkingRecords.RECORDTYPE.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.displayname = '文件类' and p.propertydomainid = (select t.id from propertydomains t where t.domainname = '新工作台帐目录类型')")
        workingParam_17['newWorkingRecords.dailyDirectory.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from DailyDirectorys t where t.shortname='会议' and t.dailyyearid = (select id from dailyYears d where d.yeardate=%s and d.makedorgid=%s and d.dailytype='0')" %(time.strftime("%Y"), orgInit['DftJieDaoOrgId']))      # yeardate：当前年份，  makedorgid：街道层级，即上一层级id，  dailytype : 0-行政部门 ，1-职能部门 
        workingParam_17['newWorkingRecords.departmentType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '党委政府'")
        workingParam_17['newWorkingRecords.name'] = '文件%s'%CommonUtil.createRandomString() 
        workingParam_17['newWorkingRecords.dealDate'] = Time.getCurrentDate()
        workingParam_17['selectedTypes'] = CommonIntf.getIdByDomainAndDisplayName(domainName='台帐关键字', displayName='专项组')   #可多选
        workingParam_17['newWorkingRecords.content'] = '主要内容'  
        responseDict = RiChangBanGongIntf.add_WorkingRecord(workingParam_17, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增文件记录失败')       
                      
        param_17 = copy.deepcopy(RiChangBanGongPara.checkRecordDict)
        param_17['name'] = workingParam_17['newWorkingRecords.name']    
        param_17['id'] = CommonIntf.getDbQueryResult(dbCommand = "select id from newWorkingRecords d where d.name='%s'" % (workingParam_17['newWorkingRecords.name']))
        ret = RiChangBanGongIntf.check_WorkingRecord(param_17, orgId=orgInit['DftSheQuOrgId'],dailyDirectoryId=workingParam_17['newWorkingRecords.dailyDirectory.id'],username=userInit['DftSheQuUser'], password='11111111')         
        self.assertTrue(ret, '查找文件记录失败') 
        
        pass 

    def testHuoDongJiLuAdd_17(self):
        '''新增活动记录'''

        workingParam_17 = copy.deepcopy(RiChangBanGongPara.workingRecordObject) 
        workingParam_17['mode']='add'
        workingParam_17['fileType']='活动类'
        workingParam_17['newWorkingRecords.RECORDTYPE.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.displayname = '活动类' and p.propertydomainid = (select t.id from propertydomains t where t.domainname = '新工作台帐目录类型')")
        workingParam_17['newWorkingRecords.dailyDirectory.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from DailyDirectorys t where t.shortname='会议' and t.dailyyearid = (select id from dailyYears d where d.yeardate=%s and d.makedorgid=%s and d.dailytype='0')" %(time.strftime("%Y"), orgInit['DftJieDaoOrgId']))      # yeardate：当前年份，  makedorgid：街道层级，即上一层级id，  dailytype : 0-行政部门 ，1-职能部门 
        workingParam_17['newWorkingRecords.departmentType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '平安领导小组'")
        workingParam_17['newWorkingRecords.name'] = '活动%s'%CommonUtil.createRandomString() 
        workingParam_17['newWorkingRecords.dealDate'] = Time.getCurrentDate()
        workingParam_17['selectedTypes'] = CommonIntf.getIdByDomainAndDisplayName(domainName='台帐关键字', displayName='综治')   #可多选
        workingParam_17['newWorkingRecords.content'] = '主要内容'  
        responseDict = RiChangBanGongIntf.add_WorkingRecord(workingParam_17, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增文件记录失败')       
                      
        param_17 = copy.deepcopy(RiChangBanGongPara.checkRecordDict)
        param_17['name'] = workingParam_17['newWorkingRecords.name']    
        param_17['id'] = CommonIntf.getDbQueryResult(dbCommand = "select id from newWorkingRecords d where d.name='%s'" % (workingParam_17['newWorkingRecords.name']))
        ret = RiChangBanGongIntf.check_WorkingRecord(param_17, orgId=orgInit['DftSheQuOrgId'],dailyDirectoryId=workingParam_17['newWorkingRecords.dailyDirectory.id'],username=userInit['DftSheQuUser'], password='11111111')         
        self.assertTrue(ret, '查找文件记录失败') 
        
        pass 

    def testQiTaJiLuAdd_17(self):
        '''新增其他记录'''

        workingParam_17 = copy.deepcopy(RiChangBanGongPara.workingRecordObject) 
        workingParam_17['mode']='add'
        workingParam_17['fileType']='其他类'
        workingParam_17['newWorkingRecords.RECORDTYPE.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.displayname = '其他类' and p.propertydomainid = (select t.id from propertydomains t where t.domainname = '新工作台帐目录类型')")
        workingParam_17['newWorkingRecords.dailyDirectory.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from DailyDirectorys t where t.shortname='会议' and t.dailyyearid = (select id from dailyYears d where d.yeardate=%s and d.makedorgid=%s and d.dailytype='0')" %(time.strftime("%Y"), orgInit['DftJieDaoOrgId']))      # yeardate：当前年份，  makedorgid：街道层级，即上一层级id，  dailytype : 0-行政部门 ，1-职能部门 
        workingParam_17['newWorkingRecords.departmentType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '维护稳定领导小组'")
        workingParam_17['newWorkingRecords.name'] = '其他%s'%CommonUtil.createRandomString() 
        workingParam_17['newWorkingRecords.dealDate'] = Time.getCurrentDate()
        workingParam_17['selectedTypes'] = CommonIntf.getIdByDomainAndDisplayName(domainName='台帐关键字', displayName='例会')   #可多选
        workingParam_17['newWorkingRecords.content'] = '主要内容'  
        responseDict = RiChangBanGongIntf.add_WorkingRecord(workingParam_17, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增文件记录失败')       
                      
        param_17 = copy.deepcopy(RiChangBanGongPara.checkRecordDict)
        param_17['name'] = workingParam_17['newWorkingRecords.name']    
        param_17['id'] = CommonIntf.getDbQueryResult(dbCommand = "select id from newWorkingRecords d where d.name='%s'" % (workingParam_17['newWorkingRecords.name']))
        ret = RiChangBanGongIntf.check_WorkingRecord(param_17, orgId=orgInit['DftSheQuOrgId'],dailyDirectoryId=workingParam_17['newWorkingRecords.dailyDirectory.id'],username=userInit['DftSheQuUser'], password='11111111')         
        self.assertTrue(ret, '查找文件记录失败') 
        
        pass 
    
    def testHuiYiJiLuEdit_18(self):
        '''修改会议记录'''

        workingParam_18 = copy.deepcopy(RiChangBanGongPara.workingRecordObject) 
        workingParam_18['mode']='add'
        workingParam_18['fileType']='会议类'
        workingParam_18['newWorkingRecords.RECORDTYPE.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.displayname = '会议类' and p.propertydomainid = (select t.id from propertydomains t where t.domainname = '新工作台帐目录类型')")
        workingParam_18['newWorkingRecords.dailyDirectory.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from DailyDirectorys t where t.shortname='会议' and t.dailyyearid = (select id from dailyYears d where d.yeardate=%s and d.makedorgid=%s and d.dailytype='0')" %(time.strftime("%Y"), orgInit['DftJieDaoOrgId']))      # yeardate：当前年份，  makedorgid：街道层级，即上一层级id，  dailytype : 0-行政部门 ，1-职能部门 
        workingParam_18['newWorkingRecords.departmentType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '平安办'")
        workingParam_18['newWorkingRecords.name'] = '会议%s'%CommonUtil.createRandomString() 
        workingParam_18['newWorkingRecords.dealDate'] = Time.getCurrentDate()
        workingParam_18['selectedTypes'] = CommonIntf.getIdByDomainAndDisplayName(domainName='台帐关键字', displayName='平安')   #可多选
        workingParam_18['newWorkingRecords.content'] = '主要内容'  
        responseDict = RiChangBanGongIntf.add_WorkingRecord(workingParam_18, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增会议记录失败')      
        
        editWorkingParam_18 = copy.deepcopy(RiChangBanGongPara.workingRecordObject) 
        editWorkingParam_18['mode']='edit'
        editWorkingParam_18['from']='byListPage'
        editWorkingParam_18['fileType']='会议类'
        editWorkingParam_18['newWorkingRecords.id'] = CommonIntf.getDbQueryResult(dbCommand = "select id from newWorkingRecords d where d.name='%s'" % (workingParam_18['newWorkingRecords.name']))
        editWorkingParam_18['newWorkingRecords.RECORDTYPE.id'] = workingParam_18['newWorkingRecords.RECORDTYPE.id']
        editWorkingParam_18['newWorkingRecords.dailyDirectory.id'] = workingParam_18['newWorkingRecords.dailyDirectory.id']
        editWorkingParam_18['newWorkingRecords.departmentType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '维稳办'")
        editWorkingParam_18['newWorkingRecords.name'] = '修改会议%s'%CommonUtil.createRandomString() 
        editWorkingParam_18['newWorkingRecords.dealDate'] = Time.getCurrentDate()
        editWorkingParam_18['selectedTypes'] = workingParam_18['selectedTypes']  #可多选
        editWorkingParam_18['newWorkingRecords.content'] = workingParam_18['newWorkingRecords.content']  
        responseDict = RiChangBanGongIntf.edit_WorkingRecord(editWorkingParam_18, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改会议记录失败')  
                      
        param_18 = copy.deepcopy(RiChangBanGongPara.checkRecordDict)
        param_18['name'] = editWorkingParam_18['newWorkingRecords.name']    
        param_18['id'] = editWorkingParam_18['newWorkingRecords.id']
        ret = RiChangBanGongIntf.check_WorkingRecord(param_18, orgId=orgInit['DftSheQuOrgId'],dailyDirectoryId=workingParam_18['newWorkingRecords.dailyDirectory.id'],username=userInit['DftSheQuUser'], password='11111111')         
        self.assertTrue(ret, '查找会议记录失败') 
        
        pass 
    
    def testWenJianJiLuEdit_18(self):
        '''修改文件记录'''

        workingParam_18 = copy.deepcopy(RiChangBanGongPara.workingRecordObject) 
        workingParam_18['mode']='add'
        workingParam_18['fileType']='文件类'
        workingParam_18['newWorkingRecords.RECORDTYPE.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.displayname = '文件类' and p.propertydomainid = (select t.id from propertydomains t where t.domainname = '新工作台帐目录类型')")
        workingParam_18['newWorkingRecords.dailyDirectory.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from DailyDirectorys t where t.shortname='会议' and t.dailyyearid = (select id from dailyYears d where d.yeardate=%s and d.makedorgid=%s and d.dailytype='0')" %(time.strftime("%Y"), orgInit['DftJieDaoOrgId']))      # yeardate：当前年份，  makedorgid：街道层级，即上一层级id，  dailytype : 0-行政部门 ，1-职能部门 
        workingParam_18['newWorkingRecords.departmentType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '平安办'")
        workingParam_18['newWorkingRecords.name'] = '会议%s'%CommonUtil.createRandomString() 
        workingParam_18['newWorkingRecords.dealDate'] = Time.getCurrentDate()
        workingParam_18['selectedTypes'] = CommonIntf.getIdByDomainAndDisplayName(domainName='台帐关键字', displayName='平安')   #可多选
        workingParam_18['newWorkingRecords.content'] = '主要内容'  
        responseDict = RiChangBanGongIntf.add_WorkingRecord(workingParam_18, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增文件记录失败')      
        
        editWorkingParam_18 = copy.deepcopy(RiChangBanGongPara.workingRecordObject) 
        editWorkingParam_18['mode']='edit'
        editWorkingParam_18['from']='byListPage'
        editWorkingParam_18['fileType']='文件类'
        editWorkingParam_18['newWorkingRecords.id'] = CommonIntf.getDbQueryResult(dbCommand = "select id from newWorkingRecords d where d.name='%s'" % (workingParam_18['newWorkingRecords.name']))
        editWorkingParam_18['newWorkingRecords.RECORDTYPE.id'] = workingParam_18['newWorkingRecords.RECORDTYPE.id']
        editWorkingParam_18['newWorkingRecords.dailyDirectory.id'] = workingParam_18['newWorkingRecords.dailyDirectory.id']
        editWorkingParam_18['newWorkingRecords.departmentType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '综治委'")
        editWorkingParam_18['newWorkingRecords.name'] = '修改文件%s'%CommonUtil.createRandomString() 
        editWorkingParam_18['newWorkingRecords.dealDate'] = Time.getCurrentDate()
        editWorkingParam_18['selectedTypes'] = workingParam_18['selectedTypes']  #可多选
        editWorkingParam_18['newWorkingRecords.content'] = workingParam_18['newWorkingRecords.content']  
        responseDict = RiChangBanGongIntf.edit_WorkingRecord(editWorkingParam_18, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改文件记录失败')  
                      
        param_18 = copy.deepcopy(RiChangBanGongPara.checkRecordDict)
        param_18['name'] = editWorkingParam_18['newWorkingRecords.name']    
        param_18['id'] = editWorkingParam_18['newWorkingRecords.id']
        ret = RiChangBanGongIntf.check_WorkingRecord(param_18, orgId=orgInit['DftSheQuOrgId'],dailyDirectoryId=workingParam_18['newWorkingRecords.dailyDirectory.id'],username=userInit['DftSheQuUser'], password='11111111')         
        self.assertTrue(ret, '查找文件记录失败') 
        
        pass 

    def testHuoDongJiLuEdit_18(self):
        '''修改活动记录'''

        workingParam_18 = copy.deepcopy(RiChangBanGongPara.workingRecordObject) 
        workingParam_18['mode']='add'
        workingParam_18['fileType']='活动类'
        workingParam_18['newWorkingRecords.RECORDTYPE.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.displayname = '活动类' and p.propertydomainid = (select t.id from propertydomains t where t.domainname = '新工作台帐目录类型')")
        workingParam_18['newWorkingRecords.dailyDirectory.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from DailyDirectorys t where t.shortname='会议' and t.dailyyearid = (select id from dailyYears d where d.yeardate=%s and d.makedorgid=%s and d.dailytype='0')" %(time.strftime("%Y"), orgInit['DftJieDaoOrgId']))      # yeardate：当前年份，  makedorgid：街道层级，即上一层级id，  dailytype : 0-行政部门 ，1-职能部门 
        workingParam_18['newWorkingRecords.departmentType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '平安办'")
        workingParam_18['newWorkingRecords.name'] = '活动%s'%CommonUtil.createRandomString() 
        workingParam_18['newWorkingRecords.dealDate'] = Time.getCurrentDate()
        workingParam_18['selectedTypes'] = CommonIntf.getIdByDomainAndDisplayName(domainName='台帐关键字', displayName='平安')   #可多选
        workingParam_18['newWorkingRecords.content'] = '主要内容'  
        responseDict = RiChangBanGongIntf.add_WorkingRecord(workingParam_18, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增活动记录失败')      
        
        editWorkingParam_18 = copy.deepcopy(RiChangBanGongPara.workingRecordObject) 
        editWorkingParam_18['mode']='edit'
        editWorkingParam_18['from']='byListPage'
        editWorkingParam_18['fileType']='活动类'
        editWorkingParam_18['newWorkingRecords.id'] = CommonIntf.getDbQueryResult(dbCommand = "select id from newWorkingRecords d where d.name='%s'" % (workingParam_18['newWorkingRecords.name']))
        editWorkingParam_18['newWorkingRecords.RECORDTYPE.id'] = workingParam_18['newWorkingRecords.RECORDTYPE.id']
        editWorkingParam_18['newWorkingRecords.dailyDirectory.id'] = workingParam_18['newWorkingRecords.dailyDirectory.id']
        editWorkingParam_18['newWorkingRecords.departmentType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '综治办'")
        editWorkingParam_18['newWorkingRecords.name'] = '修改活动%s'%CommonUtil.createRandomString() 
        editWorkingParam_18['newWorkingRecords.dealDate'] = Time.getCurrentDate()
        editWorkingParam_18['selectedTypes'] = workingParam_18['selectedTypes']  #可多选
        editWorkingParam_18['newWorkingRecords.content'] = workingParam_18['newWorkingRecords.content']  
        responseDict = RiChangBanGongIntf.edit_WorkingRecord(editWorkingParam_18, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改活动记录失败')  
                      
        param_18 = copy.deepcopy(RiChangBanGongPara.checkRecordDict)
        param_18['name'] = editWorkingParam_18['newWorkingRecords.name']    
        param_18['id'] = editWorkingParam_18['newWorkingRecords.id']
        ret = RiChangBanGongIntf.check_WorkingRecord(param_18, orgId=orgInit['DftSheQuOrgId'],dailyDirectoryId=workingParam_18['newWorkingRecords.dailyDirectory.id'],username=userInit['DftSheQuUser'], password='11111111')         
        self.assertTrue(ret, '查找活动记录失败') 
        
        pass 

    def testQiTaJiLuEdit_18(self):
        '''修改其他记录'''

        workingParam_18 = copy.deepcopy(RiChangBanGongPara.workingRecordObject) 
        workingParam_18['mode']='add'
        workingParam_18['fileType']='其他类'
        workingParam_18['newWorkingRecords.RECORDTYPE.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.displayname = '其他类' and p.propertydomainid = (select t.id from propertydomains t where t.domainname = '新工作台帐目录类型')")
        workingParam_18['newWorkingRecords.dailyDirectory.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from DailyDirectorys t where t.shortname='会议' and t.dailyyearid = (select id from dailyYears d where d.yeardate=%s and d.makedorgid=%s and d.dailytype='0')" %(time.strftime("%Y"), orgInit['DftJieDaoOrgId']))      # yeardate：当前年份，  makedorgid：街道层级，即上一层级id，  dailytype : 0-行政部门 ，1-职能部门 
        workingParam_18['newWorkingRecords.departmentType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '平安办'")
        workingParam_18['newWorkingRecords.name'] = '其他%s'%CommonUtil.createRandomString() 
        workingParam_18['newWorkingRecords.dealDate'] = Time.getCurrentDate()
        workingParam_18['selectedTypes'] = CommonIntf.getIdByDomainAndDisplayName(domainName='台帐关键字', displayName='平安')   #可多选
        workingParam_18['newWorkingRecords.content'] = '主要内容'  
        responseDict = RiChangBanGongIntf.add_WorkingRecord(workingParam_18, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增文件记录失败')      
        
        editWorkingParam_18 = copy.deepcopy(RiChangBanGongPara.workingRecordObject) 
        editWorkingParam_18['mode']='edit'
        editWorkingParam_18['from']='byListPage'
        editWorkingParam_18['fileType']='其他类'
        editWorkingParam_18['newWorkingRecords.id'] = CommonIntf.getDbQueryResult(dbCommand = "select id from newWorkingRecords d where d.name='%s'" % (workingParam_18['newWorkingRecords.name']))
        editWorkingParam_18['newWorkingRecords.RECORDTYPE.id'] = workingParam_18['newWorkingRecords.RECORDTYPE.id']
        editWorkingParam_18['newWorkingRecords.dailyDirectory.id'] = workingParam_18['newWorkingRecords.dailyDirectory.id']
        editWorkingParam_18['newWorkingRecords.departmentType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '专项组'")
        editWorkingParam_18['newWorkingRecords.name'] = '修改其他%s'%CommonUtil.createRandomString() 
        editWorkingParam_18['newWorkingRecords.dealDate'] = Time.getCurrentDate()
        editWorkingParam_18['selectedTypes'] = workingParam_18['selectedTypes']  #可多选
        editWorkingParam_18['newWorkingRecords.content'] = workingParam_18['newWorkingRecords.content']  
        responseDict = RiChangBanGongIntf.edit_WorkingRecord(editWorkingParam_18, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改其他记录失败')  
                      
        param_18 = copy.deepcopy(RiChangBanGongPara.checkRecordDict)
        param_18['name'] = editWorkingParam_18['newWorkingRecords.name']    
        param_18['id'] = editWorkingParam_18['newWorkingRecords.id']
        ret = RiChangBanGongIntf.check_WorkingRecord(param_18, orgId=orgInit['DftSheQuOrgId'],dailyDirectoryId=workingParam_18['newWorkingRecords.dailyDirectory.id'],username=userInit['DftSheQuUser'], password='11111111')         
        self.assertTrue(ret, '查找其他记录失败') 
        
        pass 

    def testHuiYiJiLuDelete_19(self):
        '''删除多条会议记录'''

        workingParam_19 = copy.deepcopy(RiChangBanGongPara.workingRecordObject) 
        workingParam_19['mode']='add'
        workingParam_19['fileType']='会议类'
        workingParam_19['newWorkingRecords.RECORDTYPE.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.displayname = '会议类' and p.propertydomainid = (select t.id from propertydomains t where t.domainname = '新工作台帐目录类型')")
        workingParam_19['newWorkingRecords.dailyDirectory.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from DailyDirectorys t where t.shortname='会议' and t.dailyyearid = (select id from dailyYears d where d.yeardate=%s and d.makedorgid=%s and d.dailytype='0')" %(time.strftime("%Y"), orgInit['DftJieDaoOrgId']))      # yeardate：当前年份，  makedorgid：街道层级，即上一层级id，  dailytype : 0-行政部门 ，1-职能部门 
        workingParam_19['newWorkingRecords.departmentType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '平安办'")
        workingParam_19['newWorkingRecords.name'] = '会议%s'%CommonUtil.createRandomString() 
        workingParam_19['newWorkingRecords.dealDate'] = Time.getCurrentDate()
        workingParam_19['selectedTypes'] = CommonIntf.getIdByDomainAndDisplayName(domainName='台帐关键字', displayName='平安')   #可多选
        workingParam_19['newWorkingRecords.content'] = '主要内容'  
        responseDict = RiChangBanGongIntf.add_WorkingRecord(workingParam_19, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增会议记录失败')  
        
        newWorkingParam_19 = copy.deepcopy(RiChangBanGongPara.workingRecordObject) 
        newWorkingParam_19['mode']='add'
        newWorkingParam_19['fileType']='会议类'
        newWorkingParam_19['newWorkingRecords.RECORDTYPE.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.displayname = '会议类' and p.propertydomainid = (select t.id from propertydomains t where t.domainname = '新工作台帐目录类型')")
        newWorkingParam_19['newWorkingRecords.dailyDirectory.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from DailyDirectorys t where t.shortname='会议' and t.dailyyearid = (select id from dailyYears d where d.yeardate=%s and d.makedorgid=%s and d.dailytype='0')" %(time.strftime("%Y"), orgInit['DftJieDaoOrgId']))      # yeardate：当前年份，  makedorgid：街道层级，即上一层级id，  dailytype : 0-行政部门 ，1-职能部门
        newWorkingParam_19['newWorkingRecords.departmentType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '平安办'")
        newWorkingParam_19['newWorkingRecords.name'] = '新增会议%s'%CommonUtil.createRandomString() 
        newWorkingParam_19['newWorkingRecords.dealDate'] = Time.getCurrentDate()
        newWorkingParam_19['selectedTypes'] = CommonIntf.getIdByDomainAndDisplayName(domainName='台帐关键字', displayName='平安')   #可多选
        newWorkingParam_19['newWorkingRecords.content'] = '主要内容'  
        responseDict = RiChangBanGongIntf.add_WorkingRecord(newWorkingParam_19, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增会议记录失败')     
        
        deleteWorkingParam_19 = copy.deepcopy(RiChangBanGongPara.deleteRecordDict) 
        deleteWorkingParam_19['ids']=str(CommonIntf.getDbQueryResult(dbCommand = "select id from newWorkingRecords d where d.name='%s'" % (workingParam_19['newWorkingRecords.name'])))+','+str(CommonIntf.getDbQueryResult(dbCommand = "select id from newWorkingRecords d where d.name='%s'" % (newWorkingParam_19['newWorkingRecords.name'])))
        responseDict = RiChangBanGongIntf.delete_WorkingRecord(deleteWorkingParam_19, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '删除会议记录失败')          
                      
        param_19 = copy.deepcopy(RiChangBanGongPara.checkRecordDict)
        param_19['name'] = workingParam_19['newWorkingRecords.name']    
        param_19['id'] = deleteWorkingParam_19['ids']
        ret = RiChangBanGongIntf.check_WorkingRecord(param_19, orgId=orgInit['DftSheQuOrgId'],dailyDirectoryId=workingParam_19['newWorkingRecords.dailyDirectory.id'],username=userInit['DftSheQuUser'], password='11111111')         
        self.assertFalse(ret, '删除的会议记录在列表中依然存在，删除失败') 
        
        pass 

    def testWenJianJiLuDelete_19(self):
        '''删除多条文件记录'''

        workingParam_19 = copy.deepcopy(RiChangBanGongPara.workingRecordObject) 
        workingParam_19['mode']='add'
        workingParam_19['fileType']='文件类'
        workingParam_19['newWorkingRecords.RECORDTYPE.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.displayname = '文件类' and p.propertydomainid = (select t.id from propertydomains t where t.domainname = '新工作台帐目录类型')")
        workingParam_19['newWorkingRecords.dailyDirectory.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from DailyDirectorys t where t.shortname='会议' and t.dailyyearid = (select id from dailyYears d where d.yeardate=%s and d.makedorgid=%s and d.dailytype='0')" %(time.strftime("%Y"), orgInit['DftJieDaoOrgId']))      # yeardate：当前年份，  makedorgid：街道层级，即上一层级id，  dailytype : 0-行政部门 ，1-职能部门 
        workingParam_19['newWorkingRecords.departmentType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '平安办'")
        workingParam_19['newWorkingRecords.name'] = '文件%s'%CommonUtil.createRandomString() 
        workingParam_19['newWorkingRecords.dealDate'] = Time.getCurrentDate()
        workingParam_19['selectedTypes'] = CommonIntf.getIdByDomainAndDisplayName(domainName='台帐关键字', displayName='平安')   #可多选
        workingParam_19['newWorkingRecords.content'] = '主要内容'  
        responseDict = RiChangBanGongIntf.add_WorkingRecord(workingParam_19, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增文件记录失败')       
        
        newWorkingParam_19 = copy.deepcopy(RiChangBanGongPara.workingRecordObject) 
        newWorkingParam_19['mode']='add'
        newWorkingParam_19['fileType']='文件类'
        newWorkingParam_19['newWorkingRecords.RECORDTYPE.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.displayname = '文件类' and p.propertydomainid = (select t.id from propertydomains t where t.domainname = '新工作台帐目录类型')")
        newWorkingParam_19['newWorkingRecords.dailyDirectory.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from DailyDirectorys t where t.shortname='会议' and t.dailyyearid = (select id from dailyYears d where d.yeardate=%s and d.makedorgid=%s and d.dailytype='0')" %(time.strftime("%Y"), orgInit['DftJieDaoOrgId']))      # yeardate：当前年份，  makedorgid：街道层级，即上一层级id，  dailytype : 0-行政部门 ，1-职能部门
        newWorkingParam_19['newWorkingRecords.departmentType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '平安办'")
        newWorkingParam_19['newWorkingRecords.name'] = '新增文件%s'%CommonUtil.createRandomString() 
        newWorkingParam_19['newWorkingRecords.dealDate'] = Time.getCurrentDate()
        newWorkingParam_19['selectedTypes'] = CommonIntf.getIdByDomainAndDisplayName(domainName='台帐关键字', displayName='平安')   #可多选
        newWorkingParam_19['newWorkingRecords.content'] = '主要内容'  
        responseDict = RiChangBanGongIntf.add_WorkingRecord(newWorkingParam_19, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增文件记录失败')     
        
        deleteWorkingParam_19 = copy.deepcopy(RiChangBanGongPara.deleteRecordDict) 
        deleteWorkingParam_19['ids']=str(CommonIntf.getDbQueryResult(dbCommand = "select id from newWorkingRecords d where d.name='%s'" % (workingParam_19['newWorkingRecords.name'])))+','+str(CommonIntf.getDbQueryResult(dbCommand = "select id from newWorkingRecords d where d.name='%s'" % (newWorkingParam_19['newWorkingRecords.name'])))
        responseDict = RiChangBanGongIntf.delete_WorkingRecord(deleteWorkingParam_19, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '删除会议记录失败')        
                      
        param_19 = copy.deepcopy(RiChangBanGongPara.checkRecordDict)
        param_19['name'] = workingParam_19['newWorkingRecords.name']    
        param_19['id'] = deleteWorkingParam_19['ids']
        ret = RiChangBanGongIntf.check_WorkingRecord(param_19, orgId=orgInit['DftSheQuOrgId'],dailyDirectoryId=workingParam_19['newWorkingRecords.dailyDirectory.id'],username=userInit['DftSheQuUser'], password='11111111')         
        self.assertFalse(ret, '删除的文件记录在列表中依然存在，删除失败') 
        
        pass 
    
    def testHuoDongJiLuDelete_19(self):
        '''删除多条活动记录'''

        workingParam_19 = copy.deepcopy(RiChangBanGongPara.workingRecordObject) 
        workingParam_19['mode']='add'
        workingParam_19['fileType']='活动类'
        workingParam_19['newWorkingRecords.RECORDTYPE.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.displayname = '活动类' and p.propertydomainid = (select t.id from propertydomains t where t.domainname = '新工作台帐目录类型')")
        workingParam_19['newWorkingRecords.dailyDirectory.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from DailyDirectorys t where t.shortname='会议' and t.dailyyearid = (select id from dailyYears d where d.yeardate=%s and d.makedorgid=%s and d.dailytype='0')" %(time.strftime("%Y"), orgInit['DftJieDaoOrgId']))      # yeardate：当前年份，  makedorgid：街道层级，即上一层级id，  dailytype : 0-行政部门 ，1-职能部门 
        workingParam_19['newWorkingRecords.departmentType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '平安办'")
        workingParam_19['newWorkingRecords.name'] = '活动%s'%CommonUtil.createRandomString() 
        workingParam_19['newWorkingRecords.dealDate'] = Time.getCurrentDate()
        workingParam_19['selectedTypes'] = CommonIntf.getIdByDomainAndDisplayName(domainName='台帐关键字', displayName='平安')   #可多选
        workingParam_19['newWorkingRecords.content'] = '主要内容'  
        responseDict = RiChangBanGongIntf.add_WorkingRecord(workingParam_19, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增活动记录失败')       
        
        newWorkingParam_19 = copy.deepcopy(RiChangBanGongPara.workingRecordObject) 
        newWorkingParam_19['mode']='add'
        newWorkingParam_19['fileType']='活动类'
        newWorkingParam_19['newWorkingRecords.RECORDTYPE.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.displayname = '活动类' and p.propertydomainid = (select t.id from propertydomains t where t.domainname = '新工作台帐目录类型')")
        newWorkingParam_19['newWorkingRecords.dailyDirectory.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from DailyDirectorys t where t.shortname='会议' and t.dailyyearid = (select id from dailyYears d where d.yeardate=%s and d.makedorgid=%s and d.dailytype='0')" %(time.strftime("%Y"), orgInit['DftJieDaoOrgId']))      # yeardate：当前年份，  makedorgid：街道层级，即上一层级id，  dailytype : 0-行政部门 ，1-职能部门
        newWorkingParam_19['newWorkingRecords.departmentType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '平安办'")
        newWorkingParam_19['newWorkingRecords.name'] = '新增活动%s'%CommonUtil.createRandomString() 
        newWorkingParam_19['newWorkingRecords.dealDate'] = Time.getCurrentDate()
        newWorkingParam_19['selectedTypes'] = CommonIntf.getIdByDomainAndDisplayName(domainName='台帐关键字', displayName='平安')   #可多选
        newWorkingParam_19['newWorkingRecords.content'] = '主要内容'  
        responseDict = RiChangBanGongIntf.add_WorkingRecord(newWorkingParam_19, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增活动记录失败')     
        
        deleteWorkingParam_19 = copy.deepcopy(RiChangBanGongPara.deleteRecordDict) 
        deleteWorkingParam_19['ids']=str(CommonIntf.getDbQueryResult(dbCommand = "select id from newWorkingRecords d where d.name='%s'" % (workingParam_19['newWorkingRecords.name'])))+','+str(CommonIntf.getDbQueryResult(dbCommand = "select id from newWorkingRecords d where d.name='%s'" % (newWorkingParam_19['newWorkingRecords.name'])))
        responseDict = RiChangBanGongIntf.delete_WorkingRecord(deleteWorkingParam_19, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '删除活动记录失败')          
                      
        param_19 = copy.deepcopy(RiChangBanGongPara.checkRecordDict)
        param_19['name'] = workingParam_19['newWorkingRecords.name']    
        param_19['id'] = deleteWorkingParam_19['ids']
        ret = RiChangBanGongIntf.check_WorkingRecord(param_19, orgId=orgInit['DftSheQuOrgId'],dailyDirectoryId=workingParam_19['newWorkingRecords.dailyDirectory.id'],username=userInit['DftSheQuUser'], password='11111111')         
        self.assertFalse(ret, '删除的活动记录在列表中依然存在，删除失败') 
        
        pass 
    
    def testQiTaJiLuDelete_19(self):
        '''删除多条其他记录'''

        workingParam_19 = copy.deepcopy(RiChangBanGongPara.workingRecordObject) 
        workingParam_19['mode']='add'
        workingParam_19['fileType']='其他类'
        workingParam_19['newWorkingRecords.RECORDTYPE.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.displayname = '其他类' and p.propertydomainid = (select t.id from propertydomains t where t.domainname = '新工作台帐目录类型')")
        workingParam_19['newWorkingRecords.dailyDirectory.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from DailyDirectorys t where t.shortname='会议' and t.dailyyearid = (select id from dailyYears d where d.yeardate=%s and d.makedorgid=%s and d.dailytype='0')" %(time.strftime("%Y"), orgInit['DftJieDaoOrgId']))      # yeardate：当前年份，  makedorgid：街道层级，即上一层级id，  dailytype : 0-行政部门 ，1-职能部门 
        workingParam_19['newWorkingRecords.departmentType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '平安办'")
        workingParam_19['newWorkingRecords.name'] = '其他%s'%CommonUtil.createRandomString() 
        workingParam_19['newWorkingRecords.dealDate'] = Time.getCurrentDate()
        workingParam_19['selectedTypes'] = CommonIntf.getIdByDomainAndDisplayName(domainName='台帐关键字', displayName='平安')   #可多选
        workingParam_19['newWorkingRecords.content'] = '主要内容'  
        responseDict = RiChangBanGongIntf.add_WorkingRecord(workingParam_19, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增其他记录失败')       
        
        newWorkingParam_19 = copy.deepcopy(RiChangBanGongPara.workingRecordObject) 
        newWorkingParam_19['mode']='add'
        newWorkingParam_19['fileType']='其他类'
        newWorkingParam_19['newWorkingRecords.RECORDTYPE.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.displayname = '其他类' and p.propertydomainid = (select t.id from propertydomains t where t.domainname = '新工作台帐目录类型')")
        newWorkingParam_19['newWorkingRecords.dailyDirectory.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from DailyDirectorys t where t.shortname='会议' and t.dailyyearid = (select id from dailyYears d where d.yeardate=%s and d.makedorgid=%s and d.dailytype='0')" %(time.strftime("%Y"), orgInit['DftJieDaoOrgId']))      # yeardate：当前年份，  makedorgid：街道层级，即上一层级id，  dailytype : 0-行政部门 ，1-职能部门
        newWorkingParam_19['newWorkingRecords.departmentType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '平安办'")
        newWorkingParam_19['newWorkingRecords.name'] = '新增其他%s'%CommonUtil.createRandomString() 
        newWorkingParam_19['newWorkingRecords.dealDate'] = Time.getCurrentDate()
        newWorkingParam_19['selectedTypes'] = CommonIntf.getIdByDomainAndDisplayName(domainName='台帐关键字', displayName='平安')   #可多选
        newWorkingParam_19['newWorkingRecords.content'] = '主要内容'  
        responseDict = RiChangBanGongIntf.add_WorkingRecord(newWorkingParam_19, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增其他记录失败')     
        
        deleteWorkingParam_19 = copy.deepcopy(RiChangBanGongPara.deleteRecordDict) 
        deleteWorkingParam_19['ids']=str(CommonIntf.getDbQueryResult(dbCommand = "select id from newWorkingRecords d where d.name='%s'" % (workingParam_19['newWorkingRecords.name'])))+','+str(CommonIntf.getDbQueryResult(dbCommand = "select id from newWorkingRecords d where d.name='%s'" % (newWorkingParam_19['newWorkingRecords.name'])))
        responseDict = RiChangBanGongIntf.delete_WorkingRecord(deleteWorkingParam_19, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '删除其他记录失败')         
                      
        param_01 = copy.deepcopy(RiChangBanGongPara.checkRecordDict)
        param_01['name'] = workingParam_19['newWorkingRecords.name']    
        param_01['id'] = deleteWorkingParam_19['ids']
        ret = RiChangBanGongIntf.check_WorkingRecord(param_01, orgId=orgInit['DftSheQuOrgId'],dailyDirectoryId=workingParam_19['newWorkingRecords.dailyDirectory.id'],username=userInit['DftSheQuUser'], password='11111111')         
        self.assertFalse(ret, '删除的其他记录在列表中依然存在，删除失败') 
        
        pass 

    def testHuiYiJiLuTransfer_20(self):
        '''将会议记录转移到文件记录分类下'''

        workingParam_20 = copy.deepcopy(RiChangBanGongPara.workingRecordObject) 
        workingParam_20['mode']='add'
        workingParam_20['fileType']='会议类'
        workingParam_20['newWorkingRecords.RECORDTYPE.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.displayname = '会议类' and p.propertydomainid = (select t.id from propertydomains t where t.domainname = '新工作台帐目录类型')")
        workingParam_20['newWorkingRecords.dailyDirectory.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from DailyDirectorys t where t.shortname='会议' and t.dailyyearid = (select id from dailyYears d where d.yeardate=%s and d.makedorgid=%s and d.dailytype='0')" %(time.strftime("%Y"), orgInit['DftJieDaoOrgId']))      # yeardate：当前年份，  makedorgid：街道层级，即上一层级id，  dailytype : 0-行政部门 ，1-职能部门 
        workingParam_20['newWorkingRecords.departmentType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '平安办'")
        workingParam_20['newWorkingRecords.name'] = '会议转移%s'%CommonUtil.createRandomString() 
        workingParam_20['newWorkingRecords.dealDate'] = Time.getCurrentDate()
        workingParam_20['selectedTypes'] = CommonIntf.getIdByDomainAndDisplayName(domainName='台帐关键字', displayName='平安')   #可多选
        workingParam_20['newWorkingRecords.content'] = '主要内容'  
        responseDict = RiChangBanGongIntf.add_WorkingRecord(workingParam_20, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增会议记录失败')     
        
        transferWorkingParam_20 = copy.deepcopy(RiChangBanGongPara.deleteRecordDict) 
        transferWorkingParam_20['ids']=CommonIntf.getDbQueryResult(dbCommand = "select id from newWorkingRecords d where d.name='%s'" % (workingParam_20['newWorkingRecords.name']))
        transferWorkingParam_20['transferDirectoryId']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from DailyDirectorys t where t.shortname='文件' and t.dailyyearid = (select a.id from dailyyears a where a.makedorgid= '%s' and a.name='2016年工作台账模版')" % orgInit['DftJieDaoOrgId'])
        responseDict = RiChangBanGongIntf.transfer_WorkingRecord(transferWorkingParam_20, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '转移会议记录失败')          
                      
        param_20 = copy.deepcopy(RiChangBanGongPara.checkRecordDict)
        param_20['name'] = workingParam_20['newWorkingRecords.name']    
        param_20['id'] = transferWorkingParam_20['ids']
        ret = RiChangBanGongIntf.check_WorkingRecord(param_20, orgId=orgInit['DftSheQuOrgId'],dailyDirectoryId=transferWorkingParam_20['transferDirectoryId'],username=userInit['DftSheQuUser'], password='11111111')         
        self.assertTrue(ret, '转移的会议记录在文件分类列表中不存在，转移失败') 
        
        pass 

    def testWenJianJiLuTransfer_20(self):
        '''将文件记录转移到活动记录分类下'''

        workingParam_20 = copy.deepcopy(RiChangBanGongPara.workingRecordObject) 
        workingParam_20['mode']='add'
        workingParam_20['fileType']='文件类'
        workingParam_20['newWorkingRecords.RECORDTYPE.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.displayname = '文件类' and p.propertydomainid = (select t.id from propertydomains t where t.domainname = '新工作台帐目录类型')")
        workingParam_20['newWorkingRecords.dailyDirectory.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from DailyDirectorys t where t.shortname='会议' and t.dailyyearid = (select id from dailyYears d where d.yeardate=%s and d.makedorgid=%s and d.dailytype='0')" %(time.strftime("%Y"), orgInit['DftJieDaoOrgId']))      # yeardate：当前年份，  makedorgid：街道层级，即上一层级id，  dailytype : 0-行政部门 ，1-职能部门 
        workingParam_20['newWorkingRecords.departmentType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '平安办'")
        workingParam_20['newWorkingRecords.name'] = '文件转移%s'%CommonUtil.createRandomString() 
        workingParam_20['newWorkingRecords.dealDate'] = Time.getCurrentDate()
        workingParam_20['selectedTypes'] = CommonIntf.getIdByDomainAndDisplayName(domainName='台帐关键字', displayName='平安')   #可多选
        workingParam_20['newWorkingRecords.content'] = '主要内容'  
        responseDict = RiChangBanGongIntf.add_WorkingRecord(workingParam_20, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增文件记录失败')     
        
        transferWorkingParam_20 = copy.deepcopy(RiChangBanGongPara.deleteRecordDict) 
        transferWorkingParam_20['ids']=CommonIntf.getDbQueryResult(dbCommand = "select id from newWorkingRecords d where d.name='%s'" % (workingParam_20['newWorkingRecords.name']))
        transferWorkingParam_20['transferDirectoryId']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from DailyDirectorys t where t.shortname='活动' and t.dailyyearid = (select a.id from dailyyears a where a.makedorgid= '%s' and a.name='2016年工作台账模版')" % orgInit['DftJieDaoOrgId'])
        responseDict = RiChangBanGongIntf.transfer_WorkingRecord(transferWorkingParam_20, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '转移文件记录失败')          
                      
        param_20 = copy.deepcopy(RiChangBanGongPara.checkRecordDict)
        param_20['name'] = workingParam_20['newWorkingRecords.name']    
        param_20['id'] = transferWorkingParam_20['ids']
        ret = RiChangBanGongIntf.check_WorkingRecord(param_20, orgId=orgInit['DftSheQuOrgId'],dailyDirectoryId=transferWorkingParam_20['transferDirectoryId'],username=userInit['DftSheQuUser'], password='11111111')         
        self.assertTrue(ret, '转移的文件记录在活动分类列表中不存在，转移失败') 
        
        pass 

    def testHuoDongJiLuTransfer_20(self):
        '''将活动记录转移到其他记录分类下'''

        workingParam_20 = copy.deepcopy(RiChangBanGongPara.workingRecordObject) 
        workingParam_20['mode']='add'
        workingParam_20['fileType']='活动类'
        workingParam_20['newWorkingRecords.RECORDTYPE.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.displayname = '活动类' and p.propertydomainid = (select t.id from propertydomains t where t.domainname = '新工作台帐目录类型')")
        workingParam_20['newWorkingRecords.dailyDirectory.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from DailyDirectorys t where t.shortname='会议' and t.dailyyearid = (select id from dailyYears d where d.yeardate=%s and d.makedorgid=%s and d.dailytype='0')" %(time.strftime("%Y"), orgInit['DftJieDaoOrgId']))      # yeardate：当前年份，  makedorgid：街道层级，即上一层级id，  dailytype : 0-行政部门 ，1-职能部门 
        workingParam_20['newWorkingRecords.departmentType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '平安办'")
        workingParam_20['newWorkingRecords.name'] = '活动转移%s'%CommonUtil.createRandomString() 
        workingParam_20['newWorkingRecords.dealDate'] = Time.getCurrentDate()
        workingParam_20['selectedTypes'] = CommonIntf.getIdByDomainAndDisplayName(domainName='台帐关键字', displayName='平安')   #可多选
        workingParam_20['newWorkingRecords.content'] = '主要内容'  
        responseDict = RiChangBanGongIntf.add_WorkingRecord(workingParam_20, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增活动记录失败')     
        
        transferWorkingParam_20 = copy.deepcopy(RiChangBanGongPara.deleteRecordDict) 
        transferWorkingParam_20['ids']=CommonIntf.getDbQueryResult(dbCommand = "select id from newWorkingRecords d where d.name='%s'" % (workingParam_20['newWorkingRecords.name']))
        transferWorkingParam_20['transferDirectoryId']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from DailyDirectorys t where t.shortname='其他' and t.dailyyearid = (select a.id from dailyyears a where a.makedorgid= '%s' and a.name='2016年工作台账模版')" % orgInit['DftJieDaoOrgId'])
        responseDict = RiChangBanGongIntf.transfer_WorkingRecord(transferWorkingParam_20, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '转移活动记录失败')          
                      
        param_20 = copy.deepcopy(RiChangBanGongPara.checkRecordDict)
        param_20['name'] = workingParam_20['newWorkingRecords.name']    
        param_20['id'] = transferWorkingParam_20['ids']
        ret = RiChangBanGongIntf.check_WorkingRecord(param_20, orgId=orgInit['DftSheQuOrgId'],dailyDirectoryId=transferWorkingParam_20['transferDirectoryId'],username=userInit['DftSheQuUser'], password='11111111')         
        self.assertTrue(ret, '转移的活动记录在其他分类列表中不存在，转移失败') 
        
        pass 

    def testQiTaJiLuTransfer_20(self):
        '''将其他记录转移到会议记录分类下'''

        workingParam_20 = copy.deepcopy(RiChangBanGongPara.workingRecordObject) 
        workingParam_20['mode']='add'
        workingParam_20['fileType']='其他类'
        workingParam_20['newWorkingRecords.RECORDTYPE.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.displayname = '其他类' and p.propertydomainid = (select t.id from propertydomains t where t.domainname = '新工作台帐目录类型')")
        workingParam_20['newWorkingRecords.dailyDirectory.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from DailyDirectorys t where t.shortname='会议' and t.dailyyearid = (select id from dailyYears d where d.yeardate=%s and d.makedorgid=%s and d.dailytype='0')" %(time.strftime("%Y"), orgInit['DftJieDaoOrgId']))      # yeardate：当前年份，  makedorgid：街道层级，即上一层级id，  dailytype : 0-行政部门 ，1-职能部门 
        workingParam_20['newWorkingRecords.departmentType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '平安办'")
        workingParam_20['newWorkingRecords.name'] = '其他转移%s'%CommonUtil.createRandomString() 
        workingParam_20['newWorkingRecords.dealDate'] = Time.getCurrentDate()
        workingParam_20['selectedTypes'] = CommonIntf.getIdByDomainAndDisplayName(domainName='台帐关键字', displayName='平安')   #可多选
        workingParam_20['newWorkingRecords.content'] = '主要内容'  
        responseDict = RiChangBanGongIntf.add_WorkingRecord(workingParam_20, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增其他记录失败')     
        
        transferWorkingParam_20 = copy.deepcopy(RiChangBanGongPara.deleteRecordDict) 
        transferWorkingParam_20['ids'] = CommonIntf.getDbQueryResult(dbCommand = "select id from newWorkingRecords d where d.name='%s'" % (workingParam_20['newWorkingRecords.name']))
        transferWorkingParam_20['transferDirectoryId'] = workingParam_20['newWorkingRecords.dailyDirectory.id']
        responseDict = RiChangBanGongIntf.transfer_WorkingRecord(transferWorkingParam_20, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '转移其他记录失败')          
                      
        param_20 = copy.deepcopy(RiChangBanGongPara.checkRecordDict)
        param_20['name'] = workingParam_20['newWorkingRecords.name']    
        param_20['id'] = transferWorkingParam_20['ids']
        ret = RiChangBanGongIntf.check_WorkingRecord(param_20, orgId=orgInit['DftSheQuOrgId'],dailyDirectoryId=transferWorkingParam_20['transferDirectoryId'],username=userInit['DftSheQuUser'], password='11111111')         
        self.assertTrue(ret, '转移的其他记录在会议分类列表中不存在，转移失败') 
        
        pass 
    
    
    def testHuiYiJiLuCopy_22(self):
        '''复制辖区台账下的会议记录到我的台账中'''

        workingParam_22 = copy.deepcopy(RiChangBanGongPara.workingRecordObject) 
        workingParam_22['mode']='add'
        workingParam_22['fileType']='会议类'
        workingParam_22['newWorkingRecords.RECORDTYPE.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.displayname = '会议类' and p.propertydomainid = (select t.id from propertydomains t where t.domainname = '新工作台帐目录类型')")
        workingParam_22['newWorkingRecords.dailyDirectory.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from DailyDirectorys t where t.shortname='会议' and t.dailyyearid = (select id from dailyYears d where d.yeardate=%s and d.makedorgid=%s and d.dailytype='0')" %(time.strftime("%Y"), orgInit['DftJieDaoOrgId']))      # yeardate：当前年份，  makedorgid：街道层级，即上一层级id，  dailytype : 0-行政部门 ，1-职能部门 
        workingParam_22['newWorkingRecords.departmentType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '平安办'")
        workingParam_22['newWorkingRecords.name'] = '会议%s'%CommonUtil.createRandomString() 
        workingParam_22['newWorkingRecords.dealDate'] = '2015-12-22'
        workingParam_22['selectedTypes'] = CommonIntf.getIdByDomainAndDisplayName(domainName='台帐关键字', displayName='平安')   #可多选
        workingParam_22['newWorkingRecords.content'] = '主要内容'  
        responseDict = RiChangBanGongIntf.add_WorkingRecord(workingParam_22, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增会议记录失败')       
                
        copyParam_22 = copy.deepcopy(RiChangBanGongPara.copyRecordDict)
        copyParam_22['ids'] = CommonIntf.getDbQueryResult(dbCommand = "select id from newWorkingRecords d where d.name='%s'" % (workingParam_22['newWorkingRecords.name']))
        copyParam_22['toWorkingDirectoryId'] = workingParam_22['newWorkingRecords.dailyDirectory.id'] 
        responseDict = RiChangBanGongIntf.copy_WorkingRecord(copyParam_22, username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(responseDict.result, '会议记录复制失败') 
        
        
        
        param_22 = copy.deepcopy(RiChangBanGongPara.checkRecordDict) 
        param_22['name'] = workingParam_22['newWorkingRecords.name']    
        ret = RiChangBanGongIntf.check_WorkingRecord(param_22, orgId=orgInit['DftJieDaoOrgId'],dailyDirectoryId=copyParam_22['toWorkingDirectoryId'],username=userInit['DftJieDaoUser'], password='11111111')         
        self.assertTrue(ret, '查找会议记录失败')
        
        pass 

    def testWenJianJiLuCopy_22(self):
        '''复制辖区台账下的文件记录到我的台账中'''

        workingParam_22 = copy.deepcopy(RiChangBanGongPara.workingRecordObject) 
        workingParam_22['mode']='add'
        workingParam_22['fileType']='文件类'
        workingParam_22['newWorkingRecords.RECORDTYPE.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.displayname = '文件类' and p.propertydomainid = (select t.id from propertydomains t where t.domainname = '新工作台帐目录类型')")
        workingParam_22['newWorkingRecords.dailyDirectory.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from DailyDirectorys t where t.shortname='会议' and t.dailyyearid = (select id from dailyYears d where d.yeardate=%s and d.makedorgid=%s and d.dailytype='0')" %(time.strftime("%Y"), orgInit['DftJieDaoOrgId']))      # yeardate：当前年份，  makedorgid：街道层级，即上一层级id，  dailytype : 0-行政部门 ，1-职能部门  
        workingParam_22['newWorkingRecords.departmentType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '平安办'")
        workingParam_22['newWorkingRecords.name'] = '文件%s'%CommonUtil.createRandomString() 
        workingParam_22['newWorkingRecords.dealDate'] = Time.getCurrentDate()
        workingParam_22['selectedTypes'] = CommonIntf.getIdByDomainAndDisplayName(domainName='台帐关键字', displayName='平安')   #可多选
        workingParam_22['newWorkingRecords.content'] = '主要内容'  
        responseDict = RiChangBanGongIntf.add_WorkingRecord(workingParam_22, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增文件记录失败')       
                     
        copyParam_22 = copy.deepcopy(RiChangBanGongPara.copyRecordDict)
        copyParam_22['ids'] = CommonIntf.getDbQueryResult(dbCommand = "select id from newWorkingRecords d where d.name='%s'" % (workingParam_22['newWorkingRecords.name']))
        copyParam_22['toWorkingDirectoryId'] = workingParam_22['newWorkingRecords.dailyDirectory.id']  
        responseDict = RiChangBanGongIntf.copy_WorkingRecord(copyParam_22, username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(responseDict.result, '文件记录复制失败') 
         
        param_22 = copy.deepcopy(RiChangBanGongPara.checkRecordDict) 
        param_22['name'] = workingParam_22['newWorkingRecords.name']    
        ret = RiChangBanGongIntf.check_WorkingRecord(param_22, orgId=orgInit['DftJieDaoOrgId'],dailyDirectoryId=copyParam_22['toWorkingDirectoryId'],username=userInit['DftJieDaoUser'], password='11111111')         
        self.assertTrue(ret, '查找文件记录失败')
        
        pass
    
    def testHuoDongJiLuCopy_22(self):
        '''复制辖区台账下的活动记录到我的台账中'''

        workingParam_22 = copy.deepcopy(RiChangBanGongPara.workingRecordObject) 
        workingParam_22['mode']='add'
        workingParam_22['fileType']='活动类'
        workingParam_22['newWorkingRecords.RECORDTYPE.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.displayname = '活动类' and p.propertydomainid = (select t.id from propertydomains t where t.domainname = '新工作台帐目录类型')")
        workingParam_22['newWorkingRecords.dailyDirectory.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from DailyDirectorys t where t.shortname='会议' and t.dailyyearid = (select id from dailyYears d where d.yeardate=%s and d.makedorgid=%s and d.dailytype='0')" %(time.strftime("%Y"), orgInit['DftJieDaoOrgId']))      # yeardate：当前年份，  makedorgid：街道层级，即上一层级id，  dailytype : 0-行政部门 ，1-职能部门  
        workingParam_22['newWorkingRecords.departmentType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '平安办'")
        workingParam_22['newWorkingRecords.name'] = '活动%s'%CommonUtil.createRandomString() 
        workingParam_22['newWorkingRecords.dealDate'] = Time.getCurrentDate()
        workingParam_22['selectedTypes'] = CommonIntf.getIdByDomainAndDisplayName(domainName='台帐关键字', displayName='平安')   #可多选
        workingParam_22['newWorkingRecords.content'] = '主要内容'  
        responseDict = RiChangBanGongIntf.add_WorkingRecord(workingParam_22, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增活动记录失败')       
                     
        copyParam_22 = copy.deepcopy(RiChangBanGongPara.copyRecordDict)
        copyParam_22['ids'] = CommonIntf.getDbQueryResult(dbCommand = "select id from newWorkingRecords d where d.name='%s'" % (workingParam_22['newWorkingRecords.name']))
        copyParam_22['toWorkingDirectoryId'] = workingParam_22['newWorkingRecords.dailyDirectory.id']  
        responseDict = RiChangBanGongIntf.copy_WorkingRecord(copyParam_22, username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(responseDict.result, '活动记录复制失败') 
         
        param_22 = copy.deepcopy(RiChangBanGongPara.checkRecordDict) 
        param_22['name'] = workingParam_22['newWorkingRecords.name']    
        ret = RiChangBanGongIntf.check_WorkingRecord(param_22, orgId=orgInit['DftJieDaoOrgId'],dailyDirectoryId=copyParam_22['toWorkingDirectoryId'],username=userInit['DftJieDaoUser'], password='11111111')         
        self.assertTrue(ret, '查找活动记录失败')
        
        pass

    def testQiTaJiLuCopy_22(self):
        '''复制辖区台账下的其他记录到我的台账中'''

        workingParam_22 = copy.deepcopy(RiChangBanGongPara.workingRecordObject) 
        workingParam_22['mode']='add'
        workingParam_22['fileType']='其他类'
        workingParam_22['newWorkingRecords.RECORDTYPE.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.displayname = '其他类' and p.propertydomainid = (select t.id from propertydomains t where t.domainname = '新工作台帐目录类型')")
        workingParam_22['newWorkingRecords.dailyDirectory.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from DailyDirectorys t where t.shortname='会议' and t.dailyyearid = (select id from dailyYears d where d.yeardate=%s and d.makedorgid=%s and d.dailytype='0')" %(time.strftime("%Y"), orgInit['DftJieDaoOrgId']))      # yeardate：当前年份，  makedorgid：街道层级，即上一层级id，  dailytype : 0-行政部门 ，1-职能部门  
        workingParam_22['newWorkingRecords.departmentType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '平安办'")
        workingParam_22['newWorkingRecords.name'] = '其他%s'%CommonUtil.createRandomString() 
        workingParam_22['newWorkingRecords.dealDate'] = Time.getCurrentDate()
        workingParam_22['selectedTypes'] = CommonIntf.getIdByDomainAndDisplayName(domainName='台帐关键字', displayName='平安')   #可多选
        workingParam_22['newWorkingRecords.content'] = '主要内容'  
        responseDict = RiChangBanGongIntf.add_WorkingRecord(workingParam_22, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增其他记录失败')       
                     
        copyParam_22 = copy.deepcopy(RiChangBanGongPara.copyRecordDict)
        copyParam_22['ids'] = CommonIntf.getDbQueryResult(dbCommand = "select id from newWorkingRecords d where d.name='%s'" % (workingParam_22['newWorkingRecords.name']))
        copyParam_22['toWorkingDirectoryId'] = workingParam_22['newWorkingRecords.dailyDirectory.id']  
        responseDict = RiChangBanGongIntf.copy_WorkingRecord(copyParam_22, username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(responseDict.result, '其他记录复制失败') 
         
        param_22 = copy.deepcopy(RiChangBanGongPara.checkRecordDict) 
        param_22['name'] = workingParam_22['newWorkingRecords.name']    
        ret = RiChangBanGongIntf.check_WorkingRecord(param_22, orgId=orgInit['DftJieDaoOrgId'],dailyDirectoryId=copyParam_22['toWorkingDirectoryId'],username=userInit['DftJieDaoUser'], password='11111111')         
        self.assertTrue(ret, '查找其他记录失败')
        
        pass



#模块： 我的资料


    def testFaLvFaGuiAdd_25(self):
        '''新增法律法规资料'''

        myProfileParam_25 = copy.deepcopy(RiChangBanGongPara.myProfileObject) 
        myProfileParam_25['myProfile.resourcePoolType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.displayseq from propertydicts  p where p.displayname = '法律法规'")  #不同的目录下typeid不同
        myProfileParam_25['mode']='add'
        myProfileParam_25['myProfile.name'] = '法律法规%s'%CommonUtil.createRandomString() 
        myProfileParam_25['myProfile.releaseUnit'] = '发文单位'
        myProfileParam_25['myProfile.releaseTime'] = Time.getCurrentDate()
        responseDict = RiChangBanGongIntf.add_MyProfile(myProfileParam_25, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增法律法规失败')       
                      
        param_25 = copy.deepcopy(RiChangBanGongPara.checkProfileDict)
        param_25['name'] = myProfileParam_25['myProfile.name']    
        param_25['id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from myProfiles t where t.name='%s'" % (myProfileParam_25['myProfile.name']))
        ret = RiChangBanGongIntf.check_MyProfile(param_25, typeId=myProfileParam_25['myProfile.resourcePoolType.id'],username=userInit['DftSheQuUser'], password='11111111')         
        self.assertTrue(ret, '查找会议记录失败') 
        
        pass 
    
    def testFaLvFaGuiEdit_26(self):
        '''修改法律法规资料'''

        myProfileParam_26 = copy.deepcopy(RiChangBanGongPara.myProfileObject) 
        myProfileParam_26['myProfile.resourcePoolType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.displayseq from propertydicts  p where p.displayname = '法律法规'")  #不同的目录下typeid不同
        myProfileParam_26['mode']='add'
        myProfileParam_26['myProfile.name'] = '法律法规%s'%CommonUtil.createRandomString() 
        myProfileParam_26['myProfile.releaseUnit'] = '发文单位'
        myProfileParam_26['myProfile.releaseTime'] = Time.getCurrentDate()
        responseDict = RiChangBanGongIntf.add_MyProfile(myProfileParam_26, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增法律法规失败')       
                      
        editMyProfileParam_26 = copy.deepcopy(RiChangBanGongPara.myProfileObject) 
        editMyProfileParam_26['myProfile.resourcePoolType.id'] = myProfileParam_26['myProfile.resourcePoolType.id']
        editMyProfileParam_26['mode'] ='edit'
        editMyProfileParam_26['myProfile.id'] = RiChangBanGongIntf.get_myprofile_id_by_name(myProfileParam_26['myProfile.name'])#CommonIntf.getDbQueryResult(dbCommand = "select t.id from myProfiles t where t.name='%s'" % (myProfileParam_26['myProfile.name']))
        editMyProfileParam_26['myProfile.name'] = '修改法律法规%s'%CommonUtil.createRandomString() 
        editMyProfileParam_26['myProfile.releaseUnit'] = myProfileParam_26['myProfile.releaseUnit']
        editMyProfileParam_26['myProfile.releaseTime'] = myProfileParam_26['myProfile.releaseTime']
        responseDict = RiChangBanGongIntf.edit_MyProfile(editMyProfileParam_26, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '修改法律法规失败')                      
                      
        param_25 = copy.deepcopy(RiChangBanGongPara.checkProfileDict)
        param_25['name'] = editMyProfileParam_26['myProfile.name']    
        param_25['id'] = editMyProfileParam_26['myProfile.id']
        ret = RiChangBanGongIntf.check_MyProfile(param_25, typeId=editMyProfileParam_26['myProfile.resourcePoolType.id'],username=userInit['DftSheQuUser'], password='11111111')         
        self.assertTrue(ret, '查找会议记录失败') 
        
        pass 

    def testFaLvFaGuiSearch_27(self):
        '''搜索法律法规资料'''

        myProfileParam_27 = copy.deepcopy(RiChangBanGongPara.myProfileObject) 
        myProfileParam_27['myProfile.resourcePoolType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.displayseq from propertydicts  p where p.displayname = '法律法规'")  #不同的目录下typeid不同
        myProfileParam_27['mode']='add'
        myProfileParam_27['myProfile.name'] = '法律法规%s'%CommonUtil.createRandomString() 
        myProfileParam_27['myProfile.releaseUnit'] = '发文单位'
        myProfileParam_27['myProfile.releaseTime'] = Time.getCurrentDate()
        responseDict = RiChangBanGongIntf.add_MyProfile(myProfileParam_27, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增法律法规失败')  
        
        newMyProfileParam_27 = copy.deepcopy(RiChangBanGongPara.myProfileObject) 
        newMyProfileParam_27['myProfile.resourcePoolType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.displayseq from propertydicts  p where p.displayname = '法律法规'")  
        newMyProfileParam_27['mode']='add'
        newMyProfileParam_27['myProfile.name'] = '新增法律法规%s'%CommonUtil.createRandomString() 
        newMyProfileParam_27['myProfile.releaseUnit'] = '发文单位'
        newMyProfileParam_27['myProfile.releaseTime'] = Time.getCurrentDate()
        responseDict = RiChangBanGongIntf.add_MyProfile(newMyProfileParam_27, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增法律法规失败')               
                      
        searchMyProfileParam_27 = copy.deepcopy(RiChangBanGongPara.checkProfileDict) 
        searchMyProfileParam_27['name'] = myProfileParam_27['myProfile.name']
        searchMyProfileParam_27['id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from myProfiles t where t.name='%s'" % (myProfileParam_27['myProfile.name']))
        ret = RiChangBanGongIntf.search_MyProfile(searchMyProfileParam_27, typeId=myProfileParam_27['myProfile.resourcePoolType.id'],name=myProfileParam_27['myProfile.name'],username=userInit['DftSheQuUser'], password='11111111')
        self.assertFalse(ret, '搜索法律法规信息失败')                      
                              
        pass 

    def testFaLvFaGuiDelete_28(self):
        '''删除法律法规资料'''

        myProfileParam_28 = copy.deepcopy(RiChangBanGongPara.myProfileObject) 
        myProfileParam_28['myProfile.resourcePoolType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.displayseq from propertydicts  p where p.displayname = '法律法规'")  #不同的目录下typeid不同
        myProfileParam_28['mode']='add'
        myProfileParam_28['myProfile.name'] = '法律法规%s'%CommonUtil.createRandomString() 
        myProfileParam_28['myProfile.releaseUnit'] = '发文单位'
        myProfileParam_28['myProfile.releaseTime'] = Time.getCurrentDate()
        responseDict = RiChangBanGongIntf.add_MyProfile(myProfileParam_28, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增法律法规失败')   
        
        newMyProfileParam_28 = copy.deepcopy(RiChangBanGongPara.myProfileObject) 
        newMyProfileParam_28['myProfile.resourcePoolType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.displayseq from propertydicts  p where p.displayname = '法律法规'")  
        newMyProfileParam_28['mode']='add'
        newMyProfileParam_28['myProfile.name'] = '新增法律法规%s'%CommonUtil.createRandomString() 
        newMyProfileParam_28['myProfile.releaseUnit'] = '发文单位'
        newMyProfileParam_28['myProfile.releaseTime'] = Time.getCurrentDate()
        responseDict = RiChangBanGongIntf.add_MyProfile(newMyProfileParam_28, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增法律法规失败')     
                      
        deleteMyProfileParam_28 = copy.deepcopy(RiChangBanGongPara.deleteProfileDict) 
        deleteMyProfileParam_28['ids'] = str(RiChangBanGongIntf.get_myprofile_id_by_name(myProfileParam_28['myProfile.name']))+','+str(RiChangBanGongIntf.get_myprofile_id_by_name(newMyProfileParam_28['myProfile.name']))#str(CommonIntf.getDbQueryResult(dbCommand = "select t.id from myProfiles t where t.name='%s'" % (myProfileParam_28['myProfile.name'])))+','+str(CommonIntf.getDbQueryResult(dbCommand = "select t.id from myProfiles t where t.name='%s'" % (newMyProfileParam_28['myProfile.name'])))
        responseDict = RiChangBanGongIntf.delete_MyProfile(deleteMyProfileParam_28, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '删除法律法规失败')                      
                      
        param_25 = copy.deepcopy(RiChangBanGongPara.checkProfileDict)
        param_25['name'] = myProfileParam_28['myProfile.name']    
        param_25['id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from myProfiles t where t.name='%s'" % (myProfileParam_28['myProfile.name']))
        ret = RiChangBanGongIntf.check_MyProfile(param_25, typeId=myProfileParam_28['myProfile.resourcePoolType.id'],username=userInit['DftSheQuUser'], password='11111111')         
        self.assertFalse(ret, '删除的法律法规资料在列表中依然存在，删除失败') 
        
        param_25['name'] = newMyProfileParam_28['myProfile.name']    
        param_25['id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from myProfiles t where t.name='%s'" % (newMyProfileParam_28['myProfile.name']))
        ret = RiChangBanGongIntf.check_MyProfile(param_25, typeId=newMyProfileParam_28['myProfile.resourcePoolType.id'],username=userInit['DftSheQuUser'], password='11111111')         
        self.assertFalse(ret, '删除的法律法规资料在列表中依然存在，删除失败')         
        
        pass 

    def testFaLvFaGuiShare_29(self):
        '''共享法律法规资料'''

        myProfileParam_29 = copy.deepcopy(RiChangBanGongPara.myProfileObject) 
        myProfileParam_29['myProfile.resourcePoolType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.displayseq from propertydicts  p where p.displayname = '法律法规'")  #不同的目录下typeid不同
        myProfileParam_29['mode']='add'
        myProfileParam_29['myProfile.name'] = '共享法律法规%s'%CommonUtil.createRandomString() 
        myProfileParam_29['myProfile.releaseUnit'] = '发文单位'
        myProfileParam_29['myProfile.releaseTime'] = Time.getCurrentDate()
        responseDict = RiChangBanGongIntf.add_MyProfile(myProfileParam_29, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增法律法规失败')
        
        cacheParam_29 = copy.deepcopy(RiChangBanGongPara.cacheObject) 
#         cacheParam_29['viewObjectVo.selectedCheckBoxStrs'] = ''   #8070（当前）/<8080时数据不同>  全选时不填  按层级选择时需填写（可多选）  省：50-0 市：40-0 县：30-0 乡镇：20-0 联村：15-0 村：10-0 网格：0-0 省级职能部门：50-1 市级职能部门：40-1 县级职能部门：30-1 乡镇职能工作站：20-1
#         cacheParam_29['viewObjectVo.selectedIdStrs']=''
#         cacheParam_29['viewObjectVo.exclusiveIdStrs'] = ''
        cacheParam_29['viewObjectVo.provinceNum'] = '2'
        cacheParam_29['viewObjectVo.cityNum'] = '3'
        cacheParam_29['viewObjectVo.districtNum'] = '5'
        cacheParam_29['viewObjectVo.townNum'] = '27'
        cacheParam_29['viewObjectVo.unitedVillageNum'] = '2'
        cacheParam_29['viewObjectVo.villageNum'] = '352'
        cacheParam_29['viewObjectVo.gridNum'] = '538'
        cacheParam_29['viewObjectVo.provinceFucDepartmentNum'] = '1'
        cacheParam_29['viewObjectVo.cityFucDepartmentNum'] = '1'
        cacheParam_29['viewObjectVo.districtFucDepartmentNum'] = '3'
        cacheParam_29['viewObjectVo.townFucDepartmentNum'] = '2'
        cacheParam_29['viewObjectVo.defProvinceNum'] = '2'
        cacheParam_29['viewObjectVo.defCityNum'] = '3'
        cacheParam_29['viewObjectVo.defDistrictNum'] = '5'
        cacheParam_29['viewObjectVo.defTownNum'] = '27'
        cacheParam_29['viewObjectVo.defUnitedVillageNum'] = '2'
        cacheParam_29['viewObjectVo.defVillageNum'] = '352'
        cacheParam_29['viewObjectVo.defGridNum'] = '538'
        cacheParam_29['viewObjectVo.defProvinceFucDepartmentNum'] = '1'
        cacheParam_29['viewObjectVo.defCityFucDepartmentNum'] = '1'
        cacheParam_29['viewObjectVo.defDistrictFucDepartmentNum'] = '3'
        cacheParam_29['viewObjectVo.defTownFucDepartmentNum'] = '2'
        cacheParam_29['viewObjectVo.selectedRadio'] = 'selectAll'  #全选 selectAll   选择部分层级selectByLevel

        shareMyProfileParam_29 = copy.deepcopy(RiChangBanGongPara.shareProfileDict) 
        shareMyProfileParam_29['ids'] = RiChangBanGongIntf.get_myprofile_id_by_name(myProfileParam_29['myProfile.name'])#CommonIntf.getDbQueryResult(dbCommand = "select t.id from myProfiles t where t.name='%s'" % (myProfileParam_29['myProfile.name']))
        shareMyProfileParam_29['resourcePoolTypeId']=CommonIntf.getDbQueryResult(dbCommand = "select p.displayseq from propertydicts  p where p.displayname = '法律法规'")  #不同的目录下typeid不同
        shareMyProfileParam_29['sendMessage'] = '0'
        shareMyProfileParam_29['identification'] = 'myProfile'
        shareMyProfileParam_29['setPermissionCacheId'] = RiChangBanGongIntf.viewObject(cacheParam_29)
        shareMyProfileParam_29['setPermissionText'] = '省级2个,市级3个,县区级5个,乡镇27个,乡村352个,网格538个,省级职能部门1个,市级职能部门1个,县区级职能部门3个,乡镇职能工作站2个' #与上面权限设置下选择的部门数量一致
        shareMyProfileParam_29['Message'] = '0'
        responseDict = RiChangBanGongIntf.share_MyProfile(shareMyProfileParam_29, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '资料分享失败')  
        
        param_29 = copy.deepcopy(RiChangBanGongPara.checkProfileDict)
        param_29['name'] = myProfileParam_29['myProfile.name']    
        param_29['id'] = shareMyProfileParam_29['ids']
        ret = RiChangBanGongIntf.check_sharingMyProfile(param_29, typeId=CommonIntf.getDbQueryResult(dbCommand = "select p.id from directorySettings p where p.name = '法律法规'") ,username=userInit['DftSheQuUser'], password='11111111')      #不同的目录下typeid：根据所属目录不同 ，法律法规、规章制度...  
        self.assertTrue(ret, '分享法律法规资料失败') 

    def testFaLvFaGuiShareCancel_30(self):
        '''将已共享的法律法规资料取消共享'''

        myProfileParam_30 = copy.deepcopy(RiChangBanGongPara.myProfileObject) 
        myProfileParam_30['myProfile.resourcePoolType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.displayseq from propertydicts  p where p.displayname = '法律法规'")  #不同的目录下typeid不同
        myProfileParam_30['mode']='add'
        myProfileParam_30['myProfile.name'] = '取消共享法律法规%s'%CommonUtil.createRandomString() 
        myProfileParam_30['myProfile.releaseUnit'] = '发文单位'
        myProfileParam_30['myProfile.releaseTime'] = Time.getCurrentDate()
        responseDict = RiChangBanGongIntf.add_MyProfile(myProfileParam_30, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '新增法律法规失败')
        
        cacheParam_30 = copy.deepcopy(RiChangBanGongPara.cacheObject) 
#         cacheParam_30['viewObjectVo.selectedCheckBoxStrs'] = ''   #8070（当前）/<8080时数据不同>  全选时不填  按层级选择时需填写（可多选）  省：50-0 市：40-0 县：30-0 乡镇：20-0 联村：15-0 村：10-0 网格：0-0 省级职能部门：50-1 市级职能部门：40-1 县级职能部门：30-1 乡镇职能工作站：20-1
#         cacheParam_30['viewObjectVo.selectedIdStrs']=''
#         cacheParam_30['viewObjectVo.exclusiveIdStrs'] = ''
        cacheParam_30['viewObjectVo.provinceNum'] = '2'
        cacheParam_30['viewObjectVo.cityNum'] = '3'
        cacheParam_30['viewObjectVo.districtNum'] = '5'
        cacheParam_30['viewObjectVo.townNum'] = '27'
        cacheParam_30['viewObjectVo.unitedVillageNum'] = '2'
        cacheParam_30['viewObjectVo.villageNum'] = '352'
        cacheParam_30['viewObjectVo.gridNum'] = '538'
        cacheParam_30['viewObjectVo.provinceFucDepartmentNum'] = '1'
        cacheParam_30['viewObjectVo.cityFucDepartmentNum'] = '1'
        cacheParam_30['viewObjectVo.districtFucDepartmentNum'] = '3'
        cacheParam_30['viewObjectVo.townFucDepartmentNum'] = '2'
        cacheParam_30['viewObjectVo.defProvinceNum'] = '2'
        cacheParam_30['viewObjectVo.defCityNum'] = '3'
        cacheParam_30['viewObjectVo.defDistrictNum'] = '5'
        cacheParam_30['viewObjectVo.defTownNum'] = '27'
        cacheParam_30['viewObjectVo.defUnitedVillageNum'] = '2'
        cacheParam_30['viewObjectVo.defVillageNum'] = '352'
        cacheParam_30['viewObjectVo.defGridNum'] = '538'
        cacheParam_30['viewObjectVo.defProvinceFucDepartmentNum'] = '1'
        cacheParam_30['viewObjectVo.defCityFucDepartmentNum'] = '1'
        cacheParam_30['viewObjectVo.defDistrictFucDepartmentNum'] = '3'
        cacheParam_30['viewObjectVo.defTownFucDepartmentNum'] = '2'
        cacheParam_30['viewObjectVo.selectedRadio'] = 'selectAll'  #全选 selectAll   选择部分层级selectByLevel

        shareMyProfileParam_30 = copy.deepcopy(RiChangBanGongPara.shareProfileDict) 
        shareMyProfileParam_30['ids'] =RiChangBanGongIntf.get_myprofile_id_by_name(myProfileParam_30['myProfile.name'] ) #CommonIntf.getDbQueryResult(dbCommand = "select t.id from myProfiles t where t.name='%s'" % (myProfileParam_30['myProfile.name']))
        shareMyProfileParam_30['resourcePoolTypeId']=CommonIntf.getDbQueryResult(dbCommand = "select p.displayseq from propertydicts  p where p.displayname = '法律法规'")  #不同的目录下typeid不同
        shareMyProfileParam_30['sendMessage'] = '0'
        shareMyProfileParam_30['identification'] = 'myProfile'
        shareMyProfileParam_30['setPermissionCacheId'] = RiChangBanGongIntf.viewObject(cacheParam_30)
        shareMyProfileParam_30['setPermissionText'] = '省级2个,市级3个,县区级5个,乡镇27个,乡村352个,网格538个,省级职能部门1个,市级职能部门1个,县区级职能部门3个,乡镇职能工作站2个' #与上面权限设置下选择的部门数量一致
        shareMyProfileParam_30['Message'] = '0'
        responseDict = RiChangBanGongIntf.share_MyProfile(shareMyProfileParam_30, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '资料分享失败')  
        
        param_30 = copy.deepcopy(RiChangBanGongPara.checkProfileDict)
        param_30['name'] = myProfileParam_30['myProfile.name']    
        param_30['id'] = shareMyProfileParam_30['ids']
        ret = RiChangBanGongIntf.check_sharingMyProfile(param_30, typeId=CommonIntf.getDbQueryResult(dbCommand = "select p.id from directorySettings p where p.name = '法律法规'") ,username=userInit['DftSheQuUser'], password='11111111')      #不同的目录下typeid：根据所属目录不同 ，法律法规、规章制度...  
        self.assertTrue(ret, '分享法律法规资料失败') 
        
        cancelSharingMyProfileParam_30 = copy.deepcopy(RiChangBanGongPara.deleteProfileDict) 
        cancelSharingMyProfileParam_30['ids'] = shareMyProfileParam_30['ids']
        responseDict = RiChangBanGongIntf.cancelSharing_MyProfile(cancelSharingMyProfileParam_30, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '资料取消分享失败')        

        ret = RiChangBanGongIntf.check_sharingMyProfile(param_30, typeId=CommonIntf.getDbQueryResult(dbCommand = "select p.id from directorySettings p where p.name = '法律法规'") ,username=userInit['DftSheQuUser'], password='11111111')      #不同的目录下typeid：根据所属目录不同 ，法律法规、规章制度...  
        self.assertFalse(ret, '取消分享的法律法规资料在共享资料中仍然存在，操作失败') 

                      
#模块： 公文管理


    def testFaWenAdd_31(self):
        '''新增发文信息'''

        documentParam_31 = copy.deepcopy(RiChangBanGongPara.documentObject) 
        documentParam_31['mode']='add'
        documentParam_31['sendOptrionalObjIds'] = orgInit['DftWangGeOrgId']  #填写当前层级下辖的orgid
        documentParam_31['document.title'] = '文件标题%s'%CommonUtil.createRandomString()
        documentParam_31['document.dispatchUnit'] = orgInit['DftSheQuOrg']  #当前账号名称
        responseDict = RiChangBanGongIntf.add_DocumentsManag(documentParam_31, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '发文信息新增失败')       
                      
        param_31 = copy.deepcopy(RiChangBanGongPara.checkDocumentDict)
        param_31['title'] = documentParam_31['document.title']   
        param_31['id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from documents p where p.title ='%s'" % (documentParam_31['document.title']))
        ret = RiChangBanGongIntf.check_DocumentsManag(param_31, sidx='createDate',username=userInit['DftSheQuUser'], password='11111111')     #sidx :（发文管理）createDate 、（收文管理）dispatchDate    
        self.assertTrue(ret, '发文信息检查失败') 
        
        pass 
    
    def testFaWenSearch_32(self):
        '''搜索发文信息'''

        documentParam_32 = copy.deepcopy(RiChangBanGongPara.documentObject) 
        documentParam_32['mode']='add'
        documentParam_32['sendOptrionalObjIds'] = orgInit['DftWangGeOrgId']  #填写当前层级下辖的orgid
        documentParam_32['document.title'] = '文件标题%s'%CommonUtil.createRandomString()
        documentParam_32['document.dispatchUnit'] = orgInit['DftSheQuOrg']  #当前账号名称
        responseDict = RiChangBanGongIntf.add_DocumentsManag(documentParam_32, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '发文信息新增失败')       
        
        newDocumentParam_32 = copy.deepcopy(RiChangBanGongPara.documentObject) 
        newDocumentParam_32['mode']='add'
        newDocumentParam_32['sendOptrionalObjIds'] = orgInit['DftWangGeOrgId']  #填写当前层级下辖的orgid
        newDocumentParam_32['document.title'] = '新增文件标题%s'%CommonUtil.createRandomString()
        newDocumentParam_32['document.dispatchUnit'] = orgInit['DftSheQuOrg']  #当前账号名称
        responseDict = RiChangBanGongIntf.add_DocumentsManag(newDocumentParam_32, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '发文信息新增失败')  
                      
        searchParam_31 = copy.deepcopy(RiChangBanGongPara.searchDocumentDict)
        searchParam_31['searchDocumentVo.title'] = documentParam_32['document.title']  
        ret = RiChangBanGongIntf.search_DocumentsManag(searchParam_31,username=userInit['DftSheQuUser'], password='11111111')     #sidx :（发文管理）createDate 、（收文管理）dispatchDate    
        self.assertTrue(ret, '发文信息搜索失败') 
        
        pass 

    def testFaWenEdit_33(self):
        '''修改未发送的发文信息'''

        documentParam_33 = copy.deepcopy(RiChangBanGongPara.documentObject) 
        documentParam_33['mode']='add'
        documentParam_33['sendOptrionalObjIds'] = orgInit['DftWangGeOrgId']  #填写当前层级下辖的orgid
        documentParam_33['document.title'] = '文件标题%s'%CommonUtil.createRandomString()
        documentParam_33['document.dispatchUnit'] = orgInit['DftSheQuOrg']  #当前账号名称
        responseDict = RiChangBanGongIntf.add_DocumentsManag(documentParam_33, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '发文信息新增失败')       
        
        editDocumentParam_33 = copy.deepcopy(RiChangBanGongPara.documentObject) 
        editDocumentParam_33['mode']='edit'
        editDocumentParam_33['document.dispatchState']='unSend'   #只有未发送的信息才可修改
        editDocumentParam_33['document.id']= CommonIntf.getDbQueryResult(dbCommand = "select p.id from documents p where p.title ='%s'" %(documentParam_33['document.title'])) 
        editDocumentParam_33['sendOptrionalObjIds'] = str(orgInit['DftWangGeOrgId'])+','+str(orgInit['DftWangGeOrgId'])   #填写当前层级下辖的orgid
        editDocumentParam_33['document.title'] = '修改文件标题%s'%CommonUtil.createRandomString()
        editDocumentParam_33['document.dispatchUnit'] = documentParam_33['document.dispatchUnit']
        responseDict = RiChangBanGongIntf.edit_DocumentsManag(editDocumentParam_33, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '发文信息修改失败')  
                      
        param_33 = copy.deepcopy(RiChangBanGongPara.checkDocumentDict)
        param_33['title'] = editDocumentParam_33['document.title']   
        param_33['id'] = editDocumentParam_33['document.id']
        ret = RiChangBanGongIntf.check_DocumentsManag(param_33, sidx='createDate',username=userInit['DftSheQuUser'], password='11111111')     #sidx :（发文管理）createDate 、（收文管理）dispatchDate    
        self.assertTrue(ret, '发文信息检查失败') 
        
        pass     

    def testFaWenDelete_34(self):  #bug
        '''批量删除发文信息'''

        documentParam_34 = copy.deepcopy(RiChangBanGongPara.documentObject) 
        documentParam_34['mode']='add'
        documentParam_34['sendOptrionalObjIds'] = orgInit['DftWangGeOrgId']  #填写当前层级下辖的orgid
        documentParam_34['document.title'] = '文件标题%s'%CommonUtil.createRandomString()
        documentParam_34['document.dispatchUnit'] = orgInit['DftSheQuOrg']  #当前账号名称
        responseDict = RiChangBanGongIntf.add_DocumentsManag(documentParam_34, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '发文信息新增失败')       
        
        newDocumentParam_34 = copy.deepcopy(RiChangBanGongPara.documentObject) 
        newDocumentParam_34['mode']='add'
        newDocumentParam_34['sendOptrionalObjIds'] = orgInit['DftWangGeOrgId']  #填写当前层级下辖的orgid
        newDocumentParam_34['document.title'] = '新增文件标题%s'%CommonUtil.createRandomString()
        newDocumentParam_34['document.dispatchUnit'] = orgInit['DftSheQuOrg']  #当前账号名称
        responseDict = RiChangBanGongIntf.add_DocumentsManag(newDocumentParam_34, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '发文信息新增失败')  
                      
        deleteParam_34 = copy.deepcopy(RiChangBanGongPara.deleteDict)
        deleteParam_34['deleteIds'] = str(CommonIntf.getDbQueryResult(dbCommand = "select p.id from documents p where p.title ='%s'" %(documentParam_34['document.title'])) )+','+str(CommonIntf.getDbQueryResult(dbCommand = "select p.id from documents p where p.title ='%s'" %(newDocumentParam_34['document.title'])) )
        ret = RiChangBanGongIntf.delete_DocumentsManag(deleteParam_34,username=userInit['DftSheQuUser'], password='11111111')     #sidx :（发文管理）createDate 、（收文管理）dispatchDate    
        self.assertTrue(ret, '发文信息删除失败') 
        
        param_34 = copy.deepcopy(RiChangBanGongPara.checkDocumentDict)
        param_34['title'] = documentParam_34['document.title']   
        ret = RiChangBanGongIntf.check_DocumentsManag(param_34, sidx='createDate',username=userInit['DftSheQuUser'], password='11111111')     #sidx :（发文管理）createDate 、（收文管理）dispatchDate    
        self.assertFalse(ret, '当前列表中一=以删除的发文信息仍然存在，删除失败') 
        
        param_34['title'] = newDocumentParam_34['document.title']   
        ret = RiChangBanGongIntf.check_DocumentsManag(param_34, sidx='createDate',username=userInit['DftSheQuUser'], password='11111111')     #sidx :（发文管理）createDate 、（收文管理）dispatchDate    
        self.assertFalse(ret, '当前列表中一=以删除的发文信息仍然存在，删除失败') 
        
        pass 

    def testFaWenEditAgain_35(self):
        '''再次编辑未发送的发文信息'''

        documentParam_35 = copy.deepcopy(RiChangBanGongPara.documentObject) 
        documentParam_35['mode']='add'
        documentParam_35['sendOptrionalObjIds'] = orgInit['DftWangGeOrgId']  #填写当前层级下辖的orgid
        documentParam_35['document.title'] = '文件标题%s'%CommonUtil.createRandomString()
        documentParam_35['document.dispatchUnit'] = orgInit['DftSheQuOrg']  #当前账号名称
        responseDict = RiChangBanGongIntf.add_DocumentsManag(documentParam_35, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '发文信息新增失败')       
        
        editAgainDocumentParam_35 = copy.deepcopy(RiChangBanGongPara.documentObject) 
        editAgainDocumentParam_35['mode']='editAgain'
        editAgainDocumentParam_35['document.dispatchState']='unSend'   #只有未发送的信息才可修改
        editAgainDocumentParam_35['document.id']= CommonIntf.getDbQueryResult(dbCommand = "select p.id from documents p where p.title ='%s'" %(documentParam_35['document.title'])) 
        editAgainDocumentParam_35['beforeSendOptrionalObjIds'] = orgInit['DftWangGeOrgId']   #填写当前层级下辖的orgid
        editAgainDocumentParam_35['beforeCopySendOptrionalObjIds'] = orgInit['DftWangGeOrgId'] 
        editAgainDocumentParam_35['document.title'] = documentParam_35['document.title']
        editAgainDocumentParam_35['document.dispatchUnit'] = documentParam_35['document.dispatchUnit']
        responseDict = RiChangBanGongIntf.editAgain_DocumentsManag(editAgainDocumentParam_35, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '发文信息再次编辑失败')  
                      
        param_33 = copy.deepcopy(RiChangBanGongPara.checkDocumentDict)
        param_33['title'] = editAgainDocumentParam_35['document.title']   
        param_33['id'] = editAgainDocumentParam_35['document.id']
        ret = RiChangBanGongIntf.check_DocumentsManag(param_33, sidx='createDate',username=userInit['DftSheQuUser'], password='11111111')     #sidx :（发文管理）createDate 、（收文管理）dispatchDate    
        self.assertTrue(ret, '发文信息检查失败') 
        
        pass  

    def testFaWenSynchToMyProfile_36(self):
        '''将未发送的发文信息同步到资料库'''

        documentParam_36 = copy.deepcopy(RiChangBanGongPara.documentObject) 
        documentParam_36['mode']='add'
        documentParam_36['sendOptrionalObjIds'] = orgInit['DftWangGeOrgId']  #填写当前层级下辖的orgid
        documentParam_36['document.title'] = '文件标题%s'%CommonUtil.createRandomString()
        documentParam_36['document.dispatchUnit'] = orgInit['DftSheQuOrg']  #当前账号名称
        responseDict = RiChangBanGongIntf.add_DocumentsManag(documentParam_36, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '发文信息新增失败')   
        
        cacheParam_36 = copy.deepcopy(RiChangBanGongPara.cacheObject) 
#         cacheParam_36['viewObjectVo.selectedCheckBoxStrs'] = ''   #8070（当前）/<8080时数据不同>  全选时不填  按层级选择时需填写（可多选）  省：50-0 市：40-0 县：30-0 乡镇：20-0 联村：15-0 村：10-0 网格：0-0 省级职能部门：50-1 市级职能部门：40-1 县级职能部门：30-1 乡镇职能工作站：20-1
#         cacheParam_36['viewObjectVo.selectedIdStrs']=''
#         cacheParam_36['viewObjectVo.exclusiveIdStrs'] = ''
        cacheParam_36['viewObjectVo.provinceNum'] = '2'
        cacheParam_36['viewObjectVo.cityNum'] = '3'
        cacheParam_36['viewObjectVo.districtNum'] = '5'
        cacheParam_36['viewObjectVo.townNum'] = '27'
        cacheParam_36['viewObjectVo.unitedVillageNum'] = '2'
        cacheParam_36['viewObjectVo.villageNum'] = '352'
        cacheParam_36['viewObjectVo.gridNum'] = '538'
        cacheParam_36['viewObjectVo.provinceFucDepartmentNum'] = '1'
        cacheParam_36['viewObjectVo.cityFucDepartmentNum'] = '1'
        cacheParam_36['viewObjectVo.districtFucDepartmentNum'] = '3'
        cacheParam_36['viewObjectVo.townFucDepartmentNum'] = '2'
        cacheParam_36['viewObjectVo.defProvinceNum'] = '2'
        cacheParam_36['viewObjectVo.defCityNum'] = '3'
        cacheParam_36['viewObjectVo.defDistrictNum'] = '5'
        cacheParam_36['viewObjectVo.defTownNum'] = '27'
        cacheParam_36['viewObjectVo.defUnitedVillageNum'] = '2'
        cacheParam_36['viewObjectVo.defVillageNum'] = '352'
        cacheParam_36['viewObjectVo.defGridNum'] = '538'
        cacheParam_36['viewObjectVo.defProvinceFucDepartmentNum'] = '1'
        cacheParam_36['viewObjectVo.defCityFucDepartmentNum'] = '1'
        cacheParam_36['viewObjectVo.defDistrictFucDepartmentNum'] = '3'
        cacheParam_36['viewObjectVo.defTownFucDepartmentNum'] = '2'
        cacheParam_36['viewObjectVo.selectedRadio'] = 'selectAll'  #全选 selectAll   选择部分层级selectByLevel

        synchMyProfileParam_36 = copy.deepcopy(RiChangBanGongPara.shareProfileDict) 
        synchMyProfileParam_36['ids'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from documents  p where p.title='%s'" % (documentParam_36['document.title']))
        synchMyProfileParam_36['resourcePoolTypeId']=CommonIntf.getDbQueryResult(dbCommand = "select p.displayseq from propertydicts  p where p.displayname = '法律法规'")  #不同的目录下typeid不同
        synchMyProfileParam_36['sendMessage'] = '0'
        synchMyProfileParam_36['identification'] = 'docSynchro'
        synchMyProfileParam_36['setPermissionCacheId'] = RiChangBanGongIntf.viewObject(cacheParam_36)
        synchMyProfileParam_36['setPermissionText'] = '省级2个,市级3个,县区级5个,乡镇27个,乡村352个,网格538个,省级职能部门1个,市级职能部门1个,县区级职能部门3个,乡镇职能工作站2个' #与上面权限设置下选择的部门数量一致
        synchMyProfileParam_36['Message'] = '0'
        responseDict = RiChangBanGongIntf.synch_DocumentsManag(synchMyProfileParam_36, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '资料同步失败') 

        param_36 = copy.deepcopy(RiChangBanGongPara.checkProfileDict)
        param_36['name'] = documentParam_36['document.title']    
        param_36['id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from myProfiles t where t.name='%s'" % (documentParam_36['document.title']))
        ret = RiChangBanGongIntf.check_sharingMyProfile(param_36, typeId=CommonIntf.getDbQueryResult(dbCommand = "select p.id from directorySettings p where p.name = '法律法规'") ,username=userInit['DftSheQuUser'], password='11111111')      #不同的目录下typeid：根据所属目录不同 ，法律法规、规章制度...  
        self.assertTrue(ret, '分享法律法规资料失败') 

    def testFaWenSynchToWorkingRecord_37(self):
        '''将发文信息同步到台账'''

        documentParam_37 = copy.deepcopy(RiChangBanGongPara.documentObject) 
        documentParam_37['mode']='add'
        documentParam_37['sendOptrionalObjIds'] = orgInit['DftWangGeOrgId']  #填写当前层级下辖的orgid
        documentParam_37['document.title'] = '文件标题%s'%CommonUtil.createRandomString()
        documentParam_37['document.dispatchUnit'] = orgInit['DftSheQuOrg']  #当前账号名称
        responseDict = RiChangBanGongIntf.add_DocumentsManag(documentParam_37, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '发文信息新增失败')    
        
        newWorkingParam_37 = copy.deepcopy(RiChangBanGongPara.workingRecordObject) 
        newWorkingParam_37['mode']='add'
        newWorkingParam_37['fileType']='会议类'
        newWorkingParam_37['newWorkingRecords.RECORDTYPE.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.displayname = '会议类' and p.propertydomainid = (select t.id from propertydomains t where t.domainname = '新工作台帐目录类型')")
        newWorkingParam_37['newWorkingRecords.dailyDirectory.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from DailyDirectorys t where t.shortname='会议' and t.dailyyearid = (select id from dailyYears d where d.yeardate=%s and d.makedorgid=%s and d.dailytype='0')" %(time.strftime("%Y"), orgInit['DftJieDaoOrgId']))      # yeardate：当前年份，  makedorgid：街道层级，即上一层级id，  dailytype : 0-行政部门 ，1-职能部门 
        newWorkingParam_37['documentId'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from documents p where p.title = '%s'" % documentParam_37['document.title'])
        newWorkingParam_37['newWorkingRecords.departmentType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '平安办'")
        newWorkingParam_37['newWorkingRecords.name'] = documentParam_37['document.title']
        newWorkingParam_37['newWorkingRecords.dealDate'] = '2015-12-24'
        newWorkingParam_37['selectedTypes'] = CommonIntf.getIdByDomainAndDisplayName(domainName='台帐关键字', displayName='平安')   #可多选
        newWorkingParam_37['newWorkingRecords.content'] = '主要内容'  
        responseDict = RiChangBanGongIntf.synch_Documents(newWorkingParam_37, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '发文信息同步失败')   # 失败   
                      
        param_01 = copy.deepcopy(RiChangBanGongPara.checkRecordDict)
        param_01['name'] = newWorkingParam_37['newWorkingRecords.name']    
        param_01['id'] = CommonIntf.getDbQueryResult(dbCommand = "select id from newWorkingRecords d where d.name='%s'" % (newWorkingParam_37['newWorkingRecords.name']))
        ret = RiChangBanGongIntf.check_WorkingRecord(param_01, orgId=orgInit['DftSheQuOrgId'],dailyDirectoryId=newWorkingParam_37['newWorkingRecords.dailyDirectory.id'],username=userInit['DftSheQuUser'], password='11111111')         
        self.assertTrue(ret, '查找会议记录失败') 
        
        pass

    def testFaWenSend_38(self):
        '''新增发文信息'''

        documentParam_38 = copy.deepcopy(RiChangBanGongPara.documentObject) 
        documentParam_38['mode']='add'
        documentParam_38['sendOptrionalObjIds'] = orgInit['DftWangGeOrgId']  #填写当前层级下辖的orgid
        documentParam_38['document.title'] = '发送文件%s'%CommonUtil.createRandomString()
        documentParam_38['document.dispatchUnit'] = orgInit['DftSheQuOrg']  #当前账号名称
        responseDict = RiChangBanGongIntf.add_DocumentsManag(documentParam_38, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '发文信息新增失败')       
        
        sendDocumentParam_38 = copy.deepcopy(RiChangBanGongPara.documentDict) 
        sendDocumentParam_38['mode']='send'
        sendDocumentParam_38['selectedIds'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from documents p where p.title ='%s'" % (documentParam_38['document.title']))
        responseDict = RiChangBanGongIntf.send_Documents(sendDocumentParam_38, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '发文信息发送失败')          
                      
        param_38 = copy.deepcopy(RiChangBanGongPara.checkDocumentDict)
        param_38['title'] = documentParam_38['document.title']   
        param_38['id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from documents p where p.title ='%s'" % (documentParam_38['document.title']))
        ret = RiChangBanGongIntf.check_Documents(param_38, sidx='dispatchDate',username=userInit['DftWangGeUser'], password='11111111')     #sidx :（发文管理）createDate 、（收文管理）dispatchDate    
        self.assertTrue(ret, '发文信息检查失败') 
        
        pass 

    def testFaWenWithdraw_39(self):
        '''撤回发文信息'''

        documentParam_39 = copy.deepcopy(RiChangBanGongPara.documentObject) 
        documentParam_39['mode']='add'
        documentParam_39['sendOptrionalObjIds'] = orgInit['DftWangGeOrgId']  #填写当前层级下辖的orgid
        documentParam_39['document.title'] = '撤回文件%s'%CommonUtil.createRandomString()
        documentParam_39['document.dispatchUnit'] = orgInit['DftSheQuOrg']  #当前账号名称
        responseDict = RiChangBanGongIntf.add_DocumentsManag(documentParam_39, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '发文信息新增失败')       
        
        sendDocumentParam_39 = copy.deepcopy(RiChangBanGongPara.documentDict) 
        sendDocumentParam_39['mode']='send'
        sendDocumentParam_39['selectedIds'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from documents p where p.title ='%s'" % (documentParam_39['document.title']))
        responseDict = RiChangBanGongIntf.send_Documents(sendDocumentParam_39, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '发文信息发送失败')          
                      
        param_39 = copy.deepcopy(RiChangBanGongPara.checkDocumentDict)
        param_39['title'] = documentParam_39['document.title']   
        param_39['id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from documents p where p.title ='%s'" % (documentParam_39['document.title']))
        ret = RiChangBanGongIntf.check_Documents(param_39, sidx='dispatchDate',username=userInit['DftWangGeUser'], password='11111111')     #sidx :（发文管理）createDate 、（收文管理）dispatchDate    
        self.assertTrue(ret, '发文信息检查失败') 
        
        withdrawDocumentParam_39 = copy.deepcopy(RiChangBanGongPara.documentDict) 
        withdrawDocumentParam_39['selectedIds'] = sendDocumentParam_39['selectedIds'] 
        responseDict = RiChangBanGongIntf.withdraw_Documents(withdrawDocumentParam_39, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '发文信息撤回失败')  
        
        param_39['title'] = documentParam_39['document.title']   
        param_39['id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from documents p where p.title ='%s'" % (documentParam_39['document.title']))
        ret = RiChangBanGongIntf.check_Documents(param_39, sidx='dispatchDate',username=userInit['DftWangGeUser'], password='11111111')     #sidx :（发文管理）createDate 、（收文管理）dispatchDate    
        self.assertFalse(ret, '已撤回的发文信息在列表中依然存在，撤回失败')               
        
        pass 

    def testShouWenSearch_40(self):
        '''高级搜索收文信息'''
 
        documentParam_40 = copy.deepcopy(RiChangBanGongPara.documentObject) 
        documentParam_40['mode']='add'
        documentParam_40['sendOptrionalObjIds'] = orgInit['DftWangGeOrgId']  #填写当前层级下辖的orgid
        documentParam_40['document.title'] = '文件标题%s'%CommonUtil.createRandomString()
        documentParam_40['document.dispatchUnit'] = orgInit['DftSheQuOrg']  #当前账号名称
        responseDict = RiChangBanGongIntf.add_DocumentsManag(documentParam_40, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '发文信息新增失败')      
        
        newDocumentParam_40 = copy.deepcopy(RiChangBanGongPara.documentObject) 
        newDocumentParam_40['mode']='add'
        newDocumentParam_40['sendOptrionalObjIds'] = orgInit['DftWangGeOrgId']  #填写当前层级下辖的orgid
        newDocumentParam_40['document.title'] = '文件标题%s'%CommonUtil.createRandomString()
        newDocumentParam_40['document.dispatchUnit'] = orgInit['DftSheQuOrg']  #当前账号名称
        responseDict = RiChangBanGongIntf.add_DocumentsManag(documentParam_40, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '发文信息新增失败')   
        
        sendDocumentParam_40 = copy.deepcopy(RiChangBanGongPara.documentDict) 
        sendDocumentParam_40['mode']='send'
        sendDocumentParam_40['selectedIds'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from documents p where p.title ='%s'" % (documentParam_40['document.title']))
        responseDict = RiChangBanGongIntf.send_Documents(sendDocumentParam_40, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '发文信息发送失败')  
        
        newSendDocumentParam_40 = copy.deepcopy(RiChangBanGongPara.documentDict) 
        newSendDocumentParam_40['mode']='send'
        newSendDocumentParam_40['selectedIds'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from documents p where p.title ='%s'" % (newDocumentParam_40['document.title']))
        responseDict = RiChangBanGongIntf.send_Documents(newSendDocumentParam_40, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '发文信息发送失败') 
                      
        searchParam_40 = copy.deepcopy(RiChangBanGongPara.searchShouWenDict)
        searchParam_40['searchDocumentVo.title'] = documentParam_40['document.title']  
        ret = RiChangBanGongIntf.search_ReceiveDocumentsManag(searchParam_40,username=userInit['DftWangGeUser'], password='11111111')     #sidx :（发文管理）createDate 、（收文管理）dispatchDate    
        self.assertTrue(ret, '收文信息搜索失败') 
        
        pass

    def testFaWenReceive_41(self):
        '''签收文件信息'''

        documentParam_41 = copy.deepcopy(RiChangBanGongPara.documentObject) 
        documentParam_41['mode']='add'
        documentParam_41['sendOptrionalObjIds'] = orgInit['DftWangGeOrgId']  #填写当前层级下辖的orgid
        documentParam_41['document.title'] = '签收文件%s'%CommonUtil.createRandomString()
        documentParam_41['document.dispatchUnit'] = orgInit['DftSheQuOrg']  #当前账号名称
        responseDict = RiChangBanGongIntf.add_DocumentsManag(documentParam_41, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '发文信息新增失败')       
        
        sendDocumentParam_41 = copy.deepcopy(RiChangBanGongPara.documentDict) 
        sendDocumentParam_41['mode']='send'
        sendDocumentParam_41['selectedIds'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from documents p where p.title ='%s'" % (documentParam_41['document.title']))
        responseDict = RiChangBanGongIntf.send_Documents(sendDocumentParam_41, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '发文信息发送失败')                   
                      
        receiveParam_41 = copy.deepcopy(RiChangBanGongPara.receiveDocumentDict)
        receiveParam_41['selectedIds'] = CommonIntf.getDbQueryResult(dbCommand = "select p.documentsHasOrgid from documentsHasOrg p where p.documentid ='%s'" % (sendDocumentParam_41['selectedIds']))
        receiveParam_41['documentsHasOrg.signDate'] = Time.getCurrentDateAndTime()
        receiveParam_41['documentsHasOrg.signer'] = userInit['DftWangGeUserXM']
        ret = RiChangBanGongIntf.receive_DocumentsManag(receiveParam_41, username=userInit['DftWangGeUser'], password='11111111')      
        self.assertTrue(ret, '文件信息签收失败') 
        
        pass 

    def testFaWenRead_42(self):
        '''阅读已签收的文件信息'''

        documentParam_42 = copy.deepcopy(RiChangBanGongPara.documentObject) 
        documentParam_42['mode']='add'
        documentParam_42['sendOptrionalObjIds'] = orgInit['DftWangGeOrgId']  #填写当前层级下辖的orgid
        documentParam_42['document.title'] = '阅读文件%s'%CommonUtil.createRandomString()
        documentParam_42['document.dispatchUnit'] = orgInit['DftSheQuOrg']  #当前账号名称
        responseDict = RiChangBanGongIntf.add_DocumentsManag(documentParam_42, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '发文信息新增失败')       
        
        sendDocumentParam_42 = copy.deepcopy(RiChangBanGongPara.documentDict) 
        sendDocumentParam_42['mode']='send'
        sendDocumentParam_42['selectedIds'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from documents p where p.title ='%s'" % (documentParam_42['document.title']))
        responseDict = RiChangBanGongIntf.send_Documents(sendDocumentParam_42, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '发文信息发送失败')                   
                      
        receiveParam_42 = copy.deepcopy(RiChangBanGongPara.receiveDocumentDict)
        receiveParam_42['selectedIds'] = CommonIntf.getDbQueryResult(dbCommand = "select p.documentsHasOrgid from documentsHasOrg p where p.documentid ='%s'" % (sendDocumentParam_42['selectedIds']))
        receiveParam_42['documentsHasOrg.signDate'] = Time.getCurrentDateAndTime()
        receiveParam_42['documentsHasOrg.signer'] = userInit['DftWangGeUserXM']
        ret = RiChangBanGongIntf.receive_DocumentsManag(receiveParam_42, username=userInit['DftWangGeUser'], password='11111111')      
        self.assertTrue(ret, '文件信息签收失败') 
        
        readParam_42 = copy.deepcopy(RiChangBanGongPara.readDict) 
        readParam_42['mode']='view'
        readParam_42['document.id'] = sendDocumentParam_42['selectedIds']
        readParam_42['document.documentsHasOrgId'] = receiveParam_42['selectedIds']
        responseDict = RiChangBanGongIntf.read_DocumentsManag(readParam_42, username=userInit['DftWangGeUser'], password='11111111')  
        
        readDocumentParam_42 = copy.deepcopy(RiChangBanGongPara.documentDict) 
        readDocumentParam_42['mode']='getReadStat'
        readDocumentParam_42['selectedIds'] = readParam_42['document.documentsHasOrgId']
        responseDict = RiChangBanGongIntf.read_DocumentsManag(readDocumentParam_42, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '文件信息阅读失败')         
        
        pass 

    def testFaWenTransmit_43(self):
        '''转发已阅读已签收的文件信息'''
        #街道发文->社区阅读签收并转发->网格查看   
        
        documentParam_43 = copy.deepcopy(RiChangBanGongPara.documentObject) 
        documentParam_43['mode'] = 'add'
        documentParam_43['sendOptrionalObjIds'] = orgInit['DftSheQuOrgId']  #填写当前层级下辖的orgid
        documentParam_43['document.title'] = '转发文件%s'%CommonUtil.createRandomString()
        documentParam_43['document.dispatchUnit'] = orgInit['DftJieDaoOrg']  #当前账号名称
        responseDict = RiChangBanGongIntf.add_DocumentsManag(documentParam_43, username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(responseDict.result, '发文信息新增失败')       
        
        sendDocumentParam_43 = copy.deepcopy(RiChangBanGongPara.documentDict) 
        sendDocumentParam_43['mode']='send'
        sendDocumentParam_43['selectedIds'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from documents p where p.title ='%s'" % (documentParam_43['document.title']))
        responseDict = RiChangBanGongIntf.send_Documents(sendDocumentParam_43, username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(responseDict.result, '发文信息发送失败')                   
                      
        receiveParam_43 = copy.deepcopy(RiChangBanGongPara.receiveDocumentDict)
        receiveParam_43['selectedIds'] = CommonIntf.getDbQueryResult(dbCommand = "select p.documentsHasOrgid from documentsHasOrg p where p.documentid ='%s'" % (sendDocumentParam_43['selectedIds']))
        receiveParam_43['documentsHasOrg.signDate'] = Time.getCurrentDateAndTime()
        receiveParam_43['documentsHasOrg.signer'] = userInit['DftSheQuUserXM']
        ret = RiChangBanGongIntf.receive_DocumentsManag(receiveParam_43, username=userInit['DftSheQuUser'], password='11111111')      
        self.assertTrue(ret, '文件信息签收失败') 
        
        readParam_43 = copy.deepcopy(RiChangBanGongPara.readDict) 
        readParam_43['mode'] = 'view'
        readParam_43['document.id'] = sendDocumentParam_43['selectedIds']
        readParam_43['document.documentsHasOrgId'] = receiveParam_43['selectedIds']
        responseDict = RiChangBanGongIntf.read_DocumentsManag(readParam_43, username=userInit['DftSheQuUser'], password='11111111')  
        
        readDocumentParam_43 = copy.deepcopy(RiChangBanGongPara.documentDict) 
        readDocumentParam_43['mode']='getReadStat'
        readDocumentParam_43['selectedIds'] = readParam_43['document.documentsHasOrgId']
        responseDict = RiChangBanGongIntf.read_DocumentsManag(readDocumentParam_43, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '文件信息阅读失败')  
        
        transmitParam_43 = copy.deepcopy(RiChangBanGongPara.documentObject) 
        transmitParam_43['mode'] = 'transmit'
        transmitParam_43['document.dispatchState'] = 'sended'
        transmitParam_43['document.id'] = readParam_43['document.id']
        transmitParam_43['sendOptrionalObjIds'] = orgInit['DftWangGeOrgId']  #填写当前层级下辖的orgid
        transmitParam_43['document.title'] = documentParam_43['document.title']
        transmitParam_43['document.dispatchUnit'] = documentParam_43['document.dispatchUnit']       
        responseDict = RiChangBanGongIntf.transmit_DocumentsManag(transmitParam_43, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '发文信息转发失败')            
       
        param_43 = copy.deepcopy(RiChangBanGongPara.checkDocumentDict)
        param_43['title'] = transmitParam_43['document.title']
        param_43['id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from documents p where p.title ='%s' and p.orgid='%s'" % (transmitParam_43['document.title'],orgInit['DftWangGeOrgId']))
        ret = RiChangBanGongIntf.check_Manag(param_43, sidx='dispatchDate',username=userInit['DftWangGeUser'], password='11111111')     #sidx :（发文管理）createDate 、（收文管理）dispatchDate    
        self.assertTrue(ret, '发文信息检查失败') 
        
        pass 

    def testShouWenDelete_44(self):
        '''批量删除收文信息'''

        documentParam_44 = copy.deepcopy(RiChangBanGongPara.documentObject) 
        documentParam_44['mode'] = 'add'
        documentParam_44['sendOptrionalObjIds'] = orgInit['DftSheQuOrgId']  #填写当前层级下辖的orgid
        documentParam_44['document.title'] = '新增删除文件%s'%CommonUtil.createRandomString()
        documentParam_44['document.dispatchUnit'] = orgInit['DftJieDaoOrg']  #当前账号名称
        responseDict = RiChangBanGongIntf.add_DocumentsManag(documentParam_44, username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(responseDict.result, '发文信息新增失败')       
        
        sendDocumentParam_44 = copy.deepcopy(RiChangBanGongPara.documentDict) 
        sendDocumentParam_44['mode']='send'
        sendDocumentParam_44['selectedIds'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from documents p where p.title ='%s'" % (documentParam_44['document.title']))
        responseDict = RiChangBanGongIntf.send_Documents(sendDocumentParam_44, username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(responseDict.result, '发文信息发送失败')                   
                      
        receiveParam_44 = copy.deepcopy(RiChangBanGongPara.receiveDocumentDict)
        receiveParam_44['selectedIds'] = CommonIntf.getDbQueryResult(dbCommand = "select p.documentsHasOrgid from documentsHasOrg p where p.documentid ='%s'" % (sendDocumentParam_44['selectedIds']))
        receiveParam_44['documentsHasOrg.signDate'] = Time.getCurrentDateAndTime()
        receiveParam_44['documentsHasOrg.signer'] = userInit['DftSheQuUserXM']
        ret = RiChangBanGongIntf.receive_DocumentsManag(receiveParam_44, username=userInit['DftSheQuUser'], password='11111111')      
        self.assertTrue(ret, '文件信息签收失败') 
        
        readParam_44 = copy.deepcopy(RiChangBanGongPara.readDict) 
        readParam_44['mode'] = 'view'
        readParam_44['document.id'] = sendDocumentParam_44['selectedIds']
        readParam_44['document.documentsHasOrgId'] = receiveParam_44['selectedIds']
        responseDict = RiChangBanGongIntf.read_DocumentsManag(readParam_44, username=userInit['DftSheQuUser'], password='11111111')  
        
        readDocumentParam_44 = copy.deepcopy(RiChangBanGongPara.documentDict) 
        readDocumentParam_44['mode']='getReadStat'
        readDocumentParam_44['selectedIds'] = readParam_44['document.documentsHasOrgId']
        responseDict = RiChangBanGongIntf.read_DocumentsManag(readDocumentParam_44, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '文件信息阅读失败')   
        
        newDocumentParam_44 = copy.deepcopy(RiChangBanGongPara.documentObject) 
        newDocumentParam_44['mode'] = 'add'
        newDocumentParam_44['sendOptrionalObjIds'] = orgInit['DftSheQuOrgId']  #填写当前层级下辖的orgid
        newDocumentParam_44['document.title'] = '新增删除文件%s'%CommonUtil.createRandomString()
        newDocumentParam_44['document.dispatchUnit'] = orgInit['DftJieDaoOrg']  #当前账号名称
        responseDict = RiChangBanGongIntf.add_DocumentsManag(newDocumentParam_44, username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(responseDict.result, '发文信息新增失败')    
        
        newSendDocumentParam_44 = copy.deepcopy(RiChangBanGongPara.documentDict) 
        newSendDocumentParam_44['mode']='send'
        newSendDocumentParam_44['selectedIds'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from documents p where p.title ='%s'" % (newDocumentParam_44['document.title']))
        responseDict = RiChangBanGongIntf.send_Documents(newSendDocumentParam_44, username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(responseDict.result, '发文信息发送失败')                   
                      
        newReceiveParam_44 = copy.deepcopy(RiChangBanGongPara.receiveDocumentDict)
        newReceiveParam_44['selectedIds'] = CommonIntf.getDbQueryResult(dbCommand = "select p.documentsHasOrgid from documentsHasOrg p where p.documentid ='%s'" % (newSendDocumentParam_44['selectedIds']))
        newReceiveParam_44['documentsHasOrg.signDate'] = Time.getCurrentDateAndTime()
        newReceiveParam_44['documentsHasOrg.signer'] = userInit['DftSheQuUserXM']
        ret = RiChangBanGongIntf.receive_DocumentsManag(newReceiveParam_44, username=userInit['DftSheQuUser'], password='11111111')      
        self.assertTrue(ret, '文件信息签收失败') 
        
        newReadParam_44 = copy.deepcopy(RiChangBanGongPara.readDict) 
        newReadParam_44['mode'] = 'view'
        newReadParam_44['document.id'] = newSendDocumentParam_44['selectedIds']
        newReadParam_44['document.documentsHasOrgId'] = newReceiveParam_44['selectedIds']
        responseDict = RiChangBanGongIntf.read_DocumentsManag(newReadParam_44, username=userInit['DftSheQuUser'], password='11111111')  
        
        newReadDocumentParam_44 = copy.deepcopy(RiChangBanGongPara.documentDict) 
        newReadDocumentParam_44['mode']='getReadStat'
        newReadDocumentParam_44['selectedIds'] = newReadParam_44['document.documentsHasOrgId']
        responseDict = RiChangBanGongIntf.read_DocumentsManag(newReadDocumentParam_44, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '文件信息阅读失败')  
              
        deleteParam_44 = copy.deepcopy(RiChangBanGongPara.delete)
        deleteParam_44['selectedIds'] = str(sendDocumentParam_44['selectedIds'])+','+str(newSendDocumentParam_44['selectedIds'])
        ret = RiChangBanGongIntf.delete_Documents(deleteParam_44,username=userInit['DftSheQuUser'], password='11111111')    
        self.assertTrue(ret, '收文信息删除失败') 
        
        param_44 = copy.deepcopy(RiChangBanGongPara.checkDocumentDict)
        param_44['title'] = documentParam_44['document.title']   
        param_44['id'] = readDocumentParam_44['selectedIds']
        ret = RiChangBanGongIntf.check_Documents(param_44, sidx='dispatchDate',username=userInit['DftSheQuUser'], password='11111111')     #sidx :（发文管理）createDate 、（收文管理）dispatchDate    
        self.assertFalse(ret, '当前列表中已删除的收文信息仍然存在，删除失败') 
        
        param_44['title'] = newDocumentParam_44['document.title']   
        param_44['id'] = newReadDocumentParam_44['selectedIds']
        ret = RiChangBanGongIntf.check_Documents(param_44, sidx='dispatchDate',username=userInit['DftSheQuUser'], password='11111111')     #sidx :（发文管理）createDate 、（收文管理）dispatchDate    
        self.assertFalse(ret, '当前列表中已删除的收文信息仍然存在，删除失败') 
        
        pass 

    def testGongWenSearch_45(self):
        '''在公文查询模块下高级搜索公文信息'''
        #公文搜索模块：包括当前层级处理的所有公文信息，例新增的发文信息搜索
         
        documentParam_45 = copy.deepcopy(RiChangBanGongPara.documentObject) 
        documentParam_45['mode']='add'
        documentParam_45['sendOptrionalObjIds'] = orgInit['DftWangGeOrgId']  #填写当前层级下辖的orgid
        documentParam_45['document.title'] = '搜索文件标题%s'%CommonUtil.createRandomString()
        documentParam_45['document.dispatchUnit'] = orgInit['DftSheQuOrg']  #当前账号名称
        responseDict = RiChangBanGongIntf.add_DocumentsManag(documentParam_45, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '发文信息新增失败')      
                      
        searchParam_45 = copy.deepcopy(RiChangBanGongPara.searchGongWenDict)
        searchParam_45['searchDocumentVo.title'] = documentParam_45['document.title']  
        ret = RiChangBanGongIntf.search_GongWenManag(searchParam_45,username=userInit['DftSheQuUser'], password='11111111')     #sidx :（发文管理）createDate 、（收文管理）dispatchDate    
        self.assertTrue(ret, '公文信息搜索失败') 
        
        pass


#模块： 民情日志


    def testLogManageAdd_46(self):
        '''新增日志信息'''

        peopleLogParam_46 = copy.deepcopy(RiChangBanGongPara.logManageObject) 
        peopleLogParam_46['mode']='add'
        peopleLogParam_46['isSubmit'] = 'true'
        peopleLogParam_46['peopleLog.isAttachment'] = 'peopleLog.isAttachment'
        peopleLogParam_46['peopleLog.belonger'] = '日志所属人%s'%CommonUtil.createRandomString()
        peopleLogParam_46['peopleLog.publishDate'] = Time.getCurrentDate()
        peopleLogParam_46['peopleLog.title'] ='日志标题%s'%CommonUtil.createRandomString()
        peopleLogParam_46['peopleLog.contents'] ='日志内容%s'%CommonUtil.createRandomString()
        responseDict = RiChangBanGongIntf.add_logManage(peopleLogParam_46, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '日志信息新增失败')       
                      
        param_46 = copy.deepcopy(RiChangBanGongPara.checkLogManageDict)
        param_46['id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from peopleLog p where p.title ='%s'" % (peopleLogParam_46['peopleLog.title']))
        ret = RiChangBanGongIntf.check_logManage(param_46, username=userInit['DftSheQuUser'], password='11111111')     #sidx :（发文管理）createDate 、（收文管理）dispatchDate    
        self.assertTrue(ret, '日志信息检查失败') 
        
        pass 
        
    def testLogManageEdit_47(self):
        '''修改日志信息'''

        peopleLogParam_47 = copy.deepcopy(RiChangBanGongPara.logManageObject) 
        peopleLogParam_47['mode']='add'
        peopleLogParam_47['isSubmit'] = 'true'
        peopleLogParam_47['peopleLog.isAttachment'] = 'peopleLog.isAttachment'
        peopleLogParam_47['peopleLog.belonger'] = '日志所属人%s'%CommonUtil.createRandomString()
        peopleLogParam_47['peopleLog.publishDate'] = Time.getCurrentDate()
        peopleLogParam_47['peopleLog.title'] ='日志标题%s'%CommonUtil.createRandomString()
        peopleLogParam_47['peopleLog.contents'] ='日志内容%s'%CommonUtil.createRandomString()
        responseDict = RiChangBanGongIntf.add_logManage(peopleLogParam_47, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '日志信息新增失败')     
        
        editLogParam_47 = copy.deepcopy(RiChangBanGongPara.logManageObject) 
        editLogParam_47['mode'] ='edit'
        editLogParam_47['peopleLog.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from peopleLog p where p.title ='%s'" % (peopleLogParam_47['peopleLog.title']))
        editLogParam_47['isSubmit'] = 'true'
        editLogParam_47['peopleLog.isAttachment'] = 'false'
        editLogParam_47['peopleLog.belonger'] = peopleLogParam_47['peopleLog.belonger']
        editLogParam_47['peopleLog.publishDate'] = peopleLogParam_47['peopleLog.publishDate']
        editLogParam_47['peopleLog.title'] = '修改日志标题%s'%CommonUtil.createRandomString()
        editLogParam_47['peopleLog.contents'] = peopleLogParam_47['peopleLog.contents']
        responseDict = RiChangBanGongIntf.edit_logManage(editLogParam_47, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '日志信息修改失败')    
                      
        param_47 = copy.deepcopy(RiChangBanGongPara.checkLogManageDict)
        param_47['id'] = editLogParam_47['peopleLog.id']
        ret = RiChangBanGongIntf.check_logManage(param_47, username=userInit['DftSheQuUser'], password='11111111')    
        self.assertTrue(ret, '日志信息检查失败') 
        
        pass 

    def testLogManageSearch_48(self):
        '''搜索日志信息'''

        peopleLogParam_48 = copy.deepcopy(RiChangBanGongPara.logManageObject) 
        peopleLogParam_48['mode']='add'
        peopleLogParam_48['isSubmit'] = 'true'
        peopleLogParam_48['peopleLog.isAttachment'] = 'peopleLog.isAttachment'
        peopleLogParam_48['peopleLog.belonger'] = '日志所属人%s'%CommonUtil.createRandomString()
        peopleLogParam_48['peopleLog.publishDate'] = Time.getCurrentDate()
        peopleLogParam_48['peopleLog.title'] ='日志标题%s'%CommonUtil.createRandomString()
        peopleLogParam_48['peopleLog.contents'] ='日志内容%s'%CommonUtil.createRandomString()
        responseDict = RiChangBanGongIntf.add_logManage(peopleLogParam_48, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '日志信息新增失败')       
        
        newLogParam_48 = copy.deepcopy(RiChangBanGongPara.logManageObject) 
        newLogParam_48['mode']='add'
        newLogParam_48['isSubmit'] = 'true'
        newLogParam_48['peopleLog.isAttachment'] = 'peopleLog.isAttachment'
        newLogParam_48['peopleLog.belonger'] = '日志所属人%s'%CommonUtil.createRandomString()
        newLogParam_48['peopleLog.publishDate'] = Time.getCurrentDate()
        newLogParam_48['peopleLog.title'] ='新增日志标题%s'%CommonUtil.createRandomString()
        newLogParam_48['peopleLog.contents'] ='日志内容%s'%CommonUtil.createRandomString()
        responseDict = RiChangBanGongIntf.add_logManage(newLogParam_48, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '日志信息新增失败') 
        
        searchParam_48 = copy.deepcopy(RiChangBanGongPara.searchLogManageDict)
        searchParam_48['searchPeopleLogVo.title'] = peopleLogParam_48['peopleLog.title']
        responseDict = RiChangBanGongIntf.search_logManage(newLogParam_48, username=userInit['DftSheQuUser'], password='11111111')
#         self.assertTrue(responseDict.result, '日志信息搜素失败')       
                      
        param_48 = copy.deepcopy(RiChangBanGongPara.checkLogManageDict)
        param_48['id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from peopleLog p where p.title ='%s'" % (peopleLogParam_48['peopleLog.title']))
        ret = RiChangBanGongIntf.check_logManage(param_48, username=userInit['DftSheQuUser'], password='11111111')    
        self.assertTrue(ret, '日志信息检查失败') 
        
        pass 

    def testLogManageDetele_49(self):
        '''批量删除日志信息'''

        peopleLogParam_49 = copy.deepcopy(RiChangBanGongPara.logManageObject) 
        peopleLogParam_49['mode']='add'
        peopleLogParam_49['isSubmit'] = 'true'
        peopleLogParam_49['peopleLog.isAttachment'] = 'peopleLog.isAttachment'
        peopleLogParam_49['peopleLog.belonger'] = '日志所属人%s'%CommonUtil.createRandomString()
        peopleLogParam_49['peopleLog.publishDate'] = Time.getCurrentDate()
        peopleLogParam_49['peopleLog.title'] ='日志标题%s'%CommonUtil.createRandomString()
        peopleLogParam_49['peopleLog.contents'] ='日志内容%s'%CommonUtil.createRandomString()
        responseDict = RiChangBanGongIntf.add_logManage(peopleLogParam_49, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '日志信息新增失败') 
        
        newLogParam_49 = copy.deepcopy(RiChangBanGongPara.logManageObject) 
        newLogParam_49['mode']='add'
        newLogParam_49['isSubmit'] = 'true'
        newLogParam_49['peopleLog.isAttachment'] = 'peopleLog.isAttachment'
        newLogParam_49['peopleLog.belonger'] = '日志所属人%s'%CommonUtil.createRandomString()
        newLogParam_49['peopleLog.publishDate'] = Time.getCurrentDate()
        newLogParam_49['peopleLog.title'] ='新增日志标题%s'%CommonUtil.createRandomString()
        newLogParam_49['peopleLog.contents'] ='日志内容%s'%CommonUtil.createRandomString()
        responseDict = RiChangBanGongIntf.add_logManage(newLogParam_49, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '日志信息新增失败') 
        
        deleteParam_49 = copy.deepcopy(RiChangBanGongPara.deleteLogManageDict)
        deleteParam_49['logIds'] = str(CommonIntf.getDbQueryResult(dbCommand = "select p.id from peopleLog p where p.title ='%s'" % (peopleLogParam_49['peopleLog.title'])))+','+str(CommonIntf.getDbQueryResult(dbCommand = "select p.id from peopleLog p where p.title ='%s'" % (newLogParam_49['peopleLog.title'])))
        responseDict = RiChangBanGongIntf.delete_logManage(deleteParam_49, username=userInit['DftSheQuUser'], password='11111111')
#         self.assertTrue(responseDict.result, '日志信息删除失败')       
                      
        param_49 = copy.deepcopy(RiChangBanGongPara.checkLogManageDict)
        param_49['title'] = peopleLogParam_49['peopleLog.title']
        ret = RiChangBanGongIntf.check_logManage(param_49, username=userInit['DftSheQuUser'], password='11111111')    
        self.assertFalse(ret, '删除的日志信息在列表中依然存在，删除失败') 
         
        param_49['title'] = newLogParam_49['peopleLog.title']
        ret = RiChangBanGongIntf.check_logManage(param_49, username=userInit['DftSheQuUser'], password='11111111')    
        self.assertFalse(ret, '删除的日志信息在列表中依然存在，删除失败')         
        
        pass 

    def testCommentManageSearch_50(self):
        '''搜素点评日志信息'''

        peopleLogParam_50 = copy.deepcopy(RiChangBanGongPara.logManageObject) 
        peopleLogParam_50['mode']='add'
        peopleLogParam_50['isSubmit'] = 'true'
        peopleLogParam_50['peopleLog.isAttachment'] = 'peopleLog.isAttachment'
        peopleLogParam_50['peopleLog.belonger'] = '日志所属人%s'%CommonUtil.createRandomString()
        peopleLogParam_50['peopleLog.publishDate'] = Time.getCurrentDate()
        peopleLogParam_50['peopleLog.title'] ='网格日志标题%s'%CommonUtil.createRandomString()
        peopleLogParam_50['peopleLog.contents'] ='日志内容%s'%CommonUtil.createRandomString()
        responseDict = RiChangBanGongIntf.add_logManage(peopleLogParam_50, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '日志信息新增失败')       
        
        newLogParam_50 = copy.deepcopy(RiChangBanGongPara.logManageObject) 
        newLogParam_50['mode']='add'
        newLogParam_50['isSubmit'] = 'true'
        newLogParam_50['peopleLog.isAttachment'] = 'peopleLog.isAttachment'
        newLogParam_50['peopleLog.belonger'] = '日志所属人%s'%CommonUtil.createRandomString()
        newLogParam_50['peopleLog.publishDate'] = Time.getCurrentDate()
        newLogParam_50['peopleLog.title'] ='新增网格日志标题%s'%CommonUtil.createRandomString()
        newLogParam_50['peopleLog.contents'] ='日志内容%s'%CommonUtil.createRandomString()
        responseDict = RiChangBanGongIntf.add_logManage(newLogParam_50, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '日志信息新增失败') 
        
        commentParam_50 = copy.deepcopy(RiChangBanGongPara.saveCommentDict)
        commentParam_50['logId'] = RiChangBanGongIntf.get_log_id_by_title(peopleLogParam_50['peopleLog.title'])#CommonIntf.getDbQueryResult(dbCommand = "select p.id from peopleLog p where p.title ='%s'" % (peopleLogParam_50['peopleLog.title']))
        commentParam_50['comment.comments'] = '点评内容'
        responseDict = RiChangBanGongIntf.comment_logManage(commentParam_50, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '日志信息点评失败')  
        
        newCommentParam_50 = copy.deepcopy(RiChangBanGongPara.saveCommentDict)
        newCommentParam_50['logId'] = RiChangBanGongIntf.get_log_id_by_title(newLogParam_50['peopleLog.title'])#CommonIntf.getDbQueryResult(dbCommand = "select p.id from peopleLog p where p.title ='%s'" % (newLogParam_50['peopleLog.title']))
        newCommentParam_50['comment.comments'] = '新增点评内容'
        responseDict = RiChangBanGongIntf.comment_logManage(newCommentParam_50, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '日志信息点评失败')      

        param_50 = copy.deepcopy(RiChangBanGongPara.searchLogManageDict)
        param_50['searchPeopleLogVo.title'] = peopleLogParam_50['peopleLog.title']
        ret = RiChangBanGongIntf.search_commentLog(param_50, username=userInit['DftSheQuUser'], password='11111111')    
        self.assertTrue(ret, '点评的日志信息搜索失败')         
        pass

    def testLogManageComment_51(self):
        '''点评日志信息'''

        peopleLogParam_51 = copy.deepcopy(RiChangBanGongPara.logManageObject) 
        peopleLogParam_51['mode']='add'
        peopleLogParam_51['isSubmit'] = 'true'
        peopleLogParam_51['peopleLog.isAttachment'] = 'peopleLog.isAttachment'
        peopleLogParam_51['peopleLog.belonger'] = '日志所属人%s'%CommonUtil.createRandomString()
        peopleLogParam_51['peopleLog.publishDate'] = Time.getCurrentDate()
        peopleLogParam_51['peopleLog.title'] ='网格新增日志标题%s'%CommonUtil.createRandomString()
        peopleLogParam_51['peopleLog.contents'] ='日志内容%s'%CommonUtil.createRandomString()
        responseDict = RiChangBanGongIntf.add_logManage(peopleLogParam_51, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '日志信息新增失败')       
        
        commentParam_51 = copy.deepcopy(RiChangBanGongPara.saveCommentDict)
        commentParam_51['logId'] = RiChangBanGongIntf.get_log_id_by_title(peopleLogParam_51['peopleLog.title'])#CommonIntf.getDbQueryResult(dbCommand = "select p.id from peopleLog p where p.title ='%s'" % (peopleLogParam_51['peopleLog.title']))
        commentParam_51['comment.comments'] = '点评内容'
        responseDict = RiChangBanGongIntf.comment_logManage(commentParam_51, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '日志信息点评失败')       

        param_51 = copy.deepcopy(RiChangBanGongPara.checkCommentManageDict)
        param_51['logId'] = commentParam_51['logId']
        param_51['comments'] = commentParam_51['comment.comments']
        ret = RiChangBanGongIntf.check_commentManage(param_51, username=userInit['DftSheQuUser'], password='11111111')    
        self.assertTrue(ret, '日志的点评情况检查失败')         
        pass

    def testCommentLogSearch_52(self):
        '''搜素下辖日志信息'''

        peopleLogParam_52 = copy.deepcopy(RiChangBanGongPara.logManageObject) 
        peopleLogParam_52['mode']='add'
        peopleLogParam_52['isSubmit'] = 'true'
        peopleLogParam_52['peopleLog.isAttachment'] = 'peopleLog.isAttachment'
        peopleLogParam_52['peopleLog.belonger'] = '日志所属人%s'%CommonUtil.createRandomString()
        peopleLogParam_52['peopleLog.publishDate'] = Time.getCurrentDate()
        peopleLogParam_52['peopleLog.title'] ='网格日志标题%s'%CommonUtil.createRandomString()
        peopleLogParam_52['peopleLog.contents'] ='日志内容%s'%CommonUtil.createRandomString()
        responseDict = RiChangBanGongIntf.add_logManage(peopleLogParam_52, username=userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(responseDict.result, '日志信息新增失败')       

        param_52 = copy.deepcopy(RiChangBanGongPara.searchLogManageDict)
        param_52['searchPeopleLogVo.isPeer'] = 'true'
        param_52['orgId'] = orgInit['DftSheQuOrgId']
        param_52['searchPeopleLogVo.title'] = peopleLogParam_52['peopleLog.title']
        ret = RiChangBanGongIntf.search_comment(param_52, username=userInit['DftSheQuUser'], password='11111111')    
        self.assertTrue(ret, '下辖日志信息搜索失败')         
        pass


#模块： 工作日志


    def testDailyLogAdd_53(self):
        '''新增工作日志信息'''

        workDiaryParam_53 = copy.deepcopy(RiChangBanGongPara.dailyObject) 
        workDiaryParam_53['mode']='add'
        workDiaryParam_53['workDiary.organization.id'] = orgInit['DftSheQuOrgId']
        workDiaryParam_53['workDiary.workUserName'] = userInit['DftSheQuUserXM']
        workDiaryParam_53['workDiary.diaryType.id'] = CommonIntf.getDbQueryResult(dbCommand ="select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '工作日志类型') and p.displayname = '其他'" )
        workDiaryParam_53['workDiary.workTime'] = Time.getCurrentDate()
        workDiaryParam_53['workDiary.workPlace'] ='地点%s'%CommonUtil.createRandomString()
        workDiaryParam_53['workDiary.workContent'] ='工作内容%s'%CommonUtil.createRandomString()
        responseDict = RiChangBanGongIntf.add_workDiary(workDiaryParam_53, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '工作日志信息新增失败')       
                      
        param_53 = copy.deepcopy(RiChangBanGongPara.checkDiaryDict)
        param_53['id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from workDiarys p where p.workPlace ='%s' and p.workContent ='%s'" % (workDiaryParam_53['workDiary.workPlace'],workDiaryParam_53['workDiary.workContent']))
        ret = RiChangBanGongIntf.check_workDiary(param_53, username=userInit['DftSheQuUser'], password='11111111')     
        self.assertTrue(ret, '工作日志信息检查失败') 
        
        pass 

    def testDailyLogDelete_54(self):
        '''批量删除工作日志信息'''

        workDiaryParam_54 = copy.deepcopy(RiChangBanGongPara.dailyObject) 
        workDiaryParam_54['mode']='add'
        workDiaryParam_54['workDiary.organization.id'] = orgInit['DftSheQuOrgId']
        workDiaryParam_54['workDiary.workUserName'] = userInit['DftSheQuUserXM']
        workDiaryParam_54['workDiary.diaryType.id'] = CommonIntf.getDbQueryResult(dbCommand ="select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '工作日志类型') and p.displayname = '其他'" )
        workDiaryParam_54['workDiary.workTime'] = Time.getCurrentDate()
        workDiaryParam_54['workDiary.workPlace'] ='地点%s'%CommonUtil.createRandomString()
        workDiaryParam_54['workDiary.workContent'] ='工作内容%s'%CommonUtil.createRandomString()
        responseDict = RiChangBanGongIntf.add_workDiary(workDiaryParam_54, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '工作日志信息新增失败')     
        
        newWorkDiaryParam_54 = copy.deepcopy(RiChangBanGongPara.dailyObject) 
        newWorkDiaryParam_54['mode']='add'
        newWorkDiaryParam_54['workDiary.organization.id'] = orgInit['DftSheQuOrgId']
        newWorkDiaryParam_54['workDiary.workUserName'] = userInit['DftSheQuUserXM']
        newWorkDiaryParam_54['workDiary.diaryType.id'] = CommonIntf.getDbQueryResult(dbCommand ="select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '工作日志类型') and p.displayname = '其他'" )
        newWorkDiaryParam_54['workDiary.workTime'] = Time.getCurrentDate()
        newWorkDiaryParam_54['workDiary.workPlace'] ='新增地点%s'%CommonUtil.createRandomString()
        newWorkDiaryParam_54['workDiary.workContent'] ='工作内容%s'%CommonUtil.createRandomString()
        responseDict = RiChangBanGongIntf.add_workDiary(newWorkDiaryParam_54, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '工作日志信息新增失败')  
                      
        deleteParam_54 = copy.deepcopy(RiChangBanGongPara.deleteObject)
        deleteParam_54['mode'] = 'delete'
        deleteParam_54['selectedIds'] = str(CommonIntf.getDbQueryResult(dbCommand = "select p.id from workDiarys p where p.workPlace ='%s' and p.workContent ='%s'" % (workDiaryParam_54['workDiary.workPlace'],workDiaryParam_54['workDiary.workContent'])))+','+str(CommonIntf.getDbQueryResult(dbCommand = "select p.id from workDiarys p where p.workPlace ='%s' and p.workContent ='%s'" % (newWorkDiaryParam_54['workDiary.workPlace'],newWorkDiaryParam_54['workDiary.workContent'])))
        ret = RiChangBanGongIntf.delete_workDiary(deleteParam_54, username=userInit['DftSheQuUser'], password='11111111')     
        self.assertTrue(ret, '工作日志信息删除失败') 
 
        param_54 = copy.deepcopy(RiChangBanGongPara.checkDiaryDict)
#         param_54['id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from workDiarys p where p.workPlace ='%s' and p.workContent ='%s'" % (workDiaryParam_54['workDiary.workPlace'],workDiaryParam_54['workDiary.workContent']))
        param_54['workPlace'] =  workDiaryParam_54['workDiary.workPlace']
        ret = RiChangBanGongIntf.check_workDiary(param_54, username=userInit['DftSheQuUser'], password='11111111')     
        self.assertFalse(ret, '列表中删除的工作日志信息仍然存在，删除失败') 

        param_54['workPlace'] =  newWorkDiaryParam_54['workDiary.workPlace']
        ret = RiChangBanGongIntf.check_workDiary(param_54, username=userInit['DftSheQuUser'], password='11111111')     
        self.assertFalse(ret, '列表中删除的工作日志信息仍然存在，删除失败') 
                        
        pass 

    def testDailyLogEdit_55(self):
        '''修改工作日志信息'''

        workDiaryParam_55 = copy.deepcopy(RiChangBanGongPara.dailyObject) 
        workDiaryParam_55['mode']='add'
        workDiaryParam_55['workDiary.organization.id'] = orgInit['DftSheQuOrgId']
        workDiaryParam_55['workDiary.workUserName'] = userInit['DftSheQuUserXM']
        workDiaryParam_55['workDiary.diaryType.id'] = CommonIntf.getDbQueryResult(dbCommand ="select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '工作日志类型') and p.displayname = '其他'" )
        workDiaryParam_55['workDiary.workTime'] = Time.getCurrentDate()
        workDiaryParam_55['workDiary.workPlace'] ='地点%s'%CommonUtil.createRandomString()
        workDiaryParam_55['workDiary.workContent'] ='工作内容%s'%CommonUtil.createRandomString()
        responseDict = RiChangBanGongIntf.add_workDiary(workDiaryParam_55, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '工作日志信息新增失败')     
        
        editWorkDiaryParam_55 = copy.deepcopy(RiChangBanGongPara.dailyObject) 
        editWorkDiaryParam_55['mode'] = 'edit'
        editWorkDiaryParam_55['workDiary.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from workDiarys p where p.workPlace ='%s' and p.workContent ='%s'" % (workDiaryParam_55['workDiary.workPlace'],workDiaryParam_55['workDiary.workContent']))
        editWorkDiaryParam_55['workDiary.organization.id'] = workDiaryParam_55['workDiary.organization.id']
        editWorkDiaryParam_55['workDiary.workUserName'] = workDiaryParam_55['workDiary.workUserName']
        editWorkDiaryParam_55['workDiary.diaryType.id'] = workDiaryParam_55['workDiary.diaryType.id']
        editWorkDiaryParam_55['workDiary.workTime'] = workDiaryParam_55['workDiary.workTime']
        editWorkDiaryParam_55['workDiary.workPlace'] ='修改地点%s'%CommonUtil.createRandomString()
        editWorkDiaryParam_55['workDiary.workContent'] ='修改工作内容%s'%CommonUtil.createRandomString()
        responseDict = RiChangBanGongIntf.edit_workDiary(editWorkDiaryParam_55, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '工作日志信息修改失败')  
                      
        param_55 = copy.deepcopy(RiChangBanGongPara.checkDiaryDict)
        param_55['id'] = editWorkDiaryParam_55['workDiary.id']
        ret = RiChangBanGongIntf.check_workDiary(param_55, username=userInit['DftSheQuUser'], password='11111111')     
        self.assertTrue(ret, '工作日志信息检查失败')         
        pass 
    def testDailyLogSearch_56(self):
        '''高级搜索工作日志信息'''

        workDiaryParam_56 = copy.deepcopy(RiChangBanGongPara.dailyObject) 
        workDiaryParam_56['mode']='add'
        workDiaryParam_56['workDiary.organization.id'] = orgInit['DftSheQuOrgId']
        workDiaryParam_56['workDiary.workUserName'] = userInit['DftSheQuUserXM']
        workDiaryParam_56['workDiary.diaryType.id'] = CommonIntf.getDbQueryResult(dbCommand ="select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '工作日志类型') and p.displayname = '其他'" )
        workDiaryParam_56['workDiary.workTime'] = Time.getCurrentDate()
        workDiaryParam_56['workDiary.workPlace'] ='地点%s'%CommonUtil.createRandomString()
        workDiaryParam_56['workDiary.workContent'] ='工作内容%s'%CommonUtil.createRandomString()
        responseDict = RiChangBanGongIntf.add_workDiary(workDiaryParam_56, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '工作日志信息新增失败')     
        
        newWorkDiaryParam_56 = copy.deepcopy(RiChangBanGongPara.dailyObject) 
        newWorkDiaryParam_56['mode']='add'
        newWorkDiaryParam_56['workDiary.organization.id'] = orgInit['DftSheQuOrgId']
        newWorkDiaryParam_56['workDiary.workUserName'] = userInit['DftSheQuUserXM']
        newWorkDiaryParam_56['workDiary.diaryType.id'] = CommonIntf.getDbQueryResult(dbCommand ="select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '工作日志类型') and p.displayname = '其他'" )
        newWorkDiaryParam_56['workDiary.workTime'] = Time.getCurrentDate()
        newWorkDiaryParam_56['workDiary.workPlace'] ='新增地点%s'%CommonUtil.createRandomString()
        newWorkDiaryParam_56['workDiary.workContent'] ='工作内容%s'%CommonUtil.createRandomString()
        responseDict = RiChangBanGongIntf.add_workDiary(newWorkDiaryParam_56, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(responseDict.result, '工作日志信息新增失败')  
                      
        searchParam_56 = copy.deepcopy(RiChangBanGongPara.checkDiaryDict)
        searchParam_56['id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from workDiarys p where p.workPlace ='%s' and p.workContent ='%s'" % (workDiaryParam_56['workDiary.workPlace'],workDiaryParam_56['workDiary.workContent']))
        searchParam_56['workPlace'] = workDiaryParam_56['workDiary.workPlace']
        ret = RiChangBanGongIntf.search_workDiary(searchParam_56, orgId=orgInit['DftSheQuOrgId'],diaryType=workDiaryParam_56['workDiary.diaryType.id'],username=userInit['DftSheQuUser'], password='11111111')     
        self.assertTrue(ret, '工作日志信息搜索失败') 
                        
        pass     
    
    def tearDown(self):
        pass
    
if __name__ == "__main__":
    suite = unittest.TestSuite()
    
#我的台账
#     suite.addTest(RiChangBanGong("testHuiYiJiLuAdd_17"))
#     suite.addTest(RiChangBanGong("testWenJianJiLuAdd_17"))
#     suite.addTest(RiChangBanGong("testHuoDongJiLuAdd_17"))
#     suite.addTest(RiChangBanGong("testQiTaJiLuAdd_17"))
#     
#     suite.addTest(RiChangBanGong("testHuiYiJiLuEdit_18"))   
#     suite.addTest(RiChangBanGong("testWenJianJiLuEdit_18"))    
#     suite.addTest(RiChangBanGong("testHuoDongJiLuEdit_18"))    
#     suite.addTest(RiChangBanGong("testQiTaJiLuEdit_18"))     
#   
#     suite.addTest(RiChangBanGong("testHuiYiJiLuDelete_19")) 
#     suite.addTest(RiChangBanGong("testWenJianJiLuDelete_19")) 
#     suite.addTest(RiChangBanGong("testHuoDongJiLuDelete_19")) 
#     suite.addTest(RiChangBanGong("testQiTaJiLuDelete_19")) 
#   
#     suite.addTest(RiChangBanGong("testHuiYiJiLuTransfer_20")) 
#     suite.addTest(RiChangBanGong("testWenJianJiLuTransfer_20")) 
#     suite.addTest(RiChangBanGong("testHuoDongJiLuTransfer_20")) 
#     suite.addTest(RiChangBanGong("testQiTaJiLuTransfer_20")) 
#  
#     suite.addTest(RiChangBanGong("testHuiYiJiLuCopy_22")) 
#     suite.addTest(RiChangBanGong("testWenJianJiLuCopy_22")) 
#     suite.addTest(RiChangBanGong("testHuoDongJiLuCopy_22")) 
#     suite.addTest(RiChangBanGong("testQiTaJiLuCopy_22")) 
#  
#     suite.addTest(RiChangBanGong("testFaLvFaGuiAdd_25")) 
#     suite.addTest(RiChangBanGong("testFaLvFaGuiEdit_26")) 
#     suite.addTest(RiChangBanGong("testFaLvFaGuiSearch_27")) 
#     suite.addTest(RiChangBanGong("testFaLvFaGuiDelete_28")) 
#     suite.addTest(RiChangBanGong("testFaLvFaGuiShare_29")) 
#     suite.addTest(RiChangBanGong("testFaLvFaGuiShareCancel_30")) 
#  
#     suite.addTest(RiChangBanGong("testFaWenAdd_31")) 
#     suite.addTest(RiChangBanGong("testFaWenSearch_32")) 
#     suite.addTest(RiChangBanGong("testFaWenEdit_33")) 
#     suite.addTest(RiChangBanGong("testFaWenDelete_34")) 
#     suite.addTest(RiChangBanGong("testFaWenEditAgain_35")) 
#     suite.addTest(RiChangBanGong("testFaWenSynchToMyProfile_36")) 
#     suite.addTest(RiChangBanGong("testFaWenSynchToWorkingRecord_37"))  
#     suite.addTest(RiChangBanGong("testFaWenSend_38"))  
#     suite.addTest(RiChangBanGong("testFaWenWithdraw_39"))  
#     suite.addTest(RiChangBanGong("testShouWenSearch_40"))  
#     suite.addTest(RiChangBanGong("testFaWenReceive_41"))  
#     suite.addTest(RiChangBanGong("testFaWenRead_42"))   
#     suite.addTest(RiChangBanGong("testFaWenTransmit_43"))   
#     suite.addTest(RiChangBanGong("testShouWenDelete_44"))
#     suite.addTest(RiChangBanGong("testGongWenSearch_45")) 
#    
#     suite.addTest(RiChangBanGong("testLogManageAdd_46"))  
#     suite.addTest(RiChangBanGong("testLogManageEdit_47"))  
#     suite.addTest(RiChangBanGong("testLogManageSearch_48"))  
#     suite.addTest(RiChangBanGong("testLogManageDetele_49"))  
#     suite.addTest(RiChangBanGong("testCommentManageSearch_50"))
#     suite.addTest(RiChangBanGong("testLogManageComment_51"))
#     suite.addTest(RiChangBanGong("testCommentLogSearch_52"))
#   
#     suite.addTest(RiChangBanGong("testDailyLogAdd_53"))
#     suite.addTest(RiChangBanGong("testDailyLogDelete_54"))
#     suite.addTest(RiChangBanGong("testDailyLogEdit_55"))
 
    suite.addTest(RiChangBanGong("testConflictRpt_009"))  

    results = unittest.TextTestRunner().run(suite)
    pass
