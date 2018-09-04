# -*- coding:UTF-8 -*-
'''
Created on 2016-2-29

@author: N-286
'''
from __future__ import unicode_literals
from COMMON import Log, Time, CommonUtil
from COMMON.CommonUtil import createRandomString
from COMMON.Time import setLinuxTime, getCurrentTime, getCurrentDateAndTime, \
    moveTime, getLinuxDateAndTime, TimeMoveType, getCurrentDate, moveTime2
from CONFIG import InitDefaultPara
from CONFIG.Global import RenZhengZhongXinUrl, RenZhengZhongXinAppServRootPass, \
    simulationEnvironment
from CONFIG.InitDefaultPara import userInit, orgInit
from Interface.PingAnJianShe.Common import CommonIntf
from Interface.PingAnJianShe.Common.CommonIntf import getDbQueryResult
from Interface.PingAnJianShe.RiChangBanGong.RiChangBanGongIntf import runJob
from Interface.PingAnJianShe.ShiJianChuLi import ShiJianChuLiPara
from Interface.PingAnJianShe.ShiJianChuLi.ShiJianChuLiIntf import \
    setJobDelayTime, addIssue, dealIssue, clearTable, deleteAllIssues2
from Interface.PingAnJianShe.ShiJianChuLi.ShiJianChuLiPara import issueObject2
from Interface.PingAnJianShe.ShiYouFangWu import ShiYouFangWuPara, \
    ShiYouFangWuIntf
from Interface.PingAnJianShe.ShiYouRenKou import ShiYouRenKouPara, \
    ShiYouRenKouIntf
from Interface.PingAnJianShe.ShiYouRenKou.ShiYouRenKouIntf import \
    deleteAllPopulation
from Interface.PingAnJianShe.SystemMgr import SystemMgrIntf
from Interface.PingAnJianShe.XiaQuGuanLi import XiaQuGuanLiIntf
from Interface.PingAnJianShe.YanPanFenXi.YanPanFenXiIntf import \
    YanPanFenXiInitEnv, checkDictInDictlist, viewOrgInfo, updateOrgInfo, \
    addJieDaoFuncUser, runJobNow, pinganjianshe_LogOut, checkOrgLogin, \
    deleteAllHouseholdStaff, deleteAllMembers, deleteSafetyProduction, \
    deleteServiceRecords, checkDictInMobileGrid, checkDictInActualPopulationStatics, \
    checkDictInActualHouseStatics, checkDictInImportantPlaceStatics, \
    checkDictInImportantPopulationStatics
from Interface.PingAnJianShe.YanPanFenXi.YanPanFenXiPara import \
    zongXiangFenXiJianCha, zongXiangFenXiJianCha2, quShiJianCha, leiXingFenBuJianCha
from Interface.PingAnJianShe.ZuZhiChangSuo import ZuZhiChangSuoPara, \
    ZuZhiChangSuoIntf
from Interface.PingAnJianShe.pingAnJianSheHttpCommon import pinganjianshe_login
from Interface.PingAnTong.RenKouXinXi import RenKouXinXiPara, RenKouXinXiIntf
from Interface.PingAnTong.ShiJianChuLi.MbShiJianChuLiIntf import mAddIssue
from Interface.PingAnTong.ShiJianChuLi.MbShiJianChuLiPara import issueAddPara1
from Interface.PingAnTong.pingAnTongHttpCommon import pingantong_login
from Interface.YunWeiPingTai.YunWeiCommon.YunWeiCommonIntf import \
    setLinuxTimeYunWei
import copy
import json
import time
import unittest
from Interface.PingAnJianShe.YanPanFenXi import YanPanFenXiPara, YanPanFenXiIntf

#仿真环境下不可用
class YanPanFenXi(unittest.TestCase):
    
    def setUp(self):
        #如果是仿真环境，则不执行初始环境操作，避免误操作
        if simulationEnvironment is False:
            SystemMgrIntf.initEnv()
            YanPanFenXiInitEnv()
        pass
    
    '''
    @功能：研判分析-综合信息查询-登录统计-行政部门登录统计
    @ chenhui 2016-4-22
    '''
    def testStatus_001(self):
        '''登录统计-行政部门登录统计'''
        #仿真环境下跳过测试
        if simulationEnvironment is True:
            pass
        else:
            #设置linux时间为2015-12-28
            try:
                data='2016-2-1 '+getCurrentTime()
                #注意''中的空格不可少
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用登录接口')
                pinganjianshe_login(userName=userInit['DftJieDaoUser'],passWord='11111111')
    #             pinganjianshe_LogOut()
                data='2016-2-8 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用登录接口')
                pinganjianshe_login(userName=userInit['DftJieDaoUser'],passWord='11111111')
    #             pinganjianshe_LogOut()
                data='2016-2-9 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用登录接口')
                pinganjianshe_login(userName=userInit['DftJieDaoUser'],passWord='11111111')
    #             pinganjianshe_LogOut()
                data='2016-2-15 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用登录接口')
                pinganjianshe_login(userName=userInit['DftJieDaoUser'],passWord='11111111')
    #             pinganjianshe_LogOut()
                data='2016-2-16 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用登录接口')
                pinganjianshe_login(userName=userInit['DftJieDaoUser'],passWord='11111111')
    #             pinganjianshe_LogOut()
                data='2016-2-17 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用登录接口')
                pinganjianshe_login(userName=userInit['DftJieDaoUser'],passWord='11111111')
    #             pinganjianshe_LogOut()
                data='2016-2-22 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用登录接口')
                pinganjianshe_login(userName=userInit['DftJieDaoUser'],passWord='11111111')
                data='2016-2-23 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用登录接口')
                pinganjianshe_login(userName=userInit['DftJieDaoUser'],passWord='11111111')
                data='2016-2-24 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用登录接口')
                pinganjianshe_login(userName=userInit['DftJieDaoUser'],passWord='11111111')
                data='2016-2-25 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用登录接口')
                pinganjianshe_login(userName=userInit['DftJieDaoUser'],passWord='11111111')
    #             pinganjianshe_LogOut()
                #系统时间改为3月份，再跑job，
                data='2016-03-02 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                #立即执行job
                para={
                 'task.name':'orgLoginStanalsJob',
                 'job.name':'OrgLoginStateRecover'
                 }
                result0=runJobNow(jobPara=para)
                self.assertTrue(result0,'job运行成功')
                viewPara={
                    'nowYear':'2016',
                    'nowMonth':2,
                    'orgId':orgInit['DftQuOrgId'],
                    'peopleCenterType':0,
                    'internalId':0,     
                          }
                checkPara={
                    'loggedday_month':10,
                    'loggedday_week1':1,
                    'loggedday_week2':2,
                    'loggedday_week3':3,
                    'loggedday_week4':4,
                    'orgName':orgInit['DftJieDaoOrg'],
                           }
                url='/statAnalyse/orgLoginStanalsManager/findOrgLoginStanalsByOrgIdForListPage.action'
                result1=checkOrgLogin(checkpara=checkPara,listpara=viewPara,url=url)
                self.assertTrue(result1, '行政部门登录统计验证失败')
                Log.LogOutput(message='行政部门登录统计验证通过！')            
            finally:
                #将服务器时间改回正确时间
                setLinuxTime(data=getCurrentDateAndTime())
                setLinuxTimeYunWei(data=getCurrentDateAndTime(),password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
            pass
    
    '''
    @功能：研判分析-综合信息查询-登录统计-职能部门登录统计
    @ chenhui 2016-4-22
    '''
    def testStatus_002(self):
        '''登录统计-职能部门登录统计'''
        #仿真环境下跳过测试
        if simulationEnvironment is True:
            pass
        else:
            #设置linux时间为2015-12-28
            try:
                data='2016-2-1 '+getCurrentTime()
                #注意''中的空格不可少
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用登录接口')
                pinganjianshe_login(userName=userInit['DftJieDaoFuncUser'],passWord='11111111')
    #             pinganjianshe_LogOut()
                data='2016-2-8 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用登录接口')
                pinganjianshe_login(userName=userInit['DftJieDaoFuncUser'],passWord='11111111')
    #             pinganjianshe_LogOut()
                data='2016-2-9 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用登录接口')
                pinganjianshe_login(userName=userInit['DftJieDaoFuncUser'],passWord='11111111')
    #             pinganjianshe_LogOut()
                data='2016-2-15 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用登录接口')
                pinganjianshe_login(userName=userInit['DftJieDaoFuncUser'],passWord='11111111')
    #             pinganjianshe_LogOut()
                data='2016-2-16 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用登录接口')
                pinganjianshe_login(userName=userInit['DftJieDaoFuncUser'],passWord='11111111')
    #             pinganjianshe_LogOut()
                data='2016-2-17 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用登录接口')
                pinganjianshe_login(userName=userInit['DftJieDaoFuncUser'],passWord='11111111')
    #             pinganjianshe_LogOut()
                data='2016-2-22 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用登录接口')
                Time.wait(1)
                pinganjianshe_login(userName=userInit['DftJieDaoFuncUser'],passWord='11111111')
                data='2016-2-23 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用登录接口')
                Time.wait(1)
                pinganjianshe_login(userName=userInit['DftJieDaoFuncUser'],passWord='11111111')
                data='2016-2-24 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用登录接口')
                Time.wait(1)
                pinganjianshe_login(userName=userInit['DftJieDaoFuncUser'],passWord='11111111')
                data='2016-2-25 '+getCurrentTime()
                Time.wait(1)
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用登录接口')
                pinganjianshe_login(userName=userInit['DftJieDaoFuncUser'],passWord='11111111')
    #             pinganjianshe_LogOut()
                #系统时间改为3月份，再跑job，
                data='2016-03-02 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Time.wait(1)
                #立即执行job
                para={
                 'task.name':'orgLoginStanalsJob',
                 'job.name':'OrgLoginStateRecover'
                 }
                result0=runJobNow(jobPara=para)
                self.assertTrue(result0,'job运行成功')
                viewPara={
                    'nowYear':'2016',
                    'nowMonth':2,
                    'orgId':orgInit['DftJieDaoOrgId'],
                    'peopleCenterType':0,
                    'internalId':1,     
                          }
                checkPara={
                    'loggedday_month':10,
                    'loggedday_week1':1,
                    'loggedday_week2':2,
                    'loggedday_week3':3,
                    'loggedday_week4':4,
                    'orgName':orgInit['DftJieDaoFuncOrg'],
                           }
                url='/statAnalyse/orgLoginStanalsManager/findOrgLoginStanalsByOrgIdForListPage.action'
                result1=checkOrgLogin(checkpara=checkPara,listpara=viewPara,url=url)
                self.assertTrue(result1, '职能部门登录统计验证失败')
                Log.LogOutput(message='职能部门登录统计验证通过！')            
            finally:
                #将服务器时间改回正确时间
                setLinuxTime(data=getCurrentDateAndTime())
                setLinuxTimeYunWei(data=getCurrentDateAndTime(),password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
            pass    
    
    '''
    @功能：研判分析-综合信息查询-登录统计-区民办中心登录统计
    @ chenhui 2016-4-22
    '''
    def testStatus_003(self):
        '''登录统计-区民办中心登录统计'''
        #仿真环境下跳过测试
        if simulationEnvironment is True:
            pass
        else:
            #设置linux时间为2015-12-28
            try:
                data='2016-2-1 '+getCurrentTime()
                #注意''中的空格不可少
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用登录接口')
                Time.wait(1)
                pinganjianshe_login(userName=userInit['DftQuMinBanFuncUser'],passWord='11111111')
    #             pinganjianshe_LogOut()
                data='2016-2-8 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用登录接口')
                Time.wait(1)
                pinganjianshe_login(userName=userInit['DftQuMinBanFuncUser'],passWord='11111111')
    #             pinganjianshe_LogOut()
                data='2016-2-9 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用登录接口')
                Time.wait(1)
                pinganjianshe_login(userName=userInit['DftQuMinBanFuncUser'],passWord='11111111')
    #             pinganjianshe_LogOut()
                data='2016-2-15 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用登录接口')
                Time.wait(1)
                pinganjianshe_login(userName=userInit['DftQuMinBanFuncUser'],passWord='11111111')
    #             pinganjianshe_LogOut()
                data='2016-2-16 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用登录接口')
                Time.wait(1)
                pinganjianshe_login(userName=userInit['DftQuMinBanFuncUser'],passWord='11111111')
    #             pinganjianshe_LogOut()
                data='2016-2-17 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用登录接口')
                Time.wait(1)
                pinganjianshe_login(userName=userInit['DftQuMinBanFuncUser'],passWord='11111111')
    #             pinganjianshe_LogOut()
                data='2016-2-22 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用登录接口')
                Time.wait(1)
                pinganjianshe_login(userName=userInit['DftQuMinBanFuncUser'],passWord='11111111')
                data='2016-2-23 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用登录接口')
                Time.wait(1)
                pinganjianshe_login(userName=userInit['DftQuMinBanFuncUser'],passWord='11111111')
                data='2016-2-24 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用登录接口')
                Time.wait(1)
                pinganjianshe_login(userName=userInit['DftQuMinBanFuncUser'],passWord='11111111')
                data='2016-2-25 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用登录接口')
                Time.wait(1)
                pinganjianshe_login(userName=userInit['DftQuMinBanFuncUser'],passWord='11111111')
    #             pinganjianshe_LogOut()
                #系统时间改为3月份，再跑job，
                data='2016-03-02 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                #立即执行job
                para={
                 'task.name':'orgLoginStanalsJob',
                 'job.name':'OrgLoginStateRecover'
                 }
                result0=runJobNow(jobPara=para)
                self.assertTrue(result0,'job运行成功')
                viewPara={
                    'nowYear':'2016',
                    'nowMonth':2,
                    'orgId':orgInit['DftQuOrgId'],
                    'peopleCenterType':1,
                    'internalId':1,     
                          }
                checkPara={
                    'loggedday_month':10,
                    'loggedday_week1':1,
                    'loggedday_week2':2,
                    'loggedday_week3':3,
                    'loggedday_week4':4,
                    'orgName':orgInit['DftQuMinBanFuncOrg']
                           }
                url='/statAnalyse/orgLoginStanalsManager/findOrgLoginStanalsByOrgIdForListPage.action'
                result1=checkOrgLogin(checkpara=checkPara,listpara=viewPara,url=url)
                self.assertTrue(result1, '区民办中心登录统计验证失败')
                Log.LogOutput(message='区民办中心登录统计验证通过！')            
            finally:
                #将服务器时间改回正确时间
                setLinuxTime(data=getCurrentDateAndTime())
                setLinuxTimeYunWei(data=getCurrentDateAndTime(),password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
            pass    

    '''
    @功能：研判分析-综合信息查询-登录统计-个人账号登录统计
    这个job默认只在浙江省下执行
    @ chenhui 2016-4-22
    '''
    def testStatus_004(self):
        '''登录统计-个人账号登录统计'''
        #仿真环境下跳过测试
        if simulationEnvironment is True:
            pass
        else:
            #设置linux时间为2015-12-28
            try:
                #第一周
                data='2016-2-1 '+getCurrentTime()
                #注意''中的空格不可少
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用PC登录接口')
                Time.wait(1)
                pinganjianshe_login(userName=userInit['DftJieDaoFuncUser'],passWord='11111111')
    #             pinganjianshe_LogOut()
                #第二周，手机登录
                data='2016-2-8 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用手机登录接口')
                Time.wait(1)
                pingantong_login(userName=userInit['DftJieDaoFuncUser'],passWord='11111111')
    #             pinganjianshe_LogOut()
                data='2016-2-9 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用手机登录接口')
                Time.wait(1)
                pingantong_login(userName=userInit['DftJieDaoFuncUser'],passWord='11111111')
    #             pinganjianshe_LogOut()
                #第三周
                data='2016-2-15 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用PC登录接口')
                Time.wait(1)
                pinganjianshe_login(userName=userInit['DftJieDaoFuncUser'],passWord='11111111')
    #             pinganjianshe_LogOut()
                data='2016-2-16 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用PC和手机登录接口')
                Time.wait(1)
                pinganjianshe_login(userName=userInit['DftJieDaoFuncUser'],passWord='11111111')
                pingantong_login(userName=userInit['DftJieDaoFuncUser'],passWord='11111111')
                 
    #             pinganjianshe_LogOut()
                data='2016-2-17 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用手机登录接口')
                Time.wait(1)
                pingantong_login(userName=userInit['DftJieDaoFuncUser'],passWord='11111111')
    #             pinganjianshe_LogOut()
                #第四周
                data='2016-2-22 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用PC和手机登录接口')
                Time.wait(1)
                pinganjianshe_login(userName=userInit['DftJieDaoFuncUser'],passWord='11111111')
                pingantong_login(userName=userInit['DftJieDaoFuncUser'],passWord='11111111')
                data='2016-2-23 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用PC和手机登录接口')
                Time.wait(1)
                pinganjianshe_login(userName=userInit['DftJieDaoFuncUser'],passWord='11111111')
                pingantong_login(userName=userInit['DftJieDaoFuncUser'],passWord='11111111')
                data='2016-2-24 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用PC和手机登录接口')
                Time.wait(1)
                pinganjianshe_login(userName=userInit['DftJieDaoFuncUser'],passWord='11111111')
                pingantong_login(userName=userInit['DftJieDaoFuncUser'],passWord='11111111')
                data='2016-2-25 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用PC和手机登录接口')
                Time.wait(1)
                pinganjianshe_login(userName=userInit['DftJieDaoFuncUser'],passWord='11111111')
                pingantong_login(userName=userInit['DftJieDaoFuncUser'],passWord='11111111')
    #             pinganjianshe_LogOut()
                #系统时间改为3月份，再跑job，
                data='2016-02-29 23:30:30'+getCurrentTime()
                #该job是统计当月的数据。。。
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                #立即执行job
                para={
                 'task.name':'accountLoginStanalsJob',
                 'job.name':'AccountLoginStateRecover'
                 }
                result0=runJobNow(jobPara=para)
                self.assertTrue(result0,'job运行成功')
                viewPara={
                    'nowYear':2016,
                    'nowMonth':2,
                    'orgId':orgInit['DftJieDaoOrgId'],
                    'displayLevel':'directJurisdiction',
                    'loginMode':'PCmobile',    
                          }
                checkPara1={
                    'loggedday_month':10,
                    'loggedday_week1':1,
                    'loggedday_week2':2,
                    'loggedday_week3':3,
                    'loggedday_week4':4,
                    'month':2,
                    'year':2016
                           }
    #             time.sleep(20)
                url='/account/accountLoginStatisAnalying/searchAccounLoginStanalstList.action'
                result1=checkOrgLogin(checkpara=checkPara1,listpara=viewPara,url=url)
                result1=checkOrgLogin(checkpara=checkPara1,listpara=viewPara,url=url)
                self.assertTrue(result1, '个人账号PC和手机登录统计验证失败')
                Log.LogOutput(message='个人账号PC和手机登录统计验证通过！')
                #仅PC
                checkPara2={
                    'loggedday_month':7,
                    'loggedday_week1':1,
                    'loggedday_week2':0,
                    'loggedday_week3':2,
                    'loggedday_week4':4,
                    'month':2,
                    'year':2016
                           }
                viewPara['loginMode']='PC'
                result2=checkOrgLogin(checkpara=checkPara2,listpara=viewPara,url=url)
                self.assertTrue(result2, '个人账号PC登录统计验证失败')
                Log.LogOutput(message='个人账号PC登录统计验证通过！')
                #仅手机
                checkPara3={
                    'loggedday_month':8,
                    'loggedday_week1':0,
                    'loggedday_week2':2,
                    'loggedday_week3':2,
                    'loggedday_week4':4,
                    'month':2,
                    'year':2016
                           }
                viewPara['loginMode']='mobile'
                result3=checkOrgLogin(checkpara=checkPara3,listpara=viewPara,url=url)
                self.assertTrue(result3, '个人账号仅手机登录统计验证失败')
                Log.LogOutput(message='个人账号仅手机登录统计验证通过！')                                     
            finally:
                #将服务器时间改回正确时间
                setLinuxTime(data=getCurrentDateAndTime())
                setLinuxTimeYunWei(data=getCurrentDateAndTime(),password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
            pass


    '''
    @功能：研判分析-综合信息查询-登录统计-个人账号登录统计
    @ chenhui 2016-4-22
    '''
    def testStatus_005(self):
        '''登录统计-个人账号登录统计'''
        #仿真环境下跳过测试
        if simulationEnvironment is True:
            pass
        else:
            #设置linux时间为2015-12-28
            try:
                #第一周
                data='2016-2-1 '+getCurrentTime()
                #注意''中的空格不可少
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用PC登录接口')
                pinganjianshe_login(userName=userInit['DftJieDaoFuncUser'],passWord='11111111')
    #             pinganjianshe_LogOut()
                #第二周，手机登录
                data='2016-2-8 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用手机登录接口')
                pingantong_login(userName=userInit['DftJieDaoFuncUser'],passWord='11111111')
    #             pinganjianshe_LogOut()
                data='2016-2-9 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用手机登录接口')
                pingantong_login(userName=userInit['DftJieDaoFuncUser'],passWord='11111111')
    #             pinganjianshe_LogOut()
                #第三周
                data='2016-2-15 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用PC登录接口')
                pinganjianshe_login(userName=userInit['DftJieDaoFuncUser'],passWord='11111111')
    #             pinganjianshe_LogOut()
                data='2016-2-16 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用PC和手机登录接口')
                pinganjianshe_login(userName=userInit['DftJieDaoFuncUser'],passWord='11111111')
                pingantong_login(userName=userInit['DftJieDaoFuncUser'],passWord='11111111')
                 
    #             pinganjianshe_LogOut()
                data='2016-2-17 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用手机登录接口')
                pingantong_login(userName=userInit['DftJieDaoFuncUser'],passWord='11111111')
    #             pinganjianshe_LogOut()
                #第四周
                data='2016-2-22 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用PC和手机登录接口')
                pinganjianshe_login(userName=userInit['DftJieDaoFuncUser'],passWord='11111111')
                pingantong_login(userName=userInit['DftJieDaoFuncUser'],passWord='11111111')
                data='2016-2-23 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用PC和手机登录接口')
                pinganjianshe_login(userName=userInit['DftJieDaoFuncUser'],passWord='11111111')
                pingantong_login(userName=userInit['DftJieDaoFuncUser'],passWord='11111111')
                data='2016-2-24 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用PC和手机登录接口')
                pinganjianshe_login(userName=userInit['DftJieDaoFuncUser'],passWord='11111111')
                pingantong_login(userName=userInit['DftJieDaoFuncUser'],passWord='11111111')
                data='2016-2-25 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                Log.LogOutput( message='调用PC和手机登录接口')
                pinganjianshe_login(userName=userInit['DftJieDaoFuncUser'],passWord='11111111')
                pingantong_login(userName=userInit['DftJieDaoFuncUser'],passWord='11111111')
    #             pinganjianshe_LogOut()
                #系统时间改为2016-2-29，再跑job，
                data='2016-02-29 '+getCurrentTime()
                #该job是统计当月的数据。。。
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                #立即执行job
                para={
                 'task.name':'accountLoginStanalsJob',
                 'job.name':'AccountLoginStateRecover'
                 }
                result0=runJobNow(jobPara=para)
                self.assertTrue(result0,'job运行成功')
                viewPara={
                    'nowYear':2016,
                    'nowMonth':2,
                    'orgId':orgInit['DftJieDaoOrgId'],
                    'displayLevel':'directJurisdiction',
                    'loginMode':'PCmobile',    
                          }
                checkPara1={
                    'loggedday_month':10,
                    'loggedday_week1':1,
                    'loggedday_week2':2,
                    'loggedday_week3':3,
                    'loggedday_week4':4,
                    'month':2,
                    'year':2016
                           }
    #             time.sleep(20)
                url='/account/accountLoginStatisAnalying/searchAccounLoginStanalstList.action'
                result1=checkOrgLogin(checkpara=checkPara1,listpara=viewPara,url=url)
    #             result1=checkOrgLogin(checkpara=checkPara1,listpara=viewPara,url=url)
                self.assertTrue(result1, '个人账号PC和手机登录统计验证失败')
                Log.LogOutput(message='个人账号PC和手机登录统计验证通过！')
                #仅PC
                checkPara2={
                    'loggedday_month':7,
                    'loggedday_week1':1,
                    'loggedday_week2':0,
                    'loggedday_week3':2,
                    'loggedday_week4':4,
                    'month':2,
                    'year':2016
                           }
                viewPara['loginMode']='PC'
                result2=checkOrgLogin(checkpara=checkPara2,listpara=viewPara,url=url)
                self.assertTrue(result2, '个人账号PC登录统计验证失败')
                Log.LogOutput(message='个人账号PC登录统计验证通过！')
                #仅手机
                checkPara3={
                    'loggedday_month':8,
                    'loggedday_week1':0,
                    'loggedday_week2':2,
                    'loggedday_week3':2,
                    'loggedday_week4':4,
                    'month':2,
                    'year':2016
                           }
                viewPara['loginMode']='mobile'
                result3=checkOrgLogin(checkpara=checkPara3,listpara=viewPara,url=url)
                self.assertTrue(result3, '个人账号仅手机登录统计验证失败')
                Log.LogOutput(message='个人账号仅手机登录统计验证通过！')                                     
            finally:
                pass
                #将服务器时间改回正确时间
                setLinuxTime(data=getCurrentDateAndTime())
                setLinuxTimeYunWei(data=getCurrentDateAndTime(),password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
            pass
    
          
    '''
    @功能：研判分析-网格员手机应用                        *系统存在bug，登录与未登录自相矛盾
    @ chenhui 2016-4-26
    '''
#     def testStatus_006(self):
#         '''综合信息查询-网格员手机应用'''
#         #仿真环境下跳过测试
#         if simulationEnvironment is True:
#             pass
#         else:
#             try:
#                 deleteAllHouseholdStaff()
#                 deleteAllMembers()
#                 deleteSafetyProduction()
#                 deleteServiceRecords()
#                 clearTable(tableName='gridmobilestatisticinfo')
#                 Data='2016-1-6 '+getCurrentTime()
#                 setLinuxTime(Data)
#                 setLinuxTimeYunWei(Data=Data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
#                 ###添加测试数据
#                 #网格一调用手机接口登录
#                 Log.LogOutput( message='调用手机登录接口')
#                 pingantong_login(userName=userInit['DftWangGeUser'],passWord='11111111')
#                 #网格二调用PC接口登录
#                 Log.LogOutput( message='调用PC登录接口')
#                 pinganjianshe_login(userName=userInit['DftWangGeUser1'],passWord='11111111')            
#                 #网格一调用手机接口新增户籍人口、服务记录
#                 HuJiParam = copy.deepcopy(RenKouXinXiPara.populationObject) 
#                 HuJiParam['tqmobile'] = 'true'
#                 HuJiParam['orgId'] = orgInit['DftWangGeOrgId']
#                 HuJiParam['householdStaff.name'] ='户籍人口新增服务记录搜索测试%s'%CommonUtil.createRandomString() 
#                 HuJiParam['householdStaff.organization.id'] = orgInit['DftWangGeOrgId']
#                 HuJiParam['householdStaff.idCardNo'] = '330000195501040028'   #性别根据身份证来确定，如何获取？
#                 HuJiParam['householdStaff.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='女')
#                 HuJiParam['householdStaff.maritalState.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '未婚'")   #婚姻状况
#                 HuJiParam['householdStaff.schooling.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '博士'")  #文化程度
#                 HuJiParam['householdStaff.politicalBackground.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '中国共产党党员'")  #政治面貌   
#                 HuJiParam['householdStaff.nation.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '汉族'")  #民族
#                 HuJiParam['householdStaff.province'] = '浙江省'  #户籍地址省
#                 HuJiParam['householdStaff.city'] = '杭州市'  #户籍地址市
#                 HuJiParam['householdStaff.district'] = '西湖区'  #户籍地址县
#                 HuJiParam['householdStaff.houseAddress'] = "%s%s%s" % (HuJiParam['householdStaff.province'],HuJiParam['householdStaff.city'],HuJiParam['householdStaff.district'])
#                 HuJiParam['householdStaff.isHaveHouse'] = 'false'  #有无住所:true/false
#                 HuJiParam['householdStaff.noHouseReason'] = '无住所原因%s'%CommonUtil.createRandomString()  #false:无住所原因
#         
#                 #户籍信息
#                 HuJiParam['householdStaff.accountNumber'] = '01'
#                 HuJiParam['householdStaff.relationShipWithHead.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '本人'")
#                 HuJiParam['householdStaff.residentStatus.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '人户同在'")
#                 responseDict = RenKouXinXiIntf.add_HuJi(HuJiRenKouDict=HuJiParam, username=userInit['DftWangGeUser'], password='11111111')
#                 self.assertTrue(responseDict.result, '新增户籍人口失败') 
#         
#                 #新增服务成员
#                 fuWuParam = copy.deepcopy(ShiYouRenKouPara.fuWuRenYuanDict)      
#                 fuWuParam['serviceTeamMemberBase.org.id'] = orgInit['DftWangGeOrgId']
#                 fuWuParam['serviceTeamMemberBase.name'] = '服务1%s'%CommonUtil.createRandomString()
#                 fuWuParam['serviceTeamMemberBase.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别(男、女)', displayName='男')     
#                 fuWuParam['serviceTeamMemberBase.mobile'] = '13000000001'
#                 responseDict = ShiYouRenKouIntf.add_FuWuChengYuan(fuWuDict=fuWuParam, username=userInit['DftWangGeUser'], password='11111111')
#                 self.assertTrue(responseDict.result, '新增成员失败') 
#         
#                 #新增服务记录1
#                 serviceParam = copy.deepcopy(RenKouXinXiPara.serviceRecordObject) 
#                 serviceParam['tqmobile'] = 'true'
#                 serviceParam['serviceRecord.userOrgId'] = orgInit['DftWangGeOrgId']
#                 serviceParam['serviceRecord.serviceJoiners'] = '服务参与者1'  #选填
#                 serviceParam['serviceRecord.teamId'] = '0'
#                 serviceParam['serviceRecord.occurDate'] = Time.getCurrentDate()
#                 serviceParam['serviceRecord.serviceObjects'] = "%s-%s-householdStaff" % (CommonIntf.getDbQueryResult(dbCommand = "select t.id from householdstaffs t where t.idcardno='%s' and t.name='%s'" % (HuJiParam['householdStaff.idCardNo'],HuJiParam['householdStaff.name'])),HuJiParam['householdStaff.name'])
#                 serviceParam['serviceRecord.organization.id'] = orgInit['DftWangGeOrgId']
#                 serviceParam['serviceRecord.serviceContent'] = '服务内容1%s'%CommonUtil.createRandomString()   #选填
#                 serviceParam['serviceRecord.serviceMembers'] = "%s-%s-0" % (CommonIntf.getDbQueryResult(dbCommand = "select t.id from Serviceteammemberbase t where t.name='%s'" % (fuWuParam['serviceTeamMemberBase.name'])),fuWuParam['serviceTeamMemberBase.name'])
#                 serviceParam['serviceRecord.occurPlace'] = '服务地点1%s'%CommonUtil.createRandomString() 
#                 responseDict = RenKouXinXiIntf.add_serviceRecord(serviceParam, username=userInit['DftWangGeUser'], password='11111111')
#                 self.assertTrue(responseDict.result, '新增户籍人口的服务记录失败')              
#                 #网格一调用手机接口新增一条事件
#                 para = copy.deepcopy(issueAddPara1) 
#                 para['issueNew.occurDate']='2016-1-1'
#                 result=mAddIssue(para=para,username = userInit['DftWangGeUser'])
#                 self.assertTrue(result.result,'新增失败')
#                 
#                 #网格二调用PC接口新增场所、服务记录
#     #         新增服务成员
#                 Premise_Param = copy.deepcopy(ZuZhiChangSuoPara.FuWuChengYuanObject) 
#                 Premise_Param['serviceTeamMemberBase.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
#                 Premise_Param['serviceTeamMemberBase.job'] = '测试职位3'
#                 Premise_Param['serviceTeamMemberBase.name'] = '测试服务成员'
#                 Premise_Param['isSubmit'] = 'true'
#                 Premise_Param['serviceTeamMemberBase.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别(男、女)', displayName='男')
#                 Premise_Param['serviceTeamMemberBase.mobile'] = '13011111111'
#                 responseDict = ZuZhiChangSuoIntf.addFuWuChengYuan(FuWuChengYuanDict=Premise_Param, username=InitDefaultPara.userInit['DftWangGeUser1'], password='11111111')
#                 self.assertTrue(responseDict.result, '新增失败')
#                 #新增安全生产重点
#                 testCase_Param = copy.deepcopy(ZuZhiChangSuoPara.addAnQuanShengChan) 
#                 testCase_Param['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId1']
#                 testCase_Param['enterprise.name'] = '测试安全生产重点'+CommonUtil.createRandomString()
#                 testCase_Param['enterprise.keyType'] = 'safetyProductionKey'
#                 testCase_Param['mode'] = 'add'
#                 testCase_Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg1']
#                 testCase_Param['placeTypeName'] = '安全生产重点'
#                 testCase_Param['enterprise.address'] = '测试地址1'
#                 testCase_Param['enterprise.legalPerson'] = '法人代表1'
#                 testCase_Param['enterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='企业类型', displayName='规上企业')
#                 responseDict = ZuZhiChangSuoIntf.addAnQuanShengChan(AnQuanShengChanDict=testCase_Param, username=InitDefaultPara.userInit['DftWangGeUser1'], password='11111111')
#                 self.assertTrue(responseDict.result, '新增失败') 
#                         
#         #         新增巡场记录
#                 ZZCSCase_Param = copy.deepcopy(ZuZhiChangSuoPara.XunChangQingKuangObject) 
#                 ZZCSCase_Param['serviceRecord.organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId1']
#                 ZZCSCase_Param['serviceRecord.recordType'] = '1'
#                 ZZCSCase_Param['mode'] = 'add'
#                 ZZCSCase_Param['isSubmit'] = 'true'
#                 ZZCSCase_Param['serviceRecord.teamId']='0'
#                 ZZCSCase_Param['serviceRecord.userOrgId'] = InitDefaultPara.orgInit['DftWangGeOrgId1']
#                 ZZCSCase_Param['serviceRecord.occurDate'] = Time.getCurrentDate()
#                 ZZCSCase_Param['serviceRecord.occurPlace'] = '服务地点'+CommonUtil.createRandomString()
#                 ZZCSCase_Param['serviceRecord.serviceMembers'] = '%s-测试服务成员-0'%CommonIntf.getDbQueryResult(dbCommand = "select t.id from SERVICETEAMMEMBERBASE t where t.name='测试服务成员'")
#                 ZZCSCase_Param['serviceRecord.serviceObjects'] = '%s-测试安全生产重点-SAFETYPRODUCTIONKEY'%CommonIntf.getDbQueryResult(dbCommand = "select t.id from enterprises t where t.name='%s' and t.keytype='safetyProductionKey'"%testCase_Param['enterprise.name'])
#                 responseDict = ZuZhiChangSuoIntf.addXunChangQingKuang(XunChangQingKuangDict=ZZCSCase_Param, username=InitDefaultPara.userInit['DftWangGeUser1'], password='11111111')
#     
#                 #更改时间为2016-2-6，执行登录统计job和网格员手机应用job
#                 Data='2016-2-6 '+getCurrentTime()
#                 setLinuxTime(Data)
#                 setLinuxTimeYunWei(Data=Data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
#                 
#                 para1={
#                  'task.name':'accountLoginStanalsJob',
#                  'job.name':'AccountLoginStateRecover'
#                  }
#                 result1=runJobNow(jobPara=para1)
#                 self.assertTrue(result1,'job运行成功')
#     
#                 para2={
#                  'task.name':'gridMobileStatisticJob',
#                  'job.name':'GridMobileStatisticJob'
#                  }
#                 result2=runJobNow(jobPara=para2)
#                 self.assertTrue(result2,'job运行成功')
#                             
#                 #######验证新增数据统计正确性
#                 checkPara1={
#                     'gridCount':1,#网格数
#                     'hasMobileGridCount':1,#开通手机的网格数
#                     'hasMLGridCount':1,#有登录的网格数
#                     'noMLGridCount':0,#未登录的网格数
#                     'hasIBIGridCount':1,#有录入基础信息的网格数
#                     'hasISRGridCount':1,#有录入服务记录的网格数
#                     'hasIIGridCount':1,#有录入事件的网格数
#                     'noInputDataCount':0,#无数据录入的网格数
#                     'orgName':'测试自动化网格'    
#                            }
#                 listPara={
#                     'mobileStatisticVo.orgId':orgInit['DftSheQuOrgId'],
#                     'mobileStatisticVo.startYear':'2016',
#                     'mobileStatisticVo.endYear':'2016',
#                     'mobileStatisticVo.startMonth':'1',
#                     'mobileStatisticVo.endMonth':'1'
#                           }
#                 result1=checkDictInMobileGrid(checkpara=checkPara1,listpara=listPara)
#                 self.assertTrue(result1, '测试自动化网格网格员手机应用统计错误')
#                 #验证测试自动化网格1统计数据
#                 checkPara2={
#                     'gridCount':1,#网格数
#                     'hasMobileGridCount':1,#开通手机的网格数
#                     'hasMLGridCount':0,#有登录的网格数
#                     'noMLGridCount':1,#未登录的网格数
#                     'hasIBIGridCount':0,#有录入基础信息的网格数
#                     'hasISRGridCount':0,#有录入服务记录的网格数
#                     'hasIIGridCount':0,#有录入事件的网格数
#                     'noInputDataCount':1,#无数据录入的网格数
#                     'orgName':'测试自动化网格1'             
#                             }
#                 result2=checkDictInMobileGrid(checkpara=checkPara2,listpara=listPara)
#                 self.assertTrue(result2, '测试自动化网格1网格员手机应用统计错误')
#                 Log.LogOutput(message='网格员手机应用统计成功')
#             finally:
#                 #将服务器时间改回正确时间
#                 setLinuxTime(Data=getCurrentDateAndTime())
#                 setLinuxTimeYunWei(Data=getCurrentDateAndTime(),password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
#             pass

    '''
    @功能：研判分析-事件多维分析-横向数量统计（职能）            *系统存在bug
    @ chenhui 2016-4-19
    '''
#     def testStatus_007(self):
#         '''事件多维分析-横向数量统计(职能)'''
#         #有bug
#         #仿真环境下跳过测试
#         if simulationEnvironment is True:
#             pass
#         else:
#             #清除事件
#             deleteAllIssues2()
#             #设置测试自动化街道职能部门的上级职能部门为测试自动化区职能部门
#             para={'orgId':orgInit['DftJieDaoFuncOrgId']}
#             resDict=viewOrgInfo(para=para)
#             updPara={
#                     'organization.id':para['orgId'],
#                     'organization.orgName':resDict['orgName'],
#                     'organization.contactWay':'0571-11111111',
#                     'organization.orgType.id':resDict['orgType']['id'],
#                     'organization.parentFunOrg.id':orgInit['DftQuFuncOrgId'],
#                     'organization.orgLevel.id':resDict['orgLevel']['id'],
#                     'organization.functionalOrgType.id':resDict['functionalOrgType']['id'],
#                     'organization.departmentNo':resDict['departmentNo'],
#                     'organization.remark':''
#                      }
#             result=updateOrgInfo(para=updPara)
#             self.assertTrue(result.result, '修改部门失败')
#             try:
#                 Data='2015-6-6 '+getCurrentTime()
#                 setLinuxTime(Data)
#                 setLinuxTimeYunWei(Data=Data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
#                 issueParam = copy.deepcopy(issueObject2) 
#                 issueParam['issue.occurDate']= Data
#                 rs=addIssue(issueDict=issueParam,username=userInit['DftJieDaoFuncUser'])
#                 #上报给区职能部门，设置上报参数
#                 sIssuePara=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)        
#                 sIssuePara['operation.dealOrg.id']=orgInit['DftJieDaoFuncOrgId']
#                 sIssuePara['operation.issue.id']=rs['issueId']
#                 sIssuePara['keyId']=rs['issueStepId']      
#                 sIssuePara['operation.dealUserName']=userInit['DftJieDaoFuncUserXM']
#                 sIssuePara['operation.mobile']=userInit['DftJieDaoFuncUserSJ']
#                 sIssuePara['operation.content']='上报事件'
#                 sIssuePara['operation.targeOrg.id']=orgInit['DftQuFuncOrgId']
#                 sIssuePara['themainOrgid']=orgInit['DftQuFuncOrgId']        
#                 sIssuePara['dealCode']='41'#上报
#                 #上报
#                 result=dealIssue(issueDict=sIssuePara,username=userInit['DftJieDaoFuncUser'])
#                 self.assertTrue(result.result, '事件上报失败')
#                 #区职能部门受理
#                 sIssuePara2={
#                          'operation.dealOrg.id':orgInit['DftQuFuncOrgId'],
#                          'operation.issue.id':sIssuePara['operation.issue.id'],
#                          'operation.dealUserName':userInit['DftQuFuncUserXM'],
#                          'operation.mobile':userInit['DftQuFuncUserSJ'],
#                          'dealCode':'61',
#                          'keyId':sIssuePara['keyId']+1
#                          }
#                 result2=dealIssue(issueDict=sIssuePara2,username=userInit['DftQuFuncUser'])
#                 self.assertTrue(result2.result,'区职能部门受理失败！')
#                 #区职能部门办结
#                 sIssuePara3=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)        
#                 sIssuePara3['operation.dealOrg.id']=orgInit['DftQuFuncOrgId']
#                 sIssuePara3['operation.issue.id']=rs['issueId']
#                 sIssuePara3['keyId']=sIssuePara['keyId']+1
#                 sIssuePara3['operation.dealUserName']=userInit['DftQuFuncUserXM']
#                 sIssuePara3['operation.mobile']=userInit['DftQuFuncUserSJ']
#                 sIssuePara3['operation.content']='事件处理'       
#                 sIssuePara3['dealCode']='31'#办结
#                 result3=dealIssue(issueDict=sIssuePara3, username=userInit['DftQuFuncUser'], password='11111111')
#                 self.assertTrue(result3.result, '办结失败')
#                 ######将时间改为29天前
#                 Data=moveTime(standardTime=getCurrentDateAndTime(),addDay=29,moveType=TimeMoveType.MINUS)
#                 setLinuxTime(Data)
#                 setLinuxTimeYunWei(Data=Data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
#                 issueParam['issue.occurDate']= Data
#                 issueParam['selectedTypes']=getDbQueryResult(dbCommand="select id from issuetypes i where i.domainid=(select id from issuetypedomains where module='core' and domainName='治安、安全隐患') and i.issuetypename='安全生产'"),
#                 rs=addIssue(issueDict=issueParam,username=userInit['DftJieDaoFuncUser'])
#                 #上报给区职能部门，设置上报参数
#                 sIssuePara['operation.issue.id']=rs['issueId']
#                 sIssuePara['keyId']=rs['issueStepId']      
#                 #上报
#                 result=dealIssue(issueDict=sIssuePara,username=userInit['DftJieDaoFuncUser'])
#                 self.assertTrue(result.result, '事件上报失败')
#                 #区职能部门受理
#                 sIssuePara2['operation.issue.id']=sIssuePara['operation.issue.id']
#                 sIssuePara2['keyId']=sIssuePara['keyId']+1
#                 result2=dealIssue(issueDict=sIssuePara2,username=userInit['DftQuFuncUser'])
#                 self.assertTrue(result2.result,'区职能部门受理失败！')
#                 #区职能部门办结
#                 sIssuePara3['operation.issue.id']=rs['issueId']
#                 sIssuePara3['keyId']=sIssuePara['keyId']+1
#                 result3=dealIssue(issueDict=sIssuePara3, username=userInit['DftQuFuncUser'], password='11111111')
#                 self.assertTrue(result3.result, '办结失败')
#                 ######将时间改为6天前
#                 Data=moveTime(standardTime=getCurrentDateAndTime(),addDay=6,moveType=TimeMoveType.MINUS)
#                 setLinuxTime(Data)
#                 setLinuxTimeYunWei(Data=Data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
#                 issueParam['issue.occurDate']= Data
#                 issueParam['selectedTypes']=getDbQueryResult(dbCommand="select id from issuetypes i where i.domainid=(select id from issuetypedomains where module='core' and domainName='民生服务') and i.issuetypename='医疗卫生'"),
#                 rs=addIssue(issueDict=issueParam,username=userInit['DftJieDaoFuncUser'])
#                 #上报给区职能部门，设置上报参数
#                 sIssuePara['operation.issue.id']=rs['issueId']
#                 sIssuePara['keyId']=rs['issueStepId']      
#                 #上报
#                 result=dealIssue(issueDict=sIssuePara,username=userInit['DftJieDaoFuncUser'])
#                 self.assertTrue(result.result, '事件上报失败')
#                 #区职能部门受理
#                 sIssuePara2['operation.issue.id']=sIssuePara['operation.issue.id']
#                 sIssuePara2['keyId']=sIssuePara['keyId']+1
#                 result2=dealIssue(issueDict=sIssuePara2,username=userInit['DftQuFuncUser'])
#                 self.assertTrue(result2.result,'区职能部门受理失败！')
#                 #区职能部门办结
#                 sIssuePara3['operation.issue.id']=rs['issueId']
#                 sIssuePara3['keyId']=sIssuePara['keyId']+1
#                 result3=dealIssue(issueDict=sIssuePara3, username=userInit['DftQuFuncUser'], password='11111111')
#                 self.assertTrue(result3.result, '办结失败')
#                 #####将时间改回今天
#                 setLinuxTime(Data=getCurrentDateAndTime())
#                 setLinuxTimeYunWei(Data=getCurrentDateAndTime(),password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
#                 issueParam['issue.occurDate']= '2016-1-6'
#                 issueParam['selectedTypes']=getDbQueryResult(dbCommand="select id from issuetypes i where i.domainid=(select id from issuetypedomains where module='core' and domainName='其他') and i.issuetypename='其他'"),
#                 rs=addIssue(issueDict=issueParam,username=userInit['DftJieDaoFuncUser'])
#                 #上报给区职能部门，设置上报参数
#                 sIssuePara['operation.issue.id']=rs['issueId']
#                 sIssuePara['keyId']=rs['issueStepId']      
#                 #上报
#                 result=dealIssue(issueDict=sIssuePara,username=userInit['DftJieDaoFuncUser'])
#                 self.assertTrue(result.result, '事件上报失败')
#                 #区职能部门受理
#                 sIssuePara2['operation.issue.id']=sIssuePara['operation.issue.id']
#                 sIssuePara2['keyId']=sIssuePara['keyId']+1
#                 result2=dealIssue(issueDict=sIssuePara2,username=userInit['DftQuFuncUser'])
#                 self.assertTrue(result2.result,'区职能部门受理失败！')
#                 #区职能部门办结
#                 sIssuePara3['operation.issue.id']=rs['issueId']
#                 sIssuePara3['keyId']=sIssuePara['keyId']+1
#                 result3=dealIssue(issueDict=sIssuePara3, username=userInit['DftQuFuncUser'], password='11111111')
#                 self.assertTrue(result3.result, '办结失败')
#                 #######验证新增数据统计正确性
#                 #当天统计数据
#                 viewPara1={
#                         'issueAnalyzeDto.orgId':orgInit['DftJieDaoOrgId'],
#                         'issueAnalyzeDto.status':'1',
#                         'issueAnalyzeDto.beginDate':getCurrentDate(),
#                         'issueAnalyzeDto.endDate':moveTime2(standardTime=getCurrentDateAndTime(),addDay=1,moveType=TimeMoveType.PLUS),
#                         'viewType':'2',
#                         '_search':'false',
#                         'rows':'1000',
#                         'page':'1',
#                         'sidx':'id',
#                         'sord':'desc'
#                            }
#                 #自动化街道数据
#                 checkPara11={
#                         'orgName':orgInit['DftJieDaoFuncOrg'],
#                         'conflictNumber':0,
#                         'otherNumber':1,
#                         'securityNumber':0,
#                         'serviceNumber':0,
#                         'totalNumber':1
#                            }
#                 #合计数据
#                 checkPara12={
#                         'orgName':'合计',
#                         'conflictNumber':0,
#                         'otherNumber':1,
#                         'securityNumber':0,
#                         'serviceNumber':0,
#                         'totalNumber':1                         
#                              }
#                 url='/analyzing/issueAnalyzeManage/statisticalIssueAnalyze.action'
#                 result11=checkDictInDictlist(checkpara=checkPara11,listpara=viewPara1,url=url)
#                 self.assertTrue(result11, '自动化区职能部门当天新增数据验证失败')
#                 result12=checkDictInDictlist(checkpara=checkPara12,listpara=viewPara1,url=url)
#                 self.assertTrue(result12, '合计当天新增数据验证失败')
#                 Log.LogOutput( message='当天新增数据验证成功!')
#                 #最近七天
#                 beginDate=moveTime2(standardTime=getCurrentDateAndTime(),addDay=6)
#                 endDate=moveTime2(standardTime=getCurrentDateAndTime(),addDay=1,moveType=TimeMoveType.PLUS)
#                 viewPara1['issueAnalyzeDto.beginDate']=beginDate
#                 viewPara1['issueAnalyzeDto.endDate']=endDate
#                 checkPara11['serviceNumber']=1
#                 checkPara11['totalNumber']=2
#                 checkPara12['serviceNumber']=1
#                 checkPara12['totalNumber']=2
#                 result11=checkDictInDictlist(checkpara=checkPara11,listpara=viewPara1,url=url)
#                 self.assertTrue(result11, '自动化区职能部门七天内新增数据验证失败')
#                 result12=checkDictInDictlist(checkpara=checkPara12,listpara=viewPara1,url=url)
#                 self.assertTrue(result12, '合计七天内新增数据验证失败')
#                 Log.LogOutput( message='七天内新增数据验证成功!')
#                 #最近30天
#                 beginDate=moveTime2(standardTime=getCurrentDateAndTime(),addDay=29)
#                 viewPara1['issueAnalyzeDto.beginDate']=beginDate
#                 checkPara11['securityNumber']=1
#                 checkPara11['totalNumber']=3
#                 checkPara12['securityNumber']=1
#                 checkPara12['totalNumber']=3
#                 result11=checkDictInDictlist(checkpara=checkPara11,listpara=viewPara1,url=url)
#                 self.assertTrue(result11, '自动化区职能部门30天内新增数据验证失败')
#                 result12=checkDictInDictlist(checkpara=checkPara12,listpara=viewPara1,url=url)
#                 self.assertTrue(result12, '合计30天内新增数据验证失败')
#                 Log.LogOutput( message='30天内新增数据验证成功!')
#                 #自定义时间，2015年1月1日至今
#                 viewPara1['issueAnalyzeDto.beginDate']='2015-1-1'
#                 checkPara11['conflictNumber']=1
#                 checkPara11['totalNumber']=4
#                 checkPara12['conflictNumber']=1
#                 checkPara12['totalNumber']=4
#                 result11=checkDictInDictlist(checkpara=checkPara11,listpara=viewPara1,url=url)
#                 self.assertTrue(result11, '自动化区职能部门2015-1-1至今新增数据验证失败')
#                 result12=checkDictInDictlist(checkpara=checkPara12,listpara=viewPara1,url=url)
#                 self.assertTrue(result12, '合计2015-1-1至今新增数据验证失败')
#                 Log.LogOutput( message='2015-1-1至今新增数据验证成功!')
#                 ######验证办理数据统计
#                 viewPara2={
#                         'issueAnalyzeDto.orgId':orgInit['DftJieDaoOrgId'],
#                         'issueAnalyzeDto.status':'2',
#                         'issueAnalyzeDto.beginDate':getCurrentDate(),
#                         'issueAnalyzeDto.endDate':moveTime2(standardTime=getCurrentDateAndTime(),addDay=1,moveType=TimeMoveType.PLUS),
#                         'viewType':'2',
#                         '_search':'false',
#                         'rows':'1000',
#                         'page':'1',
#                         'sidx':'id',
#                         'sord':'desc'
#                            }
#                 #自动化街道数据
#                 checkPara21={
#                         'orgName':orgInit['DftJieDaoFuncOrg'],
#                         'conflictNumber':0,
#                         'otherNumber':1,
#                         'securityNumber':0,
#                         'serviceNumber':0,
#                         'totalNumber':1
#                            }
#                 #合计数据
#                 checkPara22={
#                         'orgName':'合计',
#                         'conflictNumber':0,
#                         'otherNumber':1,
#                         'securityNumber':0,
#                         'serviceNumber':0,
#                         'totalNumber':1                        
#                              }
#                 result21=checkDictInDictlist(checkpara=checkPara21,listpara=viewPara2,url=url)
#                 self.assertTrue(result21, '自动化街道职能部门当天办理数据验证失败')
#                 result22=checkDictInDictlist(checkpara=checkPara22,listpara=viewPara2,url=url)
#                 self.assertTrue(result22, '合计当天办理数据验证失败')
#                 Log.LogOutput( message='当天办理数据验证成功!')
#                 #最近七天
#                 beginDate=moveTime2(standardTime=getCurrentDateAndTime(),addDay=6)
#                 viewPara2['issueAnalyzeDto.beginDate']=beginDate
#                 checkPara21['serviceNumber']=1
#                 checkPara21['totalNumber']=2
#                 checkPara22['serviceNumber']=1
#                 checkPara22['totalNumber']=2
#                 result21=checkDictInDictlist(checkpara=checkPara21,listpara=viewPara2,url=url)
#                 self.assertTrue(result21, '自动化街道职能部门七天内办理数据验证失败')
#                 result22=checkDictInDictlist(checkpara=checkPara22,listpara=viewPara2,url=url)
#                 self.assertTrue(result22, '合计七天内办理数据验证失败')
#                 Log.LogOutput( message='七天内办理数据验证成功!')
#                 #最近30天
#                 beginDate=moveTime2(standardTime=getCurrentDateAndTime(),addDay=29)
#                 viewPara2['issueAnalyzeDto.beginDate']=beginDate
#                 checkPara21['securityNumber']=1
#                 checkPara21['totalNumber']=3
#                 checkPara22['securityNumber']=1
#                 checkPara22['totalNumber']=3
#                 result21=checkDictInDictlist(checkpara=checkPara21,listpara=viewPara2,url=url)
#                 self.assertTrue(result21, '自动化街道职能部门30天内办理数据验证失败')
#                 result22=checkDictInDictlist(checkpara=checkPara22,listpara=viewPara2,url=url)
#                 self.assertTrue(result22, '合计30天内办理数据验证失败')
#                 Log.LogOutput( message='30天内办理数据验证成功!')
#                 #自定义时间，2015年1月1日至今
#                 viewPara2['issueAnalyzeDto.beginDate']='2015-1-1'
#                 checkPara21['conflictNumber']=1
#                 checkPara21['totalNumber']=4
#                 checkPara22['conflictNumber']=1
#                 checkPara22['totalNumber']=4
#                 result21=checkDictInDictlist(checkpara=checkPara21,listpara=viewPara2,url=url)
#                 self.assertTrue(result21, '自动化街道职能部门2015-1-1至今办理数据验证失败')
#                 result22=checkDictInDictlist(checkpara=checkPara22,listpara=viewPara2,url=url)
#                 self.assertTrue(result22, '合计2015-1-1至今办理数据验证失败')
#                 Log.LogOutput( message='2015-1-1至今办理数据验证成功!')
#                 ######验证办结数据统计
#                 viewPara3={
#                         'issueAnalyzeDto.orgId':orgInit['DftQuOrgId'],
#                         'issueAnalyzeDto.status':'3',
#                         'issueAnalyzeDto.beginDate':getCurrentDate(),
#                         'issueAnalyzeDto.endDate':moveTime2(standardTime=getCurrentDateAndTime(),addDay=1,moveType=TimeMoveType.PLUS),
#                         'viewType':'2',
#                         '_search':'false',
#                         'rows':'1000',
#                         'page':'1',
#                         'sidx':'id',
#                         'sord':'desc'
#                            }
#                 #自动化区职能部门数据
#                 checkPara31={
#                         'orgName':orgInit['DftQuFuncOrg'],
#                         'conflictNumber':0,
#                         'otherNumber':1,
#                         'securityNumber':0,
#                         'serviceNumber':0,
#                         'totalNumber':1
#                            }
#                 #合计数据
#                 checkPara32={
#                         'orgName':'合计',
#                         'conflictNumber':0,
#                         'otherNumber':1,
#                         'securityNumber':0,
#                         'serviceNumber':0,
#                         'totalNumber':1                        
#                              }
#                 result31=checkDictInDictlist(checkpara=checkPara31,listpara=viewPara3,url=url)
#                 self.assertTrue(result31, '自动化区职能部门当天办结数据验证失败')
#                 result32=checkDictInDictlist(checkpara=checkPara32,listpara=viewPara3,url=url)
#                 self.assertTrue(result32, '合计当天办结数据验证失败')
#                 Log.LogOutput( message='当天办结数据验证成功!')
#                 #最近七天
#                 beginDate=moveTime2(standardTime=getCurrentDateAndTime(),addDay=6)
#                 viewPara3['issueAnalyzeDto.beginDate']=beginDate
#                 checkPara31['serviceNumber']=1
#                 checkPara31['totalNumber']=2
#                 checkPara32['serviceNumber']=1
#                 checkPara32['totalNumber']=2
#                 result31=checkDictInDictlist(checkpara=checkPara31,listpara=viewPara3,url=url)
#                 self.assertTrue(result31, '自动化区职能部门七天内办结数据验证失败')
#                 result32=checkDictInDictlist(checkpara=checkPara32,listpara=viewPara3,url=url)
#                 self.assertTrue(result32, '合计七天内办结数据验证失败')
#                 Log.LogOutput( message='七天内办结数据验证成功!')
#                 #最近30天
#                 beginDate=moveTime2(standardTime=getCurrentDateAndTime(),addDay=29)
#                 viewPara3['issueAnalyzeDto.beginDate']=beginDate
#                 checkPara31['securityNumber']=1
#                 checkPara31['totalNumber']=3
#                 checkPara32['securityNumber']=1
#                 checkPara32['totalNumber']=3
#                 result31=checkDictInDictlist(checkpara=checkPara31,listpara=viewPara3,url=url)
#                 self.assertTrue(result31, '自动化区职能部门30天内办结数据验证失败')
#                 result32=checkDictInDictlist(checkpara=checkPara32,listpara=viewPara3,url=url)
#                 self.assertTrue(result32, '合计30天内办结数据验证失败')
#                 Log.LogOutput( message='30天内办结数据验证成功!')
#                 #自定义时间，2015年1月1日至今
#                 viewPara3['issueAnalyzeDto.beginDate']='2015-1-1'
#                 checkPara31['conflictNumber']=1
#                 checkPara31['totalNumber']=4
#                 checkPara32['conflictNumber']=1
#                 checkPara32['totalNumber']=4
#                 result31=checkDictInDictlist(checkpara=checkPara31,listpara=viewPara3,url=url)
#                 self.assertTrue(result31, '自动化区职能部门2015-1-1至今办结数据验证失败')
#                 result32=checkDictInDictlist(checkpara=checkPara32,listpara=viewPara3,url=url)
#                 self.assertTrue(result32, '合计2015-1-1至今办结数据验证失败')
#                 Log.LogOutput( message='2015-1-1至今办结数据验证成功!')            
#             finally:
#                 #将服务器时间改回正确时间
#                 setLinuxTime(Data=getCurrentDateAndTime())
#                 setLinuxTimeYunWei(Data=getCurrentDateAndTime(),password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
#             pass
    
    '''
    @功能：研判分析-事件多维分析-横向数量统计（民办中心）
    @ chenhui 2016-4-20
    '''
    def testStatus_008(self):
        '''事件多维分析-横向数量统计(民办中心)'''
        #仿真环境下跳过测试
        if simulationEnvironment is True:
            pass
        else:
            #清除事件
            deleteAllIssues2()
            #设置测试自动化街道职能部门的上级职能部门为测试自动化区民办中心
            para={'orgId':orgInit['DftJieDaoFuncOrgId']}
            resDict=viewOrgInfo(para=para)
            updPara={
                    'organization.id':para['orgId'],
                    'organization.orgName':resDict['orgName'],
                    'organization.contactWay':'0571-11111111',
                    'organization.orgType.id':resDict['orgType']['id'],
                    'organization.parentFunOrg.id':orgInit['DftQuMinBanFuncOrgId'],
                    'organization.orgLevel.id':resDict['orgLevel']['id'],
                    'organization.functionalOrgType.id':resDict['functionalOrgType']['id'],
                    'organization.departmentNo':resDict['departmentNo'],
                    'organization.remark':''
                     }
            result=updateOrgInfo(para=updPara)
            self.assertTrue(result.result, '修改部门失败')
            try:
                data='2015-6-6 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                issueParam = copy.deepcopy(issueObject2) 
                issueParam['issue.occurDate']= data  
                rs=addIssue(issueDict=issueParam,username=userInit['DftJieDaoFuncUser'])
                #上报给区职能部门，设置上报参数
                sIssuePara=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)        
                sIssuePara['operation.dealOrg.id']=orgInit['DftJieDaoFuncOrgId']
                sIssuePara['operation.issue.id']=rs['issueId']
                sIssuePara['keyId']=rs['issueStepId']      
                sIssuePara['operation.dealUserName']=userInit['DftJieDaoFuncUserXM']
                sIssuePara['operation.mobile']=userInit['DftJieDaoFuncUserSJ']
                sIssuePara['operation.content']='上报事件'
                sIssuePara['operation.targeOrg.id']=orgInit['DftQuMinBanFuncOrgId']
                sIssuePara['themainOrgid']=orgInit['DftQuMinBanFuncOrgId']        
                sIssuePara['dealCode']='41'#上报
                #上报
                result=dealIssue(issueDict=sIssuePara,username=userInit['DftJieDaoFuncUser'])
                self.assertTrue(result.result, '事件上报失败')
                #区民办中心部门受理
                sIssuePara2={
                         'operation.dealOrg.id':orgInit['DftQuMinBanFuncOrgId'],
                         'operation.issue.id':sIssuePara['operation.issue.id'],
                         'operation.dealUserName':userInit['DftQuMinBanFuncUserXM'],
                         'operation.mobile':userInit['DftQuMinBanFuncUserSJ'],
                         'dealCode':'61',
                         'keyId':sIssuePara['keyId']+1
                         }
                result2=dealIssue(issueDict=sIssuePara2,username=userInit['DftQuMinBanFuncUser'])
                self.assertTrue(result2.result,'区职能部门受理失败！')
                #区职能部门办结
                sIssuePara3=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)        
                sIssuePara3['operation.dealOrg.id']=orgInit['DftQuMinBanFuncOrgId']
                sIssuePara3['operation.issue.id']=rs['issueId']
                sIssuePara3['keyId']=sIssuePara['keyId']+1
                sIssuePara3['operation.dealUserName']=userInit['DftQuMinBanFuncUserXM']
                sIssuePara3['operation.mobile']=userInit['DftQuMinBanFuncUserSJ']
                sIssuePara3['operation.content']='事件处理'       
                sIssuePara3['dealCode']='31'#办结
                result3=dealIssue(issueDict=sIssuePara3, username=userInit['DftQuMinBanFuncUser'], password='11111111')
                self.assertTrue(result3.result, '办结失败')
                ######将时间改为29天前
                data=moveTime(standardTime=getCurrentDateAndTime(),addDay=29,moveType=TimeMoveType.MINUS)
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                issueParam['issue.occurDate']= data
                issueParam['selectedTypes']=getDbQueryResult(dbCommand="select id from issuetypes i where i.domainid=(select id from issuetypedomains where module='core' and domainName='治安、安全隐患') and i.issuetypename='安全生产'"),
                rs=addIssue(issueDict=issueParam,username=userInit['DftJieDaoFuncUser'])
                #上报给区职能部门，设置上报参数
                sIssuePara['operation.issue.id']=rs['issueId']
                sIssuePara['keyId']=rs['issueStepId']      
                #上报
                result=dealIssue(issueDict=sIssuePara,username=userInit['DftJieDaoFuncUser'])
                self.assertTrue(result.result, '事件上报失败')
                #区民办中心部门受理
                sIssuePara2['operation.issue.id']=sIssuePara['operation.issue.id']
                sIssuePara2['keyId']=sIssuePara['keyId']+1
                result2=dealIssue(issueDict=sIssuePara2,username=userInit['DftQuMinBanFuncUser'])
                self.assertTrue(result2.result,'区民办中心受理失败！')
                #区民办中心办结
                sIssuePara3['operation.issue.id']=rs['issueId']
                sIssuePara3['keyId']=sIssuePara['keyId']+1
                result3=dealIssue(issueDict=sIssuePara3, username=userInit['DftQuMinBanFuncUser'], password='11111111')
                self.assertTrue(result3.result, '办结失败')
                ######将时间改为6天前
                data=moveTime(standardTime=getCurrentDateAndTime(),addDay=6,moveType=TimeMoveType.MINUS)
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                issueParam['issue.occurDate']= data
                issueParam['selectedTypes']=getDbQueryResult(dbCommand="select id from issuetypes i where i.domainid=(select id from issuetypedomains where module='core' and domainName='民生服务') and i.issuetypename='医疗卫生'"),
                rs=addIssue(issueDict=issueParam,username=userInit['DftJieDaoFuncUser'])
                #上报给区民办中心，设置上报参数
                sIssuePara['operation.issue.id']=rs['issueId']
                sIssuePara['keyId']=rs['issueStepId']      
                #上报
                result=dealIssue(issueDict=sIssuePara,username=userInit['DftJieDaoFuncUser'])
                self.assertTrue(result.result, '事件上报失败')
                #区民办中心受理
                sIssuePara2['operation.issue.id']=sIssuePara['operation.issue.id']
                sIssuePara2['keyId']=sIssuePara['keyId']+1
                result2=dealIssue(issueDict=sIssuePara2,username=userInit['DftQuMinBanFuncUser'])
                self.assertTrue(result2.result,'区民办中心受理失败！')
                #区职能部门办结
                sIssuePara3['operation.issue.id']=rs['issueId']
                sIssuePara3['keyId']=sIssuePara['keyId']+1
                result3=dealIssue(issueDict=sIssuePara3, username=userInit['DftQuMinBanFuncUser'], password='11111111')
                self.assertTrue(result3.result, '办结失败')
                #####将时间改回今天
                setLinuxTime(data=getCurrentDateAndTime())
                setLinuxTimeYunWei(data=getCurrentDateAndTime(),password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                issueParam['issue.occurDate']= '2016-1-6'
                issueParam['selectedTypes']=getDbQueryResult(dbCommand="select id from issuetypes i where i.domainid=(select id from issuetypedomains where module='core' and domainName='其他') and i.issuetypename='其他'"),
                rs=addIssue(issueDict=issueParam,username=userInit['DftJieDaoFuncUser'])
                #上报给区民办中心，设置上报参数
                sIssuePara['operation.issue.id']=rs['issueId']
                sIssuePara['keyId']=rs['issueStepId']      
                #上报
                result=dealIssue(issueDict=sIssuePara,username=userInit['DftJieDaoFuncUser'])
                self.assertTrue(result.result, '事件上报失败')
                #区职能部门受理
                sIssuePara2['operation.issue.id']=sIssuePara['operation.issue.id']
                sIssuePara2['keyId']=sIssuePara['keyId']+1
                result2=dealIssue(issueDict=sIssuePara2,username=userInit['DftQuMinBanFuncUser'])
                self.assertTrue(result2.result,'区民办中心受理失败！')
                #区职能部门办结
                sIssuePara3['operation.issue.id']=rs['issueId']
                sIssuePara3['keyId']=sIssuePara['keyId']+1
                sIssuePara3['dealTime']=Time.getCurrentDate()
                sIssuePara3['transferToType']='true'                
                result3=dealIssue(issueDict=sIssuePara3, username=userInit['DftQuMinBanFuncUser'], password='11111111')
                self.assertTrue(result3.result, '办结失败')
                #######验证新增数据统计正确性
                #当天统计数据
                viewPara1={
                        'issueAnalyzeDto.orgId':orgInit['DftJieDaoOrgId'],
                        'issueAnalyzeDto.status':'1',
                        'issueAnalyzeDto.beginDate':getCurrentDate(),
                        'issueAnalyzeDto.endDate':moveTime2(standardTime=getCurrentDateAndTime(),addDay=1,moveType=TimeMoveType.PLUS),
                        'viewType':'2',
                        '_search':'false',
                        'rows':'1000',
                        'page':'1',
                        'sidx':'id',
                        'sord':'desc'
                           }
                #自动化街道数据
                checkPara11={
                        'orgName':orgInit['DftJieDaoFuncOrg'],
                        'conflictNumber':0,
                        'otherNumber':1,
                        'securityNumber':0,
                        'serviceNumber':0,
                        'totalNumber':1
                           }
                #合计数据
                checkPara12={
                        'orgName':'合计',
                        'conflictNumber':0,
                        'otherNumber':1,
                        'securityNumber':0,
                        'serviceNumber':0,
                        'totalNumber':1                         
                             }
                url='/analyzing/issueAnalyzeManage/statisticalIssueAnalyze.action'
                result11=checkDictInDictlist(checkpara=checkPara11,listpara=viewPara1,url=url)
                self.assertTrue(result11, '自动化街道职能部门当天新增数据验证失败')
                result12=checkDictInDictlist(checkpara=checkPara12,listpara=viewPara1,url=url)
                self.assertTrue(result12, '合计当天新增数据验证失败')
                Log.LogOutput( message='当天新增数据验证成功!')
                #最近七天
                beginDate=moveTime2(standardTime=getCurrentDateAndTime(),addDay=6)
                endDate=moveTime2(standardTime=getCurrentDateAndTime(),addDay=1,moveType=TimeMoveType.PLUS)
                viewPara1['issueAnalyzeDto.beginDate']=beginDate
                viewPara1['issueAnalyzeDto.endDate']=endDate
                checkPara11['serviceNumber']=1
                checkPara11['totalNumber']=2
                checkPara12['serviceNumber']=1
                checkPara12['totalNumber']=2
                result11=checkDictInDictlist(checkpara=checkPara11,listpara=viewPara1,url=url)
                self.assertTrue(result11, '自动化街道职能部门七天内新增数据验证失败')
                result12=checkDictInDictlist(checkpara=checkPara12,listpara=viewPara1,url=url)
                self.assertTrue(result12, '合计七天内新增数据验证失败')
                Log.LogOutput( message='七天内新增数据验证成功!')
                #最近30天
                beginDate=moveTime2(standardTime=getCurrentDateAndTime(),addDay=29)
                viewPara1['issueAnalyzeDto.beginDate']=beginDate
                checkPara11['securityNumber']=1
                checkPara11['totalNumber']=3
                checkPara12['securityNumber']=1
                checkPara12['totalNumber']=3
                result11=checkDictInDictlist(checkpara=checkPara11,listpara=viewPara1,url=url)
                self.assertTrue(result11, '自动化街道职能部门30天内新增数据验证失败')
                result12=checkDictInDictlist(checkpara=checkPara12,listpara=viewPara1,url=url)
                self.assertTrue(result12, '合计30天内新增数据验证失败')
                Log.LogOutput( message='30天内新增数据验证成功!')
                #自定义时间，2015年1月1日至今
                viewPara1['issueAnalyzeDto.beginDate']='2015-1-1'
                checkPara11['conflictNumber']=1
                checkPara11['totalNumber']=4
                checkPara12['conflictNumber']=1
                checkPara12['totalNumber']=4
                result11=checkDictInDictlist(checkpara=checkPara11,listpara=viewPara1,url=url)
                self.assertTrue(result11, '自动化街道职能部门2015-1-1至今新增数据验证失败')
                result12=checkDictInDictlist(checkpara=checkPara12,listpara=viewPara1,url=url)
                self.assertTrue(result12, '合计2015-1-1至今新增数据验证失败')
                Log.LogOutput( message='2015-1-1至今新增数据验证成功!')
                ######验证办理数据统计
                viewPara2={
                        'issueAnalyzeDto.orgId':orgInit['DftQuOrgId'],
                        'issueAnalyzeDto.status':'2',
                        'issueAnalyzeDto.beginDate':getCurrentDate(),
                        'issueAnalyzeDto.endDate':moveTime2(standardTime=getCurrentDateAndTime(),addDay=1,moveType=TimeMoveType.PLUS),
                        'viewType':'2',
                        '_search':'false',
                        'rows':'1000',
                        'page':'1',
                        'sidx':'id',
                        'sord':'desc'
                           }
                #自动化街道数据
                checkPara21={
                        'orgName':orgInit['DftQuMinBanFuncOrg'],
                        'conflictNumber':0,
                        'otherNumber':1,
                        'securityNumber':0,
                        'serviceNumber':0,
                        'totalNumber':1
                           }
                #合计数据
                checkPara22={
                        'orgName':'合计',
                        'conflictNumber':0,
                        'otherNumber':1,
                        'securityNumber':0,
                        'serviceNumber':0,
                        'totalNumber':1                        
                             }
                result21=checkDictInDictlist(checkpara=checkPara21,listpara=viewPara2,url=url)
                self.assertTrue(result21, '自动化民办中心当天办理数据验证失败')
                result22=checkDictInDictlist(checkpara=checkPara22,listpara=viewPara2,url=url)
                self.assertTrue(result22, '合计当天办理数据验证失败')
                Log.LogOutput( message='当天办理数据验证成功!')
                #最近七天
                beginDate=moveTime2(standardTime=getCurrentDateAndTime(),addDay=6)
                viewPara2['issueAnalyzeDto.beginDate']=beginDate
                checkPara21['serviceNumber']=1
                checkPara21['totalNumber']=2
                checkPara22['serviceNumber']=1
                checkPara22['totalNumber']=2
                result21=checkDictInDictlist(checkpara=checkPara21,listpara=viewPara2,url=url)
                self.assertTrue(result21, '自动化民办中心七天内办理数据验证失败')
                result22=checkDictInDictlist(checkpara=checkPara22,listpara=viewPara2,url=url)
                self.assertTrue(result22, '合计七天内办理数据验证失败')
                Log.LogOutput( message='七天内办理数据验证成功!')
                #最近30天
                beginDate=moveTime2(standardTime=getCurrentDateAndTime(),addDay=29)
                viewPara2['issueAnalyzeDto.beginDate']=beginDate
                checkPara21['securityNumber']=1
                checkPara21['totalNumber']=3
                checkPara22['securityNumber']=1
                checkPara22['totalNumber']=3
                result21=checkDictInDictlist(checkpara=checkPara21,listpara=viewPara2,url=url)
                self.assertTrue(result21, '自动化民办中心30天内办理数据验证失败')
                result22=checkDictInDictlist(checkpara=checkPara22,listpara=viewPara2,url=url)
                self.assertTrue(result22, '合计30天内办理数据验证失败')
                Log.LogOutput( message='30天内办理数据验证成功!')
                #自定义时间，2015年1月1日至今
                viewPara2['issueAnalyzeDto.beginDate']='2015-1-1'
                checkPara21['conflictNumber']=1
                checkPara21['totalNumber']=4
                checkPara22['conflictNumber']=1
                checkPara22['totalNumber']=4
                result21=checkDictInDictlist(checkpara=checkPara21,listpara=viewPara2,url=url)
                self.assertTrue(result21, '自动化民办中心2015-1-1至今办理数据验证失败')
                result22=checkDictInDictlist(checkpara=checkPara22,listpara=viewPara2,url=url)
                self.assertTrue(result22, '合计2015-1-1至今办理数据验证失败')
                Log.LogOutput( message='2015-1-1至今办理数据验证成功!')
        
            finally:
                #将服务器时间改回正确时间
                setLinuxTime(data=getCurrentDateAndTime())
                setLinuxTimeYunWei(data=getCurrentDateAndTime(),password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
            pass

    '''
    @功能：研判分析-事件多维分析-纵向数量统计（层级）
    @ chenhui 2016-4-20
    '''
    def testStatus_009(self):
        '''事件多维分析-纵向数量统计(层级)'''
        #仿真环境下跳过测试
        if simulationEnvironment is True:
            pass
        else:
            try:
                data='2015-6-6 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                issueParam = copy.deepcopy(issueObject2) 
                issueParam['issue.occurDate']= data
                Time.wait(1)  
                addIssue(issueDict=issueParam,username=userInit['DftWangGeUser'])
                ######将时间改为29天前
                data=moveTime(standardTime=getCurrentDateAndTime(),addDay=29,moveType=TimeMoveType.MINUS)
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                issueParam['issue.occurDate']= data
                issueParam['selectedTypes']=getDbQueryResult(dbCommand="select id from issuetypes i where i.domainid=(select id from issuetypedomains where module='core' and domainName='治安、安全隐患') and i.issuetypename='安全生产'"),
                Time.wait(1)
                addIssue(issueDict=issueParam,username=userInit['DftSheQuUser'])
                ######将时间改为6天前
                data=moveTime(standardTime=getCurrentDateAndTime(),addDay=6,moveType=TimeMoveType.MINUS)
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                issueParam['issue.occurDate']= data
                issueParam['selectedTypes']=getDbQueryResult(dbCommand="select id from issuetypes i where i.domainid=(select id from issuetypedomains where module='core' and domainName='民生服务') and i.issuetypename='医疗卫生'"),
                Time.wait(1)
                addIssue(issueDict=issueParam,username=userInit['DftJieDaoFuncUser'])
                #####将时间改回今天
                setLinuxTime(data=getCurrentDateAndTime())
                setLinuxTimeYunWei(data=getCurrentDateAndTime(),password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                issueParam['issue.occurDate']= '2016-1-6'
                issueParam['selectedTypes']=getDbQueryResult(dbCommand="select id from issuetypes i where i.domainid=(select id from issuetypedomains where module='core' and domainName='其他') and i.issuetypename='其他'"),
                Time.wait(1)
                addIssue(issueDict=issueParam,username=userInit['DftQuMinBanFuncUser'])
                #######验证新增数据统计正确性
                #当天统计数据
                viewPara1={
                    'issueAnalyzeDto.orgId':orgInit['DftShiOrgId'],
                    'issueAnalyzeDto.status':'1',
                    'issueAnalyzeDto.beginDate':getCurrentDate(),
                    'issueAnalyzeDto.endDate':moveTime2(standardTime=getCurrentDateAndTime(),addDay=1,moveType=TimeMoveType.PLUS),
                    'viewType':'4',
                    '_search':'false',
                    'rows':'100',
                    'page':'1',
                    'sidx':'id',
                    'sord':'desc'
                           }
                #区县层级数据
                checkPara11=copy.deepcopy(zongXiangFenXiJianCha)
                checkPara11['orgName']='县（区）'
                checkPara11['otherNumber']=1
                checkPara11['totalNumber']=1
                #街道层级
                checkPara12=copy.deepcopy(zongXiangFenXiJianCha)
                checkPara12['orgName']='乡镇（街道）'
                #社区层级
                checkPara13=copy.deepcopy(zongXiangFenXiJianCha)
                checkPara13['orgName']='村（社区）'            
                #网格
                checkPara14=copy.deepcopy(zongXiangFenXiJianCha)
                checkPara14['orgName']='片组片格'      
                #合计
                checkPara15=copy.deepcopy(zongXiangFenXiJianCha)
                checkPara15['orgName']='合计'
                checkPara15['otherNumber']=1
                checkPara15['totalNumber']=1                          
    
                url='/analyzing/issueAnalyzeManage/verticalStatisticalIssueAnalyze.action'
                result11=checkDictInDictlist(checkpara=checkPara11,listpara=viewPara1,url=url)
                self.assertTrue(result11, '区县当天新增数据验证失败')
                result12=checkDictInDictlist(checkpara=checkPara12,listpara=viewPara1,url=url)
                self.assertTrue(result12, '街道当天新增数据验证失败')
                result13=checkDictInDictlist(checkpara=checkPara13,listpara=viewPara1,url=url)
                self.assertTrue(result13, '社区当天新增数据验证失败')
                result14=checkDictInDictlist(checkpara=checkPara14,listpara=viewPara1,url=url)
                self.assertTrue(result14, '网格当天新增数据验证失败')
                result15=checkDictInDictlist(checkpara=checkPara15,listpara=viewPara1,url=url)
                self.assertTrue(result15, '合计当天新增数据验证失败')
                Log.LogOutput( message='纵向统计当天新增数据验证成功!')
                #最近七天
                beginDate=moveTime2(standardTime=getCurrentDateAndTime(),addDay=6)
                endDate=moveTime2(standardTime=getCurrentDateAndTime(),addDay=1,moveType=TimeMoveType.PLUS)
                viewPara1['issueAnalyzeDto.beginDate']=beginDate
                viewPara1['issueAnalyzeDto.endDate']=endDate
                #街道层级
                checkPara12['serviceNumber']=1
                checkPara12['totalNumber']=1
                #合计
                checkPara15['serviceNumber']=1
                checkPara15['totalNumber']=2         
                result11=checkDictInDictlist(checkpara=checkPara11,listpara=viewPara1,url=url)
                self.assertTrue(result11, '区县最近七天新增数据验证失败')
                result12=checkDictInDictlist(checkpara=checkPara12,listpara=viewPara1,url=url)
                self.assertTrue(result12, '街道最近七天新增数据验证失败')
                result13=checkDictInDictlist(checkpara=checkPara13,listpara=viewPara1,url=url)
                self.assertTrue(result13, '社区最近七天新增数据验证失败')
                result14=checkDictInDictlist(checkpara=checkPara14,listpara=viewPara1,url=url)
                self.assertTrue(result14, '网格最近七天新增数据验证失败')
                result15=checkDictInDictlist(checkpara=checkPara15,listpara=viewPara1,url=url)
                self.assertTrue(result15, '合计最近七天新增数据验证失败')
                Log.LogOutput( message='纵向统计最近七天新增数据验证成功!')
                #最近30天
                beginDate=moveTime2(standardTime=getCurrentDateAndTime(),addDay=29)
                viewPara1['issueAnalyzeDto.beginDate']=beginDate
                #村层级
                checkPara13['securityNumber']=1
                checkPara13['totalNumber']=1
                #合计
                checkPara15['securityNumber']=1
                checkPara15['totalNumber']=3    
                result11=checkDictInDictlist(checkpara=checkPara11,listpara=viewPara1,url=url)
                self.assertTrue(result11, '区县最近30天新增数据验证失败')
                result12=checkDictInDictlist(checkpara=checkPara12,listpara=viewPara1,url=url)
                self.assertTrue(result12, '街道最近30天新增数据验证失败')
                result13=checkDictInDictlist(checkpara=checkPara13,listpara=viewPara1,url=url)
                self.assertTrue(result13, '社区最近30天新增数据验证失败')
                result14=checkDictInDictlist(checkpara=checkPara14,listpara=viewPara1,url=url)
                self.assertTrue(result14, '网格最近30天新增数据验证失败')
                result15=checkDictInDictlist(checkpara=checkPara15,listpara=viewPara1,url=url)
                self.assertTrue(result15, '合计最近30天新增数据验证失败')
                Log.LogOutput( message='纵向统计最近30天新增数据验证成功!')
                #自定义时间，2015年1月1日至今
                viewPara1['issueAnalyzeDto.beginDate']='2015-1-1'
                checkPara14['conflictNumber']=1
                checkPara14['totalNumber']=1
                checkPara15['conflictNumber']=1
                checkPara15['totalNumber']=4
                result11=checkDictInDictlist(checkpara=checkPara11,listpara=viewPara1,url=url)
                self.assertTrue(result11, '区县2015-1-1至今新增数据验证失败')
                result12=checkDictInDictlist(checkpara=checkPara12,listpara=viewPara1,url=url)
                self.assertTrue(result12, '街道2015-1-1至今新增数据验证失败')
                result13=checkDictInDictlist(checkpara=checkPara13,listpara=viewPara1,url=url)
                self.assertTrue(result13, '社区2015-1-1至今新增数据验证失败')
                result14=checkDictInDictlist(checkpara=checkPara14,listpara=viewPara1,url=url)
                self.assertTrue(result14, '网格2015-1-1至今新增数据验证失败')
                result15=checkDictInDictlist(checkpara=checkPara15,listpara=viewPara1,url=url)
                self.assertTrue(result15, '合计2015-1-1至今新增数据验证失败')
                Log.LogOutput( message='纵向统计2015-1-1至今新增数据验证成功!')
            finally:
                #将服务器时间改回正确时间
                setLinuxTime(data=getCurrentDateAndTime())
                setLinuxTimeYunWei(data=getCurrentDateAndTime(),password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
            pass
    
    '''
    @功能：研判分析-事件多维分析-纵向数量统计（账号）
    @ chenhui 2016-4-20
    '''
    def testStatus_010(self):
        '''事件多维分析-纵向数量统计(账号)'''
        #仿真环境下跳过测试
        if simulationEnvironment is True:
            pass
        else:
            addJieDaoFuncUser()
            try:
                data='2015-6-6 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                issueParam = copy.deepcopy(issueObject2) 
                issueParam['issue.occurDate']= data  
                addIssue(issueDict=issueParam,username=userInit['DftWangGeUser'])
                ######将时间改为29天前
                data=moveTime(standardTime=getCurrentDateAndTime(),addDay=29,moveType=TimeMoveType.MINUS)
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                issueParam['issue.occurDate']= data
                issueParam['selectedTypes']=getDbQueryResult(dbCommand="select id from issuetypes i where i.domainid=(select id from issuetypedomains where module='core' and domainName='治安、安全隐患') and i.issuetypename='安全生产'"),
                addIssue(issueDict=issueParam,username=userInit['DftSheQuUser'])
                ######将时间改为6天前
                data=moveTime(standardTime=getCurrentDateAndTime(),addDay=6,moveType=TimeMoveType.MINUS)
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                issueParam['issue.occurDate']= data
                issueParam['selectedTypes']=getDbQueryResult(dbCommand="select id from issuetypes i where i.domainid=(select id from issuetypedomains where module='core' and domainName='民生服务') and i.issuetypename='医疗卫生'"),
                addIssue(issueDict=issueParam,username=userInit['DftJieDaoFuncUser'])
                addIssue(issueDict=issueParam,username='zdhjdzn2@')
                #####将时间改回今天
                setLinuxTime(data=getCurrentDateAndTime())
                setLinuxTimeYunWei(data=getCurrentDateAndTime(),password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                issueParam['issue.occurDate']= '2016-1-6'
                issueParam['selectedTypes']=getDbQueryResult(dbCommand="select id from issuetypes i where i.domainid=(select id from issuetypedomains where module='core' and domainName='其他') and i.issuetypename='其他'"),
                addIssue(issueDict=issueParam,username=userInit['DftQuMinBanFuncUser'])
                #######验证新增数据统计正确性
                #当天统计数据
                viewPara1={
                    'issueAnalyzeDto.orgId':orgInit['DftQuOrgId'],
                    'issueAnalyzeDto.status':'1',
                    'issueAnalyzeDto.beginDate':getCurrentDate(),
                    'issueAnalyzeDto.endDate':moveTime2(standardTime=getCurrentDateAndTime(),addDay=1,moveType=TimeMoveType.PLUS),
                    'viewType':'5',
                    '_search':'false',
                    'rows':'100',
                    'page':'1',
                    'sidx':'id',
                    'sord':'desc'
                           }
                #区层级账号
                checkPara11=copy.deepcopy(zongXiangFenXiJianCha2)
                checkPara11['orgName']='测试自动化省->测试自动化市->测试自动化区->测试自动化区民办中心'
                checkPara11['createUser']=userInit['DftQuMinBanFuncUser']
                checkPara11['otherNumber']=1
                checkPara11['totalNumber']=1
                #合计
                checkPara12=copy.deepcopy(zongXiangFenXiJianCha2)
                checkPara12['orgName']='合计'
                checkPara12['otherNumber']=1
                checkPara12['totalNumber']=1                          
    
                url='/analyzing/issueAnalyzeManage/verticalStatisticalIssueAnalyze.action'
                result11=checkDictInDictlist(checkpara=checkPara11,listpara=viewPara1,url=url)
                self.assertTrue(result11, '区县当天纵向新增数据验证失败')
                result12=checkDictInDictlist(checkpara=checkPara12,listpara=viewPara1,url=url)
                self.assertTrue(result12, '合计当天纵向新增数据验证失败')
                Log.LogOutput( message='纵向统计当天新增数据验证成功!')
                #最近七天
                beginDate=moveTime2(standardTime=getCurrentDateAndTime(),addDay=6)
                endDate=moveTime2(standardTime=getCurrentDateAndTime(),addDay=1,moveType=TimeMoveType.PLUS)
                viewPara1['issueAnalyzeDto.beginDate']=beginDate
                viewPara1['issueAnalyzeDto.endDate']=endDate
                viewPara1['issueAnalyzeDto.orgId']=orgInit['DftJieDaoOrgId']
                #街道层级
                checkPara21=copy.deepcopy(zongXiangFenXiJianCha2)
                checkPara21['orgName']='测试自动化省->测试自动化市->测试自动化区->测试自动化街道->测试自动化街道派出所'
                checkPara21['createUser']=userInit['DftJieDaoFuncUser']
                checkPara21['serviceNumber']=1
                checkPara21['totalNumber']=1
                checkPara22=copy.deepcopy(zongXiangFenXiJianCha2)
                checkPara22['orgName']='测试自动化省->测试自动化市->测试自动化区->测试自动化街道->测试自动化街道派出所'
                checkPara22['createUser']='zdhjdzn2@'
                checkPara22['serviceNumber']=1
                checkPara22['totalNumber']=1
                #合计
                checkPara23=copy.deepcopy(zongXiangFenXiJianCha2)
                checkPara23['serviceNumber']=2
                checkPara23['totalNumber']=2         
                result21=checkDictInDictlist(checkpara=checkPara21,listpara=viewPara1,url=url)
                self.assertTrue(result21, 'zdhjdzn@纵向最近七天新增数据验证失败')
                result22=checkDictInDictlist(checkpara=checkPara22,listpara=viewPara1,url=url)
                self.assertTrue(result22, 'zdhjdzn2@纵向最近七天新增数据验证失败')
                result23=checkDictInDictlist(checkpara=checkPara23,listpara=viewPara1,url=url)
                self.assertTrue(result23, '合计纵向最近七天新增数据验证失败')
                Log.LogOutput( message='账号纵向统计最近七天新增数据验证成功!')
                #最近30天
                beginDate=moveTime2(standardTime=getCurrentDateAndTime(),addDay=29)
                viewPara1['issueAnalyzeDto.beginDate']=beginDate
                viewPara1['issueAnalyzeDto.orgId']=orgInit['DftSheQuOrgId']
                #村层级
                checkPara31=copy.deepcopy(zongXiangFenXiJianCha2)
                checkPara31['orgName']='测试自动化省->测试自动化市->测试自动化区->测试自动化街道->测试自动化社区'
                checkPara31['createUser']='zdhsq@'
                checkPara31['securityNumber']=1
                checkPara31['totalNumber']=1
                #合计
                checkPara32=copy.deepcopy(zongXiangFenXiJianCha2)
                checkPara32['securityNumber']=1
                checkPara32['totalNumber']=1       
                result31=checkDictInDictlist(checkpara=checkPara31,listpara=viewPara1,url=url)
                self.assertTrue(result31, 'zdhsq@纵向最近30天新增数据验证失败')
                result32=checkDictInDictlist(checkpara=checkPara32,listpara=viewPara1,url=url)
                self.assertTrue(result32, '合计纵向最近30天新增数据验证失败')
                Log.LogOutput( message='纵向统计最近30天新增数据验证成功!')
                #自定义时间，2015年1月1日至今
                viewPara1['issueAnalyzeDto.beginDate']='2015-1-1'
                viewPara1['issueAnalyzeDto.orgId']=orgInit['DftWangGeOrgId']
                checkPara41=copy.deepcopy(zongXiangFenXiJianCha2)
                checkPara41['orgName']='测试自动化省->测试自动化市->测试自动化区->测试自动化街道->测试自动化社区->测试自动化网格'
                checkPara41['createUser']='zdhwg@'
                checkPara41['conflictNumber']=1
                checkPara41['totalNumber']=1
                #合计
                checkPara42=copy.deepcopy(zongXiangFenXiJianCha2)
                checkPara42['conflictNumber']=1
                checkPara42['totalNumber']=1                     
                result41=checkDictInDictlist(checkpara=checkPara41,listpara=viewPara1,url=url)
                self.assertTrue(result41, '区县2015-1-1至今新增数据验证失败')
                result42=checkDictInDictlist(checkpara=checkPara42,listpara=viewPara1,url=url)
                self.assertTrue(result42, '街道2015-1-1至今新增数据验证失败')
                Log.LogOutput( message='纵向统计2015-1-1至今新增数据验证成功!')
            finally:
                #将服务器时间改回正确时间
                setLinuxTime(data=getCurrentDateAndTime())
                setLinuxTimeYunWei(data=getCurrentDateAndTime(),password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
            pass
    
    '''
    @功能：研判分析-事件多维分析-趋势研究
    @ chenhui 2016-4-21
    '''
    def testStatus_011(self):
        '''事件多维分析-趋势研究'''
        #仿真环境下跳过测试
        if simulationEnvironment is True:
            pass
        else:
            try:
                for n in range(1,13):
    #                 print n
                    data='2015-'+str(n)+'-6 '+getCurrentTime()
    #                 print Data
                    setLinuxTime(data)
                    setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                    issueParam = copy.deepcopy(issueObject2) 
                    issueParam['issue.occurDate']= data
                    #上报公共参数
                    sIssuePara=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)
                    sIssuePara['operation.dealOrg.id']=orgInit['DftJieDaoOrgId']
                    sIssuePara['operation.dealUserName']=userInit['DftJieDaoUserXM']
                    sIssuePara['operation.mobile']=userInit['DftJieDaoUserSJ']
                    sIssuePara['operation.content']='上报事件'
                    sIssuePara['operation.targeOrg.id']=orgInit['DftQuOrgId']
                    sIssuePara['themainOrgid']=orgInit['DftQuOrgId']        
                    sIssuePara['dealCode']='41'#上报
                    #区受理公共参数
                    sIssuePara2={
                                 'operation.dealOrg.id':orgInit['DftQuOrgId'],
                                 'operation.issue.id':'',
                                 'operation.dealUserName':userInit['DftQuUserXM'],
                                 'operation.mobile':userInit['DftQuUserSJ'],
                                 'dealCode':'61',
                                 'keyId':''
                                 }
                    #区办结公共参数
                    sIssuePara3=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)        
                    sIssuePara3['operation.dealOrg.id']=orgInit['DftQuOrgId']
                    sIssuePara3['operation.dealUserName']=userInit['DftQuUserXM']
                    sIssuePara3['operation.mobile']=userInit['DftQuUserSJ']
                    sIssuePara3['operation.content']='事件处理'       
                    sIssuePara3['dealCode']='31'#办结
                    for m in range(1,n+1):
                        issueParam['issue.subject']='事件主题'+createRandomString()
                        rs=addIssue(issueDict=issueParam)
                        #上报给区，设置上报参数
                        sIssuePara['operation.issue.id']=rs['issueId']
                        sIssuePara['keyId']=rs['issueStepId']      
                        #上报
                        result=dealIssue(issueDict=sIssuePara)
                        self.assertTrue(result.result, '事件上报失败')
                        #区受理
                        sIssuePara2['operation.issue.id']=rs['issueId']
                        sIssuePara2['keyId']=rs['issueStepId']+1
                        result2=dealIssue(issueDict=sIssuePara2,username=userInit['DftQuUser'])
                        self.assertTrue(result2.result,'区受理失败！')
                        #区办结
                        sIssuePara3['operation.issue.id']=rs['issueId']
                        sIssuePara3['keyId']=rs['issueStepId']+1
                        result3=dealIssue(issueDict=sIssuePara3, username=userInit['DftQuUser'], password='11111111')
                        self.assertTrue(result3.result, '办结失败')
                ######将时间改为2016-1-1
                data='2016-1-6 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                            #当天统计数据
                viewPara1={
                        'issueAnalyzeDto.status':'1',
                        'issueAnalyzeDto.orgId':orgInit['DftShiOrgId'],
                        '_search':'false',
                        'rows':'20',
                        'page':'1',
                        'sidx':'id',
                        'sord':'desc'
                           }
                url='/analyzing/issueAnalyzeStatisticalManage/getIssueAnalyzeStatisticalGrid.action' 
                #新增趋势统计
                checkPara1=copy.deepcopy(quShiJianCha)
                for i in range(1,13):
                    if i<10:
                        checkPara1['statisticalDate']='2015-0'+str(i)
                    else:
                        checkPara1['statisticalDate']='2015-'+str(i)
                    checkPara1['statisticalTotal']=i
                    result1=checkDictInDictlist(checkpara=checkPara1,listpara=viewPara1,url=url)
                    self.assertTrue(result1, '新增趋势出错，出错月份是第'+str(i)+'月')
                #办理趋势统计
                viewPara2={
                        'issueAnalyzeDto.status':'2',
                        'issueAnalyzeDto.orgId':orgInit['DftShiOrgId'],
                        '_search':'false',
                        'rows':'20',
                        'page':'1',
                        'sidx':'id',
                        'sord':'desc'
                           }
                checkPara2=copy.deepcopy(quShiJianCha)
                for i in range(1,13):
                    if i<10:
                        checkPara2['statisticalDate']='2015-0'+str(i)
                    else:
                        checkPara2['statisticalDate']='2015-'+str(i)
                    checkPara2['statisticalTotal']=i*2
                    result2=checkDictInDictlist(checkpara=checkPara2,listpara=viewPara2,url=url)
                    self.assertTrue(result2, '新增趋势出错，出错月份是第'+str(i)+'月')
                #办结趋势统计
                viewPara3={
                        'issueAnalyzeDto.status':'3',
                        'issueAnalyzeDto.orgId':orgInit['DftShiOrgId'],
                        '_search':'false',
                        'rows':'20',
                        'page':'1',
                        'sidx':'id',
                        'sord':'desc'
                           }
                checkPara3=copy.deepcopy(quShiJianCha)
                for i in range(1,13):
                    if i<10:
                        checkPara3['statisticalDate']='2015-0'+str(i)
                    else:
                        checkPara3['statisticalDate']='2015-'+str(i)
                    checkPara3['statisticalTotal']=i
                    result3=checkDictInDictlist(checkpara=checkPara3,listpara=viewPara3,url=url)
                    self.assertTrue(result3, '办结趋势出错，出错月份是第'+str(i)+'月')                      
            finally:
                #将服务器时间改回正确时间
                setLinuxTime(data=getCurrentDateAndTime())
                setLinuxTimeYunWei(data=getCurrentDateAndTime(),password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
            pass 
        
    '''
    @功能：研判分析-事件多维分析-类型分布
    @ chenhui 2016-4-21
    '''
    def testStatus_012(self):
        '''事件多维分析-类型分布'''
        #仿真环境下跳过测试
        if simulationEnvironment is True:
            pass
        else:
            try:
                data='2015-6-6 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                issueParam = copy.deepcopy(issueObject2) 
                issueParam['issue.occurDate']= data  
                addIssue(issueDict=issueParam)
                ######将时间改为29天前
                data=moveTime(standardTime=getCurrentDateAndTime(),addDay=29,moveType=TimeMoveType.MINUS)
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                issueParam['issue.occurDate']= data
                issueParam['selectedTypes']=getDbQueryResult(dbCommand="select id from issuetypes i where i.domainid=(select id from issuetypedomains where module='core' and domainName='治安、安全隐患') and i.issuetypename='安全生产'"),
                addIssue(issueDict=issueParam)
                ######将时间改为6天前
                data=moveTime(standardTime=getCurrentDateAndTime(),addDay=6,moveType=TimeMoveType.MINUS)
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                issueParam['issue.occurDate']= data
                issueParam['selectedTypes']=getDbQueryResult(dbCommand="select id from issuetypes i where i.domainid=(select id from issuetypedomains where module='core' and domainName='民生服务') and i.issuetypename='医疗卫生'"),
                addIssue(issueDict=issueParam)
                #####将时间改回今天
                setLinuxTime(data=getCurrentDateAndTime())
                setLinuxTimeYunWei(data=getCurrentDateAndTime(),password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                issueParam['issue.occurDate']= '2016-1-6'
                issueParam['selectedTypes']=getDbQueryResult(dbCommand="select id from issuetypes i where i.domainid=(select id from issuetypedomains where module='core' and domainName='其他') and i.issuetypename='其他'"),
                addIssue(issueDict=issueParam)
                #######验证新增数据统计正确性
                #当天统计数据
                viewPara={
                    'orgId':orgInit['DftQuOrgId'],
                    'searchTimeType':'ToDay',
                    'searchMinDate':'',
                    'searchMaxDate':'',
                    '_search':'false',
                    'rows':'20',
                    'page':'1',
                    'sidx':'id',
                    'sord':'desc'
                           }
                url='/analyzing/analyzingTypeDistribution/getStatisticListForList.action'
                #其他
                checkPara11=copy.deepcopy(leiXingFenBuJianCha)
                checkPara11['issueName']='其他'
                checkPara11['issueCounts']=1
                checkPara11['percentage']='100.0%'
                #矛盾纠纷
                checkPara12=copy.deepcopy(leiXingFenBuJianCha)
                checkPara12['issueName']='矛盾纠纷'
                checkPara12['issueCounts']=0
                checkPara12['percentage']='0.0%'            
                #治安、安全隐患
                checkPara13=copy.deepcopy(leiXingFenBuJianCha)
                checkPara13['issueName']='治安、安全隐患'
                checkPara13['issueCounts']=0
                checkPara13['percentage']='0.0%'
                #民生服务
                checkPara14=copy.deepcopy(leiXingFenBuJianCha)
                checkPara14['issueName']='民生服务'
                checkPara14['issueCounts']=0
                checkPara14['percentage']='0.0%'     
                #合计
                checkPara15=copy.deepcopy(leiXingFenBuJianCha)
                checkPara15['issueName']='合计'
                checkPara15['issueCounts']=1                      
    
                result11=checkDictInDictlist(checkpara=checkPara11,listpara=viewPara,url=url)
                self.assertTrue(result11, '其他当天新增数据验证失败')
                result12=checkDictInDictlist(checkpara=checkPara12,listpara=viewPara,url=url)
                self.assertTrue(result12, '矛盾纠纷当天新增数据验证失败')
                result13=checkDictInDictlist(checkpara=checkPara13,listpara=viewPara,url=url)
                self.assertTrue(result13, '治安、安全隐患当天新增数据验证失败')
                result14=checkDictInDictlist(checkpara=checkPara14,listpara=viewPara,url=url)
                self.assertTrue(result14, '民生服务当天新增数据验证失败')
                result15=checkDictInDictlist(checkpara=checkPara15,listpara=viewPara,url=url)
                self.assertTrue(result15, '合计当天新增数据验证失败')
                Log.LogOutput( message='类型统计当天新增数据验证成功!')
                #最近七天
                viewPara['searchTimeType']='Week'
                #其他
                checkPara21=copy.deepcopy(leiXingFenBuJianCha)
                checkPara21['issueName']='其他'
                checkPara21['issueCounts']=1
                checkPara21['percentage']='50.0%'
                #矛盾纠纷
                checkPara22=copy.deepcopy(leiXingFenBuJianCha)
                checkPara22['issueName']='矛盾纠纷'
                checkPara22['issueCounts']=0
                checkPara22['percentage']='0.0%'            
                #治安、安全隐患
                checkPara23=copy.deepcopy(leiXingFenBuJianCha)
                checkPara23['issueName']='治安、安全隐患'
                checkPara23['issueCounts']=0
                checkPara23['percentage']='0.0%'
                #民生服务
                checkPara24=copy.deepcopy(leiXingFenBuJianCha)
                checkPara24['issueName']='民生服务'
                checkPara24['issueCounts']=1
                checkPara24['percentage']='50.0%'     
                #合计
                checkPara25=copy.deepcopy(leiXingFenBuJianCha)
                checkPara25['issueName']='合计'
                checkPara25['issueCounts']=2                  
    
                result21=checkDictInDictlist(checkpara=checkPara21,listpara=viewPara,url=url)
                self.assertTrue(result21, '其他最近一周新增数据验证失败')
                result22=checkDictInDictlist(checkpara=checkPara22,listpara=viewPara,url=url)
                self.assertTrue(result22, '矛盾纠纷最近一周新增数据验证失败')
                result23=checkDictInDictlist(checkpara=checkPara23,listpara=viewPara,url=url)
                self.assertTrue(result23, '治安、安全隐患最近一周新增数据验证失败')
                result24=checkDictInDictlist(checkpara=checkPara24,listpara=viewPara,url=url)
                self.assertTrue(result24, '民生服务最近一周新增数据验证失败')
                result25=checkDictInDictlist(checkpara=checkPara25,listpara=viewPara,url=url)
                self.assertTrue(result25, '合计最近一周新增数据验证失败')
                Log.LogOutput( message='类型统计最近一周新增数据验证成功!')     
                #最近一个月
                viewPara['searchTimeType']='Month'
                #其他
                checkPara31=copy.deepcopy(leiXingFenBuJianCha)
                checkPara31['issueName']='其他'
                checkPara31['issueCounts']=1
                checkPara31['percentage']='33.33%'
                #矛盾纠纷
                checkPara32=copy.deepcopy(leiXingFenBuJianCha)
                checkPara32['issueName']='矛盾纠纷'
                checkPara32['issueCounts']=0
                checkPara32['percentage']='0.0%'            
                #治安、安全隐患
                checkPara33=copy.deepcopy(leiXingFenBuJianCha)
                checkPara33['issueName']='治安、安全隐患'
                checkPara33['issueCounts']=1
                checkPara33['percentage']='33.33%'
                #民生服务
                checkPara34=copy.deepcopy(leiXingFenBuJianCha)
                checkPara34['issueName']='民生服务'
                checkPara34['issueCounts']=1
                checkPara34['percentage']='33.33%'     
                #合计
                checkPara35=copy.deepcopy(leiXingFenBuJianCha)
                checkPara35['issueName']='合计'
                checkPara35['issueCounts']=3                     
                result31=checkDictInDictlist(checkpara=checkPara31,listpara=viewPara,url=url)
                self.assertTrue(result31, '其他最近一个月新增数据验证失败')
                result32=checkDictInDictlist(checkpara=checkPara32,listpara=viewPara,url=url)
                self.assertTrue(result32, '矛盾纠纷最近一个月新增数据验证失败')
                result33=checkDictInDictlist(checkpara=checkPara33,listpara=viewPara,url=url)
                self.assertTrue(result33, '治安、安全隐患最近一个月新增数据验证失败')
                result34=checkDictInDictlist(checkpara=checkPara34,listpara=viewPara,url=url)
                self.assertTrue(result34, '民生服务最近一个月新增数据验证失败')
                result35=checkDictInDictlist(checkpara=checkPara35,listpara=viewPara,url=url)
                self.assertTrue(result35, '合计最近一个月新增数据验证失败')
                Log.LogOutput( message='类型统计最近一个月新增数据验证成功!')             
                #2015-1-1至今
                viewPara['searchTimeType']='Custom'
                viewPara['searchMinDate']='2015-1-1'
                endDate=moveTime2(standardTime=getCurrentDateAndTime(),addDay=1,moveType=TimeMoveType.PLUS)
                viewPara['searchMaxDate']=endDate
                #其他
                checkPara41=copy.deepcopy(leiXingFenBuJianCha)
                checkPara41['issueName']='其他'
                checkPara41['issueCounts']=1
                checkPara41['percentage']='25.0%'
                #矛盾纠纷
                checkPara42=copy.deepcopy(leiXingFenBuJianCha)
                checkPara42['issueName']='矛盾纠纷'
                checkPara42['issueCounts']=1
                checkPara42['percentage']='25.0%'            
                #治安、安全隐患
                checkPara43=copy.deepcopy(leiXingFenBuJianCha)
                checkPara43['issueName']='治安、安全隐患'
                checkPara43['issueCounts']=1
                checkPara43['percentage']='25.0%'
                #民生服务
                checkPara44=copy.deepcopy(leiXingFenBuJianCha)
                checkPara44['issueName']='民生服务'
                checkPara44['issueCounts']=1
                checkPara44['percentage']='25.0%'     
                #合计
                checkPara45=copy.deepcopy(leiXingFenBuJianCha)
                checkPara45['issueName']='合计'
                checkPara45['issueCounts']=4                     
    
                result41=checkDictInDictlist(checkpara=checkPara41,listpara=viewPara,url=url)
                self.assertTrue(result41, '其他2015-1-1至今新增数据验证失败')
                result42=checkDictInDictlist(checkpara=checkPara42,listpara=viewPara,url=url)
                self.assertTrue(result42, '矛盾纠纷2015-1-1至今新增数据验证失败')
                result43=checkDictInDictlist(checkpara=checkPara43,listpara=viewPara,url=url)
                self.assertTrue(result43, '治安、安全隐患2015-1-1至今新增数据验证失败')
                result44=checkDictInDictlist(checkpara=checkPara44,listpara=viewPara,url=url)
                self.assertTrue(result44, '民生服务2015-1-1至今新增数据验证失败')
                result45=checkDictInDictlist(checkpara=checkPara45,listpara=viewPara,url=url)
                self.assertTrue(result45, '合计2015-1-1至今新增数据验证失败')
                Log.LogOutput( message='类型统计2015-1-1至今新增数据验证成功!') 
            finally:
                #将服务器时间改回正确时间
                setLinuxTime(data=getCurrentDateAndTime())
                setLinuxTimeYunWei(data=getCurrentDateAndTime(),password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
            pass

    '''
    @功能：研判分析-综合信息查询-综合新增查询
    @ chenhui 2016-6-3
    '''
    def testStatus_013(self):
        '''新增统计'''
        #仿真环境下跳过测试
        if simulationEnvironment is True:
            pass
        else:
            ShiYouRenKouIntf.deleteAllPopulation()
            ShiYouFangWuIntf.deleteAllActualHouse()
            ZuZhiChangSuoIntf.deleteAllPopulation()
            #新增户籍人口
            HuJiParam_03 = copy.deepcopy(ShiYouRenKouPara.populationObject) 
            HuJiParam_03['mode']='add'
            HuJiParam_03['population.organization.id'] = orgInit['DftWangGeOrgId']
            HuJiParam_03['population.organization.orgName'] = orgInit['DftWangGeOrg']
            HuJiParam_03['population.idCardNo'] = '111111111111130'
            HuJiParam_03['population.name'] = '户籍人口'+createRandomString()
            HuJiParam_03['population.isHaveHouse1'] = 'null'         
            responseDict = ShiYouRenKouIntf.add_HuJiRenKou(HuJiRenKouDict=HuJiParam_03, username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增户籍人口失败')
            #新增流动人口
            LiuDongParam_01 = copy.deepcopy(ShiYouRenKouPara.populationObject) 
            LiuDongParam_01['population.organization.id'] = orgInit['DftWangGeOrgId']
            LiuDongParam_01['population.actualPopulationType'] = 'floatingPopulation'
            LiuDongParam_01['population.organization.orgName'] = orgInit['DftWangGeOrg']
            LiuDongParam_01['population.idCardNo'] = '111111111111111'
            LiuDongParam_01['population.name'] = 'test'+createRandomString()
            LiuDongParam_01['population.isHaveHouse1'] = 'null'
            LiuDongParam_01['population.nativePlaceAddress']='户籍详址'+createRandomString()
            LiuDongParam_01['population.usedName']='别名'+createRandomString()
            response1 = ShiYouRenKouIntf.add_LiuDongRenKou(LiuDongRenKouDict=LiuDongParam_01, username=userInit['DftWangGeUser'], password='11111111')
    #         print response1.text
            self.assertTrue(response1.result, '新增流动人口失败')
            #新增未落户人口
            WeiLuoHuParam_01 = copy.deepcopy(ShiYouRenKouPara.unsettledPopulationObject) 
            WeiLuoHuParam_01['mode'] = 'success'
            WeiLuoHuParam_01['ownerOrg.id'] = orgInit['DftWangGeOrgId']
            WeiLuoHuParam_01['unsettledPopulation.organization.id'] = orgInit['DftWangGeOrgId']
            WeiLuoHuParam_01['unsettledPopulation.organization.orgName'] = orgInit['DftWangGeOrg']
            WeiLuoHuParam_01['unsettledPopulation.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
            WeiLuoHuParam_01['unsettledPopulation.idCardNo'] = '111111111110001'
            WeiLuoHuParam_01['unsettledPopulation.name'] = 'test001'+createRandomString()
            WeiLuoHuParam_01['unsettledPopulation.isHaveHouse1'] = 'null'         
            responseDict = ShiYouRenKouIntf.add_WeiLuoHuRenKou(WeiLuoHuRenKouDict=WeiLuoHuParam_01, username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增未落户人口失败')
            #境外人员
            JingWaiParam_01 = copy.deepcopy(ShiYouRenKouPara.overseaPopulationObject) 
            JingWaiParam_01['mode'] = 'success'
            JingWaiParam_01['overseaPersonnel.organization.id'] = orgInit['DftWangGeOrgId']
            JingWaiParam_01['overseaPersonnel.englishName'] = 'www'
            JingWaiParam_01['overseaPersonnel.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
            JingWaiParam_01['overseaPersonnel.certificateType.id'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from propertydicts t where t.displayname='旅游证'" )
            JingWaiParam_01['overseaPersonnel.certificateNo'] = '343'
            JingWaiParam_01['overseaPersonnel.isHaveHouse1'] = 'null'         
            responseDict = ShiYouRenKouIntf.add_JingWaiRenKou(JingWaiRenKouDict=JingWaiParam_01, username=userInit['DftWangGeUser'], password='11111111') 
            self.assertTrue(responseDict.result, '新增境外人口失败') 
            #刑满释放
            xingShiParam_17 = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
            xingShiParam_17['mode']='add'
            xingShiParam_17['population.organization.id'] = orgInit['DftWangGeOrgId']
            xingShiParam_17['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人口or流动人口
            xingShiParam_17['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['xingManShiFangRenYuan']
            xingShiParam_17['population.organization.orgName'] = orgInit['DftWangGeOrg']
            xingShiParam_17['population.idCardNo'] = '331100199711220000'
            xingShiParam_17['population.name'] = '刑满释放人员'+createRandomString()
            xingShiParam_17['actualPersonType'] = xingShiParam_17['population.actualPopulationType']
            xingShiParam_17['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
            xingShiParam_17['population.isHaveHouse1'] = 'null'   
            xingShiParam_17['population.caseReason'] = 'Reason'+createRandomString()
            xingShiParam_17['population.positiveInfoType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '刑释人员'") 
            xingShiParam_17['population.laborEduAddress'] = '劳教所'+createRandomString()
            xingShiParam_17['population.imprisonmentDate'] = '2weeks'
            xingShiParam_17['population.releaseOrBackDate'] = '2015-12-01'  
            xingShiCheckParam_17 = copy.deepcopy(ShiYouRenKouPara.checkPopulationDict)
            xingShiCheckParam_17['idCardNo'] = xingShiParam_17['population.idCardNo']
            responseDict = ShiYouRenKouIntf.add_xingManShiFang(xingManShiFangDict=xingShiParam_17, username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增刑满释放人员失败')
            #社区矫正
            jiaoZhengParam_17 = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
            jiaoZhengParam_17['mode']='add'
            jiaoZhengParam_17['population.organization.id'] = orgInit['DftWangGeOrgId']
            jiaoZhengParam_17['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人口or流动人口
            jiaoZhengParam_17['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['sheQuJiaoZhengRenYuan']
            jiaoZhengParam_17['population.organization.orgName'] = orgInit['DftWangGeOrg']
            jiaoZhengParam_17['population.idCardNo'] = '331100199711200001'
            jiaoZhengParam_17['population.name'] = '矫正人员'+createRandomString()
            jiaoZhengParam_17['actualPersonType'] = jiaoZhengParam_17['population.actualPopulationType']
            jiaoZhengParam_17['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
            jiaoZhengParam_17['population.isHaveHouse1'] = 'null'   
            jiaoZhengParam_17['population.accusation'] = '矫正罪名'+createRandomString()
            jiaoZhengParam_17['population.executeType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '监外执行罪犯'") 
            jiaoZhengParam_17['population.rectifyStartDate'] = '2015-12-01'
            jiaoZhengParam_17['population.rectifyEndDate'] = '2015-12-31'
            jiaoZhengParam_17['population.nativePlaceAddress']='户籍地详址'+createRandomString() 
            responseDict = ShiYouRenKouIntf.add_sheQuJiaoZheng(sheQuJiaoZhengDict=jiaoZhengParam_17, username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增社区矫正人员失败')
            #精神病人员
            psychosisParam_17= copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
            psychosisParam_17['mode']='add'
            psychosisParam_17['population.organization.id'] = orgInit['DftWangGeOrgId']
            psychosisParam_17['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人口or流动人口
            psychosisParam_17['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['jingShenBingRenYuan']
            psychosisParam_17['population.organization.orgName'] = orgInit['DftWangGeOrg']
            psychosisParam_17['population.idCardNo'] = '332200199711220000'
            psychosisParam_17['population.name'] = '精神病人员'
            psychosisParam_17['actualPersonType'] = psychosisParam_17['population.actualPopulationType']
            psychosisParam_17['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
            psychosisParam_17['population.isHaveHouse1'] = 'null'   
            psychosisParam_17['population.dangerLevel.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='危险程度', displayName='低')   
            responseDict = ShiYouRenKouIntf.add_jingShengBingRenYuan(psychosisDict=psychosisParam_17, username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增精神病人员失败')
            #吸毒人员
            xiDuParam_17 = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
            xiDuParam_17['mode']='add'
            xiDuParam_17['population.organization.id'] = orgInit['DftWangGeOrgId']
            xiDuParam_17['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于会人口or流动人口
            xiDuParam_17['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['xiDuRenYuan']
            xiDuParam_17['population.organization.orgName'] = orgInit['DftWangGeOrg']
            xiDuParam_17['population.idCardNo'] = '333300199711220000'
            xiDuParam_17['population.name'] = '吸毒人员'
            xiDuParam_17['actualPersonType'] = xiDuParam_17['population.actualPopulationType']
            xiDuParam_17['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
            xiDuParam_17['population.isHaveHouse1'] = 'null'   
            xiDuParam_17['population.detoxicateCase.id'] = CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '强制戒毒'")  
            responseDict = ShiYouRenKouIntf.add_xiDuRenYuan(xiDuRenYuanDict=xiDuParam_17, username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增吸毒人员失败')
            ShiYouRenKouIntf.zhongDianQingShaoNianDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
            #重点青少年
            qingShaoNianParam_17 = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
            qingShaoNianParam_17['mode']='add'
            qingShaoNianParam_17['population.organization.id'] = orgInit['DftWangGeOrgId']
            qingShaoNianParam_17['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人口or流动人口
            qingShaoNianParam_17['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['zhongDianQingShaoNian']
            qingShaoNianParam_17['population.organization.orgName'] = orgInit['DftWangGeOrg']
            qingShaoNianParam_17['population.idCardNo'] = '334400199711220000'
            qingShaoNianParam_17['population.name'] = '重点青少年'
            qingShaoNianParam_17['actualPersonType'] = qingShaoNianParam_17['population.actualPopulationType']
            qingShaoNianParam_17['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
            qingShaoNianParam_17['population.isHaveHouse1'] = 'null'  
            qingShaoNianParam_17['staffTypeIds'] =CommonIntf.getIdByDomainAndDisplayName(domainName='闲散青少年人员类型', displayName='闲散青少年')     #人员类型，根据字段找对应id    
            responseDict = ShiYouRenKouIntf.add_zhongDianQingShaoNian(qingShaoNianDict=qingShaoNianParam_17, username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增重点青少年失败')
            #重点上访人员
            shangFangParam_17 = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
            shangFangParam_17['mode']='add'
            shangFangParam_17['population.organization.id'] = orgInit['DftWangGeOrgId']
            shangFangParam_17['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人员or流动人口
            shangFangParam_17['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['zhongDianShangFangRenYuan']
            shangFangParam_17['population.organization.orgName'] = orgInit['DftWangGeOrg']
            shangFangParam_17['population.idCardNo'] = '335500199711220000'
            shangFangParam_17['population.name'] = '重点上访人员'
            shangFangParam_17['actualPersonType'] = shangFangParam_17['population.actualPopulationType']
            shangFangParam_17['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
            shangFangParam_17['population.isHaveHouse1'] = 'null'   
            shangFangParam_17['population.visitReason'] = '上访原因'       
            responseDict = ShiYouRenKouIntf.add_shangFangRenYuan(shangFangDict=shangFangParam_17, username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增上访人员失败')   
            #危险品从业人员
            practitionerParam_17 = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
            practitionerParam_17['mode']='add'
            practitionerParam_17['population.organization.id'] = orgInit['DftWangGeOrgId']
            practitionerParam_17['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']   #属于户籍人员or流动人员
            practitionerParam_17['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['weiXianPingCongYeRenYuan']
            practitionerParam_17['population.organization.orgName'] = orgInit['DftWangGeOrg']
            practitionerParam_17['population.idCardNo'] = '336600199711220000'
            practitionerParam_17['population.name'] = '危险品从业人员'
            practitionerParam_17['actualPersonType'] = practitionerParam_17['population.actualPopulationType']
            practitionerParam_17['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
            practitionerParam_17['population.isHaveHouse1'] = 'null'   
            practitionerParam_17['population.dangerousWorkingType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='危险从业类别', displayName='其他')  #危险从业类别，选择id
            practitionerParam_17['population.legalPerson'] = '法人代表'  
            practitionerParam_17['population.legalPersonMobileNumber'] = '11111111111' 
            practitionerParam_17['population.legalPersonTelephone'] = '3333333'  
            practitionerParam_17['population.workUnit'] = '工作单位'       
            responseDict = ShiYouRenKouIntf.add_weiXianPingCongYeRenYuan(practitionerDict=practitionerParam_17, username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增危险品从业人员失败') 
            #其他人员
            otherParam_17 = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
            otherParam_17['mode']='add'
            otherParam_17['population.organization.id'] = orgInit['DftWangGeOrgId']
            otherParam_17['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人员or流动人员
            otherParam_17['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['qiTaRenYuan']
            otherParam_17['population.organization.orgName'] = orgInit['DftWangGeOrg']
            otherParam_17['population.idCardNo'] = '337700199711220000'
            otherParam_17['population.name'] = '其他人员'
            otherParam_17['actualPersonType'] = otherParam_17['population.actualPopulationType']
            otherParam_17['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
            otherParam_17['population.isHaveHouse1'] = 'null'   
            otherParam_17['population.attentionExtent.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='关注程度', displayName='一般')  #关注程度，选择id，可以不填
            otherParam_17['population.attentionReason'] = '关注原因'   #可以不填      
            responseDict = ShiYouRenKouIntf.add_qiTaRenYuan(otherDict=otherParam_17, username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增其他人员失败')       
            #新增实有房屋
            houseParam_02 = copy.deepcopy(ShiYouFangWuPara.houseObject) 
            houseParam_02['dailogName']='rentalHouseMaintanceDialog'
            houseParam_02['houseInfo.organization.id'] = orgInit['DftWangGeOrgId']
            houseParam_02['mode']='add'
            houseParam_02['isUseFrom'] = 'actualHouse'
            houseParam_02['houseInfo.organization.orgName'] = orgInit['DftWangGeOrg']
            houseParam_02['houseInfo.addressType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '现居住址类型') and p.displayname = '其他'")
            houseParam_02['currentAddressType'] = houseParam_02['houseInfo.addressType.id']   
            houseParam_02['houseInfo.address'] = '出租房%s'%CommonUtil.createRandomString() 
            houseParam_02['houseInfo.isRentalHouse'] = 'true'      
            responseDict = ShiYouFangWuIntf.add_ShiYouFangWu(fangWuDict=houseParam_02, username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增实有房失败')   
            #出租房
            rentalParam_02 = copy.deepcopy(ShiYouFangWuPara.rentalObject) 
            rentalParam_02['houseInfo.organization.id'] = houseParam_02['houseInfo.organization.id']
            rentalParam_02['houseInfo.houseId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from rentalHouse t where t.address='%s'" % (houseParam_02['houseInfo.address']))
            rentalParam_02['houseInfo.orgInternalCode'] = CommonIntf.getDbQueryResult(dbCommand = "select t.orginternalcode from ORGANIZATIONS t where t.orgname='%s'" % (rentalParam_02['houseInfo.organization.id']))
            rentalParam_02['dailogName']='rentalHouseMaintanceDialog'
            rentalParam_02['mode']='add'
            rentalParam_02['houseInfo.id'] = str(CommonIntf.getDbQueryResult(dbCommand = "select max(t.id) from RENTALHOUSE t"))
            rentalParam_02['houseInfo.isEmphasis'] = '0'
            rentalParam_02['houseInfo.rentalPerson'] = '房东'
            rentalParam_02['houseInfo.rentalType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '套房'")   
            rentalParam_02['houseInfo.hiddenDangerLevel.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='隐患程度', displayName='安全')
            responseDict = ShiYouFangWuIntf.add_ChuZuFang(chuZuDict=rentalParam_02, username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增出租房失败')
            #安全生产重点
            testCase_04Param = copy.deepcopy(ZuZhiChangSuoPara.addAnQuanShengChan) 
            testCase_04Param['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
            testCase_04Param['enterprise.name'] = '测试安全生产重点%s' % CommonUtil.createRandomString()
            testCase_04Param['enterprise.keyType'] = 'safetyProductionKey'
            testCase_04Param['mode'] = 'add'
            testCase_04Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
            testCase_04Param['placeTypeName'] = '安全生产重点'
            testCase_04Param['enterprise.address'] = '测试地址1'
            testCase_04Param['enterprise.legalPerson'] = '法人代表1'
            testCase_04Param['enterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='企业类型', displayName='规上企业')
            responseDict = ZuZhiChangSuoIntf.addAnQuanShengChan(AnQuanShengChanDict=testCase_04Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增失败')
    #         新增消防安全重点
            testCase_05Param = copy.deepcopy(ZuZhiChangSuoPara.addXiaoFangAnQuan) 
            testCase_05Param['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
            testCase_05Param['enterprise.name'] = '测试场所名称%s' % CommonUtil.createRandomString()
            testCase_05Param['enterprise.keyType'] = 'fireSafetyKey'
            testCase_05Param['mode'] = 'add'
            testCase_05Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
            testCase_05Param['placeTypeName'] = '消防安全重点'
            testCase_05Param['enterprise.address'] = '测试场所地址1'
            testCase_05Param['enterprise.legalPerson'] = '测试负责人'
            testCase_05Param['enterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='消防安全重点类别', displayName='商场')
            responseDict = ZuZhiChangSuoIntf.addXiaoFangAnQuan(XiaoFangAnQuanDict=testCase_05Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增失败')
            #新增治安重点
            testCase_06Param = copy.deepcopy(ZuZhiChangSuoPara.addZhiAnZhongDian) 
            testCase_06Param['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
            testCase_06Param['enterprise.name'] = '测试场所名称%s' % CommonUtil.createRandomString()
            testCase_06Param['enterprise.keyType'] = 'securityKey'
            testCase_06Param['mode'] = 'add'
            testCase_06Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
            testCase_06Param['placeTypeName'] = '治安重点'
            testCase_06Param['enterprise.address'] = '测试场所地址1'
            testCase_06Param['enterprise.legalPerson'] = '测试负责人'
            testCase_06Param['enterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='治安重点类别', displayName='城乡结合部')
            responseDict = ZuZhiChangSuoIntf.addZhiAnZhongDian(ZhiAnZhongDianDict=testCase_06Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增失败')
            #         新增学校
            testCase_07Param = copy.deepcopy(ZuZhiChangSuoPara.addXueXiao) 
            testCase_07Param['orgId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
            testCase_07Param['school.chineseName'] = '测试学校名称%s' % CommonUtil.createRandomString()
            testCase_07Param['school.kind.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='学校性质', displayName='公办')
            testCase_07Param['mode'] = 'add'
            testCase_07Param['school.hasCertificate'] = '请选择'
            testCase_07Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
            testCase_07Param['placeTypeName'] = '学校'
            testCase_07Param['school.address'] = '测试学校地址1'
            testCase_07Param['school.president'] = '测试校长'
            testCase_07Param['school.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='学校类型', displayName='小学')
            responseDict = ZuZhiChangSuoIntf.addXueXiao(XueXiaoDict=testCase_07Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增失败')  
            #         新增医院
            testCase_08Param = copy.deepcopy(ZuZhiChangSuoPara.addYiYuan) 
            testCase_08Param['organizationId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
            testCase_08Param['hospital.hospitalName'] = '测试医院名称%s' % CommonUtil.createRandomString()
            testCase_08Param['hospital.personLiableTelephone'] = '1234-12341234'
            testCase_08Param['mode'] = 'add'
            testCase_08Param['hospital.organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
            testCase_08Param['hospital.personLiableMobileNumber'] = '13411111111'
            testCase_08Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
            testCase_08Param['hospital.address'] = '测试医院地址1'
            testCase_08Param['hospital.personLiable'] = '测试综治负责人'
            responseDict = ZuZhiChangSuoIntf.addYiYuan(YiYuanDict=testCase_08Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增失败')  
            #         新增危险化学品单位
            testCase_09Param = copy.deepcopy(ZuZhiChangSuoPara.addWeiXianHuaXuePing) 
            testCase_09Param['organizationId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
            testCase_09Param['location.unitName'] = '测试单位名称%s' % CommonUtil.createRandomString()
            testCase_09Param['mode'] = 'add'
            testCase_09Param['location.organization.orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
            responseDict = ZuZhiChangSuoIntf.addWeiXianHuaXuePing(WeiXianHuaXuePingDict=testCase_09Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增失败')
    #         新增上网服务单位
            testCase_10Param = copy.deepcopy(ZuZhiChangSuoPara.addShangWanFuWu) 
            testCase_10Param['location.organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
            testCase_10Param['location.placeName'] = '测试单位名称%s' % CommonUtil.createRandomString()
            testCase_10Param['mode'] = 'add'
            testCase_10Param['ajaxUrl'] = '/baseinfo/internetBarManage/hasDuplicateInternetBarLocation.action'
            testCase_10Param['location.organization.orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
            responseDict = ZuZhiChangSuoIntf.addShangWanFuWu(ShangWanFuWuDict=testCase_10Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增失败')
            #         新增公共场所
            testCase_11Param = copy.deepcopy(ZuZhiChangSuoPara.addShangWanFuWu) 
            testCase_11Param['location.organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
            testCase_11Param['location.placeName'] = '测试公共场所名称%s' % CommonUtil.createRandomString()
            testCase_11Param['location.placeAddress'] = '测试场所地址'
            testCase_11Param['mode'] = 'add'
            testCase_11Param['ajaxUrl'] = '/baseinfo/publicPlaceManage/hasDuplicatePublicPlaceLocation.action'
            testCase_11Param['location.organization.orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
            responseDict = ZuZhiChangSuoIntf.addGongGongChangSuo(GongGongChangSuoDict=testCase_11Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增失败')  
            #         新增公共复杂场所
            testCase_12Param = copy.deepcopy(ZuZhiChangSuoPara.addGongGongFuZaChangSuo) 
            testCase_12Param['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
            testCase_12Param['commonComplexPlace.name'] = '测试公共复杂场所名称%s' % CommonUtil.createRandomString()
            testCase_12Param['commonComplexPlace.legalPerson'] = '测试负责人'
            testCase_12Param['mode'] = 'add'
            testCase_12Param['commonComplexPlace_orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
            responseDict = ZuZhiChangSuoIntf.addGongGongFuZaChangSuo(GongGongFuZaChangSuoDict=testCase_12Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增失败')    
            #         新增特种行业
            testCase_13Param = copy.deepcopy(ZuZhiChangSuoPara.addGongGongFuZaChangSuo) 
            testCase_13Param['organizationId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
            testCase_13Param['specialTrade.name'] = '测试特种行业名称%s' % CommonUtil.createRandomString()
            testCase_13Param['specialTrade.personLiable'] = '测试负责人'
            testCase_13Param['specialTrade.address'] = '测试企业地址'
            testCase_13Param['specialTrade.organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
            testCase_13Param['specialTrade.personLiableTelephone'] = '0571-12345678'
            testCase_13Param['specialTrade.personLiableMobileNumber'] = '13411111111'
            testCase_13Param['specialTrade.type.id'] =  CommonIntf.getIdByDomainAndDisplayName(domainName='特种行业类型', displayName='旅馆')
            testCase_13Param['specialTrade.legalPerson'] = '测试法人代表'
            testCase_13Param['mode'] = 'add'
            testCase_13Param['specialTrade.organization.orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
            responseDict = ZuZhiChangSuoIntf.addTeZhongHangYe(TeZhongHangYeDict=testCase_13Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增失败')  
            #         新增其他场所
            testCase_14Param = copy.deepcopy(ZuZhiChangSuoPara.addQiTaChangSuo) 
            testCase_14Param['organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
            testCase_14Param['otherLocale.name'] = '测试场所名称%s' % CommonUtil.createRandomString()
            testCase_14Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
            testCase_14Param['otherLocale.type.id'] =  CommonIntf.getIdByDomainAndDisplayName(domainName='其他场所类型', displayName='个体诊所')
            testCase_14Param['mode'] = 'add'
            responseDict = ZuZhiChangSuoIntf.addQiTaChangSuo(QiTaChangSuoDict=testCase_14Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增失败')     
            #验证新增实有人口统计数据
            checkPara11={
                       'orgName':orgInit['DftWangGeOrg'],
                       'householdStaffNum':9,#户籍人口
                       'floatingPopulationNum':1,#流动人口
                       'overseaPersonNum':1,#境外
                       'unsettledPopulationNum':1,#未落户
                       'subtotal':12#小计
                       }
            checkPara12={
                       'orgName':'合计',
                       'householdStaffNum':9,#户籍人口
                       'floatingPopulationNum':1,#流动人口
                       'overseaPersonNum':1,#境外
                       'unsettledPopulationNum':1,#未落户
                       'subtotal':12#小计                            
                        }
            listPara={
                        'newQueryVo.orgId':orgInit['DftSheQuOrgId'],
                        'newQueryVo.startDate':Time.getCurrentDate(),
                        'newQueryVo.endDate':Time.getCurrentDate(),
                        'newQueryVo.startHours':'00',
                        'newQueryVo.startMinute':'00',
                        'newQueryVo.endHours':'24',
                        'newQueryVo.endMinute':'00',
                        'newQueryVo.queryType':'1',
                      }
            res11=checkDictInActualPopulationStatics(checkpara=checkPara11,listpara=listPara)
            res12=checkDictInActualPopulationStatics(checkpara=checkPara12,listpara=listPara)
            self.assertTrue(res11, '新增+更新小计验证通过')
            self.assertTrue(res12, '新增+更新合计验证通过')
            Log.LogOutput( message='新增+更新实有人口统计结果验证通过')
            #验证新增重点人员统计结果
            #小计
            checkPara21={
                        "dangerousGoodsPractitionerNum": 1,
                        "druggyNum": 1,
                        "idleYouthNum": 1,
                        "mentalPatientNum": 1,
                        "orgName": orgInit['DftWangGeOrg'],
                        "otherAttentionPersonnelNum": 1,
                        "positiveinfoNum": 1,
                        "rectificativePersonNum": 1,
                        "subtotal": 8,
                        "superiorVisitNum": 1
            }
            #合计
            checkPara22={
                        "dangerousGoodsPractitionerNum": 1,
                        "druggyNum": 1,
                        "idleYouthNum": 1,
                        "mentalPatientNum": 1,
                        "orgName":'合计',
                        "otherAttentionPersonnelNum": 1,
                        "positiveinfoNum": 1,
                        "rectificativePersonNum": 1,
                        "subtotal": 8,
                        "superiorVisitNum": 1
            }
            res21=checkDictInImportantPopulationStatics(checkpara=checkPara21,listpara=listPara)
            res22=checkDictInImportantPopulationStatics(checkpara=checkPara22,listpara=listPara)
            self.assertTrue(res21, '新增+更新小计验证通过')
            self.assertTrue(res22, '新增+更新合计验证通过')
            Log.LogOutput( message='新增+更新重点人员统计结果验证通过')
            #验证实有房屋新增
            #小计
            checkPara31={
                        "houseInfoNum": 1,
                        "orgName": orgInit['DftWangGeOrg'],
                        "rentalHouseNum": 1,
                        "subtotal": 2
                         }
            checkPara32={
                        "houseInfoNum": 1,
                        "orgName": "合计",
                        "rentalHouseNum": 1,
                        "subtotal": 2
                         }
            res31=checkDictInActualHouseStatics(checkpara=checkPara31,listpara=listPara)
            res32=checkDictInActualHouseStatics(checkpara=checkPara32,listpara=listPara)
            self.assertTrue(res31, '新增小计验证通过')
            self.assertTrue(res32, '新增合计验证通过')
            Log.LogOutput( message='新增实有房屋统计结果验证通过')
            #组织场所
            checkPara41={
                        "commonComplexPlaceNum": 1,
                        "dangerousChemicalsUnitNum": 1,
                        "fireSafetyNum": 1,
                        "hospitalNum": 1,
                        "internetBarNum": 1,
                        "orgName": orgInit['DftWangGeOrg'],
                        "otherLocaleNum": 1,
                        "publicPlaceNum": 1,
                        "safetyProductionNum": 1,
                        "schoolNum": 1,
                        "securityNum": 1,
                        "specialTradeNum": 1,
                        "subtotal": 11                             
                         }
            checkPara42={
                        "commonComplexPlaceNum": 1,
                        "dangerousChemicalsUnitNum": 1,
                        "fireSafetyNum": 1,
                        "hospitalNum": 1,
                        "internetBarNum": 1,
                        "orgName": "合计",
                        "otherLocaleNum": 1,
                        "publicPlaceNum": 1,
                        "safetyProductionNum": 1,
                        "schoolNum": 1,
                        "securityNum": 1,
                        "specialTradeNum": 1,
                        "subtotal": 11                             
                         }
            res41=checkDictInImportantPlaceStatics(checkpara=checkPara41,listpara=listPara)
            res42=checkDictInImportantPlaceStatics(checkpara=checkPara42,listpara=listPara)
            self.assertTrue(res41, '新增小计验证通过')
            self.assertTrue(res42, '新增合计验证通过')
            Log.LogOutput( message='新增重点场所统计结果验证通过')                 
            pass    

    '''
    @功能：研判分析-综合信息查询-综合新增查询
    @ chenhui 2016-6-3
    '''
    def testStatus_014(self):
        '''新增+更新统计'''
        #仿真环境下跳过测试
        if simulationEnvironment is True:
            pass
        else:
            ShiYouRenKouIntf.deleteAllPopulation()
            ShiYouFangWuIntf.deleteAllActualHouse()
            ZuZhiChangSuoIntf.deleteAllPopulation()
            
            #新增并修改
            #户籍人口
            HuJiParam_03 = copy.deepcopy(ShiYouRenKouPara.populationObject) 
            HuJiParam_03['mode']='add'
            HuJiParam_03['population.organization.id'] = orgInit['DftWangGeOrgId']
            HuJiParam_03['population.organization.orgName'] = orgInit['DftWangGeOrg']
            HuJiParam_03['population.idCardNo'] = '111111111111130'
            HuJiParam_03['population.name'] = 'test3'
            HuJiParam_03['population.isHaveHouse1'] = 'null'         
            responseDict = ShiYouRenKouIntf.add_HuJiRenKou(HuJiRenKouDict=HuJiParam_03, username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增户籍人口失败')
            
            editParam = copy.deepcopy(ShiYouRenKouPara.populationObject) 
            editParam['mode']='edit'
            editParam['population.id']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from householdstaffs t where t.idcardno='%s' and t.name='%s'" % (HuJiParam_03['population.idCardNo'],HuJiParam_03['population.name']))
            editParam['population.organization.id'] = HuJiParam_03['population.organization.id']
            editParam['population.organization.orgName'] = HuJiParam_03['population.organization.orgName']  
            editParam['population.idCardNo'] = HuJiParam_03['population.idCardNo']
            editParam['population.name'] = '测试'
            editParam['population.isHaveHouse1'] = 'null'    
            responseDict = ShiYouRenKouIntf.edit_ShiYouRenKou(HuJiRenKouDict=editParam, username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '修改户籍人口失败')
            #流动人口
            LiuDongParam_01 = copy.deepcopy(ShiYouRenKouPara.populationObject) 
            LiuDongParam_01['population.organization.id'] = orgInit['DftWangGeOrgId']
            LiuDongParam_01['population.actualPopulationType'] = 'floatingPopulation'
            LiuDongParam_01['population.organization.orgName'] = orgInit['DftWangGeOrg']
            LiuDongParam_01['population.idCardNo'] = '111111111111111'
            LiuDongParam_01['population.name'] = 'test'+createRandomString()
            LiuDongParam_01['population.isHaveHouse1'] = 'null'
            LiuDongParam_01['population.nativePlaceAddress']='户籍详址'+createRandomString()
            LiuDongParam_01['population.usedName']='别名'+createRandomString()
            responseDict = ShiYouRenKouIntf.add_LiuDongRenKou(LiuDongRenKouDict=LiuDongParam_01, username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增流动人口失败')
            updPara=copy.deepcopy(ShiYouRenKouPara.populationObject)
            updPara['mode']='edit'
            updPara['population.id']=json.loads(responseDict.text)['id']
            updPara['population.organization.id']=LiuDongParam_01['population.organization.id']
            updPara['population.actualPopulationType']=LiuDongParam_01['population.actualPopulationType'] 
            updPara['population.organization.orgName']=LiuDongParam_01['population.organization.orgName']
            updPara['population.idCardNo']=LiuDongParam_01['population.idCardNo']
            updPara['population.name']=LiuDongParam_01['population.name']+'修改'
            updPara['population.isHaveHouse1']='null'
            res1=ShiYouRenKouIntf.upd_LiuDongRenKou(para=updPara)
            self.assertTrue(res1.result, '修改流动人口失败')        
            #未落户
            WeiLuoHuParam_01 = copy.deepcopy(ShiYouRenKouPara.unsettledPopulationObject) 
            WeiLuoHuParam_01['mode'] = 'success'
            WeiLuoHuParam_01['ownerOrg.id'] = orgInit['DftWangGeOrgId']
            WeiLuoHuParam_01['unsettledPopulation.organization.id'] = orgInit['DftWangGeOrgId']
            WeiLuoHuParam_01['unsettledPopulation.organization.orgName'] = orgInit['DftWangGeOrg']
            WeiLuoHuParam_01['unsettledPopulation.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
            WeiLuoHuParam_01['unsettledPopulation.idCardNo'] = '111111111110001'
            WeiLuoHuParam_01['unsettledPopulation.name'] = 'test001'+createRandomString()
            WeiLuoHuParam_01['unsettledPopulation.isHaveHouse1'] = 'null'         
            responseDict = ShiYouRenKouIntf.add_WeiLuoHuRenKou(WeiLuoHuRenKouDict=WeiLuoHuParam_01, username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增未落户人口失败') 
            WeiLuoHuParam_01['mode']='edit'
            WeiLuoHuParam_01['unsettledPopulation.id']=json.loads(responseDict.text)['id']
            WeiLuoHuParam_01['unsettledPopulation.idCardNo']='111111111110002'
            WeiLuoHuParam_01['unsettledPopulation.name']='test002'+createRandomString()
            responseDict = ShiYouRenKouIntf.add_WeiLuoHuRenKou(WeiLuoHuRenKouDict=WeiLuoHuParam_01, username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '修改未落户人口失败')            
            #境外人员
            JingWaiParam_01 = copy.deepcopy(ShiYouRenKouPara.overseaPopulationObject) 
            JingWaiParam_01['mode'] = 'success'
            JingWaiParam_01['overseaPersonnel.organization.id'] = orgInit['DftWangGeOrgId']
            JingWaiParam_01['overseaPersonnel.englishName'] = 'www'
            JingWaiParam_01['overseaPersonnel.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
            JingWaiParam_01['overseaPersonnel.certificateType.id'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from propertydicts t where t.displayname='旅游证'" )
            JingWaiParam_01['overseaPersonnel.certificateNo'] = '343'
            JingWaiParam_01['overseaPersonnel.isHaveHouse1'] = 'null'         
            responseDict = ShiYouRenKouIntf.add_JingWaiRenKou(JingWaiRenKouDict=JingWaiParam_01, username=userInit['DftWangGeUser'], password='11111111') 
            self.assertTrue(responseDict.result, '新增境外人口失败') 
            JingWaiParam_01['overseaPersonnel.id']=json.loads(responseDict.text)['id']
            JingWaiParam_01['overseaPersonnel.englishName']='upd'+createRandomString()
            JingWaiParam_01['certificateType']=CommonIntf.getDbQueryResult(dbCommand="select t.id from propertydicts t where t.displayname='港澳出入证'" )
            JingWaiParam_01['certificateNo']='123456'
            #修改境外人员，与新增是同一接口
            responseDict = ShiYouRenKouIntf.add_JingWaiRenKou(JingWaiRenKouDict=JingWaiParam_01, username=userInit['DftWangGeUser'], password='11111111') 
            self.assertTrue(responseDict.result, '修改境外人口失败')
            #刑满释放人员
            xingShiParam_17 = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
            xingShiParam_17['mode']='add'
            xingShiParam_17['population.organization.id'] = orgInit['DftWangGeOrgId']
            xingShiParam_17['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人口or流动人口
            xingShiParam_17['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['xingManShiFangRenYuan']
            xingShiParam_17['population.organization.orgName'] = orgInit['DftWangGeOrg']
            xingShiParam_17['population.idCardNo'] = '331100199711220001'
            xingShiParam_17['population.name'] = '刑满释放人员'
            xingShiParam_17['actualPersonType'] = xingShiParam_17['population.actualPopulationType']
            xingShiParam_17['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
            xingShiParam_17['population.isHaveHouse1'] = 'null'   
            xingShiParam_17['population.caseReason'] = 'Reason'
            xingShiParam_17['population.positiveInfoType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '刑释人员'") 
            xingShiParam_17['population.laborEduAddress'] = '劳教所'
            xingShiParam_17['population.imprisonmentDate'] = '2weeks'
            xingShiParam_17['population.releaseOrBackDate'] = '2015-12-01'          
            responseDict = ShiYouRenKouIntf.add_xingManShiFang(xingManShiFangDict=xingShiParam_17, username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增刑满释放人员失败')
            updPara=copy.deepcopy(xingShiParam_17)
            updPara['mode']='edit'
            updPara['population.id']=json.loads(responseDict.text)['id']
            updPara['population.idCardNo']='331100199711220001'
            updPara['population.birthday']='1997-11-22'
            updPara['population.name']=xingShiParam_17['population.name']+createRandomString()
            updPara['population.releaseOrBackDate']='2016-1-1'
            updPara['population.laborEduAddress']=xingShiParam_17['population.laborEduAddress']+createRandomString()
            updPara['population.caseReason']=xingShiParam_17['population.caseReason']+createRandomString()
            updPara['population.imprisonmentDate']=xingShiParam_17['population.imprisonmentDate']+createRandomString()
            res1 = ShiYouRenKouIntf.add_xingManShiFang(xingManShiFangDict=updPara, username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(res1.result, '修改刑满释放人员失败')        
            #矫正人员
            jiaoZhengParam_17 = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
            jiaoZhengParam_17['mode']='add'
            jiaoZhengParam_17['population.organization.id'] = orgInit['DftWangGeOrgId']
            jiaoZhengParam_17['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人口or流动人口
            jiaoZhengParam_17['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['sheQuJiaoZhengRenYuan']
            jiaoZhengParam_17['population.organization.orgName'] = orgInit['DftWangGeOrg']
            jiaoZhengParam_17['population.idCardNo'] = '331100199711200002'
            jiaoZhengParam_17['population.name'] = '矫正人员'
            jiaoZhengParam_17['actualPersonType'] = jiaoZhengParam_17['population.actualPopulationType']
            jiaoZhengParam_17['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
            jiaoZhengParam_17['population.isHaveHouse1'] = 'null'   
            jiaoZhengParam_17['population.accusation'] = '矫正罪名'
            jiaoZhengParam_17['population.executeType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '监外执行罪犯'") 
            jiaoZhengParam_17['population.rectifyStartDate'] = '2015-12-01'
            jiaoZhengParam_17['population.rectifyEndDate'] = '2015-12-31'  
            responseDict = ShiYouRenKouIntf.add_sheQuJiaoZheng(sheQuJiaoZhengDict=jiaoZhengParam_17, username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增社区矫正人员失败')
            updPara=copy.deepcopy(jiaoZhengParam_17)
            updPara['mode']='edit'
            updPara['population.id']=json.loads(responseDict.text)['id']
            updPara['population.name']='矫正人员'+createRandomString()
            updPara['population.accusation']='矫正罪名'+createRandomString()
            updPara['population.usedName']='曾用名'+createRandomString()
            responseDict = ShiYouRenKouIntf.add_sheQuJiaoZheng(sheQuJiaoZhengDict=updPara, username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增社区矫正人员失败')       
            #精神病人员
            psychosisParam_17= copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
            psychosisParam_17['mode']='add'
            psychosisParam_17['population.organization.id'] = orgInit['DftWangGeOrgId']
            psychosisParam_17['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人口or流动人口
            psychosisParam_17['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['jingShenBingRenYuan']
            psychosisParam_17['population.organization.orgName'] = orgInit['DftWangGeOrg']
            psychosisParam_17['population.idCardNo'] = '332200199711220000'
            psychosisParam_17['population.name'] = '精神病人员'
            psychosisParam_17['actualPersonType'] = psychosisParam_17['population.actualPopulationType']
            psychosisParam_17['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
            psychosisParam_17['population.isHaveHouse1'] = 'null'   
            psychosisParam_17['population.dangerLevel.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='危险程度', displayName='低')   
            responseDict = ShiYouRenKouIntf.add_jingShengBingRenYuan(psychosisDict=psychosisParam_17, username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增精神病人员失败')  
            updPara=copy.deepcopy(psychosisParam_17)
            updPara['mode']='edit'
            updPara['population.id']=json.loads(responseDict.text)['id']
            updPara['population.name']='精神病人员'+createRandomString()
            updPara['population.dangerLevel.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='危险程度', displayName='中')
            responseDict = ShiYouRenKouIntf.add_jingShengBingRenYuan(psychosisDict=updPara, username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '修改精神病人员失败')
            #吸毒人员
            xiDuParam_17 = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
            xiDuParam_17['mode']='add'
            xiDuParam_17['population.organization.id'] = orgInit['DftWangGeOrgId']
            xiDuParam_17['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于会人口or流动人口
            xiDuParam_17['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['xiDuRenYuan']
            xiDuParam_17['population.organization.orgName'] = orgInit['DftWangGeOrg']
            xiDuParam_17['population.idCardNo'] = '333300199711220000'
            xiDuParam_17['population.name'] = '吸毒人员'
            xiDuParam_17['actualPersonType'] = xiDuParam_17['population.actualPopulationType']
            xiDuParam_17['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
            xiDuParam_17['population.isHaveHouse1'] = 'null'   
            xiDuParam_17['population.detoxicateCase.id'] = CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '强制戒毒'")  
            responseDict = ShiYouRenKouIntf.add_xiDuRenYuan(xiDuRenYuanDict=xiDuParam_17, username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增吸毒人员失败') 
            updPara=copy.deepcopy(xiDuParam_17)
            updPara['mode']='edit'
            updPara['population.id']=json.loads(responseDict.text)['id']
            updPara['population.name']='吸毒人员'+createRandomString()
            updPara['population.detoxicateCase.id'] = CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '自愿戒毒'")  
            responseDict = ShiYouRenKouIntf.add_xiDuRenYuan(xiDuRenYuanDict=updPara, username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '修改吸毒人员失败')
            #重点青少年
            ShiYouRenKouIntf.zhongDianQingShaoNianDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
            qingShaoNianParam_17 = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
            qingShaoNianParam_17['mode']='add'
            qingShaoNianParam_17['population.organization.id'] = orgInit['DftWangGeOrgId']
            qingShaoNianParam_17['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人口or流动人口
            qingShaoNianParam_17['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['zhongDianQingShaoNian']
            qingShaoNianParam_17['population.organization.orgName'] = orgInit['DftWangGeOrg']
            qingShaoNianParam_17['population.idCardNo'] = '334400199711220000'
            qingShaoNianParam_17['population.name'] = '重点青少年'
            qingShaoNianParam_17['actualPersonType'] = qingShaoNianParam_17['population.actualPopulationType']
            qingShaoNianParam_17['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
            qingShaoNianParam_17['population.isHaveHouse1'] = 'null'  
            qingShaoNianParam_17['staffTypeIds'] =CommonIntf.getIdByDomainAndDisplayName(domainName='闲散青少年人员类型', displayName='闲散青少年')     #人员类型，根据字段找对应id    
            responseDict = ShiYouRenKouIntf.add_zhongDianQingShaoNian(qingShaoNianDict=qingShaoNianParam_17, username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增重点青少年失败') 
            updPara=copy.deepcopy(qingShaoNianParam_17)
            updPara['mode']='edit'
            updPara['population.id']=json.loads(responseDict.text)['id']
            updPara['population.name']='重点青少年'+createRandomString()
            updPara['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='女')
            responseDict = ShiYouRenKouIntf.add_zhongDianQingShaoNian(qingShaoNianDict=updPara, username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '修改重点青少年失败')
            #重点上访人员
            shangFangParam_17 = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
            shangFangParam_17['mode']='add'
            shangFangParam_17['population.organization.id'] = orgInit['DftWangGeOrgId']
            shangFangParam_17['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人员or流动人口
            shangFangParam_17['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['zhongDianShangFangRenYuan']
            shangFangParam_17['population.organization.orgName'] = orgInit['DftWangGeOrg']
            shangFangParam_17['population.idCardNo'] = '335500199711220000'
            shangFangParam_17['population.name'] = '重点上访人员'
            shangFangParam_17['actualPersonType'] = shangFangParam_17['population.actualPopulationType']
            shangFangParam_17['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
            shangFangParam_17['population.isHaveHouse1'] = 'null'   
            shangFangParam_17['population.visitReason'] = '上访原因'       
            responseDict = ShiYouRenKouIntf.add_shangFangRenYuan(shangFangDict=shangFangParam_17, username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增上访人员失败')
            updPara=copy.deepcopy(shangFangParam_17)
            updPara['mode']='edit'
            updPara['population.id']=json.loads(responseDict.text)['id']
            updPara['population.name']='重点上访人员'+createRandomString()
            updPara['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='女')
            responseDict = ShiYouRenKouIntf.add_shangFangRenYuan(shangFangDict=updPara, username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '修改重点上访人员失败')
            #危险品从业人员
            practitionerParam_17 = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
            practitionerParam_17['mode']='add'
            practitionerParam_17['population.organization.id'] = orgInit['DftWangGeOrgId']
            practitionerParam_17['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']   #属于户籍人员or流动人员
            practitionerParam_17['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['weiXianPingCongYeRenYuan']
            practitionerParam_17['population.organization.orgName'] = orgInit['DftWangGeOrg']
            practitionerParam_17['population.idCardNo'] = '336600199711220000'
            practitionerParam_17['population.name'] = '危险品从业人员'
            practitionerParam_17['actualPersonType'] = practitionerParam_17['population.actualPopulationType']
            practitionerParam_17['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
            practitionerParam_17['population.isHaveHouse1'] = 'null'   
            practitionerParam_17['population.dangerousWorkingType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='危险从业类别', displayName='其他')  #危险从业类别，选择id
            practitionerParam_17['population.legalPerson'] = '法人代表'  
            practitionerParam_17['population.legalPersonMobileNumber'] = '11111111111' 
            practitionerParam_17['population.legalPersonTelephone'] = '3333333'  
            practitionerParam_17['population.workUnit'] = '工作单位'       
            responseDict = ShiYouRenKouIntf.add_weiXianPingCongYeRenYuan(practitionerDict=practitionerParam_17, username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增危险品从业人员失败')
            updPara=copy.deepcopy(practitionerParam_17)
            updPara['mode']='edit'
            updPara['population.id']=json.loads(responseDict.text)['id']
            updPara['population.name']='危险品从业人员'+createRandomString()
            updPara['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='女')
            responseDict = ShiYouRenKouIntf.add_weiXianPingCongYeRenYuan(updPara, username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '修改危险品从业人员失败')
            #其他人员
            otherParam_17 = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
            otherParam_17['mode']='add'
            otherParam_17['population.organization.id'] = orgInit['DftWangGeOrgId']
            otherParam_17['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人员or流动人员
            otherParam_17['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['qiTaRenYuan']
            otherParam_17['population.organization.orgName'] = orgInit['DftWangGeOrg']
            otherParam_17['population.idCardNo'] = '337700199711220000'
            otherParam_17['population.name'] = '其他人员'
            otherParam_17['actualPersonType'] = otherParam_17['population.actualPopulationType']
            otherParam_17['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
            otherParam_17['population.isHaveHouse1'] = 'null'   
            otherParam_17['population.attentionExtent.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='关注程度', displayName='一般')  #关注程度，选择id，可以不填
            otherParam_17['population.attentionReason'] = '关注原因'   #可以不填      
            responseDict = ShiYouRenKouIntf.add_qiTaRenYuan(otherDict=otherParam_17, username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增其他人员失败')
            updPara=copy.deepcopy(otherParam_17)
            updPara['mode']='edit'
            updPara['population.id']=json.loads(responseDict.text)['id']
            updPara['population.name']='其他人员'+createRandomString()
            updPara['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='女')
            responseDict = ShiYouRenKouIntf.add_qiTaRenYuan(updPara, username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '修改其他人员失败')
            #实有房屋和出租房
            houseParam_04 = copy.deepcopy(ShiYouFangWuPara.houseObject) 
            houseParam_04['dailogName']='actualHouseMaintanceDialog'
            houseParam_04['houseInfo.organization.id'] = orgInit['DftWangGeOrgId']
            houseParam_04['mode']='add'
            houseParam_04['isUseFrom'] = 'actualHouse'
            houseParam_04['houseInfo.organization.orgName'] = orgInit['DftWangGeOrg']
            houseParam_04['houseInfo.addressType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '现居住址类型') and p.displayname = '其他'")
            houseParam_04['currentAddressType'] = houseParam_04['houseInfo.addressType.id']    
            houseParam_04['houseInfo.address'] = '新增房屋%s'%CommonUtil.createRandomString() 
            houseParam_04['houseInfo.isRentalHouse'] = 'false'      
            responseDict = ShiYouFangWuIntf.add_ShiYouFangWu(fangWuDict=houseParam_04, username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增实有房屋失败')  
            
            editParam_04 = copy.deepcopy(ShiYouFangWuPara.houseObject) 
            editParam_04['dailogName']=houseParam_04['dailogName']
            editParam_04['houseInfo.organization.id'] = houseParam_04['houseInfo.organization.id'] 
            editParam_04['mode']='edit'
            editParam_04['houseInfo.id']=CommonIntf.getDbQueryResult(dbCommand = "select t.id from houseInfo t where t.address='%s'" % (houseParam_04['houseInfo.address']))
            editParam_04['isUseFrom'] = 'actualHouse'
            editParam_04['houseInfo.organization.orgName'] = orgInit['DftWangGeOrg']
            editParam_04['houseInfo.addressType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '现居住址类型') and p.displayname = '其他'")
            editParam_04['currentAddressType'] = editParam_04['houseInfo.addressType.id']   
            editParam_04['houseInfo.address'] = '修改为出租房%s'%CommonUtil.createRandomString() 
            editParam_04['houseInfo.isRentalHouse'] = 'true'    
            editParam_04['houseInfo.rentalPerson'] = '房东信息'  
            editParam_04['houseInfo.rentalType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='出租房类别', displayName='套房') 
            editParam_04['houseInfo.hiddenDangerLevel.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='隐患程度', displayName='安全') 
            responseDict = ShiYouFangWuIntf.edit_ShiYouFangWu(editDict=editParam_04, username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '修改实有房屋失败') 
            #安全生产重点
            testCase_04Param = copy.deepcopy(ZuZhiChangSuoPara.addAnQuanShengChan) 
            testCase_04Param['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
            testCase_04Param['enterprise.name'] = '测试安全生产重点%s' % CommonUtil.createRandomString()
            testCase_04Param['enterprise.keyType'] = 'safetyProductionKey'
            testCase_04Param['mode'] = 'add'
            testCase_04Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
            testCase_04Param['placeTypeName'] = '安全生产重点'
            testCase_04Param['enterprise.address'] = '测试地址1'
            testCase_04Param['enterprise.legalPerson'] = '法人代表1'
            testCase_04Param['enterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='企业类型', displayName='规上企业')
            responseDict = ZuZhiChangSuoIntf.addAnQuanShengChan(AnQuanShengChanDict=testCase_04Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增失败')
            testCase_05Param = copy.deepcopy(ZuZhiChangSuoPara.UpdateAnQuanShengChan) 
            testCase_05Param['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
            testCase_05Param['enterprise.name'] = '测试安全生产重点1%s' % CommonUtil.createRandomString()
            testCase_05Param['enterprise.keyType'] = 'safetyProductionKey'
            testCase_05Param['mode'] = 'edit'
            testCase_05Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
            testCase_05Param['placeTypeName'] = '安全生产重点'
            testCase_05Param['enterprise.address'] = '测试地址1'
            testCase_05Param['enterprise.legalPerson'] = '法人代表1'
            testCase_05Param['enterprise.id'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from ENTERPRISES t where t.name='%s' and t.keytype='%s'"%(testCase_04Param['enterprise.name'] ,testCase_05Param['enterprise.keyType'] ))
            testCase_05Param['enterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='企业类型', displayName='规上企业')
            responseDict = ZuZhiChangSuoIntf.UpdateAnQuanShengChan(AnQuanShengChanDict=testCase_05Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '修改失败')
            #消防安全重点
            testCase_05Param = copy.deepcopy(ZuZhiChangSuoPara.addXiaoFangAnQuan) 
            testCase_05Param['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
            testCase_05Param['enterprise.name'] = '测试场所名称%s' % CommonUtil.createRandomString()
            testCase_05Param['enterprise.keyType'] = 'fireSafetyKey'
            testCase_05Param['mode'] = 'add'
            testCase_05Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
            testCase_05Param['placeTypeName'] = '消防安全重点'
            testCase_05Param['enterprise.address'] = '测试场所地址1'
            testCase_05Param['enterprise.legalPerson'] = '测试负责人'
            testCase_05Param['enterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='消防安全重点类别', displayName='商场')
            responseDict = ZuZhiChangSuoIntf.addXiaoFangAnQuan(XiaoFangAnQuanDict=testCase_05Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增失败') 
            testCase_06Param = copy.deepcopy(ZuZhiChangSuoPara.UpdateXiaoFangAnQuan) 
            testCase_06Param['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
            testCase_06Param['enterprise.name'] = '测试场所名称1%s' % CommonUtil.createRandomString()
            testCase_06Param['enterprise.keyType'] = 'fireSafetyKey'
            testCase_06Param['mode'] = 'edit'
            testCase_06Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
            testCase_06Param['placeTypeName'] = '消防安全重点'
            testCase_06Param['enterprise.address'] = '测试场所地址1'
            testCase_06Param['enterprise.legalPerson'] = '测试负责人'
            testCase_06Param['enterprise.id'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from ENTERPRISES t where t.name='%s' and t.keytype='%s'"%(testCase_05Param['enterprise.name'] ,testCase_05Param['enterprise.keyType']  ))
            testCase_06Param['enterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='消防安全重点类别', displayName='商场')
            responseDict = ZuZhiChangSuoIntf.UpdateXiaoFangAnQuan(XiaoFangAnQuanDict=testCase_06Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '修改失败')  
    #         新增治安重点
            testCase_06Param = copy.deepcopy(ZuZhiChangSuoPara.addZhiAnZhongDian) 
            testCase_06Param['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
            testCase_06Param['enterprise.name'] = '测试场所名称%s' % CommonUtil.createRandomString()
            testCase_06Param['enterprise.keyType'] = 'securityKey'
            testCase_06Param['mode'] = 'add'
            testCase_06Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
            testCase_06Param['placeTypeName'] = '治安重点'
            testCase_06Param['enterprise.address'] = '测试场所地址1'
            testCase_06Param['enterprise.legalPerson'] = '测试负责人'
            testCase_06Param['enterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='治安重点类别', displayName='城乡结合部')
            responseDict = ZuZhiChangSuoIntf.addZhiAnZhongDian(ZhiAnZhongDianDict=testCase_06Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增失败') 
    #         修改治安重点
            testCase_07Param = copy.deepcopy(ZuZhiChangSuoPara.UpdateZhiAnZhongDian) 
            testCase_07Param['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
            testCase_07Param['enterprise.name'] = '测试场所名称%s' % CommonUtil.createRandomString()
            testCase_07Param['enterprise.keyType'] = 'securityKey'
            testCase_07Param['mode'] = 'add'
            testCase_07Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
            testCase_07Param['placeTypeName'] = '治安重点'
            testCase_07Param['enterprise.address'] = '测试场所地址1'
            testCase_07Param['enterprise.legalPerson'] = '测试负责人'
            testCase_07Param['enterprise.id'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from ENTERPRISES t where t.name='%s' and t.keytype='%s'"%(testCase_06Param['enterprise.name'] ,testCase_06Param['enterprise.keyType']  ))
            testCase_07Param['enterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='治安重点类别', displayName='城乡结合部')
            responseDict = ZuZhiChangSuoIntf.UpdateZhiAnZhongDian(ZhiAnZhongDianDict=testCase_07Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '修改失败')  
    #         新增学校
            testCase_07Param = copy.deepcopy(ZuZhiChangSuoPara.addXueXiao) 
            testCase_07Param['orgId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
            testCase_07Param['school.chineseName'] = '测试学校名称%s' % CommonUtil.createRandomString()
            testCase_07Param['school.kind.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='学校性质', displayName='公办')
            testCase_07Param['mode'] = 'add'
            testCase_07Param['school.hasCertificate'] = '请选择'
            testCase_07Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
            testCase_07Param['placeTypeName'] = '学校'
            testCase_07Param['school.address'] = '测试学校地址1'
            testCase_07Param['school.president'] = '测试校长'
            testCase_07Param['school.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='学校类型', displayName='小学')
            responseDict = ZuZhiChangSuoIntf.addXueXiao(XueXiaoDict=testCase_07Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增失败')
            testCase_08Param = copy.deepcopy(ZuZhiChangSuoPara.UpdateXueXiao) 
            testCase_08Param['orgId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
            testCase_08Param['school.chineseName'] = '测试学校名称11%s' % CommonUtil.createRandomString()
            testCase_08Param['school.kind.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='学校性质', displayName='公办')
            testCase_08Param['mode'] = 'edit'
            testCase_08Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
            testCase_08Param['placeTypeName'] = '学校'
            testCase_08Param['school.address'] = '测试学校地址1'
            testCase_08Param['school.president'] = '测试校长'
            testCase_08Param['school.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='学校类型', displayName='小学')
            testCase_08Param['school.orgInternalCode'] =CommonIntf.getDbQueryResult(dbCommand="select t.orginternalcode from SCHOOLS t where t.chinesename='%s'"%testCase_07Param['school.chineseName'] )
            testCase_08Param['school.organization.id'] =InitDefaultPara.orgInit['DftWangGeOrgId']
            testCase_08Param['school.createUser'] =InitDefaultPara.userInit['DftWangGeUser']
            testCase_08Param['school.createDate'] =Time.getCurrentDateAndTime()
            testCase_08Param['school.hasCertificate'] ='false'
            testCase_08Param['school.id'] =CommonIntf.getDbQueryResult(dbCommand="select t.id from SCHOOLS t where t.chinesename='%s'"%testCase_07Param['school.chineseName'] )
            responseDict = ZuZhiChangSuoIntf.UpdateXueXiao(XueXiaoDict=testCase_08Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '修改失败') 
    #         新增医院
            testCase_08Param = copy.deepcopy(ZuZhiChangSuoPara.addYiYuan) 
            testCase_08Param['organizationId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
            testCase_08Param['hospital.hospitalName'] = '测试医院名称%s' % CommonUtil.createRandomString()
            testCase_08Param['hospital.personLiableTelephone'] = '1234-12341234'
            testCase_08Param['mode'] = 'add'
            testCase_08Param['hospital.organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
            testCase_08Param['hospital.personLiableMobileNumber'] = '13411111111'
            testCase_08Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
            testCase_08Param['hospital.address'] = '测试医院地址1'
            testCase_08Param['hospital.personLiable'] = '测试综治负责人'
            responseDict = ZuZhiChangSuoIntf.addYiYuan(YiYuanDict=testCase_08Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增失败') 
            testCase_09Param = copy.deepcopy(ZuZhiChangSuoPara.UpdateYiYuan) 
            testCase_09Param['organizationId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
            testCase_09Param['hospital.hospitalName'] = '测试医院名称11%s' % CommonUtil.createRandomString()
            testCase_09Param['hospital.personLiableTelephone'] = '1234-12341234'
            testCase_09Param['mode'] = 'edit'
            testCase_09Param['hospital.id'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from hospitals t where t.hospitalname='%s'"%testCase_08Param['hospital.hospitalName'])
            testCase_09Param['hospital.organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
            testCase_09Param['hospital.personLiableMobileNumber'] = '13411111111'
            testCase_09Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
            testCase_09Param['hospital.address'] = '测试医院地址1'
            testCase_09Param['hospital.personLiable'] = '测试综治负责人'
            responseDict = ZuZhiChangSuoIntf.UpdateYiYuan(YiYuanDict=testCase_09Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '修改失败') 
    #         新增危险化学品单位
            testCase_09Param = copy.deepcopy(ZuZhiChangSuoPara.addWeiXianHuaXuePing) 
            testCase_09Param['organizationId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
            testCase_09Param['location.unitName'] = '测试单位名称%s' % CommonUtil.createRandomString()
            testCase_09Param['mode'] = 'add'
            testCase_09Param['location.organization.orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
            responseDict = ZuZhiChangSuoIntf.addWeiXianHuaXuePing(WeiXianHuaXuePingDict=testCase_09Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增失败')
            testCase_009Param = copy.deepcopy(ZuZhiChangSuoPara.UpdateWeiXianHuaXuePing) 
            testCase_009Param['organizationId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
            testCase_009Param['location.organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
            testCase_009Param['location.unitName'] = '测试单位名称11%s' % CommonUtil.createRandomString()
            testCase_009Param['mode'] = 'edit'
            testCase_009Param['location.id'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from DANGEROUSCHEMICALSUNIT t where t.unitname='%s'"%testCase_09Param['location.unitName'])
            testCase_009Param['location.organization.orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
            responseDict = ZuZhiChangSuoIntf.UpdateWeiXianHuaXuePing(WeiXianHuaXuePingDict=testCase_009Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '修改失败') 
    #         新增上网服务单位
            testCase_10Param = copy.deepcopy(ZuZhiChangSuoPara.addShangWanFuWu) 
            testCase_10Param['location.organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
            testCase_10Param['location.placeName'] = '测试单位名称%s' % CommonUtil.createRandomString()
            testCase_10Param['mode'] = 'add'
            testCase_10Param['ajaxUrl'] = '/baseinfo/internetBarManage/hasDuplicateInternetBarLocation.action'
            testCase_10Param['location.organization.orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
            responseDict = ZuZhiChangSuoIntf.addShangWanFuWu(ShangWanFuWuDict=testCase_10Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增失败')   
            testCase_100Param = copy.deepcopy(ZuZhiChangSuoPara.UpdateShangWanFuWu) 
            testCase_100Param['location.organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
            testCase_100Param['location.placeName'] = '测试单位名称11%s' % CommonUtil.createRandomString()
            testCase_100Param['mode'] = 'edit'
            testCase_100Param['location.id'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from INTERNETBAR t where t.placename='%s'"%testCase_10Param['location.placeName'])
            testCase_100Param['ajaxUrl'] = '/baseinfo/internetBarManage/hasDuplicateInternetBarLocation.action'
            testCase_100Param['location.organization.orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
            responseDict = ZuZhiChangSuoIntf.UpdateShangWanFuWu(ShangWanFuWuDict=testCase_100Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '修改失败') 
    #         新增公共场所
            testCase_11Param = copy.deepcopy(ZuZhiChangSuoPara.addShangWanFuWu) 
            testCase_11Param['location.organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
            testCase_11Param['location.placeName'] = '测试公共场所名称%s' % CommonUtil.createRandomString()
            testCase_11Param['location.placeAddress'] = '测试场所地址'
            testCase_11Param['mode'] = 'add'
            testCase_11Param['ajaxUrl'] = '/baseinfo/publicPlaceManage/hasDuplicatePublicPlaceLocation.action'
            testCase_11Param['location.organization.orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
            responseDict = ZuZhiChangSuoIntf.addGongGongChangSuo(GongGongChangSuoDict=testCase_11Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增失败') 
            testCase_111Param = copy.deepcopy(ZuZhiChangSuoPara.UpdateShangWanFuWu1) 
            testCase_111Param['location.organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
            testCase_111Param['location.placeName'] = '测试公共场所名称11%s' % CommonUtil.createRandomString()
            testCase_111Param['location.placeAddress'] = '测试场所地址'
            testCase_111Param['mode'] = 'edit'
            testCase_111Param['location.id'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from PUBLICPLACE t where t.placename='%s'"%testCase_11Param['location.placeName'])
            testCase_111Param['ajaxUrl'] = '/baseinfo/publicPlaceManage/hasDuplicatePublicPlaceLocation.action'
            testCase_111Param['location.organization.orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
            responseDict = ZuZhiChangSuoIntf.UpdateShangWanFuWu1(GongGongChangSuoDict=testCase_111Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '修改失败')
    #         新增公共复杂场所
            testCase_12Param = copy.deepcopy(ZuZhiChangSuoPara.addGongGongFuZaChangSuo) 
            testCase_12Param['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
            testCase_12Param['commonComplexPlace.name'] = '测试公共复杂场所名称%s' % CommonUtil.createRandomString()
            testCase_12Param['commonComplexPlace.legalPerson'] = '测试负责人'
            testCase_12Param['mode'] = 'add'
            testCase_12Param['commonComplexPlace_orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
            responseDict = ZuZhiChangSuoIntf.addGongGongFuZaChangSuo(GongGongFuZaChangSuoDict=testCase_12Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增失败') 
            testCase_122Param = copy.deepcopy(ZuZhiChangSuoPara.UpdateGongGongFuZaChangSuo) 
            testCase_122Param['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
            testCase_122Param['commonComplexPlace.name'] = '测试公共复杂场所名称11%s' % CommonUtil.createRandomString()
            testCase_122Param['commonComplexPlace.legalPerson'] = '测试负责人'
            testCase_122Param['mode'] = 'edit'
            testCase_122Param['commonComplexPlace.id'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from COMMONCOMPLEXPLACES t where t.name='%s'"%testCase_12Param['commonComplexPlace.name'] )
            testCase_122Param['commonComplexPlace_orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
            responseDict = ZuZhiChangSuoIntf.UpdateGongGongFuZaChangSuo(GongGongFuZaChangSuoDict=testCase_122Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '修改失败')
    #         新增特种行业
            testCase_13Param = copy.deepcopy(ZuZhiChangSuoPara.addGongGongFuZaChangSuo) 
            testCase_13Param['organizationId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
            testCase_13Param['specialTrade.name'] = '测试特种行业名称%s' % CommonUtil.createRandomString()
            testCase_13Param['specialTrade.personLiable'] = '测试负责人'
            testCase_13Param['specialTrade.address'] = '测试企业地址'
            testCase_13Param['specialTrade.organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
            testCase_13Param['specialTrade.personLiableTelephone'] = '0571-12345678'
            testCase_13Param['specialTrade.personLiableMobileNumber'] = '13411111111'
            testCase_13Param['specialTrade.type.id'] =  CommonIntf.getIdByDomainAndDisplayName(domainName='特种行业类型', displayName='旅馆')
            testCase_13Param['specialTrade.legalPerson'] = '测试法人代表'
            testCase_13Param['mode'] = 'add'
            testCase_13Param['specialTrade.organization.orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
            responseDict = ZuZhiChangSuoIntf.addTeZhongHangYe(TeZhongHangYeDict=testCase_13Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增失败')
            testCase_133Param = copy.deepcopy(ZuZhiChangSuoPara.updatetezhonghangye) 
            testCase_133Param['organizationId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
            testCase_133Param['specialTrade.name'] = '测试特种行业名称11%s' % CommonUtil.createRandomString()
            testCase_133Param['specialTrade.personLiable'] = '测试负责人'
            testCase_133Param['specialTrade.address'] = '测试企业地址'
            testCase_133Param['specialTrade.organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
            testCase_133Param['specialTrade.personLiableTelephone'] = '0571-12345678'
            testCase_133Param['specialTrade.personLiableMobileNumber'] = '13411111111'
            testCase_133Param['specialTrade.type.id'] =  CommonIntf.getIdByDomainAndDisplayName(domainName='特种行业类型', displayName='旅馆')
            testCase_133Param['specialTrade.legalPerson'] = '测试法人代表'
            testCase_133Param['mode'] = 'edit'
            testCase_133Param['specialTrade.id'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from SPECIALTRADES t where t.name='%s'"%testCase_13Param['specialTrade.name'] )
            testCase_133Param['specialTrade.organization.orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
            responseDict = ZuZhiChangSuoIntf.addTeZhongHangYe(TeZhongHangYeDict=testCase_133Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '修改失败')                        
    #         新增其他场所
            testCase_14Param = copy.deepcopy(ZuZhiChangSuoPara.addQiTaChangSuo) 
            testCase_14Param['organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
            testCase_14Param['otherLocale.name'] = '测试场所名称%s' % CommonUtil.createRandomString()
            testCase_14Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
            testCase_14Param['otherLocale.type.id'] =  CommonIntf.getIdByDomainAndDisplayName(domainName='其他场所类型', displayName='个体诊所')
            testCase_14Param['mode'] = 'add'
            responseDict = ZuZhiChangSuoIntf.addQiTaChangSuo(QiTaChangSuoDict=testCase_14Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增失败')             
            testCase_144Param = copy.deepcopy(ZuZhiChangSuoPara.UpdateQiTaChangSuo) 
            testCase_144Param['organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
            testCase_144Param['otherLocale.name'] = '测试场所名称11%s' % CommonUtil.createRandomString()
            testCase_144Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
            testCase_144Param['otherLocale.type.id'] =  CommonIntf.getIdByDomainAndDisplayName(domainName='其他场所类型', displayName='个体诊所')
            testCase_144Param['mode'] = 'edit'
            testCase_144Param['otherLocale.id'] =  CommonIntf.getDbQueryResult(dbCommand="select t.id from OTHERLOCALES t where t.name='%s'"%testCase_14Param['otherLocale.name'] )
            responseDict = ZuZhiChangSuoIntf.UpdateQiTaChangSuo(QiTaChangSuoDict=testCase_144Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '修改失败')
            #验证新增并修改后“新增+更新”统计数据是否正确
            checkPara11={
                       'orgName':orgInit['DftWangGeOrg'],
                       'householdStaffNum':9,#户籍人口
                       'floatingPopulationNum':1,#流动人口
                       'overseaPersonNum':1,#境外
                       'unsettledPopulationNum':1,#未落户
                       'subtotal':12#小计
                       }
            checkPara12={
                       'orgName':'合计',
                       'householdStaffNum':9,#户籍人口
                       'floatingPopulationNum':1,#流动人口
                       'overseaPersonNum':1,#境外
                       'unsettledPopulationNum':1,#未落户
                       'subtotal':12#小计                            
                        }
            listPara={
                        'newQueryVo.orgId':orgInit['DftSheQuOrgId'],
                        'newQueryVo.startDate':Time.getCurrentDate(),
                        'newQueryVo.endDate':Time.getCurrentDate(),
                        'newQueryVo.startHours':'00',
                        'newQueryVo.startMinute':'00',
                        'newQueryVo.endHours':'24',
                        'newQueryVo.endMinute':'00',
                        'newQueryVo.queryType':'2',
                      }
            res11=checkDictInActualPopulationStatics(checkpara=checkPara11,listpara=listPara)
            res12=checkDictInActualPopulationStatics(checkpara=checkPara12,listpara=listPara)
            self.assertTrue(res11, '新增+更新小计验证通过')
            self.assertTrue(res12, '新增+更新合计验证通过')
            Log.LogOutput( message='新增+更新实有人口统计结果验证通过')
            #验证新增重点人员统计结果
            #小计
            checkPara21={
                        "dangerousGoodsPractitionerNum": 1,
                        "druggyNum": 1,
                        "idleYouthNum": 1,
                        "mentalPatientNum": 1,
                        "orgName": orgInit['DftWangGeOrg'],
                        "otherAttentionPersonnelNum": 1,
                        "positiveinfoNum": 1,
                        "rectificativePersonNum": 1,
                        "subtotal": 8,
                        "superiorVisitNum": 1
            }
            #合计
            checkPara22={
                        "dangerousGoodsPractitionerNum": 1,
                        "druggyNum": 1,
                        "idleYouthNum": 1,
                        "mentalPatientNum": 1,
                        "orgName":'合计',
                        "otherAttentionPersonnelNum": 1,
                        "positiveinfoNum": 1,
                        "rectificativePersonNum": 1,
                        "subtotal": 8,
                        "superiorVisitNum": 1
            }
            res21=checkDictInImportantPopulationStatics(checkpara=checkPara21,listpara=listPara)
            res22=checkDictInImportantPopulationStatics(checkpara=checkPara22,listpara=listPara)
            self.assertTrue(res21, '新增+更新小计验证通过')
            self.assertTrue(res22, '新增+更新合计验证通过')
            Log.LogOutput( message='新增+更新重点人员统计结果验证通过')
            #验证实有房屋新增
            #小计
            checkPara31={
                        "houseInfoNum": 1,
                        "orgName": orgInit['DftWangGeOrg'],
                        "rentalHouseNum": 1,
                        "subtotal": 2
                         }
            checkPara32={
                        "houseInfoNum": 1,
                        "orgName": "合计",
                        "rentalHouseNum": 1,
                        "subtotal": 2
                         }
            res31=checkDictInActualHouseStatics(checkpara=checkPara31,listpara=listPara)
            res32=checkDictInActualHouseStatics(checkpara=checkPara32,listpara=listPara)
            self.assertTrue(res31, '新增+更新小计验证通过')
            self.assertTrue(res32, '新增+更新合计验证通过')
            Log.LogOutput( message='新增+更新实有房屋统计结果验证通过')
            #组织场所
            checkPara41={
                        "commonComplexPlaceNum": 1,
                        "dangerousChemicalsUnitNum": 1,
                        "fireSafetyNum": 1,
                        "hospitalNum": 1,
                        "internetBarNum": 1,
                        "orgName": orgInit['DftWangGeOrg'],
                        "otherLocaleNum": 1,
                        "publicPlaceNum": 1,
                        "safetyProductionNum": 1,
                        "schoolNum": 1,
                        "securityNum": 1,
                        "specialTradeNum": 1,
                        "subtotal": 11                             
                         }
            checkPara42={
                        "commonComplexPlaceNum": 1,
                        "dangerousChemicalsUnitNum": 1,
                        "fireSafetyNum": 1,
                        "hospitalNum": 1,
                        "internetBarNum": 1,
                        "orgName": "合计",
                        "otherLocaleNum": 1,
                        "publicPlaceNum": 1,
                        "safetyProductionNum": 1,
                        "schoolNum": 1,
                        "securityNum": 1,
                        "specialTradeNum": 1,
                        "subtotal": 11                             
                         }
            res41=checkDictInImportantPlaceStatics(checkpara=checkPara41,listpara=listPara)
            res42=checkDictInImportantPlaceStatics(checkpara=checkPara42,listpara=listPara)
            self.assertTrue(res41, '新增+更新小计验证通过')
            self.assertTrue(res42, '新增+更新合计验证通过')
            Log.LogOutput( message='新增+更新重点场所统计结果验证通过')           

        pass   
    
    '''
    @功能：研判分析-综合信息查询-综合新增查询
    @ chenhui 2016-6-3
    '''
    def testStatus_015(self):
        '''导入+更新统计'''
        #仿真环境下跳过测试
        if simulationEnvironment is True:
            pass
        else:
            ShiYouRenKouIntf.deleteAllPopulation()
            ZuZhiChangSuoIntf.deleteAllPopulation()
            ShiYouFangWuIntf.deleteAllActualHouse()
            try:
                data='2015-6-6 '+getCurrentTime()
                setLinuxTime(data)
                setLinuxTimeYunWei(data=data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                
                #第一次导入,少数场所模块没有导入功能
                #户籍人口
                importHuJiparam_05 = copy.deepcopy(ShiYouRenKouPara.data)
                importHuJiparam_05['dataType']='householdStaffData'
                importHuJiparam_05['templates']='HOUSEHOLDSTAFF'
                files = {'upload': ('test.xls', open('C:/autotest_file/importHuJiPopulation.xls', 'rb'),'applicationnd.ms-excel')}
                ret = ShiYouRenKouIntf.import_RenKou(importHuJiparam_05, files=files,username=userInit['DftWangGeUser'], password='11111111')
                #流动人口
                importHuJiparam = copy.deepcopy(ShiYouRenKouPara.data)
                importHuJiparam['dataType']='floatingPopulationData'
                importHuJiparam['templates']='FLOATINGPOPULATION'
                files = {'upload': ('test.xls', open('C:/autotest_file/importLiuDongPopulation.xls', 'rb'),'applicationnd.ms-excel')}
                ret = ShiYouRenKouIntf.import_RenKou(importHuJiparam, files=files,username=userInit['DftWangGeUser'], password='11111111')         
                #未落户人员
                importHuJiparam = copy.deepcopy(ShiYouRenKouPara.data)
                importHuJiparam['dataType']='unsettledPopulationData'
                importHuJiparam['templates']='UNSETTLEDPOPULATION'
                files = {'upload': ('test.xls', open('C:/autotest_file/importWeiLuoHuPopulation.xls', 'rb'),'applicationnd.ms-excel')}
                ret = ShiYouRenKouIntf.import_RenKou(importHuJiparam, files=files,username=userInit['DftWangGeUser'], password='11111111')         
                #境外人口
                importHuJiparam = copy.deepcopy(ShiYouRenKouPara.data)
                importHuJiparam['dataType']='overseaPersonnel'
                importHuJiparam['templates']='OVERSEASTAFF'
                files = {'upload': ('test.xls', open('C:/autotest_file/importJingWaiPopulation.xls', 'rb'),'applicationnd.ms-excel')}
                ret = ShiYouRenKouIntf.import_RenKou(importHuJiparam, files=files,username=userInit['DftWangGeUser'], password='11111111')         
                #刑满释放人员
                importHuJiparam = copy.deepcopy(ShiYouRenKouPara.data)
                importHuJiparam['dataType']='positiveInfo'
                importHuJiparam['templates']='POSITIVEINFO_syncActualPopulation'
                files = {'upload': ('test.xls', open('C:/autotest_file/importXingShiPopulation.xls', 'rb'),'applicationnd.ms-excel')}
                ret = ShiYouRenKouIntf.import_RenKou(importHuJiparam, files=files,username=userInit['DftWangGeUser'], password='11111111')         
                #社区矫正人员
                importHuJiparam = copy.deepcopy(ShiYouRenKouPara.data)
                importHuJiparam['dataType']='rectificativePerson'
                importHuJiparam['templates']='RECTIFICATIVEPERSON_syncActualPopulation'
                files = {'upload': ('test.xls', open('C:/autotest_file/importJiaoZhengPopulation.xls', 'rb'),'applicationnd.ms-excel')}
                ret = ShiYouRenKouIntf.import_RenKou(importHuJiparam, files=files,username=userInit['DftWangGeUser'], password='11111111')         
                #精神病人员
                importHuJiparam = copy.deepcopy(ShiYouRenKouPara.data)
                importHuJiparam['dataType']='mentalPatient'
                importHuJiparam['templates']='MENTALPATIENT_syncActualPopulation'
                files = {'upload': ('test.xls', open('C:/autotest_file/importJingShenBingPopulation.xls', 'rb'),'applicationnd.ms-excel')}
                ret = ShiYouRenKouIntf.import_RenKou(importHuJiparam, files=files,username=userInit['DftWangGeUser'], password='11111111')         
                #吸毒人员
                importHuJiparam = copy.deepcopy(ShiYouRenKouPara.data)
                importHuJiparam['dataType']='druggy'
                importHuJiparam['templates']='DRUGGY_syncActualPopulation'
                files = {'upload': ('test.xls', open('C:/autotest_file/importXiDuPopulation.xls', 'rb'),'applicationnd.ms-excel')}
                ret = ShiYouRenKouIntf.import_RenKou(importHuJiparam, files=files,username=userInit['DftWangGeUser'], password='11111111')         
                #重点青少年
                importHuJiparam = copy.deepcopy(ShiYouRenKouPara.data)
                importHuJiparam['dataType']='idleYouth'
                importHuJiparam['templates']='IDLEYOUTH_syncActualPopulation'
                files = {'upload': ('test.xls', open('C:/autotest_file/importQingShaoNian.xls', 'rb'),'applicationnd.ms-excel')}
                ret = ShiYouRenKouIntf.import_RenKou(importHuJiparam, files=files,username=userInit['DftWangGeUser'], password='11111111')         
                
                #重点上访人员
                importHuJiparam = copy.deepcopy(ShiYouRenKouPara.data)
                importHuJiparam['dataType']='superiorVisit'
                importHuJiparam['templates']='SUPERIORVISIT_syncActualPopulation'
                files = {'upload': ('test.xls', open('C:/autotest_file/importZhongDianShangFangPopulation.xls', 'rb'),'applicationnd.ms-excel')}
                ret = ShiYouRenKouIntf.import_RenKou(importHuJiparam, files=files,username=userInit['DftWangGeUser'], password='11111111')         
                #危险品从业人员
                importHuJiparam = copy.deepcopy(ShiYouRenKouPara.data)
                importHuJiparam['dataType']='dangerousGoodsPractitioner'
                importHuJiparam['templates']='DANGEROUSGOODSPRACTITIONER_syncActualPopulation'
                files = {'upload': ('test.xls', open('C:/autotest_file/importWeiXianPingCongYePopulation.xls', 'rb'),'applicationnd.ms-excel')}
                ret = ShiYouRenKouIntf.import_RenKou(importHuJiparam, files=files,username=userInit['DftWangGeUser'], password='11111111')         
                #其他人员
                importHuJiparam = copy.deepcopy(ShiYouRenKouPara.data)
                importHuJiparam['dataType']='otherAttentionPersonnel'
                importHuJiparam['templates']='OTHERATTENTIONPERSONNEL_syncActualPopulation'
                files = {'upload': ('test.xls', open('C:/autotest_file/importQiTaPopulation.xls', 'rb'),'applicationnd.ms-excel')}
                ret = ShiYouRenKouIntf.import_RenKou(importHuJiparam, files=files,username=userInit['DftWangGeUser'], password='11111111')         
                #是有房屋、出租房
                importFangWuparam_06 = copy.deepcopy(ShiYouFangWuPara.data)
                importFangWuparam_06['dataType']='actualHouseData'
                importFangWuparam_06['templates']='ACTUALHOUSE'
                files = {'upload': ('test.xls', open('C:/autotest_file/importShiYouFangWu.xls', 'rb'),'applicationnd.ms-excel')}
                ret = ShiYouFangWuIntf.import_ShiYouFangWu(importFangWuparam_06, files=files,username=userInit['DftWangGeUser'], password='11111111')         
                #安全生产重点
                importChangSuoparam = copy.deepcopy(ZuZhiChangSuoPara.dataShiYouDanWei)
                importChangSuoparam['dataType']='safetyProduction'
                importChangSuoparam['templates']='SAFETYPRODUCTIONKEY'
                files = {'upload': ('test.xls', open('C:/autotest_file/importAnQuanShengChanZhongDian.xls', 'rb'),'applicationnd.ms-excel')}
                ZuZhiChangSuoIntf.dataShiYouDanWei(importChangSuoparam, files=files,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')         
                
                #消防安全重点
                importChangSuoparam = copy.deepcopy(ZuZhiChangSuoPara.dataShiYouDanWei)
                importChangSuoparam['dataType']='fire'
                importChangSuoparam['templates']='FIRESAFETYKEY'
                files = {'upload': ('test.xls', open('C:/autotest_file/importXiaoFangAnQuanZhongDian.xls', 'rb'),'applicationnd.ms-excel')}
                ZuZhiChangSuoIntf.dataShiYouDanWei(importChangSuoparam, files=files,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')                 
                #治安重点
                importChangSuoparam = copy.deepcopy(ZuZhiChangSuoPara.dataShiYouDanWei)
                importChangSuoparam['dataType']='security'
                importChangSuoparam['templates']='SECURITYKEY'
                files = {'upload': ('test.xls', open('C:/autotest_file/importZhiAnZhongDian.xls', 'rb'),'applicationnd.ms-excel')}
                ZuZhiChangSuoIntf.dataShiYouDanWei(importChangSuoparam, files=files,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')                         
                #学校
                importChangSuoparam = copy.deepcopy(ZuZhiChangSuoPara.dataShiYouDanWei)
                importChangSuoparam['dataType']='schoolData'
                importChangSuoparam['templates']='SCHOOL'
                files = {'upload': ('test.xls', open('C:/autotest_file/importXueXiao.xls', 'rb'),'applicationnd.ms-excel')}
                ZuZhiChangSuoIntf.dataShiYouDanWei(importChangSuoparam, files=files,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')                 
                
                #医院
                
                #危险品化学单位
                importChangSuoparam = copy.deepcopy(ZuZhiChangSuoPara.dataShiYouDanWei)
                importChangSuoparam['dataType']='dangerousChemicalsUnit'
                importChangSuoparam['templates']='DANGEROUSCHEMICALSUNIT'
                files = {'upload': ('test.xls', open('C:/autotest_file/importWeiXianHuaXuePingDanWei.xls', 'rb'),'applicationnd.ms-excel')}
                ZuZhiChangSuoIntf.dataShiYouDanWei(importChangSuoparam, files=files,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')                 
                
                #上网服务单位
                importChangSuoparam = copy.deepcopy(ZuZhiChangSuoPara.dataShiYouDanWei)
                importChangSuoparam['dataType']='internetBar'
                importChangSuoparam['templates']='INTERNETBAR'
                files = {'upload': ('test.xls', open('C:/autotest_file/importShangWangFuWuDanWei.xls', 'rb'),'applicationnd.ms-excel')}
                ZuZhiChangSuoIntf.dataShiYouDanWei(importChangSuoparam, files=files,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')                 
                
                #公共场所
                importChangSuoparam = copy.deepcopy(ZuZhiChangSuoPara.dataShiYouDanWei)
                importChangSuoparam['dataType']='publicPlace'
                importChangSuoparam['templates']='PUBLICPLACE'
                files = {'upload': ('test.xls', open('C:/autotest_file/importGongGongChangSuo.xls', 'rb'),'applicationnd.ms-excel')}
                ZuZhiChangSuoIntf.dataShiYouDanWei(importChangSuoparam, files=files,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')                 
                
                #其他场所
                importChangSuoparam = copy.deepcopy(ZuZhiChangSuoPara.dataShiYouDanWei)
                importChangSuoparam['dataType']='otherlocale'
                importChangSuoparam['templates']='OTHERLOCALE'
                files = {'upload': ('test.xls', open('C:/autotest_file/importQiTaChangSuo.xls', 'rb'),'applicationnd.ms-excel')}
                ZuZhiChangSuoIntf.dataShiYouDanWei(importChangSuoparam, files=files,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
                #验证数据正确性
            #验证新增并修改后“新增”统计数据是否正确
                checkPara11={
                           'orgName':orgInit['DftWangGeOrg'],
                           'householdStaffNum':9,#户籍人口
                           'floatingPopulationNum':1,#流动人口
                           'overseaPersonNum':1,#境外
                           'unsettledPopulationNum':1,#未落户
                           'subtotal':12#小计
                           }
                checkPara12={
                           'orgName':'合计',
                           'householdStaffNum':9,#户籍人口
                           'floatingPopulationNum':1,#流动人口
                           'overseaPersonNum':1,#境外
                           'unsettledPopulationNum':1,#未落户
                           'subtotal':12#小计                            
                            }
                listPara={
                            'newQueryVo.orgId':orgInit['DftSheQuOrgId'],
                            'newQueryVo.startDate':'2015-6-6',
                            'newQueryVo.endDate':'2015-6-6',
                            'newQueryVo.startHours':'00',
                            'newQueryVo.startMinute':'00',
                            'newQueryVo.endHours':'24',
                            'newQueryVo.endMinute':'00',
                            'newQueryVo.queryType':'1',
                          }
                res11=checkDictInActualPopulationStatics(checkpara=checkPara11,listpara=listPara)
                res12=checkDictInActualPopulationStatics(checkpara=checkPara12,listpara=listPara)
                self.assertTrue(res11, '新增小计验证通过')
                self.assertTrue(res12, '新增合计验证通过')
                Log.LogOutput( message='导入后新增实有人口统计结果验证通过')
                #验证新增重点人员统计结果
                #小计
                checkPara21={
                            "dangerousGoodsPractitionerNum": 1,
                            "druggyNum": 1,
                            "idleYouthNum": 1,
                            "mentalPatientNum": 1,
                            "orgName": orgInit['DftWangGeOrg'],
                            "otherAttentionPersonnelNum": 1,
                            "positiveinfoNum": 1,
                            "rectificativePersonNum": 1,
                            "subtotal": 8,
                            "superiorVisitNum": 1
                }
                #合计
                checkPara22={
                            "dangerousGoodsPractitionerNum": 1,
                            "druggyNum": 1,
                            "idleYouthNum": 1,
                            "mentalPatientNum": 1,
                            "orgName":'合计',
                            "otherAttentionPersonnelNum": 1,
                            "positiveinfoNum": 1,
                            "rectificativePersonNum": 1,
                            "subtotal": 8,
                            "superiorVisitNum": 1
                }
                res21=checkDictInImportantPopulationStatics(checkpara=checkPara21,listpara=listPara)
                res22=checkDictInImportantPopulationStatics(checkpara=checkPara22,listpara=listPara)
                self.assertTrue(res21, '新增小计验证通过')
                self.assertTrue(res22, '新增合计验证通过')
                Log.LogOutput( message='导入后新增重点人员统计结果验证通过')
                #验证实有房屋新增
                #小计
                checkPara31={
                            "houseInfoNum": 4,
                            "orgName": orgInit['DftWangGeOrg'],
                            "rentalHouseNum": 1,
                            "subtotal": 5
                             }
                checkPara32={
                            "houseInfoNum": 4,
                            "orgName": "合计",
                            "rentalHouseNum": 1,
                            "subtotal": 5
                             }
                res31=checkDictInActualHouseStatics(checkpara=checkPara31,listpara=listPara)
                res32=checkDictInActualHouseStatics(checkpara=checkPara32,listpara=listPara)
                self.assertTrue(res31, '新增小计验证通过')
                self.assertTrue(res32, '新增合计验证通过')
                Log.LogOutput( message='导入后新增实有房屋统计结果验证通过')
                #组织场所
                checkPara41={
                            "commonComplexPlaceNum": 0,
                            "dangerousChemicalsUnitNum": 1,
                            "fireSafetyNum": 1,
                            "hospitalNum": 0,
                            "internetBarNum": 1,
                            "orgName": "测试自动化网格",
                            "otherLocaleNum": 1,
                            "publicPlaceNum": 1,
                            "safetyProductionNum": 1,
                            "schoolNum": 1,
                            "securityNum": 1,
                            "specialTradeNum": 0,
                            "subtotal": 8                          
                             }
                checkPara42={
                            "commonComplexPlaceNum": 0,
                            "dangerousChemicalsUnitNum": 1,
                            "fireSafetyNum": 1,
                            "hospitalNum": 0,
                            "internetBarNum": 1,
                            "orgName": "合计",
                            "otherLocaleNum": 1,
                            "publicPlaceNum": 1,
                            "safetyProductionNum": 1,
                            "schoolNum": 1,
                            "securityNum": 1,
                            "specialTradeNum": 0,
                            "subtotal": 8                               
                             }
                res41=checkDictInImportantPlaceStatics(checkpara=checkPara41,listpara=listPara)
                res42=checkDictInImportantPlaceStatics(checkpara=checkPara42,listpara=listPara)
                self.assertTrue(res41, '新增小计验证通过')
                self.assertTrue(res42, '新增合计验证通过')
                Log.LogOutput( message='导入后新增重点场所统计结果验证通过') 
                
                #将服务器时间改回正确时间
                setLinuxTime(data=getCurrentDateAndTime())
                setLinuxTimeYunWei(data=getCurrentDateAndTime(),password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                #再次导入，相当于修改
                #户籍人口
                importHuJiparam_05 = copy.deepcopy(ShiYouRenKouPara.data)
                importHuJiparam_05['dataType']='householdStaffData'
                importHuJiparam_05['templates']='HOUSEHOLDSTAFF'
                files = {'upload': ('test.xls', open('C:/autotest_file/importHuJiPopulation.xls', 'rb'),'applicationnd.ms-excel')}
                ret = ShiYouRenKouIntf.import_RenKou(importHuJiparam_05, files=files,username=userInit['DftWangGeUser'], password='11111111')
                #流动人口
                importHuJiparam = copy.deepcopy(ShiYouRenKouPara.data)
                importHuJiparam['dataType']='floatingPopulationData'
                importHuJiparam['templates']='FLOATINGPOPULATION'
                files = {'upload': ('test.xls', open('C:/autotest_file/importLiuDongPopulation.xls', 'rb'),'applicationnd.ms-excel')}
                ret = ShiYouRenKouIntf.import_RenKou(importHuJiparam, files=files,username=userInit['DftWangGeUser'], password='11111111')         
                #未落户人员
                importHuJiparam = copy.deepcopy(ShiYouRenKouPara.data)
                importHuJiparam['dataType']='unsettledPopulationData'
                importHuJiparam['templates']='UNSETTLEDPOPULATION'
                files = {'upload': ('test.xls', open('C:/autotest_file/importWeiLuoHuPopulation.xls', 'rb'),'applicationnd.ms-excel')}
                ret = ShiYouRenKouIntf.import_RenKou(importHuJiparam, files=files,username=userInit['DftWangGeUser'], password='11111111')         
                #境外人口
                importHuJiparam = copy.deepcopy(ShiYouRenKouPara.data)
                importHuJiparam['dataType']='overseaPersonnel'
                importHuJiparam['templates']='OVERSEASTAFF'
                files = {'upload': ('test.xls', open('C:/autotest_file/importJingWaiPopulation.xls', 'rb'),'applicationnd.ms-excel')}
                ret = ShiYouRenKouIntf.import_RenKou(importHuJiparam, files=files,username=userInit['DftWangGeUser'], password='11111111')         
                #刑满释放人员
                importHuJiparam = copy.deepcopy(ShiYouRenKouPara.data)
                importHuJiparam['dataType']='positiveInfo'
                importHuJiparam['templates']='POSITIVEINFO_syncActualPopulation'
                files = {'upload': ('test.xls', open('C:/autotest_file/importXingShiPopulation.xls', 'rb'),'applicationnd.ms-excel')}
                ret = ShiYouRenKouIntf.import_RenKou(importHuJiparam, files=files,username=userInit['DftWangGeUser'], password='11111111')         
                #社区矫正人员
                importHuJiparam = copy.deepcopy(ShiYouRenKouPara.data)
                importHuJiparam['dataType']='rectificativePerson'
                importHuJiparam['templates']='RECTIFICATIVEPERSON_syncActualPopulation'
                files = {'upload': ('test.xls', open('C:/autotest_file/importJiaoZhengPopulation.xls', 'rb'),'applicationnd.ms-excel')}
                ret = ShiYouRenKouIntf.import_RenKou(importHuJiparam, files=files,username=userInit['DftWangGeUser'], password='11111111')         
                #精神病人员
                importHuJiparam = copy.deepcopy(ShiYouRenKouPara.data)
                importHuJiparam['dataType']='mentalPatient'
                importHuJiparam['templates']='MENTALPATIENT_syncActualPopulation'
                files = {'upload': ('test.xls', open('C:/autotest_file/importJingShenBingPopulation.xls', 'rb'),'applicationnd.ms-excel')}
                ret = ShiYouRenKouIntf.import_RenKou(importHuJiparam, files=files,username=userInit['DftWangGeUser'], password='11111111')         
                #吸毒人员
                importHuJiparam = copy.deepcopy(ShiYouRenKouPara.data)
                importHuJiparam['dataType']='druggy'
                importHuJiparam['templates']='DRUGGY_syncActualPopulation'
                files = {'upload': ('test.xls', open('C:/autotest_file/importXiDuPopulation.xls', 'rb'),'applicationnd.ms-excel')}
                ret = ShiYouRenKouIntf.import_RenKou(importHuJiparam, files=files,username=userInit['DftWangGeUser'], password='11111111')         
                #重点青少年
                importHuJiparam = copy.deepcopy(ShiYouRenKouPara.data)
                importHuJiparam['dataType']='idleYouth'
                importHuJiparam['templates']='IDLEYOUTH_syncActualPopulation'
                files = {'upload': ('test.xls', open('C:/autotest_file/importQingShaoNian.xls', 'rb'),'applicationnd.ms-excel')}
                ret = ShiYouRenKouIntf.import_RenKou(importHuJiparam, files=files,username=userInit['DftWangGeUser'], password='11111111')         
                
                #重点上访人员
                importHuJiparam = copy.deepcopy(ShiYouRenKouPara.data)
                importHuJiparam['dataType']='superiorVisit'
                importHuJiparam['templates']='SUPERIORVISIT_syncActualPopulation'
                files = {'upload': ('test.xls', open('C:/autotest_file/importZhongDianShangFangPopulation.xls', 'rb'),'applicationnd.ms-excel')}
                ret = ShiYouRenKouIntf.import_RenKou(importHuJiparam, files=files,username=userInit['DftWangGeUser'], password='11111111')         
                #危险品从业人员
                importHuJiparam = copy.deepcopy(ShiYouRenKouPara.data)
                importHuJiparam['dataType']='dangerousGoodsPractitioner'
                importHuJiparam['templates']='DANGEROUSGOODSPRACTITIONER_syncActualPopulation'
                files = {'upload': ('test.xls', open('C:/autotest_file/importWeiXianPingCongYePopulation.xls', 'rb'),'applicationnd.ms-excel')}
                ret = ShiYouRenKouIntf.import_RenKou(importHuJiparam, files=files,username=userInit['DftWangGeUser'], password='11111111')         
                #其他人员
                importHuJiparam = copy.deepcopy(ShiYouRenKouPara.data)
                importHuJiparam['dataType']='otherAttentionPersonnel'
                importHuJiparam['templates']='OTHERATTENTIONPERSONNEL_syncActualPopulation'
                files = {'upload': ('test.xls', open('C:/autotest_file/importQiTaPopulation.xls', 'rb'),'applicationnd.ms-excel')}
                ret = ShiYouRenKouIntf.import_RenKou(importHuJiparam, files=files,username=userInit['DftWangGeUser'], password='11111111')         
                #是有房屋、出租房
                importFangWuparam_06 = copy.deepcopy(ShiYouFangWuPara.data)
                importFangWuparam_06['dataType']='actualHouseData'
                importFangWuparam_06['templates']='ACTUALHOUSE'
                files = {'upload': ('test.xls', open('C:/autotest_file/importShiYouFangWu.xls', 'rb'),'applicationnd.ms-excel')}
                ret = ShiYouFangWuIntf.import_ShiYouFangWu(importFangWuparam_06, files=files,username=userInit['DftWangGeUser'], password='11111111')         
                #安全生产重点
                importChangSuoparam = copy.deepcopy(ZuZhiChangSuoPara.dataShiYouDanWei)
                importChangSuoparam['dataType']='safetyProduction'
                importChangSuoparam['templates']='SAFETYPRODUCTIONKEY'
                files = {'upload': ('test.xls', open('C:/autotest_file/importAnQuanShengChanZhongDian.xls', 'rb'),'applicationnd.ms-excel')}
                ZuZhiChangSuoIntf.dataShiYouDanWei(importChangSuoparam, files=files,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')         
                
                #消防安全重点
                importChangSuoparam = copy.deepcopy(ZuZhiChangSuoPara.dataShiYouDanWei)
                importChangSuoparam['dataType']='fire'
                importChangSuoparam['templates']='FIRESAFETYKEY'
                files = {'upload': ('test.xls', open('C:/autotest_file/importXiaoFangAnQuanZhongDian.xls', 'rb'),'applicationnd.ms-excel')}
                ZuZhiChangSuoIntf.dataShiYouDanWei(importChangSuoparam, files=files,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')                 
                #治安重点
                importChangSuoparam = copy.deepcopy(ZuZhiChangSuoPara.dataShiYouDanWei)
                importChangSuoparam['dataType']='security'
                importChangSuoparam['templates']='SECURITYKEY'
                files = {'upload': ('test.xls', open('C:/autotest_file/importZhiAnZhongDian.xls', 'rb'),'applicationnd.ms-excel')}
                ZuZhiChangSuoIntf.dataShiYouDanWei(importChangSuoparam, files=files,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')                         
                #学校
                importChangSuoparam = copy.deepcopy(ZuZhiChangSuoPara.dataShiYouDanWei)
                importChangSuoparam['dataType']='schoolData'
                importChangSuoparam['templates']='SCHOOL'
                files = {'upload': ('test.xls', open('C:/autotest_file/importXueXiao.xls', 'rb'),'applicationnd.ms-excel')}
                ZuZhiChangSuoIntf.dataShiYouDanWei(importChangSuoparam, files=files,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')                 
                
                #医院
                
                #危险品化学单位
                importChangSuoparam = copy.deepcopy(ZuZhiChangSuoPara.dataShiYouDanWei)
                importChangSuoparam['dataType']='dangerousChemicalsUnit'
                importChangSuoparam['templates']='DANGEROUSCHEMICALSUNIT'
                files = {'upload': ('test.xls', open('C:/autotest_file/importWeiXianHuaXuePingDanWei.xls', 'rb'),'applicationnd.ms-excel')}
                ZuZhiChangSuoIntf.dataShiYouDanWei(importChangSuoparam, files=files,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')                 
                
                #上网服务单位
                importChangSuoparam = copy.deepcopy(ZuZhiChangSuoPara.dataShiYouDanWei)
                importChangSuoparam['dataType']='internetBar'
                importChangSuoparam['templates']='INTERNETBAR'
                files = {'upload': ('test.xls', open('C:/autotest_file/importShangWangFuWuDanWei.xls', 'rb'),'applicationnd.ms-excel')}
                ZuZhiChangSuoIntf.dataShiYouDanWei(importChangSuoparam, files=files,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')                 
                
                #公共场所
                importChangSuoparam = copy.deepcopy(ZuZhiChangSuoPara.dataShiYouDanWei)
                importChangSuoparam['dataType']='publicPlace'
                importChangSuoparam['templates']='PUBLICPLACE'
                files = {'upload': ('test.xls', open('C:/autotest_file/importGongGongChangSuo.xls', 'rb'),'applicationnd.ms-excel')}
                ZuZhiChangSuoIntf.dataShiYouDanWei(importChangSuoparam, files=files,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')                 
                
                #其他场所
                importChangSuoparam = copy.deepcopy(ZuZhiChangSuoPara.dataShiYouDanWei)
                importChangSuoparam['dataType']='otherlocale'
                importChangSuoparam['templates']='OTHERLOCALE'
                files = {'upload': ('test.xls', open('C:/autotest_file/importQiTaChangSuo.xls', 'rb'),'applicationnd.ms-excel')}
                ZuZhiChangSuoIntf.dataShiYouDanWei(importChangSuoparam, files=files,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
                #验证数据正确性
            #验证新增并修改后“新增”统计数据是否正确
                checkPara11={
                           'orgName':orgInit['DftWangGeOrg'],
                           'householdStaffNum':9,#户籍人口
                           'floatingPopulationNum':1,#流动人口
                           'overseaPersonNum':1,#境外
                           'unsettledPopulationNum':1,#未落户
                           'subtotal':12#小计
                           }
                checkPara12={
                           'orgName':'合计',
                           'householdStaffNum':9,#户籍人口
                           'floatingPopulationNum':1,#流动人口
                           'overseaPersonNum':1,#境外
                           'unsettledPopulationNum':1,#未落户
                           'subtotal':12#小计                            
                            }
                listPara={
                            'newQueryVo.orgId':orgInit['DftSheQuOrgId'],
                            'newQueryVo.startDate':Time.getCurrentDate(),
                            'newQueryVo.endDate':Time.getCurrentDate(),
                            'newQueryVo.startHours':'00',
                            'newQueryVo.startMinute':'00',
                            'newQueryVo.endHours':'24',
                            'newQueryVo.endMinute':'00',
                            'newQueryVo.queryType':'2',#新增+更新
                          }
                res11=checkDictInActualPopulationStatics(checkpara=checkPara11,listpara=listPara)
                res12=checkDictInActualPopulationStatics(checkpara=checkPara12,listpara=listPara)
                self.assertTrue(res11, '新增+更新小计验证通过')
                self.assertTrue(res12, '新增+更新合计验证通过')
                Log.LogOutput( message='导入后新增+更新实有人口统计结果验证通过')
                #验证新增重点人员统计结果
                #小计
                checkPara21={
                            "dangerousGoodsPractitionerNum": 1,
                            "druggyNum": 1,
                            "idleYouthNum": 1,
                            "mentalPatientNum": 1,
                            "orgName": orgInit['DftWangGeOrg'],
                            "otherAttentionPersonnelNum": 1,
                            "positiveinfoNum": 1,
                            "rectificativePersonNum": 1,
                            "subtotal": 8,
                            "superiorVisitNum": 1
                }
                #合计
                checkPara22={
                            "dangerousGoodsPractitionerNum": 1,
                            "druggyNum": 1,
                            "idleYouthNum": 1,
                            "mentalPatientNum": 1,
                            "orgName":'合计',
                            "otherAttentionPersonnelNum": 1,
                            "positiveinfoNum": 1,
                            "rectificativePersonNum": 1,
                            "subtotal": 8,
                            "superiorVisitNum": 1
                }
                res21=checkDictInImportantPopulationStatics(checkpara=checkPara21,listpara=listPara)
                res22=checkDictInImportantPopulationStatics(checkpara=checkPara22,listpara=listPara)
                self.assertTrue(res21, '新增+更新小计验证通过')
                self.assertTrue(res22, '新增+更新合计验证通过')
                Log.LogOutput( message='导入后新增+更新重点人员统计结果验证通过')
#                 #验证实有房屋新增
#                 #小计
#                 checkPara31={
#                             "houseInfoNum": 4,
#                             "orgName": orgInit['DftWangGeOrg'],
#                             "rentalHouseNum": 1,
#                             "subtotal": 5
#                              }
#                 checkPara32={
#                             "houseInfoNum": 4,
#                             "orgName": "合计",
#                             "rentalHouseNum": 1,
#                             "subtotal": 5
#                              }
#                 res31=checkDictInActualHouseStatics(checkpara=checkPara31,listpara=listPara)
#                 res32=checkDictInActualHouseStatics(checkpara=checkPara32,listpara=listPara)
#                 self.assertTrue(res31, '新增+更新小计验证通过')
#                 self.assertTrue(res32, '新增+更新合计验证通过')
#                 Log.LogOutput( message='导入后新增+更新实有房屋统计结果验证通过')
                #组织场所
                checkPara41={
                            "commonComplexPlaceNum": 0,
                            "dangerousChemicalsUnitNum": 1,
                            "fireSafetyNum": 1,
                            "hospitalNum": 0,
                            "internetBarNum": 1,
                            "orgName": "测试自动化网格",
                            "otherLocaleNum": 1,
                            "publicPlaceNum": 1,
                            "safetyProductionNum": 1,
                            "schoolNum": 1,
                            "securityNum": 1,
                            "specialTradeNum": 0,
                            "subtotal": 8                          
                             }
                checkPara42={
                            "commonComplexPlaceNum": 0,
                            "dangerousChemicalsUnitNum": 1,
                            "fireSafetyNum": 1,
                            "hospitalNum": 0,
                            "internetBarNum": 1,
                            "orgName": "合计",
                            "otherLocaleNum": 1,
                            "publicPlaceNum": 1,
                            "safetyProductionNum": 1,
                            "schoolNum": 1,
                            "securityNum": 1,
                            "specialTradeNum": 0,
                            "subtotal": 8                               
                             }
                res41=checkDictInImportantPlaceStatics(checkpara=checkPara41,listpara=listPara)
                res42=checkDictInImportantPlaceStatics(checkpara=checkPara42,listpara=listPara)
                self.assertTrue(res41, '新增+更新小计验证通过')
                self.assertTrue(res42, '新增+更新合计验证通过')
                Log.LogOutput( message='导入后新增+更新重点场所统计结果验证通过') 
                            
            finally:
                #将服务器时间改回正确时间
                setLinuxTime(data=getCurrentDateAndTime())
                setLinuxTimeYunWei(data=getCurrentDateAndTime(),password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
                
        pass    
#     '''
#     @功能：研判分析-事件多维分析-数据地图，用户用得少，暂时关闭
#     @ chenhui 2016-4-22
#     '''
#     def testStatus_013(self):
#         '''事件多维分析-数据地图'''
#         try:
#             Data='2015-6-6 '+getCurrentTime()
#             setLinuxTime(Data)
#             setLinuxTimeYunWei(Data=Data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
#             #街道新增事件A，作为存量
#             issueParam = copy.deepcopy(issueObject2) 
#             issueParam['issue.occurDate']= Data
#             rs=addIssue(issueDict=issueParam)
#             ######将时间改为2016-2-6
#             Data='2016-2-6 '+getCurrentTime()
#             setLinuxTime(Data)
#             setLinuxTimeYunWei(Data=Data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
#             #街道新增事件B，并上报、办结 
#             issueParam = copy.deepcopy(issueObject2) 
#             issueParam['issue.occurDate']= Data
#             rs=addIssue(issueDict=issueParam)           
#             #上报给区，设置上报参数
#             sIssuePara=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)        
#             sIssuePara['operation.dealOrg.id']=orgInit['DftJieDaoOrgId']
#             sIssuePara['operation.issue.id']=rs['issueId']
#             sIssuePara['keyId']=rs['issueStepId']      
#             sIssuePara['operation.dealUserName']=userInit['DftJieDaoUserXM']
#             sIssuePara['operation.mobile']=userInit['DftJieDaoUserSJ']
#             sIssuePara['operation.content']='上报事件'
#             sIssuePara['operation.targeOrg.id']=orgInit['DftQuOrgId']
#             sIssuePara['themainOrgid']=orgInit['DftQuOrgId']        
#             sIssuePara['dealCode']='41'#上报
#             #上报
#             result=dealIssue(issueDict=sIssuePara)
#             self.assertTrue(result.result, '事件上报失败')
#             #区受理
#             sIssuePara2={
#                      'operation.dealOrg.id':orgInit['DftQuOrgId'],
#                      'operation.issue.id':sIssuePara['operation.issue.id'],
#                      'operation.dealUserName':userInit['DftQuUserXM'],
#                      'operation.mobile':userInit['DftQuUserSJ'],
#                      'dealCode':'61',
#                      'keyId':sIssuePara['keyId']+1
#                      }
#             result2=dealIssue(issueDict=sIssuePara2,username=userInit['DftQuUser'])
#             self.assertTrue(result2.result,'区受理失败！')
#             #区办结
#             sIssuePara3=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)        
#             sIssuePara3['operation.dealOrg.id']=orgInit['DftQuOrgId']
#             sIssuePara3['operation.issue.id']=rs['issueId']
#             sIssuePara3['keyId']=sIssuePara['keyId']+1
#             sIssuePara3['operation.dealUserName']=userInit['DftQuUserXM']
#             sIssuePara3['operation.mobile']=userInit['DftQuUserSJ']
#             sIssuePara3['operation.content']='事件处理'       
#             sIssuePara3['dealCode']='31'#办结
#             result3=dealIssue(issueDict=sIssuePara3, username=userInit['DftQuUser'], password='11111111')
#             self.assertTrue(result3.result, '办结失败')
#             #街道新增事件C
#             issueParam = copy.deepcopy(issueObject2) 
#             issueParam['issue.occurDate']= Data
#             rs=addIssue(issueDict=issueParam) 
#             ######将时间改为2016-2-26，查看上过月数据
#             Data='2016-2-26 '+getCurrentTime()
#             setLinuxTime(Data)
#             setLinuxTimeYunWei(Data=Data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
#             #立即执行job
#             para={
#              'task.name':'newStateConflictAnalyzingDataJob',
#              'job.name':'NewStateConflictAnalyzingDataJob'
#              }
#             result0=runJobNow(jobPara=para)
#             self.assertTrue(result0,'job运行成功')
#             
#             
#         finally:
#             #将服务器时间改回正确时间
#             setLinuxTime(Data=getCurrentDateAndTime())
#             setLinuxTimeYunWei(Data=getCurrentDateAndTime(),password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
#         pass  







#     '''
#     @功能：研判分析-总况-重点人员统计
#     @ chenyan 2016-5-25
#     '''
#     def test_ZhongDianRenYuanZongKuang(self):
#         '''总况-重点人员统计'''
#         #设置linux时间为2015-12-28
#         try:
#             Data='2016-2-1 '+getCurrentTime()
#             #注意''中的空格不可少
#             setLinuxTime(Data)
#             setLinuxTimeYunWei(Data=Data,password='tianqueshuaige',serverIp=RenZhengZhongXinUrl)
# 
#             ShiYouRenKouIntf.deleteAllPopulation()
# 
#             xingShiParam1 = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
#             xingShiParam1['mode']='add'
#             xingShiParam1['population.organization.id'] = orgInit['DftWangGeOrgId']
#             xingShiParam1['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人口or流动人口
#             xingShiParam1['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['xingManShiFangRenYuan']
#             xingShiParam1['population.organization.orgName'] = orgInit['DftWangGeOrg']
#             xingShiParam1['population.idCardNo'] = '330000199911111025'
#             xingShiParam1['population.name'] = '刑满释放人员1'
#             xingShiParam1['actualPersonType'] = xingShiParam1['population.actualPopulationType']
#             xingShiParam1['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
#             xingShiParam1['population.isHaveHouse1'] = 'null'   
#             xingShiParam1['population.caseReason'] = 'Reason'
#             xingShiParam1['population.positiveInfoType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '刑释人员'") 
#             xingShiParam1['population.laborEduAddress'] = '劳教所'
#             xingShiParam1['population.imprisonmentDate'] = '2weeks'
#             xingShiParam1['population.releaseOrBackDate'] = '2016-2-10' #Time.getCurrentDate()  
#             responseDict = ShiYouRenKouIntf.add_xingManShiFang(xingShiParam1, username=userInit['DftWangGeUser'], password='11111111')
#             self.assertTrue(responseDict.result, '新增刑满释放人员失败') 
#             
#             xingShiParam2 = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
#             xingShiParam2['mode']='add'
#             xingShiParam2['population.organization.id'] = orgInit['DftWangGeOrgId']
#             xingShiParam2['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人口or流动人口
#             xingShiParam2['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['xingManShiFangRenYuan']
#             xingShiParam2['population.organization.orgName'] = orgInit['DftWangGeOrg']
#             xingShiParam2['population.idCardNo'] = '320000199911111225'
#             xingShiParam2['population.name'] = '刑满释放人员2'
#             xingShiParam2['actualPersonType'] = xingShiParam1['population.actualPopulationType']
#             xingShiParam2['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
#             xingShiParam2['population.isHaveHouse1'] = 'null'   
#             xingShiParam2['population.death'] = 'true'
#             xingShiParam2['population.caseReason'] = 'Reason'
#             xingShiParam2['population.positiveInfoType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '解教人员'") 
#             xingShiParam2['population.laborEduAddress'] = '劳教所'
#             xingShiParam2['population.imprisonmentDate'] = '2weeks'
#             xingShiParam2['population.releaseOrBackDate'] = '2016-2-10' #Time.getCurrentDate()  
#             responseDict = ShiYouRenKouIntf.add_xingManShiFang(xingShiParam2, username=userInit['DftWangGeUser'], password='11111111')
#             self.assertTrue(responseDict.result, '新增刑满释放人员失败') 
#     
#             jiaoZhengParam = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
#             jiaoZhengParam['mode']='add'
#             jiaoZhengParam['population.organization.id'] = orgInit['DftWangGeOrgId']
#             jiaoZhengParam['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']
#             jiaoZhengParam['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['sheQuJiaoZhengRenYuan']
#             jiaoZhengParam['population.organization.orgName'] = orgInit['DftWangGeOrg']
#             jiaoZhengParam['population.idCardNo'] = '331110199711220005'
#             jiaoZhengParam['population.name'] = '矫正人员'
#             jiaoZhengParam['actualPersonType'] = jiaoZhengParam['population.actualPopulationType']
#             jiaoZhengParam['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
#             jiaoZhengParam['population.isHaveHouse1'] = 'null'   
#             jiaoZhengParam['population.accusation'] = '矫正罪名'
#             jiaoZhengParam['population.executeType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '监外执行罪犯'") 
#             jiaoZhengParam['population.rectifyStartDate'] = '2015-12-01'
#             jiaoZhengParam['population.rectifyEndDate'] = '2015-12-31'     
#             responseDict = ShiYouRenKouIntf.add_sheQuJiaoZheng(sheQuJiaoZhengDict=jiaoZhengParam, username=userInit['DftWangGeUser'], password='11111111')
#             self.assertTrue(responseDict.result, '新增社区矫正人员失败')   
#             
#         #添加成员库成员            
#             fuWuParam = copy.deepcopy(ShiYouRenKouPara.fuWuRenYuanDict)      
#             fuWuParam['serviceTeamMemberBase.org.id'] = orgInit['DftWangGeOrgId']
#             fuWuParam['serviceTeamMemberBase.name'] = '服务%s'%CommonUtil.createRandomString()
#             fuWuParam['serviceTeamMemberBase.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别(男、女)', displayName='男')     
#             fuWuParam['serviceTeamMemberBase.mobile'] = '13011111118'
#             responseDict = ShiYouRenKouIntf.add_FuWuChengYuan(fuWuParam, username=userInit['DftWangGeUser'], password='11111111')
#             self.assertTrue(responseDict.result, '新增成员失败')    
#         #添加服务记录               
#             RecordParam = copy.deepcopy(ShiYouRenKouPara.serviceRecordDict) 
#             RecordParam['mode'] = 'add'   
#             RecordParam['serviceRecord.organization.id'] = orgInit['DftWangGeOrgId']  
#             RecordParam['isSubmit'] = 'true'
#             RecordParam['serviceRecord.occurDate'] = '2016-03-10'   #Time.getCurrentDate() 
#             RecordParam['serviceRecord.occurPlace'] = '地点%s'%CommonUtil.createRandomString()
#             RecordParam['serviceRecord.serviceMembers'] = '%s-服务-0'%CommonIntf.getDbQueryResult(dbCommand = "select t.id from Serviceteammemberbase  t where t.name='%s'" %(fuWuParam['serviceTeamMemberBase.name']))
#             RecordParam['serviceRecord.serviceObjects'] = '%s-%s-rectificativePerson' %(CommonIntf.getDbQueryResult(dbCommand = "select t.id from rectificativePersons t where t.idcardno='%s' " % (jiaoZhengParam['population.idCardNo'])),jiaoZhengParam['population.name'])
#             responseDict = ShiYouRenKouIntf.add_serviceRecordHuJiRenKou(RecordDict=RecordParam, username=userInit['DftWangGeUser'], password='11111111')
#             self.assertTrue(responseDict.result, '新增服务事件失败')
#     
#             psychosisParam= copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
#             psychosisParam['mode']='add'
#             psychosisParam['population.organization.id'] = orgInit['DftWangGeOrgId']
#             psychosisParam['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人口or流动人口
#             psychosisParam['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['jingShenBingRenYuan']
#             psychosisParam['population.organization.orgName'] = orgInit['DftWangGeOrg']
#             psychosisParam['population.idCardNo'] = '332200199711220011'
#             psychosisParam['population.name'] = '精神病人员'
#             psychosisParam['actualPersonType'] = psychosisParam['population.actualPopulationType']
#             psychosisParam['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
#             psychosisParam['population.isHaveHouse1'] = 'null'   
#             psychosisParam['population.dangerLevel.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='危险程度', displayName='低')   
#             responseDict = ShiYouRenKouIntf.add_jingShengBingRenYuan(psychosisDict=psychosisParam, username=userInit['DftWangGeUser'], password='11111111')
#             self.assertTrue(responseDict.result, '新增精神病人员失败') 
#                     
#             detaileParam = copy.deepcopy(ShiYouRenKouPara.logoutHuJiDict)
#             detaileParam['populationIds'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from Mentalpatients t where t.idcardno='%s'" % psychosisParam['population.idCardNo'] )
#             detaileParam['population.logoutDetail.logout'] = '1'
#             detaileParam['population.logoutDetail.logoutDate'] = Time.getCurrentDateAndTime()
#             detaileParam['population.logoutDetail.logoutReason'] = '取消关注'
#             ret = ShiYouRenKouIntf.logout_jingShengBingRenYuan(detaileParam,username=userInit['DftWangGeUser'], password='11111111')
# #             self.assertTrue(ret.result, '人口取消关注失败')
#     
#             xiDuParam = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
#             xiDuParam['mode']='add'
#             xiDuParam['population.organization.id'] = orgInit['DftWangGeOrgId']
#             xiDuParam['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于会人口or流动人口
#             xiDuParam['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['xiDuRenYuan']
#             xiDuParam['population.organization.orgName'] = orgInit['DftWangGeOrg']
#             xiDuParam['population.idCardNo'] = '333300199711220000'
#             xiDuParam['population.name'] = '吸毒人员'
#             xiDuParam['actualPersonType'] = xiDuParam['population.actualPopulationType']
#             xiDuParam['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
#             xiDuParam['population.isHaveHouse1'] = 'null'   
#             xiDuParam['population.detoxicateCase.id'] = CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '强制戒毒'")  
#             responseDict = ShiYouRenKouIntf.add_xiDuRenYuan(xiDuRenYuanDict=xiDuParam, username=userInit['DftWangGeUser'], password='11111111')
#             self.assertTrue(responseDict.result, '新增吸毒人员失败') 
#             
#         #添加服务成员            
#             MemberParam = copy.deepcopy(ShiYouRenKouPara.serviceMemberDict)      
#             MemberParam['serviceMemberWithObject.memberId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from Serviceteammemberbase t where t.name='%s'" % (fuWuParam['serviceTeamMemberBase.name']))
#             MemberParam['serviceMemberWithObject.objectType'] = 'druggy'
#             MemberParam['serviceMemberWithObject.objectName'] = xiDuParam['population.name']   
#             MemberParam['serviceMemberWithObject.objectId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from druggys t where t.idcardno='%s' " % xiDuParam['population.idCardNo'])
#             MemberParam['serviceMemberWithObject.teamMember'] = ' 1'
#             MemberParam['serviceMemberWithObject.onDuty'] = '1'
#             MemberParam['serviceMemberWithObject.objectLogout'] = '1' 
#             responseDict = ShiYouRenKouIntf.add_serviceMemberHuJiRenKou(serviceDict=MemberParam, username=userInit['DftWangGeUser'], password='11111111')
#             self.assertTrue(responseDict.result, '新增服务人员失败')
#     
#             qingShaoNianParam = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
#             qingShaoNianParam['mode']='add'
#             qingShaoNianParam['population.organization.id'] = orgInit['DftWangGeOrgId']
#             qingShaoNianParam['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人口or流动人口
#             qingShaoNianParam['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['zhongDianQingShaoNian']
#             qingShaoNianParam['population.organization.orgName'] = orgInit['DftWangGeOrg']
#             qingShaoNianParam['population.idCardNo'] = '334400199711220000'
#             qingShaoNianParam['population.name'] = '重点青少年'
#             qingShaoNianParam['actualPersonType'] = qingShaoNianParam['population.actualPopulationType']
#             qingShaoNianParam['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
#             qingShaoNianParam['population.isHaveHouse1'] = 'null'   
#             qingShaoNianParam['staffTypeIds'] = CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '闲散青少年'")      
#             responseDict = ShiYouRenKouIntf.add_zhongDianQingShaoNian(qingShaoNianDict=qingShaoNianParam, username=userInit['DftWangGeUser'], password='11111111')
#             self.assertTrue(responseDict.result, '新增重点青少年失败') 
#     
#             shangFangParam = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
#             shangFangParam['mode']='add'
#             shangFangParam['population.organization.id'] = orgInit['DftWangGeOrgId']
#             shangFangParam['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人员or流动人口
#             shangFangParam['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['zhongDianShangFangRenYuan']
#             shangFangParam['population.organization.orgName'] = orgInit['DftWangGeOrg']
#             shangFangParam['population.idCardNo'] = '335500199711220000'
#             shangFangParam['population.name'] = '重点上访人员'
#             shangFangParam['actualPersonType'] = shangFangParam['population.actualPopulationType']
#             shangFangParam['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
#             shangFangParam['population.isHaveHouse1'] = 'null'   
#             shangFangParam['population.visitReason'] = '上访原因'       
#             responseDict = ShiYouRenKouIntf.add_shangFangRenYuan(shangFangDict=shangFangParam, username=userInit['DftWangGeUser'], password='11111111')
#             self.assertTrue(responseDict.result, '新增上访人员失败')
#     
#             practitionerParam = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
#             practitionerParam['mode']='add'
#             practitionerParam['population.organization.id'] = orgInit['DftWangGeOrgId']
#             practitionerParam['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']   #属于户籍人员or流动人员
#             practitionerParam['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['weiXianPingCongYeRenYuan']
#             practitionerParam['population.organization.orgName'] = orgInit['DftWangGeOrg']
#             practitionerParam['population.idCardNo'] = '336600199711220000'
#             practitionerParam['population.name'] = '危险品从业人员'
#             practitionerParam['actualPersonType'] = practitionerParam['population.actualPopulationType']
#             practitionerParam['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
#             practitionerParam['population.isHaveHouse1'] = 'null'   
#             practitionerParam['population.dangerousWorkingType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '民爆'")
#             practitionerParam['population.legalPerson'] = '法人代表'  
#             practitionerParam['population.legalPersonMobileNumber'] = '11111111111' 
#             practitionerParam['population.legalPersonTelephone'] = '3333333'  
#             practitionerParam['population.workUnit'] = '工作单位'       
#             responseDict = ShiYouRenKouIntf.add_weiXianPingCongYeRenYuan(practitionerDict=practitionerParam, username=userInit['DftWangGeUser'], password='11111111')
#             self.assertTrue(responseDict.result, '新增危险品从业人员失败') 
#             
#             otherParam = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
#             otherParam['mode']='add'
#             otherParam['population.organization.id'] = orgInit['DftWangGeOrgId']
#             otherParam['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人员or流动人员
#             otherParam['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['qiTaRenYuan']
#             otherParam['population.organization.orgName'] = orgInit['DftWangGeOrg']
#             otherParam['population.idCardNo'] = '337700199711220000'
#             otherParam['population.name'] = '其他人员'
#             otherParam['actualPersonType'] = otherParam['population.actualPopulationType']
#             otherParam['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
#             otherParam['population.isHaveHouse1'] = 'null'   
#             otherParam['population.attentionExtent.id'] = '545'  #关注程度，选择id，可以不填
#             otherParam['population.attentionReason'] = '关注原因'   #可以不填      
#             responseDict = ShiYouRenKouIntf.add_qiTaRenYuan(otherDict=otherParam, username=userInit['DftWangGeUser'], password='11111111')
#             self.assertTrue(responseDict.result, '新增其他人员失败')   
#             
#         #服务情况数据统计检查 —按服务时间： occurDate   logoutType='0'(现在关注)
#             checkPara5=copy.deepcopy(YanPanFenXiPara.checkServiceDict)
#             checkPara5['hasVisitedCount']=0
#             checkPara5['noVisitCount']=8
#             checkPara5['orgname']='测试自动化网格'
#             checkPara5['serviceObjectCount']=8
#             responseDict = YanPanFenXiIntf.check_service(checkPara5,serviceType='importantsPersonnel',queryDateType='occurDate',orgId=orgInit['DftSheQuOrgId'],businessType='all', beginDate='2016-02-01',endDate='2016-02-29',logoutType='0',username=userInit['DftWangGeUser'], password='11111111')
#             self.assertTrue(responseDict, '检查数据不一致') 
#                 
#         #服务情况数据统计检查 —按录入时间： createDate   logoutType=''(全部)
#             checkPara6=copy.deepcopy(YanPanFenXiPara.checkServiceDict)
#             checkPara6['hasVisitedCount']=1
#             checkPara6['noVisitCount']=8
#             checkPara6['orgname']='测试自动化网格'
#             checkPara6['serviceObjectCount']=9
#             responseDict = YanPanFenXiIntf.check_service(checkPara6,serviceType='importantsPersonnel',queryDateType='createDate',orgId=orgInit['DftSheQuOrgId'],businessType='all', beginDate='2016-02-01',endDate='2016-02-29',username=userInit['DftWangGeUser'], password='11111111')
#             self.assertTrue(responseDict, '检查数据不一致') 
#                 
#         #服务人员落实情况数据统计检查 —logoutType='0'(现在关注)
#             checkPara6=copy.deepcopy(YanPanFenXiPara.checkServiceMemberDict)
#             checkPara6['businessCount']=8
#             checkPara6['haveHelpCount']=1
#             checkPara6['orgname']='测试自动化网格'
#             checkPara6['waitHelpCount']=7
#             responseDict = YanPanFenXiIntf.check_serviceMember(checkPara6,serviceType='importantsPersonnel',orgId=orgInit['DftSheQuOrgId'],businessType='all', year='2016',month='2',logoutType='0',username=userInit['DftWangGeUser'], password='11111111')
#             self.assertTrue(responseDict, '检查数据不一致') 
#                 
#         #服务人员落实情况数据统计检查 —logoutType=''(全部)
#             checkPara6=copy.deepcopy(YanPanFenXiPara.checkServiceMemberDict)
#             checkPara6['businessCount']=0
#             checkPara6['haveHelpCount']=0
#             checkPara6['orgname']='测试自动化网格'
#             checkPara6['waitHelpCount']=0
#             responseDict = YanPanFenXiIntf.check_serviceMember(checkPara6,serviceType='importantsPersonnel',orgId=orgInit['DftSheQuOrgId'],businessType='all', year='2016',month='1',username=userInit['DftWangGeUser'], password='11111111')
#             self.assertTrue(responseDict, '检查数据不一致')  
#                 
#         #重点人员概况 
#             checkPara1=copy.deepcopy(YanPanFenXiPara.checkZhongDianRenYuan)
#             checkPara1['allCount']=9
#             checkPara1['attentionCount']=8   #关注人数
#             checkPara1['deathCount']=1
#             checkPara1['logOutCount']=1
#             checkPara1['statisticsType']='测试自动化网格'
#             checkPara1['thisMonthCount']=9 
#             checkPara1['todayAddCount']=9         
#             responseDict = YanPanFenXiIntf.check_ImportantPersonnelGaiKuang(checkPara1,orgId=orgInit['DftWangGeOrgId'],tableType='IMPORTANTPERSONNEL', username=userInit['DftWangGeUser'], password='11111111')
#             self.assertTrue(responseDict, '检查数据不一致') 
# 
#             Data='2016-3-1 '+getCurrentTime()
#             #注意''中的空格不可少
#             setLinuxTime(Data)
#             setLinuxTimeYunWei(Data=Data,password='tianqueshuaige',serverIp=RenZhengZhongXinUrl)
# 
#         #重点人员-总况  立即执行job  ——job科运行没跑成功
#             para={
#              'task.name':'automaticAttentionPopulationStatJob',
#              'job.name':'AutomaticAttentionPopulationStat'
#              }
#             result0=runJobNow(jobPara=para)
#             self.assertTrue(result0,'job运行成功')
#             
#         #重点人员总况列表信息数据统计检查 ——合计
#             checkPara3=copy.deepcopy(YanPanFenXiPara.checkzhongDianRenYuanZongKuang)
#             checkPara3['amount']=9
#             responseDict = YanPanFenXiIntf.check_ImportantPersonnel(checkPara3,orgId=orgInit['DftSheQuOrgId'],type='all_attention_population', year='2016',month='2',username=userInit['DftSheQuUser'], password='11111111')
#             self.assertTrue(responseDict, '检查数据不一致') 
#              
# 
#             deleteParam = copy.deepcopy(YanPanFenXiPara.delDict)
#             deleteParam['populationIds'] = str(CommonIntf.getDbQueryResult(dbCommand = "select t.id from positiveInfos t where t.idcardno='%s'" % xingShiParam2['population.idCardNo']))
#             ret = ShiYouRenKouIntf.delete_xingManShiFang(deleteParam,username=userInit['DftWangGeUser'], password='11111111')
#             self.assertTrue(ret.result, '删除户籍人口失败') 
#         
#         finally:
#             XiaQuGuanLiIntf.xiaQuGuanLiMemberDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
#             #将服务器时间改回正确时间
#             setLinuxTime(Data=getCurrentDateAndTime())
#             setLinuxTimeYunWei(Data=getCurrentDateAndTime(),password='tianqueshuaige',serverIp=RenZhengZhongXinUrl)
#         pass    


#     '''
#     @功能：研判分析-重点人员-刑释人员
#     @ chenyan 2016-5-30
#     '''
#     def test_positiveInfo(self):
#         '''重点人员刑释人员'''
#         #设置linux时间为2015-12-28
#         try:
#             Data='2016-2-1 '+getCurrentTime()
#             #注意''中的空格不可少
#             setLinuxTime(Data)
#             setLinuxTimeYunWei(Data=Data,password='tianqueshuaige',serverIp=RenZhengZhongXinUrl)
# 
#             ShiYouRenKouIntf.deleteAllPopulation()
# 
#             xingShiParam1 = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
#             xingShiParam1['mode']='add'
#             xingShiParam1['population.organization.id'] = orgInit['DftWangGeOrgId']
#             xingShiParam1['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人口or流动人口
#             xingShiParam1['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['xingManShiFangRenYuan']
#             xingShiParam1['population.organization.orgName'] = orgInit['DftWangGeOrg']
#             xingShiParam1['population.idCardNo'] = '330000199911111025'
#             xingShiParam1['population.name'] = '刑满释放人员1'
#             xingShiParam1['actualPersonType'] = xingShiParam1['population.actualPopulationType']
#             xingShiParam1['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
#             xingShiParam1['population.isHaveHouse1'] = 'null'   
#             xingShiParam1['population.caseReason'] = 'Reason'
#             xingShiParam1['population.positiveInfoType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '刑释人员'") 
#             xingShiParam1['population.laborEduAddress'] = '劳教所'
#             xingShiParam1['population.imprisonmentDate'] = '2weeks'
#             xingShiParam1['population.releaseOrBackDate'] = '2016-2-10' #Time.getCurrentDate()  
#             responseDict = ShiYouRenKouIntf.add_xingManShiFang(xingShiParam1, username=userInit['DftWangGeUser'], password='11111111')
#             self.assertTrue(responseDict.result, '新增刑满释放人员失败') 
#                     
#             xingShiParam2 = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
#             xingShiParam2['mode']='add'
#             xingShiParam2['population.organization.id'] = orgInit['DftWangGeOrgId']
#             xingShiParam2['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人口or流动人口
#             xingShiParam2['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['xingManShiFangRenYuan']
#             xingShiParam2['population.organization.orgName'] = orgInit['DftWangGeOrg']
#             xingShiParam2['population.idCardNo'] = '330000199911110125'
#             xingShiParam2['population.name'] = '刑满释放人员2'
#             xingShiParam2['actualPersonType'] = xingShiParam2['population.actualPopulationType']
#             xingShiParam2['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
#             xingShiParam2['population.isHaveHouse1'] = 'null'   
#             xingShiParam2['population.caseReason'] = 'Reason'
#             xingShiParam2['population.positiveInfoType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '刑释人员'") 
#             xingShiParam2['population.laborEduAddress'] = '劳教所'
#             xingShiParam2['population.imprisonmentDate'] = '2weeks'
#             xingShiParam2['population.releaseOrBackDate'] = '2016-2-10' #Time.getCurrentDate()  
#             responseDict = ShiYouRenKouIntf.add_xingManShiFang(xingShiParam2, username=userInit['DftWangGeUser'], password='11111111')
#             self.assertTrue(responseDict.result, '新增刑满释放人员失败') 
#         
#         #添加成员库成员            
#             fuWuParam = copy.deepcopy(ShiYouRenKouPara.fuWuRenYuanDict)      
#             fuWuParam['serviceTeamMemberBase.org.id'] = orgInit['DftWangGeOrgId']
#             fuWuParam['serviceTeamMemberBase.name'] = '服务%s'%CommonUtil.createRandomString()
#             fuWuParam['serviceTeamMemberBase.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别(男、女)', displayName='男')     
#             fuWuParam['serviceTeamMemberBase.mobile'] = '13011111119'
#             responseDict = ShiYouRenKouIntf.add_FuWuChengYuan(fuWuParam, username=userInit['DftWangGeUser'], password='11111111')
#             self.assertTrue(responseDict.result, '新增成员失败')    
#         #添加服务记录               
#             RecordParam = copy.deepcopy(ShiYouRenKouPara.serviceRecordDict) 
#             RecordParam['mode'] = 'add'   
#             RecordParam['serviceRecord.organization.id'] = orgInit['DftWangGeOrgId']  
#             RecordParam['isSubmit'] = 'true'
#             RecordParam['serviceRecord.occurDate'] = '2016-02-10'   #Time.getCurrentDate() 
#             RecordParam['serviceRecord.occurPlace'] = '地点%s'%CommonUtil.createRandomString()
#             RecordParam['serviceRecord.serviceMembers'] = '%s-服务-0'%CommonIntf.getDbQueryResult(dbCommand = "select t.id from Serviceteammemberbase  t where t.name='%s'" %(fuWuParam['serviceTeamMemberBase.name']))
#             RecordParam['serviceRecord.serviceObjects'] = '%s-%s-rectificativePerson' %(CommonIntf.getDbQueryResult(dbCommand = "select t.id from Positiveinfos t where t.idcardno='%s' " % xingShiParam2['population.idCardNo']),xingShiParam2['population.name'])
#             responseDict = ShiYouRenKouIntf.add_serviceRecordHuJiRenKou(RecordDict=RecordParam, username=userInit['DftWangGeUser'], password='11111111')
#             self.assertTrue(responseDict.result, '新增服务事件失败')
#                     
#             xingShiParam3 = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
#             xingShiParam3['mode']='add'
#             xingShiParam3['population.organization.id'] = orgInit['DftWangGeOrgId']
#             xingShiParam3['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人口or流动人口
#             xingShiParam3['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['xingManShiFangRenYuan']
#             xingShiParam3['population.organization.orgName'] = orgInit['DftWangGeOrg']
#             xingShiParam3['population.idCardNo'] = '330000199911110026'
#             xingShiParam3['population.name'] = '刑满释放人员3'
#             xingShiParam3['actualPersonType'] = xingShiParam3['population.actualPopulationType']
#             xingShiParam3['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
#             xingShiParam3['population.isHaveHouse1'] = 'null'   
#             xingShiParam3['population.caseReason'] = 'Reason'
#             xingShiParam3['population.positiveInfoType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '解教人员'") 
#             xingShiParam3['population.laborEduAddress'] = '劳教所'
#             xingShiParam3['population.imprisonmentDate'] = '2weeks'
#             xingShiParam3['population.releaseOrBackDate'] = '2016-2-10' #Time.getCurrentDate()
#             responseDict = ShiYouRenKouIntf.add_xingManShiFang(xingShiParam3, username=userInit['DftWangGeUser'], password='11111111')
#             self.assertTrue(responseDict.result, '新增刑满释放人员失败') 
#         #添加服务成员            
#             MemberParam = copy.deepcopy(ShiYouRenKouPara.serviceMemberDict)      
#             MemberParam['serviceMemberWithObject.memberId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from Serviceteammemberbase t where t.name='%s'" % (fuWuParam['serviceTeamMemberBase.name']))
#             MemberParam['serviceMemberWithObject.objectType'] = 'positiveInfo'
#             MemberParam['serviceMemberWithObject.objectName'] = xingShiParam3['population.name']   
#             MemberParam['serviceMemberWithObject.objectId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from positiveInfos t where t.idcardno='%s' " % xingShiParam3['population.idCardNo'])
#             MemberParam['serviceMemberWithObject.teamMember'] = ' 1'
#             MemberParam['serviceMemberWithObject.onDuty'] = '1'
#             MemberParam['serviceMemberWithObject.objectLogout'] = '1' 
#             responseDict = ShiYouRenKouIntf.add_serviceMemberHuJiRenKou(serviceDict=MemberParam, username=userInit['DftWangGeUser'], password='11111111')
#             self.assertTrue(responseDict.result, '新增服务人员失败')
#                     
#             xingShiParam4 = copy.deepcopy(ShiYouRenKouPara.zhongDianPopulationObject) 
#             xingShiParam4['mode']='add'
#             xingShiParam4['population.organization.id'] = orgInit['DftWangGeOrgId']
#             xingShiParam4['population.actualPopulationType'] = ShiYouRenKouPara.actualPopulationTypeDict['huJiRenKou']  #属于户籍人口or流动人口
#             xingShiParam4['population.attentionPopulationType'] = ShiYouRenKouPara.populationTypeDict['xingManShiFangRenYuan']
#             xingShiParam4['population.organization.orgName'] = orgInit['DftWangGeOrg']
#             xingShiParam4['population.idCardNo'] = '330000199911110126'
#             xingShiParam4['population.name'] = '刑满释放人员4'
#             xingShiParam4['actualPersonType'] = xingShiParam4['population.actualPopulationType']
#             xingShiParam4['population.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别', displayName='男')
#             xingShiParam4['population.isHaveHouse1'] = 'null'   
#             xingShiParam4['population.caseReason'] = 'Reason'
#             xingShiParam4['population.positiveInfoType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select * from propertydicts p where p.displayname = '解教人员'") 
#             xingShiParam4['population.laborEduAddress'] = '劳教所'
#             xingShiParam4['population.imprisonmentDate'] = '2weeks'
#             xingShiParam4['population.releaseOrBackDate'] = '2016-2-10' #Time.getCurrentDate()
#             responseDict = ShiYouRenKouIntf.add_xingManShiFang(xingShiParam4, username=userInit['DftWangGeUser'], password='11111111')
#             self.assertTrue(responseDict.result, '新增刑满释放人员失败') 
#         #取消关注
#             detaileParam = copy.deepcopy(ShiYouRenKouPara.logoutHuJiDict)
#             detaileParam['populationIds'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from positiveInfos t where t.idcardno='%s'" % xingShiParam4['population.idCardNo'] )
#             detaileParam['population.logoutDetail.logout'] = '1'
#             detaileParam['population.logoutDetail.logoutDate'] = Time.getCurrentDateAndTime()
#             detaileParam['population.logoutDetail.logoutReason'] = '取消关注'
#             ret = ShiYouRenKouIntf.logout_xingManShiFang(detaileParam,username=userInit['DftWangGeUser'], password='11111111')
# #             self.assertTrue(ret.result, '人口取消关注失败')
#              
#             Data='2016-3-1 '+getCurrentTime()
#             #注意''中的空格不可少
#             setLinuxTime(Data)
#             setLinuxTimeYunWei(Data=Data,password='tianqueshuaige',serverIp=RenZhengZhongXinUrl)
#              
#             #总况-重点人员各月份图表立即执行job   
#             para={
#              'task.name':'automaticAttentionPopulationStatJob',
#              'job.name':'AutomaticAttentionPopulationStat'
#              }
#             result0=runJobNow(jobPara=para)
#             self.assertTrue(result0,'job运行成功')
#              
#         #列表信息数据统计检查 ——刑释人员   
#             checkPara1=copy.deepcopy(YanPanFenXiPara.checkzhongDianRenYuanZongKuang)
#             checkPara1['typeName']='刑释人员'
#             checkPara1['sum']=2
#             checkPara1['helped']=0
#             checkPara1['noHelp']=2
#             responseDict = YanPanFenXiIntf.check_positiveInfo(checkPara1,orgId=orgInit['DftSheQuOrgId'],type='positiveInfo', year='2016',month='2',username=userInit['DftSheQuUser'], password='11111111')
#             self.assertTrue(responseDict, '检查数据不一致') 
#             
#         #列表信息数据统计检查 ——解教人员   
#             checkPara2=copy.deepcopy(YanPanFenXiPara.checkzhongDianRenYuanZongKuang)
#             checkPara2['typeName']='解教人员'
#             checkPara2['sum']=2
#             checkPara2['helped']=1
#             checkPara2['noHelp']=1
#             responseDict = YanPanFenXiIntf.check_positiveInfo(checkPara2,orgId=orgInit['DftSheQuOrgId'],type='positiveInfo', year='2016',month='2',username=userInit['DftSheQuUser'], password='11111111')
#             self.assertTrue(responseDict, '检查数据不一致') 
#             
#         #列表信息数据统计检查 ——合计
#             checkPara3=copy.deepcopy(YanPanFenXiPara.checkzhongDianRenYuanZongKuang)
#             checkPara3['typeName']='合计'
#             checkPara3['sum']=4
#             checkPara3['helped']=1
#             checkPara3['noHelp']=3
#             responseDict = YanPanFenXiIntf.check_positiveInfo(checkPara3,orgId=orgInit['DftSheQuOrgId'],type='positiveInfo', year='2016',month='2',username=userInit['DftSheQuUser'], password='11111111')
#             self.assertTrue(responseDict, '检查数据不一致') 
#             
#         #区域分布图数据统计检查 
#             checkPara3=copy.deepcopy(YanPanFenXiPara.checkzhongDianRenYuanZongKuang)
#             checkPara3['name']='刑释人员'
#             responseDict = YanPanFenXiIntf.check_positiveInfoQuYu(checkPara3,orgId=orgInit['DftSheQuOrgId'],type='positiveInfo', year='2016',month='2',username=userInit['DftSheQuUser'], password='11111111')
#             self.assertTrue(responseDict, '检查数据不一致') 
#         
#         #服务情况数据统计检查 —按服务时间： occurDate   logoutType='0'(现在关注)
#             checkPara5=copy.deepcopy(YanPanFenXiPara.checkServiceDict)
#             checkPara5['hasVisitedCount']=0
#             checkPara5['noVisitCount']=3
#             checkPara5['orgname']='测试自动化网格'
#             checkPara5['serviceObjectCount']=3
#             responseDict = YanPanFenXiIntf.check_service(checkPara5,serviceType='importantsPersonnel',queryDateType='occurDate',orgId=orgInit['DftSheQuOrgId'],businessType='positiveInfo', beginDate='2016-02-01',endDate='2016-02-29',logoutType='0',username=userInit['DftWangGeUser'], password='11111111')
#             self.assertTrue(responseDict, '检查数据不一致') 
#             
#         #服务情况数据统计检查 —按录入时间： createDate   logoutType=''(全部)
#             checkPara6=copy.deepcopy(YanPanFenXiPara.checkServiceDict)
#             checkPara6['hasVisitedCount']=0
#             checkPara6['noVisitCount']=4
#             checkPara6['orgname']='测试自动化网格'
#             checkPara6['serviceObjectCount']=4
#             responseDict = YanPanFenXiIntf.check_service(checkPara6,serviceType='importantsPersonnel',queryDateType='createDate',orgId=orgInit['DftSheQuOrgId'],businessType='positiveInfo', beginDate='2016-02-01',endDate='2016-02-29',username=userInit['DftWangGeUser'], password='11111111')
#             self.assertTrue(responseDict, '检查数据不一致') 
# 
#         #服务人员落实情况数据统计检查 —logoutType='0'(现在关注)
#             checkPara6=copy.deepcopy(YanPanFenXiPara.checkServiceMemberDict)
#             checkPara6['businessCount']=3
#             checkPara6['haveHelpCount']=1
#             checkPara6['orgname']='测试自动化网格'
#             checkPara6['waitHelpCount']=2
#             responseDict = YanPanFenXiIntf.check_serviceMember(checkPara6,serviceType='importantsPersonnel',orgId=orgInit['DftSheQuOrgId'],businessType='positiveInfo', year='2016',month='2',logoutType='0',username=userInit['DftWangGeUser'], password='11111111')
#             self.assertTrue(responseDict, '检查数据不一致') 
#             
#         #服务人员落实情况数据统计检查 —logoutType=''(全部)
#             checkPara6=copy.deepcopy(YanPanFenXiPara.checkServiceMemberDict)
#             checkPara6['businessCount']=0
#             checkPara6['haveHelpCount']=0
#             checkPara6['orgname']='测试自动化网格'
#             checkPara6['waitHelpCount']=0
#             responseDict = YanPanFenXiIntf.check_serviceMember(checkPara6,serviceType='importantsPersonnel',orgId=orgInit['DftSheQuOrgId'],businessType='positiveInfo', year='2016',month='1',username=userInit['DftWangGeUser'], password='11111111')
#             self.assertTrue(responseDict, '检查数据不一致') 
# 
#         finally:
#             XiaQuGuanLiIntf.xiaQuGuanLiMemberDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
#             #将服务器时间改回正确时间
#             setLinuxTime(Data=getCurrentDateAndTime())
#             setLinuxTimeYunWei(Data=getCurrentDateAndTime(),password='tianqueshuaige',serverIp=RenZhengZhongXinUrl)
#         pass


#     '''
#     @功能：研判分析-总况-重点场所统计                问题：后台管理服务情况，选择重点场所后页面卡死
#     @ chenyan 2016-5-25
#     '''
#     def test_ZhongDianChangSuoZongKuang(self):
#         '''总况-重点场所统计'''
#         #设置linux时间为2015-12-28
#         try:
#             Data='2016-2-1 '+getCurrentTime()
#             #注意''中的空格不可少
#             setLinuxTime(Data)
#             setLinuxTimeYunWei(Data=Data,password='tianqueshuaige',serverIp=RenZhengZhongXinUrl)
# 
#             ZuZhiChangSuoIntf.deleteAllPopulation()
# 
#         #新增安全生产重点1
#             testCase_04Param = copy.deepcopy(ZuZhiChangSuoPara.addAnQuanShengChan) 
#             testCase_04Param['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
#             testCase_04Param['enterprise.name'] = '测试安全生产重点%s' % CommonUtil.createRandomString()
#             testCase_04Param['enterprise.keyType'] = 'safetyProductionKey'
#             testCase_04Param['mode'] = 'add'
#             testCase_04Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
#             testCase_04Param['placeTypeName'] = '安全生产重点'
#             testCase_04Param['enterprise.address'] = '测试地址1'
#             testCase_04Param['enterprise.legalPerson'] = '法人代表1'
#             testCase_04Param['enterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='企业类型', displayName='规上企业')
#             responseDict = ZuZhiChangSuoIntf.addAnQuanShengChan(AnQuanShengChanDict=testCase_04Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
#             self.assertTrue(responseDict.result, '新增失败')   
# 
#         #新增服务成员
#             XiaQuGuanLiIntf.xiaQuGuanLiMemberDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
#             Premise_01Param = copy.deepcopy(ZuZhiChangSuoPara.FuWuChengYuanObject) 
#             Premise_01Param['serviceTeamMemberBase.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
#             Premise_01Param['serviceTeamMemberBase.job'] = '测试职位3'
#             Premise_01Param['serviceTeamMemberBase.name'] = '测试服务成员%s'% CommonUtil.createRandomString()
#             Premise_01Param['isSubmit'] = 'true'
#             Premise_01Param['serviceTeamMemberBase.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别(男、女)', displayName='男')
#             Premise_01Param['serviceTeamMemberBase.mobile'] = '13011111111'
#             responseDict = ZuZhiChangSuoIntf.addFuWuChengYuan(FuWuChengYuanDict=Premise_01Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
#             self.assertTrue(responseDict.result, '新增失败')
#             
#         #新增治安管理负责人
#             testCase_20Param = copy.deepcopy(ZuZhiChangSuoPara.addGuanLiZhiAn) 
#             testCase_20Param['serviceMemberWithObject.memberId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from SERVICETEAMMEMBERBASE t where t.name='%s'"%(Premise_01Param['serviceTeamMemberBase.name']))
#             testCase_20Param['serviceMemberWithObject.objectId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from enterprises t where t.name='%s'"%testCase_04Param['enterprise.name'])
#             testCase_20Param['serviceMemberWithObject.objectName'] = testCase_04Param['enterprise.name']
#             testCase_20Param['serviceMemberWithObject.objectType'] = 'SAFETYPRODUCTIONKEY'
#             testCase_20Param['serviceMemberWithObject.objectLogout'] = '1'
#             testCase_20Param['serviceMemberWithObject.onDuty'] = '1'
#             testCase_20Param['serviceMemberWithObject.teamMember'] = '1'
#             responseDict = ZuZhiChangSuoIntf.addGuanLiZhiAn(GuanLiZhiAnDict=testCase_20Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
# 
#         #新增巡场记录
#             ZZCSCase_04Param = copy.deepcopy(ZuZhiChangSuoPara.XunChangQingKuangObject) 
#             ZZCSCase_04Param['serviceRecord.organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
#             ZZCSCase_04Param['serviceRecord.recordType'] = '0'
#             ZZCSCase_04Param['serviceRecord.teamId'] = '0'
#             ZZCSCase_04Param['mode'] = 'add'
#             ZZCSCase_04Param['isSubmit'] = 'true'
#             ZZCSCase_04Param['serviceRecord.userOrgId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
#             ZZCSCase_04Param['serviceRecord.occurDate'] = '2016-02-10'
#             ZZCSCase_04Param['serviceRecord.occurPlace'] = '服务地点%s'%CommonUtil.createRandomString()
#             ZZCSCase_04Param['serviceRecord.serviceMembers'] = '%s-%s-0'%(CommonIntf.getDbQueryResult(dbCommand = "select t.id from SERVICETEAMMEMBERBASE t where t.name='%s'"%Premise_01Param['serviceTeamMemberBase.name']),Premise_01Param['serviceTeamMemberBase.name'])
#             ZZCSCase_04Param['serviceRecord.serviceObjects'] = '%s-%s-SAFETYPRODUCTIONKEY'%(CommonIntf.getDbQueryResult(dbCommand = "select t.id from enterprises t where t.name='%s'"% testCase_04Param['enterprise.name']),testCase_04Param['enterprise.name'])
#             responseDict = ZuZhiChangSuoIntf.addXunChangQingKuang(XunChangQingKuangDict=ZZCSCase_04Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
# 
#         #新增消防安全重点2
#             testCase_05Param = copy.deepcopy(ZuZhiChangSuoPara.addXiaoFangAnQuan) 
#             testCase_05Param['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
#             testCase_05Param['enterprise.name'] = '测试场所名称%s' % CommonUtil.createRandomString()
#             testCase_05Param['enterprise.keyType'] = 'fireSafetyKey'
#             testCase_05Param['mode'] = 'add'
#             testCase_05Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
#             testCase_05Param['placeTypeName'] = '消防安全重点'
#             testCase_05Param['enterprise.address'] = '测试场所地址1'
#             testCase_05Param['enterprise.legalPerson'] = '测试负责人'
#             testCase_05Param['enterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='消防安全重点类别', displayName='商场')
#             responseDict = ZuZhiChangSuoIntf.addXiaoFangAnQuan(XiaoFangAnQuanDict=testCase_05Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
#             self.assertTrue(responseDict.result, '新增失败')  
# 
#         #取消关注
#             testCaseParam = copy.deepcopy(ZuZhiChangSuoPara.addGuanLiZhiAn) 
#             testCaseParam['dailogName'] = 'fireSafetyEnterprise'
#             testCaseParam['locationIds'] = '%s,'% CommonIntf.getDbQueryResult(dbCommand = "select t.id from enterprises t where t.name='%s'"%testCase_05Param['enterprise.name'])
#             testCaseParam['location.isEmphasis'] = 'true'
#             testCaseParam['location.logOutTime'] = '2016-2-10'
#             testCaseParam['location.logOutReason'] = '取消关注原因'
#             responseDict = YanPanFenXiIntf.pdateEmphasise(testCaseParam, username=InitDefaultPara.userInit['DftWangGeUser1'], password='11111111')
# 
#         #新增治安重点3
#             testCase_06Param = copy.deepcopy(ZuZhiChangSuoPara.addZhiAnZhongDian) 
#             testCase_06Param['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
#             testCase_06Param['enterprise.name'] = '测试场所名称%s' % CommonUtil.createRandomString()
#             testCase_06Param['enterprise.keyType'] = 'securityKey'
#             testCase_06Param['mode'] = 'add'
#             testCase_06Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
#             testCase_06Param['placeTypeName'] = '治安重点'
#             testCase_06Param['enterprise.address'] = '测试场所地址1'
#             testCase_06Param['enterprise.legalPerson'] = '测试负责人'
#             testCase_06Param['enterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='治安重点类别', displayName='城乡结合部')
#             responseDict = ZuZhiChangSuoIntf.addZhiAnZhongDian(ZhiAnZhongDianDict=testCase_06Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
#             self.assertTrue(responseDict.result, '新增失败')  
#             
#         #新增学校4
#             testCase_07Param = copy.deepcopy(ZuZhiChangSuoPara.addXueXiao) 
#             testCase_07Param['orgId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
#             testCase_07Param['school.chineseName'] = '测试学校名称%s' % CommonUtil.createRandomString()
#             testCase_07Param['school.kind.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='学校性质', displayName='公办')
#             testCase_07Param['mode'] = 'add'
#             testCase_07Param['school.hasCertificate'] = '请选择'
#             testCase_07Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
#             testCase_07Param['placeTypeName'] = '学校'
#             testCase_07Param['school.address'] = '测试学校地址1'
#             testCase_07Param['school.president'] = '测试校长'
#             testCase_07Param['school.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='学校类型', displayName='小学')
#             responseDict = ZuZhiChangSuoIntf.addXueXiao(XueXiaoDict=testCase_07Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
#             self.assertTrue(responseDict.result, '新增失败')         
#     
#         #新增医院5
#             testCase_08Param = copy.deepcopy(ZuZhiChangSuoPara.addYiYuan) 
#             testCase_08Param['organizationId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
#             testCase_08Param['hospital.hospitalName'] = '测试医院名称%s' % CommonUtil.createRandomString()
#             testCase_08Param['hospital.personLiableTelephone'] = '1234-12341234'
#             testCase_08Param['mode'] = 'add'
#             testCase_08Param['hospital.organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
#             testCase_08Param['hospital.personLiableMobileNumber'] = '13411111111'
#             testCase_08Param['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
#             testCase_08Param['hospital.address'] = '测试医院地址1'
#             testCase_08Param['hospital.personLiable'] = '测试综治负责人'
#             responseDict = ZuZhiChangSuoIntf.addYiYuan(YiYuanDict=testCase_08Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
#             self.assertTrue(responseDict.result, '新增失败') 
#     
#         #新增危险化学品单位6
#             testCase_09Param = copy.deepcopy(ZuZhiChangSuoPara.addWeiXianHuaXuePing) 
#             testCase_09Param['organizationId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
#             testCase_09Param['location.unitName'] = '测试单位名称%s' % CommonUtil.createRandomString()
#             testCase_09Param['mode'] = 'add'
#             testCase_09Param['location.organization.orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
#             responseDict = ZuZhiChangSuoIntf.addWeiXianHuaXuePing(WeiXianHuaXuePingDict=testCase_09Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
#             self.assertTrue(responseDict.result, '新增失败')  
#             
#         #新增上网服务单位7
#             testCase_10Param = copy.deepcopy(ZuZhiChangSuoPara.addShangWanFuWu) 
#             testCase_10Param['location.organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
#             testCase_10Param['location.placeName'] = '测试单位名称%s' % CommonUtil.createRandomString()
#             testCase_10Param['mode'] = 'add'
#             testCase_10Param['ajaxUrl'] = '/baseinfo/internetBarManage/hasDuplicateInternetBarLocation.action'
#             testCase_10Param['location.organization.orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
#             responseDict = ZuZhiChangSuoIntf.addShangWanFuWu(ShangWanFuWuDict=testCase_10Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
#             self.assertTrue(responseDict.result, '新增失败') 
#             
#         #新增公共场所8
#             testCase_11Param = copy.deepcopy(ZuZhiChangSuoPara.addShangWanFuWu) 
#             testCase_11Param['location.organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
#             testCase_11Param['location.placeName'] = '测试公共场所名称%s' % CommonUtil.createRandomString()
#             testCase_11Param['location.placeAddress'] = '测试场所地址'
#             testCase_11Param['mode'] = 'add'
#             testCase_11Param['ajaxUrl'] = '/baseinfo/publicPlaceManage/hasDuplicatePublicPlaceLocation.action'
#             testCase_11Param['location.organization.orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
#             responseDict = ZuZhiChangSuoIntf.addGongGongChangSuo(GongGongChangSuoDict=testCase_11Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
#             self.assertTrue(responseDict.result, '新增失败')         
#     
#         #新增公共复杂场所9
#             testCase_12Param = copy.deepcopy(ZuZhiChangSuoPara.addGongGongFuZaChangSuo) 
#             testCase_12Param['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
#             testCase_12Param['commonComplexPlace.name'] = '测试公共复杂场所名称%s' % CommonUtil.createRandomString()
#             testCase_12Param['commonComplexPlace.legalPerson'] = '测试负责人'
#             testCase_12Param['mode'] = 'add'
#             testCase_12Param['commonComplexPlace_orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
#             responseDict = ZuZhiChangSuoIntf.addGongGongFuZaChangSuo(GongGongFuZaChangSuoDict=testCase_12Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
#             self.assertTrue(responseDict.result, '新增失败') 
#             
#         #服务情况数据统计检查 —按服务时间： occurDate   logoutType='0'(现在关注)
#             checkPara5=copy.deepcopy(YanPanFenXiPara.checkServiceDict)
#             checkPara5['hasVisitedCount']=0
#             checkPara5['noVisitCount']=8
#             checkPara5['orgname']='测试自动化网格'
#             checkPara5['serviceObjectCount']=8
#             responseDict = YanPanFenXiIntf.check_service(checkPara5,serviceType='importantPlace',queryDateType='occurDate',orgId=orgInit['DftSheQuOrgId'],businessType='all', beginDate='2016-02-01',endDate='2016-02-29',logoutType='0',username=userInit['DftWangGeUser'], password='11111111')
#             self.assertTrue(responseDict, '检查数据不一致') 
# 
#         #服务情况数据统计检查 —按录入时间： createDate   logoutType=''(全部)
#             checkPara6=copy.deepcopy(YanPanFenXiPara.checkServiceDict)
#             checkPara6['hasVisitedCount']=1
#             checkPara6['noVisitCount']=8
#             checkPara6['orgname']='测试自动化网格'
#             checkPara6['serviceObjectCount']=9
#             responseDict = YanPanFenXiIntf.check_service(checkPara6,serviceType='importantPlace',queryDateType='createDate',orgId=orgInit['DftSheQuOrgId'],businessType='all', beginDate='2016-02-01',endDate='2016-02-29',username=userInit['DftWangGeUser'], password='11111111')
#             self.assertTrue(responseDict, '检查数据不一致') 
#                 
#         #服务人员落实情况数据统计检查 —logoutType='0'(现在关注)
#             checkPara6=copy.deepcopy(YanPanFenXiPara.checkServiceMemberDict)
#             checkPara6['businessCount']=8
#             checkPara6['haveHelpCount']=1
#             checkPara6['orgname']='测试自动化网格'
#             checkPara6['waitHelpCount']=7
#             responseDict = YanPanFenXiIntf.check_serviceMember(checkPara6,serviceType='importantPlace',orgId=orgInit['DftSheQuOrgId'],businessType='all', year='2016',month='2',logoutType='0',username=userInit['DftWangGeUser'], password='11111111')
#             self.assertTrue(responseDict, '检查数据不一致') 
#                 
#         #服务人员落实情况数据统计检查 —logoutType=''(全部)
#             checkPara6=copy.deepcopy(YanPanFenXiPara.checkServiceMemberDict)
#             checkPara6['businessCount']=0
#             checkPara6['haveHelpCount']=0
#             checkPara6['orgname']='测试自动化网格'
#             checkPara6['waitHelpCount']=0
#             responseDict = YanPanFenXiIntf.check_serviceMember(checkPara6,serviceType='importantPlace',orgId=orgInit['DftSheQuOrgId'],businessType='all', year='2016',month='1',username=userInit['DftWangGeUser'], password='11111111')
#             self.assertTrue(responseDict, '检查数据不一致')  
# 
#         #重点场所概况 
#             checkPara1=copy.deepcopy(YanPanFenXiPara.checkZhongDianRenYuan)
#             checkPara1['allCount']=9
#             checkPara1['attentionCount']=8   #关注场所
#             checkPara1['statisticsType']='测试自动化网格'
#             checkPara1['thisMonthCount']=9 
#             checkPara1['todayAddCount']=9         
#             responseDict = YanPanFenXiIntf.check_ImportantPersonnelGaiKuang(checkPara1,orgId=orgInit['DftWangGeOrgId'],tableType='IMPORTANTPLACE', username=userInit['DftWangGeUser'], password='11111111')
#             self.assertTrue(responseDict, '检查数据不一致') 
#             
#             Data='2016-3-1 '+getCurrentTime()
#             #注意''中的空格不可少
#             setLinuxTime(Data)
#             setLinuxTimeYunWei(Data=Data,password='tianqueshuaige',serverIp=RenZhengZhongXinUrl)
#              
#         #重点场所-总况  立即执行job  ——job科运行没跑成功
#             para={
#              'task.name':'baseInfoStatTypeJob',
#              'job.name':'BaseInfoStatTypeJob'
#              }
#             result0=runJobNow(jobPara=para)
#             self.assertTrue(result0,'job运行成功')
#                 
#         #重点场所总况列表信息数据统计检查 ——合计
#             checkPara3=copy.deepcopy(YanPanFenXiPara.checkzhongDianRenYuanZongKuang)
#             checkPara3['amount']=9
#             responseDict = YanPanFenXiIntf.check_ImportantPlace(checkPara3,orgId=orgInit['DftSheQuOrgId'],keyType='IMPORTANTPLACE', year='2016',month='2',username=userInit['DftSheQuUser'], password='11111111')
#             self.assertTrue(responseDict, '检查数据不一致') 
# 
# 
#         finally:
#             XiaQuGuanLiIntf.xiaQuGuanLiMemberDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
#             #将服务器时间改回正确时间
#             setLinuxTime(Data=getCurrentDateAndTime())
#             setLinuxTimeYunWei(Data=getCurrentDateAndTime(),password='tianqueshuaige',serverIp=RenZhengZhongXinUrl)
#         pass    

    '''
    @功能：研判分析-安全生产重点统计
    @ chenyan 2016-6-2
    '''
    def test_safetyProductionKey(self):
        '''安全生产重点统计'''
        #设置linux时间为2015-12-28
        try:
            data='2016-2-1 '+getCurrentTime()
            #注意''中的空格不可少
            setLinuxTime(data)
            setLinuxTimeYunWei(data=data,password='tianqueshuaige',serverIp=RenZhengZhongXinUrl)

            ZuZhiChangSuoIntf.deleteAllPopulation()

        #新增安全生产重点
            testCaseParam1 = copy.deepcopy(ZuZhiChangSuoPara.addAnQuanShengChan) 
            testCaseParam1['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
            testCaseParam1['enterprise.name'] = '测试安全生产重点1%s' % CommonUtil.createRandomString()
            testCaseParam1['enterprise.keyType'] = 'safetyProductionKey'
            testCaseParam1['mode'] = 'add'
            testCaseParam1['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
            testCaseParam1['placeTypeName'] = '安全生产重点'
            testCaseParam1['enterprise.address'] = '测试地址'
            testCaseParam1['enterprise.legalPerson'] = '法人代表'
            testCaseParam1['enterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='企业类型', displayName='规上企业')
            responseDict = ZuZhiChangSuoIntf.addAnQuanShengChan(testCaseParam1, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增失败')  

        #新增安全生产重点
            testCaseParam2 = copy.deepcopy(ZuZhiChangSuoPara.addAnQuanShengChan) 
            testCaseParam2['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
            testCaseParam2['enterprise.name'] = '测试安全生产重点2%s' % CommonUtil.createRandomString()
            testCaseParam2['enterprise.keyType'] = 'safetyProductionKey'
            testCaseParam2['mode'] = 'add'
            testCaseParam2['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
            testCaseParam2['placeTypeName'] = '安全生产重点'
            testCaseParam2['enterprise.address'] = '测试地址1'
            testCaseParam2['enterprise.legalPerson'] = '法人代表1'
            testCaseParam2['enterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='企业类型', displayName='规上企业')
            responseDict = ZuZhiChangSuoIntf.addAnQuanShengChan(testCaseParam2, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增失败')   

        #新增服务成员
            XiaQuGuanLiIntf.xiaQuGuanLiMemberDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
            Premise_01Param = copy.deepcopy(ZuZhiChangSuoPara.FuWuChengYuanObject) 
            Premise_01Param['serviceTeamMemberBase.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
            Premise_01Param['serviceTeamMemberBase.job'] = '测试职位3'
            Premise_01Param['serviceTeamMemberBase.name'] = '测试服务成员%s'% CommonUtil.createRandomString()
            Premise_01Param['isSubmit'] = 'true'
            Premise_01Param['serviceTeamMemberBase.gender.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='性别(男、女)', displayName='男')
            Premise_01Param['serviceTeamMemberBase.mobile'] = '13011111112'
            responseDict = ZuZhiChangSuoIntf.addFuWuChengYuan(FuWuChengYuanDict=Premise_01Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增失败')

        #新增巡场记录
            ZZCSCase_04Param = copy.deepcopy(ZuZhiChangSuoPara.XunChangQingKuangObject) 
            ZZCSCase_04Param['serviceRecord.organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
            ZZCSCase_04Param['serviceRecord.recordType'] = '0'
            ZZCSCase_04Param['serviceRecord.teamId'] = '0'
            ZZCSCase_04Param['mode'] = 'add'
            ZZCSCase_04Param['isSubmit'] = 'true'
            ZZCSCase_04Param['serviceRecord.userOrgId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
            ZZCSCase_04Param['serviceRecord.occurDate'] = '2016-02-10'
            ZZCSCase_04Param['serviceRecord.occurPlace'] = '服务地点%s'%CommonUtil.createRandomString()
            ZZCSCase_04Param['serviceRecord.serviceMembers'] = '%s-%s-0'%(CommonIntf.getDbQueryResult(dbCommand = "select t.id from SERVICETEAMMEMBERBASE t where t.name='%s'"%Premise_01Param['serviceTeamMemberBase.name']),Premise_01Param['serviceTeamMemberBase.name'])
            ZZCSCase_04Param['serviceRecord.serviceObjects'] = '%s-%s-SAFETYPRODUCTIONKEY'%(CommonIntf.getDbQueryResult(dbCommand = "select t.id from enterprises t where t.name='%s'"% testCaseParam2['enterprise.name']),testCaseParam2['enterprise.name'])
            responseDict = ZuZhiChangSuoIntf.addXunChangQingKuang(XunChangQingKuangDict=ZZCSCase_04Param, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')

        #新增安全生产重点
            testCaseParam3 = copy.deepcopy(ZuZhiChangSuoPara.addAnQuanShengChan) 
            testCaseParam3['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
            testCaseParam3['enterprise.name'] = '测试安全生产重点3%s' % CommonUtil.createRandomString()
            testCaseParam3['enterprise.keyType'] = 'safetyProductionKey'
            testCaseParam3['mode'] = 'add'
            testCaseParam3['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
            testCaseParam3['placeTypeName'] = '安全生产重点'
            testCaseParam3['enterprise.address'] = '测试地址1'
            testCaseParam3['enterprise.legalPerson'] = '法人代表1'
            testCaseParam3['enterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='企业类型', displayName='规上企业')
            responseDict = ZuZhiChangSuoIntf.addAnQuanShengChan(testCaseParam3, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增失败')   
            
        #新增治安管理负责人
            testCase_20Param = copy.deepcopy(ZuZhiChangSuoPara.addGuanLiZhiAn) 
            testCase_20Param['serviceMemberWithObject.memberId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from SERVICETEAMMEMBERBASE t where t.name='%s'"%(Premise_01Param['serviceTeamMemberBase.name']))
            testCase_20Param['serviceMemberWithObject.objectId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from enterprises t where t.name='%s'"%testCaseParam3['enterprise.name'])
            testCase_20Param['serviceMemberWithObject.objectName'] = testCaseParam3['enterprise.name']
            testCase_20Param['serviceMemberWithObject.objectType'] = 'SAFETYPRODUCTIONKEY'
            testCase_20Param['serviceMemberWithObject.objectLogout'] = '1'
            testCase_20Param['serviceMemberWithObject.onDuty'] = '1'
            testCase_20Param['serviceMemberWithObject.teamMember'] = '1'
            responseDict = ZuZhiChangSuoIntf.addGuanLiZhiAn(GuanLiZhiAnDict=testCase_20Param, username=InitDefaultPara.userInit['DftWangGeUser1'], password='11111111')
            
        #新增安全生产重点
            testCaseParam4 = copy.deepcopy(ZuZhiChangSuoPara.addAnQuanShengChan) 
            testCaseParam4['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
            testCaseParam4['enterprise.name'] = '测试安全生产重点4%s' % CommonUtil.createRandomString()
            testCaseParam4['enterprise.keyType'] = 'safetyProductionKey'
            testCaseParam4['mode'] = 'add'
            testCaseParam4['orgName'] = InitDefaultPara.orgInit['DftWangGeOrg']
            testCaseParam4['placeTypeName'] = '安全生产重点'
            testCaseParam4['enterprise.address'] = '测试地址1'
            testCaseParam4['enterprise.legalPerson'] = '法人代表1'
            testCaseParam4['enterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='企业类型', displayName='规上企业')
            responseDict = ZuZhiChangSuoIntf.addAnQuanShengChan(testCaseParam4, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict.result, '新增失败')   
            
        #取消关注
            testCaseParam = copy.deepcopy(ZuZhiChangSuoPara.addGuanLiZhiAn) 
            testCaseParam['dailogName'] = 'fireSafetyEnterprise'
            testCaseParam['locationIds'] = '%s,'% CommonIntf.getDbQueryResult(dbCommand = "select t.id from enterprises t where t.name='%s'"%testCaseParam4['enterprise.name'])
            testCaseParam['location.isEmphasis'] = 'true'
            testCaseParam['location.logOutTime'] = '2016-2-10'
            testCaseParam['location.logOutReason'] = '取消关注原因'
            responseDict = YanPanFenXiIntf.pdateEmphasise(testCaseParam, username=InitDefaultPara.userInit['DftWangGeUser1'], password='11111111')
            self.assertTrue(responseDict.result, '取消关注失败')

        
        #服务情况数据统计检查 —按服务时间： occurDate   logoutType='0'(现在关注)
            checkPara5=copy.deepcopy(YanPanFenXiPara.checkServiceDict)
            checkPara5['hasVisitedCount']=1
            checkPara5['noVisitCount']=2
            checkPara5['orgname']='测试自动化网格'
            checkPara5['serviceObjectCount']=3
            responseDict = YanPanFenXiIntf.check_service(checkPara5,serviceType='importantPlace',queryDateType='occurDate',orgId=orgInit['DftSheQuOrgId'],businessType='SAFETYPRODUCTIONKEY', beginDate='2016-02-01',endDate='2016-02-29',logoutType='0',username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict, '检查数据不一致') 
            
        #服务情况数据统计检查 —按录入时间： createDate   logoutType=''(全部)
            checkPara6=copy.deepcopy(YanPanFenXiPara.checkServiceDict)
            checkPara6['hasVisitedCount']=1
            checkPara6['noVisitCount']=3
            checkPara6['orgname']='测试自动化网格'
            checkPara6['serviceObjectCount']=4
            responseDict = YanPanFenXiIntf.check_service(checkPara6,serviceType='importantPlace',queryDateType='createDate',orgId=orgInit['DftSheQuOrgId'],businessType='SAFETYPRODUCTIONKEY', beginDate='2016-02-01',endDate='2016-02-29',username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict, '检查数据不一致') 

        #服务人员落实情况数据统计检查 —logoutType='0'(现在关注)
            checkPara6=copy.deepcopy(YanPanFenXiPara.checkServiceMemberDict)
            checkPara6['businessCount']=3
            checkPara6['haveHelpCount']=1
            checkPara6['orgname']='测试自动化网格'
            checkPara6['waitHelpCount']=2
            responseDict = YanPanFenXiIntf.check_serviceMember(checkPara6,serviceType='importantPlace',orgId=orgInit['DftSheQuOrgId'],businessType='SAFETYPRODUCTIONKEY', year='2016',month='2',logoutType='0',username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict, '检查数据不一致') 
            
        #服务人员落实情况数据统计检查 —logoutType=''(全部)
            checkPara6=copy.deepcopy(YanPanFenXiPara.checkServiceMemberDict)
            checkPara6['businessCount']=0
            checkPara6['haveHelpCount']=0
            checkPara6['orgname']='测试自动化网格'
            checkPara6['waitHelpCount']=0
            responseDict = YanPanFenXiIntf.check_serviceMember(checkPara6,serviceType='importantPlace',orgId=orgInit['DftSheQuOrgId'],businessType='SAFETYPRODUCTIONKEY', year='2016',month='1',username=userInit['DftWangGeUser'], password='11111111')
            self.assertTrue(responseDict, '检查数据不一致') 
            

            data='2016-3-1 '+getCurrentTime()
            #注意''中的空格不可少
            setLinuxTime(data)
            setLinuxTimeYunWei(data=data,password='tianqueshuaige',serverIp=RenZhengZhongXinUrl)
             
            #总况-重点场所各月份图表立即执行job   
            para={
             'task.name':'baseInfoStatTypeJob',
             'job.name':'BaseInfoStatTypeJob'
            }
            result0=runJobNow(jobPara=para)
            self.assertTrue(result0,'job运行成功')
            
        #列表信息数据统计检查 
            checkPara3=copy.deepcopy(YanPanFenXiPara.checkZhongDianChangSuo)
            checkPara3['helped']=1
            checkPara3['noHelp']=2
            checkPara3['total']=3
            responseDict = YanPanFenXiIntf.check_statAnalysePlace(checkPara3,orgId=orgInit['DftSheQuOrgId'],keyType='SAFETYPRODUCTIONKEY', year='2016',month='2',username=userInit['DftSheQuUser'], password='11111111')
            self.assertTrue(responseDict, '检查数据不一致') 
            
#         #区域分布图数据统计检查
#             checkPara3=copy.deepcopy(YanPanFenXiPara.checkStatAnalysePlace)
#             checkPara3['name']='安全生产重点'
#             responseDict = YanPanFenXiIntf.check_statAnalysePlaceQuYu(checkPara3,orgId=orgInit['DftSheQuOrgId'],keyType='SAFETYPRODUCTIONKEY', year='2016',month='2',username=userInit['DftSheQuUser'], password='11111111')
#             self.assertTrue(responseDict, '检查数据不一致') 

        finally:
            XiaQuGuanLiIntf.xiaQuGuanLiMemberDelAll(username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
            #将服务器时间改回正确时间
            setLinuxTime(data=getCurrentDateAndTime())
            setLinuxTimeYunWei(data=getCurrentDateAndTime(),password='tianqueshuaige',serverIp=RenZhengZhongXinUrl)
        pass



    def tearDown(self):    
        pass

if  __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    suite = unittest.TestSuite()
    suite.addTest(YanPanFenXi("testStatus_004"))

#     suite.addTest(YanPanFenXi("test_ZhongDianRenYuanZongKuang"))
#     suite.addTest(YanPanFenXi("test_positiveInfo"))
#     suite.addTest(YanPanFenXi("test_ZhongDianChangSuoZongKuang"))
#     suite.addTest(YanPanFenXi("test_safetyProductionKey"))

    results = unittest.TextTestRunner().run(suite)
    pass
