# -*- coding:UTF-8 -*-
'''
Created on 2016-4-13

@author: lhz
'''
from __future__ import unicode_literals
import unittest
from Interface.PingAnJianShe.SystemMgr import SystemMgrIntf
import copy
from Interface.PingAnTong.XiaoXi import  MbXiaoXiIntf, MbXiaoXiPara
from COMMON import CommonUtil, Time, Log
from Interface.PingAnJianShe.Common import CommonIntf
from CONFIG import InitDefaultPara
from msilib import sequence
from CONFIG.Define import LogLevel
class XiaoXi(unittest.TestCase):
    def setUp(self):
        SystemMgrIntf.initEnv()
        pass
    
    '''
    @功能：消息--新建平台消息
    @ lhz  2016-3-3
    ''' 
    def testMessage_01(self):
        '''消息---新建平台消息'''
        #新建平台消息   
        newMessage = copy.deepcopy(MbXiaoXiPara.newMessage)
        newMessage['userReceivers'] =  CommonIntf.getDbQueryResult(dbCommand="select t.id from Contacters t  where t.fromuserid in (select t1.id from users t1 where t1.organizationid = '%s')"%InitDefaultPara.orgInit['DftWangGeOrgId1'])
        #list = CommonIntf.getDbQueryResultList(dbCommand="select t.id from Contacters t  where t.fromuserid in (select t1.id from users t1 where t1.organizationid = '%s')"%InitDefaultPara.orgInit['DftWangGeOrgId1'])
        
        newMessage['mail_receiver'] = CommonIntf.getDbQueryResult(dbCommand="select t.name from Contacters t  where t.fromuserid in (select t1.id from users t1 where t1.organizationid = '%s')"%InitDefaultPara.orgInit['DftWangGeOrgId1']).decode('utf-8') 
        newMessage['platformMessage.title'] = '标题%s' % CommonUtil.createRandomString(6) 
        newMessage['platformMessage.content'] = '内容 %s' % CommonUtil.createRandomString(6)
  
        ret =MbXiaoXiIntf.newMessage(newMessage,username=InitDefaultPara.userInit['DftWangGeUser1'], password='11111111')
        self.assertTrue(ret, '发送消息成功')   
        Time.wait(1)

        #检查在发件箱列表是否存在
        checkMessage = copy.deepcopy(MbXiaoXiPara.checkSendMessage)
        checkMessage['title'] = newMessage['platformMessage.title']
        ret =MbXiaoXiIntf.check_sendMessage(checkMessage,username=InitDefaultPara.userInit['DftWangGeUser1'], password='11111111')
        self.assertTrue(ret, '没有查找到发件信息')   
        Time.wait(1)
    
    
        #检查收信人人是否收到消息
        checkMessage = copy.deepcopy(MbXiaoXiPara.checkSendMessage)
        checkMessage['title'] = newMessage['platformMessage.title']
        username = CommonIntf.getDbQueryResult(dbCommand="select t.username from users t  where t.name in('%s')" % newMessage['mail_receiver']).decode('utf-8')
        ret =MbXiaoXiIntf.check_ReceiveMessage(checkMessage,username=username, password='11111111')
        self.assertTrue(ret, '收信人没有收到消息')   
        Time.wait(1)
        
        #检查pc端检查收信人人是否收到消息
        checkMessage = copy.deepcopy(MbXiaoXiPara.checkSendMessage)
        checkMessage['title'] = newMessage['platformMessage.title']
#         username = CommonIntf.getDbQueryResult(dbCommand="select t.username from users t  where t.name in('%s')"%newMessage['mail_receiver'])
        ret =MbXiaoXiIntf.check_ReceiveMessage(checkMessage,username=username, password='11111111')
        self.assertTrue(ret, '收信人没有收到消息')   
        Time.wait(1)


    '''
    @功能：消息--验证收件箱是否正常
    @ lhz  2016-3-3
    '''         
#     def testMessage_02(self):
#         '''消息--验证收件箱'''
#         #新建平台消息   
#         newMessage = copy.deepcopy(MbXiaoXiPara.newMessage)
#         newMessage['userReceivers'] =  CommonIntf.getDbQueryResult(dbCommand="select t.id from Contacters t  where t.fromuserid in (select t1.id from users t1 where t1.organizationid = '%s')"%InitDefaultPara.orgInit['DftWangGeOrgId1'])
#         #list = CommonIntf.getDbQueryResultList(dbCommand="select t.id from Contacters t  where t.fromuserid in (select t1.id from users t1 where t1.organizationid = '%s')"%InitDefaultPara.orgInit['DftWangGeOrgId1'])
#          
#         newMessage['mail_receiver'] = CommonIntf.getDbQueryResult(dbCommand="select t.name from Contacters t  where t.fromuserid in (select t1.id from users t1 where t1.organizationid = '%s')"%InitDefaultPara.orgInit['DftWangGeOrgId1']) 
#         newMessage['platformMessage.title'] = '标题%s' % CommonUtil.createRandomString(6) 
#         newMessage['platformMessage.content'] = '内容 %s' % CommonUtil.createRandomString(6)
#    
#         ret =MbXiaoXiIntf.newMessage(newMessage,username=InitDefaultPara.userInit['DftWangGeUser1'], password='11111111')
#         self.assertTrue(ret, '发送消息成功')   
#         Time.wait(1)
#  
#         #检查在发件箱列表是否存在
#         checkMessage = copy.deepcopy(MbXiaoXiPara.checkSendMessage)
#         checkMessage['title'] = newMessage['platformMessage.title']
#         ret =MbXiaoXiIntf.check_sendMessage(checkMessage,username=InitDefaultPara.userInit['DftWangGeUser1'], password='11111111')
#         self.assertTrue(ret, '没有查找到发件信息')   
#         Time.wait(1)
#      
#      
#         #检查收信人人是否收到消息
#         checkMessage = copy.deepcopy(MbXiaoXiPara.checkSendMessage)
#         checkMessage['title'] = newMessage['platformMessage.title']
#         username = CommonIntf.getDbQueryResult(dbCommand="select t.username from users t  where t.name in('%s')"%newMessage['mail_receiver'])
#         ret =MbXiaoXiIntf.check_ReceiveMessage(checkMessage,username=username, password='11111111')
#         self.assertTrue(ret, '收信人没有收到消息')   
#         Time.wait(1)
#          
#         #检查pc端检查收信人人是否收到消息
#         checkMessage = copy.deepcopy(MbXiaoXiPara.checkSendMessage)
#         checkMessage['title'] = newMessage['platformMessage.title']
#         username = CommonIntf.getDbQueryResult(dbCommand="select t.username from users t  where t.name in('%s')"%newMessage['mail_receiver'])
#         ret =MbXiaoXiIntf.check_ReceiveMessage(checkMessage,username=username, password='11111111')
#         self.assertTrue(ret, '收信人没有收到消息')   
#         Time.wait(1)        
#          
#         #回复消息
#         replayMessage = copy.deepcopy(MbXiaoXiPara.replyMessage)  
#         replayMessage['platformMessage.replyMessageId'] = ''
#         replayMessage['platformMessage.title'] = '回复:标题%s' % CommonUtil.createRandomString(6)    
#         replayMessage['platformMessage.receiverNames'] = newMessage['mail_receiver'] 
#         replayMessage['platformMessage.receiverId'] = CommonIntf.getDbQueryResult(dbCommand="select t.id from users t  where t.name in('%s')"%newMessage['mail_receiver']) 
#         replayMessage['platformMessage.content'] = '内容%s' % CommonUtil.createRandomString(6)   
#         replayMessage['attachFile'] = 'C:/Users/lhz/Pictures/宝宝/IMG_1656_副本.jpg'   
#         username = CommonIntf.getDbQueryResult(dbCommand="select t.username from users t  where t.name in('%s')"%newMessage['mail_receiver'])                   
#         ret =MbXiaoXiIntf.replyMessage(replayMessage,username=username, password='11111111')
#         self.assertTrue(ret, '消息是否回复成功')   
#         Time.wait(1)        
#          
#         #删除
#         id = CommonIntf.getDbQueryResult(dbCommand="select  t.id from inboxplatformmessages t where t.title = '%s'"%newMessage['platformMessage.title'])
#         username = CommonIntf.getDbQueryResult(dbCommand="select t.username from users t  where t.name in('%s')"%newMessage['mail_receiver'])
#         ret =MbXiaoXiIntf.deleteMessage(692,username=username, password='11111111')
#         self.assertTrue(ret, '消息是否删除成功')   
#         Time.wait(1)
  
    def tearDown(self):
            pass
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(XiaoXi("testMessage_01"))
#     suite.addTest(XiaoXi("testMessage_02"))
    
    results = unittest.TextTestRunner().run(suite)
    pass
        