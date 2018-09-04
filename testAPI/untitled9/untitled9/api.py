# -*- coding:utf-8 -*-
import requests
def getDetailById(self,agencyId,devId,colFlag):
    self.a=requests.get("http://192.168.1.200:8888/1/dev/getDetailById?access_token=xxxxx&agencyId=%s"%agencyId+"&devId=%s"%devId+"&colFlag=%s"%colFlag)
    return self.a

def createDev(sn):
      a=requests.post("http://192.168.1.200:8888/1/dev/createDev",json={
           "access_token":"xxxxx",
           "agencyId":1,
           "userId":3,
            "sn":sn,
            "name":"设备名",
            "modelId":1,
            "describe":"描述内容"
        })
      return a


