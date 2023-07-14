""" Module for testing ItBit API """
# pylint: disable=duplicate-code, line-too-long

import time

from hokonui.exchanges.base import Exchange as Base
from hokonui.models.ticker import Ticker
from hokonui.utils.helpers import apply_format, apply_format_level


class Itbit(Base):
    """Class for testing ItBit API"""

    TICKER_URL = "https://api.itbit.com/v1/markets/XBT%s/ticker"
    ORDER_BOOK_URL = "https://api.itbit.com/v1/markets/XBT%s/order_book"
    NAME = "itBit"

    @classmethod
    def _current_price_extractor(cls, data):
        return apply_format(data.get("lastPrice"))

    @classmethod
    def _current_bid_extractor(cls, data):
        return apply_format(data.get("bid"))

    @classmethod
    def _current_ask_extractor(cls, data):
        return apply_format(data.get("ask"))

    @classmethod
    def _current_ticker_extractor(cls, data):
        return Ticker(cls.CCY_DEFAULT, apply_format(data.get("bid")), apply_format(data.get("ask"))).to_json()

    @classmethod
    def _current_orders_extractor(cls, data, max_qty=3):
        orders = {}
        bids = {}
        asks = {}
        buymax = 0
        sellmax = 0
        for level in data["bids"]:
            if buymax > max_qty:
                continue
            else:
                bids[apply_format_level(level[0])] = "{:.8f}".format(float(level[1]))
            buymax = buymax + float(level[1])

        for level in data["asks"]:
            if sellmax > max_qty:
                continue
            else:
                asks[apply_format_level(level[0])] = "{:.8f}".format(float(level[1]))
            sellmax = sellmax + float(level[1])

        orders["source"] = "ITBIT"
        orders["bids"] = bids
        orders["asks"] = asks
        orders["timestamp"] = str(int(time.time()))
        return orders
