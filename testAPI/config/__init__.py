import time

class config:
    # data_ZDHsq = {
    # 'password': '11111111',
    # 'userName':'zdhsq@',
    # 'tqmobile': 'true',
    # 'isNewLoginVersion':'true'
    # }
    # data_ZDHsq_error = {
    #     'password': '11111eee',
    #     'userName': 'zdhsq@',
    #     'tqmobile': 'true',
    #     'isNewLoginVersion':'true'
    # }
    # data_ZDHsq_none = {
    #     'password': '',
    #     'userName': '',
    #     'isNewLoginVersion':'true'
    # }
    #
    # data_HZsq = {
    # 'password': 'a11111111',
    # 'userName':'hzsq@husg',
    # 'tqmobile': 'true',
    # 'isNewLoginVersion':'true'
    # }
    # userInfo_ZDHsq = {
    # 'dealOrgId': 913,
    # 'operatorName':'自动化社区用户',
    # 'operatorMobile':13099999999,
    # 'tqmobile': 'true'
    # }
    # userInfo_HZsq = {
    # 'dealOrgId': 1039,
    # 'operatorName':'湖州虚拟社区',
    # 'operatorMobile':11111111111,
    # 'tqmobile': 'true'
    # }
    # errorInfo_login = ["{userName:'用户登录失败，密码错误！您已有1次登录失败，超过5次将被锁定',failureTimes:'1'}",
    #                    "{userName:'用户登录失败，密码错误！您已有2次登录失败，超过5次将被锁定',failureTimes:'2'}"
    #                    ]
    # contents = '月光如流水一般,静静地泻在这一片叶子和花上,薄薄的青雾浮起在荷塘里.叶子和花仿佛在牛乳中洗过一' \
    #            '样,又像笼着轻纱的梦.虽是满月,天上却有一层淡淡的云,所以不能朗照；但我以为这恰是到了好处'
    #
    #
    # SHouJiTest_Host = 'http://anhaooray.oicp.net:18065/'
    # SHouJiTest_Host1 = 'http://192.168.1.245:8065/'
    # SHouJiTest_HostWenZhou = 'http://192.168.1.107:8065/'
    # Host = SHouJiTest_Host
    # login_userInfo = userInfo_ZDHsq
    # login_data = data_ZDHsq
    #
    #
    # addIssue_param ={
    # 'issueNew.occurOrg.id': login_userInfo['dealOrgId'],
    # 'issueRelatedPeopleNames': '张小',
    # 'issueRelatedPeopleTelephones':'',
    # 'issueNew.selectedBigType': '民生服务-教育',
    # 'selectedBigType': 3,
    # 'selectedTypes': '34',
    # 'small_type': '34',
    # 'issueNew.important': 'false',
    # 'issueNew.relatePeopleCount': 1,
    # 'tqmobile': 'true',
    # 'android_appversion': '3.0.0.15'
    # }
    #
    # list_param = {
    # 'tqmobile':'true',
    # 'rows':20,
    # 'sord':'desc',
    # 'sidx':'issueId',
    # 'page':1,
    # 'orgId':login_userInfo['dealOrgId']
    # }
    #
    # updateIssue_param = {
    # 'issueNew.occurOrg.id': login_userInfo['dealOrgId'],
    #
    # 'issueRelatedPeopleNames': '张大小',
    # 'issueRelatedPeopleTelephones': '',
    # 'hours': '',
    # 'minute': '',
    # 'issueNew.selectedBigType': '民生服务-医疗卫生',
    # 'selectedBigType': 3,
    # 'selectedTypes': '35',
    # 'small_type': '35',
    # 'issueNew.important': 'false',
    # 'issueNew.isEmergency': 'false',
    # 'issueNew.relatePeopleCount': 1,
    # 'tqmobile': 'ture',
    # 'android_appversion': '3.0.0.15'
    # }
    #
    # viewIssue_param = {
    # 'tqmobile': 'true',
    # 'keyType': 'myIssue',
    # 'mode': 'doAction'
    # }
    vc = 53
    dbpre = "db_djkj_a"
    uid_sql = "select id from dj_account where mobile = 13255716570"
    Host = "http://testpre.hahaipi.com:8118/"
    login_url = "login/index.php/login/nopwd_login"
    play_url = "scfy/index.php/pay/play"
    check_machine_playing_url = "scfy/index.php/pay/check_machine_playing"
    asset_url = "scfy/index.php/userinfo/asset"
    userinfo_url = "scfy/index.php/userinfo"
    recharge_url = "scfy/index.php/come/recharge"
    homepage_url = "scfy/index.php/come/homepage"
    index_url = "scfy/index.php/moments/index"
    moments_create_url = "scfy/index.php/moments/create"

    timeline = int(time.time())
    sign_IOS_data = {
        "ai": "1001",
        "dt": 0,
        "os": 2,
        "timeline": timeline,
        "vc": vc
    }
    login_data = {
        "cpn":13255716570,
        "ct":20160317,
        "h":667,
        "imei":"",
        "imsi":"",
        "mcode":"V6f7hWOwSMWEv4bGXdN1ZZWEVh8BT/uxHuI6O3As1C9+ps5kRO08gl+WLATnWiyfpqo8CUttwKGEb1BAjKbNj"
                "IrxwklEa7WokoBp0TeDVG9hMKZM+80R3qhz66pU1PogEkL37OLOw/iGLKpmCRBkwu4du53JpU6K7yKLSgMkWCs=",
        "mm":"iPhone8,1",
        "nt":20,
        "osv":"10.3.3",
        "public_key":"MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCebBMbIukXo5hOSdHhNXUAbaI0Wo0goBrX1wsQqm4XK"
                     "XsPUyM/AoxEQ5j7HsMYKCDL+7TeEjG6jWzIjfPNXL5hDYSDsa3LoHzKPjAB4ZCs427GqQhP+i5qQ3IPhab4"
                     "t4dAI+xLdBxKp4LPtdr4U2cCRLwpHRKecjqWFijD3LYrJQIDAQAB",
        "sv":"as",
        "uuid":"81EB0261-C803-4D5C-82A9-411680C64BA6",
        "vn":"3.3.4.0727",
        "w":375
    }
    play_data = {
        "is_scfy":0,
        "mid":10,
        "num":1,
        "type":0,
        "uuid":"81EB0261-C803-4D5C-82A9-411680C64BA6"
    }
    check_machine_playing_data = {
        "is_scfy":0,
        "mid":10
    }

    moments_create_data = {
        "city":"杭州市",
        "content":	"#热气球西溪印象城#{}" ,
        "img":"C:\\photo\\008.jpg",
        "lat":30.275031,
        "location":"南都研发中心大楼",
        "lon":120.104490,
        "visible":1
    }


