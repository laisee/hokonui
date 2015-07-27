import time
from hokonui.exchanges.base import Exchange
from hokonui.models.ticker import Ticker
from hokonui.utils.helpers import apply_format, apply_format_level

class CoinSetter(Exchange):

    TICKER_URL = 'https://api.coinsetter.com/v1/marketdata/ticker'
    ORDER_BOOK_URL = 'https://api.coinsetter.com/v1/marketdata/depth'
    NAME = 'CoinSetter'

    @classmethod
    def _current_price_extractor(cls, data):
        return apply_format(data["last"].get('price'))

    @classmethod
    def _current_bid_extractor(cls, data):
        return apply_format(data["bid"].get('price'))

    @classmethod
    def _current_ask_extractor(cls, data):
        return apply_format(data["ask"].get('price'))

    @classmethod
    def _current_ticker_extractor(cls, data):
        return Ticker('USD',apply_format(data["bid"].get('price')),apply_format(data["ask"].get('price'))).toJSON()

    @classmethod
    def _current_orders_extractor(cls,data,max_qty=3):
        orders = {}
        bids = {}
        asks = {}
        buyMax = 0
        sellMax = 0
        for level in data["topNBidAsks"]:
            if buyMax > max_qty:
                pass
            else:
                asks[apply_format_level(level["ask"]["price"])] = "{:.8f}".format(float(level["ask"]["size"]))
            buyMax = buyMax + float(level["ask"]["size"])
            if sellMax > max_qty:
                pass
            else:
                bids[apply_format_level(level["bid"]["price"])] = "{:.8f}".format(float(level["bid"]["size"]))
            sellMax = sellMax + float(level["bid"]["size"])
 
        orders["source"] = "CoinSetter"
        orders["bids"] = bids
        orders["asks"] = asks
        orders["timestamp"] = str(int(time.time()))
        return orders
