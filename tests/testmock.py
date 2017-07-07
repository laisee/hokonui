''' Module for testing Mock Exchange '''
import string
import unittest
from unittest import TestCase
from nose.tools import ok_
from nose.tools import assert_raises
import nose
from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.mock import MockExchange as mock


class TestMockExchange(TestCase):
    ''' Class for testing Mock Exchange '''

    @classmethod
    def setUp(cls):
        ''' Method for test setup '''
        print(__name__, ': TestClass.setup_class() ----------')

    @classmethod
    def tearDown(cls):
        ''' Method for test teardown '''
        print(__name__, ': TestClass.teardown_class() -------')

    @classmethod
    def test_name(cls):
        ''' Method for testing name '''
        ok_(mock.NAME == cls.__name__.replace( 'Test', ''))

    @classmethod
    @unittest.skip("skip while building mock service")
    def test_ask(cls):
        ''' Method for testing ask price '''
        with assert_raises(ValueError) as cme:
            mock.get_current_ask(base.CCY_DEFAULT)
        ex = cme.exception
        ok_(ex.message == "Not implemented yet")

    @classmethod
    @unittest.skip("skip while building mock service")
    def test_bid(cls):
        ''' Method for testing bid price '''
        with assert_raises(ValueError) as cme:
            mock.get_current_bid(base.CCY_DEFAULT)
        ex = cme.exception
        ok_(ex.message == "Not implemented yet")

    @classmethod
    @unittest.skip("skip while building mock service")
    def test_orders(cls):
        ''' Method for testing orders '''
        with assert_raises(ValueError) as cme:
            mock.get_current_orders(base.CCY_DEFAULT)
        ex = cme.exception
        ok_(ex.message == "Not implemented yet")

if __name__ == '__main__':
    nose.runmodule()
