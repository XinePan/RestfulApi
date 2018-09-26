#_*_ coding:utf-8 _*_
import requests
import json

class Tokendler(object):
    def __init__(self):
        self.__init_headers()
        requests.packages.urllib3.disable_warnings()
        self.__cookie = {}

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
        k,v = self.fuzzyfinder_dict('token', r)
        self.session.headers.update({'X-ACCESS-TOKEN':v})

    def set_parmar(self, key, value):
        self.__cookie[key] = value

    def del_parmar(self, key):
        try:
            k, v = self.fuzzyfinder_dict(key, self.__cookie)
            if k != None:
                self.__cookie.pop(k)
            else:
                self.__cookie.pop(key)
        except Exception as err:
            print("Cannot delete %s"%key)

    def get_parmar(self,key):
        try:
            k,v = self.fuzzyfinder_dict(key, self.__cookie)
            if k != None:
                return self.__cookie[k]
            else:
                return self.__cookie[k]
        except  Exception as err:
            return None

    def fuzzyfinder_dict(self, key, value):
        lists = [value]
        while lists != []:
            for li in lists:
                if isinstance(li,dict):
                    r = self.fuzzyfinder_list(key, list(li.keys()))
                    if len(r) > 0:
                        return r[0], li[r[0]]
                    lists += [v for k,v in li.items()]
                lists.remove(li)
        return None,None

    def fuzzyfinder_list(self,user_input, collection):
        import re
        suggestions = []
        pattern = '.*?'.join(user_input)  # Converts 'djm' to 'd.*?j.*?m'
        regex = re.compile(pattern)  # Compiles a regex.
        for item in collection:
            match = regex.search(item)  # Checks if the current item matches the regex.
            if match:
                suggestions.append((len(match.group()), match.start(), item))
        return [x for _, _, x in sorted(suggestions)]





if __name__=="__main__":
    url = 'https://172.31.1.206:18002/controller/v2/tokens'
    payload = {
  "userName":"vxlan2@huawei.com",
  "password":"Huawei@123"
}

    t = Tokendler()
    t.get_token(url, payload)

