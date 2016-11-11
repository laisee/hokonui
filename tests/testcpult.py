import string
import nose
from nose.tools import ok_
from unittest import TestCase
from context import hokonui
from hokonui.exchanges.base import Exchange as base 
from hokonui.exchanges.coinapult import Coinapult as cplt 

class TestCoinapult(TestCase):

  def test_name(self):
      ok_(cplt.NAME==string.replace(type(self).__name__,'Test',''))

  def test_price(self):
      ok_(cplt.get_current_price(base.CCY_DEFAULT)>0.00)

  def test_bid(self):
      ok_(cplt.get_current_bid(base.CCY_DEFAULT)>0.00)

  def test_ask(self):
      ok_(cplt.get_current_ask(base.CCY_DEFAULT)>0.00)


  def test_bif_gt_ask(self):
      ok_(cplt.get_current_bid(base.CCY_DEFAULT) <= cplt.get_current_ask(base.CCY_DEFAULT), "bid should be < ask")

if __name__ == '__main__':
    unittest.main()
