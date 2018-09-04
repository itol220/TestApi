# -*- coding:UTF-8 -*-

def enum(**enums):
    return type('Enum', (), enums)
#消息开关
MessageSwtich = enum(ON=0,OFF=1)

#修改用户参数
updUserPara={
        'tqmobile':'true',
        'id':''
             }

#检查用户信息
checkUserInfoPara = {
                    "gender":None,
                    "streetOrgName":None,
                    "address":None,
                    "nickName":None,
                    "mobile":None,
                    "grade":None,
                    "certifiedType":None
                     }

#设置消息推送开关
updateMessageSwitchPara = {
                            "id":"",
                            "messageSwit":"", #可调用枚举变量MessageSwtich，ON表示开，OFF表示关
                            "tqmobile": "true",
                            }
#新增意见反馈
addUserFeedbackPara = {
                   "userFeedBack":{
                                   "advice":"",
                                   "mobile":""
                                   },
                   }
#获取意见反馈字典
getUserFeedbackPara = {
                       "userFeedBack": {
                                        "mobile":""
                                        }
                       }
#检查意见反馈
checkUserFeedbackPara = {
                         "advice":None,
                         "mobile":None,
                         "replyUser":None,
                         "id":None,
                         "replyContent":None,
                         }

#获取意见反馈详细信息
getFeedbackDetailPara = {
                            "id":"",
                            "tqmobile":"true",
                         }

#检查意见反馈详情信息
checkFeedbackDetailPara = {
                           "advice":None, #意见反馈内容
                           "mobile":None,
                           "replyContent":None, #回复信息
                           }

#检查等级介绍
checkGradeConfigPara = {
                        "grade":None,
                        "gradeIntroduce":None,
                        }