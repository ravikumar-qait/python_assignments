import mysql.connector
import json

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="119181229Rk##",
  database = "mydatabase"
)
# ankitksr: Never put stray print statements in final code submission.
print("connected")

mycursor = mydb.cursor()

# ankitksr:
# What does 'posts10' denote? If it is a variable name, think about renaming it to something more relevant.
mycursor.execute("CREATE TABLE posts10 (userId int, id int, title VARCHAR(255), body VARCHAR(255))")

# ankitksr:
# Never use hardcoded paths in your code. As a result, no one else can run your script.
# Re-implement using 'relative paths'.
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

# ankitksr:
# Please print the final result with proper formatting.
for x in myresult:
  print(x)

