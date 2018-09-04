# -*- coding:UTF-8 -*-
'''
Created on 2015-11-4

@author: N-254
'''
##查看列表所带的postdata数据
GetHuZhouXunJianListPara = {
                            'orgId':'',
                            'page':'1',
                            '_search':'false',
                            'rows':'100',
                            'sidx':'id',
                            'sord':'desc'
                      } 
##新增修改用到的字段
editOrAddObject = {'safetyCheckBasics.org.id':'',
                 'safetyCheckBasics.org.orgInternalCode':'',
                 'safetyCheckBasics.org.orgLevel.internalId':'',
            'safetyCheckBasics.companyName':'',
            'safetyCheckBasics.companyAddr':'',
            'safetyCheckBasics.companyType.id':'',
            'safetyCheckBasics.orgNo':'',
            'safetyCheckBasics.id':'',
            'mode':''
            }
##设置检查点参数
HuZhouXunJian_check = {
           'companyAddr':None,
           'companyName':None,
           'companyType':None,
           'orgNo':None
          }
##删除
HuZhouXunJian_ids = {
                    'ids':None    
                       }

#高级搜索
HuZhouXunJian_search = {
               'safetyCheckBasics.companyName':'',
               'safetyCheckBasics.companyType.id':'',
               'safetyCheckBasics.companyAddr':'',
               'safetyCheckBasics.orgNo':'',
               '_search':'false',
               'orgId':None,
               'rows':100,
               'page':100,
               'sidx':'id',
               'sord':'desc'
                    }
#合并单位
HuZhouXunJian_unionParam = {
                 'ids':None,
                 'mergeId':None
                            }

#新增模板
addOrUpdateModelParam = {
               'safetyCheckModule.id':'',
               'safetyCheckModule.org.id':'' ,
               'safetyCheckModule.moduleName':'',
               'safetyCheckModule.checkYear':'',
               'safetyCheckModule.checkObject':'',
               'mode':''
                 }
#新增模板检查点
checkModelParam = {
                   'moduleName':''
                   }

#模板列表参数
getListModelParam = {
                'safetyCheckModule.org.id':None,
                '_search':'false',
                'rows':'1000',
                'page':'1',
                'sidx':'createDate',
                'sord':'desc'
                  }
# #新增一级分类
# addModelFirstClass ={
#                      'mode':'',
#                      'safetyCheckModuleDetail.id':'',
#                      'safetyCheckModuleDetail.parentId':'',
#                      'safetyCheckModuleDetail.moduleId':'',
#                      'safetyCheckModuleDetail.detailLevel':'',
#                      'safetyCheckModuleDetail.isLeaf':'',
#                      'safetyCheckModuleDetail.displayName':'',
#                      'safetyCheckModuleDetail.score':'',
#                      'safetyCheckModuleDetail.isUse':''
#                      }

#一级分类列表参数
modelFirstListParam = {
                 'safetyCheckModuleDetail.moduleId':'',
                  ' _search':'false',
                   'rows':'10000',
                   'page':'1',
                   'sidx':'',
                   'sord':'asc'
                   }
#一级,二级,三级分类检查点
checkModelFirst = {
                   'displayName':'',
                   'score':None
                   }

# #新增二级分类
# addTwoClass = {
#                'mode':'add',
#                'safetyCheckModuleDetail.id':'',
#                'safetyCheckModuleDetail.parentId':'',
#                'safetyCheckModuleDetail.moduleId':'',
#                'safetyCheckModuleDetail.detailLevel':'',
#                'safetyCheckModuleDetail.isLeaf':'',
#                'safetyCheckModuleDetail.displayName':'',
#                'safetyCheckModuleDetail.score':'',
#                'safetyCheckModuleDetail.isUse':''
#                }

#新增三级分类
addClass ={
               'mode':'add',
               'safetyCheckModuleDetail.id':'',
               'safetyCheckModuleDetail.parentId':'',
               'safetyCheckModuleDetail.moduleId':'',
               'safetyCheckModuleDetail.detailLevel':'',
               'safetyCheckModuleDetail.isLeaf':'',
               'safetyCheckModuleDetail.displayName':'',
               'safetyCheckModuleDetail.score':'',
               'safetyCheckModuleDetail.isUse':'',
               'safetyCheckModuleDetail.isInput':None 
                }
#分类修改
editClass= {
            'mode':'',
            'safetyCheckModuleDetail.id':'',
            'safetyCheckModuleDetail.parentId':'',
            'safetyCheckModuleDetail.moduleId':'',
            'safetyCheckModuleDetail.detailLevel':'',
            'safetyCheckModuleDetail.isLeaf':'',
            'safetyCheckModuleDetail.displayName':'',
            'safetyCheckModuleDetail.score':'',
            'safetyCheckModuleDetail.isUse':''           
            }


#模板启用
isUseMode = {
             'safetyCheckModule.isUse':'',
             'safetyCheckModule.id':''
             }
#模板启用检查点
checkIsUseMode = {
                  'isUse':'',
                  'moduleName':None
                  }
#项目细则列表
projectList = {
               '_search':'false',
               'rows':'10000',
               'page':'1',
               'sidx':None,
               'sord':'asc'
               }
#项目细则参数
projectParam = {
              'safetyCheckModuleDetail.moduleId' :None 
                }
#分类预览查看
lookClassParam = {
                  'mode':'',
                  'safetyCheckModuleDetail.id':''
                  }
#添加单位检查参数
check_unitParam = {
                 'mode':'',
                 'safetyCheckInspection.safetyCheckBasics.id':'',
                 'safetyCheckInspection.safetyCheckBasics.org.id':'',
                 'safetyCheckInspection.safetyCheckBasics.companyName':'',
                 'safetyCheckInspection.moduleDetailInspections[0].safetyCheckModuleDetail.id':'',
                 'safetyCheckInspection.moduleDetailInspections[1].safetyCheckModuleDetail.id':'',
                 'safetyCheckInspection.moduleDetailInspections[2].safetyCheckModuleDetail.id':''
                   }

check_companyParam = {
                      'safetyCheckInspection.id':'',
                      'safetyCheckInspection.checkNo':'',
                      'safetyCheckInspection.safetyCheckBasics.id':'',
                      'safetyCheckInspection.safetyCheckBasics.companyName':'',
                      'safetyCheckInspection.isQualified':'',
                      'safetyCheckInspection.org.id':'',
                      'safetyCheckInspection.checkDate':'',
                      'safetyCheckInspection.moduleDetailInspections[0].checkName':'',
                      'safetyCheckInspection.moduleDetailInspections[0].safetyCheckModuleDetail.id':'',
                      'safetyCheckInspection.moduleDetailInspections[0].checkType':'',
                      'safetyCheckInspection.riskLevel.id':'',
                      'safetyCheckInspection.checkType.id':'',
                      'safetyCheckInspection.rectificationDate':'',
                      'safetyCheckInspection.checkUsers':''
                      }

#添加单位检查点
check_unitParam= {
                  'safetyCheckInspectionVo.org.id':'',
                  '_search':'false',
                  'rows':'20',
                  'page':'1',
                  'sidx':'i.createdate',
                  'sord':'desc'
                  }


companyName = {
                'companyName' : ''
               }

#专项检查高级搜索
searchCompanyUnit = {
            'safetyCheckInspectionVo.org.id':'',
            'safetyCheckInspectionVo.safetyCheckBasics.companyName':'',
            'safetyCheckInspectionVo.checkNo':'',
            'safetyCheckInspectionVo.riskLevel.id':'',
            'safetyCheckInspectionVo.checkType.id':'',
            'safetyCheckInspectionVo.detailId':'',
            'safetyCheckInspectionVo.startCheckDate':'',
            'safetyCheckInspectionVo.endCheckDate':'',
            'safetyCheckInspectionVo.startRectificationDate':'',
            'safetyCheckInspectionVo.endRectificationDate':'',
            'safetyCheckInspectionVo.checkUsers':'',
            '_search':'false',
            'rows':'20',
            'page':'1',
            'sidx':'i.createdate',
            'sord':'desc'         
        }

#高级搜索用到的检查字段
checkCompanyUnit= {
               'safetyCheckInspectionVo.safetyCheckBasics.companyName':None,  
               'safetyCheckInspectionVo.riskLevel.id':None,
               'safetyCheckInspectionVo.checkType.id':None  
                   }
#删除模板
moudleDelete = {
             'safetyCheckModule.id':None   
                }


#专项检查--基础信息--导出参数
exportDataParam = {
                 'orgId':'',
                 'page':1,
                 '_search':'false',
                 'rows':20,
                 'sidx':'id',
                 'sord':'desc'  
                   }
#专项检查--基础信息--导入参数
importDataParam = {
                  'dataType':'',
                  'enterpriseType':'',
                  'isNew' :1,
                  'reportTime':'',
                  'startRow':'4',
                  'templates':'',
                  'upload':None,
                  'yearDate':''
                   }



