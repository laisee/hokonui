''' Module for testing BTC-E API '''
# pylint: disable=duplicate-code, line-too-long

import time
from hokonui.exchanges.base import Exchange as Base
from hokonui.models.ticker import Ticker
from hokonui.utils.helpers import apply_format
from hokonui.utils.helpers import apply_format_level


class BTCE(Base):
    ''' Class for testing BTCE API '''

    PAIR = "btc_%s" % Base.CCY_DEFAULT.lower()
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
        return Ticker(cls.CCY_DEFAULT, apply_format(data[cls.PAIR].get('buy')), apply_format(data[cls.PAIR].get('sell'))).toJSON()

    @classmethod
    def _current_orders_extractor(cls, data, max_qty=3):
        orders = {}
        bids = {}
        asks = {}
        buymax = 0
        sellmax = 0
        for level in data[cls.PAIR]["bids"]:
            if buymax > max_qty:
                pass
            else:
                asks[apply_format_level(level[0])] = "{:.8f}".format(float(level[1]))
            buymax = buymax + float(level[1])

        for level in data[cls.PAIR]["asks"]:
            if sellmax > max_qty:
                pass
            else:
                bids[apply_format_level(level[0])] = "{:.8f}".format(float(level[1]))
            sellmax = sellmax + float(level[1])

        orders["source"] = "BTCE"
        orders["bids"] = bids
        orders["asks"] = asks
        orders["timestamp"] = str(int(time.time()))
        return orders
