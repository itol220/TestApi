# -*- coding:UTF-8 -*-
'''
Created on 2016-2-29

@author: N-286
'''
#纵向统计检查参数-层级
zongXiangFenXiJianCha={
                    'orgName':'',
                    'conflictNumber':0,
                    'otherNumber':0,
                    'securityNumber':0,
                    'serviceNumber':0,
                    'totalNumber':0                  
                       }
#纵向统计检查参数-账号
zongXiangFenXiJianCha2={
                    'orgName':None,
                    'createUser':None,
                    'conflictNumber':0,
                    'otherNumber':0,
                    'securityNumber':0,
                    'serviceNumber':0,
                    'totalNumber':0                  
                       }
#趋势参数
quShiJianCha={
       'onlyView':0,
       'statisticalDate':'',
       'statisticalTotal':0
       }

#类型分布参数
leiXingFenBuJianCha={
          'issueName':'',           
          'issueCounts':'',
          'percentage':None       
                     }


#总况-重点人员
zhongDianRenYuan={
                  "orgId":"",
                  "tableType":"",
                  "_search":"false",
                  "rows":"1000",
                  "page":"1",
                  "sidx":"id",
                  "sord":"desc"
                  }

checkZhongDianRenYuan={
                       "allCount":None,
                       "attentionCount":None,
                       "deathCount":None,
                       "logOutCount":None,
                       "statisticsType":None,
                       "thisMonthCount":None,
                       "todayAddCount":None,
                       }

zhongDianRenYuanGeYue={
                  "orgId":"",
                  "tableType":"",
                  }

serviceDict={
            "serviceType":"",
            "orgId":"",
            "queryDateType":"",
            "beginDate":"",
            "endDate":"",
            "businessType":"",
            "logoutType":"",
            "_search":"false",
            "rows":"1000",
            "page":"1",
            "sidx":"id",
            "sord":"desc"
            }

checkServiceDict={
                 "hasVisitedCount":None,
                 "noVisitCount":None,
                 "orgname":None,
                 "serviceObjectCount":None,
                 }

serviceMemberDict={
                "serviceType":"",
                "orgId":"",
                "year":"",
                "month":"",
                "businessType":"",
                "logoutType":"",
                "_search":"false",
                "rows":"1000",
                "page":"1",
                "sidx":"id",
                "sord":"desc"
                }

checkServiceMemberDict={
                     "businessCount":None,
                     "haveHelpCount":None,
                     "orgname":None,
                     "waitHelpCount":None,
                     }


zhongDianRenYuanZongKuang={
                          "orgId":"",
                          "year":"",
                          "month":"",
                          "type":""
                          }

checkzhongDianRenYuanZongKuang={
                                 "sum":None,
                                 "helped":None,
                                 "noHelp":None,
                                 "typeName":None,
                                 "name":None,
                                 "orgName":None,
                                 "amount":None,
                                 }


PersonnelDict={
                  "type":"",
                  "orgId":"",
                  "year":"",
                  "month":"",
                  "isemphasis":"0"
                  }

checkQuYu={
           "name":"",
           "Data":"",
           }



updateEmphasiseDict={
                      "dailogName":"",
                      "locationIds":"",
                      "location.isEmphasis":"",
                      "location.logOutTime":"",
                      "location.logOutReason":""
                      }



zhongDianChangSuoZongKuang={
                          "orgId":"",
                          "year":"",
                          "month":"",
                          "keyType":""
                          }

checkZhongDianChangSuo={
                        "helped":None,
                        "noHelp":None,
                        "organization":None,
                        "total":None,
                        }

checkStatAnalysePlace={
                       "Data":None,
                       "name":None,
                       }
delDict={
         'populationIds':''
         }