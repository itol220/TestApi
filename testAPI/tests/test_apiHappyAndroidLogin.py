import json,unittest,copy
from lib import HttpHandler
from config import config

class Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.http = HttpHandler()
        cls.login_url = f"{config.Host}{config.login_url}"
        cls.sign = cls.http.sign(uid_check=0)




    def setUp(self):
        pass


    def tearDown(self):
        pass



    def test_login1(self):
        '''正确用户名/密码登陆'''
        login_data = dict(config.sign_IOS_data,**config.login_data)
        login_data["sign"] = self.sign
        resp = json.loads(self.http.post(self.login_url,data=login_data))
        # print(json.dumps(resp,ensure_ascii=False,indent=4),type(resp))
        self.assertEqual(resp["msg"],"登录成功",msg="登录失败")
        self.http.logOut("登录成功")

    # def test_login2(self):
    #     '''错误密码登陆'''
    #     login_data = copy.deepcopy(config.login_data)
    #     login_data["sign"] = self.sign
    #     login_data["cpn"] = "00000000000"
    #     print(login_data)
    #     # resp = json.loads(self.http.post(self.login_url,data=login_data))
        # print(resp)

if __name__ == '__main__':
    unittest.main()
