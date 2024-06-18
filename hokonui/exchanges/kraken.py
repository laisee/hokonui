""" Module for testing Kraken API """

# pylint: disable=duplicate-code, line-too-long

import time

from hokonui.exchanges.base import Exchange as Base
from hokonui.models.ticker import Ticker
from hokonui.utils.helpers import apply_format, apply_format_level


class Kraken(Base):
    """Class for testing Kraken API"""

    TICKER_URL = "https://api.kraken.com/0/public/Ticker?pair=xbtusd"
    ORDER_BOOK_URL = "https://api.kraken.com/0/public/Depth?pair=XBTUSD&count=100"
    NAME = "Kraken"

    @classmethod
    def _current_price_extractor(cls, data):
        pair = list(data["result"].keys())[0]
        last = list(data["result"][pair]["c"])[0]
        return apply_format(last)

    @classmethod
    def _current_bid_extractor(cls, data):
        pair = list(data["result"].keys())[0]
        bid = list(data["result"][pair]["b"])[0]
        return apply_format(bid)

    @classmethod
    def _current_ask_extractor(cls, data):
        pair = list(data["result"].keys())[0]
        ask = list(data["result"][pair]["a"])[0]
        return apply_format(ask)

    @classmethod
    def _current_ticker_extractor(cls, data):
        pair = list(data["result"].keys())[0]
        ask = list(data["result"][pair]["a"])[0]
        bid = list(data["result"][pair]["b"])[0]
        return Ticker(pair, apply_format(bid), apply_format(ask)).to_json()

    @classmethod
    def _current_orders_extractor(cls, data, max_qty=100.0):
        orders = {}
        bids = {}
        asks = {}
        buymax = 0.0
        sellmax = 0.0
        pair = list(data["result"].keys())[0]
        for level in data["result"][pair]["bids"]:
            if buymax > max_qty:
                pass
            else:
                asks[apply_format_level(level[0])] = "{:.8f}".format(float(level[1]))
                buymax = buymax + float(level[1])

        for level in data["result"][pair]["asks"]:
            if sellmax > max_qty:
                pass
            else:
                bids[apply_format_level(level[0])] = "{:.8f}".format(float(level[1]))
                sellmax = sellmax + float(level[1])
        orders["source"] = "Kraken"
        orders["bids"] = bids
        orders["asks"] = asks
        orders["timestamp"] = str(int(time.time()))
        return orders
