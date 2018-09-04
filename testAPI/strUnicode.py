# import json
# j1 = {"ret":1,"msg":"\u83b7\u53d6\u6210\u529f","Data":{"account":"\u53f6\u5b50\u4e5f\u7ea2\u4e86","coin":"110","third_pic":"https:\/\/tfs.alipayobjects.com\/images\/partner\/TB1VSxAXRhI81Jk6XUEXXc3yXXa","voucher_count":"4"}}
# print("\u83b7\u53d6\u6210\u529f")
# print('\u53f6\u5b50\u4e5f\u7ea2\u4e86')
# j2 = {"ret":1,"msg":"\u83b7\u53d6\u6210\u529f","Data":{"Data":[{"id":"735255","voucher_id":"111","limit":"20","discount":"3","type_id":"0","store_id":"0","unit_type":"2","type":"2","from":"15","start_time":"1531367578","end_time":"1533959578","expired":0,"from_name":"\u6e38\u73a9\u6fc0\u52b1","store_name":""},{"id":"735253","voucher_id":"108","limit":"2","discount":"2","type_id":"0","store_id":"0","unit_type":"1","type":"1","from":"15","start_time":"1531367559","end_time":"1533959559","expired":0,"from_name":"\u6e38\u73a9\u6fc0\u52b1","store_name":""},{"id":"735252","voucher_id":"107","limit":"3","discount":"1","type_id":"0","store_id":"0","unit_type":"1","type":"1","from":"15","start_time":"1531367559","end_time":"1533959559","expired":0,"from_name":"\u6e38\u73a9\u6fc0\u52b1","store_name":""}],"total_count":3,"recharge_conut":"1","pay_count":"2"}}
# j3 = {"id":"1","template_id":"1","store_id":"3","vip_id":"598865","src":"http:\/\/src.scfy.i3020.com\/contract\/usersign\/1532428707uje9.png","create_time":"2018\/07\/24 18:38:29","is_del":"0","id_number":"0","name":"\u6d4b\u8bd5\u5408\u540c","user_name":"\u5f20\u840d","mobile":"18367139328","template_src":"http:\/\/src.scfy.i3020.com\/"},{"id":"2","template_id":"1","store_id":"89","vip_id":"598873","src":"http:\/\/src.scfy.i3020.com\/contract\/usersign\/15324878031bdl.png","create_time":"2018\/07\/25 11:03:23","is_del":"0","id_number":"0","name":"\u6d4b\u8bd5\u5408\u540c","user_name":"qwqe","mobile":"15657196570","template_src":"http:\/\/src.scfy.i3020.com\/"},{"id":"3","template_id":"3","store_id":"89","vip_id":"598873","src":"http:\/\/src.scfy.i3020.com\/contract\/usersign\/15324878381ejz.png","create_time":"2018\/07\/25 11:03:59","is_del":"0","id_number":"0","name":"\u6d4b\u8bd5002","user_name":"qwqe","mobile":"15657196570","template_src":"http:\/\/src.scfy.i3020.com\/"},{"id":"4","template_id":"1","store_id":"89","vip_id":"598873","src":"http:\/\/src.scfy.i3020.com\/contract\/usersign\/1532487867ods5.png","create_time":"2018\/07\/25 11:04:27","is_del":"0","id_number":"0","name":"\u6d4b\u8bd5\u5408\u540c","user_name":"qwqe","mobile":"15657196570","template_src":"http:\/\/src.scfy.i3020.com\/"},{"id":"5","template_id":"1","store_id":"89","vip_id":"598870","src":"http:\/\/src.scfy.i3020.com\/contract\/usersign\/1532487990xckr.png","create_time":"2018\/07\/25 11:06:30","is_del":"0","id_number":"0","name":"\u6d4b\u8bd5\u5408\u540c","user_name":"yoy7","mobile":"13255716570","template_src":"http:\/\/src.scfy.i3020.com\/"}
# j4 = {"return_code":"0","msg":"\u67e5\u8be2\u6210\u529f","Data":[{"vip_id":"222374","user_name":"null","sex":"0","card_no":"#ZG379009#","mobile":"null","type_id":"0","card_type_id":"2","birthday":"null","id_number":"null"},{"vip_id":"598835","user_name":"\u5f20\u840d","sex":"2","card_no":"#ZG379009#","mobile":"18367139328","type_id":"1","card_type_id":"10","birthday":"19930601","id_number":"null"},{"vip_id":"598838","user_name":"null","sex":"0","card_no":"#ZG379009#","mobile":"null","type_id":"0","card_type_id":"2","birthday":"null","id_number":"null"},{"vip_id":"598839","user_name":"null","sex":"0","card_no":"#ZG379009#","mobile":"null","type_id":"0","card_type_id":"2","birthday":"null","id_number":"null"}]}
#
# print(json.dumps(j4,ensure_ascii=False))

# l1 = ['w','e',2,4,5]
# l2 = ['e',2,4,'f',6]
# l3 = [item for item in l1 if item not in l2]
# print(l3)
# sum = 0
# for i in range(10):
#     for j in range(10):
#         sum += j
#         print(sum)
# import os,re
# import xlrd
# from xlutils.copy import copy
# path_py = "c:\example_BOM.xls"    #以.py文件运行时读取excel时的路径
# # path_exe = "..\excel\example_BOM.xls"  #以.exe文件运行时读取excel时的路径
# # path = cur_file_dir(path_py,)#path_exe)  #获取到需要复制excel文件的路径
# # print (path)                          #打印excel文件路径
# rbook = xlrd.open_workbook(path_py)       #读取excel文件，只能读取内容无法读取excel格式信息
# wbook = copy(rbook)                    #复制excel
# wsheet = wbook.get_sheet(0)            #通过get_sheet()获取的sheet有write()方法
# wsheet.write(5, 0, 'changed!')         #在sheet 0的第六行第一列写入changed
# wbook.save('c:/temp_BOM.xls')             #保存复制修改过的excel
# raw_input("Enter enter key to exit...")
import xlrd,time,re,hashlib
import xlutils.copy
timeNow = time.strftime('%Y-%m-%d %H:%M:%S')
# x=xlrd.open_workbook(r'c:\aa.xlsx','wb')   #打开文件
# print(f'—————{timeNow} ：打开成功—————')
# workbook=xlutils.copy.copy(x)#复制文件
# print(f'—————{timeNow} ：复制成功—————')
# worksheet=workbook.get_sheet(0)#获取sheet
# print(f'—————{timeNow} ：获取页签成功—————')
# worksheet.write(2,0,'明天还是睡觉')#修改操作
# print(f'—————{timeNow} ：写入成功—————')
# workbook.save(r'c:/xlutils_save.xlsx')#另存为
# print(f'—————{timeNow} ：保存成功—————')
q,w,e,r,t, = 1,2,3,4,5
s = f'{q,w,e}asdf{r,t}'
s1 = re.sub('[(, )]','',s)
# re.sub('[(, )]','',s)
# sr = re.sub('[(, )]', '',s)
# print(s1,type(s1))
# print(round(time.time()))
# print(hashlib.md5(s1.encode()).hexdigest())
# def fp():
#     resp = None
#     for i in [1,2,3,4,5]:
#         if i==3:
#             resp='r'
#     print( resp)
# fp()
# r = []
# j = 1
# for i in range(5):
#     d = {}
#     v = j
#     for x in range(10):
#         d[str(x)] = x
#     r.append(d)
#     j+=1
# print(r)
l = []
for i in range(5):
    for j in range(10):
        d = {}
        d[i] = j
        l.append(d)
print(l)




