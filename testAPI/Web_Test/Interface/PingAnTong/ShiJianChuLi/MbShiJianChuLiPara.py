# -*- coding:UTF-8 -*-
'''
Created on 2015-11-5

@author: N-254
'''
from __future__ import unicode_literals
from Web_Test.COMMON import Time
from Web_Test.COMMON.CommonUtil import createRandomString
from Web_Test.CONFIG.InitDefaultPara import orgInit
from Web_Test.Interface.PingAnJianShe.Common.CommonIntf import getDbQueryResult
#事件新增参数
issueAddPara={
            'issueNew.occurOrg.id':'',
            'issueNew.issueContent':'',
            'issueRelatedPeopleTelephones':'',
            'issueRelatedPeopleNames':'',
            'issueNew.selectedTypes':'',
            'issueNew.occurDate':'',
            'hours':'',
            'issueNew.selectedBigType':'',
            'selectedTypes':'',
            'issueRelatedPeopleFixPhones':'',
            'issueNew.mainCharacters':'',
            'issueNew.important':'',
            'issueNew.isEmergency':'',
            'issueNew.subject':'',
            'minute':'',
            'issueNew.selfdomIssuetypeOrgCode':'',
            'issueNew.issueKind.id':'',
            'issueNew.uniqueIdForMobile':'',
            'selectedBigType':'',
            'issueNew.relatePeopleCount':'',
            'issueNew.occurLocation':'',
            'datetime':'',
            'small_type':'',
            'tqmobile':'true',
              }
#事件新增默认参数
issueAddPara1={
            'issueNew.occurOrg.id':orgInit['DftJieDaoOrgId'],
            'issueNew.issueContent':'事件内容',
            'issueRelatedPeopleTelephones':'12345678901,13111111111',
            'issueRelatedPeopleNames':'张三,李四',
            'issueNew.selectedTypes':'',
            'issueNew.occurDate':Time.getCurrentDate(),
            'hours':'',
            'issueNew.selectedBigType':'',
            'selectedTypes':'13',
            'issueRelatedPeopleFixPhones':'',
            'issueNew.mainCharacters':'',
            'issueNew.important':'True',
            'issueNew.isEmergency':'True',
            'issueNew.subject':'主题'+createRandomString(),
            'minute':'',
            'issueNew.selfdomIssuetypeOrgCode':'',
            'issueNew.issueKind.id':getDbQueryResult(dbCommand = "select id from propertydicts where propertydomainid=(select id from propertydomains where domainname='事件性质') and displayname='个体性事件'"),
            'issueNew.uniqueIdForMobile':'',
            'selectedBigType':'',
            'issueNew.relatePeopleCount':3,
            'issueNew.occurLocation':'地点',
            'datetime':'',
            'small_type':'3',
            'tqmobile':'',
              }
#我的待办列表请求参数
myTodoIssueListPara={
                    'tqmobile':'',
                    'orgId':orgInit['DftJieDaoOrgId'],
                    'sord':'desc',
                    'page':'1',
                    'search':'false',
                    'searchIssueVo.lastDealStartDate':'',
                    'searchIssueVo.lastDealEndDate':'',
                    'normal':'true',
                    'searchIssueVo.serialNumber':'',
                    'searchIssueVo.subject':'',
                    'sidx':'issueId',
                    'selfParentId':'',
                    'searchIssueVo.reportedOrgId':'',
                    'rows':'200',
}
#查询事件参数
searchIssuePara={
                    'tqmobile':'',
                    'orgId':orgInit['DftJieDaoOrgId'],
                    'sord':'desc',
                    'page':'1',
                    'search':'false',
                    'searchIssueVo.lastDealStartDate':'',
                    'searchIssueVo.lastDealEndDate':'',
#                     'normal':'true',
                    'searchIssueVo.serialNumber':'',
                    'searchIssueVo.subject':'',
                    'sidx':'',
                    'selfParentId':'',
                    'searchIssueVo.reportedOrgId':'',
                    'rows':'200',                 
                 }
#办理参数
dealPara={
                    'content':'处理内容',
                    'issueLog.issueStep.fourTeams.id':'',
                    'operatorName':'',
                    'issueLog.issueStep.fourTeamsTypeID':'',
                    'operatorMobile':'',
                    'issueLog.fourTeamsName':'',
                    'issueLog.targeOrg.id':'',
                    'issueId':'',
                    'dealOrgId':'',
                    'dealType':'',
                    'stepId':'',
                    'tqmobile':'true'
          }