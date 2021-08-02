''' module for testing Zaif API '''

import nose
import json
from sys import path
from unittest import TestCase
from nose.tools import ok_

libPath = '../hokonui'
if not libPath in path:
    path.append(libPath)

from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.zaif import Zaif as zf
from hokonui.utils.helpers import docstring_parameter as docparams

class TestZaif(TestCase):
    ''' Class for testing Zaif API '''
    @classmethod
    @docparams(zf.__name__, "setup")
    def setup(cls):
        ''' {0}.{1} '''
        print(__name__, ': TestClass.setup_class() ----------')

    @classmethod
    @docparams(zf.__name__, "teardown")
    def teardown(cls):
        ''' {0}.{1} '''
        print(__name__, ': TestClass.teardown_class() -------')

    @classmethod
    @docparams(zf.__name__, "name")
    def test_name(cls):
        ''' {0}.{1} '''

        ok_(zf.NAME == cls.__name__.replace('Test', ''))

    @classmethod
    @docparams(zf.__name__, "price")
    def test_price(cls):
        ''' {0}.{1} '''

        ok_(float(zf.get_current_price(zf.CCY_DEFAULT)) > 0.00)

    @classmethod
    @docparams(zf.__name__, "bid")
    def test_bid(cls):
        ''' {0}.{1} '''

        ok_(float(zf.get_current_bid(zf.CCY_DEFAULT)) > 0.00)

    @classmethod
    @docparams(zf.__name__, "ask")
    def test_ask(cls):
        ''' {0}.{1} '''

        ok_(float(zf.get_current_ask(zf.CCY_DEFAULT)) > 0.00)

    @classmethod
    @docparams(zf.__name__, "ticker")
    def test_ticker(cls):
        ''' {0}.{1} '''

        data = json.loads(zf.get_current_ticker(zf.CCY_DEFAULT))
        ok_(data["pair"] == zf.CCY_DEFAULT,
            "Ccy should be '%s', was '%s'" % (zf.CCY_DEFAULT, data["pair"]))
        ok_(float(data["ask"]) > 0.00, "ask should not be empty")
        ok_(float(data["bid"]) > 0.00, "bid should not be empty")
        ok_(float(data["bid"]) <= float(data["ask"]), "bid should be < ask")
        ok_(float(data["timestamp"]) > 0, "Timestamp should be > zero")

    @classmethod
    @docparams(zf.__name__, "orders")
    def test_orders(cls):
        ''' {0}.{1} '''

        orders = zf.get_current_orders(zf.CCY_DEFAULT)
        ok_(len(orders["asks"]) > 0, "Asks array should not be empty")
        ok_(len(orders["bids"]) > 0, "Bids array should not be empty")
        ok_(orders["source"] == "Zaif", "Source should be 'Zaif'")
        ok_(orders["ccy"] == zf.CCY_DEFAULT,
            "Ccy should be %s" % zf.CCY_DEFAULT)
        ok_(float(orders["timestamp"]) > 0, "Timestamp should be > zero")


if __name__ == '__main__':
    nose.runmodule()
