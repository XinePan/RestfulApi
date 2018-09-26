import requests
import json

class Tokendler(object):
    def __init__(self):
        self.__init_headers()
        requests.packages.urllib3.disable_warnings()

    def __init_headers(self):
        headers = {'Accept':'application/json',
                        'Content-Type':'application/json',
                        'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
        self.session = requests.session()
        self.session.headers.clear()
        self.session.headers.update(headers)
        self.session.verify = False

    def get_token(self,url,payload):
        js = json.dumps(payload)
        self.__session.post(url,json=js).json()





if __name__=="__main__":
    t = Tokendler()
    t.get_token()
