import pandas as pd
from geopy.geocoders import Nominatim
import numpy as np
import csv

# import earthquake_data_all.csv
data_frame = pd.read_csv('data_filtered.csv')
columns = data_frame.columns
# turn data into a numpy array
data = data_frame.to_numpy()

# column 14th is the column that has the place
# find the 60 places that appears the most
places = {}
for i in range(len(data)):
    print(1, i)
    if data[i][14] in places:
        places[data[i][14]] += 1
    else:
        places[data[i][14]] = 1

# sort the dictionary
places = sorted(places.items(), key=lambda x: x[1], reverse=True)

# get the top 60 places
top60 = []
for i in range(60):
    top60.append(places[i][0])

# print(top60)
# put them into a csv file with the columns
counter = 0
output = open('top60.csv', 'a', newline='')
writer = csv.writer(output)
writer.writerow(columns)
for i in range(len(data)):
    # print(2, i)
    place = data[i][14]
    if place in top60:
        print(counter, data[i][14])
        counter+=1
        writer.writerow(data[i])