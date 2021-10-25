import pandas as pd
import csv
# Data inladen
data = pd.read_csv('C:/Users/roang/PycharmProjects/PS_2021.09.27_05.25.58.csv', skiprows=17, nrows=100)
# print(data.head(n=10))
newData = data
# print(data['pl_name'].dtypes)

# print(data['pl_name'][0])
# print(data['pl_name'][15])
x = 1
while x <= 49:
     if (data['pl_name'][x - 1] == data['pl_name'][x]):
          data.drop(x, inplace=True)
          print("a")

     x += 1
   #  print(x)
   #  if (data['pl_name'][x - 1] == data['pl_name'][x]):
   # if False:
   #       print("inif")
   #       data = data[data.index != x]


# data = data[data.index != 12]


print(data.head(n=30))

# if (data['pl_name'][x] == data['pl_name'][x+1]):
# Print the second value in the `fat` column
