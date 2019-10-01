"""
lambdata - a collection of data science helper functions
"""
import pandas as pd

# dataframe must be in City, State, Zip format

df = pd.DataFrame({'Owner City State Zip': ["Fontana, CA 92336", "Los Angeles, CA 90006", "Salt Lake City, UT 84106", "Brookline, MA 02445"
                                           ]})

# this function splits an address into its constituent City, State, Zip parts & 
# returns a dataframe with each component in a separate column

def split_address(df):
    regex = r'(?P<City>[^,]+)\s*,\s*(?P<State>[^\s]+)\s+(?P<Zip>\S+)'
    return df['Owner City State Zip'].str.extract(regex)