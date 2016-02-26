import zaif_private
import yaml

key_pair = yaml.load(open('key.yaml.private'))
zp = zaif_private # .Zaif(key_pair['api_key'], key_pair['api_secret'])

print(zp.get_info())
print(zp.trade_history())
print(zp.active_orders())
print(zp.trade())
print(zp.deposit_history(currency='jpy'))
