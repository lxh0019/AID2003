import pymysql
import re

# 链接数据库
db = pymysql.connect(host="localhost", port=3306,
                     user="root", password="123456",
                     database="dict", charset="utf8")
# 创建游标对象(操作数据库，执行sql语句)
cur = db.cursor()
# 写数据库

file = open("dict.txt", "r")

for line in file:
    # 通过正则表达式获取单词和单词意思
    tup = re.findall(r"(\S+)\s(.*)", line)[0]
    print(tup)
    sql = "insert into words (word,mean) values (%s,%s);"
    try:
        cur.execute(sql, tup)
        db.commit()
    except Exception as e:
        # 退回到commit之前的数据库执行状态
        db.rollback()
        print(e)
cur.close()
db.close()
