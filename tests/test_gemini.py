""" module for testing Gemini API """


import json
from sys import path
from unittest import TestCase

import nose
from nose.tools import ok_

from hokonui.exchanges.gemini import Gemini as g2
from hokonui.utils.helpers import docstring_parameter as docparams

LIBPATH = "../hokonui"
if LIBPATH not in path:
    path.append(LIBPATH)


class TestGemini(TestCase):
    """Class for testing Gemini API"""

    @classmethod
    @docparams(g2.__name__, "setup")
    def setup(cls):
        """{0}.{1}"""

        print(__name__, ": TestClass.setup_class() ----------")

    @classmethod
    @docparams(g2.__name__, "teardown")
    def teardown(cls):
        """{0}.{1}"""

        print(__name__, ": TestClass.teardown_class() -------")

    @classmethod
    @docparams(g2.__name__, "name")
    def test_name(cls):
        """{0}.{1}"""

        ok_(g2.NAME == cls.__name__.replace("Test", ""))

    @classmethod
    @docparams(g2.__name__, "price")
    def test_price(cls):
        """{0}.{1}"""

        ok_(float(g2.get_current_price(g2.CCY_DEFAULT)) > 0.00)

    @classmethod
    @docparams(g2.__name__, "bid")
    def test_bid(cls):
        """{0}.{1}"""

        ok_(float(g2.get_current_bid(g2.CCY_DEFAULT)) > 0.00)

    @classmethod
    @docparams(g2.__name__, "ask")
    def test_ask(cls):
        """{0}.{1}"""

        ok_(float(g2.get_current_ask(g2.CCY_DEFAULT)) > 0.00)

    @classmethod
    @docparams(g2.__name__, "ticker")
    def test_ticker(cls):
        """{0}.{1}"""

        data = json.loads(g2.get_current_ticker(g2.CCY_DEFAULT))
        ok_(data["pair"] == g2.CCY_DEFAULT, "shd be '%s'" % g2.CCY_DEFAULT)
        ok_(float(data["ask"]) > 0.00, "ask should not be empty")
        ok_(float(data["bid"]) > 0.00, "bid should not be empty")
        ok_(float(data["bid"]) <= float(data["ask"]), "bid should be < ask")
        ok_(float(data["timestamp"]) > 0, "Timestamp should be > zero")

    @classmethod
    @docparams(g2.__name__, "orders")
    def test_orders(cls):
        """{0}.{1}"""

        orders = g2.get_current_orders(g2.CCY_DEFAULT)
        ok_(len(orders["asks"]) > 0, "Asks array should not be empty")
        ok_(len(orders["bids"]) > 0, "Bids array should not be empty")
        ok_(orders["source"] == "Gemini", "Source should be 'Gemini'")
        ok_(float(orders["timestamp"]) > 0, "Timestamp should be > zero")


if __name__ == "__main__":
    nose.runmodule()
