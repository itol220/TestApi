import requests,json

host = 'https://httpbin.org/'
# url =  f'{host}get'
addx = 'cookies'
url = ''.join([host,addx])
# print(url)
# r = requests.get(url)
# # print(r.url)
# # print(r.status_code,r.reason)
# # print(r.headers)
# print(type(r.text))
# # print(r.content)
# print(type(r.json()))
# # print(json.dumps(json.loads(r.text),ensure_ascii=False,indent=4))
# print(json.dumps(r.json(),ensure_ascii=False,indent=4))

# params = {'show_env':1}
# Data = {'a':'巧吧软件测试','b':'form-Data'}
# # Data = {'show_env':1,'a':'巧吧软件测试','b':'form-Data'}
# # r = requests.post(url,Data=Data)
# r = requests.post(url,params=params,Data=Data)
# print(r.text)
# print(r.headers)
# print(r.json()['form'])
url1 = 'http://www.baidu.com/'

r = requests.get(url1)
print(r.cookies)
d = requests.utils.dict_from_cookiejar(r.cookies)
print(d)
print({a.name:a.value for a in r.cookies})

cookies = {'cookie-name':'qiaoba'}
r1 = requests.get(url,cookies=cookies)

import requests
import unittest


class xxx(unittest.TestCase):  # 编写一个测试类，从unittest.TestCase继承


    # 在调用一个测试方法的前后方便执行
    def setup(self):
        print('setup....')


    # 以test开头的方法是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。
    # 每一类测试都需要编写一个test_xxx()方法。
    def test_get(self):
        host = 'https://httpbin.org/'
        endpoint = 'get'
        url = ''.join([host, endpoint])
        r = requests.get(url)
        print(r.url)  # 获取url
        print(r.status_code)  # 获取状态码
        self.assertEqual(abs(-1), 1)  # 断言函数返回结果是1
        # self.assertNotEqual(a,b)#断言返回的结果不相等
        # self.assertTrue(x)#判断是否为真
        # self.assertFalse(x)#判断是否为假
        # self.asserts(a,b)#判断a是否在b中
        # self.asserts(a,b)#判断a不在b中
        # with self.assertRaises(KeyError):
        value = d['empty']  # 访问不存在的key时，断言会抛出keyError


    def test_post(self):
        url = 'http://test.pl.k6.com/ywwl-wechat-web-test/user/info'
        params = {"token": "mc44otuzmdg1nty4ntkxnjdfntu3odkzmjeyotuxntg2",
                  "domainId": "YWUS25810483431157100E04C7EF0AB1"}  # 字典形式

        r = requests.get(url, params='params')
        result = r.json()
        print(r.text)
        print(r.status_code)


    def tearDown(self):
        print('tearDown...')


# 运行单元测试
if __name__ == '__main__':

    unittest.main()  # 代码底部加上可以直接运行单元测试

    # 构造测试集????????
    suite = unittest.TestSuite()
    suite.addTest(xxx("test_get"))
    suite.addTest(xxx("test_post"))

    # 执行测试
    runner = unittest.TextTestRunner()  # 通过 unittest.TextTestRunner()类中的 run()方法运行测试套件中的测试用例
    runner.run(suite)

#例子
import requests
import unittest


class GetEventListTest(unittest.TestCase):
    '''查询发布会接口测试'''


    def setUp(self):
        self.url = "http://127.0.0.1:8000/api/get_event_list/"


    def test_get_event_null(self):
        '''发布会 id 为空'''


        r = requests.get(self.url, params={'eid': ''})
        result = r.json()
        print(result)
        self.assertEqual(result['status'], 10021)
        self.assertEqual(result['message'], "parameter error")


    def test_get_event_success(self):
        '''发布会 id 为 1，查询成功'''


        r = requests.get(self.url, params={'eid': '1'})
        result = r.json()
        print(result)
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], "success")
        self.assertEqual(result['Data']['name'], "xx 产品发布会")
        self.assertEqual(result['Data']['address'], "北京林匹克公园水立方")
        self.assertEqual(result['Data']['start_time'], "2016-10-15T18:00:00")
if __name__ == '__main__':
    unittest.main()
