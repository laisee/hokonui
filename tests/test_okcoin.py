""" Module for testing Ok Coin API """


import json
from sys import path
from unittest import TestCase

import nose
from nose.tools import ok_

from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.okcoin import OKCoin as okc
from hokonui.utils.helpers import docstring_parameter as docparams

LIBPATH = "../hokonui"
if LIBPATH not in path:
    path.append(LIBPATH)


class TestOkCoin(TestCase):
    """Class for testing OkCoin API"""

    @classmethod
    @docparams(okc.__name__, "name")
    def test_name(cls):
        """{0}.{1}"""

        ok_(okc.__name__ != "")

    @classmethod
    @docparams(okc.__name__, "price")
    def test_price(cls):
        """{0}.{1}"""

        ok_(float(okc.get_current_price()) > 0.00)

    @classmethod
    @docparams(okc.__name__, "bid")
    def test_bid(cls):
        """{0}.{1}"""

        ok_(float(okc.get_current_bid()) > 0.00)

    @classmethod
    @docparams(okc.__name__, "ask")
    def test_ask(cls):
        """{0}.{1}"""

        ok_(float(okc.get_current_ask()) > 0.00)

    @classmethod
    @docparams(okc.__name__, "ticker")
    def test_ticker(cls):
        """{0}.{1}"""
        data = json.loads(okc.get_current_ticker())
        ok_(data["pair"] == base.CCY_DEFAULT, "shd be '%s'" % base.CCY_DEFAULT)
        ok_(float(data["ask"]) > 0.00, "ask should not be empty")
        ok_(float(data["bid"]) > 0.00, "bid should not be empty")
        ok_(float(data["bid"]) <= float(data["ask"]), "bid should be <= ask")
        ok_(float(data["timestamp"]) > 0, "Timestamp should be greater than zero")

    @classmethod
    @docparams(okc.__name__, "orders")
    def test_orders(cls):
        """{0}.{1}"""

        orders = okc.get_current_orders()
        ok_(len(orders["asks"]) > 0, "Asks array should not be empty")
        ok_(len(orders["bids"]) > 0, "Bids array should not be empty")
        ok_(orders["source"] == "OKCoin", "Source should be 'OKCoin'")
        ok_(float(orders["timestamp"]) > 0, "Timestamp should be > zero")


if __name__ == "__main__":
    nose.runmodule()
