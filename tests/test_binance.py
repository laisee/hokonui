""" Module for testing Binance exchange """

import json
from sys import path
from unittest import TestCase

from hokonui.exchanges.binance import Binance as bn
from hokonui.utils.helpers import docstring_parameter as docparams

LIBPATH = "../hokonui"
if LIBPATH not in path:
    path.append(LIBPATH)


class TestBinance(TestCase):
    """Class for testing Binance exchange"""

    @classmethod
    @docparams(bn.__name__, "setup")
    def setUp(cls):
        """{0}.{1}"""

        print(__name__, ": TestClass.setup_class() ----------")

    @classmethod
    @docparams(bn.__name__, "teardown")
    def tearDown(cls):
        """{0}.{1}"""

        print(__name__, ": TestClass.teardown_class() -------")

    @classmethod
    @docparams(bn.__name__, "name")
    def test_name(cls):
        """{0}.{1}"""

        assert bn.NAME == cls.__name__.replace(
            "Test", ""
        ), "Name should be '%s', was '%s'" % (bn.NAME, cls.__name__)

    @classmethod
    @docparams(bn.__name__, "price")
    def test_price(cls):
        """{0}.{1}"""

        assert float(bn.get_current_price(bn.CCY_DEFAULT)) > 0.00

    @classmethod
    @docparams(bn.__name__, "bid")
    def test_bid(cls):
        """{0}.{1}"""

        assert float(bn.get_current_bid(bn.CCY_DEFAULT)) > 0.00

    @classmethod
    @docparams(bn.__name__, "ask")
    def test_ask(cls):
        """{0}.{1}"""

        assert float(bn.get_current_ask(bn.CCY_DEFAULT)) > 0.00

    @classmethod
    @docparams(bn.__name__, "ticker")
    def test_ticker(cls):
        """{0}.{1}"""

        data = json.loads(bn.get_current_ticker(bn.CCY_DEFAULT))
        assert data["pair"] == bn.CCY_DEFAULT, "should be '%s'" % bn.CCY_DEFAULT
        assert float(data["ask"]) > 0.00, "ask should not be empty"
        assert float(data["bid"]) > 0.00, "bid should not be empty"
        assert float(data["bid"]) <= float(data["ask"]), "bid should be < ask"
        assert float(data["timestamp"]) > 0, "Timestamp should be > zero"

    @classmethod
    @docparams(bn.__name__, "orders")
    def test_orders(cls):
        """{0}.{1}"""

        orders = bn.get_current_orders(bn.CCY_DEFAULT)
        assert len(orders["asks"]) > 0, "Asks array should not be empty"
        assert len(orders["bids"]) > 0, "Bids array should not be empty"
        assert orders["source"] == "Binance", "Source should be 'Binance'"
        assert float(orders["timestamp"]) > 0, "Timestamp should be > zero"


if __name__ == "__main__":
    pass
