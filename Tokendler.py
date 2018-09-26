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
        r = self.session.post(url, data=json.dumps(payload)).json()
        self.get_parmar(r,'token')

    def get_parmar(self, data, key):
        print(data.keys())



if __name__=="__main__":
    url = 'https://172.31.1.206:18002/controller/v2/tokens'
    payload = {
  "userName":"vxlan2@huawei.com",
  "password":"Huawei@123"
}

    t = Tokendler()
    t.get_token(url, payload)
