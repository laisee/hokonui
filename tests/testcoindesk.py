import nose
import string
from unittest import TestCase
from nose.tools import ok_

if __package__ is None:
    import sys
    from os import path
    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
    from exchanges.coindesk import CoinDesk as coin 
else:
    from ..exchanges.coindesk import CoinDesk as coin 

class TestCoinDesk(TestCase):

  def test_name(self):
      ok_(coin.NAME==string.replace(type(self).__name__,'Test',''))

  def test_price(self):
      #print 'Ask   ', coin.get_current_ask()
      ok_(coin.get_current_price()>0.00)

  def test_past_price(self):
      #print 'Ask   ', coin.get_current_ask()
      ok_(coin.get_past_price('2015-07-05')>0.00)

if __name__ == '__main__':
    nosetool.runmodule()
