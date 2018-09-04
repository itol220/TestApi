# -*- coding:UTF-8 -*-
'''
Created on 2015-11-4

@author: N-254
'''
from __future__ import unicode_literals
from Web_Test.Interface.PingAnJianShe.pingAnJianSheHttpCommon import pinganjianshe_post,\
    pinganjianshe_get
import json
from Web_Test.Interface.PingAnJianShe.HuzhouXunJian import HuZhouXunJianPara
from Web_Test.COMMON import Log, CommonUtil
from Web_Test.CONFIG.Define import LogLevel
import copy
from Web_Test.CONFIG import Global, InitDefaultPara

#平安检查--基础信息--新增
def addsafetyCheckBasics(issueDict, username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "进入到新增基础信息....")
    try:    
        response = pinganjianshe_post(url='/baseinfo/safetyCheckBasicsControllerManage/maintainSafetyCheckBasics.action', postdata=issueDict , username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "新增基础信息成功")
            return True
        else:
                Log.LogOutput(LogLevel.ERROR, "新增基础信息失败")
                return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '新增基础信息过程中失败')
        return False     



#列表查找
def check_huzhouxunjian(companyDict,  username = None, password = None):
    try: 
        Log.LogOutput(LogLevel.DEBUG, "进入到查找基础信息....")
        getListDict = copy.deepcopy(HuZhouXunJianPara.GetHuZhouXunJianListPara)
        getListDict['orgId']= InitDefaultPara.orgInit['DftJieDaoOrgId']
        #getListDict['orgId']=5
        response = pinganjianshe_get(url='/baseinfo/safetyCheckBasicsControllerManage/safetyCheckBasicsList.action',param=getListDict, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取的数据集合
        listDict = responseDict['rows']
        #获取要查询的参数
        #对比查询出来的数据和要查询的是否一样
        if CommonUtil.findDictInDictlist(companyDict,listDict) is True:
            Log.LogOutput(message = '查找到企业信息')
            return True
        else:
            Log.LogOutput(message = "没查找到企业信息")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '查找基础信息过程中失败')
        return False  
    

#删除
def deleteById_huZhouXunJian(issueDict , username = None ,password = None):
    Log.LogOutput(LogLevel.DEBUG, "进入到删除基础信息....")
    response = pinganjianshe_get(url='/baseinfo/safetyCheckBasicsControllerManage/deleteSafetyCheckBasics.action',param=issueDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除基础信息成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, "删除基础信息失败")
        return False
    
  
#查找列表所有id并删除
def deleteAllSearchByIds_huZhouXunJian():
    Log.LogOutput(LogLevel.DEBUG, "进入到查找基础信息....")
    try:
        getListDict = copy.deepcopy(HuZhouXunJianPara.GetHuZhouXunJianListPara)
        getListDict['orgId']= InitDefaultPara.orgInit['DftJieDaoOrgId']
        response = pinganjianshe_get(url='/baseinfo/safetyCheckBasicsControllerManage/safetyCheckBasicsList.action',param=getListDict, username=InitDefaultPara.userInit['DftShiUser'], password=Global.PingAnJianShePass)
        responseDict = json.loads(response.text)
        #获取的数据集合
        record = responseDict['records']
        if record == 0 :
            Log.LogOutput(level=LogLevel.DEBUG, message='基础信息列表无数据')
        else:
            for dictListItem in responseDict['rows']:
                deleteDict = {'ids':dictListItem['id']}
                deleteById_huZhouXunJian(deleteDict,username=InitDefaultPara.userInit['DftShiUser'], password=Global.PingAnJianShePass)
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '查找基础信息过程中失败')
        return False     


#搜索检查
def search_check():
    Log.LogOutput(LogLevel.DEBUG, "进入到查找基础信息....")
    try:    
        getListDict = copy.deepcopy(HuZhouXunJianPara.GetHuZhouXunJianListPara)
        getListDict['orgId']= InitDefaultPara.orgInit['DftJieDaoOrgId']
        response = pinganjianshe_get(url='/baseinfo/safetyCheckBasicsControllerManage/safetyCheckBasicsList.action',param=getListDict, username=Global.PingAnJianSheUser, password=Global.PingAnJianShePass)
        responseDict = json.loads(response.text)
        #获取的数据集合
        record = responseDict['records']
        if record == 0 :
            Log.LogOutput(level=LogLevel.DEBUG, message='基础信息列表无数据')
            return True
        else:
            Log.LogOutput(level=LogLevel.DEBUG, message='基础信息存在数据') 
            return False 
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '基础信息数据搜索过程中失败')
        return False     
 
  
#修改
def edit_huZhouXunJian(issueDict, username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "进入到修改基础信息....")
    response = pinganjianshe_post(url='/baseinfo/safetyCheckBasicsControllerManage/maintainSafetyCheckBasics.action', postdata=issueDict , username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "修改基础信息成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, "修改基础信息失败")
        return False

#高级搜索 期望中的[ps:输入列表中存在的数据进行查询]
def findByCompany(issueDict, username = None, password = None):
        Log.LogOutput(LogLevel.DEBUG, "进入到基础信息高级搜索（期望中的）开始....")
        getListDict = copy.deepcopy(HuZhouXunJianPara.HuZhouXunJian_search)
        getListDict['orgId']= InitDefaultPara.orgInit['DftJieDaoOrgId']
        getListDict['safetyCheckBasics.companyName']= issueDict['safetyCheckBasics.companyName']
        getListDict['safetyCheckBasics.companyAddr']= issueDict['safetyCheckBasics.companyAddr']
        getListDict['safetyCheckBasics.companyType.id']= issueDict['safetyCheckBasics.companyType.id']
        getListDict['safetyCheckBasics.orgNo']= issueDict['safetyCheckBasics.orgNo']

        response = pinganjianshe_get(url='/baseinfo/safetyCheckBasicsControllerManage/safetyCheckBasicsList.action',param=getListDict, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取的数据集合
        record = responseDict['records']
        if record == 0 :
            Log.LogOutput(level=LogLevel.DEBUG, message='基础信息数据搜索失败')
            return False 
        else:
                Log.LogOutput(level=LogLevel.DEBUG, message='基础信息数据搜索成功') 
                return True
            
#搜索 期望中的[ps:输入列表中不存在的数据进行查询]
def findByCompanyByMatch(issueDict, company,username = None, password = None):
        Log.LogOutput(LogLevel.DEBUG, "进入到基础信息高级搜索（不期望中的）开始....")
        getListDict = copy.deepcopy(HuZhouXunJianPara.HuZhouXunJian_search)
        getListDict['orgId']= InitDefaultPara.orgInit['DftJieDaoOrgId']
        getListDict['safetyCheckBasics.companyName']= issueDict['safetyCheckBasics.companyName']
        getListDict['safetyCheckBasics.companyAddr']= issueDict['safetyCheckBasics.companyAddr']
        getListDict['safetyCheckBasics.companyType.id']= issueDict['safetyCheckBasics.companyType.id']
        getListDict['safetyCheckBasics.orgNo']= issueDict['safetyCheckBasics.orgNo']
        getListDictCheck = copy.deepcopy(HuZhouXunJianPara.HuZhouXunJian_check) 
        getListDictCheck['companyName']= company

        response = pinganjianshe_get(url='/baseinfo/safetyCheckBasicsControllerManage/safetyCheckBasicsList.action',param=getListDict, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取的数据集合
        listDict = responseDict['rows']
        record = responseDict['records']
        if record == 0 :
            Log.LogOutput(level=LogLevel.DEBUG, message='基础信息数据搜索失败')
            return False 
        else:
                if CommonUtil.findDictInDictlist(getListDictCheck,listDict) is True:
                    Log.LogOutput(message = '存在的匹配成功')
                    return True
                else:
                    Log.LogOutput(message = "不存在的数据匹配失败")
                return False
                Log.LogOutput(level=LogLevel.DEBUG, message='基础信息数据搜索成功') 
                return True

#合并单位
def unionCompany(issueDict, username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "进入到合并单位开始....")
    response = pinganjianshe_get(url='/baseinfo/safetyCheckBasicsControllerManage/mergeSafetyCheckBasics.action',param=issueDict, username=username, password=password) 
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "合并单位成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, "合并单位失败")
        return False
    

#导出
def exportData(param,username = None,password = None):
    Log.LogOutput(LogLevel.DEBUG, "进入到导出数据开始....")
    param = copy.deepcopy(HuZhouXunJianPara.GetHuZhouXunJianListPara)
    param['orgId']=InitDefaultPara.orgInit['DftJieDaoOrgId']
    response = pinganjianshe_post(url='/baseinfo/safetyCheckBasicsControllerManage/downloadList.action',postdata=param, username=username, password=password) 
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "导出数据成功")
        return True
    else:
        Log.LogOutput(LogLevel.INFO, "导出数据失败")
        return False

#新增模板
def addModel(param,username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "进入到新增模板开始....")
    try:
        Log.LogOutput(LogLevel.DEBUG, "新增模板开始....")
        response = pinganjianshe_post(url='/plugin/safetyCheckModuleManage/addSafetyCheckModule.action',postdata=param, username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "新增模板成功")
            return True
        else:
            Log.LogOutput(LogLevel.INFO, "新增模板失败")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '新增模板过程中失败')
        return False 
    
#新增模板检查点
def checkAddModel(param,username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "进入到新增模板检查点开始....")
    try:
        getListDict = copy.deepcopy(HuZhouXunJianPara.getListModelParam)
        getListDict['safetyCheckModule.org.id']=InitDefaultPara.orgInit['DftShengOrgId']
        response = pinganjianshe_post(url='/plugin/safetyCheckModuleManage/findSafetyCheckModulePageInfo.action',postdata=getListDict, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取的数据集合
        listDict = responseDict['rows']
        #获取要查询的参数
        #对比查询出来的数据和要查询的是否一样
        if CommonUtil.findDictInDictlist(param,listDict) is True:
            Log.LogOutput(message = '模板名称在列表中存在')
            return True
        else:
            Log.LogOutput(message = "模板名称在列表中不存在")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '模板信息搜索过程中失败')
        return False         
    
#新增一级,二级,三级分类
def addClass(level,param,username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "进入到新增一级，二级，三级分类开始....")
    try:        
            response = pinganjianshe_post(url='/plugin/safetyCheckModuleDetailManage/addSafetyCheckModuleDetail.action',postdata=param, username=username, password=password) 
            if response.result is True:
                if level=='1':            
                    Log.LogOutput(LogLevel.INFO, "新增一级分类成功")
                elif level=='2':                
                    Log.LogOutput(LogLevel.INFO, "新增二级分类成功")
                elif level=='3':   
                    Log.LogOutput(LogLevel.INFO, "新增三级分类成功")
                return True             
            else:
                if level=='1':
                    Log.LogOutput(LogLevel.INFO, "新增的一级分类失败")
                elif level=='2':
                    Log.LogOutput(LogLevel.INFO, "新增的二级分类失败")
                elif level=='3':
                    Log.LogOutput(LogLevel.INFO, "新增的三级分类失败")
                return False 
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '新增一级，二级，三级过程中失败')
        return False                 
    
#新增一级，二级，细则分类检查点    
def checkFirstClass(level,moduleId,param,username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "进入到查找一级，二级，三级分类开始....")
    try:    
        getListDict = copy.deepcopy(HuZhouXunJianPara.modelFirstListParam)
        getListDict['safetyCheckModuleDetail.moduleId'] = moduleId
        response = pinganjianshe_post(url='/plugin/safetyCheckModuleDetailManage/findSafetyCheckModuleDetailPageInfo.action',postdata=getListDict, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取的数据集合
        listDict = responseDict['rows']
        #获取要查询的参数
        #对比查询出来的数据和要查询的是否一样
        if CommonUtil.findDictInDictlist(param,listDict) is True:
            if level=='1':
                Log.LogOutput(LogLevel.INFO, "新增的一级分类在列表中存在")
            elif level=='2':
                Log.LogOutput(LogLevel.INFO, "新增的二级分类在列表中存在")
            elif level=='3':
                Log.LogOutput(LogLevel.INFO, "新增的三级分类在列表中存在")
            return True
        else:
            if level=='1':
                Log.LogOutput(LogLevel.INFO, "新增的一级分类在列表中不存在")
            elif level=='2':
                Log.LogOutput(LogLevel.INFO, "新增的二级分类在列表中不存在")
            elif level=='3':
                Log.LogOutput(LogLevel.INFO, "新增的三级分类在列表中不存在")
            return False  
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '新增一级，二级，三级检查点过程中失败')
        return False    


    
#启用模板
def isUseModel(param,username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "进入到启用模板开始....")
    getListDict = copy.deepcopy(HuZhouXunJianPara.getListModelParam)
    getListDict['safetyCheckModule.org.id']=InitDefaultPara.orgInit['DftShengOrgId']
    checkIsUse = copy.deepcopy(HuZhouXunJianPara.checkIsUseMode)
    checkIsUse['isUse']= True
    response = pinganjianshe_post(url='/plugin/safetyCheckModuleManage/findSafetyCheckModulePageInfo.action',postdata=getListDict, username=username, password=password)
    responseDict = json.loads(response.text)
    #获取的数据集合
    listDict = responseDict['rows']
    #获取要查询的参数
    #对比查询出来的数据和要查询的是否一样
    if CommonUtil.findDictInDictlist(checkIsUse,listDict) is True:
        Log.LogOutput(message = '已有启用的模板,不能启用其他模板')
        return False
    else:
        response = pinganjianshe_get(url='/plugin/safetyCheckModuleManage/updateSafetyCheckModule.action',param=param, username=username, password=password)
        Log.LogOutput(message = '启用的模板成功')
        return True
    
    


# 启用模板检查点
def checkIsUseMode(param,username = None, password = None):
    try:
        Log.LogOutput(LogLevel.DEBUG, "进入到查找启用模板开始....")
        getListDict = copy.deepcopy(HuZhouXunJianPara.getListModelParam)
        getListDict['safetyCheckModule.org.id']=InitDefaultPara.orgInit['DftShengOrgId']
        response = pinganjianshe_post(url='/plugin/safetyCheckModuleManage/findSafetyCheckModulePageInfo.action',postdata=getListDict, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取的数据集合
        listDict = responseDict['rows']
        #获取要查询的参数
        #对比查询出来的数据和要查询的是否一样
        if CommonUtil.findDictInDictlist(param,listDict) is True:
            Log.LogOutput(message = '启用的模板在列表中存在')
            return True
        else:
            Log.LogOutput(message = "启用的模板在列表中不存在")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '启用模板过程中失败')
        return False        
         

#停用模板
def isNotUseModel(param,username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "进入到停用模板开始....")
    getListDict = copy.deepcopy(HuZhouXunJianPara.getListModelParam)
    getListDict['safetyCheckModule.org.id']=InitDefaultPara.orgInit['DftShiOrgId']
    response = pinganjianshe_get(url='/plugin/safetyCheckModuleManage/updateSafetyCheckModule.action',param=param, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "停用模板成功")
    else:
        Log.LogOutput(LogLevel.INFO, "停用模板失败")
    return response
    
# 停用模板检查点
def checkIsNotUseMode(param,username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "进入到列表中查找停用模板开始....")
    try:
        getListDict = copy.deepcopy(HuZhouXunJianPara.getListModelParam)
        getListDict['safetyCheckModule.org.id']=InitDefaultPara.orgInit['DftShengOrgId']
        response = pinganjianshe_post(url='/plugin/safetyCheckModuleManage/findSafetyCheckModulePageInfo.action',postdata=getListDict, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取的数据集合
        listDict = responseDict['rows']
        #获取要查询的参数
        #对比查询出来的数据和要查询的是否一样
        if CommonUtil.findDictInDictlist(param,listDict) is True:
            Log.LogOutput(message = '停用的模板在列表中存在')
            return True
        else:
            Log.LogOutput(message = "停用的模板在列表中不存在")
            return False 
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '列表中查找停用模板过程中失败')
        return False         

#项目细则/分类
def projectClass(param,username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "进入到新增年度细则/分类页面....")
    response = pinganjianshe_get(url='/plugin/safetyCheckModuleDetailManage/findSafetyCheckModuleDetailPageInfo.action',param=param, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "进入到新增年度细则/分类页面")
        return True
    else:
        Log.LogOutput(LogLevel.INFO, "没有进入到新增年度细则/分类页面")
        return False


#修改模板
def updateModel(param,username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "进入到修改模板中....")
    response = pinganjianshe_post(url='/plugin/safetyCheckModuleManage/updateSafetyCheckModule.action',postdata=param, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "修改模板成功")
        return True
    else:
        Log.LogOutput(LogLevel.INFO, "修改模板失败")
        return False
    
#修改模板检查点
def checkUpdateModel(param,username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "进入到在列表中查找修改模板中....")
    try:
            getListDict = copy.deepcopy(HuZhouXunJianPara.getListModelParam)
            getListDict['safetyCheckModule.org.id']=InitDefaultPara.orgInit['DftShengOrgId']
            response = pinganjianshe_post(url='/plugin/safetyCheckModuleManage/findSafetyCheckModulePageInfo.action',postdata=getListDict, username=username, password=password)
            responseDict = json.loads(response.text)
            #获取的数据集合
            listDict = responseDict['rows']
            #获取要查询的参数
            #对比查询出来的数据和要查询的是否一样
            if CommonUtil.findDictInDictlist(param,listDict) is True:
                Log.LogOutput(message = '修改的模板名称在列表中存在')
                return True
            else:
                Log.LogOutput(message = "修改的模板名称在列表中不存在")
                return False  
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '列表中查找停用模板过程中失败')
        return False        
    
#一级,二级,三级分类修改
def editFirstClass(level,param,username = None,password = None):  
    Log.LogOutput(LogLevel.DEBUG, "进入一级,二级,三级分类修改中....")
    response = pinganjianshe_post(url='/plugin/safetyCheckModuleDetailManage/updateSafetyCheckModuleDetail.action',postdata=param, username=username, password=password) 
    if response.result is True:
        if level=='1':
            Log.LogOutput(LogLevel.INFO, "修改一级分类成功")
        elif level=='2':
            Log.LogOutput(LogLevel.INFO, "修改二级分类成功")
        elif level=='3':
            Log.LogOutput(LogLevel.INFO, "修改三级分类成功")
        return True
        
    else:
        if level=='1':
            Log.LogOutput(LogLevel.INFO, "修改一级分类失败")
        elif level=='2':
            Log.LogOutput(LogLevel.INFO, "修改二级分类失败")
        elif level=='3':
            Log.LogOutput(LogLevel.INFO, "修改三级分类失败")
        return False
        
    
#分类修改检查点
def checkEditClass(level,moduleId,param,username=None,password=None):
    Log.LogOutput(LogLevel.DEBUG, "进入一级,二级,三级分类修改检查点中....")
    try:
            getListDict = copy.deepcopy(HuZhouXunJianPara.modelFirstListParam)
            getListDict['safetyCheckModuleDetail.moduleId'] = moduleId
            response = pinganjianshe_post(url='/plugin/safetyCheckModuleDetailManage/findSafetyCheckModuleDetailPageInfo.action',postdata=getListDict, username=username, password=password)
            responseDict = json.loads(response.text)
            #获取的数据集合
            listDict = responseDict['rows']
            #获取要查询的参数
            #对比查询出来的数据和要查询的是否一样
            if CommonUtil.findDictInDictlist(param,listDict) is True:
                if level=='1':
                    Log.LogOutput(LogLevel.INFO, "修改的一级分类在列表中存在")
                elif level=='2':
                    Log.LogOutput(LogLevel.INFO, "修改的二级分类在列表中存在")
                elif level=='3':
                    Log.LogOutput(LogLevel.INFO, "修改的三级分类在列表中存在")
                return True
            else:
                if level=='1':
                    Log.LogOutput(LogLevel.INFO, "修改的一级分类在列表中存在")
                elif level=='2':
                    Log.LogOutput(LogLevel.INFO, "修改的二级分类在列表中存在")
                elif level=='3':
                    Log.LogOutput(LogLevel.INFO, "修改的三级分类在列表中存在")
                return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '列表中查找一级,二级,三级分类失败')
        return False                    
                        
#单位检查    
def checkUnit(param,username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "进入单位检查页面中....")
    response = pinganjianshe_get(url='/plugin/safetyCheckInspectionManage/dispatch.action',param=param, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "进入到新增检查单位页面")
        return True
    else:
        Log.LogOutput(LogLevel.INFO, "没有进入到新增检查单位页面")
        return False
   
def checkCompany(param,username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "开始新增单位检查....")
    try:
        response = pinganjianshe_get(url='/plugin/safetyCheckInspectionManage/addSafetyCheckInspection.action',param=param, username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "新增单位检查成功")
            return True
        else:
            Log.LogOutput(LogLevel.INFO, "新增单位检查失败")
            return False   
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '新增单位检查过程中异常')
        return False          
   
#修改单位检查
def updateUnit(param,username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "进入修改检查单位中....")  
    response = pinganjianshe_get(url='/plugin/safetyCheckInspectionManage/updateSafetyCheckInspection.action',param=param, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "修改检查单位成功")
        return True
    else:
        Log.LogOutput(LogLevel.INFO, "修改检查单位失败")
        return False    
   
   
   
#单位检查检查点
def checkUnitCompany(param,username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "检查单位检查信息....") 
    try:
        getListDict = copy.deepcopy(HuZhouXunJianPara.check_unitParam)
        getListDict['safetyCheckInspectionVo.org.id']=InitDefaultPara.orgInit['DftShiOrgId']
        response = pinganjianshe_get(url='/plugin/safetyCheckInspectionManage/findSafetyCheckInspectionPageInfo.action',param=getListDict, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取的数据集合
        listDict = responseDict['rows'][0]["safetyCheckBasics"]["companyName"]
        #获取要查询的参数
        #对比查询出来的数据和要查询的是否一样
        if CommonUtil.regMatchString(param,listDict) is True:
            Log.LogOutput(message = '检查单位列表中存在')
            return True
        else:
            Log.LogOutput(message = "检查单位列表中不存在")
            return False  
    except Exception as e:
        Log.LogOutput(LogLevel.ERROR, '进入列表查找修改单位中过程中失败')
        Log.LogOutput(LogLevel.ERROR, e)
        return False             
    
#专项检查--高级搜索 期望中的[ps:输入列表中存在的数据进行查询]
def searchCheckCompany(issueDict, username = None, password = None):
        Log.LogOutput(LogLevel.DEBUG, "进入专项检查--高级搜索(期望中)....") 
        getListDict = copy.deepcopy(HuZhouXunJianPara.searchCompanyUnit)
        getListDict['safetyCheckInspectionVo.org.id']= InitDefaultPara.orgInit['DftJieDaoOrgId']
        getListDict['safetyCheckInspectionVo.safetyCheckBasics.companyName']= issueDict['safetyCheckInspectionVo.safetyCheckBasics.companyName']
        getListDict['safetyCheckInspectionVo.riskLevel.id']=issueDict['safetyCheckInspectionVo.riskLevel.id']
        getListDict['safetyCheckInspectionVo.checkType.id']=issueDict['safetyCheckInspectionVo.checkType.id']
        response = pinganjianshe_get(url='/plugin/safetyCheckInspectionManage/findSafetyCheckInspectionPageInfo.action',param=getListDict, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取的数据集合
        record = responseDict['records']
        if record == 0 :
            Log.LogOutput(level=LogLevel.DEBUG, message='信息数据搜索失败')
            return False 
        else:
                Log.LogOutput(level=LogLevel.DEBUG, message='信息数据搜索成功') 
                return True
            
#搜索 期望中的[ps:输入列表中不存在的数据进行查询]
def searchCompanyByMatch(issueDict, company,username = None, password = None):
        Log.LogOutput(LogLevel.DEBUG, "进入专项检查--高级搜索(不期望中)....") 
        getListDict = copy.deepcopy(HuZhouXunJianPara.searchCompanyUnit)
        getListDict['safetyCheckInspectionVo.org.id']= InitDefaultPara.orgInit['DftJieDaoOrgId']
        getListDict['safetyCheckInspectionVo.safetyCheckBasics.companyName']= issueDict['safetyCheckInspectionVo.safetyCheckBasics.companyName']
        getListDict['safetyCheckInspectionVo.riskLevel.id']=issueDict['safetyCheckInspectionVo.riskLevel.id']
        getListDict['safetyCheckInspectionVo.checkType.id']=issueDict['safetyCheckInspectionVo.checkType.id']
         
        response = pinganjianshe_get(url='/plugin/safetyCheckInspectionManage/findSafetyCheckInspectionPageInfo.action',param=getListDict, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取的数据集合
        listDict = responseDict['rows']
        record = responseDict['records']
        
        if record == 0 :
            Log.LogOutput(level=LogLevel.DEBUG, message='基础信息数据搜索失败')
            return False 
        else:
                if CommonUtil.findDictInDictlist(getListDict,listDict) is True:
                    Log.LogOutput(message = '存在的匹配成功')
                    return True
                else:
                    Log.LogOutput(message = "不存在的数据匹配失败")
                return False
                Log.LogOutput(level=LogLevel.DEBUG, message='基础信息数据搜索成功') 
                return True   
     

#删除模板
def deleteById_moudle(issueDict , username = None ,password = None):
        Log.LogOutput(LogLevel.DEBUG, "进入删除模板中....") 
        response = pinganjianshe_get(url='/plugin/safetyCheckModuleManage/deleteSafetyCheckModule.action',param=issueDict, username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "删除模板信息成功")
            return True
        else:
            Log.LogOutput(LogLevel.ERROR, "删除模板信息失败")
            return False
  
#查找列表所有id并删除(模板)
def deleteAllSearchByIds_moudle():
    Log.LogOutput(LogLevel.DEBUG, "进入列表查找删除模板中....") 
    try:
        getListDict = copy.deepcopy(HuZhouXunJianPara.getListModelParam)
        getListDict['safetyCheckModule.org.id']= InitDefaultPara.orgInit['DftShengOrgId']
        response = pinganjianshe_get(url='/plugin/safetyCheckModuleManage/findSafetyCheckModulePageInfo.action',param=getListDict, username=InitDefaultPara.userInit['DftShengUser'], password=Global.PingAnJianShePass)
        responseDict = json.loads(response.text)
        
        #获取的数据集合
        record = responseDict['records']
        if record == 0 :
            Log.LogOutput(level=LogLevel.DEBUG, message='模板列表无数据')
            return True
        else:
            for dictListItem in responseDict['rows']:
                deleteDict = {'safetyCheckModule.id':dictListItem['id']}
                deleteById_moudle(deleteDict,username=InitDefaultPara.userInit['DftShiUser'], password=Global.PingAnJianShePass)
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '进入列表查找删除模板过程中失败')
        return False     

#搜索检查（模板）
def searchMouble_check():
    Log.LogOutput(LogLevel.DEBUG, "进入搜索检查（模板）....")
    try:    
        getListDict = copy.deepcopy(HuZhouXunJianPara.getListModelParam)
        getListDict['safetyCheckModule.org.id']= InitDefaultPara.orgInit['DftShiOrgId']
        response = pinganjianshe_get(url='/plugin/safetyCheckModuleManage/findSafetyCheckModulePageInfo.action',param=getListDict, username=Global.PingAnJianSheUser, password=Global.PingAnJianShePass)
        responseDict = json.loads(response.text)
        #获取的数据集合
        record = responseDict['records']
        if record == 0 :
            Log.LogOutput(level=LogLevel.DEBUG, message='模板列表无数据2')
            return True
        else:
            Log.LogOutput(level=LogLevel.DEBUG, message='模板列表存在数据') 
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '进入搜索检查（模板）过程中失败')
        return False     

 

#删除专项检查
def deleteById_check(issueDict , username = None ,password = None):
    Log.LogOutput(LogLevel.DEBUG, "进入删除专项检查....") 
    response = pinganjianshe_get(url='/plugin/safetyCheckInspectionManage/deleteSafetyCheckInspection.action',param=issueDict, username=username, password=password)
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除专项检查信息成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, "删除专项检查信息失败")
        return False
  
#查找列表所有id并删除(专项检查)
def deleteAllSearchByIds_check():
    Log.LogOutput(LogLevel.DEBUG, "进入查找列表所有id并删除(专项检查)....")
    try:
        getListDict = copy.deepcopy(HuZhouXunJianPara.getListModelParam)
        getListDict['safetyCheckInspectionVo.org.id']= InitDefaultPara.orgInit['DftJieDaoOrgId']
        response = pinganjianshe_get(url='/plugin/safetyCheckInspectionManage/findSafetyCheckInspectionPageInfo.action',param=getListDict, username=Global.PingAnJianSheUser, password=Global.PingAnJianShePass)
        responseDict = json.loads(response.text)
        #获取的数据集合
        record = responseDict['records']
        if record == 0 :
            Log.LogOutput(level=LogLevel.DEBUG, message='专项检查列表无数据')
        else:
            for dictListItem in responseDict['rows']:
                deleteDict = {'ids':dictListItem['id']}
                deleteById_check(deleteDict,username=Global.PingAnJianSheUser, password=Global.PingAnJianShePass)
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '进入查找列表所有id并删除(专项检查)过程中失败')
        return False     

#搜索检查（模板）
def searchCheck():
    Log.LogOutput(LogLevel.DEBUG, "进入搜索检查（模板)....")
    try:    
        getListDict = copy.deepcopy(HuZhouXunJianPara.getListModelParam)
        getListDict['safetyCheckModule.org.id']= InitDefaultPara.orgInit['DftShiOrgId']
        response = pinganjianshe_get(url='/plugin/safetyCheckInspectionManage/findSafetyCheckInspectionPageInfo.action',param=getListDict, username=InitDefaultPara.userInit['DftShiUser'], password=Global.PingAnJianShePass)
        responseDict = json.loads(response.text)
        #获取的数据集合
        record = responseDict['records']
        if record == 0 :
            Log.LogOutput(level=LogLevel.DEBUG, message='专项检查列表不存在数据')
        else:
            Log.LogOutput(level=LogLevel.DEBUG, message='专项检查列表存在数据') 
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '专项检查列表数据搜索g过程中失败')
        return False   
      
#基础信息导出
def exportDataCompany(param, username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "进入基础信息导出中....")
    response = pinganjianshe_get(url='/baseinfo/safetyCheckBasicsControllerManage/downloadList.action',param=param, username=username, password=password)
    return response
    
#基础信息导入    
def importDataCompany(param, files=None,username = None, password = None):
    Log.LogOutput(LogLevel.DEBUG, "进入基础信息导入中....")
    response = pinganjianshe_post(url='/dataTransfer/importToDomain.action',postdata=param, files=files,username=username, password=password)
    return response





    