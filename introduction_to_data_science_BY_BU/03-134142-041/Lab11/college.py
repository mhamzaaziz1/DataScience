import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as s

df = pd.read_csv("C:/Users/M.Shahrukh/Lab/College.csv")

print df

df.rename(columns={'Unnamed: 0':'Univerities'}, inplace=True)

df.head

df=df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1)

df.head()

df.describe()

s.pairplot(df, hue=None, hue_order=None, palette=None, vars=None, x_vars=None, y_vars=None, kind='scatter', diag_kind='hist', markers=None, size=2.5, aspect=1, dropna=True, plot_kws=None, diag_kws=None, grid_kws=None)


df.boxplot(column="Outstate", by="Private", ax=None, fontsize=12 , rot=0, grid=True, figsize=(5,6), layout=None, return_type=None)

plt.show()


fig, ax = plt.subplots()
pos = np.array(range(len(treatments))) + 1
bp = ax.boxplot(treatments, sym='k+', positions=pos,
                notch=1, bootstrap=5000,
                usermedians=medians,
                conf_intervals=conf_intervals)

ax.set_xlabel('outstate')
ax.set_ylabel('private')
plt.setp(bp['whiskers'], color='k', linestyle='-')
plt.setp(bp['fliers'], markersize=3.0)
plt.show()
