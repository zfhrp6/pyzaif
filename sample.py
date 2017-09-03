import zaif_private as zp
import zaif
import yaml
import time

key_pair = yaml.load(open('key.yaml'))

# get my current information
my_info = zp.get_info()
print(my_info)
time.sleep(0.1)

# get last trade price
last_price = zaif.last_price('btc_jpy')
time.sleep(0.1)

# get my trade history
print(zp.trade_history())
time.sleep(0.1)


def harf_int(x):
    ''' minimum BTC/JPY order unit is 5 '''
    return int(x / 2) if (x / 2) % 5 == 0 else int(x / 2 - 2.5)


def envalid_amount(fund, price):
    ''' amount set to full of deposit JPY '''
    return (fund / price) - (fund / price) % 0.0001

# buy-order BTC with JPY at a harf of last price
print(envalid_amount(my_info['return']['funds']['jpy'], harf_int(last_price['last_price'])))
trade_return = zp.trade(currency_pair='btc_jpy',
                        action='bid',
                        price=int(last_price['last_price']),
                        amount=0.0001)
print(trade_return)
time.sleep(0.1)

# get information of active orders
active_orders_return = zp.active_orders()
print(active_orders_return)
time.sleep(0.1)

# get deposit history
deposit_history_return = zp.deposit_history(currency='jpy')
print(deposit_history_return)
