import string
import nose
import json
from nose.tools import ok_
from unittest import TestCase
from context import hokonui
from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.bitx import BitX as btx

class TestBitX(TestCase):

  TEST_CCY = 'ZAR' 

  def setUp(self):
      print(__name__, ': TestClass.setup_class() ----------')

  def tearDown(self):
      print(__name__, ': TestClass.teardown_class() -------')

  def test_name(self):
      ok_(btx.NAME==string.replace(type(self).__name__,'Test',''))

  def test_price(self):
      ok_(btx.get_current_price(TEST_CCY)>0.00)

  def test_bid(self):
      ok_(btx.get_current_bid(TEST_CCY)>0.00)

  def test_ask(self):
      ok_(btx.get_current_ask(TEST_CCY)>0.00)

  def test_ticker(self):
      data = json.loads(btx.get_current_ticker(TEST_CCY))
      ok_(data["pair"]==base.CCY_DEFAULT,"pair should be '%s'" % TEST_CCY)
      ok_(data["ask"]>0.00,"ask should not be empty")
      ok_(data["bid"]>0.00,"bid should not be empty")
      ok_(data["bid"]<=data["ask"],"bid should be < ask")
      ok_(float(data["timestamp"])>0,"Timestamp should be greater than zero")

  def test_orders(self):
      orders = btx.get_current_orders(TEST_CCY)
      ok_(len(orders["asks"])>0, "Asks array should not be empty")
      ok_(len(orders["bids"])>0, "Bids array should not be empty")
      ok_(orders["source"]=="BitX", "Source should be 'BitX'")
      ok_(float(orders["timestamp"])>0,"Timestamp should be greater than zero")
      #raise ValueError(str(orders))
