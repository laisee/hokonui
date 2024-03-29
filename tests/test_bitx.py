import json
from sys import path
from unittest import TestCase

from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.bitx import BitX as btx
from hokonui.utils.helpers import docstring_parameter as docparams

LIBPATH = "../hokonui"
if LIBPATH not in path:
    path.append(LIBPATH)


class TestBitX(TestCase):
    """Class for testing BitX API"""

    TEST_CCY = "ZAR"

    @classmethod
    @docparams(btx.__name__, "setup")
    def setup(cls):
        """{0}.{1}"""
        print(__name__, ": TestClass.setup_class() ----------")

    @classmethod
    @docparams(btx.__name__, "teardown")
    def teardown(cls):
        """{0}.{1}"""
        print(__name__, ": TestClass.teardown_class() -------")

    @classmethod
    @docparams(btx.__name__, "name")
    def test_name(cls):
        """{0}.{1}"""
        assert btx.NAME == cls.__name__.replace("Test", "")

    @classmethod
    @docparams(btx.__name__, "price")
    def test_price(cls):
        """{0}.{1}"""
        assert float(btx.get_current_price(cls.TEST_CCY)) > 0.00

    @classmethod
    @docparams(btx.__name__, "bid")
    def test_bid(cls):
        """{0}.{1}"""
        assert float(btx.get_current_bid(cls.TEST_CCY)) > 0.00

    @classmethod
    @docparams(btx.__name__, "ask")
    def test_ask(cls):
        """{0}.{1}"""
        assert float(btx.get_current_ask(cls.TEST_CCY)) > 0.00

    @classmethod
    @docparams(btx.__name__, "ticker")
    def test_ticker(cls):
        """{0}.{1}"""
        data = json.loads(btx.get_current_ticker(cls.TEST_CCY))
        assert data["pair"] == base.CCY_DEFAULT, "shd be '%s'" % cls.TEST_CCY
        assert float(data["ask"]) > 0.00, "ask should not be empty"
        assert float(data["bid"]) > 0.00, "bid should not be empty"
        assert float(data["bid"]) <= float(data["ask"]), "bid should be < ask"
        assert float(data["timestamp"]) > 0, "Timestamp should be > zero"

    @classmethod
    @docparams(btx.__name__, "orders")
    def test_orders(cls):
        """{0}.{1}"""
        orders = btx.get_current_orders(cls.TEST_CCY)
        assert len(orders["asks"]) > 0, "Asks array should not be empty"
        assert len(orders["bids"]) > 0, "Bids array should not be empty"
        assert orders["source"] == "BitX", "Source should be 'BitX'"
        assert float(orders["timestamp"]) > 0, "Timestamp should be > zero"


if __name__ == "__main__":
    pass
