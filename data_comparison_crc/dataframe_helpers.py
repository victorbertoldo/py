import json
import pandas as pd

def find_non_serializable_values(df):
    non_serializable = []
    for index, row in df.iterrows():
        for column, value in row.items():
            try:
                json.dumps(value)
            except TypeError:
                non_serializable.append((index, column, value))
    return pd.DataFrame(non_serializable, columns=['Index', 'Column', 'Value'])
