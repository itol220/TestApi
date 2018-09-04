# -*- coding:UTF-8 -*-
'''
Created on 2016-12-9

@author: chenhui
'''
from __future__ import unicode_literals
from CONFIG import InitDefaultPara
from Interface.YunWeiPingTai.YunWeiCommon.YunWeiCommonIntf import \
    getDbQueryResultYunWei

departmentNo=InitDefaultPara.clueOrgInit['DftQuOrgDepNo']
def enum(**enums):
    return type('Enum', (), enums)
#抽奖记录兑换状态
# ReceiveState=enum(WEILINGQU=0,YILINGQU=1)
#滚动公告检查参数
gunDongGongGaoJianCha={
                       'contentText':None,
                       'jumpId':None
                       }
#便民服务配置列表参数
convenienceServiceListPara={
                    'tqmobile':'true',
                    'mobileType':'ios',
                    'apiVersion':'3'
                }
#便民服务配置列表检查参数
convenienceServiceListCheckPara={
  'title':None,
  'linkUrl':None
  }

#电话分类列表参数
getMobileCategoryListPara={
'tqmobile':'true',
'departmentNo':departmentNo,
'page':1,
'rows':20
  }
#电话分类检查参数
checkMobileCategoryListPara={
'categoryName':None                             
                             }
#电话管理列表参数
getMobileListPara={
'tqmobile':'true',
'departmentNo':departmentNo,
'companyName':'',
'page':1,
'rows':20
  }
#电话管理列表检查参数
checkMobileListPara={
'companyName':None,
'remark':None,
'telePhone':None,
'id':None,
'seq':None                    
                }
orgOpenStateListForMobilePara={
'countyOrgId':getDbQueryResultYunWei(dbCommand = "select t.id from ORGANIZATIONS t where t.orgname='杭州市'"),
'tqmobile':'true'
                              }
checkOrgOpenStateListForMobilePara={
'departmentNo':None,
'openState':None#OrgOpenState.OPEN/CLOSE                                      
                                    }

#获取首页轮播图列表信息
getLunBoListForMobilePara={
'tqmobile':'true',
'mobileType':'ios',
'departmentNo':departmentNo
                           }

#轮播检查参数
checkLunBoListForMobilePara={
'description':None,
'id':None,
'title':None,
'state':None,
'jumpType':None,
                             }