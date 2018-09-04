# -*- coding:UTF-8 -*-
'''
Created on 2018年1月5日14:21:25

@author: slp
'''
from COMMON import Log, Util
from CONFIG.Define import LogLevel
import json
from Interface.QuanKeCaiJi.common import QuanKeCaiJiHttpCommon

'''
    @功能： 更新关于我们
    @para: 关于我们Dict
    username:用户名
    password:密码
    @return: 如果添加成功，则返回True；否则返回False  
'''    
def saveAboutUs( aboutUsDict, toCheckMessage = None , username = None, password = None ):
    Log.LogOutput( LogLevel.INFO, "保存关于我们的显示信息" )
    response = QuanKeCaiJiHttpCommon.quan_ke_cai_ji_21200_post( "/aboutus/updateAboutus",
                                                                aboutUsDict,
                                                                username = username,
                                                                password = password )
    if response.result is True:
        Log.LogOutput( LogLevel.INFO, "保存关于我们的显示信息成功" )
        
        # 有的时候，操作成功，响应中有些关键字段信息也要检查
        if toCheckMessage is not None:
            return Util.checkMessageInHttpResponse( response,
                                                    toCheckMessage )
        
        return json.loads( response.text )
    else:
        Log.LogOutput( LogLevel.ERROR, "保存关于我们的显示信息失败" )
        if toCheckMessage is  None:
            return False
        
        return Util.checkMessageInHttpResponse( response,
                                                toCheckMessage )


