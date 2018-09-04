'''
Created on 2015-12-8

@author: chenyan
'''
import time

houseObject = {
               "dailogName":"",
               "houseInfo.imgUrl":"",
               "houseInfo.organization.id":"",
               "mode":"",               
               "houseInfo.id":"",
               "isUseFrom":"",
               "isSubmit:":"",                         
               "houseInfo.organization.orgName":"",
               "houseInfo.addressType.id":"", 
               "currentAddressType":"",
               "houseInfo.community":"",
               "houseInfo.block:":"",
               "houseInfo.unit":"",
               "houseInfo.room":"",
               "houseInfo.address":"",
               "houseInfo.standardAddressCode":"",
               "houseInfo.buildingName":"",
               "houseInfo.buildingUses.id":"",
               "houseInfo.propertyName":"",
               "houseInfo.houseOwner":"",
               "houseInfo.houseOwnerIdCardNo":"",
               "houseInfo.telephone":"",
               "houseInfo.houseDoorModel":"",
               "houseInfo.builtYear":"",
               "houseInfo.houseArea":"",
               "houseInfo.houseStructure.id":"",
               "houseInfo.houseUses.id":"",
               "houseInfo.houseSource.id":"",
               "houseInfo.rentalBuildings.id":"",
               "houseInfo.housingVouchers.id":"",
               "houseInfo.houseRightNumber":"",
               "houseInfo.houseRightNumberDate":"",
               "houseInfo.landDocuments.id":"",
               "houseInfo.landRightsNumbe":"",
               "houseInfo.landRightsNumbeDate":"",
               "houseInfo.propertyTypes.id":"",
               "phouseInfo.name":"",
               "phouseInfo.certificateType.id":"",
               "phouseInfo.certificateNumbe":"",
               "phouseInfo.propertyPersonTel":"",
               "phouseInfo.propertyPersonMobile":"",
               "phouseInfo.remark":"",
               "houseInfo.isRentalHouse":"",                                      
               }

getFangWuDict= {
                 "orgId":"",
                 "rows":"1000",
                 "page":"1",
                 "sidx":"id",
                 "sord":"desc",            
                 }

FangWuDict={
            "houseIds":'',
            "houseInfo.isEmphasis":'',
            "houseInfo.logOutTime":'',
            "houseInfo.logOutReason":'',
            }

checkFangWuDict={
                 "address":None,
                 "id":None,
                 }

deleteFangWuDict={
                 "houseIds":"",
                 }

data = {
        'dataType':'',
        'templates':'',
        'startRow':'4',
        'enterpriseType':'',
        'isNew':'1',
        'reportTime':'',
        'yearDate':''
        }

dlData = {
          'orgId':"",
          '_search':'false',
          'rows':'200',
          'page':'1',
          'sidx':'id',
          'sord':'desc',
          'pageOnly':'false'
          }

zhuHuDict={
              "houseHasActualPopulation.houseId":"",
              "houseHasActualPopulation.populationId":"",
              "houseHasActualPopulation.populationType":"",
              }

checkZhuHuDict={
                 "certificateNumber":None,
                 "personName":None,
                 }

getZhuHuDict= {
                 "houseId":"",
                 "rows":"1000",
                 "page":"1",
                 "sidx":"id",
                 "sord":"desc",            
                 }

transferFangWuDict= {
                     "orgId":"",
                     "toOrgId":"",
                     "ids":"",
                     "type":"",
                     "isTransfer":"",            
                     }



rentalObject = {
               "houseInfo.organization.id":"",
               "houseInfo.houseCode":"",
               "houseInfo.houseId":"",
               "houseInfo.imgUrl":"",
               "houseInfo.orgInternalCode":"",
               "dailogName":"",
               "mode":"",   
               "contextId":"",           
               "houseInfo.id":"",
               "houseInfo.isEmphasis":"",
               "isSubmit:":"",                         
               "cacheId.houseInfoId":"",
               "houseInfo.usage.id":"", 
               "houseInfo.houseFileNum":"",
               "houseInfo.lessorType.id":"",
               "houseInfo.rentalPerson:":"",
               "houseInfo.rentalCertificateType.id":"",
               "houseInfo.rentalCertificateNumbe":"",
               "houseInfo.rentalTelephone":"",
               "houseInfo.rentalMobileNumber":"",
               "houseInfo.lessorAddress":"",
               "houseInfo.rentalType.id":"",
               "houseInfo.rentalHouseProperty.id":"",
               "houseInfo.hiddenDangerLevel.id":"",
               "houseInfo.mangerTypes.id":"",
               "houseInfo.registDate":"",
               "houseInfo.lessorDate":"",
               "houseInfo.roomNumber":"",
               "houseInfo.limitPersons":"",
               "houseInfo.realityPersons":"",
               "houseInfo.rentMonth":"",
               "houseInfo.hiddenRectification":"",                                    
               }

getChuZuDict= {
               "searchMode":"noFast_noAdvanced_search",
               "orgId":"",
               "searchHouseInfoVo.isEmphasis":"0",
               "rows":"1000",
               "page":"1",
               "sidx":"id",
               "sord":"desc",            
               }

addFuZeRenDict={
                "serviceMemberWithObject.memberId":"",
                "serviceMemberWithObject.objectType":"",
                "serviceMemberWithObject.objectName":"",
                "serviceMemberWithObject.objectId":"",
                "serviceMemberWithObject.teamMember":"",
                "serviceMemberWithObject.onDuty":"",
                "serviceMemberWithObject.teamId":"",
                "serviceMemberWithObject.objectLogout":"",
                }

getFuZeRenDict={
                "serviceMemberVo.objectType":'RENTALHOUSE',
                "serviceMemberVo.objectId":'',
                "serviceMemberVo.onDuty":'',
                "serviceMemberVo.objectName":'',
                "_search":"false",
                "rows":'200',
                "page":'1',
                "sidx":'id',
                "sord":'desc',  
                }

checkFuZeRenDict={
                  "id":None,
                  "memberId":None,
                  "memberName":None,
                  }

deleteFuZeRenDict={
                   "selectedIds":"",
                   }

leaveFuZeRenDict={
                   "serviceMemberWithObject.id":"",
                   "serviceMemberWithObject.onDuty":"",
                   "serviceMemberWithObject.memberId":""
                   }

serviceRecordObject={
                     "mode":'',
                     "serviceRecord.userOrgId":'',
                     "serviceRecord.organization.id":'',
                     "serviceRecord.id":'',
                     "serviceRecord.teamId":'',
                     "isSubmit":'',
                     "serviceRecord.occurDate":'',
                     "serviceRecord.occurPlace":'',  
                     "serviceRecord.serviceMembers":'',
                     "serviceRecord.serviceJoiners":'',
                     "serviceRecord.recordType":'',
                     "serviceRecord.serviceObjects":'',
                     "serviceRecord.serviceContent":'',
                     }

getRecordDict={
                "objectIds":'',
                "populationType":'RENTALHOUSE',
                "serviceRecordVo.organization.id":'',
                "serviceRecordVo.displayYear":time.strftime("%Y"),  
                "_search":"false",
                "rows":'200',
                "page":'1',
                "sidx":'id',
                "sord":'desc',  
                }

deleteRecordDict={
                 "mode":"",
                 "recordIds":""
                 }

checkRecordDict={
                 "id":None,
                 "serviceObjects":None,
                 }

recordTypeDict={
                "paiChaLei":"0",
                "zhengGaiLei":"1"
                }

