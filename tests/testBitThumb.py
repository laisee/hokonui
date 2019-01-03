''' Module for testing Binance exchange '''

from tests import *

libPath = '../hokonui'
if not libPath in sys.path: sys.path.append(libPath)

from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.binance import Binance as bin


class TestBitThumb(TestCase):
    ''' Class for testing Binance exchange '''

    @classmethod
    @docparams(bin.__name__,"setup")
    def setUp(cls):
        ''' {0}.{1}'''
        print(__name__, ': TestClass.setup_class() ----------')

    @classmethod
    @docparams(bin.__name__,"teardown")
    def tearDown(cls):
        ''' {0}.{1}'''
        print(__name__, ': TestClass.teardown_class() -------')

    @classmethod
    @docparams(bin.__name__,"name")
    @unittest.skip("skip while creating Binance API calls ")
    def test_name(cls):
        ''' {0}.{1} '''
        ok_(bin.NAME == cls.__name__.replace( 'Test', ''))

    @classmethod
    @docparams(bin.__name__,"price")
    @unittest.skip("skip while creating Binance API calls ")
    def test_price(cls):
        ''' {0}.{1} '''
        ok_(float(bin.get_current_price(bin.CCY_DEFAULT)) > 0.00)

    @classmethod
    @docparams(bin.__name__,"bid")
    @unittest.skip("skip while creating Binance API calls ")
    def test_bid(cls):
        ''' {0}.{1} '''
        ok_(float(bin.get_current_bid(bin.CCY_DEFAULT)) > 0.00)

    @classmethod
    @docparams(bin.__name__,"ask")
    @unittest.skip("skip while creating Binance API calls ")
    def test_ask(cls):
        ''' {0}.{1} '''
        ok_(float(bin.get_current_ask(bin.CCY_DEFAULT)) > 0.00)

    @classmethod
    @docparams(bin.__name__,"ticker")
    @unittest.skip("skip while creating Binance API calls ")
    def test_ticker(cls):
        ''' {0}.{1} '''
        data = json.loads(bin.get_current_ticker(bin.CCY_DEFAULT))
        ok_(data["pair"] == bin.CCY_DEFAULT, "shd be '%s'" % bin.CCY_DEFAULT)
        ok_(float(data["ask"]) > 0.00, "ask should not be empty")
        ok_(float(data["bid"]) > 0.00, "bid should not be empty")
        ok_(float(data["bid"]) <= float(data["ask"]), "bid should be < ask")
        ok_(float(data["timestamp"]) > 0, "Timestamp should be > zero")

    @classmethod
    @docparams(bin.__name__,"orders")
    @unittest.skip("skip while creating Binance API calls ")
    def test_orders(cls):
        ''' {0}.{1} '''
        orders = bin.get_current_orders(bin.CCY_DEFAULT)
        ok_(len(orders["asks"]) > 0, "Asks array should not be empty")
        ok_(len(orders["bids"]) > 0, "Bids array should not be empty")
        ok_(orders["source"] == "Binance", "Source should be 'Binance'")
        ok_(float(orders["timestamp"]) > 0, "Timestamp should be > zero")

if __name__ == '__main__':
    nose.runmodule()
