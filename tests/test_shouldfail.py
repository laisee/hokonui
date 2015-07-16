import nose
from nose.tools import ok_
from nose.tools import assert_raises
from unittest import TestCase

if __package__ is None:
    import sys
    from os import path
    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
    from exchanges.mock import MockExchange as mock
else:
    from ..exchanges.mock import Mock as mock

class TestMockExchange(TestCase):

  def setUp(self):
      print(__name__, ': TestClass.setup_class() ----------')

  def tearDown(self):
      print(__name__, ': TestClass.teardown_class() -------')

  def test_price_fails_no_currency(self):
      with assert_raises(ValueError) as cm:
          mock.get_current_price(None)
      ex = cm.exception # raised exception is available through exception property of context
      ok_(ex.message == "URL https://api.mock.com/v1/markets/XBT%s/ticker should have a currency value supplied")

  def test_ask_fails_no_currency(self):
      with assert_raises(ValueError) as cm:
          mock.get_current_ask(None)
      ex = cm.exception # raised exception is available through exception property of context
      ok_(ex.message == "URL https://api.mock.com/v1/markets/XBT%s/ticker should have a currency value supplied")

  def test_bid_fails_no_currency(self):
      with assert_raises(ValueError) as cm:
          mock.get_current_bid(None)
      ex = cm.exception # raised exception is available through exception property of context
      ok_(ex.message == "URL https://api.mock.com/v1/markets/XBT%s/ticker should have a currency value supplied")

if __name__ == '__main__':
    nosetest.runmodule()
