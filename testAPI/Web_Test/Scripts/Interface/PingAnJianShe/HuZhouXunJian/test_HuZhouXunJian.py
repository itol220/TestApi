# -*- coding:UTF-8 -*-

'''
Created on 2015-11-12

@author: lhz
'''
from __future__ import unicode_literals
from CONFIG import Global
import unittest
import copy
from COMMON import Log, CommonUtil, Time
from Interface.PingAnJianShe.HuzhouXunJian import HuZhouXunJianIntf, \
    HuZhouXunJianPara
from Interface.PingAnJianShe.Common import CommonIntf
from CONFIG import InitDefaultPara 
from Interface.PingAnJianShe.SystemMgr import SystemMgrIntf
import time
# reload(sys)
# sys.setdefaultencoding('utf-8')
    
class HuZhouXunJian(unittest.TestCase):

    def setUp(self):
        SystemMgrIntf.initEnv()
        #单位删除完了，专项检查里面的东西也都没了
        #HuZhouXunJianIntf.deleteAllSearchByIds_huZhouXunJian()
        HuZhouXunJianIntf.deleteAllSearchByIds_moudle()
        HuZhouXunJianIntf.deleteAllSearchByIds_huZhouXunJian()
        pass                                                                  
# 1.验证基础信息是否能新增 成功    
    def test_HuZhouXuanJianCompanyAdd_01(self):
        """基础信息新增""" 
        #新增单位信息
        issueParam = copy.deepcopy(HuZhouXunJianPara.editOrAddObject) 
        issueParam['safetyCheckBasics.org.id'] = InitDefaultPara.orgInit['DftJieDaoOrgId']
        issueParam['safetyCheckBasics.companyName'] = '天阙科技05%s' % CommonUtil.createRandomString(6) 
        issueParam['safetyCheckBasics.companyAddr'] = '西城广场2'
        issueParam['safetyCheckBasics.companyType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='平安检查企业类型', displayName='规上企业')  
        issueParam['safetyCheckBasics.orgNo'] = '33'
        issueParam['safetyCheckBasics.id'] = ''
        issueParam['mode'] = 'add'
        
        issueParam['safetyCheckBasics.org.orgInternalCode'] = CommonIntf.getDbQueryResult(dbCommand="select t.orginternalcode from ORGANIZATIONS t where t.id = %s"%issueParam['safetyCheckBasics.org.id'])
        ret = HuZhouXunJianIntf.addsafetyCheckBasics(issueDict=issueParam,username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, '单位信息新增失败')
        Time.wait(1)
        # #检查  新增的数据是否存在 
        # 复制一份儿检查项【ps：方面重新赋值使用】
        param = copy.deepcopy(HuZhouXunJianPara.HuZhouXunJian_check)
        # 获取组织机构id
        param['companyAddr'] = issueParam['safetyCheckBasics.companyAddr']
        # 获取查询参数
        param['companyName'] = issueParam['safetyCheckBasics.companyName'] 
        ret = HuZhouXunJianIntf.check_huzhouxunjian(companyDict=param, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, '企业查找失败')
     

                
# 修改
    def test_HuZhouXuanJianCompanyUpdate_02(self):
        """基础信息修改""" 
        Log.LogOutput( message='基础信息修改    。。。')
        # 先新增 
        issueParam = copy.deepcopy(HuZhouXunJianPara.editOrAddObject) 
        issueParam['safetyCheckBasics.org.id'] = InitDefaultPara.orgInit['DftJieDaoOrgId']
        issueParam['safetyCheckBasics.companyName'] = '天阙科技%s' % CommonUtil.createRandomString(6)
        issueParam['safetyCheckBasics.companyAddr'] = '西城广场2'
        issueParam['safetyCheckBasics.companyType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='平安检查企业类型', displayName='规上企业')   
        issueParam['safetyCheckBasics.orgNo'] = '33'
        issueParam['safetyCheckBasics.id'] = ''
        issueParam['mode'] = 'add'
        issueParam['safetyCheckBasics.org.orgInternalCode'] = CommonIntf.getDbQueryResult(dbCommand="select t.orginternalcode from ORGANIZATIONS t where t.id = %s"%issueParam['safetyCheckBasics.org.id'])
        ret = HuZhouXunJianIntf.addsafetyCheckBasics(issueDict=issueParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, '企业新增失败')
        Time.wait(1)
        # 修改
        issueParam['safetyCheckBasics.id'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetycheckbasics t where t.companyname = '%s'"%issueParam['safetyCheckBasics.companyName'])
        issueParam['safetyCheckBasics.org.id'] = InitDefaultPara.orgInit['DftJieDaoOrgId']
        issueParam['safetyCheckBasics.companyName'] = '天阙科技05%s' % CommonUtil.createRandomString(6)
        issueParam['safetyCheckBasics.companyAddr'] = '西城广场'
        issueParam['safetyCheckBasics.companyType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='平安检查企业类型', displayName='规上企业')    
        issueParam['safetyCheckBasics.orgNo'] = '44'
        issueParam['mode'] = 'edit'
        issueParam['safetyCheckBasics.org.orgInternalCode'] = CommonIntf.getDbQueryResult(dbCommand="select t.orginternalcode from ORGANIZATIONS t where t.id = %s"%issueParam['safetyCheckBasics.org.id'])
        ret = HuZhouXunJianIntf.edit_huZhouXunJian(issueDict=issueParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, '企业修改失败')
        Time.wait(1)
# #检查  修改的数据是否存在 
# 复制一份儿检查项【ps：方面重新赋值使用】
        param = copy.deepcopy(HuZhouXunJianPara.HuZhouXunJian_check)
        # 获取组织机构id
        param['companyAddr'] = issueParam['safetyCheckBasics.companyAddr']
        # 获取查询参数
        param['companyName'] = issueParam['safetyCheckBasics.companyName'] 
        # param['companyType']= issueParam['safetyCheckBasics.companyType.id']
        param['orgNo'] = issueParam['safetyCheckBasics.orgNo']
        ret = HuZhouXunJianIntf.check_huzhouxunjian(companyDict=param , username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, '企业修改查找失败')
         
                
# #删除
    def test_HuZhouXunJianDelete_03(self):
        """基础信息单条删除""" 
        # 先新增
        issueParam = copy.deepcopy(HuZhouXunJianPara.editOrAddObject) 
        issueParam['safetyCheckBasics.org.id'] = InitDefaultPara.orgInit['DftJieDaoOrgId']
        issueParam['safetyCheckBasics.companyName'] = '天阙科技05%s' % CommonUtil.createRandomString(6)
        issueParam['safetyCheckBasics.companyAddr'] = '西城广场2'
        issueParam['safetyCheckBasics.companyType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='平安检查企业类型', displayName='规上企业')   
        issueParam['safetyCheckBasics.orgNo'] = '33'
        issueParam['safetyCheckBasics.id'] = ''
        issueParam['mode'] = 'add'
        issueParam['safetyCheckBasics.org.orgInternalCode'] = CommonIntf.getDbQueryResult(dbCommand="select t.orginternalcode from ORGANIZATIONS t where t.id = %s"%issueParam['safetyCheckBasics.org.id'])
        ret = HuZhouXunJianIntf.addsafetyCheckBasics(issueDict=issueParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, '企业新增失败')
        Time.wait(1)
        idsParam = copy.deepcopy(HuZhouXunJianPara.HuZhouXunJian_ids) 
        idsParam['ids'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetycheckbasics t where t.companyname ='%s'"% issueParam['safetyCheckBasics.companyName'])
        ret = HuZhouXunJianIntf.deleteById_huZhouXunJian(issueDict=idsParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, '企业删除失败')
        Time.wait(1)
        # 复制一份儿检查项【ps：方面重新赋值使用】
        param = copy.deepcopy(HuZhouXunJianPara.HuZhouXunJian_check)
        # 获取查询参数
        param['companyName'] = issueParam['safetyCheckBasics.companyName'] 
        # #检查是否删除成功
        ret = HuZhouXunJianIntf.check_huzhouxunjian(companyDict=param, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertFalse(ret, '企业删除失败')
        
# # # 批量删除
#     def test_HuZhouXunJianDeletionByQuery_04 (self):
#         """基础信息批量删除 """ 
#         # 先新增
#         issueParam = copy.deepcopy(HuZhouXunJianPara.editOrAddObject) 
#         issueParam['safetyCheckBasics.org.id'] = InitDefaultPara.orgInit['DftJieDaoOrgId']
#         issueParam['safetyCheckBasics.companyName'] = '天阙科技05%s' % CommonUtil.createRandomString(6)
#         issueParam['safetyCheckBasics.companyAddr'] = '西城广场2'
#         issueParam['safetyCheckBasics.companyType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='平安检查企业类型', displayName='规上企业')   
#         issueParam['safetyCheckBasics.orgNo'] = '33'
#         issueParam['safetyCheckBasics.id'] = ''
#         issueParam['mode'] = 'add'
#         issueParam['safetyCheckBasics.org.orgInternalCode'] = CommonIntf.getDbQueryResult(dbCommand="select t.orginternalcode from ORGANIZATIONS t where t.id = %s"%issueParam['safetyCheckBasics.org.id'])
#         ret = HuZhouXunJianIntf.addsafetyCheckBasics(issueDict=issueParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
#         self.assertTrue(ret, '企业新增失败')
#         Time.wait(1)
#         
#         # 先新增
#         issueParam2 = copy.deepcopy(HuZhouXunJianPara.editOrAddObject) 
#         issueParam2['safetyCheckBasics.org.id'] = InitDefaultPara.orgInit['DftJieDaoOrgId']
#         issueParam2['safetyCheckBasics.companyName'] = '天阙科技00%s' % CommonUtil.createRandomString(6)
#         issueParam2['safetyCheckBasics.companyAddr'] = '西城广场3'
#         issueParam2['safetyCheckBasics.companyType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='平安检查企业类型', displayName='规上企业')   
#         issueParam2['safetyCheckBasics.orgNo'] = '44'
#         issueParam2['safetyCheckBasics.id'] = ''
#         issueParam2['mode'] = 'add'
#         issueParam2['safetyCheckBasics.org.orgInternalCode'] = CommonIntf.getDbQueryResult(dbCommand="select t.orginternalcode from ORGANIZATIONS t where t.id = %s"%issueParam2['safetyCheckBasics.org.id'])
#         ret = HuZhouXunJianIntf.addsafetyCheckBasics(issueDict=issueParam2, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
#         self.assertTrue(ret, '企业新增失败')
#         Time.wait(1)
#         
#          
#         Param = copy.deepcopy(HuZhouXunJianPara.HuZhouXunJian_ids)
#         Param['ids'] = CommonIntf.getDbQueryResultList(dbCommand = "select t.id from safetycheckbasics t  where t.companyname in('%s','%s')" % (issueParam['safetyCheckBasics.companyName'],issueParam2['safetyCheckBasics.companyName']))
#         ret = HuZhouXunJianIntf.deleteAll_huZhouXunJian(issueDict=Param, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
#         self.assertTrue(ret, '企业批量删除失败')
#          
#         #第一条数据检查是否删除成功
#         deleteParam = copy.deepcopy(HuZhouXunJianPara.HuZhouXunJian_check)
#         # 获取查询参数
#         deleteParam['companyName'] = issueParam['safetyCheckBasics.companyName'] 
#         # #检查是否删除成功
#         ret = HuZhouXunJianIntf.check_huzhouxunjian(companyDict=deleteParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
#         self.assertFalse(ret, '企业批量删除失败')
#           
#           
#         #第二条数据检查是否删除成功
#         deleteParam2 = copy.deepcopy(HuZhouXunJianPara.HuZhouXunJian_check)
#         # 获取查询参数
#         deleteParam2['companyName'] = issueParam2['safetyCheckBasics.companyName'] 
#         # #检查是否删除成功
#         ret = HuZhouXunJianIntf.check_huzhouxunjian(companyDict=deleteParam2, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
#         self.assertFalse(ret, '企业批量删除失败')
         
# 高级搜索
    def test_HuZhouXunJianSearchByAll_05(self):
        """基础信息高级搜索 """
        # 先新增第一条数据
        issueParam = copy.deepcopy(HuZhouXunJianPara.editOrAddObject) 
        issueParam['safetyCheckBasics.org.id'] = InitDefaultPara.orgInit['DftJieDaoOrgId']
        issueParam['safetyCheckBasics.companyName'] = '天阙科技05%s' % CommonUtil.createRandomString(6)
        issueParam['safetyCheckBasics.companyAddr'] = '西城广场2'
        issueParam['safetyCheckBasics.companyType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='平安检查企业类型', displayName='规上企业')  
        issueParam['safetyCheckBasics.orgNo'] = '33'
        issueParam['safetyCheckBasics.id'] = ''
        issueParam['mode'] = 'add'
        issueParam['safetyCheckBasics.org.orgInternalCode'] = CommonIntf.getDbQueryResult(dbCommand="select t.orginternalcode from ORGANIZATIONS t where t.id = %s"%issueParam['safetyCheckBasics.org.id'])
        ret = HuZhouXunJianIntf.addsafetyCheckBasics(issueDict=issueParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')  
        self.assertTrue(ret, '企业新增第一条数据失败')
        Time.wait(1)
        # 先新增第二条数据
        issueParam2 = copy.deepcopy(HuZhouXunJianPara.editOrAddObject) 
        issueParam2['safetyCheckBasics.org.id'] = InitDefaultPara.orgInit['DftJieDaoOrgId']
        issueParam2['safetyCheckBasics.companyName'] = '天阙科技055%s'% CommonUtil.createRandomString(6)
        issueParam2['safetyCheckBasics.companyAddr'] = '西城广场2'
        issueParam2['safetyCheckBasics.companyType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='平安检查企业类型', displayName='规上企业')  
        issueParam2['safetyCheckBasics.orgNo'] = '33'
        issueParam2['safetyCheckBasics.id'] = ''
        issueParam2['mode'] = 'add'
        issueParam2['safetyCheckBasics.org.orgInternalCode'] = CommonIntf.getDbQueryResult(dbCommand="select t.orginternalcode from ORGANIZATIONS t where t.id = %s"%issueParam['safetyCheckBasics.org.id'])
        ret = HuZhouXunJianIntf.addsafetyCheckBasics(issueDict=issueParam2, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')  
        self.assertTrue(ret, '企业新增第二条数据失败')
        Time.wait(1)
        # 第一种情况:根据企业名称搜索 
        issueParamSearch = copy.deepcopy(HuZhouXunJianPara.editOrAddObject) 
        issueParamSearch['safetyCheckBasics.companyName'] = issueParam2['safetyCheckBasics.companyName']
        ret = HuZhouXunJianIntf.findByCompany(issueParamSearch, username=InitDefaultPara.userInit['DftShiUser'], password='11111111');
        self.assertTrue(ret, '企业信息搜索失败')
        Time.wait(1)
        ret = HuZhouXunJianIntf.findByCompanyByMatch(issueParamSearch, issueParam['safetyCheckBasics.companyName'], username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertFalse(ret, '不存在的数据匹配失败')
        Time.wait(1)
        # 第二种情况:根据企业地址,企业名称
        issueParamSearch = copy.deepcopy(HuZhouXunJianPara.editOrAddObject) 
        issueParamSearch['safetyCheckBasics.companyName'] = issueParam2['safetyCheckBasics.companyName']
        issueParamSearch['safetyCheckBasics.companyAddr'] = issueParam2['safetyCheckBasics.companyAddr']
        # 检验是否搜索成功
        ret = HuZhouXunJianIntf.findByCompany(issueParamSearch, username=InitDefaultPara.userInit['DftShiUser'], password='11111111');
        self.assertTrue(ret, '企业信息搜索失败')
        Time.wait(1)
        # 输入不存在的数据验证是否能查到
        ret = HuZhouXunJianIntf.findByCompanyByMatch(issueParamSearch, issueParam['safetyCheckBasics.companyName'], username=Global.PingAnJianSheUser, password=Global.PingAnJianShePass)
        self.assertFalse(ret, '不存在的数据匹配失败')
        Time.wait(1)
        # 第三种情况:根据企业地址,企业名称,企业地址和企业类型搜索
        issueParamSearch = copy.deepcopy(HuZhouXunJianPara.editOrAddObject) 
        issueParamSearch['safetyCheckBasics.companyName'] = issueParam2['safetyCheckBasics.companyName']
        issueParamSearch['safetyCheckBasics.companyAddr'] = issueParam2['safetyCheckBasics.companyAddr']
        issueParamSearch['safetyCheckBasics.companyType.id'] = issueParam2['safetyCheckBasics.companyType.id']
        issueParamSearch['safetyCheckBasics.orgNo'] = issueParam2['safetyCheckBasics.orgNo']
        # 检验是否搜索成功
        ret = HuZhouXunJianIntf.findByCompany(issueParamSearch, username=InitDefaultPara.userInit['DftShiUser'], password='11111111');
        self.assertTrue(ret, '企业信息搜索失败')
        Time.wait(1)
        # 输入不存在的数据验证是否能查到
        ret = HuZhouXunJianIntf.findByCompanyByMatch(issueParamSearch, issueParam['safetyCheckBasics.companyName'], username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertFalse(ret, '不存在的数据匹配失败')
        

        


# 合并单位  
    def test_unionCompany_06(self):
        """平安检查--基础信息--合并单位 """
        # 先新增第一条数据
        issueParam = copy.deepcopy(HuZhouXunJianPara.editOrAddObject) 
        issueParam['safetyCheckBasics.org.id'] = InitDefaultPara.orgInit['DftJieDaoOrgId']
        issueParam['safetyCheckBasics.companyName'] = '天阙科技05%s' % CommonUtil.createRandomString(6)
        issueParam['safetyCheckBasics.companyAddr'] = '西城广场2'
        issueParam['safetyCheckBasics.companyType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='平安检查企业类型', displayName='规上企业')  
        issueParam['safetyCheckBasics.orgNo'] = '33'
        issueParam['safetyCheckBasics.id'] = ''
        issueParam['mode'] = 'add'
        issueParam['safetyCheckBasics.org.orgInternalCode'] = CommonIntf.getDbQueryResult(dbCommand="select t.orginternalcode from ORGANIZATIONS t where t.id = %s"%issueParam['safetyCheckBasics.org.id'])
        ret = HuZhouXunJianIntf.addsafetyCheckBasics(issueDict=issueParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')  
        self.assertTrue(ret, '企业新增第一条数据失败')
        Time.wait(1)
        # 先新增第二条数据
        issueParam2 = copy.deepcopy(HuZhouXunJianPara.editOrAddObject) 
        issueParam2['safetyCheckBasics.org.id'] = InitDefaultPara.orgInit['DftJieDaoOrgId'] 
        issueParam2['safetyCheckBasics.companyName'] = '天阙科技055%s' % CommonUtil.createRandomString(6)
        issueParam2['safetyCheckBasics.companyAddr'] = '西城广场2'
        issueParam2['safetyCheckBasics.companyType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='平安检查企业类型', displayName='规上企业')  
        issueParam2['safetyCheckBasics.orgNo'] = '33'
        issueParam2['safetyCheckBasics.id'] = ''
        issueParam2['mode'] = 'add'
        issueParam2['safetyCheckBasics.org.orgInternalCode'] = CommonIntf.getDbQueryResult(dbCommand="select t.orginternalcode from ORGANIZATIONS t where t.id = %s"%issueParam['safetyCheckBasics.org.id'])
        ret = HuZhouXunJianIntf.addsafetyCheckBasics(issueDict=issueParam2, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')  
        self.assertTrue(ret, '企业新增第二条数据失败')
        Time.wait(1)
        idsParam = copy.deepcopy(HuZhouXunJianPara.HuZhouXunJian_unionParam) 
        # 获取要合并的两条数据id
        idsParam['ids'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetycheckbasics t where t.companyname in ('%s','%s')"%(issueParam2['safetyCheckBasics.companyName'],issueParam['safetyCheckBasics.companyName']))
        # 获取合并到那条数据的id
        idsParam['mergeId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetycheckbasics t where t.companyname ='%s'"%issueParam2['safetyCheckBasics.companyName'])
        ret= HuZhouXunJianIntf.unionCompany(issueDict=idsParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, '合并单位失败')
        Time.wait(1)
        # # 检查点 验证合并单位是否成功
        # 复制一份儿检查项【ps：方面重新赋值使用】
        param = copy.deepcopy(HuZhouXunJianPara.HuZhouXunJian_check)
        # 获取查询参数
        param['companyName'] = issueParam2['safetyCheckBasics.companyName'] 
        # #检查列表是否存在合并的那条数据
        ret = HuZhouXunJianIntf.check_huzhouxunjian(companyDict=param, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, "列表中没有找到合并之后的单位")     
# 导出数据 
    def test_exportData_07(self):
        """平安检查--基础信息--导出数据  """
        # 先新增第一条数据
        issueParam = copy.deepcopy(HuZhouXunJianPara.editOrAddObject) 
        issueParam['safetyCheckBasics.org.id'] = InitDefaultPara.orgInit['DftJieDaoOrgId']
        issueParam['safetyCheckBasics.companyName'] = '天阙科技05%s' % CommonUtil.createRandomString(6)
        issueParam['safetyCheckBasics.companyAddr'] = '西城广场2'
        issueParam['safetyCheckBasics.companyType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='平安检查企业类型', displayName='规上企业')  
        issueParam['safetyCheckBasics.orgNo'] = '33'
        issueParam['safetyCheckBasics.id'] = ''
        issueParam['mode'] = 'add'
        issueParam['safetyCheckBasics.org.orgInternalCode'] = CommonIntf.getDbQueryResult(dbCommand="select t.orginternalcode from ORGANIZATIONS t where t.id = %s"%issueParam['safetyCheckBasics.org.id'])
        ret = HuZhouXunJianIntf.addsafetyCheckBasics(issueDict=issueParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')  
        self.assertTrue(ret, '企业新增第一条数据失败')
        Time.wait(1)
        downLoadCompany = copy.deepcopy(HuZhouXunJianPara.exportDataParam)
        downLoadCompany['orgId'] = InitDefaultPara.orgInit['DftJieDaoOrgId']
        ret = HuZhouXunJianIntf.exportDataCompany(downLoadCompany, username=InitDefaultPara.userInit['DftShiUser'], password='11111111');         
        with open("C:/autotest_file/test.xlsx", "wb") as code:
            code.write(ret.content)
        pass 
        #检查点
        ret=CommonUtil.checkExcelCellValue(issueParam['safetyCheckBasics.companyName'],"test.xlsx" , "基础信息", "A4")
        self.assertTrue(ret, "导出信息查找失败")
          

# 模板设置---新增年度目录
    def test_addModel_08(self):
        """平安检查--模板设置--新增模板 """
        # 新增模板
        modelParam = copy.deepcopy(HuZhouXunJianPara.addOrUpdateModelParam)
        modelParam['safetyCheckModule.moduleName'] = '2016年考核模板%s' % CommonUtil.createRandomString(6)
        modelParam['safetyCheckModule.checkYear'] = '2016'
        modelParam['safetyCheckModule.id'] = ''
        modelParam['safetyCheckModule.org.id'] = ''
        modelParam['safetyCheckModule.checkObject'] = '20'
        modelParam['mode'] = 'add'
        ret = HuZhouXunJianIntf.addModel(param=modelParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, "新增的模板失败")
        Time.wait(1)
        # 检查点
        checkModelParam = copy.deepcopy(HuZhouXunJianPara.checkModelParam)
        checkModelParam['moduleName'] = modelParam['safetyCheckModule.moduleName']
        ret = HuZhouXunJianIntf.checkAddModel(param=checkModelParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, "新增的模板名称在列表中不存在") 
          
# 新增一级分类         
    def test_addFirstClass_09(self): 
        """平安检查--模板设置--新增模板--新增一级分类 """
        # 新增模板
        modelParam = copy.deepcopy(HuZhouXunJianPara.addOrUpdateModelParam)
        modelParam['safetyCheckModule.moduleName'] = '2016年考核模板%s' % CommonUtil.createRandomString(6)
        modelParam['safetyCheckModule.checkYear'] = '2016'
        modelParam['safetyCheckModule.id'] = ''
        modelParam['safetyCheckModule.org.id'] = ''
        modelParam['safetyCheckModule.checkObject'] = '20'
        modelParam['mode'] = 'add'
        ret = HuZhouXunJianIntf.addModel(param=modelParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, "新增的模板失败") 
        Time.wait(1) 
        # 新增一级分类
        firstClassParam = copy.deepcopy(HuZhouXunJianPara.addClass) 
        firstClassParam['safetyCheckModuleDetail.moduleId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModule t where t.moduleName ='%s'" % modelParam['safetyCheckModule.moduleName'])
        firstClassParam['safetyCheckModuleDetail.displayName'] = '火灾隐患%s' % CommonUtil.createRandomString(6)
        firstClassParam['safetyCheckModuleDetail.score'] = '2.0' 
        firstClassParam['safetyCheckModuleDetail.detailLevel']='1'
        firstClassParam['safetyCheckModuleDetail.isLeaf']='false'
        firstClassParam['safetyCheckModuleDetail.isUse']=True
        ret = HuZhouXunJianIntf.addClass(level=firstClassParam['safetyCheckModuleDetail.detailLevel'], param=firstClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, "新增一级分类失败")
        Time.wait(1)
        # 检查点
        moduleId = firstClassParam['safetyCheckModuleDetail.moduleId']
        level =  firstClassParam['safetyCheckModuleDetail.detailLevel']
        checkFirstClass = copy.deepcopy(HuZhouXunJianPara.checkModelFirst)
        checkFirstClass['displayName'] = firstClassParam['safetyCheckModuleDetail.displayName']
        #分数
        
        
        ret = HuZhouXunJianIntf.checkFirstClass(level,moduleId, param=checkFirstClass, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, "新增的一级分类在列表中不存在") 
       
        

# 新增二级分类         
    def test_addTwoClass_010(self): 
        """平安检查--模板设置--新增模板--新增二级分类 """
        # 新增模板
        modelParam = copy.deepcopy(HuZhouXunJianPara.addOrUpdateModelParam)
        modelParam['safetyCheckModule.moduleName'] = '2016年考核模板%s' % CommonUtil.createRandomString(6)
        modelParam['safetyCheckModule.checkYear'] = '2016'
        modelParam['safetyCheckModule.id'] = ''
        modelParam['safetyCheckModule.org.id'] = InitDefaultPara.orgInit['DftShiOrgId']
        modelParam['safetyCheckModule.checkObject'] = '20'
        modelParam['mode'] = 'add'
        ret = HuZhouXunJianIntf.addModel(param=modelParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')   
        self.assertTrue(ret, "新增模板失败")
        Time.wait(1)
        # 新增一级分类
        firstClassParam = copy.deepcopy(HuZhouXunJianPara.addClass) 
        firstClassParam['safetyCheckModuleDetail.moduleId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModule t where t.moduleName ='%s'" %modelParam['safetyCheckModule.moduleName'])
        firstClassParam['safetyCheckModuleDetail.displayName'] = '火灾隐患%s' % CommonUtil.createRandomString(6)
        firstClassParam['safetyCheckModuleDetail.score'] = '2' 
        firstClassParam['safetyCheckModuleDetail.detailLevel']='1'
        firstClassParam['safetyCheckModuleDetail.isLeaf']='false'
        firstClassParam['safetyCheckModuleDetail.isUse']=True
        ret = HuZhouXunJianIntf.addClass(level=firstClassParam['safetyCheckModuleDetail.detailLevel'], param=firstClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, "新增一级分类失败")
        Time.wait(1)
        # 新增二级分类       
        twoClassParam = copy.deepcopy(HuZhouXunJianPara.addClass)
        twoClassParam['safetyCheckModuleDetail.parentId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModuleDetail t where t.displayname = '%s'" %firstClassParam['safetyCheckModuleDetail.displayName'])
        twoClassParam['safetyCheckModuleDetail.moduleId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.moduleid from safetyCheckModuleDetail t where t.displayname = '%s'" %firstClassParam['safetyCheckModuleDetail.displayName'])
        twoClassParam['safetyCheckModuleDetail.displayName'] = '火灾隐患项2级分类%s' % CommonUtil.createRandomString(6)
        twoClassParam['safetyCheckModuleDetail.score'] = '1'
        twoClassParam['safetyCheckModuleDetail.detailLevel']='2'
        twoClassParam['safetyCheckModuleDetail.isLeaf']='false'
        twoClassParam['safetyCheckModuleDetail.isUse']=True
        ret = HuZhouXunJianIntf.addClass(level=twoClassParam['safetyCheckModuleDetail.detailLevel'],param=twoClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, "新增二级分类失败") 
        Time.wait(1)
        # 检查点
        moduleId = twoClassParam['safetyCheckModuleDetail.moduleId']
        level =  twoClassParam['safetyCheckModuleDetail.detailLevel']
        checkFirstClass = copy.deepcopy(HuZhouXunJianPara.checkModelFirst)
        checkFirstClass['displayName'] = twoClassParam['safetyCheckModuleDetail.displayName']
        ret = HuZhouXunJianIntf.checkFirstClass(level,moduleId, param=checkFirstClass, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, "新增的二级分类在列表中不存在") 

# 新增细则分类         
    def test_addThreeClass_011(self): 
        """平安检查--模板设置--新增模板--新增细则分类 """
        # 新增模板
        modelParam = copy.deepcopy(HuZhouXunJianPara.addOrUpdateModelParam)
        modelParam['safetyCheckModule.moduleName'] = '2016年考核模板%s' % CommonUtil.createRandomString(6)
        modelParam['safetyCheckModule.checkYear'] = '2016'
        modelParam['safetyCheckModule.id'] = ''
        modelParam['safetyCheckModule.org.id'] = InitDefaultPara.orgInit['DftShiOrgId']
        modelParam['safetyCheckModule.checkObject'] = '20'
        modelParam['mode'] = 'add'
        ret = HuZhouXunJianIntf.addModel(param=modelParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')   
        self.assertTrue(ret, "新增模板失败")
        Time.wait(1)
        # 新增一级分类
        firstClassParam = copy.deepcopy(HuZhouXunJianPara.addClass) 
        firstClassParam['safetyCheckModuleDetail.moduleId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModule t where t.moduleName ='%s'" % modelParam['safetyCheckModule.moduleName'])
        firstClassParam['safetyCheckModuleDetail.displayName'] = '火灾隐患%s' % CommonUtil.createRandomString(6)
        firstClassParam['safetyCheckModuleDetail.score'] = '2' 
        firstClassParam['safetyCheckModuleDetail.detailLevel']='1'
        firstClassParam['safetyCheckModuleDetail.isLeaf']='false'
        firstClassParam['safetyCheckModuleDetail.isUse']=True
        ret = HuZhouXunJianIntf.addClass(level=firstClassParam['safetyCheckModuleDetail.detailLevel'], param=firstClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, "新增一级分类失败")
        Time.wait(1)
        # 新增二级分类       
        twoClassParam = copy.deepcopy(HuZhouXunJianPara.addClass)
        twoClassParam['safetyCheckModuleDetail.parentId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModuleDetail t where t.displayname = '%s'" % firstClassParam['safetyCheckModuleDetail.displayName'])
        twoClassParam['safetyCheckModuleDetail.moduleId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.moduleid from safetyCheckModuleDetail t where t.displayname = '%s'" % firstClassParam['safetyCheckModuleDetail.displayName'])
        twoClassParam['safetyCheckModuleDetail.displayName'] = '火灾隐患项2级分类%s' % CommonUtil.createRandomString(6)
        twoClassParam['safetyCheckModuleDetail.score'] = '1'
        twoClassParam['safetyCheckModuleDetail.detailLevel']='2'
        twoClassParam['safetyCheckModuleDetail.isLeaf']='false'
        twoClassParam['safetyCheckModuleDetail.isUse']=True
        ret = HuZhouXunJianIntf.addClass(level=twoClassParam['safetyCheckModuleDetail.detailLevel'],param=twoClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, "新增二级分类失败") 
        Time.wait(1)
        # 新增三级分类       
        threeClassParam = copy.deepcopy(HuZhouXunJianPara.addClass)
        threeClassParam['safetyCheckModuleDetail.parentId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModuleDetail t where t.displayname = '%s'" % twoClassParam['safetyCheckModuleDetail.displayName'])
        threeClassParam['safetyCheckModuleDetail.moduleId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.moduleid from safetyCheckModuleDetail t where t.displayname = '%s'" %twoClassParam['safetyCheckModuleDetail.displayName'])
        threeClassParam['safetyCheckModuleDetail.displayName'] = '火灾隐患项3级分类%s' % CommonUtil.createRandomString(6)
        threeClassParam['safetyCheckModuleDetail.score'] = '1'
        threeClassParam['safetyCheckModuleDetail.isUse'] = '1'
        threeClassParam['safetyCheckModuleDetail.detailLevel']='3'
        threeClassParam['safetyCheckModuleDetail.isInput']='true'
        threeClassParam['safetyCheckModuleDetail.isLeaf']='true'
        threeClassParam['safetyCheckModuleDetail.isUse']=True
        ret = HuZhouXunJianIntf.addClass(level=threeClassParam['safetyCheckModuleDetail.detailLevel'],param=threeClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, "新增三级分类失败")
        Time.wait(1) 
        # 三级分类检查点
        moduleId = threeClassParam['safetyCheckModuleDetail.moduleId']
        level = threeClassParam['safetyCheckModuleDetail.detailLevel']
        checkFirstClass = copy.deepcopy(HuZhouXunJianPara.checkModelFirst)
        checkFirstClass['displayName'] = threeClassParam['safetyCheckModuleDetail.displayName']
        ret = HuZhouXunJianIntf.checkFirstClass(level,moduleId, param=checkFirstClass, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, "新增的三级分类在列表中不存在")
          
# 启用模板
    def test_isUseModel_012(self): 
        """平安检查--模板设置--启用模板 """
        # 新增模板
        modelParam = copy.deepcopy(HuZhouXunJianPara.addOrUpdateModelParam)
        modelParam['safetyCheckModule.moduleName'] = '2016年考核模板%s' % CommonUtil.createRandomString(6)
        modelParam['safetyCheckModule.checkYear'] = '2016'
        modelParam['safetyCheckModule.id'] = ''
        modelParam['safetyCheckModule.org.id'] = InitDefaultPara.orgInit['DftShiOrgId']
        modelParam['safetyCheckModule.checkObject'] = '20'
        modelParam['mode'] = 'add'
        ret = HuZhouXunJianIntf.addModel(param=modelParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')   
        self.assertTrue(ret, "新增模板失败")
        Time.wait(1)
        # 新增一级分类
        firstClassParam = copy.deepcopy(HuZhouXunJianPara.addClass) 
        firstClassParam['safetyCheckModuleDetail.moduleId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModule t where t.moduleName ='%s'" % modelParam['safetyCheckModule.moduleName'])
        firstClassParam['safetyCheckModuleDetail.displayName'] = '火灾隐患%s' % CommonUtil.createRandomString(6)
        firstClassParam['safetyCheckModuleDetail.score'] = '2' 
        firstClassParam['safetyCheckModuleDetail.detailLevel']='1'
        firstClassParam['safetyCheckModuleDetail.isLeaf']='false'
        firstClassParam['safetyCheckModuleDetail.isUse']=True
        ret = HuZhouXunJianIntf.addClass(level=firstClassParam['safetyCheckModuleDetail.detailLevel'], param=firstClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, "新增模板一级分类失败")
        Time.wait(1)
        # 新增二级分类       
        twoClassParam = copy.deepcopy(HuZhouXunJianPara.addClass)
        twoClassParam['safetyCheckModuleDetail.parentId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModuleDetail t where t.displayname = '%s'" % firstClassParam['safetyCheckModuleDetail.displayName'])
        twoClassParam['safetyCheckModuleDetail.moduleId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.moduleid from safetyCheckModuleDetail t where t.displayname = '%s'" % firstClassParam['safetyCheckModuleDetail.displayName'])
        twoClassParam['safetyCheckModuleDetail.displayName'] = '火灾隐患项2级分类%s' % CommonUtil.createRandomString(6)
        twoClassParam['safetyCheckModuleDetail.score'] = '1'
        twoClassParam['safetyCheckModuleDetail.detailLevel']='2'
        twoClassParam['safetyCheckModuleDetail.isLeaf']='false'
        twoClassParam['safetyCheckModuleDetail.isUse']=True
        ret = HuZhouXunJianIntf.addClass(level=twoClassParam['safetyCheckModuleDetail.detailLevel'],param=twoClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, "新增二级分类失败")
        Time.wait(1) 
        # 新增三级分类       
        threeClassParam = copy.deepcopy(HuZhouXunJianPara.addClass)
        threeClassParam['safetyCheckModuleDetail.parentId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModuleDetail t where t.displayname = '%s'" % twoClassParam['safetyCheckModuleDetail.displayName'])
        threeClassParam['safetyCheckModuleDetail.moduleId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.moduleid from safetyCheckModuleDetail t where t.displayname = '%s'" % twoClassParam['safetyCheckModuleDetail.displayName'])
        threeClassParam['safetyCheckModuleDetail.displayName'] = '火灾隐患项3级分类%s' % CommonUtil.createRandomString(6)
        threeClassParam['safetyCheckModuleDetail.score'] = '1'
        threeClassParam['safetyCheckModuleDetail.isUse'] = '1'
        threeClassParam['safetyCheckModuleDetail.detailLevel']='3'
        threeClassParam['safetyCheckModuleDetail.isInput']='true'
        threeClassParam['safetyCheckModuleDetail.isLeaf']='true'
        threeClassParam['safetyCheckModuleDetail.isUse']=True
        ret = HuZhouXunJianIntf.addClass(level=threeClassParam['safetyCheckModuleDetail.detailLevel'],param=threeClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, "新增三级分类失败") 
        Time.wait(1)
        # 启用模板
        isUseModeParam = copy.deepcopy(HuZhouXunJianPara.isUseMode)
        isUseModeParam['safetyCheckModule.isUse'] = True 
        isUseModeParam['safetyCheckModule.id'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModule t where t.moduleName ='%s'" % modelParam['safetyCheckModule.moduleName'])       
        ret = HuZhouXunJianIntf.isUseModel(param=isUseModeParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        if ret is True:
        # 检查点
            checkUseModeParam = copy.deepcopy(HuZhouXunJianPara.checkIsUseMode) 
            checkUseModeParam['isUse'] = True
            checkUseModeParam['moduleName'] = modelParam['safetyCheckModule.moduleName']
            ret = HuZhouXunJianIntf.checkIsUseMode(param=checkUseModeParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')  
            self.assertTrue(ret, "新增的模板在列表中启用失败")

#停用模板       
    def test_isNotUseModel_013(self): 
        """平安检查--模板设置--停用模板 """
        HuZhouXunJianIntf.deleteAllSearchByIds_moudle()
        # 新增模板
        modelParam = copy.deepcopy(HuZhouXunJianPara.addOrUpdateModelParam)
        modelParam['safetyCheckModule.moduleName'] = '2016年考核模板%s' % CommonUtil.createRandomString(6)
        modelParam['safetyCheckModule.checkYear'] = '2016'
        modelParam['safetyCheckModule.id'] = ''
        modelParam['safetyCheckModule.org.id'] = InitDefaultPara.orgInit['DftShiOrgId']
        modelParam['safetyCheckModule.checkObject'] = '20'
        modelParam['mode'] = 'add'
        ret = HuZhouXunJianIntf.addModel(param=modelParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')   
        self.assertTrue(ret, "新增模板失败")
        Time.wait(1)
        # 新增一级分类
        firstClassParam = copy.deepcopy(HuZhouXunJianPara.addClass) 
        firstClassParam['safetyCheckModuleDetail.moduleId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModule t where t.moduleName ='%s'" % modelParam['safetyCheckModule.moduleName'])
        firstClassParam['safetyCheckModuleDetail.displayName'] = '火灾隐患%s' % CommonUtil.createRandomString(6)
        firstClassParam['safetyCheckModuleDetail.score'] = '2' 
        firstClassParam['safetyCheckModuleDetail.detailLevel']='1'
        firstClassParam['safetyCheckModuleDetail.isLeaf']='false'
        firstClassParam['safetyCheckModuleDetail.isUse']=True
        ret = HuZhouXunJianIntf.addClass(level=firstClassParam['safetyCheckModuleDetail.detailLevel'], param=firstClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, "新增一级分类失败")
        Time.wait(1)
        # 新增二级分类       
        twoClassParam = copy.deepcopy(HuZhouXunJianPara.addClass)
        twoClassParam['safetyCheckModuleDetail.parentId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModuleDetail t where t.displayname = '%s'" %firstClassParam['safetyCheckModuleDetail.displayName'])
        twoClassParam['safetyCheckModuleDetail.moduleId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.moduleid from safetyCheckModuleDetail t where t.displayname = '%s'" % firstClassParam['safetyCheckModuleDetail.displayName'])
        twoClassParam['safetyCheckModuleDetail.displayName'] = '火灾隐患项2级分类%s' % CommonUtil.createRandomString(6)
        twoClassParam['safetyCheckModuleDetail.score'] = '1'
        twoClassParam['safetyCheckModuleDetail.detailLevel']='2'
        twoClassParam['safetyCheckModuleDetail.isLeaf']='false'
        twoClassParam['safetyCheckModuleDetail.isUse']=True
        ret = HuZhouXunJianIntf.addClass(level=twoClassParam['safetyCheckModuleDetail.detailLevel'],param=twoClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, "新增二级分类失败")
        Time.wait(1) 
        # 新增三级分类       
        threeClassParam = copy.deepcopy(HuZhouXunJianPara.addClass)
        threeClassParam['safetyCheckModuleDetail.parentId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModuleDetail t where t.displayname = '%s'" % twoClassParam['safetyCheckModuleDetail.displayName'])
        threeClassParam['safetyCheckModuleDetail.moduleId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.moduleid from safetyCheckModuleDetail t where t.displayname = '%s'"% twoClassParam['safetyCheckModuleDetail.displayName'])
        threeClassParam['safetyCheckModuleDetail.displayName'] = '火灾隐患项3级分类%s' % CommonUtil.createRandomString(6)
        threeClassParam['safetyCheckModuleDetail.score'] = '1'
        threeClassParam['safetyCheckModuleDetail.isUse'] = '1'
        threeClassParam['safetyCheckModuleDetail.detailLevel']='3'
        threeClassParam['safetyCheckModuleDetail.isInput']='true'
        threeClassParam['safetyCheckModuleDetail.isLeaf']='true'
        threeClassParam['safetyCheckModuleDetail.isUse']=True
        ret = HuZhouXunJianIntf.addClass(level=threeClassParam['safetyCheckModuleDetail.detailLevel'],param=threeClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, "新增三级分类失败")
        Time.wait(1) 
        # 启用模板
        isUseModeParam = copy.deepcopy(HuZhouXunJianPara.isUseMode)
        isUseModeParam['safetyCheckModule.isUse'] = True 
        isUseModeParam['safetyCheckModule.id'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModule t where t.moduleName ='%s'" % modelParam['safetyCheckModule.moduleName'])       
        ret = HuZhouXunJianIntf.isUseModel(param=isUseModeParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, "启用模板失败")
        Time.wait(1)
        # 停用模板
        isUseModeParam = copy.deepcopy(HuZhouXunJianPara.isUseMode)
        isUseModeParam['safetyCheckModule.isUse'] = False 
        isUseModeParam['safetyCheckModule.id'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModule t where t.moduleName ='%s'" %modelParam['safetyCheckModule.moduleName'] )       
        ret = HuZhouXunJianIntf.isNotUseModel(param=isUseModeParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, "停用模板失败")
        Time.wait(1)
        # 检查点
        checkUseModeParam = copy.deepcopy(HuZhouXunJianPara.checkIsUseMode) 
        checkUseModeParam['isUse'] = False
        checkUseModeParam['moduleName'] = modelParam['safetyCheckModule.moduleName']
        ret = HuZhouXunJianIntf.checkIsNotUseMode(param=checkUseModeParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')  
        self.assertTrue(ret, "新增的模板在列表中停用失败")    
         
         
#项目细则/分类
    def test_projectClass_014(self):
        """平安检查--模板设置--项目细则分类跳转 """ 
        # 新增模板
        modelParam = copy.deepcopy(HuZhouXunJianPara.addOrUpdateModelParam)
        modelParam['safetyCheckModule.moduleName'] = '2016年考核模板%s' % CommonUtil.createRandomString(6)
        modelParam['safetyCheckModule.checkYear'] = '2016'
        modelParam['safetyCheckModule.id'] = ''
        modelParam['safetyCheckModule.org.id'] = InitDefaultPara.orgInit['DftShiOrgId']
        modelParam['safetyCheckModule.checkObject'] = '20'
        modelParam['mode'] = 'add'
        ret = HuZhouXunJianIntf.addModel(param=modelParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, "新增的模板失败")
        Time.wait(1)
        #项目细则 
        isUseModeParam = copy.deepcopy(HuZhouXunJianPara.projectParam)
        isUseModeParam['safetyCheckModuleDetail.moduleId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModule t where t.moduleName ='%s'" % modelParam['safetyCheckModule.moduleName'])   
        ret= HuZhouXunJianIntf.projectClass(param=isUseModeParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')  
        self.assertTrue(ret, "新增项目细则跳转页面失败") 
        
#模板修改
    def test_updateModel_015(self): 
        """平安检查--模板设置--模板修改 """
        # 新增模板
        modelParam = copy.deepcopy(HuZhouXunJianPara.addOrUpdateModelParam)
        modelParam['safetyCheckModule.moduleName'] = '2016年考核模板%s' % CommonUtil.createRandomString(6)
        modelParam['safetyCheckModule.checkYear'] = '2016'
        modelParam['safetyCheckModule.id'] = ''
        modelParam['safetyCheckModule.org.id'] = InitDefaultPara.orgInit['DftShiOrgId']
        modelParam['safetyCheckModule.checkObject'] = '20'
        modelParam['mode'] = 'add'
        ret = HuZhouXunJianIntf.addModel(param=modelParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, "新增模板失败")
        Time.wait(1)
        #修改
        updateModelParam = copy.deepcopy(HuZhouXunJianPara.addOrUpdateModelParam)
        updateModelParam['safetyCheckModule.moduleName'] = '2016年考核模板%s' % CommonUtil.createRandomString(6)
        updateModelParam['safetyCheckModule.checkYear'] = '2016'
        updateModelParam['safetyCheckModule.id'] =CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModule t where t.moduleName ='%s'" %modelParam['safetyCheckModule.moduleName'] )
        updateModelParam['safetyCheckModule.org.id'] = InitDefaultPara.orgInit['DftShiOrgId']
        updateModelParam['safetyCheckModule.checkObject'] = '20'
        updateModelParam['mode'] = 'edit'
        ret = HuZhouXunJianIntf.updateModel(param=updateModelParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111') 
        self.assertTrue(ret, "修改模板失败")
        Time.wait(1) 
        # 检查点
        checkModelParam = copy.deepcopy(HuZhouXunJianPara.checkModelParam)
        checkModelParam['moduleName'] = updateModelParam['safetyCheckModule.moduleName']
        ret = HuZhouXunJianIntf.checkUpdateModel(param=checkModelParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, "修改模板在列表中不存在") 
              
#修改一级分类
    def test_updateFirstClass_016(self): 
        """平安检查--模板设置--新增模板--修改一级分类"""
        # 新增模板
        modelParam = copy.deepcopy(HuZhouXunJianPara.addOrUpdateModelParam)
        modelParam['safetyCheckModule.moduleName'] = '2016年考核模板%s' % CommonUtil.createRandomString(6)
        modelParam['safetyCheckModule.checkYear'] = '2016'
        modelParam['safetyCheckModule.id'] = ''
        modelParam['safetyCheckModule.org.id'] = InitDefaultPara.orgInit['DftShiOrgId']
        modelParam['safetyCheckModule.checkObject'] = '20'
        modelParam['mode'] = 'add'
        ret= HuZhouXunJianIntf.addModel(param=modelParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')   
        self.assertTrue(ret, "新增模板失败")
        Time.wait(1) 
        # 新增一级分类
        firstClassParam = copy.deepcopy(HuZhouXunJianPara.addClass) 
        firstClassParam['safetyCheckModuleDetail.moduleId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModule t where t.moduleName ='%s'" % modelParam['safetyCheckModule.moduleName'])
        firstClassParam['safetyCheckModuleDetail.displayName'] = '火灾隐患%s' % CommonUtil.createRandomString(6)
        firstClassParam['safetyCheckModuleDetail.score'] = '2'
        firstClassParam['safetyCheckModuleDetail.detailLevel']='1'
        firstClassParam['safetyCheckModuleDetail.isUse'] = True 
        ret = HuZhouXunJianIntf.addClass(level=firstClassParam['safetyCheckModuleDetail.detailLevel'],param=firstClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, "新增一级分类失败") 
        
        #修改一级分类
        updateFirstClassParam = copy.deepcopy(HuZhouXunJianPara.editClass)
        updateFirstClassParam['safetyCheckModuleDetail.id'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModuleDetail t where t.displayName ='%s'" % firstClassParam['safetyCheckModuleDetail.displayName'])       
        updateFirstClassParam['safetyCheckModuleDetail.parentId'] = ''
        updateFirstClassParam['safetyCheckModuleDetail.moduleId']=CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModule t where t.moduleName ='%s'" % modelParam['safetyCheckModule.moduleName'])
        updateFirstClassParam['safetyCheckModuleDetail.detailLevel']='1'
        updateFirstClassParam['safetyCheckModuleDetail.isLeaf']='false'
        updateFirstClassParam['safetyCheckModuleDetail.displayName']='修改一级分类%s'%CommonUtil.createRandomString(6)
        updateFirstClassParam['safetyCheckModuleDetail.score']='1'
        updateFirstClassParam['safetyCheckModuleDetail.isUse']=True
        updateFirstClassParam['mode']='edit'
        ret = HuZhouXunJianIntf.editFirstClass(level=updateFirstClassParam['safetyCheckModuleDetail.detailLevel'],param=updateFirstClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, "修改一级分类失败") 
        Time.wait(1)
        #检查点
        checkModelParam = copy.deepcopy(HuZhouXunJianPara.checkModelFirst)
        checkModelParam['displayName']=updateFirstClassParam['safetyCheckModuleDetail.displayName']
        ret = HuZhouXunJianIntf.checkEditClass(level=firstClassParam['safetyCheckModuleDetail.detailLevel'],moduleId=firstClassParam['safetyCheckModuleDetail.moduleId'],param=checkModelParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, "修改的一级分类没在列表中查找到")
        
#修改二级分类 
    def test_updateTwoClass_017(self): 
        """平安检查--模板设置--新增模板--修改二级分类"""
        # 新增模板
        modelParam = copy.deepcopy(HuZhouXunJianPara.addOrUpdateModelParam)
        modelParam['safetyCheckModule.moduleName'] = '2016年考核模板%s' % CommonUtil.createRandomString(6)
        modelParam['safetyCheckModule.checkYear'] = '2016'
        modelParam['safetyCheckModule.id'] = ''
        modelParam['safetyCheckModule.org.id'] = InitDefaultPara.orgInit['DftShiOrgId']
        modelParam['safetyCheckModule.checkObject'] = '20'
        modelParam['mode'] = 'add'
        ret = HuZhouXunJianIntf.addModel(param=modelParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')   
        self.assertTrue(ret, "新增模板失败")
        Time.wait(1)
        # 新增一级分类
        firstClassParam = copy.deepcopy(HuZhouXunJianPara.addClass) 
        firstClassParam['safetyCheckModuleDetail.moduleId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModule t where t.moduleName ='%s'" % modelParam['safetyCheckModule.moduleName'] )
        firstClassParam['safetyCheckModuleDetail.displayName'] = '火灾隐患%s' % CommonUtil.createRandomString(6)
        firstClassParam['safetyCheckModuleDetail.score'] = '2'
        firstClassParam['safetyCheckModuleDetail.detailLevel']='1'
        firstClassParam['safetyCheckModuleDetail.isUse'] = True 
        ret = HuZhouXunJianIntf.addClass(level=firstClassParam['safetyCheckModuleDetail.detailLevel'],param=firstClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, "新增一级分类失败")
        Time.wait(1)  
        # 新增二级分类       
        twoClassParam = copy.deepcopy(HuZhouXunJianPara.addClass)
        twoClassParam['safetyCheckModuleDetail.parentId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModuleDetail t where t.displayname = '%s'" % firstClassParam['safetyCheckModuleDetail.displayName'])
        twoClassParam['safetyCheckModuleDetail.moduleId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.moduleId from safetyCheckModuleDetail t where t.displayname = '%s'" % firstClassParam['safetyCheckModuleDetail.displayName'] )
        twoClassParam['safetyCheckModuleDetail.displayName'] = '火灾隐患项2级分类%s' % CommonUtil.createRandomString(6)
        twoClassParam['safetyCheckModuleDetail.score'] = '1'
        twoClassParam['safetyCheckModuleDetail.isUse'] = True
        twoClassParam['safetyCheckModuleDetail.detailLevel'] = '2'
        ret = HuZhouXunJianIntf.addClass(level=twoClassParam['safetyCheckModuleDetail.detailLevel'],param=twoClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, "新增二级分类失败") 
        Time.wait(1)
        
        #修改二级分类
        updateTwoClassParam = copy.deepcopy(HuZhouXunJianPara.editClass)
        updateTwoClassParam['safetyCheckModuleDetail.id'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModuleDetail t where t.displayName ='%s'" % twoClassParam['safetyCheckModuleDetail.displayName'])       
        updateTwoClassParam['safetyCheckModuleDetail.parentId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModuleDetail t where t.displayName ='%s'" % firstClassParam['safetyCheckModuleDetail.displayName'])
        updateTwoClassParam['safetyCheckModuleDetail.moduleId']=CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModule t where t.moduleName ='%s'" % modelParam['safetyCheckModule.moduleName'] )
        updateTwoClassParam['safetyCheckModuleDetail.detailLevel']='2'
        updateTwoClassParam['safetyCheckModuleDetail.isLeaf']='false'
        updateTwoClassParam['safetyCheckModuleDetail.displayName']='修改一级分类%s'%CommonUtil.createRandomString(6)
        updateTwoClassParam['safetyCheckModuleDetail.score']='1'
        updateTwoClassParam['safetyCheckModuleDetail.isUse']=True
        updateTwoClassParam['mode']='edit'
        ret = HuZhouXunJianIntf.editFirstClass(level=twoClassParam['safetyCheckModuleDetail.detailLevel'],param=updateTwoClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, "修改二级分类失败") 
        Time.wait(1)
        #检查点
        checkModelParam = copy.deepcopy(HuZhouXunJianPara.checkModelFirst)
        checkModelParam['displayName']=updateTwoClassParam['safetyCheckModuleDetail.displayName']
        ret = HuZhouXunJianIntf.checkEditClass(level=updateTwoClassParam['safetyCheckModuleDetail.detailLevel'],moduleId=updateTwoClassParam['safetyCheckModuleDetail.moduleId'],param=checkModelParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, "修改的二级分类没在列表中查找到")

#修改三级分类 (细则)
    def test_updateThreeClass_018(self): 
        """平安检查--模板设置--新增模板--修改三级分类"""
        # 新增模板
        modelParam = copy.deepcopy(HuZhouXunJianPara.addOrUpdateModelParam)
        modelParam['safetyCheckModule.moduleName'] = '2016年考核模板%s' % CommonUtil.createRandomString(6)
        modelParam['safetyCheckModule.checkYear'] = '2016'
        modelParam['safetyCheckModule.id'] = ''
        modelParam['safetyCheckModule.org.id'] = InitDefaultPara.orgInit['DftShiOrgId']
        modelParam['safetyCheckModule.checkObject'] = '20'
        modelParam['mode'] = 'add'
        ret = HuZhouXunJianIntf.addModel(param=modelParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')   
        self.assertTrue(ret, "新增模板失败")
        Time.wait(1)
        # 新增一级分类
        firstClassParam = copy.deepcopy(HuZhouXunJianPara.addClass) 
        firstClassParam['safetyCheckModuleDetail.moduleId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModule t where t.moduleName ='%s'" % modelParam['safetyCheckModule.moduleName'])
        firstClassParam['safetyCheckModuleDetail.displayName'] = '火灾隐患%s' % CommonUtil.createRandomString(6)
        firstClassParam['safetyCheckModuleDetail.score'] = '2'
        firstClassParam['safetyCheckModuleDetail.detailLevel']='1'
        firstClassParam['safetyCheckModuleDetail.isUse'] = True 
        ret = HuZhouXunJianIntf.addClass(level=firstClassParam['safetyCheckModuleDetail.detailLevel'],param=firstClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, "新增一级分类失败") 
        Time.wait(1) 
        # 新增二级分类       
        twoClassParam = copy.deepcopy(HuZhouXunJianPara.addClass)
        twoClassParam['safetyCheckModuleDetail.parentId'] =  CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetycheckmoduledetail t where t.displayname ='%s'" % firstClassParam['safetyCheckModuleDetail.displayName'])
        twoClassParam['safetyCheckModuleDetail.moduleId'] =CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModule t where t.moduleName ='%s'" %modelParam['safetyCheckModule.moduleName'])
        twoClassParam['safetyCheckModuleDetail.displayName'] = '火灾隐患项2级分类%s' % CommonUtil.createRandomString(6)
        twoClassParam['safetyCheckModuleDetail.score'] = '1'
        twoClassParam['safetyCheckModuleDetail.isUse'] = True
        twoClassParam['safetyCheckModuleDetail.detailLevel'] = '2'
        ret = HuZhouXunJianIntf.addClass(level=twoClassParam['safetyCheckModuleDetail.detailLevel'],param=twoClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, "新增二级分类失败") 
        Time.wait(1)
        #新增三级分类
        threeClassParam = copy.deepcopy(HuZhouXunJianPara.addClass)
        threeClassParam['safetyCheckModuleDetail.parentId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetycheckmoduledetail t where t.displayname = '%s'" %twoClassParam['safetyCheckModuleDetail.displayName'])
        threeClassParam['safetyCheckModuleDetail.moduleId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModule t where t.moduleName ='%s'" % modelParam['safetyCheckModule.moduleName'])
        threeClassParam['safetyCheckModuleDetail.displayName'] = '火灾隐患项3级分类%s' % CommonUtil.createRandomString(6)
        threeClassParam['safetyCheckModuleDetail.score'] = '1'
        threeClassParam['safetyCheckModuleDetail.isUse'] = True
        threeClassParam['safetyCheckModuleDetail.detailLevel']= '3'
        ret = HuZhouXunJianIntf.addClass(level=threeClassParam['safetyCheckModuleDetail.detailLevel'],param=threeClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, "新增三级分类失败") 
        Time.wait(1)
        #修改三级分类
        updateThreeClassParam = copy.deepcopy(HuZhouXunJianPara.editClass)
        updateThreeClassParam['safetyCheckModuleDetail.id'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModuleDetail t where t.displayName ='%s'"% threeClassParam['safetyCheckModuleDetail.displayName'])       
        updateThreeClassParam['safetyCheckModuleDetail.parentId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModuleDetail t where t.displayName ='%s'" % twoClassParam['safetyCheckModuleDetail.displayName'])
        updateThreeClassParam['safetyCheckModuleDetail.moduleId']=CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModule t where t.moduleName ='%s'" % modelParam['safetyCheckModule.moduleName'] )
        updateThreeClassParam['safetyCheckModuleDetail.detailLevel']='3'
        updateThreeClassParam['safetyCheckModuleDetail.isLeaf']='false'
        updateThreeClassParam['safetyCheckModuleDetail.displayName']='修改三级分类%s'%CommonUtil.createRandomString(6)
        updateThreeClassParam['safetyCheckModuleDetail.score']='1'
        updateThreeClassParam['safetyCheckModuleDetail.isUse']=True
        updateThreeClassParam['mode']='edit'
        ret = HuZhouXunJianIntf.editFirstClass(level=threeClassParam['safetyCheckModuleDetail.detailLevel'],param=updateThreeClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, "修改三级分类失败") 
        Time.wait(1)
        #检查点
        checkModelParam = copy.deepcopy(HuZhouXunJianPara.checkModelFirst)
        checkModelParam['displayName']=updateThreeClassParam['safetyCheckModuleDetail.displayName']
        ret = HuZhouXunJianIntf.checkEditClass(level=updateThreeClassParam['safetyCheckModuleDetail.detailLevel'],moduleId=updateThreeClassParam['safetyCheckModuleDetail.moduleId'],param=checkModelParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, "修改的三级分类没在列表中查找到")

#新增单位检查(基础信息检查--专项检查)
    def test_checkUnit_019(self):
        """平安检查--基础信息--添加检查  """
        HuZhouXunJianIntf.deleteAllSearchByIds_moudle() 
        # 新增模板
        modelParam = copy.deepcopy(HuZhouXunJianPara.addOrUpdateModelParam)
        modelParam['safetyCheckModule.moduleName'] = '2017年考核模板%s' % CommonUtil.createRandomString(6)
        modelParam['safetyCheckModule.checkYear'] = '2017'
        modelParam['safetyCheckModule.id'] = ''
        modelParam['safetyCheckModule.org.id'] = InitDefaultPara.orgInit['DftShiOrgId']
        modelParam['safetyCheckModule.checkObject'] = '20'
        modelParam['mode'] = 'add'
        ret = HuZhouXunJianIntf.addModel(param=modelParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')   
        self.assertTrue(ret, "新增模板失败")
        Time.wait(1)
        # 新增一级分类
        firstClassParam = copy.deepcopy(HuZhouXunJianPara.addClass) 
        firstClassParam['safetyCheckModuleDetail.moduleId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModule t where t.moduleName ='%s'" % modelParam['safetyCheckModule.moduleName'])
        firstClassParam['safetyCheckModuleDetail.displayName'] = '火灾隐患%s' % CommonUtil.createRandomString(6)
        firstClassParam['safetyCheckModuleDetail.score'] = '2' 
        firstClassParam['safetyCheckModuleDetail.detailLevel']='1'
        firstClassParam['safetyCheckModuleDetail.isLeaf']='false'
        firstClassParam['safetyCheckModuleDetail.isUse']=True
        ret = HuZhouXunJianIntf.addClass(level=firstClassParam['safetyCheckModuleDetail.detailLevel'], param=firstClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, "新增一级分类失败")
        Time.wait(1)
        # 新增二级分类       
        twoClassParam = copy.deepcopy(HuZhouXunJianPara.addClass)
        twoClassParam['safetyCheckModuleDetail.parentId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModuleDetail t where t.displayname = '%s'" % firstClassParam['safetyCheckModuleDetail.displayName'])
        twoClassParam['safetyCheckModuleDetail.moduleId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.moduleid from safetyCheckModuleDetail t where t.displayname = '%s'" % firstClassParam['safetyCheckModuleDetail.displayName'])
        twoClassParam['safetyCheckModuleDetail.displayName'] = '火灾隐患项2级分类%s' % CommonUtil.createRandomString(6)
        twoClassParam['safetyCheckModuleDetail.score'] = '1'
        twoClassParam['safetyCheckModuleDetail.detailLevel']='2'
        twoClassParam['safetyCheckModuleDetail.isLeaf']='false'
        twoClassParam['safetyCheckModuleDetail.isUse']=True
        ret = HuZhouXunJianIntf.addClass(level=twoClassParam['safetyCheckModuleDetail.detailLevel'],param=twoClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, "新增二级分类失败")
        Time.wait(1) 
        # 新增三级分类       
        threeClassParam = copy.deepcopy(HuZhouXunJianPara.addClass)
        threeClassParam['safetyCheckModuleDetail.parentId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModuleDetail t where t.displayname = '%s'" % twoClassParam['safetyCheckModuleDetail.displayName'])
        threeClassParam['safetyCheckModuleDetail.moduleId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.moduleid from safetyCheckModuleDetail t where t.displayname = '%s'" %twoClassParam['safetyCheckModuleDetail.displayName'])
        threeClassParam['safetyCheckModuleDetail.displayName'] = '火灾隐患项3级分类%s' % CommonUtil.createRandomString(6)
        threeClassParam['safetyCheckModuleDetail.score'] = '1'
        threeClassParam['safetyCheckModuleDetail.isUse'] = '1'
        threeClassParam['safetyCheckModuleDetail.detailLevel']='3'
        threeClassParam['safetyCheckModuleDetail.isInput']='true'
        threeClassParam['safetyCheckModuleDetail.isLeaf']='true'
        threeClassParam['safetyCheckModuleDetail.isUse']=True
        ret = HuZhouXunJianIntf.addClass(level=threeClassParam['safetyCheckModuleDetail.detailLevel'],param=threeClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, "新增三级分类失败") 
        Time.wait(1)
       
        # 启用模板
        isUseModeParam = copy.deepcopy(HuZhouXunJianPara.isUseMode)
        isUseModeParam['safetyCheckModule.isUse'] = True 
        isUseModeParam['safetyCheckModule.id'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModule t where t.moduleName ='%s'" % modelParam['safetyCheckModule.moduleName'])       
        ret = HuZhouXunJianIntf.isUseModel(param=isUseModeParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')         
        self.assertTrue(ret, "启用模板失败")
        Time.wait(1)
        #新增单位信息
        issueParam = copy.deepcopy(HuZhouXunJianPara.editOrAddObject) 
        issueParam['safetyCheckBasics.org.id'] = InitDefaultPara.orgInit['DftJieDaoOrgId']
        issueParam['safetyCheckBasics.companyName'] = '天阙科技05%s' % CommonUtil.createRandomString(6) 
        issueParam['safetyCheckBasics.companyAddr'] = '西城广场2'
        issueParam['safetyCheckBasics.companyType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='平安检查企业类型', displayName='规上企业')  
        issueParam['safetyCheckBasics.orgNo'] = '33'
        issueParam['safetyCheckBasics.id'] = ''
        issueParam['mode'] = 'add'
        issueParam['safetyCheckBasics.org.orgInternalCode'] = CommonIntf.getDbQueryResult(dbCommand="select t.orginternalcode from ORGANIZATIONS t where t.id = %s"%issueParam['safetyCheckBasics.org.id'])
        ret = HuZhouXunJianIntf.addsafetyCheckBasics(issueDict=issueParam,username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, '单位信息新增失败')
        Time.wait(1)
        #新增单位检查
        check_unitParam = copy.deepcopy(HuZhouXunJianPara.check_unitParam)
        check_unitParam['mode']='add'
        check_unitParam['safetyCheckInspection.safetyCheckBasics.id']=CommonIntf.getDbQueryResultList(dbCommand="select t.id from  safetycheckbasics t where t.companyname='%s'" % issueParam['safetyCheckBasics.companyName'])
        check_unitParam['safetyCheckInspection.safetyCheckBasics.org.id']=InitDefaultPara.orgInit['DftJieDaoOrgId']
        check_unitParam['safetyCheckInspection.safetyCheckBasics.companyName']=issueParam['safetyCheckBasics.companyName']
        check_unitParam['safetyCheckInspection.moduleDetailInspections[0].safetyCheckModuleDetail.id']=CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModuleDetail t where t.displayname = '%s'" % firstClassParam['safetyCheckModuleDetail.displayName'])
        check_unitParam['safetyCheckInspection.moduleDetailInspections[1].safetyCheckModuleDetail.id']=CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModuleDetail t where t.displayname = '%s'" % twoClassParam['safetyCheckModuleDetail.displayName']) 
        check_unitParam['safetyCheckInspection.moduleDetailInspections[2].safetyCheckModuleDetail.id']=CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModuleDetail t where t.displayname = '%s'" % threeClassParam['safetyCheckModuleDetail.displayName'])
       
#         ret = HuZhouXunJianIntf.checkUnit(param=check_unitParam,username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
#         self.assertTrue(ret, '进入检查页失败')
#         Time.wait(1)
        check_companyParam = copy.deepcopy(HuZhouXunJianPara.check_companyParam)
        check_companyParam['safetyCheckInspection.id']=''
        check_companyParam['safetyCheckInspection.checkNo']='15120795959595%s'% CommonUtil.createRandomString(6) 
        check_companyParam['safetyCheckInspection.org.id']=InitDefaultPara.orgInit['DftJieDaoOrgId']
        check_companyParam['safetyCheckInspection.safetyCheckBasics.id']=CommonIntf.getDbQueryResult(dbCommand="select t.id from  safetycheckbasics t where t.companyname='%s'" % issueParam['safetyCheckBasics.companyName'])
        check_companyParam['safetyCheckInspection.safetyCheckBasics.companyName']=issueParam['safetyCheckBasics.companyName']
        check_companyParam['safetyCheckInspection.isQualified']='false'
        check_companyParam['safetyCheckInspection.checkDate']=Time.getCurrentDate()
        check_companyParam['safetyCheckInspection.moduleDetailInspections[0].checkName']='其他22'
        check_companyParam['safetyCheckInspection.moduleDetailInspections[0].safetyCheckModuleDetail.id']=CommonIntf.getDbQueryResult(dbCommand="select t.id from safetyCheckModuleDetail t where t.displayname = '%s'" % threeClassParam['safetyCheckModuleDetail.displayName'])
        check_companyParam['safetyCheckInspection.moduleDetailInspections[0].checkType']='false'
        #风险等级
        check_companyParam['safetyCheckInspection.riskLevel.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='平安检查专项风险等级', displayName='一般')
        #检查类型
        check_companyParam['safetyCheckInspection.checkType.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='平安检查专项检查类型', displayName='市级')
        check_companyParam['safetyCheckInspection.rectificationDate']=Time.getCurrentDate()
        check_companyParam['safetyCheckInspection.checkUsers']=CommonIntf.getDbQueryResult(dbCommand="select t.id from users t where t.userName='" + InitDefaultPara.userInit['DftShiUser'] + "'")
        ret = HuZhouXunJianIntf.checkCompany(param=check_companyParam,username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, '添加单位检查失败')
        Time.wait(1)
        #检查点
        check_companyList = copy.deepcopy(HuZhouXunJianPara.companyName)
        check_companyList['companyName'] = issueParam['safetyCheckBasics.companyName']
#        print check_companyList['companyName']
        
        ret = HuZhouXunJianIntf.checkUnitCompany(param=check_companyList['companyName'],username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, '添加的单位检查没在列表中查找到')
        
#修改单位检查 
    def test_updateUnit_020(self):
        """平安检查--基础信息--修改专项检查  """  
        # 新增模板
        HuZhouXunJianIntf.deleteAllSearchByIds_moudle()
        modelParam = copy.deepcopy(HuZhouXunJianPara.addOrUpdateModelParam)
        modelParam['safetyCheckModule.moduleName'] = '2017年考核模板%s' % CommonUtil.createRandomString(6)
        modelParam['safetyCheckModule.checkYear'] = '2017'
        modelParam['safetyCheckModule.id'] = ''
        modelParam['safetyCheckModule.org.id'] = InitDefaultPara.orgInit['DftShiOrgId']
        modelParam['safetyCheckModule.checkObject'] = '20'
        modelParam['mode'] = 'add'
        ret = HuZhouXunJianIntf.addModel(param=modelParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')   
        self.assertTrue(ret, '新增模板失败') 
        Time.wait(1)
        # 新增一级分类
        firstClassParam = copy.deepcopy(HuZhouXunJianPara.addClass) 
        firstClassParam['safetyCheckModuleDetail.moduleId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModule t where t.moduleName ='%s'" % modelParam['safetyCheckModule.moduleName'])
        firstClassParam['safetyCheckModuleDetail.displayName'] = '火灾隐患%s' % CommonUtil.createRandomString(6)
        firstClassParam['safetyCheckModuleDetail.score'] = '2' 
        firstClassParam['safetyCheckModuleDetail.detailLevel']='1'
        firstClassParam['safetyCheckModuleDetail.isLeaf']='false'
        firstClassParam['safetyCheckModuleDetail.isUse']=True
        ret = HuZhouXunJianIntf.addClass(level=firstClassParam['safetyCheckModuleDetail.detailLevel'], param=firstClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, '新增一级分类失败')
        Time.wait(1) 
        # 新增二级分类       
        twoClassParam = copy.deepcopy(HuZhouXunJianPara.addClass)
        twoClassParam['safetyCheckModuleDetail.parentId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModuleDetail t where t.displayname = '%s'" % firstClassParam['safetyCheckModuleDetail.displayName'])
        twoClassParam['safetyCheckModuleDetail.moduleId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.moduleid from safetyCheckModuleDetail t where t.displayname = '%s'" % firstClassParam['safetyCheckModuleDetail.displayName'] )
        twoClassParam['safetyCheckModuleDetail.displayName'] = '火灾隐患项2级分类%s' % CommonUtil.createRandomString(6)
        twoClassParam['safetyCheckModuleDetail.score'] = '1'
        twoClassParam['safetyCheckModuleDetail.detailLevel']='2'
        twoClassParam['safetyCheckModuleDetail.isLeaf']='false'
        twoClassParam['safetyCheckModuleDetail.isUse']=True
        ret = HuZhouXunJianIntf.addClass(level=twoClassParam['safetyCheckModuleDetail.detailLevel'],param=twoClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, "新增二级分类失败") 
        Time.wait(1)
        # 新增三级分类       
        threeClassParam = copy.deepcopy(HuZhouXunJianPara.addClass)
        threeClassParam['safetyCheckModuleDetail.parentId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModuleDetail t where t.displayname = '%s'" % twoClassParam['safetyCheckModuleDetail.displayName'])
        threeClassParam['safetyCheckModuleDetail.moduleId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.moduleid from safetyCheckModuleDetail t where t.displayname = '%s'" % twoClassParam['safetyCheckModuleDetail.displayName'])
        threeClassParam['safetyCheckModuleDetail.displayName'] = '火灾隐患项3级分类%s' % CommonUtil.createRandomString(6)
        threeClassParam['safetyCheckModuleDetail.score'] = '1'
        threeClassParam['safetyCheckModuleDetail.isUse'] = '1'
        threeClassParam['safetyCheckModuleDetail.detailLevel']='3'
        threeClassParam['safetyCheckModuleDetail.isInput']='true'
        threeClassParam['safetyCheckModuleDetail.isLeaf']='true'
        threeClassParam['safetyCheckModuleDetail.isUse']=True
        ret = HuZhouXunJianIntf.addClass(level=threeClassParam['safetyCheckModuleDetail.detailLevel'],param=threeClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, "新增三级分类失败") 
        Time.wait(1)
       
        # 启用模板
        isUseModeParam = copy.deepcopy(HuZhouXunJianPara.isUseMode)
        isUseModeParam['safetyCheckModule.isUse'] = True 
        isUseModeParam['safetyCheckModule.id'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModule t where t.moduleName ='%s'" % modelParam['safetyCheckModule.moduleName'])       
        ret = HuZhouXunJianIntf.isUseModel(param=isUseModeParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')         
        self.assertTrue(ret, "启用模板失败")
        Time.wait(1)
        #新增单位信息
        issueParam = copy.deepcopy(HuZhouXunJianPara.editOrAddObject) 
        issueParam['safetyCheckBasics.org.id'] = InitDefaultPara.orgInit['DftJieDaoOrgId']
        issueParam['safetyCheckBasics.companyName'] = '天阙科技05%s' % CommonUtil.createRandomString(6) 
        issueParam['safetyCheckBasics.companyAddr'] = '西城广场2'
        issueParam['safetyCheckBasics.companyType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='平安检查企业类型', displayName='规上企业')  
        issueParam['safetyCheckBasics.orgNo'] = '33'
        issueParam['safetyCheckBasics.id'] = ''
        issueParam['mode'] = 'add'
        issueParam['safetyCheckBasics.org.orgInternalCode'] = CommonIntf.getDbQueryResult(dbCommand="select t.orginternalcode from ORGANIZATIONS t where t.id = %s"%issueParam['safetyCheckBasics.org.id'])
        ret = HuZhouXunJianIntf.addsafetyCheckBasics(issueDict=issueParam,username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, '单位信息新增失败')
        Time.wait(1)
        #新增单位检查
        check_companyParam = copy.deepcopy(HuZhouXunJianPara.check_companyParam)
        check_companyParam['safetyCheckInspection.id']=''
        check_companyParam['safetyCheckInspection.checkNo']='15120795959595%s'% CommonUtil.createRandomString(6) 
        check_companyParam['safetyCheckInspection.org.id']=InitDefaultPara.orgInit['DftJieDaoOrgId']
        check_companyParam['safetyCheckInspection.safetyCheckBasics.id']=CommonIntf.getDbQueryResult(dbCommand="select t.id from  safetycheckbasics t where t.companyname='%s'"% issueParam['safetyCheckBasics.companyName'])
        check_companyParam['safetyCheckInspection.safetyCheckBasics.companyName']=issueParam['safetyCheckBasics.companyName']
        check_companyParam['safetyCheckInspection.isQualified']='false'
        check_companyParam['safetyCheckInspection.checkDate']= Time.getCurrentDate()
        check_companyParam['safetyCheckInspection.moduleDetailInspections[0].checkName']='其他22'
        check_companyParam['safetyCheckInspection.moduleDetailInspections[0].safetyCheckModuleDetail.id']=CommonIntf.getDbQueryResult(dbCommand="select t.id from safetyCheckModuleDetail t where t.displayname = '%s'" % threeClassParam['safetyCheckModuleDetail.displayName'])
        check_companyParam['safetyCheckInspection.moduleDetailInspections[0].checkType']='false'
        #风险等级
        check_companyParam['safetyCheckInspection.riskLevel.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='平安检查专项风险等级', displayName='一般')
        #检查类型
        check_companyParam['safetyCheckInspection.checkType.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='平安检查专项检查类型', displayName='市级')
        check_companyParam['safetyCheckInspection.rectificationDate']=Time.getCurrentDate()
        check_companyParam['safetyCheckInspection.checkUsers']=CommonIntf.getDbQueryResult(dbCommand="select t.id from users t where t.userName='" + InitDefaultPara.userInit['DftShiUser'] + "'")
        ret = HuZhouXunJianIntf.checkCompany(param=check_companyParam,username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, '添加单位检查失败')  
        Time.wait(1)
        
        #修改单位检查
        check_companyParamUpdate = copy.deepcopy(HuZhouXunJianPara.check_companyParam)
        check_companyParamUpdate['safetyCheckInspection.id']=CommonIntf.getDbQueryResult(dbCommand="select t.id from  safetycheckinspection t where  t.checkNo='%s'" % check_companyParam['safetyCheckInspection.checkNo'])
        check_companyParamUpdate['safetyCheckInspection.checkNo']='15120795959595%s'% CommonUtil.createRandomString(6) 
        check_companyParamUpdate['safetyCheckInspection.org.id']=InitDefaultPara.orgInit['DftJieDaoOrgId']
        check_companyParamUpdate['safetyCheckInspection.safetyCheckBasics.id']=CommonIntf.getDbQueryResult(dbCommand="select t.id from  safetycheckbasics t where t.companyname='%s'" % issueParam['safetyCheckBasics.companyName'])
        check_companyParamUpdate['safetyCheckInspection.safetyCheckBasics.companyName']=issueParam['safetyCheckBasics.companyName']
        check_companyParamUpdate['safetyCheckInspection.isQualified']='false'
        check_companyParamUpdate['safetyCheckInspection.checkDate']=Time.getCurrentDate()
        check_companyParamUpdate['safetyCheckInspection.moduleDetailInspections[0].checkName']='555'
        check_companyParamUpdate['safetyCheckInspection.moduleDetailInspections[0].safetyCheckModuleDetail.id']=CommonIntf.getDbQueryResult(dbCommand="select t.id from safetyCheckModuleDetail t where t.displayname = '%s'" % threeClassParam['safetyCheckModuleDetail.displayName'])
        check_companyParamUpdate['safetyCheckInspection.moduleDetailInspections[0].checkType']='false'
        #风险等级
        check_companyParamUpdate['safetyCheckInspection.riskLevel.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='平安检查专项风险等级', displayName='一般')
        #检查类型
        check_companyParamUpdate['safetyCheckInspection.checkType.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='平安检查专项检查类型', displayName='市级')
        check_companyParamUpdate['safetyCheckInspection.rectificationDate']=Time.getCurrentDate()
        check_companyParamUpdate['safetyCheckInspection.checkUsers']=CommonIntf.getDbQueryResult(dbCommand="select t.id from users t where t.userName='" + InitDefaultPara.userInit['DftShiUser'] + "'")        
        ret = HuZhouXunJianIntf.updateUnit(param=check_companyParamUpdate,username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, '修改单位检查失败')         
        
        Time.wait(5)
        #检查点
        check_companyList = copy.deepcopy(HuZhouXunJianPara.companyName)
        check_companyList['companyName'] = issueParam['safetyCheckBasics.companyName']
        ret = HuZhouXunJianIntf.checkUnitCompany(param=check_companyList['companyName'],username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, '单位检查没在列表中查找到')
#专项检查高级搜索
    def test_searchUnit_021(self): 
        """平安检查--专项检查--高级搜索  """ 
        HuZhouXunJianIntf.deleteAllSearchByIds_moudle()
        # 新增模板
        modelParam = copy.deepcopy(HuZhouXunJianPara.addOrUpdateModelParam)
        modelParam['safetyCheckModule.moduleName'] = '2016年考核模板%s' % CommonUtil.createRandomString(6)
        modelParam['safetyCheckModule.checkYear'] = '2016'
        modelParam['safetyCheckModule.id'] = ''
        modelParam['safetyCheckModule.org.id'] = InitDefaultPara.orgInit['DftShiOrgId']
        modelParam['safetyCheckModule.checkObject'] = '20'
        modelParam['mode'] = 'add'
        ret = HuZhouXunJianIntf.addModel(param=modelParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')   
        self.assertTrue(ret, '新增模板失败')
        Time.wait(1)
        # 新增一级分类
        firstClassParam = copy.deepcopy(HuZhouXunJianPara.addClass) 
        firstClassParam['safetyCheckModuleDetail.moduleId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModule t where t.moduleName ='%s'" % modelParam['safetyCheckModule.moduleName'])
        firstClassParam['safetyCheckModuleDetail.displayName'] = '火灾隐患%s' % CommonUtil.createRandomString(6)
        firstClassParam['safetyCheckModuleDetail.score'] = '2' 
        firstClassParam['safetyCheckModuleDetail.detailLevel']='1'
        firstClassParam['safetyCheckModuleDetail.isLeaf']='false'
        firstClassParam['safetyCheckModuleDetail.isUse']=True
        ret = HuZhouXunJianIntf.addClass(level=firstClassParam['safetyCheckModuleDetail.detailLevel'], param=firstClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, '新增一级分类失败')
        Time.wait(1)
        # 新增二级分类       
        twoClassParam = copy.deepcopy(HuZhouXunJianPara.addClass)
        twoClassParam['safetyCheckModuleDetail.parentId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModuleDetail t where t.displayname = '%s'" % firstClassParam['safetyCheckModuleDetail.displayName'])
        twoClassParam['safetyCheckModuleDetail.moduleId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.moduleid from safetyCheckModuleDetail t where t.displayname = '%s'" % firstClassParam['safetyCheckModuleDetail.displayName'])
        twoClassParam['safetyCheckModuleDetail.displayName'] = '火灾隐患项2级分类%s' % CommonUtil.createRandomString(6)
        twoClassParam['safetyCheckModuleDetail.score'] = '1'
        twoClassParam['safetyCheckModuleDetail.detailLevel']='2'
        twoClassParam['safetyCheckModuleDetail.isLeaf']='false'
        twoClassParam['safetyCheckModuleDetail.isUse']=True
        ret = HuZhouXunJianIntf.addClass(level=twoClassParam['safetyCheckModuleDetail.detailLevel'],param=twoClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, "新增二级分类失败") 
        Time.wait(1)
        # 新增三级分类       
        threeClassParam = copy.deepcopy(HuZhouXunJianPara.addClass)
        threeClassParam['safetyCheckModuleDetail.parentId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModuleDetail t where t.displayname = '%s'" % twoClassParam['safetyCheckModuleDetail.displayName'])
        threeClassParam['safetyCheckModuleDetail.moduleId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.moduleid from safetyCheckModuleDetail t where t.displayname = '%s'" % twoClassParam['safetyCheckModuleDetail.displayName'])
        threeClassParam['safetyCheckModuleDetail.displayName'] = '火灾隐患项3级分类%s' % CommonUtil.createRandomString(6)
        threeClassParam['safetyCheckModuleDetail.score'] = '1'
        threeClassParam['safetyCheckModuleDetail.isUse'] = '1'
        threeClassParam['safetyCheckModuleDetail.detailLevel']='3'
        threeClassParam['safetyCheckModuleDetail.isInput']='true'
        threeClassParam['safetyCheckModuleDetail.isLeaf']='true'
        threeClassParam['safetyCheckModuleDetail.isUse']=True
        ret = HuZhouXunJianIntf.addClass(level=threeClassParam['safetyCheckModuleDetail.detailLevel'],param=threeClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, "新增三级分类失败") 
        Time.wait(1)
       
        # 启用模板
        isUseModeParam = copy.deepcopy(HuZhouXunJianPara.isUseMode)
        isUseModeParam['safetyCheckModule.isUse'] = True 
        isUseModeParam['safetyCheckModule.id'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModule t where t.moduleName ='%s'" % modelParam['safetyCheckModule.moduleName'])       
        ret = HuZhouXunJianIntf.isUseModel(param=isUseModeParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')         
        self.assertTrue(ret, "启用模板失败")
        Time.wait(1)
        #新增单位信息
        issueParam = copy.deepcopy(HuZhouXunJianPara.editOrAddObject) 
        issueParam['safetyCheckBasics.org.id'] = InitDefaultPara.orgInit['DftJieDaoOrgId']
        issueParam['safetyCheckBasics.companyName'] = '天阙科技05%s' % CommonUtil.createRandomString(6) 
        issueParam['safetyCheckBasics.companyAddr'] = '西城广场2'
        issueParam['safetyCheckBasics.companyType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='平安检查企业类型', displayName='规上企业')  
        issueParam['safetyCheckBasics.orgNo'] = '33'
        issueParam['safetyCheckBasics.id'] = ''
        issueParam['mode'] = 'add'
        issueParam['safetyCheckBasics.org.orgInternalCode'] = CommonIntf.getDbQueryResult(dbCommand="select t.orginternalcode from ORGANIZATIONS t where t.id = %s"%issueParam['safetyCheckBasics.org.id'])
        ret = HuZhouXunJianIntf.addsafetyCheckBasics(issueDict=issueParam,username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, '单位信息新增失败')
        Time.wait(1)
        #新增单位检查
        check_companyParam = copy.deepcopy(HuZhouXunJianPara.check_companyParam)
        check_companyParam['safetyCheckInspection.id']=''
        check_companyParam['safetyCheckInspection.checkNo']='15120795959595%s'% CommonUtil.createRandomString(6) 
        check_companyParam['safetyCheckInspection.org.id']=InitDefaultPara.orgInit['DftJieDaoOrgId']
        check_companyParam['safetyCheckInspection.safetyCheckBasics.id']=CommonIntf.getDbQueryResult(dbCommand="select t.id from  safetycheckbasics t where t.companyname='%s'" % issueParam['safetyCheckBasics.companyName'])
        check_companyParam['safetyCheckInspection.safetyCheckBasics.companyName']=issueParam['safetyCheckBasics.companyName']
        check_companyParam['safetyCheckInspection.isQualified']='false'
        check_companyParam['safetyCheckInspection.checkDate']=Time.getCurrentDate()
        check_companyParam['safetyCheckInspection.moduleDetailInspections[0].checkName']='其他22'
        check_companyParam['safetyCheckInspection.moduleDetailInspections[0].safetyCheckModuleDetail.id']=CommonIntf.getDbQueryResult(dbCommand="select t.id from safetyCheckModuleDetail t where t.displayname = '%s'" % threeClassParam['safetyCheckModuleDetail.displayName'])
        check_companyParam['safetyCheckInspection.moduleDetailInspections[0].checkType']='false'
        #风险等级
        check_companyParam['safetyCheckInspection.riskLevel.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='平安检查专项风险等级', displayName='一般')
        #检查类型
        check_companyParam['safetyCheckInspection.checkType.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='平安检查专项检查类型', displayName='市级')
        check_companyParam['safetyCheckInspection.rectificationDate']='2015-12-01'
        check_companyParam['safetyCheckInspection.checkUsers']=CommonIntf.getDbQueryResult(dbCommand="select t.id from users t where t.userName='" + InitDefaultPara.userInit['DftShiUser'] + "'")
       
        ret = HuZhouXunJianIntf.checkCompany(param=check_companyParam,username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, '添加单位检查失败') 
        Time.wait(1)
        #新增单位检查
        check_companyParam2 = copy.deepcopy(HuZhouXunJianPara.check_companyParam)
        check_companyParam2['safetyCheckInspection.id']=''
        check_companyParam2['safetyCheckInspection.checkNo']='15120795959595%s'% CommonUtil.createRandomString(6) 
        check_companyParam2['safetyCheckInspection.org.id']=InitDefaultPara.orgInit['DftJieDaoOrgId']
        check_companyParam2['safetyCheckInspection.safetyCheckBasics.id']=CommonIntf.getDbQueryResult(dbCommand="select t.id from  safetycheckbasics t where t.companyname='%s'" % issueParam['safetyCheckBasics.companyName'])
        check_companyParam2['safetyCheckInspection.safetyCheckBasics.companyName']=issueParam['safetyCheckBasics.companyName']
        check_companyParam2['safetyCheckInspection.isQualified']='false'
        check_companyParam2['safetyCheckInspection.checkDate']=Time.getCurrentDate()
        check_companyParam2['safetyCheckInspection.moduleDetailInspections[0].checkName']='345'
        check_companyParam2['safetyCheckInspection.moduleDetailInspections[0].safetyCheckModuleDetail.id']=CommonIntf.getDbQueryResult(dbCommand="select t.id from safetyCheckModuleDetail t where t.displayname = '%s'" % threeClassParam['safetyCheckModuleDetail.displayName'])
        check_companyParam2['safetyCheckInspection.moduleDetailInspections[0].checkType']='false'
        #风险等级
        check_companyParam2['safetyCheckInspection.riskLevel.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='平安检查专项风险等级', displayName='一般')
        #检查类型
        check_companyParam2['safetyCheckInspection.checkType.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='平安检查专项检查类型', displayName='市级')
        check_companyParam2['safetyCheckInspection.rectificationDate']=Time.getCurrentDate()
        check_companyParam2['safetyCheckInspection.checkUsers']=CommonIntf.getDbQueryResult(dbCommand="select t.id from users t where t.userName='%s'" % InitDefaultPara.userInit['DftShiUser'])
       
        ret = HuZhouXunJianIntf.checkCompany(param=check_companyParam2,username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, '添加单位检查失败')
        Time.wait(2)
        #第一种情况:根据企业名称搜索 
        issueParamSearch = copy.deepcopy(HuZhouXunJianPara.checkCompanyUnit) 
        issueParamSearch['safetyCheckInspectionVo.safetyCheckBasics.companyName'] = check_companyParam['safetyCheckInspection.safetyCheckBasics.companyName']
        ret = HuZhouXunJianIntf.searchCheckCompany(issueParamSearch, username=InitDefaultPara.userInit['DftShiUser'], password='11111111');
        self.assertTrue(ret, '信息搜索失败')
        Time.wait(1)
        ret = HuZhouXunJianIntf.searchCompanyByMatch(issueParamSearch, check_companyParam2['safetyCheckInspection.safetyCheckBasics.companyName'], username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertFalse(ret, '不存在的数据匹配失败')
        Time.wait(1)
        # 第二种情况:根据风险等级,企业名称
        issueParamSearch = copy.deepcopy(HuZhouXunJianPara.checkCompanyUnit) 
        issueParamSearch['safetyCheckInspectionVo.safetyCheckBasics.companyName'] = check_companyParam['safetyCheckInspection.safetyCheckBasics.companyName']
        issueParamSearch['safetyCheckInspectionVo.riskLevel.id'] = check_companyParam['safetyCheckInspection.riskLevel.id']
        # 检验是否搜索成功
        ret = HuZhouXunJianIntf.searchCheckCompany(issueParamSearch, username=InitDefaultPara.userInit['DftShiUser'], password='11111111');
        self.assertTrue(ret, '信息搜索失败')
        Time.wait(1)
        # 输入不存在的数据验证是否能查到
        ret = HuZhouXunJianIntf.searchCompanyByMatch(issueParamSearch, check_companyParam2['safetyCheckInspection.riskLevel.id'], username=Global.PingAnJianSheUser, password=Global.PingAnJianShePass)
        self.assertFalse(ret, '不存在的数据匹配失败')
        Time.wait(1)
        # 第三种情况:根据风险等级,企业名称，检查类型
        issueParamSearch = copy.deepcopy(HuZhouXunJianPara.checkCompanyUnit) 
        issueParamSearch['safetyCheckInspectionVo.safetyCheckBasics.companyName'] = check_companyParam['safetyCheckInspection.safetyCheckBasics.companyName']
        issueParamSearch['safetyCheckInspectionVo.riskLevel.id'] = check_companyParam['safetyCheckInspection.riskLevel.id']
        issueParamSearch['safetyCheckInspectionVo.checkType.id']=check_companyParam['safetyCheckInspection.checkType.id']
        # 检验是否搜索成功
        ret = HuZhouXunJianIntf.searchCheckCompany(issueParamSearch, username=InitDefaultPara.userInit['DftShiUser'], password='11111111');
        self.assertTrue(ret, '信息搜索失败')
        Time.wait(1)
        # 输入不存在的数据验证是否能查到
        ret = HuZhouXunJianIntf.searchCompanyByMatch(issueParamSearch, check_companyParam2['safetyCheckInspection.checkType.id'], username=Global.PingAnJianSheUser, password=Global.PingAnJianShePass)
        self.assertFalse(ret, '不存在的数据匹配失败')

#模板单条删除
    def test_deleteUnit_022(self): 
        """平安检查--模板设置--模板单条删除  """
        # 新增模板
        modelParam = copy.deepcopy(HuZhouXunJianPara.addOrUpdateModelParam)
        modelParam['safetyCheckModule.moduleName'] = '2016年考核模板%s' % CommonUtil.createRandomString(6)
        modelParam['safetyCheckModule.checkYear'] = '2016'
        modelParam['safetyCheckModule.id'] = ''
        modelParam['safetyCheckModule.org.id'] = InitDefaultPara.orgInit['DftShiOrgId']
        modelParam['safetyCheckModule.checkObject'] = '20'
        modelParam['mode'] = 'add'
        ret = HuZhouXunJianIntf.addModel(param=modelParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')   
        self.assertTrue(ret, '新增模板失败')
        Time.wait(1)
        # 新增一级分类
        firstClassParam = copy.deepcopy(HuZhouXunJianPara.addClass) 
        firstClassParam['safetyCheckModuleDetail.moduleId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModule t where t.moduleName ='%s'" % modelParam['safetyCheckModule.moduleName'])
        firstClassParam['safetyCheckModuleDetail.displayName'] = '火灾隐患%s' % CommonUtil.createRandomString(6)
        firstClassParam['safetyCheckModuleDetail.score'] = '2' 
        firstClassParam['safetyCheckModuleDetail.detailLevel']='1'
        firstClassParam['safetyCheckModuleDetail.isLeaf']='false'
        firstClassParam['safetyCheckModuleDetail.isUse']=True
        ret = HuZhouXunJianIntf.addClass(level=firstClassParam['safetyCheckModuleDetail.detailLevel'], param=firstClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, '新增一级分类失败')
        Time.wait(1)
        # 新增二级分类       
        twoClassParam = copy.deepcopy(HuZhouXunJianPara.addClass)
        twoClassParam['safetyCheckModuleDetail.parentId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModuleDetail t where t.displayname = '%s'" % firstClassParam['safetyCheckModuleDetail.displayName'])
        twoClassParam['safetyCheckModuleDetail.moduleId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.moduleid from safetyCheckModuleDetail t where t.displayname = '%s'" % firstClassParam['safetyCheckModuleDetail.displayName'])
        twoClassParam['safetyCheckModuleDetail.displayName'] = '火灾隐患项2级分类%s' % CommonUtil.createRandomString(6)
        twoClassParam['safetyCheckModuleDetail.score'] = '1'
        twoClassParam['safetyCheckModuleDetail.detailLevel']='2'
        twoClassParam['safetyCheckModuleDetail.isLeaf']='false'
        twoClassParam['safetyCheckModuleDetail.isUse']=True
        ret = HuZhouXunJianIntf.addClass(level=twoClassParam['safetyCheckModuleDetail.detailLevel'],param=twoClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, "新增二级分类失败") 
        Time.wait(1)
        # 新增三级分类       
        threeClassParam = copy.deepcopy(HuZhouXunJianPara.addClass)
        threeClassParam['safetyCheckModuleDetail.parentId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModuleDetail t where t.displayname = '%s'" % twoClassParam['safetyCheckModuleDetail.displayName'])
        threeClassParam['safetyCheckModuleDetail.moduleId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.moduleid from safetyCheckModuleDetail t where t.displayname = '%s'" % twoClassParam['safetyCheckModuleDetail.displayName'])
        threeClassParam['safetyCheckModuleDetail.displayName'] = '火灾隐患项3级分类%s' % CommonUtil.createRandomString(6)
        threeClassParam['safetyCheckModuleDetail.score'] = '1'
        threeClassParam['safetyCheckModuleDetail.isUse'] = '1'
        threeClassParam['safetyCheckModuleDetail.detailLevel']='3'
        threeClassParam['safetyCheckModuleDetail.isInput']='true'
        threeClassParam['safetyCheckModuleDetail.isLeaf']='true'
        threeClassParam['safetyCheckModuleDetail.isUse']=True
        ret = HuZhouXunJianIntf.addClass(level=threeClassParam['safetyCheckModuleDetail.detailLevel'],param=threeClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, "新增三级分类失败")  
        Time.wait(1)
        idsParam = copy.deepcopy(HuZhouXunJianPara.moudleDelete) 
        idsParam['safetyCheckModule.id'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetycheckmodule t where t.modulename='" + modelParam['safetyCheckModule.moduleName'] + "'")
        ret = HuZhouXunJianIntf.deleteById_moudle(issueDict=idsParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, "模板删除失败")
        Time.wait(1)
        # 检查点
        checkModelParam = copy.deepcopy(HuZhouXunJianPara.checkModelParam)
        checkModelParam['moduleName'] = modelParam['safetyCheckModule.moduleName']
        # #检查是否删除成功
        ret = HuZhouXunJianIntf.checkAddModel(param=checkModelParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertFalse(ret, '已删除的模板在列表中没找到')
        
# ## 批量删除(模板) 系统中没有模板批量删除
#     def deleteByMouble_23 (self): 
#         """平安检查--模板设置--模板批量删除  """
#         HuZhouXunJianIntf.deleteAllSearchByIds_moudle()
#         # #检查点
#         ret = HuZhouXunJianIntf.searchMouble_check()
#         self.assertTrue(ret, '模板批量删除失败')
          
#专项检查单条删除
    def test_delete_check_024(self): 
        """平安检查--专项检查--专项检查单条删除  """ 
        HuZhouXunJianIntf.deleteAllSearchByIds_moudle() 
        # 新增模板
        modelParam = copy.deepcopy(HuZhouXunJianPara.addOrUpdateModelParam)
        modelParam['safetyCheckModule.moduleName'] = '2016年考核模板%s' % CommonUtil.createRandomString(6)
        modelParam['safetyCheckModule.checkYear'] = '2016'
        modelParam['safetyCheckModule.id'] = ''
        modelParam['safetyCheckModule.org.id'] = InitDefaultPara.orgInit['DftShiOrgId']
        modelParam['safetyCheckModule.checkObject'] = '20'
        modelParam['mode'] = 'add'
        ret = HuZhouXunJianIntf.addModel(param=modelParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')   
        self.assertTrue(ret, '新增模板失败')
        Time.wait(1)
        # 新增一级分类
        firstClassParam = copy.deepcopy(HuZhouXunJianPara.addClass) 
        firstClassParam['safetyCheckModuleDetail.moduleId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModule t where t.moduleName ='%s'" % modelParam['safetyCheckModule.moduleName'] )
        firstClassParam['safetyCheckModuleDetail.displayName'] = '火灾隐患%s' % CommonUtil.createRandomString(6)
        firstClassParam['safetyCheckModuleDetail.score'] = '2' 
        firstClassParam['safetyCheckModuleDetail.detailLevel']='1'
        firstClassParam['safetyCheckModuleDetail.isLeaf']='false'
        firstClassParam['safetyCheckModuleDetail.isUse']=True
        ret = HuZhouXunJianIntf.addClass(level=firstClassParam['safetyCheckModuleDetail.detailLevel'], param=firstClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, '新增一级分类失败')
        Time.wait(1)
        # 新增二级分类       
        twoClassParam = copy.deepcopy(HuZhouXunJianPara.addClass)
        twoClassParam['safetyCheckModuleDetail.parentId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModuleDetail t where t.displayname = '%s'" % firstClassParam['safetyCheckModuleDetail.displayName'])
        twoClassParam['safetyCheckModuleDetail.moduleId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.moduleid from safetyCheckModuleDetail t where t.displayname = '%s'" % firstClassParam['safetyCheckModuleDetail.displayName'])
        twoClassParam['safetyCheckModuleDetail.displayName'] = '火灾隐患项2级分类%s' % CommonUtil.createRandomString(6)
        twoClassParam['safetyCheckModuleDetail.score'] = '1'
        twoClassParam['safetyCheckModuleDetail.detailLevel']='2'
        twoClassParam['safetyCheckModuleDetail.isLeaf']='false'
        twoClassParam['safetyCheckModuleDetail.isUse']=True
        ret = HuZhouXunJianIntf.addClass(level=twoClassParam['safetyCheckModuleDetail.detailLevel'],param=twoClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, "新增二级分类失败")
        Time.wait(1) 
        # 新增三级分类       
        threeClassParam = copy.deepcopy(HuZhouXunJianPara.addClass)
        threeClassParam['safetyCheckModuleDetail.parentId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModuleDetail t where t.displayname = '%s'" % twoClassParam['safetyCheckModuleDetail.displayName'] )
        threeClassParam['safetyCheckModuleDetail.moduleId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.moduleid from safetyCheckModuleDetail t where t.displayname = '%s'" % twoClassParam['safetyCheckModuleDetail.displayName'] )
        threeClassParam['safetyCheckModuleDetail.displayName'] = '火灾隐患项3级分类%s' % CommonUtil.createRandomString(6)
        threeClassParam['safetyCheckModuleDetail.score'] = '1'
        threeClassParam['safetyCheckModuleDetail.isUse'] = '1'
        threeClassParam['safetyCheckModuleDetail.detailLevel']='3'
        threeClassParam['safetyCheckModuleDetail.isInput']='true'
        threeClassParam['safetyCheckModuleDetail.isLeaf']='true'
        threeClassParam['safetyCheckModuleDetail.isUse']=True
        ret = HuZhouXunJianIntf.addClass(level=threeClassParam['safetyCheckModuleDetail.detailLevel'],param=threeClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, "新增三级分类失败") 
        Time.wait(1)
       
        # 启用模板
        isUseModeParam = copy.deepcopy(HuZhouXunJianPara.isUseMode)
        isUseModeParam['safetyCheckModule.isUse'] = True 
        isUseModeParam['safetyCheckModule.id'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModule t where t.moduleName ='%s'" % modelParam['safetyCheckModule.moduleName'])       
        ret = HuZhouXunJianIntf.isUseModel(param=isUseModeParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')         
        self.assertTrue(ret, "启用模板失败")
        Time.wait(1)
        #新增单位信息
        issueParam = copy.deepcopy(HuZhouXunJianPara.editOrAddObject) 
        issueParam['safetyCheckBasics.org.id'] = InitDefaultPara.orgInit['DftJieDaoOrgId']
        issueParam['safetyCheckBasics.companyName'] = '天阙科技05%s' % CommonUtil.createRandomString(6) 
        issueParam['safetyCheckBasics.companyAddr'] = '西城广场2'
        issueParam['safetyCheckBasics.companyType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='平安检查企业类型', displayName='规上企业')  
        issueParam['safetyCheckBasics.orgNo'] = '33'
        issueParam['safetyCheckBasics.id'] = ''
        issueParam['mode'] = 'add'
        issueParam['safetyCheckBasics.org.orgInternalCode'] = CommonIntf.getDbQueryResult(dbCommand="select t.orginternalcode from ORGANIZATIONS t where t.id = %s"%issueParam['safetyCheckBasics.org.id'])
        ret = HuZhouXunJianIntf.addsafetyCheckBasics(issueDict=issueParam,username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, '单位信息新增失败')
        Time.wait(1)
        #新增单位检查
        check_companyParam = copy.deepcopy(HuZhouXunJianPara.check_companyParam)
        check_companyParam['safetyCheckInspection.id']=''
        check_companyParam['safetyCheckInspection.checkNo']='15120795959595%s'% CommonUtil.createRandomString(6) 
        check_companyParam['safetyCheckInspection.org.id']=InitDefaultPara.orgInit['DftJieDaoOrgId']
        check_companyParam['safetyCheckInspection.safetyCheckBasics.id']=CommonIntf.getDbQueryResult(dbCommand="select t.id from  safetycheckbasics t where t.companyname='%s'" %issueParam['safetyCheckBasics.companyName'])
        check_companyParam['safetyCheckInspection.safetyCheckBasics.companyName']=issueParam['safetyCheckBasics.companyName']
        check_companyParam['safetyCheckInspection.isQualified']='false'
        check_companyParam['safetyCheckInspection.checkDate']=Time.getCurrentDate()
        check_companyParam['safetyCheckInspection.moduleDetailInspections[0].checkName']='其他22'
        check_companyParam['safetyCheckInspection.moduleDetailInspections[0].safetyCheckModuleDetail.id']=CommonIntf.getDbQueryResult(dbCommand="select t.id from safetyCheckModuleDetail t where t.displayname = '%s'" % threeClassParam['safetyCheckModuleDetail.displayName'] )
        check_companyParam['safetyCheckInspection.moduleDetailInspections[0].checkType']='false'
        #风险等级
        check_companyParam['safetyCheckInspection.riskLevel.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='平安检查专项风险等级', displayName='一般')
        #检查类型
        check_companyParam['safetyCheckInspection.checkType.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='平安检查专项检查类型', displayName='市级')
        check_companyParam['safetyCheckInspection.rectificationDate']=Time.getCurrentDate()
        check_companyParam['safetyCheckInspection.checkUsers']=CommonIntf.getDbQueryResult(dbCommand="select t.id from users t where t.userName='%s'" % InitDefaultPara.userInit['DftShiUser'])
       
        ret = HuZhouXunJianIntf.checkCompany(param=check_companyParam,username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, '添加单位检查失败') 
        Time.wait(1)
        
        idsParam = copy.deepcopy(HuZhouXunJianPara.HuZhouXunJian_ids) 
        idsParam['ids'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from  safetycheckinspection t where  t.checkNo='%s'" % check_companyParam['safetyCheckInspection.checkNo'])
        ret = HuZhouXunJianIntf.deleteById_check(issueDict=idsParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
        self.assertTrue(ret, '单位检查删除失败')
        Time.wait(1)
        #检查点
        issueParamSearch = copy.deepcopy(HuZhouXunJianPara.checkCompanyUnit) 
        issueParamSearch['safetyCheckInspectionVo.safetyCheckBasics.companyName'] = check_companyParam['safetyCheckInspection.safetyCheckBasics.companyName']
        ret = HuZhouXunJianIntf.searchCheckCompany(issueParamSearch, username=InitDefaultPara.userInit['DftShiUser'], password='11111111');
        self.assertFalse(ret, '删除的单位检查在列表中没找到')
         
# # 批量删除(专项检查)
#     #intf代码未提交
#     def deleteBycheck_025 (self): 
#         """专项检查批量删除"""
#         # 新增模板
#         modelParam = copy.deepcopy(HuZhouXunJianPara.addOrUpdateModelParam)
#         modelParam['safetyCheckModule.moduleName'] = '2016年考核模板%s' % CommonUtil.createRandomString(6)
#         modelParam['safetyCheckModule.checkYear'] = '2016'
#         modelParam['safetyCheckModule.id'] = ''
#         modelParam['safetyCheckModule.org.id'] = InitDefaultPara.orgInit['DftShiOrgId']
#         modelParam['safetyCheckModule.checkObject'] = '20'
#         modelParam['mode'] = 'add'
#         ret = HuZhouXunJianIntf.addModel(param=modelParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')   
#         self.assertTrue(ret, '新增模板失败')
#         Time.wait(1)
#         # 新增一级分类
#         firstClassParam = copy.deepcopy(HuZhouXunJianPara.addClass) 
#         firstClassParam['safetyCheckModuleDetail.moduleId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModule t where t.moduleName ='%s'" % modelParam['safetyCheckModule.moduleName'] )
#         firstClassParam['safetyCheckModuleDetail.displayName'] = '火灾隐患%s' % CommonUtil.createRandomString(6)
#         firstClassParam['safetyCheckModuleDetail.score'] = '2' 
#         firstClassParam['safetyCheckModuleDetail.detailLevel']='1'
#         firstClassParam['safetyCheckModuleDetail.isLeaf']='false'
#         firstClassParam['safetyCheckModuleDetail.isUse']=True
#         ret = HuZhouXunJianIntf.addClass(level=firstClassParam['safetyCheckModuleDetail.detailLevel'], param=firstClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
#         self.assertTrue(ret, '新增一级分类失败')
#         Time.wait(1)
#         # 新增二级分类       
#         twoClassParam = copy.deepcopy(HuZhouXunJianPara.addClass)
#         twoClassParam['safetyCheckModuleDetail.parentId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModuleDetail t where t.displayname = '%s'" % firstClassParam['safetyCheckModuleDetail.displayName'])
#         twoClassParam['safetyCheckModuleDetail.moduleId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.moduleid from safetyCheckModuleDetail t where t.displayname = '%s'" % firstClassParam['safetyCheckModuleDetail.displayName'])
#         twoClassParam['safetyCheckModuleDetail.displayName'] = '火灾隐患项2级分类%s' % CommonUtil.createRandomString(6)
#         twoClassParam['safetyCheckModuleDetail.score'] = '1'
#         twoClassParam['safetyCheckModuleDetail.detailLevel']='2'
#         twoClassParam['safetyCheckModuleDetail.isLeaf']='false'
#         twoClassParam['safetyCheckModuleDetail.isUse']=True
#         ret = HuZhouXunJianIntf.addClass(level=twoClassParam['safetyCheckModuleDetail.detailLevel'],param=twoClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
#         self.assertTrue(ret, "新增二级分类失败")
#         Time.wait(1) 
#         # 新增三级分类       
#         threeClassParam = copy.deepcopy(HuZhouXunJianPara.addClass)
#         threeClassParam['safetyCheckModuleDetail.parentId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModuleDetail t where t.displayname = '%s'" % twoClassParam['safetyCheckModuleDetail.displayName'] )
#         threeClassParam['safetyCheckModuleDetail.moduleId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.moduleid from safetyCheckModuleDetail t where t.displayname = '%s'" % twoClassParam['safetyCheckModuleDetail.displayName'] )
#         threeClassParam['safetyCheckModuleDetail.displayName'] = '火灾隐患项3级分类%s' % CommonUtil.createRandomString(6)
#         threeClassParam['safetyCheckModuleDetail.score'] = '1'
#         threeClassParam['safetyCheckModuleDetail.isUse'] = '1'
#         threeClassParam['safetyCheckModuleDetail.detailLevel']='3'
#         threeClassParam['safetyCheckModuleDetail.isInput']='true'
#         threeClassParam['safetyCheckModuleDetail.isLeaf']='true'
#         threeClassParam['safetyCheckModuleDetail.isUse']=True
#         ret = HuZhouXunJianIntf.addClass(level=threeClassParam['safetyCheckModuleDetail.detailLevel'],param=threeClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
#         self.assertTrue(ret, "新增三级分类失败") 
#         Time.wait(1)
#        
#         # 启用模板
#         isUseModeParam = copy.deepcopy(HuZhouXunJianPara.isUseMode)
#         isUseModeParam['safetyCheckModule.isUse'] = True 
#         isUseModeParam['safetyCheckModule.id'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModule t where t.moduleName ='%s'" % modelParam['safetyCheckModule.moduleName'])       
#         ret = HuZhouXunJianIntf.isUseModel(param=isUseModeParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')         
#         self.assertTrue(ret, "启用模板失败")
#         Time.wait(1)
#         #新增单位信息
#         issueParam = copy.deepcopy(HuZhouXunJianPara.editOrAddObject) 
#         issueParam['safetyCheckBasics.org.id'] = InitDefaultPara.orgInit['DftJieDaoOrgId']
#         issueParam['safetyCheckBasics.companyName'] = '天阙科技05%s' % CommonUtil.createRandomString(6) 
#         issueParam['safetyCheckBasics.companyAddr'] = '西城广场2'
#         issueParam['safetyCheckBasics.companyType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='平安检查企业类型', displayName='规上企业')  
#         issueParam['safetyCheckBasics.orgNo'] = '33'
#         issueParam['safetyCheckBasics.id'] = ''
#         issueParam['mode'] = 'add'
#         issueParam['safetyCheckBasics.org.orgInternalCode'] = CommonIntf.getDbQueryResult(dbCommand="select t.orginternalcode from ORGANIZATIONS t where t.id = %s"%issueParam['safetyCheckBasics.org.id'])
#         ret = HuZhouXunJianIntf.addsafetyCheckBasics(issueDict=issueParam,username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
#         self.assertTrue(ret, '单位信息新增失败')
#         Time.wait(1)
#         #新增单位检查
#         check_companyParam = copy.deepcopy(HuZhouXunJianPara.check_companyParam)
#         check_companyParam['safetyCheckInspection.id']=''
#         check_companyParam['safetyCheckInspection.checkNo']='15120795959595%s'% CommonUtil.createRandomString(6) 
#         check_companyParam['safetyCheckInspection.org.id']=InitDefaultPara.orgInit['DftJieDaoOrgId']
#         check_companyParam['safetyCheckInspection.safetyCheckBasics.id']=CommonIntf.getDbQueryResult(dbCommand="select t.id from  safetycheckbasics t where t.companyname='%s'" %issueParam['safetyCheckBasics.companyName'])
#         check_companyParam['safetyCheckInspection.safetyCheckBasics.companyName']=issueParam['safetyCheckBasics.companyName']
#         check_companyParam['safetyCheckInspection.isQualified']='false'
#         check_companyParam['safetyCheckInspection.checkDate']=Time.getCurrentDate()
#         check_companyParam['safetyCheckInspection.moduleDetailInspections[0].checkName']='其他22'
#         check_companyParam['safetyCheckInspection.moduleDetailInspections[0].safetyCheckModuleDetail.id']=CommonIntf.getDbQueryResult(dbCommand="select t.id from safetyCheckModuleDetail t where t.displayname = '%s'" % threeClassParam['safetyCheckModuleDetail.displayName'] )
#         check_companyParam['safetyCheckInspection.moduleDetailInspections[0].checkType']='false'
#         #风险等级
#         check_companyParam['safetyCheckInspection.riskLevel.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='平安检查专项风险等级', displayName='一般')
#         #检查类型
#         check_companyParam['safetyCheckInspection.checkType.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='平安检查专项检查类型', displayName='市级')
#         check_companyParam['safetyCheckInspection.rectificationDate']=Time.getCurrentDate()
#         check_companyParam['safetyCheckInspection.checkUsers']=CommonIntf.getDbQueryResult(dbCommand="select t.id from users t where t.userName='%s'" % InitDefaultPara.userInit['DftShiUser'])
#        
#         ret = HuZhouXunJianIntf.checkCompany(param=check_companyParam,username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
#         self.assertTrue(ret, '添加单位检查失败') 
#         Time.wait(1)
#         
#         #新增单位检查
#         check_companyParam2 = copy.deepcopy(HuZhouXunJianPara.check_companyParam)
#         check_companyParam2['safetyCheckInspection.id']=''
#         check_companyParam2['safetyCheckInspection.checkNo']='15120795959595%s'% CommonUtil.createRandomString(6) 
#         check_companyParam2['safetyCheckInspection.org.id']=InitDefaultPara.orgInit['DftJieDaoOrgId']
#         check_companyParam2['safetyCheckInspection.safetyCheckBasics.id']=CommonIntf.getDbQueryResult(dbCommand="select t.id from  safetycheckbasics t where t.companyname='%s'" %issueParam['safetyCheckBasics.companyName'])
#         check_companyParam2['safetyCheckInspection.safetyCheckBasics.companyName']=issueParam['safetyCheckBasics.companyName']
#         check_companyParam2['safetyCheckInspection.isQualified']='false'
#         check_companyParam2['safetyCheckInspection.checkDate']=Time.getCurrentDate()
#         check_companyParam2['safetyCheckInspection.moduleDetailInspections[0].checkName']='其他22'
#         check_companyParam2['safetyCheckInspection.moduleDetailInspections[0].safetyCheckModuleDetail.id']=CommonIntf.getDbQueryResult(dbCommand="select t.id from safetyCheckModuleDetail t where t.displayname = '%s'" % threeClassParam['safetyCheckModuleDetail.displayName'] )
#         check_companyParam2['safetyCheckInspection.moduleDetailInspections[0].checkType']='false'
#         #风险等级
#         check_companyParam2['safetyCheckInspection.riskLevel.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='平安检查专项风险等级', displayName='一般')
#         #检查类型
#         check_companyParam2['safetyCheckInspection.checkType.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='平安检查专项检查类型', displayName='市级')
#         check_companyParam2['safetyCheckInspection.rectificationDate']=Time.getCurrentDate()
#         check_companyParam2['safetyCheckInspection.checkUsers']=CommonIntf.getDbQueryResult(dbCommand="select t.id from users t where t.userName='%s'" % InitDefaultPara.userInit['DftShiUser'])
#        
#         ret = HuZhouXunJianIntf.checkCompany(param=check_companyParam2,username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
#         self.assertTrue(ret, '添加单位检查失败') 
#         Time.wait(1)
#         
#         
#         idsParam = copy.deepcopy(HuZhouXunJianPara.HuZhouXunJian_ids) 
#         idsParam['ids'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id  from  safetycheckinspection t where t.checkno  in ('%s','%s')" %(check_companyParam['safetyCheckInspection.checkNo'],check_companyParam2['safetyCheckInspection.checkNo']))
#         ret = HuZhouXunJianIntf.zxjc_huZhouXunJian(issueDict=idsParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
#         self.assertTrue(ret, '单位检查批量删除失败')
#         Time.wait(1)
#         #检查第一条单位检查数据
#         issueParamSearch = copy.deepcopy(HuZhouXunJianPara.checkCompanyUnit) 
#         issueParamSearch['safetyCheckInspectionVo.safetyCheckBasics.companyName'] = check_companyParam['safetyCheckInspection.safetyCheckBasics.companyName']
#         ret = HuZhouXunJianIntf.checkUnitCompany(issueParamSearch, username=InitDefaultPara.userInit['DftShiUser'], password='11111111');
#         self.assertFalse(ret, '删除的单位检查在列表中没找到')
#         
#         #检查第二条单位检查数据
#         issueParamSearch = copy.deepcopy(HuZhouXunJianPara.checkCompanyUnit) 
#         issueParamSearch['safetyCheckInspectionVo.safetyCheckBasics.companyName'] = check_companyParam2['safetyCheckInspection.safetyCheckBasics.companyName']
#         ret = HuZhouXunJianIntf.checkUnitCompany(issueParamSearch, username=InitDefaultPara.userInit['DftShiUser'], password='11111111');
#         self.assertFalse(ret, '删除的单位检查在列表中没找到')
                           
# #导入
#     def importDataCompany_026 (self): 
#         """平安检查--基础信息--导入  """  
#         importDataCompany = copy.deepcopy(HuZhouXunJianPara.importDataParam)
#         importDataCompany['dataType']='safetyCheckBasics'
#         importDataCompany['templates']='SAFETYCHECKBASICS'
#         files = {'upload': ('test.xls', open('C:/autotest_file/importCompany.xls', 'rb'),'applicationnd.ms-excel')}
#         ret = HuZhouXunJianIntf.importDataCompany(importDataCompany, files=files,username=InitDefaultPara.userInit['DftShiUser'], password='11111111')         
#         self.assertTrue(ret, '平安检查--基础信息--导入失败')   
#         #检查点
#         check_importDataCompany = copy.deepcopy(HuZhouXunJianPara.HuZhouXunJian_check) 
#         check_importDataCompany['companyName'] = '测试自动化34535435435WWW'
#         ret = HuZhouXunJianIntf.check_huzhouxunjian(companyDict=check_importDataCompany,username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
#         self.assertTrue(ret, '导入的基础数据在列表中没找到')      
#         
# #类别统计   
#     def classTongJi_027 (self):
#         # 新增模板
#         modelParam = copy.deepcopy(HuZhouXunJianPara.addOrUpdateModelParam)
#         modelParam['safetyCheckModule.moduleName'] = '2016年考核模板%s' % CommonUtil.createRandomString(6)
#         modelParam['safetyCheckModule.checkYear'] = '2016'
#         modelParam['safetyCheckModule.id'] = ''
#         modelParam['safetyCheckModule.org.id'] = InitDefaultPara.orgInit['DftShiOrgId']
#         modelParam['safetyCheckModule.checkObject'] = '20'
#         modelParam['mode'] = 'add'
#         ret = HuZhouXunJianIntf.addModel(param=modelParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')   
#         self.assertTrue(ret, '新增模板失败')
#         Time.wait(1)
#         # 新增一级分类
#         firstClassParam = copy.deepcopy(HuZhouXunJianPara.addClass) 
#         firstClassParam['safetyCheckModuleDetail.moduleId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModule t where t.moduleName ='%s'" % modelParam['safetyCheckModule.moduleName'] )
#         firstClassParam['safetyCheckModuleDetail.displayName'] = '火灾隐患%s' % CommonUtil.createRandomString(6)
#         firstClassParam['safetyCheckModuleDetail.score'] = '2' 
#         firstClassParam['safetyCheckModuleDetail.detailLevel']='1'
#         firstClassParam['safetyCheckModuleDetail.isLeaf']='false'
#         firstClassParam['safetyCheckModuleDetail.isUse']=True
#         ret = HuZhouXunJianIntf.addClass(level=firstClassParam['safetyCheckModuleDetail.detailLevel'], param=firstClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
#         self.assertTrue(ret, '新增一级分类失败')
#         Time.wait(1)
#         # 新增二级分类       
#         twoClassParam = copy.deepcopy(HuZhouXunJianPara.addClass)
#         twoClassParam['safetyCheckModuleDetail.parentId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModuleDetail t where t.displayname = '%s'" % firstClassParam['safetyCheckModuleDetail.displayName'])
#         twoClassParam['safetyCheckModuleDetail.moduleId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.moduleid from safetyCheckModuleDetail t where t.displayname = '%s'" % firstClassParam['safetyCheckModuleDetail.displayName'])
#         twoClassParam['safetyCheckModuleDetail.displayName'] = '火灾隐患项2级分类%s' % CommonUtil.createRandomString(6)
#         twoClassParam['safetyCheckModuleDetail.score'] = '1'
#         twoClassParam['safetyCheckModuleDetail.detailLevel']='2'
#         twoClassParam['safetyCheckModuleDetail.isLeaf']='false'
#         twoClassParam['safetyCheckModuleDetail.isUse']=True
#         ret = HuZhouXunJianIntf.addClass(level=twoClassParam['safetyCheckModuleDetail.detailLevel'],param=twoClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
#         self.assertTrue(ret, "新增二级分类失败")
#         Time.wait(1) 
#         # 新增三级分类       
#         threeClassParam = copy.deepcopy(HuZhouXunJianPara.addClass)
#         threeClassParam['safetyCheckModuleDetail.parentId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModuleDetail t where t.displayname = '%s'" % twoClassParam['safetyCheckModuleDetail.displayName'] )
#         threeClassParam['safetyCheckModuleDetail.moduleId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.moduleid from safetyCheckModuleDetail t where t.displayname = '%s'" % twoClassParam['safetyCheckModuleDetail.displayName'] )
#         threeClassParam['safetyCheckModuleDetail.displayName'] = '火灾隐患项3级分类%s' % CommonUtil.createRandomString(6)
#         threeClassParam['safetyCheckModuleDetail.score'] = '1'
#         threeClassParam['safetyCheckModuleDetail.isUse'] = '1'
#         threeClassParam['safetyCheckModuleDetail.detailLevel']='3'
#         threeClassParam['safetyCheckModuleDetail.isInput']='true'
#         threeClassParam['safetyCheckModuleDetail.isLeaf']='true'
#         threeClassParam['safetyCheckModuleDetail.isUse']=True
#         ret = HuZhouXunJianIntf.addClass(level=threeClassParam['safetyCheckModuleDetail.detailLevel'],param=threeClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
#         self.assertTrue(ret, "新增三级分类失败") 
#         Time.wait(1)
#        
#         # 启用模板
#         isUseModeParam = copy.deepcopy(HuZhouXunJianPara.isUseMode)
#         isUseModeParam['safetyCheckModule.isUse'] = True 
#         isUseModeParam['safetyCheckModule.id'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModule t where t.moduleName ='%s'" % modelParam['safetyCheckModule.moduleName'])       
#         ret = HuZhouXunJianIntf.isUseModel(param=isUseModeParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')         
#         self.assertTrue(ret, "启用模板失败")
#         Time.wait(1)
#         #新增单位信息
#         issueParam = copy.deepcopy(HuZhouXunJianPara.editOrAddObject) 
#         issueParam['safetyCheckBasics.org.id'] = InitDefaultPara.orgInit['DftJieDaoOrgId']
#         issueParam['safetyCheckBasics.companyName'] = '天阙科技05%s' % CommonUtil.createRandomString(6) 
#         issueParam['safetyCheckBasics.companyAddr'] = '西城广场2'
#         issueParam['safetyCheckBasics.companyType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='平安检查企业类型', displayName='规上企业')  
#         issueParam['safetyCheckBasics.orgNo'] = '33'
#         issueParam['safetyCheckBasics.id'] = ''
#         issueParam['mode'] = 'add'
#         issueParam['safetyCheckBasics.org.orgInternalCode'] = CommonIntf.getDbQueryResult(dbCommand="select t.orginternalcode from ORGANIZATIONS t where t.id = %s"%issueParam['safetyCheckBasics.org.id'])
#         ret = HuZhouXunJianIntf.addsafetyCheckBasics(issueDict=issueParam,username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
#         self.assertTrue(ret, '单位信息新增失败')
#         Time.wait(1)
#         #新增单位检查
#         check_companyParam = copy.deepcopy(HuZhouXunJianPara.check_companyParam)
#         check_companyParam['safetyCheckInspection.id']=''
#         check_companyParam['safetyCheckInspection.checkNo']='15120795959595%s'% CommonUtil.createRandomString(6) 
#         check_companyParam['safetyCheckInspection.org.id']=InitDefaultPara.orgInit['DftJieDaoOrgId']
#         check_companyParam['safetyCheckInspection.safetyCheckBasics.id']=CommonIntf.getDbQueryResult(dbCommand="select t.id from  safetycheckbasics t where t.companyname='%s'" %issueParam['safetyCheckBasics.companyName'])
#         check_companyParam['safetyCheckInspection.safetyCheckBasics.companyName']=issueParam['safetyCheckBasics.companyName']
#         check_companyParam['safetyCheckInspection.isQualified']='false'
#         check_companyParam['safetyCheckInspection.checkDate']=Time.getCurrentDate()
#         check_companyParam['safetyCheckInspection.moduleDetailInspections[0].checkName']='其他22'
#         check_companyParam['safetyCheckInspection.moduleDetailInspections[0].safetyCheckModuleDetail.id']=CommonIntf.getDbQueryResult(dbCommand="select t.id from safetyCheckModuleDetail t where t.displayname = '%s'" % threeClassParam['safetyCheckModuleDetail.displayName'] )
#         check_companyParam['safetyCheckInspection.moduleDetailInspections[0].checkType']='false'
#         #风险等级
#         check_companyParam['safetyCheckInspection.riskLevel.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='平安检查专项风险等级', displayName='一般')
#         #检查类型
#         check_companyParam['safetyCheckInspection.checkType.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='平安检查专项检查类型', displayName='市级')
#         check_companyParam['safetyCheckInspection.rectificationDate']=Time.getCurrentDate()
#         check_companyParam['safetyCheckInspection.checkUsers']=CommonIntf.getDbQueryResult(dbCommand="select t.id from users t where t.userName='%s'" % InitDefaultPara.userInit['DftShiUser'])
#        
#         ret = HuZhouXunJianIntf.checkCompany(param=check_companyParam,username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
#         self.assertTrue(ret, '添加单位检查失败') 
#         Time.wait(1)
#         
#         #查询条件
#         check_companyParam2 = copy.deepcopy(HuZhouXunJianPara.classTongJiParam)  
#         check_companyParam2['safetyCheckStatisticsVo.moduleId'] =  CommonIntf.getDbQueryResult(dbCommand="select t.id from safetyCheckModule t where t.isuse = 1") 
#         check_companyParam2['safetyCheckStatisticsVo.riskLevel'] = check_companyParam['safetyCheckInspection.riskLevel.id']
#         check_companyParam2['safetyCheckStatisticsVo.checkType'] = check_companyParam['safetyCheckInspection.checkType.id']
#         #统计
#         check_tongjiParam = copy.deepcopy(HuZhouXunJianPara.classTongJiCheck)  
#         #统计单位总数
#         check_tongjiParam['companyCount'] = CommonIntf.getDbQueryResult(dbCommand="select count(*)  from safetyCheckBasics t where t.createuser = '%s'" %InitDefaultPara.userInit['DftShiUser'])
#         #统计检查数
#         check_tongjiParam['inspectionCount'] =  CommonIntf.getDbQueryResult(dbCommand="select count(*) from  safetyCheckInspection t where t.createuser = '%s'" %InitDefaultPara.userInit['DftShiUser'])      
#         ret = HuZhouXunJianIntf.classTongJi(param=check_tongjiParam,check_companyParam=check_companyParam2,username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
#         self.assertTrue(ret, '统计类别失败') 
#         Time.wait(1)            
#         
# #类别统计   
#     def classTongJi_028 (self):
#         # 新增模板
#         modelParam = copy.deepcopy(HuZhouXunJianPara.addOrUpdateModelParam)
#         modelParam['safetyCheckModule.moduleName'] = '2016年考核模板%s' % CommonUtil.createRandomString(6)
#         modelParam['safetyCheckModule.checkYear'] = '2016'
#         modelParam['safetyCheckModule.id'] = ''
#         modelParam['safetyCheckModule.org.id'] = InitDefaultPara.orgInit['DftShiOrgId']
#         modelParam['safetyCheckModule.checkObject'] = '20'
#         modelParam['mode'] = 'add'
#         ret = HuZhouXunJianIntf.addModel(param=modelParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')   
#         self.assertTrue(ret, '新增模板失败')
#         Time.wait(1)
#         # 新增一级分类
#         firstClassParam = copy.deepcopy(HuZhouXunJianPara.addClass) 
#         firstClassParam['safetyCheckModuleDetail.moduleId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModule t where t.moduleName ='%s'" % modelParam['safetyCheckModule.moduleName'] )
#         firstClassParam['safetyCheckModuleDetail.displayName'] = '火灾隐患%s' % CommonUtil.createRandomString(6)
#         firstClassParam['safetyCheckModuleDetail.score'] = '2' 
#         firstClassParam['safetyCheckModuleDetail.detailLevel']='1'
#         firstClassParam['safetyCheckModuleDetail.isLeaf']='false'
#         firstClassParam['safetyCheckModuleDetail.isUse']=True
#         ret = HuZhouXunJianIntf.addClass(level=firstClassParam['safetyCheckModuleDetail.detailLevel'], param=firstClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
#         self.assertTrue(ret, '新增一级分类失败')
#         Time.wait(1)
#         # 新增二级分类       
#         twoClassParam = copy.deepcopy(HuZhouXunJianPara.addClass)
#         twoClassParam['safetyCheckModuleDetail.parentId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModuleDetail t where t.displayname = '%s'" % firstClassParam['safetyCheckModuleDetail.displayName'])
#         twoClassParam['safetyCheckModuleDetail.moduleId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.moduleid from safetyCheckModuleDetail t where t.displayname = '%s'" % firstClassParam['safetyCheckModuleDetail.displayName'])
#         twoClassParam['safetyCheckModuleDetail.displayName'] = '火灾隐患项2级分类%s' % CommonUtil.createRandomString(6)
#         twoClassParam['safetyCheckModuleDetail.score'] = '1'
#         twoClassParam['safetyCheckModuleDetail.detailLevel']='2'
#         twoClassParam['safetyCheckModuleDetail.isLeaf']='false'
#         twoClassParam['safetyCheckModuleDetail.isUse']=True
#         ret = HuZhouXunJianIntf.addClass(level=twoClassParam['safetyCheckModuleDetail.detailLevel'],param=twoClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
#         self.assertTrue(ret, "新增二级分类失败")
#         Time.wait(1) 
#         # 新增三级分类       
#         threeClassParam = copy.deepcopy(HuZhouXunJianPara.addClass)
#         threeClassParam['safetyCheckModuleDetail.parentId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModuleDetail t where t.displayname = '%s'" % twoClassParam['safetyCheckModuleDetail.displayName'] )
#         threeClassParam['safetyCheckModuleDetail.moduleId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.moduleid from safetyCheckModuleDetail t where t.displayname = '%s'" % twoClassParam['safetyCheckModuleDetail.displayName'] )
#         threeClassParam['safetyCheckModuleDetail.displayName'] = '火灾隐患项3级分类%s' % CommonUtil.createRandomString(6)
#         threeClassParam['safetyCheckModuleDetail.score'] = '1'
#         threeClassParam['safetyCheckModuleDetail.isUse'] = '1'
#         threeClassParam['safetyCheckModuleDetail.detailLevel']='3'
#         threeClassParam['safetyCheckModuleDetail.isInput']='true'
#         threeClassParam['safetyCheckModuleDetail.isLeaf']='true'
#         threeClassParam['safetyCheckModuleDetail.isUse']=True
#         ret = HuZhouXunJianIntf.addClass(level=threeClassParam['safetyCheckModuleDetail.detailLevel'],param=threeClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
#         self.assertTrue(ret, "新增三级分类失败") 
#         Time.wait(1)
#        
#         # 启用模板
#         isUseModeParam = copy.deepcopy(HuZhouXunJianPara.isUseMode)
#         isUseModeParam['safetyCheckModule.isUse'] = True 
#         isUseModeParam['safetyCheckModule.id'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModule t where t.moduleName ='%s'" % modelParam['safetyCheckModule.moduleName'])       
#         ret = HuZhouXunJianIntf.isUseModel(param=isUseModeParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')         
#         self.assertTrue(ret, "启用模板失败")
#         Time.wait(1)
#         #新增单位信息
#         issueParam = copy.deepcopy(HuZhouXunJianPara.editOrAddObject) 
#         issueParam['safetyCheckBasics.org.id'] = InitDefaultPara.orgInit['DftJieDaoOrgId']
#         issueParam['safetyCheckBasics.companyName'] = '天阙科技05%s' % CommonUtil.createRandomString(6) 
#         issueParam['safetyCheckBasics.companyAddr'] = '西城广场2'
#         issueParam['safetyCheckBasics.companyType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='平安检查企业类型', displayName='规上企业')  
#         issueParam['safetyCheckBasics.orgNo'] = '33'
#         issueParam['safetyCheckBasics.id'] = ''
#         issueParam['mode'] = 'add'
#         issueParam['safetyCheckBasics.org.orgInternalCode'] = CommonIntf.getDbQueryResult(dbCommand="select t.orginternalcode from ORGANIZATIONS t where t.id = %s"%issueParam['safetyCheckBasics.org.id'])
#         ret = HuZhouXunJianIntf.addsafetyCheckBasics(issueDict=issueParam,username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
#         self.assertTrue(ret, '单位信息新增失败')
#         Time.wait(1)
#         #新增单位检查
#         check_companyParam = copy.deepcopy(HuZhouXunJianPara.check_companyParam)
#         check_companyParam['safetyCheckInspection.id']=''
#         check_companyParam['safetyCheckInspection.checkNo']='15120795959595%s'% CommonUtil.createRandomString(6) 
#         check_companyParam['safetyCheckInspection.org.id']=InitDefaultPara.orgInit['DftJieDaoOrgId']
#         check_companyParam['safetyCheckInspection.safetyCheckBasics.id']=CommonIntf.getDbQueryResult(dbCommand="select t.id from  safetycheckbasics t where t.companyname='%s'" %issueParam['safetyCheckBasics.companyName'])
#         check_companyParam['safetyCheckInspection.safetyCheckBasics.companyName']=issueParam['safetyCheckBasics.companyName']
#         check_companyParam['safetyCheckInspection.isQualified']='false'
#         check_companyParam['safetyCheckInspection.checkDate']=Time.getCurrentDate()
#         check_companyParam['safetyCheckInspection.moduleDetailInspections[0].checkName']='其他22'
#         check_companyParam['safetyCheckInspection.moduleDetailInspections[0].safetyCheckModuleDetail.id']=CommonIntf.getDbQueryResult(dbCommand="select t.id from safetyCheckModuleDetail t where t.displayname = '%s'" % threeClassParam['safetyCheckModuleDetail.displayName'] )
#         check_companyParam['safetyCheckInspection.moduleDetailInspections[0].checkType']='false'
#         #风险等级
#         check_companyParam['safetyCheckInspection.riskLevel.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='平安检查专项风险等级', displayName='一般')
#         #检查类型
#         check_companyParam['safetyCheckInspection.checkType.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='平安检查专项检查类型', displayName='市级')
#         check_companyParam['safetyCheckInspection.rectificationDate']=Time.getCurrentDate()
#         check_companyParam['safetyCheckInspection.checkUsers']=CommonIntf.getDbQueryResult(dbCommand="select t.id from users t where t.userName='%s'" % InitDefaultPara.userInit['DftShiUser'])
#        
#         ret = HuZhouXunJianIntf.checkCompany(param=check_companyParam,username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
#         self.assertTrue(ret, '添加单位检查失败') 
#         Time.wait(1)
#     
#         check_tongjiParam = copy.deepcopy(HuZhouXunJianPara.classTypeParamCheck)  
#         check_tongjiParam['org907'] = CommonIntf.getDbQueryResult(dbCommand="select count(*) from scmoduledetailinspection  t where t.createuser = '%s' and t.moduledetailid = '%s'" %(InitDefaultPara.userInit['DftShiUser'],check_companyParam['safetyCheckInspection.moduleDetailInspections[0].safetyCheckModuleDetail.id']))
#         ret = HuZhouXunJianIntf.classType(param=check_tongjiParam,username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
#         self.assertTrue(ret, '统计类别失败') 
#         Time.wait(1)  
#         
#         
# #检查次数环比统计  
#     def classTongJi_029 (self):
#         # 新增模板
#         modelParam = copy.deepcopy(HuZhouXunJianPara.addOrUpdateModelParam)
#         modelParam['safetyCheckModule.moduleName'] = '2016年考核模板%s' % CommonUtil.createRandomString(6)
#         modelParam['safetyCheckModule.checkYear'] = '2016'
#         modelParam['safetyCheckModule.id'] = ''
#         modelParam['safetyCheckModule.org.id'] = InitDefaultPara.orgInit['DftShiOrgId']
#         modelParam['safetyCheckModule.checkObject'] = '20'
#         modelParam['mode'] = 'add'
#         ret = HuZhouXunJianIntf.addModel(param=modelParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')   
#         self.assertTrue(ret, '新增模板失败')
#         Time.wait(1)
#         # 新增一级分类
#         firstClassParam = copy.deepcopy(HuZhouXunJianPara.addClass) 
#         firstClassParam['safetyCheckModuleDetail.moduleId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModule t where t.moduleName ='%s'" % modelParam['safetyCheckModule.moduleName'] )
#         firstClassParam['safetyCheckModuleDetail.displayName'] = '火灾隐患%s' % CommonUtil.createRandomString(6)
#         firstClassParam['safetyCheckModuleDetail.score'] = '2' 
#         firstClassParam['safetyCheckModuleDetail.detailLevel']='1'
#         firstClassParam['safetyCheckModuleDetail.isLeaf']='false'
#         firstClassParam['safetyCheckModuleDetail.isUse']=True
#         ret = HuZhouXunJianIntf.addClass(level=firstClassParam['safetyCheckModuleDetail.detailLevel'], param=firstClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
#         self.assertTrue(ret, '新增一级分类失败')
#         Time.wait(1)
#         # 新增二级分类       
#         twoClassParam = copy.deepcopy(HuZhouXunJianPara.addClass)
#         twoClassParam['safetyCheckModuleDetail.parentId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModuleDetail t where t.displayname = '%s'" % firstClassParam['safetyCheckModuleDetail.displayName'])
#         twoClassParam['safetyCheckModuleDetail.moduleId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.moduleid from safetyCheckModuleDetail t where t.displayname = '%s'" % firstClassParam['safetyCheckModuleDetail.displayName'])
#         twoClassParam['safetyCheckModuleDetail.displayName'] = '火灾隐患项2级分类%s' % CommonUtil.createRandomString(6)
#         twoClassParam['safetyCheckModuleDetail.score'] = '1'
#         twoClassParam['safetyCheckModuleDetail.detailLevel']='2'
#         twoClassParam['safetyCheckModuleDetail.isLeaf']='false'
#         twoClassParam['safetyCheckModuleDetail.isUse']=True
#         ret = HuZhouXunJianIntf.addClass(level=twoClassParam['safetyCheckModuleDetail.detailLevel'],param=twoClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
#         self.assertTrue(ret, "新增二级分类失败")
#         Time.wait(1) 
#         # 新增三级分类       
#         threeClassParam = copy.deepcopy(HuZhouXunJianPara.addClass)
#         threeClassParam['safetyCheckModuleDetail.parentId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModuleDetail t where t.displayname = '%s'" % twoClassParam['safetyCheckModuleDetail.displayName'] )
#         threeClassParam['safetyCheckModuleDetail.moduleId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.moduleid from safetyCheckModuleDetail t where t.displayname = '%s'" % twoClassParam['safetyCheckModuleDetail.displayName'] )
#         threeClassParam['safetyCheckModuleDetail.displayName'] = '火灾隐患项3级分类%s' % CommonUtil.createRandomString(6)
#         threeClassParam['safetyCheckModuleDetail.score'] = '1'
#         threeClassParam['safetyCheckModuleDetail.isUse'] = '1'
#         threeClassParam['safetyCheckModuleDetail.detailLevel']='3'
#         threeClassParam['safetyCheckModuleDetail.isInput']='true'
#         threeClassParam['safetyCheckModuleDetail.isLeaf']='true'
#         threeClassParam['safetyCheckModuleDetail.isUse']=True
#         ret = HuZhouXunJianIntf.addClass(level=threeClassParam['safetyCheckModuleDetail.detailLevel'],param=threeClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
#         self.assertTrue(ret, "新增三级分类失败") 
#         Time.wait(1)
#        
#         # 启用模板
#         isUseModeParam = copy.deepcopy(HuZhouXunJianPara.isUseMode)
#         isUseModeParam['safetyCheckModule.isUse'] = True 
#         isUseModeParam['safetyCheckModule.id'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModule t where t.moduleName ='%s'" % modelParam['safetyCheckModule.moduleName'])       
#         ret = HuZhouXunJianIntf.isUseModel(param=isUseModeParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')         
#         self.assertTrue(ret, "启用模板失败")
#         Time.wait(1)
#         #新增单位信息
#         issueParam = copy.deepcopy(HuZhouXunJianPara.editOrAddObject) 
#         issueParam['safetyCheckBasics.org.id'] = InitDefaultPara.orgInit['DftJieDaoOrgId']
#         issueParam['safetyCheckBasics.companyName'] = '天阙科技05%s' % CommonUtil.createRandomString(6) 
#         issueParam['safetyCheckBasics.companyAddr'] = '西城广场2'
#         issueParam['safetyCheckBasics.companyType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='平安检查企业类型', displayName='规上企业')  
#         issueParam['safetyCheckBasics.orgNo'] = '33'
#         issueParam['safetyCheckBasics.id'] = ''
#         issueParam['mode'] = 'add'
#         issueParam['safetyCheckBasics.org.orgInternalCode'] = CommonIntf.getDbQueryResult(dbCommand="select t.orginternalcode from ORGANIZATIONS t where t.id = %s"%issueParam['safetyCheckBasics.org.id'])
#         ret = HuZhouXunJianIntf.addsafetyCheckBasics(issueDict=issueParam,username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
#         self.assertTrue(ret, '单位信息新增失败')
#         Time.wait(1)
#         #新增单位检查
#         check_companyParam = copy.deepcopy(HuZhouXunJianPara.check_companyParam)
#         check_companyParam['safetyCheckInspection.id']=''
#         check_companyParam['safetyCheckInspection.checkNo']='15120795959595%s'% CommonUtil.createRandomString(6) 
#         check_companyParam['safetyCheckInspection.org.id']=InitDefaultPara.orgInit['DftJieDaoOrgId']
#         check_companyParam['safetyCheckInspection.safetyCheckBasics.id']=CommonIntf.getDbQueryResult(dbCommand="select t.id from  safetycheckbasics t where t.companyname='%s'" %issueParam['safetyCheckBasics.companyName'])
#         check_companyParam['safetyCheckInspection.safetyCheckBasics.companyName']=issueParam['safetyCheckBasics.companyName']
#         check_companyParam['safetyCheckInspection.isQualified']='false'
#         check_companyParam['safetyCheckInspection.checkDate']=Time.getCurrentDate()
#         check_companyParam['safetyCheckInspection.moduleDetailInspections[0].checkName']='其他22'
#         check_companyParam['safetyCheckInspection.moduleDetailInspections[0].safetyCheckModuleDetail.id']=CommonIntf.getDbQueryResult(dbCommand="select t.id from safetyCheckModuleDetail t where t.displayname = '%s'" % threeClassParam['safetyCheckModuleDetail.displayName'] )
#         check_companyParam['safetyCheckInspection.moduleDetailInspections[0].checkType']='false'
#         #风险等级
#         check_companyParam['safetyCheckInspection.riskLevel.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='平安检查专项风险等级', displayName='一般')
#         #检查类型
#         check_companyParam['safetyCheckInspection.checkType.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='平安检查专项检查类型', displayName='市级')
#         check_companyParam['safetyCheckInspection.rectificationDate']=Time.getCurrentDate()
#         check_companyParam['safetyCheckInspection.checkUsers']=CommonIntf.getDbQueryResult(dbCommand="select t.id from users t where t.userName='%s'" % InitDefaultPara.userInit['DftShiUser'])
#        
#         ret = HuZhouXunJianIntf.checkCompany(param=check_companyParam,username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
#         self.assertTrue(ret, '添加单位检查失败') 
#         Time.wait(1)
#     
#         Data = CommonIntf.getDbQueryResult(dbCommand="select count(*) from safetyCheckInspection t  where to_char(sysdate,'yyyy-mm')=to_char(t.checkdate,'yyyy-mm')" )
# 
#         ret = HuZhouXunJianIntf.FrequencyRing(param=Data,username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
#         self.assertTrue(ret, '统计类别失败') 
#         Time.wait(1)  
#                         
#         
#         
# #检查次数同比统计  
#     def classTongJi_030 (self):
#         # 新增模板
#         modelParam = copy.deepcopy(HuZhouXunJianPara.addOrUpdateModelParam)
#         modelParam['safetyCheckModule.moduleName'] = '2016年考核模板%s' % CommonUtil.createRandomString(6)
#         modelParam['safetyCheckModule.checkYear'] = '2016'
#         modelParam['safetyCheckModule.id'] = ''
#         modelParam['safetyCheckModule.org.id'] = InitDefaultPara.orgInit['DftShiOrgId']
#         modelParam['safetyCheckModule.checkObject'] = '20'
#         modelParam['mode'] = 'add'
#         ret = HuZhouXunJianIntf.addModel(param=modelParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')   
#         self.assertTrue(ret, '新增模板失败')
#         Time.wait(1)
#         # 新增一级分类
#         firstClassParam = copy.deepcopy(HuZhouXunJianPara.addClass) 
#         firstClassParam['safetyCheckModuleDetail.moduleId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModule t where t.moduleName ='%s'" % modelParam['safetyCheckModule.moduleName'] )
#         firstClassParam['safetyCheckModuleDetail.displayName'] = '火灾隐患%s' % CommonUtil.createRandomString(6)
#         firstClassParam['safetyCheckModuleDetail.score'] = '2' 
#         firstClassParam['safetyCheckModuleDetail.detailLevel']='1'
#         firstClassParam['safetyCheckModuleDetail.isLeaf']='false'
#         firstClassParam['safetyCheckModuleDetail.isUse']=True
#         ret = HuZhouXunJianIntf.addClass(level=firstClassParam['safetyCheckModuleDetail.detailLevel'], param=firstClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
#         self.assertTrue(ret, '新增一级分类失败')
#         Time.wait(1)
#         # 新增二级分类       
#         twoClassParam = copy.deepcopy(HuZhouXunJianPara.addClass)
#         twoClassParam['safetyCheckModuleDetail.parentId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModuleDetail t where t.displayname = '%s'" % firstClassParam['safetyCheckModuleDetail.displayName'])
#         twoClassParam['safetyCheckModuleDetail.moduleId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.moduleid from safetyCheckModuleDetail t where t.displayname = '%s'" % firstClassParam['safetyCheckModuleDetail.displayName'])
#         twoClassParam['safetyCheckModuleDetail.displayName'] = '火灾隐患项2级分类%s' % CommonUtil.createRandomString(6)
#         twoClassParam['safetyCheckModuleDetail.score'] = '1'
#         twoClassParam['safetyCheckModuleDetail.detailLevel']='2'
#         twoClassParam['safetyCheckModuleDetail.isLeaf']='false'
#         twoClassParam['safetyCheckModuleDetail.isUse']=True
#         ret = HuZhouXunJianIntf.addClass(level=twoClassParam['safetyCheckModuleDetail.detailLevel'],param=twoClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
#         self.assertTrue(ret, "新增二级分类失败")
#         Time.wait(1) 
#         # 新增三级分类       
#         threeClassParam = copy.deepcopy(HuZhouXunJianPara.addClass)
#         threeClassParam['safetyCheckModuleDetail.parentId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModuleDetail t where t.displayname = '%s'" % twoClassParam['safetyCheckModuleDetail.displayName'] )
#         threeClassParam['safetyCheckModuleDetail.moduleId'] = CommonIntf.getDbQueryResultList(dbCommand="select t.moduleid from safetyCheckModuleDetail t where t.displayname = '%s'" % twoClassParam['safetyCheckModuleDetail.displayName'] )
#         threeClassParam['safetyCheckModuleDetail.displayName'] = '火灾隐患项3级分类%s' % CommonUtil.createRandomString(6)
#         threeClassParam['safetyCheckModuleDetail.score'] = '1'
#         threeClassParam['safetyCheckModuleDetail.isUse'] = '1'
#         threeClassParam['safetyCheckModuleDetail.detailLevel']='3'
#         threeClassParam['safetyCheckModuleDetail.isInput']='true'
#         threeClassParam['safetyCheckModuleDetail.isLeaf']='true'
#         threeClassParam['safetyCheckModuleDetail.isUse']=True
#         ret = HuZhouXunJianIntf.addClass(level=threeClassParam['safetyCheckModuleDetail.detailLevel'],param=threeClassParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
#         self.assertTrue(ret, "新增三级分类失败") 
#         Time.wait(1)
#        
#         # 启用模板
#         isUseModeParam = copy.deepcopy(HuZhouXunJianPara.isUseMode)
#         isUseModeParam['safetyCheckModule.isUse'] = True 
#         isUseModeParam['safetyCheckModule.id'] = CommonIntf.getDbQueryResultList(dbCommand="select t.id from safetyCheckModule t where t.moduleName ='%s'" % modelParam['safetyCheckModule.moduleName'])       
#         ret = HuZhouXunJianIntf.isUseModel(param=isUseModeParam, username=InitDefaultPara.userInit['DftShiUser'], password='11111111')         
#         self.assertTrue(ret, "启用模板失败")
#         Time.wait(1)
#         #新增单位信息
#         issueParam = copy.deepcopy(HuZhouXunJianPara.editOrAddObject) 
#         issueParam['safetyCheckBasics.org.id'] = InitDefaultPara.orgInit['DftJieDaoOrgId']
#         issueParam['safetyCheckBasics.companyName'] = '天阙科技05%s' % CommonUtil.createRandomString(6) 
#         issueParam['safetyCheckBasics.companyAddr'] = '西城广场2'
#         issueParam['safetyCheckBasics.companyType.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='平安检查企业类型', displayName='规上企业')  
#         issueParam['safetyCheckBasics.orgNo'] = '33'
#         issueParam['safetyCheckBasics.id'] = ''
#         issueParam['mode'] = 'add'
#         issueParam['safetyCheckBasics.org.orgInternalCode'] = CommonIntf.getDbQueryResult(dbCommand="select t.orginternalcode from ORGANIZATIONS t where t.id = %s"%issueParam['safetyCheckBasics.org.id'])
#         ret = HuZhouXunJianIntf.addsafetyCheckBasics(issueDict=issueParam,username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
#         self.assertTrue(ret, '单位信息新增失败')
#         Time.wait(1)
#         #新增单位检查
#         check_companyParam = copy.deepcopy(HuZhouXunJianPara.check_companyParam)
#         check_companyParam['safetyCheckInspection.id']=''
#         check_companyParam['safetyCheckInspection.checkNo']='15120795959595%s'% CommonUtil.createRandomString(6) 
#         check_companyParam['safetyCheckInspection.org.id']=InitDefaultPara.orgInit['DftJieDaoOrgId']
#         check_companyParam['safetyCheckInspection.safetyCheckBasics.id']=CommonIntf.getDbQueryResult(dbCommand="select t.id from  safetycheckbasics t where t.companyname='%s'" %issueParam['safetyCheckBasics.companyName'])
#         check_companyParam['safetyCheckInspection.safetyCheckBasics.companyName']=issueParam['safetyCheckBasics.companyName']
#         check_companyParam['safetyCheckInspection.isQualified']='false'
#         check_companyParam['safetyCheckInspection.checkDate']=Time.getCurrentDate()
#         check_companyParam['safetyCheckInspection.moduleDetailInspections[0].checkName']='其他22'
#         check_companyParam['safetyCheckInspection.moduleDetailInspections[0].safetyCheckModuleDetail.id']=CommonIntf.getDbQueryResult(dbCommand="select t.id from safetyCheckModuleDetail t where t.displayname = '%s'" % threeClassParam['safetyCheckModuleDetail.displayName'] )
#         check_companyParam['safetyCheckInspection.moduleDetailInspections[0].checkType']='false'
#         #风险等级
#         check_companyParam['safetyCheckInspection.riskLevel.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='平安检查专项风险等级', displayName='一般')
#         #检查类型
#         check_companyParam['safetyCheckInspection.checkType.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='平安检查专项检查类型', displayName='市级')
#         check_companyParam['safetyCheckInspection.rectificationDate']=Time.getCurrentDate()
#         check_companyParam['safetyCheckInspection.checkUsers']=CommonIntf.getDbQueryResult(dbCommand="select t.id from users t where t.userName='%s'" % InitDefaultPara.userInit['DftShiUser'])
#        
#         ret = HuZhouXunJianIntf.checkCompany(param=check_companyParam,username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
#         self.assertTrue(ret, '添加单位检查失败') 
#         Time.wait(1)
#         
#         #检查本周周四数据
#         Data = CommonIntf.getDbQueryResult(dbCommand="select count(*) from safetyCheckInspection t where t.checkdate =   (select trunc(sysdate, 'd')+4 from dual)" )
#         ret = HuZhouXunJianIntf.yoy(param=Data,username=InitDefaultPara.userInit['DftShiUser'], password='11111111')
#         self.assertTrue(ret, '检查次数同比统计失败') 
#         Time.wait(1) 
          
    def tearDown(self):
            pass
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(HuZhouXunJian("test_searchUnit_021")) 

    results = unittest.TextTestRunner().run(suite)
    pass
        
    
        
