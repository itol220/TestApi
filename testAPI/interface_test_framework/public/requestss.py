# -*- coding: utf-8 -*-
# @Author  : hanzilong
import json,requests


# 定义请求类
class request:
    def get(self, url, params=None, headers=None):  #get请求
        try:
            # payload = dict(key1='value1', key2='value2')
            r = requests.get(url, params=params, headers=headers)
            # 转换为python类型的字典格式,json包的响应结果，调用json(),转换成python类型
            r.encoding='UTF-8'
            json_r=r.status_code
            # return {'code':0,'result':json_r}
            return json_r
        except BaseException as e:
            print("请求失败,出错提示：%s"%e)

    def post(self, url, data, headers):   #post请求
        try:
            r = requests.post(url, data=data, headers=headers)
            # 转换为python类型的字典格式,json包的响应结果，调用json(),转换成python类型
            r.encoding = 'UTF-8'
            json_r = r.status_code
            return json_r
        except BaseException as e:
            print("请求失败，出错提示：%s"%e)
    def post_json(self, url, data, headers):  #post_json 请求
        try:
            # python类型转化为json类型
            data = json.dumps(data)
            r = requests.post(url, data=data, headers=headers)
            json_r = r.status_code
            return json_r
        except Exception as e:
            print("请求失败，出错提示：%s"%e)
