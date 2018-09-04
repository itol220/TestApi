# -*- coding:UTF-8 -*-
'''
Created on 2016-11-8

@author: hongzenghui
'''

from CONFIG import InitDefaultPara, Global
from COMMON import Time
from Interface.PingAnJianShe.Common import CommonIntf
def enum(**enums):
    return type('Enum', (), enums)
#分享状态
ShowState = enum(CLOSE=0,OPEN=1,HIGHLIGHT=2)
#处理状态
DealState = enum(ADD=0,ACCEPT=1,HANDLE=3,COMPLETE=2)
#官方回复状态
OfficialState = enum(NOTREPLY=0,REPLY=1)

#快速搜索条件字典
clueFastSearchDict = {"searchInfoVo.fastSearchKey":None, #用户昵称或者手机号
                      "searchInfoVo.information.showState":"", #爆料状态，全部此项不填，公开填0，不公开填1，精彩推荐填2
                      "searchInfoVo.information.orgId":InitDefaultPara.clueOrgInit['DftQuOrgId'],
                      "searchInfoVo.information.infoType":0,
                      "searchInfoVo.information.themeContentId":None,#主题ID，无主题填0，
                      "_search":"false",
                      "rows":20,
                      "page":1,
                      "sidx":"id",
                      "sord":"desc"
                      }
#爆料删除字典
deleteCluePara = {
                  "delInfoRecord.informationId":"",
                  "delInfoRecord.mobile":"",
                  "delInfoRecord.infoType":0, #0表示线索
                  "delInfoRecord.departmentNo":InitDefaultPara.clueOrgInit['DftJieDaoOrgDepNo'], #街道部门编码959595995
                  "chooseRecord":"其他",
                  "delInfoRecord.deleteReason":"其他"
                  }
#高级搜索条件字典
clueAdvanceSearchDict = {
                      "searchInfoVo.information.orgId":InitDefaultPara.clueOrgInit['DftQuOrgId'],
                      "searchInfoVo.information.nickName":None, #昵称
                      "searchInfoVo.information.address":None, #地点
                      "searchInfoVo.information.contentText":None, #描述
                      "searchInfoVo.information.serialNumber":None, #事件单号
                      "searchInfoVo.information.state":None, #处理状态，全部是空，0表示新增,1表示受理，2表示办理，3表示办结
                      "searchInfoVo.information.showState":None, #公开状态 ，全部是空，0表示不公开，1表示公开
                      "searchInfoVo.officialReplyState":None, #官方回复状态，全部是空，0表示未回复， 1表示已回复
                      "searchInfoVo.commentNumStart":None,
                      "searchInfoVo.commentNumEnd":None,
                      "searchInfoVo.praiseNumStart":None,
                      "searchInfoVo.praiseNumEnd":None,
                      "searchInfoVo.concernNumStart":None,
                      "searchInfoVo.concernNumEnd":None,
                      "searchInfoVo.information.visitState":None, #是否回访，全部是空
                      "searchInfoVo.acceptDateStart":None,
                      "searchInfoVo.acceptDateEnd":None,
                      "searchInfoVo.completedDateStart":None,
                      "searchInfoVo.completedDateEnd":None,                     
                      "searchInfoVo.information.infoType":None, #
                      "searchInfoVo.information.themeContentId":None, #主题id
                      "sidx":"id",
                      "sord":"desc",
                      "rows":20,
                      "page":1
                      }

#主题列表搜索字典
clueThemeListGetDict = {
                        "themeContentVo.infoType":0,
                        "searchOrgId":InitDefaultPara.clueOrgInit['DftQuOrgId'],    
                        "rows":100,
                        "page":1,
                        "sidx":"id",
                        "sord":"desc"
                        } 
#爆料搜索结果查询字典
clueSearchResultCheck = {"address":None,
                         "commentNum":None,
                         "concernNum":None,
                         "contentText":None,
                         "delState":None,
                         "mobile":None,
                         "nickName":None,
                         "praiseNum":None,
                         "score":None,
                         "showState":None,
                         "state":None,
                         "visitState":None
                        }


#转事件参数
clueToIssuePara={
            'issue.id':'',
            'stepId':'',
            'issue.occurOrg.id':InitDefaultPara.orgInit['DftJieDaoOrgId'],
            'issue.createOrg.id':InitDefaultPara.orgInit['DftJieDaoOrgId'],
            'issue.serialNumber':'',
            'inboxIds':'',
            'information.id':'',
            'information.infoType':'0',#0线索，1公告
            'information.officialReply':'',
            'information.nickName':'',
            'issue.selfdomIssuetypeOrgCode':'',
            'issue.subject':'线索转事件主题',
            'selectOrgName':InitDefaultPara.orgInit['DftJieDaoOrg'],
            'issue.occurLocation':'发生地点',
            'issue.occurDate':Time.getCurrentDate(),
            'eatHours':'',
            'eatMinute':'',
            'selectOrgNameByOwner':InitDefaultPara.orgInit['DftJieDaoOrg'],
            'issue.ownerPerson':InitDefaultPara.userInit['DftJieDaoUserXM'],
            'selectedTypes':CommonIntf.getDbQueryResult(dbCommand="select t.id from ISSUETYPES t where t.issuetypename='生活困难救助'"),
            'issueRelatedPeopleNames':'群众',
            'issueRelatedPeopleNameBaks1':'群众',
            'issueRelatedPeopleTelephones':'13111111111',
            'issue.relatePeopleCount':'1',
            'issue.issueKind.id':'',
            'issue.issueContent':''
                }

#说说列表搜索字典
shuoshuoListGetDict = {
                        "searchCasualTalkVo.orgId":InitDefaultPara.clueOrgInit['DftQuOrgId'],
                        "searchCasualTalkVo.themeContentId":"",    
                        "rows":100,
                        "page":1,
                        "sidx":"id",
                        "sord":"desc"
                        }

#说说删除字典
shuoshuoDelDict = {
                        "delInfoRecord.informationId":"",
                        "delInfoRecord.mobile":"",    
                        "delInfoRecord.infoType":5, #5表示说说
                        "delInfoRecord.departmentNo":InitDefaultPara.clueOrgInit['DftQuOrgDepNo'],
                        "chooseRecord":"其他",
                        "delInfoRecord.deleteReason":"其他"
                        }

#说说搜索条件字典
shuoshuoSearchDict = {"searchCasualTalkVo.contentText":None, #说说内容
                      "searchCasualTalkVo.mobile":None,
                      "searchCasualTalkVo.orgId":InitDefaultPara.clueOrgInit['DftQuOrgId'],
                      "searchCasualTalkVo.themeContentId":None,#主题ID，无主题填0，
                      "_search":"false",
                      "rows":20,
                      "page":1,
                      "sidx":"id",
                      "sord":"desc"
                      }

#爆料搜索结果查询字典
shuoshuoSearchResultCheck = {"themeContentName":None,
                         "commentNum":None,
                         "concernNum":None,
                         "contentText":None,
                         "delState":None,
                         "mobile":None,
                         "nickName":None,
                         "praiseNum":None,
                         "score":None,
                         "showState":None,
                         "visitState":None
                        }

#通过后台线索管理新增说说
addShuoShuoByXianSuoGuanLiPara = {
                              "casualTalkVo.casualTalk.mobile":Global.XianSuoDftMobile,
                              "orgId":InitDefaultPara.clueOrgInit['DftQuOrgId'],
                              "casualTalkVo.casualTalk.contentText":""
                              }

#更新说说
updateShuoShuoByXianSuoGuanLiPara = {
                              "casualTalk.title":"",
                              "casualTalk.id":"",
                              "casualTalk.contentText":""
                              }

#平安宣传新增
addPingAnXuanChuanDict = {
                          "mode":"add",
                          "infoType":4, #4为平安宣传
                          "informationVo.information.orgId":InitDefaultPara.clueOrgInit['DftQuOrgId'],
                          "informationVo.information.id":"",
                          "informationVo.information.title":"", #平安宣传标题
                          "informationVo.information.contentText":"", #平安宣传正文
                          }

#修改平安宣传新增
modifyPingAnXuanChuanDict = {
                          "mode":"add",
                          "infoType":"", #4为平安宣传
                          "informationVo.information.orgId":InitDefaultPara.clueOrgInit['DftQuOrgId'],
                          "informationVo.information.id":"",
                          "informationVo.information.title":"", #平安宣传标题
                          "informationVo.information.contentText":"", #平安宣传正文
                          }

#更新平安宣传状态
updatePingAnXuanChuanStateDict = {
                              "ids":"",
                              "showState":"" #0表示不公开，1表示公开，2表示精彩推荐
                              }

#平安宣传搜索字典
pingAnXuanChuanSearchDict = {"searchInfoVo.information.showState":None, #平安宣传状态，可调用ShowState枚举变量
                             "searchInfoVo.information.title":None, #标题
                             "searchInfoVo.information.orgId":InitDefaultPara.clueOrgInit['DftQuOrgId'],
                             "searchInfoVo.information.infoType":4,#4表示平安宣传，
                             "rows":20,
                             "page":1,
                              "sidx":"id",
                              "sord":"desc"
                              }

#平安宣传结果比较字典
pingAnXuanChuanSearchResultCheck = {"contentText":None,
                                     "title":None,
                                     "nickName":None,
                                     "showState":None,
                                    }

#主页精彩推荐结果比较字典
jingCaiTuiJianSearchResult = {
                              "contentText":None,
                              "informationId":None,
                              }

#线索用户认证
enableUserCertifyPara = {
                         "clueMobile":"",
                         "validateCode":""
                         }