import string
import nose
import json
from nose.tools import ok_
from unittest import TestCase
from context import hokonui
from hokonui.exchanges.huobi import Huobi as hbi 

class TestHuobi(TestCase):

  def test_name(self):
      ok_(hbi.NAME==string.replace(type(self).__name__,'Test',''))

  def test_price(self):
      #print 'Ask   ', hbi.get_current_ask()
      ok_(hbi.get_current_price()>0.00)

  def test_bid(self):
      #print 'Bid   ', hbi.get_current_bid()
      ok_(hbi.get_current_bid()>0.00)

  def test_ask(self):
      ok_(hbi.get_current_ask()>0.00)


  def test_ticker(self):
      data = json.loads(hbi.get_current_ticker())
      ok_(data["pair"]=='USD',"pair should be 'USD'")
      ok_(data["ask"]>0.00,"ask should not be empty")
      ok_(data["bid"]>0.00,"bid should not be empty")
      ok_(float(data["timestamp"])>0,"Timestamp should be greater than zero")

  def test_orders(self):
      orders = hbi.get_current_orders(None,20)
      ok_(len(orders["asks"])>0, "Asks array should not be empty")
      ok_(len(orders["bids"])>0, "Bids array should not be empty")
      ok_(orders["source"]=="Huobi", "Source should be 'Huobi'")
      ok_(float(orders["timestamp"])>0,"Timestamp should be greater than zero")

if __name__ == '__main__':
    unittest.main()
