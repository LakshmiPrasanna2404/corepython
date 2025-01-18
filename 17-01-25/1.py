
import mysql.connector as c
mydb = c.connect(
  host="localhost",
  user="root",
  password="1234",
  database="cvr"
)
mycursor = mydb.cursor()
mycursor.execute("create table student1(sid int,sname varchar(20))")
#name=input("Enter your name")
#id = input("Enter your id")
#mycursor.execute("insert into student11 values(%s,%s)",(id,name))
print("Hii")