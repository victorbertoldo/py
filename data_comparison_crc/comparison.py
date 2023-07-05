import pandas as pd
from df_crc import DataFrameCRC

# Read in the two dataframes
df1 = pd.read_csv('teste1.csv')
df2 = pd.read_csv('teste2.csv')

# Create instances of the DataFrameCRC class
df_crc1 = DataFrameCRC(df1)
df_crc2 = DataFrameCRC(df2)

# Calculate the CRC values for each dataframe
crc1 = df_crc1.calculate_crc()
crc2 = df_crc2.calculate_crc()

# Compare the CRC values
if crc1 == crc2:
    print('CRC values match!')
else:
    print('CRC values do not match.')
