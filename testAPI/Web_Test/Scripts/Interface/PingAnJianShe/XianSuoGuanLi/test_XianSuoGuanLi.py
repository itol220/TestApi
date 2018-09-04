# -*- coding:UTF-8 -*-
'''
Created on 2015-10-20

@author: ho
'''
from __future__ import unicode_literals
from COMMON import Log, CommonUtil
from CONFIG import Global
from CONFIG.Define import LogLevel
from Interface.PingAnJianShe.Common import CommonIntf
from Interface.PingAnJianShe.ShiJianChuLi import ShiJianChuLiIntf
from Interface.PingAnJianShe.SystemMgr import SystemMgrIntf
from Interface.PingAnJianShe.XianSuoGuanLi import XianSuoGuanLiPara, \
    XianSuoGuanLiIntf
from Interface.PingAnJianShe.XianSuoGuanLi.XianSuoGuanLiPara import ShowState, \
    DealState, OfficialState
from Interface.XianSuoApp.BaoLiao import XsBaoLiaoIntf, XsBaoLiaoPara
from Interface.XianSuoApp.GongZuoTai import XsGongZuoTaiIntf
from Interface.XianSuoApp.ShuoShuo import ShuoShuoPara, ShuoShuoIntf
from Interface.YunWeiPingTai.XiTongPeiZhi import XiTongPeiZhiPara, \
    XiTongPeiZhiIntf
from Interface.YunWeiPingTai.XinXiGuanLi import XinXiGuanLiIntf
from Interface.YunWeiPingTai.YunWeiCommon import YunWeiCommonIntf
import copy
import unittest

# reload(sys)
# sys.setdefaultencoding('utf-8')

class XianSuoGuanLi(unittest.TestCase):

    def setUp(self):
        #初始化用户
        XinXiGuanLiIntf.deleteyunwei()
        XsBaoLiaoIntf.deleteAllClues()
        XsGongZuoTaiIntf.initUser()
        ShiJianChuLiIntf.deleteAllIssues2()
        pass
    def testFastSearch(self):
        '''快速搜索'''
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
            
        #默认账号添加一条线索
        newClueByDftUser = copy.deepcopy(XsBaoLiaoPara.XinZeng) 
        newClueByDftUser['information']['contentText'] = '事件描述%s' % CommonUtil.createRandomString()
        newClueByDftUser['information']['baiduX'] = '120.4989885463861'
        newClueByDftUser['information']['baiduY'] = '30.27759299562879'
        newClueByDftUser['information']['x'] = '120.488114380334'
        newClueByDftUser['information']['y'] = '30.27759299562879'       
        newClueByDftUser['information']['address'] = 'addres'+CommonUtil.createRandomString()
        newClueByDftUser['information']['themeContentId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from THEMECONTENTS t where t.name='%s'" % themeAddOne['themeContent.name'])
        responseDict = XsBaoLiaoIntf.addXianSuo(newClueByDftUser)
        self.assertTrue(responseDict.result, '新增线索失败')
        #使用新账号新增一条线索
        #添加一个手机账号，用于手机号快速搜索验证
        newMobilePhone = '13588806928'
        newNickName = 'nick_%s' % newMobilePhone
        XsGongZuoTaiIntf.initUser(mobile=newMobilePhone)
        #初始化新用户的时候会默认设置昵称，昵称格式为"nick_手机号"
        newClueByNewUser = copy.deepcopy(XsBaoLiaoPara.XinZeng) 
        newClueByNewUser['information']['contentText'] = '事件描述%s' % CommonUtil.createRandomString()
        newClueByNewUser['information']['baiduX'] = '120.4989885463861'
        newClueByNewUser['information']['baiduY'] = '30.27759299562879'
        newClueByNewUser['information']['x'] = '120.488114380334'
        newClueByNewUser['information']['y'] = '30.27759299562879'       
        newClueByNewUser['information']['address'] = 'addres'+CommonUtil.createRandomString()
        newClueByNewUser['information']['themeContentId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from THEMECONTENTS t where t.name='%s'" % themeAddTwo['themeContent.name'])
        responseDict = XsBaoLiaoIntf.addXianSuo(newClueByNewUser,mobile=newMobilePhone)
        self.assertTrue(responseDict.result, '新增线索失败')
        
        #通过手机号快速搜索
        Log.LogOutput(level=LogLevel.INFO, message='------开始通过手机号快速搜索------')
        #快速搜索条件字典
        searchDict = copy.deepcopy(XianSuoGuanLiPara.clueFastSearchDict)
        searchDict['searchInfoVo.fastSearchKey'] = Global.XianSuoDftMobile
        #爆料搜索结果查询字典
        compareDict = copy.deepcopy(XianSuoGuanLiPara.clueSearchResultCheck)
        compareDict['mobile'] = Global.XianSuoDftMobile
        ret = XianSuoGuanLiIntf.check_baoliao_fast_search_result(compareDict,searchDict)
        self.assertTrue(ret, "搜索出不是本手机号的爆料")
        
        compareDict['mobile'] = newMobilePhone
        ret1 = XianSuoGuanLiIntf.check_baoliao_fast_search_result(compareDict,searchDict)
        self.assertFalse(ret1, "搜索出不是本手机号的爆料")
        
        #通过昵称快速搜索
        Log.LogOutput(level=LogLevel.INFO, message='------开始通过用户昵称快速搜索------')
        searchDict = copy.deepcopy(XianSuoGuanLiPara.clueFastSearchDict)
        searchDict['searchInfoVo.fastSearchKey'] = newNickName
        
        compareDict = copy.deepcopy(XianSuoGuanLiPara.clueSearchResultCheck)
        compareDict['nickName'] = newNickName
        ret = XianSuoGuanLiIntf.check_baoliao_fast_search_result(compareDict,searchDict)
        self.assertTrue(ret, "搜索出不是本昵称的爆料")
        
        compareDict['nickName'] = Global.XianSuoDftMobileNick
        ret1 = XianSuoGuanLiIntf.check_baoliao_fast_search_result(compareDict,searchDict)
        self.assertFalse(ret1, "搜索出不是本昵称的爆料")
        
        #通过公开和不公开快速搜索
        Log.LogOutput(level=LogLevel.INFO, message='------开始通过分享状态快速搜索------')
        #获取新用户的爆料id
        clueId = XianSuoGuanLiIntf.get_clue_id_by_description(newClueByNewUser['information']['contentText'])
        #将该爆料设置为不公开
        XianSuoGuanLiIntf.set_clue_show_state(clueId, ShowState.CLOSE)
        #搜索不公开的爆料
        searchDict = copy.deepcopy(XianSuoGuanLiPara.clueFastSearchDict)
        searchDict['searchInfoVo.information.showState'] = ShowState.CLOSE
        
        compareDict = copy.deepcopy(XianSuoGuanLiPara.clueSearchResultCheck)
        compareDict['contentText'] = newClueByNewUser['information']['contentText']
        ret = XianSuoGuanLiIntf.check_baoliao_fast_search_result(compareDict,searchDict)
        self.assertTrue(ret, "搜索出公开的爆料")
        
        compareDict['contentText'] = newClueByDftUser['information']['contentText']
        ret1 = XianSuoGuanLiIntf.check_baoliao_fast_search_result(compareDict,searchDict)
        self.assertFalse(ret1, "搜索出公开的爆料")
        
        #通过精彩推荐快速搜索
        Log.LogOutput(level=LogLevel.INFO, message='------开始通过精彩推荐快速搜索------')      
        #将新用户的爆料设置为精彩推荐
        XianSuoGuanLiIntf.set_clue_show_state(clueId, ShowState.HIGHLIGHT)
        #搜索精彩推荐
        searchDict = copy.deepcopy(XianSuoGuanLiPara.clueFastSearchDict)
        searchDict['searchInfoVo.information.showState'] = ShowState.HIGHLIGHT
        
        compareDict = copy.deepcopy(XianSuoGuanLiPara.clueSearchResultCheck)
        compareDict['contentText'] = newClueByNewUser['information']['contentText']
        ret = XianSuoGuanLiIntf.check_baoliao_fast_search_result(compareDict,searchDict)
        self.assertTrue(ret, "精彩推荐搜索异常")
        
        compareDict['contentText'] = newClueByDftUser['information']['contentText']
        ret1 = XianSuoGuanLiIntf.check_baoliao_fast_search_result(compareDict,searchDict)
        self.assertFalse(ret1, "精彩推荐搜索异常")
        
        #通过主题快速搜索
        Log.LogOutput(level=LogLevel.INFO, message='------开始通过主题快速搜索------')
        searchDict = copy.deepcopy(XianSuoGuanLiPara.clueFastSearchDict)
        searchDict['searchInfoVo.information.themeContentId'] = newClueByDftUser['information']['themeContentId']
        
        compareDict = copy.deepcopy(XianSuoGuanLiPara.clueSearchResultCheck)
        compareDict['mobile'] = Global.XianSuoDftMobile
        ret = XianSuoGuanLiIntf.check_baoliao_fast_search_result(compareDict,searchDict)
        self.assertTrue(ret, "搜索出不是本主题的爆料")
        
        compareDict['mobile'] = newMobilePhone
        ret1 = XianSuoGuanLiIntf.check_baoliao_fast_search_result(compareDict,searchDict)
        self.assertFalse(ret1, "搜索出不是本主题的爆料")      
        pass
    def testAdvanceSearch(self):
        '''高级搜索'''
        #默认账号添加一条线索
        newClueByDftUser = copy.deepcopy(XsBaoLiaoPara.XinZeng) 
        newClueByDftUser['information']['contentText'] = '事件描述%s' % CommonUtil.createRandomString()
        newClueByDftUser['information']['baiduX'] = '120.4989885463861'
        newClueByDftUser['information']['baiduY'] = '30.27759299562879'
        newClueByDftUser['information']['x'] = '120.488114380334'
        newClueByDftUser['information']['y'] = '30.27759299562879'          
        newClueByDftUser['information']['address'] = 'addres'+CommonUtil.createRandomString()
        responseDict = XsBaoLiaoIntf.addXianSuo(newClueByDftUser)
        self.assertTrue(responseDict.result, '新增线索失败')
        #使用新账号新增一条线索
        #添加一个手机账号，用于手机号快速搜索验证
        newMobilePhone = '13588806928'
        newNickName = 'nick_%s' % newMobilePhone
        XsGongZuoTaiIntf.initUser(mobile=newMobilePhone)
        #初始化新用户的时候会默认设置昵称，昵称格式为"nick_手机号"
        newClueByNewUser = copy.deepcopy(XsBaoLiaoPara.XinZeng) 
        newClueByNewUser['information']['contentText'] = '事件描述%s' % CommonUtil.createRandomString()
        newClueByNewUser['information']['baiduX'] = '120.4989885463861'
        newClueByNewUser['information']['baiduY'] = '30.27759299562879'
        newClueByNewUser['information']['x'] = '120.488114380334'
        newClueByNewUser['information']['y'] = '30.27759299562879'        
        newClueByNewUser['information']['address'] = 'addres'+CommonUtil.createRandomString()
        responseDict = XsBaoLiaoIntf.addXianSuo(newClueByNewUser,mobile=newMobilePhone)
        self.assertTrue(responseDict.result, '新增线索失败')
         
        #通过用户昵称高级搜索
        Log.LogOutput(level=LogLevel.INFO, message='------开始通过用户昵称高级搜索------')
        searchDict = copy.deepcopy(XianSuoGuanLiPara.clueAdvanceSearchDict)
        searchDict['searchInfoVo.information.nickName'] = newNickName
         
        compareDict = copy.deepcopy(XianSuoGuanLiPara.clueSearchResultCheck)
        compareDict['nickName'] = newNickName
        ret = XianSuoGuanLiIntf.check_baoliao_advance_search_result(compareDict,searchDict)
        self.assertTrue(ret, "未搜索出符合昵称的爆料")
         
        compareDict['nickName'] = Global.XianSuoDftMobileNick
        ret1 = XianSuoGuanLiIntf.check_baoliao_advance_search_result(compareDict,searchDict)
        self.assertFalse(ret1, "搜索出不是本昵称的爆料")
         
        #通过发生地点高级搜索
        Log.LogOutput(level=LogLevel.INFO, message='------开始通过发生地点高级搜索------')
        searchDict = copy.deepcopy(XianSuoGuanLiPara.clueAdvanceSearchDict)
        searchDict['searchInfoVo.information.address'] = newClueByDftUser['information']['address']
         
        compareDict = copy.deepcopy(XianSuoGuanLiPara.clueSearchResultCheck)
        compareDict['address'] = newClueByDftUser['information']['address']
        ret = XianSuoGuanLiIntf.check_baoliao_advance_search_result(compareDict,searchDict)
        self.assertTrue(ret, "搜索出不是本地址的爆料")
         
        compareDict['address'] = newClueByNewUser['information']['address']
        ret1 = XianSuoGuanLiIntf.check_baoliao_advance_search_result(compareDict,searchDict)
        self.assertFalse(ret1, "搜索出不是本地址的爆料")
         
        #通过事件描述高级搜索
        Log.LogOutput(level=LogLevel.INFO, message='------开始通过爆料描述高级搜索------')
        searchDict = copy.deepcopy(XianSuoGuanLiPara.clueAdvanceSearchDict)
        searchDict['searchInfoVo.information.contentText'] = newClueByNewUser['information']['contentText']
         
        compareDict = copy.deepcopy(XianSuoGuanLiPara.clueSearchResultCheck)
        compareDict['contentText'] = newClueByNewUser['information']['contentText']
        ret = XianSuoGuanLiIntf.check_baoliao_advance_search_result(compareDict,searchDict)
        self.assertTrue(ret, "搜索出不是本描述的爆料")
         
        compareDict['contentText'] = newClueByDftUser['information']['contentText']
        ret1 = XianSuoGuanLiIntf.check_baoliao_advance_search_result(compareDict,searchDict)
        self.assertFalse(ret1, "搜索出不是本描述的爆料")
         
        Log.LogOutput(level=LogLevel.INFO, message='------开始通过服务单号高级搜索------')
        #获取默认用户爆料的id
        defUserClueId = XianSuoGuanLiIntf.get_clue_id_by_description(newClueByDftUser['information']['contentText'])
        #将该爆料设置为不公开
        XianSuoGuanLiIntf.set_clue_show_state(defUserClueId, ShowState.CLOSE)
        #默认用户爆料转事件
        clueToIssueDict = copy.deepcopy(XianSuoGuanLiPara.clueToIssuePara)
        clueToIssueDict['information.id'] = defUserClueId
        clueToIssueDict['issue.subject'] = "%s转事件" % newClueByDftUser['information']['contentText']
        clueToIssueDict['issue.occurLocation'] = newClueByDftUser['information']['address']
        clueToIssueDict['issueRelatedPeopleTelephones'] = Global.XianSuoDftMobile
        clueToIssueDict['issue.issueContent'] = newClueByDftUser['information']['contentText']
        XianSuoGuanLiIntf.change_clue_to_issue(clueToIssueDict)
         
        #通过事件服务单号高级搜索
        issueSN = CommonIntf.getDbQueryResult(dbCommand="select t.serialnumber from ISSUES t where t.subject='%s'" % clueToIssueDict['issue.subject'])
        searchDict = copy.deepcopy(XianSuoGuanLiPara.clueAdvanceSearchDict)
        searchDict['searchInfoVo.information.serialNumber'] = issueSN
        compareDict = copy.deepcopy(XianSuoGuanLiPara.clueSearchResultCheck)
        compareDict['contentText'] = newClueByDftUser['information']['contentText']
        ret = XianSuoGuanLiIntf.check_baoliao_advance_search_result(compareDict,searchDict)
        self.assertTrue(ret, "搜索出不是本服务单号的爆料")
         
        compareDict['contentText'] = newClueByNewUser['information']['contentText']
        ret1 = XianSuoGuanLiIntf.check_baoliao_advance_search_result(compareDict,searchDict)
        self.assertFalse(ret1, "搜索出不是本服务单号的爆料")
         
        #通过是否官方回复高级搜索，默认用户创建的爆料已转事件，转事件的同时系统会自动官方回复，新用户创建的爆料未回复
        Log.LogOutput(level=LogLevel.INFO, message='------开始通过官方回复状态高级搜索------')
        searchDict = copy.deepcopy(XianSuoGuanLiPara.clueAdvanceSearchDict)
        searchDict['searchInfoVo.officialReplyState'] = OfficialState.REPLY
         
        compareDict = copy.deepcopy(XianSuoGuanLiPara.clueSearchResultCheck)
        compareDict['contentText'] = newClueByDftUser['information']['contentText']
        ret = XianSuoGuanLiIntf.check_baoliao_advance_search_result(compareDict,searchDict)
        self.assertTrue(ret, "未搜索到已官方回复的爆料")
         
        compareDict['contentText'] = newClueByNewUser['information']['contentText']
        ret1 = XianSuoGuanLiIntf.check_baoliao_advance_search_result(compareDict,searchDict)
        self.assertFalse(ret1, "搜索出未官方回复的爆料")
         
        #通过处理状态高级搜索
        Log.LogOutput(level=LogLevel.INFO, message='------开始通过处理状态高级搜索------')
        #新用户创建的线索官方回复，该爆料状态为结案
        newUserClueId = XianSuoGuanLiIntf.get_clue_id_by_description(newClueByNewUser['information']['contentText'])
        XianSuoGuanLiIntf.official_reply_for_clue(clueId=newUserClueId, officialReply="%s官方回复" % newClueByNewUser['information']['contentText'])
         
        #通过事件状态高级搜索
        searchDict = copy.deepcopy(XianSuoGuanLiPara.clueAdvanceSearchDict)
        searchDict['searchInfoVo.information.state'] = DealState.COMPLETE
         
        compareDict = copy.deepcopy(XianSuoGuanLiPara.clueSearchResultCheck)
        compareDict['contentText'] = newClueByNewUser['information']['contentText']
        ret = XianSuoGuanLiIntf.check_baoliao_advance_search_result(compareDict,searchDict)
        self.assertTrue(ret, "未搜索到结案状态的爆料")
         
        compareDict['contentText'] = newClueByDftUser['information']['contentText']
        ret1 = XianSuoGuanLiIntf.check_baoliao_advance_search_result(compareDict,searchDict)
        self.assertFalse(ret1, "搜索出不是结案状态的爆料")
         
        searchDict['searchInfoVo.information.state'] = DealState.ACCEPT
         
        compareDict = copy.deepcopy(XianSuoGuanLiPara.clueSearchResultCheck)
        compareDict['contentText'] = newClueByDftUser['information']['contentText']
        ret = XianSuoGuanLiIntf.check_baoliao_advance_search_result(compareDict,searchDict)
        self.assertTrue(ret, "未搜索到受理状态的爆料")
         
        compareDict['contentText'] = newClueByNewUser['information']['contentText']
        ret1 = XianSuoGuanLiIntf.check_baoliao_advance_search_result(compareDict,searchDict)
        self.assertFalse(ret1, "搜索出不是受理状态的爆料")
         
        #通过分享状态高级搜索，默认用户创建的爆料前文已经设置为不公开，新用户创建的爆料未公开
        Log.LogOutput(level=LogLevel.INFO, message='------开始通过分享状态高级搜索------')
        searchDict = copy.deepcopy(XianSuoGuanLiPara.clueAdvanceSearchDict)
        searchDict['searchInfoVo.information.showState'] = ShowState.CLOSE
         
        compareDict = copy.deepcopy(XianSuoGuanLiPara.clueSearchResultCheck)
        compareDict['contentText'] = newClueByDftUser['information']['contentText']
        ret = XianSuoGuanLiIntf.check_baoliao_advance_search_result(compareDict,searchDict)
        self.assertTrue(ret, "未搜索到不公开状态的爆料")
         
        compareDict['contentText'] = newClueByNewUser['information']['contentText']
        ret1 = XianSuoGuanLiIntf.check_baoliao_advance_search_result(compareDict,searchDict)
        self.assertFalse(ret1, "搜索出公开状态的爆料")
               
        pass      
        
    def testSuiBianShuoShuo(self):
        '''随便说说'''
        #先删除所有说说
        XianSuoGuanLiIntf.delete_all_shuoshuo()
        #判断是否有以下两个主题，如没有，则新增
        themeAddOne = copy.deepcopy(XiTongPeiZhiPara.themeAddDict)
        themeAddOne['themeContent.name'] = 'shuoshuoTestTheme1'
        themeAddOne['themeContent.description'] = 'shuoshuoTestDesc1'
        themeAddOne['themeRelation.infoType'] = 5
        
        themeAddTwo = copy.deepcopy(XiTongPeiZhiPara.themeAddDict)
        themeAddTwo['themeContent.name'] = 'shuoshuoTestTheme2'
        themeAddTwo['themeContent.description'] = 'shuoshuoTestDesc2'
        themeAddTwo['themeRelation.infoType'] = 5
        count0 = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select count(*) from THEMECONTENTS t where t.name='%s'" % themeAddOne['themeContent.name'])
        count1 = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select count(*) from THEMECONTENTS t where t.name='%s'" % themeAddTwo['themeContent.name'])
        if count0 == 0:
            XiTongPeiZhiIntf.add_theme(themeAddOne)
        if count1 == 0:
            XiTongPeiZhiIntf.add_theme(themeAddTwo)
        #新增第一条说说(涉及到说说列表内容可能有表情，开发做过特殊处理，列表返回会有编码问题，这里内容和title都写成英文)
        addShuoShuoOne = copy.deepcopy(ShuoShuoPara.addShuoShuoPara)
        addShuoShuoOne['casualTalk']['contentText'] = 'addOneShuoshuo'
        addShuoShuoOne['casualTalk']['title'] = 'addOneShuoshuo'
        addShuoShuoOne['casualTalk']['themeContentId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from THEMECONTENTS t where t.name='%s'" % themeAddOne['themeContent.name'])
        ShuoShuoIntf.add_shuoshuo(addShuoShuoOne)
        
        #新增另一条说说，使用非默认账号
        #添加一个手机账号，用于手机号快速搜索验证
        newMobilePhone = '13588806928'
        XsGongZuoTaiIntf.initUser(mobile=newMobilePhone)
        
        #新增第二条说说
        addShuoShuoTwo = copy.deepcopy(ShuoShuoPara.addShuoShuoPara)
        addShuoShuoTwo['casualTalk']['contentText'] = 'addSecondShuoshuo'
        addShuoShuoTwo['casualTalk']['title'] = 'addSecondShuoshuo'
        addShuoShuoTwo['casualTalk']['themeContentId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from THEMECONTENTS t where t.name='%s'" % themeAddTwo['themeContent.name'])
        ShuoShuoIntf.add_shuoshuo(addShuoShuoTwo, mobile = newMobilePhone)
        
        #通过说说内容搜索
        Log.LogOutput(level=LogLevel.INFO, message='------开始通过说说内容搜索------')
        searchDict = copy.deepcopy(XianSuoGuanLiPara.shuoshuoSearchDict)
        searchDict['searchCasualTalkVo.contentText'] =addShuoShuoOne['casualTalk']['contentText']
        
        compareDict = copy.deepcopy(XianSuoGuanLiPara.shuoshuoSearchResultCheck)
        compareDict['mobile'] = Global.XianSuoDftMobile
        ret = XianSuoGuanLiIntf.check_shuoshuo_search_result(compareDict,searchDict)
        self.assertTrue(ret, "搜索出非指定内容的说说")
        
        compareDict['mobile'] = newMobilePhone
        ret1 = XianSuoGuanLiIntf.check_shuoshuo_search_result(compareDict,searchDict)
        self.assertFalse(ret1, "搜索出非指定内容的说说")
        
        #通过主题搜索
        Log.LogOutput(level=LogLevel.INFO, message='------开始通过说说主题搜索------')
        searchDict = copy.deepcopy(XianSuoGuanLiPara.shuoshuoSearchDict)
        searchDict['searchCasualTalkVo.themeContentId'] =addShuoShuoTwo['casualTalk']['themeContentId']
        
        compareDict = copy.deepcopy(XianSuoGuanLiPara.shuoshuoSearchResultCheck)
        compareDict['mobile'] = Global.XianSuoDftMobile
        ret = XianSuoGuanLiIntf.check_shuoshuo_search_result(compareDict,searchDict)
        self.assertFalse(ret, "搜索出非指定主题的说说")
        
        compareDict['mobile'] = newMobilePhone
        ret1 = XianSuoGuanLiIntf.check_shuoshuo_search_result(compareDict,searchDict)
        self.assertTrue(ret1, "搜索出非指定主题的说说")
        
        #用默认手机号认证线索用户
        SystemMgrIntf.clueUserCertified()
        #通过我的信息搜索
        Log.LogOutput(level=LogLevel.INFO, message='------开始通过我的信息搜索------')
        searchDict = copy.deepcopy(XianSuoGuanLiPara.shuoshuoSearchDict)
        searchDict['searchCasualTalkVo.mobile'] =Global.XianSuoDftMobile
        
        compareDict = copy.deepcopy(XianSuoGuanLiPara.shuoshuoSearchResultCheck)
        compareDict['mobile'] = Global.XianSuoDftMobile
        ret = XianSuoGuanLiIntf.check_shuoshuo_search_result(compareDict,searchDict)
        self.assertTrue(ret, "搜索出非我的信息说说")
        
        compareDict['mobile'] = newMobilePhone
        ret1 = XianSuoGuanLiIntf.check_shuoshuo_search_result(compareDict,searchDict)
        self.assertFalse(ret1, "搜索出非我的信息说说")
        
        #通过后台新增说说
        shuoshuoAddDict = copy.deepcopy(XianSuoGuanLiPara.addShuoShuoByXianSuoGuanLiPara)
        shuoshuoAddDict['casualTalkVo.casualTalk.contentText'] = 'HouTaiXinZengShuoShuo'
        XianSuoGuanLiIntf.add_shuoshuo_by_xiansuoguanli(shuoshuoAddDict)
        
        #列表中检查说说
        searchDict = copy.deepcopy(XianSuoGuanLiPara.shuoshuoSearchDict)
        searchDict['searchCasualTalkVo.contentText'] = shuoshuoAddDict['casualTalkVo.casualTalk.contentText']
        
        compareDict = copy.deepcopy(XianSuoGuanLiPara.shuoshuoSearchResultCheck)
        compareDict['contentText'] = shuoshuoAddDict['casualTalkVo.casualTalk.contentText']
        ret = XianSuoGuanLiIntf.check_shuoshuo_search_result(compareDict,searchDict)
        self.assertTrue(ret, "说说列表查找说说失败")
        
        #更新说说
        shuoshuoId = XianSuoGuanLiIntf.get_shuoshuo_id_by_content(shuoshuoAddDict['casualTalkVo.casualTalk.contentText'])
        shuoshuoUpdateDict = copy.deepcopy(XianSuoGuanLiPara.updateShuoShuoByXianSuoGuanLiPara)
        shuoshuoUpdateDict['casualTalk.id'] = shuoshuoId
        shuoshuoUpdateDict['casualTalk.contentText'] = 'HouTaiXinZengShuoShuoUpdate'
        XianSuoGuanLiIntf.update_shuoshuo_by_xiansuoguanli(shuoshuoUpdateDict)

        #列表中检查说说
        searchDict = copy.deepcopy(XianSuoGuanLiPara.shuoshuoSearchDict)
        searchDict['searchCasualTalkVo.contentText'] = shuoshuoUpdateDict['casualTalk.contentText']
        
        compareDict = copy.deepcopy(XianSuoGuanLiPara.shuoshuoSearchResultCheck)
        compareDict['contentText'] = shuoshuoUpdateDict['casualTalk.contentText']
        ret = XianSuoGuanLiIntf.check_shuoshuo_search_result(compareDict,searchDict)
        self.assertTrue(ret, "说说列表查找说说失败")
        
        #删除更新后的说说
        delShuoShuoDict = copy.deepcopy(XianSuoGuanLiPara.shuoshuoDelDict)
        delShuoShuoDict['delInfoRecord.informationId'] = shuoshuoId
        delShuoShuoDict['delInfoRecord.mobile'] = Global.XianSuoDftMobile        
        XianSuoGuanLiIntf.delete_one_shuoshuo(delShuoShuoDict)
        
        #列表中检查说说
        searchDict = copy.deepcopy(XianSuoGuanLiPara.shuoshuoSearchDict)
        searchDict['searchCasualTalkVo.contentText'] = shuoshuoUpdateDict['casualTalk.contentText']
        
        compareDict = copy.deepcopy(XianSuoGuanLiPara.shuoshuoSearchResultCheck)
        compareDict['contentText'] = shuoshuoUpdateDict['casualTalk.contentText']
        ret = XianSuoGuanLiIntf.check_shuoshuo_search_result(compareDict,searchDict)
        self.assertFalse(ret, "列表中找到已经删除的说说")
        pass
    def testPingAnXuanChuan(self):
        '''平安宣传'''
        #删除所有平安宣传
        XianSuoGuanLiIntf.delete_all_pinganxuanchuan()
        #新增两个平安宣传
        addPingAnXuanChuanOne = copy.deepcopy(XianSuoGuanLiPara.addPingAnXuanChuanDict)
        addPingAnXuanChuanOne['informationVo.information.title'] = "平安宣传标题One"
        addPingAnXuanChuanOne['informationVo.information.contentText'] = "平安宣传正文One"
        ret = XianSuoGuanLiIntf.add_pinganxuanchuan(addPingAnXuanChuanOne)
        self.assertTrue(ret, "平安宣传新增失败")
        
        addPingAnXuanChuanTwo = copy.deepcopy(XianSuoGuanLiPara.addPingAnXuanChuanDict)
        addPingAnXuanChuanTwo['informationVo.information.title'] = "平安宣传标题Two"
        addPingAnXuanChuanTwo['informationVo.information.contentText'] = "平安宣传正文Two"
        ret = XianSuoGuanLiIntf.add_pinganxuanchuan(addPingAnXuanChuanTwo)
        self.assertTrue(ret, "平安宣传新增失败")
        
        #更新第一条平安宣传的状态为公开，默认为不公开
        #获取第一条平安宣传的id
        id = XianSuoGuanLiIntf.get_pinganxuanchuan_id_by_title(addPingAnXuanChuanOne['informationVo.information.title'])
        updateStateDict = copy.deepcopy(XianSuoGuanLiPara.updatePingAnXuanChuanStateDict)
        updateStateDict['ids'] = id
        updateStateDict['showState'] = ShowState.OPEN
        XianSuoGuanLiIntf.update_pinganxuanchuan_state(updateStateDict)
        
        #通过标题搜索
        Log.LogOutput(level=LogLevel.INFO, message='------开始通过平安宣传标题搜索------')
        searchDict = copy.deepcopy(XianSuoGuanLiPara.pingAnXuanChuanSearchDict)
        searchDict['searchInfoVo.information.title'] = addPingAnXuanChuanOne['informationVo.information.title']
        
        compareDict = copy.deepcopy(XianSuoGuanLiPara.pingAnXuanChuanSearchResultCheck)
        compareDict['title'] = addPingAnXuanChuanOne['informationVo.information.title']
        ret = XianSuoGuanLiIntf.check_pinganxuanchuan_search_result(compareDict,searchDict)
        self.assertTrue(ret, "搜索出非指定标题的平安宣传")
        
        compareDict['title'] = addPingAnXuanChuanTwo['informationVo.information.title']
        ret1 = XianSuoGuanLiIntf.check_pinganxuanchuan_search_result(compareDict,searchDict)
        self.assertFalse(ret1, "搜索出非指定标题的平安宣传")
        
        #通过状态搜索
        Log.LogOutput(level=LogLevel.INFO, message='------开始通过平安宣传状态搜索------')
        searchDict = copy.deepcopy(XianSuoGuanLiPara.pingAnXuanChuanSearchDict)
        searchDict['searchInfoVo.information.showState'] = ShowState.CLOSE
        
        compareDict = copy.deepcopy(XianSuoGuanLiPara.pingAnXuanChuanSearchResultCheck)
        compareDict['title'] = addPingAnXuanChuanOne['informationVo.information.title']
        ret = XianSuoGuanLiIntf.check_pinganxuanchuan_search_result(compareDict,searchDict)
        self.assertFalse(ret, "搜索出非指定标题的平安宣传")
        
        compareDict['title'] = addPingAnXuanChuanTwo['informationVo.information.title']
        ret1 = XianSuoGuanLiIntf.check_pinganxuanchuan_search_result(compareDict,searchDict)
        self.assertTrue(ret1, "搜索出非指定标题的平安宣传")
        
        #修改第二条平安宣传标题和内容
        id = XianSuoGuanLiIntf.get_pinganxuanchuan_id_by_title(addPingAnXuanChuanTwo['informationVo.information.title'])
        modifyPingAnXuanChuan = copy.deepcopy(XianSuoGuanLiPara.modifyPingAnXuanChuanDict)
        modifyPingAnXuanChuan['informationVo.information.title'] = "平安宣传标题Update"
        modifyPingAnXuanChuan['informationVo.information.contentText'] = "平安宣传内容Update"
        modifyPingAnXuanChuan['informationVo.information.id'] = id
        ret = XianSuoGuanLiIntf.modify_pinganxuanchuan(modifyPingAnXuanChuan)
        self.assertTrue(ret1, "修改平安宣传失败")
        
        #修改后标题和内容查看
        Log.LogOutput(level=LogLevel.INFO, message='------平安宣传修改后验证------')
        searchDict = copy.deepcopy(XianSuoGuanLiPara.pingAnXuanChuanSearchDict)
        
        compareDict = copy.deepcopy(XianSuoGuanLiPara.pingAnXuanChuanSearchResultCheck)
        compareDict['title'] = modifyPingAnXuanChuan['informationVo.information.title']
        compareDict['contentText'] = modifyPingAnXuanChuan['informationVo.information.contentText']
        ret = XianSuoGuanLiIntf.check_pinganxuanchuan_search_result(compareDict,searchDict)
        self.assertTrue(ret, "平安宣传修改后验证失败")
        
        compareDict['title'] = addPingAnXuanChuanTwo['informationVo.information.title']
        compareDict['contentText'] = addPingAnXuanChuanTwo['informationVo.information.contentText']
        ret1 = XianSuoGuanLiIntf.check_pinganxuanchuan_search_result(compareDict,searchDict)
        self.assertFalse(ret1, "平安宣传修改后验证失败")
        
        #删除更新后的平安宣传
        XianSuoGuanLiIntf.delete_one_pinganxuanchuan(id)
        
        #删除后校验
        compareDict = copy.deepcopy(XianSuoGuanLiPara.pingAnXuanChuanSearchResultCheck)
        compareDict['title'] = modifyPingAnXuanChuan['informationVo.information.title']
        compareDict['contentText'] = modifyPingAnXuanChuan['informationVo.information.contentText']
        ret = XianSuoGuanLiIntf.check_pinganxuanchuan_search_result(compareDict,searchDict)
        self.assertFalse(ret, "删除后仍检查到平安宣传")
        
        pass
    def tearDown(self):
        pass
if __name__ == "__main__":
    suite = unittest.TestSuite()
#     suite.addTest(XianSuoGuanLi("testFastSearch"))
    suite.addTest(XianSuoGuanLi("testAdvanceSearch"))  
#     suite.addTest(XianSuoGuanLi("testSuiBianShuoShuo"))   
#     suite.addTest(XianSuoGuanLi("testPingAnXuanChuan"))   
    results = unittest.TextTestRunner().run(suite)
    pass