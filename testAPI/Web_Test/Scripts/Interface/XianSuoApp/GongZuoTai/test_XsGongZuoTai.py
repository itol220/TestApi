# -*- coding:UTF-8 -*-
'''
Created on 2015-11-24

@author: N-133
'''
from __future__ import unicode_literals
from COMMON import Log, CommonUtil
from CONFIG import Global, InitDefaultPara
from CONFIG.InitDefaultPara import orgInit, userInit
from Interface.PingAnJianShe.Common import CommonIntf
from Interface.PingAnJianShe.ShiJianChuLi import ShiJianChuLiPara
from Interface.PingAnJianShe.ShiJianChuLi.ShiJianChuLiIntf import dealIssue
from Interface.PingAnJianShe.SystemMgr import SystemMgrIntf
from Interface.XianSuoApp.BaoLiao import XsBaoLiaoIntf, XsBaoLiaoPara
from Interface.XianSuoApp.BaoLiao.XsBaoLiaoIntf import viewSchedule, addXianSuo
from Interface.XianSuoApp.BaoLiao.XsBaoLiaoPara import xinZeng2, XinZeng
from Interface.XianSuoApp.GongZuoTai import XsGongZuoTaiIntf, XsGongZuoTaiPara
from Interface.XianSuoApp.GongZuoTai.XsGongZuoTaiIntf import addUser, \
    getMessageBoxUnReadCount, createRandomNumber, addClueWithSpecialWay
from Interface.XianSuoApp.WoDeXinXi import XsMyInformationPara, \
    XsMyInformationIntf
from Interface.XianSuoApp.WoDeXinXi.XsMyInformationIntf import encodeToMd5
from Interface.XianSuoApp.XinXiGuangChang import XsInformationSquareIntf
from Interface.XianSuoApp.XinXiGuangChang.XsInformationSquareIntf import \
    setClueShowState, clueToIssue, addComment
from Interface.XianSuoApp.XinXiGuangChang.XsInformationSquarePara import \
    culeToIssuePara, addCommentPara
from Interface.XianSuoApp.xianSuoHttpCommon import desEncrypt, getLoginSid
from Interface.YunWeiPingTai.YunWeiCommon import YunWeiCommonIntf
import copy
import json
import time
import unittest


class XsGongZuoTai(unittest.TestCase):

    def setUp(self):
#         SystemMgrIntf.initEnv()''
        #删除线索信息
        XsBaoLiaoIntf.deleteAllClues()
        #清空消息列表        
        #删除用户'12345678901'
        if Global.simulationEnvironment is False:
            XsGongZuoTaiIntf.deleteUserFromDb(mobile='12345678901')
        XsGongZuoTaiIntf.initUser()
        pass
    def test_user_regist_01(self):
        '''用户注册主流程-814'''
        try:
            #产生一个手机随机号码
            registMobile='123%s'%str(createRandomNumber(length=8))
            count=YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand="select count(*)  from users w where w.mobile='%s'" % registMobile)
            while count>=1:
                registMobile='123%s'%str(createRandomNumber(length=8))
                count=YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand="select count(*)  from users w where w.mobile='%s'" % registMobile)
            #获取验证码
            #调用获取验证码方法
            XsGongZuoTaiIntf.getValidateCode(mobile=registMobile)
            #此后验证码用123456
            
            #不输入验证码注册
    #         registMobile = '12345678901'
            para2=copy.deepcopy(XsGongZuoTaiPara.userAddPara)
            para2['mobile'] = registMobile
            para2['validateCode'] = ''
            para2['mobileKey'] = createRandomNumber(length=15)
            desPara={
                     'key':time.strftime("%Y%m%d"),
                     'value':para2['mobileKey']
            }
            para2['mobileKeyEncrypt']=desEncrypt(para=desPara)
            para2['password'] = encodeToMd5('123456')
            ret = XsGongZuoTaiIntf.addUser(para2)
            self.assertFalse(ret.result, '未输入验证码注册成功')
            
            #输入验证码，但不输入密码注册(密码必选项填写前台控制，接口并没有控制，校验点先不测试)
            XsGongZuoTaiIntf.getValidateCode(mobile=registMobile)
            para2['validateCode'] = '123456' #测试环境默认校验码都是123456
            para2['password'] = ''
    #         ret = XsGongZuoTaiIntf.addUser(para2)
    #         self.assertFalse(ret.result, '未输入密码注册成功')
    
            #所属街道和注册协议必填项验证都属于前台控制，接口无法验证，不测试
            
            #输入异常邀请码
            para2['password'] = encodeToMd5('111111')
            para2['inviteCode'] = '3333333'
            ret = XsGongZuoTaiIntf.addUser(para2)
            self.assertFalse(ret.result, '输入错误邀请码注册成功')
            
            #正常注册,使用默认用户的邀请码        
            defaultUserInviteNum = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand="select t.invitenum from userinfos t where t.userid=(select w.id from users w where w.mobile='%s')" % Global.XianSuoDftMobile)
            para2['inviteCode'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand="select t.invitecode from users t where t.mobile='%s'" % Global.XianSuoDftMobile)
            ret = XsGongZuoTaiIntf.addUser(para2)
            self.assertTrue(ret.result, '正常注册流程失败')
            
            defaultUserInviteNumNow = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand="select t.invitenum from userinfos t where t.userid=(select w.id from users w where w.mobile='%s')" % Global.XianSuoDftMobile)
            self.assertEqual(defaultUserInviteNumNow-defaultUserInviteNum, 1, '邀请记录未增加1')
            #使用已注册号码重新注册
            ret = XsGongZuoTaiIntf.addUser(para2)
            self.assertFalse(ret.result, '已注册号码重新注册成功')
            
            #注册成功后的手机登录
            ret = XsInformationSquareIntf.getUserLogin(mobile=registMobile,password='111111')
            self.assertEqual(ret['response']['success'], True, '登录验证失败')
        finally:
            if Global.simulationEnvironment is False:
                XsGongZuoTaiIntf.deleteUserFromDb(mobile=registMobile)

    def test_get_back_password_02(self):
        '''找回密码主流程验证824'''
        #产生一个123开头的手机随机号码
        registMobile='123%s'%str(createRandomNumber(length=8))
        count=YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand="select count(*)  from users w where w.mobile='%s'" % registMobile)
        while count>=1:
            registMobile='123%s'%str(createRandomNumber(length=8))
            count=YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand="select count(*)  from users w where w.mobile='%s'" % registMobile)
        try:
            #对于一个未注册过的新手机号码进行找回密码操作,线获取验证码123456
            XsGongZuoTaiIntf.getValidateCode(mobile=registMobile)
            getBackPasswordDict = copy.deepcopy(XsGongZuoTaiPara.getBackPasswordPara)
            getBackPasswordDict['mobile'] = registMobile
            getBackPasswordDict['password'] = encodeToMd5('222222')
            
            ret=XsGongZuoTaiIntf.resetPassword(getBackPasswordPara=getBackPasswordDict)
            self.assertFalse(ret.result,'未注册过的手机号码进行找回密码验证失败')
            #使用新手机号码注册
            para2=copy.deepcopy(XsGongZuoTaiPara.userAddPara)
            para2['mobile']=registMobile
            #mobileKey采用15位随机数字，防止重复测试时失败
            para2['mobileKey']=createRandomNumber(length=15)
            para2['password'] = encodeToMd5('111111')
            desPara={
                     'key':time.strftime("%Y%m%d"),
                     'value':para2['mobileKey']
            }
            para2['mobileKeyEncrypt']=desEncrypt(para=desPara)
            result2=addUser(para=para2)
            self.assertTrue(result2.result, '注册失败')
            
            #不输入验证码找回密码
            getBackPasswordDict = copy.deepcopy(XsGongZuoTaiPara.getBackPasswordPara)
            getBackPasswordDict['mobile'] = registMobile
            getBackPasswordDict['password'] = encodeToMd5('222222')
            getBackPasswordDict['validateCode'] = ''
            
            ret=XsGongZuoTaiIntf.resetPassword(getBackPasswordPara=getBackPasswordDict)
            self.assertFalse(ret.result,'不输入验证码找回密码验证失败')
            
            #不输入新密码找回密码,接口不限制密码为空，此检查项略过
            getBackPasswordDict = copy.deepcopy(XsGongZuoTaiPara.getBackPasswordPara)
            getBackPasswordDict['mobile'] = registMobile
            getBackPasswordDict['password'] = ''
            
    #         ret=XsGongZuoTaiIntf.resetPassword(getBackPasswordPara=getBackPasswordDict)
    #         self.assertFalse(ret.result,'不输入密码找回密码成功')
            
            #正常重置密码
            getBackPasswordDict = copy.deepcopy(XsGongZuoTaiPara.getBackPasswordPara)
            getBackPasswordDict['mobile'] = registMobile
            getBackPasswordDict['password'] = encodeToMd5('222222')
            
            ret=XsGongZuoTaiIntf.resetPassword(getBackPasswordPara=getBackPasswordDict)
            self.assertTrue(ret.result,'正常重置密码失败')
            
            #使用旧密码重新登录
            result4=XsInformationSquareIntf.getUserLogin(mobile=registMobile,password='111111')
            self.assertEqual(result4['response']['success'], False, '登录验证失败')
            
            #使用新密码重新登录
            result4=XsInformationSquareIntf.getUserLogin(mobile=registMobile,password='222222')
            self.assertEqual(result4['response']['success'], True, '登录验证失败')
        finally:
            if Global.simulationEnvironment is False:
                XsGongZuoTaiIntf.deleteUserFromDb(mobile=registMobile)
    def test_user_login_03(self):
        '''主流程登录-812'''
                
        #使用默认用户，错误密码登录
        res2=XsInformationSquareIntf.getUserLogin(mobile=Global.XianSuoDftMobile,password='wrong')
        self.assertEqual(res2['response']['success'], False, '错误密码登录成功')
        
        #使用错误用户和密码登录
        res3=XsInformationSquareIntf.getUserLogin(mobile='12345678901',password='wrong')
        self.assertEqual(res3['response']['success'], False, '错误手机号合密码登录成功')
        
        #手机号未空验证
        res5=XsInformationSquareIntf.getUserLogin(mobile='')
        self.assertEqual(res5['success'], False, '空手机号登录成功')
        
        #使用正常手机号和密码登录
        res=XsInformationSquareIntf.getUserLogin()
        self.assertEqual(res['response']['success'], True, '正常登录流程验证失败')
        pass

    def test_user_certify_04(self):
        '''认证用户签到功能-606'''
        #用默认手机号认证线索用户
        SystemMgrIntf.clueUserCertified()
        
        #手机端检查用户认证状态
        userCheckDict = copy.deepcopy(XsMyInformationPara.checkUserInfoPara)
        userCheckDict['mobile']=Global.XianSuoDftMobile
        userCheckDict['certifiedType'] = 1 #表示已认证，0表示未认证
        
        userId = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand="select w.id from users w where w.mobile='%s'" % Global.XianSuoDftMobile)
        ret = XsMyInformationIntf.check_personal_info(userId, userCheckDict)
        self.assertTrue(ret, '用户认证信息检查失败')
        
        #进行网格员认证操作
        wangGeYuanSignInDict = copy.deepcopy(XsGongZuoTaiPara.wangGeYuanQianDaoPara)
        wangGeYuanSignInDict['pcUserId'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from users t where t.username='%s'" % InitDefaultPara.userInit['DftQuUser'])
        wangGeYuanSignInDict['userId'] =  userId
        wangGeYuanSignInDict['address'] = "网格员签到地址%s" % createRandomNumber(length=6)
        ret = XsGongZuoTaiIntf.add_wanggeyuan_sign_in(wangGeYuanSignInDict)
        self.assertTrue(ret, '网格员签到操作失败')
        
        #检查网格员签到记录
        getWangGeYuanSignInRecord = copy.deepcopy(XsGongZuoTaiPara.getWangGeYuanSignInRecordsPara)
        getWangGeYuanSignInRecord['userId']=userId
        
        checkWangGeYuanSignInRecord = copy.deepcopy(XsGongZuoTaiPara.checkWangGeYuanSignInRecordPara)
        checkWangGeYuanSignInRecord['address'] = wangGeYuanSignInDict['address']
        checkWangGeYuanSignInRecord['userId'] = userId
        
        ret = XsGongZuoTaiIntf.check_wanggeyuan_sign_in_records(checkWangGeYuanSignInRecord, getWangGeYuanSignInRecord)
        self.assertTrue(ret, '网格员签到记录检查失败')
    
    def test_user_change_password_05(self):
        '''修改密码-827'''
        #产生一个123开头的手机随机号码
        registMobile='123%s'%str(createRandomNumber(length=8))
        count=YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand="select count(*)  from users w where w.mobile='%s'" % registMobile)
        while count>=1:
            registMobile='123%s'%str(createRandomNumber(length=8))
            count=YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand="select count(*)  from users w where w.mobile='%s'" % registMobile)
        try:
            #新用户注册
            XsGongZuoTaiIntf.getValidateCode(mobile=registMobile)
            para2=copy.deepcopy(XsGongZuoTaiPara.userAddPara)
            para2['mobile'] = registMobile
            para2['mobileKey'] = createRandomNumber(length=15)
            desPara={
                     'key':time.strftime("%Y%m%d"),
                     'value':para2['mobileKey']
            }
            para2['mobileKeyEncrypt']=desEncrypt(para=desPara)
            para2['password'] = encodeToMd5('111111')
            ret = XsGongZuoTaiIntf.addUser(para2)
            self.assertTrue(ret.result, '新用户注册失败')
            
            #修改密码
            updateUserDict = copy.deepcopy(XsGongZuoTaiPara.userUpdatePara)
            updateUserDict['id'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand="select w.id from users w where w.mobile='%s'" % registMobile)
            updateUserDict['password'] = encodeToMd5('222222')
            
            ret = XsMyInformationIntf.updateUserInfo(updateUserDict)
            self.assertTrue(ret, '修改密码失败')
            
            #使用新密码登录
            ret=XsInformationSquareIntf.getUserLogin(mobile=registMobile,password='222222')
            self.assertEqual(ret['response']['success'], True, '新密码登录验证失败')
            #使用旧密码重新登录
            ret=XsInformationSquareIntf.getUserLogin(mobile=registMobile,password='111111')
            self.assertEqual(ret['response']['success'], False, '旧密码登录验证成功')
        finally:
            if Global.simulationEnvironment is False:
                XsGongZuoTaiIntf.deleteUserFromDb(mobile=registMobile)
    
    def test_modify_my_info_06(self):
        '''修改个人信息-826'''
        #新增新手机号
        newMobilePhone = '13588806928'
         
        XsGongZuoTaiIntf.initUser(mobile=newMobilePhone)
         
        #更新昵称
        newNickName = 'nick_%s' % CommonUtil.createRandomString()
        updatePara=copy.deepcopy(XsGongZuoTaiPara.userUpdatePara)           
        updatePara['id']=YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand="select id from users where mobile='%s'"%newMobilePhone)
        updatePara['nickName']= newNickName
        XsMyInformationIntf.updateUserInfo(updatePara)
         
        #使用新手机爆料一条爆料
        newClueByNewUser = copy.deepcopy(XsBaoLiaoPara.XinZeng) 
        newClueByNewUser['information']['contentText'] = '事件描述%s' % CommonUtil.createRandomString()
        newClueByNewUser['information']['baiduX'] = '120.4989885463861'
        newClueByNewUser['information']['baiduY'] = '30.27759299562879'
        newClueByNewUser['information']['x'] = '120.488114380334'
        newClueByNewUser['information']['y'] = '30.27759299562879'         
        newClueByNewUser['information']['address'] = 'addres'+CommonUtil.createRandomString()
        responseDict = XsBaoLiaoIntf.addXianSuo(newClueByNewUser,mobile=newMobilePhone)
        self.assertTrue(responseDict.result, '新增线索失败')
         
        #在信息广场查看昵称
        getClueListDict = copy.deepcopy(XsBaoLiaoPara.getClueListPara)
         
        checkClueListDict = copy.deepcopy(XsBaoLiaoPara.checkClueInSquarePara)
        checkClueListDict['contentText'] = newClueByNewUser['information']['contentText']
        checkClueListDict['nickName'] = newNickName
         
        ret = XsBaoLiaoIntf.check_baoliao_in_list(checkClueListDict, getClueListDict)
        self.assertTrue(ret, '在信息广场验证昵称失败')
         
        #在我的爆料中检查昵称
        checkMySquareDict = copy.deepcopy(XsBaoLiaoPara.jianchaxiansuo)
        checkMySquareDict['contentText'] = newClueByNewUser['information']['contentText']
        checkMySquareDict['nickName'] = newNickName
        ret = XsBaoLiaoIntf.checkClueInMyClue(checkMySquareDict, mobile=newMobilePhone)
        self.assertTrue(ret, '在我的爆料验证昵称失败')
         
        #对线索增加评论
        clueId = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from INFORMATIONS t where t.contenttext='%s'"%newClueByNewUser['information']['contentText'])
        addCommentDict = copy.deepcopy(XsBaoLiaoPara.addCommentForCluePara)
        addCommentDict['informationId'] = clueId
        addCommentDict['contentText'] = "评论内容"
        ret = XsBaoLiaoIntf.add_comment_for_clue(addCommentDict,mobile=newMobilePhone)
         
        #检查线索评论中，昵称是否正确
        checkCommnetDict = copy.deepcopy(XsBaoLiaoPara.checkCommentInCluePara)
        checkCommnetDict['contentText'] = addCommentDict['contentText']
        checkCommnetDict['commentNickName'] = newNickName
        ret = XsBaoLiaoIntf.check_comment_in_clue(clueId, checkCommnetDict)
        self.assertTrue(ret, '在线索的评论中检查昵称失败')
         
        userId = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from USERS t where t.mobile='%s'" % newMobilePhone)
        #修改性别
        updatePara=copy.deepcopy(XsGongZuoTaiPara.userUpdatePara)           
        updatePara['id'] = userId
        updatePara['gender']= "女"
        XsMyInformationIntf.updateUserInfo(updatePara)
         
        #在我的信息中检查性别
         
        checkUserDict = copy.deepcopy(XsMyInformationPara.checkUserInfoPara)
        checkUserDict['gender'] = updatePara['gender']
        ret = XsMyInformationIntf.check_personal_info(userId, checkUserDict)
        self.assertTrue(ret, '在我的信息中检查性别失败')
         
        #修改常住地址
        updatePara=copy.deepcopy(XsGongZuoTaiPara.userUpdatePara)           
        updatePara['id'] = userId
        updatePara['address']= "测试地址%s" % CommonUtil.createRandomString()
        XsMyInformationIntf.updateUserInfo(updatePara)
         
        #在我的信息中检查地址
        checkUserDict = copy.deepcopy(XsMyInformationPara.checkUserInfoPara)
        checkUserDict['address'] = updatePara['address']
        ret = XsMyInformationIntf.check_personal_info(userId, checkUserDict)
        self.assertTrue(ret, '在我的信息中检查性别失败')
        pass
  
    
#     def test_XsGongZuoTai_07(self):
#         '''获取信箱内容,次方法的接口有问题，sign计算错误'''
#         addPara=copy.deepcopy(xinZeng2)
#         addXianSuo(addPara)
#         listPara={
#                 'tqmobile':'true',
#                 'page':'1',
#                 'rows':'100'
#                   }
#         lsr=viewSchedule(para=listPara)
# #         print lsr.text
#         lsrDict=json.loads(lsr.text)
#         para1={
#                'apiVersion':'4',
#                'tqmobile':'true',
#                'userId':lsrDict['response']['module']['rows'][0]['information']['publishUserId'],
#                }
#         print para1['userId']
#         #开始未读消息数
#         print para1
#         messageCount1=getMessageBoxUnReadCount(para=para1)
#         print messageCount1
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
#         isRes=clueToIssue(para=addIssuePara)
#         isResDict=json.loads(isRes.text) 
#         #事件办结
#         issuePara=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)
#         issuePara['operation.dealOrg.id']=orgInit['DftJieDaoOrgId']
#         issuePara['operation.issue.id']=isResDict['issueId']
#         issuePara['keyId']=isResDict['issueStepId']    
#         issuePara['operation.dealUserName']=userInit['DftJieDaoUserXM']
#         issuePara['operation.mobile']=userInit['DftJieDaoUserSJ']
#         issuePara['operation.content']='结案'       
#         issuePara['dealCode']='31'
#         result=dealIssue(issueDict=issuePara)
#         self.assertTrue(result.result, '办结失败')
#         Log.LogOutput( message='事件办结成功')
#         #获取信息数参数
#         #设置延时
#         time.sleep(2)
#         messageCount2=getMessageBoxUnReadCount(para=para1)
#         print messageCount2
#         self.assertEqual(messageCount2, messageCount1+1, '未读信息数验证失败')
#         Log.LogOutput(message='事件办结后信息数目验证通过')
#         #其他用户评论，消息数目加1
#         #新注册一个用户2'12345678901'
#         para2=copy.deepcopy(XsGongZuoTaiPara.userAddPara)
#         para2['mobile']='12345678901'
#         #mobileKey采用15位随机数字，防止重复测试时失败
#         para2['mobileKey']=createRandomNumber(length=15)
#         desPara={
#                  'key':time.strftime("%Y%m%d"),
#                  'value':para2['mobileKey']
#         }
#         para2['mobileKeyEncrypt']=desEncrypt(para=desPara)
#         result2=addUser(para=para2)
#         self.assertTrue(result2.result, '注册失败')
#         #用户2对新增的线索进行评论
#         addcompara=copy.deepcopy(addCommentPara)
#         addcompara['informationId']=lsrDict['response']['module']['rows'][0]['information']['id']
#         addcompara['commentUserId']=json.loads(result2.text)['response']['module']['id']
#         addcompara['commentType']=0
#         result3=addComment(para=addcompara,mobile=para2['mobile'],password='678901')
#         self.assertTrue(result3.text, '新增评论失败')
#         time.sleep(2)
#         messageCount3=getMessageBoxUnReadCount(para=para1)
#         self.assertEqual(messageCount3, messageCount2+1, '未读信息数验证失败')
#         Log.LogOutput(message='线索被其他用户评论后信息数目验证通过')
# 
#         pass
        
    def test_XsGongZuoTai_08(self):
        '''验证登录session过期登录后返回的错误提示信息是否正确'''
        #获取第一次登录的sid
        oldSid=getLoginSid()
        testPremise_01 = copy.deepcopy(XinZeng) 
        testPremise_01['information']['contentText'] = '事件描述%s' % CommonUtil.createRandomString()
        testPremise_01['information']['baiduX'] = '120.4989885463861'
        testPremise_01['information']['baiduY'] = '30.27759299562879'
        testPremise_01['information']['x'] = '120.488114380334'
        testPremise_01['information']['y'] = '30.27759299562879'         
        testPremise_01['information']['address'] = 'addres'+CommonUtil.createRandomString()
        #再次登录，获取新的sid
        #但是仍然使用旧的sid发送post请求
        response=addClueWithSpecialWay(sid=oldSid,XianSuoDict=testPremise_01)
        resDict=json.loads(response.text)
#         print response.text
        #验证返回的错误信息
        self.assertEquals(resDict['response']['errDesc'],"异常代码:[IOE100-01] 登录身份信息失效，请重新登录！", 'session失效后post请求返回错误信息不正确')
        Log.LogOutput( message='session失效后post请求返回错误信息正确')
        pass    
    def tearDown(self):
        pass    
    
    
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(XsGongZuoTai("test_user_regist_01"))
#     suite.addTest(XsGongZuoTai("test_get_back_password_02"))
#     suite.addTest(XsGongZuoTai("test_user_login_03"))
#     suite.addTest(XsGongZuoTai("test_user_certify_04"))
#     suite.addTest(XsGongZuoTai("test_user_change_password_05"))
#     suite.addTest(XsGongZuoTai("test_modify_my_info_06"))
#     suite.addTest(XsGongZuoTai("test_XsGongZuoTai_07"))
#     suite.addTest(XsGongZuoTai("test_XsGongZuoTai_08"))
    results = unittest.TextTestRunner().run(suite)
    pass    