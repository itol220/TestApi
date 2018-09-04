# -*- coding:UTF-8 -*-
'''
Created on 2016-3-31

@author: chenhui
'''
from __future__ import unicode_literals
from COMMON import Log
from COMMON.CommonUtil import createRandomString
from CONFIG import Global
from CONFIG.InitDefaultPara import clueOrgInit, clueUserInit
from Interface.XianSuoApp.GongGaoLan.XsGongGaoLanIntf import addClueProclamation, \
    updClueProclamationState, getClueProclamationList, getNoticeList, \
    delAllClueProclamation, checkNoticeInList, getNoticeInfo
from Interface.XianSuoApp.GongGaoLan.XsGongGaoLanPara import GongGaoLieBiao
from Interface.XianSuoApp.GongZuoTai.XsGongZuoTaiIntf import initUser
import copy
import json
import unittest



class XsGongGaoLan(unittest.TestCase):

    def setUp(self):
#         SystemMgrIntf.initEnv()''
        initUser()
        delAllClueProclamation()
        pass
    #获取验证码
    def test_XsGongGaoLan_01(self):
        '''PC新增公告栏'''
        addPara={
            'mode':'add',
            'infoType':'1',
            'informationVo.information.orgId':clueOrgInit['DftQuOrgId'],
            'informationVo.information.id':'',
            'informationVo.information.title':'测试标题%s'%createRandomString(),
            'informationVo.information.contentText':'正文%s'%createRandomString()
                 }
        addClueProclamation(para=addPara,username=clueUserInit['DftQuUser'])
        #获取列表
        listPara=copy.deepcopy(GongGaoLieBiao)
        listPara['searchInfoVo.information.orgId']=clueOrgInit['DftQuOrgId']
        response=getClueProclamationList(para=listPara)
        responseDict=json.loads(response.text)
        #获取公告,默认状态为不公开，无法获取到
        para={
                'tqmobile':'true',
                'departmentNo':clueOrgInit['DftQuOrgDepNo'],
                'page':1,
                'rows':200
              }
        res=json.loads(getNoticeList(para=para).text)
        self.assertEqual(res['response']['module']['records'], 0, '公告状态为不公开，获取公告验证失败')
        Log.LogOutput(message='公告状态为不公开，获取公告验证成功！')
        #修改状态为“公开”
        statePara={
                'ids':responseDict['rows'][0]['information']['id'],
                'showState':1
                   }
        updClueProclamationState(para=statePara) 
        #再次检测
        checkPara={
                   'contentText':addPara['informationVo.information.contentText'],
                   'title':addPara['informationVo.information.title']
                   }
        result=checkNoticeInList(checkPara=checkPara,listPara=para)
        self.assertTrue(result, '公告列表获取验证失败')
        #获取公告详情
        noticeDetailPara={
                    'tqmobile':'true',
                    'id':responseDict['rows'][0]['information']['id']
                          }
        resultDict=json.loads(getNoticeInfo(para=noticeDetailPara).text)
        self.assertEquals(resultDict['response']['module']['information']['contentText'],addPara['informationVo.information.contentText'] ,'内容验证失败')
        self.assertEquals(resultDict['response']['module']['information']['title'], addPara['informationVo.information.title'],'标题验证失败')
        Log.LogOutput(message='公告详情接口验证通过！')
        pass
        
        
    def tearDown(self):
        pass    
    
    
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(XsGongGaoLan("test_XsGongGaoLan_01"))
    results = unittest.TextTestRunner().run(suite)
    pass    