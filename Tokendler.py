#_*_ coding:utf-8 _*_
from __future__ import print_function
import requests
import json

class Tokendler(object):
    def __init__(self):
        self.__init_headers()
        requests.packages.urllib3.disable_warnings()
        self.__storage = {}

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
        result = self.fuzzyfinder_dict('token', r)
        print('the token is ', result[0][-1])
        self.session.headers.update({'X-ACCESS-TOKEN':result[0][-1]})
        return  r

    def set_parmar(self, indict):
        self.__storage.update(indict)

    def del_parmar(self, key):
        try:
            result = self.fuzzyfinder_dict(key, self.__storage)

            if k != None:
                self.__storage.pop(k)
            else:
                self.__storage.pop(key)
        except Exception as err:
            print("Cannot delete %s"%key)

    def get_parmar(self,key):
        try:
            k,v = self.fuzzyfinder_dict(key, self.__storage)
            if k != None:
                return self.__storage[k]
            else:
                return self.__storage[k]
        except  Exception as err:
            return None

    def fuzzyfinder_dict(self, user_input, collection, topN=1):
        import re
        suggestions = []
        pattern = '.*?'.join(user_input)  # Converts 'djm' to 'd.*?j.*?m'
        regex = re.compile(pattern)  # Compiles a regex.
        for item in self.dict_generator(collection):
            match = regex.search('.'.join(item[0:-1]))  # Checks if the current item matches the regex.
            if match:
                suggestions.append((len(match.group()), match.start(), ['.'.join(item[0:-1]), item[-1]]))
        return [x for _, _, x in sorted(suggestions)][0:topN]

    def dict_generator(self,indict, pre=None):
        pre = pre[:] if pre else []
        if isinstance(indict, dict):
            for key, value in indict.items():
                if isinstance(value, dict):
                    if len(value) == 0:
                        yield pre + [key, '{}']
                    else:
                        for d in self.dict_generator(value, pre + [key]):
                            yield d
                elif isinstance(value, list):
                    if len(value) == 0:
                        yield pre + [key, '[]']
                    else:
                        for v in value:
                            for d in self.dict_generator(v, pre + [key]):
                                yield d
                elif isinstance(value, tuple):
                    if len(value) == 0:
                        yield pre + [key, '()']
                    else:
                        for v in value:
                            for d in self.dict_generator(v, pre + [key]):
                                yield d
                else:
                    yield pre + [key, value]
        else:
            yield indict





if __name__=="__main__":
    url = 'https://10.173.12.36:18002/controller/v2/tokens'
    payload = {
  "userName":"api@huawei.com",
  "password":"Huawei@123"
}

    t = Tokendler()
    t.get_token(url, payload)
    siteId = []
    for jtem in range(7,9):
        url = 'https://10.173.12.36:18002/controller/campus/v3/sites'
        payload = {
                    "sites":[
                        {
                            "name":"ppsk%d"%(jtem+8),
                            "description":"site12",
                            "type":[
                                "AP"
                            ]
                        }
                    ]
                }
        r = t.session.post(url, data=json.dumps(payload)).json()
        print(r)
        v = t.fuzzyfinder_dict('id',r)
        siteId.append(v)
        print(v)
        '''
        url = 'https://10.173.12.36:18002/controller/campus/v3/devices'
        for item in range(0,1000):
            payload = {
                        "devices":[
                                    {
                                        "esn":"AA50082935AAAAA%05d"%(item+jtem*1000+6000),
                                        "name":"ap-%d"%(item+jtem*1000+6000),
                                        "siteId":v,
                                        "description": "",
                                        "tags":["12312啊ad_fs-dfd-sfd_","123"]
                                    },
                                    ]
                        }
            r = t.session.post(url, data=json.dumps(payload)).json()
            '''


    url = 'https://10.173.12.36:18002/controller/campus/v1/authconfigservice/accessconfig/1b3c75c2-8827-4fde-baba-83d38b2bfae8/ppsk'
    r = t.session.post(url).json()
    print(r)

