import mysql.connector

# database connectie & db functies
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="raketten"
)

mycursor = mydb.cursor()

def insert(raket):
    mycursor = mydb.cursor()

    command = ("INSERT INTO `launch_vehicles`( `naam`, `payloadLEO`, `jaar`, `massa`)"
               "VALUES (%s, '%s', '%s', '%s')"
               )
    vals = (raket.naam, raket.payloadLEO, raket.jaar, raket.massa)
    mycursor.execute(command, vals)
    return None


def clear_table():
    mycursor = mydb.cursor()
    mycursor.execute("DELETE FROM `launch_vehicles` WHERE 1")
    mycursor.close()
    return None


def read_all():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM launch_vehicles")
    myresult = mycursor.fetchall()
    mycursor.close()
    for x in myresult:
        print(x)
    return None