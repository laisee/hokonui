''' Module for testing BTCC exchange '''
import time
import json
import string
from unittest import TestCase
import nose
from nose.tools import ok_
from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.btcxindia import BtcXIndia as btcxindia


class TestBtcXIndia(TestCase):
    ''' Class for testing BTCC exchange '''

    @classmethod
    def setUp(cls):
        ''' Method for test setup'''
        print(__name__, ': TestClass.setup_class() ----------')

    @classmethod
    def tearDown(cls):
        ''' Method for test teardown'''
        print(__name__, ': TestClass.teardown_class() -------')

    @classmethod
    def test_name(cls):
        ''' Method for testing name'''
        ok_(btcxindia.NAME == cls.__name__.replace( 'Test', ''))

    @classmethod
    def test_price(cls):
        ''' Method for testing last price '''
        time.sleep(5)
        ok_(float(btcxindia.get_current_price()) > 0.00)

    @classmethod
    def test_bid(cls):
        ''' Method for testing bid price '''
        time.sleep(5)
        ok_(float(btcxindia.get_current_bid()) > 0.00)

    @classmethod
    def test_ask(cls):
        ''' Method for testing ask price '''
        time.sleep(5)
        ok_(float(btcxindia.get_current_ask()) > 0.00)

    @classmethod
    def test_ticker(cls):
        ''' Method for testing ticker '''
        time.sleep(5)
        data = json.loads(btcxindia.get_current_ticker())
        ok_(data["pair"] == base.CCY_DEFAULT, "shd be '%s'" % base.CCY_DEFAULT)
        ok_(float(data["ask"]) > 0.00, "ask should not be empty")
        ok_(float(data["bid"]) > 0.00, "bid should not be empty")
        ok_(float(data["bid"]) <= float(data["ask"]), "bid should be <= ask")
        ok_(float(data["timestamp"]) > 0, "Timestamp should be > zero")

    @classmethod
    def test_orders(cls):
        ''' Method for testing orders '''
        time.sleep(5)
        orders = btcxindia.get_current_orders()
        ok_(len(orders["asks"]) > 0, "Asks array should not be empty")
        ok_(len(orders["bids"]) > 0, "Bids array should not be empty")
        ok_(orders["source"] == "BtcXIndia", "Source should be 'BtcXIndia'")
        ok_(float(orders["timestamp"]) > 0, "Timestamp should be > zero")

if __name__ == '__main__':
    nose.runmodule()
