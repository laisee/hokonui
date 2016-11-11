import string
import nose
from nose.tools import ok_
from nose.tools import assert_raises
from unittest import TestCase
from context import hokonui
from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.mock import MockExchange as mock

class TestMockExchange(TestCase):

  def setUp(self):
      print(__name__, ': TestClass.setup_class() ----------')

  def tearDown(self):
      print(__name__, ': TestClass.teardown_class() -------')

  def test_name(self):
      ok_(mock.NAME==string.replace(type(self).__name__,'Test',''))

  def test_ask(self):
      with assert_raises(ValueError) as cm:
          mock.get_current_ask(base.CCY_DEFAULT)
      ex = cm.exception # raised exception is available through exception property of context
      ok_(ex.message == "Not implemented yet")

  def test_bid(self):
      with assert_raises(ValueError) as cm:
          mock.get_current_bid(base.CCY_DEFAULT)
      ex = cm.exception # raised exception is available through exception property of context
      ok_(ex.message == "Not implemented yet")

  def test_orders(self):
      with assert_raises(ValueError) as cm:
          mock.get_current_orders(base.CCY_DEFAULT)
      ex = cm.exception # raised exception is available through exception property of context
      ok_(ex.message == "Not implemented yet")

if __name__ == '__main__':
    nose.runmodule()
    print str(base)
