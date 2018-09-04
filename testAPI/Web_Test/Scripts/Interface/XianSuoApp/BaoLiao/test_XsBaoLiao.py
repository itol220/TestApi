# -*- coding:UTF-8 -*-
'''
Created on 2015-11-24

@author: 
'''
from __future__ import unicode_literals
from COMMON import CommonUtil, Log, Time
from COMMON.CommonUtil import createRandomString
from CONFIG import InitDefaultPara, Global
from CONFIG.InitDefaultPara import orgInit, userInit
from Interface.PingAnJianShe.ShiJianChuLi import ShiJianChuLiPara
from Interface.PingAnJianShe.ShiJianChuLi.ShiJianChuLiIntf import dealIssue
from Interface.PingAnJianShe.SystemMgr import SystemMgrIntf
from Interface.PingAnJianShe.XianSuoGuanLi import XianSuoGuanLiIntf
from Interface.PingAnJianShe.XianSuoGuanLi.XianSuoGuanLiPara import ShowState
from Interface.XianSuoApp.BaoLiao import XsBaoLiaoPara, XsBaoLiaoIntf
from Interface.XianSuoApp.BaoLiao.XsBaoLiaoIntf import deleteAllClues
from Interface.XianSuoApp.BaoLiao.XsBaoLiaoPara import getClueListPara, \
    getClueInMyClueList, wodeliebiaojiancha, addCommentForCluePara, \
    WoDeCommentListPara, checkHighLightPara, delCommentCluePara, \
    getCommentInCluePara, checkCommentInCluePara, WoDeConcernListPara, \
    addPraiseCluePara, xinZeng2
from Interface.XianSuoApp.GongZuoTai import XsGongZuoTaiIntf
from Interface.XianSuoApp.GongZuoTai.XsGongZuoTaiIntf import initUser
from Interface.XianSuoApp.PaiHangBang import XsPaiHangBangIntf
from Interface.XianSuoApp.ShouYe import XsShouYeIntf
from Interface.XianSuoApp.ShouYe.XsShouYePara import gunDongGongGaoJianCha
from Interface.XianSuoApp.XinXiGuangChang import XsInformationSquarePara, \
    XsInformationSquareIntf
from Interface.YunWeiPingTai.XinXiGuanLi import XinXiGuanLiIntf, XinXiGuanLiPara
from Interface.YunWeiPingTai.XinXiGuanLi.XinXiGuanLiPara import InfoType
from Interface.YunWeiPingTai.YunWeiCommon import YunWeiCommonIntf
import copy
import json
import unittest
class XsBaoLiao(unittest.TestCase):
    def setUp(self):
        SystemMgrIntf.initEnv()
        initUser()
        deleteAllClues()
        XinXiGuanLiIntf.deleteyunwei()
        if Global.simulationEnvironment is False:
            XsBaoLiaoIntf.delete_all_comments_by_mobile()
        pass

    def test_XsBaoLiao_01(self):
        """爆料发布主流程-app-232"""
     
        #新增爆料
        #验证爆料必填项
        addBaoLiaoPara=copy.deepcopy(XsBaoLiaoPara.XinZeng)    
        #调用新增爆料的方法
        res1=XsBaoLiaoIntf.addXianSuo(XianSuoDict=addBaoLiaoPara)
        self.assertFalse(res1.result, '新增爆料失败') 
        #填写内容必填项，新增爆料     
        addBaoLiaoPara['information']['contentText'] = '1234S事件描述%s' % CommonUtil.createRandomString()
        addBaoLiaoPara['information']['baiduX'] = '120.4989885463861'
        addBaoLiaoPara['information']['baiduY'] = '30.27759299562879'
        addBaoLiaoPara['information']['x'] = '120.488114380334'
        addBaoLiaoPara['information']['y'] = '30.27759299562879'         
        addBaoLiaoPara['information']['address'] = 'addres%s'%CommonUtil.createRandomString()
        res2=XsBaoLiaoIntf.addXianSuo(XianSuoDict=addBaoLiaoPara)
        self.assertTrue(res2.result, '新增线索失败') 
        #获取广场列表参数
        GuangChangLieBiaopara = copy.deepcopy(getClueListPara)
        GuangChangLieBiaopara['departmentNo']=InitDefaultPara.clueOrgInit['DftQuOrgDepNo']
        #定义广场列表检查参数
        baoliaocheckPara=copy.deepcopy(XsBaoLiaoPara.checkClueInSquarePara)
        userId=XsPaiHangBangIntf.getUserIdByPersonalPoints()
#        print userId
        baoliaocheckPara['contentText']=addBaoLiaoPara['information']['contentText']
        #调用广场列表检查方法
        result2=XsBaoLiaoIntf.check_baoliao_in_list(baoliaocheckPara,GuangChangLieBiaopara)
        self.assertTrue(result2, '检查失败')    
        #获取我的爆料列表参数
        wodebaoliaoliebiaopara = copy.deepcopy(getClueInMyClueList)
        #定义我的爆料列表检查参数
        wodebaoliaocheckpara = copy.deepcopy(wodeliebiaojiancha)
        wodebaoliaocheckpara['contentText']=addBaoLiaoPara['information']['contentText']
#        print      wodebaoliaocheckpara['contentText']
        #调用我的爆料列表检查方法
        result4=XsBaoLiaoIntf.checkClueInMyClue(wodebaoliaocheckpara,wodebaoliaoliebiaopara)
        self.assertTrue(result4, '通过我的爆料检查失败')
        Log.LogOutput(message='通过我的爆料检查成功!')
        #定义运维平台信息管理检查参数
        yunweipingtaipara = copy.deepcopy(XinXiGuanLiPara.jianchaxiansuo)
        yunweipingtaipara['contentText'] = addBaoLiaoPara['information']['contentText']
        yunweipingtaipara['address'] = addBaoLiaoPara['information']['address']
        #调用运维平台信息管理下信息检查的方法，检查爆料在运维平台是否存在
        result3 = XinXiGuanLiIntf.check_clue_in_cluelist_manage(yunweipingtaipara)         
        self.assertTrue(result3, '通过PC线索管理查找失败')
        Log.LogOutput(message='通过PC线索管理查找成功') 
        pass 
       
    def test_XsBaoLiao_02(self):
        """爆料-删除（广场列表、详情；我的评论、我的关注、精彩推荐、消息中心删除）-app-832"""
      
        #新增一条爆料
        addBaoLiaoPara1=copy.deepcopy(XsBaoLiaoPara.XinZeng)
        addBaoLiaoPara1['information']['contentText'] = '测试爆料删除%s'%CommonUtil.createRandomString()
        addBaoLiaoPara1['information']['baiduX'] = '120.4989885463861'
        addBaoLiaoPara1['information']['baiduY'] = '30.27759299562879'
        addBaoLiaoPara1['information']['x'] = '120.488114380334'
        addBaoLiaoPara1['information']['y'] = '30.27759299562879'         
        addBaoLiaoPara1['information']['address'] = 'addres%s'%CommonUtil.createRandomString()
        result=XsBaoLiaoIntf.addXianSuo(XianSuoDict=addBaoLiaoPara1)         
        self.assertTrue(result, '新增线索失败')
        #获取广场列表参数
        GuangChangLieBiaopara = copy.deepcopy(getClueListPara)
        GuangChangLieBiaopara['departmentNo']=InitDefaultPara.clueOrgInit['DftQuOrgDepNo']
        #定义广场列表检查参数
        baoliaocheckPara=copy.deepcopy(XsBaoLiaoPara.checkClueInSquarePara)
        userId=XsPaiHangBangIntf.getUserIdByPersonalPoints()
        print userId
        baoliaocheckPara['contentText']=addBaoLiaoPara1['information']['contentText']
        #调用广场列表检查方法
        result1=XsBaoLiaoIntf.check_baoliao_in_list(baoliaocheckPara,GuangChangLieBiaopara)
        self.assertTrue(result1, '检查失败')
        #获取我的爆料列表参数
        WoDeBaoLiaoLieBiaopara = copy.deepcopy(XsBaoLiaoPara.getClueInMyClueList)
        #定义我的爆料列表检查参数
        wodebaoliaoliebiaopara = copy.deepcopy(XsBaoLiaoPara.wodeliebiaojiancha)
        wodebaoliaoliebiaopara['contentText']=addBaoLiaoPara1['information']['contentText']     
        #调用我的爆料列表检查方法
        result2=XsBaoLiaoIntf.checkClueInMyClue(wodebaoliaoliebiaopara,WoDeBaoLiaoLieBiaopara)
        self.assertTrue(result2, '通过我的爆料检查失败')    
        #运维平台中获取爆料id
        BaoliaoID=XinXiGuanLiIntf.get_clue_id_by_content(addBaoLiaoPara1['information']['contentText'])
#        print BaoliaoID
        #定义新增评论参数，评论爆料
        addpinglunpara=copy.deepcopy(addCommentForCluePara) 
        addpinglunpara['informationId']=BaoliaoID
        addpinglunpara['commentUserId']=userId
        addpinglunpara['contentText']='评论爆料%s'% CommonUtil.createRandomString()
        #调用新增爆料评论的方法，新增评论
        result3=XsBaoLiaoIntf.add_comment_for_clue(addpinglunpara)
        self.assertTrue(result3, '评论爆料失败')  
        #获取我的评论参数
        wodepinglunLieBiaopara = copy.deepcopy(WoDeCommentListPara)
        wodepinglunLieBiaopara['departmentNo']=InitDefaultPara.clueOrgInit['DftQuOrgDepNo']
        
        #定义我的评论列表检查参数
        pingluncheckPara=copy.deepcopy(XsBaoLiaoPara.WoDeCommentListCheckPara)
        pingluncheckPara['contentText']=addpinglunpara['contentText']
        #调用我的评论检查方法
        result4=XsBaoLiaoIntf.check_comment_by_my_comment(pingluncheckPara,wodepinglunLieBiaopara)
        self.assertTrue(result4, '我的评论检查爆料失败')
        #定义关注爆料参数，关注爆料
        addguanzhupara=copy.deepcopy(addCommentForCluePara) 
        addguanzhupara['informationId']=BaoliaoID
        addguanzhupara['concernUserId']=userId
        #调用新增爆料关注的方法，新增关注
        result5=XsBaoLiaoIntf.add_attention_for_clue(addguanzhupara)
        self.assertTrue(result5, '关注爆料失败')
        #获取我的关注参数
        wodeguanzhuLieBiaopara = copy.deepcopy(XsBaoLiaoPara.WoDeConcernListPara)      
        #定义我的关注列表检查参数
        guanzhucheckPara=copy.deepcopy(XsBaoLiaoPara.WoDeConcernListCheckPara)
        guanzhucheckPara['contentText']=addBaoLiaoPara1['information']['contentText']
#        print guanzhucheckPara
        #调用我的关注列表检查方法
        result6=XsBaoLiaoIntf.check_myconcern_list(guanzhucheckPara,wodeguanzhuLieBiaopara)
        self.assertTrue(result6, '我的关注列表检查爆料失败')
        
        #获取爆料id,将爆料设置为精彩推荐
        sheguanbaoliaoID=XianSuoGuanLiIntf.get_clue_id_by_description(addBaoLiaoPara1['information']['contentText'])
#        print sheguanbaoliaoID
        XianSuoGuanLiIntf.set_clue_show_state(sheguanbaoliaoID, ShowState.HIGHLIGHT)
        #定义精彩推荐列表参数
        checkjingcaituijianPara=copy.deepcopy(checkHighLightPara)
        checkjingcaituijianPara['contentText']=addBaoLiaoPara1['information']['contentText']
        #调用精彩推荐列表检查参数
        result7=XsBaoLiaoIntf.check_highlight_info(checkjingcaituijianPara)
        self.assertTrue(result7, '精彩推荐列表检查爆料失败')
        #获取首页轮番公告栏的数据
        gundongpara=copy.deepcopy(gunDongGongGaoJianCha)
        gundongpara['contentText']=addBaoLiaoPara1['information']['contentText']
        #调用首页滚动公告栏检查方法
        result8=XsShouYeIntf.check_scroll_info(gundongpara)
        self.assertFalse(result8, '滚动公告栏检查爆料失败')
        #手机端删除该条爆料
        deletebaoliaopara=copy.deepcopy(XsBaoLiaoPara.ShanChuBaoLiao)
        deletebaoliaopara['id']=BaoliaoID
        result9=XsBaoLiaoIntf.delete_clue(deletebaoliaopara)
        self.assertTrue(result9, '删除爆料失败')
        #获取广场列表参数
        GuangChangLieBiaopara = copy.deepcopy(getClueListPara)
        GuangChangLieBiaopara['departmentNo']=InitDefaultPara.clueOrgInit['DftQuOrgDepNo'] 
        #定义广场列表检查参数
        baoliaocheckPara=copy.deepcopy(XsBaoLiaoPara.checkClueInSquarePara)
        baoliaocheckPara['contentText']=addBaoLiaoPara1['information']['contentText']
        #调用广场列表检查方法
        result10=XsBaoLiaoIntf.check_baoliao_in_list(GuangChangLieBiaopara,baoliaocheckPara)
        self.assertFalse(result10, '广场列表检查爆料失败')
        #获取我的爆料列表参数
        WoDeBaoLiaoLieBiaopara = copy.deepcopy(getClueInMyClueList)
        #定义我的爆料列表检查参数
        wodebaoliaoliebiaopara = copy.deepcopy(wodeliebiaojiancha)
        wodebaoliaoliebiaopara['contentText']=addBaoLiaoPara1['information']['contentText']     
        #调用我的爆料列表检查方法
        result11=XsBaoLiaoIntf.checkClueInMyClue(wodebaoliaoliebiaopara,WoDeBaoLiaoLieBiaopara)
        self.assertFalse(result11, '通过我的爆料检查失败')
        #定义爆料ID获取参数，通过评论内容获取评论id
        commentID=addpinglunpara['informationId']
        CommentContextpara=addpinglunpara['contentText']
        commentID=XsBaoLiaoIntf.get_comment_id_by_content(commentID,CommentContextpara)
#        print commentID
        #定义删除评论参数
        deletecommentpara=copy.deepcopy(delCommentCluePara)
        deletecommentpara['id']=commentID
        #调用删除评论的方法，删除评论
        result7=XsBaoLiaoIntf.delete_comment_for_clue(deletecommentpara)
        self.assertTrue(result7, '删除爆料评论失败')
        #获取我的评论参数
        wodepinglunLieBiaopara = copy.deepcopy(WoDeCommentListPara)
        wodepinglunLieBiaopara['departmentNo']=InitDefaultPara.clueOrgInit['DftQuOrgDepNo'] 
        #定义我的评论列表检查参数
        pingluncheckPara=copy.deepcopy(XsBaoLiaoPara.WoDeCommentListCheckPara)
        pingluncheckPara['contentText']=addBaoLiaoPara1['information']['contentText']
        #调用我的评论检查方法
        result12=XsBaoLiaoIntf.check_comment_by_my_comment(pingluncheckPara,wodepinglunLieBiaopara)
        self.assertFalse(result12, '我的评论检查爆料失败')
        #获取取消关注参数
        concelConcernPara=copy.deepcopy(XsBaoLiaoPara.CancelConcernPara)
        concelConcernPara['informationId']=BaoliaoID
        concelConcernPara['concernUserId']=userId
        #取消关注
        result13=XsBaoLiaoIntf.cancel_Concern_for_clue(concelConcernPara)
        self.assertTrue(result13,'取消关注失败')
        #获取我的关注参数
        wodeguanzhuLieBiaopara = copy.deepcopy(XsBaoLiaoPara.WoDeConcernListPara)      
        #定义我的关注列表检查参数
        guanzhucheckPara=copy.deepcopy(XsBaoLiaoPara.WoDeConcernListCheckPara)
        guanzhucheckPara['contentText']=addBaoLiaoPara1['information']['contentText']
#        print guanzhucheckPara
        #调用我的关注列表检查方法
        result14=XsBaoLiaoIntf.check_myconcern_list(guanzhucheckPara,wodeguanzhuLieBiaopara)
        self.assertFalse(result14, '我的关注列表检查爆料失败')
        #获取精彩推荐参数
#         jingcaituijianpara=copy.deepcopy(getHighLightPara)
        #定义精彩推荐列表参数
        checkjingcaituijianPara=copy.deepcopy(checkHighLightPara)
        checkjingcaituijianPara['contentText']=addBaoLiaoPara1['information']['contentText']
        #调用精彩推荐列表检查参数
        result15=XsBaoLiaoIntf.check_highlight_info(checkjingcaituijianPara)
        self.assertFalse(result15, '精彩推荐列表检查爆料失败')
        #获取首页轮番公告栏的数据
        gundongpara=copy.deepcopy(gunDongGongGaoJianCha)
        gundongpara['contentText']=addBaoLiaoPara1['information']['contentText']
        #调用首页滚动公告栏检查方法
        result16=XsShouYeIntf.check_scroll_info(gundongpara)
        self.assertFalse(result16, '滚动公告栏检查爆料失败')
        pass 
    def test_XsBaoLiao_03(self):
        """爆料评论、点赞、关注-app-830"""
        #新增一条爆料
        addBaoLiaoPara2=copy.deepcopy(XsBaoLiaoPara.XinZeng)
        addBaoLiaoPara2['information']['contentText'] = '1234S事件描述%s' % CommonUtil.createRandomString()
        addBaoLiaoPara2['information']['baiduX'] = '120.4989885463861'
        addBaoLiaoPara2['information']['baiduY'] = '30.27759299562879'
        addBaoLiaoPara2['information']['x'] = '120.488114380334'
        addBaoLiaoPara2['information']['y'] = '30.27759299562879'         
        addBaoLiaoPara2['information']['address'] = 'addres%s'%CommonUtil.createRandomString()
        result=XsBaoLiaoIntf.addXianSuo(XianSuoDict=addBaoLiaoPara2)         
        self.assertTrue(result, '新增线索失败')
        #获取userId
       
        userId=XsPaiHangBangIntf.getUserIdByPersonalPoints()
#        print userId
        #在运维爆料中获取id
        BaoliaoID=XinXiGuanLiIntf.get_clue_id_by_content(addBaoLiaoPara2['information']['contentText'])
#        print BaoliaoID
        #定义新增评论参数，评论爆料
        addpinglunpara1=copy.deepcopy(addCommentForCluePara) 
        addpinglunpara1['informationId']=BaoliaoID
        addpinglunpara1['commentUserId']=userId
        addpinglunpara1['contentText']='评论爆料%s'% CommonUtil.createRandomString()
        #调用新增爆料评论的方法，新增评论
        result2=XsBaoLiaoIntf.add_comment_for_clue(addpinglunpara1)
        self.assertTrue(result2, '评论爆料失败') 
        #获取评论列表参数
        getcommentpara=copy.deepcopy(getCommentInCluePara) 
        getcommentpara['departmentNo']=InitDefaultPara.clueOrgInit['DftQuOrgDepNo'] 
        #在评论列表中检查评论
        checkcommentspara=copy.deepcopy(checkCommentInCluePara)
        checkcommentspara['contentText']=addpinglunpara1['contentText']
        #调用检查评论的方法，在爆料广场检查评论
        result3=XsBaoLiaoIntf.check_comment_in_clue(BaoliaoID,checkcommentspara)
        self.assertTrue(result3, '爆料详情检查爆料评论失败')
        #获取我的评论参数
        wodepinglunLieBiaopara = copy.deepcopy(WoDeCommentListPara)
        wodepinglunLieBiaopara['departmentNo']=InitDefaultPara.clueOrgInit['DftQuOrgDepNo'] 
        #定义我的评论列表检查参数
        pingluncheckPara=copy.deepcopy(XsBaoLiaoPara.WoDeCommentListCheckPara)
        pingluncheckPara['contentText']=addpinglunpara1['contentText']
#        print pingluncheckPara['contentText']
        #调用我的评论检查方法
        result4=XsBaoLiaoIntf.check_comment_by_my_comment(pingluncheckPara,wodepinglunLieBiaopara)
        self.assertTrue(result4, '我的评论检查评论失败')
        #定义回复评论的参数
        ReplyPara=copy.deepcopy(addCommentForCluePara) 
        ReplyPara['informationId']=BaoliaoID
        ReplyPara['replyUserId']=userId
        ReplyPara['commentType']='1'
        ReplyPara['contentText']='回复评论%s'% CommonUtil.createRandomString()
        #定义回复评论列表检查参数
        ReplycheckPara=copy.deepcopy(XsBaoLiaoPara.WoDeCommentListCheckPara)
        ReplycheckPara['contentText']=ReplyPara['contentText']
#        print ReplycheckPara['contentText']
        #调用回复评论的方法，回复评论
        result5=XsBaoLiaoIntf.add_comment_for_clue(ReplyPara)
        self.assertTrue(result5, '回复评论失败') 
        #获取回复评论列表参数
        getReplycommentpara=copy.deepcopy(getCommentInCluePara) 
        getReplycommentpara['departmentNo']=InitDefaultPara.clueOrgInit['DftQuOrgDepNo'] 
        #在评论列表中检查回复评论
        checkReplycommentspara=copy.deepcopy(checkCommentInCluePara)
        checkReplycommentspara['contentText']=ReplyPara['contentText']
        #调用检查回复评论的方法，在爆料广场检查回复
        result6=XsBaoLiaoIntf.check_comment_in_clue(BaoliaoID,checkReplycommentspara)
        self.assertTrue(result6, '爆料详情检查爆料评论失败')
        #获取我的回复评论参数
        wodepinglunLieBiaopara = copy.deepcopy(WoDeCommentListPara)
        wodepinglunLieBiaopara['departmentNo']=InitDefaultPara.clueOrgInit['DftQuOrgDepNo'] 
        #定义我的回复评论列表检查参数
        pingluncheckPara=copy.deepcopy(XsBaoLiaoPara.WoDeCommentListCheckPara)
        pingluncheckPara['contentText']=ReplyPara['contentText']
#        print pingluncheckPara['contentText']
        #调用我的回复评论检查方法
        result7=XsBaoLiaoIntf.check_comment_by_my_comment(pingluncheckPara,wodepinglunLieBiaopara)
        self.assertTrue(result7, '我的评论检查评论失败')
        
        #定义爆料ID获取参数，通过评论内容获取评论id
        commentID=addpinglunpara1['informationId']
        CommentContextpara=addpinglunpara1['contentText']
        commentID=XsBaoLiaoIntf.get_comment_id_by_content(commentID,CommentContextpara)
#        print commentID
        #定义删除评论参数
        deletecommentpara=copy.deepcopy(delCommentCluePara)
        deletecommentpara['id']=commentID
        #调用删除评论的方法，删除评论
        result8=XsBaoLiaoIntf.delete_comment_for_clue(deletecommentpara)
        self.assertTrue(result8, '删除爆料评论失败')
        
        #定义关注爆料参数，关注爆料
        addguanzhupara1=copy.deepcopy(addCommentForCluePara) 
        addguanzhupara1['informationId']=BaoliaoID
        addguanzhupara1['concernUserId']=userId
        #调用新增爆料关注的方法，新增关注
        result9=XsBaoLiaoIntf.add_attention_for_clue(addguanzhupara1)
        self.assertTrue(result9, '关注爆料失败')
        #获取我的关注参数
        wodeguanzhuLieBiaopara1 = copy.deepcopy(WoDeConcernListPara)
        wodeguanzhuLieBiaopara1['departmentNo']=InitDefaultPara.clueOrgInit['DftQuOrgDepNo'] 
        #定义我的关注列表检查参数
        guanzhucheckPara1=copy.deepcopy(XsBaoLiaoPara.WoDeConcernListCheckPara)
        guanzhucheckPara1['contentText']=addBaoLiaoPara2['information']['contentText']
        #调用我的关注列表检查方法
        result10=XsBaoLiaoIntf.check_myconcern_list(guanzhucheckPara1,wodeguanzhuLieBiaopara1)
        self.assertTrue(result10, '我的关注列表检查爆料失败')
        #获取取消关注参数
        concelConcernPara=copy.deepcopy(XsBaoLiaoPara.CancelConcernPara)
        concelConcernPara['informationId']=BaoliaoID
        concelConcernPara['concernUserId']=userId
        #取消关注
        result11=XsBaoLiaoIntf.cancel_Concern_for_clue(concelConcernPara)
        self.assertTrue(result11,'取消关注失败')
        #获取我的关注参数
        wodeguanzhuLieBiaopara = copy.deepcopy(XsBaoLiaoPara.WoDeConcernListPara)      
        #定义我的关注列表检查参数
        guanzhucheckPara=copy.deepcopy(XsBaoLiaoPara.WoDeConcernListCheckPara)
        guanzhucheckPara['contentText']=addBaoLiaoPara2['information']['contentText']
#        print guanzhucheckPara
        
        #调用我的关注列表检查方法
        result12=XsBaoLiaoIntf.check_myconcern_list(guanzhucheckPara,wodeguanzhuLieBiaopara)
        self.assertFalse(result12, '我的关注列表检查爆料失败')
        #定义新增爆料点赞参数，对爆料进行点赞
        addPraisepara=copy.deepcopy(addPraiseCluePara) 
        addPraisepara['informationId']=BaoliaoID
        addPraisepara['praiseUserId']=userId
        #调用新增爆料点赞的方法，点赞爆料
        result13=XsBaoLiaoIntf.add_praise_for_clue(addPraisepara)
        self.assertTrue(result13, '点赞爆料失败')
        #获取点赞用户列表
        getpraiseUserListpara=copy.deepcopy(XsBaoLiaoPara.getPraiseuserlistPara)
        getpraiseUserListpara['informationId']=BaoliaoID
        
       
        
        pass 
         
    def test_XsBaoLiao_04(self):
        """重新提交-app-847"""
        #新增一条爆料
        addBaoLiaoPara=copy.deepcopy(xinZeng2)
        ret=XsBaoLiaoIntf.addXianSuo(XianSuoDict=addBaoLiaoPara)
        self.assertTrue(ret.result, '新增线索失败')
        #不办结事件，直接重新提交，预期false
        resubmintPara=copy.deepcopy(XsBaoLiaoPara.ChongXinTiJiao)
        resubmintPara['contentText']='重新提交内容'+createRandomString()
        resubmintPara['parentInforId']=XsBaoLiaoIntf.get_clue_parentInforId_by_content(addBaoLiaoPara['information']['contentText'])
        ret=XsBaoLiaoIntf.resubmit_clue(para=resubmintPara)
        self.assertFalse(ret.result, '重新提交失败')
        
        #转事件，并办结
        #转事件,街道层级
        listPara={
                'tqmobile':'true',
                'page':'1',
                'rows':'100'
                  }
        lsr=XsBaoLiaoIntf.viewSchedule(para=listPara)
#         print lsr.text
        lsrDict=json.loads(lsr.text)
        addIssuePara=copy.deepcopy(XsInformationSquarePara.culeToIssuePara)
        addIssuePara['information.id']=lsrDict['response']['module']['rows'][0]['information']['id']
        addIssuePara['information.nickName']=lsrDict['response']['module']['rows'][0]['information']['nickName']
        addIssuePara['issue.occurLocation']=lsrDict['response']['module']['rows'][0]['information']['address']
        addIssuePara['issue.issueContent']=lsrDict['response']['module']['rows'][0]['information']['contentText']
        isRes=XsInformationSquareIntf.clueToIssue(para=addIssuePara)
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
        result=dealIssue(issueDict=issuePara,username=userInit['DftJieDaoUser'])
        self.assertTrue(result.result, '办结失败')
        Log.LogOutput( message='事件办结成功')
        #办结后再次重新提交爆料,预期成功
        ret=XsBaoLiaoIntf.resubmit_clue(para=resubmintPara)
        self.assertTrue(ret.result, '重新提交失败')
        #运维管理平台验证重新提交内容
        checkpara={
                'contentText':resubmintPara['contentText'],
                'address':addBaoLiaoPara['information']['address'],
                'reSubmit':2,
                'infoType':InfoType.CLUE
                }
        ret=XinXiGuanLiIntf.check_clue_in_cluelist_manage(clueCheckDict=checkpara)
        self.assertTrue(ret, '线索运维平台信息管理列表验证失败')
        Log.LogOutput( message='---------线索运维平台信息管理列表验证成功！--------')
        #社管线索管理中验证
        ret=XsBaoLiaoIntf.checkxiansuoCompany(companyDict=checkpara)
        self.assertTrue(ret, '社管线索管理列表验证失败')
        Log.LogOutput( message='---------社管线索管理列表验证成功！--------')
        
    def test_XsBaoLiao_05(self):
        '''爆料-举报-836'''
        #删除所有举报记录
        if Global.simulationEnvironment is False:
            XsBaoLiaoIntf.delete_information_reports_by_db()
        try:
            registMobile=XsGongZuoTaiIntf.regist_random_mobile()
            #新注册用户发布一条爆料
            addBaoLiaoPara=copy.deepcopy(XsBaoLiaoPara.xinZeng2)
            result=XsBaoLiaoIntf.addXianSuo(XianSuoDict=addBaoLiaoPara,mobile=registMobile,password=Global.XianSuoDftPassword)         
            self.assertTrue(result.result, '新增线索失败')
            #默认用户举报
            clueId=XinXiGuanLiIntf.get_clue_id_by_content(addBaoLiaoPara['information']['contentText'])
            #针对爆料进行举报
            addClueInfoReportDict = copy.deepcopy(XsBaoLiaoPara.addClueInfoReportPara)
            addClueInfoReportDict['infoId'] = clueId
            addClueInfoReportDict['reportUserId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from USERS t where t.mobile='%s'" % Global.XianSuoDftMobile)
            addClueInfoReportDict['publishUserMobile'] = registMobile
            addClueInfoReportDict['reportType']=None
            ret = XsBaoLiaoIntf.add_clue_information_report(addClueInfoReportDict)
            self.assertFalse(ret, '不选择举报类型情况下，新增线索举报验证失败')
            #选择举报类型
            addClueInfoReportDict['reportType']='99'
            ret = XsBaoLiaoIntf.add_clue_information_report(addClueInfoReportDict)
            self.assertTrue(ret, '新增线索举报验证失败')
            #在后台信息举报列表查看
            getInfoReportDict = copy.deepcopy(XinXiGuanLiPara.getInformationReportPara)
            getInfoReportDict['informationReport.infoType'] = InfoType.CLUE
            getInfoReportDict['informationReport.state'] = 0 #表示未处理
             
            checkInfoReportDict = copy.deepcopy(XinXiGuanLiPara.checkInformationReportPara)
            checkInfoReportDict['contentText'] = addBaoLiaoPara['information']['contentText']
            checkInfoReportDict['address'] = addBaoLiaoPara['information']['address']
             
            ret = XinXiGuanLiIntf.check_information_report_in_list(getInfoReportDict, checkInfoReportDict)
            self.assertTrue(ret, '在举报信息中检查举报失败')
            #获取举报次数参数
            inforPara={
                        'contentText':addBaoLiaoPara['information']['contentText'],
                        'inforType':InfoType.CLUE,#InfoType.CLUE爆料，InfoType.SHUOSHUO说说
                        'state':0#0未处理，1已处理
                    }
            reportCount1=XinXiGuanLiIntf.get_report_count_by_content(inforPara)
            #多次举报
            ret = XsBaoLiaoIntf.add_clue_information_report(addClueInfoReportDict)
            self.assertTrue(ret, '新增线索举报验证失败')
            #多次举报后，后台检查
            ret = XinXiGuanLiIntf.check_information_report_in_list(getInfoReportDict, checkInfoReportDict)
            self.assertTrue(ret, '在举报信息中检查举报失败')
            reportCount2=XinXiGuanLiIntf.get_report_count_by_content(inforPara)
            self.assertEqual(reportCount2, reportCount1+1, '举报次数验证错误')
            Log.LogOutput( message='---------多次举报后，后台举报次数统计功能验证成功！--------')
            #后台删除举报
            XinXiGuanLiIntf.delete_all_information_report(mobile=registMobile)
            ret = XinXiGuanLiIntf.check_information_report_in_list(getInfoReportDict, checkInfoReportDict)
            self.assertFalse(ret, '删除验证失败')
            Log.LogOutput( message='---------举报删除功能验证成功！--------')
            #删除处理后，继续举报，查看后台列表是否会生成，预期不再生成举报信箱
            ret = XsBaoLiaoIntf.add_clue_information_report(addClueInfoReportDict)
            self.assertTrue(ret, '新增线索举报验证失败')
            ret = XinXiGuanLiIntf.check_information_report_in_list(getInfoReportDict, checkInfoReportDict)
            self.assertFalse(ret, '处理举报后再次举报，列表验证失败')
            Log.LogOutput( message='---------处理举报后再次举报,后台不再显示举报信箱，验证成功！--------')
        finally:
            if Global.simulationEnvironment is False:
                XsGongZuoTaiIntf.deleteUserFromDb(mobile=registMobile)                    
        pass
    
    def test_XsBaoLiao_06(self):
        '''爆料-搜索-829'''
        addBaoLiaoPara1=copy.deepcopy(XsBaoLiaoPara.xinZeng2)
        result=XsBaoLiaoIntf.addXianSuo(XianSuoDict=addBaoLiaoPara1)         
        self.assertTrue(result.result, '新增线索失败')
        addBaoLiaoPara2=copy.deepcopy(XsBaoLiaoPara.xinZeng2)
        addBaoLiaoPara2['information']['contentText']='事件描述'+createRandomString()
        result=XsBaoLiaoIntf.addXianSuo(XianSuoDict=addBaoLiaoPara2)
        self.assertTrue(result.result, '新增线索失败')
        searchCluePara=copy.deepcopy(XsBaoLiaoPara.searchCluePara)
        searchCluePara['contentText']=addBaoLiaoPara1['information']['contentText']
        #第一条数据存在查询结果中
        checkpara1=copy.deepcopy(XsBaoLiaoPara.jianchaxiansuo)
        checkpara1['contentText']=addBaoLiaoPara1['information']['contentText']
        checkpara1['address']=addBaoLiaoPara1['information']['address']
        ret=XsBaoLiaoIntf.check_clue_in_search_list(searchCluePara,checkpara1)
        self.assertTrue(ret, '搜索验证失败')
        #第二条数据不存在查询结果中
        checkpara2=copy.deepcopy(XsBaoLiaoPara.jianchaxiansuo)
        checkpara2['contentText']=addBaoLiaoPara2['information']['contentText']
        checkpara2['address']=addBaoLiaoPara2['information']['address']
        ret=XsBaoLiaoIntf.check_clue_in_search_list(searchCluePara,checkpara2)
        self.assertFalse(ret, '搜索验证失败')
        
        pass
    
    def tearDown(self):
        pass    
if __name__ == "__main__":
    suite = unittest.TestSuite()
#     suite.addTest(XsBaoLiao("test_XsBaoLiao_03"))
    suite.addTest(XsBaoLiao("test_XsBaoLiao_05"))
    results = unittest.TextTestRunner().run(suite)
    pass    