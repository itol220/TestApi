#-*- coding: utf-8 -*-
# __author__ = 'Administrator'
import requests
from lxml import etree
import json

html = requests.get('http://testerlife.com').text

element = etree.HTML(html).xpath('//title/text()')
print(element)

class TesterlifeCrawl:
    def __init__(self):
        self.page_url = "http://testerlife.com"
        self.__name = "tedterlife"
        self.__modify_Xpath = None
        self.html = self.get_page_html()


    def get_page_html(self):
        resp = requests.get(self.page_url)
        if resp.encoding != 'utf-8':
            resp.encoding = 'utf-8'
        return resp.text
    def parse(self,xpath):
        result = etree.HTML(self.html).xpath(xpath)
        self.__modify_Xpath = None
        return result

    def set_xpaths(self,xpath):
        self.__modify_Xpath = xpath


    def __repr__(self):
        if self.__modify_Xpath:
            return json.dumps(self.parse(self.__modify_Xpath),ensure_ascii=False,indent=4)
        return "没有指定xpath属性"


if __name__ == '__main__':
    crawl = TesterlifeCrawl()
    crawl.set_xpaths("//*[@id='post-tester_4']/div[1]/div[1]/blockquote/p/text()")
    print(crawl)


class TesterHome(TesterlifeCrawl):
    def __init__(self):
        super(TesterHome,self).__init__()
        self.page_url = 'http://testerhome.com'
        self.__name ='testerhome'
        self.html =self.get_page_html()


class QiuBai(TesterlifeCrawl):
    def __init__(self):
        super(QiuBai,self).__init__()
        self.page_url = 'https://www.qiushibaike.com/'
        self.__name = 'qiushibaike'
        self.html = self.get_page_html()


class Crawl:
    def __init__(self,url,name):
        self.url,self.name = url,name

    def request(self,url):
        resp = requests.get(url)
        if resp.encoding != 'utf-8':
            resp.encoding = 'utf-8'
        return resp.text
    def parse(selfself,html,xpaths):
        element = etree.HTML(html)
        if isinstance(xpaths,(tuple,list)):
            return [element.xpath(xpath) for xpath in xpaths]
        return element.xpath(xpaths)


    def output(self,url,xpath):
        htnl = self.request(url)
        return self.parse(html,xpath)


class QiuShiBaiKe(Crawl):
    def __init__(self,url,name):
        super(QiuShiBaiKe,self).__init__()
