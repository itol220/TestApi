# -*- coding:UTF-8 -*-
'''
Created on 2015-11-5

@author: N-254
'''
from __future__ import unicode_literals
from Web_Test.COMMON import CommonUtil, Log, Time
from Web_Test.CONFIG.Define import LogLevel
from Web_Test.Interface.PingAnJianShe.pingAnJianSheHttpCommon import pinganjianshe_post
from Web_Test.Interface.PingAnTong.pingAnTongHttpCommon import pingantong_post
import copy
import json
from Web_Test.Interface.PingAnTong.DanWeiChangSuo import MbDanWeiChangSuoPara


'''
    @功能：手机安全生产重点新增事件，消防安全生产重点新增,治安重点事件
    @para:Para
    @return:    true/false
    @author:  lhz 2016-2-29
'''  
def aqsczdAdd(param,typeName,username = None,password = None):
    Log.LogOutput(level=LogLevel.INFO, message = typeName+'新增。。。')
    try:    
        response = pingantong_post(url='/mobile/enterpriseManage/addEnterprise.action', postdata=param , username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "组织机构--"+typeName+"新增成功")
            return True
        else:
                Log.LogOutput(LogLevel.ERROR, "组织机构--"+typeName+"新增失败")
                return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "组织机构--"+typeName+"新增过程中失败")
        return False  



#重点场所--学校新增
def schoolAdd(param,username = None,password = None):
    Log.LogOutput(LogLevel.DEBUG, "重点场所--学校新增信息....")
    try:    
        response = pingantong_post( url = '/mobile/schoolManage/addSchool.action', postdata=param , username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "重点场所--学校新增信息成功")
            return True
        else:
                Log.LogOutput(LogLevel.ERROR, "重点场所--学校新增信息失败")
                return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '重点场所--学校新增信息过程中失败')
        return False 


#重点场所--学校修改
def schoolEdit(param,username = None,password = None):
    Log.LogOutput(LogLevel.DEBUG, "重点场所--学校修改信息....")
    try:    
        response = pingantong_post( url = '/mobile/schoolManage/updateSchool.action', postdata=param , username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "重点场所--学校修改信息成功")
            return True
        else:
                Log.LogOutput(LogLevel.ERROR, "重点场所--学校修改信息失败")
                return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '重点场所--学校修改信息过程中失败')
        return False 
    
'''
    @功能：手机安全生产重点,消防安全生产重点，规上企业修改
    @para:Para
    @return:    true/false
    @author:  lhz 2016-3-1
'''  
def aqsczdUpdate(para,typeName, username = None, password = None):
    try:    
        Log.LogOutput(LogLevel.DEBUG, "进入到"+typeName+"....")
        response = pingantong_post( url = '/mobile/enterpriseManage/updateEnterprise.action', postdata=para , username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, typeName+"成功")
            return True
        else:
                Log.LogOutput(LogLevel.ERROR, typeName+"失败")
                return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, typeName+"+过程中失败")
        return False 




'''
    @功能：检查新增的安全生产重点，消防安全生产重点列表是否能查找到
    @para:checkPara:{companyDict,,typeName,keyType，username,password}
    @param 
    @return:    true/false
    @author:  lhz 2016-3-1
'''  
#列表查找
def check_aqsczd(companyDict,typeName,keyType,orgId = None,username = None, password = None):
    try: 
        Log.LogOutput(LogLevel.DEBUG, "进入到查找"+typeName+"....")
        getListDict =  copy.deepcopy(MbDanWeiChangSuoPara.aqsczdListPara)
        getListDict['ownerOrg.id'] =  orgId  
        getListDict['enterpriseSearchCondition.keyType'] = keyType
        response = pingantong_post(url='/mobile/enterpriseManage/searchEnterprise.action',postdata=getListDict, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取要查询的参数
        #对比查询出来的数据和要查询的是否一样
        if CommonUtil.findDictInDictlist(companyDict,responseDict['rows']) is True:
            Log.LogOutput(message = '查找到'+typeName)
            return True
        else:
            Log.LogOutput(message = '没查找到'+typeName)
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '查找'+typeName+'信息过程中失败')
        return False  
    
'''
    @功能：检查新增的安全生产重点，消防安全生产重点是否能查看到
    @para:checkPara:{companyDict,,typeName,keyType，username,password}
    @param 
    @return:    true/false
    @author:  lhz 2016-3-1
'''  
#列表查找
def check_Viewaqsczd(companyDict,typeName,id = None,username = None, password = None):
    try: 
        Log.LogOutput(LogLevel.DEBUG, "进入到查找"+typeName+"....")
        getListDict =  copy.deepcopy(MbDanWeiChangSuoPara.aqsczdViewCheck) 
        getListDict['enterprise.id'] = id
        response = pingantong_post(url='/mobile/enterpriseManage/viewEnterprise.action',postdata=getListDict, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取要查询的参数
        #对比查询出来的数据和要查询的是否一样
        if CommonUtil.findDictInDictlist(companyDict,[responseDict]) is True:
            Log.LogOutput(message = '查找到'+typeName)
            return True
        else:
            Log.LogOutput(message = '没查找到'+typeName)
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '查找'+typeName+'信息过程中失败')
        return False      
    
    
'''
    @功能：检查新增的学校是否存在列表中
    @para:checkPara:{companyDict,username,password}
    @param 
    @return:    true/false
    @author:  lhz 2016-3-1
'''  
#列表查找
def check_school(companyDict,typeName,orgId = None,username = None, password = None):
    try: 
        Log.LogOutput(LogLevel.DEBUG, "进入到查找"+typeName+"....")
        getListDict =  copy.deepcopy(MbDanWeiChangSuoPara.schoolListParam)
        getListDict['orgId'] = orgId
        response = pingantong_post(url='/mobile/schoolManage/searchSchool.action',postdata=getListDict, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取要查询的参数
        #对比查询出来的数据和要查询的是否一样
        if CommonUtil.findDictInDictlist(companyDict,responseDict['rows']) is True:
            Log.LogOutput(message = '查找到'+typeName)
            return True
        else:
            Log.LogOutput(message = '没查找到'+typeName)
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '查找'+typeName+'信息过程中失败')
        return False   
'''
    @功能：检查新增的学校是否存在列表中
    @para:checkPara:{companyDict,username,password}
    @param 
    @return:    true/false
    @author:  lhz 2016-3-1
'''  
#列表查找
def checkViewschool(companyDict,typeName,id = None,username = None, password = None):
    try: 
        Log.LogOutput(LogLevel.DEBUG, "进入到查找"+typeName+"....")
        getListDict =  copy.deepcopy(MbDanWeiChangSuoPara.schoolLookParam)
        getListDict['Id'] = id
        response = pingantong_post(url='/mobile/schoolManage/viewSchool.action',postdata=getListDict, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取要查询的参数
        #对比查询出来的数据和要查询的是否一样
        if CommonUtil.findDictInDictlist(companyDict,[responseDict]) is True:
            Log.LogOutput(message = '查找到'+typeName)
            return True
        else:
            Log.LogOutput(message = '没查找到'+typeName)
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '查找'+typeName+'信息过程中失败')
        return False   
        
    
    
       

#查找消防安全生产重点PC端    
def checkXFAnQuanShengChan(companyDict, orgId=None,keyType = None,username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "查找消防安全生产重点信息开始。。。")
        compDict = copy.deepcopy(MbDanWeiChangSuoPara.ChaKanAnQuanShengChanbject)
        compDict['orgId']= orgId
        compDict['keyType']= keyType
        response = pinganjianshe_post(url = '/baseinfo/fireSafetyEnterpriseManage/fireSafetyEnterpriseList.action', postdata=compDict,username=username, password = password)
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(companyDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "PC端查找消防安全生产重点信息成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "PC端查找消防安全生产重点信息失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查找PC端消防安全生产重点信息过程中失败')
            return False
        
#查找安全生产重点PC端    
def checkAnQuanShengChan(companyDict, orgId=None,keyType = None,username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "查找治安重点信息开始。。。")
        compDict = copy.deepcopy(MbDanWeiChangSuoPara.ChaKanAnQuanShengChanbject)
        compDict['orgId']= orgId
        compDict['keyType']= keyType
        response = pinganjianshe_post(url = '/baseinfo/safetyProductionKeyManage/safetyProductionKeyList.action', postdata=compDict,username=username, password = password)
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(companyDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "PC端查找治安重点信息信息成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "PC端查找治安重点信息失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查找PC端治安重点信息过程中失败')
            return False   
        
#查找规上企业C端    
def checkCompany(companyDict, orgId=None,keyType = None,username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "查找企业--规上企业信息开始。。。")
        compDict = copy.deepcopy(MbDanWeiChangSuoPara.ChaKanAnQuanShengChanbject)
        compDict['orgId']= orgId
        compDict['keyType']= keyType
        response = pinganjianshe_post(url = '/baseinfo/safetyProductionKeyManage/safetyProductionKeyList.action', postdata=compDict,username=username, password = password)
        responseDict = json.loads(response.text)
        if CommonUtil.findDictInDictlist(companyDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "PC端查找企业--规上企业信息成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "PC端查找企业--规上企业信息失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查找PC端查找企业--规上企业信息过程中失败')
            return False               
        
           
#查找学校PC端    
def checkSchool(companyDict, username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "查找学校信息开始。。。。")
        compDict = copy.deepcopy(MbDanWeiChangSuoPara.scoolPClist)
        response = pinganjianshe_post(url='/baseinfo/schoolManage/schoolList.action', postdata=compDict,username=username, password = password)
        responseDict = json.loads(response.text)
        
        if CommonUtil.findDictInDictlist(companyDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "PC端查找学校信息成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "PC端查找学校信息失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查找学校信息失败')
            return False  
        


#重点场所--其他场所新增信息
def OtherCSAdd(param,username = None,password = None):
    Log.LogOutput(LogLevel.DEBUG, "重点场所--其他场所新增信息....")
    try:    
        response = pingantong_post(url = '/mobile/otherLocaleManage/addOtherLocale.action', postdata=param , username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "重点场所--其他场所新增信息成功")
            return True
        else:
                Log.LogOutput(LogLevel.ERROR, "重点场所--其他场所新增信息失败")
                return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '重点场所--其他场所新增信息过程中失败')
        return False 

#重点场所--其他场所修改信息
def OtherCSEdit(param,username = None,password = None):
    Log.LogOutput(LogLevel.DEBUG, "重点场所--其他场所修改信息....")
    try:    
        response = pingantong_post(url = '/mobile/otherLocaleManage/updateOtherLocale.action', postdata=param , username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "重点场所--其他场所修改信息成功")
            return True
        else:
                Log.LogOutput(LogLevel.ERROR, "重点场所--其他场所修改信息失败")
                return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '重点场所--其他场所修改信息过程中失败')
        return False 


#组织机构--社会组织新增信息
def shzzAdd(param,username = None,password = None):
    Log.LogOutput(LogLevel.DEBUG, "组织机构--社会组织新增信息....")
    try:    
        response = pingantong_post(url = '/mobile/newSocietyOrganizationsManage/addNewSocietyOrganizations.action', postdata=param , username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "组织机构--社会组织新增信息成功")
            return True
        else:
                Log.LogOutput(LogLevel.ERROR, "组织机构--社会组织新增信息失败")
                return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '组织机构--社会组织新增信息过程中失败')
        return False 
    
     
#组织机构--社会组织修改信息
def shzzEdit(param,username = None,password = None):
    Log.LogOutput(LogLevel.DEBUG, "组织机构--社会组织修改信息....")
    try:    
        response = pingantong_post(url = '/mobile/newSocietyOrganizationsManage/updateNewSocietyOrganizations.action', postdata=param , username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "组织机构--社会组织修改信息成功")
            return True
        else:
                Log.LogOutput(LogLevel.ERROR, "组织机构--社会组织修改信息失败")
                return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '组织机构--社会组织修改信息过程中失败')
        return False  

       
    
'''
    @功能：检查新增的组织机构--社会组织是否存在列表中
    @para:checkPara:{companyDict,typeName,username,password}
    @param 
    @return:    true/false
    @author:  lhz 2016-3-1
'''  
#列表查找
def check_Organizations(companyDict,typeName,orgId = None,username = None, password = None):
    try: 
        Log.LogOutput(LogLevel.DEBUG, "进入到查找"+typeName+"....")
        getListDict =  copy.deepcopy(MbDanWeiChangSuoPara.organizationsList)
        getListDict['organizationId'] = orgId
        getListDict['searchNewSocietyOrganizationsVo.organization.id'] = orgId
        response = pingantong_post(url='/mobile/newSocietyOrganizationsManage/findNewSocietyOrganizationssByQueryCondition.action',postdata=getListDict, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取要查询的参数
        #对比查询出来的数据和要查询的是否一样
        if CommonUtil.findDictInDictlist(companyDict,responseDict['rows']) is True:
            Log.LogOutput(message = '查找到'+typeName)
            return True
        else:
            Log.LogOutput(message = '没查找到'+typeName)
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '查找'+typeName+'信息过程中失败')
        return False  
'''
    @功能：检查新增的组织机构--社会组织查看
    @para:checkPara:{companyDict,typeName,username,password}
    @param 
    @return:    true/false
    @author:  lhz 2016-3-1
'''  
#列表查找
def checkViewOrganizations(companyDict,typeName,id = None,username = None, password = None):
    try: 
        Log.LogOutput(LogLevel.DEBUG, "进入到查找"+typeName+"....")
        getListDict =  copy.deepcopy(MbDanWeiChangSuoPara.organizationsViewParam)
        getListDict['id'] = id
        response = pingantong_post(url='/mobile/newSocietyOrganizationsManage/viewNewSocietyOrganizations.action',postdata=getListDict, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取的数据集合
        #对比查询出来的数据和要查询的是否一样
        if CommonUtil.findDictInDictlist(companyDict,[responseDict]) is True:
            Log.LogOutput(message = '查找到'+typeName)
            return True
        else:
            Log.LogOutput(message = '没查找到'+typeName)
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '查找'+typeName+'信息过程中失败')
        return False     
    
'''
    @功能：检查新增的组织机构--社会组织是否存在PC列表中
    @para:checkPara:{companyDict,typeName,username,password}
    @param 
    @return:    true/false
    @author:  lhz 2016-3-1
'''  
#列表查找
def checkPcOrganizations(companyDict,typeName,username = None, password = None):
    try: 
        Log.LogOutput(LogLevel.DEBUG, "进入到查找"+typeName+"....")
        getListDict =  copy.deepcopy(MbDanWeiChangSuoPara.organizationsPCList) 
        response = pinganjianshe_post(url='/baseinfo/newSocietyOrganizationsManage/newSocietyOrganizationsList.action',postdata=getListDict, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取要查询的参数
        #对比查询出来的数据和要查询的是否一样
        if CommonUtil.findDictInDictlist(companyDict,responseDict['rows']) is True:
            Log.LogOutput(message = '查找到'+typeName)
            return True
        else:
            Log.LogOutput(message = '没查找到'+typeName)
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '查找'+typeName+'信息过程中失败')
        return False  
        
'''
    @功能：检查新增的其他场所是否存在列表中
    @para:checkPara:{companyDict,username,password}
    @param 
    @return:    true/false
    @author:  lhz 2016-3-1
'''  
#列表查找
def check_other(companyDict,typeName,orgId = None,username = None, password = None):
    try: 
        Log.LogOutput(LogLevel.DEBUG, "进入到查找"+typeName+"....")
        getListDict =  copy.deepcopy(MbDanWeiChangSuoPara.otherParamList) 
        getListDict['organization.id'] = orgId
        response = pingantong_post(url='/mobile/otherLocaleManage/otherLocaleList.action',postdata=getListDict, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取要查询的参数
        #对比查询出来的数据和要查询的是否一样
        if CommonUtil.findDictInDictlist(companyDict,responseDict['rows']) is True:
            Log.LogOutput(message = '查找到'+typeName)
            return True
        else:
            Log.LogOutput(message = '没查找到'+typeName)
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '查找'+typeName+'信息过程中失败')
        return False      
    
'''
    @功能：检查新增的其他场所查看
    @para:checkPara:{companyDict,username,password}
    @param 
    @return:    true/false
    @author:  lhz 2016-3-1
'''  
#列表查找
def checkViewother(companyDict,id=None,username = None, password = None):
    try: 
        Log.LogOutput(LogLevel.DEBUG, "进入到查找重点场所--其他场所修改信息....")
        getListDict =  copy.deepcopy(MbDanWeiChangSuoPara.otherParamView) 
        getListDict['otherLocale.id'] = id
        response = pingantong_post(url='/mobile/otherLocaleManage/viewOtherLocale.action',postdata=getListDict, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取的数据集合
        #获取要查询的参数
        #对比查询出来的数据和要查询的是否一样
        if CommonUtil.findDictInDictlist(companyDict,[responseDict]) is True:
            Log.LogOutput(message = '查找到重点场所--其他场所修改信息')
            return True
        else:
            Log.LogOutput(message = '没查找到重点场所--其他场所修改信息')
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '查找重点场所--其他场所修改信息信息过程中失败')
        return False      
    
    
    
    
#查找其他场所PC端    
def checkOther(companyDict, username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "PC端查找其他场所信息开始。。。")
        compDict = copy.deepcopy(MbDanWeiChangSuoPara.scoolPClist)
        response = pinganjianshe_post(url='/baseinfo/otherLocaleManage/otherLocaleList.action', postdata=compDict,username=username, password = password)
        responseDict = json.loads(response.text)
        
        if CommonUtil.findDictInDictlist(companyDict, responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "PC端查找其他场所信息成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "PC端查找其他场所信息失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查找其他场所信息失败')
            return False      
        

    '''
    @功能：巡场情况新增
    @para:Para
    @return:    true/false
    @author:  lhz 2016-2-29
'''  
def xunChangAdd(param,username = None,password = None):
    Log.LogOutput(LogLevel.DEBUG, "组织机构--成员库新增....")
    try:    
        response = pingantong_post(url = '/mobile/serviceTeam/addServiceRecordHasObjectForMobile.action', postdata=param , username=username, password=password)
        if response.result is True:
            Log.LogOutput(LogLevel.INFO, "组织场所--巡场情况新增信息成功")
            return True
        else:
                Log.LogOutput(LogLevel.ERROR, "组织场所--巡场情况新增信息失败")
                return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '组织场所--巡场情况新增信息过程中失败')
        return False  


#查找巡场情况   
def check_xunChang(companyDict, objectId = None,username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "查找巡场情况信息开始。。。")
        compDict = copy.deepcopy(MbDanWeiChangSuoPara.xunChangListParam)
        compDict['objectIds']=objectId
        response = pingantong_post(url='/mobile/serviceTeam/findServiceRecords.action', postdata=compDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict= responseDict['rows'] 
        if CommonUtil.findDictInDictlist(companyDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "查找巡场情况信息成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查找巡场情况信息失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查找巡场情况信息过程中失败')
            return False 
        
#巡场情况pc列表查找        
def check_xunChangPc(companyDict, objectId = None,username = None, password = None):
    try:
        Log.LogOutput(LogLevel.INFO, "查找巡场情况信息开始。。。")
        compDict = copy.deepcopy(MbDanWeiChangSuoPara.xunChangListParamPc)
        compDict['objectIds']=objectId
        compDict['serviceRecordVo.displayYear'] = Time.getCurrentDate()
        response = pinganjianshe_post(url='/plugin/serviceTeam/serviceRecord/findServiceRecords.action', postdata=compDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict= responseDict['rows'] 
        if CommonUtil.findDictInDictlist(companyDict, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "查找PC端巡场情况信息成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查找PC端巡场情况信息失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查找PC端巡场情况信息过程中失败')
            return False 
            

'''
    @功能：高级搜索（安全生产重点，消防安全重点，治安重点，规上企业）[期望中的]
    @para:checkPara:{companyDict,,typeName,keyType，username,password}
    @param 
    @return:    true/false
    @author:  lhz 2016-3-1
'''  
#列表查找
def searchAqsc(companyDict,username = None, password = None):
    try: 
        Log.LogOutput(LogLevel.DEBUG, "进入到重点场所高级搜索中【期望中】....")
        getListDict =  copy.deepcopy(MbDanWeiChangSuoPara.searchListParam)
        getListDict['enterpriseSearchCondition.name'] = companyDict['enterpriseSearchCondition.name']
        response = pingantong_post(url='/mobile/enterpriseManage/searchEnterprise.action',postdata=getListDict, username=username, password=password)
        responseDict = json.loads(response.text)
        
        #获取的数据集合
        record = responseDict['records']
        if record == 0 :
            Log.LogOutput(level=LogLevel.DEBUG, message='信息数据搜索失败')
            return False 
        else:
                Log.LogOutput(level=LogLevel.DEBUG, message='信息数据搜索成功') 
                return True
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '搜索信息过程中失败')
        return False 
        
        
#搜索 期望中的[ps:输入列表中不存在的数据进行查询]
def searchAqscNot(companyDict,unit,orgId = None,username = None, password = None):
        Log.LogOutput(LogLevel.DEBUG, "进入专项检查--高级搜索(不期望中)....") 
        getListDict =  copy.deepcopy(MbDanWeiChangSuoPara.searchListParam)
        getListDict['enterpriseSearchCondition.name'] = unit
        response = pingantong_post(url='/mobile/enterpriseManage/searchEnterprise.action',postdata=getListDict, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取的数据集合
        record = responseDict['records']
        if record == 0 :
            Log.LogOutput(level=LogLevel.DEBUG, message='基础信息数据搜索失败')
            return False 
        else:
                if CommonUtil.findDictInDictlist(companyDict,responseDict['rows']) is True:
                    Log.LogOutput(message = '存在的匹配成功')
                    return True
                else:
                    Log.LogOutput(message = "不存在的数据匹配失败")
                return False
                Log.LogOutput(level=LogLevel.DEBUG, message='基础信息数据搜索成功') 
                return True   
             
        

'''
    @功能：高级搜索组织机构-社会组织[期望中的]
    @para:checkPara:{companyDict,,typeName,keyType，username,password}
    @param 
    @return:    true/false
    @author:  lhz 2016-3-1
'''  
#列表查找
def searchZzcs(companyDict,username = None, password = None):
    try: 
        Log.LogOutput(LogLevel.DEBUG, "进入到组织机构-社会组织高级搜索中【期望中】....")
        getListDict =  copy.deepcopy(MbDanWeiChangSuoPara.searchZZcsListParam)
        getListDict['searchNewSocietyOrganizationsVo.unitName'] = companyDict['searchNewSocietyOrganizationsVo.unitName']
        response = pingantong_post(url='/mobile/newSocietyOrganizationsManage/findNewSocietyOrganizationssByQueryCondition.action',postdata=getListDict, username=username, password=password)
        responseDict = json.loads(response.text)
        
        #获取的数据集合
        record = responseDict['records']
        if record == 0 :
            Log.LogOutput(level=LogLevel.DEBUG, message='组织机构-社会组织数据搜索失败')
            return False 
        else:
                Log.LogOutput(level=LogLevel.DEBUG, message='组织机构-社会组织信息数据搜索成功') 
                return True
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '搜索信息过程中失败')
        return False 
        
        
#组织机构-社会组织高级搜索 期望中的[ps:输入列表中不存在的数据进行查询]
def searchZzcsNot(companyDict,unit,orgId = None,username = None, password = None):
        Log.LogOutput(LogLevel.DEBUG, "进入组织机构-社会组织高级搜索(不期望中)....") 
        getListDict =  copy.deepcopy(MbDanWeiChangSuoPara.searchZZcsListParam)
        getListDict['searchNewSocietyOrganizationsVo.unitName'] = unit
        response = pingantong_post(url='/mobile/newSocietyOrganizationsManage/findNewSocietyOrganizationssByQueryCondition.action',postdata=getListDict, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取的数据集合
        record = responseDict['records']
        if record == 0 :
            Log.LogOutput(level=LogLevel.DEBUG, message='组织机构-社会组织列表无数据')
            return False 
        else:
                if CommonUtil.findDictInDictlist(companyDict,responseDict['rows']) is True:
                    Log.LogOutput(message = '组织机构-社会组织存在的匹配成功')
                    return True
                else:
                    Log.LogOutput(message = "组织机构-社会组织不存在的数据匹配失败")
                return False
                Log.LogOutput(level=LogLevel.DEBUG, message='组织机构-社会组织数据搜索成功') 
                return True    


'''
    @功能：高级搜索重点场所-其他组织[期望中的]
    @para:checkPara:{companyDict,,typeName,keyType，username,password}
    @param 
    @return:    true/false
    @author:  lhz 2016-3-1
'''  
#列表查找
def searchOther(companyDict,username = None, password = None):
    try: 
        Log.LogOutput(LogLevel.DEBUG, "进入到重点场所-其他组织高级搜索中【期望中】....")
        getListDict =  copy.deepcopy(MbDanWeiChangSuoPara.otherSearchListParam)
        getListDict['searchOtherLocaleVo.name'] = companyDict['searchOtherLocaleVo.name']
        response = pingantong_post(url='/mobile/otherLocaleManage/otherLocaleList.action',postdata=getListDict, username=username, password=password)
        responseDict = json.loads(response.text)
        
        #获取的数据集合
        record = responseDict['records']
        if record == 0 :
            Log.LogOutput(level=LogLevel.DEBUG, message='重点场所-其他组织数据搜索失败')
            return False 
        else:
                Log.LogOutput(level=LogLevel.DEBUG, message='重点场所-其他组织信息数据搜索成功') 
                return True
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '搜索信息过程中失败')
        return False 
        
        
#重点场所-其他组织 不期望中的[ps:输入列表中不存在的数据进行查询]
def searchOtherNot(companyDict,unit,orgId = None,username = None, password = None):
        Log.LogOutput(LogLevel.DEBUG, "进入重点场所-其他组织高级搜索(不期望中)....") 
        getListDict =  copy.deepcopy(MbDanWeiChangSuoPara.otherSearchListParam)
        getListDict['searchOtherLocaleVo.name'] = unit
        response = pingantong_post(url='/mobile/otherLocaleManage/otherLocaleList.action',postdata=getListDict, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取的数据集合
#        listDict = responseDict['rows']
        record = responseDict['records']
        
        if record == 0 :
            Log.LogOutput(level=LogLevel.DEBUG, message='重点场所-其他组织列表无数据')
            return False 
        else:
                if CommonUtil.findDictInDictlist(companyDict,responseDict['rows']) is True:
                    Log.LogOutput(message = '重点场所-其他组织存在的匹配成功')
                    return True
                else:
                    Log.LogOutput(message = "重点场所-其他组织不存在的数据匹配失败")
                return False
                Log.LogOutput(level=LogLevel.DEBUG, message='重点场所-其他组织数据搜索成功') 
                return True    
    
'''
    @功能：高级搜索重点场所-学校[期望中的]
    @para:checkPara:{companyDict,,typeName,keyType，username,password}
    @param 
    @return:    true/false
    @author:  lhz 2016-3-1
'''  
#列表查找
def searchSchool(companyDict,username = None, password = None):
    try: 
        Log.LogOutput(LogLevel.DEBUG, "进入到重点场所-学校高级搜索中【期望中】....")
        getListDict =  copy.deepcopy(MbDanWeiChangSuoPara.schoolSearchListParam)
        getListDict['location.president'] = companyDict['location.president']
        response = pingantong_post(url='/mobile/schoolManage/searchSchool.action',postdata=getListDict, username=username, password=password)
        responseDict = json.loads(response.text)
        
        #获取的数据集合
        record = responseDict['records']
        if record == 0 :
            Log.LogOutput(level=LogLevel.DEBUG, message='重点场所-学校数据搜索失败')
            return False 
        else:
                Log.LogOutput(level=LogLevel.DEBUG, message='重点场所-学校数据搜索成功') 
                return True
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '搜索信息过程中失败')
        return False 
        
        
#重点场所-学校 不期望中的[ps:输入列表中不存在的数据进行查询]
def searchSchoolNot(companyDict,unit,orgId = None,username = None, password = None):
        Log.LogOutput(LogLevel.DEBUG, "进入重点场所-学校高级搜索(不期望中)....") 
        getListDict =  copy.deepcopy(MbDanWeiChangSuoPara.otherSearchListParam)
        getListDict['location.president'] = unit
        response = pingantong_post(url='/mobile/schoolManage/searchSchool.action',postdata=getListDict, username=username, password=password)
        responseDict = json.loads(response.text)
        #获取的数据集合
        record = responseDict['records']
        
        if record == 0 :
            Log.LogOutput(level=LogLevel.DEBUG, message='重点场所-学校列表无数据')
            return False 
        else:
                if CommonUtil.findDictInDictlist(companyDict,responseDict['rows']) is True:
                    Log.LogOutput(message = '重点场所-学校存在的匹配成功')
                    return True
                else:
                    Log.LogOutput(message = "重点场所-学校不存在的数据匹配失败")
                return False
                Log.LogOutput(level=LogLevel.DEBUG, message='重点场所-学校数据搜索成功') 
                return True 

    
