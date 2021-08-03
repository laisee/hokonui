''' Module for testing Gemini API '''
# pylint: disable=duplicate-code, line-too-long

import time
from hokonui.exchanges.base import Exchange as Base
from hokonui.models.ticker import Ticker
from hokonui.utils.helpers import apply_format, apply_format_level


class Gemini(Base):
    '''
    Class for r/w Gemini API

    '''

    TICKER_URL = 'https://api.gemini.com/v2/ticker/%s'
    ORDER_BOOK_URL = 'https://api.sandbox.gemini.com/v1/book/%s'
    NAME = "Gemini"
    CCY_DEFAULT = "btcusd"

    @classmethod
    def _current_price_extractor(cls, data):
        return apply_format(data.get('close'))

    @classmethod
    def _current_bid_extractor(cls, data):
        return apply_format(data.get('bid'))

    @classmethod
    def _current_ask_extractor(cls, data):
        return apply_format(data.get('ask'))

    @classmethod
    def _current_ticker_extractor(cls, data):
        bid = apply_format(data.get('bid'))
        ask = apply_format(data.get('ask'))
        return Ticker(cls.CCY_DEFAULT, bid, ask).to_json()

    @classmethod
    def _current_orders_extractor(cls, data, max_qty=3):

        orders = {}
        bids = {}
        asks = {}
        buymax = 0
        sellmax = 0
        for level in data["bids"]:
            if buymax > max_qty:
                pass
            else:
                asks[apply_format_level(level["price"])] = "{:.8f}".format(
                    float(level["amount"]))
            buymax = buymax + float(level["amount"])

        for level in data["asks"]:
            if sellmax > max_qty:
                pass
            else:
                bids[apply_format_level(level["price"])] = "{:.8f}".format(
                    float(level["amount"]))
            sellmax = sellmax + float(level["amount"])

        orders["source"] = cls.NAME
        orders["bids"] = bids
        orders["asks"] = asks
        orders["timestamp"] = str(int(time.time()))
        return orders
