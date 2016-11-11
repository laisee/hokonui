import string
import nose
import json
from nose.tools import ok_
from unittest import TestCase
from context import hokonui
from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.bitstamp import Bitstamp as bts 

class TestBitstamp(TestCase):

  def setUp(self):
      print(__name__, ': TestClass.setup_class() ----------')
 
  def tearDown(self):
      print(__name__, ': TestClass.teardown_class() -------')
 
  def test_name(self):
      ok_(bts.NAME==string.replace(type(self).__name__,'Test',''))

  def test_price(self):
      ok_(bts.get_current_price()>0.00)

  def test_bid(self):
      ok_(bts.get_current_bid()>0.00)

  def test_ask(self):
      ok_(bts.get_current_ask()>0.00)

  def test_ticker(self):
      data = json.loads(bts.get_current_ticker())
      ok_(data["pair"]==base.CCY_DEFAULT,"pair should be '%s'" % base.CCY_DEFAULT)
      ok_(data["ask"]>0.00,"ask should not be empty")
      ok_(data["bid"]>0.00,"bid should not be empty")
      ok_(data["bid"]<=data["ask"],"bid should be < ask")
      ok_(float(data["timestamp"])>0,"Timestamp should be greater than zero")

  def test_orders(self):
      ok_(bts.get_current_orders()>0.00)

if __name__ == '__main__':
    nose.runmodule()
