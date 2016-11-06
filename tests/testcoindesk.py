import nose
import string
from unittest import TestCase
from nose.tools import ok_
from context import hokonui
from hokonui.exchanges.coindesk import CoinDesk as coin 

class TestCoinDesk(TestCase):

  def test_name(self):
      ok_(coin.NAME==string.replace(type(self).__name__,'Test',''))

  def test_price(self):
      ok_(coin.get_current_price()>0.00)

  def test_past_price(self):
      ok_(coin.get_past_price('2015-07-05')>0.00)

if __name__ == '__main__':
    nosetool.runmodule()
