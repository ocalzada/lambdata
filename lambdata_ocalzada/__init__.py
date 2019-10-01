"""
lambdata - a collection of data science helper functions
"""
import pandas as pd
import requests
import json

df = pd.read_csv('path to file')

# extract zips
df['zip'] = df['Full Address'].apply(lambda x: x[-5:])

# function to get city and state
def get_city_state(zip):
    url = 'http://ziptasticapi.com/{}'.format(zip)
    response = requests.get(url)
    adress_info = json.loads(response.content)
    return adress_info['state'], adress_info['city']

# add state_city as tuple to your df
df['state_city'] = df['zip'].apply(lambda x: get_city_state(x))

# split tuple into city and state
df[['state', 'city']] = df['state_city'].apply(pd.Series)