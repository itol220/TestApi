# -*- coding:UTF-8 -*-
'''
Created on 2016-8-16
线索相关对象定义，包括爆料、说说
@author: hongzenghui
'''
def enum(**enums):
    return type('Enum', (), enums)
#爆料状态
ClueStatus = enum(ADD='新增',ACCEPT='受理',DEAL='办理',CLOSE='结案')

#爆料对象
clueObject = {'address':'中国浙江省杭州市西湖区学院路', #地址
              'subject':None, #主题
              'description':None, #描述
              'picture':{'lakePic':False,
                         'lakePicPath':'C:\\autotest_file\\AppImage\\lake.png',
                         'lakePicListPath':'C:\\autotest_file\\AppImage\\lakeInList.png',
                         'schoolPic':False,
                         'schoolPicPath':'C:\\autotest_file\\AppImage\\school.png',
                         'treePic':False,
                         'treePicPath':'C:\\autotest_file\\AppImage\\tree.png',
                         'catPic':False,
                         'catPicPath':'C:\\autotest_file\\AppImage\\cat.png',
                         'penguinsPic':False,
                         'penguinsPicPath':'C:\\autotest_file\\AppImage\\penguins.png',
                         'londonPic':False,
                         'londonPicPath':'C:\\autotest_file\\AppImage\\london.png'}, #图片
              'speech':'', #语音
              'status':None, #处理状态
              'officialReplyCount':None, #官方回复数量
              'officialReplyContent':None, #官方回复内容
              'officialReplyEventFlow':{'reportContent':None,
                                        'closeContent':None},#为了检查方便，流程只检测街道上报到区，然后结案
              'commentCount':None, #评论数量
              'commentContent':None, #评论内容
              'commentPeople':None, #评论人
              'agreeCount':None, # 点赞数量
              'browseCount':None #浏览数
              }

#说说对象
shuoshuoObject = {'subject':None, #主题
              'description':None, #描述
              'picture':{'lakePic':False,
                         'lakePicPath':'C:\\autotest_file\\AppImage\\lake.png',
                         'schoolPic':False,
                         'schoolPicPath':'C:\\autotest_file\\AppImage\\school.png',
                         'treePic':False,
                         'treePicPath':'C:\\autotest_file\\AppImage\\tree.png',
                         'catPic':False,
                         'catPicPath':'C:\\autotest_file\\AppImage\\cat.png',
                         'penguinsPic':False,
                         'penguinsPicPath':'C:\\autotest_file\\AppImage\\penguins.png',
                         'londonPic':False,
                         'londonPicPath':'C:\\autotest_file\\AppImage\\london.png'}, #图片
              'commentCount':'', #评论数量
              'commentContent':'', #评论内容
              'agreeCount':'' # 点赞数量
              }

