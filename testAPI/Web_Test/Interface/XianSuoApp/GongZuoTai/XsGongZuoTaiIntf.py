# -*- coding:UTF-8 -*-
'''
Created on 2016-3-25

@author: N-133
'''
from __future__ import unicode_literals
from COMMON import Log
from COMMON.CommonUtil import findDictInDictlist
from CONFIG import Global
from CONFIG.Define import LogLevel
from Interface.PingAnJianShe.Common.CommonIntf import getDbQueryResult
from Interface.PingAnJianShe.ShiJianChuLi.ShiJianChuLiIntf import exeDbQuery
from Interface.XianSuoApp.GongZuoTai import XsGongZuoTaiPara
from Interface.XianSuoApp.GongZuoTai.XsGongZuoTaiPara import userAddPara, \
    userUpdatePara
from Interface.XianSuoApp.WoDeXinXi import XsMyInformationIntf
from Interface.XianSuoApp.WoDeXinXi.XsMyInformationIntf import encodeToMd5
from Interface.XianSuoApp.xianSuoHttpCommon import xiansuo_post, xiansuo_get, \
    desEncrypt, postWithSid, xiansuo_post2
from Interface.YunWeiPingTai.YunWeiCommon import YunWeiCommonIntf
from Interface.YunWeiPingTai.yunWeiPingTaiHttpCommon import xiansuoyunwei_post
import copy
import json
import random
import time

'''
    @功能：注销
    @return:    response
    @author:  chenhui 2016-03-22
'''  
def logout(para):
    Log.LogOutput(LogLevel.INFO, "注销")
    response = xiansuo_get(url='/api/clue/loginDubboService/loginOut', param=para)
    #print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "注销成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "注销失败")
    return response

'''
    @功能：获取验证码
    @return:    response
    @author:  chenhui 2016-03-22
'''  
def getValidateCode(mobile):
    Log.LogOutput(LogLevel.INFO, "获取验证码")
    #加密参数
    keyPara={
            'key':'tqmobile',
            'value':mobile
             }
    #获取验证码参数
    param={
           'tqmobile':'true',
           'mobile':desEncrypt(para=keyPara)#des加密结果
           }
    response = xiansuo_post2(url='/api/clue/loginDubboService/getValidateCode', postdata=param)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "获取验证码成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "获取验证码失败")
    return response

'''
    @功能：新增（注册）用户
    @return:    response
    @author:  chenhui 2016-04-7
'''  
def addUser(para):
    Log.LogOutput(LogLevel.INFO, "注册用户")
    response = xiansuo_post2(url='/api/clue/userDubboService/addUser', postdata=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "注册用户成功")
    else:
        Log.LogOutput(LogLevel.DEBUG, "注册用户失败")
    return response

'''
    @功能：注册一123开头的随机手机号码
    @return:    注册成功返回手机号码，注册失败返回0
    @author:  chenhui 2017-05-17
'''  
def regist_random_mobile(password=Global.XianSuoDftPassword):
    Log.LogOutput(LogLevel.INFO, "注册一个123开头的随机用户")
    registMobile='123%s'%str(createRandomNumber(length=8))
    count=YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand="select count(*)  from users w where w.mobile='%s'" % registMobile)
    while count>=1:
        registMobile='123%s'%str(createRandomNumber(length=8))
        count=YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand="select count(*)  from users w where w.mobile='%s'" % registMobile)
    try:
        #新用户注册
        getValidateCode(mobile=registMobile)
        para2=copy.deepcopy(userAddPara)
        para2['mobile'] = registMobile
        para2['validateCode'] = '123456' 
        para2['mobileKey'] = createRandomNumber(length=15)
        desPara={
                 'key':time.strftime("%Y%m%d"),
                 'value':para2['mobileKey']
        }
        para2['mobileKeyEncrypt']=desEncrypt(para=desPara)
        para2['password'] =encodeToMd5(password)
        ret =addUser(para2)
        assert ret
        return registMobile
    except Exception,e:
        Log.LogOutput(message='注册随机新用户异常%s'%str(e))
        raise RuntimeError('注册随机新用户异常')
'''
    @功能：新注册用户新增邀请码
    @param :    {'tqmobile':'','id':'','inviteCode':''}
    @return:    response
    @author:  chenhui 2016-11-30
'''  
def addInviteCode(para,mobile=None):
    info="新注册用户新增邀请码"
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuo_post(url='/api/clue/userDubboService/addUserInviteCode', postdata=para,mobile=mobile)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功")
    else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败")
    return response

'''
    @功能：首次登录修改密码
    @return:    response
    @author:  chenhui 2016-4-7
'''  
def fristChangePassword(para):
    Log.LogOutput(LogLevel.INFO, "首次登录修改密码")
    response = xiansuo_post(url='/api/clue/userDubboService/fristChangePassword', postdata=para)
    #print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "首次登录修改密码成功")
    else:
            Log.LogOutput(LogLevel.DEBUG, "首次登录修改密码失败")
    return response

'''
    @功能：找回密码
    @para:
    getBackPasswordPara:找回密码字典，请调用XsGongZuoTaiPara中的getBackPasswordPara
    @return:返回接口response    
    @author:  chenhui 2016-12-22
'''  
def resetPassword(getBackPasswordPara):
    Log.LogOutput(LogLevel.INFO, "重置密码")
    response = xiansuo_post2(url='/api/clue/userDubboService/resetpassword', postdata=getBackPasswordPara)
    #print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "重置密码成功")
    else:
        Log.LogOutput(LogLevel.DEBUG, "重置密码失败")
    return response


'''
    @功能：获取未读消息数
    @return:    具体数或者-1
    @author:  chenhui 2017-3-30
'''  
def getMessageBoxUnReadCount(para):
    Log.LogOutput(LogLevel.INFO, "获取未读消息数")
    response = xiansuo_get(url='/api/clue/umMessageBoxDubboService/getUmMessageBoxUnReadCountNew', param=para)
#    print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "获取未读消息数成功")
            json.loads(response.text)
            return json.loads(response.text)['response']['module']
    else:
            Log.LogOutput(LogLevel.DEBUG, "获取未读消息数失败")
            return -1

'''
    @功能：从数据库中删除用户
    @return:    response
    @author:  chenhui 2016-4-7
'''  
def deleteUserFromDb(mobile,dbUser=Global.XianSuoYunWeiInfo['DbUser'], dbPass=Global.XianSuoYunWeiInfo['DbPass']):
    Log.LogOutput(LogLevel.INFO, "清除手机用户"+mobile)
    count=getDbQueryResult(dbCommand="select count (*) from users where mobile='%s'"%mobile,dbUser=dbUser, dbPass=dbPass)
    #print count
    if count>0:
        dbCommand="delete from users where mobile = '%s'"%mobile 
        exeDbQuery(dbCommand = dbCommand, dbUser=dbUser, dbPass=dbPass)
    return True
        
'''
    @功能：检查用户是否在运维管理平台-在线用户列表中
    @return:    response
    @author:  chenhui 2016-4-7
'''  
def checkUserOnlineList(checkpara,listpara):
    Log.LogOutput(LogLevel.INFO, "检查用户是否在运维管理平台-在线用户列表中")
    try:
        response = xiansuoyunwei_post(url='/onLineUserManage/onLineUserList', postdata=listpara)
        responseDict=json.loads(response.text)
#         print response.text
        if findDictInDictlist(checkpara,responseDict['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "用户存在于在线列表中")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "用户不存在于在线列表中")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '出现异常')
            return False
        
'''
    @功能：新增反馈
    @return:    response
    @author:  chenhui 2016-4-11
'''  
def addUserFeedBack(para):
    Log.LogOutput(LogLevel.INFO, "新增用户反馈")
    response = xiansuo_post(url='/api/clue/userDubboService/addUserFeedBack', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "新增用户反馈成功")
    else:
            Log.LogOutput(LogLevel.DEBUG, "新增用户反馈失败")
    return response        
    
'''
    @功能：     生成一个随机数字字符串
    @para: 
    length: 随机数位数，默认为15位
    @return: 返回一串一定位数数字组成的字符串
    已有更好的随机数方法，Interface.XianSuoApp.JiFenShangCheng.XsJiFenShangChengIntf.createRandomNumber
'''

def createRandomNumber(length=15):
    if length<=0:
        Log.LogOutput(LogLevel.ERROR, "参数错误，请输入正整数")
        return -1
    else:
        loop=length/10
        code_list = []
        for i in range(loop+1):
            for i in range(10): # 0-9数字
                code_list.append(str(i))
    myslice = random.sample(code_list, length)
    random_number = ''.join(myslice) # list to string
    return random_number

'''
    @功能：采用固定sid的post方法发送请求，用以验证返回错误信息
    @XianSuoPara.XinZeng
    @return:    response
    @author:  chenhui 2016-06-14
'''  

# 新增线索
def addClueWithSpecialWay(sid,XianSuoDict, username = None, password = None):
    Log.LogOutput(LogLevel.INFO, "新增线索开始")
    response = postWithSid(sid=sid,url='/api/clue/informationDubboService/addInformationForMobile', postdata=XianSuoDict)
    #print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "新增线索成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "新增线索失败")
    return response

'''
    @功能：初始化用户,若已存在则返回True；若不存在，则注册一个新用户
    @return:    response
    @author:  chenhui 2016-4-7
'''  
def initUser(mobile=Global.XianSuoDftMobile,password='111111',dbUser=Global.XianSuoYunWeiInfo['DbUser'], dbPass=Global.XianSuoYunWeiInfo['DbPass']):
    try:
        count=getDbQueryResult(dbCommand="select count (*) from users where mobile='%s'"%mobile,dbUser=dbUser, dbPass=dbPass)
        #print count
        if count==1:
            #检查昵称是否为默认昵称，如果不是，则更新昵称
            updatePara=copy.deepcopy(userUpdatePara)           
            updatePara['id']=getDbQueryResult(dbCommand="select id from users where mobile='%s'"%mobile,dbUser=dbUser, dbPass=dbPass)
            updatePara['nickName']="nick_%s" % mobile
            count1 = getDbQueryResult(dbCommand="select count (*) from users t where t.mobile='%s' and t.nickname='%s'" % (mobile,updatePara['nickName']),dbUser=dbUser, dbPass=dbPass)
            if count1==1:
                return True
            else:
                result = XsMyInformationIntf.updateUserInfo(updatePara)
                Log.LogOutput(message='初始化昵称成功')
                return True
            pass
        elif count==0:
            Log.LogOutput(LogLevel.INFO, "初始化线索默认用户")
            '''用户注册'''
            #获取验证码
            #调用获取验证码方法
            getValidateCode(mobile=mobile)
            #此后验证码用123456
            para=copy.deepcopy(userAddPara)
            #使用已经注册成的手机号再次进行注册
            para['mobile']=mobile
            #mobileKey采用15位随机数字，防止重复测试时失败
            para['mobileKey']=createRandomNumber(length=15)
            desPara={
                     'key':time.strftime("%Y%m%d"),
                     'value':para['mobileKey']
            }
            para['mobileKeyEncrypt']=desEncrypt(para=desPara)
            para['password']=encodeToMd5(password)
            result=addUser(para=para)
            assert result.result
            Log.LogOutput(message='初始化用户成功')
            updatePara=copy.deepcopy(XsGongZuoTaiPara.userUpdatePara)           
            updatePara['id']=getDbQueryResult(dbCommand="select id from users where mobile='%s'"%mobile,dbUser=dbUser, dbPass=dbPass)
            updatePara['nickName']="nick_%s" % mobile
            result = XsMyInformationIntf.updateUserInfo(updatePara)
            Log.LogOutput(message='初始化昵称成功')
#             assert result.result
            return result.result
        else:
            Log.LogOutput(LogLevel.ERROR, message='存在多个用户，请从数据库清除')
            return False
    except Exception,e:
        Log.LogOutput(LogLevel.ERROR, message='初始化用户出现异常'+str(e))
        
'''
    @功能：获取个性化全局配置
    @param para: 
        {    'mobileType':'ios',
             'tqmobile':'true'
        }
    @return:    response
    @author:  chenhui 2016-12-6
'''  
def get_global_config_for_mobile(para):
    info='获取个性化全局配置'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuo_post(url='/api/clue/personalizedConfigurationDubboService/findGlobalConfigByMobileType', postdata=para)
    print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功")
    else:
            Log.LogOutput(LogLevel.ERROR, info+"失败")
    return response

'''
    @功能：获取爆料统计
    @param para: 
        {    'departmentNo':'',
             'tqmobile':'true'
        }
    @return:    response
    @author:  chenhui 2016-12-6
'''  
def get_broke_static_count(para):
    info='获取爆料统计'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuo_get(url='/api/clue/informationDubboService/getBrokeStatisticsCount', param=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功")
    else:
            Log.LogOutput(LogLevel.ERROR, info+"失败")
    return response

'''
    @功能： 检查爆料统计
    @param: para:           {    'departmentNo':'',
                                         'tqmobile':'true'
                                      }
        checkPara:    JiFenShangChengPara.DuiHuanJiLuJianCha
    @return:   
    @author:  chenhui 2016-12-2
'''
def check_broke_static_count(para,checkpara):
    try:
        info='检查爆料统计'
        Log.LogOutput(LogLevel.INFO, info)
        result=get_broke_static_count(para=para)
        resultDict=json.loads(result.text)
        listDict= resultDict['response']['module']
        if findDictInDictlist(checkpara, [listDict]) is True:
            Log.LogOutput(LogLevel.DEBUG, info+"成功!")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, info+"失败!")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, info+'异常')
            return False 
        
'''
    @功能：获取处理步骤信息
    @param para: 
        {    'informationId':'',
             'tqmobile':'true'
        }
    @return:    response
    @author:  chenhui 2016-12-6
'''  
def get_information_steps(para):
    info='获取处理步骤信息'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuo_post(url='/api/clue/informationStepDubboService/getInformationStepsByInfoId', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功")
    else:
            Log.LogOutput(LogLevel.ERROR, info+"失败")
    return response

'''
    @功能：根据组织机构码获取主题内容列表
    @param para: XsGongZuoTaiPara.getThemeContentPara
    @return:    response
    @author:  chenhui 2016-12-23
'''  
def get_theme_list_for_mobile(para):
    info='根据组织机构码获取主题内容列表'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuo_get(url='/api/clue/personalizedConfigurationDubboService/findThemeContentByDepartmentNo', param=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, info+"成功")
    else:
            Log.LogOutput(LogLevel.ERROR, info+"失败")
    return response

'''
    @功能： 检查主题列表
    @param: listpara:     XsGongZuoTaiPara.getThemeContentListPara
        checkPara:    XsGongZuoTaiPara.themeContentListCheckPara
    @return:   
    @author:  chenhui 2016-12-23
'''
def check_theme_list_for_mobile(listpara,checkpara):
    try:
        info='检查主题列表'
        Log.LogOutput(LogLevel.INFO, info)
        result=get_theme_list_for_mobile(para=listpara)
        resultDict=json.loads(result.text)
        listDict= resultDict['response']['module']
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
    @功能：网格员签到
    @param 
    wangGeYuanQianDaoPara:网格员签到字典，请调用XsGongZuoTaiIntf中的wangGeYuanQianDaoPara
    @return:    签到成功，返回True,否则返回False
    @author:  hongzenghui 2016年12月22日
'''  
def add_wanggeyuan_sign_in(wangGeYuanQianDaoPara):
    Log.LogOutput(LogLevel.INFO, "开始进行网格员签到操作......")
    response = xiansuo_post(url='/api/clue/userDubboService/addUserPosition', postdata=wangGeYuanQianDaoPara)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "网格员签到操作成功")
        return True
    else:
        Log.LogOutput(LogLevel.WARN, "网格员签到操作失败")
        return False
    
'''  
    @功能： 检查网格员签到记录
    @para: 
    checkWangGeYuanSignInRecordPara：检查网格员签到记录字典，请调用XsGongZuoTaiPara中的checkWangGeYuanSignInRecordPara
    getWangGeYuanSignInRecordsPara:获取网格员签到记录字典，请调用XsGongZuoTaiPara中的getWangGeYuanSignInRecordsPara
    @return: 如果检查成功，则返回True；否则返回False  
'''  
def check_wanggeyuan_sign_in_records(checkWangGeYuanSignInRecordPara,getWangGeYuanSignInRecordsPara):
    try:
        Log.LogOutput(LogLevel.INFO, "检查网格员签到记录......")
        response = xiansuo_post(url='/api/clue/userDubboService/findUserPositionsByUserIdForPage', postdata=getWangGeYuanSignInRecordsPara)
        responseDict = json.loads(response.text)
        #调用检查列表参数
        if findDictInDictlist(checkWangGeYuanSignInRecordPara, responseDict['response']['module']['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "检查网格员签到记录成功")
            return True
        else:
            Log.LogOutput(LogLevel.WARN, "检查网格员签到记录失败")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '检查过程中异常')
        return False