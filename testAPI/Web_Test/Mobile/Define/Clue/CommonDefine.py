# -*- coding:UTF-8 -*-
'''
Created on 2016-8-16
通用枚举变量
@author: N-254
'''
def enum(**enums):
    return type('Enum', (), enums)
#轮播类型
LunboType = enum(NOTICE=0,CLUE=1)
