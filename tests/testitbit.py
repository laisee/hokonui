import string
import nose
from nose.tools import ok_
from unittest import TestCase
from context import hoko
from hoko.exchanges.itbit import Itbit as itb

class TestItbit(TestCase):

  def setUp(self):
      print(__name__, ': TestClass.setup_class() ----------')

  def tearDown(self):
      print(__name__, ': TestClass.teardown_class() -------')

  def test_name(self):
      ok_(itb.NAME==string.replace(type(self).__name__,'Test',''))

  def test_price(self):
      #print 'Ask   ', itb.get_current_ask()
      ok_(itb.get_current_price('USD')>0.00)

  def test_bid(self):
      #print 'Bid   ', itb.get_current_bid()
      ok_(itb.get_current_bid('USD')>0.00)

  def test_ask(self):
      #print 'Ask   ', itb.get_current_ask()
      ok_(itb.get_current_ask('USD')>0.00)

  def test_orders(self):
      orders = itb.get_current_orders('USD')
      ok_(len(orders["Asks"])>0, "Asks array should not be empty")
      ok_(len(orders["Bids"])>0, "Bids array should not be empty")
      ok_(orders["Source"]=="ITBIT", "Source should be 'ITBIT'")
      ok_(float(orders["Timestamp"])>0,"Timestamp should be greater than zero")
      #raise ValueError(str(orders))

if __name__ == '__main__':
    nose.runmodule()
