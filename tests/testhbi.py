import nose
from nose.tools import ok_

if __package__ is None:
    import sys
    from os import path
    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
    from exchanges.huobi import Huobi as hbi 
else:
    from ..exchanges.huobi import Huobi as hbi 

class TestHuobi():

  def test_price(self):
      #print 'Ask   ', hbi.get_current_ask()
      ok_(hbi.get_current_price()>0.00)

  def test_bid(self):
      #print 'Bid   ', hbi.get_current_bid()
      ok_(hbi.get_current_bid()>0.00)

  def test_ask(self):
      #print 'Ask   ', hbi.get_current_ask()
      ok_(hbi.get_current_ask()>0.00)

if __name__ == '__main__':
    unittest.main()
