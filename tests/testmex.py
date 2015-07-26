import nose
from nose.tools import ok_
import string
from unittest import TestCase
from context import hokonui
from hokonui.exchanges.mexbtc import MexBtc as mex

class TestMexBtc(TestCase):
  
  def setup_func():
    "set up test fixtures"

  def teardown_func():
    "tear down test fixtures"

  def test_name(self):
      ok_(mex.NAME==string.replace(type(self).__name__,'Test',''))

  def test_price(self):
      ok_(mex.get_current_price() > 0.00)

  def test_bid(self):
      ok_(mex.get_current_bid() > 0.00)

  def test_ask(self):
      ok_(mex.get_current_ask() > 0.00)

  def test_orders(self):
      orders = mex.get_current_orders()
      ok_(len(orders["asks"])>0, "Asks array should not be empty")
      ok_(len(orders["bids"])>0, "Bids array should not be empty")
      ok_(orders["source"]=="MexBtc", "Source should be 'MexBtc'")
      ok_(float(orders["timestamp"])>0,"Timestamp should be greater than zero")
      #raise ValueError(str(orders))

if __name__ == '__main__':
    nose.runmodule()
