import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Carbon dioxide emissions in Nepal.csv')
df = pd.DataFrame(df)
#df = df.drop(df.columns[0], axis=1)

#df = pd.as_matrix(df)
df = df.as_matrix()
df = df[2:-3]

years = []
emissions = []

for everyLine in df:
    years.append(int(everyLine[0]))
    emissions.append(float(everyLine[1]))


#np.linalg.solve(years, emissions)

fig = plt.figure()

ax1 = fig.add_subplot(312)

ax1.plot(years,emissions)

ax2 = fig.add_subplot(313)
ax2.scatter(years, emissions)
plt.xlabel('Years')
plt.ylabel('Emissions in Metrictons.')
plt.show()
