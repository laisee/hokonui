import string
import nose
import json
from nose.tools import ok_
from unittest import TestCase
from context import hokonui
from hokonui.exchanges.bitcoinavg import BitcoinAverage as avg

class TestBitcoinAverage(TestCase):

  def setUp(self):
      print(__name__, ': TestClass.setup_class() ----------')

  def tearDown(self):
      print(__name__, ': TestClass.teardown_class() -------')

  def test_name(self):
      ok_(avg.NAME==string.replace(type(self).__name__,'Test',''))

  def test_price(self):
      ok_(avg.get_current_price('USD')>0.00)

  def test_bid(self):
      ok_(avg.get_current_bid('USD')>0.00)

  def test_ask(self):
      ok_(avg.get_current_ask('USD')>0.00)

  def test_ticker(self):
      data = json.loads(avg.get_current_ticker('USD'))
      print data
      ok_(data["pair"]=='USD',"pair should be 'USD'")
      ok_(data["ask"]>0.00,"ask should not be empty")
      ok_(data["bid"]>0.00,"bid should not be empty")
      ok_(data["bid"]<=data["ask"],"bid should be < ask")
      ok_(float(data["timestamp"])>0,"Timestamp should be greater than zero")

  def test_volume(self):
      vol = avg.get_current_volume('USD')
      ok_(float(vol["quantity"])>=0, "quantity should not be empty and should be valid number >= 0")
      print str(vol)
      ok_(vol["source"]=="BitcoinAverage", "Source should be 'BitcoinAverage'")
      ok_(float(vol["timestamp"])>0,"Timestamp should be greater than zero")
