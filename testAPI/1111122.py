
# spam = ['apple','bananas','tofu','cats']
#
# a = ','.join(spam)
# # print(str(a))
# class Person:
#     '''Represents a person.'''
#     population = 0
#
#     def __init__(self,name):
#         '''Initializes the person's Data'''
#         self.name = name
#         print('(Initializing %s)'% self.name)
#
#         # When this person is created, he/she
#         # adds to the population
#         Person.population += 1
#
#     def __del__(self):
#         '''I am dying.'''
#         print('%s says bye.'% self.name)
#         Person.population -= 1
#
#         if self.population == 0:
#             print('I am the last one.')
#         else:
#             print('There are still %d people left.'% Person.population)
#
#     def sayHi(self):
#         '''Greeting by the person.
#         Really,that's all it does.'''
#         print('Hi,my name is %s.'% self.name)
#
#     def howMany(self):
#         '''Prints the current population.'''
#         if Person.population == 1:
#             print('I am the only person here.')
#         else:
#             print('We have %d persons here.'%Person.population)
#
# alisa = Person('Alisa')
# alisa.sayHi()
# alisa.howMany()
#
# book = Person('Book')
# book.sayHi()
# book.howMany()
#
# alisa.sayHi()
# alisa.howMany()
# import json
# import math
import random,string,time,re,json

from datetime import  datetime
# newName= '测试xc01' + ''.join(random.sample(string.ascii_uppercase),4)
# print(newName)
name = '测试xc' + ''.join(random.sample(string.digits,3)) + random.choice(string.ascii_letters)
print(name)

print (time.strftime("%Y-%m-%d %H:%M:%S"))
print(time.localtime())
t = time.time()
print(t)
print (round(time.time()*1000))
print(time.strftime("%Y-%m-%d"))
print(time.strftime("%H"))
print(time.strftime("%M"))

# , time.localtime()
a = {'1':'2','q':'w'}
b = {'2':'3','w':'a'}
c = {'e':'c','c':1}
d = {'k':3,'v':'r'}
print(dict(a,**b,**c,**d))
appName = 'app.bd8a24a1fd22e4249914c22ed7f0d070.css'
print(re.findall('[^app\.]\w+[^\.css]',appName))
appN = re.findall('app\.(.*)\.css',appName)[0]
print(f'app名称：{appN}')
timeStamp = 1381419600
timeArray = time.localtime(timeStamp)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print(otherStyleTime)
# urlN = 'http://testpre.hahaipi.com/yun/index.php/store'
urlN = 'http://47.97.27.180:8118/pay/index.php/pay?mid=1733'
# print(re.findall('\.(.*)\.com',urlN)[0])
# urlH = ''.join(re.findall('http:\/\/(.*)\/',urlN)[0].split('/')[0])
urlH = urlN.split('/')[2].split('.')
print(urlH[1],type(urlH[1]))
# print(urlH)
# print([*''.join(urlH)])
if ':' in [*''.join(urlH)]:
    print(''.join(urlH).replace(':',''))
# print(''.join(urlH.split('.')))
# while i < 4:
#     i +=1
#     # print(dict(a,**b))
#     b.update(a)
#     print(b)
# Cookie = 'sid=eccdd8ac-cf9f-4c1c-a5a7-8b584ffed7bd;Path=/'
# print(Cookie)
# C = Cookie.split(',')
# print(C)
print({"data":"null","msg":"\u9a8c\u8bc1\u5931\u8d25\u975e\u6cd5\u8bf7\u6c42","return_code":-200})

data2 = {
    "q":"2",
    "w":"w"
}
print(json.dumps(data2))

print({"code":2,"message":"\u63d0\u4ea4\u5931\u8d25","referer":"http:\/\/testpre.hahaipi.com\/sms\/"})