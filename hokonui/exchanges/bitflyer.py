import time
from hokonui.exchanges.base import Exchange
from hokonui.models.ticker import Ticker
from hokonui.utils.helpers import apply_format, apply_format_level

class BitFlyer(Exchange):

    TICKER_URL = 'https://api.bitflyer.jp/v1/ticker?product_code=%s'
    ORDER_BOOK_URL = 'https://api.bitflyer.jp/v1/getboard?product_code=%s'
    PRICE_URL = 'https://api.bitflyer.jp/v1/getexecutions?product_code=%s&count=1'
    NAME = 'BitFlyer'

    @classmethod
    def _current_price_extractor(cls, data):
        return apply_format(data[0].get('price'))

    @classmethod
    def _current_bid_extractor(cls, data):
        return apply_format(data.get('best_bid'))

    @classmethod
    def _current_ask_extractor(cls, data):
        return apply_format(data.get('best_ask'))

    @classmethod
    def _current_ticker_extractor(cls, data):
        return Ticker('USD',apply_format(data.get('best_bid')), apply_format(data.get('best_ask'))).toJSON()

    @classmethod
    def _current_orders_extractor(cls,data,max_qty=3):
        orders = {}
        bids = {}
        asks = {}
        buyMax = 0
        sellMax = 0
        for level in data["bids"]:
            if buyMax > max_qty:
                pass
            else:
                asks[apply_format_level(level["price"])] = "{:.8f}".format(float(level["size"]))
            buyMax = buyMax + float(level["size"])

        for level in data["asks"]:
            if sellMax > max_qty:
                pass
            else:
                bids[apply_format_level(level["price"])] = "{:.8f}".format(float(level["size"]))
            sellMax = sellMax + float(level["size"])
 
        orders["source"] = "BitFlyer"
        orders["bids"] = bids
        orders["asks"] = asks
        orders["timestamp"] = str(int(time.time()))
        return orders
