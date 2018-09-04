# -*- coding:UTF-8 -*-
'''
Created on 2016-6-16

@author: N-66
'''
AddChaoGao={
            'firetrapNotice.firetrapNoticeId':'',
            'firetrapNotice.noticeType':'0',
            'firetrapNotice.parentId':'',
            'firetrapNotice.state':'95',
            'firetrapNotice.firetrapNoticeDept.firetrapNoticeDeptId':'',
            'firetrapNotice.firetrapSuperviseId':'',#2857
            'firetrapNotice.createDept':'',#410
            'firetrapNotice.updateDept':'',#410
            'mode':'add',
            'companyCheckRecordId':'',#3176
            'firetrapNotice.firetrapNoticeNo':'',#CG2016061600002
            'checkItems[0].code':'',#511
            'checkItems[0].checkItemId':'',#3198
            'firetrapNotice.contactor':'自动化街道用户',
            'firetrapNotice.contactTelephone':'',
            'sendeeVo':'自动化区用户',
            'firetrapNotice.firetrapNoticeDept.sendeeIds':'zdhq',
            'firetrapNotice.firetrapNoticeDept.deptNames':'测试自动化区',
            'firetrapNotice.firetrapNoticeDept.deptIds':'407',#407
            'firetrapNotice.sendDate':''
            }
ZhanZhangShenHe={
                 'approveMode':'',#audit
                 'firetrapNoticeApprove.approveId':'',#781
                 'firetrapNoticeApprove.firetrapNoticeId':'',#641
                 'approve_firetrapSuperviseId':'',#2857
                 'approve_superviseId':'',
                 'firetrapNoticeApprove.approveUser':'zdhjd@',
                 'firetrapNoticeApprove.approveDate':'',#2016-06-17
                 'firetrapNoticeApprove.state':'',#96表示审核不通过
                 'firetrapNoticeApprove.approveResult':'',#这有什么好抄告的呢
                 }
ZhiFa={
       'lawEnforcementInfo.operateDate':'',#时间
       'lawEnforcementInfo.teamLeader':'',#自动化街道用户
       'lawEnforcementInfo.attendDept':'',
       'lawEnforcementInfo.descitption':'',
       'companyCheckRecordId':'',#3345
       'lawEnforcementInfo.firetrapSuperviseId':'',#2983
       'lawEnforcementInfo.lawEnforcementInfoId':''
       }
CheckZhiFa={
            'superviseNo':'',
            'operateMobileState':''
            }



ChaoGao={
         'firetrapNoticeNo':None
         }
GetZhangZhanChaoGao={
                     'orgId':'410',
                     'stateIds':'95',
                     '_search':'false',
# nd:1467006843080
                    'rows':'100',
                    'page':'1',
                    'sidx':'id',
                    'sord':'desc'
                     }
LingDaoShenPi={
              'firetrapNoticeNo':None
              }
GetLingDaoShenPi={
                  'orgId':'',
                  'stateIds':'94',
                  '_search':'false',
# nd:1467012071187
                   'rows':'20',
                   'page':'1',
                   'sidx':'id',
                   'sord':'desc'
                  }
GetZhiFa={
          'orgId':'410',
          'state':'',
          'firetrapSupervise.noFiretrapReview':'',
          'firetrapSupervise.noReport':'',
          'firetrapSupervise.complete':'',
          'firetrapSupervise.toReview':'',
          'firetrapSupervise.fireCompanyInfo.companyName':'',
          'queryParameter.allStateSearch':'1',
          'queryParameter.orgId':'410',
          'queryParameter.publicString':'1',
          'queryParameter.reportState':'',
          '_search':'false',
# nd:1467078554586
            'rows':'100',
            'page':'1',
            'sidx':'id',
            'sord':'desc'
# _:1467078554588
          }
