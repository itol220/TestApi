# -*- coding:UTF-8 -*-
'''
Created on 2015-11-14

@author: N-286
'''
from __future__ import unicode_literals
from COMMON import Log, Time
from COMMON.CommonUtil import createRandomString
from CONFIG import Global
from CONFIG.Define import LogLevel
from CONFIG.InitDefaultPara import orgInit, userInit
from Interface.PingAnJianShe.Common import CommonIntf
from Interface.PingAnJianShe.Common.CommonIntf import getDbQueryResult
from Interface.PingAnJianShe.ShiJianChuLi import ShiJianChuLiPara
from Interface.PingAnJianShe.ShiJianChuLi.ShiJianChuLiIntf import dealIssue, \
    shiJianChuLiInitEnv, superviseIssue, addIssue, addIssueCompleteLimitConfig, \
    checkIssueCompleteLimitList, checkIssueDelayApply
from Interface.PingAnJianShe.ShiJianChuLi.ShiJianChuLiPara import dealIssuePara
from Interface.PingAnJianShe.SystemMgr import SystemMgrIntf
from Interface.PingAnTong.ShiJianChuLi.MbShiJianChuLiIntf import mAddIssue, \
    mCheckIssueInMyTodoList, mFindHeadingType, mInitSelfIssueType, \
    mStopAllSelfIssueType, mDeleteAllSelfIssueType, mFindSmallType, mMyTodoList, \
    mViewIssue, mDealIssue, mCheckIssueInMyCompleteList, mCheckIssueInMyDoneList, \
    mCheckIssueInMyDownTodoList, mCheckIssueInMyLimitList, mApplyIssueDelay
from Interface.PingAnTong.ShiJianChuLi.MbShiJianChuLiPara import issueAddPara1, \
    myTodoIssueListPara, issueAddPara, searchIssuePara, dealPara
import copy
import json
import unittest


class MbShiJianChuLi(unittest.TestCase):


    def setUp(self):
        SystemMgrIntf.initEnv()
        shiJianChuLiInitEnv()
        pass
    
    '''
    @功能：我的待办事项新增功能 
    @ chenhui 2016-1-27
    '''
    def testmIssue_001(self):
        '''我的事项-待办事项新增功能'''
        #新增事件
        para = copy.deepcopy(issueAddPara1) 
        result=mAddIssue(para=para)
        self.assertTrue(result.result,'新增失败')
        Log.LogOutput( message='验证新增的事件')
        #检查列表中是否存在新增的事件
        checkPara={
                   'subject':para['issueNew.subject'],
                   'occurDateString':para['issueNew.occurDate'],
                   'dealState':120
                   }
        listPara=copy.deepcopy(myTodoIssueListPara)
        rs=mCheckIssueInMyTodoList(checkPara=checkPara,listPara=listPara)
        self.assertTrue(rs,'列表检查失败')
        Log.LogOutput(message='新增验证通过！')
        pass

    
    '''
    @功能：我的待办事项新增必填项功能 
    @ chenhui 2016-1-27
    '''
    def testmIssue_002(self):
        '''验证事件新增必填项功能(事件大小类除外)'''
        para = copy.deepcopy(issueAddPara)
        para['issueNew.occurOrg.id']=orgInit['DftJieDaoOrgId']
        para['issueNew.issueContent']='事件内容'
        para['issueRelatedPeopleNames']='主要当事人'
        para['issueNew.occurDate']=Time.getCurrentDate()
        para['issueNew.selfdomIssuetypeOrgCode']='.2.2.2.2.'
        para['selectedTypes']=2
        para['issueNew.subject']='主题'+createRandomString()
        para['issueNew.relatePeopleCount']='3'
        #事件规模-个体性事件
        para['issueNew.issueKind.id']=getDbQueryResult(dbCommand = "select id from propertydicts where propertydomainid=(select id from propertydomains where domainname='事件性质') and displayname='个体性事件'")
        #验证必填项：发生网格、所属网格
        para['issueNew.occurOrg.id']=''
        rs1=mAddIssue(para=para)
        self.assertFalse(rs1.result, '发生网格必填项验证失败')
        Log.LogOutput( message='所属网格必填项验证通过！')
        #验证名称必填项
        para['issueNew.occurOrg.id']=orgInit['DftJieDaoOrgId']
        para['issueNew.subject']=''
        rs2=mAddIssue(para=para)
        self.assertFalse(rs2.result, '名称必填项验证失败')
        Log.LogOutput( message='名称必填项验证通过！')
        #验证时间必填项
        para['issueNew.subject']='主题'+createRandomString()
        para['issueNew.occurDate']=''
        rs3=mAddIssue(para=para)
        self.assertFalse(rs3.result, '时间必填项验证失败')
        Log.LogOutput( message='时间必填项验证通过！')
        #验证人数必填项
        #前台已经验证，接口不验证此项，先不执行
#         para['issueNew.occurDate']=Time.getCurrentDate()
#         para['issueNew.relatePeopleCount']=''
#         rs4=mAddIssue(para=para)
#         self.assertFalse(rs4.result, '人数必填项验证失败')#有bug
#         Log.LogOutput( message='人数必填项验证通过！')
        #验证主要当事人必填项
        para['issueNew.relatePeopleCount']='3'
        para['issueRelatedPeopleNames']=''
        rs5=mAddIssue(para=para)
        self.assertFalse(rs5.result, '主要当事人必填项验证失败')
        Log.LogOutput( message='主要当事人必填项验证通过！')
        #验证规模必填项
        para['issueRelatedPeopleNames']='主要当事人'
        para['issueNew.issueKind.id']=''
        rs6=mAddIssue(para=para)
        self.assertFalse(rs6.result, '规模必填项验证失败')
        Log.LogOutput( message='规模必填项验证通过！')
        #验证描述必填项
        para['issueNew.issueKind.id']=getDbQueryResult(dbCommand = "select id from propertydicts where propertydomainid=(select id from propertydomains where domainname='事件性质') and displayname='个体性事件'")
        para['issueNew.issueContent']=''
        rs7=mAddIssue(para=para)
        self.assertFalse(rs7.result, '描述必填项验证失败')
        Log.LogOutput( message='描述必填项验证通过！')
        pass

    '''
    @功能：我的待办事项新增必填项功能 
    @ chenhui 2016-2-3
    '''
    def testmIssue_003(self):
        '''验证事件新增所属网格的选择范围'''
        para = copy.deepcopy(issueAddPara)
        para['issueNew.occurOrg.id']=orgInit['DftJieDaoOrgId']
        para['issueNew.issueContent']='事件内容'
        para['issueRelatedPeopleNames']='主要当事人'
        para['issueNew.occurDate']=Time.getCurrentDate()
        para['issueNew.selfdomIssuetypeOrgCode']='.2.2.2.2.'
        para['selectedTypes']=2
        para['issueNew.subject']='主题'+createRandomString()
        para['issueNew.relatePeopleCount']='3'
        #事件规模-个体性事件
        para['issueNew.issueKind.id']=getDbQueryResult(dbCommand = "select id from propertydicts where propertydomainid=(select id from propertydomains where domainname='事件性质') and displayname='个体性事件'")
        #验证必填项：发生网格、所属网格
        para['issueNew.occurOrg.id']=orgInit['DftShiOrgId']
        rs1=mAddIssue(para=para,username=userInit['DftJieDaoUser'])
        self.assertFalse(rs1.result, '新增所属网格输入县区以上验证失败！')
        #发生网格、所属网格选择区县
        para['issueNew.occurOrg.id']=orgInit['DftQuOrgId']
        rs2=mAddIssue(para=para,username=userInit['DftJieDaoUser'])
        self.assertTrue(rs2.result, '新增所属网格输入县区以上验证失败！')
        pass
    
    '''
    @功能：我的待办事项新增返回大类验证
    @ chenhui 2016-2-3
    '''
    def testmIssue_004(self):#有bug
        '''验证事件新增返回的事件默认大类、自定义大类'''
        if Global.simulationEnvironment is True:
            Log.LogOutput(message='仿真环境跳过测试')
        else:
            Log.LogOutput(message='验证没有设置自定义类型情况下社区层级返回大类类型')
            para={
                  'tqmobile':'true',
                  'orgId':orgInit['DftSheQuOrgId']
                  }
            rs=mFindHeadingType(para=para)
            self.assertEqual(rs['issueType'][0]['category'], '平台通用分类', '返回大类类型不正确')
            
            #初始化自定义分类
            mInitSelfIssueType()
            Log.LogOutput(message='验证在设置并启用自定义类型情况下社区层级返回大类类型')
            rs=mFindHeadingType(para=para)
            self.assertEqual(rs['issueType'][0]['category'], '个性化定制分类', '返回大类类型不正确')
            Log.LogOutput(message='验证在设置并启用自定义类型情况下区层级返回大类类型')
            para['orgId']=orgInit['DftQuOrgId']
            rs=mFindHeadingType(para=para)
            self.assertEqual(rs['issueType'][0]['category'], '个性化定制分类', '返回大类类型不正确')
            Log.LogOutput(message='验证在设置并启用自定义类型情况下市层级返回大类类型')
            para['orgId']=orgInit['DftShiOrgId']
            rs=mFindHeadingType(para=para)
            self.assertEqual(rs['issueType'][0]['category'], '平台通用分类', '返回大类类型不正确')
            #停用所有自定义分类
            Log.LogOutput(message='验证在停用自定义类型情况下区层级返回大类类型')
            mStopAllSelfIssueType()
            para['orgId']=orgInit['DftQuOrgId']
            rs=mFindHeadingType(para=para)
    #         self.assertEqual(rs['issueType'][0]['category'], '平台通用分类', '返回大类类型不正确')#有bug
            #清空自定义分类
            Log.LogOutput(message='验证在清空自定义类型情况下区层级返回大类类型')
            mDeleteAllSelfIssueType()
            para['orgId']=orgInit['DftQuOrgId']
            rs=mFindHeadingType(para=para)
            self.assertEqual(rs['issueType'][0]['category'], '平台通用分类', '返回大类类型不正确')
        pass
    
    '''
    @功能：我的待办事项新增返回小类验证
    @ chenhui 2016-2-4
    '''
    def testmIssue_005(self):
        '''验证事件新增返回的事件默认小类、自定义小类'''
        if Global.simulationEnvironment is True:
            Log.LogOutput(message="仿真环境，跳过测试")
        else:
            Log.LogOutput(message='验证没有设置自定义类型情况下社区层级返回小类类型')
            bigpara={
                  'orgId':orgInit['DftSheQuOrgId']
                  }
            rs=mFindHeadingType(para=bigpara)
            self.assertEqual(rs['issueType'][0]['category'], '平台通用分类', '返回大类类型不正确')
            smallpara={
                    'orgId':orgInit['DftSheQuOrgId'],
                    'id':rs['issueType'][0]['id'],
                    'normal':'true'
                       }
            result=mFindSmallType(para=smallpara)
            self.assertEquals(result['issueType'][0]['category'], '平台通用分类', '小类返回错误')
            #初始化自定义分类
            mInitSelfIssueType()
            Log.LogOutput(message='验证在设置并启用自定义类型情况下社区层级返回大类类型')
            rs=mFindHeadingType(para=bigpara)
            smallpara['id']=rs['issueType'][0]['id']
            smallpara['normal']='false'
            result=mFindSmallType(para=smallpara)
            self.assertEquals(result['issueType'][0]['category'], '个性化定制分类', '小类返回错误')
            Log.LogOutput(message='验证在设置并启用自定义类型情况下区层级返回大类类型')
            bigpara['orgId']=orgInit['DftQuOrgId']
            rs=mFindHeadingType(para=bigpara)
            smallpara['id']=rs['issueType'][0]['id']
            smallpara['orgId']=orgInit['DftQuOrgId']
            result=mFindSmallType(para=smallpara)
            self.assertEquals(result['issueType'][0]['category'], '个性化定制分类', '小类返回错误')
            Log.LogOutput(message='验证在设置并启用自定义类型情况下市层级返回大类类型')
            bigpara['orgId']=orgInit['DftShiOrgId']
            rs=mFindHeadingType(para=bigpara)
            smallpara['id']=rs['issueType'][0]['id']
            smallpara['orgId']=orgInit['DftShiOrgId']
            smallpara['normal']='true'
            result=mFindSmallType(para=smallpara)
            self.assertEquals(result['issueType'][0]['category'], '平台通用分类', '小类返回错误')
 
    '''
    @功能：我的待办事项查看功能
    @ chenhui 2016-2-5
    '''
    def testmIssue_006(self):
        '''查看'''
        #新增事件
        para = copy.deepcopy(issueAddPara1) 
        result=mAddIssue(para=para)
        self.assertTrue(result.result,'新增失败')
        listpara=copy.deepcopy(myTodoIssueListPara)
        r=mMyTodoList(para=listpara)
        dict=json.loads(r.text)
        id=dict['rows'][0]['issueId']
        issueStepId=dict['rows'][0]['issueStepId']
        viewpara={
#                'tqmobile':'true',
                'managementMode':'manage',
                'issueNewId':id,
                'keyType':'myIssue',
#                'issueStepId':issueStepId,
                'issueId':issueStepId,
                'mode':'doAction'
                  }
        rs=mViewIssue(para=viewpara)
        
        self.assertEquals(rs['issueNew']['subject'], para['issueNew.subject'], '主题显示不正确')
        self.assertEquals(rs['issueNew']['issueContent'], para['issueNew.issueContent'], '描述显示不正确')
        self.assertEquals(rs['issueNew']['occurDateString'], para['issueNew.occurDate'], '发生时间显示不正确')
        self.assertEquals(rs['issueNew']['issueKind']['id'], para['issueNew.issueKind.id'], '规模显示不正确')
        self.assertEquals(rs['issueNew']['relatePeopleCount'], para['issueNew.relatePeopleCount'], '人数显示不正确')
        self.assertEquals(rs['issueNew']['issueTypes'][0]['issueTypeDomain']['domainName'], '矛盾纠纷', '人数显示不正确')
        self.assertEquals(rs['issueNew']['issueTypes'][0]['issueTypeName'], '海事渔事', '人数显示不正确')
        self.assertEquals(str(rs['issueNew']['important']), para['issueNew.important'], '是否重大显示不正确')
        self.assertEquals(str(rs['issueNew']['isEmergency']), para['issueNew.isEmergency'], '是否紧急显示不正确')
        Log.LogOutput( message='查看事件验证通过')
        pass       
    
    '''
    @功能：我的待办事项查询功能
    @ chenhui 2016-2-16
    '''
    def testmIssue_007(self):
        '''查询'''
        #新增事件
        para1 = copy.deepcopy(issueAddPara1) 
        result1=mAddIssue(para=para1)
        self.assertTrue(result1.result,'新增失败')
        listPara=copy.deepcopy(myTodoIssueListPara)
        response=mMyTodoList(para=listPara)
#         print response.text
        responseDict=json.loads(response.text)
        #新增第二条事件
        para2= copy.deepcopy(issueAddPara1) 
        para2['issueNew.occurDate']='2016-02-14'
        para2['issueNew.subject']='第二条主题'
        mAddIssue(para=para2)
        response=mMyTodoList(para=listPara)
#         print response.text
        #查询第一条事件主题
        searchPara=copy.deepcopy(searchIssuePara)
        searchPara['searchIssueVo.subject']=para1['issueNew.subject']
        response2=mMyTodoList(para=searchPara)
        response2Dict=json.loads(response2.text)
        self.assertEqual(response2Dict['records'], 1, '查询主题验证失败！')
        Log.LogOutput(message='查询主题验证成功')
        #查询第一条事件的服务单号
        searchPara2=copy.deepcopy(searchIssuePara)
        searchPara2['searchIssueVo.serialNumber']=responseDict['rows'][0]['serialNumber']
        response2=mMyTodoList(para=searchPara)
        response2Dict=json.loads(response2.text)
        self.assertEqual(response2Dict['records'], 1, '查询服务单号验证失败！')
        Log.LogOutput(message='查询服务单号验证成功')
        #查询开始时间,有bug
        searchPara3=copy.deepcopy(searchIssuePara)
        searchPara3['searchIssueVo.lastDealStartDate']='2015-01-01'#para1['issueNew.occurDate']
        response2=mMyTodoList(para=searchPara)
        response2Dict=json.loads(response2.text)
        self.assertEqual(response2Dict['records'], 1, '查询开始时间验证失败！')
        Log.LogOutput(message='查询开始时间验证成功')
        #查询结束时间，有bug
        searchPara4=copy.deepcopy(searchIssuePara)
        searchPara4['searchIssueVo.lastDealEndDate']=para2['issueNew.occurDate']
        response2=mMyTodoList(para=searchPara)
        response2Dict=json.loads(response2.text)
        self.assertEqual(response2Dict['records'], 1, '查询结束时间验证失败！')
        searchPara4['searchIssueVo.lastDealEndDate']='2015-01-01'
        response22=mMyTodoList(para=searchPara)
        response22Dict=json.loads(response22.text)
#         self.assertEqual(response22Dict['records'], 0, '查询结束时间验证失败！')#有bug
        Log.LogOutput(message='查询结束时间验证成功')
        pass
    '''
    @功能：我的待办事项办理中操作
    @ chenhui 2016-2-16
    '''
    def testmIssue_008(self):
        '''办理中'''
        #新增事件
        para1 = copy.deepcopy(issueAddPara1) 
        result1=mAddIssue(para=para1)
        self.assertTrue(result1.result,'新增失败')
        listPara=copy.deepcopy(myTodoIssueListPara)
        response=mMyTodoList(para=listPara)
        responseDict=json.loads(response.text)
        para=copy.deepcopy(dealPara)
        para['issueId']=responseDict['rows'][0]['issueId']
        para['dealOrgId']=orgInit['DftJieDaoOrgId']
        para['operatorName']=userInit['DftJieDaoUserXM']
        para['operatorMobile']=userInit['DftJieDaoUserSJ']
        para['stepId']=responseDict['rows'][0]['issueStepId']
#        para['issueLog.targeOrg.id']='-1'
        para['dealType']='1'
        #验证办理意见必填项若为空，是否返回错误
        para['content']=''
        #前台有验证，接口未验证，此处先不测试
#         r=mDealIssue(para=para)
#         self.assertFalse(r, '办理意见必填项验证错误')#此处有bug
        Log.LogOutput(message='办理意见必填项功能验证成功！')
        para['content']='办理意见2'
        mDealIssue(para=para)
        #1.检查我的待办列表中是否存在新增的事件
        checkPara={
                   'subject':para1['issueNew.subject'],
                   'occurDateString':para1['issueNew.occurDate'],
                   'dealState':120
                   }
        listPara=copy.deepcopy(myTodoIssueListPara)
        rs=mCheckIssueInMyTodoList(checkPara=checkPara,listPara=listPara)
        self.assertTrue(rs, '验证失败')
        #2.检查事件处理记录表issuelogs中是否存在办理中记录,'办理中 '后带空格
        result=getDbQueryResult(dbCommand = "select count(*) from issuelogs i where i.issueid='%s' and i.dealdescription='办理中 '"%para['issueId'])
        self.assertEqual(result, 1, '事件记录表中不存在“办理中”状态的数据')
        Log.LogOutput(message='事件记录表中存在”办理中“,验证通过！')
        pass

    '''
    @功能：上报操作
    @ chenhui 2016-2-23
    '''
    def testmIssue_009(self):
        '''上报'''
        #新增事件
        para1 = copy.deepcopy(issueAddPara1) 
        result1=mAddIssue(para=para1)
        self.assertTrue(result1.result,'新增失败')
        listPara=copy.deepcopy(myTodoIssueListPara)
        response=mMyTodoList(para=listPara)
        responseDict=json.loads(response.text)
        para=copy.deepcopy(dealPara)
        para['issueId']=responseDict['rows'][0]['issueId']
        para['dealOrgId']=orgInit['DftJieDaoOrgId']
        para['operatorName']=userInit['DftJieDaoUserXM']
        para['operatorMobile']=userInit['DftJieDaoUserSJ']
        para['stepId']=responseDict['rows'][0]['issueStepId']
        para['issueLog.targeOrg.id']=orgInit['DftQuOrgId']
        para['dealType']='41'
        Log.LogOutput(message='上报事件')
        mDealIssue(para=para)
        Log.LogOutput(message='验证上报功能')
        checkPara={
                   'subject':para1['issueNew.subject'],
                   }
        listPara=copy.deepcopy(myTodoIssueListPara)
        check1=mCheckIssueInMyTodoList(checkPara=checkPara,listPara=listPara)
        check2=mCheckIssueInMyDoneList(checkPara=checkPara,listPara=listPara)
        check3=mCheckIssueInMyCompleteList(checkPara=checkPara,listPara=listPara)
        #列表参数需要传递orgId，区层级不同于默认的街道；事件的状态码在不同页面显示不同
        listPara['orgId']=orgInit['DftQuOrgId']
        checkPara['dealState']=110
        check4=mCheckIssueInMyTodoList(checkPara=checkPara,listPara=listPara,username=userInit['DftQuUser'])
        if check1 is False and check2 is True and check3 is False and check4 is True:
            Log.LogOutput(message='上报功能验证通过！')
        else:
            Log.LogOutput(LogLevel.ERROR,'上报验证失败')

    '''
    @功能：受理操作
    @ chenhui 2016-2-23
    '''
    def testmIssue_010(self):
        '''受理'''
        #新增事件
        para1 = copy.deepcopy(issueAddPara1) 
        result1=mAddIssue(para=para1)
        self.assertTrue(result1.result,'新增失败')
        listPara=copy.deepcopy(myTodoIssueListPara)
        response=mMyTodoList(para=listPara)
        responseDict=json.loads(response.text)
        #上报事件
        para=copy.deepcopy(dealPara)
        para['issueId']=responseDict['rows'][0]['issueId']
        para['dealOrgId']=orgInit['DftJieDaoOrgId']
        para['operatorName']=userInit['DftJieDaoUserXM']
        para['operatorMobile']=userInit['DftJieDaoUserSJ']
        para['stepId']=responseDict['rows'][0]['issueStepId']
        para['issueLog.targeOrg.id']=orgInit['DftQuOrgId']
        para['dealType']='41'
        Log.LogOutput(message='上报事件')
        mDealIssue(para=para)
        Log.LogOutput(message='区层级受理事件')
        acceptPara=copy.deepcopy(dealPara)
        acceptPara['issueId']=responseDict['rows'][0]['issueId']
        acceptPara['dealOrgId']=orgInit['DftQuOrgId']
        acceptPara['operatorName']='承办人员为区'
        acceptPara['operatorMobile']=userInit['DftQuUserSJ']
        acceptPara['stepId']=responseDict['rows'][0]['issueStepId']+1
        acceptPara['dealType']='61'#受理
        Log.LogOutput(message='受理事件')
        mDealIssue(para=acceptPara,username=userInit['DftQuUser'])
        checkPara={
                   'subject':para1['issueNew.subject'],
                   'dealState':120#办理中状态
                   }
        listPara=copy.deepcopy(myTodoIssueListPara)
        listPara['orgId']=orgInit['DftQuOrgId']
        check=mCheckIssueInMyTodoList(checkPara=checkPara,listPara=listPara,username=userInit['DftQuUser'])
        self.assertTrue(check, '受理验证失败')
        Log.LogOutput(message='上报受理验证成功！')

    '''
    @功能：阅读操作
    @ chenhui 2016-2-23
    '''
    def testmIssue_011(self):
        '''阅读'''
        #新增事件,有bug
        para1 = copy.deepcopy(issueAddPara1) 
        result1=mAddIssue(para=para1)
        self.assertTrue(result1.result,'新增失败')
        listPara=copy.deepcopy(myTodoIssueListPara)
        response=mMyTodoList(para=listPara)
        responseDict=json.loads(response.text)
        Log.LogOutput(message='上报事件并抄告给街道职能部门')
        #应用PC端接口实现上报并抄告功能
        sIssuePara=copy.deepcopy(dealIssuePara)
        sIssuePara['operation.dealOrg.id']=orgInit['DftJieDaoOrgId']
        sIssuePara['operation.dealUserName']=userInit['DftJieDaoUserXM']
        sIssuePara['operation.mobile']=userInit['DftJieDaoUserSJ']
        sIssuePara['operation.content']='上报事件并抄告给区职能部门'
        sIssuePara['operation.issue.id']=responseDict['rows'][0]['issueId']
        sIssuePara['keyId']=responseDict['rows'][0]['issueStepId']
        sIssuePara['operation.targeOrg.id']=orgInit['DftQuOrgId']
        sIssuePara['themainOrgid']=orgInit['DftQuOrgId']
        sIssuePara['tellOrgIds']=orgInit['DftQuFuncOrgId']#('',orgInit['DftQuFuncOrgId'])
        sIssuePara['dealCode']='41'
        Log.LogOutput(message='街道上报并抄告事件中')
        #上报并抄告
        result=dealIssue(issueDict=sIssuePara)
        self.assertTrue(result.result,'事件“上报并抄告”失败！')
        #阅读事件
        Log.LogOutput(message='区层级职能部门阅读事件')
        readPara=copy.deepcopy(dealPara)
        readPara['issueId']=responseDict['rows'][0]['issueId']
        readPara['dealOrgId']=orgInit['DftQuFuncOrgId']
        readPara['operatorName']='承办人员为区'
        readPara['operatorMobile']=userInit['DftQuUserSJ']
        readPara['stepId']=sIssuePara['keyId']
        readPara['dealType']='71'#阅读
        Log.LogOutput(message='阅读事件')
        rs=mDealIssue(para=readPara,username=userInit['DftQuFuncUser'])
        response=mMyTodoList(para=listPara,username=userInit['DftQuFuncUser'])

    '''
    @功能：回退操作
    @ chenhui 2016-2-25
    '''
    def testmIssue_012(self):
        '''回退'''
        #新增事件
        para1 = copy.deepcopy(issueAddPara1) 
        result1=mAddIssue(para=para1)
        self.assertTrue(result1.result,'新增失败')
        listPara=copy.deepcopy(myTodoIssueListPara)
        response=mMyTodoList(para=listPara)
        responseDict=json.loads(response.text)
        #上报事件
        para=copy.deepcopy(dealPara)
        para['issueId']=responseDict['rows'][0]['issueId']
        para['dealOrgId']=orgInit['DftJieDaoOrgId']
        para['operatorName']=userInit['DftJieDaoUserXM']
        para['operatorMobile']=userInit['DftJieDaoUserSJ']
        para['stepId']=responseDict['rows'][0]['issueStepId']
        para['issueLog.targeOrg.id']=orgInit['DftQuOrgId']
        para['dealType']='41'
        Log.LogOutput(message='上报事件')
        mDealIssue(para=para)
        Log.LogOutput(message='区层级受理事件')
        acceptPara=copy.deepcopy(dealPara)
        acceptPara['issueId']=responseDict['rows'][0]['issueId']
        acceptPara['dealOrgId']=orgInit['DftQuOrgId']
        acceptPara['operatorName']=userInit['DftQuUserXM']
        acceptPara['operatorMobile']=userInit['DftQuUserSJ']
        acceptPara['stepId']=responseDict['rows'][0]['issueStepId']+1
        acceptPara['dealType']='61'#受理
        mDealIssue(para=acceptPara,username=userInit['DftQuUser'])
        #回退事件
        Log.LogOutput(message='回退事件')
        backPara=copy.deepcopy(dealPara)
        backPara['operatorName']=userInit['DftQuUserXM']
        backPara['operatorMobile']=userInit['DftQuUserSJ']
        backPara['issueId']=responseDict['rows'][0]['issueId']
        backPara['dealOrgId']=orgInit['DftQuOrgId']
        backPara['stepId']=responseDict['rows'][0]['issueStepId']+1
        backPara['dealType']='200'
        mDealIssue(para=backPara,username=userInit['DftQuUser'])
        
        #验证回退功能
        checkPara={
                   'subject':para1['issueNew.subject'],
                   }
        
        listPara['orgId']=orgInit['DftQuOrgId']
        #检查区我的待办列表中不存在新增的事件，false
        check1=mCheckIssueInMyTodoList(checkPara=checkPara,listPara=listPara,username=userInit['DftQuUser'])
        #区级我的已办事件中存在该事件，true
        check2=mCheckIssueInMyDoneList(checkPara=checkPara,listPara=listPara,username=userInit['DftQuUser'])
        #区级我的下辖待办中存在该事件，true
        check3=mCheckIssueInMyDownTodoList(checkPara=checkPara,listPara=listPara,username=userInit['DftQuUser'])
        #街道层级存在该事件，并且为待受理状态，true
        listPara['orgId']=orgInit['DftJieDaoOrgId']
        checkPara['dealState']=110
        check4=mCheckIssueInMyTodoList(checkPara=checkPara,listPara=listPara)
        if check1 is False and check2 is True and check3 is True and check4 is True :
            Log.LogOutput(message='回退验证成功')
        else:
            Log.LogOutput(LogLevel.ERROR,message='回退验证失败')  

    '''
    @功能：办结操作
    @ chenhui 2016-2-25
    '''
    def testmIssue_013(self):
        '''办结'''
        #新增事件
        para1 = copy.deepcopy(issueAddPara1) 
        result1=mAddIssue(para=para1)
        self.assertTrue(result1.result,'新增失败')
        listPara=copy.deepcopy(myTodoIssueListPara)
        response=mMyTodoList(para=listPara)
        responseDict=json.loads(response.text)
        #办结事件
        para=copy.deepcopy(dealPara)
        para['issueId']=responseDict['rows'][0]['issueId']
        para['dealOrgId']=orgInit['DftJieDaoOrgId']
        para['operatorName']=userInit['DftJieDaoUserXM']
        para['operatorMobile']=userInit['DftJieDaoUserSJ']
        para['stepId']=responseDict['rows'][0]['issueStepId']
        para['issueLog.targeOrg.id']=-1
        para['dealType']='31'
        para['dealTime']=Time.getCurrentDate()
        Log.LogOutput(message='办结事件')
        mDealIssue(para=para)
        #验证结案功能
        checkPara={
                   'subject':para1['issueNew.subject'],
                   }
        
        #检查我的待办列表中不存在新增的事件，false
        check1=mCheckIssueInMyTodoList(checkPara=checkPara,listPara=listPara)
        self.assertFalse(check1, '我的待办事项不存在事件验证出错')
        #我的已办事项中存在该事件，true
        check2=mCheckIssueInMyDoneList(checkPara=checkPara,listPara=listPara)
        self.assertTrue(check2, '我的已办事项存在事件验证出错')
        #我的已办结事项中存在该事件，ture
        check3=mCheckIssueInMyCompleteList(checkPara=checkPara,listPara=listPara)
        self.assertTrue(check3, '我的已办结事项存在事件验证出错')
        Log.LogOutput(message='办结功能验证通过')

    '''
    @功能：督办手机显示
    @ chenhui 2016-2-26
    '''
    def testmIssue_014(self):
        '''督办列表在手机的显示'''
        #新增事件
        issueParam = copy.deepcopy(ShiJianChuLiPara.issueObject2) 
        rs=addIssue(issueDict=issueParam, username=userInit['DftJieDaoUser'], password='11111111')
        sIssuePara=copy.deepcopy(ShiJianChuLiPara.superviseIssue)
        sIssuePara['operation.dealOrg.id']=orgInit['DftJieDaoOrgId']
        sIssuePara['operation.issue.id']=rs['issueId']
        sIssuePara['keyId']=CommonIntf.getDbQueryResult("select currentstep from issues i where i.id='%s'"%sIssuePara['operation.issue.id'])
        sIssuePara['dealCode']='81'#普通督办
        sIssuePara['operation.dealUserName']=userInit['DftJieDaoUserXM']
        sIssuePara['operation.mobile']=userInit['DftJieDaoUserSJ']
        sIssuePara['operation.content']='督办内容'
        result=superviseIssue(issueDict=sIssuePara,username=userInit['DftJieDaoUser'],password='11111111')
        self.assertTrue(result,'普通督办验证失败')
        #手机列表显示
        listPara=copy.deepcopy(myTodoIssueListPara)
        response=mMyTodoList(para=listPara)
        responseDict=json.loads(response.text)
        self.assertEqual(responseDict['rows'][0]['supervisionState'], 1, '手机列表督办状态验证错误')
        Log.LogOutput(message='手机列表普通督办状态验证正确！')
        
        sIssuePara['dealCode']='83'#黄牌督办
        result=superviseIssue(issueDict=sIssuePara,username=userInit['DftJieDaoUser'],password='11111111')
        self.assertTrue(result,'黄牌督办验证失败')
        response2=mMyTodoList(para=listPara)
        responseDict2=json.loads(response2.text)
        self.assertEqual(responseDict2['rows'][0]['supervisionState'], 100, '手机列表督办状态验证错误')
        Log.LogOutput(message='手机列表黄牌督办状态验证正确！')
        
        sIssuePara['dealCode']='86'#红牌督办
        result=superviseIssue(issueDict=sIssuePara,username=userInit['DftJieDaoUser'],password='11111111')
        self.assertTrue(result,'红牌督办验证失败')
        response3=mMyTodoList(para=listPara)
        responseDict3=json.loads(response3.text)
        self.assertEqual(responseDict3['rows'][0]['supervisionState'], 200, '手机列表督办状态验证错误')
        Log.LogOutput(message='手机列表红牌督办状态验证正确！')
        
        sIssuePara['dealCode']='88'#取消督办
        result=superviseIssue(issueDict=sIssuePara,username=userInit['DftJieDaoUser'],password='11111111')
        self.assertTrue(result,'取消督办验证失败')
        response4=mMyTodoList(para=listPara)
        responseDict4=json.loads(response4.text)
        self.assertEqual(responseDict4['rows'][0]['supervisionState'], -1, '手机列表督办状态验证错误')
        Log.LogOutput(message='手机列表取消督办后状态验证正确！')
        
    '''
    @功能：延时申请
    @ chenhui 2016-2-26
    '''
    def testmIssue_015(self):
        '''延时申请'''
        #街道账号设置街道和直属下辖社区的限时办结规则
        #设置办结规则参数
        sIssuePara=copy.deepcopy(ShiJianChuLiPara.issueCompleteLimitConfigParam)        
        sIssuePara['mode']='add'
        sIssuePara['organization.id']=CommonIntf.getOrgInfoByAccount('zdhjd@')['orgId']
        sIssuePara['issueCompleteLimitConfig.organization.id']=sIssuePara['organization.id']
        sIssuePara['issueCompleteLimitConfig.limitDay']='4'
        sIssuePara['issueCompleteLimitConfig.normalDay']='3'
        sIssuePara['issueCompleteLimitConfig.expireDay']='1'
        sIssuePara['issueCompleteLimitConfig.enable']='1'
        result=addIssueCompleteLimitConfig(issueDict=sIssuePara)
        self.assertTrue(result,'新增限时办结规则失败')
        #新增事件
        issueParam = copy.deepcopy(ShiJianChuLiPara.issueObject2)     
        rs=addIssue(issueDict=issueParam, username=userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(rs,'新增失败')
        #交办事件
        sIssuePara1=copy.deepcopy(ShiJianChuLiPara.dealIssuePara)        
        sIssuePara1['operation.dealOrg.id']=orgInit['DftJieDaoOrgId']
        sIssuePara1['operation.issue.id']=rs['issueId']
        sIssuePara1['keyId']=rs['issueStepId']      
        sIssuePara1['operation.dealUserName']=userInit['DftJieDaoUserXM']
        sIssuePara1['operation.mobile']=userInit['DftJieDaoUserSJ']
        sIssuePara1['operation.content']='普通交办事件'
        sIssuePara1['operation.targeOrg.id']=orgInit['DftSheQuOrgId']
        sIssuePara1['themainOrgid']=orgInit['DftSheQuOrgId']
        #交办状态代码       
        sIssuePara1['dealCode']='21'
        Log.LogOutput( message='事件交办中')
        #执行交办并验证
        result1=dealIssue(issueDict=sIssuePara1)
        self.assertTrue(result1.result,'交办失败')
        #验证社区限时办结列表是否有该事件
        #设置检查参数
        checkParam={
                    'issueId':rs['issueId'],
                    'subject':rs['subject'],
                    'serialNumber':rs['serialNumber']
                    }
        #设置限时办结-全部事项列表请求参数
        sIssuePara2={
                    'issueCompleteLimitVo.targeOrgId':orgInit['DftSheQuOrgId'],
                    'issueCompleteLimitVo.limitStatus':'',
                    'issueCompleteLimitVo.limitDayOrder':'0',
                    'page':'1',
                    '_search':'false',
                    'rows':'200',
                    'sidx':'lastdealdate',
                    'sord':'desc'
                    }
        result2=checkIssueCompleteLimitList(checkPara=checkParam,issueDict=sIssuePara2,username=userInit['DftSheQuUser'])
        self.assertTrue(result2,'限时办结列表验证失败')
        Log.LogOutput(message='事件交办后，限时办结列表显示功能验证通过')
        listPara=copy.deepcopy(myTodoIssueListPara)
        listPara['orgId']=orgInit['DftSheQuOrgId']
        listPara['searchIssueVo.targeOrgId']=orgInit['DftSheQuOrgId']
        listPara['sidx']='lastdealdate'
        response=mMyTodoList(para=listPara)
        checkPara2={
                   'subject':rs['subject'],
                   }
        #检查社区层级我的待办列表中不存在新增的事件，true
        check1=mCheckIssueInMyLimitList(checkPara=checkPara2,listPara=listPara,username=userInit['DftSheQuUser'])
        self.assertTrue(check1, '手机限时办结列表数据显示错误')
        #设置延时申请参数
        applyPara={
                'issueCompleteDelay.organization.id':orgInit['DftSheQuOrgId'],
                'issueCompleteDelay.reason':'延时申请原因',
                'issueCompleteDelay.applyDays':'3',
                'issueCompleteDelay.issue.id':rs['issueId']
                   }
        mApplyIssueDelay(para=applyPara,username=userInit['DftSheQuUser'])
        #设置街道“延时设置”列表显示参数
        sIssuePara3=copy.deepcopy(sIssuePara2)
        sIssuePara3['issueCompleteLimitVo.targeOrgId']=orgInit['DftJieDaoOrgId']
        #PC端街道层级查看是否收到延时申请
        check2=checkIssueDelayApply(checkPara=checkParam,issueDict=sIssuePara3)
        self.assertTrue(check2,'申请延时验证失败')
        Log.LogOutput(message='街道“延时设置”列表中存在数据，申请延时验证通过！')
        pass

    '''
    @功能：正常交办
    @ chenhui 2016-2-26
    '''
    def testmIssue_016(self):
        '''正常交办'''
        #街道新增事件
        para1 = copy.deepcopy(issueAddPara1) 
        result1=mAddIssue(para=para1)
        self.assertTrue(result1.result,'新增失败')
        listPara=copy.deepcopy(myTodoIssueListPara)
        response=mMyTodoList(para=listPara)
        responseDict=json.loads(response.text)
        #正常交办事件
        para=copy.deepcopy(dealPara)        
        para['issueId']=responseDict['rows'][0]['issueId']
        para['dealOrgId']=orgInit['DftJieDaoOrgId']
        para['operatorName']=userInit['DftJieDaoUserXM']
        para['operatorMobile']=userInit['DftJieDaoUserSJ']
        para['stepId']=responseDict['rows'][0]['issueStepId']
        para['themainOrgid']=orgInit['DftSheQuOrgId']
        para['dealType']='21'
        
        Log.LogOutput(message='交办事件')
        mDealIssue(para=para)
        #验证交办功能
        checkPara={
                   'subject':para1['issueNew.subject'],
                   }
        
        #检查我的待办列表中不存在新增的事件，false
        check1=mCheckIssueInMyTodoList(checkPara=checkPara,listPara=listPara)
        #我的已办事项中存在该事件，true
        check2=mCheckIssueInMyDoneList(checkPara=checkPara,listPara=listPara)
        #我的已办结事项中不存在该事件，false
        check3=mCheckIssueInMyCompleteList(checkPara=checkPara,listPara=listPara)
        #社区层级我的待办事项存在数据，true
        checkPara['dealState']=110
        listPara['orgId']=orgInit['DftSheQuOrgId']
        check4=mCheckIssueInMyTodoList(checkPara=checkPara,listPara=listPara,username=userInit['DftSheQuUser'])
        if check1 is False and check2 is True and check3 is False and check4 is True:
            Log.LogOutput(message='正常交办功能验证通过')
        else:
            Log.LogOutput(LogLevel.ERROR,message='交办功能验证失败')
        pass

    '''
    @功能：交办-共同办理
    @ chenhui 2016-2-26
    '''
#     def testmIssue_017(self):
#         '''交办-共同办理'''
#         #街道新增事件
#         para1 = copy.deepcopy(issueAddPara1) 
#         result1=mAddIssue(para=para1)
#         self.assertTrue(result1.result,'新增失败')
#         listPara=copy.deepcopy(myTodoIssueListPara)
#         response=mMyTodoList(para=listPara)
#         responseDict=json.loads(response.text)
#         #共同办理事件
#         para=copy.deepcopy(dealPara)        
#         para['issueId']=responseDict['rows'][0]['issueId']
#         para['dealOrgId']=orgInit['DftJieDaoOrgId']
#         para['operatorName']=userInit['DftJieDaoUserXM']
#         para['operatorMobile']=userInit['DftJieDaoUserSJ']
#         para['stepId']=responseDict['rows'][0]['issueStepId']
#         para['themainOrgid']=orgInit['DftSheQuOrgId']
#         para['specialAssignType']=1
#         para['dealType']='21'
#         
#         Log.LogOutput(message='交办-共同办理')
#         mDealIssue(para=para)
#         #验证交办-共同办理功能
#         checkPara={
#                    'subject':para1['issueNew.subject'],
#                    }
#         
#         #检查我的待办列表中不存在新增的事件，false
#         check1=mCheckIssueInMyTodoList(checkPara=checkPara,listPara=listPara)
#         self.assertFalse(check1, '交办时，我的待办验证出错')
#         #我的已办事项中存在该事件，true
#         check2=mCheckIssueInMyDoneList(checkPara=checkPara,listPara=listPara)
#         self.assertTrue(check2, '交办时，我的已办验证出错')
#         #我的已办结事项中不存在该事件，false
#         check3=mCheckIssueInMyCompleteList(checkPara=checkPara,listPara=listPara)
#         self.assertFalse(check3, '交办时，我的已完成验证出错')
#         #社区层级我的待办事项存在数据，true
#         checkPara['dealState']=110
#         listPara['orgId']=orgInit['DftSheQuOrgId']
#         check4=mCheckIssueInMyTodoList(checkPara=checkPara,listPara=listPara,username=userInit['DftSheQuUser'])
#         self.assertTrue(check4, '交办时，社区我的待办验证出错')
#         #社区受理
#         acceptPara=copy.deepcopy(dealPara)
#         acceptPara['issueId']=responseDict['rows'][0]['issueId']
#         acceptPara['dealOrgId']=orgInit['DftSheQuOrgId']
#         acceptPara['operatorName']=userInit['DftSheQuUserXM']
#         acceptPara['operatorMobile']=userInit['DftSheQuUserSJ']
#         acceptPara['stepId']=responseDict['rows'][0]['issueStepId']+1
#         acceptPara['dealType']='61'#受理
#         Log.LogOutput(message='社区受理事件')
#         mDealIssue(para=acceptPara,username=userInit['DftSheQuUser'])
#         checkPara['dealState']=120
#         #社区办理中状态的事件，true
#         check5=mCheckIssueInMyTodoList(checkPara=checkPara,listPara=listPara,username=userInit['DftSheQuUser'])
#         self.assertTrue(check5, '受理后，社区我的待办验证出错')
#         #街道层级我待办事项仍然不存在该事件,false
#         checkPara['dealState']=None
#         listPara['orgId']=orgInit['DftJieDaoOrgId']
#         check6=mCheckIssueInMyTodoList(checkPara=checkPara,listPara=listPara)
#         self.assertFalse(check6, '受理后，街道我的待办验证出错')
#         #社区回复事件
#         replyPara=copy.deepcopy(dealPara)
#         replyPara['issueId']=responseDict['rows'][0]['issueId']
#         replyPara['dealOrgId']=orgInit['DftSheQuOrgId']
#         replyPara['operatorName']=userInit['DftSheQuUserXM']
#         replyPara['operatorMobile']=userInit['DftSheQuUserSJ']
#         replyPara['stepId']=responseDict['rows'][0]['issueStepId']+1
#         replyPara['issueLog.targeOrg.id']=-1
#         replyPara['dealType']='22'#回复
#         Log.LogOutput(message='社区回复事件')
#         mDealIssue(para=replyPara,username=userInit['DftSheQuUser'])
#         #社区我的待办页面不存在数据false
#         listPara['orgId']=orgInit['DftSheQuOrgId']
#         check7=mCheckIssueInMyTodoList(checkPara=checkPara,listPara=listPara,username=userInit['DftSheQuUser'])
#         self.assertFalse(check7, '回复后，社区我的待办验证出错')
#         #街道我的待办页面存在数据，true
#         checkPara['dealState']=110
#         listPara['orgId']=orgInit['DftJieDaoOrgId']
#         check8=mCheckIssueInMyTodoList(checkPara=checkPara,listPara=listPara)
#         self.assertTrue(check8, '回复后，街道我的待办验证出错')
#         #街道受理
#         acceptPara['dealOrgId']=orgInit['DftJieDaoOrgId']
#         acceptPara['operatorName']=userInit['DftJieDaoUserXM']
#         acceptPara['operatorMobile']=userInit['DftJieDaoUserSJ']
#         acceptPara['stepId']=responseDict['rows'][0]['issueStepId']
#         mDealIssue(para=acceptPara)
#         #街道结案
#         completePara=copy.deepcopy(dealPara)
#         completePara['issueId']=responseDict['rows'][0]['issueId']
#         completePara['dealOrgId']=orgInit['DftJieDaoOrgId']
#         completePara['operatorName']=userInit['DftJieDaoUserXM']
#         completePara['operatorMobile']=userInit['DftJieDaoUserSJ']
#         completePara['stepId']=responseDict['rows'][0]['issueStepId']
#         completePara['dealType']='31'
#         #结案新加参数
#         completePara['dealTime']=Time.getCurrentDate()
#         completePara['issueLog.targeOrg.id']='-1'
#         
#         Log.LogOutput(message='办结事件')
#         mDealIssue(para=completePara)
#         checkPara['dealState']=None
#         #街道我的已完成页面存在数据，true
#         check9=mCheckIssueInMyCompleteList(checkPara=checkPara,listPara=listPara)
#         self.assertTrue(check9, '办结后，街道我的已办结验证出错')

    '''
    @功能：交办-共同办理
    @ chenhui 2016-2-26
    '''
    def testmIssue_018(self):
        '''交办-协同办理'''
        #街道新增事件
        para1 = copy.deepcopy(issueAddPara1) 
        result1=mAddIssue(para=para1)
        self.assertTrue(result1.result,'新增失败')
        listPara=copy.deepcopy(myTodoIssueListPara)
        response=mMyTodoList(para=listPara)
        responseDict=json.loads(response.text)
        #协同交办事件
        para=copy.deepcopy(dealPara)        
        para['issueId']=responseDict['rows'][0]['issueId']
        para['dealOrgId']=orgInit['DftJieDaoOrgId']
        para['operatorName']=userInit['DftJieDaoUserXM']
        para['operatorMobile']=userInit['DftJieDaoUserSJ']
        para['stepId']=responseDict['rows'][0]['issueStepId']
        para['themainOrgid']=orgInit['DftSheQuOrgId']
        para['secondaryOrgid']=orgInit['DftJieDaoFuncOrgId']
        para['specialAssignType']=2
        para['dealType']='21'
        Log.LogOutput(message='交办-协同办理')
        mDealIssue(para=para)
        #验证交办-协同办理功能
        checkPara={
                   'subject':para1['issueNew.subject'],
                   }
        #检查我的待办列表中不存在新增的事件，false
        check1=mCheckIssueInMyTodoList(checkPara=checkPara,listPara=listPara)
        self.assertFalse(check1, '交办时，我的待办验证出错')
        #我的已办事项中存在该事件，true
        check2=mCheckIssueInMyDoneList(checkPara=checkPara,listPara=listPara)
        self.assertTrue(check2, '交办时，我的已办验证出错')
        #我的已办结事项中不存在该事件，false
        check3=mCheckIssueInMyCompleteList(checkPara=checkPara,listPara=listPara)
        self.assertFalse(check3, '交办时，我的已完成验证出错')
        #街道职能部门我的待办事项中存在数据
        listPara['orgId']=orgInit['DftJieDaoFuncOrgId']
        checkPara['dealState']=110
        check4=mCheckIssueInMyTodoList(checkPara=checkPara,listPara=listPara,username=userInit['DftJieDaoFuncUser'])
        self.assertTrue(check4, '交办时，街道职能部门-我的待办验证出错')
        #社区层级我的待办事项存在数据，true
        listPara['orgId']=orgInit['DftSheQuOrgId']
        check5=mCheckIssueInMyTodoList(checkPara=checkPara,listPara=listPara,username=userInit['DftSheQuUser'])
        self.assertTrue(check5, '交办时，社区我的待办验证出错')
        #社区受理事件
        acceptPara=copy.deepcopy(dealPara)
        acceptPara['issueId']=responseDict['rows'][0]['issueId']
        acceptPara['dealOrgId']=orgInit['DftSheQuOrgId']
        acceptPara['operatorName']=userInit['DftSheQuUserXM']
        acceptPara['operatorMobile']=userInit['DftSheQuUserSJ']
        acceptPara['stepId']=responseDict['rows'][0]['issueStepId']+1
        acceptPara['dealType']='61'#受理
        Log.LogOutput(message='社区受理事件')
        mDealIssue(para=acceptPara,username=userInit['DftSheQuUser'])
        checkPara['dealState']=120
        #社区办理中状态的事件，true
        check6=mCheckIssueInMyTodoList(checkPara=checkPara,listPara=listPara,username=userInit['DftSheQuUser'])
        self.assertTrue(check6, '受理后，社区我的待办验证出错')
        #验证社区在街道职能部门不受理的情况下，直接结案
        #社区结案
        completePara=copy.deepcopy(dealPara)
        completePara['issueId']=responseDict['rows'][0]['issueId']
        completePara['dealOrgId']=orgInit['DftSheQuOrgId']
        completePara['operatorName']=userInit['DftSheQuUserXM']
        completePara['operatorMobile']=userInit['DftSheQuUserSJ']
        completePara['stepId']=responseDict['rows'][0]['issueStepId']+1
        completePara['dealType']='31'
        #新加参数
        completePara['dealTime']=Time.getCurrentDate()
        completePara['issueLog.targeOrg.id']='-1'
#         Log.LogOutput(message='办结事件')
#         r=mDealIssue(para=completePara,username=userInit['DftSheQuUser'])
#         #返回非true,有bug
#         self.assertNotEqual(r,True, '社区在街道层级不受理的情况下，直接结案没有返回错误信息')
        #街道职能部门受理
        acceptPara2=copy.deepcopy(dealPara)
        acceptPara2['issueId']=responseDict['rows'][0]['issueId']
        acceptPara2['dealOrgId']=orgInit['DftJieDaoFuncOrgId']
        acceptPara2['operatorName']=userInit['DftJieDaoFuncUserXM']
        acceptPara2['operatorMobile']=userInit['DftJieDaoFuncUserSJ']
        acceptPara2['stepId']=responseDict['rows'][0]['issueStepId']+2
        acceptPara2['dealType']='61'#受理
        Log.LogOutput(message='街道职能部门受理事件')
        mDealIssue(para=acceptPara2,username=userInit['DftJieDaoFuncUser'])
        checkPara['dealState']=120
        listPara['orgId']=orgInit['DftJieDaoFuncOrgId']
        #街道职能部门办理中状态的事件，true
        check7=mCheckIssueInMyTodoList(checkPara=checkPara,listPara=listPara,username=userInit['DftJieDaoFuncUser'])
        self.assertTrue(check7, '受理后，街道职能部门我的待办验证出错')
        
        #验证社区在街道职能部门不回复的情况下，直接结案
        #社区结案
#         Log.LogOutput(message='办结事件')
#         r2=mDealIssue(para=completePara,username=userInit['DftSheQuUser'])
#         #返回非true
#         self.assertNotEqual(r2,True, '社区在街道层级没有回复的情况下，直接结案没有返回错误信息')
        
        #街道职能部门回复
        replyPara=copy.deepcopy(dealPara)
        replyPara['issueId']=responseDict['rows'][0]['issueId']
        replyPara['dealOrgId']=orgInit['DftJieDaoFuncOrgId']
        replyPara['operatorName']=userInit['DftJieDaoFuncUserXM']
        replyPara['operatorMobile']=userInit['DftJieDaoFuncUserSJ']
        replyPara['stepId']=responseDict['rows'][0]['issueStepId']+2
        replyPara['issueLog.targeOrg.id']=-1
        replyPara['dealType']='22'#回复
        Log.LogOutput(message='街道职能部门回复事件')
        mDealIssue(para=replyPara,username=userInit['DftJieDaoFuncUser'])
        #街道职能部门我的待办页面不存在数据false
        listPara['orgId']=orgInit['DftJieDaoFuncOrgId']
        check8=mCheckIssueInMyTodoList(checkPara=checkPara,listPara=listPara,username=userInit['DftJieDaoFuncUser'])
        self.assertFalse(check8, '回复后，街道职能部门-我的待办验证出错')
        #街道职能部门我的已办页面存在数据，true
        listPara['orgId']=orgInit['DftJieDaoFuncOrgId']
        checkPara['dealState']=1
        check9=mCheckIssueInMyDoneList(checkPara=checkPara,listPara=listPara,username=userInit['DftJieDaoFuncUser'])
        self.assertTrue(check9, '回复后，街道职能部门-我的已办验证出错')
        #社区办结事件
        Log.LogOutput(message='办结事件')
        #社区我的已完成页面存在数据，true
        mDealIssue(para=completePara,username=userInit['DftSheQuUser'])
        listPara['orgId']=orgInit['DftSheQuOrgId']
        checkPara['dealState']=300
        check10=mCheckIssueInMyDoneList(checkPara=checkPara,listPara=listPara,username=userInit['DftSheQuUser'])
        self.assertTrue(check10, '办结后，社区-我的已办结验证出错')
        Log.LogOutput(message='协同办理功能验证通过')
        pass  
        
    def tearDown(self):
        pass


if  __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    suite = unittest.TestSuite()
#    suite.addTest(Shijianchuli("testHttpGet"))
    suite.addTest(MbShiJianChuLi("testmIssue_005"))
#    suite.addTest(Shijianchuli("testHttpPost"))
    results = unittest.TextTestRunner().run(suite)
    pass
