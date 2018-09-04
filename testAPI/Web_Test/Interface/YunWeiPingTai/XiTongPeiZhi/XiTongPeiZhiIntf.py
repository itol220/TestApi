# -*- coding:UTF-8 -*-
'''
Created on 2015-11-24

@author: N-133
'''
from __future__ import unicode_literals
from COMMON import Log, CommonUtil
from COMMON.CommonUtil import findDictInDictlist
from CONFIG import InitDefaultPara
from CONFIG.Define import LogLevel
from CONFIG.InitDefaultPara import clueOrgInit
from Interface.YunWeiPingTai.XiTongPeiZhi import XiTongPeiZhiPara
from Interface.YunWeiPingTai.XiTongPeiZhi.XiTongPeiZhiPara import InfoType
from Interface.YunWeiPingTai.XinXiGuanLi import XinXiGuanLiPara
from Interface.YunWeiPingTai.YunWeiCommon import YunWeiCommonIntf
from Interface.YunWeiPingTai.yunWeiPingTaiHttpCommon import xiansuoyunwei_post, \
    xiansuoyunwei_get
import copy
import json


'''  
    @功能： 新增敏感词配置
    @para: 
    addKeywordSettingPara：个性化配置字典，请调用XiTongPeiZhiPara中的addKeywordSettingPara
    @return: 新增成功，返回True；否则返回False  
''' 
def add_keyword_setting(addKeywordSettingPara):
    Log.LogOutput(LogLevel.INFO, "新增关键字开始")
    response = xiansuoyunwei_post(url='/keyWordSettingManage/addkeyWordSetting', postdata=addKeywordSettingPara)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增关键字成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, "新增关键字失败")
        return False

'''  
    @功能：删除所有敏感词配置
    @para: 
    @return: 新增成功，返回True；否则返回False  
'''
def delete_all_keyword_setting():
    Log.LogOutput(LogLevel.INFO, "删除所有关键字开始")
    try:
        getKeywordDict = copy.deepcopy(XiTongPeiZhiPara.getKeywordListPara)
        response = xiansuoyunwei_post(url='/keyWordSettingManage/findKeyWordSettingList', postdata=getKeywordDict)
        responseDict = json.loads(response.text)
        if responseDict['records']==0:
            Log.LogOutput(LogLevel.INFO, "关键字列表为空")
            return True
        listDict= responseDict['rows']
        idList = []
        for item in listDict:
            idList.append(item['id'])
        #将list转化为tuple
        deleteIds = tuple(idList)        
        deleteKeywordDict = copy.deepcopy(XiTongPeiZhiPara.deleteKeywordListPara)
        deleteKeywordDict['ids[]']=deleteIds
        response = xiansuoyunwei_post(url='/keyWordSettingManage/deleteKeyWordSettings', postdata=deleteKeywordDict)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "所有关键字删除成功")
            return True
        else:
            Log.LogOutput(LogLevel.INFO, "所有关键字删除失败")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '关键字删除过程失败')
        return False

'''  
    @功能： 修改敏感词配置
    @para: 
    updateKeywordSettingPara：修改个性化配置字典，请调用XiTongPeiZhiPara中的updateKeywordSettingPara
    @return: 新增成功，返回True；否则返回False  
'''

# 修改关键字
def update_keyword_setting(updateKeywordSettingPara):
    Log.LogOutput(LogLevel.INFO, "修改关键字开始......")
    response = xiansuoyunwei_post(url='/keyWordSettingManage/updateKeyWordSetting', postdata=updateKeywordSettingPara)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "修改关键字成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, "修改关键字失败")
        return False

'''  
    @功能： 通过关键字信息获取关键字配置id
    @para: 
    keywordSetting：关键字 
    @return: 如果找到关键字配置，则返回ID，否则返回None  
'''
def get_keyword_setting_id_by_content(keywordSetting):
    Log.LogOutput(LogLevel.INFO, "通过关键字内容获取关键字配置id开始......")
    try:
        getKeywordDict = copy.deepcopy(XiTongPeiZhiPara.getKeywordListPara)
        response = xiansuoyunwei_post(url='/keyWordSettingManage/findKeyWordSettingList', postdata=getKeywordDict)
        responseDict = json.loads(response.text)
        if responseDict['records']==0:
            Log.LogOutput(LogLevel.INFO, "关键字列表为空")
            return None
        for row in responseDict['rows']:
            if row['keyWords'] == keywordSetting:
                Log.LogOutput(LogLevel.INFO, "找到关键字配置，返回ID")
                return row['id']
        Log.LogOutput(LogLevel.INFO, "无法找到关键字配置，返回None")
        return None
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '查找关键字配置过程失败')
        return None

# 查看关键字新增
def chakanBanLiYiJianZT(companyDict):
    try:
        Log.LogOutput(LogLevel.INFO, "查看关键字新增开始")
        compDict = copy.deepcopy(XiTongPeiZhiPara.GuanJianZhi)
        response = xiansuoyunwei_post(url='/keyWordSettingManage/findKeyWordSettingList', postdata=compDict)
        responseDict = json.loads(response.text)
        listDict= responseDict['rows']
        if CommonUtil.findDictInDictlist(companyDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "查看关键字新增成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查看关键字新增失败")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '查看失败')
        return False  

# 修改积分配置
def updateJiFenPeiZhi(para):
    Log.LogOutput(LogLevel.INFO, "修改积分配置开始")
    response = xiansuoyunwei_get(url='/pointsSettingManage/updatePoint', param=para)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "修改积分配置成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "修改积分配置失败")
    return response

# 修改积分规则
def updateJiFenGuiZhe(para):
    Log.LogOutput(LogLevel.INFO, "修改积分规则开始")
    response = xiansuoyunwei_post(url='/pointsRuleManage/updatePointsRule', postdata=para)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "修改积分规则成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "修改积分规则失败")
    return response
#根据departnum获取积分信息
'''
    @功能：获取线索详情
    @return:    response
    @author:  chenhui 2016-03-22
'''  
def getPointRule(para):
    Log.LogOutput(LogLevel.INFO, "获取积分规则信息")
    response = xiansuoyunwei_post(url='/pointsRuleManage/getPointsRuleByDepartmentNo', postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "积分规则获取成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "积分规则获取失败")
    return response
# 开通区县
def openQuXian(para):
    Log.LogOutput(LogLevel.INFO, "开通区县开始")
    response = xiansuoyunwei_post(url='/organizationManage/openOrgState', postdata=para)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "开通区县成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "开通区县失败")
    return response

# 关闭区县
def closeQuXian(para):
    Log.LogOutput(LogLevel.INFO, "关闭区县开始")
    response = xiansuoyunwei_post(url='/organizationManage/closeOrgState', postdata=para)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "关闭区县成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "关闭区县失败")
    return response


# 查看积分配置
def chakanJiFenPeiZhi(companyDict):
    try:
        Log.LogOutput(LogLevel.INFO, "查看积分配置开始")
        compDict = copy.deepcopy(XiTongPeiZhiPara.chakanJiFenPeiZhi)
        response = xiansuoyunwei_post(url='/pointsSettingManage/findPointsSettingList', postdata=compDict)
        responseDict = json.loads(response.text)
        listDict= responseDict['rows']
        if CommonUtil.findDictInDictlist(companyDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "查看积分配置成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查看积分配置失败")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '查看失败')
        return False  

# 查看关于我们页面
def chakanGuanYuWoMen(companyDict):
    try:
        Log.LogOutput(LogLevel.INFO, "查看关于我们页面开始")
        response = xiansuoyunwei_post(url='/systemNoticesManage/getSystemNoticeById')
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(companyDict, [responseDict]) is True:
            Log.LogOutput(LogLevel.DEBUG, "查看关于我们页面成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查看关于我们页面失败")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '查看失败')
        return False  

# 查看积分规则
def chakanJiFenGuiZhe(companyDict,departmentNo=None):
    try:
        Log.LogOutput(LogLevel.INFO, "查看积分规则开始")
        compDict = copy.deepcopy(XiTongPeiZhiPara.chakanJiFenGuiZhe)
        compDict['departmentNo']= clueOrgInit['DftQuOrgDepNo']
        response = xiansuoyunwei_post(url='/pointsRuleManage/getPointsRuleByDepartmentNo',postdata=compDict)
#         print response.text
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(companyDict, [responseDict]) is True:
            Log.LogOutput(LogLevel.DEBUG, "查看积分规则成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查看积分规则失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查看失败')
            return False  

# 查看区县开通
def chakanQuXian(companyDict,parentId=None):
    try:
        Log.LogOutput(LogLevel.INFO, "查看区县开通开始")
        compDict = copy.deepcopy(XiTongPeiZhiPara.chakanJiFenGuiZhe)
        compDict['parentId'] = clueOrgInit['DftQuOrgId']
        response = xiansuoyunwei_post(url='/organizationManage/findOrganizationList',postdata=compDict)
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(companyDict,  [responseDict]) is True:
            Log.LogOutput(LogLevel.DEBUG, "查看区县开通成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查看区县开通失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查看失败')
            return False  

# 查看区县关闭
def chakanQuXianclose(companyDict,parentId=None):
    try:
        Log.LogOutput(LogLevel.INFO, "查看区县关闭开始")
        compDict = copy.deepcopy(XiTongPeiZhiPara.chakanJiFenGuiZhe)
        compDict['parentId'] = clueOrgInit['DftQuOrgId']
        response = xiansuoyunwei_post(url='/organizationManage/findOrganizationList',postdata=compDict)
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(companyDict,  [responseDict]) is True:
            Log.LogOutput(LogLevel.DEBUG, "查看区县关闭成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查看区县关闭失败")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '查看失败')
        return False  

def deleteXiTongPeiZhi():
    try:
# 删除关键字        
        Log.LogOutput(message='正在清空所有关键字数据...')
        listPara = copy.deepcopy(XiTongPeiZhiPara.GuanJianZhi)
#         print listPara
        response = xiansuoyunwei_post(url='/keyWordSettingManage/findKeyWordSettingList', postdata=listPara)
#         print response.text
        responseDict = json.loads(response.text)
        if responseDict['records'] == 0:
            Log.LogOutput(LogLevel.DEBUG, '列表数据为空')
        else:
            #存储所有ID
            arr=[]
            for dictListItem in responseDict['rows']:
                arr.append(dictListItem['id'])
            deleteDict = {'ids[]':tuple(arr)}
#             print deleteDict
            response=xiansuoyunwei_post(url='/keyWordSettingManage/deleteKeyWordSettings',postdata=deleteDict)
            if response.result is True:
                Log.LogOutput(LogLevel.INFO, '*删除成功*')
            else:
                Log.LogOutput(LogLevel.ERROR, '删除失败!')   

# 删除线索        
        Log.LogOutput(message='正在清空所有线索数据...')
        listPara = copy.deepcopy(XinXiGuanLiPara.chakanxiansuo)
        response = xiansuoyunwei_post(url='/informationManage/findInformationList', postdata=listPara)
        responseDict = json.loads(response.text)
        if responseDict['records'] == 0:
            Log.LogOutput(LogLevel.DEBUG, '列表数据为空')
        else:
            #存储所有ID
            arr=[]
            for dictListItem in responseDict['rows']:
                arr.append(dictListItem['information']['id'])
            deleteDict = {'ids[]':tuple(arr)}
            response=xiansuoyunwei_post(url='/informationManage/deleteInformations',postdata=deleteDict)
            if response.result is True:
                Log.LogOutput(LogLevel.INFO, '*删除成功*')
            else:
                Log.LogOutput(LogLevel.ERROR, '删除失败!')   
                
    except Exception :
        Log.LogOutput(LogLevel.ERROR, '删除异常')
        return False
    
'''
    @功能： 获取积分配置
    @para: 
    @return: 
    @author:  chenhui 2016-09-30
'''
def getPointRuleId(para):
    Log.LogOutput(LogLevel.INFO, "获取规则")
    response = xiansuoyunwei_post(url='/pointsRuleManage/getPointsRuleByDepartmentNo',postdata=para)
    responseDict = json.loads(response.text)
    return responseDict['id']

'''  
    @功能： 新增爆料主题
    @para: 
    themeAddDict：主题新增字典，请调用XiTongPeiZhiPara中的themeAddDict
    @return: 新增成功，返回主题id；否则返回False  
'''

def add_theme(themeAddDict):
    Log.LogOutput(LogLevel.INFO, "新增主题")
    response = xiansuoyunwei_post(url='/themeManage/addThemeManage',postdata=themeAddDict)
#     print response.text
    if response.result is True:
        responseDict = json.loads(response.text)
        Log.LogOutput(LogLevel.INFO, "新增主题成功")
        return responseDict['id']
    else:
        Log.LogOutput(LogLevel.INFO, "新增主题失败")
        return False

'''  
    @功能： 新增主题
    @para: 
    themeAddDict：主题新增字典，请调用XiTongPeiZhiPara中的themeAddDict
    @return: 新增成功，返回主题id；否则返回False  
'''

def add_theme2(themeAddDict):
    info='新增主题'
    Log.LogOutput(LogLevel.INFO, info+"开始")
    response = xiansuoyunwei_post(url='/themeManage/addThemeManage',postdata=themeAddDict)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功")
    else:
        Log.LogOutput(LogLevel.WARN, info+"失败")
    return response
       
'''  
    @功能： 修改主题
    @para: XiTongPeiZhiPara.themeUpdPara
    @return: response
    @author:    chenhui 2016-12-22
'''    

def upd_theme(para=None):
    info='修改主题'
    Log.LogOutput(LogLevel.INFO, info+"开始")
    response = xiansuoyunwei_post(url='/themeManage/updateThemeManage',postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功")
    else:
        Log.LogOutput(LogLevel.WARN, info+"失败")
    return response
    
'''  
    @功能： 开启/关闭主题
    @para: XiTongPeiZhiPara.updThemeStatePara
    @return: response
    @author:    chenhui 2016-12-22
'''    

def upd_theme_state(para=None):
    info='开启/关闭主题'
    Log.LogOutput(LogLevel.INFO, info+"开始")
    response = xiansuoyunwei_post(url='/themeManage/updateState',postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功")
    else:
        Log.LogOutput(LogLevel.WARN, info+"失败")
    return response

'''
    @功能： 通过主题名称获取排序号
    @para:     
                    name        #主题名称
                    inforType  #主题类别，0爆料；5说说
    @return:  如果找到，返回排列序号，如果没找到，则返回-1，如果异常，返回-2
    @author:  chenhui 2016-12-23
'''
def get_theme_seq_by_name(name,inforType,departmentNo=InitDefaultPara.clueOrgInit['DftQuOrgDepNo']):
    info='通过主题名称获取排序号'
    Log.LogOutput(LogLevel.INFO, info)
    listpara=copy.deepcopy(XiTongPeiZhiPara.themeListPara)
    listpara['themeRelation.infoType']=inforType
    listpara['themeRelation.departmentNo']=departmentNo
    try:
        response = get_theme_list(para=listpara)
        resDict=json.loads(response.text)
#         print response.text
        for item in resDict['rows']:
            if item['themeContent']['name']==name:
                Log.LogOutput(LogLevel.INFO, info+'成功')
                return item['themeRelation']['seq']
        Log.LogOutput(LogLevel.INFO, info+'失败')
        return -1 
    except Exception:
        Log.LogOutput(LogLevel.ERROR, info+'出现异常')
        return -2

'''
    @功能： 通过主题名称获取排序号
    @para:     
                    name        #主题名称
                    inforType  #主题类别，0爆料；5说说
    @return:  如果找到，返回排列序号，如果没找到，则返回-1，如果异常，返回-2
    @author:  chenhui 2016-12-23
'''
def get_theme_id_by_name(name,inforType,departmentNo=InitDefaultPara.clueOrgInit['DftQuOrgDepNo']):
    info='通过主题名称获取排id'
    Log.LogOutput(LogLevel.INFO, info)
    listpara=copy.deepcopy(XiTongPeiZhiPara.themeListPara)
    listpara['themeRelation.infoType']=inforType
    listpara['themeRelation.departmentNo']=departmentNo
    try:
        response = get_theme_list(para=listpara)
        resDict=json.loads(response.text)
#         print response.text
        for item in resDict['rows']:
            if item['themeContent']['name']==name:
                Log.LogOutput(LogLevel.INFO, info+'成功')
                return item['themeRelation']['id']
        Log.LogOutput(LogLevel.INFO, info+'失败')
        return -1 
    except Exception:
        Log.LogOutput(LogLevel.ERROR, info+'出现异常')
        return -2
    
'''  
    @功能： 移动主题
    @para: XiTongPeiZhiPara.moveThemePara
    @return: response
    @author:    chenhui 2016-12-23
'''    

def move_theme(para=None):
    info='移动主题'
    Log.LogOutput(LogLevel.INFO, info+"开始")
    response = xiansuoyunwei_post(url='/themeManage/moveThemeManage',postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功")
    else:
        Log.LogOutput(LogLevel.WARN, info+"失败")
    return response
   
'''  
    @功能： 根据themeContentsId获取themeRelationId
    @para:     {
                    'themeContentsId':'',
                    'infoType':''#0爆料，5畅聊说说
                    }
    @return:  失败返回-1，异常返回-2，正常返回数值
    @author:    chenhui 2016-12-23
'''    
def get_themeRelationId_by_themeContentsId(para=None):
    info='根据themeContentsId获取themeRelationId'
    Log.LogOutput(LogLevel.INFO, info+"开始")
    try:
        listpara=copy.deepcopy(XiTongPeiZhiPara.themeListPara)
        listpara['themeRelation.infoType']=para['infoType']
        response = get_theme_list(para=listpara)
#         print response.text
        resDict=json.loads(response.text)
        for item in resDict['rows']:
            if item['themeRelation']['themeContentsId']==para['themeContentsId']:
                return item['themeRelation']['id']
        return -1
    except:
        return -2

'''  
    @功能： 更新是否热门状态
    @para: XiTongPeiZhiPara.updHotStatePara
    @return: response
    @author:    chenhui 2016-12-22
'''    

def upd_hot_state(para=None):
    info='更新是否热门状态'
    Log.LogOutput(LogLevel.INFO, info+"开始")
    response = xiansuoyunwei_post(url='/themeManage/updateIsHotState',postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功")
    else:
        Log.LogOutput(LogLevel.WARN, info+"失败")
    return response
  
'''  
    @功能： PC端获取主题列表
    @para: XiTongPeiZhiPara.themeListPara
    @return: response
    @author:    chenhui 2016-12-22
'''    

def get_theme_list(para=None):
    info='PC端获取主题列表'
    Log.LogOutput(LogLevel.INFO, info+"开始")
    response = xiansuoyunwei_post(url='/themeManage/findThemeManageList',postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功")
    else:
        Log.LogOutput(LogLevel.WARN, info+"失败")
    return response

'''
    @功能： PC端主题检查列表
    @para:    listpara:    XiTongPeiZhiPara.themeListPara
                    checkpara: XiTongPeiZhiPara.themeListCheckPara
    @return: response
    @author:  chenhui 2016-12-22
'''
def check_theme_list(listpara,checkpara):
    info='PC端主题检查列表'
    Log.LogOutput(LogLevel.INFO, info)
    try:
        response = get_theme_list(para=listpara)
        responseDict=json.loads(response.text)
#         print response.text
        #拼接待检查列表
        arr=[]
        #待检查字典
        
        for item in responseDict['rows']:
            dict=copy.deepcopy(XiTongPeiZhiPara.themeListCheckPara)
            dict['themeContentsId']=item['themeContent']['id']
            dict['state']=item['themeRelation']['state']
            dict['isHotState']=item['themeRelation']['isHotState']
            dict['infoType']=item['themeRelation']['infoType']
            dict['name']=item['themeContent']['name']
            dict['description']=item['themeContent']['description']
            arr.append(dict)
#         print arr
        if findDictInDictlist(checkpara,arr) is True:
            Log.LogOutput(LogLevel.DEBUG, info+"成功!")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, info+'出现异常')
        return False

'''  
    @功能： 删除所有爆料和说说主题中包含“autotest”开头的主题
    @para: XiTongPeiZhiPara.themeListPara
    @return: response
    @author:    chenhui 2016-12-22
'''    

def del_all_theme():
    Log.LogOutput( message='通过数据库删除所有autotest开头的爆料和说说主题')
    YunWeiCommonIntf.exeDbQueryYunWei(dbCommand = "delete from themerelations  t where t.themeContentsId in (select id from themeContents th where th.name like 'AUTOTEST_%')")
    YunWeiCommonIntf.exeDbQueryYunWei(dbCommand = "delete from themeContents th where th.name like 'AUTOTEST_%'")

#     Log.LogOutput(LogLevel.INFO, info+"开始")
#     themeListPara=copy.deepcopy(XiTongPeiZhiPara.themeListPara)
#     themeListPara['themeRelation.infoType']=InfoType.BAOLIAO
#     response=get_theme_list(themeListPara)
#     resDict=json.loads(response.text)
#     for item in resDict['rows']:
#         themeContentsId=item['themeContent']['id']
#         #清除自动化省下的
#         YunWeiCommonIntf.exeDbQueryYunWei(dbCommand = "delete from themerelations  t where t.themeContentsId = '%s' "%themeContentsId)
#         #清除自动化省下的主题内容
#         YunWeiCommonIntf.exeDbQueryYunWei(dbCommand = "delete from themecontents  t where t.id = '%s' "%themeContentsId)
#         
#     themeListPara['themeRelation.infoType']=InfoType.SHUOSHUO
#     response=get_theme_list(themeListPara)
#     resDict=json.loads(response.text)
#     for item in resDict['rows']:
#         themeContentsId=item['themeContent']['id']
#         #清除自动化省下的
#         YunWeiCommonIntf.exeDbQueryYunWei(dbCommand = "delete from themerelations  t where t.themeContentsId = '%s' "%themeContentsId)
#         #清除自动化省下的主题内容
#         YunWeiCommonIntf.exeDbQueryYunWei(dbCommand = "delete from themecontents  t where t.id = '%s' "%themeContentsId)
    
'''  
    @功能： 新增个性化配置
    @para: 
    addPersonalConfigPara：个性化配置字典，请调用XiTongPeiZhiPara中的addPersonalConfigPara
    @return: 新增成功，返回True；否则返回False  
'''    

def add_personal_config(addPersonalConfigPara=None):
    Log.LogOutput(LogLevel.INFO, "新增个性化配置")
    response = xiansuoyunwei_post(url='/personalizedConfiguration/addPersonalizedConfiguration',postdata=addPersonalConfigPara)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增个性化配置成功")
        return True
    else:
        Log.LogOutput(LogLevel.WARN, "新增个性化配置失败")
        return False

'''  
    @功能： 新增个性化配置
    @para: 
    addPersonalConfigPara：个性化配置字典，请调用XiTongPeiZhiPara中的addPersonalConfigPara
    @return: response
'''    

def add_personal_config2(addPersonalConfigPara=None):
    Log.LogOutput(LogLevel.INFO, "新增个性化配置")
    response = xiansuoyunwei_post(url='/personalizedConfiguration/addPersonalizedConfiguration',postdata=addPersonalConfigPara)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增个性化配置成功")
    else:
        Log.LogOutput(LogLevel.WARN, "新增个性化配置失败")
    return response


'''  
    @功能： 修改个性化配置
    @para：XiTongPeiZhiPara.updPersonalConfigListPara
    @return: response
    @author: chenhui 2016-12-6
'''    

def upd_personal_config(para=None):
    Log.LogOutput(LogLevel.INFO, "修改个性化配置")
    response = xiansuoyunwei_post(url='/personalizedConfiguration/updatePersonalizedConfiguration',postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "修改个性化配置成功")
    else:
        Log.LogOutput(LogLevel.WARN, "修改个性化配置失败")
    return response
   
'''
    @功能： 获取个性化配置
    @para:  {'ids[]':''}
    @return: response
    @author:  chenhui 2016-12-6
'''
def delete_personal_config(para):
    info='删除个性化配置'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/personalizedConfiguration/deletePersonalizedConfigurations', postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
        Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 获取个性化配置列表
    @para: XiTongPeiZhiPara.personalConfigListPara
    @return: response
    @author:  chenhui 2016-12-6
'''
def get_personal_config_list(para):
    info='获取个性化配置列表'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/personalizedConfiguration/findPersonalizedConfigurationList', postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
        Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 检查个性化配置列表
    @listpara: XiTongPeiZhiPara.personalConfigListPara
        checkpara:XiTongPeiZhiPara.personalConfigListCheckPara
    @return: response
    @author:  chenhui 2016-12-6
'''
def check_personal_config_list(listpara,checkpara):
    try:
        info='检查个性化配置列表'
        Log.LogOutput(LogLevel.INFO, info)
        result=get_personal_config_list(para=listpara)
#         print result.text
        resultDict=json.loads(result.text)
        if resultDict['records']==0:
            Log.LogOutput(LogLevel.INFO, "列表数据为空")
            return False
        listDict= resultDict['rows']
        if findDictInDictlist(checkpara, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, info+"成功!")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, info+'异常')
        return False
        
          
'''
    @功能： 删除所有个性化配置
    @para: 
    @return: response
    @author:  chenhui 2016-12-6
'''
def delete_all_personal_config():
    info='删除所有个性化配置'
    Log.LogOutput(LogLevel.INFO, info)
    try:
        #获取默认配置id
        listPara=copy.deepcopy(XiTongPeiZhiPara.personalConfigListPara)
        response1=get_personal_config_list(listPara)
        resDict1=json.loads(response1.text)
        arr=[]
        if resDict1['records']!=0:
            for item in resDict1['rows']:
                arr.append(item['id'])
        #获取省配置id
        listPara['personalizedConfiguration.departmentNo']=clueOrgInit['DftShengOrgDepNo']
        response2 =get_personal_config_list(listPara)
        resDict2=json.loads(response2.text)
        if resDict2['records']==0 and resDict1['records']==0:
            Log.LogOutput(message='个性化配置数据为0，无需删除')
            return True
        for item in resDict2['rows']:
            arr.append(item['id'])
        #封装所有id
        deleteDict = {'ids[]':tuple(arr)}
        #删除所有的个性化配置
        result=delete_personal_config(deleteDict)
        if result.result==True:
            Log.LogOutput(message=info+"成功")
        else:
            Log.LogOutput(message=info+"失败")
    except Exception,e:
        Log.LogOutput(message=info+"异常"+str(e))

'''
    @功能：    新增角色
    @return:    response
    @param :    XiTongPeiZhiPara.addRolePara
    @author:  chenhui 2017-3-31
'''  
def addRole(para):
    Log.LogOutput(LogLevel.INFO, "新增角色开始...")
    response = xiansuoyunwei_post(url='/base/roleManager/addRole', postdata=para)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增角色成功")
    else:
        Log.LogOutput(LogLevel.DEBUG, "新增角色失败")
    return response 

'''
    @功能：    初始化角色
    @return:    response
    @author:  chenhui 2017-3-31
'''  
def initDefaultRole():
    Log.LogOutput(LogLevel.INFO, "初始化角色开始...")
    roleNameDict={
                  'role.roleName':'线索测试自动化岗位',
                  'roleName':'线索测试自动化岗位',
                  'roleId':''
                  }
    #验证是否已存在角色名称，若已存在则不添加
    result = xiansuoyunwei_post(url='/base/roleManager/validateRoleName.action', postdata=roleNameDict)
    if result.result is False:
        return
    addRolePara=copy.deepcopy(XiTongPeiZhiPara.addRolePara)
    idList= YunWeiCommonIntf.getDbQueryResultListYunWei(dbCommand='select  id from permissions')
    ids=''
    for item in idList:
        ids=ids+str(item[0])+','
#     print ids
    addRolePara['addPermissionIds']=ids[:-1]
    response = xiansuoyunwei_post(url='/base/roleManager/addRole', postdata=addRolePara)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "初始化角色成功")
        return True
    else:
        Log.LogOutput(LogLevel.DEBUG, "初始化角色失败")
        Log.LogOutput(message=response.text)
        return False

'''
    @功能：    通过角色名称获取角色id
    @return:    response
    @param :    XiTongPeiZhiPara.addRolePara
    @author:  chenhui 2017-3-31
'''  
def get_role_id_by_name(Name=None):
    info='通过角色名称获取id'
    Log.LogOutput(LogLevel.INFO, "%s开始..."%info)
    listpara={
        '_search':'false',
        'rows':200,
        'page':1,
        'sidx':'id',
        'sord':'desc',              
              }
    response = xiansuoyunwei_post(url='/base/roleManager/roleList', postdata=listpara)
    if response.result is True:
        resDict=json.loads(response.text)
        if resDict['records']==0:
            Log.LogOutput(message='没有找到id')
            return None
        for item in resDict['rows']:
            if item['roleName']==Name:
                Log.LogOutput(message='找到id')
                return item['id']
        Log.LogOutput(message='没有找到id')
        return None
   
'''
    @功能：新增运维人员
    @return:    response
    @param :    XiTongPeiZhiPara.xinZengYunWeiRenYuan
    @author:  chenhui 2016-04-11
'''  
def addAdminUser(para):
    Log.LogOutput(LogLevel.INFO, "新增运维管理用户")
    response = xiansuoyunwei_post(url='/adminUserManage/addAdminUser', postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增成功")
    else:
        Log.LogOutput(LogLevel.DEBUG, "新增失败")
    return response 

'''
    @功能：修改运维人员
    @return:    response
    @param : XiTongPeiZhiPara.chongZhiMiMa 
    @author:  chenhui 2016-04-11
'''  
def updAdminUser(para):
    Log.LogOutput(LogLevel.INFO, "修改运维管理用户")
    response = xiansuoyunwei_post(url='/adminUserManage/updateAdminUser', postdata=para)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "修改成功")
    else:
        Log.LogOutput(LogLevel.DEBUG, "修改失败")
    return response 

'''
    @功能：删除运维人员
    @return:    response
    @param : {'ids[]':''} 
    @author:  chenhui 2016-04-11
'''  
def delAdminUser(para):
    Log.LogOutput(LogLevel.INFO, "删除运维管理用户")
    response = xiansuoyunwei_post(url='/adminUserManage/deleteAdminUsers', postdata=para)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除成功")
    else:
        Log.LogOutput(LogLevel.DEBUG, "删除失败")
    return response 

'''
    @功能：重置运维人员密码
    @return:    response
    @param :    XiTongPeiZhiPara.chongZhiMiMa
    @author:  chenhui 2016-04-11
'''  
def resetPassword(para):
    Log.LogOutput(LogLevel.INFO, "重置运维管理用户密码")
    response = xiansuoyunwei_post(url='/adminUserManage/updateAdminUser', postdata=para)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "重置成功")
    else:
        Log.LogOutput(LogLevel.DEBUG, "重置失败")
    return response 

'''
    @功能：获取运维人员列表
    @return:    response
    @param :    XiTongPeiZhiPara.yunWeiRenYuanLieBiao
    @author:  chenhui 2016-04-11
'''  
def findAdminUserList(para):
    Log.LogOutput(LogLevel.INFO, "获取运维人员列表")
    response = xiansuoyunwei_post(url='/adminUserManage/findAdminUserList', postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "获取运维人员列表成功")
    else:
        Log.LogOutput(LogLevel.DEBUG, "获取运维人员列表失败")
    return response  

'''
    @功能：检查用户是否在运维管理平台-在线用户列表中
    @return:    response
    @param : listpara:    XiTongPeiZhiPara.yunWeiRenYuanLieBiao
                checkpara:    XiTongPeiZhiPara.yunWeiRenYuanLieBiaoJianCha
    @author:  chenhui 2016-4-7
'''  
def checkUserInAdminUserList(checkpara,listpara):
    Log.LogOutput(LogLevel.INFO, "检查用户是否在运维管理平台-运维人员列表中")
    try:
        response = findAdminUserList(para=listpara)
        responseDict=json.loads(response.text)
#         print response.text
        listData=[]
        for item in responseDict['rows']:
            listData.append(item['adminUser'])
        if findDictInDictlist(checkpara,listData) is True:
            Log.LogOutput(LogLevel.DEBUG, "用户存在于运维人员列表中")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "用户不存在于运维人员列表中")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '出现异常')
        return False
        
'''
    @功能： PC端编辑关于我们
    @para: {'notice':''}
    @return: response
    @author:  chenhui 2016-12-9
'''
def edit_about_us(para):
    info='PC端编辑”关于我们“'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/systemNoticesManage/updateSystemNotice', postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
        Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 新增运维平台公告
    @para: XiTongPeiZhiPara.yunWeiGongGaoXinZeng
    @return: response
    @author:  chenhui 2016-12-9
'''
def add_operation_notice(para,files):
    info='新增运维平台公告'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/operationNoticeManage/addOperationNotice', postdata=para,files=files)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
        Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 获取运维平台公告列表 
    @para:    XiTongPeiZhiPara.yunWeiGongGaoLieBiao
    @return: response
    @author:  chenhui 2016-12-9
'''
def get_operation_notice_list(para):
    info='获取运维平台公告列表'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/operationNoticeManage/findOperationNoticeList', postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
        Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 检查运维平台公告列表 
    @para: checkpara:  XiTongPeiZhiPara.yunWeiGongGaoLieBiaoJianCha
                    listpara:   XiTongPeiZhiPara.yunWeiGongGaoLieBiao
    @return: response
    @author:  chenhui 2016-12-9
'''
def check_operation_notice_list(checkpara,listpara):
    info='检查运维平台公告列表'
    Log.LogOutput(LogLevel.INFO, info)
    try:
        response = get_operation_notice_list(para=listpara)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, info+"成功!")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, info+'出现异常')
        return False
        
        
'''
    @功能： 修改运维平台公告
    @para: XiTongPeiZhiPara.yunWeiGongGaoXiuGai
    @return: response
    @author:  chenhui 2016-12-9
'''
def upd_operation_notice(para,files):
    info='修改运维平台公告'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/operationNoticeManage/updateOperationNotice', postdata=para,files=files)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
        Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 删除运维平台公告 
    @para:    {'ids[]':''}
    @return: response
    @author:  chenhui 2016-12-9
'''
def del_operation_notice(para):
    info='删除运维平台公告'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/operationNoticeManage/deleteOperationNotices', postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
        Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 开启运维平台公告
    @para: {'ids[]':''}
    @return: response
    @author:  chenhui 2016-12-9
'''
def open_operation_notice(para):
    info='开启运维平台公告'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/operationNoticeManage/updateOpenStates', postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
        Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 开启运维平台公告
    @para: {'ids[]':''}
    @return: response
    @author:  chenhui 2016-12-9
'''
def close_operation_notice(para):
    info='关闭运维平台公告'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/operationNoticeManage/updateCloseStates', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 删除所有运维公告
    @para: 
    @return: response
    @author:  chenhui 2016-12-6
'''
def del_all_operation_notice():
    info='删除所有运维公告'
    #首先清空轮播图配置，因其中的跳转类型为“运维活动公告”配置与运维公告有关联
    del_all_lunbo()
    Log.LogOutput(LogLevel.INFO, info)
    try:
        #获取省列表id
        listPara=copy.deepcopy(XiTongPeiZhiPara.yunWeiGongGaoLieBiao)
        
#         listPara['operationNotice.departmentNo']=InitDefaultPara.clueOrgInit['DftShengOrgDepNo']
#         response1=get_operation_notice_list(listPara)
#         resDict1=json.loads(response1.text)
        arr=[]
#         if resDict1['records']!=0:
#             for item in resDict1['rows']:
#                 arr.append(item['id'])
        #获取市列表id
#         listPara['operationNotice.departmentNo']=InitDefaultPara.clueOrgInit['DftShiOrgDepNo']
#         response2 =get_operation_notice_list(listPara)
#         resDict2=json.loads(response2.text)
#         if resDict2['records']!=0:
#             for item in resDict2['rows']:
#                 arr.append(item['id'])        
        #获取区县列表id
        listPara['operationNotice.departmentNo']=InitDefaultPara.clueOrgInit['DftQuOrgDepNo']
        response3=get_operation_notice_list(listPara)
        resDict3=json.loads(response3.text)        
        
#         if resDict3['records']==0 and resDict2['records']==0 and resDict1['records']==0:
#             Log.LogOutput(message='各层级运维公告数据为0，无需删除')
#             return True
        if resDict3['records']!=0:
            for item in resDict3['rows']:
                arr.append(item['id'])
        #如果列表为空，待办
        if len(arr)==0:
            Log.LogOutput(message='各层级运维公告数据为0，无需删除')
            return True
        #封装所有id
        deleteDict = {'ids[]':tuple(arr)}
        #删除所有的个性化配置
        result=del_operation_notice(deleteDict)
        if result.result==True:
            Log.LogOutput(message=info+"成功")
            return True
        else:
            Log.LogOutput(message=info+"失败")
            return False
    except Exception,e:
        Log.LogOutput(message=info+"异常"+str(e))
        return False
    
'''
    @功能： 新增热门搜索关键词
    @para:    XiTongPeiZhiPara.hotSearchAddPara
    @return: response
    @author:  chenhui 2016-12-16
'''
def add_hot_search(para):
    info='新增热门搜索关键词'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/hotSearchManage/addHotSearch', postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
        Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 获取热门搜索关键词列表
    @para:    XiTongPeiZhiPara.hotSearchListPara
    @return: response
    @author:  chenhui 2016-12-16
'''
def get_hot_search_list(para):
    info='获取热门搜索关键词列表'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/hotSearchManage/findHotSearchList', postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
        Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response
'''
    @功能： 检查热门搜索关键词列表
    @para:    XiTongPeiZhiPara.hotSearchListCheckPara
    @return: response
    @author:  chenhui 2016-12-16
'''
def check_hot_search_list(checkpara,listpara):
    info='检查热门搜索关键词列表'
    Log.LogOutput(LogLevel.INFO, info)
    try:
        response = get_hot_search_list(para=listpara)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, info+"成功!")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, info+'出现异常')
        return False
        
'''
    @功能： 修改热门搜索关键词
    @para:    XiTongPeiZhiPara.hotSearchUpdPara
    @return: response
    @author:  chenhui 2016-12-16
'''
def upd_hot_search(para):
    info='修改热门搜索关键词'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/hotSearchManage/updateHotSearch', postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
        Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 判断热门搜索关键词是否已存在
    @para:    XiTongPeiZhiPara.isHotSearchExist
    @return:     true/false
    @author:  chenhui 2016-12-16
'''
def is_hot_search_exist(para):
    info='判断热门搜索关键词是否已存在'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_get(url='/hotSearchManage/hasExistedHotSearch', param=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"存在!")
        return True
    else:
        Log.LogOutput(LogLevel.DEBUG, info+"不存在!")
        return False

'''
    @功能： 移动热门搜索关键词
    @para:    XiTongPeiZhiPara.hotSearchMovePara
    @return: True/False
    @author:  chenhui 2016-12-16
'''
def move_hot_search(para):
    info='移动热门搜索关键词'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/hotSearchManage/moveHotSearch', postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功!")
        return True
    else:
        Log.LogOutput(LogLevel.DEBUG, info+"失败!")
        return False

'''
    @功能： 通过关键词名称获取排序号
    @para:    'keyword'
    @return:  如果找到，返回排列序号，如果没找到，则返回-1，如果异常，返回-2
    @author:  chenhui 2016-12-16
'''
def get_hot_search_display_seq_by_keyword(para):
    info='通过关键词名称获取排序号'
    Log.LogOutput(LogLevel.INFO, info)
    listpara=copy.deepcopy(XiTongPeiZhiPara.hotSearchListPara)
    try:
        response = get_hot_search_list(para=listpara)
        resDict=json.loads(response.text)
#         print response.text
        for item in resDict['rows']:
            if item['keyword']==para:
                Log.LogOutput(LogLevel.INFO, info+'成功')
                return item['displaySeq']
        Log.LogOutput(LogLevel.INFO, info+'失败')
        return -1 
    except Exception:
        Log.LogOutput(LogLevel.ERROR, info+'出现异常')
        return -2

'''
    @功能： 开启/关闭热门搜索关键词
    @para:   {
                  'id':'',
                'state':''#true开启，false关闭          
                    }
    @return: True/False
    @author:  chenhui 2016-12-16
'''
def switch_hot_search(para):
    info='开启/关闭热门搜索关键词'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/hotSearchManage/useHotSearch', postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功!")
        return True
    else:
        Log.LogOutput(LogLevel.DEBUG, info+"失败!")
        return False
    
'''
    @功能： 删除热门搜索关键词
    @para:    {"ids[]":""}
    @return: response
    @author:  chenhui 2016-12-16
'''
def del_hot_search(para):
    info='删除热门搜索关键词'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/hotSearchManage/deleteHotSearchByIds', postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
        Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response


'''
    @功能： 删除所有热门搜索关键词
    @para:
    @return: true/false
    @author:  chenhui 2016-12-16
'''
def del_all_hot_search():
    try:
        info='删除所有热门搜索关键词'
        Log.LogOutput(LogLevel.INFO, info)
        listpara=copy.deepcopy(XiTongPeiZhiPara.hotSearchListPara)
        result=get_hot_search_list(listpara)
        resDict=json.loads(result.text)
        if resDict['records']==0:
            Log.LogOutput(message='列表关键词为空，无需删除')
            return True
        ids=[]
        for item in resDict['rows']:
            ids.append(item['id'])
        delPara={
                 'ids[]':tuple(ids)
                 }
        response=del_hot_search(delPara)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功!")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
            return False
    except Exception:
        Log.LogOutput(LogLevel.DEBUG, info+"异常!")
        return False   
    
'''
    @功能： 新增便民服务配置
    @para:    XiTongPeiZhiPara.addConvenienceServicePara
    @return: response
    @author:  chenhui 2016-12-20
'''
def add_convenience_service(para,files):
    info='新增便民服务配置'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/convenienceServiceManage/addConvenienceService', postdata=para,files=files)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
        Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 获取便民服务配置列表信息
    @para:    XiTongPeiZhiPara.convenienceServiceListPara
    @return: response
    @author:  chenhui 2016-12-20
'''
def get_convenience_service_list(para):
    info='获取便民服务配置列表信息'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/convenienceServiceManage/findConvenienceServiceList', postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
        Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 通过标题名称获取排序号
    @para:    'title'
    @return:  如果找到，返回排列序号，如果没找到，则返回-1，如果异常，返回-2
    @author:  chenhui 2016-12-16
'''
def get_convenience_service_display_seq_by_title(para):
    info='通过标题名称获取排序号'
    Log.LogOutput(LogLevel.INFO, info)
    listpara=copy.deepcopy(XiTongPeiZhiPara.hotSearchListPara)
    try:
        response = get_convenience_service_list(para=listpara)
        resDict=json.loads(response.text)
#         print response.text
        for item in resDict['rows']:
            if item['title']==para:
                Log.LogOutput(LogLevel.INFO, info+'成功')
                return item['seq']
        Log.LogOutput(LogLevel.INFO, info+'失败')
        return -1 
    except Exception:
        Log.LogOutput(LogLevel.ERROR, info+'出现异常')
        return -2
    
'''
    @功能： 检查便民服务配置列表信息
    @para:   checkpara: XiTongPeiZhiPara.convenienceServiceCheckPara
                  listpara:  XiTongPeiZhiPara.convenienceServiceListPara
    @return: response
    @author:  chenhui 2016-12-20
'''
def check_convenience_service_list(checkpara,listpara):
    info='检查便民服务配置列表信息'
    Log.LogOutput(LogLevel.INFO, info)
    try:
        response = get_convenience_service_list(para=listpara)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, info+"成功!")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, info+'出现异常')
        return False
    
'''
    @功能： 修改便民服务配置
    @para:    XiTongPeiZhiPara.updConvenienceServicePara
    @return: response
    @author:  chenhui 2016-12-20
'''
def upd_convenience_service(para,files):
    info='修改便民服务配置'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/convenienceServiceManage/updateConvenienceService', postdata=para,files=files)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
        Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response


'''
    @功能： 开启便民服务配置
    @para:    {'ids[]':''}
    @return: response
    @author:  chenhui 2016-12-20
'''
def open_convenience_service(para):
    info='开启便民服务配置'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/convenienceServiceManage/open', postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
        Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 关闭便民服务配置
    @para:    {'ids[]':''}
    @return: response
    @author:  chenhui 2016-12-20
'''
def close_convenience_service(para):
    info='关闭便民服务配置'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/convenienceServiceManage/close', postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
        Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 移动便民服务配置
    @para:    XiTongPeiZhiPara.convenienceServiceMovePara
    @return: response
    @author:  chenhui 2016-12-20
'''
def move_convenience_service(para):
    info='移动便民服务配置'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/convenienceServiceManage/moveConvenienceService', postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
        Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response


'''
    @功能： 删除便民服务配置
    @para:    {'ids[]':''}
    @return: response
    @author:  chenhui 2016-12-20
'''
def del_convenience_service(para):
    info='删除便民服务配置'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/convenienceServiceManage/deleteConvenienceServices', postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
        Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 删除所有便民服务配置
    @para:
    @return: true/false
    @author:  chenhui 2016-12-20
'''
def del_all_convenience_service():
    try:
        info='删除所有便民服务配置'
        Log.LogOutput(LogLevel.INFO, info)
        listpara=copy.deepcopy(XiTongPeiZhiPara.convenienceServiceListPara)
        result=get_convenience_service_list(listpara)
        resDict=json.loads(result.text)
        if resDict['records']==0:
            Log.LogOutput(message='列表数据为空，无需删除')
            return True
        ids=[]
        for item in resDict['rows']:
            ids.append(item['id'])
        delPara={
                 'ids[]':tuple(ids)
                 }
        response=del_convenience_service(delPara)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功!")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
            return False
    except Exception:
        Log.LogOutput(LogLevel.DEBUG, info+"异常!")
        return False  
    
'''
    @功能： 新增电话分类
    @para:    XiTongPeiZhiPara.addMobileCategoryPara
    @return: response
    @author:  chenhui 2016-12-21
'''
def add_mobile_category(para):
    info='新增电话分类'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/companyCategoryManage/addCompanyCategory', postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
        Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 获取电话分类列表
    @para:    XiTongPeiZhiPara.mobileCategoryListPara
    @return: response
    @author:  chenhui 2016-12-21
'''
def get_mobile_category_list(para):
    info='获取电话分类列表'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/companyCategoryManage/findCompanyCategoryList', postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
        Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 检查电话分类列表
    @para:      listpara:    XiTongPeiZhiPara.mobileCategoryListPara
                checkpara:    XiTongPeiZhiPara.mobileCategoryListCheckPara
    @return: response
    @author:  chenhui 2016-12-21
'''
def check_mobile_category_list(listpara,checkpara):
    info='检查电话分类列表'
    Log.LogOutput(LogLevel.INFO, info)
    try:
        response = get_mobile_category_list(para=listpara)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, info+"成功!")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, info+'出现异常')
        return False

'''
    @功能： 修改电话分类
    @para:    XiTongPeiZhiPara.updMobileCategoryPara
    @return: response
    @author:  chenhui 2016-12-21
'''
def upd_mobile_category(para):
    info='修改电话分类'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/companyCategoryManage/updateCompanyCategory', postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
        Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 移动电话分类
    @para:    XiTongPeiZhiPara.moveMobileCategoryPara
    @return: response
    @author:  chenhui 2016-12-21
'''
def move_mobile_category(para):
    info='移动电话分类'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/companyCategoryManage/moveCompanyCategory', postdata=para)
    print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
        Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 通过类别名称获取排序号
    @para:    'category'
    @return:  如果找到，返回排列序号，如果没找到，则返回-1，如果异常，返回-2
    @author:  chenhui 2016-12-21
'''
def get_mobile_category_display_seq_by_category_name(para):
    info='通过类别名称获取排序号'
    Log.LogOutput(LogLevel.INFO, info)
    listpara=copy.deepcopy(XiTongPeiZhiPara.mobileCategoryListPara)
    try:
        response = get_mobile_category_list(para=listpara)
        resDict=json.loads(response.text)
#         print response.text
        for item in resDict['rows']:
            if item['categoryName']==para:
                Log.LogOutput(LogLevel.INFO, info+'成功')
                return item['seq']
        Log.LogOutput(LogLevel.INFO, info+'失败')
        return -1 
    except Exception:
        Log.LogOutput(LogLevel.ERROR, info+'出现异常')
        return -2
    
'''
    @功能： 删除电话分类
    @para:    {'ids[]':''}
    @return: response
    @author:  chenhui 2016-12-21
'''
def del_mobile_category(para):
    info='删除电话分类'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/companyCategoryManage/deleteCompanyCategorys', postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
        Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 删除所有电话分类
    @para:
    @return: true/false
    @author:  chenhui 2016-12-21
'''
def del_all_mobile_category():
    try:
        info='删除所有电话分类'
        Log.LogOutput(LogLevel.INFO, info)
        listpara=copy.deepcopy(XiTongPeiZhiPara.mobileCategoryListPara)
        result=get_mobile_category_list(listpara)
        resDict=json.loads(result.text)
        if resDict['records']==0:
            Log.LogOutput(message='列表数据为空，无需删除')
            return True
        ids=[]
        for item in resDict['rows']:
            ids.append(item['id'])
        delPara={
                 'ids[]':tuple(ids)
                 }
        response=del_mobile_category(delPara)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功!")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
            return False
    except Exception:
        Log.LogOutput(LogLevel.DEBUG, info+"异常!")
        return False 
    
'''
    @功能： 新增电话
    @para:    XiTongPeiZhiPara.addPhonePara
    @return: response
    @author:  chenhui 2016-12-21
'''
def add_mobile(para):
    info='新增电话'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/companyPhoneManage/addCompanyPhone', postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
        Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 获取电话列表
    @para:    XiTongPeiZhiPara.phoneListPara
    @return: response
    @author:  chenhui 2016-12-21
'''
def get_mobile_list(para):
    info='获取电话列表'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/companyPhoneManage/findCompanyPhoneList', postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
        Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 检查电话列表
    @para:    listpara:    XiTongPeiZhiPara.phoneListPara
                    checkpara: XiTongPeiZhiPara.phoneListCheckPara
    @return: response
    @author:  chenhui 2016-12-21
'''
def check_mobile_list(listpara,checkpara):
    info='检查电话列表'
    Log.LogOutput(LogLevel.INFO, info)
    try:
        response = get_mobile_list(para=listpara)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, info+"成功!")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, info+'出现异常')
        return False

'''
    @功能： 修改电话
    @para:    XiTongPeiZhiPara.updPhonePara
    @return: response
    @author:  chenhui 2016-12-21
'''
def upd_mobile(para):
    info='修改电话'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/companyPhoneManage/updateCompanyPhone', postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
        Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 移动电话
    @para:    XiTongPeiZhiPara.moveMobilePara
    @return: response
    @author:  chenhui 2016-12-21
'''
def move_mobile(para):
    info='移动电话'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/companyPhoneManage/moveCompanyPhone', postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
        Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 通过类别名称获取排序号
    @para:     
                    companyName        #单位名称
                    companyCategoryId  #所属类别名称
    @return:  如果找到，返回排列序号，如果没找到，则返回-1，如果异常，返回-2
    @author:  chenhui 2016-12-22
'''
def get_mobile_display_seq_by_company_name(name,categoryId):
    info='通过单位名称获取排序号'
    Log.LogOutput(LogLevel.INFO, info)
    listpara=copy.deepcopy(XiTongPeiZhiPara.phoneListPara)
    listpara['companyPhone.companyCategoryId']=categoryId
    try:
        response = get_mobile_list(para=listpara)
        resDict=json.loads(response.text)
#         print response.text
        for item in resDict['rows']:
            if item['companyName']==name:
                Log.LogOutput(LogLevel.INFO, info+'成功')
                return item['seq']
        Log.LogOutput(LogLevel.INFO, info+'失败')
        return -1 
    except Exception:
        Log.LogOutput(LogLevel.ERROR, info+'出现异常')
        return -2
    
'''
    @功能： 删除电话
    @para:    {'ids[]':'',  'companyCategoryId':''}
    @return: response
    @author:  chenhui 2016-12-21
'''
def del_mobile(para):
    info='删除电话'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/companyPhoneManage/deleteCompanyPhones', postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
        Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 开通区县
    @para:    XiTongPeiZhiPara.openOrgPara
    @return: response
    @author:  chenhui 2016-12-22
'''
def open_org_state(para):
    info='开通区县'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/organizationManage/openOrgState', postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
        Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 关闭区县
    @para:    XiTongPeiZhiPara.openOrgPara
    @return: response
    @author:  chenhui 2016-12-22
'''
def close_org_state(para):
    info='关闭区县'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/organizationManage/closeOrgState', postdata=para)
    print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
        Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 检查区县开通列表
    @para:    listpara:    XiTongPeiZhiPara.getOrgOpenStateListPara
                checkpara:  XiTongPeiZhiPara.orgOpenStateListCheckPara
    @return:  true/false
    @author:  chenhui 2016-12-22
'''
def check_org_open_state_list(listpara,checkpara):
    info='检查区县开通列表'
    Log.LogOutput(LogLevel.INFO, info)
    try:
        response = xiansuoyunwei_post(url='/organizationManage/findOrganizationList', postdata=listpara)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, info+"成功!")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, info+'出现异常')
        return False

'''
    @功能： 新增轮播图
    @para:    XiTongPeiZhiPara.addLunBoPara
    @return: response
    @author:  chenhui 2016-12-26
'''
def add_lunbo(para,files):
    info='新增轮播图'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/eventConfigurationManage/addEventConfiguration', postdata=para,files=files)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
        Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 修改轮播图
    @para:    XiTongPeiZhiPara.updLunBoPara
    @return:    response
    @author:  chenhui 2016-12-26
'''
def upd_lunbo(para,files):
    info='修改轮播图'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/eventConfigurationManage/updateEventConfiguration', postdata=para,files=files)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
        Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 获取轮播图列表
    @para:    XiTongPeiZhiPara.getLunBoListPara
    @return:    response
    @author:  chenhui 2016-12-26
'''
def get_lunbo_list(para):
    info='获取轮播图列表'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/eventConfigurationManage/findEventConfigurationList', postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
        Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 检查轮播图列表
    @para:    listpara:    XiTongPeiZhiPara.getLunBoListPara
                checkpara:  XiTongPeiZhiPara.checkLunBoListPara
    @return:  true/false
    @author:  chenhui 2016-12-26
'''
def check_lunbo_list(listpara,checkpara):
    info='检查轮播图列表'
    Log.LogOutput(LogLevel.INFO, info)
    try:
        response = get_lunbo_list(listpara)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, info+"成功!")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, info+'出现异常')
        return False

'''
    @功能： 开启轮播图
    @para:    {'ids[]':''}
    @return: response
    @author:  chenhui 2016-12-26
'''
def open_lunbo(para):
    info='开启轮播图'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/eventConfigurationManage/updateOpenStates', postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
        Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response
   
'''
    @功能： 关闭轮播图
    @para:    {'ids[]':''}
    @return: response
    @author:  chenhui 2016-12-26
'''
def close_lunbo(para):
    info='关闭轮播图'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/eventConfigurationManage/updateCloseStates', postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
        Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 移动轮播图配置信息
    @para:    XiTongPeiZhiPara.moveLunBoPara
    @return: response
    @author:  chenhui 2016-12-26
'''
def move_lunbo(para):
    info='移动轮播图配置信息'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/eventConfigurationManage/moveEventConfiguration', postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
        Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 通过标题名称获取排序号
    @para:     
                    title        #标题
    @return:  如果找到，返回排列序号，如果没找到，则返回-1，如果异常，返回-2
    @author:  chenhui 2016-12-27
'''
def get_lunbo_seq_by_title(title):
    info='通过标题名称获取排序号'
    Log.LogOutput(LogLevel.INFO, info)
    listpara=copy.deepcopy(XiTongPeiZhiPara.getLunBoListPara)
    try:
        response = get_lunbo_list(para=listpara)
        resDict=json.loads(response.text)
#         print response.text
        for item in resDict['rows']:
            if item['title']==title:
                Log.LogOutput(LogLevel.INFO, info+'成功')
                return item['seq']
        Log.LogOutput(LogLevel.INFO, info+'失败')
        return -1 
    except Exception:
        Log.LogOutput(LogLevel.ERROR, info+'出现异常')
        return -2
    
'''
    @功能： 删除轮播图配置信息
    @para:    {'ids[]':''}
    @return: response
    @author:  chenhui 2016-12-26
'''
def del_lunbo(para):
    info='删除轮播图配置信息'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/eventConfigurationManage/deleteEventConfiguration', postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
        Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 删除所有轮播图配置信息
    @para:
    @return: true/false
    @author:  chenhui 2016-12-26
'''
def del_all_lunbo():
    try:
        info='删除所有轮播图配置信息'
        Log.LogOutput(LogLevel.INFO, info)
        listpara=copy.deepcopy(XiTongPeiZhiPara.getLunBoListPara)
        result=get_lunbo_list(listpara)
        resDict=json.loads(result.text)
        if resDict['records']==0:
            Log.LogOutput(message='数据为空，无需删除')
            return True
        ids=[]
        for item in resDict['rows']:
            ids.append(item['id'])
        delPara={
                 'ids[]':tuple(ids)
                 }
        response=del_lunbo(delPara)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功!")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
            return False
    except Exception:
        Log.LogOutput(LogLevel.DEBUG, info+"异常!")
        return False   
    
'''
    @功能： 新增等级
    @para:    XiTongPeiZhiPara.addGradePara
    @return: response
    @author:  chenhui 2016-12-21
'''
def add_grade(para):
    info='新增等级'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/gradeManage/addGrade', postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
        Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 修改等级
    @para:    XiTongPeiZhiPara.updGradePara
    @return: response
    @author:  chenhui 2016-12-21
'''
def upd_grade(para):
    info='修改等级开始......'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/gradeManage/updateGrade', postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
        Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 获取等级列表
    @para:    XiTongPeiZhiPara.gradeListPara
    @return: response
    @author:  chenhui 2016-12-21
'''
def get_grade_list(para):
    info='获取等级列表'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuoyunwei_post(url='/gradeManage/findGradeList', postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
        Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 根据等级获取所需爆料数
    @para:    XiTongPeiZhiPara.gradeListPara
    @return:  返回所需爆料数，若为-1，表示没有对应的等级
    @author:  chenhui 2017-4-13
'''
def get_clue_demand_by_grade(grade):
    info='根据等级获取所需爆料数'
    Log.LogOutput(LogLevel.INFO, info)
    listpara=copy.deepcopy(XiTongPeiZhiPara.gradeListPara)
    response = xiansuoyunwei_post(url='/gradeManage/findGradeList', postdata=listpara)
#     print response.text
    resDict=json.loads(response.text)
    for item in resDict['rows']:
        if item['grade']==grade:
            Log.LogOutput(LogLevel.INFO, info+"成功!")
            return item['gradeDemand']
    Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return -1

'''
    @功能： 检查等级列表
    @para:    listpara:    XiTongPeiZhiPara.gradeListPara
                    checkpara: XiTongPeiZhiPara.gradeListCheckPara
    @return:     检查成功返回True，失败返回False
    @author:  chenhui 2016-12-21
'''
def check_grade_list(listpara,checkpara):
    info='检查等级列表'
    Log.LogOutput(LogLevel.INFO, info)
    try:
        response = get_grade_list(para=listpara)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, info+"成功!")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, info+'出现异常')
        return False
    
'''
    @功能： 根据等级获取所需爆料数
    @para:    XiTongPeiZhiPara.gradeListPara
    @return: response
    @author:  chenhui 2017-4-1
'''
def get_clue_num_by_grade(para):
    info='根据等级获取所需爆料数'
    Log.LogOutput(LogLevel.INFO, info)
    listpara=copy.deepcopy(XiTongPeiZhiPara.gradeListPara)
    result=get_grade_list(listpara)
    resultDict=json.loads(result.text)
    
    
    response = xiansuoyunwei_post(url='/gradeManage/findGradeList', postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
        Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response   