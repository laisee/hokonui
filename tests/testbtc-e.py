import nose
import string
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

  def test_orders(self):
      orders = btce.get_current_orders('usd')
      ok_(len(orders["Asks"])>0, "Asks array should not be empty")
      ok_(len(orders["Bids"])>0, "Bids array should not be empty")
      ok_(orders["Source"]=="BTCE", "Source should be 'BTCE'")
      ok_(float(orders["Timestamp"])>0,"Timestamp should be greater than zero")
      #raise ValueError(str(orders))
