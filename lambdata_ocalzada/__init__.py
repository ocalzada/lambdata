"""
lambdata - a collection of data science helper functions
"""
import pandas as pd

df = pd.DataFrame({'Owner City State Zip': ["Los Angeles, CA 90015"]})

regex = r'(?P<City>[^,]+)\s*,\s*(?P<State>[^\s]+)\s+(?P<Zip>\S+)'
df['Owner City State Zip'].str.extract(regex)