

class config:
    data_ZDHsq = {
    'password': '',
    'userName':'zdh@',
    'tqmobile': 'true',
    'isNewLoginVersion':'true'
    }
    data_ZDHsq_error = {
        'password': '11111eee',
        'userName': 'zdhsq@eee',
        'tqmobile': 'true',
        'isNewLoginVersion':'true'
    }
    data_ZDHsq_none = {
        'password': '',
        'userName': '',
        'isNewLoginVersion':'true'
    }

    data_HZsq = {
    'password': '11111',
    'userName':'hzssg',
    'tqmobile': 'true',
    'isNewLoginVersion':'true'
    }
    userInfo_ZDHsq = {
    'dealOrgId': 913,
    'operatorName':'自动化社区用户',
    'operatorMobile':13099999999,
    'tqmobile': 'true'
    }
    userInfo_HZsq = {
    'dealOrgId': 1039,
    'operatorName':'湖州虚拟社区',
    'operatorMobile':11111111111,
    'tqmobile': 'true'
    }
    errorInfo_login = ["{userName:'用户登录失败，密码错误！您已有1次登录失败，超过5次将被锁定',failureTimes:'1'}",
                       "{userName:'用户登录失败，密码错误！您已有2次登录失败，超过5次将被锁定',failureTimes:'2'}"
                       ]
    contents = '月光如流水一般,静静地泻在这一片叶子和花上,薄薄的青雾浮起在荷塘里.叶子和花仿佛在牛乳中洗过一' \
               '样,又像笼着轻纱的梦.虽是满月,天上却有一层淡淡的云,所以不能朗照；但我以为这恰是到了好处'


    SHouJiTest_Host = 'http://anhaooray.oicp.net:18065/'
    SHouJiTest_Host1 = 'http://192.168.1.245:8065/'
    SHouJiTest_HostWenZhou = 'http://192.168.1.107:8065/'
    Host = SHouJiTest_Host
    login_userInfo = userInfo_ZDHsq
    login_data = data_ZDHsq


    addIssue_param ={
    'issueNew.occurOrg.id': login_userInfo['dealOrgId'],
    'issueRelatedPeopleNames': '张小',
    'issueRelatedPeopleTelephones':'',
    'issueNew.selectedBigType': '民生服务-教育',
    'selectedBigType': 3,
    'selectedTypes': '34',
    'small_type': '34',
    'issueNew.important': 'false',
    'issueNew.relatePeopleCount': 1,
    'tqmobile': 'true',
    'android_appversion': '3.0.0.15'
    }
    list_param = {
    'tqmobile':'true',
    'rows':20,
    'sord':'desc',
    'sidx':'issueId',
    'page':1,
    'orgId':login_userInfo['dealOrgId']
    }
    updateIssue_param = {
    'issueNew.occurOrg.id': login_userInfo['dealOrgId'],

    'issueRelatedPeopleNames': '张大小',
    'issueRelatedPeopleTelephones': '',
    'hours': '',
    'minute': '',
    'issueNew.selectedBigType': '民生服务-医疗卫生',
    'selectedBigType': 3,
    'selectedTypes': '35',
    'small_type': '35',
    'issueNew.important': 'false',
    'issueNew.isEmergency': 'false',
    'issueNew.relatePeopleCount': 1,
    'tqmobile': 'ture',
    'android_appversion': '3.0.0.15'
    }
