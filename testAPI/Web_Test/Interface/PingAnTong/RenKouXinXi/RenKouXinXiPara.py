# -*- coding:UTF-8 -*-
'''
Created on 2016-1-28

@author: chenyan
'''

#户籍人口
populationObject = {
                #均为必填项     
                    "tqmobile":"",
                    "orgId":"",
                    "householdStaff.id":"",
                #个人信息
                    "householdStaff.name":"",               
                    "householdStaff.organization.id":"",
                    "householdStaff.idCardNo":"",
                    "householdStaff.gender.id":"",  #性别为必填项，根据身份证自动获取
                    "householdStaff.maritalState.id:":"",                         
                    "householdStaff.schooling.id":"",
                    "householdStaff.politicalBackground.id":"",
                    "householdStaff.nation.id":"",
                    "householdStaff.houseAddress":"",
                    "householdStaff.province":"",
                    "householdStaff.city":"",
                    "householdStaff.district":"",
                    "householdStaff.isHaveHouse":"",
                    "householdStaff.currentAddress":"",
                    "householdStaff.noHouseReason":"", 
                    
                    "householdStaff.usedName":"",
                    "householdStaff.nativePlaceAddress":"",
                    "householdStaff.otherAddress":"",
                    "householdStaff.nativePoliceStation":"",
                    "householdStaff.mobileNumber":"",
                    "householdStaff.telephone":"",
                    "householdStaff.email":"",
                    "householdStaff.career.id":"",
                    "householdStaff.workUnit":"",
                    "householdStaff.stature":"",
                    "householdStaff.bloodType.id":"",
                    "householdStaff.faith.id":"",
                    "householdStaff.remark":"",
                #户籍信息                    
                    "householdStaff.accountNumber":"",               
                    "householdStaff.relationShipWithHead.id":"",
                    "householdStaff.residentStatus.id":"",
                    
                    "householdStaff.homePhone":"",
                    "householdStaff.outGone":"",     #是否外出（非必填项）：是（需填外出原因、时间） ，否（不必填）                    
                    "householdStaff.outReasons.id":"",   #以下是外出时所需填的项目
                    "householdStaff.reasonsDate":"",
                    "householdStaff.outProvince":"",
                    "householdStaff.outCity":"",
                    "householdStaff.outDistrict":"",
                    "householdStaff.goOutDetailedAddress":"",
                #住房信息    -前提：个人信息中选择有住房信息，才会出现该字段                
                    "houseInfo.address":"",      
                    
                    "houseInfo.houseUses.id":"",
                    "houseInfo.propertyTypes.id":"",
                    "houseInfo.name":"",
                    "houseInfo.certificateType.id":"",
                    "houseInfo.certificateNumbe":"",
                    "houseInfo.propertyPersonMobile":"",
                    "houseInfo.propertyPersonTel":"",
                    "houseInfo.isRentalHouse":"",    #是否为出租房
                    "houseInfo.remark":"",
                    "houseInfo.rentalHouse.rentalType.id":"",   #以下为出租房时所需填写的字段
                    "houseInfo.rentalHouse.hiddenDangerLevel.id":"",
                    "houseInfo.rentalHouse.rentalPerson":"",
                    "houseInfo.rentalHouse.usage.id":"",
                    "houseInfo.rentalHouse.rentalHouseProperty.id":"",
                    "houseInfo.rentalHouse.rentalTelephone":"",
                    "houseInfo.rentalHouse.rentalMobileNumber":"",
                    "houseInfo.rentalHouse.lessorAddress":""
                    }

editPopulationObject = {
                        "householdStaff.id":"",
#                         "houseInfo.organization.id":"",
#                         "householdStaff.isDeath":"",
#                         "population.actualPopulationType":"",
#                         "householdStaff.organization.orgName":"",
#                         "householdStaff.death":"",
#                         "householdStaff.age":"",
#                         "householdStaff.uuid":"",
#                         "householdStaff.orgInternalCode":"",
#                         "householdStaff.actualPopulationType":"",
#                         "householdStaff.simplePinyin":"",
#                         "householdStaff.fullPinyin":"",
#                         "householdStaff.serialVersionUID":"",
                #均为必填项     
                        "tqmobile":"",
                        "orgId":"",
                #个人信息
                        "householdStaff.name":"",               
                        "householdStaff.organization.id":"",
                        "householdStaff.idCardNo":"",
                        "householdStaff.gender.id":"",  #性别为必填项，根据身份证自动获取
                        "householdStaff.maritalState.id:":"",                         
                        "householdStaff.schooling.id":"",
                        "householdStaff.politicalBackground.id":"",
                        "householdStaff.nation.id":"",
                    "householdStaff.houseAddress":"",
                        "householdStaff.province":"",
                        "householdStaff.city":"",
                        "householdStaff.district":"",
                        "householdStaff.isHaveHouse":"",
                    "householdStaff.currentAddress":"",
                        "householdStaff.noHouseReason":"", 
                    
                        "householdStaff.outGone":"",     #是否外出（非必填项）：是（需填外出原因、时间） ，否（不必填）                    
                    }

getHuJiDict = {
               "tqmobile":"true",
               "population.id":""
               }

getOrgDict = {
                  "tqmobile":"true",
                  "orgId":"",
                  "searchRectificativePersonVo.isDeath":"0",
                  "searchRectificativePersonVo.logOut":"0",
                  "searchRectificativePersonVo.isEmphasis":"0",
                  "populationType":"",  #户籍人口：RESIDENT 流动人口：TRAMPRESIDENT 境外人口：OVERSEAPERSONNEL 刑释人员：POSITIVEINFO 矫正人员：RECTIFICATIVEPERSON 精神病人员：MENTALPATIENT 吸毒：DRUGGY 重点青少年：IDLEYOUTH 重点上访人员：SUPERIORVISIT 危险品从业人员：DANGEROUSGOODSPRACTITIONER 
                  "rows":"1000",
                  "page":"1",
                  "sidx":"id",
                  "sord":"desc"
                  }

checkPopulationDict = {
                        "idCardNo":None
                       }

#流动人口
liuDongObject = {
                #均为必填项     
                    "tqmobile":"",
                    "orgId":"",
                    "houseInfo.organization.id":"",
                    "floatingPopulation.id":"",
                #个人信息
                    "floatingPopulation.name":"",               
                    "floatingPopulation.organization.id":"",
                    "floatingPopulation.idCardNo":"",
                    "floatingPopulation.gender.id":"",
                    "floatingPopulation.maritalState.id":"",                         
                    "floatingPopulation.schooling.id":"",
                    "floatingPopulation.politicalBackground.id":"",
                    "floatingPopulation.nation.id":"",
                    "floatingPopulation.houseAddress":"",
                    "floatingPopulation.province":"",
                    "floatingPopulation.city":"",
                    "floatingPopulation.district":"",
                    "floatingPopulation.isHaveHouse":"",
                    "floatingPopulation.currentAddress":"",
                    "floatingPopulation.noHouseReason":"", 
                    
                    "floatingPopulation.usedName":"",
                    "floatingPopulation.nativePlaceAddress":"",
                    "floatingPopulation.otherAddress":"",
                    "floatingPopulation.nativePoliceStation":"",
                    "floatingPopulation.mobileNumber":"",
                    "floatingPopulation.telephone":"",
                    "floatingPopulation.email":"",
                    "floatingPopulation.career.id":"",
                    "floatingPopulation.workUnit":"",
                    "floatingPopulation.stature":"",
                    "floatingPopulation.bloodType.id":"",
                    "floatingPopulation.faith.id":"",
                    "floatingPopulation.remark":"",
                #流入人口信息                    
                    "floatingPopulation.inflowingReason.id":"",               
                    "floatingPopulation.inflowingDate":"",
                    "floatingPopulation.expectedDatedue":"",
                    "floatingPopulation.stayLocationType.id:":"",    

                    "floatingPopulation.inflowingProvince":"",
                    "floatingPopulation.inflowingCity":"",
                    "floatingPopulation.inflowingDistrict":"",
                    "floatingPopulation.registerDate":"",
                    "floatingPopulation.registrationType.id":"",
                    "floatingPopulation.economySource.id":"",
                    "floatingPopulation.stayTimeLimit.id":"",
                    "floatingPopulation.preparedStayTimeLimit.id":"",
                    "floatingPopulation.hasMarriedProve":"",
                #住房信息    -前提：个人信息中选择有住房信息，才会出现该字段                
                    "houseInfo.address":"",               
                    }

#境外人口
jingWaiObject = {
                #均为必填项     
                    "tqmobile":"",
                    "orgId":"",
                    "overseaPersonnel.id":"",
                #个人信息
                    "overseaPersonnel.name":"",               
                    "overseaPersonnel.organization.id":"",
                    "overseaPersonnel.englishName":"",
                    "overseaPersonnel.gender.id":"",                         
                    "overseaPersonnel.certificateType.id":"",
                    "overseaPersonnel.certificateNo":"",
                    "overseaPersonnel.isHaveHouse":"",
                    "overseaPersonnel.currentAddress":"",
                    "overseaPersonnel.noHouseReason":"",
                    
                    "overseaPersonnel.birthday":"",
                    "overseaPersonnel.profession.id":"",
                    "overseaPersonnel.nationality":"",
                    "overseaPersonnel.inflowReason":"",
                    "overseaPersonnel.arrivalTime":"", 
                    "overseaPersonnel.leaveTime":"",
                    "overseaPersonnel.remark":"",
                #住房信息    -前提：个人信息中选择有住房信息，才会出现该字段                
                    "houseInfo.address":"",               
                    }

getJingWaiDict = {
                   "tqmobile":"true",
                   "overseaPersonnel.id":""
                   }

checkJingWaiDict = {
                    "certificateNo":None
                    }

searchOrgDict = {
                  "tqmobile":"true",
                  "orgId":"",
                  "householdStaffVo.isDeath":"0",
                  "householdStaffVo.logout":"0",
                  "populationType":"",  #户籍人口：RESIDENT  流动人口：TRAMPRESIDENT  境外人口：OVERSEAPERSONNEL
                  "searchCondition.name":"",
                  "searchCondition.idCardNo":"",
                  "rows":"1000",
                  "page":"1",
                  "sidx":"id",
                  "sord":"desc"
                  }

searchDict = {
              "name":None,
              "idCardNo":None
              }


serviceRecordObject = {
                    #均为必填项     
                        "tqmobile":"",
                        'serviceRecord.id':"",
                    #个人信息
                        "serviceRecord.userOrgId":"",               
                        "serviceRecord.serviceJoiners":"", #选填项
                        "serviceRecord.teamId":"",
                        "serviceRecord.occurDate":"",                         
                        "serviceRecord.serviceObjects":"",
                        "serviceRecord.organization.id":"",
                        "serviceRecord.serviceContent":"",  #选填项
                        "serviceRecord.serviceMembers":"",
                        "serviceRecord.occurPlace":"",
                        }

getServiceRecordDict = {
                      "tqmobile":"true",
                      "objectIds":"",
                      "serviceRecordVo.organization.id":"",
                      "serviceRecordVo.displayLevel":"sameGrade",
                      "populationType":"",  #户籍人口：householdStaff  流动人口：TRAMPRESIDENT  境外人口：OVERSEAPERSONNEL
                      "rows":"1000",
                      "page":"1",
                      "sidx":"id",
                      "sord":"desc"
                      }

deleteServiceRecordDict = {
                           "tqmobile":"true",
                           "recordIds":"",
                           }

checkServiceRecordDict = {
                          "serviceMembers":None,
                          "serviceObjects":None
                          }



getRecordDict = {
                   "tqmobile":"true",
                   "serviceRecord.id":""
                   }


#特殊人群
teShuRenQunObject = {
                #均为必填项     
                    "tqmobile":"",
                    "orgId":"",
                    "population.id":"",
                    "population.actualPopulationType":"",   #户籍人口：householdStaff  流动人口：floatingPopulation
                    "population.attentionPopulationType":"",    #刑释：positiveInfo 矫正：rectificativePerson 精神病人员：mentalPatient 吸毒人员 ：druggy 重点青少年：idleYouth 重点上访：superiorVisits 危险品从业人员：dangerousGoodsPractitioner
                #个人信息
                    "population.name":"",               
                    "population.organization.id":"",
                    "population.idCardNo":"",
                    "population.gender.id":"",  #性别为必填项，根据身份证自动获取
                    "population.maritalState.id:":"",                         
                    "population.schooling.id":"",
                    "population.politicalBackground.id":"",
                    "population.nation.id":"",
                    "population.houseAddress":"",
                    "population.province":"",
                    "population.city":"",
                    "population.district":"",
                    "population.isHaveHouse":"",
                    "population.currentAddress":"",
                    "population.noHouseReason":"", 
                    
                #刑释信息
                    "population.positiveInfoType.id":"",
                    "population.caseReason":"",
                    "population.imprisonmentDate":"",
                    "population.laborEduAddress":"",
                    "population.releaseOrBackDate":"",
                    
                    "population.attentionExtent.id":"",
                    "population.criminalBehavior":"",
                    "population.agoProfession.id":"",
                    "population.isRepeat":"",
                    "population.isCrime":"",
                    "population.crimeDate":"",
                    "population.resettlementDate":"",
                    "population.noResettlementReason":"",
                    
                #矫正信息
                    "population.accusation":"",
                    "population.executeType.id":"",
                    "population.rectifyStartDate":"",
                    "population.rectifyEndDate":"",
                    
                    "population.attentionExtent.id":"",
                    "population.penaltyTerm":"",
                    "population.recentSituation":"",
                    
                #精神病人员信息
                    "population.dangerLevel.id":"",
                    
                    "population.psychosisName":"",
                    "population.treat":"",
                    "population.cureDepartment":"",
                    
                #吸毒人员信息
                    "population.detoxicateCase.id":"",
                    
                    "population.attentionExtent.id":"",
                    "population.detoxicateCondition.id":"",
                    "population.drugSource.id":"",
                    "population.drugReason.id":"",
                    "population.ferretOutDate":"",
                    "population.drugFristDate":"",
                    "population.controlActuality":"",
                    "population.drugType":"",
                    "population.adanon":"",

                #重点青少年信息
                    "population.staffTypeUpdateIds":"",
                    
                    "population.attentionExtent.id":"",
                    "population.workCondition":"",
                    
                #重点上访人员
                    "population.visitReason":"",
                    
                    "population.attentionExtent.id":"",
                    "population.visitType":"",
                    "population.visitState.id":"",

                #危险品从业人员
                    "population.dangerousWorkingType.id":"",
                    "population.legalPerson":"",
                    "population.legalPersonMobileNumber":"",
                    "population.legalPersonTelephone":"",
                    "population.workUnit":"",
                    
                    "population.attentionExtent.id":"",
                    "population.workingCertificate":"",
                    "population.workingCertificateNo":"",
                    "population.periodOfValidityStart":"",
                    "population.periodOfValidityEnd":""

                    }

