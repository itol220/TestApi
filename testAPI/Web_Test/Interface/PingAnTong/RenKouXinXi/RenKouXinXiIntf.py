# -*- coding:UTF-8 -*-
'''
Created on 2016-1-28

@author: chenyan
'''
from __future__ import unicode_literals
import json
import copy
from Web_Test.COMMON import Log, CommonUtil
from Web_Test.CONFIG.InitDefaultPara import orgInit
from Web_Test.CONFIG.Define import LogLevel
from Web_Test.Interface.PingAnTong.pingAnTongHttpCommon import pingantong_post
from Web_Test.Interface.PingAnTong.RenKouXinXi import RenKouXinXiPara


'''
    @人口信息 > 人口信息 
    @功能： 新增测试自动化网格下的人口信息的户籍人口
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
'''    
def add_HuJi(HuJiRenKouDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增户籍人口开始..")        
    response = pingantong_post(url='/mobile/householdStaffMobileManage/addHouseholdStaff.action', postdata=HuJiRenKouDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增户籍人口成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增户籍人口失败")
    return response

'''
    @人口信息 > 人口信息 
    @功能： 修改测试自动化网格下的人口信息的户籍人口
    @para: 
    @return: 如果修改成功，则返回True；否则返回False  
'''    
def edit_HuJi(HuJiRenKouDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "修改户籍人口开始..")        
    response = pingantong_post(url='/mobile/householdStaffMobileManage/updateHouseholdStaff.action', postdata=HuJiRenKouDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "修改户籍人口成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "修改户籍人口失败")
    return response

'''  
    @功能： 检查测试自动化网格下的户籍人口信息的详细情况
    @para: getDict：检查时需要传入的字典项
    @return: 如果检查成功，则返回True；否则返回False  
''' 
def check_HuJi(HuJiRenKouDict, populationId = None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查户籍人口详细信息开始..")
    try:
        compDict = copy.deepcopy(RenKouXinXiPara.getHuJiDict)
        compDict['population.id'] = populationId
        response = pingantong_post(url='/mobile/householdStaffMobileManage/getHouseholdStaffById.action', postdata=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(HuJiRenKouDict,[responseDict['actualPopulation']]) is True:  
            Log.LogOutput(LogLevel.DEBUG, "检查到户籍人口的详细信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到户籍人口的详细信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查户籍人口的详细信息失败")
        return False

'''
    @人口信息 > 人口信息 
    @功能： 新增测试自动化网格下的人口信息的流动人口
    @para: 
    @return: 如果添加成功，则返回True；否则返回False  
'''    
def add_LiuDong(LiuDongRenKouDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增流动人口开始..")        
    response = pingantong_post(url='/mobile/floatingPopulationMobileManage/addFloatingPopulation.action', postdata=LiuDongRenKouDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增流动人口成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增流动人口失败")
    return response

'''
    @人口信息 > 人口信息 
    @功能： 修改测试自动化网格下的人口信息的流动人口
    @para: 
    @return: 如果修改成功，则返回True；否则返回False  
'''    
def edit_LiuDong(LiuDongRenKouDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "修改流动人口开始..")        
    response = pingantong_post(url='/mobile/floatingPopulationMobileManage/updateFloatingPopulation.action', postdata=LiuDongRenKouDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "修改流动人口成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "修改流动人口失败")
    return response

'''  
    @功能： 检查测试自动化网格下的流动人口信息的详细情况
    @para: getDict：检查时需要传入的字典项
    @return: 如果检查成功，则返回True；否则返回False  
''' 
def check_LiuDong(HuJiRenKouDict, populationId = None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查流动人口详细信息开始..")
    try:
        compDict = copy.deepcopy(RenKouXinXiPara.getHuJiDict)
        compDict['population.id'] = populationId
        response = pingantong_post(url='/mobile/floatingPopulationMobileManage/getFloatingPopulationById.action', postdata=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(HuJiRenKouDict,[responseDict['actualPopulation']]) is True:  
            Log.LogOutput(LogLevel.DEBUG, "检查到流动人口的详细信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到流动人口的详细信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查流动人口的详细信息失败")
        return False

'''
    @人口信息 > 人口信息 
    @功能： 新增测试自动化网格下的人口信息的境外人口
    @para: 
    @return: 如果添加成功，则返回True；否则返回False  
'''    
def add_JingWai(JingWaiRenKouDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增境外人口开始..")        
    response = pingantong_post(url='/mobile/overseaPersonnelMobileManage/addOverseaPersonnel.action', postdata=JingWaiRenKouDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增境外人口成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增境外人口失败")
    return response

'''
    @人口信息 > 人口信息 
    @功能： 修改测试自动化网格下的人口信息的境外人口
    @para: 
    @return: 如果修改成功，则返回True；否则返回False  
'''    
def edit_JingWai(JingWaiRenKouDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "修改境外人口开始..")        
    response = pingantong_post(url='/mobile/overseaPersonnelMobileManage/updateOverseaPersonnel.action', postdata=JingWaiRenKouDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "修改境外人口成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "修改境外人口失败")
    return response

'''  
    @功能： 检查测试自动化网格下的境外人口信息的详细情况
    @para: getDict：检查时需要传入的字典项
    @return: 如果检查成功，则返回True；否则返回False  
''' 
def check_JingWai(JingWaiRenKouDict, overseaPersonnelId = None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查境外人口详细信息开始..")
    try:
        compDict = copy.deepcopy(RenKouXinXiPara.getJingWaiDict)
        compDict['overseaPersonnel.id'] = overseaPersonnelId
        response = pingantong_post(url='/mobile/overseaPersonnelMobileManage/getOverseaPersonnelById.action', postdata=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(JingWaiRenKouDict, [responseDict['actualPopulation']]) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到境外人口的详细信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到境外人口的详细信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查境外人口信息失败")
        return False

'''  
    @功能： 检查测试自动化网格下的人口信息
    @para: getOrgDict：检查时需要传入的字典项
    @return: 如果检查成功，则返回True；否则返回False  
''' 
def check_Population(renKouDict, orgId = None,populationType = None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查人口信息开始..")
    try:
        compDict = copy.deepcopy(RenKouXinXiPara.getOrgDict)
        compDict['orgId'] = orgId
        compDict['populationType'] = populationType
        response = pingantong_post(url='/mobile/commonPopulationMobileManage/findCommonPopulationList.action', postdata=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(renKouDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到人口信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到人口信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查人口信息失败")
        return False

'''  
    @功能： 搜索测试自动化网格下的人口信息
    @para: getOrgDict：检查时需要传入的字典项
    @return: 如果搜索成功，则返回True；否则返回False  
''' 
def search_Population(renKouDict, populationType = None, name=None, idCardNo=None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "搜索人口信息开始..")
    try:
        compDict = copy.deepcopy(RenKouXinXiPara.getOrgDict)
        compDict['orgId'] = orgInit['DftWangGeOrgId']
        compDict['populationType'] = populationType
        compDict['searchCondition.name'] = name
        compDict['searchCondition.idCardNo'] = idCardNo
        response = pingantong_post(url='/mobile/commonPopulationMobileManage/findCommonPopulationList.action', postdata=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(renKouDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "搜索到人口信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未搜索到人口信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "搜索人口信息失败")
        return False

'''
    @人口信息 > 人口信息 
    @功能： 添加测试自动化网格下的户籍人口的服务记录信息
    @para: 
    @return: 如果添加成功，则返回True；否则返回False  
'''    
def add_serviceRecord(serviceRecordDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "添加户籍人口的服务记录信息开始..")        
    response = pingantong_post(url='/mobile/serviceRecordMobileManage/addServiceRecordForMobile.action', postdata=serviceRecordDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "添加户籍人口的服务记录信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "添加户籍人口的服务记录信息失败")
    return response

'''
    @人口信息 > 人口信息 
    @功能： 删除测试自动化网格下的户籍人口的服务记录信息
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
'''    
def delete_serviceRecord(serviceRecordDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "删除户籍人口的服务记录信息开始..")        
    response = pingantong_post(url='/mobile/serviceTeam/deleteServiceRecordForMobile.action', postdata=serviceRecordDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除户籍人口的服务记录信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "删除户籍人口的服务记录信息失败")
    return response

'''  
    @功能： 检查测试自动化网格下户籍人口中的服务记录信息
    @para: getOrgDict：检查时需要传入的字典项
    @return: 如果检查成功，则返回True；否则返回False  
''' 
def check_serviceRecord(serviceRecordDict, objectIds = None ,populationType = None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查户籍人口中的服务记录信息开始..")
    try:
        compDict = copy.deepcopy(RenKouXinXiPara.getServiceRecordDict)
        compDict['objectIds'] = objectIds
        compDict['serviceRecordVo.organization.id'] = orgInit['DftWangGeOrgId']
        compDict['populationType'] = populationType
        response = pingantong_post(url='/mobile/serviceRecordMobileManage/findServiceRecordByQueryConditionForMobile.action', postdata=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(serviceRecordDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到户籍人口中的服务记录信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到户籍人口中的服务记录信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查户籍人口中的服务记录信息失败")
        return False
    
'''
    @人口信息 > 人口信息 
    @功能： 修改测试自动化网格下的户籍人口的服务记录信息
    @para: 
    @return: 如果修改成功，则返回True；否则返回False  
'''    
def edit_serviceRecord(serviceRecordDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "修改户籍人口的服务记录信息开始..")        
    response = pingantong_post(url='/mobile/serviceRecordMobileManage/updateServiceRecordForMobile.action', postdata=serviceRecordDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "修改户籍人口的服务记录信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "修改户籍人口的服务记录信息失败")
    return response

'''  
    @功能： 检查测试自动化网格下户籍人口中服务记录的详细信息
    @para: getOrgDict：检查时需要传入的字典项
    @return: 如果检查成功，则返回True；否则返回False  
''' 
def check_Record(serviceRecordDict, serviceRecordId = None ,username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查户籍人口中服务记录详的细信息开始..")
    try:
        compDict = copy.deepcopy(RenKouXinXiPara.getRecordDict)
        compDict['serviceRecord.id'] = serviceRecordId
        response = pingantong_post(url='/mobile/serviceRecordMobileManage/viewServiceRecordForMobile.action', postdata=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(serviceRecordDict, [responseDict]) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到户籍人口中服务记录详的细信信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到户籍人口中服务记录详的细信信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查户籍人口中服务记录详的细信信息失败")
        return False
    
    
'''
    @人口信息 > 人口信息 
    @功能： 新增测试自动化网格下的刑释人员
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
'''    
def add_XingShiRenYuan(xingShiDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增刑释人员开始..")        
    response = pingantong_post(url='/mobile/positiveInfoMobileManage/addPositiveInfo.action', postdata=xingShiDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增刑释人员成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增刑释人员失败")
    return response

'''
    @人口信息 > 人口信息 
    @功能： 修改测试自动化网格下的刑释人员
    @para: 
    @return: 如果修改成功，则返回True；否则返回False  
'''    
def edit_XingShiRenYuan(xingShiDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "修改刑释人员开始..")        
    response = pingantong_post(url='/mobile/positiveInfoMobileManage/updatePositiveInfo.action', postdata=xingShiDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "修改刑释人员成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "修改刑释人员失败")
    return response

'''  
    @功能： 检查测试自动化网格下的刑释人员信息的详细情况
    @para: getDict：检查时需要传入的字典项
    @return: 如果检查成功，则返回True；否则返回False  
''' 
def check_XingShi(xingShiDict, populationId = None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查刑释人员详细信息开始..")
    try:
        compDict = copy.deepcopy(RenKouXinXiPara.getHuJiDict)
        compDict['population.id'] = populationId
        response = pingantong_post(url='/mobile/positiveInfoMobileManage/getPositiveInfoById.action', postdata=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(xingShiDict,[responseDict['population']]) is True:  
            Log.LogOutput(LogLevel.DEBUG, "检查到刑释人员的详细信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到刑释人员的详细信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查刑释人员的详细信息失败")
        return False


'''
    @人口信息 > 人口信息 
    @功能： 新增测试自动化网格下的矫正人员
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
'''    
def add_jiaoZhengRenYuan(jiaoZhengDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增矫正人员开始..")        
    response = pingantong_post(url='/mobile/rectificativePersonMobileManage/addRectificativePerson.action', postdata=jiaoZhengDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增矫正人员成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增矫正人员失败")
    return response

'''
    @人口信息 > 人口信息 
    @功能： 修改测试自动化网格下的矫正人员
    @para: 
    @return: 如果修改成功，则返回True；否则返回False  
'''    
def edit_jiaoZhengRenYuan(jiaoZhengDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "修改矫正人员开始..")        
    response = pingantong_post(url='/mobile/rectificativePersonMobileManage/updateRectificativePerson.action', postdata=jiaoZhengDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "修改矫正人员成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "修改矫正人员失败")
    return response

'''  
    @功能： 检查测试自动化网格下的矫正人员信息的详细情况
    @para: getDict：检查时需要传入的字典项
    @return: 如果检查成功，则返回True；否则返回False  
''' 
def check_jiaoZheng(jiaoZhengDict, populationId = None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查矫正人员详细信息开始..")
    try:
        compDict = copy.deepcopy(RenKouXinXiPara.getHuJiDict)
        compDict['population.id'] = populationId
        response = pingantong_post(url='/mobile/rectificativePersonMobileManage/getRectificativePersonById.action', postdata=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(jiaoZhengDict,[responseDict['population']]) is True:  
            Log.LogOutput(LogLevel.DEBUG, "检查到矫正人员的详细信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到矫正人员的详细信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查矫正人员的详细信息失败")
        return False
    
    
'''
    @人口信息 > 人口信息 
    @功能： 新增测试自动化网格下的精神病人员
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
'''    
def add_jingShenBingRenYuan(jingShenBingDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增精神病人员开始..")        
    response = pingantong_post(url='/mobile/mentalPatientMobileManage/addMentalPatient.action', postdata=jingShenBingDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增精神病人员成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增精神病人员失败")
    return response

'''
    @人口信息 > 人口信息 
    @功能： 修改测试自动化网格下的精神病人员
    @para: 
    @return: 如果修改成功，则返回True；否则返回False  
'''    
def edit_jingShenBingRenYuan(jingShenBingDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "修改精神病人员开始..")        
    response = pingantong_post(url='/mobile/mentalPatientMobileManage/updateMentalPatient.action', postdata=jingShenBingDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "修改精神病人员成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "修改精神病人员失败")
    return response

'''  
    @功能： 检查测试自动化网格下的精神病人员信息的详细情况
    @para: getDict：检查时需要传入的字典项
    @return: 如果检查成功，则返回True；否则返回False  
''' 
def check_jingSheng(jingShenBingDict, populationId = None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查精神病人员详细信息开始..")
    try:
        compDict = copy.deepcopy(RenKouXinXiPara.getHuJiDict)
        compDict['population.id'] = populationId
        response = pingantong_post(url='/mobile/mentalPatientMobileManage/getMentalPatientById.action', postdata=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(jingShenBingDict,[responseDict['population']]) is True:  
            Log.LogOutput(LogLevel.DEBUG, "检查到精神病人员的详细信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到精神病人员的详细信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查精神病人员的详细信息失败")
        return False
    
        
'''
    @人口信息 > 人口信息 
    @功能： 新增测试自动化网格下的吸毒人员
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
'''    
def add_xiDuRenYuan(xiDuDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增吸毒人员开始..")        
    response = pingantong_post(url='/mobile/druggyMobileManage/addDruggy.action', postdata=xiDuDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增吸毒人员成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增吸毒人员失败")
    return response

'''
    @人口信息 > 人口信息 
    @功能： 修改测试自动化网格下的吸毒人员
    @para: 
    @return: 如果修改成功，则返回True；否则返回False  
'''    
def edit_xiDuRenYuan(xiDuDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "修改吸毒人员开始..")        
    response = pingantong_post(url='/mobile/druggyMobileManage/updateDruggy.action', postdata=xiDuDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "修改吸毒人员成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "修改吸毒人员失败")
    return response

'''  
    @功能： 检查测试自动化网格下的吸毒人员信息的详细情况
    @para: getDict：检查时需要传入的字典项
    @return: 如果检查成功，则返回True；否则返回False  
''' 
def check_xiDu(xiDuDict, populationId = None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查吸毒人员详细信息开始..")
    try:
        compDict = copy.deepcopy(RenKouXinXiPara.getHuJiDict)
        compDict['population.id'] = populationId
        response = pingantong_post(url='/mobile/druggyMobileManage/getDruggyById.action', postdata=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(xiDuDict,[responseDict['population']]) is True:  
            Log.LogOutput(LogLevel.DEBUG, "检查到吸毒人员的详细信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到吸毒人员的详细信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查吸毒人员的详细信息失败")
        return False
    
'''
    @人口信息 > 人口信息 
    @功能： 新增测试自动化网格下的重点青少年
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
'''    
def add_zhongDianQingShaoNian(qingShaoNianDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增重点青少年开始..")        
    response = pingantong_post(url='/mobile/idleYouthMobileManage/addIdleYouth.action', postdata=qingShaoNianDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增重点青少年成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增重点青少年失败")
    return response

'''
    @人口信息 > 人口信息 
    @功能： 修改测试自动化网格下的重点青少年
    @para: 
    @return: 如果修改成功，则返回True；否则返回False  
'''    
def edit_zhongDianQingShaoNian(qingShaoNianDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "修改重点青少年开始..")        
    response = pingantong_post(url='/mobile/idleYouthMobileManage/updateIdleYouth.action', postdata=qingShaoNianDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "修改重点青少年成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "修改重点青少年失败")
    return response

'''  
    @功能： 检查测试自动化网格下的重点青少年信息的详细情况
    @para: getDict：检查时需要传入的字典项
    @return: 如果检查成功，则返回True；否则返回False  
''' 
def check_zhongDianQingShaoNian(qingShaoNianDict, populationId = None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查重点青少年详细信息开始..")
    try:
        compDict = copy.deepcopy(RenKouXinXiPara.getHuJiDict)
        compDict['population.id'] = populationId
        response = pingantong_post(url='/mobile/idleYouthMobileManage/getIdleYouthById.action', postdata=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(qingShaoNianDict,[responseDict['population']]) is True:  
            Log.LogOutput(LogLevel.DEBUG, "检查到重点青少年的详细信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到重点青少年的详细信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查重点青少年的详细信息失败")
        return False
    
    
'''
    @人口信息 > 人口信息 
    @功能： 新增测试自动化网格下的重点上访人员
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
'''    
def add_shangFangRenYuan(shangFangDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增重点上访人员开始..")        
    response = pingantong_post(url='/mobile/superiorVisitMobileManage/addSuperiorVisit.action', postdata=shangFangDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增重点上访人员成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增重点上访人员失败")
    return response

'''
    @人口信息 > 人口信息 
    @功能： 修改测试自动化网格下的重点上访人员
    @para: 
    @return: 如果修改成功，则返回True；否则返回False  
'''    
def edit_shangFangRenYuan(shangFangDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "修改重点上访人员开始..")        
    response = pingantong_post(url='/mobile/superiorVisitMobileManage/updateSuperiorVisit.action', postdata=shangFangDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "修改重点上访人员成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "修改重点上访人员失败")
    return response

'''  
    @功能： 检查测试自动化网格下的重点上访人员信息的详细情况
    @para: getDict：检查时需要传入的字典项
    @return: 如果检查成功，则返回True；否则返回False  
''' 
def check_shangFangRenYuan(shangFangDict, populationId = None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查重点上访人员详细信息开始..")
    try:
        compDict = copy.deepcopy(RenKouXinXiPara.getHuJiDict)
        compDict['population.id'] = populationId
        response = pingantong_post(url='/mobile/superiorVisitMobileManage/getSuperiorVisitById.action', postdata=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(shangFangDict,[responseDict['population']]) is True:  
            Log.LogOutput(LogLevel.DEBUG, "检查到重点上访人员的详细信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到重点上访人员的详细信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查重点上访人员的详细信息失败")
        return False

    
'''
    @人口信息 > 人口信息 
    @功能： 新增测试自动化网格下的危险品从业人员
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
'''    
def add_practitioner(weiXianPinDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增危险品从业人员开始..")        
    response = pingantong_post(url='/mobile/dangerousGoodsPractitionerMobileManage/addDangerousGoodsPractitioner.action', postdata=weiXianPinDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增危险品从业人员成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增危险品从业人员失败")
    return response

'''
    @人口信息 > 人口信息 
    @功能： 修改测试自动化网格下的危险品从业人员
    @para: 
    @return: 如果修改成功，则返回True；否则返回False  
'''    
def edit_practitioner(weiXianPinDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "修改危险品从业人员开始..")        
    response = pingantong_post(url='/mobile/dangerousGoodsPractitionerMobileManage/updateDangerousGoodsPractitioner.action', postdata=weiXianPinDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "修改危险品从业人员成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "修改危险品从业人员失败")
    return response

'''  
    @功能： 检查测试自动化网格下的危险品从业人员信息的详细情况
    @para: getDict：检查时需要传入的字典项
    @return: 如果检查成功，则返回True；否则返回False  
''' 
def check_practitioner(weiXianPinDict, populationId = None, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "检查危险品从业人员详细信息开始..")
    try:
        compDict = copy.deepcopy(RenKouXinXiPara.getHuJiDict)
        compDict['population.id'] = populationId
        response = pingantong_post(url='/mobile/dangerousGoodsPractitionerMobileManage/getDangerousGoodsPractitionerById.action', postdata=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(weiXianPinDict,[responseDict['population']]) is True:  
            Log.LogOutput(LogLevel.DEBUG, "检查到危险品从业人员的详细信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到危险品从业人员的详细信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查危险品从业人员的详细信息失败")
        return False
