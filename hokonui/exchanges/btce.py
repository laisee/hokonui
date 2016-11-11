import time
from hokonui.exchanges.base import Exchange
from hokonui.models.ticker import Ticker
from hokonui.utils.helpers import apply_format, apply_format_level

class BTCE(Exchange):

    TICKER_URL = 'https://btc-e.com/api/3/ticker/btc_%s'
    ORDER_BOOK_URL = 'https://btc-e.com/api/3/depth/btc_%s'
    NAME = 'BTCE'
    PAIR = "btc_%s" % 'usd'

    @classmethod
    def _current_price_extractor(cls, data):
        return apply_format(data[cls.PAIR].get('last'))

    @classmethod
    def _current_bid_extractor(cls, data):
        return apply_format(data[cls.PAIR].get('buy'))

    @classmethod
    def _current_ask_extractor(cls, data):
        return apply_format(data[cls.PAIR].get('sell'))

    @classmethod
    def _current_ticker_extractor(cls, data):
        return Ticker(cls.CCY_DEFAULT,apply_format(data[cls.PAIR].get('buy')), apply_format(data[cls.PAIR].get('sell'))).toJSON()

    @classmethod
    def _current_orders_extractor(cls,data,max_qty=3):
        orders ={}
        bids  = {}
        asks  = {}
        buyMax = 0
        sellMax = 0
        for level in data[cls.PAIR]["bids"]:
            if buyMax > max_qty:
                pass
            else:
                asks[apply_format_level(level[0])] = "{:.8f}".format(float(level[1]))
            buyMax = buyMax + float(level[1])

        for level in data[cls.PAIR]["asks"]:
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
