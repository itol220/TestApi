# -*- coding: UTF-8 -*-
'''
Created on 2017-12-21

@author: n-313
'''
import os

def get_current_workspace_root_path():
    
    path = os.getcwd()
    pathList = path.split( "\\" )
    pathList = pathList[0:len( pathList ) - 2]
    rootPath = ""
    
    for item in pathList:
        rootPath += item + "\\\\"
    return rootPath[0:len( rootPath ) - 2]
