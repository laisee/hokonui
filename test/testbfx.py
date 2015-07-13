import json
from exchanges.bitfinex import Bitfinex as bfx 

print 'Ask   ', bfx.get_current_ask()
print 'Bid   ', bfx.get_current_bid()
print 'Price ', bfx.get_current_price()
