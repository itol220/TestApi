# -*- coding:UTF-8 -*-
'''
Created on 2017-7-10

@author: hongzenghui
'''
from __future__ import unicode_literals

import copy
import json
import time
import unittest
from Interface.TieLuHuLu.ZuZhiJiGou import ZuZhiJiGouPara, ZuZhiJiGouIntf
from COMMON import CommonUtil
from Interface.TieLuHuLu.Common import CommonIntf

class ZuZhiJiGou(unittest.TestCase):

    def setUp(self):
        
        pass

  
    def testTeamOfficeAdd_01(self):    #编写脚本的地方
        """领导小组--基本信息--新增-1041"""
        #输入全字段新增
        addTeamOfficeDict = copy.deepcopy(ZuZhiJiGouPara.addTeamOffice) 
        addTeamOfficeDict['railwayTeamOffice.name'] = '领导小组新增%s' % CommonUtil.createRandomString()
        addTeamOfficeDict['railwayTeamOffice.officeLevel.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='机构层级', displayName='中央')  
        addTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.personInfo.name']='lipei'
        addTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.workPlace'] = CommonIntf.getIdByDomainAndDisplayName(domainName='行政单位', displayName='党委'and'政府')
        addTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.personInfo.otherWorkPlace']=''
        addTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.jobTitle']='testjob01'
        addTeamOfficeDict['railwayTeamOffice.jobRanks.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='行政级别', displayName='国家级正职')
        addTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.personInfo.mobilePhone']='18989999099'
        addTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.personInfo.telephone']='7689889'
        addTeamOfficeDict['railwayTeamOffice.company']=''
        addTeamOfficeDict['railwayTeamOffice.id']=''
        addTeamOfficeDict['teamItemIds']=CommonIntf.getIdByDomainAndDisplayName(domainName='成员单位', displayName='党委'and'政委')  
        addTeamOfficeDict['railwayTeamOffice.orgId']='1494293777572280'
        addTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.orgId']='1494293777572280'
        addTeamOfficeDict['railwayTeamOffice.isDeleted']='0'
        addTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.isDeleted']=''
        addTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.id']=''
        addTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.personInfo.id']=''
        
        print "==========%s" % addTeamOfficeDict['workPlace']
        ret = ZuZhiJiGouIntf.add_team_office(addTeamOfficeDict)
        #ret = True
        
        self.assertTrue(ret, '新增领导小组失败') 
    
        pass
    
        
        #输必填项新增
        
        addTeamOfficeDict = copy.deepcopy(ZuZhiJiGouPara.addTeamOffice) 
        addTeamOfficeDict['railwayTeamOffice.name'] = '领导小组新增%s' % CommonUtil.createRandomString()
        addTeamOfficeDict['railwayTeamOffice.officeLevel.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='机构层级', displayName='村、社区')  
        addTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.personInfo.name']='lipei01'
        addTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.workPlace'] = CommonIntf.getIdByDomainAndDisplayName(domainName='行政单位', displayName='党委'and'政府'and'综治办')
        addTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.personInfo.otherWorkPlace']=''
        addTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.jobTitle']='testjob02'
        addTeamOfficeDict['railwayTeamOffice.jobRanks.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='行政级别', displayName='国家级副职')
        addTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.personInfo.telephone']='7689888'
        addTeamOfficeDict['railwayTeamOffice.company']=''
        addTeamOfficeDict['railwayTeamOffice.id']=''  
        addTeamOfficeDict['railwayTeamOffice.orgId']='1494293777572280'
        addTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.orgId']='1494293777572280'
        addTeamOfficeDict['railwayTeamOffice.isDeleted']='0'
        addTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.isDeleted']=''
        addTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.id']=''
        addTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.personInfo.id']=''
        
        print "==========%s" % addTeamOfficeDict['workPlace']
        ret = ZuZhiJiGouIntf.add_team_office(addTeamOfficeDict)
        #ret = True
        
        self.assertTrue(ret, '新增领导小组失败') 
    
        pass
    
        
        #输必填项暂存
        addTeamOfficeDict = copy.deepcopy(ZuZhiJiGouPara.addTeamOffice) 
        addTeamOfficeDict['railwayTeamOffice.name'] = '领导小组新增%s' % CommonUtil.createRandomString()
        addTeamOfficeDict['railwayTeamOffice.officeLevel.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='机构层级', displayName='乡镇、街道')  
        addTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.personInfo.name']='lipei003'
        addTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.workPlace'] = CommonIntf.getIdByDomainAndDisplayName(domainName='行政单位', displayName='党委'and'军区')
        addTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.personInfo.otherWorkPlace']=''
        addTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.jobTitle']=''
        addTeamOfficeDict['railwayTeamOffice.jobRanks.id']=''
        addTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.personInfo.mobilePhone']=''
        addTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.personInfo.telephone']=''
        addTeamOfficeDict['railwayTeamOffice.company']=''
        addTeamOfficeDict['railwayTeamOffice.id']=''
        addTeamOfficeDict['teamItemIds']=''
        addTeamOfficeDict['railwayTeamOffice.orgId']='1494293777572280'
        addTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.orgId']='1494293777572280'
        addTeamOfficeDict['railwayTeamOffice.isDeleted']='2'
        addTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.isDeleted']=''
        addTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.id']=''
        addTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.personInfo.id']=''
            
        ret = ZuZhiJiGouIntf.add_team_office(addTeamOfficeDict)
       #ret = True
        
        self.assertTrue(ret, '新增领导小组失败') 
      
        pass
    

    def testTeamOfficeModify_01(self):              #编写脚本的地方
        """领导小组--基本信息--修改-1044"""
        #先获取一条新增数据 
        addTeamOfficeDict = copy.deepcopy(ZuZhiJiGouPara.addTeamOffice) 
        addTeamOfficeDict['railwayTeamOffice.name'] = '领导小组新增%s' % CommonUtil.createRandomString()
        addTeamOfficeDict['railwayTeamOffice.officeLevel.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='机构层级', displayName='中央')  
        addTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.personInfo.name']='lipei'
        addTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.workPlace'] = CommonIntf.getIdByDomainAndDisplayName(domainName='行政单位', displayName='党委'and'政府')
        addTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.personInfo.otherWorkPlace']=''
        addTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.jobTitle']='testjob01'
        addTeamOfficeDict['railwayTeamOffice.jobRanks.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='行政级别', displayName='国家级正职')
        addTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.personInfo.mobilePhone']='18989999099'
        addTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.personInfo.telephone']='7689889'
        addTeamOfficeDict['railwayTeamOffice.company']=''
        addTeamOfficeDict['railwayTeamOffice.id']=''
        addTeamOfficeDict['teamItemIds']=CommonIntf.getIdByDomainAndDisplayName(domainName='成员单位', displayName='党委'and'政委')  
        addTeamOfficeDict['railwayTeamOffice.orgId']='1494293777572280'
        addTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.orgId']='1494293777572280'
        addTeamOfficeDict['railwayTeamOffice.isDeleted']='0'
        addTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.isDeleted']=''
        addTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.id']=''
        addTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.personInfo.id']=''
        
        print "==========%s" % addTeamOfficeDict['workPlace']
        result = ZuZhiJiGouIntf.add_team_office(addTeamOfficeDict)   #将新增的组织机构数据赋值给result
        
        #输入全字段修改
        modifyTeamOfficeDict = copy.deepcopy(ZuZhiJiGouPara.modifyTeamOffice) 
        modifyTeamOfficeDict['railwayTeamOffice.name'] = '领导小组新增%s' % CommonUtil.createRandomString()
        modifyTeamOfficeDict['railwayTeamOffice.officeLevel.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='机构层级', displayName='省、自治区、直辖市')  
        modifyTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.personInfo.name']='lipeimodify'
        modifyTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.workPlace'] = CommonIntf.getIdByDomainAndDisplayName(domainName='行政单位', displayName='党委'and'团委')
        modifyTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.personInfo.otherWorkPlace']=''
        modifyTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.jobTitle']='testjob08'
        modifyTeamOfficeDict['railwayTeamOffice.jobRanks.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='行政级别', displayName='科员级')
        modifyTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.personInfo.mobilePhone']='18969009099'
        modifyTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.personInfo.telephone']='6729889'
        modifyTeamOfficeDict['railwayTeamOffice.company']=''
        modifyTeamOfficeDict['railwayTeamOffice.id']=result['id']       #唯一标识进行关联，将result中的id赋给修改时的id
        modifyTeamOfficeDict['teamItemIds']=CommonIntf.getIdByDomainAndDisplayName(domainName='成员单位', displayName='党委'and'政委'and'工商局')  
        modifyTeamOfficeDict['railwayTeamOffice.orgId']='1494293777572280'
        modifyTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.orgId']='1494293777572280'
        modifyTeamOfficeDict['railwayTeamOffice.isDeleted']='0'
        modifyTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.isDeleted']='2'
        modifyTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.id']='1494486637622253'
        modifyTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.personInfo.id']='1494486637611251'
        
        print "==========%s" % modifyTeamOfficeDict['workPlace']
       
        ret = ZuZhiJiGouIntf.modify_team_office(modifyTeamOfficeDict)
        # ret = True
        
        self.assertTrue(ret, '修改领导小组失败') 
    
        
        #输入必填项为空修改
        modifyTeamOfficeDict = copy.deepcopy(ZuZhiJiGouPara.modifyTeamOffice) 
        modifyTeamOfficeDict['railwayTeamOffice.name'] = ''
        modifyTeamOfficeDict['railwayTeamOffice.officeLevel.id'] = ''
        modifyTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.personInfo.name']=''
        modifyTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.workPlace'] = CommonIntf.getIdByDomainAndDisplayName(domainName='行政单位', displayName='党委'and'团委')
        modifyTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.personInfo.otherWorkPlace']=''
        modifyTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.jobTitle']=''
        modifyTeamOfficeDict['railwayTeamOffice.jobRanks.id']=''
        modifyTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.personInfo.mobilePhone']='18969009099'
        modifyTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.personInfo.telephone']='6729889'
        modifyTeamOfficeDict['railwayTeamOffice.company']=''
        modifyTeamOfficeDict['railwayTeamOffice.id']=result['id']
        modifyTeamOfficeDict['teamItemIds']=CommonIntf.getIdByDomainAndDisplayName(domainName='成员单位', displayName='党委'and'政委'and'工商局')  
        modifyTeamOfficeDict['railwayTeamOffice.orgId']='1494293777572280'
        modifyTeamOfficeDict['railwayTeamOffice.isDeleted']='0'
        modifyTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.isDeleted']='2'
        modifyTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.id']='1494486637622253'
        modifyTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.personInfo.id']='1494486637611251'
  
            
            
        ret = ZuZhiJiGouIntf.modify_team_office(modifyTeamOfficeDict)
        # ret = True
        
        self.assertFalse(ret, '修改领导小组失败') 
        
        
        #输入必填项进行修改
        modifyTeamOfficeDict = copy.deepcopy(ZuZhiJiGouPara.modifyTeamOffice) 
        modifyTeamOfficeDict['railwayTeamOffice.name'] = '领导小组新增%s' % CommonUtil.createRandomString()
        modifyTeamOfficeDict['railwayTeamOffice.officeLevel.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='机构层级', displayName='村、社区')  
        modifyTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.personInfo.name']='lipeimodify01'
        modifyTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.workPlace'] = CommonIntf.getIdByDomainAndDisplayName(domainName='行政单位', displayName='党委'and'团委')
        modifyTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.personInfo.otherWorkPlace']=''
        modifyTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.jobTitle']='testjob023'
        modifyTeamOfficeDict['railwayTeamOffice.jobRanks.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='行政级别', displayName='办事员级')
        modifyTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.personInfo.mobilePhone']=''
        modifyTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.personInfo.telephone']='6729119'
        modifyTeamOfficeDict['railwayTeamOffice.company']=''
        modifyTeamOfficeDict['railwayTeamOffice.id']=result['id']       #唯一标识进行关联，将result中的id赋给修改时的id
        modifyTeamOfficeDict['teamItemIds']='' 
        modifyTeamOfficeDict['railwayTeamOffice.orgId']='1494293777572280'
        modifyTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.orgId']='1494293777572280'
        modifyTeamOfficeDict['railwayTeamOffice.isDeleted']='0'
        modifyTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.isDeleted']='2'
        modifyTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.id']='1494486637622253'
        modifyTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.personInfo.id']='1494486637611251'
        
        print "==========%s" % modifyTeamOfficeDict['workPlace']
       
        ret = ZuZhiJiGouIntf.modify_team_office(modifyTeamOfficeDict)
        # ret = True
        
        self.assertTrue(ret, '修改领导小组失败') 
    
    
        pass  
    
  
    def testTeamPersonDelete_01(self):
        """领导小组人员  删除"""
    #新增领导小组后，领导小组人员中存在一条数据
        addTeamOfficeDict = copy.deepcopy(ZuZhiJiGouPara.addTeamOffice) 
        addTeamOfficeDict['railwayTeamOffice.name'] = '领导小组新增%s' % CommonUtil.createRandomString()
        addTeamOfficeDict['railwayTeamOffice.officeLevel.id'] = CommonIntf.getIdByDomainAndDisplayName(domainName='机构层级', displayName='中央')  
        addTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.personInfo.name']='lipei777'
        addTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.workPlace'] = CommonIntf.getIdByDomainAndDisplayName(domainName='行政单位', displayName='党委'and'政府')
        addTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.personInfo.otherWorkPlace']=''
        addTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.jobTitle']='testjob01'
        addTeamOfficeDict['railwayTeamOffice.jobRanks.id']=CommonIntf.getIdByDomainAndDisplayName(domainName='行政级别', displayName='国家级正职')
        addTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.personInfo.mobilePhone']='18989999095'
        addTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.personInfo.telephone']='7689809'
        addTeamOfficeDict['railwayTeamOffice.company']=''
        addTeamOfficeDict['railwayTeamOffice.id']=''
        addTeamOfficeDict['teamItemIds']=CommonIntf.getIdByDomainAndDisplayName(domainName='成员单位', displayName='党委')  
        addTeamOfficeDict['railwayTeamOffice.orgId']='1494293777572280'
        addTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.orgId']='1494293777572280'
        addTeamOfficeDict['railwayTeamOffice.isDeleted']='0'
        addTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.isDeleted']=''
        addTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.id']=''
        addTeamOfficeDict['railwayTeamOffice.railwayTeamPerson.personInfo.id']=''
        
        print "==========%s" % addTeamOfficeDict['workPlace']
        result = ZuZhiJiGouIntf.add_team_office(addTeamOfficeDict)   #将新增的组织机构数据赋值给result
        #获取列表信息
        
    #删除企业信息  
        deleteDict = copy.deepcopy(ZuZhiJiGouPara.deleteTeam)
        CommonIntf.clearTeamMembers(result['id'] )
        deleteDict['strIds'] = result['id']
        ret = ZuZhiJiGouIntf.delete_team_person(deleteDict)         
        self.assertTrue(ret, '删除领导小组人员失败') 
        
    
        
        pass
  
    
    
    
    
    
    
    def tearDown(self):
        pass
    
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(ZuZhiJiGou("testTeamPersonDelete_01"))
  
    results = unittest.TextTestRunner().run(suite)
    pass
