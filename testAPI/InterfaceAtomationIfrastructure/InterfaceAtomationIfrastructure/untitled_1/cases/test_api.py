import unittest
from InterfaceAtomationIfrastructure.InterfaceAtomationIfrastructure.untitled_1.config import config
from InterfaceAtomationIfrastructure.InterfaceAtomationIfrastructure.untitled_1.lib.client import HttpHandler

class TestDoctorsApi(unittest.TestCase):
    http = None
    '''平安出行接口测试'''

    @classmethod
    def setUpClass(cls):
        cls.http = HttpHandler()
        cls.api_url = config.enum['url']
        # cls.pcn_url = config.Config.enum.get('url').get('pcn_url')
        # cls.shop_url = config.Config.enum.get('url').get('shop_url')

    @classmethod
    def tearDownClass(cls):
        cls.http.session.close()


    def test_homeFeet(self):
        '''企业信息footer部分'''
        response = self.http.get(url='{}{}'.format(self.api_url, '/extract/homeFeet'))
        self.assertEqual(self.http.get_value(response, 'code'), 200)
        self.assertEqual(self.http.get_value(response, 'success'), True)


    def test_homeTweetsList(self):
        ''''''
        response = self.http.get(url='{}{}{}'.format(self.api_url, '/home/homeTweetsList', '?ge=1&pageSize=5&status=1'))
        self.assertEqual(self.http.get_value(response, 'code'), 200)
        self.assertEqual(self.http.get_value(response, 'success'), True)

