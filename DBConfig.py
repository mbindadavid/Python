# MySQL databases configuration

import mysql.connector
mydb = mysql.connector.connect(
user='root',
password='Jesus@2022',
host='127.0.0.1',
database='machinga_ekyc'
)

mycursor = mydb.cursor()
sql = "select * from printing_jobs limit 1"
mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)