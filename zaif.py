# coding: utf-8

import urllib.request

from zaifutil import get_json

PUBLIC_ENDPOINT = 'https://api.zaif.jp/api/1'

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

@public_api
def currencies(currency='all'):
    pass


@public_api
def currency_pairs(currency_pair='all'):
    pass


@public_api
def last_price(currency_pair='btc_jpy'):
    pass


@public_api
def ticker(currency_pair='btc_jpy'):
    pass


@public_api
def trades(currency_pair='btc_jpy'):
    pass


@public_api
def depth(currency_pair='btc_jpy'):
    pass


'''
    last_price : 終値を得る
        btc_jpy – https://api.zaif.jp/api/1/last_price/btc_jpy
        mona_jpy – https://api.zaif.jp/api/1/last_price/mona_jpy
        mona_btc – https://api.zaif.jp/api/1/last_price/mona_btc
    ticker : ティッカー
        btc_jpy – https://api.zaif.jp/api/1/ticker/btc_jpy
        mona_jpy – https://api.zaif.jp/api/1/ticker/mona_jpy
        mona_btc – https://api.zaif.jp/api/1/ticker/mona_btc
        JSONディクショナリを返します:
            last – last price : 終値
            high – last 24 hours price high : 過去24時間の高値
            low – last 24 hours price low : 過去24時間の安値
            vwap – last 24 hours volume weighted average price : 過去24時間の加重平均
            volume – last 24 hours volume : 過去24時間の出来高
            bid – highest buy order : 買気配値
            ask – lowest sell order : 売気配値
    trades : 全ての取引履歴
        btc_jpy – https://api.zaif.jp/api/1/trades/btc_jpy
        mona_jpy – https://api.zaif.jp/api/1/trades/mona_jpy
        mona_btc – https://api.zaif.jp/api/1/trades/mona_btc
    depth : 板情報
        btc_jpy – https://api.zaif.jp/api/1/depth/btc_jpy
        mona_jpy – https://api.zaif.jp/api/1/depth/mona_jpy
        mona_btc – https://api.zaif.jp/api/1/depth/mona_btc
'''
