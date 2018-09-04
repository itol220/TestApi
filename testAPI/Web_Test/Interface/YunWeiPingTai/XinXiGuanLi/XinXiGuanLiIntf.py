# -*- coding:UTF-8 -*-
'''
Created on 2015-11-24

@author: N-133
'''
from __future__ import unicode_literals
from COMMON import Log, CommonUtil
from COMMON.CommonUtil import findDictInDictlist
from CONFIG.Define import LogLevel
from CONFIG.InitDefaultPara import clueOrgInit
from Interface.XianSuoApp.xianSuoHttpCommon import xiansuo_post
from Interface.YunWeiPingTai.XiTongPeiZhi import XiTongPeiZhiPara, \
    XiTongPeiZhiIntf
from Interface.YunWeiPingTai.XinXiGuanLi import XinXiGuanLiPara
from Interface.YunWeiPingTai.XinXiGuanLi.XinXiGuanLiPara import \
    PersonalConfigListPara
from Interface.YunWeiPingTai.yunWeiPingTaiHttpCommon import xiansuoyunwei_post, \
    xiansuoyunwei_get
import copy
import json




# 新增线索
def AddXianSuo(XianSuoDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增线索开始")
    response = xiansuo_post(url='/api/clue/informationDubboService/addInformationForMobile', postdata=XianSuoDict)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "新增线索成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "新增线索失败")
    return response

'''  
    @功能： 在运维平台爆料列表中通过爆料内容获取id
    @para: 
    clueContent:爆料内容
    @return: 如果查找内容成功，则返回id；否则返回None  
    @author:  gaorong 2016-12-05
'''  
def get_clue_id_by_content(clueContent):
    lispara = copy.deepcopy(XinXiGuanLiPara.chakanxiansuo) 
    Log.LogOutput(LogLevel.INFO, "在爆料列表中通过爆料内容获取id信息...")
    try:
        response = xiansuoyunwei_post(url='/informationManage/findInformationList', postdata=lispara)
#         print response.text
        responseDict = json.loads(response.text) 
        if responseDict['records']==0:
            Log.LogOutput(LogLevel.DEBUG, "爆料列表未空，无法找到ID，返回None")
            return None
        #调用检查列表参数
        for item in responseDict['rows']:
            if item['information']['contentText'] == clueContent:
                Log.LogOutput(LogLevel.DEBUG, "在爆料列表查看到爆料信息,返回id")
                return item['information']['id']
        Log.LogOutput(LogLevel.WARN, "无法在爆料列表查看到对应爆料信息")
        return None
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '通过爆料内容获取爆料id异常')
        return None 
    
'''  
    @功能： 在运维平台爆料管理中检查线索是否存在
    @para: 
    clueCheckDict：待检查的线索，请调用XinXiGuanLiPara中的jianchaxiansuo字典
    @return: 如果检查成功，则返回True；否则返回False  
'''
def check_clue_in_cluelist_manage(clueCheckDict=None,getClueList=None):
    try:
        Log.LogOutput(LogLevel.INFO, "查找线索开始")
        if getClueList is None:
            getClueList = copy.deepcopy(XinXiGuanLiPara.chakanxiansuo)
        response = xiansuoyunwei_post(url='/informationManage/findInformationList', postdata=getClueList)
#         print response.text
        responseDict = json.loads(response.text)
        listDict= responseDict['rows']
        newList=[]
        for item in listDict:
            newList.append(item['information'])
        if findDictInDictlist(clueCheckDict, newList) is True:
            Log.LogOutput(LogLevel.DEBUG, "查找线索成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查找线索失败")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '查找线索异常')
        return False  

def viewSchedule(para):
    Log.LogOutput(LogLevel.INFO, "查看进度开始")
    response = xiansuo_post(url='/api/clue/informationDubboService/findInformationsForPageByUserId', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "查看进度成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "查看进度失败")
    return response

# 在我的进度中查看新增的爆料信息    
def checkClueInSchedule(checkPara,listPara):
    try:
        Log.LogOutput(LogLevel.INFO, "检查记录是否存在于我的进度中……")
        response=viewSchedule(para=listPara)
        responseDict = json.loads(response.text)
        listDict= responseDict['response']['module']['rows']
        #定义一个空列表
        newList=[]
        #重新组装待检查列表
        for item in listDict:
            newList.append(item['information'])
        #调用检查列表参数
        if findDictInDictlist(checkPara, newList) is True:
            Log.LogOutput(LogLevel.DEBUG, "检测线索成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "检测线索失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '检测失败')
            return False

'''  
    @功能： 设置线索状态为公开
    @para: 
    para：请调用XinXiGuanLiPara中的XianSuoGongKai
    @return: 设置成功，则返回True；否则返回False  
''' 
def set_clue_state_open(para):
    Log.LogOutput(LogLevel.INFO, "设置线索状态公开开始")
    response = xiansuoyunwei_post(url='/informationManage/unShield', postdata=para)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "设置线索状态公开成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "设置线索状态公开失败")
    return response

'''  
    @功能： 设置线索状态为不公开
    @para: 
    para：请调用XinXiGuanLiPara中的XianSuoGongKai
    @return: 设置成功，则返回True；否则返回False  
'''
def set_clue_state_to_close(para):
    Log.LogOutput(LogLevel.INFO, "设置线索状态不公开开始")
    response = xiansuoyunwei_post(url='/informationManage/shield', postdata=para)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "设置线索状态不公开成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "设置线索状态不公开失败")
    return response

'''  
    @功能： 爆料设置为精彩推荐
    @para: 
    shuoshuoId：设置为精彩推荐的ID
    @return: 如果转成功，则返回True；否则返回False  
''' 

def set_clue_to_highlight(clueId):
    Log.LogOutput(LogLevel.DEBUG, "开始设置爆料为精彩推荐...")
    setDict = {'ids':clueId,
               'showState':1}
    response = xiansuoyunwei_post(url='/clueManage/clueInformationManage/findClueInformationPageBySearchsInfoVo.action', param=setDict)
    if response.result is True:
        Log.LogOutput(LogLevel.DEBUG, "设置爆料为精彩推荐成功")
        return True
    else:
        Log.LogOutput(LogLevel.WARN, "设置爆料为精彩推荐失败")     
        return False
    
# 根据手机号进行搜索
def XinXiSouSuo(para):
    Log.LogOutput(LogLevel.INFO, "根据手机号进行搜索开始")
    response = xiansuoyunwei_post(url='/informationManage/findInformationList', postdata=para)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "根据手机号进行搜索成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "根据手机号进行搜索失败")
    return response

# 根据分类名称进行搜索
def SouSuoCYDH(para):
    Log.LogOutput(LogLevel.INFO, "根据分类名称进行搜索开始")
    response = xiansuoyunwei_post(url='/companyCategoryManage/findCompanyCategoryList', postdata=para)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "根据分类名称进行搜索成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "根据分类名称进行搜索失败")
    return response


# 新增默认爆料分享状态
def addBanLiYiJianZT(para):
    Log.LogOutput(LogLevel.INFO, "新增默认爆料分享状态不公开开始")
    response = xiansuoyunwei_post(url='/personalizedConfiguration/addPersonalizedConfiguration', postdata=para)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "新增默认爆料分享状态不公开成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "新增默认爆料分享状态不公开失败")
    return response

# 新增办理意见分享状态
def addYiJianZT(para):
    Log.LogOutput(LogLevel.INFO, "新增办理意见分享状态不公开开始")
    response = xiansuoyunwei_post(url='/personalizedConfiguration/addPersonalizedConfiguration', postdata=para)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "新增办理意见分享状态不公开成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "新增办理意见分享状态不公开失败")
    return response

# 查看办理意见分享状态
def chakanYiJianZT(companyDict,departmentNo=None):
    try:
        Log.LogOutput(LogLevel.INFO, "查看办理意见分享状态开始")
        compDict = copy.deepcopy(XinXiGuanLiPara.chakanYiJianZT)
        compDict['personalizedConfiguration.departmentNo']= clueOrgInit['DftQuOrgDepNo']
        response = xiansuoyunwei_post(url='/personalizedConfiguration/findPersonalizedConfigurationList', postdata=compDict)
        responseDict = json.loads(response.text)
        listDict= responseDict['rows']
        if CommonUtil.findDictInDictlist(companyDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "查看办理意见分享状态成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查看办理意见分享状态失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查看失败')
            return False  

# 修改办理意见分享状态
def updateYiJianZT(para):
    Log.LogOutput(LogLevel.INFO, "修改办理意见分享状态公开开始")
    response = xiansuoyunwei_post(url='/personalizedConfiguration/updatePersonalizedConfiguration', postdata=para)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "修改办理意见分享状态公开成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "修改办理意见分享状态公开失败")
    return response

# 新增电话管理
def addDianHuaGL(para):
    Log.LogOutput(LogLevel.INFO, "新增电话管理开始")
    response = xiansuoyunwei_post(url='/companyPhoneManage/addCompanyPhone', postdata=para)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "新增电话管理成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "新增电话管理失败")
    return response

# 查看电话管理
def chakanDianHuaGL(companyDict,departmentNo=None,Id=None):
    try:
        Log.LogOutput(LogLevel.INFO, "查看电话管理开始")
        compDict = copy.deepcopy(XinXiGuanLiPara.chakanDianHuaGL)
        compDict['companyPhone.departmentNo']= clueOrgInit['DftQuOrgDepNo']
        compDict['companyPhone.companyCategoryId']=Id
        response = xiansuoyunwei_post(url='/companyPhoneManage/findCompanyPhoneList', postdata=compDict)
        responseDict = json.loads(response.text)
        listDict= responseDict['rows']
        if CommonUtil.findDictInDictlist(companyDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "查看电话管理成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查看电话管理失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查看失败')
            return False  

# 修改电话管理
def updateDianHuaGL(para):
    Log.LogOutput(LogLevel.INFO, "修改电话管理开始")
    response = xiansuoyunwei_post(url='/companyPhoneManage/updateCompanyPhone', postdata=para)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "修改电话管理成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "修改电话管理失败")
    return response

# 新增电话分类
def addDianHuaFL(para):
    Log.LogOutput(LogLevel.INFO, "新增电话分类开始")
    response = xiansuoyunwei_post(url='/companyCategoryManage/addCompanyCategory', postdata=para)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "新增电话分类成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "新增电话分类失败")
    return response

# 导入电话
def addDianHuaDR(para,files=None):
    Log.LogOutput(LogLevel.INFO, "导入电话开始")
    response = xiansuoyunwei_post(url='/common/dataImport/importToDomain', postdata=para)
#     print  response.content
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "导入电话成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "导入电话失败")
    return response

# 修改电话分类
def updateDianHuaFL(para):
    Log.LogOutput(LogLevel.INFO, "修改电话分类开始")
    response = xiansuoyunwei_post(url='/companyCategoryManage/updateCompanyCategory', postdata=para)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "修改电话分类成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "修改电话分类失败")
    return response

# 查看电话分类
def chakanDianHuaFL(companyDict,departmentNo=None):
    try:
        Log.LogOutput(LogLevel.INFO, "查看电话分类开始")
        compDict = copy.deepcopy(XinXiGuanLiPara.chakanDianHuaFL)
        compDict['companyCategory.departmentNo']= clueOrgInit['DftQuOrgDepNo']
        response = xiansuoyunwei_post(url='/companyCategoryManage/findCompanyCategoryList', postdata=compDict)
        responseDict = json.loads(response.text)
        listDict= responseDict['rows']
        if CommonUtil.findDictInDictlist(companyDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "查看电话分类成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查看电话分类失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查看失败')
            return False  

# 查看默认爆料分享状态
def chakanBanLiYiJianZT(companyDict,departmentNo=None):
    try:
        Log.LogOutput(LogLevel.INFO, "查看默认爆料分享状态开始")
        compDict = copy.deepcopy(XinXiGuanLiPara.chakanBanLiYiJianZT)
        compDict['personalizedConfiguration.departmentNo']= clueOrgInit['DftQuOrgDepNo']
        response = xiansuoyunwei_post(url='/personalizedConfiguration/findPersonalizedConfigurationList', postdata=compDict)
#         print response.text
        responseDict = json.loads(response.text)
        listDict= responseDict['rows']
        if CommonUtil.findDictInDictlist(companyDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "查看默认爆料分享状态成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查看默认爆料分享状态失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查看失败')
            return False  


# 修改默认爆料分享状态
def XiuGaiBanLiYiJianZT(para):
    Log.LogOutput(LogLevel.INFO, "修改默认爆料分享状态公开开始")
    response = xiansuoyunwei_post(url='/personalizedConfiguration/updatePersonalizedConfiguration', postdata=para)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "修改默认爆料分享状态公开成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "修改默认爆料分享状态公开失败")
    return response
        
def deleteyunwei():
    try:
        #清空所有删除线索        
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
                
        #清空所有说说     
        Log.LogOutput(message='正在清空所有说说...')
        listPara = copy.deepcopy(XinXiGuanLiPara.getShuoShuoListPara)
        response = xiansuoyunwei_post(url='/casualTalkManage/findCasualTalkList', postdata=listPara)
        responseDict = json.loads(response.text)
        if responseDict['records'] == 0:
            Log.LogOutput(LogLevel.DEBUG, '说说列表数据为空')
        else:
            #删除字典
#             deleteDict = copy.deepcopy(XinXiGuanLiPara.deleteShuoShuoPara)
            deleteDict={
                        'ids[]':'',
                        'deleteReason':'其他'
                        }
            for row in responseDict['rows']:
                deleteDict['ids[]'] = row['id']
#                 deleteDict['mobile'] = row['mobile']
#                 print deleteDict
                delete_shuoshuo(deleteDict)
        # 删除默认分享状态       
        Log.LogOutput(message='正在清空默认分享状态...')
        listPara = copy.deepcopy(XinXiGuanLiPara.chakanYiJianZT)
        response = xiansuoyunwei_post(url='/personalizedConfiguration/findPersonalizedConfigurationList', postdata=listPara)
        responseDict = json.loads(response.text)
        if responseDict['records'] == 0:
            Log.LogOutput(LogLevel.DEBUG, '列表数据为空')
        else:
            #存储所有ID
            arr=[]
            for dictListItem in responseDict['rows']:
                arr.append(dictListItem['id'])
            deleteDict = {'ids[]':tuple(arr)}
            response=xiansuoyunwei_post(url='/personalizedConfiguration/deletePersonalizedConfigurations',postdata=deleteDict)
            if response.result is True:
                Log.LogOutput(LogLevel.INFO, '*删除成功*')
            else:
                Log.LogOutput(LogLevel.ERROR, '删除失败!')    

        shareDefaultDict = copy.deepcopy(XiTongPeiZhiPara.addPersonalConfigPara) 
        shareDefaultDict['personalizedConfiguration.configurationType']=8 #默认分享状态
        shareDefaultDict['personalizedConfiguration.configurationValue']=1 #置为公开
        XiTongPeiZhiIntf.add_personal_config(shareDefaultDict)
# 删除常用电话分类        
        Log.LogOutput(message='正在清空所有删除常用电话分类...')
        listPara = copy.deepcopy(XinXiGuanLiPara.chakanDianHuaFL)
        response = xiansuoyunwei_post(url='/companyCategoryManage/findCompanyCategoryList', postdata=listPara)
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
            response=xiansuoyunwei_post(url='/companyCategoryManage/deleteCompanyCategorys',postdata=deleteDict)
            if response.result is True:
                Log.LogOutput(LogLevel.INFO, '*删除成功*')
            else:
                Log.LogOutput(LogLevel.ERROR, '删除失败!')                           
                
    except Exception :
        Log.LogOutput(LogLevel.ERROR, '删除异常')
        return False   
        
'''  
    @功能： 删除线索
    @para: deleteSingleCluePara：搜索结果查询，请调用XinXiGuanLiPara中的deleteSingleCluePara
    @return: 如果删除成功，则返回True；否则返回False  
''' 
def deletexiansuo(deleteSingleCluePara):  
    Log.LogOutput(LogLevel.INFO, "删除线索开始")
    response = xiansuoyunwei_post(url='/informationManage/deleteInformation', postdata=deleteSingleCluePara)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除线索成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, "删除线索失败")    
        return False         

#删除说说
'''  
    @功能： 删除说说
    @para: deleteShuoShuoPara：搜索结果查询，请调用XinXiGuanLiPara中的deleteShuoShuoPara
    @return: 如果删除成功，则返回True；否则返回False  
'''      
def delete_shuoshuo(deleteShuoShuoPara): 
    Log.LogOutput(LogLevel.INFO, "删除说说开始")
    response = xiansuoyunwei_post(url='/casualTalkManage/updateCasualTalkDelState', postdata=deleteShuoShuoPara)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除线索成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, "删除线索失败")    
        return False
        
# 删除默认爆料分享状态
def deleteBanLiYiJianZT(BanLiYiJianZTDict):  
        Log.LogOutput(LogLevel.INFO, "删除默认爆料分享状态开始")
        response = xiansuoyunwei_post(url='/personalizedConfiguration/deletePersonalizedConfigurations', postdata=BanLiYiJianZTDict)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "删除默认爆料分享状态成功")
        else:
            Log.LogOutput(LogLevel.ERROR, "删除默认爆料分享状态失败")    
            return response                 

# 删除办理意见分享状态
def deleteYiJianZT(BanLiYiJianZTDict):  
        Log.LogOutput(LogLevel.INFO, "删除办理意见分享状态开始")
        response = xiansuoyunwei_post(url='/personalizedConfiguration/deletePersonalizedConfigurations', postdata=BanLiYiJianZTDict)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "删除办理意见分享状态成功")
        else:
            Log.LogOutput(LogLevel.ERROR, "删除办理意见分享状态失败")    
            return response      
        
# 删除常用电话分类
def deleteDianHuaFL(DianHuaFLDict):  
        Log.LogOutput(LogLevel.INFO, "删除常用电话分类开始")
        response = xiansuoyunwei_post(url='/companyCategoryManage/deleteCompanyCategorys', postdata=DianHuaFLDict)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "删除常用电话分类成功")
        else:
            Log.LogOutput(LogLevel.ERROR, "删除常用电话分类失败")    
            return response                     

# 删除常用电话管理
def deleteDianHuaGL(DianHuaFLDict):  
        Log.LogOutput(LogLevel.INFO, "删除常用电话管理开始")
        response = xiansuoyunwei_post(url='/companyPhoneManage/deleteCompanyPhones', postdata=DianHuaFLDict)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "删除常用电话管理成功")
        else:
            Log.LogOutput(LogLevel.ERROR, "删除常用电话管理失败")    
            return response        
        
#获取个性化配置列表
'''
    @功能：获取个性化列表信息
    @para:PersonalConfigListPara
    @return:    true/false
    @author:  chenhui 2016-10-24
'''  
def getPersonalConfigList(para):
    Log.LogOutput(level=LogLevel.INFO, message='获取个性化配置列表信息')
    response = xiansuoyunwei_post(url='/personalizedConfiguration/findPersonalizedConfigurationList', postdata=para)
    if response.result is True:
        Log.LogOutput(message='获取列表信息成功')
    else:
        Log.LogOutput(level=LogLevel.ERROR, message='获取列表失败')
    return response

#删除个性化配置列表
'''
    @功能：删除个性化配置列表
    @para:
    @return:    response
    @author:  chenhui 2016-10-24
'''  
def initPersonalConfigList():
    listPara=copy.deepcopy(PersonalConfigListPara)
    Log.LogOutput(level=LogLevel.INFO, message='获取个性化配置列表信息')
    response = xiansuoyunwei_post(url='/personalizedConfiguration/findPersonalizedConfigurationList', postdata=listPara)
#     print response.text
    responseDict=json.loads(response.text)
    if responseDict['records']==0:
        Log.LogOutput(message='列表数据为空，无需删除')
        Log.LogOutput(level=LogLevel.INFO, message='删除个性化配置列表信息')
    else:
        ids=json.loads(response.text)['rows']
        #定义元组，用于存储待删除id
        idParaList=[]
        for item in ids:
            idParaList.append(item['id'])
        #将列表转为元组
        delPara={
              'ids[]':(idParaList)
                 }
#         print delPara
        response = xiansuoyunwei_post(url='/personalizedConfiguration/deletePersonalizedConfigurations', postdata=delPara)
#         print response.text
        if response.result is True:
            Log.LogOutput(message='删除个性化配置信息成功')
        else:
            Log.LogOutput(level=LogLevel.ERROR, message='删除个性化配置信息失败')
    return response  

'''  
    @功能： 在爆料管理中检查当前地区主题列表
    @para: 
    getThemeListDict:获取主题列表的字典，请调用XinXiGuanLiPara中的getThemeListInClueManagePara
    themeCheckDict：待检查的线索，请调用XinXiGuanLiPara中的checkThemeInClueManagePara字典
    @return: 如果检查成功，则返回True；否则返回False  
'''  
def check_theme_in_clue_manage(themeCheckDict,getThemeListDict=None):
    try:
        Log.LogOutput(LogLevel.INFO, "在爆料管理主题主题查询中检查主题")
        if getThemeListDict is None:
            getThemeListDict = copy.deepcopy(XinXiGuanLiPara.getThemeListInClueManagePara)
        response = xiansuoyunwei_post(url='/themeManage/findThemeContentListByDepartmentNo', postdata=getThemeListDict)
        responseDict = json.loads(response.text)
        if responseDict['records']==0:
            Log.LogOutput(LogLevel.DEBUG, "主题列表为空")
            return False
        #调用检查列表参数
        if findDictInDictlist(themeCheckDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "在主题列表查看到对应主题")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "无法在主题列表查看到对应主题")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '检查过程中异常')
            return False
        
'''  
    @功能： 在用户反馈中查找意见反馈
    @para: 
    getUserFeedback:获取反馈意见字典，请调用XinXiGuanLiPara中的
    checkUserFeedback:待检查的意见信息，请调用XinXiGuanLiPara中的checkUserFeedbackPara
    @return: 如果检查成功，则返回True；否则返回False  
'''  
def check_user_feedback(checkUserFeedback,getUserAdvice):
    try:
        Log.LogOutput(LogLevel.INFO, "在用户反馈列表查看反馈信息...")
        response = xiansuoyunwei_post(url='/userFeedBackManage/findUserFeedBackList', postdata=getUserAdvice)
        responseDict = json.loads(response.text)
        if responseDict['records']==0:
            Log.LogOutput(LogLevel.DEBUG, "用户反馈列表为空")
            return False
        #调用检查列表参数
        for item in responseDict['rows']:
            if findDictInDictlist(checkUserFeedback, [item['userFeedBack']]) is True:
                Log.LogOutput(LogLevel.DEBUG, "在用户反馈列表查看反馈信息成功")
                return True
        Log.LogOutput(LogLevel.WARN, "无法在用户反馈列表查看到对应反馈信息")
        return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '检查过程中异常')
        return False
    
'''  
    @功能： 在用户反馈中通过意见反馈内容获取id
    @para: 
    userFeedbackContent:意见反馈的内容
    @return: 如果查找内容成功，则返回id；否则返回None  
'''  
def get_user_feedback_id_by_content(userFeedbackContent):
    try:
        Log.LogOutput(LogLevel.INFO, "在用户反馈列表中通过反馈内容获取id信息...")
        getUserAdvice = {
                         "rows":"100",
                        "page":"1",
                        "sidx":"id",
                        "sord":"desc"
                         }
        response = xiansuoyunwei_post(url='/userFeedBackManage/findUserFeedBackList', postdata=getUserAdvice)
        responseDict = json.loads(response.text)
        if responseDict['records']==0:
            Log.LogOutput(LogLevel.DEBUG, "用户反馈列表为空")
            return None
        #调用检查列表参数
        for item in responseDict['rows']:
            if item['userFeedBack']['advice'] == userFeedbackContent:
                Log.LogOutput(LogLevel.DEBUG, "在用户反馈列表查看到反馈信息,返回id")
                return item['userFeedBack']['id']
        Log.LogOutput(LogLevel.WARN, "无法在用户反馈列表查看到对应反馈信息")
        return None
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '检查过程中异常')
        return None
    
'''  
    @功能： 针对特定用户反馈回复
    @para: 
    replyForFeedbackPara:意见反馈回复字典，请调用XinXiGuanLiPara中的replyForFeedbackPara
    @return: 回复成功，则返回True；否则返回False 
'''  
def reply_for_user_feedback(replyForFeedbackPara):
    Log.LogOutput(LogLevel.INFO, "开始回复用户反馈意见...")
    response = xiansuoyunwei_post(url='/userFeedBackManage/updateReplyContents', postdata=replyForFeedbackPara)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.DEBUG, "反馈成功")
        return True
    else:
        Log.LogOutput(LogLevel.WARN, "反馈失败")
        return True
    
'''  
    @功能： 修改意见反馈回复信息
    @para: 
    updateReplyContentPara:修改意见反馈回复内容字典，请调用XinXiGuanLiPara中的replyForFeedbackPara
    @return: 修改回复成功，则返回True；否则返回False 
'''  
def update_feedback_reply_content(updateReplyContentPara):
    Log.LogOutput(LogLevel.INFO, "开始修改用户反馈回复内容...")
    response = xiansuoyunwei_post(url='/userFeedBackManage/updateReplyContents', postdata=updateReplyContentPara)
    if response.result is True:
        Log.LogOutput(LogLevel.DEBUG, "修改用户反馈回复内容成功")
        return True
    else:
        Log.LogOutput(LogLevel.WARN, "修改用户反馈回复内容失败")
        return True

'''  
    @功能： 在信息举报列表检查举报
    @para: 
    getInformationReportPara:获取信息举报字典，请调用XinXiGuanLiPara中的getInformationReportListPara
    checkInformationReportPara:待检查的举报信息，请调用XinXiGuanLiPara中的checkInformationReportPara
    @return: 如果检查成功，则返回True；否则返回False  
'''  
def check_information_report_in_list(getInformationReportPara,checkInformationReportPara):
    try:
        Log.LogOutput(LogLevel.INFO, "在信息举报列表查看举报信息...")
        response = xiansuoyunwei_post(url='/informationReportManage/findInformationReportList', postdata=getInformationReportPara)
#         print response.text
        responseDict = json.loads(response.text)
        if responseDict['records']==0:
            Log.LogOutput(LogLevel.DEBUG, "举报列表为空")
            return False
        #调用检查列表参数
        if findDictInDictlist(checkInformationReportPara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "在信息举报列表查看举报信息成功")
            return True
        Log.LogOutput(LogLevel.WARN, "无法在信息举报列表查看到对应举报信息")
        return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '举报信息检查过程中异常')
        return False   

'''  
    @功能： 根据信息内容获取举报次数
    @para: inforPara={
                    'contentText':'',
                    'inforType':'',#InfoType.CLUE爆料，InfoType.SHUOSHUO说说
                    'state':''#0未处理，1已处理
                }
    @return: 异常返回-2，没找到返回-1 正常返回次数
    @author: chenhui 2017-1-3 
'''  
def get_report_count_by_content(inforPara):
    Log.LogOutput(LogLevel.INFO, "开始根据信息内容获取举报次数...")
    getInfoReportDict = copy.deepcopy(XinXiGuanLiPara.getInformationReportPara)
    getInfoReportDict['informationReport.infoType'] = inforPara['inforType']
    getInfoReportDict['informationReport.state'] = inforPara['state']#表示未处理
    response = xiansuoyunwei_post(url='/informationReportManage/findInformationReportList', postdata=getInfoReportDict)
    resDict=json.loads(response.text)
    if resDict['records']==0:
        Log.LogOutput(LogLevel.DEBUG, "列表数据为空")
        return -2
    for item in resDict['rows']:
        if item['contentText']==inforPara['contentText']:
            return item['informationReport']['reportCount']
    return -1
        
'''  
    @功能： 删除所有举报信息
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
''' 

def delete_all_information_report(mobile=None):
    try:
        #所有举报id信息
        ids = []
        #获取爆料待处理举报信息
        getClueInfoReportUnhandle = copy.deepcopy(XinXiGuanLiPara.getInformationReportPara)
        getClueInfoReportUnhandle['informationReport.infoType'] = 0 #爆料
        getClueInfoReportUnhandle['informationReport.state'] = 0 #待处理
        response = xiansuoyunwei_post(url='/informationReportManage/findInformationReportList', postdata=getClueInfoReportUnhandle)
#         print response.text
        responseDict = json.loads(response.text)
        if responseDict['records']==0:
            Log.LogOutput(LogLevel.DEBUG, "爆料待处理举报列表为空")
        else:
            for item in responseDict['rows']:
                if mobile is not None and item['informationReport']['publishUserMobile']==mobile:
                    ids.append(item['informationReport']['infoId']) 
            #删除爆料举报信息       
            clueDeleteDict = copy.deepcopy(XinXiGuanLiPara.deleteInfoReportPara)
            clueDeleteDict['ids[]'] = tuple(ids)
            clueDeleteDict['infoType'] = 0 #表示爆料
            response = xiansuoyunwei_post(url='/informationReportManage/deleteInformationReports', postdata=clueDeleteDict)
#             print response.text
            if response.result is True:
                Log.LogOutput(LogLevel.DEBUG, "删除爆料举报列表成功")
            else:
                Log.LogOutput(LogLevel.WARN, "删除爆料举报列表失败")
            
        ids = []
        #获取说说待处理举报信息
        getShuoShuoInfoReportUnhandle = copy.deepcopy(XinXiGuanLiPara.getInformationReportPara)
        getShuoShuoInfoReportUnhandle['informationReport.infoType'] = 5 #说说
        getShuoShuoInfoReportUnhandle['informationReport.state'] = 0 #待处理
        response = xiansuoyunwei_post(url='/informationReportManage/findInformationReportList', postdata=getShuoShuoInfoReportUnhandle)
#         print response.text
        responseDict = json.loads(response.text)
        if responseDict['records']==0:
            Log.LogOutput(LogLevel.DEBUG, "说说待处理举报列表为空")
        else:
            for item in responseDict['rows']:
                if mobile is not None and item['informationReport']['publishUserMobile']==mobile:
                    ids.append(item['informationReport']['infoId'])
                
            shuoshuoDeleteDict = copy.deepcopy(XinXiGuanLiPara.deleteInfoReportPara)
            shuoshuoDeleteDict['ids[]'] = tuple(ids)
            shuoshuoDeleteDict['infoType'] = 5 #表示说说
            response = xiansuoyunwei_post(url='/informationReportManage/deleteInformationReports', postdata=shuoshuoDeleteDict)
#             print response.text
            if response.result is True:
                Log.LogOutput(LogLevel.DEBUG, "删除说说举报列表成功")
            else:
                Log.LogOutput(LogLevel.WARN, "删除说说举报列表失败")        
            return True
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '删除举报信息过程中异常')
        return False
        pass
    
'''  
    @功能： 对举报信息进行解除举报
    @para: 
    shieldInfoReportPara:解除举报字典，请调用XinXiGuanLiPara中的shieldInfoReportPara
    @return: 解除成功，则返回True；否则返回False 
'''  
def shield_information_report(shieldInfoReportPara):
    Log.LogOutput(LogLevel.INFO, "开始举报不公开操作...")
    response = xiansuoyunwei_post(url='/informationReportManage/informationReportShield', postdata=shieldInfoReportPara)
    if response.result is True:
        Log.LogOutput(LogLevel.DEBUG, "举报不公开成功")
        return True
    else:
        Log.LogOutput(LogLevel.WARN, "解除不公开失败")
        return True
    
'''  
    @功能： 通过爆料内容获取举报信息ID
    @para: 
    getInformationReportPara:获取信息举报字典，请调用XinXiGuanLiPara中的getInformationReportListPara
    clueContentText:爆料内容
    @return: 查找成功，则返回ID；否则返回None 
'''  
def get_information_report_id_by_content(clueContentText,getInformationReportPara):
    Log.LogOutput(LogLevel.INFO, "开始获取举报信息ID...")
    response = xiansuoyunwei_post(url='/informationReportManage/findInformationReportList', postdata=getInformationReportPara)
    responseDict = json.loads(response.text)
    if responseDict['records']==0:
        Log.LogOutput(LogLevel.DEBUG, "举报列表为空,返回None")
        return False
    #调用检查列表参数
    for item in responseDict['rows']:
        if item['contentText']==clueContentText:
            Log.LogOutput(LogLevel.DEBUG, "成功找到举报信息ID")
            return item['informationReport']['infoId']
    Log.LogOutput(LogLevel.DEBUG, "无法找到举报信息ID")
    return None

'''  
    @功能： 删除特定的举报信息
    @para: 
    deleteInfoReportPara：删除信息举报字典，请调用XinXiGuanLiPara中的deleteInfoReportPara
    @return: 如果删除成功，则返回True；否则返回False  
''' 

def delete_certain_information_report(deleteInfoReportPara):
    try:
        response = xiansuoyunwei_post(url='/informationReportManage/deleteInformationReports', postdata=deleteInfoReportPara)
        if response.result is True:
            Log.LogOutput(LogLevel.DEBUG, "删除爆料举报列表成功")
            return True
        else:
            Log.LogOutput(LogLevel.WARN, "删除爆料举报列表失败")     
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '删除举报信息过程中异常')
        return False

'''  
    @功能： 解除举报信息
    @para: 
    relieveInfoReportPara：解除信息举报字典，与删除字典公用，请调用XinXiGuanLiPara中的deleteInfoReportPara
    @return: 如果解除成功，则返回True；否则返回False  
''' 

def relieve_information_report(relieveInfoReportPara):
    Log.LogOutput(LogLevel.DEBUG, "开始解除爆料举报信息...")
    response = xiansuoyunwei_post(url='/informationReportManage/deleteInformationReports', postdata=relieveInfoReportPara)
    if response.result is True:
        Log.LogOutput(LogLevel.DEBUG, "解除爆料举报信息成功")
        return True
    else:
        Log.LogOutput(LogLevel.WARN, "解除爆料举报信息失败")     
        return False
    
'''  
    @功能： 爆料转说说操作
    @para: 
    clueInfoReportId：爆料信息举报ID
    @return: 如果转成功，则返回True；否则返回False  
''' 

def convert_information_report_to_shuoshuo(clueInfoReportId):
    Log.LogOutput(LogLevel.DEBUG, "开始爆料举报信息转说说...")
    convertDict = {'infoId':clueInfoReportId}
    response = xiansuoyunwei_post(url='/informationReportManage/clueInformationConvertCasualTalk', postdata=convertDict)
    if response.result is True:
        Log.LogOutput(LogLevel.DEBUG, "爆料举报信息转说说成功")
        return True
    else:
        Log.LogOutput(LogLevel.WARN, "爆料举报信息转说说失败")     
        return False

'''  
    @功能： 在信息删除记录列表检查删除记录
    @para: 
    getDelRecordListPara:获取删除记录字典，请调用XinXiGuanLiPara中的getDelRecordListPara
    checkDelRecordPara:待检查的举报信息，请调用XinXiGuanLiPara中的checkDelRecordPara
    @return: 如果检查成功，则返回True；否则返回False  
'''  
def check_delete_record_in_list(getDelRecordListPara,checkDelRecordPara):
    try:
        Log.LogOutput(LogLevel.INFO, "在删除记录列表查看删除记录信息...")
        response = xiansuoyunwei_post(url='/delInfoRecordManage/findDelInfoRecordList', postdata=getDelRecordListPara)
        responseDict = json.loads(response.text)
        if responseDict['records']==0:
            Log.LogOutput(LogLevel.DEBUG, "删除记录列表为空")
            return False
        #调用检查列表参数
        if findDictInDictlist(checkDelRecordPara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "在信息删除列表查看删除记录成功")
            return True
        Log.LogOutput(LogLevel.WARN, "无法在信息删除列表查看到对应删除记录信息")
        return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '删除记录检查过程中异常')
        return False
    
'''  
    @功能： 在运维平台随便说说中检查说说是否存在
    @para: 
    getShuoShuoListPara: 获取说说列表字典，可以通过手机号、主题搜索，请调用XinXiGuanLiPara中的getShuoShuoListPara
    checkShuoShuoPara：待检查的线索，请调用XinXiGuanLiPara中的jianchaxiansuo字典
    @return: 如果检查成功，则返回True；否则返回False  
            重点强调：因为说说列表为了适配表情，列表数据做过编码，因此测试时需要用英文说说内容和标题
'''
def check_shuoshuo_in_list(checkShuoShuoPara=None,getShuoShuoListPara=None):
    try:
        Log.LogOutput(LogLevel.INFO, "查找说说开始......")
        if getShuoShuoListPara is None:
            getShuoShuoListPara = copy.deepcopy(XinXiGuanLiPara.getShuoShuoListPara)
        response = xiansuoyunwei_post(url='/casualTalkManage/findCasualTalkList', postdata=getShuoShuoListPara)
        responseDict = json.loads(response.text)
        if responseDict['records']==0:
            Log.LogOutput(LogLevel.DEBUG, "说说列表未空，无法找到对应说说")
            return False
        else:
            if findDictInDictlist(checkShuoShuoPara, responseDict['rows']) is True:
                Log.LogOutput(LogLevel.DEBUG, "查找说说成功")
                return True
            else:
                Log.LogOutput(LogLevel.DEBUG, "查找说说失败")
                return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '查找说说异常')
        return False
    
'''  
    @功能： 通过说说内容获取说说ID
    @para: shuoshuoContent：说说内容
    @return: 如果成功，则返回ID；否则返回None  
'''
def get_shuoshuo_id_by_content(shuoshuoContent=None):
    getListDict = copy.deepcopy(XinXiGuanLiPara.getShuoShuoListPara)
    try:
        response = xiansuoyunwei_post(url='/casualTalkManage/findCasualTalkList', postdata=getListDict)
        responseDict = json.loads(response.text)
        if responseDict['records'] == 0:
            Log.LogOutput(LogLevel.WARN, "列表未空，无法找到ID，返回None")
            return None
        for row in responseDict['rows']:
            if row['contentText']==shuoshuoContent:
                Log.LogOutput(LogLevel.WARN, "找到符合条件的说说，返回id")
                return row['id']
        else:
            Log.LogOutput(LogLevel.WARN, "未找到符合条件的说说，返回None")
            return None
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "未找到符合条件的说说，返回None")
        return False
    
'''  
    @功能： 说说设置为精彩推荐
    @para: 
    shuoshuoId：设置为精彩推荐的ID
    @return: 如果转成功，则返回True；否则返回False  
''' 

def set_shuoshuo_to_highlight(shuoshuoId):
    Log.LogOutput(LogLevel.DEBUG, "开始设置说说为精彩推荐...")
    setDict = {'ids':shuoshuoId,
               'showState':1}
    response = xiansuoyunwei_get(url='/casualTalkManage/updateCasualTalkShowStateByIds', param=setDict)
    if response.result is True:
        Log.LogOutput(LogLevel.DEBUG, "设置说说为精彩推荐成功")
        return True
    else:
        Log.LogOutput(LogLevel.WARN, "设置说说为精彩推荐失败")     
        return False
    
'''  
    @功能： 说说置顶
    @para: 
    shuoshuoId：置顶的说说ID
    @return: 如果转成功，则返回True；否则返回False  
''' 

def set_shuoshuo_to_top(shuoshuoId):
    Log.LogOutput(LogLevel.DEBUG, "开始将说说置顶...")
    setDict = {'ids':shuoshuoId,
               'topState':1}
    response = xiansuoyunwei_get(url='/casualTalkManage/updateCasualTalkTopStateByIds', param=setDict)
    if response.result is True:
        Log.LogOutput(LogLevel.DEBUG, "说说置顶成功")
        return True
    else:
        Log.LogOutput(LogLevel.WARN, "说说置顶失败")     
        return False
    
    '''  
    @功能： 在信息评论举报列表检查举报
    @para: 
    getCommentReportPara:获取信息举报字典，请调用XinXiGuanLiPara中的getCommentReportPara
    checkCommentReportPara:待检查的举报信息，请调用XinXiGuanLiPara中的checkCommentReportPara
    @return: 如果检查成功，则返回True；否则返回False  
'''  
def check_comment_report_in_list(getCommentReportPara,checkCommentReportPara):
    try:
        Log.LogOutput(LogLevel.INFO, "在信息举报列表查看举报信息...")
        response = xiansuoyunwei_post(url='/commentReportManage/findCommentReportList', postdata=getCommentReportPara)
        print checkCommentReportPara
        print response.text
        responseDict = json.loads(response.text)
        if responseDict['records']==0:
            Log.LogOutput(LogLevel.DEBUG, "举报列表为空")
            return False
        #调用检查列表参数
        if findDictInDictlist(checkCommentReportPara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "在信息举报列表查看举报信息成功")
            return True
        Log.LogOutput(LogLevel.WARN, "无法在信息举报列表查看到对应举报信息")
        return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '举报信息检查过程中异常')
        return False   
'''  
    @功能： 根据信息评论内容获取举报次数
    @para: commentPara={
                    'contentText':'',
                    'inforType':'',#InfoType.CLUE爆料，InfoType.SHUOSHUO说说
                    'state':''#0未处理，1已处理
                }
    @return: 异常返回-2，没找到返回-1 正常返回次数
    @author: chenhui 2017-1-3 
'''  
def get_report_count_by_comment(commentPara):
    Log.LogOutput(LogLevel.INFO, "开始根据评论内容获取举报次数...")
    getCommentReportDict = copy.deepcopy(XinXiGuanLiPara.getCommentReportPara)
    getCommentReportDict['informationReport.infoType'] = commentPara['inforType']
    getCommentReportDict['informationReport.state'] = commentPara['state']#表示未处理
    response = xiansuoyunwei_post(url='/commentReportManage/findCommentReportList', postdata=getCommentReportDict)
    resDict=json.loads(response.text)
    if resDict['records']==0:
        Log.LogOutput(LogLevel.DEBUG, "列表数据为空")
        return -2
    for item in resDict['rows']:
        if item['contentText']==commentPara['contentText']:
            return item['commentReport']['reportCount']
    return -1
        
'''  
    @功能： 删除所有举报信息
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
''' 

def delete_all_comment_report(mobile=None):
    try:
        #所有举报id信息
        ids = []
        #获取评论举报待处理举报信息
        getCommentReportUnhandle = copy.deepcopy(XinXiGuanLiPara.getCommentReportPara)
        getCommentReportUnhandle['informationReport.infoType'] = 0 #爆料
        getCommentReportUnhandle['informationReport.state'] = 0 #待处理
        response = xiansuoyunwei_post(url='/commentReportManage/findCommentReportList', postdata=getCommentReportUnhandle)
#         print response.text
        responseDict = json.loads(response.text)
        if responseDict['records']==0:
            Log.LogOutput(LogLevel.DEBUG, "爆料评论待处理举报列表为空")
        else:
            for item in responseDict['rows']:
                if mobile is not None and item['commentReport']['publishUserMobile']==mobile:
                    ids.append(item['commentReport']['commentId']) 
            #删除爆料举报信息       
            cluecommentreportDeleteDict = copy.deepcopy(XinXiGuanLiPara.deleteCommentReportPara)
            cluecommentreportDeleteDict['ids[]'] = tuple(ids)
            cluecommentreportDeleteDict['infoType'] = 0 #表示爆料
            response = xiansuoyunwei_post(url='/commentReportManage/deleteCommentReports', postdata=cluecommentreportDeleteDict)
#             print response.text
            if response.result is True:
                Log.LogOutput(LogLevel.DEBUG, "删除爆料举报列表成功")
            else:
                Log.LogOutput(LogLevel.WARN, "删除爆料举报列表失败")
            
        ids = []
        #获取说说待处理举报信息
        getShuoShuoCommentReportUnhandle = copy.deepcopy(XinXiGuanLiPara.getCommentReportPara)
        getShuoShuoCommentReportUnhandle['informationReport.infoType'] = 5 #说说
        getShuoShuoCommentReportUnhandle['informationReport.state'] = 0 #待处理
        response = xiansuoyunwei_post(url='/commentReportManage/findCommentReportList', postdata=getShuoShuoCommentReportUnhandle)
#         print response.text
        responseDict = json.loads(response.text)
        if responseDict['records']==0:
            Log.LogOutput(LogLevel.DEBUG, "说说待处理举报列表为空")
        else:
            for item in responseDict['rows']:
                if mobile is not None and item['commentReport']['publishUserMobile']==mobile:
                    ids.append(item['commentReport']['commentId'])
                
            sscommentreportDeleteDict = copy.deepcopy(XinXiGuanLiPara.deleteCommentReportPara)
            sscommentreportDeleteDict['ids[]'] = tuple(ids)
            sscommentreportDeleteDict['infoType'] = 5 #表示说说
            response = xiansuoyunwei_post(url='/commentReportManage/deleteCommentReports', postdata=sscommentreportDeleteDict)
#             print response.text
            if response.result is True:
                Log.LogOutput(LogLevel.DEBUG, "删除说说举报列表成功")
            else:
                Log.LogOutput(LogLevel.WARN, "删除说说举报列表失败")        
            return True
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '删除举报信息过程中异常')
        return False
        pass
    
'''  
    @功能： 解除评论举报信息
    @para: 
    relieveInfoReportPara：解除信息举报字典，与删除字典公用，请调用XinXiGuanLiPara中的deleteInfoReportPara
    @return: 如果解除成功，则返回True；否则返回False  
''' 

def relieve_comment_report(relieveCommentReportPara):
    Log.LogOutput(LogLevel.DEBUG, "开始解除评论举报信息...")
    response = xiansuoyunwei_post(url='/commentReportManage/deleteCommentReportDates', postdata=relieveCommentReportPara)
    if response.result is True:
        Log.LogOutput(LogLevel.DEBUG, "解除评论举报信息成功")
        return True
    else:
        Log.LogOutput(LogLevel.WARN, "解除评论举报信息失败")     
        return False
        return False
    


    
