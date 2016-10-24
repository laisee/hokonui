import string
import nose
import json
from nose.tools import ok_
from unittest import TestCase
from context import hokonui
from hokonui.exchanges.kraken import Kraken as kraken

class TestKraken(TestCase):

  def setUp(self):
      print(__name__, ': TestClass.setup_class() ----------')

  def tearDown(self):
      print(__name__, ': TestClass.teardown_class() -------')

  def test_name(self):
      ok_(kraken.NAME==string.replace(type(self).__name__,'Test',''))

  def test_price(self):
      body = '{"pair":"XXBTZJPY"}'
      ok_(kraken.get_current_price(None,None,body)>0.00)

  def test_bid(self):
      body = '{"pair":"XXBTZJPY"}'
      ok_(kraken.get_current_bid(None,None,body)>0.00)

  def test_ask(self):
      body = '{"pair":"XXBTZJPY"}'
      ok_(kraken.get_current_ask(None,None,body)>0.00)

  def test_ticker(self):
      body = '{"pair":"XXBTZJPY"}'
      data = json.loads(kraken.get_current_ticker(None,None,body))
      ok_(data["pair"]=='XXBTZJPY',"pair should be 'XXBTZJPY'")
      ok_(data["ask"]>0.00,"ask should not be empty")
      ok_(data["bid"]>0.00,"bid should not be empty")
      ok_(float(data["timestamp"])>0,"Timestamp should be greater than zero")

  def test_orders(self):
      body = '{"pair":"XXBTZJPY","count":"10"}'
      orders = kraken.get_current_orders(None,None,body,25)
      print orders
      ok_(len(orders["asks"])>0, "Asks array should not be empty")
      ok_(len(orders["bids"])>0, "Bids array should not be empty")
      ok_(orders["source"]=="Kraken", "Source should be 'Kraken'")
      ok_(float(orders["timestamp"])>0,"Timestamp should be greater than zero")

if __name__ == '__main__':
    nose.runmodule()
