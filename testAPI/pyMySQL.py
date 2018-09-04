# import pymysql.cursors
#
# # 创建连接
# db = pymysql.connect(host='47.97.23.104', port=3306, user='panjinmin', passwd='pjm*djkj@HZ2018', db='db_djkj_a')
# # 创建游标
# cursor = db.cursor()

# # 执行SQL，并返回收影响行数
# effect_row = cursor.execute("update hosts set host = '1.1.1.2'")

# 执行SQL，并返回受影响行数
# effect_row = cursor.execute("update hosts set host = '1.1.1.2' where nid > %s", (1,))

# 执行SQL，并返回受影响行数
# effect_row = cursor.executemany("insert into hosts(host,color_id)values(%s,%s)", [("1.1.1.11",1),("1.1.1.11",2)])
# cursor.execute("SELECT VERSION()")
# # sjb = cursor.execute('select*from pay_orders_djkj where order_id=2017120512231441840000000006')
# # print(sjb)
# Data = cursor.fetchone()
#
# print (f"Database version : {Data[0]}" )
# # # 关闭连接
# db.close()
# sql = 'select*from pay_orders_djkj where order_id=2017120512231441840000000006'
# try:
#     # 执行SQL语句
#     cursor.execute(sql)
#     # 获取所有记录列表
#     results = cursor.fetchall()
#     # for row in results:
#     #     fname = row[0]
#     #     lname = row[1]
#     #     age = row[2]
#     #     sex = row[3]
#     #     income = row[4]
#     #     # 打印结果
#     #     print("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
#     #           (fname, lname, age, sex, income))
#     print(results)
# except:
#     print("Error: unable to fetch Data")


# import pymysql.cursors
#
# # 创建连接
# # db = pymysql.connect(host='47.97.23.104', port=3306,
# #                      user='panjinmin', passwd='pjm*djkj@HZ2018', db='db_djkj_a')
# db=pymysql.connect(host='47.97.23.104 ',port=3306,
#                    user='zhangjinhong',passwd='zjh*djkj@HZ2018',db='db_djkj_a')
# #创建游标
# cursor = db.cursor()
# sql = 'select*from pay_orders_djkj where order_id=2017120512231441840000000006'
# # sql2 = 'select column_name from information_schema.COLUMNS where table_name="pay_orders_djkj" and TABLE_SCHEMA="db_djkj_a"'
# cursor.execute(sql)
# # cursor.execute(sql2)
# #     # 获取所有记录列表
# results = cursor.fetchall()
# print(results)
# # 关闭数据库连接
# db.close()


#python 操作mysql
#cmd---c----pip3 install PyMysql   要执行很多次才可以成功

#创建连接
# # config_pjm = {"host":"47.97.23.104 ","port":3306,
# #               "user":"panjinmin","passwd":"pjm*djkj@HZ2018","db":"db_djkj_a"}
# config_zjh = {"host":"47.97.23.104 ","port":3306,
#               "user":"zhangjinhong","passwd":"zjh*djkj@HZ2018",
#               "db":"db_djkj_a","charset":"utf8"}
# db=pymysql.connect(**config_zjh)
# #创建游标
# cursor=db.cursor()
# sql='select * from dj_account'# where id=93930'
# cursor.execute(sql)#execute执行一个数据库查询和命令
# results=cursor.fetchall()#返回给客户端执行后的数据,
# print(results)
# #关闭数据库连接
# cursor.close()#关闭游标
# db.close()#关闭连接
#
#
# '''对数据库进行操作'''

# sql_insert="insert into dj_account(account,mobile)values('zhangjinhong','18067988289')"
# sql_update="update dj_account set mobile=11111111111 where id=7"
# sql_delete="delete from dj_account where account='18067898289'"
# try:
# 	cursor.execute(sql_insert)
# 	print cursor.rowcount#打印sql语句对数据库造成几行影响
# 	cursor.execute(sql_update)
# 	print cursor.rowcount
# 	cursor.execute(sql_delete)
# 	print cursor.rowcount
# 	db.commit()#提交事务，让操作生效
# except Exception as e:
# 	print e  #打印出现了什么问题
# 	db.rollback()#让所有操作回到没有操作前的状态

import pymysql.cursors
def db_seleect(sql=None):
    config_zjh = {"host": "47.97.23.104 ", "port": 3306,
                  "user": "zhangjinhong", "passwd": "zjh*djkj@HZ2018",
                  "db": "db_djkj_a", "charset": "utf8"}
    db = pymysql.connect(**config_zjh)
    # 创建游标
    cursor = db.cursor()
    # sql = 'select * from dj_account'  # where id=93930'
    cursor.execute(sql)  # execute执行一个数据库查询和命令
    results = cursor.fetchall()  # 返回给客户端执行后的数据,
    # 关闭数据库连接

    cursor.close()  # 关闭游标
    db.close()  # 关闭连接
    # return results
    return results[0][0]

if __name__ == '__main__':
    # sql = 'select * from dj_account'  # where id=93930
    sql ="select id from dj_account where mobile = 13255716570"
    print(db_seleect(sql))
    # db_seleect()

