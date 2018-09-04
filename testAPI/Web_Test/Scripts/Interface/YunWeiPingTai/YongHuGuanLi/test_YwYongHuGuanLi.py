# -*- coding:UTF-8 -*-
'''
Created on 2016-4-8

@author: N-286
'''
from __future__ import unicode_literals
import copy
import json
import time
import unittest
from COMMON import Log
from CONFIG import Global
from Interface.XianSuoApp.GongZuoTai.XsGongZuoTaiIntf import createRandomNumber
from Interface.XianSuoApp.WoDeXinXi.XsMyInformationIntf import encodeToMd5
from Interface.XianSuoApp.XinXiGuangChang import XsInformationSquareIntf
from Interface.XianSuoApp.xianSuoHttpCommon import desEncrypt
from Interface.YunWeiPingTai.YunWeiCommon.YunWeiCommonIntf import \
    exeDbQueryYunWei
from Interface.XianSuoApp.GongZuoTai import XsGongZuoTaiIntf, XsGongZuoTaiPara
from Interface.YunWeiPingTai.YongHuGuanLi import YwYongHuGuanLiPara,\
    YwYongHuGuanLiIntf
from Interface.YunWeiPingTai.YunWeiCommon import YunWeiCommonIntf


class XsClueUserManager(unittest.TestCase):

    def setUp(self):
        if Global.simulationEnvironment is False:
            #删除用户'12345678901'
            XsGongZuoTaiIntf.deleteUserFromDb(mobile='12345678901')
            #清除默认手机和12345678901用户反馈表userfeedbacks中的数据
            exeDbQueryYunWei(dbCommand="delete from userfeedbacks u where u.mobile='%s' or u.mobile='%s'" % (Global.XianSuoDftMobile,'12345678901')) 
#         XsGongZuoTaiIntf.initUser()
        pass
    
    def test_user_search_01(self):
        '''通过手机号码进行搜索操作-478'''
        #产生一个手机随机号码
#         registMobile='123%s'%str(createRandomNumber(length=8))
#         count=YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand="select count(*)  from users w where w.mobile='%s'" % registMobile)
#         while count>=1:
#             registMobile='123%s'%str(createRandomNumber(length=8))
#             count=YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand="select count(*)  from users w where w.mobile='%s'" % registMobile)
#         XsGongZuoTaiIntf.initUser(mobile=registMobile)
        registMobile=XsGongZuoTaiIntf.regist_random_mobile()
        #通过手机号查询
        searchPara=copy.deepcopy(YwYongHuGuanLiPara.getClueUserManageListPara)
        searchPara['user.mobile']=registMobile

        #结果存在性查询
        checkPara1 = copy.deepcopy(YwYongHuGuanLiPara.checkClueUserManageListPara)
        checkPara1['mobile']=registMobile
        
        result1=YwYongHuGuanLiIntf.checkUserInUserManagerList(checkpara=checkPara1,listpara=searchPara)
        self.assertTrue(result1, '无法搜索到符合要求的用户信息')
        
        #默认手机号无法搜索到
        checkPara2 = copy.deepcopy(YwYongHuGuanLiPara.checkClueUserManageListPara)
        checkPara2['mobile']=Global.XianSuoDftMobile

        result2=YwYongHuGuanLiIntf.checkUserInUserManagerList(checkpara=checkPara2,listpara=searchPara)
        self.assertFalse(result2, '检查到不符合要求的用户信息')
        
        #通过默认手机号搜索
        searchPara=copy.deepcopy(YwYongHuGuanLiPara.getClueUserManageListPara)
        searchPara['user.mobile']=Global.XianSuoDftMobile
        
        checkPara1 = copy.deepcopy(YwYongHuGuanLiPara.checkClueUserManageListPara)
        checkPara1['mobile']=registMobile
        
        result1=YwYongHuGuanLiIntf.checkUserInUserManagerList(checkpara=checkPara1,listpara=searchPara)
        self.assertFalse(result1, '搜索到不符合要求的用户信息')
        
        checkPara2 = copy.deepcopy(YwYongHuGuanLiPara.checkClueUserManageListPara)
        checkPara2['mobile']=Global.XianSuoDftMobile

        result2=YwYongHuGuanLiIntf.checkUserInUserManagerList(checkpara=checkPara2,listpara=searchPara)
        self.assertTrue(result2, '未搜索到符合要求的用户信息')
        if Global.simulationEnvironment is False:
            XsGongZuoTaiIntf.deleteUserFromDb(mobile=registMobile)        
        pass
    
    def test_user_forbid_and_delete_02(self):
        '''在运维平台对账号A进行禁号/解禁/删除操作-477'''
        #产生一个手机随机号码
        registMobile=XsGongZuoTaiIntf.regist_random_mobile()
        #禁号
        userId = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from USERS t where t.mobile='%s'" % registMobile)
        ret = YwYongHuGuanLiIntf.disable_user(userId=userId)
        self.assertTrue(ret, '禁号失败')
        
        #验证禁号功能，
        #1.使用该号码登录线索
        res1=XsInformationSquareIntf.getUserLogin(mobile=registMobile,password='111111')
        self.assertEqual(res1['response']['success'], False, '禁号验证失败')
        Log.LogOutput(message='禁号成功')
        
        #2.在用户管理列表检测列表状态，为“禁用”（1）
        checkPara1 = copy.deepcopy(YwYongHuGuanLiPara.checkClueUserManageListPara)
        checkPara1['mobile'] = registMobile
        checkPara1['state'] = 1 #表示禁号
        
        searchPara=copy.deepcopy(YwYongHuGuanLiPara.getClueUserManageListPara)  
        result1=YwYongHuGuanLiIntf.checkUserInUserManagerList(checkpara=checkPara1,listpara=searchPara)
        self.assertTrue(result1, '禁号列表验证失败')
        Log.LogOutput(message='禁号列表验证成功')
        
        #解禁
        ret = YwYongHuGuanLiIntf.enable_user(userId=userId)
        self.assertTrue(ret, '解禁失败')
        
        #验证解禁功能
        #1.使用该号码登录
        res2=XsInformationSquareIntf.getUserLogin(mobile=registMobile,password='111111')
        self.assertEqual(res2['response']['success'], True, '解禁验证失败')
        Log.LogOutput(message='解禁成功')
        
        #2.检测列表状态，为“正常”（0）
        checkPara2 = copy.deepcopy(YwYongHuGuanLiPara.checkClueUserManageListPara)
        checkPara2['mobile'] = registMobile
        checkPara2['state'] = 0 #表示已解禁

        result2=YwYongHuGuanLiIntf.checkUserInUserManagerList(checkpara=checkPara2,listpara=searchPara)
        self.assertTrue(result2, '解禁列表验证失败')
        Log.LogOutput(message='解禁列表验证成功')
        
        #软删除
        ret = YwYongHuGuanLiIntf.delete_user(userId=userId)
        self.assertTrue(ret, '删除失败')
        
        #通过列表验证删除是否成功
        checkPara3 = copy.deepcopy(YwYongHuGuanLiPara.checkClueUserManageListPara)
        checkPara3['mobile'] = registMobile

        result3=YwYongHuGuanLiIntf.checkUserInUserManagerList(checkpara=checkPara3,listpara=searchPara)
        self.assertFalse(result3, '删除功能列表验证失败')
        Log.LogOutput(message='删除功能列表验证成功')
               
        res3=XsInformationSquareIntf.getUserLogin(mobile=registMobile,password='111111')
        self.assertEqual(res3['response']['success'], False, '删除验证失败')
        Log.LogOutput(message='删除成功')
        #真删除
        if Global.simulationEnvironment is False:
            XsGongZuoTaiIntf.deleteUserFromDb(mobile=registMobile)     
        pass
    
    def test_online_user_search_03(self):
        '''在线用户管理-查询-482'''
        #产生一个手机随机号码
        registMobile='123%s'%str(createRandomNumber(length=8))
        count=YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand="select count(*)  from users w where w.mobile='%s'" % registMobile)
        while count>=1:
            registMobile='123%s'%str(createRandomNumber(length=8))
            count=YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand="select count(*)  from users w where w.mobile='%s'" % registMobile)
        XsGongZuoTaiIntf.initUser(mobile=registMobile,password='678901')
        
        #登录一次新注册的用户
        res=XsInformationSquareIntf.getUserLogin(mobile=registMobile,password='678901')
        self.assertEqual(res['response']['success'], True, '新用户登录验证失败')
        
        #默认用户登录一次
        res=XsInformationSquareIntf.getUserLogin(mobile=registMobile,password='678901')
        self.assertEqual(res['response']['success'], True, '默认用户登录验证失败')
        
        #查询    
        searchPara=copy.deepcopy(YwYongHuGuanLiPara.zaiXianYongHuGuanLiLieBiao)
        searchPara['session.userName']=registMobile
        
        #结果存在性查询
        checkPara1 = copy.deepcopy(YwYongHuGuanLiPara.checkOnlineUserPara)
        checkPara1['userName'] = registMobile

        result1=YwYongHuGuanLiIntf.check_online_user_list(checkpara=checkPara1,listpara=searchPara)
        self.assertTrue(result1, '查询验证失败')
        
        checkPara2 = copy.deepcopy(YwYongHuGuanLiPara.checkOnlineUserPara)
        checkPara2['userName'] = Global.XianSuoDftMobile
        
        result2=YwYongHuGuanLiIntf.check_online_user_list(checkpara=checkPara2,listpara=searchPara)
        self.assertFalse(result2, '查询验证失败')
        if Global.simulationEnvironment is False:
            XsGongZuoTaiIntf.deleteUserFromDb(mobile=registMobile)     
        pass

    def test_user_logout_04(self):
        '''在线用户管理-注销-481'''
        #产生一个手机随机号码
        registMobile='123%s'%str(createRandomNumber(length=8))
        count=YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand="select count(*)  from users w where w.mobile='%s'" % registMobile)
        while count>=1:
            registMobile='123%s'%str(createRandomNumber(length=8))
            count=YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand="select count(*)  from users w where w.mobile='%s'" % registMobile)
        XsGongZuoTaiIntf.initUser(mobile=registMobile,password='678901')
        #登录一次新注册的用户
        res=XsInformationSquareIntf.getUserLogin(mobile=registMobile,password='678901')
        self.assertEqual(res['response']['success'], True, '登录验证失败')
        
        #在线用户列表中存在该用户
        searchPara=copy.deepcopy(YwYongHuGuanLiPara.zaiXianYongHuGuanLiLieBiao)
        
        #结果存在性查询
        checkPara1 = copy.deepcopy(YwYongHuGuanLiPara.checkClueUserManageListPara)
        checkPara1['userName'] = registMobile
        
        result1=YwYongHuGuanLiIntf.check_online_user_list(checkpara=checkPara1,listpara=searchPara)
        self.assertTrue(result1, '数据存在列表中验证失败')
        Log.LogOutput( message='账号存在在线用户列表中')
        
        #注销用户
        userListId = YwYongHuGuanLiIntf.get_online_user_id_by_mobile(registMobile)
        
        ret = YwYongHuGuanLiIntf.logout_user(userListId)
        self.assertTrue(ret, '注销失败！')
        
        #验证用户是否存在列表中
        result2=YwYongHuGuanLiIntf.check_online_user_list(checkpara=checkPara1,listpara=searchPara)
        self.assertFalse(result2, '注销后用户还存在与在线用户列表中')
        Log.LogOutput( message='注销功能验证通过！')
        if Global.simulationEnvironment is False:
            XsGongZuoTaiIntf.deleteUserFromDb(mobile=registMobile) 
        pass
    
    def tearDown(self):
        pass    
    
    
if __name__ == "__main__":
    suite = unittest.TestSuite()
#     suite.addTest(XsClueUserManager("test_user_search_01"))
    suite.addTest(XsClueUserManager("test_user_forbid_and_delete_02"))
#     suite.addTest(XsClueUserManager("test_online_user_search_03"))
#     suite.addTest(XsClueUserManager("test_user_logout_04"))
    results = unittest.TextTestRunner().run(suite)
    pass   