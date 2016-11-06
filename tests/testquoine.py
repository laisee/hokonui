import string
import nose
import json
from nose.tools import ok_
from unittest import TestCase
from context import hokonui
from hokonui.exchanges.quoine import Quoine as q

class TestQuoine(TestCase):

  def setUp(self):
      print(__name__, ': TestClass.setup_class() ----------')

  def tearDown(self):
      print(__name__, ': TestClass.teardown_class() -------')

  def test_name(self):
      ok_(q.NAME==string.replace(type(self).__name__,'Test',''))

  def test_price(self):
      ok_(q.get_current_price('USD')>0.00)

  def test_bid(self):
      ok_(q.get_current_bid('USD')>0.00)

  def test_ask(self):
      ok_(q.get_current_ask('USD')>0.00)

  def test_ticker(self):
      data = json.loads(q.get_current_ticker('USD'))
      ok_(data["pair"]=='USD',"pair should be 'USD'")
      ok_(data["ask"]>0.00,"ask should not be empty")
      ok_(data["bid"]>0.00,"bid should not be empty")
      ok_(data["bid"]<=data["ask"],"bid should be < ask")
      ok_(float(data["timestamp"])>0,"Timestamp should be greater than zero")

  def test_orders(self):
      ccy_id = self.Ccy2Id('USD')
      orders = q.get_current_orders(ccy_id)
      ok_(len(orders["asks"])>0, "Asks array should not be empty")
      ok_(len(orders["bids"])>0, "Bids array should not be empty")
      ok_(orders["source"]=="Quoine", "Source should be 'Quoine'")
      ok_(float(orders["timestamp"])>0,"Timestamp should be greater than zero")
      #raise ValueError(str(orders))

  @staticmethod
  def Ccy2Id(ccy):
     id = -1
     if ccy == 'USD':
        id = 1
     elif ccy == 'EUR':
        id = 3
     elif ccy == 'JPY':
        id = 5
     elif ccy == 'SGD':
        id = 7
     elif ccy == 'HKD':
        id = 9
     elif ccy == 'IDR':
        id = 11
     elif ccy == 'AUD':
        id = 13
     elif ccy == 'PHP':
        id = 15
     elif ccy == 'CNY':
        id = 17
     elif ccy == 'INR':
        id = 18
     else:
        raise ValueError("Invalid Currency : %s " % ccy )
     return id

if __name__ == '__main__':
    nose.runmodule()
