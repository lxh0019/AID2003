import pymysql

# 链接数据库
db = pymysql.connect(host="localhost", port=3306,
                     user="root", password="123456",
                     database="stu", charset="utf8")
# 创建游标对象(操作数据库，执行sql语句)
cur = db.cursor()
# SQL语句
sql = "insert into class values (2,'anna',25,'m',91,'2020-7-31');"
# 执行sql语句
cur.execute(sql)
#提交到数据库
db.commit()

cur.close()
db.close()

