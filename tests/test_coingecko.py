''' Module for testing CoinBasse API '''


import json
from sys import path
from unittest import TestCase
from nose.tools import ok_
import nose
from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.coinbase import CoinBase as cba
from hokonui.utils.helpers import docstring_parameter as docparams

LIBPATH = '../hokonui'
if LIBPATH not in path:
    path.append(LIBPATH)



class TestCoinbase(TestCase):
    ''' Class for testing Coinbase API '''
    @classmethod
    @docparams(cba.__name__, "setup")
    def setup(cls):
        ''' {0}.{1}'''
        print(__name__, ': TestClass.setup_class() ----------')

    @classmethod
    @docparams(cba.__name__, "teardown")
    def teardown(cls):
        ''' {0}.{1}'''
        print(__name__, ': TestClass.teardown_class() -------')

    @classmethod
    @docparams(cba.__name__, "name")
    def test_name(cls):
        ''' {0}.{1}'''
        ok_(cba.NAME == cls.__name__.replace('Test', ''))

    @classmethod
    @docparams(cba.__name__, "price")
    def test_price(cls):
        ''' {0}.{1}'''
        ok_(
            float(
                cba.get_current_price(base.CCY_DEFAULT, None, None,
                                      cba.HEADER)) > 0.00)

    @classmethod
    @docparams(cba.__name__, "bid")
    def test_bid(cls):
        ''' {0}.{1}'''
        ok_(
            float(cba.get_current_bid(base.CCY_DEFAULT, None, None,
                                      cba.HEADER)) > 0.00)

    @classmethod
    @docparams(cba.__name__, "ask")
    def test_ask(cls):
        ''' {0}.{1}'''
        ok_(float(cba.get_current_ask(base.CCY_DEFAULT, None)) > 0.00)

    @classmethod
    @docparams(cba.__name__, "ticker")
    def test_ticker(cls):
        ''' {0}.{1}'''
        data = json.loads(cba.get_current_ticker(base.CCY_DEFAULT, None))
        ok_(data["pair"] == base.CCY_DEFAULT,
            "pair should be base.CCY_DEFAULT")
        ok_(float(data["ask"]) > 0.00, "ask should not be empty")
        ok_(float(data["bid"]) > 0.00, "bid should not be empty")
        ok_(float(data["bid"]) <= float(data["ask"]), "bid should be < ask")
        ok_(float(data["timestamp"]) > 0, "Timestamp should be > zero")

    @classmethod
    @docparams(cba.__name__, "orders")
    def test_orders(cls):
        ''' {0}.{1}'''
        orders = cba.get_current_orders(base.CCY_DEFAULT)
        ok_(len(orders["asks"]) > 0, "Asks array should not be empty")
        ok_(len(orders["bids"]) > 0, "Bids array should not be empty")
        ok_(orders["source"] == "Coinbase", "Source should be 'Coinbase'")
        ok_(float(orders["timestamp"]) > 0, "Timestamp should be > zero")


if __name__ == '__main__':
    nose.runmodule()
