''' Module for testing BitFlyer API '''

import nose
import json
from sys import path
from unittest import TestCase
from nose.tools import ok_

libPath = '../hokonui'
if not libPath in path:
    path.append(libPath)


from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.bitflyer import BitFlyer as btf
from hokonui.utils.helpers import docstring_parameter as docparams


class TestBitFlyer(TestCase):
    ''' Class for testing Bitflyer API '''

    TEST_CCY = "BTC_JPY"

    @classmethod
    @docparams(btf.__name__, "setup")
    def setUp(cls):
        ''' {0}.{1} '''
        print(__name__, ': TestClass.setup_class() ----------')

    @classmethod
    @docparams(btf.__name__, "teardown")
    def tearDown(cls):
        ''' {0}.{1} '''
        print(__name__, ': TestClass.teardown_class() -------')

    @classmethod
    @docparams(btf.__name__, "name")
    def test_name(cls):
        ''' {0}.{1}'''
        ok_(btf.NAME == cls.__name__.replace('Test', ''))

    @classmethod
    @docparams(btf.__name__, "price")
    def test_price(cls):
        ''' {0}.{1}'''
        ok_(float(btf.get_current_price(cls.TEST_CCY)) > 0.00)

    @classmethod
    @docparams(btf.__name__, "bid")
    def test_bid(cls):
        ''' {0}.{1}'''
        ok_(float(btf.get_current_bid(cls.TEST_CCY)) > 0.00)

    @classmethod
    @docparams(btf.__name__, "ask")
    def test_ask(cls):
        ''' {0}.{1}'''
        ok_(float(btf.get_current_ask(cls.TEST_CCY)) > 0.00)

    @classmethod
    @docparams(btf.__name__, "ticker")
    def test_ticker(cls):
        ''' {0}.{1}'''
        data = json.loads(btf.get_current_ticker(cls.TEST_CCY))
        ok_(data["pair"] == base.CCY_DEFAULT, "shd be '%s'" % base.CCY_DEFAULT)
        ok_(float(data["ask"]) > 0.00, "ask should not be empty")
        ok_(float(data["bid"]) > 0.00, "bid should not be empty")
        ok_(float(data["bid"]) <= float(data["ask"]), "bid should be < ask")
        ok_(float(data["timestamp"]) > 0, "Timestamp should be > zero")

    @classmethod
    @docparams(btf.__name__, "orders")
    def test_orders(cls):
        ''' {0}.{1}'''
        orders = btf.get_current_orders(cls.TEST_CCY)
        ok_(len(orders["asks"]) > 0, "Asks array should not be empty")
        ok_(len(orders["bids"]) > 0, "Bids array should not be empty")
        ok_(orders["source"] == "BitFlyer", "Source should be 'BitFlyer'")
        ok_(float(orders["timestamp"]) > 0, "Timestamp should be > zero")


if __name__ == '__main__':
    nose.runmodule()
