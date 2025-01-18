import mysql.connector
mydb=mysql.connector.connect(
	host="localhost",
	user="root",
	password="1234",
	database="test"
)

mycursor = mydb.cursor()

mycursor.execute("select * from student")
students=mycursor.fetchall()
for std in students:
    print(std)

