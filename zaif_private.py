#!/usr/bin/env python
# coding: utf-8

import urllib.request
import urllib.parse
import json
import time
import hmac
import hashlib
import yaml

PRIVATE_ENDPOINT = 'https://api.zaif.jp/tapi'

post_param = []
_k = yaml.load(open('key.yaml').read())
api_key = _k['api_key']
api_secret = _k['api_secret']


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


def make_header(post_param):
    digester = hmac.new(api_secret.encode('utf-8'), digestmod=hashlib.sha512)
    digester.update(post_param)
    return {'Key': api_key,
            'Sign': digester.hexdigest()}


def make_nonce():
    return str(round(time.time() * 5) % 1000000000).encode('utf-8')


@private_api
def get_info():
    pass


@private_api
def get_info2():
    pass


@private_api
def get_personal_info():
    pass


@private_api
def get_id_info():
    pass


@private_api
def trade_history(from_=0, count=1000, from_id=0, end_id='infinity', order='DESC', since=0, end='infinity', currency_pair=None):
    pass
'''
from    No  この順番のレコードから取得   numerical   0
count   No  取得するレコード数   numerical   1000
from_id No  このトランザクションIDのレコードから取得   numerical   0
end_id  No  このトランザクションIDのレコードまで取得   numerical   infinity
order   No  ソート順    ASC (昇順)もしくは DESC (降順)  DESC
since   No  開始タイムスタンプ   UNIX time   0
end No  終了タイムスタンプ   UNIX time   infinity
currency_pair   No  通貨ペア。指定なしで全ての通貨ペア   (例) btc_jpy 全ペア
'''


@private_api
def active_orders(currency_pair=None):
    pass
'''
currency_pair   No  取得する通貨ペア。指定なしで全ての通貨ペア   (例) btc_jpy 全てのペア
'''


@private_api
def trade(currency_pair, action, price, amount, limit=None):
    pass
'''
currency_pair   Yes 発注する通貨ペア    (例) btc_jpy -
action  Yes 注文の種類   bid もしくは ask    -
price   Yes 指値注文価格  numerical   -
amount  Yes 数量(例: 0.3)  numerical   -
limit   No  リミット注文価格    numerical
'''


@private_api
def cancel_order(order_id):
    pass
'''
order_id    Yes 注文ID（tradeまたはactive_ordersで取得できます）  numerical   -
'''


@private_api
def withdraw(currency, address, amount, opt_fee=None):
    pass
'''
currency    Yes 引き出す通貨  btc もしくは mona   -
address Yes 送信先のアドレス    address string  -
amount  Yes 引き出す金額(例: 0.3)  numerical   -
opt_fee No  採掘者への手数料(例: 0.003)  numerical   -
'''


@private_api
def deposit_history(currency, from_=0, count=0, from_id=0, end_id='infinity', order='DESC', since=0, end='infinity'):
    pass
'''
currency    Yes 通貨。jpy / btc / mona のいずれかを指定    TEXT
from    No  この順番のレコードから取得   numerical   0
count   No  取得するレコード数   numerical   1000
from_id No  この入金IDのレコードから取得 numerical   0
end_id  No  この入金IDのレコードまで取得 numerical   infinity
order   No  ソート順    ASC (昇順)もしくは DESC (降順)  DESC
since   No  開始タイムスタンプ   UNIX time   0
end No  終了タイムスタンプ   UNIX time   infinity
'''


@private_api
def withdraw_history(currency, from_=0, count=1000, from_id=0, end_id='infinity', order='DESC', since=0, end='infinity'):
    pass
'''
currency    Yes 通貨。jpy / btc / mona のいずれかを指定    TEXT
from    No  この順番のレコードから取得   numerical   0
count   No  取得するレコード数   numerical   1000
from_id No  この出金IDのレコードから取得 numerical   0
end_id  No  この出金IDのレコードまで取得 numerical   infinity
order   No  ソート順    ASC (昇順)もしくは DESC (降順)  DESC
since   No  開始タイムスタンプ   UNIX time   0
end No  終了タイムスタンプ   UNIX time   infinity
'''


'''
get_info : 残高などのアカウント情報を取得する
trade_history : 取引履歴を取得する
active_orders : 現在有効な注文一覧を取得する
trade : 取引注文を行う
cancel_order : 注文を取り消す
withdraw : 暗号通貨の出金リクエストを行う
deposit_history : 入金履歴を取得する
withdraw_history : 出金
'''
