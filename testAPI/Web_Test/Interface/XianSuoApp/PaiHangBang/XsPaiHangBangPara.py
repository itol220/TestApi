# -*- coding:UTF-8 -*-
#XsJiFenShangChengPara
'''
Created on 2016-6-14

@author: N-133
'''
from CONFIG import InitDefaultPara
from CONFIG.InitDefaultPara import clueOrgInit


departmentNo=InitDefaultPara.clueOrgInit['DftQuOrgDepNo']
def enum(**enums):
    return type('Enum', (), enums)
#获取个人积分列表参数
getPersonalPointListPara={
               "tqmobile":"true",
               "departmentNo":departmentNo,
               "page":"1",
                "rows":"100"
               }
#检查个人积分参数
checkPersonalPointListPara={
             "userId":None,
             "sumPoints":None,
             "departmentNo":None,
             "id":None}
#获取区县积分排行列表参数
getPointsInCountyListPara={
                "tqmobile":"true",
                "departmentNo":departmentNo,
                "page":1,
                "rows":"100"} 