# -*- coding:UTF-8 -*-
'''
Created on 2017-10-18

@author: N-254
'''

populationObject = {
                    'baseInfo': {'name':None, #姓名
                                 'idCardNo':None, #身份证
                                 'grid':None, #网格
                                 'haveHouse':False, #有无住所
                                 'noHouseReason':None, #无住所原因
                                 'houseAddress':None, #住所地址
                                 'englishName':None, #境外人员里面的英文名
                                 'sex':None, #境外人员页面的性别
                                 'idType':None, #境外人员页面的证件类型
                                 'idNumber':None, #境外人员页面的证件号码
                                 }, #基础信息
                    'hujiInfo':{'huhao':None #户号
                                     }, #户籍信息
                    'zhufangInfo':{'houseProperty':None #房屋用途
                                   }, #房屋信息
                    'liuruInfo':{'liuruReason':None, #流入原因
                                 }, #流入信息
                    'xinshiInfo':{'yuanZuiMing':None, #原罪名
                                  'renyuanType':None, #人员类型
                                  },
                    }