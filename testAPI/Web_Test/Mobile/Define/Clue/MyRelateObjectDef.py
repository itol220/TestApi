# -*- coding:UTF-8 -*-
'''
Created on 2016-8-16
我的信息相关对象定义，包括排行榜、积分商城等
@author: hongzenghui
'''
#用户信息
from CONFIG import Global
userInfo = {"mobilePhone":Global.XianSuoDftMobile, #手机号
            "password":Global.XianSuoDftPassword, #密码
            "verifyCode":"", #验证码
            "newPassword":"", #新密码
            "verifyPassword":"", #确认密码
            "inviteCode":"", #邀请码
            "cityName":"", #所属市
            "districName":"", #所属区
            "streetName":"", #所属街道
            "nickName":"", #昵称
            "point":"", #积分
            "picturePath":"C:\\autotest_file\\AppImage\\headPic.png", #头像
            "address":"", #常住地址
            }