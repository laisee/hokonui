''' Module for testing BitX API '''

import string
import json
from unittest import TestCase
import nose
from nose.tools import ok_
from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.bitx import BitX as btx


class TestBitX(TestCase):
    ''' Class for testing BitX API '''

    TEST_CCY = 'ZAR'

    @classmethod
    def setup(cls):
        ''' method for testing setup '''
        print(__name__, ': TestClass.setup_class() ----------')

    @classmethod
    def teardown(cls):
        ''' method for testing teardown '''
        print(__name__, ': TestClass.teardown_class() -------')

    @classmethod
    def test_name(cls):
        ''' method for testing name '''
        ok_(btx.NAME == string.replace(cls.__name__, 'Test', ''))

    @classmethod
    def test_price(cls):
        ''' method for testing last price '''
        ok_(btx.get_current_price(cls.TEST_CCY) > 0.00)

    @classmethod
    def test_bid(cls):
        ''' method for testing bid price '''
        ok_(btx.get_current_bid(cls.TEST_CCY) > 0.00)

    @classmethod
    def test_ask(cls):
        ''' method for testing ask price '''
        ok_(btx.get_current_ask(cls.TEST_CCY) > 0.00)

    @classmethod
    def test_ticker(cls):
        ''' method for testing ticker '''
        data = json.loads(btx.get_current_ticker(cls.TEST_CCY))
        ok_(data["pair"] == base.CCY_DEFAULT, "shd be '%s'" % cls.TEST_CCY)
        ok_(data["ask"] > 0.00, "ask should not be empty")
        ok_(data["bid"] > 0.00, "bid should not be empty")
        ok_(data["bid"] <= data["ask"], "bid should be < ask")
        ok_(float(data["timestamp"]) > 0, "Timestamp should be > zero")

    @classmethod
    def test_orders(cls):
        ''' method for testing orders '''
        orders = btx.get_current_orders(cls.TEST_CCY)
        ok_(len(orders["asks"]) > 0, "Asks array should not be empty")
        ok_(len(orders["bids"]) > 0, "Bids array should not be empty")
        ok_(orders["source"] == "BitX", "Source should be 'BitX'")
        ok_(float(orders["timestamp"]) > 0, "Timestamp should be > zero")

if __name__ == '__main__':
    nose.runmodule()
