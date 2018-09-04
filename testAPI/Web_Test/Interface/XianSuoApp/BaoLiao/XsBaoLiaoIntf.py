# -*- coding:UTF-8 -*-
'''
Created on 2015-11-24

@author: N-133
'''
from __future__ import unicode_literals
from COMMON import Log
from COMMON.CommonUtil import findDictInDictlist
from CONFIG import Global, InitDefaultPara
from CONFIG.Define import LogLevel
from CONFIG.InitDefaultPara import userInit
from Interface.PingAnJianShe.ShiJianChuLi import ShiJianChuLiIntf
from Interface.PingAnJianShe.pingAnJianSheHttpCommon import pinganjianshe_get, \
    pinganjianshe_post
from Interface.XianSuoApp.BaoLiao import XsBaoLiaoPara
from Interface.XianSuoApp.BaoLiao.XsBaoLiaoPara import chakanxiansuo, \
    XianSuoGuanLiLieBiao
from Interface.XianSuoApp.xianSuoHttpCommon import xiansuo_post, xiansuo_get
from Interface.YunWeiPingTai.XinXiGuanLi.XinXiGuanLiPara import InfoType
import copy
import json
from Interface.YunWeiPingTai.XinXiGuanLi.XinXiGuanLiPara import InfoType
from requests.packages.urllib3 import response



'''
    @功能：手机新增线索
    @XianSuoPara.XinZeng
    @return:    response
    @author:  chenguiliang 2016-03-08
'''  

# 新增线索
def addXianSuo(XianSuoDict, mobile = Global.XianSuoDftMobile, password = Global.XianSuoDftPassword):
    Log.LogOutput(LogLevel.INFO, "新增爆料开始")
    response = xiansuo_post(url='/api/clue/informationDubboService/addInformationForMobile', postdata=XianSuoDict, mobile=mobile, password = password)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "新增爆料成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "新增失败")
    return response

'''  
    @功能：获取爆料列表
    @para: XsBaoLiaoPara.getClueListPara 
    @author: gaorong
    @return: 添加成功，则返回True；否则返回False
''' 
def get_baoliao_square_list(CheckbaoliaoPara, mobile = Global.XianSuoDftMobile, password = Global.XianSuoDftPassword):
    Log.LogOutput(LogLevel.INFO, "获取广场爆料列表")
    response = xiansuo_post(url='/api/clue/informationDubboService/findInformationsForPageForMobile', postdata=CheckbaoliaoPara, mobile=mobile, password = password)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "获取广场爆料列表成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "获取广场爆料列表失败")
    return response


'''  
    @功能：检查广场爆料列表
    @para: getbaoliaopara：请调用XsBaoLiaoPara中的getClueListPara
           checkbaoliaopara：请调用XsBaoLiaoPara.checkClueInSquarePara
    @author: gaorong
    @return: 检查成功，则返回True；否则返回False
''' 
def check_baoliao_in_list(checkbaoliaoPara, getbaoliaoPara, mobile = Global.XianSuoDftMobile, password = Global.XianSuoDftPassword):
    Log.LogOutput(LogLevel.INFO, "在爆料列表查看爆料开始......")
    try:
        response = xiansuo_post(url='/api/clue/informationDubboService/findInformationsForPageForMobile', postdata=getbaoliaoPara, mobile=mobile, password = password)
#         print response.text
        responseDict = json.loads(response.text)     
        if responseDict['response']['module']['records']==0:
            Log.LogOutput(LogLevel.DEBUG, "爆料列表为空")
            return False
        listDict= responseDict['response']['module']['rows']
        #定义一个空列表
        newList=[]
        #重新组装待检查列表
        for item in listDict:
            newList.append(item['information'])#['contentText'])
        #调用检查列表参数
        if findDictInDictlist(checkbaoliaoPara, newList) is True:
            Log.LogOutput(LogLevel.DEBUG, "在爆料广场查看到对应爆料")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "无法在爆料广场查看到对应爆料")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, '检查过程中异常')
        return False



# 通过社管线索管理查看线索是否新增成功
def checkxiansuoCompany(companyDict,  username = userInit['DftJieDaoUser'], password = '11111111'):
    try:
        Log.LogOutput(LogLevel.INFO, "查看线索开始")
        compDict = copy.deepcopy(chakanxiansuo)
        response = pinganjianshe_get(url='/clueManage/clueInformationManage/findClueInformationPageBySearchsInfoVo.action', param=compDict,username=username, password = password)
        responseDict = json.loads(response.text)
        listDict= responseDict['rows']
        newList=[]
        for item in listDict:
            newList.append(item['information'])
        if findDictInDictlist(companyDict, newList) is True:
            Log.LogOutput(LogLevel.DEBUG, "查看线索成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "查看线索失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '查看失败')
            return False  

    '''
    @功能： 查看我的爆料列表显示
    @para: {'tqmobile':'true',
                'page':'1',
                'rows':'100'}
    @return: response  
    @author:  chenhui 2016-3-21
    '''    
def viewSchedule(para,mobile=Global.XianSuoDftMobile):
    Log.LogOutput(LogLevel.INFO, "获取我的爆料列表列表数据")
    response = xiansuo_post(url='/api/clue/informationDubboService/findInformationsForPageByUserId', postdata=para, mobile=mobile)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "获取我的爆料列表数据成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "获取我的爆料列表数据失败")
    return response
    
    '''
    @功能： 通过查看我的爆料检查新增是否成功
    @para: 
    checkPara：调用XsBaoLiaoPara中的jianchaxiansuolistPara:
                             调用XsBaoLiaoPara中的getClueInMyClueList
    @return: 如果检查成功，则返回True；否则返回False  
    @author:  chenhui 2016-3-21
    '''    
def checkClueInMyClue(checkPara,listPara=None,mobile=Global.XianSuoDftMobile):
    try:
        Log.LogOutput(LogLevel.INFO, "在我的爆料中检查爆料是否存在")
        #因之前获取字典都写在脚本，现在加分支修改
        if listPara is None:
            listPara = copy.deepcopy(XsBaoLiaoPara.getClueInMyClueList)
        response=viewSchedule(para=listPara,mobile=mobile)
#         print response.text
        responseDict = json.loads(response.text)
        if responseDict['response']['module']['records']==0:
            Log.LogOutput(LogLevel.DEBUG, "我的爆料列表为空")
            return False
        listDict= responseDict['response']['module']['rows']
        #定义一个空列表
        newList=[]
        #重新组装待检查列表
        for item in listDict:
            newList.append(item['information'])
        #调用检查列表参数
        if findDictInDictlist(checkPara, newList) is True:
            Log.LogOutput(LogLevel.DEBUG, "在我的爆料中检测线索成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "在我的爆料中检测线索失败")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '检测异常')
            return False


    '''
    @功能： 删除全部线索
    @para: 
    @return: 如果删除成功，则返回True；否则返回False  
    @author:  chenhui 2016-3-18
    '''    
def deleteAllClues():
    try:
        Log.LogOutput(message='正在清空所有线索数据...')
        listPara = copy.deepcopy(XianSuoGuanLiLieBiao)
        response = pinganjianshe_get(url='/clueManage/clueInformationManage/findClueInformationPageBySearchsInfoVo.action', param=listPara)
#         print response.text
        responseDict = json.loads(response.text)
        if responseDict['records'] == 0:
            Log.LogOutput(LogLevel.DEBUG, '列表数据为空')
        else:
            #存储所有ID
            arr=[]
            for dictListItem in responseDict['rows']:
                arr.append(dictListItem['information']['id'])
            #将所有数组中的事件ID转化为字符串参数值，以，隔开
            arrString=''
            for i in range(0,len(arr)):
                if i==0:
                    arrString=str(arr[i])
                else:
                    arrString=arrString+','+str(arr[i])
            deleteDict = {'ids':str(arrString)}
            response=pinganjianshe_get(url='/clueManage/clueInformationManage/updateInformationDelStateByIds.action',param=deleteDict)
            if response.result is True:
                Log.LogOutput(LogLevel.INFO, '*线索删除成功*')
            else:
                Log.LogOutput(LogLevel.ERROR, '线索删除失败!')       
    except Exception :
        Log.LogOutput(LogLevel.ERROR, '线索删除异常')

        return False 
   
def JuBaoBaoLiao(jubaoDict): 
    Log.LogOutput(LogLevel.INFO, "举报爆料开始")
    response = xiansuo_post(url='/api/clue/iinformationDubboService/addInformationReport', postdata=jubaoDict)
#     print response.text
    if response.result is True:
            Log.LogOutput(LogLevel.INFO, "举报线索成功")
    else:
            Log.LogOutput(LogLevel.ERROR, "举报线索失败")
    return 
    return False 
    
'''  
    @功能： 在爆料广场查看线索是否存在
    @para: 
    checkClueInSquarePara：待检查的线索，请调用XsBaoLiaoPara中的checkClueInSquarePara字典
    @return: 如果检查成功，则返回True；否则返回False  
'''  
def check_clue_in_clue_list(clueCheckDict):
    try:
        Log.LogOutput(LogLevel.INFO, "检查爆料在爆料广场中是否存在")
        clueGetDict = copy.deepcopy(XsBaoLiaoPara.getClueListPara)
        response = xiansuo_post(url='/api/clue/informationDubboService/findInformationsForPageForMobile', postdata=clueGetDict)
        responseDict = json.loads(response.text)
        if responseDict['response']['module']['records']==0:
            Log.LogOutput(LogLevel.DEBUG, "广场列表为空")
            return False
        listDict= responseDict['response']['module']['rows']
        #定义一个空列表
        newList=[]
        #重新组装待检查列表
        for item in listDict:
            newList.append(item['information'])
        #调用检查列表参数
        if findDictInDictlist(clueCheckDict, newList) is True:
            Log.LogOutput(LogLevel.DEBUG, "在广场查看到对应爆料")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "无法在广场查看到对应爆料")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '检查过程中异常')
            return False
'''  
    @功能： 在爆料广场中删除爆料
    @para: 
    deleteclueDict：待删除的线索，请调用XsBaoLiaoPara中的ShanChuBaoLiao字典
    @return: 如果删除成功，则返回True；否则返回False  
    @author:  gaorong 2016-12-06
'''  
def delete_clue(deletepara, mobile = Global.XianSuoDftMobile, password = Global.XianSuoDftPassword):
    Log.LogOutput(LogLevel.INFO, "删除爆料开始")
    response = xiansuo_post(url='/api/clue/informationDubboService/updateInformationDelStateById', postdata=deletepara, mobile=mobile, password = password)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除爆料成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, "删除爆料失败")
        return False
'''
    @功能：信息举报
    @para：
    addClueInfoReportPara: 请调用XsBaoLiaoPara中的addClueInfoReportPara
    @return:    成功返回True,否则返回False
    @author:  hongzenghui 2016-12-5
'''  
def add_clue_information_report(addClueInfoReportPara, mobile = Global.XianSuoDftMobile, password = Global.XianSuoDftPassword):
    Log.LogOutput(LogLevel.INFO, "新增信息举报开始")
    response = xiansuo_post(url='/api/clue/informationDubboService/addInformationReport', postdata=addClueInfoReportPara, mobile=mobile, password = password)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增信息举报成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, "新增信息举报失败")
        return False

'''
    @功能： 从数据库中删除举报记录
    @para: 
    @author:  chenhui 2017-1-4
'''    
def delete_information_reports_by_db(departmentno=InitDefaultPara.clueOrgInit['DftQuOrgDepNo']):
    Log.LogOutput(message='正在清空所有举报记录...')
    ShiJianChuLiIntf.exeDbQuery(dbCommand="delete from informationreports"\
                                    ,dbUser=Global.XianSuoYunWeiInfo['DbUser'],dbPass=Global.XianSuoYunWeiInfo['DbPass'])


'''
    @功能：对爆料进行评论
    @para：
    addCommentForCluePara: 请调用XsBaoLiaoPara中的addCommentForCluePara
    @return:    成功返回True,否则返回False
    @author:  hongzenghui 2016-12-5
'''  
def add_comment_for_clue(addCommentForCluePara, mobile = Global.XianSuoDftMobile, password = Global.XianSuoDftPassword):
    Log.LogOutput(LogLevel.INFO, "新增线索评论开始")
    response = xiansuo_post(url='/api/clue/commentDubboService/addComment', postdata=addCommentForCluePara, mobile=mobile, password = password)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增线索评论成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, "新增线索评论失败")
        return False
    
    '''  
    @功能：通过评论内容查找评论id
    @para: 
    informationId：爆料id
    CommentContext：评论内容
    @author: gaorong
    @return: 查找成功，则返回爆料id；否则返回None
''' 

def get_comment_id_by_content(informationId, CommentContext, mobile = Global.XianSuoDftMobile, password = Global.XianSuoDftPassword):
    Log.LogOutput(LogLevel.INFO, "获取评论列表开始......")
    try:
        getCommnetDict = copy.deepcopy(XsBaoLiaoPara.getCommentInCluePara)
        getCommnetDict['informationId'] = informationId
        response = xiansuo_post(url='/api/clue/commentDubboService/findCommentsByInfoIdForPage', postdata=getCommnetDict, mobile=mobile, password = password)
        resultDict=json.loads(response.text)
        for item in resultDict['response']['module']['rows']:
            if item['contentText']==CommentContext:
                Log.LogOutput(LogLevel.WARN, "找到符合条件的评论，返回id")
                return item['id']
        Log.LogOutput(LogLevel.WARN, "未找到符合条件的评论，返回None")
        return None
    except Exception:
        Log.LogOutput(LogLevel.WARN, '通过评论内容查找ID过程中异常')
        return None   
    '''
    @功能：检查爆料评论信息
    @para：
    informationId: 爆料id信息
    checkCommentInCluePara：请调用XsBaoLiaoPara中的checkCommentInCluePara
    @return:    检查成功返回True,否则返回False
    @author:  hongzenghui 2016-12-5
'''  
def check_comment_in_clue(informationId, checkCommentInCluePara=None, mobile = Global.XianSuoDftMobile, password = Global.XianSuoDftPassword):
    try:
        Log.LogOutput(LogLevel.INFO, "开始检查线索评论信息......")
        getCommnetDict = copy.deepcopy(XsBaoLiaoPara.getCommentInCluePara)
        getCommnetDict['informationId'] = informationId
        response = xiansuo_post(url='/api/clue/commentDubboService/findCommentsByInfoIdForPage', postdata=getCommnetDict, mobile=mobile, password = password)
#         print response.text
        responseDict = json.loads(response.text)
        if responseDict['response']['module']['records']==0:
            Log.LogOutput(LogLevel.DEBUG, "爆料评论为空")
            return False
        if findDictInDictlist(checkCommentInCluePara, responseDict['response']['module']['rows']) is True:
            Log.LogOutput(LogLevel.INFO, "爆料评论检查成功")
            return True
        else:
            Log.LogOutput(LogLevel.WARN, "爆料评论检查失败")
            return False
    except Exception:
        Log.LogOutput(LogLevel.WARN, '检查爆料评论过程中异常')
        return False
'''  
    @功能：通过我的评论，检查评论列表
    @para: myccommentlistpara：请调用XsBaoLiaoPara中的WoDeCommentListPara对象
    checkWoDeCommentPara：请调用XsBaoLiaoPara中的WoDeCommentListCheckPara对象
    @author: gaorong
    @return: 检查成功，则返回True；否则返回False
''' 

def check_comment_by_my_comment(checkWoDeCommentPara,mycommentlistpara, mobile = Global.XianSuoDftMobile, password = Global.XianSuoDftPassword):
    Log.LogOutput(LogLevel.INFO, "通过我的评论检查评论列表开始......")
    try:
        response = xiansuo_post(url='/api/clue/commentDubboService/findMyCommentsByInfoIdForPage', postdata=mycommentlistpara, mobile=mobile, password = password)
#         print response.text
        resultDict=json.loads(response.text)
        if resultDict['response']['module']['records']==0:
            Log.LogOutput(message='我的评论列表无内容显示！')
            return False
        if findDictInDictlist(checkWoDeCommentPara, resultDict['response']['module']['rows']) is True:
            Log.LogOutput(message='通过我的评论检查评论列表成功！')
            return True
        else:
            Log.LogOutput(message='通过我的评论检查评论列表失败！')
            return False
    except Exception:
        Log.LogOutput(message='通过我的评论检查评论列表过程中异常！')
        return False
    
    '''
    @功能：爆料详情删除评论
    @para：
    delCommentForCluePara: 请调用XsBaoLiaoPara中的delCommentCluePara
    @return:    成功返回True,否则返回False
    @author:  gaorong 2016-12-23
'''  
def delete_comment_for_clue(delCommentForCluePara, mobile = Global.XianSuoDftMobile, password = Global.XianSuoDftPassword):
    Log.LogOutput(LogLevel.INFO, "删除爆料评论开始.......")
    response = xiansuo_post(url='/api/clue/commentDubboService/updateCommentDelStateById', postdata=delCommentForCluePara, mobile=mobile, password = password)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "删除爆料评论成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, "删除爆料评论失败")
        return False  
    
'''
    @功能：爆料信息评论举报
    @para：
    ReportCommentCluePara: 请调用XsBaoLiaoPara中的ReportCommentCluePara 
    @return:    成功返回True,否则返回False
    @author:  gaorong 2017-07-11
'''  
def add_Comment_report(ReportCommentCluePara, mobile = Global.XianSuoDftMobile, password = Global.XianSuoDftPassword):
    Log.LogOutput(LogLevel.INFO, "新增信息评论举报开始")
    response = xiansuo_post(url='/api/clue/commentDubboService/addCommentReport', postdata=ReportCommentCluePara, mobile=mobile, password = password)
    print response.text   
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增信息评论举报成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, "新增信息评论举报失败")
        return False
 
    
    '''
    @功能：对爆料进行关注
    @para：
    addattentionCluePara: 请调用XsBaoLiaoPara中的addattentionCluePara
    @return:    成功返回True,否则返回False
    @author:  hongzenghui 2016-12-5
'''  
def add_attention_for_clue(addattentionCluePara, mobile = Global.XianSuoDftMobile, password = Global.XianSuoDftPassword):
    Log.LogOutput(LogLevel.INFO, "新增线索关注开始")
    response = xiansuo_post(url='/api/clue/concernDubboService/addConcern', postdata=addattentionCluePara, mobile=mobile, password = password)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "新增线索关注成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, "新增线索关注失败")
        return False
    
    '''  
    @功能：检查我的关注列表
    @para: myconcernlistpara：请调用XsBaoLiaoPara.WoDeConcernListPara对象
    checkMyConcernPara：请调用XsBaoLiaoPara.WoDeConcernListCheckPara
    @author: gaorong
    @return: 检查成功，则返回True；否则返回False
''' 

def check_myconcern_list(checkMyConcernPara,myconcernlistpara, mobile = Global.XianSuoDftMobile, password = Global.XianSuoDftPassword):
    Log.LogOutput(LogLevel.INFO, "检查我的关注列表开始......")
    try:
        response = xiansuo_post(url='/api/clue/concernDubboService/findConcernsByUserIdForPage', postdata=myconcernlistpara, mobile=mobile, password = password)
#         print response.text
        resultDict=json.loads(response.text)
        if resultDict['response']['module']['records']==0:
            Log.LogOutput(message='我的关注列表无内容显示！')
            return False
        arr=[]
        for item in resultDict['response']['module']['rows']:
            arr.append(item['information'])
        if findDictInDictlist(checkMyConcernPara, arr):
            Log.LogOutput(message='我的关注列表检查成功！')
            return True
        else:
            Log.LogOutput(message='我的关注列表检查失败！')
            return False
    except Exception:
        Log.LogOutput(message='我的关注列表查找异常！')
        return False


    
'''
    @功能：爆料取消关注
    @para：
    CancelConcernPara: 请调用XsBaoLiaoPara.CancelConcernPara
    @return:    成功返回True,否则返回False
    @author:  wangzhijun 2016-12-22
'''  
def cancel_Concern_for_clue(CancelConcernPara, mobile = Global.XianSuoDftMobile, password = Global.XianSuoDftPassword):
    Log.LogOutput(LogLevel.INFO, "爆料取消关注开始.......")
    response = xiansuo_post(url='/api/clue/concernDubboService/updateConcernByUserIdAndInfoId', postdata=CancelConcernPara, mobile=mobile, password = password)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "爆料取消关注成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, "爆料取消关注失败")
        return False   

    '''
    @功能：爆料新增点赞
    @para：
    addpraisePara: 请调用XsBaoLiaoPara中的addPraiseCluePara
    @return:    成功返回True,否则返回False
    @author:  gaorong 2016-12-23
'''  
def add_praise_for_clue(addpraisePara, mobile = Global.XianSuoDftMobile, password = Global.XianSuoDftPassword):
    Log.LogOutput(LogLevel.INFO, "爆料新增点赞开始.......")
    response = xiansuo_post(url='/api/clue/praiseDubboService/addPraise', postdata=addpraisePara, mobile=mobile, password = password)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "爆料新增点赞成功")
        return True
    else:
        Log.LogOutput(LogLevel.ERROR, "爆料新增点赞失败")
        return False 
     
'''
    @功能：在爆料详情界面查看点赞状态
    @para：
    checkPara: 请调用XsBaoLiaoPara中的ViewPraisellistPara
  getPraiseuserlistPara: 请调用XsBaoLiaoPara中的getPraiseuserlistPara
    @return:    成功返回True,否则返回False
    @author:  gaorong 2016-12-27
'''  
def check_praise_in_clue(checkPara,clueDetail):
    Log.LogOutput(LogLevel.INFO, "爆料详情界面检查开始......")
    try:
        response = xiansuo_get(url='/api/clue/praiseDubboService/findPraisesByUserIdForPage', param=clueDetail)
        responseDict = json.loads(response.text)
#         print response.text
        listDict= responseDict['response']['module']['casualTalk']
        if findDictInDictlist(checkPara, [listDict]) is True:
            Log.LogOutput(LogLevel.DEBUG, "爆料详情页面检查成功")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "爆料详情页面检查失败")
            return False
    except Exception:
        Log.LogOutput(LogLevel.ERROR, "爆料详情界面检查过程异常")
        return False
    
    
'''
    @功能：检查精彩推荐信息
    @para：
    checkHighLightPara：精彩推荐信息，请调用XsBaoLiaoPara中的checkHighLightPara
    @return:    检查成功返回True,否则返回False
    @author:  hongzenghui 2016-12-13
'''   
   
def check_highlight_info(checkHighLightPara):
    Log.LogOutput(LogLevel.INFO, "检查精彩推荐信息开始......")
    try:
        getListDict = copy.deepcopy(XsBaoLiaoPara.getHighLightPara)
        response = xiansuo_get(url='/api/clue/informationDubboService/findWonderfulRecommendList', param=getListDict)
        responseDict = json.loads(response.text)
        if findDictInDictlist(checkHighLightPara, responseDict['response']['module']) is True:
            Log.LogOutput(LogLevel.INFO, "精彩推荐检查成功")
            return True
        else:
            Log.LogOutput(LogLevel.WARN, "精彩推荐检查失败")
            return False
    except Exception:
        Log.LogOutput(LogLevel.WARN, "精彩推荐检查过程失败")
        return False
    
'''  
    @功能： 根据内容获取线索parentInforId
    @para:  contentText
    @return: 异常返回-2，没找到返回-1 正常返回次数
    @author: chenhui 2017-1-3 
'''  
def get_clue_parentInforId_by_content(contentText,username=InitDefaultPara.userInit['DftQuUser'],password='11111111'):
    Log.LogOutput(LogLevel.INFO, "开始根据内容获取线索parentInforId...")
    listpara={
            'searchInfoVo.information.orgId':InitDefaultPara.clueOrgInit['DftQuOrgId'],
            'searchInfoVo.information.infoType':InfoType.CLUE,
            '_search':'false',
            'rows':20,
            'page':1,
            'sidx':'id',
            'sord':'desc'              
              }
    response = pinganjianshe_post(url='/clueManage/clueInformationManage/findClueInformationPageBySearchsInfoVo.action', postdata=listpara,username=username, password = password)
    resDict=json.loads(response.text)
    if resDict['records']==0:
        Log.LogOutput(LogLevel.INFO, "根据内容获取线索parentInforId异常")
        return -2
    for item in resDict['rows']:
        if item['information']['contentText']==contentText:
            Log.LogOutput(LogLevel.INFO, "根据内容获取线索parentInforId成功")
            return item['information']['parentInforId']
    Log.LogOutput(LogLevel.INFO, "根据内容获取线索parentInforId失败")        
    return -1
    
'''
    @功能：爆料重新提交
    @para：XsBaoLiaoPara.ChongXinTiJiao
    @return:    成功返回True,否则返回False
    @author:  chenhui 2017-1-3
'''  
def resubmit_clue(para, mobile = Global.XianSuoDftMobile, password = Global.XianSuoDftPassword):
    Log.LogOutput(LogLevel.INFO, "爆料重新提交开始.......")
    response = xiansuo_post(url='/api/clue/informationDubboService/reSubmitInformation', postdata=para, mobile=mobile, password = password)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "爆料重新提交成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "爆料重新提交失败")
        
    return response     
       
'''
    @功能：根据内容查询信息列表
    @para：XsBaoLiaoPara.searchCluePara
    @return:    成功返回True,否则返回False
    @author:  chenhui 2017-1-3
'''  
def search_clue_by_content(para, mobile = Global.XianSuoDftMobile, password = Global.XianSuoDftPassword):
    Log.LogOutput(LogLevel.INFO, "根据内容查询信息列表开始.......")
    response = xiansuo_post(url='/api/clue/informationDubboService/searchInformationsForPageForMobile', postdata=para, mobile=mobile, password = password)
#     print response.text
    if response.result is True:
        Log.LogOutput(LogLevel.INFO, "根据内容查询信息列表成功")
    else:
        Log.LogOutput(LogLevel.ERROR, "根据内容查询信息列表失败")
    return response

'''  
    @功能： 检查数据是否存在于搜索结果中
    @para: 
        listpara:    XsBaoLiaoPara.searchCluePara
        checkpara：    XsBaoLiaoPara.jianchaxiansuo
    @return: 如果检查成功，则返回True；否则返回False
    @author: chenhui 2017-1-3  
'''  
def check_clue_in_search_list(listpara,checkpara):
    try:
        Log.LogOutput(LogLevel.INFO, "检查爆料搜索结果中是否存在")
        response = search_clue_by_content(para=listpara)
        responseDict = json.loads(response.text)
        if responseDict['response']['module']['records']==0:
            Log.LogOutput(LogLevel.DEBUG, "搜索结果列表为空")
            return False
        listDict= responseDict['response']['module']['rows']
        #定义一个空列表
        newList=[]
        #重新组装待检查列表
        for item in listDict:
            newList.append(item['information'])
        #调用检查列表参数
        if findDictInDictlist(checkpara, newList) is True:
            Log.LogOutput(LogLevel.DEBUG, "在搜索结果查看到对应爆料")
            return True
        else:
            Log.LogOutput(LogLevel.DEBUG, "无法在搜索结果查看到对应爆料")
            return False
    except Exception:
            Log.LogOutput(LogLevel.ERROR, '检查过程中出现异常')
            return False
        
'''
    @功能： 删除所有评论信息
    @author:  chenhui 2017-1-11
'''    
def delete_all_comments_by_mobile(mobile=Global.XianSuoDftMobile):
    try:
        Log.LogOutput(message='删除所有评论信息')
        ShiJianChuLiIntf.exeDbQuery(dbCommand="delete from COMMENTS p where p.commentuserid in (select id from users u where u.mobile = '%s')"%mobile\
                                    ,dbUser=Global.XianSuoYunWeiInfo['DbUser'],dbPass=Global.XianSuoYunWeiInfo['DbPass'])
    except Exception:
        raise '删除评论出错！'
