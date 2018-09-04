# -*- coding:UTF-8 -*-
'''
Created on 2016-6-7

@author: maoxy
'''
from __future__ import unicode_literals
import copy
from COMMON import CommonUtil,Log
from Interface.XiaoFangXiTong.TongZhiTongGao import TongZhiTongGaoIntf,\
    TongZhiTongGaoPara
from CONFIG.Define import LogLevel
import unittest
from Interface.XiaoFangXiTong.Common import CommonIntf
from Interface.XiaoFangXiTong.Common import InitDefaultPara
from Interface.XiaoFangXiTong.SystemMgr import SystemMgrIntf



class TongZhiTongGao(unittest.TestCase): 

    def setUp(self):
        SystemMgrIntf.initEnv()
        
        pass 
    def testCase_001(self):
#    新增通知通告
        AddTongZhiTongGaoParam=copy.deepcopy(TongZhiTongGaoPara.AddTongZhiTongGaoParam)
        AddTongZhiTongGaoParam['fireNotice.title']='标题%s'% CommonUtil.createRandomString()
        AddTongZhiTongGaoParam['fireNotice.content']='内容%s'%CommonUtil.createRandomString()
        AddTongZhiTongGaoParam['signDeptIds']=InitDefaultPara.orgInit['DftWangGeOrgId']
        AddTongZhiTongGaoParam['fireNotice.createDeptName']=InitDefaultPara.orgInit['DftSheQuOrg']
        AddTongZhiTongGaoParam['fireNotice.createDept']=InitDefaultPara.orgInit['DftSheQuOrgId']
        AddTongZhiTongGaoParam['fireNotice.createUserName']=InitDefaultPara.userInit['DftSheQuUserXM']
        AddTongZhiTongGaoParam['fireNotice.createUser']=InitDefaultPara.userInit['DftSheQuUser']
        AddTongZhiTongGaoParam['fireNotice.noticeType']='0'
        AddTongZhiTongGaoParam['mode']='view'
        response=TongZhiTongGaoIntf.Add_TongZhiTongGao(TongZhiTongGaoDict=AddTongZhiTongGaoParam,username=InitDefaultPara.userInit['DftSheQuUser'],password='11111111')
        Log.LogOutput(LogLevel.INFO,'新增通知通告成功..')
#   列表查看通知通告
        TongZhiTongGaoParam=copy.deepcopy(TongZhiTongGaoPara.TongZhiTongGao)
        TongZhiTongGaoParam['simpleTitle']=AddTongZhiTongGaoParam['fireNotice.title']
        TongZhiTongGaoParam['fireNoticeId']=CommonIntf.getDbQueryResult(dbCommand ="select t.fire_notice_id from fire_notice t where t.title='%s'"%AddTongZhiTongGaoParam['fireNotice.title'])
        response=TongZhiTongGaoIntf.Get_TongZhiTongGao(TongZhiTongGaoDict=TongZhiTongGaoParam,username=InitDefaultPara.userInit['DftSheQuUser'],password='11111111')
        self.assertTrue(response,'通知通告查看失败')
#    修改通知通告
        EditTongZhiTongGaoParam=copy.deepcopy(TongZhiTongGaoPara.EditTongZhiTongGaoParam)
        EditTongZhiTongGaoParam['fireNotice.title']='标题%s'% CommonUtil.createRandomString()
        EditTongZhiTongGaoParam['signDeptIds']='3,1,1,3'
        EditTongZhiTongGaoParam['fireNotice.createDept']='1'
        EditTongZhiTongGaoParam['fireNotice.createUserName']='1111111'
        EditTongZhiTongGaoParam['fireNotice.createUser']='admin1'
        EditTongZhiTongGaoParam['fireNotice.noticeType']='0'
        EditTongZhiTongGaoParam['fireNotice.fireNoticeId']=CommonIntf.getDbQueryResult(dbCommand ="select t.fire_notice_id from fire_notice t where t.title='%s'"%AddTongZhiTongGaoParam['fireNotice.title'])
        response=TongZhiTongGaoIntf.Edit_TongZhiTongGao(TongZhiTongGaoDict=EditTongZhiTongGaoParam,username=InitDefaultPara.userInit['DftSheQuUser'],password='11111111')
        Log.LogOutput(LogLevel.INFO,'修改通知通告成功..')
#         self.assertTrue(response,'通知通告修改失败')
#    修改后列表查看通知通告
        EditCheckTongZhiTongGaoParam=copy.deepcopy(TongZhiTongGaoPara.TongZhiTongGao)
        EditCheckTongZhiTongGaoParam['simpleTitle']=EditTongZhiTongGaoParam['fireNotice.title']
        EditCheckTongZhiTongGaoParam['fireNoticeId']=CommonIntf.getDbQueryResult(dbCommand ="select t.fire_notice_id from fire_notice t where t.title='%s'"%EditTongZhiTongGaoParam['fireNotice.title'])
        response=TongZhiTongGaoIntf.Get_TongZhiTongGao(TongZhiTongGaoDict=EditCheckTongZhiTongGaoParam,username=InitDefaultPara.userInit['DftSheQuUser'],password='11111111')
        self.assertTrue(response,'通知通告查看失败')
#    删除通知通告
        DelTongZhiTongGaoParam=copy.deepcopy(TongZhiTongGaoPara.DelTongZhiTongGaoParam)
        DelTongZhiTongGaoParam['fireNoticeId']=EditTongZhiTongGaoParam['fireNotice.fireNoticeId']
        response=TongZhiTongGaoIntf.Del_TongZhiTongGao(TongZhiTongGaoDict=DelTongZhiTongGaoParam, username=InitDefaultPara.userInit['DftSheQuUser'], password='11111111')
        
#         self.assertTrue(response,'通知通告删除失败')
#       删除后列表查看
        DelCheckTongZhiTongGaoParam=copy.deepcopy(TongZhiTongGaoPara.TongZhiTongGao)
        DelCheckTongZhiTongGaoParam['simpleTitle']=EditTongZhiTongGaoParam['fireNotice.title']
        DelCheckTongZhiTongGaoParam['fireNoticeId']=DelTongZhiTongGaoParam['fireNoticeId']
        response=TongZhiTongGaoIntf.Get_TongZhiTongGao(TongZhiTongGaoDict=DelCheckTongZhiTongGaoParam,username=InitDefaultPara.userInit['DftSheQuUser'],password='11111111')
        self.assertFalse(response,'通知通告在列表中依然存在')
        pass
    
    
    def tearDown(self):    
        pass

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TongZhiTongGao("testCase_001"))
    results = unittest.TextTestRunner().run(suite)
    pass











