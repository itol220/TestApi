# -*- coding:UTF-8 -*-
'''
Created on 2015-11-24

@author: N-133
'''
from __future__ import unicode_literals
from COMMON import CommonUtil, Time
from CONFIG import Global, InitDefaultPara
from CONFIG.InitDefaultPara import orgInit, userInit
from Interface.PingAnJianShe.ShiJianChuLi import ShiJianChuLiPara, \
    ShiJianChuLiIntf
from Interface.PingAnJianShe.ShiJianChuLi.ShiJianChuLiIntf import dealIssue, \
    deleteAllIssues2
from Interface.XianSuoApp.BaoLiao import XsBaoLiaoIntf, XsBaoLiaoPara
from Interface.XianSuoApp.GongZuoTai import XsGongZuoTaiIntf
from Interface.XianSuoApp.WoDeXinXi import XsMyInformationPara, \
    XsMyInformationIntf
from Interface.XianSuoApp.WoDeXinXi.XsMyInformationPara import MessageSwtich
from Interface.XianSuoApp.XinXiGuangChang import XsInformationSquarePara, \
    XsInformationSquareIntf
from Interface.YunWeiPingTai.XinXiGuanLi import XinXiGuanLiIntf, XinXiGuanLiPara
from Interface.YunWeiPingTai.YunWeiCommon import YunWeiCommonIntf
import copy
import json
import unittest



class XsInformationSquare(unittest.TestCase):

    def setUp(self):
        XsGongZuoTaiIntf.initUser()
#         SystemMgrIntf.initEnv()''
        XsBaoLiaoIntf.deleteAllClues()
        XinXiGuanLiIntf.deleteyunwei()
        deleteAllIssues2()
        pass
    def test_message_userfeedback_01(self):
        """消息中心--意见反馈 -823"""
        #添加意见反馈
        addFeedBackDict = copy.deepcopy(XsMyInformationPara.addUserFeedbackPara)
        addFeedBackDict['userFeedBack']['advice'] = "意见反馈%s" % CommonUtil.createRandomString()
        addFeedBackDict['userFeedBack']['mobile'] = Global.XianSuoDftMobile
        ret = XsMyInformationIntf.add_user_feedback(addFeedBackDict)
        self.assertTrue(ret, '新增意见反馈失败')
        
        #后台回复，先获取反馈意见id
        feedBackId = XinXiGuanLiIntf.get_user_feedback_id_by_content(addFeedBackDict['userFeedBack']['advice'])
        feedBackReply = copy.deepcopy(XinXiGuanLiPara.replyForFeedbackPara)
        feedBackReply['ids'] = feedBackId
#         print feedBackId
        feedBackReply['replyContent'] = "意见反馈回复%s" % CommonUtil.createRandomString()
        ret = XinXiGuanLiIntf.reply_for_user_feedback(feedBackReply)
        self.assertTrue(ret, '回复意见反馈失败')
        
        #消息中心检查消息
        getMessageDict = copy.deepcopy(XsInformationSquarePara.getMessageListPara)
        getMessageDict['userId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from USERS t where t.mobile='%s'" % Global.XianSuoDftMobile)
        
        checkMessageDict = copy.deepcopy(XsInformationSquarePara.checkMessagePara)
        checkMessageDict['infoContent'] = addFeedBackDict['userFeedBack']['advice']
        checkMessageDict['content'] = "您的意见反馈已回答"
        Time.wait(3)
        ret = XsInformationSquareIntf.check_message_in_message_list(checkMessageDict, getMessageDict)
        self.assertTrue(ret, '回复意见检查失败')
        
        #将消息置为已读，先获取消息id
        messageId = XsInformationSquareIntf.get_message_id_by_message_content(addFeedBackDict['userFeedBack']['advice'], getMessageDict)
        ret = XsInformationSquareIntf.set_message_to_readed(messageId)   
        
        #通过详情页检查意见反馈信息
        getFeedbackDetailDict = copy.deepcopy(XsMyInformationPara.getFeedbackDetailPara)
        getFeedbackDetailDict['id'] = feedBackId
        
        checkFeedbackDetailDict = copy.deepcopy(XsMyInformationPara.checkFeedbackDetailPara)
        checkFeedbackDetailDict['advice'] =  addFeedBackDict['userFeedBack']['advice']
        checkFeedbackDetailDict['replyContent'] = feedBackReply['replyContent']
        
        ret = XsMyInformationIntf.check_user_feedback_by_detail(checkFeedbackDetailDict, getFeedbackDetailDict)
        self.assertTrue(ret, '意见反馈详情信息检查失败')
        
        #后台对反馈意见进行修改
        updateFeedbackReply = copy.deepcopy(XinXiGuanLiPara.replyForFeedbackPara) 
        updateFeedbackReply['ids'] = feedBackId
        updateFeedbackReply['replyContent'] = "意见反馈回复修改%s" % CommonUtil.createRandomString()
        ret = XinXiGuanLiIntf.update_feedback_reply_content(updateFeedbackReply)
        
        #客户端检查是否收到意见反馈回复修改消息，预期不会收到
        getMessageDict = copy.deepcopy(XsInformationSquarePara.getMessageListPara)
        getMessageDict['userId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from USERS t where t.mobile='%s'" % Global.XianSuoDftMobile)
        
        checkMessageDict = copy.deepcopy(XsInformationSquarePara.checkMessagePara)
        checkMessageDict['infoContent'] = addFeedBackDict['userFeedBack']['advice']
        checkMessageDict['content'] = "您的意见反馈已回答"
        checkMessageDict['isRead'] = 0
              
        ret = XsInformationSquareIntf.check_message_in_message_list(checkMessageDict, getMessageDict)
        self.assertFalse(ret, '修改回复信息，消息列表也收到消息')
        pass
    
    def test_message_issue_deal_02(self):
        """ 消息中心-事件流转状态消息提醒-822"""
        #手机端新增爆料
        newClueOne = copy.deepcopy(XsBaoLiaoPara.xinZeng2) 
        responseDict = XsBaoLiaoIntf.addXianSuo(newClueOne)
        self.assertTrue(responseDict.result, '新增线索失败')
        
        #爆料转事件
        clueToIssueDict = copy.deepcopy(XsInformationSquarePara.culeToIssuePara)
        clueToIssueDict['information.id'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from INFORMATIONS t where t.contenttext='%s'" % newClueOne['information']['contentText'])
        clueToIssueDict['issue.subject'] = "线索转事件%s" % CommonUtil.createRandomString()
        clueToIssueDict['issue.occurLocation'] = newClueOne['information']['address']
        clueToIssueDict['issue.issueContent'] = newClueOne['information']['contentText']
        clueToIssueDict['information.nickName'] = Global.XianSuoDftMobileNick
        issueRet = XsInformationSquareIntf.clueToIssue(clueToIssueDict)
        issueDict=json.loads(issueRet.text)
        self.assertTrue(responseDict.result, '转事件失败')
        
        #消息中心查看是否有事件受理提醒
        getMessageDict = copy.deepcopy(XsInformationSquarePara.getMessageListPara)
        getMessageDict['userId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from USERS t where t.mobile='%s'" % Global.XianSuoDftMobile)
        
        checkMessageDict = copy.deepcopy(XsInformationSquarePara.checkMessagePara)
        checkMessageDict['infoContent'] = "%s 受理" % InitDefaultPara.orgInit['DftJieDaoOrg']
        checkMessageDict['content'] = newClueOne['information']['contentText']
        Time.wait(3)
        ret = XsInformationSquareIntf.check_message_in_message_list(checkMessageDict, getMessageDict)
        self.assertTrue(ret, '未收到线索转事件受理提醒')
        
        #后台事件办理中
        dealIssuePara = copy.deepcopy(ShiJianChuLiPara.dealIssuePara)
        dealIssuePara['operation.dealOrg.id']=InitDefaultPara.orgInit['DftJieDaoOrgId']
        dealIssuePara['operation.issue.id']=issueDict['issueId']
        dealIssuePara['keyId']=issueDict['issueStepId']    
        dealIssuePara['operation.dealUserName']=InitDefaultPara.userInit['DftJieDaoUserXM']
        dealIssuePara['operation.mobile']=InitDefaultPara.userInit['DftJieDaoUserSJ']
        dealIssuePara['operation.content']='处理意见_事件办理中'       
        dealIssuePara['dealCode']='1'
        result=ShiJianChuLiIntf.dealIssue(issueDict=dealIssuePara)
        
        #消息中心查看是否有事件办理中提醒
        getMessageDict = copy.deepcopy(XsInformationSquarePara.getMessageListPara)
        getMessageDict['userId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from USERS t where t.mobile='%s'" % Global.XianSuoDftMobile)
        
        checkMessageDict = copy.deepcopy(XsInformationSquarePara.checkMessagePara)
        checkMessageDict['infoContent'] = "%s 办理中 " % InitDefaultPara.orgInit['DftJieDaoOrg']
        checkMessageDict['content'] = newClueOne['information']['contentText']
        ret = XsInformationSquareIntf.check_message_in_message_list(checkMessageDict, getMessageDict)
        Time.wait(3)
        self.assertTrue(ret, '未收到线索转事件办理中提醒')
        
        #事件交办
        issueAssign=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)
        issueAssign['operation.dealOrg.id']=orgInit['DftJieDaoOrgId']
        issueAssign['operation.issue.id']=issueDict['issueId']
        issueAssign['keyId']=issueDict['issueStepId']    
        issueAssign['operation.dealUserName']=userInit['DftJieDaoUserXM']
        issueAssign['operation.mobile']=userInit['DftJieDaoUserSJ']
        issueAssign['operation.content']='处理意见_普通交办事件'
        issueAssign['operation.targeOrg.id']=orgInit['DftSheQuOrgId']    
        issueAssign['dealCode']='21'
        issueAssign['themainOrgid']=orgInit['DftSheQuOrgId']
        result4=ShiJianChuLiIntf.dealIssue(issueDict=issueAssign)
        self.assertTrue(result4.result, '交办失败')
        
        #检查是否有交办提醒
        getMessageDict = copy.deepcopy(XsInformationSquarePara.getMessageListPara)
        getMessageDict['userId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from USERS t where t.mobile='%s'" % Global.XianSuoDftMobile)
        
        checkMessageDict = copy.deepcopy(XsInformationSquarePara.checkMessagePara)
        checkMessageDict['infoContent'] = "%s 交办%s " % (InitDefaultPara.orgInit['DftJieDaoOrg'],InitDefaultPara.orgInit['DftSheQuOrg'])
        checkMessageDict['content'] = newClueOne['information']['contentText']
        Time.wait(3)
        ret = XsInformationSquareIntf.check_message_in_message_list(checkMessageDict, getMessageDict)
        self.assertTrue(ret, '未收到线索转事件办理中提醒')
        
        #社区受理事件
        acceptPara={
             'operation.dealOrg.id':orgInit['DftSheQuOrgId'],
             'operation.issue.id':issueDict['issueId'],
             'operation.dealUserName':userInit['DftSheQuUserXM'],
             'operation.mobile':userInit['DftSheQuUserSJ'],
             'dealCode':'61',
             'keyId':issueAssign['keyId'] +1
             }
        result50=dealIssue(issueDict=acceptPara, username=userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(result50.result, '社区受理失败')
        
        #事件上报
        issueReport=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)
        issueReport['operation.dealOrg.id']=orgInit['DftSheQuOrgId']
        issueReport['operation.issue.id']=issueDict['issueId']
        issueReport['keyId']=issueDict['issueStepId']+1
        issueReport['operation.dealUserName']=userInit['DftSheQuUserXM']
        issueReport['operation.mobile']=userInit['DftSheQuUserSJ']
        issueReport['operation.content']='处理意见_上报事件'
        issueReport['operation.targeOrg.id']=orgInit['DftJieDaoOrgId']
        issueReport['themainOrgid']=orgInit['DftJieDaoOrgId']        
        issueReport['dealCode']='41'#上报
        result5=ShiJianChuLiIntf.dealIssue(issueDict=issueReport,username=userInit['DftSheQuUser'])
        self.assertTrue(result5.result, '上报失败')
        
        #检查是否有上报提醒
        getMessageDict = copy.deepcopy(XsInformationSquarePara.getMessageListPara)
        getMessageDict['userId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from USERS t where t.mobile='%s'" % Global.XianSuoDftMobile)
        
        checkMessageDict = copy.deepcopy(XsInformationSquarePara.checkMessagePara)
        checkMessageDict['infoContent'] = "%s 上报%s " % (InitDefaultPara.orgInit['DftSheQuOrg'],InitDefaultPara.orgInit['DftJieDaoOrg'])
        checkMessageDict['content'] = newClueOne['information']['contentText']
        Time.wait(3)
        ret = XsInformationSquareIntf.check_message_in_message_list(checkMessageDict, getMessageDict)
        self.assertTrue(ret, '未收到转事件上报提醒')
        
        #街道受理
        acceptParaJD={
             'operation.dealOrg.id':orgInit['DftJieDaoOrgId'],
             'operation.issue.id':issueDict['issueId'],
             'operation.dealUserName':userInit['DftJieDaoUserXM'],
             'operation.mobile':userInit['DftJieDaoUserSJ'],
             'dealCode':'61',
             'keyId':issueAssign['keyId']+2
             }
        result60=ShiJianChuLiIntf.dealIssue(issueDict=acceptParaJD)
        self.assertTrue(result60.result, '街道受理失败')
        
        #事件办结
        issueClose=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)        
        issueClose['operation.dealOrg.id']=orgInit['DftJieDaoOrgId']
        issueClose['operation.issue.id']=issueDict['issueId']
        issueClose['keyId']=issueDict['issueStepId']+2
        issueClose['operation.dealUserName']=userInit['DftJieDaoUserXM']
        issueClose['operation.mobile']=userInit['DftJieDaoUserSJ']
        issueClose['operation.content']='处理意见_结案'       
        issueClose['dealCode']='31'#办结
        result6=ShiJianChuLiIntf.dealIssue(issueDict=issueClose)
        self.assertTrue(result6.result,'办结失败')
        
        #验证是否有结案消息
        getMessageDict = copy.deepcopy(XsInformationSquarePara.getMessageListPara)
        getMessageDict['userId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from USERS t where t.mobile='%s'" % Global.XianSuoDftMobile)
        
        checkMessageDict = copy.deepcopy(XsInformationSquarePara.checkMessagePara)
        checkMessageDict['infoContent'] = "%s 办结" % InitDefaultPara.orgInit['DftJieDaoOrg']
        checkMessageDict['content'] = newClueOne['information']['contentText']
        Time.wait(3)
        ret = XsInformationSquareIntf.check_message_in_message_list(checkMessageDict, getMessageDict)
        self.assertTrue(ret, '未收到事件办结提醒')
        
        pass
    def test_comment_message_03(self):
        """消息中心评论、回复评论-821"""
        #初始化一个新账号
        newMobile = "13588806928"
        XsGongZuoTaiIntf.initUser(mobile=newMobile)
        
        #默认账号新增爆料
        addClueByDftUser = copy.deepcopy(XsBaoLiaoPara.xinZeng2) 
        responseDict = XsBaoLiaoIntf.addXianSuo(addClueByDftUser)
        self.assertTrue(responseDict.result, '新增线索失败')
        
        #新账号评论该爆料
        clueId = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from INFORMATIONS t where t.contenttext='%s'" % addClueByDftUser['information']['contentText'])
        addCommentDict = copy.deepcopy(XsBaoLiaoPara.addCommentForCluePara)
        addCommentDict['informationId'] = clueId
        addCommentDict['contentText'] = "B评论A%s" % CommonUtil.createRandomString()
        addCommentDict['commentUserId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from USERS t where t.mobile='%s'" % newMobile)
        ret = XsBaoLiaoIntf.add_comment_for_clue(addCommentDict, mobile=newMobile)
        self.assertTrue(ret, '新账号新增评论失败')
        
        #检查默认账号是否收到
        getMessageDict = copy.deepcopy(XsInformationSquarePara.getMessageListPara)
        getMessageDict['userId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from USERS t where t.mobile='%s'" % Global.XianSuoDftMobile)
        
        checkMessageDict = copy.deepcopy(XsInformationSquarePara.checkMessagePara)
        checkMessageDict['infoContent'] = addClueByDftUser['information']['contentText']
        checkMessageDict['content'] = addCommentDict['contentText']
        checkMessageDict['nickName'] = 'nick_%s' % newMobile
        ret = XsInformationSquareIntf.check_message_in_message_list(checkMessageDict, getMessageDict)
        self.assertTrue(ret, '未收到评论消息提醒')
        
        #将消息开关关闭
        setMessageSwtichDict = copy.deepcopy(XsMyInformationPara.updateMessageSwitchPara)
        setMessageSwtichDict['id'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from USERS t where t.mobile='%s'" % Global.XianSuoDftMobile)
        setMessageSwtichDict['messageSwit'] = MessageSwtich.OFF
        ret = XsMyInformationIntf.set_message_push_switch(setMessageSwtichDict)
        
        #新账号重新评论
        addCommentDict = copy.deepcopy(XsBaoLiaoPara.addCommentForCluePara)
        addCommentDict['informationId'] = clueId
        addCommentDict['contentText'] = "B再次评论A%s" % CommonUtil.createRandomString()
        addCommentDict['commentUserId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from USERS t where t.mobile='%s'" % newMobile)
        ret = XsBaoLiaoIntf.add_comment_for_clue(addCommentDict, mobile=newMobile)
        self.assertTrue(ret, '新账号再次新增评论失败')
        
        #再次检查默认账号是否收到新消息(因为消息开关只控制对系统的推送功能，因此接口无法验证，此步略过)
        
        #消息开关重新开启
        setMessageSwtichDict = copy.deepcopy(XsMyInformationPara.updateMessageSwitchPara)
        setMessageSwtichDict['id'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from USERS t where t.mobile='%s'" % Global.XianSuoDftMobile)
        setMessageSwtichDict['messageSwit'] = MessageSwtich.ON
        ret = XsMyInformationIntf.set_message_push_switch(setMessageSwtichDict)
        
        #默认用户回复新用户的评论
        addCommentReplyDict = copy.deepcopy(XsBaoLiaoPara.addCommentForCluePara)
        addCommentReplyDict['informationId'] = clueId
        addCommentReplyDict['contentText'] = "A回复B的评论%s" % CommonUtil.createRandomString()
        addCommentReplyDict['replyUserId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from USERS t where t.mobile='%s'" % newMobile)
        addCommentReplyDict['commentUserId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from USERS t where t.mobile='%s'" % Global.XianSuoDftMobile)
        addCommentReplyDict['commentType'] = 1
        ret = XsBaoLiaoIntf.add_comment_for_clue(addCommentReplyDict)
        self.assertTrue(ret, '默认账号回复新账号评论失败')
        
        #检查新账号是否收到消息
        getMessageDict = copy.deepcopy(XsInformationSquarePara.getMessageListPara)
        getMessageDict['userId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from USERS t where t.mobile='%s'" % newMobile)
        
        checkMessageDict = copy.deepcopy(XsInformationSquarePara.checkMessagePara)
        checkMessageDict['infoContent'] = addClueByDftUser['information']['contentText']
        checkMessageDict['content'] = addCommentReplyDict['contentText']
        checkMessageDict['nickName'] = Global.XianSuoDftMobileNick
        ret = XsInformationSquareIntf.check_message_in_message_list(checkMessageDict, getMessageDict)
        self.assertTrue(ret, '新用户未收到默认用户的评论回复消息')
        
        #新用户继续回复默认用户的回复
        addCommentAgainDict = copy.deepcopy(XsBaoLiaoPara.addCommentForCluePara)
        addCommentAgainDict['informationId'] = clueId
        addCommentAgainDict['contentText'] = "B重复回复A的评论%s" % CommonUtil.createRandomString()
        addCommentAgainDict['commentUserId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from USERS t where t.mobile='%s'" % newMobile)
        addCommentAgainDict['replyUserId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from USERS t where t.mobile='%s'" % Global.XianSuoDftMobile)
        addCommentAgainDict['commentType'] = 1        
        ret = XsBaoLiaoIntf.add_comment_for_clue(addCommentAgainDict, mobile=newMobile)
        self.assertTrue(ret, '新账号再次回复默认用户的回复失败')
        
        #默认用户再次检查是否收到新消息
        getMessageDict = copy.deepcopy(XsInformationSquarePara.getMessageListPara)
        getMessageDict['userId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from USERS t where t.mobile='%s'" % Global.XianSuoDftMobile)
        
        checkMessageDict = copy.deepcopy(XsInformationSquarePara.checkMessagePara)
        checkMessageDict['infoContent'] = addClueByDftUser['information']['contentText']
        checkMessageDict['content'] = addCommentAgainDict['contentText']
        checkMessageDict['nickName'] = "nick_%s" % newMobile
        ret = XsInformationSquareIntf.check_message_in_message_list(checkMessageDict, getMessageDict)
        self.assertTrue(ret, '默认用户未收到新用户的回复的回复消息')
        pass
    
#     新增线索
#     def test_XsInformationSquare_01(self):
#         """事件流转步骤显示"""
#         addPara=copy.deepcopy(xinZeng2)
#         response=addXianSuo(addPara)
#         self.assertTrue(response.result,'新增线索失败！')
#         listPara={
#                 'tqmobile':'true',
#                 'page':'1',
#                 'rows':'100'
#                   }
#         lsr=viewSchedule(para=listPara)
# #         print 'lsr:'+lsr.text
#         lsrDict=json.loads(lsr.text)
#         #后台将该线索公开
#         showStatePara={
#                        'ids':lsrDict['response']['module']['rows'][0]['information']['id'],
#                        'showState':1
#                        }
#         r=setClueShowState(para=showStatePara)
#         self.assertTrue(r.result, '设置线索分享状态失败！')
#         #设置官方回复内容
#         officialReplyPara={
#                        'ids':lsrDict['response']['module']['rows'][0]['information']['id'],
#                        'officialReply':'官方回复内容'
#         }
#         officialReply(para=officialReplyPara)
#         #获取信息广场列表
#         squareListPara=copy.deepcopy(informationSquareListPara)
#         rs=getUserLogin()
#         squareListPara['userId']=rs['response']['module']['id']
#         response=getClueList(para=squareListPara)
#         responseDict=json.loads(response.text)
#         #验证官方回复
#         Log.LogOutput(message='验证官方回复是否正确')
#         checkOfficialReplyPara={'officialReply':officialReplyPara['officialReply']}
#         result=checkDictInClueList(checkPara=checkOfficialReplyPara,listPara=squareListPara)
#         self.assertTrue(result, '官方回复验证失败')
#         Log.LogOutput(message='官方回复验证通过')
#         #验证步骤
#         stepPara={
#                         'tqmobile':'true',
#                         'informationId':responseDict['response']['module']['rows'][0]['information']['id']
#                         }
#         checkPara11={
#                     'orgName':orgInit['DftJieDaoOrg'],
#                     'state':0
#                     }
#         checkPara12={
#                     'orgName':orgInit['DftJieDaoOrg'],
#                     'state':2
#                     }
#         result11=checkDictInInforSteps(checkPara=checkPara11,stepPara=stepPara)
#         result12=checkDictInInforSteps(checkPara=checkPara12,stepPara=stepPara)
#         self.assertTrue(result11, '新增验证失败')
#         self.assertTrue(result12, '结案验证失败')
#         #删除线索，重新新增
#         XsBaoLiaoIntf.deleteAllClues()
#         addXianSuo(addPara)
#         lsr=viewSchedule(para=listPara)
#         lsrDict=json.loads(lsr.text)
#         #后台将该线索公开
#         showStatePara={
#                        'ids':lsrDict['response']['module']['rows'][0]['information']['id'],
#                        'showState':1
#                        }
#         setClueShowState(para=showStatePara)
#         #转事件,街道层级
#         addIssuePara=copy.deepcopy(culeToIssuePara)
#         addIssuePara['information.id']=lsrDict['response']['module']['rows'][0]['information']['id']
#         addIssuePara['information.nickName']=lsrDict['response']['module']['rows'][0]['information']['nickName']
#         addIssuePara['issue.occurLocation']=lsrDict['response']['module']['rows'][0]['information']['address']
#         addIssuePara['issue.issueContent']=lsrDict['response']['module']['rows'][0]['information']['contentText']
# #         addIssuePara
#         isRes=clueToIssue(para=addIssuePara)
#         isResDict=json.loads(isRes.text)
#         #获取信息广场列表
#         rs=getUserLogin()
#         squareListPara['userId']=rs['response']['module']['id']
#         response=getClueList(para=squareListPara)
#         responseDict=json.loads(response.text)
#         stepPara['informationId']=responseDict['response']['module']['rows'][0]['information']['id']
#         checkPara21={
#                     'orgName':orgInit['DftJieDaoOrg'],
#                     'state':0#新增
#                     }
#         checkPara22={
#                     'orgName':orgInit['DftJieDaoOrg'],
#                     'state':1#受理
#                     }
#         result21=checkDictInInforSteps(checkPara=checkPara21,stepPara=stepPara)
#         result22=checkDictInInforSteps(checkPara=checkPara22,stepPara=stepPara)
#         self.assertTrue(result21, '新增验证失败')
#         self.assertTrue(result22, '受理验证失败')
#         #事件处理中
#         issuePara=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)
#         issuePara['operation.dealOrg.id']=orgInit['DftJieDaoOrgId']
#         issuePara['operation.issue.id']=isResDict['issueId']
#         issuePara['keyId']=isResDict['issueStepId']    
#         issuePara['operation.dealUserName']=userInit['DftJieDaoUserXM']
#         issuePara['operation.mobile']=userInit['DftJieDaoUserSJ']
#         issuePara['operation.content']='处理意见_事件办理中'       
#         issuePara['dealCode']='1'
#         result=dealIssue(issueDict=issuePara)
#         
#         #验证步骤信息
#         checkPara31={
#                     'orgName':orgInit['DftJieDaoOrg'],
#                     'state':0#新增
#                     }
#         checkPara32={
#                     'orgName':orgInit['DftJieDaoOrg'],
#                     'state':1#受理
#                     }
#         checkPara33={
#                     'orgName':orgInit['DftJieDaoOrg'],
#                     'state':3,#办理中
#                     'replyContent':'测试自动化街道 办理中 '
#                     }
#         stepRes=getClueStepsInfo(para=stepPara)
#         stepResDict=json.loads(stepRes.text)
#         innerPara={
#                    'tqmobile':'true',
#                    'stepId':stepResDict['response']['module']['informationSteps'][0]['id']
#                    }
#         r=getClueInnerStepsInfo(para=innerPara)
#         self.assertTrue(r.result, '获取线索内部步骤信息失败')
#         checkPara34={'opinion':issuePara['operation.content']}
#         result31=checkDictInInforSteps(checkPara=checkPara31,stepPara=stepPara)
#         result32=checkDictInInforSteps(checkPara=checkPara32,stepPara=stepPara)
#         result33=checkDictInInforSteps(checkPara=checkPara33,stepPara=stepPara)
#         result34=checkDictInInnerInforSteps(checkPara=checkPara34,innerStepPara=innerPara)
#         self.assertTrue(result31, '新增验证失败')
#         self.assertTrue(result32, '受理验证失败')
#         self.assertTrue(result33, '办理中验证失败')
#         self.assertTrue(result34, '办理中处理意见验证失败')
#         #交办事件
#         issuePara2=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)
#         issuePara2['operation.dealOrg.id']=orgInit['DftJieDaoOrgId']
#         issuePara2['operation.issue.id']=isResDict['issueId']
#         issuePara2['keyId']=isResDict['issueStepId']    
#         issuePara2['operation.dealUserName']=userInit['DftJieDaoUserXM']
#         issuePara2['operation.mobile']=userInit['DftJieDaoUserSJ']
#         issuePara2['operation.content']='处理意见_普通交办事件'
#         issuePara2['operation.targeOrg.id']=orgInit['DftSheQuOrgId']    
#         issuePara2['dealCode']='21'
#         issuePara2['themainOrgid']=orgInit['DftSheQuOrgId']
#         result4=dealIssue(issueDict=issuePara2)
#         self.assertTrue(result4.result, '交办失败')
#         
#         checkPara41={
#                     'orgName':orgInit['DftJieDaoOrg'],
#                     'state':0#新增
#                     }
#         checkPara42={
#                     'orgName':orgInit['DftJieDaoOrg'],
#                     'state':1#受理
#                     }
#         checkPara43={
#                     'orgName':orgInit['DftJieDaoOrg'],
#                     'state':3,#办理中
#                     'replyContent':'测试自动化街道 交办测试自动化社区 '
#                     }
#         checkPara44={'opinion':issuePara2['operation.content']}
#         #验证步骤信息
#         result41=checkDictInInforSteps(checkPara=checkPara41,stepPara=stepPara)
#         result42=checkDictInInforSteps(checkPara=checkPara42,stepPara=stepPara)
#         result43=checkDictInInforSteps(checkPara=checkPara43,stepPara=stepPara)
#         result44=checkDictInInnerInforSteps(checkPara=checkPara44,innerStepPara=innerPara)
#         self.assertTrue(result41, '新增验证失败')
#         self.assertTrue(result42, '受理验证失败')
#         self.assertTrue(result43, '交办验证失败')
#         self.assertTrue(result44, '交办处理意见验证失败')
#         #社区受理事件
#         acceptPara={
#              'operation.dealOrg.id':orgInit['DftSheQuOrgId'],
#              'operation.issue.id':issuePara2['operation.issue.id'],
#              'operation.dealUserName':userInit['DftSheQuUserXM'],
#              'operation.mobile':userInit['DftSheQuUserSJ'],
#              'dealCode':'61',
#              'keyId':issuePara2['keyId']+1
#              }
#         result50=dealIssue(issueDict=acceptPara, username=userInit['DftSheQuUser'], password='11111111')
#         self.assertTrue(result50.result, '社区受理失败')
#         #社区上报
#         sIssuePara3=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)
#         sIssuePara3['operation.dealOrg.id']=orgInit['DftSheQuOrgId']
#         sIssuePara3['operation.issue.id']=isResDict['issueId']
#         sIssuePara3['keyId']=isResDict['issueStepId']+1
#         sIssuePara3['operation.dealUserName']=userInit['DftSheQuUserXM']
#         sIssuePara3['operation.mobile']=userInit['DftSheQuUserSJ']
#         sIssuePara3['operation.content']='处理意见_上报事件'
#         sIssuePara3['operation.targeOrg.id']=orgInit['DftJieDaoOrgId']
#         sIssuePara3['themainOrgid']=orgInit['DftJieDaoOrgId']        
#         sIssuePara3['dealCode']='41'#上报
#         result5=dealIssue(issueDict=sIssuePara3,username=userInit['DftSheQuUser'])
#         self.assertTrue(result5.result, '上报失败')
#         #验证步骤和办理意见
#         checkPara51={
#                     'orgName':orgInit['DftJieDaoOrg'],
#                     'state':0#新增
#                     }
#         checkPara52={
#                     'orgName':orgInit['DftJieDaoOrg'],
#                     'state':1#受理
#                     }
#         checkPara53={
#                     'orgName':orgInit['DftSheQuOrg'],
#                     'state':3,#办理中、上报
#                     'replyContent':'测试自动化社区 上报测试自动化街道 '
#                     }
#         checkPara54={'opinion':issuePara2['operation.content']}
#         #验证步骤信息
#         result51=checkDictInInforSteps(checkPara=checkPara51,stepPara=stepPara)
#         result52=checkDictInInforSteps(checkPara=checkPara52,stepPara=stepPara)
#         result53=checkDictInInforSteps(checkPara=checkPara53,stepPara=stepPara)
#         result54=checkDictInInnerInforSteps(checkPara=checkPara54,innerStepPara=innerPara)
#         self.assertTrue(result51, '新增验证失败')
#         self.assertTrue(result52, '受理验证失败')
#         self.assertTrue(result53, '交办验证失败')
#         self.assertTrue(result54, '交办处理意见验证失败')
#         #设置官方回复内容
#         officialReplyPara2={
#                        'ids':lsrDict['response']['module']['rows'][0]['information']['id'],
#                        'officialReply':'官方回复内容更新为大家好'
#         }
#         officialReply(para=officialReplyPara2)
#         #再次官方回复
#         Log.LogOutput(message='验证第二次官方回复是否正确')
#         checkOfficialReplyPara2={'officialReply':officialReplyPara2['officialReply']}
#         result=checkDictInClueList(checkPara=checkOfficialReplyPara2,listPara=squareListPara)
#         self.assertTrue(result, '第二次官方回复验证失败')
#         Log.LogOutput(message='第二次官方回复验证通过')
#         #街道受理
#         acceptPara2={
#              'operation.dealOrg.id':orgInit['DftJieDaoOrgId'],
#              'operation.issue.id':issuePara2['operation.issue.id'],
#              'operation.dealUserName':userInit['DftJieDaoUserXM'],
#              'operation.mobile':userInit['DftJieDaoUserSJ'],
#              'dealCode':'61',
#              'keyId':issuePara2['keyId']+2
#              }
#         result60=dealIssue(issueDict=acceptPara2)
#         self.assertTrue(result60.result, '街道受理失败')
#         #街道办结
#         sIssuePara4=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)        
#         sIssuePara4['operation.dealOrg.id']=orgInit['DftJieDaoOrgId']
#         sIssuePara4['operation.issue.id']=isResDict['issueId']
#         sIssuePara4['keyId']=isResDict['issueStepId']+2
#         sIssuePara4['operation.dealUserName']=userInit['DftJieDaoUserXM']
#         sIssuePara4['operation.mobile']=userInit['DftJieDaoUserSJ']
#         sIssuePara4['operation.content']='处理意见_结案'       
#         sIssuePara4['dealCode']='31'#办结
#         result6=dealIssue(issueDict=sIssuePara4)
#         self.assertTrue(result6.result,'办结失败')
#         
#         #验证步骤和办理意见
#         checkPara61={
#                     'orgName':orgInit['DftJieDaoOrg'],
#                     'state':0#新增
#                     }
#         checkPara62={
#                     'orgName':orgInit['DftJieDaoOrg'],
#                     'state':1#受理
#                     }
#         checkPara63={
#                     'orgName':orgInit['DftJieDaoOrg'],
#                     'state':3,#办理中、上报
#                     'replyContent':'测试自动化街道 受理 '
#                     }
#         checkPara64={
#                      'orgName':orgInit['DftJieDaoOrg'],
#                      'state':2,
#                      'replyContent':'处理意见_结案'
#                      }
#         checkPara65={'description':'测试自动化街道 受理 '}
#         #验证步骤信息
#         result61=checkDictInInforSteps(checkPara=checkPara61,stepPara=stepPara)
#         result62=checkDictInInforSteps(checkPara=checkPara62,stepPara=stepPara)
#         result63=checkDictInInforSteps(checkPara=checkPara63,stepPara=stepPara)
#         result64=checkDictInInforSteps(checkPara=checkPara64,stepPara=stepPara)
#         result65=checkDictInInnerInforSteps(checkPara=checkPara65,innerStepPara=innerPara)
#         self.assertTrue(result61, '新增验证失败')
#         self.assertTrue(result62, '受理验证失败')
#         self.assertTrue(result63, '交办验证失败')
#         self.assertTrue(result64, '交办验证失败')
#         self.assertTrue(result65, '交办处理意见验证失败')
#         #点赞
#         addpara=copy.deepcopy(addPraisePara)
#         addpara['informationId']=responseDict['response']['module']['rows'][0]['information']['id']
#         addpara['praiseUserId']=rs['response']['module']['id']
#         addPraise(para=addpara)
#         #验证点赞是否在我的点赞列表中显示
#         checkPara0={
#                    'nickName':responseDict['response']['module']['rows'][0]['information']['nickName'],
#                    'contentText':xinZeng2['information']['contentText'],
#                    'praiseNum':1
#                    }
#         listPara0=copy.deepcopy(praiseListPara)
#         listPara0['userId']=rs['response']['module']['id']
#         result7=checkInMyPraiseList(checkPara=checkPara0,listPara=listPara0)
#         self.assertTrue(result7, '我的点赞列表验证失败')
#         Log.LogOutput(message='我的点赞列表验证成功')
#         #对已点赞的数据再次点赞
#         result8=addPraise(para=addpara)
#         self.assertFalse(result8.result,'再次点赞没有返回错误信息')
#         #评论
#         addcompara=copy.deepcopy(addCommentPara)
#         addcompara['informationId']=responseDict['response']['module']['rows'][0]['information']['id']
#         addcompara['commentUserId']=rs['response']['module']['id']
#         addcompara['commentType']=0
#         result9=addComment(para=addcompara)
#         self.assertTrue(result9.text, '新增评论失败')
#         checkComPara={
#                       'contentText':addcompara['contentText'],
#                       'informationId':addcompara['informationId'],
#                       'commentUserId':addcompara['commentUserId'],
#                       'commentType':addcompara['commentType']
#                       }
#         listComPara=copy.deepcopy(listCommentPara)
#         result10=checkInMyCommentList(checkPara=checkComPara,listPara=listComPara)
#         self.assertTrue(result10, '我的评论列表验证失败')
#         listComPara['informationId']=addcompara['informationId']
#         result11=checkInCommentList(checkPara=checkComPara,listPara=listComPara)
#         self.assertTrue(result11, '评论列表验证失败')
#         #新增关注
#         addConPara={
#                 'tqmobile':'true',
#                 'informationId':responseDict['response']['module']['rows'][0]['information']['id'],
#                 'concernUserId':rs['response']['module']['id'],
#                 'concernDate':Time.getCurrentDate()
#                     }
#         result12=addConcern(para=addConPara)
#         self.assertTrue(result12.result, '新增关注失败')
#         checkConPara={
#                       'id':responseDict['response']['module']['rows'][0]['information']['id'],
#                       'concernNum':1
#                       }
#         listConPara={
#                 'tqmobile':'true',
#                 'sidx':"id",
#                 'sord':"desc",
#                 'page':1,
#                 'rows':200
#                      }
#         result13=checkInConcernList(checkPara=checkConPara,listPara=listConPara)
#         self.assertTrue(result13, '关注列表验证失败')
#         cancelConPara={
#                 'tqmobile':'true',
#                 'informationId':responseDict['response']['module']['rows'][0]['information']['id'],
#                 'concernUserId':rs['response']['module']['id']
#                        }
#         result14=cancelConcern(para=cancelConPara)
#         self.assertTrue(result14.result, '取消关注失败')
#         result15=checkInConcernList(checkPara=checkConPara,listPara=listConPara)
#         self.assertFalse(result15, '取消关注验证失败')
#         pass     
    def tearDown(self):
        pass    
    
    
if __name__ == "__main__":
    suite = unittest.TestSuite()
    
#     suite.addTest(XsInformationSquare("test_message_userfeedback_01"))
    suite.addTest(XsInformationSquare("test_message_issue_deal_02"))
#     suite.addTest(XsInformationSquare("test_comment_message_03"))
    
#     suite.addTest(XsInformationSquare("test_XsInformationSquare_01"))
    results = unittest.TextTestRunner().run(suite)
    pass    