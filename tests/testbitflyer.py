''' Module for testing BitFlyer API '''
import string
import json
from unittest import TestCase
from nose.tools import ok_
import nose
from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.bitflyer import BitFlyer as btf


class TestBitFlyer(TestCase):
    ''' Class for testing Bitflyer API '''

    TEST_CCY = "BTC_JPY"

    @classmethod
    def setUp(cls):
        ''' Method for testing setup '''
        print(__name__, ': TestClass.setup_class() ----------')

    @classmethod
    def tearDown(cls):
        ''' Method for testing teardonw '''
        print(__name__, ': TestClass.teardown_class() -------')

    @classmethod
    def test_name(cls):
        ''' Method for testing name '''
        ok_(btf.NAME == string.replace(cls.__name__, 'Test', ''))

    @classmethod
    def test_price(cls):
        ''' Method for testing last price '''
        ok_(btf.get_current_price(cls.TEST_CCY) > 0.00)

    @classmethod
    def test_bid(cls):
        ''' Method for testing bid price '''
        ok_(btf.get_current_bid(cls.TEST_CCY) > 0.00)

    @classmethod
    def test_ask(cls):
        ''' Method for testing ask price '''
        ok_(btf.get_current_ask(cls.TEST_CCY) > 0.00)

    @classmethod
    def test_ticker(cls):
        ''' Method for testing ticker '''
        data = json.loads(btf.get_current_ticker(cls.TEST_CCY))
        ok_(data["pair"] == base.CCY_DEFAULT, "shd be '%s'" % base.CCY_DEFAULT)
        ok_(data["ask"] > 0.00, "ask should not be empty")
        ok_(data["bid"] > 0.00, "bid should not be empty")
        ok_(data["bid"] <= data["ask"], "bid should be < ask")
        ok_(float(data["timestamp"]) > 0, "Timestamp should be > zero")

    @classmethod
    def test_orders(cls):
        ''' Method for testing orders '''
        orders = btf.get_current_orders(cls.TEST_CCY)
        ok_(len(orders["asks"]) > 0, "Asks array should not be empty")
        ok_(len(orders["bids"]) > 0, "Bids array should not be empty")
        ok_(orders["source"] == "BitFlyer", "Source should be 'BitFlyer'")
        ok_(float(orders["timestamp"]) > 0, "Timestamp should be > zero")

if __name__ == '__main__':
    nose.runmodule()
