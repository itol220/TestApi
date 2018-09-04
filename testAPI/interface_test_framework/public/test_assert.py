# -*- coding: utf-8 -*-
# @Author  : hanzilong

from interface_test_framework.public.requestss import request
class TestApi(object):
    def __init__(self,url=None,key=None,connent=None,fangshi=None):
        self.url = url
        self.key = key
        self.connent = connent
        self.fangshi = fangshi
    def testapi(self):
        req = request()
        self.header = {'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}
        self.headers = {'Content-Type': 'application/json;charset=utf-8'}
        response = None
        if self.fangshi == "GET":
            self.parem = {'key': self.key, 'info': self.connent}
            # self.parem= json.dumps(parem)
            response =req.get(self.url,self.parem,self.header)
            # response= r.status_code
        elif self.fangshi == 'POST_FORM':
            self.parem = {'key': self.key, 'info': self.connent}
        # self.parem = json.dumps(parem)
            response = req.post(self.url, self.parem,self.header)
        elif self.fangshi == 'POST_JSON':
            self.parem = {'key': self.key, 'info': self.connent}
            # self.parem = json.dumps(parem)
            response = req.post_json(self.url, self.parem,self.headers)
            # response = req.status_code
        else:
            print("请求不通过,请检查case用例配置")
        return response
    def getJson(self):
        json_data = self.testapi()
        return  json_data

# print(TestApi.getJson.text)
