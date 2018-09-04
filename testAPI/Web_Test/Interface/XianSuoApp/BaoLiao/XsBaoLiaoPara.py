# -*- coding:UTF-8 -*-
'''
Created on 2015-11-24

@author: N-133
'''
from __future__ import unicode_literals
from COMMON.CommonUtil import createRandomString
from CONFIG import InitDefaultPara

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
                                'address':'',
                                'themeContentId':''
                                },
                'tqmobile':'true'       
                }
#新增默认参数
xinZeng2={
          'information':{
                                'contentText': '事件描述%s'%createRandomString(),
                                'baiduX':'120.4989885463861',
                                'baiduY':'30.27759299562879',
                                'x':'120.488114380334',
                                'y':'30.27759299562879',
                                'address': '地址%s'%createRandomString()
                                },
            'tqmobile':'true' 
          }

#爆料广场线索数据获取
getClueListPara = {
                   'page':'1',
                   'tqmobile':'true',
                   'rows':'10',
                   'departmentNo':InitDefaultPara.clueOrgInit['DftQuOrgDepNo']
                   }
# 检查线索新增
chakanxiansuo={
               'searchInfoVo.information.orgId':'139854',
               'searchInfoVo.information.infoType':'0',
               '_search':'false',
               'rows':'20',
               'page':'1',
               'sidx':'id',
               'sord':'desc',
               }
#查询爆料参数
searchCluePara={
                'tqmobile':'true',
                'departmentNo':InitDefaultPara.clueOrgInit['DftQuOrgDepNo'],
                'contentText':'',
                'page':1,
                'rows':20
                }
# 新增线索检查点
wodeliebiaojiancha={
                'contentText':None,
                'address':None,
                }
jianchaxiansuo={
                'contentText':None,
                'address':None,
                'nickName':None
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
            'searchInfoVo.information.orgId':InitDefaultPara.clueOrgInit['DftQuOrgId'],
            'searchInfoVo.information.infoType':'0',
            '_search':'false',
            'rows':'200',
            'page':'1',
            'sidx':'id',
            'sord':'desc'        
                      }

#爆料广场线索数据获取
getClueListPara = {
                   'page':'1',
                   'tqmobile':'true',
                   'rows':'10',
                   'departmentNo':InitDefaultPara.clueOrgInit['DftQuOrgDepNo']
                   }

#爆料广场线索数据检查
checkClueInSquarePara = {
                 'issueHandSource':None,
                 'contentText':None,
                 'praiseNum':None,
                 'address':None,
                 'nickName':None,
                 'mobile':None,
                 'commentNum':None,
                 'showState':None,
                 'concernNum':None,
                 'visitState':None,
                 }

#我的爆料中获取列表
getClueInMyClueList = {
                       'tqmobile':'true',
                       'page':'1',
                       'rows':'100'

                       }
#重新提交参数
ChongXinTiJiao = {
                 'tqmobile':'true',
                 'contentText':'',
                 'parentInforId':'',
                  }
#删除爆料
ShanChuBaoLiao = {
                  'tqmobile':'true',
                  'id':'',
                       }
#举报爆料
addClueInfoReportPara = {
                        "reportType": "99", #99表示其他
                        "infoType": "0", #表示爆料
                        "infoId": "", #爆料Id
                        "themeContentId": "", #主题id,0表示无主题
                        "reportUserId": "", #举报用户id
                        "reportUserMobile":"", #举报人手机号
                        "tqmobile": "true",
                        "publishUserMobile": "", #爆料发布者id
                         }
#评论爆料
addCommentForCluePara = {
                            "informationId":"",
                            "tqmobile": "true",
                            "commentUserId": "", #评论用户id
                            "commentType": "0", #默认是0，0评论,1回复
                            "contentText": "", #评论内容
                            "replyUserId":""#回复评论用户id
                            }

#获取爆料评论
getCommentInCluePara = {
                        "sord": "desc",
                        "page": "1",
                        "infoType": "0", #0表示爆料
                        "sidx": "id",
                        "informationId": "", 
                        "tqmobile": "true",
                        "rows": "10",
                        }

#检查评论
checkCommentInCluePara = {
                          "contentText":None,
                          "commentNickName":None,
                          }
#获取我的评论列表
WoDeCommentListPara={
                    'tqmobile':'true',#手机识别码
                    'infoType':'',#信息类型
                    'sidx':'id',#排序字段
                    'sord':'desc',#排序方式
                    'page':'1',#页数
                    'rows':'200',#每页记录数            
                     }
#我的评论列表检查参数
WoDeCommentListCheckPara={
                          'contentText':None#爆料内容        
                          }
#删除评论参数
deletecommentPara={
                   'tqmobile':'',
                   'sidx':'',
                   'sord':'',
                   'page':'',
                   'rows':'',
                   }

#爆料删除评论参数
delCommentCluePara={
                           "tqmobile":"true",
                           "id":""#评论id
                           }
#举报评论参数
ReportCommentCluePara={
                        "tqmobile": "true",
                        "commentId": "0", #评论信息id
                        "reportUserId": "", #举报用户id
                        "reportUserMobile":"", #举报人手机号
                        "reportType":"",#举报类型
                        "infoType":"",#信息类型
                        "publishUserMobile":"",#发布人手机
                       }

#新增关注
addattentionCluePara = {
                        "informationId":"",
                        "tqmobile": "true",
                        "concernUserId": "", 
                        "concernDate": "0", 
                        }
#获取我的关注列表
WoDeConcernListPara={
                    'tqmobile':'true',#手机识别码
                    'sidx':'',#排序字段
                    'sord':'',#排序方式
                    'page':'1',#页数
                    'rows':'200',#每页记录数            
                     }

#我的关注列表检查参数
WoDeConcernListCheckPara={
                          'contentText':None#爆料内容        
                          }
#取消关注参数
CancelConcernPara={
                   "tqmobile":"true",
                    "informationId":"",#信息Id
                    "concernUserId":"",#点赞用户Id
                   }
#新增爆料点赞
addPraiseCluePara= {
                    "tqmobile":"true",
                    "informationId":"",#信息Id
                    "praiseUserId":"",#点赞用户Id
                    }
#查看点赞列表
ViewPraisellistPara={
                     'tqmobile':'True',
                     'sidx':'',
                     'sord':'',
                     'page':'',
                     'rows':'',
                     }
#爆料取消点赞参数
cancelPraiseCluePara={
                            "tqmobile":"true",
                            "informationId":"",
                            "praiseUserId":""
                            }
#获取点赞用户列表
getPraiseuserlistPara={
                       'tqmobile':'true',
                       'informationId':'',#信息id
                       'infoType':'',#信息类型 0:线索5:说说
                       'sidx':'',
                       'sord':'',
                       'page':'',
                       'rows':'',
                       }


#获取精彩推荐
getHighLightPara = {
                    "departmentNo":InitDefaultPara.clueOrgInit['DftQuOrgDepNo'],
                    "tqmobile":"true"
                    }

#检查精彩推荐
checkHighLightPara = {
                      "nickName":None,
                      "contentText":None,
                      "publishUserId":None,
                      "themeContentName":None,
                      "infoType":None, #0表示爆料，5表示说说
                      "certifiedType":None #是否认证
                      }
#获取热词配置
getHotWordPara={
                'tqmobile':'true',
                'departmentNo':InitDefaultPara.clueOrgInit['DftQuOrgDepNo'],
                'infoType':'',#类型区分
                }
#根据内容搜索主题
searchPara={
                'tqmobile':'true',
                'departmentNo':InitDefaultPara.clueOrgInit['DftQuOrgDepNo'],
                'name':'',#主题名
                'infoType':'',#类型区分 
            }