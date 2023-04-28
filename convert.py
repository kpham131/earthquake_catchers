# import necessary libraries
import pandas as pd
import numpy as np

# load earthquake data into a pandas dataframe
data = pd.read_csv('top60.csv')

# print all the unique values in the 'magType' column
print(data['magType'].unique())

# change all the magnitude type to lowercase
data['magType'] = data['magType'].str.lower()

# change mb_lg to mblg
data['magType'] = data['magType'].replace('mb_lg', 'mblg')




# convert all magnitude into ml (local magnitude)
# these are all the magnitude types: 'ml' 'mb' 'md' 'mwc' 'mw' 'mc' 'mh' 'mwr' 'mwb' 'ms' 'ma' 'mblg' 'm' 'mlg' 'mww' 'mlr' 'mwp' 'mlv'
# column 6 is the magnitude type
# column 5 is the magnitude

# create a function to convert magnitude to local magnitude (ML)
def convert_to_ml(row):
    mag_type = row['magType'].lower()
    mag = row['mag']
    if mag_type == 'ml':
        return mag
    elif mag_type == 'ms':
        ml = 1.14 * mag - 0.16
    elif mag_type == 'mb':
        ml = 1.0 * mag + 3.0
    elif mag_type == 'mw' or mag_type == 'mwc' or mag_type == 'mww':
        ml = 0.9 * mag + 0.5
    elif mag_type == 'md' or mag_type == 'mc' or mag_type == 'mh' or mag_type == 'mwr' or mag_type == 'mwb' or mag_type == 'ma' or mag_type == 'mblg' or mag_type == 'mlg' or mag_type == 'mlr' or mag_type == 'mwp' or mag_type == 'mlv' or mag_type == 'm':
        ml = mag
    else:
        ml = None
    return ml

# apply the conversion function to the 'Magnitude Type' and 'Magnitude' columns
data['mag'] = data.apply(convert_to_ml, axis=1)

# drop rows with missing ML values
# data.dropna(subset=['ML'], inplace=True)

# remove magType column
data = data.drop(['magType'], axis=1)

# for the time column, we only want the date without the dashes, we also don't want the time
# column 1 is the time
data['time'] = data['time'].str.replace('-', '')
data['time'] = data['time'].str[:8]

# make a column for year, month, day
data['year'] = data['time'].str[:4]
data['month'] = data['time'].str[4:6]
data['day'] = data['time'].str[6:8]


# save the updated data to a new csv file
data.to_csv('top60_ml.csv', index=False)

