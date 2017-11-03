import requests
from scrapy.selector import Selector

class Scrapp_service():
    def __init__(self):
        self.name = "last_week"
        self.start_url = 'https://wonder.cdc.gov/mmwr/mmwrmorb.asp'

    def get_current_week(self):
        req = requests.get(url=self.start_url)
        text = req.text
        table = Selector(text=text).xpath("//*[@id = 'list1']")
        text = table.xpath('.//b/text()')[0].extract()
        return text.split(' ')[9].replace(',', '')