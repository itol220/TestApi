# -*- coding:UTF-8 -*-
'''
Created on 2015-11-4

@author: N-254
'''
from Interface.XiaoFangXiTong.xiaoFangXiTongHttpCommon import xiaofangxitong_post
import json
from Interface.XiaoFangXiTong.ShiJianZhongXin import ShiJianZhongXinPara
from COMMON import CommonUtil, Log

# def get_shijian_list(postData = None, username = None, password = None,headers=None):
#     response = xiaofangxitong_post(url='/fire/issueController/getIssueList.action',postdata=postData,headers=headers,username=username, password=password)
#     dictObject = json.loads(response)
#     print dictObject['rows']
#     return dictObject['rows']

def check_shijian(shijianDict, username = None, password = None):
    response = xiaofangxitong_post(url='/fire/issueController/getIssueList.action',postdata=ShiJianZhongXinPara.GetShiJianListPara, username=username, password=password)
    responseDict = json.loads(response)
    listDict = responseDict['rows']
    if CommonUtil.findDictInDictlist(shijianDict,listDict) is True:
        Log.LogOutput(message = '查找事件成功')
        return True
    else:
        Log.LogOutput(message = "查找事件失败")
        return False
    