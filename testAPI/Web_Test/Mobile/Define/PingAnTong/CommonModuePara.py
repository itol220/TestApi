# -*- coding:UTF-8 -*-
'''
Created on 2016-1-26

@author: N-254
'''
from CONFIG import InitDefaultPara, Global

def enum(**enums):
    return type('Enum', (), enums)

#模块名称
ModuleName = enum(SHIJIANCHULI=0, #事件处理
                  SHIYOURENKOU=1, #实有人口
                  ZHONGDIANRENYUAN=2, #重点人员
                  GUANHUAIDUIXIANG=3, #关怀对象
                  SHIYOUFANGWU=4, #实有房屋
                  ZHONGDIANCHANGSUO=5, #重点场所
                  LIANGXINZUZHI=6, #两新组织
                  QIYE=7, #企业
                  BIANQIANBEIWANG=8, #便签备忘
                  WODERENWU=9, #我的任务
                  XITONGSHEZHI=10, #系统设置
                  XITONGTUICHU=11, #系统退出
                  
                )

#弹出框处理选择
PopupProcessType = enum(NO=0, #取消
                        OK=1, #确认
                        ACCEPT=2, #受理
                        ACCEPTANDPROCESS=3, #受理并办理
                        CANCEL=4, #取消
                        )



loginDict = {
             'username' : InitDefaultPara.userInit['DftJieDaoUser'],
             'password' : Global.PingAnJianShePass,
             'shouShiMiMa' : False,
             'checkLoginResult' : True
             }
