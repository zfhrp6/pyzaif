# coding: utf-8

# import time
import urllib.request
import urllib.parse
# import hmac
# import hashlib
import json


def get_json(url):
    return json.loads(urllib.request.urlopen(url).read().decode('utf-8'))


def public_api(func):
    def decorated(*args, **kwargs):
        if 'from_' in kwargs.keys():
            kwargs['from'] = kwargs['from_']
            del(kwargs['from_'])
        if len(args) > 0:
            param = args[0]
        elif len(kwargs) > 0:
            param = list(kwargs.values())[0]
        else:
            raise Exception()
        print(func.__name__, param)
        return get_json(PUBLIC_ENDPOINT + '/' + func.__name__ + '/' + param)
    return decorated

