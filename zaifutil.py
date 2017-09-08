# coding: utf-8

# import time
import urllib.request
import urllib.parse
# import hmac
# import hashlib
import json


def get_json(url):
    return json.loads(urllib.request.urlopen(url).read().decode('utf-8'))
