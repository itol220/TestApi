# -*- coding:UTF-8 -*-
'''
Created on 2016-3-7

@author: N-286
'''
from __future__ import unicode_literals
from COMMON import Log, Time
from CONFIG.InitDefaultPara import orgInit, userInit
from Interface.PingAnJianShe.Common.CommonIntf import getDbQueryResult, \
    getDbQueryResultList
from Interface.PingAnJianShe.RiChangBanGong.RiChangBanGongIntf import \
    check_workDiary, check_WorkingRecord
from Interface.PingAnJianShe.SystemMgr import SystemMgrIntf
from Interface.PingAnTong.RiChangBanGong.MbRiChangBanGongIntf import \
    mAddWorkDiary, mWorkDairyList, mUpdWorkDiary, mCheckWorkDairyInList, \
    mCheckWorkDairyInViewpage, MbRiChangBanGongInit, mAddMeet, mCheckMeetInList, \
    mMeetList, mUpdMeet
from Interface.PingAnTong.RiChangBanGong.MbRiChangBanGongPara import \
    addWorkDiaryPara1, searchWorkDiaryPara, viewWorlDiartPara, addMeetPara1, \
    searchMeetPara, addFilePara1, searchFilePara, addActivityPara1, \
    searchActivityPara, addOtherPara1, searchOtherPara
import copy
import json
import unittest


class MbRiChangBanGong(unittest.TestCase):


    def setUp(self):
        SystemMgrIntf.initEnv()
        MbRiChangBanGongInit()
        pass

    '''
    @功能：日常办公-工作日志新增、修改
    @ chenhui 2016-3-7
    '''
    def testmRiChangBanGong_001(self):
        '''日常办公-工作日志新增、修改,必填项验证有bug'''
        addPara=copy.deepcopy(addWorkDiaryPara1)
        #验证必填项
        Log.LogOutput( message='验证新增必填项')
        #工作人员
        addPara['workDiary.workUserName']=''
        res=mAddWorkDiary(para=addPara)
        self.assertFalse(res.result, '工作人员必填项验证失败')
        #日志类型
        addPara['workDiary.workUserName']='工作人员'
        addPara['workDiary.diaryType.id']=''
        res=mAddWorkDiary(para=addPara)
        self.assertFalse(res.result, '日志类型必填项验证失败')
        #工作时间
        addPara['workDiary.diaryType.id']=getDbQueryResult(dbCommand = "select id from propertydicts where  displayname='其他' and propertydomainid=(select id from propertydomains where domainname='工作日志类型')")
        addPara['workDiary.workTime']=''
        res=mAddWorkDiary(para=addPara)
        self.assertFalse(res.result, '工作时间必填项验证失败')
        #地点
        addPara['workDiary.workTime']=Time.getCurrentDate()
        addPara['workDiary.workPlace']=''
        res=mAddWorkDiary(para=addPara)
#         self.assertFalse(res.result, '工作地点必填项验证失败')
        #工作内容
        addPara['workDiary.workPlace']='工作地点'
        addPara['workDiary.workContent']=''
        res=mAddWorkDiary(para=addPara)
#         self.assertFalse(res.result, '工作内容必填项验证失败')
        #正常新增
        addPara['workDiary.workContent']='工作内容'
        
        res=mAddWorkDiary(para=addPara)
        self.assertTrue(res, '新增工作日志失败')
        checkPara={
                   'workUserName':addPara['workDiary.workUserName'],
                   'workPlace':addPara['workDiary.workPlace'],
                   'workTime':addPara['workDiary.workTime'],
                   'workContent':addPara['workDiary.workContent']
                   }
        listPara=copy.deepcopy(searchWorkDiaryPara)
        r0=mCheckWorkDairyInList(checkPara=checkPara,listPara=listPara)
        self.assertTrue(r0, '新增工作日志成功！')
        #修改日志
        Log.LogOutput(message='修改工作日志，并采用查看接口验证修改功能')
        response=mWorkDairyList(para=listPara)
        responseDict=json.loads(response.text)
        updPara=copy.deepcopy(addWorkDiaryPara1)
        updPara['workDiary.id']=responseDict['rows'][0]['id']
        updPara['workDiary.workContent']='工作内容1'
        updPara['workDiary.workTime']='2016-01-01'
        updPara['workDiary.workPlace']='地点1'
        updPara['workDiary.workUserName']='工作人员1'
        updPara['mode']='edit'
        res=mUpdWorkDiary(para=updPara)
        self.assertTrue(res.result, '修改出错')
        #调用查看接口检查参数
        viewPara=copy.deepcopy(viewWorlDiartPara)
        viewPara['workDiary.id']=updPara['workDiary.id']
        checkPara1={
                   'workUserName':updPara['workDiary.workUserName'],
                   'workPlace':updPara['workDiary.workPlace'],
                   'workTime':updPara['workDiary.workTime'],
                   'workContent':updPara['workDiary.workContent']
                   }        
        r1=mCheckWorkDairyInViewpage(checkPara=checkPara1,viewPara=viewPara)
        self.assertTrue(r1,'修改后查看验证失败')
        #调用PC端接口验证数据正确性
        r2=check_workDiary(diaryDict=checkPara1,  username=userInit['DftJieDaoUser'],password='11111111')
        self.assertTrue(r2,'修改后PC端验证失败')
        pass

    '''
    @功能：工作日志-搜索
    @ chenhui 2016-3-7
    '''
    def testmRiChangBanGong_002(self):
        '''工作日志-搜索'''
        addPara1=copy.deepcopy(addWorkDiaryPara1)
        mAddWorkDiary(para=addPara1)
        addPara2=copy.deepcopy(addWorkDiaryPara1)
        addPara2['workDiary.workUserName']='张三'
        addPara2['workDiary.organization.id']=orgInit['DftSheQuOrgId']
        mAddWorkDiary(para=addPara2)
        listPara=copy.deepcopy(searchWorkDiaryPara)
        checkPara1={
                   'workUserName':addPara1['workDiary.workUserName'],
                   'workPlace':addPara1['workDiary.workPlace'],
                   'workTime':addPara1['workDiary.workTime'],
                   'workContent':addPara1['workDiary.workContent']
                   }  
        checkPara2={
                   'workUserName':addPara2['workDiary.workUserName'],
                   'workPlace':addPara2['workDiary.workPlace'],
                   'workTime':addPara2['workDiary.workTime'],
                   'workContent':addPara2['workDiary.workContent']                     
                     }
        r1=mCheckWorkDairyInList(checkPara=checkPara1,listPara=listPara)
        r2=mCheckWorkDairyInList(checkPara=checkPara2,listPara=listPara)
        self.assertTrue(r1, '仅显示本级查询失败')
        self.assertFalse(r2, '仅显示本级查询失败')
        listPara['searchChild']='true'
        r1=mCheckWorkDairyInList(checkPara=checkPara1,listPara=listPara)
        r2=mCheckWorkDairyInList(checkPara=checkPara2,listPara=listPara)
        self.assertTrue(r1, '全部查询失败')
        self.assertTrue(r2, '全部查询失败')
        listPara['searchWorkDiaryVo.workUser']=addPara1['workDiary.workUserName']
        r1=mCheckWorkDairyInList(checkPara=checkPara1,listPara=listPara)
        r2=mCheckWorkDairyInList(checkPara=checkPara2,listPara=listPara)
        self.assertTrue(r1, '全部、工作人员查询失败')
        self.assertFalse(r2, '全部、工作人员查询失败')
        Log.LogOutput( message='查询功能验证通过！')
        pass


    '''
    @功能：工作日志-刷新
    @ chenhui 2016-3-9
    '''
    def testmRiChangBanGong_003(self):
        '''工作日志-刷新'''
        addPara1=copy.deepcopy(addWorkDiaryPara1)
        mAddWorkDiary(para=addPara1)
        addPara2=copy.deepcopy(addWorkDiaryPara1)
        addPara2['workDiary.workUserName']='张三'
        mAddWorkDiary(para=addPara2)
        listPara=copy.deepcopy(searchWorkDiaryPara)
        #搜索‘张三’
        listPara['searchWorkDiaryVo.workUser']=addPara2['workDiary.workUserName']
        checkPara1={
                   'workUserName':addPara1['workDiary.workUserName'],
                   'workPlace':addPara1['workDiary.workPlace'],
                   'workTime':addPara1['workDiary.workTime'],
                   'workContent':addPara1['workDiary.workContent']
                   }  
        checkPara2={
                   'workUserName':addPara2['workDiary.workUserName'],
                   'workPlace':addPara2['workDiary.workPlace'],
                   'workTime':addPara2['workDiary.workTime'],
                   'workContent':addPara2['workDiary.workContent']                     
                     }
        r1=mCheckWorkDairyInList(checkPara=checkPara1,listPara=listPara)
        r2=mCheckWorkDairyInList(checkPara=checkPara2,listPara=listPara)
        self.assertFalse(r1, '工作人员查询失败')
        self.assertTrue(r2, '工作人员查询失败')
        #刷新
        Log.LogOutput( message='验证刷新功能')
        listPara2=copy.deepcopy(searchWorkDiaryPara)
        
        r1=mCheckWorkDairyInList(checkPara=checkPara1,listPara=listPara2)
        r2=mCheckWorkDairyInList(checkPara=checkPara2,listPara=listPara2)
        self.assertTrue(r1, '工作人员查询失败')
        self.assertTrue(r2, '工作人员查询失败')
        Log.LogOutput(message='刷新验证通过')
        
    '''
    @功能：日常办公-会议新增、修改
    @ chenhui 2016-3-7
    '''
    def testmRiChangBanGong_004(self):
        '''日常办公-会议新增、修改,必填项验证'''
        addPara=copy.deepcopy(addMeetPara1)
        Log.LogOutput( message='验证新增必填项')
        #部门名称
        addPara['newWorkingRecords.departmentType.id']=''
        r1=mAddMeet(para=addPara)
        self.assertFalse(r1.result,'部门必填项验证失败')
        #名称
        addPara['newWorkingRecords.departmentType.id']=getDbQueryResult(dbCommand = "select id from propertydicts where displayname='平安办'")
        addPara['newWorkingRecords.name']=''
        #手机端前台已限制
#         r2=mAddMeet(para=addPara)
#         self.assertFalse(r2.result,'名称必填项验证失败')
        #时间
        addPara['newWorkingRecords.name']='名称'
        addPara['newWorkingRecords.dealDate']=''
        r3=mAddMeet(para=addPara)
        self.assertFalse(r3.result,'时间必填项验证失败')
        #关键词
        addPara['newWorkingRecords.dealDate']=Time.getCurrentDateAndTime()
#         addPara['selectedTypes']=''
#         r4=mAddMeet(para=addPara)
#         self.assertFalse(r4.result,'关键词必填项验证失败')
        #主要内容
        addPara['selectedTypes']=getDbQueryResultList(dbCommand = "select id from propertydicts where displayname in('教育宣传','综治')")
        addPara['newWorkingRecords.content']=''
        r5=mAddMeet(para=addPara)
#         self.assertFalse(r5.result,'主要内容必填项验证失败')
        #正常新增
        Log.LogOutput(message='必填项验证通过，即将正常新增')
        #关键词多选
        keywordsList=getDbQueryResultList(dbCommand = "select id from propertydicts where displayname in('教育宣传','综治')")
        temp=''
        for listitem in keywordsList:
            for tupleitem in listitem:
                if temp=='':
                    temp=str(tupleitem)
                    continue
                temp=str(tupleitem)+','+temp
        addPara['newWorkingRecords.content']='主要内容'
        addPara['selectedTypes']=temp
        r6=mAddMeet(para=addPara)
        self.assertTrue(r6.result, '新增失败')
        #通过列表验证新增
        checkPara={
                   'name':addPara['newWorkingRecords.name'],
                   'content':addPara['newWorkingRecords.content']
                   }
        listPara=copy.deepcopy(searchMeetPara)
        r0=mCheckMeetInList(checkPara=checkPara,listPara=listPara)
        self.assertTrue(r0, '新增会议成功！')
        #修改会议
        Log.LogOutput(message='修改会议，并采用查看接口验证修改功能')
        response=mMeetList(para=listPara)
        responseDict=json.loads(response.text)
        updPara=copy.deepcopy(addMeetPara1)
        updPara['newWorkingRecords.id']=responseDict['rows'][0]['id']
        updPara['newWorkingRecords.content']='主要内容1'
        updPara['newWorkingRecords.dealDate']='2016-01-01'
        updPara['newWorkingRecords.name']='名称1'
        updPara['attachFiles']=None#修改时不带此参数
        rs=mUpdMeet(para=updPara)
        self.assertTrue(rs.result, '修改失败')
        checkPara1={
                   'name':updPara['newWorkingRecords.name'],
                   'content':updPara['newWorkingRecords.content']
                   }        
        #调用PC端接口验证数据正确性
        r22=check_WorkingRecord(WorkingDict=checkPara1, orgId=orgInit['DftJieDaoOrgId'],dailyDirectoryId=updPara['newWorkingRecords.dailyDirectory.id'],username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(r22,'修改后PC端验证失败')

    '''
    @功能：会议-搜索
    @ chenhui 2016-3-8
    '''
    def testmRiChangBanGong_005(self):
        '''会议-搜索'''
        addPara1=copy.deepcopy(addMeetPara1)
        mAddMeet(para=addPara1)
        addPara2=copy.deepcopy(addMeetPara1)
        addPara2['newWorkingRecords.name']='测试名称'
        mAddMeet(para=addPara2)
        #文件添加一数据作为干扰项
        addPara3=copy.deepcopy(addMeetPara1)
        addPara3['newWorkingRecords.name']='文件名称'
#         addPara3['newWorkingRecords.RECORDTYPE.id']=getDbQueryResult(dbCommand = "select id from propertydicts where  displayname='文件类' and propertydomainid=(select id from propertydomains where domainname='新工作台帐目录类型')")
        addPara3['newWorkingRecords.dailyDirectory.id']=getDbQueryResult(dbCommand ="select id from dailyDirectorys d where d.dailyyearid=\
                (select id from dailyYears d where d.yeardate='2016' and d.makedorgid='%s'and d.dailytype='0') and d.shortname='文件'"%orgInit['DftQuOrgId'])
        mAddMeet(para=addPara3)
        listPara=copy.deepcopy(searchMeetPara)
        listPara['newWorkingRecordVo.name']=addPara2['newWorkingRecords.name']
        checkPara1={
                   'name':addPara1['newWorkingRecords.name'],
                   'content':addPara1['newWorkingRecords.content']
                   }
        checkPara2={
                   'name':addPara2['newWorkingRecords.name'],
                   'content':addPara2['newWorkingRecords.content']
                   }
        r1=mCheckMeetInList(checkPara=checkPara1,listPara=listPara)
        r2=mCheckMeetInList(checkPara=checkPara2,listPara=listPara)
        self.assertFalse(r1, '查询失败')
        self.assertTrue(r2, '查询失败')
        Log.LogOutput( message='查询功能验证通过！')
        pass

    '''
    @功能：日常办公-活动新增、修改
    @ chenhui 2016-3-9
    '''
    def testmRiChangBanGong_006(self):
        '''日常办公-活动新增、修改,必填项验证'''
        addPara=copy.deepcopy(addFilePara1)
        Log.LogOutput( message='验证新增必填项')
        #部门名称
        addPara['newWorkingRecords.departmentType.id']=''
        r1=mAddMeet(para=addPara)
        self.assertFalse(r1.result,'部门必填项验证失败')
        #名称
        #手机端前台已验证
        addPara['newWorkingRecords.departmentType.id']=getDbQueryResult(dbCommand = "select id from propertydicts where displayname='平安办'")
        addPara['newWorkingRecords.name']=''
#         r2=mAddMeet(para=addPara)
#         self.assertFalse(r2.result,'名称必填项验证失败')
        #时间
        addPara['newWorkingRecords.name']='名称'
        addPara['newWorkingRecords.dealDate']=''
        r3=mAddMeet(para=addPara)
        self.assertFalse(r3.result,'时间必填项验证失败')
        #关键词
        addPara['newWorkingRecords.dealDate']=Time.getCurrentDateAndTime()
        addPara['selectedTypes']=''
#         r4=mAddMeet(para=addPara)
#         self.assertFalse(r4.result,'关键词必填项验证失败')
        #主要内容
        addPara['selectedTypes']=getDbQueryResultList(dbCommand = "select id from propertydicts where displayname in('教育宣传','综治')")
        addPara['newWorkingRecords.content']=''
#         r5=mAddMeet(para=addPara)
#         self.assertFalse(r5.result,'主要内容必填项验证失败')
        #正常新增
        Log.LogOutput(message='必填项验证通过，即将正常新增')
        addPara['newWorkingRecords.content']='主要内容'
        r6=mAddMeet(para=addPara)
        self.assertTrue(r6.result, '新增失败')
        #通过列表验证新增
        checkPara={
                   'name':addPara['newWorkingRecords.name'],
                   'content':addPara['newWorkingRecords.content']
                   }
        listPara=copy.deepcopy(searchFilePara)
        r0=mCheckMeetInList(checkPara=checkPara,listPara=listPara)
        self.assertTrue(r0, '新增文件成功！')
        #修改文件
        Log.LogOutput(message='修改文件，并采用查看接口验证修改功能')
        response=mMeetList(para=listPara)
        responseDict=json.loads(response.text)
        updPara=copy.deepcopy(addFilePara1)
        updPara['newWorkingRecords.id']=responseDict['rows'][0]['id']
        updPara['newWorkingRecords.content']='主要内容1'
        updPara['newWorkingRecords.dealDate']='2016-01-01'
        updPara['newWorkingRecords.name']='名称1'
        updPara['attachFiles']=None#修改时不带此参数
        rs=mUpdMeet(para=updPara)
        self.assertTrue(rs.result, '修改失败')
        checkPara1={
                   'name':updPara['newWorkingRecords.name'],
                   'content':updPara['newWorkingRecords.content']
                   }        
        #调用PC端接口验证数据正确性
        r22=check_WorkingRecord(WorkingDict=checkPara1, orgId=orgInit['DftJieDaoOrgId'],dailyDirectoryId=updPara['newWorkingRecords.dailyDirectory.id'],username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(r22,'修改后PC端验证失败')

    '''
    @功能：日常办公-活动新增、修改
    @ chenhui 2016-3-9
    '''
    def testmRiChangBanGong_007(self):
        '''日常办公-活动新增、修改,必填项验证'''
        addPara=copy.deepcopy(addActivityPara1)
        Log.LogOutput( message='验证新增必填项')
        #部门名称
        addPara['newWorkingRecords.departmentType.id']=''
        r1=mAddMeet(para=addPara)
        self.assertFalse(r1.result,'部门必填项验证失败')
        #名称
        #手机端前台已验证
        addPara['newWorkingRecords.departmentType.id']=getDbQueryResult(dbCommand = "select id from propertydicts where displayname='平安办'")
        addPara['newWorkingRecords.name']=''
#         r2=mAddMeet(para=addPara)
#         self.assertFalse(r2.result,'名称必填项验证失败')
        #时间
        addPara['newWorkingRecords.name']='名称'
        addPara['newWorkingRecords.dealDate']=''
        r3=mAddMeet(para=addPara)
        self.assertFalse(r3.result,'时间必填项验证失败')
        #关键词
        addPara['newWorkingRecords.dealDate']=Time.getCurrentDateAndTime()
        addPara['selectedTypes']=''
#         r4=mAddMeet(para=addPara)
#         self.assertFalse(r4.result,'关键词必填项验证失败')
        #主要内容
        addPara['selectedTypes']=getDbQueryResultList(dbCommand = "select id from propertydicts where displayname in('教育宣传','综治')")
        addPara['newWorkingRecords.content']=''
#         r5=mAddMeet(para=addPara)
#         self.assertFalse(r5.result,'主要内容必填项验证失败')
        #正常新增
        Log.LogOutput(message='必填项验证通过，即将正常新增')
        addPara['newWorkingRecords.content']='主要内容'
        r6=mAddMeet(para=addPara)
        self.assertTrue(r6.result, '新增失败')
        #通过列表验证新增
        checkPara={
                   'name':addPara['newWorkingRecords.name'],
                   'content':addPara['newWorkingRecords.content']
                   }
        listPara=copy.deepcopy(searchActivityPara)
        r0=mCheckMeetInList(checkPara=checkPara,listPara=listPara)
        self.assertTrue(r0, '新增活动成功！')
        #修改活动
        Log.LogOutput(message='修改活动，并采用查看接口验证修改功能')
        response=mMeetList(para=listPara)
        responseDict=json.loads(response.text)
        updPara=copy.deepcopy(addActivityPara1)
        updPara['newWorkingRecords.id']=responseDict['rows'][0]['id']
        updPara['newWorkingRecords.content']='主要内容1'
        updPara['newWorkingRecords.dealDate']='2016-01-01'
        updPara['newWorkingRecords.name']='名称1'
        updPara['attachFiles']=None#修改时不带此参数
        rs=mUpdMeet(para=updPara)
        self.assertTrue(rs.result, '修改失败')
        checkPara1={
                   'name':updPara['newWorkingRecords.name'],
                   'content':updPara['newWorkingRecords.content']
                   }        
        #调用PC端接口验证数据正确性
        r22=check_WorkingRecord(WorkingDict=checkPara1, orgId=orgInit['DftJieDaoOrgId'],dailyDirectoryId=updPara['newWorkingRecords.dailyDirectory.id'],username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(r22,'修改后PC端验证失败')

    '''
    @功能：日常办公-其他新增、修改
    @ chenhui 2016-3-9
    '''
    def testmRiChangBanGong_008(self):
        '''日常办公-其他新增、修改,必填项验证'''
        addPara=copy.deepcopy(addOtherPara1)
        Log.LogOutput( message='验证新增必填项')
        #部门其他
        addPara['newWorkingRecords.departmentType.id']=''
        r1=mAddMeet(para=addPara)
        self.assertFalse(r1.result,'部门必填项验证失败')
        #其他
        addPara['newWorkingRecords.departmentType.id']=getDbQueryResult(dbCommand = "select id from propertydicts where displayname='平安办'")
        addPara['newWorkingRecords.name']=''
#         r2=mAddMeet(para=addPara)
#         self.assertFalse(r2.result,'其他必填项验证失败')
        #时间
        addPara['newWorkingRecords.name']='其他'
        addPara['newWorkingRecords.dealDate']=''
        r3=mAddMeet(para=addPara)
        self.assertFalse(r3.result,'时间必填项验证失败')
        #关键词
        addPara['newWorkingRecords.dealDate']=Time.getCurrentDateAndTime()
        addPara['selectedTypes']=''
#         r4=mAddMeet(para=addPara)
#         self.assertFalse(r4.result,'关键词必填项验证失败')
        #主要内容
        addPara['selectedTypes']=getDbQueryResultList(dbCommand = "select id from propertydicts where displayname in('教育宣传','综治')")
        addPara['newWorkingRecords.content']=''
#         r5=mAddMeet(para=addPara)
#         self.assertFalse(r5.result,'主要内容必填项验证失败')
        #正常新增
        Log.LogOutput(message='必填项验证通过，即将正常新增')
        addPara['newWorkingRecords.content']='主要内容'
        r6=mAddMeet(para=addPara)
        self.assertTrue(r6.result, '新增失败')
        #通过列表验证新增
        checkPara={
                   'name':addPara['newWorkingRecords.name'],
                   'content':addPara['newWorkingRecords.content']
                   }
        listPara=copy.deepcopy(searchOtherPara)
        r0=mCheckMeetInList(checkPara=checkPara,listPara=listPara)
        self.assertTrue(r0, '新增活动成功！')
        #修改活动
        Log.LogOutput(message='修改活动，并采用查看接口验证修改功能')
        response=mMeetList(para=listPara)
        responseDict=json.loads(response.text)
        updPara=copy.deepcopy(addOtherPara1)
        updPara['newWorkingRecords.id']=responseDict['rows'][0]['id']
        updPara['newWorkingRecords.content']='主要内容1'
        updPara['newWorkingRecords.dealDate']='2016-01-01'
        updPara['newWorkingRecords.name']='其他1'
        updPara['attachFiles']=None#修改时不带此参数
        rs=mUpdMeet(para=updPara)
        self.assertTrue(rs.result, '修改失败')
        checkPara1={
                   'name':updPara['newWorkingRecords.name'],
                   'content':updPara['newWorkingRecords.content']
                   }        
        #调用PC端接口验证数据正确性
        r22=check_WorkingRecord(WorkingDict=checkPara1, orgId=orgInit['DftJieDaoOrgId'],dailyDirectoryId=updPara['newWorkingRecords.dailyDirectory.id'],username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(r22,'修改后PC端验证失败')   
        
        pass
    
    def tearDown(self):
        pass


if  __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    suite = unittest.TestSuite()
    suite.addTest(MbRiChangBanGong("testmRiChangBanGong_001"))
    results = unittest.TextTestRunner().run(suite)
    pass
