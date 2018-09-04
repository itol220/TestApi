# -*- coding:UTF-8 -*-
'''
Created on 2016-6-13

@author: N-66
'''
import copy
import unittest
from Interface.XiaoFangXiTong import xiaoFangXiTongHttpCommon
from CONFIG.Define import LogLevel
from Interface.XiaoFangXiTong.XuanChuanPeiXun import XuanChuanPeiXunIntf,\
    XuanChuanPeiXunPara
from COMMON import CommonUtil,Log
from Interface.XiaoFangXiTong.SystemMgr import SystemMgrIntf
from Interface.XiaoFangXiTong.Common import CommonIntf,\
    InitDefaultPara
from Interface.XiaoFangXiTong.YinHuanDuGai import YinHuanDuGaiIntf,\
    YinHuanDuGaiPara

class XuanChuanPeiXun(unittest.TestCase): 

    def setUp(self):
        SystemMgrIntf.initEnv()   
     
        pass 
    def testCase_001(self):
#新增培训活动(企业手动添加）
        AddPeiXunHuoDongParam1=copy.deepcopy(XuanChuanPeiXunPara.AddPeiXunHuoDong)
        AddPeiXunHuoDongParam1['fireTrainingInfo.name']='培训名称%s'%CommonUtil.createRandomString()
        AddPeiXunHuoDongParam1['fireTrainingInfo.trainingNo']=CommonIntf.getDbQueryResult(dbCommand="select  max(t.training_no) from  fire_training_info t")
        AddPeiXunHuoDongParam1['fireTrainingCompany']='0_测试企业_企业负责人_13989764532'
        response=XuanChuanPeiXunIntf.Add_PeiXunHuoDong(PeiXunHuoDongDict=AddPeiXunHuoDongParam1, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        Log.LogOutput(LogLevel.INFO, "新增培训活动成功")
#新增培训活动（企业选择列表中已经有的企业）,先新增一家企业
        QiYeParam = copy.deepcopy(YinHuanDuGaiPara.fireCompanyDict) 
        QiYeParam['mode'] = 'add'  
        QiYeParam['fireCompanyInfo.createDept'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from ORGANIZATIONS t where t.Orgname='%s'"%InitDefaultPara.orgInit['DftWangGeOrg']) 
        QiYeParam['fireCompanyInfo.importOrAdd'] = '1'
        QiYeParam['fireCompanyInfo.orgPathName'] = '%s%s%s%s%s'%(InitDefaultPara.orgInit['DftShiOrg'],InitDefaultPara.orgInit['DftQuOrg'],InitDefaultPara.orgInit['DftJieDaoOrg'],InitDefaultPara.orgInit['DftSheQuOrg'],InitDefaultPara.orgInit['DftWangGeOrg'])
        QiYeParam['fireCompanyInfo.companyName'] = '宣传培训单位%s'%CommonUtil.createRandomString()
        QiYeParam['fireCompanyInfo.orgid'] = QiYeParam['fireCompanyInfo.createDept']
        QiYeParam['companySuperviseTypeIsChange'] = 'true'
        QiYeParam['fireCompanyInfo.superviseTypeName'] = '其他一般单位'
        QiYeParam['fireCompanyInfo.superviseType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%InitDefaultPara.orgInit['DftQuOrg'])
        QiYeParam['fireCompanyInfo.address'] = '测试地址'
        QiYeParam['fireCompanyInfo.manger'] = '测试姓名'
        QiYeParam['fireCompanyInfo.managerTelephone'] = '18710000000'
        QiYeParam['fireCompanyInfo.rentHousePerson'] = '0'
        QiYeParam['fireCompanyInfo.industrialCatalogue'] = CommonIntf.getDbQueryResult(dbCommand = "select t.code from fire_company_type t where t.name='电器'")  #行业类别
        QiYeParam['businessLicense'] = '1'
        QiYeParam['firelicense'] = '1'
        YinHuanDuGaiIntf.addOrEdit_fireCompany(QiYeParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        AddPeiXunHuoDongParam2=copy.deepcopy(XuanChuanPeiXunPara.AddPeiXunHuoDong)
        AddPeiXunHuoDongParam2['fireTrainingInfo.name']='培训名称%s'%CommonUtil.createRandomString()
        AddPeiXunHuoDongParam2['fireTrainingInfo.trainingNo']=CommonIntf.getDbQueryResult(dbCommand="select  max(t.training_no) from  fire_training_info t")
        AddPeiXunHuoDongParam2['fireTrainingCompany']='%s_%s_%s_%s'%(CommonIntf.getDbQueryResult(dbCommand="select t.fire_company_info_id from fire_company_info t where t.company_name='%s'"%QiYeParam['fireCompanyInfo.companyName']),QiYeParam['fireCompanyInfo.companyName'],QiYeParam['fireCompanyInfo.manger'],QiYeParam['fireCompanyInfo.managerTelephone'])
        XuanChuanPeiXunIntf.Add_PeiXunHuoDong(PeiXunHuoDongDict=AddPeiXunHuoDongParam2, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        print AddPeiXunHuoDongParam2['fireTrainingCompany']
        Log.LogOutput(LogLevel.INFO, "新增培训活动成功")
# 新增后列表中查看培训活动(企业手动添加）
        PeiXunHuoDongParam1=copy.deepcopy(XuanChuanPeiXunPara.PeiXunHuoDong)
        PeiXunHuoDongParam1['fireTrainingInfoId']=CommonIntf.getDbQueryResult(dbCommand="select t.fire_training_info_id from fire_training_info t where t.name='%s'"%AddPeiXunHuoDongParam1['fireTrainingInfo.name'])
        PeiXunHuoDongParam1['name']=AddPeiXunHuoDongParam1['fireTrainingInfo.name']
        response=XuanChuanPeiXunIntf.Get_PeiXunHuoDong(PeiXunHuoDongDict=PeiXunHuoDongParam1, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(response, '培训活动查看失败')
#新增后列表查看培训活动（选择列表中已经存在的企业）
        PeiXunHuoDongParam2=copy.deepcopy(XuanChuanPeiXunPara.PeiXunHuoDong)
        PeiXunHuoDongParam2['fireTrainingInfoId']=CommonIntf.getDbQueryResult(dbCommand="select t.fire_training_info_id from fire_training_info t where t.name='%s'"%AddPeiXunHuoDongParam2['fireTrainingInfo.name'])
        PeiXunHuoDongParam2['name']=AddPeiXunHuoDongParam2['fireTrainingInfo.name']
        response=XuanChuanPeiXunIntf.Get_PeiXunHuoDong(PeiXunHuoDongDict=PeiXunHuoDongParam2, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(response, '培训活动查看失败')        
#修改培训活动
        EditPeiXunHuoDongParam1=copy.deepcopy(XuanChuanPeiXunPara.EditPeiXunHuoDong)
        EditPeiXunHuoDongParam1['fireTrainingInfo.name']='修改培训名称%s'%CommonUtil.createRandomString()
        EditPeiXunHuoDongParam1['fireTrainingInfo.trainingNo']=AddPeiXunHuoDongParam1['fireTrainingInfo.trainingNo']
        EditPeiXunHuoDongParam1['fireTrainingCompany']=AddPeiXunHuoDongParam1['fireTrainingCompany']
        EditPeiXunHuoDongParam1['fireTrainingInfo.fireTrainingInfoId']=CommonIntf.getDbQueryResult(dbCommand="select t.fire_training_info_id from fire_training_info t where t.name='%s'"%AddPeiXunHuoDongParam1['fireTrainingInfo.name'])
        response=XuanChuanPeiXunIntf.Edit_PeiXunHuoDong(PeiXunHuoDongDict=EditPeiXunHuoDongParam1, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        Log.LogOutput(LogLevel.INFO,'修改宣传培训成功..')
#修改后查看培训活动
        EditCheckPeiXunHuoDongParam1=copy.deepcopy(XuanChuanPeiXunPara.PeiXunHuoDong)
        EditCheckPeiXunHuoDongParam1['fireTrainingInfoId']=EditPeiXunHuoDongParam1['fireTrainingInfo.fireTrainingInfoId']
        EditCheckPeiXunHuoDongParam1['name']=EditPeiXunHuoDongParam1['fireTrainingInfo.name']
        response=XuanChuanPeiXunIntf.Get_PeiXunHuoDong(PeiXunHuoDongDict=EditCheckPeiXunHuoDongParam1, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(response, '培训活动查看失败')
#删除培训活动
        DelPeiXunHuoDongParam1=copy.deepcopy(XuanChuanPeiXunPara.DelPeiXunHuoDong)
        DelPeiXunHuoDongParam1['fireTrainingInfoId']=EditPeiXunHuoDongParam1['fireTrainingInfo.fireTrainingInfoId']
        response=XuanChuanPeiXunIntf.Del_PeiXunHuoDong(PeiXunHuoDongDict=DelPeiXunHuoDongParam1,username=InitDefaultPara.userInit['DftWangGeUser'],password='11111111')
        self.assertTrue(response, '培训活动删除失败')
#删除后列表查看
        DelCheckPeiXunHuoDongParam1=copy.deepcopy(XuanChuanPeiXunPara.PeiXunHuoDong)
        DelCheckPeiXunHuoDongParam1['fireTrainingInfoId']=EditPeiXunHuoDongParam1['fireTrainingInfo.fireTrainingInfoId']
        DelCheckPeiXunHuoDongParam1['name']=EditPeiXunHuoDongParam1['fireTrainingInfo.name']
        response=XuanChuanPeiXunIntf.Get_PeiXunHuoDong(PeiXunHuoDongDict=DelCheckPeiXunHuoDongParam1,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertFalse(response, '培训活动在列表中依然存在..')
        pass

    def testCase_002(self):
#新增宣传活动(企业手动添加）
        AddXuanChuanHuoDongParam1=copy.deepcopy(XuanChuanPeiXunPara.AddXuanChuanHuoDong)    
        AddXuanChuanHuoDongParam1['firePublicInfo.title']='宣传活动名称%s'%CommonUtil.createRandomString()
        AddXuanChuanHuoDongParam1['firePublicInfo.publicDate']='2016-6-14' 
        AddXuanChuanHuoDongParam1['firePublicInfo.address']='培训地点1'  
        AddXuanChuanHuoDongParam1['firePublicInfo.hostUnit']='主办地点1'
        AddXuanChuanHuoDongParam1['firePublicInfo.organizeUser']='组织人1'
        AddXuanChuanHuoDongParam1['firePublicCompany']='undefined_测试单位手动添加1_负责人手动1_13976545454'
        response=XuanChuanPeiXunIntf.Add_XuanChuanHuoDong(XuanChuanHuoDongDict=AddXuanChuanHuoDongParam1,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        Log.LogOutput(LogLevel.INFO,'新增宣传活动成功..')
#新增宣传活动（企业在列表中选择）先新增一家企业
        QiYeParam = copy.deepcopy(YinHuanDuGaiPara.fireCompanyDict) 
        QiYeParam['mode'] = 'add'  
        QiYeParam['fireCompanyInfo.createDept'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from ORGANIZATIONS t where t.Orgname='%s'"%InitDefaultPara.orgInit['DftWangGeOrg']) 
        QiYeParam['fireCompanyInfo.importOrAdd'] = '1'
        QiYeParam['fireCompanyInfo.orgPathName'] = '%s%s%s%s%s'%(InitDefaultPara.orgInit['DftShiOrg'],InitDefaultPara.orgInit['DftQuOrg'],InitDefaultPara.orgInit['DftJieDaoOrg'],InitDefaultPara.orgInit['DftSheQuOrg'],InitDefaultPara.orgInit['DftWangGeOrg'])
        QiYeParam['fireCompanyInfo.companyName'] = '宣传培训单位%s'%CommonUtil.createRandomString()
        QiYeParam['fireCompanyInfo.orgid'] = QiYeParam['fireCompanyInfo.createDept']
        QiYeParam['companySuperviseTypeIsChange'] = 'true'
        QiYeParam['fireCompanyInfo.superviseTypeName'] = '其他一般单位'
        QiYeParam['fireCompanyInfo.superviseType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%InitDefaultPara.orgInit['DftQuOrg'])
        QiYeParam['fireCompanyInfo.address'] = '测试地址'
        QiYeParam['fireCompanyInfo.manger'] = '测试姓名'
        QiYeParam['fireCompanyInfo.managerTelephone'] = '18710000000'
        QiYeParam['fireCompanyInfo.rentHousePerson'] = '0'
        QiYeParam['fireCompanyInfo.industrialCatalogue'] = CommonIntf.getDbQueryResult(dbCommand = "select t.code from fire_company_type t where t.name='电器'")  #行业类别
        QiYeParam['businessLicense'] = '1'
        QiYeParam['firelicense'] = '1'
        YinHuanDuGaiIntf.addOrEdit_fireCompany(QiYeParam, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        AddXuanChuanHuoDongParam2=copy.deepcopy(XuanChuanPeiXunPara.AddXuanChuanHuoDong)    
        AddXuanChuanHuoDongParam2['firePublicInfo.title']='宣传活动名称%s'%CommonUtil.createRandomString()
        AddXuanChuanHuoDongParam2['firePublicInfo.publicDate']='2016-6-14' 
        AddXuanChuanHuoDongParam2['firePublicInfo.address']='培训地点1'  
        AddXuanChuanHuoDongParam2['firePublicInfo.hostUnit']='主办地点1'
        AddXuanChuanHuoDongParam2['firePublicInfo.organizeUser']='组织人1'
        AddXuanChuanHuoDongParam2['firePublicCompany']='%s_%s_%s_%s'%(CommonIntf.getDbQueryResult(dbCommand="select t.fire_company_info_id from fire_company_info t where t.company_name='%s'"%QiYeParam['fireCompanyInfo.companyName']),QiYeParam['fireCompanyInfo.companyName'],QiYeParam['fireCompanyInfo.manger'],QiYeParam['fireCompanyInfo.managerTelephone'])
        XuanChuanPeiXunIntf.Add_XuanChuanHuoDong(XuanChuanHuoDongDict=AddXuanChuanHuoDongParam1,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        Log.LogOutput(LogLevel.INFO,'新增宣传活动成功..')
#新增后列表查看        
        XuanChuanHuoDongParam1=copy.deepcopy(XuanChuanPeiXunPara.XuanChuanHuoDong)
        XuanChuanHuoDongParam1['title']=AddXuanChuanHuoDongParam1['firePublicInfo.title']
        XuanChuanHuoDongParam1['firePublicInfoId']=CommonIntf.getDbQueryResult(dbCommand="select t.fire_public_info_id from fire_public_info t where t.title='%s'"%AddXuanChuanHuoDongParam1['firePublicInfo.title'])
        response=XuanChuanPeiXunIntf.Get_XuanChuanHuoDong(XuanChuanHuoDongDict=XuanChuanHuoDongParam1,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(response,'宣传活动查看失败')
#新增后列表查看宣传活动（企业在列表中选择）
        XuanChuanHuoDongParam2=copy.deepcopy(XuanChuanPeiXunPara.XuanChuanHuoDong)
        XuanChuanHuoDongParam2['title']=AddXuanChuanHuoDongParam2['firePublicInfo.title']
        XuanChuanHuoDongParam2['firePublicInfoId']=CommonIntf.getDbQueryResult(dbCommand="select t.fire_public_info_id from fire_public_info t where t.title='%s'"%AddXuanChuanHuoDongParam2['firePublicInfo.title'])
        response=XuanChuanPeiXunIntf.Get_XuanChuanHuoDong(XuanChuanHuoDongDict=XuanChuanHuoDongParam1,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(response,'宣传活动查看失败')
#修改宣传活动
        EditXuanChuanHuoDongParam1=copy.deepcopy(XuanChuanPeiXunPara.EditXuanChuanHuoDong)
        EditXuanChuanHuoDongParam1['firePublicInfo.title']='修改宣传活动名称%s'%CommonUtil.createRandomString()
        EditXuanChuanHuoDongParam1['firePublicInfo.publicDate']='2016-6-14'
        EditXuanChuanHuoDongParam1['firePublicInfo.publicDate']='2016-6-14' 
        EditXuanChuanHuoDongParam1['firePublicInfo.address']='培训地点2'  
        EditXuanChuanHuoDongParam1['firePublicInfo.hostUnit']='主办地点2'
        EditXuanChuanHuoDongParam1['firePublicInfo.organizeUser']='组织人2'
        EditXuanChuanHuoDongParam1['firePublicInfo.firePublicInfoId']=XuanChuanHuoDongParam1['firePublicInfoId']
        EditXuanChuanHuoDongParam1['firePublicCompany']='%s__测试单位手动添加1_负责人手动1_13976545454'%EditXuanChuanHuoDongParam1['firePublicInfo.firePublicInfoId']
        response=XuanChuanPeiXunIntf.Edit_XuanChuanHuoDong(XuanChuanHuoDongDict=EditXuanChuanHuoDongParam1, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        Log.LogOutput(LogLevel.INFO,'修改宣传活动成功..')
#修改后列表中查看       
        EditCheckXuanChuanHuoDongParam1=copy.deepcopy(XuanChuanPeiXunPara.XuanChuanHuoDong)
        EditCheckXuanChuanHuoDongParam1['title']=EditXuanChuanHuoDongParam1['firePublicInfo.title']
        EditCheckXuanChuanHuoDongParam1['firePublicInfoId']=CommonIntf.getDbQueryResult(dbCommand="select t.fire_public_info_id from fire_public_info t where t.title='%s'"%EditXuanChuanHuoDongParam1['firePublicInfo.title'])
        response=XuanChuanPeiXunIntf.Get_XuanChuanHuoDong(XuanChuanHuoDongDict=EditCheckXuanChuanHuoDongParam1,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertTrue(response,'宣传活动查看失败')
#删除宣传活动
        DelXuanChuanHuoDongParam1=copy.deepcopy(XuanChuanPeiXunPara.DelXuanChuanHuoDong)
        DelXuanChuanHuoDongParam1['firePublicInfoId']=EditXuanChuanHuoDongParam1['firePublicInfo.firePublicInfoId']  
        response=XuanChuanPeiXunIntf.Del_XuanChuanHuoDong(XuanChuanHuoDongDict=DelXuanChuanHuoDongParam1, username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')     
        Log.LogOutput(LogLevel.INFO,'删除宣传活动成功..')
#删除后列表查看
        DelCheckXuanChuanHuoDongParam1=copy.deepcopy(XuanChuanPeiXunPara.XuanChuanHuoDong)
        DelCheckXuanChuanHuoDongParam1['title']=EditXuanChuanHuoDongParam1['firePublicInfo.title']
        DelCheckXuanChuanHuoDongParam1['firePublicInfoId']=EditCheckXuanChuanHuoDongParam1['firePublicInfoId']
        response=XuanChuanPeiXunIntf.Get_XuanChuanHuoDong(XuanChuanHuoDongDict=DelCheckXuanChuanHuoDongParam1,username=InitDefaultPara.userInit['DftWangGeUser'], password='11111111')
        self.assertFalse(response, '宣传活动在列表中依然存在')       
        pass
    def testCase_003(self):    
#新增学习资料
        AddXueXiZiLiaoParam=copy.deepcopy(XuanChuanPeiXunPara.AddXueXiZiLiao)
        AddXueXiZiLiaoParam['fireNotice.title']='学习资料标题%s'%CommonUtil.createRandomString()
        AddXueXiZiLiaoParam['signDeptIds']=InitDefaultPara.orgInit['DftWangGeOrgId']
        AddXueXiZiLiaoParam['fireNotice.createDeptName']=InitDefaultPara.orgInit['DftSheQuOrg']
        AddXueXiZiLiaoParam['fireNotice.createDept']=InitDefaultPara.orgInit['DftSheQuOrgId']
        AddXueXiZiLiaoParam['fireNotice.createUserName']=InitDefaultPara.userInit['DftSheQuUserXM']
        AddXueXiZiLiaoParam['fireNotice.createUser']=InitDefaultPara.userInit['DftSheQuUser']
        AddXueXiZiLiaoParam['fireNotice.noticeType']='1'
        response=XuanChuanPeiXunIntf.Add_XueXiZiLiao(XueXiZiLiaoDict=AddXueXiZiLiaoParam, username=InitDefaultPara.userInit['DftSheQuUser'],password='11111111')
        Log.LogOutput(LogLevel.INFO,'新增学习资料成功..')
#新增学习资料后列表查看         
        XueXiZiLiaoParam=copy.deepcopy(XuanChuanPeiXunPara.XueXiZiLiao)
        XueXiZiLiaoParam['simpleTitle']=AddXueXiZiLiaoParam['fireNotice.title']
        XueXiZiLiaoParam['fireNoticeId']=CommonIntf.getDbQueryResult(dbCommand="select t.fire_notice_id from fire_notice t where t.title ='%s'"%AddXueXiZiLiaoParam['fireNotice.title'])
        response=XuanChuanPeiXunIntf.Get_XueXiZiLiao(XueXiZiLiaoDict=XueXiZiLiaoParam, username=InitDefaultPara.userInit['DftSheQuUser'], password='11111111')
        self.assertTrue(response,'学习资料查看失败')
#修改学习资料        
        EditXueXiZiLiaoParam=copy.deepcopy(XuanChuanPeiXunPara.EditXueXiZiLiao)
        EditXueXiZiLiaoParam['fireNotice.title']='修改学习资料标题%s'%CommonUtil.createRandomString()
        EditXueXiZiLiaoParam['signDeptIds']=AddXueXiZiLiaoParam['signDeptIds']
        EditXueXiZiLiaoParam['fireNotice.createDeptName']=AddXueXiZiLiaoParam['fireNotice.createUserName']
        EditXueXiZiLiaoParam['fireNotice.createUserName']=AddXueXiZiLiaoParam['fireNotice.createUserName']
        EditXueXiZiLiaoParam['fireNotice.createUser']=AddXueXiZiLiaoParam['fireNotice.createUser']
        EditXueXiZiLiaoParam['fireNotice.noticeType']='1'
        EditXueXiZiLiaoParam['fireNotice.fireNoticeId']=CommonIntf.getDbQueryResult(dbCommand="select t.fire_notice_id from fire_notice t where t.title='%s'"%AddXueXiZiLiaoParam['fireNotice.title'])
        response=XuanChuanPeiXunIntf.Edit_XueXiZiLiao(EditXueXiZiLiaoParam,username=InitDefaultPara.userInit['DftSheQuUser'],password='11111111')
        print EditXueXiZiLiaoParam['fireNotice.fireNoticeId']
        Log.LogOutput(LogLevel.INFO,'修改学习资料成功..')
#修改后列表中查看
        EditCheckXueXiZiLiaoParam=copy.deepcopy(XuanChuanPeiXunPara.XueXiZiLiao)
        EditCheckXueXiZiLiaoParam['simpleTitle']=EditXueXiZiLiaoParam['fireNotice.title']
        EditCheckXueXiZiLiaoParam['fireNoticeId']=EditXueXiZiLiaoParam['fireNotice.fireNoticeId']
        response=XuanChuanPeiXunIntf.Get_XueXiZiLiao(XueXiZiLiaoDict=EditCheckXueXiZiLiaoParam,username=InitDefaultPara.userInit['DftSheQuUser'],password='11111111')
        self.assertTrue(response,'学习资料查看失败')
#删除学习资料
        DelXueXiZiLiaoParam=copy.deepcopy(XuanChuanPeiXunPara.DelXueXiZiLiao)
        DelXueXiZiLiaoParam['fireNoticeId']=EditCheckXueXiZiLiaoParam['fireNoticeId']
        XuanChuanPeiXunIntf.Del_XueXiZiLiao(DelXueXiZiLiaoParam,username=InitDefaultPara.userInit['DftSheQuUser'],password='11111111')
        Log.LogOutput(LogLevel.INFO,'删除学习资料成功..')
#删除后查看学习资料
        DelCheckXueXiZiLiaoParam=copy.deepcopy(XuanChuanPeiXunPara.XueXiZiLiao)
        DelCheckXueXiZiLiaoParam['simpleTitle']=EditXueXiZiLiaoParam['fireNotice.title']
        DelCheckXueXiZiLiaoParam['fireNoticeId']=EditXueXiZiLiaoParam['fireNotice.fireNoticeId']
        response=XuanChuanPeiXunIntf.Get_XueXiZiLiao(XueXiZiLiaoDict=EditCheckXueXiZiLiaoParam,username=InitDefaultPara.userInit['DftSheQuUser'],password='11111111')
        self.assertFalse(response,'学习资料在列表中依然存在')      
        
        
        
        
        
        
        pass
    
    
    
    
    
    
    def tearDown(self):    
        pass

if __name__ == "__main__":
    suite = unittest.TestSuite()
#     suite.addTest(XuanChuanPeiXun("testCase_001"))
#     suite.addTest(XuanChuanPeiXun("testCase_002"))
#     suite.addTest(XuanChuanPeiXun("testCase_003"))    
    results = unittest.TextTestRunner().run(suite)
    pass        