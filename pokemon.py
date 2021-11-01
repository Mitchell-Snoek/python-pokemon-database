import mysql.connector
import requests
import json

#connect database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password='',
  database="pokemon"
)

#create table
mycursor = mydb.cursor()
mycursor.execute('''
    CREATE TABLE pokemon (
      id int(50) not null,
      naam varchar(255) not null,
      weight int(50) not null,
      height int(50) not null
      )
               ''')
mydb.commit()

#get data and put it in table
for getal in range(1, 152):
    a = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(getal)).text
    test = json.loads(a)
    print(test['name'])
    sql = "INSERT INTO pokemon (id, naam, weight, height) VALUES (%s, %s, %s, %s)"
    val = (test['id'], test['name'], test['weight'], test['height'])
    mycursor.execute(sql, val)
    mydb.commit()
print(mycursor.rowcount, "Geslaagd!")
