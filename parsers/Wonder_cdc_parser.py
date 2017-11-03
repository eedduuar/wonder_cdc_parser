import pandas as pd
import io


class Wonder_cbc_parser():
    def __init__(self, http_client):
        self.region_length = 67
        self.http_client = http_client

    def calculate_skipfooter(self,text,first_row):

        lines = text.split('\n')
        return len(lines) - first_row - self.region_length-1


    def calculate_first_row(self, text):

        lines = text.split('\n')

        for i in range(0,len(lines)):
            if 'tab delimited data' in lines[i]:
                return i+1

        return 0


    def weekly_data(self, base_url, year, week, column_value):
        url = base_url % (year, week)
        print url
        text = self.http_client.get(url)
        text = text.replace('-', '0')

        if 'No records found' in text:
            raise Exception('empty data for:' + str(year) + '-' + str(week))

        sr = self.calculate_first_row(text)
        sk = self.calculate_skipfooter(text,sr)

        df = pd.read_csv(io.StringIO(text), sep='\t', header=None,
                         skiprows=sr, skipfooter=sk, engine='python',na_values=['N','U','NN','NP'])

        df = df.iloc[:, [0, column_value]]
        df['year'] = year
        df['week'] = week
        df.columns.values[0] = 'region'
        df.columns.values[1] = 'current_week'




        return df


