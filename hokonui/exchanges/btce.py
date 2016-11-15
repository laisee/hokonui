import time
import string
from hokonui.exchanges.base import Exchange
from hokonui.models.ticker import Ticker
from hokonui.utils.helpers import apply_format
from hokonui.utils.helpers import apply_format_level


class BTCE(Exchange):

    PAIR = "btc_%s" % string.lower(Exchange.CCY_DEFAULT)
    TICKER_URL = 'https://btc-e.com/api/3/ticker/%s' % PAIR
    ORDER_BOOK_URL = 'https://btc-e.com/api/3/depth/%s' % PAIR
    NAME = 'BTCE'

    @classmethod
    def _current_price_extractor(cls, data):
        return apply_format(data[cls.PAIR].get('last'))

    @classmethod
    def _current_bid_extractor(cls, data):
        return apply_format(data[cls.PAIR].get('buy'))

    @classmethod
    def _current_ask_extractor(cls, data):
        return apply_format(data[cls.PAIR].get('sell'))

    @classmethod
    def _current_ticker_extractor(cls, data):
        print data
        return Ticker(cls.CCY_DEFAULT, apply_format(data[cls.PAIR].get('buy')), apply_format(data[cls.PAIR].get('sell'))).toJSON()

    @classmethod
    def _current_orders_extractor(cls, data, max_qty=3):
        orders = {}
        bids = {}
        asks = {}
        buyMax = 0
        sellMax = 0
        print data
        for level in data[cls.PAIR]["bids"]:
            if buyMax > max_qty:
                pass
            else:
                asks[apply_format_level(level[0])] = "{:.8f}".format(float(level[1]))
            buyMax = buyMax + float(level[1])

        for level in data[cls.PAIR]["asks"]:
            if sellMax > max_qty:
                pass
            else:
                bids[apply_format_level(level[0])] = "{:.8f}".format(float(level[1]))
            sellMax = sellMax + float(level[1])

        orders["source"] = "BTCE"
        orders["bids"] = bids
        orders["asks"] = asks
        orders["timestamp"] = str(int(time.time()))
        return orders
