import pandas as pd
import matplotlib.pyplot as plt


################################################################################
## launch data stuff
################################################################################

launchfile = "launchlog.txt"

ldb = pd.read_fwf(launchfile) ## Launch database = ldb
ldb.drop(columns=["Unnamed: 10", "Unnamed: 11", "Unnamed: 12"], inplace=True) ## Remove empty columns with launchpad info

ldb.columns = ["Code", "Date_Full", "Time", "COSPAR",
                "Payload1", "Payload2", "SATCAT", "LV_Type", "LV_Serial",
                "Site", "Succes", "Reference"]

# split date into year and date
ldb["Year"] = ldb["Date_Full"].str.slice(start=0, stop=4)
ldb["Date"] = ldb["Date_Full"].str.slice(start=4, stop=None)


plotdata = pd.DataFrame(ldb["Year"].value_counts(sort=False))
plotdata.columns = ["Aantal"]
print(plotdata)

plt.bar(plotdata.index, plotdata.Aantal)
plt.ylabel("Aantal lanceringen")
plt.xlabel("Jaar")
plt.show()

################################################################################
## Vehicle stuff
################################################################################

vehicfile = "launchvehicles.txt"
vdb = pd.read_fwf(vehicfile, skiprows=65) ## vehicle database  = vdb
vhead = pd.read_fwf(vehicfile, nrows=64)

colname = "#TEXT/DTF-FIXED"
colnames = []

for row in vhead[colname]:
    if row[0:5] == "TTYPE":
        newname = row[11:]
        newname = newname[0:-1]
        colnames.append(newname)


print("Kolommen in vdb: " + str(len(vdb.columns)))
print("Colnames: " + str(len(colnames)))



