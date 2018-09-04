# -*- coding:UTF-8 -*-
'''
Created on 2016-11-16

@author: hongzenghui
'''
from __future__ import unicode_literals
from CONFIG import Global
from COMMON import Log
from CONFIG.Define import LogLevel
from CONFIG.InitDefaultPara import userInit
from Interface.PingAnJianShe.pingAnJianSheHttpCommon import pinganjianshe_get
from Interface.XianSuoApp.ShuoShuo.ShuoShuoPara import addShuoShuoPara
from Interface.XianSuoApp.xianSuoHttpCommon import xiansuo_post, xiansuo_get
from selenium.webdriver.remote import mobile
import copy
import json
from COMMON.CommonUtil import findDictInDictlist
from Interface.XianSuoApp.ShuoShuo import ShuoShuoPara

'''  
    @功能：新增说说
    @para: 
    addShuoShuoPara:请调用ShuoShuoPara中的addShuoShuoPara对象
    @return: 添加成功，则返回True；否则返回False
''' 

def add_shuoshuo(addShuoShuoPara, mobile = Global.XianSuoDftMobile, password = Global.XianSuoDftPassword):
    Log.LogOutput(LogLevel.INFO, "新增说说开始")
    response = xiansuo_post(url='/api/clue/casualTalkDubboService/addCasualTalkForMobile', postdata=addShuoShuoPara, mobile=mobile, password = password)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "新增说说成功")
            return True
    else:
            Log.LogOutput(LogLevel.ERROR, "新增说说失败")
            return False

'''  
    @功能：在说说列表查看
    @para: 
    checkShuoShuoPara:请调用ShuoShuoPara中的checkShuoShuoPara对象
    getShuoShuoPara:请调用ShuoShuoPara中的getShuoShuoPara对象
    @return: 比对成功，则返回True；否则返回False
''' 

def check_shuoshuo_in_list(checkShuoShuoPara, getShuoShuoPara, mobile = Global.XianSuoDftMobile, password = Global.XianSuoDftPassword):
    Log.LogOutput(LogLevel.INFO, "在广场说说列表查看说说开始......")
    try:
        response = xiansuo_post(url='/api/clue/casualTalkDubboService/findCasualTalksForPageForMobile', postdata=getShuoShuoPara, mobile=mobile, password = password)
#         print response.text
        responseDict = json.loads(response.text)
        if responseDict['response']['module']['records']==0:
            Log.LogOutput(LogLevel.DEBUG, "说说列表为空")
            return False
        listDict= responseDict['response']['module']['rows']
        #定义一个空列表
        newList=[]
        #重新组装待检查列表
        for item in listDict:
            newList.append(item['casualTalk'])
        #调用检查列表参数
        if findDictInDictlist(checkShuoShuoPara, newList) is True:
            Log.LogOutput(LogLevel.DEBUG, "在说说广场查看到对应说说")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "无法在说说广场查看到对应说说")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '检查过程中异常')
        return False
    

'''
    @功能：说说举报
    @para：
    addShuoShuoInfoReportPara: 请调用ShuoShuoPara中的addShuoShuoInfoReportPara
    @return:    成功返回True,否则返回False
    @author:  hongzenghui 2016-12-5
'''  
def add_shuoshuo_information_report(addShuoShuoInfoReportPara, mobile = Global.XianSuoDftMobile, password = Global.XianSuoDftPassword):
    Log.LogOutput(LogLevel.INFO, "新增说说举报开始......")
    response = xiansuo_post(url='/api/clue/informationDubboService/addInformationReport', postdata=addShuoShuoInfoReportPara, mobile=mobile, password = password)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增说说举报成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, "新增说说举报失败")
        return False

'''  
    @功能：检查我的说说列表
    @para: mylistpara：请调用ShuoShuoPara中的WoDeShouShouLieBiao对象
            checkpara：请调用ShuoShuoPara中的WoDeShuoShuoLieBiaoJianCha对象
    @author: wangzhijun
    @return: 检查成功，则返回True；否则返回False
''' 

def check_shuoshuo_my_list(checkpara,mylistpara,mobile = Global.XianSuoDftMobile, password = Global.XianSuoDftPassword):
    Log.LogOutput(LogLevel.INFO, "在我的说说列表检查说说信息.....")
    try:
        response = xiansuo_post(url='/api/clue/casualTalkDubboService/findCasualTalksForPageForMobileByUserId', postdata=mylistpara, mobile=mobile, password = password)
#         print response.text
        resultDict=json.loads(response.text)
        if resultDict['response']['module']['records']==0:
            Log.LogOutput(LogLevel.DEBUG,'我的说说列表无内容显示！')
            return False
        listDict= resultDict['response']['module']['rows']
        #定义一个空列表
        newList=[]
        #重新组装待检查列表
        for item in listDict:
            newList.append(item['casualTalk'])
        if findDictInDictlist(checkpara, newList) is True:
            Log.LogOutput(message='我的说说列表检查成功！')
            return True
        else:
            Log.LogOutput(message='我的说说列表检查失败！')
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '在我的说说列表检查说说信息过程中异常')
        return False

'''  
    @功能：获取说说列表
    @para:  squarelistpara：请调用ShuoShuoPara中的getShuoShuoPara对象
    @author: chenhui
    @return: 获取成功，则返回True；否则返回False
''' 

def get_shuoshuo_square_list(squarelistpara, mobile = Global.XianSuoDftMobile, password = Global.XianSuoDftPassword):
    Log.LogOutput(LogLevel.INFO, "获取说说列表开始")
    response = xiansuo_post(url='/api/clue/casualTalkDubboService/findCasualTalksForPageForMobile', postdata=squarelistpara, mobile=mobile, password = password)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "获取说说列表成功")
            return True
    else:
            Log.LogOutput(LogLevel.ERROR, "获取说说列表失败")
            return False

'''  
    @功能：通过说说内容查找说说id
    @para: 
    squarelistpara：请调用ShuoShuoPara中的getShuoShuoPara对象
    shuoshuoContent:说说内容
    @author: wangzhijun
    @return: 查找成功，则返回说说id；否则返回None
''' 

def get_shuoshuo_id_by_content(shuoshuoContent,squarelistpara, mobile = Global.XianSuoDftMobile, password = Global.XianSuoDftPassword):
    Log.LogOutput(LogLevel.INFO, "获取说说列表开始......")
    try:
        response = xiansuo_post(url='/api/clue/casualTalkDubboService/findCasualTalksForPageForMobile', postdata=squarelistpara, mobile=mobile, password = password)
        resultDict=json.loads(response.text)
        for item in resultDict['response']['module']['rows']:
            if item['casualTalk']['contentText']==shuoshuoContent:
                Log.LogOutput(LogLevel.DEBUG, "找到符合条件的说说，返回id")
                return item['casualTalk']['id']
        Log.LogOutput(LogLevel.DEBUG, "未找到符合条件的说说，返回None")
        return None
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '通过说说内容查找ID过程中异常')
        return None

'''  
    @功能：删除说说列表
    @para:  deletepara：请调用ShuoShuo.ShuoShuoPara中的delShuoShuoPara对象
    @author: wangzhijun
    @return: 删除成功，则返回True；否则返回False
''' 

def delete_shuoshuo(deletepara, mobile = Global.XianSuoDftMobile, password = Global.XianSuoDftPassword):
    Log.LogOutput(LogLevel.INFO, "删除说说开始")
    response = xiansuo_post(url='/api/clue/casualTalkDubboService/updateCasualTalkDelStateById', postdata=deletepara, mobile=mobile, password = password)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除说说成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, "删除说说失败")
        return False

'''  
    @功能：说说新增关注
    @para: addconcern：请调用ShuoShuoPara中的ShouShouAddConcernPara对象 
    @author: wangzhijun
    @return: 关注成功，则返回True；否则返回False
''' 

def addconcern_shuoshuo(addconcern, mobile = Global.XianSuoDftMobile, password = Global.XianSuoDftPassword):
    Log.LogOutput(LogLevel.INFO, "说说新增关注开始")
    response = xiansuo_post(url='/api/clue/concernDubboService/addConcernForCasualTalk', postdata=addconcern, mobile=mobile, password = password)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "说说新增关注成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, "说说新增关注失败")
        return False

'''  
    @功能：说说取消关注
    @para: ShuoShuoPara.ShouShouCancelConcernPara
    @author: chenhui 2017-1-4
    @return: 取消关注成功，则返回True；否则返回False
''' 

def cancel_concern_shuoshuo(para, mobile = Global.XianSuoDftMobile, password = Global.XianSuoDftPassword):
    Log.LogOutput(LogLevel.INFO, "说说取消关注开始")
    response = xiansuo_post(url='/api/clue/concernDubboService/updateCasualTalkConcernByUserIdAndInfoId', postdata=para, mobile=mobile, password = password)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "说说取消关注成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, "说说取消关注失败")
        return False
    
'''  
    @功能：获取我的关注列表
    @para: myconcernlistpara：请调用ShuoShuoPara中的WoDeConcernListPara对象 
    @author: wangzhijun
    @return: 获取成功，则返回True；否则返回False
''' 

def get_myconcern_list(myconcernlistpara, mobile = Global.XianSuoDftMobile, password = Global.XianSuoDftPassword):
    Log.LogOutput(LogLevel.INFO, "获取我的关注列表开始")
    response = xiansuo_post(url='/api/clue/concernDubboService/findCasualTalkConcernsByUserIdForPage', postdata=myconcernlistpara, mobile=mobile, password = password)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "获取我的关注列表成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "获取我的关注列表失败")
    return response

'''  
    @功能：检查我的关注列表
    @para: myconcernlistpara：请调用ShuoShuoPara中的WoDeConcernListPara对象
    checkWoDeConcernPara：请调用ShuoShuoPara中的WoDeConcernListCheckPara对象
    @author: wangzhijun
    @return: 检查成功，则返回True；否则返回False
''' 

def check_myconcern_list(checkWoDeConcernPara,myconcernlistpara, mobile = Global.XianSuoDftMobile, password = Global.XianSuoDftPassword):
    Log.LogOutput(LogLevel.INFO, "检查我的关注列表开始......")
    try:
        response = xiansuo_post(url='/api/clue/concernDubboService/findCasualTalkConcernsByUserIdForPage', postdata=myconcernlistpara, mobile=mobile, password = password)
#         print response.text
        resultDict=json.loads(response.text)
        if resultDict['response']['module']['records']==0:
            Log.LogOutput(LogLevel.DEBUG, '我的关注列表无内容显示！')
            return False
        arrList=[]
        listDict=resultDict['response']['module']['rows']
        for item in listDict:
            arrList.append(item['casualTalk'])
        if findDictInDictlist(checkWoDeConcernPara, arrList):
            Log.LogOutput(LogLevel.DEBUG, '我的关注列表检查成功！')
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, '我的关注列表检查失败！')
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR,'我的关注列表查找异常！')
        return False

'''
    @功能：对说说进行评论
    @para：
    addCommentForShuoShuoPara: 请调用XsBaoLiaoPara中的addCommentForShuoShuoPara
    @return:    成功返回True,否则返回False
    @author:  hongzenghui 2016-12-5
'''  
def add_comment_for_shuoshuo(addCommentForShuoShuoPara, mobile = Global.XianSuoDftMobile, password = Global.XianSuoDftPassword):
    Log.LogOutput(LogLevel.INFO, "新增说说评论开始")
    response = xiansuo_post(url='/api/clue/commentDubboService/addCommentForCasualTalk', postdata=addCommentForShuoShuoPara, mobile=mobile, password = password)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增说说评论成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, "新增说说评论失败")
        return False
    
'''
    @功能：通过说说详情，检查说说评论信息
    @para：
    informationId: 说说id信息
    checkCommentInShuoShuoPara：请调用ShouShouPara中的checkCommentInShuoShuoPara
    @return:    检查成功返回True,否则返回False
    @author:  hongzenghui 2016-12-5
'''  
def check_comment_in_shuoshuo(informationId, checkCommentInShuoShuoPara=None, mobile = Global.XianSuoDftMobile, password = Global.XianSuoDftPassword):
    try:
        Log.LogOutput(LogLevel.INFO, "开始检查说说评论信息......")
        getCommnetDict = copy.deepcopy(ShuoShuoPara.getCommentInShuoShuoPara)
        getCommnetDict['informationId'] = informationId
        response = xiansuo_post(url='/api/clue/commentDubboService/findCommentsByInfoIdForPage', postdata=getCommnetDict, mobile=mobile, password = password)
#         print response.text
        responseDict = json.loads(response.text)
        if responseDict['response']['module']['records']==0:
            Log.LogOutput(LogLevel.DEBUG, "说说评论为空")
            return False
        if findDictInDictlist(checkCommentInShuoShuoPara, responseDict['response']['module']['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG, "说说评论检查成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "说说评论检查失败")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '检查说说评论过程中异常')
        return False

'''  
    @功能：通过评论内容查找评论id
    @para: 
    informationId：说说id
    CommentContext：评论内容
    @author: wangzhijun
    @return: 查找成功，则返回说说id；否则返回None
''' 

def get_comment_id_by_content(informationId, CommentContext, mobile = Global.XianSuoDftMobile, password = Global.XianSuoDftPassword):
    Log.LogOutput(LogLevel.INFO, "获取评论列表开始......")
    try:
        getCommnetDict = copy.deepcopy(ShuoShuoPara.getCommentInShuoShuoPara)
        getCommnetDict['informationId'] = informationId
        response = xiansuo_post(url='/api/clue/commentDubboService/findCommentsByInfoIdForPage', postdata=getCommnetDict, mobile=mobile, password = password)
        resultDict=json.loads(response.text)
        for item in resultDict['response']['module']['rows']:
            if item['contentText']==CommentContext:
                Log.LogOutput(LogLevel.DEBUG, "找到符合条件的评论，返回id")
                return item['id']
        Log.LogOutput(LogLevel.DEBUG, "未找到符合条件的评论，返回None")
        return None
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '通过说说内容查找ID过程中异常')
        return None   
    
'''  
    @功能：通过我的评论，检查评论列表
    @para: myccommentlistpara：请调用ShuoShuoPara中的getMyCommentListPara对象
    checkWoDeCommentPara：请调用ShuoShuoPara中的checkMyCommentListPara对象
    @author: wangzhijun
    @return: 检查成功，则返回True；否则返回False
''' 

def check_comment_by_my_comment(checkWoDeCommentPara,mycommentlistpara, mobile = Global.XianSuoDftMobile, password = Global.XianSuoDftPassword):
    Log.LogOutput(LogLevel.INFO, "通过我的评论检查评论列表开始......")
    try:
        response = xiansuo_post(url='/api/clue/commentDubboService/findMyCommentsByInfoIdForPage', postdata=mycommentlistpara, mobile=mobile, password = password)
        resultDict=json.loads(response.text)
        if resultDict['response']['module']['records']==0:
            Log.LogOutput(LogLevel.DEBUG,'我的评论列表无内容显示！')
            return False
        if findDictInDictlist(checkWoDeCommentPara, resultDict['response']['module']['rows']) is True:
            Log.LogOutput(LogLevel.DEBUG,'通过我的评论检查评论列表成功！')
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG,'通过我的评论检查评论列表失败！')
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR,'通过我的评论检查评论列表过程中异常！')
        return False
    
'''
    @功能：说说详情删除评论
    @para：
    delCommentForShuoShuoPara: 请调用ShouShouPara中的delCommentForShuoShuoPara
    @return:    成功返回True,否则返回False
    @author:  wangzhijun 2016-12-22
'''  
def delete_comment_for_shuoshuo(delCommentForShuoShuoPara, mobile = Global.XianSuoDftMobile, password = Global.XianSuoDftPassword):
    Log.LogOutput(LogLevel.INFO, "删除说说评论开始.......")
    response = xiansuo_post(url='/api/clue/commentDubboService/updateCommentDelStateById', postdata=delCommentForShuoShuoPara, mobile=mobile, password = password)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除说说评论成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, "删除说说评论失败")
        return False  

'''
    @功能：说说新增点赞
    @para：
    addpraisePara: 请调用ShouShouPara中的addPraiseForShouShouPara
    @return:    成功返回True,否则返回False
    @author:  wangzhijun 2016-12-22
'''  
def add_praise_for_shuoshuo(addpraisePara, mobile = Global.XianSuoDftMobile, password = Global.XianSuoDftPassword):
    Log.LogOutput(LogLevel.INFO, "说说新增点赞开始.......")
    response = xiansuo_post(url='/api/clue/praiseDubboService/addPraiseForCasualTalk', postdata=addpraisePara, mobile=mobile, password = password)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "说说新增点赞成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, "说说新增点赞失败")
        return False 
    
'''
    @功能：说说取消点赞
    @para：
    cancelpraisePara: 请调用ShouShouPara中的cancelPraiseForShouShouPara
    @return:    成功返回True,否则返回False
    @author:  wangzhijun 2016-12-22
'''  
def cancel_praise_for_shuoshuo(cancelpraisePara, mobile = Global.XianSuoDftMobile, password = Global.XianSuoDftPassword):
    Log.LogOutput(LogLevel.INFO, "说说取消点赞开始.......")
    response = xiansuo_post(url='/api/clue/praiseDubboService/updatePraiseForCasualTalkByUserIdAndInfoId', postdata=cancelpraisePara, mobile=mobile, password = password)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "说说取消点赞成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, "说说取消点赞失败")
        return False   

'''
    @功能：在说说详情界面查看点赞状态
    @para：
    checkPara: 请调用ShouShouPara中的checkShuoShuoDetailPara
    shuoshuoDetail: 请调用ShouShouPara中的getShuoShuoDetail
    @return:    成功返回True,否则返回False
    @author:  wangzhijun 2016-12-27
'''  
def check_praise_in_shuoshuo(checkPara,shuoshuoDetail):
    Log.LogOutput(LogLevel.INFO, "说说详情界面检查开始......")
    try:
        response = xiansuo_get(url='/api/clue/casualTalkDubboService/getCasualTalksById', param=shuoshuoDetail)
        responseDict = json.loads(response.text)
#         print response.text
        listDict= responseDict['response']['module']['casualTalk']
        if findDictInDictlist(checkPara, [listDict]) is True:
            Log.LogOutput(LogLevel.DEBUG, "说说详情页面检查成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "说说详情页面检查失败")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "说说详情界面检查过程异常")
        return False
    
'''
    @功能：在说说详情界面获取点赞数
    @para：
    shuoshuoDetail: 请调用ShouShouPara中的getShuoShuoDetail
    @return:    成功返回点赞数,否则返回None
    @author:  wangzhijun 2016-12-27
'''  
def get_praisenum_in_shuoshuo(shuoshuoDetail):
    Log.LogOutput(LogLevel.INFO, "说说详情界面获取点赞数开始......")
    response = xiansuo_get(url='/api/clue/casualTalkDubboService/getCasualTalksById', param=shuoshuoDetail)
    responseDict = json.loads(response.text)
#     print response.text
    return responseDict['response']['module']['casualTalk']['praiseNum']

'''  
    @功能：检查根据内容查询出的说说列表
    @para: 
        listpara:    ShuoShuoPara.searchShuoShuoPara
        checkpara:    ShuoShuoPara.checkShuoShuoInSearchListPara
    @return: 比对成功，则返回True；否则返回False
    @author: 2017-1-4 chenhui
''' 

def check_shuoshuo_in_search_list(listpara, checkpara, mobile = Global.XianSuoDftMobile, password = Global.XianSuoDftPassword):
    Log.LogOutput(LogLevel.INFO, "检查根据内容查询出的说说列表......")
    try:
        response = xiansuo_post(url='/api/clue/casualTalkDubboService/searchCasualTalksForPageForMobile', postdata=listpara, mobile=mobile, password = password)
#         print response.text
        responseDict = json.loads(response.text)
        if responseDict['response']['module']['records']==0:
            Log.LogOutput(LogLevel.DEBUG, "说说列表为空")
            return False
        listDict= responseDict['response']['module']['rows']
        #定义一个空列表
        newList=[]
        #重新组装待检查列表
        for item in listDict:
            newList.append(item['casualTalk'])
        #调用检查列表参数
        if findDictInDictlist(checkpara, newList) is True:
            Log.LogOutput(LogLevel.DEBUG, "在列表中查看到对应说说")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "无法在列表中查看到对应说说")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '检查过程中异常')
        return False
    
    
    '''
    @功能：说说评论举报
    @para：
    ReportCommentShuoShuoPara: 请调用ShuoShuoPara中的ReportCommentShuoShuoPara
    @return:    成功返回True,否则返回False
    @author:  gaorong 2017-07-14
'''  
def add_Comment_report(ReportCommentShuoShuoPara, mobile = Global.XianSuoDftMobile, password = Global.XianSuoDftPassword):
    Log.LogOutput(LogLevel.INFO, "新增信息评论举报开始")
    response = xiansuo_post(url='/api/clue/commentDubboService/addCommentReport', postdata=ReportCommentShuoShuoPara, mobile=mobile, password = password)
    print response.text   
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增信息评论举报成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, "新增信息评论举报失败")
        return False
 