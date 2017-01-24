''' Module for testing BTCE exchange '''

import string
import json
from unittest import TestCase
from nose.tools import ok_
import nose
from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.btce import BTCE as btce


class TestBTCE(TestCase):
    ''' Class for testing BTCE exchange '''

    @classmethod
    def setUp(cls):
        ''' Method for test setup '''
        print(__name__, ': TestClass.setup_class() ----------')

    @classmethod
    def tearDown(cls):
        ''' Method for test setup '''
        print(__name__, ': TestClass.teardown_class() -------')

    @classmethod
    def test_name(cls):
        ''' Method for testing name '''
        ok_(btce.NAME == string.replace(cls.__name__, 'Test', ''))

    @classmethod
    def test_price(cls):
        ''' Method for testing last price '''
        ok_(btce.get_current_price() > 0.00)

    @classmethod
    def test_bid(cls):
        ''' Method for testing bid price'''
        ok_(btce.get_current_bid() > 0.00)

    @classmethod
    def test_ask(cls):
        ''' Method for testing ask price'''
        ok_(btce.get_current_ask() > 0.00)

    @classmethod
    def test_bid_lt_ask(cls):
        ''' Method for testing bid < ask'''
        bid = btce.get_current_bid()
        ask = btce.get_current_ask()
        ok_(bid > ask, "bid should be > ask on BTC-E only - Bid : %s Ask %s " % (bid, ask))

    @classmethod
    def test_ticker(cls):
        ''' Method for testing ticker'''
        data = json.loads(btce.get_current_ticker())
        bid = btce.get_current_bid()
        ask = btce.get_current_ask()
        ok_(data["pair"] == base.CCY_DEFAULT, "shd be '%s'" % base.CCY_DEFAULT)
        ok_(ask > 0.00, "ask should not be empty")
        ok_(bid > 0.00, "bid should not be empty")
        ok_(bid > ask, "bid should be > ask - Bid : %s Ask %s " % (bid, ask))
        ok_(float(data["timestamp"]) > 0, "Timestamp should be > zero")

    @classmethod
    def test_orders(cls):
        ''' Method for testing orders'''
        orders = btce.get_current_orders()
        ok_(len(orders["asks"]) > 0, "Asks array should not be empty")
        ok_(len(orders["bids"]) > 0, "Bids array should not be empty")
        ok_(orders["source"] == "BTCE", "Source should be 'BTCE'")
        ok_(float(orders["timestamp"]) > 0, "Timestamp should be > zero")

if __name__ == '__main__':
    nose.runmodule()