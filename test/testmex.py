import json
from exchanges.mexbtc import MexBtc as mex 

print 'Ask   ', mex.get_current_ask()
print 'Bid   ', mex.get_current_bid()
print 'Price ', mex.get_current_price()
