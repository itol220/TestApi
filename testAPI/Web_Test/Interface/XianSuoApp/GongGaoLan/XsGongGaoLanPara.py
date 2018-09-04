# -*- coding:UTF-8 -*-
'''
Created on 2016-4-4

@author: chenhui
'''
from CONFIG import InitDefaultPara

departmentNo=InitDefaultPara.clueOrgInit['DftQuOrgDepNo']

GongGaoLieBiao={
        'searchInfoVo.information.orgId':'',
        'searchInfoVo.information.infoType':'1',
        '_search':'false',
        'rows':'200',
        'page':'1',
        'sidx':'id',
        'sord':'desc'
}

#手机端获取运维公告列表参数
shouJiYunWeiGongGaoLieBiao={
        'tqmobile':'true',
        'departmentNo':departmentNo,
        'page':1,
        'rows':200
                            }

#手机端运维公告列表参数检查参数
shouJiYunWeiGongGaoLieBiaoJianCha={
        'homePageShow':None,
        'contentText':None,
        'closeState':None,
        'title':None,
        'listContentText':None
                                   }