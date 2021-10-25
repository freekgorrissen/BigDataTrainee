import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="test"
)

mycursor = mydb.cursor()


def insert(naam, salaris):
  command = "INSERT INTO `artiesten`( `naam`, `salaris`) VALUES ('{0}','{1}')".format(naam, salaris)
  mycursor.execute(command)

artiesten = ['abba', 'hendrix', 'blof', 'ik']
salarissen = [100, 5000, 9999, 1500, 2000]

# for i in range(len(artiesten)):
#   insert(artiesten[i], salarissen[i])

mycursor.execute("SELECT * FROM artiesten")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

mydb.commit()