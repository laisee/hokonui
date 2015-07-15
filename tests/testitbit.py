import nose
from nose.tools import ok_
from unittest import TestCase

if __package__ is None:
    import sys
    from os import path
    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
    from exchanges.itbit import Itbit as itb
else:
    from ..exchanges.itbit import Itbit as itb

class TestBitstamp(TestCase):

  def setUp(self):
      print(__name__, ': TestClass.setup_class() ----------')

  def tearDown(self):
      print(__name__, ': TestClass.teardown_class() -------')

  def test_price(self):
      #print 'Ask   ', itb.get_current_ask()
      ok_(itb.get_current_price('USD')>0.00)

  def test_bid(self):
      print(__name__)
      #print 'Bid   ', itb.get_current_bid()
      ok_(itb.get_current_bid('USD')>0.00)

  def test_ask(self):
      print(__name__)
      #print 'Ask   ', itb.get_current_ask()
      ok_(itb.get_current_ask('USD')>0.00)

if __name__ == '__main__':
    nosetest.runmodule()
