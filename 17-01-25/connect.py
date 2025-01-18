import mysql.connector
mydb=mysql.connector.connect(
	host="localhost",
	user="root",
	password="1234",
	database="test"
)

mycursor = mydb.cursor()

mycursor.execute("create table student(sid int,sname varchar(20))")
mydb.commit()

