# import json,unittest,copy,random,string
# from lib import HttpHandler
# from config import config
#
#
# class happy_api(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#
#         cls.http = HttpHandler()
#         cls.login_url = f"{config.Host}{config.login_url}"
#         cls.uid = cls.http.db_seleect(config.dbpre, sql=config.uid_sql, )
#         cls.login_data = dict(config.sign_IOS_data, **config.login_data)
#         cls.token = json.loads(cls.http.post(cls.login_url, data=cls.login_data))["data"]["token"]
#         cls.sign = cls.http.sign(token=cls.token, uid=cls.uid, uid_check=1)
#         cls.play_url = f"{config.Host}{config.play_url}"
#         cls.check_mchine_url = f"{config.Host}{config.check_machine_playing_url}"
#         cls.asset_url = f"{config.Host}{config.asset_url}"
#         cls.userinfo_url = f"{config.Host}{config.userinfo_url}"
#         cls.recharge_url = f"{config.Host}{config.recharge_url}"
#         cls.homepage_url = f"{config.Host}{config.homepage_url}"
#         cls.index_url = f"{config.Host}{config.index_url}"
#         cls.moments_creat_url = f"{config.Host}{config.moments_create_url}"
#
#
#
#     def setUp(self):
#         pass
#
#
#     def tearDown(self):
#         pass
#
#     def test_homepage(self):
#         '''获取首页信息'''
#         homepage_data = copy.deepcopy(config.sign_IOS_data)
#         homepage_data["sign"] = self.sign
#         homepage_data["uid"] = self.uid
#         resp = json.loads(self.http.post(self.homepage_url,data=homepage_data))
#         self.assertEqual(resp["msg"],"首页数据",msg="首页获取失败")
#         self.http.logOut("获取首页信息成功")
#         # print(json.dumps(resp,ensure_ascii=False,indent=4))
#
#     def test_index(self):
#         '''获取圈子列表'''
#         index_data = copy.deepcopy(config.sign_IOS_data)
#         index_data["sign"] = self.sign
#         index_data["page"] = 0
#         index_data["uid"] = self.uid
#         resp = json.loads(self.http.post(self.index_url,data=index_data))
#         self.assertEqual(resp["msg"],"成功",msg="获取圈子失败")
#         self.http.logOut("获取圈子列表成功")
#
#         print(json.dumps(resp, ensure_ascii=False, indent=4))
#
#     def test_momeents_creat(self):
#         '''新建动态'''
#         moments_creat_data = dict(config.sign_IOS_data,**config.moments_create_data)
#         moments_creat_data["sign"] = self.sign
#         moments_creat_data["uid"] = self.uid
#         moments_creat_data["content"] = config.moments_create_data["content"].format(self.http.newName())
#         resp = json.loads(self.http.post(self.moments_creat_url,data=moments_creat_data))
#         print(resp)
#
#
#     def test_userinfo(self):
#         '''查询用户信息'''
#         userinfo_data = copy.deepcopy(config.sign_IOS_data)
#         userinfo_data["uid"] = self.uid
#         userinfo_data["sign"] = self.sign
#         resp = json.loads(self.http.post(self.userinfo_url,data=userinfo_data))
#         self.assertEqual(resp["msg"],"成功",msg="查询用户信息失败")
#         self.http.logOut("查询用户信息成功")
#         # print(json.dumps(resp,ensure_ascii=False,indent=4))
#     #
#     def test_recharge(self):
#         '''查询套餐信息'''
#         recharge_data = copy.deepcopy(config.sign_IOS_data)
#         recharge_data["uid"] = self.uid
#         recharge_data["sign"] = self.sign
#         resp = json.loads(self.http.post(self.recharge_url,data=recharge_data))
#         self.assertEqual(resp["msg"],"成功",msg="查询失败")
#         print(self.http.logOut("查询套餐信息成功"))
#
#     #
#     def test_check_machine_playing(self):
#             '''检查机台'''
#         # for i in range(300):
#             check_machine_playing_data = copy.deepcopy(config.sign_IOS_data)
#             check_machine_playing_data["uid"] = self.uid
#             check_machine_playing_data["sign"] = self.sign
#             resp = json.loads(self.http.post(self.check_mchine_url,data=config.check_machine_playing_data))
#             self.assertEqual(resp["msg"],"机台可以游玩",msg="机台不可玩")
#             print(self.http.logOut("检测机台： 机台可以游玩"))
#     #
#     # def test_asset(self):
#     #         '''查询用户资产'''
#     #         asset_data = copy.deepcopy(config.sign_IOS_data)
#     #         asset_data["uid"] = self.uid
#     #         asset_data["sign"] = self.sign
#     #         resp = json.loads(self.http.post(self.asset_url,data=config.asset_data))
#     #         self.assertEqual(resp["msg"],"成功",msg="asset失败")
#     #         print(self.http.logOut("查询用户资产成功"))
#
#     # def test_play(self):
#     #         '''投币'''
#     #         config.play_data["uid"] = self.uid
#     #         resp = json.loads(self.http.post(self.play_url,data=config.play_data))
#     #         self.assertEqual(resp["msg"],"成功",msg="投币失败")
#     #         num = config.play_data["num"]
#     #         print(self.http.logOut(f"成功投入{num}币"))
#
# if __name__ == '__main__':
#     unittest.main()
#
