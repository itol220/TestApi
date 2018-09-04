@echo off

@echo  运行环境的前提条件：
@echo  ----------------------------------------------------------------------
@echo  1、已经安装python 3.x、ddt、unittest、requests、json、logging、xlrd。
@echo  2、log 文件目录默认是F:\untitled7\logs\test.log,需要看LOG的请手动修改。
@echo  3、自动发送邮箱需要开通SMTP服务。
@echo  ----------------------------------------------------------------------
@echo  当前目录:%~dp0
@echo  ----------------------------------------------------------------------
PAUSE

py runner.py
@echo  -------------
@echo  接口测试结束！
@echo  -------------
PAUSE