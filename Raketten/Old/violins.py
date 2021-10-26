import matplotlib.pyplot as plt
import random as rd
import pandas as pd

a = []
b = []
for i in range(100):
    a.append(rd.gauss(0, 1))
    b.append(rd.gauss(1, 0.5))

df = pd.DataFrame(a)
df = pd.concat([df, pd.DataFrame(b)], axis=1, ignore_index=True)
print(df)

plt.violinplot(df, showmedians=True)
plt.show()
