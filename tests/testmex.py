import nose
from nose.tools import ok_
import os, sys

if __package__ is None:
    import sys
    from os import path
    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
    from exchanges.mexbtc import MexBtc
else:
    from ..exchanges.mexbtc import MexBtc

class TestMex():
  
  def setup_func():
    "set up test fixtures"

  def teardown_func():
    "tear down test fixtures"

  def test_price(self):
      #print 'Ask   ', MexBtc.get_current_ask()
      ok_(MexBtc.get_current_price() > 0.00)

  def test_bid(self):
      #print 'Bid   ', MexBtc.get_current_bid()
      ok_(MexBtc.get_current_bid() > 0.00)

  def test_ask(self):
      #print 'Ask   ', MexBtc.get_current_ask()
      ok_(MexBtc.get_current_ask() > 0.00)

if __name__ == '__main__':
    nose.runmodule()
