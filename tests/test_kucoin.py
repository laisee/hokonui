""" Module for testing Kucoin exchange """

import json
from sys import path
from unittest import TestCase

import nose
from nose.tools import ok_

from hokonui.exchanges.kucoin import Kucoin as kuc
from hokonui.utils.helpers import docstring_parameter as docparams

LIBPATH = "../hokonui"
if LIBPATH not in path:
    path.append(LIBPATH)


class TestKucoin(TestCase):
    """Class for testing Kucoin exchange"""

    @classmethod
    @docparams(kuc.__name__, "setup")
    def setUp(cls):
        """{0}.{1}"""

        print(__name__, ": TestClass.setup_class() ----------")

    @classmethod
    @docparams(kuc.__name__, "teardown")
    def tearDown(cls):
        """{0}.{1}"""

        print(__name__, ": TestClass.teardown_class() -------")

    @classmethod
    @docparams(kuc.__name__, "name")
    def test_name(cls):
        """{0}.{1}"""

        ok_(kuc.NAME == cls.__name__.replace("Test", ""), "Name should be '%s', was '%s'" % (kuc.NAME, cls.__name__))

    @classmethod
    @docparams(kuc.__name__, "price")
    def test_price(cls):
        """{0}.{1}"""

        ok_(float(kuc.get_current_price()) > 0.00)

    @classmethod
    @docparams(kuc.__name__, "bid")
    def test_bid(cls):
        """{0}.{1}"""

        ok_(float(kuc.get_current_bid()) > 0.00)

    @classmethod
    @docparams(kuc.__name__, "ask")
    def test_ask(cls):
        """{0}.{1}"""

        ok_(float(kuc.get_current_ask()) > 0.00)

    @classmethod
    @docparams(kuc.__name__, "ticker")
    def test_ticker(cls):
        """{0}.{1}"""

        data = json.loads(kuc.get_current_ticker())
        ok_(data["pair"] == kuc.CCY_DEFAULT, "should be '%s'" % kuc.CCY_DEFAULT)
        ok_(float(data["ask"]) > 0.00, "ask should not be empty")
        ok_(float(data["bid"]) > 0.00, "bid should not be empty")
        ok_(float(data["bid"]) <= float(data["ask"]), "bid should be < ask")
        ok_(float(data["timestamp"]) > 0, "Timestamp should be > zero")

    @classmethod
    @docparams(kuc.__name__, "orders")
    def test_orders(cls):
        """{0}.{1}"""

        orders = kuc.get_current_orders()
        print(orders)
        ok_(len(orders["asks"]) > 0, "Asks array should not be empty")
        ok_(len(orders["bids"]) > 0, "Bids array should not be empty")
        ok_(orders["source"] == "Kucoin", "Source should be 'Kucoin'")
        ok_(float(orders["timestamp"]) > 0, "Timestamp should be > zero")


if __name__ == "__main__":
    nose.runmodule()
