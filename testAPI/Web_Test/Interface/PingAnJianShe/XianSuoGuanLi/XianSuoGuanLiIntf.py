# -*- coding:UTF-8 -*-
'''
Created on 2016-11-8

@author: hongzenghui
'''
from __future__ import unicode_literals
from COMMON import Log, CommonUtil
from CONFIG import InitDefaultPara, Global
from CONFIG.Define import LogLevel
from Interface.PingAnJianShe.XianSuoGuanLi import XianSuoGuanLiPara
from Interface.PingAnJianShe.pingAnJianSheHttpCommon import pinganjianshe_post, \
    pinganjianshe_get
import copy
import json

'''  
    @功能： 检查在线索管理列表中通过手机号或昵称、爆料状态、主题名称快速搜索的结果
    @para: compareDict：搜索结果查询，请调用XianSuoGuanLiPara中的clueSearchResultCheck
    searchDict:搜索条件字典，请调用XianSuoGuanLiPara中的clueFastSearchDict
    @return: 如果检查成功，则返回True；否则返回False  
'''
def check_baoliao_fast_search_result(compareDict=None,searchDict=None,username=InitDefaultPara.userInit['DftQuUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "开始快速搜索..")
    try:
        response = pinganjianshe_post(url='/clueManage/clueInformationManage/findClueInformationPageBySearchsInfoVo.action', postdata=searchDict,username=username, password = password)  
#         print response.text
        if response.result is False:
            Log.LogOutput(LogLevel.ERROR, "未检查到符合快速搜索条件的爆料")
            return False
        else:
            responseDict = json.loads(response.text)
            for row in responseDict['rows']:
                if CommonUtil.findDictInDictlist(compareDict, [row['information']]) is True:
                    Log.LogOutput(LogLevel.DEBUG, "检查到符合快速搜索条件的爆料")
                    return True
            Log.LogOutput(LogLevel.DEBUG, "未检查到符合快速搜索条件的爆料")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "未检查到符合快速搜索条件的爆料")
        return False

'''  
    @功能： 检查在线索管理列表中通过高级搜索的结果
    @para: compareDict：搜索结果查询，请调用XianSuoGuanLiPara中的clueSearchResultCheck
    searchDict:搜索条件字典，请调用XianSuoGuanLiPara中的clueAdvanceSearchDict
    @return: 如果检查成功，则返回True；否则返回False  
'''
def check_baoliao_advance_search_result(compareDict=None,searchDict=None,username=InitDefaultPara.userInit['DftQuUser'],password='11111111'):
#     Log.LogOutput(LogLevel.INFO, "开始高级搜索..")
    try:
        response = pinganjianshe_post(url='/clueManage/clueInformationManage/findClueInformationPageBySearchsInfoVo.action', postdata=searchDict,username=username, password = password)  
#         print response.text
        if response.result is False:
            Log.LogOutput(LogLevel.ERROR, "未检查到符合高级搜索条件的爆料")
            return False
        else:
            responseDict = json.loads(response.text)
            for row in responseDict['rows']:
                if CommonUtil.findDictInDictlist(compareDict, [row['information']]) is True:
                    Log.LogOutput(LogLevel.DEBUG, "检查到符合高级搜索条件的爆料")
                    return True
            Log.LogOutput(LogLevel.DEBUG, "未检查到符合高级搜索条件的爆料")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "未检查到符合高级搜索条件的爆料")
        return False

'''  
    @功能： 返回在线索管理列表中通过手机号或昵称、爆料状态、主题名称快速搜索的结果的数量
    @para: 
    searchDict:搜索条件字典，请调用XianSuoGuanLiPara中的clueFastSearchDict
    @return: 返回列表数量，无数据则返回0 
'''
def get_baoliao_fast_search_count(searchDict=None,username=InitDefaultPara.userInit['DftQuUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "开始快速搜索..")
    try:
        response = pinganjianshe_post(url='/clueManage/clueInformationManage/findClueInformationPageBySearchsInfoVo.action', postdata=searchDict,username=username, password = password)  
        if response.result is False:
            Log.LogOutput(LogLevel.ERROR, "搜索结果为空，返回0")
            return 0
        else:
            responseDict = json.loads(response.text)
            return responseDict["total"]
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "搜索结果为空，返回0")
        return False
    
'''  
    @功能： 通过主题名称获取主题ID
    @para: themeName：主题名称
    @return: 如果成功，则返回ID；否则返回None  
'''
def get_theme_id_by_name(themeName=None,username=InitDefaultPara.userInit['DftQuUser'],password='11111111'):
    searchDict = copy.deepcopy(XianSuoGuanLiPara.clueThemeListGetDict)
    response = pinganjianshe_get(url='/clueManage/themeManage/findThemeContentListPageByThemeContentVo.action', param=searchDict,username=username, password = password)
    responseDict = json.loads(response.text)
    if responseDict["total"] == 0:
        Log.LogOutput(LogLevel.WARN, "列表中无主题数据")
        return None
    else:
        for row in responseDict["rows"]:
            if row['name'] == themeName:
                return row['id']
        Log.LogOutput(LogLevel.WARN, "未找到符合条件的主题")
        return None
    
'''  
    @功能： 通过事件描述信息获取爆料ID
    @para: clueDesc：爆料描述
    @return: 如果成功，则返回ID；否则返回None  
'''
def get_clue_id_by_description(clueDesc=None,username=InitDefaultPara.userInit['DftQuUser'],password='11111111'):
    searchDict = copy.deepcopy(XianSuoGuanLiPara.clueFastSearchDict)
    try:
        response = pinganjianshe_post(url='/clueManage/clueInformationManage/findClueInformationPageBySearchsInfoVo.action', postdata=searchDict,username=username, password = password)
        responseDict = json.loads(response.text)
        for row in responseDict['rows']:
            if row['information']['contentText'] == clueDesc:
                Log.LogOutput(LogLevel.WARN, "找到符合条件的爆料，返回id")
                return row['information']['id']
        else:
            Log.LogOutput(LogLevel.WARN, "未找到符合条件的爆料，返回None")
            return None
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "未找到符合条件的爆料，返回None")
        return False
'''  
    @功能： 删除单条爆料信息
    @para: 
    deleteCluePara:要删除的线索信息，请调用XianSuoGuanLiPara中的deleteCluePara
    @return: 如果删除成功，则返回True；否则返回False  
''' 
def delete_single_clue(deleteCluePara,username=InitDefaultPara.userInit['DftQuUser'],password='11111111'):
    response = pinganjianshe_post(url='/clueManage/clueInformationManage/updateInformationDelState.action', postdata=deleteCluePara, username=username, password = password)
    if response.result is True:
        Log.LogOutput(LogLevel.DEBUG, "爆料删除成功")
        return True
    else:
        Log.LogOutput(LogLevel.DEBUG, "爆料删除失败")
        return False
      

'''  
    @功能： 设置爆料未公开或不公开
    @para: 
    clueId:要设置的线索id
    showState：分享状态，0表示不公开，1表示公开,2表示精彩推荐
    @return: 如果成功，则返回True；否则返回False  
''' 
def set_clue_show_state(clueId=None,showState=None,username=InitDefaultPara.userInit['DftQuUser'],password='11111111'):
    setDict = {'ids':clueId,
               'showState':showState}
    response = pinganjianshe_get(url='/clueManage/clueInformationManage/updateInformationShowStateByIds.action', param=setDict, username=username, password = password)
    if response.result is True:
        Log.LogOutput(LogLevel.DEBUG, "爆料分享状态设置完成")
        return True
    else:
        Log.LogOutput(LogLevel.DEBUG, "爆料分享状态设置失败")
        return False
    
'''  
    @功能： 爆料转事件
    @para: 
    clueToIssuePara:请调用XianSuoGuanLiPara中的爆料转事件字典clueToIssuePara
    @return: 如果成功，则返回True；否则返回False
''' 
def change_clue_to_issue(clueToIssuePara=None,username=InitDefaultPara.userInit['DftQuUser'],password='11111111'):
    response = pinganjianshe_post(url='/issues/issueManage/addIssueByClue.action', postdata=clueToIssuePara, username=username, password = password)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.DEBUG, "爆料转事件完成")
        return True
    else:
        Log.LogOutput(LogLevel.DEBUG, "爆料转事件失败")
        return False
    
'''  
    @功能：官方回复
    @para: 
    clueId:线索id号
    officialReply:官方回复内容
    @return: 如果成功，则返回True；否则返回False
''' 
def official_reply_for_clue(clueId=None,officialReply=None,username=InitDefaultPara.userInit['DftQuUser'],password='11111111'):
    officeReplyPara = {
                       "ids":clueId,
                       "officialReply":officialReply
                       }
    response = pinganjianshe_post(url='/clueManage/clueInformationManage/officialReply.action', postdata=officeReplyPara, username=username, password = password)
    if response.result is True:
        Log.LogOutput(LogLevel.DEBUG, "官方回复完成")
        return True
    else:
        Log.LogOutput(LogLevel.DEBUG, "官方回复失败")
        return False
    
'''  
    @功能：删除所有说说数据
    @para: 
    @return: 如果成功，则返回True；否则返回False
'''    
   
def delete_all_shuoshuo():
    try:
        Log.LogOutput(message='正在清空所有说说数据...')
        listPara = copy.deepcopy(XianSuoGuanLiPara.shuoshuoListGetDict)
        response = pinganjianshe_get(url='/clueManage/casualTalkManage/findCasualTalkPageBySearchCasualTalkVo.action', param=listPara)
#         print response.text
        responseDict = json.loads(response.text)
        if responseDict['records'] == 0:
            Log.LogOutput(LogLevel.DEBUG, '列表数据为空')
        else:
            #获取ID并删除
            shuoshuoDelDict = copy.deepcopy(XianSuoGuanLiPara.shuoshuoDelDict)
            for dictListItem in responseDict['rows']:
                shuoshuoDelDict['delInfoRecord.informationId'] = dictListItem['id']
                shuoshuoDelDict['delInfoRecord.mobile'] = dictListItem['mobile']
                delete_one_shuoshuo(shuoshuoDelDict)      
    except Exception :
        Log.LogOutput(LogLevel.ERROR, '说说删除异常')
        return False
    
'''  
    @功能：删除单条说说
    @para: 
    shuoshuoDelDict：请调用XianSuoGuanLiPara中的shuoshuoDelDict字典
    @return: 删除成功，则返回True；否则返回False
'''
   
def delete_one_shuoshuo(shuoshuoDelDict,username=InitDefaultPara.userInit['DftQuUser'],password='11111111'):
    response = pinganjianshe_post(url='/clueManage/casualTalkManage/updateCasualTalkDelState.action', postdata=shuoshuoDelDict, username=username, password = password)
    if response.result is True:
        Log.LogOutput(LogLevel.DEBUG, "说说删除成功")
        return True
    else:
        Log.LogOutput(LogLevel.DEBUG, "说说删除失败")
        return False
    
'''  
    @功能： 检查在随便说说列表中通过说说内容、主题名称、我的信息搜索的结果
    @para: compareDict：搜索结果查询，请调用XianSuoGuanLiPara中的shuoshuoSearchResultCheck
    searchDict:搜索条件字典，请调用XianSuoGuanLiPara中的shuoshuoSearchDict
    @return: 如果检查成功，则返回True；否则返回False  
'''
def check_shuoshuo_search_result(compareDict=None,searchDict=None,username=InitDefaultPara.userInit['DftQuUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "开始说说搜索..")
    try:
        response = pinganjianshe_get(url='/clueManage/casualTalkManage/findCasualTalkPageBySearchCasualTalkVo.action', param=searchDict,username=username, password = password)  
#         print response.text
        if response.result is False:
            Log.LogOutput(LogLevel.ERROR, "未检查到符合搜索条件的说说")
            return False
        else:
            responseDict = json.loads(response.text)
            if CommonUtil.findDictInDictlist(compareDict, responseDict['rows']) is True:
                Log.LogOutput(LogLevel.DEBUG, "检查到符合搜索条件的说说")
                return True
            else:
                Log.LogOutput(LogLevel.DEBUG, "未检查到符合搜索条件的说说")
                return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "未检查到符合搜索条件的说说")
        return False

'''  
    @功能：通过后台线索管理新增说说
    @para: 
    addShuoSHuoByXianSuoGuanLiPara：请调用XianSuoGuanLiPara中的addShuoSHuoByXianSuoGuanLiPara字典
    @return: 新增成功，则返回True；否则返回False
'''
   
def add_shuoshuo_by_xiansuoguanli(addShuoSHuoByXianSuoGuanLiPara,username=InitDefaultPara.userInit['DftQuUser'],password='11111111'):
    response = pinganjianshe_post(url='/clueManage/casualTalkManage/addCasualTalk.action', postdata=addShuoSHuoByXianSuoGuanLiPara, username=username, password = password)
    if response.result is True:
        Log.LogOutput(LogLevel.DEBUG, "说说新增成功")
        return True
    else:
        Log.LogOutput(LogLevel.DEBUG, "说说新增失败")
        return False 
    
'''  
    @功能：通过后台线索管理更新说说
    @para: 
    updateShuoShuoByXianSuoGuanLiPara：请调用XianSuoGuanLiPara中的updateShuoShuoByXianSuoGuanLiPara字典
    @return: 新增成功，则返回True；否则返回False
'''
   
def update_shuoshuo_by_xiansuoguanli(updateShuoSHuoByXianSuoGuanLiPara,username=InitDefaultPara.userInit['DftQuUser'],password='11111111'):
    response = pinganjianshe_post(url='/clueManage/casualTalkManage/updateCasualTalk.action', postdata=updateShuoSHuoByXianSuoGuanLiPara, username=username, password = password)
    if response.result is True:
        Log.LogOutput(LogLevel.DEBUG, "说说更新成功")
        return True
    else:
        Log.LogOutput(LogLevel.DEBUG, "说说更新失败")
        return False 

'''  
    @功能： 通过说说内容获取说说ID
    @para: shuoshuoDesc：说说内容
    @return: 如果成功，则返回ID；否则返回None  
'''
def get_shuoshuo_id_by_content(shuoshuoContent=None,username=InitDefaultPara.userInit['DftQuUser'],password='11111111'):
    searchDict = copy.deepcopy(XianSuoGuanLiPara.shuoshuoSearchDict)
    try:
        response = pinganjianshe_post(url='/clueManage/casualTalkManage/findCasualTalkPageBySearchCasualTalkVo.action', postdata=searchDict,username=username, password = password)
        responseDict = json.loads(response.text)
        for row in responseDict['rows']:
            if row['contentText'] == shuoshuoContent:
                Log.LogOutput(LogLevel.WARN, "找到符合条件的说说，返回id")
                return row['id']
        else:
            Log.LogOutput(LogLevel.WARN, "未找到符合条件的说说，返回None")
            return None
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "未找到符合条件的说说，返回None")
        return False  
    
'''  
    @功能：新增平安宣传
    @para: 
    addPingAnXuanChuanDict：请调用XianSuoGuanLiPara中的addPingAnXuanChuanDict字典
    @return: 新增成功，则返回True；否则返回False
'''
   
def add_pinganxuanchuan(addPingAnXuanChuanDict,username=InitDefaultPara.userInit['DftQuUser'],password='11111111'):
    response = pinganjianshe_post(url='/clueManage/clueInformationManage/addClueProclamation.action', postdata=addPingAnXuanChuanDict, username=username, password = password)
    if response.result is True:
        Log.LogOutput(LogLevel.DEBUG, "新增平安宣传成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, "新增平安宣传失败")
        return False 
    
'''  
    @功能：修改平安宣传
    @para: 
    modifyPingAnXuanChuanDict：请调用XianSuoGuanLiPara中的modifyPingAnXuanChuanDict字典
    @return: 新增成功，则返回True；否则返回False
'''
   
def modify_pinganxuanchuan(modifyPingAnXuanChuanDict,username=InitDefaultPara.userInit['DftQuUser'],password='11111111'):
    response = pinganjianshe_post(url='/clueManage/clueInformationManage/updateClueProclamation.action', postdata=modifyPingAnXuanChuanDict, username=username, password = password)
    if response.result is True:
        Log.LogOutput(LogLevel.DEBUG, "修改平安宣传成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, "修改平安宣传失败")
        return False 
    
'''  
    @功能：更新平安宣传状态
    @para: 
    updatePingAnXuanChuanStateDict：请调用XianSuoGuanLiPara中的updatePingAnXuanChuanStateDict字典
    @return: 新增成功，则返回True；否则返回False
'''
   
def update_pinganxuanchuan_state(updatePingAnXuanChuanStateDict,username=InitDefaultPara.userInit['DftQuUser'],password='11111111'):
    response = pinganjianshe_get(url='/clueManage/clueInformationManage/updateInformationShowStateByIds.action', param=updatePingAnXuanChuanStateDict, username=username, password = password)
    if response.result is True:         
        Log.LogOutput(LogLevel.DEBUG, "更新平安宣传状态成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, "更新平安宣传状态失败")
        return False
    
'''  
    @功能： 检查在平安宣传列表中通过标题、状态搜索的结果
    @para: compareDict：搜索结果查询，请调用XianSuoGuanLiPara中的shuoshuoSearchResultCheck
    searchDict:搜索条件字典，请调用XianSuoGuanLiPara中的shuoshuoSearchDict
    @return: 如果检查成功，则返回True；否则返回False  
'''
def check_pinganxuanchuan_search_result(compareDict=None,searchDict=None,username=InitDefaultPara.userInit['DftQuUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "开始平安宣传搜索..")
    try:
        response = pinganjianshe_post(url='/clueManage/clueInformationManage/findClueInformationPageBySearchsInfoVo.action', postdata=searchDict,username=username, password = password)  
#         print response.text
        if response.result is False:
            Log.LogOutput(LogLevel.ERROR, "未检查到符合搜索条件的平安宣传")
            return False
        else:
            responseDict = json.loads(response.text)
            for row in responseDict['rows']:
                if CommonUtil.findDictInDictlist(compareDict, [row['information']]) is True:
                    Log.LogOutput(LogLevel.DEBUG, "检查到符合搜索条件的平安宣传")
                    return True
            Log.LogOutput(LogLevel.DEBUG, "未检查到符合搜索条件的平安宣传")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "未检查到符合搜索条件的平安宣传")
        return False
    
'''  
    @功能： 通过平安宣传标题获取平安宣传ID
    @para: pingAnXuanChuanTitle：平安宣传标题
    @return: 如果成功，则返回ID；否则返回None  
'''
def get_pinganxuanchuan_id_by_title(pingAnXuanChuanTitle=None,username=InitDefaultPara.userInit['DftQuUser'],password='11111111'):
    searchDict = copy.deepcopy(XianSuoGuanLiPara.pingAnXuanChuanSearchDict)
    try:
        response = pinganjianshe_post(url='/clueManage/clueInformationManage/findClueInformationPageBySearchsInfoVo.action', postdata=searchDict,username=username, password = password)
        responseDict = json.loads(response.text)
        for row in responseDict['rows']:
            if row['information']['title'] == pingAnXuanChuanTitle:
                Log.LogOutput(LogLevel.WARN, "找到符合条件的平安宣传，返回id")
                return row['information']['id']
        else:
            Log.LogOutput(LogLevel.WARN, "未找到符合条件的平安宣传，返回None")
            return None
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "未找到符合条件的平安宣传，返回None")
        return False 

'''  
    @功能： 通过实时动态标题获取实时动态ID
    @para: shiShiDongTaiTitle：实时动态标题
    @return: 如果成功，则返回ID；否则返回None  
'''
def get_shishidongtai_id_by_title(shiShiDongTaiTitle = None,username=InitDefaultPara.userInit['DftQuUser'],password='11111111'):
    searchDict = copy.deepcopy(XianSuoGuanLiPara.pingAnXuanChuanSearchDict)
    searchDict['searchInfoVo.information.infoType'] = 1   
    try:
        response = pinganjianshe_post(url='/clueManage/clueInformationManage/findClueInformationPageBySearchsInfoVo.action', postdata=searchDict,username=username, password = password)
        responseDict = json.loads(response.text)
        for row in responseDict['rows']:
            if row['information']['title'] == shiShiDongTaiTitle:
                Log.LogOutput(LogLevel.WARN, "找到符合条件的实时动态，返回id")
                print row['information']['id'] 
                return row['information']['id']
        else:
            Log.LogOutput(LogLevel.WARN, "未找到符合条件的实时动态，返回None")
            return None
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "未找到符合条件的实时动态，返回None")
        return False 


'''  
    @功能：删除所有平安宣传
    @para: 
    @return: 如果成功，则返回True；否则返回False
'''    
   
def delete_all_pinganxuanchuan():
    try:
        Log.LogOutput(message='正在清空所有平安宣传数据...')
        listPara = copy.deepcopy(XianSuoGuanLiPara.pingAnXuanChuanSearchDict)
        response = pinganjianshe_post(url='/clueManage/clueInformationManage/findClueInformationPageBySearchsInfoVo.action', postdata=listPara)
#         print response.text
        responseDict = json.loads(response.text)
        if responseDict['records'] == 0:
            Log.LogOutput(LogLevel.DEBUG, '列表数据为空')
        else:
            #获取ID并删除
            
            for dictListItem in responseDict['rows']:
                delete_one_pinganxuanchuan(dictListItem['information']['id'])      
    except Exception :
        Log.LogOutput(LogLevel.ERROR, '平安宣传删除异常')
        return False
'''  
    @功能：删除所有实时动态
    @para: 
    @return: 如果成功，则返回True；否则返回False
''' 
def delete_all_shishidongtai(): 
    try:
        Log.LogOutput(message='正在清空所有平安宣传数据...')
        listPara = copy.deepcopy(XianSuoGuanLiPara.pingAnXuanChuanSearchDict)
        listPara['searchInfoVo.information.infoType'] = 1
        response = pinganjianshe_post(url='/clueManage/clueInformationManage/findClueInformationPageBySearchsInfoVo.action', postdata=listPara)
        responseDict = json.loads(response.text)
        if responseDict['records'] == 0:
            Log.LogOutput(LogLevel.DEBUG, '列表数据为空')
        else:
            for dictListItem in responseDict['rows']:
                delete_one_shishidongtai(dictListItem['information']['id'])      
    except Exception :
        Log.LogOutput(LogLevel.ERROR, '平安宣传删除异常')
        return False
    
    
      
'''  
    @功能：删除单条平安宣传
    @para: 
    pingAnXuanChuanDelDict：只有一个“ids” key的字典
    @return: 删除成功，则返回True；否则返回False
'''
   
def delete_one_pinganxuanchuan(pingAnXuanChuanDelId,username=InitDefaultPara.userInit['DftQuUser'],password='11111111'):
    pingAnXuanChuanDelDict = {"ids":pingAnXuanChuanDelId}
    response = pinganjianshe_get(url='/clueManage/clueInformationManage/updateInformationDelStateByIds.action', param=pingAnXuanChuanDelDict, username=username, password = password)
    if response.result is True:
        Log.LogOutput(LogLevel.DEBUG, "平安宣传删除成功")
        return True
    else:
        Log.LogOutput(LogLevel.DEBUG, "平安宣传删除失败")
        return False
'''  
    @功能：删除单条实时动态
    @para: 
    pingAnXuanChuanDelDict：只有一个“ids” key的字典
    @return: 删除成功，则返回True；否则返回False
'''    
def delete_one_shishidongtai(shiShiDongTaiDelId,username=InitDefaultPara.userInit['DftQuUser'],password='11111111'):
    pingAnXuanChuanDelDict = {"ids":shiShiDongTaiDelId}
    response = pinganjianshe_get(url='/clueManage/clueInformationManage/updateInformationDelStateByIds.action', param=pingAnXuanChuanDelDict, username=username, password = password)
    if response.result is True:
        Log.LogOutput(LogLevel.DEBUG, "实时动态删除成功")
        return True
    else:
        Log.LogOutput(LogLevel.DEBUG, "实时动态删除失败")
        return False

'''  
    @功能：取消线索用户认证
    @para: 
    clueMobile：取消认证对应的手机号
    @return: 取消认证成功，则返回True；否则返回False
''' 
def disable_clue_user_certify(clueMobile=Global.XianSuoDftMobile,username=InitDefaultPara.userInit['DftQuUser'],password='11111111'):
    cancelDict = {"clueMobile":clueMobile}
    response = pinganjianshe_get(url='/clueManage/clueUserManage/unCertified.action', param=cancelDict, username=username, password = password)
    if response.result is True:
        Log.LogOutput(LogLevel.DEBUG, "取消线索用户认证成功")
        return True
    else:
        Log.LogOutput(LogLevel.DEBUG, "取消线索用户认证失败")
        return False
    pass   

'''  
    @功能：线索用户认证
    @para: 
    enableUserCertifyPara：手机认证字典，调用XianSuoGuanLiIntf的enableUserCertifyPara
    @return: 认证成功，则返回True；否则返回False
''' 
def enable_clue_user_certify(enableUserCertifyPara,username=InitDefaultPara.userInit['DftQuUser'],password='11111111'):
    Log.LogOutput(message='开始进行线索用户认证...')
    response = pinganjianshe_post(url='/clueManage/clueUserManage/userCertified.action', postdata=enableUserCertifyPara, username=username, password = password)
    if response.result is True:
        Log.LogOutput(LogLevel.DEBUG, "线索用户认证成功")
        return True
    else:
        Log.LogOutput(LogLevel.DEBUG, "线索用户认证失败")
        return False
    pass        
    