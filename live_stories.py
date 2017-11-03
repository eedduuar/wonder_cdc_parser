import sys

import pandas as pd

from parsers.Wonder_cdc_parser import Wonder_cbc_parser
from services.Hepatitis_Data_Service import Hepatitis_Data_Service
from services.Scrapp_service import Scrapp_service
from util.parse_params import Params
from util.http_client import Http_client


reload(sys)
sys.setdefaultencoding('UTF-8')

from datetime import  datetime



if __name__ == '__main__':

    http_client = Http_client()
    parser = Wonder_cbc_parser(http_client)
    data_service = Hepatitis_Data_Service(parser)


    params = Params("get Morbidity and Mortality Weekly Report (MMWR) from : wonder.cdc.gov")
    current_year = now = datetime.now().year

    scrap = Scrapp_service()
    current_week = scrap.get_current_week()
    print ("current week:"+ current_week)

    base_url = params.base_url()
    output_file = params.output()
    mode = params.mode()


    if mode not in [ 'weekly','last_week','yearly','test']:
        print ("invalid mode")
        exit(1)

    if mode == 'weekly':
        df1 = data_service.get_data_legacy_format(base_url, 2016, 2017)
        df2 =  data_service.get_data_current_format(base_url, 2017, current_year + 1, current_week)

        df = pd.concat([df1,df2],axis=0,ignore_index=True)
        df.to_csv(output_file, index=False,header=True)

    if mode == 'last_week':

        df = data_service.get_data_weekly(base_url, current_year, current_week)
        df.to_csv(output_file, index=False,header=True)

    if mode == 'yearly':
        input_file= params.input_file()
        df = data_service.get_data_yearly(input_file)
        df.to_csv(output_file, index=False,header=True)


    if mode == 'test':

        df = data_service.get_data_weekly(base_url, 2016, '20')
        df.to_csv(output_file, index=False,header=True)

    print ("file generated:"+output_file)
