import json
from exchanges.bitstamp import Bitstamp as bts 

print 'Ask   ', bts.get_current_ask()
print 'Bid   ', bts.get_current_bid()
print 'Price ', bts.get_current_price()
