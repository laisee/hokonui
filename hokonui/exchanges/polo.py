""" Module for testing Poloniex API """
# pylint: disable=duplicate-code, line-too-long

import time

from hokonui.exchanges.base import Exchange as Base
from hokonui.models.ticker import Ticker
from hokonui.utils.helpers import apply_format, apply_format_level


class Poloniex(Base):
    """
    Class for Poloniex API

    """

    CCY_DEFAULT = "USDT"
    NAME = "Poloniex"
    TICKER_URL = f"https://api.poloniex.com/markets/BTC_{CCY_DEFAULT}/ticker24h"
    ORDER_BOOK_URL = f"https://api.poloniex.com/markets/BTC_%s/orderBook"

    @classmethod
    def _current_price_extractor(cls, data):
        return apply_format(str(data["bid"]))

    @classmethod
    def _current_bid_extractor(cls, data):
        return apply_format(str(data["bid"]))

    @classmethod
    def _current_ask_extractor(cls, data):
        return apply_format(str(data["ask"]))

    @classmethod
    def _current_ticker_extractor(cls, data):
        ask = apply_format(str(data["ask"]))
        bid = apply_format(str(data["bid"]))
        return Ticker(cls.CCY_DEFAULT, bid, ask).to_json()

    @classmethod
    def _current_orders_extractor(cls, data, max_qty=3):
        orders = {}
        asks = {}
        bids = {}

        buymax = 0
        sellmax = 0

        float_numbers = [float(num) for num in data["bids"]]

        # Create tuples of consecutive numbers
        buy_orders = [(float_numbers[i], float_numbers[i + 1]) for i in range(0, len(float_numbers), 2)]

        float_numbers = [float(num) for num in data["asks"]]
        sell_orders = [(float_numbers[i], float_numbers[i + 1]) for i in range(0, len(float_numbers), 2)]

        orders["source"] = cls.NAME
        orders["bids"] = buy_orders
        orders["asks"] = sell_orders
        orders["timestamp"] = str(int(time.time()))
        return orders
