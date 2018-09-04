# -*- coding:UTF-8 -*-
#XsJiFenShangChengPara
'''
Created on 2016-6-14

@author: N-133
'''
from COMMON.CommonUtil import createRandomString
from CONFIG import Global, InitDefaultPara
from CONFIG.InitDefaultPara import orgInit


departmentNo=InitDefaultPara.clueOrgInit['DftQuOrgDepNo']
def enum(**enums):
    return type('Enum', (), enums)
#抽奖记录兑换状态
ReceiveState=enum(WEILINGQU=0,YILINGQU=1)

#积分兑换参数
JiFenDuiHuan={
            'tqmobile':'true',
            'userNickName':'',
            'userId':'',
            'userMobile':Global.XianSuoDftMobile,
            'goodsName':'',
            'goodsType':1,#0手机卡1实物
            'exchangePoints':'',
            'departmentNo':'',
            'orgName':'',
            'exchangeNum':'',
            'quota':'',#面额，手机卡时
            'operators':'',#运营商，手机卡时
            'goodsConfigurationId':'',
            'exchangeOverDate':'',
            'name':'',
            'IdentityCard':'',
            'goodsNo':'',
            'activityNo':'',          
              }

#查看兑换记录参数
DuiHuanJiLu={
            'tqmobile':'true',
            'userId':'',
            'mobileType':'ios',
            'page':1,
            'rows':100         
             }

#获取Banner图信息参数
BannerPicInfo={
            'tqmobile':'true',
            'mobileType':'ios',
            'departmentNo':departmentNo,
            'apiVersion':'',
                  }
#Banner图检查参数
BannerPicInfoCheck={
        'contentText':None,
        'title': None,
        'lotteryAllocationId':None,#大转盘配置id
        'jumpType':None,#跳转类型,0活动详情，1大转盘
           }
#获取大转盘活动配置参数
DaZhuanPanPeiZhi={
        'tqmobile':'true',
        'userId':'',
        'departmentNo':departmentNo,
        'lotteryAllocationId':'',
        'mobileType':'ios',        
                  }

#大转盘配置检查参数
DaZhuanPanPeiZhiCheck={
        'lotteryActivityNo':'',
        'activityDetails':'',
        'lotteryPoints':'',#每次抽奖话费积分
        'userLotteryDayNumber':''#每日抽奖次数上限          
                  }

#用户抽奖参数
ChouJiang={
       'tqmobile':'true',
       'lotteryActivityNo':''    
           }
#信息补充参数
ZhongJiangXinXiBuChong={
        'tqmobile':'true',
        'id':'',
        'name':'张三',
        'IdentityCard':111111111111111,
        'receiptUser':None,
        'receiptAdress':None,
        'receiptMobile':None,             
              }
#手机端中奖纪录列表
ZhongJiangJiLu={
        'tqmobile':'true',
        'userId':'',
        'departmentNo':departmentNo,
        'mobileType':'ios',
        'page':'1',
        'rows':'20',
        'receiveState':'',#0未领取,1已领取  为空时 显示全部   
                }
#手机端中奖纪录列表检查参数
ZhongJiangJiLuJianCha={
         'prizeGrade':None,              
         'exchangeState':None,
         'receiveState':None,#0未领取,1已领取
         'goodsType':None,
         'shippingMethod':None
                       }

#手机端商品列表参数
ShouJiShangPingLieBiao={
        'tqmobile':'true',
        'departmentNo':departmentNo,
        'mobileType':'ios',
        'page':'1',
        'rows':'100'
          }
#手机端商品列表检查参数
ShouJiShangPingLieBiaoJianCha={
        'departmentNo':None,
        'exchangePoints':None,#兑换需要积分
        'goodsDetails':None,
        'goodsName':None,
        'goodsNum':None,
        'goodsProfile':None,
        'goodsType' :None,
        'orgName':None,
        'state':0,
        'goodsNo':None              
                    }