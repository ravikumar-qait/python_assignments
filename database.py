import mysql.connector
import json

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="119181229Rk##",
  database = "mydatabase"
)
print("connected")

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE posts10 (userId int, id int, title VARCHAR(255), body VARCHAR(255))")

with open('/home/qainfotech/Desktop/json_data/my.json') as handle:
    mylist = json.loads(handle.read())


for mydict in mylist:
    placeholders = ', '.join(['%s'] * len(mydict))
    columns = ', '.join("" + str(x).replace('/', '_') + "" for x in mydict.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in mydict.values())
    sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % ('posts10', columns, values)
    print(sql)
    mycursor.execute(sql)


mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM posts10")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

