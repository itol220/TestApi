# -*- coding:UTF-8 -*-
'''
Created on 2016-4-7

@author: lhz
'''
#督查暗访新增参数
from Web_Test.CONFIG import InitDefaultPara
from Web_Test.COMMON import Time
import time
duChaAnFangAddParam = {
           'secretSupervision.checkCompanyName':'',
           'secretSupervision.mobileNumber':'',
           'secretSupervision.checkLegalPerson':'',
           'secretSupervision.checkSubject':'',
           'secretSupervision.checkAddress':'',
           'secretSupervision.orgId':'',
            'secretSupervision.findProblems':'',
            'secretSupervision.checkTime':'',
            'secretSupervision.requires':'',
            'tqmobile':'true',
            'android_appversion':'2.0.1'            
                       }
#督查暗访列表参数
duChaAnFangListParam = {
                       'tqmobile':'true',
                        'secretSupervisionVo.orgId':'',
                        'sord':'desc',
                        'sidx':'id',
                        'page':'1',
                        'rows':'20'
                        }
#检查新增督查暗访参数
checkDuChaAnFangParam = {
                         'checkCompanyName':''
                         }


#督查暗访删除参数
deleteDuChaAnFangParam = {
               'tqmobile':'true',
               'selectIds':''           
                          }

#督查暗访高级搜索参数
searchDuChaAnFangParam = {
                    'tqmobile':'true',
                    'secretSupervisionVo.checkAddress':'',
                    'sord':'desc',
                    'page':'1',
                    'secretSupervisionVo.checkCompanyName':'',
                    'secretSupervisionVo.orgId':'',
                    'sidx':'id',
                    'secretSupervisionVo.state':'',
                    'rows':'20'         
                          }
#督查暗访高级搜索检查字段
check_searchDuChaAnFangParam = {
                               'checkAddress':'',
                               'checkCompanyName':'',
                               'state':'' 
                                }

#PC端 督查暗访 ---受理中心转事件
TransferEventsParam = {
            'stepId':'',
            'issue.occurOrg.id':InitDefaultPara.orgInit['DftJieDaoOrgId'],
            'issue.createOrg.id':InitDefaultPara.orgInit['DftJieDaoOrgId'],
            'issue.serialNumber':'',
            'inspectionIds':'',
            'dataSource':'secretSupervisionIssue',
            'issue.subject':'',
            'selectOrgName':InitDefaultPara.orgInit['DftJieDaoOrg'],
            'issue.occurLocation':InitDefaultPara.orgInit['DftJieDaoOrg'],
            'issue.occurDate':Time.getCurrentDate(),
            'eatHours' :time.strftime("%H"),
            'eatMinute':time.strftime("%M"),
            'selectOrgNameByOwner':InitDefaultPara.orgInit['DftJieDaoOrg'],
            'issue.ownerPerson':InitDefaultPara.userInit['DftJieDaoUserXM'],
            'selectedTypes':'',
            'issueRelatedPeopleNames':'',
            'issueRelatedPeopleTelephones':'',
            'issue.relatePeopleCount':'',
            'issue.issueKind.id':'',
            'issue.issueContent':''
                       }
#PC端 事件处理--结案
issueDealParam = {
                'operation.dealOrg.id':InitDefaultPara.orgInit['DftJieDaoOrgId'],
                'operation.issue.id':'',
                'operation.targeOrg.id':'',
                'keyId':'',
                'toLocalPeopleCenter':'',
                'tag':'',
                'operation.dealUserName':InitDefaultPara.userInit['DftJieDaoUserXM'],
                'operation.mobile':'',
                'dealCode':'',
                'dealTime':Time.getCurrentDate(),
                'transferToType':'true',
                'themainOrgid':'',
                'operation.dealDeadline':'',
                'themainOrgid':'',
                'secondaryOrgid':'',
                'tellOrgIds':'',
                'operation.dealDeadline':'',
                'tellOrgIds':'',
                'operation.content':'',
                'specialAssignType':''
                  }

#督查暗访删除
deleteParam = {
             'tqmobile':'true',
             'selectIds':''  
               }

