# #-*- coding: utf-8 -*-
#
# # c=dir(dict())
# #
# # print(list(d for d in c if '_' not in d))
# #
# # user_dict={}
# # beijing=user_dict.get('beijing','北京')
# # print(beijing)
# # # print(user_dict['beijing'])
# # # dict.items()
# # user_dict=dict(beijing='北京',shanghia='上海',tianjin='天津')
# # print(type(user_dict.keys()))
# # # print(user_dict.keys()[1])
# # # print(type(list(user_dict.keys())))
# # # print(list(user_dict.keys())[0])
# #
# # for key,value in user_dict.items():
# #     print(key,value)
# # from time import sleep
#
#
# # num=0
# # while num<100:
# #     num+=1
# #     try:
# #         if num==90:
# #             raise ValueError('num==100,so except')
# #     except ValueError as ex:
# #         print(num)
# #         print(ex)
# # print(num)
# # while num<100:
# #     num+=1
# #     try:
# #         if num==100:
# #             raise ValueError('num==100,so except')
# #     except ValueError as ex:
# #         print(num)
# #         print(ex)
# # print(num)
# # userdict={}
# # userdict.update(pangwang=1)
# # userdict['11']='十一'
# # userdict.update({'11':1})
# # # dict.update,dict.update,dict.default
# # dict[key]=new_value
# # print(userdict)
# # f_bool=False
# # f_none=None
# # {}==>type({}) dict
# # set()==>type(set()) set
# # class._bool_
#
# # print(bool(integer))
# # print(bool(string))
# # print(bool(f_bool))
# # f_list=[]
# # f_list.append('Raymond')
# # t_list=f_list.copy()
# # t_list=["Raymond"]
# # if t_list and len(t_list)>2:
# #     print(len(t_list))
# # elif not t_list:
# #     print('True list is empty')
# # elif t_list.count('Raymond') !=0:
# #     print("t_list.count('Raymond')) != 0")
# # elif len(t_list)*2==4:
# #     print('len(t_list)*)2==4')
# # else:
# #     print('Raymond')
# # f_list.append('Raymond')
# # t_list=f_list.copy()
# # t_list=['Raymond']
# #
# # if t_list and len(t_list)>2:
# #     print(len(list))
# # elif not t_list:
# #     print('True list is empty')
# # elif t_list.count('Raymond') != 0:
# #     print("t_list.count('Raymond') != 0")
# # elif len(t_list)*2 == 4:
# #     print("len(t_list)*2 == 4")
# # else:
# #     print('normal')
# # userinfo=['Raymond','gang','dog','devan','牛仔']
# # string_text='Hi Raymond'
# # for user in userinfo:
# #     print(user)
# # for text in string_text:
# #     print(text)
# # for key in list(userdict.keys()):
# #     print(key)
# # for param in userinfo:
# #     print(param)
# # string_text = 'Hi Raymond'
# # for user in userinfo:
# #     print(user)
# # for text in string_text:
# #     print text
# # for key in list(userdict.keys()):
# #     print(key)
# # for param in userinfo:
# #     print(param)
# # while 1,while True,while num < 5
# # while len(userinfo) <= 10:
# #     print(len(userinfo))
# #     userinfo.append('Raymond')
# #     userinfo.append('222')
# #
# # for item in userinfo:
# #     if item == 'dog':
# #         break
# #     print(item)
# # for item in userinfo:
# #     if item == 'dog':
# #         break
# #     print(item)
# # while 1:
# #     num = 0
# #     for _ in range(10):
# # userinfo=['Raymond','gang','dog','devan','牛仔']
# # for item in userinfo:
# #     if 'dog' == item:
# #         continue
# #     elif 'Raymond' == item:
# #         pass
# #     elif item == 'devan':
# #         break
# #     print(item)
# # for number in range(3,11,2):
# #     # number = 3
# #     print(number)
# #     if number == 3:
# #         pass
# #     elif number == 5:
# #         continue
# #     elif number == 7:
# #         continue
# #     else:
# #         break
#
# # import random
# # import string
# #
# # # module: python中，每个单独的文件， 代表一个module
# # # packages : pip install requests  python site-packages/requests/， 每个文件夹代表packages
# #
# # numbers = list(range(1,100))
# # print(random.choice(numbers))
# # print(random.randint(1,99)) # random.randint 接受2个参数，一个是起始点， 一个是结束点， 从这两个点之间(包含这两点)随机返回
# # print(random.sample(numbers,8))
# # print(list(item for item in dir(string) if not item.startswith('_')))
# # print(numbers)
# # random.shuffle(numbers)# random.shuffle 接受一个列表，并把这个列表中全部的元素位置打乱， 返回None, 会改变原有的列表index
# # print(numbers)
# #
# #
# # print(string.ascii_letters) # string.ascii_letters 打印a-z,A-Z 全部的大小写的26个英文字符的一个字符串
# # print(string.digits)# string.digits 返回一个0-9的全部数据的字符串
# # print(string.ascii_lowercase)
# # print(string.ascii_uppercase)
# #
# #
# # numbers = list(string.digits)
# # headers = ['138','134','139','140','131','155','157']
# #
# # e_number = ''.join(random.sample(numbers,8)) # 随机生成一个手机号
# # mobile_number = random.choice(headers)+e_number
# # print(mobile_number)
# #
# # num = 8
# # footer = ['@163.com','@qq.com','@yahoo.com','@126.com']
# # header = ''.join(random.sample(list(string.digits + string.ascii_letters),num))
# # email = header + random.choice(footer)
# # print(email)
# # #mode:r,rb,w,wb,a,a+
# # file = open('log.txt',mode='w',encoding='utf-8')
# # file.write('这是python写进来的log\n')
# # file.write('这是python写进来的log\n')
# # file.write('好吧，我要写很多个file.write')
# # # w覆盖
# # file.close()
# # file.write('mode=a时，我要在这个文件的最后位置新增一行信息')
# # file.close()
# #
# #
# # file = open('log.txt',mode='a',encoding='utf-8')
# # file.writelines(['\n我是整行写入的','\nq我想在这一行再加一些备注'])
# # file.writelines(['\n我是第二个整行','\n好吧我觉得我没什么写的了就是想在这里占一个位置'])
# # file.close()
# # file = open('log.txt',mode='a',encoding='utf-8')
# # file.write(['\n我是整行写入的','\nq我想在这一行再加一些备注'])
# # file.writelines(['\n我是第二个整行','\n好吧我觉得我没什么写的了就是想'])
# # file.write(['\n我是第二个整行','\n好吧我觉得我没什么写的了就是想在这里占一个位置'])
# # file.close()
#
#
# # string_text = '我是雷蒙德!'
# # print('string_text',string_text,type(string_text))
# # bytes_text = string_text.encode()
# # bytes_text = string_text.encode()
# # print('bytes_text',bytes_text,type(bytes_text))
# #
# # bytes2string = bytes_text.decode()
# # bytes2string = bytes_text.decode()
# # print(bytes2string)
# #
# # with open('log.txt',mode='rb') as file:
# #     Data = file.read()
# #     print(file.read())
#
# import json
# from abc import ABCMeta
# from abc import abstractmethod
#
# class Fruits(metaclass=ABCMeta):
#     '''
#      这上一个水果的父类
#     '''
#     @abstractmethod
#     def buy(self):
#         pass
#
#     @abstractmethod
#     def throw(self):
#         pass
#
#     @abstractmethod
#     def sell(self):
#         pass
#
#     def param(self):
#         pass
#
# class Apple(Fruits):
#     def buy(self):
#         print('购买一个苹果')
#
#     def sell(self):
#         print('卖掉一个苹果')
#
#     def throw(self):
#         print('苹果坏了，扔了它')
#
#
# class Banana(Fruits):
#     def buy(self):
#         print('买一个香蕉')
#
#     def sell(self):
#         print('卖掉一个香蕉')
#
#     def throw(self):
#         print('这个香蕉坏掉了，扔了它')
# # apple = Apple()
# # apple.buy()
# # apple.sell()
# # apple.throw()
# # banana = Banana()
# # banana.buy()
# # banana.sell()
# # banana.throw()
# class People():
#     def __init__(self,name,age,city,work):
#         self.user = name,age,city,work
#         self.title = ('name','age','city','work')
#
#     def get_user_info(self):
#         return json.dumps({key:value for key,value in zip(self.title,self.user)},indent=4,)
#
# class Teacher(People):
#     def _init_(self,name,age,city):
#         self.work = 'teacher'
#         super(Teacher,self).__init__(name,age,city,self.work)
#
# class Student(People):
#     def __init__(self,name,age,city):
#         self.work = "student"
#         super(Student,self).__init__(name,age,city,self.work)
#
# class Worker(People):
#     def __init__(self):
#         self.users = 'Raymond',20,'北京','工人'
#         super(Worker,self).__init__(*self.users)
#
# # if __name__ == '__main__':
# #     worker = Worker()
# #     print(worker.get_user_info())
#
#
#
#
#
#
#
#
#
#
#
# class Duck:
#     def __init__(self,_quack,_fly):
#         self._quack = _quack
#         self._fly = _fly
#         self.type = '真'
#
#     def swim(self):
#         print('swiming...')
#
#     def display(self):
#         print(self._quack)
#         print(self._fly)
#         self.swim()
#         return '我只是一只{}的鸭子'.format(self.type)
#
#
# class GreenDuck(Duck):
#     def __init__(self):
#         super(GreenDuck,self).__init__(None,None)
#         self._quack = '我会叫'
#         self._fly = '我会飞'
#         self.type = '绿头'
#
#     def green_quack(self):
#         return 'gua gua gua'
#
#
# class RubberDuck(Duck):
#     def __init__(self):
#         self._quack = '我不会叫'
#         self._fly = '我不会飞'
#         super(RubberDuck,self).__init__(self._quack.self._fly)
#         self.type = '橡皮'
#
#
#     def swim(self):
#         print('橡皮鸭漏气了，不会游泳了')
#         return '我不能游泳了'
#
# class DecoyDuck(RubberDuck):
#     def __init__(self):
#         super(DecoyDuck,self).__init__()
#         self.type = '诱饵'
#
#
# # if __name__ == '__main__':
# #     green = GreenDuck()
# #     print(green.display())
# #     green.swim()
# #     print(green.green_quack())
#     # duck = Duck('我会跳','我会笑')
#     # print(duck.display())
# from abc import ABCMeta
# from abc import abstractmethod
#
# def return_sum_number(*args,**kwargs):
#     if kwargs.get('param'):
#         args = kwargs.get('param')
#         return sum(args)
#
# class Animal(metaclass=ABCMeta):
#     def __init__(self,animal_name,animal_age,animal_color,**kwargs:dict):
#         self.animal_info = [animal_name,animal_age,animal_color]
#         if kwargs:
#             self.animal_info.append(kwargs)
#
#     @abstractmethod
#     def call(self):
#         pass
#
#
#     @abstractmethod
#     def swim(self):
#         pass
#     @abstractmethod
#     def fly(self):
#         pass
#     @abstractmethod
#     def run(self):
#         pass
#
#     def display(self):
#         if len(self.animal_info) == 3:
#             print('这是一只{}动物，它今年{}岁了，它有一身漂亮{}颜色'.format(*self.animal_info))
#         else:
#             print('这是一只{}动物，它今年{}岁了，它有一身漂亮{}颜色'.format(*self.animal_info[0:3]))
#             info = ''
#             for key,value in self.animal_info[-1].items():
#                 info += key + ',' + value + '.'
#             print('他还有一些特殊的属性：{}'.format(info))
#
#     def __repr__(self):
#         result = self.display()
#         return '' if not result else result
#
#
# class Dog(Animal):
#     def __init__(self,name,age,color,**kwargs):
#         super(Dog,self).__init__(name,age,color,**kwargs)
#
#
#     def call(self):
#         print('汪汪汪！')
#
#     def swim(self):
#         print('狗子会游泳')
#
#
#     def fly(self):
#         print('狗子不会飞')
#
#
#     def run(self):
#         print('狗子跑的快')
#
# class Duck(Animal):
#     def __init__(self,name,age,color,**kwargs):
#         super(Duck,self).__init__(name,age,color,**kwargs)
#
#
#     def call(self):
#         print('Quack!Quack!Quack!')
#
#
#     def swim(self):
#         print('鸭子会游泳')
#
#
#     def fly(self):
#         print('鸭子不会飞')
#
#
#     def run(self):
#         print('鸭子没有狗子跑的快')
#
# if __name__ == '__main__':
#     dog = Dog(1,2,3)
#     print(dog)
#
# import json
# import random
# import string
# import time
# FIST_NAME_ENUM = '赵钱孙李周吴赵王'
# LAST_NAME_ENUM = '与玉鱼兴冰明架膦认顺'
#
# class Data:
#     def __init__(self,mobile_number_head=None,first_name_head=None,name_lenth=None):
#         self.first_name = first_name_head
#         self.mobile_head = mobile_number_head
#         self.mobile_lenth = name_lenth
#
import time,random
from concurrent.futures import ThreadPoolExecutor

def get_max_num(max_num):
    time.sleep(random.randint(1,3))
    print(f"{max_num} is running")
    return max_num


if __name__ == '__main__':
    max_num = (55,32,66,7,2)
    thread = ThreadPoolExecutor(max_workers=3)
    for item in max_num:
        result = thread.submit(get_max_num,item)