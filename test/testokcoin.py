import json
from exchanges.okcoin import OKCoin as okc 

print 'Price ', okc.get_current_price()
print 'Ask   ', okc.get_current_ask()
print 'Bid   ', okc.get_current_bid()
