# -*- coding:UTF-8 -*-
'''
Created on 2016-5-4

@author: N-286
'''
from __future__ import unicode_literals
from Web_Test.COMMON import Log, CommonUtil
from Web_Test.COMMON.CommonUtil import findDictInDictlist
from Web_Test.CONFIG import Global
from Web_Test.CONFIG.Define import LogLevel
from Web_Test.CONFIG.InitDefaultPara import userInit
from Web_Test.Interface.PingAnJianShe.pingAnJianSheHttpCommon import pinganjianshe_post, \
    pinganjianshe_get
# from requests.packages.urllib3.util import url
import json

'''
    @功能：发送消息
    @return:    response
    @author:  chenhui 2016-5-4
'''   
def sendMessage(para,username=userInit['DftJieDaoUser'],password='11111111'):
    Log.LogOutput( message='发送消息')
    response=pinganjianshe_post(url='/interactive/outboxPlatformMessageManage/sendPlatformMessage.action',postdata=para,username=username,password=password)
    print (response.text)
    if response.result is True:
        Log.LogOutput(message='发送消息成功')
    else:
        Log.LogOutput(message='发送消息失败')
    return response

'''
    @功能：检查是否存在于列表中，包括发件箱、收件箱、草稿箱
    @return:    response
    @author:  chenhui 2016-5-5
'''   
def checkMessageInBox(checkpara,url,username=userInit['DftJieDaoUser'],password='11111111'):
    try:    
        Log.LogOutput( message='检查消息是否位于列表中')
        listpara={
                'page':1,
                'rows':100,
                'sidx':'id',
                'sord':'desc'
                  }
        response = pinganjianshe_get(url=url,param=listpara,username=username,password=password)
#         print response.text
        #对于字典checkpara的每一项进行匹配，若有一项找不到，则返回错误，若都找到，则返回true
        for key in checkpara:
            if CommonUtil.regMatchString(response.text,checkpara[key]) is False:
                Log.LogOutput(LogLevel.DEBUG, "数据不存在")
                return False
        Log.LogOutput(LogLevel.DEBUG, "数据存在")
        return True
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False
        
'''
    @功能：删除消息
    @return:    response
    @author:  chenhui 2016-5-5
'''   
def delMessage(para,url,username=userInit['DftJieDaoUser'],password='11111111'):
    Log.LogOutput( message='删除消息')
    response=pinganjianshe_post(url=url,postdata=para,username=username,password=password)
#     print response.text
    if response.result is True:
        Log.LogOutput(message='删除消息成功')
    else:
        Log.LogOutput(message='删除消息失败')
    return response

'''
    @功能：新建我的群组
    @return:    response
    @author:  chenhui 2016-5-5
'''   
def addMyGroup(para,username=userInit['DftJieDaoUser'],password='11111111'):
    Log.LogOutput( message='新增我的群组')
    response=pinganjianshe_post(url='/contact/myGroupManage/addMyGroup.action',postdata=para,username=username,password=password)
#     print response.text
    if response.result is True:
        Log.LogOutput(message='新增我的群组成功')
    else:
        Log.LogOutput(message='新增我的群组失败')
    return response  

'''
    @功能：编辑我的联系人
    @return:    response
    @author:  chenhui 2016-5-5
'''   
def updateMyContacter(para,username=userInit['DftJieDaoUser'],password='11111111'):
    Log.LogOutput( message='新增我的联系人')
    response=pinganjianshe_post(url='/contact/myGroupManage/updateMyGroupHasContacter.action',postdata=para,username=username,password=password)
#     print response.text
    if response.result is True:
        Log.LogOutput(message='新增我的联系人成功')
    else:
        Log.LogOutput(message='新增我的联系人失败')
    return response

'''
    @功能：转发消息
    @return:    response
    @author:  chenhui 2016-5-5
'''   
def fordwardMessage(para,username=userInit['DftJieDaoUser'],password='11111111'):
    Log.LogOutput( message='转发消息')
    response=pinganjianshe_post(url='/interactive/outboxPlatformMessageManage/forwardOutboxPlatformMessage.action',postdata=para,username=username,password=password)
#     print response.text
    if response.result is True:
        Log.LogOutput(message='转发消息成功')
    else:
        Log.LogOutput(message='转发消息失败')
    return response

'''
    @功能：再次编辑发送
    @return:    response
    @author:  chenhui 2016-5-5
'''   
def sendMessageAgain(para,username=userInit['DftJieDaoUser'],password='11111111'):
    Log.LogOutput( message='再次编辑发送')
    response=pinganjianshe_post(url='/interactive/outboxPlatformMessageManage/updatePlatformMesssgeReceiverNamesById.action',postdata=para,username=username,password=password)
#     print response.text
    if response.result is True:
        Log.LogOutput(message='再次编辑发送成功')
    else:
        Log.LogOutput(message='再次编辑发送失败')
    return response

'''
    @功能：保存到草稿箱
    @return:    response
    @author:  chenhui 2016-5-6
'''   
def addDraftBox(para,username=userInit['DftJieDaoUser'],password='11111111'):
    infoString='保存到草稿箱'
    Log.LogOutput( message=infoString)
    response=pinganjianshe_post(url='/interactive/outboxPlatformMessageManage/addDraftBox.action',postdata=para,username=username,password=password)
#     print response.text
    if response.result is True:
        Log.LogOutput(message=infoString+'成功')
    else:
        Log.LogOutput(message=infoString+'失败')
    return response

'''
    @功能：收件箱回复信息
    @return:    response
    @author:  chenhui 2016-5-6
'''   
def replyMessage(para,username=userInit['DftJieDaoUser'],password='11111111'):
    infoString='回复信息'
    Log.LogOutput( message=infoString)
    response=pinganjianshe_post(url='/interactive/inboxPlatformMessageManage/replyPlatformMessage.action',postdata=para,username=username,password=password)
#     print response.text
    if response.result is True:
        Log.LogOutput(message=infoString+'成功')
    else:
        Log.LogOutput(message=infoString+'失败')
    return response

'''
    @功能：一键阅读功能
    @return:    response
    @author:  chenhui 2016-5-6
'''   
def oneKeyRead(username=userInit['DftJieDaoUser'],password='11111111'):
    infoString='一键阅读'
    Log.LogOutput( message=infoString)
    response=pinganjianshe_get(url='/interactive/inboxPlatformMessageManage/oneKeyReadPlatformMessage.action',username=username,password=password)
#     print response.text
    if response.result is True:
        Log.LogOutput(message=infoString+'成功')
    else:
        Log.LogOutput(message=infoString+'失败')
    return response

'''
    @功能：搜索、查询
    @return:    response
    @author:  chenhui 2016-5-6
'''   
def searchOutBoxMessage(checkpara,searchpara,username=userInit['DftJieDaoUser'],password='11111111'):
    try:    
        Log.LogOutput( message='检查消息是否位于列表中')
        response = pinganjianshe_get(url='/interactive/searchPlatformMessage/searchOutboxPlatformMessage.action',param=searchpara,username=username,password=password)
#         print response.text
        #对于字典checkpara的每一项进行匹配，若有一项找不到，则返回错误，若都找到，则返回true
        for key in checkpara:
            if CommonUtil.regMatchString(response.text,checkpara[key]) is False:
                Log.LogOutput(LogLevel.DEBUG, "数据不存在")
                return False
        else:
            Log.LogOutput(LogLevel.DEBUG, "数据存在")
            return True
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '验证过程出现异常')
            return False
        
'''
    @功能： 新增互动交流-其他联系人信息
    @para:    HuDongJiaoLiuPara. addOtherContactPara
    @return:     response
    @author:  chenhui 2017-1-12
'''
def add_other_contact(addOtherContactPara,username=Global.PingAnJianSheUser, password=Global.PingAnJianShePass):
    info='新增互动交流-其他联系人信息'
    Log.LogOutput(LogLevel.INFO, info+'开始')
    response = pinganjianshe_post(url='/contact/myContacterManage/addMyContacter.action', postdata=addOtherContactPara,username=username,password=password)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
        Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 获取互动交流-其他联系人列表信息
    @para    getOtherContactListPara:    HuDongJiaoLiuPara. getOtherContactListPara
    @return:     response
    @author:  chenhui 2017-1-12
'''
def get_other_contact_list(getOtherContactListPara):
    info='获取互动交流-其他联系人列表信息'
    Log.LogOutput(LogLevel.INFO, info+'开始')
    response = pinganjianshe_post(url='/contact/myContacterManage/findMyContacters.action', postdata=getOtherContactListPara)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
        Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 检查互动交流-其他联系人列表
    @para:    listpara:    HuDongJiaoLiuPara. getOtherContactListPara
                    checkpara: HuDongJiaoLiuPara. checkOtherContactPara
    @return:    检查成功返回True，失败返回False
    @author:  chenhui 2017-1-12
'''
def check_other_contact_list(getOtherContactListPara,checkOtherContactPara):
    info='检查互动交流-其他联系人列表'
    Log.LogOutput(LogLevel.INFO, info+'开始')
    try:
        response = pinganjianshe_post(url='/contact/myContacterManage/findMyContacters.action', postdata=getOtherContactListPara)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkOtherContactPara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, info+"成功!")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, info+'出现异常')
        return False