import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import seaborn as s


earthquack=pd.read_csv("C:/Users/DataScienceLab/month.csv")

earthquack.head()

s.countplot(x='status' , data=earthquack)

earthquack.status.unique()

earthquack.describe().transpose()


# --- Process Data ---
data_file = open('datasets/earthquake_data.csv')
 
lats, lons = [], []
magnitudes = []
for index, line in enumerate(data_file.readlines()):
    if index > 0:
        lats.append(float(line.split(',')[6]))
        lons.append(float(line.split(',')[7]))
        magnitudes.append(float(line.split(',')[8]))

# --- Build Map ---

map = Basemap(projection='robin', resolution = 'l', area_thresh = 1000.0 , lat_0=0, lon_0=-130)
map.drawcoastlines()
map.drawcountries()
map.fillcontinents(color = 'gray')
map.drawmapboundary()
map.drawmeridians(np.arange(0, 360, 30))
map.drawparallels(np.arange(-90, 90, 30))

min_marker_size = 4
for lon, lat, mag in zip(lons, lats, magnitudes):
    x,y = map(lon, lat)
    msize = mag * min_marker_size
    map.plot(x, y, 'ro', markersize=msize)

plt.show()
