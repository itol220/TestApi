# -*- coding:UTF-8 -*-
'''
Created on 2016-6-7

@author: chenyan
'''

#单位类型
saveSuperviseTypeDict={
                    'orgPathName':'',
                    'orgId':'',
                    'superviseType':'',
                    }

#火灾隐患类型确认
PreviewList={
             'previewData':'',
             '_search':'false',
             'rows':'1000',
             'page':'1',
             'sidx':'id',
             'sord':'desc', 
             }

PreviewListCheck={
                 'displayName':None,
                 'level':None,
                 }

#火灾隐患类型
saveSuperviseType={
                    'superviseTypeItemVo.superviseItemMap':'',
                    'superviseTypeItemVo.index':'',
                    'superviseType':'',
                    'orgId':'',
                    }



#新增/修改单位
fireCompanyDict={
                    'mode':'',
                    'fireCompanyInfo.createDept':'',
                    'fireCompanyInfo.belongDept':'',
                    'fireCompanyInfo.importOrAdd':'',
                    'fireCompanyInfo.orgid':'',
                    'fireCompanyInfo.orgPathName':'',
                    'fireCompanyInfo.companyNo':'',
                    'fireCompanyInfo.companyName':'',
                    'companySuperviseTypeIsChange':'',
                    'fireCompanyInfo.superviseTypeName':'',
                    'fireCompanyInfo.address':'',
                    'fireCompanyInfo.superviseType.id':'',
                    'fireCompanyInfo.manger':'',
                    'fireCompanyInfo.managerTelephone':'',
                    'fireCompanyInfo.rentHousePerson':'',
                    'fireCompanyInfo.industrialCatalogue':'',
                    'businessLicense':'',
                    'firelicense':'',
                    'fireCompanyInfo.fireCompanyInfoId':'',
                    'fireCompanyInfo.updateDept':'',
                    'fireCompanyInfo.totalEmployee':'',
                    'fireCompanyInfo.residentEmployee':'',
                    'fireCompanyInfo.tempEmployee':'',
                    'fireCompanyInfo.tainedEmployee':'',
                    }

#删除单位
deleteFireCompanyDict={
                        'fireCompanyInfo.fireCompanyInfoId':'',
                        'fireCompanyInfo.updateDept':'',
                        }

#搜索/检查单位
checkFireCompanyDict={
                        'companyName':None,
#                         'fireCompanyInfoId':None,
                        }

getFireCompanyDict={
                         'orgId':'',
                         'fireCompanyInfo.companyName':'',
                         'fireCompanyInfo.createDept':'',
                         'fireCompanyInfo.address':'',
                         'fireCompanyInfo.isOffHire':'',
                         'fireCompanyInfo.sinceCompanyNo':'',
                         'fireCompanyInfo.levelShow':'',
                         '_search':'false',
                         'rows':'1000',
                         'page':'1',
                         'sidx':'id',
                         'sord':'desc', 
                        }

#单位添加日常检查
saveFiretrapSuperviseDict={
                        'isReportFlag':'',
                        'calCheckResult':'',
                        'firetrapSupervise.superviseNo':'',
                        'companyName':'',
                        'checkDate':'',
                        'firetrapSupervise.checkAddress':'',
                        'firetrapSupervise.checkPlace':'',
                        'checkItemIndexs':'',
                        'checkItemCodes':'',   #隐患项选择id
#                         '一般':'',
                        'superviseLevleId_510':'',
                        'superviseLevleId_512':'',
                        'superviseLevleId_511':'',
#                         'superviseResultAttachment':'',
#                         'firetrapSupervise.reviseDate':'',
                        'firetrapSupervise.manageName':'',
                        'companyCheckRecord_assignUserNameVo':'',
                        'companyCheckRecord_assignUserVo':'',
                        'companyCheckRecord_levelOrg':'',
                        'companyCheckRecordlevel':'',
                        'companyCheckRecordOrgId':'',
                        'user.userName':'',
                        'user.name':'',
                        'user.organization.id':'',
                        'calculationMode':'',
                        'firetrapSupervise.signDate':'',
                        'firetrapSupervise.superviseUserName':'',
                        'firetrapSupervise.superviseUser':'',
                        'firetrapSupervise.superviseDate':'',
                        'operateMode':'',
                        'firetrapSupervise.superviseState':'',
#                         'firetrapSupervise.superviseType':'',
                        'firetrapSupervise.updateDept':'',
                        'firetrapSupervise.createDept':'',
                        'firetrapSupervise.companyCheckRecordId':'',
#                         'firetrapSupervise.firetrapSuperviseId':'',
#                         'attachfileNamelist':'',
#                         'selectCheckItemCode':'',
                        'superviseTypeId':'',
#                         'operateMode':'',
                        'companyCheckRecord.companyManager':'',
                        'companyCheckRecord.assignUser':'',
                        'companyCheckRecord.assignDept':'',
                        'companyCheckRecord.checkType':'',
                        'companyCheckRecord.companyCheckRecordId':'',
                        'companyCheckRecord.checkUser':'',
                        'companyCheckRecord.fireCompanyInfoId':'',
                        'companyCheckRecord.checkDate':'',
                        'checkResult':'',
                        }

#检查日常检查项
getSaveFiretrapSuperviseDict={
                              'orgId':'',
                              'firetrapSupervise.noFiretrapReview':'',
                              'firetrapSupervise.noReport':'',
                              'firetrapSupervise.complete':'',
                              'firetrapSupervise.toReview':'',
                             'state':'',
                             'firetrapSupervise.fireCompanyInfo.companyName':'',
                             'firetrapSupervise.fireCompanyInfo.address':'',
                             'queryParameter.issueSearchType':'',
                             'queryParameter.orgId':'',
                             'queryParameter.reportState':'',
                             'queryParameter.allStateSearch':'',
                             'queryParameter.publicString':'',
                             '_search':'false',
                             'rows':'1000',
                             'page':'1',
                             'sidx':'id',
                             'sord':'desc', 
                            }

checkSaveFiretrapSuperviseDict={
                         'fireCompanyInfoId':None,
                         'companyName':None,
                        }

deleteSaveFiretrapSuperviseDict={
                                 'ids':'',
                                }


#导入单位
data = {
        'dataType':'',
        'enterpriseType':'',
        'isNew':'1',
        'startRow':'4',
        'templates':'',
        }

#导出单位
dlDanWeiData = {
              'fireCompanyInfo.createDept':'',
              'qflag':'',
              'getorgId':'',
              'orgId':"",
              'fireCompanyInfo.companyName':"",
              'fireCompanyInfo.superviseType.propertyDict.displayName':"",
              'fireCompanyInfo.isOffHire':'',
              'fireCompanyInfo.levelShow':0,  #层级：本级-1 全部-0
              '_search':'false',
              'rows':'200',
              'page':'1',
              'sidx':'id',
              'sord':'desc',
              'pageOnly':'false'
              }


#转移单位
changeFireCompanyDict={
                        'companyInfoId':'',
                        'orgId':'',
                        'orgPangtId':'',
                        'targetOrgId':'',
                        'ids':'',
                        }


#单位添加举报检查
saveComplaintHandleDict={
                        'companyCheckRecord.source':'',
                        'complaintHandleInfo.complaintHandleNo':'',
                        'complaintHandleInfo.reporterName':'',
                        'complaintHandleInfo.reporterTelephone':'',
                        'complaintHandleInfo.compliantManner':'',
                        'complaintHandleInfo.handleDate':'',
                        'complaintHandleInfo.handleName':'',
                        'complaintHandleInfo.complaintContent':'',
                        'companyCheckRecord.checkType':'',
                        'companyCheckRecord.dateFrom':'',  
                        'companyCheckRecord.dateTo':'',
                        }

# #检查举报检查项
# getSaveComplaintHandleDict={
#                          'state':'',
#                          'firetrapSupervise.fireCompanyInfo.companyNo':'',
#                          'firetrapSupervise.fireCompanyInfo.companyName':'',
#                          'firetrapSupervise.fireCompanyInfo.address':'',
#                          'queryParameter.issueSearchType':'',
#                          'queryParameter.orgId':'',
#                          'queryParameter.allStateSearch':'',
#                          'queryParameter.publicString':'',
#                          '_search':'false',
#                          'rows':'1000',
#                          'page':'1',
#                          'sidx':'id',
#                          'sord':'desc', 
#                         }
# 
# checkSaveComplaintHandleDict={
#                          'fireCompanyInfoId':None,
#                          'companyName':None,
#                         }

#复查
saveFiretrapReviewDict={
                        'calculationMode':'',
                        'superviseState':'',
                        'firetrapReview.firetrapReviewNo':'',
                        'companyName':'',
                        'superviseNo':'',
                        'reviewItems[0].id':'',
                        'reviewItems[0].checkItemId':'',
                        'reviewItems[0].state':'',
                        'firetrapReview.reviseState':'',
                        'firetrapReview.reviewState':'',  
                        'firetrapReview.reviewPersonName':'',
                        'firetrapReview.reviewPerson':'',
                        'firetrapReview.reviewDate':'',
                        'companyCheckRecordId':'',
                        'operateMode':'',
                        'firetrapReview.updateDept':'',
                        'firetrapReview.createDept':'',
                        'firetrapReview.firetrapSuperviseId':'',
                        'checkItemIndexs':'',
                        'checkItemCodes':'',
                        'superviseResultAttachment':'',
                        '__multiselect_reviewResult':'',
                        'firetrapReview.firetrapReviewId':'',
                        'attachfileNamelist':'',
                        }

#上报
saveCompanyCheckRecordTaskDict={
                                'oldCheckRecordId':'',
                                'reportState':'',
                                'companyCheckRecord.fireCompanyInfoId':'',
                                'companyCheckRecord.source':'',
                                'companyCheckRecord.checkType':'',
                                'companyName':'',
                                'address':'',
                                'manger':'',
                                'managerTelephone':'',
                                'companyCheckRecord_assignUserVoto':'',  
                                'companyCheckRecord.assignUser':'',
                                'companyCheckRecord_assignDeptVo':'',
                                'companyCheckRecord.assignDept':'',
                                'companyCheckRecord.dateTo':'',
                                'companyCheckRecord.dateFrom':'',
                                }

#检查上报督改项
getCompanyCheckRecordTaskDict={
                             'state':'',
                             'queryParameter.issueSearchType':'',
                             'queryParameter.orgId':'',
                             'queryParameter.reportState':'',
                             'queryParameter.allStateSearch':'',
                             'queryParameter.publicString':'',
                             '_search':'false',
                             'rows':'1000',
                             'page':'1',
                             'sidx':'id',
                             'sord':'desc', 
                            }

#删除上报督改检查项
deleteFiretrapReviewDict={
                        'ids':'',
                        }

#新增专项任务
SaveFirecheckTaskDict={
                    'mode':'',
                    'firecheckTask.firecheckTaskId':'',
                    'firecheckTask.taskName':'',
                    'firecheckTask.dateFrom':'',
                    'firecheckTask.dateTo':'',
                    'firecheckTask.rentHouseCatalogue':'',
                    '__multiselect_firecheckTask.rentHouseCatalogue':'',
                    '__multiselect_firecheckTask.rentHousePerson':'',
                    '__multiselect_firecheckTask.industrialCatalogue':'',
                    '__multiselect_firecheckTask.businessCatalogue':'',
                    '__multiselect_firecheckTask.educationCatalogue':'',
                    '__multiselect_firecheckTask.hospitalCatalogue':'',
                    '__multiselect_firecheckTask.entertainmentCatalogue':'',
                    '__multiselect_firecheckTask.explosiveCatalogue':'',
                    'firecheckTask.everyRandomNum':'',
                    }


#检查专项任务
getFirecheckTaskDict={
                             'getorgId':'',
                             '_search':'false',
                             'rows':'1000',
                             'page':'1',
                             'sidx':'id',
                             'sord':'desc', 
                            }

checkFirecheckTaskDict={
                         'firecheckTaskId':None,
                         'taskName':None,
                        }

#删除专项任务
deleteFirecheckTaskDict={
                        'firecheckTaskId':'',
                        }

#分派专项任务
SaveTaskItemDict={
                    'firecheckTaskId':'',
                    'userLoginId':'',
                    'orgId':'',
                    'companyIdList':'',
                    }

#检查分派专项任务
getSaveTaskItemDict={
                             'orgId':'',
                             'state':'',
                             'queryParameter.issueSearchType':'',
                             'queryParameter.orgId':'',
                             'queryParameter.allStateSearch':'',
                             'queryParameter.publicString':'',
                             'firetrapSupervise.fireCompanyInfo.companyName':'',
                             'firetrapSupervise.fireCompanyInfo.address':'',
                             '_search':'false',
                             'rows':'1000',
                             'page':'1',
                             'sidx':'id',
                             'sord':'desc', 
                            }

#分派检查
assignCheckRecordDict={
                        'companyCheckRecord.companyCheckRecordId':'',
                        'companyCheckRecord.source':'',
                        }

#检查分派
getAssignCheckRecordDict={
                             'queryParameter.issueSearchType':'',
#                              'firetrapSupervise.fireCompanyInfo.companyName':'',
#                              'firetrapSupervise.fireCompanyInfo.address':'',
#                              'queryParameter.issueSearchType':'',
                             'queryParameter.orgId':'',
#                              'queryParameter.reportState':'',
                             'queryParameter.allStateSearch':'',
                             'queryParameter.publicString':'',
                             '_search':'false',
                             'rows':'1000',
                             'page':'1',
                             'sidx':'id',
                             'sord':'desc', 
                            }

#检查下辖记录
getSubordinateListDict={
                             'orgId':'',
                             'firetrapSupervise.orgIdForSearch':'',
                             'firetrapSupervise.fireCompanyInfo.companyName':'',
                             'firetrapSupervise.fireCompanyInfo.address':'',
                             'queryParameter.orgId':'',
                             'firetrapSupervise.query':'',
                             'queryParameter.allStateSearch':'',
                             'queryParameter.publicString':'',
                             '_search':'false',
                             'rows':'1000',
                             'page':'1',
                             'sidx':'id',
                             'sord':'desc', 
                            }

deleteSubordinateListDict={
                                 'ids':'',
                                }

#导出下辖记录
dlJiLuData= {
              'firetrapSupervise.orgIdForSearch':'',
              'state':'',
              'firetrapSupervise.noFiretrapReview':'',
              'firetrapSupervise.noReport':'',
              'firetrapSupervise.complete':'',
              'firetrapSupervise.state':'',
              'firetrapSupervise.fireCompanyInfo.companyNo':'',
              'firetrapSupervise.fireCompanyInfo.companyName':'',
              'firetrapSupervise.fireCompanyInfo.address':'',
              'firetrapSupervise.companyCheckRecord.source':'',
              'queryParameter.allStateSearch':'',
              'queryParameter.orgId':'',
              'queryParameter.publicString':'',
              'queryParameter.reportState':'',
              'queryParameter.superviseTypeDisplayName':'',
              'queryParameter.startCheckDate':'',
              'queryParameter.endCheckDate':'',
              'firetrapSupervise.query':'',
              '_search':'false',
              'rows':'200',
              'page':'1',
              'sidx':'id',
              'sord':'desc',
              'orgId':'',
              'getorgId':'',
              'pageOnly':'false'
              }
