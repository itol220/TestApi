# -*- coding: UTF-8 -*-
'''
Created on 2015-10-5

@author: ho
'''
# 是否为仿真环境
simulationEnvironment = False

def enum( **enums ):
    return type( 'Enum', (), enums )

driver = None

DefaultUrl = "http://www.baidu.com"

PingAnJianSheUrl = "http://192.168.1.105:8070"
# PingAnJianSheUrl = "http://192.168.1.245:8070"


PingAnJianSheUser = "admin"

PingAnJianShePass = "admin"

PingAnJianSheDbIp = "192.168.1.240"

PingAnJianSheDbInstance = "tianque"

PingAnJianSheDbUser = "autotest"
# PingAnJianSheDbUser ="zhejiang_branch"

PingAnJianSheDbPass = "autotest"
# PingAnJianSheDbPass ="zhejiang_branch"
# 认证中心url
RenZhengZhongXinUrl = "http://192.168.1.108:8075"

# 认证中心服务器密码
RenZhengZhongXinAppServRootPass = "tianqueshuaige"

# 认证中心管理员账号
RenZhengZhongXinAdminUser = "admin"

# 认证中心管理员密码
RenZhengZhongXinAdminPass = "admin"

# 手机代理
ShouJiDaiLiUrl = "http://192.168.1.105:8065"

# 线索手机代理
XianSuoShouJiDaiLiUrl = "http://192.168.1.108:10800"

# 线索默认登录手机号
XianSuoDftMobile = "15967127466"

# 线索默认登录手机号昵称
XianSuoDftMobileNick = "nick_%s" % XianSuoDftMobile

# 线索默认登录密码
XianSuoDftPassword = "111111"

# 线索appKey
XianSuoAppKey = 'H2bLGFrv_6XJA5zW'

# 线索secretkey
XianSuoSecretKey = 'vVn0laqe_3YBADi5'

# 线索运维平台信息
XianSuoYunWeiInfo = {
                                'XianSuoYunWeiUrl':'http://192.168.1.108:8083',  # 线索运维平台url
                                'XianSuoYunWeiUsername':'admin',  # 线索运维平台账号
                                'XianSuoYunWeiPassword':'11111111',  # 线索运维平台密码
                                'DbIp':'192.168.1.240',  # 线索运维平台数据库ip
                                'DbInstance':'tianque',  # 线索运维平台数据库实例
                                'DbUser':'clue_autotest_105',  # 线索运维平台数据库用户
                                'DbPass':'clue_autotest_105',  # 线索运维平台数据库密码
                                'ServRootPass':"tianqueshuaige"  # 线索运维平台应用服务器密码
                                }

# 铁路护路平台信息
TieLuHuLuInfo = {
                'TieLuHuLuUrl':'http://115.236.101.203:48089',  # 铁路护路平台url
                'TieLuHuLuUsername':'lipei',  # 铁路护路平台账号
                'TieLuHuLuPassword':'11111111',  # 铁路护路平台密码
                'DbIp':'115.236.101.203',  # 铁路护路平台数据库ip
                'DbInstance':'tianque',  # 铁路护路平台数据库实例
                'DbUser':'hlxt',  # 铁路护路平台数据库用户
                'DbPass':'hlxt_',  # 铁路护路平台数据库密码
                'ServRootPass':"tianqueshuaige"  # 铁路护路平台应用服务器密码
                }

# 铁路护路平台信息
QuanKeCaiJiInfo = {
                'QuanKeCaiJiUrlBase':'http://192.168.110.178:',
                'QuanKeCaiJiUrl':'http://192.168.110.178:21100',  # 全科采集url
                'QuanKeCaiJiUsername':'admin',  # 全科采集平台账号
                'QuanKeCaiJiPassword':'tianque111',  # 全科采集平台密码
                
                'QuanKeCaiJiUsername21200':'slp',  # 21200平台账号
                'QuanKeCaiJiPassword21200':'11111111',  # 21200平台密码
                
                'QuanKeCaiJi21100Port':21100,
                'QuanKeCaiJi21300Port':21300,
                'QuanKeCaiJi21200Port':21200,
                'QuanKeCaiJi21400Port':21400,
                }

# 应用服务器的linux root用户密码
PingAnJianSheAppServRootPass = "tianqueshuaige"

ShengXiaoFangXiTongUser = "admin"

# 消防平台相关平台
XiaoFangInfo = {'ShengXiaoFangXiTongUrl':'http://192.168.1.242:8090',  # url
                'ShengXiaoFangXiTongUser':'admin',  # 默认用户名
                'ShengXiaoFangXiTongPass':'admin',  # 默认密码
                'DbIp':'192.168.1.241',  # 消防平台数据库ip
                'DbInstance':'tianque',  # 消防平台数据库实例
                'DbUser':'xiaofanggrid',  # 消防平台数据库用户
                'DbPass':'xiaofanggrid',  # 消防平台数据库密码
                }

ShengXiaoFangXiTongPass = "admin"

NewUserDefaultPassword = '11111111'

LogLevel = enum(INFO=0,DEBUG=1,ERROR=2,WARN=3)

# 移动端参数
PlatformName = "ANDROID"
PlatformVersion = 4.2
DeviceName = "9098d093"  # "R8SSYDKV9TSKUGEE"
AppPath = "C:/autotest_file"
PackageName = "com.tianque.linkage"


# 禅道登录ID
zentaosid = None
class responseClass():
    result = None
    statusLine = None
    text = None
    content = None
