# -*- coding:UTF-8 -*-
'''
Created on 2016-12-9

@author: chenhui
'''
from __future__ import unicode_literals
from COMMON import Log, CommonUtil
from COMMON.CommonUtil import findDictInDictlist
from CONFIG import InitDefaultPara
from CONFIG.Define import LogLevel
from Interface.XianSuoApp.ShouYe import XsShouYePara
from Interface.XianSuoApp.xianSuoHttpCommon import xiansuo_post, xiansuo_get
import copy
import json

'''
    @功能： 获取首页滚动公告
    @para: {    'tqmobile':'true',
                    'departmentNo':InitDefaultPara.xianSuoOrgInit['DftQuOrgIdNo']
                }
    @return:   response
    @author:  chenhui 2016-12-9
'''
def get_roll_operation_notice_list(para):
    info='获取首页滚动公告'
    Log.LogOutput(message=info)
    response = xiansuo_get(url='/api/clue/personalizedConfigurationDubboService/findRollInformationByDepartmentNo', param=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功")
    else:
            Log.LogOutput(LogLevel.ERROR, info+"失败")
    return response
'''
    @功能：检查首页滚动公告
    @para：
    checkHighLightPara：首页滚动公告信息，请调用XsShouYePara中的gunDongGongGaoJianCha
    @return:    检查成功返回True,否则返回False
    @author: gaorong 2016-12-22
'''   
def check_scroll_info(checkscrollPara):
    Log.LogOutput(LogLevel.INFO, "检查首页滚动公告信息开始......")
    try:
        response = xiansuo_get(url='/api/clue/personalizedConfigurationDubboService/findRollInformationByDepartmentNo', param=checkscrollPara)
        responseDict = json.loads(response.text)
        if findDictInDictlist(checkscrollPara, responseDict['response']['module']) is True:
            Log.LogOutput(LogLevel.INFO, "首页滚动公告检查成功")
            return True
        else:
            Log.LogOutput(LogLevel.WARN, "首页滚动公告检查失败")
            return False
    except Exception:
        Log.LogOutput(LogLevel.WARN, "首页滚动公告检查过程失败")
        return False


'''
    @功能： 检查运维平台公告列表 
    @para: checkpara:  XsShouYePara.gunDongGongGaoJianCha
                    listpara:   {    'tqmobile':'true',
                                        'departmentNo':InitDefaultPara.xianSuoOrgInit['DftQuOrgIdNo']
                                    }
    @return: response
    @author:  chenhui 2016-12-9
'''
def check_roll_operation_notice_list(checkpara,listpara):
    info='检查运维平台公告列表'
    Log.LogOutput(LogLevel.INFO, info)
    try:
        response = get_roll_operation_notice_list(para=listpara)
        responseDict=json.loads(response.text)
#         #print response.text
        if findDictInDictlist(checkpara,responseDict['response']['module']) is True:
            Log.LogOutput(LogLevel.DEBUG, info+"成功!")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, info+'出现异常')
            return False

'''
    @功能： 获取便民服务信息
    @para:     XsShouYePara.convenienceServiceList
    @return:   response
    @author:  chenhui 2016-12-20
'''
def get_convenience_service_list_for_mobile(para):
    info='获取手机端便民服务信息列表'
    Log.LogOutput(message=info)
    response = xiansuo_post(url='/api/clue/personalizedConfigurationDubboService/findConvenienceServicesByMobileTypeNew', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功")
    else:
            Log.LogOutput(LogLevel.ERROR, info+"失败")
    return response

'''
    @功能： 检查便民服务信息列表 
    @para: checkpara:  XsShouYePara.gunDongGongGaoJianCha
                    listpara:   XsShouYePara.convenienceServiceList
    @return: response
    @author:  chenhui 2016-12-20
'''
def check_convenience_service_list_for_mobile(checkpara,listpara):
    info='检查便民服务信息列表'
    Log.LogOutput(LogLevel.INFO, info)
    try:
        response = get_convenience_service_list_for_mobile(para=listpara)
        responseDict=json.loads(response.text)
#         #print response.text
        if findDictInDictlist(checkpara,responseDict['response']['module']) is True:
            Log.LogOutput(LogLevel.DEBUG, info+"成功!")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, info+'出现异常')
            return False
        
'''
    @功能： 获取常用电话分类信息
    @para:     XsShouYePara.getMobileCategoryListPara
    @return:   response
    @author:  chenhui 2016-12-21
'''
def get_mobile_category_list_for_mobile(para):
    info='获取手机端常用电话分类信息列表'
    Log.LogOutput(message=info)
    response = xiansuo_post(url='/api/clue/companyPhoneDubboService/findCompanyPhoneListForMobile', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功")
    else:
            Log.LogOutput(LogLevel.ERROR, info+"失败")
    return response

'''
    @功能： 手机端检查常用电话分类列表 
    @para: checkpara:  XsShouYePara.checkMobileCategoryListPara
                    listpara:   XsShouYePara.getMobileCategoryListPara
    @return: response
    @author:  chenhui 2016-12-21
'''
def check_mobile_category_list_for_mobile(listpara,checkpara):
    info='手机端检查常用电话分类列表'
    Log.LogOutput(LogLevel.INFO, info)
    try:
        response = get_mobile_category_list_for_mobile(para=listpara)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['response']['module']['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, info+"成功!")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, info+'出现异常')
            return False
        
'''
    @功能： 获取电话管理列表信息
    @para:     XsShouYePara.getMobileListPara
    @return:   response
    @author:  chenhui 2016-12-22
'''
def get_mobile_list_for_mobile(para):
    info='获取手机端电话管理列表信息'
    Log.LogOutput(message=info)
    response = xiansuo_post(url='/api/clue/companyPhoneDubboService/findCompanyPhoneListByCompanyName', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功")
    else:
            Log.LogOutput(LogLevel.ERROR, info+"失败")
    return response

'''
    @功能： 手机端检查常用电话分类列表 
    @para: checkpara:  XsShouYePara.checkMobileListPara
                    listpara:   XsShouYePara.getMobileListPara
    @return: response
    @author:  chenhui 2016-12-22
'''
def check_mobile_list_for_mobile(listpara,checkpara):
    info='手机端检查电话管理列表'
    Log.LogOutput(LogLevel.INFO, info)
    try:
        response = get_mobile_list_for_mobile(para=listpara)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['response']['module']['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, info+"成功!")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, info+'出现异常')
            return False
        
'''
    @功能： 手机端通过单位名称获取排序号
    @para:    'companyName'
    @return:  如果找到，返回排列序号，如果没找到，则返回-1，如果异常，返回-2
    @author:  chenhui 2016-12-21
'''
def get_mobile_display_seq_by_name_for_mobile(para):
    info='手机端通过单位名称获取排序号'
    Log.LogOutput(LogLevel.INFO, info)
    listpara=copy.deepcopy(XsShouYePara.getMobileListPara)
    try:
        response = get_mobile_list_for_mobile(para=listpara)
        resDict=json.loads(response.text)
#         print response.text
        for item in resDict['response']['module']['rows']:
            if item['companyName']==para:
                Log.LogOutput(LogLevel.INFO, info+'成功')
                return item['seq']
        Log.LogOutput(LogLevel.INFO, info+'失败')
        return -1 
    except Exception:
        Log.LogOutput(LogLevel.ERROR, info+'出现异常')
        return -2
'''
    @功能： 手机端检查区县开通列表
    @para:     listpara:    XsShouYePara.orgOpenStateListForMobilePara
                    checkpara:XsShouYePara.checkOrgOpenStateListForMobilePara
    @return:  true/false
    @author:  chenhui 2016-12-22
'''
def check_org_open_state_list_for_mobile(listpara,checkpara):
    info='手机端检查区县开通列表'
    Log.LogOutput(LogLevel.INFO, info)
    try:
        response = xiansuo_get(url='/api/clue/areaAcquisitionDubboService/findStreetOrganizationsByCountyOrgId', param=listpara)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['response']['module']) is True:
            Log.LogOutput(LogLevel.DEBUG, info+"成功!")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, info+'出现异常')
            return False    
        
'''
    @功能： 获取轮播列表信息
    @para:     XsShouYePara.getLunBoListForMobilePara
    @return:   response
    @author:  chenhui 2016-12-26
'''
def get_lunbo_list_for_mobile(para):
    info='获取轮播列表信息'
    Log.LogOutput(message=info)
    response = xiansuo_post(url='/api/clue/personalizedConfigurationDubboService/findEventConfigurationsByMobileTypeNew', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功")
    else:
            Log.LogOutput(LogLevel.ERROR, info+"失败")
    return response

'''
    @功能： 手机端检查首页轮播图列表
    @para:     listpara:    XsShouYePara.getLunBoListForMobilePara
                    checkpara:XsShouYePara.checkLunBoListForMobilePara
    @return:  true/false
    @author:  chenhui 2016-12-26
'''
def check_lunbo_list_for_mobile(listpara,checkpara):
    info='手机端检查首页轮播图列表'
    Log.LogOutput(LogLevel.INFO, info)
    try:
        response = get_lunbo_list_for_mobile(listpara)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['response']['module']) is True:
            Log.LogOutput(LogLevel.DEBUG, info+"成功!")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, info+'出现异常')
            return False
        
'''
    @功能： 通过标题名称获取排序号
    @para:     
                    title        标题
    @return:  如果找到，返回排列序号，如果没找到，则返回-1，如果异常，返回-2
    @author:  chenhui 2016-12-27
'''
def get_lunbo_seq_by_title_for_mobile(title):
    info='通过标题名称获取排序号'
    Log.LogOutput(LogLevel.INFO, info)
    listpara=copy.deepcopy(XsShouYePara.getLunBoListForMobilePara)
    try:
        response = get_lunbo_list_for_mobile(para=listpara)
        resDict=json.loads(response.text)
#         #print response.text
        for item in resDict['response']['module']:
            if item['title']==title:
                Log.LogOutput(LogLevel.INFO, info+'成功')
                return item['seq']
        Log.LogOutput(LogLevel.INFO, info+'失败')
        return -1
    except Exception:
        Log.LogOutput(LogLevel.ERROR, info+'出现异常')
        return -2
    
'''
    @功能： 通过内容检查首页精彩推荐
    @para: compareDict请调用XianSuoGuanLiPara里面的jingCaiTuiJianSearchResult,searchDict ={'tqmobile':'true','departmentNo':InitDefaultPara.xianSuoOrgInit['DftQuOrgIdNo'],}
    @return: 精彩推荐中匹配到内容，返回True,未检查到，返回False
    @author:  maoxiaoyu 2016-12-21
'''
def check_shouye_jingcaituijian_result(compareDict = None,searchDict = None,username=InitDefaultPara.userInit['DftQuUser'],password='11111111'):
    try:
        response = xiansuo_get(url='/api/clue/informationDubboService/findWonderfulRecommendList', param=searchDict)
        if response.result is False:
            Log.LogOutput(LogLevel.ERROR, "未检查到符合搜索条件的精彩推荐")
            return False
        else:
            responseDict = json.loads(response.text)
            for module in responseDict['response']['module']:
                if CommonUtil.findDictInDictlist(compareDict, [module]) is True:
                    Log.LogOutput(LogLevel.DEBUG, "检查到符合条件的精彩推荐")
                    return True
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "未检查到符合搜索条件的精彩推荐")
        return False   