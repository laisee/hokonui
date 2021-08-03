''' Module for testing Kraken API '''


import json
from sys import path
from unittest import TestCase
from nose.tools import ok_
import nose
from hokonui.exchanges.kraken import Kraken as kraken
from hokonui.utils.helpers import docstring_parameter as docparams


LIBPATH = '../hokonui'
if LIBPATH not in path:
    path.append(LIBPATH)

class TestKraken(TestCase):
    ''' Class for testing Kraken API '''
    @classmethod
    @docparams(kraken.__name__, "setup")
    def setUp(cls):
        ''' {0}.{1}'''
        print(__name__, ': TestClass.setup_class() ----------')

    @classmethod
    @docparams(kraken.__name__, "teardown")
    def tearDown(cls):
        ''' {0}.{1}'''
        print(__name__, ': TestClass.teardown_class() -------')

    @classmethod
    @docparams(kraken.__name__, "name")
    def test_name(cls):
        ''' {0}.{1}'''
        ok_(kraken.NAME == cls.__name__.replace('Test', ''))

    @classmethod
    @docparams(kraken.__name__, "price")
    def test_price(cls):
        ''' {0}.{1}'''
        body = '{"pair":"XXBTZUSD"}'
        ok_(float(kraken.get_current_price(None, None, body)) > 0.00)

    @classmethod
    @docparams(kraken.__name__, "bid")
    def test_bid(cls):
        ''' {0}.{1}'''
        body = '{"pair":"XXBTZJPY"}'
        ok_(float(kraken.get_current_bid(None, None, body)) > 0.00)

    @classmethod
    @docparams(kraken.__name__, "ask")
    def test_ask(cls):
        ''' {0}.{1}'''
        body = '{"pair":"XXBTZJPY"}'
        ok_(float(kraken.get_current_ask(None, None, body)) > 0.00)

    @classmethod
    @docparams(kraken.__name__, "ticker")
    def test_ticker(cls):
        ''' {0}.{1}'''
        body = '{"pair":"XXBTZJPY"}'
        data = json.loads(kraken.get_current_ticker(None, None, body))
        ok_(data["pair"] == 'XXBTZJPY', "pair should be 'XXBTZJPY'")
        ok_(float(data["ask"]) > 0.00, "ask should not be empty")
        ok_(float(data["bid"]) > 0.00, "bid should not be empty")
        ok_(float(data["bid"]) <= float(data["ask"]), "bid should be <= ask")
        ok_(float(data["timestamp"]) > 0, "Timestamp should be > zero")

    @classmethod
    @docparams(kraken.__name__, "orders")
    def test_orders(cls):
        ''' {0}.{1}'''
        body = '{"pair":"XXBTZJPY", "count":"10"}'
        orders = kraken.get_current_orders(None, None, body, 25)
        ok_(len(orders["asks"]) > 0, "Asks array should not be empty")
        ok_(len(orders["bids"]) > 0, "Bids array should not be empty")
        ok_(orders["source"] == "Kraken", "Source should be 'Kraken'")
        ok_(float(orders["timestamp"]) > 0, "Timestamp should be > zero")


if __name__ == '__main__':
    nose.runmodule()
