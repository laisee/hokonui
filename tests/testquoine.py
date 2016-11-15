
''' module for testing Quoine API '''

import json
import string
from unittest import TestCase
from nose.tools import ok_
import nose
from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.quoine import Quoine as q


class TestQuoine(TestCase):

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
        ok_(q.NAME == string.replace(cls.__name__, 'Test', ''))

    @classmethod
    def test_price(cls):
        ''' last price test method '''
        ok_(q.get_current_price(base.CCY_DEFAULT) > 0.00)

    @classmethod
    def test_bid(cls):
        ''' bid price test method '''
        ok_(q.get_current_bid(base.CCY_DEFAULT) > 0.00)

    @classmethod
    def test_ask(cls):
        ''' ask price test method '''
        ok_(q.get_current_ask(base.CCY_DEFAULT) > 0.00)

    @classmethod
    def test_ticker(cls):
        ''' ticket test method '''

        data = json.loads(q.get_current_ticker(base.CCY_DEFAULT))
        ok_(data["pair"] == base.CCY_DEFAULT, "shd be '%s'" % base.CCY_DEFAULT)
        ok_(data["ask"] > 0.00, "ask should not be empty")
        ok_(data["bid"] > 0.00, "bid should not be empty")
        ok_(data["bid"] <= data["ask"], "bid should be < ask")
        ok_(float(data["timestamp"]) > 0, "Timestamp should be > zero")

    @classmethod
    def test_orders(cls):
        ''' orders test method '''
        ccy_id = cls.CcyToId(base.CCY_DEFAULT)
        orders = q.get_current_orders(ccy_id)
        ok_(len(orders["asks"]) > 0, "Asks array should not be empty")
        ok_(len(orders["bids"]) > 0, "Bids array should not be empty")
        ok_(orders["source"] == "Quoine", "Source should be 'Quoine'")
        ok_(float(orders["timestamp"]) > 0, "Timestamp should be > zero")

    @staticmethod
    def CcyToId(ccy):
        ''' static method for converting CCY string to ID value '''

        ccyid = -1
        if ccy == 'USD':
            ccyid = 1
        elif ccy == 'EUR':
            ccyid = 3
        elif ccy == 'JPY':
            ccyid = 5
        elif ccy == 'SGD':
            ccyid = 7
        elif ccy == 'HKD':
            ccyid = 9
        elif ccy == 'IDR':
            ccyid = 11
        elif ccy == 'AUD':
            ccyid = 13
        elif ccy == 'PHP':
            ccyid = 15
        elif ccy == 'CNY':
            ccyid = 17
        elif ccy == 'INR':
            ccyid = 18
        else:
            raise ValueError("Invalid Currency : %s " % ccy)
        return ccyid

if __name__ == '__main__':
    nose.runmodule()
