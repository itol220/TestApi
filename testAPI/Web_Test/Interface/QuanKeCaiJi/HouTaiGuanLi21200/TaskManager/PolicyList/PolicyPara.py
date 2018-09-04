# -*- coding:UTF-8 -*-
'''
Created on 2018年4月8日 13:51:17

@author: sunliuping
'''
# 策略
addPolicyDict = {
    "cname": "",
    "ename": "",
    "type": "java方法",
    "code": "",
    "description": ""
}

# 查询策略列表 ,ename为空时搜索全部，不为空时指定搜索
searchPolicyListDict = {
    "taskPloyDO.ename": "",
    "_search": "false",
    "nd": 1523511439424,
    "rows": 2000,
    "page": 1,
    "sidx": "id",
    "sord": "desc"
}

# 删除策略字典

deletePolicyDict = {
    "ids[]": []
}

# 更新
updatePolicyDict = {
    "oldEname":"",
    "id": "",
    "cname": "",
    "ename": "",
    "type": "java方法",
    "code": "",
    "description": ""
}

# 检查策略
toCheckPolicyInfoDict = {
    "cname": None,
    "ename": "",
    "type": None,  # "java方法"
    "code": None,
    "description": None
}
