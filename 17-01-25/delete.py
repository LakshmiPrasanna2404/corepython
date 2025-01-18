import mysql.connector
mydb=mysql.connector.connect(
	host="localhost",
	user="root",
	password="1234",
	database="test"
)

mycursor = mydb.cursor()
id = input("Enter your id:")
mycursor.execute("DELETE FROM student WHERE sid = %s", (id,))
mydb.commit()
