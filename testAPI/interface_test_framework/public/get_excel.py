# -*- coding: utf-8 -*-
# @Author  : hanzilong

import xlrd

from interface_test_framework.public.log import Log


def get_case(path1):
    all_case = []
    open = xlrd.open_workbook(path1)  #打开xlsx
    me = open.sheets()[0]           #打开xlsx的第一个table
    nrows = me.nrows
    Log.info(r"打开测试用例!")
    # for循环遍历case
    for i in range(1, nrows):
        all_case.append({'id': me.cell(i,  0).value, 'key': me.cell(i, 2).value,
                            'coneent': me.cell(i, 3).value, 'url': me.cell(i, 4).value,
                            'name': me.cell(i, 1).value, 'fangshi': me.cell(i, 5).value,
                            'assert': me.cell(i, 6).value})
    return all_case





