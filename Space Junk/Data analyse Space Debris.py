#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Julian
#
# Created:     14/09/2021
# Copyright:   (c) Julian 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pandas as pd

dataset = pd.read_csv('C:/Users/Julian/Documents/Traineeship Projecten/Eindproject/TLE 5 archive from space track.txt', header = None)
df = dataset.values.tolist()
#print(df[0:3])
sanitized_list = []
names = []
for i in range(0,30,3):
    names.append(df[i])
    sanitized_list.append(df[i+1] + df[i+2])

#print(sanitized_list[0])

for i in range(len(sanitized_list)):
    sanitized_list[i] = " ".join(sanitized_list[i])
    sanitized_list[i] = sanitized_list[i].split()

san_df = pd.DataFrame(sanitized_list)

columns = [""]

print(names)
print(san_df)