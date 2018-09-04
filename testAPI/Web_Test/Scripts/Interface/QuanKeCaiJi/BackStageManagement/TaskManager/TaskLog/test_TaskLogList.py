# -*- coding:UTF-8 -*-
'''
Created on 2018年4月8日 17:33:13

@author: 孙留平
'''
from __future__ import unicode_literals
import unittest
from Interface.PingAnJianShe.SystemMgr import SystemMgrIntf
import copy
from COMMON import CommonUtil, Time
from Interface.PingAnTong.DanWeiChangSuo import MbDanWeiChangSuoPara, \
    MbDanWeiChangSuoIntf
from Interface.PingAnJianShe.Common import CommonIntf
from CONFIG import InitDefaultPara
from Interface.PingAnJianShe.XiaQuGuanLi import XiaQuGuanLiPara, XiaQuGuanLiIntf
import random
class TaskManager( unittest.TestCase ):
    def setUp( self ):
        SystemMgrIntf.initEnv()
        pass

    
    '''
    @功能：重点场所--安全生产重点新增，修改
    @ lhz  2016-2-29
    ''' 
    def testmDanWei_001( self ):
        '''重点场所--安全生产重点新增'''
        # 新增单位信息
        issueParam = copy.deepcopy( MbDanWeiChangSuoPara.aqsczdAddPara ) 
        issueParam['enterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName( domainName = '企业类型', displayName = '规上企业' ) 
        issueParam['placeTypeName'] = '安全生产重点'
        issueParam['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        issueParam['enterprise.name'] = '安全生产重点%s' % CommonUtil.createRandomString( 6 )   
        issueParam['enterprise.keyType'] = 'safetyProductionKey'
        issueParam['enterprise.address'] = '地址2'
        issueParam['enterprise.legalPerson'] = '代表2'
        ret = MbDanWeiChangSuoIntf.aqsczdAdd( issueParam, typeName = '安全生产重点信息', username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '安全生产重点信息新增失败' )
        Time.wait( 1 )
        # 检查参数
        param = copy.deepcopy( MbDanWeiChangSuoPara.aqsczdCheck )
        # 获取组织机构id
        param['name'] = issueParam['enterprise.name']
        # 获取查询参数
        param['address'] = issueParam['enterprise.address'] 
        param['legalPerson'] = issueParam['enterprise.legalPerson'] 
        ret = MbDanWeiChangSuoIntf.check_aqsczd( companyDict = param, typeName = '安全生产重点信息', keyType = 'safetyProductionKey', orgId = InitDefaultPara.orgInit['DftWangGeOrgId'], username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '安全生产重点信息查找失败' )
        Time.wait( 1 )
        # 检验在网格2下是否可以查看到网格1下新增的数据
        ret = MbDanWeiChangSuoIntf.check_aqsczd( companyDict = param, typeName = '安全生产重点信息在网格2下查找网格1的数据', keyType = 'safetyProductionKey', orgId = InitDefaultPara.orgInit['DftWangGeOrgId1'], username = InitDefaultPara.userInit['DftWangGeUser1'], password = '11111111' )
        self.assertFalse( ret, '安全生产重点信息在网格2下查找网格1的数据失败' )
        Time.wait( 1 )
        # 修改
        issueParamUpdate = copy.deepcopy( MbDanWeiChangSuoPara.apsczdUpdateParam ) 
        issueParamUpdate['enterprise.id'] = CommonIntf.getDbQueryResult( dbCommand = "select t.id from enterprises t  where t.name= '%s'" % issueParam['enterprise.name'] )
        issueParamUpdate['enterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName( domainName = '企业类型', displayName = '规下企业' ) 
        issueParamUpdate['placeTypeName'] = '安全生产重点'
        issueParamUpdate['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        issueParamUpdate['enterprise.name'] = '安全生产重点%s' % CommonUtil.createRandomString( 6 )   
        issueParamUpdate['enterprise.keyType'] = 'safetyProductionKey'
        issueParamUpdate['enterprise.address'] = '修改地址'
        issueParamUpdate['enterprise.legalPerson'] = '修改代表'    
        ret = MbDanWeiChangSuoIntf.aqsczdUpdate( issueParamUpdate, typeName = '安全生产重点信息', username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '安全生产重点信息修改失败' )      
        Time.wait( 1 )
        # 检查参数
        param = copy.deepcopy( MbDanWeiChangSuoPara.aqsczdCheck )
        # 获取组织机构id
        param['name'] = issueParamUpdate['enterprise.name']
#         # 获取查询参数
        param['address'] = issueParamUpdate['enterprise.address'] 
        param['legalPerson'] = issueParamUpdate['enterprise.legalPerson'] 
        ret = MbDanWeiChangSuoIntf.check_Viewaqsczd( companyDict = param, typeName = '安全生产重点信息', id = issueParamUpdate['enterprise.id'], username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '安全生产重点信息查找失败' )              
        Time.wait( 1 )
        # PC端检查
        paramPC = copy.deepcopy( MbDanWeiChangSuoPara.ChaKanAnQuanShengChan )
        paramPC['name'] = issueParamUpdate['enterprise.name']
        ret = MbDanWeiChangSuoIntf.checkAnQuanShengChan( companyDict = paramPC, orgId = issueParamUpdate['ownerOrg.id'], keyType = 'safetyProductionKey', username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '安全生产重点PC端查找失败' ) 
 
        pass    
    '''
    @功能：重点场所--消防安全生产重点新增
    @ lhz  2016-2-29
    ''' 
    def testmDanWei_002( self ):
        '''重点场所--消防安全生产重点新增'''
        # 新增单位信息
        xfParam = copy.deepcopy( MbDanWeiChangSuoPara.xfaqscAdd )
        xfParam['tqmobile'] = 'true'
        xfParam['enterprise.name'] = '消防安全生产%s' % CommonUtil.createRandomString( 6 ) 
        xfParam['placeTypeName'] = '消防安全生产重点'
        xfParam['enterprise.keyType'] = 'fireSafetyKey'
        xfParam['enterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName( domainName = '消防安全重点类别', displayName = '市场' )
        xfParam['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        xfParam['enterprise.address'] = '消防安全地址2'
        xfParam['enterprise.legalPerson'] = '消防安全代表2'
        ret = MbDanWeiChangSuoIntf.aqsczdAdd( xfParam, typeName = '消防安全生产重点信息', username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '消防安全生产重点信息新增失败' )
        Time.wait( 1 )
        # 检查
        param = copy.deepcopy( MbDanWeiChangSuoPara.aqsczdCheck )
        # 获取组织机构id
        param['name'] = xfParam['enterprise.name']
        # 获取查询参数
        param['address'] = xfParam['enterprise.address'] 
        param['legalPerson'] = xfParam['enterprise.legalPerson'] 
        ret = MbDanWeiChangSuoIntf.check_aqsczd( companyDict = param, typeName = '消防安全生产重点信息', keyType = 'fireSafetyKey', orgId = InitDefaultPara.orgInit['DftWangGeOrgId'], username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '消防安全生产重点信息查找失败' )
        Time.wait( 1 )
        # 检验在网格2下是否可以查看到网格1下新增的数据
        ret = MbDanWeiChangSuoIntf.check_aqsczd( companyDict = param, typeName = '消防安全生产重点信息在网格2下查找网格1的数据', keyType = 'fireSafetyKey', orgId = InitDefaultPara.orgInit['DftWangGeOrgId1'], username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertFalse( ret, '消防安全生产重点信息在网格2下查找网格1的数据失败' )
        Time.wait( 1 )
        # 修改
        issueParamUpdate = copy.deepcopy( MbDanWeiChangSuoPara.apsczdUpdateParam ) 
        issueParamUpdate['enterprise.id'] = CommonIntf.getDbQueryResult( dbCommand = "select t.id from enterprises t  where t.name= '%s' and t.keytype='fireSafetyKey'" % xfParam['enterprise.name'] )
        issueParamUpdate['enterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName( domainName = '消防安全重点类别', displayName = '商场' ) 
        issueParamUpdate['placeTypeName'] = '消防安全生产重点'
        issueParamUpdate['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        issueParamUpdate['enterprise.name'] = '消防安全生产重点%s' % CommonUtil.createRandomString( 6 )   
        issueParamUpdate['enterprise.keyType'] = 'fireSafetyKey'
        issueParamUpdate['enterprise.address'] = '修改消防地址'
        issueParamUpdate['enterprise.legalPerson'] = '修改消防代表'    
        ret = MbDanWeiChangSuoIntf.aqsczdUpdate( issueParamUpdate, typeName = '消防安全生产重点信息', username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '消防安全生产重点信息修改失败' )    
        Time.wait( 1 )  
        # 检查
        param = copy.deepcopy( MbDanWeiChangSuoPara.aqsczdCheck )
        # 获取查询参数
        param['name'] = issueParamUpdate['enterprise.name']
        param['address'] = issueParamUpdate['enterprise.address'] 
        param['legalPerson'] = issueParamUpdate['enterprise.legalPerson'] 
        ret = MbDanWeiChangSuoIntf.check_Viewaqsczd( companyDict = param, typeName = '消防安全生产重点信息修改', id = issueParamUpdate['enterprise.id'], username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '消防安全生产重点信息修改查找失败' )
        Time.wait( 1 )  
        # PC端检查
        paramPC = copy.deepcopy( MbDanWeiChangSuoPara.ChaKanAnQuanShengChan )
        paramPC['name'] = issueParamUpdate['enterprise.name']
        ret = MbDanWeiChangSuoIntf.checkXFAnQuanShengChan( companyDict = paramPC, orgId = issueParamUpdate['ownerOrg.id'], keyType = 'fireSafetyKey', username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '消防安全生产重点信息PC端查找失败' ) 
        Time.wait( 1 )
        pass
    
    '''
    @功能：重点场所--治安重点新增
    @ lhz  2016-3-3
    ''' 
    def testmDanWei_003( self ):
        '''重点场所--治安重点新增'''
        # 新增单位信息
        xfParam = copy.deepcopy( MbDanWeiChangSuoPara.xfaqscAdd )
        xfParam['tqmobile'] = 'true'
        xfParam['enterprise.name'] = '治安重点%s' % CommonUtil.createRandomString( 6 ) 
        xfParam['placeTypeName'] = '治安重点'
        xfParam['enterprise.keyType'] = 'securityKey'
        xfParam['enterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName( domainName = '治安重点类别', displayName = '出租房屋区' )
        xfParam['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        xfParam['enterprise.address'] = '治安重点地址2'
        xfParam['enterprise.legalPerson'] = '治安重点代表2'
        ret = MbDanWeiChangSuoIntf.aqsczdAdd( xfParam, typeName = '重点场所--治安重点信息', username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '重点场所--治安重点信息新增失败' )
        Time.wait( 1 )
        # 检查
        param = copy.deepcopy( MbDanWeiChangSuoPara.aqsczdCheck )
        # 获取组织机构id
        param['name'] = xfParam['enterprise.name']
        # 获取查询参数
        param['address'] = xfParam['enterprise.address'] 
        param['legalPerson'] = xfParam['enterprise.legalPerson'] 
        ret = MbDanWeiChangSuoIntf.check_aqsczd( companyDict = param, typeName = '重点场所--治安重点信息', keyType = 'securityKey', orgId = InitDefaultPara.orgInit['DftWangGeOrgId'], username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '重点场所--治安重点信息查找失败' )
        Time.wait( 1 )        
        # 检验在网格2下是否可以查看到网格1下新增的数据
        ret = MbDanWeiChangSuoIntf.check_aqsczd( companyDict = param, typeName = '重点场所--治安重点信息在网格2下查找网格1的数据', keyType = 'securityKey', orgId = InitDefaultPara.orgInit['DftWangGeOrgId1'], username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertFalse( ret, '重点场所--治安重点信息在网格2下查找网格1的数据失败' )
        # 修改
        issueParamUpdate = copy.deepcopy( MbDanWeiChangSuoPara.apsczdUpdateParam ) 
        issueParamUpdate['enterprise.id'] = CommonIntf.getDbQueryResult( dbCommand = "select t.id from enterprises t  where t.name= '%s'" % xfParam['enterprise.name'] )
        issueParamUpdate['enterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName( domainName = '治安重点类别', displayName = '批发市场' ) 
        issueParamUpdate['placeTypeName'] = '治安重点'
        issueParamUpdate['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        issueParamUpdate['enterprise.name'] = '治安重点%s' % CommonUtil.createRandomString( 6 )   
        issueParamUpdate['enterprise.keyType'] = 'securityKey'
        issueParamUpdate['enterprise.address'] = '治安重点地址3'
        issueParamUpdate['enterprise.legalPerson'] = '治安重点代表3'    
        ret = MbDanWeiChangSuoIntf.aqsczdUpdate( issueParamUpdate, typeName = '重点场所--治安重点信息', username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '重点场所--治安重点信息修改失败' )      
        # 检查
        param = copy.deepcopy( MbDanWeiChangSuoPara.aqsczdCheck )
        # 获取查询参数
        param['name'] = issueParamUpdate['enterprise.name']        
        param['address'] = issueParamUpdate['enterprise.address'] 
        param['legalPerson'] = issueParamUpdate['enterprise.legalPerson'] 
        ret = MbDanWeiChangSuoIntf.check_Viewaqsczd( companyDict = param, typeName = '重点场所--治安重点信息', id = issueParamUpdate['enterprise.id'], username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '重点场所--治安重点信息查找失败' )
        Time.wait( 1 )  
        # PC端检查
        paramPC = copy.deepcopy( MbDanWeiChangSuoPara.ChaKanAnQuanShengChan )
        paramPC['name'] = issueParamUpdate['enterprise.name']
        ret = MbDanWeiChangSuoIntf.checkAnQuanShengChan( companyDict = paramPC, orgId = issueParamUpdate['ownerOrg.id'], keyType = 'securityKey', username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '重点场所--治安重点信息PC端查找失败' ) 

        pass  
    
    '''
    @功能：重点场所--学校新增
    @ lhz  2016-3-3
    ''' 
    def testmDanWei_004( self ):
        '''重点场所--学校新增'''
        # 新增单位信息
        xfParam = copy.deepcopy( MbDanWeiChangSuoPara.schoolParam )
        xfParam['tqmobile'] = 'true'
        xfParam['school.kind.id'] = CommonIntf.getIdByDomainAndDisplayName( domainName = '学校性质', displayName = '公办' )
        xfParam['school.type.id'] = CommonIntf.getIdByDomainAndDisplayName( domainName = '学校类型', displayName = '小学' )
        xfParam['school.president'] = '王校长'
        xfParam['orgId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        xfParam['school.chineseName'] = '学校%s' % CommonUtil.createRandomString( 6 ) 
        xfParam['school.address'] = '中原路'
        xfParam['school.hasCertificate'] = 'false'
        ret = MbDanWeiChangSuoIntf.schoolAdd( xfParam, username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '重点场所--学校新增信息失败' )
        Time.wait( 1 )
        # 检查
        param = copy.deepcopy( MbDanWeiChangSuoPara.schoolCheck )
        # 获取组织机构id
        param['chineseName'] = xfParam['school.chineseName']
        # 获取查询参数
        param['address'] = xfParam['school.address'] 
        param['president'] = xfParam['school.president'] 
        ret = MbDanWeiChangSuoIntf.check_school( companyDict = param, typeName = '重点场所--学校新增信息', orgId = InitDefaultPara.orgInit['DftWangGeOrgId'], username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '重点场所--学校新增信息查找失败' )
        Time.wait( 1 )
        # 检验在网格2下是否可以查看到网格1下新增的数据
        ret = MbDanWeiChangSuoIntf.check_school( companyDict = param, typeName = '重点场所--学校新增信息在网格2下查找网格1的数据', orgId = InitDefaultPara.orgInit['DftWangGeOrgId1'], username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertFalse( ret, '重点场所--学校新增信息在网格2下查找网格1的数据失败' )
        Time.wait( 1 ) 
        # 修改
        issueParamUpdate = copy.deepcopy( MbDanWeiChangSuoPara.schoolParam )
        issueParamUpdate['tqmobile'] = 'true'
        issueParamUpdate['school.id'] = CommonIntf.getDbQueryResult( dbCommand = "select t.id from schools t  where t.chineseName= '%s'" % xfParam['school.chineseName'] )
        issueParamUpdate['school.kind.id'] = CommonIntf.getIdByDomainAndDisplayName( domainName = '学校性质', displayName = '民办' )
        issueParamUpdate['school.type.id'] = CommonIntf.getIdByDomainAndDisplayName( domainName = '学校类型', displayName = '幼儿园' )
        issueParamUpdate['school.president'] = '王校长'
        issueParamUpdate['orgId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        issueParamUpdate['school.chineseName'] = '学校%s' % CommonUtil.createRandomString( 6 ) 
        issueParamUpdate['school.address'] = '中原路'
        issueParamUpdate['school.hasCertificate'] = 'false'
        ret = MbDanWeiChangSuoIntf.schoolEdit( issueParamUpdate, username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '重点场所--学校信息修改失败' )
        Time.wait( 1 )    
        # 检查
        param = copy.deepcopy( MbDanWeiChangSuoPara.schoolCheck )
        # 获取组织机构id
        param['chineseName'] = issueParamUpdate['school.chineseName']
        # 获取查询参数
        param['address'] = issueParamUpdate['school.address'] 
        param['president'] = issueParamUpdate['school.president'] 
        ret = MbDanWeiChangSuoIntf.checkViewschool( companyDict = param, typeName = '重点场所--学校信息修改', id = issueParamUpdate['school.id'], username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '重点场所--学校信息修改查找失败' )
        Time.wait( 1 )   
        # PC端检查
        paramPC = copy.deepcopy( MbDanWeiChangSuoPara.schoolCheck )
        paramPC['chineseName'] = issueParamUpdate['school.chineseName']
        ret = MbDanWeiChangSuoIntf.checkSchool( companyDict = paramPC, username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '重点场所--学校信息PC端查找失败' ) 

        pass 
    
    
         
        '''
    @功能：重点场所--其他场所新增，修改，查看
    @ lhz  2016-3-3
    ''' 
    def testmDanWei_005( self ):
        '''重点场所--其他场所新增'''
        # 新增单位信息
        xfParam = copy.deepcopy( MbDanWeiChangSuoPara.otherParamAddOrUpdate )
        xfParam['tqmobile'] = 'true'
        xfParam['otherLocale.type.id'] = CommonIntf.getIdByDomainAndDisplayName( domainName = '其他场所类型', displayName = '煤气点' )
        xfParam['otherLocale.name'] = '其他场所%s' % CommonUtil.createRandomString( 6 ) 
        xfParam['organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        xfParam['otherLocale.address'] = '学院路'
        xfParam['otherLocale.contactPerson'] = '张三'
        ret = MbDanWeiChangSuoIntf.OtherCSAdd( param = xfParam, username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '重点场所--其他场所新增信息失败' )
        Time.wait( 1 )
        # 检查
        param = copy.deepcopy( MbDanWeiChangSuoPara.otherCheck )
        param['address'] = xfParam['otherLocale.address']
        # 获取查询参数
        param['contactPerson'] = xfParam['otherLocale.contactPerson'] 
        param['name'] = xfParam['otherLocale.name'] 
        ret = MbDanWeiChangSuoIntf.check_other( companyDict = param, typeName = '重点场所--其他场所新增信息', orgId = InitDefaultPara.orgInit['DftWangGeOrgId'], username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '重点场所--其他场所新增信息查找失败' )
        Time.wait( 1 )
        # 检验在网格2下是否可以查看到网格1下新增的数据
        ret = MbDanWeiChangSuoIntf.check_other( companyDict = param, typeName = '重点场所--其他场所新增信息在网格2下查找网格1的数据', orgId = InitDefaultPara.orgInit['DftWangGeOrgId1'], username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertFalse( ret, '重点场所--其他场所新增信息在网格2下查找网格1的数据失败' )
        Time.wait( 1 )
        # 修改
        issueParamUpdate = copy.deepcopy( MbDanWeiChangSuoPara.otherParamAddOrUpdate )
        issueParamUpdate['tqmobile'] = 'true'
        issueParamUpdate['otherLocale.id'] = CommonIntf.getDbQueryResult( dbCommand = "select t.id from otherlocales t  where t.name= '%s'" % xfParam['otherLocale.name'] )
        issueParamUpdate['otherLocale.type.id'] = CommonIntf.getIdByDomainAndDisplayName( domainName = '其他场所类型', displayName = '监控点' )
        issueParamUpdate['otherLocale.name'] = '其他场所%s' % CommonUtil.createRandomString( 6 ) 
        issueParamUpdate['organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        issueParamUpdate['otherLocale.address'] = '学院路11'
        issueParamUpdate['otherLocale.contactPerson'] = '张三1'
        ret = MbDanWeiChangSuoIntf.OtherCSEdit( param = issueParamUpdate, username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '重点场所--其他场所修改信息失败' )   
        Time.wait( 1 )
        # 检查
        param = copy.deepcopy( MbDanWeiChangSuoPara.otherCheck )
        # 获取组织机构id
        param['address'] = issueParamUpdate['otherLocale.address']
        # 获取查询参数
        param['contactPerson'] = issueParamUpdate['otherLocale.contactPerson'] 
        param['name'] = issueParamUpdate['otherLocale.name'] 
        ret = MbDanWeiChangSuoIntf.checkViewother( companyDict = param, id = issueParamUpdate['otherLocale.id'], username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '重点场所--其他场所修改信息查找失败' )
        Time.wait( 1 )
            
        # PC端检查
        paramPC = copy.deepcopy( MbDanWeiChangSuoPara.otherPcCheck )
        paramPC['name'] = issueParamUpdate['otherLocale.name'] 
        ret = MbDanWeiChangSuoIntf.checkOther( companyDict = paramPC, username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '重点场所--其他场所PC端查找失败' ) 

        pass 
    
        '''
    @功能：组织机构--社会组织新增,修改
    @ lhz  2016-3-4
    ''' 
    def testmDanWei_006( self ):
        '''组织机构--社会组织新增'''
        # 新增单位信息
        xfParam = copy.deepcopy( MbDanWeiChangSuoPara.organizationsAddOrUpdate )
        xfParam['tqmobile'] = 'true'
        xfParam['newSocietyOrganizations.subType.id'] = CommonIntf.getIdByDomainAndDisplayName( domainName = '社会组织类型', displayName = '社会团体' )
        xfParam['newSocietyOrganizations.type.id'] = CommonIntf.getIdByDomainAndDisplayName( domainName = '社会组织类型分类', displayName = '行业性团体' )
        xfParam['newSocietyOrganizations.name'] = '社会组织%s' % CommonUtil.createRandomString( 6 ) 
        xfParam['organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        xfParam['newSocietyOrganizations.legalPerson'] = '校长'
        xfParam['newSocietyOrganizations.address'] = '中科院'
        ret = MbDanWeiChangSuoIntf.shzzAdd( param = xfParam, username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '组织机构--社会组织新增信息失败' )
        Time.wait( 1 )
        # 检查
        param = copy.deepcopy( MbDanWeiChangSuoPara.organizationsListCheck )
        param['name'] = xfParam['newSocietyOrganizations.name'] 
        param['legalPerson'] = xfParam['newSocietyOrganizations.legalPerson']
        param['address'] = xfParam['newSocietyOrganizations.address'] 
        ret = MbDanWeiChangSuoIntf.check_Organizations( companyDict = param, typeName = '组织机构--社会组织新增信息', orgId = InitDefaultPara.orgInit['DftWangGeOrgId'], username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '组织机构--社会组织新增信息查找失败' )
        Time.wait( 1 )
        # #检验在网格2下是否可以查看到网格1下新增的数据
        ret = MbDanWeiChangSuoIntf.check_Organizations( companyDict = param, typeName = '组织机构--社会组织新增信息网格2下查找网格1的数据', orgId = InitDefaultPara.orgInit['DftWangGeOrgId1'], username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertFalse( ret, '组织机构--社会组织新增信息网格2下查找网格1的数据失败' )   
        Time.wait( 1 )            
        # 修改
        issueParamUpdate = copy.deepcopy( MbDanWeiChangSuoPara.organizationsAddOrUpdate )
        issueParamUpdate['tqmobile'] = 'true'
        issueParamUpdate['newSocietyOrganizations.id'] = CommonIntf.getDbQueryResult( dbCommand = "select t.id from newSocietyOrganizations t  where t.name = '%s'" % xfParam['newSocietyOrganizations.name'] )
        issueParamUpdate['newSocietyOrganizations.subType.id'] = CommonIntf.getIdByDomainAndDisplayName( domainName = '社会组织类型', displayName = '民办非企业' )
        issueParamUpdate['newSocietyOrganizations.type.id'] = CommonIntf.getIdByDomainAndDisplayName( domainName = '社会组织类型分类', displayName = '教育事业' )
        issueParamUpdate['newSocietyOrganizations.name'] = '社会组织%s' % CommonUtil.createRandomString( 6 ) 
        issueParamUpdate['organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        issueParamUpdate['newSocietyOrganizations.legalPerson'] = '校长2'
        issueParamUpdate['newSocietyOrganizations.address'] = '中科院2'  
        ret = MbDanWeiChangSuoIntf.shzzEdit( param = issueParamUpdate, username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '组织机构--社会组织修改信息失败' )
        Time.wait( 1 )
        # 检查
        param = copy.deepcopy( MbDanWeiChangSuoPara.organizationsListCheck )
        param['name'] = issueParamUpdate['newSocietyOrganizations.name'] 
        param['legalPerson'] = issueParamUpdate['newSocietyOrganizations.legalPerson']
        param['address'] = issueParamUpdate['newSocietyOrganizations.address'] 
        ret = MbDanWeiChangSuoIntf.checkViewOrganizations( companyDict = param, typeName = '组织机构--社会组织信息修改', id = issueParamUpdate['newSocietyOrganizations.id'], username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '组织机构--社会组织修改查找失败' )
        Time.wait( 1 )
               
             
        # PC端检查
        paramPC = copy.deepcopy( MbDanWeiChangSuoPara.otherPcCheck )
        paramPC['name'] = issueParamUpdate['newSocietyOrganizations.name'] 
        ret = MbDanWeiChangSuoIntf.checkPcOrganizations( companyDict = paramPC, typeName = '组织机构--社会组织信息', username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '组织机构--社会组织信息PC端查找失败' ) 

        pass  
       
    '''
    @功能：企业--规上企业 新增，修改
    @ lhz  2016-3-4
    ''' 
    def testmDanWei_007( self ):
        '''企业--规上企业新增'''
        # 新增单位信息
        issueParam = copy.deepcopy( MbDanWeiChangSuoPara.aqsczdAddPara ) 
        issueParam ['tqmobile'] = 'true'
        issueParam['enterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName( domainName = '企业类型', displayName = '规上企业' ) 
        issueParam['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        issueParam['enterprise.name'] = '企业%s' % CommonUtil.createRandomString( 6 )   
        issueParam['enterprise.keyType'] = 'enterpriseKey'
        issueParam['enterprise.address'] = '地址2'
        issueParam['enterprise.legalPerson'] = '代表2'
        ret = MbDanWeiChangSuoIntf.aqsczdAdd( issueParam, typeName = '企业--规上企业新增信息', username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '企业--规上企业信息新增信息失败' )
        Time.wait( 1 )
        # 检查参数
        param = copy.deepcopy( MbDanWeiChangSuoPara.aqsczdCheck )
        # 获取组织机构id
        param['name'] = issueParam['enterprise.name']
        # 获取查询参数
        param['address'] = issueParam['enterprise.address'] 
        param['legalPerson'] = issueParam['enterprise.legalPerson'] 
        ret = MbDanWeiChangSuoIntf.check_aqsczd( companyDict = param, typeName = '企业--规上企业新增信息', keyType = 'enterpriseKey', orgId = InitDefaultPara.orgInit['DftWangGeOrgId'], username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '企业--规上企业信息新增查找失败' )
        Time.wait( 1 )
        # 检验在网格2下是否可以查看到网格1下新增的数据
        ret = MbDanWeiChangSuoIntf.check_aqsczd( companyDict = param, typeName = '企业--规上企业信息在网格2下查找网格1的数据', keyType = 'enterpriseKey', orgId = InitDefaultPara.orgInit['DftWangGeOrgId1'], username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertFalse( ret, '企业--规上企业信息在网格2下查找网格1的数据失败' )
        Time.wait( 1 )
        # 修改
        issueParamUpdate = copy.deepcopy( MbDanWeiChangSuoPara.apsczdUpdateParam ) 
        issueParamUpdate['enterprise.id'] = CommonIntf.getDbQueryResult( dbCommand = "select t.id from enterprises t  where t.name= '%s'" % issueParam['enterprise.name'] )
        issueParamUpdate['enterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName( domainName = '企业类型', displayName = '规下企业' ) 
        issueParamUpdate['placeTypeName'] = '安全生产重点'
        issueParamUpdate['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        issueParamUpdate['enterprise.name'] = '企业%s' % CommonUtil.createRandomString( 6 )   
        issueParamUpdate['enterprise.keyType'] = 'enterpriseKey'
        issueParamUpdate['enterprise.address'] = '修改地址2'
        issueParamUpdate['enterprise.legalPerson'] = '修改代表2'    
        ret = MbDanWeiChangSuoIntf.aqsczdUpdate( issueParamUpdate, typeName = '企业--规上企业修改信息', username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '企业--规上企业信息修改信息失败' )      
        Time.wait( 1 )
        # 检查参数
        param = copy.deepcopy( MbDanWeiChangSuoPara.aqsczdCheck )
        # 获取组织机构id
        param['name'] = issueParamUpdate['enterprise.name']
        # 获取查询参数
        param['address'] = issueParamUpdate['enterprise.address'] 
        param['legalPerson'] = issueParamUpdate['enterprise.legalPerson'] 
        ret = MbDanWeiChangSuoIntf.check_Viewaqsczd( companyDict = param, typeName = '企业--规上企业修改信息', id = issueParamUpdate['enterprise.id'], username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '企业--规上企业修改信息查找失败' )              
        Time.wait( 1 )
        # PC端检查
        paramPC = copy.deepcopy( MbDanWeiChangSuoPara.ChaKanAnQuanShengChan )
        paramPC['name'] = issueParamUpdate['enterprise.name']
        ret = MbDanWeiChangSuoIntf.checkCompany( companyDict = paramPC, orgId = issueParamUpdate['ownerOrg.id'], keyType = 'enterpriseKey', username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '企业--规上企业信息PC端查找失败' ) 
 
        pass
    
    
    '''
    @功能：重点场所--安全生产重点新增巡场情况
    @ lhz  2016-2-29
    ''' 
    def testmDanWei_008( self ):
        '''重点场所--安全生产重点新增巡场情况'''
        # 新增单位信息
        issueParam = copy.deepcopy( MbDanWeiChangSuoPara.aqsczdAddPara ) 
        issueParam ['tqmobile'] = 'true'
        issueParam['enterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName( domainName = '企业类型', displayName = '规上企业' ) 
        issueParam['placeTypeName'] = '安全生产重点'
        issueParam['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        issueParam['enterprise.name'] = '安全生产重点%s' % CommonUtil.createRandomString( 6 )   
        issueParam['enterprise.keyType'] = 'safetyProductionKey'
        issueParam['enterprise.address'] = '地址2'
        issueParam['enterprise.legalPerson'] = '代表2'
        ret = MbDanWeiChangSuoIntf.aqsczdAdd( issueParam, typeName = '安全生产重点信息', username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '安全生产重点信息新增失败' )
        Time.wait( 1 )
        # 成员库新增
        ParamMember = copy.deepcopy( XiaQuGuanLiPara.personParam )   
        ParamMember['serviceTeamMemberBase.org.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        ParamMember['serviceTeamMemberBase.name'] = '服务%s' % CommonUtil.createRandomString( 6 ) 
        ParamMember['serviceTeamMemberBase.gender.id'] = CommonIntf.getIdByDomainAndDisplayName( domainName = '性别(男、女)', displayName = '男' ) 
        ParamMember['serviceTeamMemberBase.mobile'] = random.choice( ['139', '188', '185', '136', '158', '151'] ) + "".join( random.choice( "0123456789" ) for i in range( 8 ) )
        ParamMember['isSubmit'] = 'true' 
        ret = XiaQuGuanLiIntf.memberAdd( param = ParamMember, username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )        
        self.assertTrue( ret, '成员库新增失败' )  
        Time.wait( 1 )
        # 巡场情况新增
        xcParam = copy.deepcopy( MbDanWeiChangSuoPara.xunChangAddParam )
        xcParam['serviceRecord_organization_id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        xcParam['serviceRecord_teamId'] = 0
        xcParam['serviceRecord.occurDate'] = Time.getCurrentDate()
        xcParam['serviceRecord.recordType'] = '1'  # 0代表排查类，1代表整改类
        xcParam['serviceRecord_userOrgId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        xcParam['mode'] = 'add'
        # 安全重点场所id
        objectId = CommonIntf.getDbQueryResult( dbCommand = "select t.id from enterprises t  where t.name= '%s'" % issueParam['enterprise.name'] )
        xcParam['serviceRecord_serviceObjects'] = "%s-%s-%s" % ( objectId, issueParam['enterprise.name'], 'SAFETYPRODUCTIONKEY' )
        xcParam['serviceRecord.occurPlace'] = '学院路'
        # 成员库id
        memberId = CommonIntf.getDbQueryResult( dbCommand = "select t.id from SERVICETEAMMEMBERBASE t  where t.name ='%s'" % ParamMember['serviceTeamMemberBase.name'] )
        xcParam['serviceRecord.serviceMembers'] = "%s-%s-%s" % ( memberId, ParamMember['serviceTeamMemberBase.name'], xcParam['serviceRecord_teamId'] )
        ret = MbDanWeiChangSuoIntf.xunChangAdd( xcParam, username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '巡场情况新增信息失败' )
        Time.wait( 1 )
        # 验证列表中是否存在
        param = copy.deepcopy( MbDanWeiChangSuoPara.xunChangCheckParam )
        # 获取组织机构id
        param['occurPlace'] = xcParam['serviceRecord.occurPlace']
        # 获取查询参数
        param['occurDate'] = Time.getCurrentDate()
        param['serviceMembers'] = ParamMember['serviceTeamMemberBase.name'] 
        objectId = CommonIntf.getDbQueryResult( dbCommand = "select t.id from enterprises t  where t.name= '%s'" % issueParam['enterprise.name'] )
        ret = MbDanWeiChangSuoIntf.check_xunChang( companyDict = param, objectId = objectId, username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '巡场情况查找失败' )    
        Time.wait( 1 )
        
        # PC端检查
        paramPC = copy.deepcopy( MbDanWeiChangSuoPara.ChaKanAnQuanShengChan )
        paramPC['occurPlace'] = xcParam['serviceRecord.occurPlace']
        # 获取查询参数
        paramPC['occurDate'] = Time.getCurrentDate()
        paramPC['serviceMembers'] = ParamMember['serviceTeamMemberBase.name']
        objectId = CommonIntf.getDbQueryResult( dbCommand = "select t.id from enterprises t  where t.name= '%s'" % issueParam['enterprise.name'] ) 
        ret = MbDanWeiChangSuoIntf.check_xunChangPc( companyDict = paramPC, objectId = objectId, username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '安全生产重点PC端查找失败' ) 
  
        pass    
     
    
    '''
    @功能：列表和查询（安全生产重点，消防安全重点，治安重点，规上企业）
    @ lhz  2016-2-29
    ''' 
    def testmDanWei_009( self ):
        '''重点场所--安全生产重点搜索'''
        # 新增单位信息
        issueParam = copy.deepcopy( MbDanWeiChangSuoPara.aqsczdAddPara ) 
        issueParam['enterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName( domainName = '企业类型', displayName = '规上企业' ) 
        issueParam['placeTypeName'] = '安全生产重点'
        issueParam['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        issueParam['enterprise.name'] = '安全生产重点%s' % CommonUtil.createRandomString( 6 )   
        issueParam['enterprise.keyType'] = 'safetyProductionKey'
        issueParam['enterprise.address'] = '地址2'
        issueParam['enterprise.legalPerson'] = '代表2'
        ret = MbDanWeiChangSuoIntf.aqsczdAdd( issueParam, typeName = '安全生产重点信息', username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '安全生产重点信息新增失败' )
        Time.wait( 1 )
        # 新增第二条单位信息
        issueParam2 = copy.deepcopy( MbDanWeiChangSuoPara.aqsczdAddPara ) 
        issueParam2['enterprise.type.id'] = CommonIntf.getIdByDomainAndDisplayName( domainName = '企业类型', displayName = '规上企业' ) 
        issueParam2['placeTypeName'] = '安全生产重点'
        issueParam2['ownerOrg.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        issueParam2['enterprise.name'] = '安全生产重点%s' % CommonUtil.createRandomString( 6 )   
        issueParam2['enterprise.keyType'] = 'safetyProductionKey'
        issueParam2['enterprise.address'] = '地址2'
        issueParam2['enterprise.legalPerson'] = '代表2'
        ret = MbDanWeiChangSuoIntf.aqsczdAdd( issueParam2, typeName = '安全生产重点信息', username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '安全生产重点信息新增失败' )        
        Time.wait( 1 )
        
        # 检查参数
        param = copy.deepcopy( MbDanWeiChangSuoPara.searchParam )
        # 根据场所名称查询【期望中的】
        param['enterpriseSearchCondition.name'] = issueParam['enterprise.name']
        ret = MbDanWeiChangSuoIntf.searchAqsc( companyDict = param, username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '安全生产重点信息高级搜索【期望中的】查找失败' )
        Time.wait( 1 )
        # 根据场所名称查询【不期望中的】
        param = copy.deepcopy( MbDanWeiChangSuoPara.searchParam )
        param['enterpriseSearchCondition.name'] = issueParam['enterprise.name']
        ret = MbDanWeiChangSuoIntf.searchAqscNot( companyDict = param, unit = issueParam2['enterprise.name'], username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertFalse( ret, '安全生产重点信息高级搜索【不期望中的】查找失败' )
      
        pass   
    
    '''
    @功能：组织机构-社会组织高级搜索
    @ lhz  2016-3-3
    ''' 
    def testmDanWei_010( self ):
        xfParam = copy.deepcopy( MbDanWeiChangSuoPara.organizationsAddOrUpdate )
        xfParam['tqmobile'] = 'true'
        xfParam['newSocietyOrganizations.subType.id'] = CommonIntf.getIdByDomainAndDisplayName( domainName = '社会组织类型', displayName = '社会团体' )
        xfParam['newSocietyOrganizations.type.id'] = CommonIntf.getIdByDomainAndDisplayName( domainName = '社会组织类型分类', displayName = '行业性团体' )
        xfParam['newSocietyOrganizations.name'] = '社会组织%s' % CommonUtil.createRandomString( 6 ) 
        xfParam['organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        xfParam['newSocietyOrganizations.legalPerson'] = '校长'
        xfParam['newSocietyOrganizations.address'] = '中科院'
        ret = MbDanWeiChangSuoIntf.shzzAdd( param = xfParam, username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '组织机构--社会组织新增信息失败' )
        Time.wait( 1 )
        
        # 新增单位信息
        xfParam2 = copy.deepcopy( MbDanWeiChangSuoPara.organizationsAddOrUpdate )
        xfParam2['tqmobile'] = 'true'
        xfParam2['newSocietyOrganizations.subType.id'] = CommonIntf.getIdByDomainAndDisplayName( domainName = '社会组织类型', displayName = '社会团体' )
        xfParam2['newSocietyOrganizations.type.id'] = CommonIntf.getIdByDomainAndDisplayName( domainName = '社会组织类型分类', displayName = '行业性团体' )
        xfParam2['newSocietyOrganizations.name'] = '社会组织%s' % CommonUtil.createRandomString( 6 ) 
        xfParam2['organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        xfParam2['newSocietyOrganizations.legalPerson'] = '校长'
        xfParam2['newSocietyOrganizations.address'] = '中科院'
        ret = MbDanWeiChangSuoIntf.shzzAdd( param = xfParam2, username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '组织机构--社会组织新增信息失败' )
        Time.wait( 1 )
        # 检查【期望中的】
        param = copy.deepcopy( MbDanWeiChangSuoPara.searchZZcsParam )
        param['searchNewSocietyOrganizationsVo.unitName'] = xfParam['newSocietyOrganizations.name']
        ret = MbDanWeiChangSuoIntf.searchZzcs( companyDict = param, username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '组织机构--社会组织高级搜索查找失败' )
        Time.wait( 1 )
        # 检查【不是期望中的】
        param = copy.deepcopy( MbDanWeiChangSuoPara.searchZZcsParam )
        param['searchNewSocietyOrganizationsVo.unitName'] = xfParam['newSocietyOrganizations.name']
        ret = MbDanWeiChangSuoIntf.searchZzcsNot( companyDict = param, unit = xfParam2['newSocietyOrganizations.name'], username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertFalse( ret, '组织机构--社会组织高级搜索查找失败' )
                 


        '''
    @功能：重点场所--其他场所高级搜索
    @ lhz  2016-3-3
    ''' 
    def testmDanWei_011( self ):
        '''重点场所--其他场所新增'''
        # 新增单位信息
        xfParam = copy.deepcopy( MbDanWeiChangSuoPara.otherParamAddOrUpdate )
        xfParam['tqmobile'] = 'true'
        xfParam['otherLocale.type.id'] = CommonIntf.getIdByDomainAndDisplayName( domainName = '其他场所类型', displayName = '煤气点' )
        xfParam['otherLocale.name'] = '其他场所%s' % CommonUtil.createRandomString( 6 ) 
        xfParam['organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        xfParam['otherLocale.address'] = '学院路'
        xfParam['otherLocale.contactPerson'] = '张三'
        ret = MbDanWeiChangSuoIntf.OtherCSAdd( param = xfParam, username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '重点场所--其他场所新增信息失败' )
        Time.wait( 1 )
        
        xfParam2 = copy.deepcopy( MbDanWeiChangSuoPara.otherParamAddOrUpdate )
        xfParam2['tqmobile'] = 'true'
        xfParam2['otherLocale.type.id'] = CommonIntf.getIdByDomainAndDisplayName( domainName = '其他场所类型', displayName = '煤气点' )
        xfParam2['otherLocale.name'] = '其他场所%s' % CommonUtil.createRandomString( 6 ) 
        xfParam2['organization.id'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        xfParam2['otherLocale.address'] = '学院路'
        xfParam2['otherLocale.contactPerson'] = '张三'
        ret = MbDanWeiChangSuoIntf.OtherCSAdd( param = xfParam2, username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '重点场所--其他场所新增信息失败' ) 
        Time.wait( 1 )
                
        # 检查【期望中的】
        param = copy.deepcopy( MbDanWeiChangSuoPara.searchOtherParam )
        param['searchOtherLocaleVo.name'] = xfParam['otherLocale.name']
        ret = MbDanWeiChangSuoIntf.searchOther( companyDict = param, username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '组织机构--社会组织高级搜索查找失败' )
        Time.wait( 1 )
        # 检查【不是期望中的】
        param = copy.deepcopy( MbDanWeiChangSuoPara.searchOtherParam )
        param['searchOtherLocaleVo.name'] = xfParam['otherLocale.name']
        ret = MbDanWeiChangSuoIntf.searchOtherNot( companyDict = param, unit = xfParam2['otherLocale.name'], username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertFalse( ret, '组织机构--社会组织高级搜索查找失败' )
     
    '''
    @功能：重点场所--学校高级搜索 查询名称有问题，待开发弄好后再改
    @ lhz  2016-3-3
    ''' 
    def testmDanWei_012( self ):
        '''重点场所--学校新增'''
        # 新增单位信息
        xfParam = copy.deepcopy( MbDanWeiChangSuoPara.schoolParam )
        xfParam['tqmobile'] = 'true'
        xfParam['school.kind.id'] = CommonIntf.getIdByDomainAndDisplayName( domainName = '学校性质', displayName = '公办' )
        xfParam['school.type.id'] = CommonIntf.getIdByDomainAndDisplayName( domainName = '学校类型', displayName = '小学' )
        xfParam['school.president'] = '王校长'
        xfParam['orgId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        xfParam['school.chineseName'] = '学校%s' % CommonUtil.createRandomString( 6 ) 
        xfParam['school.address'] = '中原路'
        xfParam['school.hasCertificate'] = 'false'
        ret = MbDanWeiChangSuoIntf.schoolAdd( xfParam, username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '重点场所--学校新增信息失败' )   
        Time.wait( 1 )
        # 新增第二条数据
        xfParam2 = copy.deepcopy( MbDanWeiChangSuoPara.schoolParam )
        xfParam2['tqmobile'] = 'true'
        xfParam2['school.kind.id'] = CommonIntf.getIdByDomainAndDisplayName( domainName = '学校性质', displayName = '公办' )
        xfParam2['school.type.id'] = CommonIntf.getIdByDomainAndDisplayName( domainName = '学校类型', displayName = '小学' )
        xfParam2['school.president'] = '王校长'
        xfParam2['orgId'] = InitDefaultPara.orgInit['DftWangGeOrgId']
        xfParam2['school.chineseName'] = '学校%s' % CommonUtil.createRandomString( 6 ) 
        xfParam2['school.address'] = '中原路'
        xfParam2['school.hasCertificate'] = 'false'
        ret = MbDanWeiChangSuoIntf.schoolAdd( xfParam2, username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '重点场所--学校新增信息失败' )   
        Time.wait( 1 )
                        
        # 检查【期望中的】
        param = copy.deepcopy( MbDanWeiChangSuoPara.schoolSearchParam )
        param['location.president'] = xfParam['school.president']
        ret = MbDanWeiChangSuoIntf.searchSchool( companyDict = param, username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertTrue( ret, '重点场所--学校高级搜索查找失败' )
        Time.wait( 1 )
        # 检查【不是期望中的】
        param = copy.deepcopy( MbDanWeiChangSuoPara.searchOtherParam )
        param['location.president'] = xfParam['school.president']
        ret = MbDanWeiChangSuoIntf.searchSchoolNot( companyDict = param, unit = xfParam2['school.president'], username = InitDefaultPara.userInit['DftWangGeUser'], password = '11111111' )
        self.assertFalse( ret, '重点场所--学校高级搜索查找失败' )
        
        
  
    
    def tearDown( self ):
            pass
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest( DanWeiChangSuo( "testmDanWei_002" ) )
    
#     suite.addTest(DanWeiChangSuo("testmDanWei_001"))
#    suite.addTest(DanWeiChangSuo("testmDanWei_004"))
#    suite.addTest(DanWeiChangSuo("testmDanWei_005"))
#    suite.addTest(DanWeiChangSuo("testmDanWei_004"))
#     suite.addTest(DanWeiChangSuo("testmDanWei_006")) 
#     suite.addTest(DanWeiChangSuo("testmDanWei_007"))  
#    suite.addTest(DanWeiChangSuo("testmDanWei_008"))  
#    suite.addTest(DanWeiChangSuo("testmDanWei_009")) 
#    suite.addTest(DanWeiChangSuo("testmDanWei_010")) 
#    suite.addTest(DanWeiChangSuo("testmDanWei_011")) 
#     suite.addTest(DanWeiChangSuo("testmDanWei_012")) 
#    suite.addTest(DanWeiChangSuo("testmDanWei_008")) 


     
    
  
    results = unittest.TextTestRunner().run( suite )
    pass
        
    
            
    
    
    
    
    
