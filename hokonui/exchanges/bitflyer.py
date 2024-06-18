""" Module for testing BitFlyer API """

# pylint: disable=duplicate-code, line-too-long
import time

from hokonui.exchanges.base import Exchange as Base
from hokonui.models.ticker import Ticker
from hokonui.utils.helpers import apply_format, apply_format_level


class BitFlyer(Base):
    """Class for testing BitFlyer API"""

    TICKER_URL = "https://api.bitflyer.jp/v1/ticker?product_code=%s"
    ORDER_BOOK_URL = "https://api.bitflyer.jp/v1/getboard?product_code=%s"
    PRICE_URL = "https://api.bitflyer.jp/v1/getexecutions?product_code=%s&count=1"
    NAME = "BitFlyer"

    @classmethod
    def _current_price_extractor(cls, data):
        """Method for extracting current price"""
        return apply_format(data[0].get("price"))

    @classmethod
    def _current_bid_extractor(cls, data):
        """Method for extracting bid price"""
        return apply_format(data.get("best_bid"))

    @classmethod
    def _current_ask_extractor(cls, data):
        """Method for extracting ask price"""
        return apply_format(data.get("best_ask"))

    @classmethod
    def _current_ticker_extractor(cls, data):
        """Method for extracting ticker"""
        bid = apply_format(data.get("best_bid"))
        ask = apply_format(data.get("best_ask"))
        return Ticker(cls.CCY_DEFAULT, bid, ask).to_json()

    @classmethod
    def _current_orders_extractor(cls, data, max_qty=3):
        """Method for extracting orders"""
        orders = {}
        bids = {}
        asks = {}
        buymax = 0
        sellmax = 0
        for level in data["bids"]:
            if buymax > max_qty:
                pass
            else:
                asks[apply_format_level(level["price"])] = "{:.8f}".format(float(level["size"]))
            buymax = buymax + float(level["size"])

        for level in data["asks"]:
            if sellmax > max_qty:
                pass
            else:
                bids[apply_format_level(level["price"])] = "{:.8f}".format(float(level["size"]))
            sellmax = sellmax + float(level["size"])

        orders["source"] = cls.NAME
        orders["bids"] = bids
        orders["asks"] = asks
        orders["timestamp"] = str(int(time.time()))
        return orders
