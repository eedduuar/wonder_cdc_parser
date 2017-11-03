import requests
class Http_client():

    def get(self,url):
        return requests.get(url).text