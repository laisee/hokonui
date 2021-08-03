''' Module for testing crypto facilities API '''

import json
from sys import path
from unittest import TestCase
from nose.tools import ok_
import nose
from hokonui.exchanges.cryptofac import CryptoFacility as cfc
from hokonui.utils.helpers import docstring_parameter as docparams


LIBPATH = '../hokonui'
if LIBPATH not in path:
    path.append(LIBPATH)


class TestCryptoFacility(TestCase):
    ''' Class for testing crypto facilities API '''

    SYMBOL = 'fi_xbtusd_180615'

    @classmethod
    @docparams(cfc.__name__, "setup")
    def setUp(cls):
        ''' {0}.{1} '''

        print(__name__, ': TestClass.setup_class() ----------')

    @classmethod
    @docparams(cfc.__name__, "teardown")
    def tearDown(cls):
        ''' {0}.{1} '''

        print(__name__, ': TestClass.teardown_class() -------')

    @classmethod
    @docparams(cfc.__name__, "name")
    def test_name(cls):
        ''' {0}.{1} '''

        ok_(cfc.NAME == cls.__name__.replace('Test', ''))

    @classmethod
    @docparams(cfc.__name__, "price")
    def test_price(cls):
        ''' {0}.{1} '''

        ok_(float(cfc.get_current_price()) > 0.00)

    @classmethod
    @docparams(cfc.__name__, "bid")
    def test_bid(cls):
        ''' {0}.{1} '''

        ok_(float(cfc.get_current_bid()) > 0.00)

    @classmethod
    @docparams(cfc.__name__, "ask")
    def test_ask(cls):
        ''' {0}.{1} '''

        ok_(float(cfc.get_current_ask()) > 0.00)

    @classmethod
    @docparams(cfc.__name__, "ticker")
    def test_ticker(cls):
        ''' {0}.{1} '''

        data = json.loads(cfc.get_current_ticker())
        ok_(data["pair"] == cfc.CCY_DEFAULT, "shd be '%s'" % cfc.CCY_DEFAULT)
        ok_(float(data["ask"]) > 0.00, "ask shd not be empty")
        ok_(float(data["bid"]) > 0.00, "bid shd not be empty")
        ok_(float(data["bid"]) <= float(data["ask"]), "bid shd be <= ask")
        ok_(float(data["timestamp"]) > 0, "Timestamp should be > zero")

    @classmethod
    @docparams(cfc.__name__, "orders")
    def test_orders(cls):
        ''' {0}.{1} '''

        orders = cfc.get_current_orders(cls.SYMBOL)
        #ok_(len(orders["asks"]) > 0, "Asks array shd not be empty")
        #ok_(len(orders["bids"]) > 0, "Bids array shd not be empty")
        ok_(orders["source"] == "CryptoFacility", "Src shd = 'CryptoFacility'")
        ok_(float(orders["timestamp"]) > 0, "Timestamp shd be > zero")


if __name__ == '__main__':
    nose.runmodule()
