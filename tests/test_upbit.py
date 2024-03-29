""" Module for testing Upbit exchange """


import json
from sys import path
from unittest import TestCase

from hokonui.exchanges.upbit import Upbit as upb
from hokonui.utils.helpers import docstring_parameter as docparams

LIBPATH = "../hokonui"
if LIBPATH not in path:
    path.append(LIBPATH)


class TestUpbit(TestCase):
    """Class for testing Upbit exchange"""

    @classmethod
    @docparams(upb.__name__, "setup")
    def setUp(cls):
        """{0}.{1}"""
        print(__name__, ": TestClass.setup_class() ----------")

    @classmethod
    @docparams(upb.__name__, "teardown")
    def tearDown(cls):
        """{0}.{1}"""
        print(__name__, ": TestClass.teardown_class() -------")

    @classmethod
    @docparams(upb.__name__, "name")
    def test_name(cls):
        """{0}.{1}"""
        assert upb.NAME == cls.__name__.replace("Test", "")

    @classmethod
    @docparams(upb.__name__, "price")
    def test_price(cls):
        """{0}.{1}"""
        assert float(upb.get_current_price()) > 0.00

    @classmethod
    @docparams(upb.__name__, "bid")
    def test_bid(cls):
        """{0}.{1}"""
        assert float(upb.get_current_bid()) > 0.00

    @classmethod
    @docparams(upb.__name__, "ask")
    def test_ask(cls):
        """{0}.{1}"""
        assert float(upb.get_current_ask()) > 0.00

    @classmethod
    @docparams(upb.__name__, "ticker")
    def test_ticker(cls):
        """{0}.{1}"""
        data = json.loads(upb.get_current_ticker())
        assert float(data["ask"]) > 0.00, "ask should not be empty"
        assert float(data["bid"]) > 0.00, "bid should not be empty"
        assert float(data["bid"]) <= float(data["ask"]), "bid should be < ask"
        assert float(data["timestamp"]) > 0, "Timestamp should be > zero"

    @classmethod
    @docparams(upb.__name__, "orders")
    def test_orders(cls):
        """{0}.{1}"""
        orders = upb.get_current_orders()
        assert len(orders["asks"]) > 0, "Asks array should not be empty"
        assert len(orders["bids"]) > 0, "Bids array should not be empty"
        assert orders["source"] == "Upbit", "Source should be 'Upbit'"
        assert float(orders["timestamp"]) > 0, "Timestamp should be > zero"


if __name__ == "__main__":
    pass
