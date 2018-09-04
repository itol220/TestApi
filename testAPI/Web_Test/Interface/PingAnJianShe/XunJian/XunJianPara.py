# -*- coding:UTF-8 -*-
'''
Created on 2016-3-21

@author: chenyan
'''
# from __future__ import unicode_literals


#隐患项字典
riskRemarkObject = {
                    'riskRemark.riskRemarkName':'',               
                    'riskRemark.level.id':'',
                    'riskRemark.isEnable':'', 
                    'mode':'',
                    'riskRemark.id':'',
                    'riskRemark.riskmarkerType':'',
                    'riskRemark.orgId.id':'',
                    'isSubmit':'',
                    }

deleteRiskRemarkData = {
                      'riskRemarkIds':''
                      }


getRiskRemarkData = {
                      'riskRemark.orgId.id':'',
                      'riskRemark.riskmarkerType':'',
                      'searchChildOrg':'false',   
                      '_search':'false',
                      'rows':'200',
                      'page':'1',
                      'sidx':'indexId',
                      'sord':'asc'
                      }

searchRiskRemarkData = {
                      'riskRemark.orgId.id':'',
                      'riskRemark.riskmarkerType':'',
                      'riskRemark.riskRemarkName':'',   
                      '_search':'false',
                      'rows':'200',
                      'page':'1',
                      'sidx':'indexId',
                      'sord':'asc'
                      }

checkRiskRemarkDict = {
                       'riskRemarkName':'',
                       'id':None,
                       'indexId':None,
                       }

moveRiskRemarkDict = {
                       'riskRemark.riskmarkerType':'',
                       'mode':'',
                       'riskRemark.id':'',
                       'riskRemark.indexId':'',
                       'count':''
                       }


#企业字典项
enterpriseObject = {
                    "mode":"",               
                    "ownerOrg.id":"",
                    "orgName":"",  
                    "safeProductionEnterprise.landlordName":"",
                    "safeProductionEnterprise.landlordMobile":"",
                    "safeProductionEnterprise.id":"",
                    "safeProductionEnterprise.name":"",
                    "safeProductionEnterprise.address":"",
                    "safeProductionEnterprise.legalPerson":"",
                    "safeProductionEnterprise.type.id":"",
                    "safeProductionEnterprise.safeProductiontype.id":"",
                    "safeProductionEnterprise.mobileNumber":"",
                    "safeProductionEnterprise.businessLicense":"",
                    "safeProductionEnterprise.employeeAmount":"",
                    "safeProductionEnterprise.isEmphasis":"",
                    "safeProductionEnterprise.gridPerson":""
                    }


inspectionObject = {
                    "mode":"",               
                    "inspection.orgId":"",
                    "safeProductionEnterprise.id:":"",  
                    "safeProductionEnterprise.name":"",
                    "inspectionRecord.enterprise.id":"",
                    "inspection.inspectTime":"",
                    "inspection.inspectAddress":"",
                    "riskRemarkName":"",
                    "inspection.inspectResult":"",
                    "inspection.limitTime":"",
                    "inspection.inspectUserId":"",
                    "inspection.inspectName":"",
                    "riskRemarkIds":"",
                    "inspection.remark":""
                    }

getEnterpriseData = {
                      'orgId':'',
                      '_search':'false',
                      'rows':'200',
                      'page':'1',
                      'sidx':'id',
                      'sord':'desc'
                      }

checkEnterpriseDict = {
                      'name':None,
                      'inspectionCount':None,    
                      'gridPerson':None,
                      'state':None               
                       }


getInspectionData = {
                      "inspectionRecordVo.orgId":"",
                      "inspectionRecordVo.recordType":"",
                      "mode":"",
                      "_search":"false",
                      "rows":"200",
                      "page":"1",
                      "sidx":"id",
                      "sord":"desc",
                      "inspectionRecordVo.inspectOrder":"",
                      "inspectionRecordVo.name":"",
                      "inspectionRecordVo.state":"",
                      "inspectionRecordVo.inspectName":"",
                      "inspectionRecordVo.inspectTime":"",
                      "inspectionRecordVo.endTnspectTime":"",
                      "inspectionRecordVo.inspectAddress":"",
                      "inspectionRecordVo.sourceType":""
                      }

checkInspectionDict = {
                      'name':None,
                      'inspectionCount':None                   
                       }

data = {
        'dataType':'',
        'enterpriseType':'',
        'isNew':'1',
        'reportTime':'',
        'startRow':'3',
        'templates':'',
        'yearDate':''
        }

dlData = {
          'orgId':"",
          '_search':'false',
          'rows':'200',
          'page':'1',
          'sidx':'id',
          'sord':'desc',
          'pageOnly':''
          }

dispatchDict = {
                'selectIds':'',
                'userId':''
                }

searchEnterpriseData = {
                      'orgId':'',
                      'enterpriseSearchCondition.isEmphasis':'0',  #0?
                      'enterpriseSearchCondition.fastSearchKeyWords':'',
                      '_search':'false',
                      'rows':'200',
                      'page':'1',
                      'sidx':'id',
                      'sord':'desc'
                      }

advancedSearchEnterpriseData = {
                              'orgId':'',
                              'enterpriseSearchCondition.name':'',  
                              'enterpriseSearchCondition.address':'',
                              'enterpriseSearchCondition.legalPerson':'',
                              'enterpriseSearchCondition.typeId':'',
                              'enterpriseSearchCondition.safeProductiontypeId':'',
                              'enterpriseSearchCondition.businessLicense':'',
                              'enterpriseSearchCondition.mobileNumber':'',
                              'enterpriseSearchCondition.isEmphasis':'',  #是否注销 ：false-否  true-是
                              'enterpriseSearchCondition.gridPerson':'',
                              '_search':'false',
                              'rows':'200',
                              'page':'1',
                              'sidx':'id',
                              'sord':'desc'
                              }

dlXunJianData = {
          'inspectionRecordVo.orgId':"",
          "inspectionRecordVo.sourceType":"",
          "inspectionRecordVo.recordType":"",
          'mode':'',
          '_search':'false',
          'rows':'200',
          'page':'1',
          'sidx':'id',
          'sord':'desc',
          'pageOnly':''
          }


reviewInspectionObject = {
                        "mode":"",               
                        "inspection.orgId":"",
                        "inspection.id":"",  
                        "inspection.inspectAddress":"",
                        "inspectionRecord.enterprise.id":"",
                        "inspection.inspectTime":"",
                        "isSolve222":"",
                        "inspection.inspectResult":"",
                        "inspection.inspectUserId":"",
                        "inspection.inspectName":"",
                        "noSolveIds":"",
                        "solveIds":"",
                        "noSolveIds":"",
                        "inspection.remark":""
                        }


turnIssueObject = {
                    "stepId":"",
                    "issue.occurOrg.id":"",
                    "issue.serialNumber":"",  
                    "inspectionIds":"",
                    "dataSource":"",
                    "issue.subject":"",
                    "selectOrgName":"",
                    "issue.occurLocation":"",
                    "issue.occurDate":"",
                    "eatHours":"",
                    "eatMinute":"",
                    "selectedTypes":"",
                    "issueRelatedPeopleNames":"",
                    "issueRelatedPeopleTelephones":"",
                    "issue.relatePeopleCount":"",
                    "issue.issueKind.id":"",
                    "issue.issueContent":""
                    }

issueListPara = {
                   'organization.id':'',
                   'searchYear':"",
                   '_search':'false',
                   'page':'1',
                   'rows':'1000',
                   'sidx':'lastdealdate',
                   'sord':'desc'                 
                } 

deleteDict = {
               "enterpriseId":"",   
               "id":"",
               "inspectionId":"",
               "isSecretSupervision":"",            
               }




#督查暗访新增记录字典
getSafeProductionEnterpriseByNameObject = {
                                           "safeProductionEnterprise.name":"",
                                           "orgId":""
                                           }
                                     
supervisionObject = {
                        "secretSupervision.checkSubject":"",               
                        "secretSupervision.checkTime":"",
                        "secretSupervision.checkCompanyName":"",  
                        "secretSupervision.checkAddress":"",
                        "secretSupervision.checkLegalPerson":"",
                        "secretSupervision.mobileNumber":"",
                        "secretSupervision.findProblems":"",
                        "secretSupervision.requires":"",
                        "mode":"",
                        "secretSupervision.id":"",
                        "isSubmit":"",
                        "secretSupervision.orgId":"",
                        }


checkSupervisionDict = {
                      'checkAddress':None,
                     # 'checkUserId':None,    
                       }

getSupervisionData = {
                      "secretSupervisionVo.orgId":"",
                      "_search":"false",
                      "rows":"200",
                      "page":"1",
                      "sidx":"id",
                      "sord":"desc",
                      "secretSupervisionVo.checkCompanyName":None,
                      "secretSupervisionVo.checkAddress":None,
                      "secretSupervisionVo.checkSubject":None,
                      "secretSupervisionVo.checkTimeBegin":None,
                      "secretSupervisionVo.checkTimeEnd":None,
                     # "secretSupervisionVo.state":None
                      }

acceptCenterObject = {
                    "mode":"",               
                    "orgId":"",
                    }

deleteParam = {
               "selectIds":"",               
               }


#受理中心搜索字典项
serachInspectionData = {
                      "inspectionRecordVo.orgId":"",
                      "mode":"",
                      "inspectionRecordVo.inspectOrder":None,
                      "inspectionRecordVo.name":None,
                      "inspectionRecordVo.inspectAddress":None,
                      "inspectionRecordVo.inspectName":None,
                      "inspectionRecordVo.state":None,
                      "inspectionRecordVo.sourceType":None,
                      "_search":"false",
                      "rows":"200",
                      "page":"1",
                      "sidx":"id",
                      "sord":"desc",
                      }



#出租房
rentalObject = {
                    "mode":"",               
                    "ownerOrg.id":"",
                    "rental.id":"",  
                    "orgName":"",
                    "rental.address":"",
                    "rental.name":"",
                    "rental.owner":"",
                    "rental.ownerPhone":"",
                    "rental.rentalType.id":"",
                    "rental.rentalFloor":"",
                    "rental.rentalArea":"",
                    "rental.rentalStructure.id":"",
                    "rental.rentedNumber":"",
                    "rental.police":"",
                    "rental.isStop":"",
                    "rental.dangerSituation":"",
                    "rental.gridPerson":"",
                    }

deleteRentalDict = {
                    'selectIds':'',
                    }

checkRentalDict = {
                    'name':None,
                    'gridPerson':None,
                    }

fastSearchRentalData = {
                      'orgId':'',
                      'rentalVo.fastSearchKeyWords':'',  
                      '_search':'false',
                      'rows':'200',
                      'page':'1',
                      'sidx':'id',
                      'sord':'desc'
                      }

searchRentalData = {
                      'orgId':'',
                      'rentalVo.address':'',
                      'rentalVo.name':'',  
                      'rentalVo.owner':'', 
                      'rentalVo.rentalType.id':'', 
                      'rentalVo.rentalStructure.id':'', 
                      'rentalVo.ownerPhone':'', 
                      'rentalVo.gridPerson':'', 
                      'rentalVo.police':'', 
                      'rentalVo.isStop':'',     #是否出租
                      '_search':'false',
                      'rows':'200',
                      'page':'1',
                      'sidx':'id',
                      'sord':'desc'
                      }

inspectionRentalObject = {
                        "mode":"",               
                        "inspection.orgId":"",
                        "rental.id:":"",  
                        "rental.name":"",
                        "inspectionRecord.enterprise.id":"",
                        "inspection.inspectTime":"",
                        "inspection.inspectAddress":"",
                        "inspection.inspectResult":"",
                        "inspection.limitTime":"",
                        "inspection.inspectUserId":"",
                        "inspection.inspectName":"",
                        "riskRemarkIds":"",
                        "inspection.remark":""
                        }

getRentalData = {
                      "inspectionRecordVo.orgId":"",
                      "inspectionRecordVo.sourceType":"",
                      "inspectionRecordVo.recordType":"",
                      "mode":"",
                      "_search":"false",
                      "rows":"200",
                      "page":"1",
                      "sidx":"id",
                      "sord":"desc",
                      "inspectionRecordVo.address":"",
                      "inspectionRecordVo.name":"",
                      "inspectionRecordVo.state":"",
                      "inspectionRecordVo.inspectName":"",
                      "inspectionRecordVo.inspectTime":"",
                      "inspectionRecordVo.endTnspectTime":"",
                      }

checkRentalDict = {
                      'name':None,
                       }

reviewRentalObject = {
                        "inspectionRecord.recordType":"",
                        "mode":"",               
                        "inspection.orgId":"",
                        "inspection.id":"",  
                        "inspection.inspectAddress":"",
                        "inspectionRecord.enterprise.id":"",
                        "inspection.inspectTime":"",
                        "isSolve162":"",
                        "isSolve185":"",
                        "inspection.inspectResult":"",
                        "inspection.inspectUserId":"",
                        "inspection.inspectName":"",
                        "noSolveIds":"",
                        "solveIds":"",
                        "noSolveIds":"",
                        "inspection.remark":""
                        }

#出租房统计检查参数
rentalHouseCheck = {
#                   #出租房检查情况  
#                  'rentalTotalStr':'' ,#出租房总数
#                  'noInspectionRentalNumStr':'',#未检查数
#                  'inspectionRentalNumStr' :'',#检查数
#                  'inspectionPercentage':'',#检查率
                 #巡检检查情况
                 'inspectionTotal':'',#总数
                 'inspectionQualifiedNum':'',#合格数
               #  'inspectionQualifiedPercentage':'',#合格率
                 'inspectionNoQualifiedNum':'',#不合格
                 'inspectionBadlyNum':''#严重数
                 }
#出租房统计查询条件
rentalTongJiTiaoJian = {
                    'staticsVo.orgId':'',
                    'staticsVo.startDate':'',
                    'staticsVo.endDate':'',
                    'staticsVo.typeIdd': ''   
                        }
#出租房统计导出条件
rentalExport = {
                'staticsVo.endDate':'',
                'staticsVo.orgId':'', 
                'staticsVo.safeProductiontypeId':'' ,   
                'staticsVo.startDate':''
                }
#出租房统计检查参数
retalExportCheck = {
                   'inspectionTotal' :None #巡检总数
                    }
#出租房人员统计导出条件
rentalPerson = {
                'staticsVo.endDate':'',
                'staticsVo.gridPersonName':'',    
                'staticsVo.orgId':'',
                'staticsVo.startDate':'' 
                }
#督查暗访统计检查
inspectionCheck = {
                        'checkTotal':''  
                          }
#督查暗访统计
inspectionParam = {
             'searchStaticsVo.orgId':'',
            'searchStaticsVo.startDate':'',
            'searchStaticsVo.endDate':'',
            '_search':'false',
            'rows':'20',
            'page':'1',
            'sidx':'id',
            'sord':'desc'      
                   }



