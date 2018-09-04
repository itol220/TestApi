# -*- coding:UTF-8 -*-
'''
Created on 2015-11-24

@author: N-133
'''
from __future__ import unicode_literals
from COMMON import Time
from CONFIG import InitDefaultPara
from CONFIG.InitDefaultPara import orgInit, clueOrgInit
from Interface.PingAnJianShe.Common import CommonIntf
from Interface.YunWeiPingTai.XiTongPeiZhi.XiTongPeiZhiPara import InfoType

departmentNo=InitDefaultPara.clueOrgInit['DftQuOrgDepNo']
def enum(**enums):
    return type(str('Enum'), (), enums)
#信息广场线索显示状态，0为公开，1为不公开，2置顶
ClueShowState=enum(OPEN=1,CLOSE=0,TOP=2)
# 信息广场列表参数
informationSquareListPara={
                'tqmobile':'true',
                'departmentNo':departmentNo,
                'themeContentId':'',
                'page':1,
                'rows':200,
#                 'sord':'desc',
#                 'sidx':'id',
#                 'userId':''
                           }
informationSquareListCheckPara={
                'showState':None,#0公开,1未公开,2置顶
                'concernNum':None,
                'reSubmit':None,
                'commentNum':None,
                'publishUserId':None,
                'mobile':None,
                'nickName':None,
                'praiseNum':None,
                'contentText':None
                                }
#转事件参数
culeToIssuePara={
            'issue.id':'',
            'stepId':'',
            'issue.occurOrg.id':orgInit['DftJieDaoOrgId'],
            'issue.createOrg.id':orgInit['DftJieDaoOrgId'],
            'issue.serialNumber':'',
            'inboxIds':'',
            'information.id':'',
            'information.infoType':'0',#0线索，1公告
            'information.officialReply':'',
            'information.nickName':'',
            'issue.selfdomIssuetypeOrgCode':'',
            'issue.subject':'线索转事件',
            'selectOrgName':orgInit['DftJieDaoOrg'],
            'issue.occurLocation':'',
            'issue.occurDate':Time.getCurrentDate(),
            'eatHours':'',
            'eatMinute':'',
            'selectOrgNameByOwner':orgInit['DftJieDaoOrg'],
            'issue.ownerPerson':orgInit['DftJieDaoOrg'],
            'selectedTypes':'8',
            'issueRelatedPeopleNames':'姓名',
            'issueRelatedPeopleNameBaks1':'姓名',
            'issueRelatedPeopleTelephones':'',
            'issue.relatePeopleCount':'3',
            'issue.issueKind.id':'',
            'issue.issueContent':''
                }

#点赞参数
addPraisePara={
            'tqmobile':'true',
            'informationId':'',
            'praiseUserId':''
               }
#点赞列表参数
praiseListPara={
            'tqmobile':'true',
            'userId':'',
            'departmentNo':CommonIntf.getDbQueryResult(dbCommand ="select o.departmentno from organizations o where o.id='%s'"%orgInit['DftJieDaoOrgId']),
            'sidx':'id',
            'sord':'desc',
            'page':'1',
            'rows':'200'
                }
#新增评论参数
addCommentPara={
            'tqmobile':'true',
            'informationId':'',
            'contentText':'评论内容',
            'commentUserId':'',
            'commentType':'',#0评论1回复
            'replyUserId':'',
                }
#评论列表参数
listCommentPara={
            'tqmobile':'true',
            'sidx':'id',
            'sord':'desc',
            'page':'1',
            'rows':'200'
                 }
#新增关注参数
addConPara={
                'tqmobile':'true',
                'informationId':'',
                'concernUserId':'',
                'concernDate':Time.getCurrentDate()
                    }
#获取关键词参数
getHotKeywordPara={
     'tqmobile':'true',
     'departmentNo':departmentNo,
     'infoType':InfoType.BAOLIAO
}

#获取消息列表
getMessageListPara = {
                        "page":"1",
                        "userId":"",
                        "tqmobile":"true",
                        "messageType":"",
                        "isRead":"0",
                        "apiVersion":"3"
                      }

#检查消息列表
checkMessagePara = {
                    "infoState":None,
                    "isRead":None, #0表示未读,1表示已读
                    "content":None, #意见反馈处理意见
                    "inforDelState":None,#是否删除
                    "infoType":None,
                    "messageType":None, #事件状态
                    "commentType":None,
                    "infoContent":None, #意见反馈内容
                    "nickName":None,
                    }