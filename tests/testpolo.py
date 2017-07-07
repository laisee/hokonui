
''' module for testing Poloniex API '''

import json
import string
from unittest import TestCase
from nose.tools import ok_
import nose
from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.polo import Poloniex as p


class TestPoloniex(TestCase):

    ''' Class for testing Quoine API '''

    @classmethod
    def setup(cls):
        ''' setup method '''
        print(__name__, ': TestClass.setup_class() ----------')

    @classmethod
    def teardown(cls):
        ''' test teardown method '''
        print(__name__, ': TestClass.teardown_class() -------')

    @classmethod
    def test_name(cls):
        ''' name test method '''
        ok_(p.NAME == cls.__name__.replace( 'Test', ''))

    @classmethod
    def test_price(cls):
        ''' last price test method '''
        ok_(float(p.get_current_price()) > 0.00)

    @classmethod
    def test_bid(cls):
        ''' bid price test method '''
        ok_(float(p.get_current_bid()) > 0.00)

    @classmethod
    def test_ask(cls):
        ''' ask price test method '''
        ok_(float(p.get_current_ask()) > 0.00)

    @classmethod
    def test_ticker(cls):
        ''' ticket test method '''

        data = json.loads(p.get_current_ticker())
        ok_(data["pair"] == p.CCY_DEFAULT, "shd be '%s'" % p.CCY_DEFAULT)
        ok_(float(data["ask"]) > 0.00, "ask should not be empty")
        ok_(float(data["bid"]) > 0.00, "bid should not be empty")
        ok_(float(data["bid"]) <= float(data["ask"]), "bid should be < ask")
        ok_(float(data["timestamp"]) > 0, "Timestamp should be > zero")

    @classmethod
    def test_orders(cls):
        ''' orders test method '''
        orders = p.get_current_orders(p.CCY_DEFAULT)
        ok_(len(orders["asks"]) > 0, "Asks array should not be empty")
        ok_(len(orders["bids"]) > 0, "Bids array should not be empty")
        ok_(orders["source"] == "Poloniex", "Source should be 'Poloniex'")
        ok_(float(orders["timestamp"]) > 0, "Timestamp should be > zero")


if __name__ == '__main__':
    nose.runmodule()
