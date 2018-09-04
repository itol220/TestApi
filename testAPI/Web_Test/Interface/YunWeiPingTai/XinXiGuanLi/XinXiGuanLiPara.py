# -*- coding:UTF-8 -*-
'''
Created on 2015-11-24

@author: N-133
'''

from CONFIG.InitDefaultPara import orgInit

from CONFIG import InitDefaultPara
from CONFIG.InitDefaultPara import clueOrgInit

def enum(**enums):
    return type('Enum', (), enums)
#分享状态
ShowState = enum(CLOSE=0,OPEN=1,HIGHLIGHT=2)
#信息类型
InfoType = enum(CLUE=0,SHUOSHUO=5)
#举报类型
ReportType = enum(OTHER=99,BROADCAST=1)
#处理状态
ReportState = enum(UNHANDLE=0,HANDLED=1)
#删除方式
DeleteType = enum(YUNWEI=0,SHENGPINGTAI=1)
# 登录参数
DengLu={
        'tqmobile':'',
        'mobile':'',
        'password':'',
        'mobileType':'',
        }

# 新增线索
XinZeng={'information':{
                                'contentText':'',
                                'baiduX':'',
                                'baiduY':'',
                                'x':'',
                                'y':'',
                                'address':''},
                'tqmobile':'true'       
                }
# #新增默认参数
# xinZeng2={
#           'information':{
#                                 'contentText': '事件描述%s' % createRandomString(),
#                                 'baiduX':'120.1362348153468',
#                                 'baiduY':'30.28016484243025',
#                                 'x':'120.1250430287559',
#                                 'y':'30.27612037575986',
#                                 'address':'地址%s' % createRandomString(),
#                         },
#             'tqmobile':'true' 
#           }
# 信息管理查看线索新增
chakanxiansuo={
               'information.mobile':'',
               'information.departmentNo':InitDefaultPara.clueOrgInit['DftQuOrgDepNo'],
               'information.themeContentId':'',
               'rows':'20',
               'page':'1',
               'sidx':'id',
               'sord':'desc',
               }

# 新增线索检查点
jianchaxiansuo={
                'contentText':None,
                'address':None,
                'nickName':None,
                'mobile':None,
                'showState':None #爆料状态，1表示公开，0表示不公开
                }

#获取说说列表
getShuoShuoListPara = {
                       "mobile":"",
                       "departmentNo":InitDefaultPara.clueOrgInit['DftQuOrgDepNo'],
                       "themeContentId":"",
                       "rows":100,
                       "page":1,
                       "sidx":"id",
                       "sord":"desc"
                       }

#删除说说
deleteShuoShuoPara = {
                      "informationId":"",
                      "mobile":"",
                      "infoType":5, #5表示说说
                      "departmentNo":InitDefaultPara.clueOrgInit['DftQuOrgDepNo'],
                      "chooseRecord":"其他",
                      "deleteReason":"其他"
                      }

# 获取消息未读数量
xiaoxiweidu={
             'tqmobile':'',
             'userId':'',
             }

# 查看公告列表
gonggaoliebiao={
                'tqmobile':'',
                'departmentNo':'',
                'page':'',
                }

# 新增点赞
xinzengdianzan={
                'tqmobile':'',
                'informationId':'',
                'praiseUserId':'',
                }
#社管线索列表参数
XianSuoGuanLiLieBiao={
            'searchInfoVo.information.orgId':clueOrgInit['DftShengOrgId'],
            'searchInfoVo.information.infoType':'0',
            '_search':'false',
            'rows':'20',
            'page':'1',
            'sidx':'id',
            'sord':'desc'        
                      }

# 批量删除线索
ShanChuXianSuo={
                'ids[]':'',
                }
#单条线索删除
deleteSingleCluePara = {
                        "informationId":"",
                        "mobile":"",
                        "infoType":0, #默认线索
                        "departmentNo":InitDefaultPara.clueOrgInit['DftQuOrgDepNo'],
                        "chooseRecord":"其他",
                        "deleteReason":"其他"
                        }
delCluePara={
            'ids[]':'',
            'deleteReason':'其他'             
             }

# 设置线索状态
XianSuoGongKai={
                'ids[]':'',
                }

#     根据手机号进行搜索
XinXiSouSuo={
               'information.mobile':'',
               'information.departmentNo':'',
               '_search':'false',
               'rows':'20',
               'page':'1',
               'sidx':'id',
               'sord':'desc',             
             }

# 新增默认爆料分享状态
BanLiYiJianZT={
               'personalizedConfiguration.configurationType':'',            
               'personalizedConfiguration.configurationValue':'',   
               'personalizedConfiguration.departmentNo':'',   
               'personalizedConfiguration.orgName':'',   
               }

# 查看默认爆料分享状态
chakanBanLiYiJianZT={
               'personalizedConfiguration.departmentNo':'',
               '_search':'false',
               'rows':'20',
               'page':'1',
               'sidx':'id',
               'sord':'desc',             
             }


# 默认爆料分享状态检查点
ckBanLiYiJianZT={
               'id':None,  
                 }

# 修改默认爆料分享状态
XBanLiYiJianZT1={
               'personalizedConfiguration.configurationType':'',            
               'personalizedConfiguration.configurationValue':'',   
               'personalizedConfiguration.id':'',   
               }

#默认爆料分享状态检查点
XBanLiYiJianZT1={
                'id':None,          
                'configurationValue':None,    
               }

# 删除默认爆料分享状态
deleteXBanLiYiJianZT={
                'ids[]':'',
                }

# 新增电话分类
addDianHuaFL={
              'companyCategory.categoryName':'',    
              'companyCategory.departmentNo':'',    
              'companyCategory.orgName':'',    
              }

# 查看新增电话分类
chakanDianHuaFL={
               'companyCategory.categoryName':'',
               'companyCategory.departmentNo':InitDefaultPara.clueOrgInit['DftQuOrgDepNo'],
               '_search':'false',
               'rows':'-1',
               'page':'1',
               'sidx':'id',
               'sord':'desc',             
             }

# 新增电话分类检查点
ckDianHuaFL={
               'id':None,  
                 }

# 修改电话分类
updateDianHuaFL={
              'companyCategory.id':'',    
              'companyCategory.departmentNo':'',    
              'companyCategory.categoryName':'',    
              }

# 新增电话管理
addDianHuaGL={
              'companyPhone.companyName':'',
              'companyPhone.telePhone':'',
              'companyPhone.remark':'',
              'companyPhone.departmentNo':'',
              'companyPhone.orgName':'',
              'companyPhone.companyCategoryId':'',
              
              }

# 查看新增电话管理
chakanDianHuaGL={
               'companyPhone.departmentNo':'',
               'companyPhone.companyCategoryId':'',
               '_search':'false',
               'rows':'-1',
               'page':'1',
               'sidx':'id',
               'sord':'desc',             
             }

# 修改电话管理
updateDianHuaGL={
              'companyPhone.id':'',
              'companyPhone.companyName':'',
              'companyPhone.remark':'',
              'companyPhone.telePhone':'',
              
              }

# 删除电话管理
deleteDianHuaGL={
                 'ids[]':'',
                 'companyCategoryId':'',
                 }


# 新增办理意见分享状态
addYiJianZT={
               'personalizedConfiguration.configurationType':'',            
               'personalizedConfiguration.configurationValue':'',   
               'personalizedConfiguration.departmentNo':'',   
               'personalizedConfiguration.orgName':'',   
               }

# 查看办理意见分享状态
chakanYiJianZT={
               'personalizedConfiguration.departmentNo':InitDefaultPara.clueOrgInit['DftQuOrgDepNo'],
               '_search':'false',
               'rows':'20',
               'page':'1',
               'sidx':'id',
               'sord':'desc',             
             }


# 办理意见分享状态检查点
ckYiJianZT={
               'id':None,  
                 }

# 修改办理意见分享状态
updateYiJianZT={
               'personalizedConfiguration.configurationType':'',            
               'personalizedConfiguration.configurationValue':'',   
               'personalizedConfiguration.id':'',   
               }

#办理意见分享状态检查点
CKYiJianZT={
                'id':None,          
                'configurationValue':None,    
               }

# 删除办理意见分享状态
deleteYiJianZT={
                'ids[]':'',
                }
# 搜索常用电话分类
SouSuoCYDH={
                'companyCategory.categoryName':'',
                'companyCategory.departmentNo':'',
                '_search':'false',
                'rows':'-1',
                'page':'1',
                'sidx':'id',
                'sord':'desc',   
            }

# 导入常用电话
daoruCYDH={
                  "dataType":"",
                  "templates":"",
                  "dialog":"importDialog",
                  "startRow":"3",
                  "isNew":"1",
           }
#个性化配置列表参数
PersonalConfigListPara={
                'personalizedConfiguration.departmentNo':'000000',
                '_search':'false',
                'rows':'20',
                'page':'1',
                'sidx':'id',
                'sord':'desc'                      
                        }

#爆料管理中获取主题列表字典
getThemeListInClueManagePara = {
                                "departmentNo":InitDefaultPara.clueOrgInit['DftQuOrgDepNo'],
                                "themeContent.name":"",
                                "infoType":0, #0表示爆料
                                "rows":"20",
                                "page":"1",
                                "sidx":"id",
                                "sord":"desc"
                                }

#爆料管理中检查主题字典
checkThemeInClueManagePara = {
                              "name":None,
                              "description":None
                              }

#获取意见反馈列表字典
getUserFeedbackPara = {
                       "userFeedBack.mobile":"",
                        "rows":"1000",
                        "page":"1",
                        "sidx":"id",
                        "sord":"desc"
                      }
#检查意见反馈字典
checkUserFeedbackPara = {
                         "id":None,
                         "mobile":None,
                         "advice":None,
                         "isReply":None, #未反馈是0，已反馈是1
                         "replyUser":None,
                         "replyDate":None,
                         "replyContent":None
                         }
#用户意见反馈回复
replyForFeedbackPara = {
                        "ids":"",
                        "replyContent":""
                        }

#信息举报列表获取
getInformationReportPara = {
                                "informationReport.reportUserMobile":"",
                                "informationReport.publishUserMobile":"",
                                "informationReport.reportType":"", #举报类型，其他是99，广告营销是1
                                "informationReport.infoType":"", #0表示爆料，5表示说说
                                "informationReport.state":"", #0表示待处理，1表示已处理
                                "informationReport.themeContentId":"", #主题id
                                "rows":"20",
                                "page":"1",
                                "sidx":"id",
                                "sord":"desc"
                                }

#信息举报删除
deleteInfoReportPara = {
                        "ids[]":"", 
                        "infoType":"" #0表示爆料，5表示说说
                        }

#检查信息举报内容
checkInformationReportPara = {
                              "contentText": None, #举报原爆料内容
                              "themeContentName":None, #主题名称
                              "address":None, #地址
                              "reportName":None, #举报人
                              "publishUserName":None, #昵称
                              "title":None,
                              }						  
#解除举报
shieldInfoReportPara = {
                        "ids[]":"", 
                        "infoType":"" #0表示爆料，5表示说说
                        }
#评论举报列表获取
getCommentReportPara =   {
                            "commentReport.publishUserMobile":"",#发布用户手机
                            "commentReport.reportUserMobile":"",#举报用户手机
                            "commentReport.reportUserId":"",#举报用户ID
                            "informationReport.reportType":"", #举报类型，其他是99，广告营销是1
                            "commentReport.infoType":"", #0表示爆料，5表示说说
                            "commentReport.commentId":"",#评论ID
                            "commentReport.state":"", #0表示待处理，1表示已处理
                            "commentReport.reportCount":"",
                            "commentReport.reportInformationId":"",#举报信息id
                            "rows":"100",
                            "page":"1",
                            "sidx":"id",
                            "sord":"desc"
                            
                            }
#检查评论举报内容
checkCommentReportPara ={
                         "contentText": None, #举报评论内容
                         "reportName":None, #举报人
                         "publishUserName":None, #用户昵称
                         }
#信息评论举报删除
deleteCommentReportPara = {
                        "ids[]":"", 
                        "infoType":"" #0表示爆料，5表示说说
                        }
#获取删除记录
getDelRecordListPara = {
                        "delInfoRecord.mobile":"",
                        "delInfoRecord.infoType":"", #0表示爆料，5表示说说
                        "delInfoRecord.applicationType":"", #0表示运维平台，1表示省平台,请引用上面的DeleteType枚举变量
                        "delInfoRecord.deleteUser":"",
                        "delInfoRecord.departmentNo":InitDefaultPara.clueOrgInit['DftQuOrgDepNo'], #自动化省部门编码
                        "rows":"20",
                        "page":"1",
                        "sidx":"id",
                        "sord":"desc"
                        }

#检查删除记录
checkDelRecordPara = {
                      "contentText":None,
                      "nickName":None,
                      "address":None,
                      }

#获取说说列表
getShuoShuoListPara = {
                       "mobile":"",
                       "departmentNo":InitDefaultPara.clueOrgInit['DftQuOrgDepNo'],
                       "themeContentId":"",
                       "rows":"20",
                       "page":"1",
                       "sidx":"id",
                       "sord":"desc"
                       }

#检查说说
checkShuoShuoPara = {
                     "sortField":None,
                     "nickName":None,
                     "mobile":None,
                     "contentText":None,
                     "title":None,
                     "themeContentName":None,
                     "topState":None,
                     "showState":None #是否为精彩推荐
                     } 