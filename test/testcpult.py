import json
from exchanges.coinapult import Coinapult as cplt 

print 'Ask   ', cplt.get_current_ask()
print 'Bid   ', cplt.get_current_bid()
print 'Price ', cplt.get_current_price()
