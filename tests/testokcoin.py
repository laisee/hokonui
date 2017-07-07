''' Module for testing Ok Coin API '''

import json
from unittest import TestCase
import nose
from nose.tools import ok_
from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.okcoin import OKCoin as okc


class TestOkCoin(TestCase):
    ''' Class for testing OkCoin API '''


def test_name():
    ''' Method for testing last price '''
    ok_(okc.__name__ != "")

def test_price():
    ''' Method for testing last price '''
    ok_(float(okc.get_current_price()) > 0.00)


def test_bid():
    ''' Method for testing bid price '''
    ok_(float(okc.get_current_bid()) > 0.00)


def test_ask():
    ''' Method for testing ask price '''
    ok_(float(okc.get_current_ask()) > 0.00)


def test_ticker():
    ''' Method for testing ticker '''
    data = json.loads(okc.get_current_ticker())
    ok_(data["pair"] == base.CCY_DEFAULT, "shd be '%s'" % base.CCY_DEFAULT)
    ok_(float(data["ask"]) > 0.00, "ask should not be empty")
    ok_(float(data["bid"]) > 0.00, "bid should not be empty")
    ok_(float(data["bid"]) <= float(data["ask"]), "bid should be <= ask")
    ok_(float(data["timestamp"]) > 0, "Timestamp should be greater than zero")


def test_orders():
    ''' Method for testing orders '''
    orders = okc.get_current_orders()
    ok_(len(orders["asks"]) > 0, "Asks array should not be empty")
    ok_(len(orders["bids"]) > 0, "Bids array should not be empty")
    ok_(orders["source"] == "OKCoin", "Source should be 'OKCoin'")
    ok_(float(orders["timestamp"]) > 0, "Timestamp should be > zero")

if __name__ == '__main__':
    nose.runmodule()
