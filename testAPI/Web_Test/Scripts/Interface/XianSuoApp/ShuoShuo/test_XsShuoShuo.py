# -*- coding:UTF-8 -*-
'''
Created on 2015-11-24

@author: N-133
'''
from __future__ import unicode_literals
from COMMON import Log, Time
from COMMON.CommonUtil import createRandomString
from CONFIG import Global
from Interface.PingAnJianShe.XianSuoGuanLi import XianSuoGuanLiIntf
from Interface.XianSuoApp.BaoLiao import XsBaoLiaoPara, XsBaoLiaoIntf
from Interface.XianSuoApp.GongZuoTai import XsGongZuoTaiIntf
from Interface.XianSuoApp.GongZuoTai.XsGongZuoTaiIntf import initUser
from Interface.XianSuoApp.JiFenShangCheng.XsJiFenShangChengIntf import \
    createRandomNumber
from Interface.XianSuoApp.PaiHangBang import XsPaiHangBangIntf
from Interface.XianSuoApp.ShuoShuo import ShuoShuoPara, ShuoShuoIntf
from Interface.YunWeiPingTai.XinXiGuanLi import XinXiGuanLiIntf, XinXiGuanLiPara
from Interface.YunWeiPingTai.XinXiGuanLi.XinXiGuanLiPara import InfoType
from Interface.YunWeiPingTai.YunWeiCommon import YunWeiCommonIntf
import copy
import unittest
# from Interface.YunWeiPingTai.XinXiGuanLi import XinXiGuanLiIntf




class XsShuoShuo(unittest.TestCase):

    def setUp(self):
        XsGongZuoTaiIntf.initUser()
        XianSuoGuanLiIntf.delete_all_shuoshuo()
#         SystemMgrIntf.initEnv()''
        pass
    
#     新增线索
    def test_XsShuoShuo_01(self):
        """新增说说-app-828"""
        addShouShou=copy.deepcopy(ShuoShuoPara.addShuoShuoPara)
        #验证内容必填项，不填返回错误信息
        res1=ShuoShuoIntf.add_shuoshuo(addShouShou)
        self.assertFalse(res1, '未输入说说内容仍新增说说成功')
        #填写内容必填项，返回正确结果
        addShouShou['casualTalk']['contentText']='ShouShouAddTestContent%s'%createRandomString()
        addShouShou['casualTalk']['title']='ShouShouAddTestTitle%s'%createRandomString()
        res2=ShuoShuoIntf.add_shuoshuo(addShouShou)
        self.assertTrue(res2, '新增说说失败')
        #说说新增成功后在广场列表进行检查
        #定义列表参数 
        userId=XsPaiHangBangIntf.getUserIdByPersonalPoints()       
        getSquareListPara=copy.deepcopy(ShuoShuoPara.getShuoShuoPara)
        getSquareListPara['userId']=userId
        #定义广场列表检查参数
        checkSquareListPara=copy.deepcopy(ShuoShuoPara.checkShuoShuoPara)
        checkSquareListPara['contentText']=addShouShou['casualTalk']['contentText']
        checkSquareListPara['showState']=0#0表示公开，1表示CLOSE
        #调用检查方法
        result2=ShuoShuoIntf.check_shuoshuo_in_list(checkSquareListPara, getSquareListPara)
        self.assertTrue(result2, '广场列表查找说说失败')
        #在我的说说列表进行检查
        #定义我的列表参数
        MyListPara=copy.deepcopy(ShuoShuoPara.WoDeShouShouLieBiao)
        #定义我的列表检查参数
        checkMyListPara=copy.deepcopy(ShuoShuoPara.WoDeShuoShuoLieBiaoJianCha)
        checkMyListPara['contentText']=addShouShou['casualTalk']['contentText']
        checkMyListPara['title']=addShouShou['casualTalk']['title']
        checkMyListPara['showState']=0#0表示公开，1表示CLOSE
        #调用检查方法
        result3=ShuoShuoIntf.check_shuoshuo_my_list(checkMyListPara, MyListPara)
        self.assertTrue(result3, '我的说说列表查找说说失败')
        #在后台进行检查
        #定义运维平台随便说说列表参数
        getShouShouYunWeiList=copy.deepcopy(XinXiGuanLiPara.getShuoShuoListPara)
        getShouShouYunWeiList['mobile']=Global.XianSuoDftMobile
        #定义运维平台随便说说列表检查参数
        checkShouShouYunWeiList=copy.deepcopy(XinXiGuanLiPara.checkShuoShuoPara)
        checkShouShouYunWeiList['contentText']=addShouShou['casualTalk']['contentText']
        checkShouShouYunWeiList['title']=addShouShou['casualTalk']['title']
        result4=XinXiGuanLiIntf.check_shuoshuo_in_list(checkShouShouYunWeiList,getShouShouYunWeiList)
        self.assertTrue(result4, '运维后台随便说说列表查找说说失败')
 
        pass 
    
#删除说说
    def test_XsShuoShuo_02(self):
        """删除说说-app-837"""
        #新增说说
        addShouShou=copy.deepcopy(ShuoShuoPara.addShuoShuoPara)
        addShouShou['casualTalk']['contentText']='删除说说测试内容%s'%createRandomString()
        addShouShou['casualTalk']['title']='删除测试标题%s'%createRandomString()
        res1=ShuoShuoIntf.add_shuoshuo(addShouShou)
        self.assertTrue(res1, '说说新增成功')
        #新增成功后，在广场列表进行查看
        #定义广场列表参数 
        userId=XsPaiHangBangIntf.getUserIdByPersonalPoints()       
        getSquareListPara=copy.deepcopy(ShuoShuoPara.getShuoShuoPara)
        getSquareListPara['userId']=userId
        #调用通过说说内容获取说说id的方法
        ShouShouId=ShuoShuoIntf.get_shuoshuo_id_by_content(shuoshuoContent=addShouShou['casualTalk']['contentText'], squarelistpara=getSquareListPara)
        #定义广场列表检查参数
        checkSquareListPara1=copy.deepcopy(ShuoShuoPara.checkShuoShuoPara)
        checkSquareListPara1['contentText']=addShouShou['casualTalk']['contentText']
        checkSquareListPara1['title']=addShouShou['casualTalk']['title']
        checkSquareListPara1['showState']=0#0表示公开，1表示CLOSE
        #调用广场列表检查方法
        res2=ShuoShuoIntf.check_shuoshuo_in_list(checkSquareListPara1, getSquareListPara)
        self.assertTrue(res2, '广场列表检查失败')
        #对说说进行关注操作
        #定义关注参数
        addConcernPara=copy.deepcopy(ShuoShuoPara.ShouShouAddConcernPara)
        addConcernPara['informationId']=ShouShouId
        addConcernPara['concernUserId']=userId
        addConcernPara['concernDate']=Time.getCurrentDateAndTime()
        #调用说说新增关注方法
        res3=ShuoShuoIntf.addconcern_shuoshuo(addConcernPara)
        self.assertTrue(res3, '说说新增关注失败')
        #对说说进行评论操作
        #定义评论参数
        addCommentPara=copy.deepcopy(ShuoShuoPara.addCommentForShuoShuoPara)
        addCommentPara['informationId']=ShouShouId
        addCommentPara['contentText']='说说评论内容%s'%createRandomString()
        addCommentPara['commentUserId']=userId
        addCommentPara['commentType']=0#评论类型：0--评论；1--回复评论
        #调用说说添加评论方法
        res4=ShuoShuoIntf.add_comment_for_shuoshuo(addCommentPara)
        self.assertTrue(res4, '说说添加评论失败')
        #将说说置为精彩推荐
        res5=XinXiGuanLiIntf.set_shuoshuo_to_highlight(ShouShouId)
        self.assertTrue(res5, '说说设为精彩推荐失败')
        #说说新增成功且添加评论、关注、设为精彩推荐后，删除说说
        deleteShouShouPara=copy.deepcopy(ShuoShuoPara.delShuoShuoPara)
        deleteShouShouPara['id']=ShouShouId
        res6=ShuoShuoIntf.delete_shuoshuo(deleteShouShouPara)
        self.assertTrue(res6, '删除说说失败')
        #说说删除成功后，在广场列表进行检查
        #定义广场列表检查参数
        checkSquareListPara2=copy.deepcopy(ShuoShuoPara.checkShuoShuoPara)
        checkSquareListPara2['contentText']=addShouShou['casualTalk']['contentText']
        checkSquareListPara2['title']=addShouShou['casualTalk']['title']
        checkSquareListPara2['showState']=0#0表示公开，1表示CLOSE
        #调用广场列表检查方法
        res7=ShuoShuoIntf.check_shuoshuo_in_list(checkSquareListPara2, getSquareListPara)
        self.assertFalse(res7, '广场列表检查失败')
        #说说删除成功后，在我的说说列表进行查看
        #定义我的说说列表参数
        getMyListPara=copy.deepcopy(ShuoShuoPara.WoDeShouShouLieBiao)
        #定义我的说说列表检查参数
        checkMyListPara=copy.deepcopy(ShuoShuoPara.WoDeShuoShuoLieBiaoJianCha)
        checkMyListPara['contentText']=addShouShou['casualTalk']['contentText']
        checkMyListPara['title']=addShouShou['casualTalk']['title']
        checkMyListPara['showState']=0#0表示公开，1表示CLOSE
        #调用我的说说列表检查方法
        res8=ShuoShuoIntf.check_shuoshuo_my_list(checkMyListPara, getMyListPara)
        self.assertFalse(res8, '我的说说列表检查失败') 
        #说说删除成功后，在我的关注列表进行检查
        #定义我的关注列表参数
        getMyConcernList=copy.deepcopy(ShuoShuoPara.WoDeConcernListPara)
        #定义我的关注列表检查参数
        checkMyConcernListPara=copy.deepcopy(ShuoShuoPara.WoDeConcernListCheckPara)
        checkMyConcernListPara['contentText']=addShouShou['casualTalk']['contentText']
        checkMyConcernListPara['delState']=1
        #调用我的关注列表检查方法
        res9=ShuoShuoIntf.check_myconcern_list(checkMyConcernListPara, getMyConcernList)
        self.assertTrue(res9,'我的关注列表检查失败')
        #说说删除成功后，在我的评论列表进行检查
        #定义我的评论列表参数
        getMyCommentListPara=copy.deepcopy(ShuoShuoPara.getMyCommentListPara)
        #定义我的评论列表检查参数
        checkMyCommentListPara=copy.deepcopy(ShuoShuoPara.checkMyCommentListPara)
        checkMyCommentListPara['contentText']=addCommentPara['contentText']
        checkMyCommentListPara['inforDelState']=1
        checkMyCommentListPara['inforContent']=addShouShou['casualTalk']['contentText']
        #调用我的评论列表检查方法
        result1=ShuoShuoIntf.check_comment_by_my_comment(checkMyCommentListPara, getMyCommentListPara)
        self.assertTrue(result1,'我的评论列表检查失败')
        #说说删除成功后，在精彩推荐列表进行检查
        #定义精彩推荐列表检查方法
        checkWonderfulRecommendPara=copy.deepcopy(XsBaoLiaoPara.checkHighLightPara)
        checkWonderfulRecommendPara['contentText']=addShouShou['casualTalk']['contentText']
        checkWonderfulRecommendPara['infoType']=5#0表示爆料，5表示说说
        checkWonderfulRecommendPara['publishUserId']=XsPaiHangBangIntf.getUserIdByPersonalPoints()
        #调用精彩推荐列表检查方法
        result2=XsBaoLiaoIntf.check_highlight_info(checkWonderfulRecommendPara)
        self.assertFalse(result2,'精彩推荐列表检查失败')
        
#说说评论点赞
    def test_XsShuoShuo_03(self):
        """说说评论点赞-app-843"""
        #新增说说
        addShouShou=copy.deepcopy(ShuoShuoPara.addShuoShuoPara)
        addShouShou['casualTalk']['contentText']='说说评论点赞测试内容%s'%createRandomString()
        addShouShou['casualTalk']['title']='说说评论点赞测试标题%s'%createRandomString()
        ShuoShuoIntf.add_shuoshuo(addShuoShuoPara=addShouShou)
        #对新增说说进行检查
        #定义广场说说列表参数
        userId=XsPaiHangBangIntf.getUserIdByPersonalPoints()
        getSquareListPara=copy.deepcopy(ShuoShuoPara.getShuoShuoPara)
        getSquareListPara['userId']=userId
        #定义广场列表检查参数
        checkSquareListPara=copy.deepcopy(ShuoShuoPara.checkShuoShuoPara)
        checkSquareListPara['contentText']=addShouShou['casualTalk']['contentText']
        checkSquareListPara['showState']=0#0表示公开，1表示CLOSE
        #调用检查方法
        result=ShuoShuoIntf.check_shuoshuo_in_list(checkSquareListPara, getSquareListPara)
        self.assertTrue(result, '说说新增失败')
        #调用通过说说内容获取说说id的方法来获取说说id
        ShouShouId=ShuoShuoIntf.get_shuoshuo_id_by_content(addShouShou['casualTalk']['contentText'], squarelistpara=getSquareListPara)
        #未输入评论内容，直接点击评论按钮
        addCommentPara=copy.deepcopy(ShuoShuoPara.addCommentForShuoShuoPara)
        addCommentPara['informationId']=ShouShouId
        addCommentPara['commentUserId']=userId
        addCommentPara['contentText']=""
        addCommentPara['commentType']=0#评论类型：0--评论；1--回复
        res1=ShuoShuoIntf.add_comment_for_shuoshuo(addCommentPara)
        self.assertFalse(res1, '评论内容为空评论成功！')
        #输入评论内容，点击评论按钮
        addCommentPara['contentText']='说说添加评论%s'%createRandomString()
        res2=ShuoShuoIntf.add_comment_for_shuoshuo(addCommentPara)
        self.assertTrue(res2, '说说添加评论失败')
        #在说说详情界面进行查看
        checkCommentInShouShou1=copy.deepcopy(ShuoShuoPara.checkCommentInShuoShuoPara)
        checkCommentInShouShou1['contentText']=addCommentPara['contentText']
        res3=ShuoShuoIntf.check_comment_in_shuoshuo(ShouShouId,checkCommentInShouShou1)
        self.assertTrue(res3, '说说详情检查评论成功')
        #评论添加成功后，在我的评论界面查看
        #定义我的评论列表参数
        getMyCommentListPara=copy.deepcopy(ShuoShuoPara.getMyCommentListPara)
        #定义我的评论列表检查参数
        checkMyCommentPara=copy.deepcopy(ShuoShuoPara.checkMyCommentListPara)
        checkMyCommentPara['contentText']=addCommentPara['contentText']
        checkMyCommentPara['inforContent']=addShouShou['casualTalk']['contentText']
        #调用我的评论列表检查方法
        res4=ShuoShuoIntf.check_comment_by_my_comment(checkMyCommentPara,getMyCommentListPara)
        self.assertTrue(res4, '我的评论列表检查失败')
        #验证回复评论功能并在说说详情进行查看
        #对说说的评论进行回复评论
        addReplyCommentPara=copy.deepcopy(ShuoShuoPara.addCommentForShuoShuoPara)
        addReplyCommentPara['informationId']=ShouShouId
        addReplyCommentPara['commentUserId']=userId
        addReplyCommentPara['contentText']='说说回复评论%s'%createRandomString()
        addReplyCommentPara['commentType']=1#评论类型：0--评论；1--回复
        addReplyCommentPara['replyUserId']=userId
        res5=ShuoShuoIntf.add_comment_for_shuoshuo(addReplyCommentPara)
        self.assertTrue(res5, '说说回复评论失败')
        #在说说详情界面进行查看
        checkCommentInShouShou2=copy.deepcopy(ShuoShuoPara.checkCommentInShuoShuoPara)
        checkCommentInShouShou2['contentText']=addReplyCommentPara['contentText']
        res6=ShuoShuoIntf.check_comment_in_shuoshuo(ShouShouId,checkCommentInShouShou2)
        self.assertTrue(res6, '说说详情不存在该回复评论，回复评论失败')
        #验证删除评论功能并在说说详情界面进行检查
        #删除评论操作
        CommentId=ShuoShuoIntf.get_comment_id_by_content(ShouShouId,addCommentPara['contentText'])
        delCommentPara=copy.deepcopy(ShuoShuoPara.delCommentForShuoShuoPara)
        delCommentPara['id']=CommentId
        res7=ShuoShuoIntf.delete_comment_for_shuoshuo(delCommentPara)
        self.assertTrue(res7, '评论删除成功')
        #在说说详情界面进行查看
        checkCommentInShouShou3=copy.deepcopy(ShuoShuoPara.checkCommentInShuoShuoPara)
        checkCommentInShouShou3['contentText']=addCommentPara['contentText']
        res8=ShuoShuoIntf.check_comment_in_shuoshuo(ShouShouId,checkCommentInShouShou3)
        self.assertFalse(res8, '说说详情界面仍存在改评论，评论删除失败')
        #获取点赞前说说详情点赞数
        getShouShouDetailPara=copy.deepcopy(ShuoShuoPara.getShuoShuoDetail)
        getShouShouDetailPara['id']=ShouShouId
        PraiseNum=ShuoShuoIntf.get_praisenum_in_shuoshuo(getShouShouDetailPara)
#         print PraiseNum
        #验证说说点赞功能
        addPraise=copy.deepcopy(ShuoShuoPara.addPraiseForShouShouPara)
        addPraise['informationId']=ShouShouId
        addPraise['praiseUserId']=userId
        res9=ShuoShuoIntf.add_praise_for_shuoshuo(addPraise)
        self.assertTrue(res9, '说说新增点赞失败')
        #验证说说详情界面点赞是否成功
        checkShouShouDetailPara2=copy.deepcopy(ShuoShuoPara.checkShuoShuoDetailPara)
        checkShouShouDetailPara2['praiseNum']=PraiseNum+1
        result1=ShuoShuoIntf.check_praise_in_shuoshuo(checkShouShouDetailPara2,getShouShouDetailPara)
        self.assertTrue(result1, '说说详情界面点赞检查失败')
        #验证广场说说列表点赞是否成功
        checkShouShouListPara1=copy.deepcopy(ShuoShuoPara.checkShuoShuoPara)
        checkShouShouListPara1['contentText']=addShouShou['casualTalk']['contentText']
        checkShouShouListPara1['title']=addShouShou['casualTalk']['title']
        checkShouShouListPara1['praiseNum']=PraiseNum+1
        result2=ShuoShuoIntf.check_shuoshuo_in_list(checkShouShouListPara1, getSquareListPara)
        self.assertTrue(result2, '广场列表说说点赞检查失败')
        #验证说说取消点赞功能
        cancelPraise=copy.deepcopy(ShuoShuoPara.cancelPraiseForShouShouPara)
        cancelPraise['informationId']=ShouShouId
        cancelPraise['praiseUserId']=userId
        res0=ShuoShuoIntf.cancel_praise_for_shuoshuo(cancelPraise)
        self.assertTrue(res0, '说说取消点赞失败')
        #验证说说详情界面取消点赞是否成功
        checkShouShouDetailPara3=copy.deepcopy(ShuoShuoPara.checkShuoShuoDetailPara)
        checkShouShouDetailPara3['praiseNum']=PraiseNum
        result3=ShuoShuoIntf.check_praise_in_shuoshuo(checkShouShouDetailPara3,getShouShouDetailPara)
        self.assertTrue(result3, '说说详情界面取消点赞检查失败')
        #验证广场说说列表取消点赞是否成功
        checkShouShouListPara2=copy.deepcopy(ShuoShuoPara.checkShuoShuoPara)
        checkShouShouListPara2['contentText']=addShouShou['casualTalk']['contentText']
        checkShouShouListPara2['title']=addShouShou['casualTalk']['title']
        checkShouShouListPara2['praiseNum']=PraiseNum
        result4=ShuoShuoIntf.check_shuoshuo_in_list(checkShouShouListPara2, getSquareListPara)
        self.assertTrue(result4, '广场列表说说点赞检查失败')
        
        pass    
 
    def test_XsShuoShuo_04(self):
        """说说举报测试-app-842"""
        if Global.simulationEnvironment is False:
            XsBaoLiaoIntf.delete_information_reports_by_db()
        try:
            newMobilePhone=XsGongZuoTaiIntf.regist_random_mobile()
            #新手机用户发布一条爆料
            addShouShouPara=copy.deepcopy(ShuoShuoPara.addShuoShuoPara)
            addShouShouPara['casualTalk']['contentText']='说说举报测试内容%s'%createRandomString()
            addShouShouPara['casualTalk']['title']='说说举报测试标题%s'%createRandomString()
            ret=ShuoShuoIntf.add_shuoshuo(addShuoShuoPara=addShouShouPara,mobile=newMobilePhone)
            self.assertTrue(ret, '新增说说失败')
            #默认用户举报
            listpara=copy.deepcopy(ShuoShuoPara.getShuoShuoPara)
            shuoshuoId=ShuoShuoIntf.get_shuoshuo_id_by_content(addShouShouPara['casualTalk']['contentText'], listpara)
            #针对说说进行举报
            addInfoReportDict = copy.deepcopy(XsBaoLiaoPara.addClueInfoReportPara)
            addInfoReportDict['infoId'] = shuoshuoId
            addInfoReportDict['reportUserId'] = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from USERS t where t.mobile='%s'" % Global.XianSuoDftMobile)
            addInfoReportDict['publishUserMobile'] = newMobilePhone
            addInfoReportDict['reportType']=None
            addInfoReportDict['infoType']=InfoType.SHUOSHUO
            ret = XsBaoLiaoIntf.add_clue_information_report(addInfoReportDict)
            self.assertFalse(ret, '不选择举报类型情况下，新增说说举报验证失败')
            #选择举报类型
            addInfoReportDict['reportType']='99'
            ret = XsBaoLiaoIntf.add_clue_information_report(addInfoReportDict)
            self.assertTrue(ret, '新增说说举报验证失败')
            #在后台信息举报列表查看
            getInfoReportDict = copy.deepcopy(XinXiGuanLiPara.getInformationReportPara)
            getInfoReportDict['informationReport.infoType'] = InfoType.SHUOSHUO
            getInfoReportDict['informationReport.state'] = 0 #表示未处理
             
            checkInfoReportDict = copy.deepcopy(XinXiGuanLiPara.checkInformationReportPara)
            checkInfoReportDict['contentText'] = addShouShouPara['casualTalk']['contentText']
             
            ret = XinXiGuanLiIntf.check_information_report_in_list(getInfoReportDict, checkInfoReportDict)
            self.assertTrue(ret, '在举报信息中检查举报失败')
            #获取举报次数参数
            inforPara={
                        'contentText':addShouShouPara['casualTalk']['contentText'],
                        'inforType':InfoType.SHUOSHUO,#InfoType.CLUE爆料，InfoType.SHUOSHUO说说
                        'state':0#0未处理，1已处理
                    }
            reportCount1=XinXiGuanLiIntf.get_report_count_by_content(inforPara)
            #多次举报
            ret = XsBaoLiaoIntf.add_clue_information_report(addInfoReportDict)
            self.assertTrue(ret, '新增线索举报验证失败')
            #多次举报后，后台检查
            ret = XinXiGuanLiIntf.check_information_report_in_list(getInfoReportDict, checkInfoReportDict)
            self.assertTrue(ret, '在举报信息中检查举报失败')
            reportCount2=XinXiGuanLiIntf.get_report_count_by_content(inforPara)
            self.assertEqual(reportCount2, reportCount1+1, '举报次数验证错误')
            Log.LogOutput( message='---------多次举报后，后台举报次数统计功能验证成功！--------')
            #后台删除举报
            XinXiGuanLiIntf.delete_all_information_report(mobile=newMobilePhone)
            #后台验证删除是否成功
            ret = XinXiGuanLiIntf.check_information_report_in_list(getInfoReportDict, checkInfoReportDict)
            self.assertFalse(ret, '删除验证失败')
            #手机端验证是否删除成功
            mlistpara=copy.deepcopy(ShuoShuoPara.getShuoShuoPara)
            mcheckpara=copy.deepcopy(ShuoShuoPara.checkShuoShuoPara)
            mcheckpara['contentText']=addShouShouPara['casualTalk']['contentText']
            mcheckpara['title']=addShouShouPara['casualTalk']['title']
            ret=ShuoShuoIntf.check_shuoshuo_in_list(mcheckpara, mlistpara)
            self.assertFalse(ret, '删除说说手机端验证失败')
            Log.LogOutput( message='---------举报删除功能验证成功！--------')
            #删除处理后，继续举报，查看后台列表是否会生成，预期不再生成举报信箱
            ret = XsBaoLiaoIntf.add_clue_information_report(addInfoReportDict)
            self.assertTrue(ret, '新增线索举报验证失败')
            ret = XinXiGuanLiIntf.check_information_report_in_list(getInfoReportDict, checkInfoReportDict)
            self.assertFalse(ret, '处理举报后再次举报，列表验证失败')
            Log.LogOutput( message='---------处理举报后再次举报,后台不再显示举报信箱，验证成功！--------')
        finally:
            if Global.simulationEnvironment is False:
                XsGongZuoTaiIntf.deleteUserFromDb(mobile=newMobilePhone)
    
    def test_XsShuoShuo_05(self):
        """说说搜索测试-app-835"""
        #新增两条说说
        addShouShouPara1=copy.deepcopy(ShuoShuoPara.addShuoShuoPara)
        addShouShouPara1['casualTalk']['contentText']='第一条说说内容%s'%createRandomString()
        addShouShouPara1['casualTalk']['title']='第一条说说标题%s'%createRandomString()
        ret=ShuoShuoIntf.add_shuoshuo(addShuoShuoPara=addShouShouPara1)
        self.assertTrue(ret, '新增说说失败')
        #第二条
        addShouShouPara2=copy.deepcopy(ShuoShuoPara.addShuoShuoPara)
        addShouShouPara2['casualTalk']['contentText']='第二条说说内容%s'%createRandomString()
        addShouShouPara2['casualTalk']['title']='第二条说说标题%s'%createRandomString()
        ret=ShuoShuoIntf.add_shuoshuo(addShuoShuoPara=addShouShouPara2)
        self.assertTrue(ret, '新增说说失败')
        

        mlistpara=copy.deepcopy(ShuoShuoPara.searchShuoShuoPara)
        mlistpara['contentText']=addShouShouPara1['casualTalk']['contentText']
        mcheckpara1=copy.deepcopy(ShuoShuoPara.checkShuoShuoInSearchListPara)
        mcheckpara1['contentText']=addShouShouPara1['casualTalk']['contentText']
        mcheckpara1['title']=addShouShouPara1['casualTalk']['title']        
        ret=ShuoShuoIntf.check_shuoshuo_in_search_list(mlistpara,mcheckpara1)
        self.assertTrue(ret, '说说搜索验证失败')
        mcheckpara2=copy.deepcopy(ShuoShuoPara.searchShuoShuoPara)
        mcheckpara2['contentText']=addShouShouPara2['casualTalk']['contentText']
        mcheckpara2['title']=addShouShouPara2['casualTalk']['title']        
        ret=ShuoShuoIntf.check_shuoshuo_in_search_list(mlistpara,mcheckpara2)
        self.assertFalse(ret, '说说搜索验证失败')        
        pass 
    
    def test_XsShuoShuo_06(self):
        """说说关注测试-app-840"""
        #新增一条说说
        addShouShouPara=copy.deepcopy(ShuoShuoPara.addShuoShuoPara)
        addShouShouPara['casualTalk']['contentText']='第一条说说内容%s'%createRandomString()
        addShouShouPara['casualTalk']['title']='第一条说说标题%s'%createRandomString()
        ret=ShuoShuoIntf.add_shuoshuo(addShuoShuoPara=addShouShouPara)
        self.assertTrue(ret, '新增说说失败')
        
        userId=XsPaiHangBangIntf.getUserIdByPersonalPoints()
        getSquareListPara=copy.deepcopy(ShuoShuoPara.getShuoShuoPara)
        getSquareListPara['userId']=userId   
        ShouShouId=ShuoShuoIntf.get_shuoshuo_id_by_content(shuoshuoContent=addShouShouPara['casualTalk']['contentText'], squarelistpara=getSquareListPara)
        addConcernPara=copy.deepcopy(ShuoShuoPara.ShouShouAddConcernPara)
        addConcernPara['informationId']=ShouShouId
        addConcernPara['concernUserId']=userId
        addConcernPara['concernDate']=Time.getCurrentDateAndTime()
        #调用说说新增关注方法
        ret=ShuoShuoIntf.addconcern_shuoshuo(addConcernPara)
        self.assertTrue(ret, '说说新增关注失败')
        #检查我的关注列表
        getMyConcernList=copy.deepcopy(ShuoShuoPara.WoDeConcernListPara)
        #定义我的关注列表检查参数
        checkMyConcernListPara=copy.deepcopy(ShuoShuoPara.WoDeConcernListCheckPara)
        checkMyConcernListPara['contentText']=addShouShouPara['casualTalk']['contentText']
        #调用我的关注列表检查方法
        ret=ShuoShuoIntf.check_myconcern_list(checkMyConcernListPara, getMyConcernList)
        self.assertTrue(ret,'我的关注列表检查失败')
        #取消关注
        cancelConcernPara=copy.deepcopy(ShuoShuoPara.ShouShouCancelConcernPara)
        cancelConcernPara['informationId']=ShouShouId
        cancelConcernPara['concernUserId']=userId
        ShuoShuoIntf.cancel_concern_shuoshuo(cancelConcernPara)
        #调用我的关注列表检查方法
        ret=ShuoShuoIntf.check_myconcern_list(checkMyConcernListPara, getMyConcernList)
        self.assertFalse(ret,'我的关注列表检查失败')        
        pass
    
    def tearDown(self):
        pass    
    
    
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(XsShuoShuo("test_XsShuoShuo_04"))
    results = unittest.TextTestRunner().run(suite)
    pass    