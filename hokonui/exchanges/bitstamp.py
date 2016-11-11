import time
from hokonui.exchanges.base import Exchange
from hokonui.utils.helpers import apply_format, apply_format_level
from hokonui.models.ticker import Ticker

class Bitstamp(Exchange):

    TICKER_URL = 'https://bitstamp.net/api/ticker/'
    ORDER_BOOK_URL = 'https://www.bitstamp.net/api/order_book/'
    NAME = 'Bitstamp'

    @classmethod
    def _current_price_extractor(cls, data):
        return apply_format(data.get('last'))

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
        if data:
            for level in data["bids"]:
                if buyMax > max_qty:
                   continue
                else:
                   bids[apply_format_level(level[0])] = "{:.8f}".format(float(level[1]))
                buyMax = buyMax + float(level[1])

            for level in data["asks"]:
                if sellMax > max_qty:
                    continue
                else:
                   asks[apply_format_level(level[0])] = "{:.8f}".format(float(level[1]))
                sellMax = sellMax + float(level[1])

        orders["source"] = "Bitfinex"
        orders["bids"] = bids
        orders["asks"] = asks
        orders["timestamp"] = str(int(time.time()))
        return orders
