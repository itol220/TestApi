# -*- coding:UTF-8 -*-
'''
Created on 2018年4月12日 16:46:48

@author: slp
'''
# 新增任务字典
addDict = {
    "name": None,
    "taskGroup": None,
    "taskPloyDO.id": None,
    "taskPloyDO.cname": None,
    "Data": "",
    "description": ""
}
# 查询列表 ,name为空时搜索全部，不为空时指定搜索
searchListDict = {
    "taskDO.name": "",
    "_search": "false",
    "nd": 1523511439424,
    "rows": 2000,
    "page": 1,
    "sidx": "id",
    "sord": "desc"
}

# 删除任务字典
deleteDict = {
    "ids[]": []
}

# 更新
updateDict = {
    "oldEname":"",
    "id": "",
    "cname": "",
    "ename": "",
    "type": "java方法",
    "code": "",
    "description": ""
}

# 检查策略
toCheckInfoDict = {
    "cname": None,
    "ename": "",
    "type": None,  # "java方法"
    "code": None,
    "description": None
}
