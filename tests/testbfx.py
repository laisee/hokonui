import nose
from nose.tools import ok_

if __package__ is None:
    import sys
    from os import path
    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
    from exchanges.bitfinex import Bitfinex as bfx
else:
    from ..exchanges.bitstamp import Bitstamp as bts

class TestBitfinex():

  def test_price(self):
      #print 'Ask   ', bfx.get_current_ask()
      ok_(bfx.get_current_price('USD')>0.00)

  def test_bid(self):
      #print 'Bid   ', bfx.get_current_bid()
      ok_(bfx.get_current_bid('USD')>0.00)

  def test_ask(self):
      #print 'Ask   ', bfx.get_current_ask()
      ok_(bfx.get_current_ask('USD')>0.00)

if __name__ == '__main__':
    nosetools.runmodule()
