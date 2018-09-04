# -*- coding:UTF-8 -*-
'''
Created on 2015-11-5

@author: lhz
'''

from Web_Test.CONFIG import InitDefaultPara
#安全生产重点新增参数
aqsczdAddPara={
            'enterprise.type.id':'',
            'enterprise.fax':'',
            'placeTypeName':'',
            'ownerOrg.id':'',
            'enterprise.mobileNumber':'',
            'enterprise.name':'',
            'enterprise.hiddenRectification':'',
            'enterprise.enterpriseTelephone':'',
            'enterprise.hiddenCases':'',
            'enterprise.remark':'',
            'enterprise.partyMemberAmount':'',
            'enterprise.keyType':'',
            'enterprise.address':'',
            'enterprise.registeredCapital':'',
            'enterprise.employeeAmount':'',
            'enterprise.telephone':'',
            'enterprise.businessLicense':'',
            'enterprise.riskEnterprise':'',
            'enterprise.legalPerson':'',
            'enterprise.area':'',
            'tqmobile':'true'
              }

#消防安全生产重点,治安重点新增
xfaqscAdd = {
            'tqmobile':'',
            'enterprise.name':'',
            'enterprise.hiddenRectification':'',
            'enterprise.hiddenCases':'',
            'enterprise.remark':'',
            'enterprise.type.id':'',
            'placeTypeName':'',
            'enterprise.keyType':'',
            'enterprise.address':'',
            'ownerOrg.id':'',
            'enterprise.telephone':'',
            'enterprise.mobileNumber':'',
            'enterprise.riskEnterprise':'false',
            'enterprise.legalPerson':'' 
             }
#学校新增,修改参数
schoolParam = {
            'tqmobile':'true',
            'school.id':'', #修改用到
            'school.kind.id':'',
            'school.personLiable':'',
            'school.type.id':'',
            'school.englishName':'',
            'school.fax':'',
            'school.webSite':'',
            'school.president':'',
            'school.personLiableMobileNumber':'',
            'orgId':'',
            'school.atSchoolHeadcount':'',
            'school.attentionExtent.id':'', #修改用到
            'school.personLiableTelephone':'',
            'school.remark':'',
            'school.chineseName':'',
            'school.email':'',
            'school.address':'',
            'school.hasCertificate':'false' 
               }
#学校列表参数
schoolListParam = {
                'tqmobile':'true',
                'orgId':'',
                'sord':'desc',
                'sidx':'id',
                'page':'1',
                'rows':'20' 
                   }

#消防安全生产重点修改参数
xfaqscUpdate = {
            'tqmobile':'true',
            'enterprise.id':'',
            'enterprise.type.id':'',
            'placeTypeName':'',
            'ownerOrg.id':'',
            'enterprise.mobileNumber':'',
            'enterprise.name':'',
            'enterprise.hiddenRectification':'',
            'enterprise.hiddenCases':'',
            'enterprise.remark':'',
            'enterprise.attentionExtent.id':'',
            'enterprise.keyType':'',
            'enterprise.address':'',
            'enterprise.telephone':'',
            'enterprise.riskEnterprise':'',
            'enterprise.legalPerson':'' 
                }

#安全生产重点修改参数
apsczdUpdateParam = {
              'tqmobile':'true',
              'enterprise.id':'',
              'enterprise.industry.id':'',
              'enterprise.type.id':'',
              'enterprise.fax':'',
              'placeTypeName':'',
              'ownerOrg.id':'',
              'enterprise.mobileNumber':'',
              'enterprise.name':'',
              'enterprise.hiddenRectification':'',
              'enterprise.enterpriseTelephone':'',
              'enterprise.hiddenCases':'',
              'enterprise.remark':'',
              'enterprise.partyMemberAmount':'',
              'enterprise.attentionExtent.id':'',
              'enterprise.keyType':'safetyProductionKey',
              'enterprise.address':'',
              'enterprise.registeredCapital':'',
              'enterprise.employeeAmount':'',
              'enterprise.telephone':'',
              'enterprise.businessLicense':'',
              'enterprise.riskEnterprise':'',
              'enterprise.legalPerson':'',
              'enterprise.area':'' #企业
                
                }

#安全生产重点列表查看参数
aqsczdCheck = {
            'name':'',
            'address' :None,
            'legalPerson':None
               }

#安全生产重点查看参数
aqsczdViewCheck = {
              'tqmobile':'true',
              'enterprise.id':'' 
               }
#学校查看参数
schoolCheck = {
              'president':'', 
              'chineseName':'', 
              'address':''
               }
#学校pc列表参数
scoolPClist = {
            'orgId':InitDefaultPara.orgInit['DftWangGeOrgId'],
            'location.isEmphasis':'0',
            'keyType':'',
            'school.chineseName': '',
            'school.kind.id': '',
            'school.type.id': '',
            'school.address': '',
            '_search':'false',
            'rows':'20',
            'page':'1',
            'sidx':'id',
            'sord':'desc' 
               }
#学校pc端检查
schoolCheck = {
             'chineseName':''  
               }
#安全生产重点，消防安全生产重点，安全生产重点列表参数
aqsczdListPara = {
                  'tqmobile':'true',
                  'enterpriseSearchCondition.keyType':'',
                  'sord':'desc',
                  'ownerOrg.id':'',
                  'sidx':'id',
                  'page':'1',
                  'rows':'20'           
                  }


#安全生产重点列表参数
aqsczdListPara1 = {
            'address':'',
            'comprehensiveManageMembers':'',
            'createDate':'',
            'createUser':'',
            'fullPinyin':'',
            'hasServiceTeamMember':'',
            'id':'',
            'isEmphasis':'',
            'keyType':'',
            'lastRecordTime':'',
            'legalPerson':'',
            'locationType':'',
            'name':'',
            'orgInternalCode':'',
            'organization':'',
            'riskEnterprise':'',
            'simplePinyin':'',
            'sourcesState':'',
            'type':'',
            'updateDate':''
                  }
#安全生产重点，消防安全生产重点，安全生产重点列表参数PC端列表查找参数
ChaKanAnQuanShengChanbject ={
                           "orgId":"",
                           "location.isEmphasis":"0",
                           "keyType":"",
                           "rows":"20",
                           "page":"1",
                           "sidx":"id",
                           "sord":"desc"
                           }
#安全生产重点，消防安全生产重点，安全生产重点列表参数pc端检查
ChaKanAnQuanShengChan={
                         "name":None,
                         "organization":None
                         }

#其他场所新增，修改
otherParamAddOrUpdate = {
            'tqmobile':'true',
            'otherLocale.id:':'',
            'otherLocale.type.id':'',
            'otherLocale.contactPerson':'',
            'otherLocale.address':'',
            'otherLocale.telephone':'',
            'otherLocale.mobileNumber':'',
            'otherLocale.name':'',
            'organization.id':'',
            'otherLocale.remark':'' ,  
            'otherLocale.attentionExtent.id':'' #修改
                 }
#其他场所列表
otherParamList = {
            'tqmobile':'true',
            'searchOtherLocaleVo.hasServiceRecord':'-1',
            'sord':'desc',
            'sidx':'id',
            'searchOtherLocaleVo.hasServiceTeamMember':'-1',
            'searchOtherLocaleVo.isEmphasis':'0',
            'page':'1',
            'organization.id':'',
            'rows':'20'     
                  }
#其他场所查看
otherParamView = {
                  'tqmobile':'true',
                  'otherLocale.id':''
                  }
#其他场所新增，修改检查
otherCheck = {
              'address':'',
              'contactPerson':'',
              'name':''
              }
#其他场所pc列表
otherPcParamList = {
                'orgId':'',
                'location.isEmphasis':'0',
                'keyType':'',
                '_search':'false',
                'rows':'20',
                'page':'1',
                'sidx':'id',
                'sord':'desc'  
                    }
#其他场所pc检查
otherPcCheck = {
                'name':''
                }
#组织机构--社会组织 新增，修改
organizationsAddOrUpdate = {
                'tqmobile':'true',
                'newSocietyOrganizations.id':'',#修改
                'newSocietyOrganizations.subType.id':'',
                'newSocietyOrganizations.chargeUnit':'',
                'newSocietyOrganizations.personNum':'',
                'newSocietyOrganizations.mainResponsibilities':'',
                'newSocietyOrganizations.validityStartDate':'',
                'newSocietyOrganizations.introduction':'',
                'newSocietyOrganizations.partyNum':'',
                'newSocietyOrganizations.validityEndDate':'',
                'newSocietyOrganizations.honor':'',
                'newSocietyOrganizations.type.id':'',
                'newSocietyOrganizations.name':'',
                'newSocietyOrganizations.address':'',
                'newSocietyOrganizations.legalPersonTelephone':'',
                'newSocietyOrganizations.legalPersonMobileNumber':'',
                'newSocietyOrganizations.remark':'',
                'newSocietyOrganizations.legalPerson':'',
                'newSocietyOrganizations.registrationNumber':'',
                'organization.id':'',   
                    }
#组织机构--社会组织列表参数
organizationsList = {
                'tqmobile':'true',
                'sord':'desc',
                'organizationId':'',
                'sidx':'id',
                'searchNewSocietyOrganizationsVo.organization.id':'',
                'page':'1',
                'rows':'20'    
                     }

#组织机构--社会组织PC列表参数
organizationsPCList = {
                    'organizationId':InitDefaultPara.orgInit['DftWangGeOrgId'],
                    'location.isEmphasis':'false',
                    '_search':'false',
                    'rows':'20',
                    'page':'1',
                    'sidx':'id',
                    'sord':'desc' 
                       }


#组织机构--社会组织查看
organizationsViewParam = {
                          'tqmobile':'true',
                          'id':''
                          }
#组织机构 ---社会组织列表检查
organizationsListCheck = {
                'name':'' ,
                'legalPerson' :'',
                'address':''
                          }
#组织机构--社会组织 pc列表检查
organizationsListPcCheck = {
                       'name':''     
                            }
#新增巡场情况
xunChangAddParam = {
            'serviceRecord.serviceJoiners':'',
            'serviceRecord_teamId':'',
            'serviceRecord_organization_id':'',
            'serviceRecord.occurDate':'',
            'serviceRecord.recordType':'',
            'serviceRecord_userOrgId':'',
            'serviceRecord.serviceContent':'',
            'mode':'add',
            'serviceRecord_serviceObjects':'',
            'serviceRecord.occurPlace':'',
            'serviceRecord.serviceMembers':'',
            'tqmobile':'true'       
                    }
#巡场情况列表参数
xunChangListParam = {
                    'tqmobile':'true',
                    'objectIds':'',
                    'sord':'desc',
                    'sidx':'id',
                    'serviceRecordVo.organization.id':InitDefaultPara.orgInit['DftWangGeOrgId'],
                    'page':'1',
                    'populationType':'SAFETYPRODUCTIONKEY'
                     }

#巡场情况PC端列表查看参数
xunChangListParamPc = {
                    'objectIds':'',
                    'populationType':'SAFETYPRODUCTIONKEY',
                    'serviceRecordVo.organization.id':InitDefaultPara.orgInit['DftWangGeOrgId'],
                    'serviceRecordVo.displayYear':'',
                    '_search':'false',
                    'rows':'20',
                    'page':'1',
                    'sidx':'id',
                    'sord':'desc'
                       }

#巡场情况列表检查
xunChangCheckParam = {
                      'occurPlace':'',
                      'occurDate':'',
                      'serviceMembers':''
                      }

#重点场所--学校 查看参数
schoolLookParam = {
                   'tqmobile':'true',
                   'Id':''
                   }



#列表和查询（安全生产重点，消防安全重点，治安重点，规上企业）接口一样以安全生产重点为例
searchListParam = {
            'tqmobile':'true',
            'enterpriseSearchCondition.keyType':'safetyProductionKey',
            'sord':'desc',
            'enterpriseSearchCondition.name':'',
            'enterpriseSearchCondition.isEmphasis':'',
            'page':'1',
            'enterpriseSearchCondition.legalPerson':'',
            'ownerOrg.id':InitDefaultPara.orgInit['DftWangGeOrgId'],
            'sidx':'id',
            'rows':'20'         
                   }

#列表和查询字段（安全生产重点，消防安全重点，治安重点，规上企业）接口一样以安全生产重点为例
searchParam = {
            'enterpriseSearchCondition.name':'',
            'enterpriseSearchCondition.isEmphasis':''               
               }

#组织机构-社会组织高级搜索
searchZZcsListParam = {
                'tqmobile':'true',
                'sord':'desc',
                'searchNewSocietyOrganizationsVo.organization.id':InitDefaultPara.orgInit['DftWangGeOrgId'],
                'page':'1',
                'searchNewSocietyOrganizationsVo.unitName':'',
                'organizationId':InitDefaultPara.orgInit['DftWangGeOrgId'],
                'sidx':'id',
                'searchNewSocietyOrganizationsVo.legalPerson':'',
                'rows':'20'
                   }

#组织机构-社会组织列表查询字段
searchZZcsParam = {
                  'searchNewSocietyOrganizationsVo.unitName':'' 
                   
                   }
#重点场所--其他场所 列表字段
otherSearchListParam = {
                    'tqmobile':'true',
                    'sord':'desc',
                    'searchDangerousChemicalsUnitVo.hasServiceTeamMember':'-1',
                    'page':'1',
                    'searchDangerousChemicalsUnitVo.hasServiceRecord':'-1',
                    'searchOtherLocaleVo.contactPerson':'',
                    'searchOtherLocaleVo.name':'',
                    'sidx':'id',
                    'organization.id':InitDefaultPara.orgInit['DftWangGeOrgId'],
                    'rows':'20'     
                        }

#重点场所--其他场所 列表查询字段
searchOtherParam = {
                 'searchOtherLocaleVo.name':''   
                    }

#重点场所--学校列表字段
schoolSearchListParam = {
                     'tqmobile':'true',
                    'orgId':InitDefaultPara.orgInit['DftWangGeOrgId'],
                    'sord':'desc',
                    'sidx':'id',
                    'location.address':'',
                    'page':'1',
                    'location.president':'',
                    'rows':'20'
                         }


#重点场所--学校列表查询字段
schoolSearchParam = {
             'location.president':''       
                     }




