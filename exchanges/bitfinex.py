import json, time
from exchanges.base import Exchange
from utils.helpers import apply_format, apply_format_level

class Bitfinex(Exchange):

    """ This is an implementation of the BTC-e private trade API and the public information API.
        Please refer to https://btc-e.com/api/documentation for API documentation.
    """
    TICKER_URL = 'https://api.bitfinex.com/v1/pubticker/btc%s'
    ORDER_BOOK_URL = 'https://api.bitfinex.com/v1/book/BTCUSD'
    NAME = 'Bitfinex'

    @classmethod
    def _current_price_extractor(cls, data):
        return apply_format(data.get('last_price'))

    @classmethod
    def _current_bid_extractor(cls, data):
        return apply_format(data.get('bid'))

    @classmethod
    def _current_ask_extractor(cls, data):
        return apply_format(data.get('ask'))

    @classmethod
    def _current_orders_extractor(cls,data,max_qty=3):
        orders = {}
        bids = {}
        asks = {}
        buyMax = 0
        sellMax = 0
        for level in data["bids"]:
            if buyMax > max_qty:
               continue
            else:
               bids[apply_format_level(level["price"])] = "{:.8f}".format(float(level["amount"]))
            buyMax = buyMax + float(level["amount"])

        for level in data["asks"]:
            if sellMax > max_qty:
                continue
            else:
                asks[apply_format_level(level["price"])] = "{:.8f}".format(float(level["amount"]))
            sellMax = sellMax + float(level["amount"])

        orders["Source"] = "Bitfinex"
        orders["Bids"] = bids
        orders["Asks"] = asks
        orders["Timestamp"] = str(int(time.time()))
        return orders
