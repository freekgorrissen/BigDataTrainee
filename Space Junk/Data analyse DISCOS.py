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
from numpy.polynomial import polynomial as P
from sklearn.linear_model import LinearRegression as LR
import scipy as sp
from sklearn.metrics import r2_score

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

df = pd.read_csv("C:/Users/Julian/Documents/Traineeship Projecten/Eindproject/Big Data/local repos/BigDataTrainee/Space Junk/DISCOS clean.txt")

def Count_launches():
    x = df.groupby("cosparId").size()
    x = x.drop("one")
    return x

def Kessler_density():
    aleo = 1000 ##average low earth orbit height in km(from earth mean radius)
    emr = 6371  ##earth mean radius in km
    saleo = 4 * 3.1415926 * (aleo+emr*1000)**2 ##surface area of low earth orbit at 1000 km

    data = df.xsectavg
    count_avg = []
    for value in data:
        if value == " None":
            continue
        elif pd.isnull(value) == True:
            continue
        else:
            floaty = float(value)
            count_avg.append(floaty)
    data = pd.DataFrame(count_avg)

    xsect_avg = data.values.mean()
    xsect_std = data.values.std()
    xsect_sum = data.values.sum()
    print(xsect_sum)
    kessler_critical_number = xsect_sum/saleo

    return xsect_avg, xsect_std, kessler_critical_number

def Create_kessler_plot():
    y = Count_launches().cumsum()
    x = []
    for index in y.index:
        x.append(int(index))
    x_old = x

    x = np.array(x).reshape(-1,1)
    plt.plot(x,y.values, label="DISCOS Database")
    plt.xlabel("Jaar")
    plt.ylabel("Aantal objecten")
    plt.title("Aantal objecten in de ruimte (cumulatief)")
    model = LR()
    model.fit(x, y.values)
    x_trend = np.array(range(1957,2051,1))
    y_trend = model.intercept_+model.coef_*x_trend
    #print(model.intercept_, model.coef_)
    plt.plot(x_trend, y_trend, label="Lineaire fit")

##    for i in range(1,6):                                                          Do polynomial fits and determine R**2 fits
##        exp_model = np.poly1d(np.polyfit(x_old, y.values, i))
##        plt.plot(x_trend, exp_model(x_trend), label = "Degrees:" +str(i))
##        print(r2_score(y.values, exp_model(x_old)))
##    print(r2_score(y.values, model.intercept_+model.coef_*x_old))

    plt.legend()
    plt.show()

def Object_info():
    objects_per_class = df.groupby("objectClass").size()
    object_amount_list = [0, 0]
    for key in df.objectClass:
        if key == " Payload":
            object_amount_list[0]+=1
        else:
            object_amount_list[1]+=1
    return objects_per_class, object_amount_list

def Payload_bar():
    y = Object_info()
    title_list = ["Payload","Junk"]
    plt.bar(title_list, y[1])
    plt.ylabel("Aantal objecten")
    plt.title("Staafgrafiek van junk versus functionele payloads in de ruimte.")
    plt.text(0, 6047, str(6047), ha = "center")
    plt.text(1, 23444, str(23444), ha = "center")
    plt.show()

##Payload_bar()
Create_kessler_plot()
##print(Count_launches())
##print(Kessler_density()[0:3])

