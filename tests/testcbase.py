import nose
import string
from nose.tools import ok_
from unittest import TestCase
from context import hoko
from hoko.exchanges.coinbase import CoinBase as cba

class TestCoinBase(TestCase):

  def setUp(self):
      print(__name__, ': TestClass.setup_class() ----------')

  def tearDown(self):
      print(__name__, ': TestClass.teardown_class() -------')

  def test_name(self):
      ok_(cba.NAME==string.replace(type(self).__name__,'Test',''))

  def test_price(self):
      ok_(cba.get_current_price('USD','ticker')>0.00)

  def test_bid(self):
      ok_(cba.get_current_bid('USD','book')>0.00)

  def test_ask(self):
      ok_(cba.get_current_ask('USD','book')>0.00)

  def test_orders(self):
      orders = cba.get_current_orders('USD')
      ok_(len(orders["Asks"])>0, "Asks array should not be empty")
      ok_(len(orders["Bids"])>0, "Bids array should not be empty")
      ok_(orders["Source"]=="CoinBase", "Source should be 'CoinBase'")
      ok_(float(orders["Timestamp"])>0,"Timestamp should be greater than zero")
      #raise ValueError(str(orders))
