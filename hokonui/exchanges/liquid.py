""" Module for testing liquid API """
# pylint: disable=duplicate-code, line-too-long

import time

from hokonui.exchanges.base import Exchange as Base
from hokonui.models.ticker import Ticker
from hokonui.utils.helpers import apply_format, apply_format_level


class Liquid(Base):
    """
    Class for r/w Liquid API

    """

    TICKER_URL = "https://api.liquid.com/products/code/CASH/BTC%s"
    ORDER_BOOK_URL = "https://api.liquid.com/products/%s/price_levels"
    NAME = "Liquid"

    @classmethod
    def _current_price_extractor(cls, data):
        return apply_format(data.get("last_traded_price"))

    @classmethod
    def _current_bid_extractor(cls, data):
        return apply_format(data.get("market_bid"))

    @classmethod
    def _current_ask_extractor(cls, data):
        return apply_format(data.get("market_ask"))

    @classmethod
    def _current_ticker_extractor(cls, data):
        bid = apply_format(data.get("market_bid"))
        ask = apply_format(data.get("market_ask"))
        return Ticker(cls.CCY_DEFAULT, bid, ask).to_json()

    @classmethod
    def _current_orders_extractor(cls, data, max_qty=3):
        orders = {}
        bids = {}
        asks = {}
        buymax = 0
        sellmax = 0
        for level in data["buy_price_levels"]:
            if buymax > max_qty:
                pass
            else:
                asks[apply_format_level(level[0])] = "{:.8f}".format(float(level[1]))
            buymax = buymax + float(level[1])

        for level in data["sell_price_levels"]:
            if sellmax > max_qty:
                pass
            else:
                bids[apply_format_level(level[0])] = "{:.8f}".format(float(level[1]))
            sellmax = sellmax + float(level[1])

        orders["source"] = cls.NAME
        orders["bids"] = bids
        orders["asks"] = asks
        orders["timestamp"] = str(int(time.time()))
        return orders
