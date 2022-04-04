import mysql.connector
mydb = mysql.connector.connect(host='localhost',user='root',password='Qw12@1999')
mycursor = mydb.cursor()
query_1 = "insert into students values ('Armen','coll2'),('arm','jhd');"
query_1 = "select * from python.students"
mycursor.execute(query_1)
rows = mycursor.fetchall()
for row in rows:
    print(row[0])
query_2 = "create database table_for_join"
mycursor.execute(query_2)
query_3 = "use table_for_join;"
mycursor.execute(query_3)
query_4 = "create table users(name varchar(20),email varchar(20));"
mycursor.execute(query_4)
query_5 = "drop table users"
mycursor.execute(query_5)
query_6 = "SHOW DATABASES LIKE 'table_for_join'"
# mycursor.execute(query_5)





