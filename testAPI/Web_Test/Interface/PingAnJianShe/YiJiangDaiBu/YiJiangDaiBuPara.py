# -*- coding:UTF-8 -*-
'''
Created on 2015-11-18

@author: N-266
'''
from __future__ import unicode_literals
from Interface.PingAnJianShe.Common.CommonIntf import getDbQueryResult,\
    getIdByDomainAndDisplayName
from COMMON import Time
from CONFIG.InitDefaultPara import orgInit
from COMMON import Time, CommonUtil
ApplyReward={
       'rewardToSubsidies[0].userId':'',
       'rewardToSubsidies[0].orgId':'',
       'rewardToSubsidies[0].serviceNumber':'',
       'issueIdsStr':'',
       'content':'',
       'searchIssueVo.currentOrgId':'',
       'searchIssueVo.inputFrom':'',
       'searchIssueVo.inputEnd':'',
       '_search':'false',
#        'nd':'',
       'rows':'200',
       'page':'1',
       'sidx':'issueNumber',
       'sord':'desc',
       'userId':'',
       'applyIssueIds':'',
       'noapplyIssueIds':'6,9',
       }
findApplyReward={
                  'rewardToSubsidieId':'',
                  '_search':'false',
                  'rows':'200',
                  'page':'1',
                  'sidx':'id',
                  'sord':'desc'
                  }

CheckApplyReward={
                  'subject':None

                  }
AgreeIssue={
#             'id':'',
            'agreedIssueIds':'',
            'rewardToSubsidiesStep.content':'',
            'rewardToSubsidiesStep.currentOrgId':'',
            'rewardToSubsidiesStep.money':'',
            'rewardToSubsidiesStep.operateUserId':'',
            'rewardToSubsidiesStep.orgCode':'',
            'rewardToSubsidiesStep.orgId':'',
            'rewardToSubsidiesStep.previouStep':'',
            'rewardToSubsidiesStep.rewardToSubsidieId':'',
            'reviewRecord':'',
            
            
            }
CheckAgreeIssue={
                 'id':'',
                 'rewardToSubsidieId':'',
                'status':'',
                 
                 }
FindAgreeIssue={
                'searchVo.orgId':'',
                '_search':'false',
                'rows':'20',
                'page':'1',
                'sidx':'id',
                'sord':'desc'
                }
#上报
ReportIssue={
             'rewardToSubsidiesStep.content':'',
             'stepIds':'',
             }
#否决
Dissagree={
           'rewardToSubsidiesStep.content':'',
           'stepIds':'',
           }
#事件清单编辑
UpdateReward={
              'rewardtoSubsidieIssues.rewardToSubsidieId':'',
              'rewardtoSubsidieIssues.issueId':''
              }

#检查事件清单编辑>删除
findIssue={
             'rewardToSubsidieId':'',
             '_search':'false',
             'rows':'200',
             'page':'1',
             'sidx':'id',
             'sord':'desc'
             }
checkReward={
             'subject':'',
             'issueId':'',
             }
#重置
resetReward={
             'stepIds':'',
             }
#检查重置
checkReset={
            'money':''  ,
            'status':'',
            'id':'',
            }
#检查重置
findReset={
           'searchVo.orgId':'',
           '_search':'false',
           'rows':'200',
           'page':'1',
           'sidx':'id',
           'sord':'desc',
         }
#删除
deleteReward={
              'applyIds':'',
              }

checkDelete={
            'id':'',
            }
findDelete={
           'searchVo.orgId':'',
           '_search':'false',
           'rows':'200',
           'page':'1',
           'sidx':'id',
           'sord':'desc',
            }
searchReward={
              'status':'',
              }
findSearchReward={
                  'searchVo.orgId':None,
                  '_search':'false',
                  'rows':'20',
                  'page':'1',
                  'sidx':'id',
                  'sord':'desc',
                  'searchVo.status':'',
                  }
countReward={
             'finishAuditNumber':'',
             'hasreportedNumber':'',
             'waitAuditNumber':'',
             'rewardMoney':''
             }
findCountReward={
                 'orgId':'',
                 'beginDate':'',
                 'endDate':'',
                 'applyOrApprover':'',
                 '_search':'false',
                 'rows':'1000',
                 'page':'1',
                 'sidx':'id',
                 'sord':'desc',
                 
}
#以奖代补>数据录入情况，高级搜索
AdvancedSearch={
#                 'searchIssueVo.occurOrg.id':'',
#                 'searchIssueVo.status':'',
                'searchIssueVo.name':'',
#                 'searchIssueVo.userName':'',
#                 'searchIssueVo.inputFrom':'',
#                 'searchIssueVo.inputEnd':'',
#                 'searchIssueVo.relatePeopleMinCount':'',
#                 'searchIssueVo.relatePeopleMaxCount':'',
#                 'searchIssueVo.subject':'',
#                 'searchIssueVo.mainCharacters':'',
#                 'searchIssueVo.serialNumber':'',
#                 'selectOrgName':'',
#                 'searchIssueVo.issueTypeDomain.id':'',
#                 'searchIssueVo.important':'',
#                 'searchIssueVo.isEmergency':'',
                'searchIssueVo.currentOrgId':'',
                '_search':'false',
                'rows':'20',
                'page':'1',
                'sidx':'issueNumber',
                'sord':'desc',
                }
findAdvancedSearch={
                    
                    'searchIssueVo.name':'',
                    
                    
                    }

issueObject ={
              'eatHours':'',
              'eatMinute':'',
              'involvedPlace':'',
              'issue.centerLat':'',
              'issue.centerLat2':'',
              'issue.centerLon':'',
              'issue.centerLon2':'',
              'issue.hours':'00',
              'issue.id':'',
              'issue.issueKind.id':'',
              'issue.minute':'00',
              'issue.selfdomIssuetypeOrgCode':'',
              'issue.serialNumber':'',
              'issue.sourceKind.id':getDbQueryResult(dbCommand='''select id from propertydicts pr where pr.displayname = '人工录入' and pr.propertydomainid=(
       select id from propertydomains where domainName like '来源方式')'''),
              'selectOrgName':'',
              'selectRelatedPeople':'',
              'selfdomOrgCode':'',
              'sourceType':'',
              'stepId':'',
              'struts.token':'',
              'issue.isDefault':'true',
              'issue.occurOrg.id':'',
              'issue.subject':'',
              'issue.occurLocation':'',
              'issue.occurDate':'',
              'issueRelatedPeopleNames':'',
              'issueRelatedPeopleTelephones':'',
              'issue.relatePeopleCount':'',
              'selectedTypes':'',
              'issue.issueContent':''
              } 


issueObject2 ={
              'eatHours':'',
              'eatMinute':'',
              'involvedPlace':'',
              'issue.centerLat':'',
              'issue.centerLat2':'',
              'issue.centerLon':'',
              'issue.centerLon2':'',
              'issue.hours':'00',
              'issue.id':'',
              'issue.issueKind.id':'',
              'issue.minute':'00',
              'issue.selfdomIssuetypeOrgCode':'',
              'issue.serialNumber':'',
              'issue.sourceKind.id':getIdByDomainAndDisplayName('来源方式','人工录入'),
              'selectOrgName':orgInit['DftJieDaoOrg'],
              'selectRelatedPeople':'',
              'selfdomOrgCode':'',
              'sourceType':'',
              'stepId':'',
              'struts.token':'',
              'issue.isDefault':'true',
              'issue.occurOrg.id':orgInit['DftJieDaoOrgId'],
              'issue.subject':'事件主题',
              'issue.occurLocation':'发生地点',
              'issue.occurDate':Time.getCurrentDate(),
              'issueRelatedPeopleNames':'张三',
              'issueRelatedPeopleTelephones':'13001010102',
              'issue.relatePeopleCount':'3',
              'selectedTypes':'16',
              'issue.issueContent':'事件内容'
              } 
IssueCheckPara = {
                   'attachFilesCount':None,
                   'createDate':None,
                   'issueId':None,
                   'lastdealdate':None,
                   'occurDate':None,
                   'occurDateString':None,
                   'occurOrg':None,
                   'serialNumber':None,
                   'sourceKind':None,
                   'status':None,
                   'subject':None,
                   'targetOrg':None,
                   'userName':None               
                      } 
issueListPara = {
                   'organization.id':'',
                   'issueType':'',
                   'page':'1',
                   'rows':'1000',
                   'sidx':'lastdealdate',
                   'sord':'desc'                 
                      } 