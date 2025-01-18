import mysql.connector
mydb=mysql.connector.connect(
	host="localhost",
	user="root",
	password="1234",
	database="test"
)

mycursor = mydb.cursor()

name=input("Enter your name")
id = input("Enter your id")
mycursor.execute("insert into student values(%s,%s)",(id,name))
mycursor.execute("insert into student values(%s,%s)",(id,name))
mydb.commit()
  