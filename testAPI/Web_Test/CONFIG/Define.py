# -*- coding: UTF-8 -*-
'''
Created on 2016-1-12

@author: N-254
'''
def enum(**enums):
    return type('Enum', (), enums)
#common
LogLevel = enum(INFO=0,DEBUG=1,ERROR=2,WARN=3)
#web define
BrowserType = enum(IE=0,FIREFOX=1,CHROME=2)
#mobile define
