""" Module for testing OkCoin API """

# pylint: disable=fixme, line-too-long

import time

from hokonui.exchanges.base import Exchange as Base
from hokonui.models.ticker import Ticker
from hokonui.utils.helpers import apply_format, apply_format_level


class OKCoin(Base):
    """Class for testing OkCoin API"""

    API_VERSION = "v5"
    BASE_URL = "https://www.okcoin.com"
    TICKER_URL = f"{BASE_URL}/api/{API_VERSION}/market/ticker?instId=BTC-USD"
    ORDER_BOOK_URL = f"{BASE_URL}/api/{API_VERSION}/market/books?instId=BTC-USD"

    @classmethod
    def _current_price_extractor(cls, data):
        return apply_format(data["data"][0]["askPx"])

    @classmethod
    def _current_bid_extractor(cls, data):
        return apply_format(data["data"][0]["bidPx"])

    @classmethod
    def _current_ask_extractor(cls, data):
        print(data)
        return apply_format(data["data"][0]["askPx"])

    @classmethod
    def _current_ticker_extractor(cls, data):
        bid = apply_format(data["data"][0]["bidPx"])
        ask = apply_format(data["data"][0]["askPx"])
        return Ticker(cls.CCY_DEFAULT, bid, ask).to_json()

    @classmethod
    def _current_orders_extractor(cls, data, max_qty=3):
        orders = {}
        bids = {}
        asks = {}
        buymax = 0
        sellmax = 0
        for level in data["data"][0]["bids"]:
            if buymax > max_qty:
                pass
            else:
                bids[apply_format_level(level[0])] = "{:.8f}".format(float(level[1]))
            buymax = buymax + float(level[1])

        for level in data["data"][0]["asks"]:
            if sellmax > max_qty:
                pass
            else:
                asks[apply_format_level(level[0])] = "{:.8f}".format(float(level[1]))
            sellmax = sellmax + float(level[1])

        orders["source"] = "OKCoin"
        orders["bids"] = bids
        orders["asks"] = asks
        orders["timestamp"] = str(int(time.time()))
        return orders
