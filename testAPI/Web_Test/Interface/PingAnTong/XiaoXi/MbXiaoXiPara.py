# -*- coding:UTF-8 -*-
'''
Created on 2016-4-13

@author: lhz
'''
#新建平台消息
newMessage = {
            'userReceivers':'',
            'mail_receiver':'',
            'platformMessage.title':'',
            'platformMessage.content':'',
            'attachFile':'',
            'tqmobile':'true'   
              }

#查看发件箱列表
lookMessage = {
                'tqmobile':'true',
                'isDraft':'',
                'sord':'desc',
                'sidx':'id',
                'page':'1',
                'rows':'20'
               }
#检查 发件箱
checkSendMessage = {
                'title':''   
                    }
#查看收件箱列表
lookReceive = {
               'tqmobile':'true',
                'page':'1',
                'sord':'desc',
                'rows':'20',
                'sidx':'id'
               }
#查看pc端收件箱 
lookMessagePC = {
                 'mode':'view',
                 'platformMessage.id':'',
                 }

#回复
replyMessage = {
                'platformMessage.replyMessageId':'626',
                'platformMessage.title':'',
                'platformMessage.receiverNames':'', 
                'platformMessage.receiverId':'',
                'platformMessage.content':'',
                'attachFile':'',
                'tqmobile':'true'  
                }

#删除
deleteMessage = {
             'tqmobile':'true',
             'sord':'desc',
             'sidx':'id',
             'page':'1',
             'ids':'',
             'rows':'20'    
                 }
