import time
from hokonui.exchanges.base import Exchange
from hokonui.models.ticker import Ticker
from hokonui.utils.helpers import apply_format, apply_format_level

class BTCE(Exchange):

    TICKER_URL = 'https://btc-e.com/api/3/ticker/btc_%s'
    ORDER_BOOK_URL = 'https://btc-e.com/api/3/depth/btc_%s'
    NAME = 'BTCE'

    @classmethod
    def _current_price_extractor(cls, data):
        return apply_format(data["btc_usd"].get('last'))

    @classmethod
    def _current_bid_extractor(cls, data):
        return apply_format(data["btc_usd"].get('buy'))

    @classmethod
    def _current_ask_extractor(cls, data):
        return apply_format(data["btc_usd"].get('sell'))

    @classmethod
    def _current_ticker_extractor(cls, data):
        return Ticker('USD',apply_format(data["btc_usd"].get('buy')), apply_format(data["btc_usd"].get('sell'))).toJSON()

    @classmethod
    def _current_orders_extractor(cls,data,max_qty=3):
        orders ={}
        bids  = {}
        asks  = {}
        buyMax = 0
        sellMax = 0
        data_uri = "btc_%s" % 'usd' 
        for level in data[data_uri]["bids"]:
            if buyMax > max_qty:
                pass
            else:
                asks[apply_format_level(level[0])] = "{:.8f}".format(float(level[1]))
            buyMax = buyMax + float(level[1])

        for level in data[data_uri]["asks"]:
            if sellMax > max_qty:
                pass
            else:
                bids[apply_format_level(level[0])] = "{:.8f}".format(float(level[1]))
            sellMax = sellMax + float(level[1])
 
        orders["source"] = "BTCE"
        orders["bids"] = bids
        orders["asks"] = asks
        orders["timestamp"] = str(int(time.time()))
        return orders
