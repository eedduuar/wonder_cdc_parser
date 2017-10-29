
import sys

from services.Wonder_cdc_parser import Wonder_cbc_parser
from util.parse_params import Params

reload(sys)
sys.setdefaultencoding('UTF-8')

from datetime import  datetime



if __name__ == '__main__':


    parser = Wonder_cbc_parser()

    params = Params("get Morbidity and Mortality Weekly Report (MMWR) from : wonder.cdc.gov")
    current_year = now = datetime.now().year
    current_week = 23  # TODO: calculate current week

    base_url = params.base_url()
    output_file = params.output()
    mode = params.mode()
    if mode == 'weekly':

        df =  parser.weekly_job(base_url, 1996, current_year)
        df.to_csv(output_file, index=False,header=False)
    if mode == 'last_week':

        df = parser.weekly_data(base_url, current_year, current_week)
        df.to_csv(output_file, index=False,header=False)

    if mode == 'yearly':
        df = parser.yearly_job(base_url, current_year, current_week)
        df.to_csv(output_file, index=False,header=False)
