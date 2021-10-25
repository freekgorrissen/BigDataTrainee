import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import numpy as np


################################
###     Data reading         ###
################################

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="raketten"
)


def read_db(masslow=-1, masshigh=4000000, yearlow=-1, yearhigh=3000):
    """Functie die een sql query uitvoert en omzet naar pandas dataframe. Binnen een bepaalde massa en jaar range worden
    uitgelezen."""
    cmd = "SELECT * from launch_vehicles WHERE massa BETWEEN {} AND {} "\
        "AND jaar BETWEEN {} AND {}".format(masslow, masshigh, yearlow, yearhigh)
    df = pd.read_sql(cmd, mydb)
    return df


filtered_df = read_db(masslow=1, masshigh=1500000, yearlow=1)   # read info from rocket db
all_df = read_db(masslow=1, yearlow=1)
mydb.close()      # close db connection, no longer needed

################################
###     Analysis stuff       ###
################################

# plot van gefilterde data
fig, (ax1, ax2) = plt.subplots(1, 2)

yrmax1 = filtered_df.groupby('jaar').massa.max()

x1 = yrmax1.index
y1 = yrmax1 / 1000

ax1.scatter(x1, y1)
ax1.set_title('Plot van zwaarste raket per jaar, <1500 ton')
ax1.set(xlabel='Jaar', ylabel='Gewicht (ton)')

m, b = np.polyfit(x1, y1, 1)
ax1.plot(x1, m*x1 + b)

yrmax2 = all_df.groupby('jaar').massa.max()
x2 = yrmax2.index
y2 = yrmax2/1000

ax2.scatter(x2, y2)
ax2.set_title('Plot van zwaarste raket per jaar, alle raketten')
ax2.set(xlabel='Jaar', ylabel='Gewicht (ton)')

m, b = np.polyfit(x2, y2, 1)
plt.plot(x2, m*x2 + b)

plt.show()
