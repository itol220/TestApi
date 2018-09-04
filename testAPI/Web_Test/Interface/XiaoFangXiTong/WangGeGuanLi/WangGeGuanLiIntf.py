# -*- coding:UTF-8 -*-
'''
Created on 2016-6-15

@author: N-66
'''
from __future__ import unicode_literals
from COMMON import Log,CommonUtil
from CONFIG.Define import LogLevel
from Interface.XiaoFangXiTong import xiaoFangXiTongHttpCommon



def Add_XiaQuPic(XiaQuPic,username=None,password=None):
    Log.LogOutput(LogLevel.INFO,'新增图片开始..')
    xiaoFangXiTongHttpCommon.xiaofang_post(url='/baseinfo/villageProfile/updateOrSaveVillageProfileImgUrl.action',postdata=XiaQuPic,username=username,password=password)
     
def Add_LeadTeam(LeadTeamDict,username=None,password=None):
    Log.LogOutput(LogLevel.INFO,'新增领导班子开始..')
    xiaoFangXiTongHttpCommon.xiaofang_post(url='/baseinfo/villageProfile/addLeaderTeam.action',postdata=LeadTeamDict,username=username,password=password)

def Edit_LeadTeam(LeadTeamDict,username=None,password=None):
    Log.LogOutput(LogLevel.INFO,'修改领导班子开始..')
    xiaoFangXiTongHttpCommon.xiaofang_post(url='/baseinfo/villageProfile/updateLeaderTeam.action',postdata=LeadTeamDict,username=username,password=password)

def Del_LeadTeam(LeadTeamDict,username=None,password=None):
    Log.LogOutput(LogLevel.INFO,'删除领导班子开始..')
    xiaoFangXiTongHttpCommon.xiaofang_get(url='/baseinfo/villageProfile/deleteLeaderTeam.action',param=LeadTeamDict,username=username,password=password)