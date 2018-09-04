# -*- coding:UTF-8 -*-
'''
Created on 2015-11-24

@author: N-133
'''
from __future__ import unicode_literals
from COMMON import Log
from COMMON.CommonUtil import findDictInDictlist
from CONFIG.Define import LogLevel
from CONFIG.Global import XianSuoDftPassword
from Interface.PingAnJianShe.pingAnJianSheHttpCommon import pinganjianshe_post
from Interface.XianSuoApp.xianSuoHttpCommon import xiansuo_post, xiansuo_get
from Interface.YunWeiPingTai.yunWeiPingTaiHttpCommon import xiansuoyunwei_post
import copy
import json
import md5

'''
    @功能：修改用户（昵称、密码等）
    @para：
    userUpdatePara：请调用XsGongZuoTaiPara中的userUpdatePara
    @return:    response
    @author:  chenhui 2016-03-24
'''  
def updateUserInfo(userUpdatePara,password=XianSuoDftPassword):
    Log.LogOutput(LogLevel.INFO, "修改用户信息")
    response = xiansuo_post(url='/api/clue/userDubboService/updateUser', postdata=userUpdatePara,password=password)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "修改用户信息成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "修改用户信息失败")
    return response

'''
    @功能：设置消息开关
    @para：
    updateMessageSwitchPara：请调用XsMyInformationPara中的updateMessageSwitchPara
    @return:    更新成功，返回True;否则返回False
    @author:  hongzenghui 2016-12-30
'''  
def set_message_push_switch(updateMessageSwitchPara):
    Log.LogOutput(LogLevel.INFO, "设置消息开关......")
    response = xiansuo_post(url='/api/clue/userDubboService/updateUserMessageSwit', postdata=updateMessageSwitchPara)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "设置消息开关成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "设置消息开关失败")
    return response

'''
    @功能：检查用户信息
    @para：
    userId:用户id信息
    checkUserInfoPara：请调用XsMyInformationPara中的checkUserInfoPara
    @return:检查成功，返回True;检查失败，返回False
    @author:  hongzenghui 2016-12-20
''' 

def check_personal_info(userId,checkUserInfoPara):
    Log.LogOutput(LogLevel.INFO, "开始检查用户个人信息......")
    getUserInfoDict = {
                       "id":userId,
                       "tqmobile":"true"
                       }
    response = xiansuo_get(url='/api/clue/userDubboService/getUserById', param=getUserInfoDict)
    responseDict = json.loads(response.text)
    if findDictInDictlist(checkUserInfoPara, [responseDict['response']['module']]) is True:
        Log.LogOutput(LogLevel.DEBUG, "检查用户个人信息成功")
        return True
    else:
        Log.LogOutput(LogLevel.DEBUG, "检查用户个人信息失败")
        return False


'''
    @功能：将内容转为md5加密后的值
    @return:    md5
    @author:  chenhui 2016-03-25
'''  
def encodeToMd5(value):
    m1 = md5.new()
    m1.update(value)
    return m1.hexdigest()

'''
    @功能：定位签到
    @return:    response
    @author:  chenhui 2016-03-25
'''  
def addUserPosition(para):
    Log.LogOutput(LogLevel.INFO, "定位签到")
    response = xiansuo_post(url='/api/clue/userDubboService/addUserPosition', postdata=para)
    #print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "定位签到成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "定位签到失败")
    return response

'''
    @功能：PC社管线索添加用户认证
    @return:    response
    @author:  chenhui 2016-03-25
'''  
def systemUserCertified(para):
    Log.LogOutput(LogLevel.INFO, "线索用户认证")
    response = pinganjianshe_post(url='/clueManage/clueUserManage/systemUserCertified.action', postdata=para)
    #print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "线索用户认证成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "线索用户认证失败")
    return response

'''
    @功能：PC社管线索取消用户认证
    @return:    response
    @author:  chenhui 2016-03-25
'''  
def delSystemUserCertified(para):
    Log.LogOutput(LogLevel.INFO, "线索取消用户认证")
    response = pinganjianshe_post(url='/clueManage/clueUserManage/systemUnCertified.action', postdata=para)
#    print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "线索取消用户认证成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "线索取消用户认证失败")
    return response

'''
    @功能： 普通用户签到
    @para: {'tqmobile':'true','departmentNo':''}
    @return:   response
    @author:  chenhui 2016-11-30
'''
def userSignIn(para):
    info='普通用户签到'
    Log.LogOutput(message=info)
    response = xiansuo_post(url='/api/clue/userDubboService/userSignIn', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功")
    else:
            Log.LogOutput(LogLevel.ERROR, info+"失败")
    return response  

'''
    @功能： 获取普通用户今日签到状态
    @para: {'tqmobile':'true'}
    @return:   true/false
    @author:  chenhui 2016-11-30
'''
def getUserSignInState(para):
    info='获取普通用户今日签到状态'
    Log.LogOutput(message=info)
    response = xiansuo_post(url='/api/clue/userDubboService/getTodaySignState', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功")
    else:
            Log.LogOutput(LogLevel.ERROR, info+"失败")
    return json.loads(response.text)['response']['module']

'''  
    @功能： 新增意见反馈
    @para: 
    addUserFeedbackPara:新增用户反馈，请调用XsMyInformationPara中的addUserFeedbackPara
    @return: 新增成功，则返回True；否则返回False  
''' 
def add_user_feedback(addUserFeedbackPara):
    Log.LogOutput(LogLevel.INFO, "开始新增用户意见反馈...")
    response = xiansuo_post(url='/api/clue/userDubboService/addUserFeedBack', postdata=addUserFeedbackPara)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增用户意见反馈成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, "新增用户意见反馈失败")
        return False
    
'''  
    @功能： 在历史意见反馈列表检查意见反馈信息
    @para: 
    getUserFeedbackPara：获取意见反馈列表字典，请调用XsMyInformationIntf中的getUserFeedbackPara
    checkUserFeedback:意见反馈检查字典，请调用XsMyInformationIntf中的checkUserFeedbackPara
    @return: 如果检查成功，则返回True；否则返回False  
'''  
def check_user_feedback(checkUserFeedback,getUserFeedbackPara):
    try:
        Log.LogOutput(LogLevel.INFO, "在历史意见反馈中检查反馈意见信息...")
        response = xiansuo_post(url='/api/clue/userDubboService/findUserFeedBackListPageForMobile', postdata=getUserFeedbackPara)
        responseDict = json.loads(response.text)
        if responseDict['response']['module']['records']==0:
            Log.LogOutput(LogLevel.DEBUG, "用户反馈列表为空")
            return False
        #调用检查列表参数
        for item in responseDict['response']['module']['rows']:
            if findDictInDictlist(checkUserFeedback, [item['userFeedBack']]) is True:
                Log.LogOutput(LogLevel.DEBUG, "在历史反馈意见中查看到反馈信息")
                return True
        Log.LogOutput(LogLevel.WARN, "无法在历史反馈意见中查看到对应反馈信息")
        return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '检查过程中异常')
        return False
    
'''  
    @功能：在意见反馈详情页面检查意见反馈信息
    @para: 
    getFeedbackDetailPara：获取意见反馈详情字典，请调用XsMyInformationIntf中的getFeedbackDetailPara
    checkFeedbackDetailPara:意见反馈详情检查字典，请调用XsMyInformationIntf中的checkFeedbackDetailPara
    @return: 如果检查成功，则返回True；否则返回False  
'''  
def check_user_feedback_by_detail(checkFeedbackDetailPara,getFeedbackDetailPara):
    try:
        Log.LogOutput(LogLevel.INFO, "在意见反馈详情界面检查意见反馈信息...")
        response = xiansuo_post(url='/api/clue/userDubboService/getUserFeedBackByIdForMobile', postdata=getFeedbackDetailPara)
        responseDict = json.loads(response.text)
        #调用检查列表参数
        if findDictInDictlist(checkFeedbackDetailPara, [responseDict['response']['module']['userFeedBack']]) is True:
            Log.LogOutput(LogLevel.DEBUG, "在意见反馈详情界面查看到意见反馈成功")
            return True
        else:
            Log.LogOutput(LogLevel.WARN, "在意见反馈详情界面查看到意见反馈失败")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '检查过程中异常')
        return False
    
'''  
    @功能： 手机端检查后台配置的等级信息在前台是否正常显示
    @para: 
    checkGradeIntroduceCfg：检查等级配置字典，请调用XsMyInformationIntf中的checkGradeConfigPara
    @return: 如果检查成功，则返回True；否则返回False  
'''  
def check_user_grade_config(checkGradeIntroduceCfg):
    try:
        Log.LogOutput(LogLevel.INFO, "在我的等级页面查看等级介绍是否正确...")
        getInfoDict = {
                       "tqmobile":"true"
                       }
        response = xiansuo_post(url='/api/clue/personalizedConfigurationDubboService/findPublicGrade', postdata=getInfoDict)
        responseDict = json.loads(response.text)
        #调用检查列表参数
        if findDictInDictlist(checkGradeIntroduceCfg, responseDict['response']['module']) is True:
            Log.LogOutput(LogLevel.DEBUG, "在我的等级页面查看等级介绍成功")
            return True
        else:
            Log.LogOutput(LogLevel.WARN, "在我的等级页面查看等级介绍失败")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '检查过程中异常')
        return False
    
'''
    @功能： 删除所以的用户反馈信息
    @return:   
    @author:  chenhui 2017-1-11
'''
def delete_all_feedbaks():
    Log.LogOutput(message='清空用户反馈记录信息开始...')
    try:
        listPara={
                    '_search':'false',
                    'rows':2000,
                    'page':1,
                    'sidx':'id',
                    'sord':'desc'
                  }
        response = xiansuoyunwei_post(url='/userFeedBackManage/findUserFeedBackList', postdata=listPara)
#         print response.text
        resDict=json.loads(response.text)
        if resDict['records']==0:
            Log.LogOutput(message='数量为0,无需删除')
            return True
        else:
            arr=[]
            for item in resDict['rows']:
                arr.append(item['userFeedBack']['id'])
            deleteDict = {'ids[]':tuple(arr)}
#             print deleteDict
            response2 = xiansuoyunwei_post(url='/userFeedBackManage/deleteUserFeedBacks', postdata=deleteDict)
            print response2.text
            if response2.result is True:
                Log.LogOutput(LogLevel.INFO, '*用户反馈删除成功*')
            else:
                Log.LogOutput(LogLevel.DEBUG, '用户反馈删除失败!')  
    except Exception :
        Log.LogOutput(LogLevel.ERROR, '用户反馈删除异常')
        return False 