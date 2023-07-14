""" Module for testing Birfinex API """

import json
from sys import path
from unittest import TestCase

from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.bitfinex import Bitfinex as bfx
from hokonui.utils.helpers import docstring_parameter as docparams

LIBPATH = "../hokonui"
if LIBPATH not in path:
    path.append(LIBPATH)


class TestBitfinex(TestCase):
    """Class for testing Bitfinex API"""

    @classmethod
    @docparams(bfx.__name__, "name")
    def test_name(cls):
        """{0}.{1}"""
        assert bfx.NAME == cls.__name__.replace("Test", "")

    @classmethod
    @docparams(bfx.__name__, "price")
    def test_price(cls):
        """{0}.{1}"""
        assert float(bfx.get_current_price(base.CCY_DEFAULT)) > 0.00

    @classmethod
    @docparams(bfx.__name__, "bid")
    def test_bid(cls):
        """{0}.{1}"""
        assert float(bfx.get_current_bid(base.CCY_DEFAULT)) > 0.00

    @classmethod
    @docparams(bfx.__name__, "ask")
    def test_ask(cls):
        """{0}.{1}"""
        assert float(bfx.get_current_ask(base.CCY_DEFAULT)) > 0.00

    @classmethod
    @docparams(bfx.__name__, "ticker")
    def test_ticker(cls):
        """{0}.{1}"""
        data = json.loads(bfx.get_current_ticker(base.CCY_DEFAULT))
        assert data["pair"] == base.CCY_DEFAULT, "shd be '%s'" % base.CCY_DEFAULT
        assert float(data["ask"]) > 0.00, "ask should not be empty"
        assert float(data["bid"]) > 0.00, "bid should not be empty"
        assert float(data["bid"]) <= float(data["ask"]), "bid should be < ask"
        assert float(data["timestamp"]) > 0, "Timestamp should be > zero"

    @classmethod
    @docparams(bfx.__name__, "orders")
    def test_orders(cls):
        """{0}.{1}"""
        orders = bfx.get_current_orders(base.CCY_DEFAULT)
        assert len(orders["asks"]) > 0, "Asks array should not be empty"
        assert len(orders["bids"]) > 0, "Bids array should not be empty"
        assert orders["source"] == "Bitfinex", "Source should be 'Bitfinex'"
        assert float(orders["timestamp"]) > 0, "Timestamp should be > zero"


if __name__ == "__main__":
    pass
