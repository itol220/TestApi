# -*- coding:UTF-8 -*-
'''
Created on 2018年4月12日 17:24:34

@author: slp
'''

import copy
import json

from COMMON import Log, Util
from CONFIG.Define import LogLevel
from Interface.QuanKeCaiJi.HouTaiGuanLi21200.TaskManager.PolicyList import PolicyPara, \
    PolicyListIntf
from Interface.QuanKeCaiJi.HouTaiGuanLi21200.TaskManager.TaskList import TaskPara
from Interface.QuanKeCaiJi.common import QuanKeCaiJiHttpCommon


def add_task( addTaskDict, username = None, password = None , toCheckMessage = None ):
    Log.LogOutput( LogLevel.INFO, "=====添加任务开始=====" )
    
    url = "/taskManage/addTask";
    
    # 先根据关联策略的名称，查找策略的ID
    policyId = PolicyListIntf.get_policy_id_by_name( addTaskDict['taskPloyDO.cname'], None, username, password )
    addTaskDict['taskPloyDO.id'] = policyId
    
    response = QuanKeCaiJiHttpCommon.quan_ke_cai_ji_21200_post( url, addTaskDict, username = username, password = password )
    
    # 如果有要检查的内容，则根据实际情况检查
    if toCheckMessage is not None:
        return Util.checkMessageExistsInAnotherMessage( toCheckMessage, response.text )
    # 否则，就根据报文结果判断正误
    else:
        if response.result is True:
            Log.LogOutput( LogLevel.INFO, "=====添加任务成功=====" )
            return True
        else:
            Log.LogOutput( LogLevel.ERROR, "=====添加任务失败=====" )
            return False


'''
@see: 修改任务
@since: 2018年4月12日 17:25:59
@author: 孙留平
'''


def update_task( updateTaskDict, username = None, password = None , toCheckMessage = None ):
    Log.LogOutput( LogLevel.INFO, "=====修改策略开始=====" )
    url = "/taskPloyManage/updateTaskPloy";
    
    # 现根据旧名字查询到待修改的ID
    toUpdateId = get_id_by_name( updateTaskDict['oldEname'], username, password )
    updateTaskDict['id'] = toUpdateId
    
    response = QuanKeCaiJiHttpCommon.quan_ke_cai_ji_21200_post( url, updateTaskDict, username = username, password = password )
    
    # 如果有要检查的内容，则根据实际情况检查
    if toCheckMessage is not None:
        return Util.checkMessageExistsInAnotherMessage( toCheckMessage, response.text )
    # 否则，就根据报文结果判断正误
    else:
        if response.result is True:
            Log.LogOutput( LogLevel.INFO, "=====修改任务成功=====" )
            return True
        else:
            Log.LogOutput( LogLevel.ERROR, "=====修改任务失败=====" )
            return False


'''
@see: 批量 删除策略
@since: 2018年4月8日 17:09:01
@author: 孙留平
'''


def delete_batch_by_id( deleteTaskDict, username = None, password = None , toCheckMessage = None ):
    Log.LogOutput( LogLevel.INFO, "=====批量删除任务开始=====" )
    
    url = "/taskManage/deleteTasks";
    response = QuanKeCaiJiHttpCommon.quan_ke_cai_ji_21200_post( url, deleteTaskDict, username = username, password = password )
    
    # 如果有要检查的内容，则根据实际情况检查
    if toCheckMessage is not None:
        return Util.checkMessageExistsInAnotherMessage( toCheckMessage, response.text )
    # 否则，就根据报文结果判断正误
    else:
        if response.result is True:
            Log.LogOutput( LogLevel.INFO, "=====批量删除任务成功=====" )
            return True
        else:
            Log.LogOutput( LogLevel.ERROR, "=====批量删除任务失败=====" )
            return False


'''
@see: 批量 删除策略-根据名称
@since: 2018年4月12日 11:14:19
@author: 孙留平
'''


def delete_batch_by_name( names, username = None, password = None , toCheckMessage = None ):
    Log.LogOutput( LogLevel.INFO, "=====批量删除策略开始=====" )
    
    toDeleteIds = get_id_by_name( names, username, password )
    
    toDeleteDicts = copy.deepcopy( PolicyPara.deletePolicyDict )
    toDeleteDicts['ids[]'] = toDeleteIds
    return delete_batch_by_id( toDeleteDicts, username, password )

            
'''
@see: 单个删除策略——name
@since: 2018年4月8日 17:09:01
@author: 孙留平
'''


def delete_single_by_name( toDeleteName, username = None, password = None , toCheckMessage = None ):
    Log.LogOutput( LogLevel.INFO, "=====根据策略名称单个删除任务开始=====" )
    
    # 先根据策略名字找策略ID
    id = get_id_by_name( toDeleteName )
    deleteListDict = {}
    deleteListDict['id'] = id
    url = "/taskManage/deleteTask?id=%s" % id
    response = QuanKeCaiJiHttpCommon.quan_ke_cai_ji_21200_post( url, deleteListDict, username = username, password = password )
    
    # 如果有要检查的内容，则根据实际情况检查
    if toCheckMessage is not None:
        return Util.checkMessageExistsInAnotherMessage( toCheckMessage, response.text )
    # 否则，就根据报文结果判断正误
    else:
        if response.result is True:
            Log.LogOutput( LogLevel.INFO, "=====根据策略名称单个删除任务成功=====" )
            return True
        else:
            Log.LogOutput( LogLevel.ERROR, "=====根据策略名称单个删除任务失败=====" )
            return False

        
'''
@see: 根据名字查找ID
@since: 2018年4月9日 14:59:35
@param policyName: 如果是单个就传串，如果是多个就传list
@author: 孙留平
'''          


def get_id_by_name( name, existsListDicts = None, username = None, password = None ):
    Log.LogOutput( LogLevel.INFO, "=====根据名称【%s】查找任务=====" % name )
    if existsListDicts is None:
        existsListDicts = get_list_dict( username, password )
    
    # 如果列表中什么都没有
    if len( existsListDicts ) == 0:
        Log.LogOutput( LogLevel.INFO, "=====列表中没有任何数据=====" )
        return None
    
    # 如果是一个名字，找到就撤出
    if type( name ) == str:
        for eachItem in existsListDicts:
            if eachItem['taskDO']['name'] == name :
                Log.LogOutput( LogLevel.DEBUG, "=====找到name为【%s】的ID是【%s】=====" % ( name, eachItem['taskPloyDO']['id'] ) )
                return eachItem['taskDO']['id']
            
        Log.LogOutput( LogLevel.ERROR, "=====没有找到名称为【%s】的策略=====" % name )
        return None
    
    if type( name ) == list:
        idList = []
        
        for eachName in name:
            for eachItem in existsListDicts:
                if eachItem['taskDO']['name'] == eachName:
                    idList.append( eachItem['taskDO']['id'] )
                    continue
                
        return idList
    
    Log.LogOutput( LogLevel.ERROR, "=====policyName参数传入类型不正确=====" )
    return None


'''
@see: 单个删除策略
@since: 2018年4月8日 17:09:01
@author: 孙留平
'''


def delete_single_by_id( id, username = None, password = None , toCheckMessage = None ):
    Log.LogOutput( LogLevel.INFO, "=====单个删除策略开始=====" )
    
    # 先根据策略名字找策略ID
    deleteListDict = {}
    deleteListDict['id'] = id
    url = "/taskManage/deleteTask?id=%s" % id;
    response = QuanKeCaiJiHttpCommon.quan_ke_cai_ji_21200_post( url, deleteListDict, username = username, password = password )
    
    # 如果有要检查的内容，则根据实际情况检查
    if toCheckMessage is not None:
        return Util.checkMessageExistsInAnotherMessage( toCheckMessage, response.text )
    # 否则，就根据报文结果判断正误
    else:
        if response.result is True:
            Log.LogOutput( LogLevel.INFO, "=====单个删除策略成功=====" )
        else:
            Log.LogOutput( LogLevel.ERROR, "=====单个删除策略失败=====" )

            
'''
@see:获取策略列表
@since:  2018年4月8日 17:29:27
@author: 孙留平
'''


def get_list( searchListDict = None, username = None, password = None ):
    Log.LogOutput( LogLevel.INFO, "=====查询列表开始=====" )
    
    url = "/taskPloyManage/findTaskPloyList";
    if searchListDict is None:
        postData = PolicyPara.searchPolicyListDict
    else:
        postData = searchListDict
        
    response = QuanKeCaiJiHttpCommon.quan_ke_cai_ji_21200_post( url, postData, username = username, password = password )
    
    if response.result is True:
        Log.LogOutput( LogLevel.INFO, "=====查询列表成功=====" )
    else:
        Log.LogOutput( LogLevel.ERROR, "=====查询列表失败=====" )
    
    return response


'''
@see:搜索列表
@since:  2018年4月12日 13:38:24
@author: 孙留平
'''


def search_by_ename( toSearchEname, username = None, password = None ):
    postData = copy.deepcopy( TaskPara.searchListDict )
    postData['taskDO.name'] = toSearchEname
    return get_list_dict( postData, username, password )


'''
@see:获取策略列表DICT
@since:  2018年4月9日 15:15:32
@author: 孙留平
'''


def get_list_dict( searchListDict = None, username = None, password = None ):
    existList = get_list( searchListDict, username, password )
    responseDict = json.loads( existList.text )
    dictList = responseDict['rows']
    return dictList


'''
@功能： 在列表中查看记录
username:用户名
password:密码
@return: 查找成功返回True
'''    


def check_in_list( toCheckDict, existListDict = None , username = None, password = None ):
    Log.LogOutput( LogLevel.INFO, "=====检查列表中是否存在某记录=====" )
    
    if existListDict is None:
        existListDict = get_list_dict( username = username, password = password )
    
    for eachInfo in existListDict:
        dictList = []
        dictList.append( eachInfo['taskDO'] )
        
        if Util.checkExactDictInDictList( toCheckDict, dictList ):
            Log.LogOutput( LogLevel.INFO, "=====在列表中检查到待查记录=====" )
            return True
        
    Log.LogOutput( LogLevel.ERROR, "=====在列表中没有检查到待查记录=====" )
    return False


'''
@功能： 刷新列表
username:用户名
password:密码
@return: 刷新成功返回True
'''    


def refresh_list( username = None, password = None ):
    return get_list_dict( None, username, password )


'''
@see: 删除所有记录
@since:2018年4月8日 18:37:56
@author: 孙留平
'''


def clear_list( username = None, password = None ):
    searchListDict = copy.deepcopy( TaskPara.searchListDict )
    searchListDict['rows'] = 2000
    listResponse = get_list( searchListDict, username, password )
    
    listDict = Util.getValueByKeyFromJson( 'rows', listResponse.text )
    
    listNum = len( listDict )
    if 0 == listNum:
        Log.LogOutput( LogLevel.INFO, "=====列表没有数据不需要删除=====" )
        return True
    
    toDeleteIDs = []
    for eachPolicy in listDict:
        eachId = eachPolicy['taskDO']['id']
        toDeleteIDs.append( eachId )
        
    toDeleteDict = copy.deepcopy( TaskPara.deleteDict )
    toDeleteDict['ids[]'] = toDeleteIDs                   
    return delete_batch_by_id( toDeleteDict, username, password , 'true' )
