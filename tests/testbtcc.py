''' Module for testing BTCC exchange '''
import json
import string
from unittest import TestCase
import nose
from nose.tools import ok_
from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.btcc import BTCC as btcc


class TestBTCC(TestCase):
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
        ok_(btcc.NAME == string.replace(cls.__name__, 'Test', ''))

    @classmethod
    def test_price(cls):
        ''' Method for testing last price '''
        ok_(btcc.get_current_price() > 0.00)

    @classmethod
    def test_bid(cls):
        ''' Method for testing bid price '''
        ok_(btcc.get_current_bid() > 0.00)

    @classmethod
    def test_ask(cls):
        ''' Method for testing ask price '''
        ok_(btcc.get_current_ask() > 0.00)

    @classmethod
    def test_ticker(cls):
        ''' Method for testing ticker '''
        data = json.loads(btcc.get_current_ticker())
        ok_(data["pair"] == base.CCY_DEFAULT, "shd be '%s'" % base.CCY_DEFAULT)
        ok_(data["ask"] > 0.00, "ask should not be empty")
        ok_(data["bid"] > 0.00, "bid should not be empty")
        ok_(data["bid"] <= data["ask"], "bid should be <= ask")
        ok_(float(data["timestamp"]) > 0, "Timestamp should be > zero")

    @classmethod
    def test_orders(cls):
        ''' Method for testing orders '''
        orders = btcc.get_current_orders()
        ok_(len(orders["asks"]) > 0, "Asks array should not be empty")
        ok_(len(orders["bids"]) > 0, "Bids array should not be empty")
        ok_(orders["source"] == "BTCC", "Source should be 'BTCC'")
        ok_(float(orders["timestamp"]) > 0, "Timestamp should be > zero")

if __name__ == '__main__':
    nose.runmodule()
