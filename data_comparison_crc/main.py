from df_crc import DataFrameCRC
from dataframe_helpers import find_non_serializable_values
import pandas as pd

# Load the dataframes from your source
df1 = pd.read_csv('teste1.csv')
df2 = pd.read_csv('teste2.csv')

# Check if there is any non-serializable data in the dataframes
non_serializable_df1 = find_non_serializable_values(df1)
non_serializable_df2 = find_non_serializable_values(df2)

if not non_serializable_df1.empty:
    print('Non-serializable data found in dataframe 1:')
    print(non_serializable_df1)
if not non_serializable_df2.empty:
    print('Non-serializable data found in dataframe 2:')
    print(non_serializable_df2)

# Calculate the CRC values for the dataframes
df_crc1 = DataFrameCRC(df1)
df_crc2 = DataFrameCRC(df2)

crc1 = df_crc1.calculate_crc()
crc2 = df_crc2.calculate_crc()

# Compare the CRC values
if crc1 == crc2:
    print('Dataframes are identical.')
else:
    print('Dataframes are different.')
