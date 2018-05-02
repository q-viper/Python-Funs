import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


record = pd.read_csv('Carbon dioxide emissions in Nepal.csv')
record = pd.DataFrame(record)
record = record.as_matrix()
x = np.array(record[1:-3,0])
y = np.array(record[1:-3,2])
Sxy = 0
Ssx = 0
X = []
Y = []
n = 0

while n < len(x):
    X.append(float(x[n]))
    Y.append(float(y[n]))
    Sxy = float(x[n]) * float(y[n]) + Sxy
    Ssx = float(x[n]) ** 2 + Ssx
    n+=1

b = (n * Sxy - sum(X) * sum(Y)) /(n* Ssx - sum(X) ** 2)   
a = (sum(Y) - b * sum(X)) / n

#x = float(input('Y = a + bX --- x =?'))
#y = a + b * x
#print(y)
A = []
B = []
for year in range(1960, 2010):
    A.append(year)
    em = a + b * year
    B.append(em)

plt.plot(A,B, label ='original', c='#FF4500')

plt.plot(X,Y, label='new')
plt.show()



