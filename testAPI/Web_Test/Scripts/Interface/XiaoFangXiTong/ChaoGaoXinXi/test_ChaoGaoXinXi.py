# -*- coding:UTF-8 -*-
'''
Created on 2016-6-16

@author: N-66
'''
from __future__ import unicode_literals
import unittest
from Interface.XiaoFangXiTong.SystemMgr import SystemMgrIntf
import copy
from Interface.XiaoFangXiTong.YinHuanDuGai import YinHuanDuGaiPara,\
    YinHuanDuGaiIntf
from Interface.XiaoFangXiTong.Common.InitDefaultPara import orgInit, userInit
from Interface.XiaoFangXiTong.Common import CommonIntf
from CONFIG.Define import LogLevel
from COMMON import Log, CommonUtil,Time
from Interface.XiaoFangXiTong.ChaoGaoXinXi import ChaoGaoXinXiPara
from Interface.XiaoFangXiTong.ChaoGaoXinXi import ChaoGaoXinXiIntf
from COMMON.CommonUtil import regMatchString
import string
class ChaoGaoXinXi(unittest.TestCase): 

    def setUp(self):
#         SystemMgrIntf.initEnv()
        pass 
    def testCase_001(self):
# # 新增单位类型类型
#         enterpriseType = copy.deepcopy(YinHuanDuGaiPara.saveSuperviseTypeDict) 
#         enterpriseType['orgPathName'] = orgInit['DftQuOrg']  #动态获取
#         enterpriseType['orgId'] = orgInit['DftQuOrgId']
#         enterpriseType['superviseType'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '其他一般单位'")
#         YinHuanDuGaiIntf.add_SaveSuperviseType(enterpriseType, username='admin', password='admin')
#         Log.LogOutput(LogLevel.INFO,'新增单位类型成功..')
# # 新增隐患类型
#         superviseType = copy.deepcopy(YinHuanDuGaiPara.saveSuperviseType) 
#         superviseType['superviseTypeItemVo.superviseItemMap'] = ':%s:%s'%(CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_item_id from supervise_item t where t.name ='安全出口疏散通道堵塞'"),CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '督改项等级') and p.displayname = '严重'"))
#         superviseType['superviseTypeItemVo.superviseItemMap'] = ':%s:%s'%(CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_item_id from supervise_item t where t.name ='安全出口疏散通道数量不足'"),CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '督改项等级') and p.displayname = '一般'"))
#         superviseType['superviseTypeItemVo.superviseItemMap'] = ':%s:%s'%(CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_item_id from supervise_item t where t.name ='明火灶具未集中使用'"),CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '督改项等级') and p.displayname = '轻微'"))
#         superviseType['superviseType'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%enterpriseType['orgPathName'] )
#         superviseType['orgId'] = superviseType['orgId']
#         YinHuanDuGaiIntf.add_Type(superviseType, username='admin', password='admin')
#         Log.LogOutput(LogLevel.INFO,'新增隐患类型成功..')
# 新增企业1    
        AddEnterprise1 = copy.deepcopy(YinHuanDuGaiPara.fireCompanyDict) 
        AddEnterprise1['mode'] = 'add'  
        AddEnterprise1['fireCompanyInfo.createDept'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from ORGANIZATIONS t where t.Orgname='%s'"%orgInit['DftWangGeOrg']) 
        AddEnterprise1['fireCompanyInfo.importOrAdd'] = '1'
        AddEnterprise1['fireCompanyInfo.orgPathName'] = '%s%s%s%s%s'%(orgInit['DftShiOrg'],orgInit['DftQuOrg'],orgInit['DftJieDaoOrg'],orgInit['DftSheQuOrg'],orgInit['DftWangGeOrg'])
        AddEnterprise1['fireCompanyInfo.companyName'] = '测试单位1%s'%CommonUtil.createRandomString()
        AddEnterprise1['fireCompanyInfo.orgid'] = AddEnterprise1['fireCompanyInfo.createDept']
        AddEnterprise1['companySuperviseTypeIsChange'] = 'true'
        AddEnterprise1['fireCompanyInfo.superviseTypeName'] = '其他一般单位'
        AddEnterprise1['fireCompanyInfo.superviseType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg'])
        AddEnterprise1['fireCompanyInfo.address'] = '测试地址'
        AddEnterprise1['fireCompanyInfo.manger'] = '测试姓名'
        AddEnterprise1['fireCompanyInfo.managerTelephone'] = '18710000000'
        AddEnterprise1['fireCompanyInfo.rentHousePerson'] = '0'
        AddEnterprise1['fireCompanyInfo.industrialCatalogue'] = CommonIntf.getDbQueryResult(dbCommand = "select t.code from fire_company_type t where t.name='电器'")  #行业类别
        AddEnterprise1['businessLicense'] = '1'
        AddEnterprise1['firelicense'] = '1'
        YinHuanDuGaiIntf.addOrEdit_fireCompany(AddEnterprise1, username=userInit['DftWangGeUser'], password='11111111')
        Log.LogOutput(LogLevel.INFO,'新增一般企业1成功..')
#新增企业2
        AddEnterprise2=copy.deepcopy(AddEnterprise1)
        AddEnterprise2['fireCompanyInfo.companyName']='测试单位2%s'%CommonUtil.createRandomString()
        YinHuanDuGaiIntf.addOrEdit_fireCompany(AddEnterprise2, username=userInit['DftWangGeUser'], password='11111111')
        Log.LogOutput(LogLevel.INFO,'新增一般企业2成功..')
# 街道新增隐患项未高危的巡检1
        AddInspect1 = copy.deepcopy(YinHuanDuGaiPara.saveFiretrapSuperviseDict) 
        AddInspect1['isReportFlag'] = 0 
        AddInspect1['calCheckResult'] = 'flag'
        checkNumberStr1=CommonIntf.getDbQueryResult(dbCommand ="select max(t.supervise_no) from  firetrap_supervise t")
        checkNumberInt1=string.atoi(checkNumberStr1[2:])+1
        AddInspect1['firetrapSupervise.superviseNo']='DG%ld'%checkNumberInt1
        AddInspect1['companyName'] = AddEnterprise1['fireCompanyInfo.companyName']
        AddInspect1['checkDate'] = Time.getCurrentDate()
        AddInspect1['firetrapSupervise.checkAddress'] = AddEnterprise1['fireCompanyInfo.address'] 
        AddInspect1['firetrapSupervise.checkPlace'] = AddEnterprise1['fireCompanyInfo.companyName']
        AddInspect1['checkItemIndexs'] = '1.'
        AddInspect1['checkItemCodes'] = '511#'
        AddInspect1['严重'] = 511
        AddInspect1['superviseLevleId_510'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '督改项等级') and p.displayname = '一般'")
        AddInspect1['superviseLevleId_512'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '督改项等级') and p.displayname = '轻微'")
        AddInspect1['superviseLevleId_511'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '督改项等级') and p.displayname = '严重'")
        AddInspect1['firetrapSupervise.reviseDate'] = Time.getCurrentDate()
        AddInspect1['firetrapSupervise.manageName'] = AddEnterprise1['fireCompanyInfo.manger']
        AddInspect1['companyCheckRecord_assignUserNameVo'] = '自动化街道用户'#userInit['DftJieDaoUserXM']
        AddInspect1['companyCheckRecord_assignUserVo'] = 'zdhjd@'#userInit['DftJieDaoUser']
        AddInspect1['companyCheckRecord_levelOrg'] = '乡镇（街道）'
        AddInspect1['user.userName'] = userInit['DftJieDaoUser']
        AddInspect1['user.name'] = userInit['DftJieDaoUserXM']
        AddInspect1['user.organization.id'] = orgInit['DftJieDaoOrgId']
        AddInspect1['calculationMode'] = 0
        AddInspect1['firetrapSupervise.signDate'] = Time.getCurrentDate()
        AddInspect1['firetrapSupervise.superviseUserName'] = userInit['DftJieDaoUserXM'] 
        AddInspect1['firetrapSupervise.superviseUser'] = userInit['DftJieDaoUser'] 
        AddInspect1['firetrapSupervise.superviseDate'] = Time.getCurrentDate()
        AddInspect1['operateMode'] = 'add'
        AddInspect1['firetrapSupervise.superviseState'] = 1
        AddInspect1['firetrapSupervise.updateDept'] = orgInit['DftJieDaoOrgId']
        AddInspect1['firetrapSupervise.createDept'] = orgInit['DftJieDaoOrgId']
        AddInspect1['superviseTypeId'] = 254
        AddInspect1['companyCheckRecord.companyManager'] = AddEnterprise1['fireCompanyInfo.manger']
        AddInspect1['companyCheckRecord.assignUser'] = userInit['DftJieDaoUser'] 
        AddInspect1['companyCheckRecord.assignDept'] = orgInit['DftJieDaoOrgId']
        AddInspect1['companyCheckRecord.checkType'] = 1
        AddInspect1['companyCheckRecord.checkUser'] = userInit['DftJieDaoUser'] 
        AddInspect1['companyCheckRecord.fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%AddEnterprise1['fireCompanyInfo.companyName']) #被检查单位的id
        AddInspect1['companyCheckRecord.checkDate'] = Time.getCurrentDate()
        AddInspect1['checkResult'] = '高危'
        YinHuanDuGaiIntf.saveFiretrapSupervise(AddInspect1, username=userInit['DftJieDaoUser'], password='11111111')
# 街道新增隐患项未高危的巡检2
        AddInspect2=copy.deepcopy(AddInspect1)
        AddInspect2['companyName'] = AddEnterprise2['fireCompanyInfo.companyName']
        checkNumberStr2=CommonIntf.getDbQueryResult(dbCommand ="select max(t.supervise_no) from  firetrap_supervise t")
        checkNumberInt2=string.atoi(checkNumberStr2[2:])+1
        AddInspect2['firetrapSupervise.superviseNo']='DG%ld'%checkNumberInt2
        AddInspect2['firetrapSupervise.checkAddress'] = AddEnterprise2['fireCompanyInfo.address'] 
        AddInspect2['firetrapSupervise.checkPlace'] = AddEnterprise2['fireCompanyInfo.companyName']
        AddInspect2['firetrapSupervise.checkPlace'] = AddEnterprise2['fireCompanyInfo.companyName']
        AddInspect2['companyCheckRecord.fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%AddEnterprise2['fireCompanyInfo.companyName'])
        YinHuanDuGaiIntf.saveFiretrapSupervise(AddInspect2, username=userInit['DftJieDaoUser'], password='11111111')
# 对高危隐患企业1进行抄告        
        AddChaoGao1=copy.deepcopy(ChaoGaoXinXiPara.AddChaoGao)
        AddChaoGao1['firetrapNotice.firetrapSuperviseId']=CommonIntf.getDbQueryResult(dbCommand ="select t.firetrap_supervise_id from firetrap_supervise t where t.check_place ='%s'"%AddInspect1['firetrapSupervise.checkPlace'] )
        AddChaoGao1['firetrapNotice.createDept']=orgInit['DftJieDaoOrgId']
        AddChaoGao1['firetrapNotice.updateDept']=orgInit['DftJieDaoOrgId']
        AddChaoGao1['companyCheckRecordId']=CommonIntf.getDbQueryResult(dbCommand ="select t.company_check_record_id from firetrap_supervise t where t.check_place='%s'"%AddInspect1['firetrapSupervise.checkAddress'])
        cgNumberStr1=CommonIntf.getDbQueryResult(dbCommand="select max(t.firetrap_notice_no) from firetrap_notice t")
        cgNumberInt1=string.atoi(cgNumberStr1[2:])+1
        AddChaoGao1['firetrapNotice.firetrapNoticeNo']='CG%ld'%cgNumberInt1
        AddChaoGao1['checkItems[0].code']=511#严重
        AddChaoGao1['checkItems[0].checkItemId']=CommonIntf.getDbQueryResult(dbCommand ="select p.check_item_id from check_item p where p.firetrap_supervise_id=(select t.firetrap_supervise_id from firetrap_supervise t where t.check_place ='%s')"%AddInspect1['firetrapSupervise.checkPlace'])
#对高危隐患企业2进行抄告
        ChaoGaoXinXiIntf.add_ChaoGao(ChaoGaoDict=AddChaoGao1,username=userInit['DftJieDaoUser'],password='11111111')  
        AddChaoGao2=copy.deepcopy(AddChaoGao1)
        AddChaoGao2['firetrapNotice.firetrapSuperviseId']=CommonIntf.getDbQueryResult(dbCommand ="select t.firetrap_supervise_id from firetrap_supervise t where t.check_place ='%s'"%AddInspect2['firetrapSupervise.checkPlace'] )
        AddChaoGao2['companyCheckRecordId']=CommonIntf.getDbQueryResult(dbCommand ="select t.company_check_record_id from firetrap_supervise t where t.check_place='%s'"%AddInspect2['firetrapSupervise.checkAddress'])
        cgNumberStr2=CommonIntf.getDbQueryResult(dbCommand="select max(t.firetrap_notice_no) from firetrap_notice t")
        cgNumberInt2=string.atoi(cgNumberStr2[2:])+1
        AddChaoGao2['firetrapNotice.firetrapNoticeNo']='CG%ld'%cgNumberInt2
        AddChaoGao2['checkItems[0].checkItemId']=CommonIntf.getDbQueryResult(dbCommand ="select p.check_item_id from check_item p where p.firetrap_supervise_id=(select t.firetrap_supervise_id from firetrap_supervise t where t.check_place ='%s')"%AddInspect2['firetrapSupervise.checkPlace'])
        ChaoGaoXinXiIntf.add_ChaoGao(ChaoGaoDict=AddChaoGao2,username=userInit['DftJieDaoUser'],password='11111111')
        Log.LogOutput(LogLevel.INFO,'对2家企业抄告成功..')
#站长审核界面查看信息
        CheckInZhanZhang1=copy.deepcopy(ChaoGaoXinXiPara.ChaoGao)
        CheckInZhanZhang1['firetrapNoticeNo']=AddChaoGao1['firetrapNotice.firetrapNoticeNo']
        responseDict=ChaoGaoXinXiIntf.check_ZhangZhanChaoGao(ZhangZhanChaoGaoDict=CheckInZhanZhang1,username=userInit['DftJieDaoUser'],password='11111111')
        print CheckInZhanZhang1['firetrapNoticeNo']
        self.assertTrue(responseDict,'站长查看抄告1失败')
        CheckInZhanZhang2=copy.deepcopy(ChaoGaoXinXiPara.ChaoGao)
        CheckInZhanZhang2['firetrapNoticeNo']=AddChaoGao2['firetrapNotice.firetrapNoticeNo']
        responseDict=ChaoGaoXinXiIntf.check_ZhangZhanChaoGao(ZhangZhanChaoGaoDict=CheckInZhanZhang2,username=userInit['DftJieDaoUser'],password='11111111')
        self.assertTrue(responseDict,'站长查看抄告2失败')
# 站长审核不通过抄告1
        ZhanZhangShenHeParam1=copy.deepcopy(ChaoGaoXinXiPara.ZhanZhangShenHe)
        ZhanZhangShenHeParam1['approveMode']='audit'
        str1=CommonIntf.getDbQueryResult(dbCommand ="select t.firetrap_supervise_id from firetrap_supervise t where t.check_place='%s'"%AddInspect1['firetrapSupervise.checkPlace'])
        str2=CommonIntf.getDbQueryResult(dbCommand ="select p.firetrap_notice_id from firetrap_notice p where p.firetrap_supervise_id='%s'"%str1)
        ZhanZhangShenHeParam1['firetrapNoticeApprove.approveId']=CommonIntf.getDbQueryResult(dbCommand ="select i.approve_id from firetrap_notice_approve i where i.firetrap_notice_id='%s'"%str2)
        ZhanZhangShenHeParam1['approve_firetrapSuperviseId']=AddChaoGao1['firetrapNotice.firetrapSuperviseId']
        ZhanZhangShenHeParam1['firetrapNoticeApprove.firetrapNoticeId']=str2
        ZhanZhangShenHeParam1['firetrapNoticeApprove.approveDate']=Time.getCurrentDate()
        ZhanZhangShenHeParam1['firetrapNoticeApprove.state']='96'
        ZhanZhangShenHeParam1['firetrapNoticeApprove.approveResult']='此条不予不通过'
        ChaoGaoXinXiIntf.audit_Approve(ZhanZhangShenHeParam1, username=userInit['DftJieDaoUser'], password='11111111')
        Log.LogOutput(LogLevel.INFO,'站长审批不通过..')
#站长审核通过抄告2
        ZhanZhangShenHeParam2=copy.deepcopy(ChaoGaoXinXiPara.ZhanZhangShenHe)
        ZhanZhangShenHeParam2['approveMode']='audit'
        str1_2=CommonIntf.getDbQueryResult(dbCommand ="select t.firetrap_supervise_id from firetrap_supervise t where t.check_place='%s'"%AddInspect2['firetrapSupervise.checkPlace'])
        str2_2=CommonIntf.getDbQueryResult(dbCommand ="select p.firetrap_notice_id from firetrap_notice p where p.firetrap_supervise_id='%s'"%str1_2)
        ZhanZhangShenHeParam2['firetrapNoticeApprove.approveId']=CommonIntf.getDbQueryResult(dbCommand ="select i.approve_id from firetrap_notice_approve i where i.firetrap_notice_id='%s'"%str2)
        ZhanZhangShenHeParam2['approve_firetrapSuperviseId']=AddChaoGao2['firetrapNotice.firetrapSuperviseId']
        ZhanZhangShenHeParam2['firetrapNoticeApprove.firetrapNoticeId']=str2_2
        ZhanZhangShenHeParam2['firetrapNoticeApprove.approveDate']=Time.getCurrentDate()
        ZhanZhangShenHeParam2['firetrapNoticeApprove.state']='97'
        ZhanZhangShenHeParam2['firetrapNoticeApprove.approveResult']='此条可以通过'
        ChaoGaoXinXiIntf.audit_Approve(ZhanZhangShenHeParam2, username=userInit['DftJieDaoUser'], password='11111111')
        Log.LogOutput(LogLevel.INFO,'站长审批通过..')
# 在领导审批界面查看抄告2信息
        checkLingDaoShenPi=copy.deepcopy(ChaoGaoXinXiPara.LingDaoShenPi)
        checkLingDaoShenPi['firetrapNoticeNo']=AddChaoGao2['firetrapNotice.firetrapNoticeNo']
   
        response=ChaoGaoXinXiIntf.check_LingDaoShenPi(LingDaoShenPiDict=checkLingDaoShenPi,username=userInit['DftJieDaoUser'],password='11111111')     
        self.assertTrue(response,'领导查看抄告失败')
        
        pass
    def testCase_002(self):
# 新增企业1    
        AddEnterprise1 = copy.deepcopy(YinHuanDuGaiPara.fireCompanyDict) 
        AddEnterprise1['mode'] = 'add'  
        AddEnterprise1['fireCompanyInfo.createDept'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from ORGANIZATIONS t where t.Orgname='%s'"%orgInit['DftWangGeOrg']) 
        AddEnterprise1['fireCompanyInfo.importOrAdd'] = '1'
        AddEnterprise1['fireCompanyInfo.orgPathName'] = '%s%s%s%s%s'%(orgInit['DftShiOrg'],orgInit['DftQuOrg'],orgInit['DftJieDaoOrg'],orgInit['DftSheQuOrg'],orgInit['DftWangGeOrg'])
        AddEnterprise1['fireCompanyInfo.companyName'] = '测试单位1%s'%CommonUtil.createRandomString()
        AddEnterprise1['fireCompanyInfo.orgid'] = AddEnterprise1['fireCompanyInfo.createDept']
        AddEnterprise1['companySuperviseTypeIsChange'] = 'true'
        AddEnterprise1['fireCompanyInfo.superviseTypeName'] = '其他一般单位'
        AddEnterprise1['fireCompanyInfo.superviseType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg'])
        AddEnterprise1['fireCompanyInfo.address'] = '测试地址'
        AddEnterprise1['fireCompanyInfo.manger'] = '测试姓名'
        AddEnterprise1['fireCompanyInfo.managerTelephone'] = '18710000000'
        AddEnterprise1['fireCompanyInfo.rentHousePerson'] = '0'
        AddEnterprise1['fireCompanyInfo.industrialCatalogue'] = CommonIntf.getDbQueryResult(dbCommand = "select t.code from fire_company_type t where t.name='电器'")  #行业类别
        AddEnterprise1['businessLicense'] = '1'
        AddEnterprise1['firelicense'] = '1'
        YinHuanDuGaiIntf.addOrEdit_fireCompany(AddEnterprise1, username=userInit['DftWangGeUser'], password='11111111')
        Log.LogOutput(LogLevel.INFO,'新增一般企业1成功..')
#新增企业2
        AddEnterprise2=copy.deepcopy(AddEnterprise1)
        AddEnterprise2['fireCompanyInfo.companyName']='测试单位2%s'%CommonUtil.createRandomString()
        YinHuanDuGaiIntf.addOrEdit_fireCompany(AddEnterprise2, username=userInit['DftWangGeUser'], password='11111111')
        Log.LogOutput(LogLevel.INFO,'新增一般企业2成功..')
# 街道新增隐患项未高危的巡检1
        AddInspect1 = copy.deepcopy(YinHuanDuGaiPara.saveFiretrapSuperviseDict) 
        AddInspect1['isReportFlag'] = 0 
        AddInspect1['calCheckResult'] = 'flag'
        checkNumberStr1=CommonIntf.getDbQueryResult(dbCommand ="select max(t.supervise_no) from  firetrap_supervise t")
        checkNumberInt1=string.atoi(checkNumberStr1[2:])+1
        AddInspect1['firetrapSupervise.superviseNo']='DG%ld'%checkNumberInt1
        AddInspect1['companyName'] = AddEnterprise1['fireCompanyInfo.companyName']
        AddInspect1['checkDate'] = Time.getCurrentDate()
        AddInspect1['firetrapSupervise.checkAddress'] = AddEnterprise1['fireCompanyInfo.address'] 
        AddInspect1['firetrapSupervise.checkPlace'] = AddEnterprise1['fireCompanyInfo.companyName']
        AddInspect1['checkItemIndexs'] = '1.'
        AddInspect1['checkItemCodes'] = '511#'
        AddInspect1['严重'] = 511
        AddInspect1['superviseLevleId_510'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '督改项等级') and p.displayname = '一般'")
        AddInspect1['superviseLevleId_512'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '督改项等级') and p.displayname = '轻微'")
        AddInspect1['superviseLevleId_511'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '督改项等级') and p.displayname = '严重'")
        AddInspect1['firetrapSupervise.reviseDate'] = Time.getCurrentDate()
        AddInspect1['firetrapSupervise.manageName'] = AddEnterprise1['fireCompanyInfo.manger']
        AddInspect1['companyCheckRecord_assignUserNameVo'] = '自动化街道用户'#userInit['DftJieDaoUserXM']
        AddInspect1['companyCheckRecord_assignUserVo'] = 'zdhjd@'#userInit['DftJieDaoUser']
        AddInspect1['companyCheckRecord_levelOrg'] = '乡镇（街道）'
        AddInspect1['user.userName'] = userInit['DftJieDaoUser']
        AddInspect1['user.name'] = userInit['DftJieDaoUserXM']
        AddInspect1['user.organization.id'] = orgInit['DftJieDaoOrgId']
        AddInspect1['calculationMode'] = 0
        AddInspect1['firetrapSupervise.signDate'] = Time.getCurrentDate()
        AddInspect1['firetrapSupervise.superviseUserName'] = userInit['DftJieDaoUserXM'] 
        AddInspect1['firetrapSupervise.superviseUser'] = userInit['DftJieDaoUser'] 
        AddInspect1['firetrapSupervise.superviseDate'] = Time.getCurrentDate()
        AddInspect1['operateMode'] = 'add'
        AddInspect1['firetrapSupervise.superviseState'] = 1
        AddInspect1['firetrapSupervise.updateDept'] = orgInit['DftJieDaoOrgId']
        AddInspect1['firetrapSupervise.createDept'] = orgInit['DftJieDaoOrgId']
        AddInspect1['superviseTypeId'] = 254
        AddInspect1['companyCheckRecord.companyManager'] = AddEnterprise1['fireCompanyInfo.manger']
        AddInspect1['companyCheckRecord.assignUser'] = userInit['DftJieDaoUser'] 
        AddInspect1['companyCheckRecord.assignDept'] = orgInit['DftJieDaoOrgId']
        AddInspect1['companyCheckRecord.checkType'] = 1
        AddInspect1['companyCheckRecord.checkUser'] = userInit['DftJieDaoUser'] 
        AddInspect1['companyCheckRecord.fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%AddEnterprise1['fireCompanyInfo.companyName']) #被检查单位的id
        AddInspect1['companyCheckRecord.checkDate'] = Time.getCurrentDate()
        AddInspect1['checkResult'] = '高危'
        YinHuanDuGaiIntf.saveFiretrapSupervise(AddInspect1, username=userInit['DftJieDaoUser'], password='11111111')
# 街道新增隐患项未高危的巡检2
        AddInspect2=copy.deepcopy(AddInspect1)
        AddInspect2['companyName'] = AddEnterprise2['fireCompanyInfo.companyName']
        checkNumberStr2=CommonIntf.getDbQueryResult(dbCommand ="select max(t.supervise_no) from  firetrap_supervise t")
        checkNumberInt2=string.atoi(checkNumberStr2[2:])+1
        AddInspect2['firetrapSupervise.superviseNo']='DG%ld'%checkNumberInt2
        print AddInspect2['firetrapSupervise.superviseNo']
        AddInspect2['firetrapSupervise.checkAddress'] = AddEnterprise2['fireCompanyInfo.address'] 
        AddInspect2['firetrapSupervise.checkPlace'] = AddEnterprise2['fireCompanyInfo.companyName']
        AddInspect2['firetrapSupervise.checkPlace'] = AddEnterprise2['fireCompanyInfo.companyName']
        AddInspect2['companyCheckRecord.fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%AddEnterprise2['fireCompanyInfo.companyName'])
        YinHuanDuGaiIntf.saveFiretrapSupervise(AddInspect2, username=userInit['DftJieDaoUser'], password='11111111')
# 对高危隐患企业1进行抄告        
        AddChaoGao1=copy.deepcopy(ChaoGaoXinXiPara.AddChaoGao)
        AddChaoGao1['firetrapNotice.firetrapSuperviseId']=CommonIntf.getDbQueryResult(dbCommand ="select t.firetrap_supervise_id from firetrap_supervise t where t.check_place ='%s'"%AddInspect1['firetrapSupervise.checkPlace'] )
        AddChaoGao1['firetrapNotice.createDept']=orgInit['DftJieDaoOrgId']
        AddChaoGao1['firetrapNotice.updateDept']=orgInit['DftJieDaoOrgId']
        AddChaoGao1['companyCheckRecordId']=CommonIntf.getDbQueryResult(dbCommand ="select t.company_check_record_id from firetrap_supervise t where t.check_place='%s'"%AddInspect1['firetrapSupervise.checkAddress'])
        cgNumberStr1=CommonIntf.getDbQueryResult(dbCommand="select max(t.firetrap_notice_no) from firetrap_notice t")
        cgNumberInt1=string.atoi(cgNumberStr1[2:])+1
        AddChaoGao1['firetrapNotice.firetrapNoticeNo']='CG%ld'%cgNumberInt1
        AddChaoGao1['checkItems[0].code']=511#严重
        AddChaoGao1['checkItems[0].checkItemId']=CommonIntf.getDbQueryResult(dbCommand ="select p.check_item_id from check_item p where p.firetrap_supervise_id=(select t.firetrap_supervise_id from firetrap_supervise t where t.check_place ='%s')"%AddInspect1['firetrapSupervise.checkPlace'])
#对高危隐患企业2进行抄告
        ChaoGaoXinXiIntf.add_ChaoGao(ChaoGaoDict=AddChaoGao1,username=userInit['DftJieDaoUser'],password='11111111')  
        AddChaoGao2=copy.deepcopy(AddChaoGao1)
        AddChaoGao2['firetrapNotice.firetrapSuperviseId']=CommonIntf.getDbQueryResult(dbCommand ="select t.firetrap_supervise_id from firetrap_supervise t where t.check_place ='%s'"%AddInspect2['firetrapSupervise.checkPlace'] )
        AddChaoGao2['companyCheckRecordId']=CommonIntf.getDbQueryResult(dbCommand ="select t.company_check_record_id from firetrap_supervise t where t.check_place='%s'"%AddInspect2['firetrapSupervise.checkAddress'])
        cgNumberStr2=CommonIntf.getDbQueryResult(dbCommand="select max(t.firetrap_notice_no) from firetrap_notice t")
        cgNumberInt2=string.atoi(cgNumberStr2[2:])+1
        AddChaoGao2['firetrapNotice.firetrapNoticeNo']='CG%ld'%cgNumberInt2
        AddChaoGao2['checkItems[0].checkItemId']=CommonIntf.getDbQueryResult(dbCommand ="select p.check_item_id from check_item p where p.firetrap_supervise_id=(select t.firetrap_supervise_id from firetrap_supervise t where t.check_place ='%s')"%AddInspect2['firetrapSupervise.checkPlace'])
        ChaoGaoXinXiIntf.add_ChaoGao(ChaoGaoDict=AddChaoGao2,username=userInit['DftJieDaoUser'],password='11111111')
        Log.LogOutput(LogLevel.INFO,'对2家企业抄告成功..')
#站长审核通过 2家企业       
        ZhanZhangShenHeParm1=copy.deepcopy(ChaoGaoXinXiPara.ZhanZhangShenHe)
        ZhanZhangShenHeParm1['approveMode']='audit'
        ZhanZhangShenHeParm1['firetrapNoticeApprove.state']='97'
        str1=CommonIntf.getDbQueryResult(dbCommand ="select t.firetrap_supervise_id from firetrap_supervise t where t.check_place='%s'"%AddInspect1['firetrapSupervise.checkPlace'])
        str2=CommonIntf.getDbQueryResult(dbCommand ="select p.firetrap_notice_id from firetrap_notice p where p.firetrap_supervise_id='%s'"%str1)
        ZhanZhangShenHeParm1['firetrapNoticeApprove.approveId']=CommonIntf.getDbQueryResult(dbCommand ="select i.approve_id from firetrap_notice_approve i where i.firetrap_notice_id='%s'"%str2)
        ZhanZhangShenHeParm1['approve_firetrapSuperviseId']=AddChaoGao1['firetrapNotice.firetrapSuperviseId']
        ZhanZhangShenHeParm1['firetrapNoticeApprove.approveDate']=Time.getCurrentDate()
        ZhanZhangShenHeParm1['firetrapNoticeApprove.state']='97'
        ZhanZhangShenHeParm1['firetrapNoticeApprove.approveResult']='通过or不通过'
        ChaoGaoXinXiIntf.audit_Approve(ZhanZhangShenHeParm1, username=userInit['DftJieDaoUser'], password='11111111')
        ZhanZhangShenHeParm2=copy.deepcopy(ChaoGaoXinXiPara.ZhanZhangShenHe)
        str1=CommonIntf.getDbQueryResult(dbCommand ="select t.firetrap_supervise_id from firetrap_supervise t where t.check_place='%s'"%AddInspect2['firetrapSupervise.checkPlace'])
        str2=CommonIntf.getDbQueryResult(dbCommand ="select p.firetrap_notice_id from firetrap_notice p where p.firetrap_supervise_id='%s'"%str1)
        ZhanZhangShenHeParm2['firetrapNoticeApprove.approveId']=CommonIntf.getDbQueryResult(dbCommand ="select i.approve_id from firetrap_notice_approve i where i.firetrap_notice_id='%s'"%str2)
        ZhanZhangShenHeParm2['approve_firetrapSuperviseId']=AddChaoGao2['firetrapNotice.firetrapSuperviseId']
        ChaoGaoXinXiIntf.audit_Approve(ZhanZhangShenHeParm2, username=userInit['DftJieDaoUser'], password='11111111')
        Log.LogOutput(LogLevel.INFO,'站长审批通过..')
# 领导审批抄告1通过
        LingDaoShenPiParam1=copy.deepcopy(ChaoGaoXinXiPara.ZhanZhangShenHe)
        LingDaoShenPiParam1['approveMode']='approve'
        LingDaoShenPiParam1['firetrapNoticeApprove.state']='98'
        str1=CommonIntf.getDbQueryResult(dbCommand ="select t.firetrap_supervise_id from firetrap_supervise t where t.check_place='%s'"%AddInspect1['firetrapSupervise.checkPlace'])
        str2=CommonIntf.getDbQueryResult(dbCommand ="select p.firetrap_notice_id from firetrap_notice p where p.firetrap_supervise_id='%s'"%str1)
        LingDaoShenPiParam1['firetrapNoticeApprove.approveId']=CommonIntf.getDbQueryResult(dbCommand ="select i.approve_id from firetrap_notice_approve i where i.firetrap_notice_id='%s'"%str2)
        LingDaoShenPiParam1['approve_firetrapSuperviseId']=AddChaoGao1['firetrapNotice.firetrapSuperviseId']
        LingDaoShenPiParam1['firetrapNoticeApprove.approveDate']=Time.getCurrentDate()
        LingDaoShenPiParam1['firetrapNoticeApprove.approveResult']='通过or不通过'       
        ChaoGaoXinXiIntf.audit_Approve(LingDaoShenPiParam1, username=userInit['DftJieDaoUser'], password='11111111')
        Log.LogOutput(LogLevel.INFO,'领导审批通过..')
        pass
    def testCase_003(self):
        
    
        # 新增单位类型类型
        enterpriseType = copy.deepcopy(YinHuanDuGaiPara.saveSuperviseTypeDict) 
        enterpriseType['orgPathName'] = orgInit['DftQuOrg']  #动态获取
        enterpriseType['orgId'] = orgInit['DftQuOrgId']
        enterpriseType['superviseType'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts p where p.displayname = '其他一般单位'")
        YinHuanDuGaiIntf.add_SaveSuperviseType(enterpriseType, username='admin', password='admin')
        Log.LogOutput(LogLevel.INFO,'新增单位类型成功..')
# 新增隐患类型
        superviseType = copy.deepcopy(YinHuanDuGaiPara.saveSuperviseType) 
        superviseType['superviseTypeItemVo.superviseItemMap'] = ':%s:%s'%(CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_item_id from supervise_item t where t.name ='安全出口疏散通道堵塞'"),CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '督改项等级') and p.displayname = '严重'"))
        superviseType['superviseTypeItemVo.superviseItemMap'] = ':%s:%s'%(CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_item_id from supervise_item t where t.name ='安全出口疏散通道数量不足'"),CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '督改项等级') and p.displayname = '一般'"))
        superviseType['superviseTypeItemVo.superviseItemMap'] = ':%s:%s'%(CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_item_id from supervise_item t where t.name ='明火灶具未集中使用'"),CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '督改项等级') and p.displayname = '轻微'"))
        superviseType['superviseType'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%enterpriseType['orgPathName'] )
        superviseType['orgId'] = superviseType['orgId']
        YinHuanDuGaiIntf.add_Type(superviseType, username='admin', password='admin')
        Log.LogOutput(LogLevel.INFO,'新增隐患类型成功..')
# 新增企业        
        AddEnterprise = copy.deepcopy(YinHuanDuGaiPara.fireCompanyDict) 
        AddEnterprise['mode'] = 'add'  
        AddEnterprise['fireCompanyInfo.createDept'] = CommonIntf.getDbQueryResult(dbCommand = "select t.id from ORGANIZATIONS t where t.Orgname='%s'"%orgInit['DftWangGeOrg']) 
        AddEnterprise['fireCompanyInfo.importOrAdd'] = '1'
        AddEnterprise['fireCompanyInfo.orgPathName'] = '%s%s%s%s%s'%(orgInit['DftShiOrg'],orgInit['DftQuOrg'],orgInit['DftJieDaoOrg'],orgInit['DftSheQuOrg'],orgInit['DftWangGeOrg'])
        AddEnterprise['fireCompanyInfo.companyName'] = '测试单位%s'%CommonUtil.createRandomString()
        AddEnterprise['fireCompanyInfo.orgid'] = AddEnterprise['fireCompanyInfo.createDept']
        AddEnterprise['companySuperviseTypeIsChange'] = 'true'
        AddEnterprise['fireCompanyInfo.superviseTypeName'] = '其他一般单位'
        AddEnterprise['fireCompanyInfo.superviseType.id'] = CommonIntf.getDbQueryResult(dbCommand = "select t.supervise_type_id from supervise_type t where t.supervise_type = (select q.id from propertydicts q where q.displayname = '其他一般单位')and t.org_id = (select p.id from organizations p where p.orgname='%s')"%orgInit['DftQuOrg'])
        AddEnterprise['fireCompanyInfo.address'] = '测试地址'
        AddEnterprise['fireCompanyInfo.manger'] = '测试姓名'
        AddEnterprise['fireCompanyInfo.managerTelephone'] = '18710000000'
        AddEnterprise['fireCompanyInfo.rentHousePerson'] = '0'
        AddEnterprise['fireCompanyInfo.industrialCatalogue'] = CommonIntf.getDbQueryResult(dbCommand = "select t.code from fire_company_type t where t.name='电器'")  #行业类别
        AddEnterprise['businessLicense'] = '1'
        AddEnterprise['firelicense'] = '1'
        YinHuanDuGaiIntf.addOrEdit_fireCompany(AddEnterprise, username=userInit['DftWangGeUser'], password='11111111')
        Log.LogOutput(LogLevel.INFO,'新增一般企业成功..')
# 街道新增隐患项未高危的巡检
        AddInspect = copy.deepcopy(YinHuanDuGaiPara.saveFiretrapSuperviseDict) 
        AddInspect['isReportFlag'] = 0 
        AddInspect['calCheckResult'] = 'flag'
        checkNumberStr1=CommonIntf.getDbQueryResult(dbCommand ="select max(t.supervise_no) from  firetrap_supervise t")
        checkNumberInt1=string.atoi(checkNumberStr1[2:])+1
        AddInspect['firetrapSupervise.superviseNo']='DG%ld'%checkNumberInt1
        AddInspect['companyName'] = AddEnterprise['fireCompanyInfo.companyName']
        AddInspect['checkDate'] = Time.getCurrentDate()
        AddInspect['firetrapSupervise.checkAddress'] = AddEnterprise['fireCompanyInfo.address'] 
        AddInspect['firetrapSupervise.checkPlace'] = AddEnterprise['fireCompanyInfo.companyName']
        AddInspect['checkItemIndexs'] = '1.'
        AddInspect['checkItemCodes'] = '511#'
        AddInspect['严重'] = 511
        AddInspect['superviseLevleId_510'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '督改项等级') and p.displayname = '一般'")
        AddInspect['superviseLevleId_512'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '督改项等级') and p.displayname = '轻微'")
        AddInspect['superviseLevleId_511'] = CommonIntf.getDbQueryResult(dbCommand = "select p.id from propertydicts  p where p.propertydomainid = (select p1.id from propertydomains p1 where p1.domainname = '督改项等级') and p.displayname = '严重'")
        AddInspect['firetrapSupervise.reviseDate'] = Time.getCurrentDate()
        AddInspect['firetrapSupervise.manageName'] = AddEnterprise['fireCompanyInfo.manger']
        AddInspect['companyCheckRecord_assignUserNameVo'] = '自动化街道用户'#userInit['DftJieDaoUserXM']
        AddInspect['companyCheckRecord_assignUserVo'] = 'zdhjd@'#userInit['DftJieDaoUser']
        AddInspect['companyCheckRecord_levelOrg'] = '乡镇（街道）'
        AddInspect['user.userName'] = userInit['DftJieDaoUser']
        AddInspect['user.name'] = userInit['DftJieDaoUserXM']
        AddInspect['user.organization.id'] = orgInit['DftJieDaoOrgId']
        AddInspect['calculationMode'] = 0
        AddInspect['firetrapSupervise.signDate'] = Time.getCurrentDate()
        AddInspect['firetrapSupervise.superviseUserName'] = userInit['DftJieDaoUserXM'] 
        AddInspect['firetrapSupervise.superviseUser'] = userInit['DftJieDaoUser'] 
        AddInspect['firetrapSupervise.superviseDate'] = Time.getCurrentDate()
        AddInspect['operateMode'] = 'add'
        AddInspect['firetrapSupervise.superviseState'] = 1
        AddInspect['firetrapSupervise.updateDept'] = orgInit['DftJieDaoOrgId']
        AddInspect['firetrapSupervise.createDept'] = orgInit['DftJieDaoOrgId']
        AddInspect['superviseTypeId'] = 245
        AddInspect['companyCheckRecord.companyManager'] = AddEnterprise['fireCompanyInfo.manger']
        AddInspect['companyCheckRecord.assignUser'] = userInit['DftJieDaoUser'] 
        AddInspect['companyCheckRecord.assignDept'] = orgInit['DftJieDaoOrgId']
        AddInspect['companyCheckRecord.checkType'] = 1
        AddInspect['companyCheckRecord.checkUser'] = userInit['DftJieDaoUser'] 
        AddInspect['companyCheckRecord.fireCompanyInfoId'] = CommonIntf.getDbQueryResult(dbCommand = "select t.fire_company_info_id from fire_company_info t where t.company_name ='%s'"%AddEnterprise['fireCompanyInfo.companyName']) #被检查单位的id
        AddInspect['companyCheckRecord.checkDate'] = Time.getCurrentDate()
        AddInspect['checkResult'] = '高危'
        YinHuanDuGaiIntf.saveFiretrapSupervise(AddInspect, username=userInit['DftJieDaoUser'], password='11111111')
#对高危企业进行执法
        ZhiFaParam=copy.deepcopy(ChaoGaoXinXiPara.ZhiFa)
        ZhiFaParam['lawEnforcementInfo.operateDate']=Time.getCurrentDate()
        ZhiFaParam['lawEnforcementInfo.teamLeader']='自动化街道用户'
        ZhiFaParam['companyCheckRecordId']=CommonIntf.getDbQueryResult(dbCommand ="select t.company_check_record_id from firetrap_supervise t where t.check_place='%s'"%AddInspect['firetrapSupervise.checkAddress'])
        ZhiFaParam['lawEnforcementInfo.firetrapSuperviseId']=CommonIntf.getDbQueryResult(dbCommand ="select t.firetrap_supervise_id from firetrap_supervise t where t.check_place ='%s'"%AddInspect['firetrapSupervise.checkPlace'] )
        ChaoGaoXinXiIntf.add_ZhiFa(ZhiFaParam,username=userInit['DftJieDaoUser'], password='11111111')
        Log.LogOutput(LogLevel.INFO,'对企业添加执法成功..')
#执法后去检查此条信息状态
        checkZhiFaParam=copy.deepcopy(ChaoGaoXinXiPara.CheckZhiFa)    
        checkZhiFaParam['superviseNo']=AddInspect['firetrapSupervise.superviseNo']
        checkZhiFaParam['operateMobileState']='已执法'
        response=ChaoGaoXinXiIntf.check_ZhiFa(checkZhiFaParam,username=userInit['DftJieDaoUser'], password='11111111') 
        self.assertTrue(response,'查看失败')  
        
        pass
    def tearDown(self):    
        pass

if __name__ == "__main__":
    suite = unittest.TestSuite()
#     suite.addTest(ChaoGaoXinXi("testCase_001"))
#     suite.addTest(ChaoGaoXinXi("testCase_002"))
#     suite.addTest(ChaoGaoXinXi("testCase_003"))    
    
    results = unittest.TextTestRunner().run(suite)
    pass