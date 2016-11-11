import string
import nose
import json
from nose.tools import ok_
from unittest import TestCase
from context import hokonui
from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.bitfinex import Bitfinex as bfx

class TestBitfinex(TestCase):

  def test_name(self):
      ok_(bfx.NAME==string.replace(type(self).__name__,'Test',''))

  def test_price(self):
      ok_(bfx.get_current_price(base.CCY_DEFAULT)>0.00)

  def test_bid(self):
      ok_(bfx.get_current_bid(base.CCY_DEFAULT)>0.00)

  def test_ask(self):
      ok_(bfx.get_current_ask(base.CCY_DEFAULT)>0.00)

  def test_ticker(self):
      data = json.loads(bfx.get_current_ticker(base.CCY_DEFAULT))
      ok_(data["pair"]==base.CCY_DEFAULT,"pair should be '%s'" % base.CCY_DEFAULT)
      ok_(data["ask"]>0.00,"ask should not be empty")
      ok_(data["bid"]>0.00,"bid should not be empty")
      ok_(data["bid"]<=data["ask"],"bid should be < ask")
      ok_(float(data["timestamp"])>0,"Timestamp should be greater than zero")

  def test_orders(self):
      orders = bfx.get_current_orders(base.CCY_DEFAULT)
      ok_(len(orders["asks"])>0, "Asks array should not be empty")
      ok_(len(orders["bids"])>0, "Bids array should not be empty")
      ok_(orders["source"]=="Bitfinex", "Source should be 'Bitfinex'")
      ok_(float(orders["timestamp"])>0,"Timestamp should be greater than zero")
      #raise ValueError(str(orders))

if __name__ == '__main__':
    nosetools.runmodule()
