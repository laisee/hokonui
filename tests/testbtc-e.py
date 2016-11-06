import nose
import string
import json
from nose.tools import ok_
from unittest import TestCase
from context import hokonui
from hokonui.exchanges.btce import BTCE as btce

class TestBTCE(TestCase):

  def setUp(self):
      print(__name__, ': TestClass.setup_class() ----------')

  def tearDown(self):
      print(__name__, ': TestClass.teardown_class() -------')

  def test_name(self):
      ok_(btce.NAME==string.replace(type(self).__name__,'Test',''))

  def test_price(self):
      ok_(btce.get_current_price('usd')>0.00)

  def test_bid(self):
      ok_(btce.get_current_bid('usd')>0.00)

  def test_ask(self):
      ok_(btce.get_current_ask('usd')>0.00)

  def test_ask_GT_bid(self):
      bid = btce.get_current_bid('usd') 
      ask = btce.get_current_ask('usd')
      ok_(bid > ask,"bid should be > ask - Bid : %s Ask %s " % (bid,ask))

  def test_ticker(self):
      data = json.loads(btce.get_current_ticker('usd'))
      bid = btce.get_current_bid('usd') 
      ask = btce.get_current_ask('usd')
      ok_(data["pair"]=='USD',"pair should be 'USD'")
      ok_(ask>0.00,"ask should not be empty")
      ok_(bid>0.00,"bid should not be empty")
      ok_(bid > ask,"bid should be > ask - Bid : %s Ask %s " % (bid,ask))
      ok_(float(data["timestamp"])>0,"Timestamp should be greater than zero")

  def test_orders(self):
      orders = btce.get_current_orders('usd')
      ok_(len(orders["asks"])>0, "Asks array should not be empty")
      ok_(len(orders["bids"])>0, "Bids array should not be empty")
      ok_(orders["source"]=="BTCE", "Source should be 'BTCE'")
      ok_(float(orders["timestamp"])>0,"Timestamp should be greater than zero")
      #raise ValueError(str(orders))
