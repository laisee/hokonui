""" module for testing Poloniex API """

import json
from sys import path
from unittest import TestCase

from hokonui.exchanges.polo import Poloniex as polo
from hokonui.utils.helpers import docstring_parameter as docparams

LIBPATH = "../hokonui"
if LIBPATH not in path:
    path.append(LIBPATH)


class TestPoloniex(TestCase):
    """Class for testing Quoine API"""

    @classmethod
    @docparams(polo.__name__, "setup")
    def setup(cls):
        """{0}.{1}"""
        print(__name__, ": TestClass.setup_class() ----------")

    @classmethod
    @docparams(polo.__name__, "teardown")
    def teardown(cls):
        """{0}.{1}"""

        print(__name__, ": TestClass.teardown_class() -------")

    @classmethod
    @docparams(polo.__name__, "name")
    def test_name(cls):
        """{0}.{1}"""

        assert polo.NAME == cls.__name__.replace("Test", "")

    @classmethod
    @docparams(polo.__name__, "price")
    def test_price(cls):
        """{0}.{1}"""

        assert float(polo.get_current_price()) > 0.00

    @classmethod
    @docparams(polo.__name__, "bid")
    def test_bid(cls):
        """{0}.{1}"""

        assert float(polo.get_current_bid()) > 0.00

    @classmethod
    @docparams(polo.__name__, "ask")
    def test_ask(cls):
        """{0}.{1}"""

        assert float(polo.get_current_ask()) > 0.00

    @classmethod
    @docparams(polo.__name__, "ticker")
    def test_ticker(cls):
        """{0}.{1}"""

        data = json.loads(polo.get_current_ticker())
        assert data["pair"] == polo.CCY_DEFAULT, "shd be '%s'" % polo.CCY_DEFAULT
        assert float(data["ask"]) > 0.00, "ask should not be empty"
        assert float(data["bid"]) > 0.00, "bid should not be empty"
        assert float(data["bid"]) <= float(data["ask"]), "bid should be < ask"
        assert float(data["timestamp"]) > 0, "Timestamp should be > zero"

    @classmethod
    @docparams(polo.__name__, "orders")
    def test_orders(cls):
        """{0}.{1}"""

        orders = polo.get_current_orders(polo.CCY_DEFAULT)
        assert len(orders["asks"]) > 0, "Asks array should not be empty"
        assert len(orders["bids"]) > 0, "Bids array should not be empty"
        assert orders["source"] == "Poloniex", "Source should be 'Poloniex'"
        assert float(orders["timestamp"]) > 0, "Timestamp should be > zero"


if __name__ == "__main__":
    pass
