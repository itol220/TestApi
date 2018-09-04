import json,random,string
from jsonschema import validate
from requests import Session
from .recursion import GetDictParam

class HttpHandler(GetDictParam):
    def __init__(self):
        super(HttpHandler,self).__init__()
        self.session = Session()

    def mobile(self):
        patten = ['138','139','140','155','158','147','131','132']
        mobile = random.choice(patten) + ''.join(random.sample(string.digits,8))
        return mobile

    def newName(self):
        newName = '测试' + ''.join(random.sample(string.digits,6)) + random.choice(string.ascii_letters)
        return newName

    def updateName(self):
        updateName = '修改' + ''.join(random.sample(string.digits,7)) + random.choice(string.ascii_letters)
        return updateName

    def get(self,url=None):
        resp = self.session.get(url=url).text
        return resp

    def post(self,url=None,data=None,json=None):
        if json:
            return self.session.post(url=url,json=json).text
        return self.session.post(url,data=data).text


    def selector_issue(self,rows=None,seKey=None,id=None):
        idList = []
        for item in rows:
            if item[seKey] == id:
                idList.append(item)
        return idList[0] if idList != [] else '列表中不存在该处理类型的事件'




    @classmethod
    def valid_json(cls,myjson,class_name,schname):
        """ 按照jsonSchema格式校验jsonkey、jsonkeyType、jsonCount """
        schfile = 'schema/%s/%s.json' % (class_name,schname)
        with open(schfile,'r',encoding='utf-8') as f:
            mysch = json.load(f)
        try:
            validate(myjson,mysch)
        except Exception as e:
            print(e)
        else:
            return True
        finally:
            pass











