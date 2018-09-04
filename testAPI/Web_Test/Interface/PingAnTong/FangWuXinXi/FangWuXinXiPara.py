# -*- coding:UTF-8 -*-
'''
Created on 2016-3-8

@author: chanyan
'''


#房屋信息
fangWuObject = {
                    "tqmobile":"",
                   #房屋信息 
                    "houseInfo.organization.id":"",
                    "houseInfo.address":"",
                    "houseInfo.addressType.id":"",
                    "houseInfo.id":"",
                   
                    "houseInfo.isRentalHouse":"",
                    "houseInfo.buildingName":"",
                    "houseInfo.propertyName":"",
                    "houseInfo.houseOwner":"",
                    "houseInfo.buildingUses.id":"",
                    "houseInfo.houseOwnerIdCardNo":"",
                    "houseInfo.telephone":"",
                    "houseInfo.houseDoorModel":"",
                    "houseInfo.builtYear":"",
                    "houseInfo.houseArea":"",
                    "houseInfo.houseStructure.id":"",
                    "houseInfo.houseUses.id":"",
                    "houseInfo.ownProperty.id":"",
                    "houseInfo.housingVouchers.id":"",
                    "houseInfo.houseRightNumber":"",
                    "houseInfo.houseRightNumberDate":"",
                   #土地信息 
                    "houseInfo.landDocuments.id":"",
                    "houseInfo.landRightsNumbe":"",
                    "houseInfo.landRightsNumbeDate":"",
                    "houseInfo.propertyTypes.id":"",
                    "houseInfo.name":"",
                    "houseInfo.certificateType.id":"",
                    "houseInfo.certificateNumbe":"",
                    "houseInfo.propertyPersonTel":"",
                    "houseInfo.propertyPersonMobile":"",
                    "houseInfo.remark":"",
                   #出租信息 
                    "houseInfo.rentalPerson":"",
                    "houseInfo.rentalType.id":"",
                    "houseInfo.hiddenDangerLevel.id":"",
                    "houseInfo.houseFileNum":"",
                    "houseInfo.usage.id":"",
                    "houseInfo.lessorType.id":"",
                    "houseInfo.registDate":"",
                    "houseInfo.lessorDate":"",
                    "houseInfo.rentalHouseProperty.id":"",
                    "houseInfo.mangerTypes.id":"",
                    "houseInfo.rentalCertificateType.id":"",
                    "houseInfo.rentalCertificateNumbe":"",
                    "houseInfo.rentalTelephone":"",
                    "houseInfo.rentalMobileNumber":"",
                    "houseInfo.lessorAddress":"",
                    "houseInfo.roomNumber":"",
                    "houseInfo.limitPersons":"",
                    "houseInfo.rentMonth":"",
                    "houseInfo.hiddenRectification":"",
                    }

getHouseDict= {
                 "tqmobile":"true",
                 "orgId":"",
                 "rows":"1000",
                 "page":"1",
                 "sidx":"id",
                 "sord":"desc",     
                 }

getFangWuDict= {
                 "tqmobile":"true",
                 "houseInfo.id":"",
                 }

checkFangWuDict={
                 "address":None,
                "id":None,
                 }

searchHouseDict= {
                 "tqmobile":"true",
                 "orgId":"",
                 "rows":"1000",
                 "page":"1",
                 "sidx":"id",
                 "sord":"desc",     
                 "searchHouseInfoVo.houseCode":"",
                 "searchHouseInfoVo.address":""       
                 }

zhuHuDict={
            "tqmobile":"true",
            "houseHasActualPopulation.houseId":"",
            "Tenements":"",
             }

getzhuHuDict= {
                 "tqmobile":"true",
                 "orgId":"",
                 "houseId":"",
                 "rows":"1000",
                 "page":"1",
                 "sidx":"id",
                 "sord":"desc",     
                 }

checkFangWuDict={
                 "address":None,
                 "id":None,
                 }