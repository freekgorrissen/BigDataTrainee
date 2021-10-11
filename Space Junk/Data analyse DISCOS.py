#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Julian
#
# Created:     28/09/2021
# Copyright:   (c) Julian 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

##def Create_frame():
##    df = pd.read_csv("C:/Users/Julian/Documents/Traineeship Projecten/Eindproject/DISCOS Data.txt") ##read our data to a dataframe and do cleaning operations...
##    att = df['attributes']
##    att = att.str.split(",", expand = True)
##    att.columns = ["xsectmin", "satno", "diameter", "mass","span", "cosparId", "xsectavg", "name", "vimpelId","objectClass", "depth", "height", "shape", "xsectmax", "width", "final column", "extra", "extra2" ]
##    att=att.drop(columns=["final column", "extra", "extra2"])
##    row_counter = 0
##    for row in att.itertuples():
##        for i in range(1,16):
##            if type(row[i]) == str:
##                value = row[i]
##                value = value.split(":")
##                value[len(value)-1] = value[len(value)-1].replace("'", "")
##                value[len(value)-1] = value[len(value)-1].replace("}", "")
##                value[len(value)-1] = value[len(value)-1].replace("{", "")
##                att.iat[row_counter,i-1] = value[len(value)-1]
##
##        if type(row[6]) == str:
##            y = row[6]
##            #print(y[14:18])
##            y = y[14:18]
##            att.iat[row_counter, 5] = y
##        row_counter+=1
##    return att

##df = Create_frame()
##df.to_csv("C:/Users/Julian/Documents/Traineeship Projecten/Eindproject/DISCOS clean.txt")

df = pd.read_csv("C:/Users/Julian/Documents/Traineeship Projecten/Eindproject/DISCOS clean.txt")

def Count_launches():
    x = df.groupby("cosparId").size()
    x = x.drop("one")
    return x

def Create_plot():
    y = Count_launches().cumsum()
    ax = y.plot.bar()
    plt.show()


Create_plot()
print(Count_launches())

#x = df.groupby("objectClass").size()
#print(x)


