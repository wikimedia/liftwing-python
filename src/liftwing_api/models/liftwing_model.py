import requests

class LiftwingModel:
    def __init__(self, base_url):
        self.base_url = base_url
        # this base url will be used across every model

    def request(self, endpoint, method="GET", data=None, headers=None):
        # this method will make a request and return a json response
        #return response.json()
        return ""
