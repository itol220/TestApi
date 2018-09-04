#
# '''
# 基于python3.5
# '''
# from config import config
# from lib import HttpHandler
# import json,unittest,time,hashlib
#
# param_addIss = {
#             'issueNew.issueContent': '{}'.format(HttpHandler().newName())+config.contents,
#             'issueNew.occurDate': time.strftime("%Y-%m-%d"),
#             'hours': time.strftime("%H"),
#             'minute': time.strftime("%M"),
#             'issueNew.uniqueIdForMobile': round(time.time() * 1000),
#             'datetime': time.strftime("%Y-%m-%d %H:%M:%S")
#         }
#
# class PATlogin(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         cls.http = HttpHandler()
#         cls.param_addIss = param_addIss
#         cls.param_addIss['issueNew.subject'] = cls.http.newName()
#         cls.login_url = '{}mobile/sessionManageMobileManage/login.action'.format(config.Host)
#         cls.addIssue_url = '{}mobile/issueNewMobileManage/addIssue.action'.format(config.Host)
#         cls.updateIssue_url = '{}mobile/issueNewMobileManage/updateIssue.action'.format(config.Host)
#         cls.findNeedDoIssueList_url = '{}mobile/issueNewMobileManage/findNeedDoIssueList.action'.format(config.Host)
#         cls.deleteIssue_url = '{}mobile/issueNewMobileManage/deleteIssue.action'.format(config.Host)
#         cls.viewIssueDetail_url = '{}mobile/issueNewMobileManage/viewIssueDetail.action'.format(config.Host)
#
#
#     def setUp(self):
#         self.http.post(url=self.login_url, data=config.login_data)
#
#     def tearDown(self):
#         self.setUpClass()
#
#     def test_login(self):
#         '''[test_login]验证登录正确/空/加密后密码/错误'''
#
#         data_ZDHsq_md5 = {
#             'password': hashlib.md5((config.data_ZDHsq['password']).encode('utf-8')).hexdigest(),
#             'userName': 'zdhsq@',
#             'tqmobile': 'true',
#             'isNewLoginVersion': 'true'
#         }
#         resp = json.loads(self.http.post(url=self.login_url,data=config.data_ZDHsq))
#         self.assertEqual(self.http.get_value(resp,"name"),config.login_userInfo["operatorName"],msg="正确用户名验证失败")
#         self.assertEqual(resp["result"],"success")
#         resp = json.loads(self.http.post(url=self.login_url, data=config.data_ZDHsq_none))
#         self.assertEqual(resp["errorCode"],"001",msg="空用户名验证失败")
#         self.assertEqual(resp["Data"],"{userName:'用户名或密码错误'}")
#         resp = json.loads(self.http.post(url=self.login_url, data=data_ZDHsq_md5))
#         self.assertEqual(resp["errorCode"], "001", msg="md5用户名验证失败")
#         self.assertIn(resp["Data"], config.errorInfo_login)
#         resp = json.loads(self.http.post(url=self.login_url, data=config.data_ZDHsq_error))
#         self.assertEqual(resp["errorCode"], "001", msg="错误密码验证失败")
#         self.assertIn(resp["Data"], config.errorInfo_login)
#
#
#
#     def test_addIssue_is_ok(self):
#         '''[addIssue]事件新增'''
#         resp = json.loads(self.http.post(self.addIssue_url,data=dict(config.addIssue_param,**self.param_addIss)))
#         print(json.dumps(resp,ensure_ascii=False,indent=4))
#         self.assertEqual(self.http.get_value(resp,"result"),"success",msg="新增事件失败")
#         self.assertEqual(self.http.get_value(resp,"errorCode"),"0")
#
#     def test_updateIssue_is_ok(self):
#         '''[updateIssue]新增并修改该事件'''
#         IssueId = json.loads(self.http.post(self.addIssue_url, data=dict(config.addIssue_param, **self.param_addIss)))["Data"]
#         resp = json.loads(self.http.post(self.findNeedDoIssueList_url,data=config.list_param))
#         # print(json.dumps(self.http.get_value(resp,"rows")[0],ensure_ascii=False,indent=4))
#         result = [item for item in self.http.get_value(resp,"rows") if item["issueId"] == IssueId][0]
#         print(json.dumps(result,ensure_ascii=False,indent=4))
#         param = {'stepId': result["issueStepId"],'issueNew.id':result["issueId"], 'issueNew.occurDate': result["createDate"],
#                 'datetime': result["createDate"],'issueNew.serialNumber':result["serialNumber"],
#                  'issueNew.issueContent': '{}'.format(self.http.updateName())+config.contents,'issueNew.subject': self.http.updateName()}
#         resp = self.http.post(self.updateIssue_url,data=dict(config.updateIssue_param,**param))
#         print(resp)
#         self.assertEqual(resp,"true",msg='修改事件失败')
#
#     def test_deleteIssue_is_ok(self):
#         '''[deleteIssue]新增并删除该事件'''
#
#         param ={"android_appversion":'3.0.0.18',
#                 "tqmobile": 'true',
#                 "issueId": json.loads(self.http.post(self.addIssue_url, data=dict(config.addIssue_param, **self.param_addIss)))["Data"]
#         }
#         resp = json.loads(self.http.post(self.deleteIssue_url,data=param))
#         print(json.dumps(resp,ensure_ascii=False,indent=4))
#         self.assertEqual(resp["errorCode"],"0",msg='删除事件失败')
#         self.assertEqual(resp["Data"], True)
#
#     def test_findNeedDoIssueList_is_ok(self):
#         '''[Issue][findNeedDoIssueList]新增并在待办事件列表搜索该事件'''
#         IssueName = self.param_addIss['issueNew.subject']
#         IssueId = json.loads(self.http.post(self.addIssue_url, data=dict(config.addIssue_param, **self.param_addIss)))["Data"]
#         resp = json.loads(self.http.post(self.findNeedDoIssueList_url, data=config.list_param))
#         result = [item for item in self.http.get_value(resp, "rows") if item["issueId"] == IssueId][0]
#         # print(json.dumps(result,ensure_ascii=False,indent=4))
#         search_param = {
#             'searchIssueVo.occurOrg.id':config.login_userInfo['dealOrgId'],
#             'searchIssueVo.subject':IssueName,
#             'search':'true'
#         }
#         resp = self.http.get_value(json.loads(self.http.post(self.findNeedDoIssueList_url,data=dict(config.list_param,**search_param))),"rows")[0]
#         print(json.dumps(resp, ensure_ascii=False, indent=4))
#         self.assertEqual(result,resp,msg="搜索事件失败")
#
#     # def test_viewIssueDetail_is_ok(self):
#     #     '''[viewIssueDetail]新增并查看该事件详情'''
#     #
#     #     IssueId = json.loads(self.http.post(self.addIssue_url, Data=dict(Data.addIssue_param, **self.param_addIss)))["Data"]
#     #     resp = json.loads(self.http.post(self.findNeedDoIssueList_url, Data=Data.list_param))
#     #     result = [item for item in self.http.get_value(resp, "rows") if item["issueId"] == IssueId][0]
#     #     # print(json.dumps(self.http.get_value(result,"rows")[0],ensure_ascii=False,indent=4))
#     #     param = {'issueStepId': result["issueStepId"],'issueNewId': result["issueId"],
#     #              'managementMode':'manage','issueId': result["issueStepId"]}
#     #     resp = json.loads(self.http.post(self.viewIssueDetail_url,Data=dict(Data.viewIssue_param,**param)))
#     #     print(json.dumps(resp,ensure_ascii=False,indent=4))
#         # self.assertEqual(self.http.get_value(resp,"currentStep")["id"],param['issueStepId'])
#         # self.assertEqual(self.http.get_value(resp,"issue")["id"],param["issueNewId"])
#
# if __name__ == '__main__':
#     PATlogin().test_viewIssueDetail_is_ok()
from requests import Session