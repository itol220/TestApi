# -*- coding:UTF-8 -*-
'''
Created on 2015-11-12

@author: N-254
'''
from __future__ import unicode_literals

from CONFIG import Global
from Interface.XiaoFangXiTong.Common import CommonIntf

roleInit = {
           'DftShengRoleName':'测试自动化省岗位',
           'DftShiRoleName':'测试自动化市岗位',
           'DftQuRoleName':'测试自动化区岗位',
           'DftJieDaoRoleName':'测试自动化街道岗位',
           'DftSheQuRoleName':'测试自动化社区岗位',
           'DftWangGeRoleName':'测试自动化网格岗位',
           }

orgInit = {
           'DftShengOrg':'测试自动化省',
           'DftShengOrgId':CommonIntf.getDbQueryResult(dbCommand = "select t.id from ORGANIZATIONS t where t.orgname='测试自动化省'"),
           'DftShengFuncOrg':'测试自动化省公安部', #职能部门
           'DftShengFuncOrgId':CommonIntf.getDbQueryResult(dbCommand = "select t.id from ORGANIZATIONS t where t.orgname='测试自动化省公安部'"),
           'DftShengFuncOrgType':'公安部门', #部门类型
           'DftShiOrg':'测试自动化市',
           'DftShiOrgId':CommonIntf.getDbQueryResult(dbCommand = "select t.id from ORGANIZATIONS t where t.orgname='测试自动化市'"),
           'DftShiFuncOrg':'测试自动化市公安部',
           'DftShiFuncOrgId':CommonIntf.getDbQueryResult(dbCommand = "select t.id from ORGANIZATIONS t where t.orgname='测试自动化市公安部'"),
           'DftShiFuncOrgType':'公安部门',
           'DftQuOrg':'测试自动化区',
           'DftQuOrgId':CommonIntf.getDbQueryResult(dbCommand = "select t.id from ORGANIZATIONS t where t.orgname='测试自动化区'"),
           'DftQuFuncOrg':'测试自动化区公安部',
           'DftQuFuncOrgId':CommonIntf.getDbQueryResult(dbCommand = "select t.id from ORGANIZATIONS t where t.orgname='测试自动化区公安部'"),
           'DftQuFuncOrgType':'公安部门',
           'DftQuMinBanFuncOrg':'测试自动化区民办中心',
           'DftQuMinBanFuncOrgId':CommonIntf.getDbQueryResult(dbCommand = "select t.id from ORGANIZATIONS t where t.orgname='测试自动化区民办中心'"),
           'DftQuMinBanFuncOrgType':'民办中心',
           'DftJieDaoOrg':'测试自动化街道',
           'DftJieDaoOrgId':CommonIntf.getDbQueryResult(dbCommand = "select t.id from ORGANIZATIONS t where t.orgname='测试自动化街道'"),
           'DftJieDaoFuncOrg':'测试自动化街道派出所',
           'DftJieDaoFuncOrgId':CommonIntf.getDbQueryResult(dbCommand = "select t.id from ORGANIZATIONS t where t.orgname='测试自动化街道派出所'"),
           'DftJieDaoFuncOrgType':'公安部门',
           'DftJieDaoFuncOrg1':'测试自动化街道民政部',
           'DftJieDaoFuncOrgId1':CommonIntf.getDbQueryResult(dbCommand = "select t.id from ORGANIZATIONS t where t.orgname='测试自动化街道民政部'"),
           'DftJieDaoFuncOrgType1':'民政部门',
           'DftSheQuOrg':'测试自动化社区',
           'DftSheQuOrgId':CommonIntf.getDbQueryResult(dbCommand = "select t.id from ORGANIZATIONS t where t.orgname='测试自动化社区'"),
           'DftWangGeOrg':'测试自动化网格',
           'DftWangGeOrgId':CommonIntf.getDbQueryResult(dbCommand = "select t.id from ORGANIZATIONS t where t.orgname='测试自动化网格'"),
           'DftWangGeOrg1':'测试自动化网格1',
           'DftWangGeOrgId1':CommonIntf.getDbQueryResult(dbCommand = "select t.id from ORGANIZATIONS t where t.orgname='测试自动化网格1'")
           }

userInit = {
            'DftShengUser':'zdhp@sg',
            'DftShengUserXM':'自动化省用户',     #姓名
            'DftShengUserSJ':'13011111111',  #手机
            'DftShengFuncUser':'zdhpzn@sg',
            'DftShengFuncUserXM':'自动化省职能用户',
            'DftShengFuncUserSJ':'13022222222',
            'DftShiUser':'zdhs@',
            'DftShiUserXM':'自动化市用户',
            'DftShiUserSJ':'13033333333',
            'DftShiFuncUser':'zdhszn@',
            'DftShiFuncUserXM':'自动化市职能用户',
            'DftShiFuncUserSJ':'13044444444',
            'DftQuUser':'zdhq@',
            'DftQuUserXM':'自动化区用户',
            'DftQuUserSJ':'13055555555',
            'DftQuFuncUser':'zdhqzn@',
            'DftQuFuncUserXM':'自动化区职能用户',
            'DftQuFuncUserSJ':'13066666666',
            'DftQuMinBanFuncUser':'zdhqmbzn@',
            'DftQuMinBanFuncUserXM':'自动化区民办职能用户',
            'DftQuMinBanFuncUserSJ':'13266666666',
            'DftQuFuncUserSJ':'13066666666',
            'DftJieDaoUser':'zdhjd@',
            'DftJieDaoUserXM':'自动化街道用户',
            'DftJieDaoUserSJ':'13077777777',
            'DftJieDaoFuncUser':'zdhjdzn@',
            'DftJieDaoFuncUserXM':'自动化街道职能用户',
            'DftJieDaoFuncUserSJ':'13088888888',
            'DftJieDaoFuncUser1':'zdhjdzn1@',
            'DftJieDaoFuncUserXM1':'自动化街道职能用户1',
            'DftJieDaoFuncUserSJ1':'13088888889',
            'DftSheQuUser':'zdhsq@',
            'DftSheQuUserXM':'自动化社区用户',
            'DftSheQuUserSJ':'13099999999',
            'DftWangGeUser':'zdhwg@',
            'DftWangGeUserXM':'自动化网格用户',
            'DftWangGeUserSJ':'13111111111',
            'DftWangGeUser1':'zdhwg1@',
            'DftWangGeUserXM1':'自动化网格用户1',
            'DftWangGeUserSJ1':'13222222222'
            }

xianSuoOrgInit={
                'DftShengOrg':'测试自动化省',
                'DftShengOrgId':CommonIntf.getDbQueryResult(dbCommand = "select t.id from ORGANIZATIONS t where t.orgname='测试自动化省'",dbIp=Global.XianSuoYunWeiInfo['DbIp'], dbInstance=Global.XianSuoYunWeiInfo['DbInstance'], dbUser=Global.XianSuoYunWeiInfo['DbUser'], dbPass=Global.XianSuoYunWeiInfo['DbPass']),
                'DftShiOrg':'测试自动化市',
                'DftShiOrgId':CommonIntf.getDbQueryResult(dbCommand = "select t.id from ORGANIZATIONS t where t.orgname='测试自动化市'",dbIp=Global.XianSuoYunWeiInfo['DbIp'], dbInstance=Global.XianSuoYunWeiInfo['DbInstance'], dbUser=Global.XianSuoYunWeiInfo['DbUser'], dbPass=Global.XianSuoYunWeiInfo['DbPass']),
                'DftQuOrg':'测试自动化区',
                'DftQuOrgId':CommonIntf.getDbQueryResult(dbCommand = "select t.id from ORGANIZATIONS t where t.orgname='测试自动化区'",dbIp=Global.XianSuoYunWeiInfo['DbIp'], dbInstance=Global.XianSuoYunWeiInfo['DbInstance'], dbUser=Global.XianSuoYunWeiInfo['DbUser'], dbPass=Global.XianSuoYunWeiInfo['DbPass']),
                'DftQuOrgIdNo':CommonIntf.getDbQueryResult(dbCommand = "select t.departmentNo from ORGANIZATIONS t where t.orgname='测试自动化区'",dbIp=Global.XianSuoYunWeiInfo['DbIp'], dbInstance=Global.XianSuoYunWeiInfo['DbInstance'], dbUser=Global.XianSuoYunWeiInfo['DbUser'], dbPass=Global.XianSuoYunWeiInfo['DbPass']),
                'DftJieDaoOrg':'测试自动化街道',
                'DftJieDaoOrgId':CommonIntf.getDbQueryResult(dbCommand = "select t.id from ORGANIZATIONS t where t.orgname='测试自动化街道'",dbIp=Global.XianSuoYunWeiInfo['DbIp'], dbInstance=Global.XianSuoYunWeiInfo['DbInstance'], dbUser=Global.XianSuoYunWeiInfo['DbUser'], dbPass=Global.XianSuoYunWeiInfo['DbPass']),
                'DftJieDaoUser':'管理员',
                'DftJieDaoUserName':CommonIntf.getDbQueryResult(dbCommand = "select t.username from usersessions t where t.userrealname='管理员'",dbIp=Global.XianSuoYunWeiInfo['DbIp'], dbInstance=Global.XianSuoYunWeiInfo['DbInstance'], dbUser=Global.XianSuoYunWeiInfo['DbUser'], dbPass=Global.XianSuoYunWeiInfo['DbPass']),
                'DftJieDaoUserId':CommonIntf.getDbQueryResult(dbCommand = "select t.userid from usersessions t where t.userrealname='管理员'",dbIp=Global.XianSuoYunWeiInfo['DbIp'], dbInstance=Global.XianSuoYunWeiInfo['DbInstance'], dbUser=Global.XianSuoYunWeiInfo['DbUser'], dbPass=Global.XianSuoYunWeiInfo['DbPass']),
               
                }

