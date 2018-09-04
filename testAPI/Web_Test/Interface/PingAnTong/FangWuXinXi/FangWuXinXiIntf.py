# -*- coding:UTF-8 -*-
'''
Created on 2016-3-8

@author: chanyan
'''
from __future__ import unicode_literals
import json
import copy
# from COMMON import Log, CommonUtil
from Web_Test.COMMON import Log, CommonUtil
from Web_Test.CONFIG.InitDefaultPara import orgInit
from Web_Test.CONFIG.Define import LogLevel
from Web_Test.Interface.PingAnTong.pingAnTongHttpCommon import pingantong_post
from Web_Test.Interface.PingAnTong.FangWuXinXi import FangWuXinXiPara


'''
    @房屋信息 > 房屋信息 
    @功能： 新增测试自动化网格下的房屋信息
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
'''    
def add_FangWu(FangWuDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增房屋信息开始..")        
    response = pingantong_post(url='/mobile/actualHouseMobileManage/addActualHouse.action', postdata=FangWuDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增房屋信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增房屋信息失败")
    return response

'''  
    @功能： 检查测试自动化网格下的房屋信息
    @para: 
    @return: 如果检查成功，则返回True；否则返回False  
'''
def check_House(fangWuDict, orgId=None, username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "检查房屋信息开始..")
    try:
        compDict = copy.deepcopy(FangWuXinXiPara.getHouseDict)
        compDict['orgId']= orgId
        response = pingantong_post(url='/mobile/actualHouseMobileManage/findActualHouseList.action', postdata=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(fangWuDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到房屋信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到房屋信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查房屋信息失败")
        return False

'''
    @房屋信息 > 房屋信息 
    @功能： 修改测试自动化网格下的房屋信息
    @para: 
    @return: 如果修改成功，则返回True；否则返回False  
'''    
def edit_FangWu(FangWuDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "修改房屋信息开始..")        
    response = pingantong_post(url='/mobile/actualHouseMobileManage/updateActualHouse.action', postdata=FangWuDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "修改房屋信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "修改房屋信息失败")
    return response    
    
'''  
    @功能： 检查测试自动化网格下房屋信息的详细信息
    @para: 
    @return: 如果检查成功，则返回True；否则返回False  
'''
def check_FangWu(fangWuDict, houseInfoId=None, username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "检查房屋的详细信息开始..")
    try:
        compDict = copy.deepcopy(FangWuXinXiPara.getFangWuDict)
        compDict['houseInfo.id']= houseInfoId
        response = pingantong_post(url='/mobile/actualHouseMobileManage/getActualHouseById.action', postdata=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(fangWuDict, [responseDict['houseInfo']]) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到房屋的详细信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到房屋的详细信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查房屋的详细信息失败")
        return False
    
'''  
    @功能： 搜素测试自动化网格下的房屋信息
    @para: 
    @return: 如果搜素成功，则返回True；否则返回False  
'''
def search_House(fangWuDict, orgId=None, address=None, username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "搜素房屋信息开始..")
    try:
        compDict = copy.deepcopy(FangWuXinXiPara.searchHouseDict)
        compDict['orgId'] = orgId
        compDict['searchHouseInfoVo.address'] = address
        response = pingantong_post(url='/mobile/actualHouseMobileManage/findActualHouseList.action', postdata=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(fangWuDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "搜素到房屋信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未搜素到房屋信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "搜素房屋信息失败")
        return False
    
'''  
    @功能： 添加测试自动化网格下房屋的住户信息
    @para: 
    @return: 如果添加成功，则返回True；否则返回False  
'''
def add_ZhuHuXinXi(zhuHuDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增住户信息开始..")
    response = pingantong_post(url='/mobile/actualHousePopulationMobileManage/addHouseHasActualPopulation.action', postdata=zhuHuDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增住户信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增住户信息失败")
    return response   

'''  
    @功能： 删除测试自动化网格下房屋的住户信息
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
'''
def delete_ZhuHuXinXi(zhuHuDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "删除住户信息开始..")
    response = pingantong_post(url='/mobile/actualHousePopulationMobileManage/deleteHouseHasActualPopulation.action', postdata=zhuHuDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除住户信息成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "删除住户信息失败")
    return response  

'''  
    @功能： 检查测试自动化网格下房屋中的住户信息
    @para: 
    @return: 如果检查成功，则返回True；否则返回False  
'''
def check_ZhuHuXinXi(zhuHuDict, orgId=None, houseId=None, username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "检查房屋住户信息开始..")
    try:
        compDict = copy.deepcopy(FangWuXinXiPara.getzhuHuDict)
        compDict['orgId']= orgId
        compDict['houseId']= houseId
        response = pingantong_post(url='/mobile/actualHousePopulationMobileManage/findLivingInHousePopulationInfos.action', postdata=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(zhuHuDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到房屋住户信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到房屋住户信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查房屋住户信息失败")
        return False

'''
    @房屋信息 > 出租房 
    @功能： 新增测试自动化网格下的出租房
    @para: 
    @return: 如果新增成功，则返回True；否则返回False  
'''    
def add_ChuZuFang(ChuZuFangDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增出租房开始..")        
    response = pingantong_post(url='/mobile/rentalHouseMobileManage/addRentalHouse.action', postdata=ChuZuFangDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增出租房成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "新增出租房失败")
    return response   

'''
    @房屋信息 > 出租房 
    @功能： 修改测试自动化网格下的出租房
    @para: 
    @return: 如果修改成功，则返回True；否则返回False  
'''    
def edit_ChuZuFang(ChuZuFangDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "修改出租房开始..")        
    response = pingantong_post(url='/mobile/rentalHouseMobileManage/updateRentalHouse.action', postdata=ChuZuFangDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "修改出租房成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "修改出租房失败")
    return response  

'''  
    @功能： 检查测试自动化网格下出租房的详细信息
    @para: 
    @return: 如果检查成功，则返回True；否则返回False  
'''
def check_ChuZuFang(fangWuDict, houseInfoId=None, username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "检查出租房的详细信息开始..")
    try:
        compDict = copy.deepcopy(FangWuXinXiPara.getFangWuDict)
        compDict['houseInfo.id']= houseInfoId
        response = pingantong_post(url='/mobile/rentalHouseMobileManage/getRentalHouseById.action', postdata=compDict,username=username, password = password)  
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(fangWuDict, [responseDict['rentalHouse']]) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查到出租房的详细信息")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "未检查到出租房的详细信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "检查出租房的详细信息失败")
        return False
    
