import time
from hokonui.exchanges.base import Exchange
from hokonui.models.ticker import Ticker
from hokonui.utils.helpers import apply_format, apply_format_level

class CoinBase(Exchange):

    TICKER_URL = 'https://api.exchange.coinbase.com/products/BTC-%s/'
    ORDER_BOOK_URL = 'https://api.exchange.coinbase.com/products/BTC-%s/book?level=2'
    NAME = 'CoinBase'

    @classmethod
    def _current_price_extractor(cls, data):
        return apply_format(data.get('price'))

    @classmethod
    def _current_bid_extractor(cls, data):
        return apply_format(data["bids"][0][0])
        # {"sequence":155230585,"bids":[["281.7","2.33",1]],"asks":[["281.71","0.00036374",1]]}

    @classmethod
    def _current_ask_extractor(cls, data):
        return apply_format(data["asks"][0][0])

    @classmethod
    def _current_ticker_extractor(cls, data):
        return Ticker('USD',apply_format((data["bids"][0][0]), apply_format((data["asks"][0][0])).toJSON()

    @classmethod
    def _current_orders_extractor(cls,data,max_qty=3):
        orders ={}
        bids  = {}
        asks  = {}
        buyMax = 0
        sellMax = 0
        for level in data["bids"]:
            if buyMax > max_qty:
                pass
            else:
                asks[apply_format_level(level[0])] = "{:.8f}".format(float(level[1]))
            buyMax = buyMax + float(level[1])

        for level in data["asks"]:
            if sellMax > max_qty:
                pass
            else:
                bids[apply_format_level(level[0])] = "{:.8f}".format(float(level[1]))
            sellMax = sellMax + float(level[1])
 
        orders["source"] = "CoinBase"
        orders["bids"] = bids
        orders["asks"] = asks
        orders["timestamp"] = str(int(time.time()))
        return orders
