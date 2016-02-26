# coding: utf-8

import time
import urllib.request
import urllib.parse
import hmac
import hashlib



def make_nonce():
    return str(round(time.time()*100)%1000000007).encode('utf-8')

def make_header(post_param):
    digester = hmac.new(api_secret.encode('utf-8'), digestmod = hashlib.sha512)
    digester.update(post_param)
    return {'Key': api_key,
            'Sign': digester.hexdigest()}


def private_api(func):
    def decorated(*args, **kwargs):
        if 'from_' in kwargs.keys():
            kwargs['from'] = kwargs['from_']
            del(kwargs['from_'])
        post_param = kwargs
        post_param['method'] = func.__name__
        post_param['nonce'] = make_nonce()
        post_param = urllib.parse.urlencode(post_param).encode('utf-8')
        headers = make_header(post_param)
        req = urllib.request.Request(PRIVATE_ENDPOINT, post_param, headers)
        response = urllib.request.urlopen(req)
        return json.loads(response.read().decode('utf-8'))
    return decorated