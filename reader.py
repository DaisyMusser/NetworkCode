import pandas as pd

# read into df
df = pd.read_csv('./struct_data/csv/arrests.csv')

# A 2d list of ids for folks with dup entries
duplicates = []

# add a name column without middle names
df['simple_name'] = df['person_name'].str.replace(r' .* ', ' ', regex=True)

# found one duplicate! Antoine [thomas] martin
'''
duplicates = df[df['simple_name'].duplicated(keep=False)]
print(duplicates)
'''
