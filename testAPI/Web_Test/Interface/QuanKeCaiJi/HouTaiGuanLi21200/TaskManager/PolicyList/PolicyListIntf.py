# -*- coding:UTF-8 -*-
'''
Created on 2018年1月4日11:04:48

@author: slp
'''
'''
@see: 添加策略
@since: 2018年4月8日 17:03:25
@author: 孙留平
'''

import copy
import json

from Web_Test.COMMON import Log, Util
from Web_Test.CONFIG.Define import LogLevel
from Web_Test.Interface.QuanKeCaiJi.HouTaiGuanLi21200.TaskManager.PolicyList import PolicyPara
from Web_Test.Interface.QuanKeCaiJi.common import QuanKeCaiJiHttpCommon

'''
@see: 添加策略
@since: 2018年4月12日 18:51:00
@author: 孙留平
'''


def add_policy( addPolicyListDict, username = None, password = None , toCheckMessage = None ):
    Log.LogOutput( LogLevel.INFO, "=====添加策略开始=====" )
    
    url = "/taskPloyManage/addTaskPloy";
    response = QuanKeCaiJiHttpCommon.quan_ke_cai_ji_21200_post( url, addPolicyListDict, username = username, password = password )
    
    # 如果有要检查的内容，则根据实际情况检查
    if toCheckMessage is not None:
        return Util.checkMessageExistsInAnotherMessage( toCheckMessage, response.text )
    # 否则，就根据报文结果判断正误
    else:
        if response.result is True:
            Log.LogOutput( LogLevel.INFO, "=====添加策略成功=====" )
            return True
        else:
            Log.LogOutput( LogLevel.ERROR, "=====添加策略失败=====" )
            return False


'''
@see: 修改策略
@since: 2018年4月12日 14:11:27
@author: 孙留平
'''


def update_policy( updatePolicyListDict, username = None, password = None , toCheckMessage = None ):
    Log.LogOutput( LogLevel.INFO, "=====修改策略开始=====" )
    url = "/taskPloyManage/updateTaskPloy";
    
    # 现根据旧名字查询到待修改的ID
    toUpdatePolicyId = get_policy_id_by_name( updatePolicyListDict['oldEname'], username, password )
    updatePolicyListDict['id'] = toUpdatePolicyId
    
    response = QuanKeCaiJiHttpCommon.quan_ke_cai_ji_21200_post( url, updatePolicyListDict, username = username, password = password )
    
    # 如果有要检查的内容，则根据实际情况检查
    if toCheckMessage is not None:
        return Util.checkMessageExistsInAnotherMessage( toCheckMessage, response.text )
    # 否则，就根据报文结果判断正误
    else:
        if response.result is True:
            Log.LogOutput( LogLevel.INFO, "=====修改策略成功=====" )
            return True
        else:
            Log.LogOutput( LogLevel.ERROR, "=====修改策略失败=====" )
            return False


'''
@see: 批量 删除策略
@since: 2018年4月8日 17:09:01
@author: 孙留平
'''


def delete_policy_batch_by_id( deletePolicyListDict, username = None, password = None , toCheckMessage = None ):
    Log.LogOutput( LogLevel.INFO, "=====批量删除策略开始=====" )
    
    url = "/taskPloyManage/deleteTaskPloys";
    response = QuanKeCaiJiHttpCommon.quan_ke_cai_ji_21200_post( url, deletePolicyListDict, username = username, password = password )
    
    # 如果有要检查的内容，则根据实际情况检查
    if toCheckMessage is not None:
        return Util.checkMessageExistsInAnotherMessage( toCheckMessage, response.text )
    # 否则，就根据报文结果判断正误
    else:
        if response.result is True:
            Log.LogOutput( LogLevel.INFO, "=====批量删除策略成功=====" )
            return True
        else:
            Log.LogOutput( LogLevel.ERROR, "=====批量删除策略失败=====" )
            return False


'''
@see: 批量 删除策略-根据名称
@since: 2018年4月12日 11:14:19
@author: 孙留平
'''


def delete_policy_batch_by_name( deletePolicyListNames, username = None, password = None , toCheckMessage = None ):
    Log.LogOutput( LogLevel.INFO, "=====批量删除策略开始=====" )
    
    toDeletePolicyIds = get_policy_id_by_name( deletePolicyListNames, username, password )
    
    toDeletePolicyDicts = copy.deepcopy( PolicyPara.deletePolicyDict )
    toDeletePolicyDicts['ids[]'] = toDeletePolicyIds
    return delete_policy_batch_by_id( toDeletePolicyDicts, username, password )

            
'''
@see: 单个删除策略——name
@since: 2018年4月8日 17:09:01
@author: 孙留平
'''


def delete_policy_single_by_name( toDeletePolicyName, username = None, password = None , toCheckMessage = None ):
    Log.LogOutput( LogLevel.INFO, "=====根据策略名称单个删除策略开始=====" )
    
    # 先根据策略名字找策略ID
    policyId = get_policy_id_by_name( toDeletePolicyName )
    
    deletePolicyListDict = {}
    deletePolicyListDict['id'] = policyId
    url = "/taskPloyManage/deleteTaskPloy?id=%s" % policyId
    response = QuanKeCaiJiHttpCommon.quan_ke_cai_ji_21200_post( url, deletePolicyListDict, username = username, password = password )
    
    # 如果有要检查的内容，则根据实际情况检查
    if toCheckMessage is not None:
        return Util.checkMessageExistsInAnotherMessage( toCheckMessage, response.text )
    # 否则，就根据报文结果判断正误
    else:
        if response.result is True:
            Log.LogOutput( LogLevel.INFO, "=====根据策略名称单个删除策略成功=====" )
            return True
        else:
            Log.LogOutput( LogLevel.ERROR, "=====根据策略名称单个删除策略失败=====" )
            return False

        
'''
@see: 根据名字查找ID(英文或者中文任何一个匹配上就返回)，优先查找ename
@since: 2018年4月9日 14:59:35
@param policyName: 如果是单个就传串，如果是多个就传list
@author: 孙留平
'''          


def get_policy_id_by_name( policyName, existsPolicyListDict = None, username = None, password = None ):
    Log.LogOutput( LogLevel.INFO, "=====根据策略名称【%s】查找策略=====" % policyName )
    if existsPolicyListDict is None:
        existsPolicyListDict = get_policy_list_dict( username, password )
    
    # 如果列表中什么都没有
    if len( existsPolicyListDict ) == 0:
        Log.LogOutput( LogLevel.INFO, "=====策略列表中没有任何策略=====" )
        return None
    
    # 如果是一个名字，找到就撤出
    if type( policyName ) == str:
        for eachItem in existsPolicyListDict:
            if eachItem['taskPloyDO']['ename'] == policyName :
                Log.LogOutput( LogLevel.DEBUG, "=====找到ename为【%s】的ID是【%s】=====" % ( policyName, eachItem['taskPloyDO']['id'] ) )
                return eachItem['taskPloyDO']['id']
            
            if eachItem['taskPloyDO']['cname'] == policyName:
                Log.LogOutput( LogLevel.DEBUG, "=====找到cname为【%s】的ID是【%s】=====" % ( policyName, eachItem['taskPloyDO']['id'] ) )
                return eachItem['taskPloyDO']['id']
        Log.LogOutput( LogLevel.ERROR, "=====没有找到ename或者cname为【%s】的策略=====" % policyName )
        return None
    
    if type( policyName ) == list:
        idList = []
        
        for eachName in policyName:
            for eachItem in existsPolicyListDict:
                if eachItem['taskPloyDO']['ename'] == eachName:
                    idList.append( eachItem['taskPloyDO']['id'] )
                    continue
                
                if eachItem['taskPloyDO']['cname'] == eachName:
                    idList.append( eachItem['taskPloyDO']['id'] )
                    continue
                
        return idList
    
    Log.LogOutput( LogLevel.ERROR, "=====policyName参数传入类型不正确=====" )
    return None


'''
@see: 单个删除策略
@since: 2018年4月8日 17:09:01
@author: 孙留平
'''


def delete_policy_single_by_id( toDeletePolicyId, username = None, password = None , toCheckMessage = None ):
    Log.LogOutput( LogLevel.INFO, "=====单个删除策略开始=====" )
    
    # 先根据策略名字找策略ID
    
    deletePolicyListDict = {}
    deletePolicyListDict['id'] = id
    url = "/taskPloyManage/deleteTaskPloy?id=%s" % id;
    response = QuanKeCaiJiHttpCommon.quan_ke_cai_ji_21200_post( url, deletePolicyListDict, username = username, password = password )
    
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


def get_policy_list( searchPolicyListDict = None, username = None, password = None ):
    Log.LogOutput( LogLevel.INFO, "=====查询策略列表开始=====" )
    
    url = "/taskPloyManage/findTaskPloyList";
    if searchPolicyListDict is None:
        postData = PolicyPara.searchPolicyListDict
    else:
        postData = searchPolicyListDict
        
    response = QuanKeCaiJiHttpCommon.quan_ke_cai_ji_21200_post( url, postData, username = username, password = password )
    
    if response.result is True:
        Log.LogOutput( LogLevel.INFO, "=====查询策略列表成功=====" )
    else:
        Log.LogOutput( LogLevel.ERROR, "=====查询策略列表失败=====" )
    
    return response


'''
@see:搜索策略列表
@since:  2018年4月12日 13:38:24
@author: 孙留平
'''


def search_policy_by_ename( toSearchEname, username = None, password = None ):
    postData = copy.deepcopy( PolicyPara.searchPolicyListDict )
    postData['taskPloyDO.ename'] = toSearchEname
    return get_policy_list_dict( postData, username, password )


'''
@see:获取策略列表DICT
@since:  2018年4月9日 15:15:32
@author: 孙留平
'''


def get_policy_list_dict( searchPolicyListDict = None, username = None, password = None ):
    existPolicyList = get_policy_list( searchPolicyListDict, username, password )
    responseDict = json.loads( existPolicyList.text )
    dictList = responseDict['rows']
    return dictList


'''
@功能： 在策略列表中查看列表 
username:用户名
password:密码
@return: 查找成功返回True
'''    


def check_policy_in_list( toCheckPolicyDict, existPolicyListDict = None , username = None, password = None ):
    Log.LogOutput( LogLevel.INFO, "=====检查策略列表中是否存在策略开始=====" )
    
    if existPolicyListDict is None:
        existPolicyListDict = get_policy_list_dict( username = username, password = password )
    
    for eachPolicyInfo in existPolicyListDict:
        dictList = []
        dictList.append( eachPolicyInfo['taskPloyDO'] )
        
        if Util.checkExactDictInDictList( toCheckPolicyDict, dictList ):
            Log.LogOutput( LogLevel.INFO, "=====在策略列表中检查到策略=====" )
            return True
        
    Log.LogOutput( LogLevel.ERROR, "=====在策略列表中没有检查到策略=====" )
    return False


'''
@功能： 刷新策略列表
username:用户名
password:密码
@return: 刷新成功返回True
'''    


def refresh_policy_list( username = None, password = None ):
    return get_policy_list_dict( None, username, password )


'''
@see: 删除所有策略
@since:2018年4月8日 18:37:56
@author: 孙留平
'''


def clear_policy_list( username = None, password = None ):
    searchPolicyListDict = copy.deepcopy( PolicyPara.searchPolicyListDict )
    searchPolicyListDict['rows'] = 2000
    policyListResponse = get_policy_list( searchPolicyListDict, username, password )
    
    policyListDict = Util.getValueByKeyFromJson( 'rows', policyListResponse.text )
    
    listNum = len( policyListDict )
    if 0 == listNum:
        Log.LogOutput( LogLevel.INFO, "=====策略列表没有数据不需要删除=====" )
        return True
    
    toDeleteIDs = []
    for eachPolicy in policyListDict:
        eachId = eachPolicy['taskPloyDO']['id']
        toDeleteIDs.append( eachId )
        
    toDeletePolicyDict = copy.deepcopy( PolicyPara.deletePolicyDict )
    toDeletePolicyDict['ids[]'] = toDeleteIDs                   
    return delete_policy_batch_by_id( toDeletePolicyDict, username, password , 'true' )
