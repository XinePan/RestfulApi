import requests
import json

class Tokendler(object):
    def __init__(self):
        headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                   'Accept-Encoding': 'gzip, deflate, compress',
                   'Accept-Language': 'en-us;q=0.5,en;q=0.3',
                   'Cache-Control': 'max-age=0',
                   'Connection': 'keep-alive',
                   'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
        self.__session = requests.session()
        self.__session.headers.update(headers)

    def get_token(self,url,payload):
        js = json.dumps(payload)
        self.__session.post(url,json=js).json()





if __name__=="__main__":
    t = Tokendler()
    t.get_token()
