# import json,unittest
# from lib import HttpHandler
#
#
# data1_1 = {
#
# }
# dataBack1_1 = {
#
# }
# data1_2 = {
#
# }
# dataBack1_2 = {
#
# }
# data1_3 = {
#
# }
# dataBack1_3 = {
#
# }
# data1_4 = {
#
# }
# dataBack1_4 = {
#
# }
# data1_5 = {
#
# }
# dataBack1_5 = {
#
# }
#
# data2_1 = {
#
# }
# dataBack2_1 = {
#
# }
# data2_2 = {
#
# }
# dataBack2_2 = {
#
# }
# data2_3 = {
#
# }
# dataBack2_3 = {
#
# }
# data2_4 = {
#
# }
# dataBack2_4 = {
#
# }
# data2_5 = {
#
# }
# dataBack2_5 = {
#
# }
#
#
# data3_1 = {
#
# }
# dataBack3_1 = {
#
# }
# data3_2 = {
#
# }
# dataBack3_2 = {
#
# }
# data3_3 = {
#
# }
# dataBack3_3 = {
#
# }
# data3_4 = {
#
# }
# dataBack3_4 = {
#
# }
# data3_5 = {
#
# }
# dataBack3_5 = {
#
# }
#
#
# data4_1 = {
#
# }
# dataBack4_1 = {
#
# }
# data4_2 = {
#
# }
# dataBack4_2 = {
#
# }
# data4_3 = {
#
# }
# dataBack4_3 = {
#
# }
# data4_4 = {
#
# }
# dataBack4_4 = {
#
# }
# data4_5 = {
#
# }
# dataBack4_5 = {
#
# }
#
#
# data5_1 = {
#
# }
# dataBack5_1 = {
#
# }
# data5_2 = {
#
# }
# dataBack5_2 = {
#
# }
# data5_3 = {
#
# }
# dataBack5_3 = {
#
# }
# data5_4 = {
#
# }
# dataBack5_4 = {
#
# }
# data5_5 = {
#
# }
# dataBack5_5 = {
#
# }
#
#
# class HappyWTM_BaseApi(unittest.TestCase):
#     '''天猫基础接口'''
#
#     @classmethod
#     def setUpClass(cls):
#         cls.http = HttpHandler()
#         cls.url1 = ""
#         cls.url2 = ""
#         cls.url3 = ""
#         cls.rul4 = ""
#         cls.url5 = ""
#
#
#
#     def test_1_1(self):
#         '''1_1'''
#         resp = json.loads(self.http.post(self.url1,data=data1_1))
#         self.http.logOut(msg='载入url')
#         print(self.url1)
#         self.http.logOut(msg='传入参数')
#         print(data1_1)
#         self.http.logOut(msg='解析返回参数')
#         print(json.dumps(resp,ensure_ascii=False,indent=4))
#         # self.assertEqual(resp,dataBack1_1,msg='回参全量对比失败')
#         # self.http.logOut(msg='回参全量对比成功')
#
#
#     def test_1_2(self):
#         '''1_2'''
#         resp = json.loads(self.http.post(self.url1,data=data1_2))
#         self.http.logOut(msg='载入url')
#         print(self.url1)
#         self.http.logOut(msg='传入参数')
#         print(data1_2)
#         self.http.logOut(msg='解析返回参数')
#         print(json.dumps(resp, ensure_ascii=False, indent=4))
#         # self.assertEqual(resp, dataBack1_2, msg='回参全量对比失败')
#         # self.http.logOut(msg='回参全量对比成功')
#
#
#     def test_1_3(self):
#         '''1_3'''
#         resp = json.loads(self.http.post(self.url1,data=data1_3))
#         self.http.logOut(msg='载入url')
#         print(self.url1)
#         self.http.logOut(msg='传入参数')
#         print(data1_3)
#         self.http.logOut(msg='解析返回参数')
#         print(json.dumps(resp, ensure_ascii=False, indent=4))
#         # self.assertEqual(resp, dataBack1_3, msg='回参全量对比失败')
#         # self.http.logOut(msg='回参全量对比成功')
#
#
#     def test_1_4(self):
#         '''1_4'''
#         resp = json.loads(self.http.post(self.url1,data=data1_4))
#         self.http.logOut(msg='载入url')
#         print(self.url1)
#         self.http.logOut(msg='传入参数')
#         print(data1_4)
#         self.http.logOut(msg='解析返回参数')
#         print(json.dumps(resp, ensure_ascii=False, indent=4))
#         # self.assertEqual(resp, dataBack1_4, msg='回参全量对比失败')
#         # self.http.logOut(msg='回参全量对比成功')
#
#
#
#     def test_1_5(self):
#         '''1_5'''
#         resp = json.loads(self.http.post(self.url1,data=data1_5))
#         self.http.logOut(msg='载入url')
#         print(self.url1)
#         self.http.logOut(msg='传入参数')
#         print(data1_5)
#         self.http.logOut(msg='解析返回参数')
#         print(json.dumps(resp, ensure_ascii=False, indent=4))
#         # self.assertEqual(resp, dataBack1_5, msg='回参全量对比失败')
#         # self.http.logOut(msg='回参全量对比成功')
#
#     def test_2_1(self):
#         '''2_1'''
#         resp = json.loads(self.http.post(self.url2, data=data2_1))
#         self.http.logOut(msg='载入url')
#         print(self.url2)
#         self.http.logOut(msg='传入参数')
#         print(data2_1)
#         self.http.logOut(msg='解析返回参数')
#         print(json.dumps(resp, ensure_ascii=False, indent=4))
#         # self.assertEqual(resp, dataBack2_1, msg='回参全量对比失败')
#         # self.http.logOut(msg='回参全量对比成功')
#
#     def test_2_2(self):
#         '''2_2'''
#         resp = json.loads(self.http.post(self.url2, data=data2_2))
#         self.http.logOut(msg='载入url')
#         print(self.url2)
#         self.http.logOut(msg='传入参数')
#         print(data2_2)
#         self.http.logOut(msg='解析返回参数')
#         print(json.dumps(resp, ensure_ascii=False, indent=4))
#         # self.assertEqual(resp, dataBack2_2, msg='回参全量对比失败')
#         # self.http.logOut(msg='回参全量对比成功')
#
#     def test_2_3(self):
#         '''2_3'''
#         resp = json.loads(self.http.post(self.url2, data=data2_3))
#         self.http.logOut(msg='载入url')
#         print(self.url2)
#         self.http.logOut(msg='传入参数')
#         print(data2_3)
#         self.http.logOut(msg='解析返回参数')
#         print(json.dumps(resp, ensure_ascii=False, indent=4))
#         # self.assertEqual(resp, dataBack2_3, msg='回参全量对比失败')
#         # self.http.logOut(msg='回参全量对比成功')
#
#     def test_2_4(self):
#         '''2_4'''
#         resp = json.loads(self.http.post(self.url2, data=data2_4))
#         self.http.logOut(msg='载入url')
#         print(self.url2)
#         self.http.logOut(msg='传入参数')
#         print(data2_4)
#         self.http.logOut(msg='解析返回参数')
#         print(json.dumps(resp, ensure_ascii=False, indent=4))
#         # self.assertEqual(resp, dataBack2_4, msg='回参全量对比失败')
#         # self.http.logOut(msg='回参全量对比成功')
#
#     def test_2_5(self):
#         '''2_5'''
#         resp = json.loads(self.http.post(self.url2, data=data2_5))
#         self.http.logOut(msg='载入url')
#         print(self.url2)
#         self.http.logOut(msg='传入参数')
#         print(data2_5)
#         self.http.logOut(msg='解析返回参数')
#         print(json.dumps(resp, ensure_ascii=False, indent=4))
#         # self.assertEqual(resp, dataBack2_5, msg='回参全量对比失败')
#         # self.http.logOut(msg='回参全量对比成功')
#
#     def test_3_1(self):
#         '''3_1'''
#         resp = json.loads(self.http.post(self.url3, data=data3_1))
#         self.http.logOut(msg='载入url')
#         print(self.url3)
#         self.http.logOut(msg='传入参数')
#         print(data3_1)
#         self.http.logOut(msg='解析返回参数')
#         print(json.dumps(resp, ensure_ascii=False, indent=4))
#         # self.assertEqual(resp, dataBack3_1, msg='回参全量对比失败')
#         # self.http.logOut(msg='回参全量对比成功')
#
#     def test_3_2(self):
#         '''3_2'''
#         resp = json.loads(self.http.post(self.url3, data=data3_2))
#         self.http.logOut(msg='载入url')
#         print(self.url3)
#         self.http.logOut(msg='传入参数')
#         print(data3_2)
#         self.http.logOut(msg='解析返回参数')
#         print(json.dumps(resp, ensure_ascii=False, indent=4))
#         # self.assertEqual(resp, dataBack3_2, msg='回参全量对比失败')
#         # self.http.logOut(msg='回参全量对比成功')
#
#     def test_3_3(self):
#         '''3_3'''
#         resp = json.loads(self.http.post(self.url3, data=data3_3))
#         self.http.logOut(msg='载入url')
#         print(self.url3)
#         self.http.logOut(msg='传入参数')
#         print(data3_3)
#         self.http.logOut(msg='解析返回参数')
#         print(json.dumps(resp, ensure_ascii=False, indent=4))
#         # self.assertEqual(resp, dataBack3_3, msg='回参全量对比失败')
#         # self.http.logOut(msg='回参全量对比成功')
#
#     def test_3_4(self):
#         '''3_4'''
#         resp = json.loads(self.http.post(self.url3, data=data3_4))
#         self.http.logOut(msg='载入url')
#         print(self.url3)
#         self.http.logOut(msg='传入参数')
#         print(data3_4)
#         self.http.logOut(msg='解析返回参数')
#         print(json.dumps(resp, ensure_ascii=False, indent=4))
#         # self.assertEqual(resp, dataBack3_4, msg='回参全量对比失败')
#         # self.http.logOut(msg='回参全量对比成功')
#
#     def test_3_5(self):
#         '''3_5'''
#         resp = json.loads(self.http.post(self.url3, data=data3_5))
#         self.http.logOut(msg='载入url')
#         print(self.url3)
#         self.http.logOut(msg='传入参数')
#         print(data3_5)
#         self.http.logOut(msg='解析返回参数')
#         print(json.dumps(resp, ensure_ascii=False, indent=4))
#         # self.assertEqual(resp, dataBack3_5, msg='回参全量对比失败')
#         # self.http.logOut(msg='回参全量对比成功')
#
#     def test_4_1(self):
#         '''4_1'''
#         resp = json.loads(self.http.post(self.url4, data=data4_1))
#         self.http.logOut(msg='载入url')
#         print(self.url4)
#         self.http.logOut(msg='传入参数')
#         print(data4_1)
#         self.http.logOut(msg='解析返回参数')
#         print(json.dumps(resp, ensure_ascii=False, indent=4))
#         # self.assertEqual(resp, dataBack4_1, msg='回参全量对比失败')
#         # self.http.logOut(msg='回参全量对比成功')
#
#     def test_4_2(self):
#         '''4_2'''
#         resp = json.loads(self.http.post(self.url4, data=data4_2))
#         self.http.logOut(msg='载入url')
#         print(self.url4)
#         self.http.logOut(msg='传入参数')
#         print(data4_2)
#         self.http.logOut(msg='解析返回参数')
#         print(json.dumps(resp, ensure_ascii=False, indent=4))
#         # self.assertEqual(resp, dataBack4_2, msg='回参全量对比失败')
#         # self.http.logOut(msg='回参全量对比成功')
#
#     def test_4_3(self):
#         '''4_3'''
#         resp = json.loads(self.http.post(self.url4, data=data4_3))
#         self.http.logOut(msg='载入url')
#         print(self.url4)
#         self.http.logOut(msg='传入参数')
#         print(data4_3)
#         self.http.logOut(msg='解析返回参数')
#         print(json.dumps(resp, ensure_ascii=False, indent=4))
#         # self.assertEqual(resp, dataBack4_3, msg='回参全量对比失败')
#         # self.http.logOut(msg='回参全量对比成功')
#
#     def test_4_4(self):
#         '''4_4'''
#         resp = json.loads(self.http.post(self.url1, data=data4_4))
#         self.http.logOut(msg='载入url')
#         print(self.url4)
#         self.http.logOut(msg='传入参数')
#         print(data4_4)
#         self.http.logOut(msg='解析返回参数')
#         print(json.dumps(resp, ensure_ascii=False, indent=4))
#         # self.assertEqual(resp, dataBack4_4, msg='回参全量对比失败')
#         # self.http.logOut(msg='回参全量对比成功')
#
#     def test_4_5(self):
#         '''4_5'''
#         resp = json.loads(self.http.post(self.url4, data=data4_5))
#         self.http.logOut(msg='载入url')
#         print(self.url4)
#         self.http.logOut(msg='传入参数')
#         print(data4_5)
#         self.http.logOut(msg='解析返回参数')
#         print(json.dumps(resp, ensure_ascii=False, indent=4))
#         # self.assertEqual(resp, dataBack4_5, msg='回参全量对比失败')
#         # self.http.logOut(msg='回参全量对比成功')
#
#     def test_5_1(self):
#         '''5_1'''
#         resp = json.loads(self.http.post(self.url5, data=data5_1))
#         self.http.logOut(msg='载入url')
#         print(self.url5)
#         self.http.logOut(msg='传入参数')
#         print(data5_1)
#         self.http.logOut(msg='解析返回参数')
#         print(json.dumps(resp, ensure_ascii=False, indent=4))
#         # self.assertEqual(resp, dataBack5_1, msg='回参全量对比失败')
#         # self.http.logOut(msg='回参全量对比成功')
#
#     def test_5_2(self):
#         '''5_2'''
#         resp = json.loads(self.http.post(self.url5, data=data5_2))
#         self.http.logOut(msg='载入url')
#         print(self.url5)
#         self.http.logOut(msg='传入参数')
#         print(data5_2)
#         self.http.logOut(msg='解析返回参数')
#         print(json.dumps(resp, ensure_ascii=False, indent=4))
#         # self.assertEqual(resp, dataBack5_2, msg='回参全量对比失败')
#         # self.http.logOut(msg='回参全量对比成功')
#
#     def test_5_3(self):
#         '''5_3'''
#         resp = json.loads(self.http.post(self.url5, data=data5_3))
#         self.http.logOut(msg='载入url')
#         print(self.url5)
#         self.http.logOut(msg='传入参数')
#         print(data5_3)
#         self.http.logOut(msg='解析返回参数')
#         print(json.dumps(resp, ensure_ascii=False, indent=4))
#         # self.assertEqual(resp, dataBack5_3, msg='回参全量对比失败')
#         # self.http.logOut(msg='回参全量对比成功')
#
#     def test_5_4(self):
#         '''5_4'''
#         resp = json.loads(self.http.post(self.url5, data=data5_4))
#         self.http.logOut(msg='载入url')
#         print(self.url5)
#         self.http.logOut(msg='传入参数')
#         print(data5_4)
#         self.http.logOut(msg='解析返回参数')
#         print(json.dumps(resp, ensure_ascii=False, indent=4))
#         # self.assertEqual(resp, dataBack5_4, msg='回参全量对比失败')
#         # self.http.logOut(msg='回参全量对比成功')
#
#     def test_5_5(self):
#         '''5_5'''
#         resp = json.loads(self.http.post(self.url1, data=data5_5))
#         self.http.logOut(msg='载入url')
#         print(self.url5)
#         self.http.logOut(msg='传入参数')
#         print(data5_5)
#         self.http.logOut(msg='解析返回参数')
#         print(json.dumps(resp, ensure_ascii=False, indent=4))
#         # self.assertEqual(resp, dataBack5_5, msg='回参全量对比失败')
#         # self.http.logOut(msg='回参全量对比成功')
#
