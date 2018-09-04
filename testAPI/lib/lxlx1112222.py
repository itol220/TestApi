# v = [
#     {"name": "电脑", "price": 1999},
#     {"name": " 鼠标", "price": 10},
#     {"name": "游艇", "price": 20},
#     {"name": "美 女 ", "price": 998}
# ]
# sum_m = 0
# lis_car = []
# print('--------------欢迎光临-------------')
# user_money = input('请输入您的金额')
# if int(user_money) > 0:
#     while 1:
#         for index,item in enumerate(v,1):
#             print(index,item['name'].strip(),item['price'])
#         stor_num_user = input('请输入您要购买的商品序号/退出请按Q/结算B')
#         if stor_num_user.strip().isdigit():
#             if 0 < int(stor_num_user) < len(v)+1:
#                 sum_m = sum_m + v[int(stor_num_user)-1]['price']
#                 if int(user_money) < sum_m:
#                     print('添加商品失败，余额不足')
#                 else:
#                     user_l_money = int(user_money) - sum_m
#                     print('添加商品成功, 余额为：', user_l_money)
#                 lis_car.append(sum_m)
#             else:
#                 print('请输入有效数字')
#         elif stor_num_user.strip().isalpha():
#             if stor_num_user.strip().upper() == 'B':
#                 lis_car_money = sum(lis_car)
#                 if lis_car_money < int(user_money):
#                     print('剁手成功，账户余额：',user_l_money)
#                     break
#                 else:
#                     print('余额不足,请充值')
#                     break
#         else:
#             print('输入正确退出按键')
# else:
#     print('余额为0，请充值再购物')
import hashlib,copy,random,string
from requests import Session,request
# import requests

a = "a test string"
print(hashlib.md5(a.encode('utf-8')).hexdigest())
sum = lambda a,b : a+b
print(sum(2,3))
a = ['1','2','3',5]
b = ['a','b',3,5]

dict1 = lambda a,b: {k:v for k,v in zip(a,b)}
print(dict1(a,b))
n = '测试' + ''.join(random.sample(string.digits,6)) + random.choice(string.ascii_letters)
a = {'1':'4','2':'a','a':n}

b=copy.deepcopy(a)
b['a']=n
print(a)
print(b)
print(random.random())
a=3
b=5
print(a,b)
print([item for item in dir(request)])#if "__" not in item])
