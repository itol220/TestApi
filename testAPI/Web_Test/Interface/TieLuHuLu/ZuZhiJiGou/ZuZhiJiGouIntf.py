# -*- coding:UTF-8 -*-
'''
Created on 2017-7-10

@author: Administrator
'''
from COMMON import Log
from CONFIG.Define import LogLevel
from Interface.TieLuHuLu.TieLuHuLuHttpCommon import tieluhulu_post
import json

'''
    @功能： 新增领导小组
    @para: 
    TeamOfficeDict:请调用字典项 ZuZhiGouPara.addTeamOffice
    username:用户名
    password:密码
    @return: 如果添加成功，则返回True；否则返回False  
'''    
def add_team_office(TeamOfficeDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增领导小组开始..")        
    response = tieluhulu_post(url='/baseData/railwayTeamOfficeManage/addRailwayTeamOffice.action', postdata=TeamOfficeDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增领导小组成功")
        return json.loads(response.text)
    else:
        Log.LogOutput(LogLevel.WARN, "新增领导小组失败")
        return False
    
'''
    @功能： 修改领导小组
    @para: modifyTeamOffice
    TeamOfficeDict:请调用字典项 ZuZhiJiGouPara.modifyTeamOffice
    username:用户名
    password:密码
    @return: 如果添加成功，则返回True；否则返回False  
'''    
def modify_team_office(TeamOfficeDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "修改领导小组开始..")        
    response = tieluhulu_post(url='/baseData/railwayTeamOfficeManage/updateRailwayTeamOffice.action', postdata=TeamOfficeDict, username=username, password=password)
    print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "修改领导小组成功")
        return True
    else:
        Log.LogOutput(LogLevel.WARN, "修改领导小组失败")
        return False
    
    
'''  
    @功能： 删除领导小组人员信息
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
'''
def delete_team_person(deleteDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "删除领导小组人员开始..")
    response = tieluhulu_post(url='/baseData/railwayTeamPersonManage/deleteRailwayTeamPersonByIds.action', postdata=deleteDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除领导小组人员成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "删除领导小组人员失败")
    return response
    