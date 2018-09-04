# -*- coding:UTF-8 -*-
'''
Created on 2015-12-22

@author: lhz
'''
#编辑辖区管理信息
import time
xiaQuGuanLiEdit = {
                   'villageProfile.id':None,
                   'villageProfile.organization.id':None,
                   'villageProfile.introduction':'' ,
                   'mode':''                
                   }
#辖区管理检查点
xiaQuGuanLiEdit_check = {
                         'introduction':''
                         }
#辖区管理列表查询
xiaQuGuanLiSearch = {
                     'organization.id':None,
                     'mode':''
                     }
#辖区管理图片上传
imageUpload = {
                 'upload':None,
                 'villageProfile.id':None,
                 'villageProfile.organization.id':''
               }

#辖区领导班子内容编辑
xiaQuGuanLiLeader = {
                     'mode':'',
                     'leaderTeams.id':'',
                     'leaderTeams.organization.orgInternalCode':'',
                     'leaderTeams.organization.id':'',
                     'leaderTeams.imageUrl':'',
                     'leaderTeams.name':'',
                     'leaderTeams.gender':'',
                     'leaderTeams.duty':'',
                     'leaderTeams.contact':'',
                     'leaderTeams.introduction':''        
                     }
#辖区领导班子删除
xiaQuGuanLiDel = {
                  'leaderTeams.id' :''
                  }

#辖区队伍列表
xiaQuDuiWuListParam = {
                       'leaderTeamsVo.organization.id':'',
                        'leaderTeamsVo.displayLevel':'allJurisdiction',
                        'leaderTeamsVo.orgLevel':'',
                        '_search':'false',
                        'rows':'20',
                        'page':'100',
                        'sidx':'id',
                        'sord':'desc'
                       }

#编辑基础信息
baseInformation = {
                    'villageProfile.id':'',
                    'villageProfile.organization.id':'',
                    'villageProfile.gridNum':'',
                    'villageProfile.acreage':'',
                    'villageProfile.doors':'',
                    'villageProfile.villagers':'',
                    'villageProfile.villageRingsters':'',
                    'villageProfile.villageDelegate':'',
                    'villageProfile.interzoneLeading':'',
                    'villageProfile.villageBuildupSecretary':'',
                    'villageProfile.buildupSecretaryPhone':'',
                    'villageProfile.villageDirector':'',
                    'villageProfile.villageDirectorPhone':'',
                    'villageProfile.informationPersonA':'',
                    'villageProfile.informationPersonAPhone':''
                   }


#组织机构--综治组织  新增/修改
oragnizationAddParam = {
                'mode':'',
                'primaryOrg.id':'',
                'primaryOrg.org.id':'',
                'isSubmit':'',
                'appendMember':'',
                'primaryOrg.teamClass.id':'',
                'primaryOrg.org.orgName':'',
                'primaryOrg.teamType.id':'',
                'primaryOrg.name':'',
                'primaryOrg.detailName':'',
                'primaryOrg.remark':''       
                        }

#组织机构--综治组织   检查点
oragnizationAddParam_check = {
                              'detailName':''
                              }


#组织机构--综治组织 列表
oragnizationList = {
                   'primaryOrgVo.org.id':'',
                   'primaryOrgVo.displayLevel':'',
                    'primaryOrgVo.teamClass.id':'',
                    '_search':'false',
                    'rows':'100',
                    'page':'1',
                    'sidx':'id',
                    'sord':'desc' 
                    }

#组织机构--综治组织 删除
oragnizationDelete = {
                  'mode':'',
                  'selectedIds':''    
                      }


#组织机构--综治组织 导出
oragnizationExport = {
                   'primaryOrgVo.org.id':'',
                   'primaryOrgVo.displayLevel':'',
                   'primaryOrgVo.teamClass.id':'',
                   '_search':'false',
                   'rows':'20',
                   'page':'1',
                   'sidx':'id',
                   'sord':'desc',
                   'primaryOrgVo.teamClass.internalId':'',
                   'primaryOrgVo.teamClass.displayName':'' 
                      }

#组织机构--综治组织 -- 维护成员
memberParam = {
                'serviceTeamMember.baseId':'',
                'serviceTeamMember.teamId':'',
                'serviceTeamMember.isTeam':'',
                'serviceTeamMember.position.id':'',
                'serviceTeamMember.onDuty':''
               }




#新增/修改成员库
personParam = {
            'serviceTeamMemberBase.id':'',
            'serviceTeamMemberBase.org.id':'',
            'addTeam':'',
            'serviceTeamMemberBase.name':'',
            'serviceTeamMemberBase.gender.id':'',
            'serviceTeamMemberBase.job':'',
            'serviceTeamMemberBase.birthday':'',
            'serviceTeamMemberBase.mobile':'',
            'serviceTeamMemberBase.homePhone':'',
            'serviceTeamMemberBase.remark':'',
            'positionInTeam':'',
            'isSubmit':''   
               }

#成员库列表
personList = {
                'serviceTeamMemberVo.orgScope':'',
                'serviceTeamMemberVo.org.Id':'',
                'serviceTeamMemberVo.nameIsDuplicate':'',
                '_search':'false',
                'rows':'20',
                'page':'1',
                'sidx':'baseId',
                'sord':'desc'
              }

#成员库检查点
personCheck = {
              'name' :''
               }
personCheck2 = {
              'name' :'',
              'mobile':''
               }
#成员库删除
personDel = {
             'selectedIds':'',
             'mode' : ''
             }

#综治组织新增成员库
memberAdd = {
            'serviceTeamMember.baseId':'',
            'serviceTeamMember.teamId':'',
            'serviceTeamMember.isTeam':'',
            'serviceTeamMember.position.id':'',
            'serviceTeamMember.onDuty':'' 
             }

#综治组织移除成员
memberRemove = {
                'serviceTeamMemberVo.baseId':'',
                'serviceTeamMemberVo.teamId':'',
                'serviceTeamMemberVo.isTeam':''
                }

#综治组织--维护成员--重新担任职位
danRenZhiWei = {
               'count':'',
                'serviceTeamMemberVo.memberId':'',
                'serviceTeamMemberVo.onDuty':'',
                'serviceTeamMemberVo.isTeam':'',
                'serviceTeamMemberVo.teamId':'' 
                }
#组织机构--辖区队伍--导出
export_xqdw = {
            '_search':'false'  ,  
            'leaderTeamsVo.displayLevel':'allJurisdiction',    
            'leaderTeamsVo.organization.id':'',
            'leaderTeamsVo.orgLevel':'',    
            'organization.id':'',
            'page':'1',    
            'rows':'20',
            'sidx':'id',
            'sord':'desc'   
               }
#组织机构--服务团队 --新增团队
addTeam = {
            'mode':'',
            'serviceTeam.id':'',
            'serviceTeam.org.id':'',
            'isSubmit':'',
            'serviceTeam.org.orgName':'',
            'serviceTeam.teamType.id':'',
            'serviceTeam.teamName':'',
            'serviceTeam.buildDate':'',
            'serviceTeam.remark':''
           }

#组织机构--服务团队--列表
TeamList = {
            'serviceTeamVo.org.id':'',
            'serviceTeamVo.displayLevel':'',
            'serviceTeamVo.logOut':'',
            'serviceTeamVo.teamType.id':'',
            '_search':'false',
            'rows':'20',
            'page':'1',
            'sidx':'id',
            'sord':'desc'  
            }
#组织机构--服务团队--检查点（新增）
checkTeamName = {
                 'teamName':''
                 }
#组织机构--服务团队--删除
deleteTeam = {
              'mode':'',
              'selectedIds':''
              }
#组织机构--服务团队--导出
exportTeam = {
                'serviceTeamVo.org.id':'',
                'serviceTeamVo.displayLevel':'sameGrade',
                'serviceTeamVo.logOut':'',
                'serviceTeamVo.teamType.id':'',
               ' _search':'false',
                'rows':'20',
                'page':'1',
                'sidx':'id',
                'sord':'desc'
              }
#组织机构--服务团队--解散团队
dismissTeam = {
              'serviceTeam.logOutReason':'',
              'serviceTeam.logOutTime':'',
              'serviceTeam.id':'' 
              }

#组织机构--成员库--维护对象
weiHuDuiXiang = {
                'baseId':'',
                'objectType':'',
                'objectIdsAndNames':''
                 }
#组织机构--成员库--检测查重
jianCeChaChong = {
                'selectedIds':'',
                'serviceTeamMemberVo.mobile':'',
                'serviceTeamMemberVo.name':'',
                'serviceTeamMemberVo.baseId':'',
                'serviceTeamMemberVo.org.id':'',
                'combineSelectedIds':'',
                'serviceTeamMemberBase.name':'',
                'serviceTeamMemberBase.job':'',
                'serviceTeamMemberBase.mobile':'',
                'serviceTeamMemberBase.homePhone':''
                  }

#组织机构--成员库 -- 层级转移
cengJiZhuanYi = {
               'orgId':'',
               'selectedIds':''
                 }

#组织机构--成员库--导入
importMember = {
                'dataType':'',        
                'enterpriseType':'',    
                'isNew':'1',    
                'reportTime':'' ,   
                'startRow':'4',    
                'templates':'',    
                'upload':None,
                'yearDate':''     
                }

#         新增服务成员——参数
FuWuChengYuanObject ={
                     'serviceTeamMemberBase.id':'',
                     'erviceTeamMemberBase.org.id':'',
                     'addTeam':'',
                     'serviceTeamMemberBase.name':'',
                     'serviceTeamMemberBase.gender.id':'',
                     'serviceTeamMemberBase.job':'',
                     'serviceTeamMemberBase.birthday':'',
                     'serviceTeamMemberBase.mobile':'',
                     'serviceTeamMemberBase.homePhone':'',
                     'serviceTeamMemberBase.remark':'',
                     'positionInTeam':'',
                     'isSubmit':''
                     }

#            查看服务人员——检查点
ChaKanRenYuanObject = {
          "name":None,
          "job":None,
          "serviceTeamMemberVo.org.Id":None
              
             }

#         删除服务人员——参数
delFuWuChengYuan={
                  'selectedIds':'',
                  'mode':'delete'
                  }

# 删除记录——参数
deljilu={
                  'recordIds':'',
                  'mode':'delete'
                  }

#         删除民情日志 ——参数       
delminqinrizhi={
                  'logIds':'',
                  }

# 查看服务成员是否新增成功——参数
getFuWuChengYuan={
                  'serviceTeamMemberVo.orgScope':'sameGrade',
                  'serviceTeamMemberVo.org.Id':'',
                  'serviceTeamMemberVo.nameIsDuplicate':'0',
                  '_search':'',
                  'rows':'100',
                  'page':'1',
                  'sidx':'baseId',
                  'sord':'desc'
                  }

#         新增实有单位——参数
ShiYouDanWeiObject ={
             'mode':'',
              'organizationId':'',
              'location.gisInfo.buildingId':'',
              'location.gisInfo.centerX':'',
              'location.gisInfo.centerY':'',
              'location.id':'',
              'location.imgUrl':'',
              'location.organization.orgName':'',
              'location.companyName':'',
              'location.companyAddress':'',
              'location.businessLicenseNo':'',
              'location.orgCode':'',
              'location.companyType.id':'',
              'location.corporateRepresentative':'',
              'location.idCardNo':'',
              'location.telephone':'',
              'location.facsimile':'',
              'location.registeredCapital':'',
              'location.economicNature.id':'',
              'location.registrationDate':'',
              'location.expiryDate':'',
              'location.businessScope':'',
              'location.registrationAddress':'',
              'location.employeesNum':'',
              'location.competentDepartment':'',
              'location.supervisoryLevel.id':'',
              'location.supervisoryDepartment':'',
              'location.fireFightingLevel.id':'',
              'location.securityChief':'',
              'location.remark':''
              } 

#            查看实有单位——检查点
ChaKanDanWeiObject = {
          "companyName":None,
          "companyAddress":None,
          "organizationId":None
              
             }

#     删除实有单位——参数
ChaKanShiYouDanWeiObject ={
                           "organizationId":"",
                           "location.isEmphasis":"false",
                           "_search":"false",
                           "rows":"20",
                           "page":"1",
                           "sidx":"id",
                           "sord":"desc"
                           }

#            新增记录——参数
jilu={
      "mode":"",
      "serviceRecord.userOrgId":"",
      "serviceRecord.organization.id":"",
      "serviceRecord.id":"",
      "serviceRecord.teamId":"",
      "isSubmit":"",
      "serviceRecord.occurDate":"",
      "serviceRecord.occurPlace":"",
      "serviceRecord.serviceMembers":"",
      "serviceRecord.serviceJoiners":"",
      "serviceRecord.serviceObjects":"",
      "serviceRecord.recordType":"",
      "serviceRecord.serviceContent":""
      }

#         查看记录是否新增成功——检查点
ChaKanXunChangQingKuang={
                         "occurPlace":None,
                         "objectIds":None,
                         }

# 查看记录是否新增成功{——参数
getXunChangQingKuang={
                      "serviceRecordVo.displayLevel":"sameGrade",
                      "serviceRecordVo.organization.id":"",
                      "serviceRecordVo.displayYear":time.strftime("%Y"),
                      "rows":"200",
                      "page":"1",
                      "sidx":"id",
                      "_search":"false",
                      "sord":"desc"
                      }
#        生成民情日志——参数
mingqinrizhi={
              "peopleLog.userId":"",
              "peopleLog.serviceRecordId":"",
              "peopleLog.organization.id":"",
              "peopleLog.isAttachment":"",
              "peopleLog.organization.orgName":"",
              "peopleLog.belonger":"",
              "peopleLog.publishDate":"",
              "peopleLog.address":"",
              "peopleLog.title":"",
              "peopleLog.contents":"",
              "peopleLog.summary":""
              }

#        修改记录——参数
xiugaijilu={
            "mode":"",
            "serviceRecord.userOrgId":"",
            "serviceRecord.organization.id":"",
            "serviceRecord.id":"",
            "serviceRecord.teamId":"",
            "isSubmit":"",
            "serviceRecord.occurDate":"",
            "serviceRecord.occurPlace":"",
            "serviceRecord.serviceMembers":"",
            "serviceRecord.serviceJoiners":"",
            "serviceRecord.serviceObjects":"",
            "serviceRecord.recordType":"",
            "serviceRecord.serviceContent":""
            }

#        生成民情日志——参数
scmingqinrizhi={
                "peopleLog.userId":"",
                "peopleLog.serviceRecordId":"",
                "peopleLog.organization.id":"",
                "peopleLog.isAttachment":"",
                "peopleLog.organization.orgName":"",
                "peopleLog.belonger":"",
                "peopleLog.publishDate":"",
                "peopleLog.address":"",
                "peopleLog.title":"",
                "peopleLog.contents":"",
                "peopleLog.summary":""
                }

# 查看民情日志是否新增成功——参数
minqinrizhi={
             "isComment":"false",
             "_search":"false",
             "rows":"20",
             "page":"1",
             "sidx":"id",
             "sord":"desc",
             }

#   查看民情日志是否新增成功—检查点
chakanminqinrizhi={
                         "title":None,
                         }

#  导出记录库数据——参数
dldataShiYouDanWei={
                    "serviceRecordVo.organization.id":"",
                    "serviceRecordVo.displayLevel":"sameGrade",
                    "serviceRecordVo.displayYear":time.strftime("%Y"),
                    "rows":"20",
                    "page":"1",
                    "sidx":"id",
                    "sord":"desc",
                    "_search":"false",
                    "pageOnly":"false"
                    }

# 输入存在的数据进行搜索——参数
goajisousuo={
             "serviceRecord.organization.id":"",
             "serviceRecordVo.occurDateStart":"",
             "serviceRecordVo.occurDateEnd":"",
             "serviceRecordVo.occurPlace":"",
             "serviceRecordVo.serviceMembers":"",
             "serviceRecordVo.serviceJoiners":"",
             "serviceRecordVo.serviceObjects":"",
             "serviceRecordVo.serviceContent":"",
             "serviceRecordVo.organization.id":"",
             "serviceRecordVo.displayLevel":"sameGrade",
             "_search":"false",
             "rows":"20",
             "page":"1",
             "sidx":"id",
             "sord":"desc"
             }

# 输入不存在的数据进行搜索——参数
getchaxundaibanrizhi={
                      "subject":None,
                      }
#服务记录库列表参数
serviceRecordListPara={
                'serviceRecordVo.organization.id':'',
                'serviceRecordVo.displayLevel':'allJurisdiction',
                'serviceRecordVo.displayYear':'',
                '_search':'false',
                'rows':'200',
                'page':'1',
                'sidx':'id',
                'sord':'desc'                       
                       }