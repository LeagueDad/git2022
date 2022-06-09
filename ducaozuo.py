'''
    pymysql使用流程
    1.建立数据库连接（db=pymysql.connect(...)）
    2.创建游标对象（c=db.cursor()）
    3.游标方法：c.execute("insert...")
    4.提交到数据库：db.commit()
    5.关闭游戏对象：c.close()
    6.断开数据库连接：db.close()
'''

import pymysql

# 连接数据库    db就是stu数据库对象
db = pymysql.connect(host='localhost',port =3306,user  = 'root',password='zhangchao',database ='stu',charset = 'utf8')


# 获取游标 （操作数据库，执行sql语句）
cur = db.cursor()

# 获取数据库数据
sql = "select * from class_1 where gender = 'w';"
# 执行正确后cur调用函数获取结果
cur.execute(sql)

# 获取一个查询结果
one_row = cur.fetchone()
print(one_row)

# 获取多个查询结果
many_row = cur.fetchmany(2)
print(many_row)

# 获取所有查询结果
all_row = cur.fetchall()
print(all_row)

# 关闭数据库
cur.close()
db.close()

