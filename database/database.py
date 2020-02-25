import mysql.connector
import json

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="119181229Rk##",
  database = "mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE New_Table (userId int, id int, title VARCHAR(255), body VARCHAR(255))")

with open('my.json') as handle:
    mylist = json.loads(handle.read())


for mydict in mylist:
    placeholders = ', '.join(['%s'] * len(mydict))
    columns = ', '.join("" + str(x).replace('/', '_') + "" for x in mydict.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in mydict.values())
    sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % ('New_Table', columns, values)
    mycursor.execute(sql)


mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM New_Table")

myresult = mycursor.fetchall()

for table_data in myresult:
  print(table_data)


