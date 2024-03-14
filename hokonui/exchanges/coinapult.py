""" Module for testing Coinapult API """
# pylint: disable=duplicate-code, line-too-long

from hokonui.exchanges.base import Exchange as Base
from hokonui.models.ticker import Ticker
from hokonui.utils.helpers import apply_format, get_response


class Coinapult(Base):
    """Class for testing Coinapult API"""

    TICKER_URL = "https://api.coinapult.com/api/ticker?market=%s_BTC"
    TICKER_LEVEL = [
        (50, "small"),
        (250, "medium"),
        (1000, "large"),
        (2500, "vip"),
        (5000, "vip+"),
    ]
    NAME = "Coinapult"

    @classmethod
    def get_current_price(cls, ccy=None, params=None, body=None, header=None):
        """method for testing last price"""

        url = cls.TICKER_URL.format(ccy)
        data = get_response(url, ccy)
        return apply_format(str(data["index"]))

    @classmethod
    def get_current_bid(cls, ccy=None, params=None, body=None, header=None):
        """method for testing current bid price"""
        btc_amount = 0.1
        url = cls.TICKER_URL.format(ccy)
        data = get_response(url, ccy)
        level = cls._pick_level(btc_amount) if btc_amount > 0 else "small"
        price = str(data[level]["bid"])
        return apply_format(price)

    @classmethod
    def get_current_ask(cls, ccy=None, params=None, body=None, header=None):
        """method for testing current ask price"""
        btc_amount = 0.1
        url = cls.TICKER_URL.format(ccy)
        data = get_response(url, ccy)
        level = cls._pick_level(btc_amount) if btc_amount > 0 else "small"
        price = str(data[level]["ask"])
        return apply_format(price)

    @classmethod
    def get_current_ticker(cls, ccy=None, params=None, body=None, header=None):
        """method for testing current ticker"""

        btc_amount = 0
        url = cls.TICKER_URL.format(ccy)
        data = get_response(url, ccy, params, body, header)
        level = cls._pick_level(btc_amount) if btc_amount > 0 else "small"
        ask = apply_format(str(data[level]["ask"]))
        bid = apply_format(str(data[level]["bid"]))
        return Ticker(ccy, bid, ask).to_json()

    @classmethod
    def _current_ticker_extractor(cls, data):
        """Method for extracting current price"""

    @classmethod
    def _current_price_extractor(cls, data):
        """Method for extracting current price"""

    @classmethod
    def _current_bid_extractor(cls, data):
        """Method for extracting bid price"""

    @classmethod
    def _current_ask_extractor(cls, data):
        """Method for extracting ask price"""

    @classmethod
    def _current_orders_extractor(cls, data, max_qty=100):
        """Method for extracting ask price"""

    @classmethod
    def get_current_orders(cls, ccy=None, params=None, body=None, header=None):
        """method for testing current orders"""
        raise ValueError("not implemented for this class using ccy %s" % ccy)

    @classmethod
    def _pick_level(cls, btc_amount):
        """ """
        for size, level in cls.TICKER_LEVEL:
            if btc_amount < size:
                return level
        return cls.TICKER_LEVEL[-1][1]
