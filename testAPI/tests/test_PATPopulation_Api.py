# import json,time,unittest
# from lib import HttpHandler
# from Data import Data
#
#
# userInfo = Data.login_userInfo
# Host = Data.Host
# Data = Data.login_data
# list_param = {
#     'tqmobile':'true',
#     'rows':20,
#     'sord':'desc',
#     'sidx':'issueId',
#     'page':1,
#     'orgId':userInfo['dealOrgId']
# }
#
# search_param = {
#     'searchIssueVo.inputFrom':'2018-1-9',
#     'searchIssueVo.occurOrg.id':userInfo['dealOrgId'],
#     'searchIssueVo.subject':'x',
#     'searchIssueVo.inputEnd':'2018-1-9',
#     'search':'true',
#     'searchIssueVo.occurEnd':'2018-1-9',
#     'searchIssueVo.occurFrom':'2018-1-9'
# }
#
# new_param ={
#     'issueNew.occurOrg.id': userInfo['dealOrgId'],
#     'issueNew.issueContent': '{}：我人有的和主产不为这工要在地一上是中国同经以发了民'.format(HttpHandler.newName(None)),
#     'issueRelatedPeopleNames': '张小',
#     'issueRelatedPeopleTelephones':'',
#     'issueNew.occurDate': time.strftime("%Y-%m-%d"),
#     'hours': time.strftime("%H"),
#     'minute': time.strftime("%M"),
#     'issueNew.selectedBigType': '民生服务-教育',
#     'selectedBigType': 3,
#     'selectedTypes': '34',
#     'small_type': '34',
#     'issueNew.important': 'false',
#     'issueNew.subject': HttpHandler.newName(None),
#     'issueNew.uniqueIdForMobile': round(time.time()*1000),
#     'issueNew.relatePeopleCount': 1,
#     'datetime': time.strftime("%Y-%m-%d %H:%M:%S"),
#     'tqmobile': 'true',
#     'android_appversion': '3.0.0.15'
#
# }
#
# addSubmit_param = {
#     'issueNew.subject': '{}，快速上报事件内容，我人有的和主主产不为这'.format(HttpHandler.newName(None)),
#     'issueNew.issueContent': '{}，快速上报事件内容，我人有的和主主产不为这'.format(HttpHandler.newName(None)),
#     'issueNew.occurOrg.id': userInfo['dealOrgId'],
#     'issueNew.mainCharacters': '',
#     'issueNew.occurLocation': '',
#     'issueNew.relatePeopleCount': 1,
#     'issueNew.module_IssueType': '矛盾纠纷',
#     'issueNew.mSelect_secondTypeName': '其它',
#     'issueNew.occurDate': time.strftime("%Y-%m-%d"),
#     'hours': time.strftime("%H"),
#     'minute': time.strftime("%M"),
#     'issueRelatedPeopleNames': '待填写',
#     'issueRelatedPeopleTelephones': '',
#     'issueRelatedPeopleFixPhones': '',
#     'involvedPersonnel': '',
#     'content': '快速上报',
#     'selContradictionId': 19,
# }
#
# viewIssue_param = {
#     'tqmobile': 'true',
#     'keyType': 'myIssue',
#     'mode': 'doAction'
# }
#
# updateIssue_param = {
#     'issueNew.occurOrg.id': userInfo['dealOrgId'],
#     'issueNew.issueContent': '测试-{}—自动化修改内容：工要在地一经以发了民上是中国同'.format(HttpHandler.updateName(None)),
#     'issueRelatedPeopleNames': '张大小',
#     'issueRelatedPeopleTelephones': '',
#     'hours': '',
#     'minute': '',
#     'issueNew.selectedBigType': '民生服务-医疗卫生',
#     'selectedBigType': 3,
#     'selectedTypes': '35',
#     'small_type': '35',
#     'issueNew.important': 'false',
#     'issueNew.isEmergency': 'false',
#     'issueNew.subject': HttpHandler.updateName(None),
#     'issueNew.relatePeopleCount': 1,
#     'tqmobile': 'ture',
#     'android_appversion': '3.0.0.15'
# }
#
# updateIssueLogMessage_param = {
#     'issueLog.content': updateIssue_param['issueNew.issueContent'],
#     'android_appversion': '3.0.0.15',
#     'tqmobile': 'true'
# }
#
# dealIssue_param = {
#     'content': new_param['issueNew.issueContent'],
#     'issueLog.issueStep.fourTeams.id': '',
#     'issueLog.issueStep.fourTeamsTypeID': '',
#     'issueLog.fourTeamsName': '',
# }
#
#
# class ZJPAT_issue(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#
#         cls.http = HttpHandler()
#         cls.login_url = '{}mobile/sessionManageMobileManage/login.action'.format(Host)
#         cls.findNeedDoIssueList_url = '{}mobile/issueNewMobileManage/findNeedDoIssueList.action'.format(Host)
#         cls.searchDoneIssues_url = '{}mobile/issueNewMobileManage/searchDoneIssues.action'.format(Host)
#         cls.findCompletedIssues_url = '{}mobile/issueNewMobileManage/findCompletedIssues.action'.format(Host)
#         cls.findMyJurisdictionsNeedDo_url = '{}mobile/issueNewMobileManage/findMyJurisdictionsNeedDo.action'.format(Host)
#         cls.findJurisdictionsDoneIssues_url = '{}mobile/issueNewMobileManage/findJurisdictionsDoneIssues.action'.format(Host)
#         cls.addIssue_url = '{}mobile/issueNewMobileManage/addIssue.action'.format(Host)
#         cls.viewIssueDetail_url = '{}mobile/issueNewMobileManage/viewIssueDetail.action'.format(Host)
#         cls.updateIssue_url = '{}mobile/issueNewMobileManage/updateIssue.action'.format(Host)
#         cls.updateIssueLogMessage_url = '{}mobile/issueNewMobileManage/updateIssueLogMessage.action'.format(Host)
#         cls.dealIssue_url = '{}mobile/issueNewMobileManage/dealIssue.action'.format(Host)
#         cls.findHeadingType_url = '{}mobile/issueTypeMobileManage/findHeadingType.action'.format(Host)
#         cls.findChildrenByParentId_url = '{}mobile/issueTypeMobileManage/findChildrenByParentId.action'.format(Host)
#         cls.findIssueTypes_url = '{}mobile/issueNewMobileManage/findIssueTypes.action'.format(Host)
#         cls.findOrganizationsByParent_url = '{}mobile/organizationMobileManage/findOrganizationsByParent.action'.format(Host)
#         cls.findFunctionOrgByParent_url = '{}mobile/organizationMobileManage/findOrganizationsAndFunctionOrgByParent.action'.format(Host)
#         cls.getHandlePreData_url = '{}mobile/issueNewMobileManage/getHandlePreData.action'.format(Host)
#         cls.addIssueAndSubmit_url = '{}mobile/issueNewMobileManage/addIssueAndSubmit.action'.format(Host)
#
#
#     def setUp(self):
#         '''[Issue]login/登录'''
#         result = self.http.post(self.login_url,Data=Data)
#         # print(result)
#         self.assertEqual(result,"true")
#
#     def test_findNeedDoIssueList_is_ok(self):
#         '''[Issue][findNeedDoIssueList]查询待办事件列表/搜索'''
#         result = json.loads(self.http.post(self.findNeedDoIssueList_url,Data=dict(list_param,**search_param)))
#         # print(json.dumps(result,ensure_ascii=False,indent=4))
#         self.assertEqual(self.http.get_value(result,"total"),1)
#         print(self.http.get_value(result,"subject"))
#         self.assertIn(search_param["searchIssueVo.subject"],self.http.get_value(result,"subject"))
#         self.assertEqual(self.http.get_value(result,"occurOrg")["id"],search_param["searchIssueVo.occurOrg.id"])
#
#     def test_searchDoneIssues_is_ok(self):
#         '''[searchDoneIssues]查询已办事件列表/搜索'''
#         result = json.loads(self.http.post(self.searchDoneIssues_url,Data=dict(list_param,**search_param)))
#         print(json.dumps(result,ensure_ascii=False,indent=4))
#         self.assertEqual(self.http.get_value(result,"total"),1)
#         self.assertIn(search_param["searchIssueVo.subject"],self.http.get_value(result,"subject"))
#         self.assertEqual(self.http.get_value(result,"occurOrg")["id"],search_param["searchIssueVo.occurOrg.id"])
#
#     def test_findCompletedIssues_is_ok(self):
#         '''[findCompletedIssues]查询已办结事件列表/搜索'''
#         result = json.loads(self.http.post(self.findCompletedIssues_url,Data=dict(list_param,**search_param)))
#         print(json.dumps(result,ensure_ascii=False,indent=4))
#         self.assertEqual(self.http.get_value(result,"total"),1)
#         self.assertIn(search_param["searchIssueVo.subject"],self.http.get_value(result,"subject"))
#         self.assertEqual(self.http.get_value(result,"occurOrg")["id"],search_param["searchIssueVo.occurOrg.id"])
#
#     def test_findMyJurisdictionsNeedDo_is_ok(self):
#         '''[findMyJurisdictionsNeedDo]查询下辖待办事件列表/搜索'''
#         result = json.loads(self.http.post(self.findMyJurisdictionsNeedDo_url,Data=dict(list_param,**search_param)))
#         print(json.dumps(result,ensure_ascii=False,indent=4))
#         self.assertEqual(self.http.get_value(result,"total"),1)
#         self.assertIn(search_param["searchIssueVo.subject"],self.http.get_value(result,"subject"))
#         self.assertEqual(self.http.get_value(result,"occurOrg")["id"],search_param["searchIssueVo.occurOrg.id"])
#
#     def test_findJurisdictionsDoneIssues_is_ok(self):
#         '''[findJurisdictionsDoneIssues]查询下辖已办事件列表/搜索'''
#         result = json.loads(self.http.post(self.findJurisdictionsDoneIssues_url,Data=dict(list_param,**search_param)))
#         print(json.dumps(result,ensure_ascii=False,indent=4))
#         self.assertEqual(self.http.get_value(result,"total"),1)
#         self.assertIn(search_param["searchIssueVo.subject"],self.http.get_value(result,"subject"))
#         self.assertEqual(self.http.get_value(result,"occurOrg")["id"],search_param["searchIssueVo.occurOrg.id"])
#
#     def test_addIssue_is_ok(self):
#         '''[addIssue]事件新增'''
#         i = 1
#         while i < 4:
#             i += 1
#             result = json.loads(self.http.post(self.addIssue_url,Data=new_param))
#             print(json.dumps(result,ensure_ascii=False,indent=4))
#             self.assertEqual(self.http.get_value(result,"result"),"success")
#             self.assertEqual(self.http.get_value(result,"errorCode"),"0")
#
#     def test_viewIssueDetail_is_ok(self):
#         '''[viewIssueDetail]查看事件详情'''
#         result = json.loads(self.http.post(self.findNeedDoIssueList_url,Data=list_param))
#         # print(json.dumps(self.http.get_value(result,"rows")[0],ensure_ascii=False,indent=4))
#         response = self.http.list_for_key_to_dict("issueId","issueStepId",my_dict=result["rows"][0])
#         param = {'issueStepId': response["issueStepId"],'issueNewId': response["issueId"],
#                  'managementMode':'manage','issueId': response["issueStepId"]}
#         result = json.loads(self.http.post(self.viewIssueDetail_url,Data=dict(viewIssue_param,**param)))
#         print(json.dumps(result,ensure_ascii=False,indent=4))
#         self.assertEqual(self.http.get_value(result,"currentStep")["id"],param['issueStepId'])
#         self.assertEqual(self.http.get_value(result,"issue")["id"],param["issueNewId"])
#
#     def test_updateIssue_is_ok(self):
#         '''[updateIssue]事件修改'''
#         result = json.loads(self.http.post(self.findNeedDoIssueList_url,Data=list_param))
#         print(json.dumps(self.http.get_value(result,"rows")[1],ensure_ascii=False,indent=4))
#         response = self.http.list_for_key_to_dict("issueId","issueStepId","createDate","serialNumber",my_dict=self.http.get_value(result,"rows")[1])
#         param = {'stepId': response["issueStepId"],'issueNew.id':response["issueId"], 'issueNew.occurDate': response["createDate"],
#                  'datetime': response["createDate"],'issueNew.serialNumber':response["serialNumber"]}
#         result = self.http.post(self.updateIssue_url,Data=dict(updateIssue_param,**param))
#         print(result)
#         self.assertEqual(result,"true")
#
#     def test_updateIssueLogMessage_is_ok(self):
#         '''[updateIssueLogMessage]修改办理意见'''
#         result = json.loads(self.http.post(self.findCompletedIssues_url,Data=list_param))
#         response = self.http.get_value(result,"rows")[1]
#         print(json.dumps(response,ensure_ascii=False,indent=4))
#         param = { 'issueNewId': self.http.get_value(response,"issueId"),'issueId':self.http.get_value(response,"issueId")}
#         result = json.loads(self.http.post(self.viewIssueDetail_url,Data=dict(viewIssue_param,**param)))
#         print(json.dumps(result,ensure_ascii=False,indent=4))
#         response = self.http.get_value(result,"issueLogs")[0]
#         param = {'issueLogId':response["id"]}
#         result = self.http.post(self.updateIssueLogMessage_url,dict(updateIssueLogMessage_param,**param))
#         print(result)
#         self.assertEqual(result,"true")
#
#     def test_dealIssueJAn_is_ok(self):
#         '''[dealIssue]事件办理—办理中—结案'''
#         result = json.loads(self.http.post(self.findNeedDoIssueList_url,Data=list_param))
#         # print(json.dumps(self.http.get_value(result,"rows"),ensure_ascii=False,indent=4))
#         issue = self.http.selector_issue(rows=result["rows"],seKey="dealState",id=120)
#         # print(issue)
#         param = {'dealType': 1,'issueId': issue["issueId"],'stepId': issue["issueStepId"],
#                  "issueLog.targeOrg.id":-1}
#         result = self.http.post(self.dealIssue_url,Data=dict(userInfo,**dealIssue_param,**param))
#         # print(result)
#         self.assertEqual(result,"true")
#         print("办理—办理中-成功")
#         param = {'dealType': 31,'issueId': issue["issueId"],'stepId': issue["issueStepId"],
#                         'dealTime': time.strftime("%Y-%m-%d"),"issueLog.targeOrg.id":-1}
#         result = self.http.post(self.dealIssue_url,Data=dict(userInfo,**dealIssue_param,**param))
#         # print(json.dumps(result,ensure_ascii=False,indent=4))
#         self.assertEqual(result,"true")
#         print("办理—结案—成功")
#
#     def test_dealIssueJBan_is_ok(self):
#         '''[dealIssue]事件办理—交办—协同办理'''
#         result = json.loads(self.http.post(self.findNeedDoIssueList_url,Data=list_param))
#         # print(json.dumps(result,ensure_ascii=False,indent=4))
#         issue = self.http.selector_issue(rows=result["rows"],seKey="dealState",id=120)
#         # print(issue)
#         param = {'dealType': 21,'issueId': issue["issueId"],'stepId': issue["issueStepId"],
#                  'issueLog.targeOrg.id':-1,'themainOrgid':'914','specialAssignType': '2','secondaryOrgid':'915,916'}
#         result = self.http.post(self.dealIssue_url,Data=dict(userInfo,**dealIssue_param,**param))
#         self.assertEqual(result,"true",msg="事件办理—交办—协同办理成功")
#
#     def test_dealIssueSBao_is_ok(self):
#         '''[dealIssue]事件办理—上报'''
#         result = json.loads(self.http.post(self.findNeedDoIssueList_url,Data=list_param))
#         # print(json.dumps(result,ensure_ascii=False,indent=4))
#         issue = self.http.selector_issue(rows=result["rows"],seKey="dealState",id=120)
#         print(issue)
#         param = {'dealType': 41,'issueId': issue["issueId"],'stepId': issue["issueStepId"],
#                 'issueLog.targeOrg.id': 910,}
#         result = self.http.post(self.dealIssue_url,Data=dict(userInfo,**dealIssue_param,**param))
#         self.assertEqual(result,"true")
#
#     def test_dealIssueSLi_is_ok(self):
#         '''[dealIssue]事件受理'''
#         result = json.loads(self.http.post(url=self.findNeedDoIssueList_url,Data=list_param))
#         # print(json.dumps(result["rows"],ensure_ascii=False,indent=4))
#         issue = self.http.selector_issue(rows=result["rows"],id=160,seKey="dealState")
#         print(issue)
#         param = {'issueId':issue['issueId'],'dealOrgId': userInfo['dealOrgId'],'dealType':61,
#                  'issueLog.targeOrg.id':-1,'stepId':issue['issueStepId']}
#         result = self.http.post(self.dealIssue_url,Data=dict(userInfo,**param))
#         self.assertEqual(result,"true",msg="事件受理,操作失败")
#
#     def test_dealIssueYDu_is_ok(self):
#         '''[dealIssue]事件阅读'''
#         result = json.loads(self.http.post(url=self.findNeedDoIssueList_url,Data=list_param))
#         # print(json.dumps(result["rows"],ensure_ascii=False,indent=4))
#         issue = self.http.selector_issue(rows=result["rows"],seKey="dealState",id=110)
#         print(issue)
#         param = {'issueId':issue['issueId'],'dealOrgId': userInfo['dealOrgId'],'dealType':71,'stepId':issue['issueStepId']}
#         result = self.http.post(self.dealIssue_url,Data=dict(userInfo,**param))
#         self.assertEqual(result,"true",msg="事件阅读，操作失败")
#
#     def test_findChildrenByParentId_is_ok(self):
#         '''[findHeadingType]获取事件类型大类/小类'''
#         param = {'tqmobile':'true','orgId':userInfo['dealOrgId']}
#         result = json.loads(self.http.post(url=self.findHeadingType_url,Data=param))
#         self.assertIn("category",result["issueType"][0])
#         print(json.dumps(result,ensure_ascii=False,indent=4))
#         self.assertIsInstance(result["issueType"],list)
#         param = {'tqmobile':'true','orgId':userInfo["dealOrgId"],'id':result["issueType"][1]["id"],'normal':'false'}
#         result = json.loads(self.http.post(url=self.findChildrenByParentId_url,Data=param))
#         print("===================================小类如下=====================================")
#         print(json.dumps(result,ensure_ascii=False,indent=4))
#         self.assertIsInstance(result["issueType"],list)
#         self.assertIn("category",result["issueType"][1])
#
#
#     def test_findIssueTypes_is_ok(self):
#         '''[findIssueTypes]获取登陆账号层级下事件类型'''
#         result = json.loads(self.http.post(url=self.findIssueTypes_url,Data=None))
#         print(json.dumps(result,ensure_ascii=False,indent=4))
#         self.assertIsInstance(result[0]["矛盾纠纷"],list)
#         self.assertIsInstance(self.http.get_value(result,"民生服务")[0],dict)
#
#     def test_findOrganizationsByParent_is_ok(self):
#         '''[findOrganizationsByParent]获取登陆账号层级下辖层级列表'''
#         result = json.loads(self.http.post(url=self.findOrganizationsByParent_url,Data=None))
#         print(json.dumps(result,ensure_ascii=False,indent=4))
#         print(json.dumps(result["parentOrg"],ensure_ascii=False,indent=4))
#         self.assertEqual(result["parentOrg"]["id"],userInfo['dealOrgId'])
#         self.assertIsInstance(self.http.get_value(result,"orgLevel"),dict)
#
#     def test_findOrganizationsAndFunctionOrgByParent_is_ok(self):
#         '''[FunctionOrg]获取登陆账号层级下辖层级列表和职能部门'''
#         param = {'tqmobile':'true','orgId':userInfo['dealOrgId']}
#         result = json.loads(self.http.post(url=self.findFunctionOrgByParent_url,Data=param))
#         print(json.dumps(result["parentOrg"],ensure_ascii=False,indent=4))
#         self.assertEqual(result["parentOrg"]["id"],userInfo['dealOrgId'])
#         self.assertIsInstance(self.http.get_value(result,"orgLevel"),dict)
#
#     def test_getHandlePreData_is_ok(self):
#         '''[getHandlePreData]获得办理信息'''
#         result = json.loads(self.http.post(url=self.findNeedDoIssueList_url,Data=list_param))
#         print(json.dumps(result["rows"][0],ensure_ascii=False,indent=4))
#         param = {'stepId':result["rows"][0]["issueStepId"],'issueStepId':result["rows"][0]["issueStepId"]}
#         result = json.loads(self.http.post(url=self.getHandlePreData_url,Data=param))
#         print(json.dumps(result,ensure_ascii=False,indent=4))
#         self.assertIn("desc",result["canDoList"][0])
#         self.assertEqual(result["stepId"],param["stepId"])
#
#     def test_addIssueAndSubmit_is_ok(self):
#         '''[addIssueAndSubmit]快速上报'''
#         result = json.loads(self.http.post(url=self.addIssueAndSubmit_url,Data=dict(addSubmit_param,**userInfo)))
#         print(result)
#         self.assertEqual(result["errorCode"],"0")
#         self.assertEqual(result["result"],"success")
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
