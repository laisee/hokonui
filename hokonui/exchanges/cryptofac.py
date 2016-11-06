import time
from hokonui.exchanges.base import Exchange
from hokonui.models.ticker import Ticker
from hokonui.utils.helpers import apply_format, apply_format_level

class CryptoFacility(Exchange):

    TICKER_URL = 'https://www.cryptofacilities.com/derivatives/api/v2/tickers/'
    ORDER_BOOK_URL = 'https://www.cryptofacilities.com/derivatives/api/v2/orderbook?symbol=%s'
    NAME = 'CryptoFacility'

    @classmethod
    def _current_price_extractor(cls, data):
        price = data["tickers"][0]["last"]
        return apply_format(price)

    @classmethod
    def _current_bid_extractor(cls, data):
        bid = data["tickers"][0]["bid"]
        return apply_format(bid)

    @classmethod
    def _current_ask_extractor(cls, data):
        ask = data["tickers"][0]["ask"]
        return apply_format(ask)

    @classmethod
    def _current_ticker_extractor(cls, data):
        ask = data["tickers"][0]["ask"]
        bid = data["tickers"][0]["bid"]
        return Ticker('USD',apply_format(bid), apply_format(ask)).toJSON()

    @classmethod
    def _current_orders_extractor(cls,data,max_qty=3):
        orders = {}
        bids = {}
        asks = {}
        buyMax = 0
        sellMax = 0
        print data
        for level in data["orderBook"]["bids"]:
            if buyMax > max_qty:
               continue
            else:
               bids[apply_format_level(level[0])] = "{:.8f}".format(float(level[1]))
            buyMax = buyMax + float(level[1])

        for level in data["orderBook"]["asks"]:
            if sellMax > max_qty:
                continue
            else:
                asks[apply_format_level(level[0])] = "{:.8f}".format(float(level[1]))
            sellMax = sellMax + float(level[1])
 
        orders["source"] = cls.NAME
        orders["bids"] = bids
        orders["asks"] = asks
        orders["timestamp"] = str(int(time.time()))
        return orders
