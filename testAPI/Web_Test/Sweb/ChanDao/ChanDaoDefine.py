# -*- coding: UTF-8 -*-
'''
Created on 2017-12-21

@author: n-313
'''
from CONFIG.Define import enum
FirstLevelMenu = enum(MYZONE='我的地盘',Product='产品',Project='项目',
                       Testing='测试',Document='文档',Statistics='统计')
SecondLevelMenu = enum(Requirement='需求',Dynamic='产品',Plan='计划',
                       Publish='发布')