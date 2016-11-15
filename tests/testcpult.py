''' Module for testing Coinapult exchange '''

import string
from unittest import TestCase
import nose
from nose.tools import ok_
from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.coinapult import Coinapult as cplt


class TestCoinapult(TestCase):
    ''' Class for testing Coinapult exchange '''

    @classmethod
    def test_name(cls):
        ''' Method for testing name '''
        ok_(cplt.NAME == string.replace(cls.__name__, 'Test', ''))

    @classmethod
    def test_price(cls):
        ''' Method for testing last price '''
        ok_(cplt.get_current_price(base.CCY_DEFAULT) > 0.00)

    @classmethod
    def test_bid(cls):
        ''' Method for testing bid price '''
        ok_(cplt.get_current_bid(base.CCY_DEFAULT) > 0.00)

    @classmethod
    def test_ask(cls):
        ''' Method for testing ask price '''
        ok_(cplt.get_current_ask(base.CCY_DEFAULT) > 0.00)

    @classmethod
    def test_bid_lt_ask(cls):
        ''' Method for testing bid price < ask price '''
        bid = cplt.get_current_bid(base.CCY_DEFAULT)
        ask = cplt.get_current_ask(base.CCY_DEFAULT)
        ok_(bid < ask, "bid should be < ask")

if __name__ == '__main__':
    nose.runmodule()
