# -*- coding:UTF-8 -*-
'''
Created on 2015-11-18

@author: N-266
'''
# from __future__ import unicode_literals
from Web_Test.Interface.PingAnJianShe.Common.CommonIntf import getIdByDomainAndDisplayName
def enum(**enums):
    return type('Enum', (), enums)
#新增
riskObject={
            'riskProjectReportIds':'',
            'riskProjectReport.id':'',
            'mode':'',
            'riskProjectReport.createOrg.id':'',
            'riskProjectReport.importMatterName':'',
            'riskProjectReport.projectLeader':'',
            'riskProjectReport.phone':'',
            'riskProjectReport.projectClassification.id':'',
            'riskProjectReport.projectType.id':'',
            'riskProjectReport.memo':'',
            'riskProjectReport.remark':'',
            'riskProjectReport.beginYearFiling':'',
           }
#查看
checkObject={
              'importMatterName':None,
#               'projectLeader':None,
#               'projectClassification':None,
#               'projectType':None,
#               'beginYearFiling':None,
#               'memo':None
               
              }
#删除
deleteObject={
              'riskProjectReportIds':''
             }
CheckDeleteParam={
                  'importMatterName':None,
#                   'riskProjectReport.createOrgId':'',
#                   'riskProjectReport.processStatus':'-1',
#                   '_search':'false',
#                   'nd':None,
#                   'rows:':'20',
#                   'page:':'1',
#                   'sidx':'id',
#                   'sord':'desc'
                  }
GetDeleteParam={
                'riskProjectReport.createOrgId':'',
                'riskProjectReport.processStatus':'-1',
                '_search':'false',
                'nd':None,
                'rows:':'20',
                'page:':'1',
                'sidx':'id',
                'sord':'desc'
                }
#批量删除
deleteAllObject={
                 'riskProjectReportIds':''
                 }
#检查新增项目是否成功
getRiskOrgDict={
                'riskProjectReport.createOrgId':'',
                'riskProjectReport.processStatus':'-1',
                '_search':None,
                'nd':None,
                'rows':'2000',
                'page':'1',
                'sidx':'id',
                'sord':'desc'
                }
#删除
deleteAllRisk_1={
                 'riskProjectReport.createOrgId':'',
                 '_search':'false',
                 'rows':'200',
                 'page':'1',
                 'sidx':'id',
                 'sord':'desc'
                 }
#暂缓
zanhuanObject={
               'riskProjectReportIds':'',
               'riskProjectReport.status':''
               }
#调整
adjustObject={
              'struts.token':'',
              'adjustmentIds':'',
              'riskProjectReport.adjustmentDetail.adjustment':'',
              'riskProjectReport.adjustmentDetail.adjustmentDate':'',
              'riskProjectReport.adjustmentDetail.adjustmentReason':'',
              }
quXiaoAdjustObject={
                    'riskProjectReport.adjustmentDetail.adjustment':'',
                    'adjustmentIds':''
                    }
#验证调整是否成功
CheckAdjustParam={
                  'importMatterName':None,
                  }
GetAdjustParam={
                'riskProjectReport.createOrgId':'',
                'riskProjectReport.processStatus':'-1',
                '_search':'false',
                'nd':None,
                'rows':'20',
                'page':'1',
                'sidx':'id',
                'sord':'desc'
                }
#评估立项
initiationObject={
                  'struts.token':'',
                  'riskProjectReport.id':'',
                  'modeTemp':'',
                  'riskProjectReport.bodyOrg':'',
                  'riskProjectReport.bodyOrgPhone':'',
                  'riskProjectReport.startDate':'',
                  'riskProjectReport.endDate':'',
                  'riskProjectReport.assessmentWarn':'',
                  'riskProjectReport.evaluateType':'',
                  'riskProjectReport.reviewSuggestion':''
                  }

saveInitiationObject={
                     'riskProjectReport.id':''
                     }
#检查评估立项
checkInitiationObject={
                        'riskProjectReport.createOrgId':'',
#                 'riskProjectReport.processStatus':'-1',
                        '_search':'false',
                        'nd':None,
                        'rows':'20',
                        'page':'1',
                       'sidx':'id',
                        'sord':'desc'
                       }
checkMakeplanObject={
                     'riskProjectReport.createOrgId':'',
                        '_search':'false',
                        'nd':None,
                        'rows':'20',
                        'page':'1',
                       'sidx':'id',
                        'sord':'desc'
                     }
#制定评估方案
makeplanObject={
                 'struts.token':'',
                 'riskAssessPlan.id':'',
                 'riskAssessPlan.project.id':'',
                 'modeTemp':'',
                 'riskAssessPlan.relativeRegion':'',
                 'riskAssessPlan.relativePeople':'',
                 'riskAssessPlan.landUseSituation':'',
                 'riskAssessPlan.relativeFundSituation':'',
                 'riskAssessPlan.evaluateUnit':'',
                 'riskAssessPlan.evaluateMember':'',
                 'assessmentMode':'',
                 'riskAssessPlan.assessmentMode':'',
                 'riskAssessPlan.timeManage':'',
                 'riskAssessPlan.bodyOrg':'',
                 'riskAssessPlan.leader':'',
                 'riskAssessPlan.leaderPhone':'',
                 'riskAssessPlan.evaluateLeader':'',
                 'riskAssessPlan.phone':'',
                 'riskAssessPlan.commissionRisk':'',
                 'riskAssessPlan.implementBody':'',
                 'riskAssessPlan.implementResponsible':'',
                 'riskAssessPlan.implementPhone':'',
                 'riskAssessPlan.riskEstimate':'',
                 'riskAssessPlan.request':'',
                 'riskAssessPlan.orgids':'',
               
                 
                 }
#评估实施>论证专家
ExpertObject={
                 'struts.token':'',
                 'mode':'',
                 'saveOrSubmitType':'',
                 'operationType':'',
                 'riskAssessMeasure.id':'',
                 'riskAssessMeasure.projectReport.id':'',
                 'riskAssessMeasure.assessType':'',
                 'riskAssessMeasure.argumentationFormPeople':'',
                 'riskAssessMeasure.argumentationTitle':'',
                 'riskAssessMeasure.argumentationDate':'',
                 'riskAssessMeasure.argumentationAddress':'',
                 'riskAssessMeasure.assessMember':'',
                 'riskAssessMeasure.argumentationRecordPelple':'',
                 'riskAssessMeasure.argumentationRecordSituation':'',
                 'riskAssessMeasure.advice':'',
                 'riskAssessMeasure.argumentationOneCompletion':'',
                 'orgId':''
                 
                  
                  }
measureObject={
              'struts.token':'',
              'mode':'',
              'saveOrSubmitType':'',
              'operationType':'',
              'riskAssessMeasure.id':'',
              'riskAssessMeasure.projectReport.id':'',
              'riskAssessMeasure.assessType':'',
              'riskAssessMeasure.assessMember':'',
              'riskAssessMeasure.meetingDate':'',  
              'riskAssessMeasure.meetingAddress':'',
              'riskAssessMeasure.meetingRecordPeople':'',
              'riskAssessMeasure.advice':'',
              }
submitMeasureObject={
             'ids':''
              }
backObject={
             'ids':''
            }
AssessSuggest={
              'struts.token':'',
              'riskAssessSuggest.id':'',
              'riskAssessSuggest.project.id':'',
               'mode':'',
               'flag':'',
               'riskAssessSuggest.riskPoint':'',
               'riskAssessSuggest.precaution':'',
               'riskAssessSuggest.riskLevel.id':'',
               'riskAssessSuggest.suggest.id':'',
               'riskAssessSuggest.advice':'',
               }
#决策结果>决策意见
RiskDecisionAdvice={
                    'struts.token':'',
                    'riskDecisionAdvice.id':'',
                    'riskDecisionAdvice.project.id':'',
                    'mode':'',
                    'flag':'',
                    'riskDecisionAdvice.convener':'',
                    'participantNames':'',
                    'hearingPersonNameBaks1':'',
                    'participantWorkUnits':'',
                    'riskDecisionAdvice.occurTim':'',
                    'riskDecisionAdvice.address':'',
                    'riskDecisionAdvice.recorder':'',
                    'riskDecisionAdvice.advice':'',
                    'riskDecisionAdvice.projectLeader:':'',
                    'riskDecisionAdvice.leader':'',
                    'riskDecisionAdvice.measures':'',
                    'riskDecisionAdvice.suggest.id':'',
                    'riskDecisionAdvice.project.proplanExecutionStartdate':'',
                    'riskDecisionAdvice.project.proplanExecutionEnddate':'',
                    'riskDecisionAdvice.record':'',
                    

                    }
lookPlanParam={
               'importMatterName':None,
               
               }
checkLookPlanParam={
                    
                    'riskProjectReport.createOrgId':'',
                    'riskProjectReport.processStatus':'-1',
                    '_search':'',
                    'nd':'',
                    'rows':'200',
                    'page':'1',
                    'sidx':'id',
                    'sord':'desc'
                    }
checkInitiation={
                 'importMatterName':None,
                 }


measureParam={
              'importMatterName':None,
              }

checkMeasureRisk={
                    'riskProjectReport.createOrgId':'',
                    '_search':'false',
                    'rows':'2000',
                    'page':'1',
                    'sidx':'id',
                    'sord':'desc'
                  }
checkSuggestParam={
                   
                   'importMatterName':None
                   }
checkRiskDecisionAdvice={
                         'importMatterName':None
                         }
CheckAdvice={
                  'riskProjectReport.createOrgId':'',
                    '_search':'false',
                    'nd':None,
                    'rows':'20',
                    'page':'1',
                   'sidx':'id',
                    'sord':'desc'
           }
ArchiveParam={
              'riskDecisionTrackEvent.project.id':''
              }
CheckArchiveParam={
                    '_search':'false',
                    'nd':None,
                    'rows':'200',
                    'page':'1',
                   'sidx':'id',
                    'sord':'desc'
                   }
CheckBackParam={
                'importMatterName':None
                }
GetBackParam={
              'riskProjectReport.createOrgId':'',
                    '_search':'false',
                    'nd':None,
                    'rows':'20',
                    'page':'1',
                   'sidx':'id',
                    'sord':'desc'
              }
addExpert={
           'struts.token':'',
           'riskExpert.picture':'',
           'mode':'',
           'riskExpert.id':'',
           'riskExpert.name':'',
           'riskExpert.sex.id':'',
           'riskExpert.age':'',
           'riskExpert.phone':'',
           'riskExpert.province':'',
           'riskExpert.city':'',
           'riskExpert.district':'',
           'riskExpert.dept':'',
           'riskExpert.skillTitle.id':'',
           'riskExpert.post':'',
           'riskExpert.belongIndustry.id':'',
           'riskExpert.subject':'',
           'riskExpert.resume':'',
          
           }
updateExpert={
              
              
              }
checkAddParam={
               'name':None,
               'sex':None
               }
CheckAddExpert={
                   '_search':'false',
                    'nd':None,
                    'rows':'20',
                    'page':'1',
                   'sidx':'id',
                    'sord':'desc'
                }
WangPing={
          'struts.token':'',
          'mode':'',
          'riskAssessMeasure.id':'',
          'riskAssessMeasure.projectReport.id':'',
          'riskAssessMeasure.assessType':'',
          'riskAssessMeasure.assessMember':'',
          'riskAssessMeasure.advice':'',
          'riskAssessMeasure.onlineDate':'',
          
          }
importRisk={
            'dataType':'',
            'enterpriseType':'',
            'isNew':'1',
            'reportTime':'',
            'startRow':'3',
            'struts.token':'',
            'templates':'',
#             'upload':'',
            'yearDate':'',
            }
downLoadRisk={
              'riskProjectReport.createOrgId':'',
              '_search':'false',
#               'nd':None,
              'rows':'200',
              'page':'',
              'sidx':'id',
              'sord':'desc',
              'pageOnly':'false'
              }
# checkUpdateExpert={
# #                    '_search':'false',
# #                    'nd':None,
# #                    'rows':'200',
# #                    'page':'1',
# #                    'sidx':'id',
# #                    'sord':'desc',
#                     'mode':'',
#                     'expertId':'',
#                      
#                    
#                    
#                    }

#计划情况：0表中计划内，1表中计划外
PlanInfo = enum(INPLAN='0',OUTPLAN='1')
#暂缓：2表示暂缓，0表示取消暂缓
Status=enum(POSTPONE='2',NOPOSTPONE='0')
#调整：1表示调整，0表中取消调整
PlanAdjust=enum(ADJUST='1',NOADJUST='0')
#评估立项，评估类型:0表示一般评估
EvaluateType=enum(EVALUATE='0',NOEVALUATE='1')
#制定评估方案>评估方式：0：网上联评，1：专家论证，2：实地走访，3：会议座谈，4：问卷调查，5：听证。6：公示公告，7：其他
AssessmentMode=enum(WANGPING='0',ZHUANJIA='1',HUIYI='3',WENJUAN='4',TINGZHENG='7',GONGGAO='5',QITA='6')
#是否委托评估：0：不委托。1：委托
CommissionRisk=enum(COMMISSION='1',NOCOMMISSION='0')
#评估报告>评估建议>风险等级，高:1636,中：1637，低：1638
RiskLevel=enum(HIGH=getIdByDomainAndDisplayName(domainName='风险等级',displayName='高'),MIDDLE=getIdByDomainAndDisplayName(domainName='风险等级',displayName='中'),LOW=getIdByDomainAndDisplayName(domainName='风险等级',displayName='低'))
#评估报告>评估建议>建议，1639：准予实施:1640
RiskSuggest=enum(PERMIT=getIdByDomainAndDisplayName(domainName='建议',displayName='准予实施'),RESPITE=getIdByDomainAndDisplayName(domainName='建议',displayName='不予实施'),NOPERMIT=getIdByDomainAndDisplayName(domainName='建议',displayName='暂缓实施'))
#是否委托评估
Delegate=enum(YES='1',NO='0')
#决策结果>决策意见>结论，1639表示准予实施，1641表示不予实施，1640表示暂缓实施
Conclusion=enum(YES=getIdByDomainAndDisplayName(domainName='建议',displayName='准予实施'),NO=getIdByDomainAndDisplayName(domainName='建议',displayName='不予实施'),ZANHUAN=getIdByDomainAndDisplayName(domainName='建议',displayName='暂缓实施'))
#决策结果>决策意见>备案情况,0表示未备案，1表示已备案
Record=enum(YES='1',NO='0')
#专家库，专家性别，91表示男，92表示女
RiskExpertSex=enum(BOY=getIdByDomainAndDisplayName(domainName='性别(男、女)',displayName='男'),GIRL=getIdByDomainAndDisplayName(domainName='性别(男、女)',displayName='女'))
#技术职称:1693表示教授
RiskExpertSkillTitle=enum(PROFESSOR=getIdByDomainAndDisplayName(domainName='技术职称',displayName='教授'))
RiskExpertBelongIndustry=enum(NONG=getIdByDomainAndDisplayName(domainName='所属行业',displayName='农、 林、牧、渔业'))
#决策事项分类
Classification=enum(ONE=getIdByDomainAndDisplayName(domainName='项目分类',displayName='重大工程项目'))
#涉及领域
ProjectType=enum(YI=getIdByDomainAndDisplayName(domainName='项目类别',displayName='农村征地'))