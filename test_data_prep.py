# test_data_prep.py

from utils.data_prep import load_location_text

df = load_location_text()
print(df.head())