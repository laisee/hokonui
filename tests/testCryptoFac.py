import string
import nose
import json
from nose.tools import ok_
from unittest import TestCase
from context import hokonui
from hokonui.exchanges.cryptofac import CryptoFacility as cfc

class TestCryptoFacility(TestCase):
  
  SYMBOL = 'f-xbt:usd-jun17' 

  def setUp(self):
      print(__name__, ': TestClass.setup_class() ----------')
      
  def tearDown(self):
      print(__name__, ': TestClass.teardown_class() -------')

  def test_price(self):
      self.assertNotEqual(cfc.get_current_price(),0.00)

  def test_bid(self):
      self.assertNotEqual(cfc.get_current_bid(),0.00)

  def test_ask(self):
      print(cfc.get_current_ask())
      self.assertNotEqual(cfc.get_current_ask(),0.00)

  def test_ticker(self):
      data = json.loads(cfc.get_current_ticker())
      ok_(data["pair"]==cfc.CCY_DEFAULT,"pair should be '%s'" % cfc.CCY_DEFAULT)
      ok_(data["ask"]>0.00,"ask should not be empty")
      ok_(data["bid"]>0.00,"bid should not be empty")
      ok_(data["bid"]<=data["ask"],"bid should be <= ask")
      ok_(float(data["timestamp"])>0,"Timestamp should be greater than zero")

  def test_orders(self):
      orders = cfc.get_current_orders(self.SYMBOL)
      ok_(len(orders["asks"])>0, "Asks array should not be empty")
      ok_(len(orders["bids"])>0, "Bids array should not be empty")
      ok_(orders["source"]=="CryptoFacility", "Source should be 'CryptoFacility'")
      ok_(float(orders["timestamp"])>0,"Timestamp should be greater than zero")

if __name__ == '__main__':
    nose.runmodule()
