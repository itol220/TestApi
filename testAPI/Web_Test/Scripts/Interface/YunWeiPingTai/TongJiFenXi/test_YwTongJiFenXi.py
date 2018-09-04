# -*- coding:UTF-8 -*-
'''
Created on 2016-4-12

@author: N-286
'''
from __future__ import unicode_literals
from COMMON import Log
from COMMON.Time import getCurrentDateAndTime
from CONFIG.Global import simulationEnvironment
from CONFIG.InitDefaultPara import orgInit, userInit
from Interface.PingAnJianShe.ShiJianChuLi import ShiJianChuLiPara
from Interface.PingAnJianShe.ShiJianChuLi.ShiJianChuLiIntf import dealIssue, \
    deleteAllIssues2
from Interface.XianSuoApp.BaoLiao.XsBaoLiaoIntf import addXianSuo, \
    deleteAllClues, viewSchedule
from Interface.XianSuoApp.BaoLiao.XsBaoLiaoPara import xinZeng2
from Interface.XianSuoApp.XinXiGuangChang import XsInformationSquareIntf
from Interface.XianSuoApp.XinXiGuangChang.XsInformationSquarePara import \
    culeToIssuePara
from Interface.YunWeiPingTai.TongJiFenXi.TongJiFenXiIntf import doJob, \
    getStaticAnalysisList, addScoreToClue
from Interface.YunWeiPingTai.TongJiFenXi.TongJiFenXiPara import TongJiLieBiao
from Interface.YunWeiPingTai.YunWeiCommon.YunWeiCommonIntf import \
    clearTableYunWei, setLinuxTimeYunWei, getLinuxDateAndTimeYunWei
import copy
import json
import unittest

class YwStaticAnalysis(unittest.TestCase):
    #仿真环境不可用,加判断防止误操作
    def setUp(self):
        if simulationEnvironment is False:
            #清空历史月份统计表
            clearTableYunWei(tableName='informationstatisticshistory')
            deleteAllClues()
            deleteAllIssues2()
        pass
    
    def test_YwStaticAnalysis_01(self):
        '''线索信息统计'''
        #仿真环境下跳过测试
        if simulationEnvironment is True:
            pass
        else:
            #修改系统时间
            try:
                #1月份新增存量数据
                setLinuxTimeYunWei(data='2016-1-26 18:18:18')
                #6月份为“当前月”数据
                para={'yearMonth':'2016-06'}
                doJob(para=para)
                listPara=copy.deepcopy(TongJiLieBiao)
                listPara['informationStatistics.yearMonth']='2016-06'
                reserveSum1=getStaticAnalysisList(para=listPara)['rows'][0]['reserveSum']
#                 print reserveSum1
                self.assertEquals(reserveSum1, 0, '初始存量统计数据错误')
                #新增一条线索
                addPara=copy.deepcopy(xinZeng2)
                addXianSuo(addPara)
                
                #再次新增一条线索，并办结，不应纳入存量
                addXianSuo(addPara)
                clueListPara={
                    'tqmobile':'true',
                    'page':'1',
                    'rows':'100'
                      }
                #转事件参数
                addIssuePara=copy.deepcopy(culeToIssuePara)
                #办结事件参数
                issuePara=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)
                issuePara['operation.dealOrg.id']=orgInit['DftJieDaoOrgId']
                issuePara['operation.dealUserName']=userInit['DftJieDaoUserXM']
                issuePara['operation.mobile']=userInit['DftJieDaoUserSJ']
                issuePara['operation.content']='结案'       
                issuePara['dealCode']='31'
                lsrDict=json.loads(viewSchedule(para=clueListPara).text)
                addIssuePara['issue.occurDate']='2016-1-25'
                addIssuePara['information.id']=lsrDict['response']['module']['rows'][0]['information']['id']
                addIssuePara['information.nickName']=lsrDict['response']['module']['rows'][0]['information']['nickName']
                addIssuePara['issue.occurLocation']=lsrDict['response']['module']['rows'][0]['information']['address']
                addIssuePara['issue.issueContent']=lsrDict['response']['module']['rows'][0]['information']['contentText']
                #转事件
                addIssuePara['issue.occurDate']=getLinuxDateAndTimeYunWei()
#                print addIssuePara['issue.occurDate']
                isRes=XsInformationSquareIntf.clueToIssue(para=addIssuePara)
                isResDict=json.loads(isRes.text)
                issuePara['operation.issue.id']=isResDict['issueId']
                issuePara['keyId']=isResDict['issueStepId']
                #办结
                result=dealIssue(issueDict=issuePara)
                self.assertTrue(result.result, '办结失败')
                #运行job并统计存量，应为1而不是2
                doJob(para=para)
                reserveSum2=getStaticAnalysisList(para=listPara)['rows'][0]['reserveSum']
                self.assertEquals(reserveSum2, reserveSum1+1, '存量统计错误')
                #将时间改成6月份，测试当月统计数据是否正确
                setLinuxTimeYunWei(data='2016-6-26 18:18:18')
                
                monthAdd1=getStaticAnalysisList(para=listPara)['rows'][0]['monthAdd']
                self.assertEquals(monthAdd1, 0, '本月新增统计初始数据错误')
                #本页新增一条线索并执行统计job
                addXianSuo(addPara)        
                #运行统计job
                doJob(para=para)
                monthAdd2=getStaticAnalysisList(para=listPara)['rows'][0]['monthAdd']
                self.assertEquals(monthAdd1+1, monthAdd2, '本月新增统计错误')
                #再连续新增8条线索
                #事件评分参数
                addScorePara={
                        'tqmobile':'true',
                        'publishUserId':'',
                        'id':'',
                        'score':''
                              }
                for i in range(1,9):
                    addPara=copy.deepcopy(xinZeng2)
                    addPara['information']['contentText']=addPara['information']['contentText']+str(i)
                    addXianSuo(addPara)
        #             lsrDict=json.loads(viewSchedule(para=clueListPara).text)
                    if i %2==0:#第2/4/6/8线索转事件
                        lsrDict=json.loads(viewSchedule(para=clueListPara).text)
                        addIssuePara['information.id']=lsrDict['response']['module']['rows'][0]['information']['id']
                        addIssuePara['information.nickName']=lsrDict['response']['module']['rows'][0]['information']['nickName']
                        addIssuePara['issue.occurLocation']=lsrDict['response']['module']['rows'][0]['information']['address']
                        addIssuePara['issue.issueContent']=lsrDict['response']['module']['rows'][0]['information']['contentText']
                        isRes=XsInformationSquareIntf.clueToIssue(para=addIssuePara)
                        isResDict=json.loads(isRes.text)
        #                 print i+1000000
                        if i%4!=0:#将第2/6条事件结案
                            issuePara['operation.issue.id']=isResDict['issueId']
                            issuePara['keyId']=isResDict['issueStepId']
                            result=dealIssue(issueDict=issuePara)
                            self.assertTrue(result.result, '办结失败')
                            #评分
                            addScorePara['publishUserId']=lsrDict['response']['module']['rows'][0]['information']['publishUserId']
                            addScorePara['id']=lsrDict['response']['module']['rows'][0]['information']['id']
                            addScorePara['score']=i#2,6分
                            addScoreToClue(para=addScorePara)
                doJob(para=para)
                staticDict=getStaticAnalysisList(para=listPara)['rows'][0]
                monthAdd=staticDict['monthAdd']
                reserveSum=staticDict['reserveSum']
                conversionSum=staticDict['conversionSum']
                conversionRate=staticDict['conversionRate']
                completedSum=staticDict['completedSum']
                completedRate=staticDict['completedRate']
                avgCompletedTime=staticDict['avgCompletedTime']
                avgCompletedScore=staticDict['avgCompletedScore']
                #验证统计结果
                self.assertEquals(monthAdd, 9, '本月新增统计错误')
                self.assertEqual(reserveSum, 1, '存量统计错误')
                self.assertEqual(conversionSum, 4, '转化数统计错误')
                self.assertEqual(conversionRate, 40, '转化率统计错误')
                self.assertEqual(completedSum, 2, '办结数统计错误')
                self.assertEqual(completedRate, 20, '办结率统计错误')
                self.assertEqual(avgCompletedTime, 1, '评价办结时间统计错误')
                self.assertEqual(avgCompletedScore, 4, '存量统计错误')
                Log.LogOutput(message='统计结果正确')
            
            finally:
                #将系统时间改回正确时间
                setLinuxTimeYunWei(data=getCurrentDateAndTime())
            pass
    
    def tearDown(self):
        pass    

    
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(YwStaticAnalysis("test_YwStaticAnalysis_01"))
    results = unittest.TextTestRunner().run(suite)
    pass   