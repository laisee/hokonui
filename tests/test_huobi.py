''' Module for testing Huobi exchange '''

import nose
import json
from sys import path
from unittest import TestCase
from nose.tools import ok_

libPath = '../hokonui'
if not libPath in path:
    path.append(libPath)

from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.huobi import Huobi as hbi
from hokonui.utils.helpers import docstring_parameter as docparams

class TestHuobi(TestCase):
    ''' Class for testing Huobi exchange'''
    @classmethod
    @docparams(hbi.__name__, "name")
    def test_name(cls):
        ''' {0}.{1} '''

        ok_(hbi.NAME == cls.__name__.replace('Test', ''))

    @classmethod
    @docparams(hbi.__name__, "price")
    def test_price(cls):
        ''' {0}.{1} '''

        ok_(float(hbi.get_current_price()) > 0.00)

    @classmethod
    @docparams(hbi.__name__, "bid")
    def test_bid(cls):
        ''' {0}.{1} '''

        ok_(float(hbi.get_current_bid()) > 0.00)

    @classmethod
    @docparams(hbi.__name__, "ask")
    def test_ask(cls):
        ''' {0}.{1} '''

        ok_(float(hbi.get_current_ask()) > 0.00)

    @classmethod
    @docparams(hbi.__name__, "ticker")
    def test_ticker(cls):
        ''' {0}.{1} '''

        data = json.loads(hbi.get_current_ticker())
        ok_(data["pair"] == hbi.CCY_DEFAULT, "shd be '%s'" % hbi.CCY_DEFAULT)
        ok_(float(data["ask"]) > 0.00, "ask should not be empty")
        ok_(float(data["bid"]) > 0.00, "bid should not be empty")
        ok_(float(data["bid"]) <= float(data["ask"]), "bid should be <= ask")
        ok_(float(data["timestamp"]) > 0, "Timestamp should be > zero")

    @classmethod
    @docparams(hbi.__name__, "orders")
    def test_orders(cls):
        ''' {0}.{1} '''

        orders = hbi.get_current_orders(None)
        ok_(len(orders["asks"]) > 0, "Asks array should not be empty")
        ok_(len(orders["bids"]) > 0, "Bids array should not be empty")
        ok_(orders["source"] == "Huobi", "Source should be 'Huobi'")
        ok_(float(orders["timestamp"]) > 0, "Timestamp should be > zero")


if __name__ == '__main__':
    nose.runmodule()
