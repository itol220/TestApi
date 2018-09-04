# -*- coding:UTF-8 -*-
#注册
from __future__ import unicode_literals
from COMMON.CommonUtil import createRandomString
from CONFIG import InitDefaultPara, Global
from CONFIG.Global import XianSuoDftMobile

departmentNo=InitDefaultPara.clueOrgInit['DftQuOrgDepNo']
userAddPara={
        'tqmobile':'true',
        'mobile':'',
        'validateCode':'123456',
        'departmentNo':InitDefaultPara.clueOrgInit['DftJieDaoOrgDepNo'],
        'mobileKey':'',#手机识别码15位数字
        'mobileKeyEncrypt':'',
        'password':'',
        'inviteCode':''
           }

userUpdatePara={
                'tqmobile':'true',
                'id':'',
                'nickName':'',
                'gender':'',
                'address':'',
                'password':'',
                'mobileType':'android'
                }
addUserFeedBackPara={
        'tqmobile':'true',
        'userFeedBack':{
                        'mobile':XianSuoDftMobile,
                        'advice':'意见反馈'+createRandomString()},
            }
YaoQingMaXinZeng={
         'tqmobile':'true',
         'id':'',
         'inviteCode':''         
                  }
#爆料统计检查参数
checkBrokeStaticCountPara={
        'brokeStatisticsSwitc':None,                 
        'countyWeekComplete':None,
        'provinceWeekComplete':None,
        'todayAdd':None
                           }
#获取主题内容
getThemeContentListPara={
'tqmobile':'true',
'departmentNo':departmentNo,
'infoType':0#0:爆料信息,5:说说
                     }

#检查主题内容
themeContentListCheckPara={
'name':None,
'description':None,
'id':None,
'isHot':None#1否，0是
                     }
#网格员签到参数
wangGeYuanQianDaoPara = {
                        "pcUserId":"", #网格员账号id,默认使用自动化区账号id
                        "baiduX": "120.136681",
                        "baiduY": "30.279818",
                        "address": "中国浙江省杭州市西湖区学院路46号",
                        "userId":"", #线索手机账号id
                        "tqmobile": "true",
                        "y": "30.27577431223904",
                        "x": "120.12549021162512",
                        "mobile":Global.XianSuoDftMobile,
                         }

#获取网格员签到记录
getWangGeYuanSignInRecordsPara = {
                                    "page": "1",
                                    "userId":"",
                                    "tqmobile":"true",
                                    "rows":"10",
                                  }

#检查网格员签到记录
checkWangGeYuanSignInRecordPara = {
                                   "address":None,
                                   "pcUserId":None, #网格员用户id
                                   "mobile":None, #线索手机号
                                   "userId":None, #线索手机号id
                                   }

#找回密码参数
getBackPasswordPara = {
                        "validateCode":"123456",
                        "tqmobile":"true",
                        "password":"",
                        "mobile":"",
                       }