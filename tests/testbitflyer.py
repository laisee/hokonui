import string
import nose
import json
from nose.tools import ok_
from unittest import TestCase
from context import hokonui
from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.bitflyer import BitFlyer as btf

class TestBitFlyer(TestCase):

  TEST_CCY = "BTC_JPY"

  def setUp(self):
      print(__name__, ': TestClass.setup_class() ----------')

  def tearDown(self):
      print(__name__, ': TestClass.teardown_class() -------')

  def test_name(self):
      ok_(btf.NAME==string.replace(type(self).__name__,'Test',''))

  def test_price(self):
      ok_(btf.get_current_price(TEST_CCY)>0.00)

  def test_bid(self):
      ok_(btf.get_current_bid(TEST_CCY)>0.00)

  def test_ask(self):
      ok_(btf.get_current_ask(TEST_CCY)>0.00)

  def test_ticker(self):
      data = json.loads(btf.get_current_ticker(TEST_CCY))
      ok_(data["pair"]==base.CCY_DEFAULT,"pair should be '%s'" % base.CCY_DEFAULT)
      ok_(data["ask"]>0.00,"ask should not be empty")
      ok_(data["bid"]>0.00,"bid should not be empty")
      ok_(data["bid"]<=data["ask"],"bid should be < ask")
      ok_(float(data["timestamp"])>0,"Timestamp should be greater than zero")

  def test_orders(self):
      orders = btf.get_current_orders(TEST_CCY)
      ok_(len(orders["asks"])>0, "Asks array should not be empty")
      ok_(len(orders["bids"])>0, "Bids array should not be empty")
      ok_(orders["source"]=="BitFlyer", "Source should be 'BitFlyer'")
      ok_(float(orders["timestamp"])>0,"Timestamp should be greater than zero")
      #raise ValueError(str(orders))
