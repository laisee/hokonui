""" Module for testing Bitstamp exchange """

import json
from sys import path
from unittest import TestCase

import nose
from nose.tools import ok_

from hokonui.exchanges.bitstamp import Bitstamp as bts
from hokonui.utils.helpers import docstring_parameter as docparams

LIBPATH = "../hokonui"
if LIBPATH not in path:
    path.append(LIBPATH)


class TestBitstamp(TestCase):
    """Class for testing Bitstamp exchange"""

    @classmethod
    @docparams(bts.__name__, "setup")
    def setUp(cls):
        """{0}.{1}"""
        print(__name__, ": TestClass.setup_class() ----------")

    @classmethod
    @docparams(bts.__name__, "teardown")
    def tearDown(cls):
        """{0}.{1}"""
        print(__name__, ": TestClass.teardown_class() -------")

    @classmethod
    @docparams(bts.__name__, "name")
    def test_name(cls):
        """{0}.{1}"""
        ok_(bts.NAME == cls.__name__.replace("Test", ""))

    @classmethod
    @docparams(bts.__name__, "price")
    def test_price(cls):
        """{0}.{1}"""
        ok_(float(bts.get_current_price(bts.CCY_DEFAULT)) > 0.00)

    @classmethod
    @docparams(bts.__name__, "bid")
    def test_bid(cls):
        """{0}.{1}"""
        ok_(float(bts.get_current_bid(bts.CCY_DEFAULT)) > 0.00)

    @classmethod
    @docparams(bts.__name__, "ask")
    def test_ask(cls):
        """{0}.{1}"""
        ok_(float(bts.get_current_ask(bts.CCY_DEFAULT)) > 0.00)

    @classmethod
    @docparams(bts.__name__, "ticker")
    def test_ticker(cls):
        """{0}.{1}"""
        data = json.loads(bts.get_current_ticker(bts.CCY_DEFAULT))
        ok_(data["pair"] == bts.CCY_DEFAULT, "shd be '%s'" % bts.CCY_DEFAULT)
        ok_(float(data["ask"]) > 0.00, "ask should not be empty")
        ok_(float(data["bid"]) > 0.00, "bid should not be empty")
        ok_(float(data["bid"]) <= float(data["ask"]), "bid should be < ask")
        ok_(float(data["timestamp"]) > 0, "Timestamp should be > zero")

    @classmethod
    @docparams(bts.__name__, "orders")
    def test_orders(cls):
        """{0}.{1}"""
        orders = bts.get_current_orders(bts.CCY_DEFAULT)
        ok_(len(orders["asks"]) > 0, "Asks array should not be empty")
        ok_(len(orders["bids"]) > 0, "Bids array should not be empty")
        ok_(orders["source"] == "Bitstamp", "Source should be 'Bitstamp'")
        ok_(float(orders["timestamp"]) > 0, "Timestamp should be > zero")


if __name__ == "__main__":
    nose.runmodule()
