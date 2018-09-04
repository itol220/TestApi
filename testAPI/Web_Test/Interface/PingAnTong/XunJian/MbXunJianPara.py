# -*- coding:UTF-8 -*-
'''
Created on 2016-3-24

@author: lhz
'''
#新增企业信息参数
addCompanyParam = {
            'tqmobile':'true',
            'safeProductionEnterprise.address':'',
            'safeProductionEnterprise.employeeAmount':'',
            'safeProductionEnterprise.legalPerson':'',
            'safeProductionEnterprise.type.id':'',
            'safeProductionEnterprise.isEmphasis':'',
            'safeProductionEnterprise.name':'',
            'safeProductionEnterprise.businessLicense':'',
            'safeProductionEnterprise.gridPerson':'',
            'safeProductionEnterprise.landlordName':'',
            'ownerOrg.id':'',
            'safeProductionEnterprise.mobileNumber':'',
            'safeProductionEnterprise.landlordMobile':''      
                   }

#修改企业信息参数
updateCompanyParam = {
                'tqmobile':'true',
                'safeProductionEnterprise.address':'',
                'safeProductionEnterprise.employeeAmount':'',
                'safeProductionEnterprise.type.id':'',
                'safeProductionEnterprise.isEmphasis':'',
                'ownerOrg.id':'',
                'safeProductionEnterprise.safeProductiontype.id':'',
                'safeProductionEnterprise.legalPerson':'',
                'safeProductionEnterprise.name':'',
                'safeProductionEnterprise.businessLicense':'',
                'safeProductionEnterprise.gridPerson':'',
                'safeProductionEnterprise.landlordName':'',
                'safeProductionEnterprise.id':'',
                'safeProductionEnterprise.mobileNumber':'',
                'safeProductionEnterprise.landlordMobile':''        
                      }

#企业信息列表参数
companyListParam = {
                'tqmobile':'true',
                'orgId':'',
                'sord':'desc',
                'sidx':'id',
                'page':'1',
                'rows':'20'     
              }
#企业信息列表检查点
addOrEditCheck = {
           'name':'' 
            }
#Pc端企业信息列表查询参数
companyListPcParam = {
                    'orgId':'',
                    '_search':'false',
                    'rows':'20',
                    'page':'1',
                    'sidx':'id',
                    'sord':'desc'  
                     }
#新增巡检记录
addXunJianRecord = {
                'inspection.remark':'',
                'inspection.inspectAddress':'',
                'inspection.limitTime':'',
                'inspection.lat':'',#纬度 (会自动获取)
                'inspectionRecord.recordType':'',
                'inspection.inspectResult':'',
                'inspection.inspectTime':'',
                'inspection.inspectUserId':'',
                'inspection.orgId':'',
                'riskRemarkIds':'',
                'inspection.lng':'', #经度(会自动获取)
                'inspectionRecord.enterprise.id':'',
                'inspection.inspectMobileAddr':'',#(会定位地址)
                'inspection.inspectName':'',
                'tqmobile':'true',
                'android_appversion':'2.0.1'    
                    }
#检查巡检记录
check_record = {
                'tqmobile':'true',
                'inspectionRecordVo.recordType':'',
                'sord':'desc',
                'sidx':'id',
                'inspectionRecordVo.enterpriseId':'',
                'inspectionRecordVo.orgId':'',
                'mode':'inspectionRecord'
                }
#巡检记录地址
recordAdress = {
                'address':''
                } 

#新增复查记录
reCheck = {
            'inspection.inspectResult':'',
            'solveIds':'',
            'inspection.inspectTime':'',
            'inspection.inspectUserId':'',
            'inspection.inspectAddress':'',
            'inspection.lat':'',
            'inspection.orgId':'',
            'inspection.lng':'',
            'inspectionRecord.enterprise.id':'',
            'inspection.inspectMobileAddr':'',
            'inspectionRecord.recordType':'',
            'inspection.inspectName':'',
            'inspection.id':'',
            'tqmobile':'true',
            'android_appversion':'2.0.1'
           }
#检查复查记录
check_reCheck = {
                'tqmobile':'true',
                'recordType':'',
                'enterpriseId':'',
                'inspectionId':'' 
                 }
#高级搜索
searchParam = {
               'tqmobile':'true',
                'safeProductionEnterprise.address':'',
                'orgId':'',
                'sord':'desc',
                'page':'1',
                'safeProductionEnterprise.isEmphasis':'false',
                'safeProductionEnterprise.fastSearchKeyWords':'',
                'safeProductionEnterprise.businessLicense':'',
                'safeProductionEnterprise.gridPerson':'',
                'sidx':'id',
                'rows':'20'
               }
#高级搜索检查参数
checkSearchParam = {
                    'name':'',
                    'address':''
                  }

