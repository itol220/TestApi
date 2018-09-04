# -*- coding:UTF-8 -*-
'''
Created on 2015-11-5

@author: N-254
'''
from __future__ import unicode_literals
from COMMON import Time
from COMMON.CommonUtil import createRandomString
from CONFIG.InitDefaultPara import orgInit
from Interface.PingAnJianShe.Common.CommonIntf import getDbQueryResult
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
              'issue.sourceKind.id':getDbQueryResult(dbCommand='''select id from propertydicts pr where pr.displayname = '人工录入' and pr.propertydomainid=(
       select id from propertydomains where domainName like '来源方式'
)'''),
              'selectOrgName':orgInit['DftJieDaoOrg'],
              'selectRelatedPeople':'',
              'selfdomOrgCode':'',
              'sourceType':'',
              'stepId':'',
              'struts.token':'',
              'issue.isDefault':'true',
              'issue.occurOrg.id':orgInit['DftJieDaoOrgId'],
              'issue.subject':'事件主题'+createRandomString(),
              'issue.occurLocation':'发生地点',
              'issue.occurDate':Time.getCurrentDate(),
              'issueRelatedPeopleNames':'张三',
              'issueRelatedPeopleTelephones':'13001010102',
              'issue.relatePeopleCount':'3',
              'selectedTypes':getDbQueryResult(dbCommand="select id from issuetypes i where i.domainid=(select id from issuetypedomains where module='core' and domainName='矛盾纠纷') and i.issuetypename='医患纠纷'"),
              'issue.issueContent':'事件内容'
              } 
issueListPara = {
                   'organization.id':'',
                   'issueType':'',
                   'page':'1',
                   'rows':'1000',
                   'sidx':'lastdealdate',
                   'sord':'desc'                 
                      } 
issueSearchObj={
                'page':'1',
                'rows':'100',
                'searchIssueVo.sortField':'issueId',
                'searchIssueVo.order':'desc',
                'searchIssueVo.status':'',
                'searchIssueVo.occurOrg.id':'',
                'searchIssueVo.targeOrgId':'',
                'selOrgIds1':'',
                'searchIssueVo.subject':'',
                'selectOrgName':'',
                'searchIssueVo.issueKind.id':'',
                'searchIssueVo.isEmergency':'',
                'searchIssueVo.serialNumber':'',
                'searchIssueVo.sourceKindId':'',
                'searchIssueVo.occurFrom':'',
                'searchIssueVo.occurEnd':'',
                'searchIssueVo.occurLocation':'',
                'searchIssueVo.inputFrom':'',
                'searchIssueVo.inputEnd':'',
                'searchIssueVo.userName':'',
                'searchIssueVo.relatePeopleMinCount':'',
                'searchIssueVo.relatePeopleMaxCount':'',
                'searchIssueVo.mainCharacters':'',
                'searchIssueVo.useSelfdomIssuetype':'false'
                }
xiaXiaDaiBanLieBiao={
                     'keyId':'',
                     'seachValue':'all',
                     '_search':'false',
                     'nd':'',
                     'rows':'200',
                     'page':'1',
                     'sidx':'iu.createDate',
                     'sord':'desc'
                     }
xiaXiaYiBanJieLieBiao={
                    'keyId':'',
                    '_search':'false',
                    'nd':',',
                    'rows':'200',
                    'page':'1',
                    'sidx':'createDate',
                    'sord':'desc'
                    }
woDeDaiBanLieBiao={
                    'keyId':'',
                    'issueType:':'',
                    'rows':'200',
                    'page':'1',
                    'sidx':'issueId',
                    'sord':'desc'
                   }
#督办
superviseIssue={
                    'operation.dealOrg.id':'',
                    'operation.issue.id':'',
                    'keyId':'',
                    'dealCode':'',
                    'operation.dealUserName':'',
                    'operation.mobile':'',
                    'operation.content':'',
}
superviseIssueListPara={
                    'issueVO.createOrg.id' :'',
                    'supervisePageType':'',
                    '_search':'false',
                    'nd':'',
                    'rows':'200',
                    'page':'1',
                    'sidx':'issueId',
                    'sord':'desc',
                    }
dealIssuePara={
                'operation.dealOrg.id':'',
                'operation.issue.id':'',
                'operation.targeOrg.id':'',
                'keyId':'',
                'toLocalPeopleCenter':'',
                'tag':'',
                'operation.dealUserName':'',
                'operation.mobile':'',
                'dealCode':'',
                
                'dealTime':'',
                'transferToType':'true',
                'themainOrgid':'',
                'operation.dealDeadline':'',
                'themainOrgid':'',
                'secondaryOrgid':'',
                'operation.dealDeadline':'',
                'tellOrgIds':'',
                'operation.content':'',
                'specialAssignType':'',
                'dealTime':Time.getCurrentDate(),
                'transferToType':'true',
               }
#评价post参数
issueEvaluateParam={
                     'issueEvaluate.id':'',
                     'issueEvaluate.issue.id':'',
                     'issueEvaluate.evaluateTime':'',
                     'score':'',
                     'issueEvaluate.evaluateType':'',
                     'issueEvaluate.evaluateContent':''
                     }

#我的事项-报表统计列表参数
bbtjPara={
                'orgId':'',
                'page':'1',
                'rows':'50',
                'sidx':'issueId',
                'sord':'desc',
                'requestType':'',
                'searchTestIndividuallyVo.issueTypeId':None,
                'searchTestIndividuallyVo.issueTypeDomainName':None,
                'searchSecuritytroubleVo.issueTypeDomainName':None,
                'searchPeopleLiveServiceVo.issueTypeDomainName':None,
                'searchOtherTypeVo.issueTypeDomainName':None,
                }
#下辖全部事项查询参数
dowonAllIssueSearchPara={
                'page':'1',
                'rows':'20',
                'searchIssueVo.sortField':'createdate',
                'searchIssueVo.order':'desc', 
                'searchIssueVo.status':'',
                'searchIssueVo.occurOrg.id':'',
                'searchIssueVo.targeOrgId':'',
                'selOrgIds1':'',
                'searchIssueVo.subject':'',
                'selectOrgName':'请点击此处选择',
                'searchIssueVo.issueKind.id':'',
                'searchIssueVo.isEmergency':'',
                'searchIssueVo.sourceKindId':'',
                'searchIssueVo.occurFrom':'',
                'searchIssueVo.occurEnd':'',
                'searchIssueVo.occurLocation':'',
                'searchIssueVo.inputFrom':'',
                'searchIssueVo.inputEnd':'',
                'searchIssueVo.userName':'',
                'searchIssueVo.relatePeopleMinCount':'',
                'searchIssueVo.relatePeopleMaxCount':'',
                'searchIssueVo.mainCharacters':'',
                'searchIssueVo.evaluateStar':'',
                'searchIssueVo.assignTimeFrom':'',
                'searchIssueVo.assignTimeEnd':'',
                'searchIssueVo.dealOrgId':'',
                'searchIssueVo.useSelfdomIssuetype':'false',
                '_search':'false',
                'sidx':'createDate',
                'sord':'desc',
                'searchIssueVo.serialNumber':'',
                         }

#工作简报新增参数
workBulletinPara={
            'mode':'add',
            'workBulletin.id':'',
            'workBulletin.organization.id':'',
            'workBulletin.workBulletinSourceType.id':'',
            'ids':'',
            'workBulletin.bulletinName':'',#名称
            'workBulletin.bulletinDate':'',#2015-12-17
            'workBulletin.userName':'',#临平东湖街道
            'workBulletin.fillDate':'',#2015-12-17
            'workBulletin.summary':'',#概要
#            'attachFiles':'',#,截图05.png
       }

#下辖督办列表参数
superviseIssuesList={
            'issueVO.createOrg.id':'',
            'supervisePageType':'notDoneSupervise',#notDoneSupervise doneSupervise allSupervise
            '_search':'false',
            'rows':'200',
            'page':'1',
            'sidx':'issueId',
            'sord':'desc',        
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
issureSearchPara={
                    'searchIssueVo.status':'',
                    'searchIssueVo.occurOrg.id':'',
                    'searchIssueVo.targeOrgId':'',
                    'selOrgIds1':'',
                    'searchIssueVo.subject':'',
                    'selectOrgName':'请点击此处选择',
                    'searchIssueVo.issueKind.id':'',
                    'searchIssueVo.isEmergency':'',
                    'searchIssueVo.serialNumber':'',
                    'searchIssueVo.sourceKindId':'',
                    'searchIssueVo.occurFrom':'',
                    'searchIssueVo.occurEnd':'',
                    'searchIssueVo.occurLocation':'',
                    'searchIssueVo.inputFrom':'',
                    'searchIssueVo.inputEnd':'',
                    'searchIssueVo.userName':'',
                    'searchIssueVo.relatePeopleMinCount':'',
                    'searchIssueVo.relatePeopleMaxCount':'',
                    'searchIssueVo.mainCharacters':'',
                    'searchIssueVo.useSelfdomIssuetype':'false',                   
                  }
superviseIssueCheckPara={
                    'attachFilesCount': None,
                    'createDate': None,
                    'currentOrg': None,
                    'currentOrgDisplayName': None,
                    'dealState': None,
                    'dealTime': None,
                    'issueId':None,
                    'issueStepId':None,
                    'occurDate':None,
                    'occurDateString':None,
                    'occurOrg':None,
                    'serialNumber':None,
                    'sourceKind':None,
                    'subject': None,
                    'supervisionState':None,
                    'urgent': None,
                    'userName': None,
                         }

#下辖待办事项检查参数
xiaXiaDaiBanJianCha={
                    'attachFilesCount': 0,
                    'createDate': None,
                    'currentOrg': None,
                    'currentOrgDisplayName':None, 
                    'dealState':None,
                    'dealTime':None,
                    'domainName': None,
                    'issueId': None,
                    'issueLogId': None,
                    'issueStepId': None,
                    'lastOrg': None,
                    'occurDate': None,
                    'occurDateString': None,
                    'occurOrg': None,
                    'operateForSupervision': None,
                    'serialNumber':None,
                    'sourceKind': None,
                    'status': None,
                    'subject': None,
                    'superviseLevel': None,
                    'supervisionState': None,
                    'targeOrg': None,
                    'urgent': None,
                    'userName': None,
                    }
#事件限时办结参数
issueCompleteLimitConfigParam={
                        'mode':'',
                        'issueCompleteLimitConfig.id':'',
                        'organization.id':'',
                        'issueCompleteLimitConfig.organization.id':'',
                        'issueCompleteLimitConfig.isDirectlyJurisdiction':'true',
                        'issueCompleteLimitConfig.limitDay':'',
                        'issueCompleteLimitConfig.normalDay':'',
                        'issueCompleteLimitConfig.expireDay':'',
                        'issueCompleteLimitConfig.enable':'',
                               }

#我的事项-限时办结列表参数
issueCompleteLimitListCheckPara={
                                 'assignDays':None,
                                 'attachFilesCount':None,
                                 'createDate':None,
                                 'delayDays':None,
                                 'issueId':None,
                                 'lastdealdate':None,
                                 'limitDays':None,
                                 'normalDays':None,
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