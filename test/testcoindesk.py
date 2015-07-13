import json
from exchanges.coindesk import CoinDesk as coin 

print 'Current Price          ', coin.get_current_price()
print 'Past Price @ 01-Dec-14 ', coin.get_past_price('2015-07-05')
