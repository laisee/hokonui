""" Module for testing Zaif API """

# pylint: disable=duplicate-code, line-too-long

import time

from hokonui.exchanges.base import Exchange as Base
from hokonui.models.ticker import Ticker
from hokonui.utils.helpers import apply_format, apply_format_level


class Zaif(Base):
    """
    Class for Zaif API

    """

    TICKER_URL = "https://api.zaif.jp/api/1/ticker/btc_%s"
    ORDER_BOOK_URL = "https://api.zaif.jp/api/1/depth/btc_%s"
    NAME = "Zaif"
    CCY_DEFAULT = "jpy"

    @classmethod
    def _current_price_extractor(cls, data):
        return apply_format(str(data.get("last")))

    @classmethod
    def _current_bid_extractor(cls, data):
        return apply_format(data.get("bid"))

    @classmethod
    def _current_ask_extractor(cls, data):
        return apply_format(data.get("ask"))

    @classmethod
    def _current_ticker_extractor(cls, data):
        bid = apply_format(data.get("bid"))
        ask = apply_format(data.get("ask"))
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
                asks[apply_format_level(level[0])] = "{:.8f}".format(float(level[1]))
            buymax = buymax + float(level[1])

        for level in data["asks"]:
            if sellmax > max_qty:
                pass
            else:
                bids[apply_format_level(level[0])] = "{:.8f}".format(float(level[1]))
            sellmax = sellmax + float(level[1])

        orders["source"] = cls.NAME
        orders["bids"] = bids
        orders["asks"] = asks
        orders["ccy"] = cls.CCY_DEFAULT if cls.CCY_DEFAULT else Base.CCY_DEFAULT
        orders["timestamp"] = str(int(time.time()))
        return orders
