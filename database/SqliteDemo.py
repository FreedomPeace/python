import sqlite3
#连接到Sqlite数据库
# 数据库文件是test.db
# 如果数据库文件不存在，则会在当前目录创建
conn = sqlite3.connect('test.db')
#创建cursor
cursor = conn.cursor()
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id,name) values (\'1\', \'jack\')')
# 通过rowcount获取插入的行数
cursor.rowcount
#关闭游标
cursor.close()
#提交事务
conn.commit()
# 关闭连接
conn.close()

