import string
import nose
from nose.tools import ok_
from unittest import TestCase
from context import hokonui
from hokonui.exchanges.coinapult import Coinapult as cplt 

class TestCoinapult(TestCase):

  def test_name(self):
      ok_(cplt.NAME==string.replace(type(self).__name__,'Test',''))

  def test_price(self):
      ok_(cplt.get_current_price('USD')>0.00)

  def test_bid(self):
      ok_(cplt.get_current_bid('USD')>0.00)

  def test_ask(self):
      ok_(cplt.get_current_ask('USD')>0.00)

if __name__ == '__main__':
    unittest.main()
