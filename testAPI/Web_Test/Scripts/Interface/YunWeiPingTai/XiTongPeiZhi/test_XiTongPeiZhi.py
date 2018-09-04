# -*- coding:UTF-8 -*-
'''
Created on 2016-4-6

@author: N-133
'''
from __future__ import unicode_literals
from COMMON import Log, CommonUtil, Time
from COMMON.CommonUtil import createRandomString
from CONFIG import InitDefaultPara, Global
from CONFIG.InitDefaultPara import orgInit, userInit, clueOrgInit
from Interface.PingAnJianShe.ShiJianChuLi import ShiJianChuLiPara, \
    ShiJianChuLiIntf
from Interface.XianSuoApp.BaoLiao import XsBaoLiaoPara, XsBaoLiaoIntf
from Interface.XianSuoApp.BaoLiao.XsBaoLiaoIntf import addXianSuo
from Interface.XianSuoApp.GongGaoLan import XsGongGaoLanPara, XsGongGaoLanIntf
from Interface.XianSuoApp.GongZuoTai import XsGongZuoTaiIntf, XsGongZuoTaiPara
from Interface.XianSuoApp.ShouYe import XsShouYeIntf, XsShouYePara
from Interface.XianSuoApp.ShuoShuo import ShuoShuoPara, ShuoShuoIntf
from Interface.XianSuoApp.WoDeXinXi import XsMyInformationIntf
from Interface.XianSuoApp.XinXiGuangChang import XsInformationSquarePara, \
    XsInformationSquareIntf
from Interface.XianSuoApp.XinXiGuangChang.XsInformationSquareIntf import \
    clueToIssue
from Interface.XianSuoApp.XinXiGuangChang.XsInformationSquarePara import \
    ClueShowState
from Interface.YunWeiPingTai.XiTongPeiZhi import XiTongPeiZhiIntf, \
    XiTongPeiZhiPara
from Interface.YunWeiPingTai.XiTongPeiZhi.XiTongPeiZhiPara import ConfigType, \
    ConfigValue, NoticeType, HomePageShow, CloseState, ConvenienceState, \
    OrgOpenState, ThemeState, InfoType, IsHotState, JumpType, FilterType
from Interface.YunWeiPingTai.XinXiGuanLi import XinXiGuanLiPara, XinXiGuanLiIntf
from Interface.YunWeiPingTai.XinXiGuanLi.XinXiGuanLiPara import ShowState, \
    ReportState
from Interface.YunWeiPingTai.YunWeiCommon import YunWeiCommonIntf
from Interface.YunWeiPingTai.yunWeiPingTaiHttpCommon import xiansuoyunwei_login
import copy
import json
import unittest



class XiTongPeiZhi(unittest.TestCase):

    def setUp(self):
#         SystemMgrIntf.initEnv()''
        XiTongPeiZhiIntf.deleteXiTongPeiZhi()
        #删除所有系统配置
        XiTongPeiZhiIntf.delete_all_personal_config()
        
        pass		
    def testSystemConfig_01(self):
        """新增/修改/删除关键字信息-489"""
        #清空所有关键字
        XiTongPeiZhiIntf.delete_all_keyword_setting()
        #新增关键字        
        addKeywordSettingDict = copy.deepcopy(XiTongPeiZhiPara.addKeywordSettingPara) 
        addKeywordSettingDict['keyWordSetting.filterType'] =FilterType.INFO #表示信息
        addKeywordSettingDict['keyWordSetting.keyWords'] = '曼联'
        ret = XiTongPeiZhiIntf.add_keyword_setting(addKeywordSettingDict)
        self.assertTrue(ret, '新增关键字失败') 
        #新增各一条带关键字信息的爆料和说说，后台查看是否有举报信息
        addClueDict = copy.deepcopy(XsBaoLiaoPara.xinZeng2) 
        addClueDict['information']['contentText'] = '%s%s' % (addKeywordSettingDict['keyWordSetting.keyWords'],CommonUtil.createRandomString())
        responseDict = XsBaoLiaoIntf.addXianSuo(addClueDict)
        self.assertTrue(responseDict.result, '新增线索失败')
        
        
        addShuoShuoOne = copy.deepcopy(ShuoShuoPara.addShuoShuoPara)
        addShuoShuoOne['casualTalk']['contentText'] = '说说内容%s%s' % (addKeywordSettingDict['keyWordSetting.keyWords'],CommonUtil.createRandomString())
        addShuoShuoOne['casualTalk']['title'] = '说说内容%s' % CommonUtil.createRandomString()
        ret = ShuoShuoIntf.add_shuoshuo(addShuoShuoOne)
        
        #后台查看是否有两条举报信息
        getInfoReportDict = copy.deepcopy(XinXiGuanLiPara.getInformationReportPara)
        getInfoReportDict['informationReport.infoType'] = InfoType.BAOLIAO
        getInfoReportDict['informationReport.state'] = ReportState.UNHANDLE #表示未处理
         
        checkInfoReportDict = copy.deepcopy(XinXiGuanLiPara.checkInformationReportPara)
        checkInfoReportDict['contentText'] = addClueDict['information']['contentText']
        checkInfoReportDict['address'] = addClueDict['information']['address']
        
        Time.wait(3)
        ret = XinXiGuanLiIntf.check_information_report_in_list(getInfoReportDict, checkInfoReportDict)
        self.assertTrue(ret, '在爆料待处理页面未检查到自动爆料举报信息')
        
        getInfoReportDict = copy.deepcopy(XinXiGuanLiPara.getInformationReportPara)
        getInfoReportDict['informationReport.infoType'] = InfoType.SHUOSHUO
        getInfoReportDict['informationReport.state'] = ReportState.UNHANDLE #表示未处理
         
        checkInfoReportDict = copy.deepcopy(XinXiGuanLiPara.checkInformationReportPara)
        checkInfoReportDict['contentText'] = addShuoShuoOne['casualTalk']['contentText']
        checkInfoReportDict['address'] = None
         
        ret = XinXiGuanLiIntf.check_information_report_in_list(getInfoReportDict, checkInfoReportDict)
        self.assertTrue(ret, '在说说待处理页面未检查到自动说说举报信息')
        
        #对爆料进行评论，评论中带上关键字
        clueId = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from INFORMATIONS t where t.contenttext='%s'"%addClueDict['information']['contentText'])
        addCommentDict = copy.deepcopy(XsBaoLiaoPara.addCommentForCluePara)
        addCommentDict['informationId'] = clueId
        addCommentDict['contentText'] = "红魔%s" % addKeywordSettingDict['keyWordSetting.keyWords']
        addCommentDict['commentUserId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from USERS t where t.mobile='%s'" % Global.XianSuoDftMobile)
        ret = XsBaoLiaoIntf.add_comment_for_clue(addCommentDict)
        
        #因为评论中带有关键字，因此关键字会被屏蔽，返回用**代替
        checkCommentDict = copy.deepcopy(XsBaoLiaoPara.checkCommentInCluePara)
#         checkCommentDict['contentText'] = "红魔**"
        checkCommentDict['contentText'] = addCommentDict['contentText']
        ret = XsBaoLiaoIntf.check_comment_in_clue(clueId, checkCommentDict)
        self.assertTrue(ret, '检查爆料评论信息中带上关键字用**替代失败')
        
        #说说评论带关键字，应该会被屏蔽，返回**代替
        shuoshuoId = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from CASUALTALKS t where t.contenttext='%s'" % addShuoShuoOne['casualTalk']['contentText'])
        addCommentDict = copy.deepcopy(ShuoShuoPara.addCommentForShuoShuoPara)
        addCommentDict['informationId'] = shuoshuoId
        addCommentDict['contentText'] = "红魔%s" % addKeywordSettingDict['keyWordSetting.keyWords']
        addCommentDict['commentUserId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from USERS t where t.mobile='%s'" % Global.XianSuoDftMobile)
        ret = ShuoShuoIntf.add_comment_for_shuoshuo(addCommentDict)
        
        #因为评论中带有关键字，因此关键字会被屏蔽，返回用**代替，现在已经不用**代替了
        checkCommentDict = copy.deepcopy(ShuoShuoPara.checkCommentInShuoShuoPara)
        checkCommentDict['contentText'] = addCommentDict['contentText']#"红魔**"
        
        ret = ShuoShuoIntf.check_comment_in_shuoshuo(shuoshuoId, checkCommentDict)
        self.assertTrue(ret, '检查说说评论信息中带上关键字用**替代失败')
        
        #修改关键字配置，将"曼联"改为"联"
        keywordSettingId= XiTongPeiZhiIntf.get_keyword_setting_id_by_content(addKeywordSettingDict['keyWordSetting.keyWords'])
        updateKeywordSettingDict = copy.deepcopy(XiTongPeiZhiPara.updateKeywordSettingPara)
        updateKeywordSettingDict['keyWordSetting.id'] = keywordSettingId
        updateKeywordSettingDict['keyWordSetting.keyWords'] = "联"
        ret = XiTongPeiZhiIntf.update_keyword_setting(updateKeywordSettingDict)
        self.assertTrue(ret, '修改关键字配置失败')
        
        #关键字修改为“联”后，爆料评论信息会显示成"红魔曼**"，新加的评论信息才会生效
        addCommentDict2 = copy.deepcopy(XsBaoLiaoPara.addCommentForCluePara)
        addCommentDict2['informationId'] = clueId
        addCommentDict2['contentText'] = "红魔曼%s" % updateKeywordSettingDict['keyWordSetting.keyWords']
        addCommentDict2['commentUserId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from USERS t where t.mobile='%s'" % Global.XianSuoDftMobile)
        ret = XsBaoLiaoIntf.add_comment_for_clue(addCommentDict2)
        
        checkCommentDict2 = copy.deepcopy(XsBaoLiaoPara.checkCommentInCluePara)
        checkCommentDict2['contentText'] = addCommentDict2['contentText'] #"红魔曼**"        
        ret = XsBaoLiaoIntf.check_comment_in_clue(clueId, checkCommentDict2)
        self.assertTrue(ret, '检查爆料评论信息中带上关键字用**替代失败')
        
        #关键字修改为“联”后，说说评论信息会显示成"红魔曼*"，新加的评论信息才会生效
        addCommentDict2 = copy.deepcopy(ShuoShuoPara.addCommentForShuoShuoPara)
        addCommentDict2['informationId'] = shuoshuoId
        addCommentDict2['contentText'] = "红魔曼%s" % updateKeywordSettingDict['keyWordSetting.keyWords']
        addCommentDict2['commentUserId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from USERS t where t.mobile='%s'" % Global.XianSuoDftMobile)
        ret = ShuoShuoIntf.add_comment_for_shuoshuo(addCommentDict2)
                
        checkCommentDict2 = copy.deepcopy(ShuoShuoPara.checkCommentInShuoShuoPara)
        checkCommentDict2['contentText'] = addCommentDict2['contentText'] #"红魔曼**"      
        ret = ShuoShuoIntf.check_comment_in_shuoshuo(shuoshuoId, checkCommentDict2)
        self.assertTrue(ret, '检查说说评论信息中带上关键字用**替代失败')
        
        #删除关键字配置
        XiTongPeiZhiIntf.delete_all_keyword_setting()
        
        #再次检查评论信息是否恢复正常，新增的评论才会生效
        addCommentDict3 = copy.deepcopy(XsBaoLiaoPara.addCommentForCluePara)
        addCommentDict3['informationId'] = clueId
        addCommentDict3['contentText'] = "红魔%s" % addKeywordSettingDict['keyWordSetting.keyWords']
        addCommentDict3['commentUserId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from USERS t where t.mobile='%s'" % Global.XianSuoDftMobile)
        ret = XsBaoLiaoIntf.add_comment_for_clue(addCommentDict3)
                
        checkCommentDict3 = copy.deepcopy(XsBaoLiaoPara.checkCommentInCluePara)
        checkCommentDict3['contentText'] = addCommentDict3['contentText']        
        ret = XsBaoLiaoIntf.check_comment_in_clue(clueId, checkCommentDict3)
        self.assertTrue(ret, '检查爆料评论信息中删除关键字配置后未回复正常')

        addCommentDict3 = copy.deepcopy(ShuoShuoPara.addCommentForShuoShuoPara)
        addCommentDict3['informationId'] = shuoshuoId
        addCommentDict3['contentText'] = "红魔%s" % addKeywordSettingDict['keyWordSetting.keyWords']
        addCommentDict3['commentUserId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from USERS t where t.mobile='%s'" % Global.XianSuoDftMobile)
        ret = ShuoShuoIntf.add_comment_for_shuoshuo(addCommentDict3)
                
        checkCommentDict3 = copy.deepcopy(ShuoShuoPara.checkCommentInShuoShuoPara)
        checkCommentDict3['contentText'] = addCommentDict3['contentText']      
        ret = ShuoShuoIntf.check_comment_in_shuoshuo(shuoshuoId, checkCommentDict3)
        self.assertTrue(ret, '检查说说评论信息中删除关键字配置后未回复正常')
        
        
        #新增昵称关键字配置
        addKeywordSettingDict = copy.deepcopy(XiTongPeiZhiPara.addKeywordSettingPara) 
        addKeywordSettingDict['keyWordSetting.filterType'] =FilterType.NICK #表示信息
        addKeywordSettingDict['keyWordSetting.keyWords'] = 'forbid'
        ret = XiTongPeiZhiIntf.add_keyword_setting(addKeywordSettingDict)
        self.assertTrue(ret, '新增昵称关键字失败') 
        
        #尝试将默认手机的昵称改成‘forbid’
        updateNickDict = copy.deepcopy(XsGongZuoTaiPara.userUpdatePara)
        updateNickDict['id']=YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from USERS t where t.mobile='%s'" % Global.XianSuoDftMobile)
        updateNickDict['nickName']= addKeywordSettingDict['keyWordSetting.keyWords']
        response = XsMyInformationIntf.updateUserInfo(updateNickDict)
        self.assertRegexpMatches(response.text, '昵称含不当信息', '修改包含关键字信息的昵称不报错')
        pass

    def testSystemConfig_02(self):
        """运维管理平台-系统配置-爆料统计开关-759"""
        #新增后台爆料统计开关配置，默认为关闭状态
        addPara=copy.deepcopy(XiTongPeiZhiPara.addPersonalConfigPara)
        addPara['personalizedConfiguration.configurationType']=ConfigType.BAOLIAOTONGJI
        addPara['personalizedConfiguration.configurationValue']=ConfigValue.CLOSE
        addPara['personalizedConfiguration.departmentNo']=InitDefaultPara.clueOrgInit['DftQuOrgDepNo']
        result=XiTongPeiZhiIntf.add_personal_config2(addPersonalConfigPara=addPara)
        resDict=json.loads(result.text)
        #列表检查参数
        checkPara=copy.deepcopy(XiTongPeiZhiPara.personalConfigListCheckPara)
        checkPara['id']=resDict['personalizedConfiguration']['id']
        checkPara['configurationType']=addPara['personalizedConfiguration.configurationType']
        checkPara['configurationValue']=addPara['personalizedConfiguration.configurationValue']
        #列表参数
        listPara=copy.deepcopy(XiTongPeiZhiPara.personalConfigListPara)
        res=XiTongPeiZhiIntf.check_personal_config_list(listPara,checkPara)
        self.assertTrue(res, '检查列表系统配置出错')
        #新增一条线索，并办结
        clueAddPara=copy.deepcopy(XsBaoLiaoPara.xinZeng2)
        addXianSuo(clueAddPara)
        listPara1={
                'tqmobile':'true',
                'page':'1',
                'rows':'100'
                  }
        lsr=XsBaoLiaoIntf.viewSchedule(para=listPara1)
#         print lsr.text
        lsrDict=json.loads(lsr.text)
        para1={
               'tqmobile':'true',
               'userId':lsrDict['response']['module']['rows'][0]['information']['publishUserId']
               }
        #后台将该线索公开
#         showStatePara={
#                        'ids':lsrDict['response']['module']['rows'][0]['information']['id'],
#                        'showState':1
#                        }
#         setClueShowState(para=showStatePara)
        #转事件,街道层级
        addIssuePara=copy.deepcopy(XsInformationSquarePara.culeToIssuePara)
        addIssuePara['information.id']=lsrDict['response']['module']['rows'][0]['information']['id']
        addIssuePara['information.nickName']=lsrDict['response']['module']['rows'][0]['information']['nickName']
        addIssuePara['issue.occurLocation']=lsrDict['response']['module']['rows'][0]['information']['address']
        addIssuePara['issue.issueContent']=lsrDict['response']['module']['rows'][0]['information']['contentText']
        isRes=clueToIssue(para=addIssuePara)
        isResDict=json.loads(isRes.text) 
        #事件办结
        issuePara=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)
        issuePara['operation.dealOrg.id']=orgInit['DftJieDaoOrgId']
        issuePara['operation.issue.id']=isResDict['issueId']
        issuePara['keyId']=isResDict['issueStepId']    
        issuePara['operation.dealUserName']=userInit['DftJieDaoUserXM']
        issuePara['operation.mobile']=userInit['DftJieDaoUserSJ']
        issuePara['operation.content']='结案'       
        issuePara['dealCode']='31'
        result=ShiJianChuLiIntf.dealIssue(issueDict=issuePara)
        self.assertTrue(result.result, '办结失败')
        Log.LogOutput( message='事件办结成功')
        
        #手机端获取统计,只有brokeStatisticsSwitc跟后台配置相关，其他数据是否显示有客户端页面决定
        para={
              'departmentNo':InitDefaultPara.clueOrgInit['DftQuOrgDepNo'],
              'tqmobile':'true'
              }
        checkmPara=copy.deepcopy(XsGongZuoTaiPara.checkBrokeStaticCountPara)
        checkmPara['brokeStatisticsSwitc']=addPara['personalizedConfiguration.configurationValue']
        checkmPara['countyWeekComplete']=1
        checkmPara['provinceWeekComplete']=1
        checkmPara['todayAdd']=1
        res=XsGongZuoTaiIntf.check_broke_static_count(para, checkmPara)
        self.assertTrue(res, '手机端获取爆料统计失败')
        #修改爆料统计开关
        updPara=copy.deepcopy(XiTongPeiZhiPara.updPersonalConfigListPara)
        updPara['personalizedConfiguration.configurationValue']=ConfigValue.OPEN
        updPara['personalizedConfiguration.id']=resDict['personalizedConfiguration']['id']
        updPara['personalizedConfiguration.configurationType']=addPara['personalizedConfiguration.configurationType']
        res=XiTongPeiZhiIntf.upd_personal_config(updPara)
        self.assertTrue(res.result, '修改失败')
        #检查PC端列表
        checkPara['configurationValue']=updPara['personalizedConfiguration.configurationValue']
        res=XiTongPeiZhiIntf.check_personal_config_list(listPara,checkPara)
        self.assertTrue(res, '检查列表系统配置出错')
        #检查手机端数据
        checkmPara['brokeStatisticsSwitc']=updPara['personalizedConfiguration.configurationValue']
        res=XsGongZuoTaiIntf.check_broke_static_count(para, checkmPara)
        self.assertTrue(res, '手机端获取爆料统计失败')
        pass
    
    def testSystemConfig_03(self):
        """运维管理平台-系统配置-爆料统计开关-471"""
        #新增后台办理意见是否展现开关配置，默认为关闭状态
        addPara=copy.deepcopy(XiTongPeiZhiPara.addPersonalConfigPara)
        addPara['personalizedConfiguration.configurationType']=ConfigType.BANLIYIJIAN
        addPara['personalizedConfiguration.configurationValue']=ConfigValue.CLOSE
        addPara['personalizedConfiguration.departmentNo']=InitDefaultPara.clueOrgInit['DftQuOrgDepNo']
        result=XiTongPeiZhiIntf.add_personal_config2(addPersonalConfigPara=addPara)
        resDict=json.loads(result.text)
        clueAddPara=copy.deepcopy(XsBaoLiaoPara.xinZeng2)
        addXianSuo(clueAddPara)
        listPara1={
                'tqmobile':'true',
                'page':'1',
                'rows':'100'
                  }
        lsr=XsBaoLiaoIntf.viewSchedule(para=listPara1)
#         print lsr.text
        lsrDict=json.loads(lsr.text)
        informationId=lsrDict['response']['module']['rows'][0]['information']['id']
        para1={
               'tqmobile':'true',
               'userId':lsrDict['response']['module']['rows'][0]['information']['publishUserId']
               }
        #后台将该线索公开
#         showStatePara={
#                        'ids':lsrDict['response']['module']['rows'][0]['information']['id'],
#                        'showState':1
#                        }
#         setClueShowState(para=showStatePara)
        #转事件,街道层级
        addIssuePara=copy.deepcopy(XsInformationSquarePara.culeToIssuePara)
        addIssuePara['information.id']=lsrDict['response']['module']['rows'][0]['information']['id']
        addIssuePara['information.nickName']=lsrDict['response']['module']['rows'][0]['information']['nickName']
        addIssuePara['issue.occurLocation']=lsrDict['response']['module']['rows'][0]['information']['address']
        addIssuePara['issue.issueContent']=lsrDict['response']['module']['rows'][0]['information']['contentText']
        isRes=clueToIssue(para=addIssuePara)
        isResDict=json.loads(isRes.text) 
        #事件办结
        issuePara=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)
        issuePara['operation.dealOrg.id']=orgInit['DftJieDaoOrgId']
        issuePara['operation.issue.id']=isResDict['issueId']
        issuePara['keyId']=isResDict['issueStepId']    
        issuePara['operation.dealUserName']=userInit['DftJieDaoUserXM']
        issuePara['operation.mobile']=userInit['DftJieDaoUserSJ']
        issuePara['operation.content']='结案'       
        issuePara['dealCode']='31'
        result=ShiJianChuLiIntf.dealIssue(issueDict=issuePara)
        self.assertTrue(result.result, '办结失败')
        Log.LogOutput( message='事件办结成功')
        #手机端获取办理意见
        para={
              'tqmobile':'true',
              'informationId':informationId
              }
        result=XsGongZuoTaiIntf.get_information_steps(para)
        resultDict=json.loads(result.text)
        self.assertEqual(addPara['personalizedConfiguration.configurationValue'], resultDict['response']['module']['opinionSwit'], '手机端获取办理意见开关出错')
        #修改开关为开
        updPara=copy.deepcopy(XiTongPeiZhiPara.updPersonalConfigListPara)
        updPara['personalizedConfiguration.configurationValue']=ConfigValue.OPEN
        updPara['personalizedConfiguration.id']=resDict['personalizedConfiguration']['id']
        updPara['personalizedConfiguration.configurationType']=addPara['personalizedConfiguration.configurationType']
        ret=XiTongPeiZhiIntf.upd_personal_config(updPara)
        self.assertTrue(ret.result, '修改失败')
        result2=XsGongZuoTaiIntf.get_information_steps(para)
        resultDict2=json.loads(result2.text)
        self.assertEqual(updPara['personalizedConfiguration.configurationValue'], resultDict2['response']['module']['opinionSwit'], '手机端获取办理意见开关出错')
        Log.LogOutput(message='手机端获取办理意见开关正确')
        pass   
    
    def testSystemConfig_04(self):
        """运维管理平台-系统配置- 新增默认分享状态-470"""
        #新增后台默认分享状态是否展现开关配置，默认为公开状态
        addPara=copy.deepcopy(XiTongPeiZhiPara.addPersonalConfigPara)
        addPara['personalizedConfiguration.configurationType']=ConfigType.MORENFENXIANG
        addPara['personalizedConfiguration.configurationValue']=ConfigValue.OPEN
        addPara['personalizedConfiguration.departmentNo']=InitDefaultPara.clueOrgInit['DftQuOrgDepNo']
        result=XiTongPeiZhiIntf.add_personal_config2(addPersonalConfigPara=addPara)
        resDict=json.loads(result.text)
        #新增一条线索
        clueAddPara=copy.deepcopy(XsBaoLiaoPara.xinZeng2)
        XsBaoLiaoIntf.addXianSuo(clueAddPara)
        #验证爆料管理中该爆料的分享状态是否为公开
        listPara=copy.deepcopy(XinXiGuanLiPara.chakanxiansuo)
        checkCluePara=copy.deepcopy(XinXiGuanLiPara.jianchaxiansuo)
        checkCluePara['showState']=ShowState.OPEN
        checkCluePara['contentText']=clueAddPara['information']['contentText']
        ret=XinXiGuanLiIntf.check_clue_in_cluelist_manage(checkCluePara,listPara)
        self.assertTrue(ret, '信息管理中检查线索分享状态不正确')
        Log.LogOutput( message='信息管理中检查线索分享状态正确')
        #验证手机端信息广场数据是否显示正确
        mlistPara=copy.deepcopy(XsInformationSquarePara.informationSquareListPara)
        XsInformationSquareIntf.getClueList(mlistPara)
        mcheckPara=copy.deepcopy(XsInformationSquarePara.informationSquareListCheckPara)
        mcheckPara['showState']=ClueShowState.OPEN
        mcheckPara['contentText']=clueAddPara['information']['contentText']
        ret=XsInformationSquareIntf.checkDictInClueList(mcheckPara, mlistPara)
        self.assertTrue(ret, '手机端验证公开状态失败')
        Log.LogOutput(message='---------默认分享状态为公开时，验证通过--------')
        
        #修改默认分享状态为不公开
        updPara=copy.deepcopy(XiTongPeiZhiPara.updPersonalConfigListPara)
        updPara['personalizedConfiguration.configurationValue']=ConfigValue.CLOSE
        updPara['personalizedConfiguration.id']=resDict['personalizedConfiguration']['id']
        updPara['personalizedConfiguration.configurationType']=addPara['personalizedConfiguration.configurationType']
        ret=XiTongPeiZhiIntf.upd_personal_config(updPara)
        self.assertTrue(ret.result, '修改失败')
        #再次新增一条爆料
        clueAddPara['information']['contentText']='事件描述'+CommonUtil.createRandomString()
        XsBaoLiaoIntf.addXianSuo(clueAddPara)
        #验证爆料管理中该爆料的分享状态是否为不公开
        checkCluePara['showState']=ShowState.CLOSE
        checkCluePara['contentText']=clueAddPara['information']['contentText']
        ret=XinXiGuanLiIntf.check_clue_in_cluelist_manage(checkCluePara,listPara)
        self.assertTrue(ret, '信息管理中检查线索分享状态不正确')
        Log.LogOutput( message='信息管理中检查线索分享状态正确')
        #验证手机端信息广场数据是否显示正确
        mcheckPara['showState']=ClueShowState.CLOSE
        mcheckPara['contentText']=clueAddPara['information']['contentText']
        ret=XsInformationSquareIntf.checkDictInClueList(mcheckPara, mlistPara)
        self.assertFalse(ret, '手机端验证公开状态失败')
        Log.LogOutput(message='---------默认分享状态为不公开时，验证通过--------')       
        pass
    
    def testSystemConfig_05(self):
        """系统配置-运维管理平台-系统配置- 运维人员新增、修改、重置密码、删除-479"""
        #初始化角色
        XiTongPeiZhiIntf.initDefaultRole()
        #新增运维人员
        addPara=copy.deepcopy(XiTongPeiZhiPara.xinZengYunWeiRenYuan)
        addPara['roleIdList']=XiTongPeiZhiIntf.get_role_id_by_name(Name='线索测试自动化岗位')
        res=XiTongPeiZhiIntf.addAdminUser(para=addPara)
        self.assertTrue(res.result, '新增运维人员失败')
        adminUserId=json.loads(res.text)['id']
        #通过列表验证新增功能
        checkPara1={
            'userName':addPara['adminUser.userName'],
            'name':addPara['adminUser.name'],
            'mobile':addPara['adminUser.mobile']
                    }
        listPara=copy.deepcopy(XiTongPeiZhiPara.yunWeiRenYuanLieBiao)
        result=XiTongPeiZhiIntf.checkUserInAdminUserList(checkpara=checkPara1,listpara=listPara)
        self.assertTrue(result, '新增验证失败')
        Log.LogOutput( message='新增运维人员列表验证通过')
        #通过登录验证新增用户成功
        res2=xiansuoyunwei_login(username=addPara['adminUser.userName'],password=addPara['adminUser.password'])
        self.assertTrue(res2, '登录失败')
        Log.LogOutput(message='-------通过登录验证新增用户成功！-------')
        #修改
        updPara=copy.deepcopy(XiTongPeiZhiPara.xiuGaiYunWeiRenYuan)
        updPara['adminUser.id']=adminUserId
        updPara['adminUser.userName']=addPara['adminUser.userName']
        updPara['adminUser.name']=addPara['adminUser.name']+'001'
        updPara['adminUser.mobile']='13222222222'
        result1=XiTongPeiZhiIntf.updAdminUser(para=updPara)
        self.assertTrue(result1.result, '修改成功')
        #验证修改功能
        checkPara2={
            'userName':updPara['adminUser.userName'],
            'name':updPara['adminUser.name'],
            'mobile':updPara['adminUser.mobile']
                    }
        result2=XiTongPeiZhiIntf.checkUserInAdminUserList(checkpara=checkPara2,listpara=listPara)
        self.assertTrue(result2, '修改验证成功')
        Log.LogOutput(message='--------修改验证通过--------')
        #重置密码
        rsPwdPara={
                'adminUser.id':adminUserId,
                'adminUser.password':'123456',
                'confirmPwd':'123456',
                   }
        r=XiTongPeiZhiIntf.updAdminUser(para=rsPwdPara)
        self.assertTrue(r.result, '重置密码失败')
        #通过登录验证
        res2=xiansuoyunwei_login(username=addPara['adminUser.userName'],password=rsPwdPara['adminUser.password'])
        self.assertTrue(res2, '登录失败')
        res3=xiansuoyunwei_login(username=addPara['adminUser.userName'],password=addPara['adminUser.password'])
        self.assertFalse(res3, '登录失败')        
        Log.LogOutput(message='----------通过登录验证重置密码成功！-----------')
        #删除
        delPara={'ids[]':adminUserId}
        result3=XiTongPeiZhiIntf.delAdminUser(para=delPara)
        self.assertTrue(result3.result, '删除失败')
        #通过列表验证删除功能
        result4=XiTongPeiZhiIntf.checkUserInAdminUserList(checkpara=checkPara2,listpara=listPara)
        self.assertFalse(result4, '删除验证成功')
        Log.LogOutput(message='删除验证通过')
        #通过登录验证删除用户成功
        res4=xiansuoyunwei_login(username=addPara['adminUser.userName'],password=addPara['adminUser.password'])
        self.assertFalse(res4, '登录失败')
        Log.LogOutput(message='-----------通过登录验证删除用户成功！------------')
        pass
    
    def testSystemConfig_06(self):
        '''系统配置-运维人员管理-查询-480'''
        try:
            #初始化角色
            XiTongPeiZhiIntf.initDefaultRole()
            #新增运维人员
            addPara=copy.deepcopy(XiTongPeiZhiPara.xinZengYunWeiRenYuan)
            addPara['roleIdList']=XiTongPeiZhiIntf.get_role_id_by_name(Name='线索测试自动化岗位')
            res=XiTongPeiZhiIntf.addAdminUser(para=addPara)
            self.assertTrue(res.result, '新增运维人员失败')
            adminUserId=json.loads(res.text)['id']
            #查询
            searchPara=copy.deepcopy(XiTongPeiZhiPara.yunWeiRenYuanLieBiao)
            searchPara['adminUser.userName']=addPara['adminUser.userName']
            result=XiTongPeiZhiIntf.findAdminUserList(para=searchPara)
            self.assertTrue(result.result, '查询失败')
            #验证存在性
            checkPara={
                'userName':addPara['adminUser.userName'],
                'name':addPara['adminUser.name'],
                'mobile':addPara['adminUser.mobile']                   
                       }
            result=XiTongPeiZhiIntf.checkUserInAdminUserList(checkpara=checkPara,listpara=searchPara)
            self.assertTrue(result, '查询验证失败')
            #唯一性
#             print searchPara
            listDict=json.loads(XiTongPeiZhiIntf.findAdminUserList(para=searchPara).text)
            print listDict['records']
            self.assertEquals(listDict['records'], 1, '查询结果唯一性错误')
            Log.LogOutput( message='查询功能验证通过')
        finally:
            delPara={'ids[]':adminUserId}
            result3=XiTongPeiZhiIntf.delAdminUser(para=delPara)
            self.assertTrue(result3.result, '删除失败')            
        pass
    
    def testSystemConfig_07(self):
        '''系统配置-公告管理新增-754'''
        #清空所有公告
        ret=XiTongPeiZhiIntf.del_all_operation_notice()
        self.assertTrue(ret, '清空所有公告失败')
        addPara=copy.deepcopy(XiTongPeiZhiPara.yunWeiGongGaoXinZeng)
        addPara['operationNotice.noticeType']=NoticeType.SYSTEM
        addPara['operationNotice.title']='标题'+createRandomString()
        addPara['homePageShow']='on'
        addPara['operationNotice.homePageShow']=HomePageShow.SHOW
        addPara['operationNotice.contentText']='公告内容'+createRandomString()
        addPara['operationNotice.listContentText']='列表显示内容'+createRandomString()
        files = {
                 'androidImgUrl':open('C:/autotest_file/Tulips.jpg', 'rb'),
                'iosImgUrl':open('C:/autotest_file/Penguins.jpg','rb')
                }                  
        res=XiTongPeiZhiIntf.add_operation_notice(addPara,files=files)
        self.assertTrue(res, "新增失败")
#         resDict=json.loads(res.text)
        #列表检查
        checkPara=copy.deepcopy(XiTongPeiZhiPara.yunWeiGongGaoLieBiaoJianCha)
        checkPara['noticeType']=addPara['operationNotice.noticeType']
        checkPara['title']=addPara['operationNotice.title']
        checkPara['homePageShow']=addPara['operationNotice.homePageShow']
        checkPara['contentText']=addPara['operationNotice.contentText']
        checkPara['listContentText']=addPara['operationNotice.listContentText']
        checkPara['closeState']=CloseState.OPEN#默认开启状态
        listPara=copy.deepcopy(XiTongPeiZhiPara.yunWeiGongGaoLieBiao)
        ret=XiTongPeiZhiIntf.check_operation_notice_list(checkPara, listPara)
        self.assertTrue(ret, '新增列表检查出错')
        #手机端首页检查
        mlistpara1={    'tqmobile':'true',
                    'departmentNo':InitDefaultPara.clueOrgInit['DftQuOrgDepNo']
                    }
        XsShouYeIntf.get_roll_operation_notice_list(mlistpara1)
        mcheckpara1=copy.deepcopy(XsShouYePara.gunDongGongGaoJianCha)
        mcheckpara1['contentText']=addPara['operationNotice.title']
        ret=XsShouYeIntf.check_roll_operation_notice_list(mcheckpara1, mlistpara1)
        self.assertTrue(ret , '首页检查滚动公告失败')
        #手机端公告页面检查
        mlistpara2=copy.deepcopy(XsGongGaoLanPara.shouJiYunWeiGongGaoLieBiao)
        XsGongGaoLanIntf.get_mobile_operation_notice_list(mlistpara2)
        mcheckpara2=copy.deepcopy(XsGongGaoLanPara.shouJiYunWeiGongGaoLieBiaoJianCha)
        mcheckpara2['title']=addPara['operationNotice.title']
        mcheckpara2['homePageShow']=addPara['operationNotice.homePageShow']
        mcheckpara2['contentText']=addPara['operationNotice.contentText']
        mcheckpara2['listContentText']=addPara['operationNotice.listContentText']
        mcheckpara2['closeState']=CloseState.OPEN#默认开启状态
        ret=XsGongGaoLanIntf.check_mobile_operation_notice_list(mcheckpara2, mlistpara2)
        self.assertTrue(ret , '手机端公告列表检查运维公告失败')
        
        pass
    
    def testSystemConfig_08(self):
        '''系统配置-公告管理修改-755'''
        #清空所有公告
        ret=XiTongPeiZhiIntf.del_all_operation_notice()
        self.assertTrue(ret, '清空所有公告失败')
        addPara=copy.deepcopy(XiTongPeiZhiPara.yunWeiGongGaoXinZeng)
        addPara['operationNotice.noticeType']=NoticeType.SYSTEM
        addPara['operationNotice.title']='标题'+createRandomString()
        addPara['homePageShow']='on'
        addPara['operationNotice.homePageShow']=HomePageShow.SHOW
        addPara['operationNotice.contentText']='公告内容'+createRandomString()
        addPara['operationNotice.listContentText']='列表显示内容'+createRandomString()
        files = {
                 'androidImgUrl':open('C:/autotest_file/Tulips.jpg', 'rb'),
                'iosImgUrl':open('C:/autotest_file/Penguins.jpg','rb')
                }                  
        res=XiTongPeiZhiIntf.add_operation_notice(addPara,files=files)
        self.assertTrue(res, "新增失败")
        resDict=json.loads(res.text)
        #修改
        updPara={
          'operationNotice.id':resDict['id'],
          'operationNotice.noticeType':NoticeType.ACTIVITY,
          'operationNotice.title':addPara['operationNotice.title']+'修改',
          'operationNotice.homePageShow':HomePageShow.SHOW,#0不在首页显示，1在首页显示
          'noticeEndDate':addPara['noticeEndDate'],
          'operationNotice.contentText':addPara['operationNotice.contentText']+'修改',
          'operationNotice.listContentText':addPara['operationNotice.listContentText']+'修改'
               }
        ret=XiTongPeiZhiIntf.upd_operation_notice(updPara, files)
        self.assertTrue(ret.result, '修改失败')
#         resDict=json.loads(res.text)
        #列表检查
        checkPara=copy.deepcopy(XiTongPeiZhiPara.yunWeiGongGaoLieBiaoJianCha)
        checkPara['noticeType']=updPara['operationNotice.noticeType']
        checkPara['title']=updPara['operationNotice.title']
        checkPara['homePageShow']=updPara['operationNotice.homePageShow']
        checkPara['contentText']=updPara['operationNotice.contentText']
        checkPara['listContentText']=updPara['operationNotice.listContentText']
        checkPara['closeState']=CloseState.OPEN#默认开启状态
        listPara=copy.deepcopy(XiTongPeiZhiPara.yunWeiGongGaoLieBiao)
        ret=XiTongPeiZhiIntf.check_operation_notice_list(checkPara, listPara)
        self.assertTrue(ret, '修改后列表检查出错')
        #手机端首页检查
        mlistpara1={    'tqmobile':'true',
                    'departmentNo':InitDefaultPara.clueOrgInit['DftQuOrgDepNo']
                    }
        XsShouYeIntf.get_roll_operation_notice_list(mlistpara1)
        mcheckpara1=copy.deepcopy(XsShouYePara.gunDongGongGaoJianCha)
        mcheckpara1['contentText']=updPara['operationNotice.title']
        ret=XsShouYeIntf.check_roll_operation_notice_list(mcheckpara1, mlistpara1)
        self.assertTrue(ret , '首页检查滚动公告失败')
        #手机端公告页面检查
        mlistpara2=copy.deepcopy(XsGongGaoLanPara.shouJiYunWeiGongGaoLieBiao)
        XsGongGaoLanIntf.get_mobile_operation_notice_list(mlistpara2)
        mcheckpara2=copy.deepcopy(XsGongGaoLanPara.shouJiYunWeiGongGaoLieBiaoJianCha)
        mcheckpara2['title']=updPara['operationNotice.title']
        mcheckpara2['homePageShow']=updPara['operationNotice.homePageShow']
        mcheckpara2['contentText']=updPara['operationNotice.contentText']
        mcheckpara2['listContentText']=updPara['operationNotice.listContentText']
        mcheckpara2['closeState']=CloseState.OPEN#默认开启状态
        ret=XsGongGaoLanIntf.check_mobile_operation_notice_list(mcheckpara2, mlistpara2)
        self.assertTrue(ret , '手机端公告列表检查运维公告失败')
        #将公告修改为“首页不显示”
        updPara['operationNotice.id']=resDict['id']
        updPara['operationNotice.noticeType']=NoticeType.ACTIVITY
        updPara['title']=updPara['operationNotice.title']
        updPara['operationNotice.homePageShow']=HomePageShow.HIDE
        updPara['noticeEndDate']=addPara['noticeEndDate']
        updPara['operationNotice.contentText']=addPara['operationNotice.contentText']+'修改'
        updPara['operationNotice.listContentText']=addPara['operationNotice.listContentText']+'修改'
        ret=XiTongPeiZhiIntf.upd_operation_notice(updPara, files)
        self.assertTrue(ret.result, '修改失败')
        checkPara['homePageShow']=updPara['operationNotice.homePageShow']
        mcheckpara2['homePageShow']=updPara['operationNotice.homePageShow']
        ret=XiTongPeiZhiIntf.check_operation_notice_list(checkPara, listPara)
        self.assertTrue(ret, '修改后列表检查出错')
        ret=XsShouYeIntf.check_roll_operation_notice_list(mcheckpara1, mlistpara1)
        self.assertFalse(ret , '首页检查滚动公告失败')
        ret=XsGongGaoLanIntf.check_mobile_operation_notice_list(mcheckpara2, mlistpara2)
        self.assertTrue(ret , '手机端公告列表检查运维公告失败')
        
        pass
    
    def testSystemConfig_09(self):
        '''系统配置-公告管理删除-756'''
        #清空所有公告
        ret=XiTongPeiZhiIntf.del_all_operation_notice()
        self.assertTrue(ret, '清空所有公告失败')
        addPara=copy.deepcopy(XiTongPeiZhiPara.yunWeiGongGaoXinZeng)
        addPara['operationNotice.noticeType']=NoticeType.SYSTEM
        addPara['operationNotice.title']='标题'+createRandomString()
        addPara['homePageShow']='on'
        addPara['operationNotice.homePageShow']=HomePageShow.SHOW
        addPara['operationNotice.contentText']='公告内容'+createRandomString()
        addPara['operationNotice.listContentText']='列表显示内容'+createRandomString()
        files = {
                 'androidImgUrl':open('C:/autotest_file/Tulips.jpg', 'rb'),
                'iosImgUrl':open('C:/autotest_file/Penguins.jpg','rb')
                }                  
        res=XiTongPeiZhiIntf.add_operation_notice(addPara,files=files)
        self.assertTrue(res, "新增失败")
        resDict=json.loads(res.text)
        #列表检查
        checkPara=copy.deepcopy(XiTongPeiZhiPara.yunWeiGongGaoLieBiaoJianCha)
        checkPara['noticeType']=addPara['operationNotice.noticeType']
        checkPara['title']=addPara['operationNotice.title']
        checkPara['homePageShow']=addPara['operationNotice.homePageShow']
        checkPara['contentText']=addPara['operationNotice.contentText']
        checkPara['listContentText']=addPara['operationNotice.listContentText']
        checkPara['closeState']=CloseState.OPEN#默认开启状态
        listPara=copy.deepcopy(XiTongPeiZhiPara.yunWeiGongGaoLieBiao)
        ret=XiTongPeiZhiIntf.check_operation_notice_list(checkPara, listPara)
        self.assertTrue(ret, '新增列表检查出错')
        #手机端首页检查
        mlistpara1={    'tqmobile':'true',
                    'departmentNo':InitDefaultPara.clueOrgInit['DftQuOrgDepNo']
                    }
        XsShouYeIntf.get_roll_operation_notice_list(mlistpara1)
        mcheckpara1=copy.deepcopy(XsShouYePara.gunDongGongGaoJianCha)
        mcheckpara1['contentText']=addPara['operationNotice.title']
        ret=XsShouYeIntf.check_roll_operation_notice_list(mcheckpara1, mlistpara1)
        self.assertTrue(ret , '首页检查滚动公告失败')
        #手机端公告页面检查
        mlistpara2=copy.deepcopy(XsGongGaoLanPara.shouJiYunWeiGongGaoLieBiao)
        XsGongGaoLanIntf.get_mobile_operation_notice_list(mlistpara2)
        mcheckpara2=copy.deepcopy(XsGongGaoLanPara.shouJiYunWeiGongGaoLieBiaoJianCha)
        mcheckpara2['title']=addPara['operationNotice.title']
        mcheckpara2['homePageShow']=addPara['operationNotice.homePageShow']
        mcheckpara2['contentText']=addPara['operationNotice.contentText']
        mcheckpara2['listContentText']=addPara['operationNotice.listContentText']
        mcheckpara2['closeState']=CloseState.OPEN#默认开启状态
        ret=XsGongGaoLanIntf.check_mobile_operation_notice_list(mcheckpara2, mlistpara2)
        self.assertTrue(ret , '手机端公告列表检查运维公告失败')
        #删除
        res=XiTongPeiZhiIntf.del_operation_notice({'ids[]':resDict['id']})
        self.assertTrue(res, "删除失败")
        ret=XiTongPeiZhiIntf.check_operation_notice_list(checkPara, listPara)
        self.assertFalse(ret, '修改后列表检查出错')
        ret=XsShouYeIntf.check_roll_operation_notice_list(mcheckpara1, mlistpara1)
        self.assertFalse(ret , '首页检查滚动公告失败')
        ret=XsGongGaoLanIntf.check_mobile_operation_notice_list(mcheckpara2, mlistpara2)
        self.assertFalse(ret , '手机端公告列表检查运维公告失败')        
        pass
    
    def testSystemConfig_10(self):
        '''系统配置-公告开启/关闭-765'''
        #清空所有公告
        ret=XiTongPeiZhiIntf.del_all_operation_notice()
        self.assertTrue(ret, '清空所有公告失败')
        #新增公告
        addPara=copy.deepcopy(XiTongPeiZhiPara.yunWeiGongGaoXinZeng)
        addPara['operationNotice.noticeType']=NoticeType.SYSTEM
        addPara['operationNotice.title']='标题'+createRandomString()
        addPara['homePageShow']='on'
        addPara['operationNotice.homePageShow']=HomePageShow.SHOW
        addPara['operationNotice.contentText']='公告内容'+createRandomString()
        addPara['operationNotice.listContentText']='列表显示内容'+createRandomString()
        files = {
                 'androidImgUrl':open('C:/autotest_file/Tulips.jpg', 'rb'),
                'iosImgUrl':open('C:/autotest_file/Penguins.jpg','rb')
                }                  
        res=XiTongPeiZhiIntf.add_operation_notice(addPara,files=files)
        self.assertTrue(res, "新增失败")
        resDict=json.loads(res.text)
        #默认开启状态
        checkPara=copy.deepcopy(XiTongPeiZhiPara.yunWeiGongGaoLieBiaoJianCha)
        checkPara['noticeType']=addPara['operationNotice.noticeType']
        checkPara['title']=addPara['operationNotice.title']
        checkPara['homePageShow']=addPara['operationNotice.homePageShow']
        checkPara['contentText']=addPara['operationNotice.contentText']
        checkPara['listContentText']=addPara['operationNotice.listContentText']
        checkPara['closeState']=CloseState.OPEN#默认开启状态
        listPara=copy.deepcopy(XiTongPeiZhiPara.yunWeiGongGaoLieBiao)
        ret=XiTongPeiZhiIntf.check_operation_notice_list(checkPara, listPara)
        self.assertTrue(ret, '新增列表检查出错')        
        #手机端首页检查
        mlistpara1={    'tqmobile':'true',
                    'departmentNo':InitDefaultPara.clueOrgInit['DftQuOrgDepNo']
                    }
        XsShouYeIntf.get_roll_operation_notice_list(mlistpara1)
        mcheckpara1=copy.deepcopy(XsShouYePara.gunDongGongGaoJianCha)
        mcheckpara1['contentText']=addPara['operationNotice.title']
        ret=XsShouYeIntf.check_roll_operation_notice_list(mcheckpara1, mlistpara1)
        self.assertTrue(ret , '首页检查滚动公告失败')
        #手机端公告页面检查
        mlistpara2=copy.deepcopy(XsGongGaoLanPara.shouJiYunWeiGongGaoLieBiao)
        XsGongGaoLanIntf.get_mobile_operation_notice_list(mlistpara2)
        mcheckpara2=copy.deepcopy(XsGongGaoLanPara.shouJiYunWeiGongGaoLieBiaoJianCha)
        mcheckpara2['title']=addPara['operationNotice.title']
        mcheckpara2['homePageShow']=addPara['operationNotice.homePageShow']
        mcheckpara2['contentText']=addPara['operationNotice.contentText']
        mcheckpara2['listContentText']=addPara['operationNotice.listContentText']
        mcheckpara2['closeState']=CloseState.OPEN#默认开启状态
        ret=XsGongGaoLanIntf.check_mobile_operation_notice_list(mcheckpara2, mlistpara2)
        self.assertTrue(ret , '手机端公告列表检查运维公告失败')
        Log.LogOutput( message='------新增功能验证通过--------')
        
        
        #关闭公告
        ret=XiTongPeiZhiIntf.close_operation_notice({'ids[]':resDict['id']})
        self.assertTrue(ret , '手机端公告列表检查运维公告失败')
        
        checkPara['closeState']=CloseState.CLOSE
        ret=XiTongPeiZhiIntf.check_operation_notice_list(checkPara, listPara)
        self.assertTrue(ret, '关闭操作后列表检查出错')
        ret=XsShouYeIntf.check_roll_operation_notice_list(mcheckpara1, mlistpara1)
        self.assertFalse(ret , '首页检查滚动公告失败')
        mcheckpara2['closeState']=CloseState.CLOSE
        ret=XsGongGaoLanIntf.check_mobile_operation_notice_list(mcheckpara2, mlistpara2)
        self.assertFalse(ret , '手机端公告列表检查运维公告失败')
        Log.LogOutput( message='------关闭功能验证通过--------')
        #开启公告
        
        ret=XiTongPeiZhiIntf.open_operation_notice({'ids[]':resDict['id']})
        self.assertTrue(ret , '手机端公告列表检查运维公告失败')
        checkPara['closeState']=CloseState.OPEN
        ret=XiTongPeiZhiIntf.check_operation_notice_list(checkPara, listPara)
        self.assertTrue(ret, '开启操作后列表检查出错')
        ret=XsShouYeIntf.check_roll_operation_notice_list(mcheckpara1, mlistpara1)
        self.assertTrue(ret , '首页检查滚动公告失败')
        mcheckpara2['closeState']=CloseState.OPEN
        ret=XsGongGaoLanIntf.check_mobile_operation_notice_list(mcheckpara2, mlistpara2)
        self.assertTrue(ret , '手机端公告列表检查运维公告失败')        
        Log.LogOutput( message='------开启功能验证通过--------')
        pass       
    
    def testSystemConfig_11(self):
        '''系统配置-公告查询-758'''
        #清空所有公告
        ret=XiTongPeiZhiIntf.del_all_operation_notice()
        self.assertTrue(ret, '清空所有公告失败')
        #新增公告
        addPara=copy.deepcopy(XiTongPeiZhiPara.yunWeiGongGaoXinZeng)
        addPara['operationNotice.noticeType']=NoticeType.SYSTEM
        addPara['operationNotice.title']='标题'+createRandomString()
        addPara['homePageShow']='on'
        addPara['operationNotice.homePageShow']=HomePageShow.SHOW
        addPara['operationNotice.contentText']='公告内容'+createRandomString()
        addPara['operationNotice.listContentText']='列表显示内容'+createRandomString()
        files = {
                 'androidImgUrl':open('C:/autotest_file/Tulips.jpg', 'rb'),
                'iosImgUrl':open('C:/autotest_file/Penguins.jpg','rb')
                }                  
        res=XiTongPeiZhiIntf.add_operation_notice(addPara,files=files)
        self.assertTrue(res, "新增失败")
        #新增第二条
        addPara2=copy.deepcopy(addPara)
        addPara2['operationNotice.title']='标题'+createRandomString()
        res=XiTongPeiZhiIntf.add_operation_notice(addPara2,files=files)
        self.assertTrue(res, "新增失败")
        #查询参数,以第一条标题为查询条件，检查列表中的标题是否正确
        searchPara=copy.deepcopy(XiTongPeiZhiPara.yunWeiGongGaoLieBiao)
        searchPara['operationNotice.title']=addPara['operationNotice.title']
        checkPara=copy.deepcopy(XiTongPeiZhiPara.yunWeiGongGaoLieBiaoJianCha)
        checkPara['title']=addPara['operationNotice.title']
        ret=XiTongPeiZhiIntf.check_operation_notice_list(checkPara, searchPara)
        self.assertTrue(ret, '查询列表检查出错')
        #检查查询结果中是否包含第二条标题
        checkPara['title']=addPara2['operationNotice.title']
        ret=XiTongPeiZhiIntf.check_operation_notice_list(checkPara, searchPara)
        self.assertFalse(ret, '查询列表检查出错')        
        pass
    
    def testSystemConfig_12(self):
        '''系统配置-热门搜索管理-新增、修改、删除、查询797'''
        #清空所有热门搜索配置
        XiTongPeiZhiIntf.del_all_hot_search()
        #新增一条热门搜索
        addPara=copy.deepcopy(XiTongPeiZhiPara.hotSearchAddPara)
        addPara['keyword']='热搜关键字'+createRandomString()
        addPara['remark']='备注'+createRandomString()
        res=XiTongPeiZhiIntf.add_hot_search(addPara)
        resDict=json.loads(res.text)
        #PC端列表检查
        checkPara=copy.deepcopy(XiTongPeiZhiPara.hotSearchListCheckPara)
        checkPara['id']=resDict['id']
        checkPara['infoType']=addPara['infoType']
        checkPara['keyword']=addPara['keyword']
        checkPara['state']=True
        checkPara['remark']=addPara['remark']
        #列表参数
        listPara=copy.deepcopy(XiTongPeiZhiPara.hotSearchListPara)
        ret=XiTongPeiZhiIntf.check_hot_search_list(checkPara, listPara)
        self.assertTrue(ret, '检查列表成功！')
        #手机端查看
        mlistpara=copy.deepcopy(XsInformationSquarePara.getHotKeywordPara)
        ret=XsInformationSquareIntf.check_hot_search_list(checkPara, mlistpara)
        self.assertTrue(ret, '手机端检查热门关键词失败')
        Log.LogOutput( message='---------新增热门搜索关键词成功！--------')
        
        #修改
        updPara=copy.deepcopy(XiTongPeiZhiPara.hotSearchUpdPara)
        updPara['id']=resDict['id']
        updPara['keyword']=addPara['keyword']+'修改'
        updPara['remark']=addPara['remark']+'修改'
        XiTongPeiZhiIntf.upd_hot_search(updPara)
        #PC端列表检查
        checkPara['keyword']=updPara['keyword']
        checkPara['remark']=updPara['remark']
        ret=XiTongPeiZhiIntf.check_hot_search_list(checkPara, listPara)
        self.assertTrue(ret, '检查列表成功！')
        #手机端列表检查
        ret=XsInformationSquareIntf.check_hot_search_list(checkPara, mlistpara)
        self.assertTrue(ret, '手机端检查热门关键词失败')
        Log.LogOutput( message='---------修改热门搜索关键词成功！--------')
        
        #再次新增一条数据
        addPara2=copy.deepcopy(XiTongPeiZhiPara.hotSearchAddPara)
        addPara2['keyword']='热搜关键字'+createRandomString()
        addPara2['remark']='备注'+createRandomString()
        res2=XiTongPeiZhiIntf.add_hot_search(addPara2)
        self.assertTrue(res2.result, '新增失败')
        res2Dict=json.loads(res2.text)
        #检查第二条数据是否位于列表
        #第二条数据检查参数
        checkPara2=copy.deepcopy(XiTongPeiZhiPara.hotSearchListCheckPara)
        checkPara2['id']=res2Dict['id']
        checkPara2['infoType']=addPara2['infoType']
        checkPara2['keyword']=addPara2['keyword']
        checkPara2['state']=True
        checkPara2['remark']=addPara2['remark']
        ret=XiTongPeiZhiIntf.check_hot_search_list(checkPara2, listPara)
        self.assertTrue(ret, '检查列表成功！')
        #搜索
        searchpara=copy.deepcopy(XiTongPeiZhiPara.hotSearchListPara)
        searchpara['hotSearch.keyword']=updPara['keyword']
        ret=XiTongPeiZhiIntf.check_hot_search_list(checkPara, searchpara)
        self.assertTrue(ret, '检查列表成功！')
        #检查第二条是否位于搜索列表中
        ret=XiTongPeiZhiIntf.check_hot_search_list(checkPara2, searchpara)
        self.assertFalse(ret, '检查列表成功！')        
        Log.LogOutput( message='---------查询热门搜索关键词成功！--------')
        
        #删除,只删除第二条数据
        delpara={
                 'ids[]':res2Dict['id']
                 }
        XiTongPeiZhiIntf.del_hot_search(delpara)
        #检查第二条数据是否还位于PC端列表中
        ret=XiTongPeiZhiIntf.check_hot_search_list(checkPara2, listPara)
        self.assertFalse(ret, '检查列表成功！')
        #检查第二条数据是否还位于手机端列表中
        ret=XsInformationSquareIntf.check_hot_search_list(checkPara2, mlistpara)
        self.assertFalse(ret, '手机端检查热门关键词失败')
        #检查第一条数据是否不受删除影响
        #PC端
        ret=XiTongPeiZhiIntf.check_hot_search_list(checkPara, listPara)
        self.assertTrue(ret, '检查列表成功！')
        #手机端列表检查
        ret=XsInformationSquareIntf.check_hot_search_list(checkPara, mlistpara)
        self.assertTrue(ret, '手机端检查热门关键词失败')        
        Log.LogOutput( message='---------删除热门搜索关键词成功！--------')        
        pass    

    def testSystemConfig_13(self):
        '''系统配置-热门搜索管理-上移/下移操作-868'''
        #清空所有热门搜索配置
        XiTongPeiZhiIntf.del_all_hot_search()
        #新增一条热门搜索
        addPara1=copy.deepcopy(XiTongPeiZhiPara.hotSearchAddPara)
        addPara1['keyword']='第一条热搜关键字'+createRandomString()
        addPara1['remark']='备注'+createRandomString()
        res1=XiTongPeiZhiIntf.add_hot_search(addPara1)
        resDict1=json.loads(res1.text)       
        
        #再次新增一条数据
        addPara2=copy.deepcopy(XiTongPeiZhiPara.hotSearchAddPara)
        addPara2['keyword']='第二条热搜关键字'+createRandomString()
        addPara2['remark']='备注'+createRandomString()
        res2=XiTongPeiZhiIntf.add_hot_search(addPara2)
        resDict2=json.loads(res2.text)
        #PC端序号
        seq1=XiTongPeiZhiIntf.get_hot_search_display_seq_by_keyword(addPara1['keyword'])
        seq2=XiTongPeiZhiIntf.get_hot_search_display_seq_by_keyword(addPara2['keyword'])
        #手机端序号
        m_seq1=XsInformationSquareIntf.get_hot_search_display_seq_by_keyword_for_mobile(addPara1['keyword'])
        m_seq2=XsInformationSquareIntf.get_hot_search_display_seq_by_keyword_for_mobile(addPara2['keyword'])
        self.assertEqual(m_seq1, seq1,'手机端获取序号与PC端不一致')
        self.assertEqual(m_seq2, seq2,'手机端获取序号与PC端不一致')
#         print seq1,seq2
        #将第一条数据下移
        hotSearchMovePara=copy.deepcopy(XiTongPeiZhiPara.hotSearchMovePara)
        hotSearchMovePara['id']=resDict1['id']
        hotSearchMovePara['referId']=resDict2['id']
        hotSearchMovePara['position']='after'
        
        XiTongPeiZhiIntf.move_hot_search(hotSearchMovePara)
        #获取移动后的排序号
        seq11=XiTongPeiZhiIntf.get_hot_search_display_seq_by_keyword(addPara1['keyword'])
        seq22=XiTongPeiZhiIntf.get_hot_search_display_seq_by_keyword(addPara2['keyword'])
#         print seq11,seq22
        self.assertEqual(seq1+1, seq11, '下移后序号错误')
        self.assertEqual(seq2- 1, seq22, '下移后序号错误')
        #手机端序号
        m_seq11=XsInformationSquareIntf.get_hot_search_display_seq_by_keyword_for_mobile(addPara1['keyword'])
        m_seq22=XsInformationSquareIntf.get_hot_search_display_seq_by_keyword_for_mobile(addPara2['keyword'])
        self.assertEqual(m_seq11, seq11,'手机端获取序号与PC端不一致')
        self.assertEqual(m_seq22, seq22,'手机端获取序号与PC端不一致')        
        Log.LogOutput( message='---------下移成功！--------')
        
        #上移操作
        hotSearchMovePara['id']=resDict1['id']
        hotSearchMovePara['referId']=resDict2['id']
        hotSearchMovePara['position']='before'#Direction.UP
        XiTongPeiZhiIntf.move_hot_search(hotSearchMovePara)
        #获取移动后的排序号
        seq111=XiTongPeiZhiIntf.get_hot_search_display_seq_by_keyword(addPara1['keyword'])
        seq222=XiTongPeiZhiIntf.get_hot_search_display_seq_by_keyword(addPara2['keyword'])
#         print seq111,seq222
        self.assertEqual(seq11-1, seq111, '上移后序号错误')
        self.assertEqual(seq22+1, seq222, '上移后序号错误')
        #手机端序号
        m_seq111=XsInformationSquareIntf.get_hot_search_display_seq_by_keyword_for_mobile(addPara1['keyword'])
        m_seq222=XsInformationSquareIntf.get_hot_search_display_seq_by_keyword_for_mobile(addPara2['keyword'])
        self.assertEqual(m_seq111, seq111,'手机端获取序号与PC端不一致')
        self.assertEqual(m_seq222, seq222,'手机端获取序号与PC端不一致')
        
        Log.LogOutput( message='---------上移成功！--------')   
        pass
    
    def testSystemConfig_14(self):
        '''系统配置-热门搜索管理-启用/停用操作-871'''
        #清空所有热门搜索配置
        XiTongPeiZhiIntf.del_all_hot_search()
        #新增一条热门搜索
        addPara=copy.deepcopy(XiTongPeiZhiPara.hotSearchAddPara)
        addPara['keyword']='热搜关键字'+createRandomString()
        addPara['remark']='备注'+createRandomString()
        res=XiTongPeiZhiIntf.add_hot_search(addPara)
        resDict=json.loads(res.text)
        #停用操作
        para={
                  'id':resDict['id'],
                'state':'false'#true开启，false关闭          
                    }
        XiTongPeiZhiIntf.switch_hot_search(para)
        #PC端列表检查
        checkPara=copy.deepcopy(XiTongPeiZhiPara.hotSearchListCheckPara)
        checkPara['id']=resDict['id']
        checkPara['infoType']=addPara['infoType']
        checkPara['keyword']=addPara['keyword']
        checkPara['state']=False
        checkPara['remark']=addPara['remark']
        #列表参数
        listPara=copy.deepcopy(XiTongPeiZhiPara.hotSearchListPara)
        ret=XiTongPeiZhiIntf.check_hot_search_list(checkPara, listPara)
        self.assertTrue(ret, '检查列表成功！')
        #手机端查看
        mlistpara=copy.deepcopy(XsInformationSquarePara.getHotKeywordPara)
        ret=XsInformationSquareIntf.check_hot_search_list(checkPara, mlistpara)
        #关闭时，手机端返回的数据不包含检测参数
        self.assertFalse(ret, '手机端检查热门关键词失败')
        Log.LogOutput( message='---------关闭热门搜索关键词成功！--------')
        
        #开启
        para['state']='true'
        XiTongPeiZhiIntf.switch_hot_search(para)
        #PC端列表检查
        checkPara=copy.deepcopy(XiTongPeiZhiPara.hotSearchListCheckPara)
        checkPara['id']=resDict['id']
        checkPara['infoType']=addPara['infoType']
        checkPara['keyword']=addPara['keyword']
        checkPara['state']=True
        checkPara['remark']=addPara['remark']
        #列表参数
        listPara=copy.deepcopy(XiTongPeiZhiPara.hotSearchListPara)
        ret=XiTongPeiZhiIntf.check_hot_search_list(checkPara, listPara)
        self.assertTrue(ret, '检查列表成功！')
        #手机端查看
        mlistpara=copy.deepcopy(XsInformationSquarePara.getHotKeywordPara)
        ret=XsInformationSquareIntf.check_hot_search_list(checkPara, mlistpara)
        self.assertTrue(ret, '手机端检查热门关键词失败')
        Log.LogOutput( message='---------开启热门搜索关键词成功！--------')        
        pass 
      
    def testSystemConfig_15(self):
        '''系统配置-便民服务配置-增删改操作-494'''
        #清空所有配置
        XiTongPeiZhiIntf.del_all_convenience_service()
        #新增
        addConvenienceServicePara=copy.deepcopy(XiTongPeiZhiPara.addConvenienceServicePara)
        addConvenienceServicePara['convenienceService.title']='便民服务'+createRandomString()
        addConvenienceServicePara['convenienceService.linkUrl']='http://'+createRandomString()
        files={
               'iosImgValue':open('C:/autotest_file/Tulips.jpg', 'rb'),
               'androidImgValue':open('C:/autotest_file/Penguins.jpg','rb')
               }
        res=XiTongPeiZhiIntf.add_convenience_service(addConvenienceServicePara,files=files)
        resDict=json.loads(res.text)
        #检查列表
        listpara=copy.deepcopy(XiTongPeiZhiPara.convenienceServiceListPara)
        checkpara=copy.deepcopy(XiTongPeiZhiPara.convenienceServiceCheckPara)
        checkpara['id']=resDict['id']
        checkpara['linkUrl']=resDict['linkUrl']
        checkpara['title']=resDict['title']
        checkpara['state']=ConvenienceState.OPEN
        ret=XiTongPeiZhiIntf.check_convenience_service_list(checkpara, listpara)
        self.assertTrue(ret, '新增后检查列表失败')
        #手机端检查列表
        mcheckpara=copy.deepcopy(XsShouYePara.convenienceServiceListCheckPara)
        mcheckpara['title']=resDict['title']
        mcheckpara['linkUrl']=resDict['linkUrl']
        mlistpara= {    
                    'tqmobile':'true',
                    'mobileType':'ios',
                    'apiVersion':'3'
                }   
        ret=XsShouYeIntf.check_convenience_service_list_for_mobile(mcheckpara, mlistpara)
        self.assertTrue(ret, '手机端检查列表错误')
        Log.LogOutput( message='---------便民服务配置新增成功！--------') 
        #修改
        updConvenienceServicePara=copy.deepcopy(XiTongPeiZhiPara.updConvenienceServicePara)
        updConvenienceServicePara['convenienceService.id']=resDict['id']
        updConvenienceServicePara['convenienceService.title']='便民服务修改'+createRandomString()
        updConvenienceServicePara['convenienceService.linkUrl']='http2://'+createRandomString()
        XiTongPeiZhiIntf.upd_convenience_service(updConvenienceServicePara, files)
        #检查参数
        checkpara['linkUrl']=updConvenienceServicePara['convenienceService.linkUrl']
        checkpara['title']=updConvenienceServicePara['convenienceService.title']
        ret=XiTongPeiZhiIntf.check_convenience_service_list(checkpara, listpara)
        self.assertTrue(ret, '修改后检查列表失败')
        mcheckpara['title']=updConvenienceServicePara['convenienceService.title']
        mcheckpara['linkUrl']=updConvenienceServicePara['convenienceService.linkUrl']
        ret=XsShouYeIntf.check_convenience_service_list_for_mobile(mcheckpara, mlistpara)
        self.assertTrue(ret, '手机端检查列表错误')        
        Log.LogOutput( message='---------便民服务配置修改成功！--------')       
        #删除
        XiTongPeiZhiIntf.del_convenience_service({'ids[]':resDict['id']})
        ret=XiTongPeiZhiIntf.check_convenience_service_list(checkpara, listpara)
        self.assertFalse(ret, '删除后PC端检查列表失败')
        ret=XsShouYeIntf.check_convenience_service_list_for_mobile(mcheckpara, mlistpara)
        self.assertFalse(ret, '删除后手机端检查列表错误')                  
        Log.LogOutput( message='---------便民服务配置删除成功！--------')
        pass
    
    def testSystemConfig_16(self):
        '''系统配置-便民服务配置-开启/关闭操作-1016'''
        #清空所有配置
        XiTongPeiZhiIntf.del_all_convenience_service()        
        addConvenienceServicePara=copy.deepcopy(XiTongPeiZhiPara.addConvenienceServicePara)
        addConvenienceServicePara['convenienceService.title']='便民服务'+createRandomString()
        addConvenienceServicePara['convenienceService.linkUrl']='http://'+createRandomString()
        files={
               'iosImgValue':open('C:/autotest_file/Tulips.jpg', 'rb'),
               'androidImgValue':open('C:/autotest_file/Penguins.jpg','rb')
               }
        res=XiTongPeiZhiIntf.add_convenience_service(addConvenienceServicePara,files=files)
        resDict=json.loads(res.text)
        #PC检查列表参数
        listpara=copy.deepcopy(XiTongPeiZhiPara.convenienceServiceListPara)
        checkpara=copy.deepcopy(XiTongPeiZhiPara.convenienceServiceCheckPara)
        checkpara['id']=resDict['id']
        checkpara['linkUrl']=resDict['linkUrl']
        checkpara['title']=resDict['title']
        checkpara['state']=ConvenienceState.OPEN
        ret=XiTongPeiZhiIntf.check_convenience_service_list(checkpara, listpara)
        self.assertTrue(ret, '新增后检查列表失败')
        #手机端检查列表
        mcheckpara=copy.deepcopy(XsShouYePara.convenienceServiceListCheckPara)
        mcheckpara['title']=resDict['title']
        mcheckpara['linkUrl']=resDict['linkUrl']
        mlistpara= {    
                    'tqmobile':'true',
                    'mobileType':'ios',
                    'apiVersion':'3'
                }   
        ret=XsShouYeIntf.check_convenience_service_list_for_mobile(mcheckpara, mlistpara)
        self.assertTrue(ret, '手机端检查列表错误')
        #关闭操作
        XiTongPeiZhiIntf.close_convenience_service({'ids[]':resDict['id']})
        #PC端检查
        checkpara['state']=ConvenienceState.CLOSE
        ret=XiTongPeiZhiIntf.check_convenience_service_list(checkpara, listpara)
        self.assertTrue(ret, '新增后检查列表失败')
        #手机端检查
        ret=XsShouYeIntf.check_convenience_service_list_for_mobile(mcheckpara, mlistpara)
        self.assertFalse(ret, '手机端检查列表错误')
        Log.LogOutput( message='---------便民服务配置关闭成功！--------')
        #开启操作
        XiTongPeiZhiIntf.open_convenience_service({'ids[]':resDict['id']})
        #PC端检查
        checkpara['state']=ConvenienceState.OPEN
        ret=XiTongPeiZhiIntf.check_convenience_service_list(checkpara, listpara)
        self.assertTrue(ret, '新增后检查列表失败')
        #手机端检查
        ret=XsShouYeIntf.check_convenience_service_list_for_mobile(mcheckpara, mlistpara)
        self.assertTrue(ret, '手机端检查列表错误')
        Log.LogOutput( message='---------便民服务配置开启成功！--------')      
        pass
    
    def testSystemConfig_17(self):
        '''系统配置-便民服务配置-上移、下移、到顶、到底操作-495'''
        #清空所有配置
        XiTongPeiZhiIntf.del_all_convenience_service()
        #新增第一条
        addConvenienceServicePara1=copy.deepcopy(XiTongPeiZhiPara.addConvenienceServicePara)
        addConvenienceServicePara1['convenienceService.title']='第一条便民服务'+createRandomString()
        addConvenienceServicePara1['convenienceService.linkUrl']='http://'+createRandomString()
        files={
               'iosImgValue':open('C:/autotest_file/Tulips.jpg', 'rb'),
               'androidImgValue':open('C:/autotest_file/Penguins.jpg','rb')
               }
        res1=XiTongPeiZhiIntf.add_convenience_service(addConvenienceServicePara1,files=files)
        resDict1=json.loads(res1.text)
        #新增第二条
        addConvenienceServicePara2=copy.deepcopy(XiTongPeiZhiPara.addConvenienceServicePara)
        addConvenienceServicePara2['convenienceService.title']='第二条便民服务'+createRandomString()
        addConvenienceServicePara2['convenienceService.linkUrl']='http://'+createRandomString()
        res2=XiTongPeiZhiIntf.add_convenience_service(addConvenienceServicePara2,files=files)
        resDict2=json.loads(res2.text)
        #新增第三条
        addConvenienceServicePara3=copy.deepcopy(XiTongPeiZhiPara.addConvenienceServicePara)
        addConvenienceServicePara3['convenienceService.title']='第三条便民服务'+createRandomString()
        addConvenienceServicePara3['convenienceService.linkUrl']='http://'+createRandomString()
        res3=XiTongPeiZhiIntf.add_convenience_service(addConvenienceServicePara3,files=files)
        resDict3=json.loads(res3.text)
        listpara=copy.deepcopy(XiTongPeiZhiPara.convenienceServiceListPara)
        XiTongPeiZhiIntf.get_convenience_service_list(listpara)
        seq1=XiTongPeiZhiIntf.get_convenience_service_display_seq_by_title(addConvenienceServicePara1['convenienceService.title'])
        seq2=XiTongPeiZhiIntf.get_convenience_service_display_seq_by_title(addConvenienceServicePara2['convenienceService.title'])
#         print seq1,seq2
        #将第一条数据下移
        movePara=copy.deepcopy(XiTongPeiZhiPara.convenienceServiceMovePara)
        movePara['id']=resDict1['id']
        movePara['referId']=resDict2['id']
        movePara['position']='after'
        XiTongPeiZhiIntf.move_convenience_service(movePara)
        seq11=XiTongPeiZhiIntf.get_convenience_service_display_seq_by_title(addConvenienceServicePara1['convenienceService.title'])
        seq22=XiTongPeiZhiIntf.get_convenience_service_display_seq_by_title(addConvenienceServicePara2['convenienceService.title'])
#         print seq11,seq22
        self.assertEquals(seq1,seq22, '下移验证失败')
        self.assertEquals(seq2, seq11, '下移验证失败')
        Log.LogOutput( message='---------便民服务配置下移成功！--------')
        
        #将原来的第一条数据上移
        movePara['id']=resDict1['id']
        movePara['referId']=resDict2['id']
        movePara['position']='before'
        XiTongPeiZhiIntf.move_convenience_service(movePara)
        seq111=XiTongPeiZhiIntf.get_convenience_service_display_seq_by_title(addConvenienceServicePara1['convenienceService.title'])
        seq222=XiTongPeiZhiIntf.get_convenience_service_display_seq_by_title(addConvenienceServicePara2['convenienceService.title'])
#         print seq111,seq222
        self.assertEquals(seq111,seq22, '上移验证失败')
        self.assertEquals(seq222, seq11, '上移验证失败')
        Log.LogOutput( message='---------便民服务配置上移成功！--------')
        
        #将原来的第一条数据置底
        movePara['id']=resDict1['id']
        movePara['referId']=resDict3['id']
        movePara['position']='last'
        seq333=XiTongPeiZhiIntf.get_convenience_service_display_seq_by_title(addConvenienceServicePara3['convenienceService.title'])
        XiTongPeiZhiIntf.move_convenience_service(movePara)
        seq1111=XiTongPeiZhiIntf.get_convenience_service_display_seq_by_title(addConvenienceServicePara1['convenienceService.title'])
        seq2222=XiTongPeiZhiIntf.get_convenience_service_display_seq_by_title(addConvenienceServicePara2['convenienceService.title'])
        seq3333=XiTongPeiZhiIntf.get_convenience_service_display_seq_by_title(addConvenienceServicePara3['convenienceService.title'])
#         print seq1111,seq2222,seq3333
        self.assertEquals(seq1111,seq333, '置底验证失败')
        self.assertEquals(seq2222, seq222-1, '置底验证失败')
        self.assertEquals(seq3333, seq333-1, '置底验证失败')
        Log.LogOutput( message='---------便民服务配置置底成功！--------')
        
        #将原来的第一条数据置顶
        movePara['id']=resDict1['id']
        movePara['referId']=resDict2['id']
        movePara['position']='first'
        XiTongPeiZhiIntf.move_convenience_service(movePara)
        seq11111=XiTongPeiZhiIntf.get_convenience_service_display_seq_by_title(addConvenienceServicePara1['convenienceService.title'])
        seq22222=XiTongPeiZhiIntf.get_convenience_service_display_seq_by_title(addConvenienceServicePara2['convenienceService.title'])
        seq33333=XiTongPeiZhiIntf.get_convenience_service_display_seq_by_title(addConvenienceServicePara3['convenienceService.title'])
#         print seq11111,seq22222,seq33333
        self.assertEquals(seq11111,seq2222, '置底验证失败')
        self.assertEquals(seq22222, seq2222+1, '置底验证失败')
        self.assertEquals(seq33333, seq3333+1, '置底验证失败')
        Log.LogOutput( message='---------便民服务配置置顶成功！--------')
        pass
        
    def testSystemConfig_18(self):
        '''系统配置-电话分类的新增、修改、删除操作-472'''
        #清空所有分类信息
        XiTongPeiZhiIntf.del_all_mobile_category()
        addMobileCategoryPara=copy.deepcopy(XiTongPeiZhiPara.addMobileCategoryPara)
        addMobileCategoryPara['companyCategory.categoryName']='分类名称'+createRandomString()
        res=XiTongPeiZhiIntf.add_mobile_category(addMobileCategoryPara)
        resDict=json.loads(res.text)
        #检查列表
        checkpara=copy.deepcopy(XiTongPeiZhiPara.mobileCategoryListCheckPara)
        checkpara['id']=resDict['id']
        checkpara['categoryName']=addMobileCategoryPara['companyCategory.categoryName']
        listpara=copy.deepcopy(XiTongPeiZhiPara.mobileCategoryListPara)
        ret=XiTongPeiZhiIntf.check_mobile_category_list(listpara, checkpara)
        self.assertTrue(ret, '电话分类新增验证失败')
        #手机端检查
        mlistpara=copy.deepcopy(XsShouYePara.getMobileCategoryListPara)
        mcheckpara=copy.deepcopy(XsShouYePara.checkMobileCategoryListPara)
        mcheckpara['categoryName']=addMobileCategoryPara['companyCategory.categoryName']
        ret=XsShouYeIntf.check_mobile_category_list_for_mobile(mlistpara, mcheckpara)
        self.assertTrue(ret, '手机端电话分类检查失败')
        Log.LogOutput( message='---------新增电话分类成功！--------')
        
        #修改
        updMobileCategoryPara=copy.deepcopy(XiTongPeiZhiPara.updMobileCategoryPara)
        updMobileCategoryPara['companyCategory.id']=resDict['id']
        updMobileCategoryPara['companyCategory.categoryName']='修改后分类名称'+createRandomString()
        XiTongPeiZhiIntf.upd_mobile_category(updMobileCategoryPara)
        #检查列表
        checkpara['categoryName']=updMobileCategoryPara['companyCategory.categoryName']
        ret=XiTongPeiZhiIntf.check_mobile_category_list(listpara, checkpara)
        self.assertTrue(ret, '电话分类修改验证失败')
        #手机端检查列表
        mcheckpara['categoryName']=updMobileCategoryPara['companyCategory.categoryName']
        ret=XsShouYeIntf.check_mobile_category_list_for_mobile(mlistpara, mcheckpara)
        self.assertTrue(ret, '手机端电话分类检查失败')       
        Log.LogOutput( message='---------修改电话分类成功！--------')
         
        #删除
        ids={'ids[]':resDict['id']}
        XiTongPeiZhiIntf.del_mobile_category(ids)
        #检查列表
        ret=XiTongPeiZhiIntf.check_mobile_category_list(listpara, checkpara)
        self.assertFalse(ret, '电话分类删除验证失败')
        #手机端检查
        ret=XsShouYeIntf.check_mobile_category_list_for_mobile(mlistpara, mcheckpara)
        self.assertFalse(ret, '手机端电话分类检查失败')
        Log.LogOutput( message='---------删除电话分类成功！--------')   
        pass
    
    def testSystemConfig_19(self):
        '''系统配置-电话分类的上移下移、置顶置底操作-474'''
        #清空所有分类信息
        XiTongPeiZhiIntf.del_all_mobile_category()
        #新增第一条电话分类
        addMobileCategoryPara1=copy.deepcopy(XiTongPeiZhiPara.addMobileCategoryPara)
        addMobileCategoryPara1['companyCategory.categoryName']='第一条分类名称'+createRandomString()
        res=XiTongPeiZhiIntf.add_mobile_category(addMobileCategoryPara1)
        resDict1=json.loads(res.text)
        #新增第二条电话分类
        addMobileCategoryPara2=copy.deepcopy(XiTongPeiZhiPara.addMobileCategoryPara)
        addMobileCategoryPara2['companyCategory.categoryName']='第二条分类名称'+createRandomString()
        res=XiTongPeiZhiIntf.add_mobile_category(addMobileCategoryPara2)
        resDict2=json.loads(res.text)        
        #第三条电话分类
        addMobileCategoryPara3=copy.deepcopy(XiTongPeiZhiPara.addMobileCategoryPara)
        addMobileCategoryPara3['companyCategory.categoryName']='第三条分类名称'+createRandomString()
        res=XiTongPeiZhiIntf.add_mobile_category(addMobileCategoryPara3)
        resDict3=json.loads(res.text)
        #将第一条下移
        seq1=XiTongPeiZhiIntf.get_mobile_category_display_seq_by_category_name(addMobileCategoryPara1['companyCategory.categoryName'])
        seq2=XiTongPeiZhiIntf.get_mobile_category_display_seq_by_category_name(addMobileCategoryPara2['companyCategory.categoryName'])
        moveMobileCategoryPara=copy.deepcopy(XiTongPeiZhiPara.moveMobileCategoryPara)
        moveMobileCategoryPara['id']=resDict1['id']
        moveMobileCategoryPara['referId']=resDict2['id']
        moveMobileCategoryPara['position']='after'
        XiTongPeiZhiIntf.move_mobile_category(moveMobileCategoryPara)
        seq11=XiTongPeiZhiIntf.get_mobile_category_display_seq_by_category_name(addMobileCategoryPara1['companyCategory.categoryName'])
        seq22=XiTongPeiZhiIntf.get_mobile_category_display_seq_by_category_name(addMobileCategoryPara2['companyCategory.categoryName'])
        self.assertEqual(seq11, seq2, "下移验证失败")
        self.assertEqual(seq22, seq1, "下移验证失败")
        Log.LogOutput( message='---------电话分类下移成功！--------')
        
        
        #将原来第一条上移
        moveMobileCategoryPara['id']=resDict1['id']
        moveMobileCategoryPara['referId']=resDict2['id']
        moveMobileCategoryPara['position']='before'
        XiTongPeiZhiIntf.move_mobile_category(moveMobileCategoryPara)
        seq111=XiTongPeiZhiIntf.get_mobile_category_display_seq_by_category_name(addMobileCategoryPara1['companyCategory.categoryName'])
        seq222=XiTongPeiZhiIntf.get_mobile_category_display_seq_by_category_name(addMobileCategoryPara2['companyCategory.categoryName'])
        self.assertEqual(seq111, seq22, "上移验证失败")
        self.assertEqual(seq222, seq11, "上移验证失败")
        Log.LogOutput( message='---------电话分类上移成功！--------')
        
        
        #将原来第一条置底
        seq333=XiTongPeiZhiIntf.get_mobile_category_display_seq_by_category_name(addMobileCategoryPara3['companyCategory.categoryName'])
        print seq111,seq222,seq333
        moveMobileCategoryPara['id']=resDict1['id']
        moveMobileCategoryPara['referId']=resDict3['id']
        moveMobileCategoryPara['position']='last'
        XiTongPeiZhiIntf.move_mobile_category(moveMobileCategoryPara)
        seq1111=XiTongPeiZhiIntf.get_mobile_category_display_seq_by_category_name(addMobileCategoryPara1['companyCategory.categoryName'])
        seq2222=XiTongPeiZhiIntf.get_mobile_category_display_seq_by_category_name(addMobileCategoryPara2['companyCategory.categoryName'])
        seq3333=XiTongPeiZhiIntf.get_mobile_category_display_seq_by_category_name(addMobileCategoryPara3['companyCategory.categoryName'])
        print seq1111,seq2222,seq3333
        self.assertEqual(seq1111, seq333, "置底验证失败")
        self.assertEqual(seq2222, seq222-1, "置底验证失败")        
        self.assertEqual(seq3333, seq333-1, "置底验证失败")
        Log.LogOutput( message='---------电话分类置底成功！--------')
        
        #将原来第一条置顶
        moveMobileCategoryPara['id']=resDict1['id']
        moveMobileCategoryPara['referId']=resDict2['id']
        moveMobileCategoryPara['position']='first'
        XiTongPeiZhiIntf.move_mobile_category(moveMobileCategoryPara)
        seq11111=XiTongPeiZhiIntf.get_mobile_category_display_seq_by_category_name(addMobileCategoryPara1['companyCategory.categoryName'])
        seq22222=XiTongPeiZhiIntf.get_mobile_category_display_seq_by_category_name(addMobileCategoryPara2['companyCategory.categoryName'])
        seq33333=XiTongPeiZhiIntf.get_mobile_category_display_seq_by_category_name(addMobileCategoryPara3['companyCategory.categoryName'])
        print seq11111,seq22222,seq33333
        self.assertEqual(seq11111, seq2222, "置顶验证失败")
        self.assertEqual(seq22222, seq2222+1, "置顶验证失败")        
        self.assertEqual(seq33333, seq3333+1, "置顶验证失败")
        Log.LogOutput( message='---------电话分类置顶成功！--------')        
        pass
    
    def testSystemConfig_20(self):
        '''系统配置-电话分类的搜索操作-476'''
        #清空所有分类信息
        XiTongPeiZhiIntf.del_all_mobile_category()
        #新增第一条电话分类
        addMobileCategoryPara1=copy.deepcopy(XiTongPeiZhiPara.addMobileCategoryPara)
        addMobileCategoryPara1['companyCategory.categoryName']='第一条分类名称'+createRandomString()
        res=XiTongPeiZhiIntf.add_mobile_category(addMobileCategoryPara1)
        resDict1=json.loads(res.text)
        #新增第二条电话分类
        addMobileCategoryPara2=copy.deepcopy(XiTongPeiZhiPara.addMobileCategoryPara)
        addMobileCategoryPara2['companyCategory.categoryName']='第二条分类名称'+createRandomString()
        res=XiTongPeiZhiIntf.add_mobile_category(addMobileCategoryPara2)
        resDict2=json.loads(res.text) 
        
        #搜索
        searchpara=copy.deepcopy(XiTongPeiZhiPara.mobileCategoryListPara)
        searchpara['companyCategory.categoryName']=addMobileCategoryPara1['companyCategory.categoryName']
        checkpara1=copy.deepcopy(XiTongPeiZhiPara.mobileCategoryListCheckPara)
        checkpara1['id']=resDict1['id']
        checkpara1['categoryName']=addMobileCategoryPara1['companyCategory.categoryName']
        
        checkpara2=copy.deepcopy(XiTongPeiZhiPara.mobileCategoryListCheckPara)
        checkpara2['id']=resDict2['id']
        checkpara2['categoryName']=addMobileCategoryPara2['companyCategory.categoryName']
        ret=XiTongPeiZhiIntf.check_mobile_category_list(searchpara, checkpara1)
        self.assertTrue(ret, '电话分类搜索验证失败')        
        ret=XiTongPeiZhiIntf.check_mobile_category_list(searchpara, checkpara2)
        self.assertFalse(ret, '电话分类搜索验证失败')
        Log.LogOutput( message='---------电话分类搜索成功！--------')
                
        pass
    
    def testSystemConfig_21(self):
        '''系统配置-电话管理的新增、修改、删除操作-873'''
        #清空所有分类信息
        XiTongPeiZhiIntf.del_all_mobile_category()
        #新增第一条电话分类
        addMobileCategoryPara1=copy.deepcopy(XiTongPeiZhiPara.addMobileCategoryPara)
        addMobileCategoryPara1['companyCategory.categoryName']='第一条分类名称'+createRandomString()
        res=XiTongPeiZhiIntf.add_mobile_category(addMobileCategoryPara1)
        resDict=json.loads(res.text)
        
        #电话管理新增
        addPhonePara=copy.deepcopy(XiTongPeiZhiPara.addPhonePara)
        addPhonePara['companyPhone.companyName']='单位名称'+createRandomString()
        addPhonePara['companyPhone.telePhone']='13000000000'
        addPhonePara['companyPhone.remark']='备注'+createRandomString()
        addPhonePara['companyPhone.companyCategoryId']=resDict['id']
        res2=XiTongPeiZhiIntf.add_mobile(para=addPhonePara)
        res2Dict=json.loads(res2.text)
        #列表检查
        listpara=copy.deepcopy(XiTongPeiZhiPara.phoneListPara)
        listpara['companyPhone.companyCategoryId']=resDict['id']
        checkpara=copy.deepcopy(XiTongPeiZhiPara.phoneListCheckPara)
        checkpara['id']=res2Dict['id']
        checkpara['companyName']=addPhonePara['companyPhone.companyName']
        checkpara['remark']=addPhonePara['companyPhone.remark']
        checkpara['telePhone']=addPhonePara['companyPhone.telePhone']
        ret=XiTongPeiZhiIntf.check_mobile_list(listpara, checkpara)
        self.assertTrue(ret , '新增列表检查失败')
        #手机端
        mlistpara=copy.deepcopy(XsShouYePara.getMobileListPara)
        ret=XsShouYeIntf.check_mobile_list_for_mobile(mlistpara, checkpara)
        self.assertTrue(ret , "手机端列表检查失败")
        Log.LogOutput( message='---------电话管理新增成功！--------')
        
        #修改
        updPhonePara=copy.deepcopy(XiTongPeiZhiPara.updPhonePara)
        updPhonePara['companyPhone.companyName']='单位名称'+createRandomString()
        updPhonePara['companyPhone.telePhone']='13111111111'
        updPhonePara['companyPhone.remark']='备注'+createRandomString()
        updPhonePara['companyPhone.id']=res2Dict['id']
        XiTongPeiZhiIntf.upd_mobile(updPhonePara)
        checkpara['companyName']=updPhonePara['companyPhone.companyName']
        checkpara['remark']=updPhonePara['companyPhone.remark']
        checkpara['telePhone']=updPhonePara['companyPhone.telePhone']
        ret=XiTongPeiZhiIntf.check_mobile_list(listpara, checkpara)
        self.assertTrue(ret , '修改后列表检查失败')
        ret=XsShouYeIntf.check_mobile_list_for_mobile(mlistpara, checkpara)
        self.assertTrue(ret , "修改后手机端列表检查失败")
        Log.LogOutput( message='---------电话管理修改成功！--------')
        
        #删除
        delPara={'ids[]':res2Dict['id'],  'companyCategoryId':resDict['id']}
        XiTongPeiZhiIntf.del_mobile(delPara)
        ret=XiTongPeiZhiIntf.check_mobile_list(listpara, checkpara)
        self.assertFalse(ret , '删除后列表检查失败')
        ret=XsShouYeIntf.check_mobile_list_for_mobile(mlistpara, checkpara)
        self.assertFalse(ret , "删除后手机端列表检查失败")
        Log.LogOutput( message='---------电话管理删除成功！--------')
        pass
    
    def testSystemConfig_22(self):
        '''系统配置-电话管理的上移/下移、到顶/到底操作-874'''
        #清空所有分类信息
        XiTongPeiZhiIntf.del_all_mobile_category()
        #新增第一条电话分类
        addMobileCategoryPara1=copy.deepcopy(XiTongPeiZhiPara.addMobileCategoryPara)
        addMobileCategoryPara1['companyCategory.categoryName']='第一条分类名称'+createRandomString()
        res=XiTongPeiZhiIntf.add_mobile_category(addMobileCategoryPara1)
        resDict=json.loads(res.text)
        categoryId=resDict['id']
        #电话管理新增
        #新增第一条电话
        addPhonePara1=copy.deepcopy(XiTongPeiZhiPara.addPhonePara)
        addPhonePara1['companyPhone.companyName']='第一条单位名称'+createRandomString()
        addPhonePara1['companyPhone.telePhone']='13111111111'
        addPhonePara1['companyPhone.remark']='备注'+createRandomString()
        addPhonePara1['companyPhone.companyCategoryId']=resDict['id']
        res1=XiTongPeiZhiIntf.add_mobile(para=addPhonePara1)
        resDict1=json.loads(res1.text)
        #新增第二条电话
        addPhonePara2=copy.deepcopy(XiTongPeiZhiPara.addPhonePara)
        addPhonePara2['companyPhone.companyName']='第二条单位名称'+createRandomString()
        addPhonePara2['companyPhone.telePhone']='13222222222'
        addPhonePara2['companyPhone.remark']='备注'+createRandomString()
        addPhonePara2['companyPhone.companyCategoryId']=resDict['id']
        res2=XiTongPeiZhiIntf.add_mobile(para=addPhonePara2)
        resDict2=json.loads(res2.text)
        #新增第三条电话
        addPhonePara3=copy.deepcopy(XiTongPeiZhiPara.addPhonePara)
        addPhonePara3['companyPhone.companyName']='第三条单位名称'+createRandomString()
        addPhonePara3['companyPhone.telePhone']='13333333333'
        addPhonePara3['companyPhone.remark']='备注'+createRandomString()
        addPhonePara3['companyPhone.companyCategoryId']=resDict['id']
        res3=XiTongPeiZhiIntf.add_mobile(para=addPhonePara3)
        resDict3=json.loads(res3.text)
        #获取各条数据序号
        seq1=XiTongPeiZhiIntf.get_mobile_display_seq_by_company_name(addPhonePara1['companyPhone.companyName'],categoryId)
        seq2=XiTongPeiZhiIntf.get_mobile_display_seq_by_company_name(addPhonePara2['companyPhone.companyName'],categoryId)
        seq3=XiTongPeiZhiIntf.get_mobile_display_seq_by_company_name(addPhonePara3['companyPhone.companyName'],categoryId)
        print seq1,seq2,seq3
        #将第一条数据下移操作
        moveMobilePara=copy.deepcopy(XiTongPeiZhiPara.moveMobilePara)
        moveMobilePara['id']=resDict1['id']
        moveMobilePara['referId']=resDict2['id']
        moveMobilePara['position']='after'
        XiTongPeiZhiIntf.move_mobile(moveMobilePara)
        seq11=XiTongPeiZhiIntf.get_mobile_display_seq_by_company_name(addPhonePara1['companyPhone.companyName'],categoryId)
        seq22=XiTongPeiZhiIntf.get_mobile_display_seq_by_company_name(addPhonePara2['companyPhone.companyName'],categoryId)
        self.assertEqual(seq11, seq2, "下移验证失败")
        self.assertEqual(seq22, seq1, "下移验证失败")
        #验证手机端序号
        
        mseq11=XsShouYeIntf.get_mobile_display_seq_by_name_for_mobile(addPhonePara1['companyPhone.companyName'])
        mseq22=XsShouYeIntf.get_mobile_display_seq_by_name_for_mobile(addPhonePara2['companyPhone.companyName'])
        print mseq11,mseq22
        self.assertEqual(mseq11, seq11, '手机端下移验证失败')
        self.assertEqual(mseq22, seq22, "手机端下移验证失败")
        Log.LogOutput( message='---------电话下移成功！--------')
        
        #将原第一条数据上移
        moveMobilePara['id']=resDict1['id']
        moveMobilePara['referId']=resDict2['id']
        moveMobilePara['position']='before'
        XiTongPeiZhiIntf.move_mobile(moveMobilePara)
        seq111=XiTongPeiZhiIntf.get_mobile_display_seq_by_company_name(addPhonePara1['companyPhone.companyName'],categoryId)
        seq222=XiTongPeiZhiIntf.get_mobile_display_seq_by_company_name(addPhonePara2['companyPhone.companyName'],categoryId)
        self.assertEqual(seq111, seq22, "上移验证失败")
        self.assertEqual(seq222, seq11, "上移验证失败")
        #手机端验证
        mseq111=XsShouYeIntf.get_mobile_display_seq_by_name_for_mobile(addPhonePara1['companyPhone.companyName'])
        mseq222=XsShouYeIntf.get_mobile_display_seq_by_name_for_mobile(addPhonePara2['companyPhone.companyName'])
        print mseq111,mseq222
        self.assertEqual(mseq111, seq111, '手机端上移验证失败')
        self.assertEqual(mseq222, seq222, "手机端上移验证失败")
        Log.LogOutput( message='---------电话上移成功！--------')
        
        #将第一条数据置底
        seq333=XiTongPeiZhiIntf.get_mobile_display_seq_by_company_name(addPhonePara3['companyPhone.companyName'],categoryId)
        moveMobilePara['id']=resDict1['id']
        moveMobilePara['referId']=resDict3['id']
        moveMobilePara['position']='last'
        XiTongPeiZhiIntf.move_mobile(moveMobilePara)
        seq1111=XiTongPeiZhiIntf.get_mobile_display_seq_by_company_name(addPhonePara1['companyPhone.companyName'],categoryId)
        seq2222=XiTongPeiZhiIntf.get_mobile_display_seq_by_company_name(addPhonePara2['companyPhone.companyName'],categoryId)
        seq3333=XiTongPeiZhiIntf.get_mobile_display_seq_by_company_name(addPhonePara3['companyPhone.companyName'],categoryId)
        self.assertEqual(seq1111, seq333, "置底验证失败")
        self.assertEqual(seq2222, seq222-1, "置底验证失败")
        self.assertEqual(seq3333, seq333-1, "置底验证失败")
        #手机端验证
        mseq1111=XsShouYeIntf.get_mobile_display_seq_by_name_for_mobile(addPhonePara1['companyPhone.companyName'])
        mseq2222=XsShouYeIntf.get_mobile_display_seq_by_name_for_mobile(addPhonePara2['companyPhone.companyName'])
        mseq3333=XsShouYeIntf.get_mobile_display_seq_by_name_for_mobile(addPhonePara3['companyPhone.companyName'])
        print mseq1111,mseq2222,mseq3333
        self.assertEqual(mseq1111, seq1111, '手机端置底验证失败')
        self.assertEqual(mseq2222, seq2222, "手机端置底验证失败")
        self.assertEqual(mseq3333, seq3333, "手机端置底验证失败")
        Log.LogOutput( message='---------电话置底成功！--------')
        
        #将原第一条数据置顶
        moveMobilePara['id']=resDict1['id']
        moveMobilePara['referId']=resDict2['id']
        moveMobilePara['position']='first'
        XiTongPeiZhiIntf.move_mobile(moveMobilePara)
        seq11111=XiTongPeiZhiIntf.get_mobile_display_seq_by_company_name(addPhonePara1['companyPhone.companyName'],categoryId)
        seq22222=XiTongPeiZhiIntf.get_mobile_display_seq_by_company_name(addPhonePara2['companyPhone.companyName'],categoryId)
        seq33333=XiTongPeiZhiIntf.get_mobile_display_seq_by_company_name(addPhonePara3['companyPhone.companyName'],categoryId)
        self.assertEqual(seq11111, seq2222, "置顶验证失败")
        self.assertEqual(seq22222, seq2222+1, "置顶验证失败")
        self.assertEqual(seq33333, seq3333+1, "置顶验证失败")
        #手机端验证
        mseq11111=XsShouYeIntf.get_mobile_display_seq_by_name_for_mobile(addPhonePara1['companyPhone.companyName'])
        mseq22222=XsShouYeIntf.get_mobile_display_seq_by_name_for_mobile(addPhonePara2['companyPhone.companyName'])
        mseq33333=XsShouYeIntf.get_mobile_display_seq_by_name_for_mobile(addPhonePara3['companyPhone.companyName'])
        print mseq11111,mseq22222,mseq33333
        self.assertEqual(mseq11111, seq11111, '手机端置顶验证失败')
        self.assertEqual(mseq22222, seq22222, "手机端置顶验证失败")
        self.assertEqual(mseq33333, seq33333, "手机端置顶验证失败")
        Log.LogOutput( message='---------电话置顶成功！--------')
        pass    
    
    def testSystemConfig_23(self):
        '''系统配置-开通区县操作-496'''
        try:
            operateOrgPara=copy.deepcopy(XiTongPeiZhiPara.operateOrgPara)
            #关闭区县
            XiTongPeiZhiIntf.close_org_state(operateOrgPara)
            #pc端检查开通状态
            listpara=copy.deepcopy(XiTongPeiZhiPara.getOrgOpenStateListPara)
            checkpara=copy.deepcopy(XiTongPeiZhiPara.orgOpenStateListCheckPara)
            checkpara['departmentNo']=InitDefaultPara.clueOrgInit['DftQuOrgDepNo']
            checkpara['openState']=OrgOpenState.CLOSE
            ret=XiTongPeiZhiIntf.check_org_open_state_list(listpara,checkpara)
            self.assertTrue(ret, 'PC端区县关闭状态验证失败')
            #手机端检查开通状态
            mlistpara=copy.deepcopy(XsShouYePara.orgOpenStateListForMobilePara)
            mcheckpara=copy.deepcopy(XsShouYePara.checkOrgOpenStateListForMobilePara)
            mcheckpara['departmentNo']=InitDefaultPara.clueOrgInit['DftQuOrgDepNo']
            mcheckpara['openState']=OrgOpenState.OPEN
            ret=XsShouYeIntf.check_org_open_state_list_for_mobile(mlistpara, mcheckpara)
            self.assertFalse(ret, '手机端区县关闭状态验证失败')
            #开通区县
            XiTongPeiZhiIntf.open_org_state(operateOrgPara)
            #pc端检查开通状态
            checkpara['openState']=OrgOpenState.OPEN
            ret=XiTongPeiZhiIntf.check_org_open_state_list(listpara,checkpara)
            self.assertTrue(ret, 'PC端区县开通状态验证失败')
            #手机端检查开通状态
            mcheckpara['openState']=OrgOpenState.OPEN
            ret=XsShouYeIntf.check_org_open_state_list_for_mobile(mlistpara, mcheckpara)
            self.assertTrue(ret, '手机端区县开通状态验证失败')        
        finally:
            XiTongPeiZhiIntf.open_org_state(operateOrgPara)  
            pass

    def testSystemConfig_24(self):
        '''系统配置-爆料主题新增操作-760'''
        XsBaoLiaoIntf.deleteAllClues()
        #清空爆料主题信息
        if Global.simulationEnvironment is False:
            XiTongPeiZhiIntf.del_all_theme()
        #省级新增爆料主题，默认下辖开放
        addThemePara=copy.deepcopy(XiTongPeiZhiPara.themeAddDict)
        addThemePara['themeContent.name'] = "AUTOTEST_测试主题1"+createRandomString(length=3)
        addThemePara['themeContent.description'] = "测试描述1"+createRandomString()
        res=XiTongPeiZhiIntf.add_theme2(addThemePara)
        resDict=json.loads(res.text)
        checkpara=copy.deepcopy(XiTongPeiZhiPara.themeListCheckPara)
        checkpara['themeContentsId']=resDict['themeContentsId']
        checkpara['infoType']=addThemePara['themeRelation.infoType']
        checkpara['description']=addThemePara['themeContent.description']
        checkpara['name']=addThemePara['themeContent.name']
        checkpara['state']=ThemeState.OPEN
        checkpara['isHotState']=IsHotState.NO
        #默认检查省级列表数据
        listpara=copy.deepcopy(XiTongPeiZhiPara.themeListPara)
        listpara['themeRelation.infoType']=InfoType.BAOLIAO
        ret=XiTongPeiZhiIntf.check_theme_list(listpara, checkpara)
        self.assertTrue(ret , '新增主题PC端检查失败')
        #检查区县列表数据
        listpara['themeRelation.departmentNo']=clueOrgInit['DftQuOrgDepNo']
        ret=XiTongPeiZhiIntf.check_theme_list(listpara, checkpara)
        self.assertTrue(ret , '新增主题PC端检查失败')
        #手机端检查,省级列表检查
        mlistpara=copy.deepcopy(XsGongZuoTaiPara.getThemeContentListPara)
        mlistpara['departmentNo']=clueOrgInit['DftShengOrgDepNo']
        mcheckpara=copy.deepcopy(XsGongZuoTaiPara.themeContentListCheckPara)
        mcheckpara['name']=addThemePara['themeContent.name']
        mcheckpara['description']=addThemePara['themeContent.description']
        mcheckpara['id']=resDict['themeContentsId']
        mcheckpara['isHot']=IsHotState.NO
        ret=XsGongZuoTaiIntf.check_theme_list_for_mobile(listpara=mlistpara, checkpara=mcheckpara)
        self.assertTrue(ret , '新增主题手机端检查失败')
        #区县列表检查
        mlistpara['departmentNo']=clueOrgInit['DftQuOrgDepNo']
        ret=XsGongZuoTaiIntf.check_theme_list_for_mobile(listpara=mlistpara, checkpara=mcheckpara)
        self.assertTrue(ret , '新增主题手机端检查失败')       
        
        #省层级新增一条新数据，辖区不开放
        addThemePara2=copy.deepcopy(XiTongPeiZhiPara.themeAddDict)
        addThemePara2['themeContent.name'] = "AUTOTEST_测试主题1"+createRandomString(length=3)
        addThemePara2['themeContent.description'] = "测试描述1"+createRandomString()
        addThemePara2['themeRelation.openState']=1
        res2=XiTongPeiZhiIntf.add_theme2(addThemePara2)
        resDict2=json.loads(res2.text)
        #区检查参数
        checkpara2=copy.deepcopy(XiTongPeiZhiPara.themeListCheckPara)
        checkpara2['themeContentsId']=resDict2['themeContentsId']
        checkpara2['infoType']=addThemePara2['themeRelation.infoType']
        checkpara2['description']=addThemePara2['themeContent.description']
        checkpara2['name']=addThemePara2['themeContent.name']
        checkpara2['state']=ThemeState.OPEN
        checkpara2['isHotState']=IsHotState.NO
        #默认检查省级列表数据,false
        listpara2=copy.deepcopy(XiTongPeiZhiPara.themeListPara)
        listpara2['themeRelation.infoType']=InfoType.BAOLIAO
        ret=XiTongPeiZhiIntf.check_theme_list(listpara2, checkpara2)
        self.assertTrue(ret , '新增主题PC端检查失败')
        #检查区级列表，false
        listpara2['themeRelation.departmentNo']=clueOrgInit['DftQuOrgDepNo']      
        ret=XiTongPeiZhiIntf.check_theme_list(listpara2, checkpara2)
        self.assertFalse(ret , '新增主题PC端检查失败')
        #手机端检查,省级列表检查,true
        mlistpara2=copy.deepcopy(XsGongZuoTaiPara.getThemeContentListPara)
        mlistpara2['departmentNo']=clueOrgInit['DftShengOrgDepNo']
        mcheckpara2=copy.deepcopy(XsGongZuoTaiPara.themeContentListCheckPara)
        mcheckpara2['name']=addThemePara2['themeContent.name']
        mcheckpara2['description']=addThemePara2['themeContent.description']
        mcheckpara2['id']=resDict2['themeContentsId']
        mcheckpara2['isHot']=IsHotState.NO
        ret=XsGongZuoTaiIntf.check_theme_list_for_mobile(listpara=mlistpara2, checkpara=mcheckpara2)
        self.assertTrue(ret , '新增主题手机端检查失败')
        #手机端检查，区级列表检查,false
        mlistpara2['departmentNo']=clueOrgInit['DftQuOrgDepNo']
        ret=XsGongZuoTaiIntf.check_theme_list_for_mobile(listpara=mlistpara2, checkpara=mcheckpara2)
        self.assertFalse(ret , '新增主题手机端检查失败')        
        Log.LogOutput( message='---------主题新增验证成功！--------')        
        pass    
    
    def testSystemConfig_25(self):
        '''系统配置-爆料主题开启、关闭、编辑、热门操作-761'''
        XsBaoLiaoIntf.deleteAllClues()
        #清空爆料主题信息
        if Global.simulationEnvironment is False:
            XiTongPeiZhiIntf.del_all_theme()
        #新增爆料主题
        addThemePara=copy.deepcopy(XiTongPeiZhiPara.themeAddDict)
        addThemePara['themeContent.name'] = "AUTOTEST_测试主题1"+createRandomString()
        addThemePara['themeContent.description'] = "测试描述1"+createRandomString()
        res=XiTongPeiZhiIntf.add_theme2(addThemePara)
        resDict=json.loads(res.text)
        checkpara=copy.deepcopy(XiTongPeiZhiPara.themeListCheckPara)
        checkpara['themeContentsId']=resDict['themeContentsId']
        checkpara['infoType']=addThemePara['themeRelation.infoType']
        checkpara['description']=addThemePara['themeContent.description']
        checkpara['name']=addThemePara['themeContent.name']
        checkpara['state']=ThemeState.OPEN
        checkpara['isHotState']=IsHotState.NO
        listpara=copy.deepcopy(XiTongPeiZhiPara.themeListPara)
        listpara['themeRelation.infoType']=InfoType.BAOLIAO
        ret=XiTongPeiZhiIntf.check_theme_list(listpara, checkpara)
        self.assertTrue(ret , '新增主题PC端检查失败')
        #手机端检查
        mlistpara=copy.deepcopy(XsGongZuoTaiPara.getThemeContentListPara)
        mcheckpara=copy.deepcopy(XsGongZuoTaiPara.themeContentListCheckPara)
        mcheckpara['name']=addThemePara['themeContent.name']
        mcheckpara['description']=addThemePara['themeContent.description']
        mcheckpara['id']=resDict['themeContentsId']
        mcheckpara['isHot']=IsHotState.NO
        ret=XsGongZuoTaiIntf.check_theme_list_for_mobile(listpara=mlistpara, checkpara=mcheckpara)
        self.assertTrue(ret , '新增主题手机端检查失败')
        Log.LogOutput( message='---------主题新增验证成功！--------')
        
        #关闭
        para= {
                    'themeContentsId':resDict['themeContentsId'],
                    'infoType':InfoType.BAOLIAO#0爆料，5畅聊说说
                    }
        ids=XiTongPeiZhiIntf.get_themeRelationId_by_themeContentsId(para)
        updThemeStatePara=copy.deepcopy(XiTongPeiZhiPara.updThemeStatePara)
        updThemeStatePara['ids[]']=ids
        updThemeStatePara['state']=ThemeState.CLOSE
        XiTongPeiZhiIntf.upd_theme_state(updThemeStatePara)
        #PC端检查状态
        checkpara['state']=ThemeState.CLOSE
        ret=XiTongPeiZhiIntf.check_theme_list(listpara, checkpara)
        self.assertTrue(ret , 'PC端关闭主题检查失败')
        #手机端检查
        ret=XsGongZuoTaiIntf.check_theme_list_for_mobile(listpara=mlistpara, checkpara=mcheckpara)
        self.assertFalse(ret , '新增主题手机端检查失败')        
        Log.LogOutput( message='---------主题关闭验证成功！--------')
        
        #开启主题
        updThemeStatePara['state']=ThemeState.OPEN
        XiTongPeiZhiIntf.upd_theme_state(updThemeStatePara)
        #PC端检查状态
        checkpara['state']=ThemeState.OPEN
        ret=XiTongPeiZhiIntf.check_theme_list(listpara, checkpara)
        self.assertTrue(ret , 'PC端关闭主题检查失败')
        #手机端检查
        ret=XsGongZuoTaiIntf.check_theme_list_for_mobile(listpara=mlistpara, checkpara=mcheckpara)
        self.assertTrue(ret , '新增主题手机端检查失败')
        Log.LogOutput( message='---------主题开启验证成功！--------')
        
        #修改为热门
        updHotStatePara=copy.deepcopy(XiTongPeiZhiPara.updHotStatePara)
        updHotStatePara['ids[]']=ids
        updHotStatePara['isHotState']=IsHotState.YES
        XiTongPeiZhiIntf.upd_hot_state(updHotStatePara)
        #PC端检查状态
        checkpara['isHotState']=IsHotState.YES
        ret=XiTongPeiZhiIntf.check_theme_list(listpara, checkpara)
        self.assertTrue(ret , 'PC端验证热门主题检查失败')
        #手机端检查
        mcheckpara['isHot']=IsHotState.YES
        ret=XsGongZuoTaiIntf.check_theme_list_for_mobile(listpara=mlistpara, checkpara=mcheckpara)
        self.assertTrue(ret , '手机端验证热门主题检查失败') 
        Log.LogOutput( message='---------主题设置热门功能验证成功！--------')
        
        #修改为非热门
        updHotStatePara['isHotState']=IsHotState.NO
        XiTongPeiZhiIntf.upd_hot_state(updHotStatePara)
        #PC端检查状态
        checkpara['isHotState']=IsHotState.NO
        ret=XiTongPeiZhiIntf.check_theme_list(listpara, checkpara)
        self.assertTrue(ret , 'PC端验证热门主题检查失败')
        #手机端检查
        mcheckpara['isHot']=IsHotState.NO
        ret=XsGongZuoTaiIntf.check_theme_list_for_mobile(listpara=mlistpara, checkpara=mcheckpara)
        self.assertTrue(ret , '手机端验证热门主题检查失败')
        Log.LogOutput( message='---------主题设置非热门功能验证成功！--------')
        
        #修改爆料主题
        updThemePara=copy.deepcopy(XiTongPeiZhiPara.themeUpdPara)
        updThemePara['id'] = resDict['themeContentsId']
        updThemePara['name'] = "AUTOTEST_测试主题修改"
        updThemePara['description'] = "测试描述"+createRandomString()
        XiTongPeiZhiIntf.upd_theme(updThemePara)
        checkpara=copy.deepcopy(XiTongPeiZhiPara.themeListCheckPara)
        checkpara['themeContentsId']=updThemePara['id'] 
        checkpara['description']=updThemePara['description']
        checkpara['name']=updThemePara['name']
        listpara=copy.deepcopy(XiTongPeiZhiPara.themeListPara)
        listpara['themeRelation.infoType']=InfoType.BAOLIAO
        ret=XiTongPeiZhiIntf.check_theme_list(listpara, checkpara)
        self.assertTrue(ret , '修改主题PC端检查失败')
        #手机端检查
        mlistpara=copy.deepcopy(XsGongZuoTaiPara.getThemeContentListPara)
        mcheckpara=copy.deepcopy(XsGongZuoTaiPara.themeContentListCheckPara)
        mcheckpara['name']=updThemePara['name']
        mcheckpara['description']=updThemePara['description']
        mcheckpara['id']=updThemePara['id'] 
        ret=XsGongZuoTaiIntf.check_theme_list_for_mobile(listpara=mlistpara, checkpara=mcheckpara)
        self.assertTrue(ret , '修改主题手机端检查失败')
        Log.LogOutput( message='---------主题修改验证成功！--------')               
        pass
    
    def testSystemConfig_26(self):
        '''系统配置-爆料主题上移下移操作-762'''
        XsBaoLiaoIntf.deleteAllClues()
        #清空爆料主题信息
        if Global.simulationEnvironment is False:
            XiTongPeiZhiIntf.del_all_theme()
        #新增第一条爆料主题
        addThemePara1=copy.deepcopy(XiTongPeiZhiPara.themeAddDict)
        addThemePara1['themeContent.name'] = "AUTOTEST_第一条爆料主题"
        addThemePara1['themeContent.description'] = "测试描述"+createRandomString()
#         addThemePara1['themeContent.departmentNo']=InitDefaultPara.xianSuoOrgInit['DftQuOrgIdNo']
#         addThemePara1['themeContent.orgName']=InitDefaultPara.xianSuoOrgInit['DftQuOrg']
        XiTongPeiZhiIntf.add_theme2(addThemePara1)
        #新增第二条爆料主题
        addThemePara2=copy.deepcopy(XiTongPeiZhiPara.themeAddDict)
        addThemePara2['themeContent.name'] = "AUTOTEST_第二条爆料主题"
        addThemePara2['themeContent.description'] = "测试描述"+createRandomString()
#         addThemePara2['themeContent.departmentNo']=InitDefaultPara.xianSuoOrgInit['DftQuOrgIdNo']
#         addThemePara2['themeContent.orgName']=InitDefaultPara.xianSuoOrgInit['DftQuOrg']
        XiTongPeiZhiIntf.add_theme2(addThemePara2)

        #将第一条数据下移
        seq1=XiTongPeiZhiIntf.get_theme_seq_by_name(addThemePara1['themeContent.name'], InfoType.BAOLIAO)
        seq2=XiTongPeiZhiIntf.get_theme_seq_by_name(addThemePara2['themeContent.name'], InfoType.BAOLIAO)
        moveThemePara=copy.deepcopy(XiTongPeiZhiPara.moveThemePara)
        moveThemePara['id']=XiTongPeiZhiIntf.get_theme_id_by_name(addThemePara1['themeContent.name'], InfoType.BAOLIAO)
        moveThemePara['referId']=XiTongPeiZhiIntf.get_theme_id_by_name(addThemePara2['themeContent.name'], InfoType.BAOLIAO)
        moveThemePara['position']='after'
        XiTongPeiZhiIntf.move_theme(moveThemePara)
        #再次获取序列号
        seq11=XiTongPeiZhiIntf.get_theme_seq_by_name(addThemePara1['themeContent.name'], InfoType.BAOLIAO)
        seq22=XiTongPeiZhiIntf.get_theme_seq_by_name(addThemePara2['themeContent.name'], InfoType.BAOLIAO)
        self.assertEqual(seq11, seq2, '主题下移失败')
        self.assertEqual(seq22, seq1, '主题下移失败')
        Log.LogOutput( message='---------主题下移验证成功！--------')
          
        #将第二条数据上移
#         moveThemePara['id']=resDict1['id']
#         moveThemePara['referId']=resDict2['id']
        moveThemePara['position']='before'
        XiTongPeiZhiIntf.move_theme(moveThemePara)
        #再次获取序列号
        seq111=XiTongPeiZhiIntf.get_theme_seq_by_name(addThemePara1['themeContent.name'], InfoType.BAOLIAO)
        seq222=XiTongPeiZhiIntf.get_theme_seq_by_name(addThemePara2['themeContent.name'], InfoType.BAOLIAO)
        self.assertEqual(seq111, seq22, '主题上移失败')
        self.assertEqual(seq222, seq11, '主题上移失败')
        Log.LogOutput( message='---------主题上移验证成功！--------')
              
        pass  
    
    def testSystemConfig_27(self):
        '''系统配置-爆料主题搜索操作-764'''
        XsBaoLiaoIntf.deleteAllClues()
        #清空爆料主题信息
        if Global.simulationEnvironment is False:
            XiTongPeiZhiIntf.del_all_theme()
        #新增第一条爆料主题
        addThemePara1=copy.deepcopy(XiTongPeiZhiPara.themeAddDict)
        addThemePara1['themeContent.name'] = "AUTOTEST_1%s"%createRandomString(5)
        addThemePara1['themeContent.description'] = "测试描述"+createRandomString()
        addThemePara1['themeContent.departmentNo']=InitDefaultPara.clueOrgInit['DftQuOrgDepNo']
        addThemePara1['themeContent.orgName']=InitDefaultPara.clueOrgInit['DftQuOrg']
        res1=XiTongPeiZhiIntf.add_theme2(addThemePara1)
        resDict1=json.loads(res1.text)
        #新增第二条爆料主题
        addThemePara2=copy.deepcopy(XiTongPeiZhiPara.themeAddDict)
        addThemePara2['themeContent.name'] = "AUTOTEST_第二条爆料主题%s"%createRandomString(5)
        addThemePara2['themeContent.description'] = "测试描述"+createRandomString()
        addThemePara2['themeContent.departmentNo']=InitDefaultPara.clueOrgInit['DftQuOrgDepNo']
        addThemePara2['themeContent.orgName']=InitDefaultPara.clueOrgInit['DftQuOrg']
        res2=XiTongPeiZhiIntf.add_theme2(addThemePara2)
        resDict2=json.loads(res2.text)
        #第一条数据检查参数
        checkpara1=copy.deepcopy(XiTongPeiZhiPara.themeListCheckPara)
        checkpara1['themeContentsId']=resDict1['themeContentsId']
        checkpara1['infoType']=addThemePara1['themeRelation.infoType']
        checkpara1['description']=addThemePara1['themeContent.description']
        checkpara1['name']=addThemePara1['themeContent.name']
        checkpara1['state']=ThemeState.OPEN
        checkpara1['isHotState']=IsHotState.NO
        #第二条数据检查参数
        checkpara2=copy.deepcopy(XiTongPeiZhiPara.themeListCheckPara)
        checkpara2['themeContentsId']=resDict2['themeContentsId']
        checkpara2['infoType']=addThemePara2['themeRelation.infoType']
        checkpara2['description']=addThemePara2['themeContent.description']
        checkpara2['name']=addThemePara2['themeContent.name']
        checkpara2['state']=ThemeState.OPEN
        checkpara2['isHotState']=IsHotState.NO
        searchpara=copy.deepcopy(XiTongPeiZhiPara.themeListPara)
        searchpara['themeRelation.infoType']=InfoType.BAOLIAO
        searchpara['themeContent.name']=addThemePara1['themeContent.name']
        ret=XiTongPeiZhiIntf.check_theme_list(searchpara, checkpara1)
        self.assertTrue(ret , '搜索主题检查失败')
        ret=XiTongPeiZhiIntf.check_theme_list(searchpara, checkpara2)
        self.assertFalse(ret , '搜索主题检查失败')
        Log.LogOutput( message='---------主题搜索功能验证成功！--------')
        
        pass

    def testSystemConfig_28(self):
        '''系统配置-畅聊主题新增操作-765'''
        XsBaoLiaoIntf.deleteAllClues()
        #清空畅聊主题信息
        if Global.simulationEnvironment is False:
            XiTongPeiZhiIntf.del_all_theme()
        #省级新增畅聊主题，默认下辖开放
        addThemePara=copy.deepcopy(XiTongPeiZhiPara.themeAddDict)
        addThemePara['themeContent.name'] = "AUTOTEST_测试主题1"+createRandomString()
        addThemePara['themeContent.description'] = "测试描述1"+createRandomString()
        addThemePara['themeRelation.infoType']=InfoType.SHUOSHUO
        res=XiTongPeiZhiIntf.add_theme2(addThemePara)
        resDict=json.loads(res.text)
        checkpara=copy.deepcopy(XiTongPeiZhiPara.themeListCheckPara)
        checkpara['themeContentsId']=resDict['themeContentsId']
        checkpara['infoType']=addThemePara['themeRelation.infoType']
        checkpara['description']=addThemePara['themeContent.description']
        checkpara['name']=addThemePara['themeContent.name']
        checkpara['state']=ThemeState.OPEN
        checkpara['isHotState']=IsHotState.NO
        #默认检查省级列表数据
        listpara=copy.deepcopy(XiTongPeiZhiPara.themeListPara)
        listpara['themeRelation.infoType']=InfoType.SHUOSHUO
        ret=XiTongPeiZhiIntf.check_theme_list(listpara, checkpara)
        self.assertTrue(ret , '新增主题PC端检查失败')
        #检查区县列表数据
        listpara['themeRelation.departmentNo']=clueOrgInit['DftQuOrgDepNo']
        ret=XiTongPeiZhiIntf.check_theme_list(listpara, checkpara)
        self.assertTrue(ret , '新增主题PC端检查失败')
        #手机端检查,省级列表检查
        mlistpara=copy.deepcopy(XsGongZuoTaiPara.getThemeContentListPara)
        mlistpara['departmentNo']=clueOrgInit['DftShengOrgDepNo']
        mlistpara['infoType']=addThemePara['themeRelation.infoType']
        mcheckpara=copy.deepcopy(XsGongZuoTaiPara.themeContentListCheckPara)
        mcheckpara['name']=addThemePara['themeContent.name']
        mcheckpara['description']=addThemePara['themeContent.description']
        mcheckpara['id']=resDict['themeContentsId']
        mcheckpara['isHot']=IsHotState.NO
        ret=XsGongZuoTaiIntf.check_theme_list_for_mobile(listpara=mlistpara, checkpara=mcheckpara)
        self.assertTrue(ret , '新增主题手机端检查失败')
        #区县列表检查
        mlistpara['departmentNo']=clueOrgInit['DftQuOrgDepNo']
        ret=XsGongZuoTaiIntf.check_theme_list_for_mobile(listpara=mlistpara, checkpara=mcheckpara)
        self.assertTrue(ret , '新增主题手机端检查失败')       
        
        #省层级新增一条新数据，辖区不开放
        addThemePara2=copy.deepcopy(XiTongPeiZhiPara.themeAddDict)
        addThemePara2['themeContent.name'] = "AUTOTEST_测试主题1"+createRandomString()
        addThemePara2['themeContent.description'] = "测试描述1"+createRandomString()
        addThemePara2['themeRelation.openState']=1
        addThemePara2['themeRelation.infoType']=InfoType.SHUOSHUO
        res2=XiTongPeiZhiIntf.add_theme2(addThemePara2)
        resDict2=json.loads(res2.text)
        #区检查参数
        checkpara2=copy.deepcopy(XiTongPeiZhiPara.themeListCheckPara)
        checkpara2['themeContentsId']=resDict2['themeContentsId']
        checkpara2['infoType']=addThemePara2['themeRelation.infoType']
        checkpara2['description']=addThemePara2['themeContent.description']
        checkpara2['name']=addThemePara2['themeContent.name']
        checkpara2['state']=ThemeState.OPEN
        checkpara2['isHotState']=IsHotState.NO
        #默认检查省级列表数据,false
        listpara2=copy.deepcopy(XiTongPeiZhiPara.themeListPara)
        listpara2['themeRelation.infoType']=InfoType.SHUOSHUO
        ret=XiTongPeiZhiIntf.check_theme_list(listpara2, checkpara2)
        self.assertTrue(ret , '新增主题PC端检查失败')
        #检查区级列表，false
        listpara2['themeRelation.departmentNo']=clueOrgInit['DftQuOrgDepNo']      
        ret=XiTongPeiZhiIntf.check_theme_list(listpara2, checkpara2)
        self.assertFalse(ret , '新增主题PC端检查失败')
        #手机端检查,省级列表检查,true
        mlistpara2=copy.deepcopy(XsGongZuoTaiPara.getThemeContentListPara)
        mlistpara2['departmentNo']=clueOrgInit['DftShengOrgDepNo']
        mlistpara2['infoType']=addThemePara['themeRelation.infoType']
        mcheckpara2=copy.deepcopy(XsGongZuoTaiPara.themeContentListCheckPara)
        mcheckpara2['name']=addThemePara2['themeContent.name']
        mcheckpara2['description']=addThemePara2['themeContent.description']
        mcheckpara2['id']=resDict2['themeContentsId']
        mcheckpara2['isHot']=IsHotState.NO
        ret=XsGongZuoTaiIntf.check_theme_list_for_mobile(listpara=mlistpara2, checkpara=mcheckpara2)
        self.assertTrue(ret , '新增主题手机端检查失败')
        #手机端检查，区级列表检查,false
        mlistpara2['departmentNo']=clueOrgInit['DftQuOrgDepNo']
        ret=XsGongZuoTaiIntf.check_theme_list_for_mobile(listpara=mlistpara2, checkpara=mcheckpara2)
        self.assertFalse(ret , '新增主题手机端检查失败')        
        Log.LogOutput( message='---------主题新增验证成功！--------')        
        pass
    
    def testSystemConfig_29(self):
        '''系统配置-畅聊主题开启、关闭、热门操作-766'''
        XsBaoLiaoIntf.deleteAllClues()
        #清空爆料主题信息
        if Global.simulationEnvironment is False:
            XiTongPeiZhiIntf.del_all_theme()
        #新增爆料主题
        addThemePara=copy.deepcopy(XiTongPeiZhiPara.themeAddDict)
        addThemePara['themeContent.name'] = "AUTOTEST_测试主题1"+createRandomString()
        addThemePara['themeContent.description'] = "测试描述1"+createRandomString()
        addThemePara['themeRelation.infoType']=InfoType.SHUOSHUO
        res=XiTongPeiZhiIntf.add_theme2(addThemePara)
        resDict=json.loads(res.text)
        checkpara=copy.deepcopy(XiTongPeiZhiPara.themeListCheckPara)
        checkpara['themeContentsId']=resDict['themeContentsId']
        checkpara['infoType']=addThemePara['themeRelation.infoType']
        checkpara['description']=addThemePara['themeContent.description']
        checkpara['name']=addThemePara['themeContent.name']
        checkpara['state']=ThemeState.OPEN
        checkpara['isHotState']=IsHotState.NO
        listpara=copy.deepcopy(XiTongPeiZhiPara.themeListPara)
        ret=XiTongPeiZhiIntf.check_theme_list(listpara, checkpara)
        self.assertTrue(ret , '新增主题PC端检查失败')
        #手机端检查
        mlistpara=copy.deepcopy(XsGongZuoTaiPara.getThemeContentListPara)
        mlistpara['infoType']=addThemePara['themeRelation.infoType']
        mcheckpara=copy.deepcopy(XsGongZuoTaiPara.themeContentListCheckPara)
        mcheckpara['name']=addThemePara['themeContent.name']
        mcheckpara['description']=addThemePara['themeContent.description']
        mcheckpara['id']=resDict['themeContentsId']
        mcheckpara['isHot']=IsHotState.NO
        ret=XsGongZuoTaiIntf.check_theme_list_for_mobile(listpara=mlistpara, checkpara=mcheckpara)
        self.assertTrue(ret , '新增主题手机端检查失败')
        Log.LogOutput( message='---------主题新增验证成功！--------')
        
        #关闭
        para= {
                    'themeContentsId':resDict['themeContentsId'],
                    'infoType':InfoType.SHUOSHUO#0爆料，5畅聊说说
                    }
        ids=XiTongPeiZhiIntf.get_themeRelationId_by_themeContentsId(para)
        updThemeStatePara=copy.deepcopy(XiTongPeiZhiPara.updThemeStatePara)
        updThemeStatePara['ids[]']=ids
        updThemeStatePara['state']=ThemeState.CLOSE
        XiTongPeiZhiIntf.upd_theme_state(updThemeStatePara)
        #PC端检查状态
        checkpara['state']=ThemeState.CLOSE
        ret=XiTongPeiZhiIntf.check_theme_list(listpara, checkpara)
        self.assertTrue(ret , 'PC端关闭主题检查失败')
        #手机端检查
        ret=XsGongZuoTaiIntf.check_theme_list_for_mobile(listpara=mlistpara, checkpara=mcheckpara)
        self.assertFalse(ret , '新增主题手机端检查失败')        
        Log.LogOutput( message='---------主题关闭验证成功！--------')
        
        #开启主题
        updThemeStatePara['state']=ThemeState.OPEN
        XiTongPeiZhiIntf.upd_theme_state(updThemeStatePara)
        #PC端检查状态
        checkpara['state']=ThemeState.OPEN
        ret=XiTongPeiZhiIntf.check_theme_list(listpara, checkpara)
        self.assertTrue(ret , 'PC端关闭主题检查失败')
        #手机端检查
        ret=XsGongZuoTaiIntf.check_theme_list_for_mobile(listpara=mlistpara, checkpara=mcheckpara)
        self.assertTrue(ret , '新增主题手机端检查失败')
        Log.LogOutput( message='---------主题开启验证成功！--------')
        
        #修改为热门
        updHotStatePara=copy.deepcopy(XiTongPeiZhiPara.updHotStatePara)
        updHotStatePara['ids[]']=ids
        updHotStatePara['isHotState']=IsHotState.YES
        XiTongPeiZhiIntf.upd_hot_state(updHotStatePara)
        #PC端检查状态
        checkpara['isHotState']=IsHotState.YES
        ret=XiTongPeiZhiIntf.check_theme_list(listpara, checkpara)
        self.assertTrue(ret , 'PC端验证热门主题检查失败')
        #手机端检查
        mcheckpara['isHot']=IsHotState.YES
        ret=XsGongZuoTaiIntf.check_theme_list_for_mobile(listpara=mlistpara, checkpara=mcheckpara)
        self.assertTrue(ret , '手机端验证热门主题检查失败') 
        Log.LogOutput( message='---------主题设置热门功能验证成功！--------')
        
        #修改为非热门
        updHotStatePara['isHotState']=IsHotState.NO
        XiTongPeiZhiIntf.upd_hot_state(updHotStatePara)
        #PC端检查状态
        checkpara['isHotState']=IsHotState.NO
        ret=XiTongPeiZhiIntf.check_theme_list(listpara, checkpara)
        self.assertTrue(ret , 'PC端验证热门主题检查失败')
        #手机端检查
        mcheckpara['isHot']=IsHotState.NO
        ret=XsGongZuoTaiIntf.check_theme_list_for_mobile(listpara=mlistpara, checkpara=mcheckpara)
        self.assertTrue(ret , '手机端验证热门主题检查失败')
        Log.LogOutput( message='---------主题设置非热门功能验证成功！--------')
        
        #修改爆料主题
        updThemePara=copy.deepcopy(XiTongPeiZhiPara.themeUpdPara)
        updThemePara['id'] = resDict['themeContentsId']
        updThemePara['name'] = "AUTOTEST_测试主题修改"
        updThemePara['description'] = "测试描述"+createRandomString()
        XiTongPeiZhiIntf.upd_theme(updThemePara)
        checkpara=copy.deepcopy(XiTongPeiZhiPara.themeListCheckPara)
        checkpara['themeContentsId']=updThemePara['id'] 
        checkpara['description']=updThemePara['description']
        checkpara['name']=updThemePara['name']
        listpara=copy.deepcopy(XiTongPeiZhiPara.themeListPara)
        listpara['themeRelation.infoType']=InfoType.SHUOSHUO
        ret=XiTongPeiZhiIntf.check_theme_list(listpara, checkpara)
        self.assertTrue(ret , '修改主题PC端检查失败')
        #手机端检查
        mlistpara=copy.deepcopy(XsGongZuoTaiPara.getThemeContentListPara)
        mlistpara['infoType']=InfoType.SHUOSHUO
        mcheckpara=copy.deepcopy(XsGongZuoTaiPara.themeContentListCheckPara)
        mcheckpara['name']=updThemePara['name']
        mcheckpara['description']=updThemePara['description']
        mcheckpara['id']=updThemePara['id'] 
        ret=XsGongZuoTaiIntf.check_theme_list_for_mobile(listpara=mlistpara, checkpara=mcheckpara)
        self.assertTrue(ret , '修改主题手机端检查失败')
        Log.LogOutput( message='---------主题修改验证成功！--------')               
        pass    
    
    def testSystemConfig_30(self):
        '''系统配置-说说主题上移下移操作-767'''
        XsBaoLiaoIntf.deleteAllClues()
        #清空爆料主题信息
        if Global.simulationEnvironment is False:
            XiTongPeiZhiIntf.del_all_theme()
        #新增第一条爆料主题
        addThemePara1=copy.deepcopy(XiTongPeiZhiPara.themeAddDict)
        addThemePara1['themeContent.name'] = "AUTOTEST_第一条说说主题"
        addThemePara1['themeContent.description'] = "测试描述"+createRandomString()
        addThemePara1['themeContent.departmentNo']=InitDefaultPara.clueOrgInit['DftQuOrgDepNo']
        addThemePara1['themeContent.orgName']=InitDefaultPara.clueOrgInit['DftQuOrg']
        addThemePara1['themeRelation.infoType']=InfoType.SHUOSHUO
        res1=XiTongPeiZhiIntf.add_theme2(addThemePara1)
        json.loads(res1.text)
        #新增第二条爆料主题
        addThemePara2=copy.deepcopy(XiTongPeiZhiPara.themeAddDict)
        addThemePara2['themeContent.name'] = "AUTOTEST_第二条说说主题"
        addThemePara2['themeContent.description'] = "测试描述"+createRandomString()
        addThemePara2['themeContent.departmentNo']=InitDefaultPara.clueOrgInit['DftQuOrgDepNo']
        addThemePara2['themeContent.orgName']=InitDefaultPara.clueOrgInit['DftQuOrg']
        addThemePara2['themeRelation.infoType']=InfoType.SHUOSHUO
        XiTongPeiZhiIntf.add_theme2(addThemePara2)

        #将第一条数据下移
        seq1=XiTongPeiZhiIntf.get_theme_seq_by_name(addThemePara1['themeContent.name'], InfoType.SHUOSHUO,departmentNo=InitDefaultPara.clueOrgInit['DftQuOrgDepNo'])
        seq2=XiTongPeiZhiIntf.get_theme_seq_by_name(addThemePara2['themeContent.name'], InfoType.SHUOSHUO,departmentNo=InitDefaultPara.clueOrgInit['DftQuOrgDepNo'])
        print seq1,seq2
        moveThemePara=copy.deepcopy(XiTongPeiZhiPara.moveThemePara)
        moveThemePara['id']=XiTongPeiZhiIntf.get_theme_id_by_name(addThemePara1['themeContent.name'], InfoType.SHUOSHUO)
        moveThemePara['referId']=XiTongPeiZhiIntf.get_theme_id_by_name(addThemePara2['themeContent.name'], InfoType.SHUOSHUO)
        moveThemePara['position']='after'
        XiTongPeiZhiIntf.move_theme(moveThemePara)
        #再次获取序列号
        seq11=XiTongPeiZhiIntf.get_theme_seq_by_name(addThemePara1['themeContent.name'], InfoType.SHUOSHUO,departmentNo=InitDefaultPara.clueOrgInit['DftQuOrgDepNo'])
        seq22=XiTongPeiZhiIntf.get_theme_seq_by_name(addThemePara2['themeContent.name'], InfoType.SHUOSHUO,departmentNo=InitDefaultPara.clueOrgInit['DftQuOrgDepNo'])
        print seq11,seq22
        self.assertEqual(seq11, seq2, '主题下移失败')
        self.assertEqual(seq22, seq1, '主题下移失败')
        Log.LogOutput( message='---------主题下移验证成功！--------')
        
        #将第二条数据上移
#         moveThemePara['id']=resDict1['id']
#         moveThemePara['referId']=resDict2['id']
        moveThemePara['position']='before'
        XiTongPeiZhiIntf.move_theme(moveThemePara)
        #再次获取序列号
        seq111=XiTongPeiZhiIntf.get_theme_seq_by_name(addThemePara1['themeContent.name'], InfoType.SHUOSHUO,departmentNo=InitDefaultPara.clueOrgInit['DftQuOrgDepNo'])
        seq222=XiTongPeiZhiIntf.get_theme_seq_by_name(addThemePara2['themeContent.name'], InfoType.SHUOSHUO,departmentNo=InitDefaultPara.clueOrgInit['DftQuOrgDepNo'])
        self.assertEqual(seq111, seq22, '主题上移失败')
        self.assertEqual(seq222, seq11, '主题上移失败')
        Log.LogOutput( message='---------主题上移验证成功！--------')
        pass 

    def testSystemConfig_31(self):
        '''系统配置-畅聊主题搜索操作-769'''
        XsBaoLiaoIntf.deleteAllClues()
        if Global.simulationEnvironment is False:
            #清空爆料主题信息
            XiTongPeiZhiIntf.del_all_theme()
        #新增第一条爆料主题
        addThemePara1=copy.deepcopy(XiTongPeiZhiPara.themeAddDict)
        addThemePara1['themeContent.name'] = "AUTOTEST_第一条畅聊主题"+createRandomString()
        addThemePara1['themeContent.description'] = "测试描述"+createRandomString()
        addThemePara1['themeContent.departmentNo']=InitDefaultPara.clueOrgInit['DftQuOrgDepNo']
        addThemePara1['themeContent.orgName']=InitDefaultPara.clueOrgInit['DftQuOrg']
        addThemePara1['themeRelation.infoType']=InfoType.SHUOSHUO
        res1=XiTongPeiZhiIntf.add_theme2(addThemePara1)
        resDict1=json.loads(res1.text)
        #新增第二条爆料主题
        addThemePara2=copy.deepcopy(XiTongPeiZhiPara.themeAddDict)
        addThemePara2['themeContent.name'] = "AUTOTEST_第二条畅聊主题"+createRandomString()
        addThemePara2['themeContent.description'] = "测试描述"+createRandomString()
        addThemePara2['themeContent.departmentNo']=InitDefaultPara.clueOrgInit['DftQuOrgDepNo']
        addThemePara2['themeContent.orgName']=InitDefaultPara.clueOrgInit['DftQuOrg']
        addThemePara2['themeRelation.infoType']=InfoType.SHUOSHUO
        res2=XiTongPeiZhiIntf.add_theme2(addThemePara2)
        resDict2=json.loads(res2.text)
        #第一条数据检查参数
        checkpara1=copy.deepcopy(XiTongPeiZhiPara.themeListCheckPara)
        checkpara1['themeContentsId']=resDict1['themeContentsId']
        checkpara1['infoType']=addThemePara1['themeRelation.infoType']
        checkpara1['description']=addThemePara1['themeContent.description']
        checkpara1['name']=addThemePara1['themeContent.name']
        checkpara1['state']=ThemeState.OPEN
        checkpara1['isHotState']=IsHotState.NO
        #第二条数据检查参数
        checkpara2=copy.deepcopy(XiTongPeiZhiPara.themeListCheckPara)
        checkpara2['themeContentsId']=resDict2['themeContentsId']
        checkpara2['infoType']=addThemePara2['themeRelation.infoType']
        checkpara2['description']=addThemePara2['themeContent.description']
        checkpara2['name']=addThemePara2['themeContent.name']
        checkpara2['state']=ThemeState.OPEN
        checkpara2['isHotState']=IsHotState.NO
        searchpara=copy.deepcopy(XiTongPeiZhiPara.themeListPara)
        searchpara['themeRelation.infoType']=InfoType.SHUOSHUO
        searchpara['themeContent.name']=addThemePara1['themeContent.name']
        ret=XiTongPeiZhiIntf.check_theme_list(searchpara, checkpara1)
        self.assertTrue(ret , '搜索主题检查失败')
        ret=XiTongPeiZhiIntf.check_theme_list(searchpara, checkpara2)
        self.assertFalse(ret , '搜索主题检查失败')
        Log.LogOutput( message='---------主题搜索功能验证成功！--------')
        pass

    def testSystemConfig_32(self):
        '''系统配置-轮播图配置新增-770'''
        #清空所有轮播图配置信息
        XiTongPeiZhiIntf.del_all_lunbo()
        XiTongPeiZhiIntf.del_all_operation_notice()
        #新增图片类型的轮播图
        addLunBoPara1=copy.deepcopy(XiTongPeiZhiPara.addLunBoPara)
        addLunBoPara1['eventConfiguration.title']='轮播图_图片'+createRandomString()
        addLunBoPara1['eventConfiguration.description']='轮播图_描述信息'+createRandomString()
        addLunBoPara1['eventConfiguration.jumpType']=JumpType.PICTURE
        files={
               'iosImgUrl':open('C:/autotest_file/Penguins.jpg','rb'),
               'androidImgUrl':open('C:/autotest_file/Penguins.jpg','rb')
               }
        res1=XiTongPeiZhiIntf.add_lunbo(addLunBoPara1, files)
        resDict1=json.loads(res1.text)
        #PC端检查
        checkpara1=copy.deepcopy(XiTongPeiZhiPara.checkLunBoListPara)
        checkpara1['description']=addLunBoPara1['eventConfiguration.description']
        checkpara1['id']=resDict1['id']
        checkpara1['title']=addLunBoPara1['eventConfiguration.title']
        checkpara1['jumpType']=addLunBoPara1['eventConfiguration.jumpType']
        listpara=copy.deepcopy(XiTongPeiZhiPara.getLunBoListPara)
        ret=XiTongPeiZhiIntf.check_lunbo_list(listpara, checkpara1)
        self.assertTrue(ret, 'PC端列表检查失败')
        #手机端检查
        mlistpara={    
                   'tqmobile':'true',
                   'mobileType':'ios',
                    'departmentNo':InitDefaultPara.clueOrgInit['DftQuOrgDepNo'],
                    'apiVersion':3
                }
        #手机端检查参数类似为str，PC端为int
#         checkpara1['jumpType']=str(JumpType.PICTURE)
        ret=XsShouYeIntf.check_lunbo_list_for_mobile(mlistpara,checkpara1)
        self.assertTrue(ret, '手机端列表检查失败')
        
        #新增运维活动公告
        addPara=copy.deepcopy(XiTongPeiZhiPara.yunWeiGongGaoXinZeng)
        addPara['operationNotice.noticeType']=NoticeType.SYSTEM
        addPara['operationNotice.title']='标题'+createRandomString()
        addPara['homePageShow']='on'
        addPara['operationNotice.homePageShow']=HomePageShow.SHOW
        addPara['operationNotice.contentText']='公告内容'+createRandomString()
        addPara['operationNotice.listContentText']='列表显示内容'+createRandomString()
        noticefiles = {
                 'androidImgUrl':open('C:/autotest_file/Tulips.jpg', 'rb'),
                'iosImgUrl':open('C:/autotest_file/Penguins.jpg','rb')
                }                  
        res=XiTongPeiZhiIntf.add_operation_notice(addPara,files=noticefiles)
        self.assertTrue(res.result, "新增失败")
        noticeId=json.loads(res.text)['id']
        #新增运维公告类型的轮播图
        addLunBoPara2=copy.deepcopy(XiTongPeiZhiPara.addLunBoPara)
        addLunBoPara2['eventConfiguration.title']='轮播图_运维公告'+createRandomString()
        addLunBoPara2['eventConfiguration.description']='轮播图_描述信息'+createRandomString()
        addLunBoPara2['eventConfiguration.jumpType']=JumpType.NOTICE
        addLunBoPara2['eventConfiguration.operationNoticeId']=noticeId
        res2=XiTongPeiZhiIntf.add_lunbo(addLunBoPara2, files)
        resDict2=json.loads(res2.text)
        #PC端检查
        checkpara2=copy.deepcopy(XiTongPeiZhiPara.checkLunBoListPara)
        checkpara2['description']=addLunBoPara2['eventConfiguration.description']
        checkpara2['id']=resDict2['id']
        checkpara2['title']=addLunBoPara2['eventConfiguration.title']
        checkpara2['jumpType']=addLunBoPara2['eventConfiguration.jumpType']
        ret=XiTongPeiZhiIntf.check_lunbo_list(listpara, checkpara2)
        self.assertTrue(ret, 'PC端列表检查失败')
        #手机端检查
#         checkpara2['jumpType']=str(JumpType.NOTICE)
        ret=XsShouYeIntf.check_lunbo_list_for_mobile(mlistpara,checkpara2)
        self.assertTrue(ret, '手机端列表检查失败')
                
        #新增html5类型的轮播图
        addLunBoPara3=copy.deepcopy(XiTongPeiZhiPara.addLunBoPara)
        addLunBoPara3['eventConfiguration.title']='轮播图_html5'+createRandomString()
        addLunBoPara3['eventConfiguration.description']='轮播图_描述信息'+createRandomString()
        addLunBoPara3['eventConfiguration.jumpType']=JumpType.HTML5
        addLunBoPara3['eventConfiguration.operationNoticeId']=noticeId
        addLunBoPara3['eventConfiguration.linkUrl']='http://linkUrl'+createRandomString()
        addLunBoPara3['eventConfiguration.shareUrl']='http://shareUrl'+createRandomString()
        res3=XiTongPeiZhiIntf.add_lunbo(addLunBoPara3, files)
        resDict3=json.loads(res3.text)
        #PC端检查
        checkpara3=copy.deepcopy(XiTongPeiZhiPara.checkLunBoListPara)
        checkpara3['description']=addLunBoPara3['eventConfiguration.description']
        checkpara3['id']=resDict3['id']
        checkpara3['title']=addLunBoPara3['eventConfiguration.title']
        checkpara3['jumpType']=addLunBoPara3['eventConfiguration.jumpType']
        checkpara3['shareUrl']=addLunBoPara3['eventConfiguration.shareUrl']
        checkpara3['linkUrl']=addLunBoPara3['eventConfiguration.linkUrl']
        ret=XiTongPeiZhiIntf.check_lunbo_list(listpara, checkpara3)
        self.assertTrue(ret, 'PC端列表检查失败')
        
#         checkpara3['jumpType']=str(JumpType.HTML5)
        ret=XsShouYeIntf.check_lunbo_list_for_mobile(mlistpara,checkpara3)
        self.assertTrue(ret, '手机端列表检查失败')     
        Log.LogOutput( message='---------轮播图新增功能验证成功！--------')  
        pass

    def testSystemConfig_33(self):
        '''系统配置-轮播图配置修改-771'''
        #清空所有轮播图配置信息
        XiTongPeiZhiIntf.del_all_lunbo()
        XiTongPeiZhiIntf.del_all_operation_notice()
        #新增运维活动公告
        addPara1=copy.deepcopy(XiTongPeiZhiPara.yunWeiGongGaoXinZeng)
        addPara1['operationNotice.noticeType']=NoticeType.SYSTEM
        addPara1['operationNotice.title']='第一条标题'+createRandomString()
        addPara1['homePageShow']='on'
        addPara1['operationNotice.homePageShow']=HomePageShow.SHOW
        addPara1['operationNotice.contentText']='公告内容'+createRandomString()
        addPara1['operationNotice.listContentText']='列表显示内容'+createRandomString()
        noticefiles = {
                 'androidImgUrl':open('C:/autotest_file/Tulips.jpg', 'rb'),
                'iosImgUrl':open('C:/autotest_file/Penguins.jpg','rb')
                }                  
        res1=XiTongPeiZhiIntf.add_operation_notice(addPara1,files=noticefiles)
        self.assertTrue(res1.result, "新增失败")
        
        addPara2=copy.deepcopy(XiTongPeiZhiPara.yunWeiGongGaoXinZeng)
        addPara2['operationNotice.noticeType']=NoticeType.SYSTEM
        addPara2['operationNotice.title']='第二条标题'+createRandomString()
        addPara2['homePageShow']='on'
        addPara2['operationNotice.homePageShow']=HomePageShow.SHOW
        addPara2['operationNotice.contentText']='公告内容'+createRandomString()
        addPara2['operationNotice.listContentText']='列表显示内容'+createRandomString()
        res2=XiTongPeiZhiIntf.add_operation_notice(addPara2,files=noticefiles)
        self.assertTrue(res2.result, "新增失败")        
        
        noticeId1=json.loads(res1.text)['id']
        noticeId2=json.loads(res2.text)['id']
        #新增运维公告类型的轮播图
        addLunBoPara=copy.deepcopy(XiTongPeiZhiPara.addLunBoPara)
        addLunBoPara['eventConfiguration.title']='轮播图_运维公告'+createRandomString()
        addLunBoPara['eventConfiguration.description']='轮播图_描述信息'+createRandomString()
        addLunBoPara['eventConfiguration.jumpType']=JumpType.NOTICE
        addLunBoPara['eventConfiguration.operationNoticeId']=noticeId1
        files={
               'iosImgUrl':open('C:/autotest_file/Penguins.jpg','rb'),
               'androidImgUrl':open('C:/autotest_file/Penguins.jpg','rb')
               }
        res=XiTongPeiZhiIntf.add_lunbo(addLunBoPara, files)
        resDict=json.loads(res.text)
        #PC端检查
        checkpara1=copy.deepcopy(XiTongPeiZhiPara.checkLunBoListPara)
        checkpara1['description']=addLunBoPara['eventConfiguration.description']
        checkpara1['id']=resDict['id']
        checkpara1['title']=addLunBoPara['eventConfiguration.title']
        checkpara1['jumpType']=addLunBoPara['eventConfiguration.jumpType']
        listpara=copy.deepcopy(XiTongPeiZhiPara.getLunBoListPara)
        ret=XiTongPeiZhiIntf.check_lunbo_list(listpara, checkpara1)
        self.assertTrue(ret, 'PC端列表检查失败')
        #手机端检查
        mlistpara={    
                   'tqmobile':'true',
                   'mobileType':'ios',
                    'departmentNo':InitDefaultPara.clueOrgInit['DftQuOrgDepNo'],
                    'apiVersion':3
                }
        #手机端该参数类型为str
#         checkpara1['jumpType']=str(addLunBoPara['eventConfiguration.jumpType'])
        ret=XsShouYeIntf.check_lunbo_list_for_mobile(mlistpara,checkpara1)
        self.assertTrue(ret, '手机端列表检查失败')
        #修改
        updLunBoPara=copy.deepcopy(XiTongPeiZhiPara.updLunBoPara)
        updLunBoPara['eventConfiguration.id']=resDict['id']
        updLunBoPara['eventConfiguration.title']='标题修改'
        updLunBoPara['eventConfiguration.description']='描述修改'
        updLunBoPara['eventConfiguration.operationNoticeId']=noticeId2
        XiTongPeiZhiIntf.upd_lunbo(updLunBoPara, files)
        #PC端检查
        checkpara2=copy.deepcopy(XiTongPeiZhiPara.checkLunBoListPara)
        checkpara2['description']=updLunBoPara['eventConfiguration.description']
        checkpara2['id']=resDict['id']
        checkpara2['title']=updLunBoPara['eventConfiguration.title']
        ret=XiTongPeiZhiIntf.check_lunbo_list(listpara, checkpara2)
        self.assertTrue(ret, 'PC端列表检查失败')
        #手机端检查
        ret=XsShouYeIntf.check_lunbo_list_for_mobile(mlistpara,checkpara2)
        self.assertTrue(ret, '手机端列表检查失败') 
        Log.LogOutput( message='---------轮播图修改功能验证成功！--------')     
        pass
    
    def testSystemConfig_34(self):
        '''系统配置-轮播图配置开启、关闭、删除-772'''
        #清空所有轮播图配置信息
        XiTongPeiZhiIntf.del_all_operation_notice()
        #新增图片类型的轮播图
        addLunBoPara1=copy.deepcopy(XiTongPeiZhiPara.addLunBoPara)
        addLunBoPara1['eventConfiguration.title']='轮播图_图片'+createRandomString()
        addLunBoPara1['eventConfiguration.description']='轮播图_描述信息'+createRandomString()
        addLunBoPara1['eventConfiguration.jumpType']=JumpType.PICTURE
        files={
               'iosImgUrl':open('C:/autotest_file/Penguins.jpg','rb'),
               'androidImgUrl':open('C:/autotest_file/Penguins.jpg','rb')
               }
        res=XiTongPeiZhiIntf.add_lunbo(addLunBoPara1, files)
        resDict=json.loads(res.text)
        #PC端检查
        checkpara1=copy.deepcopy(XiTongPeiZhiPara.checkLunBoListPara)
        checkpara1['description']=addLunBoPara1['eventConfiguration.description']
        checkpara1['id']=resDict['id']
        checkpara1['title']=addLunBoPara1['eventConfiguration.title']
        checkpara1['jumpType']=addLunBoPara1['eventConfiguration.jumpType']
        checkpara1['state']=0
        listpara=copy.deepcopy(XiTongPeiZhiPara.getLunBoListPara)
        ret=XiTongPeiZhiIntf.check_lunbo_list(listpara, checkpara1)
        self.assertTrue(ret, 'PC端列表检查失败')
        #手机端检查
        mlistpara={    
                   'tqmobile':'true',
                   'mobileType':'ios',
                    'departmentNo':InitDefaultPara.clueOrgInit['DftQuOrgDepNo'],
                    'apiVersion':3
                }
        mcheckpara=copy.deepcopy(checkpara1)
        #转化检查参数类型为str
#         mcheckpara['jumpType']=str(addLunBoPara1['eventConfiguration.jumpType'])
        
        ret=XsShouYeIntf.check_lunbo_list_for_mobile(mlistpara,mcheckpara)
        self.assertTrue(ret, '手机端列表检查失败')
        #关闭
        XiTongPeiZhiIntf.close_lunbo({'ids[]':resDict['id']})
        checkpara1['state']=1
        ret=XiTongPeiZhiIntf.check_lunbo_list(listpara, checkpara1)
        self.assertTrue(ret, 'PC端列表检查失败')
        ret=XsShouYeIntf.check_lunbo_list_for_mobile(mlistpara,checkpara1)
        self.assertFalse(ret, '手机端列表检查失败')
        Log.LogOutput( message='---------轮播图关闭功能验证成功！--------')
        
        #再次开启
        XiTongPeiZhiIntf.open_lunbo({'ids[]':resDict['id']})
        checkpara1['state']=0
        ret=XiTongPeiZhiIntf.check_lunbo_list(listpara, checkpara1)
        self.assertTrue(ret, 'PC端列表检查失败')
        ret=XsShouYeIntf.check_lunbo_list_for_mobile(mlistpara,mcheckpara)
        self.assertTrue(ret, '手机端列表检查失败')
        Log.LogOutput( message='---------轮播图开启功能验证成功！--------')
        
        #删除
        XiTongPeiZhiIntf.del_lunbo({'ids[]':resDict['id']})
        ret=XiTongPeiZhiIntf.check_lunbo_list(listpara, checkpara1)
        self.assertFalse(ret, 'PC端列表检查失败')
        ret=XsShouYeIntf.check_lunbo_list_for_mobile(mlistpara,mcheckpara)
        self.assertFalse(ret, '手机端列表检查失败')
        Log.LogOutput( message='---------轮播图删除功能验证成功！--------')
        pass
    
    def testSystemConfig_35(self):
        '''系统配置-轮播图配置上移、下移、到顶、到底-773'''
        #清空所有轮播图配置信息
        XiTongPeiZhiIntf.del_all_operation_notice()
        #新增图片类型的轮播图
        addLunBoPara1=copy.deepcopy(XiTongPeiZhiPara.addLunBoPara)
        addLunBoPara1['eventConfiguration.title']='第一条轮播图_图片'+createRandomString()
        addLunBoPara1['eventConfiguration.description']='轮播图_描述信息'+createRandomString()
        addLunBoPara1['eventConfiguration.jumpType']=JumpType.PICTURE
        files={
               'iosImgUrl':open('C:/autotest_file/Penguins.jpg','rb'),
               'androidImgUrl':open('C:/autotest_file/Penguins.jpg','rb')
               }
        res1=XiTongPeiZhiIntf.add_lunbo(addLunBoPara1, files)
        resDict1=json.loads(res1.text)
        
        #新增运维活动公告
        addPara=copy.deepcopy(XiTongPeiZhiPara.yunWeiGongGaoXinZeng)
        addPara['operationNotice.noticeType']=NoticeType.SYSTEM
        addPara['operationNotice.title']='标题'+createRandomString()
        addPara['homePageShow']='on'
        addPara['operationNotice.homePageShow']=HomePageShow.SHOW
        addPara['operationNotice.contentText']='公告内容'+createRandomString()
        addPara['operationNotice.listContentText']='列表显示内容'+createRandomString()
        noticefiles = {
                 'androidImgUrl':open('C:/autotest_file/Tulips.jpg', 'rb'),
                'iosImgUrl':open('C:/autotest_file/Penguins.jpg','rb')
                }                  
        res=XiTongPeiZhiIntf.add_operation_notice(addPara,files=noticefiles)
        self.assertTrue(res.result, "新增失败")
        noticeId=json.loads(res.text)['id']
        #新增运维公告类型的轮播图
        addLunBoPara2=copy.deepcopy(XiTongPeiZhiPara.addLunBoPara)
        addLunBoPara2['eventConfiguration.title']='第二条轮播图_运维公告'+createRandomString()
        addLunBoPara2['eventConfiguration.description']='轮播图_描述信息'+createRandomString()
        addLunBoPara2['eventConfiguration.jumpType']=JumpType.NOTICE
        addLunBoPara2['eventConfiguration.operationNoticeId']=noticeId
        res2=XiTongPeiZhiIntf.add_lunbo(addLunBoPara2, files)
        resDict2=json.loads(res2.text)
                
        #新增html5类型的轮播图
        addLunBoPara3=copy.deepcopy(XiTongPeiZhiPara.addLunBoPara)
        addLunBoPara3['eventConfiguration.title']='第三条轮播图_html5'+createRandomString()
        addLunBoPara3['eventConfiguration.description']='轮播图_描述信息'+createRandomString()
        addLunBoPara3['eventConfiguration.jumpType']=JumpType.HTML5
        addLunBoPara3['eventConfiguration.operationNoticeId']=noticeId
        addLunBoPara3['eventConfiguration.linkUrl']='http://linkUrl'+createRandomString()
        addLunBoPara3['eventConfiguration.shareUrl']='http://shareUrl'+createRandomString()
        res3=XiTongPeiZhiIntf.add_lunbo(addLunBoPara3, files)
        resDict3=json.loads(res3.text)
        
        seq1=XiTongPeiZhiIntf.get_lunbo_seq_by_title(addLunBoPara1['eventConfiguration.title'])
        seq2=XiTongPeiZhiIntf.get_lunbo_seq_by_title(addLunBoPara2['eventConfiguration.title'])
        print seq1,seq2
        #将第一条数据下移
        movePara=copy.deepcopy(XiTongPeiZhiPara.moveLunBoPara)
        movePara['id']=resDict1['id']
        movePara['referId']=resDict2['id']
        movePara['position']='after'
        XiTongPeiZhiIntf.move_lunbo(movePara)
        seq11=XiTongPeiZhiIntf.get_lunbo_seq_by_title(addLunBoPara1['eventConfiguration.title'])
        seq22=XiTongPeiZhiIntf.get_lunbo_seq_by_title(addLunBoPara2['eventConfiguration.title'])
        self.assertEqual(seq11, seq2, '下移失败')
        self.assertEqual(seq22, seq1, '下移失败')
        Log.LogOutput( message='---------轮播图下移功能验证成功！--------')
        
        #将原第一条数据上移
        movePara['position']='before'
        XiTongPeiZhiIntf.move_lunbo(movePara)
        seq111=XiTongPeiZhiIntf.get_lunbo_seq_by_title(addLunBoPara1['eventConfiguration.title'])
        seq222=XiTongPeiZhiIntf.get_lunbo_seq_by_title(addLunBoPara2['eventConfiguration.title'])
        self.assertEqual(seq111, seq22, '上移失败')
        self.assertEqual(seq222, seq11, '上移失败')
        Log.LogOutput( message='---------轮播图上移功能验证成功！--------')
        
        #将第一条数据置底
        seq333=XiTongPeiZhiIntf.get_lunbo_seq_by_title(addLunBoPara3['eventConfiguration.title'])
        movePara['position']='last'
        movePara['referId']=resDict3['id']
        XiTongPeiZhiIntf.move_lunbo(movePara)
        seq1111=XiTongPeiZhiIntf.get_lunbo_seq_by_title(addLunBoPara1['eventConfiguration.title'])
        seq2222=XiTongPeiZhiIntf.get_lunbo_seq_by_title(addLunBoPara2['eventConfiguration.title'])
        seq3333=XiTongPeiZhiIntf.get_lunbo_seq_by_title(addLunBoPara3['eventConfiguration.title'])
        self.assertEqual(seq1111, seq333, '置底失败')
        self.assertEqual(seq2222, seq222-1, '置底失败')
        self.assertEqual(seq3333, seq333-1, '置底失败')
        Log.LogOutput( message='---------轮播图置底功能验证成功！--------')
        
        #将原第一条数据置顶
        movePara['position']='first'
        XiTongPeiZhiIntf.move_lunbo(movePara)
        seq11111=XiTongPeiZhiIntf.get_lunbo_seq_by_title(addLunBoPara1['eventConfiguration.title'])
        seq22222=XiTongPeiZhiIntf.get_lunbo_seq_by_title(addLunBoPara2['eventConfiguration.title'])
        seq33333=XiTongPeiZhiIntf.get_lunbo_seq_by_title(addLunBoPara3['eventConfiguration.title'])
        self.assertEqual(seq11111, seq2222, '置顶失败')
        self.assertEqual(seq22222, seq2222+1, '置顶失败')
        self.assertEqual(seq33333, seq3333+1, '置顶失败')
        Log.LogOutput( message='---------轮播图置顶功能验证成功！--------')        
        pass    

    def tearDown(self):
        pass    
    
    
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(XiTongPeiZhi("testSystemConfig_32"))
#     suite.addTest(XiTingPeiZhi("testPremise_02"))
#     suite.addTest(XiTingPeiZhi("testPremise_03"))
#     suite.addTest(XiTingPeiZhi("testPremise_04"))
#     suite.addTest(XiTingPeiZhi("testPremise_05"))    
    results = unittest.TextTestRunner().run(suite)
    pass    