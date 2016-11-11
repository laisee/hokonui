import time
from hokonui.exchanges.base import Exchange
from hokonui.models.ticker import Ticker
from hokonui.utils.helpers import apply_format, apply_format_level

class BitX(Exchange):

    TICKER_URL = 'https://api.mybitx.com/api/1/ticker?pair=XBT%s'
    ORDER_BOOK_URL = 'https://api.mybitx.com/api/1/orderbook?pair=XBT%s'
    NAME = 'BitX'

    @classmethod
    def test_name(cls):
       print " Name = ",cls.NAME
       print " test NAME : ", self.__name__

    @classmethod
    def _current_price_extractor(cls, data):
        return apply_format(data.get('last_trade'))

    @classmethod
    def _current_bid_extractor(cls, data):
        return apply_format(data.get('bid'))

    @classmethod
    def _current_ask_extractor(cls, data):
        return apply_format(data.get('ask'))

    @classmethod
    def _current_ticker_extractor(cls, data):
        return Ticker(cls.CCY_DEFAULT,apply_format(data.get('bid')), apply_format(data.get('ask'))).toJSON()

    @classmethod
    def _current_orders_extractor(cls,data,max_qty=3):
        orders = {}
        bids = {}
        asks = {}
        buyMax = 0
        sellMax = 0
        print data
        for level in data["bids"]:
            if buyMax > max_qty:
                pass
            else:
                asks[apply_format_level(level["price"])] = "{:.8f}".format(float(level["volume"]))
            buyMax = buyMax + float(level["volume"])

        for level in data["asks"]:
            if sellMax > max_qty:
                pass
            else:
                bids[apply_format_level(level["price"])] = "{:.8f}".format(float(level["volume"]))
            sellMax = sellMax + float(level["volume"])
 
        orders["source"] = cls.NAME
        orders["bids"] = bids
        orders["asks"] = asks
        orders["timestamp"] = str(int(time.time()))
        return orders
