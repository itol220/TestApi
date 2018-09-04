# -*- coding:utf-8 -*-
from Data import  readExcel,mySql
from api import getDetailById,createDev
from time import strftime
from unittest import TestCase


class getDetailByIdTest(TestCase):
    def test001(self):
        self.a=getDetailById(self,int(readExcel("getDetailById",1,2)),int(readExcel("getDetailById",1,3)),int(readExcel("getDetailById",1,4)))
        self.assertEqual(str(self.a.json()),readExcel("getDetailById",1,5))

    def test002(self):
        self.a=getDetailById(self,int(readExcel("getDetailById",2,2)),int(readExcel("getDetailById",2,3)),int(readExcel("getDetailById",2,4)))
        self.assertEqual(str(self.a.json()),readExcel("getDetailById",2,5))

    def test003(self):
        self.a=getDetailById(self,int(readExcel("getDetailById",3,2)),int(readExcel("getDetailById",3,3)),int(readExcel("getDetailById",3,4)))
        self.assertEqual(str(self.a.json()),readExcel("getDetailById",3,5))


class createDevTest(TestCase):
    @classmethod
    def setUpClass(self):
        self.sn=strftime("%y%m%d%H%M%S")

    def test001(self):
        self.assertEqual(0,mySql('SELECT sn from t_dev_list where sn="%s"'%self.sn))
        self.a=createDev(self.sn)
        c=mySql('SELECT sn from t_dev_list where sn="%s"'%self.sn)
        self.assertEqual(1,c)
        self.assertEqual(self.a.json(),{u'msg': u'Success', u'code': 0})

    def test002(self):
       self.assertEqual(1,mySql('SELECT sn from t_dev_list where sn="%s"'%self.sn))
       self.a=createDev(self.sn)
       c=mySql('SELECT sn from t_dev_list where sn="%s"'%self.sn)
       self.assertEqual(1,c)
       self.assertEqual(self.a.json(),{u'msg': u'此sn码已注册', u'code': 102})





