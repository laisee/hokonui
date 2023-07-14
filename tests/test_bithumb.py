""" Module for testing BitThumb exchange """

import json
from sys import path
from unittest import TestCase

# from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.bithumb import BitThumb as bth
from hokonui.utils.helpers import docstring_parameter as docparams

LIBPATH = "../hokonui"
if LIBPATH not in path:
    path.append(LIBPATH)


class TestBitThumb(TestCase):
    """Class for testing BitThumb exchange"""

    @classmethod
    @docparams(bth.__name__, "setup")
    def setUp(cls):
        """{0}.{1}"""
        print(__name__, ": TestClass.setup_class() ----------")

    @classmethod
    @docparams(bth.__name__, "teardown")
    def tearDown(cls):
        """{0}.{1}"""
        print(__name__, ": TestClass.teardown_class() -------")

    @classmethod
    @docparams(bth.__name__, "name")
    def test_name(cls):
        """{0}.{1}"""
        assert bth.NAME == cls.__name__.replace("Test", "")

    @classmethod
    @docparams(bth.__name__, "price")
    def test_price(cls):
        """{0}.{1}"""
        assert float(bth.get_current_price()) > 0.00

    @classmethod
    @docparams(bth.__name__, "bid")
    def test_bid(cls):
        """{0}.{1}"""
        assert float(bth.get_current_bid()) > 0.00

    @classmethod
    @docparams(bth.__name__, "ask")
    def test_ask(cls):
        """{0}.{1}"""
        assert float(bth.get_current_ask()) > 0.00

    @classmethod
    @docparams(bth.__name__, "ticker")
    def test_ticker(cls):
        """{0}.{1}"""
        data = json.loads(bth.get_current_ticker())
        assert data["pair"] == bth.CCY_DEFAULT, "shd be '%s'" % bth.CCY_DEFAULT
        assert float(data["ask"]) > 0.00, "ask should not be empty"
        assert float(data["bid"]) > 0.00, "bid should not be empty"
        assert float(data["bid"]) <= float(data["ask"]), "bid ({}) shd be < ask ({})".format(data["bid"], data["ask"])
        assert float(data["timestamp"]) > 0, "Timestamp should be > zero"

    @classmethod
    @docparams(bth.__name__, "orders")
    def test_orders(cls):
        """{0}.{1}"""
        orders = bth.get_current_orders()
        assert len(orders["asks"]) > 0, "Asks array should not be empty"
        assert len(orders["bids"]) > 0, "Bids array should not be empty"
        assert orders["source"] == "BitThumb", "Source should be 'BitThumb'"
        assert float(orders["timestamp"]) > 0, "Timestamp should be > zero"


if __name__ == "__main__":
    pass
