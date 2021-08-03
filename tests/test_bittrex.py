''' Module for testing Bittrex exchange '''


import json
from sys import path
from unittest import TestCase
from nose.tools import ok_
import nose
from hokonui.exchanges.bittrex import Bittrex as btx
from hokonui.utils.helpers import docstring_parameter as docparams


LIBPATH = '../hokonui'
if LIBPATH not in path:
    path.append(LIBPATH)


class TestBittrex(TestCase):
    ''' Class for testing Bittrex exchange '''
    @classmethod
    @docparams(btx.__name__, "setup")
    def setUp(cls):
        ''' {0}.{1}'''
        print(__name__, ': TestClass.setup_class() ----------')

    @classmethod
    @docparams(btx.__name__, "teardown")
    def tearDown(cls):
        ''' {0}.{1}'''
        print(__name__, ': TestClass.teardown_class() -------')

    @classmethod
    @docparams(btx.__name__, "name")
    def test_name(cls):
        ''' {0}.{1} '''
        ok_(btx.NAME == cls.__name__.replace('Test', ''))

    @classmethod
    @docparams(btx.__name__, "price")
    def test_price(cls):
        ''' {0}.{1} '''
        ok_(float(btx.get_current_price(btx.CCY_DEFAULT)) > 0.00)

    @classmethod
    @docparams(btx.__name__, "bid")
    def test_bid(cls):
        ''' {0}.{1} '''
        ok_(float(btx.get_current_bid(btx.CCY_DEFAULT)) > 0.00)

    @classmethod
    @docparams(btx.__name__, "ask")
    def test_ask(cls):
        ''' {0}.{1} '''
        ok_(float(btx.get_current_ask(btx.CCY_DEFAULT)) > 0.00)

    @classmethod
    @docparams(btx.__name__, "ticker")
    def test_ticker(cls):
        ''' {0}.{1} '''
        data = json.loads(btx.get_current_ticker(btx.CCY_DEFAULT))
        ok_(data["pair"] == btx.CCY_DEFAULT, "shd be '%s'" % btx.CCY_DEFAULT)
        ok_(float(data["ask"]) > 0.00, "ask should not be empty")
        ok_(float(data["bid"]) > 0.00, "bid should not be empty")
        ok_(float(data["bid"]) <= float(data["ask"]), "bid should be < ask")
        ok_(float(data["timestamp"]) > 0, "Timestamp should be > zero")

    @classmethod
    @docparams(btx.__name__, "orders")
    def test_orders(cls):
        ''' {0}.{1} '''
        orders = btx.get_current_orders(btx.CCY_DEFAULT)
        ok_(len(orders["asks"]) > 0, "Asks array should not be empty")
        ok_(len(orders["bids"]) > 0, "Bids array should not be empty")
        ok_(orders["source"] == "Bittrex", "Source should be 'Bittrex'")
        ok_(float(orders["timestamp"]) > 0, "Timestamp should be > zero")


if __name__ == '__main__':
    nose.runmodule()
