# -*- coding:UTF-8 -*-
'''
Created on 2015-11-16

@author: chenyan
'''
#新增
populationObject = {
                    "mode":"",               
                    "population.id":"",
                    "contextId":"",
                    "updateType:":"",                         
                    "population.organization.id":"",
                    "population.imgUrl":"",
                    "population.logOut":"",
                    "population.actualPopulationType":"",
                    "population.attentionPopulationType":"",
                    "population.settleTime":"",
                    "population.outGone":"",
                    "population.baseInfo":"",
                    "population.organization.orgName":"",
                    "population.idCardNo":"", 
                    "population.name":"",
                    "population.gender.id":"",
                    "population.usedName":"",
                    "population.mobileNumber":"",
                    "population.telephone":"",
                    "population.birthday":"",
                    "population.nation.id":"",
                    "population.politicalBackground.id":"",
                    "population.schooling.id":"",
                    "population.career.id":"",
                    "population.workUnit":"",
                    "population.maritalState.id":"",
                    "population.death":"",
                    "householdStaffIds":"",
                    "population.stature":"",
                    "population.bloodType.id":"",
                    "population.faith.id":"",
                    "population.email":"",
                    "population.province":"",
                    "population.city":"",
                    "population.district":"",
                    "population.nativePlaceAddress":"",
                    "population.nativePoliceStation":"",
                    "population.isHaveHouse1":"",
                    "population.noHouseReason":"",
                    "population.houseId":"",
                    "population.currentAddress":"",
                    "population.otherAddress":"",
                    "population.remark":"",                                      
                    }

huzhuObject = {
              "population.houseId":"",
              "mode":"",               
              "cacheId.id":"",
              "contextId":"",
              "population.id":"",
              "population.organization.id":"",
              "population.imgUrl":"",
              "population.attentionPopulationType":"",
              "population.settleTime":"",
              "dailogName":"",
              "englishName":"",
              "population.organization.orgName":"",
              "population.idCardNo":"", 
              "population.accountNumber":"",
              "population.relationShipWithHead.id":"",
              "population.homePhone":"",
              "population.residentStatus.id":"",
              "population.residenceType.id":"",
              "population.outReasons.id":"",
              "population.outReasons":"",
              "population.outProvince":"",
              "population.outCity":"",
              "population.outDistrict":"",
              "population.goOutDetailedAddress":""
              }

checkPopulationDict={
#                      "detailNativeAddress":None,
#                      "certificateType":None,
                     "idCardNo":None,
                     "name":None,
                     }

getHuJiOrgDict= {
                 "searchMode":"noFast_noAdvanced_search",
                 "householdStaffVo.logout":"0",
                 "householdStaffVo.isDeath":"0",
                 "orgId":"",
                 "rows":"1000",
                 "page":"1",
                 "sidx":"id",
                 "sord":"desc",            
                 }
##查找其他人员
checkOtherPerson = {
               'organizationId':None,
                'population.isEmphasis':0,
                '_search':'false',
                'rows':'20',
                'page':'1',
                'sidx':'id',
                'sord':'desc'     
                    }

delHuJiDict={
            "householdStaffVo.idStr":"",
            }

logoutHuJiDict={
                "populationIds":"",
                "population.logoutDetail.logout":"",
                "population.logoutDetail.logoutDate":"",
                "population.logoutDetail.logoutReason":"",
                }

transferObject={
                "orgId":"",
                "Ids":"",
                "toOrgId":"",
                "type":"",
                "isTransfer":"",
                }

searchHuJiOrgDict= {
                 "actualPopulationType":None,
                 "createDate":None,
                 "death":None,
                 "detailNativeAddress":None,
                 "detailOutAddress":None,
                 "fullPinyin":None,
                 "id":None,
                 "idCardNo":None,
                 "logOut":None,
                 "logoutDetail":None,
                 "name":None,
                 "orgInternalCode":None,
                 "organization":None,
                 "outGone":None,
                 "simplePinyin":None,
                 "sourcesState":None,
                 "uuid":None,        
                 }

data = {
        'dataType':'',
        'enterpriseType':'',
        'isNew':'1',
        'reportTime':'',
        'startRow':'4',
        'templates':'',
        'yearDate':''
        }

dlHuJiData = {
          'searchMode':'',
          'orgId':"",
          'householdStaffVo.logout':0,
          'householdStaffVo.isDeath':0,
          '_search':'false',
          'rows':'200',
          'page':'1',
          'sidx':'id',
          'sord':'desc',
          'pageOnly':'false'
          }

fuWuRenYuanDict={
                 "serviceTeamMemberBase.id":"",
                 "serviceTeamMemberBase.org.id":"",
                 "addTeam":"",
                 "serviceTeamMemberBase.name":"",
                 "serviceTeamMemberBase.gender.id":"",
                 "serviceTeamMemberBase.job":"",
                 "serviceTeamMemberBase.birthday":"",
                 "serviceTeamMemberBase.mobile":"",
                 "serviceTeamMemberBase.homePhone":"",
                 "serviceTeamMemberBase.remark":"",
                 "positionInTeam":"",
                 "isSubmit":""
                 }

serviceMemberDict={
                 "serviceMemberWithObject.memberId":"",
                 "serviceMemberWithObject.objectType":"",
                 "serviceMemberWithObject.objectName":"",
                 "serviceMemberWithObject.objectId":"",
                 "serviceMemberWithObject.teamMember":"",
                 "serviceMemberWithObject.onDuty":"",
                 "serviceMemberWithObject.objectLogout":"",
                 }

getServiceMemberDict={
                      "serviceMemberVo.objectType":"",
                      "serviceMemberVo.objectId":"",
                      "serviceMemberVo.objectName":"",
                      "_search":"false",
                      "rows":"1000",
                      "page":"1",
                      "sidx":"id",
                      "sord":"desc",  
                      }

deleteServiceMemberDict={
                         "selectedIds":"",
                         }

leaveOrBackServiceMemberDict={
                         "serviceMemberWithObject.id":"",
                         'serviceMemberWithObject.onDuty':"",
                         'serviceMemberWithObject.memberId':""
                         }

getLeaveServiceMemberDict={
                      "serviceMemberVo.objectType":"householdStaff",
                      "serviceMemberVo.objectId":"",
                      "serviceMemberVo.onDuty":"",
                      "serviceMemberVo.teamMember":"",
                      "_search":"false",
                      "rows":"1000",
                      "page":"1",
                      "sidx":"id",
                      "sord":"desc",  
                      }


checkServiceMemberDict={
                      "memberName":None,
                      "memberId":None,
                      }

serviceGuardersDict={
                 "serviceTeamMemberVo.org.id":"",
                 "serviceTeamGuarders.serviceGuardersWithObject.objectType":"",
                 "serviceTeamGuarders.serviceGuardersWithObject.objectName":"",
                 "serviceTeamGuarders.serviceGuardersWithObject.objectId":"",
                 "serviceTeamGuarders.serviceGuardersWithObject.teamMember":"",
                 "isSubmit":"",
                 "serviceTeamGuarders.guarderName":"",
                 "serviceTeamGuarders.gender.id":"",
                 "serviceTeamGuarders.relation":"",
                 "serviceTeamGuarders.idCardNo":"",
                 "serviceTeamGuarders.mobile":"",
                 "serviceTeamGuarders.phone":"",
                 "serviceTeamGuarders.remark":"",
                 "serviceTeamGuarders.id":""
                 }

serviceRecordDict={
                   "mode":"",
                   "serviceRecord.userOrgId":"1",
                   "serviceRecord.organization.id":"",
                   "serviceRecord.id":"",
                   "serviceRecord.teamId":"0",
                   "isSubmit":"",
                   "serviceRecord.occurDate":"",
                   "serviceRecord.occurPlace":"",
                   "serviceRecord.serviceMembers":"",
                   "serviceRecord.serviceJoiners":"",
                   "serviceRecord.serviceObjects":"",
                   "serviceRecord.serviceContent":"",
                   "serviceRecord.visitSituation.id":"",
                   "serviceRecord.createUser":"",
                   "serviceRecord.createDate":"",
                   "attachFileUrls":""
                   }

deleteServiceRecordDict={
                      "mode":'',
                      "recordIds":''
                      }

checkServiceRecordDict={
                      "id":None,
                      "occurDate":None,
                      "occurPlace":None,
                      "serviceMembers":None,
                      }

getServiceRecordDict={
                      "objectIds":"",
                      "populationType":"householdStaff",
                      "serviceRecordVo.organization.id":"",
                      "rows":"1000",
                      "page":"1",
                      "sidx":"id",
                      "sord":"desc", 
                      }



getLiuDongOrgDict= {
                    "objectIds":"",
                    "populationType":"",
                    "serviceRecordVo.organization.id":"",
                    "serviceRecordVo.displayYear":"",
                    "_search":"false",
                    "rows":"1000",
                    "page":"1",
                    "sidx":"id",
                    "sord":"desc",            
                    }

delLiuDongDict={
                "floatingPopulationIds":"",
                }

dlLiuDongData = {
          'organizationId':'',
          'searchFloatingPopulationVo.logout':0,
          'searchFloatingPopulationVo.isDeath':'False',
          '_search':'false',
          'rows':'200',
          'page':'1',
          'sidx':'id',
          'sord':'desc',
          'pageOnly':'false'
          }



unsettledPopulationObject = {
                    "mode":"",   
                    "modeType":"", 
                    "populationType":"",           
                    "unsettledPopulation.id":"",                        
                    "ownerOrg.id":"",
                    "unsettledPopulation.organization.id":"",
                    "personTypeName":"",
                    "unsettledPopulation.logOut":"",
                    "unsettledPopulation.organization.orgName":"",
                    "unsettledPopulation.idCardNo":"",
                    "unsettledPopulation.name":"",
                    "unsettledPopulation.gender.id":"",
                    "unsettledPopulation.usedName":"", 
                    "unsettledPopulation.mobileNumber":"",
                    "unsettledPopulation.telephone":"",
                    "unsettledPopulation.birthday":"",
                    "unsettledPopulation.nation.id":"",
                    "unsettledPopulation.politicalBackground.id":"",
                    "unsettledPopulation.schooling.id":"",
                    "unsettledPopulation.career.id":"",
                    "unsettledPopulation.workUnit":"",
                    "unsettledPopulation.maritalState.id":"",
                    "unsettledPopulation.stature":"",
                    "unsettledPopulation.bloodType.id":"",
                    "unsettledPopulation.faith.id":"",
                    "unsettledPopulation.email":"",
                    "unsettledPopulation.unSettedTime":"",
                    "unsettledPopulation.unSettedReason.id":"",
                    "unsettledPopulation.certificateType.id":"",
                    "unsettledPopulation.certificateNo":"",
                    "unsettledPopulation.province":"",
                    "unsettledPopulation.city":"",
                    "unsettledPopulation.district":"",
                    "unsettledPopulation.nativePlaceAddress":"",
                    "unsettledPopulation.isHaveHouse1":"",   
                    "unsettledPopulation.noHouseReason":"",
                    "unsettledPopulation.houseId":"",
                    "unsettledPopulation.currentAddress":"",
                    "unsettledPopulation.otherAddress":"",
                    "unsettledPopulation.remark":"",                                 
                    }
#未落户人员查询参数
weiLuoHuChaXun={
                    'orgId':'',
                    'unsettledPopulationCondition.logOut':'0',
                    'unsettledPopulationCondition.isDeath':'0',
                    'unsettledPopulationCondition.fastSearchKeyWords':'',
                    '_search':'false',
                    'rows':'200',
                    'page':'1',
                    'sidx':'id',
                    'sord':'desc'               
                }
#未落户高级查询参数
weiLuoHuGaoJiChaXun={
                'orgId':'',
                'unsettledPopulationCondition.name':'',
                'unsettledPopulationCondition.usedName':'',
                'unsettledPopulationCondition.gender.id':'',
                'unsettledPopulationCondition.idCardNo':'',
                'unsettledPopulationCondition.certificateType.id':'',
                'unsettledPopulationCondition.certificateNo':'',
                'unsettledPopulationCondition.nativePlaceAddress':'',
                'unsettledPopulationCondition.politicalBackground.id':'',
                'unsettledPopulationCondition.currentAddress':'',
                'unsettledPopulationCondition.workUnit':'',
                'unsettledPopulationCondition.telephone':'',
                'unsettledPopulationCondition.mobileNumber':'',
                'unsettledPopulationCondition.birthdayStart':'',
                'unsettledPopulationCondition.birthdayEnd':'',
                'unsettledPopulationCondition.unSettedReason.id':'',
                'unsettledPopulationCondition.unsettedTimeStart':'',
                'unsettledPopulationCondition.unsettedTimeEnd':'',
                'unsettledPopulationCondition.serviceDateStart':'',
                'unsettledPopulationCondition.serviceDateEnd':'',
                'unsettledPopulationCondition.province':'',
                'unsettledPopulationCondition.city':'',
                'unsettledPopulationCondition.district':'',
                'unsettledPopulationCondition.maritalState.id':'',
                'unsettledPopulationCondition.nation.id':'',
                'unsettledPopulationCondition.faith.id':'',
                'unsettledPopulationCondition.schooling.id':'',
                'unsettledPopulationCondition.bloodType.id':'',
                'unsettledPopulationCondition.email':'',
                'unsettledPopulationCondition.stature':'',
                'unsettledPopulationCondition.career.id':'',
                '_search':'false',
                'rows':'200',
                'page':'1',
                'sidx':'id',
                'sord':'desc' 
                    }
getWeiLuoHuDict= {
                  'orgId':'',
                  'logOut':'0',
                  'rows':'100',
                  'page':'1',
                  'sidx':'id',
                  'sord':'desc'
                  }

delWeiLuoHuDict={
                 "unsettledPopulationIds":""
                 }


dlWeiLuoHuData = {
          'orgId':'',
          'logout':0,
          '_search':'false',
          'rows':'200',
          'page':'1',
          'sidx':'id',
          'sord':'desc',
          'pageOnly':'false'
          }


overseaPopulationObject = {
                    "mode":"",    
                    "populationType":"",           
                    "overseaPersonnel.id":"",                        
                    "overseaPersonnel.organization.id":"",
                    "overseaPersonnel.imgUrl":"",
                    "houseInfo.houseType.id":"",
                    "overseaPersonnel.logOut":"",
                    "overseaPersonnel.englishName":"", 
                    "overseaPersonnel.name":"",
                    "overseaPersonnel.gender.id":"",
                    "overseaPersonnel.birthday":"",
                    "overseaPersonnel.mobileNumber":"",
                    "overseaPersonnel.telephone":"",
                    "overseaPersonnel.nationality":"",
                    "overseaPersonnel.certificateType.id":"",
                    "overseaPersonnel.certificateNo":"",
                    "overseaPersonnel.certificateStrartDay":"",
                    "overseaPersonnel.certificateEndDay":"",
                    "overseaPersonnel.isHaveHouse1":"",
                    "overseaPersonnel.noHouseReason":"",
                    "overseaPersonnel.houseId":"",
                    "overseaPersonnel.currentAddress":"",
                    "overseaPersonnel.inflowReason":"",
                    "overseaPersonnel.profession.id":"",
                    "overseaPersonnel.nativePlaceAddress":"",
                    "overseaPersonnel.mail":"",
                    "overseaPersonnel.workUnit":"",
                    "overseaPersonnel.arrivalTime":"",
                    "overseaPersonnel.leaveTime":"",
                    "overseaPersonnel.remark":"",                                    
                    }
#境外快速搜索参数
jingWaiFastSearch={
                    'orgId':'',
                    'searchOverseaPersonnelVo.logOut':0,
                    'searchOverseaPersonnelVo.fastSearchKeyWords':'',
                    '_search':'false',
                    'rows':200,
                    'page':1,
                    'sidx':'id',
                    'sord':'desc'                   
                   }
#境外人员高级搜索
jingWaiSeniorSearch={
                     
                     }
getJingWaiOrgDict= {
                    "orgId":"",
                    "overseaPersonnel.logOut":"0",
                    "_search":"false",
                    "rows":"1000",
                    "page":"1",
                    "sidx":"id",
                    "sord":"desc",            
                    }

checkJingWaiOrgDict= {
                    "certificateNo":None,
                    "certificateType":None,
                    "englishName":None,  
                    "idCardNo":None,   
                    }

delJingWaiDict={
                "deleteIds":"",
                }

dlJingWaiHuData = {
          'orgId':'',
          'overseaPersonnel.logOut':0,
          '_search':'false',
          'rows':'200',
          'page':'1',
          'sidx':'id',
          'sord':'desc',
          'pageOnly':'false'
          }


houseFamilyObject = {
                     "newHouseHold.accountNumber":"",
                     "newHouseHold.id":"",
                     "orgId":"",
                     }

familyObject = {
                "familyid":""
                }

deleteFamilyObject = {
                     "ids":"",
                     }

getHouseFamilyDict= {
                    "orgId":"",
                    "_search":"false",
                    "rows":"1000",
                    "page":"1",
                    "sidx":"cen_id",
                    "sord":"desc",            
                    }

checkHouseFamilyDict={
                      "censusRegisterFamily":None,
                      "id":None,
                      }

houseMemberObject = {
                     "orgId":"",
                     "houseFamilyId":"",
                     "householdStaffId":"",
                     "accountNumber":"",
                     }

getHouseMemberDict= {
                      "householdStaffVo.logout":"0",
                      "orgId":"",
                      "houseFamily.id":"",
                      "rows":"1000",
                      "page":"1",
                      "sidx":"id",
                      "sord":"desc",            
                      }

checkHouseMemberDict={
                       "accountNumber":None,
                       "censusRegisterFamily":None,
                       "idCardNo":None,
                       "name":None,
                       }

viewDataObject={
                "mode":"",
                "viewdata.id":"",
                "viewdata.fromSystem":"",
                "viewdata.organization.id":"",
                "viewdata.status":"",
                "viewdata.viewName":"",
                "viewdata.viewDate":"",
                "viewdata.family.householdName":"",
                "viewdata.viewInfo":""
                }

deleteDict={
            "ids":'',
            }

searchViewDataDict={
                    "searchViewdataVo.orgId":'',
                    "searchViewdataVo.viewName":'',
                    "searchViewdataVo.status":'',
                    "searchViewdataVo.viewDateFrom":'',
                    "searchViewdataVo.viewDateTo":'',
                    "searchViewdataVo.headName":'',
                    "_search":"false",
                    "rows":"1000",
                    "page":"1",
                    "sidx":"createDate",
                    "sord":"desc",
                    }

sentViewDataObject={
                    "issueNew.viewDataIds":"",
                    "issueNew.occurOrg.id":"",
                    "issueNew.subject":"",
                    "eventOccurOrgSelector":"",
                    "issueNew.createPersonId":"",
                    "issueNew.createPerson":"",
                    "issueNew.sourceMobile":"",
                    "issueNew.sourcePerson":"",
                    "issueNew.issueTypeName":"",
                    "issueNew.issueContent":""
                    }

checkViewDataDict={
                   "id":None,
                   "viewName":None,
                   "status":None
                   }

getViewDataDict={
                 "searchViewdataVo.orgId":'',
                 "_search":"false",
                 "rows":"1000",
                 "page":"1",
                 "sidx":"createDate",
                 "sord":"desc",
                 }


actualPopulationTypeDict={
                          "huJiRenKou":"householdStaff",
                          "liuDongRenKou":"floatingPopulation",
                          }


populationTypeDict={
                      "xingManShiFangRenYuan":"positiveInfo",
                      "sheQuJiaoZhengRenYuan":"rectificativePerson",
                      "jingShenBingRenYuan":"mentalPatient",
                      "xiDuRenYuan":"druggy",
                      "zhongDianQingShaoNian":"idleYouth",
                      "zhongDianShangFangRenYuan":"superiorVisit",
                      "weiXianPingCongYeRenYuan":"dangerousGoodsPractitioner",
                      "qiTaRenYuan":"otherAttentionPersonnel",
                      "jianYiYongWei":"samaritanPeople",
                      "laoNianRen":"elderlyPeople",
                      "canJiRen":"handicapped",
                      "youFuDuiXiang":"optimalObject",
                      "xuYaoJiuZhuRenYuan":"aidNeedPopulation",
                      "shiYeRenYuan":"unemployedPeople",
                      "yuLingFuNv":"nurturesWomen",
                      "qiaoShu":"abroadDependent",
                      "shiDiJiaTing":"lostEarth",
                      "qiuZhiRenYuan":"bewerBung",  
                      "qingShaoNian":"youth"                                        
                      }

zhongDianPopulationObject = {
                    "mode":"",               
                    "population.id":"",                       
                    "population.organization.id":"",
                    "population.actualPopulationType":"",
                    "population.attentionPopulationType":"",
                    "population.imgUrl":"",
                    "population.organization.orgName":"",
                    "population.idCardNo":"", 
                    "population.name":"",
                    "actualPersonType":"",
                    "population.gender.id":"",
                    "population.usedName":"",
                    "population.mobileNumber":"",
                    "population.telephone":"",
                    "population.birthday":"",
                    "population.career.id":"",
                    "population.politicalBackground.id":"",
                    "population.schooling.id":"",
                    "population.nation.id":"",
                    "population.maritalState.id":"",
                    "population.death":"",
                    "population.stature":"",
                    "population.bloodType.id":"",
                    "population.faith.id":"",
                    "population.email":"",
                    "population.province":"",
                    "population.city":"",
                    "population.district":"",
                    "population.nativePlaceAddress":"",
                    "population.nativePoliceStation":"",
                    "population.isHaveHouse1":"",
                    "population.noHouseReason":"",
                    "population.houseId":"",
                    "population.currentAddress":"",
                    "population.otherAddress":"",
                    "population.remark":"",   
                    "contextId":"",   
                    "cacheId.id":"",
                    "isSubmit":"", 

                    "population.controlledStandards.id":"",
                    "population.caseReason":"",
                    "population.positiveInfoType.id":"",
                    "population.laborEduAddress":"",
                    "population.imprisonmentDate":"",
                    "population.releaseOrBackDate":"",
                    "population.criminalBehavior":"",
                    "population.agoProfession.id":"",
                    "population.resettlementDate":"",
                    "population.crimeDate":"",
                    "population.noResettlementReason":"", 

                    "population.accusation":"",
                    "population.executeType.id":"",
                    "population.penaltyTerm":"",
                    "population.rectifyStartDate":"",
                    "population.rectifyEndDate":"",
                    "population.recentSituation":"",             
   
                    "population.dangerLevel.id":"",
                    "population.psychosisName":"",
                    "population.cureDepartmen":"",  
                      
                    "population.attentionExtent.id":"",
                    "population.detoxicateCondition.id":"",
                    "population.drugFristDate":"",
                    "population.ferretOutDate":"",
                    "population.birthday":"",
                    "population.controlActuality":"",
                    "population.drugReason.id":"",
                    "population.drugSource.id":"",
                    "population.detoxicateCase.id":"",
                    "population.drugType":"",
 
                    "population.workCondition":"",
                    "staffTypeIds":"",
 
                    "population.visitState.id":"",
                    "supval_just_marked":"",
                    "population.visitReason":"", 
    
                    "population.dangerousWorkingType.id":"",
                    "population.workingCertificate":"",
                    "population.workingCertificateNo":"",
                    "population.periodOfValidityStart":"",
                    "population.periodOfValidityEnd":"",
                    "population.legalPerson":"",
                    "population.legalPersonMobileNumber":"",
                    "population.legalPersonTelephone":"",
                    "population.workUnit":"",
                             
                    "population.attentionReason":"",
                    }

getPopulationDict= {
                    "organizationId":"",
                    "population.isEmphasis":"0",
                    "rows":"1000",
                    "page":"1",
                    "sidx":"id",
                    "sord":"desc",            
                    }

deleteDict= {
             "populationIds":"",        
             }

transferDict= {
               "dailogName":"",     
               "population.id":"", 
               "id":"", 
               "organizationId":"",    
               "type":""
               }
#刑满释放人员快速搜索参数
xingManShiFangFastSearch={
                'organizationId':'',
                'searchPositiveInfoVo.isEmphasis':'0',
                'searchPositiveInfoVo.fastSearchKeyWords':'',
                '_search':'false',
                'rows':'20',
                'page':'1',
                'sidx':'id',
                'sord':'desc'                     
                          }
#快速搜索公共参数
fastSearch={
                'organizationId':'',
#                 'searchPositiveInfoVo.isEmphasis':'0',
#                 'searchPositiveInfoVo.fastSearchKeyWords':'',
                '_search':'false',
                'rows':'200',
                'page':'1',
                'sidx':'id',
                'sord':'desc'                     
                          }

#刑满释放人员高级查询参数
xingManShiFangSeniorSearch={
                'searchPositiveInfoVo.isEmphasis':'-1',
                'organizationId':'',
                'searchPositiveInfoVo.isDeath':'-1',
                'searchPositiveInfoVo.idCardNo':'',
                'searchPositiveInfoVo.name':'',
                'searchPositiveInfoVo.positiveInfosType.id':'',
                'searchPositiveInfoVo.mobileNumber':'',
                'searchPositiveInfoVo.caseReason':'',
                'searchPositiveInfoVo.imprisonmentDate':'',
                'searchPositiveInfoVo.agoProfession.id':'',
                'searchPositiveInfoVo.laborEduAddress':'',
                'searchPositiveInfoVo.hasServiceTeamMember':'-1',
                'searchPositiveInfoVo.hasServiceTeamRecord':'-1',
                'searchPositiveInfoVo.schooling.id':'',
                'searchPositiveInfoVo.releaseOrBackDate':'',
                'searchPositiveInfoVo.endReleaseOrBackDate':'',
                'searchPositiveInfoVo.resettlementDate':'',
                'searchPositiveInfoVo.crimeDate':'',
                'searchPositiveInfoVo.endCrimeDate':'',
                'searchPositiveInfoVo.birthday':'',
                'searchPositiveInfoVo.endBirthday':'',
                'searchPositiveInfoVo.gender.id':'',
                'searchPositiveInfoVo.career.id':'',
                'searchPositiveInfoVo.province':'',
                'searchPositiveInfoVo.city':'',
                'searchPositiveInfoVo.district':'',
                'searchPositiveInfoVo.nativePlaceAddress':'',
                'searchPositiveInfoVo.workUnit':'',
                'searchPositiveInfoVo.currentlyAddress':'',
                '_search':'false',
                'rows':'200',
                'page':'1',
                'sidx':'id',
                'sord':'desc'                            
                            }
#矫正人员高级搜索参数
jiaoZhengSeniorSearch={
                'searchRectificativePersonVo.isEmphasis':'-1',
                'organizationId':'',
                'searchRectificativePersonVo.isDeath':'-1',
                'searchRectificativePersonVo.idCardNo':'',
                'searchRectificativePersonVo.name':'',
                'searchRectificativePersonVo.executeTypeId':'',
                'searchRectificativePersonVo.mobileNumber':'',
                'searchRectificativePersonVo.rectifyStartDate':'',
                'searchRectificativePersonVo.rectifyEndDate':'',
                'searchRectificativePersonVo.genderId':'',
                'searchRectificativePersonVo.schooling.id':'',
                'searchRectificativePersonVo.hasServiceTeamMember':'-1',
                'searchRectificativePersonVo.hasServiceTeamRecord':'-1',
                'searchRectificativePersonVo.startBirthday':'',
                'searchRectificativePersonVo.endBirthday':'',
                'searchRectificativePersonVo.province':'',
                'searchRectificativePersonVo.city':'',
                'searchRectificativePersonVo.district':'',
                'searchRectificativePersonVo.nativePlaceAddress':'',
                'searchRectificativePersonVo.currentAddress':'',
                '_search':'false',
                'rows':'200',
                'page':'1',
                'sidx':'id',
                'sord':'desc'                    
                       }
#高级搜索公共参数
seniorSearch={
              'organizationId':'914',
                '_search':'false',
                'nd':'1463562689394',
                'rows':'20',
                'page':'1',
                'sidx':'id',
                'sord':'desc',
              }
#精神病人员高级搜索参数
jingShenBingSeniorSearch={
                'searchMentalPatientVo.isEmphasis':'-1',
                'organizationId':'',
                'searchMentalPatientVo.isDeath':'-1',
                'searchMentalPatientVo.idCardNo':'',
                'searchMentalPatientVo.name':'',
                'searchMentalPatientVo.startBirthday':'',
                'searchMentalPatientVo.endBirthday':'',
                'searchMentalPatientVo.genderId':'',
                'searchMentalPatientVo.dangerLevelId':'',
                'searchMentalPatientVo.hasIsTreatType.code':'-1',
                'searchMentalPatientVo.cureDepartment':'',
                'searchMentalPatientVo.nativeProvince':'',
                'searchMentalPatientVo.nativeCity':'',
                'searchMentalPatientVo.nativeDistrict':'',
                'searchMentalPatientVo.hasServiceTeamMember':'-1',
                'searchMentalPatientVo.hasServiceTeamRecord':'-1',
                'searchMentalPatientVo.nativePlaceAddress':'',
                'searchMentalPatientVo.currentAddress':'',
                'searchMentalPatientVo.nation.id':'',
                'searchMentalPatientVo.politicalBackground.id':'',
                'searchMentalPatientVo.maritalState.id':'',
                'searchMentalPatientVo.schooling.id':'',
                'searchMentalPatientVo.career.id':'',
                'searchMentalPatientVo.workUnit':'',
                'searchMentalPatientVo.startStature':'',
                'searchMentalPatientVo.endStature':'',
                'searchMentalPatientVo.bloodType.id':'',
                'searchMentalPatientVo.faith.id':'',
                'searchMentalPatientVo.email':'',
                'searchMentalPatientVo.telephone':'',
                'searchMentalPatientVo.mobileNumber':'',
                '_search':'false',
                'rows':'20',
                'page':'1',
                'sidx':'id',
                'sord':'desc'                        
                         }
dlZhongDianData = {
          'organizationId':'',
          'population.isEmphasis':0,
          '_search':'false',
          'rows':'200',
          'page':'1',
          'sidx':'id',
          'sord':'desc',
          'pageOnly':'false'
          }



guanHuaiDuiXiangObject = {
                    "mode":"",               
                    "population.id":"",                       
                    "population.organization.id":"",
                    "population.actualPopulationType":"",
                    "population.attentionPopulationType":"",
                    "population.imgUrl":"",
                    "population.organization.orgName":"",
                    "population.idCardNo":"", 
                    "population.name":"",
                    "actualPersonType":"",
                    "population.gender.id":"",
                    "population.usedName":"",
                    "population.mobileNumber":"",
                    "population.telephone":"",
                    "population.birthday":"",
                    "population.career.id":"",
                    "population.politicalBackground.id":"",
                    "population.schooling.id":"",
                    "population.nation.id":"",
                    "population.maritalState.id":"",
                    "population.stature":"",
                    "population.bloodType.id":"",
                    "population.faith.id":"",
                    "population.email":"",
                    "population.province":"",
                    "population.city":"",
                    "population.district":"",
                    "population.nativePlaceAddress":"",
                    "population.nativePoliceStation":"",
                    "population.isHaveHouse1":"",
                    "population.noHouseReason":"",
                    "population.houseId":"",
                    "population.currentAddress":"",
                    "population.otherAddress":"",
                    "population.remark":"",   
                    "contextId":"",   
                    "cacheId.id":"",
                    "isSubmit":"", 

                    "population.occurrenceDate":"",
                    "population.sureDate":"",
                    "population.occurrencePlace":"",
                    "population.institutionName":"",
                    "population.glories":"",
                    "population.medicalInsurance":"",
                    "population.socialInsurance":"",
                    "population.minLivingStandard":"",
                    "population.sympathyCount":"",
                    "population.donation":"",
                    "population.healthStatus.id":"", 
                    "population.disability":"",
                    "population.treatments":"",
                    "population.poorFamilies":"",
                    "population.income":"",
                    "population.mainEvent":"",
                    "population.familyMmember":"",    
                    "population.ideaAndsuggest":"", 
                            
                    "population.attentionExtent.id":"",
                    "population.elderPeopleId":"",
                    "population.peopleType.id":"",
                    "population.currentStatus.id:":"",
                    "population.liveStatus.id":"",
                    "population.spouseStatus.id":"",
                    "population.incomeSource.id":"",
                    "population.enterWorkDate":"",
                    "population.retireUnitAndDuty":"",
                    "population.retireDate":"",
                    "population.zhiwu":"",
                    "population.pension":"",                       
                    
                    "population.disabilityReason":"",
                    "population.disabilityDate":"",
                    "population.disabilityType.id":"",
                    "population.disability.id":"",
                    "population.hadDisabilityCard":"",
                    "population.disabilityCardNo":"",
                    "population.skillProfile.id":"",
                    "population.workProfile.id":"",
                    "population.guardianName":"",

                    "population.optimalCardNo":"",
                    "population.optimalCardType.id":"",
                    "population.laborAbility.id":"",
                    "population.abilityLiving.id":"",
                    "population.employmentSituation.id":"",
                    "population.supportSituation.id":"",
                    "population.monthLivingExpenses":"", 
   
                    "population.aidReason.id":"",
                    "population.difficultCardNo":"",
                    "population.difficultType.id":"",
                    "population.subsidiesAmount":"",
                    "population.subsidiesGetTime":"",
                    "population.subsidiesStartTime":"",
                    "population.subsidiesPopulation":"",
                    "population.subsidiesArea":"",
                    }

renYuanObject = {
                    "mode":"",               
                    "population.id":"",                       
                    "population.organization.id":"",
                    "population.actualPopulationType":"",
                    "population.attentionPopulationType":"",
                    "population.imgUrl":"",
                    "population.organization.orgName":"",
                    "population.idCardNo":"", 
                    "population.name":"",
                    "actualPersonType":"",
                    "population.gender.id":"",
                    "population.usedName":"",
                    "population.mobileNumber":"",
                    "population.telephone":"",
                    "population.birthday":"",
                    "population.career.id":"",
                    "population.politicalBackground.id":"",
                    "population.schooling.id":"",
                    "population.nation.id":"",
                    "population.maritalState.id":"",
                    "population.stature":"",
                    "population.bloodType.id":"",
                    "population.faith.id":"",
                    "population.email":"",
                    "population.province":"",
                    "population.city":"",
                    "population.district":"",
                    "population.nativePlaceAddress":"",
                    "population.nativePoliceStation":"",
                    "population.isHaveHouse1":"",
                    "population.noHouseReason":"",
                    "population.houseId":"",
                    "population.currentAddress":"",
                    "population.otherAddress":"",
                    "population.remark":"",   
                    "contextId":"",   
                    "cacheId.id":"",
                    "isSubmit":"", 

                    "population.attentionExtent.id":"",
                    "population.unemployedPeopleType.id":"",
                    "population.registerNumber":"",
                    "population.unemploymentDate":"",
                    "population.unemploymentReason.id":"",
                    "population.upEnterWorkDate":"",
                    "population.originalWorkUnit":"",
                    "population.originalWorkUnitType":"",
                    "population.title":"",
                    "population.technologyLevel.id":"",
                    "population.specialtySkills":"", 
                    "population.participatedPrograms":"",
                            
                    "maritalState":"",
                    "population.attentionExtent.id":"",
                    "population.firstMarriageTime":"",
                    "population.marriageRegistrationTime:":"",
                    "population.marriageOrDivorceTime":"",
                    "population.planningManagement.id":"",
                    "population.remarryTime":"",
                    "population.boyNumber":"",
                    "population.girlNumber":"",
                    "population.singleChildCardno":"",
                    "population.singleChildCDIssueTime":"",
                    "population.onechildOfCouple.id":"",  
                    "population.licenseSituation.id":"",
                    "population.fertilityServicesNo":"",
                    "population.licenseTime":"",
                    "population.certifiedUnit":"",
                    "population.contraceptiveMethod":"",
                    "population.contraceptiveTime":"",
                    "population.maternityCardUnit":"",
                    "population.maternityCardNo":"",
                    "population.maternityCardIssueTime":"",
                    "population.maternityCardValidityTime":"",
                    "population.maternityCardCheckTime":"",
                    "population.maternityCardRemark":"",
                    "population.manIdcardNo":"",
                    "population.manName":"",
                    "population.manMaritalState.id":"",
                    "population.manFirstMarriageTime":"",
                    "population.manMobileNumber":"",
                    "population.manTelephone":"",
                    "population.manBirthday":"",
                    "population.manNation.id":"",
                    "population.manPoliticalBackground.id":"",
                    "population.manSchooling.id":"",
                    "population.manCareer.id":"",
                    "population.manWorkUnit":"",
                    "population.manProvince":"",
                    "population.manCity":"",
                    "population.manDistrict":"",
                    "population.manNativeplaceAddress":"",  
                    "population.manCurrentAddressType.id":"", 
                    "population.manCommunity":"", 
                    "population.manBlock":"", 
                    "population.manUnit":"", 
                    "population.manRoom":"", 
                    "population.manCurrentAddress":"", 
                    "population.manRemark":"",                    
                    
                    "population.abroadDependentsType.id":"",
                    "population.abroadDependents":"",

                    "population.lostEarthDate":"",
                    "population.lostEarthReason.id":"",
                    "population.uncontractingReason.id":"",
                    "population.originalContractEarth":"",
                    "population.lostArea":"",
                    "population.paddyField":"",
                    "population.nowContractEarth":"", 
                    "population.compensationMethod.id":"", 
                    "population.compensationAmount":"", 
                    "population.benefitNumber":"", 
   
                    "population.unemployedDate":"",
                    "population.unemployedNumber":"",
                    "population.lastOccupation":"",
                    "population.lastCompany":"",
                    "population.workState.id":"",
                    "population.skill.id":"",
                    "population.jobIntention":"",
                    "population.monthlyWages":"",
                    "population.endDateOfUnemploymentMoney":"2015-12-05",
                    }

getQiaoShuDict= {
                    "abroadDependent.organization.id":"",
                    "abroadDependent.whetherDeath":"0",
                    "abroadDependent.isEmphasis":"0",
                    "rows":"1000",
                    "page":"1",
                    "sidx":"id",
                    "sord":"desc",            
                    }

deleteQiaoShuDict= { 
                    "ids":""     
                    }

#查询流动人口
kuaiSuSouSuo={
                    'organizationId':'',
                    'searchFloatingPopulationVo.logOut':'0',
                    'searchFloatingPopulationVo.isDeath':'false',
                    'searchFloatingPopulationVo.fastSearchKeyWords':'',
                    '_search':'false',
                    'rows':'200',
                    'page':'1',
                    'sidx':'id',
                    'sord':'desc'             
              }

#服务记录转事件参数
serviceRecordToIssuePara={
                    'issue.isDefault':'true',
                    'issue.id':'',
                    'stepId':'',
                    'issue.occurOrg.id':'',#发生网格id
                    'issue.serialNumber':'',
                    'sourceType':'',#来源方式id
                    'issue.centerLon':'',
                    'issue.centerLat':'',
                    'issue.centerLon2':'',
                    'issue.centerLat2':'',
                    'issue.selfdomIssuetypeOrgCode':'',
                    'issue.sourceKind.id':'',
                    'issue.subject':'',#主题
                    'selectOrgName':'',#网格名称
                    'issue.occurLocation':'',#地点
                    'involvedPlace':'',
                    'issue.occurDate':'',#发生日期
                    'eatHours':'',
                    'eatMinute':'',
                    'issue.hours':'00',
                    'issue.minute':'00',
                    'issueRelatedPeopleNames':'test9iJwIcK-672-householdStaff',#涉及人员
                    'issueRelatedPeopleTelephones':'',
                    'issueRelatedPeopleNames':'',#服务人员姓名
                    'issueRelatedPeopleNameBaks1':'',#服务人员姓名
                    'issueRelatedPeopleTelephones':'',#服务人员手机
                    'selectRelatedPeople':'672-householdStaff-test9iJwIcK-',#拼接
                    'issue.relatePeopleCount':'',#涉及人数
                    'issue.issueKind.id':'',
                    'selectedTypes':'',#事件类型id
                    'issue.issueContent':'',#事件内容
                    'serviceRecordAddIssue.serviceRecordId':''#服务记录id                          
                          }
#获取人员对应的服务记录列表参数
personServiceRecopdListPara={
                    'objectIds':'',#人口id
                    'populationType':'householdStaff',#户籍人口
                    'serviceRecordVo.organization.id':'',
                    'serviceRecordVo.displayYear':'',
                    '_search':'false',
                    'rows':'200',
                    'page':'1',
                    'sidx':'id',
                    'sord':'desc'
                             }