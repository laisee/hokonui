import string
import nose
from nose.tools import ok_
from unittest import TestCase

if __package__ is None:
    import sys
    from os import path
    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
    from exchanges.bitfinex import Bitfinex as bfx
else:
    from ..exchanges.bitfinex import Bitfinex as bfx

class TestBitfinex(TestCase):

  def test_name(self):
      ok_(bfx.NAME==string.replace(type(self).__name__,'Test',''))

  def test_price(self):
      #print 'Ask   ', bfx.get_current_ask()
      ok_(bfx.get_current_price('USD')>0.00)

  def test_bid(self):
      #print 'Bid   ', bfx.get_current_bid()
      ok_(bfx.get_current_bid('USD')>0.00)

  def test_ask(self):
      #print 'Ask   ', bfx.get_current_ask()
      ok_(bfx.get_current_ask('USD')>0.00)

  def test_orders(self):
      orders = bfx.get_current_orders(None,20)
      ok_(len(orders["Asks"])>0, "Asks array should not be empty")
      ok_(len(orders["Bids"])>0, "Bids array should not be empty")
      ok_(orders["Source"]=="Bitfinex", "Source should be 'Bitfinex'")
      ok_(float(orders["Timestamp"])>0,"Timestamp should be greater than zero")
      #raise ValueError(str(orders))

if __name__ == '__main__':
    nosetools.runmodule()
