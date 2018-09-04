# -*- coding:UTF-8 -*-
'''
Created on 2016-4-6

@author: N-133
'''
from __future__ import unicode_literals
from COMMON import CommonUtil, Log
from CONFIG import Global, InitDefaultPara
from Interface.YunWeiPingTai.XinXiGuanLi import XinXiGuanLiPara, XinXiGuanLiIntf
from Interface.YunWeiPingTai.XinXiGuanLi.XinXiGuanLiPara import \
    ShowState, InfoType, ReportState, ReportType,\
    DeleteType
from Interface.YunWeiPingTai.YunWeiCommon import YunWeiCommonIntf
import copy
import unittest
from Interface.XianSuoApp.GongZuoTai import XsGongZuoTaiIntf
from Interface.XianSuoApp.BaoLiao import XsBaoLiaoPara, XsBaoLiaoIntf
from Interface.YunWeiPingTai.XiTongPeiZhi import XiTongPeiZhiPara,\
    XiTongPeiZhiIntf
from Interface.XianSuoApp.WoDeXinXi import XsMyInformationPara,\
    XsMyInformationIntf
from Interface.XianSuoApp.ShuoShuo import ShuoShuoPara, ShuoShuoIntf
from CONFIG.Define import LogLevel
from Interface.PingAnJianShe.XianSuoGuanLi import XianSuoGuanLiIntf,\
    XianSuoGuanLiPara



class XinXiGuanLi(unittest.TestCase):

    def setUp(self):
#         SystemMgrIntf.initEnv()''
        XinXiGuanLiIntf.deleteyunwei()
        XsGongZuoTaiIntf.initUser()
        pass
    
    #设置线索状态
    def test_baoliaoguanli_01(self):
        """线索公开/不公开状态设置-467"""
        #新增线索        
        testClueAdd_01 = copy.deepcopy(XsBaoLiaoPara.xinZeng2) 
        testClueAdd_01['information']['contentText'] = '测试爆料信息%s' % CommonUtil.createRandomString()
#         testClueAdd_01['information']['baiduX'] = '120.1362348153468'
#         testClueAdd_01['information']['baiduY'] = '30.28016484243025'
#         testClueAdd_01['information']['x'] = '120.1250430287559'
#         testClueAdd_01['information']['y'] = '30.27612037575986'         
        testClueAdd_01['information']['address'] = '大江东测试地点'+CommonUtil.createRandomString()
        responseDict = XinXiGuanLiIntf.AddXianSuo(testClueAdd_01)
        self.assertTrue(responseDict.result, '新增线索失败') 
        
        #信息管理中查看新增线索
        param = copy.deepcopy(XinXiGuanLiPara.jianchaxiansuo)
        param['contentText'] = testClueAdd_01['information']['contentText']
        param['address'] = testClueAdd_01['information']['address']
        param['nickName'] = Global.XianSuoDftMobileNick
        param['mobile'] = Global.XianSuoDftMobile
        param['showState'] = ShowState.OPEN 
        ret = XinXiGuanLiIntf.check_clue_in_cluelist_manage(clueCheckDict=param)         
        self.assertTrue(ret, '在爆料列表中无法找到爆料')
                
        #修改状态为公开
        param1 = copy.deepcopy(XinXiGuanLiPara.XianSuoGongKai)
        param1['ids[]'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from INFORMATIONS t where t.contenttext='%s'"%testClueAdd_01['information']['contentText'])
        result=XinXiGuanLiIntf.set_clue_state_open(param1)
        self.assertTrue(result, '修改状态为公开失败')
        
        #在手机端爆料广场检查爆料是否存在
        clueCheck = copy.deepcopy(XsBaoLiaoPara.checkClueInSquarePara)
        clueCheck['contentText'] = testClueAdd_01['information']['contentText']
        clueCheck['address'] = testClueAdd_01['information']['address']
        clueCheck['nickName'] = Global.XianSuoDftMobileNick
        clueCheck['mobile'] = Global.XianSuoDftMobile
        
        ret = XsBaoLiaoIntf.check_clue_in_clue_list(clueCheck)
        self.assertTrue(ret, '设置为公开后，爆料列表不显示')   
         
        #修改状态为不公开
        param1 = copy.deepcopy(XinXiGuanLiPara.XianSuoGongKai)
        param1['ids[]'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from INFORMATIONS t where t.contenttext='%s'"%testClueAdd_01['information']['contentText'])
        result=XinXiGuanLiIntf.set_clue_state_to_close(param1)
        self.assertTrue(result, '修改状态为公开失败')
        
        #重新检查爆料列表，不应显示
        ret = XsBaoLiaoIntf.check_clue_in_clue_list(clueCheck)
        self.assertFalse(ret, '设置为不公开后，爆料列表还是显示爆料')
        
        #删除线索        
        deleteparam_03 = copy.deepcopy(XinXiGuanLiPara.delCluePara)
        deleteparam_03['ids[]'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from INFORMATIONS t where t.contenttext='%s'"%testClueAdd_01['information']['contentText'])
        deleteparam_03['deleteReason']='其他'
        ret = XinXiGuanLiIntf.deletexiansuo(deleteparam_03)         
         
        #在运维平台线索列表中查看是否存在
        param['showState'] = None
        ret = XinXiGuanLiIntf.check_clue_in_cluelist_manage(clueCheckDict=param)         
        self.assertFalse(ret, '在爆料列表中无法找到爆料')
        
        #在手机端我的爆料中查看
        checkClueInMyClue = copy.deepcopy(XsBaoLiaoPara.jianchaxiansuo)
        checkClueInMyClue['contentText'] = testClueAdd_01['information']['contentText']
        checkClueInMyClue['address'] = testClueAdd_01['information']['address']
        ret = XsBaoLiaoIntf.checkClueInMyClue(checkClueInMyClue)
        self.assertFalse(ret, '运维平台删除爆料后在手机端我的爆料中还是能查看到爆料')
        pass 
       
    def test_ClueTheme_02(self):
        """爆料主题列表搜索-774仿真跳过"""
        #主题只能在省级设置，仿真环境跳过
        if Global.simulationEnvironment is True:
            Log.LogOutput( message='仿真环境跳过测试')
            pass
        else:
            #判断是否有以下两个主题，如没有，则新增
            themeAddOne = copy.deepcopy(XiTongPeiZhiPara.themeAddDict)
            themeAddOne['themeContent.name'] = "测试主题1"
            themeAddOne['themeContent.description'] = "测试描述1"
            
            themeAddTwo = copy.deepcopy(XiTongPeiZhiPara.themeAddDict)
            themeAddTwo['themeContent.name'] = "测试主题2"
            themeAddTwo['themeContent.description'] = "测试描述2"
            count0 = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select count(*) from THEMECONTENTS t where t.name='%s'" % themeAddOne['themeContent.name'])
            count1 = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select count(*) from THEMECONTENTS t where t.name='%s'" % themeAddTwo['themeContent.name'])
            if count0 == 0:
                XiTongPeiZhiIntf.add_theme(themeAddOne)
            if count1 == 0:
                XiTongPeiZhiIntf.add_theme(themeAddTwo)
                
            #在主题查询列表中检查主题
            themeCheckDict = copy.deepcopy(XinXiGuanLiPara.checkThemeInClueManagePara)
            themeCheckDict['name'] = themeAddOne['themeContent.name']
            themeCheckDict['description'] = themeAddOne['themeContent.description']
            ret = XinXiGuanLiIntf.check_theme_in_clue_manage(themeCheckDict)
            self.assertTrue(ret, '在爆料管理主题查询中无法查到新增的主题')
            
            themeCheckDict['name'] = themeAddTwo['themeContent.name']
            themeCheckDict['description'] = themeAddTwo['themeContent.description']
            ret = XinXiGuanLiIntf.check_theme_in_clue_manage(themeCheckDict)
            self.assertTrue(ret, '在爆料管理主题查询中无法查到新增的主题')
            
            #新增两条不同主题的爆料
            newClueThemeOne = copy.deepcopy(XsBaoLiaoPara.xinZeng2) 
            newClueThemeOne['information']['contentText'] = '事件描述%s' % CommonUtil.createRandomString()
#             newClueThemeOne['information']['baiduX'] = '120.1362348153468'
#             newClueThemeOne['information']['baiduY'] = '30.28016484243025'
#             newClueThemeOne['information']['x'] = '120.1250430287559'
#             newClueThemeOne['information']['y'] = '30.27612037575986'         
            newClueThemeOne['information']['address'] = 'addres'+CommonUtil.createRandomString()
            newClueThemeOne['information']['themeContentId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from THEMECONTENTS t where t.name='%s'" % themeAddOne['themeContent.name'])
            responseDict = XsBaoLiaoIntf.addXianSuo(newClueThemeOne)
            self.assertTrue(responseDict.result, '新增线索失败')
            
            newClueThemeTwo = copy.deepcopy(XsBaoLiaoPara.xinZeng2) 
            newClueThemeTwo['information']['contentText'] = '事件描述%s' % CommonUtil.createRandomString()
    #         newClueThemeTwo['information']['baiduX'] = '120.1362348153468'
    #         newClueThemeTwo['information']['baiduY'] = '30.28016484243025'
    #         newClueThemeTwo['information']['x'] = '120.1250430287559'
    #         newClueThemeTwo['information']['y'] = '30.27612037575986'         
            newClueThemeTwo['information']['address'] = 'addres'+CommonUtil.createRandomString()
            newClueThemeTwo['information']['themeContentId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from THEMECONTENTS t where t.name='%s'" % themeAddTwo['themeContent.name'])
            responseDict = XsBaoLiaoIntf.addXianSuo(newClueThemeTwo)
            self.assertTrue(responseDict.result, '新增线索失败')
            
            #通过主题1搜索，线索1可以检查到，线索2检查不到
            getClueList = copy.deepcopy(XinXiGuanLiPara.chakanxiansuo)
            getClueList['information.themeContentId'] = newClueThemeOne['information']['themeContentId']
            
            checkClueDict = copy.deepcopy(XinXiGuanLiPara.jianchaxiansuo)
            checkClueDict['contentText']=newClueThemeOne['information']['contentText']
            
            ret = XinXiGuanLiIntf.check_clue_in_cluelist_manage(checkClueDict, getClueList)
            self.assertTrue(ret, '通过主题搜索线索失败')
            
            checkClueDict['contentText']=newClueThemeTwo['information']['contentText']
            ret = XinXiGuanLiIntf.check_clue_in_cluelist_manage(checkClueDict, getClueList)
            self.assertFalse(ret, '通过主题搜索线索失败')    
        
    def test_moblie_search_03(self):
        """根据手机号码进行搜索-468"""
        #使用两个手机号新增两条线索
        #默认账号添加一条线索
        newClueByDftUser = copy.deepcopy(XsBaoLiaoPara.xinZeng2) 
        newClueByDftUser['information']['contentText'] = '事件描述%s' % CommonUtil.createRandomString()
#         newClueByDftUser['information']['baiduX'] = '120.1362348153468'
#         newClueByDftUser['information']['baiduY'] = '30.28016484243025'
#         newClueByDftUser['information']['x'] = '120.1250430287559'
#         newClueByDftUser['information']['y'] = '30.27612037575986'         
        newClueByDftUser['information']['address'] = 'addres'+CommonUtil.createRandomString()
        responseDict = XsBaoLiaoIntf.addXianSuo(newClueByDftUser)
        self.assertTrue(responseDict.result, '新增线索失败')
        #使用新账号新增一条线索
        #添加一个手机账号，用于手机号快速搜索验证
        newMobilePhone = '13588806928'
        newNickName = 'nick_%s' % newMobilePhone
        XsGongZuoTaiIntf.initUser(mobile=newMobilePhone)
        #初始化新用户的时候会默认设置昵称，昵称格式为"nick_手机号"
        newClueByNewUser = copy.deepcopy(XsBaoLiaoPara.xinZeng2) 
        newClueByNewUser['information']['contentText'] = '事件描述%s' % CommonUtil.createRandomString()
#         newClueByNewUser['information']['baiduX'] = '120.1362348153468'
#         newClueByNewUser['information']['baiduY'] = '30.28016484243025'
#         newClueByNewUser['information']['x'] = '120.1250430287559'
#         newClueByNewUser['information']['y'] = '30.27612037575986'         
        newClueByNewUser['information']['address'] = 'addres'+CommonUtil.createRandomString()
        responseDict = XsBaoLiaoIntf.addXianSuo(newClueByNewUser,mobile=newMobilePhone)
        self.assertTrue(responseDict.result, '新增线索失败')
        
        #通过默认手机号搜索，线索1可以检查到，线索2检查不到
        getClueList = copy.deepcopy(XinXiGuanLiPara.chakanxiansuo)
        getClueList['information.mobile'] = Global.XianSuoDftMobile
        
        checkClueDict = copy.deepcopy(XinXiGuanLiPara.jianchaxiansuo)
        checkClueDict['contentText']=newClueByDftUser['information']['contentText']
        
        ret = XinXiGuanLiIntf.check_clue_in_cluelist_manage(checkClueDict, getClueList)
        self.assertTrue(ret, '通过手机号搜索线索失败')
        
        checkClueDict['contentText']=newClueByNewUser['information']['contentText']
        ret = XinXiGuanLiIntf.check_clue_in_cluelist_manage(checkClueDict, getClueList)
        self.assertFalse(ret, '通过手机号搜索线索失败')  
        pass 
    
    def test_user_deedback_04(self):
        """用户反馈查看-859"""
        #清空意见反馈信息
        if Global.simulationEnvironment is False:
            XsMyInformationIntf.delete_all_feedbaks()
        #手机端新增意见反馈
        addUserAdvice = copy.deepcopy(XsMyInformationPara.addUserFeedbackPara)
        addUserAdvice['userFeedBack']['advice'] = '意见反馈%s' % CommonUtil.createRandomString()
        addUserAdvice['userFeedBack']['mobile'] = Global.XianSuoDftMobile
        ret = XsMyInformationIntf.add_user_feedback(addUserAdvice)
        self.assertTrue(ret, '新增意见反馈失败')
        
        #运维平台检查意见反馈
        checkUserAdvice = copy.deepcopy(XinXiGuanLiPara.checkUserFeedbackPara)
        checkUserAdvice['mobile'] = Global.XianSuoDftMobile
        checkUserAdvice['advice'] = addUserAdvice['userFeedBack']['advice']
        
        getUserAdvice = copy.deepcopy(XinXiGuanLiPara.getUserFeedbackPara)
        ret = XinXiGuanLiIntf.check_user_feedback(checkUserAdvice,getUserAdvice)
        self.assertTrue(ret, '未检查到用户反馈信息')
        
        #选择意见反馈进行回复
        adviceId = XinXiGuanLiIntf.get_user_feedback_id_by_content(addUserAdvice['userFeedBack']['advice'])
        replyAdvice = copy.deepcopy(XinXiGuanLiPara.replyForFeedbackPara)
        replyAdvice['ids'] = adviceId
        replyAdvice['replyContent'] = "回复内容%s" % CommonUtil.createRandomString()
        ret = XinXiGuanLiIntf.reply_for_user_feedback(replyAdvice)
        
        #在列表检查回复信息是否正常
        checkUserAdvice['replyContent'] = replyAdvice['replyContent']
        ret = XinXiGuanLiIntf.check_user_feedback(checkUserAdvice,getUserAdvice)
        self.assertTrue(ret, '未检查到用户反馈信息')
        
        #手机端检查回复信息
        getUserAdvice = copy.deepcopy(XsMyInformationPara.getUserFeedbackPara)
        getUserAdvice['userFeedBack']['mobile'] = Global.XianSuoDftMobile
        
        checkUserAdviceReply = copy.deepcopy(XsMyInformationPara.checkUserFeedbackPara)
        checkUserAdviceReply['advice'] = addUserAdvice['userFeedBack']['advice']
        checkUserAdviceReply['mobile'] = Global.XianSuoDftMobile
        checkUserAdviceReply['replyContent'] = replyAdvice['replyContent']
        ret = XsMyInformationIntf.check_user_feedback(checkUserAdviceReply, getUserAdvice)
        self.assertTrue(ret, '用户意见反馈信息检查失败')
        pass
    
    def test_user_deedback_search_05(self):
        """用户反馈搜索及高级搜索-484"""
        #清空意见反馈信息
        if Global.simulationEnvironment is False:
            XsMyInformationIntf.delete_all_feedbaks()
        
        #添加一个手机账号，用于手机号快速搜索验证
        newMobilePhone = '13588806928'
        XsGongZuoTaiIntf.initUser(mobile=newMobilePhone)
        
        #用不同用户添加两条不同的反馈意见
        #手机端默认用户新增意见反馈
        addUserAdvice = copy.deepcopy(XsMyInformationPara.addUserFeedbackPara)
        addUserAdvice['userFeedBack']['advice'] = '意见反馈%s' % CommonUtil.createRandomString()
        addUserAdvice['userFeedBack']['mobile'] = Global.XianSuoDftMobile
        ret = XsMyInformationIntf.add_user_feedback(addUserAdvice)
        self.assertTrue(ret, '新增意见反馈失败')
        
        #手机端另外用户新增反馈意见
        addUserAdviceAnother = copy.deepcopy(XsMyInformationPara.addUserFeedbackPara)
        addUserAdviceAnother['userFeedBack']['advice'] = '意见反馈%s' % CommonUtil.createRandomString()
        addUserAdviceAnother['userFeedBack']['mobile'] = newMobilePhone
        ret = XsMyInformationIntf.add_user_feedback(addUserAdviceAnother)
        self.assertTrue(ret, '新增意见反馈失败')
        
        #通过新手机号搜索意见反馈，默认用户的反馈意见不显示，新用户意见反馈显示
        getUserAdvice = copy.deepcopy(XinXiGuanLiPara.getUserFeedbackPara)
        getUserAdvice['userFeedBack.mobile'] = newMobilePhone
        
        checkUserAdvice = copy.deepcopy(XinXiGuanLiPara.checkUserFeedbackPara)
        checkUserAdvice['mobile'] = newMobilePhone
        checkUserAdvice['advice'] = addUserAdviceAnother['userFeedBack']['advice']
        
        ret = XinXiGuanLiIntf.check_user_feedback(checkUserAdvice,getUserAdvice)
        self.assertTrue(ret, '搜索用户意见反馈失败')
        
        checkUserAdvice['mobile'] = Global.XianSuoDftMobile
        checkUserAdvice['advice'] = addUserAdvice['userFeedBack']['advice']
        ret = XinXiGuanLiIntf.check_user_feedback(checkUserAdvice,getUserAdvice)
        self.assertFalse(ret, '查到不符合搜索条件的用户意见反馈')
        
        #通过手机号高级查询与手机搜索是同一个接口，因此不再单独测试

    def test_information_report_06(self):
        """ 信息举报记录删除、解除举报、不公开、爆料转说说操作-851"""
        #删除所有后台关键字设置
        XiTongPeiZhiIntf.delete_all_keyword_setting()
        #删除所有举报信息
        XinXiGuanLiIntf.delete_all_information_report()
        #添加一个手机账号，用于手机号快速搜索验证
        newMobilePhone = '13588806928'
        XsGongZuoTaiIntf.initUser(mobile=newMobilePhone)
        #初始化新用户的时候会默认设置昵称，昵称格式为"nick_手机号"
        newClueByNewUser = copy.deepcopy(XsBaoLiaoPara.xinZeng2) 
        newClueByNewUser['information']['contentText'] = '事件描述%s' % CommonUtil.createRandomString()
#         newClueByNewUser['information']['baiduX'] = '120.1362348153468'
#         newClueByNewUser['information']['baiduY'] = '30.28016484243025'
#         newClueByNewUser['information']['x'] = '120.1250430287559'
#         newClueByNewUser['information']['y'] = '30.27612037575986'         
        newClueByNewUser['information']['address'] = 'addres'+CommonUtil.createRandomString()
        responseDict = XsBaoLiaoIntf.addXianSuo(newClueByNewUser,mobile=newMobilePhone)
        self.assertTrue(responseDict.result, '新增线索失败')
         
        #针对爆料进行举报
        clueId = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from INFORMATIONS t where t.contenttext='%s'"%newClueByNewUser['information']['contentText'])
        addClueInfoReportDict = copy.deepcopy(XsBaoLiaoPara.addClueInfoReportPara)
        addClueInfoReportDict['infoId'] = clueId
        addClueInfoReportDict['reportUserId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from USERS t where t.mobile='%s'" % Global.XianSuoDftMobile)
        addClueInfoReportDict['publishUserMobile'] = newMobilePhone
        ret = XsBaoLiaoIntf.add_clue_information_report(addClueInfoReportDict)
        self.assertTrue(ret, '新增线索举报失败')
         
        #在后台信息举报列表查看
        getInfoReportDict = copy.deepcopy(XinXiGuanLiPara.getInformationReportPara)
        getInfoReportDict['informationReport.infoType'] = InfoType.CLUE
        getInfoReportDict['informationReport.state'] = 0 #表示未处理
         
        checkInfoReportDict = copy.deepcopy(XinXiGuanLiPara.checkInformationReportPara)
        checkInfoReportDict['contentText'] = newClueByNewUser['information']['contentText']
        checkInfoReportDict['address'] = newClueByNewUser['information']['address']
         
        ret = XinXiGuanLiIntf.check_information_report_in_list(getInfoReportDict, checkInfoReportDict)
        self.assertTrue(ret, '在举报信息中检查举报失败')
        
        
        #对举报进行删除
        Log.LogOutput(LogLevel.DEBUG, "------爆料举报删除后后台及手机端查看------")
        deleteInfoReportDict = copy.deepcopy(XinXiGuanLiPara.deleteInfoReportPara)
        deleteInfoReportDict['ids[]'] = XinXiGuanLiIntf.get_information_report_id_by_content(newClueByNewUser['information']['contentText'], getInfoReportDict)
        deleteInfoReportDict['infoType'] = InfoType.CLUE
        ret = XinXiGuanLiIntf.delete_certain_information_report(deleteInfoReportDict)
        self.assertTrue(ret, '删除举报信息失败')
          
        #后台列表再次检查是否被删除，此时因为被删除，应该无法找到
        ret = XinXiGuanLiIntf.check_information_report_in_list(getInfoReportDict, checkInfoReportDict)
        self.assertFalse(ret, '删除的举报信息在列表中还是存在')
          
        #在手机端检查爆料是否被删除
        appClueCheckDict = copy.deepcopy(XsBaoLiaoPara.checkClueInSquarePara)
        appClueCheckDict['contentText'] = newClueByNewUser['information']['contentText']
        appClueCheckDict['address'] = newClueByNewUser['information']['address']
        ret = XsBaoLiaoIntf.check_clue_in_clue_list(appClueCheckDict)
        self.assertFalse(ret, '删除的举报信息在手机列表中还是存在')
         
        #重新发送一条爆料
        Log.LogOutput(LogLevel.DEBUG, "------重新发布爆料，进行解除举报操作------")
        newClueByNewUser = copy.deepcopy(XsBaoLiaoPara.xinZeng2) 
        newClueByNewUser['information']['contentText'] = '事件描述%s' % CommonUtil.createRandomString()
#         newClueByNewUser['information']['baiduX'] = '120.1362348153468'
#         newClueByNewUser['information']['baiduY'] = '30.28016484243025'
#         newClueByNewUser['information']['x'] = '120.1250430287559'
#         newClueByNewUser['information']['y'] = '30.27612037575986'         
        newClueByNewUser['information']['address'] = 'addres'+CommonUtil.createRandomString()
        responseDict = XsBaoLiaoIntf.addXianSuo(newClueByNewUser,mobile=newMobilePhone)
        self.assertTrue(responseDict.result, '新增线索失败')
         
        #针对爆料进行举报
        clueId = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from INFORMATIONS t where t.contenttext='%s'"%newClueByNewUser['information']['contentText'])
        addClueInfoReportDict = copy.deepcopy(XsBaoLiaoPara.addClueInfoReportPara)
        addClueInfoReportDict['infoId'] = clueId
        addClueInfoReportDict['reportUserId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from USERS t where t.mobile='%s'" % Global.XianSuoDftMobile)
        addClueInfoReportDict['publishUserMobile'] = newMobilePhone
        ret = XsBaoLiaoIntf.add_clue_information_report(addClueInfoReportDict)
        self.assertTrue(ret, '新增线索举报失败')
         
        #解除举报
        relieveInfoReport = copy.deepcopy(XinXiGuanLiPara.deleteInfoReportPara)
        relieveInfoReport['ids[]'] = XinXiGuanLiIntf.get_information_report_id_by_content(newClueByNewUser['information']['contentText'], getInfoReportDict)
        relieveInfoReport['infoType'] = InfoType.CLUE
        ret = XinXiGuanLiIntf.relieve_information_report(relieveInfoReport)
        self.assertTrue(ret, '解除线索举报失败')
         
        #在后台已处理信息举报列表查看
        Log.LogOutput(LogLevel.DEBUG, "------爆料举报举报后后台查看------")
        getInfoReportDict = copy.deepcopy(XinXiGuanLiPara.getInformationReportPara)
        getInfoReportDict['informationReport.infoType'] = InfoType.CLUE
        getInfoReportDict['informationReport.state'] = 1 #表示未处理
         
        checkInfoReportDict = copy.deepcopy(XinXiGuanLiPara.checkInformationReportPara)
        checkInfoReportDict['contentText'] = newClueByNewUser['information']['contentText']
        checkInfoReportDict['address'] = newClueByNewUser['information']['address']
         
        ret = XinXiGuanLiIntf.check_information_report_in_list(getInfoReportDict, checkInfoReportDict)
        self.assertTrue(ret, '在举报信息中检查举报失败')
         
        #手机端重新举报
        Log.LogOutput(LogLevel.DEBUG, "------爆料举报删除后手机端重新举报，后台查看------")
        clueId = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from INFORMATIONS t where t.contenttext='%s'"%newClueByNewUser['information']['contentText'])
        addClueInfoReportDict = copy.deepcopy(XsBaoLiaoPara.addClueInfoReportPara)
        addClueInfoReportDict['infoId'] = clueId
        addClueInfoReportDict['reportUserId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from USERS t where t.mobile='%s'" % Global.XianSuoDftMobile)
        addClueInfoReportDict['publishUserMobile'] = newMobilePhone
        ret = XsBaoLiaoIntf.add_clue_information_report(addClueInfoReportDict)
         
        #后台举报信息未处理列表不再出现该举报
        getInfoReportDict = copy.deepcopy(XinXiGuanLiPara.getInformationReportPara)
        getInfoReportDict['informationReport.infoType'] = InfoType.CLUE
        getInfoReportDict['informationReport.state'] = 0 #表示未处理
         
        checkInfoReportDict = copy.deepcopy(XinXiGuanLiPara.checkInformationReportPara)
        checkInfoReportDict['contentText'] = newClueByNewUser['information']['contentText']
        checkInfoReportDict['address'] = newClueByNewUser['information']['address']
         
        ret = XinXiGuanLiIntf.check_information_report_in_list(getInfoReportDict, checkInfoReportDict)
        self.assertFalse(ret, '解除举报后，重新举报，后台还是生成举报记录')
         
        #重新爆料
        Log.LogOutput(LogLevel.DEBUG, "------进行爆料举报不公开操作------")
        newClueByNewUser = copy.deepcopy(XsBaoLiaoPara.xinZeng2) 
        newClueByNewUser['information']['contentText'] = '事件描述%s' % CommonUtil.createRandomString()
#         newClueByNewUser['information']['baiduX'] = '120.1362348153468'
#         newClueByNewUser['information']['baiduY'] = '30.28016484243025'
#         newClueByNewUser['information']['x'] = '120.1250430287559'
#         newClueByNewUser['information']['y'] = '30.27612037575986'         
        newClueByNewUser['information']['address'] = 'addres'+CommonUtil.createRandomString()
        responseDict = XsBaoLiaoIntf.addXianSuo(newClueByNewUser,mobile=newMobilePhone)
        self.assertTrue(responseDict.result, '新增线索失败')
         
        #举报
        clueId = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from INFORMATIONS t where t.contenttext='%s'"%newClueByNewUser['information']['contentText'])
        addClueInfoReportDict = copy.deepcopy(XsBaoLiaoPara.addClueInfoReportPara)
        addClueInfoReportDict['infoId'] = clueId
        addClueInfoReportDict['reportUserId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from USERS t where t.mobile='%s'" % Global.XianSuoDftMobile)
        addClueInfoReportDict['publishUserMobile'] = newMobilePhone
        ret = XsBaoLiaoIntf.add_clue_information_report(addClueInfoReportDict)
        self.assertTrue(ret, '新增线索举报失败')
         
        #设置为不公开
        shieldInfoReportDict = copy.deepcopy(XinXiGuanLiPara.shieldInfoReportPara)
        shieldInfoReportDict['ids[]'] = XinXiGuanLiIntf.get_information_report_id_by_content(newClueByNewUser['information']['contentText'], getInfoReportDict)
        shieldInfoReportDict['infoType'] = 0 #表示未处理 
        ret = XinXiGuanLiIntf.shield_information_report(shieldInfoReportDict)
        self.assertTrue(ret, '线索举报不公开失败')
         
        #在后台已处理列表显示举报信息
        Log.LogOutput(LogLevel.DEBUG, "------爆料举报不公开后后台及手机端查看------")
        getInfoReportDict = copy.deepcopy(XinXiGuanLiPara.getInformationReportPara)
        getInfoReportDict['informationReport.infoType'] = InfoType.CLUE
        getInfoReportDict['informationReport.state'] = 1 #表示未处理
         
        checkInfoReportDict = copy.deepcopy(XinXiGuanLiPara.checkInformationReportPara)
        checkInfoReportDict['contentText'] = newClueByNewUser['information']['contentText']
        checkInfoReportDict['address'] = newClueByNewUser['information']['address']
         
        ret = XinXiGuanLiIntf.check_information_report_in_list(getInfoReportDict, checkInfoReportDict)
        self.assertTrue(ret, '在举报信息中检查举报失败')
 
        #在手机端检查爆料是否不显示
        appClueCheckDict = copy.deepcopy(XsBaoLiaoPara.checkClueInSquarePara)
        appClueCheckDict['contentText'] = newClueByNewUser['information']['contentText']
        appClueCheckDict['address'] = newClueByNewUser['information']['address']
        ret = XsBaoLiaoIntf.check_clue_in_clue_list(appClueCheckDict)
        self.assertFalse(ret, '删除的举报信息在手机列表中还是存在')
        
        #新增说说
        Log.LogOutput(LogLevel.DEBUG, "------开始进行说说举报删除操作------")
        addShuoShuoOne = copy.deepcopy(ShuoShuoPara.addShuoShuoPara)
        addShuoShuoOne['casualTalk']['contentText'] = 'addOneShuoshuo%s' % CommonUtil.createRandomString()
        addShuoShuoOne['casualTalk']['title'] = 'addOneShuoshuo%s' % CommonUtil.createRandomString()
        ret = ShuoShuoIntf.add_shuoshuo(addShuoShuoOne,mobile=newMobilePhone)
        
        #举报
        shuoshuoId = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from CASUALTALKS t where t.contenttext='%s'" % addShuoShuoOne['casualTalk']['contentText'])
        addShuoShuoInfoReportDict = copy.deepcopy(ShuoShuoPara.addShuoShuoInfoReportPara)
        addShuoShuoInfoReportDict['infoId'] = shuoshuoId
        addShuoShuoInfoReportDict['infoType'] = InfoType.SHUOSHUO
        addShuoShuoInfoReportDict['reportUserId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from USERS t where t.mobile='%s'" % Global.XianSuoDftMobile)
        addShuoShuoInfoReportDict['publishUserMobile'] = newMobilePhone
        ret = ShuoShuoIntf.add_shuoshuo_information_report(addShuoShuoInfoReportDict)
        self.assertTrue(ret, '新增说说举报失败')
        
        #删除  
        #对举报进行删除
        getInfoReportDict = copy.deepcopy(XinXiGuanLiPara.getInformationReportPara)
        getInfoReportDict['informationReport.infoType'] = InfoType.SHUOSHUO
        getInfoReportDict['informationReport.state'] = 0 #表示未处理
        
        Log.LogOutput(LogLevel.DEBUG, "------说说举报删除后后台及手机端查看------")
        deleteInfoReportDict = copy.deepcopy(XinXiGuanLiPara.deleteInfoReportPara)
        deleteInfoReportDict['ids[]'] = XinXiGuanLiIntf.get_information_report_id_by_content(addShuoShuoOne['casualTalk']['contentText'], getInfoReportDict)
        deleteInfoReportDict['infoType'] = InfoType.SHUOSHUO
        ret = XinXiGuanLiIntf.delete_certain_information_report(deleteInfoReportDict)
        self.assertTrue(ret, '删除举报信息失败')
         
        #在后台说说已处理列表可以查看
        getInfoReportDict = copy.deepcopy(XinXiGuanLiPara.getInformationReportPara)
        getInfoReportDict['informationReport.infoType'] = InfoType.SHUOSHUO
        getInfoReportDict['informationReport.state'] = 1 #表示已处理
         
        checkInfoReportDict = copy.deepcopy(XinXiGuanLiPara.checkInformationReportPara)
        checkInfoReportDict['contentText'] = addShuoShuoOne['casualTalk']['contentText']
         
        ret = XinXiGuanLiIntf.check_information_report_in_list(getInfoReportDict, checkInfoReportDict)
        self.assertTrue(ret, '在举报信息中检查举报失败')
        
        #在手机端说说列表查看
        getShuoShuoListDict = copy.deepcopy(ShuoShuoPara.getShuoShuoPara)
        getShuoShuoListDict['userId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from USERS t where t.mobile='%s'" % Global.XianSuoDftMobile)
        
        checkShuoSHuoListDict = copy.deepcopy(ShuoShuoPara.checkShuoShuoPara)
        checkShuoSHuoListDict['contentText'] = addShuoShuoOne['casualTalk']['contentText']
        checkShuoSHuoListDict['nickName'] = "nick_%s" % newMobilePhone
        ret = ShuoShuoIntf.check_shuoshuo_in_list(checkShuoSHuoListDict,getShuoShuoListDict)
        self.assertFalse(ret, '说说举报信息删除后手机说说列表还存在')
        #因说说举报解除与删除类似，就不检查了
        
        #爆料转说说
        #重新爆料
        Log.LogOutput(LogLevel.DEBUG, "------进行爆料转说说操作------")
        newClueByNewUser = copy.deepcopy(XsBaoLiaoPara.xinZeng2) 
        newClueByNewUser['information']['contentText'] = '事件描述%s' % CommonUtil.createRandomString()
#         newClueByNewUser['information']['baiduX'] = '120.1362348153468'
#         newClueByNewUser['information']['baiduY'] = '30.28016484243025'
#         newClueByNewUser['information']['x'] = '120.1250430287559'
#         newClueByNewUser['information']['y'] = '30.27612037575986'         
        newClueByNewUser['information']['address'] = 'addres'+CommonUtil.createRandomString()
        responseDict = XsBaoLiaoIntf.addXianSuo(newClueByNewUser,mobile=newMobilePhone)
        self.assertTrue(responseDict.result, '新增线索失败')
         
        #举报
        clueId = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from INFORMATIONS t where t.contenttext='%s'"%newClueByNewUser['information']['contentText'])
        addClueInfoReportDict = copy.deepcopy(XsBaoLiaoPara.addClueInfoReportPara)
        addClueInfoReportDict['infoId'] = clueId
        addClueInfoReportDict['reportUserId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from USERS t where t.mobile='%s'" % Global.XianSuoDftMobile)
        addClueInfoReportDict['publishUserMobile'] = newMobilePhone
        ret = XsBaoLiaoIntf.add_clue_information_report(addClueInfoReportDict)
        self.assertTrue(ret, '新增线索举报失败')
        
        #爆料转说说,现获取爆料举报信息ID
        getInfoReportDict = copy.deepcopy(XinXiGuanLiPara.getInformationReportPara)
        getInfoReportDict['informationReport.infoType'] = InfoType.CLUE
        getInfoReportDict['informationReport.state'] = 0 #表示未处理
        clueInfoId = XinXiGuanLiIntf.get_information_report_id_by_content(newClueByNewUser['information']['contentText'], getInfoReportDict)
        
        ret = XinXiGuanLiIntf.convert_information_report_to_shuoshuo(clueInfoId)
        self.assertTrue(ret, '举报信息爆料转说说失败')
        
        #在手机端说说列表查看
        getShuoShuoListDict = copy.deepcopy(ShuoShuoPara.getShuoShuoPara)
        getShuoShuoListDict['userId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from USERS t where t.mobile='%s'" % Global.XianSuoDftMobile)
        
        checkShuoSHuoListDict = copy.deepcopy(ShuoShuoPara.checkShuoShuoPara)
        checkShuoSHuoListDict['contentText'] = newClueByNewUser['information']['contentText']
        checkShuoSHuoListDict['nickName'] = "nick_%s" % newMobilePhone
        ret = ShuoShuoIntf.check_shuoshuo_in_list(checkShuoSHuoListDict,getShuoShuoListDict)
        self.assertTrue(ret, '说说举报信息删除后手机说说列表还存在')
             
    def test_info_report_search_07(self): 
        """举报信息查询操作-850"""
        if Global.simulationEnvironment is True:
            Log.LogOutput(message='仿真环境跳过')
            pass
        else:
            #删除所有后台关键字设置
            XiTongPeiZhiIntf.delete_all_keyword_setting()
            #删除所有举报信息
            XinXiGuanLiIntf.delete_all_information_report()
            #添加一个手机账号，用于手机号快速搜索验证
            newMobilePhone = '13588806928'
            XsGongZuoTaiIntf.initUser(mobile=newMobilePhone)
            #判断是否有以下两个爆料主题，如没有，则新增
            clueThemeAddOne = copy.deepcopy(XiTongPeiZhiPara.themeAddDict)
            clueThemeAddOne['themeContent.name'] = "爆料测试主题1"
            clueThemeAddOne['themeContent.description'] = "爆料测试描述1"
            
            clueThemeAddTwo = copy.deepcopy(XiTongPeiZhiPara.themeAddDict)
            clueThemeAddTwo['themeContent.name'] = "爆料测试主题2"
            clueThemeAddTwo['themeContent.description'] = "爆料测试描述2"
            count0 = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select count(*) from THEMECONTENTS t where t.name='%s'" % clueThemeAddOne['themeContent.name'])
            count1 = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select count(*) from THEMECONTENTS t where t.name='%s'" % clueThemeAddTwo['themeContent.name'])
            if count0 == 0:
                XiTongPeiZhiIntf.add_theme(clueThemeAddOne)
            if count1 == 0:
                XiTongPeiZhiIntf.add_theme(clueThemeAddTwo)
            
            #判断是否有以下两个说说主题，如没有，则新增
            shuoshuoThemeAddOne = copy.deepcopy(XiTongPeiZhiPara.themeAddDict)
            shuoshuoThemeAddOne['themeContent.name'] = "说说测试主题1"
            shuoshuoThemeAddOne['themeContent.description'] = "说说测试描述1"
            shuoshuoThemeAddOne['themeRelation.infoType'] = InfoType.SHUOSHUO
            
            shuoshuoThemeAddTwo = copy.deepcopy(XiTongPeiZhiPara.themeAddDict)
            shuoshuoThemeAddTwo['themeContent.name'] = "说说测试主题2"
            shuoshuoThemeAddTwo['themeContent.description'] = "说说测试描述2"
            count0 = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select count(*) from THEMECONTENTS t where t.name='%s'" % shuoshuoThemeAddOne['themeContent.name'])
            count1 = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select count(*) from THEMECONTENTS t where t.name='%s'" % shuoshuoThemeAddTwo['themeContent.name'])
            if count0 == 0:
                XiTongPeiZhiIntf.add_theme(shuoshuoThemeAddOne)
            if count1 == 0:
                XiTongPeiZhiIntf.add_theme(shuoshuoThemeAddTwo)
                
            #使用新手机爆料不同主题的两个爆料
            Log.LogOutput(LogLevel.DEBUG, "------使用新手机号爆料2个不同主题的爆料------")
            newClueThemeOne = copy.deepcopy(XsBaoLiaoPara.xinZeng2) 
            newClueThemeOne['information']['contentText'] = '事件描述%s' % CommonUtil.createRandomString()
    #         newClueThemeOne['information']['baiduX'] = '120.1362348153468'
    #         newClueThemeOne['information']['baiduY'] = '30.28016484243025'
    #         newClueThemeOne['information']['x'] = '120.1250430287559'
    #         newClueThemeOne['information']['y'] = '30.27612037575986'         
            newClueThemeOne['information']['address'] = 'addres'+CommonUtil.createRandomString()
            newClueThemeOne['information']['themeContentId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from THEMECONTENTS t where t.name='%s'" % clueThemeAddOne['themeContent.name'])
            responseDict = XsBaoLiaoIntf.addXianSuo(newClueThemeOne,mobile=newMobilePhone)
            self.assertTrue(responseDict.result, '新增线索失败')
            
            newClueThemeTwo = copy.deepcopy(XsBaoLiaoPara.xinZeng2) 
            newClueThemeTwo['information']['contentText'] = '事件描述%s' % CommonUtil.createRandomString()
#             newClueThemeTwo['information']['baiduX'] = '120.1362348153468'
#             newClueThemeTwo['information']['baiduY'] = '30.28016484243025'
#             newClueThemeTwo['information']['x'] = '120.1250430287559'
#             newClueThemeTwo['information']['y'] = '30.27612037575986'         
            newClueThemeTwo['information']['address'] = 'addres'+CommonUtil.createRandomString()
            newClueThemeTwo['information']['themeContentId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from THEMECONTENTS t where t.name='%s'" % clueThemeAddTwo['themeContent.name'])
            responseDict = XsBaoLiaoIntf.addXianSuo(newClueThemeTwo,mobile=newMobilePhone)
            self.assertTrue(responseDict.result, '新增线索失败')
            
            #使用默认手机新增一条爆料
            Log.LogOutput(LogLevel.DEBUG, "------使用默认手机添加一个爆料------")
            defaultClueThemeOne = copy.deepcopy(XsBaoLiaoPara.xinZeng2) 
            defaultClueThemeOne['information']['contentText'] = '事件描述%s' % CommonUtil.createRandomString()
#             defaultClueThemeOne['information']['baiduX'] = '120.1362348153468'
#             defaultClueThemeOne['information']['baiduY'] = '30.28016484243025'
#             defaultClueThemeOne['information']['x'] = '120.1250430287559'
#             defaultClueThemeOne['information']['y'] = '30.27612037575986'         
            defaultClueThemeOne['information']['address'] = 'addres'+CommonUtil.createRandomString()
            defaultClueThemeOne['information']['themeContentId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from THEMECONTENTS t where t.name='%s'" % clueThemeAddOne['themeContent.name'])
            responseDict = XsBaoLiaoIntf.addXianSuo(defaultClueThemeOne)
            self.assertTrue(responseDict.result, '新增线索失败')
            
            #使用新手机号新增两条不同主题的说说
            Log.LogOutput(LogLevel.DEBUG, "------使用新手机添加2个不同主题的说说------")
            addShuoShuoOne = copy.deepcopy(ShuoShuoPara.addShuoShuoPara)
            addShuoShuoOne['casualTalk']['contentText'] = '说说内容%s' % CommonUtil.createRandomString()
            addShuoShuoOne['casualTalk']['title'] = '说说标题%s' % CommonUtil.createRandomString()
            addShuoShuoOne['casualTalk']['themeContentId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from THEMECONTENTS t where t.name='%s'" % shuoshuoThemeAddOne['themeContent.name'])
            ret = ShuoShuoIntf.add_shuoshuo(addShuoShuoOne,mobile=newMobilePhone)
            
            addShuoShuoTwo = copy.deepcopy(ShuoShuoPara.addShuoShuoPara)
            addShuoShuoTwo['casualTalk']['contentText'] = '说说内容%s' % CommonUtil.createRandomString()
            addShuoShuoTwo['casualTalk']['title'] = '说说标题%s' % CommonUtil.createRandomString()
            addShuoShuoTwo['casualTalk']['themeContentId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from THEMECONTENTS t where t.name='%s'" % shuoshuoThemeAddTwo['themeContent.name'])
            ret = ShuoShuoIntf.add_shuoshuo(addShuoShuoTwo,mobile=newMobilePhone)
            
            #使用默认手机新增一个说说
            Log.LogOutput(LogLevel.DEBUG, "------使用默认手机添加1个说说------")
            addShuoShuoDefaultUser = copy.deepcopy(ShuoShuoPara.addShuoShuoPara)
            addShuoShuoDefaultUser['casualTalk']['contentText'] = '说说内容%s' % CommonUtil.createRandomString()
            addShuoShuoDefaultUser['casualTalk']['title'] = '说说标题%s' % CommonUtil.createRandomString()
            addShuoShuoDefaultUser['casualTalk']['themeContentId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from THEMECONTENTS t where t.name='%s'" % shuoshuoThemeAddOne['themeContent.name'])
            ret = ShuoShuoIntf.add_shuoshuo(addShuoShuoDefaultUser)
            
            #使用默认手机号举报新手机号新增的爆料和说说
            Log.LogOutput(LogLevel.DEBUG, "------使用默认手机举报新手机号的爆料和说说------")
            clueId = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from INFORMATIONS t where t.contenttext='%s'"%newClueThemeOne['information']['contentText'])
            addClueInfoReportDict = copy.deepcopy(XsBaoLiaoPara.addClueInfoReportPara)
            addClueInfoReportDict['infoId'] = clueId
            addClueInfoReportDict['reportUserId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from USERS t where t.mobile='%s'" % Global.XianSuoDftMobile)
            addClueInfoReportDict['reportUserMobile'] = Global.XianSuoDftMobile       
            addClueInfoReportDict['publishUserMobile'] = newMobilePhone
            ret = XsBaoLiaoIntf.add_clue_information_report(addClueInfoReportDict)
            self.assertTrue(ret, '新增线索举报失败')
            
            clueId = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from INFORMATIONS t where t.contenttext='%s'"%newClueThemeTwo['information']['contentText'])
            addClueInfoReportDict['infoId'] = clueId
            ret = XsBaoLiaoIntf.add_clue_information_report(addClueInfoReportDict)
            self.assertTrue(ret, '新增线索举报失败')
            
            #说说举报
            shuoshuoId = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from CASUALTALKS t where t.contenttext='%s'" % addShuoShuoOne['casualTalk']['contentText'])
            addShuoShuoInfoReportDict = copy.deepcopy(ShuoShuoPara.addShuoShuoInfoReportPara)
            addShuoShuoInfoReportDict['infoId'] = shuoshuoId
            addShuoShuoInfoReportDict['infoType'] = InfoType.SHUOSHUO
            addShuoShuoInfoReportDict['reportUserId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from USERS t where t.mobile='%s'" % Global.XianSuoDftMobile)
            addShuoShuoInfoReportDict['reportUserMobile'] = Global.XianSuoDftMobile 
            addShuoShuoInfoReportDict['publishUserMobile'] = newMobilePhone
            ret = ShuoShuoIntf.add_shuoshuo_information_report(addShuoShuoInfoReportDict)
            self.assertTrue(ret, '新增说说举报失败')
            
            shuoshuoId = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from CASUALTALKS t where t.contenttext='%s'" % addShuoShuoTwo['casualTalk']['contentText'])
            addShuoShuoInfoReportDict['infoId'] = shuoshuoId
            ret = ShuoShuoIntf.add_shuoshuo_information_report(addShuoShuoInfoReportDict)
            self.assertTrue(ret, '新增说说举报失败')
            
            #使用新手机号举报默认手机号新增的爆料和说说
            Log.LogOutput(LogLevel.DEBUG, "------使用新手机举报默认手机号的爆料和说说------")
            clueId = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from INFORMATIONS t where t.contenttext='%s'"%defaultClueThemeOne['information']['contentText'])
            addClueInfoReportDict = copy.deepcopy(XsBaoLiaoPara.addClueInfoReportPara)
            addClueInfoReportDict['infoId'] = clueId
            addClueInfoReportDict['reportType'] = ReportType.BROADCAST
            addClueInfoReportDict['reportUserId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from USERS t where t.mobile='%s'" % newMobilePhone)
            addClueInfoReportDict['reportUserMobile'] = newMobilePhone
            addClueInfoReportDict['publishUserMobile'] = Global.XianSuoDftMobile
            ret = XsBaoLiaoIntf.add_clue_information_report(addClueInfoReportDict,mobile=newMobilePhone)
            self.assertTrue(ret, '新增线索举报失败')
            
            shuoshuoId = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from CASUALTALKS t where t.contenttext='%s'" % addShuoShuoDefaultUser['casualTalk']['contentText'])
            addShuoShuoInfoReportDict = copy.deepcopy(ShuoShuoPara.addShuoShuoInfoReportPara)
            addShuoShuoInfoReportDict['infoId'] = shuoshuoId
            addShuoShuoInfoReportDict['infoType'] = InfoType.SHUOSHUO
            addShuoShuoInfoReportDict['reportType'] = ReportType.BROADCAST
            addShuoShuoInfoReportDict['reportUserId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from USERS t where t.mobile='%s'" % newMobilePhone)
            addShuoShuoInfoReportDict['reportUserMobile'] = newMobilePhone
            addShuoShuoInfoReportDict['publishUserMobile'] = Global.XianSuoDftMobile
            ret = ShuoShuoIntf.add_shuoshuo_information_report(addShuoShuoInfoReportDict)
            self.assertTrue(ret, '新增说说举报失败')
            
            #===========================
            #通过主题查询，目前105环境有问题，暂时跳过       
            #===========================
            
            #在爆料、待处理列表查看举报信息
            Log.LogOutput(LogLevel.DEBUG, "------在爆料\待处理列表查看举报信息------")
            getInfoReportDict = copy.deepcopy(XinXiGuanLiPara.getInformationReportPara)
            getInfoReportDict['informationReport.infoType'] = InfoType.CLUE
            getInfoReportDict['informationReport.state'] = ReportState.UNHANDLE #表示未处理
             
            checkInfoReportDict = copy.deepcopy(XinXiGuanLiPara.checkInformationReportPara)
            checkInfoReportDict['contentText'] = newClueThemeOne['information']['contentText']
            checkInfoReportDict['address'] = newClueThemeOne['information']['address']
             
            ret = XinXiGuanLiIntf.check_information_report_in_list(getInfoReportDict, checkInfoReportDict)
            self.assertTrue(ret, '在爆料待处理页面未检查到爆料举报信息')
            
            checkInfoReportDict['contentText'] = addShuoShuoOne['casualTalk']['contentText']
            checkInfoReportDict['address'] = None
            ret = XinXiGuanLiIntf.check_information_report_in_list(getInfoReportDict, checkInfoReportDict)
            self.assertFalse(ret, '在爆料待处理页面检查到说说举报信息')
            
            #在说说待处理页面检查说说和爆料举报
            Log.LogOutput(LogLevel.DEBUG, "------在说说\待处理列表查看举报信息------")
            getInfoReportDict = copy.deepcopy(XinXiGuanLiPara.getInformationReportPara)
            getInfoReportDict['informationReport.infoType'] = InfoType.SHUOSHUO
            getInfoReportDict['informationReport.state'] = ReportState.UNHANDLE #表示未处理
             
            checkInfoReportDict = copy.deepcopy(XinXiGuanLiPara.checkInformationReportPara)
            checkInfoReportDict['contentText'] = newClueThemeOne['information']['contentText']
            checkInfoReportDict['address'] = newClueThemeOne['information']['address']
             
            ret = XinXiGuanLiIntf.check_information_report_in_list(getInfoReportDict, checkInfoReportDict)
            self.assertFalse(ret, '在说说待处理页面检查到爆料举报信息')
            
            checkInfoReportDict['contentText'] = addShuoShuoOne['casualTalk']['contentText']
            checkInfoReportDict['address'] = None
            ret = XinXiGuanLiIntf.check_information_report_in_list(getInfoReportDict, checkInfoReportDict)
            self.assertTrue(ret, '在说说待处理页面未检查到说说举报信息')
            
            #通过举报人手机号(默认手机号)查询，默认手机号举报的信息可以看到
            Log.LogOutput(LogLevel.DEBUG, "------在爆料\待处理列表通过举报人手机号查看------")
            getInfoReportDict = copy.deepcopy(XinXiGuanLiPara.getInformationReportPara)
            getInfoReportDict['informationReport.infoType'] = InfoType.CLUE
            getInfoReportDict['informationReport.reportUserMobile'] = Global.XianSuoDftMobile
            getInfoReportDict['informationReport.state'] = ReportState.UNHANDLE #表示未处理
             
            checkInfoReportDict = copy.deepcopy(XinXiGuanLiPara.checkInformationReportPara)
            checkInfoReportDict['contentText'] = newClueThemeOne['information']['contentText']
            checkInfoReportDict['address'] = newClueThemeOne['information']['address']
             
            ret = XinXiGuanLiIntf.check_information_report_in_list(getInfoReportDict, checkInfoReportDict)
            self.assertTrue(ret, '在爆料待处理页面未检查到符合举报手机号的信息')
            
            checkInfoReportDict = copy.deepcopy(XinXiGuanLiPara.checkInformationReportPara)
            checkInfoReportDict['contentText'] = newClueThemeTwo['information']['contentText']
            checkInfoReportDict['address'] = newClueThemeTwo['information']['address']
             
            ret = XinXiGuanLiIntf.check_information_report_in_list(getInfoReportDict, checkInfoReportDict)
            self.assertTrue(ret, '在爆料待处理页面未检查到符合举报手机号的信息')
            
            #新手机号举报的信息被过滤
            checkInfoReportDict = copy.deepcopy(XinXiGuanLiPara.checkInformationReportPara)
            checkInfoReportDict['contentText'] = defaultClueThemeOne['information']['contentText']
            checkInfoReportDict['address'] = defaultClueThemeOne['information']['address']
             
            ret = XinXiGuanLiIntf.check_information_report_in_list(getInfoReportDict, checkInfoReportDict)
            self.assertFalse(ret, '在爆料待处理页面检查到不符合举报手机号的信息')
            
            
            #通过发布人手机号(默认手机号)查询，默认手机号举报的信息无法看到
            Log.LogOutput(LogLevel.DEBUG, "------在爆料\待处理列表通过发布人手机号查看------")
            getInfoReportDict = copy.deepcopy(XinXiGuanLiPara.getInformationReportPara)
            getInfoReportDict['informationReport.infoType'] = InfoType.CLUE
            getInfoReportDict['informationReport.publishUserMobile'] = Global.XianSuoDftMobile
            getInfoReportDict['informationReport.state'] = ReportState.UNHANDLE #表示未处理
             
            checkInfoReportDict = copy.deepcopy(XinXiGuanLiPara.checkInformationReportPara)
            checkInfoReportDict['contentText'] = newClueThemeOne['information']['contentText']
            checkInfoReportDict['address'] = newClueThemeOne['information']['address']
             
            ret = XinXiGuanLiIntf.check_information_report_in_list(getInfoReportDict, checkInfoReportDict)
            self.assertFalse(ret, '在爆料待处理页面检查到不符合发布人手机号的信息')
            
            checkInfoReportDict = copy.deepcopy(XinXiGuanLiPara.checkInformationReportPara)
            checkInfoReportDict['contentText'] = newClueThemeTwo['information']['contentText']
            checkInfoReportDict['address'] = newClueThemeTwo['information']['address']
             
            ret = XinXiGuanLiIntf.check_information_report_in_list(getInfoReportDict, checkInfoReportDict)
            self.assertFalse(ret, '在爆料待处理页面检查到不符合发布人手机号的信息')
            
            #新手机号举报的信息可以看到
            checkInfoReportDict = copy.deepcopy(XinXiGuanLiPara.checkInformationReportPara)
            checkInfoReportDict['contentText'] = defaultClueThemeOne['information']['contentText']
            checkInfoReportDict['address'] = defaultClueThemeOne['information']['address']
             
            ret = XinXiGuanLiIntf.check_information_report_in_list(getInfoReportDict, checkInfoReportDict)
            self.assertTrue(ret, '在爆料待处理页面未检查到符合发布人手机号的信息')
            
            #通过举报类型查看
            Log.LogOutput(LogLevel.DEBUG, "------在爆料\待处理列表通过举报类型查看------")
            getInfoReportDict = copy.deepcopy(XinXiGuanLiPara.getInformationReportPara)
            getInfoReportDict['informationReport.infoType'] = InfoType.CLUE
            getInfoReportDict['informationReport.reportType'] = ReportType.OTHER
            getInfoReportDict['informationReport.state'] = ReportState.UNHANDLE #表示未处理
             
            checkInfoReportDict = copy.deepcopy(XinXiGuanLiPara.checkInformationReportPara)
            checkInfoReportDict['contentText'] = newClueThemeOne['information']['contentText']
            checkInfoReportDict['address'] = newClueThemeOne['information']['address']
             
            ret = XinXiGuanLiIntf.check_information_report_in_list(getInfoReportDict, checkInfoReportDict)
            self.assertTrue(ret, '在爆料待处理页面未检查到符合发布类型的信息')
            
            #默认手机号新增的爆料类型是广告，因此应该查不到
            checkInfoReportDict['contentText'] = defaultClueThemeOne['information']['contentText']
            checkInfoReportDict['address'] = defaultClueThemeOne['information']['address']
            ret = XinXiGuanLiIntf.check_information_report_in_list(getInfoReportDict, checkInfoReportDict)
            self.assertFalse(ret, '在爆料待处理页面检查到不符合爆料类型的的信息')
            
            #对一条爆料举报消息进行删除，通过处理状态进行搜索
            Log.LogOutput(LogLevel.DEBUG, "------爆料举报进行删除，该举报变为已处理------")       
            getInfoReportDict = copy.deepcopy(XinXiGuanLiPara.getInformationReportPara)
            getInfoReportDict['informationReport.infoType'] = InfoType.CLUE
            getInfoReportDict['informationReport.state'] = ReportState.UNHANDLE #表示未处理
            
            deleteInfoReportDict = copy.deepcopy(XinXiGuanLiPara.deleteInfoReportPara)
            deleteInfoReportDict['ids[]'] = XinXiGuanLiIntf.get_information_report_id_by_content(newClueThemeOne['information']['contentText'], getInfoReportDict)
            deleteInfoReportDict['infoType'] = InfoType.CLUE
            ret = XinXiGuanLiIntf.delete_certain_information_report(deleteInfoReportDict)
            self.assertTrue(ret, '删除举报信息失败')
            
            #通过爆料未处理和已处理分别搜索
            Log.LogOutput(LogLevel.DEBUG, "------爆料举报未处理搜索------")
            getInfoReportDict = copy.deepcopy(XinXiGuanLiPara.getInformationReportPara)
            getInfoReportDict['informationReport.infoType'] = InfoType.CLUE
            getInfoReportDict['informationReport.state'] = ReportState.UNHANDLE #表示未处理
             
            checkInfoReportDict = copy.deepcopy(XinXiGuanLiPara.checkInformationReportPara)
            checkInfoReportDict['contentText'] = newClueThemeOne['information']['contentText']
            checkInfoReportDict['address'] = newClueThemeOne['information']['address']
             
            ret = XinXiGuanLiIntf.check_information_report_in_list(getInfoReportDict, checkInfoReportDict)
            self.assertFalse(ret, '在爆料待处理页面检查到已经删除的信息')
            
            getInfoReportDict['informationReport.state'] = ReportState.HANDLED
            ret = XinXiGuanLiIntf.check_information_report_in_list(getInfoReportDict, checkInfoReportDict)
            self.assertTrue(ret, '在爆料已处理页面未检查到已经删除的信息')
            
            #举报时间和爆料时间测试性价比低，暂时不开发
        
    def test_delete_record_search_08(self): 
        """信息删除记录查询-852"""
        #清空信息删除记录表delinforecords
        if Global.simulationEnvironment is False:
            YunWeiCommonIntf.clearTableYunWei('delinforecords')
        #添加一个手机账号，用于手机号快速搜索验证
        newMobilePhone = '13588806928'
        XsGongZuoTaiIntf.initUser(mobile=newMobilePhone)
        
        #使用默认手机号新增一条线索和说说
        addClueDftMobile = copy.deepcopy(XsBaoLiaoPara.xinZeng2) 
        addClueDftMobile['information']['contentText'] = '事件描述%s' % CommonUtil.createRandomString()
#         addClueDftMobile['information']['baiduX'] = '120.1362348153468'
#         addClueDftMobile['information']['baiduY'] = '30.28016484243025'
#         addClueDftMobile['information']['x'] = '120.1250430287559'
#         addClueDftMobile['information']['y'] = '30.27612037575986'         
        addClueDftMobile['information']['address'] = 'addres'+CommonUtil.createRandomString()
        responseDict = XsBaoLiaoIntf.addXianSuo(addClueDftMobile)
        self.assertTrue(responseDict.result, '新增线索失败')
        
        addShuoShuoDftMobile = copy.deepcopy(ShuoShuoPara.addShuoShuoPara)
        addShuoShuoDftMobile['casualTalk']['contentText'] = '说说内容%s' % CommonUtil.createRandomString()
        addShuoShuoDftMobile['casualTalk']['title'] = '说说标题%s' % CommonUtil.createRandomString()
        ret = ShuoShuoIntf.add_shuoshuo(addShuoShuoDftMobile)
        self.assertTrue(ret, '新增说说失败')
        
        #使用新手机号新增一条爆料和说说
        addClueNewMobile = copy.deepcopy(XsBaoLiaoPara.xinZeng2) 
        addClueNewMobile['information']['contentText'] = '事件描述%s' % CommonUtil.createRandomString()
#         addClueNewMobile['information']['baiduX'] = '120.1362348153468'
#         addClueNewMobile['information']['baiduY'] = '30.28016484243025'
#         addClueNewMobile['information']['x'] = '120.1250430287559'
#         addClueNewMobile['information']['y'] = '30.27612037575986'         
        addClueNewMobile['information']['address'] = 'addres'+CommonUtil.createRandomString()
        responseDict = XsBaoLiaoIntf.addXianSuo(addClueNewMobile,mobile=newMobilePhone)
        self.assertTrue(responseDict.result, '新增线索失败')
        
        addShuoShuoNewMobile = copy.deepcopy(ShuoShuoPara.addShuoShuoPara)
        addShuoShuoNewMobile['casualTalk']['contentText'] = '说说内容%s' % CommonUtil.createRandomString()
        addShuoShuoNewMobile['casualTalk']['title'] = '说说标题%s' % CommonUtil.createRandomString()
        ret = ShuoShuoIntf.add_shuoshuo(addShuoShuoNewMobile,mobile=newMobilePhone)
        self.assertTrue(ret, '新增说说失败')
        
        #通过运维平台删除默认用户的爆料和新用户的说说
        deleteDftMobileClue = copy.deepcopy(XinXiGuanLiPara.delCluePara)
        deleteDftMobileClue['ids[]'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from INFORMATIONS t where t.contenttext='%s'" % addClueDftMobile['information']['contentText'])
        deleteDftMobileClue['deleteReason'] = '其他'
        ret = XinXiGuanLiIntf.deletexiansuo(deleteDftMobileClue)
        self.assertTrue(ret, '通过运维平台删除线索失败')
          
        deleteNewMobileShuoShuo = copy.deepcopy(XinXiGuanLiPara.delCluePara)
        deleteNewMobileShuoShuo['ids[]'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from CASUALTALKS t where t.contenttext='%s'" % addShuoShuoNewMobile['casualTalk']['contentText'])
        deleteNewMobileShuoShuo['deleteReason'] = newMobilePhone
        ret = XinXiGuanLiIntf.delete_shuoshuo(deleteNewMobileShuoShuo)
        self.assertTrue(ret, '通过运维平台删除说说失败')
          
        #通过省平台删除新用户的爆料和默认用户的说说
        deleteClueDict = copy.deepcopy(XianSuoGuanLiPara.deleteCluePara)
        deleteClueDict['delInfoRecord.informationId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from INFORMATIONS t where t.contenttext='%s'" % addClueNewMobile['information']['contentText'])
        deleteClueDict['delInfoRecord.mobile'] = newMobilePhone
        ret = XianSuoGuanLiIntf.delete_single_clue(deleteClueDict)
        self.assertTrue(ret, '通过省平台线索管理删除线索失败')
          
        deleteShuoShuoDict = copy.deepcopy(XianSuoGuanLiPara.shuoshuoDelDict)
        deleteShuoShuoDict['delInfoRecord.informationId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from CASUALTALKS t where t.contenttext='%s'" % addShuoShuoDftMobile['casualTalk']['contentText'])
        deleteShuoShuoDict['delInfoRecord.mobile'] = Global.XianSuoDftMobile
        ret = XianSuoGuanLiIntf.delete_one_shuoshuo(deleteShuoShuoDict)
        self.assertTrue(ret, '通过省平台说说管理删除说说失败')
        
        #通过默认手机号在线索列表查询，默认账号发布的爆料存在，新手机号的爆料不存在
        getDelRecordDict = copy.deepcopy(XinXiGuanLiPara.getDelRecordListPara)
        getDelRecordDict['delInfoRecord.mobile'] = Global.XianSuoDftMobile
        getDelRecordDict['delInfoRecord.infoType'] = InfoType.CLUE
        
        checkDelRecordDict = copy.deepcopy(XinXiGuanLiPara.checkDelRecordPara)
        checkDelRecordDict['contentText'] = addClueDftMobile['information']['contentText']
        
        ret = XinXiGuanLiIntf.check_delete_record_in_list(getDelRecordDict, checkDelRecordDict)
        self.assertTrue(ret, '通过手机号未搜索到符合要求的删除记录')
        
        checkDelRecordDict = copy.deepcopy(XinXiGuanLiPara.checkDelRecordPara)
        checkDelRecordDict['contentText'] = addClueNewMobile['information']['contentText']
        ret = XinXiGuanLiIntf.check_delete_record_in_list(getDelRecordDict, checkDelRecordDict)
        self.assertFalse(ret, '通过手机号搜索到不符合要求的删除记录')
        
        #在说说界面通过删除方式为省平台搜索
        getDelRecordDict = copy.deepcopy(XinXiGuanLiPara.getDelRecordListPara)
        getDelRecordDict['delInfoRecord.applicationType'] = DeleteType.YUNWEI
        getDelRecordDict['delInfoRecord.infoType'] = InfoType.SHUOSHUO
        
        checkDelRecordDict = copy.deepcopy(XinXiGuanLiPara.checkDelRecordPara)
        checkDelRecordDict['contentText'] = addShuoShuoNewMobile['casualTalk']['contentText']
        ret = XinXiGuanLiIntf.check_delete_record_in_list(getDelRecordDict, checkDelRecordDict)
        self.assertTrue(ret, '未搜索到通过运维方式删除的删除记录')
        
        checkDelRecordDict = copy.deepcopy(XinXiGuanLiPara.checkDelRecordPara)
        checkDelRecordDict['contentText'] = addShuoShuoDftMobile['casualTalk']['contentText']
        ret = XinXiGuanLiIntf.check_delete_record_in_list(getDelRecordDict, checkDelRecordDict)
        self.assertFalse(ret, '搜索到非运维方式删除的删除记录')
        
        #通过指定删除人员未zdhq@搜索爆料
        getDelRecordDict = copy.deepcopy(XinXiGuanLiPara.getDelRecordListPara)
        getDelRecordDict['delInfoRecord.deleteUser'] = InitDefaultPara.userInit['DftQuUser']
        getDelRecordDict['delInfoRecord.infoType'] = InfoType.CLUE
        
        checkDelRecordDict = copy.deepcopy(XinXiGuanLiPara.checkDelRecordPara)
        checkDelRecordDict['contentText'] = addClueNewMobile['information']['contentText']
        ret = XinXiGuanLiIntf.check_delete_record_in_list(getDelRecordDict, checkDelRecordDict)
        self.assertTrue(ret, '未搜索到大江东区用户删除的删除记录')
        
        checkDelRecordDict = copy.deepcopy(XinXiGuanLiPara.checkDelRecordPara)
        checkDelRecordDict['contentText'] = addClueDftMobile['information']['contentText']
        ret = XinXiGuanLiIntf.check_delete_record_in_list(getDelRecordDict, checkDelRecordDict)
        self.assertFalse(ret, '搜索到非大江东区用户删除的删除记录')
        pass
    def test_shuoshuo_search_09(self):
        """随便说说查询功能-860"""
        #添加一个手机账号，用于说说搜索验证
        newMobilePhone = '13588806928'
        XsGongZuoTaiIntf.initUser(mobile=newMobilePhone)
        
        #判断是否有以下两个说说主题，如没有，则新增
        shuoshuoThemeAddOne = copy.deepcopy(XiTongPeiZhiPara.themeAddDict)
        shuoshuoThemeAddOne['themeContent.name'] = "说说测试主题1"
        shuoshuoThemeAddOne['themeContent.description'] = "说说测试描述1"
        shuoshuoThemeAddOne['themeRelation.infoType'] = InfoType.SHUOSHUO
        
        shuoshuoThemeAddTwo = copy.deepcopy(XiTongPeiZhiPara.themeAddDict)
        shuoshuoThemeAddTwo['themeContent.name'] = "说说测试主题2"
        shuoshuoThemeAddTwo['themeContent.description'] = "说说测试描述2"
        count0 = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select count(*) from THEMECONTENTS t where t.name='%s'" % shuoshuoThemeAddOne['themeContent.name'])
        count1 = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select count(*) from THEMECONTENTS t where t.name='%s'" % shuoshuoThemeAddTwo['themeContent.name'])
        if count0 == 0:
            XiTongPeiZhiIntf.add_theme(shuoshuoThemeAddOne)
        if count1 == 0:
            XiTongPeiZhiIntf.add_theme(shuoshuoThemeAddTwo)
            
        #新增不同主题的两个说说
        addShuoShuoOne = copy.deepcopy(ShuoShuoPara.addShuoShuoPara)
        addShuoShuoOne['casualTalk']['contentText'] = 'talkContent%s' % CommonUtil.createRandomString()
        addShuoShuoOne['casualTalk']['title'] = 'talkTitle%s' % CommonUtil.createRandomString()
        addShuoShuoOne['casualTalk']['themeContentId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from THEMECONTENTS t where t.name='%s'" % shuoshuoThemeAddOne['themeContent.name'])
        ret = ShuoShuoIntf.add_shuoshuo(addShuoShuoOne,mobile=newMobilePhone)
        
        #使用默认手机新增一个说说
        Log.LogOutput(LogLevel.DEBUG, "------使用默认手机添加1个说说------")
        addShuoShuoDefaultUser = copy.deepcopy(ShuoShuoPara.addShuoShuoPara)
        addShuoShuoDefaultUser['casualTalk']['contentText'] = 'talkContent%s' % CommonUtil.createRandomString()
        addShuoShuoDefaultUser['casualTalk']['title'] = 'talkTitle%s' % CommonUtil.createRandomString()
        addShuoShuoDefaultUser['casualTalk']['themeContentId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from THEMECONTENTS t where t.name='%s'" % shuoshuoThemeAddTwo['themeContent.name'])
        ret = ShuoShuoIntf.add_shuoshuo(addShuoShuoDefaultUser)
        
        #通过手机号搜索
        Log.LogOutput(LogLevel.DEBUG, "------通过手机号搜索------")
        getShuoShuoDict = copy.deepcopy(XinXiGuanLiPara.getShuoShuoListPara)
        getShuoShuoDict['mobile'] = newMobilePhone
        
        checkShuoShuoDict = copy.deepcopy(XinXiGuanLiPara.checkShuoShuoPara)
        checkShuoShuoDict['contentText'] = addShuoShuoOne['casualTalk']['contentText']
        checkShuoShuoDict['title'] = addShuoShuoOne['casualTalk']['title']
        
        ret = XinXiGuanLiIntf.check_shuoshuo_in_list(checkShuoShuoDict, getShuoShuoDict)
        self.assertTrue(ret, '未搜索到符合手机号要求的说说')
        
        checkShuoShuoDict['contentText'] = addShuoShuoDefaultUser['casualTalk']['contentText']
        checkShuoShuoDict['title'] = addShuoShuoDefaultUser['casualTalk']['title']
        ret = XinXiGuanLiIntf.check_shuoshuo_in_list(checkShuoShuoDict, getShuoShuoDict)
        self.assertFalse(ret, '搜索到不符合手机号要求的说说')
        
        #通过主题搜索
        Log.LogOutput(LogLevel.DEBUG, "------通过主题搜索------")
        getShuoShuoDict = copy.deepcopy(XinXiGuanLiPara.getShuoShuoListPara)
        getShuoShuoDict['themeContentId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from THEMECONTENTS t where t.name='%s'" % shuoshuoThemeAddTwo['themeContent.name'])
        
        checkShuoShuoDict = copy.deepcopy(XinXiGuanLiPara.checkShuoShuoPara)
        checkShuoShuoDict['contentText'] = addShuoShuoOne['casualTalk']['contentText']
        checkShuoShuoDict['title'] = addShuoShuoOne['casualTalk']['title']
        
        ret = XinXiGuanLiIntf.check_shuoshuo_in_list(checkShuoShuoDict, getShuoShuoDict)
        self.assertFalse(ret, '搜索到不符合主题要求的说说')
        
        checkShuoShuoDict['contentText'] = addShuoShuoDefaultUser['casualTalk']['contentText']
        checkShuoShuoDict['title'] = addShuoShuoDefaultUser['casualTalk']['title']
        ret = XinXiGuanLiIntf.check_shuoshuo_in_list(checkShuoShuoDict, getShuoShuoDict)
        self.assertTrue(ret, '未搜索到符合主题要求的说说')
        
    def test_shuoshuo_highlight_10(self):
        """随便说说精彩推荐设置及置顶-861"""
        #新增两条说说
        addShuoShuoOneDefaultUser = copy.deepcopy(ShuoShuoPara.addShuoShuoPara)
        addShuoShuoOneDefaultUser['casualTalk']['contentText'] = 'talkContent%s' % CommonUtil.createRandomString()
        addShuoShuoOneDefaultUser['casualTalk']['title'] = 'talkTitle%s' % CommonUtil.createRandomString()
        ret = ShuoShuoIntf.add_shuoshuo(addShuoShuoOneDefaultUser)
        self.assertTrue(ret, '新增说说失败')
        
        addShuoShuoTwoDefaultUser = copy.deepcopy(ShuoShuoPara.addShuoShuoPara)
        addShuoShuoTwoDefaultUser['casualTalk']['contentText'] = 'talk%s' % CommonUtil.createRandomString()
        addShuoShuoTwoDefaultUser['casualTalk']['title'] = 'talkTitle%s' % CommonUtil.createRandomString()
        ret = ShuoShuoIntf.add_shuoshuo(addShuoShuoTwoDefaultUser)
        self.assertTrue(ret, '新增说说失败')
        
        #将一条说说设置为精彩推荐
        shuoshuoId = XinXiGuanLiIntf.get_shuoshuo_id_by_content(addShuoShuoOneDefaultUser['casualTalk']['contentText'])
        ret = XinXiGuanLiIntf.set_shuoshuo_to_highlight(shuoshuoId)
        self.assertTrue(ret, '设置说说为精彩推荐失败')
        
        #在列表查看说说是否被设置为精彩推荐
        getShuoShuoDict = copy.deepcopy(XinXiGuanLiPara.getShuoShuoListPara)
        
        checkShuoShuoDict = copy.deepcopy(XinXiGuanLiPara.checkShuoShuoPara)
        checkShuoShuoDict['contentText'] = addShuoShuoOneDefaultUser['casualTalk']['contentText']
        checkShuoShuoDict['title'] = addShuoShuoOneDefaultUser['casualTalk']['title']
        checkShuoShuoDict['showState'] = 1
        ret = XinXiGuanLiIntf.check_shuoshuo_in_list(checkShuoShuoDict, getShuoShuoDict)
        self.assertTrue(ret, '在列表查看精彩推荐说说失败')      
        
        #在手机端查看精彩推荐
        checkHighLightDict = copy.deepcopy(XsBaoLiaoPara.checkHighLightPara)
        checkHighLightDict['contentText'] = addShuoShuoOneDefaultUser['casualTalk']['contentText']
        checkHighLightDict['nickName'] = Global.XianSuoDftMobileNick
        
        ret = XsBaoLiaoIntf.check_highlight_info(checkHighLightDict)
        self.assertTrue(ret, '在手机端检查精彩推荐失败') 
        
        #将说说置顶
        ret = XinXiGuanLiIntf.set_shuoshuo_to_top(shuoshuoId)
        self.assertTrue(ret, '说说置顶失败')
        
        #检查说说置顶情况
        getShuoShuoDict = copy.deepcopy(XinXiGuanLiPara.getShuoShuoListPara)
        
        checkShuoShuoDict = copy.deepcopy(XinXiGuanLiPara.checkShuoShuoPara)
        checkShuoShuoDict['contentText'] = addShuoShuoOneDefaultUser['casualTalk']['contentText']
        checkShuoShuoDict['title'] = addShuoShuoOneDefaultUser['casualTalk']['title']
        checkShuoShuoDict['topState'] = 1
        ret = XinXiGuanLiIntf.check_shuoshuo_in_list(checkShuoShuoDict, getShuoShuoDict)
        self.assertTrue(ret, '在列表查看置顶说说失败')
        
        #在手机端查看置顶情况
        getShuoShuoDict = copy.deepcopy(ShuoShuoPara.getShuoShuoPara)
        
        checkShuoShuoDict = copy.deepcopy(ShuoShuoPara.checkShuoShuoPara)
        checkShuoShuoDict['contentText'] = addShuoShuoOneDefaultUser['casualTalk']['contentText']
        checkShuoShuoDict['title'] = addShuoShuoOneDefaultUser['casualTalk']['title']
        checkShuoShuoDict['topState'] = 1
        ret = ShuoShuoIntf.check_shuoshuo_in_list(checkShuoShuoDict, getShuoShuoDict)
        self.assertTrue(ret, '在手机端说说列表查看置顶失败')
        pass
    
    def tearDown(self):
        pass    
    
    
if __name__ == "__main__":
    suite = unittest.TestSuite()
#     suite.addTest(XinXiGuanLi("test_baoliaoguanli_01"))
#     suite.addTest(XinXiGuanLi("test_ClueTheme_02"))
#     suite.addTest(XinXiGuanLi("test_moblie_search_03"))
#     suite.addTest(XinXiGuanLi("test_user_deedback_04"))
#     suite.addTest(XinXiGuanLi("test_user_deedback_search_05"))
#     suite.addTest(XinXiGuanLi("test_information_report_06"))
#     suite.addTest(XinXiGuanLi("test_info_report_search_07"))

#     suite.addTest(XinXiGuanLi("test_delete_record_search_08"))
#     suite.addTest(XinXiGuanLi("test_shuoshuo_search_09"))
    suite.addTest(XinXiGuanLi("test_shuoshuo_highlight_10"))
  
    results = unittest.TextTestRunner().run(suite)
    pass    