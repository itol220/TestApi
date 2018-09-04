# -*- coding:UTF-8 -*-
'''
Created on 2015-11-24

@author: N-133
'''
from COMMON import Time
from COMMON.CommonUtil import createRandomString
from COMMON.Time import TimeMoveType
from CONFIG import InitDefaultPara
from Interface.YunWeiPingTai.YunWeiCommon.YunWeiCommonIntf import \
    getDbQueryResultYunWei

departmentNo=InitDefaultPara.clueOrgInit['DftQuOrgDepNo']
def enum(**enums):
    return type('Enum', (), enums)
#个性化配置选项
ConfigType = enum(ZHUYETU=1,ERWEIMA=2,BANLIYIJIAN=9,MORENFENXIANG=8,BAOLIAOTONGJI=3,SHENGYIN=4)
ConfigValue=enum(CLOSE='0',OPEN='1')
#关键字过滤类型
FilterType=enum(INFO=0,NICK=1)
NoticeType=enum(SYSTEM=0,ACTIVITY=1)
HomePageShow=enum(HIDE=0,SHOW=1)
CloseState=enum(OPEN=0,CLOSE=1)
InfoType=enum(BAOLIAO=0,SHUOSHUO=5)
# Direction=enum(UP=0,DOWN=1)
ConvenienceState=enum(OPEN=0,CLOSE=1)
OrgOpenState=enum(OPEN=1,CLOSE=0)
ThemeState=enum(OPEN=0,CLOSE=1)
IsHotState=enum(YES=0,NO=1)
JumpType=enum(HTML5=1,NOTICE=2,PICTURE=3)

# 新增关键字参数
addKeywordSettingPara={
               "keyWordSetting.filterType":"", #过滤类型，0表示信息，1表示昵称
               "keyWordSetting.keyWords":"" #关键字信息
               }

#更新关键字参数
updateKeywordSettingPara = {
                            "keyWordSetting.id":"",
                            "keyWordSetting.keyWords":""
                            }
# 获取关键字列表
getKeywordListPara={
                   "rows":"20",
                   "page":"1",
                   "sidx":"id",
                   "sord":"desc",
                   }

# 删除关键字
deleteKeywordListPara={
                   "ids[]":""
                   }



# 修改关键字参数
updateGuanJianZi={
               "keyWordSetting.id":None,
               "keyWordSetting.keyWords":None
               }

# 查看关键字检查点
GuanJianZhi={
                   "notice":None
                   }

# 修改关于我们页面
updateGuanYuWoMen={
                   "notice":''
                   }

# 修改积分配置
updateJiFenPeiZhi={
                   "pointsSetting.points":'',
                   "pointsSetting.id":''
                   }

# 查看积分配置
chakanJiFenPeiZhi={
                    "_search":"false",
                   "rows":"20",
                   "page":"1",
                   "sidx":"id",
                   "sord":"desc",
                   }
# 积分配置检查点
JiFenPeiZhi={
             "id":None,
             "points":None,
             }

# 修改积分规则
updateJiFenGuiZhe={
                   "departmentNo":"",
                   "userName":"",
                   "updateUserId":"",
                   "id":"",
                   "notice":"",
                   
                   }

# 查看积分规则
chakanJiFenGuiZhe={
                   "departmentNo":"",
                   
                   }

#主题新增
themeAddDict = {
                "themeRelation.openState":0, #是否全下辖开放，0表示开放，1表示不开放
                "themeContent.name":"", #主题名称
                "themeContent.description":"", #主题描述
                "themeRelation.departmentNo":InitDefaultPara.clueOrgInit['DftShengOrgDepNo'], #部门编码，默认用省
                "themeRelation.orgName":InitDefaultPara.clueOrgInit['DftShengOrg'], #部门名称，默认用省
                "themeRelation.infoType":0 #主题类型，0表示爆料主题，5表示说说主题
                }
#修改主题
themeUpdPara={
              'id':'',
              'name':'',
              'description':'',
              }
#开启/关闭主题
updThemeStatePara={
            'ids[]':'',
            'state':''#1关闭，0开启                   
                   }
#更新热门状态
updHotStatePara={
'ids[]':'',                 
'isHotState':''#0开启热门#1关闭热门      
                 }

#移动主题参数
moveThemePara={
            'id':'',
            'referId':'',
            'departmentNo':departmentNo,
            'position':'after'
               }
#主题列表参数
themeListPara={
'themeRelation.departmentNo':InitDefaultPara.clueOrgInit['DftShengOrgDepNo'],
'themeContent.name':'',
'themeRelation.infoType':'5',#0爆料，5畅聊说说
'_search':'false',
'rows':'-1',
'page':'1',
'sidx':'id',
'sord':'desc',               
               }
#主题列表检查参数
themeListCheckPara={
'themeContentsId':None,
'state':None,#是否开启，1关闭，0开启
'isHotState':None,#是否热门
'infoType':None,
'description':None,
'name':None                    
                    }
#新增个性化配置
addPersonalConfigPara = {
                "personalizedConfiguration.configurationType":'', #8为默认分享状态,主题=1,二维码=2,办理意见=9,默认分享=8,爆料统计=3,爆料声音=4
                "personalizedConfiguration.configurationValue":'', #状态，1表示公开
                "personalizedConfiguration.mobileType":"",
                "personalizedConfiguration.departmentNo":InitDefaultPara.clueOrgInit['DftQuOrgDepNo'],
                "personalizedConfiguration.orgName":InitDefaultPara.clueOrgInit['DftQuOrg']
                 }
#个性化配置列表参数
personalConfigListPara={
                'personalizedConfiguration.departmentNo':InitDefaultPara.clueOrgInit['DftQuOrgDepNo'],
                '_search':'false',
                'rows':'200',
                'page':'1',
                'sidx':'id',
                'sord':'desc',                        
                        }
#个性化配置列表检查参数
personalConfigListCheckPara={
           'id':None,
           'configurationType':None, #8为默认分享状态,主题=1,二维码=2,办理意见=9,默认分享=8,爆料统计=3,爆料声音=4               
           'configurationValue':None,#状态，1表示公开
                             }

#修改个性化配置列表参数
updPersonalConfigListPara={
            'personalizedConfiguration.configurationValue':'',
            'personalizedConfiguration.id':'',
            'personalizedConfiguration.configurationType':'',                           
                        }
#新增角色参数
addRolePara={
'mode':'add',
'addPermissionIds':'',
'deletePermissionIds':'',
'role.id':'',
'role.roleName':'线索测试自动化岗位',
'role.description':'',
             }
#新增运维人员参数
xinZengYunWeiRenYuan={
                'adminUser.userName':'test001'+createRandomString(),
                'adminUser.name':'test%s' % createRandomString(),
                'adminUser.password':'111111',
                'confirmPwd':'111111',
                'adminUser.mobile':'13111111111',
                'orgSelectTree':InitDefaultPara.clueOrgInit['DftQuOrg'],
                'adminUser.departmentNo':InitDefaultPara.clueOrgInit['DftQuOrgDepNo'],
                'adminUser.administrator':0,
                'roleIdList':'',#岗位id
                      }
#运维人员列表参数
yunWeiRenYuanLieBiao={
            'adminUser.userName':'',
            '_search':'false',
            'rows':'200',
            'page':'1',
            'sidx':'id',
            'sord':'desc'
                      }
#运维人员列表检查参数
yunWeiRenYuanLieBiaoJianCha={
            'userName':None,
            'name':None,
            'mobile':None
                    }
#修改运维人员参数
xiuGaiYunWeiRenYuan={
            'adminUser.id':'',
            'mode':'edit',
            'adminUser.userName':'',
            'adminUser.name':'',
            'adminUser.mobile':'',
            'orgSelectTree':InitDefaultPara.clueOrgInit['DftShengOrg'],
            'adminUser.departmentNo':'95',
            'orgName':InitDefaultPara.clueOrgInit['DftShengOrg'],         
                     }
#运维人员重置密码参数
chongZhiMiMa={
                'adminUser.id':'',
                'adminUser.password':'',
                'confirmPwd':'',
                   }
#新增公告
yunWeiGongGaoXinZeng={
          'operationNotice.noticeType':'',
          'operationNotice.title':'',
          'homePageShow':'',#on/off
          'operationNotice.homePageShow':'',#0不在首页显示，1在首页显示
          'noticeEndDate':Time.moveTime(standardTime=Time.getCurrentDateAndTime(),addDay=1,moveType=TimeMoveType.PLUS),
          'operationNotice.contentText':'',
          'operationNotice.listContentText':'',
          'operationNotice.departmentNo':InitDefaultPara.clueOrgInit['DftQuOrgDepNo'],
          'operationNotice.orgName':InitDefaultPara.clueOrgInit['DftQuOrg']
               }

#修改公告
yunWeiGongGaoXiuGai={
          'operationNotice.id':'',     
          'operationNotice.noticeType':'',
          'operationNotice.title':'',
          'operationNotice.homePageShow':'',#0不在首页显示，1在首页显示
          'noticeEndDate':Time.moveTime(standardTime=Time.getCurrentDateAndTime(),addDay=1,moveType=TimeMoveType.PLUS),
          'operationNotice.contentText':'',
          'operationNotice.listContentText':''
               }
#公告列表
yunWeiGongGaoLieBiao={
            'operationNotice.title':'',
            'operationNotice.departmentNo':InitDefaultPara.clueOrgInit['DftQuOrgDepNo'],
            '_search':'false',
            'rows':'200',
            'page':'1',
            'sidx':'id',
            'sord':'desc',
  }
#公告检查
yunWeiGongGaoLieBiaoJianCha={
            'noticeType':None,
            'title':None,
            'homePageShow':None,
            'contentText':None,
            'listContentText':None,
            'closeState':None
  }

#热门搜索关键字新增参数
hotSearchAddPara={
'mode':'add',
'id':'',
'infoType':InfoType.BAOLIAO,#0爆料，1说说
'keyword':'',
'remark':''
                  }

#热门搜索关键词列表参数
hotSearchListPara={
'hotSearch.keyword':'',
'hotSearch.infoType':'',#InfoType.BAOLIAO,
'_search':'false',
'rows':'20',
'page':'1',
'sidx':'displaySeq',
'sord':'desc',                   
                   }
#热门搜索关键词列表检查参数
hotSearchListCheckPara={
'id':None,
'infoType':None,
'keyword':None,
'state':None,#True启用False停用
'remark':None,#备注
}
#热门搜索关键字修改参数
hotSearchUpdPara={
'mode':'edit',
'id':'',
'infoType':InfoType.BAOLIAO,#0爆料，1说说
'keyword':'',
'remark':''
                  }

#判断热门搜索关键词是否已存在参数
isHotSearchExist={
'infoType':InfoType.BAOLIAO,
'keyword':'',
'id':''                  
                  }
#热门搜索关键字移动参数
hotSearchMovePara={
'id':'',
'referId':'',#目标id
'infoType':InfoType.BAOLIAO,
# 'direction':'',#Direction.UP向上，Direction.DOWN向下
'position':''#after下移，before上移，last到底，first到顶
}

#便民服务新增参数
addConvenienceServicePara={
'convenienceService.title':'',                   
'convenienceService.linkUrl':''
                       }

#便民服务修改参数
updConvenienceServicePara={
'convenienceService.id':'',                        
'convenienceService.title':'',                   
'convenienceService.linkUrl':''
                       }

#便民服务列表参数
convenienceServiceListPara={
'_search':'false',
'rows':'20',
'page':'1',
'sidx':'id',
'sord':'desc'          
                            }

#便民服务列表检查参数
convenienceServiceCheckPara={
'id':None,
'seq':None,#序号
'linkUrl':None,
'order':None,
'state':None,#ConvenienceState.OPEN  ConvenienceState.CLOSE
'title':None
                            }

#便民服务移动参数
convenienceServiceMovePara={
'id':'',#源id
'referId':'',#目标id
'position':''#after下移，before上移，last到底，first到顶
                            }

#新增电话分类参数
addMobileCategoryPara={
'companyCategory.categoryName':'',
'companyCategory.departmentNo':departmentNo,
'companyCategory.orgName':InitDefaultPara.clueOrgInit['DftQuOrg']        
                       }

#修改电话分类参数
updMobileCategoryPara={
'companyCategory.id':'',
'companyCategory.departmentNo':departmentNo,
'companyCategory.categoryName':''       
                       }

#电话分类移动参数
moveMobileCategoryPara={
'id':'',#源id
'referId':'',#目标id
'position':'',#after下移，before上移，last到底，first到顶
'departmentNo':departmentNo
                            }
#电话分类列表参数
mobileCategoryListPara={
'companyCategory.categoryName':'',
'companyCategory.departmentNo':departmentNo,
'_search':'false',
'rows':'-1',
'page':'1',
'sidx':'id',
'sord':'desc',  
  }
#电话分类列表检查参数
mobileCategoryListCheckPara={
'id':None,                             
'seq':None,
'categoryName':None                             
                             }
#新增电话参数
addPhonePara={
'companyPhone.companyName':'单位名称',
'companyPhone.telePhone':'',
'companyPhone.remark':'备注',
'companyPhone.departmentNo':departmentNo,
'companyPhone.orgName':'测试自动化区',
'companyPhone.companyCategoryId':'',
              }
#修改电话参数
updPhonePara={
'companyPhone.companyName':'单位名称',
'companyPhone.telePhone':'',
'companyPhone.remark':'备注',
'companyPhone.id':'',
              }
#电话列表参数
phoneListPara={
'companyPhone.departmentNo':departmentNo,
'companyPhone.companyCategoryId':'',
'_search':'false',
'rows':'-1',
'page':'1',
'sidx':'id',
'sord':'desc',               
               }
#电话列表检查参数
phoneListCheckPara={
'id':None,
'companyName':None,
'remark':None,
'seq':None,
'telePhone':None        
               }
#电话移动参数
moveMobilePara={
'id':'',#源id
'referId':'',#目标id
'position':'',#after下移，before上移，last到底，first到顶
'departmentNo':departmentNo
                            }
#操作区县开通、关闭参数
operateOrgPara={
'id':InitDefaultPara.clueOrgInit['DftQuOrgId'],
'departmentNo':departmentNo,
'parentOrg.id':InitDefaultPara.clueOrgInit['DftShiOrgId']
             }
#获取区县开通列表参数
getOrgOpenStateListPara={
'parentId':InitDefaultPara.clueOrgInit['DftShiOrgId'],
'_search':'false',
'rows':20,
'page':1,
'sidx':'id',
'sord':'desc',                         
            }

#区县开通列表检查参数
orgOpenStateListCheckPara={
'departmentNo':None,
'openState':None#OrgOpenState.OPEN/CLOSE         
                           }


#新增等级参数
addGradePara={
'grade.gradeDemand':'',#下一等级要求
'grade.gradeIntroduce':''#等级介绍
              }
#修改等级参数
updGradePara={
'grade.gradeIntroduce':'',
'grade.id':'',
'mode':'edit',
'grade.id':''     
              }

#获取等级列表参数
gradeListPara={
'_search':'false',
'rows':'200',
'page':'1',
'sidx':'id',
'sord':'desc',               
               }

#检查等级列表参数
gradeListCheckPara={
'id':None,
'grade':None,
'gradeDemand':None,
'gradeIntroduce':None
               }
#新增轮播图参数
addLunBoPara={
'eventConfiguration.title':'',
'eventConfiguration.description':'',
'eventConfiguration.jumpType':'',#1:JumpType.HTML5，2:公告JumpType.NOTICE，3：图片 JumpType.PICTURE
'startDate':Time.getCurrentDate(),
'endDate':Time.getCurrentDate(),
'eventConfiguration.departmentNo':departmentNo,
'eventConfiguration.linkUrl':None,#html5才有
'eventConfiguration.shareUrl':None,#html5才有
'eventConfiguration.operationNoticeId':None#运维公告才有
              }

#修改轮播图参数
updLunBoPara={
'eventConfiguration.id':'',
'eventConfiguration.title':'',
'eventConfiguration.description':'',
'startDate':Time.getCurrentDate(),
'endDate':Time.getCurrentDate(),
'eventConfiguration.departmentNo':departmentNo,
'eventConfiguration.operationNoticeId':None,#运维公告才有
              }
#轮播图列表参数
getLunBoListPara={
'eventConfiguration.departmentNo':departmentNo,
'_search':'false',
'rows':20,
'page':1,
'sidx':'id',
'sord':'desc'
               }
#轮播图列表检查参数
checkLunBoListPara={
'description':None,
'id':None,
'title':None,
'state':None,
'jumpType':None,
'shareUrl':None,
'linkUrl':None 
                    }
#轮播图移动参数
moveLunBoPara={
'id':'',#源id
'referId':'',#目标id
'position':'',#after下移，before上移，last到底，first到顶
'departmentNo':departmentNo
                            }