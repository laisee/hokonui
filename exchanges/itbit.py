import time
from exchanges.base import Exchange
from helpers import apply_format, apply_format_level

class Itbit(Exchange):

    TICKER_URL = 'https://api.itbit.com/v1/markets/XBT%s/ticker'
    ORDER_BOOK_URL = 'https://api.itbit.com/v1/markets/XBT%s/order_book'
    DEFAULT_MAX_ORDERBOOK_CUM_QTY = 10000.00
    NAME = 'Itbit'

    @classmethod
    def _current_price_extractor(cls, data):
        return apply_format(data.get('lastPrice'))

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
               bids[apply_format_level(level[0])] = "{:.8f}".format(float(level[1]))
            buyMax = buyMax + float(level[1])

        for level in data["asks"]:
            if sellMax > max_qty:
                continue
            else:
                asks[apply_format_level(level[0])] = "{:.8f}".format(float(level[1]))
            sellMax = sellMax + float(level[1])
 
        orders["Source"] = "ITBIT"
        orders["Bids"] = bids
        orders["Asks"] = asks
        orders["Timestamp"] = str(int(time.time()))
        return orders