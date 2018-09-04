# -*- coding:UTF-8 -*-
'''
Created on 2016-4-7

@author: lhz
'''
from __future__ import unicode_literals
import unittest
from Interface.PingAnJianShe.SystemMgr import SystemMgrIntf
import copy
from Interface.PingAnTong.DuChaAnFnag import MbDuChaAnFangPara,\
    MbDuChaAnFangIntf
from COMMON import Time, CommonUtil, Log
import random
from CONFIG import InitDefaultPara
from Interface.PingAnJianShe.Common import CommonIntf
import json
from CONFIG.Define import LogLevel
class MbDuChaAnFang(unittest.TestCase):
    def setUp(self):
        SystemMgrIntf.initEnv()
        pass

    '''
    @功能：督查暗访新增
    @ lhz  2016-4-7
    ''' 
    def teskssb_001(self):
        '''新增督查暗访信息'''
        #督查暗访信息新增
        issueParam = copy.deepcopy(MbDuChaAnFangPara.duChaAnFangAddParam)
        issueParam['secretSupervision.checkCompanyName'] = '检查单位%s' % CommonUtil.createRandomString(6) 
        issueParam['secretSupervision.mobileNumber'] = random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8))
        issueParam['secretSupervision.checkLegalPerson'] = '张三'
        issueParam['secretSupervision.checkSubject'] = '检查科目%s' % CommonUtil.createRandomString(6)
        issueParam['secretSupervision.checkAddress'] = '学院路50号'
        issueParam['secretSupervision.orgId'] = InitDefaultPara.orgInit['DftJieDaoOrgId']
        issueParam['secretSupervision.findProblems'] = '正常'
        issueParam['secretSupervision.checkTime'] = Time.getCurrentDate()
        issueParam['secretSupervision.requires'] ='荼毒'

        #验证检查单位是否为必填项
        issueParam['secretSupervision.checkCompanyName'] = ''
        ret =  MbDuChaAnFangIntf.KuaiShuShangBaoAdd(issueParam, username=InitDefaultPara.userInit['DftJieDaoUser'], password='11111111')
        self.assertFalse(ret.result, '新增督查暗访检查单位为空仍能新增，验证失败') 
        Log.LogOutput(LogLevel.DEBUG, "新增督查暗访检查单位不能为空")
        issueParam['secretSupervision.checkCompanyName'] = issueParam['secretSupervision.checkCompanyName']
        
        #验证法人代表是否为必填项
        issueParam['secretSupervision.checkLegalPerson']  = ''
        ret =  MbDuChaAnFangIntf.KuaiShuShangBaoAdd(issueParam, username=InitDefaultPara.userInit['DftJieDaoUser'], password='11111111')
        self.assertFalse(ret.result, '新增督查暗访法人代表为空仍能新增，验证失败') 
        Log.LogOutput(LogLevel.DEBUG, "新增督查暗访法人代表不能为空")
        issueParam['secretSupervision.checkLegalPerson']  = issueParam['secretSupervision.checkLegalPerson'] 
        
        #验证检查科目是否为必填项
        issueParam['secretSupervision.checkSubject']  = ''
        ret =  MbDuChaAnFangIntf.KuaiShuShangBaoAdd(issueParam, username=InitDefaultPara.userInit['DftJieDaoUser'], password='11111111')
        self.assertFalse(ret.result, '新增督查暗访检查科目为空仍能新增，验证失败') 
        Log.LogOutput(LogLevel.DEBUG, "新增督查暗访检查科目不能为空")
        issueParam['secretSupervision.checkSubject']  = issueParam['secretSupervision.checkSubject']        

 
        #验证手机号码是否为必填项
        issueParam['secretSupervision.mobileNumber'] = ''
        ret =  MbDuChaAnFangIntf.KuaiShuShangBaoAdd(issueParam, username=InitDefaultPara.userInit['DftJieDaoUser'], password='11111111')
        self.assertFalse(ret.result, '新增督查暗访手机号码为空仍能新增，验证失败') 
        Log.LogOutput(LogLevel.DEBUG, "新增督查暗访手机号码不能为空")
        issueParam['secretSupervision.mobileNumber'] =issueParam['secretSupervision.mobileNumber']
        
        #验证检查地址是否为必填项
        issueParam['secretSupervision.checkAddress'] = ''
        ret =  MbDuChaAnFangIntf.KuaiShuShangBaoAdd(issueParam, username=InitDefaultPara.userInit['DftJieDaoUser'], password='11111111')
        self.assertFalse(ret.result, '新增督查暗访检查地址为空仍能新增，验证失败') 
        Log.LogOutput(LogLevel.DEBUG, "新增督查暗访检查地址不能为空")
        issueParam['secretSupervision.checkAddress'] =issueParam['secretSupervision.checkAddress']
        
        
        #验证检查地址是否为必填项
        issueParam['secretSupervision.findProblems'] = ''
        ret =  MbDuChaAnFangIntf.KuaiShuShangBaoAdd(issueParam, username=InitDefaultPara.userInit['DftJieDaoUser'], password='11111111')
        self.assertFalse(ret.result, '新增督查暗访检查结果为空仍能新增，验证失败') 
        Log.LogOutput(LogLevel.DEBUG, "新增督查暗访检查结果不能为空")
        issueParam['secretSupervision.findProblems'] =issueParam['secretSupervision.findProblems']
        
        #验证要求是否为必填项
        issueParam['secretSupervision.requires'] = ''
        ret =  MbDuChaAnFangIntf.KuaiShuShangBaoAdd(issueParam, username=InitDefaultPara.userInit['DftJieDaoUser'], password='11111111')
        self.assertFalse(ret.result, '新增督查暗访要求为空仍能新增，验证失败') 
        Log.LogOutput(LogLevel.DEBUG, "新增督查暗访要求不能为空")
        issueParam['secretSupervision.requires']=issueParam['secretSupervision.requires']

        ret =  MbDuChaAnFangIntf.KuaiShuShangBaoAdd(issueParam, username=InitDefaultPara.userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(ret,'督查暗访新增失败')
        Time.wait(1)
        
        #检查督查暗访信息
        checkParam = copy.deepcopy(MbDuChaAnFangPara.checkDuChaAnFangParam)
        checkParam['checkCompanyName'] = issueParam['secretSupervision.checkCompanyName']
        ret =  MbDuChaAnFangIntf.check_KuaiShuShangBao(checkParam, username=InitDefaultPara.userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(ret,'督查暗访查找失败')
        Time.wait(1)
        

    def teskssb_002(self):
        '''删除督查暗访信息'''
        #督查暗访信息新增
        issueParam = copy.deepcopy(MbDuChaAnFangPara.duChaAnFangAddParam)
        issueParam['secretSupervision.checkCompanyName'] = '检查单位%s' % CommonUtil.createRandomString(6) 
        issueParam['secretSupervision.mobileNumber'] = random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8))
        issueParam['secretSupervision.checkLegalPerson'] = '张三'
        issueParam['secretSupervision.checkSubject'] = '检查科目%s' % CommonUtil.createRandomString(6)
        issueParam['secretSupervision.checkAddress'] = '学院路%s' % CommonUtil.createRandomString(6)
        issueParam['secretSupervision.orgId'] = InitDefaultPara.orgInit['DftJieDaoOrgId']
        issueParam['secretSupervision.findProblems'] = '正常'
        issueParam['secretSupervision.checkTime'] = Time.getCurrentDate()
        issueParam['secretSupervision.requires'] ='荼毒'
        ret =  MbDuChaAnFangIntf.KuaiShuShangBaoAdd(issueParam, username=InitDefaultPara.userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(ret,'督查暗访新增失败')
        Time.wait(1)
        
        #督查暗访流转到巡检的受理中心中，进行转事件处理
        issueParam2 = copy.deepcopy(MbDuChaAnFangPara.TransferEventsParam)
        #巡检id
        issueParam2['inspectionIds'] =  CommonIntf.getDbQueryResult(dbCommand="select t.id from inspection t  where t.inspectaddress ='%s'"%issueParam['secretSupervision.checkAddress'])
        issueParam2['issue.subject'] = issueParam['secretSupervision.checkCompanyName']
        issueParam2['selectedTypes'] = 1 #事件类型
        issueParam2['issueRelatedPeopleNames'] = '张三'
        issueParam2['issueRelatedPeopleTelephones'] = random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8))
        issueParam2['issue.relatePeopleCount'] = '33'
        issueParam2['issue.issueContent'] = '正常'
        ret =  MbDuChaAnFangIntf.TransferEvents(issueParam2, username=InitDefaultPara.userInit['DftJieDaoUser'], password='11111111')
        result =  json.loads(ret.text)
        self.assertTrue(ret.result,'督查暗访受理中心转事件失败')
        Time.wait(1)
        
        #事件处理 进行结案
        closeParam = copy.deepcopy(MbDuChaAnFangPara.issueDealParam)
        closeParam['operation.issue.id'] = result['issueId']
        closeParam['keyId'] = result['issueStepId']
        closeParam['operation.mobile'] = random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8))
        closeParam['dealCode'] = 31
        closeParam['operation.content'] = '内容'
        ret =  MbDuChaAnFangIntf.eventClosed(closeParam, username=InitDefaultPara.userInit['DftJieDaoUser'], password='11111111')
        result2 =  json.loads(ret.text)
        self.assertTrue(ret.result,'事件结案失败')
        
        Time.wait(5)
        
        #督查暗访删除
        delParam = copy.deepcopy(MbDuChaAnFangPara.deleteParam)
        delParam['selectIds'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from secretsupervision t where t.checkcompanyname='%s'"% result2['subject'])
        ret =  MbDuChaAnFangIntf.duChaAnFangDel(delParam, username=InitDefaultPara.userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(ret.result,'督查暗访删除失败')


        
        
        
        
        
        
        
#督查暗访高级搜索        
    def teskssb_003(self):
        '''督查暗访高级搜索'''
        #督查暗访信息新增
        issueParam = copy.deepcopy(MbDuChaAnFangPara.duChaAnFangAddParam)
        issueParam['secretSupervision.checkCompanyName'] = '检查单位%s' % CommonUtil.createRandomString(6) 
        issueParam['secretSupervision.mobileNumber'] = random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8))
        issueParam['secretSupervision.checkLegalPerson'] = '张三'
        issueParam['secretSupervision.checkSubject'] = '检查科目%s' % CommonUtil.createRandomString(6)
        issueParam['secretSupervision.checkAddress'] = '学院路50号'
        issueParam['secretSupervision.orgId'] = InitDefaultPara.orgInit['DftJieDaoOrgId']
        issueParam['secretSupervision.findProblems'] = '正常'
        issueParam['secretSupervision.checkTime'] = Time.getCurrentDate()
        issueParam['secretSupervision.requires'] ='荼毒'

        ret =  MbDuChaAnFangIntf.KuaiShuShangBaoAdd(issueParam, username=InitDefaultPara.userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(ret,'督查暗访新增失败')
        Time.wait(1)
        
        #督查暗访信息新增
        issueParam2 = copy.deepcopy(MbDuChaAnFangPara.duChaAnFangAddParam)
        issueParam2['secretSupervision.checkCompanyName'] = '检查单位%s' % CommonUtil.createRandomString(6) 
        issueParam2['secretSupervision.mobileNumber'] = random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8))
        issueParam2['secretSupervision.checkLegalPerson'] = '张三'
        issueParam2['secretSupervision.checkSubject'] = '检查科目%s' % CommonUtil.createRandomString(6)
        issueParam2['secretSupervision.checkAddress'] = '学院路50号'
        issueParam2['secretSupervision.orgId'] = InitDefaultPara.orgInit['DftJieDaoOrgId']
        issueParam2['secretSupervision.findProblems'] = '正常'
        issueParam2['secretSupervision.checkTime'] = Time.getCurrentDate()
        issueParam2['secretSupervision.requires'] ='荼毒'

        ret =  MbDuChaAnFangIntf.KuaiShuShangBaoAdd(issueParam2, username=InitDefaultPara.userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(ret,'督查暗访新增失败')
        Time.wait(1)        
        
        #高级搜索 搜索检查地址 期望中的
        searchParam  = copy.deepcopy(MbDuChaAnFangPara.check_searchDuChaAnFangParam)
        searchParam['checkAddress'] = issueParam2['secretSupervision.checkAddress'] 
        ret =  MbDuChaAnFangIntf.searchDuChaAnFangAddress(searchParam,issueParam['secretSupervision.checkAddress'] , username=InitDefaultPara.userInit['DftJieDaoUser'], password='11111111')
        self.assertTrue(ret,'督查暗访期望中的检查地址搜索失败')
        
        #高级搜索 搜索检查地址 不期望中的
        searchParam  = copy.deepcopy(MbDuChaAnFangPara.check_searchDuChaAnFangParam)
        searchParam['checkAddress'] = issueParam2['secretSupervision.checkAddress'] 
        ret =  MbDuChaAnFangIntf.searchDuChaAnFangAddressNot(searchParam,issueParam2['secretSupervision.checkAddress'] , username=InitDefaultPara.userInit['DftJieDaoUser'], password='11111111')
        self.assertFalse(ret,'督查暗访不期望中的检查地址搜索失败')

    
    def tearDown(self):
            pass
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(MbDuChaAnFang("teskssb_001")) 
#    suite.addTest(MbDuChaAnFang("teskssb_002")) 
#     suite.addTest(MbDuChaAnFang("teskssb_003")) 
    
    results = unittest.TextTestRunner().run(suite)
    pass