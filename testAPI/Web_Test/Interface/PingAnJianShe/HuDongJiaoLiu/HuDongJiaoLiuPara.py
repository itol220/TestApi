# -*- coding:UTF-8 -*-
'''
Created on 2016-5-4

@author: N-286
'''
from __future__ import unicode_literals
from Web_Test.COMMON.CommonUtil import createRandomString

#平台消息-发信息
FaXinXi={
        'platformMessage.messageType':'0',
        'platformMessage.sendType':'0',
        'userReceivers':'',
        'orgReceivers':'',
        'roleReceivers':'',
        'platformMessage.showName':'',
        'platformMessage.title':'测试标题'+createRandomString(),
        'platformMessage.content':'',
        'platformMessage.receiptState':'1'#是否有回执，0无，1有
         }

#通讯录-我的联系人
LianXiRen={
        'platformContactsOrgId':'',#社区
        'otherContactsOrgId':'',
        'areaorgId':'',#街道
        'orgReceivers':'',
        'mode':'edit',
        'myGroup.id':'',
        '自动化社区用户':'',
        'contacterIds':''
           }

#回复
HuiFuXinXi={
        'platformMessage.replyMessageId':'',
        'platformMessage.receiverId':'',
        'platformMessage.receiverNames':'',
        'platformMessage.title':'',
        'platformMessage.content':'',
        'platformMessage.receiptState':'0'          
            }
#查询参数
FajianxiangChaxun={
        'page':'1',
        'rows':'20',
        'sidx':'id',
        'sord':'desc',
        'searchPlatformMessageVo.title':'',
        'searchPlatformMessageVo.content':'',
        'searchPlatformMessageVo.sendTimeStart':'',
        'searchPlatformMessageVo.sendTimeEnd':'',
        'searchPlatformMessageVo.receiverNames':'',
        'searchPlatformMessageVo.hasAttach':'',
        'searchPlatformMessageVo.fastSearchCondition':''        
                   }
#新增其他联系人
addOtherContactPara={
        'mode':'add',
        'myContacter.id':'',
        'myContacter.belongClass':'myContact',
        'myContacter.name':'张三'+createRandomString(),
        'myContacter.mobileNumber':13333333333,
        'myContacter.fixedTelephone':'',
        'myContacter.myGroup.id':'',
        'myContacter.unit':'',
        'myContacter.office':'',
        'myContacter.remark':'',  
                     }
#获取联系人列表参数
getOtherContactListPara={
        '_search':'false',
        'rows':20,
        'page':1,
        'sidx':'id',
        'sord':'desc',                     
                         }
#联其他系人检查参数
checkOtherContactPara={
         'mobileNumber':None,
         'name':None              
                       }