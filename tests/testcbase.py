''' Module for testing CoinBasse API '''

import string
import json
from unittest import TestCase
import nose
from nose.tools import ok_
from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.coinbase import CoinBase as cba


class TestCoinBase(TestCase):
    ''' Class for testing Coinbase API '''

    @classmethod
    def setup(cls):
        ''' method for testing setup'''
        print(__name__, ': TestClass.setup_class() ----------')

    @classmethod
    def teardown(cls):
        ''' method for testing teardown'''
        print(__name__, ': TestClass.teardown_class() -------')

    @classmethod
    def test_name(cls):
        ''' method for testing name'''
        ok_(cba.NAME == string.replace(cls.__name__, 'Test', ''))

    @classmethod
    def test_price(cls):
        ''' method for testing last price'''
        ok_(cba.get_current_price(base.CCY_DEFAULT, None) > 0.00)

    @classmethod
    def test_bid(cls):
        ''' method for testing bid price'''
        ok_(cba.get_current_bid(base.CCY_DEFAULT, None) > 0.00)

    @classmethod
    def test_ask(cls):
        ''' method for testing ask price'''
        ok_(cba.get_current_ask(base.CCY_DEFAULT, None) > 0.00)

    @classmethod
    def test_ticker(cls):
        ''' method for testing ticker'''
        data = json.loads(cba.get_current_ticker(base.CCY_DEFAULT, None))
        ok_(data["pair"] == base.CCY_DEFAULT, "pair should be base.CCY_DEFAULT")
        ok_(data["ask"] > 0.00, "ask should not be empty")
        ok_(data["bid"] > 0.00, "bid should not be empty")
        ok_(data["bid"] <= data["ask"], "bid should be < ask")
        ok_(float(data["timestamp"]) > 0, "Timestamp should be > zero")

    @classmethod
    def test_orders(cls):
        ''' method for testing orders'''
        orders = cba.get_current_orders(base.CCY_DEFAULT)
        ok_(len(orders["asks"]) > 0, "Asks array should not be empty")
        ok_(len(orders["bids"]) > 0, "Bids array should not be empty")
        ok_(orders["source"] == "CoinBase", "Source should be 'CoinBase'")
        ok_(float(orders["timestamp"]) > 0, "Timestamp should be > zero")

if __name__ == '__main__':
    nose.runmodule()
