# -*- coding:UTF-8 -*-
'''
Created on 2016-4-8

@author: N-286
'''
#用户管理列表参数
from __future__ import unicode_literals
from COMMON.CommonUtil import createRandomString

#获取用户管理列表
getClueUserManageListPara ={
                            'user.mobile':'',
                            'state':'', #0表示正常，1表示禁号
                            'rows':200,
                            'page':1,
                            'sidx':'id',
                            'sord':'desc'                   
                            }

#检查用户管理列表
checkClueUserManageListPara = {
                               'mobile':None    
                                }
#在线用户管理列表参数
zaiXianYongHuGuanLiLieBiao={
                    'session.userName':'',
                    'rows':200,
                    'page':1,
                    'sidx':'id',
                    'sord':'desc'                          
                            }

#在线用户检查
checkOnlineUserPara = {
                       'userName':None
                       }
