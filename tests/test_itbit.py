""" Module for testing ITBIT exchange """


import json
from sys import path
from unittest import TestCase

import nose
from nose.tools import ok_

from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.itbit import Itbit as itb
from hokonui.utils.helpers import docstring_parameter as docparams

LIBPATH = "../hokonui"
if LIBPATH not in path:
    path.append(LIBPATH)


class TestitBit(TestCase):
    """Class for testing ITBIT exchange"""

    @classmethod
    @docparams(itb.__name__, "setup")
    def setUp(cls):
        """{0}.{1}"""

        print(__name__, ": TestClass.setup_class() ----------")

    @classmethod
    @docparams(itb.__name__, "teardown")
    def tearDown(cls):
        """{0}.{1}"""

        print(__name__, ": TestClass.teardown_class() -------")

    @classmethod
    @docparams(itb.__name__, "name")
    def test_name(cls):
        """{0}.{1}"""

        ok_(itb.NAME == cls.__name__.replace("Test", ""))

    @classmethod
    @docparams(itb.__name__, "price")
    def test_price(cls):
        """{0}.{1}"""

        ok_(float(itb.get_current_price(base.CCY_DEFAULT)) > 0.00)

    @classmethod
    @docparams(itb.__name__, "bid")
    def test_bid(cls):
        """{0}.{1}"""

        ok_(float(itb.get_current_bid(base.CCY_DEFAULT)) > 0.00)

    @classmethod
    @docparams(itb.__name__, "ask")
    def test_ask(cls):
        """{0}.{1}"""

        ok_(float(itb.get_current_ask(base.CCY_DEFAULT)) > 0.00)

    @classmethod
    @docparams(itb.__name__, "ticker")
    def test_ticker(cls):
        """{0}.{1}"""

        data = json.loads(itb.get_current_ticker(base.CCY_DEFAULT))
        ok_(data["pair"] == base.CCY_DEFAULT, "shd be '%s'" % base.CCY_DEFAULT)
        ok_(float(data["ask"]) > 0.00, "ask should not be empty")
        ok_(float(data["bid"]) > 0.00, "bid should not be empty")
        ok_(float(data["bid"]) <= float(data["ask"]), "bid should be <= ask")
        ok_(float(data["timestamp"]) > 0, "Timestamp should be > zero")

    @classmethod
    @docparams(itb.__name__, "orders")
    def test_orders(cls):
        """{0}.{1}"""

        orders = itb.get_current_orders(base.CCY_DEFAULT)
        ok_(len(orders["asks"]) > 0, "Asks array should not be empty")
        ok_(len(orders["bids"]) > 0, "Bids array should not be empty")
        ok_(orders["source"] == "ITBIT", "Source should be 'ITBIT'")
        ok_(float(orders["timestamp"]) > 0, "Timestamp should be > zero")


if __name__ == "__main__":
    nose.runmodule()
