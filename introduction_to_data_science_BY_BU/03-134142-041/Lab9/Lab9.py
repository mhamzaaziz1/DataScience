import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
df = pd.read_csv("Retrosheet.csv")
#print (df)
nplistDate= np.array(df['date'].values.tolist())
nplistDay= np.array(df['day'].values.tolist())
nplistHome= np.array(df['home'].values.tolist())
nplistAway= np.array(df['away'].values.tolist())
nplistHScore= np.array(df['homeScore'].values.tolist())
nplistAScore= np.array(df['awayScore'].values.tolist())
nplistAttendance= np.array(df['attendance'].values.tolist())
dfnew= pd.DataFrame({'date': nplistDate, 'day': nplistDay, 'home': nplistHome, 'away': nplistAway, 'homeScore': nplistHScore, 'awayScore': nplistAScore, 'attendance': nplistAttendance}, dtype=None)
#print (dfnew)
#print(dfnew.describe())         #for information
#print(dfnew.dtypes)             #for data type 
plt.plot(nplistDate,nplistDate,'o')
plt.plot(nplistDate,nplistDay)
