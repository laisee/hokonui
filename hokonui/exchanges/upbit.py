''' Module for testing Upbit API '''
# pylint: disable=duplicate-code, line-too-long

import time
from hokonui.exchanges.base import Exchange as Base
from hokonui.models.ticker import Ticker
from hokonui.utils.helpers import apply_format, apply_format_level


class Upbit(Base):
    '''
    Class for Upbit API
    '''

    PRICE_URL = 'https://api.upbit.com/v1/ticker?markets=KRW-BTC'
    TICKER_URL = 'https://api.upbit.com/v1/ticker?markets=KRW-BTC'
    ORDER_BOOK_URL = 'https://api.upbit.com/v1/orderbook?markets=KRW-BTC'
    NAME = "Upbit"
    CCY_DEFAULT = "KRW"

    @classmethod
    def _current_price_extractor(cls, data):
        return apply_format(data[0].get('trade_price'))

    @classmethod
    def _current_bid_extractor(cls, data):
        return apply_format(data[0].get('trade_price'))

    @classmethod
    def _current_ask_extractor(cls, data):
        return apply_format(data[0].get('trade_price'))

    @classmethod
    def _current_ticker_extractor(cls, data):
        bid = apply_format(data[0].get('trade_price'))
        ask = apply_format(data[0].get('trade_price'))
        return Ticker(cls.CCY_DEFAULT, bid, ask).toJSON()

    @classmethod
    def _current_orders_extractor(cls, data, max_qty=3):

        orders = {}
        bids = {}
        asks = {}
        buymax = 0
        sellmax = 0
        for level in data[0]["orderbook_units"]:
            if buymax > max_qty:
                pass
            else:
                asks[apply_format_level(level["ask_price"])] = "{:.8f}".format(
                    float(level["ask_size"]))
            buymax = buymax + float(level["ask_size"])

        for level in data[0]["orderbook_units"]:
            if sellmax > max_qty:
                pass
            else:
                bids[apply_format_level(level["bid_price"])] = "{:.8f}".format(
                    float(level["bid_size"]))
            sellmax = sellmax + float(level["bid_size"])

        orders["source"] = cls.NAME
        orders["bids"] = bids
        orders["asks"] = asks
        orders["timestamp"] = str(int(time.time()))
        return orders
