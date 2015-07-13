import json
from exchanges.huobi import Huobi as hbi 

print 'Ask   ', hbi.get_current_ask()
print 'Bid   ', hbi.get_current_bid()
print 'Price ', hbi.get_current_price()
