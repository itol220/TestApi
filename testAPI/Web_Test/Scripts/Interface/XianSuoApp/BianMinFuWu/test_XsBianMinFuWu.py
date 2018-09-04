# -*- coding:UTF-8 -*-
'''
Created on 2016-4-8

@author: N-286
'''
from __future__ import unicode_literals
from CONFIG import Global
from CONFIG.InitDefaultPara import clueOrgInit
from Interface.XianSuoApp.BianMinFuWu.XsBianMinFuWuIntf import addPhoneCategory, \
    addPhone, checkPhoneInList, deleteAllPhones
from Interface.XianSuoApp.BianMinFuWu.XsBianMinFuWuPara import changYongDianHua
from Interface.XianSuoApp.GongZuoTai.XsGongZuoTaiIntf import initUser
import copy
import json
import unittest

class XsBianMinFuWu(unittest.TestCase):

    def setUp(self):
#         SystemMgrIntf.initEnv()''
        if Global.simulationEnvironment is False:
            deleteAllPhones()
        initUser()
        pass
    def test_XsBianMinFuWu_01(self):
        #运维平台新增便民服务
        addPara1={
            'companyCategory.categoryName':'治安安全',
            'companyCategory.departmentNo':clueOrgInit['DftQuOrgDepNo'],
            'companyCategory.orgName':clueOrgInit['DftQuOrg']
               }
        result1=addPhoneCategory(para=addPara1)
        self.assertTrue(result1.result, '新增电话分类失败')
        #新增常用电话
        addPara2=copy.deepcopy(changYongDianHua)
        addPara2['companyPhone.companyCategoryId']=json.loads(result1.text)['id']
        result2=addPhone(para=addPara2)
        self.assertTrue(result2.result, '新增电话失败')
        #线索中查看便民服务
        viewPhonePara={
                'tqmobile':'true',
                'departmentNo':addPara1['companyCategory.departmentNo'],
                'page':'1',
                'rows':'200',
                       }
        checkPara={
                'companyName':addPara2['companyPhone.companyName'],
                'telePhone':addPara2['companyPhone.telePhone'],
                'remark':addPara2['companyPhone.remark']
                   }
        result3=checkPhoneInList(checkPara=checkPara,listPara=viewPhonePara)
        self.assertTrue(result3, '便民服务电话查找失败')
        pass
    def tearDown(self):
        pass  
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(XsBianMinFuWu("test_XsBianMinFuWu_01"))
    results = unittest.TextTestRunner().run(suite)
    pass   
