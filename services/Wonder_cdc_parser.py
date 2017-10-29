import pandas as pd
import requests
import io

class Wonder_cbc_parser():

    def getWeeks(self):

        weeks = []

        # accordint to web site, all yerar have 53 weeks
        for i in range(1, 54):
            weeks.append(str(i).zfill(2))

        return weeks

    def weekly_data(self,base_url, year, week):
        url = base_url % (year, week)
        print url
        text = requests.get(url).text
        text = text.replace('-', '0')
        df= pd.read_csv(io.StringIO(text), sep='\t', header=None, skiprows=17, skipfooter=21,engine='python')
        df['year'] = year
        df['week'] = week
        return df

    def weekly_job(self,base_url, start_year, end_year):
        years = range(start_year, end_year)
        weeks = self.getWeeks()
        dfs = []
        for year in years:
            for week in weeks[0:2]:
                df = self.weekly_data(base_url, year, week)
                dfs.append(df)

        full_df = pd.concat(dfs, axis=0, ignore_index=True)
        #TODO:remove last week
        return full_df

    # the five column contains the Cumulative year-to-date counts.
    # th ezero column contain the region.

    def yearly_job(self,base_url, start_year, end_year):
        years = range(start_year+1, end_year-1)
        dfs = []
        for year in years:
            df = self.weekly_data(base_url, year, 1)
            df = df.iloc[:,[0,5]]
            dfs.append(df)

        full_df = pd.concat(dfs, axis=0, ignore_index=True)
        return full_df
