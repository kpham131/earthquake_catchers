import pandas as pd
from geopy.geocoders import Nominatim
import numpy as np
import csv
# initialize Nominatim API
geolocator = Nominatim(user_agent="geoapiExercises")

# import earthquake_data_all.csv
data_frame = pd.read_csv('earthquake_data_all.csv')
data_frame.rename(columns={'Unnamed: 0': 'id'}, inplace=True)
# columns = data_frame.columns
# columns.to_series().to_csv("data_newPlace.csv", index=False)
output = open('data_newPlace.csv', 'a', newline='')
writer = csv.writer(output)

# turn data into a numpy array
data = data_frame.to_numpy()

# counters for each type of place
countyCounter = 0
emptycounter = 0
cityCounter = 0
townVillageCounter=0
results = np.array([])
start = 0
end = 613788
while start < end:
    print(start)
    error = 1
    while(error == 1):
        try:
            location = geolocator.reverse(str(data[start][2])+","+str(data[start][3]))
            error = 0
        except:
            error = 1
    
    # location = geolocator.reverse(str(data[start][2])+","+str(data[start][3]))
    result = ''
    if location != None:
        address = location.raw['address']
        city = address.get('city', '')
        county = address.get('county', '')
        town = address.get('town', '')
        village = address.get('village', '')
        
        if city != '':
            # have city
            result = city
            cityCounter+=1

        elif county != '':
            # have county
            result = county
            countyCounter+=1

        elif town != '':
            # have town
            result = town
            townVillageCounter+=1

        elif village != '':
            # have village  
            result = village
            townVillageCounter+=1
            
        else:
            # have nothing
            result = 'None'
            emptycounter+=1
            
    else:
        emptycounter+=1
        result = 'None'

    # update column place
    data[start][14] = result
    writer.writerow(data[start])
    start += 1


# write data to csv
# df = pd.DataFrame(data, columns=columns)
# df.to_csv('data_newPlace.csv', index=False)