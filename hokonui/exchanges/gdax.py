import time
from hokonui.exchanges.base import Exchange
from hokonui.models.ticker import Ticker
from hokonui.utils.helpers import apply_format, apply_format_level

class gdax(Exchange):

    TICKER_URL = 'https://api.exchange.coinbase.com/products/btc-usd/ticker'
    ORDER_BOOK_URL = 'https://api.bitflyer.jp/v1/getboard?product_code=%s'
    NAME = 'gdax'

    @classmethod
    def _current_price_extractor(cls, data):
        return apply_format(data.get('price'))

    @classmethod
    def _current_bid_extractor(cls, data):
        return apply_format(data.get('bid'))

    @classmethod
    def _current_ask_extractor(cls, data):
        return apply_format(data.get('ask'))

    @classmethod
    def _current_ticker_extractor(cls, data):
        return Ticker('USD',apply_format(data.get('bid')), apply_format(data.get('ask'))).toJSON()

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
 
        orders["source"] = cls.NAME
        orders["bids"] = bids
        orders["asks"] = asks
        orders["timestamp"] = str(int(time.time()))
        return orders
