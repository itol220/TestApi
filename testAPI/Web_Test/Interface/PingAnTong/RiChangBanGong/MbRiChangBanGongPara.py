# -*- coding:UTF-8 -*-
'''
Created on 2016-3-7

@author: N-286
'''
from __future__ import unicode_literals
from Web_Test.COMMON import Time
from Web_Test.CONFIG.InitDefaultPara import orgInit
from Web_Test.Interface.PingAnJianShe.Common.CommonIntf import getDbQueryResult, \
    getDbQueryResultList
#工作日志新增参数
addWorkDiaryPara={
                'tqmobile':'true',
                'workDiary.id':'',
                'workDiary.workContent':'',
                'workDiary.workTime':'',
                'workDiary.workPlace':'',
                'workDiary.organization.id':'',
                'workDiary.diaryType.id':getDbQueryResult(dbCommand = "select id from propertydicts where  displayname='其他' and propertydomainid=(select id from propertydomains where domainname='工作日志类型')"),
                'workDiary.workUserName':'',
                'mode':'add'
                  }
#新增工作日志默认参数
addWorkDiaryPara1={
                'tqmobile':'true',
                'workDiary.id':'',
                'workDiary.workContent':'工作内容',
                'workDiary.workTime':Time.getCurrentDate(),
                'workDiary.workPlace':'地点',
                'workDiary.organization.id':orgInit['DftJieDaoOrgId'],
                'workDiary.diaryType.id':getDbQueryResult(dbCommand = "select id from propertydicts where  displayname='其他' and propertydomainid=(select id from propertydomains where domainname='工作日志类型')"),
                'workDiary.workUserName':'工作人员',
                'mode':'add'
                  }
#工作日志列表、查询参数
searchWorkDiaryPara={
                     'tqmobile':'true',
                     'sord':'desc',
                     'sidx':'id',
                     'searchChild':'false',
                     'page':'1',
                     'searchWorkDiaryVo.organization.id':orgInit['DftJieDaoOrgId'],
                     'rows':200
                     }
#工作日志查看参数
viewWorlDiartPara={
                   'tqmobile':'true',
                   'workDiary.id':'',
                   'mode':'view'
                   }

#会议新增参数
addMeetPara={
                'tqmobile':'true',
                'attachFiles':None,
                'yearDate':'2016',
                'newWorkingRecords.participant':'',
                'newWorkingRecords.departmentType.id':'',
                'selectedTypes':'',
                'newWorkingRecords.proceedSite':'',
                'newWorkingRecords.name':'',
                'newWorkingRecords.fileNo':'',
                'newWorkingRecords.dealDate':'' 
             }
#会议新增默认参数
#会议、文件、活动中的关键词参数，可多选
keywordsList=getDbQueryResultList(dbCommand = "select id from propertydicts where displayname in('教育宣传','综治')")
selectedTypes=''
for listitem in keywordsList:
    for tupleitem in listitem:
        selectedTypes=str(tupleitem)+','+selectedTypes
addMeetPara1={
                'tqmobile':'true',
                'attachFiles':None,
                'yearDate':'2016',
                'newWorkingRecords.participant':'',
                'newWorkingRecords.departmentType.id':getDbQueryResult(dbCommand = "select id from propertydicts where displayname='平安办'"),
                'selectedTypes':selectedTypes,#getDbQueryResultList(dbCommand = "select id from propertydicts where displayname in('教育宣传','综治')"),
                'newWorkingRecords.proceedSite':'',
                'newWorkingRecords.name':'名称',
                'newWorkingRecords.fileNo':'',
                'newWorkingRecords.dealDate':Time.getCurrentDateAndTime(),
                'newWorkingRecords.RECORDTYPE.id':getDbQueryResult(dbCommand = "select id from propertydicts where  displayname='会议类' and propertydomainid=(select id from propertydomains where domainname='新工作台帐目录类型')"),
                'newWorkingRecords.content':'主要内容',
                'newWorkingRecords.dailyDirectory.id':getDbQueryResult(dbCommand ="select id from dailyDirectorys d where d.dailyyearid=\
                (select id from dailyYears d where d.yeardate='2016' and d.makedorgid='%s'and d.dailytype='0') and d.shortname='会议'"%orgInit['DftQuOrgId']),
             }
#会议搜索、列表参数
searchMeetPara={
                'tqmobile':'true',
                'newWorkingRecordVo.organization.id':orgInit['DftJieDaoOrgId'],
                'sord':'desc',
                'yearDate':'2016',
                'newWorkingRecordVo.displayLevel':'true',
                'page':'1',
                'sidx':'id',
                'newWorkingRecordVo.hasAttach':'-1',
                'rows':'200',
                'newWorkingRecordVo.dailyDirectoryId':getDbQueryResult(dbCommand ="select id from dailyDirectorys d where d.dailyyearid=\
                (select id from dailyYears d where d.yeardate='2016' and d.makedorgid='%s'and d.dailytype='0') and d.shortname='会议'"%orgInit['DftQuOrgId']),
                }
#文件新增默认参数
addFilePara1={
                'tqmobile':'true',
                'attachFiles':None,
                'yearDate':'2016',
                'newWorkingRecords.participant':'',
                'newWorkingRecords.departmentType.id':getDbQueryResult(dbCommand = "select id from propertydicts where displayname='平安办'"),
                'selectedTypes':selectedTypes,#getDbQueryResultList(dbCommand = "select id from propertydicts where displayname in('教育宣传','综治')"),
                'newWorkingRecords.proceedSite':'',
                'newWorkingRecords.name':'名称',
                'newWorkingRecords.fileNo':'',
                'newWorkingRecords.dealDate':Time.getCurrentDateAndTime(),
                'newWorkingRecords.RECORDTYPE.id':getDbQueryResult(dbCommand = "select id from propertydicts where  displayname='文件类' and propertydomainid=(select id from propertydomains where domainname='新工作台帐目录类型')"),
                'newWorkingRecords.content':'主要内容',
                'newWorkingRecords.dailyDirectory.id':getDbQueryResult(dbCommand ="select id from dailyDirectorys d where d.dailyyearid=\
                (select id from dailyYears d where d.yeardate='2016' and d.makedorgid='%s'and d.dailytype='0') and d.shortname='文件'"%orgInit['DftQuOrgId']),
             }
#文件搜索、列表参数
searchFilePara={
                'tqmobile':'true',
                'newWorkingRecordVo.organization.id':orgInit['DftJieDaoOrgId'],
                'sord':'desc',
                'yearDate':'2016',
                'newWorkingRecordVo.displayLevel':'true',
                'page':'1',
                'sidx':'id',
                'newWorkingRecordVo.hasAttach':'-1',
                'rows':'200',
                'newWorkingRecordVo.dailyDirectoryId':getDbQueryResult(dbCommand ="select id from dailyDirectorys d where d.dailyyearid=\
                (select id from dailyYears d where d.yeardate='2016' and d.makedorgid='%s'and d.dailytype='0') and d.shortname='文件'"%orgInit['DftQuOrgId']),
                }
#活动新增默认参数
addActivityPara1={
                'tqmobile':'true',
                'attachFiles':None,
                'yearDate':'2016',
                'newWorkingRecords.participant':'',
                'newWorkingRecords.departmentType.id':getDbQueryResult(dbCommand = "select id from propertydicts where displayname='平安办'"),
                'selectedTypes':selectedTypes,#getDbQueryResultList(dbCommand = "select id from propertydicts where displayname in('教育宣传','综治')"),
                'newWorkingRecords.proceedSite':'',
                'newWorkingRecords.name':'名称',
                'newWorkingRecords.fileNo':'',
                'newWorkingRecords.dealDate':Time.getCurrentDateAndTime(),
                'newWorkingRecords.RECORDTYPE.id':getDbQueryResult(dbCommand = "select id from propertydicts where  displayname='活动类' and propertydomainid=(select id from propertydomains where domainname='新工作台帐目录类型')"),
                'newWorkingRecords.content':'主要内容',
                'newWorkingRecords.dailyDirectory.id':getDbQueryResult(dbCommand ="select id from dailyDirectorys d where d.dailyyearid=\
                (select id from dailyYears d where d.yeardate='2016' and d.makedorgid='%s'and d.dailytype='0') and d.shortname='活动'"%orgInit['DftQuOrgId']),
             }
#活动搜索、列表参数
searchActivityPara={
                'tqmobile':'true',
                'newWorkingRecordVo.organization.id':orgInit['DftJieDaoOrgId'],
                'sord':'desc',
                'yearDate':'2016',
                'newWorkingRecordVo.displayLevel':'true',
                'page':'1',
                'sidx':'id',
                'newWorkingRecordVo.hasAttach':'-1',
                'rows':'200',
                'newWorkingRecordVo.dailyDirectoryId':getDbQueryResult(dbCommand ="select id from dailyDirectorys d where d.dailyyearid=\
                (select id from dailyYears d where d.yeardate='2016' and d.makedorgid='%s'and d.dailytype='0') and d.shortname='活动'"%orgInit['DftQuOrgId']),
                }

#其他新增默认参数

addOtherPara1={
                'tqmobile':'true',
                'attachFiles':None,
                'yearDate':'2016',
                'newWorkingRecords.participant':'',
                'newWorkingRecords.departmentType.id':getDbQueryResult(dbCommand = "select id from propertydicts where displayname='平安办'"),
                'selectedTypes':selectedTypes,#getDbQueryResult(dbCommand = "select id from propertydicts where displayname ='教育宣传'"),
                'newWorkingRecords.proceedSite':'',
                'newWorkingRecords.name':'名称',
                'newWorkingRecords.fileNo':'',
                'newWorkingRecords.dealDate':Time.getCurrentDateAndTime(),
                'newWorkingRecords.RECORDTYPE.id':getDbQueryResult(dbCommand = "select id from propertydicts where  displayname='其他类' and propertydomainid=(select id from propertydomains where domainname='新工作台帐目录类型')"),
                'newWorkingRecords.content':'主要内容',
                'newWorkingRecords.dailyDirectory.id':getDbQueryResult(dbCommand ="select id from dailyDirectorys d where d.dailyyearid=\
                (select id from dailyYears d where d.yeardate='2016' and d.makedorgid='%s'and d.dailytype='0') and d.shortname='其他'"%orgInit['DftQuOrgId']),
             }
#其他搜索、列表参数
searchOtherPara={
                'tqmobile':'true',
                'newWorkingRecordVo.organization.id':orgInit['DftJieDaoOrgId'],
                'sord':'desc',
                'yearDate':'2016',
                'newWorkingRecordVo.displayLevel':'true',
                'page':'1',
                'sidx':'id',
                'newWorkingRecordVo.hasAttach':'-1',
                'rows':'200',
                'newWorkingRecordVo.dailyDirectoryId':getDbQueryResult(dbCommand ="select id from dailyDirectorys d where d.dailyyearid=\
                (select id from dailyYears d where d.yeardate='2016' and d.makedorgid='%s'and d.dailytype='0') and d.shortname='其他'"%orgInit['DftQuOrgId']),
                }