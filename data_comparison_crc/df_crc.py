class DataFrameCRC:
    def __init__(self, df):
        self.df = df
    
    def _format_row(self, row):
        return ''.join([str(row[col]) for col in self.df.columns])
    
    def calculate_crc(self):
        crc = 0
        for index, row in self.df.iterrows():
            formatted_row = self._format_row(row)
            crc = crc ^ int(formatted_row.encode().hex(), 16)
        return crc
