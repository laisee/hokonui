import nose
from nose.tools import ok_

if __package__ is None:
    import sys
    from os import path
    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
    from exchanges.coinapult import Coinapult as cplt 
else:
    from ..exchanges.coinapult import Coinapult as cplt 

class TestCoinapult():

  def test_price(self):
      #print 'Ask   ', cplt.get_current_ask()
      ok_(cplt.get_current_price('USD')>0.00)

  def test_bid(self):
      #print 'Bid   ', cplt.get_current_bid()
      ok_(cplt.get_current_bid('USD')>0.00)

  def test_ask(self):
      #print 'Ask   ', cplt.get_current_ask()
      ok_(cplt.get_current_ask('USD')>0.00)

if __name__ == '__main__':
    unittest.main()
