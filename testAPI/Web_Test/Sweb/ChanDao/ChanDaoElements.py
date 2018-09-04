# -*- coding: UTF-8 -*-
'''
Created on 2017-12-21

@author: n-313
'''
Url = "http://192.168.1.247/zentaopms/www/"
LoginUsername = 'test'
LoginPassword = 'Admin@123'
LoginUsernameInput = "//*[@id='account']"
LoginPasswordInput = "//*[@name='password']"
LoginSubmitButton = "//*[@id='submit']"

CurrentProject ="//*[@id='currentItem']"

ToChooseProject = "//*[text()='%s']"
ToChooseFirstMenu = "//*[text()='%s']"
ToChooseSecondMenu = CurrentProject +"//*[text()='%s']"

requirementData={
                 'productName':None,#所属产品
                 'moduleName':None,#所属模块
                 'plan':None,#所属计划
                 'requirementName':None,#需求名称
                 'requirementDesc':None,#需求描述
                 'acceptanceStandard':None,#验收标准
                 'requirementSource':None,#需求来源
                 'priorityLevel':None,#优先级
                 'estimatedWorkingHours':None,#预计工时
                 'keywords':None,#关键词
                 }