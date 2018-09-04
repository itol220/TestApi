# -*- coding:UTF-8 -*-
'''
Created on 2016-11-16

@author: Administrator
'''
from CONFIG import InitDefaultPara
#新增说说
addShuoShuoPara = {
                   "casualTalk":{
                                "themeContentId":"", #主题id
                                "contentText":"", #说说内容描述
                                "title":"", #说说标题
                                "departmentNo":InitDefaultPara.clueOrgInit['DftQuOrgDepNo']
                                }
                   }

#说说详情参数
getShuoShuoDetail={
                   "tqmobile":"true",
                   "id":""#信息id
                   }

#说说详情检查参数
checkShuoShuoDetailPara={
                         "praiseNum":None,
                         "commentNum":None,
                         "showState":None,
                         "topState":None
                         }

#获取说说
getShuoShuoPara = {
                   "page": "1",
                   "userId": "", 
                   "tqmobile": "true",
                   "rows": "10",
                   "departmentNo":InitDefaultPara.clueOrgInit['DftQuOrgDepNo'],
                   'themeContentId':'',
                   }

#检查说说
checkShuoShuoPara = {
                    "contentText":None,
                    "title":None,
                    "nickName":None,
                    "mobile":None,
                    "showState":None, #0表示公开，1表示CLOSE
                    "topState":None,#置顶状态：0表示未置顶，1表示置顶
                    "praiseNum":None#点赞数
                     }

#增加说说举报
addShuoShuoInfoReportPara = {
                            "reportType": "99", #99表示其他
                            "infoType": "5", #表示爆料
                            "infoId": "", #爆料Id
                            "themeContentId": "", #主题id,0表示无主题
                            "reportUserId": "", #举报用户id
                            "tqmobile": "true",
                            "publishUserMobile": "", #爆料发布者id
                             }

#我的说说列表参数
WoDeShouShouLieBiao={
                    'tqmobile':'ture',#手机识别码
                    'page':'1',#页数
                    'rows':'10' #每页记录数                            
                     }

#我的说说列表检查参数
WoDeShuoShuoLieBiaoJianCha={
                          'contentText':None,#说说内容
                          'title':None,#说说标题  
                          "nickName":None,#昵称
                          "mobile":None,#手机号
                          "showState":None, #显示状态：0表示公开，1表示CLOSE
                                  }

#删除说说参数
delShuoShuoPara = {
                   'tqmobile':'true',#手机识别码
                   'id':''#说说id
                   }

#说说新增关注参数
ShouShouAddConcernPara={
                    'tqmobile':'true',#手机识别码
                    'informationId':'',#信息Id
                    'concernUserId':'',#关注用户Id
                     }

#说说取消关注参数
ShouShouCancelConcernPara={
                     'tqmobile':'true',#手机识别码
                     'informationId':'',#信息Id
                     'concernUserId':''#关注用户Id                       
                     }

#获取我的关注列表
WoDeConcernListPara={
                    'tqmobile':'true',#手机识别码
                    'page':'1',#页数
                    'rows':'200',#每页记录数
                    'sidx':'',
                    'sord':''        
                     }

#我的关注列表检查参数
WoDeConcernListCheckPara={
                          'contentText':None,#说说内容 
                          'delState' :None#信息删除状态：0--未删除；1--删除    
                          }

#评论说说
addCommentForShuoShuoPara = {
                            "informationId":"",
                            "tqmobile": "true",
                            "commentUserId": "", #评论用户id
                            "commentType": "", #评论类型：0--评论；1--回复
                            "contentText": "", #评论内容
                            'replyUserId':""#回复用户Id
                            }

#获取说说评论
getCommentInShuoShuoPara = {
                        "sord": "desc",
                        "page": "1",
                        "infoType": "5", #0表示爆料
                        "sidx": "id",
                        "informationId": "", 
                        "tqmobile": "true",
                        "rows": "10",
                        }

#检查评论
checkCommentInShuoShuoPara = {
                          "contentText":None,
                          "commentNickName":None,
                          }

#获取我的评论列表
getMyCommentListPara={
                      "tqmobile":"true",
                      "infoType":"5",#信息类型：0--线索；5--说说
                      "sidx":"id",
                      "sord":"desc",
                      "page":"1",
                      "rows":"10"
                      }

#我的评论列表检查参数
checkMyCommentListPara={
                        "contentText":None,#评论内容
                        "inforDelState":None,#信息删除状态：0--未删除；1--删除
                        "inforContent":None,#说说内容
                        "delState":None,#删除状态：0--未删除；1--删除
                        "informationId":None#信息Id
                        }

#说说删除评论参数
delCommentForShuoShuoPara={
                           "tqmobile":"true",
                           "id":""#评论id
                           }

#说说新增点赞参数
addPraiseForShouShouPara={
               "tqmobile":"true",
               "informationId":"",
               "praiseUserId":"",
               }

#说说取消点赞参数
cancelPraiseForShouShouPara={
                            "tqmobile":"true",
                            "informationId":"",
                            "praiseUserId":""
                            }

#检查说说搜索列表
checkShuoShuoInSearchListPara = {
                    "contentText":None,
                    "title":None,
                    "nickName":None,
                    "mobile":None,
                    "commentNum":None, 
                    "concernNum":None,
                    "praiseNum":None#点赞数
                     }
#搜索说说参数
searchShuoShuoPara={
                    'tqmobile':'true',
                    'departmentNo':InitDefaultPara.clueOrgInit['DftQuOrgDepNo'],
                    'contentText':'',
                    'page':1,
                    'rows':20
                    }
#新增评论举报参数
ReportCommentShuoShuoPara={
                                "commentId": "",#评论信息id
                                "infoType": "",#信息类型
                                "reportType": "",#举报类型
                                "reportUserId": "",#举报用户id
                                "reportUserMobile": "",#举报人手机号
                                "tqmobile": "true",
                                "publishUserMobile": "", #爆料发布者
                                
                            }