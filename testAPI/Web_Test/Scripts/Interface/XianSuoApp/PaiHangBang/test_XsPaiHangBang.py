# -*- coding:UTF-8 -*-
'''
Created on 2016-4-8

@author: N-286
'''
from __future__ import unicode_literals
from COMMON import Log, Time
from CONFIG import Global
from CONFIG.InitDefaultPara import clueOrgInit
from Interface.XianSuoApp.BaoLiao.XsBaoLiaoIntf import addXianSuo, \
    deleteAllClues, viewSchedule
from Interface.XianSuoApp.BaoLiao.XsBaoLiaoPara import xinZeng2
from Interface.XianSuoApp.GongZuoTai.XsGongZuoTaiIntf import initUser
from Interface.XianSuoApp.JiFenShangCheng import XsJiFenShangChengIntf
from Interface.XianSuoApp.PaiHangBang.XsPaiHangBangIntf import getPersonalPoints, \
    checkPersonalPointInList, checkPersonalPointInCountyList
from Interface.XianSuoApp.XinXiGuangChang.XsInformationSquareIntf import \
    getUserLogin, addConcern, addPraise, addComment
from Interface.XianSuoApp.XinXiGuangChang.XsInformationSquarePara import \
    addPraisePara, addCommentPara
from Interface.YunWeiPingTai.JiFenShangCheng import JiFenShangChengIntf
from Interface.YunWeiPingTai.JiFenShangCheng.JiFenShangChengIntf import \
    getPersonalPointsOnPcByUsername
from Interface.YunWeiPingTai.XiTongPeiZhi import XiTongPeiZhiIntf
import copy
import json
import unittest

class XsPaiHangBang(unittest.TestCase):

    def setUp(self):
#         SystemMgrIntf.initEnv()''
        initUser()
        deleteAllClues()
        pass
    
    def test_XsPaiHangBang_01(self):
        '''运维平台-积分商城-积分配置、积分排行-487、490'''
        #积分配置
        #新增爆料，信息
        JiFenShangChengIntf.initPointSetting()
        if Global.simulationEnvironment is False:
        #设置用户初始积分值
            XsJiFenShangChengIntf.setPointByMobile( point=10086)
        #获取登录信息
        resDict=getUserLogin()
        self.assertEqual(resDict['success'], True, '登录验证失败')      
        #获取个人积分
        para1={
               'tqmobile':'true',
               'departmentNo':clueOrgInit['DftQuOrgDepNo']
               }
        result1=getPersonalPoints(para=para1)
        checkDict=json.loads(result1.text)['response']['module']['pointsStatistics']
        #区县积分列表参数
        listpara1={
                "tqmobile":"true",
                "departmentNo":clueOrgInit['DftQuOrgDepNo'],
                "page":"1",
                "rows":"100"
               }
        listpara2={
               "tqmobile":"true",
               "page":"1",
               "rows":"100"
        }
        rs1=checkPersonalPointInCountyList(checkDict=checkDict,listpara=listpara1)
        self.assertTrue(rs1, "验证积分位于区县列表中失败")
        #验证个人积分位于积分列表中
        rs2=checkPersonalPointInList(checkDict=checkDict,listpara=listpara2)
        self.assertTrue(rs2, '验证个人积分位于列表中失败')
        myPoints1=json.loads(result1.text)['response']['module']['pointsStatistics']['sumPoints']
        userId=json.loads(result1.text)['response']['module']['pointsStatistics']['userId']
        para0={
                'pointsStatistics.departmentNo':clueOrgInit['DftQuOrgDepNo'],#95,
                '_search':'false',
                'rows':200,
                'page':1,
                'sidx':'id',
                'sord':'desc'
                }
        #PC与APP积分比较
        myPoints11=getPersonalPointsOnPcByUsername(para=para0,userId=userId)
        self.assertEqual(myPoints1, myPoints11, 'PC与APP积分数据不一致')
        #新增一条线索，查看积分是否+1
        addPara=copy.deepcopy(xinZeng2)
        res1=addXianSuo(addPara)
        self.assertTrue(res1.result, '新增线索失败')
        result2=getPersonalPoints(para=para1)
        self.assertTrue(result2.result, '获取个人积分信息失败')
        myPoints2=json.loads(result2.text)['response']['module']['pointsStatistics']['sumPoints']
        #PC与APP积分比较
        myPoints22=getPersonalPointsOnPcByUsername(para=para0,userId=userId)
        self.assertEqual(myPoints2, myPoints22, 'PC与APP积分数据不一致')
        self.assertEquals(myPoints2, myPoints1+1, '新增爆料后积分累计不正确')
        Log.LogOutput( message='新增爆料后积分累计正确')
        #关注线索，查看积分是否加2
        listPara={
                'tqmobile':'true',
                'page':'1',
                'rows':'100'
                  }
        lsr=viewSchedule(para=listPara)
        #查看进度列表结果字典项
        lsrDict=json.loads(lsr.text)
        #新增关注
        addConPara={
                'tqmobile':'true',
                'informationId':lsrDict['response']['module']['rows'][0]['information']['id'],
                'concernUserId':lsrDict['response']['module']['rows'][0]['information']['publishUserId'],
                'concernDate':Time.getCurrentDate()
                    }
        res=addConcern(para=addConPara)
        self.assertTrue(res.result, '新增关注失败')
        result3=getPersonalPoints(para=para1)
        self.assertTrue(result3.result, '获取个人积分信息失败')
        myPoints3=json.loads(result3.text)['response']['module']['pointsStatistics']['sumPoints']
        #PC与APP积分比较
        myPoints33=getPersonalPointsOnPcByUsername(para=para0,userId=userId)
        self.assertEqual(myPoints3, myPoints33,'PC与APP积分数据不一致')
        self.assertEquals(myPoints3, myPoints2+2, '新增关注后积分累计不正确')
        Log.LogOutput( message='新增关注后积分累计正确')
        #新增点赞
        addpara=copy.deepcopy(addPraisePara)
        addpara['praiseUserId']=lsrDict['response']['module']['rows'][0]['information']['publishUserId']
        addpara['informationId']=lsrDict['response']['module']['rows'][0]['information']['id']
        res2=addPraise(para=addpara)
        self.assertTrue(res2.result, '新增点赞失败')
        result4=getPersonalPoints(para=para1)
        self.assertTrue(result4.result, '获取个人积分信息失败')
        myPoints4=json.loads(result4.text)['response']['module']['pointsStatistics']['sumPoints']
        #PC与APP积分比较
        myPoints44=getPersonalPointsOnPcByUsername(para=para0,userId=userId)
        self.assertEqual(myPoints4, myPoints44, 'PC与APP积分数据不一致')
        self.assertEquals(myPoints4, myPoints3+3, '新增点赞后积分累计不正确')
        Log.LogOutput( message='新增点赞后积分累计正确')
        #新增评论
        addcompara=copy.deepcopy(addCommentPara)
        addcompara['informationId']=lsrDict['response']['module']['rows'][0]['information']['id']
        addcompara['commentUserId']=lsrDict['response']['module']['rows'][0]['information']['publishUserId']
        addcompara['commentType']=0
        res3=addComment(para=addcompara)
        self.assertTrue(res3.text, '新增评论失败')
        result5=getPersonalPoints(para=para1)
        self.assertTrue(result5.result, '获取个人积分信息失败')
        myPoints5=json.loads(result5.text)['response']['module']['pointsStatistics']['sumPoints']
        #PC与APP积分比较
        myPoints55=getPersonalPointsOnPcByUsername(para=para0,userId=userId)
        self.assertEqual(myPoints5, myPoints55, 'PC与APP积分数据不一致')
        self.assertEquals(myPoints5, myPoints4+4, '新增评论后积分累计不正确')
        Log.LogOutput( message='新增点赞后积分累计正确')
        pass
    def tearDown(self):
        pass  
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(XsPaiHangBang("test_XsPaiHangBang_01"))
    results = unittest.TextTestRunner().run(suite)
    pass  