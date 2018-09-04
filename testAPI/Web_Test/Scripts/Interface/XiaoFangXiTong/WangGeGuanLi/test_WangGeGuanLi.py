# -*- coding:UTF-8 -*-
'''
Created on 2016-6-15

@author: N-66
'''
from __future__ import unicode_literals
import unittest
import copy
import random
from CONFIG.Define import LogLevel
from Interface.XiaoFangXiTong.SystemMgr import SystemMgrIntf
from Interface.XiaoFangXiTong.WangGeGuanLi import WangGeGuanLiPara,\
    WangGeGuanLiIntf
from Interface.XiaoFangXiTong.Common import InitDefaultPara, CommonIntf
from COMMON import CommonUtil
from COMMON import Log


class WangGeGuanLi(unittest.TestCase): 
    def setUp(self):
        SystemMgrIntf.initEnv()
        
        pass 
    def testCase_001(self):
#新增辖区信息图片
#         AddXiaQuPic=copy.deepcopy(WangGeGuanLiPara.AddXiaQuPic)
#         WangGeGuanLiIntf.Add_XiaQuPic(AddXiaQuPic, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
#         Log.LogOutput(LogLevel.INFO,'新增辖区图片成功..')
#新增辖区领导班子成员        
        AddLead1=copy.deepcopy(WangGeGuanLiPara.AddLeadTeam)
        AddLead1['leaderTeams.orgId']=InitDefaultPara.orgInit['DftWangGeOrgId']
        AddLead1['leaderTeams.name']='领导名字%s'% CommonUtil.createRandomString()
        AddLead1['leaderTeams.gender']='0'
        AddLead1['leaderTeams.duty']=random.choice(['网格负责人','网格领导人','网格小秘'])
        AddLead1['leaderTeams.sort']='1'
        AddLead1['leaderTeams.introduction']='网格领导永垂不朽'
        WangGeGuanLiIntf.Add_LeadTeam(LeadTeamDict=AddLead1, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        AddLead2=copy.deepcopy(AddLead1)
        AddLead2['leaderTeams.name']='领导名字%s'% CommonUtil.createRandomString()
        AddLead2['leaderTeams.duty']=random.choice(['网格负责人','网格领导','网格小秘'])
        WangGeGuanLiIntf.Add_LeadTeam(LeadTeamDict=AddLead2, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        Log.LogOutput(LogLevel.INFO,'新增辖区领导班子成功..')
#修改领导班子成员
        EditLead=copy.deepcopy(WangGeGuanLiPara.EditLeadTeam)
        EditLead['leaderTeams.id']=CommonIntf.getDbQueryResult(dbCommand="select t.id from leaderteams t where t.name='%s'"%AddLead1['leaderTeams.name'])
        EditLead['leaderTeams.orgCode']=CommonIntf.getDbQueryResult(dbCommand="select t.orgcode from leaderteams t where t.name='%s'"%AddLead1['leaderTeams.name'])
        EditLead['leaderTeams.orgId']=InitDefaultPara.orgInit['DftWangGeOrgId']
        EditLead['leaderTeams.name']='修改领导名字%s'% CommonUtil.createRandomString()
        WangGeGuanLiIntf.Edit_LeadTeam(LeadTeamDict=EditLead, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        Log.LogOutput(LogLevel.INFO,'修改辖区领导班子成功..')
#删除领导班子成员
        DelLead=copy.deepcopy(WangGeGuanLiPara.DelLeadTeam)
        DelLead['leaderTeams.id']=CommonIntf.getDbQueryResult(dbCommand="select t.id from leaderteams t where t.name='%s'"%EditLead['leaderTeams.name'])
        WangGeGuanLiIntf.Del_LeadTeam(LeadTeamDict=DelLead, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        Log.LogOutput(LogLevel.INFO,'删除辖区领导班子成功..')
        
        
         
        
        pass


def tearDown(self):    
        pass

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(WangGeGuanLi("testCase_001"))
    results = unittest.TextTestRunner().run(suite)
    pass