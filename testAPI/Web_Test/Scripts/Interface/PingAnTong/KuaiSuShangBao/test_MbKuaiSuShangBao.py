# -*- coding:UTF-8 -*-
'''
Created on 2016-4-7

@author: lhz
'''
from __future__ import unicode_literals
import unittest
from Interface.PingAnJianShe.SystemMgr import SystemMgrIntf
import copy
from Interface.PingAnTong.KuaiShuShangBao import MbKuaiSuShangBaoPara,\
    MbKuaiSuShangBaoIntf
from CONFIG import InitDefaultPara
from COMMON import Time
import random
import time
class KuaiSuShangBao(unittest.TestCase):
    def setUp(self):
        SystemMgrIntf.initEnv()
        pass

    '''
    @功能：快速上报新增
    @ lhz  2016-4-7
    ''' 
    def testkssb_001(self):
        '''快速上报'''
        #新增单位信息
        issueParam = copy.deepcopy(MbKuaiSuShangBaoPara.reportParam)
        issueParam['issueNew.occurOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        issueParam['issueNew.issueContent'] = '其他'
        issueParam['issueNew.occurDate'] = Time.getCurrentDate()
        issueParam['hours'] =  time.strftime("%H")
        issueParam['issueNew.module_IssueType'] = ''
        issueParam['issueRelatedPeopleNames'] = '待填写'
        issueParam['issueNew.subject'] = '其他'
        issueParam['issueNew.relatePeopleCount'] = '1'
        issueParam['content'] = '快速上报'
        issueParam['operatorName'] =InitDefaultPara.userInit['DftWangGeUserXM'] 
        issueParam['operatorMobile'] = random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8))
        issueParam['issueNew.mSelect_secondTypeName'] = '其他'
        issueParam['dealOrgId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        issueParam['selContradictionId'] = 19
        issueParam['minute'] = time.strftime("%M")
        
        ret =  MbKuaiSuShangBaoIntf.KuaiShuShangBaoAdd(issueParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret,'快速上报失败')
        Time.wait(1)
        
        #检验快速上报后是否在上一级中有显示
        checkIssueParam = copy.deepcopy(MbKuaiSuShangBaoPara.checkParam)
        checkIssueParam['subject'] = issueParam['issueNew.subject']
        ret =  MbKuaiSuShangBaoIntf.check_KuaiShuShangBao(checkIssueParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret,'快速上报失败')

    
    def tearDown(self):
            pass
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(KuaiSuShangBao("testkssb_001")) 
    
    results = unittest.TextTestRunner().run(suite)
    pass