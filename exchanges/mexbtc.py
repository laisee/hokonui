import time
from exchanges.base import Exchange
from utils.helpers import apply_format, apply_format_level

class MexBtc(Exchange):

    TICKER_URL = 'https://public-api.mexbt.com/v1/ticker'
    ORDER_BOOK_URL = 'https://public-api.mexbt.com/v1/order-book'
    BODY = '{"productPair": "BTCUSD"}'
    NAME = 'MexBtc' 

    @classmethod
    def _current_price_extractor(cls, data):
        return apply_format(data.get('last'))
        #raise ValueError(str(data))

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
               bids[apply_format_level(level["px"])] = "{:.8f}".format(float(level["qty"]))
            buyMax = buyMax + float(level["qty"])

        for level in data["asks"]:
            if sellMax > max_qty:
                continue
            else:
                asks[apply_format_level(level["px"])] = "{:.8f}".format(float(level["qty"]))
            sellMax = sellMax + float(level["qty"])

        orders["Source"] = "MexBtc"
        orders["Bids"] = bids
        orders["Asks"] = asks
        orders["Timestamp"] = str(int(time.time()))
        #raise ValueError(str(orders))
        return orders
