import pandas as pd
from geopy.geocoders import Nominatim
import numpy as np
import csv
# initialize Nominatim API
geolocator = Nominatim(user_agent="geoapiExercises")

# import earthquake_data_all.csv
data_frame = pd.read_csv('data_newPlace_complete.csv')
columns = data_frame.columns

counter = 0
# turn data into a numpy array
data = data_frame.to_numpy()

output = open('data_filtered.csv', 'a', newline='')
writer = csv.writer(output)

start = 0
end = len(data)

while start < end:
    print(start)
    if data[start][14] != "None":
        writer.writerow(data[start])
    start+=1
# print(len(data))

# if data[2][14] == "None":
#     # remove that row
#     print("here")
#     data = np.delete(data, 2, 0)
# print(data[2][14])



# # write data to csv
# df = pd.DataFrame(data,columns=columns)
# df.to_csv('data_filtered.csv', index=False)