''' Module for testing Bitstamp exchange '''

import string
import json
from unittest import TestCase
import nose
from nose.tools import ok_
from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.bitstamp import Bitstamp as bts


class TestBitstamp(TestCase):
    ''' Class for testing Bitstamp exchange '''

    @classmethod
    def setUp(cls):
        ''' Method for testing setup '''
        print(__name__, ': TestClass.setup_class() ----------')

    @classmethod
    def tearDown(cls):
        ''' Method for testing teardown '''
        print(__name__, ': TestClass.teardown_class() -------')

    @classmethod
    def test_name(cls):
        ''' Method for testing name '''
        ok_(bts.NAME == string.replace(cls.__name__, 'Test', ''))

    @classmethod
    def test_price(cls):
        ''' Method for testing last price '''
        ok_(bts.get_current_price() > 0.00)

    @classmethod
    def test_bid(cls):
        ''' Method for testing bid prices '''
        ok_(bts.get_current_bid() > 0.00)

    @classmethod
    def test_ask(cls):
        ''' Method for testing ask prices '''
        ok_(bts.get_current_ask() > 0.00)

    @classmethod
    def test_ticker(cls):
        ''' Method for testing ticker '''
        data = json.loads(bts.get_current_ticker())
        ok_(data["pair"] == base.CCY_DEFAULT, "shd be '%s'" % base.CCY_DEFAULT)
        ok_(data["ask"] > 0.00, "ask should not be empty")
        ok_(data["bid"] > 0.00, "bid should not be empty")
        ok_(data["bid"] <= data["ask"], "bid should be < ask")
        ok_(float(data["timestamp"]) > 0, "Timestamp should be > zero")

    @classmethod
    def test_orders(cls):
        ''' Method for testing orders '''
        ok_(bts.get_current_orders() > 0.00)

if __name__ == '__main__':
    nose.runmodule()
