''' Module for testing Birfinex API '''

import string
import json
from unittest import TestCase
import nose
from nose.tools import ok_
from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.bitfinex import Bitfinex as bfx


class TestBitfinex(TestCase):
    ''' Class for testing Bitfinex API '''

    @classmethod
    def test_name(cls):
        ''' Method for testing name '''
        ok_(bfx.NAME == string.replace(cls.__name__, 'Test', ''))

    @classmethod
    def test_price(cls):
        ''' Method for testing last price '''
        ok_(bfx.get_current_price(base.CCY_DEFAULT) > 0.00)

    @classmethod
    def test_bid(cls):
        ''' Method for testing bid price '''
        ok_(bfx.get_current_bid(base.CCY_DEFAULT) > 0.00)

    @classmethod
    def test_ask(cls):
        ''' Method for testing ask price '''
        ok_(bfx.get_current_ask(base.CCY_DEFAULT) > 0.00)

    @classmethod
    def test_ticker(cls):
        ''' Method for testing ticker '''
        data = json.loads(bfx.get_current_ticker(base.CCY_DEFAULT))
        ok_(data["pair"] == base.CCY_DEFAULT, "shd be '%s'" % base.CCY_DEFAULT)
        ok_(data["ask"] > 0.00, "ask should not be empty")
        ok_(data["bid"] > 0.00, "bid should not be empty")
        ok_(data["bid"] <= data["ask"], "bid should be < ask")
        ok_(float(data["timestamp"]) > 0, "Timestamp should be > zero")

    @classmethod
    def test_orders(cls):
        ''' Method for testing orders '''
        orders = bfx.get_current_orders(base.CCY_DEFAULT)
        ok_(len(orders["asks"]) > 0, "Asks array should not be empty")
        ok_(len(orders["bids"]) > 0, "Bids array should not be empty")
        ok_(orders["source"] == "Bitfinex", "Source should be 'Bitfinex'")
        ok_(float(orders["timestamp"]) > 0, "Timestamp should be > zero")

if __name__ == '__main__':
    nose.runmodule()
