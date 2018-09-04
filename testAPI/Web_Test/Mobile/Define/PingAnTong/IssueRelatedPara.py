# -*- coding:UTF-8 -*-
'''
Created on 2017-9-30

@author: N-254
'''
def enum(**enums):
    return type('Enum', (), enums)

#事件处理状态，分为待受理、办理中、完成
IssueProcessState = enum(UNPROCESS=0,PROCESSING=2,PROCESSED=3)

#事件处理类型选择，分为交办，上报，办理中，结案，回退等类型
IssueProcessType = enum(JIAOBAN=0,SHANGBAO=1,BANLIZHONG=2,JIEAN=3,HUITUI=4,XIETONGBANLI=5,HUIFU=6)

#事件分类菜单，分为我的待办，我的已办，我的已办结，下辖待办，下辖已办结
IssueClassifyMenu = enum(WODEDAIBAN=0,WODEYIBAN=1,WODEYIBANJIE=2,XIAXIADAIBAN=3,XIAXIAYIBANJIE=4)
#事件对象
issueObject = {'subject':None, #标题
               'description':None, #简述
               'state':None, #事件状态，有受理、办理中、结案等，请传入上面定义的结构体 IssueProcessState
               'occueGrid':None, #发生网格，如果是当前层级，则默认不用选择；如果是下辖，则用'测试自动化社区-测试自动化网格'格式传入
               'address':None, #发生地点
               'type':None, #事件类型，使用大类加小类的方式传入，如A-B
               'peopleNo':None, #涉及人数
               'peopleInfo':None, #当事人信息，为一个字典，类型如{'姓名':'手机号'}
               'attachment':False, #事件各步骤是否添加附件，目前只支持通过相册添加图片，如需添加，传入True
               'needAccept':False, #是否需要受理动作,如果需要，则传入True
               'processType':None, #事件处理类型,请传入上面定义的事件处理类型结构体 IssueProcessType
               'processOpinion':None, #事件处理意见
               'jiaobanOrg':None, #交办部门
               'jiaobanUser':None, #交办用户
               'xiebanOrg':None, #协办部门
               'xiebanUser':None, #协办用户
               }