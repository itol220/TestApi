# -*- coding:UTF-8 -*-
'''
Created on 2018年1月5日15:48:21

@author: slp
'''
# 待检查的留言内容
toCheckUserLeavedMessageDict = {
        "id": None,
        "createUser": None,
        "createDate": None,
        "updateUser": None,
        "updateDate": None,
        "sortField": None,
        "order": None,
        "tqmobile": None,
        "submitTime": None,
        "userName": None,
        "orgName": None,
        "orginternalCode": None,
        "content": None,
        "remark": None
    }


# 搜索留言的请求字典
searchUserLeavedMessageDict = {
                               'leaveMessageDO.userName':'',    
                               'leaveMessageDO.orgName':   '',
                               '_search':   'false',
                               'nd':    1515138218786,
                               'rows':    2000,
                               'page':    1,
                               'sidx' :   "submitTime",
                               'sord':    'desc'
                               }
