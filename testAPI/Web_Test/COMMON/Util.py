# -*- coding: UTF-8 -*-
'''
Created on 2018年4月8日 11:15:28

@author: sunliuping
'''
from Web_Test.COMMON import Log, CommonUtil
from Web_Test.CONFIG.Define import LogLevel
import json

'''
@author: Sunliuping
@attention: 从响应信息中查找待检查字段
'''
def checkMessageInHttpResponse( response, toCheckMessage ):
    return checkMessageExistsInAnotherMessage( response, toCheckMessage )

'''
@author: Sunliuping
@attention: 从一个字符串中查找另一个字符串
@return: bool
'''
def checkMessageExistsInAnotherMessage( sourceMessage, toCheckMessage ):
    if toCheckMessage in sourceMessage:
        Log.LogOutput( LogLevel.INFO, "在【%s】中查找【%s】成功！" % ( sourceMessage, toCheckMessage ) )
        return True
    else:
        Log.LogOutput( LogLevel.ERROR, "在【%s】中查找【%s】失败！" % ( sourceMessage, toCheckMessage ) )
        return False

'''
@see: 检查字典列表中是否有字典项
@since: 2018年4月8日 14:12:45
@author: sunliuping
'''
def checkExactDictInDictList( toCheckDict, dictList ):
    if CommonUtil.findDictInDictlist( toCheckDict, dictList ):
        Log.LogOutput( LogLevel.INFO, "在【%s】\n中查找\n【%s】\n成功！" % ( dictList, toCheckDict ) )
        return True
    else:
        Log.LogOutput( LogLevel.ERROR, "在【%s】\n中查找\n【%s】\n失败！" % ( dictList, toCheckDict ) )
        return False
    
'''
@see: 把对象转换成json字符串
@since: 2018年4月9日 08:34:56
@author: 孙留平
'''
def changePythonObjectToJsonString( sourceObject ):
    in_json = json.dumps( sourceObject, sort_keys = True, indent = 4, separators = ( ',', ': ' ), encoding = "gbk", ensure_ascii = True )
    return in_json

'''
@see: 把son字符串转换成对象
@since: 2018年4月9日 08:34:56
@author: 孙留平
'''
def changeJsonStringToPythonObject( sourceString ):
    return json.loads( sourceString )

'''
@see: 从Python对象中查找指定key
@since: 2018年4月9日 08:35:45
@author: 孙留平
'''
def getValueByKeyFromJson( key, sourceJson ):
    json_to_python = changeJsonStringToPythonObject( sourceJson )
    return json_to_python[key]
