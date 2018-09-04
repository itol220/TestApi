# -*- coding:UTF-8 -*-
'''
Created on 2015-11-24

@author: N-133
'''
from __future__ import unicode_literals
from COMMON import Log
from COMMON.CommonUtil import findDictInDictlist, httpResponseResultDeal
from CONFIG import Global
from CONFIG.Define import LogLevel
from CONFIG.Global import XianSuoDftMobile, XianSuoDftPassword
from CONFIG.InitDefaultPara import userInit, clueUserInit
from Interface.PingAnJianShe.pingAnJianSheHttpCommon import pinganjianshe_post
from Interface.XianSuoApp.XinXiGuangChang import XsInformationSquarePara
from Interface.XianSuoApp.xianSuoHttpCommon import xiansuo_post, xiansuo_get
import copy
import json
import md5
import requests
'''
    @功能：设置分享状态
    @XianSuoPara{ids,showState}
    @return:    response
    @author:  chenhui 2016-03-21
'''  
# PC设置状态
def setClueShowState(para):
    Log.LogOutput(LogLevel.INFO, "设置线索状态")
    response = pinganjianshe_post(url='/clueManage/clueInformationManage/updateInformationShowStateByIds.action', postdata=para)
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "设置线索状态成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "设置线索状态失败")
    return response

'''
    @功能：PC官方回复
    @XianSuoPara
    @return:    response
    @author:  chenhui 2016-03-21
'''  
# 新增线索
def officialReply(para):
    Log.LogOutput(LogLevel.INFO, "PC设置官方回复")
    response = pinganjianshe_post(url='/clueManage/clueInformationManage/officialReply.action', postdata=para,username=userInit['DftJieDaoUser'],password='11111111')
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "设置官方回复成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "设置官方回复失败")
    return response

'''
    @功能：获取信息广场列表
    @param :listPara=XsInformationSquarePara.informationSquareListPara 
    @return:    response
    @author:  chenhui 2016-03-22
'''  
# 获取线索、信息广场列表
def getClueList(para):
    Log.LogOutput(LogLevel.INFO, "获取信息广场列表数据")
    response = xiansuo_post(url='/api/clue/informationDubboService/findInformationsForPageForMobile', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "列表数据获取成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "列表数据获取失败")
    return response

'''
    @功能：获取用户信息
    @param param:    {'tqmobile':'','id':''}
    @return:    response
    @author:  chenhui 2016-03-22
'''  
# 获取用户信息
def getUserInfo(para):
    Log.LogOutput(LogLevel.INFO, "获取用户信息")
    response = xiansuo_get(url='/api/clue/userDubboService/getUserById', param=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "用户信息获取成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "用户信息获取失败")
    return response

'''
    @功能： 检查某一字典是否存在于用户信息返回的字典中
    @para: 
    @return: 如果检查成功，则返回True；否则返回False  
    @author:  chenhui 2016-3-21
'''    
def checkDictInUserInfoDict(checkPara,userpara):
    try:
        Log.LogOutput(LogLevel.INFO, "检查记录是否存在于用户信息字典中")
        response=getUserInfo(para=userpara)
        responseDict = json.loads(response.text)
        #print response.text
        listDict= responseDict['response']['module']
        #定义一个空列表
        newList=[]
        #将字典项转化为列表
        newList.append(listDict)
        #调用检查列表参数
        if findDictInDictlist(checkPara, newList) is True:
            Log.LogOutput(LogLevel.DEBUG, "检测字典成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "检测字典失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '检测异常')
            return False
        
'''
    @功能：获取用户登录信息
    @return:    response
    @author:  chenhui 2016-03-22
'''
def getUserLogin(mobile=XianSuoDftMobile, password=XianSuoDftPassword, mobileType="android"):
    # 获取登录信息
    Log.LogOutput(LogLevel.INFO, "获取用户登录信息")
    appkey =Global.XianSuoAppKey
    secretkey =Global.XianSuoSecretKey
    paramString=''

    if mobile is None or password is None: 
        m1 = md5.new()
        m1.update(Global.XianSuoDftPassword)
        m2=md5.new()
        #需要排序的字典
        sortDict={"mobile":Global.XianSuoDftMobile, "password":m1.hexdigest(), "tqmobile":"true","mobileType":mobileType,"appKey":appkey}
        sortKeyList=sorted(sortDict.keys(),key=lambda d:d[0])
        #拼接key、value字符串
        for item in sortKeyList:
            paramString=paramString+item+sortDict[item]
        #需要参与md5运算的字符串，还要加上secretKey的值，不需要加上该key
        paramString=secretkey+paramString
        m2.update(paramString)
        #运算结果转成大写
        sign=m2.hexdigest().upper()
        postData = {"mobile":Global.XianSuoDftMobile,"password":m1.hexdigest(),"tqmobile":"true","mobileType":mobileType,
                    "appKey":appkey,"sign":sign}
    else:
        m1 = md5.new()
        m1.update(password)
        m2=md5.new()
        #需要排序的字典
        sortDict={"mobile":mobile, "password":m1.hexdigest(), "tqmobile":"true","mobileType":mobileType,"appKey":appkey}
        sortKeyList=sorted(sortDict.keys(),key=lambda d:d[0])
        for item in sortKeyList:
            paramString=paramString+item+sortDict[item]
        #需要参与md5运算的字符串，还要加上secretKey的值，不需要加上该key
        paramString=secretkey+paramString
        m2.update(paramString)
        #运算结果转成大写
        sign=m2.hexdigest().upper()
        postData = {"mobile":mobile, "password":m1.hexdigest(), "tqmobile":"true","mobileType":mobileType,
                    "appKey":appkey,"sign":sign}
    response = requests.get("%s/api/clue/loginDubboService/loginNew" % Global.XianSuoShouJiDaiLiUrl,params=postData)
    responseObj=httpResponseResultDeal(response)
    jsonData = json.loads(responseObj.text)
#     print responseObj.text
    return jsonData



'''
    @功能： 检查某一字典是否存在于信息详情的information字典中
    @para: listPara=XsInformationSquarePara.informationSquareListPara
                checkPara=
    @return: 如果检查成功，则返回True；否则返回False  
    @author:  chenhui 2016-3-21
'''    
def checkDictInClueList(checkPara,listPara):
    try:
        Log.LogOutput(LogLevel.INFO, "检查记录是否存在于信息广场中")
        response=getClueList(para=listPara)
        responseDict = json.loads(response.text)
        #print response.text
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
            Log.LogOutput(LogLevel.ERROR, '检测异常')
            return False
'''
    @功能：获取线索详情
    @return:    response
    @author:  chenhui 2016-03-22
'''  
def getClueDetails(para):
    Log.LogOutput(LogLevel.INFO, "获取线索详细信息")
    response = xiansuo_post(url='/api/clue/informationDubboService/getInformationById', postdata=para)
    #print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "线索详情获取成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "线索详情获取失败")
    return response


'''
    @功能：获取线索简易步骤信息
    @return:    response
    @author:  chenhui 2016-03-23
'''  
def getClueStepsInfo(para):
    Log.LogOutput(LogLevel.INFO, "获取线索简易步骤信息")
    response = xiansuo_post(url='/api/clue/informationStepDubboService/getInformationStepsByInfoId', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "线索简易步骤信息获取成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "线索简易步骤信息获取失败")
    return response
    
'''
    @功能：获取线索内部步骤信息
    @return:    response
    @author:  chenhui 2016-03-23
'''  
def getClueInnerStepsInfo(para):
    Log.LogOutput(LogLevel.INFO, "获取线索内部步骤信息")
    response = xiansuo_get(url='/api/clue/informationStepDubboService/findInnerStepByStepId', param=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "线索内部步骤信息获取成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "线索内部步骤信息获取失败")
    return response

'''
    @功能： 检查某一字典是否存在于信息详情的步骤informationSteps字典中，用于验证流程状态
    @para: 
    @return: 如果检查成功，则返回True；否则返回False  
    @author:  chenhui 2016-3-23
'''    
def checkDictInInforSteps(checkPara,stepPara):
    try:
        Log.LogOutput(LogLevel.INFO, "检查记录是否存在于处理步骤中")
        response=getClueStepsInfo(para=stepPara)
        responseDict = json.loads(response.text)
#         print response.text
        listDict= responseDict['response']['module']['informationSteps']
        if findDictInDictlist(checkPara, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "检测步骤成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "检测步骤失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '检测步骤异常')
            return False
'''
    @功能： 检查某一字典是否存在于信息详情的内部步骤字典中，用于验证处理意见
    @para: 
    @return: 如果检查成功，则返回True；否则返回False  
    @author:  chenhui 2016-3-23
'''    
def checkDictInInnerInforSteps(checkPara,innerStepPara):
    try:
        Log.LogOutput(LogLevel.INFO, "检查处理意见是否存在于处理步骤中")
        response=getClueInnerStepsInfo(para=innerStepPara)
        responseDict = json.loads(response.text)
        listDict= responseDict['response']['module']
        #定义一个空列表
        newList=[]
        #重新组装待检查列表
        for item in listDict:
            newList.append(item['innerStep'])
        if findDictInDictlist(checkPara, newList) is True:
            Log.LogOutput(LogLevel.DEBUG, "检测处理意见成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "检测处理意见失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '检测处理意见异常')
            return False
'''
    @功能：线索转事件
    @param:    XsInformationSquarePara.culeToIssuePara
    @return:    response
    @author:  chenhui 2016-03-23
'''  
def clueToIssue(para,username=userInit['DftJieDaoUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "将线索转为事件处理")
    response = pinganjianshe_post(url='/issues/issueManage/addIssueByClue.action', postdata=para,username=username,password=password)
#     print 'cluetoissue  '+response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "将线索转为事件处理成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "将线索转为事件处理失败")
    return response

'''
    @功能：新增点赞
    @return:    response
    @author:  chenhui 2016-03-23
'''  
def addPraise(para):
    Log.LogOutput(LogLevel.INFO, "新增点赞")
    response = xiansuo_post(url='/api/clue/praiseDubboService/addPraise', postdata=para)
    #print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "点赞成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "点赞失败")
    return response
'''
    @功能：验证点赞列表
    @return:    true/false
    @author:  chenhui 2016-03-23
'''  
def checkInMyPraiseList(checkPara,listPara):
    try:
        Log.LogOutput(LogLevel.INFO, "检查是否存在于我的点赞列表中")
        response = xiansuo_post(url='/api/clue/praiseDubboService/findPraisesByUserIdForPage', postdata=listPara)
        #print response.text
        responseDict = json.loads(response.text)
        listDict= responseDict['response']['module']['rows']
        #定义一个空列表
        newList=[]
        #重新组装待检查列表
        for item in listDict:
            newList.append(item['information'])
        if findDictInDictlist(checkPara, newList) is True:
            Log.LogOutput(LogLevel.DEBUG, "检测点赞成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "检测点赞失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '检测点赞异常')
            return False
        
'''
    @功能：新增评论
    @return:    response
    @author:  chenhui 2016-03-23
'''  
def addComment(para,mobile=Global.XianSuoDftMobile, password=Global.XianSuoDftPassword):
    Log.LogOutput(LogLevel.INFO, "新增评论")
    response = xiansuo_post(url='/api/clue/commentDubboService/addComment', postdata=para,mobile=mobile,password=password)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "评论成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "评论失败")
    return response

'''
    @功能：验证我的评论列表
    @return:    true/false
    @author:  chenhui 2016-03-23
'''  
def checkInMyCommentList(checkPara,listPara):
    try:
        Log.LogOutput(LogLevel.INFO, "检查是否存在于我的评论列表中")
        response = xiansuo_post(url='/api/clue/commentDubboService/findMyCommentsByInfoIdForPage', postdata=listPara)
        #print response.text
        responseDict = json.loads(response.text)
        listDict= responseDict['response']['module']['rows']
        if findDictInDictlist(checkPara, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "检测我的评论成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "检测我的评论失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '检测我的评论异常')
            return False
        
'''
    @功能：验证评论列表
    @return:    true/false
    @author:  chenhui 2016-03-23
'''  
def checkInCommentList(checkPara,listPara):
    try:
        Log.LogOutput(LogLevel.INFO, "检查是否存在于评论列表中")
        response = xiansuo_post(url='/api/clue/commentDubboService/findCommentsByInfoIdForPage', postdata=listPara)
        #print response.text
        responseDict = json.loads(response.text)
        listDict= responseDict['response']['module']['rows']
        if findDictInDictlist(checkPara, listDict) is True:
            Log.LogOutput(LogLevel.DEBUG, "检测评论成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "检测评论失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '检测评论异常')
            return False        
        
'''
    @功能：新增关注
    @return:    response
    @author:  chenhui 2016-03-23
'''  
def addConcern(para):
    Log.LogOutput(LogLevel.INFO, "新增关注")
    response = xiansuo_post(url='/api/clue/concernDubboService/addConcern', postdata=para)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "关注成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "关注失败")
    return response

'''
    @功能：取消关注
    @return:    response
    @author:  chenhui 2016-03-23
'''  
def cancelConcern(para):
    Log.LogOutput(LogLevel.INFO, "取消关注")
    response = xiansuo_post(url='/api/clue/concernDubboService/updateConcernByUserIdAndInfoId', postdata=para)
    #print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "取消关注成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "取消关注失败")
    return response

'''
    @功能：验证关注列表
    @return:    true/false
    @author:  chenhui 2016-03-23
'''  
def checkInConcernList(checkPara,listPara):
    try:
        Log.LogOutput(LogLevel.INFO, "检查是否存在于关注列表中")
        response = xiansuo_post(url='/api/clue/concernDubboService/findConcernsByUserIdForPage', postdata=listPara)
#         print 'concern:'+response.text
        responseDict = json.loads(response.text)
        listDict= responseDict['response']['module']['rows']
        newList=[]
        for item in listDict:
            newList.append(item['information'])
        if findDictInDictlist(checkPara, newList) is True:
            Log.LogOutput(LogLevel.DEBUG, "检测关注成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "检测关注失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '检测关注异常')
            return False 
        
'''
    @功能： 获取热门搜索关键词
    @para:    XsInformationSquarePara.getHotKeywordPara
    @return: response
    @author:  chenhui 2016-12-16
'''
def get_hot_search_list_for_mobile(para):
    info='获取热门搜索关键词'
    Log.LogOutput(LogLevel.INFO, info)
    response = xiansuo_get(url='/api/clue/personalizedConfigurationDubboService/findHotSearch', param=para)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, info+"成功!")
    else:
        Log.LogOutput(LogLevel.DEBUG, info+"失败!")
    return response

'''
    @功能： 手机端检查热门搜索关键词列表
    @para:    checkpara:    XiTongPeiZhiPara.hotSearchListCheckPara
                    listpara:        XsInformationSquarePara.getHotKeywordPara
    @return: response
    @author:  chenhui 2016-12-16
'''
def check_hot_search_list(checkpara,listpara):
    info='手机端检查热门搜索关键词列表'
    Log.LogOutput(LogLevel.INFO, info)
    try:
        response = get_hot_search_list_for_mobile(para=listpara)
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
    @功能： 通过关键词名称获取排序号
    @para:    'keyword'
    @return:  如果找到，返回排列序号，如果没找到，则返回-1，如果异常，返回-2
    @author:  chenhui 2016-12-16
'''
def get_hot_search_display_seq_by_keyword_for_mobile(para):
    info='手机端通过关键词名称获取排序号'
    Log.LogOutput(LogLevel.INFO, info)
    listpara=copy.deepcopy(XsInformationSquarePara.getHotKeywordPara)
    try:
        response = get_hot_search_list_for_mobile(para=listpara)
        resDict=json.loads(response.text)
#         print response.text
        for item in resDict['response']['module']:
            if item['keyword']==para:
                Log.LogOutput(LogLevel.INFO, info+'成功')
                return item['displaySeq']
        Log.LogOutput(LogLevel.INFO, info+'失败')
        return -1 
    except Exception:
        Log.LogOutput(LogLevel.ERROR, info+'出现异常')
        return -2

'''
    @功能： 在消息列表检查消息
    @para:    
    checkMessagePara:检查消息字典，调用XsInformationSquarePara中的checkMessagePara
    getMessageListPara:获取消息列表字典，调用XsInformationSquarePara中的getMessageListPara
    @return: 检查成功，返回True;否则返回False
    @author:  hongzenghui 2016年12月26日
'''
def check_message_in_message_list(checkMessagePara,getMessageListPara):
    Log.LogOutput(LogLevel.INFO, '消息列表检查消息内容开始......')
    try:
        response = xiansuo_post(url='/api/clue/umMessageBoxDubboService/findUmMessageBoxForPageNew', postdata=getMessageListPara)
#         print response.text
        responseDict=json.loads(response.text)
        if findDictInDictlist(checkMessagePara,responseDict['response']['module']['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "消息列表检查消息内容成功!")
            return True
        else:
            Log.LogOutput(LogLevel.INFO, "消息列表检查消息内容失败!")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "消息列表检查消息内容过程中异常")
        return False
    
'''
    @功能： 在消息列表通过消息内容获取id
    @para:    
    messageContent:消息内容
    getMessageListPara:获取消息列表字典，调用XsInformationSquarePara中的getMessageListPara
    @return: 查找成功，返回ID信息;否则返回None
    @author:  hongzenghui 2016年12月26日
'''
def get_message_id_by_message_content(messageContent,getMessageListPara):
    Log.LogOutput(LogLevel.INFO, '在消息列表获取消息ID开始......')
    try:
        response = xiansuo_post(url='/api/clue/umMessageBoxDubboService/findUmMessageBoxForPageNew', postdata=getMessageListPara)
        responseDict=json.loads(response.text)
#         #print response.text
        for item in responseDict['response']['module']['rows']:
            if item['infoContent'] == messageContent:
                Log.LogOutput(LogLevel.DEBUG, "检查到消息，返回ID")
                return item['id']
        Log.LogOutput(LogLevel.DEBUG, "无法找到相应的信息，返回None!")
        return None
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "消息列表查找消息过程中异常")
        return None
    
'''
    @功能： 将消息置为已读
    @para:
    messageId:消息ID
    @return: 设置成功，返回True;否则返回False
    @author:  hongzenghui 2016年12月26日
'''
def set_message_to_readed(messageId):
    setReadedDict = {
                     'id':messageId,
                     'tqmobile':'true'
                     }
    Log.LogOutput(LogLevel.INFO, '开始设置消息为已读......')
    response = xiansuo_post(url='/api/clue/umMessageBoxDubboService/updateUmMessageBoxIsRead', postdata=setReadedDict)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "消息设置为已读成功!")
        return True
    else:
        Log.LogOutput(LogLevel.DEBUG, "消息设置为已读失败!")
        return False