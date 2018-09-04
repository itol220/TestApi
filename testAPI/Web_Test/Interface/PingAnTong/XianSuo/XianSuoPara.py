# -*- coding:UTF-8 -*-
'''
Created on 2015-11-24

@author: N-133
'''

# 登录参数
DengLu={
        'tqmobile':'',
        'mobile':'',
        'password':'',
        'mobileType':'',
        }

# 新增线索
XinZeng={'information':{
                                'contentText':'',
                                'baiduX':'',
                                'baiduY':'',
                                'x':'',
                                'y':'',
                                'address':''},
                'tqmobile':'true'       
                }

# 查看线索新增
chakanxiansuo={
               'searchInfoVo.information.orgId':'139854',
               'searchInfoVo.information.infoType':'0',
               '_search':'false',
               'rows':'20',
               'page':'1',
               'sidx':'id',
               'sord':'desc',
               }

# 新增线索检查点
jianchaxiansuo={
                'contentText':None,
                'address':None,
                }

# 获取消息未读数量
xiaoxiweidu={
             'tqmobile':'',
             'userId':'',
             }

# 查看公告列表
gonggaoliebiao={
                'tqmobile':'',
                'departmentNo':'',
                'page':'',
                }

# 新增点赞
xinzengdianzan={
                'tqmobile':'',
                'informationId':'',
                'praiseUserId':'',
                }