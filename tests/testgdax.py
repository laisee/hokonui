''' Module for testing GDAX API '''

from tests import *

libPath = '../hokonui'
if not libPath in sys.path: sys.path.append(libPath)

from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.gdax import GDAX as gdx


class Testgdax(TestCase):
    ''' Class for executing test on GDAX API '''

    @classmethod
    def setUp(cls):
        ''' test setup '''
        print(__name__, ': TestClass.setup_class() ----------')

    @classmethod
    def tearDown(cls):
        ''' test setup '''
        print(__name__, ': TestClass.teardown_class() -------')

    @classmethod
    def test_name(cls):
        ''' test name '''
        ok_(gdx.NAME == cls.__name__.replace('Test', ''))

    @classmethod
    def test_price(cls):
        ''' method  for testing last price '''
        ok_(float(gdx.get_current_price(base.CCY_DEFAULT)) > 0.00)

    @classmethod
    def test_bid(cls):
        ''' method for testing bid price  '''
        ok_(float(gdx.get_current_bid(base.CCY_DEFAULT)) > 0.00)

    @classmethod
    def test_ask(cls):
        ''' method for testing ask price  '''
        ok_(float(gdx.get_current_ask(base.CCY_DEFAULT)) > 0.00)

    @classmethod
    def test_ticker(cls):
        ''' method for testing ticker '''
        data = json.loads(gdx.get_current_ticker(base.CCY_DEFAULT))
        ok_(data["pair"] == base.CCY_DEFAULT, "shd be '%s'" % base.CCY_DEFAULT)
        ok_(float(data["ask"]) > 0.00, "ask should not be empty")
        ok_(float(data["bid"]) > 0.00, "bid should not be empty")
        ok_(float(data["bid"]) <= float(data["ask"]), "bid should be < ask")
        ok_(float(data["timestamp"]) > 0, "Timestamp should be > zero")

    @classmethod
    def test_orders(cls):
        ''' method for testing orders '''
        orders = gdx.get_current_orders(base.CCY_DEFAULT)
        ok_(len(orders["asks"]) > 0, "Asks array should not be empty")
        ok_(len(orders["bids"]) > 0, "Bids array should not be empty")
        ok_(orders["source"] == "gdax", "Source should be 'gdax'")
        ok_(float(orders["timestamp"]) > 0, "Timestamp should be > zero")

if __name__ == '__main__':
    nose.runmodule()
