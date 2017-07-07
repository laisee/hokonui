''' Module for testing Huobi exchange '''
import string
import json
from unittest import TestCase
from nose.tools import ok_
import nose

from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.huobi import Huobi as hbi


class TestHuobi(TestCase):
    ''' Class for testing Huobi exchange'''

    @classmethod
    def test_name(cls):
        ''' Method for testing name '''
        ok_(hbi.NAME == cls.__name__.replace( 'Test', ''))

    @classmethod
    def test_price(cls):
        ''' Method for testing last price '''
        ok_(float(hbi.get_current_price()) > 0.00)

    @classmethod
    def test_bid(cls):
        ''' Method for testing bid price '''
        ok_(float(hbi.get_current_bid()) > 0.00)

    @classmethod
    def test_ask(cls):
        ''' Method for testing ask price '''
        ok_(float(hbi.get_current_ask()) > 0.00)

    @classmethod
    def test_ticker(cls):
        ''' Method for testing ticker '''
        data = json.loads(hbi.get_current_ticker())
        ok_(data["pair"] == base.CCY_DEFAULT, "shd be '%s'" % base.CCY_DEFAULT)
        ok_(float(data["ask"]) > 0.00, "ask should not be empty")
        ok_(float(data["bid"]) > 0.00, "bid should not be empty")
        ok_(float(data["bid"]) <= float(data["ask"]), "bid should be <= ask")
        ok_(float(data["timestamp"]) > 0, "Timestamp should be > zero")

    @classmethod
    def test_orders(cls):
        ''' Method for testing orders '''
        orders = hbi.get_current_orders(None, 20)
        ok_(len(orders["asks"]) > 0, "Asks array should not be empty")
        ok_(len(orders["bids"]) > 0, "Bids array should not be empty")
        ok_(orders["source"] == "Huobi", "Source should be 'Huobi'")
        ok_(float(orders["timestamp"]) > 0, "Timestamp should be > zero")

if __name__ == '__main__':
    nose.runmodule()
