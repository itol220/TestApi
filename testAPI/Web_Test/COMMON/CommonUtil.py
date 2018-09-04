# -*- coding: UTF-8 -*-
'''
Created on 2015-11-5

@author: N-254
'''
from __future__ import unicode_literals
from Web_Test.CONFIG.Global import responseClass
from Web_Test.CONFIG.Define import LogLevel
import random
import xlrd,json,re
from Web_Test.COMMON import Log


'''
    @功能：     比较两个字典Dict1和Dict的键值
    @para: 
    Dict1: 待比较的字典 或者字典列表
    Dict: 待查找的字典
    @return: 如果DictList中的任何一个list包含Dict中所有不为None的键，且键值相同，则返回True；否则返回False   
'''
def findDictInDictlist(Dict,DictList):
    compareResult = False
    for dictItem in DictList:
        itemExist = 0
        for (d,x) in Dict.items():
            if x is None:
                continue
            keyValue = (d,x)
            if dictItem.items().count(keyValue) > 0:
                continue
            else:
                itemExist = -1
                break
        if itemExist == 0:
            compareResult = True
            break
        else:
            continue      
    return compareResult

'''
    @功能：     在某一字符串中匹配特定的字符串
    @para: 
    stringOrg: 原字符串
    stringReg: 待匹配的字符串
    @return: 如果匹配成功，则返回True；否则返回False   
'''

def regMatchString(stringOrg,stringReg):
    expected_regexp = re.compile(stringReg)
    match = expected_regexp.search(stringOrg)
    if match:
#         Log.LogOutput(level=LogLevel.DEBUG, message='字符串匹配成功')
        return True
    else:
#         Log.LogOutput(level=LogLevel.DEBUG, message='字符串匹配失败')
        return False

'''
    @功能：     对http报文的response进行解析，并返回一个类，包含解析后的结果、状态、及text属性
    @para: 
    httpResponse: http报文响应
    @return: 如果一个类的对象，类中有result、statusLine及text三个属性 
'''
def httpResponseResultDeal(httpResponse):
    responseObject = responseClass()
    responseObject.result = False
    if httpResponse is not None:
        responseObject.text = httpResponse.text
        responseObject.statusLine = httpResponse.status_code
        responseObject.content = httpResponse.content
        try:
            #当返回不为json时，该函数会抛出异常
#             httpResponse.json()
            responseDict = json.loads(httpResponse.text)
            #最新开发框架，有错误返回的格式为{'errorCode':'BE100-01','message':'获取失败','expLevel':'error'}
            if responseDict.has_key('errorCode'):
                if responseDict['errorCode']!="0":
                    responseObject.result = False
                    return responseObject
            #线索运维平台返回错误格式：{"errorMsg":"修改大转盘活动配置出错"}
            if responseDict.has_key('errorMsg'):
                responseObject.result = False
                return responseObject
            if responseDict.has_key('success'):
                if responseDict['success']=="false":
                    responseObject.result = False
                    return responseObject
            #线索返回判断
            if responseDict.has_key('response'):
                if responseDict['response'].has_key('success'):
                    if responseDict['response']['success']==False:
                        responseObject.result = False
                        return responseObject
            responseObject.result = True 
        except:          #非json异常
            if regMatchString(httpResponse.text,'true'):
                responseObject.result = True
            elif regMatchString(httpResponse.text,'null'):
                responseObject.result = True
#             elif isinstance(httpResponse.text, list) and len(httpResponse.text):
            elif regMatchString(httpResponse.text,'^\[.+\]$'):
                responseObject.result = True
                
            elif regMatchString(httpResponse.text,'''^[0-9]+$'''):
                responseObject.result = True
            elif regMatchString(httpResponse.text,'''^\"[0-9]+\"$'''):
                responseObject.result = True
            else:
                responseObject.result = False
    return responseObject

'''
    @功能：     生成一个随机字符串，默认6位
    @para: 
    length: 随机数位数，默认为6位
    @return: 返回一个包含大小写字母和数字的字符串
'''

def createRandomString(length=6):
    code_list = []
    for i in range(10): # 0-9数字
        code_list.append(str(i))
    for i in range(65, 91): # A-Z
        code_list.append(chr(i))
    for i in range(97, 123): # a-z
        code_list.append(chr(i))
    myslice = random.sample(code_list, length)  # 从list中随机获取6个元素，作为一个片断返回
    random_string = ''.join(myslice) # list to string
    return random_string

'''
    @功能：     检查excel单元格内容
    @para: 
    expectValue: 预期单元格内容
    fileName:excel文件名称，只需写文件名即可，默认路径为c:/autotest_file
    sheetName:单元格所在的sheet名
    cellName:单元格标记，用"A1" "B3"形式表示,字母大小写不敏感
    @return: 单元格内容正则匹配,匹配成功返回True,匹配失败，返回False
'''

def checkExcelCellValue(expectValue,fileName, sheetName,cellName):
    columnNum = ord(cellName[0:1].upper())-65
    rowNum = int(cellName[1:])-1
    newFileName = "c:/autotest_file/%s" % fileName
    try:
        data = xlrd.open_workbook(newFileName)
    except Exception as e:
        Log.LogOutput(LogLevel.ERROR, "打开文件失败")
        Log.LogOutput(LogLevel.ERROR, e)
        return False
    cellExactValueOrg = data.sheet_by_name(sheetName).cell(rowNum,columnNum).value
    cellExactValue = "%s" % cellExactValueOrg
    strExact = cellExactValue
#     strExact = cellExactValue.encode("utf-8")
    expected_regexp = re.compile(expectValue)
    match = expected_regexp.search(strExact)
    if match:
        Log.LogOutput(LogLevel.INFO, "单元格内容匹配成功")
        return True
    else:
        Log.LogOutput(LogLevel.DEBUG, "单元格内容匹配失败")
        return False