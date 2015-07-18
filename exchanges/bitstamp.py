from exchanges.base import Exchange
from utils.helpers import apply_format

class Bitstamp(Exchange):

    TICKER_URL = 'https://bitstamp.net/api/ticker/'
    ORDER_BOOK_URL = 'https://www.bitstamp.net/api/order_book'
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
            buyMax = buyMax + float(level["amount"])

        for level in data["asks"]:
            if sellMax > max_qty:
                continue
            else:
               asks[apply_format_level(level[0])] = "{:.8f}".format(float(level[1]))
            sellMax = sellMax + float(level["amount"])

        orders["Source"] = "Bitfinex"
        orders["Bids"] = bids
        orders["Asks"] = asks
        orders["Timestamp"] = str(int(time.time()))
        return orders
