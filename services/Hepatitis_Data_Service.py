import pandas as pd

class Hepatitis_Data_Service():

    def __init__(self, parser):
        self.parser = parser


    def getWeeks(self):
        weeks = []

        # accordint to web site, the max week numner is 53
        for i in range(1, 54):
            weeks.append(str(i).zfill(2))
        return weeks

    # the five column contains the Cumulative year-to-date counts in 2017.
    # the 15th column contains the Cumulative year-to-date counts for legacy years format.
    # th ezero column contain the region.

    def get_value_position(self,year):
        if year == '2017':
            return 5
        else:
            return 15

    def get_data_weekly(self,base_url,year,week):
        return self.parser.weekly_data(base_url, year, week, 1)


    def get_data_legacy_format(self, base_url, start_year, end_year):
        years = range(start_year, end_year)
        weeks = self.getWeeks()
        dfs = []
        for year in years:
            for week in weeks:
                try:
                    df = self.parser.weekly_data(base_url, year, week,11)
                    dfs.append(df)
                except Exception as e :
                    print e
                    continue
        full_df = pd.concat(dfs, axis=0, ignore_index=True)
        return full_df


    def get_data_current_format(self, base_url, start_year, end_year, current_week):
        years = range(start_year, end_year)
        weeks = self.getWeeks()
        dfs = []
        for year in years:
            weeks = [x for x in weeks if x < current_week ]
            for week in weeks:
                try:
                    df = self.parser.weekly_data(base_url, year, week,1)
                    dfs.append(df)
                except Exception as e:
                    print e
                    continue
        full_df = pd.concat(dfs, axis=0, ignore_index=True)
        return full_df





    def get_data_yearly(self, input_file):
        df = pd.read_csv(input_file)
        df = df.groupby(['year']).sum()
        df = df.reset_index()
        return df[['year','current_week']]
