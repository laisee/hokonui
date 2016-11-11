import string
import nose
import json
from nose.tools import ok_
from unittest import TestCase
from context import hokonui

from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.okcoin import OKCoin as okc

class TestOkCoin(TestCase):

  def test_price(self):
      self.assertNotEqual(okc.get_current_price(),0.00)

  def test_bid(self):
      self.assertNotEqual(okc.get_current_bid(),0.00)

  def test_ask(self):
      self.assertNotEqual(okc.get_current_ask(),0.00)

  def test_ticker(self):
      data = json.loads(okc.get_current_ticker())
      ok_(data["pair"]==base.CCY_DEFAULT,"pair should be '%s'" % base.CCY_DEFAULT )
      ok_(data["ask"]>0.00,"ask should not be empty")
      ok_(data["bid"]>0.00,"bid should not be empty")
      ok_(data["bid"]<=data["ask"],"bid should be <= ask")
      ok_(float(data["timestamp"])>0,"Timestamp should be greater than zero")

  def test_orders(self):
      orders = okc.get_current_orders()
      ok_(len(orders["asks"])>0, "Asks array should not be empty")
      ok_(len(orders["bids"])>0, "Bids array should not be empty")
      ok_(orders["source"]=="OKCoin", "Source should be 'OKCoin'")
      ok_(float(orders["timestamp"])>0,"Timestamp should be greater than zero")

if __name__ == '__main__':
    nose.runmodule()
