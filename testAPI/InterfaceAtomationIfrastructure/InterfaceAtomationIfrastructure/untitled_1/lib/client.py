
from requests import Session
# from user_agent import generate_user_agent
from .recursion import GetDictParam


class HttpHandler(GetDictParam):
    http = None
    def __init__(self):
        super(HttpHandler, self).__init__()
        self.session = Session()
        self.headers = {
            # 'User-Agent': generate_user_agent()
        }

    def get(self, url):
        '''get请求'''
        resp = self.session.get(url, headers=self.headers).json()
        return resp

    def post(self, url, data=None, json=None, headers=None):
        '''post请求'''
        if json is not None:
            return self.session.post(url, json=json, headers=headers).json()
        return self.session.post(url, data=data, headers=headers).json()



