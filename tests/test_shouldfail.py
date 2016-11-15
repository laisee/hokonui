''' Module for tests that should always fail '''
from unittest import TestCase
from nose.tools import ok_
from nose.tools import assert_raises
import nose

from hokonui.exchanges.mock import MockExchange as mock


class TestMockExchange(TestCase):
    ''' Class for executing tests that should always fail '''

    @classmethod
    def setup(cls):
        ''' method for test setup '''
        print(__name__, ': TestClass.setup_class() ----------')

    @classmethod
    def teardown(cls):
        ''' method for test teardown '''
        print(__name__, ': TestClass.teardown_class() -------')

    @classmethod
    def test_exchange_name(cls):
        ''' method for testing name '''
        ok_(mock.NAME != '')

    @classmethod
    def test_price_fails_no_currency(cls):
        ''' method for testing no ccy '''
        msg = "URL https://api.mock.com/XBT%s/ticker should have a currency value supplied"
        with assert_raises(ValueError) as cme:
            mock.get_current_price(None)
        ex = cme.exception
        ok_(ex.message == msg, "error %s should be %s " % (ex.message, msg))

    @classmethod
    def test_ask_fails_no_currency(cls):
        ''' method for testing no ask price '''
        msg = "URL https://api.mock.com/XBT%s/ticker should have a currency value supplied"
        with assert_raises(ValueError) as cme:
            mock.get_current_ask(None)
        ex = cme.exception
        ok_(ex.message == msg, "error %s should be %s " % (ex.message, msg))

    @classmethod
    def test_bid_fails_no_currency(cls):
        ''' method for testing no bid price '''
        msg = "URL https://api.mock.com/XBT%s/ticker should have a currency value supplied"
        with assert_raises(ValueError) as cme:
            mock.get_current_bid(None)
        ex = cme.exception
        ok_(ex.message == msg, "error %s should be %s " % (ex.message, msg))

if __name__ == '__main__':
    nose.runmodule()
