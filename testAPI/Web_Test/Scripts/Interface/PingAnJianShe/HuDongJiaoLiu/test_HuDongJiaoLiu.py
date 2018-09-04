# -*- coding:UTF-8 -*-
'''
Created on 2016-5-4

@author: N-286
'''
from __future__ import unicode_literals
from COMMON import Log
from COMMON.CommonUtil import createRandomString
from CONFIG import Global
from CONFIG.InitDefaultPara import userInit, orgInit
from Interface.PingAnJianShe.Common.CommonIntf import getDbQueryResult
from Interface.PingAnJianShe.HuDongJiaoLiu.HuDongJiaoLiuIntf import sendMessage, \
    checkMessageInBox, delMessage, addMyGroup, updateMyContacter, fordwardMessage, \
    sendMessageAgain, addDraftBox, replyMessage, oneKeyRead, searchOutBoxMessage
from Interface.PingAnJianShe.HuDongJiaoLiu.HuDongJiaoLiuPara import FaXinXi, \
    LianXiRen, HuiFuXinXi, FajianxiangChaxun
from Interface.PingAnJianShe.ShiJianChuLi.ShiJianChuLiIntf import clearTable, \
    exeDbQuery
from Interface.PingAnJianShe.SystemMgr import SystemMgrIntf
import copy
import json
import unittest
class Hudongjiaoliu(unittest.TestCase):


    def setUp(self):
        SystemMgrIntf.initEnv()
#         clearTable(tableName='outboxplatformmessages')
#         clearTable(tableName='inboxplatformmessages')
#         clearTable(tableName='draftbox')#草稿箱
        if Global.simulationEnvironment is False:
            #删除测试自动化街道和测试自动化社区层级的草稿箱数据
            exeDbQuery(dbCommand="delete from draftbox i where i.receiverid in (select c.fromuserid from Contacters c where c.name='%s' or c.name='%s')"%(userInit['DftJieDaoUserXM'],userInit['DftSheQuUserXM']))
            #删除测试自动化街道和测试自动化社区层级的收件箱数据
            exeDbQuery(dbCommand="delete from inboxplatformmessages i where i.receiverid in (select c.fromuserid from Contacters c where c.name='%s' or c.name='%s')"%(userInit['DftJieDaoUserXM'],userInit['DftSheQuUserXM']))
            #删除测试自动化街道和测试自动化社区层级的发件箱数据
            exeDbQuery(dbCommand="delete from outboxplatformmessages o where o.senderid in (select c.fromuserid from Contacters c where c.name='%s'or c.name='%s')"%(userInit['DftJieDaoUserXM'],userInit['DftSheQuUserXM']))
            #删除自定义群组
            exeDbQuery(dbCommand="delete from contacters c where c.belongclass='myGroup' and c.name='自动化群组'" )
        pass
    
    def testHudongjiaoliu_001(self):
        '''验证发件箱发平台消息和删除功能'''
        para=copy.deepcopy(FaXinXi)
        para['userReceivers']=getDbQueryResult(dbCommand="select id from Contacters where name='%s'"%userInit['DftSheQuUserXM'])
        para['platformMessage.showName']=userInit['DftSheQuUserXM']
        result=sendMessage(para=para)
        self.assertTrue(result.result, '发消息失败')
        checkPara={'title':para['platformMessage.title']}
        #验证街道发件箱
        url1='/interactive/outboxPlatformMessageManage/findOutboxPlatformMessageByUserId.action'
        result1=checkMessageInBox(checkpara=checkPara,url=url1)
        self.assertTrue(result1,'发件箱验证失败')
        #验证社区收件箱
        url2='/interactive/inboxPlatformMessageManage/findInboxPlatformMessageByUserId.action'
        result2=checkMessageInBox(checkpara=checkPara,url=url2,username=userInit['DftSheQuUser'])
        self.assertTrue(result2,'收件箱验证失败')
        Log.LogOutput(message='发消息功能验证通过')
        #删除发件箱信息
        delPara3={
         'deleteIds': getDbQueryResult(dbCommand="select id from outboxplatformmessages where title='%s'"%para['platformMessage.title'])      
                 }
        url3='/interactive/outboxPlatformMessageManage/deletePlatformMessageById.action'
        rs3=delMessage(para=delPara3,url=url3)
        self.assertTrue(rs3.result, '删除失败')
        #验证发件箱删除功能
        result3=checkMessageInBox(checkpara=checkPara,url=url1)
        self.assertFalse(result3,'发件箱删除验证失败')
        Log.LogOutput( message='发件箱删除成功')

        #删除收件箱信息
        delPara4={
         'ids': getDbQueryResult(dbCommand="select id from inboxplatformmessages where title='%s'"%para['platformMessage.title'])      
                 }
        url4='/interactive/inboxPlatformMessageManage/deleteInboxPlatformMessageByIds.action'
        rs4=delMessage(para=delPara4,url=url4,username=userInit['DftSheQuUser'])
        self.assertTrue(rs4.result, '删除失败')
        #验证收件箱删除功能
        result4=checkMessageInBox(checkpara=checkPara,url=url2,username=userInit['DftSheQuUser'])
        self.assertFalse(result4,'收件箱删除验证失败')
        Log.LogOutput( message='收件箱删除成功')        
        pass

    def testHudongjiaoliu_002(self):
        '''验证发件箱-转发功能'''
        #新建我的群组
        addPara={'myGroup.name':'自动化群组'}
        result=addMyGroup(para=addPara)
        self.assertTrue(result.result, '新增我的群组失败')
        #新建我的联系人
        addPara2=copy.deepcopy(LianXiRen)
        addPara2['platformContactsOrgId']=orgInit['DftSheQuOrgId']
        addPara2['areaorgId']=orgInit['DftJieDaoOrgId']
        addPara2['myGroup.id']=json.loads(result.text)['id']
        addPara2['自动化社区用户']=getDbQueryResult(dbCommand="select id from Contacters where name='%s'"%userInit['DftSheQuUserXM'])
        addPara2['contacterIds']=getDbQueryResult(dbCommand="select id from Contacters where name='%s'"%userInit['DftSheQuUserXM'])
        result2=updateMyContacter(para=addPara2)
        self.assertTrue(result2.result, '编辑我的联系人失败')
        para=copy.deepcopy(FaXinXi)
        para['userReceivers']=getDbQueryResult(dbCommand="select id from Contacters where name='%s'"%userInit['DftSheQuUserXM'])
        para['platformMessage.showName']=userInit['DftSheQuUserXM']
        result=sendMessage(para=para)
        self.assertTrue(result.result, '发消息失败')
        para2=copy.deepcopy(FaXinXi)
        para2['userReceivers']=para['userReceivers']
        para2['platformMessage.showName']=addPara['myGroup.name']+"(群)"
        para2['platformMessage.title']='转发:'+para['platformMessage.title']
        para2['platformMessage.receiptState']=1
        result2=fordwardMessage(para=para2)
        self.assertTrue(result2.result, '转发失败')
        #验证转发功能
        checkPara={'title':para2['platformMessage.title']}
        #验证街道发件箱
        url3='/interactive/outboxPlatformMessageManage/findOutboxPlatformMessageByUserId.action'
        result3=checkMessageInBox(checkpara=checkPara,url=url3)
        self.assertTrue(result3,'发件箱验证失败')
        #验证社区收件箱
        url4='/interactive/inboxPlatformMessageManage/findInboxPlatformMessageByUserId.action'
        result4=checkMessageInBox(checkpara=checkPara,url=url4,username=userInit['DftSheQuUser'])
        self.assertTrue(result4,'收件箱验证失败')
        Log.LogOutput(message='发消息功能验证通过')
        pass
    
    def testHudongjiaoliu_003(self):
        '''验证发件箱-再次编辑功能'''
        para=copy.deepcopy(FaXinXi)
        para['userReceivers']=getDbQueryResult(dbCommand="select id from Contacters where name='%s'"%userInit['DftSheQuUserXM'])
        para['platformMessage.showName']=userInit['DftSheQuUserXM']
        result=sendMessage(para=para)
        self.assertTrue(result.result, '发消息失败')
        para2=copy.deepcopy(FaXinXi)
        orgLevelId=str(getDbQueryResult(dbCommand="select p.internalid from propertydicts p where p.displayname='村（社区）'"))
        para2['userReceivers']=str(orgInit['DftJieDaoOrgId'])+'_'+orgLevelId+'_0-levelList'
        para2['platformMessage.id']=getDbQueryResult(dbCommand="select id from outboxplatformmessages where title='%s'"%para['platformMessage.title'])
        para2['orgReceivers']=','+str(orgInit['DftJieDaoOrgId'])+'_'+orgLevelId+'_0'
        para2['platformMessage.showName']='测试自动化街道层级下的全部村社区已选择,自动化社区用户,'
        para2['platformMessage.receiverNames']='自动化社区用户'
        para2['platformMessage.title']=para['platformMessage.title']
        para2['platformMessage.receiptState']=None
        result2=sendMessageAgain(para=para2)
        self.assertTrue(result2.result, '再次编辑发送失败')
        #验证再次编辑发送功能
        checkPara={'title':para2['platformMessage.title']}
        #验证街道发件箱
        url3='/interactive/outboxPlatformMessageManage/findOutboxPlatformMessageByUserId.action'
        result3=checkMessageInBox(checkpara=checkPara,url=url3)
        self.assertTrue(result3,'发件箱验证失败')
        #验证社区收件箱
        url4='/interactive/inboxPlatformMessageManage/findInboxPlatformMessageByUserId.action'
        result4=checkMessageInBox(checkpara=checkPara,url=url4,username=userInit['DftSheQuUser'])
        self.assertTrue(result4,'收件箱验证失败')
        Log.LogOutput(message='发消息功能验证通过')        
        pass
    
    def testHudongjiaoliu_004(self):
        '''验证存草稿功能'''
        para=copy.deepcopy(FaXinXi)
        para['platformMessage.content']='测试内容'
        para['platformMessage.title']='测试标题%s'%createRandomString()
        result=addDraftBox(para=para)
        self.assertTrue(result.result, '发消息失败')   
        #验证保存到草稿箱功能
        checkPara={'title':para['platformMessage.title']}
        #验证街道发件箱不存在
        url1='/interactive/outboxPlatformMessageManage/findOutboxPlatformMessageByUserId.action'
        result1=checkMessageInBox(checkpara=checkPara,url=url1)
#        print result1
        self.assertFalse(result1,'保存到草稿箱-发件箱验证失败')
        #验证街道草稿箱存在
        url2='/interactive/draftBoxManage/findDraftBoxByUserId.action'
        result2=checkMessageInBox(checkpara=checkPara,url=url2)
        self.assertTrue(result2,'草稿箱验证失败')
        Log.LogOutput(message='保存到草稿箱功能验证通过')
        #草稿箱中发送消息
        para['draftBox.id']=getDbQueryResult(dbCommand="select id from draftbox where title='%s'"%para['platformMessage.title'])
        #查询出村、社区级的测试自动化岗位id
        orgLevel=getDbQueryResult(dbCommand="select o.orglevel from organizations o where o.id='%s'"%orgInit['DftSheQuOrgId'])
        roleId=getDbQueryResult("select * from roles a where a.id in (select r.roleid from role_level r where r.levelid='%s') and a.rolename='测试自动化岗位'"%orgLevel)
        para['userReceivers']=str(roleId)+'_'+str(orgInit['DftJieDaoOrgId'])+'_1-roleList'
        para['roleReceivers']=','+str(roleId)+'_'+str(orgInit['DftJieDaoOrgId'])+'_1'
        para['platformMessage.showName']='测试自动化街道下的全部测试自动化岗位已选择,'
        para['draftBox.receiptState']=0
        result=sendMessage(para=para)
        self.assertTrue(result.result, '发消息失败')
        #验证发送信息是否成功
        #发件箱存在
        result3=checkMessageInBox(checkpara=checkPara,url=url1)
        self.assertTrue(result3,'发件箱验证失败')
        #草稿箱存在
        result4=checkMessageInBox(checkpara=checkPara,url=url2)
        self.assertTrue(result4,'草稿箱验证失败')
        #社区收件箱存在
        url5='/interactive/inboxPlatformMessageManage/findInboxPlatformMessageByUserId.action'
        result5=checkMessageInBox(checkpara=checkPara,url=url5,username=userInit['DftSheQuUser'])
        self.assertTrue(result5,'社区收件箱验证失败')
        Log.LogOutput(message='草稿箱发消息功能验证通过')
        #删除草稿箱信息
        delPara={
         'deleteIds': getDbQueryResult(dbCommand="select id from draftbox where title='%s'"%para['platformMessage.title'])
                 }
        url6='/interactive/draftBoxManage/deleteDraftBoxById.action'
        result6=delMessage(para=delPara,url=url6)
        self.assertTrue(result6.result, '删除失败')
        #验证草稿箱删除功能
        result7=checkMessageInBox(checkpara=checkPara,url=url2)
        self.assertFalse(result7,'草稿箱删除验证失败')
        Log.LogOutput( message='草稿箱删除成功')                              
        pass 
    
    def testHudongjiaoliu_005(self):
        '''验证收件箱回复功能'''
        #街道发送一条消息给社区
        para=copy.deepcopy(FaXinXi)
        para['userReceivers']=getDbQueryResult(dbCommand="select id from Contacters where name='%s'"%userInit['DftSheQuUserXM'])
        para['platformMessage.showName']=userInit['DftSheQuUserXM']
        result=sendMessage(para=para)
        self.assertTrue(result.result, '发消息失败')
        #社区回复
        para2=copy.deepcopy(HuiFuXinXi)
        para2['platformMessage.replyMessageId']=getDbQueryResult(dbCommand="select id from inboxplatformmessages where title='%s'"%para['platformMessage.title'])
        para2['platformMessage.receiverId']=getDbQueryResult(dbCommand="select c.fromuserid from Contacters c where c.name='%s'"%userInit['DftJieDaoUserXM'])
        para2['platformMessage.receiverNames']=userInit['DftJieDaoUserXM']
        para2['platformMessage.title']='回复:'+para['platformMessage.title']
        para2['platformMessage.content']='回复内容'
        result2=replyMessage(para=para2,username=userInit['DftSheQuUser'])
        self.assertTrue(result2.result, '回复失败')
        #验证回复功能
        #验证社区发件箱
        checkPara={'title':para2['platformMessage.title']}        
        url3='/interactive/outboxPlatformMessageManage/findOutboxPlatformMessageByUserId.action'
        result3=checkMessageInBox(checkpara=checkPara,url=url3,username=userInit['DftSheQuUser'])
        self.assertTrue(result3,'发件箱验证失败')
        #验证街道收件箱
        url4='/interactive/inboxPlatformMessageManage/findInboxPlatformMessageByUserId.action'
        result4=checkMessageInBox(checkpara=checkPara,url=url4)
        self.assertTrue(result4,'收件箱验证失败')
        Log.LogOutput(message='回复息功能验证通过')
        pass
    
    def testHudongjiaoliu_006(self):
        '''验证收件箱一键阅读功能,有bug'''
        para=copy.deepcopy(FaXinXi)
        para['userReceivers']=getDbQueryResult(dbCommand="select id from Contacters where name='%s'"%userInit['DftSheQuUserXM'])
        para['platformMessage.showName']=userInit['DftSheQuUserXM']
        #街道给社区发送10条信息
        for i in range(0,10):
            para['platformMessage.title']='测试一键阅读功能'+createRandomString()+str(i+1)
            result=sendMessage(para=para)
            self.assertTrue(result.result, '发消息失败')
        #一键阅读前，收件箱拥有的指定标题格式的信息数
        count1=getDbQueryResult(dbCommand="select count(*) from inboxplatformmessages i where i.readstate=0 and i.title like '测试一键阅读功能%'")
        self.assertEqual(count1, 10, '一键阅读失败')      
        #社区一键阅读
        result1=oneKeyRead(username=userInit['DftSheQuUser'])
        self.assertTrue(result1.result, '一键阅读失败')
        #验证一键阅读功能
        #通过查询数据库中的inboxplatformmessages的readstate为1的数目来验证一键阅读功能
        count2=getDbQueryResult(dbCommand="select count(*) from inboxplatformmessages i where i.readstate=1 and i.title like '测试一键阅读功能%'")
        self.assertEqual(count2,10, '一键阅读失败')
        Log.LogOutput(message='一键阅读成功')
        #验证一键阅读后的回执，街道收件箱收到回执消息
        checkPara={
                   'title':'回执'
                   }
        url3='/interactive/inboxPlatformMessageManage/findInboxPlatformMessageByUserId.action'
        result3=checkMessageInBox(checkpara=checkPara,url=url3)
        #此处有bug
#         self.assertTrue(result3,'街道收件箱阅读回执功能验证失败')
#         Log.LogOutput(message='阅读回执功能验证通过')
                
        pass
    
    def testHudongjiaoliu_007(self):
        '''验证发件箱快速检索、高级搜索功能'''
        if Global.simulationEnvironment is True:
            Log.LogOutput(message='仿真环境跳过测试')
        else:
        #设置linux时间为2015-6-6
#         try:
#             Data='2015-6-6 '+getCurrentTime()
#             #注意''中的空格不可少
#             setLinuxTime(Data)
#             setLinuxTimeYunWei(Data=Data,password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
            para1=copy.deepcopy(FaXinXi)
            para1['platformMessage.title']='测试标题'+createRandomString()
            para1['userReceivers']=getDbQueryResult(dbCommand="select id from Contacters where name='%s'"%userInit['DftShiUserXM'])
            para1['platformMessage.showName']=userInit['DftShiUserXM']
            para1['platformMessage.content']='测试内容'+createRandomString()
            result1=sendMessage(para=para1)
            self.assertTrue(result1.result,'发送信息失败')
            #修改senddate字段
            exeDbQuery(dbCommand="update outboxplatformmessages  o set o.senddate =to_date('2015-06-06 18:18:18','yyyy-MM-dd HH24:mi:ss') where o.title='%s'"%para1['platformMessage.title'])
            #改回当前时间
    #             setLinuxTime(Data=getCurrentDateAndTime())
    #             setLinuxTimeYunWei(Data=getCurrentDateAndTime(),password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
            para2=copy.deepcopy(FaXinXi)
            para2['platformMessage.title']='测试标题'+createRandomString()
            para2['userReceivers']=getDbQueryResult(dbCommand="select id from Contacters where name='%s'"%userInit['DftSheQuUserXM'])
            para2['platformMessage.showName']=userInit['DftSheQuUserXM']
            para2['platformMessage.content']='测试内容'+createRandomString()
            result2=sendMessage(para=para2)
            self.assertTrue(result2.result,'发送信息失败')
            #按照标题快捷搜索
            checkPara1={'title':para1['platformMessage.title']}
            checkPara2={'title':para2['platformMessage.title']}
            searchPara1=copy.deepcopy(FajianxiangChaxun)
            searchPara1['searchPlatformMessageVo.fastSearchCondition']=para1['platformMessage.title']
            res1=searchOutBoxMessage(checkpara=checkPara1,searchpara=searchPara1)
            self.assertTrue(res1, '查询验证失败')
            res2=searchOutBoxMessage(checkpara=checkPara2,searchpara=searchPara1)
            self.assertFalse(res2, '查询验证失败')
            Log.LogOutput( message='根据标题快速检索通过')
            #按照内容快捷搜索
            searchPara1['searchPlatformMessageVo.fastSearchCondition']=para1['platformMessage.content']
            res1=searchOutBoxMessage(checkpara=checkPara1,searchpara=searchPara1)
            self.assertTrue(res1, '查询验证失败')
            res2=searchOutBoxMessage(checkpara=checkPara2,searchpara=searchPara1)
            self.assertFalse(res2, '查询验证失败')
            Log.LogOutput( message='根据内容快速检索通过')
            #按照标题高级搜索
            searchPara2=copy.deepcopy(FajianxiangChaxun)
            searchPara2['searchPlatformMessageVo.title']=para1['platformMessage.title']
            res1=searchOutBoxMessage(checkpara=checkPara1,searchpara=searchPara2)
            self.assertTrue(res1, '查询验证失败')
            res2=searchOutBoxMessage(checkpara=checkPara2,searchpara=searchPara2)
            self.assertFalse(res2, '查询验证失败')
            Log.LogOutput( message='根据标题高级检索通过')
            #按照内容高级搜索
            searchPara2['searchPlatformMessageVo.title']=''
            searchPara2['searchPlatformMessageVo.content']=para1['platformMessage.content']
            res1=searchOutBoxMessage(checkpara=checkPara1,searchpara=searchPara2)
            self.assertTrue(res1, '查询验证失败')
            res2=searchOutBoxMessage(checkpara=checkPara2,searchpara=searchPara2)
            self.assertFalse(res2, '查询验证失败')
            Log.LogOutput( message='根据内容高级检索通过')
            #按照发送时间高级搜索
            searchPara2['searchPlatformMessageVo.content']=''
            searchPara2['searchPlatformMessageVo.sendTimeStart']='2015-6-1'
            searchPara2['searchPlatformMessageVo.sendTimeEnd']='2015-6-8'
            res1=searchOutBoxMessage(checkpara=checkPara1,searchpara=searchPara2)
            self.assertTrue(res1, '查询验证失败')
            res2=searchOutBoxMessage(checkpara=checkPara2,searchpara=searchPara2)
            self.assertFalse(res2, '查询验证失败')
            Log.LogOutput( message='根据发送时间高级检索通过')
            #按照收件人高级搜索
            searchPara2['searchPlatformMessageVo.sendTimeStart']=''
            searchPara2['searchPlatformMessageVo.sendTimeEnd']=''            
            searchPara2['searchPlatformMessageVo.receiverNames']=userInit['DftShiUserXM']
            res1=searchOutBoxMessage(checkpara=checkPara1,searchpara=searchPara2)
            self.assertTrue(res1, '查询验证失败')
            res2=searchOutBoxMessage(checkpara=checkPara2,searchpara=searchPara2)
            self.assertFalse(res2, '查询验证失败')
            Log.LogOutput( message='根据收件人高级检索通过')            
            
#         finally:
#             #将服务器时间改回正确时间
#             setLinuxTime(Data=getCurrentDateAndTime())
#             setLinuxTimeYunWei(Data=getCurrentDateAndTime(),password=RenZhengZhongXinAppServRootPass,serverIp=RenZhengZhongXinUrl)
        pass
    def tearDown(self):    
        pass

if  __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    suite = unittest.TestSuite()
    suite.addTest(Hudongjiaoliu("testHudongjiaoliu_006"))
    results = unittest.TextTestRunner().run(suite)
    pass