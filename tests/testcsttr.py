import string
import nose
from nose.tools import ok_
from unittest import TestCase
from context import hokonui
from hokonui.exchanges.coinsetter import CoinSetter as csttr

class TestCoinSetter(TestCase):

  def setUp(self):
      print(__name__, ': TestClass.setup_class() ----------')

  def tearDown(self):
      print(__name__, ': TestClass.teardown_class() -------')

  def test_name(self):
      ok_(csttr.NAME==string.replace(type(self).__name__,'Test',''))

  def test_price(self):
      #print 'Ask   ', csttr.get_current_ask()
      ok_(csttr.get_current_price()>0.00)

  def test_bid(self):
      #print 'Bid   ', csttr.get_current_bid()
      ok_(csttr.get_current_bid()>0.00)

  def test_ask(self):
      #print 'Ask   ', csttr.get_current_ask()
      ok_(csttr.get_current_ask()>0.00)

  def test_orders(self):
      orders = csttr.get_current_orders()
      ok_(len(orders["Asks"])>0, "Asks array should not be empty")
      ok_(len(orders["Bids"])>0, "Bids array should not be empty")
      ok_(orders["Source"]=="CoinSetter", "Source should be 'CoinSetter'")
      ok_(float(orders["Timestamp"])>0,"Timestamp should be greater than zero")
      #raise ValueError(str(orders))

if __name__ == '__main__':
    nose.runmodule()
